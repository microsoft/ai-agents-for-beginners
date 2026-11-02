---
name: microsoft-docs
---
# Microsoft 文件

Microsoft 技術生態系統的研究技能。涵蓋 learn.microsoft.com 以及存在於其之外的文檔（VS Code、GitHub、Aspire、Agent Framework 倉庫）。

---

## 預設：Microsoft Learn MCP

使用這些工具搜尋 **learn.microsoft.com** 上的所有內容 — 包括 Azure、.NET、M365、Power Platform、Agent Framework、Semantic Kernel、Windows 等。這是大多數 Microsoft 文件查詢的主要工具。

| 工具 | 用途 |
|------|---------|
| `microsoft_docs_search` | 搜尋 learn.microsoft.com — 概念、指南、教學、配置 |
| `microsoft_code_sample_search` | 從 Learn 文件中找工作代碼片段。傳入 `language`（`python`、`csharp` 等）可取得最佳結果 |
| `microsoft_docs_fetch` | 從特定 URL 取得完整頁面內容（當搜尋摘要不足時） |

在需要完整教學、所有配置選項或搜尋摘要被截斷時，請於搜尋後使用 `microsoft_docs_fetch`。

---

## 例外情況：何時使用其他工具

以下類別存在於 **learn.microsoft.com 之外**。請改用指定工具。

### Aspire — 使用 Aspire MCP Server（首選）或 Context7

Aspire 文件位於 **aspire.dev**，非 Learn。最佳工具取決於你的 Aspire CLI 版本：

**CLI 13.2+**（推薦）— Aspire MCP 伺服器包含內建的文件搜尋工具：

| MCP 工具 | 說明 |
|----------|-------------|
| `list_docs` | 列出 aspire.dev 中所有可用的文件 |
| `search_docs` | 對 aspire.dev 內容進行加權詞彙搜尋 |
| `get_doc` | 根據 slug 取得特定文件 |

這些功能隨 Aspire CLI 13.2 版本發布（[PR #14028](https://github.com/microsoft/aspire/pull/14028)）。更新指令：`aspire update --self --channel daily`。

**CLI 13.1** — MCP 伺服器提供整合查詢（`list_integrations`、`get_integration_docs`），但<strong>不提供</strong>文件搜尋。請使用 Context7 作為備用：

| 函式庫 ID | 用途 |
|---|---|
| `/microsoft/aspire.dev` | 主要用於指南、整合、CLI 參考、部署 |
| `/microsoft/aspire` | 執行時來源 — API 內部、實作細節 |
| `/communitytoolkit/aspire` | 社群整合 — Go、Java、Node.js、Ollama |

### VS Code — 使用 Context7

VS Code 文件位於 **code.visualstudio.com**，非 Learn。

| 函式庫 ID | 用途 |
|---|---|
| `/websites/code_visualstudio` | 使用者文件 — 設定、功能、偵錯、遠端開發 |
| `/websites/code_visualstudio_api` | 擴充 API — 網頁檢視、樹狀檢視、指令、貢獻點 |

### GitHub — 使用 Context7

GitHub 文件位於 **docs.github.com** 與 **cli.github.com**。

| 函式庫 ID | 用途 |
|---|---|
| `/websites/github_en` | Actions、API、倉庫、安全性、管理、Copilot |
| `/websites/cli_github` | GitHub CLI（`gh`）指令及參數 |

### Agent Framework — 使用 Learn MCP + Context7

Agent Framework 教學在 learn.microsoft.com（使用 `microsoft_docs_search`），但 **GitHub 倉庫** 提供的 API 細節往往比已發布文件更新 — 特別是 DevUI REST API 參考、CLI 選項及 .NET 整合。

| 函式庫 ID | 用途 |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | 教學 — DevUI 指南、追蹤、工作流編排 |
| `/microsoft/agent-framework` | API 細節 — DevUI REST 端點、CLI 參數、驗證、.NET `AddDevUI`/`MapDevUI` |

**DevUI 小秘訣：** 先從 Learn 網站原始碼查詢操作指南，再從倉庫原始碼查詢 API 細節（端點架構、代理配置、驗證令牌）。

---

## Context7 設定

對任何 Context7 查詢，請先解析函式庫 ID（每次會話一次即可）：

1. 呼叫 `mcp_context7_resolve-library-id` 並指定技術名稱
2. 使用返回的函式庫 ID 和特定查詢呼叫 `mcp_context7_query-docs`

---

## 撰寫有效查詢

要具體 — 包含版本、意圖和程式語言：

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
- 有相關時包含 <strong>版本</strong>（`.NET 8`、`Aspire 13`、`VS Code 1.96`）
- <strong>任務意圖</strong>（`quickstart`、`tutorial`、`overview`、`limits`、`API reference`）
- 多語言文件請包含 <strong>語言</strong>（`Python`、`TypeScript`、`C#`）

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->