# Responses API Cheat Sheet (Python + Azure OpenAI)

> Alle onderstaande voorbeelden gaan ervan uit dat `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` en dat `client` al is geïnitialiseerd (zie client-setup).

## Basisverzoek
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Client-setup — EntraID (aanbevolen)
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

## Client-setup — API-sleutel
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Async client-setup — EntraID
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

## Async client-setup — EntraID met expliciete tenant (multi-tenant)

Wanneer de Azure OpenAI resource in een **andere tenant** dan de standaard staat, geef `tenant_id` expliciet door aan de credential. Dit is gebruikelijk in dev/testscenario's waarbij de thuis-tenant van de ontwikkelaar verschilt van de resource tenant.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential voor productie (Azure Container Apps, App Service, enz.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # door gebruiker toegewezen beheerde identiteit
)
# AzureDeveloperCliCredential voor lokale ontwikkeling — expliciete tenant_id is cruciaal
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Ketting: probeer eerst beheerde identiteit, val terug op azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Async client migratie — voor/na

Voorheen (verouderd):
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

Na:
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

## Volledige sync-migratie — voor/na

Voorheen (legacy — Azure OpenAI Chat Completions):
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

Na (Responses API — Azure OpenAI v1 endpoint):
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

## Streaming (sync)
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
        print()  # nieuwe regel aan het einde
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

## Web app streaming — backend-naar-frontend structuur

Bij het migreren van een webapp die SSE/JSONL streamt naar een frontend verandert het **backend-serialisatieformaat**. Ontwerp de nieuwe backend-output zo dat de bestaande toegangs patronen van de frontend behouden blijven zodat de frontend geen aanpassingen behoeft.

**Voorheen** — Chat Completions backend serialiseerde typisch de `choices[0]` dict van elk chunk:
```python
# Oud: geserialiseerde volledige keuze dict per chunk
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend leest: `response.delta.content` (diepe pad in het choice-object).

**Daarna** — Responses API backend geeft een minimale vorm die hetzelfde frontend toegangs pad behoudt:
```python
# Nieuw: zend alleen uit wat de frontend nodig heeft
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
De frontend leest nog steeds `response.delta.content` — **geen frontend wijzigingen nodig**.

> **Belangrijke inzicht**: De streamingvorm van de Responses API (`event.type` + `event.delta`) is fundamenteel anders dan Chat Completions (`chunk.choices[0].delta.content`). Maar het contract tussen backend en frontend bepaal jij. Vorm de backend-output zodat deze overeenkomt met wat de frontend al verwacht.

## Streaming eventvolgorde

Wanneer `stream: true`, wordt de API-events uitgezonden in deze volgorde:
1. `response.created` – response-object geïnitialiseerd
2. `response.in_progress` – generatie gestart
3. `response.output_item.added` – output-item gemaakt
4. `response.content_part.added` – content-deel gestart
5. `response.output_text.delta` – tekstchunks (meerdere, elk met `delta: string`)
6. `response.output_text.done` – tekstgeneratie voltooid
7. `response.content_part.done` – content-deel afgerond
8. `response.output_item.done` – output-item afgerond
9. `response.completed` – volledige response gereed

Voor basale tekststreaming behandel je alleen `response.output_text.delta` (voor tekstchunks) en `response.completed` (voor finish).

## Streaming foutafhandeling in webapps

Bij streaming in een webapp, wikkel de async-iteratie in een `try/except` en lever fouten als JSON zodat de frontend deze netjes kan tonen (bijvoorbeeld bij rate limits, tijdelijke fouten):

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

> **Waarom dit belangrijk is**: Azure OpenAI geeft bij rate limiting een `429 Too Many Requests`. Zonder `try/except` stopt de streaming response stilletjes. Met `try/except` krijgt de frontend `{"error": "Too Many Requests"}` en kan deze een retry prompt tonen.

