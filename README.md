# Python Seminar

Python セミナーで使用した資料・コード・演習ファイルをまとめるリポジトリです。

このセミナーでは、Python を研究やデータ分析で使うための基礎として、仮想環境の作成、パッケージ管理、Notebook の利用、サーバへの接続、機械学習モデルの実装を扱います。

## セミナー概要

### 第1回: Python 環境構築とサーバ利用

- 仮想環境とは、プロジェクトごとに Python のバージョンやライブラリを分けて管理するための独立した環境です。
- 環境構築ツールとして `uv` を使い、Python バージョンの指定、パッケージ追加、Notebook 用の `ipykernel` 導入を行います。
- macOS では Homebrew を使って開発ツールを入れ、サーバ環境では `curl` による `uv` のインストールも扱います。
- VS Code の SSH 接続を使い、研究室サーバへ接続してサーバ上でも仮想環境を作成します。
- `cd`、`mkdir`、`cp`、`pwd` などの基本的なシェルコマンドも、環境作成やファイル操作の練習として扱います。

### 第2回: 機械学習の基本と回帰モデルの評価

- マテリアルズ・インフォマティクスの考え方と、機械学習を材料開発に使う流れを扱います。
- 特徴量、説明変数、目的変数など、機械学習で使う基本用語を確認します。
- XGBoost を使った有機化合物の HOMO エネルギー予測を題材に、CSV の読み込み、前処理、学習データとテストデータへの分割、モデル構築、結果の評価を体験します。
- 回帰モデルの評価指標として、MAE、RMSE、R2 を扱い、予測値と実測値のプロットや重要特徴量の見方を学びます。

### 第3回: 線形回帰・Lasso 回帰・PLS 回帰

- 入力と出力が直線的に変化する「線形」の考え方と、線形回帰の基本を扱います。
- 実測値と予測値のずれを二乗して、合計が最も小さくなる直線を求める最小二乗法を確認します。
- Lasso 回帰では、予測誤差を小さくしつつ不要な変数の係数を 0 に近づける正則化の考え方を学びます。
- PLS 回帰では、多数の説明変数を少数の成分にまとめて予測する考え方を扱います。

### 第4回: 非線形回帰と SVR

- 直線では表現できない非線形の関係と、非線形回帰モデルの考え方を扱います。
- SVR（サポートベクター回帰）を題材に、高次元空間への写像、カーネル関数、RBF カーネル、ε-チューブの考え方を確認します。
- 線形回帰と SVR の違いとして、外れ値への強さや非線形データへの対応を学びます。
- クロスバリデーション、データリーク、再現性のための seed 固定、特徴量エンジニアリングなど、モデル評価や実験設計で重要な用語も扱います。

### 第5回: 分類モデルと評価指標

- 回帰と分類の違いを確認し、カテゴリを予測する分類問題の基本を扱います。
- k-NN（k 近傍法）では、近いサンプルの多数決でクラスを決める考え方と、`k` の値による予測の変化を学びます。
- Random Forest では、決定木を複数組み合わせるアンサンブル学習、バギング、多数決による分類を扱います。
- 分類モデルの評価指標として、混同行列、Accuracy、Precision、Recall、F1 score、ROC 曲線、PR 曲線、AUC を確認します。

第6回以降も、Notebook と CSV データを使いながら、分類・予測モデルの実装と評価を実践しています。

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

## Codex CLI シェルコマンドまとめ

Codex CLI で使うコマンドは、大きく次の2種類に分かれます。

1. ターミナルで実行する `codex ...` コマンド
2. Codex 起動後に入力する `/...` スラッシュコマンド

公式ドキュメント:

- Codex CLI reference: <https://developers.openai.com/codex/cli/reference>
- Codex CLI slash commands: <https://developers.openai.com/codex/cli/slash-commands>

### 1. ターミナルで使う `codex` コマンド

| コマンド | 機能 |
|---|---|
| `codex` | 対話型の Codex CLI を起動する |
| `codex "依頼内容"` | 最初のプロンプト付きで Codex CLI を起動する |
| `codex exec "依頼内容"` / `codex e` | Codex を非対話で実行する。スクリプトや CI 向け |
| `codex review` | 作業ツリーのコードレビューを非対話で実行する |
| `codex login` | ChatGPT または API key などでログインする |
| `codex logout` | 保存済みの認証情報を削除する |
| `codex doctor` | インストール、認証、設定、実行環境を診断する |
| `codex resume` | 過去の対話セッションを再開する |
| `codex fork` | 過去セッションを分岐して新しい会話にする |
| `codex archive` | セッションをアーカイブする |
| `codex delete` | セッションを完全削除する |
| `codex unarchive` | アーカイブしたセッションを戻す |
| `codex apply` / `codex a` | Codex が作成した最新 diff をローカル作業ツリーに適用する |
| `codex mcp` | MCP サーバーを管理する |
| `codex plugin` | Codex plugin を管理する |
| `codex mcp-server` | Codex を MCP server として stdio で起動する |
| `codex app` | Codex デスクトップアプリを起動する |
| `codex completion` | zsh、bash、fish、PowerShell 用の補完スクリプトを生成する |
| `codex update` | Codex CLI を最新バージョンに更新する |
| `codex sandbox` | Codex の sandbox 内で任意コマンドを実行する |
| `codex features` | feature flag を確認する |
| `codex cloud` | Codex Cloud のタスクをターミナルから扱う。実験的機能 |
| `codex help` | ヘルプを表示する |

