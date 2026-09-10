---
name: microsoft-docs
description: 查詢官方 Microsoft 文件以尋找跨 Azure、.NET、Agent Framework、Aspire、VS Code、GitHub
  等的概念、教學和程式碼範例。預設使用 Microsoft Learn MCP，對於存在於 learn.microsoft.com 以外的內容則使用 Context7
  和 Aspire MCP。
---
# Microsoft Docs

研究 Microsoft 技術生態系的搜尋技能。涵蓋 learn.microsoft.com 以及存在於其外的文件（VS Code、GitHub、Aspire、Agent Framework 倉庫）。

---

## Default: Microsoft Learn MCP

對於 **learn.microsoft.com** 上的所有內容請使用這些工具 —— Azure、.NET、M365、Power Platform、Agent Framework、Semantic Kernel、Windows 等等。這是絕大多數 Microsoft 文件查詢的主要工具。

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | 搜尋 learn.microsoft.com — 概念、指南、教學、設定 |
| `microsoft_code_sample_search` | 從 Learn 文件中尋找可運行的程式碼片段。傳入 `language`（`python`、`csharp` 等）可獲得最佳結果 |
| `microsoft_docs_fetch` | 從特定 URL 取得完整頁面內容（當搜尋摘錄不足時） |

當您需要完整教學、所有設定選項，或搜尋摘錄被截斷時，請在搜尋後使用 `microsoft_docs_fetch`。

---

## Exceptions: When to Use Other Tools

下列類別的內容位於 **learn.microsoft.com 之外**。請改用指定的工具。

### .NET Aspire — 使用 Aspire MCP Server（首選）或 Context7

Aspire 文件位於 **aspire.dev**，而非 Learn。最佳工具取決於您的 Aspire CLI 版本：

**CLI 13.2+**（建議） — Aspire MCP 伺服器內建文件搜尋工具：

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | 列出來自 aspire.dev 的所有可用文件 |
| `search_docs` | 對 aspire.dev 內容進行加權詞彙搜尋 |
| `get_doc` | 根據 slug 取得特定文件 |

這些功能隨 Aspire CLI 13.2 一併發布（[PR #14028](https://github.com/dotnet/aspire/pull/14028)）。要更新：`aspire update --self --channel daily`。參考： https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP 伺服器提供整合查詢（`list_integrations`, `get_integration_docs`）但**不**提供文件搜尋。請退回使用 Context7：

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | 主要 — 指南、整合、CLI 參考、部署 |
| `/dotnet/aspire` | 執行時原始碼 — API 內部、實作細節 |
| `/communitytoolkit/aspire` | 社群整合 — Go、Java、Node.js、Ollama |

### VS Code — 使用 Context7

VS Code 文件位於 **code.visualstudio.com**，非 Learn。

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | 使用者文件 — 設定、功能、偵錯、遠端開發 |
| `/websites/code_visualstudio_api` | 擴充功能 API — webviews、TreeViews、commands、contribution points |

### GitHub — 使用 Context7

GitHub 文件位於 **docs.github.com** 與 **cli.github.com**。

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions、API、倉庫、資安、管理、Copilot |
| `/websites/cli_github` | GitHub CLI（`gh`）指令與參數 |

### Agent Framework — 使用 Learn MCP + Context7

Agent Framework 教學在 learn.microsoft.com（使用 `microsoft_docs_search`），但 **GitHub 倉庫** 擁有經常領先已發布文件的 API 細節 — 尤其是 DevUI REST API 參考、CLI 選項，以及 .NET 的整合。

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | 教學 — DevUI 指南、追蹤、工作流程編排 |
| `/microsoft/agent-framework` | API 細節 — DevUI REST 端點、CLI 參數、認證、.NET `AddDevUI`/`MapDevUI` |

**DevUI 提示：** 先查詢 Learn 網站的操作指南，然後查詢倉庫原始碼以取得 API 級別的細節（端點結構、代理設定、驗證權杖）。

---

## Context7 Setup

對於任何 Context7 查詢，請先解析 library ID（每個工作階段一次性）：

1. 呼叫 `mcp_context7_resolve-library-id` 並傳入技術名稱
2. 使用回傳的 library ID 與具體查詢呼叫 `mcp_context7_query-docs`

---

## Writing Effective Queries

請具體 — 包含版本、目的與語言：

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
- **Version** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Task intent** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Language** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件係使用 AI 翻譯服務 Co-op Translator（https://github.com/Azure/co-op-translator）翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言的文件應視為具權威性的來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或曲解負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->