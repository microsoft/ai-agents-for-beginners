# AGENTS.md

## Panoramica del Progetto

Questo repository contiene "Agenti AI per Principianti" - un corso educativo completo che insegna tutto il necessario per costruire Agenti AI. Il corso è composto da oltre 15 lezioni che coprono fondamentali, pattern di design, framework e distribuzione in produzione degli agenti AI.

**Tecnologie Chiave:**
- Python 3.12+
- Jupyter Notebooks per apprendimento interattivo
- Framework AI: Microsoft Agent Framework (MAF)
- Servizi Azure AI: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architettura:**
- Struttura basata su lezioni (directory 00-15+)
- Ogni lezione contiene: documentazione README, esempi di codice (notebook Jupyter) e immagini
- Supporto multilingue tramite sistema di traduzione automatica
- Un notebook Python per ogni lezione che utilizza Microsoft Agent Framework

## Comandi per la Configurazione

### Prerequisiti
- Python 3.12 o superiore
- Abbonamento Azure (per Azure AI Foundry)
- Azure CLI installato e autenticato (`az login`)

### Configurazione Iniziale

1. **Clona o fai fork del repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # O
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Crea e attiva un ambiente virtuale Python:**
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
   # Modifica .env con le tue chiavi API e gli endpoint
   ```

### Variabili d'Ambiente Necessarie

Per **Azure AI Foundry** (obbligatorio):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint del progetto Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nome del deployment del modello (es. gpt-4o)

Per **Azure AI Search** (Lezione 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - chiave API Azure AI Search

Autenticazione: eseguire `az login` prima di usare i notebook (utilizza `AzureCliCredential`).

## Flusso di Lavoro di Sviluppo

### Esecuzione dei Jupyter Notebooks

Ogni lezione contiene più notebook Jupyter per differenti framework:

1. **Avvia Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviga nella directory della lezione** (es. `01-intro-to-ai-agents/code_samples/`)

3. **Apri ed esegui i notebook:**
   - `*-python-agent-framework.ipynb` - Usando Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Usando Microsoft Agent Framework (.NET)

### Lavorare con Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Richiede abbonamento Azure
- Usa `AzureAIProjectAgentProvider` per Agent Service V2 (agenti visibili nel portale Foundry)
- Pronto per produzione con osservabilità integrata
- Pattern dei file: `*-python-agent-framework.ipynb`

## Istruzioni per il Testing

Questo è un repository educativo con codice di esempio piuttosto che codice di produzione con test automatizzati. Per verificare la tua configurazione e modifiche:

### Test Manuale

1. **Test ambiente Python:**
   ```bash
   python --version  # Dovrebbe essere 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test esecuzione notebook:**
   ```bash
   # Converti il notebook in script ed esegui (testa le importazioni)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifica variabili d'ambiente:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Esecuzione di Singoli Notebook

Apri i notebook in Jupyter e esegui le celle in sequenza. Ogni notebook è autonomo e include:
- Istruzioni di importazione
- Caricamento configurazione
- Implementazioni esempio di agenti
- Output attesi in celle markdown

## Stile di Codice

### Convenzioni Python

- **Versione Python**: 3.12+
- **Stile codice**: Seguire le convenzioni PEP 8 standard per Python
- **Notebook**: Usare chiare celle markdown per spiegare i concetti
- **Import**: Raggruppare per librerie standard, di terze parti e locali

### Convenzioni Jupyter Notebook

- Includere celle markdown descrittive prima delle celle di codice
- Aggiungere esempi di output nei notebook per riferimento
- Usare nomi di variabili chiari che rispecchiano i concetti delle lezioni
- Mantenere ordine lineare di esecuzione (cella 1 → 2 → 3...)

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

### Costruzione Documentazione

Questo repository utilizza Markdown per la documentazione:
- File README.md in ogni cartella lezione
- README.md principale nella root del repository
- Sistema di traduzione automatica tramite GitHub Actions

### Pipeline CI/CD

Situata in `.github/workflows/`:

1. **co-op-translator.yml** - Traduzione automatica in oltre 50 lingue
2. **welcome-issue.yml** - Messaggio di benvenuto per nuovi issue
3. **welcome-pr.yml** - Messaggio di benvenuto per nuovi contributori di pull request

### Distribuzione

Questo è un repository educativo - nessun processo di distribuzione. Gli utenti:
1. Forkano o clonano il repository
2. Eseguono notebook localmente o su GitHub Codespaces
3. Imparano modificando ed esperimentando con esempi

## Linee Guida per le Pull Request

### Prima di Inviare

1. **Testa le modifiche:**
   - Esegui completamente i notebook coinvolti
   - Verifica che tutte le celle si eseguano senza errori
   - Controlla che gli output siano appropriati

2. **Aggiornamenti della documentazione:**
   - Aggiorna README.md se aggiungi nuovi concetti
   - Aggiungi commenti nei notebook per codice complesso
   - Assicurati che le celle markdown spieghino lo scopo

3. **Modifiche ai file:**
   - Evita di committare file `.env` (usa `.env.example`)
   - Non committare le directory `venv/` o `__pycache__/`
   - Mantieni output notebook quando dimostrano concetti
   - Rimuovi file temporanei e notebook di backup (`*-backup.ipynb`)

### Formato del Titolo PR

Usa titoli descrittivi:
- `[Lesson-XX] Aggiungi nuovo esempio per <concept>`
- `[Fix] Correggi errore di battitura in lesson-XX README`
- `[Update] Migliora esempio di codice in lesson-XX`
- `[Docs] Aggiorna istruzioni di configurazione`

### Controlli Richiesti

- I notebook devono eseguire senza errori
- I file README devono essere chiari e accurati
- Seguire i pattern di codice esistenti nel repository
- Mantenere coerenza con le altre lezioni

## Note Aggiuntive

### Errori Comuni

1. **Versione Python non corretta:**
   - Assicurarsi di usare Python 3.12+
   - Alcuni pacchetti potrebbero non funzionare con versioni più vecchie
   - Usare `python3 -m venv` per specificare esplicitamente la versione Python

2. **Variabili d'ambiente:**
   - Creare sempre `.env` a partire da `.env.example`
   - Non committare il file `.env` (è in `.gitignore`)
   - Il token GitHub necessita permessi appropriati

3. **Conflitti di pacchetti:**
   - Usare un ambiente virtuale pulito
   - Installare da `requirements.txt` invece che singoli pacchetti
   - Alcuni notebook potrebbero richiedere pacchetti aggiuntivi menzionati nelle celle markdown

4. **Servizi Azure:**
   - I servizi Azure AI richiedono un abbonamento attivo
   - Alcune funzionalità sono specifiche per regione
   - Limitazioni del livello gratuito per GitHub Models

### Percorso di Apprendimento

Progressione raccomandata nelle lezioni:
1. **00-course-setup** - Inizia da qui per la configurazione ambiente
2. **01-intro-to-ai-agents** - Comprendi i fondamenti degli agenti AI
3. **02-explore-agentic-frameworks** - Scopri i vari framework
4. **03-agentic-design-patterns** - Pattern di design core
5. Prosegui seguendo l'ordine numerico delle lezioni

### Scelta del Framework

Scegli il framework in base ai tuoi obiettivi:
- **Tutte le lezioni**: Microsoft Agent Framework (MAF) con `AzureAIProjectAgentProvider`
- **Agenti registrati lato server** in Azure AI Foundry Agent Service V2 e visibili nel portale Foundry

### Dove Trovare Aiuto

- Unisciti al [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Consulta i file README delle lezioni per istruzioni specifiche
- Controlla il [README.md](./README.md) principale per la panoramica del corso
- Vedi [Course Setup](./00-course-setup/README.md) per istruzioni dettagliate di configurazione

### Contributi

Questo è un progetto educativo aperto. Sono benvenuti contributi:
- Migliora esempi di codice
- Correggi refusi o errori
- Aggiungi commenti esplicativi
- Suggerisci nuovi argomenti per le lezioni
- Traduci in ulteriori lingue

Consulta le [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) per le necessità attuali.

## Contesto Specifico del Progetto

### Supporto Multilingue

Questo repository utilizza un sistema di traduzione automatica:
- Supportate oltre 50 lingue
- Traduzioni sotto `/translations/<lang-code>/`
- Workflow GitHub Actions gestisce aggiornamenti di traduzione
- I file sorgente sono in inglese nella root del repository

### Struttura delle Lezioni

Ogni lezione segue uno schema costante:
1. Miniatura video con link
2. Contenuto scritto della lezione (README.md)
3. Esempi di codice in più framework
4. Obiettivi di apprendimento e prerequisiti
5. Risorse extra di apprendimento linkate

### Nomenclatura Esempi Codice

Formato: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lezione 1, MAF Python
- `14-sequential.ipynb` - Lezione 14, pattern avanzati MAF

### Directory Speciali

- `translated_images/` - Immagini localizzate per traduzioni
- `images/` - Immagini originali per contenuti in inglese
- `.devcontainer/` - Configurazione container sviluppo VS Code
- `.github/` - Workflow e template GitHub Actions

### Dipendenze

Pacchetti chiave dal `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Supporto protocollo Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Servizi Azure AI
- `azure-identity` - Autenticazione Azure (AzureCliCredential)
- `azure-search-documents` - Integrazione Azure AI Search
- `mcp[cli]` - Supporto Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale effettuata da un esperto umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->