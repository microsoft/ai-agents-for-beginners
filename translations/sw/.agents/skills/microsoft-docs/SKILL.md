---
name: microsoft-docs
description: Fanya uchunguzi kwenye nyaraka rasmi za Microsoft ili upate dhana, mafunzo,
  na mifano ya msimbo katika Azure, .NET, Agent Framework, Aspire, VS Code, GitHub,
  na zaidi. Inatumia Microsoft Learn MCP kama chaguo-msingi, na Context7 na Aspire
  MCP kwa maudhui yanayopatikana nje ya learn.microsoft.com.
---
# Microsoft Docs

Ujuzi wa utafiti kwa ekosistimu ya teknolojia ya Microsoft. Inashughulikia learn.microsoft.com na nyaraka zinazoshikilia nje yake (VS Code, GitHub, Aspire, hazina za Agent Framework).

---

## Default: Microsoft Learn MCP

Tumia zana hizi kwa **kila kitu kwenye learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, na zaidi. Hii ni zana kuu kwa sehemu kubwa ya maswali ya nyaraka za Microsoft.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Tafuta learn.microsoft.com — dhana, mwongozo, mafunzo, usanidi |
| `microsoft_code_sample_search` | Tafuta vipande vya msimbo vinavyofanya kazi kutoka kwenye nyaraka za Learn. Tumia `language` (`python`, `csharp`, n.k.) kwa matokeo bora |
| `microsoft_docs_fetch` | Pata yaliyomo ya ukurasa kamili kutoka kwenye URL maalum (wanapo toleo la utafutaji halitoshi) |

Tumia `microsoft_docs_fetch` baada ya utafutaji wakati unahitaji mafunzo kamili, chaguzi zote za usanidi, au wakati vifupisho vya utafutaji vimekatwa.

---

## Exceptions: When to Use Other Tools

Makundi yafuatayo yapo **nje** ya learn.microsoft.com. Tumia zana maalum badala yake.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Nyaraka za Aspire zinapatikana kwenye **aspire.dev**, si Learn. Zana bora inategemea toleo lako la Aspire CLI:

**CLI 13.2+** (inayopendekezwa) — Aspire MCP server ina zana za utafutaji wa nyaraka zilizojengwa ndani:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Orodhesha nyaraka zote zinazopatikana kutoka aspire.dev |
| `search_docs` | Utafutaji wa kifasiri wenye uzito kwenye yaliyomo ya aspire.dev |
| `get_doc` | Inarekebisha hati maalum kwa slug |

Hizi zinaambatana katika Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Ili kusasisha: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP server hutoa utafutaji wa integrasiyo (`list_integrations`, `get_integration_docs`) lakini **si** utafutaji wa nyaraka. Rudia Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Msingi — mwongozo, integrasiyo, rejea ya CLI, upeleka |
| `/dotnet/aspire` | Chanzo cha runtime — ndani za API, maelezo ya utekelezaji |
| `/communitytoolkit/aspire` | Integrasiyo za jamii — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

Nyaraka za VS Code zinapatikana kwenye **code.visualstudio.com**, si Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Nyaraka za mtumiaji — mipangilio, vipengele, debugging, maendeleo ya mbali |
| `/websites/code_visualstudio_api` | API ya upanuzi — webviews, TreeViews, amri, pointi za mchango |

### GitHub — Use Context7

Nyaraka za GitHub zinapatikana kwenye **docs.github.com** na **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repos, usalama, usimamizi, Copilot |
| `/websites/cli_github` | Amri na bendera za GitHub CLI (`gh`) |

### Agent Framework — Use Learn MCP + Context7

Mafunzo ya Agent Framework yako kwenye learn.microsoft.com (tumia `microsoft_docs_search`), lakini **repo ya GitHub** ina maelezo ya kiwango cha API ambayo mara nyingi iko mbele ya nyaraka zilizochapishwa — hasa rejea ya DevUI REST API, chaguzi za CLI, na ujumuishaji wa .NET.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Mafunzo — mwongozo wa DevUI, ufuatiliaji, uendeshaji wa workflow |
| `/microsoft/agent-framework` | Maelezo ya API — endpoints za DevUI REST, bendera za CLI, auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Ulizi chanzo cha tovuti ya Learn kwa mwongozo wa jinsi ya kufanya, kisha chanzo cha repo kwa maelezo ya kiwango cha API (miundo ya endpoint, usanidi wa proxy, tokeni za uthibitisho).

---

## Context7 Setup

Kwa swali lolote la Context7, tatua library ID kwanza (mara moja kwa kila kikao):

1. Call `mcp_context7_resolve-library-id` with the technology name
2. Call `mcp_context7_query-docs` with the returned library ID and a specific query

---

## Writing Effective Queries

Kuwa maalum — jumuisha toleo, nia, na lugha:

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
- **Toleo** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Nia ya kazi** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Lugha** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Tamko:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya utafsiri wa AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Nyaraka ya asili kwa lugha yake inapaswa kuchukuliwa kama chanzo chenye mamlaka. Kwa taarifa muhimu, tunapendekeza tafsiri ya kitaalamu iliyofanywa na mtafsiri wa binadamu. Hatubebei uwajibikaji kwa kutokuelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->