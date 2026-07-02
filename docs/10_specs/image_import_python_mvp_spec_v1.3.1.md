# 画像取り込みPython MVP仕様書 v1.3.1対応版

## 目的

Obsidian + PureRef + Python によるメディア管理ワークフローのために、画像取り込み作業を自動化する。

このMVPでは、`ArtArchive_Inbox/` に入れた画像ファイルをPythonで処理し、以下を自動生成する。

- 実画像ファイル
- サムネイル画像
- Obsidian用メディアノート
- 取り込みログ

この仕様書は、GitHub上の `docs/10_specs/metadata-template-v1.3.1.md` を正本として、Python実装チャット、Claude、Codexなどに渡すための実装指示書として使う。

---

## 正本テンプレート

正本は以下。

```text
docs/10_specs/metadata-template-v1.3.1.md
```

Python MVPは、このテンプレートに従ってメディアノートを生成する。

重要な前提：

- 個別メディア管理ノートは **メディアノート** と呼ぶ
- IDは `REF-YYYYMMDD-HHMMSS` 形式
- 実画像は `ArtArchive/originals/images/`
- サムネイルは `_assets/thumbnails/`
- メディアノートは `10_References/Images/`
- サムネイル名は `REF-YYYYMMDD-HHMMSS_thumb.jpg`
- `thumbnail` プロパティはクォートなし
- Obsidian Basesは `thumbnail` プロパティをImage propertyに指定して表示する
- `cover` プロパティは使わない
- Bases formulaは予備案として保留

---

## MVPの対象範囲

### やること

- Inbox内の画像ファイルを検出する
- `REF-YYYYMMDD-HHMMSS` 形式のIDを発行する
- 実画像を `ArtArchive/originals/images/` にコピーする
- 実画像をIDベースのファイル名にリネームする
- サムネイルを生成する
- メディアノート `.md` を生成する
- `thumbnail` プロパティをクォートなしで出力する
- 成功した元ファイルを `_processed/` に移動する
- 失敗した元ファイルを `_failed/` に移動する
- CSVログを出力する

### やらないこと

MVPでは以下は対象外。

- GUI
- フォルダ監視
- Pixiv自動取得
- X自動取得
- Instagram自動取得
- Webページ自動保存
- PDF対応
- 動画対応
- GIFアニメーションの本格対応
- Source Group対応
- 関連メディアリンク自動生成
- 作者ノート自動生成
- 作品ノート自動生成
- キャラクターノート自動生成
- PureRef連携
- AIタグ付け
- タグ推定
- データベース管理

---

## 用語

### メディアノート

1つの画像・動画・Web由来資料など、個別メディアを管理するObsidianノート。

このMVPでは、画像1枚につき1つのメディアノートを生成する。

### 実画像

管理対象となる元画像のコピー。

保存先：

```text
ArtArchive/originals/images/
```

### サムネイル

Obsidian Basesやノート本文で表示する軽量画像。

保存先：

```text
_assets/thumbnails/
```

### Source Group

同じX投稿、Pixiv作品、Webページなど、複数メディアをまとめる元ページ単位。

MVPでは実装しない。将来対応候補として残す。

---

## 想定フォルダ構成

MVPでは、まずObsidian Vault内にすべて置く前提にする。

```text
ObsidianVault/
├─ 10_References/
│  └─ Images/
├─ _assets/
│  └─ thumbnails/
├─ ArtArchive/
│  ├─ originals/
│  │  └─ images/
│  ├─ logs/
│  └─ metadata/
└─ ArtArchive_Inbox/
   ├─ _processed/
   └─ _failed/
```

---

## 入力フォルダ

```text
ArtArchive_Inbox/
```

ユーザーは、このフォルダに取り込みたい画像をドラッグ&ドロップする。

処理成功後：

```text
ArtArchive_Inbox/_processed/
```

処理失敗後：

```text
ArtArchive_Inbox/_failed/
```

---

