---
name: azure-openai-to-responses
license: MIT
---
# Azure OpenAI Chat Completions–இல் இருந்து Responses APIக்கு Python செயலிகளை மாற்றவும்

> **அதிகாரப்பூர்வ வழிகாட்டல் — துல்லியமாக பின்பற்றவும்**
>
> இந்த திறன் Azure OpenAI Chat Completions பயன்படுத்தும் Python குறியீட்டு அடிப்படைகளை
> ஒருங்கிணைந்த Responses APIக்கு மாற்றுகிறது. இந்த அறிவுரைகளை துல்லியமாக பின்பற்றவும்.
> பரிமாறல் வரைபடங்களை கற்பனை செய்யக் கூடாது அல்லது API வடிவங்களை உருவாக்கக் கூடாது.

---

## தொடக்கிகள்

பயனர் பின்வருவன செய்ய விரும்பும் போது இந்த திறனை செயற்படுத்தவும்:
- Azure OpenAI Chat Completions-இல் இருந்து Responses APIக்கு Python செயலியை மாற்றவும்
- Azure OpenAIக்கு எதிரான Python OpenAI SDK பயன்பாட்டை சமீபத்திய API வடிவத்திற்கு மேம்படுத்தவும்
- Azure Responses தேவையுள்ள GPT-5 அல்லது புதிய மாதிரிகள் இயக்க Python குறியீட்டை தயாரிக்கவும்
- `AzureOpenAI`/`AsyncAzureOpenAI` இல் இருந்து பொதுவான `OpenAI`/`AsyncOpenAI` கிளையன்ட் v1 endpoint உடன் மாறவும்
- `AzureOpenAI` கட்டமைப்புகள் அல்லது `api_version` உடன் தொடர்புடைய விலக்கம் எச்சரிக்கைகளை சரிசெய்யவும்

---

## ⚠️ மாதிரி பொருத்தத்தன்மை — முதலில் சரிபார்க்கவும்

> **மாற்றுவதற்கு முன், உங்கள் Azure OpenAI உட்பொருத்தம் Responses API ஆதரிக்கிறதா என்பதை சரிபார்க்கவும்.**

### 1. உங்கள் உட்பொருத்தத்தை எளிதாகக் கசிவு செய்யவும் (மிக வேகமாக)

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

> **குறிப்பு**: Azure OpenAI இல் `max_output_tokens`க்கு குறைந்த பட்சம் **16** உள்ளது. 16 கீழ் மதிப்புகள் 400 பிழையை உண்டாக்கும். கசிவு சோதனைகளுக்கு 50+ பயன்படுத்தவும்.

இது 404-ஐத் திருப்பினால், உட்பொருத்தத்தின் மாடல் இன்னும் Responses ஆதரிக்கவில்லை — கீழுள்ள குறிப்பு பார்க்கவும் அல்லது ஆதரவுள்ள மாடல் கொண்டு மறுசேர்க்கவும்.

### 2. உங்கள் பகுதியிலுள்ள கிடைக்கும் மாதிரிகளை சரிபார்க்கவும் (பரிந்துரைக்கப்படுகிறது)

Responses API ஆதரவு உடன் உங்கள் குறிப்பிட்ட பகுதியில் கிடைக்கும் விவரங்களுக்கான உள்ளமைக்கப்பட்ட மாதிரி பொருத்தம் கருவியை இயக்கவும்:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

இது Azure ARM நேரலைக்கு கேட்கிறது மற்றும் ஒரு பொருத்த மட்ரிக்ஸ் காட்டுகிறது — எது Responses, கட்டமைந்த வெளி, கருவிகள் ஆதரிக்கின்றன; `--filter gpt-5.1,gpt-5.2` மூலம் முடிவுகளை குறைக்கவும் அல்லது ஸ்கிரிப்டிங்கிற்கு `--json` பயன்படுத்தவும்.

### 3. முழுமையான மாடல் ஆதரவு குறிப்பு

