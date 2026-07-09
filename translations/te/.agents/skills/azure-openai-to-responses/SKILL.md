---
name: azure-openai-to-responses
license: MIT
---
# Azure OpenAI చాట్ కంప్లీషన్స్ నుండి Responses API కి Python యాప్‌లను మైగ్రేట్ చేయండి

> **అధికారం గల మార్గదర్శకాలు — ఖచ్చితంగా అనుసరించండి**
>
> ఈ స్కిల్ Azure OpenAI చాట్ కంప్లీషన్స్ ఉపయోగించే Python కోడ్‌బేస్‌లను unified Responses API కు మైగ్రేట్ చేస్తుంది.
> ఈ సూచనలను ఖచ్చితంగా అనుసరించండి.
> ప్యారామీటర్ మ్యాపింగ్‌లను అనుకోకూడదు లేదా API ఆకృతులను కనిపెట్టకూడదు.

---

## ట్రిగ్గర్స్

యూజర్ చేయాలనుకున్నపుడు ఈ స్కిల్‌ను సక్రియం చేయండి:
- Azure OpenAI చాట్ కంప్లీషన్స్ నుండి Responses API కు Python యాప్‌ను మైగ్రేట్ చేయండి
- Azure OpenAI కు సంబంధించి Python OpenAI SDK ఉపయోగం ని తాజా API ఆకృతికి అప్‌గ్రేడ్ చేయండి
- Responses అవసరమయ్యే GPT-5 లేదా కొత్త మోడల్‌లకు Python కోడ్ ని సిద్ధం చేయండి
- `AzureOpenAI`/`AsyncAzureOpenAI` నుండి స్టాండర్డ్ `OpenAI`/`AsyncOpenAI` క్లయింట్ v1 ఎండ్‌పాయింట్‌తో మార్చండి
- `AzureOpenAI` కన్స్ట్రక్టర్ల లేదా `api_version` కు సంబంధించిన డిప్రికేషన్ వార్నింగ్స్ ను సరిచేయండి

---

## ⚠️ మోడల్ అనుగుణత — ముందు తనిఖీ చేయండి

> **మైగ్రేషన్ చేసేముందు, మీ Azure OpenAI డిప్లాయ్మెంట్ Responses API ని మద్దతు ఇస్తుందో లేదో నిర్ధారించుకోండి.**

### 1. స్మోక్-టెస్ట్ చేయండి (అత్యంత వేగంగా)

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

> **గమనిక**: Azure OpenAI లో `max_output_tokens` కనీసం 16. 16 కన్నా తక్కువ విలువలకు 400 ఎర్రర్ వస్తుంది. స్మోక్ టెస్టులకు 50+ ఉపయోగించండి.

ఇది 404 ఇవ్విస్తే, డిప్లాయ్మెంట్‌లోని మోడల్ ఇంకా Responses ను మద్దతు ఇవ్వదు — దిగువ రిలేటెడ్ రిఫరెన్స్ చూసి లేదా మద్దతు ఉన్న మోడల్ తో తిరిగి డిప్లాయ్ చేయండి.

### 2. మీ రీజియన్‌లో అందుబాటులో ఉన్న మోడల్‌లను తనిఖీ చేయండి (సిఫార్సు చేయబడినది)

మీ ప్రత్యేక రీజియన్ లో Responses API మద్దతు ఉన్న మోడల్‌లు ఏమిటి అని చూడటానికి బిల్ట్-ఇన్ మోడల్ అనుగుణత టూల్‌ను అమలు చేయండి:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

ఇది Azure ARM ను ప్రత్యక్షంగా క్యూ చేసి అనుగుణత మ్యాట్రిక్స్ చూపిస్తుంది — ఏ మోడల్‌లు Responses, సట్రక్చర్డ్ అవుట్పుట్, టూల్స్ మద్దతు ఇస్తాయో. ఫలితాలను తగ్గించడానికి `--filter gpt-5.1,gpt-5.2` లేదా స్క్రిప్టింగ్ కోసం `--json` ఉపయోగించండి.

### 3. పూర్తి మోడల్ మద్దతు సూచిక

