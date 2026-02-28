---
name: microsoft-docs
description: ഔദ്യോഗിക Microsoft ഡോക്യുമെന്റേഷൻ ക്വറി ചെയ്ത് Azure, .NET, Agent Framework,
  Aspire, VS Code, GitHub എന്നിവയിൽ ഉൾപ്പെടെ സങ്കൽപ്പങ്ങൾ, ട്യൂട്ടോറിയലുകൾ, കോഡ് ഉദാഹരണങ്ങൾ
  കണ്ടെത്തുക. Microsoft Learn MCP നെ ഡീഫോൾട്ട് ആയി ഉപയോഗിക്കുന്നു, learn.microsoft.com
  പുറത്ത് നിലനിൽക്കുന്ന ഉള്ളടക്കത്തിന് Context7യും Aspire MCPയും ഉപയോഗിക്കുന്നു.
---
# Microsoft Docs

Microsoft സാങ്കേതിക പരിസ്ഥിതിക്കുള്ള ഗവേഷണ കഴിവ്. learn.microsoft.com-യും അതിനപ്പുറം ഉള്ള ഡോക്യുമെന്റേഷൻ (VS Code, GitHub, Aspire, Agent Framework റിപോസിറ്ററികൾ) ഉൾക്കൊള്ളുന്നു.

---

## ഡീഫോൾട്ട്: Microsoft Learn MCP

ഈ ടൂളുകൾ ഉപയോഗിക്കുക **learn.microsoft.com-ൽ ഉള്ള എല്ലാത്തിനും** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, എന്നിവയും കൂടുതൽ. മൈക്രോസോഫ്റ്റ് ഡോക്യുമെന്റേഷനുമായി ബന്ധപ്പെട്ട ഭൂരിഭാഗം അന്വേഷങ്ങൾക്ക് ഇത് പ്രധാന ടൂൾ ആണ്.

| ടൂൾ | ഉദ്ദേശ്യം |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com-ൽ തിരയുക — ആശയങ്ങൾ, ഗൈഡുകൾ, ട്യൂട്ടോറിയലുകൾ, കോൺഫിഗറേഷൻ |
| `microsoft_code_sample_search` | Learn ഡോക്സിൽ നിന്നുള്ള പ്രവർത്തനക്ഷമമായ കോഡ് സ്നിപ്പറ്റുകൾ കണ്ടെത്തുക. മികച്ച ഫലത്തിനായി `language` (`python`, `csharp`, മുതലായവ) നൽകുക |
| `microsoft_docs_fetch` | നിശ്ചിത URL-ൽ നിന്നുള്ള പൂർണ്ണ പേജ് ഉള്ളടക്കം നേടുക (തിരയൽ ഉദ്ധരണികൾ മതിയാകാതിരിക്കുന്നപ്പോൾ) |

പരമാവധി ട്യൂട്ടോറിയലുകൾ, എല്ലാ കോൺഫിഗറേഷൻ ഓപ്ഷനുകളും, അല്ലെങ്കിൽ തിരയൽ ഉദ്ധരണികൾ തകർന്നാൽ തിരയലിന്റെ ശേഷമുള്ള ഘട്ടത്തിൽ `microsoft_docs_fetch` ഉപയോഗിക്കുക.

---

## വ്യത്യാസങ്ങൾ: മറ്റു ടൂളുകൾ ഉപയോഗിക്കേണ്ടപ്പോൾ

താഴെപ്പറയപ്പെടുന്ന വിഭാഗങ്ങൾ **learn.microsoft.com-നിന്ന് പുറത്താണ്**. പകരം നിശ്ചിത ടൂൾ ഉപയോഗിക്കുക.

### .NET Aspire — Aspire MCP Server (മുൻഗണനയോടെ) അല്ലെങ്കിൽ Context7 ഉപയോഗിക്കുക

Aspire ഡോകുകൾ **aspire.dev**-ൽ ആണ്, Learn-ൽ അല്ല. മികച്ച ടൂൾ നിങ്ങളുടെ Aspire CLI പതിപ്പിനെ ആശ്രയിച്ചിരിക്കുന്നു:

**CLI 13.2+** (ശുപാർശ) — Aspire MCP സർവർ ബിൽറ്റ്-ഇൻ ഡോക്സ് സെർച്ച് ടൂളുകൾ ഉൾക്കൊള്ളുന്നു:

| MCP ടൂൾ | വിവരണം |
|----------|-------------|
| `list_docs` | aspire.dev-ൽ നിന്ന് ലഭ്യമായ എല്ലാ ഡോക്യുമെന്റേഷനുമുള്ള ലിസ്റ്റ് |
| `search_docs` | aspire.dev ഉള്ളടക്കത്തിനായുള്ള ഭാരിത ലെക്സിക്കൽ തിരയൽ |
| `get_doc` | സ്ലഗ് ഉപയോഗിച്ച് ഒരു പ്രത്യേക ഡോക്യുമെന്റ് വീണ്ടെടുക്കുന്നു |

ഇവ Aspire CLI 13.2-ൽ ഉൾപ്പെട്ടിരിക്കുന്നു ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). അപ്ഡേറ്റ് ചെയ്യാൻ: `aspire update --self --channel daily`. റഫറൻസ്: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP സർവർ integration lookup (`list_integrations`, `get_integration_docs`) നൽകുന്നു പക്ഷേ ഡോക്സ് സെർച്ച് നൽകുന്നില്ല. Context7-ൽ fallback ചെയ്യുക:

| ലൈബ്രറി ID | ഉപയോഗത്തിന് |
|---|---|
| `/microsoft/aspire.dev` | പ്രാഥമികം — ഗൈഡുകൾ, ഇന്റഗ്രേഷനുകൾ, CLI റഫറൻസ്, ഡെപ്ലോയ്മെന്റ് |
| `/dotnet/aspire` | റൺടൈം സോഴ്‌സ് — API ഇന്റർണൽസ്, നടപ്പിലാക്കൽ വിശദാംശങ്ങൾ |
| `/communitytoolkit/aspire` | കമ്മ്യൂണിറ്റി ഇന്റഗ്രേഷനുകൾ — Go, Java, Node.js, Ollama |

### VS Code — Context7 ഉപയോഗിക്കുക

VS Code ഡോകുകൾ **code.visualstudio.com**-ൽ ആണ്, Learn-ൽ അല്ല.

| ലൈബ്രറി ID | ഉപയോഗത്തിന് |
|---|---|
| `/websites/code_visualstudio` | ഉപയോക്തൃ ഡോകുകൾ — സജ്ജീകരണങ്ങൾ, ഫീച്ചറുകൾ, ഡീബഗിംഗ്, റിമോട്ട് ഡെവ് |
| `/websites/code_visualstudio_api` | എക്സ്റ്റൻഷൻ API — webviews, TreeViews, കമാൻഡുകൾ, കൺട്രിബ്യൂഷൻ പോയിന്റുകൾ |

### GitHub — Context7 ഉപയോഗിക്കുക

GitHub ഡോകുകൾ **docs.github.com**-യും **cli.github.com**-ഉം ആണ്.

| ലൈബ്രറി ID | ഉപയോഗത്തിന് |
|---|---|
| `/websites/github_en` | Actions, API, റീപോസ്, സെക്യൂരിറ്റി, അഡ്മിൻ, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) കമാൻഡുകൾയും ഫ്ലാഗുകളും |

### Agent Framework — Learn MCP + Context7 ഉപയോഗിക്കുക

Agent Framework ട്യൂട്ടോറിയലുകൾ learn.microsoft.com-ൽ ആണ് (ഉപയോഗിക്കുക `microsoft_docs_search`), പക്ഷേ **GitHub റിപോ**പിൽ API-നിരത്തിലുള്ള വിശദാംശങ്ങൾ പ്രസിദ്ധീകരിച്ച ഡോക്യുമെന്റേഷനേക്കാൾ മുന്നിലുള്ളതായിരിക്കും — പ്രത്യേകിച്ച് DevUI REST API റഫറൻസ്, CLI ഓപ്ഷനുകൾ, .NET ഇന്റഗ്രേഷൻ.

| ലൈബ്രറി ID | ഉപയോഗത്തിന് |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ട്യൂട്ടോറിയലുകൾ — DevUI ഗൈഡുകൾ, ട്രേസിംഗ്, വർക്ഫ്ലോ ഓർക്കസ്‌ട്രേഷൻ |
| `/microsoft/agent-framework` | API വിശദാംശങ്ങൾ — DevUI REST എൻഡ്പോയിന്റുകൾ, CLI ഫ്ലാഗുകൾ, ഓത്ത്, .NET `AddDevUI`/`MapDevUI` |

**DevUI ടിപ്പ്:** how-to ഗൈഡുകൾക്കായി Learn വെബ്‌സൈറ്റ് സോഴ്‌സ് അന്വേഷിച്ച് പിന്നീട് API-നിർവചന വിശദാംശങ്ങൾക്ക് (എൻഡ്പോയിന്റ് സ്കീമുകൾ, പ്രോക്സി കോൺഫിഗ്, ഓത് ടോക്കനുകൾ) റിപ്പോ സോഴ്‌സ് പരിശോധിക്കുക.

---

## Context7 സെറ്റ്‌അപ്പ്

ഏതെങ്കിലും Context7 ക്വെറിയിനും ശേഷം, ഒരു സെഷനിൽ ഒരിക്കൽ ലൈബ്രറി ID പരിഹരിക്കുക:

1. ടെക്നോളജി നാമവുമായി `mcp_context7_resolve-library-id` കോൾ ചെയ്യുക
2. കിട്ടിയ ലൈബ്രറി ID ഉപയോഗിച്ച് ഒരു പ്രത്യേക ക്വറി നൽക്കാൻ `mcp_context7_query-docs` കോൾ ചെയ്യുക

---

## ഫലപ്രദമായ ക്വെറികൾ എഴുതൽ

സൂക്ഷ്മമായി ആയിരിക്കുക — പതിപ്പ്, ഉദ്ദേശ്യം, ഭാഷ എന്നിവ ഉൾപ്പെടുത്തുക:

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
- **പതിപ്പ്** പ്രസക്തിയുള്ളപ്പോൾ (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **ടാസ്ക് ഉദ്ദേശ്യം** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **ഭാഷ** പോളിഗ്ലോട്ട് ഡോക്കുകൾക്കായി (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
അറിയിപ്പ്:
ഈ രേഖ AI അടിസ്ഥാനത്തിലുള്ള പരിഭാഷാ സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. നാം കൃത്യതയ്ക്ക് പരിശ്രമിക്കും എന്നെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ തെറ്റുകളും അശുദ്ധികളോ ഉണ്ടാകാൻ സാധ്യതയുണ്ട് എന്ന് ദയവായി ശ്രദ്ധിക്കുക. മാതൃഭാഷയിൽ ഉള്ള ഒറിജിനൽ രേഖയാണ് അധികാരമുള്ള ഉറവിടമായിരിക്കണമെന്നും കരുതേണ്ടത്. നിർണായക വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യപരിഭാഷക്കു ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ പരിഭാഷയുടെ ഉപയോഗത്തിൽനിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകളുടെയും തെറ്റായ വ്യാഖ്യാനങ്ങളുടെയും ഉത്തരവാദിത്തം ഞങ്ങൾക്ക് ഉണ്ടാകില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->