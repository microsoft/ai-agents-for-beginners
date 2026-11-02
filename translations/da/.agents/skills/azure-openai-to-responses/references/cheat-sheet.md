# Responses API Snydeark (Python + Azure OpenAI)

> Alle kodeeksempler nedenfor antager `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` og at `client` allerede er initialiseret (se klientopsætning).

## Grundlæggende forespørgsel
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Klientopsætning — EntraID (anbefalet)
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

## Klientopsætning — API-nøgle
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Async klientopsætning — EntraID
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

## Async klientopsætning — EntraID med eksplicit lejer (multi-lejer)

Når Azure OpenAI ressourcen er i en **anden lejer** end standarden, skal `tenant_id` eksplicit videregives til troværdigheden. Det er almindeligt i udviklings-/testscenarier, hvor udviklerens hjemlejer adskiller sig fra ressourcens lejer.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential til produktion (Azure Container Apps, App Service osv.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # bruger-tilknyttet administreret identitet
)
# AzureDeveloperCliCredential til lokal udvikling — eksplicit tenant_id er afgørende
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Kæde: prøv administreret identitet først, fal tilbage til azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Async klientmigrering — før/efter

Før (forældet):
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

Efter:
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

## Fuldsynkron migrering — før/efter

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

Efter (Responses API — Azure OpenAI v1 endpoint):
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
        print()  # ny linje til slut
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

## Webapp streaming — backend-til-frontend format

Når du migrerer en webapp, der streamer SSE/JSONL til en frontend, ændres **backend-serialiseringsformatet**. Design det nye backend-output, så det bevarer den frontend, der allerede findes, så frontend ikke behøver at ændres.

**Før** — Chat Completions backend serialiserede typisk hver chunks `choices[0]` dict:
```python
# Gammel: serialiseret fuld valgordbog pr. stykke
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend læser: `response.delta.content` (dyb sti ind i choice-objektet).

**Efter** — Responses API backend udsender en minimal form, der bevarer samme frontend-tilgang:
```python
# Ny: udsend kun det, frontenden har brug for
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend læser stadig `response.delta.content` — **ingen frontend-ændringer nødvendige**.

> **Vigtigt indblik**: Responses API streaming-formen (`event.type` + `event.delta`) er grundlæggende anderledes end Chat Completions (`chunk.choices[0].delta.content`). Men din backend-til-frontend aftale er op til dig. Form backend-outputtet, så det matcher det frontend allerede forventer.

## Streaming event sekvens

Når `stream: true`, udsender API'en events i denne rækkefølge:
1. `response.created` – svarobjekt initialiseret
2. `response.in_progress` – generering startet
3. `response.output_item.added` – output element oprettet
4. `response.content_part.added` – indholdsdel startet
5. `response.output_text.delta` – tekststykker (flere, hver har `delta: string`)
6. `response.output_text.done` – tekstgenerering færdig
7. `response.content_part.done` – indholdsdel færdig
8. `response.output_item.done` – output element færdig
9. `response.completed` – fuldt svar fuldført

For grundlæggende tekststreaming håndtér kun `response.output_text.delta` (for tekststykker) og `response.completed` (for færdiggørelse).

## Streaming fejlhåndtering i webapps

Når du streamer i en webapp, skal du omslutte den asynkrone iteration med `try/except` og sende fejl som JSON, så frontend kan vise dem pænt (fx raterestriktioner, midlertidige fejl):

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

> **Hvorfor det er vigtigt**: Azure OpenAI returnerer `429 Too Many Requests` ved raterestriktion. Uden `try/except` dør streaming-responsen stille. Med den modtager frontend `{"error": "Too Many Requests"}` og kan vise en genforsøg-prompt.

## Streaming eventtyper (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Samtaleformat
```python
# Responses API'en understøtter samtaleformat via input-array
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

## Fejlhåndtering ved indholdsfilter

Fejl-kropsstrukturen ændrede sig fra Chat Completions til Responses API.

Før (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Efter (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Vigtige forskelle:
- `innererror` wrapperen er **fjernet** — indholdsfilterdetaljer er nu på øverste niveau i `error.body`.
- `content_filter_result` (ental) → `content_filters` (flertal array) indeholdende `content_filter_results` (flertal) i hver post.
- Hver post i `content_filters` indeholder `blocked`, `source_type` og `content_filter_results` med detaljer pr. kategori (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Fuld Responses API indholdsfilter fejl-krop form:
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

## Raw HTTP migrering (requests/httpx)

Hvis appen kalder Azure OpenAI REST direkte i stedet for at bruge SDK'en:

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

Efter (Responses API):
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

> **Bemærk**: `output_text` er en bekvemmelighedsegenskab på Python SDK's `Response` objekt. Den rå REST JSON respons har ikke et topniveau `output_text` felt — teksten findes ved `output[0].content[0].text`.

## Multi-turn samtale
```python
# Byg en samtale med Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Tilføj assistentens svar til samtalen
messages.append({"role": "assistant", "content": response.output_text})

# Fortsæt samtalen
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Indholdstypet multi-turn (eksplicit `input_text`/`output_text`):
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

I stedet for at administrere samtalematricen selv, kan du kæde svar sammen
serverside ved at bruge `previous_response_id`. API'en gemmer hvert svar og
føjer automatisk tidligere runder forrest.

