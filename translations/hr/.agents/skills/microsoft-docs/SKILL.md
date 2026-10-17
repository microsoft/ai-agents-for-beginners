---
name: microsoft-docs
description: Pretražujte službenu Microsoftovu dokumentaciju kako biste pronašli koncepte,
  vodiče i primjere koda za Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  i druge. Koristi Microsoft Learn MCP kao zadano, s Context7 i Aspire MCP za sadržaj
  koji se nalazi izvan learn.microsoft.com.
---
# Microsoft Docs

Vještina istraživanja za Microsoft tehnologijski ekosustav. Obuhvaća learn.microsoft.com i dokumentaciju koja se nalazi izvan njega (VS Code, GitHub, Aspire, Agent Framework spremišta).

---

## Zadano: Microsoft Learn MCP

Koristite ove alate za **sve na learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows i više. Ovo je glavni alat za veliki dio upita o Microsoft dokumentaciji.

| Alat | Svrha |
|------|---------|
| `microsoft_docs_search` | Pretražujte learn.microsoft.com — pojmove, vodiče, tutorijale, konfiguraciju |
| `microsoft_code_sample_search` | Pronađite radne isječke koda iz Learn dokumenata. Proslijedite `language` (`python`, `csharp` itd.) za najbolje rezultate |
| `microsoft_docs_fetch` | Dohvatite puni sadržaj stranice s određenog URL-a (kada isječci pretraživanja nisu dovoljni) |

Koristite `microsoft_docs_fetch` nakon pretraživanja kada trebate potpune tutorijale, sve opcije konfiguracije ili kada su isječci pretraživanja skraćeni.

---

## Izuzeci: Kada koristiti druge alate

Sljedeće kategorije nalaze se **izvan** learn.microsoft.com. Umjesto toga koristite navedeni alat.

### Aspire — Koristite Aspire MCP Server (preporučeno) ili Context7

Aspire dokumentacija je na **aspire.dev**, ne na Learnu. Najbolji alat ovisi o vašoj Aspire CLI verziji:

**CLI 13.2+** (preporučeno) — Aspire MCP server uključuje ugrađene alate za pretraživanje dokumenata:

| MCP Alat | Opis |
|----------|-------------|
| `list_docs` | Prikazuje svu dostupnu dokumentaciju s aspire.dev |
| `search_docs` | Vagano leksičko pretraživanje sadržaja aspire.dev |
| `get_doc` | Dohvaća određeni dokument prema slug-u |

Ove funkcije dolaze u Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Za ažuriranje: `aspire update --self --channel daily`.

**CLI 13.1** — MCP server pruža integracijski prikaz (`list_integrations`, `get_integration_docs`) ali **ne** pretraživanje dokumenata. Povratak na Context7:

| ID knjižnice | Koristi za |
|---|---|
| `/microsoft/aspire.dev` | Primarno — vodiči, integracije, CLI referenca, implementacija |
| `/microsoft/aspire` | Izvor za vrijeme izvođenja — detalji interne API, implementacije |
| `/communitytoolkit/aspire` | Integracije zajednice — Go, Java, Node.js, Ollama |

### VS Code — Koristite Context7

VS Code dokumentacija je na **code.visualstudio.com**, ne na Learnu.

| ID knjižnice | Koristi za |
|---|---|
| `/websites/code_visualstudio` | Korisnička dokumentacija — postavke, značajke, otklanjanje pogrešaka, udaljeni razvoj |
| `/websites/code_visualstudio_api` | API za proširenja — webviewovi, TreeViewovi, naredbe, točke doprinosa |

### GitHub — Koristite Context7

GitHub dokumentacija je na **docs.github.com** i **cli.github.com**.

| ID knjižnice | Koristi za |
|---|---|
| `/websites/github_en` | Actions, API, spremišta, sigurnost, administracija, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) naredbe i zastavice |

### Agent Framework — Koristite Learn MCP + Context7

Agent Framework tutorijali su na learn.microsoft.com (koristite `microsoft_docs_search`), ali **GitHub repozitorij** ima detalje razine API-ja koji su često ispred objavljene dokumentacije — posebno DevUI REST API referenca, CLI opcije i .NET integracija.

| ID knjižnice | Koristi za |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorijali — DevUI vodiči, praćenje, orkestracija radnih tokova |
| `/microsoft/agent-framework` | Detalji API-ja — DevUI REST krajnje točke, CLI zastavice, autentikacija, .NET `AddDevUI`/`MapDevUI` |

**Savjet za DevUI:** Prvo upitajte Learn internetsku stranicu za vodiče, zatim repozitorij za specifikacije razine API-ja (sheme krajnjih točaka, proxy konfiguracija, autorizacijski tokeni).

---

## Postavljanje Context7

Za svaki upit Context7, prvo razriješite ID knjižnice (jednokratan po sesiji):

1. Pozovite `mcp_context7_resolve-library-id` s nazivom tehnologije
2. Pozovite `mcp_context7_query-docs` s vraćenim ID knjižnice i određenim upitom

---

## Pisanje učinkovitih upita

Budite specifični — uključite verziju, namjeru i jezik:

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

Uključite kontekst:
- **Verziju** kada je relevantno (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Namjeru zadatka** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Jezik** za poliglotsku dokumentaciju (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->