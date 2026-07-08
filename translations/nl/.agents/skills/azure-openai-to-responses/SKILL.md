---
name: azure-openai-to-responses
license: MIT
---
# Migreer Python-apps van Azure OpenAI Chat Completions naar Responses API

> **AUTHORITATIEVE RICHTLIJN — VOLG EXACT**
>
> Deze skill migreert Python-codebases die Azure OpenAI Chat Completions gebruiken
> naar de uniforme Responses API. Volg deze instructies nauwkeurig.
> Improviseer niet met parameter mappings en verzin geen API vormen.

---

## Triggers

Activeer deze skill wanneer de gebruiker wil:
- Een Python-app migreren van Azure OpenAI Chat Completions naar Responses API
- Het gebruik van de Python OpenAI SDK upgraden naar de nieuwste API-vorm voor Azure OpenAI
- Python-code voorbereiden voor GPT-5 of nieuwere modellen die Responses op Azure vereisen
- Overschakelen van `AzureOpenAI`/`AsyncAzureOpenAI` naar de standaard `OpenAI`/`AsyncOpenAI` client met de v1 endpoint
- Deprecatie-waarschuwingen oplossen gerelateerd aan `AzureOpenAI` constructors of `api_version`

---

## ⚠️ Modelcompatibiliteit — EERST CONTROLEREN

> **Controleer vóór migratie of je Azure OpenAI-implementatie de Responses API ondersteunt.**

### 1. Voer een snelle test uit op je implementatie (snelste)

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

> **Opmerking**: `max_output_tokens` heeft een **minimum van 16** op Azure OpenAI. Waarden onder 16 geven een 400-fout. Gebruik 50+ voor snelle tests.

Als dit een 404 retourneert, ondersteunt het model van de implementatie Responses nog niet — controleer de referentie hieronder of zet opnieuw uit met een ondersteund model.

### 2. Controleer beschikbare modellen in jouw regio (aanbevolen)

Voer de ingebouwde modelcompatibiliteitstool uit om te zien wat beschikbaar is met ondersteuning voor Responses API in jouw specifieke regio:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Dit vraagt Azure ARM live op en toont een compatibiliteitsmatrix — welke modellen Responses, gestructureerde output, tools, enz. ondersteunen. Gebruik `--filter gpt-5.1,gpt-5.2` om te filteren of `--json` voor scripting.

### 3. Volledige referentie van modelondersteuning

