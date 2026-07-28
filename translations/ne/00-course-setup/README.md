# कोर्स सेटअप

## परिचय

यस पाठले यस कोर्सका कोड नमूनाहरू कसरी चलाउने भनेर समावेश गर्नेछ।

## अन्य सिक्नेहरूसँग जोडिनुहोस् र सहायता पाउनुहोस्

तपाईँको रेपो क्लोन गर्न सुरु गर्नु अघि, सेटअपमा कुनै पनि सहयोग लिन, कोर्स सम्बन्धी कुनै पनि प्रश्नहरू सोध्न, वा अन्य सिक्नेहरूसँग जडान हुन [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) मा सामेल हुनुहोस्।

## यो रेपो क्लोन वा फोर्क गर्नुहोस्

सुरु गर्नका लागि, कृपया GitHub Repository क्लोन वा फोर्क गर्नुहोस्। यसले तपाईँलाई कोर्स सामग्रीको आफ्नै संस्करण बनाउनेछ जसले गर्दा तपाईँ कोड चलाउन, परीक्षण गर्न, र परिमार्जन गर्न सक्नुहुन्छ!

यसलाई गर्नको लागि <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a> मा क्लिक गर्नुहोस्

अब तपाईँसँग निम्न लिंकमा यस कोर्सको आफ्नै फोर्क गरिएको संस्करण हुनु पर्छ:

![Forked Repo](../../../translated_images/ne/forked-repo.33f27ca1901baa6a.webp)

### शैलो क्लोन (कार्यशाला / Codespaces का लागि सिफारिस गरिन्छ)

  >पूरा रिपोजिटरी पूर्ण इतिहास र सबै फाइलहरू डाउनलोड गर्दा ठूलो (~3 GB) हुन सक्छ। यदि तपाईं केवल कार्यशालामा सहभागी हुनुभएको छ वा केवल केही पाठ फोल्डरहरू चाहिन्छ भने, शैलो क्लोन (वा स्पार्स क्लोन) ले इतिहास कटौती गरेर र/वा ब्लबहरू स्किप गरेर धेरै डाउनलोडबाट बचाउँछ।

#### छिटो शैलो क्लोन — न्यूनतम इतिहास, सबै फाइलहरू

तलको आदेशहरूमा `<your-username>` स्थानमा आफ्नो फोर्क URL (वा यदि चाहनु हुन्छ भने अपस्ट्रीम URL) राख्नुहोस्।

केवल सबैभन्दा पछिल्लो कमिट इतिहास क्लोन गर्न (सानो डाउनलोड):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

विशेष शाखा क्लोन गर्न:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### आंशिक (स्पार्स) क्लोन — न्यूनतम ब्लबहरू + मात्र चयनित फोल्डरहरू

यसले आंशिक क्लोन र स्पार्स-चेकआउट प्रयोग गर्छ (Git 2.25+ आवश्यक छ र आंशिक क्लोन समर्थन सहितको आधुनिक Git सिफारिस गरिन्छ):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

रिपो फोल्डरमा जानुहोस्:

```bash|powershell
cd ai-agents-for-beginners
```

त्यसपछि तपाईँले चाहनुभएको फोल्डरहरू निर्दिष्ट गर्नुहोस् (तलको उदाहरणले दुई फोल्डरहरू देखाउँछ):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

क्लोन र फाइलहरू प्रमाणित गरेपछि, यदि तपाईँलाई केवल फाइलहरू चाहिन्छ र ठाउँ खाली गर्न चाहनु हुन्छ (गिट इतिहास नभएको), कृपया रिपोजिटरी मेटाडाटा मेटाउनुहोस् (💀अपरिवर्तनीय — तपाईंले सबै Git कार्यक्षमता गुमाउनुहुनेछ: कमिटहरू, पुल, पुष, वा इतिहास पहुँच छैन)।

```bash
# zsh/bash
rm -rf .git
```

