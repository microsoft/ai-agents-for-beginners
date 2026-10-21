---
name: microsoft-docs
description: ਅਧਿਕਾਰਿਕ Microsoft ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਨੂੰ ਪੁੱਛਤਾਛ ਕਰੋ ਤਾਂ ਕਿ Azure, .NET, Agent
  Framework, Aspire, VS Code, GitHub, ਅਤੇ ਹੋਰ ਵਿੱਚ ਧਾਰਣਾਵਾਂ, ਟਿਊਟੋਰਿਅਲ ਅਤੇ ਕੋਡ ਉਦਾਹਰਨਾਂ
  ਲੱਭ ਸਕੋ। ਡਿਫੌਲਟ ਵਜੋਂ Microsoft Learn MCP ਵਰਤਦਾ ਹੈ, ਜਦਕਿ ਇਸ ਤੋਂ ਬਾਹਰ ਰਹਿਣ ਵਾਲੇ ਸਮੱਗਰੀ
  ਲਈ Context7 ਅਤੇ Aspire MCP ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ।
---
# Microsoft ਦਸਤਾਵੇਜ਼

Microsoft ਤਕਨਾਲੋਜੀ ਪਰਿਆਵਰਨ ਲਈ ਸਰਗਰਮੀ ਹੁਨਰ। learn.microsoft.com ਅਤੇ ਇਸ ਤੋਂ ਬਾਹਰ ਮੌਜੂਦ ਦਸਤਾਵੇਜ਼ (VS ਕੋਡ, GitHub, Aspire, Agent Framework ਰਿਪੋਜ਼) ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ।

---

## ਡਿਫੌਲਟ: Microsoft Learn MCP

ਇਨ੍ਹਾਂ ਟੂਲਜ਼ ਨੂੰ **learn.microsoft.com ਉੱਤੇ ਸਭ ਕੁਝ ਲਈ** ਵਰਤੋਂ ਕਰੋ — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, ਅਤੇ ਹੋਰ। ਇਹ ਮਾਇਕ੍ਰੋਸਾਫਟ ਦਸਤਾਵੇਜ਼ ਪ੍ਰਸ਼ਨਾਂ ਦੀ ਬਹੁਤ ਜ਼ਿਆਦਾ ਸਾਂਝ ਲਈ ਮੁੱਖ ਟੂਲ ਹੈ।

| ਟੂਲ | ਮਕਸਦ |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com ਤਲਾਸ਼ ਕਰੋ — ਧਾਰਨਾ, ਗਾਈਡ, ਟਿਊਟੋਰਿਯਲ, ਸੰਰਚਨਾ |
| `microsoft_code_sample_search` | Learn ਦਸਤਾਵੇਜ਼ਾਂ ਵਿਚੋਂ ਕੰਮ ਕਰਨ ਵਾਲੇ ਕੋਡ ਸਨਿੱਪੇਟ ਲੱਭੋ। ਵਧੀਆ ਨਤੀਜੇ ਲਈ `language` (`python`, `csharp`, ਆਦਿ) ਪਾਸ ਕਰੋ |
| `microsoft_docs_fetch` | ਇੱਕ ਖ਼ਾਸ URL ਤੋਂ ਪੂਰਾ ਪੰਨਾ ਸਮੱਗਰੀ ਪ੍ਰਾਪਤ ਕਰੋ (ਜਦੋਂ ਤਲਾਸ਼ ਨੰੂ ਛੋਟੇ ਅੰਸ਼ ਹੀ ਮਿਲਦੇ ਹਨ) |

ਜਦੋਂ ਤੁਹਾਨੂੰ ਪੂਰੇ ਟਿਊਟੋਰਿਯਲ, ਸਾਰੀ ਸੰਰਚਨਾ ਵਿਕਲਪਾਂ ਦੀ ਲੋੜ ਹੋਵੇ ਜਾਂ ਜਦੋਂ ਤਲਾਸ਼ ਅੰਸ਼ ਕੱਟੇ ਜਾਣ, ਤਾਂ ਤਲਾਸ਼ ਤੋਂ ਬਾਅਦ `microsoft_docs_fetch` ਵਰਤੋਂ।

---

## ਛੂਟ: ਕਿਹੜੇ ਸਮੇਂ ਹੋਰ ਟੂਲ ਵਰਤਣੇ

ਹੇਠ ਲਿਖੀਆਂ ਸ਼੍ਰੇਣੀਆਂ **learn.microsoft.com ਤੋਂ ਬਾਹਰ** ਹਨ। ਇਨ੍ਹਾਂ ਲਈ ਦਿੱਤੇ ਟੂਲ ਦੀ ਵਰਤੋਂ ਕਰੋ।

