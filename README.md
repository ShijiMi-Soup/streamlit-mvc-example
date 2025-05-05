# Streamlit MVC Example

- database/posts.csv: データベース代わりの csv ファイル
- model.py: データベースとのやり取り
- view.py: 見た目の部分（これを実行する）
- controller.py: モデルとビューのやり取り

## 使い方

1. Python を実行できる環境を用意
1. コマンドプロンプトやターミナルで、このプログラムがあるディレクトリに移動
1. 下記を実行して、必要なモジュール（`requirements.txt`に記載）をインストール
   ```shell
   pip install -r requirements.txt
   ```
1. streamlit で view.py を実行する
   ```shell
   streamlit run view.py
   ```
