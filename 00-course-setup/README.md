# သင်တန်းအစီအစဉ် တည်ဆောက်ခြင်း

## နိဒါန်း

ဤသင်ခန်းစာတွင် ဤသင်တန်း၏ ကုဒ်နမူနာများကို မည်သို့အသုံးပြုရမည်ကို လေ့လာရမည်ဖြစ်ပါသည်။

## ဤ Repo ကို Clone သို့မဟုတ် Fork လုပ်ပါ

စတင်ရန်အတွက်၊ GitHub Repository ကို clone သို့မဟုတ် fork လုပ်ပေးပါ။ ၎င်းသည် သင်တန်းပစ္စည်းများ၏ သင့်ကိုယ်ပိုင်ဗားရှင်းကို ဖန်တီးပေးမည်ဖြစ်ပြီး ကုဒ်များကို run၊ test နှင့် tweak လုပ်နိုင်မည်ဖြစ်ပါသည်။

ဤလုပ်ငန်းကို <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repo fork လုပ်ရန် လင့်ခ်</a> ကို နှိပ်ခြင်းဖြင့် ပြုလုပ်နိုင်ပါသည်။

ယခုအခါ သင့်တွင် အောက်ပါလင့်ခ်တွင် ဤသင်တန်း၏ သင့်ကိုယ်ပိုင် forked version ရှိနေပြီဖြစ်ပါသည်။

![Forked Repo](./images/forked-repo.png)

## ကုဒ်များကို အသုံးပြုခြင်း

ဤသင်တန်းတွင် AI Agents များတည်ဆောက်ခြင်းဆိုင်ရာ လက်တွေ့အတွေ့အကြုံရရှိရန်အတွက် အသုံးပြုနိုင်သော Jupyter Notebooks များကို ပံ့ပိုးထားပါသည်။

ကုဒ်နမူနာများတွင် အောက်ပါများကို အသုံးပြုထားပါသည်-

**GitHub အကောင့်လိုအပ်သည် - အခမဲ့**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace (semantic-kernel.ipynb ဟု အမှတ်အသားပြုထားသည်)
2) AutoGen Framework + GitHub Models Marketplace (autogen.ipynb ဟု အမှတ်အသားပြုထားသည်)

**Azure Subscription လိုအပ်သည်**:
3) Azure AI Foundry + Azure AI Agent Service (azureaiagent.ipynb ဟု အမှတ်အသားပြုထားသည်)

သင့်အတွက် အကောင်းဆုံးဖြစ်သည့်အရာကို ရှာဖွေတွေ့ရှိရန် အမျိုးအစားသုံးမျိုးလုံးကို စမ်းကြည့်ရန် အကြံပြုအပ်ပါသည်။

သင်ရွေးချယ်သည့်ရွေးချယ်မှုက အောက်တွင်လိုက်နာရမည့် စနစ်တည်ဆောက်မှုအဆင့်များကို ဆုံးဖြတ်မည်ဖြစ်ပါသည်-

## လိုအပ်ချက်များ

- Python 3.12+
- GitHub Account - GitHub Models Marketplace ကို ဝင်ရောက်အသုံးပြုရန်အတွက်
- Azure Subscription - Azure AI Foundry ကို ဝင်ရောက်အသုံးပြုရန်အတွက်
- Azure AI Foundry Account - Azure AI Agent Service ကို ဝင်ရောက်အသုံးပြုရန်အတွက်

ကုဒ်နမူနာများကို run လုပ်ရန်အတွက် လိုအပ်သော Python packages များအားလုံးပါဝင်သည့် `requirements.txt` ဖိုင်ကို ဤ repository ၏ root တွင် ထည့်သွင်းထားပါသည်။

Repository ၏ root တွင် terminal တွင် အောက်ပါ command ကို run လုပ်ခြင်းဖြင့် ၎င်းတို့ကို install လုပ်နိုင်ပါသည်-

