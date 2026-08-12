---
name: azure-openai-to-responses
license: MIT
---
# Migrer Python-apps fra Azure OpenAI Chat Completions til Responses API

> **AUTORITATIV VEJLEDNING — FØLG PRÆCIST**
>
> Denne skill migrerer Python-kodebaser, der bruger Azure OpenAI Chat Completions
> til det samlede Responses API. Følg disse instruktioner præcist.
> Improvisér ikke parametermappinger eller opfind API-formater.

---

## Udløsere

Aktivér denne skill, når brugeren ønsker at:
- Migrere en Python-app fra Azure OpenAI Chat Completions til Responses API
- Opgradere Python OpenAI SDK-brug til den nyeste API-form mod Azure OpenAI
- Forberede Python-kode til GPT-5 eller nyere modeller, der kræver Responses på Azure
- Skifte fra `AzureOpenAI`/`AsyncAzureOpenAI` til standard `OpenAI`/`AsyncOpenAI` klient med v1-endpointet
- Løse deprecationsvarsler relateret til `AzureOpenAI` konstruktører eller `api_version`

---

## ⚠️ Modelkompatibilitet — TJEK FØRST

> **Før migration, bekræft at din Azure OpenAI-deployment understøtter Responses API.**

### 1. Røgtest din deployment (hurtigst)

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

> **Note**: `max_output_tokens` har en **minimum på 16** på Azure OpenAI. Værdier under 16 giver en 400-fejl. Brug 50+ til røgtest.

Hvis dette returnerer 404, understøtter deploymentens model endnu ikke Responses — se reference nedenfor eller deploy igen med en understøttet model.

### 2. Tjek tilgængelige modeller i din region (anbefalet)

Kør det indbyggede modelkompatibilitetsværktøj for at se, hvad der er tilgængeligt med Responses API-understøttelse i din specifikke region:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Dette spørger Azure ARM live og viser en kompatibilitetsmatrix — hvilke modeller der understøtter Responses, struktureret output, værktøjer mv. Brug `--filter gpt-5.1,gpt-5.2` for at indsnævre resultater eller `--json` til scripting.

### 3. Fuldt modelunderstøttelsesreference