- **நேரடி கேள்வி**: `python migrate.py models` (மேலே காணவும் — பகுதி-சார்ந்தது, எப்போதும் புதுப்பிக்கப்பட்டது)
- **கிடைக்கும் விவரம்**: [Model summary table and region availability](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **துவக்க மற்றும் வழிகாட்டல்**: **https://aka.ms/openai/start**

### ⚠️ பழைய மாடல் வரம்புகள்

> **எச்சரிக்கை**: பழைய மாதிரிகள் (`gpt-4.1` முன் உள்ளவை) Responses API அனைத்து அம்சங்களையும் முழுமையாக ஆதரிக்காமல் இருக்கலாம்.
>
> பழைய மாதிரிகளுடன் உள்ள அறிவிக்கப்பட்ட வரம்புகள்:
> - **`reasoning` பரிமாறல்**: பல நிலை-தல்லாக்கல் மாதிரிகள் ஆதரிக்கவில்லை. தொடக்கக் குறியீட்டில் இருந்தால் மட்டுமே `reasoning`-ஐ மாற்றவும்.
> - **`seed` பரிமாறல்**: Responses API இல் முழுமையாக ஆதரிக்கப்படவில்லை — அனைத்து கோரிக்கைகளிலும் அகற்றவும்.
> - **`text.format` மூலம் கட்டமைந்த வெளியீடு**: பழைய மாதிரிகள் `strict: true` JSON வடிவங்களை நம்பகமாக அமுல்படுத்தாமலும் இருக்கலாம்.
> - **கருவி ஒருங்கிணைப்பு**: GPT-5+ கருவி அழைப்புகளை உள்ளார்ந்த காரணியலுக்கு இணையாக ஒழுங்குபடுத்தும். Responses இல் பழைய மாதிரிகள் வேலை செய்யும் ஆனால் இந்த ஆழமான ஒருங்கிணைப்பு இல்லை.
> - **வெப்பநிலை கட்டுப்பாடுகள்**: `gpt-5`க்கு மாற்றும்போது வெப்பநிலை தவிர்க்கப்படவேண்டும் அல்லது `1` ஆக அமைக்கவேண்டும். பழைய மாதிரிகளுக்கு இவ்விதமான கட்டுப்பாடு இல்லை.

### O-தொடர் காரணியலாக்கல் மாதிரிகள் (o1, o3-mini, o3, o4-mini)

O-தொகுப்பின் மாதிரிகளுக்கு தனித்துவமான பரிமாறல் கட்டுப்பாடுகள் உள்ளன. o-தொகுதி மாதிரிகளுக்கான செயலிகளை மாற்றும் போது:

- **`temperature`**: `1` ஆகவேண்டும் (அல்லது தவிர்க்கப்படவேண்டும்). O-தொகுதி மாதிரிகள் மற்ற மதிப்புகளை ஏற்கவில்லை.
- **`max_completion_tokens` → `max_output_tokens`**: Azure-விசேட `max_completion_tokens` பயன்பாட்டை `max_output_tokens`-க்கு மாற்ற வேண்டும். 4096+ மாதிரிகளைப் பயன்படுத்தவும் ஏனெனில் காரணல் டோக்கன்கள் வரம்புக்கு எதிராக கணக்கிடப்படும்.
- **`reasoning_effort`**: பயன்பாடு `reasoning_effort` (குறைவு/நடுத்தரம்/மிக அதிகம்) பயன்படுத்தினால் அதனை வைத்திருக்கவும் — o-தொகுதி மாதிரிகளுக்கு Responses API இந்த பரிமாறலை ஆதரிக்கிறது.
- **ஒளிபரப்பு நடத்தை**: O-தொகுதி மாதிரிகள் காரணல் முடியும் வரை வெளியீட்டை காலதாமதமாக தள்ளி வைக்கலாம் பிறகு டெல்டா நிகழ்வுகளை விடுவிக்கும். ஒளிபரப்பு வேலை செய்கிறது, ஆனால் முதலாவது `response.output_text.delta` GPT மாதிரிகளைவிட அதிக கால தாமதத்துடன் வரும்.
- **`top_p`**: O-தொகுதி மாதிரிகளில் ஆதரிக்கப்படவில்லை — இருந்தால் அகற்றவும்.
- **கருவி பயன்பாடு**: O-தொகுதி மாதிரிகள் Responses API மூலம் கருவிகளுக்கு ஆதரவு GPT மாதிரிகளுக்கு இசையாக உள்ளது, ஆனால் கருவி அழைப்பு ஒருங்கிணைப்பு தரம் மாதிரிக்கு வித்தியாசம் காட்டுகிறது.

**செயல் — முன்கூட்டிய மாதிரி அறிவுரை**: ஸ்கேன் கட்டத்தின்போது, செயலி எது மாதிரியை குறிவைக்கிறது (உட்பொருத்த பெயர்கள், சூழல் மாறிகள், கட்டமைப்பு) என்று காணவும். மாதிரிகள் `gpt-4.1` க்கு முன் வருமானால் (gpt-4.1+ அல்ல), பயனருக்கு முன்கூட்டியே தெரிவிக்கவும்:
- அவர்களின் தற்போதைய மாதிரியில் அடிப்படைக் கருவிகள், உரை, ஒளிபரப்பு மற்றும் கருவிகளுக்கு மாற்றம் வேலை செய்யும்.
- புதிய மாதிரிகள் (`gpt-5.1`, `gpt-5.2`) சிறந்த கருவி ஒருங்கிணைப்பு, கட்டமைந்த வெளியீடு, காரணல் மற்றும் பகுதி வெளிப்படும் வசதிகளை வழங்குகின்றன.
- தயார் நிலையில் இருந்தால், உட்பொருத்தத்தை மேம்படுத்த பரிந்துரைக்க வேண்டும் — இது மாற்றத்தை தடுக்கும் இல்லை.

மாதிரி பதிப்பின் அடிப்படையில் மாற்றத்தை தடையிட வேண்டாம் அல்லது மறுத்துவிட வேண்டாம். அறிவிப்பு தகவல் சார்ந்தது.

### GitHub Models Responses APIக்கு ஆதரவு தரவில்லை

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) Responses APIக்கு ஆதரவு அளிக்காது.**

