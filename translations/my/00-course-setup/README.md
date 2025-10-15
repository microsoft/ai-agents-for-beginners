<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T11:57:24+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "my"
}
-->
# သင်ခန်းစာ စတင်ခြင်း

## မိတ်ဆက်

ဒီသင်ခန်းစာမှာ သင်ခန်းစာရဲ့ ကုဒ်နမူနာတွေကို ဘယ်လို run လုပ်ရမယ်ဆိုတာကို ဖော်ပြပေးမှာပါ။

## အခြားလေ့လာသူတွေနဲ့ ပေါင်းသင်းပြီး အကူအညီရယူပါ

သင့် repo ကို clone လုပ်ဖို့ စတင်မလုပ်ခင် [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) ကို join လုပ်ပါ။ ဒီမှာ setup အတွက် အကူအညီရယူနိုင်သလို သင်ခန်းစာနဲ့ပတ်သက်တဲ့ မေးခွန်းတွေကို မေးနိုင်ပါတယ်။ အခြားလေ့လာသူတွေနဲ့ ဆက်သွယ်နိုင်ပါတယ်။

## ဒီ Repo ကို Clone လုပ်ပါ သို့မဟုတ် Fork လုပ်ပါ

စတင်ရန် GitHub Repository ကို clone သို့မဟုတ် fork လုပ်ပါ။ ဒါက သင့်ကိုယ်ပိုင် သင်ခန်းစာအကြောင်းအရာကို ရရှိစေပြီး ကုဒ်ကို run, test, နဲ့ ပြင်ဆင်နိုင်ပါမယ်။

<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repo ကို fork လုပ်ရန်</a> link ကို နှိပ်ပါ။

အခု သင့်မှာ ဒီသင်ခန်းစာရဲ့ ကိုယ်ပိုင် fork လုပ်ထားတဲ့ version ရှိပါပြီ။

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.my.png)

### Shallow Clone (workshop / Codespaces အတွက် အကြံပြု)

  >အပြည့်အစုံ repository ကို download လုပ်တဲ့အခါ file အားလုံးနဲ့ history အပြည့်အစုံကြောင့် အလွန်ကြီးမား (~3 GB) ဖြစ်နိုင်ပါတယ်။ workshop တက်ရောက်ဖို့ သို့မဟုတ် lesson folder အနည်းငယ်သာလိုအပ်တဲ့အခါ Shallow clone (သို့မဟုတ် sparse clone) က history အများစုကို truncate လုပ်ပြီး blob တွေကို skip လုပ်ခြင်းအားဖြင့် download အများစုကို ရှောင်ရှားနိုင်ပါတယ်။

#### Quick shallow clone — minimal history, all files

အောက်ပါ command တွေမှာ `<your-username>` ကို သင့် fork URL (သို့မဟုတ် upstream URL) နဲ့ အစားထိုးပါ။

နောက်ဆုံး commit history ကိုသာ clone လုပ်ရန် (download size သေးငယ်):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

တိကျတဲ့ branch ကို clone လုပ်ရန်:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimal blobs + only selected folders

ဒီမှာ partial clone နဲ့ sparse-checkout ကို အသုံးပြုပါတယ် (Git 2.25+ လိုအပ်ပြီး partial clone support ရှိတဲ့ Git ကို အကြံပြုပါတယ်):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

repo folder ထဲကို ဝင်ပါ:

bash အတွက်:

```bash
cd ai-agents-for-beginners
```

Powershell အတွက်:

```powershell
Set-Location ai-agents-for-beginners
```

ထို့နောက် သင်လိုအပ်တဲ့ folder တွေကို သတ်မှတ်ပါ (အောက်မှာ ဥပမာအနေနဲ့ folder နှစ်ခုကို ဖော်ပြထားပါတယ်):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

clone လုပ်ပြီး file တွေကို စစ်ဆေးပြီးနောက် သင့်မှာ file တွေသာလိုအပ်ပြီး space ကို လွှတ်ချင်လျှင် (git history မပါ) repository metadata ကို delete လုပ်ပါ (💀မပြန်လည်ပြင်နိုင် — Git functionality အားလုံးကို ဆုံးရှုံးပါမည်: commit, pull, push, သို့မဟုတ် history access မရှိပါ):

