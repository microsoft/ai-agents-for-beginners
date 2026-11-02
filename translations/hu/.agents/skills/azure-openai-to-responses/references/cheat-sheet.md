# Válaszok API Gyorsreferencia (Python + Azure OpenAI)

> Az alábbi összes kódrészlet azt feltételezi, hogy `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` és a `client` már inicializálva van (lásd client beállítás).

## Alap kérelem
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Client beállítás — EntraID (ajánlott)
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

## Client beállítás — API kulcs
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Aszinkron client beállítás — EntraID
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

## Aszinkron client beállítás — EntraID explicit tenant (több bérlős)

Ha az Azure OpenAI erőforrás egy **másik bérlőhöz** tartozik, mint az alapértelmezett, adjuk át a `tenant_id`-t explicit módon a hitelesítő adatoknak. Ez gyakori fejlesztési/tesztelési környezetekben, ahol a fejlesztő otthoni bérlője eltér az erőforrás bérlőjétől.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential éles környezethez (Azure Container Apps, App Service, stb.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # felhasználó által hozzárendelt kezelt identitás
)
# AzureDeveloperCliCredential helyi fejlesztéshez — a tenant_id megadása kritikus
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Lánc: először a kezelt identitást próbálja, majd az azd CLI-re esik vissza
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Async client migráció — előtte/utána

Előtte (elavult):
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

Utána:
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

## Teljes szinkron migráció — előtte/utána

Előtte (régi — Azure OpenAI Chat befejezések):
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

Utána (Válaszok API — Azure OpenAI v1 végpont):
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

## Streaming (szinkron)
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
        print()  # új sor a végén
```

## Streaming (aszinkron)
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

## Webalkalmazás streaming — backend-to-frontend forma

Amikor olyan webalkalmazást migrálunk, amely SSE/JSONL streamel a frontend felé, a **háttér szerializációs formátuma** változik. Tervezd meg az új backend kimenetet úgy, hogy megőrizze a frontend meglévő elérési mintáit, így a frontend nem igényel módosítást.

**Előtte** — A Chat Completions backend tipikusan minden darab `choices[0]` dict-jét szerializálta:
```python
# Régi: sorosított teljes választási szótár darabonként
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
A frontend olvassa: `response.delta.content` (mély útvonala a válasz objektumnak).

**Utána** — A Válaszok API backend minimális formát bocsát ki, amely megőrzi ugyanazt a frontend hozzáférési útvonalat:
```python
# Új: csak azt bocsátja ki, amire a frontendnek szüksége van
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
A frontend továbbra is `response.delta.content`-t olvas — **nincs szükség frontend változtatásra**.

> **Kulcsgondolat**: A Válaszok API streaming formája (`event.type` + `event.delta`) alapvetően eltér a Chat Completionsétől (`chunk.choices[0].delta.content`). De a backend-to-frontend szerződés a saját döntésed. Alakítsd a backend kimenetet úgy, hogy megfeleljen annak, amit a frontend már elvár.

## Streaming eseménysorozat

Amikor `stream: true`, az API az eseményeket ebben a sorrendben bocsátja ki:
1. `response.created` – válasz objektum inicializálva
2. `response.in_progress` – generálás elindult
3. `response.output_item.added` – kimeneti elem létrehozva
4. `response.content_part.added` – tartalmi rész elkezdődött
5. `response.output_text.delta` – szöveg darabok (több, mindegyik `delta: string`)
6. `response.output_text.done` – szöveg generálás befejezve
7. `response.content_part.done` – tartalmi rész befejezve
8. `response.output_item.done` – kimeneti elem befejezve
9. `response.completed` – teljes válasz kész

Egyszerű szöveg streameléshez csak a `response.output_text.delta` (szöveg darabok) és a `response.completed` (befejezés) eseményeket kezeld.

## Streaming hiba kezelés webalkalmazásokban

Amikor webalkalmazásban streamelsz, csomagold aszinkron iterációt `try/except` blokkba, és a hibákat JSON-ként add vissza, hogy a frontend szépen meg tudja jeleníteni (pl. korlátozások, átmeneti hibák):

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

> **Miért fontos ez:** Az Azure OpenAI `429 Too Many Requests` üzenetet ad a korlátozás alatt. `try/except` nélkül a streaming válasz csendben megszakad. Ezzel a blokkal a frontend kap egy `{"error": "Too Many Requests"}`-et és megjeleníthet egy újrapróbálkozási promptot.

## Streaming eseménytípusok (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Beszélgetés formátum
```python
# A Responses API támogatja a párbeszéd formátumot bemeneti tömb használatával
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

