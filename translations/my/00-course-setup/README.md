# သင်တန်း ပြင်ဆင်ခြင်း

## နိဒါန်း

ဤသင်ခန်းစာတွင် သင်တန်း၏ ကုဒ်နမူနာများကို မည်သို့ လုပ်ဆောင်ရမည်ကို ဖော်ပြပါမည်။

## အခြား လေ့လာသူများနှင့် ဆက်သွယ်၍ ကူညီမှု ရယူရန်

သင်၏ repo ကို clone မလုပ်မီ [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) သို့ ဆက်သွယ်ပါ၊ စတင်ပြင်ဆင်မှု၊ သင်ခန်းစာဆိုင်ရာ မေးခွန်းများ သို့မဟုတ် အခြား လေ့လာသူများနှင့် ချိတ်ဆက်ရန် ကူညီပေးမည်ဖြစ်သည်။

## ဤ Repo ကို Clone သို့မဟုတ် Fork ပြုလုပ်ရန်

စတင်ရန်၊ ကျေးဇူးပြု၍ GitHub Repository ကို clone သို့မဟုတ် fork လုပ်ပါ။ ၎င်းသည် သင့်ကိုယ်ပိုင် သင်ခန်းစာ အကြောင်းအရာများ ဗားရှင်းကို ဖန်တီးပေးမည်ဖြစ်ပြီး သင်သည် ကုဒ်ကို ပြေး၊ စမ်းသပ်၊ ပြင်ဆင်နိုင်မည်ဖြစ်သည်။

ဤကို <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a> ကို နှိပ်ခြင်းဖြင့် ပြုလုပ်နိုင်သည်။

သင်တွင် ယခုအချိန်တွင် သင်၏ forked ဗားရှင်းကို အောက်ပါလင့့်တွင် ရရှိထားပါပြီ။