Linux/macOS အတွက်:

```bash
rm -rf .git
```

Windows အတွက်:

```powershell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ကို အသုံးပြုခြင်း (local download ကြီးမားမှုကို ရှောင်ရှားရန် အကြံပြု)

- GitHub UI မှတဆင့် repo အတွက် Codespace အသစ်တစ်ခုကို ဖန်တီးပါ။  

- အသစ်ဖန်တီးထားတဲ့ codespace ရဲ့ terminal မှာ shallow/sparse clone command တစ်ခုကို run လုပ်ပြီး သင်လိုအပ်တဲ့ lesson folder တွေကို Codespace workspace ထဲသို့ ယူဆောင်ပါ။
- အလိုအလျောက်: Codespaces ထဲမှာ clone လုပ်ပြီးနောက် .git ကို ဖယ်ရှားပြီး အပို space ကို reclaim လုပ်ပါ (ဖယ်ရှားရေး command တွေကို အထက်မှာ ကြည့်ပါ)။
- မှတ်ချက်: repo ကို Codespaces ထဲမှာ တိုက်ရိုက်ဖွင့်ချင်လျှင် (အပို clone မရှိဘဲ) Codespaces က devcontainer environment ကို တည်ဆောက်ပြီး သင်လိုအပ်တာထက် ပိုပြီး provision လုပ်နိုင်ပါတယ်။ အသစ်ဖန်တီးထားတဲ့ Codespace ထဲမှာ shallow copy ကို clone လုပ်ခြင်းက disk usage ကို ပိုမိုထိန်းချုပ်နိုင်စေပါတယ်။

#### အကြံပြုချက်များ

- edit/commit လုပ်ချင်လျှင် clone URL ကို သင့် fork နဲ့ အစားထိုးပါ။
- နောက်ပိုင်းမှာ history သို့မဟုတ် file တွေ ပိုလိုအပ်လာလျှင် fetch လုပ်နိုင်သလို sparse-checkout ကို ပြင်ဆင်ပြီး အပို folder တွေကို ထည့်သွင်းနိုင်ပါတယ်။

## ကုဒ်ကို run လုပ်ခြင်း

ဒီသင်ခန်းစာမှာ AI Agents တည်ဆောက်ဖို့ လက်တွေ့လုပ်ဆောင်နိုင်ဖို့ Jupyter Notebooks တွေကို ပေးထားပါတယ်။

ကုဒ်နမူနာတွေမှာ အောက်ပါ framework တွေကို အသုံးပြုထားပါတယ်:

**GitHub Account လိုအပ်သည် - အခမဲ့**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. (semantic-kernel.ipynb) အဖြစ် label လုပ်ထားသည်။
2) AutoGen Framework + GitHub Models Marketplace. (autogen.ipynb) အဖြစ် label လုပ်ထားသည်။

**Azure Subscription လိုအပ်သည်**:
3) Azure AI Foundry + Azure AI Agent Service. (azureaiagent.ipynb) အဖြစ် label လုပ်ထားသည်။

သုံးမျိုးလုံးကို စမ်းသပ်ကြည့်ဖို့ အကြံပြုပါတယ်။ သင့်အတွက် အကောင်းဆုံးအလုပ်လုပ်မယ့် နမူနာကို ရှာဖွေကြည့်ပါ။

သင်ရွေးချယ်တဲ့ option အပေါ်မူတည်ပြီး အောက်မှာဖော်ပြထားတဲ့ setup အဆင့်တွေကို လိုက်နာရပါမယ်:

## လိုအပ်ချက်များ

- Python 3.12+
  - **NOTE**: Python3.12 မရှိလျှင် install လုပ်ပါ။ ထို့နောက် requirements.txt file မှာပါဝင်တဲ့ version တွေကို install လုပ်ဖို့ python3.12 ကို အသုံးပြုပြီး venv ကို ဖန်တီးပါ။
  
    >ဥပမာ

    Python venv directory ဖန်တီးပါ:

    ``` bash
    python3 -m venv venv
    ```

    ထို့နောက် venv environment ကို activate လုပ်ပါ:

    macOS နဲ့ Linux အတွက်

    ```bash
    source venv/bin/activate
    ```
  
    Windows အတွက်

    ```bash
    venv\Scripts\activate
    ```

- GitHub Account - GitHub Models Marketplace ကို အသုံးပြုရန်
- Azure Subscription - Azure AI Foundry ကို အသုံးပြုရန်
- Azure AI Foundry Account - Azure AI Agent Service ကို အသုံးပြုရန်

ဒီ repository ရဲ့ root မှာ `requirements.txt` file ကို ထည့်သွင်းထားပြီး ကုဒ်နမူနာတွေကို run လုပ်ဖို့လိုအပ်တဲ့ Python packages အားလုံးပါဝင်ပါတယ်။

terminal မှာ root repository မှာ အောက်ပါ command ကို run လုပ်ပြီး install လုပ်နိုင်ပါတယ်:

```bash
pip install -r requirements.txt
```
Python virtual environment ကို ဖန်တီးပြီး conflicts နဲ့ ပြဿနာတွေကို ရှောင်ရှားဖို့ အကြံပြုပါတယ်။

## VSCode ကို Setup လုပ်ပါ
VSCode မှာ Python ရဲ့ version မှန်ကန်မှုကို သေချာစေပါ။

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Models ကို အသုံးပြုတဲ့ နမူနာများအတွက် Set Up

### အဆင့် 1: GitHub Personal Access Token (PAT) ကို ရယူပါ

ဒီသင်ခန်းစာမှာ GitHub Models Marketplace ကို အသုံးပြုထားပြီး သင် AI Agents တည်ဆောက်ဖို့ အသုံးပြုမယ့် Large Language Models (LLMs) ကို အခမဲ့ access ရရှိစေပါတယ်။

GitHub Models ကို အသုံးပြုဖို့ [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) ကို ဖန်တီးရပါမယ်။

GitHub Account ရဲ့ <a href="https://github.com/settings/personal-access-tokens" target="_blank">Personal Access Tokens settings</a> ကို သွားပြီး ဖန်တီးနိုင်ပါတယ်။

Token ဖန်တီးတဲ့အခါ [Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) ကို လိုက်နာပါ။ ဒါက သင့် token ကို ဒီသင်ခန်းစာရဲ့ ကုဒ်နမူနာတွေကို run လုပ်ဖို့လိုအပ်တဲ့ permission တွေကိုသာပေးဖို့ အရေးကြီးပါတယ်။

1. **Developer settings** ကို သွားပြီး ဘယ်ဘက်ဘက်မှာရှိတဲ့ `Fine-grained tokens` option ကို ရွေးချယ်ပါ။
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.my.png)

    ထို့နောက် `Generate new token` ကို ရွေးချယ်ပါ။

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.my.png)

2. သင့် token ရဲ့ ရည်ရွယ်ချက်ကို ဖော်ပြတဲ့ အဓိကအမည်ကို ထည့်သွင်းပါ။

    🔐 Token Duration အကြံပြုချက်

    အကြံပြုထားတဲ့ သက်တမ်း: 30 ရက်
    ပိုမိုလုံခြုံမှုအတွက် သက်တမ်းကို ပိုမိုတိုတောင်းစေဖို့ — ဥပမာ 7 ရက် 🛡️
    သင့်ကိုယ်ပိုင် learning momentum ကို မြှင့်တင်ပြီး သင်ခန်းစာကို ပြီးမြောက်စေဖို့ အကောင်းဆုံးနည်းလမ်း 🚀။

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.my.png)

3. Token ရဲ့ scope ကို ဒီ repository ရဲ့ fork အတွက်သာ ကန့်သတ်ပါ။

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.my.png)

4. Token ရဲ့ permissions ကို ကန့်သတ်ပါ: **Permissions** အောက်မှာ **Account** tab ကို click လုပ်ပြီး "+ Add permissions" button ကို click လုပ်ပါ။ Dropdown တစ်ခု ပေါ်လာပါမယ်။ **Models** ကို ရှာပြီး box ကို check လုပ်ပါ။
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.my.png)

5. Token ကို ဖန်တီးမည့်အခါ လိုအပ်တဲ့ permissions တွေကို verify လုပ်ပါ။ ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.my.png)

6. Token ကို ဖန်တီးမည့်အခါ password manager vault ကဲ့သို့ secure နေရာမှာ သိမ်းဆည်းရန် ပြင်ဆင်ထားပါ။ Token ကို ဖန်တီးပြီးနောက် ပြန်လည်ကြည့်ရှုနိုင်မည်မဟုတ်ပါ။ ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.my.png)

သင်ဖန်တီးထားတဲ့ token ကို copy လုပ်ပါ။ အခု သင့် `.env` file ထဲကို ဒီ token ကို ထည့်သွင်းပါ။

### အဆင့် 2: သင့် `.env` File ကို ဖန်တီးပါ

terminal မှာ အောက်ပါ command ကို run လုပ်ပြီး `.env` file ကို ဖန်တီးပါ။

```bash
cp .env.example .env
```

ဒီဟာက example file ကို copy လုပ်ပြီး `.env` ကို directory ထဲမှာ ဖန်တီးပါမယ်။ ထို့နောက် environment variable တွေကို value တွေဖြည့်ပါ။

သင့် token ကို copy လုပ်ပြီး `.env` file ကို သင့်အကြိုက်ဆုံး text editor မှာ ဖွင့်ပြီး `GITHUB_TOKEN` field ထဲကို paste လုပ်ပါ။
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.my.png)

အခု သင် ဒီသင်ခန်းစာရဲ့ ကုဒ်နမူနာတွေကို run လုပ်နိုင်ပါပြီ။

## Azure AI Foundry နဲ့ Azure AI Agent Service ကို အသုံးပြုတဲ့ နမူနာများအတွက် Set Up

### အဆင့် 1: Azure Project Endpoint ကို ရယူပါ

Azure AI Foundry မှ hub နဲ့ project တစ်ခုကို ဖန်တီးဖို့ အဆင့်တွေကို [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources) မှာ ကြည့်ပါ။

Project ကို ဖန်တီးပြီးနောက် project ရဲ့ connection string ကို ရယူရပါမယ်။

ဒီဟာကို Azure AI Foundry portal ရဲ့ **Overview** စာမျက်နှာမှာ သွားပြီး ရယူနိုင်ပါတယ်။

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.my.png)

### အဆင့် 2: သင့် `.env` File ကို ဖန်တီးပါ

terminal မှာ အောက်ပါ command ကို run လုပ်ပြီး `.env` file ကို ဖန်တီးပါ။

```bash
cp .env.example .env
```

ဒီဟာက example file ကို copy လုပ်ပြီး `.env` ကို directory ထဲမှာ ဖန်တီးပါမယ်။ ထို့နောက် environment variable တွေကို value တွေဖြည့်ပါ။

သင့် token ကို copy လုပ်ပြီး `.env` file ကို သင့်အကြိုက်ဆုံး text editor မှာ ဖွင့်ပြီး `PROJECT_ENDPOINT` field ထဲကို paste လုပ်ပါ။

### အဆင့် 3: Azure ကို Sign in လုပ်ပါ

လုံခြုံရေးအကောင်းဆုံးအနေအထားအတွက် Microsoft Entra ID နဲ့ [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) ကို အသုံးပြုပါ။

terminal ကို ဖွင့်ပြီး `az login --use-device-code` ကို run လုပ်ပြီး Azure account ကို sign in လုပ်ပါ။

Sign in လုပ်ပြီးနောက် terminal မှာ subscription ကို ရွေးချယ်ပါ။

## အပို Environment Variables - Azure Search နဲ့ Azure OpenAI 

Agentic RAG Lesson - Lesson 5 - မှာ Azure Search နဲ့ Azure OpenAI ကို အသုံးပြုတဲ့ နမူနာတွေ ပါဝင်ပါတယ်။

ဒီနမူနာတွေကို run လုပ်ချင်လျှင် `.env` file ထဲမှာ အောက်ပါ environment variable တွေကို ထည့်သွင်းရပါမယ်:

### Overview Page (Project)

- `AZURE_SUBSCRIPTION_ID` - **Overview** စာမျက်နှာရဲ့ **Project details** မှာ စစ်ဆေးပါ။

- `AZURE_AI_PROJECT_NAME` - **Overview** စာမျက်နှာရဲ့ အပေါ်မှာ project ရဲ့ အမည်ကို ကြည့်ပါ။

- `AZURE_OPENAI_SERVICE` - **Overview** စာမျက်နှာရဲ့ **Included capabilities** tab မှာ **Azure OpenAI Service** ကို ရှာပါ။

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - **Management Center** ရဲ့ **Overview** စာမျက်နှာမှာ **Project properties** ကို သွားပါ။

- `GLOBAL_LLM_SERVICE` - **Connected resources** အောက်မှာ **Azure AI Services** connection name ကို ရှာပါ။ မရှိလျှင် **Azure portal** မှာ သင့် resource group အောက်မှာ AI Services resource name ကို စစ်ဆေးပါ။

### Models + Endpoints Page

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - embedding model ကို ရွေးချယ်ပါ (ဥပမာ `text-embedding-ada-002`) နဲ့ model details မှ **Deployment name** ကို မှတ်သားပါ။

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - chat model ကို ရွေးချယ်ပါ (ဥပမာ `gpt-4o-mini`) နဲ့ model details မှ **Deployment name** ကို မှတ်သားပါ။

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - **Azure AI services** ကို ရှာပြီး click လုပ်ပါ၊ ထို့နောက် **Resource Management**, **Keys and Endpoint** ကို သွားပါ၊ "Azure OpenAI endpoints" မှာ "Language APIs" ဆိုတဲ့ endpoint ကို copy လုပ်ပါ။

- `AZURE_OPENAI_API_KEY` - အတူတူသော screen မှာ KEY 1 သို့မဟုတ် KEY 2 ကို copy လုပ်ပါ။

- `AZURE_SEARCH_SERVICE_ENDPOINT` - **Azure AI Search** resource ကို ရှာပြီး click လုပ်ပါ၊ **Overview** ကို ကြည့်ပါ။

- `AZURE_SEARCH_API_KEY` - **Settings** ကို သွားပြီး **Keys** ကို click လုပ်ပါ၊ primary သို့မဟုတ် secondary admin key ကို copy လုပ်ပါ။

### External Webpage

- `AZURE_OPENAI_API_VERSION` - [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) စာမျက်နှာရဲ့ **Latest GA API release** ကို သွားပါ။

### keyless authentication ကို Setup လုပ်ပါ

သင့် credentials တွေကို hardcode မလုပ်ဘဲ Azure OpenAI နဲ့ keyless connection ကို အသုံးပြုပါ။ ဒီအတွက် `DefaultAzureCredential` ကို import လုပ်ပြီးနောက် `DefaultAzureCredential` function ကို call လုပ်ပါ။

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## ဘယ်နေရာမှာပဲ ရှုပ်ထွေးနေလဲ?
အကယ်၍ ဒီစနစ်ကို အလုပ်မလုပ်နိုင်တာတွေ့ရင် <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> သို့မဟုတ် <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ပြဿနာတစ်ခုဖန်တီးပါ</a>။

## နောက်ဆင့်သင်ခန်းစာ

ဒီသင်တန်းအတွက် ကုဒ်ကို အလုပ်လုပ်ဖို့ အဆင်သင့်ဖြစ်ပါပြီ။ AI Agents အကြောင်းကို ပိုမိုလေ့လာရင်း ပျော်ရွှင်ပါစေ!

[AI Agents နှင့် Agent အသုံးပြုမှုများအကြောင်း အကျဉ်းချုပ်](../01-intro-to-ai-agents/README.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။