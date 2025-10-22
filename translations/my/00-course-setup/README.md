<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T08:50:08+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "my"
}
-->
# သင်ခန်းစာ စတင်ခြင်း

## မိတ်ဆက်

ဒီသင်ခန်းစာမှာ ဒီသင်တန်းရဲ့ ကုဒ်နမူနာတွေကို ဘယ်လိုအသုံးပြုရမလဲဆိုတာကို ဖော်ပြပေးမှာဖြစ်ပါတယ်။

## အခြားလေ့လာသူတွေနဲ့ ပေါင်းသင်းပြီး အကူအညီရယူပါ

သင့်ရဲ့ repo ကို clone လုပ်ဖို့မစတင်ခင် [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) ကို join လုပ်ပြီး setup အတွက် အကူအညီရယူပါ၊ သင်တန်းနဲ့ပတ်သက်တဲ့မေးခွန်းတွေမေးပါ၊ ဒါမှမဟုတ် အခြားလေ့လာသူတွေနဲ့ ဆက်သွယ်ပါ။

## ဒီ Repo ကို Clone လုပ်ပါ ဒါမှမဟုတ် Fork လုပ်ပါ

စတင်ရန်အတွက် GitHub Repository ကို clone လုပ်ပါ ဒါမှမဟုတ် fork လုပ်ပါ။ ဒါက သင့်ကိုယ်ပိုင် သင်တန်းစာအုပ်ကို ရရှိစေပြီး ကုဒ်တွေကို run, test, ပြင်ဆင်နိုင်ပါမယ်။

ဒီအရာကို <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repo ကို fork လုပ်ရန်</a> လင့်ခ်ကို နှိပ်ခြင်းဖြင့် ပြုလုပ်နိုင်ပါတယ်။

အခု သင့်မှာ ဒီသင်တန်းရဲ့ fork လုပ်ထားတဲ့ ကိုယ်ပိုင် version ကို အောက်ပါလင့်ခ်မှာ ရရှိထားပါပြီ။

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.my.png)

### Shallow Clone (workshop / Codespaces အတွက် အကြံပြုချက်)

  >အပြည့်အစုံ repository ကို download လုပ်တဲ့အခါမှာ အလွန်ကြီးမားတဲ့ (~3 GB) file တွေကို download လုပ်ရနိုင်ပါတယ်။ Workshop တက်ရောက်ဖို့ ဒါမှမဟုတ် သင်ခန်းစာ folder အနည်းငယ်သာလိုအပ်တဲ့အခါမှာ shallow clone (ဒါမှမဟုတ် sparse clone) က history အများစုကို truncate လုပ်ပြီး blob တွေကို skip လုပ်ခြင်းဖြင့် download အများဆုံးကို ရှောင်ရှားနိုင်ပါတယ်။

#### Quick shallow clone — နောက်ဆုံး commit history, အားလုံး file များ

အောက်ပါ command တွေမှာ `<your-username>` ကို သင့် fork URL (ဒါမှမဟုတ် သင့်အကြိုက်အတိုင်း upstream URL) နဲ့ အစားထိုးပါ။

နောက်ဆုံး commit history ကိုသာ clone လုပ်ရန် (download အနည်းဆုံး):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

တစ်ခုချင်း branch ကို clone လုပ်ရန်:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — blob အနည်းဆုံး + ရွေးချယ်ထားသော folder များသာ

ဒီအရာက partial clone နဲ့ sparse-checkout ကို အသုံးပြုပါတယ် (Git 2.25+ လိုအပ်ပြီး partial clone ကို ပံ့ပိုးတဲ့ Git version အသစ်ကို အကြံပြုပါတယ်):

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

ထို့နောက် သင်လိုအပ်တဲ့ folder တွေကို သတ်မှတ်ပါ (အောက်မှာ ဥပမာအနေနဲ့ folder နှစ်ခုကို ပြထားပါတယ်):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

clone လုပ်ပြီး file တွေကို အတည်ပြုပြီးနောက်မှာ၊ file တွေကိုသာလိုအပ်ပြီး နေရာလွတ်ချင်ရင် (git history မပါ) repository metadata ကို delete လုပ်ပါ (💀မပြန်လည်ပြင်နိုင် — Git functionality အားလုံးကို ဆုံးရှုံးပါမည်: commit, pull, push, ဒါမှမဟုတ် history access မရှိပါ):

