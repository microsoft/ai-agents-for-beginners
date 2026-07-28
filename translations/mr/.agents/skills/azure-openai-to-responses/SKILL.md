---
name: azure-openai-to-responses
license: MIT
---
# Azure OpenAI Chat Completions कडून Responses API कडे Python अ‍ॅप्सचे स्थलांतर करा

> **अधिकृत मार्गदर्शन — नेमके पालन करा**
>
> हा कौशल्य Azure OpenAI Chat Completions वापरणारे Python कोडबेस Responses API या एकत्रित अनुप्रयोगाकडे स्थलांतरित करतो.
> कृपया या सूचनांचे अचूक पालन करा.
> पॅरामीटर मॅपिंगमध्ये अनिश्चितता करू नका किंवा API चे स्वरूप बनवू नका.

---

## ट्रिगर्स

वापरकर्ता जेव्हा इच्छितो तेव्हा हा कौशल्य सक्रिय करा:
- Azure OpenAI Chat Completions कडून Responses API कडे Python अ‍ॅप स्थलांतर करा
- Azure OpenAI विरुद्ध नवीनतम API स्वरूपासाठी Python OpenAI SDK वापर सुधारित करा
- GPT-5 किंवा नवीन मॉडेलसाठी Python कोड तयार करा ज्यांना Azure वर Responses API ची आवश्यकता आहे
- `AzureOpenAI`/`AsyncAzureOpenAI` कडून मानक `OpenAI`/`AsyncOpenAI` क्लायंटकडे v1 एंडपॉइंटसह बदला
- `AzureOpenAI` कन्स्ट्रक्टर्स किंवा `api_version` संबंधित डिप्रिकेटेड चेतावण्या दुरुस्त करा

---

## ⚠️ मॉडेल सुसंगतता — प्रथम तपासा

> **स्थलांतर करण्यापूर्वी, खात्री करा की तुमचा Azure OpenAI डिप्लॉयमेंट Responses API ला सपोर्ट करतो.**

### 1. तुमच्या डिप्लॉयमेंटची स्मोक-टेस्ट करा (सर्वात जलद)

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

> **सूचना**: Azure OpenAI वर `max_output_tokens` किमान 16 आहे. 16 पेक्षा कमी मूल्ये 400 त्रुटी परत करतात. स्मोक टेस्टसाठी 50+ वापरा.

जर 404 परत आला तर डिप्लॉयमेंटच्या मॉडेलने अजून Responses सपोर्ट केलेले नाही — खालील संदर्भ तपासा किंवा समर्थित मॉडेलसह पुन्हा डिप्लॉय करा.

### 2. तुमच्या प्रदेशातील उपलब्ध मॉडेल तपासा (शिफारस केली जाते)

Responses API सपोर्टसह तुमच्या विशिष्ट प्रदेशात काय उपलब्ध आहे ते पाहण्यासाठी अंगभूत मॉडेल सुसंगतता साधन चालवा:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

हे Azure ARM ला थेट क्वेरी करते आणि सुसंगतता मॅट्रिक्स दाखवते — कोणते मॉडेल्स Responses, संरचित आउटपुट, टूल्स इ. सपोर्ट करतात. `--filter gpt-5.1,gpt-5.2` वापरून निकाल कमी करा किंवा स्क्रिप्टिंगसाठी `--json` वापरा.

### 3. पूर्ण मॉडेल सपोर्ट संदर्भ

