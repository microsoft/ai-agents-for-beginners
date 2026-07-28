---
name: azure-openai-to-responses
license: MIT
---
# Azure OpenAI चैट पूर्णताओं से Responses API में Python ऐप्स माइग्रेट करें

> **अधिकारिक मार्गदर्शन — ठीक वैसे ही पालन करें**
>
> यह कौशल Python कोडबेस का माइग्रेशन करता है जो Azure OpenAI चैट पूर्णताओं का उपयोग करते हैं
> एकीकृत Responses API में। इन निर्देशों का सटीक पालन करें।
> पैरामीटर मैपिंग में खुद से बदलाव न करें या API के रूप की कल्पना न करें।

---

## ट्रिगर्स

इस स्किल को सक्रिय करें जब उपयोगकर्ता चाहता है:
- Azure OpenAI चैट पूर्णताओं से Responses API में Python ऐप माइग्रेट करना
- Azure OpenAI के विरुद्ध Python OpenAI SDK का उपयोग नवीनतम API आकृति में अपग्रेड करना
- GPT-5 या नए मॉडल के लिए Python कोड तैयार करना जिन्हें Azure पर Responses की आवश्यकता हो
- `AzureOpenAI`/`AsyncAzureOpenAI` से मानक `OpenAI`/`AsyncOpenAI` क्लाइंट के v1 एंडपॉइंट पर स्विच करना
- `AzureOpenAI` कंस्ट्रक्टर या `api_version` से संबंधित डिप्रिकेशन चेतावनियों को ठीक करना

---

## ⚠️ मॉडल संगतता — सबसे पहले जांचें

> **माइग्रेशन से पहले, पुष्टि करें कि आपका Azure OpenAI तैनाती Responses API का समर्थन करता है।**

### 1. अपनी तैनाती का स्मोक-टेस्ट करें (सबसे तेज़)

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

> **नोट**: `max_output_tokens` का Azure OpenAI पर **न्यूनतम 16** है। 16 से कम मानों पर 400 त्रुटि आती है। स्मोक टेस्ट के लिए 50+ का उपयोग करें।

अगर यह 404 लौटाता है, तो तैनाती का मॉडल अभी भी Responses को समर्थन नहीं करता — नीचे संदर्भ जांचें या समर्थित मॉडल के साथ पुनः तैनाती करें।

### 2. अपने क्षेत्र में उपलब्ध मॉडल जांचें (अनुशंसित)

बिल्ट-इन मॉडल संगतता उपकरण चलाएं यह देखने के लिए कि आपके विशिष्ट क्षेत्र में Responses API का समर्थन कौन से मॉडल करते हैं:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

यह Azure ARM लाइव क्वेरी करता है और एक संगतता मैट्रिक्स दिखाता है — कौन से मॉडल Responses, संरचित आउटपुट, टूल्स आदि को समर्थन देते हैं। परिणामों को सीमित करने के लिए `--filter gpt-5.1,gpt-5.2` या स्क्रिप्टिंग के लिए `--json` का उपयोग करें।

### 3. पूर्ण मॉडल समर्थन संदर्भ

