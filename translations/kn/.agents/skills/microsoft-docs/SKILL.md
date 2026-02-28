---
name: microsoft-docs
description: Azure, .NET, Agent Framework, Aspire, VS Code, GitHub ಮತ್ತು ಇನ್ನಷ್ಟು
  ವಿಷಯಗಳ ಕುರಿತು ಸಿದ್ಧಾಂತಗಳು, ಟ್ಯುಟೋರಿಯಲ್ಗಳು ಮತ್ತು ಕೋಡ್ ಉದಾಹರಣೆಗಳನ್ನು ಹುಡುಕಲು ಅಧಿಕೃತ
  Microsoft ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಅನ್ನು ಶೋಧಿಸಿ. ಡೀಫಾಲ್ಟ್‌ವಾಗಿ Microsoft Learn MCP ಅನ್ನು ಬಳಸುತ್ತದೆ
  ಮತ್ತು learn.microsoft.com ನ ಹೊರಗಿನ ವಿಷಯಗಳಿಗೆ Context7 ಮತ್ತು Aspire MCP ಅನ್ನು ಬಳಸುತ್ತದೆ.
---
# Microsoft Docs

Microsoft ತಂತ್ರಜ್ಞಾನ ಪ್ರಣಾಲಿಕೆಯಿಗಾಗಿ ಸಂಶೋಧನಾ ಕೌಶಲ್ಯ. learn.microsoft.com ಮತ್ತು ಅದರ ಹೊರಗೆ ಇರುವ ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳು (VS Code, GitHub, Aspire, Agent Framework ರೆಪೋಗಳು) ಅನ್ನು ಒಳಗೊಂಡಿರುತ್ತದೆ.

---

## Default: Microsoft Learn MCP

ಈ ಸಾಧನಗಳನ್ನು **learn.microsoft.com**上的 ಎಲ್ಲದರಿಗಾಗಿ ಬಳಸಿರಿ — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows ಮತ್ತು ಇನ್ನಷ್ಟು. ಬಹುಮತದ Microsoft ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಪ್ರಶ್ನೆಗಳಿಗಾಗಿ ಇದು ಪ್ರಾಥಮಿಕ ಸಾಧನವಾಗಿದೆ.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com ಅನ್ನು ಹುಡುಕಿ — ಪರಿಕಲ್ಪನೆಗಳು, ಮಾರ್ಗದರ್ಶಿಗಳು, ಟ್ಯುಟೋರಿಯಲ್‌ಗಳು, ಕಾನ್ಫಿಗರೇಶನ್ |
| `microsoft_code_sample_search` | Learn ಡಾಕ್ಸ್‌ನಿಂದ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಕೋಡ್ ಸ್ನಿಪೆට්‌ಗಳನ್ನು ಹುಡುಕಿ. ಉತ್ತಮ ಫಲಿತಾಂಶಕ್ಕಾಗಿ `language` (`python`, `csharp`, ಇತ್ಯಾದಿ) ಅನ್ನು ಪಾಸ್ ಮಾಡಿ |
| `microsoft_docs_fetch` | ನಿರ್ದಿಷ್ಟ URL ನಿಂದ ಸಂಪೂರ್ಣ ಪುಟದ ವಿಷಯವನ್ನು ಪಡೆಯಿರಿ (ಹುಡುಕಾಟ ಉದ್ಧರಣಗಳು ಸಾಕಾಗದಾಗ) |

ಹುಡುಕಾಟದ ನಂತರ ಸಂಪೂರ್ಣ ಟ್ಯುಟೋರಿಯಲ್ಗಳು, ಎಲ್ಲಾ ಕಾನ್ಫಿಗ್ ಆಯ್ಕೆಗಳು ಅಥವಾ ಹುಡುಕಾಟ ಉದ್ಧರಣೆಗಳು ಕಡಿತಗೊಂಡಾಗ `microsoft_docs_fetch` ಅನ್ನು ಬಳಸಿ.

---

## Exceptions: When to Use Other Tools

