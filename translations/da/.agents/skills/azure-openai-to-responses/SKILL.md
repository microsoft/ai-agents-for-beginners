---
name: azure-openai-to-responses
license: MIT
---
# Migrer Python-apps fra Azure OpenAI Chat Completions til Responses API

> **AUTORITATIV VEJLEDNING – FØLG NØJE**
>
> Denne færdighed migrerer Python-kodebaser, der bruger Azure OpenAI Chat Completions
> til den samlede Responses API. Følg disse instruktioner præcist.
> Improvisér ikke med parameterkortlægninger eller opfind API-strukturer.

---

## Udløsere

Aktivér denne færdighed, når brugeren ønsker at:
- Migrere en Python-app fra Azure OpenAI Chat Completions til Responses API
- Opgradere Python OpenAI SDK-brug til den nyeste API-struktur mod Azure OpenAI
- Forberede Python-kode til GPT-5 eller nyere modeller, der kræver Responses på Azure
- Skifte fra `AzureOpenAI`/`AsyncAzureOpenAI` til standard `OpenAI`/`AsyncOpenAI` klient med v1-endpoint
- Løse forældelsesadvarsler relateret til `AzureOpenAI` konstruktører eller `api_version`

---

## ⚠️ Modelkompatibilitet – TJEK FØRST

> **Før migration, verificer at din Azure OpenAI-udrulning understøtter Responses API.**

### 1. Røgtest din udrulning (hurtigst)

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

> **Bemærk**: `max_output_tokens` har en **minimum på 16** på Azure OpenAI. Værdier under 16 giver en 400-fejl. Brug 50+ til røgtest.

Hvis dette returnerer 404, understøtter udrulningens model ikke Responses endnu — tjek referencen nedenfor eller deploy med en understøttet model.

### 2. Tjek tilgængelige modeller i din region (anbefalet)

Kør det indbyggede værktøj til modelkompatibilitet for at se, hvad der er tilgængeligt med Responses API-understøttelse i din specifikke region:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Dette forespørger Azure ARM live og viser en kompatibilitetsmatrix — hvilke modeller der understøtter Responses, struktureret output, værktøjer osv. Brug `--filter gpt-5.1,gpt-5.2` for at indsnævre resultater eller `--json` til scripting.

### 3. Fuld modelunderstøttelsesreference

