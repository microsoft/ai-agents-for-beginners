---
name: azure-openai-to-responses
license: MIT
---
# Perkelti Python programėles iš Azure OpenAI Chat Completions į Responses API

> **AUTORITETINĖS NUKREIPTYS — TIKSLIAI VYKDYTI**
>
> Ši įgūdžių sistema perkelia Python kodų bazes, naudojančias Azure OpenAI Chat Completions,
> į vieningą Responses API. Tiksliai vykdykite šias instrukcijas.
> Neimprovizuokite parametrų atitikimų ar nenumatytų API formų.

---

## Trigeriai

Aktyvinkite šį įgūdį, kai vartotojas nori:
- Perkelti Python programėlę iš Azure OpenAI Chat Completions į Responses API
- Atnaujinti Python OpenAI SDK naudojimą iki naujausios API formos Azure OpenAI atžvilgiu
- Paruošti Python kodą GPT-5 ar naujesniems modeliams, kuriems reikia Responses Azure platformoje
- Pereiti nuo `AzureOpenAI`/`AsyncAzureOpenAI` prie standartinio `OpenAI`/`AsyncOpenAI` kliento su v1 endpoint’u
- Išspręsti deprecijavimo įspėjimus, susijusius su `AzureOpenAI` konstruktoriais arba `api_version`

---

## ⚠️ Modelių suderinamumas — PATIKRINKITE PIRMIAUSIA

> **Prieš migraciją patikrinkite, ar jūsų Azure OpenAI diegimas palaiko Responses API.**

### 1. Išbandykite diegimą paprastai (greičiausias būdas)

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

> **Pastaba**: Azure OpenAI `max_output_tokens` turi **minimalų 16**. Vertės mažesnės nei 16 grąžina 400 klaidą. Dėl testų naudokite daugiau nei 50.

Jei grąžina 404, diegimo modelis dar nepalaiko Responses — patikrinkite toliau pateiktą nuorodą arba persirikiuokite su palaikomu modeliu.

### 2. Patikrinkite modelių prieinamumą savo regione (rekomenduojama)

Paleiskite įmontuotą modelių suderinamumo įrankį, kad pamatytumėte, kas yra prieinama ir palaiko Responses API jūsų regione:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Tai atlieka Azure ARM tiesioginį užklausimą ir rodo suderinamumo matricą — kurie modeliai palaiko Responses, struktūrizuotą išvestį, įrankius ir pan. Naudokite `--filter gpt-5.1,gpt-5.2`, kad siaurintumėte rezultatus arba `--json` skriptavimui.

### 3. Visapusiškas modelių palaikymo žinynas

