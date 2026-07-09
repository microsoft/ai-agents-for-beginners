---
name: azure-openai-to-responses
license: MIT
---
# Perkelkite Python programas iš Azure OpenAI pokalbių pabaigų į Responses API

> **OFICIALIOS NURODYMAS — VYKDYKITE TIKSLIAI**
>
> Šis įgūdis perkelia Python kodo bazes, naudodamas Azure OpenAI pokalbių pabaigas
> į vieningą Responses API. Laikykitės šių nurodymų tiksliai.
> Neeksperimentuokite su parametro priskyrimu ar API formų kūrimu.

---

## Aktivatoriai

Aktyvinkite šį įgūdį, kai vartotojas nori:
- Perkelti Python programą iš Azure OpenAI pokalbių pabaigų į Responses API
- Atnaujinti Python OpenAI SDK naudojimą į naujausią API formą Azure OpenAI aplinkoje
- Paruošti Python kodą GPT-5 ar naujesniems modeliams, kuriems reikalingas Responses Azure
- Pereiti nuo `AzureOpenAI`/`AsyncAzureOpenAI` prie standartinio `OpenAI`/`AsyncOpenAI` kliento su v1 galiniu tašku
- Ištaisyti pasenimo įspėjimus, susijusius su `AzureOpenAI` konstruktoriais arba `api_version`

---

## ⚠️ Modelio suderinamumas — PATIKRINKITE PIRMIAUSIAI

> **Prieš migraciją įsitikinkite, kad jūsų Azure OpenAI diegimas palaiko Responses API.**

### 1. Patikrinkite diegimą (greičiausias būdas)

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

> **Pastaba**: `max_output_tokens` Azure OpenAI turi **mažiausią ribą 16**. Vertės žemiau 16 grąžina 400 klaidą. Naudokite 50+ bandymams.

Jei tai grąžina 404, modelis diegime dar nepalaiko Responses — patikrinkite žemiau esančią nuorodą arba perdiegiant naudokite palaikomą modelį.

### 2. Patikrinkite regionui prieinamus modelius (rekomenduojama)

Paleiskite įmontuotą modelių suderinamumo įrankį, kad pamatytumėte, kas yra su Responses API palaikymu jūsų regione:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Tai užklausia tiesiogiai Azure ARM ir rodo suderinamumo matricą — kurie modeliai palaiko Responses, struktūrizuotą išvestį, įrankius ir pan. Naudokite `--filter gpt-5.1,gpt-5.2` rezultatų siaurinimui arba `--json` skriptavimui.

### 3. Pilnas modelių palaikymo šaltinis

