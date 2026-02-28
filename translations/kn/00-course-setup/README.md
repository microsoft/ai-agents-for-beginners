# ಕೋರ್ಸ್ ಸೆಟಪ್

## ಪರಿಚಯ

ಈ ಪಾಠವು ಈ ಕೋರ್ಸ್‌ನ ಕೋಡ್ ಉದಾಹರಣೆಗಳನ್ನು ಹೇಗೆ ಚಾಲನೆ ಮಾಡಬೇಕು ಎಂಬುದನ್ನು ಒಳಗೊಂಡಿರುತ್ತದೆ.

## ಇತರ ಅಧ್ಯಯನಾರ್ಥಿಗಳೊಂದಿಗೆ ಸೇರಿ ಸಹಾಯ ಪಡೆಯಿರಿ

ನೀವು ನಿಮ್ಮ ರೆಪೊವನ್ನು ಕ್ಲೋನ್ ಮಾಡಬೇಕೆಂಬುದನ್ನು ಪ್ರಾರಂಭಿಸುವ ಮೊದಲು, ಸೆಟ್ ಅಪ್ ಕುರಿತು ಯಾವುದೇ ಸಹಾಯಕ್ಕೋರ್ವ, ಕೋರ್ಸ್ ಕುರಿತು ಯಾವುದೇ ಪ್ರಶ್ನೆಗಳಿಗೋ ಅಥವಾ ಇತರ ಅಧ್ಯಯನಾರ್ಥಿಗಳೊಂದಿಗೆ ಸಂಪರ್ಕ ಸಾಧಿಸಲು [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) ಅನ್ನು ಸಂಪರ್ಕಿಸಿ.

## ಈ ರೆಪೊವನ್ನು ಕ್ಲೋನ್ ಅಥವಾ ಫೋರ್ಕ್ ಮಾಡಿ

ಆರಂಭಿಸಲು, ದಯವಿಟ್ಟು GitHub ರೆಪೊಸಿಟರಿ ಅನ್ನು ಕ್ಲೋನ್ ಅಥವಾ ಫೋರ್ಕ್ ಮಾಡಿ. ಇದರಿಂದ ಕೋರ್ಸ್ ಸಾಮಗ್ರಿಯ ನಿಮ್ಮ ಸ್ವಂತ ಪ್ರತಿಯನ್ನು ಹೊಂದಿರುತ್ತೀರಿ ಹಾಗೂ ನೀವು ಕೋಡ್ ಅನ್ನು ಓಡಿಸಲು, ಪರೀಕ್ಷೆ ಮಾಡಲು ಮತ್ತು ಸವಿರಿಸುವುದಕ್ಕೆ ಸಾಧ್ಯವಾಗುತ್ತದೆ!

This can be done by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ರೆಪೊ ಅನ್ನು ಫೋರ್ಕ್ ಮಾಡಿ</a>

You should now have your own forked version of this course in the following link:

![ಫೋರ್ಕ್ ಮಾಡಿದ ರೆಪೊ](../../../translated_images/kn/forked-repo.33f27ca1901baa6a.webp)

### ಶಲ್ಲೋ ಕ್ಲೋನ್ (ವಾರ್ಕ್‌ಶಾಪ್ / Codespaces ಗೆ ಶಿಫಾರಸು)

  > ಸಂಪೂರ್ಣ ರೆಪೊಸಿಟರಿ ಪೂರ್ಣ ಇತಿಹಾಸ ಮತ್ತು ಎಲ್ಲಾ ಫೈಲ್‌ಗಳನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿದಾಗ ದೊಡ್ಡದಾಗಿರಬಹುದು (~3 GB). ನೀವು ಕೇವಲ ವರ್ಕ್‌ಶಾಪ್‌ನಲ್ಲಿ ಪಾಲ್ಗೊಳ್ಳುತ್ತಿದ್ದೀರಾ ಅಥವಾ ಕೆಲವು ಪಾಠ ಫೋಲ್ಡರ್‌ಗಳಿಗೆ ಮಾತ್ರ ಅಗತ್ಯವಿದ್ದರೆ, ಶಲ್ಲೋ ಕ್ಲೋನ್ (ಅಥವಾ ಸ್ಪಾರ್ಸ್ ಕ್ಲೋನ್) ಇತಿಹಾಸವನ್ನು ಕಟ್ ಮಾಡಿ ಮತ್ತು/ಅಥವಾ ಬ್ಲಾಬ್‌ಗಳನ್ನು ಬಿಟ್ಟುಬಿಡುವುದರಿಂದ ಬಹುಭಾಗದ ಡೌನ್‌ಲೋಡ್ ತಪ್ಪಿಸುತ್ತದೆ.

