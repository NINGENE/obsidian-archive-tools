# Virtual Folder Rule

`virtual_folders` は、将来の資料管理アプリにおける仮想フォルダーを想定したフィールド。

## 目的

実ファイルを移動せずに、フォルダーのような分類を行うためのルールを定義する。

---

## 基本方針

- `tags` と `virtual_folders` は別物として扱う
- `tags` は検索用の柔軟なキーワード
- `virtual_folders` はフォルダー的な配置・分類
- 実ファイルは移動しない
- 1つの資料が複数の仮想フォルダーに所属してもよい

---

## tags と virtual_folders の違い

### tags

資料の性質や要素を表す。

例：

```txt
character
background
lighting
color
composition
anime-style
pose
vehicle
weapon
```

### virtual_folders

資料をどこに置くか、どのカテゴリに属するかを表す。

例：

```txt
Reference/Character/Female
Reference/Background/Interior
Reference/Vehicle/Motorcycle
Project/Mashumaro/Character
Project/Mashumaro/Background
```

---

## 書き方

MarkdownのYAML frontmatterでは以下のように書く。

```yaml
virtual_folders:
  - Reference/Character/Female
  - Project/Mashumaro/Character
```

---

## ルール

### 1. 階層は `/` で区切る

```txt
Reference/Character/Female
```

### 2. 先頭カテゴリは大きな用途にする

例：

```txt
Reference
Project
Study
Favorite
Archive
```

### 3. 具体的すぎる情報は tags に入れる

悪い例：

```txt
Reference/Character/Female/BlueHair/Smile/Standing
```

良い例：

```yaml
virtual_folders:
  - Reference/Character/Female

tags:
  - blue-hair
  - smile
  - standing
```

### 4. 実フォルダーとは一致しなくてよい

`virtual_folders` はあくまで仮想的な分類。実ファイルの保存場所とは別に考える。

### 5. 将来のアプリUIで使うことを想定する

将来的には、左サイドバーに仮想フォルダーを表示するようなUIを想定する。

```txt
Reference
├─ Character
│  └─ Female
├─ Background
│  └─ Interior
└─ Vehicle
   └─ Motorcycle
```

---

## 初期カテゴリ案

```txt
Reference/
Project/
Study/
Favorite/
Archive/
```

---

## 関連ページ

- [[metadata-template-v1.1]]
- [[ADR-001-use-obsidian-first]]