- **లైవ్ క్యూరి**: `python migrate.py models` (పైన చూడండి — ప్రత్యేక రీజియన్, ఎప్పుడూ తాజా)
- **అందుబాటులో ఉన్నవి బ్రౌజ్ చేయండి**: [Model summary table and region availability](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **క్విక్‌స్టార్ట్ & మార్గదర్శకాలు**: **https://aka.ms/openai/start**

### ⚠️ పాత మోడల్ పరిమితులు

> **చెతువు**: పాత మోడల్‌లు (ఉదా: `gpt-4o`, `gpt-4`) Responses API ఫీచర్లను పూర్తిగా మద్దతు ఇవ్వకపోవచ్చు.
>
> పాత మోడల్‌లకు తెలిసిన పరిమితులు:
> - **`reasoning` ప్యారామీటర్**: `gpt-4o-mini`, `gpt-4o`, మరియు అనేక నాన్-రీజనింగ్ మోడల్స్‌లో మద్దతు లేదు. అసలైన కోడ్‌లో `reasoning` ఇప్పటికే ఉంటే మాత్రమే అది మైగ్రేట్ చేయండి.
> - **`seed` ప్యారామీటర్**: Responses API లో పూర్తిగా మద్దతు లేదు — అన్ని రిక్వెస్టుల నుండి తొలగించాలి.
> - **`text.format` ద్వారా సట్రక్చర్డ్ అవుట్పుట్**: పాత మోడల్స్ `strict: true` JSON స్కీమాలను విశ్వసనీయంగా అమలు చేయకపోవచ్చు.
> - **టూల్ ఒర్చిస్ట్రేషన్**: GPT-5+ లో టూల్ కాల్స్ అంతర్గత reasoning భాగంగా ఉంటాయి. పాత మోడల్స్ Responses API లో పనిచేస్తాయి కానీ ఇదే లోతైన ఇంటిగ్రేషన్ లేరు.
> - **తాపనపరిమితులు**: `gpt-5`కు మైగ్రేట్ చేసే సమయంలో temperature తొలగించాలి లేదా `1` గా సెట్ చేయాలి. పాత మోడల్స్‌కు ఇలాంటి పరిమితి లేదు.

### O-సిరీస్ reasoning మోడల్స్ (o1, o3-mini, o3, o4-mini)

O-సిరీస్ మోడల్స్‌కు ప్రత్యేక ప్యారామీటర్ పరిమితులు ఉంటాయి. O-సిరీస్ మోడల్స్ కోసం ఇనుప్లికేషన్స్ చేస్తునప్పుడు:

- **`temperature`**: తప్పనిసరిగా `1` (లేదా మినహాయింపుగా). O-సిరీస్ మోడల్స్ ఇతర విలువలను అనుమతించవు.
- **`max_completion_tokens` → `max_output_tokens`**: Azure నిర్దిష్ట `max_completion_tokens` ఉపయోగించే యాప్స్ `max_output_tokens` కు మార్చాలి. reasoning టోకెన్లు పరిమితిని పెంచే కారణంగా పెద్ద విలువలు (4096+) సెట్ చేయండి.
- **`reasoning_effort`**: యాప్ `reasoning_effort` (low/medium/high) ఉపయోగిస్తే, దానిని ఉంచండి — Responses API O-సిరీస్ మోడల్స్ కి మద్దతు ఇస్తుంది.
- **స్ట్రీమింగ్ ప్రవర్తన**: O-సిరీస్ మోడల్స్ reasoning పూర్తయ్యేవరకు అవుట్పుట్ బఫర్ చేసి తర్వాతే టెక్స్ట్ డెల్టా ఈవెంట్స్ జారీ చేస్తాయి. స్ట్రీమింగ్ పనిచేస్తుంది, కానీ మొదటి `response.output_text.delta` GPT మోడల్స్ కన్నా ఆలస్యంగా వస్తుంది.
- **`top_p`**: O-సిరీస్‌లో మద్దతు లేదు — ఉంటే తీసివేయండి.
- **టూల్ వాడకం**: O-సిరీస్ మోడల్స్ Responses API ద్వారా టూల్స్ మద్దతు ఇస్తాయి గాను, టూల్ కాల్ ఒర్చిస్ట్రేషన్ నాణ్యత మోడల్ పైన ఆధారపడి ఉంటుంది.

**చర్య — ముందస్తుగా మోడల్ సలహా ఇవ్వండి**: స్కాన్ దశలో, యాప్ ఏ మోడల్‌ను టార్గెట్ చేస్తున్నదో (డిప్లాయ్‌మెంట్ పేర్లు, env vars, కాన్ఫిగ్) తనిఖీ చేయండి. మోడల్ `gpt-4o` లేదా పాతది అయితే (gpt-4.1+ కాదు), యూజర్‌ని ముందస్తు తెలపండి:
- వారి ప్రస్తుత మోడల్‌లో ప్రాథమిక టెక్స్ట్, చాట్, స్ట్రీమింగ్, టూల్స్ మైగ్రేషన్ పనిచేస్తుంది.
- కొత్త మోడల్‌లు (`gpt-5.1`, `gpt-5.2`) మెరుగైన టూల్ ఒర్చిస్ట్రేషన్, సట్రక్చర్డ్ అవుట్పుట్ అమలు, reasoning, మరియు క్రాస్-రిజియన్ అందుబాటు ఇస్తాయి.
- సిద్ధంగా ఉన్నపుడు వారి డిప్లాయ్‌మెంట్ అప్‌గ్రేడ్ చేయాలని వారు భావించాలి — ఇది మైగ్రేషన్‌కు అడ్డుపడదు.

మోడల్ వెర్షన్ ఆధారంగా మైగ్రేషన్ నిరోధించవద్దు లేదా తిరస్కరించవద్దు. సలహా మాత్రమే.

### GitHub మోడల్స్ Responses API ని మద్దతు ఇవ్వడం లేదు

> **GitHub మోడల్స్ (`models.github.ai`, `models.inference.ai.azure.com`) Responses API కి మద్దతు ఇవ్వవు.**

కోడ్‌బేస్‌లో GitHub మోడల్స్ కోడ్ పాథ్ ఉంటే (`base_url` `models.github.ai` లేదా `models.inference.ai.azure.com` వాటి వైపు ఉండటం చూడండి), మైగ్రేషన్ లో **అన్నింటిని తొలగించండి**. Responses API కు Azure OpenAI, OpenAI, లేదా Ollama వంటి అనుకూల స్థానిక ఎండ్‌పాయింట్ అవసరం.

స్కాన్ సమయంలో చర్య:
- GitHub మోడల్స్ కోడ్ పాథ్‌లను తొలగించడానికి సూచించండి.

---

## ఫ్రేమ్‌వర్క్ మైగ్రేషన్

చాలా యాప్‌లు OpenAI పై ఉన్న ఉన్నత-స్థాయి ఫ్రేమ్‌వర్క్‌లు ఉపయోగిస్తాయి. వీటిని మైగ్రేట్ చేసేటప్పుడు, ఫ్రేమ్‌వర్క్ యొక్క సొంత API మార్పులు ఉంటాయి — కేవలం పొలమేమైనా OpenAI కాల్స్ మాత్రమే కాదు.

### Microsoft ఏజెంట్ ఫ్రేమ్‌వర్క్ (MAF)

**ముందుగా మీ MAF వెర్షన్‌ని తనిఖీ చేయండి** — మైగ్రేషన్ MAF 1.0.0+ లేదా pre-1.0.0 బేటా/ఆర్‌సీ ఆధారపడి ఉంటుంది.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ఇప్పటికే Responses API ఉపయోగిస్తోంది** — మైగ్రేషన్ అవసరం లేదు. లెగసీ `OpenAIChatCompletionClient` (`chat.completions.create` ఉపయోగించే) ఉంటే, దాన్ని `OpenAIChatClient` తో మార్చండి.

| మునుపటి | తరువాత |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

మీ వెర్షన్ తెలుసుకోవడానికి: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (బేటా/ఆర్‌సీ విడుదలలు)

pre-1.0.0 MAF లో, `OpenAIChatClient` చాట్ కంప్లీషన్స్ ఉపయోగించేది. `agent-framework-openai>=1.0.0` కు అప్‌గ్రేడ్ చేయండి, అక్కడ `OpenAIChatClient` డీఫాల్ట్‌గా Responses API ఉపయోగిస్తుంది.

మరేదైనా మార్పులు అవసరం లేదు — `Agent` మరియు టూల్ API లు అదేవిధంగా ఉంటాయి.

### LangChain (`langchain-openai`)

`ChatOpenAI()` కి `use_responses_api=True` జోడించండి. రిస్పాన్స్ యాక్సెస్ ను `.content` నుండి `.text` కి మార్చండి.

| ముందుగా | తరువాత |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

పూర్తి ముందుకు/తర్వాత కోడ్ ఉదాహరణలకోసం [cheat-sheet.md](./references/cheat-sheet.md) చూడండి.

---

## ఫ్రంట్‌ఎండ్ మైగ్రేషన్ మార్గదర్శకాలు

> **Responses API సర్వర్-సైడ్ అంశం.** మీ Python బ్యాక్‌ఎండ్‌ను మైగ్రేట్ చేయండి; ఫ్రంట్‌ఎండ్ HTTP ఒప్పందం మారవద్దు, లేకపోతే బ్యాక్‌ఎండ్ ఒక తక్కువ-స్థాయి పాస్-త్రూ అయితే మాత్రమే — ఆ పరిస్థితిలో Responses రిక్వెస్ట్ ఆకృతిని స్వీకరించడం పరిగణించండి అనువాద పాథ్ తొలగించడానికి. ఫ్రంట్‌ఎండ్ డైరెక్ట్‌గా క్లీన్ సైడ్ కీతో OpenAI కాల్స్ చేస్తుంటే, ఆ కాల్స్ మొదట బ్యాక్‌ఎండ్‌కు మార్చండి.

### `@microsoft/ai-chat-protocol` డిప్రికేషన్

`@microsoft/ai-chat-protocol` npm ప్యాకేజీ డిప్రికేట్ అయింది, దీని స్థానంలో [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) ఉపయోగించండి. మీరు ఫ్రంట్‌ఎండ్‌లో దీన్ని చూసినపుడు:

1. CDN స్క్రిప్ట్ ట్యాగ్ మార్చండి:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` ఇనిస్టేషనేషన్ (`new ChatProtocol.AIChatProtocolClient("/chat")`) తీసివేయండి.
3. `client.getStreamedCompletion(messages)` ని ప్రత్యక్ష `fetch()` కాల్ తో బ్యాక్‌ఎండ్ స్ట్రీమింగ్ ఎండ్‌పాయింట్ కు మార్చండి.
4. `for await (const response of result)` ని `for await (const chunk of readNDJSONStream(response.body))` గా మార్చండి.
5. ప్రాపర్టీ యాక్సెస్‌ను `response.delta.content` / `response.error` నుండి `chunk.delta.content` / `chunk.error` కు మార్చండి.

---

## లక్ష్యాలు

- Azure OpenAI మీద Chat Completions లేదా లెగసీ Completions ఉపయోగించే అన్ని Python కాల్ సైట్లను లెక్కించడం.
- Python కోడ్‌బేస్ కోసం మైగ్రేషన్ ప్లాన్ మరియు క్రమ ప్రమాణాలని ప్రతిపాదించడం.
- Responses API కి స్వీచు చేయటానికి సురక్షితమైన, కనిష్ఠ ఎడిట్లను అనుప్రయోగించడం.
- Responses అవుట్పుట్ స్కీమాను వినియోగించటానికి కాలర్లను అప్‌డేట్ చేయడం; బ్యాక్‌కాంపాట్ వ్రాపర్లు లేకుండా.
- టెస్టులు/లింట్స్ నిర్వహించడం; మైగ్రేషన్ వల్ల సృష్టించిన చిన్న బ్రేకేజ్లను సరిదిద్దడం.
- చిన్న, రివ్యువబుల్ మార్పుల సెట్‌లను సిద్ధం చేసి, తుది సమ్మరీని దిఫ్‌లతో అందించడం (కమిట్ చెయ్యకండి).

---

## గార్డ్రైల్స్

- గిట్ వర్క్‌స్పేస్ లో ఉన్న ఫైళ్లను మాత్రమే మార్చండి. బయట ఎక్కడా వ్రాయకండి.
- వెనుకకు అనుకూలత కలిగించే షిమ్లను ఉంచకండి; కొత్త API ఆకృతికి కోడ్‌ను పూర్తి మైగ్రేట్ చేయండి.
- టుంబ్‌స్టోన్లు / ట్రాన్సిషన్ వ్యాఖ్యలు లేదా బ్యాకప్ ఫైళ్ళు మిగిల్చవద్దు.
- మొదటి స్ట్రీమింగ్ ఉపయోగం ఉంటే, స్ట్రీమింగ్ నిర్వాహణ ఉంచండి; లేకపోతే నాన్-స్ట్రీమింగ్ వాడండి.
- అప్రూవల్ మోడ్‌లో ఉంటే, కమాండ్లు లేదా నెట్‌వర్క్ కాల్స్ అమలు చేయడానికి ముందు అనుమతి తీసుకోండి.
- `git add`/`git commit`/`git push` నడపకండి; పనిచేసే ట్రీ ఎడిట్లను మాత్రమే ఉత్పత్తి చేయండి.

---

## దశ 0: Azure OpenAI క్లయింట్ మైగ్రేషన్ (ముందుగా ఉండవలసినది)

కోడ్‌బేస్ లో `AzureOpenAI` లేదా `AsyncAzureOpenAI` కన్స్ట్రక్టర్లు ఉపయోగిస్తుంటే, ముందు స్టాండర్డైన `OpenAI` / `AsyncOpenAI` కన్స్ట్రక్టర్లకు మార్చండి. Azure స్పెసిఫిక్ కన్స్ట్రక్టర్లు `openai>=1.108.1` లో డిప్రికేట్ అయిపోయాయి.

### ఎందుకు వి1 API పాథ్?

కొత్త `/openai/v1` ఎండ్‌పాయింట్ `AzureOpenAI()` కంటే సాదా `OpenAI()` క్లయింట్ ఉపయోగిస్తుంది, `api_version` అవసరం లేదు, OpenAI మరియు Azure OpenAI రెండింటిలోనూ ఒకే విధంగా పని చేస్తుంది. అదే క్లయింట్ కోడ్ భవిష్యత్తుకు తగును — వెర్షన్ నిర్వహణ అవసరం లేదు.

### ముఖ్యమైన మార్పులు

| మునుపటి | తరువాత |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | పూర్తిగా తీసివేయండి |

### శుభ్రపరిచే చెక్‌లిస్ట్

- క్లయింట్ కన్స్ట్రక్షన్ నుండి `api_version` ఆర్గ్యుమెంట్ తీసివేయండి.
- `.env`, యాప్ సెట్టింగ్స్ మరియు Bicep/ఇన్‌ఫ్రా ఫైళ్ళ నుంచి `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` ఎన్‌వైరన్మెంట్ వేరియబుల్స్ తీసివేయండి.
- `.env`, యాప్ సెట్టింగ్స్, Bicep/ఇన్‌ఫ్రా మరియు టెస్ట్ ఫిక్చర్లు లో `AZURE_OPENAI_CLIENT_ID` న Weiterlesen ఎవీళ్ళకు `AZURE_CLIENT_ID` గా పునర్నామకరణ చేయండి (స్టాండర్డ్ Azure ఐడెంటిటీ SDK సంప్రదాయం).
- `requirements.txt` లేదా `pyproject.toml` లో `openai>=1.108.1` ఉండాలని నిర్ధారించుకోండి.

### ఎన్‌వైరన్మెంట్ వేరియబుల్ మైగ్రేషన్

| పాత env var | చర్య | గమనికలు |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **తీసివేయండి** | వి1 ఎండ్‌పాయింట్‌తో `api_version` అవసరం లేదు |
| `AZURE_OPENAI_API_VERSION` | **తీసివేయండి** | అంతే పై విధంగా |
| `AZURE_OPENAI_CLIENT_ID` | **పునర్నామకరణ** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)` కోసం స్టాండర్డ్ Azure ఐడెంటిటీ SDK సంప్రదాయం |
| `AZURE_OPENAI_ENDPOINT` | **ఎలా ఉంచాలి** | ఇంకా `base_url` నిర్మాణానికి అవసరం |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **ఎలా ఉంచాలి** | `responses.create` లోగా `model` పారామీటర్‌గా ఉపయోగిస్తారు |
| `AZURE_OPENAI_API_KEY` | **ఎలా ఉంచాలి** | కీ ఆధారిత ధృవీకరణ కోసం `api_key` గా ఉపయోగిస్తారు |

క్లయింట్ సెటప్ కోడ్ ఉదాహరణలకి (సింక్, ఆసింక్, EntraID, API కీ, మల్టీ-టెనెంట్), [cheat-sheet.md](./references/cheat-sheet.md) చూడండి.

---

## దశ 1: లెగసీ కాల్ సైట్ల గుర్తింపు

మైగ్రేషన్ కావలసిన అన్ని కాల్ సైట్లను కనుగొనడానికి [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) స్క్రిప్ట్ నడపండి:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

లేదా ఈ సెర్చ్‌లను మాన్యువల్‌గా నడపండి — ప్రతి మ్యాచ్ ఒక మైగ్రేషన్ లక్ష్యం:

```bash
# పాత API కాల్స్ (మళ్ళీ రాయాలి)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# పాత Azure క్లయింట్ కన్‌స్ట్రక్టర్స్ (మార్చాలి)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# ప్రతిస్పందన ఆకారపు యాక్సెస్ నమూనాలు (నవీకరించాలి)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# పాత పదును లోపల టూల్ నిర్వచనాలు (పట్టుదల చేయాలి)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# పాత ఫార్మాట్ లో టూల్ ఫలితాలు (function_call_output కి మార్చాలి)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# పాత పారామితులు (తీయాలి లేదా పేరును మార్చాలి)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens అనగా పేరు మార్చండి
rg "['\"]seed['\"]"      # remove entirely

# పాత ఇన్విరాన్‌మెంట్ వేరియబుల్స్ (సाफు చేయాలి)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID కావాలి

# GitHub మోడల్స్ ఎండ్పాయింట్లు (తీయాలి — Responses API మద్దతు లేదు)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# ఫ్రేమ్‌వర్క్-స్థాయి పాత నమూనాలు (నవీకరించాలి)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient తో మార్చండి
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True అవసరం

# పరీక్షా వేదిక (నవీకరించాలి)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# కంటెంట్ ఫిల్టర్ లోపం బాడీ యాక్సెస్ (నవీకరించాలి — నిర్మాణం మారింది)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # పాత ఏకవచనం — ఇప్పుడు content_filter_results (బహువచనం) content_filters ఆరేలో ఉన్నది

# Chat Completions ఎండ్పాయింట్ కు రా HTTP కాల్స్ (URL నవీకరించాలి)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### హ్యూరిస్టిక్స్ (గుర్తించి పునర్రాచడం)

- **చాట్ కంప్లీషన్స్ క్లయింట్**: `client.chat.completions.create` → `client.responses.create(...)`.

- **అజ్యూర్ క్లయింట్ కన్స్ట్రక్టర్లు**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **టూల్స్**: ఫంక్షన్-కాల్ టూల్ నిర్వచనాలను నెస్టెడ్ ఫార్మాట్ (`{"type": "function", "function": {"name": ...}}`) నుండి ఫ్లాట్ రెస్పాన్సెస్ ఫార్మాట్ (`{"type": "function", "name": ...}`) గా మార్చండి; `tool_choice` ఉపయోగించండి; టూల్ ఫలితాలను `{"type": "function_call_output", "call_id": ..., "output": ...}` ఐటెమ్‌లుగా రిటర్న్ చేయండి (`{"role": "tool", ...}` కాదు).
- **టూల్ రౌండ్-ట్రిప్స్**: మోడల్ ఫంక్షన్ కాల్స్ ఇచ్చినప్పుడు, `response.output` ఐటెమ్‌లను సంభాషణకు జత చేయండి (మానవీయంగా `{"role": "assistant", "tool_calls": [...]}` డిక్ట్ కాకుండా), తరువాత ప్రతి ఫలితానికి `function_call_output` ఐటెమ్‌లు జత చేయండి.
- **ఫ్యూ-షాట్ టూల్ ఉదాహరణలు**: సంభాషణలో హార్డ్‌కోడ్ చేసిన టూల్ కాల్ ఉదాహరణలు ఉంటే, వాటిని `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` ఐటెమ్‌లుగా మార్చండి. IDs `fc_` తో మొదలవ్వాలి.
- **`pydantic_function_tool()`**: ఈ సహాయకుడు ఇంకా పాత నెస్టెడ్ ఫార్మాట్ ఉత్పత్తి చేస్తుంది మరియు `responses.create()` తో గుర్తింపుతో లేదు. దాన్ని మాన్యువల్ టూల్ నిర్వచనలు లేదా ఒక ఫ్లాటనింగ్ రాపర్‌తో స్థానంలో ఉంచండి.
- **మల్టి-టర్న్**: అనువర్తనంలో సంభాషణ చరిత్రను నిలుపుకోండి; పూర్వ టర్న్స్‌ను `input` ఐటెమ్‌లుగా అందించండి.
- **ఫార్మాటింగ్**: Chat యొక్క టాప్-లెవల్ `response_format` ను Responses లో `text.format` తో మార్చండి. సాంప్రదాయ ఆకృతి: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **కంటెంట్ ఐటెమ్‌లు**: Chat లో `content[].type: "text"` ను Responses లో `content[].type: "input_text"` తో స్వాప్ చేయండి యూజర్/సిస్టమ్ టర్న్స్ కోసం.
- **చిత్ర కంటెంట్ ఐటెమ్‌లు**: Chat `content[].type: "image_url"` ను Responses `content[].type: "input_image"` తో మార్చండి. `image_url` ఫీల్డ్ నెస్టెడ్ ఆబ్జెక్టు `{"url": "..."}` నుండి ఫ్లాట్ స్ట్రింగ్‌గా మారుతుంది. ముందు/తర్వాత ఉదాహరణల కోసం చీట్ షీట్ చూడండి.
- **తర్క పర్యాస**: **మూల కోడ్‌లో ఇప్పటికే `reasoning` ఉన్నప్పుడు మాత్రమే దాన్ని మైగ్రేట్ చేయండి**.
- **కంటెంట్ ఫిల్టర్ లోపం నిర్వహణ**: లోపం బాడీ నిర్మాణం మారింది. Chat Completions లో `error.body["innererror"]["content_filter_result"]` (ఏకపదం) ఉండేది; Responses API లో `error.body["content_filters"][0]["content_filter_results"]` (బహువచనం, ఒక అర్రేలో) ఉంటుంది. `innererror` యాక్సెస్ చేసే కోడ్ `KeyError` ఇస్తుంది. కొత్త మార్గాన్ని ఉపయోగించి తిరుగు రాయండి.
- **రా HTTP కాల్స్**: అనువర్తనం Azure OpenAI REST API ను నేరుగా `/openai/deployments/{name}/chat/completions?api-version=...` ద్వారా పిలిచితే, దాన్ని `/openai/v1/responses` కు మార్చండి. రిక్వెస్ట్ బాడీ మారుతుంది: `messages` → `input`, `max_output_tokens` మరియు `store: false` చేర్చండి, `api-version` క్వెరీ పరిమాణం తీసివేయండి. రిస్పాన్స్ బాడీ మారుతుంది: `choices[0].message.content` → `output[0].content[0].text` (గమనిక: `output_text` అనేది SDK సౌకర్య లక్షణం, రా REST JSON‌లో లేదు).

---

## దశ 2: మైగ్రేషన్ వర్తించండి

### మైగ్రేషన్ గమనికలు (Chat Completions → Responses)

- **మైగ్రేట్ ఎందుకు**: Responses టెక్స్ట్, టూల్స్, మరియు స్ట్రీమింగ్ కోసం సమైకృత API; Chat Completions పాతది. GPT-5 తో, Responses ఉత్తమ పనితత్వానికి అవసరం.
- **HTTP**: Azure ఎండ్‌పాయింట్ `/openai/deployments/{name}/chat/completions` నుండి `/openai/v1/responses` కి మారుతుంది.
- **ఫీల్డ్స్**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` మార్చలేదు.
- **ఫార్మాటింగ్**: `response_format` → `text.format` సరైన ఆబ్జెక్టుతో.
- **కంటెంట్ ఐటెమ్‌లు**: సిస్టమ్/యూజర్ టర్న్స్ కోసం Chat లో `content[].type: "text"` ను Responses `content[].type: "input_text"` తో మార్చండి.
- **చిత్ర కంటెంట్ ఐటెమ్‌లు**: Chat లో `content[].type: "image_url"` ను Responses లో `content[].type: "input_image"` తో మార్చండి. `image_url` ఫీల్డ్‌ను `{"image_url": {"url": "..."}}` నుండి `{"image_url": "..."}` (సాధారణ స్ట్రింగ్ — HTTPs URL లేదా `data:image/...;base64,...` డేటా URI) ఫ్లాటన్ చేయండి.

### పారామీటర్ మ్యాపింగ్ సూచిక

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (ఐటెమ్‌ల అర్రే) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (ఆబ్జెక్ట్) |
| `temperature` | `temperature` (మార్పు లేదు) |
| `stop` | `stop` (మార్పు లేదు) |
| `frequency_penalty` | `frequency_penalty` (మరచిన లేదు) |
| `presence_penalty` | `presence_penalty` (మార్పు లేదు) |
| `tools` / ఫంక్షన్-కాల్ | `tools` (మార్పు లేదు) |
| `seed` | **తీసివేయండి** (కొనసాగింపు లేదు) |
| `store` | `store` (ముఖ్యంగా `false` గా సెట్‌ చేయబడింది) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (ఫ్లాట్ స్ట్రింగ్) |

పూర్తిగా ముందు/తర్వాత కోడ్ ఉదాహరణల కోసం [cheat-sheet.md](./references/cheat-sheet.md) చూడండి.

పరీక్ష మౌలిక సదుపాయ మైగ్రేషన్ (మాాక్స్, స్నాప్‌షాట్లు, నిర్ధారణలు) కోసం [test-migration.md](./references/test-migration.md) చూడండి.

లోపాలు మరియు సమస్యలకు పరిష్కారాలు కోసం [troubleshooting.md](./references/troubleshooting.md) చూడండి.

---

## డేటా నిలుపుదల & స్థితి

- అన్ని Responses రిక్వెస్టులపై `store: false` సెట్ చేయండి.
- గత మెసేజ్ IDs లేదా సర్వర్ నిల్వ చేసిన కాంటెక్స్ట్‌పై ఆధారపడకండి; స్థితిని క్లయింట్ నిర్వహించడంలో ఉంచండి మరియు మెటాడేటాను తగ్గించండి.

---

## అంగీకార ప్రమాణాలు

### కోడ్-స్థాయి గేట్లు (ఇకన్నీ పాస్ కావాలి)

- [ ] మైగ్రేట్ చేసిన ఫైల్స్‌లో `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` కు జీరో మ్యాచ్‌లు.
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` కు జీరో మ్యాచ్‌లు — అన్ని కన్స్ట్రక్టర్లు v1 ఎండ్‌పాయింట్ తో `OpenAI`/`AsyncOpenAI` ఉపయోగించాలి.
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` కు జీరో మ్యాచ్‌లు — GitHub మోడల్స్ కోడ్ మార్గాలు తొలగించబడ్డాయన్నవి.
- [ ] `rg "OpenAIChatCompletionClient"` కు జీరో మ్యాచ్‌లు — MAF 1.0.0+ కోడ్ `OpenAIChatClient` (Responses API ఉపయోగిస్తుంది) ఉపయోగిస్తుంది. 1.0.0 క్రితం వర్షన్‌లో, `agent-framework-openai>=1.0.0` కు అప్‌గ్రేడ్ చేయండి.
- [ ] అన్ని `ChatOpenAI(...)` కాల్స్ లో `use_responses_api=True` ఉంటుంది.
- [ ] `rg "choices\[0\]"` కు జీరో మ్యాచ్‌లు — అన్ని రెస్పాన్స్ యాక్సెస్ `resp.output_text` లేదా Responses అవుట్‌పుట్ స్కీమా ఉపయోగిస్తుంది.
- [ ] టాప్-లెవల్‌లో `response_format` లేదు; అన్ని నిర్మిత అవుట్‌పుట్‌లు `text={"format": {...}}` ఉపయోగిస్తుంది.
- [ ] `openai>=1.108.1` మరియు `azure-identity` `requirements.txt` లేదా `pyproject.toml` లో; డిపెండెన్సీలు తిరిగి ఇన్‌స్టాల్ అయ్యాయి.
- [ ] ప్రతి `responses.create` కాల్‌లో `store=False` సెట్ చేయబడింది.
- [ ] క్లయింట్ కన్‌స్ట్రక్షన్‌లో `api_version` లేదు; `AZURE_OPENAI_API_VERSION` ఎన్‌వి ఫైల్స్ మరియు ఇన్‌ఫ్రా నుండి తొలగించబడింది.

### పరీక్ష మౌలిక సదుపాయ గేట్లు (ఇకన్నీ పాస్ కావాలి)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` కు జీరో మ్యాచ్‌లు.
- [ ] `rg "_azure_ad_token_provider" tests/` కు జీరో మ్యాచ్‌లు — నిర్ధారణలు `isinstance(client, AsyncOpenAI)` లేదా `base_url` ను పరిశీలించడానికి మార్చబడ్డాయి.
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` కు జీరో మ్యాచ్‌లు — Azure-ప్రత్యేక ఫిల్టర్ మాాక్స్ తొలగించబడ్డాయి.
- [ ] మాాక ఫిక్స్చర్‌లు `kwargs.get("input")` ఉపయోగిస్తాయి `kwargs.get("messages")` కాదు.
- [ ] స్నాప్‌షాట్ / గోల్డెన్ ఫైల్స్ Responses స్ట్రీమింగ్ ఆకారానికి అనుగుణంగా నవీకరించబడ్డాయి (`choices[0]`, `function_call`, `logprobs` లేవు).
- [ ] అన్ని పరీక్ష నవీకరణల తర్వాత `pytest` జీరో వైఫల్యాలతో మార్గదారితనం.

### ప్రవర్తనా గేట్లు (మనవచ్చు లేదా టెస్ట్ హార్నెస్ ద్వారా ధృవీకరించండి)

- [ ] **మూల పూర్తి చేయడం**: non-streaming `responses.create` ఖాళీ కాని `output_text` ఇవ్వాలి.
- [ ] **స్ట్రీమ్ సమానత్వం**: అసలు కోడ్ స్ట్రీమింగ్ ఉపయోగిస్తున్నట్లైతే, మైగ్రేట్ చేసిన కోడ్ స్ట్రీమ్ చేస్తుంది మరియు ఖాళీ కాని డెల్టాలతో `response.output_text.delta` ఈవెంట్లు ఇస్తుంది.
- [ ] **నిర్మిత అవుట్పుట్**: `text.format` తో `json_schema` ఉపయోగిస్తే, `json.loads(resp.output_text)` సక్సెస్ అవుతుంది మరియు స్కీమాతో సరిపోతుంది.
- [ ] **టూల్-కాల్ లూప్**: టూల్స్ ఉపయోగిస్తే, మోడల్ టూల్ కాల్స్ ఇస్తుంది, అనువర్తనం వాటిని అమలు చేస్తుంది, తదుపరి రిక్వెస్ట్ తుది `output_text` ఇస్తుంది (అనంత లూప్ లేదు).
- [ ] **అసింక్రో సమానత్వం**: `AsyncAzureOpenAI` ఉపయోగిస్తే, `AsyncOpenAI` సరిపోలిక `await` తో పని చేస్తుంది.
- [ ] **లోపాల రేటు**: ప్రీ-మైగ్రేషన్ బెంచ్‌మార్క్ తో పోలిస్తే కొత్త 400/401/404 లోపాలు లేవు.

### డెలివరిబుల్స్

- సారాంశంలో సవరణ చేసిన ఫైళ్లు, పాత/కొత్త లెగసీ కాల్ సైట్లు సంఖ్యలు, మరియు చరిష్టి దశలు ఉంటాయి.
- మార్పులు వర్కింగ్-ట్రీ ఎడిట్లు మాత్రమే (క‌మిటీలు కాదు).

---

## SDK వెర్షన్ అవసరాలు

| ప్యాకేజ్ | కనీస వెర్షన్ |
|---------|--------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | తాజా (EntraID ప్రామాణీకరణ కోసం) |

---

## సూచనలు

- [చీట్ షీట్ — అన్ని కోడ్ స్నిపెట్లతో](./references/cheat-sheet.md)
- [టెస్ట్ మైగ్రేషన్ — మాాక్స్, స్నాప్‌షాట్లు, నిర్ధారణలు](./references/test-migration.md)
- [సమస్య పరిష్కారం — లోపాలు, ప్రమాద పట్టిక, గోచారాలు](./references/troubleshooting.md)
- [detect_legacy.py — ఆటోమేటెడ్ స్కానర్](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [అజ్యూర్ ఓపన్ఏఐ స్టార్టర్ కిట్](https://aka.ms/openai/start)
- [అజ్యూర్ ఓపన్ఏఐ Responses API డాక్స్](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [అజ్యూర్ ఓపన్ఏఐ API వెర్షన్ లైఫ్సైకిల్](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [ఓపన్ఏఐ Responses API రిఫరెన్స్](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->