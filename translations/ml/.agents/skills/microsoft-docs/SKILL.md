---
name: microsoft-docs
description: Microsoft-ന്റെ ഔദ്യോഗിക ഡോക്യുമെന്റേഷൻ അന്വേഷിച്ച് Azure, .NET, Agent
  Framework, Aspire, VS Code, GitHub എന്നിവ ഉൾപ്പെടെയുള്ള മേഖലയിലെ ആശയങ്ങൾ, ട്യൂട്ടോറിയലുകൾ,
  കോഡ് ഉദാഹരണങ്ങൾ എന്നിവ കണ്ടെത്തുക. ഡിഫോൾട്ട് ആയി Microsoft Learn MCP ഉപയോഗിക്കുന്നു;
  learn.microsoft.com-ന്റെ പുറത്തുള്ള ഉള്ളടക്കങ്ങൾക്ക് Context7യും Aspire MCPയും ഉപയോഗിക്കുന്നു.
---
# Microsoft Docs

Microsoft സാങ്കേതിക പരിസ്ഥിതിക്കുള്ള റിസർച്ച് കഴിവ്. ഇതിൽ learn.microsoft.com ഉൾപ്പെടുന്നു കൂടാതെ അതിന് പുറത്തുള്ള ഡോക്യുമെന്റേഷൻകളും (VS Code, GitHub, Aspire, Agent Framework റെപ്പോകൾ) शामिल ചെയ്യും.

---

## Default: Microsoft Learn MCP

learn.microsoft.com-上的 എല്ലാത്തിലുമുള്ളവയ്ക്കായി ഈ ടൂളുകൾ ഉപയോഗിക്കുക — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, തുടങ്ങിയവ. മൈക്രോസോഫ്റ്റ് ഡോക്യുമെന്റ് ചോദനകളുടെ വലിയഭാഗത്തിനായുള്ള പ്രധാന ടൂൾ ഇതാണ്.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com-ൽ തിരയൽ — സങ്കല്പങ്ങൾ, മാർഗ്ഗനിർദ്ദേശങ്ങൾ, ട്യൂട്ടോറിയലുകൾ, കോൺഫിഗറേഷൻ |
| `microsoft_code_sample_search` | Learn ഡോകുകളിലെ പ്രവർത്തിക്കുന്ന കോഡ് സ്നിപ്പറ്റുകൾ കണ്ടെത്തുക. മികച്ച ഫലങ്ങൾക്കായി `language` (`python`, `csharp`, മുതലായവ) കൈമാറുക |
| `microsoft_docs_fetch` | ഒരു പ്രത്യേക URL-ലുള്ള പേജ് മുഴുവൻ ഉള്ളടക്കം നേടുക (തിരയൽ ഉദ്ധരണികൾ മതിയാകാത്തപ്പോൾ) |

തിരയൽ കഴിഞ്ഞ്，当需要完整的 ട്യൂട്ടോറിയലുകൾ, എല്ലാ കോൺഫിഗ് ഓപ്ഷനുകളും അല്ലെങ്കിൽ തിരയൽ ഉദ്ധരണികൾ ട്രങ്കേറ്റുചെയ്‌തപ്പോൾ, `microsoft_docs_fetch` ഉപയോഗിക്കുക.

---

## Exceptions: When to Use Other Tools

താഴെ കൊടുത്തിരിക്കുന്ന വിഭാഗങ്ങൾ learn.microsoft.com-നു പുറത്താണ്. പകരം വ്യക്തമാക്കിയ ടൂൾ ഉപയോഗിക്കുക.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire ഡോക്യുമെന്റേഷൻ **aspire.dev**-യിൽ ആണ്, Learn-ൽ അല്ല. മികച്ച ടൂൾ നിങ്ങളുടെ Aspire CLI പതിപ്പിനെ ആശ്രയിച്ചിരിക്കുന്നു:

**CLI 13.2+** (추천) — Aspire MCP സെർവർ ബിൽറ്റ്-ഇൻ ഡോക്‌സ് തിരയൽ ടൂളുകൾ ഉൾക്കൊള്ളുന്നു:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | aspire.dev-യിൽ നിന്നുള്ള ലഭ്യമായ എല്ലാ ഡോക്യുമെന്റേഷനുകളും പട്ടികപ്പെടുത്തുന്നു |
| `search_docs` | aspire.dev ഉള്ളടക്കത്തിൽ ഭാരിത ലെക്സിക്കൽ തിരയൽ |
| `get_doc` | slug ഉപയോഗിച്ച് ഒരു പ്രത്യേക ഡോക്യുമെന്റ് തിരികെയെടുക്കുന്നു |

