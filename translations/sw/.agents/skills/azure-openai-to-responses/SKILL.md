---
name: azure-openai-to-responses
license: MIT
---
# Hamisha Programu za Python kutoka Azure OpenAI Chat Completions kwenda Responses API

> **MWONGOZO WA MTAALAM — FUATA KIBEBE KIBEBE**
>
> Ujuzi huu unahamisha misimbo ya Python inayotumia Azure OpenAI Chat Completions
> kwenda API moja ya Responses. Fuata maagizo haya kwa ufasaha.
> Usibuni ramani za vigezo au umbize miundo ya API.

---

## Vichocheo

Washa ujuzi huu wakati mtumiaji anataka:
- Kuhamisha app ya Python kutoka Azure OpenAI Chat Completions kwenda Responses API
- Kuboresha matumizi ya SDK ya Python OpenAI kwa muundo wa API mpya dhidi ya Azure OpenAI
- Kuandaa msimbo wa Python kwa modeli za GPT-5 au mpya zaidi zinazohitaji Responses kwenye Azure
- Kubadilisha kutoka `AzureOpenAI`/`AsyncAzureOpenAI` kwenda mteja wa kawaida `OpenAI`/`AsyncOpenAI` na kiunganishi cha v1
- Kurekebisha onyo la kuachwa matumizi yanayohusiana na wajenzi wa `AzureOpenAI` au `api_version`

---

## ⚠️ Ulinganifu wa Modeli — KAGUA KWA MWANZO

> **Kabla ya kuhama, hakikisha usambazaji wako wa Azure OpenAI unaunga mkono Responses API.**

### 1. Jaribio la haraka la usambazaji wako (haraka zaidi)

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

> **Kumbuka**: `max_output_tokens` ina **chini kabisa ya 16** kwenye Azure OpenAI. Thamani chini ya 16 hurejesha kosa la 400. Tumia 50+ kwa majaribio ya haraka.

Ikiwa hii inarejesha 404, modeli ya usambazaji haijaunga mkono Responses bado — angalia rejea hapa chini au safisha tena na modeli inayounga mkono.

### 2. Kagua modeli zinazopatikana katika eneo lako (inapendekezwa)

Endesha chombo cha ulinganifu cha modeli kilichojengwa kuona kinachopatikana na msaada wa Responses API katika eneo lako maalum:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Hii huhitaji Azure ARM kuishi na kuonyesha matriki ya ulinganifu — modeli gani zinaunga mkono Responses, matokeo yaliyo na muundo, zana, nk. Tumia `--filter gpt-5.1,gpt-5.2` kupunguza matokeo au `--json` kwa hali ya usimbaji.

### 3. Rejea kamili la msaada wa modeli

