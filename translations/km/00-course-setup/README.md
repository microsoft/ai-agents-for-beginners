# ការតំឡើងវគ្គសិក្សា

## ការណែនាំ

មេរៀននេះនឹងបណ្តុះបណទពីវិធីដើម្បីរត់កូដឧទាហរណ៍នៃវគ្គសិក្សានេះ។

## ចូលរួមជាមួយសិស្សផ្សេងទៀត ហើយទទួលបានជំនួយ

មុនពេលអ្នកចាប់ផ្តើមចម្លង repo របស់អ្នក សូមចូលរួមក្នុង [ប៉ុស្តិ៍ Discord របស់ AI Agents សម្រាប់អ្នកចាប់ផ្តើម](https://aka.ms/ai-agents/discord) ដើម្បីទទួលបានជំនួយណាមួយសម្រាប់ការតំឡើង សម្រាប់សំណួរណាមួយទាក់ទងនឹងវគ្គសិក្សា ឬសម្រាប់ភ្ជាប់ទៅអ្នកសិក្សាផ្សេងទៀត។

## ចម្លងឬ Fork repo នេះ

ដើម្បីចាប់ផ្តើម សូមចម្លងឬ fork GitHub Repository។ នេះនឹងបង្កើតជំនាន់ផ្ទាល់ខ្លួនរបស់អ្នកនៃសម្ភារៈវគ្គសិក្សា ដើម្បីអ្នកអាចរត់ បង្កើតតែមើល ជួសជុលកូដបាន!

អ្នកអាចធ្វើការនេះដោយចុចតំណភ្ជាប់ទៅ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repo</a>

ឥឡូវនេះអ្នកគួរតែមានជំនាន់ fork ផ្ទាល់ខ្លួននៃវគ្គសិក្សានៅតាមតំណភ្ជាប់ខាងក្រោម៖

![Forked Repo](../../../translated_images/km/forked-repo.33f27ca1901baa6a.webp)

### រចនាសម្ព័ន shallow clone (ផ្ដល់អនុសាសន៍សម្រាប់វគ្គសិក្សា / Codespaces)

  > រក្សាទុកកន្លែង Repository ពេញលេញអាចធំ (~3 GB) នៅពេលអ្នកទាញយកប្រវត្តិពេញលេញនិងគ្រប់ឯកសារ។ ប្រសិនបើអ្នកត្រឹមតែកំពុងចូលរួមវគ្គសិក្សា ឬត្រឹមតែចង់បានថតមេរៀនមួយចំនួនប៉ុណ្ណោះ រចនាសម្ព័ន shallow clone (ឬ sparse clone) នឹងទាញយកតិចជាង។

#### រចនាសម្ព័ន quick shallow clone — ប្រវត្តិអប្បបរមា, គ្រប់ឯកសារ

ប្តូរ `<your-username>` ក្នុងពាក្យបញ្ជានៅខាងក្រោមជាមួយ URL fork របស់អ្នក (ឬ URL upstream ប្រសើរជាង ប្រសិនបើអ្នកចូលចិត្ត)។

ដើម្បីចម្លងតែប្រវត្តិសកម្មថ្មីបំផុត (ទាញយកតិច):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

ដើម្បីចម្លងបង្អួចភាគច្រើន:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### រចនាសម្ព័ន Partial (sparse) clone — ប្លចតិចបំផុត + ថតដែលបានជ្រើសរើសតែប៉ុណ្ណោះ

នេះប្រើ partial clone និង sparse-checkout (ត្រូវការជំនាន់ Git 2.25+ និងផ្ដល់អនុសាសន៍ដល់ Git នាពេលបច្ចុប្បន្នដែលគាំទ្រ partial clone):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

ចូលទៅក្នុងថត repo:

```bash
cd ai-agents-for-beginners
```

បន្ទាប់មកបញ្ជាក់ថាតើអ្នកចង់បានថតណា (ឧទាហរណ៍ខាងក្រោមបង្ហាញថតពីរ):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

បន្ទាប់ពីចម្លងនិងបញ្ជាក់ឯកសារ ប្រសិនបើអ្នកត្រឹមតែត្រូវការឯកសារ និងចង់ដកដេញកន្លែង (គ្មានប្រវត្តិក្នុង git) សូមលុប metadata repository (💀មិនអាចធ្វើឡើងវិញ — អ្នកនឹងបាត់បង់មុខងារ Git ទាំងអស់):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### ការប្រើ GitHub Codespaces (ផ្ដល់អនុសាសន៍ដើម្បីជៀសវាងការទាញយកធំៗក្នុងម៉ាស៊ីនបន្ទាល់)

- បង្កើត Codespace ថ្មីសម្រាប់ repo នេះតាមរយៈ [GitHub UI](https://github.com/codespaces)។  

- ក្នុង Terminal របស់ codespace ថ្មីបង្កើត រ៉ាន់ពីរ shallow/sparse clone ពីលើដើម្បីយកតែថតមេរៀនដែលអ្នកត្រូវការចូល Codespace workspace។
- ជាជម្រើស៖ បន្ទាប់ពីចម្លងក្នុង Codespaces លុប .git ដើម្បីទទួលបានកន្លែងបន្ថែម (មើលពាក្យបញ្ជាលុបខាងលើ)។
- សម្គាល់៖ ប្រសិនបើអ្នកចូលចិត្តបើក repo ដោយផ្ទាល់ក្នុង Codespaces (ដោយមិនចម្លងបន្ថែម) សូមយល់ថា Codespaces នឹងបង្កើតបរិយាកាស devcontainer និងប្រហែលជានឹងផ្គត់ផ្គង់ច្រើនជាងអ្វីដែលអ្នកត្រូវការនោះទេ។

#### ជំនួយ

- តែងតែបម្លែង URL clone ជាមួយ fork របស់អ្នក ប្រសិនបើអ្នកចង់កែ/បញ្ជូនកូដ។
- ប្រសិនបើអ្នកត្រូវការបន្ថែមប្រវត្តិ ឬឯកសារជាក្រោយ អ្នកអាច fetch យកពួកវា ឬកែ sparse-checkout ដើម្បីបញ្ចូលថតបន្ថែម។

## រត់កូដ

វគ្គសិក្សានេះផ្ដល់ជាស៊េរី Jupyter Notebooks ដែលអ្នកអាចរត់បាន ដើម្បីទទួលបទពិសោធន៍ផ្ទាល់ខ្លួនក្នុងការសាងសង់ AI Agents។

កូដឧទាហរណ៍ប្រើ **Microsoft Agent Framework (MAF)** ជាមួយ `FoundryChatClient` ដែលភ្ជាប់ទៅ **Microsoft Foundry Agent Service V2** (Responses API) តាមរយៈ **Microsoft Foundry**។

កំណត់ត្រា Python ទាំងអស់ត្រូវបានស្លាក `*-python-agent-framework.ipynb`។

## តម្រូវការ

- Python 3.12+
  - **សម្គាល់**៖ ប្រសិនបើអ្នកមិនមាន Python3.12 ដំឡើង សូមធ្វើការដំឡើង។ បន្ទាប់មក បង្កើត venv របស់អ្នកដោយប្រើ python3.12 ដើម្បីធានាថា កំណែត្រឹមត្រូវត្រូវបានដំឡើងពីឯកសារ requirements.txt។
  
    >ឧទាហរណ៍

    បង្កើតថត Python venv៖

    ```bash
    python -m venv venv
    ```

    បន្ទាប់មកធ្វើអាជីវកម្មវេទិកានិង venv សំរាប់:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: សម្រាប់កូដឧទាហរណ៍ដែលប្រើ .NET សុំធានាថាអ្នកបានដំឡើង [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ឬកាន់តែថ្មី។ បន្ទាប់មក ពិនិត្យកំណែ SDK .NET ដែលបានដំឡើងរបស់អ្នក៖

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — តម្រូវសម្រាប់ការផ្ទៀងផ្ទាត់អត្តសញ្ញាណ។ ដំឡើងពី [aka.ms/installazurecli](https://aka.ms/installazurecli)។
- **Azure Subscription** — សម្រាប់ការចូលដំណើរការទៅ Microsoft Foundry និង Microsoft Foundry Agent Service។
- **Microsoft Foundry Project** — គម្រោងដែលមានម៉ូដែលបានដាប់ឡូយ (ឧទាហរណ៍ `gpt-5-mini`)។ មើល៖ [ជំហានទី 1](#ជំហានទី-1៖-បង្កើតគម្រោង-microsoft-foundry) ខាងក្រោម។

យើងបានបញ្ចូលឯកសារ `requirements.txt` នៅក្នុងឫស repo នេះ ដែលមាន paquet Python ត្រូវតែប្រើដើម្បីរត់កូដឧទាហរណ៍ទាំងអស់។

អ្នកអាចដំឡើងពួកវា ដោយរត់ពាក្យបញ្ជាខាងក្រោមក្នុង terminal របស់អ្នកនៅឫស repo៖

```bash
pip install -r requirements.txt
```

យើងផ្ដល់អនុសាសន៍បង្កើតបរិយាកាស Python virtual ដើម្បីជៀសវាងការជំរះ និងបញ្ហាផ្សេងៗ។

## តំឡើង VSCode

ធានាថាអ្នកកំពុងប្រើកំណែ Python ត្រឹមត្រូវក្នុង VSCode។

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## តំឡើង Microsoft Foundry និង Microsoft Foundry Agent Service

### ជំហានទី 1៖ បង្កើតគម្រោង Microsoft Foundry

អ្នកត្រូវការ **hub** និង **គម្រោង** Microsoft Foundry ជាមួយម៉ូដែលបានដាប់ឡូយដើម្បីរត់ notebook។

1. ចូលទៅ [ai.azure.com](https://ai.azure.com) ហើយចុះឈ្មោះជាមួយគណនី Azure របស់អ្នក។
2. បង្កើត **hub** (ឬប្រើ hub ដែលមានស្រាប់)។ មើលៈ [ផែនការដំណើរការ Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)។
3. នៅក្នុង hub សូមបង្កើត **គម្រោង**។
4. ដាប់ឡូយម៉ូដែល (ឧទាហរណ៍ `gpt-5-mini`) ពី **Models + Endpoints** → **Deploy model**។

### ជំហានទី 2៖ ទទួល URL Endpoint របស់គម្រោង និងឈ្មោះការដាប់ឡូយម៉ូដែលរបស់អ្នក

ពីគម្រោងរបស់អ្នកនៅក្នុង Microsoft Foundry portal៖

- **Project Endpoint** — ចូលទៅទំព័រ **Overview** និងចម្លង URL endpoint។

![Project Connection String](../../../translated_images/km/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — ចូលទៅ **Models + Endpoints**, ជ្រើសម៉ូដែលដែលបានដាប់ឡូយរបស់អ្នក ហើយចំណាំ **Deployment name** (ឧទាហរណ៍ `gpt-5-mini`)។

### ជំហានទី 3៖ ចុះឈ្មោះក្នុង Azure ជាមួយ `az login`

ខ្លឹមសារ notebook របស់ភាគច្រើន Authenticate តាមរយៈ **ការចុះឈ្មោះ Azure CLI** — ប្រើ `AzureCliCredential` ឬ `DefaultAzureCredential` (ទាំងពីរគឺយកសម័យ `az login` របស់អ្នក) ពី paquet `azure-identity` — ដូច្នេះពួកវាមិនត្រូវការ API keysទេ។ មេរៀនខ្លះ និងការចូលរួមជាជម្រើសប្រើ API keys; សូមពិនិត្យមើលលក្ខខណ្ឌមុននៃមេរៀនសម្រាប់អថេរផ្សេងទៀតនៅក្នុងបរិយាកាស។ នេះតម្រូវឱ្យអ្នកចុះឈ្មោះតាមរយៈ Azure CLI។

1. **ដំឡើង Azure CLI** ប្រសិនបើអ្នកមិនបានធ្វើ: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **ចុះឈ្មោះ** ដោយរត់ពាក្យបញ្ជា៖

    ```bash
    az login
    ```

    រឺប្រសិនបើអ្នកនៅក្នុងបរិយាកាស remote/Codespace ដោយគ្មាន browser៖

    ```bash
    az login --use-device-code
    ```

3. **ជ្រើសរើស subscription** ប្រសិនបើបានទទួលសំណួរ — ជ្រើស subscription ដែលមានគម្រោង Foundry របស់អ្នក។

4. **ផ្ទៀងផ្ទាត់** អ្នកបានចុះឈ្មោះហើយ៖

    ```bash
    az account show
    ```

> **ហេតុអ្វីបានជា `az login`?** Notebook authenticate ដោយប្រើ `AzureCliCredential` (ឬ `DefaultAzureCredential` ដែលក៏យក session ចុះឈ្មោះ Azure CLI របស់អ្នក) ពី paquet `azure-identity`។ នេះមានន័យថា session Azure CLI របស់អ្នកផ្តល់ការផ្ទៀងផ្ទាត់អត្តសញ្ញាណ — មិនមាន API keys ឬសម្ងាត់ក្នុងឯកសារ `.env`។ នេះគឺជា [អនុវត្តដោយមានសុវត្ថិភាពខ្ពស់](https://learn.microsoft.com/azure/developer/ai/keyless-connections)។

### ជំហានទី 4៖ បង្កើតឯកសារ `.env` របស់អ្នក

ចម្លងឯកសារឧទាហរណ៍៖

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

បើក `.env` ហើយបំពេញតម្លៃទាំងពីរនេះ៖

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| អថេរ | ទីកន្លែងរកបាន |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | ផ្ទាំង Foundry → គម្រោងរបស់អ្នក → ទំព័រ **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | ផ្ទាំង Foundry → **Models + Endpoints** → ឈ្មោះម៉ូដែលដែលបានដាប់ឡូយរបស់អ្នក |

នេះគឺគ្រប់គ្រងសម្រាប់តែប៉ុន្មានមេរៀនភាគច្រើន! Notebook នឹង Authenticate ដោយស្វ័យប្រវត្តិតាម `az login` session របស់អ្នក។

### ជំហានទី 5៖ ដំឡើងការពឹងផ្អែក Python

```bash
pip install -r requirements.txt
```

យើងផ្ដល់អនុសាសន៍ដើម្បីរត់វានៅក្នុងបរិយាកាស virtual ដែលអ្នកបានបង្កើតមុននេះ។

## ការតំឡើងជាជម្រើស៖ Azure AI Search (មេរៀន 5 និង 16)

មេរៀន 5 (Agentic RAG) និង Notebook មេរៀន 16 រត់បានភ្លាមៗជាមួយ **មូលដ្ឋានចំណេះដឹងនៅក្នុងหน่วยចងចាំ** — មិនតម្រូវឱ្យមានធនធាន Azure បន្ថែម។ ប្រសិនបើអ្នកចង់គាំទ្រពួកវាជាមួយរយៈពេលពិត **Azure AI Search** សូមចំណាំថា **Notebook មេរៀន 16 ប្រើការផ្ទៀងផ្ទាត់ដោយ key (key-based authentication)**៖ វាប្ដូរពីការស្វែងរកក្នុងหน่วยចងចាំទៅ Azure AI Search តែពេលដែលទាំងពីរ `AZURE_SEARCH_SERVICE_ENDPOINT` និង `AZURE_SEARCH_API_KEY` ត្រូវបានកំណត់ ហើយវានឹងនៅ​លើការស្វែងរកក្នុងหน่วยចងចាំប៉ុណ្ណោះ — ដូច្នេះដើម្បីរត់វាពីរប្រភេទពិត អ្នកត្រូវតែមើលថែ Admin Key ផងដែរ។ ការផ្ទៀងផ្ទាត់មិនប្រើ Key (keyless) ជាមួយ Microsoft Entra ID (RBAC) គឺជាវិធីសាស្រ្តដែលបានផ្តល់អនុសាសន៍សម្រាប់កូដផលិតកម្មផ្ទាល់ខ្លួនរបស់អ្នក ដែលស្របទៅនឹងប្រព័ន្ធ `az login` ដែលប្រើនៅកន្លែងផ្សេងទៀតក្នុងវគ្គសិក្សានេះ។

ជំហាន RBAC ខាងក្រោមអនុវត្តសម្រាប់គំរូមេនាំផ្ដល់មុខតាមរយៈការណែនាំ និងកូដផ្ទាល់ខ្លួនរបស់អ្នក។ មិនបើកការផ្ទៀងផ្ទាត់ keyless នៅក្នុង Notebook មេរៀន 16 ទេ; Notebook មេរៀន 16 នៅតែត្រូវការទាំង endpoint និង Admin key ដើម្បីប្រើ Azure AI Search។

1. **បើកការចូលដំណើរការតាមតួនាទី** នៅលើសេវាកម្មស្វែងរករបស់អ្នក៖

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **ផ្ដល់តួនាទីដែលត្រូវការ** សម្រាប់ខ្លួនអ្នក (បង្កើត/ទាញយក index និងសំណួរ):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **បន្ថែម endpoint** ទៅឯកសារ `.env` របស់អ្នក៖

| អថេរ | ទីកន្លែងរកបាន |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | ផ្ទាំង Azure → ធនធាន **Azure AI Search** របស់អ្នក → ទំព័រ **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | ត្រូវការ (ជាមួយ endpoint) ដើម្បីបើក Azure AI Search នៅក្នុង Notebook មេរៀន 16 ដែលប្រើ authentication ដោយ key។ ផ្ទាំង Azure → **Settings** → **Keys** → key អ្នកគ្រប់គ្រងសំខាន់ |

> **ហេតុអ្វីបានជា បន្តិចមិនប្រើ Key?** Key អ្នកគ្រប់គ្រងផ្តល់សិទ្ធិការសរសេរ​ពេញលេញទៅសេវាដំណើរការ ស្របពេលដែលកំហុសក្នុង `.env` អាចបញ្ចេញ key ឡើង។ ជាមួយ RBAC អត្តសញ្ញាណ `az login` របស់អ្នកត្រូវបានប្រើជំនួស — គំរូពី Entra ID keyless ដូចដែល notebook នៅក្នុងវគ្គសិក្សា ប្រើ (តាមរយៈ `AzureCliCredential` / `DefaultAzureCredential`)។ មើល [ភ្ជាប់ទៅ Azure AI Search ដោយប្រើតួនាទី](https://learn.microsoft.com/azure/search/search-security-rbac)។

មើល [Azure AI Search មគ្គុទេសក៍តំឡើង](./AzureSearch.md) សម្រាប់គំរូបង្កើត index ពេញលេញក្នុង Python និង .NET។

## ការតំឡើងបន្ថែមសម្រាប់មេរៀនដែលហៅ Azure OpenAI ដោយផ្ទាល់ (មេរៀន 6 និង 8)

notebook ខ្លះក្នុងមេរៀន 6 និង 8 ហៅ **Azure OpenAI** ដោយផ្ទាល់ (ប្រើ **Responses API**) មិនត្រូវបានបណ្តោះអាសន្នជាមួយគម្រោង Microsoft Foundry។ ឧទាហរណ៍ទាំងនេះបានប្រើ GitHub Models មុននេះ ដែលបានបាត់បង់ និងមិនគាំទ្រ Responses API ទេ។ បន្ថែមអថេរទាំងនេះទៅឯកសារ `.env` របស់អ្នក៖

| អថេរ | ទីកន្លែងរកបាន |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | ផ្ទាំង Azure → ធនធាន **Azure OpenAI** របស់អ្នក → **Keys and Endpoint** → Endpoint (ឧទាហរណ៍ `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | ឈ្មោះម៉ូដែលដែលបានដាប់ឡូយ (ឧទាហរណ៍ `gpt-5-mini`) ដែលគាំទ្រ Responses API |
| `AZURE_OPENAI_API_KEY` | ជាជម្រើស — តែប៉ុណ្ណោះបើអ្នកប្រើ authentication ដោយ key មិនមែន `az login` / Entra ID |

> Responses API ប្រើ endpoint មានស្ថិរភាព `/openai/v1/` ដូច្នេះមិនត្រូវការប្រើ `api-version` មួយទេ។ ចុះឈ្មោះជាមួយ `az login` ដើម្បីប្រើ authentication keyless Entra ID។

## អ្នកផ្គត់ផ្គង់ជំនួស៖ MiniMax (គាំទ្រដូច OpenAI)

[MiniMax](https://platform.minimaxi.com/) ផ្ដល់ម៉ូដែល context ធំ (រហូតដល់ 204K tokens) តាមរយៈ API ដែលគាំទ្រដូច OpenAI។ ពីព្រោះ Microsoft Agent Framework `OpenAIChatClient` អាចដំណើរការជាមួយ endpoint គាំទ្រដូច OpenAI អ្នកអាចប្រើ MiniMax ជាជំនួសដោយបញ្ចូលស្វ័យប្រវត្តិសម្រាប់មេរៀនដែលប្រើ `OpenAIChatClient`។

បន្ថែមអថេរទាំងនេះទៅឯកសារ `.env` របស់អ្នក៖

| អថេរ | ទីកន្លែងរកបាន |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | ប្រើ `https://api.minimax.io/v1` (តម្លៃលំនាំដើម) |
| `MINIMAX_MODEL_ID` | ឈ្មោះម៉ូដែលដែលប្រើ (ឧទាហរណ៍ `MiniMax-M3`) |

**ម៉ូដែលឧទាហរណ៍**៖ `MiniMax-M3` (ផ្ដល់អនុសាសន៍), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (មានចម្លើយលឿនជាង)។ ឈ្មោះម៉ូដែលនិងភាពមានស្រាប់អាចផ្លាស់ប្តូរជាលំដាប់សម័យ ហើយការចូលដំណើរការម៉ូដែលណាមួយអាស្រ័យទៅលើគណនីរបស់អ្នក។

កូដឧទាហរណ៍ដែលប្រើ `OpenAIChatClient` (ឧទាហរណ៍ ដំណើរការការកក់សណ្ឋាគារមេរៀន ១៤) នឹងស្វ័យប្រវត្តិយល់ដឹង និងប្រើកំណត់រចនាសម្ព័ន MiniMax របស់អ្នកនៅពេលដែល `MINIMAX_API_KEY` ត្រូវបានកំណត់។


## កម្ម៉ងជំនួស: Foundry Local (រត់ម៉ូដែលលើឧបករណ៍)

[Foundry Local](https://foundrylocal.ai) គឺជារត់ไทម៍ស្រាលដែលទាញយក គ្រប់គ្រង និងបម្រើម៉ូដែលភាសា **ដោយពេញលេញលើកុំព្យូទ័រប្រព័ន្ធរបស់អ្នក** តាមរយៈ API ដែលស្របតាម OpenAI — មិនចាំបាច់ប្រើពពក។

ពីព្រោះ `OpenAIChatClient` នៃ Microsoft Agent Framework អាចប្រើបានជាមួយកន្លែងបញ្ចប់ណាមួយដែលស្របតាម OpenAI បាន, Foundry Local គឺជាកម្ម៉ងជំនួសក្នុងក្នុងសម្រាប់ Azure OpenAI។

**1. តម្លើង Foundry Local**

```bash
# វីនដូوز
winget install Microsoft.FoundryLocal

# ម៉ាក់អូអេស
brew install foundrylocal
```

**2. ទាញយក និងរត់ម៉ូដែល** (នេះក៏ជាចាប់ផ្តើមសេវាកម្មក្នុងក្នុងផងដែរ):

```bash
foundry model list          # មើលម៉ូដែលដែលមានស្រាប់
foundry model run phi-4-mini
```

**3. តម្លើង Python SDK** ដែលប្រើសម្រាប់ស្វែងរកកន្លែងបញ្ចប់ក្នុងក្នុង:

```bash
pip install foundry-local-sdk
```

**4. ចំរុះ Microsoft Agent Framework ទៅម៉ូដែលក្នុងក្នុងរបស់អ្នក:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# ទាញយក (បើចាំបាច់) និងបម្រើគំរូនៅក្នុងតំបន់មូលដ្ឋាន រួចស្វែងរកចំណុចបញ្ចប់/ការច្រក។
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ឧ. http://localhost:<port>/v1
    api_key=manager.api_key,        # តែងតែ "មិនទាមទារ" សម្រាប់ Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **បញ្ជាក់៖** Foundry Local បង្ហាញច្រក **Chat Completions** ដែលស្របតាម OpenAI។ ប្រើវាសម្រាប់ការអភិវឌ្ឍក្នុងក្នុង និងសេណារីយ៉ូក្រៅបណ្តាញ។ សម្រាប់មុខងារ **Responses API** ពេញលេញ (សន្ទនាទាន់សម័យ ល។។), ប្រើ Azure OpenAI ឬគម្រោង Microsoft Foundry។

## ការតម្លើងបន្ថែមសម្រាប់មេរៀន 8 (ដំណើរការ Bing Grounding)

កំណត់ត្រាដំណើរការ ជាភាពលក្ខណៈក្នុងមេរៀន 8 ប្រើ **Bing grounding** តាម Microsoft Foundry។ ប្រសិនបើអ្នកមានគ្រោងរត់គំរូប៏នេះ សូមបន្ថែមអថេរ​នេះទៅឯកសារ `.env` របស់អ្នក៖

| អថេរ | កន្លែងរកបាន |
|----------|-----------------|
| `BING_CONNECTION_ID` | ច្រក Microsoft Foundry → គម្រោងរបស់អ្នក → **ការគ្រប់គ្រង** → **ឧបករណ៍ភ្ជាប់** → ការភ្ជាប់ Bing របស់អ្នក → ចម្លងលេខសម្គាល់នៃការភ្ជាប់ |

## ការជួសជុលបញ្ហា

### សេចក្ដីកំហុសវាយតម្លៃសិទ្ធិ SSL លើ macOS

ប្រសិនបើអ្នកប្រើ macOS ហើយឃើញកំហុសដូចជា៖

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

ព这是ជាបញ្ហាដែលគេស្គាល់ជាមួយ Python លើ macOS ដែលវិញ្ញាបនបត្រ SSL របស់ប្រព័ន្ធមិនត្រូវបានទុកចិត្តដោយស្វ័យប្រវត្តិ។ សូមសាកល្បងដំណោះស្រាយខាងក្រោមក្នុងលំដាប់៖

**ជម្រើស 1: រត់ស្គ្រីប Install Certificates របស់ Python (ផ្ដល់អនុសាសន៍)**

```bash
# ជំនួស 3.XX ជាមួយកំណែ Python ដែលអ្នកបានដំឡើងរួច (ឧ. 3.12 ឬ 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ជម្រើស 2: ប្រើ `connection_verify=False` ក្នុងកំណត់ត្រារបស់អ្នក (សម្រាប់កំណត់ត្រា GitHub Models តែប៉ុណ្ណោះ)**

នៅក្នុងកំណត់ត្រា មេរៀន 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), មានវិធីដោះស្រាយដែលបានមើលមិនចេញដោយបានធ្វើការcomment។ សូមដកcomment `connection_verify=False` ពេលដែលអ្នកជួបកំហុសវិញ្ញាបនបត្រ៖

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # បិទការផ្ទៀងផ្ទាត់ SSL ប្រសិន​បើ​អ្នក​ជួប​កំហុសវិញ្ញាបនប័ត្រ
)
```

> **⚠️ ការព្រមានៈ** ធ្វើឲ្យត្រួតពិនិត្យ SSL មិនដំណើរការ (`connection_verify=False`) បន្ថយសុវត្ថិភាពដោយរំលងការបញ្ជាក់វិញ្ញាបនបត្រ។ ប្រើនូវនេះវាជាវិធីដោះស្រាយបណ្ដោះអាសន្នក្នុងបរិវេណអភិវឌ្ឍន៍ប៉ុណ្ណោះ។ កុំប្រើវានៅក្នុងផលិតកម្ម។

**ជម្រើស 3: តម្លើង និងប្រើ `truststore`**

```bash
pip install truststore
```

រួចបន្ថែមខាងក្រោមនៅលើកំណត់ត្រារបស់អ្នក ឬស្គ្រីប មុនពេលមានការហៅបណ្តាញណាមួយ៖

```python
import truststore
truststore.inject_into_ssl()
```

## ភស្តុតាងធ្វើមិនបាន?

ប្រសិនបើអ្នកប្រឈមនឹងបញ្ហាណាមួយក្នុងការដំណើរការការតំឡើងនេះ សូមចូលរួមក្នុង <a href="https://discord.gg/kzRShWzttr" target="_blank">ក្រុម Azure AI Community Discord</a> ឬ <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">បង្កើតបញ្ហាឡើង</a>។

## មេរៀនបន្ទាប់

ឥឡូវនេះអ្នកបានត្រៀមខ្លួនរួចសម្រាប់រត់កូដសម្រាប់វគ្គសិក្សានេះ។ សូមសំណាងល្អក្នុងការសិក្សាបន្ថែមអំពីពិភពអ្នកទទួល AI!

[ភាពម៉ាស៊ីនសង្ខេបអំពី AI Agents និងករណីប្រើប្រាស់របស់ Agent](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->