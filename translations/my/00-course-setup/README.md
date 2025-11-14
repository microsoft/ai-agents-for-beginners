<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86273689a010b5efecaf7fa23104e0fb",
  "translation_date": "2025-11-07T08:51:04+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "my"
}
-->
# သင်ခန်းစာ စတင်ခြင်း

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာမှာ ဒီသင်တန်းရဲ့ ကုဒ်နမူနာတွေကို ဘယ်လို run လုပ်ရမလဲဆိုတာကို လေ့လာပါမယ်။

## အခြားလေ့လာသူတွေနဲ့ ပူးပေါင်းပြီး အကူအညီရယူပါ

သင့်ရဲ့ repo ကို clone လုပ်ဖို့မစတင်ခင် [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) ကို join လုပ်ပါ။ ဒီမှာ setup အတွက် အကူအညီရယူနိုင်ပြီး သင်တန်းနဲ့ပတ်သက်တဲ့ မေးခွန်းတွေကို မေးနိုင်သလို အခြားလေ့လာသူတွေနဲ့ ဆက်သွယ်နိုင်ပါတယ်။

## ဒီ Repo ကို Clone လုပ်ပါ သို့မဟုတ် Fork လုပ်ပါ

စတင်ဖို့အတွက် GitHub Repository ကို clone လုပ်ပါ သို့မဟုတ် fork လုပ်ပါ။ ဒါက သင့်ကိုယ်ပိုင် သင်တန်းစာရင်းကို ရရှိစေပြီး ကုဒ်တွေကို run, test, tweak လုပ်နိုင်ပါမယ်။

ဒီအရာကို <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a> လင့်ခ်ကို နှိပ်ပြီးလုပ်ဆောင်နိုင်ပါတယ်။

အခု သင့်မှာ ဒီသင်တန်းရဲ့ fork လုပ်ထားတဲ့ ကိုယ်ပိုင် version ရှိပါပြီ။

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.my.png)

### Shallow Clone (workshop / Codespaces အတွက် အကြံပြုထားသည်)

  >အပြည့်အစုံ repository ကို download လုပ်တဲ့အခါ (~3 GB) အတော်လေးကြီးမားနိုင်ပါတယ်။ workshop တက်ရောက်ဖို့ သို့မဟုတ် lesson folder အနည်းငယ်သာလိုအပ်တဲ့အခါ Shallow clone (သို့မဟုတ် sparse clone) က history အများစုကို truncate လုပ်ပြီး download ကိုလျှော့ချနိုင်ပါတယ်။

#### Quick shallow clone — minimal history, all files

အောက်မှာပါတဲ့ command တွေမှာ `<your-username>` ကို သင့် fork URL (သို့မဟုတ် upstream URL) နဲ့ အစားထိုးပါ။

နောက်ဆုံး commit history ကိုသာ clone လုပ်ဖို့ (download အနည်းငယ်):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

တစ်ခုချင်း branch ကို clone လုပ်ဖို့:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimal blobs + only selected folders

ဒီမှာ partial clone နဲ့ sparse-checkout ကို အသုံးပြုပါတယ် (Git 2.25+ လိုအပ်ပြီး partial clone support ရှိတဲ့ modern Git ကို အကြံပြုထားပါတယ်):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

repo folder ထဲကို ဝင်ပါ:

```bash|powershell
cd ai-agents-for-beginners
```

ပြီးရင် သင်လိုအပ်တဲ့ folder တွေကို သတ်မှတ်ပါ (အောက်မှာ ဥပမာအနေနဲ့ folder နှစ်ခုကို ပြထားပါတယ်):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

clone လုပ်ပြီး file တွေကို verify လုပ်ပြီးရင် file တွေသာလိုအပ်ပြီး အာကာသကို လွတ်လပ်စေချင်ရင် (git history မပါ) repository metadata ကို delete လုပ်ပါ (💀မပြန်ပြင်နိုင် — Git functionality အားလုံးကိုဆုံးရှုံးပါမယ်: commits, pulls, pushes, သို့မဟုတ် history access မရနိုင်ပါ):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ကို အသုံးပြုခြင်း (local large downloads ကိုရှောင်ရှားဖို့ အကြံပြုထားသည်)

