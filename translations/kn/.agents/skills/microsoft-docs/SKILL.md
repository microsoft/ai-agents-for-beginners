---
name: microsoft-docs
---
# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಡಾಕ್ಸ್

ಮೈಕ್ರೋಸಾಫ್ಟ್ ತಂತ್ರಜ್ಞಾನ ಪರಿಸರಕ್ಕಾಗಿ ಸಂಶೋಧನಾ ಕೌಶಲ್ಯ. learn.microsoft.com ಮತ್ತು ಅದರ ಹೊರಗೆ ಇರುವ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ (VS ಕೋಡ್, GitHub, Aspire, ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ರೆಪೊಗಳು) ಅನ್ನು ಒಳಗೊಂಡಿದೆ.

---

## ಡೀಫಾಲ್ಟ್: Microsoft Learn MCP

**learn.microsoft.com** ನಲ್ಲಿ ಎಲ್ಲವೂ ಮಾಡಲು ಈ ಸಾಧನಗಳನ್ನು ಬಳಸಿರಿ — ಅಸ್ಯೂರ್, .NET, M365, ಪವರ್ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್, ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್, ಸೆಮಾಂಟಿಕ್ ಕರ್ಣೆಲ್, ವಿಂಡೋಸ್ ಮತ್ತು ಮತ್ತಷ್ಟು. ಇದು ಬಹುತೇಕ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಪ್ರಶ್ನೆಗಳ ಪ್ರಮುಖ ಸಾಧನ.

| ಸಾಧನ | ಉದ್ದೇಶ |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com ಹುಡುಕಿ — ಕಲ್ಪನೆಗಳು, ಮಾರ್ಗದರ್ಶಿಗಳು, ಟ್ಯುಟೋರಿಯಲ್ಗಳು, ಸಂರಚನೆ |
| `microsoft_code_sample_search` | ಲೆರ್ನ್ ಡಾಕ್ಸ್‌ನಿಂದ ಕಾರ್ಯಗತ ಮಾಡಲಾದ ಕೋಡ್ ಸಂಕೇತಗಳನ್ನು ಹುಡುಕಿ. ಉತ್ತಮ ಫಲಿತಾಂಶಕ್ಕಾಗಿ `language` (`python`, `csharp`, ಇತ್ಯಾದಿ) ಬಳಸಿ |
| `microsoft_docs_fetch` | ವಿಶೇಷ URLನಿಂದ ಸಂಪೂರ್ಣ ಪುಟದ ವಿಷಯ ಪಡೆಯಿರಿ (ಹುಡುಕು ಉದಾಹರಣೆಗಳು ಸಾಕಾಗದಾಗ) |

ಸಂಪೂರ್ಣ ಟ್ಯುಟೋರಿಯಲ್ಗಳು, ಎಲ್ಲಾ ಸಂರಚನಾ ಆಯ್ಕೆಗಳನ್ನು ಬೇಕಾದಾಗ ಅಥವಾ ಹುಡುಕು ಉದಾಹರಣೆಗಳು ಕಡಿತಗೊಂಡಾಗ `microsoft_docs_fetch` ಬಳಸಿ.

---

## ಬಾಹ್ಯ ಸಂದರ್ಭಗಳು: ಇತರ ಸಾಧನಗಳನ್ನು ಬಳಸಬೇಕಾಗಿರುವಾಗ

ಕೆಳಗಿನ ವರ್ಗಗಳು **learn.microsoft.com** ಕ್ಕಿಂತ ಹೊರಗಿನವು. ಅವುಗಳಿಗೆ ನಿರ್ದಿಷ್ಟ ಸಾಧನ ಬಳಸಿ.

### Aspire — Aspire MCP ಸರ್ವರ್ (ಆದ್ಯತೆ) ಅಥವಾ Context7 ಬಳಸಿ

Aspire ಡಾಕ್ಸ್ **aspire.dev** ನಲ್ಲಿ ಇರುತ್ತವೆ, ಲರ್ನ್ ನಲ್ಲಿ ಅಲ್ಲ. ಉತ್ತಮ ಸಾಧನ ನಿಮ್ಮ Aspire CLI ಆವೃತ್ತಿಗೆ ಅವಲಂಬನೆಯಾಗಿರುತ್ತದೆ:

**CLI 13.2+** (ಶಿಫಾರಸು) — Aspire MCP ಸರ್ವರ್ ಕುಗ್ಗಿಸಿದ ಡಾಕ್ಸ್ ಹುಡುಕು ಸಾಧನಗಳನ್ನು ಒಳಗೊಂಡಿದೆ:

