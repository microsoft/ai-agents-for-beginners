---
name: azure-openai-to-responses
license: MIT
---
# Azure OpenAI Chat Completions-இல் இருந்து Responses API-க்கு Python செயலிகளை இடமாற்றம் செய்யவும்

> **அதிகாரப்பூர்வ வழிகாட்டல் — சரியாக பின்பற்றவும்**
>
> இந்த திறன் Azure OpenAI Chat Completions பயன்படுத்தும் Python குறியீட்டு அடுக்குகளை
> ஒருங்கிணைக்கப்பட்ட Responses API-க்கு இடமாற்றம் செய்கிறது. இந்த அறிவுரைகளை சரியாக பின்பற்றவும்.
> அளவுரு பொருத்தங்களை தற்காலிகமாக மாற்றவோ API வடிவங்களை கண்டுபிடிக்கவோ முயல belonging

---

## தூண்டுதல்கள்

பயனர் விரும்பும் போது இந்த திறனை இயக்கவும்:
- Azure OpenAI Chat Completions-இல் இருந்து Responses APIக்கு Python செயலியை இடமாற்றம் செய்ய
- Azure OpenAIக்கான Python OpenAI SDK பயன்பாட்டை புதிய API வடிவத்திற்கு மேம்படுத்த
- Azure Responses-இல் Responses தேவைப்படுகின்ற GPT-5 அல்லது புதிய மாதிரிகளுக்கான Python குறியீட்டை தயாரிக்க
- `AzureOpenAI`/`AsyncAzureOpenAI` இருந்து v1 முடிவிடல் கொண்ட வழக்கம் `OpenAI`/`AsyncOpenAI` கிளையண்டுக்கு மாற
- `AzureOpenAI` கட்டமைப்புகள் அல்லது `api_version` தொடர்புடைய பழைய அறிவிப்புகளை சரி செய்ய

---

## ⚠️ மாதிரி இணக்கத்தன்மை — முதலில் சோதிக்கவும்

> **இடமாற்றத்திற்கு முன், உங்கள் Azure OpenAI நிறுவல் Responses API-ஐ ஆதரிக்கிறதா என்று உறுதி செய்யவும்.**

### 1. உங்கள் நிறுவலை விரைவான சோதனை செய்க

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

> **குறிப்பு**: Azure OpenAIவில் `max_output_tokens` குறைந்தபட்சம் 16 ஆகவே இருக்க வேண்டும். 16 கீழான மதிப்புகள் 400 பிழையை அளிக்கும். விரைவான சோதனைக்கு 50க்கும் மேல் பயன்படுத்தவும்.

இது 404 ஐ தருமானால், அந்த நிறுவலின் மாதிரி Responses API-ஐ இன்னும் ஆதரிக்கவில்லை — கீழ்க்கண்ட குறிப்பு பாருங்கள் அல்லது ஆதரவு பெற்ற மாதிரியுடன் மீண்டும் நிறுவவும்.

### 2. உங்கள் பிராந்தியத்தில் கிடைக்கும் மாதிரிகளைச் சரிபார்க்கவும் (பரிந்துரைக்கப்பட்டது)

உங்கள் குறிப்பிட்ட பிராந்தியத்தில் Responses API ஆதரவுடன் கிடைக்கும் மாதிரிகளை காண ஏற்கனவே உள்ள மாதிரி இணக்கத்தன்மை கருவியை இயக்கவும்:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Azure ARM நேரடி கோரிக்கையை இந்த ஸ்கிரிப்ட் செய்கின்றது மற்றும் ஒரு இணக்கத்தன்மை அட்டவணையை காட்டுகிறது — எந்த மாதிரிகள் Responses, கட்டமைக்கப்பட்ட வெளியீடு, கருவிகள் மற்றும் பிற ஆதரிக்கின்றன என்பதை. `--filter gpt-5.1,gpt-5.2` கொண்டு முடிவுகளை குறைக்கவோ `--json` கொண்டு ஸ்கிரிப்டிங் செய்யவோ பயன்படவும்.

### 3. முழு மாதிரி ஆதரவுக்கான குறிப்பு

