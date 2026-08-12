---
name: azure-openai-to-responses
license: MIT
---
# Migreer Python-apps van Azure OpenAI Chat Completions naar Responses API

> **OFFICIËLE RICHTLIJNEN — VOLG PRECIES**
>
> Deze skill migreert Python-codebases die Azure OpenAI Chat Completions gebruiken
> naar de uniforme Responses API. Volg deze instructies nauwkeurig.
> Improviseer geen parameter-mappingen of bedenk geen API-structuren.

---

## Triggers

Activeer deze skill wanneer de gebruiker wil:
- Een Python-app migreren van Azure OpenAI Chat Completions naar Responses API
- Gebruik van Python OpenAI SDK upgraden naar de nieuwste API-structuur tegen Azure OpenAI
- Python-code voorbereiden voor GPT-5 of nieuwere modellen die Responses op Azure vereisen
- Overschakelen van `AzureOpenAI`/`AsyncAzureOpenAI` naar de standaard `OpenAI`/`AsyncOpenAI` client met de v1 endpoint
- Deprecation-waarschuwingen oplossen gerelateerd aan `AzureOpenAI` constructors of `api_version`

---

## ⚠️ Modelcompatibiliteit — EERST CONTROLEREN

> **Controleer vóór migratie of je Azure OpenAI deployment de Responses API ondersteunt.**

### 1. Voer een snelle test uit op je deployment (snelste)

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

> **Opmerking**: `max_output_tokens` heeft een **minimum van 16** op Azure OpenAI. Waarden lager dan 16 geven een 400-fout. Gebruik voor snelle tests 50+.

Als dit een 404 retourneert, ondersteunt het model van de deployment Responses nog niet — controleer de referentie hieronder of herdeploy met een ondersteund model.

### 2. Controleer beschikbare modellen in je regio (aanbevolen)

Voer de ingebouwde modelcompatibiliteitstool uit om te zien wat beschikbaar is met Responses API-ondersteuning in jouw specifieke regio:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Dit vraagt Azure ARM live op en toont een compatibiliteitsmatrix — welke modellen Responses, gestructureerde output, tools etc. ondersteunen. Gebruik `--filter gpt-5.1,gpt-5.2` om resultaten te filteren of `--json` voor scripting.

### 3. Volledige modelondersteuning referentie

- **Live query**: `python migrate.py models` (zie hierboven — regio-specifiek, altijd up-to-date)
- **Bekijk beschikbaarheid**: [Modeloverzichtstabel en regio-beschikbaarheid](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Quickstart & richtlijnen**: **https://aka.ms/openai/start**

### ⚠️ Beperkingen van oudere modellen

> **WAARSCHUWING**: Oudere modellen (voor `gpt-4.1`) ondersteunen mogelijk niet alle functies van de Responses API volledig.
>
> Bekende beperkingen van oudere modellen:
> - **`reasoning` parameter**: Niet ondersteund op veel niet-redenerende modellen. Migreer `reasoning` alleen als het al in de originele code aanwezig was.
> - **`seed` parameter**: Helemaal niet ondersteund in Responses API — verwijder uit alle verzoeken.
> - **Gestructureerde output via `text.format`**: Oudere modellen kunnen `strict: true` JSON-schema's mogelijk niet betrouwbaar afdwingen.
> - **Toolorkestratie**: GPT-5+ orkestreert toolaanroepen als onderdeel van interne reasoning. Oudere modellen op Responses werken nog steeds maar missen deze diepe integratie.
> - **Temperatuurbeperkingen**: Bij migratie naar `gpt-5` moet temperatuur worden weggelaten of op `1` gezet. Oudere modellen hebben hier geen beperking.

### O-serie reasoning modellen (o1, o3-mini, o3, o4-mini)

O-serie modellen hebben unieke parameterbeperkingen. Bij migratie van apps die o-serie modellen gebruiken:

- **`temperature`**: Moet `1` zijn (of weggelaten). O-serie modellen accepteren geen andere waarden.
- **`max_completion_tokens` → `max_output_tokens`**: Apps die de Azure-specifieke `max_completion_tokens` gebruiken moeten overstappen op `max_output_tokens`. Stel hoge waarden (4096+) in omdat reasoning-tokens meetellen voor de limiet.
- **`reasoning_effort`**: Als de app `reasoning_effort` gebruikt (laag/middel/hoog), behoud het — Responses API ondersteunt deze parameter voor o-serie modellen.
- **Streaming-gedrag**: O-serie modellen kunnen output bufferen tot reasoning voltooid is voor ze tekst-delta gebeurtenissen uitsturen. Streaming werkt nog steeds, maar de eerste `response.output_text.delta` kan later arriveren dan bij GPT-modellen.
- **`top_p`**: Niet ondersteund op o-serie — verwijder indien aanwezig.
- **Toolgebruik**: O-serie modellen ondersteunen tools via Responses API net als GPT modellen, maar kwaliteit van tool-aanroeporkestratie varieert per model.

**Actie — proactieve modeladviezen**: Tijdens de scanfase controleren welk model de app target (deploymentnamen, omgevingsvariabelen, configuratie). Als het model ouder is dan `gpt-4.1` (dus niet gpt-4.1+), vertel de gebruiker proactief:
- De migratie werkt voor basis tekst, chat, streaming en tools op het huidige model.
- Nieuwere modellen (`gpt-5.1`, `gpt-5.2`) bieden betere toolorkestratie, afdwingen van gestructureerde output, reasoning, en cross-region beschikbaarheid.
- Ze zouden hun deployment kunnen upgraden als ze willen — het blokkeert de migratie niet.

Blokkeer of weiger niet te migreren op basis van modelversie. Het advies is informatief.

### GitHub Models ondersteunt WELKE Responses API NIET

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) ondersteunt de Responses API NIET.**