- GitHub UI မှာ [Codespace အသစ်](https://github.com/codespaces) တစ်ခုကို ဒီ repo အတွက် ဖန်တီးပါ။  

- အသစ်ဖန်တီးထားတဲ့ codespace ရဲ့ terminal မှာ shallow/sparse clone command တစ်ခုကို run လုပ်ပြီး Codespace workspace ထဲ lesson folder တွေကိုသာယူပါ။
- အလိုအလျောက်: Codespaces ထဲမှာ clone လုပ်ပြီးနောက် .git ကို ဖျက်ပြီး အပိုအာကာသကို reclaim လုပ်ပါ (အပေါ်မှာဖော်ပြထားတဲ့ ဖျက်ခြင်း command တွေကို ကြည့်ပါ)။
- မှတ်ချက်: Codespaces ထဲမှာ repo ကို တိုက်ရိုက်ဖွင့်ချင်ရင် (အပို clone မရှိဘဲ) Codespaces က devcontainer environment ကို တည်ဆောက်ပြီး သင့်လိုအပ်ချက်ထက်ပို provision လုပ်နိုင်ပါတယ်။ အသစ်စ Codespace ထဲမှာ shallow copy ကို clone လုပ်ခြင်းက disk usage ကိုပိုထိန်းချုပ်နိုင်စေပါတယ်။

#### အကြံပြုချက်များ

- edit/commit လုပ်ချင်ရင် clone URL ကို သင့် fork နဲ့ အစားထိုးပါ။
- နောက်ပိုင်းမှာ history သို့မဟုတ် file တွေ ပိုလိုအပ်လာရင် fetch လုပ်နိုင်သလို sparse-checkout ကို ပြင်ပြီး folder တွေ ပိုထည့်နိုင်ပါတယ်။

## ကုဒ်ကို Run လုပ်ခြင်း

ဒီသင်တန်းမှာ AI Agents တည်ဆောက်ဖို့ Jupyter Notebooks တွေကို run လုပ်ပြီး လက်တွေ့ကျကျ လေ့လာနိုင်ပါတယ်။

ကုဒ်နမူနာတွေမှာ အောက်ပါအရာတွေကို အသုံးပြုထားပါတယ်:

**GitHub Account လိုအပ်သည် - အခမဲ့**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. (semantic-kernel.ipynb) အဖြစ် label လုပ်ထားသည်။
2) AutoGen Framework + GitHub Models Marketplace. (autogen.ipynb) အဖြစ် label လုပ်ထားသည်။

**Azure Subscription လိုအပ်သည်**:
3) Azure AI Foundry + Azure AI Agent Service. (azureaiagent.ipynb) အဖြစ် label လုပ်ထားသည်။

အထက်ပါနမူနာ ၃ မျိုးကို စမ်းသုံးဖို့ အကြံပြုပါတယ်။ သင့်အတွက် အကောင်းဆုံးအလုပ်လုပ်မယ့်နည်းကို ရှာဖွေပါ။

သင်ရွေးချယ်တဲ့နည်းက အောက်မှာဖော်ပြထားတဲ့ setup အဆင့်တွေကို သတ်မှတ်ပေးပါမယ်:

## လိုအပ်ချက်များ

- Python 3.12+
  - **NOTE**: Python3.12 မရှိရင် install လုပ်ပါ။ requirements.txt file မှာပါတဲ့ version တွေကို install လုပ်ဖို့ python3.12 ကို အသုံးပြုပြီး venv တစ်ခုဖန်တီးပါ။
  
    >ဥပမာ

    Python venv directory ဖန်တီးပါ:

    ```bash|powershell
    python -m venv venv
    ```

    venv environment ကို activate လုပ်ပါ:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET ကို အသုံးပြုတဲ့ sample code တွေအတွက် [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) သို့မဟုတ် နောက်ဆုံး version ကို install လုပ်ပါ။ ပြီးရင် install လုပ်ထားတဲ့ .NET SDK version ကို စစ်ဆေးပါ:

    ```bash|powershell
    dotnet --list-sdks
    ```

