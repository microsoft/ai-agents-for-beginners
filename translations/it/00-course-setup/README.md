# Configurazione del Corso

## Introduzione

Questa lezione spiega come eseguire gli esempi di codice di questo corso.

## Unisciti ad Altri Studenti e Ricevi Aiuto

Prima di iniziare a clonare il tuo repository, unisciti al [canale Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) per ricevere aiuto con la configurazione, qualsiasi domanda sul corso, o per connetterti con altri studenti.

## Clona o Fai Fork di questo Repo

Per iniziare, clona o fai il fork del repository GitHub. Questo creerà la tua versione del materiale del corso così potrai eseguire, testare e modificare il codice!

Puoi farlo cliccando sul link per <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fare il fork del repo</a>

Ora dovresti avere la tua versione forkata di questo corso al seguente link:

![Forked Repo](../../../translated_images/it/forked-repo.33f27ca1901baa6a.webp)

### Clonazione Poco Profonda (consigliata per workshop / Codespaces)

  >Il repository completo può essere grande (~3 GB) scaricando tutta la cronologia e tutti i file. Se parteciperai solo al workshop o ti servono solo poche cartelle delle lezioni, una clonazione poco profonda (o clonazione sparsa) evita gran parte di quel download troncando la cronologia e/o saltando blob.

#### Clonazione Poco Profonda Rapida — cronologia minima, tutti i file

Sostituisci `<your-username>` nei comandi sottostanti con l’URL del fork (o con l’URL upstream se preferisci).

Per clonare solo la cronologia dell’ultimo commit (download piccolo):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Per clonare un branch specifico:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clonazione Parziale (sparsa) — blob minimi + solo cartelle selezionate

Questo utilizza la clonazione parziale e sparse-checkout (richiede Git 2.25+ e Git moderno con supporto a clonazione parziale):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Entra nella cartella del repo:

```bash|powershell
cd ai-agents-for-beginners
```

Quindi specifica quali cartelle vuoi (l’esempio sotto mostra due cartelle):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Dopo aver clonato e verificato i file, se ti servono solo i file e vuoi liberare spazio (niente cronologia git), elimina i metadati del repository (💀 irreversibile — perderai tutte le funzionalità Git: nessun commit, pull, push o accesso alla cronologia).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Usare GitHub Codespaces (consigliato per evitare grandi download locali)

- Crea un nuovo Codespace per questo repo tramite l'[interfaccia GitHub](https://github.com/codespaces).  

- Nel terminale del Codespace appena creato, esegui uno dei comandi di clonazione poco profonda/sparsa sopra per portare solo le cartelle delle lezioni di cui hai bisogno nell’ambiente Codespace.
- Opzionale: dopo la clonazione dentro Codespaces, rimuovi .git per recuperare spazio extra (vedi comandi di rimozione sopra).
- Nota: Se preferisci aprire direttamente il repo in Codespaces (senza clonare di nuovo), tieni presente che Codespaces costruirà l’ambiente devcontainer e potrebbe comunque fornire più di quanto ti serve. Clonare una copia poco profonda dentro un nuovo Codespace ti dà più controllo sull’uso del disco.

#### Consigli

- Sostituisci sempre l’URL del clone con quello del tuo fork se vuoi modificare o fare commit.
- Se poi necessiti di più cronologia o file, puoi recuperarli o regolare sparse-checkout per includere cartelle aggiuntive.

## Esecuzione del Codice

Questo corso offre una serie di Jupyter Notebooks che puoi eseguire per fare esperienza pratica nella creazione di AI Agents.

Gli esempi di codice utilizzano **Microsoft Agent Framework (MAF)** con il `FoundryChatClient`, che si collega a **Microsoft Foundry Agent Service V2** (le Responses API) tramite **Microsoft Foundry**.

Tutti i notebook Python sono etichettati `*-python-agent-framework.ipynb`.

## Requisiti

