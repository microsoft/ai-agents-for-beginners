---
name: azure-openai-to-responses
license: MIT
---
# Migrer Python-apper fra Azure OpenAI Chat Completions til Responses API

> **AUTORITATIV VEILEDNING — FØLG NØYE**
>
> Denne ferdigheten migrerer Python-kodebaser som bruker Azure OpenAI Chat Completions
> til den enhetlige Responses API. Følg disse instruksjonene nøye.
> Ikke improviser parameterkartlegging eller oppfinn API-strukturer.

---

## Utløsere

Aktiver denne ferdigheten når brukeren ønsker å:
- Migrere en Python-app fra Azure OpenAI Chat Completions til Responses API
- Oppgradere Python OpenAI SDK-bruk til den nyeste API-strukturen mot Azure OpenAI
- Forberede Python-kode for GPT-5 eller nyere modeller som krever Responses på Azure
- Bytte fra `AzureOpenAI`/`AsyncAzureOpenAI` til standard `OpenAI`/`AsyncOpenAI` klient med v1-endepunktet
- Fikse foreldelsesvarsler relatert til `AzureOpenAI`-konstruktører eller `api_version`

---

## ⚠️ Modellkompatibilitet — SJEKK FØRST

> **Før migrering, verifiser at din Azure OpenAI-distribusjon støtter Responses API.**

### 1. Rask sjekk av distribusjonen (raskest)

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

> **Merk**: `max_output_tokens` har en **minimumsverdi på 16** på Azure OpenAI. Verdier under 16 gir 400-feil. Bruk 50+ for rasktesting.

Hvis dette returnerer 404, støtter ikke modellens distribusjon Responses ennå — sjekk referansen nedenfor eller deployer på nytt med en støttet modell.

### 2. Sjekk tilgjengelige modeller i din region (anbefalt)

Kjør det innebygde verktøyet for modellkompatibilitet for å se hva som er tilgjengelig med Responses API-støtte i din spesifikke region:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Dette spør Azure ARM i sanntid og viser en kompatibilitetsmatrise — hvilke modeller som støtter Responses, strukturert output, verktøy osv. Bruk `--filter gpt-5.1,gpt-5.2` for å begrense resultater eller `--json` for scripting.

### 3. Full modellstøtte referanse