```powershell
# पावरशेल
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces प्रयोग गर्दै (स्थानीय ठूलो डाउनलोडबाट बच्न सिफारिस गरिन्छ)

- यो रेपोसँग नयाँ Codespace सिर्जना गर्नुहोस् [GitHub UI](https://github.com/codespaces) मार्फत।  

- नयाँ सृजना गरिएको Codespace को टर्मिनलमा माथिका शैलो/स्पार्स क्लोन आदेशहरूमध्ये एक चलाउनुहोस् जसले केवल तिमीलाई चाहिएको पाठ फोल्डरहरू Codespace कार्यक्षेत्रमा ल्याउँछ।
- वैकल्पिक: Codespaces भित्र क्लोन गरेपछि, थप ठाउँ फिर्ता लिन .git हटाउन सकिन्छ (माथिको हटाउने आदेशहरू हेर्नुहोस्)।
- नोट: यदि तपाईँले कोडस्पेसमा सिधै रेपो खोल्न चाहनुहुन्छ भने (अतिरिक्त क्लोन बिना), सावधान हुनुहोस् कि Codespaces ले devcontainer वातावरण निर्माण गर्छ र तपाईँलाई आवश्यक भन्दा बढी संसाधनहरू प्रदान गर्न सक्छ। नयाँ Codespace भित्र शैलो क्लोन गर्दा डिस्क प्रयोगमा बढी नियन्त्रण मिल्छ।

#### सुझावहरू

- यदि तपाईँ सम्पादन/कमिट गर्न चाहनु हुन्छ भने, क्लोन URL सधैं तपाईँको फोर्कसँग बदल्नुहोस्।
- यदि पछि तपाईँलाई थप इतिहास वा फाइलहरू चाहिन्छ भने, तिनीहरू फेच गर्न सक्नुहुन्छ वा स्पार्स-चेकआउट समायोजन गरेर थप फोल्डरहरू समावेश गर्न सक्नुहुन्छ।

## कोड चलाउने तरिका

यस कोर्समा तपाईँलाई AI एजेन्टहरू निर्माण गर्ने व्यावहारिक अनुभव दिनका लागि Jupyter Notebooks को श्रृंखला प्रदान गरिएको छ जुन तपाईँले चलाउन सक्नुहुन्छ।

कोड नमूनाहरूले **Microsoft Agent Framework (MAF)** प्रयोग गर्दछ `FoundryChatClient` सँग, जुन **Microsoft Foundry Agent Service V2** (Responses API) मार्फत **Microsoft Foundry** सँग जडान हुन्छ।

सबै Python नोटबुकहरू `*-python-agent-framework.ipynb` ले चिह्नित गरिएको छ।

## आवश्यकताहरू

- Python 3.12+
  - **नोट**: यदि तपाईँसँग Python3.12 स्थापना छैन भने, यो स्थापना गर्न सुनिश्चित गर्नुहोस्। त्यसपछि requirements.txt फाइल बाट सहि संस्करणहरू स्थापना गर्न python3.12 प्रयोग गरेर आफ्नो venv सिर्जना गर्नुहोस्।
  
    >उदाहरण

    Python venv डाइरेक्टरी सिर्जना गर्नुहोस्:

    ```bash|powershell
    python -m venv venv
    ```

    त्यसपछि venv वातावरण सक्रिय पार्नुहोस्:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET को नमूना कोडहरूका लागि, कृपया [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) वा पछिल्लो संस्करण स्थापना गर्नुहोस्। त्यसपछि आफ्नो स्थापना गरिएको .NET SDK संस्करण जाँच्नुहोस्:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — प्रमाणीकरणको लागि आवश्यक। [aka.ms/installazurecli](https://aka.ms/installazurecli) बाट स्थापना गर्नुहोस्।
- **Azure सदस्यता** — Microsoft Foundry र Microsoft Foundry Agent Service पहुँचका लागि।
- **Microsoft Foundry Project** — तैनाथ गरिएको मोडेल भएको प्रोजेक्ट (जस्तै, `gpt-5-mini`)। तल [Step 1](#चरण-1-microsoft-foundry-प्रोजेक्ट-सिर्जना-गर्नुहोस्) मा हेर्नुहोस्।

हामीले यस रिपोजिटरीको मल मौसमामा एक `requirements.txt` फाइल समावेश गरेका छौं जसमा कोड नमूनाहरू चलाउन आवश्यक सबै Python प्याकेजहरू छन्।

यसलाई तपाईँको टर्मिनलमा रिपोजिटरीको मूल फोल्डरमा यस आदेश चलाएर स्थापना गर्न सक्नुहुन्छ:

```bash|powershell
pip install -r requirements.txt
```

कुनै पनि द्वैत वा समस्या हुन नदिन हामी Python भर्चुअल वातावरण बनाउन सिफारिस गर्छौं।

## VSCode सेटअप

VSCode मा तपाईँ सही Python संस्करण प्रयोग गर्दै हुनुहुन्छ भनेर सुनिश्चित गर्नुहोस्।

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry र Microsoft Foundry Agent Service सेटअप गर्नुहोस्

### चरण 1: Microsoft Foundry प्रोजेक्ट सिर्जना गर्नुहोस्

नोटबुकहरू चलाउन Microsoft Foundry **hub** र **project** आवश्यक छ जसमा तैनाथ गरिएको मोडेल छ।

1. [ai.azure.com](https://ai.azure.com) मा जानुहोस् र आफ्नो Azure खाताले लगइन गर्नुहोस्।
2. एक **hub** सिर्जना गर्नुहोस् (वा पहिले देखिको प्रयोग गर्नुहोस्)। हेर्नुहोस्: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)।
3. hub भित्र एक **project** सिर्जना गर्नुहोस्।
4. **Models + Endpoints** → **Deploy model** मा गई मोडेल तैनाथ गर्नुहोस् (जस्तै, `gpt-5-mini`)।

### चरण 2: आफ्नो प्रोजेक्ट Endpoint र Model Deployment नाम प्राप्त गर्नुहोस्

Microsoft Foundry पोर्टलमा आफ्नो प्रोजेक्टबाट:

- **Project Endpoint** — **Overview** पृष्ठमा गई endpoint URL कपी गर्नुहोस्।

![Project Connection String](../../../translated_images/ne/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — **Models + Endpoints** मा गई आफ्नो तैनाथ गरिएको मोडेल चयन गर्नुहोस् र **Deployment name** नोट गर्नुहोस् (जस्तै, `gpt-5-mini`)।

### चरण 3: `az login` प्रयोग गरी Azure मा लगइन गर्नुहोस्

सबै नोटबुकहरूले प्रमाणीकरणको लागि **`AzureCliCredential`** प्रयोग गर्छन् — कुनै API कुञ्जीहरू व्यवस्थापन आवश्यक छैन। यसका लागि Azure CLI मार्फत साइन इन हुनु पर्ने हुन्छ।

1. **Azure CLI स्थापना गर्नुहोस्** यदि पूर्वस्थापित छैन भने: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **लगइन गर्नुहोस्** यसरी:

    ```bash|powershell
    az login
    ```

    यदि तपाईँ रिमोट/Codespace वातावरणमा हुनुहुन्छ जहाँ ब्राउजर छैन भने:

    ```bash|powershell
    az login --use-device-code
    ```

3. **आवश्यक परे आफ्नो सदस्यता चयन गर्नुहोस्** — तिनीहरू मध्ये आफ्नो Foundry प्रोजेक्ट भएको सदस्यता छान्नुहोस्।

4. **लगइन भएको पक्का गर्नुहोस्**:

    ```bash|powershell
    az account show
    ```

> **किन `az login`?** नोटबुकहरूले `azure-identity` प्याकेजबाट `AzureCliCredential` प्रयोग गरेर प्रमाणीकरण गर्दछन्। यसको अर्थ Azure CLI सत्रले क्रेडेन्सियलहरू प्रदान गर्छ — कुनै API कुञ्जी वा गोप्य कुञ्जीहरू तपाईँको `.env` फाइलमा पर्दैनन्। यो एक [सुरक्षा उत्कृष्ट अभ्यास](https://learn.microsoft.com/azure/developer/ai/keyless-connections) हो।

### चरण 4: आफ्नो `.env` फाइल सिर्जना गर्नुहोस्

उदाहरण फाइल कपी गर्नुहोस्:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# पावरशेल
Copy-Item .env.example .env
```