### 2. よく使う CLI オプション

| オプション | 機能 |
|---|---|
| `-C, --cd <DIR>` | Codex の作業ディレクトリを指定する |
| `-m, --model <MODEL>` | 使用するモデルを指定する |
| `-s, --sandbox <MODE>` | shell 実行時の sandbox 方針を指定する |
| `-a, --ask-for-approval <POLICY>` | コマンド実行前に承認を求める条件を指定する |
| `--search` | ライブ web search を有効化する |
| `-i, --image <FILE>` | 初回プロンプトに画像を添付する |
| `-c, --config <key=value>` | `~/.codex/config.toml` の設定を一時的に上書きする |
| `--add-dir <DIR>` | 追加の書き込み可能ディレクトリを指定する |
| `-p, --profile <PROFILE>` | 指定した profile config を重ねて使う |
| `--no-alt-screen` | alternate screen を使わず、端末のスクロール履歴を残す |
| `-h, --help` | ヘルプを表示する |
| `-V, --version` | Codex CLI のバージョンを表示する |

#### sandbox mode

| 値 | 意味 |
|---|---|
| `read-only` | ファイルの読み取り中心。書き込みは制限される |
| `workspace-write` | 現在の workspace 内への書き込みを許可する |
| `danger-full-access` | sandbox なしで広いアクセスを許可する。慎重に使う |

#### approval policy

| 値 | 意味 |
|---|---|
| `untrusted` | 信頼済みコマンド以外はユーザー承認を求める |
| `on-request` | Codex が必要に応じて承認を求める |
| `never` | 承認を求めない。失敗はそのまま Codex に返される |

### 3. 使用例

```bash
# 現在のディレクトリで Codex CLI を起動
codex

# 作業ディレクトリを指定して起動
codex -C /Users/t-shuichi/Developer/seminar7

# 最初の依頼を渡して起動
codex "このリポジトリの構成を説明して"

# モデルを指定して起動
codex -m gpt-5.4 "このコードをレビューして"

# 非対話で実行
codex exec -C . "テストを実行して失敗原因を要約して"

# 現在の変更をレビュー
codex review

# 診断
codex doctor

# 過去のセッションを再開
codex resume
```

### 4. Codex 起動後に使う `/` スラッシュコマンド

Codex CLI を起動したあと、入力欄で `/` を入力すると、使えるスラッシュコマンドの一覧を確認できます。

| コマンド | 機能 |
|---|---|
| `/status` | 現在のモデル、権限、作業場所、トークン使用量などを表示する |
| `/model` | 使用モデルを変更する |
| `/permissions` | 承認や実行権限を変更する |
| `/diff` | 現在の Git diff を表示する |
| `/review` | 現在の変更をレビューする |
| `/compact` | 長くなった会話を要約して文脈を圧縮する |
| `/clear` | 画面や会話をリセットする |
| `/new` | 新しい会話を開始する |
| `/resume` | 保存済み会話を再開する |
| `/fork` | 現在または過去の会話を分岐する |
| `/plan` | Plan mode に切り替える |
| `/goal` | 長めの作業目標を設定、確認、停止、再開する |
| `/ide` | IDE で開いているファイルや選択範囲を文脈に含める |
| `/mcp` | MCP ツール一覧を確認する |
| `/plugins` | plugin を確認、管理する |
| `/skills` | skill を選択、利用する |
| `/apps` | connector や app を選択する |
| `/mention` | ファイルやフォルダを会話に添付する |
| `/copy` | 最新の Codex 出力をコピーする |
| `/quit` / `/exit` | Codex CLI を終了する |

### 5. まず覚えると便利なコマンド

開発作業では、まず次のコマンドだけ覚えれば十分です。

```text
/status
/diff
/model
/permissions
/review
/compact
/quit
```

よくある流れ:

```text
1. codex -C <作業ディレクトリ> で起動する
2. 作業を依頼する
3. /diff で変更内容を確認する
4. /review で問題がないか確認する
5. 会話が長くなったら /compact する
6. /quit で終了する
```