## 対応画像形式

MVPでは以下を対象とする。

```text
.jpg
.jpeg
.png
.webp
```

### 後回し

```text
.gif
.bmp
.tif
.tiff
.heic
.mp4
.mov
.pdf
```

GIFはMVPでは後回し。必要になったら、最初のフレームをサムネイル化する方針を検討する。

---

## ID仕様

### 基本形式

```text
REF-YYYYMMDD-HHMMSS
```

例：

```text
REF-20260702-231530
```

意味：

```text
REF = Reference / メディアノート用プレフィックス
YYYYMMDD = 取り込み日
HHMMSS = 取り込み時刻
```

### 同一秒の衝突対策

複数画像を同時に取り込む場合、同じ秒に複数IDが発行される可能性がある。

その場合は、末尾に連番を追加して衝突を避ける。

例：

```text
REF-20260702-231530
REF-20260702-231530-001
REF-20260702-231530-002
```

Python実装では、以下をチェックする。

- 同名のメディアノートが存在しないか
- 同名の実画像が存在しないか
- 同名のサムネイルが存在しないか
- 同じ実行内で生成済みIDと衝突しないか

---

## ファイル命名ルール

### 実画像

元画像の拡張子を維持する。

```text
ArtArchive/originals/images/REF-YYYYMMDD-HHMMSS.jpg
ArtArchive/originals/images/REF-YYYYMMDD-HHMMSS.png
ArtArchive/originals/images/REF-YYYYMMDD-HHMMSS.webp
```

例：

```text
ArtArchive/originals/images/REF-20260702-231530.jpg
```

### サムネイル

サムネイルは必ず `_thumb.jpg` にする。

```text
_assets/thumbnails/REF-YYYYMMDD-HHMMSS_thumb.jpg
```

例：

```text
_assets/thumbnails/REF-20260702-231530_thumb.jpg
```

元画像がjpgでも、サムネイルには `_thumb` を付ける。

理由：

- 実画像とサムネイルを区別しやすい
- Obsidianのリンク解決で混乱しにくい
- Python処理で扱いやすい
- Bases表示で管理しやすい

### メディアノート

```text
10_References/Images/REF-YYYYMMDD-HHMMSS.md
```

例：

```text
10_References/Images/REF-20260702-231530.md
```

---

## 生成するメディアノート

### 生成先

```text
10_References/Images/
```

### ファイル名

```text
REF-YYYYMMDD-HHMMSS.md
```

---

## メディアノートfrontmatter

Pythonは以下のfrontmatterを生成する。

重要：`thumbnail` はクォートなしで出力する。

```markdown
---
id: REF-20260702-231530
type: image
title: ""
original_filename: "original_image.jpg"
source_url: ""
author: ""
work_title: ""
characters: []
tags:
  - inbox
virtual_folders:
  - References/Unsorted
local_file: "ArtArchive/originals/images/REF-20260702-231530.jpg"
local_file_uri: ""
thumbnail: _assets/thumbnails/REF-20260702-231530_thumb.jpg
created: 2026-07-02
status: inbox
rating:
---
```

### thumbnailの注意

OK：

```yaml
thumbnail: _assets/thumbnails/REF-20260702-231530_thumb.jpg
```

NG：

```yaml
thumbnail: "_assets/thumbnails/REF-20260702-231530_thumb.jpg"
```

Obsidian BasesでImage propertyに指定するため、`thumbnail` はクォートなしで出力する。

---

## メディアノート本文

Pythonはfrontmatterの下に以下の本文を生成する。

```markdown
[![REF-20260702-231530](../../_assets/thumbnails/REF-20260702-231530_thumb.jpg)](../../ArtArchive/originals/images/REF-20260702-231530.jpg)

# メモ

# 気になったところ

# 使い道

# 仮想フォルダ

- References/Unsorted

# 元情報

- 元ファイル名: original_image.jpg
- 実画像: [開く](../../ArtArchive/originals/images/REF-20260702-231530.jpg)
- 実ファイルパス: `ArtArchive/originals/images/REF-20260702-231530.jpg`
- サムネイル: `_assets/thumbnails/REF-20260702-231530_thumb.jpg`
```