`.env` खोल्नुहोस् र यी दुई मानहरू भर्नुहोस्:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| भेरिएबल | कहाँ फेला पार्ने |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry पोर्टल → आफ्नो प्रोजेक्ट → **Overview** पृष्ठ |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry पोर्टल → **Models + Endpoints** → आफ्नो तैनाथ गरिएको मोडेलको नाम |

अधिकांश पाठहरूको लागि यति नै! नोटबुकहरूले तपाईँको `az login` सत्रबाट स्वचालित प्रमाणीकरण गर्छन्।

### चरण 5: Python निर्भरता स्थापना गर्नुहोस्

```bash|powershell
pip install -r requirements.txt
```

हामी सिफारिस गर्छौं कि तपाईं यो पहिले सिर्जित भर्चुअल वातावरणभित्र चलाउनुहोस्।

## पाठ 5 अतिरिक्त सेटअप (Agentic RAG)

पाठ 5 ले पुनर्प्राप्ति-समृद्ध उत्पत्तिका लागि **Azure AI Search** प्रयोग गर्दछ। यदि तपाईँ सो पाठ चलाउने योजना बनाउनुहुन्छ भने, यी भेरिएबलहरू तपाईँको `.env` फाइलमा थप्नुहोस्:

| भेरिएबल | कहाँ फेला पार्ने |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure पोर्टल → आफ्नो **Azure AI Search** स्रोत → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure पोर्टल → आफ्नो **Azure AI Search** स्रोत → **Settings** → **Keys** → प्राथमिक एडमिन कुञ्जी |

