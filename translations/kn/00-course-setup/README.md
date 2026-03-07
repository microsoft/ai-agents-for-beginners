# ಕೋರ್ಸ್ ಸೆಟ್‌ಅಪ್

## ಪರಿಚಯ

ಈ ಪಾಠವು ಈ ಕೋರ್ಸ್‌ನ ಕೋಡ್ ಉದಾಹರಣೆಗಳನ್ನು ಹೇಗೆ ಚಲಿಸಲು ಎಂಬುದನ್ನು ವಿವರಿಸುತ್ತದೆ.

## ಇತರ ಕಲಿಕಾರರೊಂದಿಗೆ ಸೇರಿ ಮತ್ತು ಸಹಾಯ ಪಡೆಯಿರಿ

ನಿಮ್ಮ ರೆಪೋವನ್ನು ಕ್ಲೋನ್ ಮಾಡಲು ಪ್ರಾರಂಭಿಸುವ ಮೊದಲು, ಸೆಟ್‌ಅಪ್‌ಗೆ ಸಂಬಂಧಿಸಿದ ಸಹಾಯ ಪಡೆಯಲು, ಕೋರ್ಸ್‌ ಕುರಿತು ಯಾವುದೇ ಪ್ರಶ್ನೆಗಳಿಗೆ ಅಥವಾ ಇತರ ಕಲಿಕಾರರೊಂದಿಗೆ ಸಂಪರ್ಕಕ್ಕೆ [AI Agents For Beginners Discord ಚಾನೆಲ್](https://aka.ms/ai-agents/discord) ಸೇರಿ.

## ಈ ರೆಪೋವನ್ನು ಕ್ಲೋನ್ ಅಥವಾ ಫೋರ್ಕ್ ಮಾಡಿ

ಆರಂಭಿಸಲು, ದಯವಿಟ್ಟು GitHub ರೆಪೋವನ್ನು ಕ್ಲೋನ್ ಅಥವಾ ಫೋರ್ಕ್ ಮಾಡಿ. ಇದರಿಂದ ಈ ಕೋರ್ಸ್ ಸಾಮಗ್ರಿಯ ನಿಮ್ಮದೇ ಸಂಚಿಕೆ ಸೃಷ್ಟಿಯಾಗುತ್ತದೆ, ಅದನ್ನು ನೀವು ಚಾಲನೆ ಮಾಡಬಹುದು, ಪರೀಕ್ಷಿಸಬಹುದು ಮತ್ತು ಕೋಡ್ ಅನ್ನು ತಿದ್ದುಪಡಿ ಮಾಡಬಹುದು!

This can be done by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ರೆಪೋ ಫೋರ್ಕ್ ಮಾಡಿ</a>

You should now have your own forked version of this course in the following link:

![ಫೋರ್ಕ್ ಮಾಡಿದ ರೆಪೋ](../../../translated_images/kn/forked-repo.33f27ca1901baa6a.webp)

### ಶ್ಯಾಲೋ ಕ್ಲೋನ್ (ಕಾರ್ಯಾಗಾರ / Codespaces ಗಾಗಿ ಶಿಫಾರಸು)

  > ಸಂಪೂರ್ಣ ರೆಪೋವು ಸಂಪೂರ್ಣ ಇತಿಹಾಸ ಮತ್ತು ಎಲ್ಲಾ ಫೈಲ್‌ಗಳನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡುವಾಗ ದೊಡ್ಡದಾಗಿರಬಹುದು (~3 GB). ನೀವು ಕೇವಲ ಕಾರ್ಯಾಗಾರಕ್ಕೆ ಹಾಜರಾಗುತ್ತಿರುವುದಾದರೆ ಅಥವಾ ಕೆಲವು ಪಾಠ ಫೋಲ್ಡರ್‌ಗಳೇ ಬೇಕಾದರೆ, ಶ್ಯಾಲೋ ಕ್ಲೋನ್ (ಅಥವಾ ಸ್ಪಾರ್ಸ್ ಕ್ಲೋನ್) ಇತಿಹಾಸವನ್ನು ಕೊಂಚ ಕಡಿತ ಮಾಡುವುದು ಮತ್ತು/ಅಥವಾ ಬ್ಲಾಬ್‌ಗಳನ್ನು ಬಿಟ್ಟುಹಾಕುವುದರಿಂದ ಹೆಚ್ಚಿನ ಡೌನ್‌ಲೋಡ್‌ನ್ನು ತಪ್ಪಿಸುತ್ತದೆ.

#### ತ್ವರಿತ ಶ್ಯಾಲೋ ಕ್ಲೋನ್ — ಕನಿಷ್ಠ ಇತಿಹಾಸ, ಎಲ್ಲಾ ಫೈಲ್‌ಗಳು

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
# ಪವರ್‌ಶೆಲ್
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ಬಳಕೆ (ಪ್ರಾದೇಶಿಕವಾಗಿ ದೊಡ್ಡ ಡೌನ್‌ಲೋಡ್‌ಗಳನ್ನು ತಪ್ಪಿಸಲು ಶಿಫಾರಸು)

- Create a new Codespace for this repo via the [GitHub UI](https://github.com/codespaces).  

- In the terminal of the newly created codespace, run one of the shallow/sparse clone commands above to bring only the lesson folders you need into the Codespace workspace.
- Optional: after cloning inside Codespaces, remove .git to reclaim extra space (see removal commands above).
- Note: If you prefer to open the repo directly in Codespaces (without an extra clone), be aware Codespaces will construct the devcontainer environment and may still provision more than you need. Cloning a shallow copy inside a fresh Codespace gives you more control over disk usage.

#### ಸಲಹೆಗಳು

- Always replace the clone URL with your fork if you want to edit/commit.
- If you later need more history or files, you can fetch them or adjust sparse-checkout to include additional folders.

## ಕೋಡ್ ಚಲಾಯಿಸುವುದು

This course offers a series of Jupyter Notebooks that you can run with to get hands-on experience building AI Agents.

The code samples use **Microsoft Agent Framework (MAF)** with the `AzureAIProjectAgentProvider`, which connects to **Azure AI Agent Service V2** (the Responses API) through **Microsoft Foundry**.

All Python notebooks are labelled `*-python-agent-framework.ipynb`.

## ಅಗತ್ಯಗಳು

- Python 3.12+
  - **ಗಮನಿಸಿ**: ನೀವು Python3.12 ಹೊಂದಿರದಿದ್ದರೆ, ದಯವಿಟ್ಟು ಅದನ್ನು ಸ್ಥಾಪಿಸಿ.  ನಂತರ requirements.txt ಫೈಲ್‌ನಿಂದ ಸರಿಯಾದ ಆವೃತ್ತಿಗಳನ್ನು ಸ್ಥಾಪಿಸಲು python3.12 ಬಳಸಿ ನಿಮ್ಮ venv ರಚಿಸಿ.
  
    >ಉದಾಹರಣೆ

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

- .NET 10+: For the sample codes using .NET, ensure you install [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) or later. Then, check your installed .NET SDK version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — ಪ್ರಾಮಾಣೀಕರಣಕ್ಕಾಗಿ ಅಗತ್ಯ. Install from [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Microsoft Foundry ಮತ್ತು Azure AI Agent Service ಗೆ ಪ್ರವೇಶಕ್ಕಾಗಿ.
- **Microsoft Foundry Project** — ನಿಯೋಜಿತ ಮಾದರಿಯೊಂದಿಗೆ ಇರುವ ಪ್ರಾಜೆಕ್ಟ್ (ಉದಾ., `gpt-4o`). See [Step 1](../../../00-course-setup) below.

We have included a `requirements.txt` file in the root of this repository that contains all the required Python packages to run the code samples.

You can install them by running the following command in your terminal at the root of the repository:

```bash|powershell
pip install -r requirements.txt
```

We recommend creating a Python virtual environment to avoid any conflicts and issues.

## VSCode ಸೆಟ್‌ಅಪ್

Make sure that you are using the right version of Python in VSCode.

![ಚಿತ್ರ](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ಮತ್ತು Azure AI Agent Service ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿ

### ಹಂತ 1: Microsoft Foundry ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸಿ

You need an Azure AI Foundry **hub** and **project** with a deployed model to run the notebooks.

1. Go to [ai.azure.com](https://ai.azure.com) and sign in with your Azure account.
2. Create a **hub** (or use an existing one). See: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inside the hub, create a **project**.
4. Deploy a model (e.g., `gpt-4o`) from **Models + Endpoints** → **Deploy model**.

### ಹಂತ 2: ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಮತ್ತು ಮಾದರಿ ನಿಯೋಜನೆ ಹೆಸರು ಪಡೆದಿರಿ

From your project in the Microsoft Foundry portal:

- **Project Endpoint** — **Overview** ಪುಟಕ್ಕೆ ಹೋಗಿ ಮತ್ತು ಎಂಡ್‌ಪಾಯಿಂಟ್ URL ನ್ನು ನಕಲಿಸಿ.

![ಪ್ರಾಜೆಕ್ಟ್ ಸಂಪರ್ಕ ಸ್ಟ್ರಿಂಗ್](../../../translated_images/kn/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** ಗೆ ಹೋಗಿ, ನಿಮ್ಮ ನಿಯೋಜಿತ ಮಾದರಿಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ, ಮತ್ತು **Deployment name** ಅನ್ನು ಗಮನಿಸಿ (ಉದಾ., `gpt-4o`).

### ಹಂತ 3: `az login` ಬಳಸಿ Azure ಗೆ ಸೈನ್ ಇನ್ ಮಾಡಿ

All notebooks use **`AzureCliCredential`** for authentication — no API keys to manage. This requires you to be signed in via the Azure CLI.

1. **Azure CLI ಅನ್ನು ಸ್ಥಾಪಿಸಿ** if you haven't already: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **ಸೈನ್ ಇನ್** ಮಾಡಲು ಕೆಳಗಿನ ಕಮಾಂಡ್ ಚಾಲನೆ ಮಾಡಿ:

    ```bash|powershell
    az login
    ```

    Or if you're in a remote/Codespace environment without a browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **ನಿಮ್ಮ ಸಬ್‌ಸ್ಕ್ರಿಪ್ಷನ್ ಆಯ್ಕೆಮಾಡಿ** if prompted — choose the one containing your Foundry project.

4. **ಸत्यಾಪಿಸಿ** you're signed in:

    ```bash|powershell
    az account show
    ```

> **ಏಕೆ `az login`?** ನೋಟ್ಬುಕ್‌ಗಳು `azure-identity` ಪ್ಯಾಕೇಜ್‌ನಿಂದ `AzureCliCredential` ಅನ್ನು ಬಳಸಿಕೊಂಡು ಪ್ರಾಮಾಣೀಕರಣ ಮಾಡುತ್ತವೆ. ಇದರ ಅರ್ಥ ನಿಮ್ಮ Azure CLI ಸೆಷನ್ ಕ್ರೆಡೆನ್ಶಿಯಲ್ಸ್ ಅನ್ನು ನೀಡುತ್ತದೆ — ನಿಮ್ಮ `.env` ಫೈಲ್‌ನಲ್ಲಿ ಯಾವುದೇ API ಕೀಗಳು ಅಥವಾ ರಹಸ್ಯಗಳ ಅಗತ್ಯವಿಲ್ಲ. This is a [security best practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### ಹಂತ 4: ನಿಮ್ಮ `.env` ಫೈಲ್ ರಚಿಸಿ

Copy the example file:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# ಪವರ್‌ಶೆಲ್
Copy-Item .env.example .env
```

Open `.env` and fill in these two values:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| ಚರ | ಎಲ್ಲಿ ಕಂಡುಹಿಡಿಯುವುದು |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ → **Overview** ಪುಟ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → ನಿಮ್ಮ ನಿಯೋಜಿತ ಮಾದರಿಯ ಹೆಸರು |

That's it for most lessons! The notebooks will authenticate automatically through your `az login` session.

### ಹಂತ 5: Python ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

```bash|powershell
pip install -r requirements.txt
```

We recommend running this inside the virtual environment you created earlier.

## ಪಾಠ 5 (ಏಜೆಂಟಿಕ್ RAG) ಗಾಗಿ ಹೆಚ್ಚುವರಿ ಸೆಟ್ ಅಪ್

Lesson 5 uses **Azure AI Search** for retrieval-augmented generation. If you plan to run that lesson, add these variables to your `.env` file:

| ಚರ | ಎಲ್ಲಿ ಕಂಡುಹಿಡಿಯುವುದು |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure ಪೋರ್ಟಲ್ → ನಿಮ್ಮ **Azure AI Search** ಸಂಪನ್ಮೂಲ → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure ಪೋರ್ಟಲ್ → ನಿಮ್ಮ **Azure AI Search** ಸಂಪನ್ಮೂಲ → **Settings** → **Keys** → ಪ್ರಾಥಮಿಕ ಆಡಳಿತ ಕೀ |

## ಪಾಠ 6 ಮತ್ತು ಪಾಠ 8 (GitHub Models) ಗಾಗಿ ಹೆಚ್ಚುವರಿ ಸೆಟ್ ಅಪ್

Some notebooks in lessons 6 and 8 use **GitHub Models** instead of Azure AI Foundry. If you plan to run those samples, add these variables to your `.env` file:

| ಚರ | ಎಲ್ಲಿ ಕಂಡುಹಿಡಿಯುವುದು |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## ಪಾಠ 8 (Bing Grounding Workflow) ಗಾಗಿ ಹೆಚ್ಚುವರಿ ಸೆಟ್ ಅಪ್

The conditional workflow notebook in lesson 8 uses **Bing grounding** via Azure AI Foundry. If you plan to run that sample, add this variable to your `.env` file:

| ಚರ | ಎಲ್ಲಿ ಕಂಡುಹಿಡಿಯುವುದು |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → your project → **Management** → **Connected resources** → your Bing connection → copy the connection ID |

## ಸಮಸ್ಯೆ ಪರಿಹಾರ

### macOS ನಲ್ಲಿ SSL ಪ್ರಮಾಣಪತ್ರ ಪರಿಶೀಲನೆ ದೋಷಗಳು

If you are on macOS and encounter an error like:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

This is a known issue with Python on macOS where the system SSL certificates are not automatically trusted. Try the following solutions in order:

**ಆಯ್ಕೆ 1: Python ನ Install Certificates ಸ್ಕ್ರಿಪ್ಟ್ ಅನ್ನು ಚಲಾಯಿಸಿ (ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ)**

```bash
# 3.XX ಅನ್ನು ನಿಮ್ಮ ಸ್ಥಾಪಿಸಿರುವ Python ಆವೃತ್ತಿಯಿಂದ ಬದಲಿಸಿ (ಉದಾಹರಣೆಗೆ, 3.12 ಅಥವಾ 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ಆಯ್ಕೆ 2: Use `connection_verify=False` in your notebook (for GitHub Models notebooks only)**

In the Lesson 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), a commented-out workaround is already included. Uncomment `connection_verify=False` when creating the client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # ನೀವು ಪ್ರಮಾಣಪತ್ರ ದೋಷಗಳನ್ನು ಎದುರಿಸಿದರೆ SSL ಪರಿಶೀಲನೆಯನ್ನು ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಿ
)
```

> **⚠️ Warning:** Disabling SSL verification (`connection_verify=False`) reduces security by skipping certificate validation. Use this only as a temporary workaround in development environments, never in production.

**ಆಯ್ಕೆ 3: `truststore` ಅನ್ನು ಸ್ಥಾಪಿಸಿ ಮತ್ತು ಬಳಸಿ**

```bash
pip install truststore
```

Then add the following at the top of your notebook or script before making any network calls:

```python
import truststore
truststore.inject_into_ssl()
```

## ಎಲ್ಲಿಾದರೂ ಅಡಕವಿದ್ದೀರಾ?

If you have any issues running this setup, hop into our <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> or <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ಇಶ್ಯೂ ರಚಿಸಿ</a>.

## ಮುಂದಿನ ಪಾಠ

You are now ready to run the code for this course. ಈ ಕೋರ್ಸ್‌ನ ಕೋಡ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಲು ನೀವು ಸಿದ್ಧರಾಗಿದ್ದೀರಿ. AI ಏಜೆಂಟ್‌ಗಳ ವಿಶ್ವದ ಬಗ್ಗೆ ಇನ್ನಷ್ಟು ತಿಳಿದುಕೊಳ್ಳಲು ಶುಭವಾಗಲಿ!

[AI ಏಜೆಂಟ್‌ಗಳ ಪರಿಚಯ ಮತ್ತು ಏಜೆಂಟ್ ಉಪಯೋಗದ ಸಂದರ್ಭಗಳು](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಜವಾಬ್ದಾರಿ ನಿರಾಕರಣೆ:
ಈ ದಾಖಲೆ ಅನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನuvadಿಸಲಾಗಿದೆ. ನಿಖರತೆಗೆ ನಾವು ಪ್ರಯತ್ನಿಸುವುದರೂ ಸಹ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಮರ್ಪಕತೆಗಳು ಇರಬಹುದಾಗಿದೆ ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿ ಇರುವ ಮೂಲ ದಾಖಲೆನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. この ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಗ್ರಹಿಕೆಗಳು ಅಥವಾ ತಪ್ಪಾದ ವ್ಯಾಖ್ಯಾನದಿಗಾಗಿ ನಾವು ಜವಾಬ್ದಾರಿಯಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->