### Aspire — Aspire MCP ਸਰਵਰ (ਪਸੰਦੀਦਾ) ਜਾਂ Context7 ਵਰਤੋ

Aspire ਦਸਤਾਵੇਜ਼ **aspire.dev** 'ਤੇ ਹਨ, Learn ਉੱਤੇ ਨਹੀਂ। ਸਭ ਤੋਂ ਵਧੀਆ ਟੂਲ ਤੁਹਾਡੇ Aspire CLI ਵਰਜਨ 'ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ:

**CLI 13.2+** (ਸੁਝਾਅਕਾਰ) — Aspire MCP ਸਰਵਰ ਵਿੱਚ ਬਿਲਟ-ਇਨ ਦਸਤਾਵੇਜ਼ ਤਲਾਸ਼ ਟੂਲ ਸ਼ਾਮਲ ਹਨ:

| MCP ਟੂਲ | ਵੇਰਵਾ |
|----------|-------------|
| `list_docs` | aspire.dev ਤੋਂ ਸਾਰਾ ਦਸਤਾਵੇਜ਼ ਦਿਖਾਉਂਦਾ ਹੈ |
| `search_docs` | aspire.dev ਸਮੱਗਰੀ ‘ਤੇ ਵਜ਼ਨੀ ਲੈਕਸੀਕਲ ਤਲਾਸ਼ |
| `get_doc` | ਕਿਸੇ ਖ਼ਾਸ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਸਲੱਗ ਦੁਆਰਾ ਲਿਆਉਂਦਾ ਹੈ |

