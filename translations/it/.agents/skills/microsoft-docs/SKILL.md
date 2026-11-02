---
name: microsoft-docs
description: Interroga la documentazione ufficiale di Microsoft per trovare concetti,
  tutorial ed esempi di codice su Azure, .NET, Agent Framework, Aspire, VS Code, GitHub
  e altro. Utilizza Microsoft Learn MCP come predefinito, con Context7 e Aspire MCP
  per contenuti che si trovano al di fuori di learn.microsoft.com.
---
# Microsoft Docs

Capacità di ricerca per l'ecosistema tecnologico Microsoft. Copre learn.microsoft.com e la documentazione che si trova al di fuori di esso (VS Code, GitHub, Aspire, repository Agent Framework).

---

## Predefinito: Microsoft Learn MCP

Usa questi strumenti per **tutto su learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows e altro. Questo è lo strumento principale per la stragrande maggioranza delle query sulla documentazione Microsoft.

| Strumento | Scopo |
|------|---------|
| `microsoft_docs_search` | Cerca in learn.microsoft.com — concetti, guide, tutorial, configurazione |
| `microsoft_code_sample_search` | Trova snippet di codice funzionanti dalla documentazione Learn. Passa `language` (`python`, `csharp`, ecc.) per migliori risultati |
| `microsoft_docs_fetch` | Ottieni il contenuto completo della pagina da un URL specifico (quando gli estratti di ricerca non sono sufficienti) |

Usa `microsoft_docs_fetch` dopo la ricerca quando ti servono tutorial completi, tutte le opzioni di configurazione, o quando gli estratti di ricerca sono troncati.

---

## Eccezioni: Quando usare altri strumenti

Le seguenti categorie vivono **al di fuori** di learn.microsoft.com. Usa lo strumento specificato invece.

### Aspire — Usa Aspire MCP Server (preferito) o Context7

La documentazione Aspire si trova su **aspire.dev**, non su Learn. Il miglior strumento dipende dalla tua versione dell' Aspire CLI:

**CLI 13.2+** (consigliato) — Il server Aspire MCP include strumenti di ricerca documenti integrati:

| Strumento MCP | Descrizione |
|----------|-------------|
| `list_docs` | Elenca tutta la documentazione disponibile da aspire.dev |
| `search_docs` | Ricerca lessicale pesata tra i contenuti di aspire.dev |
| `get_doc` | Recupera un documento specifico tramite slug |

Questi sono inclusi in Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Per aggiornare: `aspire update --self --channel daily`.

**CLI 13.1** — Il server MCP fornisce lookup integrazione (`list_integrations`, `get_integration_docs`) ma **non** ricerca documenti. Usa invece Context7:

| ID Libreria | Da usare per |
|---|---|
| `/microsoft/aspire.dev` | Principale — guide, integrazioni, riferimento CLI, deployment |
| `/microsoft/aspire` | Sorgente runtime — internals API, dettagli implementazione |
| `/communitytoolkit/aspire` | Integrazioni comunitarie — Go, Java, Node.js, Ollama |

### VS Code — Usa Context7

La documentazione di VS Code si trova su **code.visualstudio.com**, non su Learn.

| ID Libreria | Da usare per |
|---|---|
| `/websites/code_visualstudio` | Documentazione utente — impostazioni, funzionalità, debug, sviluppo remoto |
| `/websites/code_visualstudio_api` | API estensioni — webviews, TreeViews, comandi, punti di contribuzione |

### GitHub — Usa Context7

La documentazione GitHub si trova su **docs.github.com** e **cli.github.com**.

| ID Libreria | Da usare per |
|---|---|
| `/websites/github_en` | Azioni, API, repository, sicurezza, amministrazione, Copilot |
| `/websites/cli_github` | Comandi e flag GitHub CLI (`gh`) |

### Agent Framework — Usa Learn MCP + Context7

I tutorial di Agent Framework sono su learn.microsoft.com (usa `microsoft_docs_search`), ma il **repository GitHub** contiene dettagli a livello API spesso più aggiornati rispetto alla documentazione pubblicata — in particolare riferimento REST API DevUI, opzioni CLI e integrazione .NET.

| ID Libreria | Da usare per |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorial — guide DevUI, tracciamento, orchestrazione workflow |
| `/microsoft/agent-framework` | Dettagli API — endpoint REST DevUI, flag CLI, autenticazione, .NET `AddDevUI`/`MapDevUI` |

**Suggerimento DevUI:** Interroga la fonte del sito Learn per guide pratiche, poi la fonte del repo per dettagli a livello API (schemi endpoint, configurazione proxy, token autenticazione).

---

## Configurazione Context7

Per qualsiasi query Context7, risolvi prima l'ID libreria (una volta per sessione):

1. Chiama `mcp_context7_resolve-library-id` con il nome della tecnologia
2. Chiama `mcp_context7_query-docs` con l'ID libreria restituito e una query specifica

---

## Scrivere query efficaci

Sii specifico — includi versione, intento e linguaggio:

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

Includi il contesto:
- **Versione** quando rilevante (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Intento del compito** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Linguaggio** per documentazione poliglotta (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->