# သင်တန်းပြင်ဆင်ခြင်း

## နိဒါန်း

ဤသင်ခန်းစာတွင် သင်တန်း၏ ကုဒ်နမူနာများကို မည်သို့ run ချမည်ကို ဖော်ပြမည်ဖြစ်သည်။

## အခြားသင်ယူသူများနှင့် ပူးပေါင်းကူညီရန်

သင်၏ repo ကို clone မလုပ်ခင် [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) တွင်ပါဝင်၍ ဆက်တင် ပြင်ဆင်မှုများအတွက်၊ သင်တန်းနှင့်ပတ်သက်သောမေးခွန်းများ၊ သို့မဟုတ် အခြားသင်ယူသူများနှင့်ဆက်သွယ်ရန် ဝင်ပါ။

## Repo ကို Clone သို့မဟုတ် Fork ဆွဲရန်

စတင်ရန် GitHub Repository ကို ကလုံး သို့မဟုတ် fork ဆွဲပါ။ ၎င်းသည် သင်တန်းပစ္စည်း၏ ကိုယ်ပိုင်ဗားရှင်းကို ရရှိစေပြီး ကုဒ်များကို ရှာဖွေ စမ်းသပ် ပြင်ဆင်နိုင်စေရန်ဖြစ်သည်။

၎င်းကို <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repo ကို fork ဆွဲရန်</a> link ကို နှိပ်ခြင်းဖြင့် ပြုလုပ်နိုင်သည်။

ယခု သင်၏ ကိုယ်ပိုင် fork ဆွဲထားသော သင်တန်းဗားရှင်းကို အောက်ပါလင့်ခ်တွင် ရရှိသင့်သည်-

![Forked Repo](../../../translated_images/my/forked-repo.33f27ca1901baa6a.webp)

### သက်သာသော Clone (ဆန်းသစ်ခြင်း / Codespaces အတွက် အကြံပြု)

> ဖိုင်နှင့် သမိုင်းကြောင်း အပြည့်အစုံ ဒေါင်းလုပ်လုပ်မည်ဆိုလျှင် ရှယ်ထောင့် (~3 GB) ကြီးမားနိုင်သည်။ သင်ကွင်းဆင်းသင်တန်းတက်မည်ဆိုလျှင် သို့မဟုတ် သင်ခန်းစာ folder အနည်းငယ်လိုအပ်ပါက သက်သာသော clone (သို့) sparse clone သည် သမိုင်းကြောင်းကို ပိုဒေါင်းလုဒ်ခြင်းမှ ရှောင်ရှားသည်။

#### မြန်ဆန်သက်သာသော clone — သမိုင်းဖြတ်တို၊ ဖိုင်များ အပြည့်အဝ

အောက်ပါ command များတွင် `<your-username>` ကို သင်၏ fork URL (သို့) upstream URL အစားထိုး၍ အသုံးပြုပါ။

နောက်ဆုံး commit သမိုင်းကို သာ clone ဆွဲရန် (ဒေါင်းလုပ်အသွေးသေး):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

အထူးခွဲထုတ်ထားသော branch ကို clone ဆွဲရန်:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### အပိုင်းအခြား (sparse) clone — blob နည်းပြီး ရွေးချယ်ထားသော folder များသာ clone ဆွဲခြင်း

Git 2.25+ နှင့် partial clone ကို ပံ့ပိုးသည့် သက်တမ်းရှိ Git ကို အသုံးပြု၍ partial clone နှင့် sparse-checkout ကိုအသုံးပြုသည်။

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Repo folder ထဲသို့ ဝင်ရောက်ရန်:

```bash|powershell
cd ai-agents-for-beginners
```

သင်လိုအပ်သော folder များကို သတ်မှတ်ပါ (ဥပမာတွင် folder နှစ်ခုပြထားသည်):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Clone ပြီးဖိုင်များ စစ်ဆေးပြီးပါက သင့်တွင် ဖိုင်ပိုပြီး လိုအပ်မရှိ၍ နေရာလွတ်လိုပါက repository metadata ကို ဖျက်ပစ်ပါ (💀မပြန်လည် ရနိုင်ပါမည် — Git အားလုံးလုပ်ဆောင်ချက် မရှိတော့ပါ: commit များ၊ pull များ၊ push များ သို့မဟုတ် သမိုင်းကြောင်းသွားရောက် ကြည့်ရှုခြင်း မပြုနိုင်ပါ)။

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces အသုံးပြုခြင်း (ဒေါင်းလုပ်ကြီးများကို သွားနေရခြင်းမှ ရှောင်ရှားရန် အကြံပြုသည်)