- **நேரடி கோரிக்கை**: `python migrate.py models` (மேலே பார்த்தது — பிராந்திய-சால், எப்போதும் புதுப்பிக்கபடும்)
- **கிடைக்கும் விவரம்**: [மாதிரி சுருக்க அட்டவணை மற்றும் பிராந்திய கிடைக்கும் விவரம்](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **விரைவான தொடக்கம் மற்றும் வழிகாட்டி**: **https://aka.ms/openai/start**

### ⚠️ பழைய மாதிரிகளின் கட்டுப்பாடுகள்

> **எச்சரிக்கை**: பழைய மாதிரிகள் (எ.கா., `gpt-4o`, `gpt-4`) Responses API அம்சங்களை முழுமையாக ஆதரிக்காமல் இருக்கலாம்.
>
> பழைய மாதிரிகளுடன் பரிச்சிதமான கட்டுப்பாடுகள்:
> - **`reasoning` அளவுரு**: `gpt-4o-mini`, `gpt-4o`, மற்றும் பல reasoning செய்யாத மாதிரிகளில் ஆதரிக்கப்படவில்லை. முதலில் இருந்த குறியீட்டில் இருந்தால் மட்டும் `reasoning` இடமாற்றம் செய்ய வேண்டும்.
> - **`seed` அளவுரு**: Responses APIயில் முழுவதுமாக ஆதரிக்கப்படவில்லை — அனைத்து கோரிக்கைகளிலும் நீக்கவும்.
> - **`text.format` வழியாக கட்டமைக்கப்பட்ட வெளியீடு**: பழைய மாதிரிகள் `strict: true` JSON விளக்கங்களை நம்பகமாக அமல்படுத்தாமலிருக்கலாம்.
> - **கருவி ஒருங்கிணைப்பு**: GPT-5+ கருவி அழைக்கைகள் உள் காரணத்திற்கான reasoning பகுதியாக ஒருங்கிணைக்கின்றன. Responses-இல் பழைய மாதிரிகள் இயங்கும் ஆனால் இந்த ஆழ்ந்த ஒருங்கிணைப்படுத்தல் இல்லாது.
> - **தெப்பவரி கட்டுப்பாடுகள்**: `gpt-5` இடமாற்றத்தில், வெப்பத்தை தவிர்க்கவோ அதனை `1` ஆக அமைக்கவோ வேண்டும். பழைய மாதிரிகளுக்கு இது கட்டாயம் இல்லை.

### O-வரிசை reasoning மாதிரிகள் (o1, o3-mini, o3, o4-mini)

O-வரிசை மாதிரிகளுக்கு தனித்துவமான அளவுரு கட்டுப்பாடுகள் உள்ளன. o-வரிசை மாதிரிகளை குறிவைக்கும் செயலிகளை இடமாற்றம் செய்யும்போது:

- **`temperature`**: `1` ஆகவே இருக்க வேண்டும் (அல்லது தவிர்க்கப்படும்). O-வரிசை மாதிரிகள் பிற மதிப்புகளைக் பெறாது.
- **`max_completion_tokens` → `max_output_tokens`**: Azure-சார்ந்த `max_completion_tokens` பயன்படுத்துபவை `max_output_tokens`-க்கு மாற வேண்டும். reasoning tokens வரம்பிற்கு எதிராக எண்ணப்படுவதால் உயர் மதிப்புகள் (4096+) அமைக்கவும்.
- **`reasoning_effort`**: செயலி `reasoning_effort` (குறைவு/மাঝம்/அதிகம்) பயன்படுத்தினால், அதைப் பயன்படுத்தத் தொடங்கவும் — Responses API இந்த அளவுருவை o-வரிசை மாதிரிகளுக்கு ஆதரிக்கிறது.
- **ஓடுதல் (Streaming) நடத்தை**: O-வரிசை மாதிரிகள் reasoning முடிந்தவரை வெளியீட்டை தணிக்கலாம் முன்னர் எழுத்து மாற்ற நிகழ்வுகளை வெளியிடுவதற்கு முன். ஓடுதல் நிகழ்கிறது, ஆனால் முதல் `response.output_text.delta` GPT மாதிரிகளுடன் ஒப்பிடுகையில் நீண்ட தாமதத்துடன் வரலாம்.
- **`top_p`**: O-வரிசையில் ஆதரிக்கப்படாது — இருந்தால் நீக்கவும்.
- **கருவி பயன்பாடு**: O-வரிசை மாதிரிகள் Responses API வழியாக கருவிகளை GPT மாதிரிகள் போல ஆதரிக்கின்றன, ஆனால் கருவி அழைப்பு ஒருங்கிணைப்பின் தரம் மாதிரி வேறுபடலாம்.

**செயல் — முன்கூட்டிய மாதிரி அறிவுரை**: ஸ்கேன் பகுதியில், செயலி குறிவைக்கும் மாதிரியை (நிறுவல் பெயர்கள், சூழல் மாறிகள், அமைப்பு) சரிபார்க்கவும். மாதிரி `gpt-4o` அல்லது பழைய (gpt-4.1+ அல்ல) என்றால் பயனருக்கு முன்கூட்டியே சொல்வது:
- அடிப்படையான எழுத்து, அரட்டை, ஓடுதல் மற்றும் கருவி பயன்பாட்டிற்கான இடமாற்றம் இயentliche நடக்கும்.
- புதிய மாதிரிகள் (`gpt-5.1`, `gpt-5.2`) சிறந்த கருவி ஒருங்கிணைப்பு, கட்டமைக்கப்பட்ட வெளியீடு கட்டாயம், காரணமுற்றல் மற்றும் பிராந்திய கடந்து கிடைக்கும் வசதிகளை வழங்குகின்றன.
- தயாராக இருந்தால் நிறுவலை மேம்படுத்த பரிந்துரைக்கப்படுகிறது — இடமாற்றத்தை தடுக்கும் நிலை இல்லை.

மாதிரி பதிப்பின் அடிப்படையில் இடமாற்றத்தை தடுப்பதோ மறுப்பதோ செய்ய வேண்டாம். அறிவுரைகள் தகவல்தொடர்புக்காகவுள்ளது.

### GitHub Models Responses API-ஐ ஆதரிக்காது

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) Responses API-ஐ ஆதரிக்காது.**

