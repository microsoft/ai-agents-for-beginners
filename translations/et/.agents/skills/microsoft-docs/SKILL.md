---
name: microsoft-docs
description: Küsib ametlikku Microsofti dokumentatsiooni, et leida mõisteid, juhendeid
  ja koodinäiteid Azure'i, .NET-i, Agent Frameworki, Aspire'i, VS Code'i, GitHubi
  ja muu kohta. Vaikimisi kasutatakse Microsoft Learn MCP-i; Context7 ja Aspire MCP-i
  kasutatakse sisu jaoks, mis asub väljaspool learn.microsoft.com-i.
---
# Microsoft Docs

Uurimisoskus Microsofti tehnoloogiate ökosüsteemi jaoks. Hõlmab learn.microsoft.com ja väljaspool seda asuvat dokumentatsiooni (VS Code, GitHub, Aspire, Agent Frameworki hoidlad).

---

## Default: Microsoft Learn MCP

Kasutage neid tööriistu **kõigi learn.microsoft.com lehel olevate materjalide** jaoks — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows ja muud. See on peamine tööriist enamikule Microsofti dokumentatsiooni päringutele.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Otsi learn.microsoft.com — kontseptsioonid, juhendid, õppetunnid, konfiguratsioon |
| `microsoft_code_sample_search` | Leia töötavad koodinäited Learn-dokumentidest. Parimate tulemuste saamiseks anna `language` (`python`, `csharp`, jne) |
| `microsoft_docs_fetch` | Hangi kogu lehe sisu konkreetsest URL-ist (kui otsingu väljavõtted ei piisa) |

Kasutage `microsoft_docs_fetch`-i pärast otsingut, kui vajate täielikke õpetusi, kõiki konfiguratsiooni valikuid või kui otsingu väljavõtted on kärbitud.

---

## Exceptions: When to Use Other Tools

Järgnevate kategooriate dokumentatsioon asub **väljaspool** learn.microsoft.com-i. Kasutage selle asemel määratud tööriista.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire'i dokumendid asuvad **aspire.dev**-is, mitte Learn'is. Parim tööriist sõltub teie Aspire CLI versioonist:

**CLI 13.2+** (soovitatav) — Aspire MCP server sisaldab sisseehitatud dokumentide otsingutööriistu:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Loetleb kogu aspire.dev-i dokumentatsiooni |
| `search_docs` | Kaalutud leksikaalne otsing aspire.dev sisu ulatuses |
| `get_doc` | Toob konkreetse dokumendi slugi järgi |

Need on kaasas Aspire CLI 13.2-s ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Uuendamiseks: `aspire update --self --channel daily`. Viide: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP server pakub integratsioonide otsimist (`list_integrations`, `get_integration_docs`), kuid ei paku dokumentide otsingut. Tuleks kasutada Context7-i:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Põhiline — juhendid, integratsioonid, CLI viide, juurutamine |
| `/dotnet/aspire` | Käitusaja lähtekood — API sise-elemendid, teostuse üksikasjad |
| `/communitytoolkit/aspire` | Kogukonna integratsioonid — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code dokumendid asuvad **code.visualstudio.com**-is, mitte Learn'is.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Kasutaja dokumentatsioon — seaded, funktsioonid, silumine, kaugarendus |
| `/websites/code_visualstudio_api` | Laienduse API — webviews, TreeViews, käsud, contribution points |

### GitHub — Use Context7

GitHubi dokumendid asuvad **docs.github.com** ja **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, hoidlad, turvalisus, admin, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) käsud ja lipud |

### Agent Framework — Use Learn MCP + Context7

Agent Frameworki õpetused on learn.microsoft.com-is (kasutage `microsoft_docs_search`), kuid **GitHubi hoidlas** on API-taseme üksikasjad, mis sageli eelsirguvad avaldatud dokumentatsioonist — eriti DevUI REST API viide, CLI valikud ja .NET integratsioon.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Õpetused — DevUI juhendid, traceerimine, töövoo orkestreerimine |
| `/microsoft/agent-framework` | API üksikasjad — DevUI REST lõpp-punktid, CLI lipud, autentimine, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Pärige Learn-veebisaidi lähteallikat how-to juhendite jaoks ja seejärel hoidla allikat API-taseme üksikasjade (lõpp-punktide skeemid, proxy konfiguratsioon, autentimistokenid) jaoks.

---

## Context7 Setup

Iga Context7 päringu jaoks lahendage esmalt library ID (üks kord per sessioon):

1. Käivitage `mcp_context7_resolve-library-id` koos tehnoloogia nimega
2. Käivitage `mcp_context7_query-docs` tagastatud library ID ja konkreetse päringuga

---

## Writing Effective Queries

Tõhusate päringute koostamiseks olge täpsed — lisage versioon, eesmärk ja keel:

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
- **Versioon** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Ülesande eesmärk** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Keel** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastutusest loobumine:

See dokument on tõlgitud tehisintellektil põhineva tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, tuleb arvestada, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Algset dokumenti selle emakeeles tuleks pidada autoriteetseks allikaks. Kriitilise tähtsusega teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta käesoleva tõlke kasutamisest tulenevate arusaamatuste ega väärtõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->