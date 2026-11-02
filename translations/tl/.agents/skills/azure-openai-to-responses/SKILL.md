---
name: azure-openai-to-responses
license: MIT
description: 'Ilipat ang mga Python app mula sa Azure OpenAI Chat Completions papuntang
  Responses API. Saklaw nito ang pag-migrate ng AzureOpenAI/AsyncAzureOpenAI client
  sa v1 endpoint, streaming, tools, structured output, multi-turn, EntraID auth, at
  mga pagsusuri sa compatibility ng modelo. Nakatuon sa Python, para sa Azure OpenAI.
  GAMITIN PARA SA: pag-migrate sa responses API, paglipat mula sa chat completions,
  openai responses, pag-upgrade ng openai SDK, migration sa responses API, paglipat
  mula completions sa responses, gpt-5 migration, azure openai python migration, chat
  completions papuntang responses, AzureOpenAI papuntang OpenAI client, python azure
  openai upgrade. HUWAG GAMITIN PARA SA: paggawa ng mga bagong app mula sa simula
  (simulan direkta sa responses), Node/TypeScript/C#/Java/Go migrations (Python lang
  ang kasanayang ito), Azure infrastructure setup (gumamit ng azure-prepare), pag-deploy
  ng mga modelo (gumamit ng microsoft-foundry).'
---
# Ilipat ang mga Python App mula sa Azure OpenAI Chat Completions patungo sa Responses API

> **AWTORITATIBONG GABAY — SUNODAN NG TAMA**
>
> Inililipat ng kasanayang ito ang mga Python codebases na gumagamit ng Azure OpenAI Chat Completions
> papunta sa pinag-isang Responses API. Sundin nang tumpak ang mga tagubiling ito.
> Huwag mag-improvise sa mga parameter mappings o gumawa ng bagong hugis ng API.

---

## Mga Trigger

Isaaktibo ang kasanayang ito kapag nais ng user na:
- Ilipat ang isang Python app mula sa Azure OpenAI Chat Completions patungo sa Responses API
- I-upgrade ang paggamit ng Python OpenAI SDK sa pinakabagong hugis ng API laban sa Azure OpenAI
- Ihanda ang Python code para sa GPT-5 o mas bagong mga modelo na nangangailangan ng Responses sa Azure
- Lumipat mula sa `AzureOpenAI`/`AsyncAzureOpenAI` papuntang standard na `OpenAI`/`AsyncOpenAI` client gamit ang v1 endpoint
- Ayusin ang mga babalang deprecation na may kinalaman sa mga `AzureOpenAI` constructors o `api_version`

---

## ⚠️ Compatibility ng Modelo — SURIIN MUNA

> **Bago mag-migrate, tiyaking sinusuportahan ng iyong Azure OpenAI deployment ang Responses API.**

### 1. Subukan ang iyong deployment (pinakamabilis)

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

> **Tandaan**: Ang `max_output_tokens` ay may **minimum na 16** sa Azure OpenAI. Ang mga halagang mas mababa sa 16 ay magbabalik ng 400 error. Gumamit ng 50 pataas para sa mga smoke test.

Kung magbabalik ito ng 404, ang modelo ng deployment ay hindi pa sumusuporta sa Responses — tingnan ang reference sa ibaba o mag-redeploy gamit ang suportadong modelo.

### 2. Suriin ang mga available na modelo sa iyong rehiyon (inirerekomenda)

Patakbuhin ang built-in na tool ng compatibility ng modelo upang makita kung ano ang available na may suporta sa Responses API sa iyong partikular na rehiyon:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Nagtatanong ito ng live sa Azure ARM at nagpapakita ng compatibility matrix — kung aling mga modelo ang sumusuporta sa Responses, structured output, tools, atbp. Gamitin ang `--filter gpt-5.1,gpt-5.2` para paliitin ang resulta o `--json` para sa scripting.

### 3. Buong reference sa suporta ng modelo