## Streaming eventtypes (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Gespreksformaat
```python
# De Responses API ondersteunt conversatieformaat via input-array
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

## Foutafhandeling contentfilter

De fout-body structuur wijzigde van Chat Completions naar Responses API.

Voorheen (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Na (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Belangrijkste verschillen:
- De `innererror` wrapper is **verdwenen** — contentfilter details staan nu op topniveau van `error.body`.
- `content_filter_result` (enkelvoud) → `content_filters` (meervoudige array) met binnen elke entry `content_filter_results` (meervoud).
- Elke entry in `content_filters` bevat `blocked`, `source_type`, en `content_filter_results` met details per categorie (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Volledige Responses API contentfilter fout-body structuur:
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

## Raw HTTP migratie (requests/httpx)

Als de app Azure OpenAI REST direct aanroept in plaats van de SDK:

Voorheen (Chat Completions):
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

Na (Responses API):
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

> **Opmerking**: `output_text` is een gemaksattribuut op het Python SDK-object `Response`. De raw REST JSON-response heeft geen topniveau `output_text` veld — de tekst staat op `output[0].content[0].text`.

## Multi-turn gesprek
```python
# Bouw een gesprek met Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Voeg de reactie van de assistent toe aan het gesprek
messages.append({"role": "assistant", "content": response.output_text})