```python
# Første tur
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Efterfølgende ture — send blot den nye brugermeddelelse + tidligere svar-ID
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Hvornår man bruger hvad:**

| Tilgang | Fordele | Ulemper |
|---|---|---|
| `input` array (manuel) | Fuld kontrol over historik; kan trimme/sammendrage; ingen server-side lagring nødvendig (`store=False`) | Mere kode; du administrerer arrayet |
| `previous_response_id` | Simpel kode; automatisk sammenkædning | Kræver `store=True` (standard); samtale lagres serverside; kan ikke ændre historik mellem runder |

> **Migreringsnote:** De fleste Chat Completions apps håndterer allerede deres egne meddelelsesarrays, så konvertering til `input` array er en mere direkte 1:1 migrering. Brug `previous_response_id` til ny kode eller når du ikke behøver at manipulere samtalehistorik.

## O-serie ræsonnementsmodeller (o1, o3-mini, o3, o4-mini)

O-serie modeller har unikke parameterbegrænsninger ved migrering til Responses API.

### Parametermapping for o-serien

| Chat Completions (o-serie) | Responses API | Noter |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Sæt højt (4096+) — ræsonnementstokens tæller mod grænsen |
| `reasoning_effort` | `reasoning.effort` | Behold som det er hvis til stede (lav/mellem/høj) |
| `temperature` | Fjern eller sæt til `1` | O-serien accepterer kun `1` |
| `top_p` | Fjern | Ikke understøttet på o-serien |
| `seed` | Fjern | Ikke understøttet i Responses API |

### O-serie før/efter

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

Efter (Responses API):
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

> **Bemærk**: O-serie modeller kan buffere output under ræsonnement før de udsender tekst-deltaer. Streaming virker stadig, men første `response.output_text.delta` event kan komme efter en længere forsinkelse end med GPT-modeller.

## Adgang til ræsonnementstokens
```python
# Årsagsmodeller bruger intern ræsonnering — du kan se, hvor mange ræsonneringstokens der blev brugt
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

> **Vigtigt**: Brug `max_output_tokens=1000` (ikke 50–200) for at tage højde for ræsonnementsmodellernes interne ræsonneringsproces. Modellen bruger ræsonnementstokens internt før generering af endeligt output.

## Struktureret output — JSON Schema
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

## Værktøjsbrug

- Definér funktioner i `tools` med det **flade Responses API format** — `name`, `description` og `parameters` på topniveau (ikke indlejret under `function`).
- Når modellen beder om at kalde et værktøj, udfør det i din app og inklusiv værktøjets resultat i næste forespørgsel som et `function_call_output` element inden i `input`.
- Hold skemaer minimale; valider input før udførelse.
- Når du bruger `strict: true`, skal alle egenskaber listes i `required` og `additionalProperties: false` er obligatorisk.

> **⚠️ `pydantic_function_tool()` er inkompatibel**: Hjælperen `openai.pydantic_function_tool()` genererer stadig det gamle Chat Completions indlejrede format (`{"type": "function", "function": {"name": ...}}`). Brug det ikke med `responses.create()`. Definér værktøjsskemaer manuelt eller skriv en wrapper til at flade outputtet ud.

### Værktøjsdefineringsformat

Responses API bruger et **fladt** værktøjsformat — `name`, `description`, `parameters` er topnøgle (ikke indlejret under `function`).

**Før (Chat Completions — indlejret):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Efter (Responses API — fladt):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Fuld eksempel:
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

Med `strict: true` (skema-håndhævelse):
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
            "required": ["city_name"],       # Alle egenskaber SKAL være opført
            "additionalProperties": False,   # Krævet for strikt tilstand
        },
    }
]
```

### Værktøjskald rundtur (udfør og returnér resultater)

Når modellen anmoder om et værktøjskald, brug `response.output` elementer + `function_call_output` — **ikke** Chat Completions `role: assistant` + `role: tool` mønsteret.

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
    # Tilføj modellens function_call-elementer til samtalen
    messages.extend(response.output)

    # Udfør hvert værktøj og tilføj resultater
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Få det endelige svar med værktøjsresultater
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Få-skudte værktøjskalds-eksempler

Ved fremsendelse af få-skudte eksempler på værktøjskald i `input` brug `function_call` og `function_call_output` elementer. IDs skal starte med `fc_`.

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
# Indbygget eksempel på websøgning
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Billedinput

Billedindholdselementer ændrer type fra `image_url` til `input_image`, og URL'en ændres fra et indlejret objekt til en flad streng.

### Billedinput — før (Chat Completions)
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

### Billedinput — efter (Responses API, URL)
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

### Billedinput — efter (Responses API, base64)
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

> **Vigtige ændringer**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (indlejret objekt) → `"image_url": "..."` (flad streng — enten HTTPS URL eller `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) migrering

**Tjek først din MAF version** — migreringen afhænger af, om du er på MAF 1.0.0+ eller en pre-1.0.0 beta/rc.

For at tjekke: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

I MAF 1.0.0+ bruger `OpenAIChatClient` **allerede Responses API** — ingen migrering nødvendig.

Hvis kodebasen bruger legacy `OpenAIChatCompletionClient` (som bruger `chat.completions.create`), erstat det med `OpenAIChatClient`:

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

Efter:
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

### MAF pre-1.0.0 (beta/rc releases)

I pre-1.0.0 MAF brugte `OpenAIChatClient` Chat Completions. Opgrader til `agent-framework-openai>=1.0.0` hvor `OpenAIChatClient` bruger Responses API som standard.

> **Bemærk**: `Agent`, `MCPStreamableHTTPTool` og andre MAF API'er forbliver uændrede — kun klientklassens import og instansiering ændres.

## LangChain (`langchain-openai`) migrering

Tilføj `use_responses_api=True` til `ChatOpenAI()`. Opdater også adgang til meddelelsesindhold fra `.content` til `.text`.

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

# ... agent påkaldelse ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Efter:
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

# ... agentpåkaldelse ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Vigtige ændringer**: (1) `use_responses_api=True` i konstruktøren, (2) `.content` → `.text` på responsbeskeder.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->