| MCP ಸಾಧನ | ವಿವರಣೆ |
|----------|-------------|
| `list_docs` | aspire.dev ನಿಂದ ಲಭ್ಯವಿರುವ ಎಲ್ಲಾ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಪಟ್ಟಿಮಾಡುತ್ತದೆ |
| `search_docs` | aspire.dev ವಿಷಯದ ಮೇಲೆ ತೂಕ ಹೊಂದಿದ ಲೆಕ್ಸಿಕಲ್ ಹುಡುಕು |
| `get_doc` | ಕಂಡುಹಿಡಿದ ದಾಖಲೆ ಯನ್ನು ಸ್ಲಗ್ ಮೂಲಕ ತರುತ್ತದೆ |

ಈವುಗಳು Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)) ನಲ್ಲಿ ಕಳುಹಿಸಲಾಗಿವೆ. ನವೀಕರಿಸಲು: `aspire update --self --channel daily`.

**CLI 13.1** — MCP ಸರ್ವರ್ ಸಂಯೋಜನೆ ಹುಡುಕುವಿಕೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ (`list_integrations`, `get_integration_docs`) ಆದರೆ **ಡಾಕ್ಸ್ ಹುಡುಕು ಇಲ್ಲ.** Context7ಗೆ ಮರಳಿರಿ:

| ಲೈಬ್ರರಿ ಐಡಿ | ಯಾವಕ್ಕಾಗಿ ಉಪಯೋಗಿಸాలి |
|---|---|
| `/microsoft/aspire.dev` | ಪ್ರಾಥಮಿಕ — ಮಾರ್ಗದರ್ಶಿಗಳು, ಸಂಯೋಜನೆಗಳು, CLI ಉಲ್ಲೇಖ, ಅನುಸ್ಥಾಪನೆ |
| `/microsoft/aspire` | ರನ್‌ಟೈಮ್ ಮೂಲ — API ಒಳಗಿನ ಮಾಹಿತಿ, ಜಾರಿಗೊಳಿಸುವ ವಿವರಗಳು |
| `/communitytoolkit/aspire` | ಸಮುದಾಯ ಸಂಯೋಜನೆಗಳು — ಗೋ, ಜವಾ, ನೋಡ್.ಜೆಎಸ್, ಒಲ್ಲಾಮಾ |

### VS ಕೋಡ್ — Context7 ಬಳಸಿ

VS ಕೋಡ್ ಡಾಕ್ಸ್ **code.visualstudio.com** ನಲ್ಲಿ ಇರುತ್ತವೆ, ಲರ್ನ್ ನಲ್ಲಿ ಅಲ್ಲ.

| ಲೈಬ್ರರಿ ಐಡಿ | ಯಾವಕ್ಕಾಗಿ ಉಪಯೋಗಿಸాలి |
|---|---|
| `/websites/code_visualstudio` | ಬಳಕೆದಾರ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ — ಸೆಟ್ಟಿಂಗ್ಗಳು, ವೈಶಿಷ್ಟ್ಯಗಳು, ಡಿಬಗಿಂಗ್, ದೂರस्थ ಅಭಿವೃದ್ಧಿ |
| `/websites/code_visualstudio_api` | ಎಕ್ಸ್ಟೆನ್ಶನ್ API — ವೆಬ್‌ವ್ಯೂಗಳು, ಟ್ರೀವ್ಯೂಗಳು, ಆಜ್ಞೆಗಳು, ಕೊಡುಗೆ ಪಾಯಿಂಟ್‌ಗಳು |

### GitHub — Context7 ಬಳಸಿ

GitHub ಡಾಕ್ಸ್ **docs.github.com** ಮತ್ತು **cli.github.com** ನಲ್ಲಿ ಇರುತ್ತವೆ.

| ಲೈಬ್ರರಿ ಐಡಿ | ಯಾವಕ್ಕಾಗಿ ಉಪಯೋಗಿಸాలి |
|---|---|
| `/websites/github_en` | ಕ್ರಿಯೆಗಳು, API, ರೆಪೊಗಳು, ಭದ್ರತೆ, ನಿರ್ವಾಹক, ಕ್ಯಾಪೈಲಟ್ |
| `/websites/cli_github` | GitHub CLI (`gh`) ಆಜ್ಞೆಗಳು ಮತ್ತು ಧ್ವಜಗಳು |