- GitHub Account - GitHub Models Marketplace ကို အသုံးပြုဖို့
- Azure Subscription - Azure AI Foundry ကို အသုံးပြုဖို့
- Azure AI Foundry Account - Azure AI Agent Service ကို အသုံးပြုဖို့

ဒီ repository ရဲ့ root မှာ `requirements.txt` file ကို ထည့်ထားပြီး Python package တွေကို install လုပ်ဖို့လိုအပ်ပါတယ်။

terminal မှာ root repository မှာ အောက်ပါ command ကို run လုပ်ပြီး install လုပ်နိုင်ပါတယ်:

```bash|powershell
pip install -r requirements.txt
```

Python virtual environment တစ်ခုဖန်တီးဖို့ အကြံပြုပါတယ်။ conflicts နဲ့ ပြဿနာတွေကို ရှောင်ရှားနိုင်ပါတယ်။

## VSCode Setup

VSCode မှာ Python ရဲ့ version မှန်ကန်မှုကို သေချာစေပါ။

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Models ကို အသုံးပြုတဲ့ နမူနာများအတွက် Set Up

### အဆင့် ၁: GitHub Personal Access Token (PAT) ကို ရယူပါ

ဒီသင်တန်းမှာ GitHub Models Marketplace ကို အသုံးပြုထားပြီး သင် AI Agents တည်ဆောက်ဖို့ အသုံးပြုမယ့် Large Language Models (LLMs) တွေကို အခမဲ့ access ရရှိစေပါတယ်။

GitHub Models ကို အသုံးပြုဖို့ [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) တစ်ခုကို ဖန်တီးဖို့လိုအပ်ပါတယ်။

GitHub Account ရဲ့ <a href="https://github.com/settings/personal-access-tokens" target="_blank">Personal Access Tokens settings</a> ကို သွားပြီးလုပ်ဆောင်နိုင်ပါတယ်။

Token ဖန်တီးတဲ့အခါ [Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) ကို လိုက်နာပါ။ ဒါက token ကို ဒီသင်တန်းရဲ့ code samples တွေ run လုပ်ဖို့လိုအပ်တဲ့ permission တွေကိုသာပေးဖို့ဆိုလိုပါတယ်။

1. **Developer settings** မှာ ဘယ်ဘက်ဘက်က `Fine-grained tokens` option ကို ရွေးပါ။

   ![Developer settings](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.my.png)

   ပြီးရင် `Generate new token` ကို ရွေးပါ။

   ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.my.png)

2. Token ရဲ့ ရည်ရွယ်ချက်ကို ဖော်ပြတဲ့ အမည်တစ်ခုကို ထည့်ပါ။ နောက်ပိုင်းမှာ အလွယ်တကူသိနိုင်အောင် ဖြစ်ပါတယ်။

    🔐 Token Duration အကြံပြုချက်

    အကြံပြုထားတဲ့ သက်တမ်း: 30 ရက်
    ပိုမိုလုံခြုံမှုအတွက် သက်တမ်းကို ပိုမိုတိုတောင်းစေဖို့ — ဥပမာ 7 ရက် 🛡️
    သင့်ရဲ့ သင်ယူမှု momentum ကို မြှင့်တင်ထားတဲ့အချိန်မှာ သင်တန်းကို ပြီးမြောက်စေဖို့ အကောင်းဆုံးနည်းလမ်း 🚀။

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.my.png)

3. Token ရဲ့ scope ကို ဒီ repository ရဲ့ fork မှာသာ ကန့်သတ်ပါ။

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.my.png)

4. Token ရဲ့ permissions ကို ကန့်သတ်ပါ: **Permissions** အောက်မှာ **Account** tab ကို click လုပ်ပြီး "+ Add permissions" button ကို click လုပ်ပါ။ Dropdown တစ်ခုပေါ်လာပါမယ်။ **Models** ကို ရှာပြီး box ကို check လုပ်ပါ။

    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.my.png)

