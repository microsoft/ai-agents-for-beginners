# Responses API jukselapp (Python + Azure OpenAI)

> Alle kodestykker under forutsetter `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` og at `client` allerede er initialisert (se klientoppsett).

## Grunnleggende forespørsel
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Klientoppsett — EntraID (anbefalt)
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = OpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Klientoppsett — API-nøkkel
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Asynkront klientoppsett — EntraID
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AsyncOpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Asynkront klientoppsett — EntraID med eksplisitt tenant (multi-tenant)

Når Azure OpenAI-ressursen er i en **annen tenant** enn standard, send `tenant_id` eksplisitt til legitimasjonen. Dette er vanlig i utviklings-/test-scenarier hvor utviklerens hjemme-tenant er forskjellig fra ressurs-tenant.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential for produksjon (Azure Container Apps, App Service, osv.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # Brukertildelt administrert identitet
)
# AzureDeveloperCliCredential for lokal utvikling – eksplisitt tenant_id er kritisk
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Kjede: prøv administrert identitet først, fallback til azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migrering av asynkront klient — før/etter

Før (utrangert):
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

Etter:
```python
from openai import AsyncOpenAI

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)

resp = await client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Full synkron migrering — før/etter

Før (gammel — Azure OpenAI Chat Completions):
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

Etter (Responses API — Azure OpenAI v1-endepunkt):
```python
from openai import OpenAI
import os

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Streaming (synkron)
```python
stream = client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()  # ny linje på slutten
```

## Streaming (asynkron)
```python
stream = await client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
async for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()
```

## Webapp-streaming — backend-til-frontend-form

Ved migrering av en webapp som streamer SSE/JSONL til frontend, endres **backend-serialiseringsformatet**. Design den nye backend-utgangen for å bevare front-endens eksisterende tilgangsmønstre slik at frontend ikke trenger endringer.

**Før** — Chat Completions-backend serialiserte vanligvis `choices[0]` dict for hver chunk:
```python
# Gammel: serialisert full valgordbok per del
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend leser: `response.delta.content` (dypt sti inn i valg-objektet).

**Etter** — Responses API-backend sender en minimal form som bevarer samme frontend-tilgangssti:
```python
# Nytt: send kun det frontend trenger
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend leser fortsatt `response.delta.content` — **ingen frontend-endringer nødvendig**.

> **Nøkkelinnsikt**: Streaming-formen for Responses API (`event.type` + `event.delta`) er grunnleggende annerledes enn Chat Completions (`chunk.choices[0].delta.content`). Men kontrakten mellom backend og frontend er opp til deg å definere. Form backend-utgangen slik at den matcher det frontend allerede forventer.

## Streaming hendelsessekvens

Når `stream: true`, sender API hendelser i denne rekkefølgen:
1. `response.created` – respons-objekt initialisert
2. `response.in_progress` – generering startet
3. `response.output_item.added` – output-element opprettet
4. `response.content_part.added` – innholdsdel startet
5. `response.output_text.delta` – tekst-chunks (flere, hver har `delta: string`)
6. `response.output_text.done` – tekstgenerering ferdig
7. `response.content_part.done` – innholdsdel ferdig
8. `response.output_item.done` – output-element ferdig
9. `response.completed` – full respons ferdig

For grunnleggende tekst-streaming, håndter kun `response.output_text.delta` (for tekstchunks) og `response.completed` (for fullføring).

## Streaming feilbehandling i web-apper

Når du streamer i en webapp, pakk inn asynkron iterasjon i `try/except` og yield feil som JSON slik at frontend kan vise dem pent (f.eks. rate limits, midlertidige feil):

```python
@stream_with_context
async def response_stream():
    chat_coroutine = client.responses.create(
        model=deployment,
        input=all_messages,
        max_output_tokens=1000,
        stream=True,
        store=False,
    )
    try:
        async for event in await chat_coroutine:
            if event.type == "response.output_text.delta":
                yield json.dumps({"delta": {"content": event.delta}}) + "\n"
            elif event.type == "response.completed":
                yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
    except Exception as e:
        current_app.logger.error(e)
        yield json.dumps({"error": str(e)}) + "\n"
```