- **Live-forespørgsel**: `python migrate.py models` (se ovenfor — regionspecifik, altid opdateret)
- **Gennemse tilgængelighed**: [Oversigtstabel over modeller og regions-tilgængelighed](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Hurtigstart & vejledning**: **https://aka.ms/openai/start**

### ⚠️ Ældre modellimitations

> **ADVARSEL**: Ældre modeller (fx `gpt-4o`, `gpt-4`) understøtter ikke fuldt ud alle Responses API-funktioner.
>
> Kendte begrænsninger med ældre modeller:
> - **`reasoning` parameter**: Ikke understøttet på `gpt-4o-mini`, `gpt-4o`, og mange ikke-reasoning modeller. Migrer kun `reasoning`, hvis det allerede var til stede i originalkoden.
> - **`seed` parameter**: Ikke understøttet i Responses API overhovedet — fjern fra alle forespørgsler.
> - **Struktureret output via `text.format`**: Ældre modeller håndhæver muligvis ikke pålideligt `strict: true` JSON-skemaer.
> - **Værktøjorkestrering**: GPT-5+ orkestrerer værktøjskald som en del af intern ræsonnering. Ældre modeller på Responses virker stadig, men mangler denne dybe integration.
> - **Temperaturbegrænsninger**: Ved migration til `gpt-5` skal temperatur udelades eller sættes til `1`. Ældre modeller har ingen sådan begrænsning.

### O-serie ræsonneringsmodeller (o1, o3-mini, o3, o4-mini)

O-serie modeller har unikke parameterbegrænsninger. Ved migration af apps, der målretter o-serie modeller:

- **`temperature`**: Skal være `1` (eller udelades). O-serie modeller accepterer ikke andre værdier.
- **`max_completion_tokens` → `max_output_tokens`**: Apps, der bruger Azure-specifikke `max_completion_tokens`, skal skifte til `max_output_tokens`. Sæt høje værdier (4096+) fordi reasoning tokens tæller mod grænsen.
- **`reasoning_effort`**: Hvis appen bruger `reasoning_effort` (lav/mellem/høj), behold det — Responses API understøtter denne parameter for o-serie modeller.
- **Streamingadfærd**: O-serie modeller kan buffere output indtil ræsonnering er færdig, før der udsendes tekst-delta events. Streaming virker stadig, men første `response.output_text.delta` kan ankomme med længere forsinkelse end med GPT-modeller.
- **`top_p`**: Ikke understøttet på o-serie — fjern hvis til stede.
- **Værktøjsbrug**: O-serie modeller understøtter værktøjer via Responses API på samme måde som GPT-modeller, men orkestreringskvaliteten af værktøjskald varierer efter model.

**Handling – proaktiv modelrådgivning**: I scanningfasen, tjek hvilken model appen målretter (udrulningsnavne, miljøvariabler, konfiguration). Hvis modellen er `gpt-4o` eller ældre (ikke gpt-4.1+), sig proaktivt til brugeren:
- Migrationen vil fungere til basistekst, chat, streaming og værktøjer på deres nuværende model.
- Nyere modeller (`gpt-5.1`, `gpt-5.2`) tilbyder bedre værktøjsorkestrering, håndhævelse af struktureret output, ræsonnering og tværregions tilgængelighed.
- De bør overveje at opgradere deres udrulning, når de er klar – det blokerer ikke migrationen.

Bloker ikke eller nægt at migrere baseret på modelversion. Rådgivningen er kun informativ.

### GitHub Models understøtter IKKE Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) understøtter ikke Responses API.**

Hvis kodebasen har en GitHub Models kodevej (se efter `base_url`, der peger på `models.github.ai` eller `models.inference.ai.azure.com`), **fjern den helt** under migrationen. Responses API kræver Azure OpenAI, OpenAI eller en kompatibel lokal endpoint (fx Ollama med Responses-understøttelse).

Handling under scanning:
- Marker alle GitHub Models kodeveje til fjernelse.

---

## Framework-migration

Mange apps bruger højere-niveau frameworks oven på OpenAI. Ved migration af disse ændres frameworkets egen API – ikke kun de underliggende OpenAI-kald.

### Microsoft Agent Framework (MAF)

**Tjek din MAF-version først** – migrationen afhænger af, om du er på MAF 1.0.0+ eller en pre-1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **bruger allerede Responses API** – ingen migration nødvendig. Hvis kodebasen bruger den gamle `OpenAIChatCompletionClient` (som bruger `chat.completions.create`), udskift den med `OpenAIChatClient`.

| Før | Efter |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

For at tjekke din version: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc-udgivelser)

I pre-1.0.0 MAF brugte `OpenAIChatClient` Chat Completions. Opgrader til `agent-framework-openai>=1.0.0`, hvor `OpenAIChatClient` som standard bruger Responses API.

Ingen andre ændringer nødvendige – `Agent` og værktøjs-API'er forbliver de samme.

### LangChain (`langchain-openai`)

Tilføj `use_responses_api=True` til `ChatOpenAI()`. Opdater også responsadgang fra `.content` til `.text`.

| Før | Efter |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

For komplette før/efter kodeeksempler, se [cheat-sheet.md](./references/cheat-sheet.md).

---

## Frontend-migrationsvejledning

> **Responses API er et serversideanliggende.** Migrer din Python-backend; frontendens HTTP-kontrakt bør forblive uændret, medmindre din backend er et tyndt pass-through — i så fald overvej at adoptere Responses-forespørgselsskjemaet for at eliminere et oversættelseslag. Hvis frontend kalder OpenAI direkte med en klientnøgle, flyt disse kald til backend først.

### `@microsoft/ai-chat-protocol` forældelse

