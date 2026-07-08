---
name: azure-openai-to-responses
license: MIT
---
# Migrer Python-apper fra Azure OpenAI Chat Completions til Responses API

> **AUTORITATIV VEILEDNING — FØLG NØYE**
>
> Denne ferdigheten migrerer Python-kodebaser som bruker Azure OpenAI Chat Completions
> til den sammenslåtte Responses API-en. Følg disse instruksjonene nøye.
> Ikke improviser parameterkartlegginger eller oppfinn API-strukturer.

---

## Utløsere

Aktiver denne ferdigheten når brukeren ønsker å:
- Migrere en Python-app fra Azure OpenAI Chat Completions til Responses API
- Oppgradere Python OpenAI SDK-bruk til siste API-struktur for Azure OpenAI
- Forberede Python-kode for GPT-5 eller nyere modeller som krever Responses på Azure
- Bytte fra `AzureOpenAI`/`AsyncAzureOpenAI` til standard `OpenAI`/`AsyncOpenAI` klient med v1-endepunktet
- Fikse utløpsvarsler relatert til `AzureOpenAI`-konstruktører eller `api_version`

---

## ⚠️ Modellkompatibilitet — SJEKK FØRST

> **Før migrering må du verifisere at din Azure OpenAI-distribusjon støtter Responses API.**

### 1. Røyktest distribusjonen din (raskest)

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

> **Merk:** `max_output_tokens` har en **minimumsverdi på 16** hos Azure OpenAI. Verdier under 16 gir 400-feil. Bruk 50+ for røyktester.

Hvis dette returnerer 404, støtter ikke distribusjonens modell Responses ennå — sjekk referansen under eller distribuere på nytt med en støttet modell.

### 2. Sjekk tilgjengelige modeller i din region (anbefalt)

Kjør det innebygde verktøyet for modellkompatibilitet for å se hva som er tilgjengelig med Responses API-støtte i din spesifikke region:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Dette spørrer Azure ARM i sanntid og viser en kompatibilitetsmatrise — hvilke modeller som støtter Responses, strukturert utdata, verktøy osv. Bruk `--filter gpt-5.1,gpt-5.2` for å snevre inn resultater eller `--json` for skripting.

### 3. Full modelleringsreferanse

