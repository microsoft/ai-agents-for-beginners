# AGENTS.md

## Panoramica del Progetto

Questo repository contiene "Agenti AI per Principianti" - un corso educativo completo che insegna tutto il necessario per costruire Agenti AI. Il corso consiste in 18 lezioni (numerate da 00 a 18) che coprono i fondamenti, i pattern di progettazione, i framework, il deployment in produzione, agenti locali/su dispositivo e la sicurezza degli agenti AI.

**Tecnologie Chiave:**
- Python 3.12+
- Jupyter Notebooks per l'apprendimento interattivo
- Framework AI: Microsoft Agent Framework (MAF)
- Servizi AI di Azure: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architettura:**
- Struttura basata su lezioni (cartelle 00-15+)
- Ogni lezione contiene: documentazione README, esempi di codice (Jupyter notebooks) e immagini
- Supporto multilingue tramite sistema di traduzione automatica
- Un notebook Python per lezione che usa Microsoft Agent Framework

## Comandi di Configurazione

### Prerequisiti
- Python 3.12 o superiore
- Abbonamento Azure (per Microsoft Foundry)
- Azure CLI installata e autenticata (`az login`)

### Configurazione Iniziale

1. **Clona o crea fork del repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # O
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Crea e attiva l'ambiente virtuale Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Su Windows: venv\Scripts\activate
   ```

3. **Installa le dipendenze:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura le variabili d'ambiente:**
   ```bash
   cp .env.example .env
   # Modifica .env con le tue chiavi API e endpoint
   ```

### Variabili d'Ambiente Richieste

Per **Microsoft Foundry** (Obbligatorio):
- `AZURE_AI_PROJECT_ENDPOINT` - Endpoint del progetto Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Nome del deployment del modello (es. gpt-5-mini)

Per **Azure AI Search** (Lezione 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Endpoint di Azure AI Search
- `AZURE_SEARCH_API_KEY` - Chiave API di Azure AI Search

Autenticazione: Esegui `az login` prima di eseguire i notebook (usa `AzureCliCredential`).

## Flusso di Lavoro per lo Sviluppo

### Esecuzione di Jupyter Notebooks

Ogni lezione contiene più Jupyter notebooks per diversi framework:

1. **Avvia Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviga nella cartella della lezione** (es. `01-intro-to-ai-agents/code_samples/`)

3. **Apri ed esegui i notebook:**
   - `*-python-agent-framework.ipynb` - Usando Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando Microsoft Agent Framework (.NET)

### Lavorare con Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Richiede abbonamento Azure
- Usa `FoundryChatClient` per Agent Service V2 (agenti visibili nel portale Foundry)
- Pronto per la produzione con osservabilità integrata
- Pattern di file: `*-python-agent-framework.ipynb`

## Istruzioni per il Testing

Questo è un repository educativo con codice esempio e non codice di produzione con test automatizzati. Per verificare la tua configurazione e le modifiche:

### Testing Manuale

1. **Test dell'ambiente Python:**
   ```bash
   python --version  # Dovrebbe essere 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test di esecuzione del notebook:**
   ```bash
   # Converti il notebook in script ed esegui (importa i test)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifica delle variabili d'ambiente:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Esecuzione di Singoli Notebook

Apri i notebook in Jupyter ed esegui le celle sequenzialmente. Ogni notebook è autonomo e include:
- Istruzioni di importazione
- Caricamento della configurazione
- Esempi di implementazioni di agenti
- Output attesi nelle celle markdown

### Smoke-Testing degli Agenti Distribuiti

Per le lezioni dove un agente è distribuito come agente ospitato Microsoft Foundry (01, 04, 05, 16), il repo include cataloghi di smoke-test nella cartella `tests/` che vengono eseguiti dal workflow `.github/workflows/smoke-test.yml` tramite l'azione [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Questi sono una verifica leggera post-distribuzione (l'agente è raggiungibile e segue le aspettative di prompt di base?), che completano la pipeline di valutazione delle Lezioni 10 e 16. Vedi [tests/README.md](./tests/README.md) per la mappatura catalogo-lezione-agente. La Lezione 17 viene eseguita localmente con Foundry Local e non ha endpoint ospitato, quindi è validata eseguendo direttamente il suo notebook.

## Stile del Codice

### Convenzioni Python

- **Versione Python**: 3.12+
- **Stile del codice**: Seguire le convenzioni standard PEP 8 di Python
- **Notebook**: Usare celle markdown chiare per spiegare i concetti
- **Importazioni**: Raggruppare per librerie standard, terze parti e locali

### Convenzioni per Jupyter Notebook

- Includere celle markdown descrittive prima delle celle di codice
- Aggiungere esempi di output nei notebook come riferimento
- Usare nomi di variabili chiari che corrispondano ai concetti della lezione
- Mantenere l'ordine di esecuzione del notebook lineare (cella 1 → 2 → 3...)

### Organizzazione dei File

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Build e Distribuzione

### Generazione della Documentazione

Questo repository utilizza Markdown per la documentazione:
- File README.md in ogni cartella di lezione
- README.md principale nella root del repository
- Sistema di traduzione automatica tramite GitHub Actions

### Pipeline CI/CD

Situata in `.github/workflows/`:

1. **co-op-translator.yml** - Traduzione automatica in oltre 50 lingue
2. **welcome-issue.yml** - Benvenuto ai creatori di nuove issue
3. **welcome-pr.yml** - Benvenuto ai nuovi contributori di pull request

### Distribuzione

Questo è un repository educativo - nessun processo di distribuzione. Gli utenti:
1. Creano un fork o clonano il repository
2. Eseguono i notebook localmente o in GitHub Codespaces
3. Imparano modificando e sperimentando con gli esempi

## Linee Guida per le Pull Request

### Prima di Inviare

1. **Testa le tue modifiche:**
   - Esegui interamente i notebook interessati
   - Verifica che tutte le celle si eseguano senza errori
   - Controlla che gli output siano appropriati

2. **Aggiornamenti della documentazione:**
   - Aggiorna README.md se aggiungi nuovi concetti
   - Aggiungi commenti nei notebook per codice complesso
   - Assicurati che le celle markdown spieghino lo scopo

3. **Modifiche ai file:**
   - Evita di commitare file `.env` (usa `.env.example`)
   - Non commitare cartelle `venv/` o `__pycache__/`
   - Mantieni gli output dei notebook quando dimostrano concetti
   - Rimuovi file temporanei e backup di notebook (`*-backup.ipynb`)

### Formato del Titolo PR

Usa titoli descrittivi:
- `[Lesson-XX] Aggiungi nuovo esempio per <concept>`
- `[Fix] Correggi refuso in README lezione-XX`
- `[Update] Migliora esempio di codice in lezione-XX`
- `[Docs] Aggiorna istruzioni di setup`

### Check Richiesti

- I notebook devono eseguire senza errori
- I file README devono essere chiari e accurati
- Seguire i pattern di codice esistenti nel repository
- Mantenere coerenza con le altre lezioni

## Note Aggiuntive

### Errori Comuni

1. **Disallineamento della versione di Python:**
   - Assicurarsi di usare Python 3.12+
   - Alcuni pacchetti potrebbero non funzionare con versioni più vecchie
   - Usare `python3 -m venv` per specificare esplicitamente la versione Python

2. **Variabili d'ambiente:**
   - Creare sempre `.env` partendo da `.env.example`
   - Non commitare il file `.env` (è inserito in `.gitignore`)
   - Effettuare il login con `az login` per autenticazione Entra ID senza chiavi

3. **Conflitti di pacchetti:**
   - Usare un ambiente virtuale pulito
   - Installare da `requirements.txt` piuttosto che pacchetti singoli
   - Alcuni notebook potrebbero richiedere ulteriori pacchetti indicati nelle loro celle markdown

4. **Servizi Azure:**
   - I servizi AI Azure richiedono abbonamento attivo
   - Alcune funzionalità sono specifiche per regione
   - Assicurati che il deployment del modello Azure OpenAI supporti la Responses API

### Percorso di Apprendimento

Progressione raccomandata attraverso le lezioni:
1. **00-course-setup** - Inizia qui per la configurazione dell'ambiente
2. **01-intro-to-ai-agents** - Comprendi i fondamenti degli agenti AI
3. **02-explore-agentic-frameworks** - Scopri diversi framework
4. **03-agentic-design-patterns** - Pattern di progettazione principali
5. Continua con le lezioni numerate in ordine

### Scelta del Framework

Scegli il framework in base ai tuoi obiettivi:
- **Tutte le lezioni**: Microsoft Agent Framework (MAF) con `FoundryChatClient`
- **Gli agenti si registrano server-side** in Microsoft Foundry Agent Service V2 e sono visibili nel portale Foundry

### Come Ottenere Aiuto

- Unisciti al [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Consulta i file README delle lezioni per indicazioni specifiche
- Controlla il [README.md](./README.md) principale per panoramica del corso
- Consulta [Course Setup](./00-course-setup/README.md) per istruzioni dettagliate di configurazione

### Contribuire

Questo è un progetto educativo aperto. Contributi benvenuti:
- Migliorare esempi di codice
- Correggere refusi o errori
- Aggiungere commenti esplicativi
- Suggerire nuovi argomenti per lezioni
- Tradurre in ulteriori lingue

Vedi [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) per necessità attuali.

## Contesto Specifico del Progetto

### Supporto Multilingue

Questo repository usa un sistema di traduzione automatica:
- Supporta più di 50 lingue
- Traduzioni nelle cartelle `/translations/<lang-code>/`
- Il workflow GitHub Actions gestisce gli aggiornamenti delle traduzioni
- I file sorgenti sono in inglese nella root del repository

### Struttura della Lezione

Ogni lezione segue un pattern coerente:
1. Anteprima video con link
2. Contenuto scritto della lezione (README.md)
3. Esempi di codice in più framework
4. Obiettivi di apprendimento e prerequisiti
5. Risorse aggiuntive collegate

### Naming degli Esempi di Codice

Formato: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lezione 1, MAF Python
- `14-sequential.ipynb` - Lezione 14, pattern avanzati MAF
- `16-python-agent-framework.ipynb` - Lezione 16, agente supporto clienti in produzione
- `17-local-agent-foundry-local.ipynb` - Lezione 17, agente locale con Foundry Local + Qwen

### Cartelle Speciali

- `translated_images/` - Immagini localizzate per le traduzioni
- `images/` - Immagini originali per contenuti in inglese
- `.devcontainer/` - Configurazione del container di sviluppo VS Code
- `.github/` - Workflow e template di GitHub Actions

### Dipendenze

Pacchetti chiave da `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Supporto protocollo Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Servizi AI di Azure
- `azure-identity` - Autenticazione Azure (AzureCliCredential)
- `azure-search-documents` - Integrazione Azure AI Search
- `mcp[cli]` - Supporto Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->