ಕೆಳಗಿನ ವರ್ಗಗಳು learn.microsoft.com ಯಿಂದ **ಬಾಹ್ಯ**ವಾಗಿವೆ. ಬದಲಿಗೆ ನಿರ್ದಿಷ್ಟಪಡಿಸಿದ ಸಾಧನವನ್ನು ಬಳಸಿ.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire ಡಾಕ್ಸ್ **aspire.dev** ನಲ್ಲಿ ಇರುತ್ತವೆ, Learn ನಲ್ಲಿ ಅಲ್ಲ. ನಿಮ್ಮ Aspire CLI ಆವೃತ್ತಿಯ ಮೇಲೆ ಉತ್ತಮ ಸಾಧನ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ:

**CLI 13.2+** (ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ) — Aspire MCP ಸರ್ವರ್ ಒಳಗೊಂಡಿರುವ docs ಹುಡುಕಾಟ ಸಾಧನಗಳನ್ನು ಒಳಗೊಂಡಿದೆ:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | aspire.dev ನಲ್ಲಿನ ಎಲ್ಲಾ ಲಭ್ಯ ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಪಟ್ಟಿಮಾಡುತ್ತದೆ |
| `search_docs` | aspire.dev ವಿಷಯಗಳ ಮೇಲೆ ಭಾರಿತ ಲೆಕ್ಸಿಕಲ್ ಹುಡುಕಾಟ |
| `get_doc` | ಸ್ಲಗ್ನಿಂದ ನಿರ್ದಿಷ್ಟ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು ಪಡೆಯುತ್ತದೆ |

ಇವು Aspire CLI 13.2 ನಲ್ಲಿ ಸೇರಿವೆ ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). ಅಪ್‌ಡೇಟ್ ಮಾಡಲು: `aspire update --self --channel daily`. ಉಲ್ಲೇಖ: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP ಸರ್ವರ್ ಇಂಟಿಗ್ರೇಶನ್ ಲುಕಪ್ (`list_integrations`, `get_integration_docs`) ಒದಗಿಸುತ್ತದೆ ಆದರೆ ಡಾಕ್ಸ್ ಹುಡುಕಾಟವನ್ನು ಒದಗಿಸುವುದಿಲ್ಲ. ಈ ಸಂದರ್ಭದಲ್ಲಿ Context7 ಗೆFallback ನೀಡಿ:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | ಪ್ರಾಥಮಿಕ — ಮಾರ್ಗದರ್ಶಿಗಳು, ಇಂಟಿಗ್ರೇಷನ್‌ಗಳು, CLI ರೆಫರೆನ್ಸ್, ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ |
| `/dotnet/aspire` | ರನ್‌ಟೈಮ್ ಸೋರ್ಸ್ — API ಒಳಗಿನ ವರ್ಗಗಳು, ಅನುಷ್ಠಾನ ವಿವರಗಳು |
| `/communitytoolkit/aspire` | ಸಮುದಾಯ ಇಂಟಿಗ್ರೇಷನ್‌ಗಳು — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code ಡಾಕ್ಸ್ **code.visualstudio.com** ನಲ್ಲಿ ಇವೆ, Learn ನಲ್ಲಿ ಅಲ್ಲ.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | ಬಳಕೆದಾರ ಡಾಕ್ಸ್ — ಸೆಟ್ಟಿಂಗ್ಗಳು, ವೈಶಿಷ್ಟ್ಯಗಳು, ಡಿಬಗಿಂಗ್, ರಿಮೋಟ್ ಡೆವ್ |
| `/websites/code_visualstudio_api` | ಎಕ್ಸ್ಟೆನ್ಷನ್ API — webviews, TreeViews, ಕಮಾಂಡ್‌ಗಳು, ಕೊಂಟ್ರಿಬ್ಯೂಶನ್ ಪಾಯಿಂಟ್‌ಗಳು |

### GitHub — Use Context7

GitHub ಡಾಕ್ಸ್ **docs.github.com** ಮತ್ತು **cli.github.com** ನಲ್ಲಿ ಇವೆ.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, ರೆಪೋಗಳು, ಸ್ಮರಣೆ, ನಿರ್ವಹಣೆ, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) ಕಮಾಂಡ್‌ಗಳು ಮತ್ತು ಫ್ಲಾಗ್‌ಗಳು |