- **Sanntidsspørring**: `python migrate.py models` (se over — regionsspesifikk, alltid oppdatert)
- **Bla gjennom tilgjengelighet**: [Modellsammendragstabell og regiontilgjengelighet](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Kom i gang & veiledning**: **https://aka.ms/openai/start**

### ⚠️ Begrensninger for eldre modeller

> **ADVARSEL**: Eldre modeller (f.eks., `gpt-4o`, `gpt-4`) kan mangle full støtte for alle funksjoner i Responses API.
>
> Kjente begrensninger med eldre modeller:
> - **`reasoning` parameter**: Støttes ikke på `gpt-4o-mini`, `gpt-4o` og mange modeller uten resonnement. Migrer `reasoning` bare hvis det allerede fantes i originalkoden.
> - **`seed` parameter**: Støttes ikke i Responses API i det hele tatt — fjern fra alle forespørsler.
> - **Strukturert output via `text.format`**: Eldre modeller kan ha upålitelig håndheving av `strict: true` JSON-skjemaer.
> - **Verktøroktestrasjon**: GPT-5+ orkestrerer verktøy-kall som del av intern resonnement. Eldre modeller på Responses fungerer fortsatt, men mangler denne dype integrasjonen.
> - **Temperaturbegrensninger**: Ved migrering til `gpt-5` må temperatur utelates eller settes til `1`. Eldre modeller har ingen slik begrensning.

### O-serie resonnementmodeller (o1, o3-mini, o3, o4-mini)

O-serie modeller har unike parameterbegrensninger. Ved migrering av apper som målretter o-serie modeller:

- **`temperature`**: Må være `1` (eller utelatt). O-serie modeller godtar ikke andre verdier.
- **`max_completion_tokens` → `max_output_tokens`**: Apper som bruker Azure-spesifikk `max_completion_tokens` må bytte til `max_output_tokens`. Sett høye verdier (4096+) fordi resonnementstokener teller mot grensen.
- **`reasoning_effort`**: Hvis appen bruker `reasoning_effort` (lav/middels/høy), behold det — Responses API støtter denne parameteren for o-serie modeller.
- **Streamingadferd**: O-serie modeller kan buffre output til resonnement er ferdig før tekstdelta-hendelser sendes. Streaming fungerer fortsatt, men den første `response.output_text.delta` kan komme senere enn med GPT-modeller.
- **`top_p`**: Støttes ikke på o-serie — fjern hvis tilstede.
- **Verktøybruk**: O-serie modeller støtter verktøy via Responses API likt GPT-modeller, men kvaliteten på verktøroktestrasjon varierer per modell.

**Handling — proaktiv modellrådgivning**: Under skanning, sjekk hvilken modell appen retter seg mot (distribusjonsnavn, miljøvariabler, konfig). Hvis modellen er `gpt-4o` eller eldre (ikke gpt-4.1+), informer brukeren proaktivt:
- Migreringen vil fungere for grunnleggende tekst, chat, streaming og verktøy på deres nåværende modell.
- Nyere modeller (`gpt-5.1`, `gpt-5.2`) tilbyr bedre verktøroktestrasjon, håndheving av strukturert output, resonnement og tverrregiontilgjengelighet.
- De bør vurdere å oppgradere distribusjonen når klar — det blokkerer ikke migreringen.

Ikke blokker eller nekt migrering basert på modellversjon. Rådgivningen er informativ.

### GitHub Models støtter IKKE Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) støtter ikke Responses API.**

Hvis kodebasen har en GitHub Models-kodevei (sjekk `base_url` som peker til `models.github.ai` eller `models.inference.ai.azure.com`), **fjern den helt** under migrering. Responses API krever Azure OpenAI, OpenAI, eller et kompatibelt lokalt endepunkt (f.eks., Ollama med Responses-støtte).

Handling under skanning:
- Merk alle GitHub Models-kodeveier for fjerning.

---

## Rammeverksmigrering

Mange apper bruker høyere nivå rammeverk over OpenAI. Ved migrering av disse endres rammeverkets egen API — ikke bare de underliggende OpenAI-kallene.

### Microsoft Agent Framework (MAF)

**Sjekk din MAF-versjon først** — migreringen avhenger av om du bruker MAF 1.0.0+ eller en pre-1.0.0 beta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **bruker allerede Responses API** — ingen migrering nødvendig. Hvis kodebasen bruker den gamle `OpenAIChatCompletionClient` (som bruker `chat.completions.create`), bytt den ut med `OpenAIChatClient`.

| Før | Etter |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

For å sjekke versjonen: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (beta/rc-utgivelser)

I pre-1.0.0 MAF brukte `OpenAIChatClient` Chat Completions. Oppgrader til `agent-framework-openai>=1.0.0` hvor `OpenAIChatClient` bruker Responses API som standard.

Ingen andre endringer trengs — `Agent` og verktøy-API-er forblir de samme.

### LangChain (`langchain-openai`)

Legg til `use_responses_api=True` i `ChatOpenAI()`. Oppdater også respons-tilgang fra `.content` til `.text`.

| Før | Etter |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

For fullstendige før/etter-kodeeksempler, se [cheat-sheet.md](./references/cheat-sheet.md).

---

## Frontend-migreringsveiledning

> **Responses API er et serversideanliggende.** Migrer din Python-backend; frontendens HTTP-kontrakt bør forbli uendret med mindre backenden er et tynt gjennomgangslag — i så fall vurder å adoptere Responses forespørselsstruktur for å eliminere et oversettelseslag. Hvis frontenden kaller OpenAI direkte med en klientnøkkel, flytt disse kallene til backend først.

### Nedleggelse av `@microsoft/ai-chat-protocol`

`@microsoft/ai-chat-protocol` npm-pakken er nedlagt og bør erstattes med [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Hvis du støter på den i en frontend:

1. Bytt ut CDN-skript-tagg:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Fjern `AIChatProtocolClient`-instansiering (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Erstatt `client.getStreamedCompletion(messages)` med et direkte `fetch()`-kall til backend streamingendepunkt.
4. Erstatt `for await (const response of result)` med `for await (const chunk of readNDJSONStream(response.body))`.
5. Oppdater eiendomstilgang fra `response.delta.content` / `response.error` til `chunk.delta.content` / `chunk.error`.

---

## Mål

- Liste alle Python-kallsteder som bruker Chat Completions eller legacy Completions mot Azure OpenAI.
- Foreslå en migreringsplan og sekvens for Python-kodebasen.
- Anvend sikre, minimale endringer for å bytte til Responses API.
- Oppdater kallere til å bruke Responses output-skjema; ingen tilbakestøtte-innpakninger.
- Kjør tester/linter; fiks trivielle brudd forårsaket av migreringen.
- Forbered små, gjennomgåbare endringssett og gi en endelig oppsummering med diff (ikke commit).

---

## Retningslinjer

- Endre kun filer inne i git-arbeidsområdet. Aldri skriv utenfor.
- Ikke bevar bakoverkompatible shims; migrer kode til ny API-struktur.
- Ikke legg igjen gravstein/overgangskommentarer eller backupfiler.
- Bevar streamingsemantikk hvis tidligere brukt; ellers bruk ikke-streaming.
- Be om godkjenning før kjøring av kommandoer eller nettverkskall i godkjenningsmodus.
- Ikke kjør `git add`/`git commit`/`git push`; produser kun endringer i arbeidsområdet.

---

## Steg 0: Migrering av Azure OpenAI-klient (forutsetning)

Hvis kodebasen bruker `AzureOpenAI` eller `AsyncAzureOpenAI` konstruktører, migrer først til standard `OpenAI` / `AsyncOpenAI` konstruktører. Azure-spesifikke konstruktører er avviklet i `openai>=1.108.1`.

### Hvorfor v1 API-sti?

Det nye `/openai/v1` endepunktet bruker standard `OpenAI()` klient i stedet for `AzureOpenAI()`, krever ingen `api_version`-parameter, og fungerer likt på OpenAI og Azure OpenAI. Samme klientkode er fremtidssikker — ingen versjonshåndtering nødvendig.

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
- Fjern miljøvariablene `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` fra `.env`, applinstillinger og Bicep/infrastrukturfiler.
- Omdøp `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` i `.env`, applinstillinger, Bicep/infra, og test-fixtures (standard Azure Identity SDK-konvensjon).
- Sørg for `openai>=1.108.1` i `requirements.txt` eller `pyproject.toml`.

### Migrering av miljøvariabler

| Gammel env-var | Handling | Notater |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Fjern** | Ingen `api_version` nødvendig med v1-endepunktet |
| `AZURE_OPENAI_API_VERSION` | **Fjern** | Samme som ovenfor |
| `AZURE_OPENAI_CLIENT_ID` | **Omdøp** → `AZURE_CLIENT_ID` | Standard Azure Identity SDK-konvensjon for `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Behold** | Trengs fortsatt for `base_url`-konstruksjon |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Behold** | Brukes som `model`-parameter i `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Behold** | Brukes som `api_key` for nøkkelbasert autentisering |

For klientoppsett eksempel (synk, asynk, EntraID, API-nøkkel, multi-leietaker), se [cheat-sheet.md](./references/cheat-sheet.md).

---

## Steg 1: Oppdag legacy kallsteder

Kjør skriptet [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) for å finne alle kallsteder som trenger migrering:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Eller kjør disse søkene manuelt — hvert treff er et migreringsmål:

```bash
# Legacy API-kall (må skrive om)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Utdaterte Azure-klientkonstruktører (må erstattes)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Tilgangsmønstre for responsstruktur (må oppdateres)
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

# Utdaterte parametere (må fjernes eller gis nytt navn)
rg "response_format"
rg "max_tokens\b"        # gi nytt navn til max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Utdaterte miljøvariabler (rydde opp)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # skal være AZURE_CLIENT_ID

# GitHub Models-endepunkter (må fjernes — Responses API støttes ikke)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Rammeverksnivå legacy-mønstre (må oppdateres)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: erstatt med OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: trenger use_responses_api=True

# Testinfrastruktur (må oppdateres)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Tilgang til innholdsfilterfeil-innhold (må oppdateres — struktur endret)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # gammel entallsform — nå content_filter_results (flertall) inne i content_filters-array

# Rå HTTP-kall til Chat Completions-endepunkt (må oppdatere URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristikker (oppdage og omskrive)

- **Chat Completions klient**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure-klientkonstruktører**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Verktøy**: konverter funksjonskallverktøydefinisjoner fra innfelt format (`{"type": "function", "function": {"name": ...}}`) til flat Responses-format (`{"type": "function", "name": ...}`); bruk `tool_choice`; returner verktøyresultater som `{"type": "function_call_output", "call_id": ..., "output": ...}` elementer (ikke `{"role": "tool", ...}`).
- **Verktøyrundturer**: når modellen returnerer funksjonskall, legg til `response.output` elementer i samtalen (ikke en manuell `{"role": "assistant", "tool_calls": [...]}` ordliste), deretter legg til `function_call_output` elementer for hvert resultat.
- **Eksempler på fåskuddverktøy**: hvis samtalen inkluderer hardkodede eksempler på verktøykall, konverter dem til `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` elementer. ID-er må starte med `fc_`.
- **`pydantic_function_tool()`**: denne hjelpefunksjonen genererer fortsatt det gamle innfelte formatet og er **ikke kompatibel** med `responses.create()`. Bytt den ut med manuelle verktøydefinisjoner eller en flatleggingswrapper.
- **Flere runder**: vedlikehold samtalehistorikk i appen; send tidligere runder via `input` elementer.
- **Formatering**: erstatt Chats top-nivå `response_format` med `text.format` i Responses. Kanonisk form: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Innholdselementer**: erstatt Chat `content[].type: "text"` med Responses `content[].type: "input_text"` for bruker-/systemrunder.
- **Bildeinnholdselementer**: erstatt Chat `content[].type: "image_url"` med Responses `content[].type: "input_image"`. Feltet `image_url` endres fra et innfelt objekt `{"url": "..."}` til en flat streng. Se jukseark for før/etter-eksempler.
- **Resonneringsinnsats**: **migrer bare `reasoning` hvis det allerede finnes i originalkoden**.
- **Feilhåndtering for innholdsfilter**: feilens kroppsstruktur har endret seg. Chat Completions brukte `error.body["innererror"]["content_filter_result"]` (entall); Responses API bruker `error.body["content_filters"][0]["content_filter_results"]` (flertall, inne i en matrise). Kode som får tilgang til `innererror` vil kaste `KeyError`. Skriv om til den nye banen.
- **Rå HTTP-kall**: hvis appen kaller Azure OpenAI REST API direkte (via `requests`, `httpx` osv.) med `/openai/deployments/{name}/chat/completions?api-version=...`, skriv om til `/openai/v1/responses`. Forespørselskroppen endres: `messages` → `input`, legg til `max_output_tokens` og `store: false`, fjern `api-version` som spørringsparameter. Responskroppen endres: `choices[0].message.content` → `output[0].content[0].text` (merk: `output_text` er en SDK-bekvemmelighetsegenskap som ikke finnes i rå REST JSON).

---

## Trinn 2: Bruk migrering

### Migrasjonsnotater (Chat Completions → Responses)

- **Hvorfor migrere**: Responses er det forente API-et for tekst, verktøy og streaming; Chat Completions er legacy. Med GPT-5 kreves Responses for best ytelse.
- **HTTP**: Azure-endepunktet bytter fra `/openai/deployments/{name}/chat/completions` til `/openai/v1/responses`.
- **Felt**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` forblir.
- **Formatering**: `response_format` → `text.format` med et gyldig objekt.
- **Innholdselementer**: erstatt Chat `content[].type: "text"` med Responses `content[].type: "input_text"` for system-/brukerrunder.
- **Bildeinnholdselementer**: erstatt Chat `content[].type: "image_url"` med Responses `content[].type: "input_image"`. Gjør feltet `image_url` flatt fra `{"image_url": {"url": "..."}}` til `{"image_url": "..."}` (en enkel streng — enten en HTTPS-URL eller en `data:image/...;base64,...` data-URI).

### Referanse for parameterkartlegging

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (array av elementer) |
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

For komplette før/etter kodeeksempler, se [cheat-sheet.md](./references/cheat-sheet.md).

For testinfrastrukturmigrering (mocks, øyeblikksbilder, påstander), se [test-migration.md](./references/test-migration.md).

For feilsøking av feil og fallgruver, se [troubleshooting.md](./references/troubleshooting.md).

---

## Databevaring & Tilstand

- Sett `store: false` på alle Requests til Responses.
- Ikke stol på forrige meldings-IDer eller kontekst lagret på server; hold tilstanden klientstyrt og minimer metadata.

---

## Akseptansekriterier

### Kode-nivå porter (alle må bestå)

- [ ] Null treff for `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` i migrerte filer.
- [ ] Null treff for `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — alle konstruktører bruker `OpenAI`/`AsyncOpenAI` med v1 endepunktet.
- [ ] Null treff for `rg "models\.github\.ai|models\.inference\.ai\.azure"` — GitHub Models-kodebaner fjernet.
- [ ] Null treff for `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ bruker `OpenAIChatClient` (som bruker Responses API). I pre-1.0.0, oppgrader til `agent-framework-openai>=1.0.0`.
- [ ] Alle `ChatOpenAI(...)` kall inkluderer `use_responses_api=True`.
- [ ] Null treff for `rg "choices\[0\]"` — all responsadgang bruker `resp.output_text` eller Responses output-skjema.
- [ ] Ingen `response_format` på toppnivå; all strukturert output bruker `text={"format": {...}}`.
- [ ] `openai>=1.108.1` og `azure-identity` i `requirements.txt` eller `pyproject.toml`; avhengigheter reinstalleres.
- [ ] `store=False` satt på alle `responses.create` kall.
- [ ] Ingen `api_version` i klientkonstruksjon; `AZURE_OPENAI_API_VERSION` fjernet fra miljøfiler og infrastruktur.

### Testinfrastrukturporter (alle må bestå)

- [ ] Null treff for `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Null treff for `rg "_azure_ad_token_provider" tests/` — påstander oppdatert til å sjekke `isinstance(client, AsyncOpenAI)` eller `base_url`.
- [ ] Null treff for `rg "prompt_filter_results|content_filter_results" tests/` — Azure-spesifikke filtermocks fjernet.
- [ ] Mock-fixtures bruker `kwargs.get("input")` ikke `kwargs.get("messages")`.
- [ ] Øyeblikksbildedata / gullfiler oppdatert til Responses streamingform (ingen `choices[0]`, `function_call`, `logprobs`, osv.).
- [ ] `pytest` kjører med null feil etter alle testoppdateringer.

### Atferdsporter (verifiser manuelt eller via testrammeverk)

- [ ] **Grunnleggende ferdigstilling**: ikke-strømmende `responses.create` returnerer ikke-tom `output_text`.
- [ ] **Strømmeparitet**: hvis originalkode brukte streaming, strømmer migrert kode og sender `response.output_text.delta` hendelser med ikke-tomme deltaljer.
- [ ] **Strukturert output**: hvis `text.format` med `json_schema` brukes, lykkes `json.loads(resp.output_text)` og samsvarer med skjemaet.
- [ ] **Verktøykallsløyfe**: hvis verktøy brukes, gjør modellen verktøykall, appen utfører dem, og oppfølgingsforespørsel returnerer endelig `output_text` (ingen uendelig løkke).
- [ ] **Async-paritet**: hvis `AsyncAzureOpenAI` ble brukt, fungerer `AsyncOpenAI` tilsvarende med `await`.
- [ ] **Feilrate**: ingen nye 400/401/404 feil sammenlignet med baseline før migrering.

### Leveranser

- Sammendrag inkluderer redigerte filer, før/etter tellinger av legacy-kallsteder og neste steg.
- Endringene er bare arbeidsområdeendringer (ingen commits).

---

## SDK-versjonskrav

| Pakke | Minimum versjon |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Nyeste (for EntraID autentisering) |

---

## Referanser

- [Jukseark — alle kodeutdrag](./references/cheat-sheet.md)
- [Testmigrering — mocks, øyeblikksbilder, påstander](./references/test-migration.md)
- [Feilsøking — feil, risikotabell, fallgruver](./references/troubleshooting.md)
- [detect_legacy.py — automatisert scanner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI startpakke](https://aka.ms/openai/start)
- [Azure OpenAI Responses API dokumentasjon](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API versjons livssyklus](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API referanse](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->