- **Live query**: `python migrate.py models` (zie hierboven — regio-specifiek, altijd actueel)
- **Beschikbaarheid bekijken**: [Model overzichtstabel en regio-beschikbaarheid](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Quickstart & richtlijnen**: **https://aka.ms/openai/start**

### ⚠️ Beperkingen oudere modellen

> **WAARSCHUWING**: Oudere modellen (bijv. `gpt-4o`, `gpt-4`) ondersteunen mogelijk niet volledig alle features van de Responses API.
>
> Bekende beperkingen bij oudere modellen:
> - **`reasoning` parameter**: Niet ondersteund op `gpt-4o-mini`, `gpt-4o`, en veel niet-redeneer modellen. Migreer `reasoning` alleen als dit al in de originele code aanwezig was.
> - **`seed` parameter**: Helemaal niet ondersteund in Responses API — verwijder uit alle verzoeken.
> - **Gestructureerde output via `text.format`**: Oudere modellen handhaven mogelijk niet betrouwbaar `strict: true` JSON-schema's.
> - **Toolorchestratie**: GPT-5+ orkestreert tool-calls als onderdeel van interne redenering. Oudere modellen in Responses werken nog steeds maar missen deze diepe integratie.
> - **Temperatuurbeperkingen**: Bij migratie naar `gpt-5` moet temperatuur worden weggelaten of worden ingesteld op `1`. Oudere modellen kennen deze beperking niet.

### O-serie redeneer modellen (o1, o3-mini, o3, o4-mini)

O-serie modellen hebben unieke parameterbeperkingen. Bij migratie van apps die op o-serie modellen targeten:

- **`temperature`**: Moet `1` zijn (of worden weggelaten). O-serie modellen accepteren geen andere waarden.
- **`max_completion_tokens` → `max_output_tokens`**: Apps die de Azure-specifieke `max_completion_tokens` gebruiken moeten overschakelen naar `max_output_tokens`. Gebruik hoge waarden (4096+) omdat redeneertokens meetellen tegen de limiet.
- **`reasoning_effort`**: Als de app `reasoning_effort` gebruikt (laag/middel/hoog), behoud deze — de Responses API ondersteunt deze parameter voor o-serie modellen.
- **Streaming gedrag**: O-serie modellen kunnen output bufferen tot de redenering is voltooid voordat tekst delta-event wordt uitgegeven. Streaming werkt nog steeds, maar de eerste `response.output_text.delta` kan later aankomen dan bij GPT-modellen.
- **`top_p`**: Niet ondersteund op o-serie — verwijderen als aanwezig.
- **Toolgebruik**: O-serie modellen ondersteunen tools via Responses API hetzelfde als GPT-modellen, maar de kwaliteit van toolcall-orchestratie varieert per model.

**Actie — proactief modeladvies**: Controleer tijdens de scanfase welk model de app target (deploymentnamen, omgevingsvariabelen, config). Als het model `gpt-4o` of ouder is (niet gpt-4.1+), informeer de gebruiker proactief:
- De migratie werkt voor basis tekst, chat, streaming en tools op hun huidige model.
- Nieuwere modellen (`gpt-5.1`, `gpt-5.2`) bieden betere toolorchestratie, afdwinging gestructureerde output, redenering en regio-overstijgende beschikbaarheid.
- Ze zouden hun deployment kunnen upgraden wanneer ze klaar zijn — het blokkeert de migratie niet.

Blokkeer of weiger niet te migreren op basis van modelversie. Het advies is informatief.

### GitHub Models ondersteunt NIET de Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) ondersteunt de Responses API niet.**

Als de codebase een GitHub Models codepad heeft (zoek naar `base_url` die naar `models.github.ai` of `models.inference.ai.azure.com` wijst), **verwijder dit volledig** tijdens migratie. De Responses API vereist Azure OpenAI, OpenAI, of een compatibele lokale endpoint (bijv. Ollama met Responses ondersteuning).

Actie tijdens scan:
- Markeer alle GitHub Models codepaden voor verwijdering.

---

## Frameworkmigratie

Veel apps gebruiken hogere frameworks bovenop OpenAI. Bij migratie hiervan veranderen de API's van het framework zelf — niet alleen de onderliggende OpenAI-calls.

### Microsoft Agent Framework (MAF)

**Controleer eerst je MAF-versie** — de migratie hangt af van of je MAF 1.0.0+ of een pre-1.0.0 beta/rc gebruikt.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **gebruikt al de Responses API** — geen migratie nodig. Als de codebase de legacy `OpenAIChatCompletionClient` gebruikt (die `chat.completions.create` gebruikt), vervang dit dan door `OpenAIChatClient`.

| Voor | Na |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Om je versie te controleren: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc releases)

In pre-1.0.0 MAF gebruikte `OpenAIChatClient` Chat Completions. Upgrade naar `agent-framework-openai>=1.0.0` waarbij `OpenAIChatClient` standaard de Responses API gebruikt.

Geen andere wijzigingen nodig — de `Agent` en tool-API's blijven hetzelfde.

### LangChain (`langchain-openai`)

Voeg `use_responses_api=True` toe aan `ChatOpenAI()`. Pas ook response-toegang aan van `.content` naar `.text`.

| Voor | Na |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Voor volledige voor/na-codevoorbeelden, zie [cheat-sheet.md](./references/cheat-sheet.md).

---

## Frontend-migratierichtlijnen

> **De Responses API is een server-side kwestie.** Migreer je Python backend; het HTTP-contract van de frontend blijft ongewijzigd tenzij je backend slechts een dunne doorgeefluik is — in dat geval overweeg de Responses request-vorm over te nemen om een vertalingslaag te elimineren. Als de frontend direct met een client-side sleutel OpenAI aanroept, verplaats die calls dan eerst naar een backend.

### `@microsoft/ai-chat-protocol` deprecatie

