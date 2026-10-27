---
name: microsoft-docs
description: Query di official Microsoft documentation to find concepts, tutorials,
  and code examples for Azure, .NET, Agent Framework, Aspire, VS Code, GitHub, and
  more. Dem dey use Microsoft Learn MCP as di default, plus Context7 and Aspire MCP
  for content wey no dey inside learn.microsoft.com.
---
# Microsoft Docs

Research skill for di Microsoft technology ecosystem. E cover learn.microsoft.com and documentation wey dey outside am (VS Code, GitHub, Aspire, Agent Framework repos).

---

## Default: Microsoft Learn MCP

Use dis tools for **everything for learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, and more. Na di main tool wey people dey use for majority of Microsoft documentation questions.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Search learn.microsoft.com — concepts, guides, tutorials, configuration |
| `microsoft_code_sample_search` | Find working code snippets from Learn docs. Pass `language` (`python`, `csharp`, etc.) for best results |
| `microsoft_docs_fetch` | Get full page content from specific URL (when search excerpts no reach) |

Use `microsoft_docs_fetch` after search when you need complete tutorials, all config options, or when search excerpts dem cut short.

---

## Exceptions: When to Use Other Tools

The following categories dey **outside** learn.microsoft.com. Use the correct tool for dem instead.

### Aspire — Use Aspire MCP Server (better) or Context7

Aspire docs dey for **aspire.dev**, no be Learn. The best tool depend on your Aspire CLI version:

**CLI 13.2+** (we recommend) — The Aspire MCP server get built-in docs search tools:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Lists all available documentation from aspire.dev |
| `search_docs` | Weighted lexical search across aspire.dev content |
| `get_doc` | Retrieves specific document by slug |

These dey come for Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). To update: `aspire update --self --channel daily`.

**CLI 13.1** — The MCP server get integration lookup (`list_integrations`, `get_integration_docs`) but no get docs search. Use Context7 instead:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Main — guides, integrations, CLI reference, deployment |
| `/microsoft/aspire` | Runtime source — API internals, implementation details |
| `/communitytoolkit/aspire` | Community integrations — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code docs dey for **code.visualstudio.com**, no be Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | User docs — settings, features, debugging, remote dev |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, commands, contribution points |

### GitHub — Use Context7

GitHub docs dey for **docs.github.com** and **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repos, security, admin, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) commands and flags |

### Agent Framework — Use Learn MCP + Context7

Agent Framework tutorials dey for learn.microsoft.com (use `microsoft_docs_search`), but the **GitHub repo** get API-level detail wey dey often ahead of published docs — specially DevUI REST API reference, CLI options, and .NET integration.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorials — DevUI guides, tracing, workflow orchestration |
| `/microsoft/agent-framework` | API detail — DevUI REST endpoints, CLI flags, auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Ask Learn website source for how-to guides, then ask the repo source for API-level things (endpoint schemas, proxy config, auth tokens).

---

## Context7 Setup

For any Context7 query, find the library ID first (one-time per session):

1. Call `mcp_context7_resolve-library-id` with the technology name
2. Call `mcp_context7_query-docs` with the returned library ID and specific query

---

## Writing Effective Queries

Make am specific — put version, intent, and language:

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
- **Version** when e dey important (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Task intent** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Language** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->