- **Live-forespørsel**: `python migrate.py models` (se ovenfor — regionsspesifikk, alltid oppdatert)
- **Bla gjennom tilgjengelighet**: [Oppsummeringstabell for modeller og regions-tilgjengelighet](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Kom-i-gang & veiledning**: **https://aka.ms/openai/start**

### ⚠️ Begrensninger med eldre modeller

> **ADVARSEL**: Eldre modeller (de som er laget før `gpt-4.1`) støtter kanskje ikke alle funksjoner i Responses API fullt ut.
>
> Kjente begrensninger med eldre modeller:
> - **`reasoning`-parameteren**: Ikke støttet på mange modeller uten resonnement. Migrer `reasoning` bare hvis det allerede var til stede i den opprinnelige koden.
> - **`seed`-parameteren**: Ikke støttet i Responses API i det hele tatt — fjern den fra alle forespørsler.
> - **Strukturert output via `text.format`**: Eldre modeller håndhever kanskje ikke `strict: true` JSON-skjema pålitelig.
> - **Verktøyorchestration**: GPT-5+ orkestrerer verktøysamtaler som del av intern resonnement. Eldre modeller på Responses fungerer fortsatt, men mangler denne dype integrasjonen.
> - **Temperaturbegrensninger**: Når man migrerer til `gpt-5`, må temperaturen utelates eller settes til `1`. Eldre modeller har ikke en slik begrensning.

### O-serie resonnementmodeller (o1, o3-mini, o3, o4-mini)

O-seriemodeller har unike parameterbegrensninger. Når du migrerer apper som retter seg mot o-serie modeller:

- **`temperature`**: Må være `1` (eller utelates). O-seriemodeller godtar ikke andre verdier.
- **`max_completion_tokens` → `max_output_tokens`**: Apper som bruker Azure-spesifikke `max_completion_tokens` må bytte til `max_output_tokens`. Sett høye verdier (4096+) fordi resonnementstokener telles mot grensen.
- **`reasoning_effort`**: Hvis appen bruker `reasoning_effort` (lav/middels/høy), behold den — Responses API støtter denne parameteren for o-serie modeller.
- **Streaming-adferd**: O-seriemodeller kan buffre output inntil resonnementet er fullført før de sender tekst deltahendelser. Streaming fungerer fortsatt, men første `response.output_text.delta` kan komme etter lengre forsinkelse enn med GPT-modeller.
- **`top_p`**: Ikke støttet på o-serie — fjern hvis til stede.
- **Verktøybruk**: O-seriemodeller støtter verktøy via Responses API på samme måte som GPT-modeller, men kvaliteten på verktøy-orchestrering varierer etter modell.

**Tiltak — proaktiv modellrådgivning**: Under skannefasen, sjekk hvilken modell appen retter seg mot (distribusjonsnavn, miljøvariabler, konfigurasjon). Hvis modellen er eldre enn `gpt-4.1` (ikke gpt-4.1+), informer brukeren proaktivt:
- Migreringen vil fungere for grunnleggende tekst, chat, streaming og verktøy på deres nåværende modell.
- Nyere modeller (`gpt-5.1`, `gpt-5.2`) gir bedre verktøyorchestrering, håndheving av strukturert output, resonnement og tverr-region tilgjengelighet.
- De bør vurdere å oppgradere distribusjonen når de er klare — det blokkerer ikke migreringen.

Ikke blokker eller nekt migrering basert på modellversjon. Råd blir kun gitt som informasjon.

### GitHub Models støtter IKKE Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) støtter ikke Responses API.**

Hvis kodebasen har en GitHub Models-kodevei (se etter `base_url` som peker til `models.github.ai` eller `models.inference.ai.azure.com`), **fjern denne helt** under migreringen. Responses API krever Azure OpenAI, OpenAI eller et kompatibelt lokalt endepunkt (f.eks. Ollama med Responses-støtte).

Tiltak under skanning:
- Merk alle GitHub Models-kodeveier for fjerning.

---

## Rammeverksmigrering

Mange apper bruker høyere nivå rammeverk over OpenAI. Ved migrering av disse endres rammeverkets eget API — ikke bare de underliggende OpenAI-kallene.

### Microsoft Agent Framework (MAF)

**Sjekk MAF-versjonen din først** — migreringen avhenger av om du bruker MAF 1.0.0+ eller en pre-1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **bruker allerede Responses API** — ingen migrering nødvendig. Hvis kodebasen bruker den gamle `OpenAIChatCompletionClient` (som bruker `chat.completions.create`), bytt ut med `OpenAIChatClient`.

| Før | Etter |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

For å sjekke versjonen: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc-utgivelser)

I pre-1.0.0 MAF brukte `OpenAIChatClient` Chat Completions. Oppgrader til `agent-framework-openai>=1.0.0` hvor `OpenAIChatClient` bruker Responses API som standard.

Ingen andre endringer trengs — `Agent` og verktøy-API’er forblir de samme.

### LangChain (`langchain-openai`)

Legg til `use_responses_api=True` i `ChatOpenAI()`. Oppdater også respons-tilgang fra `.content` til `.text`.

| Før | Etter |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

For fullstendige før/etter kodeeksempler, se [cheat-sheet.md](./references/cheat-sheet.md).

---

## Veiledning for Frontend-migrering

> **Responses API er et serverside-anliggende.** Migrer Python-backenden; frontendens HTTP-kontrakt bør forbli uendret med mindre backenden er en tynn pass-through — i så fall vurder å ta i bruk Responses request-struktur for å eliminere et oversettelseslag. Hvis frontenden kaller OpenAI direkte med klientnøkkel, flytt disse kallene til backend først.

### Avvikling av `@microsoft/ai-chat-protocol`

