# കോഴ്‌സ് സജ്ജീകരണം

## പരിചയം

ഈ പാഠം ഈ കോഴ്‌സിന്റെ കോഡ് സാമ്പിളുകൾ എങ്ങനെ റൺ ചെയ്യാമെന്ന് ഉൾക്കൊള്ളുന്നു.

## മറ്റു പഠിക്കുന്നവരുമായി ചേര്‍ന്ന് സഹായം നേടുക

നിങ്ങളുടെ റിപൊ ക്ലോൺ ചെയ്യാൻ തുടങ്ങുന്നതിനു മുൻപ്, സഹായത്തിനായി, കോഴ്‌സ് സംബന്ധിച്ച 질문കൾക്കായി, അല്ലെങ്കിൽ മറ്റു പഠിക്കുന്നവരുമായി ബന്ധപ്പെടുന്നതിനായി [AI Agents For Beginners Discord ചാനലിൽ](https://aka.ms/ai-agents/discord) ചേരുക.

## ഈ റിപൊ ക്ലോൺ ചെയ്യുക അല്ലെങ്കിൽ ഫോർക്കുചെയ്യുക

തുടങ്ങാൻ, ദയവായി GitHub റിപ്പോസിററി ക്ലോൺ ചെയ്യുകയോ ഫോർക്കുചെയ്യുകയോ ചെയ്യുക. ഇത് നിങ്ങൾക്ക് കോഴ്‌സ് മെറ്റീരിയലിന്റെ നിങ്ങളുടെ സ്വന്തം പതിപ്പ് ഉണ്ടാകാൻ സഹായിക്കും, അതിലൂടെ നിങ്ങൾ കോഡ് റൺ ചെയ്യാനും, ടെസ്റ്റ് ചെയ്യാനും, മാറ്റങ്ങൾ ചെയ്യാനും കഴിയും!

ഇത് ചെയ്യാൻ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">റിപൊ ഫോർക്കുചെയ്യുക</a> ലിങ്കിൽ ക്ലിക്ക് ചെയ്യുക.

ഇപ്പോൾ നിങ്ങൾക്ക് ഈ കോഴ്‌സിന്റെ സ്വന്തം ഫോർക്കുചെയ്ത പതിപ്പ് താഴെ കാണുന്ന ലിങ്കിൽ ഉണ്ടായിരിക്കണം:

![Forked Repo](../../../translated_images/ml/forked-repo.33f27ca1901baa6a.webp)

### ശലോ ക്ലോൺ (വർക്ക്ഷോപ്പ് / കോഡ്സ്പേസുകൾക്ക് ശുപാർശ ചെയ്യുന്നു)

  >പൂർണ്ണ റിപോസിററി ഡൗൺലോഡ് ചെയ്യുമ്പോൾ അത് വലുതായിരിക്കാം (~3 GB), പൂർണ്ണ ചരിത്രവും എല്ലാ ഫയലുകളും അടക്കം. നിങ്ങൾ വർക്ക്ഷോപ്പ് പങ്കെടുക്കുകയാണെങ്കിൽ അല്ലെങ്കിൽ കുറച്ച് പാഠി ഫോളഡറുകളുടേം മാത്രം ആവശ്യമാണെങ്കിൽ, ശലോ ക്ലോൺ (അല്ലെങ്കിൽ സ്പാഴ്‌സ് ക്ലോൺ) ചരിത്രം കുറക്കുകയോ ബ്‌ളോബുകൾ ഒഴിവാക്കുകയോ ചെയ്ത് കൂടുതലായ ഡൗൺലോഡ് ഒഴിവാക്കും.

#### വേഗത്തിൽ ശലോ ക്ലോൺ — ഏറ്റവും കുറഞ്ഞ ചരിത്രം, എല്ലാ ഫയലുകളും

താഴെയുള്ള കമാൻഡുകളിൽ `<your-username>` നിങ്ങളുടെ ഫോർക്കിന്റെ URL (അഥവാ ഇഷ്ടാനുസൃത upstream URL) കൊണ്ട് മാറ്റുക.

ഏറ്റവും പുതിയ commit ചരിത്രം മാത്രം ക്ലോൺ ചെയ്യാൻ (ചെറുതായ ഡൗൺലോഡ്):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

പ്രത്യേക ബ്രാഞ്ച് ക്ലോൺ ചെയ്യാൻ:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### ഭാഗിക (സ്പാഴ്‌സ്) ക്ലോൺ — കുറഞ്ഞ ബ്‌ളോബുകളും തിരഞ്ഞെടുത്ത ഫോളഡറുകളും മാത്രം

ഇത് ഭാഗിക ക്ലോൺ, സ്പാഴ്‌സ്-ചെക്കൗട്ട് ഉപയോഗിക്കുന്നു (Git 2.25+ വേണം, ട്രെൻഡായി gedeelt_clone പിന്തുണയുള്ള പുതിയ Git ശുപാർശ ചെയ്യുന്നു):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

റിപോ ഫോളഡറിലേക്ക് പോയി:

```bash|powershell
cd ai-agents-for-beginners
```

തുടർന്ന് നിങ്ങൾക്ക് വേണ്ട ഫോളഡറുകൾ উল্লেখിക്കുക (താഴെയുള്ള ഉദാഹരണം രണ്ട് ഫോളഡറുകൾ കാണിക്കുന്നു):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

ക്ലോൺ ചെയ്ത് ഫയലുകൾ പരിശോധിച്ചതിനു ശേഷം, നിങ്ങൾക്ക് ഫയലുകൾ മാത്രമേ ആവശ്യമായുള്ളൂ കൂടാതെ സ്ഥലമൊന്നും ഒഴിവാക്കണമെന്ന് ഞാൻ താല്പര്യപ്പെടുന്നുവെങ്കിൽ (ഗിറ്റ് ചരിത്രമില്ലാതെ), റിപോസിററി മെറ്റാഡേറ്റ ഡിലീറ്റ് ചെയ്യുക (💀ശേഷിയില്ലാത്ത നടപടി — എല്ലാ Git പ്രവർത്തനങ്ങളും നഷ്ടപ്പെടും: commit, pull, push, ചരിത്രം എല്ലാം).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# പവർഷെൽ
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ഉപയോഗിക്കുന്നത് (പ്രാദേശിക വലിയ ഡൗൺലോഡുകൾ ഒഴിവാക്കാൻ ശുപാർശ)

- ഈ റിപൊയ്ക്ക് പുതിയ Codespace സൃഷ്ടിക്കാൻ [GitHub UI](https://github.com/codespaces) ഉപയോഗിക്കുക.  

- പുതിയ Codespace ടർമിനലിൽ, മുകളിലെ ശലോ / സ്പാഴ്‌സ് ക്ലോൺ കമാൻഡുകളിൽ ഏതെങ്കിലും ഒന്നു ഓടിച്ച് നിങ്ങൾക്ക് ആവശ്യമുള്ള പാഠഫോളഡറുകൾ മാത്രമേ Codespace വർക്ക്സ്പേസിലേക്ക് കൊണ്ടുവരൂ.
- ഐഷ്ഫിക്: Codespaces മുകളിൽ ക്ലോൺ ചെയ്യുന്നതിനു ശേഷം, അധികം സ്ഥലമൊന്നും ഒഴിവാക്കാനായി .git നീക്കം ചെയ്യുക (മുകളിലെ നീക്കം കമാൻഡുകൾ നോക്കുക).
- നോട്ടീസ്: നിങ്ങൾക്ക് റിപൊ നേരിട്ടു Codespacesൽ തുറക്കണമെങ്കിൽ (ക്ലോൺ ഇല്ലാതെ), Codespaces devcontainer പരിസ്ഥിതി നിർമ്മിക്കും, കൂടുതൽ പ്രവിഷനും നൽകും. ശലോ കോപ്പി Kl(െടഒരു പുതിയ Codespaceൽ ക്ലോൺ ചെയ്യുന്നതോടെ നിങ്ങൾക്ക് ഹാർഡ് ഡ്രൈവ് ഉപയോഗം ഭരണപ്പെടുത്താം.

#### സൂചനകൾ

- നിങ്ങൾ മാറ്റം വരുത്താനും കമിറ്റ് ചെയ്യാനും ആഗ്രഹിക്കുന്നുവെങ്കിൽ clone URL നിങ്ങളുടെ ഫോർക്കിൽ എപ്പോഴും മാറ്റുക.
- പിന്നീട് കൂടുതൽ ചരിത്രം അല്ലെങ്കിൽ ഫയലുകൾ ആവശ്യമായെങ്കിൽ, അവയെ fetch ചെയ്യുകയോ സ്പാഴ്‌സ്-ചെക്കൗട്ട് ക്രമീകരിച്ച് കൂടുതൽ ഫോളഡറുകൾ ഉൾപ്പെടുത്തുകയോ ചെയ്യാം.

## കോഡ് റൺ ചെയ്യൽ

ഈ കോഴ്‌സ് AI ഏജന്റുകൾ നിർമ്മിക്കുന്നതിനുള്ള പ്രായോഗിക അനുഭവങ്ങൾ ലഭിക്കാൻ ഉപയോഗിക്കാവുന്ന ഒരു നിരയുടെ Jupyter നോട്ട്‌ബുക്കുകൾ നൽകുന്നു.

കോഡ് സാമ്പിളുകൾ നായ്ക്കുന്നു **Microsoft Agent Framework (MAF)** `FoundryChatClient` ഉപയോഗിച്ച്, ഇത് **Microsoft Foundry Agent Service V2** (Responses API) വഴി **Microsoft Foundry**-യുമായി ബന്ധിപ്പിക്കുന്നു.

എല്ലാ Python നോട്ട്‌ബുക്കുകളും `*-python-agent-framework.ipynb` എന്ന ലേബൽ നേടിയിരിക്കുന്നു.

## ആവശ്യങ്ങൾ

- Python 3.12+
  - **കുറിപ്പ്**: Python3.12 ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടെങ്കിൽ മാത്രമേ തുടരുക. പിന്നീട് requirements.txt ഫയലിൽ ഉചിതമായ പതിപ്പുകൾ ഇൻസ്റ്റാൾ ചെയ്യാൻ python3.12 ഉപയോഗിച്ച് വെർച്ച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കുക.
  
    >ഉദാഹരണം

    Python വെർച്ച്വൽ എൻവയോൺമെന്റ് ഡയറക്ടറി സൃഷ്ടിക്കുക:

    ```bash|powershell
    python -m venv venv
    ```

    ശേഷം വെർച്ച്വൽ എൻവയോൺമെന്റ് പ്രവർത്തിപ്പിക്കുക:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET ഉപയോഗിക്കുന്ന സാമ്പിൾ കോഡുകൾക്കായി [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) അല്ലെങ്കിൽ അതിനും പുതിയത് ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക. തുടർന്ന് ഇൻസ്റ്റാൾ ചെയ്ത ഡോട്ട്‌നെറ്റ് SDK പതിപ്പ് പരിശോധിക്കുക:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — പ്രാമാണീകരണത്തിനായി ആവശ്യമാണ്. [aka.ms/installazurecli](https://aka.ms/installazurecli) നിന്നും ഇൻസ്റ്റാൾ ചെയ്യുക.
- **Azure Subscription** — Microsoft Foundry, Microsoft Foundry Agent Service അംഗീകാരത്തിന്.
- **Microsoft Foundry Project** — വിന്യാസ മോഡലുമായി ഒരു പ്രോജക്ട് (ഉദാ: `gpt-4o`). താഴെ [പടിയം 1](#പ്രഥമ-പടി-microsoft-foundry-പ്രോജക്ട്-സൃഷ്ടിക്കുക) കാണുക.

ഈ റിപോസിററിയിൽ ഒരു `requirements.txt` ഫയൽ ഉൾപ്പെടുത്തിയിട്ടുണ്ട്, ഇത് കോഡ് സാമ്പിളുകൾ റൺ ചെയ്യാൻ ആവശ്യമായ എല്ലാ Python പാക്കേജുകളും ഉൾക്കൊള്ളുന്നു.

റിലോപ്പി റിപോസിററിയുടെ റൂട്ടിൽ താഴെ കമാൻഡ് റൺ ചെയ്ത് ഇത് ഇൻസ്റ്റാൾ ചെയ്യാം:

```bash|powershell
pip install -r requirements.txt
```

- വേദാന്തവിരുദ്ധതകൾ ഒഴിവാക്കാനായി Python വെർച്ച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കുകയും ഉപയോഗിക്കുകയും ചെയ്യാൻ ശുപാർശ ചെയ്യുന്നു.

## VSCode സജ്ജമാക്കുക

VSCode-ൽ ശരിയായ Python പതിപ്പ് ഉപയോഗിക്കുന്നുവെന്ന് ഉറപ്പ് വരുത്തുക.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry, Microsoft Foundry Agent Service സജ്ജീകരിക്കൽ

### പ്രഥമ പടി: Microsoft Foundry പ്രോജക്ട് സൃഷ്ടിക്കുക

നിങ്ങൾക്ക് നോട്ട്‌ബുക്കുകൾ റൺ ചെയ്യുവാൻ Microsoft Foundry **ഹബ്**യും **പ്രോജക്ടും** വിന്യസിച്ച മോഡലോടുകൂടി വേണം.

1. [ai.azure.com](https://ai.azure.com) സന്ദർശിച്ച് നിങ്ങളുടെ Azure അക്കൗണ്ടിൽ സൈൻ ഇൻ ചെയ്യുക.
2. ഒരു **ഹബ്** സൃഷ്ടിക്കുക (അല്ലെങ്കിൽ നിലവിലുള്ളത് ഉപയോഗിക്കുക). കാണുക: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. ഹബിനുള്ളിൽ ഒരു **പ്രോജക്ട്** സൃഷ്ടിക്കുക.
4. **Models + Endpoints** → **Deploy model** വഴി മോഡൽ (ഉദാ: `gpt-4o`) വിന്യസിക്കുക.

### രണ്ടാം പടി: പ്രോജക്ട് എൻഡ്‌പോയിന്റ്, മോഡൽ വിന്യാസ നാമം കണ്ടുപിടിക്കുക

Microsoft Foundry പോർട്ടൽയിൽ നിന്നു:

- **Project Endpoint** — **Overview** പേജ് സന്ദർശിച്ച് എൻഡ്‌പോയിന്റ് URL αντιγράψτε ചെയ്യുക.

![Project Connection String](../../../translated_images/ml/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** സന്ദർശിച്ച് വിന്യസിച്ച മോഡൽ തിരഞ്ഞെടുക്കുക, **Deployment name** അനുസ്മരിച്ചു നോക്കുക (ഉദാ: `gpt-4o`).

### മൂന്നാം പടി: `az login` ഉപയോഗിച്ച് Azure-യിൽ സൈൻ ഇൻ ചെയ്യുക

എല്ലാ നോട്ട്‌ബുക്കുകളും **`AzureCliCredential`** ഉപയോഗിച്ച് പ്രാമാണീകരിക്കുന്നു — API കീകൾ മാനേജ് ചെയ്യേണ്ടതില്ല. അതിനായി Azure CLI വഴി സൈൻ ഇൻ ചെയ്തിരിക്കണം.

1. **Azure CLI ഇൻസ്റ്റാൾ ചെയ്യുക**: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **സൈൻ ഇൻ ചെയ്യുക** ഈ കമാൻഡ് റൺ ചെയ്ത്:

    ```bash|powershell
    az login
    ```

    അല്ലെങ്കിൽ ബ്രൗസർ ഇല്ലാത്ത റിമോട്ട്/Codespace സാഹചര്യത്തിൽ:

    ```bash|powershell
    az login --use-device-code
    ```

3. ആവശ്യപ്പെട്ടാൽ **സബ്സ്ക്രിപ്ഷൻ തിരഞ്ഞെടുക്കുക** — നിങ്ങളുടെ Foundry പ്രോജക്ട് ഉൾപ്പെടുത്തിയ സബ്സ്ക്രിപ്ഷൻ തെരഞ്ഞെടുക്കുക.

4. **സൈൻ ഇൻ ആയിരിക്കുന്നുവെന്ന് ഉറപ്പ് വരുത്തുക**:

    ```bash|powershell
    az account show
    ```

> **`az login` എന്ത്ന്നുവെന്ന്?** നോട്ട്‌ബുക്കുകൾ `azure-identity` പാക്കേജിലുള്ള `AzureCliCredential` ഉപയോഗിച്ച് പ്രാമാണീകരിക്കുന്നു. അതായത് നിങ്ങളുടെ Azure CLI സെഷൻ ക്രെഡൻഷ്യലുകൾ നൽകുന്നു — നിങ്ങളുടെ `.env` ഫയലിൽ API കീകളും രഹസ്യങ്ങളും വേണ്ടതില്ല. ഇത് [സുരക്ഷിത നടപ്പായിരിക്കും](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### നാലാം പടി: `.env` ഫയൽ സൃഷ്ടിക്കുക

ഉദാഹരണ ഫയൽ പകർത്തുക:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# പവർഷെൽ
Copy-Item .env.example .env
```

`.env` തുറന്ന് ഈ രണ്ട് മൂല്യങ്ങൾ പൂരിപ്പിക്കുക:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| വേരിയബിൾ | എവിടെ കണ്ടെത്തും |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → നിങ്ങളുടെ പ്രോജക്ട് → **Overview** പേജ് |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → നിങ്ങളുടെ വിന്യസിച്ച മോഡൽ നാമം |

മിക്ക പാഠങ്ങൾക്കായി ഇതുപോലെയാണ്! നോട്ട്‌ബുക്കുകൾ നിങ്ങളുടെ `az login` സെഷൻ വഴി സ്വയം പ്രാമാണീകരിക്കും.

### അഞ്ചാം പടി: Python അനിവാര്യങ്ങളൊക്ക് ഇൻസ്റ്റാൾ ചെയ്യുക

```bash|powershell
pip install -r requirements.txt
```

നിങ്ങൾ മുമ്പ് സൃഷ്ടിച്ച വെർച്ച്വൽ എൻവയോൺമെന്റിൽ ഇത് ഓടിക്കാൻ ശുപാർശ ചെയ്യുന്നു.

## പാഠം 5 (Agentic RAG) ന് അധിക സജ്ജീകരണം

പാഠം 5-ൽ **Azure AI Search** retrieval-augmented generation-നായി ഉപയോഗിക്കുന്നു. ആ പാഠം ഓടിക്കാൻ ആങ്കിൽ നിങ്ങളുടെ `.env` ഫയലിൽ ഈ വേരിയബിളുകൾ ചേർക്കുക:

| വേരിയബിൾ | എവിടെ കണ്ടെത്തും |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → നിങ്ങളുടെ **Azure AI Search** റിസോഴ്‌സ് → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → നിങ്ങളുടെ **Azure AI Search** റിസോഴ്‌സ് → **Settings** → **Keys** → പ്രധാന അഡ്മിൻ കീ |

## Azure OpenAI നേരിട്ട് വിളിക്കുന്ന പാഠങ്ങൾക്കായുള്ള അധിക സജ്ജീകരണം (പാഠം 6, 8)

പാഠങ്ങൾ 6, 8 ലെ ചില നോട്ട്‌ബുക്കുകൾ Microsoft Foundry പ്രോജക്ട് വഴി പോയാതെയാണ് നേരിട്ട് **Azure OpenAI** (Responses API ഉപയോഗിച്ചു) വിളിക്കുന്നത്. മുൻപ് GitHub Models ഉപയോഗിച്ചിരുന്നു, ഇപ്പോൾ ഫസ്ച്ച് ചെയ്യപ്പെട്ടിരിക്കുന്നു (2026 ജൂലൈയിൽ വിരമിക്കും) കൂടാതെ Responses API പിന്തുണയില്ല. ഈ സാമ്പിളുകൾ റൺ ചെയ്യാൻ ആഗ്രഹിച്ചാൽ താഴെയുള്ള വേരിയബിൾ `.env` ഫയലിൽ ചേർക്കുക:

| വേരിയബിൾ | എവിടെ കണ്ടെത്തും |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → നിങ്ങളുടെ **Azure OpenAI** റിസോഴ്‌സ് → **Keys and Endpoint** → Endpoint (ഉദാ: `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Responses API പിന്തുണയുള്ള നിങ്ങളുടെ വിന്യസിച്ച മോഡൽ നാമം (ഉദാ: `gpt-4o-mini`) |
| `AZURE_OPENAI_API_KEY` | ഐച്ഛികം — `az login` / Entra ID വേദംമൂലം കീ അടിസ്ഥാന auth വേണ്ടാന്നെങ്കിൽ മാത്രം |

> Responses API സ്ഥിരതയുള്ള `/openai/v1/` എൻഡ്‌പോയിന്റ് ഉപയോഗിക്കുന്നു, അതിനാൽ `api-version` ആവശ്യമായിട്ടില്ല. കീലസ് Entra ID പ്രാമാണീകരണത്തിന് `az login` ഉപയോഗിച്ച് സൈൻ ഇൻ ചെയ്യുക.

## മറ്റ് പ്രൊവൈഡർ: MiniMax (OpenAI-അനുകൂലമാക്കിയ)

[MiniMax](https://platform.minimaxi.com/) വലിയ പ്രാസം തിരമാലകളുള്ള മോഡലുകൾ (204K ടോക്കൺ വരെ) OpenAI-അനുകൂല API വഴിപാടു നൽകുന്നു. Microsoft Agent Framework-ന്റെ `OpenAIChatClient` OpenAI-അനുകൂല എൻഡ്‌പോയിന്റ് കൂടെ പ്രവർത്തിക്കുന്നതിനാൽ, MiniMax Azure OpenAI അല്ലെങ്കിൽ OpenAI-യുടെ പര്യായമായി ഡ്രോപ്പ്-ഇൻ ആയി ഉപയോഗിക്കാം.

നിങ്ങളുടെ `.env` ഫയലിൽ ഈ വേരിയബിൾകൾ ചേർക്കുക:

| വേരിയബിൾ | എവിടെ കണ്ടെത്തും |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API കീകൾ |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` (പ്രീവിധാനം) |
| `MINIMAX_MODEL_ID` | ഉപയോഗിക്കാനുള്ള മോഡൽ നാമം (ഉദാ: `MiniMax-M3`) |

**ഉദാഹരണ മോഡലുകൾ**: `MiniMax-M3` (ശുപാർശചെയ്യുന്നു), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` ( വേഗതയുള്ള മറുപടികൾ). മോഡൽ നാമങ്ങളും ലഭ്യതയും മാറാൻ സാധ്യതയുണ്ട്, നിങ്ങളുടെ അക്കൗണ്ടിനും പ്രദേശത്തിനും അനുസരിച്ച്. നിലവിലെ പട്ടികക്ക് [MiniMax പ്ലാറ്റ്‌ഫോം](https://platform.minimaxi.com/) പരിശോധിക്കുക. നിങ്ങളുടെ അക്കൗണ്ടിന് `MiniMax-M3` ലഭ്യമല്ലെങ്കിൽ, നിങ്ങൾക്കുള്ള ഒരു മോഡലിലേക്ക് `MINIMAX_MODEL_ID` സജ്ജീകരിക്കുക (ഉദാ: `MiniMax-M2.7`).

`OpenAIChatClient` ഉപയോഗിക്കുന്ന കോഡ് സാമ്പിളുകൾ (പാഠം 14 ഹോട്ടൽ ബുക്കിംഗ് വർക്ക്‌ഫ്ലോ പോലുള്ള) `MINIMAX_API_KEY` സജ്ജമാക്കിയാൽ നിങ്ങളുടെ MiniMax ആകമാനിക്കുക സ്വയമേ കണ്ടെത്തുകയും ഉപയോഗിക്കുകയും ചെയ്യും.

## മറ്റ് പ്രൊവൈഡർ: Foundry Local (മოდലുകൾ ഓൺ-ഡിവൈസിൽ റൺ ചെയ്യുക)

[Foundry Local](https://foundrylocal.ai) ഒരു ലഘുവായ റൺടൈം ആണ്, ഭാഷാ മോഡലുകൾ **നിങ്ങളുടെ സ്വന്തം മെഷീനിൽ മുഴുവനായും** ഡൗൺലോഡ് ചെയ്ത് കൈകാര്യം ചെയ്യുകയും OpenAI-അനുകൂല API വഴി സർവिस് ചെയ്യുകയും ചെയ്യുന്നു — ക്ലൗഡ്, Azure സബ്സ്ക്രിപ്ഷൻ അല്ല, API കീകളും ആവശ്യമാണ്. ഓഫ്‌ലൈൻ ഡവലപ്പ്മെന്റിനും ക്ലൗഡ് ചെലവുകൾ ഒഴിവാക്കാനും ഡാറ്റ ഡിവൈസ്-ലെയ്ക്ക് മാത്രമായി സൂക്ഷിക്കാനുമുള്ള ഒരു മികച്ച പരിഹാരമാണ്.

Microsoft Agent Frameworkയുടെ `OpenAIChatClient` OpenAI-അനുകൂല ഏത് എൻഡ്‌പോയിന്റുമായും പ്രവർത്തിക്കുന്നതിനാൽ, Foundry Local Azure OpenAI-യുടെ ഒരു പ്രാദേശിക പകരം കൂടിയാണ്.

**1. Foundry Local ഇൻസ്റ്റാൾ ചെയ്യുക**

```bash
# വിൻഡോസ്
winget install Microsoft.FoundryLocal

# മാക് ഓ.എസ്
brew install foundrylocal
```

**2. ഒരു മോഡൽ ഡൗൺലോഡ് ചെയ്ത് റൺ ചെയ്യുക** (ഇത് പ്രാദേശിക സർവീസ് ആരംഭിക്കുകയും ചെയ്യും):

```bash
foundry model list          # ലഭ്യമായ മോഡലുകൾ കാണുക
foundry model run phi-4-mini
```

**3. പ്രാദേശിക എൻഡ്‌പോയിന്റ് കണ്ടെത്താനുള്ള Python SDK ഇൻസ്റ്റാൾ ചെയ്യുക:**

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework-നെ നിങ്ങളുടെ പ്രാദേശിക മോഡലിലേക്ക് ചൂണ്ടിക്കാണിക്കുക:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# മോഡൽ (ആവശ്യമായാൽ) ഡൗൺലോഡ് ചെയ്ത് ലോക്കലായി സേവനം നൽകുന്നു, പിന്നീട് എൻഡ്‌പോയിന്റ്/പോർട്ട് കണ്ടെത്തുന്നു.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ഉദാ. http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local-ക്കായി എല്ലായ്പ്പോഴും "ആവശ്യമില്ല"
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **കുറിപ്പ്:** Foundry Local OpenAI-അനുകൂല **Chat Completions** എൻഡ്‌പോയിന്റ് ഒന്നാം. പ്രാദേശിക വികസനം, ഓഫ്‌ലൈൻ സാഹചര്യങ്ങൾക്കായി ഇത് ഉപയോഗിക്കുക. പൂർണ്ണ **Responses API** സവിശേഷതകൾക്ക് (സ്ഥിതിസംരക്ഷിച്ച സംഭാഷണങ്ങൾ, ഗഹന ടൂൾ ഓർക്കസ്‌ട്രേഷൻ, ഏജന്റ്-ശൈലി വികസനം) **Azure OpenAI** അല്ലെങ്കിൽ **Microsoft Foundry** പ്രോജക്ടുമായി പ്രവർത്തിക്കുക. നിലവിലെ മോഡൽ പട്ടികയും പ്ലാറ്റ്ഫോം പിന്തുണയും [Foundry Local ഡോക്യുമെന്റേഷൻ](https://foundrylocal.ai) ൽ കാണുക.

## പാഠം 8 (Bing Grounding Workflow) ക്കുള്ള അധിക സജ്ജീകരണം


പാഠം 8ലെ ശിബിരപ്രവര്‍ത്തി കുറിപ്പ് Microsoft Foundry മുഖേന **Bing ഗ്രൗണ്ടിംഗ്** ഉപയോഗിക്കുന്നു. നിങ്ങൾ ആ സാമ്പിൾ ഓടിക്കാൻ പദ്ധതിയിടുകയാണെങ്കിൽ, ഈ വ്യരിയബിൾ നിങ്ങളുടെ `.env` ഫയലിൽ ചേർക്കുക:

| വ്യരിയബിൾ | എവിടെ കണ്ടെത്താം |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry പോർട്ടൽ → നിങ്ങളുടെ പ്രോജക്റ്റ് → **Management** → **Connected resources** → നിങ്ങളുടെ Bing കണക്ഷൻ → കണക്ഷൻ ഐഡി കോപ്പി ചെയ്യുക |

## പ്രശ്നപരിഹാരം

### macOS-ൽ SSL സർട്ടിഫിക്കറ്റ് സ്ഥിരീകരണ പിശകുകൾ

macOS-യില്‍ പ്രവർത്തിക്കുന്നിടത്ത് താഴെപോലുള്ള പിശക് സ്ഥിരീകരിക്കുന്നുണ്ടെങ്കില്‍:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

ഇതു macOS-ൽ Python നു ബന്ധപ്പെട്ട അറിയപ്പെടുന്ന പ്രശ്നമാണ്, സിസ്റ്റം SSL സർട്ടിഫിക്കറ്റുകൾ സ്വയം വിശ്വസിക്കപ്പെടുന്നില്ല. താഴെ പറയുന്ന പരിഹാരങ്ങൾ കക്ഷിക്രമത്തിൽ പരീക്ഷിക്കുക:

**ഓപ്ഷനു 1: Pythonന്റെ ഇൻസ്റ്റാൾ സർട്ടിഫിക്കറ്റുകൾ സ്‌ക്രിപ്റ്റ് ഓടിക്കുക (അനുകൂല്യം)**

```bash
# നിങ്ങളുടെ ഇൻസ്റ്റാൾ ചെയ്ത Python പതിപ്പുമായി 3.XX മാറ്റുക (ഉദാഹരണത്തിന്, 3.12 അല്ലെങ്കിൽ 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ഓപ്ഷനു 2: നിങ്ങളുടെ നോട്ട്ബുക്കിൽ `connection_verify=False` ഉപയോഗിക്കുക (GitHub Models നോട്ട്ബുക്കുകൾക്കു മാത്രം)**

പാഠം 6 നോട്ട്ബുക്കിൽ (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), അഭിപ്രായം ചെയ്ത ഒരുപടியாக പരിഹാരം ഇതിനകം ഉൾപ്പെടുത്തിയിട്ടുണ്ട്. ക്ലയന്റ് സൃഷ്ടിക്കുമ്പോൾ `connection_verify=False` അൺകമ്മെന്റ് ചെയ്യുക:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # സര്‍ട്ടിഫിക്കറ്റ് പിശകുകള്‍ നേരിടുന്നുണ്ടെങ്കില്‍ SSL പരിശോധന നിഷേധിക്കുക
)
```

> **⚠️ മുന്നറിയിപ്പ്:** SSL സ്ഥിരീകരണം ( `connection_verify=False` ) വീഴ്ത്തിയാൽ സർട്ടിഫിക്കറ്റ് സർവകലാശാല ഒഴിവാക്കപ്പെടുന്നതുകൊണ്ട് സുരക്ഷ കുറയുന്നു. വികസന കാലഘട്ടങ്ങളിൽ താൽക്കാലിക പരിഹാരമായി മാത്രമേ ഇത് ഉപയോഗിക്കാവു, ഉത്പാദനത്തിൽ ഒരിക്കലും ഉപയോഗിക്കരുത്.

**ഓപ്ഷനു 3: `truststore` ഇൻസ്റ്റാൾ ചെയ്തു ഉപയോഗിക്കുക**

```bash
pip install truststore
```

പിന്നെ നിങ്ങൾയുടെ നോട്ട്ബുക്കിന്റെ മുകൾഭാഗത്തോ സ്‌ക്രിപ്റ്റ് തുടങ്ങുമ്പോഴോ നെറ്റ്‌വർക്ക് കോളുകൾ നടത്തുന്നതിന് മുമ്പായി ഇതുകൂടി ചേർക്കുക:

```python
import truststore
truststore.inject_into_ssl()
```

## എവിടെയോ കുടുങ്ങിയോ?

ഈ ക്രമീകരണം നടത്തുന്നതിൽ എന്തെങ്കിലും പ്രശ്നങ്ങളുണ്ടെങ്കിൽ, ഞങ്ങളുടെ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> ലേക്ക് ചേരുക അല്ലെങ്കിൽ <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ഒരു പ്രശ്നം സൃഷ്ടിക്കുക</a>.

## അടുത്ത പാഠം

ഈ കോഴ്സിന്റെ കോഡ് ഓടിക്കാൻ നിങ്ങൾ ഇപ്പോൾ സജ്ജമാണ്. AI ഏജന്റുകളുടെ ലോകത്തെ കുറിച്ച് കൂടുതൽ പഠനത്തിൽ സന്തോഷം നേരൂ!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->