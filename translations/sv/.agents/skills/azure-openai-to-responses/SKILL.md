---
name: azure-openai-to-responses
license: MIT
---
# Migrera Python-appar från Azure OpenAI Chat Completions till Responses API

> **AUKTORITATIV VÄGLEDNING — FÖLJ PRECIS**
>
> Denna funktion migrerar Python-kodbaser som använder Azure OpenAI Chat Completions
> till det enhetliga Responses API. Följ dessa instruktioner noggrant.
> Improvise inte parametrar eller hitta på API-strukturer.

---

## Utlösare

Aktivera denna funktion när användaren vill:
- Migrera en Python-app från Azure OpenAI Chat Completions till Responses API
- Uppgradera Python OpenAI SDK-användning till den senaste API-strukturen för Azure OpenAI
- Förbereda Python-kod för GPT-5 eller nyare modeller som kräver Responses på Azure
- Byta från `AzureOpenAI`/`AsyncAzureOpenAI` till standard `OpenAI`/`AsyncOpenAI` klient med v1-endpoint
- Fixa föråldringsvarningar relaterade till `AzureOpenAI`-konstruktörer eller `api_version`

---

## ⚠️ Modellkompatibilitet — KOLLA FÖRST

> **Innan migrering, verifiera att din Azure OpenAI-distribution stöder Responses API.**

### 1. Snabbtest av distributionen (snabbast)

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

> **Notera**: `max_output_tokens` har ett **minimum på 16** på Azure OpenAI. Värden under 16 ger ett 400-fel. Använd 50+ för snabbtester.

Om detta returnerar 404, stödjer inte modellens distribution Responses än — kolla referensen nedan eller distribuera om med en stödjande modell.

### 2. Kolla tillgängliga modeller i din region (rekommenderas)

Kör det inbyggda verktyget för modellkompatibilitet för att se vad som är tillgängligt med Responses API-stöd i just din region:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Detta gör en live-fråga mot Azure ARM och visar en kompatibilitetsmatris — vilka modeller som stöder Responses, strukturerad output, verktyg etc. Använd `--filter gpt-5.1,gpt-5.2` för att begränsa resultat eller `--json` för skript.

### 3. Full modellstödsreferens