- **Uchunguzi wa moja kwa moja**: `python migrate.py models` (angalia hapo juu — maalum kwa eneo, kila mara ni mpya)
- **Vinyozavyo upatikanaji**: [Jedwali la muhtasari wa modeli na upatikanaji wa eneo](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Mwongozo wa kuanzia kwa haraka**: **https://aka.ms/openai/start**

### ⚠️ Vizuizi vya modeli za zamani

> **ONYO**: Modeli za zamani (mfano, `gpt-4o`, `gpt-4`) huenda zisiunge mkono kabisa vipengele vyote vya Responses API.
>
> Vizuizi vinavyojulikana na modeli za zamani:
> - **Kigezo cha `reasoning`**: Hakihimizwi kwenye `gpt-4o-mini`, `gpt-4o`, na modeli nyingi zisizo za reasoning. Hamisha `reasoning` tu ikiwa tayari ilikuwa imetumika katika msimbo wa awali.
> - **Kigezo cha `seed`**: Hakihimizwi kabisa katika Responses API — toa kwenye maombi yote.
> - **Matokeo yaliyopangwa kupitia `text.format`**: Modeli za zamani huenda zisilazimishe schema za JSON za `strict: true` kwa uhakika.
> - **Mpangilio wa zana (tool orchestration)**: GPT-5+ husimamia simu za zana kama sehemu ya reasoning ya ndani. Modeli za zamani kwenye Responses bado hufanya kazi lakini hazina ushirikiano huu wa kina.
> - **Vizuizi vya joto la mtiririko (temperature constraints)**: Wakati wa kuhama kwenda `gpt-5`, joto lazima libaki zisizo na thamani au liwe `1`. Modeli za zamani hazina vizuizi hivi.

### Modeli za mfululizo O (o1, o3-mini, o3, o4-mini)

Modeli za mfululizo O zina vizuizi maalum vya vigezo. Unapohamisha programu zinazolenga modeli za mfululizo O:

- **`temperature`**: Lazima iwe ni `1` (au iachwe bila thamani). Modeli za mfululizo O hazikubali thamani nyingine.
- **`max_completion_tokens` → `max_output_tokens`**: Programu zinazotumia `max_completion_tokens` maalum ya Azure lazima zibadilishe kwenda `max_output_tokens`. Weka thamani kubwa (4096+) kwa sababu tokeni za reasoning huhesabiwa kwa kikomo.
- **`reasoning_effort`**: Ikiwa programu inatumia `reasoning_effort` (chini/katikati/juu), ibakie — Responses API inaunga mkono kigezo hiki kwa modeli za mfululizo O.
- **Tabia ya mtiririko (streaming behavior)**: Modeli za mfululizo O huenda zibongeze matokeo hadi reasoning itakapokamilika kabla ya kutoa matukio ya mabadiliko ya maandishi. Mtiririko bado hufanya kazi, lakini kwanza `response.output_text.delta` inaweza kufika baada ya kuchelewa zaidi ikilinganishwa na modeli za GPT.
- **`top_p`**: Haikubaliwi kwenye mfululizo O — toa ikiwa ipo.
- **Matumizi ya zana**: Modeli za mfululizo O zinaunga mkono zana kupitia Responses API kama vile modeli za GPT, lakini ubora wa mpangilio wa simu za zana hutofautiana kwa modeli.

**Tendo — ushauri wa modeli kwa njia ya tahadhari**: Wakati wa awamu ya ukaguzi, angalia ni modeli gani programu inalenga (majina ya deployments, mabadiliko ya mazingira, usanidi). Ikiwa modeli ni `gpt-4o` au ya zamani (si gpt-4.1+), kwa tahadhari mwambie mtumiaji:
- Uhamishaji utaendeshwa kwa maandishi ya msingi, mazungumzo, mtiririko, na zana kwenye modeli yao ya sasa.
- Modeli mpya (`gpt-5.1`, `gpt-5.2`) zina mpangilio bora wa zana, utekelezaji wa matokeo yaliyo na muundo, reasoning, na upatikanaji wa maeneo mbalimbali.
- Wanapaswa kufikiria kuboresha usambazaji wao wakati watakapokuwa tayari — si kizuizi kwa uhamishaji.

Usizui au kukataa kuhama kwa misingi ya toleo la modeli. Ushauri huu ni wa taarifa tu.

### GitHub Models HAIUNGA MKONO Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) haiungi mkono Responses API.**

Ikiwa msimbo una njia ya GitHub Models (angalia `base_url` inayoelekea `models.github.ai` au `models.inference.ai.azure.com`), **itoa kabisa** wakati wa uhamisho. Responses API inahitaji Azure OpenAI, OpenAI, au kiunganishi cha ndani kinachotegemewa (mfano, Ollama na msaada wa Responses).

Kitendo wakati wa ukaguzi:
- Taja njia zozote za msimbo wa GitHub Models kwa kuondolewa.

---

## Uhamisho wa Mfumo wa Kufanya Kazi (Framework Migration)

Programu nyingi hutumia mifumo ya juu zaidi juu ya OpenAI. Unapohamisha hizi, mabadiliko ni katika API ya mfumo wa kazi, si tu simu za msingi za OpenAI.

### Mfumo wa Wakala wa Microsoft (MAF)

**Kagua toleo lako la MAF kwanza** — uhamisho unategemea ikiwa uko kwenye MAF 1.0.0+ au beta/rc kabla ya 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **tayari hutumia Responses API** — hakuna uhamisho unaohitajika. Ikiwa msimbo unatumia zamani `OpenAIChatCompletionClient` (inayotumia `chat.completions.create`), badilisha na `OpenAIChatClient`.

| Kabla | Baada |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Kuangalia toleo lako: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF kabla ya 1.0.0 (maelezo ya beta/rc)

Katika MAF kabla ya 1.0.0, `OpenAIChatClient` ilitumia Chat Completions. Boresha kwa `agent-framework-openai>=1.0.0` ambapo `OpenAIChatClient` hutumia Responses API kwa chaguo-msingi.

Hakuna mabadiliko mengine yanayohitajika — API za `Agent` na zana zinabaki kama zilivyo.

### LangChain (`langchain-openai`)

Ongeza `use_responses_api=True` kwa `ChatOpenAI()`. Pia badilisha ufikivu wa majibu kutoka `.content` kwenda `.text`.

| Kabla | Baada |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Kwa mifano kamili ya msimbo kabla/baada, angalia [cheat-sheet.md](./references/cheat-sheet.md).

---

## Mwongozo wa Uhamisho wa Mbele ya Mtumiaji

> **Responses API ni suala la seva upande.** Hamisha backend yako ya Python; mkataba wa HTTP wa eneo la mbele haupaswi kubadilika isipokuwa backend yako ni njia mwembamba tu — katika hali hiyo, fikiria kutumia muundo wa ombi la Responses kuondoa tabaka la tafsiri. Ikiwa sehemu ya mbele inaita OpenAI moja kwa moja kwa ufunguo wa upande wa mteja, hamisha miito hiyo kwanza kwenye backend.

### Uachwaji wa `@microsoft/ai-chat-protocol`

Pakiti ya npm ya `@microsoft/ai-chat-protocol` imetangazwa haitatumiki na inapaswa kubadilishwa na [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Ikiwa unakutana nayo katika sehemu ya mbele:

1. Badilisha lebo ya script ya CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Toa uanzishaji wa `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Badilisha `client.getStreamedCompletion(messages)` kwa wito wa moja kwa moja `fetch()` kwenda sehemu ya mtiririko ya backend.
4. Badilisha `for await (const response of result)` kwa `for await (const chunk of readNDJSONStream(response.body))`.
5. Sasisha ufikivu wa mali kutoka `response.delta.content` / `response.error` kwenda `chunk.delta.content` / `chunk.error`.

---

## Malengo

- Taja maeneo yote ya simu ya Python yanayotumia Chat Completions au Completions ya zamani dhidi ya Azure OpenAI.
- Pendekeza mpango wa uhamisho na mfuatano wa uhamisho wa msimbo wa Python.
- Fanya mabadiliko salama, madogo kubadili kwenda Responses API.
- Sasisha wito wa maandishi ili watumie schema ya matokeo ya Responses; usitumie vitambazo vya ulinganifu wa nyuma.
- Endesha majaribio/lints; rekebisha makosa madogo yaliyotokana na uhamisho.
- Andaa seti ndogo za mabadiliko za kukaguliwa na toa muhtasari wa mwisho pamoja na tofauti (usihifadhi).

---

## Mipaka ya Usalama

- Badilisha faili ndani ya eneo la git tu. Usitoe chochote nje.
- Usihifadhi vitambazo vya ulinganifu wa nyuma; hamisha msimbo wa API mpya kabisa.
- Usiachie maoni ya kuhamisha au faili za akiba.
- Hifadhi mantiki ya mtiririko ikiwa ilitumika awali; vinginevyo tumia isiyopitia.
- Uliza idhini kabla ya kuendesha amri au mawasiliano ya mtandao ikiwa uko katika hali ya idhini.
- Usifanye `git add`/`git commit`/`git push`; tengeneza mabadiliko kwenye mti wa kazi tu.

---

## Hatua 0: Uhamisho wa Mteja wa Azure OpenAI (Shetani)

Ikiwa msimbo unatumia wajenzi `AzureOpenAI` au `AsyncAzureOpenAI`, hamisha kwa wajenzi wa kawaida `OpenAI` / `AsyncOpenAI` kwanza. Wajenzi maalum wa Azure wameachwa matumizi katika `openai>=1.108.1`.

### Kwanini njia ya API ya v1?

Kiunganishi kipya cha `/openai/v1` kinatumia mteja wa kawaida `OpenAI()` badala ya `AzureOpenAI()`, hakihitaji kigezo cha `api_version`, na hufanya kazi sawa kwenye OpenAI na Azure OpenAI. Msimbo huo huo wa mteja ni wa baadaye — hakuna usimamizi wa toleo unaohitajika.

### Mabadiliko muhimu

| Kabla | Baada |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Ondoa kabisa |

### Kagua Usafi

- Ondoa hoja ya `api_version` kutoka ujenzi wa mteja.
- Ondoa vigezo vya mazingira `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` kutoka `.env`, mipangilio ya programu, na faili za Bicep/miundo.
- Badilisha jina la `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` katika `.env`, mipangilio, Bicep/miundo, na vifaa vya mtihani (kawaida ya SDK ya Azure Identity).
- Hakikisha `openai>=1.108.1` katika `requirements.txt` au `pyproject.toml`.

### Uhamisho wa vigezo vya mazingira

| Kigezo cha zamani | Tendo | Maelezo |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Ondoa** | Hakuna `api_version` inahitajika na kiunganishi cha v1 |
| `AZURE_OPENAI_API_VERSION` | **Ondoa** | Kama ilivyo juu |
| `AZURE_OPENAI_CLIENT_ID` | **Badilisha jina** → `AZURE_CLIENT_ID` | Kawaida ya SDK ya Azure Identity kwa `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Hifadhi** | Bado inahitajika kwa ujenzi wa `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Hifadhi** | Inatumiwa kama kigezo cha `model` katika `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Hifadhi** | Inatumiwa kama `api_key` kwa uthibitishaji kwa msingi wa ufunguo |

Kwa mifano ya msimbo wa usanidi wa mteja (synchronous, asynchronous, EntraID, kiunganishi cha API, multi-tenant), angalia [cheat-sheet.md](./references/cheat-sheet.md).

---

## Hatua 1: Tambua Sehemu za Kale za Simu

Endesha skripti ya [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) kupata maeneo yote ya simu yanayohitaji uhamisho:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Au fanya utafutaji huu kwa mkono — kila patano ni lengo la uhamisho:

```bash
# Simu za API za kale (lazima uandike upya)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Majengo ya mteja wa Azure yaliyopotoka (lazima uibadilishe)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Mifumo ya upatikanaji wa umbo la jibu (lazima uasasishaji)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Maelezo ya zana katika umbizo la zamani lililojikunja (lazima uifanane)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Matokeo ya zana katika umbizo la zamani (lazima ubadilishe kuwa function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Vigezo vilivyopotoka (lazima viondolewe au vibrege)
rg "response_format"
rg "max_tokens\b"        # birejeleo kuwa max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Mabadilishano ya mazingira yaliyopotoka (takataka safi)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # inapaswa kuwa AZURE_CLIENT_ID

# Vituo vya Modeli za GitHub (lazima yaondolewe — API za Majibu hazitoi msaada)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Mifumo ya urithi wa ngazi ya mfumo (lazima uasasishaji)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: badilisha na OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: inahitaji use_responses_api=True

# Miundombinu ya mtihani (lazima uasasishaji)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Upatikanaji wa mwili wa kosa la kichujio cha maudhui (lazima uasasishaji — muundo umebadilika)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # Umbizo la zamani la sari — sasa content_filter_results (mara nyingi) ndani ya safu ya content_filters

# Simu ghafi za HTTP kwa kituo cha Chat Completions (lazima uasasishaji URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Mbinu za kuangalia (gundua na andika upya)

- **Mteja wa Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Mjenzi wa mteja wa Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Zana**: badilisha ufafanuzi wa zana za kuwaita kazi kutoka muundo ulio ndani (`{"type": "function", "function": {"name": ...}}`) hadi muundo wa Responses ulio wima (`{"type": "function", "name": ...}`); tumia `tool_choice`; rudisha matokeo ya zana kama vitu vya `{"type": "function_call_output", "call_id": ..., "output": ...}` (si `{"role": "tool", ...}`).
- **Mizunguko ya zana**: wakati mfano unarudisha mwito wa kazi, ongeza vitu vya `response.output` kwenye mazungumzo (si kamusi ya mkono ya `{"role": "assistant", "tool_calls": [...]}`), kisha ongeza vitu vya `function_call_output` kwa kila matokeo.
- **Mifano michache ya zana**: ikiwa mazungumzo yanajumuisha mifano ya mwito wa zana yenye msimbo mkali, ibadilishe kuwa vitu vya `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. Vitambulisho lazima vianze na `fc_`.
- **`pydantic_function_tool()`**: msaidizi huyu bado hutengeneza muundo wa zamani wa ndani na **hauendani** na `responses.create()`. Badilisha kwa ufafanuzi wa zana za mkono au kifuniko cha kuondoa ukatirifu.
- **Mizunguko mingi**: hifadhi historia ya mazungumzo katika app; pita zamu zilizopita kupitia vitu vya `input`.
- **Uundaji**: badilisha `response_format` ya ngazi ya juu ya Chat na `text.format` katika Responses. Umbo halisi: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Vitu vya maudhui**: badilisha Chat `content[].type: "text"` na Responses `content[].type: "input_text"` kwa zamu za mtumiaji/mfumo.
- **Vitu vya maudhui ya picha**: badilisha Chat `content[].type: "image_url"` na Responses `content[].type: "input_image"`. Sehemu ya `image_url` hubadilika kutoka kitu kilicho ndani `{"url": "..."}` kuwa mfuatano rahisi. Tazama kibao cha mbinu kwa mifano kabla/baada.
- **Jitihada za kufikiri**: **hamia tu `reasoning` ikiwa tayari ipo kwenye msimbo wa asili**.
- **Zamisho la hitilafu za kichujio cha maudhui**: muundo wa mwili wa hitilafu ulibadilika. Chat Completions ilitumia `error.body["innererror"]["content_filter_result"]` (moja); Responses API hutumia `error.body["content_filters"][0]["content_filter_results"]` (kwingineko, ndani ya safu). Msimbo unaotumia `innererror` utaleta `KeyError`. Andika upya ili utumie njia mpya.
- **Mitoaji ya HTTP ghafi**: ikiwa app inadhamiria API ya Azure OpenAI REST moja kwa moja (kutumia `requests`, `httpx`, n.k.) kwa `/openai/deployments/{name}/chat/completions?api-version=...`, andika upya hadi `/openai/v1/responses`. Mwili wa ombi hubadilika: `messages` → `input`, ongeza `max_output_tokens` na `store: false`, toa parameta ya kuuliza `api-version`. Mwili wa jibu hubadilika: `choices[0].message.content` → `output[0].content[0].text` (taarifa: `output_text` ni mali ya SDK ya urahisi isiyo kwenye REST JSON ghafi).

---

## Hatua 2: Tumia Uhamisho

### Vidokezo vya Uhamisho (Chat Completions → Responses)

- **Kwa nini kuhamisha**: Responses ni API iliyounganishwa kwa maandishi, zana, na mtiririko; Chat Completions ni ya zamani. Kwa GPT-5, Responses ni muhimu kwa utendaji bora.
- **HTTP**: Kituo cha Azure kinabadilika kutoka `/openai/deployments/{name}/chat/completions` hadi `/openai/v1/responses`.
- **Sehemu**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` inabaki.
- **Uundaji**: `response_format` → `text.format` na kitu sahihi.
- **Vitu vya maudhui**: Badilisha Chat `content[].type: "text"` na Responses `content[].type: "input_text"` kwa zamu za mfumo/mtumiaji.
- **Vitu vya maudhui ya picha**: Badilisha Chat `content[].type: "image_url"` na Responses `content[].type: "input_image"`. Tenganisha sehemu ya `image_url` kutoka `{"image_url": {"url": "..."}}` hadi `{"image_url": "..."}` (kamba rahisi — URL ya HTTPS au URI ya data ya `data:image/...;base64,...`).

### Marejeleo ya ramani za vigezo

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (safu ya vitu) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (kitu) |
| `temperature` | `temperature` (bila mabadiliko) |
| `stop` | `stop` (bila mabadiliko) |
| `frequency_penalty` | `frequency_penalty` (bila mabadiliko) |
| `presence_penalty` | `presence_penalty` (bila mabadiliko) |
| `tools` / function-calling | `tools` (bila mabadiliko) |
| `seed` | **Ondoa** (haitekelezwi) |
| `store` | `store` (weka kuwa `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (kamba sawa) |

Kwa mifano kamili ya msimbo kabla/baada, angalia [cheat-sheet.md](./references/cheat-sheet.md).

Kwa uhamisho wa miundombinu ya majaribio (mocks, nakala, ushahidi), angalia [test-migration.md](./references/test-migration.md).

Kwa utatuzi wa matatizo na hila, angalia [troubleshooting.md](./references/troubleshooting.md).

---

## Uhifadhi Data & Hali

- Weka `store: false` kwenye maombi yote ya Responses.
- Usitegemee vitambulisho vya ujumbe vya awali au muktadha uliohifadhiwa kwenye seva; hudumia hali ikisimamiwa na mteja na punguza metadata.

---

## Vigezo vya Kukubali

### Vikovyo vya ngazi ya msimbo (vyote lazima viwe sahihi)

- [ ] Hakuna mechi za `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` katika faili zilizohamishwa.
- [ ] Hakuna mechi za `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — majengo yote ya mteja yanatumia `OpenAI`/`AsyncOpenAI` na kituo cha v1.
- [ ] Hakuna mechi za `rg "models\.github\.ai|models\.inference\.ai\.azure"` — njia za msimbo za GitHub Models zimetolewa.
- [ ] Hakuna mechi za `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ msimbo unatumia `OpenAIChatClient` (ambayo hutumia API ya Responses). Kabla ya 1.0.0, boresha hadi `agent-framework-openai>=1.0.0`.
- [ ] Mitoaji yote ya `ChatOpenAI(...)` jumuisha `use_responses_api=True`.
- [ ] Hakuna mechi za `rg "choices\[0\]"` — ufikiaji wote wa jibu hutumia `resp.output_text` au muundo wa jibu wa Responses.
- [ ] Hakuna `response_format` kwenye ngazi ya juu; matokeo yote yaliyo na muundo hutumia `text={"format": {...}}`.
- [ ] `openai>=1.108.1` na `azure-identity` kwenye `requirements.txt` au `pyproject.toml`; utegemezi umewekwa upya.
- [ ] `store=False` imetangazwa kila mwito wa `responses.create`.
- [ ] Hakuna `api_version` katika kujenga mteja; `AZURE_OPENAI_API_VERSION` imetolewa kwenye faili za mazingira na miundombinu.

### Vikovyo vya miundombinu ya majaribio (vyote lazima viwe sahihi)

- [ ] Hakuna mechi za `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Hakuna mechi za `rg "_azure_ad_token_provider" tests/` — uthibitisho umeboreshwa ili kuchunguza `isinstance(client, AsyncOpenAI)` au `base_url`.
- [ ] Hakuna mechi za `rg "prompt_filter_results|content_filter_results" tests/` — mocks maalum ya kichujio cha Azure zimetolewa.
- [ ] Vipimo vya mock vinatumia `kwargs.get("input")` si `kwargs.get("messages")`.
- [ ] Nakala / faili za dhahabu zimebadilishwa hadi umbo la mtiririko la Responses (hakuna `choices[0]`, `function_call`, `logprobs`, n.k.).
- [ ] `pytest` hupita bila makosa baada ya masasisho yote ya majaribio.

### Vikovyo vya mienendo (hakikisha kwa mikono au kupitia kifaa cha mtihani)

- [ ] **Kamilisho msingi**: `responses.create` isiyotiririsha inarudisha `output_text` isiyo tupu.
- [ ] **Usawa wa mtiririko**: ikiwa msimbo wa asili ulitumia mtiririko, msimbo ulihamishwa hutiririsha na kutoa matukio ya `response.output_text.delta` yenye tofauti zisizo tupu.
- [ ] **Matokeo yaliyo na muundo**: ikiwa unatumia `text.format` na `json_schema`, `json.loads(resp.output_text)` inafanikiwa na inalingana na muundo.
- [ ] **Mzunguko wa mwito wa zana**: ikiwa zana zinatumika, mfano hutoa miito ya zana, app huita, na ombi la kufuatilia hurudisha `output_text` ya mwisho (hakuna mzunguko usio na mwisho).
- [ ] **Usawa wa Async**: ikiwa `AsyncAzureOpenAI` ilitumika, sawa ya `AsyncOpenAI` inafanya kazi kwa `await`.
- [ ] **Kiwango cha hitilafu**: hakuna makosa mapya ya 400/401/404 ikilinganishwa na mstari wa msingi kabla ya uhamisho.

### Vifaa vinavyopaswa kutolewa

- Muhtasari unajumuisha faili zilizo haririwa, hesabu kabla/b baada ya vituo vya mwito vya zamani, na hatua zinazofuata.
- Mabadiliko ni ya mti wa kazi tu (hakuna commits).

---

## Mahitaji ya Toleo la SDK

| Kifurushi | Toleo la Angalau |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Ya Hivi Karibuni (kwa uthibitishaji wa EntraID) |

---

## Marejeleo

- [Kibao cha Mbinu — vipande vyote vya msimbo](./references/cheat-sheet.md)
- [Uhamisho wa Mtihani — mocks, nakala, ushahidi](./references/test-migration.md)
- [Utatuzi wa Matatizo — hitilafu, jedwali la hatari, hila](./references/troubleshooting.md)
- [detect_legacy.py — kipiga otomatiki](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Kifurushi cha Mwanzo cha Azure OpenAI](https://aka.ms/openai/start)
- [Hati za Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Mzunguko wa toleo la Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Marejeleo ya OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->