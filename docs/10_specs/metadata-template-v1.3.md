## 目的  
  
Obsidianで制作資料・参考資料を管理するための、資料ノートテンプレート v1.3。  
  
v1.3では、v1.1の手動テスト結果を踏まえて、以下を反映する。  
  
- 資料ノートIDを `REF-YYYYMMDD-HHMMSS` 形式に変更  
- サムネイルのファイル名に `_thumb` を付ける  
- 作品名とキャラクター名をタグではなく専用プロパティで管理する  
- `tags` と `virtual_folders` を分離する  
- 実画像はVault内の `ArtArchive/originals/images/` に置く前提で手動テストする  
- `local_file_uri` は将来のVault外運用用として残す  
- Obsidian Basesでのサムネイル表示は、`cover` プロパティではなくformula方式を検証する  
  
---  
  
## 基本方針  
  
```text  
1資料 = 1Markdownノート  
```  
  
画像本体・サムネイル・ノートは同じIDで紐付ける。  
  
例：  
  
```text  
資料ID:  
REF-20260622-143012  
  
資料ノート:  
10_References/Images/REF-20260622-143012.md  
  
実画像:  
ArtArchive/originals/images/REF-20260622-143012.jpg  
  
サムネイル:  
_assets/thumbnails/REF-20260622-143012_thumb.jpg  
```  
  
---  
  
## IDルール  
  
### 資料ノート  
  
資料ノートのIDは `REF` を使う。  
  
```text  
REF-YYYYMMDD-HHMMSS  
```  
  
例：  
  
```text  
REF-20260622-143012  
```  
  
### その他のノート種別  
  
将来的には以下のプレフィックスを使う。  
  
```text  
REF   = 資料ノート / Reference  
AUTH  = 作者ノート / Author  
WORK  = 作品ノート / Work  
CHAR  = キャラクターノート / Character  
```  
  
資料ノートは数が多くなるため、ファイル名もIDベースにする。  
  
```text  
10_References/Images/REF-20260622-143012.md  
```  
  
作者・作品・キャラクターのノートは、人間が探しやすいように名前ベースのファイル名を基本とする。  
  
```text  
20_Authors/作者名.md  
作品名.md  
キャラクター名.md  
```  
  
IDはfrontmatter内に持たせる。  
  
---  
  
## ファイル命名ルール  
  
### 実画像  
  
元画像の拡張子を維持する。  
  
```text  
ArtArchive/originals/images/REF-20260622-143012.jpg  
ArtArchive/originals/images/REF-20260622-143012.png  
ArtArchive/originals/images/REF-20260622-143012.webp  
```  
  
### サムネイル  
  
サムネイルは `_thumb` を付けて、基本は `.jpg` にする。  
  
```text  
_assets/thumbnails/REF-20260622-143012_thumb.jpg  
```  
  
元画像がjpgでも、実画像とサムネイルのファイル名を完全一致させない。  
  
理由：  
  
- Obsidianのリンク解決で混乱しにくい  
- 実画像とサムネイルを見分けやすい  
- Bases formulaでサムネイルを組み立てやすい  
- Python自動生成時に処理しやすい  
  
---  
  
## tags / virtual_folders / 固有名詞の使い分け  
  
### tags  
  
資料の特徴・属性・用途を表す。  
  
例：  
  
```yaml  
tags:  
  - inbox  - pose/standing  - lighting/backlight  - use/character-design```  
  
タグは増やしすぎない。  
  
細かい印象や曖昧な情報は本文メモに書く。  
  
---  
  
### virtual_folders  
  
将来の自作管理アプリやObsidianプラグインで、仮想フォルダとして表示したい分類を表す。  
  
例：  
  
```yaml  
virtual_folders:  
  - References/Unsorted  - References/Character/Costume  - Project/Mashumaro/CharacterDesign```  
  
役割：  
  
```text  
tags            = 資料の特徴・検索軸  
virtual_folders = 仮想フォルダ上の置き場所  
```  
  
---  
  
### 作品名・キャラクター名  
  
作品名とキャラクター名はタグにはせず、専用プロパティにする。  
  
```yaml  
work_title: ""  
characters: []  
```  
  
例：  
  
```yaml  
work_title: "作品名"  
characters:  
  - "キャラクターA"  - "キャラクターB"```  
  
役割：  
  
```text  
work_title = 作品名  
characters = キャラクター名  
```  
  
作品名・キャラクター名をタグにするとタグ一覧が膨らみやすいため、v1.3では別プロパティとして扱う。  
  
---  
  
