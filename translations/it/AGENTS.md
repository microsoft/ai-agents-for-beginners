# AGENTS.md

## Panoramica del Progetto

Questo repository contiene "AI Agents for Beginners" - un corso educativo completo che insegna tutto ciò che serve per costruire agenti AI. Il corso è composto da oltre 15 lezioni che coprono i fondamenti, i design pattern, i framework e il deployment in produzione degli agenti AI.

**Tecnologie Chiave:**
- Python 3.12+
- Jupyter Notebooks per l'apprendimento interattivo
- Framework AI: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Servizi Azure AI: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (disponibile un livello gratuito)

**Architettura:**
- Struttura basata su lezioni (directory 00-15+)
- Ogni lezione contiene: documentazione README, esempi di codice (notebook Jupyter) e immagini
- Supporto multilingue tramite sistema di traduzione automatica
- Opzioni multiple di framework per ogni lezione (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Comandi di Configurazione

### Prerequisiti
- Python 3.12 o superiore
- Account GitHub (per GitHub Models - livello gratuito)
- Abbonamento Azure (opzionale, per i servizi Azure AI)

### Configurazione Iniziale

1. **Clona o fai un fork del repository:**
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


### Variabili d'Ambiente Necessarie

Per **GitHub Models (Gratuito)**:
- `GITHUB_TOKEN` - Token di accesso personale da GitHub

Per **Servizi Azure AI** (opzionale):
- `PROJECT_ENDPOINT` - Endpoint del progetto Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - Chiave API di Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL dell'endpoint di Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Nome del deployment per il modello di chat
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Nome del deployment per gli embeddings
- Configurazione aggiuntiva di Azure come mostrato in `.env.example`

## Workflow di Sviluppo

### Esecuzione dei Notebook Jupyter

Ogni lezione contiene diversi notebook Jupyter per i vari framework:

1. **Avvia Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviga nella directory di una lezione** (es. `01-intro-to-ai-agents/code_samples/`)

3. **Apri ed esegui i notebook:**
   - `*-semantic-kernel.ipynb` - Utilizzando il framework Semantic Kernel
   - `*-autogen.ipynb` - Utilizzando il framework AutoGen
   - `*-python-agent-framework.ipynb` - Utilizzando il Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Utilizzando il Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Utilizzando il servizio Azure AI Agent

### Lavorare con i Diversi Framework

**Semantic Kernel + GitHub Models:**
- Livello gratuito disponibile con account GitHub
- Ideale per apprendimento e sperimentazione
- Pattern file: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Livello gratuito disponibile con account GitHub
- Capacità di orchestrazione multi-agente
- Pattern file: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Ultimo framework di Microsoft
- Disponibile in Python e .NET
- Pattern file: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Richiede abbonamento Azure
- Funzionalità pronte per la produzione
- Pattern file: `*-azureaiagent.ipynb`

## Istruzioni per il Testing

Questo è un repository educativo con codice di esempio piuttosto che codice di produzione con test automatizzati. Per verificare la configurazione e le modifiche:

### Testing Manuale

1. **Testa l'ambiente Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Testa l'esecuzione dei notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifica le variabili d'ambiente:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### Esecuzione dei Singoli Notebook

Apri i notebook in Jupyter ed esegui le celle in sequenza. Ogni notebook è autonomo e include:
- Dichiarazioni di importazione
- Caricamento della configurazione
- Implementazioni di esempio degli agenti
- Output attesi nelle celle markdown

## Stile del Codice

### Convenzioni Python

- **Versione Python**: 3.12+
- **Stile del Codice**: Segui le convenzioni standard PEP 8 di Python
- **Notebook**: Usa celle markdown chiare per spiegare i concetti
- **Importazioni**: Raggruppa per libreria standard, librerie di terze parti, importazioni locali

### Convenzioni per i Notebook Jupyter

- Includi celle markdown descrittive prima delle celle di codice
- Aggiungi esempi di output nei notebook come riferimento
- Usa nomi di variabili chiari che corrispondano ai concetti della lezione
- Mantieni l'ordine di esecuzione lineare (cella 1 → 2 → 3...)

### Organizzazione dei File

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## Build e Deployment

### Creazione della Documentazione

Questo repository utilizza Markdown per la documentazione:
- File README.md in ogni cartella di lezione
- README.md principale nella radice del repository
- Sistema di traduzione automatica tramite GitHub Actions

### Pipeline CI/CD

Situata in `.github/workflows/`:

1. **co-op-translator.yml** - Traduzione automatica in oltre 50 lingue
2. **welcome-issue.yml** - Messaggio di benvenuto per i creatori di nuove issue
3. **welcome-pr.yml** - Messaggio di benvenuto per i nuovi contributori di pull request

### Deployment

Questo è un repository educativo - nessun processo di deployment. Gli utenti:
1. Fanno un fork o clonano il repository
2. Eseguono i notebook localmente o in GitHub Codespaces
3. Apprendono modificando e sperimentando con gli esempi

## Linee Guida per le Pull Request

### Prima di Inviare

1. **Testa le tue modifiche:**
   - Esegui completamente i notebook interessati
   - Verifica che tutte le celle vengano eseguite senza errori
   - Controlla che gli output siano appropriati

2. **Aggiornamenti alla documentazione:**
   - Aggiorna README.md se aggiungi nuovi concetti
   - Aggiungi commenti nei notebook per codice complesso
   - Assicurati che le celle markdown spieghino lo scopo

3. **Modifiche ai file:**
   - Evita di committare file `.env` (usa `.env.example`)
   - Non committare directory `venv/` o `__pycache__/`
   - Mantieni gli output dei notebook quando dimostrano concetti
   - Rimuovi file temporanei e backup dei notebook (`*-backup.ipynb`)

### Formato del Titolo della PR

Usa titoli descrittivi:
- `[Lesson-XX] Aggiungi nuovo esempio per <concetto>`
- `[Fix] Correggi errore di battitura in README della lezione-XX`
- `[Update] Migliora esempio di codice nella lezione-XX`
- `[Docs] Aggiorna istruzioni di configurazione`

### Controlli Necessari

- I notebook devono essere eseguiti senza errori
- I file README devono essere chiari e accurati
- Segui i pattern di codice esistenti nel repository
- Mantieni la coerenza con le altre lezioni

## Note Aggiuntive

### Problemi Comuni

1. **Mismatch della versione di Python:**
   - Assicurati di utilizzare Python 3.12+
   - Alcuni pacchetti potrebbero non funzionare con versioni precedenti
   - Usa `python3 -m venv` per specificare esplicitamente la versione di Python

2. **Variabili d'ambiente:**
   - Crea sempre `.env` da `.env.example`
   - Non committare il file `.env` (è in `.gitignore`)
   - Il token GitHub necessita di permessi appropriati

3. **Conflitti di pacchetti:**
   - Usa un ambiente virtuale nuovo
   - Installa da `requirements.txt` piuttosto che da pacchetti individuali
   - Alcuni notebook potrebbero richiedere pacchetti aggiuntivi menzionati nelle loro celle markdown

4. **Servizi Azure:**
   - I servizi Azure AI richiedono un abbonamento attivo
   - Alcune funzionalità sono specifiche per regione
   - Limitazioni del livello gratuito si applicano ai GitHub Models

### Percorso di Apprendimento

Progressione consigliata attraverso le lezioni:
1. **00-course-setup** - Inizia qui per la configurazione dell'ambiente
2. **01-intro-to-ai-agents** - Comprendi i fondamenti degli agenti AI
3. **02-explore-agentic-frameworks** - Scopri i diversi framework
4. **03-agentic-design-patterns** - Pattern di design fondamentali
5. Continua attraverso le lezioni numerate in sequenza

### Selezione del Framework

Scegli il framework in base ai tuoi obiettivi:
- **Apprendimento/Prototipazione**: Semantic Kernel + GitHub Models (gratuito)
- **Sistemi multi-agente**: AutoGen
- **Ultime funzionalità**: Microsoft Agent Framework (MAF)
- **Deployment in produzione**: Azure AI Agent Service

### Ottenere Aiuto

- Unisciti al [Discord della Community di Azure AI Foundry](https://aka.ms/ai-agents/discord)
- Consulta i file README delle lezioni per indicazioni specifiche
- Controlla il [README.md principale](./README.md) per una panoramica del corso
- Fai riferimento a [Course Setup](./00-course-setup/README.md) per istruzioni dettagliate sulla configurazione

### Contribuire

Questo è un progetto educativo aperto. Contributi benvenuti:
- Migliora gli esempi di codice
- Correggi errori di battitura o errori
- Aggiungi commenti chiarificatori
- Suggerisci nuovi argomenti per le lezioni
- Traduci in lingue aggiuntive

Consulta [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) per le necessità attuali.

## Contesto Specifico del Progetto

### Supporto Multilingue

Questo repository utilizza un sistema di traduzione automatica:
- Supporto per oltre 50 lingue
- Traduzioni nelle directory `/translations/<lang-code>/`
- Il workflow GitHub Actions gestisce gli aggiornamenti delle traduzioni
- I file sorgente sono in inglese nella radice del repository

### Struttura delle Lezioni

Ogni lezione segue un pattern coerente:
1. Miniatura del video con link
2. Contenuto scritto della lezione (README.md)
3. Esempi di codice in diversi framework
4. Obiettivi di apprendimento e prerequisiti
5. Risorse di apprendimento extra collegate

### Nomenclatura degli Esempi di Codice

Formato: `<numero-lezione>-<nome-framework>.ipynb`
- `04-semantic-kernel.ipynb` - Lezione 4, Semantic Kernel
- `07-autogen.ipynb` - Lezione 7, AutoGen
- `14-python-agent-framework.ipynb` - Lezione 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Lezione 14, MAF .NET

### Directory Speciali

- `translated_images/` - Immagini localizzate per le traduzioni
- `images/` - Immagini originali per il contenuto in inglese
- `.devcontainer/` - Configurazione del container di sviluppo per VS Code
- `.github/` - Workflow e template di GitHub Actions

### Dipendenze

Pacchetti chiave da `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - Framework AutoGen
- `semantic-kernel` - Framework Semantic Kernel
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Servizi Azure AI
- `azure-search-documents` - Integrazione Azure AI Search
- `chromadb` - Database vettoriale per esempi RAG
- `chainlit` - Framework UI per chat
- `browser_use` - Automazione del browser per agenti
- `mcp[cli]` - Supporto per Model Context Protocol
- `mem0ai` - Gestione della memoria per agenti

---

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.