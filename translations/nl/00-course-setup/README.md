# Course Setup

## Introduction

This lesson will cover how to run the code samples of this course.

## Join Other Learners and Get Help

Before you begin cloning your repo, join the [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) to get any help with setup, any questions about the course, or to connect with other learners.

## Clone or Fork this Repo

To begin, please clone or fork the GitHub Repository. This will make your own version of the course material so that you can run, test, and tweak the code!

This can be done by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a>

You should now have your own forked version of this course in the following link:

![Geforkte repository](../../../translated_images/nl/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (recommended for workshop / Codespaces)

  >The full repository can be large (~3 GB) when you download full history and all files. If you're only attending the workshop or only need a few lesson folders, a shallow clone (or a sparse clone) avoids most of that download by truncating history and/or skipping blobs.

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
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Using GitHub Codespaces (recommended to avoid local large downloads)

- Create a new Codespace for this repo via the [GitHub UI](https://github.com/codespaces).  

- In the terminal of the newly created codespace, run one of the shallow/sparse clone commands above to bring only the lesson folders you need into the Codespace workspace.
- Optional: after cloning inside Codespaces, remove .git to reclaim extra space (see removal commands above).
- Note: If you prefer to open the repo directly in Codespaces (without an extra clone), be aware Codespaces will construct the devcontainer environment and may still provision more than you need. Cloning a shallow copy inside a fresh Codespace gives you more control over disk usage.

#### Tips

- Always replace the clone URL with your fork if you want to edit/commit.
- If you later need more history or files, you can fetch them or adjust sparse-checkout to include additional folders.

## Running the Code

This course offers a series of Jupyter Notebooks that you can run with to get hands-on experience building AI Agents.

The code samples use **Microsoft Agent Framework (MAF)** with the `AzureAIProjectAgentProvider`, which connects to **Azure AI Agent Service V2** (the Responses API) through **Microsoft Foundry**.

All Python notebooks are labelled `*-python-agent-framework.ipynb`.

## Requirements

- Python 3.12+
  - **OPMERKING**: If you don't have Python3.12 installed, ensure you install it.  Then create your venv using python3.12 to ensure the correct versions are installed from the requirements.txt file.
  
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

- .NET 10+: For the sample codes using .NET, ensure you install [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) or later. Then, check your installed .NET SDK version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Required for authentication. Install from [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — For access to Microsoft Foundry and Azure AI Agent Service.
- **Microsoft Foundry Project** — A project with a deployed model (e.g., `gpt-4o`). See [Step 1](../../../00-course-setup) below.

We have included a `requirements.txt` file in the root of this repository that contains all the required Python packages to run the code samples.

You can install them by running the following command in your terminal at the root of the repository:

```bash|powershell
pip install -r requirements.txt
```

We recommend creating a Python virtual environment to avoid any conflicts and issues.

## Setup VSCode

Make sure that you are using the right version of Python in VSCode.

![afbeelding](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Set Up Microsoft Foundry and Azure AI Agent Service

### Step 1: Create a Microsoft Foundry Project

You need an Azure AI Foundry **hub** and **project** with a deployed model to run the notebooks.

1. Go to [ai.azure.com](https://ai.azure.com) and sign in with your Azure account.
2. Create a **hub** (or use an existing one). See: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inside the hub, create a **project**.
4. Deploy a model (e.g., `gpt-4o`) from **Models + Endpoints** → **Deploy model**.

### Step 2: Retrieve Your Project Endpoint and Model Deployment Name

From your project in the Microsoft Foundry portal:

- **Project Endpoint** — Go to the **Overview** page and copy the endpoint URL.

![Project-eindpunt](../../../translated_images/nl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Go to **Models + Endpoints**, select your deployed model, and note the **Deployment name** (e.g., `gpt-4o`).

### Step 3: Sign in to Azure with `az login`

All notebooks use **`AzureCliCredential`** for authentication — no API keys to manage. This requires you to be signed in via the Azure CLI.

1. **Install the Azure CLI** if you haven't already: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Sign in** by running:

    ```bash|powershell
    az login
    ```

    Or if you're in a remote/Codespace environment without a browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Select your subscription** if prompted — choose the one containing your Foundry project.

4. **Verify** you're signed in:

    ```bash|powershell
    az account show
    ```

> **Why `az login`?** The notebooks authenticate using `AzureCliCredential` from the `azure-identity` package. This means your Azure CLI session provides the credentials — no API keys or secrets in your `.env` file. This is a [security best practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Step 4: Create Your `.env` File

Copy the example file:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Open `.env` and fill in these two values:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → your project → **Overview** page |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → your deployed model's name |

That's it for most lessons! The notebooks will authenticate automatically through your `az login` session.

### Step 5: Install Python Dependencies

```bash|powershell
pip install -r requirements.txt
```

We recommend running this inside the virtual environment you created earlier.

## Additional Setup for Lesson 5 (Agentic RAG)

Lesson 5 uses **Azure AI Search** for retrieval-augmented generation. If you plan to run that lesson, add these variables to your `.env` file:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → your **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → your **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## Additional Setup for Lesson 6 and Lesson 8 (GitHub Models)

Some notebooks in lessons 6 and 8 use **GitHub Models** instead of Azure AI Foundry. If you plan to run those samples, add these variables to your `.env` file:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## Additional Setup for Lesson 8 (Bing Grounding Workflow)

The conditional workflow notebook in lesson 8 uses **Bing grounding** via Azure AI Foundry. If you plan to run that sample, add this variable to your `.env` file:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → your project → **Management** → **Connected resources** → your Bing connection → copy the connection ID |

## Troubleshooting

### SSL Certificate Verification Errors on macOS

If you are on macOS and encounter an error like:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

This is a known issue with Python on macOS where the system SSL certificates are not automatically trusted. Try the following solutions in order:

**Option 1: Run Python's Install Certificates script (recommended)**

```bash
# Vervang 3.XX door de geïnstalleerde Python-versie (bijv. 3.12 of 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Option 2: Use `connection_verify=False` in your notebook (for GitHub Models notebooks only)**

In the Lesson 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), a commented-out workaround is already included. Uncomment `connection_verify=False` when creating the client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Schakel SSL-verificatie uit als u certificaatfouten tegenkomt
)
```

> **⚠️ Waarschuwing:** Disabling SSL verification (`connection_verify=False`) reduces security by skipping certificate validation. Use this only as a temporary workaround in development environments, never in production.

**Option 3: Install and use `truststore`**

```bash
pip install truststore
```

Then add the following at the top of your notebook or script before making any network calls:

```python
import truststore
truststore.inject_into_ssl()
```

## Stuck Somewhere?

If you have any issues running this setup, hop into our <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> or <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">create an issue</a>.

## Next Lesson

You are now ready to run the code for this course. Happy learning more about the world of AI Agents! 

[Introductie tot AI Agents en gebruiksscenario's](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we naar nauwkeurigheid streven, wees u ervan bewust dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal dient als de gezaghebbende bron te worden beschouwd. Voor kritieke informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->