# သင်တန်း စတင်ပြင်ဆင်ခြင်း

## နိဒါန်း

ဒီသင်ခန်းစာမှာ ဒီသင်တန်းရဲ့ ကုဒ်နမူနာတွေကို ဘယ်လို run မယ်ဆိုတာ ဖော်ပြပါမယ်။

## အခြားသင်ယူသူတွေနဲ့ ပူးပေါင်းကူညီမှုရယူခြင်း

သင့် GitHub repo ကို clone မလုပ်မီ၊ [AI Agents For Beginners Discord ချန်နယ်](https://aka.ms/ai-agents/discord) မှာ ဝင်ရောက်ပြီး စတင်ပြင်ဆင်မှုနဲ့ ပတ်သက်တဲ့ ကူညီမှုများ၊ သင်တန်းဆိုင်ရာ မေးခွန်းများ မေးမြန်းနိုင်ရန်၊ နှင့် အခြားသင်ယူသူများနှင့် ဆက်သွယ်နိုင်ရန် လိုအပ်ပါသည်။

## Repo ကို Clone သို့ Fork ပြုလုပ်ပါ

စတင်ရန်အတွက် GitHub Repository ကို clone သို့မဟုတ် fork ပြုလုပ်ပါ။ ဒါကြောင့် သင်တန်းထဲပါ ကုဒ် နမူနာများကို ကိုယ်တိုင်လည်ပတ်၊ စမ်းသပ် နှင့် ပြင်ဆင်နိုင်မှာဖြစ်ပါတယ်။

ဒီကိုလည်း <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repo ကို fork ပြုလုပ်ရန်</a>ကလစ်ခြယ်ချနိုင်ပါတယ်။

သင်ယခုသင်တန်းရဲ့ ကိုယ်ပိုင် forked ဗားရှင်းကို အောက်ပါလင့်에게 ရရှိထားပြီဖြစ်သည်။

![Forked Repo](../../../translated_images/my/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (workshop / Codespaces အတွက် အကြံပြု)

  > အပြည့်အစုံ repo မှာ ဖိုင်တွေကောင်း အင်္ဂါရပ်တွေကြီးကြီး (~3 GB) ရှိနိုင်ပါတယ်။ workshop သို့တက်ရောက်မယ်ဆို၊ သို့မဟုတ် သင်ခန်းစာ ဖိုလ်ဒါသေးသေးသာ လိုအပ်မယ်ဆို shallow clone (သို့မဟုတ် sparse clone) သာကြောင့် အနည်းငယ်သာ download လုပ်ရမှာ ဖြစ်ပါတယ်။

#### ယူဆောင်မယ့် shallow clone — သမိုင်းကြောင်းနည်း၊ ဖိုင်အားလုံးပါ

အောက်ကမီရှင်းတွေမှာ `<your-username>` ကို သင့်ရဲ့ fork URL (သို့မဟုတ် upstream URL ကို သင်ကြိုက်နှစ်သက်တယ်ဆို) ဖြင့် အစားထိုးပါ။

နောက်ဆုံး commit history ကိုသာ clone လုပ်ချင်တယ်ဆိုလျှင် (ဒေါင်းလုဒ် သေးငယ်သည်):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

အထူး branch တစ်ခု clone လုပ်ချင်ရင်:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### နည်းလမ်းအချို့ (partial sparse) clone — နည်းနည်းသော blob များနှင့် ရွေးချယ်ထားတဲ့ဖိုလ်ဒါတွေကိုသာ clone

ဒါက partial clone နဲ့ sparse-checkout ကိုသုံးသောနည်းဖြင့် (Git 2.25+ လိုအပ်ပြီး partial clone ကိုထောက်ပံ့တဲ့ကြီးမားသော Git version များ အကြံပြုသည်။)

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Repo folder ထဲကို ဝင်ပါ။

```bash
cd ai-agents-for-beginners
```

ထို့နောက် သင်လိုချင်သောဖိုလ်ဒါတွေကို သတ်မှတ်ပါ ( အောက်ပါဥပမာတွင် ဖိုလ်ဒါနှစ်ခုပါဝင်သည်)။

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Clone ပြီးလျှင် ဖိုင်တွေ အတည်ပြုပြီး နေရာလွတ်ချင်လျှင် (Git သမိုင်း မလိုလျှင်) ဤ Repo metadata ကို ဖျက်ပစ်ပါ (💀မပြန်ဖွင့်နိုင်။ Git ဂဲ့ာကုပ်ဘ်အလုပ်ပိတ်မိပါလိမ့်မယ်)။

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces သုံးခြင်း (ဒေါင်းလုဒ် ကြီးမားမှုကို ရှောင်တခင် အကြံပြု)

- ဒီ repo အတွက် [GitHub UI](https://github.com/codespaces) မှာ Codespace အသစ် တစ်ခု ဖန်တီးပါ။

- ဒါဆိုပြီး Codespace ရဲ့ terminal မှာ အထက်ပါ shallow / sparse clone commands တစ်ခုခု run ပြီး သင့်လိုချင်တဲ့ သင်ခန်းစာ ဖိုလ်ဒါတွေကို Codespace workspace ထဲ ဆွဲနိုင်ပါသည်။
- ရွေးချယ်စရာ: Codespaces အတွင်း cloned လုပ်ပြီးနောက် `.git` ဖိုင်ကို ဖျက်ပစ်၍ နေရာလွတ်နိုင်သည် (အပေါ်က ဖျက်ပစ်မှု ကုတ်ကြောင်းကို ကြည့်ပါ)။
- သတိပြုရန်၊ repo ကို Codespaces တွင် တိုက်ရိုက်ဖွင့်ချင်တယ်ဆို၊ ဒါဟာ Codespaces အတွက် devcontainer ပတ်ဝန်းကျင်တွေကို ဖန်တီးသွားမှာဖြစ်ပြီး သင်လိုချင်သတာထက် ပိုမို provision လုပ်ပေးနိုင်သည်။

#### အကြံပြုချက်များ

- ဟိုကလုံ URL ကို အမြဲသင့် fork URL ဖြင့် အစားထိုးပါ (ပြင်ဆိုင်ရန်/ commit တင်ရန်လိုလျှင်)။
- နောက်ပြီးတွင် သမိုင်းကြောင်း (history) ပိုမိုလိုအပ်လာပါက ဖိုလ်ဒါများကို sparse-checkout ဖြင့် ထပ်မံ ထည့်သွင်း fetch လုပ်နိုင်ပါသည်။

## ကုဒ် run ပြုလုပ်ခြင်း

ဒီသင်တန်းမှာ AI Agents တည်ဆောက်ရာ Jupyter Notebooks စီးရီးများကို တိုက်ရိုက် အတွေ့အကြုံရရှိရန် run လုပ်နိုင်ပါသည်။

ကုဒ်နမူနာများမှာ **Microsoft Agent Framework (MAF)** ကို `FoundryChatClient` နဲ့ အသုံးပြုပြီး **Microsoft Foundry Agent Service V2** (Responses API) ကို **Microsoft Foundry** မှ တဆင့် ဆက်သွယ်သည်။

Python notebook အားလုံးကို `*-python-agent-framework.ipynb` လို label ထားသည်။

## လိုအပ်ချက်များ

- Python 3.12+ အကြောင်း
  - **သတိပေးချက်**: သင် Python 3.12 မရှိသေးလျှင် install ပြုလုပ်ပါ။ ပြီးနောက် python3.12 ဖြင့် venv ကိုဖန်တီးကာ requirements.txt မှ အမှန်တကယ်လိုအပ်သော version များကို စစ်ဆေးထည့်သွင်းပါ။
  
    >ဥပမာ

    Python venv directory ဖန်တီးခြင်း

    ```bash
    python -m venv venv
    ```

    ထိုပြီးနောက် venv environment ကို ဖွင့်ပါ

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET ဖြင့် စမ်းသပ်ကုဒ်များအတွက် [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) သို့မဟုတ် နောက်ထပ်version ကို install လုပ်ပါ။ ထိုပြီးနောက် .NET SDK version ကို စစ်ဆေးပါ။

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — အတည်ပြုရန်လိုအပ်သည်။ [aka.ms/installazurecli](https://aka.ms/installazurecli) မှ install လုပ်ပါ။
- **Azure Subscription** — Microsoft Foundry နှင့် Microsoft Foundry Agent Service သုံးရန်။
- **Microsoft Foundry Project** — မော်ဒယ်တစ်ခု deploy ပြီးသော project ဖြစ်သည် (ဥပမာ `gpt-5-mini`) ။ [အဆင့် ၁](#အဆင့်-၁-microsoft-foundry-project-ဖန်တီးခြင်း) ကိုကြည့်ပါ။

ဒီ repo ရဲ့ root folder ထဲမှာ `requirements.txt` ဖိုင်ပါရှိပြီး ကုဒ်နမူနာတွေ run ဖို့လိုအပ်တဲ့ Python package အားလုံး ပါဝင်သည်။

ရှိနေသော terminal မှာ အောက်ဖော်ပြထားသော command ကို run လုပ်ကာ ထည့်သွင်းနိုင်ပါသည်။

```bash
pip install -r requirements.txt
```

conflict မဖြစ်အောင် Python virtual environment တစ်ခု ဖန်တီးရန် အကြံပြုပါသည်။

## VSCode Setup ပြုလုပ်ခြင်း

VSCode မှာမှန်ကန်တဲ့ Python version ကို သုံးနေခြင်းကို သေချာစေပါ။

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry နဲ့ Microsoft Foundry Agent Service ကို စတင်ပြင်ဆင်ခြင်း

### အဆင့် ၁: Microsoft Foundry Project ဖန်တီးခြင်း

Microsoft Foundry **hub** နဲ့ **project** တစ်ခုလို့မူ အချိန်မတိုင်ခင် မော်ဒယ်တစ်ခု deploy လုပ်ထားဖို့လိုအပ်သည်။

1. [ai.azure.com](https://ai.azure.com) သို့ဝင်၍ Azure အကောင့်ဖြင့် login ဝင်ပါ။
2. **hub** အသစ် တစ်ခုဖန်တီးပါ (အလိုရှိလျှင် ယှဉ်ပြပြီးအသုံးပြုနိုင်သည်)။ ကြည့်ရှုရန်: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)။
3. hub ထဲမှာ **project** တစ်ခုဖန်တီးပါ။
4. **Models + Endpoints** → **Deploy model** မှ မော်ဒယ်တစ်ခု (ဥပမာ `gpt-5-mini`) ကို deploy လုပ်ပါ။

### အဆင့် ၂: Project Endpoint နဲ့ Model Deployment Name ရယူခြင်း

Microsoft Foundry portal မှ သင့် project ထဲမှာ:

- **Project Endpoint** — **Overview** စာမျက်နှာသို့သွားပြီး endpoint URL ကို ကူးယူပါ။

![Project Connection String](../../../translated_images/my/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** သွားပြီး deploy ထားသော မော်ဒယ်ကို ရွေးယူပြီး **Deployment name** (ဥပမာ `gpt-5-mini`) ကို မှတ်သားပါ။

### အဆင့် ၃: `az login` ဖြင့် Azure တွင် လက်မှတ်ထိုးဝင်ရောက်ခြင်း

Jupyter notebook များသည် သင့် **Azure CLI sign-in** စနစ်ဖြင့် အတည်ပြုမှုများ ပြုလုပ်သည် — `AzureCliCredential` သို့မဟုတ် `DefaultAzureCredential` (အောက်ပါ `az login` session ကို ဖမ်းယူသည်) ကို `azure-identity` package မှ အသုံးပြုသည် — အတည်ပြုရန် API key မလိုအပ်ဘဲ လည်ပတ်ပါတယ်။ တချို့ သင်ခန်းစာများနှင့် ထည့်သွင်းမှုများတွင် API keys ဖြင့် အတည်ပြုမှု လိုအပ်နိုင်သောကြောင့် သင်ခန်းစာစာရင်းမှုအနေဖြင့် environment variables စစ်ဆေးပါ။ CLI ဖြင့် လက်မှတ်ထိုးဝင်ထားကြောင်းလိုအပ်သည်။

1. **Azure CLI ကို install လုပ်ပါ** (မရှိသေးလျှင်): [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **လက်မှတ်ထိုးဝင်ရန်** အောက်ပါအတိုင်း run ပါ:

    ```bash
    az login
    ```

    browser မဲ့ remote/Codespace ပတ်ဝန်းကျင်တွင်ပါက:

    ```bash
    az login --use-device-code
    ```

3. **သင့် Subscription ကို ရွေးချယ်ပါ** — သင့် Foundry project ပါဝင်သော subscription ကိုရွေးပါ။

4. **လက်မှတ်ထိုးဝင်မှု အတည်ပြုပါ**:

    ```bash
    az account show
    ```

> **ဘာကြောင့် `az login` လဲ?** notebooks များသည် `azure-identity` package မှ `AzureCliCredential` (သို့မဟုတ် `DefaultAzureCredential` ကို အသုံးပြု၍ သင့် Azure CLI လက်မှတ်ထိုးစက်ရှင်ကို ဖမ်းယူပြီး) အသုံးပြုပါသည်။ ထို့ကြောင့် API keys သို့မဟုတ် အရေးကြီးသော secret များ `.env` ဖိုင်တွင် မသွင်းရပါ။ ဒါဟာ [လုံခြုံရေးအတွက် အကောင်းဆုံး လမ်းညွှန်ချက်](https://learn.microsoft.com/azure/developer/ai/keyless-connections) ဖြစ်ပါသည်။

### အဆင့် ၄: သင့် `.env` ဖိုင် ကိုဖန်တီးပါ

ဥပမာဖိုင်ကို ကူးယူပါ:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

`.env` ဖိုင်ကို ဖွင့်ပြီး အောက်ပါတန်ဖိုးများ ဖြည့်စွက်ပါ

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| အပြောင်းအလဲ | ရှာဖွေရာနေရာ |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → သင့် project → **Overview** စာမျက်နှာ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → သင် deploy ထားသော မော်ဒယ်အမည် |

ဒီအထိ လုပ်ပါမယ်ဆိုရင် သင်ခန်းစာအများစုအတွက် ကောင်းမွန်ပါပြီ။ notebooks များသည် သင့် `az login` session ဖြင့် အလိုအလျောက် အတည်ပြုမှု ပြုလုပ်ပါလိမ့်မယ်။

### အဆင့် ၅: Python Dependencies များ ထည့်သွင်းပါ

```bash
pip install -r requirements.txt
```

သင်ဖန်တီးထားသော virtual environment ထဲတွင် သုံးရန် အကြံပြုသည်။

## စိတ်ကြိုက်တပ်ဆင်ခြင်း: Azure AI Search (သင်ခန်းစာ ၅ နှင့် ၁၆)

သင်ခန်းစာ ၅ (Agentic RAG) နှင့် သင်ခန်းစာ ၁၆ ဖိုင်များမှာ မည်သည့်အပို resource အသုံးမပြုဘဲ **in-memory knowledge base** ဖြင့် တိုက်ရိုက် run နိုင်သည်။ သင့်ရဲ့နောက်ခံအနေနဲ့ တကယ့် **Azure AI Search** index အသုံးပြုချင်သော်လည်း သင်ခန်းစာ ၁၆ notebook သည် ယခုအခါ key-based authentication ကိုသာ သုံးသည်။ အဲဒါက `AZURE_SEARCH_SERVICE_ENDPOINT` နဲ့ `AZURE_SEARCH_API_KEY` နှစ်ခုလုံး သတ်မှတ်ထားမှသာ memory-based search မှ Azure AI Search သို့ ပြောင်းသွားပြီး၊ မဟုတ်လျှင် အမြဲ memory search ကို သုံးပါသည်။ ထို့ကြောင့် တကယ် index ကို အသုံးပြုရန် admin key ကိုလည်း သတ်မှတ်ထားရန်လိုပါသည်။ keyless authentication ကို Microsoft Entra ID (RBAC) ဖြင့် သုံးရန် သင့်ရဲ့ production code တွင် အကြံပြုသည်။ ဒီသင်တန်းရဲ့ အခြားနေရာများတွင် အသုံးပြုထားသော `az login` လမ်းကြောင်းနှင့် ကိုက်ညီသည်။

အောက်ပါ RBAC အဆင့်များသည် setup-guide နမူနာများနှင့် သင့်ကိုယ်ပိုင်ကုဒ်များအတွက်လည်း သက်ဆိုင်သည်။ သင်ခန်းစာ ၁၆ notebook မှာ keyless auth ကို မရရှိစေ; သင်ခန်းစာ ၁၆ ကမ်းလှမ်းမှုအတွက် endpoint နဲ့ admin key နှစ်ခုလုံး လိုအပ်သေးသည်။

1. သင်၏ search service တွင် role-based access ကို ခွင့်ပြုပါ။

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. လိုအပ်သော အခန်းကဏ္ဍများ (index ဖန်တီးခြင်း၊ load လုပ်ခြင်း နှင့် မေးမြန်းခြင်း) ကို ကိုယ်ပိုင် ရယူပါ။

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. `.env` ဖိုင်အတွင်း endpoint ကို ထည့်သွင်းပါ။

| အပြောင်းအလဲ | ရှာဖွေရာနေရာ |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → သင့် **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | လက်ရှိ key-based auth ဖြင့် အသုံးပြုရန်လိုရှိသော Azure AI Search အတွက် လိုအပ်သည်။ Azure portal → **Settings** → **Keys** → primary admin key |

> **ဘာကြောင့် keyless?** Admin keys များသည် သင့် search service တွင် အပြည့်အဝ စာရေးခွင့် ထောက်ပံ့ပြီး .env ဖိုင်မှ ဖြန့်ဝေခြင်းဖြစ်နိုင်သည်။ RBAC ဖြင့် သင့် `az login` အချက်အလက်ကိုအသုံးပြုသည်။ ဒီဟာက သင့်ရဲ့သင်ခန်းစာ notebooks များထဲမှာ အသုံးပြုထားသော keyless Entra ID နမူနာဖြစ်သည် (`AzureCliCredential` / `DefaultAzureCredential`)။ [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) ကို ကြည့်ပါ။

Python နဲ့ .NET မှာ index ဖန်တီးနမူနာများအတွက် [Azure AI Search setup guide](./AzureSearch.md) ကိုကြည့်ပါ။

## Azure OpenAI ကို တိုက်ရိုက်ခေါ်သုံးသည့် သင်ခန်းစာများအတွက် အပိုပြင်ဆင်မှု (သင်ခန်းစာ ၆ နှင့် ၈)

သင်ခန်းစာ ၆ နှင့် ၈ အချို့ notebooks တွင် **Azure OpenAI** ကို တိုက်ရိုက် (Responses API အသုံးပြု၍) Microsoft Foundry အသုံးမပြုဘဲခေါ်သုံးသည်။ ဒီနမူနာများဟာ ယခင်က GitHub Models ကို အသုံးပြုခဲ့ပြီး အဲဒါဟာ deprecated ဖြစ်ပြီး Responses API ကို မထောက်ပံ့တော့ဘူး။ အောက်ပါ variable များကို `.env` ဖိုင်ထဲထည့်ပါ။

| အပြောင်းအလဲ | ရှာဖွေရာနေရာ |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → သင့် **Azure OpenAI** resource → **Keys and Endpoint** → Endpoint (ဥပမာ `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | သင် deploy ထားသော မော်ဒယ်အမည် (ဥပမာ `gpt-5-mini`) သည် Responses API ကို ထောက်ပံ့သည် |
| `AZURE_OPENAI_API_KEY` | ရွေးချယ်စရာ — `az login` / Entra ID မလိုဘဲ key-based auth သုံးချင်လျှင်သာ |

> Responses API သည် `/openai/v1/` stable endpoint ကို အသုံးပြုတဲ့အတွက် `api-version` မလိုအပ်ပါ။ Keyless Entra ID auth ကိုအသုံးပြုရန် `az login` ဖြင့် လက်မှတ်ထိုးဝင်ပါ။

## အခြား Provider: MiniMax (OpenAI-Compatible)

[MiniMax](https://platform.minimaxi.com/) သည် OpenAI-Compatible API မှတဆင့် 204K token အထိ ရနိုင်သော large-context မော်ဒယ်များကို ပံ့ပိုးသည်။ Microsoft Agent Framework ရဲ့ `OpenAIChatClient` သည် OpenAI-compatible endpoint များနှင့် လက်တွဲလုပ်နိုင်သောကြောင့် MiniMax ကို lessons တွေရဲ့ `OpenAIChatClient` အသုံးပြုမှုအတွက် အစားထိုးဖြစ်အောင် သုံးနိုင်သည်။

အောက်ပါ variables များကို `.env` ထဲထည့်ပါ။

| အပြောင်းအလဲ | ရှာဖွေရာနေရာ |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` (Default တန်ဖိုး) အသုံးပြုပါ |
| `MINIMAX_MODEL_ID` | အသုံးပြုမယ့် model အမည် (ဥပမာ `MiniMax-M3`) |

**ဥပမာမော်ဒယ်များ** — `MiniMax-M3` (အကြံပြု), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (တုံ့ပြန်မှု မြန်) မော်ဒယ်အမည်များ နှင့် ရရှိနိုင်မှုများကာလအလိုက် ပြောင်းလဲနိုင်ပြီး သင့်အကောင့်အပေါ် မူတည်သည်။

`OpenAIChatClient` ကို အသုံးပြုသည့် ကုဒ်နမူနာများ (ဥပမာ သင်ခန်းစာ ၁၄ ဟိုတယ် booking workflow) သည် `MINIMAX_API_KEY` သတ်မှတ်ထားသောအခါ သင့် MiniMax configuration ကို အလိုအလျောက် တွေ့ရှိပြီး သုံးပါလိမ့်မယ်။


## အခြားရွေးချယ်စရာ ပံ့ပိုးသူ: Novita AI (OpenAI-နှိုင်းယှဉ်မှု ပါဝင်သည်)

[Novita AI](https://novita.ai/llm-api) သည် open-source နှင့် frontier LLM များ (DeepSeek, Llama, Qwen စသည်ဖြင့်) အတွက် OpenAI-နှိုင်းယှဉ်နိုင်သော API ကို ပံ့ပိုးပေးသည်။ Microsoft Agent Framework ရဲ့ `OpenAIChatClient` သည် OpenAI-နှိုင်းယှဉ်မှုရှိသည့် endpoint များနှင့် အလုပ်လုပ်နိုင်သောကြောင့် Novita AI ကို Azure OpenAI သို့မဟုတ် OpenAI အစား အလွယ်တကူ အသုံးပြုနိုင်သည်။

သင်၏ `.env` ဖိုင်တွင် အောက်ပါ variable များကို ထည့်သွင်းပါ။

| Variable | သွားရှာရမည့်နေရာ |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | `https://api.novita.ai/openai/v1` (ပုံမှန်တန်ဖိုး) ကို အသုံးပြုပါ |
| `NOVITA_MODEL_ID` | အသုံးပြုမည့် model အမည် (ဥပမာ `moonshotai/kimi-k3`) |

**ဥပမာ model များ**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`။ Novita AI သည် Llama, Qwen, GLM စသည့် အခြား open-source model များကိုလည်း ပံ့ပိုးသည်။ လက်ရှိ မော်ဒယ်စာရင်းနှင့် model ID များသည် [Novita AI model library](https://novita.ai/llm-api) တွင် ကြည့်ရှုနိုင်ပါသည်။

လက်ရှိ ဥပမာများတွင် `NOVITA_*` variable များကို အလိုအလျောက် အသုံးမပြုပါ။ Novita AI ကို အသုံးပြုလိုပါက `OpenAIChatClient` ကို တည်ဆောက်စဉ် အထက်ဖော်ပြထားသည့်တန်ဖိုးများကို ဖော်ပြပါ။

## အခြားရွေးချယ်စရာ ပံ့ပိုးသူ: Foundry Local (မော်ဒယ်များကို စက်ပေါ်တွင် ပေးဆောင်ခြင်း)

[Foundry Local](https://foundrylocal.ai) သည် သက်သေလွယ်ကူပြီး မိမိစက်ပေါ်တွင် OpenAI-နှိုင်းယှဉ်နိုင်သည့် API ဖြင့် ဘာသာစကားမော်ဒယ်များကို ဒေါင်းလုပ် ဆွဲ၊ စီမံခန့်ခွဲ၍ ဆော့ဖ်ဝဲဝန်ဆောင်မှု ထောက်ပံ့ပေးသည်။ cloud မလိုအပ်ပါ။

Microsoft Agent Framework ရဲ့ `OpenAIChatClient` သည် OpenAI-နှိုင်းယှဉ်မှုရှိသည့် endpoint များနှင့် အလုပ်လုပ်နိုင်သဖြင့် Foundry Local ကို local မော်ဒယ်အနေဖြင့် Azure OpenAI အစား လွယ်ကူစွာ အသုံးပြုနိုင်ပါသည်။

**1. Foundry Local ကို ထည့်သွင်းပါ**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. မော်ဒယ်တစ်ခုကို ဒေါင်းလုပ်ဆွဲပြီး စက်ပေါ်တွင် စတင်အလုပ်လုပ်ရန် (ဒီအဆင့်တွင် local ဝန်ဆောင်မှု စတင်သည်)**

```bash
foundry model list          # ရနိုင်သော မော်ဒယ်များ ကြည့်ပါ
foundry model run phi-4-mini
```

**3. local endpoint ကို ရှာဖွေရန် အသုံးပြုမည့် Python SDK ကို ထည့်သွင်းပါ**

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework ကို သင်၏ local model သို့ ဖွင့်ချိန်**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# လိုအပ်ပါက ဒေါင်းလုပ်လုပ်ပြီး မော်ဒယ်ကို ဒေသတွင်းတွင် ရောင်းချပေး၍၊ ပြီးနောက် endpoint/port ကို ရှာဖွေသည်။
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ဥပမာ http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local အတွက် အမြဲ "လိုအပ်မှုမရှိ" ဖြစ်သည်။
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **မှတ်ချက်:** Foundry Local သည် OpenAI-compatible **Chat Completions** endpoint ကို ထံပေးသည်။ local စမ်းသပ်မှုနှင့် အော့ဖ်လိုင်းအခြေအနေများတွင် အသုံးပြုပါ။ အပြည့်အစုံ **Responses API** လုပ်ဆောင်ချက်များအတွက် (ဖွဲ့စည်းသိမ်းဆည်းထားသော ပြောဆိုဆက်သွယ်မှု စသည်တို့) Azure OpenAI သို့မဟုတ် Microsoft Foundry စီမံကိန်းကိုအသုံးပြုပါ။

## သင်ခန်းစာ ၈ (Bing Grounding Workflow) အတွက် နောက်ထပ် ပြင်ဆင်မှုများ

သင်ခန်းစာ ၈ တွင် conditional workflow notebook သည် Microsoft Foundry မှာ ဖြင့်ထားသော **Bing grounding** ကို အသုံးပြုထားသည်။ ထိုနမူနာကို လုပ်ဆောင်လိုပါက သင်၏ `.env` ဖိုင်တွင် အောက်ပါ variable ကို ထည့်သွင်းပါ။

| Variable | သွားရှာရမည့်နေရာ |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry ဝဘ်ဆိုဒ် → သင်၏စီမံကိန်း → **Management** → **Connected resources** → သင်၏ Bing connection → connection ID ကို မိတ္တူထုတ်ပါ |

## ပြဿနာဖြေရှင်းမှု

### macOS ပေါ်တွင် SSL Certificate စစ်ဆေးမှု အမှားများ

မိမိသည် macOS နှင့် အလုပ်လုပ်ပြီး အောက်ပါအမှားမျိုးတွေ့လျှင် -

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

သည် macOS ပေါ်တွင် Python နှင့် လုပ်ဆောင်ရာတွင် စနစ် SSL certificates များကို အလိုအလျောက် ယုံကြည်မှုမပြုဘဲ ဖြစ်သော ပြဿနာတစ်ခုဖြစ်သည်။ အောက်ပါ နည်းလမ်းများကို လိုက်လံ လုပ်ဆောင်ကြည့်ပါ။

**ရွေးချယ်စရာ ၁: Python Install Certificates script ကို လုပ်ဆောင်ပါ (အကြံပြု)**

```bash
# သင့်တပ်ဆင်ထားသော Python ဗားရှင်းဖြင့် 3.XX ကို အစားထိုးပါ (ဥပမာ၊ 3.12 သို့မဟုတ် 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ရွေးချယ်စရာ ၂: သင့် notebook တွင် `connection_verify=False` ကို အသုံးပြုပါ (GitHub Models notebooks အတွက်သာ)**

Lesson 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) တွင် ပါရှိသော မှတ်ချက်ထည့်ထားသော workaround ကို အသုံးပြုနိုင်သည်။ certificate error တွေ့လျှင် `connection_verify=False` ကို uncomment ပြုလုပ်ပါ။

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # စာရွက်ပြားမှားယွင်းမှုများဖြစ်ပါက SSL အတည်ပြုခြင်းကို ပိတ်ရန်
)
```

> **⚠️ သတိပြုရန်:** SSL စစ်ဆေးမှုကို ပိတ်ထားခြင်း (`connection_verify=False`) သည် လုံခြုံမှုကို လျော့ပါးစေပြီး certificate အတည်ပြုမှုကို ကျော်လွှားသွားမည်ဖြစ်သည်။ development ပတ်ဝန်းကျင်တွင် ယာယီ ဖြေရှင်းနည်းအနေဖြင့်သာ အသုံးပြုပါ။ production အတွက် မသုံးသင့်ပါ။

**ရွေးချယ်စရာ ၃: `truststore` ကို ထည့်သွင်းပြီး အသုံးပြုပါ**

```bash
pip install truststore
```

ထို့နောက် network call သည်မပြုမီ သင်၏ notebook သို့မဟုတ် script အပေါ်မျက်နှာပြင်တွင် အောက်ပါ အတိုင်း ထည့်ပါ။

```python
import truststore
truststore.inject_into_ssl()
```

## တခြားပြဿနာတစ်ခုခု ပါသလား?

ဒီ setup ကို မည်သည့်ပြဿနာကိုမဆို တွေ့ကြုံပါက ကျွန်ုပ်တို့၏ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> သို့မဟုတ် <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">issue ဖန်တီးရန်</a> ဝင်ရောက် ဆက်သွယ်နိုင်ပါသည်။

## နောက်တစ်ခေါက်စာသင်ခန်းစာ

ဒါဖြင့် သင်နေသော သင်ခန်းစာအတွက် ကုဒ်များကို လုပ်ဆောင်ရန် ပြင်ဆင်ပြီး ဖြစ်ပါပြီ။ AI Agents ၏ ကမ္ဘာကြီးကို ပိုမိုသိရှိလေ့လာဖို့ ပျော်ရွှင်စွာ သင်ယူပါ။

[AI Agents နှင့် Agent အသုံးပြုမှုများ စတင်ခြင်း](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->