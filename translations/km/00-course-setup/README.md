# ការតំឡើងវគ្គសិក្សា

## ការណែនាំ

មេរៀននេះនឹងពន្យល់ពីរបៀបរត់ឧទាហរណ៍កូដនៃវគ្គសិក្សានេះ។

## ចូលរួមជាមួយអ្នករៀនផ្សេងទៀត និងទទួលបានជំនួយ

មុនដែលអ្នកចាប់ផ្តើមក្លូន repo របស់អ្នក សូមចូលរួមក្នុង [ប៊ូស្ត Discord សំរាប់ AI Agents Beginners](https://aka.ms/ai-agents/discord) ដើម្បីទទួលបានជំនួយណាមួយក្នុងការតំឡើង មានសំណួរអំពីវគ្គសិក្សា ឬដើម្បីភ្ជាប់ជាមួយអ្នករៀនផ្សេងទៀត។

## ក្លូន ឬ Fork Repo នេះ

ដើម្បីចាប់ផ្តើម សូមក្លូន ឬ Fork Repository GitHub ។ វានឹងបង្កើតជាម៉ូដែលវគ្គសិក្សារបស់អ្នកឲ្យអាចរត់ តេស្ត និងកែប្រែកូដបាន។

អ្នកអាចធ្វើបានដោយចុចតំណភ្ជាប់ទៅកាន់ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repo</a>

ពេលនេះអ្នកគួរតែមានកំណែ fork ផ្ទាល់ខ្លួននៃវគ្គសិក្សានេះនៅតាមតំណភ្ជាប់ខាងក្រោម៖

![Forked Repo](../../../translated_images/km/forked-repo.33f27ca1901baa6a.webp)

### ក្លូនតំបន់សាមញ្ញ (ផ្ដល់អនុសាសន៍សម្រាប់វេទិកា / Codespaces)

  >Repository ពេញលេញអាចធំ (~3 GB) នៅពេលអ្នកទាញយកប្រវត្តិពេញនិយម និងឯកសារទាំងអស់។ ប្រសិនបើអ្នកត្រឹមតែចូលរួមវេទិកា ឬត្រូវការត្រឹមតែថតមេរៀនមួយចំនួន ក្លូនតំបន់សាមញ្ញ (ឬក៏តំបន់ខ្លះៗ) នឹងទាញយកតិចជាង។

#### ក្លូនតំបន់សាមញ្ញរហ័ស — ប្រវត្តិអតិផរណា, ឯកសារទាំងអស់

ប្ដូរ `<your-username>` នៅក្នុងពាក្យបញ្ជាខាងក្រោមជាមួយ URL fork របស់អ្នក (ឬ URL upstream ប្រសិនបើអ្នកចូលចិត្ត)។

ដើម្បីក្លូនប្រវត្តិ commit ចុងក្រោយតែតែម្ដង (ទូទាញតិច):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

ដើម្បីក្លូនសាខាមួយជាក់លាក់:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### ក្លូនខ្នាតតូច (sparse) — blobs តិច + តែថតជ្រើសរើស

វាប្រើការក្លូនខ្នាតតូច និង sparse-checkout (ទាមទារ Git 2.25+ និងផ្ដល់អនុសាសន៍ប្រើ Git ទាន់សម័យដែលគាំទ្រការក្លូនខ្នាតតូច):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

ចូលក្នុងថត repo៖

```bash
cd ai-agents-for-beginners
```

បន្ទាប់មកបញ្ជាក់ថតដែលអ្នកចង់បាន (ឧទាហរណ៍ខាងក្រោមបង្ហាញពីពីរថត):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

បន្ទាប់ពីក្លូន និងផ្ទៀងផ្ទាត់ឯកសារ ប្រសិនបើអ្នកចង់ទទួលបានតែឯកសារ និងចង់ដោះស្រាយទំហំទិន្នន័យ (គ្មានប្រវត្តិក្រុមហ៊ុន git) សូមលុបមេទាដាតារបស់ repo (💀 មិនអាចត្រឡប់វិញ — អ្នកនឹងបាត់បង់មុខងារ Git ទាំងមូល៖

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### ប្រើ GitHub Codespaces (ផ្ដល់អនុសាសន៍ដើម្បីជៀសវាងការទាញយកធំក្នុងកុំព្យូទ័រផ្ទាល់)

- បង្កើត Codespace ថ្មីសម្រាប់ repo នេះតាមរយៈ [GitHub UI](https://github.com/codespaces)។  

- នៅក្នុង terminal របស់ codespace ថ្មីនេះ រត់កំណត់បញ្ជាក្លូនសាមញ្ញ/ខ្នាតតូចខាងលើ ដើម្បីយកតែថតមេរៀនដែលអ្នកចាំបាច់ចូល Codespace។
- ជាជម្រើស៖ បន្ទាប់ពីក្លូនក្នុង Codespaces សូមលុប .git ដើម្បីបានទំហំលើស (មើលពាក្យបញ្ជាលុបខាងលើ)។
- ចំណាំ៖ ប្រសិនបើអ្នកចូលចិត្តបើក repo ត្រង់ក្នុង Codespaces ដោយមិនត្រូវ fork បន្ថែម អ្នកគួរតែដឹងថា Codespaces នឹងបង្កើតបរិយាកាស devcontainer ហើយប្រហែលជានឹងបញ្ចូលបន្ថែមលើកត្រូវការ។

#### គន្លឹះ

- នៅសព្វថ្ងៃ ជាមួយការប្ដូរតំណភ្ជាប់ក្លូនជាមួយ fork របស់អ្នក ប្រសិនបើអ្នកចង់កែប្រែ/commit។
- ប្រសិនបើអ្នកត្រូវការបន្ថែមប្រវត្តិ ឬឯកសារក្រោយមក អ្នកអាច fetch ឬកែ sparse-checkout ដើម្បីបញ្ចូលថតបន្ថែម។

## រត់កូដ

វគ្គសិក្សានេះផ្តល់ឲ្យមានទំព័រ Jupyter Notebooks ជាច្រើនដែលអ្នកអាចរត់ ដើម្បីទទួលបទពិសោធន៍ដៃក្នុងការបង្កើត AI Agents។

ឧទាហរណ៍កូដប្រើ **Microsoft Agent Framework (MAF)** ដោយប្រើ `FoundryChatClient`, ដែលភ្ជាប់ទៅ **Microsoft Foundry Agent Service V2** (Responses API) តាមរយៈ **Microsoft Foundry**។

សៀវភៅ Python ទាំងអស់ត្រូវបានសម្គាល់ជាមួយឈ្មោះ `*-python-agent-framework.ipynb`។

## តម្រូវការ

- Python 3.12+
  - **ចំណាំ**៖ ប្រសិនបើអ្នកមិនទាន់ដំឡើង Python3.12 សូមដំឡើងវា។ ប្រាកដថាបង្កើត venv របស់អ្នកដោយប្រើ python3.12 ដើម្បីធានាថាភាសា និងកំណែត្រឹមត្រូវត្រូវបានដំឡើងពីឯកសារ requirements.txt។
  
    >ឧទាហរណ៍

    បង្កើតថត venv របស់ Python:

    ```bash
    python -m venv venv
    ```

    បន្ទាប់មកបើកបរិយាកាស venv សម្រាប់:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: សម្រាប់ឧទាហរណ៍កូដដែលប្រើ .NET សូមប្រាកដថាទៅដំឡើង [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ឬកំណែថ្មីបំផុត។ បន្ទាប់មកពិនិត្យកំណែ .NET SDK ដែលបានដំឡើង៖

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — តម្រូវសម្រាប់ការផ្ទៀងផ្ទាត់។ ដំឡើងពី [aka.ms/installazurecli](https://aka.ms/installazurecli)។
- **ការជាវ Azure** — ដើម្បីចូលដំណើរការ Microsoft Foundry និង Microsoft Foundry Agent Service។
- **Microsoft Foundry Project** — គម្រោងមួយដែលមានគំរូបានដាក់ចេញ (ឧ. `gpt-5-mini`)។ មើល [ជំហាន 1](#ជំហាន-1៖-បង្កើតគម្រោង-microsoft-foundry) ខាងក្រោម។

យើងបានបញ្ចូលឯកសារ `requirements.txt` នៅក្នុងឫស repo នេះ ដែលមានវត្ថុ Python ទាំងអស់ដែលត្រូវការដើម្បីរត់ឧទាហរណ៍កូដ។

អ្នកអាចដំឡើងវាតាមការបញ្ជារខាងក្រោមនៅក្នុង terminal របស់អ្នកនៅក្នុងឫស repo៖

```bash
pip install -r requirements.txt
```

យើងផ្ដល់អនុសាសន៍ឲ្យបង្កើតបរិយាកាស Python virtual ដើម្បីជៀសវាងការជ្រុលគ្នា និងបញ្ហានានា។

## តំឡើង VSCode

សូមប្រាកដថាអ្នកកំពុងប្រើកំណែ Python ត្រឹមត្រូវនៅក្នុង VSCode។

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## តំឡើង Microsoft Foundry និង Microsoft Foundry Agent Service

### ជំហាន 1៖ បង្កើតគម្រោង Microsoft Foundry

អ្នកត្រូវការម្ចាស់ hub និងគម្រោង Microsoft Foundry ដែលមានគំរូបានដាក់ចេញ ដើម្បីរត់សៀវភៅកំណត់ត្រា។

1. ចូលទៅ [ai.azure.com](https://ai.azure.com) ហើយចុះឈ្មោះជាមួយគណនី Azure របស់អ្នក។
2. បង្កើត **hub** ថ្មី (ឬប្រើមួយដែលមានរួចមកហើយ)។ មើល: [ពិពណ៌នាសម្ភារៈ hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)។
3. នៅក្នុង hub បង្កើត **គម្រោង**។
4. ដាក់ផ្សាយគំរូ (ឧ. `gpt-5-mini`) ពី **Models + Endpoints** → **Deploy model**។

### ជំហាន 2៖ ទាញយក Endpoint និងឈ្មោះការដាក់ផ្សាយគំរូរបស់គម្រោងអ្នក

ពីគម្រោងរបស់អ្នកនៅក្នុងកំពូល Microsoft Foundry ៖

- **Project Endpoint** — ចូលទៅទំព័រ **Overview** ហើយចម្លង URL endpoint ។

![Project Connection String](../../../translated_images/km/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — ចូលទៅ **Models + Endpoints** ជ្រើសម៉ូដែលដែលបានដាក់ចេញ ហើយចំណាំឈ្មោះ **Deployment name** (ឧ. `gpt-5-mini`)។

### ជំហាន 3៖ ចុះឈ្មោះចូល Azure ជាមួយ `az login`

សៀវភៅកំណត់ត្រាច្រើន authenticate តាមរយៈ **Azure CLI ចុះឈ្មោះចូល** — ប្រើ `AzureCliCredential` ឬ `DefaultAzureCredential` (ទាំងពីរចាប់ session `az login` របស់អ្នក) ពី `azure-identity` package — ដូច្នេះគ្មានការទាមទារកូន API keys។ មេរៀន និងការជួសជុលជាជម្រើសខ្លះប្រើ API keys; សូមពិនិត្យមើលគ្រប់អត្រាទុនមេរៀនសម្រាប់ម៉ូឌុលបរិស្ថានបន្ថែមណាមួយ។ នេះតម្រូវឲ្យអ្នកបានចុះឈ្មោះចូលតាមរយៈ Azure CLI។

1. **ដំឡើង Azure CLI** ប្រសិនបើអ្នកមិនទាន់ដំឡើង៖ [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **ចុះឈ្មោះចូល** ដោយរត់៖

    ```bash
    az login
    ```

    បើអ្នកនៅក្នុងបរិយាកាស remote/Codespace ដែលមិនមាន browser:

    ```bash
    az login --use-device-code
    ```

3. **ជ្រើសការជាវ** ប្រសិនបើត្រូវបានស្នើ — ជ្រើសណាមួយនៅក្នុងគម្រោង Foundry របស់អ្នក។

4. **ផ្ទៀងផ្ទាត់** អ្នកបានចូលឈ្មោះចូលទេ៖

    ```bash
    az account show
    ```

> **ហេតុអ្វីបានជា `az login`?** សៀវភៅកំណត់ត្រានេះ authenticate ប្រើ `AzureCliCredential` (ឬ `DefaultAzureCredential` ដែលក៏ថត session Azure CLI របស់អ្នកផងពី `azure-identity` package)។ នេះមានន័យថា session Azure CLI របស់អ្នកផ្ដល់ឲ្យ凭证 — គ្មាន API keys ឬសំងាត់នៅក្នុងឯកសារ `.env` របស់អ្នក។ នេះគឺជា [អនុសាសន៍ជាសុវត្ថិភាពល្អបំផុត](https://learn.microsoft.com/azure/developer/ai/keyless-connections)។

### ជំហាន 4៖ បង្កើតឯកសារ `.env` របស់អ្នក

ចម្លងឯកសារឧទាហរណ៍៖

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

បើក `.env` ហើយបញ្ចូលតម្លៃពីរនេះ៖

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| អថេរ | ត្រូវស្វែងរកនៅណា |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | ផតថល Foundry → គម្រោងរបស់អ្នក → ទំព័រ **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | ផតថល Foundry → **Models + Endpoints** → ឈ្មោះម៉ូដែលបានដាក់ចេញ |

នេះគឺគ្រប់គ្រាន់សម្រាប់មេរៀនភាគច្រើន! សៀវភៅកំណត់ត្រានឹង authenticate ជាអ្វីដោយស្វ័យប្រវត្តិតាម session `az login` របស់អ្នក។

### ជំហាន 5៖ ដំឡើងអាស្រ័យភាព Python

```bash
pip install -r requirements.txt
```

យើងផ្ដល់អនុសាសន៍រត់នេះក្នុងបរិយាកាស virtual ដែលអ្នកបានបង្កើតមុននេះ។

## ការតំឡើងបន្ថែមជាជម្រើស: Azure AI Search (មេរៀន 5 និង 16)

មេរៀន 5 (Agentic RAG) និង មេរៀន 16 រត់បានតាមលក្ខណៈ **in-memory knowledge base** — មិនទាមទារបន្ថែមផ្នែកAzure។ បើអ្នកចង់ចូលបញ្ចូលជាជំនួយជាមួយ **Azure AI Search** index ពិតប្រាកដ សូមចំណាំថា **សៀវភៅកំណត់ត្រា មេរៀន 16 ប្រើការផ្ទៀងផ្ទាត់ជាមួយ key-based**៖ វាប្រែពីការស្វែងរក in-memory ទៅ Azure AI Search តែពេលដែល **ទាំងពីរ** `AZURE_SEARCH_SERVICE_ENDPOINT` **និង** `AZURE_SEARCH_API_KEY` ត្រូវបានកំណត់រួច ហើយមិនដំណើរការជាមួយ in-memory search ទេ។ ដើម្បីរត់លើ index ពិតប្រាកដ អ្នកត្រូវដាក់សោរអ្នកគ្រប់គ្រងផងដែរ។ ការផ្ទៀងផ្ទាត់ keyless ជាមួយ Microsoft Entra ID (RBAC) មានសក្តានុពលសម្រាប់កូដផលិតកម្មផ្ទាល់ខ្លួនរបស់អ្នក ដូចត្រូវគ្នាជាមួយខ្សែអ្វី `az login` ដែលប្រើទូទាំងវគ្គសិក្សានេះ។

ជំហាន RBAC ខាងក្រោមអនុវត្តសម្រាប់តែមួយឧទាហរណ៍នៃកម្មវិធី ព្រមទាំងកូដរបស់អ្នកផ្ទាល់។ វាមិនបើកការផ្ទៀងផ្ទាត់ keyless សម្រាប់សៀវភៅកំណត់ត្រា មេរៀន 16; មេរៀន 16 តម្រូវឲ្យមានទាំងអស់ពី endpoint និង key admin ដើម្បីប្រើ Azure AI Search។

1. **បើកការចូលប្រើដោយផ្អែកលើតួនាទី** នៅលើសេវាកម្មស្វែងរករបស់អ្នក:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **ផ្ដល់តួនាទីដែលត្រូវការឱ្យខ្លួនអ្នក** (បង្កើត/ផ្ទុក Index ឬសួរសំណួរ):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **បញ្ចូល endpoint** ទៅក្នុងឯកសារ `.env` របស់អ្នក:

| អថេរ | ត្រូវស្វែងរកនៅណា |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | ផតថល Azure → អ្នកធនធាន **Azure AI Search** របស់អ្នក → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | ត្រូវការ (ជាមួយ endpoint) ដើម្បីបើក Azure AI Search ក្នុងសៀវភៅកំណត់ត្រា មេរៀន 16 ដែលប្រើ auth based key។ ផតថល Azure → **Settings** → **Keys** → សោរអ្នកគ្រប់គ្រងសំខាន់ |

> **ហេតុអ្វី Keyless?** សោរ admin ផ្តល់សិទ្ធិបញ្ចូលទិន្នន័យពេញលេញទៅសេវាកម្មស្វែងរករបស់អ្នក ងាយរអាការ​ក្នុងឯកសារ `.env`។ ជាមួយ RBAC អត្តសញ្ញាណ `az login` របស់អ្នកត្រូវបានប្រើជំនួស — គំរូ keyless Entra ID ដែលសៀវភៅកំណត់ត្រាវគ្គសិក្សាប្រើ (តាម `AzureCliCredential` / `DefaultAzureCredential`)។ មើល [ភ្ជាប់ទៅ Azure AI Search ដោយប្រើតួនាទី](https://learn.microsoft.com/azure/search/search-security-rbac)។

សូមមើល [មេរៀងឲ្យបំពេញ Azure AI Search](./AzureSearch.md) សម្រាប់ឧទាហរណ៍បង្កើត index សព្វក្នុង Python និង .NET។

## ការតំឡើងបន្ថែមសម្រាប់មេរៀនដែលហៅ Azure OpenAI ត្រង់ (មេរៀន 6 និង 8)

សៀវភៅកំណត់ត្រាមួយចំនួននៅមេរៀន 6 និង 8 ហៅ **Azure OpenAI** ត្រង់ (ប្រើ **Responses API**) ជំនួស Microsoft Foundry project។ ឧទាហរណ៍ទាំងនេះធ្លាប់ប្រើ GitHub Models ដែលត្រូវបានចាកចេញ ហើយមិនគាំទ្រ Responses API ទេ។ ចូលបន្ថែមអថេរទាំងនេះក្នុង `.env` របស់អ្នក៖

| អថេរ | ត្រូវស្វែងរកនៅណា |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | ផតថល Azure → អ្នកធនធាន **Azure OpenAI** → **Keys and Endpoint** → Endpoint (ឧ. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | ឈ្មោះម៉ូដែលដែលបានដាក់ចេញ (ឧ. `gpt-5-mini`) ដែលគាំទ្រ Responses API |
| `AZURE_OPENAI_API_KEY` | ជាជម្រើស — ប្រសិនបើអ្នកប្រើ authentication ជាមួយ key ជំនួស `az login` / Entra ID |

> Responses API ប្រើ stable `/openai/v1/` endpoint ដូច្នេះមិនត្រូវការ `api-version` នោះទេ។ ចូលដំណើរការជាមួយ `az login` ដើម្បីប្រើ authentication keyless Entra ID។

## អ្នកផ្គត់ផ្គង់ជំនួយជម្រើស៖ MiniMax (គាំទ្រ OpenAI-Compatible)

[MiniMax](https://platform.minimaxi.com/) ផ្តល់ម៉ូដែល context ធំ (រហូតដល់ 204K tokens) តាម API ដែលគាំទ្រអោយ OpenAI។ ពីព្រោះ Microsoft Agent Framework `OpenAIChatClient` ដំណើរការជាមួយ endpoint ដែលគាំទ្រ OpenAI អ្នកអាចប្រើ MiniMax ជាជំនួសឆ្លើយតបទៅមេរៀនដែលប្រើ `OpenAIChatClient`។

ចូលបន្ថែមអថេរទាំងនេះក្នុង `.env` របស់អ្នក៖

| អថេរ | ត្រូវស្វែងរកនៅណា |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → កូន API Keys |
| `MINIMAX_BASE_URL` | ប្រើ `https://api.minimax.io/v1` (តម្លៃលំនាំដើម) |
| `MINIMAX_MODEL_ID` | ឈ្មោះម៉ូដែលដែលត្រូវប្រើ (ឧ. `MiniMax-M3`) |

**ម៉ូដែលឧទាហរណ៍**៖ `MiniMax-M3` (ផ្ដល់អនុសាសន៍), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (ឆ្លើយតបលឿន)។ ឈ្មោះម៉ូដែល និងមានភាពអាចប្រើបានអាចប្រែប្រួលគ្នាតាមពេលវេលា ហើយការចូលដំណើរការម៉ូដែលមួយអាចអាស្រ័យលើយើងមានគណនី។

ឧទាហរណ៍កូដដែលប្រើ `OpenAIChatClient` (ឧ. ការចាត់តាំងផ្ទះសណ្ឋាគារមេរៀន 14) នឹងរកឃើញ និងប្រើការកំណត់រចនាសម្ព័ន្ធ MiniMax របស់អ្នកដោយស្វ័យប្រវត្តិពេល `MINIMAX_API_KEY` ត្រូវបានកំណត់។


## ផ្គត់ផ្គង់ជំនួស៖ Novita AI (សមស្របជាមួយ OpenAI)

[Novita AI](https://novita.ai/llm-api) ផ្តល់ជូន API សមស្របជាមួយ OpenAI សម្រាប់ LLMs ជីវចលដំណើរការដោយប្រភពបើក និងអនាគត (DeepSeek, Llama, Qwen, និងផ្សេងទៀត)។ ពីព្រោះ `OpenAIChatClient` របស់ Microsoft Agent Framework អាចដំណើរការជាមួយ endpoint ស្មើ OpenAI អ្វីក៏បាន អ្នកអាចប្រើប្រាស់ Novita AI ជាជម្រើសជំនួសបញ្ចូលដោយផ្ទាល់ទៅ Azure OpenAI ឬ OpenAI។

បន្ថែមអថេរទាំងនេះទៅក្នុងឯកសារ `.env` របស់អ្នក៖

| អថេរ | កន្លែងដែលអាចរកបាន |
|----------|-----------------|
| `NOVITA_API_KEY` | [ផ្ទាំងគ្រប់គ្រង Novita AI](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | ប្រើ `https://api.novita.ai/openai/v1` (តម្លៃលំនាំដើម) |
| `NOVITA_MODEL_ID` | ឈ្មោះម៉ូដែលសម្រាប់ប្រើ (ឧ. `moonshotai/kimi-k3`) |

**ម៉ូដែលគំរូ**៖ `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`។ Novita AI ក៏ផ្តល់ម៉ូដែលជាច្រើនទៀតដោយប្រភពបើក (Llama, Qwen, GLM, និងផ្សេងទៀត) — សូមពិនិត្យមើល [បណ្ណាល័យម៉ូដែល Novita AI](https://novita.ai/llm-api) សម្រាប់បញ្ជីម៉ូដែលដែលមាន និង ID ម៉ូដែលរបស់ពួកវា។

ឧទាហរណ៍បច្ចុប្បន្នមិនទទួលយកអថេរ `NOVITA_*` ដោយស្វ័យប្រវត្តិទេ។ ដើម្បីប្រើ Novita AI អ្នកត្រូវផ្តល់តម្លៃទាំងនេះដោយច្បាស់នៅពេលបង្កើត `OpenAIChatClient` ក្នុងឧទាហរណ៍ដែលអ្នកកំពុងដំណើរការ។

## ផ្គត់ផ្គង់ជំនួស៖ Foundry Local (រត់ម៉ូដែលលើឧបករណ៍ផ្ទាល់)

[Foundry Local](https://foundrylocal.ai) គឺជា runtime ទម្ងន់ស្រាលមួយដែលទាញយក គ្រប់គ្រង និងផ្តល់សេវាម៉ូដែលភាសា **ពេញលេញលើម៉ាស៊ីនផ្ទាល់របស់អ្នក** តាមរយៈ API សមស្របជាមួយ OpenAI — មិនចាំបាច់មាន cloud ទេ។

ពីព្រោះ `OpenAIChatClient` របស់ Microsoft Agent Framework អាចដំណើរការជាមួយ endpoint ស្មើ OpenAI គ្រប់ប្រភេទ Foundry Local ជាជម្រើសប្រែប្រួលក្នុងតំបន់លើ Azure OpenAI។

**១. ហៅបញ្ចូល Foundry Local**

```bash
# វីនដូ
winget install Microsoft.FoundryLocal

# ម៉ាក់អូស
brew install foundrylocal
```

**២. ទាញយក និងដំណើរការម៉ូដែល** (វាក៏ចាប់ផ្តើមសេវាកម្មក្នុងតំបន់ផងដែរ)៖

```bash
foundry model list          # មើលម៉ូឌែលដែលមានស្រាប់
foundry model run phi-4-mini
```

**៣. ដំឡើង Python SDK** ដែលប្រើសម្រាប់ស្វែងរក endpoint ក្នុងតំបន់៖

```bash
pip install foundry-local-sdk
```

**៤. បង្ហាញ Microsoft Agent Framework ទៅម៉ូដែលក្នុងតំបន់របស់អ្នក៖**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# ទាញយក (ប្រសិនបើចាំបាច់) ហើយបម្រើម៉ូឌែលនៅក្នុងកន្លែងវិញ បន្ទាប់មករកមើលចំណុចចេញ/ច្រក។
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ឧទាហរណ៍ http://localhost:<port>/v1
    api_key=manager.api_key,        # តែងតែ "មិនចាំបាច់" សម្រាប់ Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **ចំណាំ៖** Foundry Local បង្ហាញ endpoint **Chat Completions** ដែលស្របជាមួយ OpenAI។ ប្រើវាសម្រាប់ការអភិវឌ្ឍក្នុងតំបន់ និងករណីក្រៅបណ្តាញ។ សម្រាប់លក្ខណៈពិសេស **Responses API** (ជជែកមានស្ថានភាព ល។) សូមប្រើ Azure OpenAI ឬគម្រោង Microsoft Foundry។

## ការតំរូវបន្ថែមសម្រាប់មេរៀនទី 8 (ដំណើរការជាមួយ Bing Grounding)

កម្មវិធីដំណើរការជាកម្មវិធីកំឡុងដែលមានលក្ខខណ្ឌ ក្នុងមេរៀនទី 8 ប្រើ **Bing grounding** តាមរយៈ Microsoft Foundry។ ប្រសិនបើអ្នកមានផែនការរត់ឧទាហរណ៍នោះ សូមបន្ថែមអថេរនេះទៅ `.env` របស់អ្នក៖

| អថេរ | កន្លែងដែលអាចរកបាន |
|----------|-----------------|
| `BING_CONNECTION_ID` | ទំព័របណ្ដាញ Microsoft Foundry → គម្រោងរបស់អ្នក → **Management** → **Connected resources** → ការតភ្ជាប់ Bing របស់អ្នក → ចម្លង ID ការតភ្ជាប់ |

## ដោះសោបញ្ហា

### ការផ្ទៀងផ្ទាត់សញ្ញាបត្រ SSL លើ macOS មានបញ្ហា

ប្រសិនបើអ្នកកំពុងប្រើ macOS ហើយជួបប្រទៈកំហុសដូចជា៖

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

នេះគឺជាបញ្ហារស់រានមានជីវិតថ្ងៃនៅ Python លើ macOS ដែលសញ្ញាបត្រ SSL ស្ថិតក្នុងប្រព័ន្ធមិនត្រូវទុកចិត្តដោយស្វ័យប្រវត្តិទេ។ សូមព្យាយាមដំណោះស្រាយខាងក្រោមតាមលំដាប់៖

**ជម្រើស១៖ រត់ script ការដំឡើងសញ្ញាបត្ររបស់ Python (ណែនាំ)**

```bash
# ជំនួស 3.XX ជាមួយកំណែ Python ដែលអ្នកបានដំឡើង (ឧ. 3.12 ឬ 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ជម្រើស២៖ ប្រើ `connection_verify=False` ក្នុង notebook របស់អ្នក (សម្រាប់ notebook ម៉ូដែល GitHub តែប៉ុណ្ណោះ)**

នៅក្នុង notebook មេរៀនទី 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), មានរបៀបដោះស្រាយដែលបាន comment ពីមុនរួច។ សូមដក comment `connection_verify=False` ពេលដែលជួបកំហុសអត្តសញ្ញាណសញ្ញាបត្រ៖

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # បិទការត្រួតពិនិត្យ SSL ប្រសិនបើអ្នកប្រឈមមុខនឹងកំហុសវិញ្ញាបនបត្រ
)
```

> **⚠️ ការព្រមាន៖** ការបិទការផ្ទៀងផ្ទាត់ SSL (`connection_verify=False`) បន្ថយសុវត្ថិភាពដោយរំលងការត្រួតពិនិត្យសញ្ញាបត្រ។ សូមប្រើលទ្ធផលនេះតែជា វិធីសាស្រ្តបណ្តោះអាសន្នក្នុងបរិបទអភិវឌ្ឍន៍ ប៉ុណ្ណោះ។ មិនគួរប្រើក្នុងផលិតកម្មឡើយ។

**ជម្រើស៣៖ ការដំឡើង និងប្រើ `truststore`**

```bash
pip install truststore
```

បន្ទាប់មកបន្ថែមកូដខាងក្រោមនៅខាងលើ notebook ឬ script របស់អ្នក មុនពេលទាក់ទងបណ្តាញណាមួយ៖

```python
import truststore
truststore.inject_into_ssl()
```

## ត្រូវមានការពិបាកនៅកន្លែងណាមួយ?

ប្រសិនបើមានបញ្ហាណាមួយក្នុងការរត់ការតំឡើងនេះ សូមចូលរួមក្នុង <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> រឺ <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">បង្កើតបញ្ហា</a>។

## មេរៀនបន្ទាប់

ឥឡូវនេះអ្នកបានរៀបចំរួចហើយសម្រាប់រត់កូដសិក្សាសម្រាប់វគ្គនេះ។ សូមរៀនសូត្រកាន់តែច្រើនអំពីពិភព AI Agents! 

[ការណែនាំអំពី AI Agents និងករណីប្រើប្រាស់ Agent](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->