---

## パス仕様

MVPでは、Vault内パスを基本にする。

### frontmatter内

```yaml
local_file: "ArtArchive/originals/images/REF-20260702-231530.jpg"
thumbnail: _assets/thumbnails/REF-20260702-231530_thumb.jpg
```

### 本文内

メディアノートは `10_References/Images/` にあるため、本文内の画像リンクは相対パスで書く。

```markdown
[![REF-20260702-231530](../../_assets/thumbnails/REF-20260702-231530_thumb.jpg)](../../ArtArchive/originals/images/REF-20260702-231530.jpg)
```

---

## サムネイル仕様

### 保存形式

```text
.jpg
```

### 命名

```text
REF-YYYYMMDD-HHMMSS_thumb.jpg
```

### サイズ

MVPでは長辺512px程度を基本にする。

例：

```yaml
thumbnail:
  max_size: 512
  format: jpg
  quality: 85
```

### アスペクト比

維持する。

### 透過画像

PNGやWebPで透過がある場合、白背景に合成してJPEG化する。

将来的には背景色を設定可能にしてもよいが、MVPでは白背景でよい。

---

## 処理フロー

```text
1. config.yaml を読み込む
2. 必要なフォルダを確認・作成する
3. ArtArchive_Inbox/ 内の画像ファイルを列挙する
4. 各画像に対して処理する
   4-1. 対応拡張子か確認する
   4-2. REF日時IDを発行する
   4-3. 出力ファイル名を決める
   4-4. 実画像を ArtArchive/originals/images/ にコピーする
   4-5. サムネイルを _assets/thumbnails/ に生成する
   4-6. メディアノートMarkdownを生成する
   4-7. ログを書く
   4-8. 成功した元ファイルを _processed/ に移動する
   4-9. 失敗した元ファイルを _failed/ に移動する
5. 処理結果をコンソールに表示する
```

---

## 安全設計

### 元ファイルを削除しない

MVPでは、元ファイルを削除しない。

成功時は `_processed/` に移動する。

失敗時は `_failed/` に移動する。

### 上書き禁止

以下のファイルが既に存在する場合は上書きしない。

- 実画像
- サムネイル
- メディアノート

衝突した場合は新しいIDを発行する。

### 1ファイル失敗しても処理続行

1枚の画像で失敗しても、他の画像の処理は続行する。

### 失敗理由を残す

失敗理由はログとコンソールに出す。

---

## ログ仕様

### 保存先

```text
ArtArchive/logs/import_log.csv
```

### カラム案

```csv
imported_at,id,type,original_filename,source_path,local_file,thumbnail,note_path,status,error
```

### 成功例

```csv
2026-07-02T23:15:30+09:00,REF-20260702-231530,image,original_image.jpg,ArtArchive_Inbox/original_image.jpg,ArtArchive/originals/images/REF-20260702-231530.jpg,_assets/thumbnails/REF-20260702-231530_thumb.jpg,10_References/Images/REF-20260702-231530.md,success,
```

### 失敗例

```csv
2026-07-02T23:16:10+09:00,,image,broken.jpg,ArtArchive_Inbox/broken.jpg,,,,failed,"画像を開けませんでした"
```

---

## config.yaml仕様

パスはスクリプトに直書きしない。

```yaml
vault_dir: "/path/to/ObsidianVault"

inbox_dir: "ArtArchive_Inbox"
processed_dir: "ArtArchive_Inbox/_processed"
failed_dir: "ArtArchive_Inbox/_failed"

originals_dir: "ArtArchive/originals/images"
thumbnails_dir: "_assets/thumbnails"
notes_dir: "10_References/Images"
logs_dir: "ArtArchive/logs"

id:
  prefix: "REF"
  format: "%Y%m%d-%H%M%S"
  collision_suffix_digits: 3

thumbnail:
  max_size: 512
  format: "jpg"
  quality: 85
  background: "white"

defaults:
  tags:
    - inbox
  virtual_folders:
    - References/Unsorted
  status: inbox
```

