---
name: microsoft-docs
description: 公式の Microsoft ドキュメントを検索して、Azure、.NET、Agent Framework、Aspire、VS Code、GitHub
  などの概念、チュートリアル、コード例を見つけます。既定では Microsoft Learn MCP を使用し、learn.microsoft.com の外にあるコンテンツには
  Context7 と Aspire MCP を使用します。
---
# Microsoft ドキュメント

Microsoft テクノロジー エコシステム向けのリサーチスキル。learn.microsoft.com とその外部にあるドキュメント（VS Code、GitHub、Aspire、Agent Framework リポジトリ）をカバーします。

---

## 既定: Microsoft Learn MCP

これらのツールは **learn.microsoft.com のすべて** — Azure、.NET、M365、Power Platform、Agent Framework、Semantic Kernel、Windows など — に使用してください。ほとんどの Microsoft ドキュメントに関する問い合わせで主要なツールです。

| ツール | 用途 |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com を検索 — 概念、ガイド、チュートリアル、構成 |
| `microsoft_code_sample_search` | Learn ドキュメントから動作するコードスニペットを見つけます。最良の結果を得るには `language` (`python`, `csharp`, etc.) を渡してください |
| `microsoft_docs_fetch` | 特定の URL からページ全体のコンテンツを取得します（検索抜粋では不十分なとき） |

検索の後で、完全なチュートリアルやすべての構成オプションが必要な場合、または検索抜粋が切り捨てられている場合は `microsoft_docs_fetch` を使用してください。

---

## 例外: 他のツールを使用する場合

以下のカテゴリは **learn.microsoft.com の外部** にあります。代わりに指定されたツールを使用してください。

### .NET Aspire — Aspire MCP Server（推奨）または Context7 を使用

Aspire ドキュメントは **aspire.dev** にあり、Learn ではありません。最適なツールは Aspire CLI のバージョンによります。

**CLI 13.2+**（推奨） — Aspire MCP サーバーには組み込みのドキュメント検索ツールが含まれています:

| MCP ツール | 説明 |
|----------|-------------|
| `list_docs` | aspire.dev から利用可能なすべてのドキュメントを一覧表示します |
| `search_docs` | aspire.dev コンテンツに対する重み付きレキシカル検索 |
| `get_doc` | スラッグで特定のドキュメントを取得します |

これらは Aspire CLI 13.2 に同梱されています（[PR #14028](https://github.com/dotnet/aspire/pull/14028)）。更新するには: `aspire update --self --channel daily`。参照: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP サーバーは統合の検索（`list_integrations`, `get_integration_docs`）を提供しますが、ドキュメント検索は提供しません。Context7 にフォールバックしてください:

| Library ID | 使用対象 |
|---|---|
| `/microsoft/aspire.dev` | 主要 — ガイド、統合、CLI リファレンス、デプロイ |
| `/dotnet/aspire` | ランタイムソース — API 内部、実装の詳細 |
| `/communitytoolkit/aspire` | コミュニティ統合 — Go、Java、Node.js、Ollama |

### VS Code — Context7 を使用

VS Code ドキュメントは **code.visualstudio.com** にあり、Learn ではありません。

| Library ID | 使用対象 |
|---|---|
| `/websites/code_visualstudio` | ユーザードキュメント — 設定、機能、デバッグ、リモート開発 |
| `/websites/code_visualstudio_api` | 拡張 API — webviews、TreeViews、コマンド、contribution points |

### GitHub — Context7 を使用

GitHub ドキュメントは **docs.github.com** と **cli.github.com** にあります。

| Library ID | 使用対象 |
|---|---|
| `/websites/github_en` | Actions、API、リポジトリ、セキュリティ、管理、Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) のコマンドとフラグ |

### Agent Framework — Learn MCP + Context7 を使用

Agent Framework のチュートリアルは learn.microsoft.com にあります（`microsoft_docs_search` を使用）が、**GitHub リポジトリ** には公開ドキュメントよりも先行することの多い API レベルの詳細があります — 特に DevUI REST API リファレンス、CLI オプション、.NET 統合。

| Library ID | 使用対象 |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | チュートリアル — DevUI ガイド、トレース、ワークフローオーケストレーション |
| `/microsoft/agent-framework` | API の詳細 — DevUI REST エンドポイント、CLI フラグ、認証、.NET `AddDevUI`/`MapDevUI`` |

DevUI のヒント: まず Learn サイトのソースでハウツーガイドを照会し、その後リポジトリのソースで API レベルの詳細（エンドポイントスキーマ、プロキシ設定、認証トークン）を確認してください。

---

## Context7 のセットアップ

任意の Context7 クエリについて、最初にライブラリ ID を解決してください（セッションごとに一度）:

1. 技術名で `mcp_context7_resolve-library-id` を呼び出します
2. 返されたライブラリ ID と具体的なクエリで `mcp_context7_query-docs` を呼び出します

---

## 効果的なクエリの作成

具体的に記述してください — バージョン、意図、言語を含めてください:

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

Include context:
- **バージョン** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **タスクの意図** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **言語** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責事項：
本書は AI 翻訳サービス「Co‑op Translator」(https://github.com/Azure/co-op-translator) を用いて翻訳されました。正確性の確保に努めていますが、自動翻訳は誤りや不正確な表現を含む場合があります。重要な情報については、原文（原言語版）を権威ある出典としてご参照ください。重要な内容については専門の人による翻訳を推奨します。本翻訳の使用により生じたいかなる誤解や解釈の相違についても責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->