### Agent Framework — Use Learn MCP + Context7

Agent Framework ಟ್ಯುಟೋರಿಯಲ್‌ಗಳು learn.microsoft.com ನಲ್ಲಿ ಇವೆ (ಬಳಸಿರಿ `microsoft_docs_search`), ಆದರೆ GitHub ರೆಪೋದಲ್ಲಿ API-ಸ್ತರದ ವಿವರಗಳು ಉಲ್ಲೇಖಿತ ಡಾಕ್ಸ್ಗಿಂತ ಮುಂದಿರುವ ಅವಶ್ಯಕತೆ ಹೆಚ್ಚಿದೆ — ವಿಶೇಷವಾಗಿ DevUI REST API ರೆಫರೆನ್ಸ್, CLI ಆಯ್ಕೆಗಳು, ಮತ್ತು .NET ইಂಟಿಗ್ರೇಶನ್.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ಟ್ಯುಟೋರಿಯಲ್‌ಗಳು — DevUI ಮಾರ್ಗದರ್ಶಿಗಳು, ಟ್ರೇಸಿಂಗ್, ವರ್ಕ್‌ಫ್ಲೋ ಆರ್ಕೆಸ್ಟ್ರೇಷನ್ |
| `/microsoft/agent-framework` | API ವಿವರಗಳು — DevUI REST ಎಂಡ್ಪಾಯಿನ್‌ಟ್ಗಳು, CLI ಫ್ಲಾಗ್‌ಗಳು, ಪ್ರಮಾಣೀಕರಣ, .NET `AddDevUI`/`MapDevUI` |

DevUI ಸಲಹೆ: ಹೇಗೆ-ಮಾಡುವುದು ಮಾರ್ಗದರ್ಶಿಗಳಿಗೆ Learn ವೆಬ್‌ಸೈಟ್ ಮೂಲವನ್ನು ಪ್ರಶ್ನಿಸಿ, ನಂತರ ಎಂಡ್ಪಾಯಿನ್‌ಟ್ schemaಗಳು, ಪ್ರಾಕ್ಸಿ ಕಾನ್ಫಿಗ್, auth ಟೋಕನ್‌ಗಳು ಮುಂತಾದ API-ಸ್ತರ ವಿಶೇಷಗಳಿಗೆ ರೆಪೋ ಮೂಲವನ್ನು ನೋಡಿ.

---

## Context7 Setup

ಯಾವುದೇ Context7 ಚೊಚ್ಚಲೆಯಿಗಾಗಿ, ಮೊದಲಿಗೆ ಲೈಬ್ರರಿ ID ಅನ್ನು ಸರಹದ್ದುಮಾಡಿ (ಪ್ರತಿ ಸೆಷನ್‌ಗೆ ಒಂದು ಬಾರಿ):

1. Call `mcp_context7_resolve-library-id` with the technology name
2. Call `mcp_context7_query-docs` with the returned library ID and a specific query

---

## Writing Effective Queries

ನಿರ್ದಿಷ್ಟವಾಗಿರಿ — ಆವೃತ್ತಿ, ಉದ್ದೇಶ, ಮತ್ತು ಭಾಷೆಯನ್ನು ಸೇರಿಸಿ:

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
- **Version** ಬೇಕಾದಾಗ (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Task intent** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Language** ಬಹುಭಾಷಾ ಡಾಕ್ಸ್‌ಗಾಗಿ (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ನಿರಾಕರಣೆ:
ಈ ದಾಖಲೆ ಅನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗಾಗಿ ಪ್ರಯತ್ನಿಸಿದರೂ ಸಹ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅನಿಖರತೆಗಳು ಇರಬಹುದೆಂದು ದಯವಿಟ್ಟು ತಿಳಿದಿರಲಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿನ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗೆ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ಗೊಂದಲಗಳು ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನದ ಹೊಣೆಗಾರಿಕೆ ನಮ್ಮ ಬಳಿ ಇರುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->