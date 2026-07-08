---
name: azure-openai-to-responses
license: MIT
description: 'Ilipat ang mga Python na app mula sa Azure OpenAI Chat Completions patungo
  sa Responses API. Saklaw nito ang AzureOpenAI/AsyncAzureOpenAI client migration
  sa v1 endpoint, streaming, tools, structured output, multi-turn, EntraID auth, at
  mga tseke sa pagiging compatible ng modelo. Nakatuon sa Python, partikular sa Azure
  OpenAI. GAMITIN PARA SA: paglipat sa responses API, pag-switch mula sa chat completions,
  openai responses, pag-upgrade ng openai SDK, responses API migration, paglipat mula
  completions patungong responses, gpt-5 migration, azure openai python migration,
  chat completions patungong responses, AzureOpenAI patungong OpenAI client, python
  azure openai upgrade. HUWAG GAMITIN PARA SA: pagbuo ng bagong mga app mula sa simula
  (simulan nang direkta sa responses), Node/TypeScript/C#/Java/Go migrations (ang
  kasanayang ito ay para lamang sa Python), Azure infrastructure setup (gamitin ang
  azure-prepare), pag-deploy ng mga modelo (gamitin ang microsoft-foundry).'
---
# Ilipat ang mga Python App mula Azure OpenAI Chat Completions papuntang Responses API

> **AWTORITATIBONG PATNUBAY — SUNDIN NG TAMA**
>
> Inililipat ng kasanayang ito ang mga codebase ng Python na gumagamit ng Azure OpenAI Chat Completions
> sa pinag-isang Responses API. Sundin nang eksakto ang mga tagubiling ito.
> Huwag mag-improvise ng parameter mappings o gumawa ng mga bagong hugis ng API.

---

## Mga Trigger

Isaaktibo ang kasanayang ito kapag nais ng gumagamit na:
- Ilipat ang Python app mula Azure OpenAI Chat Completions papuntang Responses API
- I-upgrade ang paggamit ng Python OpenAI SDK sa pinakabagong hugis ng API laban sa Azure OpenAI
- Ihanda ang Python code para sa GPT-5 o mas bagong mga modelo na nangangailangan ng Responses sa Azure
- Lumipat mula sa `AzureOpenAI`/`AsyncAzureOpenAI` papuntang pangkaraniwang `OpenAI`/`AsyncOpenAI` client gamit ang v1 endpoint
- Ayusin ang mga babalang deprecation na may kaugnayan sa `AzureOpenAI` constructors o `api_version`

---

## ⚠️ Compatibility ng Modelo — SURIIN MUNA

> **Bago mag-migrate, tiyaking sinusuportahan ng iyong Azure OpenAI deployment ang Responses API.**

### 1. Smoke-test ang iyong deployment (pinakamabilis)

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

> **Tandaan**: Ang `max_output_tokens` ay may **minimum na 16** sa Azure OpenAI. Mga halagang mas mababa sa 16 ay magbibigay ng error na 400. Gumamit ng 50+ para sa smoke tests.

Kung ito ay magreresulta sa 404, hindi pa sinusuportahan ng deployment na modelo ang Responses — tingnan ang sanggunian sa ibaba o muling ideploy gamit ang suportadong modelo.

### 2. Suriin ang mga available na modelo sa iyong rehiyon (inirerekomenda)

Patakbuhin ang built-in na tool para sa compatibility ng modelo upang makita kung ano ang available na may suporta sa Responses API sa iyong partikular na rehiyon:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Itong query na ito ay kumukuha ng Azure ARM live at nagpapakita ng compatibility matrix — kung aling mga modelo ang sumusuporta ng Responses, structured output, tools, atbp. Gamitin ang `--filter gpt-5.1,gpt-5.2` para pag-ibayuhin ang resulta o `--json` para sa scripting.

### 3. Buong sanggunian sa suporta ng modelo