`@microsoft/ai-chat-protocol` npm-pakken er forældet og bør erstattes med [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Hvis du møder det i en frontend:

1. Udskift CDN-script-tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Fjern instansiering af `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Udskift `client.getStreamedCompletion(messages)` med et direkte `fetch()` kald til backend streaming-endpointet.
4. Udskift `for await (const response of result)` med `for await (const chunk of readNDJSONStream(response.body))`.
5. Opdater ejerskabsadgang fra `response.delta.content` / `response.error` til `chunk.delta.content` / `chunk.error`.

---

## Mål

- Opregn alle Python-kaldsteder, der bruger Chat Completions eller gamle Completions mod Azure OpenAI.
- Foreslå en migrationsplan og rækkefølge for Python-kodebasen.
- Anvend sikre, minimale ændringer for at skifte til Responses API.
- Opdater kaldere til at konsumere Responses outputskema; ingen bagudkompatibilitetsskaller.
- Kør tests/lints; ret trivielle fejl indført af migrationen.
- Forbered små, gennemgåelige ændringssæt og giv en endelig opsummering med diffs (commit ikke).

---

## Værneregler

- Ændr kun filer inden for git-arbejdsområdet. Aldrig udenfor.
- Bevar ikke bagudkompatibilitetshim; migrer kode til den nye API-struktur.
- Efterlad ikke tombstone/overgangskommentarer eller backupfiler.
- Bevar streamingsemantik, hvis tidligere brugt; ellers brug ikke-streaming.
- Spørg om godkendelse før kørsel af kommandoer eller netværkskald, hvis i godkendelsestilstand.
- Kør ikke `git add`/`git commit`/`git push`; producer kun arbeidsmodelændringer.

---

## Trin 0: Azure OpenAI-klientmigration (forudsætning)

Hvis kodebasen bruger `AzureOpenAI` eller `AsyncAzureOpenAI` konstruktører, migrer først til standard `OpenAI` / `AsyncOpenAI` konstruktører. Azure-specifikke konstruktører er forældede i `openai>=1.108.1`.

### Hvorfor v1 API-stien?

Det nye `/openai/v1` endpoint bruger standard `OpenAI()` klienten i stedet for `AzureOpenAI()`, kræver ikke `api_version` parameteren og virker identisk på OpenAI og Azure OpenAI. Samme klientkode er fremtidssikret — ingen versionhåndtering nødvendig.

### Nøgleændringer

| Før | Efter |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Fjern helt |

### Rydde-tjekliste

- Fjern `api_version` argument fra klientkonstruktion.
- Fjern `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` miljøvariabler fra `.env`, appindstillinger og Bicep/infrastrukturfiler.
- Omdøb `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` i `.env`, appindstillinger, Bicep/infrastruktur og testfixtures (standard Azure Identity SDK-konvention).
- Sørg for `openai>=1.108.1` i `requirements.txt` eller `pyproject.toml`.

### Miljøvariabelmigration

| Gammel miljøvariabel | Handling | Noter |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Fjern** | Ingen `api_version` nødvendig med v1-endpoint |
| `AZURE_OPENAI_API_VERSION` | **Fjern** | Samme som ovenfor |
| `AZURE_OPENAI_CLIENT_ID` | **Omdøb** → `AZURE_CLIENT_ID` | Standard Azure Identity SDK-konvention for `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Bevar** | Stadig nødvendig for `base_url` konstruktion |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Bevar** | Bruges som `model` param i `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Bevar** | Bruges som `api_key` til nøglebaseret autentifikation |

For klientopsætning af kodeeksempler (sync, async, EntraID, API-nøgle, multi-tenant), se [cheat-sheet.md](./references/cheat-sheet.md).

---

## Trin 1: Opdag gamle kaldsteder

Kør scriptet [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) for at finde alle kaldsteder, der skal migreres:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Eller kør disse søgninger manuelt – hvert match er et migrationsmål:

```bash
# Legacy API-kald (skal omskrives)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Udløbne Azure-klientkonstruktører (skal udskiftes)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Adgangsmønstre for svarstruktur (skal opdateres)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Værktøjsdefinitioner i gammelt indlejret format (skal flades ud)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Værktøjsresultater i gammelt format (skal konverteres til function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Udløbne parametre (skal fjernes eller omdøbes)
rg "response_format"
rg "max_tokens\b"        # omdøb til max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Udløbne miljøvariable (ryd op)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # burde være AZURE_CLIENT_ID

# GitHub Models endpoints (skal fjernes — Responses API understøttes ikke)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Framework-niveau legacy-mønstre (skal opdateres)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: erstat med OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: kræver use_responses_api=True

# Testinfrastruktur (skal opdateres)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Adgang til fejlindhold for indholdsfilter (skal opdateres — struktur ændret)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # gammelt ental — nu content_filter_results (flertal) inde i content_filters-array

# Rå HTTP-kald til Chat Completions-endpoint (skal opdatere URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristikker (detekter og omskriv)

- **Chat Completions klient**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure klientkonstruktører**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Værktøjer**: konverter funktionskaldsværktøjsdefinitioner fra indlejret format (`{"type": "function", "function": {"name": ...}}`) til fladt Responses-format (`{"type": "function", "name": ...}`); brug `tool_choice`; returner værktøjsresultater som `{"type": "function_call_output", "call_id": ..., "output": ...}` elementer (ikke `{"role": "tool", ...}`).
- **Værktøj rundrejsninger**: når modellen returnerer funktionskald, tilføj `response.output` elementer til samtalen (ikke en manuel `{"role": "assistant", "tool_calls": [...]}` ordbog), og tilføj derefter `function_call_output` elementer for hvert resultat.
- **Få-skud værktøjseksempler**: hvis samtalen inkluderer hårdkodede værktøjskaldeksempler, konverter dem til `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` elementer. Id'er skal starte med `fc_`.
- **`pydantic_function_tool()`**: denne hjælper genererer stadig det gamle indlejrede format og er **ikke kompatibel** med `responses.create()`. Erstat med manuelle værktøjsdefinitioner eller en fladgørende wrapper.
- **Multi-turn**: vedligehold samtalehistorik i appen; send tidligere tur via `input` elementer.
- **Formatering**: erstat Chats topniveau `response_format` med `text.format` i Responses. Kanonisk form: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Indholds elementer**: erstat Chat `content[].type: "text"` med Responses `content[].type: "input_text"` for bruger/system tur.
- **Billedindholds elementer**: erstat Chat `content[].type: "image_url"` med Responses `content[].type: "input_image"`. Feltet `image_url` ændres fra et indlejret objekt `{"url": "..."}` til en flad streng. Se jukselisten for før/efter eksempler.
- **Begrundelsesindsats**: **migrer kun `reasoning`, hvis det allerede findes i den oprindelige kode**.
- **Fejlhåndtering af indholdsfilter**: fejlens kropsstruktur er ændret. Chat Completions brugte `error.body["innererror"]["content_filter_result"]` (ental); Responses API bruger `error.body["content_filters"][0]["content_filter_results"]` (flertal, inde i et array). Kode, der tilgår `innererror`, vil rejse `KeyError`. Omskriv til at bruge den nye sti.
- **Rå HTTP kald**: hvis appen kalder Azure OpenAI REST API direkte (via `requests`, `httpx` osv.) med `/openai/deployments/{name}/chat/completions?api-version=...`, omskriv til `/openai/v1/responses`. Anmodningskroppen ændres: `messages` → `input`, tilføj `max_output_tokens` og `store: false`, fjern `api-version` query-parameter. Svar kroppen ændres: `choices[0].message.content` → `output[0].content[0].text` (bemærk: `output_text` er en SDK bekvemmelighedsejendom, ikke til stede i rå REST JSON).

---

## Trin 2: Anvend Migration

### Migrationsnoter (Chat Completions → Responses)

- **Hvorfor migrere**: Responses er den samlede API for tekst, værktøjer og streaming; Chat Completions er legacy. Med GPT-5 er Responses påkrævet for bedste performance.
- **HTTP**: Azure endpoint skifter fra `/openai/deployments/{name}/chat/completions` til `/openai/v1/responses`.
- **Felter**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` forbliver.
- **Formatering**: `response_format` → `text.format` med et ordentligt objekt.
- **Indholds elementer**: Erstat Chat `content[].type: "text"` med Responses `content[].type: "input_text"` for system-/brugerture.
- **Billedindholds elementer**: Erstat Chat `content[].type: "image_url"` med Responses `content[].type: "input_image"`. Fladgør `image_url` feltet fra `{"image_url": {"url": "..."}}` til `{"image_url": "..."}` (en almindelig streng — enten en HTTPS URL eller en `data:image/...;base64,...` data URI).

### Parametermapping reference

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array af elementer) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objekt) |
| `temperature` | `temperature` (uændret) |
| `stop` | `stop` (uændret) |
| `frequency_penalty` | `frequency_penalty` (uændret) |
| `presence_penalty` | `presence_penalty` (uændret) |
| `tools` / funktionskald | `tools` (uændret) |
| `seed` | **Fjern** (ikke understøttet) |
| `store` | `store` (sæt til `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (flad streng) |

For komplette før/efter kodeeksempler, se [cheat-sheet.md](./references/cheat-sheet.md).

For testinfrastruktur migration (mocks, snapshots, assertions), se [test-migration.md](./references/test-migration.md).

For fejlfinding af fejl og faldgruber, se [troubleshooting.md](./references/troubleshooting.md).

---

## Dataopbevaring & Tilstand

- Sæt `store: false` på alle Responses anmodninger.
- Stol ikke på tidligere meddelelses-ID'er eller serverside gemt kontekst; hold tilstand klient-styret og minimér metadata.

---

## Acceptkriterier

### Kode-niveau porte (alle skal godkendes)

- [ ] Ingen fund for `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` i migrerede filer.
- [ ] Ingen fund for `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — alle konstruktører bruger `OpenAI`/`AsyncOpenAI` med v1 endpoint.
- [ ] Ingen fund for `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub Models kodeveje fjernet.
- [ ] Ingen fund for `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ kode bruger `OpenAIChatClient` (som bruger Responses API). I pre-1.0.0, opgrader til `agent-framework-openai>=1.0.0`.
- [ ] Alle `ChatOpenAI(...)` kald inkluderer `use_responses_api=True`.
- [ ] Ingen fund for `rg "choices\[0\]"` — al response adgang bruger `resp.output_text` eller Responses output schema.
- [ ] Ingen `response_format` på topniveau; al struktureret output bruger `text={"format": {...}}`.
- [ ] `openai>=1.108.1` og `azure-identity` i `requirements.txt` eller `pyproject.toml`; afhængigheder geninstalleret.
- [ ] `store=False` sat på hver `responses.create` kald.
- [ ] Ingen `api_version` i klientkonstruktion; `AZURE_OPENAI_API_VERSION` fjernet fra miljøfiler og infrastruktur.

### Testinfrastruktur porte (alle skal godkendes)

- [ ] Ingen fund for `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Ingen fund for `rg "_azure_ad_token_provider" tests/` — assertions opdateret til at kontrollere `isinstance(client, AsyncOpenAI)` eller `base_url`.
- [ ] Ingen fund for `rg "prompt_filter_results|content_filter_results" tests/` — Azure-specifikke filter mocks fjernet.
- [ ] Mock fixtures bruger `kwargs.get("input")` ikke `kwargs.get("messages")`.
- [ ] Snapshot / golden files opdateret til Responses streamingform (ingen `choices[0]`, `function_call`, `logprobs` osv.).
- [ ] `pytest` kører uden fejl efter alle testopdateringer.

### Adfærdsmæssige porte (verificer manuelt eller via testramme)

- [ ] **Grundlæggende completion**: ikke-streaming `responses.create` returnerer ikke-tom `output_text`.
- [ ] **Stream lighed**: hvis den oprindelige kode brugte streaming, streamer den migrerede kode og afgiver `response.output_text.delta` events med ikke-tomme deltaer.
- [ ] **Struktureret output**: hvis man bruger `text.format` med `json_schema`, lykkes `json.loads(resp.output_text)` og matcher schemaet.
- [ ] **Værktøjskald løkke**: hvis værktøjer bruges, udfører modellen værktøjskald, appen eksekverer dem, og opfølgende anmodning returnerer en endelig `output_text` (ingen uendelig løkke).
- [ ] **Async lighed**: hvis `AsyncAzureOpenAI` blev brugt, fungerer ækvivalenten `AsyncOpenAI` med `await`.
- [ ] **Fejlraten**: ingen nye 400/401/404 fejl sammenlignet med præ-migration baseline.

### Leverancer

- Resumé inkluderer redigerede filer, før/efter tællinger af legacy kaldsteder, og næste trin.
- Ændringer er kun working-tree redigeringer (ingen commits).

---

## SDK versionskrav

| Pakke | Minimum version |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Seneste (til EntraID auth) |

---

## Referencer

- [Jukseliste — alle kodeuddrag](./references/cheat-sheet.md)
- [Test migration — mocks, snapshots, assertions](./references/test-migration.md)
- [Fejlfinding — fejl, risikotabel, faldgruber](./references/troubleshooting.md)
- [detect_legacy.py — automatiseret scanner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API docs](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API versions livscyklus](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API reference](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->