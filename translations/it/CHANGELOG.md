# Changelog

Tutte le modifiche importanti al corso **AI Agents for Beginners** sono documentate in questo file.

## [Rilasciato] — 2026-07-14

Questa versione sposta il corso da due modelli appena deprecati, migra i notebook delle lezioni rimanenti all'API stabile di Microsoft Agent Framework e valida i notebook Python contro un'installazione Microsoft Foundry attiva.

### Modificato

- **Passaggio dai modelli deprecati (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** `gpt-4.1` e `gpt-4.1-mini` sono ora deprecati (data di ritiro pubblicata **14 ottobre 2026**). Sostituiti tutti i riferimenti nel corso (documentazione, `.env.example`, notebook e esempi Python/.NET) con il modello non deprecato `gpt-5-mini`. L'esempio di instradamento del modello della Lezione 16 mantiene un contrasto piccolo/grande usando `gpt-5-nano` (piccolo) e `gpt-5-mini` (grande). I file di terze parti forniti ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), il testo storico dei Modelli GitHub e le note di capacità della skill `azure-openai-to-responses` sono stati lasciati intenzionalmente invariati.
- **Notebook handoff della Lezione 14 migrato alla API stabile.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) ora usa `agent_framework.orchestrations.HandoffBuilder` con `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, streaming basato su `event.type` e `FoundryChatClient` (sostituendo i simboli rimossi pre-1.0 `HandoffBuilder` / `ChatMessage` / `RequestInfoEvent`).
- **Notebook human-in-the-loop della Lezione 14 migrato alla API stabile.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) ora mette in pausa tramite `ctx.request_info(...)` + `@response_handler` (sostituendo `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` rimossi), costruisce con `WorkflowBuilder(start_executor=..., output_executors=[...])`, gestisce l'output strutturato tramite `default_options={"response_format": ...}`, e utilizza una risposta scriptata in modo che il notebook possa essere eseguito senza supervisione (nessun blocco da `input()`).
- **Configurazione dell'ambiente** ([.env.example](../../.env.example)): cambiati i nomi delle distribuzioni dei modelli in `gpt-5-mini`; aggiunti `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (instradamento Lezione 16) e il precedentemente mancante `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (uso browser Lezione 15).
- **Dipendenze** ([requirements.txt](../../requirements.txt)): fissate le versioni di `agent-framework`, `agent-framework-foundry` e `agent-framework-openai` a `~=1.10.0` per un set coerente e validato (la 1.11.0 introduce cambiamenti sperimentali incompatibili sulle superfici usate da queste lezioni).

### Note e limitazioni note

- **Validato contro Microsoft Foundry attivo.** I notebook Python sono stati eseguiti senza interfaccia grafica con `nbconvert` contro un progetto Microsoft Foundry usando `gpt-5-mini` (e `gpt-5-nano` per l'instradamento della Lezione 16). Distribuite modelli equivalenti non deprecati nel vostro progetto; i notebook leggono il nome della distribuzione da `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Richiede ancora risorse extra per alcune lezioni.** La Lezione 05 necessita di Azure AI Search; il workflow di grounding Bing della Lezione 08 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) necessita di una connessione Bing e degli strumenti ospitati Microsoft Foundry Agent Service; Lezioni 13 (Cognee) e 17 (Foundry Local) necessitano dei propri runtime.

## [Rilasciato] — 2026-07-13

Questa versione aggiunge due nuove lezioni che completano l'arco del deployment — scalando gli agenti fino a Microsoft Foundry e riducendoli a un singolo workstation — oltre a una pipeline di smoke-test, navigazione del corso aggiornata, nuove competenze per gli studenti e branding aggiornato.

### Aggiunto

