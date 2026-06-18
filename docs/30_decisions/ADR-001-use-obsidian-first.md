# ADR-001: 進捗管理はObsidianとGitHubを中心にする

## Status

Accepted

## Date

2026-06-18

---

## Context

Obsidian自動化、および将来的な資料管理ツール制作を本格的に進めるにあたり、進捗管理方法を検討した。

候補として以下があった。

- Notion
- Obsidian
- GitHub
- VSCode
- PyCharm

Notionは見た目のよいデータベースやタスク管理に強いが、最初からObsidianと併用すると、タスクやメモが二重管理になりやすい。

今回のプロジェクトは、Obsidian自体の自動化やMarkdownベースの資料管理が中心になる。
そのため、進捗管理や仕様書もObsidian内のMarkdownとして扱う方が相性が良い。

---

## Decision

進捗管理は、まず以下の2つを中心にする。

```txt
Obsidian
GitHub
```

役割は以下。

```txt
Obsidian：
進捗管理・仕様書・開発ログ・決定事項を書く場所

GitHub：
Markdown・コード・履歴を管理する場所
```

Notionは最初は使わない。必要になった場合のみ、上位ダッシュボードとして追加を検討する。

---

## Consequences

### 良い点

- Markdownで管理できる
- GitHubで変更履歴を追える
- 仕様書とコードを同じリポジトリで管理できる
- Obsidianのリンク機能を使える
- 将来の自作ツールのテストデータとしても使いやすい
- Notionとの二重管理を避けられる

### 注意点

- Obsidianの `[[Wikiリンク]]` はGitHub上では通常のMarkdownリンクとしては機能しない
- ファイル名変更や移動はObsidian側で行う方が安全
- 大量画像や動画をGitHubに入れないように注意する
- 個人的すぎるDevlogや案件情報は公開リポジトリに入れない

---

## Related

- [[01_dashboard]]
- [[02_roadmap]]
- [[03_backlog]]
- [[metadata-template-v1.1]]
- [[virtual-folder-rule]]