```bash
pip install -r requirements.txt
```
ပဋိပက္ခများနှင့် ပြဿနာများကို ရှောင်ရှားရန်အတွက် Python virtual environment တစ်ခုဖန်တီးရန် အကြံပြုအပ်ပါသည်။

## GitHub Models အသုံးပြု၍ နမူနာများအတွက် စနစ်တည်ဆောက်ခြင်း

### အဆင့် ၁- သင့် GitHub Personal Access Token (PAT) ကို ရယူခြင်း

လက်ရှိအချိန်တွင် ဤသင်တန်းသည် AI Agents များဖန်တီးရန်အတွက် အသုံးပြုမည့် Large Language Models (LLMs) များကို အခမဲ့ဝင်ရောက်အသုံးပြုခွင့်ပေးရန်အတွက် GitHub Models Marketplace ကို အသုံးပြုထားပါသည်။

ဤဝန်ဆောင်မှုကို ဝင်ရောက်အသုံးပြုရန်အတွက် သင့်တွင် GitHub Personal Access Token တစ်ခုဖန်တီးရန် လိုအပ်ပါသည်။

ဤလုပ်ငန်းကို သင့် GitHub Account ရှိ <a href="https://github.com/settings/personal-access-tokens" target="_blank">Personal Access Tokens settings</a> သို့ သွားခြင်းဖြင့် ပြုလုပ်နိုင်ပါသည်။

သင့်မျက်နှာပြင်၏ ဘယ်ဘက်ခြမ်းတွင် `Fine-grained tokens` ရွေးချယ်မှုကို ရွေးချယ်ပါ။

ထို့နောက် `Generate new token` ကို ရွေးချယ်ပါ။

![Generate Token](./images/generate-token.png)

သင့်အား token အတွက် အမည်တစ်ခုရိုက်ထည့်ရန်၊ သက်တမ်းကုန်ဆုံးရက် (အကြံပြုချက်- ရက် ၃၀)၊ နှင့် သင့် token အတွက် scopes များ (Public Repositories) ကို ရွေးချယ်ရန် တောင်းဆိုမည်ဖြစ်ပါသည်။

ဤ token ၏ permissions များကို ပြင်ဆင်ရန်လည်း လိုအပ်ပါသည်- Permissions -> Models -> Allows access to GitHub Models

သင်အခုမှ ဖန်တီးပြီးသား သင့်အသစ်သော token ကို ကူးယူပါ။ ယခုအခါ ၎င်းကို ဤသင်တန်းတွင် ပါဝင်သော သင့် `.env` ဖိုင်သို့ ထည့်သွင်းမည်ဖြစ်ပါသည်။

### အဆင့် ၂- သင့် `.env` ဖိုင်ကို ဖန်တီးခြင်း

သင့် `.env` ဖိုင်ကို ဖန်တီးရန်အတွက် သင့် terminal တွင် အောက်ပါ command ကို run လုပ်ပါ။

```bash
cp .env.example .env
```

ဤလုပ်ငန်းသည် example file ကို ကူးယူပြီး သင့် directory တွင် `.env` တစ်ခုဖန်တီးမည်ဖြစ်ပြီး ၎င်းတွင် environment variables များအတွက် တန်ဖိုးများကို ဖြည့်သွင်းရမည်ဖြစ်ပါသည်။

သင့် token ကို ကူးယူပြီးပါက၊ သင့်နှစ်သက်သော text editor တွင် `.env` ဖိုင်ကို ဖွင့်ပြီး သင့် token ကို `GITHUB_TOKEN` field တွင် ကပ်ထည့်ပါ။

ယခုအခါ သင်သည် ဤသင်တန်း၏ ကုဒ်နမူနာများကို run လုပ်နိုင်ပြီဖြစ်ပါသည်။

## Azure AI Foundry နှင့် Azure AI Agent Service အသုံးပြု၍ နမူနာများအတွက် စနစ်တည်ဆောက်ခြင်း

