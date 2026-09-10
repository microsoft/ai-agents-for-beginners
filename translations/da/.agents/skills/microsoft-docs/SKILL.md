---
name: microsoft-docs
description: Søg i den officielle Microsoft-dokumentation for at finde koncepter,
  vejledninger og kodeeksempler på tværs af Azure, .NET, Agent Framework, Aspire,
  VS Code, GitHub og mere. Bruger Microsoft Learn MCP som standard, samt Context7
  og Aspire MCP til indhold, der findes uden for learn.microsoft.com.
---
# Microsoft Docs

Forskningsfærdighed for Microsoft-teknologiøkosystemet. Dækker learn.microsoft.com og dokumentation, der ligger udenfor det (VS Code, GitHub, Aspire, Agent Framework-repositorier).

---

## Default: Microsoft Learn MCP

Brug disse værktøjer til **alt på learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows og mere. Dette er det primære værktøj til langt de fleste Microsoft-dokumentationsforespørgsler.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Søg på learn.microsoft.com — koncepter, guider, tutorials, konfiguration |
| `microsoft_code_sample_search` | Find fungerende kodeeksempler fra Learn-dokumenter. Angiv `language` (`python`, `csharp`, etc.) for bedste resultater |
| `microsoft_docs_fetch` | Hent hele sidens indhold fra en bestemt URL (når søgeuddrag ikke er nok) |

Brug `microsoft_docs_fetch` efter søgning, når du har brug for komplette vejledninger, alle konfigurationsmuligheder, eller når søgeuddrag er trunkeret.

---

## Exceptions: When to Use Other Tools

Følgende kategorier ligger **udenfor** learn.microsoft.com. Brug det angivne værktøj i stedet.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire-dokumenter ligger på **aspire.dev**, ikke Learn. Det bedste værktøj afhænger af din Aspire CLI-version:

**CLI 13.2+** (anbefales) — Aspire MCP-serveren inkluderer indbyggede dokumentsøgeværktøjer:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Lister al tilgængelig dokumentation fra aspire.dev |
| `search_docs` | Vægtet leksikalsk søgning i aspire.dev-indhold |
| `get_doc` | Henter et specifikt dokument efter slug |

Disse leveres i Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). For at opdatere: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP-serveren tilbyder integrationsopslag (`list_integrations`, `get_integration_docs`) men **ikke** dokumentsøgning. Fald tilbage til Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Primær — guider, integrationer, CLI-reference, deployment |
| `/dotnet/aspire` | Runtime-kilde — API-interne detaljer, implementeringsdetaljer |
| `/communitytoolkit/aspire` | Fællesskabsintegrationer — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code-dokumentation findes på **code.visualstudio.com**, ikke Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Brugerdokumentation — indstillinger, funktioner, fejlfinding, remote dev |
| `/websites/code_visualstudio_api` | Udvidelses-API — webviews, TreeViews, kommandoer, contribution points |

### GitHub — Use Context7

GitHub-dokumentation findes på **docs.github.com** og **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repoer, sikkerhed, administration, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) kommandoer og flag |

### Agent Framework — Use Learn MCP + Context7

Agent Framework-vejledninger er på learn.microsoft.com (brug `microsoft_docs_search`), men **GitHub-repositoriet** har API-niveau detaljer, der ofte er foran de publicerede docs — især DevUI REST API-reference, CLI-indstillinger og .NET-integration.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorials — DevUI-guides, tracing, workflow orchestration |
| `/microsoft/agent-framework` | API-detaljer — DevUI REST-endpoints, CLI-flags, auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Forespørg Learn-webstedets kilde efter how-to-guides, og brug derefter repo-kilden til API-specifikke detaljer (endpunktskemaer, proxy-konfiguration, auth-tokens).

---

## Context7 Setup

For enhver Context7-forespørgsel, opløs biblioteks-ID'et først (en-gangs per session):

1. Call `mcp_context7_resolve-library-id` with the technology name
2. Call `mcp_context7_query-docs` with the returned library ID and a specific query

---

## Writing Effective Queries

Vær specifik — inkluder version, formål og sprog:

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
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Originaldokumentet på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->