- **Live-fråga**: `python migrate.py models` (se ovan — regionsspecifik, alltid uppdaterad)
- **Bläddra tillgänglighet**: [Modellsammanfattningstabell och regiontillgänglighet](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Snabbstart & vägledning**: **https://aka.ms/openai/start**

### ⚠️ Begränsningar för äldre modeller

> **VARNING**: Äldre modeller (de som föregår `gpt-4.1`) kan sakna fullständigt stöd för alla Responses API-funktioner.
>
> Kända begränsningar för äldre modeller:
> - **`reasoning`-parametern**: Stöds inte på många modeller utan resonemang. Migrera endast `reasoning` om det redan fanns med i originalkoden.
> - **`seed`-parametern**: Stöds inte alls i Responses API — ta bort från alla anrop.
> - **Strukturerad output via `text.format`**: Äldre modeller kan ha svårt att pålitligt genomdriva `strict: true` JSON-scheman.
> - **Verktygsorkestrering**: GPT-5+ orkestrerar verktygssamtal som del av internt resonemang. Äldre modeller i Responses fungerar fortfarande men saknar denna djupa integration.
> - **Temperaturbegränsningar**: Vid migrering till `gpt-5` måste temperatur utelämnas eller sättas till `1`. Äldre modeller har inte denna begränsning.

### O-seriens resonemangsmodeller (o1, o3-mini, o3, o4-mini)

O-seriens modeller har unika parameterbegränsningar. När appar migreras som riktar sig mot o-serien:

- **`temperature`**: Måste vara `1` (eller utelämnas). O-seriens modeller accepterar inga andra värden.
- **`max_completion_tokens` → `max_output_tokens`**: Appar som använder Azure-specifika `max_completion_tokens` måste växla till `max_output_tokens`. Sätt höga värden (4096+) då tokens för resonemang räknas mot gränsen.
- **`reasoning_effort`**: Om appen använder `reasoning_effort` (low/medium/high), behåll det — Responses API stödjer denna parameter för o-seriens modeller.
- **Streamingbeteende**: O-seriens modeller kan buffra output tills resonemanget är klart innan de skickar textdelta-events. Streaming fungerar ändå, men första `response.output_text.delta` kan komma med längre fördröjning än med GPT-modeller.
- **`top_p`**: Stöds inte på o-serien — ta bort om det finns.
- **Verktygsanvändning**: O-seriens modeller stödjer verktyg via Responses API likt GPT-modeller, men kvaliteten på orkestreringen varierar beroende på modell.

**Åtgärd — proaktiv modellrådgivning**: Under skanningsfas, kolla vilken modell appen riktar sig mot (distributionsnamn, miljövariabler, konfiguration). Om modellen föregår `gpt-4.1` (inte gpt-4.1+), informera användaren proaktivt:
- Migreringen fungerar för grundläggande text, chatt, streaming och verktyg på deras nuvarande modell.
- Nyare modeller (`gpt-5.1`, `gpt-5.2`) erbjuder bättre verktygsorkestrering, striktare strukturerad output, resonemang och tillgång över regioner.
- De bör överväga att uppgradera sin distribution när de är redo — det blockerar inte migreringen.

Blockera inte eller vägra migrera baserat på modellversion. Rådgivningen är informativ.

### GitHub Models stöder INTE Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) stöder inte Responses API.**

Om kodbasen har en GitHub Models-kodväg (sök efter `base_url` som pekar mot `models.github.ai` eller `models.inference.ai.azure.com`), **ta bort den helt** vid migrering. Responses API kräver Azure OpenAI, OpenAI eller en kompatibel lokal endpoint (t.ex. Ollama med Responses-stöd).

Åtgärd vid scanning:
- Markera alla GitHub Models-kodvägar för borttagning.

---

## Ramverksmigrering

Många appar använder högre nivåers ramverk ovanpå OpenAI. Vid migrering ändras ramverkets egna API — inte bara underliggande OpenAI-anrop.

### Microsoft Agent Framework (MAF)

**Kolla din MAF-version först** — migreringen beror på om du har MAF 1.0.0+ eller en pre-1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **använder redan Responses API** — ingen migrering behövs. Om kodbasen använder den äldre `OpenAIChatCompletionClient` (som använder `chat.completions.create`), ersätt med `OpenAIChatClient`.

| Före | Efter |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

För att kolla din version: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc-utgåvor)

I pre-1.0.0 MAF använde `OpenAIChatClient` Chat Completions. Uppgradera till `agent-framework-openai>=1.0.0` där `OpenAIChatClient` använder Responses API som standard.

Inga andra ändringar krävs — `Agent` och verktygs-API:er förblir desamma.

### LangChain (`langchain-openai`)

Lägg till `use_responses_api=True` till `ChatOpenAI()`. Uppdatera även svarstillgång från `.content` till `.text`.

| Före | Efter |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

För fullständiga före- och efter-exempel, se [cheat-sheet.md](./references/cheat-sheet.md).

---

## Frontend-migreringsvägledning

> **Responses API är en serversidesak.** Migrera din Python-backend; frontendens HTTP-kontrakt bör förbli oförändrat om inte backenden är ett tunt genomskick — i så fall överväg att använda Responses-förfrågestruktur för att eliminera ett översättningslager. Om frontenden anropar OpenAI direkt med en klient-side-nyckel, flytta dessa anrop till backend först.

### `@microsoft/ai-chat-protocol` är föråldrat