## Tartalomszűrő hiba kezelése

A hiba test struktúrája változott a Chat Completionsről a Válaszok API-ra.

Előtte (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Utána (Válaszok API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Fő különbségek:
- Az `innererror` csomagoló **eltűnt** — a tartalomszűrő részletek most közvetlenül az `error.body` tetején vannak.
- Az egyesített `content_filter_result` helyett többes számban `content_filters` tömb található, amely minden elemén belül vannak a `content_filter_results` elemek.
- Minden bejegyzés a `content_filters`-ben tartalmazza a `blocked`, `source_type`, és `content_filter_results` kategóriánkénti részleteit (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Teljes Válaszok API tartalomszűrő hiba test forma:
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

## Nyers HTTP migráció (requests/httpx)

Ha az alkalmazás közvetlenül az Azure OpenAI REST API-t hívja SDK helyett:

Előtte (Chat Completions):
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

Utána (Válaszok API):
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

> **Megjegyzés**: Az `output_text` a Python SDK `Response` objektum kényelmi tulajdonsága. A nyers REST JSON válasz nem rendelkezik felső szintű `output_text` mezővel — a szöveg az `output[0].content[0].text` alatt van.

## Többfordulós beszélgetés
```python
# Építs beszélgetést a Válaszok API-val
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Add hozzá a segítő válaszát a beszélgetéshez
messages.append({"role": "assistant", "content": response.output_text})

# Folytasd a beszélgetést
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Tartalomtípusos többfordulós (explicit `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Többfordulós a `previous_response_id` segítségével (alternatív)

Ahelyett, hogy te magad kezelgetnéd a beszélgetés tömböt, láncolhatod a válaszokat
szerveroldalon a `previous_response_id` használatával. Az API tárol minden választ és
automatikusan előre fűzi az előző fordulókat.

```python
# Első kör
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# További körök — csak add át az új felhasználói üzenetet + az előző válasz azonosítóját
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Mikor melyiket használd:**

| Megközelítés | Előnyök | Hátrányok |
|---|---|---|
| `input` tömb (kézi) | Teljes kontroll a történet felett; lejegyezhető/összefoglalható; nem kell szerveroldali tárolás (`store=False`) | Több kód; te kezeled a tömböt |
| `previous_response_id` | Egyszerűbb kód; automatikus láncolás | Szükséges `store=True` (alapértelmezett); beszélgetés szerveroldalon tárolva; nem lehet módosítani a többi forduló között |

> **Migrációs megjegyzés:** A legtöbb Chat Completions alkalmazás már kezeli saját üzenettömbjét, így az `input` tömbre váltás közvetlen, 1:1 migrációt jelent. A `previous_response_id`-t akkor használd, ha új kódot írsz, vagy nincs szükséged a beszélgetés történet manipulálására.

## O-sorozatú érvelő modellek (o1, o3-mini, o3, o4-mini)

Az O-sorozat modellek egyedi paraméterkorlátokkal rendelkeznek a Válaszok API-ra való migrációnál.

### Paraméter leképezés o-sorozat esetén

| Chat Completions (o-sorozat) | Válaszok API | Megjegyzések |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Magasan állítsd be (4096+) — az érvelési tokenek beleszámítanak a limitbe |
| `reasoning_effort` | `reasoning.effort` | Ha van, hagyd változatlanul (alacsony/közepes/magas) |
| `temperature` | Távolítsd el vagy állítsd `1`-re | Az o-sorozat csak `1`-et fogad el |
| `top_p` | Távolítsd el | Nincs támogatva o-sorozaton |
| `seed` | Távolítsd el | Nem támogatja a Válaszok API |

### O-sorozat előtte/utána

Előtte (Chat Completions o-sorozattal):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Utána (Válaszok API):
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

> **Megjegyzés**: Az o-sorozat modellek érvelés közben tárolhatnak kimenetet, mielőtt szöveg deltákat bocsátanak ki. Streaming továbbra is működik, de az első `response.output_text.delta` esemény később érkezhet, mint GPT modelleknél.

## Érvelési tokenek elérése
```python
# Az érvelő modellek belső érvelést használnak — láthatod, hány érvelő token volt használatban
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

> **Fontos**: Használd a `max_output_tokens=1000`-et (nem 50–200), hogy lefedje az érvelő modellek belső érvelési folyamatait. A modell érvelési tokeneket használ belül, mielőtt a végleges kimenetet előállítja.

## Strukturált kimenet — JSON séma
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

## Eszköz használat

- Definiálj függvényeket a `tools`-ban a **lapos Válaszok API formátumban** — `name`, `description` és `parameters` a felső szinten (nem a `function` alatt).
- Amikor a modell eszköz hívást kér, hajtsd végre az alkalmazásodban, és az eszköz eredményét tedd bele a következő kérésbe `function_call_output` elemként az `input`-ban.
- Tartsd a sémákat minimálisan; validáld a bemeneteket végrehajtás előtt.
- Ha `strict: true`-t használsz, az összes tulajdonságot fel kell sorolni a `required`-ben, és az `additionalProperties: false` kötelező.

> **⚠️ `pydantic_function_tool()` inkompatibilis**: Az `openai.pydantic_function_tool()` helper még mindig a régi Chat Completions beágyazott formátumot generálja (`{"type": "function", "function": {"name": ...}}`). Ne használd a `responses.create()`-al. Definiáld az eszköz sémákat kézzel, vagy írj egy wrapper-t a kimenet laposításához.

### Eszköz definíciós formátum

A Válaszok API **lapos** eszköz formátumot használ — `name`, `description`, `parameters` felső szintű kulcsok (nem a `function` alatt).

**Előtte (Chat Completions — beágyazott):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Utána (Válaszok API — lapos):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Teljes példa:
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

`strict: true`-vel (séma érvényesítés):
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
            "required": ["city_name"],       # Minden tulajdonságot FEL KELL tüntetni
            "additionalProperties": False,   # Szigorú módhoz kötelező
        },
    }
]
```

### Eszköz hívás oda-vissza (végrehajtás és eredmény visszaadása)

Amikor a modell eszköz hívást kér, használd a `response.output` elemeket + `function_call_output`-ot — **nem** a Chat Completions `role: assistant` + `role: tool` mintát.

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
    # Add hozzá a modell function_call elemeit a beszélgetéshez
    messages.extend(response.output)

    # Hajtsa végre az egyes eszközöket és adja hozzá az eredményeket
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Szerezze be a végső választ az eszközök eredményeivel
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Néhány példa eszköz hívásra

Amikor példákat adsz eszköz hívásokra az `input`-ban, használd a `function_call` és `function_call_output` elemeket. Azonosítók `fc_`-vel kell kezdődjenek.

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
# Beépített webes keresési példa
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Kép bemenet

A képtartalom típus `image_url`-ról `input_image`-re változik, és az URL átalakul a beágyazott objektumból lapos stringgé.

### Kép bemenet — előtte (Chat Completions)
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

### Kép bemenet — utána (Válaszok API, URL)
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

### Kép bemenet — utána (Válaszok API, base64)
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

> **Fő változások**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (bejgyazott objektum) → `"image_url": "..."` (lapos string — vagy HTTPS URL vagy `data:image/...;base64,...` adat URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) migráció

**Ellenőrizd először MAF verziódat** — a migráció attól függ, hogy MAF 1.0.0+ vagy pre-1.0.0 béta/rc verzióval dolgozol-e.

Ellenőrzés: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ esetén az `OpenAIChatClient` **már a Válaszok API-t használja** — nem szükséges migráció.

Ha a kód korábban a régi `OpenAIChatCompletionClient`-et használja (`chat.completions.create`), cseréld ki `OpenAIChatClient`-re:

Előtte:
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

Utána:
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

### MAF pre-1.0.0 (beta/rc kiadások)

Pre-1.0.0 MAF esetén az `OpenAIChatClient` még a Chat Completions-t használta. Frissíts agent-framework-openai>=1.0.0-ra, ahol alapból a Válaszok API-t használja.

> **Megjegyzés**: Az `Agent`, `MCPStreamableHTTPTool` és más MAF API-k változatlanok maradnak — csak a kliosztály import és példányosítás változik.

## LangChain (`langchain-openai`) migráció

Add hozzá a `use_responses_api=True` paramétert a `ChatOpenAI()`-hoz. Frissítsd az üzenetek tartalom elérését `.content`-ról `.text`-re.

Előtte:
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

# ... ügynök hívás ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Utána:
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

# ... ügynök hívás ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Fő változások**: (1) `use_responses_api=True` a konstruktorban, (2) `.content` helyett `.text` az válasz üzeneteknél.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->