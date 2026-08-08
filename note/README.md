# note記事

## ディレクトリ構成

- `articles/<slug>/article.md`
  - note記事の原稿です。
- `articles/<slug>/note.xml`
  - 同じディレクトリの原稿から生成した、noteインポート用WXRです。
- `reference/`
  - 記事へ分割する前の全体原稿など、執筆時に参照する資料です。
- `tools/build_wxr.py`
  - 一つのMarkdown原稿から一つのWXRを生成します。

記事数や公開順をディレクトリ名へ含めず、記事の内容を表すslugを使います。

## WXRの生成

リポジトリのルートで、対象記事を明示して実行します。

```bash
python3 note/tools/build_wxr.py \
  --source note/articles/quantum_theory_introduction/article.md \
  --output note/articles/quantum_theory_introduction/note.xml \
  --slug quantum-theory-introduction \
  --post-date 2026-08-02
```

`--post-date` はWXRに記録する日付です。note上の公開日へ影響する可能性があるため、インポート対象ごとに明示します。

## 数式の確認

数式は、インラインでは `$${...}$$`、独立した段落では開始行と終了行を `$$` として記述します。

WXR内にTeX文字列と改行が保持されていても、noteが数式表示へ変換するとは限りません。実際にnoteの下書きへインポートし、インライン数式とディスプレイ数式を確認してから公開します。

ローカルでは、MarkdownとWXRの見出し・数式の一致、およびTeX構文を次のように検証します。

```bash
python3 note/tools/validate_article.py \
  --source note/articles/quantum_theory_introduction/article.md \
  --xml note/articles/quantum_theory_introduction/note.xml \
  --slug quantum-theory-introduction
```