- **Live query**: `python migrate.py models` (tingnan sa itaas — rehiyon-specipiko, palaging napapanahon)
- **Browse availability**: [Model summary table and region availability](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Quickstart at gabay**: **https://aka.ms/openai/start**

### ⚠️ Mga limitasyon ng mas lumang modelo

> **BABALA**: Maaaring hindi ganap na suportahan ng mas lumang mga modelo (hal. `gpt-4o`, `gpt-4`) ang lahat ng tampok ng Responses API.
>
> Kilalang mga limitasyon sa mas lumang mga modelo:
> - **Parameter na `reasoning`**: Hindi sinusuportahan sa `gpt-4o-mini`, `gpt-4o`, at maraming non-reasoning na modelo. Ilipat lamang ang `reasoning` kung ito ay nasa orihinal na code na.
> - **Parameter na `seed`**: Hindi sinusuportahan sa Responses API — alisin sa lahat ng kahilingan.
> - **Structured output sa pamamagitan ng `text.format`**: Maaaring hindi maayos na ipatupad ng mga mas lumang modelo ang `strict: true` JSON schemas.
> - **Tool orchestration**: Ang GPT-5+ ay nag-oorganisa ng tool calls bilang bahagi ng internal reasoning. Gumagana pa rin ang mas lumang mga modelo sa Responses ngunit walang ganitong malalim na integrasyon.
> - **Temperature constraints**: Kapag lumilipat sa `gpt-5`, kailangang iwan o itakda ang temperature sa `1`. Walang ganitong limitasyon ang mas lumang mga modelo.

### Mga modelo ng O-series reasoning (o1, o3-mini, o3, o4-mini)

May natatanging parameter constraints ang O-series models. Kapag nagmi-migrate ng mga app na target ang o-series models:

- **`temperature`**: Dapat ay `1` (o hindi inilalagay). Hindi tinatanggap ng o-series models ang ibang mga halaga.
- **`max_completion_tokens` → `max_output_tokens`**: Ang mga app na gumagamit ng Azure-specific na `max_completion_tokens` ay kailangang lumipat sa `max_output_tokens`. Itakda ang mataas na halaga (4096+) dahil binibilang ang reasoning tokens para sa limitasyon.
- **`reasoning_effort`**: Kung ginagamit ng app ang `reasoning_effort` (low/medium/high), panatilihin ito — sinusuportahan ng Responses API ang parameter na ito para sa o-series models.
- **Streaming behavior**: Maaaring i-buffer ng o-series models ang output hanggang matapos ang reasoning bago maglabas ng mga text delta events. Gumagana pa rin ang streaming, ngunit maaaring dumating ang unang `response.output_text.delta` nang mas mabagal kumpara sa GPT models.
- **`top_p`**: Hindi sinusuportahan sa o-series — alisin kung naroroon.
- **Paggamit ng Tool**: Sinusuportahan ng o-series models ang mga tools sa pamamagitan ng Responses API katulad ng GPT models, ngunit iba-iba ang kalidad ng tool call orchestration depende sa modelo.

**Aksyon — proactive na advisory sa modelo**: Sa panahon ng scan phase, suriin kung anong modelo ang target ng app (mga pangalan ng deployment, env vars, config). Kung ang modelo ay `gpt-4o` o mas luma (hindi gpt-4.1+), ipaalam nang proactive sa user:
- Gagana ang migration para sa basic na teksto, chat, streaming, at tools sa kasalukuyan nilang modelo.
- Mas magaganda ang tool orchestration, structured output enforcement, reasoning, at cross-region availability ng mas bagong mga modelo (`gpt-5.1`, `gpt-5.2`).
- Dapat nilang isaalang-alang ang pag-upgrade ng kanilang deployment kapag handa na — hindi ito hadlang sa migration.

Huwag pigilan o tanggihan ang migration base sa bersyon ng modelo. Ang advisory ay panuto lamang.

### Hindi sinuportahan ng GitHub Models ang Responses API

> **Hindi sinusuportahan ng GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) ang Responses API.**

Kung ang codebase ay may GitHub Models code path (tingnan ang `base_url` na tumuturo sa `models.github.ai` o `models.inference.ai.azure.com`), **alisin ito nang buo** sa panahon ng migration. Nangangailangan ang Responses API ng Azure OpenAI, OpenAI, o kompatibleng lokal na endpoint (hal. Ollama na may suporta sa Responses).

Aksyon habang nagsi-scan:
- I-flag ang anumang GitHub Models code paths para alisin.

---

## Pag-migrate ng Framework

Maraming mga app ang gumagamit ng mga higher-level frameworks sa ibabaw ng OpenAI. Kapag ini-migrate ito, nagbabago ang API ng framework mismo — hindi lang ang mga pang-ibaba ng OpenAI calls.

