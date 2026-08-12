---
name: azure-openai-to-responses
license: MIT
---
# Azure OpenAI చాట్ కంఫ్లిషన్స్ నుండి Responses API కి Python యాప్స్ ను మార్పిడి చేయండి

> **అధికారిక మార్గదర్శనం — ఖచ్చితంగా అనుసరించండి**
>
> ఈ నైపుణ్యం Azure OpenAI చాట్ కంఫ్లిషన్స్ వాడే Python కోడ్‌బేస్‌లను
> ఏకీకృత Responses API కి మార్చుతుంది. ఈ సూచనలను ఖచ్చితంగా అనుసరించండి.
> పారామితి మ్యాపింగ్స్ ని ఊహించ వద్దు లేదా API ఆకారాలను ఆవిష్కరించ వద్దు.

---

## ట్రిగ్గర్స్

వాడుకరి క్రింది చర్యలు కోరినప్పుడు ఈ నైపుణ్యాన్ని ప్రారంభించండి:
- Azure OpenAI చాట్ కంఫ్లిషన్స్ నుండి Responses APIకి Python యాప్ మార్చడం
- Azure OpenAI కి వ్యతిరేకంగా Python OpenAI SDK వాడకాన్ని తాజాగా API ఆకారానికి అభివృద్ధి చేయడం
- Responses అవసరమయ్యే GPT-5 లేదా కొత్త మోడల్స్ కి Python కోడ్ సిద్ధం చేయడం
- `AzureOpenAI`/`AsyncAzureOpenAI` నుండి సాంప్రదాయ `OpenAI`/`AsyncOpenAI` క్లయింట్ కి v1 ఎండ్పాయింట్ తో మారడం
- `AzureOpenAI` నిర్మాణాలు లేదా `api_version` కి సంబంధించి డిప్రికేషన్ హెచ్చరికలను సవరణ చేయడం

---

## ⚠️ మోడల్ అనుకూలత — ముందుగా తనిఖీ చేయండి

> **మార్పిడి చేసేముందు, మీ Azure OpenAI డిప్లాయ్‌మెంట్ Responses APIని మద్దతు ఇస్తుందో లేదో ధృవీకరించండి.**

### 1. మీ డిప్లాయ్‌మెంట్‌ను స్మోక్స్-టెస్ట్ చేయండి (అత్యంత వేగవంతమైనది)

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

> **గమనిక**: Azure OpenAIలో `max_output_tokens`కి **కనీసం 16** ఉంటుంది. 16 కంటే తక్కువ విలువలు 400 ఎర్రర్ ఇస్తాయి. స్మోక్స్ టెస్ట్ కోసం 50+ వాడండి.

ఇది 404 ఇస్తే, డిప్లాయ్‌మెంట్ మోడల్ ఇంకా Responses మద్దతు ఇవ్వట్లేదు — క్రింది సూచనలను తనిఖీ చేయండి లేదా మద్దతు ఇచ్చే మోడల్‌తో మళ్లీ డిప్లాయ్ చేయండి.

### 2. మీ ప్రాంతంలో అందుబాటులో ఉన్న మోడల్స్ తనిఖీ చేయండి (భలే సూచన)

Responses API మద్దతుతో మీ నిర్దిష్ట ప్రాంతంలో ఏ మోడల్స్ అందుబాటులో ఉన్నాయో చూడటానికి బిల్ట్-ఇన్ మోడల్ అనుకూలత టూల్ ను రన్ చేయండి:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

ఇది Azure ARM లైవ్‌ను క్వెరీ చేసి అనుకూలత మేట్రిక్స్ చూపిస్తుంది — ఏ మోడల్స్ Responses, నిర్మిత అవుట్‌పుట్, టూల్స్ మద్దతు ఇస్తాయి. ఫలితాలను మాత్రం `--filter gpt-5.1,gpt-5.2` తో ఎలా తగ్గించుకునాలో లేదా స్క్రిప్టింగ్ కోసం `--json` ఉపయోగించండి.

### 3. పూర్తి మోడల్ మద్దతు సూచిక