#### ವೇಗದ ಶಲ್ಲೋ ಕ್ಲೋನ್ — ಕನಿಷ್ಠ ಇತಿಹಾಸ, ಎಲ್ಲಾ ಫೈಲ್‌ಗಳು

Replace `<your-username>` in the below commands with your fork URL (or the upstream URL if you prefer).

To clone only the latest commit history (small download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

To clone a specific branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### ಭಾಗಶಃ (ಸ್ಪಾರ್ಸ್) ಕ್ಲೋನ್ — ಕಡಿಮೆ ಬ್ಲಾಬ್‌ಗಳು + ಆಯ್ದ ಫೋಲ್ಡರ್‌ಗಳು ಮಾತ್ರ

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
# zsh/ಬ್ಯಾಶ್
rm -rf .git
```

```powershell
# ಪವರ್‌ಶೆಲ್
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ಉಪಯೋಗಿಸುವುದು (ಸ್ಥಳೀಯ ದೊಡ್ಡ ಡೌನ್‌ಲೋಡ್ ತಪ್ಪಿಸಲು ಶಿಫಾರಸು)

- Create a new Codespace for this repo via the [GitHub UI](https://github.com/codespaces).  

- In the terminal of the newly created codespace, run one of the shallow/sparse clone commands above to bring only the lesson folders you need into the Codespace workspace.
- Optional: after cloning inside Codespaces, remove .git to reclaim extra space (see removal commands above).
- Note: If you prefer to open the repo directly in Codespaces (without an extra clone), be aware Codespaces will construct the devcontainer environment and may still provision more than you need. Cloning a shallow copy inside a fresh Codespace gives you more control over disk usage.

#### ಟಿಪ್ಸ್

- ಎಡಿಟ್/ಕಮಿಟ್ ಮಾಡಲು ನೀವು ನಿಮ್ಮ ಫೋರ್ಕ್ ಅನ್ನು ಬಳಸಬೇಕಾದರೆ ಯಾವಾಗಲೂ ಕ್ಲೋನ್ URL ಅನ್ನು ನಿಮ್ಮ ಫೋರ್ಕ್ URL ಗೆ ಬದಲಾಯಿಸಿ.
- ನಂತರ ನಿಮಗೆ ಹೆಚ್ಚು ಇತಿಹಾಸ ಅಥವಾ ಫೈಲ್‌ಗಳು ಬೇಕಾದರೆ, ಅವುಗಳನ್ನು ಫೆಚ್ ಮಾಡಲು ಅಥವಾ ಹೆಚ್ಚುವರಿ ಫೋಲ್ಡರ್‌ಗಳನ್ನು ಸೇರಿಸಲು sparse-checkout ಅನ್ನು ಸಡಿಲಿಸಬಹುದು.

## ಕೋಡ್ ನಡಿಸುವುದು

ಈ ಕೋರ್ಸಿನಲ್ಲಿ ಕೈಗೂಂಡು ಅನುಭವಕ್ಕಾಗಿ ನೀವು Jupyter Notebooks ಸರಣಿಯನ್ನು ಓಡಿಸಬಹುದಾಗಿದೆ.

ಕೋಡ್ ಉದಾಹರಣೆಗಳು **Microsoft Agent Framework (MAF)** ಅನ್ನು `AzureAIProjectAgentProvider` ಜೊತೆಗೆ ಬಳಸುತ್ತವೆ, ಇದು **Microsoft Foundry** ಮುಖಾಂತರ **Azure AI Agent Service V2** (Responses API) ಗೆ ಸಂಪರ್ಕ ಹೊಂದಿಸುತ್ತದೆ.

ಎಲ್ಲಾ Python ನೋಟ್‌ಬುಕ್‌ಗಳನ್ನು `*-python-agent-framework.ipynb` ಎಂದು ಲೇಬೆಲ್ ಮಾಡಲಾಗಿದೆ.

## ಅಗತ್ಯಗಳು

- Python 3.12+
  - **NOTE**: ನೀವು Python3.12 ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡದೆ ಇದ್ದರೆ, ದಯವಿಟ್ಟು ಅದನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ. ನಂತರ ಸರಿಯಾದ ಆವೃತ್ತಿಗಳಿಗೆ ಸುರಕ್ಷಿತವಾಗಿ requirements.txt ಫೈಲ್‌ನಲ್ಲಿ ಸೂಚಿಸಿದ ಪ್ಯಾಕೇಜ್‌ಗಳನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಲು python3.12 ಬಳಸಿ ನಿಮ್ಮ venv ಅನ್ನು ರಚಿಸಿ.
  
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

- **Azure CLI** — ಪ್ರಾಮಾಣೀಕರಣಕ್ಕಾಗಿ ಅಗತ್ಯ. ಇನ್‌ಸ್ಟಾಲ್‌ ಮಾಡಲು [aka.ms/installazurecli](https://aka.ms/installazurecli) ವೀಕ್ಷಿಸಿ.
- **Azure Subscription** — Microsoft Foundry ಮತ್ತು Azure AI Agent Service ಗೆ ಪ್ರವೇಶಕ್ಕಾಗಿ.
- **Microsoft Foundry Project** — ನೋಟ್‌ಬುಕ್‌ಗಳನ್ನು ಚಾಲನೆ ಮಾಡಲು ನಿಯೋಜಿಸಿದ ಮಾದರಿಯೊಂದಿಗೆ ಇರುವ ಒಂದು ಪ್ರಾಜೆಕ್ಟ್ (ಉದಾಹರಣೆಗೆ, `gpt-4o`). ಕೆಳಗಿನ [Step 1](../../../00-course-setup) ನೋಡಿ.

ನಮ್ಮ ರೆಪೊರೊಟ್ರಿಯಲ್ಲಿ ರೂಟ್‌ನಲ್ಲಿರುವ `requirements.txt` ಫೈಲ್‌ನಲ್ಲಿ ಎಲ್ಲಾ ಅಗತ್ಯ Python ಪ್ಯಾಕೇಜ್‌ಗಳನ್ನು ಸೇರಿಸಲಾಗಿದೆ.

ನೀವು ಅವುಗಳನ್ನು ರೆಪೊನ ರೂಟ್ ನಲ್ಲಿ ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಓಡಿಸುವ ಮೂಲಕ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಬಹುದು:

```bash|powershell
pip install -r requirements.txt
```

ಕೋನ್‌ಫ್ಲಿಕ್ಟ್‌ಗಳು ಮತ್ತು ಸಮಸ್ಯೆಗಳನ್ನು ತಪ್ಪಿಸಲು Python ವರ್ಚ್ಯೂಅಲ್ ಎನ್ವಿರಾನ್‌ಮೆಂಟ್ ರಚಿಸುವುದು ನಾವು ಶಿಫಾರಸು ಮಾಡುತ್ತೇವೆ.

## VSCode ಸೆಟಪ್

VSCode ನಲ್ಲಿ ನೀವು ಸರಿಯಾದ Python ಆವೃತ್ತಿ ಬಳಸುತ್ತಿದ್ದೀರಾ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಂಡು работы.

![ಚಿತ್ರ](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry ಮತ್ತು Azure AI Agent Service ಸೆಟಪ್ ಮಾಡಿ

### ಹಂತ 1: Microsoft Foundry ಪ್ರಾಜೆಕ್ಟ್ ರಚನೆ ಮಾಡಿ

ನಿಮ್ಮ ನೋಟ್‌ಬುಕ್‌ಗಳನ್ನು ಓಡಿಸಲು ನಿಯೋಜಿತ ಮಾದರಿಯೊಂದಿಗೆ Azure AI Foundry **ಹಬ್** ಮತ್ತು **ಪ್ರಾಜೆಕ್ಟ್** ಅಗತ್ಯವಿದೆ.

1. [ai.azure.com](https://ai.azure.com) ಗೆ ಹೋಗಿ ಮತ್ತು ನಿಮ್ಮ Azure ಖಾತೆಯಿಂದ ಸೈನ್ ಇನ್ ಮಾಡಿ.
2. **ಹಬ್** ರಚಿಸಿ (ಅಥವಾ ಈಗಿರುವುದನ್ನು ಬಳಸಿಕೊಳ್ಳಿ). ನೋಡಿ: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. ಹಬ್‌ನ ಒಳಗೆ **ಪ್ರಾಜೆಕ್ಟ್** ರಚಿಸಿ.
4. **Models + Endpoints** → **Deploy model** ನಿಂದ ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸಿ (ಉದಾ., `gpt-4o`).

### ಹಂತ 2: ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಮತ್ತು ಮಾದರಿ ನಿಯೋಜನೆ ಹೆಸರು ಪಡೆಯಿರಿ

Microsoft Foundry ಪೋರ್ಟಲ್‌ನಲ್ಲಿರುವ ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನಿಂದ:

- **ಪ್ರಾಜೆಕ್ಟ್ ಎಂಡ್‌ಪಾಯಿಂಟ್** — **Overview** ಪುಟಕ್ಕೆ ಹೋಗಿ ಮತ್ತು ಎಂಡ್‌ಪಾಯಿಂಟ್ URL ನ್ನು ನಕಲಿಸಿ.

![Project Connection String](../../../translated_images/kn/project-endpoint.8cf04c9975bbfbf1.webp)

- **ಮಾದರಿ ನಿಯೋಜನೆ ಹೆಸರು** — **Models + Endpoints** ಗೆ ಹೋಗಿ, ನಿಮ್ಮ ನಿಯೋಜಿಸಿದ ಮಾದರಿಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ ಮತ್ತು **Deployment name** (ಉದಾ., `gpt-4o`) ಅನ್ನು ಗಮನಿಸಿ.

### ಹಂತ 3: `az login` ಮೂಲಕ Azure ಗೆ ಸೈನ್ ಇನ್ ಆಗಿ

ಎಲ್ಲಾ ನೋಟ್‌ಬುಕ್‌ಗಳು ಪ್ರಾಮಾಣೀಕರಣಕ್ಕಾಗಿ **`AzureCliCredential`** ಅನ್ನು ಬಳಸುತ್ತವೆ — ನಿರ್ವಹಣೆಗೆ ಯಾವುದೇ API ಕೀಗಳನ್ನು ಅಗತ್ಯವಿಲ್ಲ. ಇದಕ್ಕಾಗಿ ನೀವು Azure CLI ಮೂಲಕ ಸೈನ್ ಇನ್ ಆಗಿರಬೇಕು.

1. **Azure CLI ಅನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ** যদি ನೀವು ಇನ್ನೂ ಮಾಡಿಲ್ಲ: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **ಸೈನ್ ಇನ್** ಮಾಡಲು ಕೆಳಗಿನ ಆಜ್ಞೆ ಓಡಿಸಿ:

    ```bash|powershell
    az login
    ```

    Or if you're in a remote/Codespace environment without a browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **ನಿಮ್ಮ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್ ಆಯ್ಕೆಮಾಡಿ** ಪ್ರಾಂಪ್ಟ್ ಆಗಿದ್ರೆ — ನಿಮ್ಮ Foundry ಪ್ರಾಜೆಕ್ಟ್ ಒಳಗೊಂಡಿರುವುದನ್ನು ಆಯ್ಕೆಮಾಡಿ.

4. **ನೀವು ಸೈನ್ ಇನ್ ಆಗಿದ್ದೀರಾ ಎಂದು ಪರಿಶೀಲಿಸಿ**:

    ```bash|powershell
    az account show
    ```

> **ಏಕೆ `az login`?** ನೋಟ್‌ಬುಕ್‌ಗಳು `azure-identity` ಪ್ಯಾಕೇಜಿನ `AzureCliCredential` ಅನ್ನು ಬಳಸಿಕೊಂಡು ಪ್ರಾಮಾಣೀಕರಿಸುತ್ತವೆ. ಇದರಿಂದ ನಿಮ್ಮ Azure CLI ಸೆಷನ್ ಕ್ರೆಡೆನ್ಶಿಯಲ್ಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ — `.env` ಫೈಲ್‌ನಲ್ಲಿ ಯಾವುದೇ API ಕೀಗಳು ಅಥವಾ ರಹಸ್ಯಗಳ ಅವಶ್ಯಕತೆ ಇಲ್ಲ. ಇದು ಒಂದು [ಸುರಕ್ಷತಾ ಉತ್ತಮ ಅಭ್ಯಾಸ](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### ಹಂತ 4: ನಿಮ್ಮ `.env` ಫೈಲ್ ರಚಿಸಿ

ಉದಾಹರಣಾ ಫೈಲ್ ನಕಲಿಸಿ:

```bash
# ಝೆಡ್‌ಎಸ್‌ಎಚ್/ಬ್ಯಾಶ್
cp .env.example .env
```

```powershell
# ಪವರ್‌ಶೆಲ್
Copy-Item .env.example .env
```

`.env` ಓಪಿ ಮಾಡಿ ಈ երկու ಮೌಲ್ಯಗಳನ್ನು ತುಂಬಿ:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ → **Overview** ಪುಟ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → ನಿಮ್ಮ ನಿಯೋಜಿತ ಮಾದರಿಯ ಹೆಸರು |

ಅದೇ ಸಾಕು ಬಹುತೇಕ ಪಾಠಗಳಿಗೆ! ನೋಟ್‌ಬುಕ್‌ಗಳು ನಿಮ್ಮ `az login` ಸೆಷನ್ ಮೂಲಕ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪ್ರಾಮಾಣೀಕರಿಸುತ್ತವೆ.

### ಹಂತ 5: Python ನಿರ್ಭರತೆಗಳನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ

```bash|powershell
pip install -r requirements.txt
```

ನಾವು ಶಿಫಾರಸು ಮಾಡುತ್ತೇವೆ ಈ ಆಜ್ಞೆಯನ್ನು ನೀವು ಹಿಂದಿನದಾಗಿ ರಚಿಸಿರುವ ವರ್ಚುಯಲ್ ಎನ್ವಿರಾನ್‌ಮೆಂಟ್ ಒಳಗೆ ಓಡಿಸುವುದು.

## ಪಾಠ 5 (Agentic RAG) ಗಾಗಿ ಹೆಚ್ಚುವರಿ ಸೆಟಪ್

ಪಾಠ 5 ನಲ್ಲಿ **Azure AI Search** ಅನ್ನು retrieval-augmented generation ಗಾಗಿ ಬಳಸಲಾಗುತ್ತದೆ. ನೀವು ಆ ಪಾಠವನ್ನು ಓಡಿಸುವ ಉದ್ದೇಶವಿದ್ದರೆ, ಈ ಮೌಲ್ಯಗಳನ್ನು ನಿಮ್ಮ `.env` ಫೈಲ್‌ಗೆ ಸೇರಿಸಿ:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → ನಿಮ್ಮ **Azure AI Search** ಸಂಪನ್ಮೂಲ → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → ನಿಮ್ಮ **Azure AI Search** ಸಂಪನ್ಮೂಲ → **Settings** → **Keys** → primary admin key |

## ಪಾಠ 6 ಮತ್ತು ಪಾಠ 8 (GitHub Models) ಗಾಗಿ ಹೆಚ್ಚುವರಿ ಸೆಟಪ್

ಪಾಠ 6 ಮತ್ತು 8 ರ ಕೆಲವು ನೋಟ್‌ಬುಕ್‌ಗಳು Azure AI Foundry ಬದಲು **GitHub Models** ಅನ್ನು ಬಳಸುತ್ತವೆ. ನೀವು ಆ ಉದಾಹರಣೆಗಳನ್ನು ಓಡಿಸುವ ಯೋಜನೆ ಇದ್ದರೆ, ಈ ಮೌಲ್ಯಗಳನ್ನು ನಿಮ್ಮ `.env` ಫೈಲ್‌ಗೆ ಸೇರಿಸಿ:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## ಪಾಠ 8 (Bing Grounding Workflow) ಗಾಗಿ ಹೆಚ್ಚುವರಿ ಸೆಟಪ್

ಪಾಠ 8 ರಲ್ಲಿ conditional workflow ನೋಟ್‌ಬುಕ್‌ವು Azure AI Foundry ಮೂಲಕ **Bing grounding** ಅನ್ನು ಬಳಸುತ್ತದೆ. ನೀವು ಆ ಉದಾಹರಣೆಯನ್ನು ಓಡಿಸಲು ಯೋಜಿಸುತ್ತಿದ್ದರೆ, ಈ ಮೌಲ್ಯವನ್ನು ನಿಮ್ಮ `.env` ಫೈಲ್‌ಗೆ ಸೇರಿಸಿ:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ → **Management** → **Connected resources** → ನಿಮ್ಮ Bing ಸಂಪರ್ಕ → ಸಂಪರ್ಕ ID ನಕಲಿಸಿ |

## ಸಮಸ್ಯೆ ಪರಿಹಾರ

### macOS ಮೇಲೆ SSL ಪ್ರಮಾಣಪತ್ರ ಪರಿಶೀಲನೆ ದೋಷಗಳು

ನೀವು macOS ಬಳಸುತ್ತಿರುವಾಗ ಕೆಳಗಿನಂತಹ ದೋಷವು ಎದುರಿಸಬಹುದಾಗಿದೆ:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

ಇದು macOS ಮೇಲೆ Python ನೊಂದಿಗೆ ಪರಿಚಿತ ಸಮಸ್ಯೆ — ವ್ಯವಸ್ಥೆಯ SSL ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ವಿಶ್ವಾಸಾರ್ಹವೆಂದು ಗುರುತಿಸಲಾಗುವುದಿಲ್ಲ. ಕೆಳಗಿನ ಪರಿಹಾರಗಳನ್ನು ಕ್ರಮವಾಗಿ ಪ್ರಯತ್ನಿಸಿ:

**ಆಯ್ಕೆ 1: Python ನ Install Certificates ಸ್ಕ್ರಿಪ್ಟ್ (ಶಿಫಾರಸು ಮಾಡಿದೆ) ಅನ್ನು ಓಡಿಸಿ**

```bash
# 3.XX ಅನ್ನು ನಿಮ್ಮ ಸ್ಥಾಪಿಸಲಾದ Python ಆವೃತ್ತಿಗೆ (ಉದಾ., 3.12 ಅಥವಾ 3.13) ಬದಲಾಯಿಸಿ:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ಆಯ್ಕೆ 2: ನಿಮ್ಮ ನೋಟ್‌ಬುಕ್‌ನಲ್ಲಿ `connection_verify=False` ಉಪಯೋಗಿಸಿ (GitHub Models ನೋಟ್‌ಬುಕ್‌ಗಳಿಗೆ ಮಾತ್ರ)**

Lesson 6 ನೋಟ್‌ಬುಕ್ ನಲ್ಲಿ (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), ಕಾಮೆಂಟ್ ಮಾಡಿರುವ ಕಾರ್ಯಚರಣಾ ಪರಿಹಾರ ಈಗಾಗಲೇ ಸೇರಿಸಲಾಗಿದೆ. ಕ್ಲೈಂಟ್ ರಚಿಸುವಾಗ `connection_verify=False` ಅನಕಾಮೆಂಟ್ ಮಾಡಿ:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # ನೀವು ಪ್ರಮಾಣಪತ್ರ ದೋಷಗಳನ್ನು ಎದುರಿಸಿದರೆ SSL ಪರಿಶೀಲನೆಯನ್ನು ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಿ
)
```

> **⚠️ ಎಚ್ಚರಿಕೆ:** SSL ಪರಿಶೀಲನೆಯನ್ನು ನಿಷ್ಕ್ರಿಯಗೊಳಿಸುವುದು (`connection_verify=False`) ವಿಶ್ವಾಸಾರ್ಹತೆಯನ್ನು ಕಡಿಮೆಗೊಳಿಸುತ್ತದೆ ಏಕೆಂದ್ರೆ ಪ್ರಮಾಣಪತ್ರ ಪರಿಶೀಲನೆಯನ್ನು ತಪ್ಪಿಸುತ್ತದೆ. ಇದು ಡೆವಲಪ್‌ಮೆಂಟ್ ಪರಿಸರದಲ್ಲಿ ತಾತ್ಕಾಲಿಕ ಪರಿಹಾರವಾಗಿ ಮಾತ್ರ ಬಳಸಿರಿ, ಉತ್ಪಾದನೆಯಲ್ಲಿ ಎಂದಿಗೂ ಬಳಸಬೇಡಿ.

**ಆಯ್ಕೆ 3: `truststore` ಅನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ ಮತ್ತು ಬಳಸಿ**

```bash
pip install truststore
```

ನಂತರ ನಿಮ್ಮ ನೋಟ್‌ಬುಕ್ ಅಥವಾ ಸ್ಕ್ರಿಪ್ಟ್‌ನ ಮೇಲೆಗಡೆಯಿನಲ್ಲಿ ಯಾವುದೇ ನೆಟ್ವರ್ಕ್ ಕರೆಗಳನ್ನು ಮಾಡಹೋಗುವ ಮೊದಲು ಕೆಳಗಿನನ್ನು ಸೇರಿಸಿ:

```python
import truststore
truststore.inject_into_ssl()
```

## ಯಾವುದೆಡೆ ಸಿಲುಕಿದ್ದೀರಾ?

ಈ ಸೆಟಪ್ ಓಡಿಸಲು ಯಾವುದೇ ಸಮಸ್ಯೆಗಳು ಬಂದರೆ, ನಮ್ಮ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> ಗೆ ಹಪ್ಪಿಕೊಂಡು ಬನ್ನಿ ಅಥವಾ <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ಒಂದು ಇಶ್ಯೂ ರಚಿಸಿ</a>.

## ಮುಂದಿನ ಪಾಠ

ನೀವು ಈಗ ಈ ಕೋರ್ಸಿನ ಕೋಡ್ ಅನ್ನು ಓಡಿಸಲು ಸಿದ್ಧರಿದ್ದೀರಿ. AI ಏಜೆಂಟ್‌ಗಳ ಜಗತ್ತಿನ ಬಗ್ಗೆ ಇನ್ನೂ ಹೆಚ್ಚು ತಿಳಿತುಕೊಳ್ಳುವುದನ್ನು ಆನಂದಿಸಿ!

[AI ಏಜೆಂಟ್‌ಗಳ ಪರಿಚಯ ಮತ್ತು ಏಜೆಂಟ್ ಬಳಕೆಯ ಪ್ರಕರಣಗಳು](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ನಿರಾಕರಣೆ:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯನ್ನು ಕಾಯ್ದುಕೊಳ್ಳಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ತಪ್ಪುತೆಗಳು ഉണ്ടായಿರಬಹುದೆಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅದರ ಮೂಲ ಭಾಷೆಯಲ್ಲೇ ಪ್ರಾಧಿಕಾರಬದ್ಧ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೆಗಳು ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳ ಮೇಲೆ ನಾವು ಜವಾಬ್ದಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->