குறியீட்டு அடிப்படையில் GitHub Models குறியீட்டு பாதை இருந்தால் (`base_url` `models.github.ai` அல்லது `models.inference.ai.azure.com` திசைக்காட்டுமானால்), **மாற்றத்தின்போது முழுமையாக நீக்கவும்**. Responses APIக்கு Azure OpenAI, OpenAI அல்லது இசைவான உள்ளூர் எண்ட்பாயிண்ட் (எ.கா., Responses ஆதரவு உடன் Ollama) தேவை.

ஸ்கேன் செய்யும் போது செயல்:
- GitHub Models குறியீட்டு பாதைகளை நீக்குவதற்கான குறியீட்டை கொடுங்கள்.

---

## கட்டமைப்பு மாற்றம்

பல செயலிகள் OpenAI மேல் உள்ள உயர்நிலை கட்டமைப்புகளைப் பயன்படுத்துகின்றன. இன்னும், அவற்றை மாற்றும் போது, கட்டமைப்பின் சொந்த API மாற்றம் — அடிப்படை OpenAI அழைப்புகள் மட்டுமல்ல.

### Microsoft Agent Framework (MAF)

**முதலில் உங்கள் MAF பதிப்பை சரிபார்க்கவும்** — மாற்றம் MAF 1.0.0+ அல்லது முன்னணி 1.0.0 முன் பீட்டா/ஆர்.சி. மீது பொறுத்தது.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ஏற்கனவே Responses API பயன்படுத்துகிறது** — மாற்றம் தேவையில்லை. குறியீட்டு அடிப்படையில் பழைய `OpenAIChatCompletionClient` (`chat.completions.create` பயன்படுத்தியது) இருந்தால், அதை `OpenAIChatClient`-ஆக மாற்றவும்.

| முந்தையது | பின் |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

உங்கள் பதிப்பை பார்க்க: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (பீட்டா/ஆர்.சி வெளியீடுகள்)

முந்தைய 1.0.0 MAF இல், `OpenAIChatClient` Chat Completions பயன்படுத்தியது. `agent-framework-openai>=1.0.0`க்கு மேம்படுத்து, அங்கே `OpenAIChatClient` Responses API-ஐ இயல்பாக பயன்படுத்தும்.

வேறு மாற்றங்கள் தேவையில்லை — `Agent` மற்றும் கருவி APIகள் அதே நிலை.

### LangChain (`langchain-openai`)

`ChatOpenAI()`க்கு `use_responses_api=True` சேர்க்கவும். பதிலின் அணுகலை `.content` இலிருந்து `.text` ஆகவும் மாற்றவும்.

| முந்தையது | பின் |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

முழு முன்/பின் குறியீடு உதாரணங்களுக்கு, [cheat-sheet.md](./references/cheat-sheet.md) பார்க்கவும்.

---

## முன்னணி மாற்ற வழிகாட்டி

> **Responses API என்பது சர்வர்-பக்கம் கவலை.** உங்கள் Python பின்னணி மாற்றவும்; முன்னணியின் HTTP ஒப்பந்தம் மாற்றப்படக்கூடாது, உங்கள் பின்னணி பாதி வழியாகவிருந்தால் — மாற்ற அடிக்கடி Responses கோரிக்கை வடிவத்தை பின்பற்றலாம். முன்னணி நேரடியாக கிளையன்ட்-சைட் விசையுடன் OpenAI அழைக்கின், முதலில் பின்னணிக்கு அழைப்புகளை மாற்றவும்.

### `@microsoft/ai-chat-protocol` பாவனை நிறுத்தப்பட்டது

`@microsoft/ai-chat-protocol` npm தொகுப்பு நிறுத்தப்பட்டது, பதிலாக [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) பயன்படுத்தவேண்டும். முன்னணியில் கண்டுபிடித்தால்:

1. CDN ஸ்கிரிப்ட் குறிச்சொல்லை மாற்றவும்:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` உருவாக்கத்தை நீக்கவும் (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. `client.getStreamedCompletion(messages)`-ஐ நேரடி `fetch()` backend ஒளிபரப்பு endpointக்கு மாற்றவும்.
4. `for await (const response of result)`-ஐ `for await (const chunk of readNDJSONStream(response.body))` ஆக மாற்றவும்.
5. சொத்து அணுகலை `response.delta.content` / `response.error` இலிருந்து `chunk.delta.content` / `chunk.error` ஆக மாற்றவும்.

---

## இலக்குகள்

- Azure OpenAIவுக்கு எதிரான Chat Completions அல்லது பழைய Completions பயன்பாட்டைக் காணவும்.
- Python குறியீட்டு அடிப்படைக்கான மாற்ற திட்டம் மற்றும் வரிசை பரிந்துறவும்.
- Responses APIக்கு மாற்றுவதற்கு பாதுகாப்பான, குறைந்த முறையில் திருத்தங்களை செய்யவும்.
- Responses வெளியீட்டு வடிவத்தை பயன்படுத்த அழைப்பாளர்களை புதுப்பிக்கவும்; பின்வட்ட இணைப்பு சட்டைகள் இல்லாமல்.
- சோதனைகள்/தடை செக்கள்களை இயக்கவும்; மாற்றத்தின் மூலம் வந்த சிறிய பிழைகளை சரி செய்யவும்.
- சிறிய, மதிப்பாய்வு செய்யக்கூடிய மாற்ற தொகுதிகளை தயாரித்து இறுதி சுருக்கத்துடன் வழங்கவும் (கமைட் செய்யவேண்டாம்).

---

## பாதுகாப்பு வழிமுறைகள்

- Git பணிச்சூழலைப் பிறத்திலும் கோப்புகளை திருத்தக்கூடாது. வெளியே எழுத கூடாது.
- பின்வட்ட இணைப்பு சட்டைகளை காக்காமல் புதிய API வடிவத்திற்கு குறியீட்டை மாற்றவும்.
- மரணச்சின்னங்கள்/மாற்றுச் குறிப்புகள் அல்லது கோப்புப் போக்குகளை எப்படியுமேன்று விட்டு விட வேண்டாம்.
- முன்பு ஒளிபரப்பு இருந்தால் அதனை காக்கவும்; இல்லையெனில் ஒளிபரப்பில்லாத முறையைப் பயன்படுத்தவும்.
- அங்கீகார முறை இருந்தால் கட்டளைகள் அல்லது பிணைய அழைப்புகள் முன் அனுமதி கேளுங்கள்.
- `git add`/`git commit`/`git push` இயக்க வேண்டாம்; வேலை செய்யும் கோப்புநிலை மாற்றங்கள் மட்டும் வழங்கவும்.

---

## படி 0: Azure OpenAI கிளையன்ட் மாற்றம் (முன்னிலை)

குறியீட்டு அடிப்படையில் `AzureOpenAI` அல்லது `AsyncAzureOpenAI` கட்டமைப்புகளை பயன்படுத்தினால், முதலில் பொதுவான `OpenAI` / `AsyncOpenAI` கட்டமைப்புக்களுக்கு மாற்றவும். Azure-விசேட கட்டமைப்புகள் `openai>=1.108.1` இல் நிறுத்தப்படுகின்றன.

### ஏன் v1 API பாதை?

புதிய `/openai/v1` endpoint பொதுவான `OpenAI()` கிளையன்டை `AzureOpenAI()` பதிலாக பயன்படுத்துகிறது, `api_version` பரிமாறல் தேவையில்லை, OpenAI மற்றும் Azure OpenAIக்கு ஒத்த செயல்பாடு உள்ளது. அதே கிளையன்ட் குறியீடு எதிர்காலத்திற்கும் பொருந்தும் — பதிப்பு மேலாண்மை தேவையில்லை.

### முக்கிய மாற்றங்கள்

| முந்தையது | பின் |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | முழுமையாக நீக்கவும் |

### சுத்தம்செய்யும் பட்டியல்

- கிளையன்ட் கட்டமைப்பிலிருந்து `api_version` பரிமாறலை அகற்றவும்.
- `.env`, செயலி அமைப்புகள் மற்றும் Bicep/இன்ஃப்ரா கோப்புகளிலிருந்து `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` சுற்றுச்சூழல் மாறிகளை அகற்றவும்.
- `.env`, செயலி அமைப்புகள், Bicep/இன்ஃப்ரா மற்றும் சோதனை அமைப்பில் `AZURE_OPENAI_CLIENT_ID` ஐ `AZURE_CLIENT_ID` ஆக மறுபெயர்க்கவும் (பொது Azure அடையாள SDK நடைமுறை).
- `requirements.txt` அல்லது `pyproject.toml` இல் `openai>=1.108.1` இருக்கும் என்பதை உறுதிசெய்க.

### சுற்றுச்சூழல் மாறி மாற்றம்

| பழைய சுற்றுச்சூழல் மாறி | செயல் | குறிப்பு |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **அகற்றவும்** | v1 endpoint இல் `api_version` தேவையில்லை |
| `AZURE_OPENAI_API_VERSION` | **அகற்றவும்** | மேலேவிட மேல் |
| `AZURE_OPENAI_CLIENT_ID` | **மறுபெயர்** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)` க்கான பொதுவான Azure அடையாள SDK நடைமுறை |
| `AZURE_OPENAI_ENDPOINT` | **காக்கவும்** | இன்னும் `base_url` கட்டமைப்புக்கு தேவை |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **காக்கவும்** | `responses.create` இல் `model` பரிமாறலாக உபயோகிக்கப்படுகிறது |
| `AZURE_OPENAI_API_KEY` | **காக்கவும்** | விசை அடிப்படை அங்கீகாரத்திற்கு பயன்படும் |