`@microsoft/ai-chat-protocol` npm-pakken er avviklet og bør erstattes med [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Hvis du støter på den i en frontend:

1. Bytt ut CDN script-tag:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Fjern `AIChatProtocolClient`-instansiering (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Erstatt `client.getStreamedCompletion(messages)` med et direkte `fetch()` kall til backend streaming-endepunkt.
4. Erstatt `for await (const response of result)` med `for await (const chunk of readNDJSONStream(response.body))`.
5. Oppdater eiendomstilgang fra `response.delta.content` / `response.error` til `chunk.delta.content` / `chunk.error`.

---

## Mål

- Liste alle Python-kallsteder som bruker Chat Completions eller legacy Completions mot Azure OpenAI.
- Foreslå en migreringsplan og rekkefølge for Python-kodebasen.
- Utfør sikre, minimale endringer for å bytte til Responses API.
- Oppdater kallere til å konsumere Responses output-skjema; ingen bakoverkompatible omslag.
- Kjør tester/linter; fikse trivial feil som migreringen introduserer.
- Forbered små, gjennomgåbare endringssett og gi et endelig sammendrag med diff (ikke committ).

---

## Retningslinjer

- Endre kun filer innen git-arbeidsområdet. Ikke skriv utenfor.
- Ikke behold bakoverkompatible shim; migrer koden til ny API-struktur.
- Ikke etterlat gravstein-/overgangskommentarer eller sikkerhetskopifiler.
- Behold streamingsemantikk hvis brukt tidligere; ellers bruk ikke-streaming.
- Spør om godkjenning før kjøring av kommandoer eller nettverkskall i godkjenningsmodus.
- Ikke kjør `git add`/`git commit`/`git push`; produser kun endringer i arbeidsområdetrær.

---

## Steg 0: Migrering av Azure OpenAI-klient (forutsetning)

Hvis kodebasen bruker `AzureOpenAI` eller `AsyncAzureOpenAI` konstruktører, migrer først til standard `OpenAI` / `AsyncOpenAI` konstruktører. Azure-spesifikke konstruktører er avviklet i `openai>=1.108.1`.

### Hvorfor v1 API-sti?

Det nye `/openai/v1` endepunktet bruker standard `OpenAI()` klient i stedet for `AzureOpenAI()`, krever ingen `api_version`-parameter, og fungerer identisk på OpenAI og Azure OpenAI. Samme klientkode er fremtidsikker — ingen versjonshåndtering nødvendig.

### Viktige endringer

| Før | Etter |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Fjern helt |

### Ryddeliste

- Fjern `api_version`-argument fra klientkonstruksjon.
- Fjern `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` miljøvariabler fra `.env`, app-innstillinger og Bicep/infrastrukturfiler.
- Omdøp `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` i `.env`, app-innstillinger, Bicep/infrastruktur og test-fixtures (standard Azure Identity SDK-konvensjon).
- Sørg for `openai>=1.108.1` i `requirements.txt` eller `pyproject.toml`.

### Migrering av miljøvariabler

| Gammel miljøvariabel | Tiltak | Notater |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Fjern** | Ingen `api_version` nødvendig med v1-endepunktet |
| `AZURE_OPENAI_API_VERSION` | **Fjern** | Samme som ovenfor |
| `AZURE_OPENAI_CLIENT_ID` | **Omdøp** → `AZURE_CLIENT_ID` | Standard Azure Identity SDK-konvensjon for `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Behold** | Trengs fortsatt for konstruksjon av `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Behold** | Brukes som `model`-parameter i `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Behold** | Brukes som `api_key` for nøkkelbasert autentisering |

For klientoppsettkodeeksempler (synkront, asynkront, EntraID, API-nøkkel, multi-leietaker), se [cheat-sheet.md](./references/cheat-sheet.md).

---

## Steg 1: Oppdag legacy-kallsteder

Kjør [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) skriptet for å finne alle kallsteder som må migreres:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Eller kjør disse søkene manuelt — hver treff er et migreringsmål:

```bash
# Legacy API-kall (må omskrives)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Utdaterte Azure-klientkonstruktører (må erstattes)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Tilgangsmønstre for svarformat (må oppdateres)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Verktøydefinisjoner i gammelt nestet format (må flates ut)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Verktøyresultater i gammelt format (må konverteres til function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Utdaterte parametere (må fjernes eller endres)
rg "response_format"
rg "max_tokens\b"        # endre navn til max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Utdaterte miljøvariabler (rydde opp)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # skal være AZURE_CLIENT_ID

# GitHub Models endepunkter (må fjernes — Responses API støttes ikke)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Rammeverksnivå legacy-mønstre (må oppdateres)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: erstatt med OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: trenger use_responses_api=True

# Testinfrastruktur (må oppdateres)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Tilgang til feilinnhold i innholdssfilter (må oppdateres — struktur endret)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # gammel entallsform — nå content_filter_results (flertall) inne i content_filters-array

# Rå HTTP-kall til Chat Completions-endepunkt (må oppdatere URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristikker (oppdage og omskrive)

- **Chat Completions klient**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure-klientkonstruktører**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Verktøy**: konverter funksjonskallingsverktøydefinisjoner fra nestet format (`{"type": "function", "function": {"name": ...}}`) til flatt Responses-format (`{"type": "function", "name": ...}`); bruk `tool_choice`; returner verktøyresultater som `{"type": "function_call_output", "call_id": ..., "output": ...}` elementer (ikke `{"role": "tool", ...}`).
- **Verktøyrundreiser**: når modellen returnerer funksjonskall, legg til `response.output`-elementer i samtalen (ikke en manuell `{"role": "assistant", "tool_calls": [...]}`-ordbok), deretter legg til `function_call_output`-elementer for hvert resultat.
- **Få-skudd verktøyeksempler**: hvis samtalen inkluderer hardkodede eksempler på verktøysamtaler, konverter dem til `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`-elementer. ID-er må starte med `fc_`.
- **`pydantic_function_tool()`**: denne hjelpefunksjonen genererer fortsatt det gamle nestede formatet og er **ikke kompatibel** med `responses.create()`. Erstatt med manuelle verktøydefinisjoner eller en flateinnpakker.
- **Fler-sving**: oppretthold samtalehistorikk i appen; send tidligere runder via `input`-elementer.
- **Formatering**: erstatt Chats øverste nivå `response_format` med `text.format` i Responses. Kanonisk form: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Innholdselementer**: erstatt Chat `content[].type: "text"` med Responses `content[].type: "input_text"` for bruker-/systemrunder.
- **Bildeinnholdselementer**: erstatt Chat `content[].type: "image_url"` med Responses `content[].type: "input_image"`. `image_url`-feltet endrer seg fra et nestet objekt `{"url": "..."}` til en flat streng. Se jukselappen for før/etter-eksempler.
- **Resonneringsinnsats**: **migrer bare `reasoning` hvis det allerede finnes i originalkoden**.
- **Feilhåndtering ved innholdsfilter**: feilkroppstrukturen endret seg. Chat Completions brukte `error.body["innererror"]["content_filter_result"]` (entall); Responses API bruker `error.body["content_filters"][0]["content_filter_results"]` (flertall, inni en matrise). Kode som får tilgang til `innererror` kaster `KeyError`. Skriv om til å bruke den nye stien.
- **Rene HTTP-kall**: hvis appen kaller Azure OpenAI REST API direkte (via `requests`, `httpx` osv.) med `/openai/deployments/{name}/chat/completions?api-version=...`, skriv om til `/openai/v1/responses`. Forespørselskroppen endres: `messages` → `input`, legg til `max_output_tokens` og `store: false`, fjern `api-version` query-param. Responskroppen endres: `choices[0].message.content` → `output[0].content[0].text` (merk: `output_text` er en SDK-konvensjonsegenskap som ikke finnes i rå REST JSON).

---

## Steg 2: Utfør migrering

### Migreringsnotater (Chat Completions → Responses)

- **Hvorfor migrere**: Responses er det samlede API-et for tekst, verktøy og streaming; Chat Completions er utdatert. Med GPT-5 kreves Responses for best ytelse.
- **HTTP**: Azure-endepunktet bytter fra `/openai/deployments/{name}/chat/completions` til `/openai/v1/responses`.
- **Felter**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` forblir.
- **Formatering**: `response_format` → `text.format` med et korrekt objekt.
- **Innholdselementer**: erstatt Chat `content[].type: "text"` med Responses `content[].type: "input_text"` for system-/brukerrunder.
- **Bildeinnholdselementer**: erstatt Chat `content[].type: "image_url"` med Responses `content[].type: "input_image"`. Flatt `image_url`-feltet fra `{"image_url": {"url": "..."}}` til `{"image_url": "..."}` (en vanlig streng – enten en HTTPS-URL eller en `data:image/...;base64,...` data-URI).

### Referanse for parameterkartlegging

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array med elementer) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objekt) |
| `temperature` | `temperature` (uendret) |
| `stop` | `stop` (uendret) |
| `frequency_penalty` | `frequency_penalty` (uendret) |
| `presence_penalty` | `presence_penalty` (uendret) |
| `tools` / funksjonskall | `tools` (uendret) |
| `seed` | **Fjern** (ikke støttet) |
| `store` | `store` (sett til `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (flat streng) |

For komplette før/etter-kodeeksempler, se [cheat-sheet.md](./references/cheat-sheet.md).

For testinfrastrukturmigrering (mocker, snapshots, assertions), se [test-migration.md](./references/test-migration.md).

For feilsøking og fallgruver, se [troubleshooting.md](./references/troubleshooting.md).

---

## Dataoppbevaring og tilstand

- Sett `store: false` på alle Responses-forespørsler.
- Ikke stol på tidligere meldings-IDer eller serverlagret kontekst; hold tilstanden klientstyrt og minimer metadata.

---

## Akseptansekriterier

### Kode-nivå porter (alle må passere)

- [ ] Null treff for `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` i migrerte filer.
- [ ] Null treff for `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — alle konstruktører bruker `OpenAI`/`AsyncOpenAI` med v1-endepunkt.
- [ ] Null treff for `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub Models kodebaner fjernet.
- [ ] Null treff for `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ kode bruker `OpenAIChatClient` (som bruker Responses API). I pre-1.0.0, oppgrader til `agent-framework-openai>=1.0.0`.
- [ ] Alle `ChatOpenAI(...)` kall inkluderer `use_responses_api=True`.
- [ ] Null treff for `rg "choices\[0\]"` — all responsadgang bruker `resp.output_text` eller Responses output-skjema.
- [ ] Ingen `response_format` på toppnivå; all strukturert utdata bruker `text={"format": {...}}`.
- [ ] `openai>=1.108.1` og `azure-identity` i `requirements.txt` eller `pyproject.toml`; avhengigheter reinstallert.
- [ ] `store=False` satt på hvert `responses.create` kall.
- [ ] Ingen `api_version` i klientkonstruksjon; `AZURE_OPENAI_API_VERSION` fjernet fra miljøfiler og infrastruktur.

### Testinfrastrukturporter (alle må passere)

- [ ] Null treff for `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Null treff for `rg "_azure_ad_token_provider" tests/` — assertions oppdatert til å sjekke `isinstance(client, AsyncOpenAI)` eller `base_url`.
- [ ] Null treff for `rg "prompt_filter_results|content_filter_results" tests/` — Azure-spesifikke filtermocker fjernet.
- [ ] Mock-fiksturer bruker `kwargs.get("input")` ikke `kwargs.get("messages")`.
- [ ] Snapshot- / golden-filer oppdatert til Responses streaming-format (ingen `choices[0]`, `function_call`, `logprobs`, osv.).
- [ ] `pytest` kjører uten feil etter alle testoppdateringer.

### Atferdsporter (verifiser manuelt eller via testrammeverk)

- [ ] **Grunnleggende fullføring**: ikke-strømmende `responses.create` returnerer ikke-tom `output_text`.
- [ ] **Strømmeparethet**: hvis originalkoden brukte streaming, streames og yields `response.output_text.delta`-hendelser med ikke-tomme deltas.
- [ ] **Strukturert utdata**: hvis du bruker `text.format` med `json_schema`, lykkes `json.loads(resp.output_text)` og samsvarer med skjemaet.
- [ ] **Verktøysamtaleloop**: hvis verktøy brukes, initierer modellen verktøysamtaler, appen utfører dem, og oppfølgingsforespørselen returnerer en endelig `output_text` (ingen uendelig loop).
- [ ] **Async-jevnhet**: hvis `AsyncAzureOpenAI` ble brukt, fungerer `AsyncOpenAI`-ekvivalent med `await`.
- [ ] **Feilrate**: ingen nye 400/401/404-feil sammenlignet med pre-migreringslinjen.

### Leveranser

- Sammendrag inkluderer redigerte filer, før/etter-tellinger av legacy-kallsteder, og neste steg.
- Endringer er kun arbeidsområde-redigeringer (ingen commits).

---

## SDK-versjonskrav

| Pakke | Minimum versjon |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Nyeste (for EntraID-autentisering) |

---

## Referanser

- [Jukselapp — alle kodebiter](./references/cheat-sheet.md)
- [Testmigrering — mocker, snapshots, assertions](./references/test-migration.md)
- [Feilsøking — feil, risikotabell, fallgruver](./references/troubleshooting.md)
- [detect_legacy.py — automatisert skanner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Startpakke](https://aka.ms/openai/start)
- [Azure OpenAI Responses API-dokumentasjon](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API versjon livssyklus](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API referanse](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->