- **లైవ్ క్వెరీ**: `python migrate.py models` (పైన చూడండి — ప్రాంత పరీక్షిత, ఎప్పుడూ నవీకరణలు)
- **దహించిన సవరించు**: [మోడల్ సారాంశ పట్టిక మరియు ప్రాంత అందుబాటు](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **త్వరిత ప్రారంభం & మార్గదర్శనం**: **https://aka.ms/openai/start**

### ⚠️ పాత మోడల్ పరిమితులు

> **హెచ్చరిక**: పాత మోడల్స్ (`gpt-4.1` కి ముందు) Responses API యొక్క అన్ని సവിശేషాలు పూర్తిగా మద్దతు ఇవ్వకపోవచ్చును.
>
> పాత మోడల్స్ కు తెలిసిన పరిమితులు:
> - **`reasoning` పారామితి**: చాలా non-reasoning మోడల్స్ మద్దతు ఇవ్వవు. అసలైన కోడ్‌లో ఉండకపోతే `reasoning`ని మార్చవద్దు.
> - **`seed` పారామితి**: Responses APIలో మద్దతు లేదు — అన్ని అభ్యర్థనల నుంచి తీసివేయండి.
> - **`text.format` ద్వారా నిర్మిత అవుట్‌పుట్**: పాత మోడల్స్ `strict: true` JSON స్కీమాస్‌ను విశ్వసనీయంగా అమలు చేయకపోవచ్చు.
> - **టూల్ నిర్వహణ**: GPT-5+ అంతర్గత reasoningలో టూల్ కాల్స్ నిర్వహణ చేస్తుంది. Responses పై పాత మోడల్స్ ఇంకా పనిచేస్తాయి కానీ దీర్ఘ అనుసంధానం ఉండదు.
> - **ఉష్ణోగ్రత పరిమితులు**: `gpt-5`కి మార్పిడి చేస్తే ఉష్ణోగ్రత వదిలివేయాలి లేదా `1` కు సెట్ చేయాలి. పాత మోడల్స్ కు ఇలాంటి పరిమితి లేదు.

### O-శ్రేణి reasoning మోడల్స్ (o1, o3-mini, o3, o4-mini)

O-శ్రేణి మోడల్స్ కి ప్రత్యేక పారామితి పరిమితులు ఉంటాయి. o-శ్రేణి మోడల్స్ ఉపయోగించే యాప్స్ మార్చేటప్పుడు:

- **`temperature`**: `1` (లేదా వదిలివేయాలి). O-శ్రేణి మోడల్స్ ఇతర విలువలను స్వీకరించవు.
- **`max_completion_tokens` → `max_output_tokens`**: Azure ప్రత్యేక `max_completion_tokens` వాడుతూ యాప్స్ `max_output_tokens` కి మారాలి. reasoning టోకెన్స్ పరిమితి మీద నీడ పడుతాయి కాబట్టి ఎక్కువ విలువ (4096+) సెట్ చేయండి.
- **`reasoning_effort`**: యాప్ `reasoning_effort` (తక్కువ/మధ్య/అధిక) వాడితే కొనసాగించండి — Responses API ఇది o-శ్రేణి మోడల్స్ కి మద్దతు ఇస్తుంది.
- **స్ట్రీమింగ్ ప్రవర్తన**: O-శ్రేణి మోడల్స్ reasoning పూర్తయ్యేవరకు అవుట్‌పుట్‌ను బఫర్ చేసి టెక్స్ట్ డెల్టా ఈవెంట్స్ విడుదల చేస్తాయి. స్ట్రీమింగ్ పనిచేస్తుంది, కానీ మొదటి `response.output_text.delta` GPT మోడల్స్ కంటే ఎక్కువ ఆలస్యం తో వచ్చుకోవచ్చు.
- **`top_p`**: O-శ్రేణి మీద మద్దతు లేదు — ఉన్నా తీసివేయండి.
- **టూల్ వాడకం**: O-శ్రేణి మోడల్స్ Responses API ద్వారా టూల్స్ ను GPT మోడల్స్ లాగా మద్దతు ఇస్తాయి, కానీ టూల్ కాల్ నిర్వహణ నాణ్యత మోడల్ పై ఆధారపడి ఉంటుంది.

**చర్య — ముందస్తు మోడల్ సలహా**: స్కాన్ దశలో యాప్ ఏ మోడల్ లక్ష్యంగా పెట్టుకొన్నదో (డిప్లాయ్‌ನామాలు, env వేరియబుల్స్, కాన్ఫిగ్) తనిఖీ చేయండి. మోడల్ `gpt-4.1` కంటే ముందు వుంటే (gpt-4.1+ కాదంటే) వాడుకరికి ముందస్తుగా చెప్పండి:
- ప్రస్తుతం ఉపయోగిస్తున్న మోడల్ మీద సాధారణ టెక్స్ట్, చాట్, స్ట్రీమింగ్ మరియు టూల్స్ కోసం మైగ్రేషన్ పనిచేస్తుంది.
- కొత్త మోడల్స్ (`gpt-5.1`, `gpt-5.2`) మెరుగైన టూల్ నిర్వహణ, నిర్మిత అవుట్‌పుట్ అమల, reasoning మరియు ప్రాంతాల మధ్య అందుబాటును అందిస్తాయి.
- వారు సిద్ధంగా ఉన్నప్పుడు డిప్లాయ్‌మెంట్ ని అభివృద్ధి చేయాలని పరిగణించాలి — ఇది మైగ్రేషన్ ని అడ్డుకోవడం కాదు.

మోడల్ వెర్షన్ ఆధారంగా మైగ్రేషన్ ని ఆపివేయొద్దు లేదా నిరాకరించొద్దు. సలహా సమాచారకరకమైంది.

### GitHub Models Responses APIని మద్దతు ఇవ్వలేదు

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) Responses APIని మద్దతు ఇవ్వవు.**