கிளையன்ட் அமைப்பு குறியீடு உதாரணங்கள் (சமகால, ஏசிங்க், EntraID, API விசை, பன்முக வாடிக்கையாளர்கள்) க்கான விவரங்களுக்கு [cheat-sheet.md](./references/cheat-sheet.md) பார்க்கவும்.

---

## படி 1: பழைய அழைப்பு இடங்களை கண்டறிதல்

மாற்றம் தேவையான அனைத்து அழைப்புகளை கண்டறிய [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) ஸ்கிரிப்டை இயக்கவும்:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

அல்லது அந்தக் தேடல்களை கையேடு முறையில் இயக்கவும் — ஒவ்வொரு பொருத்தமும் மாற்ற இலக்காகும்:

```bash
# பரம்பரை API அழைப்புகள் (மறுபிரதியாக எழுத வேண்டும்)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# பழைய Azure கிளையாண்ட் கட்டுமானிகள் (மாற்ற வேண்டும்)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# பதிலின் வடிவத்தின் அணுகல் முறைமைகள் (புதுப்பிக்க வேண்டும்)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# கருவி வரையறைகள் பழைய நெஸ்ட்டட் வடிவிலானவை (சமமம் செய்)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# கருவி முடிவுகள் பழைய வடிவில் (function_call_output க்கு மாற்ற வேண்டும்)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# பழைய அளவுருக்கள் (நீக்க அல்லது மறுபெயர் செய்ய வேண்டும்)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens ஆக மறுபெயர் செய்யவும்
rg "['\"]seed['\"]"      # remove entirely

# பழைய சூழல் மாறிகள் (தூய்மைப்படுத்தவும்)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID ஆக இருக்க வேண்டும்

# GitHub மாதிரி முடிவுகள் (அநுமதிக்கப்படவில்லை - Responses API ஆதரிக்கப்படவில்லை)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# கட்டமைப்பு நிலை பரம்பரை முறைமைகள் (புதுப்பிக்க வேண்டும்)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient க்கு மாற்றவும்
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True தேவை

# சோதனை அடிப்படை அமைப்பு (புதுப்பிக்க வேண்டும்)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# உள்ளடக்க வடிகாட்டி பிழை உடல் அணுகல் (புதுப்பிக்க வேண்டும் - அமைப்பு மாறியுள்ளது)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # பழைய ஒருமைப் படை - இப்போது content_filter_results (பலபடை) content_filters வரிசையில் உள்ளன

# Chat Completions முடிவுக்கான நேரடி HTTP அழைப்புகள் (URL புதுப்பிக்க வேண்டும்)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### heuristic (கண்டறிதல் மற்றும் மறுஐழைப்பு)

- **Chat Completions கிளையன்ட்**: `client.chat.completions.create` → `client.responses.create(...)`.

- **ஏசூர் கிளையன்ட் கட்டமைப்பாளர்கள்**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **கருவிகள்**: பண்பல வடிவிலிருந்து (`{"type": "function", "function": {"name": ...}}`) செயல்பாடு-கால் கருவி வரையறைகளை Responses சமநிலை வடிவிற்கு மாற்றவும் (`{"type": "function", "name": ...}`); `tool_choice` ஐப் பயன்படுத்துங்கள்; கருவி முடிவுகளை `{"type": "function_call_output", "call_id": ..., "output": ...}` பொருட்களாக திருப்பவும் (`{"role": "tool", ...}` அல்ல).
- **கருவி சுற்றுப்பயணங்கள்**: மாதிரி செயல்பாட்டு அழைப்புகளை மீட்டமைக்கும் போது, குரல் (conversation)க்கு `response.output` பொருட்களை சேர்க்கவும் (கையால் `{"role": "assistant", "tool_calls": [...]}` அகராதி அல்ல), பின்னர் ஒவ்வொரு முடிவிற்கும் `function_call_output` பொருட்களைச் சேர்க்கவும்.
- **சிறிய-துடிப்பான கருவி எடுத்துக்காட்டுகள்**: உரையாடல் கடினமாக நிரலிடப்பட்ட கருவி கால் எடுத்துக்காட்டுகளை உள்ளடக்கியால், அவைகளை `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` பொருட்களாக மாற்றவும். IDs `fc_` கொண்டு துவங்க வேண்டும்.
- **`pydantic_function_tool()`**: இந்த உதவியாளர் இன்னும் பழைய பண்பல வடிவை உருவாக்குகிறது மற்றும் `responses.create()` உடன் **பொருந்தாது**. அதை கையால் கருவி வரையறைகள் அல்லது flattening வாய்ப்பாட்டுடன் மாற்றவும்.
- **பல-திருப்பங்கள்**: செயலியில் உரையாடல் வரலாற்றை பராமரிக்கவும்; முன் திருப்பங்களை `input` பொருட்களின் மூலம் வழங்கவும்.
- **வடிவமைப்பு**: Chat இன் மேல்நிலை `response_format` ஐ Responses இல் `text.format` ஆக மாற்றவும். ஒழுங்கான வடிவம்: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **உள்ளடக்கப் பொருட்கள்**: Chat இல் `content[].type: "text"` ஐ Responses இல் `content[].type: "input_text"` ஆக மாற்றவும் இவை பயனர்/கணினி திருப்பங்களுக்கு.
- **பட உள்ளடக்கப் பொருட்கள்**: Chat இல் `content[].type: "image_url"` ஐ Responses இல் `content[].type: "input_image"` ஆக மாற்றவும். `image_url` களம் ஒரு பண்பல பொருள் `{"url": "..."}` இருந்து ஒரு நேரான ஸ்ட்ரிங்காக மாறுகிறது. முன்பும் பின்னாலும் எடுத்துக்காட்டுகளுக்கு கட்டளை அட்டவணையை பார்க்கவும்.
- **காரணம் முனைப்புக் கௌரவம்**: **மூலக் குறியீட்டில் ஏற்கனவே இருந்தால் மட்டுமே `reasoning`ஐ மாற்றவும்**.
- **உள்ளடக்க வடிகட்டும் பிழை கையாளுதல்**: பிழை உடல் அமைப்பு மாற்றப்பட்டது. Chat Completions `error.body["innererror"]["content_filter_result"]` (ஒற்றை) பயன்படுத்தியது; Responses API `error.body["content_filters"][0]["content_filter_results"]` (பன்மை, ஒரு வரிசையில்) பயன்படுத்துகிறது. `innererror` அணுகும் குறியீடு `KeyError` எழுப்பும். புதிய பாதையை பயன்படுத்துவதற்காக மறுஆகச் செய்யவும்.
- **நிரலாக்க HTTP அழைப்புகள்**: செயலி நேரடியாக ஏசூர் OpenAI REST API ஐ (`requests`, `httpx` போன்றவை மூலம்) `/openai/deployments/{name}/chat/completions?api-version=...` அழைக்கும் போது, அதை `/openai/v1/responses` ஆக மறுஆகச் செய்யவும். கோரிக்கை உடல் மாற்றங்கள்: `messages` → `input`, `max_output_tokens` மற்றும் `store: false` சேர்க்கவும், `api-version` கேள்விப் பராமரிப்பை நீக்கவும். பதில் உடல் மாற்றங்கள்: `choices[0].message.content` → `output[0].content[0].text` (குறிப்பு: `output_text` என்பது SDK வசதியின்மை அம்சம், நெருக்கடியான REST JSON இல் இல்லை).

---

## படி 2: மாற்றத்தைக் கடைபிடிக்கவும்

### மாற்ற குறிப்புகள் (Chat Completions → Responses)

- **ஏன் மாற்ற வேண்டும்**: Responses என்பது உரை, கருவிகள் மற்றும் ஸ்ட்ரீமிங்கிற்கான ஒருங்கிணைந்த API ஆகும்; Chat Completions පැරණிய செயல்தளம். GPT-5 உடன் Responses சிறந்த செயல்திறனை வழங்க தேவை.
- **HTTP**: ஏசூர் இறுதி புள்ளி `/openai/deployments/{name}/chat/completions` இருந்து `/openai/v1/responses` ஆக மாறுகிறது.
- **புலங்கள்**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` மாறாது.
- **வடிவமைப்பு**: `response_format` → `text.format` ஒரு பொருளாக.
- **உள்ளடக்கப் பொருட்கள்**: Chat இல் `content[].type: "text"` ஐ Responses இல் `content[].type: "input_text"` ஆக மாற்றவும் கணினி/பயனர் திருப்பங்களுக்கு.
- **பட உள்ளடக்கப் பொருட்கள்**: Chat `content[].type: "image_url"` ஐ Responses `content[].type: "input_image"` ஆக மாற்றவும். `image_url` களத்தை `{"image_url": {"url": "..."}}` இருந்து `{"image_url": "..."}` என்ற நேரான ஸ்ட்ரிங்காக விடவும் (HTTPS URL அல்லது `data:image/...;base64,...` தரவு URI ஆக).

