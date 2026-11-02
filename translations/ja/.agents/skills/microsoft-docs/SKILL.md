---
name: microsoft-docs
---
# Microsoft Docs

Microsoft テクノロジー エコシステムのリサーチスキル。learn.microsoft.com とその外側にあるドキュメント（VS Code、GitHub、Aspire、Agent Framework リポジトリ）をカバーします。

---

## デフォルト: Microsoft Learn MCP

learn.microsoft.com 上の<strong>すべてのコンテンツ</strong>（Azure、.NET、M365、Power Platform、Agent Framework、Semantic Kernel、Windows など）にはこれらのツールを使用してください。これは大多数の Microsoft ドキュメントの問い合わせに対する主要なツールです。

| ツール | 目的 |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com の検索 — 概念、ガイド、チュートリアル、構成 |
| `microsoft_code_sample_search` | Learn ドキュメントから動作するコードスニペットを探す。最良の結果には `language`（`python`、`csharp` など）を渡してください |
| `microsoft_docs_fetch` | 検索抜粋では不十分な場合、特定の URL からページ全体のコンテンツを取得 |

完全なチュートリアルや全ての構成オプションが必要な場合、または検索抜粋が切り詰められている場合には検索後に `microsoft_docs_fetch` を使用してください。

---

## 例外: 他のツールを使用する場合

以下のカテゴリは **learn.microsoft.com の外側** にあります。代わりに指定されたツールを使用してください。

### Aspire — Aspire MCP Server（推奨）または Context7 を使用

Aspire のドキュメントは **aspire.dev** にあり、Learn にはありません。最適なツールは Aspire CLI のバージョンによって異なります：

**CLI 13.2以降**（推奨）— Aspire MCP サーバーには組み込みのドキュメント検索ツールがあります：

| MCP ツール | 説明 |
|----------|-------------|
| `list_docs` | aspire.dev から利用可能な全ドキュメントのリストを表示 |
| `search_docs` | aspire.dev のコンテンツに対する重み付けされたレキシカル検索 |
| `get_doc` | スラッグによる特定のドキュメントの取得 |

これらは Aspire CLI 13.2 で提供されています（[PR #14028](https://github.com/microsoft/aspire/pull/14028)）。アップデートには `aspire update --self --channel daily` を使用してください。

**CLI 13.1** — MCP サーバーは統合の検索（`list_integrations`、`get_integration_docs`）は提供しますが、ドキュメント検索は<strong>提供しません</strong>。Fallback は Context7 を使用してください：

| ライブラリ ID | 用途 |
|---|---|
| `/microsoft/aspire.dev` | 主要 — ガイド、統合、CLI リファレンス、デプロイメント |
| `/microsoft/aspire` | ランタイムソース — API 内部、実装詳細 |
| `/communitytoolkit/aspire` | コミュニティ統合 — Go、Java、Node.js、Ollama |

### VS Code — Context7 を使用

VS Code のドキュメントは **code.visualstudio.com** にあり、Learn ではありません。

| ライブラリ ID | 用途 |
|---|---|
| `/websites/code_visualstudio` | ユーザードキュメント — 設定、機能、デバッグ、リモート開発 |
| `/websites/code_visualstudio_api` | Extension API — webviews、TreeViews、コマンド、貢献ポイント |

### GitHub — Context7 を使用

GitHub のドキュメントは **docs.github.com** と **cli.github.com** にあります。

| ライブラリ ID | 用途 |
|---|---|
| `/websites/github_en` | Actions、API、リポジトリ、セキュリティ、管理、Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) のコマンドとフラグ |

### Agent Framework — Learn MCP + Context7 を使用

Agent Framework のチュートリアルは learn.microsoft.com 上にあります（`microsoft_docs_search` を使用）が、**GitHub リポジトリ** には公開ドキュメントより先行するAPIレベルの詳細があります — 特に DevUI REST API リファレンス、CLI オプション、および .NET 統合。

| ライブラリ ID | 用途 |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | チュートリアル — DevUI ガイド、トレーシング、ワークフローオーケストレーション |
| `/microsoft/agent-framework` | API 詳細 — DevUI REST エンドポイント、CLI フラグ、認証、.NET `AddDevUI`/`MapDevUI` |

**DevUI のヒント：** ハウツーガイドは Learn サイトのソースに問い合わせた後、API レベルの詳細（エンドポイントスキーマ、プロキシ構成、認証トークン）はリポジトリのソースを参照してください。

---

## Context7 セットアップ

すべての Context7 クエリについて、セッションごとに1回ライブラリ ID を解決してください：

1. `mcp_context7_resolve-library-id` に技術名を渡す
2. 返されたライブラリ ID と特定のクエリで `mcp_context7_query-docs` を呼び出す

---

## 効果的なクエリの書き方

明確に記述してください — バージョン、意図、および言語を含める：

```
# ❌ Too broad
"Azure Functions"
"agent framework"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"GitHub Actions workflow_dispatch inputs matrix strategy"
"Aspire AddUvicornApp Python FastAPI integration"
"DevUI serve agents tracing OpenTelemetry directory discovery"
"Agent Framework workflow conditional edges branching handoff"
```

コンテキストを含める：
- 関連する場合は <strong>バージョン</strong>（`.NET 8`、`Aspire 13`、`VS Code 1.96`）
- <strong>タスクの意図</strong>（`quickstart`、`tutorial`、`overview`、`limits`、`API reference`）
- 多言語ドキュメントの場合は <strong>言語</strong>（`Python`、`TypeScript`、`C#`）

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->