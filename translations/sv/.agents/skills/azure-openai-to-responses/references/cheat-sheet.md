# Responses API Fuskblad (Python + Azure OpenAI)

> Alla kodsnuttar nedan förutsätter `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` och att `client` redan är initierad (se klientuppsättning).

## Enkel förfrågan
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Klientuppsättning — EntraID (rekommenderat)
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

## Klientuppsättning — API-nyckel
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Async klientuppsättning — EntraID
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

## Async klientuppsättning — EntraID med explicit tenant (multi-tenant)

När Azure OpenAI-resursen finns i en **annan tenant** än standard, skicka `tenant_id` explicit till credential. Detta är vanligt i utvecklings-/testscenarier där utvecklarens hemmatenant skiljer sig från resurstenanten.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential för produktion (Azure Container Apps, App Service, etc.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # användartilldelad hanterad identitet
)
# AzureDeveloperCliCredential för lokal utveckling — explicit tenant_id är avgörande
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Kedja: försök hanterad identitet först, fallback till azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Async klientmigrering — före/efter

Före (föråldrat):
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4o",
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

## Full synkron migrering — före/efter

Före (legacy — Azure OpenAI Chat Completions):
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

Efter (Responses API — Azure OpenAI v1-endpoint):
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
        print()  # ny rad i slutet
```

## Streaming (async)
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

## Webbapp-streaming — backend-till-frontend-format

Vid migrering av en webbapp som streamar SSE/JSONL till frontend ändras **backend-serialiseringsformatet**. Designa den nya backendutgången för att bevara frontends befintliga åtkomstmönster så att frontend inte behöver ändras.

**Före** — Chat Completions backend serialiserade vanligtvis varje chunks `choices[0]` dict:
```python
# Gammal: serialiserad komplett valordbok per chunk
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend läser: `response.delta.content` (djup väg in i choice-objektet).

**Efter** — Responses API backend emitterar en minimal form som bevarar samma frontendåtkomstväg:
```python
# Ny: sänd endast det som frontend behöver
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend läser fortfarande `response.delta.content` — **inga frontendändringar behövs**.

> **Viktig insikt**: Responses API streamingformat (`event.type` + `event.delta`) skiljer sig fundamentalt från Chat Completions (`chunk.choices[0].delta.content`). Men kontraktet backend-till-frontend definierar du själv. Forma backendutgången för att matcha vad frontend redan förväntar sig.

## Streaming händelsesekvens

När `stream: true` emitterar API:et händelser i följande ordning:
1. `response.created` – svarobjekt initierat
2. `response.in_progress` – generering påbörjad
3. `response.output_item.added` – utdataobjekt skapat
4. `response.content_part.added` – innehållsdel påbörjad
5. `response.output_text.delta` – textchunkar (flera, varje med `delta: string`)
6. `response.output_text.done` – textgenerering slutförd
7. `response.content_part.done` – innehållsdel färdig
8. `response.output_item.done` – utdataobjekt färdigt
9. `response.completed` – fullt svar komplett

Vid grundläggande textstreaming hantera endast `response.output_text.delta` (textchunkar) och `response.completed` (slut).

## Felhantering vid streaming i webbappar

Vid streaming i en webbapp, omslut den asynkrona iterationen i `try/except` och yielda fel som JSON så frontend kan visa dem snyggt (t.ex. rate limits, tillfälliga fel):

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

> **Varför detta är viktigt**: Azure OpenAI returnerar `429 Too Many Requests` vid rate limiting. Utan `try/except` dör streamingen tyst. Med den får frontend `{"error": "Too Many Requests"}` och kan visa en återförsöksfråga.

## Streaming händelstyper (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Konversationsformat
```python
# Responses API stöder konversationsformat via inmatningsarray
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

## Felhantering innehållsfilter

Felstrukturen förändrades från Chat Completions till Responses API.

Före (Chat Completions):
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