- **Tiesioginis užklausimas**: `python migrate.py models` (žr. aukščiau — regionui specifiškas, visada atnaujintas)
- **Naršymas**: [Modelių santraukos lentelė ir regiono prieinamumas](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Greitas startas & gaires**: **https://aka.ms/openai/start**

### ⚠️ Senesnių modelių apribojimai

> **ĮSPĖJIMAS**: Senesni modeliai (kurie yra prieš `gpt-4.1`) gali ir nepalaikyti visų Responses API galimų funkcijų pilnai.
>
> Žinomi apribojimai senesniems modeliams:
> - **`reasoning` parametras**: Nepalaikomas daugelyje modelių be reasoning funkcijos. Migruokite `reasoning` tik jei jis jau buvo originaliame kode.
> - **`seed` parametras**: Visiškai nepalaikomas Responses API — pašalinkite iš visų užklausų.
> - **Struktūrizuota išvestis per `text.format`**: Senesni modeliai gali nepaisyti `strict: true` JSON schemų patikimai.
> - **Įrankių valdymas**: GPT-5+ valdo įrankių kvietimus kaip vidinį reasoning procesą. Senesni modeliai Responses API veikia, bet be šios gilios integracijos.
> - **Temperatūros apribojimai**: Migruojant į `gpt-5`, temperatūra turi būti pašalinta arba nustatyta į `1`. Senesni modeliai tokio apribojimo neturi.

### O serijos reasoning modeliai (o1, o3-mini, o3, o4-mini)

O serijos modeliai turi unikalius parametrų apribojimus. Migravimo metu, kai programėlė naudoja o serijos modelius:

- **`temperature`**: privalo būti `1` (arba pašalintas). O serijos modeliai nepriima kitų reikšmių.
- **`max_completion_tokens` → `max_output_tokens`**: Programėlės, naudojančios Azure specifinį `max_completion_tokens`, turi pereiti prie `max_output_tokens`. Nustatykite aukštas vertes (4096+), nes reasoning tokenai skaičiuojami prie limito.
- **`reasoning_effort`**: Jei programėlė naudoja `reasoning_effort` (low/medium/high), laikykite jį — Responses API palaiko šį parametrą o serijos modeliams.
- **Srautinio atsiuntimo elgsena**: O serijos modeliai gali buferizuoti išvestį, kol baigia reasoning, prieš išleidžiant teksto delta įvykius. Srautinio atsiuntimo funkcija veikia, bet pirmasis `response.output_text.delta` gali atvykti vėliau negu GPT modeliams.
- **`top_p`**: Nepalaikomas o serijos modeliuose — pašalinkite jei yra.
- **Įrankių naudojimas**: O serijos modeliai palaiko įrankius per Responses API kaip GPT modeliai, bet įrankių kvietimų koordinavimo kokybė priklauso nuo modelio.

**Veiksmas — proaktyvi modelio konsultacija**: Skenavimo metu patikrinkite, kokį modelį naudoja programėlė (pagal diegimo vardus, aplinkos kintamuosius, konfigūraciją). Jei modelis yra prieš `gpt-4.1` (ne `gpt-4.1+`), informuokite vartotoją:
- Migracija veiks su pagrindiniu tekstu, pokalbiu, srautu ir įrankiais jų dabartiniame modelyje.
- Naujesni modeliai (`gpt-5.1`, `gpt-5.2`) siūlo geresnę įrankių valdymą, struktūrizuotos išvesties užtikrinimą, reasoning ir tarpregioninį prieinamumą.
- Jie turėtų apsvarstyti atnaujinimą kai bus pasiruošę — tai nemato būtinumo migracijai.

Nemeskite ar neatsisakykite migracijos pagal modelio versiją. Konsultacija yra tik informacinė.

### GitHub modeliai nepalaiko Responses API

> **GitHub modeliai (`models.github.ai`, `models.inference.ai.azure.com`) nepalaiko Responses API.**

Jei kodo bazėje yra GitHub modelių kodo kelias (ieškokite `base_url` rodančio į `models.github.ai` ar `models.inference.ai.azure.com`), **visiškai pašalinkite jį migracijos metu**. Responses API reikalauja Azure OpenAI, OpenAI arba suderinamo vietinio endpoint’o (pvz., Ollama su Responses palaikymu).

Veiksmas skenavimo metu:
- Pažymėkite visus GitHub modelių kodo kelius šalinimui.

---

## Framework migracija

Daugelis programėlių naudoja aukštesnio lygio framework'us ant OpenAI. Migracijos metu keičiasi framework'o API — ne tik viduriniojo OpenAI kvietimai.

### Microsoft agentų framework (MAF)

**Pirmiausia patikrinkite MAF versiją** — migracija priklauso nuo to, ar naudojate MAF 1.0.0+ ar ankstesnę beta/rc versiją.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **jau naudoja Responses API** — migracija nereikalinga. Jei kode naudojamas senstelėjęs `OpenAIChatCompletionClient` (naudojantis `chat.completions.create`), pakeiskite į `OpenAIChatClient`.

| Prieš | Po |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Patikrinkite versiją: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF ankstesnės 1.0.0 (beta/rc leidimai)

Ankstesnėje 1.0.0 MAF versijoje, `OpenAIChatClient` naudojo Chat Completions. Atnaujinkite iki `agent-framework-openai>=1.0.0`, kur `OpenAIChatClient` naudoja Responses API pagal numatytuosius nustatymus.

Kitų pakeitimų nereikia — `Agent` ir įrankių API lieka nepakitę.

### LangChain (`langchain-openai`)

Pridėkite `use_responses_api=True` į `ChatOpenAI()`. Taip pat pakeiskite atsakymų prieigą iš `.content` į `.text`.

| Prieš | Po |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Išsamias prieš/po kodo pavyzdžius žr. [cheat-sheet.md](./references/cheat-sheet.md).

---

## Frontendo migracijos gairės

> **Responses API yra serverio pusės klausimas.** Migruokite savo Python backend'ą; frontendo HTTP sutartis turėtų likti nepakitusi, nebent jūsų backend yra plonas praleidimo sluoksnis — tokiu atveju apsvarstykite Responses užklausos formos priėmimą, kad pašalintumėte vertimo sluoksnį. Jei frontend'as kviečia OpenAI tiesiogiai su kliento raktu, perkelkite tuos kvietimus į backend.

### `@microsoft/ai-chat-protocol` pasenimas

`@microsoft/ai-chat-protocol` npm paketas yra pasenęs ir turėtų būti pakeistas į [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Jeigu jį radote fronte:

1. Pakeiskite CDN script tag'ą:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Pašalinkite `AIChatProtocolClient` inicijavimą (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Pakeiskite `client.getStreamedCompletion(messages)` tiesioginiu `fetch()` kvietimu į backend’o srautinio atsiuntimo endpoint’ą.
4. Pakeiskite `for await (const response of result)` į `for await (const chunk of readNDJSONStream(response.body))`.
5. Atnaujinkite prieigą prie savybių iš `response.delta.content` / `response.error` į `chunk.delta.content` / `chunk.error`.

---

## Tikslai

- Išvardinti visas Python kvietimo vietas, naudojančias Chat Completions ar senas Completions Azure OpenAI atžvilgiu.
- Pasiūlyti migracijos planą ir seką Python kodų bazei.
- Atlikti saugius, minimaliai įpareigojančius pataisymus, kad pereitų prie Responses API.
- Atnaujinti kvietikus, kad naudotų Responses išvesties formą; be atgalinio suderinamumo apvalkalų.
- Vykdyti testus/laikymosi taisykles; taisyti smulkius klaidų pažeidimus po migracijos.
- Pasiruošti nedideliems, peržiūrai tinkamiems pakeitimų rinkiniams ir pateikti galutinę santrauką su skirtumais (neįsipareigoti).

---

## Saugančios gairės

- Keisti tik failus, esančius git darbo vietoje. Niekada nerašyti už jos ribų.
- Neišlaikyti atgalinio suderinamumo sluoksnių; migruoti į naują API formą.
- Neperpalikti pereinamojo laikotarpio komentarų ar atsarginių failų.
- Išlaikyti srautinio atsiuntimo semantiką, jei ji buvo naudojama; kitu atveju naudoti nesrautinį variantą.
- Prašyti patvirtinimo prieš vykdant komandų ar tinklo kvietimus, jei patvirtinimo režimas įjungtas.
- Nevykdyti `git add`/`git commit`/`git push`; daryti tik darbo medžio pakeitimus.

---

## 0 veiksmas: Azure OpenAI kliento migracija (priešreikšmė)

Jei kodų bazė naudoja `AzureOpenAI` arba `AsyncAzureOpenAI` konstruktorius, pereikite prie standartinių `OpenAI` / `AsyncOpenAI` konstruktorių pirmiausia. Azure specifiniai konstruktoriai yra nutraukti `openai>=1.108.1`.

### Kodėl v1 API endpoint’as?

Naujas `/openai/v1` endpoint’as naudoja standartinį `OpenAI()` klientą, o ne `AzureOpenAI()`, nereikalauja `api_version` parametro, ir veikia vienodai tiek OpenAI, tiek Azure OpenAI. Tas pats kliento kodas yra ateities patvirtintas — nereikia valdyti versijų.

### Pagrindiniai pakeitimai

| Prieš | Po |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Pašalinti visiškai |

### Išvalymo kontrolinis sąrašas

- Pašalinkite `api_version` argumentą iš kliento konstruktoriaus.
- Pašalinkite `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` aplinkos kintamuosius iš `.env`, programėlės nustatymų ir Bicep/infrastruktūros failų.
- Pervardykite `AZURE_OPENAI_CLIENT_ID` į `AZURE_CLIENT_ID` `.env`, programėlės nustatymuose, Bicep/infrastruktūros ir testavimo įrangoje (standartinė Azure Identity SDK konvencija).
- Užtikrinkite `openai>=1.108.1` `requirements.txt` arba `pyproject.toml`.

### Aplinkos kintamųjų migracija

| Senas env kintamasis | Veiksmas | Pastabos |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Pašalinti** | Nereikia `api_version` su v1 endpoint’u |
| `AZURE_OPENAI_API_VERSION` | **Pašalinti** | Taip pat kaip aukščiau |
| `AZURE_OPENAI_CLIENT_ID` | **Pervadinti** → `AZURE_CLIENT_ID` | Standartinė Azure Identity SDK praktika naudoti `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Palikti** | Reikalingas `base_url` konstravimui |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Palikti** | Naudojamas kaip `model` parametras `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Palikti** | Naudojamas kaip `api_key` raktu pagrįstam autentifikavimui |

Kliento nustatymo kodo pavyzdžius (sinchroninius, asinchroninius, EntraID, API raktą, daugiavartotojiškumą) žr. [cheat-sheet.md](./references/cheat-sheet.md).

---

## 1 veiksmas: Aptikti senus kvietimo taškus

Paleiskite [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) skriptą, kad rastumėte visas kvietimo vietas, kurias reikia migruoti:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Arba atlikite paieškas rankiniu būdu — kiekvienas atitikmuo yra migracijos taikinys:

```bash
# Senoji API kvietimai (būtina perrašyti)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Nebenaudojami Azure kliento konstruktoriai (būtina pakeisti)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Atsakymo struktūros prieigos modeliai (būtina atnaujinti)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Įrankių aprašymai senojoje įdėtoje formoje (būtina supaprastinti)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Įrankių rezultatai senojoje formoje (būtina konvertuoti į function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Nebenaudojami parametrai (būtina pašalinti arba pervardyti)
rg "response_format"
rg "max_tokens\b"        # pervardyti į max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Nebenaudojami aplinkos kintamieji (išvalyti)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # turėtų būti AZURE_CLIENT_ID

# GitHub Modelių galiniai taškai (būtina pašalinti — Responses API nepalaikoma)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Framwork'o lygmens seni modeliai (būtina atnaujinti)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: pakeisti į OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: reikia use_responses_api=True

# Testavimo infrastruktūra (būtina atnaujinti)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Turinį filtruojančios klaidos informacijos prieiga (būtina atnaujinti — struktūra pasikeitė)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # sena vienaskaita forma — dabar content_filter_results (daugiskaita) viduje content_filters masyvo

# Raw HTTP kvietimai į Chat Completions galinį tašką (būtina atnaujinti URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristika (aptikti ir perrašyti)

- **Chat Completions klientas**: `client.chat.completions.create` → `client.responses.create(...)`.

- **„Azure“ kliento konstruktoriai**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Įrankiai**: konvertuoti funkcijų kvietimo įrankių apibrėžimus iš įdėto formato (`{"type": "function", "function": {"name": ...}}`) į plokščią Responses formatą (`{"type": "function", "name": ...}`); naudoti `tool_choice`; grąžinti įrankio rezultatus kaip `{"type": "function_call_output", "call_id": ..., "output": ...}` elementus (ne `{"role": "tool", ...}`).
- **Įrankių grąžinimai**: kai modelis grąžina funkcijų kvietimus, pridėti `response.output` elementus prie pokalbio (ne rankinį `{"role": "assistant", "tool_calls": [...]}` žodyną), tada pridėti `function_call_output` elementus kiekvienam rezultatui.
- **Keletas pavyzdžių su įrankiais**: jei pokalbyje yra standžiai įrašyti įrankių kvietimų pavyzdžiai, konvertuoti juos į `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` elementus. ID turi prasidėti nuo `fc_`.
- **`pydantic_function_tool()`**: šis pagalbinis įrankis vis dar generuoja seną įdėtą formatą ir **nėra suderinamas** su `responses.create()`. Pakeisti rankiniais įrankių apibrėžimais arba naudojant apvalkalą, kuris supločia formatą.
- **Daugiatūris**: išlaikyti pokalbio istoriją programėlėje; perduoti ankstesnius ėjimus per `input` elementus.
- **Formatavimas**: pakeisti Chat viršutinio lygio `response_format` į `text.format` Responses. Kanoninė forma: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Turinio elementai**: pakeisti Chat `content[].type: "text"` į Responses `content[].type: "input_text"` vartotojo/sistemos ėjimams.
- **Vaizdo turinio elementai**: pakeisti Chat `content[].type: "image_url"` į Responses `content[].type: "input_image"`. Laukas `image_url` keičiasi iš įdėto objekto `{"url": "..."}` į plokščią eilutę. Žr. iš anksto/po to pavyzdžius cheat lape.
- **Mąstymo pastangos**: **migracija atliekama tik jei `reasoning` jau egzistuoja pradiniame kode**.
- **Turinio filtro klaidų apdorojimas**: klaidos objekto struktūra pasikeitė. Chat Completions naudojo `error.body["innererror"]["content_filter_result"]` (vienaskaita); Responses API naudoja `error.body["content_filters"][0]["content_filter_results"]` (daugiskaita, masyvo viduje). Kodo, kuris prieina prie `innererror`, bus metama `KeyError`. Perrašyti naudoti naują kelią.
- **Žemi HTTP kvietimai**: jei programėlė kviečia Azure OpenAI REST API tiesiogiai (per `requests`, `httpx` ir pan.) naudodama `/openai/deployments/{name}/chat/completions?api-version=...`, perrašyti į `/openai/v1/responses`. Užklausos kūnas keičiasi: `messages` → `input`, pridėti `max_output_tokens` ir `store: false`, pašalinti `api-version` užklausos parametrą. Atsakymo kūnas keičiasi: `choices[0].message.content` → `output[0].content[0].text` (pastaba: `output_text` yra SDK patogumo savybė, kurios nėra žaliame REST JSON).

---

## 2 veiksmas: pritaikyti migraciją

### Migracijos pastabos (Chat Completions → Responses)

- **Kodėl migruoti**: Responses yra vieningas API tekstui, įrankiams ir srautiniam perdavimui; Chat Completions yra legacy. Su GPT-5 Responses reikalingas geriausiems rezultatams.
- **HTTP**: Azure galinis taškas keičiasi iš `/openai/deployments/{name}/chat/completions` į `/openai/v1/responses`.
- **Laukai**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` nesikeičia.
- **Formatavimas**: `response_format` → `text.format` su tinkamu objektu.
- **Turinio elementai**: Pakeisti Chat `content[].type: "text"` į Responses `content[].type: "input_text"` sistemos/vartotojo ėjimams.
- **Vaizdo turinio elementai**: Pakeisti Chat `content[].type: "image_url"` į Responses `content[].type: "input_image"`. Supaprastinti `image_url` lauką iš `{"image_url": {"url": "..."}}` į `{"image_url": "..."}` (paprasta eilutė — HTTPS URL arba `data:image/...;base64,...` duomenų URI).

### Parametrų atitikmenų nuoroda

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (elementų masyvas) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objektas) |
| `temperature` | `temperature` (nepasikeitė) |
| `stop` | `stop` (nepasikeitė) |
| `frequency_penalty` | `frequency_penalty` (nepasikeitė) |
| `presence_penalty` | `presence_penalty` (nepasikeitė) |
| `tools` / funkcijų kvietimas | `tools` (nepasikeitė) |
| `seed` | **Pašalinti** (nepalaikoma) |
| `store` | `store` (nustatyta į `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (plokšti tekstas) |

Kompletiškus prieš/po kodo pavyzdžius žr. [cheat-sheet.md](./references/cheat-sheet.md).

Testavimo infrastruktūros migracijai (mock'ai, snapshoot'ai, patikrinimai) žr. [test-migration.md](./references/test-migration.md).

Problemų sprendimui ir klaidų identifikavimui žr. [troubleshooting.md](./references/troubleshooting.md).

---

## Duomenų išlaikymas ir būsena

- Nustatyti `store: false` visuose Responses užklausose.
- Nesikliauti ankstesnių žinučių ID ar serveryje saugomu kontekstu; valdyti būseną kliento pusėje ir minimalizuoti metaduomenis.

---

## Priėmimo kriterijai

### Kodo lygmens vartai (visi turi būti įvykdyti)

- [ ] Migravus failuose nerasti jokių atitikmenų `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"`.
- [ ] Nerasti jokių atitikmenų `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — visi konstruktoriai naudoja `OpenAI`/`AsyncOpenAI` su v1 galu.
- [ ] Nerasti jokių atitikmenų `rg "models\.github\.ai|models\.inference\.ai\.azure"` — pašalinti GitHub modelių kodo takai.
- [ ] Nerasti jokių atitikmenų `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ kodas naudoja `OpenAIChatClient` (kuris naudoja Responses API). Iki 1.0.0 versijos atnaujinti į `agent-framework-openai>=1.0.0`.
- [ ] Visi `ChatOpenAI(...)` kvietimai turi `use_responses_api=True`.
- [ ] Nerasti jokių atitikmenų `rg "choices\[0\]"` — visa atsakymų prieiga naudoja `resp.output_text` arba Responses išvesties schemą.
- [ ] Viršutiniame lygyje nėra `response_format`; visas struktūruotas išvestis naudoja `text={"format": {...}}`.
- [ ] `openai>=1.108.1` ir `azure-identity` yra `requirements.txt` arba `pyproject.toml`; priklausomybės persiųstos.
- [ ] Visuose kvietimuose `responses.create` nustatytas `store=False`.
- [ ] Nėra `api_version` kliento konstravime; `AZURE_OPENAI_API_VERSION` pašalintas iš aplinkos failų ir infrastruktūros.

### Testavimo infrastruktūros vartai (visi turi būti įvykdyti)

- [ ] Nerasti jokių atitikmenų `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Nerasti jokių atitikmenų `rg "_azure_ad_token_provider" tests/` — patikrinimai atnaujinti tikrinti `isinstance(client, AsyncOpenAI)` arba `base_url`.
- [ ] Nerasti jokių atitikmenų `rg "prompt_filter_results|content_filter_results" tests/` — pašalinti Azure specifiniai filtrų mock'ai.
- [ ] Mock objektai naudoja `kwargs.get("input")` ne `kwargs.get("messages")`.
- [ ] Snapsot / auksiniai failai atnaujinti į Responses srautinio formato formą (be `choices[0]`, `function_call`, `logprobs` ir t.t.).
- [ ] `pytest` vyksta be klaidų po visų testų atnaujinimų.

### Elgesio vartai (patikrinti rankiniu būdu arba per testų aplinką)

- [ ] **Pagrindinė baigtis**: ne srautiniai `responses.create` gražina neužpildytą `output_text`.
- [ ] **Srauto paritetas**: jei pradiniame kode buvo naudojamas srautas, migravus kodas srautuoja ir išskiria `response.output_text.delta` įvykius su neužpildytais delta duomenimis.
- [ ] **Struktūruotas išvestis**: jei naudojamas `text.format` su `json_schema`, `json.loads(resp.output_text)` sėkmingas ir atitinka schemą.
- [ ] **Įrankių kvietimo ciklas**: jei naudojami įrankiai, modelis vykdo įrankių kvietimus, programėlė juos vykdo, o tolesnis užklausimas grąžina galutinį `output_text` (be begalinio ciklo).
- [ ] **Asinchroninis paritetas**: jei naudotas `AsyncAzureOpenAI`, lygiavertis `AsyncOpenAI` veikia su `await`.
- [ ] **Klaidų lygis**: nėra naujų 400/401/404 klaidų, palyginus su pradinės bazės linijos būkle.

### Griežtiniai

- Santrauka apima redaguotus failus, prieš/po senųjų kvietimų vietų skaičius ir tolesnius žingsnius.
- Pokyčiai yra tik darbo kopijos pakeitimai (nereikia komitų).

---

## SDK versijų reikalavimai

| Paketas | Minimalios versijos |
|---------|------------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Naujausia (EntraID autentifikacijai) |

---

## Nuorodos

- [Santraukos lapas — visi kodo pavyzdžiai](./references/cheat-sheet.md)
- [Testavimo migracija — mock'ai, snapshoot'ai, patikrinimai](./references/test-migration.md)
- [Problemų sprendimas — klaidos, rizikos lentelė, spąstai](./references/troubleshooting.md)
- [detect_legacy.py — automatinis skeneris](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI pradžios rinkinys](https://aka.ms/openai/start)
- [Azure OpenAI Responses API dokumentacija](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API versijos gyvavimo ciklas](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API nuoroda](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->