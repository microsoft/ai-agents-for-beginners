---
name: microsoft-docs
description: Pretražuje službenu Microsoftovu dokumentaciju kako bi pronašao koncepte,
  vodiče i primjere koda za Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  i još mnogo toga. Koristi Microsoft Learn MCP kao zadano, te Context7 i Aspire MCP
  za sadržaj koji se nalazi izvan learn.microsoft.com.
---
# Microsoft Docs

Istraživačka vještina za Microsoft tehnološki ekosustav. Obuhvaća learn.microsoft.com i dokumentaciju koja živi izvan njega (VS Code, GitHub, Aspire, Agent Framework repozitoriji).

---

## Zadano: Microsoft Learn MCP

Koristite ove alate za **sve na learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows i više. Ovo je primarni alat za velik većinu upita vezanih uz Microsoft dokumentaciju.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Pretraživanje learn.microsoft.com — koncepti, vodiči, tutorijali, konfiguracija |
| `microsoft_code_sample_search` | Pronađite radne isječke koda iz Learn dokumenata. Proslijedite `language` (`python`, `csharp`, itd.) za najbolje rezultate |
| `microsoft_docs_fetch` | Dohvati cjelokupan sadržaj stranice s određenog URL-a (kad isječci iz pretrage nisu dovoljni) |

Koristite `microsoft_docs_fetch` nakon pretrage kada trebate kompletne tutorijale, sve opcije konfiguracije ili kada su isječci iz pretrage skraćeni.

---

## Izuzeci: Kada koristiti druge alate

Sljedeće kategorije žive **izvan** learn.microsoft.com. Umjesto toga koristite navedeni alat.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire dokumentacija se nalazi na **aspire.dev**, a ne na Learnu. Najbolji alat ovisi o verziji vašeg Aspire CLI-ja:

**CLI 13.2+** (preporučeno) — Aspire MCP server uključuje ugrađene alate za pretraživanje dokumenata:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Navodi svu dostupnu dokumentaciju s aspire.dev |
| `search_docs` | Težinska leksikalna pretraga kroz sadržaj aspire.dev |
| `get_doc` | Dohvaća određeni dokument po slugu |

Ovo dolazi u Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Za ažuriranje: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP server pruža integracijski lookup (`list_integrations`, `get_integration_docs`) ali **ne** pretraživanje dokumenata. Vratite se na Context7:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Primarno — vodiči, integracije, referenca CLI-ja, deployment |
| `/dotnet/aspire` | Izvor runtime-a — API internals, detalji implementacije |
| `/communitytoolkit/aspire` | Community integracije — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code dokumentacija živi na **code.visualstudio.com**, a ne na Learnu.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Korisnička dokumentacija — postavke, značajke, debuggiranje, remote dev |
| `/websites/code_visualstudio_api` | Extension API — webviews, TreeViews, naredbe, contributin pointi |

### GitHub — Use Context7

GitHub dokumentacija živi na **docs.github.com** i **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repozitoriji, sigurnost, administracija, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) naredbe i zastavice |

### Agent Framework — Use Learn MCP + Context7

Agent Framework tutorijali su na learn.microsoft.com (koristite `microsoft_docs_search`), ali **GitHub repo** sadrži detalje na razini API-ja koji su često ispred objavljene dokumentacije — osobito DevUI REST API referenca, CLI opcije i .NET integracija.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorijali — DevUI vodiči, praćenje (tracing), orkestracija workflowa |
| `/microsoft/agent-framework` | Detalji API-ja — DevUI REST endpointi, CLI zastavice, auth, .NET `AddDevUI`/`MapDevUI` |

**DevUI savjet:** Upitavajte izvor Learn web-mjesta za how-to vodiče, zatim izvor repozitorija za specifikacije na razini API-ja (sheme endpointa, proxy konfiguracija, auth tokeni).

---

## Postavljanje Context7

Za bilo koji Context7 upit, najprije razriješite library ID (jednokratno po sesiji):

1. Pozovite `mcp_context7_resolve-library-id` s nazivom tehnologije
2. Pozovite `mcp_context7_query-docs` s vraćenim library ID-om i konkretnim upitom

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

Include context:
- **Version** when relevant (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Task intent** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Language** for polyglot docs (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Odricanje odgovornosti:
Ovaj je dokument preveden pomoću AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->