> **Hvorfor dette er viktig**: Azure OpenAI returnerer `429 Too Many Requests` ved rate limiting. Uten `try/except` dør streaming-responsen stille. Med den, mottar frontend `{"error": "Too Many Requests"}` og kan vise en retry-melding.

## Streaming hendelsestyper (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Samtaleformat
```python
# Responses API støtter samtaleformat via input-array
response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are an Azure cloud architect."},
        {"role": "user", "content": "Design a scalable web application architecture."},
    ],
    max_output_tokens=1000,
)
print(response.output_text)
```

## Feilbehandling av innholdsfilter

Feilstrukturen endret seg fra Chat Completions til Responses API.

Før (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Etter (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Nøkkelforskjeller:
- `innererror` wrapper er **borte** — detaljer om innholdsfilter er nå på øverste nivå i `error.body`.
- `content_filter_result` (entall) → `content_filters` (flertall array) som inneholder `content_filter_results` (flertall) inni hver oppføring.
- Hver oppføring i `content_filters` inkluderer `blocked`, `source_type`, og `content_filter_results` med per-kategori detaljer (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Full Responses API content filter feil-kroppsstruktur:
```json
{
  "message": "The response was filtered...",
  "type": "invalid_request_error",
  "param": "prompt",
  "code": "content_filter",
  "content_filters": [
    {
      "blocked": true,
      "source_type": "prompt",
      "content_filter_results": {
        "jailbreak": { "detected": true, "filtered": true },
        "hate": { "filtered": false, "severity": "safe" },
        "sexual": { "filtered": false, "severity": "safe" },
        "violence": { "filtered": false, "severity": "safe" },
        "self_harm": { "filtered": false, "severity": "safe" }
      }
    }
  ]
}
```

## Rå HTTP migrering (requests/httpx)

Hvis appen kaller Azure OpenAI REST direkte i stedet for å bruke SDK:

Før (Chat Completions):
```python
endpoint = f"{azure_endpoint}/openai/deployments/{deployment}/chat/completions?api-version=2024-03-01-preview"
data = {
    "messages": [{"role": "user", "content": query}],
    "model": model_name,
    "temperature": 0,
}
response = requests.post(endpoint, headers=headers, json=data)
message = response.json()["choices"][0]["message"]["content"]
```

Etter (Responses API):
```python
endpoint = f"{azure_endpoint}/openai/v1/responses"
data = {
    "model": deployment,
    "input": [{"role": "user", "content": query}],
    "temperature": 0,
    "max_output_tokens": 1000,
    "store": False,
}
response = requests.post(endpoint, headers=headers, json=data)
output_text = response.json()["output"][0]["content"][0]["text"]
```

> **Merk**: `output_text` er en bekvemmelighetsegenskap i Python SDK sitt `Response` objekt. Den rå REST JSON-responsen har ikke et øverste nivå `output_text`-felt — teksten ligger på `output[0].content[0].text`.

## Multi-turn samtale
```python
# Bygg en samtale med Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Legg til assistentens svar i samtalen
messages.append({"role": "assistant", "content": response.output_text})

# Fortsett samtalen
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Innholdstypet multi-turn (eksplisitt `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Multi-turn via `previous_response_id` (alternativ)

I stedet for å håndtere samtalearrayet selv, kan du kjede svar
på serversiden ved å bruke `previous_response_id`. API lagrer hver respons og
legger automatisk til tidligere turer foran.

```python
# Første trekk
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Påfølgende trekk — bare send den nye brukermeldingen + forrige respons-ID
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Når man bruker hva:**

| Tilnærming | Fordeler | Ulemper |
|---|---|---|
| `input` array (manuell) | Full kontroll over historikk; kan trimme/summere; ingen server-lagring nødvendig (`store=False`) | Mer kode; du håndterer arrayet |
| `previous_response_id` | Enklere kode; automatisk kjeding | Krever `store=True` (standard); samtale lagres server-side; kan ikke modifisere historikk mellom turer |

> **Migreringsnotat:** De fleste Chat Completions-appene håndterer allerede sin egen meldingsarray, så konvertering til `input`-array er en mer direkte 1:1-migrering. Bruk `previous_response_id` for ny kode eller når du ikke trenger å manipulere samtalehistorikk.

## O-serie resonnementmodeller (o1, o3-mini, o3, o4-mini)

O-seriemodeller har unike parameterbegrensninger ved migrering til Responses API.

### Parametermapping for o-serien

| Chat Completions (o-serie) | Responses API | Notater |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Sett høyt (4096+) — resonnementstokens teller mot grensen |
| `reasoning_effort` | `reasoning.effort` | Behold som den er hvis tilstede (low/medium/high) |
| `temperature` | Fjern eller sett til `1` | O-serien godtar bare `1` |
| `top_p` | Fjern | Ikke støttet på o-serien |
| `seed` | Fjern | Ikke støttet i Responses API |

### O-serie før/etter

Før (Chat Completions med o-serie):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Etter (Responses API):
```python
resp = client.responses.create(
    model=deployment,
    input="Solve this step by step: 2x + 5 = 13",
    max_output_tokens=4096,
    reasoning={"effort": "medium"},
    store=False,
)
print(resp.output_text)
```

> **Merk**: O-seriemodeller kan bufre utdata under resonnement før tekstdeltahendelser sendes. Streaming fungerer fortsatt, men første `response.output_text.delta`-hendelse kan komme etter lengre forsinkelse enn med GPT-modeller.

## Tilgang til resonnementstokens
```python
# Resonneringsmodeller bruker intern resonnering — du kan se hvor mange resonnementstokens som ble brukt
response = client.responses.create(
    model=deployment,
    input="Explain quantum computing in simple terms",
    max_output_tokens=1000,
)
print(response.output_text)
print(f"Status: {response.status}")
print(f"Reasoning tokens: {response.usage.output_tokens_details.reasoning_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
```

> **Viktig**: Bruk `max_output_tokens=1000` (ikke 50–200) for å ta høyde for resonnementmodellens interne resonnementprosess. Modellen bruker resonnementstokens internt før den genererer den endelige utdata.

## Strukturert utdata — JSON Schema
```python
resp = client.responses.create(
    model=deployment,
    input="What is the capital of France?",
    max_output_tokens=500,
    text={
        "format": {
            "type": "json_schema",
            "name": "Output",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {"answer": {"type": "string"}},
                "required": ["answer"],
                "additionalProperties": False,
            },
        }
    },
    store=False,
)
import json
data = json.loads(resp.output_text)
print(data["answer"])
```

## Verktøybruk

- Definer funksjoner i `tools` med det **flate Responses API-formatet** — `name`, `description` og `parameters` på øverste nivå (ikke nested under `function`).
- Når modellen ber om å kalle et verktøy, kjør det i appen din og inkluder verktøyresultatet i neste forespørsel som en `function_call_output`-oppføring innen `input`.
- Hold skjemaene minimale; valider input før kjøring.
- Når du bruker `strict: true`, må alle egenskaper listes i `required` og `additionalProperties: false` er obligatorisk.

> **⚠️ `pydantic_function_tool()` er inkompatibel**: `openai.pydantic_function_tool()`-hjelperen genererer fortsatt det gamle Chat Completions nested-formatet (`{"type": "function", "function": {"name": ...}}`). Ikke bruk den med `responses.create()`. Definer verktøyskjemaer manuelt eller lag en wrapper for å flate ut output.

### Verktøydefinisjonsformat

Responses API bruker et **flatt** verktøyformat — `name`, `description`, `parameters` er toppnøkler (ikke nested under `function`).

**Før (Chat Completions — nested):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Etter (Responses API — flatt):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Fullt eksempel:
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are a weather chatbot."},
        {"role": "user", "content": "What's the weather in Berkeley?"},
    ],
    tools=tools,
    tool_choice="auto",
    store=False,
)
```

Med `strict: true` (skjema-håndhevelse):
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],       # Alle egenskaper MÅ listes opp
            "additionalProperties": False,   # Påkrevd for streng modus
        },
    }
]
```

### Verktøykall round-trip (kjør og returner resultater)

Når modellen ber om et verktøykall, bruk `response.output` elementer + `function_call_output` — **ikke** Chat Completions `role: assistant` + `role: tool` mønsteret.

```python
import json