## ती पाठहरूको लागि थप सेटअप जुन Azure OpenAI सिधै कल गर्छ (पाठ 6 र 8)

पाठ 6 र 8 मा केही नोटबुकहरूले **Azure OpenAI** सिधै कल गर्छन् (Responses API प्रयोग गरेर) Microsoft Foundry प्रोजेक्टबाट नभई। यी नमूनाहरू पहिले GitHub Models प्रयोग गर्थे, जुन अवसान हुँदैछ (जुलाई २०२६ मा) र Responses API समर्थन गर्दैन। यदि तपाईँ ती नमूनाहरू चलाउने योजना बनाउनुभएको छ भने, यी भेरिएबलहरू तपाईँको `.env` फाइलमा थप्नुहोस्:

| भेरिएबल | कहाँ फेला पार्ने |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure पोर्टल → आफ्नो **Azure OpenAI** स्रोत → **Keys and Endpoint** → Endpoint (जस्तै `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | तपाईँले तैनाथ गरेको मोडेलको नाम (जस्तै `gpt-5-mini`) जुन Responses API समर्थन गर्दछ |
| `AZURE_OPENAI_API_KEY` | वैकल्पिक — केवल यदि तपाईं कुञ्जी-आधारित प्रमाणीकरण प्रयोग गर्नुहुन्छ `az login` / Entra ID को सट्टा |

> Responses API स्थिर `/openai/v1/` endpoint प्रयोग गर्छ, त्यसैले कुनै `api-version` आवश्यक पर्दैन। कुञ्जीरहित Entra ID प्रमाणीकरणको लागि `az login` साइन इन गर्नुहोस्।

## वैकल्पिक प्रदायक: MiniMax (OpenAI-संग मेल खाने)

[MiniMax](https://platform.minimaxi.com/) ले ठूलो-सन्दर्भ मोडेलहरू (२०४K टोकन्स सम्म) OpenAI-संग मेल खाने API मार्फत प्रदान गर्दछ। Microsoft Agent Framework को `OpenAIChatClient` जससुकै OpenAI-संग मेल खाने endpoint सँग काम गर्छ, त्यसैले तपाईँले MiniMax लाई Azure OpenAI वा OpenAI को सट्टामा प्रयोग गर्न सक्नुहुन्छ।

यी भेरिएबलहरू तपाईँको `.env` फाइलमा थप्नुहोस्:

| भेरिएबल | कहाँ फेला पार्ने |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | `https://api.minimax.io/v1` प्रयोग गर्नुहोस् (डिफल्ट मान) |
| `MINIMAX_MODEL_ID` | प्रयोग गर्न मोडेल नाम (जस्तै, `MiniMax-M3`) |

**उदाहरण मोडेलहरू**: `MiniMax-M3` (सिफारिस गरिएको), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (छिटो प्रतिक्रिया)। मोडेल नामहरू र उपलब्धता समयानुसार बदल्न सक्छ, र मोडेलमा पहुँच तपाईँको खाता वा क्षेत्र अनुसार निर्भर हुन सक्छ — हालको सूचीका लागि [MiniMax Platform](https://platform.minimaxi.com/) जाँच गर्नुहोस्। यदि `MiniMax-M3` तपाईँको खातामा उपलब्ध छैन भने, तपाईँले पहुँच पाएको मोडेल `MINIMAX_MODEL_ID` मा सेट गर्नुहोस् (जस्तै `MiniMax-M2.7`)।

जसले `OpenAIChatClient` प्रयोग गर्ने कोड नमूनाहरू (जस्तै, पाठ १४ होटल बुकिंग वर्कफ्लो) स्वतः तपाईँको MiniMax कन्फिगरेसन पहिचान गरी प्रयोग गर्नेछ जब `MINIMAX_API_KEY` सेट गरिएको हुन्छ।

## वैकल्पिक प्रदायक: Foundry Local (आफ्नो उपकरणमा मोडेल चलाउनुहोस्)

[Foundry Local](https://foundrylocal.ai) एक हल्का रUNTIME हो जसले OpenAI-सँग मेल खाने API मार्फत भाषा मोडेलहरू **पूरी रूपमा तपाईँको आफ्नै मशीनमा** डाउनलोड, व्यवस्थापन, र सेवा गर्दछ — कुनै क्लाउड, Azure सदस्यता, वा API कुञ्जीहरू आवश्यक पर्दैन। यो अफलाइन विकासका लागि, क्लाउड लागत बिना प्रयोगात्मक विकास, वा डाटा डिभाइसमै राख्न उत्तम विकल्प हो।

किनकि Microsoft Agent Framework को `OpenAIChatClient` जुनसुकै OpenAI-सँग मेल खाने endpoint सँग काम गर्दछ, Foundry Local Azure OpenAI को लागि स्थानीय विकल्प हो।

**1. Foundry Local स्थापना गर्नुहोस्**

```bash
# विन्डोज
winget install Microsoft.FoundryLocal

# म्याकओएस
brew install foundrylocal
```

**2. मोडेल डाउनलोड र चलाउनुहोस्** (यसले स्थानीय सेवा पनि सुरु गर्छ):

```bash
foundry model list          # उपलब्ध मोडेलहरू हेर्नुहोस्
foundry model run phi-4-mini
```

**3. स्थानीय endpoint पत्ता लगाउन Python SDK स्थापना गर्नुहोस्:**

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework लाई आफ्नो स्थानीय मोडेलमा निर्देशन गर्नुहोस्:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# मोडेललाई आवश्यक परेमा डाउनलोड गरी स्थानीय रूपमा सेवा गर्दछ, त्यसपछि अन्त्यबिन्दु/पोर्ट पत्ता लगाउँछ।
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # जस्तै http://localhost:<port>/v1
    api_key=manager.api_key,        # Foundry Local का लागि सधैं "आवश्यक छैन" हुन्छ।
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **नोट:** Foundry Local OpenAI-सँग मेल खाने **Chat Completions** endpoint प्रदान गर्दछ। यसलाई स्थानीय विकास र अफलाइन अवस्थाहरूमा प्रयोग गर्नुहोस्। पूर्ण **Responses API** सुविधाहरू (स्टेटफुल कुराकानीहरू, गहिरो उपकरण समन्वय, र एजेन्ट शैली विकास) को लागि पाठहरूमा देखाइएको जस्तो **Azure OpenAI** वा **Microsoft Foundry** प्रोजेक्ट प्रयोग गर्नुहोस्। हालको मोडेल क्याटलग र प्लेटफर्म समर्थनको लागि [Foundry Local documentation](https://foundrylocal.ai) हेर्नुहोस्।

## पाठ ८ (Bing Grounding Workflow) का लागि अतिरिक्त सेटअप


पाठ ८ मा सर्तसापेक्षित वर्कफ्लो नोटबुकले Microsoft Foundry मार्फत **Bing ग्राउन्डिंग** प्रयोग गर्दछ। यदि तपाईं त्यो नमूना चलाउने योजना बनाउँदै हुनुहुन्छ भने, आफ्नो `.env` फाइलमा यो भेरिएबल थप्नुहोस्:

| भेरिएबल | कहाँ फेला पार्ने |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry पोर्टल → तपाईंको प्रोजेक्ट → **Management** → **Connected resources** → तपाईंको Bing कनेक्शन → कनेक्शन ID कपी गर्नुहोस् |

## समस्या समाधान

### macOS मा SSL प्रमाणपत्र प्रमाणीकरण त्रुटिहरू

यदि तपाईं macOS मा हुनुहुन्छ र यस्तो त्रुटि आएको छ:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

यो macOS मा पाइथनसँग परिचित समस्या हो जहाँ सिस्टम SSL प्रमाणपत्रहरू स्वचालित रूपमा भरोसायोग्य हुँदैनन्। तलका समाधानहरू क्रमशः प्रयास गर्नुहोस्:

**विकल्प १: पाइथनको Install Certificates स्क्रिप्ट चलाउनुहोस् (सिफारिस गरिएको)**

```bash
# तपाईंले स्थापना गर्नुभएको Python संस्करण (जस्तै, 3.12 वा 3.13) सँग 3.XX प्रतिस्थापन गर्नुहोस्:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**विकल्प २: तपाइँको नोटबुकमा `connection_verify=False` प्रयोग गर्नुहोस् (Github मोडलहरूका नोटबुकहरूका लागि मात्र)**

पाठ ६ को नोटबुकमा (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), एक कमेन्ट गरिएको समाधान पहिले नै समावेश छ। क्लाइंट बनाउँदा `connection_verify=False` लाई अनकमेन्ट गर्नुहोस्:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # प्रमाणपत्र त्रुटिहरू आएमा SSL प्रमाणीकरण निष्क्रिय गर्नुहोस्
)
```

> **⚠️ चेतावनी:** SSL प्रमाणीकरण बन्द गर्दा (`connection_verify=False`) प्रमाणपत्र प्रमाणीकरण नछोइकन सुरक्षा कम हुन्छ। यसलाई विकास वातावरणमा अस्थायी समाधानको रूपमा मात्र प्रयोग गर्नुहोस्, कहिल्यै उत्पादनमा होइन।

**विकल्प ३: `truststore` इन्स्टल र प्रयोग गर्नुहोस्**

```bash
pip install truststore
```

त्यसपछि नेटवर्क कल गर्ने अघि आफ्नो नोटबुक वा स्क्रिप्टको सुरुमै निम्न थप्नुहोस्:

```python
import truststore
truststore.inject_into_ssl()
```

## कतै अटकलमा पर्‍यो?

यदि तपाईंलाई यो सेटअप चलाउन कुनै समस्या छ भने, हाम्रो <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> मा जानुहोस् वा <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">एक समस्या सिर्जना गर्नुहोस्</a>।

## अर्को पाठ

अब तपाईं यस कोर्षका लागि कोड चलाउन तयार हुनुहुन्छ। AI एजेन्टहरूको संसारबारे थप सिक्न शुभकामना!

[AI एजेन्टहरू र एजेन्ट उपयोग मामिलाहरूको परिचय](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->