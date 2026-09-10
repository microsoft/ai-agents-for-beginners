---
name: microsoft-docs
description: Doorzoek de officiële Microsoft-documentatie om concepten, tutorials
  en codevoorbeelden te vinden voor Azure, .NET, Agent Framework, Aspire, VS Code,
  GitHub en meer. Gebruikt Microsoft Learn MCP als standaard, met Context7 en Aspire
  MCP voor inhoud die buiten learn.microsoft.com staat.
---
# Microsoft Docs

Onderzoeksvaardigheid voor het Microsoft-technologie-ecosysteem. Behandelt learn.microsoft.com en documentatie die daarbuiten bestaat (VS Code, GitHub, Aspire, Agent Framework repositories).

---

## Standaard: Microsoft Learn MCP

Gebruik deze tools voor **alles op learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows en meer. Dit is het primaire hulpmiddel voor de overgrote meerderheid van Microsoft-documentatievragen.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Zoek learn.microsoft.com — concepten, gidsen, tutorials, configuratie |
| `microsoft_code_sample_search` | Vind werkende codefragmenten uit Learn-documentatie. Geef `language` (`python`, `csharp`, enz.) door voor de beste resultaten |
| `microsoft_docs_fetch` | Haal volledige paginainhoud op van een specifieke URL (wanneer zoekfragmenten niet genoeg zijn) |

Gebruik `microsoft_docs_fetch` na het zoeken wanneer je volledige tutorials, alle configuratie-opties, of wanneer zoekfragmenten zijn afgekapt nodig hebt.

---

## Exceptions: When to Use Other Tools

De volgende categorieën staan **buiten** learn.microsoft.com. Gebruik in plaats daarvan de opgegeven tool.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire-documentatie staat op **aspire.dev**, niet op Learn. De beste tool hangt af van je Aspire CLI-versie:

**CLI 13.2+** (aanbevolen) — De Aspire MCP-server bevat ingebouwde docs-zoekhulpmiddelen:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Toont alle beschikbare documentatie van aspire.dev |
| `search_docs` | Gewogen lexicale zoekopdracht over aspire.dev-inhoud |
| `get_doc` | Haalt een specifiek document op via de slug |

These ship in Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). To update: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — De MCP-server biedt integratie-opzoeking (`list_integrations`, `get_integration_docs`) maar **geen** docs-zoekfunctie. Val terug op Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Primair — gidsen, integraties, CLI-referentie, implementatie |
| `/dotnet/aspire` | Runtimebron — API-internals, implementatiedetails |
| `/communitytoolkit/aspire` | Community-integraties — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code-documentatie staat op **code.visualstudio.com**, niet op Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Gebruikersdocumentatie — instellingen, functies, foutopsporing, remote-ontwikkeling |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, commands, contribution points |

### GitHub — Use Context7

GitHub-documentatie staat op **docs.github.com** en **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repos, beveiliging, beheer, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) commando's en flags |

### Agent Framework — Use Learn MCP + Context7

Agent Framework-tutorials staan op learn.microsoft.com (gebruik `microsoft_docs_search`), maar de **GitHub-repo** bevat API-niveau details die vaak vooruitlopen op de gepubliceerde docs — met name de DevUI REST API-referentie, CLI-opties en .NET-integratie.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorials — DevUI-gidsen, tracing, workflow-orchestratie |
| `/microsoft/agent-framework` | API detail — DevUI REST-endpoints, CLI-flags, auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Raadpleeg de Learn-websitebron voor how-to-gidsen en daarna de repo-bron voor API-specifieke details (endpoint-schema's, proxyconfiguratie, auth-tokens).

---

## Context7 Setup

Voor elke Context7-query, los eerst de library ID op (eenmalig per sessie):

1. Roep `mcp_context7_resolve-library-id` aan met de technologienaam
2. Roep `mcp_context7_query-docs` aan met de teruggegeven library ID en een specifieke query

---

## Effectieve queries schrijven

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
- **Taal** voor polyglotte documentatie (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we naar nauwkeurigheid streven, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de originele taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->