Als de codebase een GitHub Models codepad heeft (zoek naar `base_url` die wijst naar `models.github.ai` of `models.inference.ai.azure.com`), **verwijder dit volledig** tijdens migratie. De Responses API vereist Azure OpenAI, OpenAI, of een compatibele lokale endpoint (bijv. Ollama met Responses ondersteuning).

Actie tijdens scan:
- Markeer alle GitHub Models codepaden voor verwijdering.

---

## Framework-migratie

Veel apps gebruiken hogere frameworks bovenop OpenAI. Bij migratie hiervan verandert ook de eigen API van het framework — niet alleen de onderliggende OpenAI-aanroepen.

### Microsoft Agent Framework (MAF)

**Controleer eerst je MAF-versie** — migratie hangt af van of je MAF 1.0.0+ of een pre-1.0.0 beta/rc gebruikt.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **gebruikt al de Responses API** — migratie niet nodig. Als de codebase de legacy `OpenAIChatCompletionClient` gebruikt (met `chat.completions.create`), vervang dit door `OpenAIChatClient`.

| Voor | Na |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Om versie te controleren: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc releases)

In pre-1.0.0 MAF gebruikte `OpenAIChatClient` Chat Completions. Upgrade naar `agent-framework-openai>=1.0.0` waar `OpenAIChatClient` standaard Responses API gebruikt.

Geen andere veranderingen nodig — `Agent` en tool APIs blijven ongewijzigd.

### LangChain (`langchain-openai`)

Voeg `use_responses_api=True` toe aan `ChatOpenAI()`. Update ook response-access van `.content` naar `.text`.

| Voor | Na |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Voor volledige voor/na codevoorbeelden, zie [cheat-sheet.md](./references/cheat-sheet.md).

---

## Frontend Migratie Richtlijnen

> **De Responses API is een server-side aangelegenheid.** Migreer je Python backend; het HTTP-contract van de frontend moet ongewijzigd blijven tenzij je backend een lichte doorgeeflaag is — overweeg dan de Responses request-structuur te adopteren om een vertaallaag te elimineren. Als de frontend OpenAI direct aanroept met een client-side sleutel, verplaats die aanroepen eerst naar een backend.

### `@microsoft/ai-chat-protocol` deprecieerd