- **Live query**: `python migrate.py models` (tingnan sa itaas — region-specific, laging up to date)
- **Tingnan ang availability**: [Model summary table and region availability](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Quickstart & gabay**: **https://aka.ms/openai/start**

### ⚠️ Mga limitasyon ng mas lumang modelo

> **BABALA**: Ang mga lumang modelo (mga nauna sa `gpt-4.1`) ay maaaring hindi sumusuporta nang buo sa lahat ng mga feature ng Responses API.
>
> Kilalang mga limitasyon sa mga lumang modelo:
> - **`reasoning` parameter**: Hindi sinusuportahan sa maraming non-reasoning models. Ilipat lamang ang `reasoning` kung dati itong nandito sa orihinal na code.
> - **`seed` parameter**: Hindi sinusuportahan sa Responses API — alisin ito sa lahat ng request.
> - **Structured output sa pamamagitan ng `text.format`**: Ang mga lumang modelo ay maaaring hindi maaasahang gamitin ang `strict: true` JSON schemas.
> - **Tool orchestration**: Ang GPT-5+ ay nag-o-orchestrate ng tawag sa tool bilang bahagi ng internal na pag-iisip. Ang mga lumang modelo sa Responses ay gumagana pa rin ngunit walang ganitong malalim na integration.
> - **Temperature constraints**: Kapag lumilipat sa `gpt-5`, ang temperature ay dapat tanggalin o itakda sa `1`. Ang mga lumang modelo ay walang ganitong limitasyon.

### Mga O-series reasoning models (o1, o3-mini, o3, o4-mini)

May mga natatanging limitasyon sa mga parameter ang O-series models. Kapag nililipat ang apps na target ang mga o-series na modelo:

- **`temperature`**: Dapat `1` (o tanggalin). Hindi tinatanggap ng O-series ang ibang halaga.
- **`max_completion_tokens` → `max_output_tokens`**: Ang mga app na gumagamit ng Azure-specific na `max_completion_tokens` ay dapat lumipat sa `max_output_tokens`. Magtakda ng mataas na halaga (4096+) dahil ang mga reasoning token ay bibilangin laban sa limitasyon.
- **`reasoning_effort`**: Kung gumagamit ang app ng `reasoning_effort` (mababa/katamtaman/mataas), panatilihin ito — sinusuportahan ito ng Responses API para sa o-series na modelo.
- **Streaming behavior**: Ang O-series models ay maaaring mag-buffer ng output hanggang matapos ang reasoning bago maglabas ng mga text delta events. Gumagana pa rin ang streaming, ngunit ang unang `response.output_text.delta` ay maaaring dumating nang mas matagal kaysa sa GPT models.
- **`top_p`**: Hindi sinusuportahan sa o-series — alisin kung nandiyan.
- **Paggamit ng tool**: Sinusuportahan ng O-series models ang mga tools gamit ang Responses API na katulad ng GPT models, ngunit nagkakaiba ang kalidad ng tool call orchestration depende sa modelo.

**Aksyon — proactive na advisory sa modelo**: Sa panahon ng scan phase, suriin kung aling modelo ang target ng app (mga deployment name, env vars, config). Kung ang modelo ay nauna sa `gpt-4.1` (hindi gpt-4.1+), ipaalam nang proactively sa user:
- Tatakbo ang migration para sa basic text, chat, streaming, at tools sa kanilang kasalukuyang modelo.
- Nag-aalok ang mas bagong mga modelo (`gpt-5.1`, `gpt-5.2`) ng mas mahusay na tool orchestration, structured output enforcement, reasoning, at availability sa iba't ibang rehiyon.
- Dapat nilang isaalang-alang ang pag-upgrade ng kanilang deployment kapag handa na — hindi ito hadlang sa migration.

Huwag pigilan o tanggihan ang migration batay sa bersyon ng modelo. Ang advisory ay para lang sa impormasyon.

### Hindi sinusuportahan ng GitHub Models ang Responses API

> **Ang GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) ay hindi sumusuporta sa Responses API.**

Kung ang codebase ay may GitHub Models code path (tingnan ang `base_url` na nagtuturo sa `models.github.ai` o `models.inference.ai.azure.com`), **alisin ito nang buo** habang nagmi-migrate. Nangangailangan ang Responses API ng Azure OpenAI, OpenAI, o compatible na lokal na endpoint (hal. Ollama na may Responses support).

Aksyon sa panahon ng scan:
- I-flag ang anumang GitHub Models code paths para alisin.

---

## Paglilipat ng Framework

Maraming apps ang gumagamit ng mas mataas na antas na mga framework sa ibabaw ng OpenAI. Kapag nililipat ito, nagbabago hindi lang ang mga tawag sa OpenAI kundi pati ang API ng framework mismo.

### Microsoft Agent Framework (MAF)