- **लाइव क्वेरी**: `python migrate.py models` (ऊपर देखें — क्षेत्र-विशिष्ट, हमेशा अद्यतित)
- **उपलब्धता ब्राउज़ करें**: [मॉडल सारांश तालिका और क्षेत्रीय उपलब्धता](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **क्विकस्टार्ट और मार्गदर्शन**: **https://aka.ms/openai/start**

### ⚠️ पुराने मॉडल सीमाएं

> **चेतावनी**: पुराने मॉडल (`gpt-4.1` से पहले वाले) सभी Responses API विशेषताओं का पूर्ण समर्थन नहीं कर सकते।
>
> पुराने मॉडलों के ज्ञात सीमाएं:
> - **`reasoning` पैरामीटर**: कई गैर-तर्कसंगत मॉडल पर समर्थित नहीं। केवल उन्हीं को माइग्रेट करें जहाँ मूल कोड में `reasoning` पहले से था।
> - **`seed` पैरामीटर**: Responses API में पूरी तरह से समर्थित नहीं — सभी अनुरोधों से हटाएं।
> - **`text.format` के माध्यम से संरचित आउटपुट**: पुराने मॉडल `strict: true` JSON स्कीमा को विश्वसनीय रूप से लागू नहीं कर सकते।
> - **टूल ऑर्केस्ट्रेशन**: GPT-5+ आंतरिक तर्क के हिस्से के रूप में टूल कॉल ऑर्केस्ट्रेशन करता है। पुराने मॉडल Responses पर काम करते हैं लेकिन इस गहराई वाले एकीकरण के बिना।
> - **तापमान प्रतिबंध**: `gpt-5` में माइग्रेट करते समय तापमान या तो हटाएं या `1` सेट करें। पुराने मॉडलों में ऐसा कोई प्रतिबंध नहीं।

### O-सीरीज़ तर्कसंगत मॉडल (o1, o3-mini, o3, o4-mini)

O-सीरीज़ मॉडल की अलग पैरामीटर सीमाएं होती हैं। जब O-सीरीज़ मॉडल को लक्षित करने वाली ऐप्स माइग्रेट करें:

- **`temperature`**: `1` होना चाहिए (या छोड़ा जाए)। O-सीरीज़ मॉडल अन्य मान स्वीकार नहीं करते।
- **`max_completion_tokens` → `max_output_tokens`**: Azure-विशिष्ट `max_completion_tokens` उपयोग करने वाली ऐप को `max_output_tokens` में बदलना चाहिए। उच्च मान (4096+) सेट करें क्योंकि तर्कसंगत टोकन सीमा के विरुद्ध गिने जाते हैं।
- **`reasoning_effort`**: यदि ऐप `reasoning_effort` (निम्न/मध्यम/उच्च) उपयोग करता है, तो इसे रखें — Responses API इस पैरामीटर का O-सीरीज़ मॉडल के लिए समर्थन करता है।
- **स्ट्रीमिंग व्यवहार**: O-सीरीज़ मॉडल आउटपुट को तब तक बफर कर सकते हैं जब तक तर्क समाप्त न हो जाए फिर टेक्स्ट डेल्टा इवेंट्स जारी करें। स्ट्रीमिंग अभी भी काम करती है, लेकिन पहला `response.output_text.delta` GPT मॉडलों की तुलना में विलंब के साथ आ सकता है।
- **`top_p`**: O-सीरीज़ पर समर्थित नहीं — मौजूद होने पर हटा दें।
- **टूल उपयोग**: O-सीरीज़ मॉडल GPT मॉडलों की तरह Responses API के माध्यम से टूल्स का समर्थन करते हैं, लेकिन टूल कॉल ऑर्केस्ट्रेशन की गुणवत्ता मॉडल के अनुसार भिन्न होती है।

**कदम — सक्रिय मॉडल सलाहकार**: स्कैन चरण के दौरान जांचें कि ऐप कौन सा मॉडल लक्षित करता है (तैनाती नाम, पर्यावरण चर, कॉन्फ़िग)। यदि मॉडल `gpt-4.1` से पहले का है (gpt-4.1+ नहीं), तो उपयोगकर्ता को सक्रिय रूप से बताएं:
- माइग्रेशन मौजूदा मॉडल पर बुनियादी टेक्स्ट, चैट, स्ट्रीमिंग, और टूल्स के लिए काम करेगा।
- नए मॉडल (`gpt-5.1`, `gpt-5.2`) बेहतर टूल ऑर्केस्ट्रेशन, संरचित आउटपुट लागूकरण, तर्कसंगता, और क्रॉस-रिजन उपलब्धता प्रदान करते हैं।
- वे जब तैयार हों तो अपनी तैनाती अपग्रेड करने पर विचार करें — यह माइग्रेशन को बाधित नहीं करता।

मॉडल संस्करण के आधार पर माइग्रेशन को ब्लॉक या अस्वीकार न करें। सलाह केवल सूचना प्रदान करने के लिए है।

### GitHub मॉडल Responses API का समर्थन नहीं करते

> **GitHub मॉडल (`models.github.ai`, `models.inference.ai.azure.com`) Responses API को समर्थन नहीं देते।**

यदि कोडबेस में GitHub मॉडल कोड पथ हो (जांचें कि `base_url` `models.github.ai` या `models.inference.ai.azure.com` की ओर इशारा करता हो), तो माइग्रेशन के दौरान इसे **पूरी तरह हटा दें**। Responses API के लिए Azure OpenAI, OpenAI, या संगत लोकल एंडपॉइंट (जैसे Ollama with Responses सपोर्ट) आवश्यक है।

स्कैन के दौरान कार्रवाई:
- GitHub मॉडल कोड पथ को हटाने के लिए चिह्नित करें।

---

## फ्रेमवर्क माइग्रेशन

कई ऐप्स OpenAI के ऊपर उच्च-स्तरीय फ्रेमवर्क का उपयोग करते हैं। जब इन्हें माइग्रेट करें, तो केवल आधार OpenAI कॉल ही नहीं बल्कि फ्रेमवर्क के API भी बदलते हैं।

### Microsoft एजेंट फ्रेमवर्क (MAF)

**पहले अपने MAF संस्करण की जांच करें** — माइग्रेशन इस बात पर निर्भर करता है कि आप MAF 1.0.0+ पर हैं या प्री-1.0.0 बीटा/आरसी पर।

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **पहले से ही Responses API का उपयोग करता है** — माइग्रेशन की जरूरत नहीं। अगर कोडबेस लेगसी `OpenAIChatCompletionClient` (जो `chat.completions.create` का उपयोग करता है) का उपयोग करता है, तो उसे `OpenAIChatClient` से बदलें।

| पहले | बाद में |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

अपने संस्करण की जांच करने के लिए: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF प्री-1.0.0 (बीटा/आरसी रिलीज)

प्री-1.0.0 MAF में, `OpenAIChatClient` चैट पूर्णताओं का उपयोग करता था। `agent-framework-openai>=1.0.0` में अपग्रेड करें जहाँ `OpenAIChatClient` डिफ़ॉल्ट रूप से Responses API का उपयोग करता है।

अन्य कोई बदलाव नहीं चाहिए — `Agent` और टूल APIs वैसे के वैसे ही रहते हैं।

### LangChain (`langchain-openai`)

`ChatOpenAI()` में `use_responses_api=True` जोड़ें। प्रतिक्रिया पहुंच को `.content` से `.text` में अपडेट करें।

| पहले | बाद में |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

पूर्ण पहले/बाद के कोड उदाहरणों के लिए देखें [cheat-sheet.md](./references/cheat-sheet.md)।

---

## फ्रंटेंड माइग्रेशन मार्गदर्शन

> **Responses API एक सर्वर-साइड मामला है।** अपने Python बैकएंड को माइग्रेट करें; फ्रंटेंड का HTTP अनुबंध बिना बदले रहना चाहिए जब तक आपका बैकएंड केवल पतला पास-थ्रू न हो — उस स्थिति में, Responses अनुरोध आकृति को अपनाने पर विचार करें ताकि अनुवाद परत खत्म हो सके। अगर फ्रंटेंड OpenAI को सीधे क्लाइंट-साइड कुंजी के साथ कॉल करता है, तो उन कॉलों को पहले बैकएंड पर स्थानांतरित करें।

### `@microsoft/ai-chat-protocol` डिप्रिकेशन

`@microsoft/ai-chat-protocol` npm पैकेज डिप्रिकेटेड है और इसे [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) से बदलना चाहिए। यदि आप इसे फ्रंटेंड में पाते हैं:

1. CDN स्क्रिप्ट टैग बदलें:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` का इंस्टांसिएशन हटाएं (`new ChatProtocol.AIChatProtocolClient("/chat")`)।
3. `client.getStreamedCompletion(messages)` को सीधे बैकेंड स्ट्रीमिंग एंडपॉइंट के लिए `fetch()` कॉल से बदलें।
4. `for await (const response of result)` को `for await (const chunk of readNDJSONStream(response.body))` से बदलें।
5. `response.delta.content` / `response.error` से प्रॉपर्टी एक्सेस को `chunk.delta.content` / `chunk.error` में अपडेट करें।

---

## लक्ष्य

- Azure OpenAI के विरुद्ध चैट पूर्णताओं या लेगसी पूर्णताओं का उपयोग करने वाले सभी Python कॉल साइट्स गिनें।
- Python कोडबेस के लिए माइग्रेशन योजना और अनुक्रमण प्रस्तावित करें।
- Responses API में स्विच करने के लिए सुरक्षित, न्यूनतम संपादन लागू करें।
- कॉलर्स को Responses आउटपुट स्कीमा उपभोग करने के लिए अपडेट करें; कोई पिछड़ा संगतता रैपर नहीं।
- परीक्षण/लिंट चलाएं; माइग्रेशन से उत्पन्न मामूली टूट-फूट ठीक करें।
- छोटे, समीक्षा योग्य परिवर्तन सेट तैयार करें और अंतिम सारांश डिफ के साथ प्रदान करें (कमिट न करें)।

---

## गार्डरेल

- केवल गिट कार्यक्षेत्र के अंदर फाइलें संशोधित करें। कभी बाहर न लिखें।
- पिछड़ा-संगतता शिम्स को संरक्षित न करें; कोड को नए API रूप में माइग्रेट करें।
- टॉम्बस्टोन/ट्रांजिशन टिप्पणियाँ या बैकअप फाइलें न छोड़ें।
- पहले उपयोग की गई हो तो स्ट्रीमिंग सेमांटिक्स संरक्षित करें; अन्यथा, गैर-स्ट्रीमिंग का उपयोग करें।
- अनुमोदन मोड में कमांड या नेटवर्क कॉल चलाने से पहले अनुमोदन माँगें।
- `git add`/`git commit`/`git push` न चलाएं; केवल वर्किंग-ट्री संपादन उत्पन्न करें।

---

## चरण 0: Azure OpenAI क्लाइंट माइग्रेशन (पूर्वापेक्षित)

यदि कोडबेस में `AzureOpenAI` या `AsyncAzureOpenAI` कंस्ट्रक्टर का उपयोग होता है, तो पहले उन्हें मानक `OpenAI` / `AsyncOpenAI` कंस्ट्रक्टर्स में माइग्रेट करें। Azure-विशिष्ट कंस्ट्रक्टर्स `openai>=1.108.1` में डिप्रिकेटेड हैं।

### v1 API पथ क्यों?

नया `/openai/v1` एंडपॉइंट मानक `OpenAI()` क्लाइंट का उपयोग करता है, `AzureOpenAI()` का नहीं, `api_version` पैरामीटर की जरूरत नहीं होती, और OpenAI तथा Azure OpenAI दोनों में समान काम करता है। वही क्लाइंट कोड भविष्य-सबूत है — संस्करण प्रबंधन की जरूरत नहीं।

### प्रमुख बदलाव

| पहले | बाद में |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | पूरी तरह हटाएं |

### सफाई चेकलिस्ट

- क्लाइंट निर्माण से `api_version` तर्क हटाएं।
- `.env`, ऐप सेटिंग्स, और Bicep/इन्फ्रा फाइलों से `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` पर्यावरण चर हटाएं।
- `.env`, ऐप सेटिंग्स, Bicep/इन्फ्रा, और परीक्षण फिक्स्चर में `AZURE_OPENAI_CLIENT_ID` को `AZURE_CLIENT_ID` में रिनेम करें (मूल Azure Identity SDK कन्वेंशन)।
- `requirements.txt` या `pyproject.toml` में `openai>=1.108.1` सुनिश्चित करें।

### पर्यावरण चर माइग्रेशन

| पुराना env var | कार्रवाई | नोट्स |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **हटाएं** | v1 एंडपॉइंट के साथ `api_version` की ज़रूरत नहीं |
| `AZURE_OPENAI_API_VERSION` | **हटाएं** | ऊपर जैसा ही |
| `AZURE_OPENAI_CLIENT_ID` | **रिनेम करें** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)` के लिए मानक Azure Identity SDK कन्वेंशन |
| `AZURE_OPENAI_ENDPOINT` | **रखें** | अभी भी `base_url` निर्माण के लिए जरूरी |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **रखें** | `responses.create` में `model` पैरामीटर के रूप में उपयोग किया जाता है |
| `AZURE_OPENAI_API_KEY` | **रखें** | कुंजी-आधारित प्रमाणीकरण के लिए `api_key` के रूप में उपयोग किया जाता है |

क्लाइंट सेटअप कोड उदाहरणों (सिंक्रोनस, असिंक्रोनस, EntraID, API की, मल्टी-टेनेंट) के लिए देखें [cheat-sheet.md](./references/cheat-sheet.md)।

---

## चरण 1: लेगसी कॉल साइट्स का पता लगाएं

माइग्रेशन की जरूरत वाले सभी कॉल साइट्स खोजने के लिए [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) स्क्रिप्ट चलाएं:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

या मैन्युअली इन खोजों को चलाएं — हर मैच माइग्रेशन लक्ष्य होता है:

```bash
# पुरानी API कॉल (पुनः लिखनी होगी)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# बंद किए गए Azure क्लाइंट कंस्ट्रक्टर (बदलना होगा)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# प्रतिक्रिया आकार पहुंच पैटर्न (अद्यतन करना होगा)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# पुराने नेस्टेड प्रारूप में टूल परिभाषाएँ (सादा करना होगा)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# पुराने प्रारूप में टूल परिणाम (function_call_output में बदलना होगा)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# बंद किए गए पैरामीटर (हटाना या नाम बदलना होगा)
rg "response_format"
rg "max_tokens\b"        # अधिकतम आउटपुट टोकन के लिए नाम बदलें
rg "['\"]seed['\"]"      # remove entirely

# बंद किए गए वातावरण वेरिएबल (साफ़ करें)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID होना चाहिए

# GitHub मॉडल एंडपॉइंट (हटाना होगा — Responses API समर्थित नहीं है)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# फ्रेमवर्क-स्तरीय पुरानी पैटर्न (अद्यतन करना होगा)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient से बदलें
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True आवश्यक है

# परीक्षण अवसंरचना (अद्यतन करना होगा)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# कंटेंट फ़िल्टर त्रुटि बॉडी एक्सेस (अद्यतन करना होगा — संरचना बदल गई है)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # पुराना एकवचन रूप — अब content_filters ऐरे के अंदर content_filter_results (बहुवचन)

# Chat Completions एंडपॉइंट के लिए कच्चे HTTP कॉल (URL अपडेट करना होगा)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### ह्यूरिस्टिक्स (पता लगाना और पुनर्लेखन)

- **चैट पूर्णताएँ क्लाइंट**: `client.chat.completions.create` → `client.responses.create(...)`।

- **Azure क्लाइंट कंस्ट्रक्टर्स**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`।
- **टूल्स**: फ़ंक्शन-कॉलिंग टूल परिभाषाओं को नेस्टेड फॉर्मेट (`{"type": "function", "function": {"name": ...}}`) से फ्लैट Responses फॉर्मेट (`{"type": "function", "name": ...}`) में रूपांतरित करें; `tool_choice` का उपयोग करें; टूल परिणामों को `{"type": "function_call_output", "call_id": ..., "output": ...}` आइटम के रूप में लौटाएं (न कि `{"role": "tool", ...}`)।
- **टूल राउंड-ट्रिप्स**: जब मॉडल फ़ंक्शन कॉल लौटाए, तो बातचीत में `response.output` आइटम जोड़ें (मैन्युअल `{"role": "assistant", "tool_calls": [...]}` डिक्ट नहीं), फिर प्रत्येक परिणाम के लिए `function_call_output` आइटम जोड़ें।
- **कुछ-शॉट टूल उदाहरण**: यदि बातचीत में हार्डकोडेड टूल कॉल उदाहरण शामिल हैं, तो उन्हें `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` आइटम में रूपांतरित करें। IDs `fc_` से शुरू होनी चाहिए।
- **`pydantic_function_tool()`**: यह हेल्पर अभी भी पुराना नेस्टेड फॉर्मेट जनरेट करता है और `responses.create()` के साथ **अनुकूल नहीं है**। मैन्युअल टूल परिभाषाओं या फ्लैटनिंग रैपर से प्रतिस्थापित करें।
- **मल्टी-टर्न**: एप्लिकेशन में संवाद इतिहास बनाए रखें; पूर्व टर्न्स को `input` आइटम के माध्यम से पास करें।
- **फॉर्मेटिंग**: चैट के टॉप-लेवल `response_format` को Responses में `text.format` से बदलें। कैनोनिकल रूप: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`।
- **कंटेंट आइटम्स**: चैट `content[].type: "text"` को Responses में सिस्टम/उपयोगकर्ता टर्न के लिए `content[].type: "input_text"` से बदलें।
- **छवि कंटेंट आइटम्स**: चैट के `content[].type: "image_url"` को Responses में `content[].type: "input_image"` से बदलें। `image_url` फ़ील्ड नेस्टेड ऑब्जेक्ट `{"url": "..."}` से फ्लैट स्ट्रिंग में बदल जाता है। पहले/बाद के उदाहरणों के लिए चीट शीट देखें।
- **तर्क प्रयास**: **केवल तभी मायग्रेट करें जब यह मूल कोड में पहले से मौजूद हो**।
- **कंटेंट फ़िल्टर त्रुटि हैंडलिंग**: त्रुटि बॉडी संरचना बदल गई। चैट कम्प्लीशन्स में `error.body["innererror"]["content_filter_result"]` (सिंगुलर) इस्तेमाल होता था; Responses API में `error.body["content_filters"][0]["content_filter_results"]` (प्लुरल, एक एरे के अंदर) उपयोग होता है। जो कोड `innererror` एक्सेस करता है वह `KeyError` उठाएगा। नए पथ का उपयोग करने के लिए पुनर्लेखन करें।
- **रॉ HTTP कॉल्स**: यदि ऐप सीधे Azure OpenAI REST API कॉल करता है (`requests`, `httpx` आदि से) `/openai/deployments/{name}/chat/completions?api-version=...` के माध्यम से, तो इसे `/openai/v1/responses` में पुनर्लेखन करें। रिक्वेस्ट बॉडी बदलती है: `messages` → `input`, `max_output_tokens` जोड़ें और `store: false`, `api-version` क्वेरी पैरामीटर हटाएं। प्रतिक्रिया बॉडी बदलती है: `choices[0].message.content` → `output[0].content[0].text` (नोट: `output_text` एक SDK सुविधा गुण है, रॉ REST JSON में नहीं होता)।

---

## चरण 2: माइग्रेशन लागू करें

### माइग्रेशन नोट्स (चैट कम्प्लीशन्स → Responses)

- **माइग्रेट क्यों करें**: Responses टेक्स्ट, टूल्स, और स्ट्रीमिंग के लिए एकीकृत API है; चैट कम्प्लीशन्स पुराना है। GPT-5 के साथ, Responses सर्वोत्तम प्रदर्शन के लिए आवश्यक है।
- **HTTP**: Azure एंडपॉइंट `/openai/deployments/{name}/chat/completions` से `/openai/v1/responses` में बदलता है।
- **फ़ील्ड्स**: `messages` → `input`, `max_tokens` → `max_output_tokens`। `temperature` अपरिवर्तित रहता है।
- **फॉर्मेटिंग**: `response_format` → `text.format` एक उचित ऑब्जेक्ट के साथ।
- **कंटेंट आइटम्स**: सिस्टम/उपयोगकर्ता टर्न के लिए चैट `content[].type: "text"` को Responses में `content[].type: "input_text"` से बदलें।
- **छवि कंटेंट आइटम्स**: चैट `content[].type: "image_url"` को Responses में `content[].type: "input_image"` से बदलें। `image_url` फ़ील्ड को `{"image_url": {"url": "..."}}` से `{"image_url": "..."}` (सरल स्ट्रिंग — HTTPS URL या `data:image/...;base64,...` डेटा URI) में फ्लैट करें।

### पैरामीटर मैपिंग संदर्भ

| चैट कम्प्लीशन्स | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (आइटम्स की एरे) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (ऑब्जेक्ट) |
| `temperature` | `temperature` (अपरिवर्तित) |
| `stop` | `stop` (अपरिवर्तित) |
| `frequency_penalty` | `frequency_penalty` (अपरिवर्तित) |
| `presence_penalty` | `presence_penalty` (अपरिवर्तित) |
| `tools` / function-calling | `tools` (अपरिवर्तित) |
| `seed` | **हटाएं** (समर्थित नहीं) |
| `store` | `store` (सेट करें `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (फ्लैट स्ट्रिंग) |

पूर्ण पहले/बाद के कोड उदाहरणों के लिए [cheat-sheet.md](./references/cheat-sheet.md) देखें।

परीक्षण अवसंरचना माइग्रेशन (मॉक्स, स्नैपशॉट, असर्शन) के लिए [test-migration.md](./references/test-migration.md) देखें।

त्रुटियों और समस्याओं के निवारण के लिए [troubleshooting.md](./references/troubleshooting.md) देखें।

---

## डेटा संरक्षा और स्टेट

- सभी Responses रिक्वेस्ट पर `store: false` सेट करें।
- पिछले संदेश IDs या सर्वर-संग्रहीत संदर्भ पर भरोसा न करें; स्टेट क्लाइंट-प्रबंधित रखें और मेटाडेटा कम से कम करें।

---

## प्रवेश मानदंड

### कोड-स्तर के गेट (सभी पास होने चाहिए)

- [ ] माइग्रेटेड फ़ाइलों में `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` के लिए ज़ीरो मैच।
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` के लिए ज़ीरो मैच — सभी कंस्ट्रक्टर्स `OpenAI`/`AsyncOpenAI` वर्शन 1 एंडपॉइंट का उपयोग करें।
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` के लिए ज़ीरो मैच — GitHub Models कोड पथ हटाए गए।
- [ ] `rg "OpenAIChatCompletionClient"` के लिए ज़ीरो मैच — MAF 1.0.0+ कोड `OpenAIChatClient` (जो Responses API का उपयोग करता है) का उपयोग करता है। 1.0.0 से पहले के लिए `agent-framework-openai>=1.0.0` में अपग्रेड करें।
- [ ] सभी `ChatOpenAI(...)` कॉल्स में `use_responses_api=True` शामिल हो।
- [ ] `rg "choices\[0\]"` के लिए ज़ीरो मैच — सभी प्रतिक्रिया एक्सेस `resp.output_text` या Responses आउटपुट स्कीमा का उपयोग करते हैं।
- [ ] शीर्ष स्तर पर कोई `response_format` न हो; सभी स्ट्रक्चर्ड आउटपुट `text={"format": {...}}` का उपयोग करते हैं।
- [ ] `requirements.txt` या `pyproject.toml` में `openai>=1.108.1` और `azure-identity`; डिपेंडेंसी पुनर्स्थापित की गईं।
- [ ] हर `responses.create` कॉल पर `store=False` सेट है।
- [ ] क्लाइंट निर्माण में कोई `api_version` नहीं; `AZURE_OPENAI_API_VERSION` एन्व फ़ाइलों और इंफ्रा से हटाया गया।

### टेस्ट अवसंरचना गेट्स (सभी पास होने चाहिए)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions"` टेस्ट फ़ोल्डर में ज़ीरो मैच।
- [ ] `rg "_azure_ad_token_provider"` टेस्ट फ़ोल्डर में ज़ीरो मैच — असर्शन अपडेट किए गए हैं, जांचें `isinstance(client, AsyncOpenAI)` या `base_url`।
- [ ] `rg "prompt_filter_results|content_filter_results"` टेस्ट फ़ोल्डर में ज़ीरो मैच — Azure-विशिष्ट फ़िल्टर मॉक हटाए गए।
- [ ] मॉक फिक्स्चर `kwargs.get("input")` का उपयोग करते हैं, `kwargs.get("messages")` का नहीं।
- [ ] स्नैपशॉट / गोल्डन फाइल्स Responses स्ट्रीमिंग फ़ॉर्मेट में अपडेट किए गए (कोई `choices[0]`, `function_call`, `logprobs` नहीं)।
- [ ] `pytest` सभी टेस्ट अपडेट्स के बाद ज़ीरो फेल्योर के साथ पास होता है।

### व्यवहार संबंधी गेट्स (मैन्युअल या टेस्ट हार्नेस के माध्यम से सत्यापित करें)

- [ ] **बेसिक कम्प्लीशन**: नॉन-स्ट्रीमिंग `responses.create` गैर-खाली `output_text` लौटाता है।
- [ ] **स्ट्रीम समरूपता**: यदि मूल कोड ने स्ट्रीमिंग उपयोग किया, तो माइग्रेट किया गया कोड स्ट्रीम करता है और `response.output_text.delta` घटनाएं गैर-खाली डेल्टा के साथ जारी करता है।
- [ ] **स्ट्रक्चर्ड आउटपुट**: यदि `text.format` के साथ `json_schema` का उपयोग करता है, तो `json.loads(resp.output_text)` सफल होता है और स्कीमा से मिलता है।
- [ ] **टूल-कॉल लूप**: यदि टूल्स का उपयोग होता है, तो मॉडल टूल कॉल करता है, एप्लिकेशन उन्हें निष्पादित करता है, और फॉलो-अप रिक्वेस्ट अंतिम `output_text` लौटाता है (कोई अनंत लूप नहीं)।
- [ ] **Async समरूपता**: यदि `AsyncAzureOpenAI` इस्तेमाल किया, तो `AsyncOpenAI` समकक्ष `await` के साथ काम करता है।
- [ ] **त्रुटि दर**: माइग्रेशन पूर्व बेसलाइन की तुलना में कोई नई 400/401/404 त्रुटियां नहीं।

### डिलिवरेबल्स

- सारांश में संपादित फ़ाइलें, परंपरागत कॉल साइट्स की पहले/बाद की गिनती, और अगली कार्रवाइयाँ शामिल हैं।
- परिवर्तन कार्य-ट्री संपादन हैं केवल (कोई कमिट नहीं)।

---

## SDK संस्करण आवश्यकताएँ

| पैकेज | न्यूनतम संस्करण |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | नवीनतम (EntraID प्रमाणीकरण के लिए) |

---

## संदर्भ

- [चीट शीट — सभी कोड स्निपेट्स](./references/cheat-sheet.md)
- [टेस्ट माइग्रेशन — मॉक, स्नैपशॉट, असर्शन](./references/test-migration.md)
- [ट्रबलशूटिंग — त्रुटियां, जोखिम तालिका, समस्याएं](./references/troubleshooting.md)
- [detect_legacy.py — स्वचालित स्कैनर](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI स्टार्टर किट](https://aka.ms/openai/start)
- [Azure OpenAI Responses API दस्तावेज़](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API संस्करण जीवनचक्र](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API संदर्भ](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->