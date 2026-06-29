# Python Seminar

Python セミナーで使用した資料・コード・演習ファイルをまとめるリポジトリです。

このセミナーでは、Python を研究やデータ分析で使うための基礎として、仮想環境の作成、パッケージ管理、Notebook の利用、サーバへの接続、機械学習モデルの実装を扱います。

## セミナー概要

第1回では、Python を安全に使うための土台として仮想環境を扱いました。

- 仮想環境とは、プロジェクトごとに Python のバージョンやライブラリを分けて管理するための独立した環境です。
- 環境構築ツールとして `uv` を使い、Python バージョンの指定、パッケージ追加、Notebook 用の `ipykernel` 導入を行います。
- macOS では Homebrew を使って開発ツールを入れ、サーバ環境では `curl` による `uv` のインストールも扱います。
- VS Code の SSH 接続を使い、研究室サーバへ接続してサーバ上でも仮想環境を作成します。
- `cd`、`mkdir`、`cp`、`pwd` などの基本的なシェルコマンドも、環境作成やファイル操作の練習として扱います。

以降の回では、Notebook と CSV データを使いながら、回帰分析、特徴量エンジニアリング、正則化、分類・予測モデルなどを実践しています。

## リポジトリ内容

- `lasso_boston.py`: Boston housing データを使って Lasso 回帰を実行するサンプルコード
- `seminar4/`: 第4回の回帰分析・特徴量エンジニアリング関連ファイル
- `seminar5/`: 第5回の演習 Notebook と diabetes データ
- `seminar6/`: 第6回の演習 Notebook と MNICT 学習データ

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

## 補足

`seminar6/MNICT_train.csv` はサイズが大きいため Git LFS で管理しています。リポジトリを clone する場合は、必要に応じて Git LFS を有効にしてください。
