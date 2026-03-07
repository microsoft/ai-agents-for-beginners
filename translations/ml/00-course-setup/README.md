# കോഴ്‌സ് സജ്ജീകരണം

## പരിചയം

ഈ പാഠം ഈ കോഴ്‌സിന്റെ കോഡ് സാമ്പിൾസ് എങ്ങനെ പ്രവർത്തിപ്പിക്കാമെന്ന് ഉൾക്കൊള്ളുന്നു.

## മറ്റ് പഠിക്കുന്നവരുമായി ചേരുക, സഹായം നേടുക

നിങ്ങളുടെ റപോ ക്ലോൺ ചെയ്യാൻ തുടങ്ങുന്നതിനുമുമ്പ്, സജ്ജീകരണ സഹായം, കോഴ്‌സിനെക്കുറിച്ചുള്ള ചോദ്യങ്ങൾ, അല്ലെങ്കിൽ മറ്റ് പഠിക്കുന്നവരുമായി ബന്ധപ്പെടാൻ [AI Agents For Beginners Discord ചാനലിൽ](https://aka.ms/ai-agents/discord) ചേരുക.

## ഈ റപോ ക്ലോൺ ചെയ്യുക അല്ലെങ്കിൽ ഫോർക്ക് ചെയ്യുക

ആരംഭിക്കാൻ, ദയവായി GitHub रिपോസിറ്ററി ക്ലോൺ ചെയ്യുകയോ ഫോർക്ക് ചെയ്യുകയോ ചെയ്യുക. ഇതിലൂടെ നിങ്ങള്ക്ക് കോഴ്‌സ് മെറ്റീരിയലിന്റെ സ്വന്തം പതിപ്പ് ഉണ്ടാകും, അതിലൂടെ നിങ്ങൾക്ക് കോഡ് പ്രവർത്തിപ്പിക്കാനും പരീക്ഷിക്കാനും തിരുത്താനും കഴിയും!

ഇത് ചെയ്യാൻ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">റപ്പോ ഫോർക്ക് ചെയ്യുക</a> ലിങ്ക് ക്ലിക്കുചെയ്യുക.

ഇപ്പോൾ ഈ ലിങ്കിൽ നിങ്ങളുടെ സ്വന്തം ഫോർക്ക് ചെയ്ത പതിപ്പ് ഉണ്ടാകണം:

![Forked Repo](../../../translated_images/ml/forked-repo.33f27ca1901baa6a.webp)

### ലഘു ക്ലോൺ (വർക്ക്‌ഷോപ്പ് / Codespaces-നു ശുപാർശചെയ്യുന്നു)

  >ഫുൾ റിപ്പോസിറ്ററി വലുതായിരിക്കും (~3 GB) നിങ്ങൾ മുഴുവൻ ചരിത്രവും ഫയലുകളും ഡൗൺലോഡ് ചെയ്താൽ. നിങ്ങൾ വെറും വർക്ക്‌ഷോപ്പിൽ പങ്കെടുക്കുകയോ കുറച്ച് പാഠഭാഗങ്ങൾക്കായി മാത്രം ആവശ്യമുള്ളെങ്കിൽ, ലഘു ക്ലോൺ (അഥവാ സ്പാർസ് ക്ലോൺ) തിരുത്തൽ ചരിത്രം ചെറുക്കുന്നതിലൂടെയും/അല്ലെങ്കിൽ ബ്ലോബുകൾ ഒഴിവാക്കുന്നതിലൂടെയും ഏറ്റവും വലിയ ഡൗൺലോഡുകൾ ഒഴിവാക്കുന്നു.

#### ത്വരിത ലഘു ക്ലോൺ — പരമാവധി ചരിത്രം ഇല്ലാതെ, എല്ലാ ഫയലുകളും

താഴെ കൊടുത്തിരിക്കുന്ന കമാൻഡിൽ `<your-username>` നിങ്ങളുടെ ഫോർക്ക് URL-ആയിട്ട് (അഥവാ നിങ്ങൾ ഇഷ്ടപ്പെടുന്നെങ്കിൽ അപ്സ്ട്രീം URL) മാറ്റുക.

പുതിയ കൊമിറ്റുകളുടെ ചരിത്രം മാത്രം ക്ലോൺ ചെയ്യാൻ (ചെറിയ ഡൗൺലോഡ്):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

ഒരു പ്രത്യേക ബ്രാഞ്ച് ക്ലോൺ ചെയ്യാൻ:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### ഭാഗിക (സ്പാർസ്) ക്ലോൺ — പരമാവധി ബ്ലോബുകൾ ഇല്ലാതെ + തിരഞ്ഞെടുത്ത ഫോൾഡറുകൾ മാത്രം

ഇതിന് ഭാഗിക ക്ലോൺ, സ്പാർസ്-ചെക്കൗട്ട് ഉപയോഗിക്കുന്നു (Git 2.25+ ആവശ്യം, ഇപ്പോഴത്തെ Git-ഉം ഭാഗിക ക്ലോൺ പിന്തുണയോടെ ശുപാർശ ചെയ്യുന്നു):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

റപ്പോ ഫോൾഡറിൽ പ്രവേശിക്കുക:

```bash|powershell
cd ai-agents-for-beginners
```

തുടർന്ന് നിങ്ങൾക്ക് ആവശ്യമുള്ള ഫോൾഡറുകൾ വ്യക്തമാക്കുക (താഴെ ഉദാഹരണത്തിൽ രണ്ടു ഫോൾഡറുകൾ കാണിക്കുന്നു):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

ക്ലോൺ ചെയ്ത് ഫയലുകൾ പരിശോധിച്ച ശേഷം, ഫയലുകൾ മാത്രം ആവശ്യമുണ്ടെങ്കിൽ, സ്ഥലം ഒഴിവാക്കാൻ (ഗിറ്റ് ചരിത്രമില്ല) റപ്പോ മീറ്റാഡേറ്റ ഡിലീറ്റ് ചെയ്യുക (💀മാറ്റം പിന്മാറാനാവില്ല — എല്ലാ Git പ്രവർത്തനങ്ങളും നഷ്ടപ്പെടും: കമ്മിറ്റുകൾ, പുൾ, പൂഷ് അല്ലാതെയുള്ള ചരിത്രം കാണൽ).

```bash
# സ്ഷ്/bash
rm -rf .git
```

```powershell
# പവർഷെൽ
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ഉപയോഗിച്ച് (പ്രാദേശിക വലിയ ഡൗൺലോഡുകൾ ഒഴിവാക്കാൻ ശുപാർശ)

- ഈ റപ്പോയ്ക്ക് പുതിയ Codespace GitHub UI വഴി സൃഷ്ടിക്കുക: [GitHub UI](https://github.com/codespaces).  

- പുതിയ സൃഷ്ടിച്ച Codespace ടർമിനലിൽ, മുകളിൽ കൊടുത്ത ലഘു/സ്പാർസ് ക്ലോൺ കമാൻഡുകളിൽ ഒന്ന് പ്രവർത്തിപ്പിച്ച് നിങ്ങൾക്ക് ആവശ്യമുള്ള പാഠ ഫോൾഡറുകൾ മാത്രം Codespace വേർക്ക്സ്പെയ്‌സ്‌വിലേക്ക് കൊണ്ടുവരിക.
- ഓപ്ഷണൽ: Codespaces-ലിൽ ക്ലോൺ ചെയ്ത ശേഷം, അധിക സ്ഥലം പിടിച്ചതിനാൽ .git ഫയൽ നീക്കം ചെയ്യാം (മുകളിൽ കൊടുത്ത നീക്കം കമാൻഡുകൾ കാണുക).
- ഷീറെങ്കിൽ, റപ്പോ നേരിട്ടു Codespaces-ൽ തുറക്കാൻ പോകുകയാണെങ്കിൽ (അതിർത് ക്ലോൺ ഇല്ലാതെ), Codespaces ഡെവ്‌കന്റെയ്ൻർ പരിസ്ഥിതി സജ്ജമാക്കും, നിങ്ങൾക്ക് ആവശ്യമുള്ളതിലുണ്ടെങ്കിലുമേൽ കൂടുതൽ വിഭവങ്ങളും സജ്ജീകരിച്ചേക്കാം. പുതിയ Codespace-ൽ ലഘു ക്ലോൺ ചെയ്താൽ ഡിസ്‌ക് ഉപയോഗത്തിൽ നിങ്ങൾക്ക് കൂടുതൽ നിയന്ത്രണം ലഭിക്കും.

#### ഉപദേശങ്ങൾ

- എപ്പോഴും ക്ലോൺ URL നിങ്ങളുടെ ഫോർക്കിനു മാറ്റുക, എഡിറ്റ്/കമ്മിറ്റ് ചെയ്യാൻ ആഗ്രഹിക്കുന്നതെങ്കിൽ.
- പിന്നീട് നിങ്ങൾക്ക് കൂടുതൽ ചരിത്രം അഥവാ ഫയലുകൾ ആവശ്യമുണ്ടെങ്കിൽ, അത് ഫേറ്റ് ചെയ്ത് ഉൾപ്പെടുത്താനോ സ്പാർസ്-ചെക്കൗട്ട് ക്രമീകരിച്ച് കൂടുതൽ ഫോൾഡറുകൾ ഉൾപ്പെടുത്താനോ കഴിയും.

## കോഡ് പ്രവർത്തിപ്പിക്കൽ

ഈ കോഴ്‌സ് എടുത്തെടുത്ത Jupyter നോട്ട്ബുക്കുകൾ സ്രഷ്ടിക്കുന്നു, നിങ്ങള്ക്ക് നേരിട്ടു AI ഏജന്റുകളിൽ പ്രവർത്തിക്കാനുള്ള പ്രായോഗിക അനുഭവം നേടാൻ.

കോഡ് സാമ്പിൾസ് **Microsoft Agent Framework (MAF)** ഉപയോഗിച്ചാണ്, ഇതിൽ `AzureAIProjectAgentProvider`, **Azure AI Agent Service V2** (Responses API) വഴി **Microsoft Foundry**-യുമായി കണക്ട് ചെയ്യുന്നു.

എല്ലാ Python നോട്ട്ബുക്കുകളും `*-python-agent-framework.ipynb` എന്ന ലേബലോടെയാണ്.

## ആവശ്യകതകൾ

- Python 3.12+
  - **ശ്രദ്ധിക്കുക**: Python3.12 നിങ്ങൾインസ്റ്റാൾ ചെയ്തിട്ടില്ലെങ്കിൽ, ദയവായിインസ്റ്റാൾ ചെയ്യുക. പിന്നീട് python3.12 ഉപയോഗിച്ച് venv സൃഷ്ടിക്കുക, requirements.txt ഫയലിൽ നിന്നുള്ള ശരിയായ പതിപ്പുകൾ インസ്റ്റാൾ ചെയ്യാൻ.
  
    >ഉദാഹരണം

    Python venv ഡയറക്ടറി സൃഷ്ടിക്കുക:

    ```bash|powershell
    python -m venv venv
    ```

    തുടർന്ന് venv സജീവമാക്കുക:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET ഉപയോഗിച്ചുള്ള സാമ്പിൾ കോഡുകൾക്കായി [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) അല്ലെങ്കിൽ പിന്നീട് പതിപ്പ് インസ്റ്റാൾ ചെയ്യുക. ഇൻസ്റ്റാൾ ചെയ്ത .NET SDK പതിപ്പ് പരിശോധിക്കുക:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — ഒട്ടും 인증ക്കായി ആവശ്യമാണ്. ഇൻസ്റ്റാൾ ചെയ്യുന്നതിന് [aka.ms/installazurecli](https://aka.ms/installazurecli) സന്ദർശിക്കുക.
- **Azure Subscription** — Microsoft Foundryക്കും Azure AI Agent Service-ക്കും ആക്സസ് നേടാൻ.
- **Microsoft Foundry Project** — മോഡൽ ഡിപ്ലോയ് ചെയ്ത ഒരു പ്രോജക്ട് (ഉദാ: `gpt-4o`). താഴെ ഉള്ള [പടി 1](../../../00-course-setup) കാണുക.

ഈ റപ്പോയുടെ റൂട്ട് ഡയറക്ടറിയില്‍ `requirements.txt` ഫയൽ ഉൾപ്പെടുത്തിയിട്ടുണ്ട്, കോഡ് സാമ്പിൾസ് പ്രവർത്തിപ്പിക്കാൻ ആവശ്യമായ എല്ലാ Python പാക്കേജുകളും ഉള്ളത്.

ഇത് ഇൻസ്റ്റാൾ ചെയ്യാൻ റൂട്ട് ഡയറക്ടറിയിൽ താഴെ കൊടുത്ത കമാൻഡ് ഓടിക്കുക:

```bash|powershell
pip install -r requirements.txt
```

ചേടുകൾ ഒഴിവാക്കാനും പ്രശ്നങ്ങൾ ഒഴിവാക്കാൻ Python virtual environment സൃഷ്ടിക്കാനാണ് ശുപാർശ.

## VSCode ക്രമീകരിക്കുക

VSCode-ൽ ശരിയായ Python പതിപ്പ് ഉപയോഗിക്കുന്നുണ്ടെന്ന് ഉറപ്പാക്കുക.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundryയും Azure AI Agent Serviceയും ക്രമീകരിക്കുക

### പടി 1: Microsoft Foundry പ്രോജക്ട് സൃഷ്ടിക്കുക

നോട്ട്ബുക്കുകൾ പ്രവർത്തിപ്പിക്കാൻ Azure AI Foundry **ഹബ്**ക്കും **പോജക്ട്**ഉം ഡിപ്ലോയ്ഡ് ചെയ്ത മോഡലോടുകൂടി ആവശ്യമുണ്ട്.

1. [ai.azure.com](https://ai.azure.com) സന്ദർശിച്ചു നിങ്ങളുടെ Azure അക്കൗണ്ടിൽ സൈൻ ഇൻ ചെയ്യുക.
2. ഒരു **ഹബ്** സൃഷ്ടിക്കുക (അല്ലെങ്കിൽ നിലവിലുള്ളത് ഉപയോഗിക്കുക). കാണുക: [ഹബ് റിസോഴ്‌സസ് അവലോകനം](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. ഹബ്‌ക്കുള്ളിൽ ഒരു **പ്രോജക്ട്** സൃഷ്ടിക്കുക.
4. **Models + Endpoints** → **Deploy model** വഴി മോഡൽ (ഉദാ: `gpt-4o`) ഡിപ്ലോയ് ചെയ്യുക.

### പടി 2: നിങ്ങളുടെ പ്രോജക്ട് എન્ડ്പോയിന്റ്, മോഡൽ ഡിപ്ലോയ്‌മെന്റ് പേര് കിട്ടുക

Microsoft Foundry പോർട്ടലിലെ നിങ്ങളുടെ പ്രോജക്ടിൽ നിന്നു:

- **Project Endpoint** — **Overview** പേജ് സന്ദർശിച്ച് എന്റ്‌പോയിന്റ് URL പകർപ്പിക്കുക.

![Project Connection String](../../../translated_images/ml/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** തുറന്ന് നിങ്ങളുടെ ഡിപ്ലോയ്ഡ് ചെയ്ത മോഡൽ തിരഞ്ഞെടുക്കുക, **Deployment name** (ഉദാ: `gpt-4o`) നോട്ട് ചെയ്യുക.

### പടി 3: `az login` ഉപയോഗിച്ച് Azure-യിൽ സൈൻ ഇൻ ചെയ്യുക

എല്ലാ നോട്ട്ബുക്കുകളും **`AzureCliCredential`** ഉപയോഗിച്ച് 인증 ചെയ്യുന്നു — API കീകൾ ആവശ്യമില്ല. അതിനായി നിങ്ങൾ Azure CLI വഴി സൈൻ ഇൻ ചെയ്തിരിക്കണം.

1. Azure CLI インസ്റ്റാൾ ചെയ്യുക: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. താഴെ കമാൻഡ് ഉപയോഗിച്ച് സൈൻ ഇൻ ചെയ്യുക:

    ```bash|powershell
    az login
    ```

    അല്ലിയോ നിങ്ങൾ റിമോട്ട്/Codespace പരിസ്ഥിതിയിലാണെങ്കില്‍ ബ്രൗസർ ഇല്ലാതെ:

    ```bash|powershell
    az login --use-device-code
    ```

3. ആവശ്യമായാൽ നിങ്ങളുടെ സബ്സ്ക്രിപ്ഷൻ തിരഞ്ഞെടുക്കുക — നിങ്ങളുടെ Foundry പ്രോജക്ട് ഉള്ളത്.

4. സൈൻ ഇൻ ചെയ്തിട്ടുണ്ടോ എന്ന് പരിശോധിക്കുക:

    ```bash|powershell
    az account show
    ```

> **`az login` എന്തിന്?** നോട്ട്ബുക്കുകൾ `azure-identity` പാക്കേജിൽ നിന്നുള്ള `AzureCliCredential` ഉപയോഗിച്ച് 인증 നടത്തുന്നു — ഇത് Azure CLI സെഷനിൽ നിന്നുള്ള ക്രെഡൻഷ്യലുകളാണ് ഉപയോഗിക്കുന്നത് — API കീകൾ അല്ല `.env` ഫയലിൽ രഹസ്യ വിവരങ്ങൾ ആണില്ലാത്തത് ഈ ഉപയോഗം സുരക്ഷിതമായ രീതിയാണ്. ഇത് [സുരക്ഷിത മേധാവിത്വം](https://learn.microsoft.com/azure/developer/ai/keyless-connections) ആണ്.

### പടി 4: നിങ്ങളുടെ `.env` ഫയൽ സൃഷ്ടിക്കുക

ഉദാഹരണ ഫയൽ പകർത്തുക:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# പവർഷെൽ
Copy-Item .env.example .env
```

`.env` ഫയൽ തുറന്ന് താഴെ കൈയെടുക്കേണ്ട രണ്ട് വിലങ്ങൾ പകർപിക്കുക:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| വേരിയബിൾ | എവിടെ കണ്ടെത്താം |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry പോർട്ടൽ → നിങ്ങളുടെ പ്രോജക്ട് → **Overview** പേജ് |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry പോർട്ടൽ → **Models + Endpoints** → നിങ്ങളുടെ ഡിപ്ലോയ്ഡ് ചെയ്ത മോഡലിന്റെ പേര് |

അതിർത്തി പാഠങ്ങൾക്കായി ആവശ്യമുള്ളത് ഇതുവരെ! നോട്ട്ബുക്കുകൾ ആ automática ആയി നിങ്ങളുടെ `az login` സെഷൻ വഴി 인증 ചെയ്യും.

### പടി 5: Python ആശ്രിതങ്ങൾ インസ്റ്റാൾ ചെയ്യുക

```bash|powershell
pip install -r requirements.txt
```

ഈ കമാൻഡ് നിങ്ങൾ ആദ്യം സൃഷ്ടിച്ച virtual environment-ൽ ഓടാൻ ശുപാർശ.

## പാഠം 5 (Agentic RAG) ആവശ്യമായ അധിക ക്രമീകരണം

പാഠം 5 **Azure AI Search** ഉപയോഗിച്ച് Retrieval-Augmented Generation സൃഷ്ടിക്കുന്നു. ആ പാഠം ഓടിക്കാൻ പദ്ധതിയുണ്ടെങ്കിൽ, `.env` ഫയലിൽ താഴെ പറയുന്ന വേരിയബിൾസ് ചേർക്കുക:

| വേരിയബിൾ | എവിടെ കണ്ടെത്താം |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure പോർട്ടൽ → നിങ്ങളുടെ **Azure AI Search** റിസോഴ്സ് → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure പോർട്ടൽ → നിങ്ങളുടെ **Azure AI Search** റിസോഴ്സ് → **Settings** → **Keys** → പ്രാഥമിക അഡ്മിൻ കീ |

## പാഠം 6, 8 (GitHub Models) ആവശ്യമായ അധിക ക്രമീകരണം

പാഠം 6, 8ലെ ചില നോട്ട്ബുക്കുകളിൽ **Azure AI Foundry** പ്രയോഗിക്കുന്നതിന പകരം **GitHub Models** ഉപയോഗിക്കുന്നു. ആ സാമ്പിളുകൾ ഓടിക്കാൻ ആഗ്രഹിക്കുന്നുവെങ്കിൽ, `.env` ഫയലിൽ താഴെ പറയുന്നവ ചേർക്കുക:

| വേരിയബിൾ | എവിടെ കണ്ടെത്താം |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | `https://models.inference.ai.azure.com` (ഡീഫോൾട്ട് വില) |
| `GITHUB_MODEL_ID` | ഉപയോഗിക്കാൻ മോഡൽ പേര് (ഉദാ: `gpt-4o-mini`) |

## പാഠം 8 (Bing Grounding Workflow) ആവശ്യമായ അധിക ക്രമീകരണം

പാഠം 8ലെ conditional workflow നോട്ട്ബുക്ക് Azure AI Foundry വഴി **Bing grounding** ഉപയോഗിക്കുന്നു. ആ സാമ്പിൾ ഓടിക്കാൻ ആഗ്രഹിക്കുന്നുവെങ്കിൽ, `.env` ഫയലിൽ ഈ വേരിയബിൾ ചേർക്കുക:

| വേരിയബിൾ | എവിടെ കണ്ടെത്താം |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry പോർട്ടൽ → നിങ്ങളുടെ പ്രോജക്ട് → **Management** → **Connected resources** → നിങ്ങളുടെ Bing കണക്ഷൻ → കണക്ഷൻ ഐഡി പകർപ്പിക്കുക |

## പ്രശ്നപരിഹാരം

### macOS-ൽ SSL സർട്ടിഫിക്കറ്റ് സ്ഥിരീകരണ പിഴവുകൾ

macOS-യിൽ താഴെയുള്ള പിഴവ് പ്രത്യക്ഷപ്പെടുമ്പോൾ:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

ഇത് macOS-ൽ Python SSL സർട്ടിഫിക്കറ്റുകൾ സ്വയം വിശ്വസിക്കാത്ത പ്രശ്നം ആയി അറിയപ്പെടുന്നു. താഴെ പറയുന്ന പരിഹാരങ്ങൾ ക്രമത്തിൽ പരീക്ഷിക്കുക:

**ഓപ്ഷൻ 1: Python ആണ് ഇൻസ്റ്റാൾ ചെയ്ത സർട്ടിഫിക്കറ്റ് സ്ക്രിപ്റ്റ് ഓടിക്കുക (ശുപാർശചെയ്യുന്നു)**

```bash
# നിങ്ങളുടെ ഇൻസ്റ്റാൾ ചെയ്ത Python പതിപ്പുമായി 3.XX മാറ്റുക (ഉദാ: 3.12 അല്ലെങ്കിൽ 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ഓപ്ഷൻ 2: നിങ്ങളുടെ നോട്ട്ബുക്കിൽ `connection_verify=False` ഉപയോഗിക്കുക (GitHub Models നോട്ട്ബുക്കുകൾക്ക് മാത്രം)**

Lesson 6 നോട്ട്ബുക്കിൽ (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), കുറിപ്പ് ചെയ്ത ചെറിയ പരിഹാരം ഇതിനകം ഉൾപ്പെടുത്തിയിട്ടുണ്ട്. ക്ലയന്റ് സൃഷ്‌ടിച്ചപ്പോൾ `connection_verify=False` അൺകോമന്റ് ചെയ്യുക:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # സർട്ടിഫിക്കറ്റ് പിശകുകൾ നേരിടുമ്പോൾ SSL പരിശോധന പ്രവർത്തനരഹിതമാക്കുക
)
```

> **⚠️ ഓർമ്മിക്കുക:** SSL പരിശോദന നിഷേധിക്കുന്നത് (`connection_verify=False`) സുരക്ഷ കുറയ്ക്കുന്നു. ഇത് വികസന പരിതസ്ഥിതികളിൽ താൽക്കാലിക പരിഹാരമായി മാത്രം ഉപയോഗിക്കുക, പ്രൊഡക്ഷൻ ഇന്യിരത്തു ഒഴിവാക്കുക.

**ഓപ്ഷൻ 3: `truststore` インസ്റ്റാൾ ചെയ്യുകയും ഉപയോഗിക്കുക**

```bash
pip install truststore
```

നോട്ട്ബുക്ക് അല്ലെങ്കിൽ സ്ക്രിപ്റ്റ് മുകളിൽ ഏത് നെറ്റ്‌വർക്ക് കോൾസ് ചെയ്യുന്നതിനു മുൻപ് താഴെ ചേർക്കുക:

```python
import truststore
truststore.inject_into_ssl()
```

## എവിടെയെങ്കിലും കുടുങ്ങിയോ?

ഈ ക്രമീകരണം ഓടിക്കാൻ എങ്ങനെ സഹായം ആവശ്യമുണ്ടെങ്കിൽ, ഞങ്ങളുടെ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> ൽ ചേരൂ അല്ലെങ്കിൽ <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ഇഷ്യു സൃഷ്ടിക്കൂ</a>.

## അടുത്ത പാഠം

ഇപ്പോൾ നിങ്ങൾക്ക് ഈ കോഴ്‌സിന്റെ കോഡ് ഓടിക്കാൻ തയ്യാറാണ്. AI ഏജന്റുകളുടെ ലോകത്തെ കുറിച്ച് കൂടുതൽ മനസ്സിലാക്കാൻ സന്തോഷകരമായ പഠനം നേടുക!

[AI ഏജന്റുകളും ഏജന്റ് ഉപയോഗ കേസുകളും പരിചയം](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസാധുവാക്കൽ**:
ഈ документы [Co-op Translator](https://github.com/Azure/co-op-translator) എന്ന AI പരിഭാഷ സേവനം ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിക്കുന്നുവെങ്കിലും, автоматിക് പരിഭാഷകളിൽ പിശകുകൾ അല്ലെങ്കിൽ അശുദ്ധികൾ ഉണ്ടായിരിക്കാം എന്ന് ശ്രദ്ധിക്കുക. മാതൃഭാഷയിൽ ഉള്ള മാതൃകാ രേഖ പരമാവധി വിശ്വാസയോഗ്യമാണെന്ന് കണക്കാക്കണമെന്നും നിർബന്ധൂം വ്യക്തമാക്കുന്നു. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മാനവ പരിഭാഷ ശിപാർശവുമാണ്. ഈ പരിഭാഷ ഉപയോഗത്തിനാൽ any any അർത്ഥമാറ്റങ്ങൾക്കും വ്യത്യാസങ്ങൾക്കുമുള്ള ഉത്തരവാദിത്വം ഞങ്ങൾ ഏറ്റെടുക്കുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->