కోడ్‌బేస్‌లో GitHub Models కోడ్ పాథ్ ఉన్నట్లయితే (`base_url` `models.github.ai` లేదా `models.inference.ai.azure.com`కి సూచిస్తుంటే), మైగ్రేషన్ సమయంలో **మొత్తం తీసివేయండి**. Responses APIకి Azure OpenAI, OpenAI లేదా సారూప్య లోకల్ ఎండ్పాయింట్ (ఉదా: Ollama Responses మద్దతుతో) అవసరం.

స్కాన్ సమయంలో చర్య:
- GitHub Models కోడ్ పాథ్‌లను తీసివేం చేయడానికి గుర్తించండి.

---

## ఫ్రేమ్‌వర్క్ మైగ్రేషన్

చాల యాప్స్ OpenAI పై ఉన్న ఉన్నత స్థాయి ఫ్రేమ్‌వర్క్లు వాడతారు. ఇవి మార్చేటప్పుడు కేవలం OpenAI కాల్స్ కాదు, ఫ్రేమ్‌వర్క్ యొక్క స్వంత API మార్పులు తప్పనిసరి.

### Microsoft Agent Framework (MAF)

**మీలాంటి MAF వెర్షన్ ముందు తనిఖీ చేయండి** — మైగ్రేషన్ మీరు MAF 1.0.0+ లో ఉన్నారా లేదా పూర్వ 1.0.0 బీటా/ఆర్‌సి లో అన్నది ఆధారపడి ఉంటుంది.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **ఇప్పటికే Responses API వాడుతుంది** — మార్పులు అవసరం లేదు. కోడ్‌బేస్ లెగసీ `OpenAIChatCompletionClient` (`chat.completions.create` వాడుతుంది) వాడుతుంటే దానిని `OpenAIChatClient`తో మార్చండి.

| మునుపటి | తర్వాత |
|---------|--------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

మీ వెర్షన్ తనిఖీకి: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (బీటా/ఆర్‌సి విడుదలలు)

pre-1.0.0 MAFలో, `OpenAIChatClient` Chat Completions వాడింది. `agent-framework-openai>=1.0.0`కు నవీకరించండి, ఇక్కడ `OpenAIChatClient` డిఫాల్ట్ గా Responses API వాడుతుంది.

ఇంకొన్ని మార్పులు అవసరం లేదు — `Agent` మరియు టూల్ APIలు అలాగే ఉంటాయి.

### LangChain (`langchain-openai`)

`ChatOpenAI()`కు `use_responses_api=True` జత చేయండి. అదే సమయంలో ప్రతిస్పందన యాక్సెస్ `.content` నుండి `.text` కి మార్చండి.

| మునుపటి | తర్వాత |
|---------|--------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

పూర్తి మునుపటి/తర్వాత కోడ్ ఉదాహరణల కోసం [cheat-sheet.md](./references/cheat-sheet.md) చూడండి.

---

## ఫ్రంట్‌ఎండ్ మార్పిడి మార్గదర్శనం

> **Responses API సర్వర్-సైడ్ విషయం.** మీ Python బ్యాకెండ్ మార్చండి; ఫ్రంట్‌ఎండ్ HTTP ఒప్పందం మారకూడదు, మీ బ్యాకెండ్ తేలికపాటి పాస్-త్రూ అయితే మాత్రమే Responses అభ్యర్థన ఆకారాన్ని స్వీకరించడం పరిశీలించండి. ఫ్రంట్‌ఎండ్ నుండి క్లీంట్-సైడ్ కీతో నేరుగా OpenAIకి సంభాషిస్తే, మొదట ఆ కాల్స్ బ్యాకెండ్‌కు మార్చండి.

### `@microsoft/ai-chat-protocol` డిప్రికేషన్

`@microsoft/ai-chat-protocol` npm ప్యాకేజీ డిప్రికేట్ అయింది, దాన్ని [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream)తో మార్చాలి. ఫ్రంట్‌ఎండ్‌లో దాన్ని చూసినట్లయితే:

1. CDN స్క్రిప్ట్ ట్యాగ్ మార్చండి:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` యొక్క ఇనిస్టాన్షియేషన్ (`new ChatProtocol.AIChatProtocolClient("/chat")`) తీసివేయండి.
3. `client.getStreamedCompletion(messages)`ని ప్రత్యక్ష `fetch()` బ్యాకెండ్ స్ట్రీమింగ్ ఎండ్పాయింట్ కాల్‌తో మార్చండి.
4. `for await (const response of result)` ని `for await (const chunk of readNDJSONStream(response.body))` తో మార్చండి.
5. ప్రాపర్టీ యాక్సెస్‌ను `response.delta.content` / `response.error` నుండి `chunk.delta.content` / `chunk.error` కు సవరించండి.

---

## లక్ష్యాలు

- Azure OpenAIపై చాట్ కంఫ్లిషన్స్ లేదా లెగసీ కంఫ్లిషన్స్ వాడే అన్ని Python కాల్ సైట్లను లిస్ట్ చేయండి.
- Python కోడ్‌బేస్ కోసం మైగ్రేషన్ ప్రణాళిక మరియు సన్నాహాలను ప్రతిపాదించండి.
- Responses APIకి మార్పిడికి భద్రంగా, కనిష్ట మార్పులను వర్తించండి.
- కాలర్స్ Responses అవుట్‌పుట్ స్కీమాను వినియోగించేందుకు అప్డేట్ చేయండి; బ్యాక్‌కంపాటిబిలిటీ ర్యాపర్లు అవసరం లేదు.
- పరీక్షలు / లింట్స్ నడపండి; మైగ్రేషన్ వల్ల ఏర్పడిన చిన్న బగ్స్ ని సరి చేయండి.
- చిన్న, సమీక్షించదగిన చేంజ్ సెట్‌లను సిద్ధం చేసి చివరి సారాంశాన్ని డిఫ్స్ తో ఇవ్వండి (కమిట్ వద్దు).

---

## గార్డ్రెయిల్స్

- గిట్ వర్క్ స్పేస్ లోని ఫైళ్ళను మాత్రమే మార్చండి. బైటకు ఎక్కడైనా రాయకండి.
- వెనుకకు అనుకూలత కోసం షిమ్స్ పోషించకండి; కోడ్ ను కొత్త API ఆకారానికి మార్చండి.
- టంబ్‌స్టోన్/ట్రాన్సిషన్ కామెంట్లు లేదా బ్యాకప్ ఫైళ్ళను వదలవద్దు.
- ముందుగా స్ట్రీమింగ్ వాడితే ఆ semantics ని నిలుపుకోండి; లేకపోతే non-streaming వాడండి.
- అంగీకార మోడ్ లో ఉంటే కమాండ్లు లేదా నెట్‌వర్క్ కాల్స్ నీడ నడపేముందు ఆమోదం కోరండి.
- `git add`/`git commit`/`git push` నడపకండి; వర్కింగ్-ట్రీ ఎడిట్స్ మాత్రమే ఉత్పత్తి చేయండి.

---

## అడుగు 0: Azure OpenAI క్లయింట్ మైగ్రేషన్ (ముందస్తు అవసరం)

కోడ్‌బేస్ `AzureOpenAI` లేదా `AsyncAzureOpenAI` నిర్మాణాలు వాడుతుంటే, ముందుగా స్టాండర్డ్ `OpenAI` / `AsyncOpenAI` కాంట్రాక్టర్లు కి మార్చండి. Azure-ప్రత్యేక కాంట్రాక్టర్లు `openai>=1.108.1` లో డిప్రికేట్ అయ్యాయి.

### ఎందుకు v1 API మార్గం?

కొత్త `/openai/v1` ఎండ్పాయింట్ `AzureOpenAI()` కాకుండా సాదారణ `OpenAI()` క్లయింట్ ఉపయోగిస్తుంది, `api_version` పారామితి అవసరం లేదు, OpenAI మరియు Azure OpenAIలో ఒకే విధంగా పనిచేస్తుంది. ఒకే క్లయింట్ కోడ్ భవిష్యత్ సుస్థిరం — వెర్షన్ నిర్వహణ అవసరం లేదు.

### ముఖ్యమైన మార్పులు

| మునుపటి | తర్వాత |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | పూర్తిగా తీసివేయండి |

### శుభ్రపరిచే జాబితా

- క్లయింట్ నిర్మాణం నుంచి `api_version` ఆర్గ్యూమెంటును తీసివేయండి.
- `.env`, యాప్ సెట్టింగ్స్, Bicep/ఇన్‌ఫ్రా ఫైళ్ల నుండి `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` వాతావరణ వేరియబుల్స్ తొలగించండి.
- `.env`, యాప్ సెట్టింగ్స్, Bicep/ఇన్‌ఫ్రా, టెస్ట్ ఫిక్స్చర్లలో `AZURE_OPENAI_CLIENT_ID`ను `AZURE_CLIENT_ID`గా పేరు మార్చండి (స్టాండర్డ్ Azure Identity SDK సాంప్రదాయం).
- `requirements.txt` లేదా `pyproject.toml` లో `openai>=1.108.1` ని నిర్ధారించండి.

### వాతావరణ వేరియబుల్ మైగ్రేషన్

| పాత env var | చర్య | గమనికలు |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **తీసివేయండి** | v1 ఎండ్పాయింట్‌తో `api_version` అవసరం లేదు |
| `AZURE_OPENAI_API_VERSION` | **తీసివేయండి** | పై విధంగా |
| `AZURE_OPENAI_CLIENT_ID` | **పేరు మార్చండి** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)` కు స్టాండర్డ్ Azure Identity SDK సాంప్రదాయం |
| `AZURE_OPENAI_ENDPOINT` | **పొడుపు** | ఇంకా `base_url` నిర్మాణానికి అవసరం |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **పొడుపు** | `responses.create`లో `model` పారామితిగా ఉపయోగం |
| `AZURE_OPENAI_API_KEY` | **పొడుపు** | కీ ఆధారిత ధృవీకరణ కోసం `api_key`గా ఉపయోగం |

