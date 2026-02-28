# AGENTS.md

## Panoramica del Progetto

Questo repository contiene "Agenti AI per Principianti" - un corso educativo completo che insegna tutto il necessario per costruire Agenti AI. Il corso è composto da oltre 15 lezioni che coprono i fondamenti, i pattern di progettazione, i framework e il deployment in produzione di agenti AI.

**Tecnologie chiave:**
- Python 3.12+
- Jupyter Notebooks per l'apprendimento interattivo
- Framework AI: Microsoft Agent Framework (MAF)
- Servizi Azure AI: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architettura:**
- Struttura basata su lezioni (directory 00-15+)
- Ogni lezione contiene: documentazione README, esempi di codice (notebook Jupyter) e immagini
- Supporto multilingue tramite sistema di traduzione automatica
- Un notebook Python per ogni lezione che utilizza Microsoft Agent Framework

## Comandi di Configurazione

### Prerequisiti
- Python 3.12 o superiore
- Sottoscrizione Azure (per Azure AI Foundry)
- Azure CLI installato e autenticato (`az login`)

### Configurazione Iniziale

1. **Clona o fai fork del repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OPPURE
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

### Variabili d'Ambiente Richieste

Per **Azure AI Foundry** (Obbligatorie):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint del progetto Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nome del deployment del modello (es. gpt-4o)

