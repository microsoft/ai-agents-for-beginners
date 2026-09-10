---
name: microsoft-docs
description: ಅಧಿಕೃತ Microsoft ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಅನ್ನು ಪ್ರಶ್ನೆ ಮಾಡಿ Azure, .NET, Agent
  Framework, Aspire, VS Code, GitHub ಮತ್ತು ಇತರೆ ಸಂಬಂಧಿತ ವಿಷಯಗಳ ಮೇಲೆ ತತ್ವಗಳು, ಟ್ಯುಟೋರಿಯಲ್ಗಳು
  ಮತ್ತು ಕೋಡ್ ಉದಾಹರಣೆಗಳನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ. ಡೀಫಾಲ್ಟ್‌ವಾಗಿ Microsoft Learn MCP ಅನ್ನು ಬಳಸುತ್ತದೆ;
  learn.microsoft.com ಹೊರಗಿನ ವಿಷಯಗಳಿಗೆ Context7 ಮತ್ತು Aspire MCP ಅನ್ನು ಬಳಸಲಾಗುತ್ತದೆ.
---
# Microsoft Docs

Microsoft ತಂತ್ರಜ್ಞಾನ ಪರಿಸರಕ್ಕಾಗಿ ಸಂಶೋಧನಾ ಕೌಶಲ್ಯ. Covers learn.microsoft.com ಮತ್ತು ಅದರ ಹೊರಗೆ ಇರುವ ಡಾಕ್ಯುಮೆಂಟೇಷನ್‌ಗಳನ್ನು ಒಳಗೊಂಡಿದೆ (VS Code, GitHub, Aspire, Agent Framework repos).

---

## ಡೀಫಾಲ್ಟ್: Microsoft Learn MCP

ಈ ಉಪಕರಣಗಳನ್ನು **learn.microsoft.com ನಲ್ಲಿ ಇರುವ ಎಲ್ಲಾ ವಿಷಯಗಳಿಗಾಗಿ** ಬಳಸಿ — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows ಮತ್ತು ಇತರೆ. ಇದು ಬಹುತೇಕ Microsoft ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಪ್ರಶ್ನೆಗಳಿಗಾಗಿ ಪ್ರಾಥಮಿಕ ಉಪಕರಣವಾಗಿದೆ.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com ಅನ್ನು ಹುಡುಕಿ — ಕಲ್ಪನೆಗಳು, ಮಾರ್ಗದರ್ಶಿಗಳು, ಟ್ಯುಟೋರಿಯಲ್ಗಳು, ಸಂರಚನೆ |
| `microsoft_code_sample_search` | Learn ಡಾಕ್ಸ್‌ನಿಂದ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಕೋಡ್ ಸೆಂಪಲ్స్ ಹುಡುಕಿ. ಉತ್ತಮ ಫಲಿತಾಂಶಕ್ಕಾಗಿ `language` (`python`, `csharp`, ಇತ್ಯಾದಿ) ಪಾಸ್ ಮಾಡಿ |
| `microsoft_docs_fetch` | ನಿರ್ದಿಷ್ಟ URL ನಿಂದ ಸಂಪೂರ್ಣ ಪುಟದ ವಿಷಯ ಪಡೆಯಿರಿ (ಹುಡುಕಾಟ ಉಲ್ಲೇಖಗಳು ಸಾಕಾಗದಾಗ) |

ಹುಡುಕಾಟದ ನಂತರ ಸಂಪೂರ್ಣ ಟ್ಯೂಟೋರಿಯಲ್ಸ್, ಎಲ್ಲಾ ಕಾಂಫಿಗ್ ಆಯ್ಕೆಗಳು, ಅಥವಾ ಹುಡುಕಾಟ ಉಲ್ಲೇಖಗಳು ಕತ್ತರಿಸಲಾಗಿದೆಯಾದರೆ `microsoft_docs_fetch` ಅನ್ನು ಬಳಸಿ.

---

## ಬೇರೆ ಉಪಕರಣಗಳನ್ನು ಬಳಸಬೇಕಾಗುವ ಸಂದರ್ಭಗಳು