క్లయింట్ సెటప్ కోడ్ ఉదాహరణల కోసం (సింక్, అసింక్, EntraID, API కీ, బహుళ-టెనెంట్), [cheat-sheet.md](./references/cheat-sheet.md) చూడండి.

---

## అడుగు 1: లెగసీ కాల్ సైట్లను గుర్తించండి

మార్చాల్సిన అన్ని కాల్ సైట్లను కనుగొనడానికి [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) స్క్రిప్ట్ నడిపించండి:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

లేకపోతే ఈ సెర్చ్‌లు మాన వాయిగా నిర్వహించండి — ప్రతి మ్యాచ్ మైగ్రేషన్ టార్గెట్.

```bash
# వారసత్వ API కాల్స్ (మళ్ళీ రాయాలి)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# డిప్రికేటెడ్ అజ్యూర్ క్లయింట్ కనిస్ట్రక్టర్స్ (మార్చాలి)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# స్పందన ఆకృతి యాక్సెస్ నమూనాలు (అప్డేట్ చేయాలి)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# పాత నెస్టెడ్ ఫార్మాట్‌లో టూల్ నిర్వచనలు (ఫ్లాటెన్ చేయాలి)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# పాత ఫార్మాట్‌లో టూల్ ఫలితాలు (function_call_output కు మార్చాలి)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# డిప్రికేటెడ్ పారామీటర్లు (తొలగించాలి లేదా పేరును మార్పు చేయాలి)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens అనే పేరుతో మార్చండి
rg "['\"]seed['\"]"      # remove entirely

# డిప్రికేటెడ్ env వేరియబుల్స్ (శుభ్రపరచండి)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID కావాలి

# GitHub మోడల్స్ ఎండ్పాయింట్లు (తొలగించాలి — Responses API మద్దతు లేదు)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# ఫ్రేమ్‌వర్క్ స్థాయి వారసత్వ నమూనాలు (అప్డేట్ చేయాలి)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: OpenAIChatClient తో మార్చండి
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True కావాలి

# టెస్ట్ ఇన్‌ఫ్రాస్ట్రక్చర్ (అప్డేట్ చేయాలి)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# కంటెంట్ ఫిల్టర్ లోపం బాడీ యాక్సెస్ (అప్డేట్ చేయాలి — నిర్మాణం మారింది)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # పాత ఏకవచనం — ఇప్పుడు content_filters అర్రేలో content_filter_results (బహువచనం)

# Chat Completions ఎండ్పాయింట్‌కి రా HTTP కాల్స్ (URL అప్డేట్ చేయాలి)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### heuristics (గుర్తించి, పునఃరాయింపు చేయండి)

- **చాట్ కంఫ్లిషన్స్ క్లయింట్**: `client.chat.completions.create` → `client.responses.create(...)`.

- **ఆజ్యూర్ క్లయింట్ కన్స్ట్రక్టర్లు**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **సాధనాలు**: ఫంక్షన్-కాలింగ్ టూల్ నిర్వచనాలను నెస్ట్格式్ నుండి (`{"type": "function", "function": {"name": ...}}`) ఫ్లాట్ Responses ఫార్మాట్ కు మార్చండి (`{"type": "function", "name": ...}`); `tool_choice` ఉపయోగించండి; టూల్ ఫలితాలను `{"type": "function_call_output", "call_id": ..., "output": ...}` ఐటెమ్స్ (కాదు `{"role": "tool", ...}`) గా రిటర్న్ చేయండి.
- **టూల్ రౌండ్-ట్రిప్స్**: మోడల్ ఫంక్షన్ కాల్స్ ఇచ్చినపుడు, `response.output` ఐటెమ్స్ ను సంభాషణకు జోడించండి (మాన్యువల్ `{"role": "assistant", "tool_calls": [...]}` డిక్ట్ కాదు), తరువాత ప్రతి ఫలితానికీ `function_call_output` ఐటెమ్స్ ను జోడించండి.
- **ఫ్యూ-షాట్ టూల్ ఉదాహరణలు**: సంభాషణలో హార్డ్‌కోడ్ చేసిన టూల్ కాల్ ఉదాహరణలు ఉంటే, వాటిని `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` ఐటెమ్స్ గా మార్పులు చేయండి. IDs తప్పనిసరిగా `fc_` తో మొదలవ్వాలి.
- **`pydantic_function_tool()`**: ఈ హెల్పర్ ఇంకా పాత నెస్ట్格式్ ను ఉత్పత్తి చేస్తుంది మరియు `responses.create()` కు **అనుకూలం కాదు**. దానిని మాన్యువల్ టూల్ నిర్వచనలతో లేదా ఫ్లాటెనింగ్ ర్యాపర్ తో మార్చండి.
- **మల్టీ-టర్న్**: అప్లో సంభాషణ చరිතాన్ని ఉంచండి; గత టర్న్లను `input` ఐటెమ్స్ ద్వారా పంపండి.
- **ఫార్మాటింగ్**: చాట్లో ఉన్న టాప్-లెవెల్ `response_format` ను Responses లో `text.format` తో మార్చండి. సాధారణ ఆకారము: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **కంటెంట్ ఐటెమ్స్**: చాట్ `content[].type: "text"` ను Responses లో యూజర్/సిస్టమ్ టర్న్ల కోసం `content[].type: "input_text"` గా మార్చండి.
- **చిత్రం కంటెంట్ ఐటెమ్స్**: చాట్ `content[].type: "image_url"` ను Responses లో `content[].type: "input_image"` గా మార్చండి. `image_url` ఫీల్డ్ గల నెస్ట్ అబ్జెక్ట్ `{"url": "..."}` ను ఫ్లాట్ స్ట్రింగ్ గా మార్చండి. ముందు / తరువాత ఉదాహరణలు కోసం చిట్ షీట్ చూడండి.
- **ఆలోచనా శ్రమ**: **అసలు కోడులో `reasoning` ఇప్పటికే ఉంటేనే మాత్రమే మైగ్రేట్ చేయండి**.
- **కంటెంట్ ఫిల్టర్ ఎర్రర్ హ్యాండ్లింగ్**: లోపపు బాడీ నిర్మాణం మార్చబడింది. చాట్ కంప్లీషన్స్ `error.body["innererror"]["content_filter_result"]` (ఏకవచనం) ఉపయోగించగా; Responses API `error.body["content_filters"][0]["content_filter_results"]` (బహువచనం, ఒక అర్రే లో) ఉపయోగిస్తుంది. `innererror` ను యాక్సెస్ చేసే కోడ్ `KeyError` ని తేపుతుంది. కొత్త పాథ్ ఉపయోగించి రచయిత చేయండి.
- **అనరూప రా HTTP కాల్స్**: అప్లికేషన్ Azure OpenAI REST API ని నేరుగా (/openai/deployments/{name}/chat/completions?api-version=...) ద్వారా పిలిచితే, `/openai/v1/responses` కి రీసెటప్ చేయండి. రిక్వెస్ట్ బాడీ మార్పులు: `messages` → `input`, `max_output_tokens` మరియు `store: false` జతచేయండి, `api-version` క్వెరీ ప్యారామీ తీసేయండి. రిస్పాన్స్ బాడీ మార్పులు: `choices[0].message.content` → `output[0].content[0].text` (గమనిక: `output_text` అనేది SDK సౌకర్యం, రా REST JSON లో లేదు).

---

## దశ 2: మైగ్రేషన్ అప్లై చేయండి

### మైగ్రేషన్ గమనికలు (చాట్ కంప్లీషన్స్ → Responses)

- **ఎందుకు మైగ్రేట్ చేయాలి**: Responses టెక్స్ట్, టూల్స్, మరియు స్ట్రీమింగ్ కి యూనిఫైడ్ API; చాట్ కంప్లీషన్స్ పాతది. GPT-5 తో Responses మంచి పనితీరు కోసం అవసరము.
- **HTTP**: ఆజ్యూర్ ఎండ్‌పాయింట్ `/openai/deployments/{name}/chat/completions` నుండి `/openai/v1/responses` కి మారింది.
- **ఫీల్డ్స్**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` ఒకటే.
- **ఫార్మాటింగ్**: `response_format` → సరైన ఆబ్జెక్టుతో `text.format`.
- **కంటెంట్ ఐటెమ్స్**: సిస్టమ్/యూజర్ టర్న్ల కోసం చాట్ `content[].type: "text"` ని Responses లో `content[].type: "input_text"`కి మార్చండి.
- **చిత్రం కంటెంట్ ఐటెమ్స్**: చాట్ `content[].type: "image_url"` ను Responses లో `content[].type: "input_image"`గా మార్చండి. `image_url` ఫీల్డ్-ను `{"image_url": {"url": "..."}}` నుండి `{"image_url": "..."}` (ప్లెయిన్ స్ట్రింగ్ — HTTPS URL లేకపోతే `data:image/...;base64,...` డేటా URI)గా ఫ్లాటెన్ చేయండి.