messages = [
    {"role": "system", "content": "You are a weather chatbot."},
    {"role": "user", "content": "Is it sunny in Berkeley?"},
]

response = client.responses.create(
    model=deployment, input=messages, tools=tools, store=False,
)

tool_calls = [item for item in response.output if item.type == "function_call"]
if tool_calls:
    # Legg til modellens function_call-elementer i samtalen
    messages.extend(response.output)

    # Utfør hvert verktøy og legg til resultater
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Hent endelig svar med verktøyresultater
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Få-skudd verktøykalleksempler

Når du gir få-skudd-eksempler på verktøykall i `input`, bruk `function_call` og `function_call_output` elementer. ID-er må starte med `fc_`.

```python
messages = [
    {"role": "system", "content": "You are a product search assistant."},
    {"role": "user", "content": "Find climbing gear for outdoors"},
    {
        "type": "function_call",
        "id": "fc_example1",
        "call_id": "call_example1",
        "name": "search_database",
        "arguments": '{"search_query": "climbing gear outdoor"}',
    },
    {
        "type": "function_call_output",
        "call_id": "call_example1",
        "output": "Results: ...",
    },
    {"role": "user", "content": "Now find shoes under $50"},
]
```

```python
# Innebygd nett søk eksempel
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Bildeinput

Bildeinnholdselementer endrer type fra `image_url` til `input_image`, og URL går fra å være et nested objekt til en flat streng.

### Bildeinput — før (Chat Completions)
```python
resp = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

