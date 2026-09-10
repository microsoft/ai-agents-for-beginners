---
name: microsoft-docs
description: Interoghează documentația oficială Microsoft pentru a găsi concepte,
  tutoriale și exemple de cod pentru Azure, .NET, Agent Framework, Aspire, VS Code,
  GitHub și altele. Folosește Microsoft Learn MCP ca implicit, iar pentru conținutul
  care se află în afara learn.microsoft.com utilizează Context7 și Aspire MCP.
---
# Microsoft Docs

Abilitate de cercetare pentru ecosistemul tehnologic Microsoft. Acoperă learn.microsoft.com și documentația care există în afara acestuia (VS Code, GitHub, Aspire, depozitele Agent Framework).

---

## Implicit: Microsoft Learn MCP

Folosește aceste instrumente pentru **tot ce se află pe learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows și altele. Acesta este instrumentul principal pentru marea majoritate a interogărilor legate de documentația Microsoft.

| Instrument | Scop |
|------|---------|
| `microsoft_docs_search` | Caută în learn.microsoft.com — concepte, ghiduri, tutoriale, configurare |
| `microsoft_code_sample_search` | Găsește fragmente de cod funcționale din documentele Learn. Transmite `language` (`python`, `csharp`, etc.) pentru cele mai bune rezultate |
| `microsoft_docs_fetch` | Obține conținutul complet al paginii dintr-un URL specific (când extrasele din căutare nu sunt suficiente) |

Folosește `microsoft_docs_fetch` după căutare când ai nevoie de tutoriale complete, toate opțiunile de configurare sau când extrasele din căutare sunt trunchiate.

---

## Excepții: Când să folosești alte instrumente

Următoarele categorii există **în afara** learn.microsoft.com. Folosește instrumentul specificat în schimb.

### .NET Aspire — Folosește Aspire MCP Server (preferat) sau Context7

Documentația Aspire se află pe **aspire.dev**, nu pe Learn. Cel mai bun instrument depinde de versiunea CLI Aspire pe care o folosești:

**CLI 13.2+** (recomandat) — Serverul Aspire MCP include instrumente încorporate de căutare în documentație:

| Instrument MCP | Descriere |
|----------|-------------|
| `list_docs` | Listează toată documentația disponibilă de pe aspire.dev |
| `search_docs` | Căutare lexicală ponderată în conținutul aspire.dev |
| `get_doc` | Recuperează un document specific după slug |

Acestea sunt incluse în Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Pentru actualizare: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — Serverul MCP oferă căutare a integrărilor (`list_integrations`, `get_integration_docs`) dar **nu** oferă căutare în documentație. Recurge la Context7:

| Library ID | Utilizare pentru |
|---|---|
| `/microsoft/aspire.dev` | Principal — ghiduri, integrări, referință CLI, deployment |
| `/dotnet/aspire` | Sursă runtime — internals API, detalii de implementare |
| `/communitytoolkit/aspire` | Integrări comunitare — Go, Java, Node.js, Ollama |

### VS Code — Folosește Context7

Documentația VS Code se află pe **code.visualstudio.com**, nu pe Learn.

| Library ID | Utilizare pentru |
|---|---|
| `/websites/code_visualstudio` | Documentație utilizator — setări, funcționalități, depanare, dezvoltare la distanță |
| `/websites/code_visualstudio_api` | API pentru extensii — webviews, TreeViews, comenzi, puncte de contribuție |

### GitHub — Folosește Context7

Documentația GitHub se află pe **docs.github.com** și **cli.github.com**.

| Library ID | Utilizare pentru |
|---|---|
| `/websites/github_en` | Actions, API, repository-uri, securitate, administrare, Copilot |
| `/websites/cli_github` | Comenzi și flag-uri GitHub CLI (`gh`) |

### Agent Framework — Folosește Learn MCP + Context7

Tutorialele Agent Framework sunt pe learn.microsoft.com (folosește `microsoft_docs_search`), dar **repozitorul GitHub** conține detalii la nivel de API care sunt adesea înaintea documentației publicate — în special referința DevUI REST API, opțiunile CLI și integrarea .NET.

| Library ID | Utilizare pentru |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutoriale — ghiduri DevUI, trasare, orchestrarea fluxurilor de lucru |
| `/microsoft/agent-framework` | Detalii API — endpoint-uri DevUI REST, flag-uri CLI, autentificare, .NET `AddDevUI`/`MapDevUI` |

**DevUI tip:** Interoghează sursa site-ului Learn pentru ghiduri practice, apoi sursa din repo pentru specificații la nivel de API (scheme de endpoint, configurare proxy, token-uri de autentificare).

---

## Configurare Context7

Pentru orice interogare Context7, rezolvă mai întâi ID-ul bibliotecii (o singură dată pe sesiune):

1. Apelează `mcp_context7_resolve-library-id` cu numele tehnologiei
2. Apelează `mcp_context7_query-docs` cu ID-ul bibliotecii returnat și o interogare specifică

---

## Scrierea interogărilor eficiente

Fii specific — include versiunea, intenția și limbajul:

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

Include contextul:
- **Versiune** când este relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Intenția sarcinii** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Limbaj** pentru documentația poliglotă (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Declinare de responsabilitate:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să fim cât mai preciși, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa de referință. Pentru informații critice, se recomandă o traducere profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->