- **Lezione 16 — Deployment di agenti scalabili con Microsoft Foundry.** Nuova lezione [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) e notebook eseguibile [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) che costruisce un agente di supporto clienti di produzione (strumenti, RAG, memoria, instradamento modello, caching delle risposte, approvazione umana, gate di valutazione e tracciamento OpenTelemetry), con diagrammi Mermaid per sviluppo/deploy/runtime, un controllo di conoscenza, un compito e una sfida.
- **Lezione 17 — Creazione di agenti AI locali con Foundry Local e Qwen.** Nuova lezione [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) e notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) che costruisce un assistente ingegneristico completamente on-device (chiamate di funzione Qwen tramite Foundry Local, strumenti file sandboxati, RAG locale con Chroma, MCP locale opzionale), con diagrammi solo locale / RAG locale / chiamata a strumenti, controllo di conoscenza, compito e sfida.
- **Pipeline di smoke-test.** Nuovo workflow [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) più cataloghi per ogni lezione sotto [tests/](./tests/README.md) per gli agenti deployabili nelle Lezioni 01, 04, 05 e 16, con README indice che mappa ogni catalogo alla rispettiva lezione e nome agente ospitato. La Lezione 16 aggiunge una sezione "Validazione di un agente deployato con Smoke Tests"; Lezioni 01/04/05 aggiungono un puntatore opzionale allo smoke-test.
- **Competenze per gli studenti.** Nuove Agent Skills sotto `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (che raggruppano le guide delle Lezioni 16 e 17), e [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (come validare gli esempi del notebook contro un setup Microsoft Foundry / Azure OpenAI attivo).
- **Runner per validazione dei notebook.** Nuovo [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) che esegue ogni notebook Python senza interfaccia con `nbconvert` e stampa una matrice PASS/FAIL (più `results.json`). Rileva automaticamente la radice del repository e Python, esclude i notebook non di corso ( `.venv`, `site-packages`, `translations`, asset modello skill) e notebook `.NET` di default, supporta `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` e `-Python`.
- **Navigazione del corso.** Aggiunti link alle lezioni Precedente/Successiva alle Lezioni 11–15 (prima mancanti) così che tutto il corso sia concatenato da 00 a 18 in entrambe le direzioni.
- **Nuove miniature.** Miniature per le Lezioni 16 e 17, più un'immagine social di repository rinfrescata [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (ora pubblicizza le due nuove lezioni e l'URL `aka.ms/ai-agents-beginners`).
- **Dipendenze** ([requirements.txt](../../requirements.txt)): aggiunti `foundry-local-sdk` e `chromadb` per la Lezione 17.

### Modificato

- **Tabella principale delle lezioni in [README.md](./README.md)**: Lezioni 16 e 17 ora linkano al loro contenuto (prima era "Coming Soon"); immagine del repository aggiornata a `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: aggiunte Lezioni 16 e 17 alla guida lezione per lezione e ai percorsi di apprendimento, più una sezione "Validazione degli agenti deployati con Smoke Tests".
- **[AGENTS.md](./AGENTS.md)**: aggiornato il conteggio/descrizione delle lezioni (00–18), aggiunta sezione di validazione smoke-testing e esempi di denominazione per Lezioni 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Lezione precedente" ora punta alla Lezione 17 (prima Lezione 15), chiudendo la catena.
- **Riferimenti ai modelli standardizzati su modelli non deprecati.** Sostituiti tutti i riferimenti `gpt-4o` / `gpt-4o-mini` in tutto il corso (documenti, `.env.example`, notebook e esempi Python/.NET) con `gpt-4.1-mini` — `gpt-4o` (tutte le versioni) verrà ritirato nel 2026. L'esempio di instradamento del modello della Lezione 16 mantiene un contrasto piccolo/grande usando `gpt-4.1-mini` (piccolo) e `gpt-4.1` (grande). I notebook Python selezionano ora il modello tramite variabili ambiente (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) anziché hardcodare un nome modello.

### Note e limitazioni note

- **Non eseguiti contro Azure attivo.** I notebook delle nuove lezioni sono esempi educativi; eseguiteli e validateli contro la vostra installazione Microsoft Foundry / Foundry Local. Il workflow smoke-test richiede il deployment dell'agente della lezione e la configurazione dei segreti Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) con il ruolo **Azure AI User** a livello di progetto Foundry.
- **La Lezione 17 è solo locale.** Non dispone di endpoint Foundry Responses, quindi l’azione di smoke-test non si applica; validatela eseguendo il notebook sulla vostra workstation.

## [Rilasciato] — 2026-07-06

Questa versione migra il corso all'**Azure OpenAI Responses API**, standardizza i nomi di prodotto su **Microsoft Foundry** e **Microsoft Agent Framework (MAF)**, ritira GitHub Models, aggiorna le versioni SDK e aggiunge nuovo contenuto su modelli locali e hosting di altri framework su Foundry.

### Aggiunto

