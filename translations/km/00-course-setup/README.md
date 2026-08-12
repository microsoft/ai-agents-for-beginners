# ការតំឡើងវគ្គសិក្សា

## ការណែនាំ

មេរៀននេះនឹងពិភាក្សាពីរបៀបដំណើរការឧទាហរណ៍កូដនៃវគ្គសិក្សានេះ។

## ចូលរួមជាមួយអ្នករៀនផ្សេងទៀត និងទទួលបានជំនួយ

មុនពេលអ្នកចាប់ផ្តើមបង្កើតច្បាប់ចម្លង repo របស់អ្នក សូមចូលរួមក្នុង [ប៉ុស្តិ៍ AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) ដើម្បីទទួលបានជំនួយណាមួយទាក់ទងនឹងការតំឡើង, សំណួរអំពីវគ្គសិក្សា, ឬដើម្បីភ្ជាប់ជាមួយអ្នករៀនផ្សេងទៀត។

## ចម្លងឬចុះបញ្ជី Fork Repo នេះ

ដើម្បីចាប់ផ្តើម សូមចម្លងឬ fork GitHub Repository។ នេះនឹងបង្កើតជំនាន់ផ្ទាល់ខ្លួនរបស់អ្នកនៃសម្ភារៈវគ្គសិក្សា ដើម្បីអោយអ្នកអាចដំណើរការ, សាកល្បង, និងកែប្រែកូដបាន!

អ្នកអាចធ្វើបានដោយចុចលីងទៅ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a>

ឥឡូវនេះអ្នកគួរតែមានជំនាន់ fork ផ្ទាល់ខ្លួនរបស់វគ្គសិក្សានេះនៅលីងដូចខាងក្រោម៖

![Forked Repo](../../../translated_images/km/forked-repo.33f27ca1901baa6a.webp)

### ចម្លង Shallow (ផ្ដល់អនុសាសន៍សម្រាប់សិក្ខាសាលា / Codespaces)

  >Repository ពេញលេញអាចធំ (~3 GB) នៅពេលអ្នកទាញយកប្រវត្តិពេញលេញនិងឯកសារទាំងអស់។ ប្រសិនបើអ្នកតែចូលរួមសិក្ខាសាលា ឬត្រូវការត្រឹមតែមេរៀនខ្លះៗទេ ភាពចម្លង shallow (ឬ sparse clone) នឹងជៀសវាងការទាញយកភាគច្រើនដោយកាត់បន្ថយប្រវត្តិនិង/ឬបដិសេធ blobs។

#### ចម្លង shallow លឿន — ប្រវត្តិទាបជាង គ្រប់ឯកសារ

ជំនួស `<your-username>` ក្នុងពាក្យបញ្ជានៅខាងក្រោមជាមួយ URL fork របស់អ្នក (ឬ URL upstream ប្រសិនបើអ្នកចូលចិត្ត)។

ដើម្បីចម្លងតែប្រវត្តិ commit ចុងក្រោយប៉ុណ្ណោះ (ទាញយកតិច):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

ដើម្បីចម្លងសាខាតែមួយច្បាស់លាស់:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### ចម្លង​បង្រួម (sparse) — blobs ទាបបំផុត + ត្រឹមតែថតដែលបានជ្រើសរើស

