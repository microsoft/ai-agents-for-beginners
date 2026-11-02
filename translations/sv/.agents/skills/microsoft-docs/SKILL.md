---
name: microsoft-docs
description: Sök i officiell Microsoft-dokumentation för att hitta begrepp, handledningar
  och kodexempel inom Azure, .NET, Agent Framework, Aspire, VS Code, GitHub med mera.
  Använder Microsoft Learn MCP som standard, med Context7 och Aspire MCP för innehåll
  som finns utanför learn.microsoft.com.
---
# Microsoft Docs

Forskningsfärdighet för Microsofts teknologiekosystem. Täcker learn.microsoft.com och dokumentation som finns utanför detta (VS Code, GitHub, Aspire, Agent Framework-repositorier).

---

## Standard: Microsoft Learn MCP

Använd dessa verktyg för **allt på learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows och mer. Detta är det primära verktyget för de allra flesta Microsoft-dokumentationsfrågor.

| Verktyg | Syfte |
|------|---------|
| `microsoft_docs_search` | Sök på learn.microsoft.com — koncept, guider, handledningar, konfiguration |
| `microsoft_code_sample_search` | Hitta fungerande kodexempel från Learn-dokumentation. Använd `language` (`python`, `csharp`, osv.) för bästa resultat |
| `microsoft_docs_fetch` | Hämta komplett sidinnehåll från en specifik URL (när utdrag från sök inte räcker) |

Använd `microsoft_docs_fetch` efter sökning när du behöver kompletta handledningar, alla konfigurationsalternativ eller när sökutdrag är avkortade.

---

## Undantag: När man ska använda andra verktyg

Följande kategorier finns **utanför** learn.microsoft.com. Använd det angivna verktyget istället.

### Aspire — Använd Aspire MCP Server (föredras) eller Context7

Aspire-dokumentation finns på **aspire.dev**, inte på Learn. Det bästa verktyget beror på din Aspire CLI-version:

**CLI 13.2+** (rekommenderas) — Aspire MCP-servern inkluderar inbyggda sökverktyg för dokumentation:

| MCP-verktyg | Beskrivning |
|----------|-------------|
| `list_docs` | Listar all tillgänglig dokumentation från aspire.dev |
| `search_docs` | Viktad lexikalisk sökning över aspire.dev:s innehåll |
| `get_doc` | Hämtar ett specifikt dokument via slug |

Dessa ingår i Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). För att uppdatera: `aspire update --self --channel daily`.

**CLI 13.1** — MCP-servern erbjuder integreringsuppslag (`list_integrations`, `get_integration_docs`) men **ingen** dokumentsökning. Återgå till Context7:

| Biblioteks-ID | Används för |
|---|---|
| `/microsoft/aspire.dev` | Primärt — guider, integrationer, CLI-referens, distribution |
| `/microsoft/aspire` | Körningens källkod — API-internals, implementationsdetaljer |
| `/communitytoolkit/aspire` | Community-integrationer — Go, Java, Node.js, Ollama |

### VS Code — Använd Context7

VS Code-dokumentationen finns på **code.visualstudio.com**, inte på Learn.

| Biblioteks-ID | Används för |
|---|---|
| `/websites/code_visualstudio` | Användardokumentation — inställningar, funktioner, felsökning, fjärrutveckling |
| `/websites/code_visualstudio_api` | Tilläggs-API — webviews, TreeViews, kommandon, bidragspunkter |

### GitHub — Använd Context7

GitHub-dokumentation finns på **docs.github.com** och **cli.github.com**.

| Biblioteks-ID | Används för |
|---|---|
| `/websites/github_en` | Actions, API, repos, säkerhet, administration, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) kommandon och flaggor |

### Agent Framework — Använd Learn MCP + Context7

Agent Framework-handledningar finns på learn.microsoft.com (använd `microsoft_docs_search`), men **GitHub-repot** har API-nivådetaljer som ofta är före de publicerade dokumenten — särskilt DevUI REST API-referens, CLI-alternativ och .NET-integration.

| Biblioteks-ID | Används för |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Handledningar — DevUI-guider, spårning, arbetsflödsorkestrering |
| `/microsoft/agent-framework` | API-detaljer — DevUI REST-endpoints, CLI-flaggor, autentisering, .NET `AddDevUI`/`MapDevUI` |

**DevUI tips:** Fråga Learn-webbplatsens källa efter instruktionsguider, sedan repots källa för API-nivåsärskilda detaljer (endpoint-scheman, proxykonfiguration, autentiseringstoken).

---

## Context7 Setup

För varje Context7-fråga, lös bibliotekets ID först (en gång per session):

1. Anropa `mcp_context7_resolve-library-id` med teknologinamnet
2. Anropa `mcp_context7_query-docs` med det returnerade biblioteks-ID:t och en specifik fråga

---

## Att skriva effektiva frågor

Var specifik — inkludera version, avsikt och språk:

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

Inkludera kontext:
- **Version** när relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Uppgiftsavsikt** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Språk** för polyglotta dokument (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->