### Microsoft Agent Framework (MAF)

**Suriin muna ang iyong MAF version** — nakasalalay ang migration kung nasa MAF 1.0.0+ ka o mas maagang beta/rc ng pre-1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Ang `OpenAIChatClient` **ay gumagamit na ng Responses API** — walang kinakailangang migration. Kung ang codebase ay gumagamit ng legacy na `OpenAIChatCompletionClient` (na gumagamit ng `chat.completions.create`), palitan ito ng `OpenAIChatClient`.

| Bago | Pagkatapos |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Upang suriin ang iyong bersyon: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc releases)

Sa pre-1.0.0 MAF, ang `OpenAIChatClient` ay gumagamit ng Chat Completions. Mag-upgrade sa `agent-framework-openai>=1.0.0` kung saan ang `OpenAIChatClient` ay default na gumagamit ng Responses API.

Walang iba pang pagbabago ang kailangan — nananatili ang `Agent` at tool APIs.

### LangChain (`langchain-openai`)

Idagdag ang `use_responses_api=True` sa `ChatOpenAI()`. I-update din ang access sa response mula `.content` papuntang `.text`.

| Bago | Pagkatapos |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Para sa kumpletong mga halimbawa ng code bago/pagkatapos, tingnan ang [cheat-sheet.md](./references/cheat-sheet.md).

---

## Gabay sa Frontend Migration

> **Ang Responses API ay usapin sa server-side.** Ilipat ang iyong Python backend; hindi dapat magbago ang HTTP contract ng frontend maliban kung ang backend mo ay payat na pass-through — sa ganitong kaso, isaalang-alang ang paggamit ng hugis ng Responses request upang tanggalin ang translation layer. Kung ang frontend ay tumatawag direkta sa OpenAI gamit ang client-side key, ilipat muna ang mga tawag na ito sa backend.

### Pag-deprecate ng `@microsoft/ai-chat-protocol`

