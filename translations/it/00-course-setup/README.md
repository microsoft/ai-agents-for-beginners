# Configurazione del corso

## Introduzione

Questa lezione spiega come eseguire gli esempi di codice di questo corso.

## Unisciti ad altri partecipanti e ottieni aiuto

Prima di iniziare a clonare il tuo repo, unisciti al [canale Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) per ottenere aiuto con la configurazione, porre domande sul corso o connetterti con altri partecipanti.

## Clona o crea un fork di questo repository

Per cominciare, clona o crea un fork del repository GitHub. Questo creerà la tua versione del materiale del corso in modo da poter eseguire, testare e modificare il codice!

This can be done by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">eseguire il fork del repo</a>

Dovresti ora avere la tua versione fork del corso al seguente link:

![Repository forkato](../../../translated_images/it/forked-repo.33f27ca1901baa6a.webp)

### Clonazione superficiale (consigliata per workshop / Codespaces)

  >Il repository completo può essere grande (~3 GB) quando scarichi tutta la cronologia e tutti i file. Se stai partecipando solo al workshop o hai bisogno solo di alcune cartelle delle lezioni, una clonazione superficiale (o una clonazione sparse) evita la maggior parte di quel download troncando la cronologia e/o saltando i blob.

#### Clonazione superficiale rapida — cronologia minima, tutti i file

Replace `<your-username>` in the below commands with your fork URL (or the upstream URL if you prefer).