ഇവ Aspire CLI 13.2-ൽ ഉൾപ്പെടുത്തിയിട്ടുണ്ട് ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). അപ്ഡേറ്റ് ചെയ്യാൻ: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP സെർവർ ഇന്റഗ്രേഷൻ ലുക്കപ്പ് (`list_integrations`, `get_integration_docs`) നൽകുന്നു, പക്ഷേ ഡോക്കുകൾ തിരയൽ നൽകുന്നില്ല. ഈ സാഹചര്യത്തിൽ Context7-ലേക്ക് മടങ്ങുക:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Primary — മാർഗ്ഗനിർദ്ദേശങ്ങൾ, ഇന്റഗ്രേഷനുകൾ, CLI റഫറൻസ്, ഡിപ്ലോയ്മെന്റ് |
| `/dotnet/aspire` | റൺടൈം സോഴ്‌സ് — API ഇന്റർണൽ, ഇംപ്ലിമെന്റേഷൻ വിശദാംശങ്ങൾ |
| `/communitytoolkit/aspire` | കമ്മ്യൂണിറ്റി ഇന്റഗ്രേഷനുകൾ — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code ഡോകുകൾ **code.visualstudio.com**-ൽ ആണ്, Learn-ൽ അല്ല.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | ഉപയോക്തൃ ഡോകുകൾ — സജ്ജീകരണങ്ങൾ, ഫീച്ചറുകൾ, ഡീബഗ്ഗിംഗ്, റിമോട്ട് ഡെവ് |
| `/websites/code_visualstudio_api` | എക്സ്റ്റൻഷൻ API — webviews, TreeViews, കമാൻഡുകൾ, contriution points |

### GitHub — Use Context7

GitHub ഡോകുകൾ **docs.github.com** και **cli.github.com**-ൽ ഉണ്ട്.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, റೆപ്പോസിറ്ററികൾ, സുരക്ഷ, അഡ്മിൻ, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) കമാൻഡുകളും ഫ്ലാഗുകളും |

### Agent Framework — Use Learn MCP + Context7

Agent Framework ട്യൂട്ടോറിയലുകൾ learn.microsoft.com-ൽ ആണ് (ഉപയോഗിക്കുക `microsoft_docs_search`), പക്ഷേ **GitHub repo** പ്രസിദ്ധീകരിച്ച ഡോകുകൾക്കേക്കാൾ അക്കാദമിക് API-തലത്തിൽ വിശദാംശങ്ങൾ മുമ്പേ ഉള്ളതായി കാണപ്പെടാറുണ്ട് — പ്രത്യേകിച്ച് DevUI REST API റഫറൻസ്, CLI ഓപ്ഷനുകൾ, .NET ഇന്റഗ്രേഷൻ എന്നിവ.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ട്യൂട്ടോറിയലുകൾ — DevUI മാർഗ്ഗനിർദ്ദേശങ്ങൾ, ട്രേസിംഗ്, വർക്‌ഫ്ലോ ഓർക്കസ്ട്രേഷൻ |
| `/microsoft/agent-framework` | API വിശദാംശങ്ങൾ — DevUI REST എൻഡ്പോയിന്റുകൾ, CLI ഫ്ലാഗുകൾ, ഓതെന്റിക്കേഷൻ, .NET `AddDevUI`/`MapDevUI` |

**DevUI ടിപ്പ്:** How-to ഗൈഡുകൾക്കായി Learn വെബ്സൈറ്റ് സോഴ്‌സ് ചിലവയിൽ ചോദിക്കുക, പിന്നെ API-തലത്തിലുള്ള വിശദാംശങ്ങൾക്കായി റെപ്പോ സോഴ്‌സ് പരിശോധിക്കുക (എൻഡ്പോയിന്റ് സ്കീമകൾ, പ്രോക്സി കോൺഫിഗ്, ഓത്ടോ ടോക്കൺകൾ).

---

## Context7 Setup

ഏതെങ്കിലും Context7 ക്വയറി ഉണ്ടെങ്കില്‍, ആദ്യം ലൈബ്രറി ID തീര്‍ചെയ്യുക (ഓരോ സെഷൻ-വട്ടം ഒന്ന്):

1. ടെക്നോളജി നാമം ഉപയോഗിച്ച് `mcp_context7_resolve-library-id` വിളിക്കുക
2. ലഭിച്ച ലൈബ്രറി IDയും ഒരു പ്രത്യേക ക്വയറിയും ഉപയോഗിച്ച് `mcp_context7_query-docs` വിളിക്കുക

---

## Writing Effective Queries

ഫലപ്രദമായ ചോദനകൾ എഴുതുക — പതിപ്പ്, ഉദ്ദേശ്യം, ഭാഷ എന്നിവ ഉൾപ്പെടുത്തുക:

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
ഡിസ്ക്ലെയിമർ:
ഈ ദസ്താവേയം AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷ ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, യാന്ത്രികമായി നടത്തിയ പരിഭാഷകളിൽ പിശകുകളും അപൂര്‍ണതകളും ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. മാതൃഭാഷയിലുള്ള യഥാർത്ഥ ദസ്താവേയം ഔദ്യോഗിക സ്രോതസ്സായി പരിഗണിക്കണം. നിർണായക വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മാനവ പരിഭാഷ ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ പരിഭാഷയിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകളോ തെറ്റായ വ്യാഖ്യാനങ്ങളോയ്ക്ക് ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->