Ang `@microsoft/ai-chat-protocol` npm package ay deprecated at dapat palitan ng [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Kung makita mo ito sa frontend:

1. Palitan ang CDN script tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Alisin ang `AIChatProtocolClient` na instantiation (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Palitan ang `client.getStreamedCompletion(messages)` ng direktang tawag na `fetch()` sa backend streaming endpoint.
4. Palitan ang `for await (const response of result)` ng `for await (const chunk of readNDJSONStream(response.body))`.
5. I-update ang property access mula `response.delta.content` / `response.error` papuntang `chunk.delta.content` / `chunk.error`.

---

## Mga Layunin

- Itala ang lahat ng Python call sites na gumagamit ng Chat Completions o legacy Completions laban sa Azure OpenAI.
- Magmungkahi ng plano at sekwensiya para sa migration ng Python codebase.
- Mag-apply ng ligtas, minimal na mga pag-edit upang lumipat sa Responses API.
- I-update ang mga tumatawag upang gamitin ang output schema ng Responses; walang backcompat wrappers.
- Patakbuhin ang mga tests/lints; ayusin ang mga simpleng sirang dulot ng migration.
- Ihanda ang maliliit, madaling suriin na mga pagbabago at magbigay ng huling buod na may mga diff (huwag mag-commit).

---

## Mga Guardrails

- Baguhin lamang ang mga file sa loob ng git workspace. Huwag magsulat sa labas nito.
- Huwag panatilihin ang backward-compatibility shims; imigrate ang code sa bagong hugis ng API.
- Huwag mag-iwan ng mga tombstone/transition na komento o backup files.
- Panatilihin ang streaming semantics kung dati nang ginamit; kung hindi, gamitin ang non-streaming.
- Humingi ng pag-apruba bago magpatakbo ng mga command o network calls kung nasa approval mode.
- Huwag patakbuhin ang `git add`/`git commit`/`git push`; gumawa lamang ng mga pagbabago sa working-tree.

---

## Hakbang 0: Azure OpenAI Client Migration (Pangunahing Kailangan)

Kung gumagamit ang codebase ng `AzureOpenAI` o `AsyncAzureOpenAI` constructors, ilipat muna sa pangkaraniwang `OpenAI` / `AsyncOpenAI` constructors. Ang Azure-specific constructors ay deprecated sa `openai>=1.108.1`.

### Bakit ang v1 API path?

Ang bagong `/openai/v1` endpoint ay gumagamit ng pangkaraniwang `OpenAI()` client sa halip na `AzureOpenAI()`, hindi na nangangailangan ng `api_version` parameter, at gumagana nang pareho sa OpenAI at Azure OpenAI. Ang parehong client code ay pangmatagalan — hindi na kailangan ng pamamahala ng bersyon.

### Mga Pangunahing Pagbabago

| Bago | Pagkatapos |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Alisin nang buo |

### Checklist sa Paglilinis

- Alisin ang `api_version` argument mula sa konstruksiyon ng client.
- Alisin ang `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` na environment variables mula sa `.env`, app settings, at Bicep/infra files.
- Palitan ang pangalan ng `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` sa `.env`, app settings, Bicep/infra, at test fixtures (standard na convention ng Azure Identity SDK).
- Siguraduhing `openai>=1.108.1` sa `requirements.txt` o `pyproject.toml`.

### Migration ng environment variable

| Lumang env var | Aksyon | Mga Tala |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Alisin** | Hindi na kailangan ang `api_version` sa v1 endpoint |
| `AZURE_OPENAI_API_VERSION` | **Alisin** | Ganon din tulad ng nasa itaas |
| `AZURE_OPENAI_CLIENT_ID` | **Palitan ng pangalan** → `AZURE_CLIENT_ID` | Standard na convention ng Azure Identity SDK para sa `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Panatilihin** | Kailangan pa rin para sa konstruksyon ng `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Panatilihin** | Ginagamit bilang `model` param sa `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Panatilihin** | Ginagamit bilang `api_key` para sa key-based auth |

Para sa mga halimbawa ng client setup (sync, async, EntraID, API key, multi-tenant), tingnan ang [cheat-sheet.md](./references/cheat-sheet.md).

---

## Hakbang 1: Tuklasin ang Legacy Call Sites

Patakbuhin ang [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) script upang hanapin lahat ng call sites na kailangang i-migrate:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

O patakbuhin ang mga paghahanap na ito nang manu-mano — bawat tugma ay target ng migration:

```bash
# Mga tawag sa Legacy API (kailangan isulat muli)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Mga deprecated na Azure client constructors (kailangan palitan)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Mga pattern ng pag-access sa response shape (kailangan i-update)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Mga kahulugan ng tool sa lumang nested na format (kailangan gawing patag)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Mga resulta ng tool sa lumang format (kailangang i-convert sa function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Mga deprecated na parameter (kailangan tanggalin o palitan ng pangalan)
rg "response_format"
rg "max_tokens\b"        # palitan ang pangalan sa max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Mga deprecated na env vars (linisin)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # dapat ay AZURE_CLIENT_ID

# GitHub Models endpoints (kailangang tanggalin — Hindi sinusuportahan ang Responses API)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Mga pattern ng framework-level legacy (kailangan i-update)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: palitan ng OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: kailangan ang use_responses_api=True

# Test infrastructure (kailangan i-update)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Pag-access sa content filter error body (kailangan i-update — nagbago ang istruktura)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # lumang anyong isahan — ngayon content_filter_results (maramihan) sa loob ng array na content_filters

# Raw HTTP calls sa Chat Completions endpoint (kailangan i-update ang URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristics (detect at rewrite)

- **Chat Completions client**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure client constructors**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Tools**: i-convert ang mga depinisyon ng tool na tumatawag ng function mula sa nested na format (`{"type": "function", "function": {"name": ...}}`) patungo sa flat Responses format (`{"type": "function", "name": ...}`); gamitin ang `tool_choice`; ibalik ang mga resulta ng tool bilang mga item na `{"type": "function_call_output", "call_id": ..., "output": ...}` (hindi `{"role": "tool", ...}`).
- **Tool round-trips**: kapag ang modelo ay nagbalik ng mga pagtawag sa function, idagdag ang mga item na `response.output` sa pag-uusap (hindi isang manwal na `{"role": "assistant", "tool_calls": [...]}` na diksyonaryo), pagkatapos ay idagdag ang mga item na `function_call_output` para sa bawat resulta.
- **Few-shot tool examples**: kung ang pag-uusap ay may kasamang mga hardcoded na halimbawa ng pagtawag sa tool, i-convert ang mga ito sa `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + mga item na `{"type": "function_call_output", ...}`. Ang mga ID ay dapat magsimula sa `fc_`.
- **`pydantic_function_tool()`**: ang helper na ito ay nagbibigay pa rin ng lumang nested na format at **hindi kompatible** sa `responses.create()`. Palitan ng mga manwal na depinisyon ng tool o isang flattening na wrapper.
- **Multi-turn**: panatilihin ang kasaysayan ng pag-uusap sa app; ipasa ang mga naunang turn gamit ang mga item na `input`.
- **Formatting**: palitan ang Chat na top-level na `response_format` ng `text.format` sa Responses. Canonical na anyo: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Content items**: palitan ang Chat `content[].type: "text"` ng Responses `content[].type: "input_text"` para sa mga turn ng user/system.
- **Image content items**: palitan ang Chat `content[].type: "image_url"` ng Responses `content[].type: "input_image"`. Ang field na `image_url` ay nagbabago mula sa nested na object na `{"url": "..."}` papuntang flat na string. Tingnan ang cheat sheet para sa mga halimbawa bago/ pagkatapos.
- **Reasoning effort**: **ilipat lamang ang `reasoning` kung ito ay umiiral na sa orihinal na code**.
- **Content filter error handling**: nagbago ang istruktura ng error body. Ginamit ng Chat Completions ang `error.body["innererror"]["content_filter_result"]` (isahan); ang Responses API ay gumagamit ng `error.body["content_filters"][0]["content_filter_results"]` (maramihan, nasa loob ng array). Ang code na uma-access sa `innererror` ay magreresulta sa `KeyError`. Isulat muli upang gamitin ang bagong path.
- **Raw HTTP calls**: kung ang app ay tumatawag nang direkta sa Azure OpenAI REST API (gamit ang `requests`, `httpx`, atbp.) sa `/openai/deployments/{name}/chat/completions?api-version=...`, isulat muli patungo sa `/openai/v1/responses`. Nagbabago ang request body: `messages` → `input`, idagdag ang `max_output_tokens` at `store: false`, alisin ang query param na `api-version`. Nagbabago ang response body: `choices[0].message.content` → `output[0].content[0].text` (tandaan: `output_text` ay isang SDK convenience property na wala sa raw REST JSON).

---

## Hakbang 2: Isagawa ang Migrasyon

### Mga Tala sa Migrasyon (Chat Completions → Responses)

- **Bakit lilipat**: Ang Responses ay ang pinag-isang API para sa teksto, tools, at streaming; ang Chat Completions ay legacy. Sa GPT-5, kailangan ang Responses para sa pinakamahusay na performance.
- **HTTP**: Nagbabago ang endpoint ng Azure mula `/openai/deployments/{name}/chat/completions` patungo sa `/openai/v1/responses`.
- **Mga Fields**: `messages` → `input`, `max_tokens` → `max_output_tokens`. Nanatili ang `temperature`.
- **Formatting**: `response_format` → `text.format` na may angkop na object.
- **Mga Content items**: Palitan ang Chat `content[].type: "text"` ng Responses `content[].type: "input_text"` para sa mga turn ng system/user.
- **Mga Image content items**: Palitan ang Chat `content[].type: "image_url"` ng Responses `content[].type: "input_image"`. I-flatten ang `image_url` mula sa `{"image_url": {"url": "..."}}` patungo sa `{"image_url": "..."}` (isang plain string — pwedeng HTTPS URL o `data:image/...;base64,...` data URI).

### Sanggunian para sa Pagsasalin ng Parameter

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
| `seed` | **Tanggalin** (hindi suportado) |
| `store` | `store` (iset sa `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (flat string) |

Para sa kumpletong mga halimbawa ng code bago/ pagkatapos, tingnan ang [cheat-sheet.md](./references/cheat-sheet.md).

Para sa migrasyon ng test infrastructure (mocks, snapshots, assertions), tingnan ang [test-migration.md](./references/test-migration.md).

Para sa pag-troubleshoot ng mga error at mga problema, tingnan ang [troubleshooting.md](./references/troubleshooting.md).

---

## Data Retention & Estado

- Itakda ang `store: false` sa lahat ng mga kahilingan ng Responses.
- Huwag umasa sa mga naunang message ID o sa server-stored na konteksto; panatilihin ang estado na pinangangasiwaan ng client at bawasan ang metadata.

---

## Mga Acceptance Criteria

### Mga Code-level gates (dapat lahat pumasa)

- [ ] Walang tugmang `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` sa mga na-migrate na files.
- [ ] Walang tugmang `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — lahat ng constructors ay gumagamit ng `OpenAI`/`AsyncOpenAI` na may v1 endpoint.
- [ ] Walang tugmang `rg "models\.github\.ai|models\.inference\.ai\.azure"` — mga code paths ng GitHub Models ay tinanggal.
- [ ] Walang tugmang `rg "OpenAIChatCompletionClient"` — Ang MAF 1.0.0+ code ay gumagamit ng `OpenAIChatClient` (na gumagamit ng Responses API). Sa pre-1.0.0, i-upgrade sa `agent-framework-openai>=1.0.0`.
- [ ] Lahat ng tawag na `ChatOpenAI(...)` ay may kasamang `use_responses_api=True`.
- [ ] Walang tugmang `rg "choices\[0\]"` — lahat ng pag-access sa response ay gumagamit ng `resp.output_text` o ng Responses output schema.
- [ ] Wala nang `response_format` sa top level; lahat ng istraktura ng output ay gumagamit ng `text={"format": {...}}`.
- [ ] `openai>=1.108.1` at `azure-identity` ay nasa `requirements.txt` o `pyproject.toml`; dependencies ay na-reinstall.
- [ ] Naka-set ang `store=False` sa bawat tawag sa `responses.create`.
- [ ] Wala nang `api_version` sa pagbuo ng client; tinanggal ang `AZURE_OPENAI_API_VERSION` mula sa mga env files at infra.

### Mga Test infrastructure gates (dapat lahat pumasa)

- [ ] Walang tugmang `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Walang tugmang `rg "_azure_ad_token_provider" tests/` — mga assertion ay in-update upang i-check ang `isinstance(client, AsyncOpenAI)` o `base_url`.
- [ ] Walang tugmang `rg "prompt_filter_results|content_filter_results" tests/` — Azure-specific na filter mocks ay tinanggal.
- [ ] Ang mga mock fixtures ay gumagamit ng `kwargs.get("input")` hindi `kwargs.get("messages")`.
- [ ] Ang mga snapshot / golden files ay na-update sa Responses streaming shape (wala nang `choices[0]`, `function_call`, `logprobs`, atbp.).
- [ ] Pumasa ang `pytest` nang walang failure pagkatapos ng lahat ng pag-update ng tests.

### Mga Behavioral gates (suriin nang manual o gamit ang test harness)

- [ ] **Basic completion**: ang non-streaming na `responses.create` ay nagbabalik ng hindi walang laman na `output_text`.
- [ ] **Stream parity**: kung ang orihinal na code ay gumamit ng streaming, ang na-migrate na code ay nag-stream at nagbibigay ng mga event na `response.output_text.delta` na may mga non-empty na delta.
- [ ] **Structured output**: kung gumagamit ng `text.format` gamit ang `json_schema`, ang `json.loads(resp.output_text)` ay matagumpay at tumutugma sa schema.
- [ ] **Tool-call loop**: kung ginagamit ang mga tools, ang modelo ay naglalabas ng mga tool calls, ang app ay nagpapatupad nito, at ang follow-up na kahilingan ay nagbabalik ng panghuling `output_text` (walang walang katapusang loop).
- [ ] **Async parity**: kung ginamit ang `AsyncAzureOpenAI`, gumagana ang katumbas na `AsyncOpenAI` sa `await`.
- [ ] **Error rate**: walang bagong 400/401/404 errors kumpara sa pre-migration baseline.

### Mga Deliverables

- Kasama sa buod ang mga na-edit na files, bilang bago/ pagkatapos ng legacy call sites, at mga susunod na hakbang.
- Ang mga pagbabago ay mga edits lamang sa working-tree (walang commits).

---

## Mga Kinakailangan sa Bersyon ng SDK

| Package | Minimum na Bersyon |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Pinakabago (para sa EntraID auth) |

---

## Mga Sanggunian

- [Cheat Sheet — lahat ng code snippets](./references/cheat-sheet.md)
- [Test Migration — mocks, snapshots, assertions](./references/test-migration.md)
- [Troubleshooting — mga error, risk table, mga gotchas](./references/troubleshooting.md)
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