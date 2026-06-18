# Metadata Template v1.1

資料管理用Markdownノートのメタデータテンプレート。

## 目的

画像、動画、Webページ、PDFなどの資料を、Obsidian上で管理しやすくするための共通テンプレートを定義する。

---

## 基本方針

- 1資料につき1Markdownノートを作る
- 実データはGitHubには入れない
- 実データへのパス、サムネイル、出典情報、タグ、仮想フォルダーをMarkdownに記録する
- tags と virtual_folder は役割を分ける

---

## テンプレート

```yaml
---
id: AA-000001
title: ""
type: image
status: active

source:
  url: ""
  site: ""
  author: ""
  author_url: ""
  published_at: ""
  saved_at: ""

files:
  original: ""
  thumbnail: ""
  pdf: ""

tags:
  - reference

virtual_folders:
  - ""

rating: 0
favorite: false

created_at: ""
updated_at: ""
---
```

## 本文テンプレート

```md
# {{title}}

## Preview

![[thumbnail-path]]

## Source

- URL:
- Site:
- Author:
- Published:
- Saved:

## File

- Original:
- Thumbnail:
- PDF:

## Tags

-

## Virtual Folders

-

## Memo

## Related

```

---

## 各項目の意味

### id

資料ごとの一意なID。

例：

```txt
AA-000001
AA-000002
AA-000003
```

### title

資料の表示名。ファイル名と完全一致していなくてもよい。

### type

資料の種類。

候補：

```txt
image
video
pdf
web
text
model
other
```

### status

資料の状態。

候補：

```txt
active
archived
draft
deleted
```

### source

出典情報を記録する。

### files

実ファイルやサムネイルへのパスを記録する。

### tags

検索・分類用の柔軟なキーワード。複数つけてよい。

### virtual_folders

将来の仮想フォルダー用フィールド。タグとは別に、フォルダー的な配置・カテゴリを表す。

### rating

重要度や好みの度合い。最初は `0` でよい。

### favorite

よく見る資料かどうか。

---

## 関連ページ

- [[virtual-folder-rule]]
- [[03_backlog]]