MVPでは、`vault_dir` を基準に相対パスを解決する。

---

## 実装ファイル構成

MVPでは、まず以下の構成でよい。

```text
import_images.py
config.yaml
requirements.txt
README.md
```

### requirements.txt

```text
Pillow
PyYAML
```

---

## コマンド実行

### 基本実行

```bash
python import_images.py
```

### config指定

```bash
python import_images.py --config config.yaml
```

### dry-run

余裕があれば実装する。

```bash
python import_images.py --dry-run
```

dry-runでは実ファイルを作らず、何が生成される予定かだけ表示する。

---

## コンソール出力例

```text
=== Obsidian Archive Image Import MVP ===

Vault: /path/to/ObsidianVault
Inbox: ArtArchive_Inbox
Found: 3 files

[OK] REF-20260702-231530 original_image.jpg
[OK] REF-20260702-231531 reference.png
[FAILED] broken.webp - 画像を開けませんでした

Done.
Success: 2
Failed: 1
```

---

## MVP完了条件

以下ができればMVP完了。

- `ArtArchive_Inbox/` に画像を入れる
- Pythonを実行する
- `REF-YYYYMMDD-HHMMSS` 形式のIDが発行される
- 実画像が `ArtArchive/originals/images/` にコピーされる
- サムネイルが `_assets/thumbnails/` に生成される
- メディアノートが `10_References/Images/` に生成される
- `thumbnail` プロパティがクォートなしで出力される
- Obsidian Basesで `thumbnail` をImage propertyに指定するとサムネイル表示できる
- サムネイルをクリックすると実画像を開ける
- 成功ファイルが `_processed/` に移動する
- 失敗ファイルが `_failed/` に移動する
- `import_log.csv` に処理結果が残る

---

## MVP後に検討すること

### v1.4候補

- `subjects` プロパティ追加
- `source_type`
- `source_group_id`
- `source_index`
- 関連メディアリンク
- Source Group単位の一覧
- X / Pixiv / Instagram / Webページ対応

### 自作アプリ候補

- メディアサムネイル表示
- ノートプレビュー表示
- メタデータ付きカード表示
- 詳細リスト表示
- ギャラリーサイズ変更
- Source Group内の関連メディア一覧

---

## 実装依頼文

Claude / Codex / 新しいChatGPT実装チャットに渡す場合は以下。

```markdown
Obsidian資料管理用の画像取り込みPython MVPを実装してください。

正本仕様は `画像取り込みPython MVP仕様書 v1.3.1対応版` です。
メディアノートの正本テンプレートは `docs/10_specs/metadata-template-v1.3.1.md` です。

要件：
- Python 3.x
- Pillowでサムネイル生成
- PyYAMLでconfig読み込み
- CSVログ出力
- GUIなし
- フォルダ監視なし
- 対象は jpg / jpeg / png / webp
- IDは REF-YYYYMMDD-HHMMSS
- 同一秒衝突時は -001 などを付けて回避
- 実画像は ArtArchive/originals/images/
- サムネイルは _assets/thumbnails/
- サムネイル名は REF-YYYYMMDD-HHMMSS_thumb.jpg
- メディアノートは 10_References/Images/
- thumbnailプロパティはクォートなし
- coverプロパティは使わない
- Bases formulaは使わない
- 元ファイルを削除しない
- 成功時は _processed/ へ移動
- 失敗時は _failed/ へ移動
- 1ファイル失敗しても他の処理は続行

成果物：
- import_images.py
- config.yaml
- requirements.txt
- README.md

安全性を重視し、ファイルの上書きや消失が起きないようにしてください。
```