### Bildeinput — etter (Responses API, URL)
```python
resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": "https://example.com/image.jpg",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

### Bildeinput — etter (Responses API, base64)
```python
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image("path_to_your_image.jpg")

resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

> **Viktige endringer**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (nested objekt) → `"image_url": "..."` (flat streng — enten HTTPS URL eller `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) migrering

**Sjekk din MAF-versjon først** — migreringen avhenger av om du er på MAF 1.0.0+ eller en pre-1.0.0 beta/rc.

For å sjekke: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

I MAF 1.0.0+ bruker `OpenAIChatClient` **allerede Responses API** — ingen migrering nødvendig.

Hvis koden basen bruker den gamle `OpenAIChatCompletionClient` (som bruker `chat.completions.create`), bytt den ut med `OpenAIChatClient`:

Før:
```python
from agent_framework.openai import OpenAIChatCompletionClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatCompletionClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

Etter:
```python
from agent_framework.openai import OpenAIChatClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

### MAF pre-1.0.0 (beta/rc utgaver)

I pre-1.0.0 MAF brukte `OpenAIChatClient` Chat Completions. Oppgrader til `agent-framework-openai>=1.0.0` hvor `OpenAIChatClient` bruker Responses API som standard.

> **Merk**: `Agent`, `MCPStreamableHTTPTool` og andre MAF API-er forblir uendret — kun klientklasse-import og instansiering endres.

## LangChain (`langchain-openai`) migrering

Legg til `use_responses_api=True` til `ChatOpenAI()`. Oppdater også meldingstilgang fra `.content` til `.text`.

Før:
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
)

# ... agentpåkallelse ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Etter:
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
    use_responses_api=True,
)

# ... agentpåkalling ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Viktige endringer**: (1) `use_responses_api=True` i konstruktøren, (2) `.content` → `.text` på responsmeldinger.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->