# သင်တန်း စတင်ချိန်

## နိဒါန်း

ဤသင်ခန်းစာသည် သင်တန်း၏ ကိုဒ်နမူနာများကို မည်သို့ချည့်ရမည်ကိုဖော်ပြပါမည်။

## အခြားလေ့လာသူများနှင့် စည်းဝေးကူညီမှုရယူရန်

သင့်ရဲ့ repo ကို ကလုံးခြင်းမပြုမီ၊ [AI Agents For Beginners Discord နာရီချန်နယ်](https://aka.ms/ai-agents/discord) တွင် ပါဝင်ကူညီမှု၊ သင်တန်းနှင့်ပတ်သက်သော မေးခွန်းများအတွက် သို့မဟုတ် အခြားလေ့လာသူများနှင့် ဆက်သွယ်ရန် ပါဝင်ပါ။

## Repo ဒီကို ကလုံးခြင်း သို့မဟုတ် Fork လုပ်ခြင်း

စတင်ရန် GitHub Repository ကို ကျေးဇူးပြု၍ ကလုံးခြင်း သို့မဟုတ် fork လုပ်ပါ။ ၎င်းသည် သင်တန်းပစ္စည်း၏ ကိုယ်ပိုင် ဗားရှင်းကို ဖန်တီးပေးပြီး သင်သည် ကိုဒ်ကို ပြေးစမ်း၊ စမ်းသပ်၊ ပြင်ဆင်နိုင်သည်။

၎င်းအား <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repo ကို fork လုပ်ရန်</a> ခလုတ်ကို နှိပ်ခြင်းဖြင့် ပြုလုပ်နိုင်သည်

ယခု သင်မှာ ဤသင်တန်း၏ ကိုယ်ပိုင် fork လုပ်ထားသော ဗားရှင်းအား အောက်ပါလင့်ခ်တွင်ရှိနေပါပြီ-

![Forked Repo](../../../translated_images/my/forked-repo.33f27ca1901baa6a.webp)

### အနည်းငယ် ကလုံးခြင်း (Workshop / Codespaces အတွက် အကြံပြု)

  >မှတ်ချက်-အပြည့်အစုံကို ရယူသည်မှာ (လက်ရှိထည့်သွင်းမှု အပြည့်အစုံနှင့် ဖိုင်အားလုံးပါ ~3 GB) အရွယ်ကြီးနိုင်သည်။ သင်သည် workshop ပဲ တက်ရောက်မည်ဆိုပါက သို့မဟုတ် သင်ခန်းစာဖိုဒါ အနည်းငယ်ပဲ လိုပါက အနည်းငယ် ကလုံးခြင်း (သို့မဟုတ် sparse ကလုံးခြင်း) ကို အသုံးပြုခြင်းဖြင့် အများဆုံးဒေါင်းလုပ်ကိုယ်တာမှ ရှောင်လွှဲနိုင်သည် (သမိုင်းကိုတ်ခြင်း/ blob များ မယူခြင်း)။

#### လျွောက်လွှာ အနည်းငယ် ကလုံးခြင်း — သမိုင်းနိမ့် အနည်းဆံုး၊ ဖိုင်အားလုံး

အောက်ပါ command များတွင် `<your-username>` ကို သင့် fork URL (သို့မဟုတ် upstream URL ကို သုံးချင်ပါက) ဖြင့် အစားထိုးပါ။

နောက်ဆုံး commit သမိုင်းကိုသာ ကလုံးရန် (ဒေါင်းလုပ်သေးရေ) ကိုင်တွယ်ပါ:

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

အထူးတစ်ခွင့်ခွဲ ကို ကလုံးရန်:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### အစိတ်အပိုင်း (sparse) ကလုံးခြင်း — blob အနည်းငယ် + ဖိုဒါများ ထောက်ပြချက်အရသာရွေးချယ်ခြင်း

၎င်းသည် partial clone နှင့် sparse-checkout ကို အသုံးပြုသည် (Git 2.25+ လိုအပ်ပြီး partial clone လုပ်ထားသော နောက်ဆုံး Git အတွက် အကြံပြု).

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

repo ဖိုဒါထဲ သွားပါ:

```bash|powershell
cd ai-agents-for-beginners
```

အသုံးပြုလိုသော ဖိုဒါများကို သတ်မှတ်ပါ (အောက်ပါ ဥပမာတွင် ဖိုဒါ ၂ ခု ပြသထားသည်):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

ကလုံးပြီး ဖိုင်များကို အတည်ပြုပြီးနောက် သင် ဖိုင်များကိုသာ လိုအပ်ပြီးနေရာပိုင်ခွင့် ရယူလိုပါက (git သမိုင်း မပါ) repo metadata ကို ဖျက်ပစ်ပါ (💀 ပြန်ဘယ်မရ။ Git လုပ်ဆောင်ချက်များအားလုံး ပျောက်ဆုံးသည်- commit မရှိ၊ pull မလုပ်နိုင်၊ push မလုပ်နိုင်၊ သမိုင်း ကြည့်ရှုမှု မရှိ။

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ကို အသုံးပြုခြင်း (ဒေါင်းလုပ်ကြီးများကို ရှောင်ရန် အကြံပြု)

- ဒီ repo အတွက် [GitHub UI](https://github.com/codespaces) မှ Codespace အသစ် တစ်ခု ဖန်တီးပါ။  

- အသစ်ဖန်တီးသော Codespace ၏ terminal မှ shallow/sparse ကလုံး command များကို သုံးပြီး သင့်လိုအပ်သော သင်ခန်းစာ ဖိုဒါများကို Codespace အလုပ်ကွင်းထဲ ရယူပါ။
- ရွေးချယ်စရာ- Codespaces တွင် clone ပြီးနောက် .git ကို ဖျက်ပစ်၍ နေရာ ပိုလျှော့ပါ (အထက်ဖော်ပြသော ဖျက်ပစ် command များကြည့်ပါ)။
- မှတ်ချက်- Repo ကို ဒါရိုက် ကျ Codespaces ထဲ တိုက်ရိုက်ဖွင့်ရန် ရွေးပါက (clone သေးတင့်မဟုတ်ဘဲ), Codespaces သည် devcontainer ပတ်ဝန်းကျင်ကို ဖန်တီးပေးပြီး သင့်လိုအပ်ချက်ထက်ပို Provision လုပ်ပေးနိုင်သည်။ သင့်ကိုယ်ပိုင် fresh Codespace ထဲ shallow copy ကလုံးခြင်းဖြင့် диск နှုန်းများ ထိန်းချုပ်မှုပိုမို ရရှိမည်။

#### အကြံပြုချက်များ

- ကိုယ်တိုင် ပြင်ဆင်/commit လုပ်လိုပါက clone URL ကို သင့် fork URL ဖြင့် အမြဲအစားထိုးပါ။
- နောက်မှ သမိုင်းပိုများ သို့မဟုတ် ဖိုင်ပိုများ လိုအပ်လာပါက fetch လုပ်နိုင်ပြီး sparse-checkout ဖြင့် ဖိုဒါ များ ထပ်ထည့်နိုင်သည်။

## ကိုဒ် အလုပ်လုပ်ခြင်း

ဤသင်တန်းသည် AI Agents ဖန်တီးခြင်းအတွက် လက်တွေ့ အတွေ့အကြုံရရှိရန် အသုံးပြုနိုင်သော Jupyter Notebooks စုစည်းမှုတစ်ခုကို ပေးပါသည်။

ကိုဒ်နမူနာများသည် **Microsoft Agent Framework (MAF)** ကို `FoundryChatClient` နှင့် အသုံးပြုသည်။ ၎င်းသည် **Microsoft Foundry** မှတစ်ဆင့် **Microsoft Foundry Agent Service V2** (Responses API) နှင့် ချိတ်ဆက်ထားသည်။

Python notebooks အားလုံးမှာ `*-python-agent-framework.ipynb` ဟူသော အမှတ်အသားရှိပါသည်။

## လိုအပ်ချက်များ

- Python 3.12+  
  - **မှတ်ချက်**: Python3.12 မရှိပါက ထည့်သွင်းရန် လိုအပ်သည်။ ထို့နောက် python3.12 ဖြင့် virtual environment ကို ဖန်တီးပြီး လိုအပ်သော package များကို requirements.txt မှ တင်သွင်းပေးရန်။
  
    >ဥပမာ

    Python venv directory ဖန်တီးခြင်း:

    ```bash|powershell
    python -m venv venv
    ```

    ထို့နောက် venv environment ကို အောက်ပါအတိုင်း ချိန်ဆက်ပါ:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+ : .NET ကို သုံးသော နမူနာကိုဒ်များအတွက် [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) သို့မဟုတ် နောက်ဆုံးဗားရှင်းကို ထည့်သွင်းထားမှသာ မည်သည့် .NET SDK ကို ထည့်သွင်းထားသည်ကိုစစ်ဆေးပါ။

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — authentication အတွက် လိုအပ်သည်။ [aka.ms/installazurecli](https://aka.ms/installazurecli) မှ ထည့်သွင်းပါ။
- **Azure Subscription** — Microsoft Foundry နှင့် Microsoft Foundry Agent Service အတွက် ဝင်ရောက်ခွင့်။
- **Microsoft Foundry Project** — တပ်ဆင်ပြီးရှိသော မော်ဒယ်ပါရှိသော project (ဥပမာ- `gpt-5-mini`)။ [Step 1](#အဆင့်-၁-microsoft-foundry-project-တစ်ခု-ဖန်တီးပါ) ကိုကြည့်ပါ။

ဤ repo ၏ root တွင် `requirements.txt` ပါဝင်ပြီး ကိုဒ်နမူနာများကို chạyရန် လိုအပ်သော Python package များကို ပါဝင်ထားသည်။

terminal မှာ အောက်ပါတို့ကို ရိုက်ထည့်လို့ package များကို ထည့်သွင်းနိုင်သည်။

```bash|powershell
pip install -r requirements.txt
```

ပြဋ္ဌာန်းချက် ပြဿနာများ ရှောင်ရန် Python virtual environment ဖန်တီးပြီး ကျွမ်းကျင်စွာ သုံးရန် အကြံပြုပါသည်။

## VSCode ကို တပ်ဆင်ခြင်း

VSCode တွင် သင့်အသုံးပြုမည့် Python ဗားရှင်းမှန်ကန်ကြောင်း အာမခံပါ။

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry နှင့် Microsoft Foundry Agent Service ကို တပ်ဆင်ခြင်း

### အဆင့် ၁: Microsoft Foundry Project တစ်ခု ဖန်တီးပါ

Notebooks များ ရှေ့ မောင်းရန် စွဲထားပြီး project နှင့် hub တို့ လိုအပ်ပါသည်။

၁။ [ai.azure.com](https://ai.azure.com) သို့သွား၍ သင့် Azure အကောင့်ဖြင့် ဝင်ပါ။
၂။ **hub** အသစ် ဖန်တီးပါ (သို့မဟုတ် ရှိရှိ hub ကို အသုံးပြုပါ)။ [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources) ကို ကြည့်ပါ။
၃။ hub အတွင်း သို့ ဝင်၍ **project** တစ်ခု ဖန်တီးပါ။
၄။ **Models + Endpoints** → **Deploy model** မှ မော်ဒယ်တစ်ခု (ဥပမာ- `gpt-5-mini`) ကို တပ်ဆင်ပါ။

### အဆင့် ၂: Project Endpoint နှင့် Model Deployment နာမည် ရယူခြင်း

Microsoft Foundry portal တွင် သင့် project မှ:

- **Project Endpoint** — **Overview** စာမျက်နှာသို့ သွား၍ endpoint URL ကို ကူးယူပါ။

![Project Connection String](../../../translated_images/my/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** သို့ သွား၍ တပ်ဆင်ထားသော မော်ဒယ်ကို ရွေးပါ၊ **Deployment name** (ဥပမာ- `gpt-5-mini`) ကို မှတ်သားပါ။

### အဆင့် ၃: `az login` ဖြင့် Azure မှာ ဝင်ရောက်ခြင်း

Notebooks များသည် authentication အတွက် **`AzureCliCredential`** ကို အသုံးပြုသည် — API key မလိုအပ်ပါ။ သင့်ကို Azure CLI ဖြင့် ဝင်ထားရမည်။

၁။ **Azure CLI ကို ထည့်သွင်းပါ** - [aka.ms/installazurecli](https://aka.ms/installazurecli)

၂။ **ဝင်ရန်** အောက်ပါ command ကို run ပါ။

    ```bash|powershell
    az login
    ```

    ဒါမှမဟုတ် browser မရှိတဲ့ remote/Codespace ပတ်ဝန်းကျင်မှာ ရှိပါက:

    ```bash|powershell
    az login --use-device-code
    ```

၃။ **သင်၏ Subscription ကို ရွေးချယ်ပါ** (ဖေါ်ပြပါက) — သင့် Foundry project ပါဝင်သော subscription ကို ရွေးချယ်ပါ။

၄။ **ဝင်ထားကြောင်း အတည်ပြုပါ** -

    ```bash|powershell
    az account show
    ```

> **`az login` ရဲ့ အနှစ်သာရ?** Notebooks များသည် `azure-identity` package ထဲက `AzureCliCredential` ကို အသုံးပြုပြီး authentication လုပ်သည်။ ဒါဟာ သင့် Azure CLI session ကလီဒင်ရှယ်များ ပေးစွမ်းသည့်အတွက် API keys သို့မဟုတ် လျှို့ဝှက်ချက်များကို `.env` ဖိုင်တွင် မလိုအပ်တော့ပါ။ ၎င်းသည် [လုံခြုံရေးအကောင်းဆုံး လေ့ကျင်မှုတစ်ခု](https://learn.microsoft.com/azure/developer/ai/keyless-connections) ဖြစ်သည်။

### အဆင့် ၄: သင့် `.env` ဖိုင်ကို ဖန်တီးပါ

ဥပမာ ဖိုင်ကို ကူးယူပါ:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

`.env` ဖိုင်ကို ဖွင့်ပြီး အောက်ပါ တန်ဖိုး ၂ ခု ဖြည့်ပါ -

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variable | ရှာဖွေရမည့်နေရာ |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → သင့် project → **Overview** စာမျက်နှာ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → တပ်ဆင်ထားသော မော်ဒယ် နာမည် |

ဒီသင်ခန်းစာများအတွက် ပြီးဆုံးပါပြီ! Notebooks များသည် သင့် `az login` session မှတဆင့် အလိုအလျောက် authentication လုပ်မည်။

### အဆင့် ၅: Python အားလိုအပ်သော package များ ထည့်သွင်းပါ

```bash|powershell
pip install -r requirements.txt
```

ယခင်ဖန်တီးထားသော virtual environment အတွင်းတွင် ၎င်းကို run စေခြင်းကို အကြံပြုပါသည်။

## သင်ခန်းစာ ၅ (Agentic RAG) အတွက် ထပ်ဆောင်း ပြင်ဆင်မှု

သင်ခန်းစာ ၅ သည် ရယူဖော်ပြန်ထုတ်မှု အတွက် **Azure AI Search** ကို သုံးသည်။ ဤသင်ခန်းစာ run လုပ်မည်ဆိုလျှင် `.env` ဖိုင်ထဲတွင် အောက်ပါ variables များ ထည့်သွင်းပါ -

| Variable | ရှာဖွေရမည့်နေရာ |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → သင့် **Azure AI Search** အရင်းအမြစ် → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → သင်၏ **Azure AI Search** အရင်းအမြစ် → **Settings** → **Keys** → primary admin key |

## Lessons 6 နှင့် 8 တွေမှာ Azure OpenAI ကို တိုက်ရိုက်ခေါ်သုံးခြင်း အတွက် ထပ်သွင်း စီစဉ်မှုများ

Lessons 6 နှင့် 8 တွင် အသုံးပြုသည့် notebooks များသည် **Microsoft Foundry project** မှတစ်ဆင့်မဟုတ်ဘဲ, **Responses API** ကို သုံးသော Azure OpenAI ကို တိုက်ရိုက်ခေါ်သုံးသည်။ ဤနမူနာများသည် ယူ GitHub Models ကို ယခင်က သုံးခဲ့ပြီး ထို Models သည် ၂၀၂၆ ခုနှစ် ဇူလိုင်တွင် ရုပ်သိမ်းမည်မဟုတ်ပဲ Responses API ကို မထောက်ပံ့တော့ပါ။ ၎င်းနမူနာများကို run မည်ဆိုလျှင် `.env` ထဲတွင် အောက်ပါ variables များ ထည့်ပါ -

| Variable | ရှာဖွေရမည့်နေရာ |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → သင်၏ **Azure OpenAI** အရင်းအမြစ် → **Keys and Endpoint** → Endpoint (ဥပမာ `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Responses API ကို ထောက်ပံ့သော သင်တပ်ဆင်ထားသော မော်ဒယ် နာမည် (ဥပမာ `gpt-5-mini`) |
| `AZURE_OPENAI_API_KEY` | ရွေးချယ်စရာ — `az login` / Entra ID ထက် key-based auth သုံးလျှင်သာ |

> Responses API သည် stable `/openai/v1/` endpoint ကို သုံးသည်၊ ဒါကြောင့် `api-version` မလိုပါ။ Keyless Entra ID authentication  သုံးရန် `az login` ဖြင့် ဝင်ရောက်ပါ။

## အခြား Provider: MiniMax (OpenAI-Compatible)

[MiniMax](https://platform.minimaxi.com/) သည် OpenAI-compatible API ဖြင့် သိုင်းကြီး token 204K အထိ မော်ဒယ်များကို ပေးသည်။ Microsoft Agent Framework ၏ `OpenAIChatClient` သည် OpenAI-compatible endpoint မည်သည့်ဟာကိုမဆို အသုံးပြုနိုင်သောကြောင့် MiniMax ကို Azure OpenAI သို့မဟုတ် OpenAI ၏ အစားထိုး အဖြစ် သုံးနိုင်သည်။

`.env` ဖိုင်ထဲတွင် အောက်ပါ variables များ ထည့်ပါ –

| Variable | ရှာဖွေရမည့်နေရာ |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | သုံးရန်- `https://api.minimax.io/v1` (ပုံမှန်တန်ဖိုး) |
| `MINIMAX_MODEL_ID` | သုံးမည့် မော်ဒယ် နာမည် (ဥပမာ `MiniMax-M3`) |

**မော်ဒယ်နမူနာများ**: `MiniMax-M3` (အကြံပြု), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (အမြန်တုံ့ပြန်မှု)။ မော်ဒယ်နာမည်များနှင့် ရရှိနိုင်မှုသည် အချိန်နှင့်အညီပြောင်းနိုင်သည်၊ သင့်အကောင့် သို့မဟုတ် ဒေသပေါ် မူတည်၍ မော်ဒယ်ချင်း အသုံးပြုခွင့်ရှိ/မရှိ တိုင်းတာသည်။ သက်ဆိုင်ရာ စာရင်းအတွက် [MiniMax Platform](https://platform.minimaxi.com/) ကြည့်ပါ။ `MiniMax-M3` သင့်အကောင့်တွင် မရရှိပါက `MINIMAX_MODEL_ID` တွင် သင့်အကောင့် ရရှိနိုင်သည့် မော်ဒယ်တစ်ခု (ဥပမာ- `MiniMax-M2.7`) ထည့်သွင်းပါ။

`OpenAIChatClient` (ဥပမာ - သင်ခန်းစာ 14 ဟိုတယ်ဘွတ်ကင် ဝါသနာ) ကိုသုံးသော ကိုဒ်နမူနာများသည် `MINIMAX_API_KEY` များထားရှိထားပါက သင့် MiniMax ဖန်တီးချက်ကို အလိုအလျောက် တွေ့ရှိအသုံးပြုမည်။

## အခြား Provider: Foundry Local (မော်ဒယ်များကို စက်ပေါ်တွင် တိုက်ရိုက် run)

[Foundry Local](https://foundrylocal.ai) သည် အလေးချိန်နည်းသော runtime ဖြစ်ပြီး မော်ဒယ်များကို ဒေါင်းလုပ်ရယူ စီမံခန့်ခွဲပြီး OpenAI-compatible API ဖြင့် **သင့်စက်ပေါ်တွင် တစ်ရပ်တည်း** သိမ်းဆည်း ပေးသည်။ Cloud မလိုအပ်၊ Azure subscription မလိုအပ်၊ API keys မလိုအပ်ပါ။ Offline development အတွက်၊ cloud ကုန်ကျစရိတ် မဖြစ်စေဖို့၊ ဒေတာများကို စက်ပေါ်မှာထားရှိချင်သောသူများအတွက် အထူးသင့်တော်သည်။

Microsoft Agent Framework ၏ `OpenAIChatClient` သည် OpenAI-compatible endpoint မည်သည့်ဟာနဲ့မဆို အလုပ်လုပ်နိုင်သဖြင့် Foundry Local ကို Azure OpenAI အစား ပင်အသုံးပြုနိုင်သည်။

**၁။ Foundry Local ထည့်သွင်းပါ**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**၂။ မော်ဒယ်တစ်ခု ဒေါင်းလုပ်ပြီး run ပါ** (local service  ကိုလည်း စတင်သည်) -

```bash
foundry model list          # ရနိုင်သော မော်ဒယ်များကိုကြည့်ပါ
foundry model run phi-4-mini
```

**၃။ local endpoint ကို ရှာဖွေရာတွင် အသုံးပြုသော Python SDK ကို ထည့်သွင်းပါ**

```bash
pip install foundry-local-sdk
```

**၄။ Microsoft Agent Framework ကို သင့်စက်ပေါ် မော်ဒယ်ဆီ ရွှေ့ပြောင်းပါ -**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# လိုအပ်ပါက ဒေါင်းလုဒ်လုပ်ပြီး မော်ဒယ်ကို ဒေသဆိုင်ရာတွင် စတင်ဆောင်ရွက်ပြီး၊ ပြီးလျောက် endpoint/port ကို ရှာဖွေသည်။
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ဥပမာ http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local အတွက် အမြဲ "မလိုအပ်ပါ" ဖြစ်သည်။
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **မှတ်ချက်:** Foundry Local သည် OpenAI-compatible **Chat Completions** endpoint ကို ပံ့ပိုးပေးသည်။ ဒါကို ဒေတာဆုံးရှုံးခြင်းမရှိဘဲ offline သက်ဆိုင်ရာနှင့် development အတွက် သုံးပါ။ **Responses API** အပြည့်အစုံအသုံးပြုမှုများ (stateful conversations, နက်ရှိုင်းသော tool orchestration, agent-style ဖွံ့ဖြိုးမှု) များအတွက် သင်ခန်းစာများအတိုင်း **Azure OpenAI** သို့မဟုတ် **Microsoft Foundry** project ကို ရည်ညွှန်းပါ။ [Foundry Local documentation](https://foundrylocal.ai) တွင် လက်ရှိ မော်ဒယ်စာရင်းနှင့် ပလက်ဖောင်း ထောက်ပံ့မှုကို ကြည့်ရှုနိုင်သည်။

## သင်ခန်းစာ ၈ (Bing Grounding Workflow) အတွက် ထပ်ဆောင်း ပြင်ဆင်ခြင်း


အတန်း ၈ မှ ကြီးကြပ်စောင့်ကြည့်မှုလုပ်ငန်းစဉ်မှတ်စုတွင် Microsoft Foundry မှ **Bing grounding** ကို အသုံးပြုထားသည်။ ဥပမာကို chạyရန် စီစဥ်ပါက၊ သင်၏ `.env` ဖိုင်တွင် ဒီအပြောင်းအလဲကို ထည့်သွင်းပါ။

| အပြောင်းအလဲ | ဘယ်မှာတွေ့မလဲ |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → သင်၏ ပရောဂျက် → **Management** → **Connected resources** → သင်၏ Bing ဆက်သွယ်ချက် → ဆက်သွယ်ချက် ID ကို ကူးယူပါ |

## ပြဿနာဖြေရှင်းခြင်း

### macOS တွင် SSL မှတ်ပုံတင်အတည်ပြုမှု အမှားများ

သင် macOS သုံးပြီး အောက်ပါအမှားဖြစ်ပေါ်ခဲ့ပါက -

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

၎င်းသည် macOS 系统တွင် Python အသုံးပြုရာတွင် စနစ် SSL မှတ်ပုံတင်များကို အလိုအလျောက် ယုံကြည်မှု မရရှိသော အမှားအကြောင်းဖြစ်သည်။ အောက်ပါ ဖြေရှင်းနည်းများကို နောက်တစ်ကြိမ်စဉ်းစားကြည့်ပါ။

**ရွေးချယ်စရာ ၁: Python ၏ Install Certificates လုပ်ဆောင်ချက်ကို chạy (အကြံပြုသည်)**

```bash
# သင်ထည့်သွင်းထားသော Python ဗားရှင်း (ဥပမာ၊ 3.12 သို့မဟုတ် 3.13) ဖြင့် 3.XX ကို အစားထိုးပါ:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ရွေးချယ်စရာ ၂: သင့်မှတ်စုတွင် `connection_verify=False` ကို သုံးပါ (GitHub Models မှတ်စုများအတွက်သာ)**

Lesson 6 မှတ်စု (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) တွင် မှတ်ချက်ထည့်ထားသော နည်းလမ်းလည်း ပါပြီးဖြစ်သည်။ client ဖန်တီးသည့်အခါ `connection_verify=False` ကို ပြန်ဖျက်ထုတ်ပါ။

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # လက်မှတ်အမှားများတွေ့ပါက SSL အတည်ပြုချက်ကို ပိတ်လိုက်ပါ
)
```

> **⚠️ သတိပေးချက်။:** SSL အတည်ပြုမှု ပိတ်ထားခြင်း (`connection_verify=False`) သည် မှတ်ပုံတင်အတည်ပြုချက်စစ်ဆေးမှုကို ကျော်လွန်ခြင်းကြောင့် လုံခြုံမှုလျော့နည်းစေပါသည်။ ဖွံ့ဖြိုးတိုးတက်မှုပတ်ဝန်းကျင်တွင် တစ်ခဏအတွက်သာ အသုံးပြုပါ၊ ထုတ်လွှင့်မှုတွင် မသုံးပါနှင့်။

**ရွေးချယ်စရာ ၃: `truststore` ကို ထည့်သွင်းအသုံးပြုပါ**

```bash
pip install truststore
```

ထို့နောက်၊ မှတ်စု သို့မဟုတ် စကရစ်ပ် ၏ အပေါ်အစပိုင်းတွင် နောက်ကောက်ခိုးခိုး မည်သည့် network ခေါ်ဆိုမှုမလုပ်မီ အောက်ပါ ကိုးဒ်ကိုထည့်ပါ။

```python
import truststore
truststore.inject_into_ssl()
```

## ဘာမှတ်စုတခုခုတွင် ပိတ်ဆို့နေပါသလား?

ဤစနစ်ကို ခရီးဆက်မည့်အခါ ပြဿနာများ ဖြစ်ပေါ်ပါက သင်၏ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> သို့ သွားရောက် ဆွေးနွေးနိုင်ပါသည် သို့မဟုတ် <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ပြဿနာတင်ပြနိုင်ပါသည်</a>။

## နောက်ထပ်သင်ခန်းစာ

သင်သည် ယခုသင်ကြားမည့် သင်ခန်းစာကို chạyဖို့ ပြင်ဆင်ပြီးဖြစ်ပါပြီ။ AI Agent များ၏ကမ္ဘာကြီးအကြောင်း တက်ကြွစွာလေ့လာရင်း ပျော်ရွှင်ပါစေ။

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->