5. Token ဖန်တီးမယ့်အခါ လိုအပ်တဲ့ permissions တွေကို verify လုပ်ပါ။ ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.my.png)

6. Token ဖန်တီးမယ့်အခါ သင့် token ကို password manager vault လို secure နေရာမှာ သိမ်းထားဖို့ ပြင်ဆင်ထားပါ။ Token ကို ဖန်တီးပြီးနောက်မှာ ပြန်ပြမယ့်အခါ မရှိပါဘူး။ ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.my.png)

သင်ဖန်တီးထားတဲ့ token ကို copy လုပ်ပါ။ အခု သင့် `.env` file ထဲမှာ ဒီ token ကို ထည့်သွင်းပါမယ်။

### အဆင့် ၂: `.env` File ကို ဖန်တီးပါ

`.env` file ကို ဖန်တီးဖို့ terminal မှာ အောက်ပါ command ကို run လုပ်ပါ။

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

ဒီဟာက example file ကို copy လုပ်ပြီး `.env` ကို directory ထဲမှာ ဖန်တီးပါမယ်။ အဲဒီမှာ environment variables အတွက် value တွေကို ဖြည့်ပါ။

Token ကို copy လုပ်ပြီး `.env` file ကို သင့်အကြိုက်ဆုံး text editor မှာ ဖွင့်ပြီး `GITHUB_TOKEN` field ထဲမှာ paste လုပ်ပါ။

![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.my.png)

အခု သင့်မှာ ဒီသင်တန်းရဲ့ code samples တွေကို run လုပ်နိုင်ပါပြီ။

## Azure AI Foundry နဲ့ Azure AI Agent Service ကို အသုံးပြုတဲ့ နမူနာများအတွက် Set Up

### အဆင့် ၁: Azure Project Endpoint ကို ရယူပါ

Azure AI Foundry မှာ hub နဲ့ project တစ်ခုဖန်တီးဖို့ အဆင့်တွေကို [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources) မှာ ရှာဖွေပါ။

Project တစ်ခုဖန်တီးပြီးနောက် project ရဲ့ connection string ကို ရယူဖို့လိုအပ်ပါတယ်။

ဒီဟာကို Azure AI Foundry portal ရဲ့ **Overview** စာမျက်နှာမှာ သွားပြီးလုပ်ဆောင်နိုင်ပါတယ်။

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.my.png)

### အဆင့် ၂: `.env` File ကို ဖန်တီးပါ

`.env` file ကို ဖန်တီးဖို့ terminal မှာ အောက်ပါ command ကို run လုပ်ပါ။

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

ဒီဟာက example file ကို copy လုပ်ပြီး `.env` ကို directory ထဲမှာ ဖန်တီးပါမယ်။ အဲဒီမှာ environment variables အတွက် value တွေကို ဖြည့်ပါ။

Token ကို copy လုပ်ပြီး `.env` file ကို သင့်အကြိုက်ဆုံး text editor မှာ ဖွင့်ပြီး `PROJECT_ENDPOINT` field ထဲမှာ paste လုပ်ပါ။

### အဆင့် ၃: Azure ကို Sign in လုပ်ပါ

လုံခြုံရေးအတွက် အကောင်းဆုံးနည်းလမ်းအနေနဲ့ Microsoft Entra ID နဲ့ [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) ကို အသုံးပြုပါ။

နောက်ဆုံးမှာ terminal ကို ဖွင့်ပြီး `az login --use-device-code` ကို run လုပ်ပြီး သင့် Azure account ကို sign in လုပ်ပါ။

Sign in လုပ်ပြီးနောက် terminal မှာ subscription ကို ရွေးပါ။

## အပို Environment Variables - Azure Search နဲ့ Azure OpenAI 

Agentic RAG Lesson - Lesson 5 - မှာ Azure Search နဲ့ Azure OpenAI ကို အသုံးပြုတဲ့ နမူနာတွေပါဝင်ပါတယ်။