- Python 3.12+
  - **NOTA**: Se non hai Python3.12 installato, assicurati di installarlo. Poi crea il tuo venv usando python3.12 per garantire che le versioni corrette vengano installate dal file requirements.txt.
  
    >Esempio

    Crea la cartella virtualenv Python:

    ```bash|powershell
    python -m venv venv
    ```

    Poi attiva l’ambiente venv per:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Per i codici d’esempio che usano .NET, assicurati di installare [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o successivo. Poi, verifica la versione del SDK .NET installata:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Necessaria per l’autenticazione. Installa da [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Sottoscrizione Azure** — Per l’accesso a Microsoft Foundry e Microsoft Foundry Agent Service.
- **Progetto Microsoft Foundry** — Un progetto con modello distribuito (e.g., `gpt-5-mini`). Vedi [Passo 1](#passo-1-crea-un-progetto-microsoft-foundry) qui sotto.

Abbiamo incluso un file `requirements.txt` nella radice di questo repository che contiene tutti i pacchetti Python necessari per eseguire gli esempi di codice.

Puoi installarli eseguendo questo comando nel terminale nella radice del repository:

```bash|powershell
pip install -r requirements.txt
```

Raccomandiamo di creare un ambiente virtuale Python per evitare conflitti e problemi.

## Configura VSCode

Assicurati di utilizzare la versione corretta di Python in VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configura Microsoft Foundry e Microsoft Foundry Agent Service

### Passo 1: Crea un Progetto Microsoft Foundry

Hai bisogno di un **hub** e un **progetto** Microsoft Foundry con un modello distribuito per eseguire i notebook.

1. Vai su [ai.azure.com](https://ai.azure.com) e accedi con il tuo account Azure.
2. Crea un **hub** (o usa uno esistente). Vedi: [Panoramica delle risorse Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. All’interno dell’hub, crea un **progetto**.
4. Distribuisci un modello (e.g., `gpt-5-mini`) da **Models + Endpoints** → **Deploy model**.

### Passo 2: Recupera l’Endpoint del Progetto e il Nome di Distribuzione del Modello

Dal tuo progetto nel portale Microsoft Foundry:

- **Endpoint del Progetto** — Vai alla pagina **Overview** e copia l’URL endpoint.

![Project Connection String](../../../translated_images/it/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nome di Distribuzione del Modello** — Vai su **Models + Endpoints**, seleziona il modello distribuito e annota il **Deployment name** (e.g., `gpt-5-mini`).

### Passo 3: Accedi ad Azure con `az login`

Tutti i notebook usano **`AzureCliCredential`** per l’autenticazione — nessuna chiave API da gestire. Questo richiede di essere connessi tramite Azure CLI.

1. **Installa Azure CLI** se non l’hai già fatto: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Accedi** eseguendo:

    ```bash|powershell
    az login
    ```

    Oppure, se sei in un ambiente remoto/Codespace senza browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Seleziona la sottoscrizione** se richiesto — scegli quella contenente il progetto Foundry.

4. **Verifica** di essere connessi:

    ```bash|powershell
    az account show
    ```

> **Perché `az login`?** I notebook si autenticano usando `AzureCliCredential` dal pacchetto `azure-identity`. Ciò significa che la sessione Azure CLI fornisce le credenziali — niente chiavi API o segreti nel file `.env`. Questa è una [buona pratica di sicurezza](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Passo 4: Crea il tuo file `.env`

Copia il file di esempio:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Apri `.env` e completa questi due valori:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variabile | Dove trovarla |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portale Foundry → il tuo progetto → pagina **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portale Foundry → **Models + Endpoints** → nome del modello distribuito |

Questo è tutto per la maggior parte delle lezioni! I notebook si autenticheranno automaticamente tramite la tua sessione `az login`.

### Passo 5: Installa le Dipendenze Python

```bash|powershell
pip install -r requirements.txt
```

Raccomandiamo di eseguire questo all’interno dell’ambiente virtuale creato in precedenza.

## Configurazione Aggiuntiva per la Lezione 5 (Agentic RAG)

La lezione 5 usa **Azure AI Search** per la generazione aumentata da recupero. Se prevedi di eseguire quella lezione, aggiungi queste variabili al tuo file `.env`:

| Variabile | Dove trovarla |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portale Azure → tua risorsa **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Portale Azure → tua risorsa **Azure AI Search** → **Settings** → **Keys** → chiave amministratore primaria |

## Configurazione Aggiuntiva per Lezioni che Usano Azure OpenAI Direttamente (Lezioni 6 e 8)

Alcuni notebook delle lezioni 6 e 8 chiamano **Azure OpenAI** direttamente (usando le **Responses API**) invece di passare da un progetto Microsoft Foundry. Questi esempi usavano precedentemente GitHub Models, ora deprecato (ritirato da luglio 2026) e non supporta le Responses API. Se prevedi di eseguire quegli esempi, aggiungi queste variabili al tuo file `.env`:

| Variabile | Dove trovarla |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portale Azure → risorsa **Azure OpenAI** → **Keys and Endpoint** → Endpoint (e.g. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Nome del modello distribuito (e.g. `gpt-5-mini`) che supporta le Responses API |
| `AZURE_OPENAI_API_KEY` | Opzionale — solo se utilizzi autenticazione tramite chiave invece di `az login` / Entra ID |

> Le Responses API usano l’endpoint stabile `/openai/v1/`, quindi non serve `api-version`. Accedi con `az login` per usare l’autenticazione senza chiave tramite Entra ID.

## Fornitore Alternativo: MiniMax (Compatibile OpenAI)

[MiniMax](https://platform.minimaxi.com/) fornisce modelli con contesto esteso (fino a 204K token) tramite un’API compatibile OpenAI. Poiché il `OpenAIChatClient` del Microsoft Agent Framework funziona con qualsiasi endpoint compatibile OpenAI, puoi usare MiniMax come alternativa plug-and-play ad Azure OpenAI o OpenAI.

Aggiungi queste variabili al tuo file `.env`:

| Variabile | Dove trovarla |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Usa `https://api.minimax.io/v1` (valore di default) |
| `MINIMAX_MODEL_ID` | Nome del modello da usare (es. `MiniMax-M3`) |

**Modelli d’esempio**: `MiniMax-M3` (consigliato), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (risposte più rapide). I nomi e la disponibilità dei modelli possono cambiare nel tempo, e l’accesso a un modello può dipendere dal tuo account o regione — verifica la [MiniMax Platform](https://platform.minimaxi.com/) per la lista aggiornata. Se `MiniMax-M3` non è disponibile per il tuo account, imposta `MINIMAX_MODEL_ID` su un modello a cui hai accesso (es. `MiniMax-M2.7`).

Gli esempi di codice che usano `OpenAIChatClient` (e.g., la lezione 14 sul workflow di prenotazione hotel) rileveranno automaticamente e useranno la configurazione MiniMax quando `MINIMAX_API_KEY` è impostato.

## Fornitore Alternativo: Foundry Local (Esegui Modelli sul Dispositivo)

[Foundry Local](https://foundrylocal.ai) è un runtime leggero che scarica, gestisce e serve modelli linguistici **interamente sul tuo computer** tramite un’API compatibile OpenAI — niente cloud, nessuna sottoscrizione Azure, nessuna chiave API. È una ottima opzione per sviluppo offline, sperimentazione senza costi cloud, o mantenere i dati sul dispositivo.

Poiché il `OpenAIChatClient` del Microsoft Agent Framework funziona con qualsiasi endpoint compatibile OpenAI, Foundry Local è una valida alternativa locale ad Azure OpenAI.

**1. Installa Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Scarica ed esegui un modello** (questo avvia anche il servizio locale):

```bash
foundry model list          # vedere i modelli disponibili
foundry model run phi-4-mini
```

**3. Installa l’SDK Python** necessario per scoprire l’endpoint locale:

```bash
pip install foundry-local-sdk
```

**4. Punta il Microsoft Agent Framework al tuo modello locale:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Scarica (se necessario) e serve il modello localmente, quindi scopre l'endpoint/porta.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # es. http://localhost:<port>/v1
    api_key=manager.api_key,        # sempre "non richiesto" per Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Nota:** Foundry Local espone un endpoint compatibile OpenAI **Chat Completions**. Usalo per sviluppo locale e scenari offline. Per il set completo di funzionalità **Responses API** (conversazioni con stato, orchestrazione profonda di tool e sviluppo in stile agent), usa **Azure OpenAI** o un progetto **Microsoft Foundry** come illustrato nelle lezioni. Consulta la [documentazione Foundry Local](https://foundrylocal.ai) per il catalogo modelli e supporto piattaforme aggiornato.

## Configurazione Aggiuntiva per la Lezione 8 (Workflow di Grounding Bing)


Il notebook del flusso di lavoro condizionale nella lezione 8 utilizza **Bing grounding** tramite Microsoft Foundry. Se prevedi di eseguire quel campione, aggiungi questa variabile al tuo file `.env`:

| Variabile | Dove trovarla |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portale Microsoft Foundry → il tuo progetto → **Gestione** → **Risorse connesse** → la tua connessione Bing → copia l'ID della connessione |

## Risoluzione dei problemi

### Errori di verifica del certificato SSL su macOS

Se usi macOS e incontri un errore come:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Questo è un problema noto di Python su macOS in cui i certificati SSL di sistema non sono automaticamente considerati attendibili. Prova le seguenti soluzioni in ordine:

**Opzione 1: Esegui lo script di Installazione Certificati di Python (consigliato)**

```bash
# Sostituisci 3.XX con la versione di Python installata (ad esempio, 3.12 o 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opzione 2: Usa `connection_verify=False` nel tuo notebook (solo per i notebook Modelli GitHub)**

Nel notebook della Lezione 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), è già incluso un workaround commentato. Rimuovi il commento da `connection_verify=False` quando crei il client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Disabilita la verifica SSL se incontri errori di certificato
)
```

> **⚠️ Attenzione:** Disabilitare la verifica SSL (`connection_verify=False`) riduce la sicurezza saltando la convalida del certificato. Usalo solo come soluzione temporanea in ambienti di sviluppo, mai in produzione.

**Opzione 3: Installa e usa `truststore`**

```bash
pip install truststore
```

Poi aggiungi quanto segue all’inizio del tuo notebook o script prima di effettuare qualsiasi chiamata di rete:

```python
import truststore
truststore.inject_into_ssl()
```

## Bloccato da qualche parte?

Se hai problemi nell’eseguire questa configurazione, entra nella nostra <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> o <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">crea un issue</a>.

## Lezione successiva

Ora sei pronto per eseguire il codice di questo corso. Buon apprendimento sul mondo degli Agenti AI!

[Introduzione agli Agenti AI e ai casi d'uso degli agenti](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->