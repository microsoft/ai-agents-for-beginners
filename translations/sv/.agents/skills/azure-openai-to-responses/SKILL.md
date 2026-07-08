---
name: azure-openai-to-responses
license: MIT
---
# Migrera Python-appar från Azure OpenAI Chat Completions till Responses API

> **AUTORITATIV VÄGLEDNING — FÖLJ EXAKT**
>
> Denna skill migrerar Python-kodbaser som använder Azure OpenAI Chat Completions
> till det enhetliga Responses API. Följ dessa instruktioner noggrant.
> Improvisera inte med parameterkartläggningar och uppfinn inte API-strukturer.

---

## Utlösare

Aktivera denna skill när användaren vill:
- Migrera en Python-app från Azure OpenAI Chat Completions till Responses API
- Uppgradera användningen av Python OpenAI SDK till den senaste API-strukturen mot Azure OpenAI
- Förbereda Python-kod för GPT-5 eller nyare modeller som kräver Responses på Azure
- Byta från `AzureOpenAI`/`AsyncAzureOpenAI` till standard `OpenAI`/`AsyncOpenAI` klient med v1-endpoint
- Fixa avskrivningsvarningar relaterade till `AzureOpenAI`-konstruktörer eller `api_version`

---

## ⚠️ Kompatibilitet med modell — KONTROLLERA FÖRST

> **Innan migrering, verifiera att din Azure OpenAI-distribution stöder Responses API.**

### 1. Röktest av distributionen (snabbast)

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

> **Notera**: `max_output_tokens` har ett **minimum på 16** på Azure OpenAI. Värden under 16 ger fel 400. Använd 50+ för röktester.

Om detta returnerar 404 så stöder inte distributionens modell Responses ännu — kontrollera referensen nedan eller distribuera om med en stödd modell.

### 2. Kontrollera tillgängliga modeller i din region (rekommenderat)

Kör det inbyggda verktyget för modellkompatibilitet för att se vad som finns tillgängligt med stöd för Responses API i din specifika region:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Det här frågar Azure ARM live och visar en kompatibilitetsmatris — vilka modeller som stödjer Responses, strukturerad output, verktyg etc. Använd `--filter gpt-5.1,gpt-5.2` för att begränsa resultat eller `--json` för skriptning.

### 3. Full referens för modellstöd