ಕೆಳಗಿನ ವರ್ಗಗಳು **learn.microsoft.com ರ ಹೊರಗೆ** ಇವೆ. ಬದಲಾಗಿ ನಿಗದಿಗೊಂಡಿರುವ ಉಪಕರಣವನ್ನು ಬಳಸಿ.

### .NET Aspire — Aspire MCP ಸರ್ವರ್ ಬಳಸಿ (ಶಿಫಾರಸು) ಅಥವಾ Context7

Aspire ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳು **aspire.dev** ನಲ್ಲಿ ಇವೆ, Learn ನಲ್ಲಿ ಅಲ್ಲ. ಉತ್ತಮ ಉಪಕರಣವು ನಿಮ್ಮ Aspire CLI ಆವೃತ್ತಿಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುತ್ತದೆ:

**CLI 13.2+** (ಶಿಫಾರಸು) — Aspire MCP ಸರ್ವರ್‌ನಲ್ಲಿ ಒಳಗೊಂಡ ಡಾಕ್ಯುಮೆಂಟ್ ಹುಡುಕಾಟ ಉಪಕರಣಗಳು ಇವೆ:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | aspire.dev‌ನಿಂದ ಲಭ್ಯವಿರುವ ಎಲ್ಲಾ ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುತ್ತದೆ |
| `search_docs` | aspire.dev ವಿಷಯದ ಮೇಲೆ ತೂಕದ ಲೆಕ್ಸಿಕಲ್ ಹುಡುಕಾಟ |
| `get_doc` | ಶ್ಲಗ್ ಮೂಲಕ ನಿರ್ದಿಷ್ಟ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು ಪಡೆಯುತ್ತದೆ |

ಈವು Aspire CLI 13.2 ನಲ್ಲಿ ಶಿಪ್ ಆಗುತ್ತವೆ ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). ಅಪ್‌ಡೇಟ್ ಮಾಡಲು: `aspire update --self --channel daily`. ಉಲ್ಲೇಖ: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP ಸರ್ವರ್ ಇಂಟಿಗ್ರೇಷನ್ ಹುಡುಕಾಟ (`list_integrations`, `get_integration_docs`) ಅನ್ನು ಒದಗಿಸುತ್ತದೆ ಆದರೆ ಡಾಕ್ಸ್ ಹುಡುಕಾಟವನ್ನು **ಕೊಡುವುದಿಲ್ಲ**. Context7 ಗೆ ಮರಳಿರಿ:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | ಪ್ರಾಥಮಿಕ — ಮಾರ್ಗದರ್ಶಿಗಳು, ಇಂಟಿಗ್ರೇಷನ್ಗಳು, CLI ರೆಫರೆನ್ಸ್, ಡಿಪ್ಲೊಯ್ಮೆಂಟ್ |
| `/dotnet/aspire` | ರನ್‌ಟೈಮ್ ಮೂಲ — API ಅಂತರಂಗ, ಜಾರಿಗೆ ಸಂಬಂಧಿಸಿದ ವಿವರಗಳು |
| `/communitytoolkit/aspire` | ಸಮುದಾಯ ಇಂಟಿಗ್ರೇಷನ್ಗಳು — Go, Java, Node.js, Ollama |

### VS Code — Context7 ಬಳಸಿ

VS Code ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳು **code.visualstudio.com** ನಲ್ಲಿ ಇವೆ, Learn ನಲ್ಲಿ ಅಲ್ಲ.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | ಬಳಕೆದಾರ ಡಾಕ್ಸ್ — ಸೆಟ್ಟಿಂಗ್ಗಳು, ವೈಶಿಷ್ಟ್ಯಗಳು, ಡೀಬಗಿಂಗ್, ರಿಮೋಟ್ ಡೆವ್ |
| `/websites/code_visualstudio_api` | ವಿಸ್ತರಣಾ API — webviews, TreeViews, ಆಜ್ಞೆಗಳು, ಕೊಡುಗೆ ಬಿಂದುಗಳು |

### GitHub — Context7 ಬಳಸಿ

GitHub ಡಾಕ್ಸ್ **docs.github.com** ಮತ್ತು **cli.github.com** ನಲ್ಲಿ ಇವೆ.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, ರೆಪೋಗಳು, ಭದ್ರತೆ, ಆಡಳಿತ, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) ಆಜ್ಞೆಗಳು ಮತ್ತು ಫ್ಲ್ಯಾಗ್ಗಳು |