Viktiga skillnader:
- `innererror`-wrappern är **borttagen** — innehållsfilterdetaljer finns nu på översta nivån i `error.body`.
- `content_filter_result` (singular) → `content_filters` (plural array) innehållande `content_filter_results` (plural) i varje post.
- Varje post i `content_filters` innehåller `blocked`, `source_type` och `content_filter_results` med per-kategori detaljer (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Full Responses API innehållsfilter felkroppsstruktur:
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

## Rå HTTP-migrering (requests/httpx)

Om appen anropar Azure OpenAI REST direkt istället för att använda SDK:

Före (Chat Completions):
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

> **Observera**: `output_text` är en bekvämlighets-egenskap i Python SDK:s `Response`-objekt. Den råa REST JSON-responsen har inte ett toppen-nivå `output_text`-fält — texten finns på `output[0].content[0].text`.

## Flerstegs-konversation
```python
# Skapa en konversation med Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Lägg till assistentens svar i konversationen
messages.append({"role": "assistant", "content": response.output_text})

# Fortsätt konversationen
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Content-typad flerstegs (explicit `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Flerstegs via `previous_response_id` (alternativ)

Istället för att hantera konversationsarrayen själv kan du kedja svar
server-side med `previous_response_id`. API:et lagrar varje svar och
lägger automatiskt till tidigare steg.

```python
# Första draget
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Efterföljande drag — skicka bara det nya användarmeddelandet + tidigare svar-ID
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**När man använder vilket:**

| Tillvägagångssätt | Fördelar | Nackdelar |
|---|---|---|
| `input` array (manuell) | Full kontroll över historik; kan trimma/sammanfatta; kräver ingen serverlagring (`store=False`) | Mer kod; du hanterar arrayen |
| `previous_response_id` | Enklare kod; automatiska kedjor | Kräver `store=True` (standard); konversation lagras server-side; kan inte ändra historik mellan steg |

> **Migreringsnotis:** De flesta Chat Completions-appar hanterar redan sin egen meddelande-array så att konvertera till `input` array är en direkt 1:1-migrering. Använd `previous_response_id` för ny kod eller när du inte behöver manipulera konversationshistoriken.

## O-seriens resonemangsmodeller (o1, o3-mini, o3, o4-mini)

O-seriens modeller har unika parameterbegränsningar vid migrering till Responses API.

### Parameterkarta för o-serien

| Chat Completions (o-serien) | Responses API | Noteringar |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Sätt högt (4096+) — resonemangstokens räknas mot gränsen |
| `reasoning_effort` | `reasoning.effort` | Behåll som den är om den finns (low/medium/high) |
| `temperature` | Ta bort eller sätt till `1` | O-serien accepterar endast `1` |
| `top_p` | Ta bort | Stöds inte i o-serien |
| `seed` | Ta bort | Stöds inte i Responses API |

### O-serien före/efter

Före (Chat Completions med o-serien):
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

> **Notera**: O-seriens modeller kan buffra utdata under resonemang innan text-delta emitteras. Streaming fungerar fortfarande men första `response.output_text.delta`-händelsen kan komma efter längre fördröjning jämfört med GPT-modeller.

## Åtkomst till resonemangstokens
```python
# Resonemangsmodeller använder intern resonemang — du kan se hur många resonemangstoken som användes
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

> **Viktigt**: Använd `max_output_tokens=1000` (inte 50–200) för att tillgodose resonemangsmodellernas interna process. Modellen använder resonemangstokens internt innan slutgiltig output genereras.

## Strukturerad output — JSON Schema
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

## Verktygsanvändning

- Definiera funktioner i `tools` med **flat Responses API-format** — `name`, `description` och `parameters` på toppnivå (inte inbäddade under `function`).
- När modellen begär att kalla ett verktyg, kör det i din app och inkludera verktygsresultatet i nästa förfrågan som ett `function_call_output` objekt inom `input`.
- Håll scheman minimala; validera indata före körning.
- Vid användning av `strict: true` måste alla egenskaper listas i `required` och `additionalProperties: false` är obligatoriskt.

> **⚠️ `pydantic_function_tool()` är inkompatibel**: Hjälpfunktionen `openai.pydantic_function_tool()` genererar fortfarande gamla Chat Completions-nestade formatet (`{"type": "function", "function": {"name": ...}}`). Använd inte med `responses.create()`. Definiera verktygsscheman manuellt eller skriv en wrapper som plattar ut outputen.

### Verktygsdefinitionsformat

Responses API använder ett **flatt** verktygsformat — `name`, `description`, `parameters` är toppnycklar (inte inbäddade under `function`).

**Före (Chat Completions — inbäddat):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Efter (Responses API — flatt):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Fullständigt exempel:
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

Med `strict: true` (schema enforcement):
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
            "required": ["city_name"],       # Alla egenskaper MÅSTE listas
            "additionalProperties": False,   # Obligatorisk för strikt läge
        },
    }
]
```

### Verktygscall round-trip (exekvera och returnera resultat)

När modellen efterfrågar en verktygscall, använd `response.output`-objekt + `function_call_output` — **inte** Chat Completions `role: assistant` + `role: tool`-mönster.

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
    # Lägg till modellens function_call-poster i konversationen
    messages.extend(response.output)

    # Kör varje verktyg och lägg till resultaten
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Hämta slutligt svar med verktygsresultat
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Few-shot verktygscall-exempel

Vid few-shot-exempel av verktygscall i `input`, använd `function_call` och `function_call_output` objekt. ID:n måste börja med `fc_`.

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
# Exempel på inbyggd webbsökning
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Bildindata

Bildinnehållsobjekt ändrar typ från `image_url` till `input_image`, och URL ändras från ett inbäddat objekt till en platt sträng.

### Bildindata — före (Chat Completions)
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

### Bildindata — efter (Responses API, URL)
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

### Bildindata — efter (Responses API, base64)
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

> **Viktiga ändringar**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (inbäddat objekt) → `"image_url": "..."` (platt sträng — antingen HTTPS-URL eller `data:image/...;base64,...` data-URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) migrering

**Kolla din MAF-version först** — migreringen beror på om du använder MAF 1.0.0+ eller en pre-1.0.0 beta/rc.

För att kolla: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

I MAF 1.0.0+ använder `OpenAIChatClient` **redan Responses API** — ingen migrering krävs.

Om kodbasen använder legacy `OpenAIChatCompletionClient` (som använder `chat.completions.create`), ersätt den med `OpenAIChatClient`:

Före:
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

### MAF pre-1.0.0 (beta/rc-releaser)

I pre-1.0.0 MAF använde `OpenAIChatClient` Chat Completions. Uppgradera till `agent-framework-openai>=1.0.0` där `OpenAIChatClient` använder Responses API som standard.

> **Notera**: `Agent`, `MCPStreamableHTTPTool` och andra MAF-API:er är oförändrade — endast klientklassimport och instansiering ändras.

## LangChain (`langchain-openai`) migrering

Lägg till `use_responses_api=True` i `ChatOpenAI()`. Uppdatera även åtkomst till meddelandeinnehåll från `.content` till `.text`.

Före:
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

# ... agentanrop ...
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

# ... agentanrop ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Viktiga ändringar**: (1) `use_responses_api=True` i konstruktorn, (2) `.content` → `.text` på responsmeddelanden.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->