![Fork လုပ်ထားသော repository](../../../translated_images/my/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (workshop / Codespaces အတွက် ထိုက်တန်သလို)

  > အပြည့်အစုံသော repository သမိုင်းကြောင်းနှင့် ဖိုင်အားလုံးကို ဒေါင်းလုပ်လုပ်ပါက အရွယ်အစားကြီးနိုင်သည် (~3 GB)။ သင်သည် workshop တက်ရောက်ထက်သာမက သတ်မှတ်သင်ခန်းစာ ဖိုလ်ဒါအနည်းငယ်သာ လိုအပ်ပါက၊ shallow clone (သို့) sparse clone သည် သမိုင်းကြောင်းကို ကန့်သတ်၍ သို့မဟုတ် blobs များကို ကျော်လွှား၍ ဒေါင်းလုပ်အများစုကိုလျော့ချပေးနိုင်သည်။

#### Quick shallow clone — အနည်းဆုံး သမိုင်းကြောင်း၊ ဖိုင်အားလုံး

အောက်ပါ command များတွင် `<your-username>`ကို သင့် fork URL (သို့) upstream URL ဖြင့် ပြောင်းပါ။

နောက်ဆုံး commit သမိုင်းကြောင်းကို မှတ်သား၍ clone လုပ်ရန် (ဒေါင်းလုပ် သေးငယ်သည်)။

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

တိကျသော branch ကို clone လုပ်ရန်။

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### အပို (sparse) clone — အနည်းငယ်သော blobs + ရွေးချယ်ထားသော ဖိုလ်ဒါများတင်သာ

ဤသည်မှာ partial clone နှင့် sparse-checkout ကို အသုံးပြုသည် (Git 2.25+ လိုအပ်ပြီး partial clone ကို ထောက်ပံ့သော တိုးတက်သော Git ကို အကြံပြုသည်)။

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

repo ဖိုလ်ဒါထဲသို့ ဝင်ရောက်သွားပါ။

```bash|powershell
cd ai-agents-for-beginners
```

ထို့နောက် သင်လိုချင်သော ဖိုလ်ဒါများကို သတ်မှတ်ပါ (ဥပမာ အောက်တွင် ဖိုလ်ဒါနှစ်ခုကို ပြထားသည်)။

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

clone ပြီး ဖိုင်များကို စစ်ဆေးပြီးနောက်၊ သင်သက်ဆိုင်သော ဖိုင်များသာလိုအပ်ပြီးနေရာသိမ်းချင်ပါက (git သမိုင်းမလိုချင်လျှင်) repository metadata ကို ဖျက်ပစ်ပါ (💀ပြန်လည်မရအောင် — Git လုပ်ဆောင်ချက်များအားလုံး ပျောက်ဆုံးမည်: commit များ၊ pull များ၊ push များ သို့မဟုတ် သမိုင်းကြောင်း ဝင်ရောက်စစ်ဆေးခြင်း မရှိသေး)။

```bash
# zsh/bash
rm -rf .git
```

```powershell
# ပါဝါရှဲလ်
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ကို အသုံးပြုခြင်း (လက်လိပ်ဒေါင်းလုပ်များကို ရှောင်ကြဉ်ရန် အကြံပြု)

- ဤ repo အတွက် အသစ်သော Codespace တစ်ခုကို [GitHub UI](https://github.com/codespaces) မှ ဖန်တီးပါ။  

- အသစ်ဖန်တီးထားသည့် codespace ၏ terminal တွင် အထက်ပါ shallow/sparse clone command များထဲမှ တစ်ခုကို 실행၍ သင်လိုအပ်သော သင်ခန်းစာ ဖိုလ်ဒါများကို Codespace workspace သို့သာယူပါ။
- ရွေးစရာ: Codespaces ထဲတွင် clone ပြီးနောက် .git ကို ဖယ်ရှား၍ အပိုနေရာ ပြန်လည်ရယူနိုင်သည် (အထက်ပါ ဖျက်ရန် command များကို ကြည့်ပါ)။
- မှတ်ချက်: repo ကို Codespaces တွင်တိုက်ရိုက် ဖွင့်လိုပါက (clone မလုပ်ဘဲ) Codespaces သည် devcontainer ပတ်ဝန်းကျင်ကို ဖန်တီးပေးမည်ဖြစ်ပြီး သင့်လိုအပ်ချက်ထက် ပိုမိုဖြစ်နိုင်ပါသည်။ အသစ်ဖန်တီးထားသော Codespace အတွင်း တွင် shallow copy ကို clone လုပ်ခြင်းသည် disk အသုံးပြုမှုကို ပိုမိုထိန်းချုပ်နိုင်စေသည်။

#### အကြံပြုချက်များ

- ပြင်ဆင်/commit ပြုလုပ်လိုပါက အမြဲတမ်း clone URL ကို သင့် fork ဖြင့် သတိပြု၍ အစားထိုးပါ။
- နောက်ပိုင်း သမိုင်းကြောင်း သို့မဟုတ် ဖိုင်များပိုမိုလိုအပ်လာပါက၊ fetch လုပ်၍ sparse-checkout ကို ပြန်လည်ပြင်ဆင်ကာ အပိုဖိုလ်ဒါများ ထည့်နိုင်ပါသည်။

## ကုဒ်များ ပြေးဆော့ခြင်း

ဤသင်တန်းတွင် သင့်အား လက်တွေ့လုပ်ဆောင်နိုင်ရန် Jupyter Notebooks အစုစည်းကို ပံ့ပိုးပေးသည်။

ကုဒ်နမူနာများသည် **Microsoft Agent Framework (MAF)** ကို `AzureAIProjectAgentProvider` နှင့် အသုံးပြုသည်၊ ၎င်းသည် **Microsoft Foundry** မှတဆင့် **Azure AI Agent Service V2** (Responses API) သို့ ချိတ်ဆက်သည်။

Python notebooks အားလုံးကို `*-python-agent-framework.ipynb` ဟု အမည်ပေးထားသည်။

## တိုက်တောင်းချက်များ

- Python 3.12+
  - **မှတ်ချက်**: သင်တွင် Python3.12 မရှိပါက၊ ထည့်သွင်းပါ။ ထို့နောက် venv ကို python3.12 ဖြင့် ဖန်တီးပြီး requirements.txt ဖိုင်ကနေ လိုအပ်သော ဗားရှင်းများကို ထည့်သွင်းထားရန် သေချာစေပါ။
  
    > ဥပမာ

    Python venv directory ကို ဖန်တီးပါ။

    ```bash|powershell
    python -m venv venv
    ```

    ထို့နောက် venv ပတ်ဝန်းကျင်ကို အောက်ပါအတိုင်း ဖွင့်ပါ။

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET ကို အသုံးပြုသော နမူနာကုဒ်များအတွက် [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) သို့မဟုတ် နောက်ထပ်ဗားရှင်းကို ထည့်သွင်းထားရန် သေချာပါစေ။ ထို့နောက် သင်ထည့်သွင်းထားသည့် .NET SDK ဗားရှင်းကို စစ်ဆေးပါ။

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — authentication အတွက် လိုအပ်သည်။ [aka.ms/installazurecli](https://aka.ms/installazurecli) မှ ထည့်သွင်းပါ။
- **Azure Subscription** — Microsoft Foundry နှင့် Azure AI Agent Service အသုံးပြုရန် လိုအပ်သည်။
- **Microsoft Foundry Project** — တစ်ခုခု deploy ထားသော model (ဥပမာ၊ `gpt-4o`) ပါဝင်သော project တစ်ခု။ အောက်တွင် [Step 1](../../../00-course-setup) ကို ကြည့်ပါ။

ဤ repository ၏ root တွင် `requirements.txt` ဖိုင်ကို ထည့်သွင်းထားပြီး ကုဒ်နမူနာများကို chạy ရန် အလိုရှိသော Python package များအားလုံးပါရှိသည်။

သင်သည် repository root တွင် terminal မှ အောက်ပါ command ကို 실행၍ ၎င်းတို့ကို ထည့်သွင်းနိုင်သည်။

```bash|powershell
pip install -r requirements.txt
```

ကြာရှည်ဆုံး အရေးပေါ် အပြန်အလှန်တုံ့ပြန်မှုများနှင့် ကိစ္စများ ပျက်ကွက်ခြင်းကို တားဆီးရန် Python virtual environment တစ်ခု ဖန်တီးရန် အကြံပြုပါသည်။

## VSCode ကို စီစဉ်ခြင်း

VSCode တွင် သင် အသုံးပြုနေသည့် Python ဗားရှင်းမှန်ကန်မှုရှိကြောင်း သေချာစေပါ။

![ပုံ](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry နှင့် Azure AI Agent Service ကို သတ်မှတ်ရန်

### အဆင့် 1: Microsoft Foundry Project တစ်ခု ဖန်တီးရန်

Notebook များကို chạy ရန် Microsoft Foundry တွင် **hub** နှင့် **project** တစ်ခု ဖြစ်ပြီး deploy ထားသော model တစ်ခု လိုအပ်ပါသည်။

1. [ai.azure.com](https://ai.azure.com) သို့ သွားပြီး သင့် Azure အကောင့်ဖြင့် Sign in ဝင်ပါ။
2. **hub** တစ်ခု ဖန်တီးပါ (သို့မဟုတ် ရှိပြီးသားကို အသုံးပြုပါ)။ ကြည့်ရန်: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)။
3. hub အတွင်းတွင် **project** တစ်ခု ဖန်တီးပါ။
4. **Models + Endpoints** → **Deploy model** မှတဆင့် model တစ်ခု (ဥပမာ `gpt-4o`) ကို deploy လုပ်ပါ။

### အဆင့် 2: သင်၏ Project Endpoint နှင့် Model Deployment Name ကို ရယူခြင်း

Microsoft Foundry portal တွင် သင်၏ project မှ:

- **Project Endpoint** — **Overview** စာမျက်နှာသို့ သွား၍ endpoint URL ကို ကော်ပီလုပ်ပါ။

![Project Connection String](../../../translated_images/my/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** သို့ သွားပြီး သင် deploy ထားသော model ကို ရွေးချယ်ကာ **Deployment name** ကို မှတ်သားပါ (ဥပမာ၊ `gpt-4o`)။

### အဆင့် 3: `az login` ဖြင့် Azure သို့ sign in ဝင်ရန်

Notebook များတွင် authentication အတွက် **`AzureCliCredential`** ကို အသုံးပြုသည် — API key မလိုအပ်ပါ။ ၎င်းသည် Azure CLI မှ sign in လုပ်ထားရန် တောင်းဆိုပါသည်။

1. သင် မထည့်သွင်းထားသေးပါက **Azure CLI** ကို ထည့်သွင်းပါ: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Sign in** ပြုလုပ်ရန် အောက်ပါ command ကို 실행ပါ။

    ```bash|powershell
    az login
    ```

    သို့မဟုတ် browser မရှိသည့် remote/Codespace ပတ်ဝန်းကျင်တွင် ဖြစ်ပါက:

    ```bash|powershell
    az login --use-device-code
    ```

3. တောင်းဆိုပါက **သင်၏ subscription** ကို ရွေးချယ်ပါ — သင့် Foundry project ပါဝင်သော subscription ကို ရွေးချယ်ပါ။

4. **Sign in ဖြစ်ကြောင်း အတည်ပြုရန်**:

    ```bash|powershell
    az account show
    ```

> **ဘာကြောင့် `az login` လုပ်သနည်း?** Notebooks များသည် `azure-identity` package မှ `AzureCliCredential` ကို အသုံးပြု၍ authenticate လုပ်သည်။ ၎င်းသည် သင့် Azure CLI session သည် credentials များကို ပံ့ပိုးပေးမည်ကို ဆိုလိုသည် — `.env` ဖိုင်ထဲတွင် API key မဟုတ်သော လျှို့ဝှက်အချက်အလက် မလိုအပ်ပါ။ ၎င်းသည် [security best practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections) ဖြစ်သည်။

### အဆင့် 4: သင့် `.env` ဖိုင်ကို ဖန်တီးပါ

ဥပမာဖိုင်ကို ကော်ပီလုပ်ပါ:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# ပါဝါရှဲလ်
Copy-Item .env.example .env
```

`.env` ဖိုင်ကို ဖွင့်ပြီး အောက်ပါတန်ဖိုး နှစ်ခုကို ဖြည့်စွက်ပါ:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | ဘယ်နေရာမှာ တွေ့ရမည် |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → သင့် project → **Overview** စာမျက်နှာ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → သင့် deploy ထားသော model ၏ name |

အများသင်ခန်းစာအတွက် အဲဒါပဲ ရပါပြီ! Notebooks များသည် သင့် `az login` session မှတဆင့် အလိုအလျောက် authenticate လုပ်ပါလိမ့်မည်။

### အဆင့် 5: Python Dependencies ထည့်သွင်းခြင်း

```bash|powershell
pip install -r requirements.txt
```

ဤကို အကြံပြုသည်မှာ မိမိ ဖန်တီးထားသည့် virtual environment အတွင်းတွင် 실행ရန် ဖြစ်သည်။

## အပိုဆောင်း စီစဉ်မှု - Lesson 5 (Agentic RAG)

Lesson 5 သည် retrieval-augmented generation အတွက် **Azure AI Search** ကို အသုံးပြုသည်။ ထို lesson ကို chạy ရန် ရည်ရွယ်ပါက `.env` ဖိုင်ထဲတွင် အောက်ပါ အပြောင်းအလဲများကို ထည့်ပါ။

| Variable | ဘယ်နေရာမှာ တွေ့ရမည် |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → သင့် **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → သင့် **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## အပိုဆောင်း စီစဉ်မှု - Lesson 6 နှင့် Lesson 8 (GitHub Models)

Lesson 6 နှင့် 8 မှာတချို့ Notebook များသည် Azure AI Foundry အစား **GitHub Models** ကို အသုံးပြုသည်။ ၎င်းနမူနာများကို chạy ရန် ရည်ရွယ်ပါက `.env` ဖိုင်ထဲတွင် အောက်ပါ တန်ဖိုးများကို ထည့်ပါ။

| Variable | ဘယ်နေရာမှာ တွေ့ရမည် |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | အသုံးပြုမည့် model အမည် (ဥပမာ `gpt-4o-mini`) |

## အပိုဆောင်း စီစဉ်မှု - Lesson 8 (Bing Grounding Workflow)

Lesson 8 အတွင်းရှိ conditional workflow notebook သည် Azure AI Foundry မှတဆင့် **Bing grounding** ကို အသုံးပြုသည်။ ထိုနမူနာကို chạy ရန် ရည်ရွယ်ပါက `.env` ဖိုင်ထဲတွင် ဤ variable ကို ထည့်ပါ။

| Variable | ဘယ်နေရာမှာ တွေ့ရမည် |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → သင့် project → **Management** → **Connected resources** → သင့် Bing connection → connection ID ကို ကော်ပီလုပ်ပါ |

## ပြဿနာဖြေရှင်းခြင်း

### macOS တွင် SSL Certificate စစ်ဆေးမှု အမှားများ

macOS တွင် အောက်ပါကဲ့သို့ အမှားတစ်ခုရပါက:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

ဤသည်မှာ macOS အတွက် Python တွင် system SSL certificates များကို အလိုအလျောက် ယုံကြည်မှုမရရှိသော ပြဿနာ တစ်ခုဖြစ်သည်။ အောက်ပါ ဖြေရှင်းချက်များကို အဆင့်လိုက် အသုံးပြုကြည့်ပါ။

**ရွေးစရာ 1: Python ၏ Install Certificates script ကို 실행ပါ (အကြံပြု)**

```bash
# 3.XX ကို သင်တပ်ဆင်ထားသော Python ဗားရှင်းနံပါတ် (ဥပမာ 3.12 သို့ 3.13) ဖြင့် အစားထိုးပါ:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**ရွေးစရာ 2: Notebook အတွင်း `connection_verify=False` ကို အသုံးပြုပါ (GitHub Models notebooks အတွက်သာ)**

Lesson 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) တွင် မှာcomment ထားသော workaround တစ်ခု ပါရှိသည်။ client ဖန်တီးစဉ်တွင် `connection_verify=False` ကို uncomment ပြီး အသုံးပြုပါ။

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # လက်မှတ်အမှားတွေ့ရင် SSL စစ်ဆေးမှုကို ပိတ်ပါ
)
```

> **⚠️ သတိပြုရန်:** SSL verification ကို ပိတ်သိမ်းခြင်း (`connection_verify=False`) သည် certificate အတည်ပြုမှုကို ရှောင်လွှဲသဖြင့် လုံခြုံရေးကို လျော့ပါးစေသည်။ ၎င်းကို development ပတ်ဝန်းကျင်တွင်သာ ယာယီ လျော့ချရန်အသုံးပြုပါ၊ production တွင် မသုံးသင့်ပါ။

**ရွေးစရာ 3: `truststore` ကို ထည့်သွင်း၍ အသုံးပြုပါ**

```bash
pip install truststore
```

ထို့နောက် မည်သည့် network ခေါ်ဆိုမှု မပြုမီ သင်၏ notebook သို့မဟုတ် script ၏ အပေါ်တွင် အောက်ပါကို ထည့်ပါ။

```python
import truststore
truststore.inject_into_ssl()
```

## ဘာမှမဖြစ်နေရဆဲလား?

ဤ setup ကို 실행ရာတွင် ပြဿနာမဖြေရှင်းနိုင်ပါက ကျွန်ုပ်တို့၏ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> သို့ ဝင်ပါ သို့မဟုတ် <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">issue တစ်ခု ဖန်တီးပါ</a>။

## နောက်ထပ် သင်ခန်းစာ

ယခုအချိန်တွင် သင်သည် သင်ခန်းစာ၏ ကုဒ်များကို chạy ရန် အသင့်ဖြစ်နေပါပြီ။ AI Agents ကမ္ဘာအကြောင်း ပိုမိုလေ့လာရန် ဝမ်းမြောက်ပါစေ!

[AI Agents မိတ်ဆက်နှင့် Agent အသုံးချမှုများကို မိတ်ဆက်ခြင်း](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ရှင်းလင်းချက်:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု Co‑op Translator (https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်ရေးအတွက် ကြိုးပမ်းသော်လည်း အလိုအလျောက် ဘာသာပြန်ချက်များတွင် အမှားများ သို့မဟုတ် မှန်ကန်မှုနည်းပါးမှုများ ပါဝင်နိုင်ကြောင်း သတိပြုရန် လိုအပ်ပါသည်။ မူရင်းစာရွက်စာတမ်းကို မိခင်ဘာသာစကားဖြင့် ရှိသည့်အတိုင်း အတည်ပြုထားသည့် ကိုးကားအရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူ့ဘာသာပြန် ဝန်ဆောင်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် နားမလည်မှုများ သို့မဟုတ် မှားယွင်းဖော်ပြမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->