- [GitHub UI](https://github.com/codespaces) မှ ဒီ repo အတွက် Codespace အသစ်တစ်ခု ဖန်တီးပါ။

- Codespace ထဲရှိ terminal တွင် အထက်ပါ သက်သာသော/sparse clone commands များကို အသုံးပြုပြီး သင်လိုအပ်သော သင်ခန်းစာ folder များသာ Codespace စာရင်းသွင်းပါ။
- အလိုအလျောက်: Codespaces အတွင်း clone ပြီးပါက၊ အပိုနေရာရရှိရန် .git ဖိုင်ကို ဖျက်ပစ်ပါ (အထက်ပါ ဖျက်သိမ်း နည်းများကို ကြည့်ပါ)။
- မှတ်ချက်: Codespaces တွင် တိုက်ရိုက် repo ကို ဖွင့်လိုပါက (clone မလုပ်ဘဲ), Codespaces သည် devcontainer ပတ်ဝန်းကျင် တည်ဆောက်မည်ဖြစ်ပြီး သင်လိုအပ်သည့် ပမာဏထက် ပို provision လုပ်နိုင်သည်။ Codespace အသစ် နှင့် သက်သာ clone လုပ်ခြင်းဖြင့် disk အသုံးပြုမှုကို ပိုမို ထိန်းချုပ်နိုင်သည်။

#### အကြံပြုချက်များ

- ပြင်ဆင်/commit လုပ်လိုပါက clone URL ကို မည်သည့် fork ဖြစ်မဆို အမြဲ ပြောင်းလဲပေးပါ။
- နောက်ပိုင်းတွင် သမိုင်းကြောင်း (history) သို့မဟုတ် ဖိုင်များ ပိုလိုအပ်ပါက fetch လုပ်နိုင်ပြီး sparse-checkout ကို ပြင်ဆင်၍ folder အသစ်ထည့်နိုင်သည်။

## ကုဒ် run ပြုလုပ်ခြင်း

သင်တန်းတွင် AI Agents ဆောက်ရန် လက်တွေ့လုပ်ဆောင် သင်ယူနိုင်ရန် Jupyter Notebooks များပါရှိသည်။

ကုဒ်နမူနာများသည် **Microsoft Agent Framework (MAF)** ကို အသုံးပြုသည်။ `FoundryChatClient` အသုံးပြု၍ **Microsoft Foundry Agent Service V2** (Responses API) ကို **Microsoft Foundry** မှ ချိတ်ဆက်သည်။

Python notebooks အားလုံးကို `*-python-agent-framework.ipynb` ဟူ၍ အမှတ်အသား မိန့်ပြုထားသည်။

## လိုအပ်ချက်များ

- Python 3.12+
  - **မှတ်ချက်**: သင်တွင် Python3.12 မရှိပါက ထည့်သွင်းပါ။ ထို့နောက် python3.12 သုံးလျှင် venv ဖန်တီးပြီး requirements.txt မှမှန်ကန်သောဗားရှင်းများ ထည့်သွင်းမှု အတည်ပြုပါ။
  
    >ဥပမာ

    Python venv directory ဖန်တီးခြင်း:

    ```bash|powershell
    python -m venv venv
    ```

    ထို့နောက် venv ပတ်ဝန်းကျင်ကို လှုပ်လုပ်ရန်:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET သုံးကုဒ်များအတွက် [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) သို့မဟုတ် နောက်ဆက်တွဲ ဗားရှင်းကို ထည့်သွင်းပါ။ ထို့နောက် သင်ထည့်သွင်းထားသော .NET SDK ဗားရှင်းကို တိုင်းတာပါ။

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — အတည်ပြုမှုအတွက် လိုအပ်သည်။ [aka.ms/installazurecli](https://aka.ms/installazurecli) မှ ထည့်သွင်းပါ။
- **Azure Subscription** — Microsoft Foundry နှင့် Microsoft Foundry Agent Service အသုံးပြုရန်။
- **Microsoft Foundry Project** — ဖြန့်ချိထားသော မော်ဒယ် (ဥပမာ `gpt-4.1-mini`) ပါသော project တစ်ခု။ [အဆင့် ၁](#အဆင့်-၁-microsoft-foundry-project-ဖန်တီးခြင်း) ကို ကြည့်ပါ။

Repo၏ root တွင် requirements.txt ဖိုင် ပါဝင်ပြီး ကုဒ်နမူနာများ run ရန် လိုအပ်သော Python package များကို ပါဝင်သည်။

Repo root တွင် terminal ဖြင့် အောက်ပါ command ကို run ပြုလုပ်၍ ထည့်သွင်းနိုင်သည်။

```bash|powershell
pip install -r requirements.txt
```

ဂေဘလူးနှင့် ပြဿနာကင်းရန် Python virtual environment ဖန်တီးဖို့ အကြံပြုသည်။

## VSCode ပြင်ဆင်ခြင်း

VSCode တွင် များသောအားဖြင့် မှန်ကန်သော Python ဗားရှင်းကို အသုံးပြုနေကြောင်း သေချာစေရန်။

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry နှင့် Microsoft Foundry Agent Service ပြင်ဆင်ခြင်း

### အဆင့် ၁: Microsoft Foundry Project ဖန်တီးခြင်း

Notebook များကို run ချရန် Microsoft Foundry **hub** နှင့် မော်ဒယ် ဖြန့်ထားသော **project** တစ်ခု လိုအပ်သည်။

1. [ai.azure.com](https://ai.azure.com) သို့ သွားပါ၊ Azure အကောင့်ဖြင့် အဝင်ဝင်ပါ။
2. **hub** တစ်ခုဖန်တီးပါ (ဟုတ်ရင် ရှိပြီးသား hub ကို အသုံးပြုလို့ရသည်)။ ကြည့်ရန်: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)။
3. hub အတွင်း **project** တစ်ခု ဖန်တီးပါ။
4. **Models + Endpoints** → **Deploy model** မှ မော်ဒယ် (ဥပမာ `gpt-4.1-mini`) တစ်ခု ဖြန့်ချိပါ။

### အဆင့် ၂: မိမိ၏ Project Endpoint နှင့် Model Deployment Name ရယူခြင်း

Microsoft Foundry portal တွင် မိမိ project မှ:

- **Project Endpoint** — **Overview** စာမျက်နှာသို့ သွားကာ endpoint URL ကို ကူးယူပါ။

![Project Connection String](../../../translated_images/my/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** သို့ သွားပြီး မော်ဒယ်ဖြန့်ထားသည့် အမည် (ဥပမာ `gpt-4.1-mini`) ကို မှတ်သားပါ။

### အဆင့် ၃: `az login` ဖြင့် Azure တွင် အဝင်ဝင်ပါ

Notebooks များသည် **`AzureCliCredential`** ကို အသုံးပြုသောကြောင့် API Keys မလိုပါ။ Azure CLI ဖြင့် အဝင်ဝင်ထားရမည်။

1. **Azure CLI ထည့်သွင်းပါ** (မရှိသေးပါက): [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. အောက်ပါ command ဖြင့် **အဝင်ဝင်ပါ**:

    ```bash|powershell
    az login
    ```

    သို့မဟုတ် browser မပါတဲ့ remote/Codespace environment တွင်ရှိပါက:

    ```bash|powershell
    az login --use-device-code
    ```

3. အသေးစိတ် မေးပါက မိမိ၏ Foundry project ပါဝင်သော subscription ကို ရွေးချယ်ပါ။

4. အဝင်ဝင်ပြီးကြောင်း အတည်ပြုပါ:

    ```bash|powershell
    az account show
    ```

> **ဘာကြောင့် `az login`?** Notebooks များသည် `azure-identity` package မှ **`AzureCliCredential`** ဖြင့် အတည်ပြုသည်။ Azure CLI session သည် API key မလိုဘဲ credential ကို ပေးသည်။ ၎င်းသည် [လုံခြုံရေးအကောင်းဆုံး လေ့လာမှု](https://learn.microsoft.com/azure/developer/ai/keyless-connections) ဖြစ်သည်။

### အဆင့် ၄: မိမိ၏ `.env` ဖိုင် ဖန်တီးခြင်း

ဥပမာဖိုင်ကို ကူးယူပါ:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

`.env` ဖိုင်ကို ဖွင့်ပြီး အောက်ပါ တန်ဖိုး နှစ်ခုကို ဖြည့်ပါ:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| Variable | ရှာဖွေရာနေရာ |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → မိမိ project → **Overview** စာမျက်နှာ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → မော်ဒယ် အမည် |

သင်ခန်းစာများ အများစုအတွက် အဟာရပါသည်! Notebooks များသည် မိမိ၏ `az login` session ဖြင့် အလိုအလျောက် အတည်ပြုသည်။

### အဆင့် ၅: Python Dependencies ထည့်သွင်းခြင်း

```bash|powershell
pip install -r requirements.txt
```

ရှေ့က ဖန်တီးထားသော virtual environment အတွင်း run ပြုလုပ်ရန် ညွှန်ကြားပါသည်။

## အပိုဆောင်း ပြင်ဆင်မှု မေးခန်း ၅ (Agentic RAG) အတွက်

Lesson 5 တွင် **Azure AI Search** ကို အသုံးပြုသည့် retrieval-augmented generation တွင် ပါဝင်သည်။ သင်သွား run မည်ဆိုလျှင် အောက်ပါ Variables များကို `.env` ဖိုင်တွင် ထည့်ပါ:

| Variable | ရှာဖွေရာနေရာ |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## Azure OpenAI တိုက်ရိုက် ခေါ်သည့် တခြား သင်ခန်းစာများ (Lessons 6 နှင့် 8)

Lessons 6 နှင့် 8 တချို့ notebooks များသည် Microsoft Foundry project မဖြတ်ဘဲ **Azure OpenAI** ကို တိုက်ရိုက် (Responses API အသုံးပြုပြီး) ခေါ်သည်။ ယခင်တွင် GitHub Models ကိုအသုံးပြုပြီးဖြစ်ပြီး၊ စတင်နှစ်လအတွင်း ပရိတ်သတ်နေသောမှတ်တမ်းဖြစ်ပါသည် (2026 ဇူလိုင်တွင် ပိတ်သိမ်းမည်)၊ Responses API ပံ့ပိုးမှုမရှိပါ။ အဆိုပါ နမူနာများကို run မည်ဆိုလျှင် အောက်ပါ Variables များကို `.env` ဖိုင်တွင် ထည့်သွင်းပါ။

| Variable | ရှာဖွေရာနေရာ |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → **Azure OpenAI** resource → **Keys and Endpoint** → Endpoint (ဥပမာ `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Responses API ကို ပံ့ပိုးသည့် မော်ဒယ် ဖြန့်ချိမှု အမည် (ဥပမာ `gpt-4.1-mini`) |
| `AZURE_OPENAI_API_KEY` | အထွ optional — `az login` / Entra ID ထက် key-based auth သုံးမည့်အခါသာလိုအပ်ပါသည် |

> Responses API သည် စံ `/openai/v1/` endpoint ကို အသုံးပြုသည်၊ ထို့ကြောင့် `api-version` မလိုအပ်ပါ။ az login ဖြင့် keyless Entra ID authentication ကို အသုံးပြုနိုင်သည်။

## လွဲချော် Provider: MiniMax (OpenAI-Compatible)

[MiniMax](https://platform.minimaxi.com/) သည် OpenAI-compatible API နှင့် လက်ခံရရှိ၍ 204K tokens အထိ ရှည်သော context မော်ဒယ်များ ပေးဆောင်ပါသည်။ Microsoft Agent Framework ၏ `OpenAIChatClient` သည် OpenAI-compatible endpoint များအားလုံးနှင့် အလုပ်လုပ်နိုင်သဖြင့် MiniMax ကို Azure OpenAI သို့မဟုတ် OpenAI ၏ အစားထိုး အဖြစ် အသုံးပြုနိုင်သည်။

`.env` ဖိုင်ထဲ ထည့်သွင်းရန် Variables များ:

| Variable | ရှာဖွေရာနေရာ |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` (မူရင်းတန်ဖိုး) |
| `MINIMAX_MODEL_ID` | အသုံးပြုမည့် model အမည် (ဥပမာ `MiniMax-M3`) |

**ဥပမာ မော်ဒယ်များ**: `MiniMax-M3` (အကြံပြု), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (တုံ့ပြန်မှု မြန်ဆန်)။ မော်ဒယ် အမည်များနှင့် ရနိုင်မှုကာလကာတာများက ချိန်ညှိနိုင်ပြီး သင့် အကောင့် (သို့) ဒေသပေါ်မူတည်၍ ရရှိနိုင်သည် — [MiniMax Platform](https://platform.minimaxi.com/) တွင် စစ်ဆေးပါ။ သင်၏အကောင့်တွင် `MiniMax-M3` မရဖြစ်ပါက `MINIMAX_MODEL_ID` သည် သင်ရရှိနိုင်သော model နဲ့ တက်နိုင်ပါ (ဥပမာ `MiniMax-M2.7`)။

`OpenAIChatClient` သုံးသည့် ကုဒ်နမူနာများတွင် (ဥပမာ Lesson 14 ဟိုတယ်ဘွတ်ကင် Workflow) `MINIMAX_API_KEY` သတ်မှတ်ထားပါက မိမိ၏ MiniMax သတ်မှတ်ချက်အတိုင်း အလိုအလျောက် စမ်းသုံးပါလိမ့်မည်။

## လွဲချော် Provider: Foundry Local (Device တွင် မော်ဒယ်များ run ပြုလုပ်ခြင်း)

[Foundry Local](https://foundrylocal.ai) သည် လေးထားသော runtime တစ်ခုဖြစ်၍ သင့်စက်ပေါ်တွင် OpenAI-compatible API ဖြင့် မော်ဒယ်များကို downloadable၊ စီမံခန့်ခွဲခြင်း၊ ရောင်းချခြင်းများ ချီးမြှင့်သည်။ Cloud သုံးရန် မလိုအပ်၊ Azure subscription မလိုအပ်၊ API key မလိုအပ်ပါ။ Offline ဖွံ့ဖြိုးတိုးတက်မှုပြုရန်၊ ကုန်ကျစရိတ်မတိုးစေဖို့၊ ဒေတာကို စက်ပေါ်မှာ ထိန်းသိမ်းရန် သင့်လျော်သည်။

Microsoft Agent Framework ၏ `OpenAIChatClient` သည် OpenAI-compatible မည်သည့် endpoint မဆို အလုပ်လုပ်နိုင်သောကြောင့် Foundry Local သည် Azure OpenAI အစား ထည့်သွင်းသုံးစွဲနိုင်သော local အစီအစဉ်တစ်ခုဖြစ်သည်။

**1. Foundry Local ထည့်သွင်းခြင်း**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. မော်ဒယ် download ပြုလုပ်ပြီး run ပြုလုပ်ခြင်း** (local service ကိုလည်း စတင်ပါလိမ့်မည်):

```bash
foundry model list          # ရနိုင်သော မော်ဒယ်များကို ကြည့်ပါ
foundry model run phi-4-mini
```

**3. local endpoint ရှာဖွေရန် အသုံးပြုမည့် Python SDK ထည့်သွင်းခြင်း:**

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework ကို မိမိ၏ local model ပေါ် သတ်မှတ်ရန်:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# မော်ဒယ်ကို ဒေါင်းလုပ်လုပ်ပြီး (လိုအပ်လျှင်) ဒေသစံပြနေရာတွင် ဆားဗ်လုပ်သည်၊ ထို့နောက် endpoint/port ကို ရှာဖွေသည်။
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # ဥပမာ http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local အတွက် အမြဲ "မလိုအပ်ပါ" ဖြစ်သည်
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **မှတ်ချက်:** Foundry Local သည် OpenAI-compatible **Chat Completions** endpoint ကို ထောက်ပံ့သည်။ ဒါကို local တိုးတက်မှုနှင့် offline အသုံးပြုမှုများအတွက် သုံးနိုင်သည်။ **Responses API** ၏ အပြည့်အဝ လုပ်ဆောင်ချက်များ (stateful စကားစဉ်၊ tool orchestration နက်ရှိုင်းမှုများ၊ agent ပုံစံ ဖွံ့ဖြိုးမှု) စသည်တို့အတွက် **Azure OpenAI** သို့မဟုတ် **Microsoft Foundry** project ကို သင်ခန်းစာများအတိုင်း ကြည့်ရှုပြုရန် ဖြစ်သည်။ [Foundry Local documentation](https://foundrylocal.ai) တွင် လက်ရှိ မော်ဒယ်စာရင်းနှင့် ပလက်ဖောင်း ပံ့ပိုးမှုများ ရှိပါသည်။


## အတန်း ၈ အတွက် ထပ်မံဆက်တင်ခြင်း (Bing Grounding Workflow)

အတန်း ၈ ရဲ့ conditional workflow notebook မှာ Microsoft Foundry မှ Bing grounding ကို အသုံးပြုပါတယ်။ အဲဒီ sample ကို run ဖို့ စိတ်ဝင်စားရင် `.env` ဖိုင်ထဲမှာ ဒီ variable ကို ထည့်သွင်းပါ။

| Variable | ရှာဖွေနိုင်တဲ့နေရာ |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → သင့် project → **Management** → **Connected resources** → သင့် Bing ချိတ်ဆက်မှု → connection ID ကို ကူးရန် |

## ပြဿနာရောက်လျှင်ဖြေရှင်းနည်း

### macOS မှာ SSL Certificate Verification အမှားများ

macOS မှာအောက်ပါ error အမျိုးအစားတက်လာခဲ့ရင်

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

ဒါဟာ macOS ပေါ် Python နဲ့ မျှော်လင့်ထားတဲ့ system SSL certificates ကို ယုံကြည်ခြင်း မ ရရှိတာကြောင့် ဖြစ်တယ်။ အောက်ပါ ဖြေရှင်းနည်းများကို အဆင့်လိုက် စမ်းကြည့်ပါ။

**ရွေးချယ်စရာ ၁: Python ရဲ့ Install Certificates script ကို run ပြုလုပ်ပါ (အကြံပြု)**

```bash
# သင့်ထည့်သွင်းထားသော Python ဗားရှင်း (ဥပမာ၊ 3.12 သို့မဟုတ် 3.13) ဖြင့် 3.XX ကိုထားပါ။
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ရွေးချယ်စရာ ၂: Notebook မှာ `connection_verify=False` ကို အသုံးပြုပါ (GitHub Models notebooks များအတွက်သာ)**

Lesson 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) မှာ comment ထားတဲ့ workaround တစ်ခု ရှိပြီး ဖြစ်ပါတယ်။ client ဖန်တီးချိန်မှာ `connection_verify=False` ကို uncomment လုပ်ပါ။

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # လက်မှတ်အမှားများကြုံတွေ့လျှင် SSL အတည်ပြုချက်ကိုပိတ်ပါ
)
```

> **⚠️ သတိပေးချက်:** SSL verification ကို ပိတ်ခြင်း (`connection_verify=False`) က သက်ဆိုင်ရာ certificate အတည်ပြုခြင်းကို ခုခံပစ်သွားတာဖြစ်ပါသည်။ ဒါကို အချက်အချာ တာဝန်ရှိသော ပရိုဒပ်ရှင်းပတ်ဝန်းကျင်တွင် မသုံးပါနဲ့၊ တံခါးခန်းဖွင့်ခြင်းအနေနဲ့သာ ဒါမှမဟုတ် development ပတ်ဝန်းက်တွင်သာ အသုံးပြုပါ။

**ရွေးချယ်စရာ ၃: `truststore` ကို တပ်ဆင်ပြီး အသုံးပြုပါ**

```bash
pip install truststore
```

အဲ့ဒီနောက် သင့် notebook သို့ script မှာ network call မလုပ်ခင် တစ်ဖက်တွင် အောက်ပါ code ကို ထည့်ပါ။

```python
import truststore
truststore.inject_into_ssl()
```

## ဘယ်နေရာမှာ ရပ်သွားသလဲ?

ဒီ setup ကို run ပြုလုပ်ရာမှာ တခုခုပြဿနာ ရှိရင် ကျွန်ုပ်တို့ရဲ့ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> မှာ ဝင်ရောက် မေးမြန်းပါ သို့မဟုတ် <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">issue တစ်ခုဖန်တီးပါ</a>။

## နောက်တန်းသင်ခန်းစာ

သင့်အနေနဲ့ ယခု သင်တန်းအတွက် code ကို run ပြုလုပ်ရန် အသင့်ဖြစ်ပါပြီ။ AI Agents ရဲ့ ကမ္ဘာကြီးကို ပို၍လေ့လာစရာပျော်ရွှင်ပါစေ!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->