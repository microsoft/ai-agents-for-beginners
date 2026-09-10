---
name: microsoft-docs
description: Na to search official Microsoft documentation make you fit find concepts,
  tutorials, and code examples for Azure, .NET, Agent Framework, Aspire, VS Code,
  GitHub, and plenty more. E dey use Microsoft Learn MCP as the default, together
  with Context7 and Aspire MCP for content wey dey outside learn.microsoft.com.
---
# Microsoft Docs

Skill wey you fit use to do research for the Microsoft technology ecosystem. E cover learn.microsoft.com and documentation wey dey outside am (VS Code, GitHub, Aspire, Agent Framework repos).

---

## Di Default: Microsoft Learn MCP

Use these tools for **everytin for learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, and more. Na dis one be di main tool for most Microsoft documentation questions.

| Tool | Wetin e dey do |
|------|----------------|
| `microsoft_docs_search` | Search learn.microsoft.com — concepts, guides, tutorials, configuration |
| `microsoft_code_sample_search` | Find working code snippets from Learn docs. Pass `language` (`python`, `csharp`, etc.) for best results |
| `microsoft_docs_fetch` | Get full page content from a specific URL (when search excerpts aren't enough) |

Use `microsoft_docs_fetch` after search if you need full tutorials, all config options, or when search excerpts don cut.

---

## Exceptions: When to Use Other Tools

Di categories wey follow dey live **outside** learn.microsoft.com. Use di tool wey dem specify instead.

### .NET Aspire — Use Aspire MCP Server (wey better) or Context7

Aspire docs dey for **aspire.dev**, no for Learn. Di best tool depend on your Aspire CLI version:

**CLI 13.2+** (wey recommended) — The Aspire MCP server get built-in docs search tools:

| MCP Tool | Wetin e dey do |
|----------|----------------|
| `list_docs` | List all di documentation wey dey for aspire.dev |
| `search_docs` | Weighted lexical search across aspire.dev content |
| `get_doc` | Retrieve specific document by slug |

Dem ship dis for Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). To update: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — The MCP server provides integration lookup (`list_integrations`, `get_integration_docs`) but **no** docs search. Fall back to Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Primary — guides, integrations, CLI reference, deployment |
| `/dotnet/aspire` | Runtime source — API internals, implementation details |
| `/communitytoolkit/aspire` | Community integrations — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code docs dey for **code.visualstudio.com**, no for Learn.

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

Agent Framework tutorials dey for learn.microsoft.com (use `microsoft_docs_search`), but di **GitHub repo** get API-level detail wey dey ahead of wetin dem publish — especially DevUI REST API reference, CLI options, and .NET integration.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorials — DevUI guides, tracing, workflow orchestration |
| `/microsoft/agent-framework` | API detail — DevUI REST endpoints, CLI flags, auth, .NET `AddDevUI`/`MapDevUI` |

DevUI tip: Query di Learn website source for how-to guides first, then check di repo source for API-level specifics (endpoint schemas, proxy config, auth tokens).

---

## Context7 Setup

For any Context7 query, resolve the library ID first (one-time per session):

1. Call `mcp_context7_resolve-library-id` with di technology name
2. Call `mcp_context7_query-docs` with di returned library ID and a specific query

---

## Writing Effective Queries

Make e specific — include version, intent, and language:

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
- **Version** when e relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Task intent** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Language** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis dokument na AI translate — we take Co‑op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, make you sabi say automated translations fit get mistakes or no 100% accurate. The original dokument for im original language na the correct/official source. If na important matter, make you use professional human translator. We no go responsible for any misunderstanding or wrong interpretation wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->