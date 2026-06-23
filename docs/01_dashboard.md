# Dashboard

Obsidian自動化・資料管理ツール制作プロジェクトの現在地を確認するためのページ。

## 現在の目標

Obsidian + GitHub を中心に、資料管理ワークフローと自動化ツールの土台を作る。
現在は、Python自動化に入る前に、Obsidian側の資料ノート構造・ID命名・サムネイル命名・一覧表示方法を手動で検証している段階。

## 現在地

### フェーズ

Python実装前の手動検証フェーズ
### 検証中の主な内容

- 新しい検証用兼運用Vaultでのフォルダ構成
- `metadata-template v1.3` の手動テスト
- `REF-YYYYMMDD-HHMMSS` 形式のID運用
- 実画像とサムネイルの命名ルール
- `work_title` / `characters` の扱い
- `tags` / `virtual_folders` の分離
- Bases / Notes Explorer での一覧表示
---
## 今週やること

- [ ] `docs/10_specs/metadata-template-v1.3.md` を追加する
- [ ] `metadata-template v1.3` を使って画像1枚を手動登録する
- [ ] サムネイルクリックで実画像が開くか確認する
- [ ] Bases formulaでサムネイル表示できるか確認する
- [ ] Notes Explorerで一覧表示を確認する
- [ ] 作者ノートテンプレート v1 を検討する
---
## 今やっていること
- [ ] `metadata-template v1.3` の反映
- [ ] 新Vaultでの資料ノート手動登録テスト
- [ ] Bases / Notes Explorer の一覧表示検証
---
## 詰まっていること

- Bases formulaによるサムネイル表示方法は未検証
- Notes Explorerが資料ブラウザとして十分使えるか未検証
- 作者ノート・作品ノート・キャラクターノートのテンプレートは未確定
---
## 次に決めること

- [ ] `virtual_folders` / `vfolders` の命名を最終決定する
- [ ] 作者ノートテンプレート v1 の項目
- [ ] 作品ノート・キャラクターノートを作るかどうか
- [ ] Bases formulaの書き方を確定する
- [ ] Python MVP仕様書へ反映する差分
- [ ] 実データ置き場とGitHub管理対象の境界
---
## 現在の仕様方針メモ

### ID

資料ノートは `REF` プレフィックスを使う。

```
REF-YYYYMMDD-HHMMSS
```

例：

```
REF-20260622-143012
```

将来的なノート種別ごとのプレフィックス案：

```
REF   = 資料ノート / Reference
AUTH  = 作者ノート / Author
WORK  = 作品ノート / Work
CHAR  = キャラクターノート / Character
```

### ファイル命名

```
資料ノート:
10_References/Images/REF-YYYYMMDD-HHMMSS.md

実画像:
ArtArchive/originals/images/REF-YYYYMMDD-HHMMSS.元拡張子

サムネイル:
_assets/thumbnails/REF-YYYYMMDD-HHMMSS_thumb.jpg
```

### プロパティ方針

```
work_title / characters = 固有名詞
tags = 特徴・用途・見た目
virtual_folders = 仮想フォルダ上の分類
memo = 曖昧な印象や補足
```

作品名・キャラクター名はタグにしない。

### Bases方針

`cover` プロパティは一旦使わず、Bases formulaでサムネイルを表示する方式を検証する。

候補：

```
formulas:
  thumb: image(file(link("[[_assets/thumbnails/" + file.basename + "_thumb.
```
---
## 最近完了したこと

- [x] 進捗管理はNotionではなく、まずObsidianとGitHubで進める方針に決定
- [x] docs内のファイル番号は `00_project_overview.md` を考慮して `01_` 以降にする方針に決定
- [x] [[02_roadmap]] を作成する
- [x] [[03_backlog]] に初期タスクを整理する
- [x] [[04_current_sprint]] に今週の作業範囲を書く
- [x] [[metadata-template-v1.1]] を確認する
- [x] [[virtual-folder-rule]] を確認する
- [x] ObsidianとGitHubを使った進捗管理の初期構成作成
- [x] `metadata-template-v1.1` の実運用テスト
- [x] 新しい検証用兼運用Vaultを作成
- [x] 最小フォルダ構成を確認
- [x] 資料ノートIDを `REF-YYYYMMDD-HHMMSS` 形式にする方針を決定
- [x] 作者・作品・キャラクター用プレフィックスとして `AUTH` / `WORK` / `CHAR` を使う方針を決定
- [x] サムネイルに `_thumb` を付ける方針を決定
- [x] 作品名・キャラクター名をタグではなく専用プロパティにする方針を決定
- [x] `metadata-template v1.3` を作成

## 関連ページ

- [[00_project_overview]]
- [[02_roadmap]]
- [[03_backlog]]
- [[04_current_sprint]]
- [[metadata-template-v1.1]]
- [[virtual-folder-rule]]
- [[ADR-001-use-obsidian-first]]