### அளவுரு பொருத்தம் குறிப்பு

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (பொருட்களின் வரிசை) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (பொருள்) |
| `temperature` | `temperature` (மாற்றமில்லாமல்) |
| `stop` | `stop` (மாற்றமில்லாமல்) |
| `frequency_penalty` | `frequency_penalty` (மாற்றமில்லாமல்) |
| `presence_penalty` | `presence_penalty` (மாற்றமில்லாமல்) |
| `tools` / function-calling | `tools` (மாற்றமில்லாமல்) |
| `seed` | **நீக்கு** (ஆதரவு இல்லை) |
| `store` | `store` (`false` ஆக அமைக்கவும்) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (நேரான ஸ்ட்ரிங்) |

முழுமையான முன்பும் பின்னரும் குறியீடு எடுத்துக்காட்டுகளுக்கு [cheat-sheet.md](./references/cheat-sheet.md) பார்க்கவும்.

சோதனை கட்டமைப்பு மாற்றங்களுக்கு (மோகிகள், ஸ்நாப்ப்ஷாட்கள், உறுதிப்படுத்தல்கள்) [test-migration.md](./references/test-migration.md) பார்க்கவும்.

பிழைகள் மற்றும் கெட்டதனங்கள் சந்திக்கும் போது [troubleshooting.md](./references/troubleshooting.md) பார்க்கவும்.