# Ga verder met het gesprek
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Content-getype multi-turn (expliciet `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Multi-turn via `previous_response_id` (alternatief)

In plaats van zelf het gespreksarray te beheren, kun je server-side responses ketenen
met `previous_response_id`. De API slaat elke respons op en
plaatst automatisch voorafgaande beurten ervoor.

```python
# Eerste beurt
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Volgende beurten — geef gewoon het nieuwe gebruikersbericht + vorige reactie-ID door
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Wanneer welk gebruiken:**

| Aanpak | Voordelen | Nadelen |
|---|---|---|
| `input` array (manueel) | Volledige controle over geschiedenis; trimmen/samenvatten mogelijk; geen server-side opslag nodig (`store=False`) | Meer code; je beheert de array zelf |
| `previous_response_id` | Eenvoudigere code; automatische ketening | Vereist `store=True` (standaard); gesprek wordt server-side opgeslagen; geen bewerking van geschiedenis tussen beurten mogelijk |

> **Migratienoot:** De meeste Chat Completions apps beheren al hun eigen berichtenarray, dus omzetten naar `input` array is een directere 1:1 migratie. Gebruik `previous_response_id` voor nieuwe code of als je de conversatiegeschiedenis niet hoeft te manipuleren.

## O-serie redeneer modellen (o1, o3-mini, o3, o4-mini)

O-serie modellen hebben unieke parameterbeperkingen bij migratie naar Responses API.

### Parame-termapping voor o-serie

| Chat Completions (o-serie) | Responses API | Opmerkingen |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Zet hoog (4096+) — redeneertokens tellen mee tegen limiet |
| `reasoning_effort` | `reasoning.effort` | Laat ongewijzigd als aanwezig (laag/midden/hoog) |
| `temperature` | Verwijder of zet op `1` | O-serie accepteert alleen `1` |
| `top_p` | Verwijder | Niet ondersteund op o-serie |
| `seed` | Verwijder | Niet ondersteund in Responses API |

### O-serie voor/na

Voor (Chat Completions met o-serie):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Na (Responses API):
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

> **Opmerking**: O-serie modellen kunnen output bufferen tijdens redeneerlussen voor ze tekst-delta's uitsturen. Streaming werkt nog steeds maar het eerste `response.output_text.delta` event kan langer op zich laten wachten dan bij GPT-modellen.

## Toegang tot redeneertokens
```python
# Redeneermodellen gebruiken interne redenering — je kunt zien hoeveel redeneertokens werden gebruikt
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

> **Belangrijk**: Gebruik `max_output_tokens=1000` (niet 50–200) om rekening te houden met het interne redeneerproces van het model. Het model gebruikt redeneertokens intern voordat de finale output wordt gegenereerd.

## Gestructureerde output — JSON Schema
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

## Gereedschap gebruik

- Definieer functies in `tools` met het **platte Responses API formaat** — `name`, `description`, en `parameters` op het topniveau (niet genest onder `function`).
- Wanneer het model vraagt een tool aan te roepen, voer deze uit in je app en voeg het toolresultaat toe aan het volgende verzoek als een `function_call_output` item binnen `input`.
- Houd schema's minimaal; valideer inputs voor uitvoering.
- Bij gebruik van `strict: true` moeten alle eigenschappen in `required` staan en is `additionalProperties: false` verplicht.

> **⚠️ `pydantic_function_tool()` is incompatibel**: De helper `openai.pydantic_function_tool()` genereert nog steeds het oude geneste Chat Completions formaat (`{"type": "function", "function": {"name": ...}}`). Gebruik dit niet met `responses.create()`. Definieer tool-schemas handmatig of schrijf een wrapper om de output te platte.

### Tool definitie formaat

De Responses API gebruikt een **plat** toolformaat — `name`, `description`, `parameters` zijn top-level keys (niet genest onder `function`).

**Voorheen (Chat Completions — genest):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Daarna (Responses API — plat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Volledig voorbeeld:
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

Met `strict: true` (schema afdwinging):
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
            "required": ["city_name"],       # Alle eigenschappen MOETEN worden vermeld
            "additionalProperties": False,   # Vereist voor strikte modus
        },
    }
]
```

### Tool call round-trip (uitvoeren en resultaten retourneren)

Wanneer het model een tool-aanroep vraagt, gebruik `response.output` items + `function_call_output` — **niet** het Chat Completions patroon `role: assistant` + `role: tool`.

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
    # Voeg de function_call-items van het model toe aan het gesprek
    messages.extend(response.output)

    # Voer elk hulpmiddel uit en voeg resultaten toe
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Verkrijg de definitieve reactie met hulpmiddelresultaten
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Few-shot tool-aanroep voorbeelden

Wanneer je few-shot voorbeelden van tool-aanroepen geeft in `input`, gebruik dan `function_call` en `function_call_output` items. ID's moeten beginnen met `fc_`.

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
# Voorbeeld van ingebouwde webzoekfunctie
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Afbeelding-input

Items van afbeeldingscontent wijzigen type van `image_url` naar `input_image`, en de URL verandert van een genest object naar een platte string.

### Afbeelding-input — voorheen (Chat Completions)
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

### Afbeelding-input — daarna (Responses API, URL)
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

### Afbeelding-input — daarna (Responses API, base64)
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

> **Belangrijke wijzigingen**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (genest object) → `"image_url": "..."` (platte string – ofwel HTTPS URL of `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) migratie

**Controleer eerst je MAF-versie** — de migratie hangt af van of je MAF 1.0.0+ of een pre-1.0.0 beta/rc gebruikt.

Om te controleren: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

In MAF 1.0.0+ gebruikt `OpenAIChatClient` **al de Responses API** — geen migratie nodig.

Als de codebase de legacy `OpenAIChatCompletionClient` gebruikt (die `chat.completions.create` gebruikt), vervang deze dan door `OpenAIChatClient`:

Voorheen:
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

Na:
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

In pre-1.0.0 MAF gebruikte `OpenAIChatClient` Chat Completions. Upgrade naar `agent-framework-openai>=1.0.0` waar `OpenAIChatClient` standaard de Responses API gebruikt.

> **Opmerking**: De `Agent`, `MCPStreamableHTTPTool`, en andere MAF API's blijven ongewijzigd — alleen de client class import en instantiering veranderen.

## LangChain (`langchain-openai`) migratie

Voeg `use_responses_api=True` toe aan `ChatOpenAI()`. Pas ook toegang tot berichtinhoud aan van `.content` naar `.text`.

Voorheen:
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

# ... agentaanroep ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Na:
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

# ... agent-aanroep ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Belangrijke wijzigingen**: (1) `use_responses_api=True` in constructor, (2) `.content` → `.text` op responsberichten.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->