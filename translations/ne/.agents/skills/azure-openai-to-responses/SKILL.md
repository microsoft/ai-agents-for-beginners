---
name: azure-openai-to-responses
license: MIT
---
# Azure OpenAI Chat Completions बाट Responses API मा Python अनुप्रयोगहरू माइग्रेसन गर्नुहोस्

> **अधिकारिक मार्गदर्शन — ठ्याक्कै पालन गर्नुहोस्**
>
> यो स्किलले Python कोडबेसहरूलाई Azure OpenAI Chat Completions बाट
> संयुक्त Responses API तर्फ माइग्रेसन गर्छ। यी निर्देशनहरू ठीकसँग पालन गर्नुहोस्।
> प्यारामिटर म्यापिङहरू आफैं सुधार नगर्नुहोस् वा API आकृतिहरू आविष्कार नगर्नुहोस्।

---

## ट्रिगरहरू

प्रयोगकर्ताले चाहेको बेला यो स्किल सक्रिय गर्नुहोस्:
- Azure OpenAI Chat Completions बाट Responses API मा Python अनुप्रयोग माइग्रेसन गर्न
- Azure OpenAI विरुद्ध Python OpenAI SDK प्रयोगलाई नवीनतम API आकृति तर्फ अपग्रेड गर्न
- Azure मा Responses आवश्यक पर्ने GPT-5 वा नयाँ मोडेलहरूको लागि Python कोड तयार पार्न
- `AzureOpenAI`/`AsyncAzureOpenAI` बाट मानक `OpenAI`/`AsyncOpenAI` क्लाइन्टसँग v1 अन्तबिन्दुमा सर्न
- `AzureOpenAI` निर्माणकर्ता वा `api_version` सम्बन्धी अवमूल्यन चेतावनीहरू समाधान गर्न

---

## ⚠️ मोडेल अनुकूलता — पहिले जाँच्नुहोस्

> **माइग्रेसन गर्नु अघि, तपाइँको Azure OpenAI डिप्लोयमेन्टले Responses API समर्थन गर्दछ भनी पुष्टि गर्नुहोस्।**

### 1. तपाइँको डिप्लोयमेन्टको स्मोक टेस्ट (सबैभन्दा छिटो)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **नोट**: Azure OpenAI मा `max_output_tokens` को **न्यूनतम 16** छ। 16 भन्दा तलका मानहरूले 400 त्रुटि फर्काउँछन्। स्मोक परीक्षणका लागि 50+ प्रयोग गर्नुहोस्।

यदि यसले 404 फर्काउँछ भने, डिप्लोयमेन्टको मोडेलले अझै Responses समर्थन गर्दैन — तल दिइएको सन्दर्भ जाँच्नुहोस् वा समर्थन गरिएको मोडेलसँग पुन: डिप्लोय गर्नुहोस्।

### 2. तपाइँको क्षेत्रका उपलब्ध मोडेलहरू जाँच्नुहोस् (सिफारिस गरिएको)

बुझेको टूल प्रयोग गरेर तपाइँको विशिष्ट क्षेत्रमा Responses API समर्थन गर्ने मोडेलहरू हेर्नुहोस्:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

यसले Azure ARM लाई प्रत्यक्ष सोध्छ र अनुकूलता म्याट्रिक्स देखाउँछ — कुन मोडेलहरूले Responses, संरचित आउटपुट, उपकरणहरू आदि समर्थन गर्छन्। `--filter gpt-5.1,gpt-5.2` प्रयोग गरेर नतिजा सिमित गर्नुहोस् वा scripting का लागि `--json`।

### 3. पूर्ण मोडेल समर्थन सन्दर्भ