Per **Azure AI Search** (Lezione 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - chiave API Azure AI Search

Autenticazione: eseguire `az login` prima di usare i notebook (usa `AzureCliCredential`).

## Flusso di Sviluppo

### Esecuzione di Jupyter Notebooks

Ogni lezione contiene più notebook Jupyter per diversi framework:

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
- Richiede sottoscrizione Azure
- Usa `AzureAIProjectAgentProvider` per Agent Service V2 (agenti visibili nel portale Foundry)
- Pronto per la produzione con osservabilità integrata
- Pattern file: `*-python-agent-framework.ipynb`

## Istruzioni per il Testing

Questo è un repository educativo con codice di esempio piuttosto che codice di produzione con test automatizzati. Per verificare la configurazione e le modifiche:

### Testing Manuale

1. **Test ambiente Python:**
   ```bash
   python --version  # Dovrebbe essere 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test esecuzione notebook:**
   ```bash
   # Converti il notebook in script ed eseguilo (importazioni di test)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifica variabili d'ambiente:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Esecuzione di Singoli Notebook

Apri i notebook in Jupyter ed esegui le celle in ordine. Ogni notebook è indipendente e include:
- Statement di importazione
- Caricamento configurazione
- Esempi di implementazioni agenti
- Output attesi in celle markdown

## Stile del Codice

### Convenzioni Python

- **Versione Python**: 3.12+
- **Stile Codice**: Seguire le convenzioni standard Python PEP 8
- **Notebook**: Usare chiare celle markdown per spiegare i concetti
- **Importazioni**: Raggruppare per librerie standard, di terze parti e locali

### Convenzioni Jupyter Notebook

- Includere celle markdown descrittive prima delle celle codice
- Aggiungere esempi di output nei notebook come riferimento
- Usare nomi di variabili chiari e coerenti con i concetti della lezione
- Mantenere ordine di esecuzione lineare nel notebook (cella 1 → 2 → 3…)

### Organizzazione File

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Build e Deployment

### Costruzione Documentazione

Questo repository usa Markdown per la documentazione:
- File README.md in ogni cartella lezione
- README.md principale in root del repository
- Sistema di traduzione automatica tramite GitHub Actions

### Pipeline CI/CD

Situata in `.github/workflows/`:

1. **co-op-translator.yml** - Traduzione automatica in 50+ lingue
2. **welcome-issue.yml** - Messaggi di benvenuto per nuove issue
3. **welcome-pr.yml** - Messaggi di benvenuto per nuovi contributori pull request

### Deployment

Repository educativo - nessun processo di deployment. Gli utenti:
1. Fanno fork o clonano il repository
2. Eseguono i notebook localmente o in GitHub Codespaces
3. Imparano modificando ed esperimentando con gli esempi

## Linee Guida per le Pull Request

### Prima di Inviare

1. **Testa le modifiche:**
   - Esegui completamente i notebook coinvolti
   - Verifica che tutte le celle si eseguano senza errori
   - Controlla che gli output siano corretti

2. **Aggiornamenti documentazione:**
   - Aggiorna README.md se aggiungi nuovi concetti
   - Inserisci commenti nei notebook per codice complesso
   - Assicurati che le celle markdown spieghino gli scopi

3. **Modifiche ai file:**
   - Evita di committare file `.env` (usa `.env.example`)
   - Non committare le directory `venv/` o `__pycache__/`
   - Mantieni output notebook quando dimostrano concetti
   - Rimuovi file temporanei e copie backup dei notebook (`*-backup.ipynb`)

### Formato del Titolo PR

Usa titoli descrittivi:
- `[Lesson-XX] Aggiungi nuovo esempio per <concetto>`
- `[Fix] Correggi errore di battitura nel README della lezione-XX`
- `[Update] Migliora esempio di codice nella lezione-XX`
- `[Docs] Aggiorna istruzioni di configurazione`

### Controlli Richiesti

- I notebook devono eseguire senza errori
- I file README devono essere chiari e accurati
- Seguire i pattern di codice esistenti nel repository
- Mantenere coerenza con le altre lezioni

## Note Aggiuntive

### Problemi Comuni

1. **Versione Python non corretta:**
   - Assicurarsi di usare Python 3.12+
   - Alcuni pacchetti potrebbero non funzionare con versioni più vecchie
   - Usare `python3 -m venv` per specificare esplicitamente la versione Python

2. **Variabili d’ambiente:**
   - Creare sempre il file `.env` a partire da `.env.example`
   - Non committare il file `.env` (è in `.gitignore`)
   - Il token GitHub deve avere i permessi appropriati

3. **Conflitti di pacchetti:**
   - Usare un ambiente virtuale pulito
   - Installare da `requirements.txt` e non da singoli pacchetti
   - Alcuni notebook possono richiedere pacchetti aggiuntivi indicati nelle celle markdown

4. **Servizi Azure:**
   - I servizi Azure AI richiedono una sottoscrizione attiva
   - Alcune funzionalità sono limitate a specifiche regioni
   - Le limitazioni del tier gratuito si applicano ai modelli GitHub

### Percorso di Apprendimento

Progressione raccomandata tra le lezioni:
1. **00-course-setup** - Inizia qui per la configurazione ambiente
2. **01-intro-to-ai-agents** - Comprendere i fondamenti degli agenti AI
3. **02-explore-agentic-frameworks** - Impara diversi framework
4. **03-agentic-design-patterns** - Pattern di design fondamentali
5. Prosegui con le lezioni numerate in sequenza

### Scelta del Framework

Scegli il framework in base agli obiettivi:
- **Tutte le lezioni**: Microsoft Agent Framework (MAF) con `AzureAIProjectAgentProvider`
- **Agenti registrati lato server** in Azure AI Foundry Agent Service V2 e visibili nel portale Foundry

### Come Ottenere Aiuto

- Partecipa alla [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Consulta i file README delle lezioni per indicazioni specifiche
- Controlla il [README.md](./README.md) principale per panoramica corso
- Consulta [Course Setup](./00-course-setup/README.md) per istruzioni dettagliate di configurazione

### Contribuire

Questo è un progetto educativo aperto. Contributi benvenuti:
- Migliorare esempi di codice
- Correggere refusi o errori
- Aggiungere commenti esplicativi
- Suggerire nuovi argomenti per le lezioni
- Tradurre in lingue aggiuntive

Consulta le [Issue GitHub](https://github.com/microsoft/ai-agents-for-beginners/issues) per esigenze correnti.

## Contesto Specifico del Progetto

### Supporto Multilingue

Questo repository utilizza un sistema di traduzione automatica:
- Supporta oltre 50 lingue
- Le traduzioni si trovano in `/translations/<codice-lingua>/`
- Il workflow GitHub Actions gestisce gli aggiornamenti delle traduzioni
- I file sorgente sono in inglese nella root del repository

### Struttura delle Lezioni

Ogni lezione segue uno schema coerente:
1. Miniatura video con link
2. Contenuto scritto della lezione (README.md)
3. Esempi di codice in più framework
4. Obiettivi di apprendimento e prerequisiti
5. Risorse addizionali collegate

### Nomenclatura Esempi di Codice

Formato: `<numero-lezione>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lezione 1, MAF Python
- `14-sequential.ipynb` - Lezione 14, pattern avanzati MAF

### Directory Speciali

- `translated_images/` - Immagini localizzate per traduzioni
- `images/` - Immagini originali per contenuti in inglese
- `.devcontainer/` - Configurazione contenitore di sviluppo VS Code
- `.github/` - Workflow GitHub Actions e template

### Dipendenze

Pacchetti chiave da `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Supporto protocollo Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - servizi Azure AI
- `azure-identity` - autenticazione Azure (AzureCliCredential)
- `azure-search-documents` - integrazione Azure AI Search
- `mcp[cli]` - supporto Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->