**Suriin muna ang iyong bersyon ng MAF** — nakadepende ang paglilipat kung ikaw ay nasa MAF 1.0.0+ o pre-1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Ang `OpenAIChatClient` **ay gumagamit na ng Responses API** — hindi na kailangan ng migration. Kung gumagamit ang codebase ng legacy na `OpenAIChatCompletionClient` (na gumagamit ng `chat.completions.create`), palitan ito ng `OpenAIChatClient`.

| Bago | Pagkatapos |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Para suriin ang iyong bersyon: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)" `

#### MAF pre-1.0.0 (beta/rc releases)

Sa pre-1.0.0 MAF, ang `OpenAIChatClient` ay gumagamit ng Chat Completions. I-upgrade sa `agent-framework-openai>=1.0.0` kung saan ang `OpenAIChatClient` ang default na gumagamit ng Responses API.

Walang ibang pagbabago ang kailangan — nananatili ang `Agent` at tool APIs.

### LangChain (`langchain-openai`)

Magdagdag ng `use_responses_api=True` sa `ChatOpenAI()`. Palitan din ang pag-access ng response mula `.content` patungo sa `.text`.

| Bago | Pagkatapos |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Para sa kumpletong halimbawa ng code bago/pagkatapos, tingnan ang [cheat-sheet.md](./references/cheat-sheet.md).

---

## Gabay sa Paglilipat sa Frontend

> **Ang Responses API ay tungkol sa server-side.** Ilipat ang iyong Python backend; dapat manatiling pareho ang HTTP contract ng frontend maliban kung ang backend mo ay isang manipis na pass-through lang — sa ganitong kaso, isaalang-alang ang paggamit ng Responses request shape para alisin ang translation layer. Kung direktang tumatawag ang frontend sa OpenAI gamit ang client-side key, ilipat ang tawag sa backend muna.

### Deprecated na `@microsoft/ai-chat-protocol`

