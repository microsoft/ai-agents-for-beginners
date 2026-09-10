---
name: microsoft-docs
description: 查询官方 Microsoft 文档，以查找有关 Azure、.NET、Agent Framework、Aspire、VS Code、GitHub
  等的概念、教程和代码示例。默认使用 Microsoft Learn MCP，对于存在于 learn.microsoft.com 之外的内容，则使用 Context7
  和 Aspire MCP。
---
# Microsoft 文档

研究 Microsoft 技术生态系统的检索技能。涵盖 learn.microsoft.com 以及存在于其外部的文档（VS Code、GitHub、Aspire、Agent Framework 仓库）。

---

## 默认：Microsoft Learn MCP

对 **learn.microsoft.com** 上的所有内容使用这些工具 —— Azure、.NET、M365、Power Platform、Agent Framework、Semantic Kernel、Windows 等等。对于绝大多数 Microsoft 文档查询，这是主要工具。

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | 在 learn.microsoft.com 上搜索 —— 概念、指南、教程、配置 |
| `microsoft_code_sample_search` | 查找来自 Learn 文档的可运行代码片段。传入 `language`（`python`、`csharp` 等）以获得最佳结果 |
| `microsoft_docs_fetch` | 从特定 URL 获取完整页面内容（当搜索摘录不足时） |

当需要完整教程、所有配置选项或搜索摘录被截断时，在搜索之后使用 `microsoft_docs_fetch`。

---

## 例外：何时使用其他工具

以下类别位于 learn.microsoft.com **之外**。请改用指定的工具。

### .NET Aspire — 使用 Aspire MCP Server（首选）或 Context7

Aspire 文档位于 **aspire.dev**，而不是 Learn。最佳工具取决于你的 Aspire CLI 版本：

**CLI 13.2+**（推荐）—— Aspire MCP 服务器包含内置的文档搜索工具：

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | 列出来自 aspire.dev 的所有可用文档 |
| `search_docs` | 跨 aspire.dev 内容的加权词汇搜索 |
| `get_doc` | 按 slug 检索特定文档 |

这些包含于 Aspire CLI 13.2（[PR #14028](https://github.com/dotnet/aspire/pull/14028)）。要更新：`aspire update --self --channel daily`。参考： https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** —— MCP 服务器提供集成查找（`list_integrations`, `get_integration_docs`），但**不**提供文档搜索。回退使用 Context7：

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | 主要 —— 指南、集成、CLI 参考、部署 |
| `/dotnet/aspire` | 运行时源码 —— API 内部、实现细节 |
| `/communitytoolkit/aspire` | 社区集成 —— Go、Java、Node.js、Ollama |

### VS Code — 使用 Context7

VS Code 文档位于 **code.visualstudio.com**，而不是 Learn。

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | 用户文档 —— 设置、功能、调试、远程开发 |
| `/websites/code_visualstudio_api` | 扩展 API —— webviews、TreeViews、命令、贡献点 |

### GitHub — 使用 Context7

GitHub 文档位于 **docs.github.com** 和 **cli.github.com**。

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions、API、仓库、安全、管理、Copilot |
| `/websites/cli_github` | GitHub CLI（`gh`）命令和标志 |

### Agent Framework — 使用 Learn MCP + Context7

Agent Framework 教程位于 learn.microsoft.com（使用 `microsoft_docs_search`），但 **GitHub 仓库** 包含经常领先于已发布文档的 API 级别细节 —— 特别是 DevUI REST API 参考、CLI 选项和 .NET 集成。

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | 教程 —— DevUI 指南、追踪、工作流编排 |
| `/microsoft/agent-framework` | API 细节 —— DevUI REST 端点、CLI 标志、身份验证、.NET `AddDevUI`/`MapDevUI` |

**DevUI 提示：** 先查询 Learn 网站源码以获取操作指南，然后查询仓库源码以获取 API 级别的具体信息（端点模式、代理配置、身份验证令牌）。

---

## Context7 设置

对于任何 Context7 查询，首先解析 library ID（每会话一次）：

1. 调用 `mcp_context7_resolve-library-id` 并传入技术名称
2. 调用 `mcp_context7_query-docs` 并使用返回的 library ID 以及具体查询

---

## 编写有效的查询

要具体 —— 包含版本、意图和语言：

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
免责声明：
本文件已使用 AI 翻译服务 Co‑op Translator（https://github.com/Azure/co-op-translator）进行翻译。尽管我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威版本。对于关键信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或曲解，我们不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->