# သင်တန်းအတွက် Setup ပြင်ဆင်ခြင်း

## မိတ်ဆက်

ဒီသင်ခန်းစာမှာ သင်တန်းအတွင်းပါဝင်တဲ့ code sample တွေကို ဘယ်လိုအသုံးပြုရမယ်ဆိုတာကိုလေ့လာသွားမှာဖြစ်ပါတယ်။

## Repository ကို Clone လုပ်ခြင်း သို့မဟုတ် Fork လုပ်ခြင်း

ပထမဆုံးအဆင့်အနေနဲ့ GitHub မှာရှိတဲ့ Repository ကို **clone လုပ်ပါ** သို့မဟုတ် **fork လုပ်ပါ**။ ဒါဆိုရ် သင့်ရဲ့ ကိုယ်ပိုင် version ရလာပြီး၊ ကိုယ်တိုင် code ကို run လုပ်၊ စမ်းသပ်၊ ပြုပြင်နိုင်ပါလိမ့်မယ်။

အောက်ပါ link ကိုနှိပ်၍ fork လုပ်နိုင်ပါတယ် -  
[Repo ကို fork လုပ်ရန်](https://github.com/microsoft/ai-agents-for-beginners/fork)

Fork လုပ်ပြီးပါက သင့်ရဲ့ ကိုယ်ပိုင် repository ကို အောက်ပါလင့်ခ်မှာတွေ့နိုင်ပါတယ် -

![Forked Repo](./images/forked-repo.png)

## Code ကို Run လုပ်ခြင်း

ဒီသင်တန်းမှာတော့ AI Agent တွေကို တည်ဆောက်ဖို့အတွက် လက်တွေ့ကျကျ လေ့လာနိုင်အောင် Jupyter Notebooks များဖြင့် တင်ထားပေးပါတယ်။

Code sampleအတွက် အောက်ကFramework ထဲက တစ်ခုခုအသုံးပြုလို့ရပါတယ် -



### **GitHub Account ဖြင့် အသုံးပြုခြင်း (အခမဲ့)**

1. **Semantic Kernel Agent Framework + GitHub Models Marketplace**  
   **ဖိုင်အမည်** – `semantic-kernel.ipynb`

2. **AutoGen Framework + GitHub Models Marketplace**  
   **ဖိုင်အမည်** – `autogen.ipynb`



### **Azure Subscription လိုအပ်သော**

3. **Azure AI Foundry + Azure AI Agent Service**  
   **ဖိုင်အမည်** – `azureaiagent.ipynb`


Framework သုံးမျိုးလုံးကိုလည်း စမ်းသပ်ကြည့်ဖို့ အကြံပြုပါတယ်၊ ဘယ်ဟာက သင့်နဲ့အကောင်းဆုံး လိုက်ဖက်တယ်ဆိုတာကို စမ်းသပ်ကြည့်ဖို့ပါ။

သင်ရွေးချယ်မယ့် option ပေါ်မူတည်ပြီး အောက်မှာဖော်ပြထားတဲ့ setup လုပ်ငန်းစဉ်များ မတူညီနိုင်ပါဘူး
## လိုအပ်ချက်များ (Requirements)

- Python 3.12 နှင့်အထက်
- GitHub Models Marketplace ကို အသုံးပြုရန်အတွက် - GitHub Account တစ်ခု -
- Azure AI Foundry ကို အသုံးပြုရန်အတွက် - Azure Subscription 
- Azure AI Agent Service ကို အသုံးပြုရန်အတွက် - Azure AI Foundry Account တသ်ခု -

ဒီ repository ရဲ့ root directory မှာ `requirements.txt` ဖိုင်တစ်ခု ပါဝင်ပါတယ်။  
ဒီဖိုင်တွင် code sample များကို run ဖို့လိုအပ်တဲ့ Python package များကို စုစည်းဖော်ပြထားပါတယ်။

အောက်ပါ command ကို terminal တွင် run လုပ်ခြင်းဖြင့် install လုပ်နိုင်ပါသည် –

```bash
pip install -r requirements.txt
```
**အကြံပြုချက်** – Dependencyများ မရှုပ်ထွေးအောင် Python Virtual Environment တစ်ခုဖန်တီးပြီး အသုံးပြုဖို့ အကြံပြုလိုပါသည်။



## GitHub Models အသုံးပြုသည့် Samples များအတွက် Setup လုပ်ခြင်း

### အဆင့် ၁ – GitHub Personal Access Token (PAT) ရယူခြင်း

ဒီသင်တန်းအတွင်းမှာ GitHub Models Marketplace ကို အသုံးပြုပြီး Large Language Models (LLMs) များကို အခမဲ့အသုံးပြုခွင့်ပေးထားပါတယ်။  
AI Agents များတည်ဆောက်ဖို့အတွက် GitHub Personal Access Token (PAT) တစ်ခုလိုအပ်ပါသည်။

PAT ကိုရယူရန် သင့် GitHub အကောင့်ထဲမှ  
**[Personal Access Tokens settings](https://github.com/settings/personal-access-tokens)** ကိုသွားပါ။

ဘယ်ဘက် sidebar မှာ **Fine-grained tokens** ကိုရွေးချယ်ပြီး  
**Generate new token** ကို နှိပ်ပါ။

![Generate Token](./images/generate-token.png)

သင်သည် Token အသစ်ဖန်တီးရာတွင် အောက်ပါအချက်များကို ဖြည့်သွင်းရန် လိုအပ်ပါမည်။

- Token အတွက် **အမည်** တစ်ခု ထည့်သွင်းပါ  
- **သက်တမ်း (Expiration Date)** ကိုရွေးချယ်ပါ *(အကြံပြုချက် – ၃၀ ရက်)*  
- Token ၏ **အသုံးပြုခွင့်များ (Scopes)** မှာ **Public Repositories** ကိုသာ ရွေးချယ်ပါ

Token ဖန်တီးပြီးသွားသောအခါတွင် သင်ဖန်တီးလိုက်သော **Token ကို copy လုပ်ထားပါ**။  
GitHub သည် Token ကိုနောက်မှပြသမည်မဟုတ်ပါ။

ဒီသင်တန်းတွင် ပါဝင်တဲ့ `.env` ဖိုင်အတွင်း `GITHUB_TOKEN` ဆိုသည့်နေရာတွင် သင့် Token ကို ထည့်သွင်းရန် လိုအပ်ပါသည်။


### အဆင့် ၂ – `.env` ဖိုင် ဖန်တီးခြင်း

Terminal ထဲတွင် အောက်ပါ command ကို run လုပ်ပါ –

```bash
cp .env.example .env
```

ဒီ command သည် `.env.example` ကို copy လုပ်ပြီး သင့် directory ထဲတွင် `.env` ဖိုင်အသစ်တစ်ခုဖန်တီးပေးပါမည်။  
ထို `.env` ဖိုင်တွင် သင်လိုအပ်သည့် environment variables များ၏ တန်ဖိုးများကို ဖြည့်သွင်းနိုင်ပါသည်။

သင်၏ Token ကို copy လုပ်ပြီးပါက၊ သင်အကြိုက်ဆုံး Text Editor ဖြင့် `.env` ဖိုင်ကိုဖွင့်ပါ။  
ထို့နောက် `GITHUB_TOKEN=` နေရာတွင် သင့် Token ကို paste လုပ်ပါ။

ယခုအချိန်တွင် သင်သည် သင်တန်းတွင်ပါဝင်သော code sample များကို run လုပ်နိုင်ပြီဖြစ်ပါသည်။

## Azure AI Foundry နှင့် Azure AI Agent Service ကို အသုံးပြုသော Samples များအတွက် Setup

### အဆင့် ၁ – Azure Project Connection String ရယူခြင်း

Azure AI Foundry တွင် Project နှင့် Agent တစ်ခုဖန်တီးရန်အတွက် [အောက်ပါလင့်ခ်](https://learn.microsoft.com/en-us/azure/ai-services/agents/quickstart?pivots=ai-foundry-portal?WT.mc_id=academic-105485-koreyst) ကိုလိုက်နာပါ။

Project တစ်ခုဖန်တီးပြီးပါက၊ သင့် Project ၏ **Connection String** ကိုရယူရန် လိုအပ်ပါသည်။  
ဤအရာကို Azure AI Foundry portal ၏ **Overview** စာမျက်နှာတွင်ရယူနိုင်သည်။

![Project Connection String](./images/project-connection-string.png)


### အဆင့် ၂ – `.env` ဖိုင်ဖန်တီးခြင်း

Terminal ထဲတွင် အောက်ပါ command ကို run လုပ်ပါ –

```bash
cp .env.example .env
```
ဤ command သည် `.env.example` ကို copy လုပ်ပြီး `.env` ဖိုင်အသစ်တစ်ခုဖန်တီးပေးပါမည်။  
ဤဖိုင်အတွင်းတွင် environment variables များအတွက် တန်ဖိုးများကို ဖြည့်သွင်းရပါမည်။

Token ကို copy လုပ်ပြီးပါက `.env` ဖိုင်ကိုဖွင့်ပြီး `PROJECT_CONNECTION_STRING=` နေရာတွင် Paste လုပ်ပါ။

---

### အဆင့် ၃ – Azure သို့ Sign in လုပ်ခြင်း

လုံခြုံရေးအကောင်းဆုံးဖြစ်အောင် **Keyless Authentication** ကို အသုံးပြုမည်ဖြစ်ပြီး၊  
**Microsoft Entra ID** ဖြင့် **Azure OpenAI** ကို Authenticate လုပ်ပါမည်။  
ဤလုပ်ဆောင်မှုအတွက် သင်၏ OS အလိုက် **Azure CLI** ကို ဤအညွှန်းအတိုင်း ထည့်သွင်းရန်လိုအပ်ပါသည် –  
➡️ [Azure CLI Installation Guide](https://learn.microsoft.com/cli/azure/install-azure-cli?WT.mc_id=academic-105485-koreyst)

ထို့နောက် Terminal ကိုဖွင့်ပြီး အောက်ပါ command ကို run လုပ်ပါ –

```bash
az login --use-device-code
```
Azure မှာ login ၀င်ပြီးပါက Terminal ထဲတွင် သင့် subscription ကို ရွေးချယ်ပါ။

## ထပ်ဆောင်း Environment Variables များ - Azure Search နှင့် Azure OpenAI

**Lesson 5 - Agentic RAG** တွင် Azure Search နှင့် Azure OpenAI ကို အသုံးပြုသည့် sample များပါဝင်ပါသည်။  
ဤ sample များကို run လုပ်ရန် `.env` ဖိုင်အတွင်း အောက်ဖော်ပြပါ environment variables များ ထည့်သွင်းရန် လိုအပ်ပါသည်။

### Overview Page (Project)

- `AZURE_SUBSCRIPTION_ID` - သင့် project ၏ **Overview** စာမျက်နှာရှိ **Project details** တွင်ကြည့်ပါ
- `AZURE_AI_PROJECT_NAME` - **Overview** စာမျက်နှာ၏ ထိပ်တွင်ဖော်ပြထားသည်
- `AZURE_OPENAI_SERVICE` - **Overview** စာမျက်နှာအတွင်း **Included capabilities** tab မှာ **Azure OpenAI Service** ကို ရှာကြည့်ပါ

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - **Management Center** > **Overview** စာမျက်နှာရှိ **Project properties** တွင်ကြည့်ပါ
- `GLOBAL_LLM_SERVICE` - **Connected resources** အောက်တွင် **Azure AI Services** connection name ကိုကြည့်ပါ။ မတွေ့လျှင် Azure Portal တွင် သင့် resource group အောက်မှ AI Services resource name ကို ကြည့်ပါ

### Models + Endpoints Page

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - သင့် embedding model (ဥပမာ - `text-embedding-ada-002`) ကိုရွေးပြီး **Deployment name** ကို မှတ်သားပါ
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - သင့် chat model (ဥပမာ - `gpt-4o-mini`) ကိုရွေးပြီး **Deployment name** ကို မှတ်သားပါ

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - **Azure AI Services** ကို click လုပ်ပြီး **Resource Management** > **Keys and Endpoint** သို့သွားပါ၊ “Azure OpenAI endpoints” တွင် **Language APIs** ကို Copy လုပ်ပါ
- `AZURE_OPENAI_API_KEY` - အထက်ဖော်ပြပါနေရာမှ **KEY 1** သို့မဟုတ် **KEY 2** ကို Copy လုပ်ပါ
- `AZURE_SEARCH_SERVICE_ENDPOINT` - သင့် **Azure AI Search** resource ကို click လုပ်ပြီး **Overview** တွင်ကြည့်ပါ
- `AZURE_SEARCH_API_KEY` - **Settings** > **Keys** ထဲတွင် admin key (primary သို့မဟုတ် secondary) ကို Copy လုပ်ပါ

### External Webpage

- `AZURE_OPENAI_API_VERSION` - [API Version Lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) စာမျက်နှာတွင် **Latest GA API release** ကို ကြည့်ပါ

## Keyless Authentication Setup

Credentials များကို hardcode မလုပ်ဘဲ Azure OpenAI နှင့် keyless connection ကို အသုံးပြုပါမည်။  
အတွက်အနေနှင့် Python မှာ အောက်ပါအတိုင်း `DefaultAzureCredential` ကို import ပြုလုပ်ပါ။

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## အဆင်မပြေတာရှိလား?

ဤ setup ကို run လုပ်ရာတွင် ပြဿနာများရှိပါက  
<a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> သို့ ဝင်ရောက်ဆွေးနွေးနိုင်ပြီး  
သို့မဟုတ် <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">GitHub မှ issue တစ်ခုဖန်တီးပါ</a>။

## နောက်ထပ်သင်ခန်းစာ

ယခုအခါ သင်သည် ဤသင်တန်းအတွက် code များကို run လုပ်ရန် အသင့်ဖြစ်ပါပြီ။  
AI Agents များ၏ ကမ္ဘာအကြောင်းကို ဆက်လက်လေ့လာနိုင်ပါပြီ။

[AI Agent များနှင့် အသုံးပြုမှု Use Cases များအကြောင်း မိတ်ဆက်](../01-intro-to-ai-agents/README.md)