### పారామీటరు మ్యాపింగ్ సూచిక

| చాట్ కంప్లీషన్స్ | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (ఐటమ్‌ల అర్రే) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (ఆబ్జెక్ట్) |
| `temperature` | `temperature` (అనుకూలంగా) |
| `stop` | `stop` (అనుకూలంగా) |
| `frequency_penalty` | `frequency_penalty` (అనుకూలంగా) |
| `presence_penalty` | `presence_penalty` (అనుకూలంగా) |
| `tools` / function-calling | `tools` (అన్‌ఛేంజ్) |
| `seed` | **తీసేయండి** (మద్దతు లేదు) |
| `store` | `store` (పరిమితి: `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (ఫ్లాట్ స్ట్రింగ్) |

పూర్తి ముందు/తరువాత కోడ్ ఉదాహరణల కోసం, [cheat-sheet.md](./references/cheat-sheet.md) చూడండి.

పరీక్షా మౌలిక సదుపాయ మైగ్రేషన్ (మోక్స్, స్నాప్షాట్స్, ధృవీకరణలు) కోసం, [test-migration.md](./references/test-migration.md) చూడండి.

లోపాలు మరియు సమస్యలు పరిష్కారానికి, [troubleshooting.md](./references/troubleshooting.md) చూడండి.

---

## డేటా రిటెన్షన్ & స్టేట్

- అన్ని Responses అభ్యర్థనలపై `store: false` సెట్ చేయండి.
- గత సందేశ IDs లేదా సర్వర్-సంగ్రహిత సందర్భంపై ఆధారపడకండి; స్టేట్ క్లయింట్-నియంత్రణలో ఉంచండి మరియు మెటాడేటా తగ్గించండి.

---

## ఆమోదం ప్రమాణాలు

### కోడ్-స్థాయి గేట్లు (అన్నీ పూర్తి కావాలి)

- [ ] మార్చిన ఫైళ్లలో `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` కోసం ఏ మ్యాచ్‌లు ఉండకూడదు.
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` కోసం ఏ మ్యాచ్‌లు ఉండకూడదు — అన్ని కన్స్ట్రక్టర్లు `OpenAI`/`AsyncOpenAI` v1 ఎండ్‌పాయింట్ తో ఉపయోగించాలి.
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` కోసం ఏ మ్యాచ్‌లు ఉండకూడదు — GitHub మోడల్స్ కోడ్ మార్గాలు తీసేయబడ్డాయి.
- [ ] `rg "OpenAIChatCompletionClient"` కోసం ఏ మ్యాచ్‌లు ఉండకూడదు — MAF 1.0.0+ కోడ్ `OpenAIChatClient` (Responses API వాడుతుంది) ఉపయోగిస్తుంది. 1.0.0 ముందు ఉండితే `agent-framework-openai>=1.0.0` కు నవీకరించండి.
- [ ] అన్ని `ChatOpenAI(...)` పిలుపుల్లో `use_responses_api=True` ఉంటుంది.
- [ ] `rg "choices\[0\]"` కోసం ఏ మ్యాచ్‌లు ఉండకూడదు — అన్ని ప్రతిస్పందన యాక్సెస్ `resp.output_text` లేదా Responses అవుట్పుట్ స్కీమాను ఉపయోగిస్తుంది.
- [ ] టాప్-లెవెల్‌లో `response_format` ఉండకూడదు; అన్ని సాంరాచనాత్మక అవుట్పుట్లకు `text={"format": {...}}` ఉపయోగించాలి.
- [ ] `requirements.txt` లేదా `pyproject.toml` లో `openai>=1.108.1` మరియు `azure-identity` ఉండాలి; డిపెండెన్సిస్ మళ్ళీ ఇన్స్టాల్ చేయబడాలి.
- [ ] ప్రతి `responses.create` పిలుపులో `store=False` సెట్ చేయాలి.
- [ ] క్లయింట్ కన్స్ట్రక్షన్‌లో `api_version` ఉండరాదు; `AZURE_OPENAI_API_VERSION` ను ఎన్వ్ ఫైల్స్ మరియు ఇన్‌ఫ్రా నుండి తీసేయాలి.

### టెస్ట్ మౌలిక సదుపాయ గేట్లు (అన్నీ పూర్తి కావాలి)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` కోసం ఏ మ్యాచ్‌లు ఉండకూడదు.
- [ ] `rg "_azure_ad_token_provider" tests/` కోసం ఏ మ్యాచ్‌లు ఉండకూడదు — అసर्शन‌లు `isinstance(client, AsyncOpenAI)` లేదా `base_url` ను పరీక్షించాలి.
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` కోసం ఏ మ్యాచ్‌లు ఉండకూడదు — ఆజ్యూర్ ప్రత్యేక ఫిల్టర్ మోక్స్ తీసేయబడ్డాయి.
- [ ] మాక్ ఫిక్చర్స్ `kwargs.get("input")` ఉపయోగిస్తాయి, `kwargs.get("messages")` కాకుండా.
- [ ] స్నాప్షాట్ / గోల్డెన్ ఫైళ్లను Responses స్ట్రీమింగ్ ఆకారానికి అనుగుణంగా నవీకరించండి (`choices[0]`, `function_call`, `logprobs` లేవు).
- [ ] అన్ని టెస్ట్ నవీకరణల తర్వాత `pytest` లో ఎలాంటి వైఫల్యాలు ఉండకూడదు.

### ప్రవర్తనా గేట్లు (మాన్యువల్ లేదా టెస్ట్ హార్నెస్ ద్వారా ధృవీకరించాలి)

- [ ] **బేసిక్ కంప్లీషన్**: నాన్-స్ట్రీమింగ్ `responses.create` ఖాళీ కాని `output_text` ను రిటర్న్ చేయాలి.
- [ ] **స్ట్రీమ్ సమానత్వం**: అసలు కోడులో స్ట్రీమింగ్ వాడితే, మార్చిన కోడ్ కూడా స్ట్రీమ్ చేసి, ఖాళీ కాని డెల్టాలతో `response.output_text.delta` ఈవెంట్లు ఇస్తుంది.
- [ ] **స్ట్రక్చర్డ్ అవుట్పుట్**: `text.format` తో `json_schema` ఉపయోగిస్తే, `json.loads(resp.output_text)` విజయవంతం అవుతుంది మరియు స్కీమాకు సరిపోతుంది.
- [ ] **టూల్-కాల్స్ లూపు**: టూల్స్ ఉపయోగించినప్పుడు, మోడల్ టూల్ కాల్స్ చేస్తుంది, యాప్ అవి అమలు చేస్తుంది, తదుపరి అభ్యర్థన తుది `output_text` ను ఇస్తుంది (అనంత లూప్ కాదు).
- [ ] **అసింక్ సమానత్వం**: `AsyncAzureOpenAI` వాడితే, `AsyncOpenAI` సమానం `await` తో పనిచేస్తుంది.
- [ ] **లోపాల రేటు**: మైగ్రేషన్ ముందు స్థాయి తో పోల్చితే కొత్త 400/401/404 లోపాలు ఉండకూడదు.

### డెలివరబుల్స్

- సారాంశంలో మార్చిన ఫైళ్ళు, పాత/కొత్త లిగసీ కాల్ సైట్లు గణాంకాలు, తదుపరి చర్యలు ఉంటాయి.
- మార్పులు వర్కింగ్-ట్రీ ఎడిట్స్ మాత్రమే (కామిట్ లేవు).

---

## SDK సంస్కరణ అవసరాలు

| ప్యాకేజ్ | కనిష్ఠ సంస్కరణ |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | తాజా (ఎంట్రాID ఆథ్ కోసం) |

---

## సూచనలు

- [చిట్ షీట్ — అన్ని కోడ్ స్నిపెట్లు](./references/cheat-sheet.md)
- [టెస్ట్ మైగ్రేషన్ — మోక్స్, స్నాప్షాట్లు, ధృవీకరణలు](./references/test-migration.md)
- [ట్రబుల్షూటింగ్ — లోపాలు, ప్రమాద పట్టిక, గోచర్లు](./references/troubleshooting.md)
- [detect_legacy.py — ఆటోమేటెడ్ స్కానర్](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [ఆజ్యూర్ OpenAI ప్రారంభ కిట్](https://aka.ms/openai/start)
- [ఆజ్యూర్ OpenAI Responses API డాక్స్](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [ఆజ్యూర్ OpenAI API వెర్షన్ జీవన చక్రం](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API సూచీ](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->