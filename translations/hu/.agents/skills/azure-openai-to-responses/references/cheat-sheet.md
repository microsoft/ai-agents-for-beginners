# Responses API Gyorssegédlet (Python + Azure OpenAI)

> Az alábbi összes példakód feltételezi, hogy `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` és hogy a `client` már inicializálva van (lásd: kliens beállítása).

## Alap kérés
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Kliens beállítása — EntraID (ajánlott)
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

## Kliens beállítása — API kulcs
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Aszinkron kliens beállítása — EntraID
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

## Aszinkron kliens beállítása — EntraID explicit tenanttel (többtenantos)

Amikor az Azure OpenAI erőforrás egy **másik tenantban** van mint az alapértelmezett, az azonosítóhoz explicit módon add át a `tenant_id`-t. Ez gyakori a fejlesztési/tesztelési helyzetekben, amikor a fejlesztő home tenanja eltér az erőforrás tenantjától.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential a gyártásban (Azure Container Apps, App Service stb.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # felhasználó által hozzárendelt kezelt identitás
)
# AzureDeveloperCliCredential helyi fejlesztéshez — az explicit tenant_id kritikus
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Lánc: először a kezelt identitást próbáljuk, majd az azd CLI-re esik vissza
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Aszinkron kliens migráció — előtt/után

Előtt (elavult):
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

Után:
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

## Teljes szinkron migráció — előtt/után

Előtt (régi — Azure OpenAI Chat Befejezések):
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

Után (Responses API — Azure OpenAI v1 végpont):
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

## Webalkalmazás streaming — backendből frontend felé alak

Amikor egy webalkalmazást migrálsz, ami SSE/JSONL formában streamel a frontend felé, a **backend szerializációs formátum** változik. Alakítsd az új backend kimenetet úgy, hogy megőrizze a frontend meglévő elérési mintáit, így a frontendnek nem kell változtatni.

**Előtte** — a Chat Befejezések backend tipikusan a chunk-ok `choices[0]` dict-jét szerializálta:
```python
# Régi: egy tömbönként sorosított teljes választás szótár
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend olvasás: `response.delta.content` (mély útvonal a választ objektumban).

**Utána** — a Responses API backend egy minimális alakot ad ki, mely megőrzi ugyanazt a frontend elérési útvonalat:
```python
# Új: csak azt bocsátja ki, amire a frontendnek szüksége van
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend továbbra is olvassa a `response.delta.content`-et — **nem szükséges frontend módosítás**.

> **Fontos meglátás**: A Responses API streaming alakja (`event.type` + `event.delta`) alapvetően eltér a Chat Befejezésektől (`chunk.choices[0].delta.content`). De a backendből frontendbe szóló szerződés a tiéd. Alakítsd a backend kimenetet úgy, hogy megfeleljen annak, amit a frontend már elvár.

## Streaming eseménysorozat

Amikor `stream: true`, az API az eseményeket ebben a sorrendben bocsátja ki:
1. `response.created` – a válasz objektum inicializálva
2. `response.in_progress` – a generálás elkezdődött
3. `response.output_item.added` – kimeneti elem létrehozva
4. `response.content_part.added` – tartalmi rész elkezdődött
5. `response.output_text.delta` – szövegrészletek (többszörös, mindegyikben `delta: string`)
6. `response.output_text.done` – szöveg generálás befejezve
7. `response.content_part.done` – tartalmi rész befejezve
8. `response.output_item.done` – kimeneti elem befejezve
9. `response.completed` – teljes válasz elkészült

Alap szöveg streaminghez csak kezelni kell `response.output_text.delta` (szövegrészletekhez) és `response.completed` (befejezéshez).

## Streaming hibakezelés webalkalmazásokban

Webalkalmazásban a streamelést `try/except` blokkba kell csomagolni, és a hibákat JSON formában kell továbbítani, hogy a frontend szépen tudja megjeleníteni (pl. túlterhelés, átmeneti hibák):

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

> **Miért fontos ez**: Az Azure OpenAI `429 Too Many Requests` választ ad túlterhelés esetén. `try/except` nélkül a streaming válasz csendben megszakad. Ezzel együtt a frontend kapja a `{"error": "Too Many Requests"}` üzenetet, és tud retry promptot mutatni.

