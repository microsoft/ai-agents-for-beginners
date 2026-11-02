---
name: microsoft-docs
description: 查詢官方 Microsoft 文件，以尋找涵蓋 Azure、.NET、Agent Framework、Aspire、VS Code、GitHub
  等的概念、教學和程式碼範例。預設使用 Microsoft Learn MCP，對於存在於 learn.microsoft.com 以外的內容，則使用 Context7
  和 Aspire MCP。
---
# Microsoft Docs

專爲 Microsoft 技術生態系的研究技能。涵蓋 learn.microsoft.com 以及存在於它之外的文件（VS Code、GitHub、Aspire、Agent Framework 倉庫）。

---

## 預設：Microsoft Learn MCP

對 **learn.microsoft.com** 上的所有內容使用這些工具 — Azure、.NET、M365、Power Platform、Agent Framework、Semantic Kernel、Windows 等等。這是絕大多數 Microsoft 文件查詢的主要工具。

| Tool | 用途 |
|------|---------|
| `microsoft_docs_search` | 搜索 learn.microsoft.com — 概念、指南、教程、配置 |
| `microsoft_code_sample_search` | 從 Learn 文件中找到有效的程式碼片段。傳遞 `language`（`python`、`csharp` 等）以獲得最佳結果 |
| `microsoft_docs_fetch` | 從特定 URL 獲取完整頁面內容（當搜尋摘錄不足時） |

搜尋後需要完整教程、所有配置選項，或者當搜尋摘錄被截斷時使用 `microsoft_docs_fetch`。

---

## 例外情況：何時使用其他工具

以下分類存在於 **learn.microsoft.com** 之外。請改用指定工具。

### Aspire — 優先使用 Aspire MCP Server 或 Context7

Aspire 文件存在於 **aspire.dev**，而非 Learn。最佳工具取決於您的 Aspire CLI 版本：

**CLI 13.2+**（推薦）— Aspire MCP 伺服器內置文件搜索工具：

| MCP 工具 | 描述 |
|----------|-------------|
| `list_docs` | 列出 aspire.dev 上所有可用文件 |
| `search_docs` | 對 aspire.dev 內容進行加權詞彙搜索 |
| `get_doc` | 通過 slug 獲取特定文件 |

這些功能包含於 Aspire CLI 13.2（[PR #14028](https://github.com/microsoft/aspire/pull/14028)）。更新方法：`aspire update --self --channel daily`。

**CLI 13.1** — MCP 伺服器提供集成查找（`list_integrations`, `get_integration_docs`）但<strong>不含</strong>文件搜索。請退回使用 Context7：

| 函式庫 ID | 用途 |
|---|---|
| `/microsoft/aspire.dev` | 主要 — 指南、整合、CLI 參考、部署 |
| `/microsoft/aspire` | 運行時來源 — API 內部、實作細節 |
| `/communitytoolkit/aspire` | 社群整合 — Go、Java、Node.js、Ollama |

### VS Code — 使用 Context7

VS Code 文件存在於 **code.visualstudio.com**，而非 Learn。

| 函式庫 ID | 用途 |
|---|---|
| `/websites/code_visualstudio` | 使用者文件 — 設定、功能、除錯、遠程開發 |
| `/websites/code_visualstudio_api` | 擴充 API — webviews、TreeViews、指令、擴充點 |

### GitHub — 使用 Context7

GitHub 文件存在於 **docs.github.com** 和 **cli.github.com**。

| 函式庫 ID | 用途 |
|---|---|
| `/websites/github_en` | Actions、API、倉庫、安全性、管理、Copilot |
| `/websites/cli_github` | GitHub CLI（`gh`）指令與旗標 |

### Agent Framework — 使用 Learn MCP + Context7

Agent Framework 教程存在於 learn.microsoft.com（使用 `microsoft_docs_search`），但 **GitHub 倉庫** 擁有通常領先於發佈文件的 API 細節 — 特別是 DevUI REST API 參考、CLI 選項以及 .NET 整合。

| 函式庫 ID | 用途 |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | 教程 — DevUI 指南、追蹤、工作流編排 |
| `/microsoft/agent-framework` | API 細節 — DevUI REST 端點、CLI 旗標、認證、.NET `AddDevUI`/`MapDevUI` |

**DevUI 小提示：** 先查詢 Learn 網站資源獲得使用指南，然後查詢倉庫資源了解 API 細節（端點結構、代理配置、認證令牌）。

---

## Context7 設定

對任何 Context7 查詢，首先解析函式庫 ID（每次會話一次）：

1. 使用技術名稱呼叫 `mcp_context7_resolve-library-id`
2. 使用返回的函式庫 ID 和特定查詢呼叫 `mcp_context7_query-docs`

---

## 撰寫高效查詢

具體說明 — 包含版本、意圖及語言：

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

包含上下文：
- 相關時的 <strong>版本</strong>（`.NET 8`、`Aspire 13`、`VS Code 1.96`）
- <strong>任務意圖</strong>（`quickstart`、`tutorial`、`overview`、`limits`、`API reference`）
- 多語言文件的 <strong>語言</strong>（`Python`、`TypeScript`、`C#`）

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->