Ang npm package na `@microsoft/ai-chat-protocol` ay deprecated at dapat palitan ng [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Kung makita ito sa frontend:

1. Palitan ang CDN script tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Alisin ang `AIChatProtocolClient` instantiation (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Palitan ang `client.getStreamedCompletion(messages)` ng direktang `fetch()` call sa backend streaming endpoint.
4. Palitan ang `for await (const response of result)` ng `for await (const chunk of readNDJSONStream(response.body))`.
5. I-update ang pag-access ng properties mula `response.delta.content` / `response.error` papuntang `chunk.delta.content` / `chunk.error`.

---

## Mga Layunin

- Itala ang lahat ng Python call sites na gumagamit ng Chat Completions o legacy Completions laban sa Azure OpenAI.
- Magmungkahi ng plano sa migration at pagkakasunod-sunod para sa Python codebase.
- Gawin ang mga ligtas at minimal na pag-edit para lumipat sa Responses API.
- I-update ang mga caller para gamitin ang Responses output schema; walang mga backcompat wrapper.
- Patakbuhin ang mga tests/lint; ayusin ang mga simpleng sira na dulot ng migration.
- Ihanda ang maliliit at madaling suring change set at magbigay ng huling buod na may diffs (huwag mag-commit).

---

## Mga Patakaran

- Baguhin lamang ang mga file sa loob ng git workspace. Huwag magsulat sa labas nito.
- Huwag panatilihin ang backward-compatibility shims; i-migrate ang code sa bagong hugis ng API.
- Huwag mag-iwan ng mga tombstone/transition comments o mga backup file.
- Panatilihin ang streaming semantics kung dating ginamit; kung hindi, gamitin ang non-streaming.
- Humingi ng pag-apruba bago magpatakbo ng mga command o network call kung nasa approval mode.
- Huwag magpatakbo ng `git add`/`git commit`/`git push`; gumawa lamang ng mga edit sa working-tree.

---

## Hakbang 0: Paglilipat ng Azure OpenAI Client (Paunang Kailangan)

Kung gumagamit ang codebase ng `AzureOpenAI` o `AsyncAzureOpenAI` constructors, ilipat muna sa standard na `OpenAI` / `AsyncOpenAI` constructors. Ang Azure-specific constructors ay deprecated sa `openai>=1.108.1`.

### Bakit ang v1 API path?

Ang bagong `/openai/v1` endpoint ay gumagamit ng standard na `OpenAI()` client sa halip na `AzureOpenAI()`, hindi na nangangailangan ng `api_version` parameter, at pareho ang pagkilos sa OpenAI at Azure OpenAI. Ang parehong client code ay pangmatagalan — walang kailangan na version management.

### Mga pangunahing pagbabago

| Bago | Pagkatapos |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Alisin nang buo |

### Checklist sa paglilinis

- Alisin ang `api_version` na argumento mula sa client construction.
- Alisin ang mga environment variables `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` mula sa `.env`, app settings, at Bicep/infra files.
- Palitan ang `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` sa `.env`, app settings, Bicep/infra, at test fixtures (standard na Azure Identity SDK convention).
- Siguraduhin na `openai>=1.108.1` ang nasa `requirements.txt` o `pyproject.toml`.

### Paglilipat ng environment variable

| Lumang env var | Aksyon | Tala |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Alisin** | Hindi na kailangan ng `api_version` sa v1 endpoint |
| `AZURE_OPENAI_API_VERSION` | **Alisin** | Pareho ng nasa itaas |
| `AZURE_OPENAI_CLIENT_ID` | **Palitan** → `AZURE_CLIENT_ID` | Standard na convention sa Azure Identity SDK para sa `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Panatilihin** | Kailangan pa rin para sa `base_url` construction |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Panatilihin** | Ginagamit bilang `model` parameter sa `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Panatilihin** | Ginagamit bilang `api_key` para sa key-based na authentication |

Para sa mga halimbawa ng client setup code (sync, async, EntraID, API key, multi-tenant), tingnan ang [cheat-sheet.md](./references/cheat-sheet.md).

---

## Hakbang 1: Tukuyin ang Legacy Call Sites

Patakbuhin ang script na [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) upang mahanap ang lahat ng call sites na kailangang i-migrate:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

O patakbuhin nang mano-mano ang mga paghahanap — bawat tugma ay target ng migration:

```bash
# Mga tawag sa Legacy API (kailangang isulat muli)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Mga deprecated na Azure client constructors (kailangang palitan)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Mga pattern ng pag-access sa hugis ng tugon (kailangang i-update)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Mga depinisyon ng tool sa lumang nested na format (kailangang gawing patag)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Mga resulta ng tool sa lumang format (kailangang i-convert sa function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Mga deprecated na parameter (kailangang alisin o palitan ang pangalan)
rg "response_format"
rg "max_tokens\b"        # palitan ng pangalan sa max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Mga deprecated na env vars (linisin)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # dapat ay AZURE_CLIENT_ID

# Mga GitHub Models endpoints (kailangang alisin — Hindi suportado ang Responses API)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Mga legacy pattern sa antas ng framework (kailangang i-update)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: palitan ng OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: kailangan ang use_responses_api=True

# Test infrastructure (kailangang i-update)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Pag-access sa error body ng content filter (kailangang i-update — nagbago ang istruktura)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # Lumang anyong singular — ngayon ay content_filter_results (maramihan) sa loob ng content_filters array

# Raw HTTP calls sa Chat Completions endpoint (kailangang i-update ang URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristics (tuklasin at i-rewrite)

- **Chat Completions client**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Mga constructor ng Azure client**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Mga Tools**: i-convert ang mga function-calling tool definitions mula nested na format (`{"type": "function", "function": {"name": ...}}`) papuntang flat Responses format (`{"type": "function", "name": ...}`); gamitin ang `tool_choice`; ibalik ang mga resulta ng tool bilang `{"type": "function_call_output", "call_id": ..., "output": ...}` items (hindi `{"role": "tool", ...}`).
- **Mga round-trip ng Tool**: kapag ang model ay nagbabalik ng function calls, idagdag ang `response.output` items sa usapan (hindi manual na `{"role": "assistant", "tool_calls": [...]}` dict), pagkatapos ay idagdag ang mga `function_call_output` items para sa bawat resulta.
- **Mga Few-shot na halimbawa ng tool**: kung ang usapan ay may kasamang mga hardcoded tool call na halimbawa, i-convert ang mga ito sa `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` na mga item. Dapat magsimula ang mga ID sa `fc_`.
- **`pydantic_function_tool()`**: ang helper na ito ay patuloy na gumagawa ng lumang nested format at **hindi compatible** sa `responses.create()`. Palitan ng manual na tool definitions o flattening wrapper.
- **Multi-turn**: panatilihin ang kasaysayan ng usapan sa app; ipasa ang mga naunang turn sa pamamagitan ng `input` items.
- **Pag-format**: palitan ang top-level na `response_format` ng Chat sa `text.format` sa Responses. Canonical na anyo: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Mga item ng nilalaman**: palitan ang Chat `content[].type: "text"` ng Responses `content[].type: "input_text"` para sa mga user/system na turno.
- **Mga item ng nilalaman ng larawan**: palitan ang Chat `content[].type: "image_url"` ng Responses `content[].type: "input_image"`. Ang field na `image_url` ay nagbabago mula sa nested na object na `{"url": "..."}` papuntang flat na string. Tingnan ang cheat sheet para sa mga halimbawa bago/pagkatapos.
- **Pagsisikap sa pangangatwiran**: **ililipat lamang ang `reasoning` kung ito ay umiiral na sa orihinal na code**.
- **Pag-handle ng error sa content filter**: nagbago ang istruktura ng error body. Ang Chat Completions ay gumagamit ng `error.body["innererror"]["content_filter_result"]` (isahan); ang Responses API ay gumagamit ng `error.body["content_filters"][0]["content_filter_results"]` (maramihan, nasa loob ng array). Ang code na gumagamit ng `innererror` ay magreresulta ng `KeyError`. Isulat muli upang gamitin ang bagong path.
- **Raw HTTP calls**: kung ang app ay tumatawag nang direkta sa Azure OpenAI REST API (sa pamamagitan ng `requests`, `httpx`, etc.) gamit ang `/openai/deployments/{name}/chat/completions?api-version=...`, palitan ng `/openai/v1/responses`. Nagbabago ang request body: `messages` → `input`, magdagdag ng `max_output_tokens` at `store: false`, alisin ang `api-version` query param. Nagbabago ang response body: `choices[0].message.content` → `output[0].content[0].text` (tandaan: ang `output_text` ay isang SDK convenience property na wala sa raw REST JSON).

---

## Hakbang 2: Isaayos ang Migration

### Mga tala sa migration (Chat Completions → Responses)

- **Bakit mag-migrate**: Ang Responses ay ang pinag-isang API para sa teksto, mga tools, at streaming; ang Chat Completions ay legacy na. Sa GPT-5, kailangan ang Responses para sa pinakamahusay na performance.
- **HTTP**: Ang Azure endpoint ay lumilipat mula sa `/openai/deployments/{name}/chat/completions` papuntang `/openai/v1/responses`.
- **Mga field**: `messages` → `input`, `max_tokens` → `max_output_tokens`. Ang `temperature` ay nananatili.
- **Pag-format**: `response_format` → `text.format` na may angkop na object.
- **Mga item ng nilalaman**: Palitan ang Chat `content[].type: "text"` ng Responses `content[].type: "input_text"` para sa mga system/user na turno.
- **Mga item ng nilalaman ng larawan**: Palitan ang Chat `content[].type: "image_url"` ng Responses `content[].type: "input_image"`. I-flatten ang field na `image_url` mula `{"image_url": {"url": "..."}}` papuntang `{"image_url": "..."}` (isang plain string — maaaring HTTPS URL o isang `data:image/...;base64,...` data URI).

### Sanggunian sa parameter mapping

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array ng mga item) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (object) |
| `temperature` | `temperature` (hindi nagbago) |
| `stop` | `stop` (hindi nagbago) |
| `frequency_penalty` | `frequency_penalty` (hindi nagbago) |
| `presence_penalty` | `presence_penalty` (hindi nagbago) |
| `tools` / function-calling | `tools` (hindi nagbago) |
| `seed` | **Alisin** (hindi suportado) |
| `store` | `store` (itakda sa `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (flat string) |

Para sa kumpletong mga halimbawa ng code bago/pagkatapos, tingnan ang [cheat-sheet.md](./references/cheat-sheet.md).

Para sa pag-migrate ng test infrastructure (mocks, snapshots, assertions), tingnan ang [test-migration.md](./references/test-migration.md).

Para sa pag-troubleshoot ng mga error at mga mahahalagang paalala, tingnan ang [troubleshooting.md](./references/troubleshooting.md).

---

## Pagpapanatili ng Data at Estado

- Itakda ang `store: false` sa lahat ng Requests ng Responses.
- Huwag umasa sa mga naunang message ID o kontekstong naka-imbak sa server; panatilihin ang estado na pinamamahalaan ng kliyente at i-minimize ang metadata.

---

## Mga Pamantayan sa Pagtanggap

### Mga code-level na gate (lahat ay dapat pumasa)

- [ ] Walang tumutugma para sa `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` sa mga na-migrate na file.
- [ ] Walang tumutugma para sa `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — lahat ng mga constructor ay gumagamit ng `OpenAI`/`AsyncOpenAI` sa v1 endpoint.
- [ ] Walang tumutugma para sa `rg "models\.github\.ai|models\.inference\.ai\.azure"` — tinanggal ang mga code path ng GitHub Models.
- [ ] Walang tumutugma para sa `rg "OpenAIChatCompletionClient"` — Ginagamit ng MAF 1.0.0+ na code ang `OpenAIChatClient` (na gumagamit ng Responses API). Sa pre-1.0.0, i-upgrade sa `agent-framework-openai>=1.0.0`.
- [ ] Lahat ng tawag sa `ChatOpenAI(...)` ay may `use_responses_api=True`.
- [ ] Walang tumutugma para sa `rg "choices\[0\]"` — lahat ng pag-access sa response ay gumagamit ng `resp.output_text` o ang schema ng output sa Responses.
- [ ] Walang `response_format` sa top level; lahat ng structured output ay gumagamit ng `text={"format": {...}}`.
- [ ] `openai>=1.108.1` at `azure-identity` sa `requirements.txt` o `pyproject.toml`; mga dependencies ay nai-install muli.
- [ ] Itina-set ang `store=False` sa bawat tawag ng `responses.create`.
- [ ] Walang `api_version` sa construction ng client; tinanggal ang `AZURE_OPENAI_API_VERSION` mula sa mga env file at infra.

### Mga gate para sa test infrastructure (lahat ay dapat pumasa)

- [ ] Walang tumutugma para sa `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Walang tumutugma para sa `rg "_azure_ad_token_provider" tests/` — na-update ang mga assertion upang suriin ang `isinstance(client, AsyncOpenAI)` o `base_url`.
- [ ] Walang tumutugma para sa `rg "prompt_filter_results|content_filter_results" tests/` — tinanggal ang mga Azure-specific filter mocks.
- [ ] Ang mga mock fixture ay gumagamit ng `kwargs.get("input")` hindi `kwargs.get("messages")`.
- [ ] Na-update ang snapshot / golden files sa Responses streaming shape (walang `choices[0]`, `function_call`, `logprobs`, atbp.).
- [ ] Pumasa ang `pytest` na walang pagkabigo pagkatapos ng lahat ng update sa test.

### Mga gate sa pag-uugali (beripikahin nang manu-mano o gamit ang test harness)

- [ ] **Basic completion**: non-streaming `responses.create` ay nagbabalik ng non-empty `output_text`.
- [ ] **Stream parity**: kung ang orihinal na code ay gumamit ng streaming, ang na-migrate na code ay nag-stream at naglalabas ng `response.output_text.delta` na mga event na may non-empty deltas.
- [ ] **Structured output**: kung gumagamit ng `text.format` na may `json_schema`, ang `json.loads(resp.output_text)` ay matagumpay at tumutugma sa schema.
- [ ] **Tool-call loop**: kung may gamit na mga tool, ang model ay gumagawa ng tool calls, pinapatakbo ng app ang mga ito, at ang sumunod na request ay nagbabalik ng panghuling `output_text` (walang walang katapusang loop).
- [ ] **Async parity**: kung ginamit ang `AsyncAzureOpenAI`, ang katumbas na `AsyncOpenAI` ay gumagana gamit ang `await`.
- [ ] **Error rate**: walang bagong 400/401/404 errors kumpara sa baseline bago ang migration.

### Mga Deliverables

- Kasama sa summary ang mga na-edit na file, bilang ng legacy call site bago/pagkatapos, at mga susunod na hakbang.
- Ang mga pagbabago ay sa working-tree lang (walang commits).

---

## Mga Pangangailangan sa Bersyon ng SDK

| Package | Pinakamababang Bersyon |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Pinakabago (para sa EntraID auth) |

---

## Mga Sanggunian

- [Cheat Sheet — lahat ng mga code snippet](./references/cheat-sheet.md)
- [Test Migration — mocks, snapshots, assertions](./references/test-migration.md)
- [Troubleshooting — mga error, risk table, mga paalala](./references/troubleshooting.md)
- [detect_legacy.py — automated scanner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API docs](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API reference](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->