ਇਹ Aspire CLI 13.2 ਵਿੱਚ ਆਉਂਦੇ ਹਨ ([PR #14028](https://github.com/microsoft/aspire/pull/14028))। ਅਪਡੇਟ ਕਰਨ ਲਈ: `aspire update --self --channel daily`।

**CLI 13.1** — MCP ਸਰਵਰ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਲੁੱਕਅੱਪ (`list_integrations`, `get_integration_docs`) ਦਿੰਦਾ ਹੈ ਪਰ ਦਸਤਾਵੇਜ਼ ਤਲਾਸ਼ ਨਹੀ। ਇਸ ਲਈ Context7 ਤੇ ਵਾਪਸ ਜਾਓ:

| ਲਾਇਬ੍ਰੇਰੀ ID | ਇਸ ਲਈ ਵਰਤੋਂ ਕਰੋ |
|---|---|
| `/microsoft/aspire.dev` | ਮੁੱਖ —ਗਾਈਡ, ਇੰਟੀਗ੍ਰੇਸ਼ਨ, CLI ਰੈਫਰੈਂਸ, ਡਿਪਲੋਇਮੈਂਟ |
| `/microsoft/aspire` | ਰਨਟਾਈਮ ਸਰੋਤ — API ਅੰਦਰੂਨੀ ਵੇਰਵਾ, ਅਮਲ ਦਰਜਾ |
| `/communitytoolkit/aspire` | ਕਮਿਉਨਿਟੀ ਇੰਟੀਗ੍ਰੇਸ਼ਨ — Go, Java, Node.js, Ollama |

### VS ਕੋਡ — Context7 ਵਰਤੋਂ

VS ਕੋਡ ਦਸਤਾਵੇਜ਼ **code.visualstudio.com** 'ਤੇ ਹਨ, Learn 'ਤੇ ਨਹੀਂ।

| ਲਾਇਬ੍ਰੇਰੀ ID | ਇਸ ਲਈ ਵਰਤੋਂ ਕਰੋ |
|---|---|
| `/websites/code_visualstudio` | ਯੂਜ਼ਰ ਦਸਤਾਵੇਜ਼ — ਸੈਟਿੰਗ, ਫੀਚਰ, ਡੀਬੱਗਿੰਗ, ਰਿਮੋਟ ਡੈਵ |
| `/websites/code_visualstudio_api` | ਐਕਸਟੈਂਸ਼ਨ API — ਵੈਬਵਿਊ, ਟ੍ਰੀਵਿਊ, ਕਮਾਂਡ, ਯੋਗਦਾਨ ਪੁਆਇੰਟ |

### GitHub — Context7 ਵਰਤੋਂ

GitHub ਦਸਤਾਵੇਜ਼ **docs.github.com** ਅਤੇ **cli.github.com** ਉੱਤੇ ਹਨ।

| ਲਾਇਬ੍ਰੇਰੀ ID | ਇਸ ਲਈ ਵਰਤੋਂ ਕਰੋ |
|---|---|
| `/websites/github_en` | ਐਕਸ਼ਨ, API, ਰਿਪੋ, ਸੁਰੱਖਿਆ, ਐਡਮਿਨ, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) ਕਮਾਂਡ ਅਤੇ ਫਲੈਗ |

### Agent Framework — Learn MCP + Context7 ਵਰਤੋਂ

Agent Framework ਟਿਊਟੋਰਿਯਲ learn.microsoft.com ਉੱਤੇ ਹਨ (`microsoft_docs_search` ਵਰਤੋਂ ਕਰੋ), ਪਰ **GitHub ਰਿਪੋ** ਵਿੱਚ API-ਸਤਰ ਦੇ ਵੇਰਵਿਆਂ ਹਨ ਜੋ ਅਕਸਰ ਪ੍ਰਕਾਸ਼ਿਤ ਦਸਤਾਵੇਜ਼ਾਂ ਤੋਂ ਅੱਗੇ ਹੁੰਦੇ ਹਨ — ਖ਼ਾਸ ਕਰਕੇ DevUI REST API ਸੰਦਰਭ, CLI ਵਿਕਲਪ, ਅਤੇ .NET ਇੰਟੀਗ੍ਰੇਸ਼ਨ।

| ਲਾਇਬ੍ਰੇਰੀ ID | ਇਸ ਲਈ ਵਰਤੋਂ ਕਰੋ |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ਟਿਊਟੋਰਿਯਲ — DevUI ਗਾਈਡ, ਟਰੇਸਿੰਗ, ਵਰਕਫਲੋ ਆਰਕੈसਟਰੈਸ਼ਨ |
| `/microsoft/agent-framework` | API ਵੇਰਵਾ — DevUI REST ਐਂਡਪੌਇੰਟ, CLI ਫਲੈਗ, ਪ੍ਰਮਾਣਿਕਤਾ, .NET `AddDevUI`/`MapDevUI` |

**DevUI ਸੁਝਾਅ:** Learn ਵੈਬਸਾਈਟ ਸਰੋਤ ਤੋਂ ਕਿਵੇਂ-ਕਰਣਾ ਗਾਈਡ ਲਈ ਪੁੱਛਗਿੱਛ ਕਰੋ, ਫਿਰ API-ਸਤਰ ਦੇ ਵਿਸ਼ੇਸ਼ਤਾ (ਐਂਡਪੌਇੰਟ ਸਕੀਮਾ, ਪ੍ਰਾਕਸੀ ਸੰਰਚਨਾ, ਪ੍ਰਮਾਣਿਕਤਾ ਟੋਕਨ) ਲਈ ਰਿਪੋ ਸਰੋਤ ਨੂੰ ਵੇਖੋ।

---

## Context7 ਸੈੱਟਅਪ

ਕਿਸੇ ਵੀ Context7 ਪੁੱਛਗਿੱਛ ਲਈ, ਪਹਿਲਾਂ ਲਾਇਬ੍ਰੇਰੀ ID ਨਿਰਧਾਰਿਤ ਕਰੋ (ਹਰ ਸੈਸ਼ਨ ਵਿੱਚ ਇੱਕ ਵਾਰੀ):

1. `mcp_context7_resolve-library-id` ਨੂੰ ਟੈਕਨਾਲੋਜੀ ਨਾਮ ਦੇ ਕੇ ਕਾਲ ਕਰੋ
2. ਪਰਤਾਇਆ ਲਾਇਬ੍ਰੇਰੀ ID ਅਤੇ ਖ਼ਾਸ ਪੁੱਛਗਿੱਛ ਨਾਲ `mcp_context7_query-docs` ਕਾਲ ਕਰੋ

---

## ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਪੁੱਛਗਿੱਛਾਂ ਲਿਖਣਾ

ਵਿਸ਼ੇਸ਼ ਬਣੋ — ਵਰਜਨ, ਨੀਤੀ, ਅਤੇ ਭਾਸ਼ਾ ਸ਼ਾਮਲ ਕਰੋ:

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

ਸੰਦਰਭ ਸ਼ਾਮਲ ਕਰੋ:
- ਲੋੜ ਮੁਤਾਬਕ **ਵਰਜਨ** (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **ਕੰਮ ਦੀ ਨੀਤੀ** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- ਪੌਲੀਗਲੌਟ ਦਸਤਾਵੇਜ਼ ਲਈ **ਭਾਸ਼ਾ** (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->