## 資料ノートテンプレート v1.3  
  
実際の資料ノートでは、以下をノート先頭にそのまま書く。    
` ```yaml ` は書かない。  
  
```markdown  
---  
id: REF-20260622-143012  
type: image  
title: ""  
original_filename: "original_image.jpg"  
source_url: ""  
author: ""  
work_title: ""  
characters: []  
tags:  
  - inboxvirtual_folders:  
  - References/Unsortedlocal_file: "ArtArchive/originals/images/REF-20260622-143012.jpg"  
local_file_uri: ""  
thumbnail: "_assets/thumbnails/REF-20260622-143012_thumb.jpg"  
created: 2026-06-22  
status: inbox  
rating:  
---  
  
[![REF-20260622-143012](../../_assets/thumbnails/REF-20260622-143012_thumb.jpg)](../../ArtArchive/originals/images/REF-20260622-143012.jpg)  
  
# メモ  
  
# 気になったところ  
  
# 使い道  
  
# 仮想フォルダ  
  
- References/Unsorted  
  
# 元情報  
  
- 元ファイル名: original_image.jpg  
- 実画像: [開く](../../ArtArchive/originals/images/REF-20260622-143012.jpg)  
- 実ファイルパス: `ArtArchive/originals/images/REF-20260622-143012.jpg`  
- サムネイル: `_assets/thumbnails/REF-20260622-143012_thumb.jpg`  
```  
  
---  
  
## frontmatter項目  
  
### id  
  
```yaml  
id: REF-20260622-143012  
```  
  
資料ごとの一意なID。  
  
---  
  
### type  
  
```yaml  
type: image  
```  
  
資料の種類。  
  
v1.3ではまず画像を対象にする。  
  
将来的には以下も検討する。  
  
```yaml  
type: video  
type: webpage  
type: pdf  
type: document  
```  
  
---  
  
### title  
  
```yaml  
title: ""  
```  
  
資料に分かりやすいタイトルを付けたい場合に使う。空欄でもよい。  
  
---  
  
### original_filename  
  
```yaml  
original_filename: "original_image.jpg"  
```  
  
取り込み前の元ファイル名。  
  
IDベースにリネームしても元の名前を確認できるようにする。  
  
---  
  
### source_url  
  
```yaml  
source_url: ""  
```  
  
掲載元URL。  
  
Pixiv、X、Webページ、記事などのURLを入れる。  
  
---  
  
### author  
  
```yaml  
author: ""  
```  
  
作者名。  
  
将来的には作者ノートへリンクする。  
  
```yaml  
author: "[[作者名]]"  
```  
  
作者ノート側には `AUTH` IDを持たせる予定。  
  
---  
  
### work_title  
  
```yaml  
work_title: ""  
```  
  
作品名。  
  
タグではなく専用プロパティとして管理する。  
  
---  
  
### characters  
  
```yaml  
characters: []  
```  
  
キャラクター名。  
  
複数キャラクターが写っている資料に対応するため、配列で持つ。  
  
例：  
  
```yaml  
characters:  
  - "キャラクターA"  - "キャラクターB"```  
  
---  
  
### tags  
  
```yaml  
tags:  
  - inbox```  
  
特徴・属性・用途を表すタグ。  
  
タグ疲れを防ぐため、増やしすぎない。  
  
---  
  
### virtual_folders  
  
```yaml  
virtual_folders:  
  - References/Unsorted```  
  
仮想フォルダ用の分類。  
  
実際のフォルダは動かさず、将来の自作プラグインや自作管理アプリでツリー表示するために使う。  
  
---  
  
### local_file  
  
```yaml  
local_file: "ArtArchive/originals/images/REF-20260622-143012.jpg"  
```  
  
実画像本体へのVault内パス。  
  
v1.3では、手動テストしやすいように実画像もVault内に置く。  
  
---  
  
### local_file_uri  
  
```yaml  
local_file_uri: ""  
```  
  
将来的に実画像をVault外へ出した場合に使う。  
  
例：  
  
```yaml  
local_file_uri: "file:///Users/username/ArtArchive/originals/images/REF-20260622-143012.jpg"  
```  
  
v1.3では空欄でよい。  
  
---  
  
### thumbnail  
  
```yaml  
thumbnail: "_assets/thumbnails/REF-20260622-143012_thumb.jpg"  
```  
  
サムネイルへのVault内パス。  
  
Pythonや将来の管理アプリが読むための情報として残す。  
  
---  
  
### created  
  
```yaml  
created: 2026-06-22  
```  
  
資料ノートを作成した日、または取り込み日。  
  
---  
  
### status  
  
```yaml  
status: inbox  
```  
  
整理状態。  
  
候補：  
  
```text  
inbox  = 取り込み直後・未整理  
active = 整理済み・使用中  
done   = 確認済み・保管  
```  
  
---  
  
### rating  
  
```yaml  
rating:  
```  
  
資料評価。  
  
必要になったら `1〜5` などで使う。  
  
---  
  
## 本文項目  
  
### サムネイルクリックで実画像を開く  
  
```markdown  
[![REF-20260622-143012](../../_assets/thumbnails/REF-20260622-143012_thumb.jpg)](../../ArtArchive/originals/images/REF-20260622-143012.jpg)  
```  
  
意味：  
  
```text  
サムネイルを表示  
  ↓クリック  
  ↓実画像を開く  