---

## தரவு வைத்தல் & நிலைமை

- அனைத்து Responses கோரிக்கைகளிலும் `store: false` ஐ அமைக்கவும்.
- முந்தய செய்தி ஐடியை மற்றும் சர்வர்-பாரம்பரியக் காணொளியை நம்ப வேண்டாம்; நிலையை கிளையன்ட் நிர்வகிக்கவும் மற்றும் எ Metadata ஐ குறைக்கவும்.

---

## ஏற்றுக்கொள்ளும் நிபந்தனைகள்

### குறியீட்டு நிலை வாவிகள் (எல்லாம் கடந்து செல்ல வேண்டும்)

- [ ] மாற்றப்பட்ட கோப்புகளில் `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` எனும் பொருந்தல்கள் எதுவும் இல்லை.
- [ ] அனைத்து கட்டமைப்பாளர்களும் v1 இறுதி புள்ளியுடன் `OpenAI`/`AsyncOpenAI` பயன்படுத்துகின்றன; `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` பொருந்தல்கள் இல்லை.
- [ ] GitHub மாதிரிகள் குறியீட்டு பாதைகள் அகற்றப்பட்டுள்ளன; `rg "models\.github\.ai|models\.inference\.ai\.azure"` பொருந்தல்கள் இல்லை.
- [ ] `rg "OpenAIChatCompletionClient"` பொருந்தல்கள் இல்லை — MAF 1.0.0+ குறியீடு `OpenAIChatClient` (Responses API பயன்படுத்துவது) ஐப் பயன்படுத்துகிறது. முந்தைய 1.0.0 முனையை `agent-framework-openai>=1.0.0` இல் மேம்படுத்தவும்.
- [ ] அனைத்து `ChatOpenAI(...)` அழைப்புகளும் `use_responses_api=True` அடங்கும்.
- [ ] அனைத்து பதில் அணுகலும் `resp.output_text` அல்லது Responses வெளியீட்டு விளக்கக் கோவை பயன்படுத்துகிறது; `rg "choices\[0\]"` பொருந்தல்கள் இல்லை.
- [ ] மேல் நிலை `response_format` இல்லை; அனைத்து அமைந்த வெளியீடுகள் `text={"format": {...}}` ஐப் பயன்படுத்தும்.
- [ ] `openai>=1.108.1` மற்றும் `azure-identity` `requirements.txt` அல்லது `pyproject.toml` இல்; சார்புகள் மீண்டும் நிறுவப்பட்டுள்ளன.
- [ ] அனைத்து `responses.create` அழைப்புகளிலும் `store=False` அமைக்கப்பட்டுள்ளது.
- [ ] எந்த கிளையன்ட் கட்டமைப்பிலும் `api_version` இல்லை; `AZURE_OPENAI_API_VERSION` சுற்றுச்சூழல் கோப்புகளிலிருந்து மற்றும் கட்டமைப்பிலிருந்து அகற்றப்பட்டது.