### Agent Framework — Learn MCP + Context7 ಬಳಸಿ

Agent Framework ಟ್ಯೂಟೋರಿಯಲ್ಗಳು learn.microsoft.com ಮೇಲೆ ಇವೆ (`microsoft_docs_search` ಬಳಸಿ), ಆದರೆ **GitHub ರೆಪೊ**ನಲ್ಲಿ ಪ್ರಸಿದ್ಧ ಡಾಕ್ಸ್‌ಗಿಂತ ಮುಂದಿರುವ API-ಮಟ್ಟದ ವಿವರಗಳಿವೆ — ವಿಶೇಷವಾಗಿ DevUI REST API ರೆಫರೆನ್ಸ್, CLI ಆಯ್ಕೆಗಳು, ಮತ್ತು .NET ಇಂಟಿಗ್ರೇಷನ್.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ಟ್ಯೂಟೋರಿಯಲ್ಗಳು — DevUI ಮಾರ್ಗದರ್ಶಿಗಳು, ಟ್ರೇಸಿಂಗ್, ವರ್ಕ್ಫ್ಲೋ ಸಂಘಟನೆ |
| `/microsoft/agent-framework` | API ವಿವರ — DevUI REST ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳು, CLI ಫ್ಲ್ಯಾಗ್ಗಳು, auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI ಟിപ್:** Learn ವೆಬ್‌ಸೈಟ್ ಮೂಲವನ್ನು how-to ಮಾರ್ಗದರ್ಶಿಗಳಿಗಾಗಿ ವಿಚಾರಿಸಿ, ಮತ್ತು ನಂತರ API-ಮಟ್ಟದ ವಿವರಗಳಿಗಾಗಿ ರೆಪೊ ಮೂಲವನ್ನು ಪರಿಶೀಲಿಸಿ (ಎಂಡ್ಪಾಯಿಂಟ್ ಸ್ಕೀಮಾಗಳು, ಪ್ರಾಕ್ಸಿ ಸಂರಚನೆ, auth ಟೋಕನ್ಗಳು).

---

## Context7 ಸೆಟ್‌ಅಪ್

ಯಾವುದೇ Context7 ಪ್ರಶ್ನೆಗಾಗಿ, ಮೊದಲು ಲೈಬ್ರರಿ ID ಅನ್ನು ಪರಿಹರಿಸಿ (ಒಂದು ಬಾರಿ ಪ್ರತಿ ಸೆಷನ್‌ಗಾಗಿ):

1. ತಂತ್ರಜ್ಞಾನದ ಹೆಸರಿನೊಂದಿಗೆ `mcp_context7_resolve-library-id` ಅನ್ನು ಕರೆ ಮಾಡಿ
2. ಮರಳಿಸಿದ ಲೈಬ್ರರಿ ID ಮತ್ತು ನಿರ್ದಿಷ್ಟ ಕ್ವೇರಿಯನ್ನು ಬಳಸಿ `mcp_context7_query-docs` ಅನ್ನು ಕರೆ ಮಾಡಿ

---

## ಪರಿಣಾಮಕಾರಿ ಕ್ವೆರಿಗಳು ಬರೆಯುವುದು

ನಿಖರವಾಗಿರಿ — ಆವೃತ್ತಿ, ಉದ್ದೇಶ, ಮತ್ತು ಭಾಷೆ ಸೇರಿಸಿ:

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
- **ಆವೃತ್ತಿ** ಸಂಬಂಧಿಸಿದಾಗ (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **ಕಾರ್ಯ ಉದ್ದೇಶ** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **ಭಾಷೆ** ಬಹುಭಾಷಾ ಡಾಕ್ಸ್‌ಗೆ (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ನಿರಾಕರಣೆ**:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಮೂಲಕ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗೆ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸೂಕ್ತತೆಗಳು ಇರಬಹುದೇ ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಅಥವಾ ನಿರ್ಣಾಯಕ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗ्रहಣ ಅಥವಾ ತಪ್ಪಾದ ವ್ಯಾಖ್ಯಾನಗಳಿಗಾಗಿ ನಾವು ಜವಾಬ್ದಾರಿಯಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->