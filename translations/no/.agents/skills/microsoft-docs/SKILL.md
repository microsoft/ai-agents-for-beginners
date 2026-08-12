---
name: microsoft-docs
description: Søk i offisiell Microsoft-dokumentasjon for å finne konsepter, veiledninger
  og kodeeksempler på tvers av Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  og mer. Bruker Microsoft Learn MCP som standard, med Context7 og Aspire MCP for
  innhold som ligger utenfor learn.microsoft.com.
---
# Microsoft Docs

Forskningsverktøy for Microsoft-teknologiøkosystemet. Dekker learn.microsoft.com og dokumentasjon som ligger utenfor det (VS Code, GitHub, Aspire, Agent Framework-repositorier).

---

## Standard: Microsoft Learn MCP

Bruk disse verktøyene for **alt på learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows og mer. Dette er hovedverktøyet for langt de fleste Microsoft-dokumentasjonsforespørsler.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Søk på learn.microsoft.com — konsepter, veiledninger, opplæringer, konfigurasjon |
| `microsoft_code_sample_search` | Finn fungerende kodeeksempler fra Learn-dokumenter. Oppgi `language` (`python`, `csharp`, etc.) for beste resultat |
| `microsoft_docs_fetch` | Hent hele sidens innhold fra en spesifikk URL (når søkutdrag ikke er nok) |

Bruk `microsoft_docs_fetch` etter søk når du trenger komplette opplæringer, alle konfigurasjonsalternativer, eller når søkutdrag er trunkert.

---

## Exceptions: When to Use Other Tools

Følgende kategorier ligger **utenfor** learn.microsoft.com. Bruk det angitte verktøyet i stedet.

### .NET Aspire — Bruk Aspire MCP Server (foretrukket) eller Context7

Aspire-dokumentasjon ligger på **aspire.dev**, ikke Learn. Det beste verktøyet avhenger av hvilken Aspire CLI-versjon du har:

**CLI 13.2+** (anbefalt) — Aspire MCP-serveren inkluderer innebygde dokumentsøkeverktøy:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Lister all tilgjengelig dokumentasjon fra aspire.dev |
| `search_docs` | Vektet leksikalsøk på tvers av aspire.dev-innhold |
| `get_doc` | Henter et bestemt dokument etter slug |

Disse følger med i Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). For å oppdatere: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP-serveren tilbyr integrasjonsoppslag (`list_integrations`, `get_integration_docs`) men **ikke** dokumentsøk. Fall tilbake til Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Primær — veiledninger, integrasjoner, CLI-referanse, distribusjon |
| `/dotnet/aspire` | Kjøretidskilde — API-interne detaljer, implementasjonsdetaljer |
| `/communitytoolkit/aspire` | Fellesskapsintegrasjoner — Go, Java, Node.js, Ollama |

### VS Code — Bruk Context7

VS Code-dokumentasjon ligger på **code.visualstudio.com**, ikke Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Brukerdokumentasjon — innstillinger, funksjoner, feilsøking, fjernutvikling |
| `/websites/code_visualstudio_api` | Utvidelses-API — webviews, TreeViews, kommandoer, bidragspunkter |

### GitHub — Bruk Context7

GitHub-dokumentasjon ligger på **docs.github.com** og **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repos, sikkerhet, administrasjon, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) kommandoer og flagg |

### Agent Framework — Bruk Learn MCP + Context7

Agent Framework-opplæringer er på learn.microsoft.com (bruk `microsoft_docs_search`), men **GitHub-repoet** har API-nivådetaljer som ofte ligger foran publiserte docs — spesielt DevUI REST API-referansen, CLI-alternativer og .NET-integrasjon.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Opplæringer — DevUI-veiledninger, sporing, arbeidsflytorkestrering |
| `/microsoft/agent-framework` | API-detaljer — DevUI REST-endepunkter, CLI-flagg, autentisering, .NET `AddDevUI`/`MapDevUI` |

**DevUI-tip:** Søk i Learn-nettstedets kilde for veiledninger, og deretter i repo-kilden for API-nivås detaljer (endepunktskjemaer, proxy-konfigurasjon, autentiseringstokener).

---

## Context7-oppsett

For enhver Context7-forespørsel, løs opp bibliotek-ID først (én gang per økt):

1. Kall `mcp_context7_resolve-library-id` med teknologinavnet
2. Kall `mcp_context7_query-docs` med den returnerte bibliotek-IDen og en spesifikk forespørsel

---

## Å skrive effektive forespørsler

Vær spesifikk — inkluder versjon, hensikt og språk:

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

Inkluder kontekst:
- **Versjon** når relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Oppgaveintensjon** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Språk** for flerspråklig dokumentasjon (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet har blitt oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som følge av bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->