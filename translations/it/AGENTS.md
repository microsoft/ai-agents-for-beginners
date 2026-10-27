# AGENTS.md

## Panoramica del Progetto

Questo repository contiene "AI Agents for Beginners" - un corso educativo completo che insegna tutto il necessario per costruire Agenti AI. Il corso è composto da 18 lezioni (numerate da 00 a 18) che coprono fondamentali, modelli di progettazione, framework, distribuzione in produzione, agenti locali/su dispositivo e sicurezza degli agenti AI.

**Tecnologie Chiave:**
- Python 3.12+
- Jupyter Notebooks per l'apprendimento interattivo
- Framework AI: Microsoft Agent Framework (MAF)
- Servizi Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architettura:**
- Struttura basata sulle lezioni (cartelle 00-18)
- Ogni lezione contiene: documentazione README, esempi di codice (notebook Jupyter) e immagini
- Supporto multilingue tramite sistema di traduzione automatica
- Un notebook Python per ogni lezione che utilizza Microsoft Agent Framework

## Comandi di Configurazione

### Prerequisiti
- Python 3.12 o superiore
- Sottoscrizione Azure (per Microsoft Foundry)
- Azure CLI installata e autenticata (`az login`)

### Configurazione Iniziale

1. **Clona o fai fork del repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Crea e attiva un ambiente virtuale Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Installa le dipendenze:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura le variabili d'ambiente:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Variabili d'Ambiente Richieste

Per **Microsoft Foundry** (Richiesto):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint del progetto Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nome del deployment del modello (ad esempio, gpt-5-mini)

Per **Azure AI Search** (Lezione 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - chiave API Azure AI Search

Autenticazione: Esegui `az login` prima di avviare i notebook (utilizza `AzureCliCredential`).

## Flusso di Sviluppo

### Avvio dei Jupyter Notebooks

Ogni lezione contiene diversi notebook Jupyter per differenti framework:

1. **Avvia Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviga nella directory della lezione** (ad esempio `01-intro-to-ai-agents/code_samples/`)

3. **Apri ed esegui i notebook:**
   - `*-python-agent-framework.ipynb` - Usando Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando Microsoft Agent Framework (.NET)

### Lavorare con Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Richiede sottoscrizione Azure
- Usa `FoundryChatClient` per Agent Service V2 (agenti visibili nel portale Foundry)
- Pronto per la produzione con osservabilità integrata
- Modello di file: `*-python-agent-framework.ipynb`

## Istruzioni per il Test

Questo è un repository educativo con codice d'esempio piuttosto che codice di produzione con test automatici. Per verificare la configurazione e le modifiche:

### Test Manuale

1. **Testa l'ambiente Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testa l'esecuzione del notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifica le variabili d'ambiente:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Esecuzione di Singoli Notebook

Apri i notebook in Jupyter ed esegui le celle sequenzialmente. Ogni notebook è autonomo e include:
- Istruzioni di importazione
- Caricamento configurazioni
- Implementazioni di esempio per agenti
- Output attesi nelle celle markdown

### Smoke-Test degli Agenti Distribuiti

Per le lezioni in cui un agente è distribuito come agente ospitato da Microsoft Foundry (01, 04, 05, 16), il repo include cataloghi di smoke-test sotto `tests/` eseguiti dal workflow `.github/workflows/smoke-test.yml` tramite l'azione [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Questi rappresentano un gate post-distribuzione leggero (l'agente è raggiungibile e risponde secondo le aspettative di base?), complementando la pipeline di valutazione nelle Lezioni 10 e 16. Vedi [tests/README.md](./tests/README.md) per la mappatura da catalogo a lezione ad agente. La lezione 17 viene eseguita localmente con Foundry Local e non ha endpoint ospitato, quindi viene validata eseguendo direttamente il notebook.

## Stile del Codice

### Convenzioni Python

- **Versione Python**: 3.12+
- **Stile Codice**: Seguire le convenzioni standard Python PEP 8
- **Notebook**: Usare chiare celle markdown per spiegare i concetti
- **Importazioni**: Raggruppare per libreria standard, terze parti, importazioni locali

### Convenzioni Jupyter Notebook

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

### Creazione Documentazione

Questo repository usa Markdown per la documentazione:
- File README.md in ogni cartella delle lezioni
- README.md principale nella radice del repository
- Sistema di traduzione automatica tramite GitHub Actions

### Pipeline CI/CD

Situata in `.github/workflows/`:

1. **co-op-translator.yml** - Traduzione automatica in oltre 50 lingue
2. **welcome-issue.yml** - Accoglie i creatori di nuovi issue
3. **welcome-pr.yml** - Accoglie i contributori di nuove pull request

### Distribuzione

Questo è un repository educativo - nessun processo di distribuzione. Gli utenti:
1. Fanno fork o clonano il repository
2. Eseguono i notebook localmente o in GitHub Codespaces
3. Imparano modificando ed esperimentando con esempi

## Linee Guida per le Pull Request

### Prima di Inviare

