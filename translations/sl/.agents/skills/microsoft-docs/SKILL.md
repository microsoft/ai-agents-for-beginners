---
name: microsoft-docs
description: Poizvedovanje uradne Microsoftove dokumentacije za iskanje konceptov,
  vodičev in primerov kode v Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  in še več. Kot privzeto uporablja Microsoft Learn MCP, za vsebino, ki je zunaj learn.microsoft.com,
  pa Context7 in Aspire MCP.
---
# Microsoft Docs

Spretnost raziskovanja za Microsoftov tehnološki ekosistem. Vsebuje learn.microsoft.com in dokumentacijo, ki živi zunaj njega (VS Code, GitHub, Aspire, Agent Framework repozitoriji).

---

## Privzeto: Microsoft Learn MCP

Uporabite ta orodja za **vse na learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows in več. To je glavno orodje za velikansko večino poizvedb o Microsoftovi dokumentaciji.

| Orodje | Namen |
|------|---------|
| `microsoft_docs_search` | Iskanje na learn.microsoft.com — koncepti, vodniki, vadnice, konfiguracija |
| `microsoft_code_sample_search` | Iskanje delujočih izvlečkov kode iz Learn dokumentacije. Podajte `language` (`python`, `csharp`, itd.) za najboljše rezultate |
| `microsoft_docs_fetch` | Dobite celotno vsebino strani z določenega URL-ja (ko izvlečki iskanja niso dovolj) |

Uporabite `microsoft_docs_fetch` po iskanju, ko potrebujete popolne vadnice, vse konfiguracijske možnosti ali ko so izvlečki iskanja skrajšani.

---

## Izjeme: Kdaj uporabiti druga orodja

Naslednje kategorije so **izven** learn.microsoft.com. Namesto tega uporabite določeno orodje.

### Aspire — uporabite Aspire MCP strežnik (priporočeno) ali Context7

Aspire dokumentacija je na **aspire.dev**, ne na Learn. Najboljše orodje je odvisno od vaše Aspire CLI različice:

**CLI 13.2+** (priporočeno) — Aspire MCP strežnik vključuje vgrajena orodja za iskanje v dokumentaciji:

| MCP orodje | Opis |
|----------|-------------|
| `list_docs` | Prikaže vse na voljo dokumente z aspire.dev |
| `search_docs` | Neuravnoteženo leksikalno iskanje v vsebini aspire.dev |
| `get_doc` | Pridobi določen dokument po slugu |

Ta so vključena v Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Za posodobitev: `aspire update --self --channel daily`.

**CLI 13.1** — MCP strežnik ponuja iskanje integracij (`list_integrations`, `get_integration_docs`) vendar **ne** iskanje dokumentacije. Vrnite se na Context7:

| ID knjižnice | Uporaba za |
|---|---|
| `/microsoft/aspire.dev` | Primarno — vodniki, integracije, CLI referenca, namestitev |
| `/microsoft/aspire` | Izvor izvajanja — API notranjosti, podrobnosti implementacije |
| `/communitytoolkit/aspire` | Skupnostne integracije — Go, Java, Node.js, Ollama |

### VS Code — uporabi Context7

VS Code dokumentacija je na **code.visualstudio.com**, ne na Learn.

| ID knjižnice | Uporaba za |
|---|---|
| `/websites/code_visualstudio` | Uporabniška dokumentacija — nastavitve, funkcije, odpravljanje napak, oddaljen razvoj |
| `/websites/code_visualstudio_api` | Razširitev API — spletni prikazi, TreeViews, ukazi, prispevne točke |

### GitHub — uporabi Context7

GitHub dokumentacija je na **docs.github.com** in **cli.github.com**.

| ID knjižnice | Uporaba za |
|---|---|
| `/websites/github_en` | Actions, API, repozitoriji, varnost, upravljanje, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) ukazi in zastavice |

### Agent Framework — uporabi Learn MCP + Context7

Vadnice za Agent Framework so na learn.microsoft.com (uporabite `microsoft_docs_search`), vendar ima **GitHub repozitorij** podrobnosti na nivoju API, ki pogosto prednjačijo pred objavljeno dokumentacijo — predvsem DevUI REST API referenco, možnosti CLI in .NET integracijo.

| ID knjižnice | Uporaba za |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Vadnice — DevUI vodniki, sledljivost, orkestracija potekov dela |
| `/microsoft/agent-framework` | Podrobnosti API — DevUI REST končne točke, CLI zastavice, avtentikacija, .NET `AddDevUI`/`MapDevUI` |

**Nasvet za DevUI:** Poizvedujte Learn spletno mesto za kako vodnike, nato pa repozitorij za API podrobnosti (sheme končnih točk, konfiguracija proxyja, avtorizacijski žetoni).

---

## Nastavitev Context7

Za katerokoli Context7 poizvedbo najprej razjasnite ID knjižnice (eno na sejo):

1. Pokličite `mcp_context7_resolve-library-id` z imenom tehnologije
2. Pokličite `mcp_context7_query-docs` z vrnjenim ID knjižnice in določeno poizvedbo

---

## Pisanje učinkovitih poizvedb

Bodite specifični — vključite različico, namen in jezik:

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

Vključite kontekst:
- **Različica** kjer je pomembno (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Namen naloge** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Jezik** za poliglotske dokumente (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->