Het `@microsoft/ai-chat-protocol` npm-pakket is deprecated en moet vervangen worden door [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Als je het in een frontend tegenkomt:

1. Vervang het CDN script-tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Verwijder de instantie van `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Vervang `client.getStreamedCompletion(messages)` door een rechtstreekse `fetch()` call naar de backend streaming endpoint.
4. Vervang `for await (const response of result)` door `for await (const chunk of readNDJSONStream(response.body))`.
5. Update property-toegang van `response.delta.content` / `response.error` naar `chunk.delta.content` / `chunk.error`.

---

## Doelen

- Alle Python aanroepplaatsen enumereren die Chat Completions of legacy Completions tegen Azure OpenAI gebruiken.
- Een migratieplan en ordening voor de Python-codebase voorstellen.
- Veilige, minimale aanpassingen doorvoeren om over te schakelen naar Responses API.
- Aanroepen bijwerken om de Responses output-schema te consumeren; geen backcompat wrappers.
- Tests/lints uitvoeren; triviale breuken door migratie oplossen.
- Kleine, reviewbare wijzigingssets voorbereiden en een eindoverzicht met diffs leveren (niet commiten).

---

## Beveiligingen

- Alleen bestanden binnen de git workspace wijzigen. Nooit buiten schrijven.
- Bewaar geen backward compatibiliteit shims; migreer code naar de nieuwe API-structuur.
- Laat geen grafsteen-/transitiecommentaren of backupbestanden achter.
- Streaming-semantiek behouden indien eerder gebruikt; anders niet-streaming gebruiken.
- Vraag goedkeuring vóór het uitvoeren van commando's of netwerk-aanroepen als je in goedkeuringsmodus bent.
- Voer geen `git add`/`git commit`/`git push` uit; lever alleen werkende-tree wijzigingen.

---

## Stap 0: Azure OpenAI Client Migratie (Vereiste)

Als de codebase `AzureOpenAI` of `AsyncAzureOpenAI` constructors gebruikt, migreer dan eerst naar de standaard `OpenAI` / `AsyncOpenAI` constructors. De Azure-specifieke constructors zijn deprecated in `openai>=1.108.1`.

### Waarom het v1 API-pad?

Het nieuwe `/openai/v1` endpoint gebruikt de standaard `OpenAI()` client in plaats van `AzureOpenAI()`, vereist geen `api_version` parameter, en werkt identiek op OpenAI en Azure OpenAI. Dezelfde client-code is toekomstbestendig — geen versiebeheer nodig.

### Belangrijkste wijzigingen

| Voor | Na |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Helemaal verwijderen |

### Opschoonchecklist

- Verwijder het `api_version` argument uit client-constructie.
- Verwijder `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` omgevingsvariabelen uit `.env`, app-instellingen en Bicep/infra-bestanden.
- Hernoem `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` in `.env`, app-instellingen, Bicep/infra, en testfixtures (standaard Azure Identity SDK conventie).
- Zorg dat `openai>=1.108.1` in `requirements.txt` of `pyproject.toml` staat.

### Migratie van omgevingsvariabelen

| Oude env var | Actie | Opmerkingen |
|-------------|--------|-----------|
| `AZURE_OPENAI_VERSION` | **Verwijderen** | Geen `api_version` nodig met v1 endpoint |
| `AZURE_OPENAI_API_VERSION` | **Verwijderen** | Zelfde als hierboven |
| `AZURE_OPENAI_CLIENT_ID` | **Hernoemen** → `AZURE_CLIENT_ID` | Standaard Azure Identity SDK conventie voor `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Behoud** | Nog steeds nodig voor `base_url` constructie |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Behoud** | Wordt gebruikt als `model` parameter in `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Behoud** | Wordt gebruikt als `api_key` voor sleutelgebaseerde authenticatie |

Voor client-setup codevoorbeelden (sync, async, EntraID, API key, multi-tenant), zie [cheat-sheet.md](./references/cheat-sheet.md).

---

## Stap 1: Legacy aanroepplaatsen detecteren

Voer het script [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) uit om alle aanroepplaatsen te vinden die migratie nodig hebben:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Of voer deze zoekopdrachten handmatig uit — elke match is een migratiedoel:

```bash
# Legacy API-aanroepen (moeten herschreven worden)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Verouderde Azure clientconstructors (moeten vervangen worden)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Toegangsmodellen voor responsvorm (moeten bijgewerkt worden)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Tooldefinities in oud genest formaat (moeten worden afgevlakt)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Toolresultaten in oud formaat (moeten worden geconverteerd naar function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Verouderde parameters (moeten verwijderd of hernoemd worden)
rg "response_format"
rg "max_tokens\b"        # hernoem naar max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Verouderde omgevingsvariabelen (opruimen)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # zou AZURE_CLIENT_ID moeten zijn

# GitHub Models endpoints (moeten verwijderd worden — Responses API niet ondersteund)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Framework-niveau legacy patronen (moeten bijgewerkt worden)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: vervang door OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: vereist use_responses_api=True

# Testinfrastructuur (moet worden bijgewerkt)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Toegang tot contentfilterfout body (moet worden bijgewerkt — structuur gewijzigd)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # oud enkelvoud — nu content_filter_results (meervoud) binnen content_filters array

# Rauwe HTTP-aanroepen naar Chat Completions endpoint (moeten URL bijwerken)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristieken (detecteren en herschrijven)

- **Chat Completions client**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure client constructors**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Tools**: converteer functie-aanroep tooldefinities van genest formaat (`{"type": "function", "function": {"name": ...}}`) naar vlak Responses-formaat (`{"type": "function", "name": ...}`); gebruik `tool_choice`; retourneer toolresultaten als `{"type": "function_call_output", "call_id": ..., "output": ...}` items (niet `{"role": "tool", ...}`).
- **Tool round-trips**: wanneer het model functie-aanroepen retourneert, voeg dan `response.output` items toe aan het gesprek (niet een handmatige `{"role": "assistant", "tool_calls": [...]}` dict), voeg daarna `function_call_output` items toe voor elk resultaat.
- **Few-shot tool voorbeelden**: als het gesprek hardcoded toolaanroep voorbeelden bevat, converteer ze dan naar `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` items. IDs moeten beginnen met `fc_`.
- **`pydantic_function_tool()`**: deze helper genereert nog steeds het oude geneste formaat en is **niet compatibel** met `responses.create()`. Vervang door handmatige tooldefinities of een flattening-wrapper.
- **Multi-turn**: onderhoud de gespreksgeschiedenis in de app; geef eerdere beurten door via `input` items.
- **Formatting**: vervang Chats top-level `response_format` door `text.format` in Responses. Canonieke vorm: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Content items**: vervang Chat `content[].type: "text"` door Responses `content[].type: "input_text"` voor gebruiker/systeem beurten.
- **Image content items**: vervang Chat `content[].type: "image_url"` door Responses `content[].type: "input_image"`. Het `image_url` veld verandert van een genest object `{"url": "..."}` naar een vlakke string. Zie de cheat sheet voor voor- en na voorbeelden.
- **Reasoning effort**: **migreer alleen `reasoning` als het al in de originele code bestaat**.
- **Content filter foutafhandeling**: de structuur van de foutbody is veranderd. Chat Completions gebruikte `error.body["innererror"]["content_filter_result"]` (enkelvoud); Responses API gebruikt `error.body["content_filters"][0]["content_filter_results"]` (meervoud, in een array). Code die `innererror` aanroept veroorzaakt een `KeyError`. Herschrijf om het nieuwe pad te gebruiken.
- **Raw HTTP calls**: als de app direct de Azure OpenAI REST API aanroept (via `requests`, `httpx`, enz.) met `/openai/deployments/{name}/chat/completions?api-version=...`, herschrijf deze naar `/openai/v1/responses`. De request body verandert: `messages` → `input`, voeg `max_output_tokens` en `store: false` toe, verwijder de `api-version` query param. De response body verandert: `choices[0].message.content` → `output[0].content[0].text` (let op: `output_text` is een SDK-convenience property die niet in de ruwe REST JSON staat).

---

## Stap 2: Pas migratie toe

### Migratienotities (Chat Completions → Responses)

- **Waarom migreren**: Responses is de uniforme API voor tekst, tools en streaming; Chat Completions is legacy. Met GPT-5 is Responses vereist voor optimale prestaties.
- **HTTP**: Azure endpoint schakelt van `/openai/deployments/{name}/chat/completions` naar `/openai/v1/responses`.
- **Velden**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` blijft gelijk.
- **Formatting**: `response_format` → `text.format` met een correct object.
- **Content items**: vervang Chat `content[].type: "text"` door Responses `content[].type: "input_text"` voor systeem/gebruiker beurten.
- **Image content items**: vervang Chat `content[].type: "image_url"` door Responses `content[].type: "input_image"`. Vlak het `image_url` veld af van `{"image_url": {"url": "..."}}` naar `{"image_url": "..."}` (een gewone string — een HTTPS URL of een `data:image/...;base64,...` data URI).

### Parameter mapping referentie

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array van items) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (object) |
| `temperature` | `temperature` (onveranderd) |
| `stop` | `stop` (onveranderd) |
| `frequency_penalty` | `frequency_penalty` (onveranderd) |
| `presence_penalty` | `presence_penalty` (onveranderd) |
| `tools` / functie-aanroepen | `tools` (onveranderd) |
| `seed` | **Verwijderen** (niet ondersteund) |
| `store` | `store` (instellen op `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (platte string) |

Voor volledige code-voor-na voorbeelden, zie [cheat-sheet.md](./references/cheat-sheet.md).

Voor test infrastructuur migratie (mocks, snapshots, assertions), zie [test-migration.md](./references/test-migration.md).

Voor probleemoplossing bij fouten en valkuilen, zie [troubleshooting.md](./references/troubleshooting.md).

---

## Gegevensbewaring & Status

- Zet `store: false` op alle Responses-aanroepen.
- Vertrouw niet op eerdere bericht-ID’s of context die op de server opgeslagen is; houd status client-managed en minimaliseer metadata.

---

## Acceptatiecriteria

### Code-niveau poorten (alle moeten slagen)

- [ ] Geen matches voor `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` in gemigreerde bestanden.
- [ ] Geen matches voor `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — alle constructors gebruiken `OpenAI`/`AsyncOpenAI` met de v1 endpoint.
- [ ] Geen matches voor `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub Models code paths verwijderd.
- [ ] Geen matches voor `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ code gebruikt `OpenAIChatClient` (die Responses API gebruikt). Upgrade naar `agent-framework-openai>=1.0.0` in pre-1.0.0.
- [ ] Alle `ChatOpenAI(...)` aanroepen bevatten `use_responses_api=True`.
- [ ] Geen matches voor `rg "choices\[0\]"` — alle response toegang gebruikt `resp.output_text` of de Responses output schema.
- [ ] Geen `response_format` op topniveau; alle gestructureerde output gebruikt `text={"format": {...}}`.
- [ ] `openai>=1.108.1` en `azure-identity` in `requirements.txt` of `pyproject.toml`; dependencies opnieuw geïnstalleerd.
- [ ] `store=False` ingesteld op elke `responses.create` aanroep.
- [ ] Geen `api_version` in clientconstructie; `AZURE_OPENAI_API_VERSION` verwijderd uit env-bestanden en infra.

### Test infrastructuur poorten (alle moeten slagen)

- [ ] Geen matches voor `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Geen matches voor `rg "_azure_ad_token_provider" tests/` — assertions geüpdatet om `isinstance(client, AsyncOpenAI)` of `base_url` te controleren.
- [ ] Geen matches voor `rg "prompt_filter_results|content_filter_results" tests/` — Azure-specifieke filter mocks verwijderd.
- [ ] Mock fixtures gebruiken `kwargs.get("input")` niet `kwargs.get("messages")`.
- [ ] Snapshot / golden files aangepast aan Responses streaming vorm (geen `choices[0]`, `function_call`, `logprobs`, etc.).
- [ ] `pytest` slaagt met nul fouten na alle testupdates.

### Gedrags poorten (verifieer handmatig of via testomgeving)

- [ ] **Basis completion**: niet-streaming `responses.create` retourneert niet-lege `output_text`.
- [ ] **Stream pariteit**: als de originele code streaming gebruikte, streamt de gemigreerde code en levert `response.output_text.delta` events met niet-lege deltas.
- [ ] **Gestructureerde output**: als `text.format` met `json_schema` gebruikt wordt, slaagt `json.loads(resp.output_text)` en komt overeen met het schema.
- [ ] **Tool-aanroep lus**: als tools gebruikt worden, doet het model tool-aanroepen, voert de app ze uit, en de vervolg-aanroep retourneert een finale `output_text` (geen oneindige lus).
- [ ] **Async pariteit**: als `AsyncAzureOpenAI` werd gebruikt, werkt `AsyncOpenAI` equivalent met `await`.
- [ ] **Foutenpercentage**: geen nieuwe 400/401/404 fouten vergeleken met de pre-migratie baseline.

### Oplevering

- Samenvatting bevat bewerkte bestanden, voor/na tellingen van legacy aanroep locaties en volgende stappen.
- Wijzigingen zijn alleen werkboom edits (geen commits).

---

## SDK Versievereisten

| Pakket | Minimale Versie |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Laatste (voor EntraID authenticatie) |

---

## Referenties

- [Spiekbrief — alle codefragmenten](./references/cheat-sheet.md)
- [Test migratie — mocks, snapshots, assertions](./references/test-migration.md)
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