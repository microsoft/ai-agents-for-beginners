---
name: microsoft-docs
---
# Microsoft Docs

针对微软技术生态系统的研究技能。涵盖 learn.microsoft.com 以及存在于其之外的文档（VS Code、GitHub、Aspire、Agent Framework 仓库）。

---

## 默认：Microsoft Learn MCP

对 **learn.microsoft.com** 上的所有内容使用这些工具 —— Azure、.NET、M365、Power Platform、Agent Framework、Semantic Kernel、Windows 等。这是绝大多数微软文档查询的主要工具。

| 工具 | 用途 |
|------|---------|
| `microsoft_docs_search` | 搜索 learn.microsoft.com — 概念、指南、教程、配置 |
| `microsoft_code_sample_search` | 从 Learn 文档中查找可用的代码片段。传递 `language`（`python`、`csharp` 等）以获得最佳结果 |
| `microsoft_docs_fetch` | 从特定 URL 获取完整页面内容（当搜索摘要不够时） |

当需要完整教程、所有配置选项或搜索摘要被截断时，搜索后使用 `microsoft_docs_fetch`。

---

## 例外情况：何时使用其他工具

以下类别存在于 **learn.microsoft.com** 之外。请使用指定工具。

### Aspire — 使用 Aspire MCP Server（优选）或 Context7

Aspire 文档位于 **aspire.dev**，而非 Learn。最佳工具取决于您的 Aspire CLI 版本：

**CLI 13.2+**（推荐）—— Aspire MCP 服务器内置文档搜索工具：

| MCP 工具 | 说明 |
|----------|-------------|
| `list_docs` | 列出 aspire.dev 上所有可用文档 |
| `search_docs` | 对 aspire.dev 内容进行加权词汇搜索 |
| `get_doc` | 通过 slug 检索特定文档 |

这些工具随 Aspire CLI 13.2 一起发布（[PR #14028](https://github.com/microsoft/aspire/pull/14028)）。更新命令：`aspire update --self --channel daily`。

**CLI 13.1** — MCP 服务器提供集成查询（`list_integrations`、`get_integration_docs`），但<strong>不支持</strong>文档搜索。请回退使用 Context7：

| 库 ID | 用途 |
|---|---|
| `/microsoft/aspire.dev` | 主要用法 — 指南、集成、CLI 参考、部署 |
| `/microsoft/aspire` | 运行时源 — API 内部实现细节 |
| `/communitytoolkit/aspire` | 社区集成 — Go、Java、Node.js、Ollama |

### VS Code — 使用 Context7

VS Code 文档位于 **code.visualstudio.com**，而非 Learn。

| 库 ID | 用途 |
|---|---|
| `/websites/code_visualstudio` | 用户文档 — 设置、功能、调试、远程开发 |
| `/websites/code_visualstudio_api` | 扩展 API — webviews、TreeViews、命令、贡献点 |

### GitHub — 使用 Context7

GitHub 文档位于 **docs.github.com** 和 **cli.github.com**。

| 库 ID | 用途 |
|---|---|
| `/websites/github_en` | Actions、API、仓库、安全、管理、Copilot |
| `/websites/cli_github` | GitHub CLI（`gh`）的命令和参数 |

### Agent Framework — 使用 Learn MCP + Context7

Agent Framework 教程位于 learn.microsoft.com（使用 `microsoft_docs_search`），但<strong>GitHub 仓库</strong>有时包含比公开文档更前沿的 API 级细节——特别是 DevUI REST API 参考、CLI 选项和 .NET 集成。

| 库 ID | 用途 |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | 教程 — DevUI 指南、跟踪、工作流编排 |
| `/microsoft/agent-framework` | API 细节 — DevUI REST 端点、CLI 标志、认证、.NET `AddDevUI`/`MapDevUI` |

**DevUI 提示：** 先查询 Learn 网站源获取操作指南，再查询仓库源获得 API 级细节（端点模式、代理配置、认证令牌）。

---

## Context7 设置

任何 Context7 查询之前，先解析库 ID（一会话一次）：

1. 使用技术名称调用 `mcp_context7_resolve-library-id`
2. 使用返回的库 ID 和具体查询调用 `mcp_context7_query-docs`

---

## 编写高效查询

要具体 —— 包括版本、意图和语言：

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
- 适用时写明 <strong>版本</strong>（`.NET 8`、`Aspire 13`、`VS Code 1.96`）
- <strong>任务意图</strong>（`quickstart`、`tutorial`、`overview`、`limits`、`API reference`）
- 针对多语言文档的 <strong>语言</strong>（`Python`、`TypeScript`、`C#`）

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->