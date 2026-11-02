---
name: azure-openai-to-responses
license: MIT
---
# Hamisha Programu za Python kutoka Azure OpenAI Chat Completions kwenda Responses API

> **MWONGOZO WA KIHALIFU — FUATA KIDHIDI**
>
> Ujuzi huu unahamisha misimbo ya Python inayotumia Azure OpenAI Chat Completions
> kwenda Responses API iliyounganishwa. Fuata maagizo haya kwa usahihi.
> Usijaribu kubuni ramani za vigezo au kufikiria maumbo ya API.

---

## Vichocheo

Amsha ujuzi huu wakati mtumiaji anataka:
- Kuhamisha programu ya Python kutoka Azure OpenAI Chat Completions kwenda Responses API
- Kuboresha matumizi ya SDK ya Python OpenAI kwa muundo mpya wa API dhidi ya Azure OpenAI
- Kuandaa msimbo wa Python kwa modeli za GPT-5 au mpya zaidi zinazotumia Responses kwenye Azure
- Kubadilisha kutoka `AzureOpenAI`/`AsyncAzureOpenAI` kwenda mteja wa kawaida `OpenAI`/`AsyncOpenAI` kwa kiambatisho cha v1
- Kutatua onyo za kuachwa matumizi zinazohusiana na wajenzi wa `AzureOpenAI` au `api_version`

---

## ⚠️ Uendeshaji wa Modeli — KAGUA KWANZA

> **Kabla ya kuhamisha, thibitisha kuwa usaandaji wako wa Azure OpenAI unaunga mkono Responses API.**

### 1. Fanya mtihani wa haraka wa usaandaji (haraka zaidi)

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

> **Kumbuka**: `max_output_tokens` ina **chini ya angalau 16** kwenye Azure OpenAI. Thamani chini ya 16 hurudisha kosa la 400. Tumia 50+ kwa majaribio ya haraka.

Ikiwa hii itarudisha 404, modeli ya usaandaji haijaunga mkono Responses bado — angalia kumbukumbu hapa chini au fanya upya usaandaji ukiwa na modeli inayoungwa mkono.

### 2. Angalia modeli zinapatikana katika eneo lako (inashauriwa)

Endesha chombo cha ukaguzi wa muafaka wa modeli kilicho ndani kuona ni zipi zinazounga mkono Responses API katika eneo lako maalum:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Hii inauliza Azure ARM moja kwa moja na inaonyesha meza ya muafaka — ni modeli gani zinaunga mkono Responses, matokeo ya muundo, zana, nk. Tumia `--filter gpt-5.1,gpt-5.2` kupunguza matokeo au `--json` kwa usanifu wa skripti.

### 3. Kumbukumbu kamili ya msaada wa modeli