- **प्रत्यक्ष सोधपुछ**: `python migrate.py models` (माथि हेर्नुहोस् — क्षेत्र-विशिष्ट, सँधै अद्यावधिक)
- **उपलब्धता ब्राउज गर्नुहोस्**: [मोडेल सारांश तालिका र क्षेत्र उपलब्धता](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **सुरुवात र मार्गदर्शन**: **https://aka.ms/openai/start**

### ⚠️ पुराना मोडेल सीमाहरू

> **चेतावनी**: पुराना मोडेलहरू (जसले `gpt-4.1` भन्दा पहिले बनेका हुन्) सबै Responses API सुविधाहरू पूर्ण रूपमा समर्थन नगर्न सक्छन्।
>
> पुराना मोडेलसँग ज्ञात सीमाहरू:
> - **`reasoning` प्यारामिटर**: धेरै गैर-रिजनिंग मोडेलहरूमा समर्थन छैन। मात्र तिनीहरूलाई माइग्रेट गर्नुहोस् जुन पहिले नै कोडमा थियो।
> - **`seed` प्यारामिटर**: Responses API मा पूर्ण रूपमा समर्थन छैन — सबै अनुरोधबाट हटाउनुहोस्।
> - **`text.format` मार्फत संरचित आउटपुट**: पुराना मोडेलहरूले `strict: true` JSON schemas रeliably जाँच नहुन सक्छन्।
> - **उपकरण समन्वय**: GPT-5+ ले आन्तरिक reasoning को भागका रूपमा उपकरण कलहरू समन्वय गर्छ। Responses मा पुराना मोडेलहरूले काम गर्छन् तर गहिरो समाकलन छैन।
> - **तापमान सीमा**: `gpt-5` मा माइग्रेसन गर्दा तापमान छुट्टै राख्नुहोस् वा `1` मा सेट गर्नुहोस्। पुराना मोडेलमा यस्तो सीमा छैन।

### O-श्रृंखला reasoning मोडेलहरू (o1, o3-mini, o3, o4-mini)

O-श्रृंखला मोडेलहरूसँग विशिष्ट प्यारामिटर सीमाहरू छन्। जब यी लक्षित गरी एप्स माइग्रेसन गर्ने हो:

- **`temperature`**: `1` हुनुपर्छ (वा छुट्ट्याउनुहोस्)। O-श्रृंखला मोडेलहरूले अन्य मानहरू स्वीकार गर्दैनन्।
- **`max_completion_tokens` → `max_output_tokens`**: Azure-विशिष्ट `max_completion_tokens` प्रयोग गर्ने एपहरूले `max_output_tokens` मा सर्नुपर्छ। reasoning टोकनहरू सीमालाई असर गर्छन् त्यसैले उच्च मान (4096+) सेट गर्नुहोस्।
- **`reasoning_effort`**: यदि एपले `reasoning_effort` (low/medium/high) प्रयोग गरेको छ भने राख्नुहोस् — Responses API ले यो O-श्रृंखलाहरूको लागि समर्थन गर्दछ।
- **स्ट्रीमिङ व्यवहार**: O-श्रृंखला मोडेलहरूले reasoning पूरा हुनुअघि आउटपुट बफर गर्न सक्छन् र पछि delta घटना पठाउँछन्। स्ट्रीमिङले अझै काम गर्छ, तर पहिलो `response.output_text.delta` ढिलो आउन सक्छ GPT मोडेलहरूको भन्दा।
- **`top_p`**: O-श्रृंखला मा समर्थन छैन — यदि छ भने हटाउनुहोस्।
- **उपकरण प्रयोग**: O-श्रृंखला मोडेलहरूले GPT मोडेलहरू झैँ Responses API मार्फत उपकरण समर्थन गर्छन् तर उपकरण कल समन्वय गुणस्तर मोडेल अनुसार फरक हुन्छ।

**कार्य — सक्रिय मोडेल सल्लाह:** स्क्यान चरणमा, एपले कुन मोडेल लक्षित गरेको छ (डिप्लोयमेन्ट नाम, env var, config) जाँच्नुहोस्। यदि मोडेल `gpt-4.1` भन्दा पुरानो छ भने प्रयोगकर्तालाई सक्रिय रूपमा भन्नुहोस्:
- माइग्रेसन मौलिक पाठ, च्याट, स्ट्रीमिङ, र उपकरणहरूका लागि हालको मोडेलमा काम गर्ने छ।
- नयाँ मोडेलहरूले (`gpt-5.1`, `gpt-5.2`) राम्रो उपकरण समन्वय, संरचित आउटपुट, reasoning, र क्षेत्रीय उपलब्धता प्रदान गर्छन्।
- तिनीहरूले तयार हुँदा डिप्लोयमेन्ट अपग्रेड गर्नु उचित हुन्छ — माइग्रेसन रोक्ने छैन।

मोडेल संस्करणका आधारमा माइग्रेसन रोक्नुहोस् वा अस्वीकार नगर्नुहोस्। सल्लाह जानकारीमूलक मात्र हो।

### GitHub मोडेलहरूले Responses API समर्थन गर्दैनन्

> **GitHub मोडेलहरू (`models.github.ai`, `models.inference.ai.azure.com`) Responses API समर्थन गर्दैनन्।**

यदि कोडबेसमा GitHub मोडेलको कोड पथ छ भने (`base_url` `models.github.ai` वा `models.inference.ai.azure.com` लाई संकेत गर्छ), माइग्रेसनका क्रममा **यो पूर्ण रूपमा हटाउनुहोस्**। Responses API लाई Azure OpenAI, OpenAI, वा अनुकूल स्थानीय अन्तबिन्दु (जस्तै, Responses समर्थित Ollama) आवश्यक हुन्छ।

स्क्यान गर्दा कार्रवाईहरू:
- कुनै पनि GitHub मोडेल कोड पथलाई हटाउन झण्डा लगाउनुहोस्।

---

## फ्रेमवर्क माइग्रेसन

धेरै एप्सले OpenAI माथि उच्च-स्तरीय फ्रेमवर्कहरू प्रयोग गर्छन्। यी माइग्रेसन गर्दा, फ्रेमवर्कको आफ्नै API परिवर्तन हुन्छ — केवल आधारभूत OpenAI कल मात्र होइन।

### Microsoft एजेन्ट फ्रेमवर्क (MAF)

**पहिले आफ्नो MAF संस्करण जाँच्नुहोस्** — माइग्रेसन MAF 1.0.0+ वा पूर्व 1.0.0 बीटा/RC मा निर्भर छ।

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **पहिले नै Responses API प्रयोग गर्दछ** — माइग्रेसन आवश्यक छैन। यदि कोडबेस पुरानो `OpenAIChatCompletionClient` (`chat.completions.create` प्रयोग गर्ने) प्रयोग गर्छ भने, यसलाई `OpenAIChatClient` ले प्रतिस्थापन गर्नुहोस्।

| पहिले | पछि |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

आफ्नो संस्करण जाँच्न: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF पूर्व 1.0.0 (बीटा/RC रिलिजहरू)

पूर्व 1.0.0 MAF मा, `OpenAIChatClient` ले Chat Completions प्रयोग गर्थ्यो। `agent-framework-openai>=1.0.0` मा अपग्रेड गर्नुहोस् जहाँ `OpenAIChatClient` डिफल्ट रूपमा Responses API प्रयोग गर्दछ।

अन्य परिवर्तन आवश्यक छैन — `Agent` र उपकरण API हरू उस्तै रहन्छन्।

### LangChain (`langchain-openai`)

`ChatOpenAI()` मा `use_responses_api=True` थप्नुहोस्। साथै प्रतिक्रियाको पहुँच `.content` बाट `.text` मा अपडेट गर्नुहोस्।

| पहिले | पछि |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

पूर्ण पहिले/पछि कोड उदाहरणहरूका लागि [cheat-sheet.md](./references/cheat-sheet.md) हेर्नुहोस्।

---

## फ्रन्टएण्ड माइग्रेसन मार्गदर्शन

> **Responses API एक सर्भर-पक्षीय विषय हो।** आफ्नो Python ब्याकएण्ड माइग्रेसन गर्नुहोस्; फ्रन्टएण्डको HTTP सम्झौता परिवर्तन नगर्नुहोस् जबसम्म तपाईंको ब्याकएण्ड एउटा साधारण पास-थ्रू नभएको हो — त्यो केसमा Responses अनुरोध आकृति अपनाउन विचार गर्नुहोस् जसले अनुवाद तह हटाउँछ। यदि फ्रन्टएण्डले क्लाइन्ट-साइड कुञ्जी प्रयोग गरेर सिधै OpenAI कल गर्छ भने ती कलहरू पहिले ब्याकएण्डमा सार्नुहोस्।

### `@microsoft/ai-chat-protocol` अवमूल्यन

`@microsoft/ai-chat-protocol` npm प्याकेज अवमूल्यन गरिएको छ र [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) सँग परिवर्तन गर्नुहोस्। यदि फ्रन्टएण्डमा पाइयो भने:

1. CDN स्क्रिप्ट ट्याग प्रतिस्थापन गर्नुहोस्:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` को उत्पत्तिलाई हटाउनुहोस् (`new ChatProtocol.AIChatProtocolClient("/chat")`)।
3. `client.getStreamedCompletion(messages)` लाई सिधा ब्याकएण्ड स्ट्रीमिङ अन्तबिन्दुमा `fetch()` कलले प्रतिस्थापन गर्नुहोस्।
4. `for await (const response of result)` लाई `for await (const chunk of readNDJSONStream(response.body))` मा परिवर्तन गर्नुहोस्।
5. सम्पत्ति पहुँच `response.delta.content` / `response.error` बाट `chunk.delta.content` / `chunk.error` मा अपडेट गर्नुहोस्।

---

## लक्ष्यहरू

- Azure OpenAI विरुद्ध Chat Completions वा पुरानो Completions प्रयोग गर्ने सबै Python कल साइटहरू गनेर निर्धारण गर्नुहोस्।
- Python कोडबेसका लागि माइग्रेसन योजना र अनुक्रम प्रस्ताव गर्नुहोस्।
- Responses API मा सर्न सुरक्षित, न्यूनतम सम्पादनहरू लागू गर्नुहोस्।
- प्रतिक्रियाको आउटपुट योजना प्रयोग गर्न कलरहरू अपडेट गर्नुहोस्; कुनै पछाडिको अनुकूलता आवरण छैन।
- परीक्षण/लिन्ट गर्नुहोस्; माइग्रेसनबाट आएको साना भंगहरू सन्चालन गर्नुहोस्।
- साना, समीक्षा योग्य परिवर्तन सेट तयार गर्नुहोस् र भिन्नताहरू सहित अन्तिम सारांश दिनुहोस् (कमिट नगर्नुहोस्)।

---

## संरक्षक नियमहरू

- केवल git कार्यक्षेत्र भित्रका फाइलहरू परिवर्तन गर्नुहोस्। बाहिर कहिल्यै नलेख्नुहोस्।
- पछाडिको अनुकूलता ढाँचा राख्नुहोस् नगर्नुहोस्; नयाँ API आकृतिमा कोड माइग्रेसन गर्नुहोस्।
- टुम्बस्टोन/रूपान्तरण टिप्पणी वा ब्याकअप फाइलहरू नछोड्नुहोस्।
- पहिले प्रयोग भएको भए स्ट्रीमिङ अर्थ कायम राख्नुहोस्; अन्यथा गैर-स्ट्रीमिङ प्रयोग गर्नुहोस्।
- अनुमोदन मोडमा कमाण्ड वा नेटवर्क कलहरू अघि अनुमोदन माग्नुहोस्।
- `git add`/`git commit`/`git push` नचलाउनुहोस्; केवल कार्यकारी पेड़ सम्पादन उत्पादन गर्नुहोस्।

---

## चरण 0: Azure OpenAI क्लाइन्ट माइग्रेसन (पूर्वापेक्षित)

यदि कोडबेसले `AzureOpenAI` वा `AsyncAzureOpenAI` निर्माणकर्ता प्रयोग गरेको छ भने, पहिले मानक `OpenAI` / `AsyncOpenAI` निर्माणकर्तामा माइग्रेसन गर्नुहोस्। Azure-विशिष्ट निर्माणकर्ताहरू `openai>=1.108.1` मा अवमूल्यन भइसकेका छन्।

### किन v1 API पथ?

नयाँ `/openai/v1` अन्तबिन्दुले मानक `OpenAI()` क्लाइन्ट प्रयोग गर्छ, `AzureOpenAI()` होइन, कुनै `api_version` प्यारामिटर आवश्यक छैन, र OpenAI तथा Azure OpenAI मा समान रूपमा काम गर्छ। एउटै क्लाइन्ट कोड भविष्य-अनुकूल छ — संस्करण व्यवस्थापन आवश्यक छैन।

### मुख्य परिवर्तनहरू

| पहिले | पछि |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | पूर्ण रूपमा हटाउनुहोस् |

### सफाई कार्य सूची

- क्लाइन्ट निर्माणबाट `api_version` प्यारामिटर हटाउनुहोस्।
- `.env`, एप सेटिङहरू, र Bicep/इन्फ्रास्ट्रक्चर फाइलहरूबाट `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` वातावरण भेरिएबलहरू हटाउनुहोस्।
- `.env`, एप सेटिङहरू, Bicep/इन्फ्रास्ट्रक्चर, र परीक्षण फिक्स्चरहरूमा `AZURE_OPENAI_CLIENT_ID` लाई `AZURE_CLIENT_ID` मा नाम परिवर्तन गर्नुहोस् (मानक Azure Identity SDK विधान)।
- `requirements.txt` वा `pyproject.toml` मा `openai>=1.108.1` सुनिश्चित गर्नुहोस्।

### वातावरण भेरिएबल माइग्रेसन

| पुरानो env var | कार्य | नोटहरू |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **हटाउनुहोस्** | v1 अन्तबिन्दुसँग `api_version` आवश्यक छैन |
| `AZURE_OPENAI_API_VERSION` | **हटाउनुहोस्** | माथिको जस्तै |
| `AZURE_OPENAI_CLIENT_ID` | **नाम परिवर्तन** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)` को लागि मानक Azure Identity SDK विधान |
| `AZURE_OPENAI_ENDPOINT` | **राख्नुहोस्** | अझै `base_url` निर्माणका लागि आवश्यक |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **राख्नुहोस्** | `responses.create` मा `model` प्यारामिटरको रूपमा प्रयोग हुन्छ |
| `AZURE_OPENAI_API_KEY` | **राख्नुहोस्** | कुञ्जी-आधारित प्रमाणीकरणमा `api_key` रूपमा प्रयोग हुन्छ |

क्लाइन्ट सेटअप कोड उदाहरणहरूका लागि (समक्रमित, असमक्रमित, EntraID, API कुञ्जी, बहु-टेनेन्ट), [cheat-sheet.md](./references/cheat-sheet.md) हेर्नुहोस्।

---

## चरण 1: पुराना कल साइटहरू पत्ता लगाउनुहोस्

माइग्रेसन आवश्यक सबै कल साइटहरू भेट्न [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) स्क्रिप्ट चलाउनुहोस्:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

वा यी खोजहरू म्यानुअल रूपमा चलाउनुहोस् — प्रत्येक मिल्दोजुल्दो माइग्रेसन लक्ष्य हो:

```bash
# पुरानो API कलहरू (पुनर्लेखन गर्नै पर्छ)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# अप्रचलित Azure क्लाइन्ट निर्माणकर्ता (प्रतिस्थापन गर्नै पर्छ)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# प्रतिक्रिया आकृति पहुँच ढाँचा (अद्यावधिक गर्नै पर्छ)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# उपकरण परिभाषाहरू पुरानो नेस्टेड ढाँचामा (साधारण बनाउनुपर्छ)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# उपकरण परिणामहरू पुरानो ढाँचामा (function_call_output मा रूपान्तरण गर्नै पर्छ)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# अप्रचलित प्यारामिटरहरू (हटाउन वा नाम परिवर्तन गर्नै पर्छ)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens मा नाम परिवर्तन गर्नुहोस्
rg "['\"]seed['\"]"      # remove entirely

# अप्रचलित वातावरण भेरिएबलहरू (सफा गर्नुहोस्)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID हुनुपर्छ

# GitHub मोडेलहरू अन्तबिन्दुहरू (हटाउनै पर्छ — Responses API समर्थित छैन)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# फ्रेमवर्क स्तरको पुरानो ढाँचा (अद्यावधिक गर्नै पर्छ)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient सँग प्रतिस्थापन गर्नुहोस्
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True आवश्यक छ

# परीक्षण पूर्वाधार (अद्यावधिक गर्नै पर्छ)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# सामग्री फिल्टर त्रुटि बडी पहुँच (अद्यावधिक गर्नै पर्छ — संरचना परिवर्तन भएको छ)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # पुरानो एकवचन रूप — अहिले content_filter_results (बहुवचन) content_filters एरे भित्र छ

# Chat Completions अन्तबिन्दुमा कच्चा HTTP कलहरू (URL अद्यावधिक गर्नै पर्छ)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### सिद्धान्तहरू (पत्ता लगाउने र पुनःलेखन)

- **Chat Completions क्लाइन्ट**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure क्लाइन्ट कन्स्ट्रक्टरहरू**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **टूलहरू**: फंक्शन-कलिङ टूल निर्धारणलाई नेस्टेड ढाँचा (`{"type": "function", "function": {"name": ...}}`) बाट फ्ल्याट Responses ढाँचामा (`{"type": "function", "name": ...}`) रूपान्तरण गर्नुहोस्; `tool_choice` प्रयोग गर्नुहोस्; टूल परिणामहरूलाई `{"type": "function_call_output", "call_id": ..., "output": ...}` वस्तुहरूका रूपमा फर्काउनुहोस् ( `{"role": "tool", ...}` होइन)।
- **टूल राउन्ड-ट्रिपहरू**: मोडेलले फंक्शन कलहरू फिर्ता गर्दा, कन्भर्सेशनमा `response.output` वस्तुहरू थप्नुहोस् (म्यानुअल `{"role": "assistant", "tool_calls": [...]}` डिक्ट होइन), त्यसपछि प्रत्येक परिणामका लागि `function_call_output` वस्तुहरू थप्नुहोस्।
- **थोरै-शट टूल उदाहरणहरू**: यदि कन्भर्सेशनमा हार्डकोडेड टूल कल उदाहरणहरू छन् भने, तिनीहरूलाई `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` वस्तुहरूमा रूपान्तरण गर्नुहोस्। IDs कम्तिमा `fc_` बाट सुरु हुनुपर्छ।
- **`pydantic_function_tool()`**: यो सहायक अझै पुरानो नेस्टेड ढाँचा उत्पन्न गर्दछ र `responses.create()` सँग उपयुक्त छैन। यसलाई म्यानुअल टूल परिभाषाहरू वा फ्ल्याटेनिङ र्यापरले प्रतिस्थापन गर्नुहोस्।
- **मल्टि-टर्न**: एपमा कन्भर्सेशन इतिहास कायम गर्नुहोस्; अघिल्ला टर्नहरू `input` वस्तुहरूमार्फत पास गर्नुहोस्।
- **फर्म्याटिङ**: Chat को शीर्ष-स्तरीय `response_format` लाई Responses मा `text.format` ले प्रतिस्थापन गर्नुहोस्। क्यानोनिकल ढाँचा: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`।
- **कन्टेन्ट वस्तुहरू**: Chat को `content[].type: "text"` लाई Responses मा `content[].type: "input_text"` प्रयोग गरेर प्रयोगकर्ता/सिस्टम टर्नहरूका लागि प्रतिस्थापन गर्नुहोस्।
- **छवि कन्टेन्ट वस्तुहरू**: Chat को `content[].type: "image_url"` लाई Responses मा `content[].type: "input_image"` मा प्रतिस्थापन गर्नुहोस्। `image_url` फिल्ड नेस्टेड वस्तु `{"url": "..."}` बाट फ्ल्याट स्ट्रिङमा बदलिन्छ। पहिले/पछि उदाहरणहरूको लागि चिट शीट हेर्नुहोस्।
- **तर्क गर्ने प्रयास**: **केवल तब मात्र `reasoning` माइगरेट गर्नुहोस् यदि यो मूल कोडमा पहिले नै छ भने**।
- **कन्टेन्ट फिल्टर त्रुटि ह्यान्डलिङ**: त्रुटि संरचना परिवर्तन भयो। Chat Completions ले `error.body["innererror"]["content_filter_result"]` (एकल) प्रयोग गर्थ्यो; Responses API ले `error.body["content_filters"][0]["content_filter_results"]` (बहु, एर्रे भित्र) प्रयोग गर्छ। `innererror` पहुँच गर्ने कोड `KeyError` ल्याउनेछ। नयाँ पथ प्रयोग गरेर पुनर्लेखन गर्नुहोस्।
- **Raw HTTP कलहरू**: यदि एपले Azure OpenAI REST API लाई सिधै (requests, httpx आदि मार्फत) `/openai/deployments/{name}/chat/completions?api-version=...` endpoint मार्फत कल गर्दछ भने, यसलाई `/openai/v1/responses` मा पुनर्लेखन गर्नुहोस्। अनुरोध बडी परिवर्तन हुन्छ: `messages` → `input`, `max_output_tokens` थप्नुहोस् र `store: false` राख्नुहोस्, `api-version` क्वेरी प्याराम हटाउनुहोस्। प्रतिक्रिया बडी परिवर्तन हुन्छ: `choices[0].message.content` → `output[0].content[0].text` ( नोट: `output_text` SDK सुविधा हो जुन कच्चा REST JSON मा हुँदैन)।

---

## कदम २: माइग्रेशन लागू गर्नुहोस्

### माइग्रेशन नोटहरू (Chat Completions → Responses)

- **किन माइग्रेट गर्ने**: Responses पाठ, टूलहरू, र स्ट्रीमिङका लागि एकीकृत API हो; Chat Completions पुरानो छ। GPT-5 सँग, उत्तम प्रदर्शनका लागि Responses आवश्यक छ।
- **HTTP**: Azure endpoint `/openai/deployments/{name}/chat/completions` बाट `/openai/v1/responses` मा सर्नुहोस्।
- **फिल्डहरू**: `messages` → `input`, `max_tokens` → `max_output_tokens`। `temperature` अपरिवर्तित रहन्छ।
- **फर्म्याटिङ**: `response_format` → `text.format` (सही वस्तु सहित)।
- **कन्टेन्ट वस्तुहरू**: Chat को `content[].type: "text"` लाई Responses मा `content[].type: "input_text"` ले प्रतिस्थापन गर्नुहोस्।
- **छवि कन्टेन्ट वस्तुहरू**: Chat को `content[].type: "image_url"` लाई Responses मा `content[].type: "input_image"` मा प्रतिस्थापन गर्नुहोस्। `image_url` फिल्ड `{"image_url": {"url": "..."}}` बाट `{"image_url": "..."}` (सादा स्ट्रिङ — HTTPS URL वा `data:image/...;base64,...` डेटा URI) मा परिवर्तन गर्नुहोस्।

### प्यारामिटर म्यापिङ सन्दर्भ

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (वस्तुहरूको एर्रे) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (वस्तु) |
| `temperature` | `temperature` (परिवर्तित छैन) |
| `stop` | `stop` (परिवर्तित छैन) |
| `frequency_penalty` | `frequency_penalty` (परिवर्तित छैन) |
| `presence_penalty` | `presence_penalty` (परिवर्तित छैन) |
| `tools` / function-calling | `tools` (परिवर्तित छैन) |
| `seed` | **हटाउनुहोस्** (समर्थित छैन) |
| `store` | `store` (`false` मा सेट गर्नुहोस्) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (फ्ल्याट स्ट्रिङ) |

पूर्ण अघि/पछिका कोड उदाहरणहरूको लागि [cheat-sheet.md](./references/cheat-sheet.md) हेर्नुहोस्।

परीक्षण पूर्वाधार माइग्रेशन (मकहरू, स्न्यापशटहरू, पुष्टि) का लागि [test-migration.md](./references/test-migration.md) हेर्नुहोस्।

समस्याहरू र खतराहरूको लागि [troubleshooting.md](./references/troubleshooting.md) हेर्नुहोस्।

---

## डाटा अख्तियारी र अवस्था

- सबै Responses अनुरोधहरूमा `store: false` सेट गर्नुहोस्।
- अघिल्लो म्यासेज ID वा सर्भरमा राखिएको सन्दर्भमा निर्भर नहुनुहोस्; अवस्था क्लाइन्ट-व्यवस्थापनमा राख्नुहोस् र मेटाडाटा कम गर्नुहोस्।

---

## स्वीकृति मापदण्डहरू

### कोड-स्तरका गेटहरू (सबै पास हुनुपर्छ)

- [ ] माइग्रेट गरिएका फाइलहरूमा `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` को लागि शून्य मिलानहरू।
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` का लागि शून्य मिलानहरू — सबै कन्स्ट्रक्टरहरू `OpenAI`/`AsyncOpenAI` र v1 endpoint प्रयोग गर्छन्।
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` का लागि शून्य मिलानहरू — GitHub मोडेल कोड पथहरु हटाइएका छन्।
- [ ] `rg "OpenAIChatCompletionClient"` का लागि शून्य मिलानहरू — MAF 1.0.0+ कोडले `OpenAIChatClient` प्रयोग गर्छ (जो Responses API प्रयोग गर्छ)। 1.0.0 भन्दा पहिलेको संस्करणमा `agent-framework-openai>=1.0.0` मा अपग्रेड गर्नुहोस्।
- [ ] सबै `ChatOpenAI(...)` कलहरूमा `use_responses_api=True` समावेश छ।
- [ ] `rg "choices\[0\]"` का लागि शून्य मिलानहरू — सबै प्रतिक्रिया पहुँच `resp.output_text` वा Responses आउटपुट स्कीमाले हुन्छ।
- [ ] शीर्ष स्तरमा `response_format` छैन; सबै संरचित आउटपुट `text={"format": {...}}` प्रयोग गर्दछ।
- [ ] `requirements.txt` वा `pyproject.toml` मा `openai>=1.108.1` र `azure-identity` छ; निर्भरता पुनःइंस्टल गरिएको छ।
- [ ] प्रत्येक `responses.create` कलमा `store=False` सेट गरिएको छ।
- [ ] क्लाइन्ट कन्स्ट्रक्शनमा `api_version` छैन; `AZURE_OPENAI_API_VERSION` इन्भाइरनमेन्ट फाइलहरू र पूर्वाधारबाट हटाइएको छ।

### परीक्षण पूर्वाधार गेटहरू (सबै पास हुनुपर्छ)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` का लागि शून्य मिलानहरू।
- [ ] `rg "_azure_ad_token_provider" tests/` का लागि शून्य मिलानहरू — पुष्टि गरियो कि `isinstance(client, AsyncOpenAI)` वा `base_url` जाँच गरिन्छ।
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` का लागि शून्य मिलानहरू — Azure-विशेष फिल्टर मकहरू हटाइएका।
- [ ] मोक फिक्स्चरहरूले `kwargs.get("input")` प्रयोग गर्छन्, `kwargs.get("messages")` होइन।
- [ ] स्न्यापशट/गोल्डेन फाइलहरू Responses स्ट्रीमिङ ढाँचामा अपडेट गरिएका (कुनै `choices[0]`, `function_call`, `logprobs` आदिको प्रयोग छैन)।
- [ ] सबै परीक्षण अपडेटपछि `pytest` शून्य असफलतासँग पास हुन्छ।

### व्यवहारिक गेटहरू (म्यानुअल वा टेस्ट हार्नेस मार्फत जाँच गर्नुहोस्)

- [ ] **मूल पूर्णता**: नन-स्ट्रीमिङ `responses.create` ले खाली नभएको `output_text` फर्काउँछ।
- [ ] **स्ट्रीम समानता**: यदि मूल कोडले स्ट्रीमिङ प्रयोग गर्यो भने, माइग्रेट गरिएको कोडले स्ट्रीमिङ गर्दछ र `response.output_text.delta` घटनाहरू दियेर खाली नभएका डेल्टाहरू उत्पन्न गर्छ।
- [ ] **संरचित आउटपुट**: यदि `text.format` र `json_schema` प्रयोग गरिएको छ भने, `json.loads(resp.output_text)` सफल हुन्छ र स्कीमा मेल खान्छ।
- [ ] **टूल-कल लूप**: यदि टूलहरू प्रयोग भइरहेको छ भने, मोडेलले टूल कलहरू जारी गर्छ, एपले तिनीहरू कार्यान्वयन गर्छ, र पछिल्लो अनुरोध अन्तिम `output_text` (अनन्त लूप छैन) फर्काउँछ।
- [ ] **Async समानता**: यदि `AsyncAzureOpenAI` प्रयोग गरिएको थियो भने, समकक्ष `AsyncOpenAI` ले `await` सँग काम गर्छ।
- [ ] **त्रुटि दर**: पूर्व-माइग्रेशन बेसलाइनसँग तुलना गर्दा नयाँ 400/401/404 त्रुटिहरू छैनन्।

### डेलिभरेबलहरू

- सारांशमा सम्पादित फाइलहरू, पुराना/नयाँ कल साइट सङ्ख्या, र अर्को चरणहरू समावेश हुन्छन्।
- परिवर्तनहरू वर्किङ ट्रीका सम्पादन मात्र छन् (कमिटहरू होइन)।

---

## SDK संस्करण आवश्यकताहरू

| प्याकेज | न्यूनतम संस्करण |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | नवीनतम (EntraID प्रमाणीकरणका लागि) |

---

## सन्दर्भहरू

- [चिट शीट — सबै कोड स्निपेटहरू](./references/cheat-sheet.md)
- [परीक्षण माइग्रेशन — मोकहरू, स्न्यापशटहरू, पुष्टि](./references/test-migration.md)
- [समस्या समाधान — त्रुटिहरू, जोखिम तालिका, खतराहरू](./references/troubleshooting.md)
- [detect_legacy.py — स्वत: स्क्यानर](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI स्टार्टर किट](https://aka.ms/openai/start)
- [Azure OpenAI Responses API डक्स](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API संस्करण जीवनचक्र](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API सन्दर्भ](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->