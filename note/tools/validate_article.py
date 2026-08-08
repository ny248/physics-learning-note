#!/usr/bin/env python3
"""Validate one note Markdown source against its generated WXR file."""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


CONTENT_NAMESPACE = "http://purl.org/rss/1.0/modules/content/"
WP_NAMESPACE = "http://wordpress.org/export/1.2/"


def extract_source_formulas(source: str) -> tuple[list[str], list[str]]:
    display = re.findall(r"(?ms)^\$\$\n(.*?)\n\$\$$", source)
    inline = re.findall(r"\$\$\{(.*?)\}\$\$", source)
    delimiter_count = len(re.findall(r"(?m)^\$\$$", source))
    if delimiter_count != 2 * len(display):
        raise ValueError("Display-math delimiters are unbalanced or malformed.")
    return display, inline


def validate_wxr(source: str, xml_path: Path, slug: str) -> tuple[int, int]:
    root = ET.parse(xml_path).getroot()
    item = root.find("./channel/item")
    if item is None:
        raise ValueError("The WXR file does not contain one article item.")

    payload = item.findtext(f"{{{CONTENT_NAMESPACE}}}encoded")
    if payload is None:
        raise ValueError("The WXR article body is missing.")

    source_lines = source.splitlines()
    if not source_lines or not source_lines[0].startswith("# "):
        raise ValueError("The Markdown source has no level-1 title.")
    title = source_lines[0][2:]
    if item.findtext("title") != title:
        raise ValueError("The Markdown and WXR titles differ.")

    post_name = item.findtext(f"{{{WP_NAMESPACE}}}post_name")
    if post_name != slug:
        raise ValueError(f"Unexpected WXR slug: {post_name!r}")

    source_headings = re.findall(r"(?m)^(#{2,3}) (.+)$", source)
    xml_headings = [
        ("#" * int(level), html.unescape(text))
        for level, text in re.findall(r"<h([23])>(.*?)</h\1>", payload)
    ]
    if source_headings != xml_headings:
        raise ValueError("The Markdown and WXR heading outlines differ.")

    source_display, source_inline = extract_source_formulas(source)
    xml_display = [
        html.unescape(formula)
        for formula in re.findall(r"(?ms)<p>\$\$\n(.*?)\n\$\$</p>", payload)
    ]
    xml_inline = [
        html.unescape(formula)
        for formula in re.findall(r"\$\$\{(.*?)\}\$\$", payload)
    ]
    if source_display != xml_display:
        raise ValueError("Display formulas changed during WXR generation.")
    if source_inline != xml_inline:
        raise ValueError("Inline formulas changed during WXR generation.")
    if "<p>$$<br" in payload:
        raise ValueError("A display formula uses HTML breaks instead of literal lines.")

    return len(source_display), len(source_inline)


def validate_latex(formulas: list[str], working_root: Path) -> None:
    pdflatex = shutil.which("pdflatex")
    if pdflatex is None:
        raise RuntimeError("pdflatex is required for formula syntax validation.")

    document = [
        r"\documentclass{article}",
        r"\usepackage{amsmath,amssymb}",
        r"\begin{document}",
    ]
    document.extend(r"\[" + formula + r"\]" for formula in formulas)
    document.append(r"\end{document}")

    with tempfile.TemporaryDirectory(prefix="note-validation-", dir=working_root) as tmp:
        tmp_path = Path(tmp)
        tex_path = tmp_path / "formulas.tex"
        tex_path.write_text("\n".join(document), encoding="utf-8")
        result = subprocess.run(
            [
                pdflatex,
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-output-directory={tmp_path}",
                str(tex_path),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(result.stdout + result.stderr)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--xml", type=Path, required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--forbid", action="append", default=[])
    args = parser.parse_args()

    source = args.source.read_text(encoding="utf-8")
    for term in args.forbid:
        if term in source:
            raise ValueError(f"Out-of-scope term found: {term}")

    display_count, inline_count = validate_wxr(source, args.xml, args.slug)
    display, inline = extract_source_formulas(source)
    note_root = Path(__file__).resolve().parents[1]
    validate_latex(display + inline, note_root)

    print(f"source: {args.source} ({len(source)} characters)")
    print(f"xml: {args.xml} ({args.xml.stat().st_size} bytes)")
    print(f"headings/formula round-trip: OK")
    print(f"display formulas: {display_count}")
    print(f"inline formulas: {inline_count}")
    print("LaTeX formula syntax: OK")


if __name__ == "__main__":
    main()