## Streaming eseménytípusok (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Beszélgetés formátum
```python
# A Responses API támogatja a beszélgetés formátumot bemeneti tömbön keresztül
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

## Tartalomszűrő hibakezelés

A hiba test szerkezete megváltozott a Chat Befejezésekről a Responses API-ra.

Előtte (Chat Befejezések):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Utána (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Fő különbségek:
- Az `innererror` csomagoló **eltűnt** — a tartalomszűrő részletek mostantól az `error.body` tetején vannak.
- `content_filter_result` (egyes szám) → `content_filters` (többes szám tömb), mely tartalmaz `content_filter_results` (többes szám) elemeket minden bejegyzésben.
- Minden bejegyzés a `content_filters`-ben tartalmazza a `blocked`, `source_type`, és `content_filter_results` mezőket kategóriánkénti részletekkel (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Teljes Responses API tartalomszűrő hiba test alak:
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

Ha az alkalmazás közvetlenül hívja az Azure OpenAI REST-et SDK helyett:

Előtte (Chat Befejezések):
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

Utána (Responses API):
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

> **Megjegyzés**: Az `output_text` a Python SDK `Response` objektumának kényelmi tulajdonsága. A nyers REST JSON válasznak nincs top-level `output_text` mezője — a szöveg az `output[0].content[0].text` alatt található.

## Többfordulós beszélgetés
```python
# Beszélgetés létrehozása a Responses API-val
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# A segítő válaszának hozzáadása a beszélgetéshez
messages.append({"role": "assistant", "content": response.output_text})

# A beszélgetés folytatása
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

### Többfordulós `previous_response_id`-vel (alternatíva)

Ahelyett, hogy te magad kezelné a beszélgetés tömböt, láncolhatsz válaszokat
szerveroldalon a `previous_response_id` használatával. Az API eltárolja az egyes válaszokat és
automatikusan előfűzi a korábbi fordulókat.

```python
# Első kör
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# További körök — csak továbbítsd az új felhasználói üzenetet + az előző válasz azonosítóját
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
| `input` tömb (kézi) | Teljes kontroll a történelem felett; lehet vágni/összefoglalni; nincs szükség szerveroldali tárolásra (`store=False`) | Több kód; neked kell kezelni a tömböt |
| `previous_response_id` | Egyszerűbb kód; automatikus láncolás | Megköveteli a `store=True`-t (alapértelmezett); a beszélgetés szerveroldalon tárolódik; nem módosítható a történelem fordulók között |

> **Migrációs megjegyzés:** A legtöbb Chat Befejezések alkalmazás már kezeli a saját üzenettömbjét, így az `input` tömbre váltás egy közvetlen 1:1 migráció. Használd a `previous_response_id`-t új kódokhoz vagy ha nem kell módosítani a beszélgetés előzményeit.

## O-sorozatú érvelő modellek (o1, o3-mini, o3, o4-mini)

Az O-sorozat modelleknek egyedi paraméter korlátai vannak a Responses API-ra való migrációkor.

### Paraméter térkép az o-sorozathoz

| Chat Befejezések (o-sorozat) | Responses API | Megjegyzések |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | Magas értékre állítás (4096+) — a gondolkodási tokenek beleszámítanak a korlátba |
| `reasoning_effort` | `reasoning.effort` | Hagyd változatlanul, ha jelen van (alacsony/közepes/magas) |
| `temperature` | Távolítsd el vagy állítsd `1`-re | Az O-sorozat csak az `1`-et fogadja el |
| `top_p` | Távolítsd el | Nem támogatott az o-sorozaton |
| `seed` | Távolítsd el | Nem támogatott a Responses API-ban |

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

Utána (Responses API):
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

> **Megjegyzés**: Az O-sorozat modellek kibővítik a kimenetet a gondolkodási fázis alatt, mielőtt a szövegdeltákat kibocsátanák. Az adatfolyam továbbra is működik, de az első `response.output_text.delta` esemény hosszabb késéssel érkezhet, mint a GPT-modelleknél.

## Gondolkodási tokenek elérése
```python
# A következtetési modellek belső következtetést használnak — láthatod, hány következtetési token lett felhasználva
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

