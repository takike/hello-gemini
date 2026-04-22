# AtCoder Markdown Link Generator

## 1. 概要
指定された AtCoder のコンテストIDから問題一覧を取得し、Markdown形式のリンクを標準出力に表示するCLIツール。

## 2. 実行イメージ
```bash
python atcoder_links.py abc300
```

**出力結果:**
```text
- [A - N-choice question](https://atcoder.jp/contests/abc300/tasks/abc300_a)
- [B - Same Map in the RPG World](https://atcoder.jp/contests/abc300/tasks/abc300_b)
...
```

## 3. 主要コンポーネント
- **CLI引数解析**: `argparse` または `sys.argv` を使用。
- **HTTPリクエスト**: `requests` を使用してコンテストの `tasks` ページ（例: `https://atcoder.jp/contests/abc300/tasks`）を取得。
- **HTML解析**: `beautifulsoup4` を使用して問題テーブルから「問題記号（A, B...）」「タイトル」「URL」を抽出。

## 4. 考慮事項
- **エラーハンドリング**: 存在しないコンテストIDが渡された場合の処理（HTTP 404など）。
- **依存ライブラリ**: `requests`, `beautifulsoup4` のインストールが必要（`requirements.txt` を用意する）。
