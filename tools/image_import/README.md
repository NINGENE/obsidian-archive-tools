# Image Import MVP

Obsidian資料管理用の画像取り込みPythonツール。

`ArtArchive_Inbox/` に入れた画像を処理し、以下を自動生成する。

* 実画像ファイル
* サムネイル画像
* Obsidian用メディアノート
* 取り込みログ

## 目的

Obsidian + PureRef + Python によるメディア管理ワークフローのために、画像取り込み作業を自動化する。

このツールは、まずMVPとして画像ファイルのみを対象にする。

## 対象ファイル

対応予定の画像形式:

* `.jpg`
* `.jpeg`
* `.png`
* `.webp`

MVPでは、GIF / 動画 / PDF / Webページ保存は対象外。

## フォルダ構成

想定するVault内の構成:

```text
ObsidianVault/
├─ 10_References/
│  └─ Images/
├─ _assets/
│  └─ thumbnails/
├─ ArtArchive/
│  ├─ originals/
│  │  └─ images/
│  └─ logs/
└─ ArtArchive_Inbox/
   ├─ _processed/
   └─ _failed/
```

## 生成されるもの

画像1枚につき、以下を生成する。

```text
実画像:
ArtArchive/originals/images/REF-YYYYMMDD-HHMMSS.jpg

サムネイル:
_assets/thumbnails/REF-YYYYMMDD-HHMMSS_thumb.jpg

メディアノート:
10_References/Images/REF-YYYYMMDD-HHMMSS.md

ログ:
ArtArchive/logs/import_log.csv
```

## IDルール

メディアノートIDは以下の形式にする。

```text
REF-YYYYMMDD-HHMMSS
```

例:

```text
REF-20260703-213000
```

同じ秒に複数画像を処理した場合は、末尾に連番を付ける。

```text
REF-20260703-213000
REF-20260703-213000-001
REF-20260703-213000-002
```

## セットアップ

必要なライブラリをインストールする。

```bash
pip install -r requirements.txt
```

## 設定ファイル

`config.example.yaml` をコピーして、ローカル用の `config.yaml` を作る。

```bash
cp config.example.yaml config.yaml
```

`config.yaml` には、自分のObsidian Vaultのパスを書く。

例:

```yaml
vault_dir: "/path/to/ObsidianVault"
```

`config.yaml` はPCごとのローカル設定なので、Git管理しない。

## 実行方法

基本実行:

```bash
python import_images.py
```

configを指定する場合:

```bash
python import_images.py --config config.yaml
```

## 現在の実装状況

### 実装済み

* `load_config()`
  `config.yaml` を読み込む

* `build_paths()`
  Vault基準で必要なフォルダパスを組み立てる

### 次に実装すること

* Inbox内の画像ファイルを検出する
* 対応拡張子だけに絞り込む
* 実画像をコピーする
* サムネイルを生成する
* メディアノートを生成する
* CSVログを出力する
* 成功ファイルを `_processed/` に移動する
* 失敗ファイルを `_failed/` に移動する

## 注意

このMVPでは、元ファイルを削除しない。

処理成功後は `ArtArchive_Inbox/_processed/` に移動する。
処理失敗後は `ArtArchive_Inbox/_failed/` に移動する。

既存ファイルの上書きはしない。