1. **Testa le tue modifiche:**
   - Esegui completamente i notebook interessati
   - Verifica che tutte le celle si eseguano senza errori
   - Controlla che gli output siano appropriati

2. **Aggiornamenti documentazione:**
   - Aggiorna README.md se aggiungi nuovi concetti
   - Aggiungi commenti nei notebook per codice complesso
   - Assicurati che le celle markdown spieghino lo scopo

3. **Modifiche ai file:**
   - Evita di commitare file `.env` (usa `.env.example`)
   - Non commitare le cartelle `venv/` o `__pycache__/`
   - Mantieni gli output dei notebook quando dimostrano concetti
   - Rimuovi file temporanei e backup dei notebook (`*-backup.ipynb`)

### Formato del Titolo PR

Usa titoli descrittivi:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Controlli Richiesti

- I notebook devono eseguire senza errori
- I file README devono essere chiari e accurati
- Seguire i pattern di codice esistenti nel repository
- Mantenere coerenza con le altre lezioni

## Note Aggiuntive

### Problemi Comuni

1. **Incompatibilità della versione di Python:**
   - Assicurarsi di usare Python 3.12+
   - Alcuni pacchetti potrebbero non funzionare con versioni più vecchie
   - Usare `python3 -m venv` per specificare esplicitamente la versione Python

2. **Variabili d'ambiente:**
   - Creare sempre `.env` da `.env.example`
   - Non commitare il file `.env` (è incluso in `.gitignore`)
   - Accedi con `az login` per autenticazione Entra ID senza chiave

3. **Conflitti di pacchetti:**
   - Usare un ambiente virtuale pulito
   - Installare da `requirements.txt` invece che da pacchetti individuali
   - Alcuni notebook potrebbero richiedere pacchetti addizionali menzionati nelle celle markdown

4. **Servizi Azure:**
   - I servizi Azure AI richiedono una sottoscrizione attiva
   - Alcune funzionalità sono specifiche per regione
   - Assicurarsi che il deployment del modello Azure OpenAI supporti l'API Responses

### Percorso di Apprendimento

Progressione raccomandata attraverso le lezioni:
1. **00-course-setup** - Inizia qui per configurare l'ambiente
2. **01-intro-to-ai-agents** - Comprendere i fondamentali degli agenti AI
3. **02-explore-agentic-frameworks** - Conoscere differenti framework
4. **03-agentic-design-patterns** - Modelli di design fondamentali
5. Continua seguendo le lezioni numerate in sequenza

### Selezione del Framework

Scegli il framework in base ai tuoi obiettivi:
- **Tutte le lezioni**: Microsoft Agent Framework (MAF) con `FoundryChatClient`
- **Agenti registrati lato server** nel Microsoft Foundry Agent Service V2 e visibili nel portale Foundry

### Ottenere Aiuto

- Unisciti al [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Consulta i file README delle lezioni per indicazioni specifiche
- Consulta il [README.md](./README.md) principale per una panoramica del corso
- Vedi [Course Setup](./00-course-setup/README.md) per istruzioni dettagliate di configurazione

### Contributi

Questo è un progetto educativo aperto. Contributi benvenuti:
- Migliorare esempi di codice
- Correggere refusi o errori
- Aggiungere commenti chiarificatori
- Suggerire nuovi argomenti per le lezioni
- Tradurre in lingue aggiuntive

Vedi [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) per i bisogni attuali.

## Contesto Specifico del Progetto

### Supporto Multilingue

Questo repository utilizza un sistema di traduzione automatica:
- Supporta oltre 50 lingue
- Traduzioni in cartelle `/translations/<lang-code>/`
- Workflow GitHub Actions gestisce aggiornamenti di traduzione
- I file sorgente sono in inglese nella radice del repository

### Struttura della Lezione

Ogni lezione segue uno schema coerente:
1. Miniatura video con link
2. Contenuto scritto della lezione (README.md)
3. Esempi di codice in vari framework
4. Obiettivi di apprendimento e prerequisiti
5. Risorse di apprendimento extra collegate

### Nomenclatura degli Esempi di Codice

Formato: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lezione 1, MAF Python
- `14-sequential.ipynb` - Lezione 14, pattern avanzati MAF
- `16-python-agent-framework.ipynb` - Lezione 16, agente supporto clienti in produzione
- `17-local-agent-foundry-local.ipynb` - Lezione 17, agente locale con Foundry Local + Qwen

### Cartelle Speciali

- `translated_images/` - Immagini localizzate per traduzioni
- `images/` - Immagini originali per contenuti in inglese
- `.devcontainer/` - Configurazione del container di sviluppo VS Code
- `.github/` - Workflow e template GitHub Actions

### Dipendenze

Pacchetti chiave da `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Supporto protocollo Agente-Agente
- `azure-ai-inference`, `azure-ai-projects` - Servizi Azure AI
- `azure-identity` - Autenticazione Azure (AzureCliCredential)
- `azure-search-documents` - Integrazione Azure AI Search
- `mcp[cli]` - Supporto protocollo Model Context

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->