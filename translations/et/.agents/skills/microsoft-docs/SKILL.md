---
name: microsoft-docs
---
# Microsoft Docs

Uurimisoskus Microsofti tehnoloogiliste ökosüsteemide jaoks. Katab learn.microsoft.com-i ja dokumentatsiooni, mis asub väljaspool seda (VS Code, GitHub, Aspire, Agent Frameworki hoidlad).

---

## Vaikimisi: Microsoft Learn MCP

Kasuta neid tööriistu **kõike otsimiseks learn.microsoft.com-is** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows ja palju muud. See on peamine tööriist enamiku Microsofti dokumentatsiooni päringute jaoks.

| Tööriist | Eesmärk |
|------|---------|
| `microsoft_docs_search` | otsi learn.microsoft.com — kontseptsioonid, juhendid, õpetused, seadistused |
| `microsoft_code_sample_search` | leia töötavad koodinäited Learn dokumentidest. Parimate tulemuste jaoks kasuta `language` (`python`, `csharp` jne) |
| `microsoft_docs_fetch` | saa kogu lehe sisu konkreetsest URL-ist (kui otsingu lõiked ei piisa) |

Kasuta `microsoft_docs_fetch` pärast otsingut, kui vajad täielikke õpetusi, kõiki seadistusvõimalusi või kui otsingu lõiked on lühendatud.

---

## Erandid: millal kasutada teisi tööriistu

Järgmised kategooriad asuvad **väljaspool** learn.microsoft.com-i. Kasuta kindlasti määratud tööriista.

### Aspire — kasuta Aspire MCP serverit (eelistatuim) või Context7

Aspire dokumentatsioon asub **aspire.dev** lehel, mitte Learnis. Parim tööriist sõltub sinu Aspire CLI versioonist:

**CLI 13.2+** (soovitatav) — Aspire MCP server sisaldab sisseehitatud dokumentatsiooni otsingutööriistu:

| MCP tööriist | Kirjeldus |
|----------|-------------|
| `list_docs` | Loetleb kogu saadaval oleva dokumentatsiooni aspire.dev lehelt |
| `search_docs` | Kaalutud leksikaalne otsing aspire.dev sisu ulatuses |
| `get_doc` | Toob konkreetse dokumenti slugi alusel |

Need kaasati Aspire CLI 13.2-sse ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Uuendamiseks: `aspire update --self --channel daily`.

**CLI 13.1** — MCP server toetab integreerimisotsingut (`list_integrations`, `get_integration_docs`), kuid **ei toeta** dokumentatsiooni otsingut. Seda tööriista asenduseks kasuta Context7:

| Raamatu ID | Kasutusala |
|---|---|
| `/microsoft/aspire.dev` | Peamine — juhendid, integratsioonid, CLI viited, juurutamine |
| `/microsoft/aspire` | Käitusallikas — API sisemine toimimine, rakenduse üksikasjad |
| `/communitytoolkit/aspire` | Kogukonna integratsioonid — Go, Java, Node.js, Ollama |

### VS Code — kasuta Context7

VS Code dokumentatsioon asub **code.visualstudio.com** lehel, mitte Learnis.

| Raamatu ID | Kasutusala |
|---|---|
| `/websites/code_visualstudio` | Kasutaja dokumentatsioon — seaded, funktsioonid, silumine, kaug-arendus |
| `/websites/code_visualstudio_api` | Laienduse API — veebivaated, TreeViews, käsud, panusetipmid |

### GitHub — kasuta Context7

GitHub dokumentatsioon asub aadressidel **docs.github.com** ja **cli.github.com**.

| Raamatu ID | Kasutusala |
|---|---|
| `/websites/github_en` | Actions, API, repos, turvalisus, administreerimine, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) käsud ja lipud |

### Agent Framework — kasuta Learn MCP + Context7

Agent Frameworki õpetused asuvad learn.microsoft.com-il (kasuta `microsoft_docs_search`), kuid **GitHubi hoidlas** on API tasandi üksikasjad, mis sageli on välja antud dokumentatsioonist ees — eriti DevUI REST API viited, CLI valikud ja .NET integratsioon.

| Raamatu ID | Kasutusala |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Õpetused — DevUI juhendid, jälgimine, töövoo orkestreerimine |
| `/microsoft/agent-framework` | API üksikasjad — DevUI REST lõpp-punktid, CLI lipud, autentimine, .NET `AddDevUI`/`MapDevUI` |

**DevUI nõuanne:** Küsi Learn veebisaidi allikat, et saada kuidas-juhtuda juhendite jaoks, seejärel repo allikat API tasandi detailsuste saamiseks (lõpp-punkti skeemid, proxy konfiguratsioon, autentimismärgid).

---

## Context7 seadistus

Iga Context7 päringu puhul järgi kõigepealt raamatu ID saamist (üks kord sessiooni jooksul):

1. Kutse `mcp_context7_resolve-library-id` tehnoloogia nimega
2. Kutse `mcp_context7_query-docs` koos tagastatud raamatu ID ja konkreetse päringuga

---

## Tõhusate päringute kirjutamine

Ole konkreetne — lisa versioon, eesmärk ja keel:

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

Lisa kontekst:
- **Versioon** kui asjakohane (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Tööülesande eesmärk** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Keel** polüglott dokumentide puhul (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->