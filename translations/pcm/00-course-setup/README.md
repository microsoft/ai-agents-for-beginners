# Setup Kọs

## Introdakshon

Dis lɛsɔn go tok how to run di kɔd sampl dem for dis kọs.

## Join Other Learna Dem and Get Help

Befor you start to clone your repo, join di [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) to get any help with setup, any question about di kọs, or to connect wit other learners.

## Clone or Fork dis Repo

To start, abeg clone or fork di GitHub Repository. Dis go make your own version of di kọs material so you fit run, test, and change di kɔd!

You fit do am by klik di link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork di repo</a>

Now you for get your own forked version of dis kọs for di link wey follow:

![Forked Repo](../../../translated_images/pcm/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (wey dem dey recommend for workshop / Codespaces)

  >Di full repository fit big (~3 GB) if you download full history and all files. If na only workshop you dey attend or na only some lesson folders you need, shallow clone (or sparse clone) go reduce di download by cutting history or skip blobs.

#### Quick shallow clone — minimal history, all files

Change `<your-username>` for di commands below wit your fork URL (or di upstream URL if you prefer).

To clone only di latest commit history (small download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

To clone a specific branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimal blobs + only selected folders

Dis one dey use partial clone and sparse-checkout (you need Git 2.25+ and modern Git wey fit do partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Go inside di repo folder:

```bash|powershell
cd ai-agents-for-beginners
```

Then tell wetin folders you want (example show two folders):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

After you don clone and check di files, if na only di files you want and you want free space (no git history), abeg delete di repository metadata (💀no fit take back — you go lose all Git functionality: no commits, pulls, pushes, or history access).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Using GitHub Codespaces (dem recommend am to avoid big local downloads)

- Create new Codespace for dis repo via di [GitHub UI](https://github.com/codespaces).  

- For terminal inside di new codespace, run one shallow/sparse clone command dem above to bring only di lesson folders you need inside di Codespace workspace.
- Optional: after cloning inside Codespaces, remove .git to free more space (see removal commands above).
- Note: If you prefer open di repo directly inside Codespaces (without extra clone), know say Codespaces go build di devcontainer environment and fit still provide more than you need. Cloning shallow copy inside fresh Codespace go give you more control on disk use.

#### Tips

- Always use your fork clone URL if you want to edit/commit.
- If you later want more history or files, you fit fetch them or adjust sparse-checkout to add more folders.

## How to Run Di Kɔd

Dis kọs get series of Jupyter Notebooks wey you fit run to get hands-on experience to build AI Agents.

Di kɔd samples dey use **Microsoft Agent Framework (MAF)** plus `FoundryChatClient`, wey connect to **Microsoft Foundry Agent Service V2** (di Responses API) through **Microsoft Foundry**.

All Python notebooks get label `*-python-agent-framework.ipynb`.

## Wetin You Need

- Python 3.12+
  - **NOTE**: If you never install Python3.12, abeg install am. Then create your venv with python3.12 to make sure say correct versions dey from the requirements.txt file.
  
    >Example

    Create Python venv directory:

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

- .NET 10+: For di sample codes dem wey dey use .NET, abeg install [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) or later. Then, check your installed .NET SDK version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — E dey necessary for authentication. Install from [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — For access to Microsoft Foundry and Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Project with deployed model (e.g., `gpt-5-mini`). See [Step 1](#step-1-create-microsoft-foundry-project) below.

We don put `requirements.txt` file for root of dis repository wey get all di necessary Python packages for run di kɔd samples.

You fit install dem by running di command wey follow inside your terminal at root of di repository:

```bash|powershell
pip install -r requirements.txt
```

We recommend say make you create Python virtual environment to avoid conflict and wahala.

## Setup VSCode

Make sure say you dey use di right version of Python for VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Set Up Microsoft Foundry and Microsoft Foundry Agent Service

### Step 1: Create Microsoft Foundry Project

You need Microsoft Foundry **hub** and **project** wey get deployed model to run di notebooks.

1. Go [ai.azure.com](https://ai.azure.com) and sign in wit your Azure account.
2. Create **hub** (or use existing one). See: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inside di hub, create **project**.
4. Deploy model (e.g., `gpt-5-mini`) from **Models + Endpoints** → **Deploy model**.

### Step 2: Find Your Project Endpoint and Model Deployment Name

From your project for Microsoft Foundry portal:

- **Project Endpoint** — Go **Overview** page and copy the endpoint URL.

![Project Connection String](../../../translated_images/pcm/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Go **Models + Endpoints**, select your deployed model, and note **Deployment name** (e.g., `gpt-5-mini`).

### Step 3: Sign in to Azure with `az login`

All notebooks dey use **`AzureCliCredential`** to authenticate — no API keys need to manage. You gats sign in via Azure CLI.

1. **Install Azure CLI** if you never do am: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Sign in** by running:

    ```bash|powershell
    az login
    ```

    Or if you dey remote/Codespace environment without browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Select your subscription** if dem ask — pick di one wey get your Foundry project.

4. **Check** say you sign in:

    ```bash|powershell
    az account show
    ```

> **Why `az login`?** Di notebooks dey authenticate with `AzureCliCredential` from `azure-identity` package. Dis mean say your Azure CLI session dey provide di creds — no API keys or secrets for your `.env` file. Na [security best practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Step 4: Create Your `.env` File

Copy di example file:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Open `.env` and fill these two values:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variable | Weh you fit find am |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → your project → **Overview** page |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → your deployed model's name |

Na so e be for most lessons! Di notebooks go authenticate automatically via your `az login` session.

### Step 5: Install Python Dependencies

```bash|powershell
pip install -r requirements.txt
```

We recommend say make you run dis inside di virtual environment wey you create before.

## Additional Setup for Lesson 5 (Agentic RAG)

Lesson 5 dey use **Azure AI Search** for retrieval-augmented generation. If you want run dat lesson, add these variables for your `.env` file:

| Variable | Weh you fit find am |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → your **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → your **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## Additional Setup for Lessons wey Call Azure OpenAI Directly (Lessons 6 and 8)

Some notebooks for lessons 6 and 8 dey call **Azure OpenAI** directly (using **Responses API**) instead of using Microsoft Foundry project. Dem sampl dem bin dey use GitHub Models, wey dem stop (retiring July 2026) and e no support Responses API. If you wan run dem sampl dem, add these variables to your `.env` file:

| Variable | Weh you fit find am |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → your **Azure OpenAI** resource → **Keys and Endpoint** → Endpoint (e.g. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Name of your deployed model (e.g. `gpt-5-mini`) wey support Responses API |
| `AZURE_OPENAI_API_KEY` | Optional — only if you dey use key-based auth instead of `az login` / Entra ID |

> Responses API dey use stable `/openai/v1/` endpoint, so no `api-version` need. Sign in with `az login` to use keyless Entra ID auth.

## Alternative Provider: MiniMax (OpenAI-Compatible)

[MiniMax](https://platform.minimaxi.com/) dey provide large-context models (up to 204K tokens) through OpenAI-compatible API. Since Microsoft Agent Framework's `OpenAIChatClient` dey work wit any OpenAI-compatible endpoint, you fit use MiniMax as drop-in alternative to Azure OpenAI or OpenAI.

Add these variables to your `.env` file:

| Variable | Weh you fit find am |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Use `https://api.minimax.io/v1` (default value) |
| `MINIMAX_MODEL_ID` | Model name to use (e.g., `MiniMax-M3`) |

**Example models**: `MiniMax-M3` (recommend am), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (faster responses). Model names and availability fit change over time, and access to model fit depend on your account or region — check [MiniMax Platform](https://platform.minimaxi.com/) for current list. If `MiniMax-M3` no dey your account, set `MINIMAX_MODEL_ID` to model wey you fit use (e.g. `MiniMax-M2.7`).

Di kɔd samples wey use `OpenAIChatClient` (e.g., Lesson 14 hotel booking workflow) go automatically detect and use your MiniMax config when `MINIMAX_API_KEY` set.

## Alternative Provider: Foundry Local (Run Models On-Device)

[Foundry Local](https://foundrylocal.ai) na lightweight runtime wey go download, manage, and serve language models **entirely on your own machine** through OpenAI-compatible API — no cloud, no Azure subscription, no API keys. E good for offline development, experiment without cloud cost, or keep data for your device.

Because Microsoft Agent Framework's `OpenAIChatClient` fit work wit any OpenAI-compatible endpoint, Foundry Local na local drop-in alternative to Azure OpenAI.

**1. Install Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Download and run model** (dis one go also start di local service):

```bash
foundry model list          # see di models wey dey available
foundry model run phi-4-mini
```

**3. Install di Python SDK** wey dem dey use to find di local endpoint:

```bash
pip install foundry-local-sdk
```

**4. Point Microsoft Agent Framework to your local model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Downloads (if e need am) and dey serve the model for inside machine, den e go find the endpoint/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # e.g. http://localhost:<port>/v1
    api_key=manager.api_key,        # always "not-required" for Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Note:** Foundry Local get OpenAI-compatible **Chat Completions** endpoint. Use am for local development and offline use. For full **Responses API** featureset (stateful conversations, deep tool orchestration, agent-style development), use **Azure OpenAI** or **Microsoft Foundry** project as dem show for lessons. See [Foundry Local documentation](https://foundrylocal.ai) for current model catalog and platform support.

## Additional Setup for Lesson 8 (Bing Grounding Workflow)


Di conditional workflow notebook for lesson 8 dey use **Bing grounding** thru Microsoft Foundry. If you wan run dat sample, add dis variable to your `.env` file:

| Variable | Where to find am |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → your project → **Management** → **Connected resources** → your Bing connection → copy di connection ID |

## Troubleshooting

### SSL Certificate Verification Errors on macOS

If you dey use macOS and you see error like dis:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dis na known wahala with Python for macOS wey di system SSL certificates no dey automatically trusted. Try dis solutions for dis order:

**Option 1: Run Python's Install Certificates script (na dis we recommend)**

```bash
# Change 3.XX to di Python version wey you don install (for example, 3.12 or 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Option 2: Use `connection_verify=False` for your notebook (na for GitHub Models notebooks only)**

For the Lesson 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), dem don put one commented-out workaround. Make you uncomment `connection_verify=False` when you dey create the client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Turn off SSL check if you see trouble with certificate
)
```

> **⚠️ Warning:** If you turn off SSL verification (`connection_verify=False`) e dey reduce security because e go skip certificate validation. Make you use am only as temporary workaround for development environment, no even try am for production.

**Option 3: Install and use `truststore`**

```bash
pip install truststore
```

Then add dis one for top of your notebook or script before you begin make any network calls:

```python
import truststore
truststore.inject_into_ssl()
```

## You Dey Stuck?

If any issue dey try run dis setup, just jump into our <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> or <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">create issue</a>.

## Next Lesson

You don ready to run di code for dis course. Happy to dey learn more about di world of AI Agents! 

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->