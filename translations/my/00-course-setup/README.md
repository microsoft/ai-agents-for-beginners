# သင်တန်း စတင်ခြင်း

## နိဒါန်း

ဤသင်ခန်းစာတွင် သင်တန်း၏ ကုဒ်သင်ခန်းစာများကို မည်သို့ ဖွင့်၍ လုပ်ဆောင်ရမည်ကို ဖေါ်ပြပါမည်။

## အခြားသင်တန်းသားများနှင့် ပူးပေါင်းပြီး ကူညီမှုရယူခြင်း

သင်၏ repo ကို clone မလုပ်မီ [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) ကို ဝင်ရောက်ပါက စတင်ခြင်းအတွက် ကူညီမှုများ၊ သင်တန်းအကြောင်း မေးခွန်းများ သို့မဟုတ် အခြားသင်တန်းသားများနှင့် ဆက်သွယ်နိုင်ပါသည်။

## ဒီ Repo ကို Clone သို့မဟုတ် Fork စေခြင်း

စတင်ရန် GitHub Repository ကို clone သို့မဟုတ် fork ပြုလုပ်ပါ။ ဒါက သင်တန်းပစ္စည်းကို ကိုယ်ပိုင်ဗားရှင်း ရရှိစေပြီး ကုဒ်ကို လည်ပတ်၍ စမ်းသပ်ကာ ပြင်ဆင်နိုင်ပါသည်။

<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repo ကို fork ဆောင်ရွက်ရန်</a> တွင်ကလစ်နှိပ်၍ ပြုလုပ်နိုင်ပါသည်။

ယခု သင်၏ ကိုယ်ပိုင် forked version ကို အောက်ပါ link တွင် ရရှိထားမည်ဖြစ်သည်။

