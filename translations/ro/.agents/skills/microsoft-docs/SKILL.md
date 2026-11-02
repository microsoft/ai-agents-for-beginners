---
name: microsoft-docs
---
# Microsoft Docs

Competență de cercetare pentru ecosistemul tehnologic Microsoft. Acoperă learn.microsoft.com și documentația care există în afara acestuia (VS Code, GitHub, Aspire, repo-uri Agent Framework).

---

## Implicit: Microsoft Learn MCP

Folosiți aceste instrumente pentru **tot ce este pe learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows și altele. Acesta este instrumentul principal pentru majoritatea interogărilor privind documentația Microsoft.

| Instrument | Scop |
|------|---------|
| `microsoft_docs_search` | Căutare pe learn.microsoft.com — concepte, ghiduri, tutoriale, configurare |
| `microsoft_code_sample_search` | Găsește fragmente de cod funcționale din documentația Learn. Transmite `language` (`python`, `csharp`, etc.) pentru cele mai bune rezultate |
| `microsoft_docs_fetch` | Obține conținutul complet al paginii de la un URL specific (când fragmentele de căutare nu sunt suficiente) |

Utilizează `microsoft_docs_fetch` după căutare când ai nevoie de tutoriale complete, toate opțiunile de configurare sau când fragmentele de căutare sunt trunchiate.

---

## Excepții: Când să folosești alte instrumente

Următoarele categorii există **în afara** learn.microsoft.com. Utilizează instrumentul specificat în schimb.

### Aspire — Folosește Aspire MCP Server (preferat) sau Context7

Documentația Aspire se găsește pe **aspire.dev**, nu pe Learn. Cel mai bun instrument depinde de versiunea Aspire CLI pe care o ai:

**CLI 13.2+** (recomandat) — Serverul Aspire MCP include instrumente integrate de căutare în documentație:

| Instrument MCP | Descriere |
|----------|-------------|
| `list_docs` | Listează toată documentația disponibilă de pe aspire.dev |
| `search_docs` | Căutare lexical ponderată în conținutul aspire.dev |
| `get_doc` | Recuperează un document specific prin slug |

Acestea sunt incluse în Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Pentru actualizare: `aspire update --self --channel daily`.

**CLI 13.1** — Serverul MCP oferă căutare în integrare (`list_integrations`, `get_integration_docs`) dar **nu** căutare în documentație. Folosește fallback pe Context7:

| ID bibliotecă | Utilizare pentru |
|---|---|
| `/microsoft/aspire.dev` | Primar — ghiduri, integrări, referință CLI, implementare |
| `/microsoft/aspire` | Surse runtime — API intern, detalii implementare |
| `/communitytoolkit/aspire` | Integrări comunitare — Go, Java, Node.js, Ollama |

### VS Code — Folosește Context7

Documentația VS Code se găsește pe **code.visualstudio.com**, nu pe Learn.

| ID bibliotecă | Utilizare pentru |
|---|---|
| `/websites/code_visualstudio` | Documentație utilizator — setări, funcționalități, debugging, dezvoltare remote |
| `/websites/code_visualstudio_api` | API Extensie — webviews, TreeViews, comenzi, puncte de contribuție |

### GitHub — Folosește Context7

Documentația GitHub este pe **docs.github.com** și **cli.github.com**.

| ID bibliotecă | Utilizare pentru |
|---|---|
| `/websites/github_en` | Actions, API, repo-uri, securitate, administrare, Copilot |
| `/websites/cli_github` | Comenzi și opțiuni GitHub CLI (`gh`) |

### Agent Framework — Folosește Learn MCP + Context7

Tutorialele Agent Framework sunt pe learn.microsoft.com (folosește `microsoft_docs_search`), dar **repo-ul GitHub** conține detalii nivel API care de multe ori sunt mai noi decât documentația publicată — în special referințe DevUI REST API, opțiuni CLI și integrare .NET.

| ID bibliotecă | Utilizare pentru |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutoriale — ghiduri DevUI, tracing, orchestrare fluxuri de lucru |
| `/microsoft/agent-framework` | Detalii API — endpoint-uri DevUI REST, flag-uri CLI, autentificare, .NET `AddDevUI`/`MapDevUI` |

**Sfat DevUI:** Consultă sursa site-ului Learn pentru ghiduri cum să faci, apoi sursa repo-ului pentru detalii la nivel API (scheme endpoint, configurare proxy, token-uri de autentificare).

---

## Configurare Context7

Pentru orice interogare Context7, stabilește mai întâi ID-ul bibliotecii (o singură dată pe sesiune):

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

Include context:
- **Versiune** când este relevantă (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Intenția sarcinii** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Limbaj** pentru documentație poliglot (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->