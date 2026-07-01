# Backlog

今後やること、思いついたこと、後で整理するタスクを置いておく場所。

## 運用ルール

- 思いついたものはまず `Inbox` に入れる
- 次にやる候補は `Next` に移す
- 今進めているものは `Doing` に置く
- 詰まっているものは `Blocked` に置く
- 確認中のものは `Review` に置く
- 完了したものは `Done` に移す
- `Doing` は最大3つまでにする

---

## Inbox

- [ ] GitHubに入れるもの・入れないもののルールを整理する
- [ ] `.gitignore` の内容を確認する
- [ ] READMEからdocsへの導線を作る
- [ ] Obsidianで開いたときに見やすいリンク構成を確認する
- 作者ノートテンプレート v1 を作る
- 作品ノートテンプレート v1 を作るか検討する
- キャラクターノートテンプレート v1 を作るか検討する
- `virtual_folders` / `vfolders` の命名を最終決定する
- タグ運用ルールを整理する
- 自作アプリでギャラリー表示サイズ変更を要件化する
- 自作アプリで表示モード切り替え機能を検討する
	- メディアサムネイル表示
	- ノートプレビュー表示
	- メタデータ付きカード表示
	- 詳細リスト表示
- 自作アプリで、サムネイルと一緒に表示するプロパティを選べるようにする
- Notes Explorer的な「ノートそのもののプレビュー表示」を自作アプリUI要件として検討する
- Bases的な「thumbnailプロパティ画像のみのギャラリー表示」を自作アプリUI要件として検討する

---

## Next

### Obsidian運用

- `metadata-template v1.3` のBases関連記述を実検証結果に合わせて更新する
	- `thumbnail` プロパティをBases表示用として明記
	- `thumbnail` パスはクォートなしにする
	- `cover` / Bases formula案は予備案に変更
	- 「資料ノート」表記を必要に応じて「メディアノート」へ変更
- [ ] virtual_folder フィールドの書き方を決める
- [ ] tags と virtual_folder の使い分けルールを書く
- [ ] Obsidian内でのリンク表記ルールを決める
- `work_title` / `characters` を入力してみる


### Python自動化

- [ ] ID生成スクリプトを作る
- [ ] ファイルコピー処理を作る
- [ ] サムネイル生成処理を作る
- [ ] Markdownノート生成処理を作る
- [ ] URL、作者名、投稿日、タグを入力できる形を考える

### PureRef連携

- [ ] PureRefから元画像IDを確認できる運用を考える
- [ ] 画像ファイル名にIDを含める
- [ ] Obsidianノートへの逆引き方法を検証する

### GitHub管理

- [ ] docs構成を確認する
- [ ] READMEに現在の目的を書く
- [ ] changelogを書くか決める

### 将来のアプリ化

- [ ] Qt/Pythonモックの最小UIを考える
- [ ] 仮想フォルダーのデータ構造を考える
- [ ] Apple写真アプリ風のUI要素をメモする

---

## Doing
- Obsidian資料管理用のメタデータテンプレート検証
- Bases / Notes Explorer による一覧表示検証
- Python自動化前の手動運用テスト

---

## Blocked

なし

---

## Review

なし

---

## Done

- [x] Notionは最初は使わず、ObsidianとGitHubで進める方針に決定
- [x] `docs/00_project_overview.md` を既存の概要ページとして扱う方針に決定
- [x] ObsidianとGitHubを使った進捗管理の初期構成作成
- [x]   Bases formulaでサムネイル表示する方法を検証する
- [x] Notes Explorerが資料ブラウザとして使えるか検証する
- [x] メタデータテンプレート v1.1 を実ファイルでテストする
- 新しい検証用兼運用Vaultを作成
- 最小フォルダ構成を確認
- `metadata-template v1.1` を使って手動ノート作成を実施
- 資料ノートIDを `REF-YYYYMMDD-HHMMSS` 形式にする方針を決定
- 作者・作品・キャラクター用プレフィックスとして `AUTH` / `WORK` / `CHAR` を使う方針を決定
- サムネイルに `_thumb` を付ける方針を決定
- 作品名・キャラクター名をタグではなく専用プロパティにする方針を決定
- `metadata-template v1.3` を `docs/10_specs/` に追加する
- `metadata-template v1.3` を使って画像1枚を手動登録する
- `REF-YYYYMMDD-HHMMSS` 形式のIDを実際に試す
- サムネイル `_thumb.jpg` 命名で問題がないか確認する
- サムネイルクリックで実画像が開くか確認する
- Basesで `thumbnail` プロパティをImage propertyに指定し、複数画像のサムネイル一覧表示ができることを確認
- `cover` プロパティとBases formulaは一旦不要と判断
- `thumbnail` パスはクォートなしで書く必要があることを確認
- Notes ExplorerとBasesの表示思想の違いを確認
	- Notes Explorerはノートそのもののプレビューに近い
	- Basesは指定したthumbnail画像とプロパティ表示に向いている