- **Utakaso wa moja kwa moja**: `python migrate.py models` (tazama hapo juu — maalum kwa eneo, kila wakati updated)
- **Vinjari upatikanaji**: [Jedwali la muhtasari wa modeli na upatikanaji wa eneo](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Anza haraka & mwongozo**: **https://aka.ms/openai/start**

### ⚠️ Vikwazo vya modeli za zamani

> **ONYO**: Modeli za zamani (zisizozidi `gpt-4.1`) huenda zisiwe na vipengele vyote vya Responses API kikamilifu.
>
> Vikwazo vinavyojulikana kwa modeli za zamani:
> - **Kigezo cha `reasoning`**: Hakinaungwa mkono kwa modeli nyingi zisizo za reasoning. Hamisha `reasoning` tu ikiwa tayari lilikuwepo katika msimbo wa awali.
> - **Kigezo cha `seed`**: Hakinaungwa mkono kabisa katika Responses API — ondoa kutoka kwa maombi yote.
> - **Matokeo ya muundo kupitia `text.format`**: Modeli za zamani huenda zisiwe na utekelezaji thabiti wa miundo ya JSON yenye `strict: true`.
> - **Uratibu wa zana**: GPT-5+ hufuata mwitikio wa zana kama sehemu ya reasoning ya ndani. Modeli za zamani kwenye Responses bado zinafanya kazi lakini hazina ujumuishaji huu mzito.
> - **Vizuizi vya joto**: Wakati wa kuhamisha kwa `gpt-5`, joto lazima liache au liwe `1`. Modeli za zamani hazina vizuizi hivi.

### Modeli za mfululizo wa O (o1, o3-mini, o3, o4-mini)

Modeli za mfululizo wa O zina vikwazo maalum vya vigezo. Wakati wa kuhamisha programu zinazolenga modeli za mfululizo wa O:

- **`temperature`**: Lazima iwe `1` (au iachwe). Modeli za mfululizo wa O hazikubali thamani nyingine.
- **`max_completion_tokens` → `max_output_tokens`**: Programu zinazotumia `max_completion_tokens` maalum ya Azure lazima zibadilishe kwenda `max_output_tokens`. Weka thamani kubwa (4096+) kwa sababu tokens za reasoning zinaathiri kikomo.
- **`reasoning_effort`**: Ikiwa programu inatumia `reasoning_effort` (chini/kati/juu), endelea kuitumia — Responses API inaunga mkono kigezo hiki kwa modeli za mfululizo wa O.
- **Tabia ya mtiririko**: Modeli za mfululizo wa O zinaweza kuhifadhi matokeo hadi reasoning itakapokamilika kabla ya kutoa matukio ya matoleo ya maandishi. Mkondo bado unaendelea, lakini `response.output_text.delta` ya kwanza inaweza kuchelewa zaidi kuliko kwa modeli za GPT.
- **`top_p`**: Haikuungwa mkono kwa mfululizo wa O — ondoa kama ipo.
- **Matumizi ya zana**: Modeli za mfululizo wa O zinaunga mkono zana kupitia Responses API kama za GPT, lakini ubora wa uratibu wa simu za zana hutofautiana kwa modeli.

**Hatua — ushauri wa proactive wa modeli**: Wakati wa awamu ya ukaguzi, angalia ni modeli gani programu inalenga (majina ya usaandaji, mabadiliko ya mazingira, usanidi). Ikiwa modeli ni kabla ya `gpt-4.1` (si gpt-4.1+), mwambie mtumiaji kwa hiari:
- Uhamisho utafanya kazi kwa maandishi ya msingi, mazungumzo, mtiririko, na zana kwenye modeli yao ya sasa.
- Modeli mpya (`gpt-5.1`, `gpt-5.2`) zinatoa uratibu bora wa zana, utekelezaji wa matokeo ya muundo, reasoning, na upatikanaji wa eneo jipya.
- Wanapaswa kufikiria kuboresha usaandaji wao wakati wako tayari — si vizuizi kwa uhamishaji.

Usizuie au ukatae kuhamisha kwa sababu ya toleo la modeli. Ushauri ni taarifa tu.

### GitHub Models HAIUNGA MKONO Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) haiungi mkono Responses API.**

Ikiwa msimbo una njia ya msimbo wa GitHub Models (tazama `base_url` inayoelekeza `models.github.ai` au `models.inference.ai.azure.com`), **iondoe kabisa** wakati wa uhamishaji. Responses API inahitaji Azure OpenAI, OpenAI, au kiambatisho cha ndani kinachoweza kufanana (mfano, Ollama yenye msaada wa Responses).

Hatua wakati wa ukaguzi:
- Bainisha njia zozote za msimbo za GitHub Models kwa kuondolewa.

---

## Uhamishaji wa Muktadha

Programu nyingi hutumia mifumo ya kiwango cha juu juu ya OpenAI. Wakati wa kuhamisha hizi, mabadiliko ya API ya mfumo ni tofauti — si tu wito wa msingi wa OpenAI.

### Mfumo wa Wakala wa Microsoft (MAF)

**Angalia toleo lako la MAF kwanza** — uhamishaji unategemea kama uko kwenye MAF 1.0.0+ au beta/rc kabla ya 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **tunahamisha API ya Responses** — hakuna uhamisho unaohitajika. Ikiwa msimbo unatumia `OpenAIChatCompletionClient` ya zamani (inayotumia `chat.completions.create`), badilisha na `OpenAIChatClient`.

| Kabla | Baada |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Kuangalia toleo lako: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"` 

#### MAF kabla ya 1.0.0 (toleo la beta/rc)

Katika MAF kabla ya 1.0.0, `OpenAIChatClient` lilitumia Chat Completions. Boresha kwenda `agent-framework-openai>=1.0.0` ambapo `OpenAIChatClient` hutumia Responses API kama chaguo-msingi.

Hakuna mabadiliko mengine yanayohitajika — API za `Agent` na zana zinaendelea kuwa ile ile.

### LangChain (`langchain-openai`)

Ongeza `use_responses_api=True` kwa `ChatOpenAI()`. Pia update upatikanaji wa jibu kutoka `.content` kwenda `.text`.

| Kabla | Baada |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Kwa mifano kamili ya msimbo kabla/baada, angalia [cheat-sheet.md](./references/cheat-sheet.md).

---

## Mwongozo wa Uhamishaji wa Mbele ya Programu

> **Responses API ni dhima upande wa seva.** Hamisha sehemu yako ya nyuma ya Python; mkataba wa HTTP wa mbele haupaswi kubadilika isipokuwa sehemu ya nyuma ni njia nyembamba tu — katika hali hiyo, fikiria kutumia muundo wa ombi la Responses kuondoa tabaka la tafsiri. Ikiwa mbele ya programu inaita OpenAI moja kwa moja na funguo za upande wa mteja, hamisha miito hiyo kwanza sehemu ya nyuma.

### Kuachwa kwa `@microsoft/ai-chat-protocol`

Kifurushi cha npm `@microsoft/ai-chat-protocol` kimeachwa na kinapaswa kubadilishwa na [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Ikiwa unakutana nacho mbele ya programu:

1. Badilisha tagi ya script ya CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Ondoa kuanzishwa kwa `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Badilisha `client.getStreamedCompletion(messages)` kwa wito wa moja kwa moja wa `fetch()` kwa kiambatisho cha mtiririko cha sehemu ya nyuma.
4. Badilisha `for await (const response of result)` kwa `for await (const chunk of readNDJSONStream(response.body))`.
5. Sasisha upatikanaji wa mali kutoka `response.delta.content` / `response.error` kwenda `chunk.delta.content` / `chunk.error`.

---

## Malengo

- Tazama maeneo yote ya mwito ya Python yanayotumia Chat Completions au Completions za zamani dhidi ya Azure OpenAI.
- Pendekeza mpango wa uhamishaji na mfuatano kwa msimbo wa Python.
- Tumia mabadiliko salama, madogo kuhamia Responses API.
- Sasisha wito ili kutumia muundo wa matokeo ya Responses; usiweke vifuniko vya kurudisha nyuma.
- Endesha vipimo/lints; rekebisha makosa madogo yaliyosababishwa na uhamishaji.
- Andaa sets ndogo za mabadiliko za kupitia na toa muhtasari wa mwisho na tofauti (usifanye kuwekea).

---

## Mipaka ya Usalama

- Badilisha tu faili zilizo ndani ya ghala la git. Usiliandike nje.
- Usidumishe vifuniko vya urudisho nyuma; hamisha msimbo kwenda muundo mpya wa API.
- Usiachie maoni ya hatua za mpito au faili zaharibifu.
- Hifadhi semantiki za mtiririko ikiwa zilikuwa zikitumika awali; vinginevyo tumia isiyo na mtiririko.
- Omba idhini kabla ya kuendesha amri au miito ya mtandao ikiwa uko katika hali ya idhini.
- Usifanye `git add`/`git commit`/`git push`; tengeneza mabadiliko ya mti wa kazi tu.

---

## Hatua 0: Uhamishaji wa Mteja wa Azure OpenAI (Sharti la Awali)

Ikiwa msimbo unatumia wajenzi wa `AzureOpenAI` au `AsyncAzureOpenAI`, hamisha kwanza kwenda wajenzi wa kawaida wa `OpenAI` / `AsyncOpenAI`. Wajenzi maalum wa Azure wameachwa matumizi katika `openai>=1.108.1`.

### Kwa nini njia ya API ya v1?

Kiambatisho kipya cha `/openai/v1` kinatumia mteja wa kawaida `OpenAI()` badala ya `AzureOpenAI()`, hakihitaji kigezo cha `api_version`, na hufanya kazi sawa kwenye OpenAI na Azure OpenAI. Msimbo huo wa mteja ni salama kwa siku za usoni — hakuna udhibiti wa matoleo unaohitajika.

### Mabadiliko muhimu

| Kabla | Baada |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Ondoa kabisa |

### Orodha ya usafishaji

- Ondoa hoja ya `api_version` kutoka kwa ujenzi wa mteja.
- Ondoa mabadiliko ya mazingira ya `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` kwenye `.env`, mipangilio ya programu, na faili za Bicep/infra.
- Badilisha `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` kwenye `.env`, mipangilio ya programu, Bicep/infra, na vifaa vya mtihani (konvensheni ya kawaida ya SDK ya Azure Identity).
- Hakikisha `openai>=1.108.1` katika `requirements.txt` au `pyproject.toml`.

### Uhamishaji wa mabadiliko ya mazingira

| Mabadiliko ya zamani | Hatua | Maelezo |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Ondoa** | Hakuna `api_version` inayohitajika na kiambatisho cha v1 |
| `AZURE_OPENAI_API_VERSION` | **Ondoa** | Kama ilivyo hapo juu |
| `AZURE_OPENAI_CLIENT_ID` | **Badilisha jina** → `AZURE_CLIENT_ID` | Konvensheni ya kawaida ya SDK ya Azure Identity kwa `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Weka** | Bado inahitajika kwa ujenzi wa `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Weka** | Inatumiwa kama kigezo `model` katika `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Weka** | Inatumiwa kama `api_key` kwa uthibitishaji wa funguo |

Kwa mifano ya usanidi wa mteja (synchronous, asynchronous, EntraID, API key, multi-tenant), tazama [cheat-sheet.md](./references/cheat-sheet.md).

---

## Hatua 1: Tambua Maeneo ya Mwisho ya Zamani

Endesha script ya [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) kutafuta maeneo yote ya mwito yanayohitaji uhamishaji:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Au fanya utafutaji huu kwa mikono — kila patano ni lengo la uhamishaji:

```bash
# Miito ya API ya zamani (inapaswa kuandikwa upya)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Wahariri wa mteja wa Azure waliopitwa na wakati (inapaswa kubadilishwa)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Mifumo ya upatikanaji wa umbo la jibu (inapaswa kusasishwa)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Ufafanuzi wa zana katika muundo wa zamani uliojaa (inapaswa kufumwa)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Matokeo ya zana katika muundo wa zamani (inapaswa kubadilishwa kuwa function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Vigezo vilivyopitwa na wakati (inapaswa kuondolewa au kubadilishwa jina)
rg "response_format"
rg "max_tokens\b"        # badilisha jina kuwa max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Vigezo vya mazingira vilivyopitwa na wakati (kusafisha)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # inapaswa kuwa AZURE_CLIENT_ID

# Vituo vya Moduli za GitHub (inapaswa kuondolewa — API ya Majibu haitegemezwi)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Mifumo ya urithi wa kiwango cha mfumo (inapaswa kusasishwa)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: badilisha na OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: inahitaji use_responses_api=True

# Miundombinu ya mtihani (inapaswa kusasishwa)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Upatikanaji wa mwili wa hitilafu ya kichujio cha maudhui (inapaswa kusasishwa — muundo umebadilika)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # umbo la zamani la kipekee — sasa content_filter_results (wingi) ndani ya safu ya content_filters

# Miito ya moja kwa moja ya HTTP kwa kiungo cha Chat Completions (inapaswa kusasisha URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Kanuni za kugundua (gundua na andika upya)

- **Mteja wa Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Majengo ya mteja wa Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Vifaa**: badilisha ufafanuzi wa zana za kuiita kazi kutoka muundo uliojaa (`{"type": "function", "function": {"name": ...}}`) hadi muundo wa Spring Responses (`{"type": "function", "name": ...}`); tumia `tool_choice`; rudisha matokeo ya zana kama vitu vya `{"type": "function_call_output", "call_id": ..., "output": ...}` (sio `{"role": "tool", ...}`).
- **Mizunguko ya zana**: wakati mfano unarudisha miito ya kazi, ongeza vitu vya `response.output` kwenye mazungumzo (sio kamusi ya mkono ya `{"role": "assistant", "tool_calls": [...]}`), kisha ongeza vitu vya `function_call_output` kwa kila matokeo.
- **Mifano michache ya zana**: ikiwa mazungumzo yanajumuisha mifano ya miito ya zana iliyowekwa vikali, ibadilishe kuwa vitu vya `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. Vitambulisho lazima vianze na `fc_`.
- **`pydantic_function_tool()`**: msaidizi huyu bado hutengeneza muundo wa zamani uliojaa na **hauendani** na `responses.create()`. Badilisha kwa ufafanuzi wa zana wa mkono au kifuniko cha kulainisha.
- **Mizunguko mingi**: dumisha kumbukumbu ya mazungumzo katika app; pitisha kona za awali kupitia vitu vya `input`.
- **Uundaji**: badilisha `response_format` ya ngazi ya juu ya Chat kuwa `text.format` katika Responses. Umbo halisi: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Vitu vya maudhui**: badilisha `content[].type: "text"` ya Chat kuwa `content[].type: "input_text"` kwa mizunguko ya mtumiaji/sistem.
- **Vitu vya maudhui ya picha**: badilisha `content[].type: "image_url"` ya Chat kuwa `content[].type: "input_image"`. Sehemu ya `image_url` hubadilika kutoka kitu kilichojazwa `{"url": "..."}` kuwa mfuatiliaji rahisi. Tazama karatasi ya mbinu kwa mifano ya kabla/baada.
- **Juhudi za kufikiri**: **hamia tu `reasoning` ikiwa tayari ipo katika msimbo wa awali**.
- **Usimamizi wa makosa ya kichujio cha maudhui**: muundo wa mwili wa kosa umebadilika. Chat Completions ilitumia `error.body["innererror"]["content_filter_result"]` (moja); API ya Responses hutumia `error.body["content_filters"][0]["content_filter_results"]` (zaidi, ndani ya orodha). Msimbo unaotumia `innererror` utaongeza `KeyError`. Andika upya kutumia njia mpya.
- **Miito ya moja kwa moja ya HTTP**: ikiwa app inaita Azure OpenAI REST API moja kwa moja (kupitia `requests`, `httpx`, n.k.) ikitumia `/openai/deployments/{name}/chat/completions?api-version=...`, badilisha kuwa `/openai/v1/responses`. Mwili wa ombi hubadilika: `messages` → `input`, ongeza `max_output_tokens` na `store: false`, toa parameta ya kuulizia `api-version`. Mwili wa majibu hubadilika: `choices[0].message.content` → `output[0].content[0].text` (kumbuka: `output_text` ni sifa ya urahisi ya SDK isiyoonekana katika JSON ghafi ya REST).

---

## Hatua ya 2: Tekeleza Uhamiaji

### Vidokezo vya uhamiaji (Chat Completions → Responses)

- **Kwa nini uhamie**: Responses ni API ya umoja kwa maandishi, zana, na utiririshaji; Chat Completions ni ya zamani. Kwa GPT-5, Responses inahitajika kwa utendaji bora zaidi.
- **HTTP**: eneo la Azure linabadilika kutoka `/openai/deployments/{name}/chat/completions` kuwa `/openai/v1/responses`.
- **Sehemu**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` inabaki.
- **Uundaji**: `response_format` → `text.format` yenye kitu halali.
- **Vitu vya maudhui**: Badilisha `content[].type: "text"` ya Chat kuwa `content[].type: "input_text"` kwa mizunguko ya mtumiaji/sistem.
- **Vitu vya picha maudhui**: Badilisha `content[].type: "image_url"` ya Chat kuwa `content[].type: "input_image"`. Lainisha sehemu ya `image_url` kutoka `{"image_url": {"url": "..."}}` kuwa `{"image_url": "..."}` (inafuata mfuatiliaji wa kawaida - URL ya HTTPS au URI ya data ya base64 `data:image/...;base64,...`).

### Marejeleo ya ramani ya parameta

| Chat Completions | API ya Responses |
|-----------------|---------------------|
| `prompt` | `input` |
| `messages` | `input` (orodha ya vitu) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (kitu) |
| `temperature` | `temperature` (haijabadilika) |
| `stop` | `stop` (haijabadilika) |
| `frequency_penalty` | `frequency_penalty` (haijabadilika) |
| `presence_penalty` | `presence_penalty` (haijabadilika) |
| `tools` / kuitwa kwa kazi | `tools` (haijabadilika) |
| `seed` | **Toa** (haitekelezwi) |
| `store` | `store` (wekwa `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (mfuatiliaji mwepesi) |

Kwa mifano kamili ya kabla/baada ya msimbo, ona [cheat-sheet.md](./references/cheat-sheet.md).

Kwa uhamiaji wa miundombinu ya majaribio (mock, snapshot, uthibitisho), ona [test-migration.md](./references/test-migration.md).

Kwa kutatua matatizo na vidokezo, ona [troubleshooting.md](./references/troubleshooting.md).

---

## Uhifadhi wa Data & Hali

- Weka `store: false` kwenye maombi yote ya Responses.
- Usitegemee vitambulisho vya ujumbe wa awali au muktadha ulihifadhiwa kwenye seva; dumisha hali udhibitiwa na mteja na punguza metadata.

---

## Vigezo vya Kukubalika

### Vizuizi vya kiwango cha msimbo (vyote lazima vipite)

- [ ] Hakuna mechi ya `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` katika faili zilizohamishwa.
- [ ] Hakuna mechi ya `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — majengo yote yatumia `OpenAI`/`AsyncOpenAI` na eneo la v1.
- [ ] Hakuna mechi ya `rg "models\.github\.ai|models\.inference\.ai\.azure"` — njia za msimbo za GitHub Models zimeondolewa.
- [ ] Hakuna mechi ya `rg "OpenAIChatCompletionClient"` — msimbo wa MAF 1.0.0+ unatumia `OpenAIChatClient` (inayotumia API ya Responses). Kabla ya 1.0.0, sasisha kuwa `agent-framework-openai>=1.0.0`.
- [ ] Mito yote ya `ChatOpenAI(...)` inajumuisha `use_responses_api=True`.
- [ ] Hakuna mechi ya `rg "choices\[0\]"` — upatikanaji wote wa majibu unatumia `resp.output_text` au muundo wa output wa Responses.
- [ ] Hakuna `response_format` ngazi ya juu; mafanikio yote ya kimuundo yanatumia `text={"format": {...}}`.
- [ ] `openai>=1.108.1` na `azure-identity` katika `requirements.txt` au `pyproject.toml`; utegemezi umewekwa tena.
- [ ] `store=False` imewekwa katika kila simu ya `responses.create`.
- [ ] Hakuna `api_version` katika ujenzi wa mteja; `AZURE_OPENAI_API_VERSION` imeondolewa kutoka kwa faili za mazingira na miundombinu.

### Vizuizi vya miundombinu ya majaribio (vyote lazima vipite)

- [ ] Hakuna mechi ya `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Hakuna mechi ya `rg "_azure_ad_token_provider" tests/` — kuthibitisha kumesasishwa kuangalia `isinstance(client, AsyncOpenAI)` au `base_url`.
- [ ] Hakuna mechi ya `rg "prompt_filter_results|content_filter_results" tests/` — mock za kichujio maalum za Azure zimeondolewa.
- [ ] Mock fixtures hutumia `kwargs.get("input")` si `kwargs.get("messages")`.
- [ ] Faili za snapshot / dhahabu zimesasishwa kuwa umbo la utiririshaji la Responses (hakuna `choices[0]`, `function_call`, `logprobs`, n.k.).
- [ ] `pytest` inapitisha bila makosa baada ya masasisho yote ya majaribio.

### Vizuizi vya tabia (hakikisha kwa mkono au kupitia kifaa cha majaribio)

- [ ] **Umaliziaji wa msingi**: `responses.create` isiyotiririka inarudisha `output_text` isiyo tupu.
- [ ] **Ulinganifu wa utiririshaji**: ikiwa msimbo wa awali ulitumia utiririshaji, msimbo uliohamishwa hutiririsha na kutoa matukio ya `response.output_text.delta` yenye tofauti zisizo tupu.
- [ ] **Matokeo ya kimuundo**: ikiwa unatumia `text.format` yenye `json_schema`, `json.loads(resp.output_text)` inafanikiwa na inalingana na schema.
- [ ] **Mzunguko wa kuitwa zana**: ikiwa zana zina tumika, mfano hutoa miito ya zana, app inatekeleza, na ombi linalofuata hurejesha `output_text` ya mwisho (hakuna mzunguko usioisha).
- [ ] **Ulinganifu wa Async**: ikiwa `AsyncAzureOpenAI` ilitumika, mfano wa `AsyncOpenAI` unafanya kazi kwa `await`.
- [ ] **Kiwango cha makosa**: hakuna makosa mapya ya 400/401/404 ikilinganishwa na msingi wa kabla ya uhamiaji.

### Yanayopaswa Kutolewa

- Muhtasari unajumuisha faili zilizohaririwa, idadi za maeneo ya miito ya zamani kabla/baada, na hatua zinazofuata.
- Mabadiliko ni mabadiliko ya mti wa kazi tu (hakuna commits).

---

## Mahitaji ya Toleo la SDK

| Kipengee | Toleo la chini |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Ya hivi karibuni (kwa uthibitishaji wa EntraID) |

---

## Marejeleo

- [Karatasi ya Mbinu — vipande vyote vya msimbo](./references/cheat-sheet.md)
- [Uhamiaji wa Jaribio — mock, snapshot, uthibitisho](./references/test-migration.md)
- [Matatua ya Matatizo — makosa, jedwali la hatari, vidokezo](./references/troubleshooting.md)
- [detect_legacy.py — kijkeo kiotomatiki](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Hati za API za Azure OpenAI Responses](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Mzunguko wa toleo la API la Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Marejeleo ya API ya OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->