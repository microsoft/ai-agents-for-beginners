---
name: microsoft-docs
---
# Microsoft Docs

Research-færdighed for Microsoft-teknologiøkosystemet. Dækker learn.microsoft.com og dokumentation, der findes uden for det (VS Code, GitHub, Aspire, Agent Framework repos).

---

## Standard: Microsoft Learn MCP

Brug disse værktøjer til **alt på learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows og mere. Dette er det primære værktøj til langt de fleste forespørgsler om Microsoft-dokumentation.

| Værktøj | Formål |
|------|---------|
| `microsoft_docs_search` | Søg på learn.microsoft.com — begreber, vejledninger, tutorials, konfiguration |
| `microsoft_code_sample_search` | Find fungerende kodeeksempler fra Learn-dokumenter. Brug `language` (`python`, `csharp`, osv.) for bedst resultat |
| `microsoft_docs_fetch` | Få fuld sideindhold fra en specifik URL (når uddrag fra søgning ikke er nok) |

Brug `microsoft_docs_fetch` efter søgning, når du har brug for komplette tutorials, alle konfigurationsmuligheder, eller når uddrag fra søgningen er afkortede.

---

## Undtagelser: Hvornår bruges andre værktøjer

Følgende kategorier ligger **uden for** learn.microsoft.com. Brug det angivne værktøj i stedet.

### Aspire — Brug Aspire MCP Server (foretrukket) eller Context7

Aspire-dokumenter findes på **aspire.dev**, ikke Learn. Det bedste værktøj afhænger af din Aspire CLI-version:

**CLI 13.2+** (anbefalet) — Aspire MCP-serveren indeholder indbyggede søgeværktøjer til dokumentation:

| MCP-værktøj | Beskrivelse |
|----------|-------------|
| `list_docs` | Viser alle tilgængelige dokumenter fra aspire.dev |
| `search_docs` | Vægtet leksikal søgning på aspire.dev indhold |
| `get_doc` | Henter et specifikt dokument ved slug |

Disse følger med Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). For at opdatere: `aspire update --self --channel daily`.

**CLI 13.1** — MCP-serveren giver integrationsopslag (`list_integrations`, `get_integration_docs`) men **ikke** dokumentsøgning. Brug i stedet Context7:

| Biblioteks-ID | Brug til |
|---|---|
| `/microsoft/aspire.dev` | Primært — vejledninger, integrationer, CLI-reference, udrulning |
| `/microsoft/aspire` | Runtime-kilde — API-intern info, implementeringsdetaljer |
| `/communitytoolkit/aspire` | Community-integrationer — Go, Java, Node.js, Ollama |

### VS Code — Brug Context7

VS Code-dokumenter findes på **code.visualstudio.com**, ikke Learn.

| Biblioteks-ID | Brug til |
|---|---|
| `/websites/code_visualstudio` | Brugerdokumenter — indstillinger, funktioner, fejlfinding, fjernudvikling |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, kommandoer, bidragspunkter |

### GitHub — Brug Context7

GitHub-dokumenter findes på **docs.github.com** og **cli.github.com**.

| Biblioteks-ID | Brug til |
|---|---|
| `/websites/github_en` | Actions, API, repos, sikkerhed, administration, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) kommandoer og flag |

### Agent Framework — Brug Learn MCP + Context7

Agent Framework tutorials findes på learn.microsoft.com (brug `microsoft_docs_search`), men **GitHub repoet** har API-niveau detaljer, som ofte er foran offentliggjorte dokumenter — især DevUI REST API-reference, CLI-indstillinger og .NET-integration.

| Biblioteks-ID | Brug til |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorials — DevUI-vejledninger, sporing, workflow orkestrering |
| `/microsoft/agent-framework` | API-detaljer — DevUI REST-endpoints, CLI-flag, autentificering, .NET `AddDevUI`/`MapDevUI` |

**DevUI-tip:** Søg først i Learn-webstedets kilde efter hvordan-man-gør-vejledninger, og derefter i repo-kilden for API-specifikke detaljer (endpointskemaer, proxykonfiguration, autentificeringstokens).

---

## Context7 Opsætning

Ved enhver Context7-forespørgsel, find først biblioteks-ID'et (én gang per session):

1. Kald `mcp_context7_resolve-library-id` med teknologinavnet
2. Kald `mcp_context7_query-docs` med det returnerede biblioteks-ID og en specifik forespørgsel

---

## Skriv Effektive Forespørgsler

Vær specifik — medtag version, formål og sprog:

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

Medtag kontekst:
- **Version** når relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Opgavens formål** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Sprog** til polyglot dokumenter (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->