- **Live-fråga**: `python migrate.py models` (se ovan — regionspecifik, alltid uppdaterad)
- **Bläddra tillgänglighet**: [Modellsammanfattningstabell och regionsstöd](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Snabbstart & vägledning**: **https://aka.ms/openai/start**

### ⚠️ Begränsningar för äldre modeller

> **VARNING**: Äldre modeller (t.ex. `gpt-4o`, `gpt-4`) kan ha ofullständigt stöd för alla Responses API-funktioner.
>
> Kända begränsningar med äldre modeller:
> - **`reasoning`-parametern**: Stöds inte på `gpt-4o-mini`, `gpt-4o` och många icke-resoneringsmodeller. Migrera endast `reasoning` om det redan fanns i originalkoden.
> - **`seed`-parametern**: Stöds inte alls i Responses API — ta bort från alla förfrågningar.
> - **Strukturerad output via `text.format`**: Äldre modeller kan ha svagt stöd för strikt `true` JSON-schema.
> - **Verktygsorkestrering**: GPT-5+ orkestrerar verktygsanrop som del av intern resonemang. Äldre modeller på Responses fungerar dock men saknar detta djupa integrationssteg.
> - **Temperaturbegränsningar**: Vid migrering till `gpt-5` måste temperatur utelämnas eller sättas till `1`. Äldre modeller har inga sådana begränsningar.

### O-seriens resoneringsmodeller (o1, o3-mini, o3, o4-mini)

O-seriens modeller har unika parameterbegränsningar. Vid migrering av appar som riktar sig mot o-seriens modeller:

- **`temperature`**: Måste vara `1` (eller utelämnas). O-seriens modeller accepterar inga andra värden.
- **`max_completion_tokens` → `max_output_tokens`**: Appar som använder Azure-specifika `max_completion_tokens` måste byta till `max_output_tokens`. Sätt höga värden (4096+) eftersom resonemangstokens räknas mot gränsen.
- **`reasoning_effort`**: Om appen använder `reasoning_effort` (low/medium/high), behåll den — Responses API stöder denna parameter för o-seriens modeller.
- **Streaming-beteende**: O-seriens modeller kan buffra output tills resonemanget avslutats innan text-delta events sänds. Streaming fungerar fortfarande, men första `response.output_text.delta` kan komma efter en längre fördröjning än med GPT-modeller.
- **`top_p`**: Stöds inte på o-serien — ta bort om det finns.
- **Verktygsanvändning**: O-seriens modeller stödjer verktyg via Responses API likt GPT-modeller, men orkestreringskvaliteten varierar per modell.

**Åtgärd — proaktiv modellrådgivning**: Under skanningsfasen, kontrollera vilken modell appen riktar sig mot (distributionsnamn, miljövariabler, konfig). Om modellen är `gpt-4o` eller äldre (inte gpt-4.1+), informera användaren proaktivt:
- Migreringen kommer fungera för grundläggande text, chatt, streaming och verktyg på deras nuvarande modell.
- Nyare modeller (`gpt-5.1`, `gpt-5.2`) erbjuder bättre verktygsorkestrering, striktare strukturerad output, resonemang och tvärregional tillgänglighet.
- De bör överväga att uppgradera sin distribution när de är redo — det blockerar inte migreringen.

Blockera inte eller vägra migrera baserat på modellversion. Rådgivningen är informativ.

### GitHub Models stöder INTE Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) stöder inte Responses API.**

Om kodbasen har en GitHub Models-kodväg (kolla efter `base_url` som pekar på `models.github.ai` eller `models.inference.ai.azure.com`), **ta bort den helt** vid migrering. Responses API kräver Azure OpenAI, OpenAI eller en kompatibel lokal endpoint (t.ex. Ollama med Responses-stöd).

Åtgärd under skanning:
- Markera alla GitHub Models-kodvägar för borttagning.

---

## Framework-migrering

Många appar använder högre nivåsramverk ovanpå OpenAI. Vid migrering av dessa ändras ramverkets egna API, inte bara de underliggande OpenAI-anropen.

### Microsoft Agent Framework (MAF)

**Kontrollera din MAF-version först** — migreringen beror på om du använder MAF 1.0.0+ eller en pre-1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **använder redan Responses API** — ingen migrering behövs. Om kodbasen använder den gamla `OpenAIChatCompletionClient` (som använder `chat.completions.create`), byt till `OpenAIChatClient`.

| Före | Efter |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

För att kontrollera din version: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc-releaser)

I pre-1.0.0 MAF användes `OpenAIChatClient` Chat Completions. Uppgradera till `agent-framework-openai>=1.0.0` där `OpenAIChatClient` som standard använder Responses API.

Inga ytterligare ändringar behövs — `Agent` och verktygs-API:erna förblir samma.

### LangChain (`langchain-openai`)

Lägg till `use_responses_api=True` till `ChatOpenAI()`. Uppdatera även åtkomst från `.content` till `.text`.

| Före | Efter |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

För kompletta före/efter-kodexempel, se [cheat-sheet.md](./references/cheat-sheet.md).

---

## Vägledning för frontend-migrering

> **Responses API är en server-side-fråga.** Migrera din Python-backend; front-endens HTTP-kontrakt bör förbli oförändrat såvida inte backenden är en tunn vidarebefordrare — i det fallet överväg att anta Responses-förfrågestrukturen för att eliminera ett översättningslager. Om frontend anropar OpenAI direkt med keys på klientsidan, flytta dessa anrop till backend först.

### `@microsoft/ai-chat-protocol` avskrivning

