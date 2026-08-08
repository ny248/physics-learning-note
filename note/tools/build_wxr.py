#!/usr/bin/env python3
"""Build a one-article WXR file accepted by note's article importer.

The importer preserves TeX source as article text, but it does not reliably
reconstruct note's formula blocks. Formula rendering must be verified and, when
necessary, restored in the note editor after import.
"""

from __future__ import annotations

import argparse
import html
import re
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path


def inline_html(text: str) -> str:
    """Escape a Markdown text line and retain the small inline subset in use."""
    parts = re.split(r"(\*\*.*?\*\*)", text)
    converted: list[str] = []
    for part in parts:
        if part.startswith("**") and part.endswith("**"):
            converted.append(
                f"<strong>{html.escape(part[2:-2], quote=False)}</strong>"
            )
        else:
            converted.append(html.escape(part, quote=False))
    return "".join(converted)


def markdown_body_to_html(lines: list[str]) -> tuple[str, str]:
    """Convert the article's constrained Markdown subset to note-friendly HTML."""
    if not lines or not lines[0].startswith("# "):
        raise ValueError("The source must begin with one level-1 title.")

    title = lines[0][2:].strip()
    body = lines[1:]
    blocks: list[str] = []
    paragraph: list[str] = []
    list_kind: str | None = None
    list_items: list[str] = []
    display_math: list[str] | None = None

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            # Lines wrapped for source readability belong to the same paragraph.
            blocks.append(f"<p>{''.join(inline_html(line) for line in paragraph)}</p>")
            paragraph = []

    def flush_list() -> None:
        nonlocal list_kind, list_items
        if list_kind is not None:
            items = "".join(f"<li>{inline_html(item)}</li>" for item in list_items)
            blocks.append(f"<{list_kind}>{items}</{list_kind}>")
            list_kind = None
            list_items = []

    for line_number, line in enumerate(body, start=2):
        if display_math is not None:
            if line == "$$":
                escaped = "\n".join(
                    html.escape(math_line, quote=False)
                    for math_line in display_math
                )
                # Keep note's display-math delimiters and TeX body on literal,
                # independent lines. Using <br /> here can lose line boundaries
                # when an importer reads DOM textContent.
                blocks.append(f"<p>$$\n{escaped}\n$$</p>")
                display_math = None
            else:
                display_math.append(line)
            continue

        if line == "$$":
            flush_paragraph()
            flush_list()
            display_math = []
            continue

        if not line:
            flush_paragraph()
            flush_list()
            continue

        if line == "---":
            flush_paragraph()
            flush_list()
            blocks.append("<hr />")
            continue

        heading = re.fullmatch(r"(#{2,3}) (.+)", line)
        if heading:
            flush_paragraph()
            flush_list()
            level = len(heading.group(1))
            if "$$" in heading.group(2):
                raise ValueError(
                    f"note does not support formula notation in headings: "
                    f"line {line_number}"
                )
            blocks.append(
                f"<h{level}>{inline_html(heading.group(2))}</h{level}>"
            )
            continue

        ordered_item = re.fullmatch(r"\d+\. (.+)", line)
        unordered_item = re.fullmatch(r"- (.+)", line)
        if ordered_item or unordered_item:
            flush_paragraph()
            requested_kind = "ol" if ordered_item else "ul"
            if list_kind not in (None, requested_kind):
                flush_list()
            list_kind = requested_kind
            match = ordered_item or unordered_item
            assert match is not None
            list_items.append(match.group(1))
            continue

        quote = re.fullmatch(r"> (.+)", line)
        if quote:
            flush_paragraph()
            flush_list()
            blocks.append(
                f"<blockquote><p>{inline_html(quote.group(1))}</p></blockquote>"
            )
            continue

        paragraph.append(line)

    if display_math is not None:
        raise ValueError("The source contains an unclosed display formula.")
    flush_paragraph()
    flush_list()
    return title, "\n".join(blocks)


def build_wxr(
    title: str,
    article_html: str,
    *,
    slug: str,
    post_date: date,
) -> str:
    """Wrap one HTML article in the WordPress 1.2 WXR interchange format."""
    if "]]>" in title or "]]>" in article_html:
        raise ValueError("CDATA terminator is not allowed in the article.")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError("The slug must contain lowercase ASCII words and hyphens.")

    jst = timezone(timedelta(hours=9))
    local_datetime = datetime.combine(post_date, time(12, 0), tzinfo=jst)
    utc_datetime = local_datetime.astimezone(timezone.utc)
    pub_date = utc_datetime.strftime("%a, %d %b %Y %H:%M:%S +0000")
    local_mysql = local_datetime.strftime("%Y-%m-%d %H:%M:%S")
    utc_mysql = utc_datetime.strftime("%Y-%m-%d %H:%M:%S")
    date_key = post_date.strftime("%Y%m%d")

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
  xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"
  xmlns:content="http://purl.org/rss/1.0/modules/content/"
  xmlns:wfw="http://wellformedweb.org/CommentAPI/"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:wp="http://wordpress.org/export/1.2/">
  <channel>
    <title>Physics Articles</title>
    <link>https://example.invalid/physics</link>
    <description>Physics article import data</description>
    <pubDate>{pub_date}</pubDate>
    <language>ja</language>
    <wp:wxr_version>1.2</wp:wxr_version>
    <wp:base_site_url>https://example.invalid/physics</wp:base_site_url>
    <wp:base_blog_url>https://example.invalid/physics</wp:base_blog_url>
    <item>
      <title><![CDATA[{title}]]></title>
      <link>https://example.invalid/physics/{slug}</link>
      <pubDate>{pub_date}</pubDate>
      <dc:creator><![CDATA[author]]></dc:creator>
      <guid isPermaLink="false">physics-{slug}-{date_key}</guid>
      <description></description>
      <content:encoded><![CDATA[
{article_html}
]]></content:encoded>
      <excerpt:encoded><![CDATA[]]></excerpt:encoded>
      <wp:post_id>1</wp:post_id>
      <wp:post_date><![CDATA[{local_mysql}]]></wp:post_date>
      <wp:post_date_gmt><![CDATA[{utc_mysql}]]></wp:post_date_gmt>
      <wp:comment_status><![CDATA[closed]]></wp:comment_status>
      <wp:ping_status><![CDATA[closed]]></wp:ping_status>
      <wp:post_name><![CDATA[{slug}]]></wp:post_name>
      <wp:status><![CDATA[draft]]></wp:status>
      <wp:post_parent>0</wp:post_parent>
      <wp:menu_order>0</wp:menu_order>
      <wp:post_type><![CDATA[post]]></wp:post_type>
      <wp:post_password><![CDATA[]]></wp:post_password>
      <wp:is_sticky>0</wp:is_sticky>
      <category domain="category" nicename="physics"><![CDATA[物理学]]></category>
    </item>
  </channel>
</rss>
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--post-date", type=date.fromisoformat, required=True)
    args = parser.parse_args()

    source_lines = args.source.read_text(encoding="utf-8").splitlines()
    title, article_html = markdown_body_to_html(source_lines)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        build_wxr(
            title,
            article_html,
            slug=args.slug,
            post_date=args.post_date,
        ),
        encoding="utf-8",
    )
    print(args.output)
    print(
        "warning: note may import TeX delimiters as plain text; "
        "verify formulas in the imported draft"
    )


if __name__ == "__main__":
    main()