- **Skill di migrazione** — Installata la Agent Skill [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (da [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) sotto `.agents/skills/`, inclusi i riferimenti e lo script scanner.
- **Foundry Local (esegui modelli on-device)** — Nuova sezione "Fornitore alternativo: Foundry Local" in [00-course-setup/README.md](./00-course-setup/README.md) che tratta installazione (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` e collegamento di `FoundryLocalManager` a Microsoft Agent Framework tramite `OpenAIChatClient`.
- **Hosting degli agenti LangChain / LangGraph su Microsoft Foundry** — Nuova sezione in [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) più esempio eseguibile [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) che usa `langchain-azure-ai[hosting]` e `ResponsesHostServer` (protocollo `/responses`), basato su [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — Nuova sezione "Esempio reale: Microsoft Project Opal" in [15-browser-use/README.md](./15-browser-use/README.md) che inquadra Opal come agente d'uso aziendale del computer e lo mappa ai concetti del corso (umano nel loop, fiducia/sicurezza, pianificazione, Skills).
- **Secondo esempio Python per la Lezione 02** — Aggiunto [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (vedi "Modificato" — migrato dal notebook Semantic Kernel precedente) e collegato nel README della lezione.
- **Aggiunta sezione Modelli e Fornitori** a [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Modificato

- **Chat Completions → Responses API (Python).** Gli esempi che chiamavano il modello direttamente sono stati migrati da Chat Completions a Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), usando il client `OpenAI` all'endpoint stabile Azure OpenAI `/openai/v1/` (senza `api_version`). Gli esempi interessati includono:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — walkthrough completo delle chiamate a funzione (schema degli strumenti appiattito al formato Responses, risultati degli strumenti restituiti come `function_call_output`, `max_output_tokens`, ecc.).

- **Modelli GitHub → Azure OpenAI.** I modelli GitHub sono deprecati (in pensionamento **luglio 2026**) e non supportano l'API delle Risposte. Tutti i percorsi di codice dei modelli GitHub sono stati convertiti in Azure OpenAI / Microsoft Foundry negli esempi Python e .NET:
  - Python: workflow notebook della Lezione 08 (`01`–`03`), Lezione 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + documentazione `.md` correlata, e i notebook/workflow `.md` dotNET della Lezione 08 (`01`–`03`) ora usano `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` con `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Il precedente `02-semantic-kernel.ipynb` è stato riscritto per usare Microsoft Agent Framework con Azure OpenAI (API Risposte) e rinominato in `02-python-agent-framework-azure-openai.ipynb`.
- **Standardizzazione su `FoundryChatClient` + `as_agent`.** Il README e i codici notebook che facevano riferimento a `AzureAIProjectAgentProvider` sono stati standardizzati sul pattern canonico usato dalla Lezione 01 e dagli esempi del framework: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` con `provider.as_agent(...)`. Aggiornato in tutti i README e notebook di Lezioni 02–14 (es. memoria Lezione 13, tutti i notebook Lezione 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Nomenclatura prodotto.** Rinominato nel contenuto in inglese:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Invariato: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", e nomi delle variabili d'ambiente.)
- **Dipendenze** ([requirements.txt](../../requirements.txt)):
  - Bloccate versioni `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Bloccata versione `openai>=1.108.1` (minima per l'API Risposte).
  - Rimosso `azure-ai-inference` (usato solo negli esempi migrati dei modelli GitHub).
- **Configurazione ambiente** ([.env.example](../../.env.example)): rimosse variabili dei modelli GitHub (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); aggiunte `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` e opzionale `AZURE_OPENAI_API_KEY`; aggiornata nomenclatura a Microsoft Foundry.
- **Documentazione** — Aggiornati [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md) e [STUDY_GUIDE.md](./STUDY_GUIDE.md) per quanto sopra (variabili ambiente setup, snippet di verifica, guida provider, nomenclatura).

### Rimossi

- Passaggi di onboarding dei modelli GitHub e variabili ambiente dai documenti di setup (sostituiti da Azure OpenAI / Microsoft Foundry).

### Sicurezza / Privacy (pulizia dati pubblici)

- Cancellati output di esecuzione Jupyter notebook che mostravano un reale **ID sottoscrizione Azure**, nomi di resource-group/risorse e ID connessione Bing, più **percorsi file locali e nomi utenti** degli sviluppatori, in:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Verificato che non rimangono chiavi API, token, ID sottoscrizione o percorsi personali nei contenuti inglesi tracciati (i riferimenti a `GITHUB_TOKEN` che restano sono il token GitHub Actions nei workflow e il PAT server GitHub MCP nella configurazione della Lezione 11 — entrambi legittimi e non collegati ai modelli GitHub).

### Note e limitazioni conosciute

- **Non eseguiti/compilati.** Questi sono esempi didattici aggiornati per correttezza API/nomenclatura; non sono stati eseguiti contro risorse Azure live, e gli esempi .NET non sono stati compilati in questo ambiente. Verificare con la propria distribuzione Microsoft Foundry / Azure OpenAI.
- **Il deployment del modello deve supportare l'API Risposte.** Usare un deployment come `gpt-4.1-mini`, `gpt-4.1` o un modello `gpt-5.x`. I modelli più vecchi supportano le funzionalità principali delle Risposte ma non tutte le caratteristiche.
- **Versione agent-framework.** Gli esempi puntano all'ultima MAF (`>=1.10.0`). La chiamata canonica per creare un agente è `client.as_agent(...)`; le API sono state validate con la documentazione ufficiale e una build installata. Se si usa una versione differente, confermare la disponibilità del metodo (`as_agent` vs `create_agent`).
- **Notebook workflow Lezione 08 04** mantiene intenzionalmente `AzureAIAgentClient` (da `agent-framework-azure-ai`) perché utilizza strumenti ospitati Microsoft Foundry Agent Service (grounding Bing, interprete codice); è già basato su Risposte.
- **Deployment di default .NET.** Due esempi workflow dotNET della Lezione 08 in precedenza codificavano un modello specifico; ora usano di default `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). Se un esempio usa input multimodale/vision, impostare `AZURE_OPENAI_DEPLOYMENT` su un modello adeguato.
- **Foundry Local** espone un endpoint **Chat Completions** compatibile OpenAI ed è pensato per sviluppo locale; usare Azure OpenAI / Microsoft Foundry per l'intero set di funzionalità API Risposte.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->