`@microsoft/ai-chat-protocol` npm-paketet är avskrivet och bör ersättas med [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Om du stöter på det i en frontend:

1. Byt ut CDN-script-taggen:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```

2. Ta bort instansen av `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Byt ut `client.getStreamedCompletion(messages)` med ett direkt `fetch()`-anrop till backend streaming-endpoint.
4. Byt ut `for await (const response of result)` med `for await (const chunk of readNDJSONStream(response.body))`.
5. Uppdatera egenskapsåtkomst från `response.delta.content` / `response.error` till `chunk.delta.content` / `chunk.error`.

---

## Mål

- Identifiera alla Python-anropsställen som använder Chat Completions eller gamla Completions mot Azure OpenAI.
- Föreslå en migreringsplan och ordning för Python-kodbasen.
- Utför säkra, minimala ändringar för att byta till Responses API.
- Uppdatera anropare att konsumera Responses output-schema; inga bakåtkompatibla omslag.
- Kör tester/lints; fixa triviala brytningar som migreringen orsakat.
- Förbered små, granskbara ändringsset och ge en slutlig sammanfattning med diffar (committa inte).

---

## Styrregler

- Ändra endast filer inom git-arbetsytan. Skriv aldrig utanför.
- Behåll inte bakåtkompatibilitets-shims; migrera koden till ny API-struktur.
- Lämna inga kvarlämnade övergångskommentarer eller backup-filer.
- Behåll streamingsemantik om den användes tidigare; annars använd icke-streaming.
- Begär godkännande före körning av kommandon eller nätverksanrop om läge för godkännande är aktiverat.
- Kör inte `git add`/`git commit`/`git push`; gör endast ändringar i arbetsytan.

---

## Steg 0: Azure OpenAI-klientmigrering (Förutsättning)

Om kodbasen använder `AzureOpenAI` eller `AsyncAzureOpenAI` konstruktörer, migrera först till standard `OpenAI` / `AsyncOpenAI`-konstruktörer. Azure-specifika konstruktörer är avskrivna i `openai>=1.108.1`.

### Varför v1 API-väg?

Den nya `/openai/v1` endpointen använder standardklienten `OpenAI()` istället för `AzureOpenAI()`, kräver ingen `api_version`-parameter, och fungerar lika för OpenAI och Azure OpenAI. Samma klientkod är framtidssäker — ingen versionshantering krävs.

### Viktiga ändringar

| Före | Efter |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Ta bort helt |

### Rensningschecklista

- Ta bort `api_version`-argument från klientkonstruktion.
- Ta bort miljövariabler `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` från `.env`, appinställningar och Bicep/infrastruktur-filer.
- Byt namn på `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` i `.env`, appinställningar, Bicep/infra och test-fixtures (standard för Azure Identity SDK).
- Säkerställ `openai>=1.108.1` i `requirements.txt` eller `pyproject.toml`.

### Migrering av miljövariabler

| Gammal miljövariabel | Åtgärd | Noteringar |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Ta bort** | Ingen `api_version` behövs med v1 endpoint |
| `AZURE_OPENAI_API_VERSION` | **Ta bort** | Samma som ovan |
| `AZURE_OPENAI_CLIENT_ID` | **Byt namn** → `AZURE_CLIENT_ID` | Standard Azure Identity SDK-konvention för `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Behåll** | Fortfarande nödvändig för konstruktion av `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Behåll** | Används som `model`-param i `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Behåll** | Används som `api_key` för nyckelbaserad autentisering |

För klientuppsättningsexempel (sync, async, EntraID, API-nyckel, multitenant), se [cheat-sheet.md](./references/cheat-sheet.md).

---

## Steg 1: Identifiera gamla anropspunkter

Kör skriptet [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) för att hitta alla anropsställen som behöver migreras:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Eller kör följande sökningar manuellt — varje träff är en migreringsmål:

```bash
# Legacy API-anrop (måste skriva om)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Föråldrade Azure-klientkonstruktörer (måste ersättas)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Svarsmall åtkomstmönster (måste uppdateras)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Verktygsdefinitioner i gammalt nästlat format (måste plattas till)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Verktygsresultat i gammalt format (måste konverteras till function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Föråldrade parametrar (måste tas bort eller byta namn på)
rg "response_format"
rg "max_tokens\b"        # byt namn till max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Föråldrade miljövariabler (städa upp)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # bör vara AZURE_CLIENT_ID

# GitHub Models-endpoints (måste tas bort — Responses API stöds inte)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Ramverksnivå legacy-mönster (måste uppdateras)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: ersätt med OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: behöver use_responses_api=True

# Testinfrastruktur (måste uppdateras)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Åtkomst till innehållsfiltreringsfel kropp (måste uppdateras — struktur ändrad)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # gammal singularform — nu content_filter_results (plural) inom content_filters-arrayen

# Råa HTTP-anrop till Chat Completions-endpoint (måste uppdatera URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristik (detektera och omskriv)

- **Chat Completions klient**: `client.chat.completions.create` → `client.responses.create(...)`.
- **Azure-klientkonstruktörer**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Verktyg**: konvertera funktionsanropsverktygsdefinitioner från nästlad form (`{"type": "function", "function": {"name": ...}}`) till platt Responses-format (`{"type": "function", "name": ...}`); använd `tool_choice`; returnera verktygsresultat som `{"type": "function_call_output", "call_id": ..., "output": ...}`-element (inte `{"role": "tool", ...}`).
- **Verktygs rundresor**: när modellen returnerar funktionsanrop, lägg till `response.output`-element i konversationen (inte en manuell `{"role": "assistant", "tool_calls": [...]}`-ordbok), och lägg sedan till `function_call_output`-element för varje resultat.
- **Få-skott verktygsexempel**: om konversationen innehåller hårdkodade verktygsanropsexempel, konvertera dem till `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`-element. ID:n måste börja med `fc_`.
- **`pydantic_function_tool()`**: denna hjälpare genererar fortfarande det gamla nästlade formatet och är **inte kompatibel** med `responses.create()`. Ersätt med manuella verktygsdefinitioner eller en flatnings-wrapper.
- **Flersteg**: behåll konversationshistoriken i appen; skicka tidigare turer via `input`-element.
- **Formatering**: ersätt Chats översta `response_format` med `text.format` i Responses. Kanonisk form: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Innehållselement**: ersätt Chat `content[].type: "text"` med Responses `content[].type: "input_text"` för användar-/systemturer.
- **Bildinnehållselement**: ersätt Chat `content[].type: "image_url"` med Responses `content[].type: "input_image"`. Fältet `image_url` ändras från en nästlad objekt `{"url": "..."}` till en platt sträng. Se fuskbladet för före/efter-exempel.
- **Slutsats ansträngning**: **migrera endast `reasoning` om det redan finns i originalkoden**.
- **Felhantering vid innehållsfilter**: felstrukturen ändrades. Chat Completions använde `error.body["innererror"]["content_filter_result"]` (ental); Responses API använder `error.body["content_filters"][0]["content_filter_results"]` (flertal, i en lista). Kod som åtkomst till `innererror` kastar `KeyError`. Omskriv för att använda den nya sökvägen.
- **Råa HTTP-anrop**: om appen anropar Azure OpenAI REST API direkt (via `requests`, `httpx` osv.) med `/openai/deployments/{name}/chat/completions?api-version=...`, skriv om till `/openai/v1/responses`. Begäran ändras: `messages` → `input`, lägg till `max_output_tokens` och `store: false`, ta bort `api-version`-query-parametern. Svarsstruktur ändras: `choices[0].message.content` → `output[0].content[0].text` (observera: `output_text` är en SDK-bekvämlighets-egenskap som inte finns i rå REST JSON).

---

## Steg 2: Tillämpar migrering

### Migreringsanteckningar (Chat Completions → Responses)

- **Varför migrera**: Responses är det enade API:t för text, verktyg och strömning; Chat Completions är föråldrat. Med GPT-5 krävs Responses för bästa prestanda.
- **HTTP**: Azure-endpoint byts från `/openai/deployments/{name}/chat/completions` till `/openai/v1/responses`.
- **Fält**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` oförändrat.
- **Formatering**: `response_format` → `text.format` med ett korrekt objekt.
- **Innehållselement**: ersätt Chat `content[].type: "text"` med Responses `content[].type: "input_text"` för system-/användarturer.
- **Bildinnehållselement**: ersätt Chat `content[].type: "image_url"` med Responses `content[].type: "input_image"`. Platta till `image_url` från `{"image_url": {"url": "..."}}` till `{"image_url": "..."}` (en vanlig sträng – antingen HTTPS URL eller en `data:image/...;base64,...` data URI).

### Kartläggning av parametrar

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array av element) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objekt) |
| `temperature` | `temperature` (oförändrad) |
| `stop` | `stop` (oförändrad) |
| `frequency_penalty` | `frequency_penalty` (oförändrad) |
| `presence_penalty` | `presence_penalty` (oförändrad) |
| `tools` / funktionsanrop | `tools` (oförändrad) |
| `seed` | **Ta bort** (stöds inte) |
| `store` | `store` (sätts till `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (platt sträng) |

För kompletta före/efter kodexempel, se [cheat-sheet.md](./references/cheat-sheet.md).

För testinfrastrukturmigration (mocks, snapshots, assertions), se [test-migration.md](./references/test-migration.md).

För felsökning av fel och vanliga fallgropar, se [troubleshooting.md](./references/troubleshooting.md).

---

## Datahantering och tillstånd

- Sätt `store: false` på alla Responses-förfrågningar.
- Förlita dig inte på tidigare meddelande-ID:n eller serverlagrat kontext; hantera tillstånd klient-sidigt och minimera metadata.

---

## Acceptanskriterier

### Kodnivågrindar (alla måste passera)

- [ ] Noll träffar för `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` i migrerade filer.
- [ ] Noll träffar för `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — alla konstruktorer använder `OpenAI`/`AsyncOpenAI` med v1-endpoint.
- [ ] Noll träffar för `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub-modellsökvägar borttagna.
- [ ] Noll träffar för `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ kod använder `OpenAIChatClient` (som använder Responses API). I pre-1.0.0, uppgradera till `agent-framework-openai>=1.0.0`.
- [ ] Alla `ChatOpenAI(...)`-anrop inkluderar `use_responses_api=True`.
- [ ] Noll träffar för `rg "choices\[0\]"` — alla svar åtkomst använder `resp.output_text` eller Responses output-schema.
- [ ] Ingen `response_format` på översta nivå; all strukturerad output använder `text={"format": {...}}`.
- [ ] `openai>=1.108.1` och `azure-identity` i `requirements.txt` eller `pyproject.toml`; beroenden ominstallerade.
- [ ] `store=False` satt på varje `responses.create`-anrop.
- [ ] Ingen `api_version` vid klientkonstruktion; `AZURE_OPENAI_API_VERSION` borttagen från miljöfiler och infrastruktur.

### Testinfrastrukturgrindar (alla måste passera)

- [ ] Noll träffar för `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Noll träffar för `rg "_azure_ad_token_provider" tests/` — assertions uppdaterade för att kontrollera `isinstance(client, AsyncOpenAI)` eller `base_url`.
- [ ] Noll träffar för `rg "prompt_filter_results|content_filter_results" tests/` — Azure-specifika filtermocks borttagna.
- [ ] Mock-fixtures använder `kwargs.get("input")` och inte `kwargs.get("messages")`.
- [ ] Snapshot-/golden-filer uppdaterade till Responses strömningsform (ingen `choices[0]`, `function_call`, `logprobs` osv.).
- [ ] `pytest` passerar utan fel efter alla testuppdateringar.

### Beteendegrindar (verifiera manuellt eller via testrigg)

- [ ] **Grundläggande completion**: icke-strömmande `responses.create` returnerar icke-tomt `output_text`.
- [ ] **Strömningsparitet**: om originalkoden använde strömning, strömmar migrerad kod och levererar `response.output_text.delta`-händelser med icke-tomma deltal.
- [ ] **Strukturerad output**: om `text.format` med `json_schema` används, lyckas `json.loads(resp.output_text)` och matcher schemat.
- [ ] **Verktygsanropsloop**: om verktyg används, gör modellen verktygsanrop, appen exekverar dem, och uppföljningsförfrågan returnerar slutligt `output_text` (ingen oändlig loop).
- [ ] **Async-paritet**: om `AsyncAzureOpenAI` användes, fungerar ekvivalent `AsyncOpenAI` med `await`.
- [ ] **Felrate**: inga nya 400/401/404-fel jämfört med pre-migrations-baslinjen.

### Leveranser

- Sammanfattning inkluderar redigerade filer, före-/efter-räkningar av legacy-anropsplatser, och nästa steg.
- Ändringar är endast working-tree-redigeringar (inga commit).

---

## SDK-versionkrav

| Paket | Minsta version |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Senaste (för EntraID-autentisering) |

---

## Referenser

- [Fuskblad — alla kodsnuttar](./references/cheat-sheet.md)
- [Testmigration — mocks, snapshots, assertions](./references/test-migration.md)
- [Felsökning — fel, risktabell, fallgropar](./references/troubleshooting.md)
- [detect_legacy.py — automatiserad scanner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Startpaket](https://aka.ms/openai/start)
- [Azure OpenAI Responses API-dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API versionslivscykel](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API referens](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->