- **थेट क्वेरी**: `python migrate.py models` (वरीलप्रमाणे — प्रदेश-विशिष्ट, सदैव अद्ययावत)
- **उपलब्धता ब्राउझ करा**: [मॉडेल सारांश तक्ती आणि प्रदेश उपलब्धता](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **क्विकस्टार्ट & मार्गदर्शन**: **https://aka.ms/openai/start**

### ⚠️ जुने मॉडेल मर्यादा

> **इशारा**: जुन्या मॉडेल्स (`gpt-4.1` पूर्वीचे) कदाचित Responses API चे सर्व फिचर पूर्णपणे समर्थित करू शकत नाहीत.
>
> जुन्या मॉडेल्ससह ओळखल्या गेलेल्या मर्यादा:
> - **`reasoning` पॅरामीटर**: अनेक नॉन-रीझनिंग मॉडेल्सवर समर्थित नाही. मूळ कोडमध्ये असेल तरच `reasoning` स्थलांतर करा.
> - **`seed` पॅरामीटर**: Responses API मध्ये अजिबात समर्थित नाही — सर्व विनंत्यांमधून काढा.
> - **`text.format` द्वारे संरचित आउटपुट**: जुन्या मॉडेल्स कदाचित `strict: true` JSON स्कीमा विश्वसनीयपणे लागू करू शकत नाहीत.
> - **टूल ऑर्केस्ट्रेशन**: GPT-5+ अंतर्गत रीझनिंगचा भाग म्हणून टूल कॉल्सचे नियोजन करते. जुन्या Responses मॉडेल्स चालतात पण सखोल समाकलन नसते.
> - **तापमान मर्यादा**: `gpt-5` कडे स्थलांतर करताना तापमान टाळावे किंवा `1` वर सेट करावे. जुन्या मॉडेल्सवर अशी मर्यादा नाही.

### O-सीरीज रीझनिंग मॉडेल्स (o1, o3-mini, o3, o4-mini)

O-सीरीज मॉडेल्सना विशेष पॅरामीटर मर्यादा असतात. जेव्हा o-सीरीज मॉडेल्ससाठी अ‍ॅप्स स्थलांतरित करत असाल:

- **`temperature`**: `1` असणे आवश्यक (किंवा वगळा). O-सीरीज मॉडेल्स इतर मूल्य स्वीकारत नाहीत.
- **`max_completion_tokens` → `max_output_tokens`**: Azure-विशिष्ट `max_completion_tokens` वापरणारे अ‍ॅप्स `max_output_tokens` कडे स्विच करा. reasoning टोकन्समुळे मर्यादा जास्त ठेवा (4096+).
- **`reasoning_effort`**: अ‍ॅपमध्ये `reasoning_effort` (low/medium/high) वापरले असेल तर ठेवा — Responses API o-सीरीज मॉडेल्ससाठी हे पॅरामीटर सपोर्ट करते.
- **स्ट्रीमिंग वर्तन**: O-सीरीज मॉडेल्स रीझनिंग पूर्ण होईपर्यंत आउटपुट बफर करू शकतात आणि नंतर टेक्स्ट डेल्टा इव्हेंट्स पाठवतात. स्ट्रीमिंग चालू राहते, पण GPT मॉडेल्सच्या तुलनेत पहिला `response.output_text.delta` देरीने येऊ शकतो.
- **`top_p`**: O-सीरीजवर समर्थित नाही — असल्यास काढा.
- **टूल वापर**: O-सीरीज मॉडेल्स Responses API द्वारे GPT मॉडेल्ससारखे टूल्स सपोर्ट करतात, पण टूल कॉल ऑर्केस्ट्रेशन गुणवत्ता मॉडेलनुसार वेगळी आहे.

**क्रिया — सक्रिय मॉडेल सल्ला**: स्कॅन टप्प्यात अ‍ॅप कोणत्या मॉडेलसाठी टार्गेट करते ते तपासा (डिप्लॉयमेंट नावे, एन्व्ह वेरिएबल्स, कॉन्फिग). मॉडेल जर `gpt-4.1` पूर्वीचे असेल तर वापरकर्त्याला पुढील सूचना द्या:
- स्थलांतर त्याच्या सध्याच्या मॉडेलवर बेसिक टेक्स्ट, चॅट, स्ट्रीमिंग, आणि टूल्ससाठी काम करेल.
- नवीन मॉडेल्स (`gpt-5.1`, `gpt-5.2`) चांगले टूल ऑर्केस्ट्रेशन, संरचित आउटपुट अंमलबजावणी, रीझनिंग, आणि क्रॉस-रिजन उपलब्धता देतात.
- त्यांना जेव्हा तयार वाटेल तेव्हा डिप्लॉयमेंट अपग्रेड करण्याचा विचार करावा — हे स्थलांतराला अडथळा ठरत नाही.

मॉडेल आवृत्तीवर आधारित स्थलांतर थांबवू किंवा नकार देऊ नका. हा सल्ला माहितीपर आहे.

### GitHub मॉडेल्स Responses API ला सपोर्ट करत नाहीत

> **GitHub मॉडेल्स (`models.github.ai`, `models.inference.ai.azure.com`) Responses API ला सपोर्ट करत नाहीत.**

जर कोडबेसमध्ये GitHub मॉडेल्सचा कोड पथ असेल (`base_url` जे `models.github.ai` किंवा `models.inference.ai.azure.com` कडे निर्देशित करतो), तर **स्थलांतर दरम्यान पूर्णपणे काढून टाका**. Responses API साठी Azure OpenAI, OpenAI, किंवा जुळणारा लोकल एंडपॉइंट (उदा. Ollama ज्याला Responses सपोर्ट आहे) आवश्यक आहे.

स्कॅन दरम्यान क्रिया:
- कोणत्याही GitHub मॉडेल्स कोड पाथसाठी काढून टाकण्याचा धोकाही रहदारी करा.

---

## फ्रेमवर्क स्थलांतर

बरेच अ‍ॅप्स OpenAI वर उच्च-स्तरीय फ्रेमवर्क वापरतात. जेव्हा हे स्थलांतर करता, तेव्हा फक्त OpenAI कॉल्स नव्हे तर फ्रेमवर्कची स्वतःची API बदलते.

### Microsoft एजंट फ्रेमवर्क (MAF)

**आपला MAF व्हर्जन प्रथम तपासा** — स्थलांतर MAF 1.0.0+ किंवा 1.0.0 पूर्वीच्या बीटा/RC वर अवलंबून आहे.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **आधीच Responses API वापरतो** — स्थलांतर आवश्यक नाही. जर कोडबेस जुना `OpenAIChatCompletionClient` (जो `chat.completions.create` वापरतो) वापरत असेल, तर तो `OpenAIChatClient` ने बदला.

| पूर्वी | नंतर |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

तुम्ही कोणता व्हर्जन वापरत आहात हे तपासण्यासाठी: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF पूर्व-1.0.0 (बीटा/RC रिलीज)

पूर्व-1.0.0 MAF मध्ये, `OpenAIChatClient` Chat Completions वापरत होता. `agent-framework-openai>=1.0.0` मध्ये अपग्रेड करा जिथे `OpenAIChatClient` डिफॉल्टने Responses API वापरतो.

दुसरे कोणतेही बदल आवश्यक नाही — `Agent` आणि टूल API समान रहातात.

### LangChain (`langchain-openai`)

`ChatOpenAI()` मध्ये `use_responses_api=True` जोडा. तसेच प्रतिसाद प्रवेश `.content` कडून `.text` कडे बदला.

| पूर्वी | नंतर |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

पूर्ण पूर्वी/नंतर कोड उदाहरणांसाठी, पहा [cheat-sheet.md](./references/cheat-sheet.md).

---

## फ्रंटेंड स्थलांतर मार्गदर्शन

> **Responses API हे सर्व्हर-साइडचे बाब आहे.** तुमचा Python बॅकेंड स्थलांतर करा; फ्रंटेंडचा HTTP करार जवळजवळ बदलू नये जोपर्यंत तुमचा बॅकेंड एक लहान पास-थ्रू नसतो — त्या परिस्थितीत Responses विनंतीचे स्वरूप स्वीकारण्याचा विचार करा जेणेकरून भाषांतर थर टाळता येईल. जर फ्रंटेंड OpenAI ला थेट क्लायंट-साइड की सह कॉल करत असेल तर आधी ते कॉल बॅकेंडकडे हलवा.

### `@microsoft/ai-chat-protocol` चे डिप्रिसेशन

`@microsoft/ai-chat-protocol` एनपीएम पॅकेज डिप्रिकेटेड झाले आहे आणि ते [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) ने बदला पाहिजे. फ्रंटेंडमध्ये आढळल्यास:

1. CDN स्क्रिप्ट टॅग बदला:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` ची इंस्टेंशिएशन (`new ChatProtocol.AIChatProtocolClient("/chat")`) काढा.
3. `client.getStreamedCompletion(messages)` ची जागा थेट `fetch()` कॉलने बॅकेंड स्ट्रीमिंग एंडपॉइंटला द्या.
4. `for await (const response of result)` च्या जागी `for await (const chunk of readNDJSONStream(response.body))` वापरा.
5. प्रॉपर्टी प्रवेश `response.delta.content` / `response.error` कडून `chunk.delta.content` / `chunk.error` कडे बदला.

---

## उद्दिष्टे

- Azure OpenAI विरुद्ध Chat Completions किंवा जुने Completions वापरणाऱ्या सर्व Python कॉल साइट्सची गणना करा.
- Python कोडबेससाठी स्थलांतर योजना आणि अनुक्रमण प्रस्तावित करा.
- Responses API कडे सुरक्षित, लहान बदलाव करा.
- कॉलर्सना Responses आउटपुट स्कीमा वापरायला अपडेट करा; मागील सुसंगततेचे व्रॅपर वापरू नका.
- चाचण्या/लिंट्स चालवा; स्थलांतरामुळे उद्भवलेल्या लहान ब्रेक सुधारित करा.
- लहान, पुनरावलोकनयोग्य बदल संच तयार करा आणि डीफ्ससह अंतिम सारांश द्या (कमिट करू नका).

---

## संरक्षण नियम

- फक्त Git कार्यक्षेत्रातील फाइल्समध्ये बदल करा. कधीही बाहेर लिहू नका.
- मागील सुसंगतता शिम्स ठेवल्या पाहिजेत नाहीत; कोड नवीन API स्वरूपात स्थलांतरित करा.
- टॉम्बस्टोन/ट्रांझिशन टिप्पण्या वा बॅकअप फाइल्स सोडू नका.
- जर आधी स्ट्रीमिंग वापरले गेले असेल तर ते जपणूक करा; नाहीतर नॉन-स्ट्रीमिंग वापरा.
- परवानगी मोडमध्ये असाल तर कमांड किंवा नेटवर्क कॉल्स चालवण्यापूर्वी मान्यता घ्या.
- `git add`/`git commit`/`git push` चालवू नका; फक्त कार्यरत ट्री संपादने तयार करा.

---

## पाऊल 0: Azure OpenAI क्लायंट स्थलांतर (आधीच गरजेचे)

जर कोडबेस `AzureOpenAI` किंवा `AsyncAzureOpenAI` कन्स्ट्रक्टर्स वापरत असेल तर आधीच ते मानक `OpenAI` / `AsyncOpenAI` कन्स्ट्रक्टर्सकडे स्थलांतर करा. Azure-विशिष्ट कन्स्ट्रक्टर्स `openai>=1.108.1` मध्ये डिप्रिकेटेड आहेत.

### का v1 API मार्ग?

नवीन `/openai/v1` एंडपॉइंट `AzureOpenAI()` च्या ऐवजी मानक `OpenAI()` क्लायंट वापरतो, `api_version` पॅरामीटरची आवश्यकता नाही, आणि OpenAI व Azure OpenAI दोन्हीवर समान कार्य करतो. त्याच क्लायंट कोडमुळे भविष्यातील आवृत्ती व्यवस्थापन आवश्यक नाही.

### मुख्य बदल

| पूर्वी | नंतर |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | पूर्णपणे काढा |

### स्वच्छता तपासणी यादी

- क्लायंट तयार करताना `api_version` आर्ग्युमेंट काढा.
- `.env`, अ‍ॅप सेटिंग्ज, Bicep/इन्फ्रा फाइल्समधून `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` एन्व्ह वेरिएबल काढा.
- `.env`, अ‍ॅप सेटिंग्ज, Bicep/इन्फ्रा आणि चाचणी फिक्स्चरमध्ये `AZURE_OPENAI_CLIENT_ID` चे नाव बदलून `AZURE_CLIENT_ID` करा (मानक Azure Identity SDK कन्व्हेन्शन).
- `requirements.txt` किंवा `pyproject.toml` मध्ये `openai>=1.108.1` सुनिश्चित करा.

### वातावरण वेरिएबल स्थलांतर

| जुने एन्व्ह वेरिएबल | कृती | टीपा |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **काढा** | v1 एंडपॉइंटसह `api_version` आवश्यक नाही |
| `AZURE_OPENAI_API_VERSION` | **काढा** | वरच्याचप्रमाणे |
| `AZURE_OPENAI_CLIENT_ID` | **नाव बदला** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)` साठी मानक Azure Identity SDK कन्व्हेन्शन |
| `AZURE_OPENAI_ENDPOINT` | **ठेवा** | `base_url` तयार करण्यासाठी आवश्यक आहे |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **ठेवा** | `responses.create` मध्ये `model` पॅरामीटर म्हणून वापरले जाते |
| `AZURE_OPENAI_API_KEY` | **ठेवा** | की-आधारित प्रमाणीकरणासाठी `api_key` म्हणून वापरले जाते |

क्लायंट सेटअप कोड उदाहरणांसाठी (सिंक, अ‍ॅसिंक, EntraID, API की, मल्टी-टेनंट), पहा [cheat-sheet.md](./references/cheat-sheet.md).

---

## पाऊल 1: जुने कॉल साइट शोधा

स्थलांतर आवश्यक असलेल्या सर्व कॉल साइट्स शोधण्यासाठी [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) स्क्रिप्ट चालवा:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

किंवा हे शोध स्वतः करा — प्रत्येक जुळणारा स्थलांतराचा उद्देश आहे:

```bash
# लेगसी API कॉल्स (पुन्हा लिहावे लागेल)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# बंद केलेले Azure क्लायंट कंस्ट्रक्टर्स (बदला करावा लागेल)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# प्रतिसादाचे स्वरूप उपलब्धीचे नमुने (अपडेट करणे आवश्यक आहे)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# जुना नेस्टेड फॉर्मॅटमधील टूल डिफिनिशन्स (सोप्या स्वरूपात मदत करा)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# जुना फॉर्मॅटमधील टूल निकाल (function_call_output मध्ये रूपांतर करावे)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# बंद केलेले पॅरामीटर्स (काढून टाकावे किंवा नाव बदलावे)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens असे नाव द्या
rg "['\"]seed['\"]"      # remove entirely

# बंद केलेले env व्हेरिएबल्स (साफसफाई करा)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID असावे

# GitHub मॉडेल्स एंडपॉइंट्स (काढून टाका — Responses APIला समर्थित नाही)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# फ्रेमवर्क-स्तरीय लेगसी नमुने (अपडेट करणे आवश्यक आहे)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient ने बदला करा
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True आवश्यक आहे

# चाचणी पायाभूत सुविधा (अपडेट करणे आवश्यक आहे)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# कंटेंट फिल्टर त्रुटी बॉडी ऍक्सेस (अपडेट करा — रचना बदलली आहे)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # जुना एकवचनी स्वरूप — आता content_filter_results (बहुवचनी) content_filters ऍरेमध्ये आहे

# Chat Completions एंडपॉइंटसाठी रॉ HTTP कॉल्स (URL अपडेट करा)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### नियम (ओळखा आणि पुन्हा लिहा)

- **Chat Completions क्लायंट**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure क्लायंट कन्स्ट्रक्टर**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **टूल्स**: फंक्शन-कॉलिंग टूल डिफिनिशन्सचे नेस्टेड फॉरमॅट (`{"type": "function", "function": {"name": ...}}`) मधून फ्लॅट Responses फॉरमॅट (`{"type": "function", "name": ...}`) येथे कन्व्हर्ट करा; `tool_choice` वापरा; टूल निकाल परत करा `{"type": "function_call_output", "call_id": ..., "output": ...}` आयटम्स (नाहीतर `{"role": "tool", ...}`).
- **टूल राऊंड-ट्रिप्स**: जेव्हा मॉडेल फंक्शन कॉल परत करते, तेव्हा `response.output` आयटम संभाषणात जोडा (मॅन्युअल `{"role": "assistant", "tool_calls": [...]}` डिक्ट नाही), नंतर प्रत्येकी निकालासाठी `function_call_output` आयटम जोडा.
- **फ्यु-शॉट टूल उदा.**: जर संभाषणामध्ये हार्डकोडेड टूल कॉल उदाहरणे असतील, तर त्यांना `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` आयटम्समध्ये रूपांतरित करा. IDs नेहमी `fc_` वर सुरू होणे आवश्यक आहे.
- **`pydantic_function_tool()`**: हा हेल्पर अजूनही जुना नेस्टेड फॉरमॅट तयार करतो आणि `responses.create()` सोबत **सुसंगत नाही**. मॅन्युअल टूल डिफिनिशन्स किंवा फ्लॅटिंग wrapper वापरून बदल करा.
- **मल्टी-टर्न**: अॅपमध्ये संभाषण इतिहास सांगा; मागील टर्न `input` आयटम्सद्वारे पास करा.
- **फॉरमॅटिंग**: Chat च्या टॉप-लेव्हल `response_format` चा वापर टाळा, Responses मध्ये `text.format` वापरा. कॅनॉनिकल स्वरूप: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **कंटेंट आयटम्स**: Chat मध्ये `content[].type: "text"` बदला Responses मध्ये `content[].type: "input_text"` असे, वापरकर्ता/सिस्टम टर्नसाठी.
- **इमेज कंटेंट आयटम्स**: Chat मध्ये `content[].type: "image_url"` च्या जागी Responses मध्ये `content[].type: "input_image"` वापरा. `image_url` फील्ड एक नेस्टेड ऑब्जेक्ट `{"url": "..."}` मधून फ्लॅट स्ट्रिंगमध्ये बदलेल. पूर्व आणि नंतरच्या उदाहरणांसाठी चीट शीट बघा.
- **रिजनिंग प्रयत्न**: **फक्त तेव्हाच `reasoning` माईग्रेट करा जे मूळ कोडमध्ये आधीपासून आहे**.
- **कंटेंट फिल्टर त्रुटी हँडलिंग**: त्रुटीचा बॉडी स्ट्रक्चर बदलला आहे. Chat Completions मध्ये `error.body["innererror"]["content_filter_result"]` (एकवचन); Responses API मध्ये `error.body["content_filters"][0]["content_filter_results"]` (बहुवचन, अर्रेमध्ये). ज्या कोडने `innererror` ला ऍक्सेस केले आहे तो `KeyError` देते. नवीन पथ वापरा.
- **रॉ HTTP कॉल्स**: जर अॅप थेट Azure OpenAI REST API कॉल करत असेल (`requests`, `httpx` इत्यादीद्वारे) `/openai/deployments/{name}/chat/completions?api-version=...`, तर ते `/openai/v1/responses` मध्ये पुनर्लेखन करा. रिक्वेस्ट बॉडी बदलते: `messages` → `input`, `max_output_tokens` जोडा आणि `store: false`, `api-version` क्वेरी पॅराम काढा. रिस्पॉन्स बॉडी बदलते: `choices[0].message.content` → `output[0].content[0].text` (टीप: `output_text` हे SDK चं एक सोयीचे प्रॉपर्टी असून ते थेट REST JSON मध्ये नसतं).

---

## स्टेप 2: माईग्रेशन लागू करा

### माईग्रेशन नोट्स (Chat Completions → Responses)

- **माईग्रेट का करायचे**: Responses हा टेक्स्ट, टूल्स आणि स्ट्रीमिंगसाठी एकत्रित API आहे; Chat Completions जुनाट आहे. GPT-5 सह Responses सर्वोत्तम कामगिरीसाठी आवश्यक आहे.
- **HTTP**: Azure एंडपॉईंट `/openai/deployments/{name}/chat/completions` वरून `/openai/v1/responses` मध्ये बदलतो.
- **फील्डस्**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` जसेचे तसे राहते.
- **फॉरमॅटिंग**: `response_format` → `text.format` (योग्य ऑब्जेक्टसह).
- **कंटेंट आयटम्स**: System/User टर्नसाठी Chat मध्ये `content[].type: "text"` बदला Responses मध्ये `content[].type: "input_text"`.
- **इमेज कंटेंट आयटम्स**: Chat मध्ये `content[].type: "image_url"` बदला Responses मध्ये `content[].type: "input_image"`. `image_url` फील्ड `{"image_url": {"url": "..."}}` पासून `{"image_url": "..."}` (साधा स्ट्रिंग — HTTPS URL किंवा `data:image/...;base64,...` डेटा URI) मध्ये बदला.

### पॅरामीटर मॅपिंग संदर्भ

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (आयटम्सची अ‍ॅरे) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (ऑब्जेक्ट) |
| `temperature` | `temperature` (बदलेले नाही) |
| `stop` | `stop` (बदलेले नाही) |
| `frequency_penalty` | `frequency_penalty` (बदलेले नाही) |
| `presence_penalty` | `presence_penalty` (बदलेले नाही) |
| `tools` / function-calling | `tools` (बदलेले नाही) |
| `seed` | **काढून टाका** (सपोर्टेड नाही) |
| `store` | `store` (सेट करा `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (फ्लॅट स्ट्रिंग) |

पूर्णपूर्व आणि नंतरच्या कोड उदाहरणांसाठी [cheat-sheet.md](./references/cheat-sheet.md) पहा.

टेस्ट इन्फ्रास्ट्रक्चर माईग्रेशनसाठी (मॉक्स, स्नॅपशॉट्स, अ‍ॅसर्शन) [test-migration.md](./references/test-migration.md) पहा.

त्रुटी निराकरण आणि लेक्शीन्ससाठी [troubleshooting.md](./references/troubleshooting.md) पहा.

---

## डेटा रिटेन्शन आणि स्थिती

- सर्व Responses विनंत्यांवर `store: false` सेट करा.
- मागील मेसेज ID किंवा सर्व्हर-संग्रहीत संदर्भावर अवलंबून राहू नका; स्थिती क्लायंट-व्यवस्थापित ठेवा आणि मेटाडेटा कमी करा.

---

## स्वीकार्यता निकष

### कोड-स्तरीय गेट्स (सर्व पास व्हावेत)

- [ ] `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` साठी माईग्रेट केलेल्या फाइल्समध्ये जुळणारे कोणतेही नसेल.
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` साठी शून्य मॅचेस — सर्व कन्स्ट्रक्टर `OpenAI`/`AsyncOpenAI` वापरतात v1 एंडपॉईंटसह.
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` साठी शून्य मॅचेस — GitHub Models कोड काढलेले.
- [ ] `rg "OpenAIChatCompletionClient"` साठी शून्य मॅचेस — MAF 1.0.0+ कोड `OpenAIChatClient` वापरतो (जो Responses API वापरतो). प्री-1.0.0 मध्ये `agent-framework-openai>=1.0.0` मध्ये अपग्रेड करा.
- [ ] सर्व `ChatOpenAI(...)` कॉल्स मध्ये `use_responses_api=True` आहे.
- [ ] `rg "choices\[0\]"` साठी शून्य मॅचेस — सर्व प्रतिसादासाठी ऍक्सेस `resp.output_text` किंवा Responses आउटपुट स्कीमा वापरते.
- [ ] टॉप लेव्हलवर `response_format` नाही; सर्व स्ट्रक्चर्ड आउटपुट `text={"format": {...}}` वापरतो.
- [ ] `openai>=1.108.1` आणि `azure-identity` `requirements.txt` किंवा `pyproject.toml` मध्ये; dependency पुन्हा इन्स्टॉल केलेली.
- [ ] प्रत्येक `responses.create` कॉलवर `store=False` सेट केलेले.
- [ ] क्लायंट कन्स्ट्रक्शनमध्ये `api_version` नाही; `AZURE_OPENAI_API_VERSION` एन्व्ह फाइल्स आणि इन्फ्रातून काढले आहे.

### टेस्ट इन्फ्रास्ट्रक्चर गेट्स (सर्व पास व्हावेत)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` साठी शून्य मॅचेस.
- [ ] `rg "_azure_ad_token_provider" tests/` साठी शून्य मॅचेस — अ‍ॅसर्शन अपडेट केलेले आहेत `isinstance(client, AsyncOpenAI)` किंवा `base_url` तपासण्यासाठी.
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` साठी शून्य मॅचेस — Azure-विशिष्ट फिल्टर मॉक्स काढलेले.
- [ ] मॉक फिक्स्चर्स `kwargs.get("input")` वापरतात, `kwargs.get("messages")` नाही.
- [ ] स्नॅपशॉट / गोल्डन फाइल्स Responses स्ट्रीमिंग स्वरूपात अपडेट केल्या (कोणतीही `choices[0]`, `function_call`, `logprobs` नाहीत).
- [ ] सर्व टेस्ट अपडेट्सनंतर `pytest` शून्य यश-अपयशांसह पास झाला.

### वर्तणुकीचे निकष (मॅन्युअली किंवा टेस्ट हर्नेसद्वारे तपासा)

- [ ] **मूलभूत पूर्णता**: नॉन-स्ट्रीमिंग `responses.create` रिक्त नसलेले `output_text` परत करते.
- [ ] **स्ट्रीम समता**: मूळ कोडने स्ट्रीमिंग वापरले असल्यास, माईग्रेटेड कोड स्ट्रीम करतो आणि रिक्त नसलेल्या `response.output_text.delta` इव्हेंट्स यील्ड करतो.
- [ ] **स्ट्रक्चर्ड आउटपुट**: `text.format` वापरता `json_schema` सह, `json.loads(resp.output_text)` यशस्वी होते आणि स्कीमाशी जुळते.
- [ ] **टूल-कॉल लूप**: टूल्स वापरले असतील तर मॉडेल टूल कॉल्स करते, अॅप त्यांना अंमलात आणतो, आणि नंतरच्या विनंतीमध्ये अंतिम `output_text` परत येतो (अमर्यादित लूप नाही).
- [ ] **असिंक्रोनस समता**: जर `AsyncAzureOpenAI` वापरले असेल, तर `AsyncOpenAI` समतुल्य `await` सह काम करते.
- [ ] **त्रुटी दर**: माईग्रेशनपूर्वीच्या तुलनेत कोणतीही नवीन 400/401/404 त्रुटी नाहीत.

### देयके

- संपादित फाइल्सचा सारांश, पूर्व/नंतर लेगसी कॉल साइट्सची गणना, पुढील पावले.
- बदल कार्यप्रवाहातील संपादने आहेत (कोणतेही कमिट नाहीत).

---

## SDK आवृत्ती आवश्यकता

| पॅकेज | किमान आवृत्ती |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | लेटेस्ट (EntraID ऑथसाठी) |

---

## संदर्भ

- [चीट शीट — सर्व कोड स्निपेट्स](./references/cheat-sheet.md)
- [टेस्ट माईग्रेशन — मॉक, स्नॅपशॉट्स, अ‍ॅसर्शन](./references/test-migration.md)
- [त्रुटी निराकरण — त्रुटी, धोका तालिका, अडचणी](./references/troubleshooting.md)
- [detect_legacy.py — स्वयंचलित स्कॅनर](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI स्टार्टर किट](https://aka.ms/openai/start)
- [Azure OpenAI Responses API डॉक्स](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API आवृत्ती जीवनचक्र](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API संदर्भ](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->