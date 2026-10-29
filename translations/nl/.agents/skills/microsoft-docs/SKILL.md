---
name: microsoft-docs
description: Zoek in officiële Microsoft-documentatie naar concepten, tutorials en
  codevoorbeelden over Azure, .NET, Agent Framework, Aspire, VS Code, GitHub en meer.
  Maakt standaard gebruik van Microsoft Learn MCP, met Context7 en Aspire MCP voor
  inhoud die buiten learn.microsoft.com valt.
---
# Microsoft Docs

Onderzoekvaardigheid voor het Microsoft-technologie-ecosysteem. Beslaat learn.microsoft.com en documentatie die daarbuiten bestaat (VS Code, GitHub, Aspire, Agent Framework repos).

---

## Standaard: Microsoft Learn MCP

Gebruik deze hulpmiddelen voor **alles op learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows en meer. Dit is het primaire hulpmiddel voor de overgrote meerderheid van Microsoft documentatievragen.

| Hulpmiddel | Doel |
|------|---------|
| `microsoft_docs_search` | Zoek op learn.microsoft.com — concepten, handleidingen, tutorials, configuratie |
| `microsoft_code_sample_search` | Vind werkende codefragmenten uit Learn-documentatie. Gebruik `language` (`python`, `csharp`, etc.) voor de beste resultaten |
| `microsoft_docs_fetch` | Krijg volledige pagina-inhoud van een specifieke URL (wanneer zoekfragmenten niet genoeg zijn) |

Gebruik `microsoft_docs_fetch` na zoeken wanneer je complete tutorials, alle configuratieopties, of wanneer zoekfragmenten worden afgekapt nodig hebt.

---

## Uitzonderingen: Wanneer andere hulpmiddelen te gebruiken

De volgende categorieën bevinden zich **buiten** learn.microsoft.com. Gebruik daarvoor het opgegeven hulpmiddel.

### Aspire — Gebruik Aspire MCP Server (voorkeur) of Context7

Aspire-docs staan op **aspire.dev**, niet op Learn. Het beste hulpmiddel hangt af van je Aspire CLI-versie:

**CLI 13.2+** (aanbevolen) — De Aspire MCP-server bevat ingebouwde documentatie-zoekhulpmiddelen:

| MCP Hulpmiddel | Beschrijving |
|----------|-------------|
| `list_docs` | Lijst met alle beschikbare documentatie van aspire.dev |
| `search_docs` | Gewogen lexicale zoekopdracht over aspire.dev content |
| `get_doc` | Haalt een specifiek document op per slug |

Deze worden meegeleverd in Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Om bij te werken: `aspire update --self --channel daily`.

**CLI 13.1** — De MCP-server biedt integratielookup (`list_integrations`, `get_integration_docs`) maar **geen** documentatiezoekfunctie. Schakel terug naar Context7:

| Bibliotheek-ID | Gebruik voor |
|---|---|
| `/microsoft/aspire.dev` | Primair — handleidingen, integraties, CLI-referentie, deployment |
| `/microsoft/aspire` | Runtime-bron — API-internals, implementatiedetails |
| `/communitytoolkit/aspire` | Community-integraties — Go, Java, Node.js, Ollama |

### VS Code — Gebruik Context7

VS Code-docs staan op **code.visualstudio.com**, niet op Learn.

| Bibliotheek-ID | Gebruik voor |
|---|---|
| `/websites/code_visualstudio` | Gebruikersdocumentatie — instellingen, functies, debuggen, remote develop |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, opdrachten, bijdragepunten |

### GitHub — Gebruik Context7

GitHub-documentatie staat op **docs.github.com** en **cli.github.com**.

| Bibliotheek-ID | Gebruik voor |
|---|---|
| `/websites/github_en` | Actions, API, repos, beveiliging, beheer, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) opdrachten en vlaggen |

### Agent Framework — Gebruik Learn MCP + Context7

Tutorials van Agent Framework staan op learn.microsoft.com (gebruik `microsoft_docs_search`), maar de **GitHub repo** heeft API-niveau detail dat vaak voorloopt op gepubliceerde documentatie — vooral DevUI REST API referentie, CLI-opties en .NET-integratie.

| Bibliotheek-ID | Gebruik voor |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorials — DevUI-handleidingen, tracing, workflow orkestratie |
| `/microsoft/agent-framework` | API-detail — DevUI REST eindpunten, CLI-vlaggen, authenticatie, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Vraag eerst de Learn-websitebron naar how-to handleidingen, dan de repo bron voor API-niveau specificaties (eindpunt schema’s, proxy config, auth tokens).

---

## Context7 Configuratie

Voor elke Context7-query, bepaal eerst de bibliotheek-ID (eenmalig per sessie):

1. Roep `mcp_context7_resolve-library-id` aan met de technologische naam
2. Roep `mcp_context7_query-docs` aan met de teruggegeven bibliotheek-ID en een specifieke zoekopdracht

---

## Effectieve Zoekopdrachten Schrijven

Wees specifiek — vermeld versie, intentie en taal:

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

Voeg context toe:
- **Versie** wanneer relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Taakintentie** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Taal** voor meertalige documentatie (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->