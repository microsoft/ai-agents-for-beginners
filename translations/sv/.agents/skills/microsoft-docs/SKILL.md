---
name: microsoft-docs
description: Fråga den officiella Microsoft-dokumentationen för att hitta koncept,
  handledningar och kodexempel inom Azure, .NET, Agent Framework, Aspire, VS Code,
  GitHub och mer. Använder Microsoft Learn MCP som standard, med Context7 och Aspire
  MCP för innehåll som finns utanför learn.microsoft.com.
---
# Microsoft Docs

Forskningskompetens för Microsofts teknologiekosystem. Täcker learn.microsoft.com och dokumentation som finns utanför det (VS Code, GitHub, Aspire, Agent Framework repos).

---

## Standard: Microsoft Learn MCP

Använd dessa verktyg för **allt på learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows och mer. Detta är det primära verktyget för majoriteten av Microsoft-dokumentationsfrågor.

| Verktyg | Syfte |
|------|---------|
| `microsoft_docs_search` | Sök på learn.microsoft.com — begrepp, guider, handledningar, konfiguration |
| `microsoft_code_sample_search` | Hitta fungerande kodexempel från Learn-dokumentation. Ange `language` (`python`, `csharp`, etc.) för bästa resultat |
| `microsoft_docs_fetch` | Hämta hela sidans innehåll från en specifik URL (när sökutdrag inte räcker) |

Använd `microsoft_docs_fetch` efter sökning när du behöver kompletta handledningar, alla konfigurationsalternativ eller när sökutdrag avkortas.

---

## Undantag: När man ska använda andra verktyg

Följande kategorier finns **utanför** learn.microsoft.com. Använd istället det angivna verktyget.

### .NET Aspire — Använd Aspire MCP Server (föredras) eller Context7

Aspire-dokumentation finns på **aspire.dev**, inte på Learn. Det bästa verktyget beror på din Aspire CLI-version:

**CLI 13.2+** (rekommenderat) — Aspire MCP-servern inkluderar inbyggda verktyg för dokumentsökning:

| MCP-verktyg | Beskrivning |
|----------|-------------|
| `list_docs` | Visar all tillgänglig dokumentation från aspire.dev |
| `search_docs` | Viktad lexikal sökning över aspire.dev-innehåll |
| `get_doc` | Hämtar ett specifikt dokument via slug |

Dessa levereras i Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). För att uppdatera: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP-servern erbjuder integrationssökning (`list_integrations`, `get_integration_docs`) men **inte** dokumentsökning. Falla tillbaka till Context7:

| Library ID | Använd för |
|---|---|
| `/microsoft/aspire.dev` | Primär — guider, integrationer, CLI-referens, driftsättning |
| `/dotnet/aspire` | Körningskällkod — API-interna delar, implementeringsdetaljer |
| `/communitytoolkit/aspire` | Community-integrationer — Go, Java, Node.js, Ollama |

### VS Code — Använd Context7

VS Code-dokumentation finns på **code.visualstudio.com**, inte på Learn.

| Library ID | Använd för |
|---|---|
| `/websites/code_visualstudio` | Användardokumentation — inställningar, funktioner, felsökning, fjärrutveckling |
| `/websites/code_visualstudio_api` | Tilläggs-API — webviews, TreeViews, kommandon, bidragspunkter |

### GitHub — Använd Context7

GitHub-dokumentation finns på **docs.github.com** och **cli.github.com**.

| Library ID | Använd för |
|---|---|
| `/websites/github_en` | Actions, API, repo, säkerhet, administration, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) kommandon och flaggor |

### Agent Framework — Använd Learn MCP + Context7

Agent Framework-handledningar finns på learn.microsoft.com (använd `microsoft_docs_search`), men **GitHub-repot** innehåller API-nivådetaIjer som ofta ligger före de publicerade dokumenten — särskilt DevUI REST API-referensen, CLI-alternativ och .NET-integration.

| Library ID | Använd för |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Handledningar — DevUI-guider, spårning, orkestrering av arbetsflöden |
| `/microsoft/agent-framework` | API-detaljer — DevUI REST-endpoints, CLI-flaggor, autentisering, .NET `AddDevUI`/`MapDevUI` |

DevUI-tips: Sök i Learn-webbplatsens källkod för how-to-guider, och i repots källkod för API-specifika detaljer (endpunktscheman, proxykonfiguration, autentiseringstoken).

---

## Context7 Setup

För alla Context7-frågor, bestäm bibliotekets ID först (en gång per session):

1. Anropa `mcp_context7_resolve-library-id` med tekniknamnet
2. Anropa `mcp_context7_query-docs` med det returnerade bibliotekets ID och en specifik fråga

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

Include context:
- **Version** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Uppgiftsavsikt** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Språk** för polyglotta dokument (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfriskrivning:
Detta dokument har översatts med hjälp av AI-översättningstjänsten Co-op Translator (https://github.com/Azure/co-op-translator). Vi eftersträvar noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet i dess ursprungliga språkversion bör betraktas som den auktoritativa källan. För kritisk information rekommenderas en professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->