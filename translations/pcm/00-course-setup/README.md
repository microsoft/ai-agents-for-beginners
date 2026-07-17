# Course Setup

## Introduction

Dis lesson go cover how to run di code samples for dis course.

## Join Other Learners and Get Help

Before you start to clone your repo, join di [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) to fit get any help with setup, any question about di course, or to connect wit oda learners.

## Clone or Fork this Repo

To start, abeg clone or fork di GitHub Repository. Dis one go make your own copy of di course material so that you fit run, test, and adjust di code!

You fit do dis by clicking di link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork di repo</a>

You suppose don get your own forked version of dis course for di link wey dey below:

![Forked Repo](../../../translated_images/pcm/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (recommended for workshop / Codespaces)

  >Di full repository fit be heavy (~3 GB) when you download full history and all files. If na only workshop you dey attend or you need just small lesson folders, shallow clone (or sparse clone) go reduce di download by cutting history and/or skipping some blobs.

#### Quick shallow clone — minimal history, all files

Change `<your-username>` for di commands below to your fork URL (or di upstream URL if na di one you prefer).

To clone only di latest commit history (small download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

To clone one specific branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — small blobs + selected folders only

Dis one dey use partial clone and sparse-checkout (you go need Git 2.25+ plus recommended new Git with partial clone support):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Enter inside di repo folder:

```bash|powershell
cd ai-agents-for-beginners
```

Then mark di folders wey you want (example below show two folders):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

After you don clone and check di files, if na only files you want and you want free space (no git history), abeg delete di repository metadata (💀no fit undo — you go lose all Git functionality: no commits, pulls, pushes, or history access).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Using GitHub Codespaces (recommended to avoid big downloads locally)

- Create new Codespace for dis repo using di [GitHub UI](https://github.com/codespaces).  

- For di terminal inside di new codespace, run one of di shallow/sparse clone commands wey dey above to only bring di lesson folders you want inside di Codespace workspace.
- Optional: afta cloning inside Codespaces, remove .git to get more space back (see removal commands wey dey above).
- Note: If you prefer open di repo direct inside Codespaces (without clone), remember say Codespaces go build di devcontainer environment and fit still install more than you need. Clone shallow copy inside fresh Codespace dey give you more control over di disk space.

#### Tips

- Always change di clone URL to your fork if you wan edit/commit.
- If later you need more history or files, you fit fetch dem or adjust sparse-checkout to add more folders.

## Running the Code

Dis course get series of Jupyter Notebooks wey you fit run to get hands-on experience building AI Agents.

Di code samples dey use **Microsoft Agent Framework (MAF)** with di `FoundryChatClient`, wey dey connect to **Microsoft Foundry Agent Service V2** (di Responses API) through **Microsoft Foundry**.

All Python notebooks get label `*-python-agent-framework.ipynb`.

## Requirements

- Python 3.12+ 
  - **NOTE**: If you never install Python3.12, abeg install am. Then create your venv using python3.12 to make sure say correct versions dey installed from di requirements.txt file.
  
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

- .NET 10+: For sample codes wey dey use .NET, abeg install [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) or newer. Then check your installed .NET SDK version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Na requirement for authentication. Install from [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — To get access to Microsoft Foundry and Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Project wey get deployed model (like `gpt-4.1-mini`). See [Step 1](#step-1-create-a-microsoft-foundry-project) below.

We don put one `requirements.txt` file for root of dis repo wey get all di Python packages wey you need to run di code samples.

You fit install dem by running di command below for your terminal for root of di repository:

```bash|powershell
pip install -r requirements.txt
```

We recommend say you create Python virtual environment make e no get conflicts or wahala.

## Setup VSCode

Make sure say you dey use di correct Python version inside VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Set Up Microsoft Foundry and Microsoft Foundry Agent Service

### Step 1: Create a Microsoft Foundry Project

You need Microsoft Foundry **hub** and **project** wey get deployed model to fit run di notebooks.

1. Go [ai.azure.com](https://ai.azure.com) sign in wit your Azure account.
2. Create **hub** (or use one wey you get already). See: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. For inside di hub, create **project**.
4. Deploy model (like `gpt-4.1-mini`) inside **Models + Endpoints** → **Deploy model**.

### Step 2: Find Your Project Endpoint and Model Deployment Name

From your project for Microsoft Foundry portal:

- **Project Endpoint** — Go to **Overview** page and copy di endpoint URL.

![Project Connection String](../../../translated_images/pcm/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Go **Models + Endpoints**, choose your deployed model, note di **Deployment name** (like `gpt-4.1-mini`).

### Step 3: Sign in to Azure with `az login`

All notebooks dey use **`AzureCliCredential`** for authentication — no API keys to worry about. This one require say you sign in with Azure CLI.

1. **Install Azure CLI** if you never install: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Sign in** by running:

    ```bash|powershell
    az login
    ```

    Or if na remote/Codespace environment without browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Choose your subscription** if dem ask — pick di one wey get your Foundry project.

4. **Make sure** say you don sign in:

    ```bash|powershell
    az account show
    ```

> **Why `az login`?** Di notebooks dey authenticate with `AzureCliCredential` from `azure-identity` package. Dis means your Azure CLI session dey provide credentials — no API keys or secrets dey `.env` file. Na [security best practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

Open `.env` and fill dis two values:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| Variable | Where to find am |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → your project → **Overview** page |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → your deployed model name |

That's it for most lessons! Di notebooks go authenticate automatically through your `az login` session.

### Step 5: Install Python Dependencies

```bash|powershell
pip install -r requirements.txt
```

We recommend make you run dis inside di virtual environment wey you create before.

## Additional Setup for Lesson 5 (Agentic RAG)

Lesson 5 dey use **Azure AI Search** for retrieval-augmented generation. If you plan to run dat lesson, add dis variables to your `.env` file:

| Variable | Where to find am |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → your **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → your **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## Additional Setup for Lessons wey Call Azure OpenAI Directly (Lessons 6 and 8)

Some notebooks for lessons 6 and 8 dey call **Azure OpenAI** directly (using **Responses API**) instead of pass through Microsoft Foundry project. Dis samples before dem dey use GitHub Models, but dem don retire am (July 2026) and e no support Responses API. If you wan run dis samples, add these variables inside your `.env` file:

| Variable | Where to find am |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → your **Azure OpenAI** resource → **Keys and Endpoint** → Endpoint (e.g., `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Di name of your deployed model (e.g., `gpt-4.1-mini`) wey support Responses API |
| `AZURE_OPENAI_API_KEY` | Optional — only if you dey use key-based auth instead of `az login` / Entra ID |

> Di Responses API dey use stable `/openai/v1/` endpoint, so no `api-version` needed. Sign in wit `az login` to use keyless Entra ID authentication.

## Alternative Provider: MiniMax (OpenAI-Compatible)

[MiniMax](https://platform.minimaxi.com/) dey provide large-context models (up to 204K tokens) through OpenAI-compatible API. Since Microsoft Agent Framework `OpenAIChatClient` fit work wit any OpenAI-compatible endpoint, you fit use MiniMax as drop-in alternative to Azure OpenAI or OpenAI.

Add dis variables to your `.env` file:

| Variable | Where to find am |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Use `https://api.minimax.io/v1` (default value) |
| `MINIMAX_MODEL_ID` | Model name to use (e.g., `MiniMax-M3`) |

**Example models**: `MiniMax-M3` (recommended), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (faster responses). Model names and availability fit change anytime, and access to model fit depend on your account or region — check [MiniMax Platform](https://platform.minimaxi.com/) for current list. If `MiniMax-M3` no dey your account, set `MINIMAX_MODEL_ID` to model wey you get access (e.g. `MiniMax-M2.7`).

Di code samples wey use `OpenAIChatClient` (like Lesson 14 hotel booking workflow) go automatically detect and use your MiniMax settings when `MINIMAX_API_KEY` dey set.

## Alternative Provider: Foundry Local (Run Models On-Device)

[Foundry Local](https://foundrylocal.ai) na lightweight runtime wey download, manage, and serve language models **completely on your own machine** through OpenAI-compatible API — no cloud, no Azure subscription, no API keys. E good if you wan develop offline, test without cloud cost, or keep data local.

Because Microsoft Agent Framework `OpenAIChatClient` fit work wit any OpenAI-compatible endpoint, Foundry Local na drop-in local alternative to Azure OpenAI.

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

**3. Install di Python SDK** to find di local endpoint:

```bash
pip install foundry-local-sdk
```

**4. Point Microsoft Agent Framework to your local model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Downloads (if needed) and serves de model for local, den find di endpoint/port.
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

> **Note:** Foundry Local get OpenAI-compatible **Chat Completions** endpoint. Use am for local development and offline scenarios. For full **Responses API** features (stateful conversations, tool orchestration, and agent-style development), use **Azure OpenAI** or **Microsoft Foundry** project as di lessons show. Check [Foundry Local documentation](https://foundrylocal.ai) for current model catalog and platform support.


## Additional Setup for Lesson 8 (Bing Grounding Workflow)

Di conditional workflow notebook wey dey for lesson 8 dey use **Bing grounding** through Microsoft Foundry. If you plan to run dat sample, add dis variable to your `.env` file:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → your project → **Management** → **Connected resources** → your Bing connection → copy the connection ID |

## Troubleshooting

### SSL Certificate Verification Errors on macOS

If you dey use macOS and error like dis show:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dis na known wahala with Python on macOS where system SSL certificates no dey automatically trusted. Try dis solutions dem one-by-one:

**Option 1: Run Python's Install Certificates script (recommended)**

```bash
# Change 3.XX to di Python version wey you don install (for example, 3.12 or 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Option 2: Use `connection_verify=False` for your notebook (for GitHub Models notebooks only)**

For Lesson 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), dem don already put one commented-out workaround. Uncomment `connection_verify=False` when you dey create the client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Turn off SSL check if you see certificate wahala
)
```

> **⚠️ Warning:** If you disable SSL verification (`connection_verify=False`), e go reduce security because e go skip certificate validation. Use dis one only as temporary workaround for development environment, no ever use am for production.

**Option 3: Install and use `truststore`**

```bash
pip install truststore
```

After dat, add dis one for top of your notebook or script before you start to make any network calls:

```python
import truststore
truststore.inject_into_ssl()
```

## Stuck Somewhere?

If you get any issue to run dis setup, join our <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> or <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">create an issue</a>.

## Next Lesson

You don ready to run di code for dis course now. Happy to learn more about di world of AI Agents! 

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->