- **Gyva užklausa**: `python migrate.py models` (žr. aukščiau — regionui specifinė, visada atnaujinta)
- **Naršymas**: [Modelių santraukos lentelė ir regiono prieinamumas](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Greitas pradžios vadovas & gairės**: **https://aka.ms/openai/start**

### ⚠️ Senesnių modelių apribojimai

> **ĮSPĖJIMAS**: Senesni modeliai (pvz., `gpt-4o`, `gpt-4`) gali nepalaikyti visų Responses API funkcijų pilnai.
>
> Žinomi senų modelių apribojimai:
> - **`reasoning` parametras**: Nepalaikomas `gpt-4o-mini`, `gpt-4o` ir daugelyje modelių be reasoning. Migracijai įtraukite `reasoning` tik jei jis jau buvo originaliame kode.
> - **`seed` parametras**: Visai nepalaikomas Responses API — pašalinkite iš visų užklausų.
> - **Struktūruota išvestis per `text.format`**: Senesni modeliai gali patikimai nenaudoti `strict: true` JSON schemų.
> - **Įrankių orkestracija**: GPT-5+ orkestruoja įrankių iškvietimus kaip vidinį reasoning etapą. Senesni modeliai Responses API veikia, bet neturi šios gilesnės integracijos.
> - **Temperatūros apribojimai**: Migruojant į `gpt-5`, temperatūra turi būti praleista arba nustatyta į `1`. Senesniems modeliams tokio apribojimo nėra.

### O serijos reasoning modeliai (o1, o3-mini, o3, o4-mini)

O serijos modeliai turi unikalius parametro apribojimus. Migruojant programas, taikančias o serijos modelius:

- **`temperature`**: Turi būti `1` (arba praleista). O serijos modeliai nepriima kitų reikšmių.
- **`max_completion_tokens` → `max_output_tokens`**: Programos, naudodamos Azure specifinį `max_completion_tokens`, turi pereiti prie `max_output_tokens`. Nustatykite aukštas reikšmes (4096+), nes reasoning tokenai skaičiuojami į ribą.
- **`reasoning_effort`**: Jei programa naudoja `reasoning_effort` (low/medium/high), palikite — Responses API palaiko šį parametrą o serijos modeliams.
- **Srautinis perdavimas**: O serijos modeliai gali rezervuoti išvestį iki reasoning pabaigos prieš siunčiant teksto delta įvykius. Srautinės funkcijos veikia, bet pirmasis `response.output_text.delta` gali atvykti vėliau nei GPT modelių atveju.
- **`top_p`**: Nepalaikomas o serijos modeliuose — pašalinkite jei yra.
- **Įrankių naudojimas**: O serijos modeliai palaiko įrankius per Responses API kaip ir GPT modeliai, bet įrankių iškvietimo orkestracijos kokybė priklauso nuo modelio.

**Veiksmas — proaktyvus modelio įspėjimas**: Skenavimo metu patikrinkite, kokį modelį programa naudoja (diegimo pavadinimai, aplinkos kintamieji, konfigūracija). Jei modelis yra `gpt-4o` arba senesnis (ne gpt-4.1+), informuokite vartotoją:
- Migracija veiks pagrindiniam tekstui, pokalbiams, srautiniam perdavimui ir įrankiams jų dabartiniame modelyje.
- Naujesni modeliai (`gpt-5.1`, `gpt-5.2`) siūlo geresnę įrankių orkestraciją, struktūruotą išvesties privalomumą, reasoning ir tarpregioninį pasiekiamumą.
- Jie turėtų apsvarstyti savo diegimo atnaujinimą, kai bus pasiruošę — tai netrukdo migracijai.

Nemeskite ir neleiskite atlikti migracijos dėl modelio versijos. Šis pranešimas yra informacinio pobūdžio.

### GitHub modeliai nepalaiko Responses API

> **GitHub modeliai (`models.github.ai`, `models.inference.ai.azure.com`) nepalaiko Responses API.**

Jei kodo bazėje yra GitHub modelių kodo kelias (ieškokite `base_url`, nukreipiančio į `models.github.ai` arba `models.inference.ai.azure.com`), **visiškai jį pašalinkite** migracijos metu. Responses API reikalauja Azure OpenAI, OpenAI arba suderinamo vietinio galo taško (pvz., Ollama su Responses palaikymu).

Veiksmai skenavimo metu:
- Pažymėkite bet kokius GitHub modelių kodo kelius pašalinimui.

---

## Framework migracija

Daugelis programų naudoja aukštesnio lygio karkasus ant viršaus OpenAI. Migracijos metu keičiasi ne tik pagrindiniai OpenAI kvietimai, bet ir pats karkaso API.

### Microsoft Agent Framework (MAF)

**Pirmiausia patikrinkite savo MAF versiją** — migracija priklauso nuo to, ar naudojate MAF 1.0.0+ ar ankstesnę beta/rc versiją.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **jau naudoja Responses API** — migracija nereikalinga. Jei kodo bazėje naudojate seną `OpenAIChatCompletionClient` (naudojantį `chat.completions.create`), pakeiskite jį į `OpenAIChatClient`.

| Prieš | Po |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Norėdami patikrinti versiją: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF prieš 1.0.0 (beta/rc versijos)

Ankstesnėse MAF versijose `OpenAIChatClient` naudojo Chat Completions. Atnaujinkite į `agent-framework-openai>=1.0.0`, kur `OpenAIChatClient` pagal nutylėjimą naudoja Responses API.

Kitos pakeitimų nereikia — `Agent` ir įrankių API lieka tokie patys.

### LangChain (`langchain-openai`)

Pridėkite `use_responses_api=True` prie `ChatOpenAI()`. Taip pat atnaujinkite atsakymo prieigą nuo `.content` į `.text`.

| Prieš | Po |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Pilnus prieš/po kodo pavyzdžius žr. [cheat-sheet.md](./references/cheat-sheet.md).

---

## Priekinės dalies migracijos gairės

> **Responses API yra serverio pusės reikalas.** Perkelkite savo Python backendą; priekinės dalies HTTP sutartis turėtų likti nepakitusi, nebent jūsų backend yra plonas tarpinis sluoksnis — tokiu atveju apsvarstykite Responses užklausos formą, kad pašalintumėte vertimo sluoksnį. Jei priekinė dalis tiesiogiai kviečia OpenAI su kliento pusės raktu, pirmiausia perkelkite tuos kvietimus į backendą.

### `@microsoft/ai-chat-protocol` pasenimas

`@microsoft/ai-chat-protocol` npm paketas yra pasenęs ir turėtų būti pakeistas [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Jei tai randate priekinėje dalyje:

1. Pakeiskite CDN skripto žymę:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Pašalinkite `AIChatProtocolClient` inicializavimą (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Pakeiskite `client.getStreamedCompletion(messages)` tiesioginiu `fetch()` kvietimu backend srautiniam galiniam taškui.
4. Pakeiskite `for await (const response of result)` į `for await (const chunk of readNDJSONStream(response.body))`.
5. Atnaujinkite prieigą prie savybių nuo `response.delta.content` / `response.error` į `chunk.delta.content` / `chunk.error`.

---

## Tikslai

- Surasti visus Python iškvietimus, naudojančius Chat Completions arba senąsias Completions Azure OpenAI atveju.
- Pasiūlyti migracijos planą ir seką Python kodo bazei.
- Taikyti saugius, minimalius pakeitimus pereinant prie Responses API.
- Atnaujinti kvietėjus naudoti Responses išvesties schemą; be atgalinio suderinamumo įvorių.
- Paleisti testus/linterius; ištaisyti smulkias klaidas, atsiradusias migracijos metu.
- Paruošti mažus, apžvelgiamus pakeitimų rinkinius ir pateikti galutinę ataskaitą su skirtumais (neįsipareigokite commitinti).

---

## Saugikliai

- Keisti tik failus, esančius git darbo aplinkoje. Niekada nerašyti už jos ribų.
- Išmesti atgalinio suderinamumo adapterius; perkelti kodą į naują API formą.
- Neleisti palikti mirusių komentarų ar atsarginių failų.
- Išlaikyti srautinio perdavimo semantiką, jei buvo naudojama; kitu atveju naudoti nesrautinį perdavimą.
- Prašyti patvirtinimo prieš vykdant komandas ar tinklo kvietimus, jei yra patvirtinimo režimas.
- Nevykdyti `git add`/`git commit`/`git push`; generuoti tik darbo srities pakeitimus.

---

## Žingsnis 0: Azure OpenAI kliento migracija (prieš sąlygą)

Jei kodo bazėje naudojami `AzureOpenAI` arba `AsyncAzureOpenAI` konstruktoriai, pereikite prie standartinių `OpenAI` / `AsyncOpenAI` konstruktorių pirmiausia. Azure specifiniai konstruktoriai yra pasenę `openai>=1.108.1`.

### Kodėl v1 API kelias?

Naujas `/openai/v1` galinis taškas naudoja standartinį `OpenAI()` klientą, o ne `AzureOpenAI()`, nereikalauja `api_version` parametro, ir veikia identiškai tiek OpenAI, tiek Azure OpenAI. Tas pats kliento kodas yra ateičiai pritaikytas — nereikia versijų valdymo.

### Pagrindiniai pakeitimai

| Prieš | Po |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Pašalinti visiškai |

### Švarinimo kontrolinis sąrašas

- Pašalinti `api_version` argumentą iš kliento konstruktoriaus.
- Pašalinti `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` aplinkos kintamuosius iš `.env`, app nustatymų ir Bicep/infra failų.
- Pervardyti `AZURE_OPENAI_CLIENT_ID` į `AZURE_CLIENT_ID` `.env`, app nustatymuose, Bicep/infra ir testų šablonuose (standartinė Azure Identity SDK konvencija).
- Užtikrinti `openai>=1.108.1` `requirements.txt` ar `pyproject.toml`.

### Aplinkos kintamųjų migracija

| Senas aplinkos kintamasis | Veiksmas | Pastabos |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Pašalinti** | V1 gale nereikia `api_version` |
| `AZURE_OPENAI_API_VERSION` | **Pašalinti** | Tas pats kaip aukščiau |
| `AZURE_OPENAI_CLIENT_ID` | **Pervardyti** → `AZURE_CLIENT_ID` | Standartinė Azure Identity SDK konvencija `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Išlaikyti** | Reikalinga `base_url` sudarymui |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Išlaikyti** | Naudojama kaip `model` parametras `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Išlaikyti** | Naudojama kaip `api_key` autentifikacijai su raktu |

Kliento setup kodo pavyzdžiams (sinchroninis, asinchroninis, EntraID, API raktas, multi-tenant) žr. [cheat-sheet.md](./references/cheat-sheet.md).

---

## Žingsnis 1: Aptikti senus iškvietimo taškus

Paleiskite [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) skriptą, kad rastumėte visus iškvietimo taškus, kurie reikalauja migracijos:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Arba atlikite šiuos paieškas rankiniu būdu — kiekvienas sutapimas yra migracijos tikslas:

```bash
# Senos API užklausos (reikia perrašyti)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Nebenaudojami Azure kliento konstruktoriai (reikia pakeisti)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Atsakymų struktūros prieigos šablonai (reikia atnaujinti)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Įrankių apibrėžimai sename įdėtame formate (reikia supaprastinti)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Įrankių rezultatai sename formate (reikia konvertuoti į function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Nebenaudojami parametrai (reikia pašalinti arba pervardyti)
rg "response_format"
rg "max_tokens\b"        # pervardyti į max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Nebenaudojami aplinkos kintamieji (reikia sutvarkyti)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # turėtų būti AZURE_CLIENT_ID

# GitHub modelių galiniai taškai (reikia pašalinti — Responses API nepalaikomas)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Korpusų lygmens senosios schemos (reikia atnaujinti)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: pakeisti į OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: reikia use_responses_api=True

# Testavimo infrastruktūra (reikia atnaujinti)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Turinio filtro klaidos kūno prieiga (reikia atnaujinti — struktūra pasikeitė)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # senas vienaskaitos formatas — dabar content_filter_results (daugiskaita) esančios content_filters masyve

# Žaliavinių HTTP užklausų siuntimas Chat Completions galiniam taškui (reikia atnaujinti URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristika (identifikuoti ir perrašyti)

- **Chat Completions klientas**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure kliento konstruktoriai**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Įrankiai**: konvertuoti funkcijų kvietimų įrankių apibrėžimus iš įdėto formato (`{"type": "function", "function": {"name": ...}}`) į plokščią Responses formatą (`{"type": "function", "name": ...}`); naudoti `tool_choice`; grąžinti įrankio rezultatus kaip `{"type": "function_call_output", "call_id": ..., "output": ...}` elementus (ne `{"role": "tool", ...}`).
- **Įrankių apdorojimas pirmyn-atgal**: kai modelis grąžina funkcijų kvietimus, pridėti `response.output` elementus prie pokalbio (ne rankiniu būdu `{"role": "assistant", "tool_calls": [...]}` žodyno), tuomet pridėti `function_call_output` elementus kiekvienam rezultatui.
- **Keletas pavyzdžių su įrankiais**: jei pokalbyje yra įkoduoti įrankių kvietimų pavyzdžiai, konvertuoti juos į `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` elementus. ID turi prasidėti `fc_`.
- **`pydantic_function_tool()`**: šis pagalbinis vis dar generuoja seną įdėtą formatą ir **nėra suderinamas** su `responses.create()`. Pakeisti rankiniais įrankių apibrėžimais arba suapvalinančiu wrapperiu.
- **Daugiaturnis**: palaikyti pokalbio istoriją programoje; prieš tai buvusius turus perduoti per `input` elementus.
- **Formatavimas**: pakeisti Chat aukščiausio lygio `response_format` su `text.format` Responses. Kanoninė forma: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Turinio elementai**: pakeisti Chat `content[].type: "text"` į Responses `content[].type: "input_text"` vartotojo/sistemos turams.
- **Vaizdo turinio elementai**: pakeisti Chat `content[].type: "image_url"` į Responses `content[].type: "input_image"`. Laukas `image_url` keičiasi iš įdėto objekto `{"url": "..."}` į plokščią tekstą. Žr. cheato lapą dėl prieš ir po pavyzdžių.
- **Loginis atsakingumas**: **atidžiai migruoti `reasoning`, jei jis jau egzistuoja originaliame kode**.
- **Turinio filtro klaidų tvarkymas**: klaidų struktūra pasikeitė. Chat Completions naudojo `error.body["innererror"]["content_filter_result"]` (vienaskaita); Responses API naudoja `error.body["content_filters"][0]["content_filter_results"]` (daugiskaita, masyvo viduje). Kodas, kuris kreipiasi į `innererror` kels `KeyError`. Pervadinti naudoti naują kelią.
- **RAW HTTP kvietimai**: jei programa tiesiogiai kviečia Azure OpenAI REST API (per `requests`, `httpx` ir kt.) naudodama `/openai/deployments/{name}/chat/completions?api-version=...`, perrašyti į `/openai/v1/responses`. Užklausos kūnas keičiasi: `messages` → `input`, pridedama `max_output_tokens` ir `store: false`, pašalinamas `api-version` užklausos parametras. Atsakymo kūnas keičiasi: `choices[0].message.content` → `output[0].content[0].text` (pastaba: `output_text` yra SDK patogumo savybė, kurios nėra žaliame REST JSON).

---

## 2 žingsnis: Taikyti migraciją

### Migracijos pastabos (Chat Completions → Responses)

- **Kodėl migracija**: Responses yra vieningas API tekstui, įrankiams ir srautiniam duomenų pateikimui; Chat Completions yra paveldėtas. Su GPT-5, Responses būtinas geriausiam veikimui.
- **HTTP**: Azure galinis taškas keičiasi iš `/openai/deployments/{name}/chat/completions` į `/openai/v1/responses`.
- **Laukai**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` lieka.
- **Formatavimas**: `response_format` → `text.format` su tinkamu objektu.
- **Turinio elementai**: pakeisti Chat `content[].type: "text"` į Responses `content[].type: "input_text"` sisteminių/vartotojo turų atvejais.
- **Vaizdo turinio elementai**: pakeisti Chat `content[].type: "image_url"` į Responses `content[].type: "input_image"`. Išplokštinti `image_url` lauką iš `{"image_url": {"url": "..."}}` į `{"image_url": "..."}` (paprastas tekstas — HTTPS URL arba `data:image/...;base64,...` duomenų URI).

### Parametrų atitikčių žemėlapis

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (elementų masyvas) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objektas) |
| `temperature` | `temperature` (be pakitimų) |
| `stop` | `stop` (be pakitimų) |
| `frequency_penalty` | `frequency_penalty` (be pakitimų) |
| `presence_penalty` | `presence_penalty` (be pakitimų) |
| `tools` / funkcijų kvietimai | `tools` (nepakitę) |
| `seed` | **Pašalinti** (nėra palaikymo) |
| `store` | `store` (nustatyta į `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (plokščias tekstas) |

Pilnai priekinio ir užpakalinio kodo pavyzdžiams žr. [cheat-sheet.md](./references/cheat-sheet.md).

Testavimo infrastruktūros migracijai (mimikos, momentinės nuotraukos, patikrinimai) žr. [test-migration.md](./references/test-migration.md).

Klaidų ir painiavos sprendimams žr. [troubleshooting.md](./references/troubleshooting.md).

---

## Duomenų saugojimas ir būsena

- Nustatyti `store: false` kiekvienam Responses užklausos kvietimui.
- Nesikliauti ankstesniais pranešimų ID ar serveryje saugoma konteksto informacija; palaikyti būseną klientui valdomą ir minimalizuoti meta duomenis.

---

## Priėmimo kriterijai

### Kodo lygmens kontrolės (visos turi būti įvykdytos)

- [ ] Nėra atitikmenų `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` migravimuose failuose.
- [ ] Nėra atitikmenų `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — visi konstruktoriai naudoja `OpenAI`/`AsyncOpenAI` su v1 galiniu tašku.
- [ ] Nėra atitikmenų `rg "models\.github\.ai|models\.inference\.ai\.azure"` — pašalintos GitHub modelių kodo dalys.
- [ ] Nėra atitikmenų `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ naudoja `OpenAIChatClient` (kuris naudoja Responses API). Prieš 1.0.0, pakelti versiją į `agent-framework-openai>=1.0.0`.
- [ ] Visi `ChatOpenAI(...)` kvietimai turi `use_responses_api=True`.
- [ ] Nėra atitikmenų `rg "choices\[0\]"` — visas atsakymas gauna `resp.output_text` arba naudoja Responses išvesties schemą.
- [ ] Nėra `response_format` aukščiausiame lygyje; visa struktūruota išvestis naudoja `text={"format": {...}}`.
- [ ] `openai>=1.108.1` ir `azure-identity` yra `requirements.txt` arba `pyproject.toml`; priklausomybės perinstaliuotos.
- [ ] Kiekviename `responses.create` kvietime nustatyta `store=False`.
- [ ] Nėra `api_version` kliento konstravimo metu; `AZURE_OPENAI_API_VERSION` pašalintas iš aplinkos failų ir infrastruktūros.

### Testavimo infrastruktūros kontrolės (visos turi būti įvykdytos)

- [ ] Nėra atitikmenų `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Nėra atitikmenų `rg "_azure_ad_token_provider" tests/` — patikrinimai atnaujinti tikrinti `isinstance(client, AsyncOpenAI)` arba `base_url`.
- [ ] Nėra atitikmenų `rg "prompt_filter_results|content_filter_results" tests/` — pašalinti Azure specifiški filtro mimikos.
- [ ] Mimikos naudoja `kwargs.get("input")`, o ne `kwargs.get("messages")`.
- [ ] Momentinių nuotraukų / golden failai atnaujinti į Responses srautinio formato struktūrą (nėra `choices[0]`, `function_call`, `logprobs` ir pan.).
- [ ] `pytest` sėkmingai praeina be klaidų po visų testų atnaujinimų.

### Elgsenos patikros (tikrinti rankiniu būdu arba per testo sistemą)

- [ ] **Pagrindinis atsakymas**: ne srautinės `responses.create` kvietimas grąžina ne tuščią `output_text`.
- [ ] **Srautinio srauto atitikimas**: jei originalus kodas naudojo srautą, migravę duoda srautą ir grąžina `response.output_text.delta` įvykius su ne tuščiais delta duomenimis.
- [ ] **Struktūruota išvestis**: jei naudojama `text.format` su `json_schema`, `json.loads(resp.output_text)` nepakyla klaidos ir atitinka schemą.
- [ ] **Įrankių kvietimo ciklas**: jei naudojami įrankiai, modelis siunčia įrankių kvietimus, programa juos vykdo, ir sekanti užklausa grąžina galutinį `output_text` (be begalinių ciklų).
- [ ] **Async atitikimas**: jei naudotas `AsyncAzureOpenAI`, tinkamas `AsyncOpenAI` veikia su `await`.
- [ ] **Klaidų lygis**: nėra naujų 400/401/404 klaidų lyginant su prieš migraciją.

### Pateikimai

- Santrauka apima pakeistus failus, senų kvietimų prieš/po skaičių, ir tolesnius žingsnius.
- Pokyčiai tik darbo kataloge (be įsipareigojimų).

---

## SDK versijos reikalavimai

| Paketas | Minimalios versijos |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Naujausia (EntraID autentifikavimui) |

---

## Nuorodos

- [Greito naudojimo lapas — visi kodo fragmentai](./references/cheat-sheet.md)
- [Testavimo migracija — mimikos, momentinės nuotraukos, patikrinimai](./references/test-migration.md)
- [Klaidų sprendimas — klaidos, rizikų lentelė, painiavos](./references/troubleshooting.md)
- [detect_legacy.py — automatizuotas skeneris](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI pradžios rinkinys](https://aka.ms/openai/start)
- [Azure OpenAI Responses API dokumentacija](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API versijos gyvavimo ciklas](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API referencija](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->