To clone only the latest commit history (small download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

To clone a specific branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Clonazione parziale (sparse) — blob minimi + solo cartelle selezionate

This uses partial clone and sparse-checkout (requires Git 2.25+ and recommended modern Git with partial clone support):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Traverse into the repo folder:

```bash|powershell
cd ai-agents-for-beginners
```

Then specify which folders you want (example below shows two folders):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

After cloning and verifying the files, if you only need files and want to free space (no git history), please delete the repository metadata (💀irreversible — you will lose all Git functionality: no commits, pulls, pushes, or history access).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Usare GitHub Codespaces (consigliato per evitare grandi download locali)

- Crea un nuovo Codespace per questo repo tramite la [GitHub UI](https://github.com/codespaces).  

- Nel terminale del Codespace appena creato, esegui uno dei comandi di clone shallow/sparse sopra riportati per portare solo le cartelle delle lezioni di cui hai bisogno nello spazio di lavoro del Codespace.
- Opzionale: dopo il clone all'interno di Codespaces, rimuovi .git per recuperare spazio extra (vedi i comandi di rimozione sopra).
- Nota: Se preferisci aprire il repo direttamente in Codespaces (senza un clone extra), tieni presente che Codespaces costruirà l'ambiente devcontainer e potrebbe ancora fornire più di quanto ti serve. Clonare una copia superficiale all'interno di un Codespace nuovo ti dà più controllo sull'uso del disco.

#### Suggerimenti

- Sostituisci sempre l'URL del clone con il tuo fork se vuoi modificare/commitare.
- Se in seguito hai bisogno di più cronologia o file, puoi recuperarli o regolare sparse-checkout per includere cartelle aggiuntive.

## Esecuzione del codice

Questo corso offre una serie di Jupyter Notebooks che puoi eseguire per ottenere esperienza pratica nella creazione di AI Agents.

Gli esempi di codice utilizzano **Microsoft Agent Framework (MAF)** con il `AzureAIProjectAgentProvider`, che si connette a **Azure AI Agent Service V2** (la Responses API) tramite **Microsoft Foundry**.

Tutti i notebook Python sono etichettati `*-python-agent-framework.ipynb`.

## Requisiti

- Python 3.12+
  - **NOTE**: Se non hai Python3.12 installato, assicurati di installarlo. Quindi crea il tuo venv usando python3.12 per garantire che le versioni corrette vengano installate dal file requirements.txt.
  
    >Esempio

    Crea la directory del venv Python:

    ```bash|powershell
    python -m venv venv
    ```

    Then activate venv environment for:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Per i codici di esempio che usano .NET, assicurati di installare [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o successivo. Poi, verifica la versione del .NET SDK installata:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Necessario per l'autenticazione. Installa da [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Sottoscrizione Azure** — Per l'accesso a Microsoft Foundry e Azure AI Agent Service.
- **Progetto Microsoft Foundry** — Un progetto con un modello distribuito (ad es., `gpt-4o`). Vedi [Step 1](../../../00-course-setup) più sotto.

Abbiamo incluso un file `requirements.txt` nella root di questo repository che contiene tutti i pacchetti Python necessari per eseguire gli esempi di codice.

Puoi installarli eseguendo il seguente comando nel terminale nella root del repository:

```bash|powershell
pip install -r requirements.txt
```

Consigliamo di creare un ambiente virtuale Python per evitare conflitti e problemi.

## Configura VSCode

Assicurati di utilizzare la versione corretta di Python in VSCode.

![immagine](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configura Microsoft Foundry e Azure AI Agent Service

### Passo 1: Crea un progetto Microsoft Foundry

Hai bisogno di un **hub** e di un **progetto** Azure AI Foundry con un modello distribuito per eseguire i notebook.

1. Vai su [ai.azure.com](https://ai.azure.com) e accedi con il tuo account Azure.
2. Crea un **hub** (o usa uno esistente). Vedi: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. All'interno dell'hub, crea un **progetto**.
4. Distribuisci un modello (ad es., `gpt-4o`) da **Modelli + Endpoint** → **Distribuisci modello**.

### Passo 2: Recupera l'endpoint del progetto e il nome di deployment del modello

Dal tuo progetto nel portale Microsoft Foundry:

- **Project Endpoint** — Vai alla pagina **Panoramica** e copia l'URL dell'endpoint.

![Stringa di connessione del progetto](../../../translated_images/it/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Vai a **Modelli + Endpoint**, seleziona il tuo modello distribuito e annota il **Deployment name** (ad es., `gpt-4o`).

### Passo 3: Accedi ad Azure con `az login`

Tutti i notebook usano **`AzureCliCredential`** per l'autenticazione — nessuna chiave API da gestire. Questo richiede che tu sia autenticato tramite Azure CLI.

1. **Installa Azure CLI** se non l'hai già fatto: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Accedi** eseguendo:

    ```bash|powershell
    az login
    ```

    Or if you're in a remote/Codespace environment without a browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Seleziona la sottoscrizione** se richiesto — scegli quella che contiene il tuo progetto Foundry.

4. **Verifica** di essere autenticato:

    ```bash|powershell
    az account show
    ```

> **Perché `az login`?** I notebook si autenticano usando `AzureCliCredential` dal pacchetto `azure-identity`. Questo significa che la tua sessione Azure CLI fornisce le credenziali — nessuna chiave API o segreto nel tuo file `.env`. Questa è una [best practice di sicurezza](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

Apri `.env` e inserisci questi due valori:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variabile | Dove trovarla |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portale Foundry → il tuo progetto → pagina **Panoramica** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portale Foundry → **Modelli + Endpoint** → il nome del modello distribuito |

Questo è tutto per la maggior parte delle lezioni! I notebook si autenticheranno automaticamente tramite la tua sessione `az login`.

### Passo 5: Installa le dipendenze Python

```bash|powershell
pip install -r requirements.txt
```

Consigliamo di eseguire questo all'interno dell'ambiente virtuale che hai creato in precedenza.

## Configurazione aggiuntiva per la Lezione 5 (Agentic RAG)

La Lezione 5 utilizza **Azure AI Search** per la retrieval-augmented generation. Se prevedi di eseguire quella lezione, aggiungi queste variabili al tuo file `.env`:

| Variabile | Dove trovarla |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portale Azure → la tua risorsa **Azure AI Search** → **Panoramica** → URL |
| `AZURE_SEARCH_API_KEY` | Portale Azure → la tua risorsa **Azure AI Search** → **Impostazioni** → **Chiavi** → chiave amministratore primaria |

## Configurazione aggiuntiva per la Lezione 6 e la Lezione 8 (GitHub Models)

Alcuni notebook nelle lezioni 6 e 8 usano **GitHub Models** invece di Azure AI Foundry. Se prevedi di eseguire quegli esempi, aggiungi queste variabili al tuo file `.env`:

| Variabile | Dove trovarla |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## Configurazione aggiuntiva per la Lezione 8 (Bing Grounding Workflow)

Il notebook del workflow condizionale nella lezione 8 usa il **Bing grounding** tramite Azure AI Foundry. Se prevedi di eseguire quell'esempio, aggiungi questa variabile al tuo file `.env`:

| Variabile | Dove trovarla |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portale Azure AI Foundry → il tuo progetto → **Management** → **Connected resources** → la tua connessione Bing → copia l'ID della connessione |

## Risoluzione dei problemi

### Errori di verifica del certificato SSL su macOS

Se sei su macOS e incontri un errore come:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Questo è un problema noto con Python su macOS dove i certificati SSL di sistema non sono automaticamente considerati attendibili. Prova le seguenti soluzioni in ordine:

**Opzione 1: Esegui lo script Install Certificates di Python (consigliato)**

```bash
# Sostituisci 3.XX con la versione di Python installata (ad es., 3.12 o 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opzione 2: Usa `connection_verify=False` nel tuo notebook (solo per i notebook GitHub Models)**

Nel notebook della Lezione 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), è già incluso un workaround commentato. Decommenta `connection_verify=False` quando crei il client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Disabilita la verifica SSL se riscontri errori di certificato
)
```

> **⚠️ Avvertenza:** Disabilitare la verifica SSL (`connection_verify=False`) riduce la sicurezza saltando la validazione del certificato. Usa questo solo come soluzione temporanea in ambienti di sviluppo, mai in produzione.

**Opzione 3: Installa e usa `truststore`**

```bash
pip install truststore
```

Poi aggiungi quanto segue all'inizio del tuo notebook o script prima di effettuare qualsiasi chiamata di rete:

```python
import truststore
truststore.inject_into_ssl()
```

## Bloccato da qualche parte?

Se hai problemi nell'eseguire questa configurazione, entra nel <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord della community Azure AI</a> o <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">apri un'issue</a>.

## Lezione successiva

Ora sei pronto per eseguire il codice di questo corso. Buono studio nel mondo degli AI Agents! 

[Introduzione agli AI Agents e casi d'uso degli Agent](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Dichiarazione di non responsabilità:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica Co-op Translator (https://github.com/Azure/co-op-translator). Pur impegnandoci per l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua di origine deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->