វានៅត្រូវការចម្លងបង្រួម និង sparse-checkout (តម្រូវ Git 2.25+ និងផ្ដល់អនុសាសន៍ថ្មីសម្រាប់ Git មាន partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

ចូលទៅក្នុងថត repo:

```bash|powershell
cd ai-agents-for-beginners
```

បន្ទាប់មកបញ្ជាក់ថតដែលអ្នកចង់បាន (ឧទាហរណ៍ខាងក្រោមបង្ហាញពីពីរថត):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

បន្ទាប់ពីចម្លងនិងផ្ទៀងផ្ទាត់ឯកសារ ប្រសិនបើអ្នកត្រូវការតែឯកសារនិងចង់សំអាតកន្លែងទំនេរ (គ្មានប្រវត្តិ git) សូមលុបបណ្តាញទិន្នន័យ repo (💀 មិនអាចប្រតិបត្តិឡើងវិញ — អ្នកនឹងបាត់បង់មុខងារ Git ទាំងឡាយ៖ គ្មាន commit, pull, push ឬការចូលប្រវត្តិ)។

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### ប្រើ GitHub Codespaces (ផ្ដល់អនុសាសន៍ដើម្បីជៀសវាងការទាញយកធំៗនៅក្នុងម៉ាស៊ីន)

- បង្កើត Codespace ថ្មីសម្រាប់ repo នេះតាមរយៈ [GitHub UI](https://github.com/codespaces)។  

- នៅក្នុង terminal របស់ codespace ថ្មី បើកដំណើរការបញ្ជា shallow/sparse clone ខាងលើដើម្បីយកតែថតមេរៀនដែលអ្នកត្រូវការចូលទៅក្នុងបរិយាកាស Codespace។
- ជម្រើសបន្ថែម៖ បន្ទាប់ពីចម្លងក្នុង Codespaces សូមដក .git ដើម្បីស្ដារកន្លែងបន្ថែម (មើលបញ្ជាដកចេញខាងលើ)។
- សម្គាល់៖ ប្រសិនបើអ្នកចូលចិត្តបើក repo ដោយផ្ទាល់នៅក្នុង Codespaces (គ្មានការចម្លងបន្ថែម) សូមយល់ព្រមថា Codespaces នឹងរៀបចំបរិយាកាស devcontainer ហើយអាចនឹងពន្លឿនការផ្គត់ផ្គង់លើសត្រូវការដែរ។ ការ fork ចម្លង shallow ក្នុង Codespace ថ្មីផ្តល់ឱ្យអ្នកការត្រួតពិនិត្យល្អជាងការប្រើទំហំ hard disk។

#### យោបល់ជំនួយ

- តែងតែជំនួស URL ចម្លងជាមួយ fork របស់អ្នកប្រសិនបើចង់កែប្រែ/commit។
- ប្រសិនបើអ្នកត្រូវការប្រវត្តិឬឯកសារបន្ថែមពេលក្រោយ អ្នកអាច fetch ឬកែ sparse-checkout ដើម្បីបញ្ចូលថតបន្ថែម។

## ដំណើរការកូដ

វគ្គសិក្សានេះផ្តល់អោយនូវ Jupyter Notebooks ដែលអ្នកអាចដំណើរការដើម្បីទទួលបទពិសោធន៍ដៃលើការបង្កើត AI Agents។

ឧទាហរណ៍កូដប្រើ **Microsoft Agent Framework (MAF)** ជាមួយ `FoundryChatClient` ដែលភ្ជាប់ទៅកាន់ **Microsoft Foundry Agent Service V2** (API Responses) តាមរយៈ **Microsoft Foundry**។

កំណត់ត្រា Python ទាំងអស់ត្រូវបានស្លាក `*-python-agent-framework.ipynb`។

## តម្រូវការ

- Python 3.12+
  - **សម្គាល់**៖ ប្រសិនអ្នកមិនមាន Python3.12 ត្រូវតែដំឡើងវា។ បន្ទាប់មកបង្កើត venv របស់អ្នកដោយប្រើ python3.12 ដើម្បីធានាថាចំំណែកត្រូវបានដំឡើងត្រឹមត្រូវពី requirements.txt។
  
    >ឧទាហរណ៍

    បង្កើតថត Python venv:

    ```bash|powershell
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

- .NET 10+: សម្រាប់ឧទាហរណ៍កូដដែលប្រើ .NET សូមដំឡើង [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ឬថ្មីជាងនេះ។ បន្ទាប់មកពិនិត្យមើលកំណែ .NET SDK ដែលបានដំឡើងរបស់អ្នក។

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — តម្រូវឲ្យមានសម្រាប់ការផ្ទៀងផ្ទាត់។ ដំឡើងពី [aka.ms/installazurecli](https://aka.ms/installazurecli)។
- **Azure Subscription** — សម្រាប់ចូលដំណើរការទៅ Microsoft Foundry និង Microsoft Foundry Agent Service។
- **Microsoft Foundry Project** — គម្រោងមួយដែលមានម៉ូដែលបានចុះបញ្ជី (ឧ. `gpt-5-mini`)។ មើល [ជំហានទី 1](#ជំហាន-1៖-បង្កើតគម្រោង-microsoft-foundry) ខាងក្រោម។

យើងបានបញ្ចូលឯកសារ `requirements.txt` នៅឬកណ្តាល repo នេះដែលមាន កញ្ចប់ Python រួមទាំងអស់ដែលត្រូវការដើម្បីរត់ឧទាហរណ៍កូដ។

អ្នកអាចដំឡើងវាដោយបញ្ជារបញ្ជាដូចខាងក្រោមក្នុង terminal នៅឬកណ្តាល repo៖

```bash|powershell
pip install -r requirements.txt
```

យើងផ្ដល់អនុសាសន៍បង្កើតបរិយាកាស Python virtual environment ដើម្បីជៀសវាងជំងឺផ្ទុះណាមួយនិងបញ្ហា។

## កំណត់ VSCode

ត្រូវប្រាកដថាអ្នកកំពុងប្រើកំណែ Python ត្រឹមត្រូវនៅក្នុង VSCode។

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## កំណត់ Microsoft Foundry និង Microsoft Foundry Agent Service

### ជំហាន 1៖ បង្កើតគម្រោង Microsoft Foundry

អ្នកត្រូវការប្រព័ន្ធ Microsoft Foundry **hub** និង **project** ដែលមានម៉ូដែលបានចុះបញ្ជីដើម្បីរត់ notebooks។

1. ចូលទៅ [ai.azure.com](https://ai.azure.com) ហើយចុះឈ្មោះជាមួយគណនី Azure របស់អ្នក។
2. បង្កើត **hub** (ឬប្រើវាដែលមានរួចមកហើយ)។ មើល៖ [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)។
3. ក្នុង hub បង្កើត **project**។
4. ចុះបញ្ជីម៉ូដែល (ឧ. `gpt-5-mini`) ពី **Models + Endpoints** → **Deploy model**។

### ជំហាន 2៖ យក Endpoint គំរូនិងឈ្មោះម៉ូដែលចុះបញ្ជីរបស់អ្នក

ពីគម្រោងរបស់អ្នកក្នុង Microsoft Foundry portal៖

- **Project Endpoint** — ចូលទៅទំព័រ **Overview** ហើយចម្លង URL endpoint។

![Project Connection String](../../../translated_images/km/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — ចូលទៅ **Models + Endpoints** រើសម៉ូដែលដែលបានចុះបញ្ជី ហើយចំណាំឈ្មោះ **Deployment name** (ឧ. `gpt-5-mini`)។

### ជំហាន 3៖ ចូលតាម Azure ជាមួយ `az login`

កំណត់ត្រាគ្រប់ទាំង notebooks ប្រើ **`AzureCliCredential`** សម្រាប់ការផ្ទៀងផ្ទាត់ — គ្មាន key API ត្រូវគ្រប់គ្រងទេ។ នេះទាមទារឲ្យអ្នកចូលតាម Azure CLI។

1. **ដំឡើង Azure CLI** ប្រសិនបើអ្នកមិនទាន់មានៈ [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **ចូល** ដោយបញ្ជារបញ្ជា:

    ```bash|powershell
    az login
    ```

    ប្រសិនអ្នកនៅក្នុងបរិយាកាស remote/Codespace ដែលគ្មាន browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **ជ្រើសរើស subscription** ប្រសិនបានស្នើ — ជ្រើសរើស subscription ដែលមានគម្រោង Foundry របស់អ្នក។

4. **ផ្ទៀងផ្ទាត់** ថាអ្នកបានចូល។

    ```bash|powershell
    az account show
    ```

> **ហេតុអ្វីគួរប្រើ `az login`?** notebooks ផ្ទៀងផ្ទាត់ដោយប្រើ `AzureCliCredential` ពី package `azure-identity`។ នេះមានន័យថា អង្គភាព Azure CLI របស់អ្នកផ្ដល់អត្តសញ្ញាណ — គ្មាន key API ឬសម្ងាត់នៅក្នុងឯកសារ `.env`។ នេះគឺជាលំនាំអនុវត្តល្អបំផុតក្នុងសន្តិសុខ។

### ជំហាន 4៖ បង្កើតឯកសារ `.env` របស់អ្នក

ចម្លងឯកសារឧទាហរណ៍:

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

| ប្លាក | កន្លែងរកឃើញ |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | កន្លែង Microsoft Foundry portal → គម្រោងរបស់អ្នក → ទំព័រ **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Microsoft Foundry portal → **Models + Endpoints** → ឈ្មោះម៉ូដែលដែលបានចុះបញ្ជី |

នេះគឺគ្រប់គ្រាន់សម្រាប់មេរៀនភាគច្រើន! notebooks នឹងផ្ទៀងផ្ទាត់ស្វ័យប្រវត្តិតាមរយៈសម័យ `az login` របស់អ្នក។

### ជំហាន 5៖ តំឡើង Python Dependencies

```bash|powershell
pip install -r requirements.txt
```

យើងផ្ដល់អនុសាសន៍ដំណើរការនេះនៅក្នុងបរិយាកាស virtual environment ដែលអ្នកបានបង្កើតមុននេះ។

## ការតំឡើងបន្ថែមសម្រាប់មេរៀនទី 5 (Agentic RAG)

មេរៀន 5 ប្រើ **Azure AI Search** សម្រាប់ការបង្កើតតាមការស្វែងរកបន្ថែម។ ប្រសិនបើអ្នកមានគម្រោងដំណើរការមេរៀននោះ សូមបន្ថែមប្លាកទាំងនេះទៅឯកសារ `.env` របស់អ្នក៖

| ប្លាក | កន្លែងរក |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | នាយកដ្ឋាន Azure → អ្នក resource **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | នាយកដ្ឋាន Azure → អ្នក resource **Azure AI Search** → **Settings** → **Keys** → កូនសោគ្រប់គ្រងសំខាន់ |

## ការតំឡើងបន្ថែមសម្រាប់មេរៀនដែលហៅ Azure OpenAI ដោយផ្ទាល់ (មេរៀនទី 6 និង 8)

គម្រោង notebooks ក្នុងមេរៀន 6 និង 8 ហៅ **Azure OpenAI** ដោយផ្ទាល់ (ប្រើ **Responses API**) ជំនួសមិនឲ្យឆ្លងកាត់គម្រោង Microsoft Foundry។ ឧទាហរណ៍នោះត្រូវបានប្រើក្រោយមក GitHub Models ដែលត្រូវបានលើកលែង (នឹងផុតកំណត់ត្រឡប់ខ្សែ ២០២៦ ខែកញ្ញា) ហើយមិនគាំទ្រ Responses API ទេ។ ប្រសិនបើអ្នកមានគម្រោងដំណើរការឧទាហរណ៍ទាំងនេះ សូមបន្ថែមប្លាកទាំងនេះទៅឯកសារ `.env` របស់អ្នក៖

| ប្លាក | កន្លែងរក |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | នាយកដ្ឋាន Azure → អ្នក resource **Azure OpenAI** → **Keys and Endpoint** → Endpoint (ឧ. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | ឈ្មោះម៉ូដែលដែលបានចុះបញ្ជី (ឧ. `gpt-5-mini`) ដែលគាំទ្រ Responses API |
| `AZURE_OPENAI_API_KEY` | ជាចំណង់ចំណូល — តែបើអ្នកប្រើការផ្ទៀងផ្ទាត់ដោយ key ជំនួស `az login` / Entra ID |

> Responses API ប្រើ stable endpoint `/openai/v1/` ដូច្នេះមិនចាំបាច់មាន `api-version` ទេ។ ចូលតាម `az login` ដើម្បីប្រើការផ្ទៀងផ្ទាត់ Entra ID ដោយគ្មាន key។

## អ្នកផ្គត់ផ្គង់ជំនួស៖ MiniMax (បង្កើតស្របទៅ OpenAI)

[MiniMax](https://platform.minimaxi.com/) ផ្ដល់ម៉ូដែល context ធំ (រហូតដល់ 204K tokens) តាមរយៈ API ដែលស្របទៅ OpenAI។ ពីព្រោះ Microsoft Agent Framework `OpenAIChatClient` អាចប្រើជាមួយ endpoint ស្របទៅ OpenAI មួយណាក៏បាន អ្នកអាចប្រើ MiniMax ជាជំនួសត្រង់ទៅ Azure OpenAI ឬ OpenAI។

បន្ថែមប្លាកទាំងនេះទៅក្នុងឯកសារ `.env` របស់អ្នក៖

| ប្លាក | កន្លែងរក |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | ប្រើ `https://api.minimax.io/v1` (តម្លៃលំនាំដើម) |
| `MINIMAX_MODEL_ID` | ឈ្មោះម៉ូដែលសម្រាប់ប្រើ (ឧ. `MiniMax-M3`) |

**ម៉ូដែលឧទាហរណ៍**៖ `MiniMax-M3` (ផ្តល់អនុសាសន៍), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (ឆ្លើយតបលឿនជាង)។ ឈ្មោះម៉ូដែល និងភាពរួមមានអាចផ្លាស់ប្ដូរតាមពេលវេលា ហើយការចូលដំណើរការម៉ូដែលមួយអាចអាស្រ័យលើគណនីឬតំបន់របស់អ្នក — សូមពិនិត្យ [MiniMax Platform](https://platform.minimaxi.com/) សម្រាប់បញ្ជីបច្ចុប្បន្ន។ បើ `MiniMax-M3` មិនអាចប្រើបាន សូមកំណត់ `MINIMAX_MODEL_ID` ទៅម៉ូដែលដែលអ្នកអាចចូលប្រើ (ឧ. `MiniMax-M2.7`)។

ឧទាហរណ៍កូដដែលប្រើ `OpenAIChatClient` (ឧ. មេរៀន 14 លំហាត់ការកក់សណ្ឋាគារ) នឹងស្វ័យប្រវត្តិកំណត់ហើយប្រើកំណត់រចនាសម្ព័ន្ធ MiniMax របស់អ្នកពេល `MINIMAX_API_KEY` ត្រូវបានកំណត់។

## អ្នកផ្គត់ផ្គង់ជំនួស៖ Foundry Local (ដំណើរការម៉ូដែលលើឧបករណ៍)

[Foundry Local](https://foundrylocal.ai) គឺជាកម្មវិធី runtime ទ្រទ្រង់ស្រាលដែលទាញយក គ្រប់គ្រង និងបម្រើម៉ូដែលភាសា **តែម្ដងនៅលើម៉ាស៊ីនរបស់អ្នកផ្ទាល់** តាមរយៈ API ស្របទៅ OpenAI — គ្មាន cloud, គ្មាន اشتراك Azure, ហើយគ្មាន key API។ វាជាជម្រើសល្អសម្រាប់ការអភិវឌ្ឍក្រៅបណ្តាញ សាកល្បងដោយគ្មានចំណាយ cloud, ឬរក្សាទិន្នន័យនៅលើឧបករណ៍។

ពីព្រោះ Microsoft Agent Framework `OpenAIChatClient` អាចប្រើជាមួយ endpoint ស្របទៅ OpenAI ណាមួយបាន Foundry Local គឺជាជំនួសក្នុងស្រុកមួយសម្រាប់ Azure OpenAI។

**1. ដំឡើង Foundry Local**

```bash
# វីនដូว์
winget install Microsoft.FoundryLocal

# ម៉ាក់អូអេស
brew install foundrylocal
```

**2. ទាញយក ហើយរត់ម៉ូដែល** (វានៅចាប់ផ្តើមសេវាកម្មក្នុងស្រុកផងដែរ)៖

```bash
foundry model list          # មើលម៉ូដែលដែលមានស្រាប់
foundry model run phi-4-mini
```

**3. ដំឡើង Python SDK** ដែលប្រើសម្រាប់រក endpoint ក្នុងស្រុក៖

```bash
pip install foundry-local-sdk
```

**4. ផ្ដោត Microsoft Agent Framework នឹងម៉ូដែលក្នុងស្រុករបស់អ្នក៖**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# ទាញយក (បើត្រូវការ) ហើយបម្រើម៉ូដែលក្នុងតំបន់រួចបន្ទាប់មកស្វែងរកចំណុចចេញ/គ្រឿងចុច។
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ឧទាហរណ៍ http://localhost:<port>/v1
    api_key=manager.api_key,        # ទៅតែ "មិនទាមទារ" សម្រាប់ Foundry Local ផង​ពេលណា
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **សម្គាល់:** Foundry Local បង្ហាញ endpoint OpenAI-compatible **Chat Completions**។ ប្រើវាសម្រាប់អភិវឌ្ឍន៍ក្នុងស្រុក និងករណីក្រៅបណ្តាញ។ សម្រាប់មុខងារ **Responses API** ពេញលេញ (ការសន្ទនាស្ថិតស្ថេរ, រៀបចំឧបករណ៍ជ្រៅ, និងអភិវឌ្ឍអ្នកតំណាង), សូមកំណត់ត្រូវទៅ **Azure OpenAI** ឬគម្រោង **Microsoft Foundry** ដូចបានបង្ហាញនៅក្នុងមេរៀន។ សូមមើល [ឯកសាររបស់ Foundry Local](https://foundrylocal.ai) សម្រាប់បញ្ជីម៉ូដែលបច្ចុប្បន្ន និងការគាំទ្រផ្ល랫폼។

## ការតំឡើងបន្ថែមសម្រាប់មេរៀន 8 (កម្មវិធី Bing Grounding)


សៀវភៅកំណត់ត្រាដំណើរការតាមលក្ខខណ្ឌនៅក្នុងមេរៀនទី 8 ប្រើ **Bing grounding** តាមរយៈ Microsoft Foundry។ ប្រសិនបើអ្នកមានគម្រោងធ្វើដំណើរការឧទាហរណ៍នោះ សូមបន្ថែមអថេរនេះទៅក្នុងឯកសារ `.env` របស់អ្នក៖

| អថេរ | បណ្តឹងរកទីតាំង |
|----------|-----------------|
| `BING_CONNECTION_ID` | វេទិកា Microsoft Foundry → គម្រោងរបស់អ្នក → **Management** → **Connected resources** → ការតភ្ជាប់ Bing របស់អ្នក → ចម្លង ID ការតភ្ជាប់ |

## ការដោះស្រាយបញ្ហា

### កំហុសផ្ទៀងផ្ទាត់លិខិតសញ្ញា SSL នៅលើ macOS

បើអ្នកប្រើ macOS ហើយជួបប្រទះកំហុសដូចជា៖

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

នេះជាបញ្ហាដែលបានគេដឹងជាមួយ Python នៅលើ macOS ដូចដែលលិខិតសញ្ញា SSL ប្រព័ន្ធមិនត្រូវបានទុកចិត្តដោយស្វ័យប្រវត្តិ។ សូមព្យាយាមដំណោះស្រាយខាងក្រោមតាមលំដាប់៖

**ជម្រើស 1៖ ដំណើរការស្ក្រីប Install Certificates របស់ Python (ផ្តល់អនុសាសន៍)**

```bash
# ជំនួស 3.XX ជាមួយនឹងកំណែ Python ដែលអ្នកបានដំឡើង (ឧ. 3.12 ឬ 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ជម្រើស 2៖ ប្រើ `connection_verify=False` នៅក្នុងសៀវភៅកំណត់ត្រារបស់អ្នក (សម្រាប់សៀវភៅកំណត់ត្រា GitHub Models ប៉ុណ្ណោះ)**

នៅក្នុងសៀវភៅកំណត់ត្រាមេរៀនទី 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), មានការធ្វើបច្ចុប្បន្នភាពដោយមិនបង្ហាញសម្ងាត់ហើយ។ សូមដោះសោ `connection_verify=False` ពេលបង្កើត client៖

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # បិទការត្រួតពិនិត្យ SSL ប្រសិនបើអ្នកប្រទះបញ្ហាការផ្ទៀងផ្ទាត់វិញ្ញាបនបត្រ
)
```

> **⚠️ សំគាល់៖** ការផ្អាកការផ្ទៀងផ្ទាត់ SSL (`connection_verify=False`) នាំឲ្យសុវត្ថិភាពកាន់តិចដោយផ្លាស់ប្ដូរដំណើរការផ្ទៀងផ្ទាត់លិខិតសញ្ញាដោយខ្លួនឯង។ សូមប្រើវាមិនលើសពីឱកាសបណ្ដោះអាសន្នក្នុងបរិយាកាសអភិវឌ្ឍន៍ទេ ហើយមិនត្រូវប្រើសម្រាប់ផលិតកម្មឡើយ។

**ជម្រើស 3៖ ตំឡើង និងប្រើ `truststore`**

```bash
pip install truststore
```

បន្ទាប់មកបន្ថែមអ្វីខាងក្រោមនៅលើបណ្តាសៀវភៅកំណត់ត្រារបស់អ្នក ឬ ស្ក្រីបជាមុនសិនមុនពេលធ្វើការហៅបណ្តាញណាមួយ៖

```python
import truststore
truststore.inject_into_ssl()
```

## ចាប់សោះនៅកន្លែងណាមួយ?

ប្រសិនបើអ្នកមានបញ្ហារបស់ការបង្ហោះការដំឡើងនេះ សូមចូលរួមនៅ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> ឬ <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">បង្កើតបញ្ហាតាមតំណ</a>។

## មេរៀនបន្ទាប់

ឥឡូវនេះអ្នករួចរាល់ក្នុងការប្រតិបត្តិកូដសម្រាប់វគ្គនេះ។ សូមសំណាងល្អក្នុងការស្វែងយល់បន្ថែមអំពីពិភពខ្លួន AI Agents!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->