Linux/macOS အတွက်:

```bash
rm -rf .git
```

Windows အတွက်:

```powershell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ကို အသုံးပြုခြင်း (local large downloads ကိုရှောင်ရှားရန်အတွက် အကြံပြုချက်)

- GitHub UI မှတဆင့် ဒီ repo အတွက် Codespace အသစ်တစ်ခုကို ဖန်တီးပါ။  

- အသစ်ဖန်တီးထားသော codespace ရဲ့ terminal မှာ shallow/sparse clone command တွေထဲက တစ်ခုကို run လုပ်ပြီး သင်လိုအပ်တဲ့ သင်ခန်းစာ folder တွေကို Codespace workspace ထဲသို့ ယူပါ။
- ရွေးချယ်စရာ: Codespaces ထဲမှာ clone လုပ်ပြီးနောက် .git ကို ဖယ်ရှားပြီး နေရာလွတ်အပိုကို ပြန်ယူပါ (ဖယ်ရှားရေး command တွေကို အထက်မှာကြည့်ပါ)။
- မှတ်ချက်: repo ကို Codespaces ထဲမှာ တိုက်ရိုက်ဖွင့်ချင်တယ်ဆိုရင် (အပို clone မရှိဘဲ) Codespaces က devcontainer ပတ်ဝန်းကျင်ကို တည်ဆောက်ပြီး သင်လိုအပ်တာထက် ပိုပြီး provision လုပ်နိုင်ပါတယ်။ Codespaces အသစ်တစ်ခုထဲမှာ shallow copy ကို clone လုပ်ခြင်းက disk usage ကို ပိုမိုထိန်းချုပ်နိုင်စေပါတယ်။

#### အကြံပြုချက်များ

- သင် edit/commit လုပ်ချင်တယ်ဆိုရင် clone URL ကို သင့် fork နဲ့ အစားထိုးပါ။
- နောက်ပိုင်းမှာ history ဒါမှမဟုတ် file တွေ ပိုလိုအပ်လာရင် fetch လုပ်နိုင်ပါတယ် ဒါမှမဟုတ် sparse-checkout ကို ပြင်ဆင်ပြီး အပို folder တွေကို ထည့်သွင်းနိုင်ပါတယ်။

## ကုဒ်ကို run လုပ်ခြင်း

ဒီသင်တန်းက AI Agents တည်ဆောက်ခြင်းကို လက်တွေ့လုပ်ဆောင်နိုင်ဖို့ Jupyter Notebooks တွေကို ပေးထားပါတယ်။

ကုဒ်နမူနာတွေမှာ အောက်ပါအတိုင်း အသုံးပြုထားပါတယ် -

**GitHub Account လိုအပ်သည် - အခမဲ့**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. (semantic-kernel.ipynb) အဖြစ် label လုပ်ထားသည်။
2) AutoGen Framework + GitHub Models Marketplace. (autogen.ipynb) အဖြစ် label လုပ်ထားသည်။

**Azure Subscription လိုအပ်သည်**:
3) Azure AI Foundry + Azure AI Agent Service. (azureaiagent.ipynb) အဖြစ် label လုပ်ထားသည်။

ဒီနမူနာ ၃ ခုလုံးကို စမ်းသုံးဖို့ အကြံပြုပါတယ်၊ ဘယ်ဟာက သင့်အတွက် အကောင်းဆုံးဖြစ်မလဲဆိုတာကို သိနိုင်ဖို့။

သင်ရွေးချယ်တဲ့ option တစ်ခုတည်းက အောက်မှာဖော်ပြထားတဲ့ setup အဆင့်တွေကို သင်လိုက်နာဖို့လိုအပ်မှုကို သတ်မှတ်ပေးပါမယ်။

## လိုအပ်ချက်များ

- Python 3.12+
  - **NOTE**: Python3.12 မရှိရင် install လုပ်ပါ။ ထို့နောက် requirements.txt file မှာပါဝင်တဲ့ version တွေကို install လုပ်ဖို့ python3.12 ကို အသုံးပြုပြီး venv ကို ဖန်တီးပါ။
  
    >ဥပမာ

    Python venv directory ကို ဖန်တီးပါ:

    ``` bash
    python3 -m venv venv
    ```

    ထို့နောက် venv environment ကို activate လုပ်ပါ:

    macOS နှင့် Linux အတွက်

    ```bash
    source venv/bin/activate
    ```
  
    Windows အတွက်

    ```bash
    venv\Scripts\activate
    ```

- GitHub Account - GitHub Models Marketplace ကို access ရယူရန်
- Azure Subscription - Azure AI Foundry ကို access ရယူရန်
- Azure AI Foundry Account - Azure AI Agent Service ကို access ရယူရန်

ဒီ repository ရဲ့ root မှာ `requirements.txt` file ကို ထည့်သွင်းထားပြီး ကုဒ်နမူနာတွေကို run လုပ်ဖို့လိုအပ်တဲ့ Python packages တွေပါဝင်ပါတယ်။

အောက်ပါ command ကို terminal မှာ run လုပ်ခြင်းဖြင့် install လုပ်နိုင်ပါတယ်:

```bash
pip install -r requirements.txt
```
Python virtual environment ကို ဖန်တီးပြီး conflicts နဲ့ ပြဿနာတွေကို ရှောင်ရှားဖို့ အကြံပြုပါတယ်။

## VSCode ကို Setup လုပ်ပါ
VSCode မှာ Python version မှန်ကန်တဲ့အရာကို အသုံးပြုနေကြောင်း သေချာပါစေ။

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Models ကို အသုံးပြုတဲ့ နမူနာများအတွက် Set Up

### အဆင့် ၁: GitHub Personal Access Token (PAT) ကို ရယူပါ

ဒီသင်တန်းက GitHub Models Marketplace ကို အသုံးပြုပြီး သင် AI Agents တည်ဆောက်ဖို့ အသုံးပြုမယ့် Large Language Models (LLMs) ကို အခမဲ့ access ရရှိစေပါတယ်။

GitHub Models ကို အသုံးပြုဖို့ [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) ကို ဖန်တီးဖို့လိုအပ်ပါတယ်။

ဒီအရာကို သင့် GitHub Account ရဲ့ <a href="https://github.com/settings/personal-access-tokens" target="_blank">Personal Access Tokens settings</a> ကိုသွားပြီး ပြုလုပ်နိုင်ပါတယ်။

Token ကို ဖန်တီးတဲ့အခါ [Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) ကို လိုက်နာပါ။ ဒါက သင့် token ကို ဒီသင်တန်းရဲ့ ကုဒ်နမူနာတွေကို run လုပ်ဖို့လိုအပ်တဲ့ permission တွေကိုသာပေးဖို့ အဓိကပါ။

1. **Developer settings** ကိုသွားပြီး ဘယ်ဘက်ဘက်မှာရှိတဲ့ `Fine-grained tokens` option ကို ရွေးပါ။
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.my.png)

    ထို့နောက် `Generate new token` ကို ရွေးပါ။

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.my.png)

2. Token ရဲ့ ရည်ရွယ်ချက်ကို ဖော်ပြတဲ့ အမည်တစ်ခုကို ထည့်သွင်းပြီး နောက်ပိုင်းမှာ အလွယ်တကူသိနိုင်အောင် ပြုလုပ်ပါ။

    🔐 Token Duration အကြံပြုချက်

    အကြံပြုထားသော သက်တမ်း: ၃၀ ရက်
    ပိုမိုလုံခြုံမှုရှိစေရန် အတိုချုပ်တဲ့ကာလကို ရွေးချယ်နိုင်ပါတယ်—ဥပမာ ၇ ရက် 🛡️
    သင့်ရဲ့ သင်ယူမှုအလှုပ်လှုပ်ရှိနေစဉ်အတွင်း သင်တန်းကို ပြီးမြောက်စေရန် ကိုယ်ပိုင်ပန်းတိုင်တစ်ခုကို သတ်မှတ်နိုင်ပါတယ် 🚀။

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.my.png)

3. Token ရဲ့ scope ကို ဒီ repository ရဲ့ fork အတွက်သာ ကန့်သတ်ပါ။

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.my.png)

4. Token ရဲ့ permissions ကို ကန့်သတ်ပါ: **Permissions** အောက်မှာ **Account** tab ကို click လုပ်ပြီး "+ Add permissions" button ကို click လုပ်ပါ။ Dropdown တစ်ခု ပေါ်လာပါမယ်။ **Models** ကို ရှာပြီး box ကို check လုပ်ပါ။
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.my.png)

5. Token ကို generate လုပ်မည့်အခါမှာ လိုအပ်တဲ့ permissions တွေကို အတည်ပြုပါ။ ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.my.png)

6. Token ကို generate လုပ်မည့်အခါမှာ password manager vault ကဲ့သို့သော လုံခြုံတဲ့နေရာမှာ token ကို သိမ်းဆည်းဖို့ ပြင်ဆင်ထားပါ။ Token ကို ဖန်တီးပြီးနောက်မှာ ပြန်လည်ကြည့်နိုင်မှာမဟုတ်ပါဘူး။ ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.my.png)

သင် vừa ဖန်တီးထားတဲ့ token ကို copy လုပ်ပါ။ အခု သင့်ရဲ့ `.env` file ထဲကို ဒီ token ကို ထည့်သွင်းပါ။

### အဆင့် ၂: သင့် `.env` File ကို ဖန်တီးပါ

သင့် terminal မှာ အောက်ပါ command ကို run လုပ်ပြီး `.env` file ကို ဖန်တီးပါ။

```bash
cp .env.example .env
```

ဒီအရာက example file ကို copy လုပ်ပြီး `.env` file ကို directory ထဲမှာ ဖန်တီးပါမယ်။ ထို့နောက် environment variables အတွက် value တွေကို ဖြည့်ပါ။

သင့် token ကို copy လုပ်ပြီး `.env` file ကို သင့်အကြိုက်ဆုံး text editor မှာ ဖွင့်ပြီး `GITHUB_TOKEN` field ထဲကို paste လုပ်ပါ။
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.my.png)

အခု သင် ဒီသင်တန်းရဲ့ ကုဒ်နမူနာတွေကို run လုပ်နိုင်ပါပြီ။

## Azure AI Foundry နှင့် Azure AI Agent Service ကို အသုံးပြုတဲ့ နမူနာများအတွက် Set Up

### အဆင့် ၁: Azure Project Endpoint ကို ရယူပါ

Azure AI Foundry မှာ hub နဲ့ project တစ်ခုကို ဖန်တီးခြင်းအဆင့်တွေကို ဒီမှာ လိုက်နာပါ: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Project ကို ဖန်တီးပြီးနောက်မှာ project ရဲ့ connection string ကို ရယူဖို့လိုအပ်ပါမယ်။

ဒီအရာကို Azure AI Foundry portal ရဲ့ **Overview** စာမျက်နှာကိုသွားပြီး ပြုလုပ်နိုင်ပါတယ်။

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.my.png)

### အဆင့် ၂: သင့် `.env` File ကို ဖန်တီးပါ

သင့် terminal မှာ အောက်ပါ command ကို run လုပ်ပြီး `.env` file ကို ဖန်တီးပါ။

```bash
cp .env.example .env
```

ဒီအရာက example file ကို copy လုပ်ပြီး `.env` file ကို directory ထဲမှာ ဖန်တီးပါမယ်။ ထို့နောက် environment variables အတွက် value တွေကို ဖြည့်ပါ။

သင့် token ကို copy လုပ်ပြီး `.env` file ကို သင့်အကြိုက်ဆုံး text editor မှာ ဖွင့်ပြီး `PROJECT_ENDPOINT` field ထဲကို paste လုပ်ပါ။

### အဆင့် ၃: Azure ကို Sign in လုပ်ပါ

လုံခြုံရေးအကောင်းဆုံးအနေအထားအတွက် Microsoft Entra ID နဲ့ [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) ကို အသုံးပြုပြီး Azure OpenAI ကို authenticate လုပ်ပါ။

နောက်ဆုံးမှာ terminal ကိုဖွင့်ပြီး `az login --use-device-code` ကို run လုပ်ပြီး သင့် Azure account ကို sign in လုပ်ပါ။

Sign in လုပ်ပြီးနောက်မှာ terminal မှာ သင့် subscription ကို ရွေးချယ်ပါ။

## အပို Environment Variables - Azure Search နှင့် Azure OpenAI 

Agentic RAG Lesson - Lesson 5 - မှာ Azure Search နှင့် Azure OpenAI ကို အသုံးပြုတဲ့ နမူနာတွေပါဝင်ပါတယ်။

ဒီနမူနာတွေကို run လုပ်ချင်တယ်ဆိုရင် `.env` file ထဲမှာ အောက်ပါ environment variables တွေကို ထည့်သွင်းဖို့လိုအပ်ပါတယ်:

### Overview Page (Project)

- `AZURE_SUBSCRIPTION_ID` - **Overview** စာမျက်နှာရဲ့ **Project details** မှာ ကြည့်ပါ။

- `AZURE_AI_PROJECT_NAME` - သင့် project ရဲ့ **Overview** စာမျက်နှာရဲ့ အပေါ်မှာ ကြည့်ပါ။

- `AZURE_OPENAI_SERVICE` - **Overview** စာမျက်နှာရဲ့ **Included capabilities** tab မှာ **Azure OpenAI Service** ကို ရှာပါ။

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - **Management Center** ရဲ့ **Overview** စာမျက်နှာမှာ **Project properties** ကို သွားပါ။

- `GLOBAL_LLM_SERVICE` - **Connected resources** အောက်မှာ **Azure AI Services** connection name ကို ရှာပါ။ မရှိရင် **Azure portal** မှာ သင့် resource group အောက်မှာ AI Services resource name ကို ကြည့်ပါ။

### Models + Endpoints Page

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - သင့် embedding model (ဥပမာ `text-embedding-ada-002`) ကို ရွေးချယ်ပြီး model details မှာ **Deployment name** ကို မှတ်သားပါ။

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - သင့် chat model (ဥပမာ `gpt-4o-mini`) ကို ရွေးချယ်ပြီး model details မှာ **Deployment name** ကို မှတ်သားပါ။

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - **Azure AI services** ကို ရှာပြီး click လုပ်ပါ၊ ထို့နောက် **Resource Management**, **Keys and Endpoint** ကို သွားပြီး "Azure OpenAI endpoints" မှာ "Language APIs" ဆိုတဲ့ endpoint ကို copy လုပ်ပါ။

- `AZURE_OPENAI_API_KEY` - အဲဒီအတူတူ screen မှာ KEY 1 ဒါမှမဟုတ် KEY 2 ကို copy လုပ်ပါ။

- `AZURE_SEARCH_SERVICE_ENDPOINT` - သင့် **Azure AI Search** resource ကို ရှာပြီး click လုပ်ပါ၊ ထို့နောက် **Overview** ကို ကြည့်ပါ။

- `AZURE_SEARCH_API_KEY` - **Settings** ကို သွားပြီး **Keys** ကို click လုပ်ပြီး primary ဒါမှမဟုတ် secondary admin key ကို copy လုပ်ပါ။

###
အကယ်၍ ဒီ setup ကို run လုပ်ရာတွင် ပြဿနာများရှိပါက၊ ကျွန်ုပ်တို့၏ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> သို့ ဝင်ရောက်ပါ၊ သို့မဟုတ် <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">issue တစ်ခု ဖန်တီးပါ</a>။

## နောက်ဆုံး သင်ခန်းစာ

ဒီ course အတွက် code ကို run လုပ်ရန် သင့်အနေဖြင့် အဆင်သင့်ဖြစ်ပါပြီ။ AI Agents အကြောင်းကို ပိုမိုလေ့လာရင်း ပျော်ရွှင်ပါစေ!

[AI Agents နှင့် Agent အသုံးပြုမှု အကြောင်းအရာများကို မိတ်ဆက်ခြင်း](../01-intro-to-ai-agents/README.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။