# AtCoder Markdown Link Generator

## 1. 概要
指定された AtCoder のコンテストIDから問題一覧を取得し、Markdown形式のリンクを標準出力に表示するCLIツールです。

## 2. インストール方法

このツールを実行するには Python 3.x が必要です。

1. リポジトリをクローンします。
   ```bash
   git clone https://github.com/takuyaikemachi/hello-gemini.git
   cd hello-gemini
   ```

2. 仮想環境を作成し、有効化します。
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # venv\Scripts\activate  # Windows
   ```

3. 依存ライブラリをインストールします。
   ```bash
   pip install -r requirements.txt
   ```

## 3. 使い方

コンテストIDを指定して実行します。

```bash
python atcoder_links.py abc345
```

**出力結果:**
```text
- [A - Tally](https://atcoder.jp/contests/abc345/tasks/abc345_a)
- [B - Integer Division Returns](https://atcoder.jp/contests/abc345/tasks/abc345_b)
- [C - One Character Edition](https://atcoder.jp/contests/abc345/tasks/abc345_c)
...
```

## 今後の改善・既知の課題
- [ ] `argparse` を導入し、コマンドライン引数の柔軟性を向上（将来的なオプション追加への対応）
- [ ] ネットワークリクエストにタイムアウトを設定し、ハングアップを防止
- [ ] HTML解析のセレクタをより具体的にし、サイト構造の変化に対する堅牢性を向上
- [ ] エラーハンドリングの強化（ネットワークエラー時のリトライや詳細なエラーメッセージ）

## 4. テストの実行

`pytest` を使用してテストを実行できます。

```bash
pytest
```

## 5. 主要コンポーネント
- **CLI引数解析**: `sys.argv` を使用。
- **HTTPリクエスト**: `requests` を使用してコンテストの `tasks` ページを取得。
- **HTML解析**: `beautifulsoup4` を使用して問題テーブルから情報を抽出。

## 6. 考慮事項
- **エラーハンドリング**: 存在しないコンテストIDが渡された場合はエラーメッセージを表示して終了します。
- **依存ライブラリ**: `requests`, `beautifulsoup4`, `pytest` が必要です。