### အဆင့် ၁- သင့် Azure Project Connection String ကို ရယူခြင်း

Azure AI Foundry တွင် hub နှင့် project ဖန်တီးခြင်းအတွက် အဆင့်များကို ဤနေရာတွင် လိုက်နာပါ- [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

သင့် project ကို ဖန်တီးပြီးပါက၊ သင့် project အတွက် connection string ကို ရယူရန် လိုအပ်မည်ဖြစ်ပါသည်။

ဤလုပ်ငန်းကို Azure AI Foundry portal ရှိ သင့် project ၏ **Overview** စာမျက်နှာသို့ သွားခြင်းဖြင့် ပြုလုပ်နိုင်ပါသည်။

![Project Connection String](./images/project-connection-string.png)

### အဆင့် ၂- သင့် `.env` ဖိုင်ကို ဖန်တီးခြင်း

သင့် `.env` ဖိုင်ကို ဖန်တီးရန်အတွက် သင့် terminal တွင် အောက်ပါ command ကို run လုပ်ပါ။

```bash
cp .env.example .env
```

ဤလုပ်ငန်းသည် example file ကို ကူးယူပြီး သင့် directory တွင် `.env` တစ်ခုဖန်တီးမည်ဖြစ်ပြီး ၎င်းတွင် environment variables များအတွက် တန်ဖိုးများကို ဖြည့်သွင်းရမည်ဖြစ်ပါသည်။

သင့် token ကို ကူးယူပြီးပါက၊ သင့်နှစ်သက်သော text editor တွင် `.env` ဖိုင်ကို ဖွင့်ပြီး သင့် token ကို `PROJECT_CONNECTION_STRING` field တွင် ကပ်ထည့်ပါ။

### အဆင့် ၃- Azure သို့ ဝင်ရောက်ခြင်း

လုံခြုံရေးအတွက် အကောင်းဆုံးအလေ့အကျင့်အနေဖြင့်၊ ကျွန်ုပ်တို့သည် Microsoft Entra ID ဖြင့် Azure OpenAI သို့ authentication လုပ်ရန်အတွက် [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) ကို အသုံးပြုမည်ဖြစ်ပါသည်။ ထိုသို့လုပ်ရန်မတိုင်မီ၊ သင့် operating system အတွက် [installation instructions](https://learn.microsoft.com/cli/azure/install-azure-cli?WT.mc_id=academic-105485-koreyst) အတိုင်း **Azure CLI** ကို ဦးစွာ install လုပ်ရန် လိုအပ်ပါသည်။

ထို့နောက်၊ terminal တစ်ခုဖွင့်ပြီး သင့် Azure account သို့ sign in လုပ်ရန်အတွက် `az login --use-device-code` ကို run လုပ်ပါ။

သင် log in ဝင်ပြီးပါက၊ terminal တွင် သင့် subscription ကို ရွေးချယ်ပါ။

## ထပ်လောင်း Environment Variables များ - Azure Search နှင့် Azure OpenAI

Agentic RAG Lesson - သင်ခန်းစာ ၅ အတွက် Azure Search နှင့် Azure OpenAI ကို အသုံးပြုသော နမူနာများရှိပါသည်။

ဤနမူနာများကို run လုပ်လိုပါက၊ သင့် `.env` ဖိုင်တွင် အောက်ပါ environment variables များကို ထည့်သွင်းရန် လိုအပ်ပါသည်-

### Overview Page (Project)

- `AZURE_SUBSCRIPTION_ID` - သင့် project ၏ **Overview** စာမျက်နှာရှိ **Project details** တွင် စစ်ဆေးပါ။

- `AZURE_AI_PROJECT_NAME` - သင့် project အတွက် **Overview** စာမျက်နှာ၏ ထိပ်ဘက်တွင် ကြည့်ပါ။

- `AZURE_OPENAI_SERVICE` - ဤအရာကို **Overview** စာမျက်နှာရှိ **Azure OpenAI Service** အတွက် **Included capabilities** tab တွင် ရှာပါ။

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - **Management Center** ၏ **Overview** စာမျက်နှာရှိ **Project properties** သို့ သွားပါ။

- `GLOBAL_LLM_SERVICE` - **Connected resources** အောက်တွင် **Azure AI Services** connection name ကို ရှာပါ။ အကယ်၍ စာရင်းတွင် မပါရှိပါက၊ AI Services resource name အတွက် သင့် resource group အောက်ရှိ **Azure portal** ကို စစ်ဆေးပါ။

### Models + Endpoints Page

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - သင့် embedding model (ဥပမာ `text-embedding-ada-002`) ကို ရွေးချယ်ပြီး model details မှ **Deployment name** ကို မှတ်ချက်ပြုပါ။

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - သင့် chat model (ဥပမာ `gpt-4o-mini`) ကို ရွေးချယ်ပြီး model details မှ **Deployment name** ကို မှတ်ချက်ပြုပါ။

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - **Azure AI services** ကို ရှာပြီး နှိပ်ပါ၊ ထို့နောက် **Resource Management**၊ **Keys and Endpoint** သို့ သွားပြီး "Azure OpenAI endpoints" သို့ scroll down လုပ်ပြီး "Language APIs" ဟုဖော်ပြထားသည့်အရာကို ကူးယူပါ။

- `AZURE_OPENAI_API_KEY` - တူညီသောမျက်နှာပြင်မှ KEY 1 သို့မဟုတ် KEY 2 ကို ကူးယူပါ။

- `AZURE_SEARCH_SERVICE_ENDPOINT` - သင့် **Azure AI Search** resource ကို ရှာပြီး နှိပ်ပြီး **Overview** ကို ကြည့်ပါ။

- `AZURE_SEARCH_API_KEY` - ထို့နောက် **Settings** သို့ သွားပြီး **Keys** သို့ သွား၍ primary သို့မဟုတ် secondary admin key ကို ကူးယူပါ။

### External Webpage

- `AZURE_OPENAI_API_VERSION` - **Latest GA API release** အောက်ရှိ [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) စာမျက်နှာကို ကြည့်ရှုပါ။

### Keyless authentication တည်ဆောက်ခြင်း

သင့် credentials များကို hardcode လုပ်မည့်အစား၊ ကျွန်ုပ်တို့သည် Azure OpenAI နှင့် keyless connection ကို အသုံးပြုမည်ဖြစ်ပါသည်။ ထိုသို့လုပ်ရန်အတွက်၊ ကျွန်ုပ်တို့သည် `DefaultAzureCredential` ကို import လုပ်ပြီး နောက်ပိုင်းတွင် credential ရရှိရန်အတွက် `DefaultAzureCredential` function ကို ခေါ်မည်ဖြစ်ပါသည်။

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## တစ်နေရာရာတွင် စွန့်သတ်နေပါသလား?

အကယ်၍ သင့်တွင် ဤစနစ်တည်ဆောက်မှုကို run လုပ်ရာတွင် မည်သည့်ပြဿနာများရှိပါက၊ ကျွန်ုပ်တို့၏ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> သို့ ဝင်ရောက်ပါ သို့မဟုတ် <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">issue တစ်ခုဖန်တီးပါ</a>။

## နောက်သင်ခန်းစာ

ယခုအခါ သင်သည် ဤသင်တန်းအတွက် ကုဒ်များကို run လုပ်ရန် အသင့်ဖြစ်နေပြီဖြစ်ပါသည်။ AI Agents များ၏ ကမ္ဘာကြီးအကြောင်း ပိုမိုလေ့လာရာတွင် ပျော်ရွှင်ကြပါစေ!

[AI Agents များနှင့် Agent အသုံးပြုမှုကိစ္စများ မိတ်ဆက်](../01-intro-to-ai-agents/README.md)