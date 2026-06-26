# Python Seminar

Python セミナーで使用したコードをまとめるリポジトリです。

## 内容

- `lasso_boston.py`: Boston housing データを使って Lasso 回帰を実行するサンプルコード

## 実行方法

必要なライブラリをインストールします。

```bash
python3 -m pip install -r requirements.txt
```

`boston.csv` を `data/boston.csv` に置いてから実行します。

```bash
python3 lasso_boston.py
```

CSV ファイルを別の場所に置く場合は、`BOSTON_CSV_PATH` にパスを指定します。

```bash
BOSTON_CSV_PATH=/path/to/boston.csv python3 lasso_boston.py
```