ဒီနမူနာတွေကို run လုပ်ချင်ရင် `.env` file ထဲမှာ အောက်ပါ environment variables တွေကို ထည့်သွင်းဖို့လိုအပ်ပါတယ်:

### Overview Page (Project)

- `AZURE_SUBSCRIPTION_ID` - **Overview** စာမျက်နှာရဲ့ **Project details** မှာ စစ်ဆေးပါ။

- `AZURE_AI_PROJECT_NAME` - **Overview** စာမျက်နှာရဲ့ အပေါ်မှာ project ရဲ့အမည်ကို ကြည့်ပါ။

- `AZURE_OPENAI_SERVICE` - **Overview** စာမျက်နှာရဲ့ **Included capabilities** tab မှာ **Azure OpenAI Service** ကို ရှာပါ။

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - **Management Center** ရဲ့ **Overview** စာမျက်နှာမှာ **Project properties** ကို သွားပါ။

- `GLOBAL_LLM_SERVICE` - **Connected resources** အောက်မှာ **Azure AI Services** connection name ကို ရှာပါ။ မရှိရင် **Azure portal** ရဲ့ resource group အောက်မှာ AI Services resource name ကို စစ်ဆေးပါ။

### Models + Endpoints Page

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - embedding model ကို ရွေးပါ (ဥပမာ `text-embedding-ada-002`) နဲ့ model details မှာ **Deployment name** ကို မှတ်သားပါ။

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - chat model ကို ရွေးပါ (ဥပမာ `gpt-4o-mini`) နဲ့ model details မှာ **Deployment name** ကို မှတ်သားပါ။

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - **Azure AI services** ကို ရှာပြီး click လုပ်ပါ၊ ပြီးရင် **Resource Management**, **Keys and Endpoint** ကို သွားပါ၊ "Azure OpenAI endpoints" မှာ "Language APIs" ဆိုတဲ့ endpoint ကို copy လုပ်ပါ။

- `AZURE_OPENAI_API_KEY` - အဲဒီ screen မှာ KEY 1 သို့မဟုတ် KEY 2 ကို copy လုပ်ပါ။

- `AZURE_SEARCH_SERVICE_ENDPOINT` - **Azure AI Search** resource ကို ရှာပြီး click လုပ်ပါ၊ **Overview** ကို ကြည့်ပါ။

- `AZURE_SEARCH_API_KEY` - **Settings** ကို သွားပြီး **Keys** ကို click လုပ်ပါ၊ primary သို့မဟုတ် secondary admin key ကို copy လုပ်ပါ။

### External Webpage

- `AZURE_OPENAI_API_VERSION` - [API version lifecycle](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) စာမျက်နှာရဲ့ **Latest GA API release** အောက်မှာ ရှာပါ။

### keyless authentication ကို Set Up လုပ်ပါ

Credential တွေကို hardcode မလုပ်ဘဲ Azure OpenAI နဲ့ keyless connection ကို အသုံးပြုပါ။ ဒီအတွက် `DefaultAzureCredential` ကို import လုပ်ပြီးနောက် `DefaultAzureCredential` function ကို call လုပ်ပါ။

```python
# Python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## ဘယ်နေရာမှာပဲ ရှုပ်နေတာလဲ?
အကယ်၍ ဒီစနစ်ကို အလုပ်မလုပ်နိုင်ဘဲ ပြဿနာတက်လာပါက၊ ကျွန်ုပ်တို့ရဲ့ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> သို့ ဝင်ရောက်ပါ၊ သို့မဟုတ် <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ပြဿနာတစ်ခု ဖန်တီးပါ</a>။

## နောက်သင်ခန်းစာ

ဒီသင်တန်းအတွက် ကုဒ်ကို အလုပ်လုပ်ဖို့ အဆင်သင့်ဖြစ်ပါပြီ။ AI Agents ရဲ့ ကမ္ဘာကို ပိုမိုလေ့လာရင်း ပျော်ရွှင်ပါစေ!

[AI Agents နှင့် Agent အသုံးပြုမှုများအကြောင်း အကျဉ်းချုပ်](../01-intro-to-ai-agents/README.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။