![Forked Repo](../../../translated_images/my/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (workshop / Codespaces အတွက် အကြံပြု)

 > အနက်အပြည့်ကို ဒေါင်းလုပ်လုပ်ယူပါက repository စုစုပေါင်းသည် (ခန့်မှန်း၍ 3 GB) ကြီးမားနိုင်ပါသည်။ သင်သည် workshop တစ်ခုတွင် ပါဝင်နေသည် သို့မဟုတ် သင်ခန်းစာအတန်းအနည်းငယ်ကိုသာ လိုအပ်ပါက shallow clone (သို့) sparse clone ဖြင့် ကွန်ပြူတာတွင် လိုအပ်သည့် ပမာဏသာ ဒေါင်းလုပ်လုပ်ပါသည်။

#### အလျင်အမြန် shallow clone — သမိုင်းနောက်ခံအနည်းဆုံး၊ ဖိုင်အားလုံးပါဝင်သည်

အောက်ပါ commands တွင် `<your-username>` ကို သင့် fork URL နှင့် (သို့) upstream URL နှင့် အစားထိုးပါ။

နောက်ဆုံး commit သမိုင်းကိုသာ clone ဆောင်ရွက်ရန် (ဒေါင်းလုပ်အရွယ်အစားသိမ်မွေ့):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

အထူး branch တစ်ခုကို clone ဆောင်ရွက်ရန်:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### အစိတ်အပိုင်း (sparse) clone — blobs နည်းပါးပြီး folder များရွေးချယ်သည်သာ

ဤသည်မှာ partial clone နှင့် sparse-checkout ကို အသုံးပြုသည် (Git 2.25+ လိုအပ်ပြီး partial clone ကို ထောက်ခံသော modern Git အတွက် အကြံပြုသည်)။

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

repo folder ထဲ သို့ ဝင်ရောက်ပါ။

```bash
cd ai-agents-for-beginners
```

ပြီးနောက် သင်လိုချင်သော folders များကို ဖော်ပြပါ (နမူနာအနေဖြင့် ဖိုလ်ဒါနှစ်ခုပြထားသည်)။

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

cloning ပြုလုပ်ပြီး ဖိုင်များ စစ်ဆေးပြီးပါက ဖိုင်ပင်ပန်း မလိုအပ်၍ နေရာလွတ်ချင်ပါက (git history မလိုအပ်သော) repository metadata ကို ဖျက်ပစ်ပါ (💀 ပြန်လည်ဆပ်မရ — Git လုပ်ဆောင်ချက်အားလုံးဆုံးရှုံးမည်)။

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces အသုံးပြုခြင်း (ဒေါင်းလုပ်ကြီးများကိုမလိုအပ်ရန် အကြံပြု)

- [GitHub UI](https://github.com/codespaces) မှတဆင့် ဤ repo အတွက် သစ်မည့် Codespace အသစ်တစ်ခု ဖန်တီးပါ။

- အသစ်ဖန်တီးသော codespace ၏ terminal တွင် အထက်ပါ shallow/sparse clone command များကို ဆောင်ရွက်ကာ သင်လိုအပ်သည့် lesson folders များကို Codespace workspace ထဲ သာ ရယူပါ။
- ရွေးချယ်စရာ - Codespaces မှာ cloning ပြီးနောက်၊ .git ဖိုင် ကိုဖယ်ရှားကာ နေရာ ပြန်လွတ်နိုင်ပါသည် (အထက်ဖော်ပြသော ဖယ်ရှားခြင်း မှတ်ချက်များကို ကြည့်ပါ)။
- သတိပြုရန် - Repo ကို Codespaces တွင် တိုက်ရိုက်ဖွင့်လိုပါက (clone အပို လုပ်ရန်မလိုသော နေရာ) Codespaces သည် devcontainer ပတ်ဝန်းကျင်ကို တည်ဆောက်ပြီး သင့်လိုအပ်ချက်ထက် ပိုမို provision လုပ်နိုင်သည်။

#### အကြံပြုချက်များ

- သင့်အတွက် ပြင်ဆင်/commit လုပ်လိုပါက clone URL ကို သင့်ကိုယ်ပိုင် fork သို့ အမြဲပြောင်းပါ။
- နောက်ပိုင်းတွင် သမိုင်းနောက်ခံများ သို့မဟုတ် ဖိုင်များပိုလိုအပ်ပါက fetch လုပ်ပါ သို့မဟုတ် sparse-checkout ဖြင့် folder များ ထပ်ထည့်ပါ။

## ကုဒ် လည်ပတ်ခြင်း

ဤသင်တန်းတွင် သင်လက်တွေ့လုပ်ကိုင်ကြည့်ရန် Jupyter Notebooks များကို ပေးထားသည်။

ကုဒ်နမူနာများသည် **Microsoft Agent Framework (MAF)** ကို အသုံးပြုပြီး `FoundryChatClient` အသုံးပြုသည်၊ သည်သည် **Microsoft Foundry Agent Service V2** (Responses API) နှင့် **Microsoft Foundry** မှ ဆက်သွယ်သည်။

Python notebooks အားလုံးကို `*-python-agent-framework.ipynb` ဟုပဲ အမည်တပ်ထားသည်။

## လိုအပ်ချက်များ

- Python 3.12+
  - **မှတ်ချက်**: Python3.12 မရှိပါက ထည့်သွင်းကြပါ။ ထို့နောက် venv ကို python3.12 ဖြင့် ဖန်တီးကာ requirements.txt မှ လိုအပ်သော ဗားရှင်းများ ထည့်သွင်းပါ။
  
    >ဥပမာ

    Python venv directory ဖန်တီးခြင်း။

    ```bash
    python -m venv venv
    ```

    ထို့နောက် venv environment ကို အောက်ပါအတိုင်း ဖွင့်ပါ။

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET ကို အသုံးပြုသော ကုဒ်များအတွက် [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) သို့မဟုတ် ေနာက္ပိုင်းဗားရှင်း ထည့်သွင်းထားရန်။ ထို့နောက် သင့်ထည့်သွင်းထားသော .NET SDK ဗားရှင်းကို ဆန်းစစ်ပါ။

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — အတည်ပြုခြင်းအတွက် မရှိမဖြစ်လိုအပ်သည်။ [aka.ms/installazurecli](https://aka.ms/installazurecli) မှတဆင့် ထည့်သွင်းပါ။
- **Azure Subscription** — Microsoft Foundry နှင့် Microsoft Foundry Agent Service သို့ ဝင်ရောက်ခွင့်။
- **Microsoft Foundry Project** — deployed model တစ်ခုဖြင့် project (ဥပမာ `gpt-5-mini`)။ အောက်တွင် [Step 1](#အဆင့်-1-microsoft-foundry-project-ဖန်တီးခြင်း) ပြုလုပ်ရန်။

repository ရဲ့ root မှာ `requirements.txt` ဖိုင်တစ်ခု ပါရှိပြီး ကုဒ်နမူနာများ ထည့်သွင်းရန် လိုအပ်သော Python package အားလုံး ပါဝင်သည်။

repo root ကို terminal တွင် သွားပြီး အောက်ပါ command ဖြင့် ထည့်သွင်းနိုင်ပါသည်။

```bash
pip install -r requirements.txt
```

အမြဲ Python virtual environment တစ်ခုဖန်တီး၍ conflicts မဖြစ်အောင် ကြံ့ကြံ့ခံပြီး အသုံးပြုရန် အကြံပြုပါသည်။

## VSCode ကို ပြင်ဆင်ခြင်း

VSCode တွင် သင့်အသုံးပြုသော Python ဗားရှင်း သေချာစွာ ငြိမ်းချမ်းစွာအသုံးပြုနေမည်စစ်ဆေးပါ။

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry နှင့် Microsoft Foundry Agent Service ကို ပြင်ဆင်ခြင်း

### အဆင့် 1: Microsoft Foundry Project ဖန်တီးခြင်း

notebooks များမှာ လည်ပတ်ရန် deployed model ပါရှိသည့် Microsoft Foundry **hub** နှင့် **project** တို့ လိုအပ်ပါသည်။

1. [ai.azure.com](https://ai.azure.com) သို့ သွား၍ Azure အကောင့်ဖြင့် ဝင်ရောက်ပါ။
2. **hub** တစ်ခု ဖန်တီးပါ (သို့) ရှိပြီးသားကို အသုံးပြုပါ။ ကြည့်ရန်: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)။
3. hub အတွင်းတွင် **project** တစ်ခု ဖန်တီးပါ။
4. **Models + Endpoints** → **Deploy model** မှ မော်ဒယ်တစ်ခု (ဥပမာ `gpt-5-mini`) ကို deploy ပါ။

### အဆင့် 2: Project Endpoint နှင့် Model Deployment Name ရယူခြင်း

Microsoft Foundry portal မှ သင့် project ထဲမှ:

- **Project Endpoint** — **Overview** စာမျက်နှာသို့ သွားရောက်ပြီး endpoint URL ကို ကူးယူပါ။

![Project Connection String](../../../translated_images/my/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** သို့သွား၍ deployed model ကို ရွေးချယ်ပြီး၊ **Deployment name** ကို မှတ်ထားပါ (ဥပမာ `gpt-5-mini`)။

### အဆင့် 3: Azure သို့ `az login` ဖြင့် အကောင့်ဝင်ခြင်း

notebooks များသည် သင့်ရဲ့ **Azure CLI sign-in** ဖြင့် သော့ချက်မလိုဘဲ `AzureCliCredential` သို့မဟုတ် `DefaultAzureCredential` (စကားဝှက်မပါသော signin session ကို သုံးသည်) ဖြင့် authentication လုပ်သည်။ တချို့ သင်ခန်းစာနှင့် လိုအပ်ချက်ကွဲပြားမှုများသည် API keys သုံးမှုရှိနိုင်သည်။ အဆိုပါသင့်ကို Azure CLI ဖြင့် အသုံးပြု sign in ပြုလုပ်ထားရန် လိုအပ်သည်။

1. **Azure CLI ကို ထည့်သွင်းခြင်း** (မရှိသေးလျှင်): [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Signin** အတွက် အောက်ပါ command ကို လည်ပတ်ပါ။

    ```bash
    az login
    ```

    မိုဘိုင်း / remote/Codespace ပတ်ဝန်းကျင်မှ browser မပါရှိပါက:

    ```bash
    az login --use-device-code
    ```

3. **Subscription ရွေးချယ်မှု** လိုအပ်ပါက သင့် Foundry project ပါသော subscription ကို ရွေးပါ။

4. **Signin ဖြစ်ပါက အတည်ပြုခြင်း**။

    ```bash
    az account show
    ```

> **`az login` အကြောင်း** notebooks များသည် `azure-identity` package မှ `AzureCliCredential` (သို့) `DefaultAzureCredential` ကို အသုံးပြု၍ API သော့ချက်မလိုဘဲ Azure CLI session မှ credentials ပေးသည်။  `.env` ဖိုင်တွင် သော့ချက်မပါ။ ဒါသည် [လုံခြုံရေးအကောင်းဆုံးလုပ်နည်း](https://learn.microsoft.com/azure/developer/ai/keyless-connections) ဖြစ်သည်။

### အဆင့် 4: `.env` ဖိုင် ဖန်တီးခြင်း

ဥပမာဖိုင်ကို ကူးယူပါ။

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

`.env` ဖိုင်ကို ဖွင့်ပြီး အောက်ပါ မှန်ကန်သည့် တန်ဖိုး ၂ ခု သွင်း ထားပါ။

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variable | ဘယ်မှာတွေ့ရမလဲ |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → သင့် project → **Overview** စာမျက်နှာ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → သင့် deployed model အမည် |

များသော သင်ခန်းစာများနှင့် notebooks များ အတွက် ရပ်တန့်ပါသည်။ notebooks များမှာ `az login` session ကနေ အလိုအလျောက် အတည်ပြုမှု ပြုလုပ်ပါသည်။

### အဆင့် 5: Python လိုအပ်ချက်များ ထည့်သွင်းခြင်း

```bash
pip install -r requirements.txt
```

သင့်ဖန်တီးထားသော virtual environment အတွင်းတွင် လည်ပတ်ရန် အကြံပြုသည်။

## ရွေးချယ်စရာ: Azure AI Search (သင်ခန်းစာ 5 နှင့် 16)

သင်ခန်းစာ 5 (Agentic RAG) နှင့် 16 notebooks များသည် **in-memory knowledge base** ဖြင့် အလိုအလျောက် ရိုက်သွင်းသည်။ သင်သည် အမှန်တကယ် **Azure AI Search** index အသုံးပြုရန် လိုပါက သတိပြုပါ။ **Lesson 16 notebook သည် key-based authentication အသုံးပြုခြင်း** ဖြစ်သည်။ `AZURE_SEARCH_SERVICE_ENDPOINT` နှင့် `AZURE_SEARCH_API_KEY` နှစ်ခုလုံး မပါသော်လည်း in-memory search ကို သုံးသည်။ ထို့ကြောင့် သင့်မှာ admin key ကိုလည်း သတ်မှတ်ရမည်ဖြစ်သည်။ Keyless authentication က Microsoft Entra ID (RBAC) ဖြစ်ပြီး သင်၏ ကိုယ်ပိုင် ထုတ်လုပ်မှုကုဒ်အတွက် အကြံပြုသောနည်းလမ်းဖြစ်သည်။ ဒါက ဒီသင်တန်းတွင် သုံးတဲ့ `az login` စနစ်နှင့်ကိုက်ညီပါသည်။

RBAC အဆင့်များမှာ အောက်ပါ setup-guide နမူနာများ နှင့် ကိုယ်ပိုင်ကုဒ်များတွင် အသုံးပြုနိုင်သည်။ တွဲချိတ်ထားခြင်း မရှိပါ။ Lesson 16 notebook သည် Azure AI Search ကို အသုံးပြုရန် endpoint နှင့် admin key နှစ်ခုလုံး လိုအပ်သည်။

1. သင်၏ search service တွင် **role-based access** ကို ဖွင့်ပါ

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. လိုအပ်သော roles များကို သင်ကိုယ်တိုင် ထည့်သွင်းပါ (index များ ဖန်တီး/တင်သည်နှင့် query လုပ်သည်။

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. သင့် `.env` ဖိုင်တွင် endpoint ကို ထည့်ပါ။

| Variable | ဘယ်မှာတွေ့ရမလဲ |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → သင့် **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Lesson 16 notebook သည် key-based auth ကို အသုံးပြု၍ Azure portal → **Settings** → **Keys** → primary admin key | 

> **ဘာကြောင့် keyless?** Admin keys သည် search service ကို အပြီးအမှတ်ရေးမှု များ ဖွင့်ပေးပြီး `.env` ဖိုင်များမှ ဖြန့်လွှင့်နိုင်ပါသည်။ RBAC ဖြင့် `az login` အကောင့်ကို အသုံးပြုပြီး key မလိုအပ်ပါ။ သင်ခန်းစာ notebooks တွင် အသုံးပြုသော keyless Entra ID ပုံစံဖြစ်သည် (`AzureCliCredential` / `DefaultAzureCredential`)။ [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) ကို ကြည့်ပါ။

Python နှင့် .NET မှာ အပြည့်အစုံ index ဖန်တီးနမူနာများအတွက် [Azure AI Search setup guide](./AzureSearch.md) ကို ကြည့်ပါ။

## Azure OpenAI ကို တိုက်ရိုက် ဖုန်းခေါ်သော သင်ခန်းစာများအတွက် အထူးပြုဖြည့်သွင်းချက် (သင်ခန်းစာ 6 နှင့် 8)

သင်ခန်းစာ 6 နှင့် 8 အချို့သော notebooks များသည် Microsoft Foundry project မှတစ်ဆင့် မသွားပဲ **Azure OpenAI** ကို တိုက်ရိုက် **Responses API** အသုံးပြု၍ ဖုန်းခေါ်သည်။ GitHub Models ကို ယခင်တွင်အသုံးပြုခဲ့သည်ကတော့ Response API ကို ထောက်ခံမထားပေ။ အောက်ဖော်ပြထားသော variable များကို `.env` ဖိုင်တွင် ထည့်သွင်းပါ။

| Variable | ဘယ်မှာတွေ့ရမလဲ |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → သင့် **Azure OpenAI** resource → **Keys and Endpoint** → Endpoint (ဥပမာ `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Responses API ကို ထောက်ခံသော သင့် deployed model အမည် (ဥပမာ `gpt-5-mini`) |
| `AZURE_OPENAI_API_KEY` | ရွေးချယ်စရာ — 'az login' / Entra ID အစား key-based auth သုံးလိုပါကသာ |

> Responses API သည် stable `/openai/v1/` endpoint ကို အသုံးပြုသည်၊ `api-version` မလိုအပ်ပါ။ keyless Entra ID auth အတွက် `az login` ဖြင့် signin ပြုလုပ်ပါ။

## အခြား provider: MiniMax (OpenAI-compatible)

[MiniMax](https://platform.minimaxi.com/) သည် OpenAI-compatible API ဖြင့် 204K token အထိ စိတ်ဓာတ်ကြီးမားသော model များ ပေးအပ်သည်။ Microsoft Agent Framework ၏ `OpenAIChatClient` က OpenAI-compatible endpoint များအားလုံးနှင့် အလုပ်လုပ်နိုင်ပြီး MiniMax ကို `OpenAIChatClient` အသုံးပြုသည့် သင်ခန်းစာများအတွက် လွယ်ကူစွာ အစားထိုးအသုံးပြုနိုင်ပါသည်။

variable များကို `.env` ဖိုင်တွင်ထည့်ပါ။

| Variable | ဘယ်မှာတွေ့ရမလဲ |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` (အပျမ်းမျှတန်ဖိုး) အသုံးပြုပါ |
| `MINIMAX_MODEL_ID` | အသုံးပြုမည့် model အမည် (ဥပမာ `MiniMax-M3`) |

**နမူနာ model များ**: `MiniMax-M3` (အကြံပြု), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (အမြန်၍ တုံ့ပြန်မှုမြန်)။ Model အမည်များနှင့် ရရှိနိုင်မှုက အချိန်နှင့်အညီ ပြောင်းလဲနိုင်ပြီး သင့်အကောင့်ပေါ်မှပေါ်မူတည်သည်။

`OpenAIChatClient` ကို အသုံးပြုသော ကုဒ်နမူနာများ (ဥပမာ သင်ခန်းစာ 14 ဟိုတယ်မှာတင်ခြင်း workflow) သည် `MINIMAX_API_KEY` သတ်မှတ်ထားသောအခါ သင့် MiniMax ဖော်ပြချက်အား အလိုအလျောက် တွေ့ရှိသုံးစွဲပါမည်။


## အခြားဆောင်ရွက်သူ: Foundry Local (မော်ဒယ်တွေကို စက်ပေါ်မှာ လည်ပတ်စေခြင်း)

[Foundry Local](https://foundrylocal.ai) သည် သင့်ရဲ့စက်ပေါ်မှာပင် OpenAI-ကိုက်ညီသော API များမှတဆင့် ဘာသာစကားမော်ဒယ်များကို ဒေါင်းလုပ်ဆွဲ၊ စီမံခန့်ခွဲ၊ နှင့် စနစ်တကျ ဖြန့်ဝေရန်အတွက် အလေးပြုထားသော runtime တစ်ခုဖြစ်သည် — မိုးကောင်းကင်မလိုအပ်ပါ။

Microsoft Agent Framework ရဲ့ `OpenAIChatClient` သည် OpenAI-ကိုက်ညီသော endpoint များနှင့် မည်သည့်အချိန်မဆို လုပ်ဆောင်နိုင်သဖြင့် Foundry Local သည် Azure OpenAI အတွက် တိုက်ရိုက်အစားထိုး local ဖြေရှင်းချက်တစ်ခုဖြစ်သည်။

**၁။ Foundry Local ကို 설치 လုပ်ပါ**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**၂။ မော်ဒယ်တစ်ခုကို ဒေါင်းလုပ်ဆွဲပြီး မောင်းနှင်ပါ** (ဤအဆင့်တွင် local service ကိုလည်း စတင်လည်ပတ်စေသည်)။

```bash
foundry model list          # အသုံးပြုနိုင်သော မော်ဒယ်များကို ကြည့်ပါ
foundry model run phi-4-mini
```

**၃။ local endpoint ကို ရှာဖွေရန် အသုံးပြုမည့် Python SDK ကို 설치 လုပ်ပါ**

```bash
pip install foundry-local-sdk
```

**၄။ Microsoft Agent Framework ကို သင့် local မော်ဒယ်သို့ ချိတ်ဆက်ပါ:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# မော်ဒယ်ကို (လိုအပ်လျှင်) ဒေါင်းလုတ်လုပ်ပြီး ဒေသတွင်သုံးရန် ပေးဆောင်ပြီး ထို့နောက် endpoint/port ကို ရှာဖွေသည်။
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ဥပမာ http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local အတွက် အမြဲတမ်း "လိုအပ်မထားပါ" ဖြစ်သည်။
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **မှတ်ချက်။** Foundry Local သည် OpenAI-ကိုက်ညီသော **Chat Completions** endpoint ကို ဖော်ပြထားသည်။ ဒါကို local ဖွံ့ဖြိုးရေးနှင့် offline ဖြစ်ပြီးသော အခြေအနေများအတွက် အသုံးပြုပါ။ **Responses API** အပြည့်အစုံသော လုပ်ဆောင်ချက်များ (stateful conversations စသည်) အတွက် Azure OpenAI သို့မဟုတ် Microsoft Foundry project ကို အသုံးပြုပါ။

## ကိစ္စ ၈ အတွက် အပိုပြင်ဆင်မှု (Bing Grounding Workflow)

ကိစ္စ ၈ တွင် conditional workflow notebook သည် Microsoft Foundry မှ Bing grounding ကို အသုံးပြုသည်။ ထိုစမ်းသပ်မှုကို မောင်းနှင်ရန် ရည်ရွယ်ပါက `.env` ဖိုင်၌ ဤ variable ကို ထည့်သွင်းပါ-

| Variable | ရရှိနိုင်သောနေရာ |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → သင့် project → **Management** → **Connected resources** → သင့် Bing ချိတ်ဆက်မှု → connection ID ကို ကူးယူပါ |

## ပြဿနာဖြေရှင်းခြင်း

### macOS တွင် SSL လက်မှတ်စစ်ဆေးမှုပြဿနာများ

macOS တွင် အောက်ပါအတုအယောင်ဖြစ်မှုပုံစံ တစ်ခုကြုံတွေ့ပါက-

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

ဤသည်မှာ macOS ပေါ်ရှိ Python တွင် စနစ် SSL လက်မှတ်များကို အလိုအလြောအယား ယုံကြည်မထားသော ပြဿနာတစ်ခုဖြစ်သည်။ အောက်ပါ ကူညီမှုများကို စီစဉ်အသုံးပြုကြည့်ပါ-

**ရွေးချယ်မှု ၁။ Python Install Certificates script ကို run ရန် (အကြံပြုချက်)**

```bash
# သင်တပ်ဆင်ထားသော Python ဗားရှင်း (ဥပမာ 3.12 သို့မဟုတ် 3.13) ဖြင့် 3.XX ကို အစားထိုးပါ။
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ရွေးချယ်မှု ၂။ notebook များတွင် `connection_verify=False` ကို အသုံးပြု (GitHub Models notebooks သာ)**

Lesson 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) တွင် အဆိုပါ workaround ကို မှတ်ချက်ထဲကနေ ဖယ်ရှားထားပြီးဖြစ်သည်။ လက်မှတ်အမှားဖြစ်ပါက `connection_verify=False` ကို ဖွင့်လိုက်ပါ-

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # လက်မှတ်ဆိုင်ရာ အမှားများ ကြုံတွေ့ပါက SSL စစ်ဆေးမှုကို ပိတ်မည်
)
```

> **⚠️ သတိပေးချက်။** SSL စစ်ဆေးမှု ဖျက်ပစ်ခြင်း (`connection_verify=False`) သည် လက်မှတ်အတည်ပြုခြင်းကို ရှောင်ကြဉ်လျှော့ချပေးသဖြင့် လုံခြုံမှုကို လျော့နည်းစေနိုင်သည်။ ထိုကာလအတွင်း ဖွံ့ဖြိုးရေး (development environment) အတွက်သာ ယင်းကို စမ်းသပ်အသုံးပြုပါ။ ထုတ်လုပ်မှု (production) တွင် မသုံးရ။

**ရွေးချယ်မှု ၃။ `truststore` ကို 설치 လုပ်ပြီး အသုံးပြုပါ**

```bash
pip install truststore
```

နောက်တစ်ဆင့်မှာ သင့် notebook သို့ script ၏ အပေါ်ဆုံးတွင် ကွန်ယက်ခေါ်ဆိုမှု မပြုမီ အောက်ဖော်ပြပါကို ထည့်ပါ-

```python
import truststore
truststore.inject_into_ssl()
```

## နေရာတစ်ခုမှာ ပိတ်မိသလား?

ဤလုပ်ထုံးလုပ်နည်းတွင် ပြဿနာရှိပါက <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> သို့ မိတ်ဆက် ပေးနိုင်သော်လည်း <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">issue တင်နိုင်ပါသည်</a>။

## နောက်တစ်ခန်း

သင်သည် ယခုဤသင်ခန်းစာအတွက် ကုဒ်များကို မောင်းနှင်ရန် အဆင်သင့်ဖြစ်ပါပြီ။ AI Agents ၏ ကမ္ဘာအကြောင်း ပိုမိုသင်ယူ ဖို့ပျော်ရွှင်ပါစေ!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->