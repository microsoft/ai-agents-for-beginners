---
name: microsoft-docs
---
# Microsoft Docs

Forskningsevne for Microsoft teknologiekosystemet. Dekker learn.microsoft.com og dokumentasjon som ligger utenfor den (VS Code, GitHub, Aspire, Agent Framework-repos).

---

## Standard: Microsoft Learn MCP

Bruk disse verktøyene for **alt på learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows og mer. Dette er hovedverktøyet for det store flertallet av Microsoft-dokumentasjonsspørsmål.

| Verktøy | Formål |
|------|---------|
| `microsoft_docs_search` | Søk på learn.microsoft.com — konsepter, veiledninger, opplæringskurs, konfigurasjon |
| `microsoft_code_sample_search` | Finn fungerende kodeeksempler fra Learn-dokumenter. Bruk `language` (`python`, `csharp`, osv.) for best resultat |
| `microsoft_docs_fetch` | Hent fullsideinnhold fra en spesifikk URL (når søk utdrag ikke er nok) |

Bruk `microsoft_docs_fetch` etter søk når du trenger komplette opplæringskurs, alle konfigurasjonsvalg eller når søkutdrag er forkortet.

---

## Unntak: Når du skal bruke andre verktøy

Følgende kategorier ligger **utenfor** learn.microsoft.com. Bruk det angitte verktøyet i stedet.

### Aspire — Bruk Aspire MCP Server (foretrukket) eller Context7

Aspire-dokumenter ligger på **aspire.dev**, ikke Learn. Det beste verktøyet avhenger av din Aspire CLI-versjon:

**CLI 13.2+** (anbefalt) — Aspire MCP-serveren inkluderer innebygde dokumentasjonssøkverktøy:

| MCP-verktøy | Beskrivelse |
|----------|-------------|
| `list_docs` | Lister all tilgjengelig dokumentasjon fra aspire.dev |
| `search_docs` | Vektet leksikalsøk i aspire.dev-innhold |
| `get_doc` | Henter et spesifikt dokument etter slug |

Disse leveres med Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). For å oppdatere: `aspire update --self --channel daily`.

**CLI 13.1** — MCP-serveren tilbyr integrasjonsoppslag (`list_integrations`, `get_integration_docs`) men **ikke** dokumentasjonssøk. Bruk Context7 som fallback:

| Bibliotek-ID | Bruk for |
|---|---|
| `/microsoft/aspire.dev` | Primær — veiledninger, integrasjoner, CLI-referanse, distribusjon |
| `/microsoft/aspire` | Kjøretidskilde — API-internals, implementasjonsdetaljer |
| `/communitytoolkit/aspire` | Fellesskapsintegrasjoner — Go, Java, Node.js, Ollama |

### VS Code — Bruk Context7

VS Code-dokumentasjon ligger på **code.visualstudio.com**, ikke Learn.

| Bibliotek-ID | Bruk for |
|---|---|
| `/websites/code_visualstudio` | Brukerdokumentasjon — innstillinger, funksjoner, feilsøking, fjernutvikling |
| `/websites/code_visualstudio_api` | Extension API — webvisninger, TreeViews, kommandoer, bidragspunkter |

### GitHub — Bruk Context7

GitHub-dokumentasjon ligger på **docs.github.com** og **cli.github.com**.

| Bibliotek-ID | Bruk for |
|---|---|
| `/websites/github_en` | Actions, API, repos, sikkerhet, administrasjon, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) kommandoer og flagg |

### Agent Framework — Bruk Learn MCP + Context7

Agent Framework-opplæringskurs er på learn.microsoft.com (bruk `microsoft_docs_search`), men **GitHub-repoet** har API-nivå detaljer som ofte er foran publiserte dokumenter — særlig DevUI REST API-referanse, CLI-valg og .NET-integrasjon.

| Bibliotek-ID | Bruk for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Opplæringskurs — DevUI-veiledninger, sporing, arbeidsflytorkestrering |
| `/microsoft/agent-framework` | API-detaljer — DevUI REST-endepunkter, CLI-flagg, autentisering, .NET `AddDevUI`/`MapDevUI` |

**DevUI-tips:** Spørr Learn-nettstedets kilde for hvordan-veiledninger, deretter repo-kilden for API-nivå spesifikasjoner (endepunktskjemaer, proxy-konfigurasjon, autentiseringstokener).

---

## Context7-oppsett

For alle Context7-spørringer, finn først bibliotek-ID (én gang per økt):

1. Kall `mcp_context7_resolve-library-id` med teknologienavnet
2. Kall `mcp_context7_query-docs` med den returnerte bibliotek-ID-en og en spesifikk forespørsel

---

## Skrive effektive forespørsler

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
- **Oppgavehensikt** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Språk** for flerspråklig dokumentasjon (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->