> **Fontos**: Használd a `max_output_tokens=1000` értéket (nem 50–200-at), hogy számolni tudj a gondolkodó modellek belső gondolkodási folyamatával. A modell belsőleg gondolkodási tokeneket használ, mielőtt előállítja a végső kimenetet.

## Strukturált kimenet — JSON Séma
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

## Eszközhasználat

- Definiálj függvényeket a `tools` alatt a **lapos Responses API formátumban** — `name`, `description` és `parameters` a legfelső szinten, nem a `function` alatt.
- Amikor a modell eszközhívást kér, hajtsd végre az alkalmazásodban, és az eszközhívás eredményét küldd bele a következő kérésbe `function_call_output` elemként az `input` részen belül.
- Tartsd minimálisra a sémákat; validáld a bemeneteket a végrehajtás előtt.
- Ha `strict: true` a beállítás, minden tulajdonságot fel kell sorolni a `required`-ben, és az `additionalProperties: false` kötelező.

> **⚠️ A `pydantic_function_tool()` inkompatibilis**: Az `openai.pydantic_function_tool()` segédfüggvény még mindig a régi Chat Completions beágyazott formátumot generálja (`{"type": "function", "function": {"name": ...}}`). Ne használd a `responses.create()`-al. Definiáld kézzel az eszköz sémákat, vagy írj egy wrappert, hogy laposítsd az outputot.

### Eszközdefiníciós formátum

A Responses API **lapos** eszközformátumot használ — `name`, `description`, `parameters` legfelső szintű kulcsok, nem a `function` alatt.

**Előtte (Chat Completions — beágyazott):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Utána (Responses API — lapos):**
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

`strict: true`-val (sémaellenőrzéssel):
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
            "additionalProperties": False,   # Kötelező a szigorú módhoz
        },
    }
]
```

### Eszközhívás oda-vissza (végrehajtás és eredmény visszaadása)

Amikor a modell eszközhívást kér, használj `response.output` elemeket + `function_call_output`-ot — **ne** a Chat Completions `role: assistant` + `role: tool` mintáját.

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

### Kevéspéldás eszközhívási példák

Ha kevéspéldás eszközhívási példákat adsz meg az `input`-ban, használj `function_call` és `function_call_output` elemeket. Az azonosítóknak `fc_`-vel kell kezdődniük.

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

## Kép bevitel

A kép tartalmi elemek típusa megváltozik `image_url`-ről `input_image`-re, és a URL egy beágyazott objektum helyett lapos stringgé válik.

### Kép bevitel — előtte (Chat Completions)
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

### Kép bevitel — utána (Responses API, URL)
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

### Kép bevitel — utána (Responses API, base64)
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

> **Főbb változások**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (beágyazott objektum) → `"image_url": "..."` (lapos string — lehet HTTPS URL vagy `data:image/...;base64,...` adat URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) migráció

**Először ellenőrizd a MAF verziódat** — a migráció attól függ, hogy MAF 1.0.0+ vagy korábbi, pre-1.0.0 béta/rc verziót használsz-e.

Ellenőrzéshez: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

A MAF 1.0.0+-ban az `OpenAIChatClient` **már a Responses API-t használja** — nincs szükség migrációra.

Ha a kódbázis a régi `OpenAIChatCompletionClient`-et használja (`chat.completions.create`-et), cseréld le `OpenAIChatClient`-re:

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

A pre-1.0.0 MAF-ban az `OpenAIChatClient` Chat Completions-t használt. Frissíts `agent-framework-openai>=1.0.0`-ra, ahol az `OpenAIChatClient` alapértelmezetten a Responses API-t használja.

> **Megjegyzés**: Az `Agent`, `MCPStreamableHTTPTool` és más MAF API-k változatlanok maradnak — csak a kliensosztály importja és példányosítása változik.

## LangChain (`langchain-openai`) migráció

Add hozzá a `use_responses_api=True` paramétert a `ChatOpenAI()`-hoz. Frissítsd az üzenetek tartalmának elérését `.content`-ről `.text`-re.

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

# ... ügynök meghívás ...
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

# ... ügynök meghívás ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Főbb változások**: (1) `use_responses_api=True` a konstruktorban, (2) `.content` → `.text` a válasz üzeneteken.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->