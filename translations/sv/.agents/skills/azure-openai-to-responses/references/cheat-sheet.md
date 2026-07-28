# Responses API Fuskark (Python + Azure OpenAI)

> Alla kodavsnitt nedan förutsätter `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` och att `client` redan är initierad (se klientinställning).

## Grundläggande förfrågan
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Klientinställning — EntraID (rekommenderat)
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

## Klientinställning — API-nyckel
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Asynkron klientinställning — EntraID
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

## Asynkron klientinställning — EntraID med explicit hyresgäst (multi-tenant)

När Azure OpenAI-resursen finns i en **annan hyresgäst** än standard, skicka `tenant_id` explicit till credential. Detta är vanligt i utvecklings- och testscenarion där utvecklarens hemhyresgäst skiljer sig från resursens hyresgäst.

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
# Kedja: försök med hanterad identitet först, fall tillbaka till azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Asynkron klientmigration — före/efter

Före (föråldrat):
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

## Full synkron migration — före/efter

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
    model="gpt-4.1",
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
        print()  # radbrytning i slutet
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

## Webbappstreaming — backend-till-frontend-form

När du migrerar en webbapp som strömmar SSE/JSONL till frontend, ändras **backendens serialiseringsformat**. Utforma backendutdata så att frontendens befintliga åtkomstmönster bevaras så att frontend inte behöver förändras.

**Före** — Chat Completions backend serialiserade typiskt varje chunks `choices[0]` dict:
```python
# Gammal: serialiserad full serienygdsordbok per bit
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend läser: `response.delta.content` (djup sökväg in i choice-objektet).

**Efter** — Responses API backend skickar minimal form som bevarar samma frontendåtkomst:
```python
# Nytt: skicka bara ut det frontend behöver
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend läser fortfarande `response.delta.content` — **inga ändringar i frontend behövs**.

> **Viktig insikt**: Responses API streamingform (`event.type` + `event.delta`) skiljer sig fundamentalt från Chat Completions (`chunk.choices[0].delta.content`). Men kontraktet mellan backend och frontend definierar du själv. Forma backendutdata för att matcha vad frontenden redan förväntar sig.

## Sekvens för streaminghändelser

När `stream: true`, skickar API:n händelser i denna ordning:
1. `response.created` – svarobjekt initierat
2. `response.in_progress` – generering påbörjad
3. `response.output_item.added` – outputobjekt skapat
4. `response.content_part.added` – innehållsdel påbörjad
5. `response.output_text.delta` – textbitar (flera, var och en med `delta: string`)
6. `response.output_text.done` – textgenerering klar
7. `response.content_part.done` – innehållsdel klar
8. `response.output_item.done` – outputobjekt klart
9. `response.completed` – fullständigt svar klart

För grundläggande textstreaming, hantera bara `response.output_text.delta` (för textbitar) och `response.completed` (för färdig).

## Felhantering vid streaming i webbappar

När du strömmar i en webbapp, omslut den asynkrona iterationen i `try/except` och yield:a fel som JSON så frontenden kan visa dem snyggt (t.ex. gränser för förfrågningar, tillfälliga fel):

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

> **Varför detta är viktigt**: Azure OpenAI returnerar `429 Too Many Requests` vid rate limiting. Utan `try/except` dör streamingen tyst. Med den får frontenden `{"error": "Too Many Requests"}` och kan visa en uppmaning om försök igen.

## Streaming-händelsetyper (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Samtalsformat
```python
# Responses API stöder konversationsformat via input-array
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

## Felhantering för innehållsfilter

Felkroppens struktur ändrades från Chat Completions till Responses API.

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
- `innererror`-omslutaren är **borta** — innehållsfilterdetaljer finns nu på översta nivån av `error.body`.
- `content_filter_result` (singular) → `content_filters` (plural array) som innehåller `content_filter_results` (plural) inuti varje post.
- Varje post i `content_filters` inkluderar `blocked`, `source_type` och `content_filter_results` med per-kategori detaljer (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Fullständig Responses API innehållsfilter felkroppsstruktur:
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

## Rå HTTP-migration (requests/httpx)

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

> **Notera**: `output_text` är en bekvämlighetsegenskap på Python SDK:ns `Response`-objekt. Det råa REST JSON-svaret har inte ett översta `output_text`-fält — texten finns på `output[0].content[0].text`.

## Fleromgångskonversation
```python
# Bygg en konversation med Responses API
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

