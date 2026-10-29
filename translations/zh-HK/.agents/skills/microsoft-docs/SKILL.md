---
name: microsoft-docs
description: 查詢官方微軟文件，以尋找涵蓋 Azure、.NET、代理框架、Aspire、VS Code、GitHub 等的概念、教學和範例程式碼。預設使用
  Microsoft Learn MCP，對於那些不在 learn.microsoft.com 上的內容，則使用 Context7 和 Aspire MCP。
---
# Microsoft Docs

Microsoft 技術生態系的研究技能。涵蓋 learn.microsoft.com 及其外的文件（VS Code、GitHub、Aspire、Agent Framework 倉庫）。

---

## 默認：Microsoft Learn MCP

使用這些工具搜尋 **learn.microsoft.com** 上的所有內容 — Azure、.NET、M365、Power Platform、Agent Framework、Semantic Kernel、Windows 等。這是絕大多數 Microsoft 文件查詢的主要工具。

| 工具 | 用途 |
|------|---------|
| `microsoft_docs_search` | 搜尋 learn.microsoft.com — 概念、指南、教學、配置 |
| `microsoft_code_sample_search` | 從 Learn 文件中尋找可用的程式碼片段。傳入 `language` (如 `python`、`csharp` 等) 以獲得最佳結果 |
| `microsoft_docs_fetch` | 從特定 URL 取得完整頁面內容（當搜尋摘錄不夠時） |

當需要完整教學、所有配置選項，或搜尋摘錄被截斷時，搜尋後使用 `microsoft_docs_fetch`。

---

## 例外：何時使用其他工具

以下類別位於 **learn.microsoft.com** 之外。請使用指定工具。

### Aspire — 使用 Aspire MCP 伺服器（首選）或 Context7

Aspire 文件位於 **aspire.dev**，非 Learn。最佳工具取決於您的 Aspire CLI 版本：

**CLI 13.2+**（推薦）— Aspire MCP 伺服器包含內建文件搜尋工具：

| MCP 工具 | 說明 |
|----------|-------------|
| `list_docs` | 列出 aspire.dev 上所有可用文件 |
| `search_docs` | 權重詞彙搜尋 aspire.dev 內容 |
| `get_doc` | 透過 slug 取得特定文件 |

這些工具隨 Aspire CLI 13.2 發佈（[PR #14028](https://github.com/microsoft/aspire/pull/14028)）。更新指令為：`aspire update --self --channel daily`。

**CLI 13.1** — MCP 伺服器提供整合查詢 (`list_integrations`, `get_integration_docs`)，但 <strong>不包括</strong> 文件搜尋。請退回使用 Context7：

| 函式庫 ID | 使用範圍 |
|---|---|
| `/microsoft/aspire.dev` | 主要 — 指南、整合、CLI 參考、部署 |
| `/microsoft/aspire` | 執行時原始碼 — API 內部細節、實作細節 |
| `/communitytoolkit/aspire` | 社群整合 — Go, Java, Node.js, Ollama |

### VS Code — 使用 Context7

VS Code 文件位於 **code.visualstudio.com**，非 Learn。

| 函式庫 ID | 使用範圍 |
|---|---|
| `/websites/code_visualstudio` | 用戶文件 — 設定、功能、偵錯、遠端開發 |
| `/websites/code_visualstudio_api` | 擴充 API — 網頁檢視、樹狀檢視、命令、貢獻點 |

### GitHub — 使用 Context7

GitHub 文件位於 **docs.github.com** 與 **cli.github.com**。

| 函式庫 ID | 使用範圍 |
|---|---|
| `/websites/github_en` | Actions、API、倉庫、資安、管理、Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) 命令與參數 |

### Agent Framework — 使用 Learn MCP + Context7

Agent Framework 教學在 learn.microsoft.com（使用 `microsoft_docs_search`），但 **GitHub 倉庫** 擁有比發佈文件更前沿的 API 細節 — 特別是 DevUI REST API 參考、CLI 選項和 .NET 整合。

| 函式庫 ID | 使用範圍 |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | 教學 — DevUI 指南、追蹤、工作流程編排 |
| `/microsoft/agent-framework` | API 細節 — DevUI REST 端點、CLI 參數、驗證、.NET `AddDevUI`/`MapDevUI` |

**DevUI 提示：** 先查詢 Learn 網站來源以獲得操作指南，再查 GitHub 倉庫來源了解 API 細節（端點結構、代理配置、驗證令牌）。

---

## Context7 設定

對任何 Context7 查詢，首先解析函式庫 ID（每次會話一次）：

1. 呼叫 `mcp_context7_resolve-library-id` 傳入技術名稱
2. 呼叫 `mcp_context7_query-docs` 傳入回傳函式庫 ID 及特定查詢

---

## 撰寫有效查詢

具體明確 — 包含版本、目的和語言：

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

包含背景：
- <strong>版本</strong>（當相關時，如 `.NET 8`、`Aspire 13`、`VS Code 1.96`）
- <strong>任務目的</strong>（`quickstart`、`tutorial`、`overview`、`limits`、`API reference`）
- <strong>語言</strong> 用於多語言文件（`Python`、`TypeScript`、`C#`）

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->