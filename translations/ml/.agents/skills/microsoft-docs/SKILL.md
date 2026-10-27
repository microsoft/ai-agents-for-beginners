---
name: microsoft-docs
---
# Microsoft Docs

മൈക്രോസോഫ്റ്റ് ടെക്നോളജി ഇക്കോസ്‌istemകളെക്കുറിച്ചുള്ള ഗവേഷണ കഴിവ്. learn.microsoft.com നെ കൂടാതെ ഉള്ള ഡോക്യുമെന്റേഷനും (VS Code, GitHub, Aspire, Agent Framework റെപ്പോസ്) ഉൾപ്പെടുന്നു.

---

## ഡിഫോൾട്ട്: Microsoft Learn MCP

**learn.microsoft.com** ലെ എല്ലാത്തിലും ഇവ ടൂളുകൾ ഉപയോഗിക്കുക — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, മുതലായവ. മിക്ക മൈക്രോസോഫ്റ്റ് ഡോക്യുമെന്റേഷൻ ചോദ്യങ്ങൾക്ക് പ്രധാന ടൂൾ ഇതാണ്.

| ടൂൾ | ഉദ്ദേശ്യം |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com ലെ കാഴ്‌ചകൾ, ഗൈഡുകൾ, ട്യൂട്ടോറിയലുകൾ, കോൺഫിഗറേഷൻ_SEARCH ചെയ്യുക |
| `microsoft_code_sample_search` | Learn ഡോക്സ് നിന്നും പ്രവർത്തനകുറിപ്പുകൾ കണ്ടെത്തുക. മികച്ച ഫലങ്ങൾക്ക് `language` (`python`, `csharp`, തുടങ്ങിയവ) ഉപയോഗിക്കുക |
| `microsoft_docs_fetch` | ഒരു പ്രത്യേക URL ലെ പൂർണ്ണ പേജ് ഉള്ളടക്കം ലഭിക്കുക (ശേർച്ച്Excerptകൾ പോരാത്തപ്പോൾ) |

പൂർണ്ണ ട്യൂട്ടോറിയലുകൾ, എല്ലാ കോൺഫിഗ് ഓപ്ഷനുകളും അല്ലെങ്കിൽ ശേർച്ച്Excerptകൾ കുരുങ്ങിയപ്പോൾ `microsoft_docs_fetch` search കേന്ദ്രീകരിക്കുക.

---

## വ്യത്യസ്ത സന്ദർഭങ്ങൾ: മറ്റ് ടൂളുകൾ ഉപയോഗിക്കേണ്ട സമയങ്ങൾ

താഴെ കൊടുത്തിരിക്കുന്ന വർഗ്ഗങ്ങൾ **learn.microsoft.com** നു പുറത്താണ്. നിർദ്ദിഷ്ട ടൂൾ ഉപയോഗിക്കുക.

### Aspire — Aspire MCP Server (ആഗ്രഹമേറിയത്) അല്ലെങ്കിൽ Context7 ഉപയോഗിക്കുക

Aspire ഡോക്യുമെന്റ്‌സ് **aspire.dev** ല്‍ തന്നെ ഉണ്ടാകുന്നു, Learn ലല്ല. Aspire CLI പതിപ്പിനെ ആശ്രയിച്ച് ഏറ്റവും നല്ല ടൂൾ മാറ്റം വരും:

**CLI 13.2+** (പരാമർശനീയമായ) — Aspire MCP സെർവർ ഇന്റഗ്രേറ്റഡ് ഡോക്യുമെന്റ്_SEARCH ടൂളുകൾ ഉൾപ്പെടുത്തിയിട്ടുണ്ട്:

| MCP ഉപകരണങ്ങൾ | വിവരണം |
|----------|-------------|
| `list_docs` | aspire.dev ൽ ഉള്ള പ്രമാണങ്ങൾ എല്ലാ ലഭ്യമായ ഡോക്യുമെന്റ് ലിസ്റ്റ് ചെയ്യുക |
| `search_docs` | aspire.dev ഉള്ളടക്കത്തിൽ ഭാരമുള്ള ലെക്സിക്കൽ തിരയൽ |
| `get_doc` | സ്ലഗ് പ്രകാരം ഒരു പ്രത്യേക ഡോക്യുമെന്റ് ലഭിക്കുക |

Aspire CLI 13.2 ൽ ഈ ഫീച്ചറുകൾ എത്തിച്ചു ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). അപ്ഡേറ്റ് ചെയ്യാൻ: `aspire update --self --channel daily`.

**CLI 13.1** — MCP സെർവർ ഇന്റഗ്രേഷൻ ലുക്കപ്പ് നൽകുന്നു (`list_integrations`, `get_integration_docs`) എന്നാൽ ഡോക്യുമെന്റ്_SEARCH ഇല്ല. അതിനാൽ Context7 ഉപയോഗിക്കുക:

| ലൈബ്രറി ഐഡി | ഉപയോഗം |
|---|---|
| `/microsoft/aspire.dev` | പ്രാഥമികം — ഗൈഡുകൾ, ഇന്റഗ്രേഷനുകൾ, CLI റഫറൻസ്, ഡെപ്ലോയ്മെന്റ് |
| `/microsoft/aspire` | റൺടൈം സ്രോതസ്സ് — API ആന്തരഘടനകൾ, നടപ്പാക്കൽ വിശദാംശങ്ങൾ |
| `/communitytoolkit/aspire` | കമ്മ്യൂണിറ്റി ഇന്റഗ്രേഷനുകൾ — Go, ജാവ, Node.js, ഒല്ലാമ |

### VS Code — Context7 ഉപയോഗിക്കുക

VS Code ഡോക്യുമെന്റ്‌സ് **code.visualstudio.com** ല്‍ അതവസരം Learn ൽ അല്ല.

| ലൈബ്രറി ഐഡി | ഉപയോഗം |
|---|---|
| `/websites/code_visualstudio` | ഉപയോക്തൃ ഡോക്‌മെന്റ്-സെറ്റിങ്ങ്സ്, ഫീച്ചറുകൾ, ഡീബഗ്ഗിംഗ്, റിമോട്ട് ഡെവ് |
| `/websites/code_visualstudio_api` | എക്സ്റ്റൻഷൻ API — വെബ്‌വ്യൂസ്, TreeViews, കമാൻഡുകൾ, സംഭാവന പോയിന്റുകൾ |

### GitHub — Context7 ഉപയോഗിക്കുക

GitHub ഡോക്യുമെന്റ്‌സ് **docs.github.com**നും **cli.github.com**ക്കും ഉള്ളതാണ്.

| ലൈബ്രറി ഐഡി | ഉപയോഗം |
|---|---|
| `/websites/github_en` | ആക്ഷനുകൾ, API, റെപ്പോസ്, സുരക്ഷ, അഡ്മിൻ, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) കമാൻഡുകളും ഫ്ലാഗുകളും |

### Agent Framework — Learn MCP + Context7 ഉപയോഗിക്കുക

Agent Framework ട്യൂട്ടോറിയലുകൾ learn.microsoft.com ല്‍ ഉണ്ട് (`microsoft_docs_search` ഉപയോഗിക്കുക), പക്ഷേ **GitHub റെപ്പോ**യിൽ പ്രസിദ്ധീകരിച്ച ഡോക്യുമെന്റേഷനൈക്കാൾ API നിലവാരത്തിലുള്ള വിശദാംശങ്ങൾ വളരെ മുന്നിലാണ് — പ്രത്യേകിച്ച് DevUI REST API റഫറൻസ്, CLI ഓപ്ഷനുകൾ, .NET ഇന്റഗ്രേഷൻ.

| ലൈബ്രറി ഐഡി | ഉപയോഗം |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | ട്യൂട്ടോറിയലുകൾ — DevUI ഗൈഡുകൾ, ട്രേസിംഗ്, വർക്‌ഫ്ലോ ഓർക്കസ്ട്രേഷൻ |
| `/microsoft/agent-framework` | API വിശദാംശങ്ങൾ — DevUI REST എന്റ്‌പ്പോയിന്റുകൾ, CLI ഫ്ലാഗുകൾ, അയത്ഥ, .NET `AddDevUI`/`MapDevUI` |

**DevUI ഉപദേശം:** Learn വെബ്സൈറ്റ് സ്രോതസ്സ് വഴി ഹൗ-ടു ഗൈഡുകൾ അന്വേഷിക്കൂ, പിന്നെ റെപ്പോ സ്രോതസ്സ് വഴി API നിലവാരത്തിലുള്ള സ്പെസിഫിക് വിവരങ്ങൾ (എന്റ്‌പോയ്‌ന്റ് സ്കീമകൾ, പ്രോക്സി കോൺഫിഗ്യുറേഷൻ, അയത്ത് ടോക്കണുകൾ).

---

## Context7 സെറ്റപ്പ്

എതിരാളിയായ Context7 ചോദ്യത്തിനായി, ആദ്യം ലൈബ്രറി ഐഡി കണ്ടെത്തുക (ഒരു സെഷനിൽ ഒരു തവണ):

1. ടെക്നോളജി പേര് ഉപയോഗിച്ച് `mcp_context7_resolve-library-id` വിളിക്കുക
2. ലഭിച്ച ലൈബ്രറി ഐഡി ഉപയോഗിച്ച് പ്രത്യേക ചോദ്യത്തോടുകൂടി `mcp_context7_query-docs` വിളിക്കുക

---

## ഫലപ്രദമായ ക്വെരികൾ എഴുതുക

പ്രത്യേകമാക്കുക — പതിപ്പ്, ഉദ്ദേശ്യം, ഭാഷ ഉൾപ്പെടുത്തുക:

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

സന്ദർഭം ഉൾപ്പെടുത്തുക:
- പ്രസക്തമായപ്പോൾ **പതിപ്പ്** (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **ടാസ്‌ക് ഉദ്ദേശ്യം** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- പോളിഗ്ലോട്ട് ഡോക്യുമെന്റേഷനായി **ഭാഷ** (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->