Het `@microsoft/ai-chat-protocol` npm-pakket is verouderd en moet worden vervangen door [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Als je dit in een frontend tegenkomt:

1. Vervang het CDN script-tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Verwijder de `AIChatProtocolClient` instantiering (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Vervang `client.getStreamedCompletion(messages)` door een rechtstreekse `fetch()` call naar de backend streaming endpoint.
4. Vervang `for await (const response of result)` door `for await (const chunk of readNDJSONStream(response.body))`.
5. Werk property toegang bij van `response.delta.content` / `response.error` naar `chunk.delta.content` / `chunk.error`.

---

## Doelen

- Alle Python-callsites opsporen die Chat Completions of legacy Completions tegen Azure OpenAI gebruiken.
- Een migratieplan en volgorde voorstellen voor de Python-codebase.
- Veilige, minimale wijzigingen toepassen om te switchen naar Responses API.
- Aanroepers bijwerken om het Responses output schema te gebruiken; geen backcompat wrappers.
- Tests en lints draaien; triviale breuken door migratie oplossen.
- Kleine, controleerbare veranderingen voorbereiden en een eindoverzicht met diffs geven (niet committen).

---

## Beveiligingen

- Alleen bestanden binnen de git-werkruimte wijzigen. Nooit er buiten schrijven.
- Bewaar geen backward-compatibility shims; migreer code naar het nieuwe API-formaat.
- Laat geen tombstone/overgangscommentaar of backupbestanden achter.
- Preserve streaming-semantiek indien eerder gebruikt; anders niet-streaming gebruiken.
- Vraag goedkeuring voordat je commando's of netwerkcalls uitvoert als je in goedkeuringsmodus bent.
- Voer geen `git add`/`git commit`/`git push` uit; produceer alleen werkende boomwijzigingen.

---

## Stap 0: Migratie Azure OpenAI Client (voorwaarde)

Als de codebase `AzureOpenAI` of `AsyncAzureOpenAI` constructors gebruikt, migreer dan eerst naar de standaard `OpenAI` / `AsyncOpenAI` constructors. De Azure-specifieke constructors zijn verouderd in `openai>=1.108.1`.

### Waarom de v1 API route?

De nieuwe `/openai/v1` endpoint gebruikt de standaard `OpenAI()` client in plaats van `AzureOpenAI()`, vereist geen `api_version` parameter, en werkt identiek op OpenAI en Azure OpenAI. Dezelfde client code is toekomstbestendig — geen versiebeheer nodig.

### Belangrijkste veranderingen

| Voor | Na |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Helemaal verwijderen |

### Opschoonchecklist

- Verwijder het `api_version` argument uit de clientconstructie.
- Verwijder `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` omgevingsvariabelen uit `.env`, app-instellingen, en Bicep/infra-bestanden.
- Hernoem `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` in `.env`, app-instellingen, Bicep/infra en testfixtures (standaard Azure Identity SDK conventie).
- Zorg voor `openai>=1.108.1` in `requirements.txt` of `pyproject.toml`.

### Migratie van omgevingsvariabelen

| Oude env var | Actie | Opmerkingen |
|-------------|--------|------------|
| `AZURE_OPENAI_VERSION` | **Verwijderen** | Geen `api_version` nodig met v1 endpoint |
| `AZURE_OPENAI_API_VERSION` | **Verwijderen** | Zoals hierboven |
| `AZURE_OPENAI_CLIENT_ID` | **Hernoemen** → `AZURE_CLIENT_ID` | Standaard Azure Identity SDK conventie voor `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Behoud** | Nog steeds nodig voor constructie `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Behoud** | Wordt gebruikt als `model` parameter in `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Behoud** | Wordt gebruikt als `api_key` voor key-based authenticatie |

Voor voorbeelden van client-opzetcode (synchroon, asynchroon, EntraID, API sleutel, multi-tenant), zie [cheat-sheet.md](./references/cheat-sheet.md).

---

## Stap 1: Detecteer legacy callsites

Voer het script [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) uit om alle callsites te vinden die gemigreerd moeten worden:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Of voer deze zoekopdrachten handmatig uit — elke match is een migratiedoelwit:

```bash
# Legacy API-aanroepen (moeten herschreven worden)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Verouderde Azure-clientconstructors (moeten worden vervangen)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Toegangspatronen voor responsevorm (moeten worden bijgewerkt)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Tooldefinities in oud genest formaat (moeten worden afgevlakt)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Toolresultaten in oud formaat (moeten worden omgezet naar function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Verouderde parameters (moeten worden verwijderd of hernoemd)
rg "response_format"
rg "max_tokens\b"        # hernoemen naar max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Verouderde omgevingsvariabelen (schoonmaken)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # moet AZURE_CLIENT_ID zijn

# GitHub Models endpoints (moeten worden verwijderd — Responses API niet ondersteund)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Framework-niveau legacy patronen (moeten worden bijgewerkt)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: vervangen door OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: vereist use_responses_api=True

# Testinfrastructuur (moet worden bijgewerkt)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Toegang tot error body van contentfilter (moet worden bijgewerkt — structuur gewijzigd)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # oude enkelvoudsvorm — nu content_filter_results (meervoud) binnen content_filters array

# Rauwe HTTP-aanroepen naar Chat Completions endpoint (moeten URL bijwerken)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristieken (detectie en herschrijving)

- **Chat Completions client**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure-clientconstructors**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Tools**: converteer functieroepende tooldefinities van geneste indeling (`{"type": "function", "function": {"name": ...}}`) naar platte Responses-indeling (`{"type": "function", "name": ...}`); gebruik `tool_choice`; retourneer toolresultaten als `{"type": "function_call_output", "call_id": ..., "output": ...}` items (niet `{"role": "tool", ...}`).
- **Tool round-trips**: wanneer het model functieroepen retourneert, voeg dan `response.output` items toe aan het gesprek (niet een handmatige `{"role": "assistant", "tool_calls": [...]}` dict), voeg daarna `function_call_output` items toe voor elk resultaat.
- **Weinig-shot toolvoorbeelden**: als het gesprek hardcoded toolroepsvoorbeelden bevat, converteer deze dan naar `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` items. ID's moeten beginnen met `fc_`.
- **`pydantic_function_tool()`**: deze helper genereert nog steeds de oude geneste indeling en is **niet compatibel** met `responses.create()`. Vervang door handmatige tooldefinities of een flattening-wrapper.
- **Multi-turn**: onderhoud de gespreksgeschiedenis in de app; geef eerdere beurten door via `input` items.
- **Formattering**: vervang Chat's top-level `response_format` door `text.format` in Responses. Canonieke vorm: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Content items**: vervang Chat `content[].type: "text"` door Responses `content[].type: "input_text"` voor gebruiker/systeem beurten.
- **Afbeeldingscontent items**: vervang Chat `content[].type: "image_url"` door Responses `content[].type: "input_image"`. Het veld `image_url` verandert van een genest object `{"url": "..."}` naar een platte string. Zie het spiekbriefje voor voor/na voorbeelden.
- **Redeneringsinspanning**: **migreer `reasoning` alleen als het al bestaat in de originele code**.
- **Foutafhandeling contentfilter**: de foutbody-structuur is veranderd. Chat Completions gebruikte `error.body["innererror"]["content_filter_result"]` (enkelvoud); Responses API gebruikt `error.body["content_filters"][0]["content_filter_results"]` (meervoud, binnen een array). Code die `innererror` aanspreekt veroorzaakt een `KeyError`. Herschrijf om het nieuwe pad te gebruiken.
- **Raw HTTP oproepen**: als de app rechtstreeks de Azure OpenAI REST API aanroept (via `requests`, `httpx`, etc.) met `/openai/deployments/{name}/chat/completions?api-version=...`, herschrijf dan naar `/openai/v1/responses`. De requestbody verandert: `messages` → `input`, voeg `max_output_tokens` en `store: false` toe, verwijder de queryparameter `api-version`. De responsbody verandert: `choices[0].message.content` → `output[0].content[0].text` (let op: `output_text` is een SDK gemaksattribuut dat niet in raw REST JSON voorkomt).

---

## Stap 2: Toepassen van Migratie

### Migratienotities (Chat Completions → Responses)

- **Waarom migreren**: Responses is de uniforme API voor tekst, tools en streaming; Chat Completions is legacy. Met GPT-5 is Responses vereist voor optimale prestaties.
- **HTTP**: Azure endpoint verandert van `/openai/deployments/{name}/chat/completions` naar `/openai/v1/responses`.
- **Velden**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` blijft hetzelfde.
- **Formattering**: `response_format` → `text.format` met een juiste objectvorm.
- **Content items**: vervang Chat `content[].type: "text"` door Responses `content[].type: "input_text"` voor systeem/gebruikersbeurten.
- **Afbeeldingscontent items**: vervang Chat `content[].type: "image_url"` door Responses `content[].type: "input_image"`. Maak het `image_url` veld plat van `{"image_url": {"url": "..."}}` naar `{"image_url": "..."}` (een platte string — een HTTPS URL of een `data:image/...;base64,...` data-URI).

### Parametermappingreferentie

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array van items) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (object) |
| `temperature` | `temperature` (ongwijzigd) |
| `stop` | `stop` (ongwijzigd) |
| `frequency_penalty` | `frequency_penalty` (ongwijzigd) |
| `presence_penalty` | `presence_penalty` (ongwijzigd) |
| `tools` / function-calling | `tools` (ongwijzigd) |
| `seed` | **Verwijderen** (niet ondersteund) |
| `store` | `store` (instellen op `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (platte string) |

Voor volledige voor/na codevoorbeelden, zie [cheat-sheet.md](./references/cheat-sheet.md).

Voor testinfrastructuurmigratie (mocks, snapshots, assertions), zie [test-migration.md](./references/test-migration.md).

Voor het oplossen van fouten en valkuilen, zie [troubleshooting.md](./references/troubleshooting.md).

---

## Gegevensopslag & Status

- Stel `store: false` in op alle Responses-verzoeken.
- Vertrouw niet op eerdere bericht-ID's of door de server opgeslagen context; houd de status client-beheerd en minimaliseer metadata.

---

## Acceptatiecriteria

### Code-niveau poorten (alle moeten slagen)

- [ ] Geen resultaten voor `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` in gemigreerde bestanden.
- [ ] Geen resultaten voor `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — alle constructors gebruiken `OpenAI`/`AsyncOpenAI` met de v1 endpoint.
- [ ] Geen resultaten voor `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub Models codepaden verwijderd.
- [ ] Geen resultaten voor `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ code gebruikt `OpenAIChatClient` (dat Responses API gebruikt). In pre-1.0.0, upgrade naar `agent-framework-openai>=1.0.0`.
- [ ] Alle `ChatOpenAI(...)` aanroepen bevatten `use_responses_api=True`.
- [ ] Geen resultaten voor `rg "choices\[0\]"` — alle response toegang gebruikt `resp.output_text` of de Responses output schema.
- [ ] Geen `response_format` op topniveau; alle gestructureerde output gebruikt `text={"format": {...}}`.
- [ ] `openai>=1.108.1` en `azure-identity` in `requirements.txt` of `pyproject.toml`; afhankelijkheden opnieuw geïnstalleerd.
- [ ] `store=False` ingesteld op elke `responses.create` oproep.
- [ ] Geen `api_version` in clientconstructie; `AZURE_OPENAI_API_VERSION` verwijderd uit omgevingsbestanden en infra.

### Testinfrastructuur poorten (alle moeten slagen)

- [ ] Geen resultaten voor `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Geen resultaten voor `rg "_azure_ad_token_provider" tests/` — assertions bijgewerkt om `isinstance(client, AsyncOpenAI)` of `base_url` te controleren.
- [ ] Geen resultaten voor `rg "prompt_filter_results|content_filter_results" tests/` — Azure-specifieke filter mocks verwijderd.
- [ ] Mocks maken gebruik van `kwargs.get("input")` niet `kwargs.get("messages")`.
- [ ] Snapshot / golden bestanden bijgewerkt naar Responses streaming vorm (geen `choices[0]`, `function_call`, `logprobs`, enz.).
- [ ] `pytest` slaagt met nul fouten na alle testupdates.

### Gedragspoorten (verifieer handmatig of via testomgeving)

- [ ] **Basisvoltooiing**: niet-streaming `responses.create` retourneert niet-lege `output_text`.
- [ ] **Stream-pariteit**: als de originele code streaming gebruikte, stroomt de gemigreerde code en levert `response.output_text.delta` events met niet-lege delta's.
- [ ] **Gestructureerde output**: als `text.format` met `json_schema` wordt gebruikt, slaagt `json.loads(resp.output_text)` en komt overeen met het schema.
- [ ] **Tool-oproep lus**: als tools worden gebruikt, doet het model tool-aanroepen, voert de app ze uit, en de vervolgoproep retourneert een definitieve `output_text` (geen oneindige lus).
- [ ] **Async-pariteit**: als `AsyncAzureOpenAI` werd gebruikt, werkt het equivalent `AsyncOpenAI` met `await`.
- [ ] **Foutrapport**: geen nieuwe 400/401/404 fouten vergeleken met de pre-migratie baseline.

### Op te leveren zaken

- Samenvatting bevat bewerkte bestanden, voor/na tellingen van legacy aanroepplaatsen, en volgende stappen.
- Wijzigingen zijn alleen werkboom-bewerkingen (geen commits).

---

## SDK Versievereisten

| Pakket | Minimale Versie |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Laatste (voor EntraID authenticatie) |

---

## Referenties

- [Spiekbrief — alle codefragmenten](./references/cheat-sheet.md)
- [Testmigratie — mocks, snapshots, assertions](./references/test-migration.md)
- [Probleemoplossing — fouten, risicotabel, valkuilen](./references/troubleshooting.md)
- [detect_legacy.py — geautomatiseerde scanner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API docs](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API versie levenscyclus](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API referentie](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->