---
name: microsoft-docs
description: Interroga la documentazione ufficiale Microsoft per trovare concetti,
  tutorial ed esempi di codice relativi ad Azure, .NET, Agent Framework, Aspire, VS
  Code, GitHub e altro. Usa Microsoft Learn MCP come predefinito, con Context7 e Aspire
  MCP per i contenuti che si trovano al di fuori di learn.microsoft.com.
---
# Documentazione Microsoft

Competenze di ricerca per l'ecosistema tecnologico Microsoft. Copre learn.microsoft.com e la documentazione che vive al di fuori di esso (VS Code, GitHub, Aspire, repository Agent Framework).

---

## Predefinito: Microsoft Learn MCP

Usa questi strumenti per **tutto ciò che è su learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows e altro. Questo è lo strumento principale per la stragrande maggioranza delle richieste di documentazione Microsoft.

| Strumento | Scopo |
|------|---------|
| `microsoft_docs_search` | Cerca su learn.microsoft.com — concetti, guide, tutorial, configurazione |
| `microsoft_code_sample_search` | Trova snippet di codice funzionanti dalle pagine di Learn. Passa `language` (`python`, `csharp`, ecc.) per i migliori risultati |
| `microsoft_docs_fetch` | Ottieni il contenuto completo della pagina da un URL specifico (quando gli estratti della ricerca non sono sufficienti) |

Usa `microsoft_docs_fetch` dopo la ricerca quando hai bisogno di tutorial completi, di tutte le opzioni di configurazione o quando gli estratti di ricerca sono troncati.

---

## Eccezioni: Quando usare altri strumenti

Le seguenti categorie vivono **al di fuori** di learn.microsoft.com. Usa lo strumento specificato invece.

### .NET Aspire — Usa Aspire MCP Server (preferito) o Context7

La documentazione di Aspire è su **aspire.dev**, non su Learn. Il miglior strumento dipende dalla versione della tua CLI Aspire:

**CLI 13.2+** (consigliato) — L'Aspire MCP server include strumenti di ricerca della documentazione integrati:

| Strumento MCP | Descrizione |
|----------|-------------|
| `list_docs` | Elenca tutta la documentazione disponibile da aspire.dev |
| `search_docs` | Ricerca lessicale pesata attraverso il contenuto di aspire.dev |
| `get_doc` | Recupera un documento specifico per slug |

Questi sono inclusi in Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Per aggiornare: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — L'MCP server fornisce lookup delle integrazioni (`list_integrations`, `get_integration_docs`) ma **non** la ricerca nella documentazione. Ricorri a Context7:

| ID libreria | Da usare per |
|---|---|
| `/microsoft/aspire.dev` | Principale — guide, integrazioni, riferimento CLI, distribuzione |
| `/dotnet/aspire` | Sorgente runtime — internals dell'API, dettagli di implementazione |
| `/communitytoolkit/aspire` | Integrazioni della community — Go, Java, Node.js, Ollama |

### VS Code — Usa Context7

La documentazione di VS Code è su **code.visualstudio.com**, non su Learn.

| ID libreria | Da usare per |
|---|---|
| `/websites/code_visualstudio` | Documentazione utente — impostazioni, funzionalità, debugging, sviluppo remoto |
| `/websites/code_visualstudio_api` | API per estensioni — webviews, TreeViews, comandi, punti di contributo |

### GitHub — Usa Context7

La documentazione di GitHub è su **docs.github.com** e **cli.github.com**.

| ID libreria | Da usare per |
|---|---|
| `/websites/github_en` | Actions, API, repository, sicurezza, amministrazione, Copilot |
| `/websites/cli_github` | Comandi e flag del GitHub CLI (`gh`) |

### Agent Framework — Usa Learn MCP + Context7

I tutorial di Agent Framework sono su learn.microsoft.com (usa `microsoft_docs_search`), ma il **repo GitHub** contiene dettagli a livello API che spesso sono avanti rispetto alla documentazione pubblicata — in particolare il riferimento REST API di DevUI, le opzioni CLI e l'integrazione .NET.

| ID libreria | Da usare per |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorial — guide DevUI, tracing, orchestrazione dei workflow |
| `/microsoft/agent-framework` | Dettagli API — endpoint REST di DevUI, flag CLI, autenticazione, .NET `AddDevUI`/`MapDevUI` |

**Suggerimento DevUI:** Interroga la sorgente del sito Learn per le guide how-to, poi la sorgente del repository per specifiche a livello API (schemi degli endpoint, configurazione del proxy, token di autenticazione).

---

## Configurazione di Context7

Per qualsiasi query su Context7, risolvi prima l'ID libreria (una tantum per sessione):

1. Chiamare `mcp_context7_resolve-library-id` con il nome della tecnologia
2. Chiamare `mcp_context7_query-docs` con l'ID libreria restituito e una query specifica

---

## Scrivere query efficaci

Sii specifico — includi versione, intento e lingua:

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

Include il contesto:
- **Versione** quando rilevante (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Obiettivo** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Lingua** per documentazione poliglotta (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Dichiarazione di non responsabilità:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci a garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua originale deve essere considerato la fonte autorevole. Per informazioni critiche si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->