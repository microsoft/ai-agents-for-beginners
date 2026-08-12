---
name: microsoft-docs
description: 查詢官方 Microsoft 文件以尋找跨 Azure、.NET、Agent Framework、Aspire、VS Code、GitHub
  等的概念、教學與程式範例。預設使用 Microsoft Learn MCP，對於存在於 learn.microsoft.com 以外的內容，則使用 Context7
  與 Aspire MCP。
---
# Microsoft 文件

Research skill for the Microsoft technology ecosystem. Covers learn.microsoft.com and documentation that lives outside it (VS Code, GitHub, Aspire, Agent Framework repos).

---

## 預設：Microsoft Learn MCP

Use these tools for **everything on learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, and more. This is the primary tool for the vast majority of Microsoft documentation queries.

| 工具 | 用途 |
|------|---------|
| `microsoft_docs_search` | 搜尋 learn.microsoft.com — 概念、指南、教學、設定 |
| `microsoft_code_sample_search` | 從 Learn 文件中尋找可執行的程式碼片段。傳入 `language`（`python`、`csharp` 等）以獲得最佳結果 |
| `microsoft_docs_fetch` | 從指定 URL 取得完整頁面內容（當搜尋節錄不足時） |

Use `microsoft_docs_fetch` after search when you need complete tutorials, all config options, or when search excerpts are truncated.

---

## 例外情況：何時使用其他工具

The following categories live **outside** learn.microsoft.com. Use the specified tool instead.

### .NET Aspire — 使用 Aspire MCP Server（建議）或 Context7

Aspire 文件位於 **aspire.dev**，而非 Learn。最佳工具取決於你的 Aspire CLI 版本：

**CLI 13.2+**（建議）— Aspire MCP 伺服器包含內建的文件搜尋工具：

| MCP 工具 | 描述 |
|----------|-------------|
| `list_docs` | 列出來自 aspire.dev 的所有可用文件 |
| `search_docs` | 在 aspire.dev 內容中進行加權詞彙搜尋 |
| `get_doc` | 以 slug 取得特定文件 |

These ship in Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). To update: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — The MCP server provides integration lookup (`list_integrations`, `get_integration_docs`) but **not** docs search. Fall back to Context7:

| Library ID | 使用於 |
|---|---|
| `/microsoft/aspire.dev` | 主要 — 指南、整合、CLI 參考、部署 |
| `/dotnet/aspire` | 執行時來源 — API 內部、實作細節 |
| `/communitytoolkit/aspire` | 社群整合 — Go、Java、Node.js、Ollama |

### VS Code — 使用 Context7

VS Code 文件位於 **code.visualstudio.com**，而非 Learn。

| Library ID | 使用於 |
|---|---|
| `/websites/code_visualstudio` | 使用者文件 — 設定、功能、偵錯、遠端開發 |
| `/websites/code_visualstudio_api` | 擴充功能 API — web 檢視、樹狀檢視、指令、貢獻點 |

### GitHub — 使用 Context7

GitHub 文件位於 **docs.github.com** 與 **cli.github.com**。

| Library ID | 使用於 |
|---|---|
| `/websites/github_en` | Actions、API、儲存庫、資安、管理、Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) 的指令與旗標 |

### Agent Framework — 使用 Learn MCP + Context7

Agent Framework 的教學位於 learn.microsoft.com（使用 `microsoft_docs_search`），但 **GitHub 倉庫** 擁有常常比已發佈文件更新的 API 細節 — 尤其是 DevUI REST API 參考、CLI 選項，以及 .NET 整合。

| Library ID | 使用於 |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | 教學 — DevUI 指南、追蹤、工作流程編排 |
| `/microsoft/agent-framework` | API 細節 — DevUI REST 端點、CLI 旗標、驗證、.NET `AddDevUI`/`MapDevUI` |

**DevUI 提示：** 先查詢 Learn 網站的來源以取得操作指南，然後再查閱倉庫來源以獲取 API 級別的具體內容（端點模式、代理設定、驗證令牌）。

---

## Context7 設定

For any Context7 query, resolve the library ID first (one-time per session):

1. 使用技術名稱呼叫 `mcp_context7_resolve-library-id`
2. 使用回傳的 library ID 及特定查詢呼叫 `mcp_context7_query-docs`

---

## 撰寫有效查詢

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
- **版本**（視情況）（`.NET 8`、`Aspire 13`、`VS Code 1.96`）
- **任務目的**（`quickstart`、`tutorial`、`overview`、`limits`、`API reference`）
- **語言**（針對多語系文件）（`Python`、`TypeScript`、`C#`）

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而造成的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->