குறியீடு GitHub Models பாதையை கொண்டிருந்தால் (`base_url` `models.github.ai` அல்லது `models.inference.ai.azure.com` நோக்கி இருந்தால்), **இடமாற்றத்தின் போது முழுமையாக அகற்றவும்**. Responses API-க்கு Azure OpenAI, OpenAI, அல்லது செம்மையான உள்ளூர் முடிவிடல் (எ.கா., Ollama Responses ஆதரவு உடன்) தேவைப்படுகிறது.

ஸ்கேன் செய்கையில் செயல்:
- GitHub Models குறியீட்டு பாதைகள் அகற்றுவதற்கு குறிக்கவும்.

---

## கட்டமைப்பு இடமாற்றம்

பல செயலிகள் OpenAI மேலே உயர் நிலை கட்டமைப்புகளை பயன்படுத்துகின்றன. இவற்றை இடமாற்றும்போது, கட்டமைப்பின் சொந்த API மாற்றங்கள் — OpenAI அழைப்புகளை மட்டும் மாற்றுதல் அல்ல.

### Microsoft Agent Framework (MAF)

**உங்கள் MAF பதிப்பை முதலில் சரிபார்க்கவும்** — இடமாற்றம் MAF 1.0.0+ அல்லது முன்-1.0.0 பீட்டா/RC என்றதைக் கருதி நடக்கும்.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ஏற்கனவே Responses API-யைப் பயன்படுத்துகிறது** — இடமாற்றம் தேவையில்லை. பழைய `OpenAIChatCompletionClient` (இது `chat.completions.create` பயன்படுத்துகிறது) இருந்தால் `OpenAIChatClient`-ஆக மாற்றவும்.

| முந்தையது | பிறகு |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

உங்கள் பதிப்பை சரிபார்க்க: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF முன்-1.0.0 (பீட்டா/RC வெளியீடுகள்)

முன்-1.0.0 MAF-இல், `OpenAIChatClient` Chat Completions பயன்படுத்தியது. `agent-framework-openai>=1.0.0`க்கு மேம்படுத்தவும், இது Responses API பாவனை செய்கிறது.

பிற மாற்றங்கள் தேவையில்லை — `Agent` மற்றும் கருவி APIகள் அதேபோல் இருக்கும்.

### LangChain (`langchain-openai`)

`ChatOpenAI()`-க்கு `use_responses_api=True` சேர்க்கவும். பதில் அணுகலை `.content` இருந்து `.text` ஆக மாற்றவும்.

| முந்தையது | பிறகு |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

முழுமையான முந்தைய/பிறகு குறியீடு உதாரணங்களுக்கு [cheat-sheet.md](./references/cheat-sheet.md) பார்க்கவும்.

---

## முன்னணி இடமாற்றக் கையேடு

> **Responses API என்பது சர்வர்-பக்க கவலை.** உங்கள் Python பின்தளத்தை இடமாற்றவும்; முன்னணி HTTP ஒப்பந்தம் மாற்றம் தேவையில்லை, உங்கள் பின்தளம் பாச்சுமானால் — அந்த சூழலில் Responses கோரிக்கை வடிவத்தை ஏற்றுக்கொண்டு மொழிபெயர்ப்பு அடுக்கு அகற்றலாம். முன்னணி நேரடி OpenAI அழைப்புகள் இருந்தால் அவற்றை முதலில் பின்தளத்திற்கு மாற்றவும்.

### `@microsoft/ai-chat-protocol` பழையதாக உள்ளது