### ಏಜೆಂಟ್ ಫ್ರೇಮ್ಯುವರ್ಕ್ — Learn MCP + Context7 ಬಳಸಿ

ಏಜೆಂಟ್ ಫ್ರೇಮ್ಯುವರ್ಕ್ ಟ್ಯುಟೋರಿಯಲ್ಗಳು learn.microsoft.com ನಲ್ಲಿ ಇವೆ (`microsoft_docs_search` ಬಳಸಿ), ಆದರೆ **GitHub ರೆಪೊ** ದಲ್ಲಿ ಪ್ರಕಟಿತ ಡಾಕ್ಸ್ ಗಿಂತ ಮುಂಚಿತವಾಗಿರುವ API-ಮಟ್ಟದ ವಿವರ ಇದೆ — ವಿಶೇಷವಾಗಿ DevUI REST API ಉಲ್ಲೇಖ, CLI ಆಯ್ಕೆಗಳು, ಮತ್ತು .NET ಸಂಯೋಜನೆ.

| ಲೈಬ್ರರಿ ಐಡಿ | ಯಾವതിന് ಉಪಯೋಗಿಸಬೇಕು |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ಟ್ಯುಟೋರಿಯಲ್ಗಳು — DevUI ಮಾರ್ಗದರ್ಶಿಗಳು, ಟ್ರೇಸಿಂಗ್, ವರ್ಕ್‌ಫ್ಲೋ ಒರ್ಕೆಸ್ಟ್ರೇಷನ್ |
| `/microsoft/agent-framework` | API ವಿವರ — DevUI REST ಎಂಡ್‌ಪಾಯಿಂಟ್ಸ್, CLI ಧ್ವಜಗಳು, ಪ್ರಾಮಾಣೀಕರಣ, .NET `AddDevUI`/`MapDevUI` |

**DevUI ಸೂತ್ರ:** ಹೇಗೆ ಮಾಡುವುದಕ್ಕೆ ಗೈಡ್‌ಗಳಿಗಾಗಿ ಮೊದಲಿಗೆ Learn ವೆಬ್‌ಸೈಟ್ ಮೂಲವನ್ನು, ನಂತರ API-ಮಟ್ಟದ ವಿಶೇಷಗಳಿಗಾಗಿ (ಎಂಡ್‌ಪಾಯಿಂಟ್ ಸ್ಕೀಮಾಗಳು, ಪ್ರಾಕ್ಸಿ ಸಂರಚನೆ, ಪ್ರಾಮಾಣೀಕರಣ ಟೋಕನ್‌ಗಳು) ರೆಪೊ ಮೂಲವನ್ನು ವಿಚಾರಿಸಿ.

---

## Context7 ಸೆಟಪ್

ಯಾವುದೇ Context7 ಪ್ರಶ್ನೆಗಾಗಿ, ಮೊದಲು ಲೈಬ್ರರಿ ಐಡಿ ಪರಿಹರಿಸಿರಿ (ಪ್ರತಿ ಸಷನ್ ಒ一次):

1. ತಂತ್ರಜ್ಞಾನದ ಹೆಸರಿನಿಂದ `mcp_context7_resolve-library-id`ನ್ನು ಕರೆ ಮಾಡಿ
2. ಸ್ಫುಟಿತ ಲೈಬ್ರರಿ ಐಡಿ ಮತ್ತು ನಿರ್ದಿಷ್ಟ ಪ್ರಶ್ನೆಯೊಂದಿಗೆ `mcp_context7_query-docs` ಅನ್ನು ಕರೆ ಮಾಡಿ

---

## ಪರಿಣಾಮಕಾರೀ ಪ್ರಶ್ನೆಗಳು ಬರೆಯುವುದು

ಸ್ಪಷ್ಟವಾಗಿರಿ — ಆವೃತ್ತಿ, ಉದ್ದೇಶ ಮತ್ತು ಭಾಷೆಯನ್ನು ಒಳಗೊಳ್ಳಿಸಿ:

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

ಸಂದರ್ಭವನ್ನು ಸೇರಿಸಿ:
- ಸಂಬಂಧಿಸಿದಾಗ **ಆವೃತ್ತಿ** (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **ಕಾರ್ಯದ ಉದ್ದೇಶ** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- ಬಹುಭಾಷಾ ಡಾಕ್ಸ್‌ಗಾಗಿ **ಭಾಷೆ** (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->