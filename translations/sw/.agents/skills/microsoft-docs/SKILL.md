---
name: microsoft-docs
description: Tafuta nyaraka rasmi za Microsoft ili kupata dhana, mafunzo, na mifano
  ya msimbo katika Azure, .NET, Agent Framework, Aspire, VS Code, GitHub, na zaidi.
  Inatumia Microsoft Learn MCP kama chaguo la msingi, pamoja na Context7 na Aspire
  MCP kwa maudhui yanayoishi nje ya learn.microsoft.com.
---
# Microsoft Docs

Uwezo wa utafiti kwa mfumo wa teknolojia ya Microsoft. Unajumuisha learn.microsoft.com na nyaraka zinazopo nje yake (VS Code, GitHub, Aspire, repos za Agent Framework).

---

## Chaguo la Msingi: Microsoft Learn MCP

Tumia zana hizi kwa **kila kitu kwenye learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, na zaidi. Hii ni zana kuu kwa ajili ya mchanganyiko mkubwa wa maswali ya nyaraka za Microsoft.

| Zana | Kusudi |
|------|---------|
| `microsoft_docs_search` | Tafuta learn.microsoft.com — dhana, mwongozo, mafunzo, usanidi |
| `microsoft_code_sample_search` | Tafuta vipande vya msimbo vinavyofanya kazi kutoka kwa nyaraka za Learn. Tumia `language` (`python`, `csharp`, nk) kwa matokeo bora |
| `microsoft_docs_fetch` | Pata maudhui kamili ya ukurasa kutoka URL maalum (wakati vipande vya utafutaji havitoshi) |

Tumia `microsoft_docs_fetch` baada ya utafutaji unapotaka mafunzo kamili, chaguzi zote za usanidi, au wakati vipande vya utafutaji vilivyo kifupi vinakatwa.

---

## Mambo ya Kutojali: Lini Utumie Zana Nyingine

Makundi yafuatayo yanaishi **nje** ya learn.microsoft.com. Badala yake tumia zana maalum.

### Aspire — Tumia Aspire MCP Server (iliyopendekezwa) au Context7

Nyaraka za Aspire ziko kwenye **aspire.dev**, si Learn. Zana bora hutegemea toleo lako la Aspire CLI:

**CLI 13.2+** (iliyopendekezwa) — Server ya Aspire MCP ina zana za kutafutia nyaraka zilizojengwa ndani:

| Zana ya MCP | Maelezo |
|----------|-------------|
| `list_docs` | Inaorodhesha nyaraka zote zinazopatikana kutoka aspire.dev |
| `search_docs` | Utafutaji wa kishabiki wenye uzito katika maudhui ya aspire.dev |
| `get_doc` | Huleta hati maalum kwa slug |

Hizi hupakiwa katika Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Ili kusasisha: `aspire update --self --channel daily`.

**CLI 13.1** — Server ya MCP hutoa utafutaji wa muungano (`list_integrations`, `get_integration_docs`) lakini **sio** utafutaji wa nyaraka. Rudia Context7:

| Kitambulisho cha Maktaba | Matumizi |
|---|---|
| `/microsoft/aspire.dev` | Kuu — mwongozo, miunganiko, rejea ya CLI, usambazaji |
| `/microsoft/aspire` | Chanzo cha wakati wa kukimbia — sehemu za ndani za API, maelezo ya utekelezaji |
| `/communitytoolkit/aspire` | Miunganiko ya jamii — Go, Java, Node.js, Ollama |

### VS Code — Tumia Context7

Nyaraka za VS Code ziko kwenye **code.visualstudio.com**, si Learn.

| Kitambulisho cha Maktaba | Matumizi |
|---|---|
| `/websites/code_visualstudio` | Nyaraka za mtumiaji — mipangilio, vipengele, urekebishaji, maendeleo ya mbali |
| `/websites/code_visualstudio_api` | API ya ugani — webviews, TreeViews, amri, pointi za michango |

### GitHub — Tumia Context7

Nyaraka za GitHub ziko kwenye **docs.github.com** na **cli.github.com**.

| Kitambulisho cha Maktaba | Matumizi |
|---|---|
| `/websites/github_en` | Matendo, API, repos, usalama, usimamizi, Copilot |
| `/websites/cli_github` | Amri na bendera za GitHub CLI (`gh`) |

### Agent Framework — Tumia Learn MCP + Context7

Mafunzo ya Agent Framework yako kwenye learn.microsoft.com (tumia `microsoft_docs_search`), lakini **repo ya GitHub** ina maelezo ya kiwango cha API ambayo mara nyingi ni mbele ya nyaraka zilizochapishwa — hasa rejea ya DevUI REST API, chaguzi za CLI, na muunganiko wa .NET.

| Kitambulisho cha Maktaba | Matumizi |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Mafunzo — mwongozo wa DevUI, ufuatiliaji, upangaji wa mtiririko wa kazi |
| `/microsoft/agent-framework` | Maelezo ya API — sehemu za mwisho za DevUI REST, bendera za CLI, uthibitishaji, .NET `AddDevUI`/`MapDevUI` |

**Kipengele cha DevUI:** Uliza chanzo cha tovuti ya Learn kwa mwongozo wa jinsi ya kufanya, kisha chanzo cha repo kwa maelezo ya kiwango cha API (miundo ya sehemu za mwisho, usanidi wa wakala, tokeni za uthibitishaji).

---

## Usanidi wa Context7

Kwa swali lolote la Context7, hakikisha kwanza kitambulisho cha maktaba (mara moja kwa kila kikao):

1. Piga simu `mcp_context7_resolve-library-id` na jina la teknolojia
2. Piga simu `mcp_context7_query-docs` na kitambulisho cha maktaba kilichorejeshwa na swali maalum

---

## Kuandika Maswali yenye Ufanisi

Kuwa maalum — jumuisha toleo, kusudi, na lugha:

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

Jumuisha muktadha:
- **Toleo** inapohitajika (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Kusudi la kazi** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Lugha** kwa nyaraka nyingi (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->