`@microsoft/ai-chat-protocol` npm தொகுப்பு பழையதாகி [[ndjson-readablestream](https://www.npmjs.com/package/ndjson-readablestream)]-ஆல் மாற்றப்பட வேண்டும். முன்னணியில் இதை கண்டால்:

1. CDN ஸ்கிரிப்ட் குறியீட்டை மாற்றவும்:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` உருவாக்கல் (`new ChatProtocol.AIChatProtocolClient("/chat")`) நீக்கவும்.
3. `client.getStreamedCompletion(messages)`-ஐ நேரடி `fetch()` பின்தள ஓடுநிலை முடிவுடலை அழைக்கும் வகையில் மாற்றவும்.
4. `for await (const response of result)`-ஐ `for await (const chunk of readNDJSONStream(response.body))` ஆக மாற்றவும்.
5. சொத்துக்களை `response.delta.content` / `response.error` இருந்து `chunk.delta.content` / `chunk.error` என மாற்றவும்.

---

## குறிக்கோள்கள்

- Azure OpenAIக்கு எதிரான Chat Completions அல்லது பழைய Completions பயன்படுத்தும் அனைத்து Python அழைப்பை உள்ளடக்க உரிய இடங்களை பட்டியலிடுக.
- Python குறியீடு அடுக்கிற்கான இடமாற்றம் திட்டம் மற்றும் வரிசையை முன்மொழியவும்.
- Responses APIக்கு மாற்ற பாதுகாப்பான, குறைந்த அளவு திருத்தங்களை செய்யவும்.
- அழைப்பாளர்களை Responses வெளியீட்டு விளக்கத்தைப் பயன்படுத்தும் முறைக்குக் கற்றுக்கொள்ளவும்; பின்வட்டகம் அடுக்குக்களை தவிர்க்கவும்.
- சோதனைகள்/தவறுகளை ஓட்டவும்; இடமாற்றத்தால் ஏற்படும் அசல் தடைகளை சரிசெய்யவும்.
- சிறிய, விமர்சனமான மாற்ற தொகுதிகளையும் இறுதியான சுருக்கத்துடன் (இணைப்புகளுடன்) வழங்கவும் (உருவாக்கவேண்டாம்).

---

## பாதுகாப்புக் கட்டுப்பாடுகள்

- கோப்புகளை மட்டும் git வேலையிடலுக்குள் மாற்றவும். வெளியே எழுத வேண்டாம்.
- பின்வட்டக இணக்கத்தன்மை அடுக்குக்களை காப்பாற்ற வேண்டாம்; குறியீடு புதிய API வடிவத்திற்கு இடமாற்றவும்.
- தொட்டுப் போன மதிப்புரை/மாற்றுக் குறிப்புகள் அல்லது காப்பு கோப்புகள் இடமாட்ட வேண்டாம்.
- முன்பு வாசனை ஓடுதலை (streaming) பயன்படுத்தினால் அதனை காப்பாற்றவும்; இல்லையேல் தவிர் ஓடுதலை பயன்படுத்தவும்.
- ஒப்புதல் முறையில் இருந்தால் கட்டளைகள் அல்லது நெட்வொர்க் அழைப்புகளில் முன் அனுமதி கேட்கவும்.
- `git add`/`git commit`/`git push` இயங்கவிட வேண்டாம்; வேலைசெய்யும் மரத்தைத் திருத்தங்கள் மட்டுமே செய்யவும்.

---

## படி 0: Azure OpenAI கிளையண்ட் இடமாற்றம் (முன்னோட்டம்)

குறியீடில் `AzureOpenAI` அல்லது `AsyncAzureOpenAI` கட்டமைப்புகள் இருந்தால், முதலில் வழக்கமான `OpenAI` / `AsyncOpenAI` கட்டமைப்புக்கு மாற்றவும். Azure-சார்ந்த கட்டமைப்புகள் `openai>=1.108.1`-இல் பழையதாகியுள்ளன.

### ஏன் v1 API பாதை?

புதிய `/openai/v1` முடிவிடல் வழக்கமான `OpenAI()` கிளையண்டைப் பயன்படுத்துகிறது `AzureOpenAI()` இல்லாமல், `api_version`-ஆவளை தேவையில்லை, OpenAI மற்றும் Azure OpenAI இரண்டிலும் ஒரே மாதிரியான செயல்பாடு உள்ளது. அதே கிளையண்ட் குறியீடு எதிர்காலத்துக்கு பொருந்தும் — பதிப்பு நிர்வகிப்பு தேவையில்லை.

### முக்கிய மாற்றங்கள்

| முந்தையது | பிறகு |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | முழுமையாக அகற்றவும் |

### சுத்திகரிப்பு செயற்பட்டியியல்

- கிளையண்ட் உருவாக்கத்தில் `api_version` அளவுருவை அகற்றவும்.
- `.env`, செயலி அமைப்புகள், Bicep/உள்ளமைப்பு கோப்புகளில் இருந்து `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` சூழல் மாறிகளை அகற்றவும்.
- `.env`, செயலி அமைப்புகள், Bicep/உள்ளமைப்பில் `AZURE_OPENAI_CLIENT_ID`-ஐ `AZURE_CLIENT_ID` ஆக மறுபெயரிடவும் (சாதாரண Azure Identity SDK மரபு).
- `requirements.txt` அல்லது `pyproject.toml`-இல் `openai>=1.108.1` இருப்பதை உறுதி செய்யவும்.

### சூழல் மாறி இடமாற்றம்

| பழைய சூழல் மாறி | செயல் | குறிப்பு |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **அகற்றவும்** | v1 முடிவிலைப் பயன்படுத்த api_version தேவையில்லை |
| `AZURE_OPENAI_API_VERSION` | **அகற்றவும்** | மேலே கூறியது போல |
| `AZURE_OPENAI_CLIENT_ID` | **மறுபெயரிடவும்** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)` க்கான சாதாரண Azure Identity SDK மரபு |
| `AZURE_OPENAI_ENDPOINT` | **காப்பாற்றவும்** | இன்னும் `base_url` கட்டமைப்புக்கு தேவைப்படும் |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **காப்பாற்றவும்** | `responses.create`-இல் `model` அளவுருவாக பயன்படுத்தப்படும் |
| `AZURE_OPENAI_API_KEY` | **காப்பாற்றவும்** | விசை-அடிப்படையிலான அங்கீகாரத்துக்கு `api_key` ஆக பயன்படுத்தப்படும் |

கிளையண்ட் அமைப்பு குறியீட்டு (sync, async, EntraID, API விசை, பன்முக வாடிக்கையாளர்) உதாரணங்களுக்காக [cheat-sheet.md](./references/cheat-sheet.md) பார்க்கவும்.

---

## படி 1: பழைய அழைப்புகளை கண்டறிதல்

இடமாற்றம் தேவைப்படும் அனைத்து அழைப்புகளை கண்டுபிட md; detect_legacy.py ஸ்கிரிப்டைப் பயன்படுத்தவும்:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

அல்லது இந்த தேடலை கையேடாக செய்துகொள்ளவும் — ஒவ்வொரு பொருத்தலும் இடமாற்ற குறியீடு:

```bash
# பாரம்பரிய API அழைப்புகள் (மீண்டும் எழுத வேண்டும்)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# பழமைவாய்ந்த Azure கிளையன்ட் கட்டமைப்பாளர்கள் (மாற்ற வேண்டும்)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# பதில் வடிவ அணுகல் முறைகள் (புதுப்பிக்க வேண்டும்)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# பழைய அடுக்குக்குள் குறியீட்டு கருவிகள் வரையறைகள் (சிறிது மாற்ற வேண்டும்)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# கருவி முடிவுகள் பழைய வடிவில் (function_call_output ஆக மாற்ற வேண்டும்)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# பழைய அளவுருக்கள் (அகற்ற அல்லது பெயர் மாற்ற வேண்டும்)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens என்று பெயர் மாற்றவும்
rg "['\"]seed['\"]"      # remove entirely

# பழைய சூழல் மாறிகள் (சுத்தம் செய்யவும்)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # இது AZURE_CLIENT_ID ஆக இருக்க வேண்டும்

# GitHub Models முடியும் கள்கள் (அகற்ற வேண்டும் — Responses API ஆதரிக்கவில்லை)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# கட்டமைப்புச் நிலை பாரம்பரிய முறைகள் (புதுப்பிக்க வேண்டும்)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient உடன் மாற்றவும்
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True என்றதைப் பயன்படுத்த வேண்டும்

# சோதனை அடித்தளம் (புதுப்பிக்க வேண்டும்)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# உள்ளடக்க பரிசோதகர் பிழை உடல் அணுகல் (புதுப்பிக்க வேண்டும் — அமைப்பு மாற்றப்பட்டது)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # பழைய ஒருமைப் போல் — இப்போது content_filter_results (பலமைப்படுத்தப்பட்டவை) content_filters வரிசையில் உள்ளன

# Chat Completions முடிக்கும் களத்திற்கு நேரடி HTTP அழைப்புகள் (URL புதுப்பிக்கவேண்டும்)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### heuristic (கண்டுபிடித்து மறுஅழைப்பு)

- **Chat Completions client**: `client.chat.completions.create` → `client.responses.create(...)`.

- **அஜூரு கிளையன்ட் கான்ஸ்ட்ரக்டர்கள்**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **கருவிகள்**: நெஸ்டட் வடிவிலிருந்து ( `{"type": "function", "function": {"name": ...}}` ) செயல்பாடு-கால் கருவி வரையறைகளை நிழலற்ற பதில்கள் வடிவத்திற்கு மாற்றவும் ( `{"type": "function", "name": ...}` ); `tool_choice` ஐப் பயன்படுத்தவும்; கருவி முடிவுகளை `{"type": "function_call_output", "call_id": ..., "output": ...}` பொருட்களாகக் கொடுக்கவும் ( `{"role": "tool", ...}` அல்ல).
- **கருவி சுற்றுப்பயணங்கள்**: மODEல் செயல்பாடு அழைப்புகளை திருப்பும்போது, உரையாடலுக்கு `response.output` பொருட்களைச் சேர்க்கவும் (கைமுறையில் `{"role": "assistant", "tool_calls": [...]}` அகராதி அல்ல), பின்னர் ஒவ்வொரு முடிவிற்கும் `function_call_output` பொருட்களையும் சேர்க்கவும்.
- **குறைந்த-காட்சி கருவி உதாரணங்கள்**: உரையாடலில் கடினமாக குறிக்கப்பட்ட கருவி அழைப்பு உதாரணங்கள் இருந்தால், அவற்றை `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` பொருட்களாக மாற்றவும். ஐடிஎக்கள் `fc_` உடன் தொடங்கவேண்டும்.
- **`pydantic_function_tool()`**: இந்த உதவியாளர் இன்னும் பழைய நெஸ்டட் வடிவத்தை உருவாக்குகிறது மற்றும் `responses.create()` உடன் **சம்மதி இல்லை**. கையேடு கருவி வரையறைகள் அல்லது ஒரு நிழலற்ற ரேப்பர் பயன்படுத்தவும்.
- **பல-முறை**: செயலியில் உரையாடல் வரலாற்றை பராமரிக்கவும்; முந்தைய சுற்றுக்களை `input` பொருட்களாக எடுத்துச் செல்லவும்.
- **வடிவமைப்பு**: Chat ஓர் உச்ச நிலை `response_format` ஐ Responses இல் `text.format` ஆக மாற்றவும். வழக்கமான வடிவம்: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **உள்ளடக்க பொருட்கள்**: Chat இன் `content[].type: "text"` ஐ Responses இல் `content[].type: "input_text"` ஆக மாற்றவும், பயனர்/கணினி திருப்புகளுக்கு.
- **பட உள்ளடக்க பொருட்கள்**: Chat இன் `content[].type: "image_url"` ஐ Responses இல் `content[].type: "input_image"` ஆக மாற்றவும். `image_url` புலம் நெஸ்டட் பொருள் `{"url": "..."}` இருந்து நேர்த்தியான சரமாக மாறுகிறது. முன்/பின்னர் உதாரணங்கள் கற்குக்கோவையில் காண்க.
- **காரண முயற்சி**: **அசல் குறியீட்டில் தவிர்க்கப்படும் `reasoning` மட்டும் குடுத்தல்.**
- **உள்ளடக்க வடிகட்டும் பிழை கையாளல்**: பிழை உடல் வடிவம் மாறியுள்ளது. Chat Completions நுட்பமாக `error.body["innererror"]["content_filter_result"]` (ஒற்றை) பயன்படுத்தியிருந்தது; Responses API `error.body["content_filters"][0]["content_filter_results"]` (பன்மை, வரிசை உள்ளே) பயன்படுத்துகிறது. `innererror` அணுகும் குறியீடுகள் `KeyError` எழுப்பும். புதிய பாதையை எழுதுங்கள்.
- **மூடிரல் HTTP அழைப்புகள்**: செயலி நேரடியாக Azure OpenAI REST API ஐ (/openai/deployments/{name}/chat/completions?api-version=...) பயன்படுத்துமானால், அதை /openai/v1/responses ஆக மறு எழுதி உடல் மாற்றங்களைச் செய்யவும்: `messages` → `input`, `max_output_tokens` ஐச் சேர்க்கவும் மற்றும் `store: false` ஐச் சேர்க்கவும், `api-version` குவேரி பராமரிப்பை நீக்கவும். பதில் உடல்: `choices[0].message.content` → `output[0].content[0].text` (குறிப்பு: `output_text` என்பது எளிய REST JSON இல் காணாத ஒரு SDK உதவிப் பண்புருவாகும்).

---

## படி 2: மாற்றத்தை செயல்படுத்தவும்

### மாற்ற குறிப்புகள் (Chat Completions → Responses)

- **ஏன் மாற்றுவது**: Responses என்பது உரை, கருவிகள் மற்றும் ஸ்ட்ரீமிங் க்கான ஒருசேர API; Chat Completions என்பது பழையது. GPT-5 உடன், Responses சிறந்த செயல்திறனுக்காக தேவையானது.
- **HTTP**: Azure எண்ட்பாயின்ட் `/openai/deployments/{name}/chat/completions` இருந்து `/openai/v1/responses` ஆக மாறுகிறது.
- **புலங்கள்**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` மாற்றமில்லை.
- **வடிவமைப்பு**: `response_format` → `text.format` ஒரு உருப்படி ஆக.
- **உள்ளடக்க பொருட்கள்**: Chat இன் `content[].type: "text"` ஐ Responses இன் `content[].type: "input_text"` ஆக மாற்றவும், கணினி/பயனர் திருப்புகளுக்கு.
- **பட உள்ளடக்க பொருட்கள்**: Chat இன் `content[].type: "image_url"` ஐ Responses இல் `content[].type: "input_image"` ஆக மாற்றவும். `image_url` புலத்தை `{"image_url": {"url": "..."}}` இருந்து `{"image_url": "..."}` (ஒரு நேரடியான சரம் — HTTPS URL அல்லது `data:image/...;base64,...` தரவு URI) ஆக எளிமைப்படுத்தவும்.

### அளவுகோல் வரைபடம் குறிப்பு

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (பொருட்களைக் கொண்ட பட்டியல்) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (உருப்படி) |
| `temperature` | `temperature` (மாற்றமில்லை) |
| `stop` | `stop` (மாற்றமில்லை) |
| `frequency_penalty` | `frequency_penalty` (மாற்றமில்லை) |
| `presence_penalty` | `presence_penalty` (மாற்றமில்லை) |
| `tools` / function-calling | `tools` (மாற்றமில்லை) |
| `seed` | **நீக்கவும்** (ஆதரிக்கப்படவில்லை) |
| `store` | `store` ( `false` ஆக அமைக்கவும்) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (நேர்த்தியான சரம்) |

முழுமையான முன்/பின் குறியீடு உதாரணங்களுக்கு, [cheat-sheet.md](./references/cheat-sheet.md) காண்க.

சோதனை அடிப்படைய மாற்றம் (mocks, snapshots, assertions) பற்றியும் [test-migration.md](./references/test-migration.md) பார்.

பிழைகள் மற்றும் சிக்கல்கள் தொடர்பான உதவிக்கு [troubleshooting.md](./references/troubleshooting.md) பார்.

---

## தரவு காப்பாற்றல் & நிலை

- அனைத்து Responses கோரிக்கைகளிலும் `store: false` அமைக்கவும்.
- முந்தைய செய்தி ஐடிகள்போன்றவையோ அல்லது சர்வர்-சேமிக்கப்பட்ட குறைந்தபட்ச சூழலை நம்ப வேண்டாம்; நிலையை கிளையன்ட் கையாளவும் மற்றும் மெட்டாஎடாவை குறைக்கவும்.

---

## ஏற்றுக்கொள்ளும் நிபந்தனைகள்

### குறியீடு நிலை கதவுகள் (அனைத்தும் கடக்க வேண்டும்)

- [ ] மாற்றிய கோப்புகளில் `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` எங்கேயும் இல்லாமை.
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` எங்கேயும் இல்லை — அனைத்து கட்டமைப்புகள் `OpenAI`/`AsyncOpenAI` உடன் v1 எண்ட்பாயிண்ட் பயன்படுத்தும்.
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` எங்கேயும் இல்லை — GitHub மாடல்கள் குறியீடு பாதைகள் நீக்கப்பட்டன.
- [ ] `rg "OpenAIChatCompletionClient"` இல்லை — MAF 1.0.0+ குறியீடு `OpenAIChatClient` பயன்படுத்தும் (இது Responses API பயன்படுத்துகிறது). முன்னர் 1.0.0, `agent-framework-openai>=1.0.0` க்கு மேம்படுத்து.
- [ ] அனைத்து `ChatOpenAI(...)` அழைப்பிலும் `use_responses_api=True` உள்ளது.
- [ ] `rg "choices\[0\]"` எங்கேயும் இல்லை — அனைத்து பதிலடி அணுகல் `resp.output_text` அல்லது Responses வெளியீட்டு வடிவமைப்பை பயன்படுத்துகிறது.
- [ ] உச்ச நிலை `response_format` இல்லை; அனைத்து கட்டமைக்கப்பட்ட வெளியீடு `text={"format": {...}}` வடிவத்தைப் பயன்படுத்துகிறது.
- [ ] `openai>=1.108.1` மற்றும் `azure-identity` `requirements.txt` அல்லது `pyproject.toml` இல் உள்ளது; சார்புகள் மீண்டும் நிறுவப்பட்டன.
- [ ] அனைத்து `responses.create` அழைப்பிலும் `store=False` அமைக்கப்பட்டுள்ளது.
- [ ] கிளையன்ட் கட்டமைப்பில் `api_version` இல்லை; `AZURE_OPENAI_API_VERSION` சுற்றுச்சூழல் கோப்புகளிலிருந்தும் மற்றும் கட்டமைப்பிலிருந்தும் நீக்கப்பட்டது.

### சோதனை அடிப்படைய கதவுகள் (அனைத்தும் கடக்க வேண்டும்)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` எங்கேயும் இல்லை.
- [ ] `rg "_azure_ad_token_provider" tests/` இல்லை — உறுதிப்படுத்தல்கள் `isinstance(client, AsyncOpenAI)` அல்லது `base_url` ஐ சரிபார்க்கும்.
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` இல்லை — Azure-சூழல் வடிகட்டு மாக்குகள் நீக்கப்பட்டன.
- [ ] மாக் பொருட்கள் `kwargs.get("input")` பயன்படுத்தும், `kwargs.get("messages")` அல்ல.
- [ ] ஸ்னாப்ஷாட் / கோல்டன் கோப்புகள் Responses ஸ்ட்ரீமிங் வடிவத்திற்கு புதுப்பிக்கப்பட்டவை (`choices[0]`, `function_call`, `logprobs` இல்லை).
- [ ] அனைத்து சோதனைகளும் `pytest` உடன் தோல்வியில்லாமல் கடக்கின்றன.

### நடத்தை கதவுகள் (கைமுறையில் அல்லது சோதனை கணினியில் சரிபார்க்கவும்)

- [ ] **அடிப்படைக் முடிவு**: non-streaming `responses.create` செல்லும் போது வெற்று அல்லாத `output_text` திருப்புகிறது.
- [ ] **ஸ்ட்ரீம் சமம்**: அசல் குறியீடு ஸ்ட்ரீமிங் பயன்படுத்தினால், மாற்றிய குறியீடு ஸ்ட்ரீமான மற்றும் வெற்று அல்லாத `response.output_text.delta` நிகழ்வுகளை வழங்கும்.
- [ ] **கட்டமைக்கப்பட்ட வெளியீடு**: `text.format` உடன் `json_schema` பயன்படுத்தினால், `json.loads(resp.output_text)` வெற்றிகரமாக இயங்கும் மற்றும் வடிவமைப்புடன் பொருந்தும்.
- [ ] **கருவி-அழைப்பு சுற்று**: கருவிகள் பயன்படுத்தப்பட்டால், மODEல் கருவி அழைப்புகளை விடுத்து, செயலி அவற்றை இயக்கி, தொடர்ச்சியான கோரிக்கை இறுதி `output_text` (இன்ஃபைனிட் லூப் இல்லை) திருப்புகிறது.
- [ ] **ஆசிங்க் சமம்**: `AsyncAzureOpenAI` பயன்படுத்தினால், `AsyncOpenAI` இணையானது `await` உடன் வேலை செய்கிறது.
- [ ] **பிழை விகிதம்**: முந்தைய மாற்றம் முன்பணியுடன் ஒப்பிடுகையில் புதிய 400/401/404 பிழைகள் இல்லை.

### வழங்கப்பட வேண்டியவை

- தொகுப்பு கோப்புகள், பழைய அழைப்பு தளங்களின் முன்பும் பின் எண்ணிக்கைகள் மற்றும் அடுத்த படிகள் மற்றும் சுருக்கம்.
- மாற்றங்கள் வெர்சன் மரத்தில் மட்டும் (கமிட்டுகள் இல்லை).

---

## SDK பதிப்பு தேவைகள்

| தொகுப்பு | குறைந்தபட்ச பதிப்பு |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | சமீபத்தியது (EntraID அங்கீகாரத்திற்கானது) |

---

## குறிப்பு

- [அடுக்ககுறிப்பு — அனைத்து குறியீடு துண்டுகள்](./references/cheat-sheet.md)
- [சோதனை மாற்றம் — மாக்கள், ஸ்னாப்ஷாட்கள், உறுதிப்படுத்தல்கள்](./references/test-migration.md)
- [பிழை தீர்வு — பிழைகள், அபாய அட்டவணை, சிக்கல்கள்](./references/troubleshooting.md)
- [detect_legacy.py — தானியங்கி ஸ்கானர்](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI தொடக்க குழு](https://aka.ms/openai/start)
- [Azure OpenAI Responses API ஆவணங்கள்](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API பதிப்பு வாழ்நாள்](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API குறிப்புகள்](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->