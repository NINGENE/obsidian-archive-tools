
期間：2026-06-18 ～ 2026-06-24  
  
---  
  
## 今週のテーマ  
  
Python自動化に入る前に、Obsidian側の資料ノート構造・ID命名・サムネイル命名・一覧表示方法を手動で検証する。  
  
当初のテーマである「ObsidianとGitHubを使った進捗管理の初期構成」は完了済み。    
現在は次の段階として、実際の資料管理テンプレートを検証する。  
  
---  
  
## 今週やること  
  
- [x] [[01_dashboard]] を作成する  
- [x] [[02_roadmap]] を作成する  
- [x] [[03_backlog]] を作成する  
- [x] [[metadata-template-v1.1]] を確認する  
- [x] [[virtual-folder-rule]] を確認する  
- [x] [[ADR-001-use-obsidian-first]] を作成する  
- [x] `.gitignore` の内容を確認する  
  
---  
  
## 追加で今週やること  
  
- [x] [[metadata-template-v1.3]] を `docs/10_specs/` に追加する  
- [x] `metadata-template v1.3` を使って画像1枚を手動登録する  
- [x] `REF-YYYYMMDD-HHMMSS` 形式のIDを実際に使ってみる  
- [ ] 実画像とサムネイルの命名ルールを確認する  
- [x] サムネイルクリックで実画像が開くか確認する  
- [ ] `work_title` / `characters` の入力感を確認する  
- [ ] `tags` / `virtual_folders` の分離が自然か確認する  
- [x] Bases formulaでサムネイル表示できるか確認する  
- [x] Notes Explorerで資料ノートを一覧表示できるか確認する  
- [ ] 作者ノートテンプレート v1 の内容を検討する  
  
---  
  
## 今週やらないこと  
  
- GUI化  
- 大量ファイル処理  
- Pixiv完全自動取得  
- Qtアプリ化  
- Notion連携  
- 本格的なデータベース設計  
- Pythonによる本格自動化  
- PureRef連携の実装  
- 仮想フォルダプラグインの実装  
- 作者・作品・キャラクターノートの大量作成  
  
---  
  
## 現在の検証ポイント  
  
### metadata-template v1.3  
  
v1.3では以下を検証する。  
  
- 資料ノートIDを `REF-YYYYMMDD-HHMMSS` 形式にする  
- サムネイル名に `_thumb` を付ける  
- 作品名を `work_title` で管理する  
- キャラクター名を `characters` で管理する  
- 作品名・キャラクター名をタグにしない  
- `tags` と `virtual_folders` を分離する  
- 実画像はVault内の `ArtArchive/originals/images/` に置いて検証する  
- サムネイルは `_assets/thumbnails/` に置く  
- `cover` プロパティは使わず、Bases formula方式を検証する  
  
---  
  
## 手動登録テストの想定  
  
画像1枚を使って、以下の3点を手動で作る。  
  
```text  
実画像:  
ArtArchive/originals/images/REF-YYYYMMDD-HHMMSS.jpg  
  
サムネイル:  
_assets/thumbnails/REF-YYYYMMDD-HHMMSS_thumb.jpg  
  
資料ノート:  
10_References/Images/REF-YYYYMMDD-HHMMSS.md  
```  
  
資料ノート内では、サムネイルをクリックして実画像を開けるようにする。  
  
```markdown  
[![REF-YYYYMMDD-HHMMSS](../../_assets/thumbnails/REF-YYYYMMDD-HHMMSS_thumb.jpg)](../../ArtArchive/originals/images/REF-YYYYMMDD-HHMMSS.jpg)  
```  
  
---  
  
## 完了条件  
  
### 初期構成の完了条件  
  
- [x] docs内に進捗管理用Markdownが作成されている  
- [x] ObsidianでリポジトリをVaultとして開ける  
- [x] Dashboardから主要ページへ移動できる  
- [x] Backlogに初期タスクが入っている  
- [x] Roadmapに大まかなマイルストーンがある  
- [x] Devlogに初日の作業ログがある  
- [x] Decisionsに方針決定ログがある  
  
### 追加検証の完了条件  
  
- [ ] `docs/10_specs/metadata-template-v1.3.md` が追加されている  
- [ ] 画像1枚をv1.3形式で手動登録できている  
- [ ] サムネイルクリックで実画像を開ける  
- [ ] `work_title` / `characters` の入力感を確認できている  
- [ ] `tags` / `virtual_folders` の使い分けを確認できている  
- [ ] Bases formulaによるサムネイル表示を試せている  
- [ ] Notes Explorerの一覧表示を試せている  
- [ ] 次にPython MVP仕様書へ反映すべき差分が整理されている  
  
---  
  
## 関連ページ  
  
- [[01_dashboard]]  
- [[02_roadmap]]  
- [[03_backlog]]  
- [[2026-06-18]]  
- [[2026-06-22]]  
- [[metadata-template-v1.1]]  
- [[metadata-template-v1.3]]  
- [[virtual-folder-rule]]  
- [[ADR-001-use-obsidian-first]]  
  
---  
  
## 次回再開するとき  
  
まずは以下から再開する。  
  
```text  
1. metadata-template-v1.3.md を docs/10_specs/ に追加  
2. 画像1枚をv1.3形式で手動登録  
3. サムネイルクリックで実画像を開けるか確認  
4. Bases formulaでカード表示できるか確認  
5. Notes Explorerで一覧表示を確認  
```