`@microsoft/ai-chat-protocol` npm-paketet är föråldrat och ska ersättas med [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Om du stöter på det i en frontend:

1. Ersätt CDN-script-taggen:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Ta bort `AIChatProtocolClient`-instansieringen (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Ersätt `client.getStreamedCompletion(messages)` med direkt `fetch()`-anrop till backend streaming endpoint.
4. Ersätt `for await (const response of result)` med `for await (const chunk of readNDJSONStream(response.body))`.
5. Uppdatera egenskapsåtkomst från `response.delta.content` / `response.error` till `chunk.delta.content` / `chunk.error`.

---

## Mål

- Lista alla Python-anropsställen som använder Chat Completions eller äldre Completions mot Azure OpenAI.
- Föreslå en migreringsplan och sekvensering för Python-kodbaskoden.
- Använd säkra, minimala ändringar för att byta till Responses API.
- Uppdatera anropare att konsumera Responses output-schema; inga bakåtkompatibla omslag.
- Kör tester/lintar; fixa triviala fel som migreringen medför.
- Förbered små, granskningsbara ändringsset och ge en slutgiltig sammanfattning med diffar (committra inte).

---

## Ramverk

- Ändra endast filer inom git-arbetsytan. Skriv aldrig utanför.
- Behåll inte bakåtkompatibilitets-shims; migrera koden till ny API-struktur.
- Lämna inga gravstenar/övergångskommentarer eller säkerhetskopior.
- Behåll streamingsemantik om det användes tidigare; annars använd icke-streaming.
- Be om godkännande innan körning av kommandon eller nätverksanrop om i godkännandeläge.
- Kör inte `git add`/`git commit`/`git push`; producera endast redigeringar i arbetsytan.

---

## Steg 0: Azure OpenAI-klientmigrering (Förutsättning)

Om kodbasen använder `AzureOpenAI` eller `AsyncAzureOpenAI`-konstruktörer, migrera först till standard `OpenAI` / `AsyncOpenAI`-konstruktörer. Azure-specifika konstruktörer är föråldrade i `openai>=1.108.1`.

### Varför v1 API-vägen?

Den nya `/openai/v1`-endpointen använder standardklienten `OpenAI()` istället för `AzureOpenAI()`, kräver ingen `api_version`-parameter och fungerar identiskt för OpenAI och Azure OpenAI. Samma klientkod är framtidssäker – ingen versionshantering behövs.

### Viktiga förändringar

| Före | Efter |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Ta bort helt |

### Rensningschecklista

- Ta bort `api_version`-argumentet från klientkonstruktion.
- Ta bort `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` miljövariabler från `.env`, appinställningar och Bicep/infra-filer.
- Byt namn på `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` i `.env`, appinställningar, Bicep/infra och test-fixtures (standard Azure Identity SDK-konvention).
- Säkerställ `openai>=1.108.1` i `requirements.txt` eller `pyproject.toml`.

### Migrering av miljövariabler

| Gammal miljövariabel | Åtgärd | Noteringar |
|-------------|--------|-----------|
| `AZURE_OPENAI_VERSION` | **Ta bort** | Ingen `api_version` behövs med v1 endpoint |
| `AZURE_OPENAI_API_VERSION` | **Ta bort** | Samma som ovan |
| `AZURE_OPENAI_CLIENT_ID` | **Byt namn** → `AZURE_CLIENT_ID` | Standard Azure Identity SDK-konvention för `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Behåll** | Fortfarande behövs för `base_url`-konstruktion |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Behåll** | Används som `model`-param i `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Behåll** | Används som `api_key` för nyckelbaserad autentisering |

För klientuppsättningskodsexempel (synkron, asynkron, EntraID, API-nyckel, multi-tenant), se [cheat-sheet.md](./references/cheat-sheet.md).

---

## Steg 1: Hitta äldre anropsställen

Kör skriptet [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) för att hitta alla anropsställen som behöver migreras:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Eller gör dessa sökningar manuellt — varje träff är ett migreringsmål:

```bash
# Äldre API-anrop (måste skrivas om)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Föråldrade Azure-klientkonstruktörer (måste bytas ut)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Svarsmönster för åtkomst (måste uppdateras)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Verktygsdefinitioner i gammalt nästlat format (måste plattas ut)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Verktygsresultat i gammalt format (måste konverteras till function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Föråldrade parametrar (måste tas bort eller byta namn på)
rg "response_format"
rg "max_tokens\b"        # byt namn till max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Föråldrade miljövariabler (rensa upp)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # bör vara AZURE_CLIENT_ID

# GitHub Models-endpunkter (måste tas bort — Responses API stöds ej)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Ramverksnivå äldre mönster (måste uppdateras)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: ersätt med OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: kräver use_responses_api=True

# Testinfrastruktur (måste uppdateras)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Åtkomst för felkropp vid innehållsfilter (måste uppdateras — struktur ändrad)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # gammalt singularform — nu content_filter_results (plural) inuti content_filters-arrayen

# Råa HTTP-anrop till Chat Completions-endpunkt (måste uppdatera URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristik (identifiera och skriv om)

- **Chat Completions-klient**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure-klientkonstruktörer**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Verktyg**: konvertera funktionsanropsverktygsdefinitioner från nästlad form (`{"type": "function", "function": {"name": ...}}`) till flat Responses-format (`{"type": "function", "name": ...}`); använd `tool_choice`; returnera verktygsresultat som `{"type": "function_call_output", "call_id": ..., "output": ...}`-objekt (inte `{"role": "tool", ...}`).
- **Verktygsrundresor**: när modellen returnerar funktionsanrop, lägg till `response.output`-objekt till konversationen (inte en manuell `{"role": "assistant", "tool_calls": [...]}`-ordbok), och lägg sedan till `function_call_output`-objekt för varje resultat.
- **Få-shot-verktygsexempel**: om konversationen innehåller hårdkodade verktygsanropsexempel, konvertera dem till `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`-objekt. ID måste börja med `fc_`.
- **`pydantic_function_tool()`**: denna hjälpfunktion genererar fortfarande det gamla nästlade formatet och är **inte kompatibel** med `responses.create()`. Ersätt med manuella verktygsdefinitioner eller ett plattande omslag.
- **Fleromgångar**: behåll konversationshistoriken i appen; skicka tidigare omgångar via `input`-objekt.
- **Formatering**: ersätt Chats översta `response_format` med `text.format` i Responses. Kanonisk form: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Innehållsobjekt**: ersätt Chat `content[].type: "text"` med Responses `content[].type: "input_text"` för användar-/systemomgångar.
- **Bildinnehållsobjekt**: ersätt Chat `content[].type: "image_url"` med Responses `content[].type: "input_image"`. Fältet `image_url` ändras från ett nästlat objekt `{"url": "..."}` till en platt sträng. Se fusklappen för exempel före/efter.
- **Resonemangsinsats**: **migrera endast `reasoning` om det redan finns i originalkoden**.
- **Felhantering vid innehållsfilter**: felkroppsstrukturen har ändrats. Chat Completions använde `error.body["innererror"]["content_filter_result"]` (singular); Responses API använder `error.body["content_filters"][0]["content_filter_results"]` (plural, i en array). Kod som använder `innererror` kastar `KeyError`. Skriv om för att använda den nya vägen.
- **Råa HTTP-anrop**: om appen anropar Azure OpenAI REST API direkt (via `requests`, `httpx`, etc.) med `/openai/deployments/{name}/chat/completions?api-version=...`, skriv om till `/openai/v1/responses`. Förfrågningskroppen ändras: `messages` → `input`, lägg till `max_output_tokens` och `store: false`, ta bort `api-version` från query-param. Svarskroppen ändras: `choices[0].message.content` → `output[0].content[0].text` (notera: `output_text` är en SDK-bekvämlighetsfunktion som inte finns i rå REST JSON).

---

## Steg 2: Genomför migrering

### Migreringsanteckningar (Chat Completions → Responses)

- **Varför migrera**: Responses är det enhetliga API:et för text, verktyg och streaming; Chat Completions är legacy. Med GPT-5 krävs Responses för bästa prestanda.
- **HTTP**: Azure-endpoint ändras från `/openai/deployments/{name}/chat/completions` till `/openai/v1/responses`.
- **Fält**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` oförändrat.
- **Formatering**: `response_format` → `text.format` med ett korrekt objekt.
- **Innehållsobjekt**: ersätt Chat `content[].type: "text"` med Responses `content[].type: "input_text"` för system-/användaromgångar.
- **Bildinnehållsobjekt**: ersätt Chat `content[].type: "image_url"` med Responses `content[].type: "input_image"`. Platta ut `image_url`-fältet från `{"image_url": {"url": "..."}}` till `{"image_url": "..."}` (en enkel sträng – antingen en HTTPS-URL eller en `data:image/...;base64,...` data-URI).

### Referens för parametrarmappning

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array av objekt) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objekt) |
| `temperature` | `temperature` (oförändrat) |
| `stop` | `stop` (oförändrat) |
| `frequency_penalty` | `frequency_penalty` (oförändrat) |
| `presence_penalty` | `presence_penalty` (oförändrat) |
| `tools` / funktionsanrop | `tools` (oförändrat) |
| `seed` | **Ta bort** (stödjs inte) |
| `store` | `store` (sätt till `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (platt sträng) |

För fullständiga exempel före/efter, se [cheat-sheet.md](./references/cheat-sheet.md).

För migrering av testinfrastruktur (mocks, snapshots, assertions), se [test-migration.md](./references/test-migration.md).

För felsökning av fel och fallgropar, se [troubleshooting.md](./references/troubleshooting.md).

---

## Datahantering & Tillstånd

- Sätt `store: false` på alla Responses-förfrågningar.
- Lita inte på tidigare meddelande-ID:n eller serverlagrad kontext; håll tillståndet klienthanterat och minimera metadata.

---

## Acceptanskriterier

### Kodnivågrindar (alla måste passera)

- [ ] Noll träffar för `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` i migrerade filer.
- [ ] Noll träffar för `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — alla konstruktörer använder `OpenAI`/`AsyncOpenAI` med v1-endpoint.
- [ ] Noll träffar för `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub Models-kodvägar borttagna.
- [ ] Noll träffar för `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ använder `OpenAIChatClient` (som använder Responses API). I pre-1.0.0, uppgradera till `agent-framework-openai>=1.0.0`.
- [ ] Alla `ChatOpenAI(...)`-anrop inkluderar `use_responses_api=True`.
- [ ] Noll träffar för `rg "choices\[0\]"` — all åtkomst till svar använder `resp.output_text` eller Responses output-schema.
- [ ] Inget `response_format` på toppnivå; all strukturerad output använder `text={"format": {...}}`.
- [ ] `openai>=1.108.1` och `azure-identity` i `requirements.txt` eller `pyproject.toml`; beroenden ominstallerade.
- [ ] `store=False` satt på varje `responses.create`-anrop.
- [ ] Ingen `api_version` vid klientkonstruktion; `AZURE_OPENAI_API_VERSION` borttagen från miljöfiler och infrastruktur.

### Testinfrastrukturgrindar (alla måste passera)

- [ ] Noll träffar för `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Noll träffar för `rg "_azure_ad_token_provider" tests/` — assertions uppdaterade för att kontrollera `isinstance(client, AsyncOpenAI)` eller `base_url`.
- [ ] Noll träffar för `rg "prompt_filter_results|content_filter_results" tests/` — Azure-specifika filtermocks borttagna.
- [ ] Mock-fixtures använder `kwargs.get("input")` inte `kwargs.get("messages")`.
- [ ] Snapshot- / golden-filer uppdaterade till Responses streaming-form (ingen `choices[0]`, `function_call`, `logprobs` etc.).
- [ ] `pytest` går igenom utan fel efter alla testuppdateringar.

### Beteendegrindar (verifiera manuellt eller via testrigg)

- [ ] **Grundläggande completion**: icke-streamande `responses.create` returnerar icke-tomt `output_text`.
- [ ] **Streamparitet**: om den ursprungliga koden använde streaming, så strömmar den migrerade koden och avger `response.output_text.delta`-händelser med icke-tomma deltas.
- [ ] **Strukturerad output**: om `text.format` används med `json_schema` lyckas `json.loads(resp.output_text)` och matchar schemat.
- [ ] **Verktygsanropsloop**: om verktyg används, utfärdar modellen verktygsanrop, appen exekverar dem, och uppföljningsförfrågan returnerar slutlig `output_text` (ingen oändlig loop).
- [ ] **Async-paritet**: om `AsyncAzureOpenAI` användes fungerar motsvarande `AsyncOpenAI` med `await`.
- [ ] **Felränta**: inga nya 400/401/404-fel jämfört med pre-migreringsbaslinjen.

### Leveranser

- Sammanfattning inkluderar redigerade filer, före/efter-räkningar av legacy-anropsställen, och nästa steg.
- Ändringar är endast arbetskatalogsredigeringar (inga commits).

---

## SDK Versionskrav

| Paket | Minsta version |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Senaste (för EntraID-autentisering) |

---

## Referenser

- [Fusklapp — alla kodsnuttar](./references/cheat-sheet.md)
- [Testmigrering — mocks, snapshots, assertions](./references/test-migration.md)
- [Felsökning — fel, risktabell, fallgropar](./references/troubleshooting.md)
- [detect_legacy.py — automatiskt skannerverktyg](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API docs](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API reference](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->