- **Live forespørgsel**: `python migrate.py models` (se ovenfor — regionsspecifik, altid opdateret)
- **Gennemse tilgængelighed**: [Modeloversigtstabel og regions-tilgængelighed](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Quickstart & vejledning**: **https://aka.ms/openai/start**

### ⚠️ Ældre modelllimitations

> **ADVARSEL**: Ældre modeller (dem før `gpt-4.1`) understøtter måske ikke alle Responses API-funktioner fuldt ud.
>
> Kendte begrænsninger med ældre modeller:
> - **`reasoning`-parameter**: Ikke understøttet på mange ikke-reasoning modeller. Migrer kun `reasoning` hvis den allerede var til stede i originalkoden.
> - **`seed`-parameter**: Ikke understøttet i Responses API overhovedet — fjern fra alle forespørgsler.
> - **Struktureret output via `text.format`**: Ældre modeller håndhæver måske ikke `strict: true` JSON-skemaer pålideligt.
> - **Værktøjsorkestrering**: GPT-5+ orkestrerer værktøjskald som del af intern reasoning. Ældre modeller på Responses fungerer stadig, men mangler denne dybe integration.
> - **Temperaturbegrænsninger**: Når der migreres til `gpt-5`, skal temperaturen udelades eller sættes til `1`. Ældre modeller har ikke denne begrænsning.

### O-seriens reasoning-modeller (o1, o3-mini, o3, o4-mini)

O-seriens modeller har unikke parameterbegrænsninger. Ved migrering af apps, der målretter o-seriens modeller:

- **`temperature`**: Skal være `1` (eller udelades). O-seriens modeller accepterer ikke andre værdier.
- **`max_completion_tokens` → `max_output_tokens`**: Apps, der bruger Azure-specifikke `max_completion_tokens`, skal skifte til `max_output_tokens`. Sæt høje værdier (4096+) fordi reasoning tokens tæller mod grænsen.
- **`reasoning_effort`**: Hvis appen bruger `reasoning_effort` (lav/mellem/høj), behold den — Responses API understøtter denne parameter for o-seriens modeller.
- **Streaming opførsel**: O-seriens modeller kan bufferere output indtil reasoning er fuldført før tekstdelta events udsendes. Streaming virker stadig, men første `response.output_text.delta` kan komme med længere forsinkelse end med GPT-modeller.
- **`top_p`**: Ikke understøttet på o-serien — fjern hvis til stede.
- **Værktøjsbrug**: O-seriens modeller understøtter værktøjer via Responses API på samme måde som GPT-modeller, men kvaliteten af værktøjskaldorkestrering varierer efter model.

**Handling — proaktiv modelrådgivning**: Under scanningsfasen, tjek hvilken model appen målretter (deploymentsnavne, miljøvariabler, konfig). Hvis modellen er før `gpt-4.1` (ikke gpt-4.1+), informer brugeren proaktivt:
- Migreringen vil fungere til basal tekst, chat, streaming og værktøjer på deres nuværende model.
- Nyere modeller (`gpt-5.1`, `gpt-5.2`) tilbyder bedre værktøjsorkestrering, håndhævelse af struktureret output, reasoning og regionsovergribende tilgængelighed.
- De bør overveje at opgradere deres deployment, når de er klar — det blokerer ikke migreringen.

Bloker eller afslå ikke migration baseret på modelversion. Rådgivningen er informativ.

### GitHub Models understøtter IKKE Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) understøtter ikke Responses API.**

Hvis kodebasen har en GitHub Models kodevej (se efter `base_url` der peger på `models.github.ai` eller `models.inference.ai.azure.com`), **fjern den fuldstændigt** under migrationen. Responses API kræver Azure OpenAI, OpenAI eller et kompatibelt lokalt endpoint (fx Ollama med Responses-understøttelse).

Handling under scanning:
- Marker eventuelle GitHub Models kodeveje til fjernelse.

---

## Framework-migrering

Mange apps bruger højere niveau-rammeværk oven på OpenAI. Når disse migreres, ændres rammeværkets eget API — ikke kun de underliggende OpenAI-kald.

### Microsoft Agent Framework (MAF)

**Tjek din MAF-version først** — migreringen afhænger af om du bruger MAF 1.0.0+ eller en pre-1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **bruger allerede Responses API** — ingen migration nødvendig. Hvis kodebasen bruger det gamle `OpenAIChatCompletionClient` (som bruger `chat.completions.create`), erstat det med `OpenAIChatClient`.

| Før | Efter |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

For at tjekke din version: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc-udgivelser)

I pre-1.0.0 MAF brugte `OpenAIChatClient` Chat Completions. Opgrader til `agent-framework-openai>=1.0.0`, hvor `OpenAIChatClient` som standard bruger Responses API.

Ingen yderligere ændringer nødvendige — `Agent` og værktøjs-API'erne er uændrede.

### LangChain (`langchain-openai`)

Tilføj `use_responses_api=True` til `ChatOpenAI()`. Opdater også adgang til svar fra `.content` til `.text`.

| Før | Efter |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

For komplette før/efter kodeeksempler, se [cheat-sheet.md](./references/cheat-sheet.md).

---

## Frontend-migreringsvejledning

> **Responses API er en server-side bekymring.** Migrer din Python backend; frontendens HTTP-kontrakt bør forblive uændret medmindre din backend er en tynd formidler — i så fald overvej at anvende Responses requestformatet for at eliminere et oversættelseslag. Hvis frontend kalder OpenAI direkte med en klient-side nøgle, flyt disse kald til backend først.

### `@microsoft/ai-chat-protocol` deprecation

