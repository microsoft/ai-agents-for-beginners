---
name: microsoft-docs
description: Poizvedujte v uradni Microsoftovi dokumentaciji, da poiščete koncepte,
  vodiče in primere kode za Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  in še več. Privzeto uporablja Microsoft Learn MCP, za vsebino, ki se nahaja zunaj
  learn.microsoft.com, pa Context7 in Aspire MCP.
---
# Microsoft Docs

Raziskovalna veščina za Microsoftov tehnološki ekosistem. Vključuje learn.microsoft.com in dokumentacijo, ki živi izven njega (VS Code, GitHub, Aspire, Agent Framework repozitoriji).

---

## Privzeto: Microsoft Learn MCP

Uporabite ta orodja za **vse na learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows in več. To je primarno orodje za veliko večino poizvedb glede Microsoftove dokumentacije.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Išči learn.microsoft.com — koncepti, vodiči, vadnice, konfiguracije |
| `microsoft_code_sample_search` | Poiščite delujoče primere kode iz Learn dokumentacije. Posredujte `language` (`python`, `csharp`, itd.) za najboljše rezultate |
| `microsoft_docs_fetch` | Pridobi celotno vsebino strani z določene URL (ko izvlečki iskanja niso dovolj) |

Uporabite `microsoft_docs_fetch` po iskanju, ko potrebujete celotne vodiče, vse možnosti konfiguracije, ali ko so izvlečki iskanja skrajšani.

---

## Izjeme: Kdaj uporabiti druga orodja

Naslednje kategorije obstajajo **izven** learn.microsoft.com. Namesto tega uporabite navedeno orodje.

### .NET Aspire — Uporabite Aspire MCP Server (priporočeno) ali Context7

Dokumentacija Aspire je na **aspire.dev**, ne na Learn. Najboljše orodje je odvisno od različice vašega Aspire CLI:

**CLI 13.2+** (priporočeno) — Aspire MCP strežnik vključuje vgrajena orodja za iskanje dokumentacije:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Našteje vso razpoložljivo dokumentacijo z aspire.dev |
| `search_docs` | Uteženo leksikalno iskanje po vsebini aspire.dev |
| `get_doc` | Pridobi določen dokument po slugu |

Te so v Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Za posodobitev: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP strežnik zagotavlja iskanje integracij (`list_integrations`, `get_integration_docs`) vendar **ne** iskanje dokumentacije. Uporabite Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Primarno — vodiči, integracije, referenca CLI, uvajanje |
| `/dotnet/aspire` | Izvor za izvajanje — API-ja notranjosti, podrobnosti implementacije |
| `/communitytoolkit/aspire` | Skupnostne integracije — Go, Java, Node.js, Ollama |

### VS Code — Uporabite Context7

Dokumentacija VS Code je na **code.visualstudio.com**, ne na Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Uporabniška dokumentacija — nastavitve, funkcije, razhroščevanje, oddaljeni razvoj |
| `/websites/code_visualstudio_api` | API za razširitve — webviews, TreeViews, ukazi, prispevne točke |

### GitHub — Uporabite Context7

Dokumentacija GitHub je na **docs.github.com** in **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repozitoriji, varnost, administracija, Copilot |
| `/websites/cli_github` | Ukazi in zastavice GitHub CLI (`gh`) |

### Agent Framework — Uporabite Learn MCP + Context7

Vodiči za Agent Framework so na learn.microsoft.com (uporabite `microsoft_docs_search`), vendar ima **GitHub repozitorij** podrobnosti na ravni API, ki so pogosto pred objavljenimi dokumenti — zlasti referenca DevUI REST API, možnosti CLI in integracija .NET.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Vodiči — DevUI vodiči, sledenje, orkestracija delovnih tokov |
| `/microsoft/agent-framework` | Podrobnosti API — DevUI REST končne točke, CLI zastavice, avtentikacija, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Poizvedujte po izvoru spletne strani Learn za vodnike 'how-to', nato pa po izvoru repozitorija za podrobnosti na ravni API (sheme končnih točk, proxy konfiguracija, avtentikacijski žetoni).

---

## Context7 Setup

Za vsako poizvedbo Context7 najprej razrešite ID knjižnice (enkrat na sejo):

1. Pokličite `mcp_context7_resolve-library-id` z imenom tehnologije
2. Pokličite `mcp_context7_query-docs` z vrnjenim ID-jem knjižnice in specifično poizvedbo

---

## Pisanje učinkovitih poizvedb

Bodite konkretni — vključite različico, namen in jezik:

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
- **Različica** ko je relevantno (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Namen naloge** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Jezik** za poliglotsko dokumentacijo (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Izjava o omejitvi odgovornosti:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvor­nem jeziku velja za avtoritativni vir. Za kritične informacije priporočamo strokovni prevod, opravljen s strani človeka. Ne odgovarjamo za morebitna nerazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->