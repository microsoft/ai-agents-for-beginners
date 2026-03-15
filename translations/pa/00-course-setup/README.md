# ਕੋਰਸ ਸੈਟਅਪ

## ਪਰਿਚਯ

ਇਹ ਪਾਠ ਦੱਸੇਗਾ ਕਿ ਇਸ ਕੋਰਸ ਦੇ ਕੋਡ ਸੈਂਪਲ ਕਿਵੇਂ ਚਲਾਏ ਜਾਂਦੇ ਹਨ।

## ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਜੁੜੋ ਅਤੇ ਮਦਦ ਪ੍ਰਾਪਤ ਕਰੋ

ਆਪਣਾ ਰਿਪੋ ਕਲੋਨ ਕਰਨਾ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਸੈਟਅਪ ਵਿੱਚ ਮਦਦ ਲਈ, ਕੋਰਸ ਬਾਰੇ ਕੋਈ ਵੀ ਪ੍ਰਸ਼ਨ ਪੁੱਛਣ ਲਈ ਜਾਂ ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਕਨੈਕਟ ਕਰਨ ਲਈ [AI Agents For Beginners Discord ਚੈਨਲ](https://aka.ms/ai-agents/discord) ਵਿੱਚ ਸ਼ਾਮਿਲ ਹੋਵੋ।

## ਇਸ ਰਿਪੋ ਨੂੰ ਕਲੋਨ ਜਾਂ ਫੋਰਕ ਕਰੋ

ਸ਼ੁਰੂਆਤ ਕਰਨ ਲਈ, ਕਿਰਪਾ ਕਰਕੇ GitHub ਰਿਪੋਜ਼ਿਟਰੀ ਨੂੰ ਕਲੋਨ ਜਾਂ ਫੋਰਕ ਕਰੋ। ਇਸ ਨਾਲ ਤੁਹਾਡੇ ਕੋਲ ਕੋਰਸ ਮਟੀਰੀਅਲ ਦਾ ਆਪਣਾ ਸੰਸਕਰਨ ਬਣ ਜਾਵੇਗਾ, ਤਾਂ ਜੋ ਤੁਸੀਂ ਕੋਡ ਚਲਾ ਸਕੋ, ਟੈਸਟ ਕਰ ਸਕੋ ਅਤੇ ਇਸ ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਕਰ ਸਕੋ!

This can be done by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ਰੀਪੋ ਫੋਰਕ ਕਰੋ</a>

You should now have your own forked version of this course in the following link:

![ਫੋਰਕ ਕੀਤਾ ਰਿਪੋ](../../../translated_images/pa/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (recommended for workshop / Codespaces)

  >ਪੂਰੀ ਰਿਪੋਜ਼ਿਟਰੀ ਸਮੱਗਰੀ (ਪੂਰਾ ਇਤਿਹਾਸ ਅਤੇ ਸਾਰੇ ਫ਼ਾਇਲਾਂ) ਡਾਊਨਲੋਡ ਕਰਨ 'ਤੇ ਵੱਡੀ (~3 GB) ਹੋ ਸਕਦੀ ਹੈ। ਜੇ ਤੁਸੀਂ ਸਿਰਫ ਵਰਕਸ਼ਾਪ ਵਿੱਚ ਭਾਗ ਲੈ ਰਹੇ ਹੋ ਜਾਂ ਸਿਰਫ ਕੁਝ ਪਾਠ ਫੋਲਡਰਾਂ ਦੀ ਲੋੜ ਹੈ, ਤਾਂ ਇੱਕ ਸ਼ੈਲੋ ਕਲੋਨ (ਜਾਂ ਸਪਾਰਸ ਕਲੋਨ) ਇਤਿਹਾਸ ਨੂੰ ਠੰਢਾ ਕਰਕੇ ਅਤੇ/ਜਾਂ ਬਲੌਬਸ ਨੂੰ ਸਕਿਪ ਕਰਕੇ ਜ਼ਿਆਦਾਤਰ ਡਾਊਨਲੋਡ ਤੋਂ ਬਚਾਉਂਦਾ ਹੈ।

#### Quick shallow clone — minimal history, all files

Replace `<your-username>` in the below commands with your fork URL (or the upstream URL if you prefer).

To clone only the latest commit history (small download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

To clone a specific branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimal blobs + only selected folders

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
# ਪਾਵਰਸ਼ੈਲ
Remove-Item -Recurse -Force .git
```

#### Using GitHub Codespaces (recommended to avoid local large downloads)

- Create a new Codespace for this repo via the [GitHub UI](https://github.com/codespaces).  

- In the terminal of the newly created codespace, run one of the shallow/sparse clone commands above to bring only the lesson folders you need into the Codespace workspace.
- Optional: after cloning inside Codespaces, remove .git to reclaim extra space (see removal commands above).
- Note: If you prefer to open the repo directly in Codespaces (without an extra clone), be aware Codespaces will construct the devcontainer environment and may still provision more than you need. Cloning a shallow copy inside a fresh Codespace gives you more control over disk usage.

#### ਟਿੱਪਸ

- ਹਮੇਸ਼ਾਂ ਕਲੋਨ URL ਨੂੰ ਆਪਣੀ ਫੋਰਕ ਨਾਲ ਬਦਲੋ ਜੇ ਤੁਸੀਂ ਸੰਪਾਦਨ/ਕਮਿਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ।
- ਜੇ ਬਾਅਦ ਵਿੱਚ ਤੁਹਾਨੂੰ ਹੋਰ ਇਤਿਹਾਸ ਜਾਂ ਫਾਈਲਾਂ ਦੀ ਲੋੜ ਹੋਵੇ, ਤਾਂ ਤੁਸੀਂ ਉਨ੍ਹਾਂ ਨੂੰ ਫੈਚ ਕਰ ਸਕਦੇ ਹੋ ਜਾਂ sparse-checkout ਨੂੰ ਅਨੁਕੂਲ ਕਰਕੇ ਵਾਧੂ ਫੋਲਡਰ ਸ਼ਾਮਿਲ ਕਰ ਸਕਦੇ ਹੋ।

## ਕੋਡ ਚਲਾਉਣਾ

ਇਹ ਕੋਰਸ ਕੁਝ Jupyter ਨੋਟਬੁੱਕਸ ਮੁਹੱਈਆ ਕਰਵਾਉਂਦਾ ਹੈ, ਜੋ ਤੁਹਾਨੂੰ AI ਏਜੰਟ ਬਣਾਉਣ ਵਿੱਚ ਹੈਂਡਸ-ਆਨ ਅਨੁਭਵ ਦੇਣ ਲਈ ਚਲਾਏ ਜਾ ਸਕਦੇ ਹਨ।

The code samples use **Microsoft Agent Framework (MAF)** with the `AzureAIProjectAgentProvider`, which connects to **Azure AI Agent Service V2** (the Responses API) through **Microsoft Foundry**.

All Python notebooks are labelled `*-python-agent-framework.ipynb`.

## ਲੋੜੀਂਦੀਆਂ ਚੀਜ਼ਾਂ

- Python 3.12+
  - **NOTE**: If you don't have Python3.12 installed, ensure you install it.  Then create your venv using python3.12 to ensure the correct versions are installed from the requirements.txt file.
  
    >ਉਦਾਹਰਨ

    Create Python venv directory:

    ```bash|powershell
    python -m venv venv
    ```

    Then activate venv environment for:

    ```bash
    # ਜ਼ੇਐਸਐਚ/ਬੈਸ਼
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: For the sample codes using .NET, ensure you install [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) or later. Then, check your installed .NET SDK version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Required for authentication. Install from [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — For access to Microsoft Foundry and Azure AI Agent Service.
- **Microsoft Foundry Project** — A project with a deployed model (e.g., `gpt-4o`). See [Step 1](../../../00-course-setup) below.

ਸਾਡੇ ਰਿਪੋ ਦੀ ਰੂਟ ਵਿੱਚ ਇੱਕ `requirements.txt` ਫਾਇਲ ਸ਼ਾਮਿਲ ਹੈ ਜਿਸ ਵਿੱਚ ਸਾਰੇ ਲਾਜ਼ਮੀ Python ਪੈਕੇਜ ਹਨ ਜੋ ਕੋਡ ਸੈਂਪਲ ਚਲਾਉਣ ਲਈ ਚਾਹੀਦੇ ਹਨ।

ਤੁਸੀਂ ਇਨ੍ਹਾਂ ਨੂੰ ਰਿਪੋ ਦੀ ਰੂਟ ਵਿੱਚ ਆਪਣੇ ਟਰਮੀਨਲ 'ਚ ਹੇਠ ਲਿਖੇ ਕਮਾਂਡ ਚਲਾ ਕੇ ਇੰਸਟਾਲ ਕਰ ਸਕਦੇ ਹੋ:

```bash|powershell
pip install -r requirements.txt
```

ਅਸੀਂ ਕਿਸੇ ਵੀ ਟਕਰਾਅ ਅਤੇ ਸਮੱਸਿਆਵਾਂ ਤੋਂ ਬਚਣ ਲਈ ਇੱਕ Python ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਬਣਾਉਣ ਦੀ ਸਿਫਾਰਿਸ਼ ਕਰਦੇ ਹਾਂ।

## VSCode ਸੈਟਅਪ

ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ VSCode ਵਿੱਚ ਸਹੀ ورਜ਼ਨ ਦਾ Python ਵਰਤ ਰਹੇ ਹੋ।

![ਚਿੱਤਰ](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ਅਤੇ Azure AI Agent Service ਸੈਟਅਪ ਕਰੋ

### ਕਦਮ 1: Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ

ਨੋਟਬੁੱਕ ਚਲਾਉਣ ਲਈ ਤੁਹਾਨੂੰ Azure AI Foundry ਵਿੱਚ ਇੱਕ **hub** ਅਤੇ **project** ਦੀ ਲੋੜ ਹੈ ਜਿਸ ਵਿੱਚ ਇੱਕ ਡਿਪਲੋਯ ਕੀਤੀ ਹੋਈ ਮਾਡਲ ਹੋਵੇ।

1. [ai.azure.com](https://ai.azure.com) 'ਤੇ ਜਾਓ ਅਤੇ ਆਪਣੇ Azure ਖਾਤੇ ਨਾਲ ਸਾਈਨ ਇਨ ਕਰੋ।
2. ਇੱਕ **hub** ਬਣਾਉ (ਜਾਂ ਮੌਜੂਦਾ ਹਬ ਦੀ ਵਰਤੋਂ ਕਰੋ)। ਵੇਖੋ: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. ਹਬ ਦੇ ਅੰਦਰ ਇੱਕ **project** ਬਣਾਓ।
4. **Models + Endpoints** → **Deploy model** ਤੋਂ ਇੱਕ ਮਾਡਲ (ਉਦਾਹਰਨ ਲਈ `gpt-4o`) ਡਿਪਲੋਇ ਕਰੋ।

### ਕਦਮ 2: ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਐਂਡਪੁਇੰਟ ਅਤੇ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਨਾਂ ਪ੍ਰਾਪਤ ਕਰੋ

Microsoft Foundry ਪੋਰਟਲ ਵਿੱਚ ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਤੋਂ:

- **Project Endpoint** — **Overview** ਪੇਜ 'ਤੇ ਜਾਓ ਅਤੇ endpoint URL ਕੌਪੀ ਕਰੋ।

![ਪ੍ਰੋਜੈਕਟ ਕਨੈਕਸ਼ਨ ਸਟਰਿੰਗ](../../../translated_images/pa/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** 'ਤੇ ਜਾਓ, ਆਪਣੇ ਡਿਪਲੋਯ ਕੀਤੇ ਮਾਡਲ ਨੂੰ ਚੁਣੋ ਅਤੇ **Deployment name** ਨੋਟ ਕਰੋ (ਉਦਾਹਰਨ ਲਈ `gpt-4o`)।

### ਕਦਮ 3: `az login` ਨਾਲ Azure ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ

ਸਾਰੇ ਨੋਟਬੁੱਕਸ authentication ਲਈ **`AzureCliCredential`** ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ — ਕੋਈ API ਕੀਜ਼ ਮੈਨੇਜ ਕਰਨ ਦੀ ਲੋੜ ਨਹੀਂ। ਇਸ ਲਈ ਤੁਹਾਨੂੰ Azure CLI ਰਾਹੀਂ ਸਾਈਨ ਇਨ ਹੋਣਾ ਲਾਜ਼ਮੀ ਹੈ।

1. **Install the Azure CLI** ਜੇ ਤੁਸੀਂ ਪਹਿਲਾਂ ਨਹੀਂ ਕੀਤਾ: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Sign in** ਕਰਨ ਲਈ ਰਨ ਕਰੋ:

    ```bash|powershell
    az login
    ```

    Or if you're in a remote/Codespace environment without a browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Select your subscription** ਜੇ ਪ੍ਰਾਂਪਟ ਕੀਤਾ ਜਾਵੇ — ਉਸੇ ਨੂੰ ਚੁਣੋ ਜਿਸ ਵਿੱਚ ਤੁਹਾਡਾ Foundry ਪ੍ਰੋਜੈਕਟ ਹੈ।

4. **Verify** ਕਿ ਤੁਸੀਂ ਸਾਈਨ ਇਨ ਹੋ: 

    ```bash|powershell
    az account show
    ```

> **ਕਿਉਂ `az login`?** ਨੋਟਬੁੱਕਸ `azure-identity` ਪੈਕੇਜ ਤੋਂ `AzureCliCredential` ਦੀ ਵਰਤੋਂ ਕਰਕੇ authenticate ਕਰਦੇ ਹਨ। ਇਸਦਾ ਮਤਲਬ ਇਹ ਹੈ ਕਿ ਤੁਹਾਡਾ Azure CLI ਸੈਸ਼ਨ ਹੀ ਪ੍ਰਮਾਣਿਕਤਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ — ਤੁਹਾਡੇ `.env` ਫਾਇਲ ਵਿੱਚ ਕੋਈ API ਕੀਜ ਜਾਂ ਸਿਕ੍ਰੇਟ ਨਹੀਂ। ਇਹ ਇੱਕ [ਸੁਰੱਖਿਆ ਦੇ ਸਭ ਤੋਂ ਚੰਗੇ ਅਭਿਆਸ](https://learn.microsoft.com/azure/developer/ai/keyless-connections) ਹੈ।

### ਕਦਮ 4: ਆਪਣੀ `.env` ਫਾਇਲ ਬਣਾਓ

Example ਫਾਇਲ ਨੂੰ ਕਾਪੀ ਕਰੋ:

```bash
# zsh/ਬੈਸ਼
cp .env.example .env
```

```powershell
# ਪਾਵਰਸ਼ੈੱਲ
Copy-Item .env.example .env
```

`.env` ਖੋਲ੍ਹੋ ਅਤੇ ਇਹ ਦੋ ਮੁੱਲ ਭਰੋ:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → your project → **Overview** page |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → your deployed model's name |

ਇਹ ਜ਼ਿਆਦਾਤਰ ਪਾਠਾਂ ਲਈ ਕਾਫੀ ਹੈ! ਨੋਟਬੁੱਕਸ ਆਪਣੇ `az login` ਸੈਸ਼ਨ ਰਾਹੀਂ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ authenticate ਕਰ ਲੈਣਗੇ।

### ਕਦਮ 5: Python Dependencies ਇੰਸਟਾਲ ਕਰੋ

```bash|powershell
pip install -r requirements.txt
```

ਅਸੀਂ ਸਿਫਾਰਿਸ਼ ਕਰਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ ਇਹ ਪਹਿਲਾਂ ਬਣਾਏ ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਦੇ ਅੰਦਰ ਚਲਾਓ।

## Lesson 5 (Agentic RAG) ਲਈ ਵਾਧੂ ਸੈਟਅਪ

Lesson 5 retrieval-augmented generation ਲਈ **Azure AI Search** ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। ਜੇ ਤੁਸੀਂ ਉਹ ਪਾਠ ਚਲਾਉਣ ਦਾ ਯੋਜਨਾ ਬਣਾਉਂਦੇ ਹੋ, ਤਾਂ ਆਪਣੀ `.env` ਫਾਇਲ ਵਿੱਚ ਇਹ ਵੈਰੀਏਬਲ ਜੋੜੋ:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → your **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → your **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## Lesson 6 ਅਤੇ Lesson 8 (GitHub Models) ਲਈ ਵਾਧੂ ਸੈਟਅਪ

ਕਈ ਨੋਟਬੁੱਕਸ ਜੋ Lesson 6 ਅਤੇ 8 ਵਿੱਚ ਹਨ, ਉਹ Azure AI Foundry ਦੀ ਬਜਾਏ **GitHub Models** ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ। ਜੇ ਤੁਸੀਂ ਉਹ ਸੈਂਪਲ ਚਲਾਉਣ ਦਾ ਯੋਜਨਾ ਬਣਾਉਂਦੇ ਹੋ, ਤਾਂ ਆਪਣੀ `.env` ਫਾਇਲ ਵਿੱਚ ਇਹ ਵੈਰੀਏਬਲ ਸ਼ਾਮਿਲ ਕਰੋ:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## Lesson 8 (Bing Grounding Workflow) ਲਈ ਵਾਧੂ ਸੈਟਅਪ

Lesson 8 ਦਾ conditional workflow ਨੋਟਬੁੱਕ Azure AI Foundry ਰਾਹੀਂ **Bing grounding** ਵਰਤਦਾ ਹੈ। ਜੇ ਤੁਸੀਂ ਉਹ ਸੈਂਪਲ ਚਲਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਆਪਣੀ `.env` ਫਾਇਲ ਵਿੱਚ ਇਹ ਵੈਰੀਏਬਲ ਜੋੜੋ:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → your project → **Management** → **Connected resources** → your Bing connection → copy the connection ID |

## ਸਮੱਸਿਆ ਨਿਪਟਾਰਾ

### macOS 'ਤੇ SSL ਸਰਟੀਫਿਕੇਟ ਵੈਰੀਫਿਕੇਸ਼ਨ ਦੀਆਂ ਗਲਤੀਆਂ

ਜੇ ਤੁਸੀਂ macOS 'ਤੇ ਹੋ ਅਤੇ ਇਸ ਤਰ੍ਹਾਂ ਦੀ ਗਲਤੀ ਆਉਂਦੀ ਹੈ:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

ਇਹ Python ਦੇ macOS 'ਤੇ ਜਾਣੀ-ਪਹਚਾਨੀ ਸਮੱਸਿਆ ਹੈ ਜਿੱਥੇ ਸਿਸਟਮ SSL ਸਰਟੀਫਿਕੇਟ ਆਪੇ ਤੋਂ ਟਰੱਸਟ ਨਹੀਂ ਮੰਨੇ ਜਾਂਦੇ। ਕ੍ਰਮਵਾਰ ਹੇਠ ਲਿਖੇ ਹੱਲ ਅਜ਼ਮਾਓ:

**Option 1: Run Python's Install Certificates script (recommended)**

```bash
# ਆਪਣੇ ਇੰਸਟਾਲ ਹੋਏ Python ਵਰਜ਼ਨ ਨਾਲ 3.XX ਨੂੰ ਬਦਲੋ (ਉਦਾਹਰਨ ਵੱਜੋਂ, 3.12 ਜਾਂ 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Option 2: Use `connection_verify=False` in your notebook (for GitHub Models notebooks only)**

Lesson 6 ਨੋਟਬੁੱਕ (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) ਵਿੱਚ ਇੱਕ commented-out ਵਰਕਅਰਾਉਂਡ ਪਹਿਲਾਂ ਤੋਂ ਸ਼ਾਮਿਲ ਹੈ। client ਬਣਾਉਂਦੇ ਸਮੇਂ `connection_verify=False` ਨੂੰ uncomment ਕਰੋ:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # ਜੇ ਤੁਹਾਨੂੰ ਸਰਟੀਫਿਕੇਟ ਸਮੱਸਿਆਵਾਂ ਆਉਂਦੀਆਂ ਹਨ ਤਾਂ SSL ਜਾਂਚ ਬੰਦ ਕਰੋ
)
```

> **⚠️ ਚੇਤਾਵਨੀ:** SSL ਵੈਰੀਫਿਕੇਸ਼ਨ ਬੰਦ ਕਰਨਾ (`connection_verify=False`) ਸਰਟੀਫਿਕੇਟ ਵੈਧਤਾ ਨੂੰ ਸਕਿਪ ਕਰਕੇ ਸੁਰੱਖਿਆ ਨੂੰ ਘਟਾਉਂਦਾ ਹੈ। ਇਹ ਸਿਰਫ ਵਿਕਾਸ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਅਸਥਾਈ ਵਰਕਅਰਾਉਂਡ ਵਜੋਂ ਵਰਤੋ, ਪ੍ਰੋਡਕਸ਼ਨ ਵਿੱਚ ਕਦੇ ਵੀ ਨਹੀਂ।

**Option 3: Install and use `truststore`**

```bash
pip install truststore
```

ਫਿਰ ਆਪਣੇ ਨੋਟਬੁੱਕ ਜਾਂ ਸਕ੍ਰਿਪਟ ਦੇ ਸ਼ੁਰੂ ਵਿੱਚ, ਕਿਸੇ ਵੀ ਨੈਟਵਰਕ ਕਾਲ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਹੇਠ ਲਿਖਿਆ ਸ਼ਾਮਿਲ ਕਰੋ:

```python
import truststore
truststore.inject_into_ssl()
```

## ਫਸ ਗਏ ਹੋ?

ਜੇ ਇਸ ਸੈਟਅਪ ਨੂੰ ਚਲਾਉਣ ਸਮੇਂ ਤੁਹਾਨੂੰ ਕੋਈ ਸਮੱਸਿਆ ਆਉਂਦੀ ਹੈ, ਤਾਂ ਸਾਡੇ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> ਵਿੱਚ ਸ਼ਾਮਿਲ ਹੋਵੋ ਜਾਂ <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ਇੱਕ ਇਸ਼ੂ ਬਣਾਓ</a>।

## ਅਗਲਾ ਪਾਠ

ਤੁਸੀਂ ਹੁਣ ਇਸ ਕੋਰਸ ਲਈ ਕੋਡ ਚਲਾਉਣ ਲਈ ਤਿਆਰ ਹੋ। AI ਏਜੰਟਸ ਦੀ ਦੁਨੀਆ ਬਾਰੇ ਹੋਰ ਸਿੱਖਣ ਲਈ ਖੁਸ਼ ਰਹੋ!

[AI ਏਜੰਟਸ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਉਪਯੋਗ ਕੇਸ](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ਜ਼ਿੰਮੇਵਾਰੀ ਤੋਂ ਇਨਕਾਰ:
ਇਹ ਦਸਤਾਵੇਜ਼ ਏ.ਆਈ. ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਸ਼ੁੱਧਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸ਼ੁੱਧਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਗੰਭੀਰ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ-ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->