Innehållstypad fleromgång (explicit `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Fleromgång via `previous_response_id` (alternativ)

Istället för att hantera konversations-arrayen själv kan du kedja svar
serversidan med `previous_response_id`. API:n lagrar varje svar och
lägger automatiskt till tidigare varv.

```python
# Första turen
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Efterföljande turer — skicka bara det nya användarmeddelandet + föregående svar-ID
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**När man använder vad:**

| Tillvägagångssätt | Fördelar | Nackdelar |
|---|---|---|
| `input`-array (manuell) | Full kontroll över historik; kan trimma/sammanfatta; ingen serversideslagring behövs (`store=False`) | Mer kod; du hanterar arrayen |
| `previous_response_id` | Enklare kod; automatisk koppling | Kräver `store=True` (standard); konversation lagras serverside; kan inte ändra historik mellan varv |

> **Migreringsnotis:** De flesta Chat Completions-appar hanterar redan egna meddelandearray, så att konvertera till `input`-array är en mer direkt 1:1-migrering. Använd `previous_response_id` för ny kod eller när du inte behöver manipulera konversationshistoriken.

## O-seriens resonemangsmodeller (o1, o3-mini, o3, o4-mini)

O-seriens modeller har unika parameterbegränsningar när man migrerar till Responses API.

### Parametermappning för o-serien

| Chat Completions (o-serien) | Responses API | Noteringar |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Sätt högt (4096+) — resonemangstoken räknas mot gränsen |
| `reasoning_effort` | `reasoning.effort` | Behåll som den är om närvarande (låg/medel/hög) |
| `temperature` | Ta bort eller sätt till `1` | O-serien accepterar bara `1` |
| `top_p` | Ta bort | Stöds inte på o-serien |
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

> **Observera**: O-seriens modeller kan buffra utdata under resonemang innan de skickar textdelar. Streaming fungerar fortfarande men första `response.output_text.delta`-händelsen kan komma efter en längre fördröjning än med GPT-modeller.

## Åtkomst till resonemangstoken
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

> **Viktigt**: Använd `max_output_tokens=1000` (inte 50–200) för att rymma resonemangsmodellens interna resonemangsprocess. Modellen använder resonemangstoken internt innan slutligt svar genereras.

## Strukturerad utdata — JSON-schema
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

- Definiera funktioner i `tools` med det **platta Responses API-formatet** — `name`, `description` och `parameters` på översta nivån (inte inbäddat under `function`).
- När modellen ber om att kalla ett verktyg, kör det i din app och inkludera resultatet som ett `function_call_output`-objekt inom `input` i nästa förfrågan.
- Håll scheman minimala; validera indata innan körning.
- Vid användning av `strict: true` måste alla egenskaper listas i `required` och `additionalProperties: false` är obligatoriskt.

> **⚠️ `pydantic_function_tool()` är inkompatibel**: Hjälpmetoden `openai.pydantic_function_tool()` genererar fortfarande det gamla, inbäddade Chat Completions-formatet (`{"type": "function", "function": {"name": ...}}`). Använd inte med `responses.create()`. Definiera verktygsscheman manuellt eller skriv en wrapper för att platta ut output.

### Verktygsdefinitionsformat

Responses API använder ett **platt** verktygsformat — `name`, `description`, `parameters` är nycklar på översta nivån (inte inbäddade under `function`).

**Före (Chat Completions — inbäddat):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Efter (Responses API — platt):**
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

Med `strict: true` (schema-uppfyllnad):
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
            "additionalProperties": False,   # Krävs för strikt läge
        },
    }
]
```

### Verktygsanrop runt-resa (kör och returnera resultat)

När modellen ber om ett verktygsanrop, använd `response.output`-objekt + `function_call_output` — **inte** Chat Completions `role: assistant` + `role: tool`-mönster.

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

### Få-skott-exempel på verktygsanrop

När du tillhandahåller några exempel på verktygsanrop i `input`, använd `function_call` och `function_call_output`-objekt. ID:n måste börja med `fc_`.

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
# Inbyggt exempel på webbsökning
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Bildindata

Bildinnehållsobjekt ändrar typ från `image_url` till `input_image`, och URL:en ändras från ett inbäddat objekt till en platt sträng.

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

> **Viktiga förändringar**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (inbäddat objekt) → `"image_url": "..."` (platt sträng — antingen HTTPS URL eller `data:image/...;base64,...`-data-URI), (3) `"type": "text"` → `"type": "input_text"`.

## Migrering för Microsoft Agent Framework (MAF)

**Kontrollera din MAF-version först** — migreringen beror på om du använder MAF 1.0.0+ eller en pre-1.0.0 beta/rc.

För att kontrollera: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

I MAF 1.0.0+ använder `OpenAIChatClient` **redan Responses API** — ingen migrering behövs.

Om kodbasen använder det gamla `OpenAIChatCompletionClient` (som använder `chat.completions.create`), byt ut det mot `OpenAIChatClient`:

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

### MAF pre-1.0.0 (beta/rc-versioner)

I pre-1.0.0 MAF användes Chat Completions i `OpenAIChatClient`. Uppgradera till `agent-framework-openai>=1.0.0` där `OpenAIChatClient` använder Responses API som standard.

> **Notera**: `Agent`, `MCPStreamableHTTPTool` och andra MAF-API:er är oförändrade — endast klientklassimport och instantiationssätt ändras.

## LangChain (`langchain-openai`) migrering

Lägg till `use_responses_api=True` till `ChatOpenAI()`. Uppdatera också åtkomst till meddelandeinnehåll från `.content` till `.text`.

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

> **Viktiga förändringar**: (1) `use_responses_api=True` i konstruktorn, (2) `.content` → `.text` på svarmeddelanden.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->