```  
  
---  
  
### メモ  
  
```markdown  
# メモ  
```  
  
自由メモ。  
  
タグにしない細かい印象や、あいまい検索したい内容を書く。  
  
例：  
  
```markdown  
手の形が自然。  
斜め上からの構図で、キャラが強く見える。  
服のシワはラフだが、シルエットが分かりやすい。  
```  
  
---  
  
### 気になったところ  
  
```markdown  
# 気になったところ  
```  
  
観察ポイントを箇条書きで書く。  
  
---  
  
### 使い道  
  
```markdown  
# 使い道  
```  
  
この資料を何に使うかを書く。  
  
例：  
  
```markdown  
- キャラクターデザイン参考  
- ポーズ練習  
- 背景ライティング参考  
```  
  
---  
  
### 仮想フォルダ  
  
```markdown  
# 仮想フォルダ  
```  
  
frontmatterの `virtual_folders` を人間が見やすいように本文にも書く。  
  
将来的に不要なら削除してよい。  
  
---  
  
### 元情報  
  
```markdown  
# 元情報  
```  
  
元ファイル名、実画像リンク、サムネイルパスなどを確認する場所。  
  
---  
  
## Obsidian Bases用メモ  
  
v1.3では `cover` プロパティは一旦使わない。  
  
BasesのCards viewでギャラリー表示する場合は、formulaでサムネイル画像を組み立てる方式を検証する。  
  
サムネイル名は以下の規則にする。  
  
```text  
file.basename + "_thumb.jpg"  
```  
  
例：  
  
```text  
REF-20260622-143012.md  
REF-20260622-143012_thumb.jpg  
```  
  
Bases formula候補：  
  
```yaml  
formulas:  
  thumb: image(file(link("[[_assets/thumbnails/" + file.basename + "_thumb.jpg]]")))```  
  
この方式が動けば、資料ノート側に `cover` を書かなくても、ノート名とサムネイル名の規則だけでカード表示できる。  
  
---  
  
## 手動テスト手順  
  
まずは画像1枚で試す。  
  
```text  
1. 実画像を ArtArchive/originals/images/ に置く  
2. 実画像を REF-YYYYMMDD-HHMMSS.元拡張子 にリネームする  
3. サムネイルを _assets/thumbnails/ に置く  
4. サムネイル名を REF-YYYYMMDD-HHMMSS_thumb.jpg にする  
5. 10_References/Images/ に REF-YYYYMMDD-HHMMSS.md を作る  
6. v1.3テンプレートを貼る  
7. パスと元ファイル名を実データに合わせて修正する  
8. サムネイルクリックで実画像が開くか確認する  
9. Bases / Notes Explorer で一覧表示を確認する  
```  
  
---  
  
## v1.3で確認したいこと  
  
- `REF-YYYYMMDD-HHMMSS` のIDが扱いやすいか  
- サムネイルの `_thumb` 命名が分かりやすいか  
- 実画像とサムネイルが混同されないか  
- `work_title` と `characters` をタグと分離した運用が自然か  
- `tags` が増えすぎないか  
- `virtual_folders` が仮想フォルダ設計に使えそうか  
- 本文メモがあいまい検索用の情報として機能しそうか  
- Bases formulaでサムネイル表示できるか  
- Notes Explorerで見やすく一覧できるか  
  
---  
  
## 今後の検討  
  
- 作者ノートテンプレート v1  
- 作品ノートテンプレート v1  
- キャラクターノートテンプレート v1  
- タグ運用ルール  
- virtual_folders / vfolders の命名確定  
- Bases formulaの確定  
- Python MVP仕様書への反映  
- 自作アプリでのギャラリー表示サイズ変更