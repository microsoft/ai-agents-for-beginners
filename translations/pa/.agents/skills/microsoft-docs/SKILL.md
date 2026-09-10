---
name: microsoft-docs
---
# Microsoft Docs

Microsoft ਤਕਨਾਲੋਜੀ ਇਕੋਸਿਸਟਮ ਲਈ ਰਿਸਰਚ ਸਕਿਲ। ਇਹ learn.microsoft.com ਅਤੇ ਉਸ ਤੋਂ ਬਾਹਰ ਰਹਿਣ ਵਾਲੀ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ (VS Code, GitHub, Aspire, Agent Framework ਰੇਪੋਜ਼).

---

## Default: Microsoft Learn MCP

ਇਹ ਟੂਲ ਵਰਤੋ ਲਈ **learn.microsoft.com ਉਤੇ ਸਭ ਕੁਝ** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, ਅਤੇ ਹੋਰ। ਇਹ ਜ਼ਿਆਦਾਤਰ Microsoft ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਪੁੱਛਗਿੱਛ ਲਈ ਮੁੱਖ ਟੂਲ ਹੈ।

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Search learn.microsoft.com — ਸੰਕਲਪ, ਗਾਈਡ, ਟਿਊਟੋਰਿਅਲ, ਕਨਫਿਗਰੇਸ਼ਨ |
| `microsoft_code_sample_search` | Learn ਡੌਕਸ ਵਿਚੋਂ ਕੰਮ ਕਰਨ ਵਾਲੇ ਕੋਡ ਸਨਿਪੇਟ ਲੱਭੋ। ਸਭ ਤੋਂ ਵਧੀਆ ਨਤੀਜਿਆਂ ਲਈ `language` (`python`, `csharp`, ਆਦਿ) ਪਾਸ ਕਰੋ |
| `microsoft_docs_fetch` | ਕਿਸੇ ਨਿਰਧਾਰਿਤ URL ਤੋਂ ਪੂਰਾ ਪੰਨਾ ਦੀ ਸਮੱਗਰੀ ਪ੍ਰਾਪਤ ਕਰੋ (ਜਦੋਂ ਖੋਜ ਦੇ ਉਲਲੇਖ ਕਾਫੀ ਨਹੀਂ ਹੁੰਦੇ) |

ਜਦੋਂ ਤੁਹਾਨੂੰ ਪੂਰੇ ਟਿਊਟੋਰਿਅਲ, ਸਾਰੇ ਕਨਫਿਗ ਵਿਕਲਪਾਂ ਦੀ ਲੋੜ ਹੋਵੇ ਜਾਂ ਖੋਜ ਦੇ ਉਲਲੇਖ ਕੱਟ ਦਿੱਤੇ ਜਾਣ, ਤਾਂ ਖੋਜ ਤੋਂ ਬਾਅਦ `microsoft_docs_fetch` ਵਰਤੋਂ ਕਰੋ।

---

## Exceptions: When to Use Other Tools

ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਸ਼੍ਰੇਣੀਆਂ **learn.microsoft.com ਦੇ ਬਾਹਰ** ਰਹਿੰਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਬਜਾਇ ਨਿਰਧਾਰਿਤ ਟੂਲ ਵਰਤੋ।

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire ਡੌਕਸ **aspire.dev** 'ਤੇ ਹੁੰਦੇ ਹਨ, Learn 'ਤੇ ਨਹੀਂ। ਸਭ ਤੋਂ ਵਧੀਆ ਟੂਲ ਤੁਹਾਡੇ Aspire CLI ਸੰਸਕਰਣ 'ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ:

**CLI 13.2+** (ਸਿਫਾਰਸ਼ ਕੀਤੀ) — Aspire MCP ਸਰਵਰ ਵਿੱਚ ਇੰਬਿਲਟ ਡੌਕਸ ਖੋਜ ਟੂਲ ਸ਼ਾਮਿਲ ਹਨ:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | aspire.dev ਤੋਂ ਸਾਰੀ ਉਪਲਬਧ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਦੀ ਸੂਚੀ ਦਿਖਾਉਂਦਾ ਹੈ |
| `search_docs` | aspire.dev ਸਮੱਗਰੀ 'ਤੇ ਵਜ਼ਨੀ ਸ਼ਬਦਿਕ ਖੋਜ |
| `get_doc` | ਇੱਕ ਖ਼ਾਸ ਦਸਤਾਵੇਜ਼ ਨੂੰ slug ਰਾਹੀਂ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ |

ਇਹ Aspire CLI 13.2 ਨਾਲ ਸ਼ਿਪ ਹੁੰਦੇ ਹਨ ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). ਅਪਡੇਟ ਕਰਨ ਲਈ: `aspire update --self --channel daily`. ਸੰਦਰਭ: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP ਸਰਵਰ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਲੁੱਕਅਪ (`list_integrations`, `get_integration_docs`) ਮੁਹੱਈਆ ਕਰਦਾ ਹੈ ਪਰ ਡੌਕਸ ਖੋਜ ਨਹੀਂ। Context7 ਨੂੰ ਵਰਤੋ:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | ਮੁੱਖ — ਗਾਈਡ, ਇੰਟੀਗ੍ਰੇਸ਼ਨ, CLI ਰੈਫਰੈਂਸ, ਡਿਪਲੋਇਮੈਂਟ |
| `/dotnet/aspire` | ਰਨਟਾਈਮ ਸੋਰਸ — API ਅੰਦਰੂਨੀ ਹਿੱਸੇ, ਇੰਪਲੀਮੇੰਟੇਸ਼ਨ ਵੇਰਵੇ |
| `/communitytoolkit/aspire` | ਕਮਿਊਨਿਟੀ ਇੰਟੀਗ੍ਰੇਸ਼ਨ — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code ਡੌਕਸ **code.visualstudio.com** 'ਤੇ ਹਨ, Learn 'ਤੇ ਨਹੀਂ।

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | ਯੂਜ਼ਰ ਡੌਕਸ — ਸੈਟਿੰਗਜ਼, ਫੀਚਰ, ਡੀਬੱਗਿੰਗ, ਰਿਮੋਟ ਡਿਵੈਲਪਮੈਂਟ |
| `/websites/code_visualstudio_api` | ਐਕਸਟੈਂਸ਼ਨ API — webviews, TreeViews, ਕਮਾਂਡ, ਯੋਗਦਾਨ ਦੇ ਨੁਕਤੇ |

### GitHub — Use Context7

GitHub ਡੌਕਸ **docs.github.com** ਅਤੇ **cli.github.com** 'ਤੇ ਹਨ।

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, ਰਿਪੋਜ਼, ਸੁਰੱਖਿਆ, ਪ੍ਰਸ਼ਾਸਨ, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) ਦੇ ਕਮਾਂਡ ਅਤੇ ਫਲੈਗ |

### Agent Framework — Use Learn MCP + Context7

Agent Framework ਟਿਊਟੋਰਿਅਲ learn.microsoft.com 'ਤੇ ਹਨ (ਮਾਈਕ੍ਰੋਸੋਫਟ ਲਈ `microsoft_docs_search` ਵਰਤੋਂ), ਪਰ **GitHub repo** ਵਿੱਚ ਅਕਸਰ ਪ੍ਰਕਾਸ਼ਿਤ ਡੌਕਸ ਤੋਂ ਆਗੇ API-ਸਤਰ ਦੇ ਵੇਰਵੇ ਹੁੰਦੇ ਹਨ — ਖਾਸ ਕਰਕੇ DevUI REST API ਰੈਫਰੈਂਸ, CLI ਵਿਕਲਪ, ਅਤੇ .NET ਇੰਟਿਗ੍ਰੇਸ਼ਨ।

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ਟਿਊਟੋਰਿਅਲ — DevUI ਗਾਈਡ, ਟਰੇਸਿੰਗ, ਵਰਕਫਲੋ ਆਰਕੈਸਟ੍ਰੇਸ਼ਨ |
| `/microsoft/agent-framework` | API ਵੇਰਵੇ — DevUI REST ਏਂਡਪੌਇੰਟ, CLI ਫਲੈਗ, auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI ਸਲਾਹ:** ਹਾਊ-ਟੂ ਗਾਈਡਾਂ ਲਈ Learn ਵੈੱਬਸਾਈਟ ਸਰੋਤ ਨੂੰ ਪੁੱਛੋ, ਫਿਰ API-ਸਤਰ ਦੇ ਵਿਸਥਾਰਾਂ ਲਈ ਰੇਪੋ ਸਰੋਤ (ਏਂਡਪੌਇੰਟ ਸਕੀਮਾਂ, ਪ੍ਰਾਕਸੀ ਕੰਫਿਗ, auth ਟੋਕਨ) ਦੇਖੋ।

---

## Context7 Setup

ਕੋਈ ਵੀ Context7 ਕਵੈਰੀ ਲਈ, ਪਹਿਲਾਂ ਲਾਇਬ੍ਰੇਰੀ ID ਨੂੰ ਰਿਜ਼ੋਲਵ ਕਰੋ (ਸ਼ੈਸ਼ਨ ਵਿੱਚ ਇੱਕ ਵਾਰੀ):

1. `mcp_context7_resolve-library-id` ਨੂੰ ਤਕਨਾਲੋਜੀ ਨਾਮ ਦੇ ਨਾਲ ਕਾਲ ਕਰੋ
2. `mcp_context7_query-docs` ਨੂੰ ਵਾਪਸ ਮਿਲੀ ਲਾਇਬ੍ਰੇਰੀ ID ਅਤੇ ਇੱਕ ਨਿਰਧਾਰਿਤ ਕਵੈਰੀ ਦੇ ਨਾਲ ਕਾਲ ਕਰੋ

---

## Writing Effective Queries

ਵਿਸ਼ੇਸ਼ ਹੋਵੋ — ਸੰਸਕਰਣ, ਮਕਸਦ, ਅਤੇ ਭਾਸ਼ਾ ਸ਼ਾਮਿਲ ਕਰੋ:

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
- **ਸੰਸਕਰਣ** ਜਦੋਂ ਲਾਗੂ ਹੋਵੇ (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **ਕਾਰਜ ਦਾ ਉਦੇਸ਼** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **ਭਾਸ਼ਾ** ਬਹੁਭਾਸ਼ੀ ਡੌਕਸ ਲਈ (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰ**:
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਪਸ਼ਟਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਾਰਨ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->