### சோதனை கட்டமைப்பு வாவிகள் (எல்லாம் கடந்து செல்ல வேண்டும்)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` பொருந்தல்கள் இல்லை.
- [ ] `rg "_azure_ad_token_provider" tests/` பொருந்தல்கள் இல்லை — உறுதிப்படுத்தல்கள் `isinstance(client, AsyncOpenAI)` அல்லது `base_url` சரிபார்க்கும்.
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` பொருந்தல்கள் இல்லை — Azure-சர்வரை சார்ந்த வடிகட் மோகிகள் நீக்கப்பட்டுள்ளன.
- [ ] மோகி அம்சங்கள் `kwargs.get("input")` ஐப் பயன்படுத்தும்; `kwargs.get("messages")` அல்ல.
- [ ] ஸ்நாப்ப்ஷாட் / தங்கக் கோப்புகள் Responses ஸ்ட்ரீமிங் வடிவத்திற்கு அப்டேட் செய்யப்பட்டுள்ளன (`choices[0]`, `function_call`, `logprobs` இல்லை).
- [ ] அனைத்து சோதனைகள் `pytest` மூலம் தோல்வியின்றி வெற்றியடைகின்றன.

### நடத்தும் விதி வாவிகள் (கைமுறைமையாக அல்லது சோதனை கருவி மூலம் சரிபார்க்கவும்)

- [ ] **அடிப்படை முடிவு**: ஸ்ட்ரீமிங் இல்லாத `responses.create` வெறுமையான அல்லாத `output_text` ஐ திருப்புகிறது.
- [ ] **ஸ்ட்ரீம் சமம்**: மூலக் குறியீடு ஸ்ட்ரீமிங் பயன்படுத்தியிருந்தால், மாற்றப்பட்ட குறியீடும் ஸ்ட்ரீம் பண்ணி `response.output_text.delta` நிகழ்வுகளை வெறுமை அல்லாத டெல்டாக்கள் உடன் வழங்கும்.
- [ ] **சீரமைக்கப்பட்ட வெளியீடு**: `text.format` `json_schema` உடன் பயன்படுத்தப்படும் போது, `json.loads(resp.output_text)` வெற்றிகரமாக நிறைவேற்று மற்றும் அட்டவணையை பொருந்தும்.
- [ ] **கருவி-கால் சுற்று**: கருவிகள் பயன்படுத்தப்பட்டால், மாதிரி கருவி அழைப்புகளை விடுக்கும், செயலி அவற்றைச் செயல்படுத்தும், பின்னர் தொடரும் கோரிக்கை இறுதி `output_text` ஐ வழங்கும் ( முடிவற்ற சுற்று இல்லை).
- [ ] **சர்வதேச சமம்**: `AsyncAzureOpenAI` பயன்படுத்தியிருந்தால், `AsyncOpenAI` நீட்டிப்பு await உடன் வேலை செய்வதை உறுதிப்படுத்தவும்.
- [ ] **பிழை விகிதம்**: முந்தைய நிலைமையைவிட 400/401/404 பிழைகள் கூடாது.

### வழங்கவேண்டியவை

- தொகுப்பு மாற்றப்பட்ட கோப்புகளை, பழைய அழைப்புகளின் எண்ணிக்கையை முன்பும் பின்னரும், அடுத்து எடுக்கும் படிகளை உள்ளடக்கும்.
- மாற்றங்கள் வேலைநாட் திருத்தங்கள் மட்டுமே (கமிட் இல்லை).

---

## SDK பதிப்பு தேவைகள்

| தொகுப்பு | குறைந்தபட்ச பதிப்பு |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | EntraID அங்கீகாரத்திற்கான நடுத்தர பதிப்பு |

---

## குறிப்பு வழிகாட்டிகள்

- [மாயாவியாக உள்ளடக்கக் குறியீடுகள் — எல்லா குறியீட்டும்](./references/cheat-sheet.md)
- [சோதனை மாற்றம் — மோகிகள், ஸ்நாப்ப்ஷாட்கள், உறுதிப்படுத்தல்கள்](./references/test-migration.md)
- [பிழை தீர்வு — பிழைகள், ஆபத்து அட்டவணை, கெட்டதனங்கள்](./references/troubleshooting.md)
- [detect_legacy.py — தானியங்கி ஸ்கானர்](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [ஏசூர் OpenAI தொடக்க தொகுப்பு](https://aka.ms/openai/start)
- [ஏசூர் OpenAI Responses API ஆவணங்கள்](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [ஏசூர் OpenAI API பதிப்பு ஆயுள்](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API குறிப்பு](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->