---
name: microsoft-docs
description: 查詢官方 Microsoft 文件，以尋找有關 Azure、.NET、Agent Framework、Aspire、VS Code、GitHub
  等的概念、教學及程式碼範例。預設使用 Microsoft Learn MCP，對於存放在 learn.microsoft.com 以外的內容，則使用 Context7
  與 Aspire MCP。
---
# Microsoft Docs

Research skill for the Microsoft technology ecosystem. Covers learn.microsoft.com and documentation that lives outside it (VS Code, GitHub, Aspire, Agent Framework repos).

---

## Default: Microsoft Learn MCP

Use these tools for **learn.microsoft.com 上的所有內容** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, and more. This is the primary tool for the vast majority of Microsoft documentation queries.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | 在 learn.microsoft.com 搜尋 — 概念、指南、教學、設定 |
| `microsoft_code_sample_search` | 從 Learn 文件中尋找可運行的程式碼片段。傳入 `language`（`python`、`csharp` 等）以獲得最佳結果 |
| `microsoft_docs_fetch` | 從特定 URL 取得完整頁面內容（當搜尋摘錄不足時） |

Use `microsoft_docs_fetch` after search when you need complete tutorials, all config options, or when search excerpts are truncated.

---

## Exceptions: When to Use Other Tools

The following categories live **outside** learn.microsoft.com. Use the specified tool instead.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire docs live on **aspire.dev**, not Learn. The best tool depends on your Aspire CLI version:

**CLI 13.2+** (recommended) — The Aspire MCP server includes built-in docs search tools:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Lists all available documentation from aspire.dev |
| `search_docs` | Weighted lexical search across aspire.dev content |
| `get_doc` | Retrieves a specific document by slug |

These ship in Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). To update: `aspire update --self --channel daily`. 參考: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — The MCP server provides integration lookup (`list_integrations`, `get_integration_docs`) but **not** docs search. Fall back to Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Primary — guides, integrations, CLI reference, deployment |
| `/dotnet/aspire` | Runtime source — API internals, implementation details |
| `/communitytoolkit/aspire` | Community integrations — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code docs live on **code.visualstudio.com**, not Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | User docs — settings, features, debugging, remote dev |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, commands, contribution points |

### GitHub — Use Context7

GitHub docs live on **docs.github.com** and **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repos, security, admin, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) commands and flags |

### Agent Framework — Use Learn MCP + Context7

Agent Framework tutorials are on learn.microsoft.com (use `microsoft_docs_search`), but the **GitHub repo** has API-level detail that is often ahead of published docs — particularly DevUI REST API reference, CLI options, and .NET integration.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorials — DevUI guides, tracing, workflow orchestration |
| `/microsoft/agent-framework` | API detail — DevUI REST endpoints, CLI flags, auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI 小貼士：** 先查詢 Learn 網站來源以取得操作指南，然後查詢儲存庫來源以取得 API 級別的細節（端點 schema、代理設定、驗證令牌）。

---

## Context7 Setup

For any Context7 query, resolve the library ID first (one-time per session):

1. Call `mcp_context7_resolve-library-id` with the technology name
2. Call `mcp_context7_query-docs` with the returned library ID and a specific query

---

## Writing Effective Queries

Be specific — include version, intent, and language:

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
- **版本**（視情況而定）（` .NET 8`, `Aspire 13`, `VS Code 1.96`）
- **任務目的**（`quickstart`, `tutorial`, `overview`, `limits`, `API reference`）
- **語言**，針對多語言文件（`Python`, `TypeScript`, `C#`）

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件已使用 AI 翻譯服務 Co-op Translator（https://github.com/Azure/co-op-translator）進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的原語版本應被視為具權威性的來源。若涉及重要資訊，建議採用專業人工翻譯。我們對因使用本翻譯而引致的任何誤解或誤釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->