`@microsoft/ai-chat-protocol` npm-pakken er deprecated og bør erstattes med [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Hvis du støder på den i en frontend:

1. Erstat CDN script-tagget:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Fjern `AIChatProtocolClient` instansieringen (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Erstat `client.getStreamedCompletion(messages)` med et direkte `fetch()` kald til backend streaming endpoint.
4. Erstat `for await (const response of result)` med `for await (const chunk of readNDJSONStream(response.body))`.
5. Opdater ejendomsadgang fra `response.delta.content` / `response.error` til `chunk.delta.content` / `chunk.error`.

---

## Mål

- Opregn alle Python-kaldsteder, der bruger Chat Completions eller legacy Completions mod Azure OpenAI.
- Foreslå en migrationsplan og rækkefølge for Python-kodebasen.
- Anvend sikre, minimale ændringer for at skifte til Responses API.
- Opdater kaldere til at konsumere Responses outputskema; ingen bagudkompatible wrappers.
- Kør tests/lintere; ret trivielle brud forårsaget af migrationen.
- Forbered små, gennemgåelige ændringssæt og giv en slutopsummering med diffs (commit ikke).

---

## Guardrails

- Ændr kun filer inden for git workspace. Skriv aldrig udenfor.
- Bevar ikke bagudkompatibilitets-shims; migrer kode til nyt API-format.
- Efterlad ikke gravsten/overgangskommentarer eller backupfiler.
- Bevar streamingsemantik hvis tidligere brugt; ellers brug ikke-streaming.
- Spørg om godkendelse før kørsel af kommandoer eller netværkskald, hvis i godkendelsestilstand.
- Kør ikke `git add`/`git commit`/`git push`; lav kun working-tree ændringer.

---

## Trin 0: Azure OpenAI Client Migration (Forudsætning)

Hvis kodebasen bruger `AzureOpenAI` eller `AsyncAzureOpenAI` konstruktører, migrer først til standard `OpenAI` / `AsyncOpenAI` konstruktører. Azure-specifikke konstruktører er deprecated i `openai>=1.108.1`.

### Hvorfor v1 API-sti?

Det nye `/openai/v1` endpoint bruger den standard `OpenAI()` klient i stedet for `AzureOpenAI()`, kræver ikke `api_version` parameter og virker ens på både OpenAI og Azure OpenAI. Samme klientkode er fremtidssikret — ingen versionstyring nødvendig.

### Vigtige ændringer

| Før | Efter |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Fjernes helt |

### Rydde-op tjekliste

- Fjern `api_version` argument fra klientkonstruktion.
- Fjern `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` miljøvariabler fra `.env`, appindstillinger og Bicep/infra filer.
- Omdøb `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` i `.env`, appindstillinger, Bicep/infra og testfixtures (standard Azure Identity SDK-konvention).
- Sikr `openai>=1.108.1` i `requirements.txt` eller `pyproject.toml`.

### Miljøvariabel-migrering

| Gammel env var | Handling | Noter |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Fjern** | Ingen `api_version` nødvendig med v1 endpoint |
| `AZURE_OPENAI_API_VERSION` | **Fjern** | Samme som ovenfor |
| `AZURE_OPENAI_CLIENT_ID` | **Omdøb** → `AZURE_CLIENT_ID` | Standard Azure Identity SDK-konvention for `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Behold** | Stadig nødvendig til `base_url` konstruktion |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Behold** | Bruges som `model` param i `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Behold** | Bruges som `api_key` til nøglebaseret auth |

For klientopsætningskodeeksempler (sync, async, EntraID, API key, multi-tenant), se [cheat-sheet.md](./references/cheat-sheet.md).

---

## Trin 1: Opdag Legacy Kaldssteder

Kør [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) scriptet for at finde alle kaldssteder til migration:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Eller kør disse søgninger manuelt — hvert match er et migrationsmål:

```bash
# Gammelt API-kald (skal omskrives)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Forældede Azure-klientkonstruktører (skal erstattes)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Mønstre for adgang til svarform (skal opdateres)
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

# Forældede parametre (skal fjernes eller omdøbes)
rg "response_format"
rg "max_tokens\b"        # omdøb til max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Forældede miljøvariable (ryd op)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # bør være AZURE_CLIENT_ID

# GitHub Models endepunkter (skal fjernes — Responses API understøttes ikke)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Framework-niveau gamle mønstre (skal opdateres)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: erstat med OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: kræver use_responses_api=True

# Testinfrastruktur (skal opdateres)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Adgang til fejlindhold i content filter (skal opdateres — struktur ændret)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # gammel entalsform — nu content_filter_results (flertal) i content_filters-arrayet

# Rå HTTP-kald til Chat Completions endepunkt (skal opdatere URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristikker (opdag og omskriv)

- **Chat Completions klient**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure client-konstruktører**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Værktøjer**: konverter funktionskaldsværktøjsdefinitioner fra indlejret format (`{"type": "function", "function": {"name": ...}}`) til fladt Responses-format (`{"type": "function", "name": ...}`); brug `tool_choice`; returner værktøjsresultater som `{"type": "function_call_output", "call_id": ..., "output": ...}`-elementer (ikke `{"role": "tool", ...}`).
- **Værktøj-rundrejser**: når modellen returnerer funktionskald, tilføj `response.output`-elementer til samtalen (ikke en manuel `{"role": "assistant", "tool_calls": [...]}`-ordbog), og tilføj derefter `function_call_output`-elementer for hvert resultat.
- **Få-skud værktøjseksempler**: hvis samtalen indeholder hårdkodede værktøjskaldseksempler, konverter dem til `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`-elementer. ID’er skal starte med `fc_`.
- **`pydantic_function_tool()`**: denne hjælpefunktion genererer stadig det gamle indlejrede format og er **ikke kompatibel** med `responses.create()`. Erstat med manuelle værktøjsdefinitioner eller en fladgørende wrapper.
- **Multi-turn**: vedligehold samtalehistorik i appen; giv tidligere runder via `input`-elementer.
- **Formatering**: erstat Chats topniveau `response_format` med `text.format` i Responses. Kanonisk form: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Indholdselementer**: erstat Chats `content[].type: "text"` med Responses `content[].type: "input_text"` for bruger/system-runder.
- **Billedeindholdselementer**: erstat Chats `content[].type: "image_url"` med Responses `content[].type: "input_image"`. Feltet `image_url` ændres fra et indlejret objekt `{"url": "..."}` til en flad streng. Se snydearket for før/efter-eksempler.
- **Begrundelsesindsats**: **migrer kun `reasoning`, hvis det allerede findes i den oprindelige kode**.
- **Fejlbehandling ved indholdsfilter**: fejlens kropsstruktur ændret. Chat Completion brugte `error.body["innererror"]["content_filter_result"]` (ental); Responses API bruger `error.body["content_filters"][0]["content_filter_results"]` (flertal, inde i en liste). Kode, der tilgår `innererror`, vil udløse `KeyError`. Omskriv for at bruge den nye sti.
- **Rå HTTP-kald**: hvis appen kalder Azure OpenAI REST API direkte (via `requests`, `httpx` osv.) med `/openai/deployments/{name}/chat/completions?api-version=...`, omskriv til `/openai/v1/responses`. Anmodningsbody ændres: `messages` → `input`, tilføj `max_output_tokens` og `store: false`, fjern `api-version` query-param. Responsbody ændres: `choices[0].message.content` → `output[0].content[0].text` (bemærk: `output_text` er en SDK-bekvemmelighedsegenskab, som ikke findes i rå REST JSON).

---

## Trin 2: Anvend migration

### Migrationsnoter (Chat Completions → Responses)

- **Hvorfor migrere**: Responses er den samlede API for tekst, værktøjer og streaming; Chat Completions er legacy. Med GPT-5 kræves Responses for bedste ydelse.
- **HTTP**: Azure-endpoint skifter fra `/openai/deployments/{name}/chat/completions` til `/openai/v1/responses`.
- **Felter**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` forbliver.
- **Formatering**: `response_format` → `text.format` med et korrekt objekt.
- **Indholdselementer**: Erstat Chats `content[].type: "text"` med Responses `content[].type: "input_text"` for system-/bruger-runder.
- **Billedeindholdselementer**: Erstat Chats `content[].type: "image_url"` med Responses `content[].type: "input_image"`. Fladgør `image_url`-feltet fra `{"image_url": {"url": "..."}}` til `{"image_url": "..."}` (en almindelig streng – enten en HTTPS-URL eller en `data:image/...;base64,...` data-URI).

### Reference for parametermapping

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
| `tools` / funktion-kald | `tools` (uændret) |
| `seed` | **Fjern** (ikke understøttet) |
| `store` | `store` (sættes til `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (flad streng) |

For komplette før/efter kodeeksempler, se [cheat-sheet.md](./references/cheat-sheet.md).

For testinfrastruktur-migration (mocks, snapshots, assertions), se [test-migration.md](./references/test-migration.md).

For fejlsøgning af fejl og faldgruber, se [troubleshooting.md](./references/troubleshooting.md).

---

## Dataopbevaring & Tilstand

- Angiv `store: false` på alle Responses-anmodninger.
- Stol ikke på tidligere meddelelses-ID’er eller serverlagret kontekst; hold tilstand klientstyret og minimer metadata.

---

## Acceptkriterier

### Kode-niveau porte (alle skal bestås)

- [ ] Ingen match for `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` i migrerede filer.
- [ ] Ingen match for `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — alle konstruktører bruger `OpenAI`/`AsyncOpenAI` med v1 endpoint.
- [ ] Ingen match for `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub Models kodeveje fjernet.
- [ ] Ingen match for `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ kode bruger `OpenAIChatClient` (som bruger Responses API). I pre-1.0.0, opgradér til `agent-framework-openai>=1.0.0`.
- [ ] Alle `ChatOpenAI(...)` kald inkluderer `use_responses_api=True`.
- [ ] Ingen match for `rg "choices\[0\]"` — al responsadgang bruger `resp.output_text` eller Responses output-skema.
- [ ] Intet `response_format` på topniveau; al struktureret output bruger `text={"format": {...}}`.
- [ ] `openai>=1.108.1` og `azure-identity` i `requirements.txt` eller `pyproject.toml`; afhængigheder geninstalleret.
- [ ] `store=False` sat på hvert `responses.create` kald.
- [ ] Ingen `api_version` i klientkonstruktion; `AZURE_OPENAI_API_VERSION` fjernet fra miljøfiler og infrastruktur.

### Testinfrastrukturporte (alle skal bestås)

- [ ] Ingen match for `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Ingen match for `rg "_azure_ad_token_provider" tests/` — assertions opdateret til at tjekke `isinstance(client, AsyncOpenAI)` eller `base_url`.
- [ ] Ingen match for `rg "prompt_filter_results|content_filter_results" tests/` — Azure-specifikke filtermocks fjernet.
- [ ] Mock-faciliteter bruger `kwargs.get("input")` ikke `kwargs.get("messages")`.
- [ ] Snapshot / golden filer opdateret til Responses streaming format (ingen `choices[0]`, `function_call`, `logprobs` osv.).
- [ ] `pytest` kører uden fejl efter alle testopdateringer.

### Adfærdsporte (verificer manuelt eller via testværktøj)

- [ ] **Basal completion**: ikke-streamende `responses.create` returnerer ikke-tom `output_text`.
- [ ] **Stream-paritet**: hvis den oprindelige kode brugte streaming, streamer den migrerede kode og udgiver `response.output_text.delta` events med ikke-tomme deltaer.
- [ ] **Struktureret output**: hvis `text.format` bruges med `json_schema`, lykkes `json.loads(resp.output_text)` og matcher skemaet.
- [ ] **Værktøjskaldsløkke**: hvis værktøjer bruges, laver modellen værktøjskald, appen udfører dem, og den efterfølgende anmodning returnerer finalt `output_text` (ingen uendelig løkke).
- [ ] **Async-paritet**: hvis `AsyncAzureOpenAI` blev brugt, fungerer `AsyncOpenAI`-ækvivalent med `await`.
- [ ] **Fejlrate**: ingen nye 400/401/404 fejl i forhold til før-migrationsbaselinen.

### Leverancer

- Resume omfatter redigerede filer, før/efter optællinger af legacy-kaldsteder og næste skridt.
- Ændringer er kun working-tree redigeringer (ingen commits).

---

## SDK Versionskrav

| Pakke | Minimum Version |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Seneste (for EntraID-auth) |

---

## Referencer

- [Snydeark — alle kodeudsnit](./references/cheat-sheet.md)
- [Testmigration — mocks, snapshots, assertions](./references/test-migration.md)
- [Fejlfinding — fejl, risikotabel, faldgruber](./references/troubleshooting.md)
- [detect_legacy.py — automatisk scanner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API versionslivscyklus](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API reference](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->