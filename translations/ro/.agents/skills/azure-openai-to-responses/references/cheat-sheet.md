# Foaie de trucuri Responses API (Python + Azure OpenAI)

> Toate fragmentele de cod de mai jos presupun `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` și că `client` este deja inițializat (vezi configurarea clientului).

## Cerere de bază
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Configurarea clientului — EntraID (recomandat)
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

## Configurarea clientului — Cheie API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Configurarea clientului asincron — EntraID
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

## Configurarea clientului asincron — EntraID cu tenant explicit (multi-tenant)

Când resursa Azure OpenAI este într-un **tenant diferit** de cel implicit, transmiteti `tenant_id` explicit în credential. Acest lucru este comun în scenarii de dev/test unde tenantul principal al dezvoltatorului diferă de cel al resursei.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential pentru producție (Azure Container Apps, App Service, etc.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # identitate gestionată atribuită utilizatorului
)
# AzureDeveloperCliCredential pentru dezvoltare locală — tenant_id explicit este esențial
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Lanț: încearcă mai întâi identitatea gestionată, apoi revino la azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migrarea clientului asincron — înainte/după

Înainte (depreciat):
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

După:
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

## Migrarea completă sincronă — înainte/după

Înainte (vechi — Azure OpenAI Chat Completions):
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

După (Responses API — Endpoint Azure OpenAI v1):
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

## Streaming (sincron)
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
        print()  # linie nouă la sfârșit
```

## Streaming (asincron)
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

## Streaming aplicație web — structură backend-către-frontend

Când migrați o aplicație web care transmite SSE/JSONL către frontend, **formatul de serializare de pe backend** se schimbă. Proiectați ieșirea noului backend pentru a păstra modelele de acces existente ale frontend-ului astfel încât frontend-ul să nu necesite modificări.

**Înainte** — backend Chat Completions serializa de obicei dicționarul `choices[0]` al fiecărui chunk:
```python
# Vechi: dict complet alegere serializat per chunk
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Citirea de pe frontend: `response.delta.content` (cale profundă în obiectul choice).

**După** — backend Responses API emite o formă minimală care păstrează aceeași cale de acces de pe frontend:
```python
# Nou: emit doar ceea ce are nevoie frontend-ul
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend încă citește `response.delta.content` — **nu sunt necesare modificări frontend**.

> **Observație cheie**: Forma de streaming Responses API (`event.type` + `event.delta`) este fundamental diferită de cea din Chat Completions (`chunk.choices[0].delta.content`). Dar contractul vostru backend-către-frontend este în responsabilitatea voastră. Modelați ieșirea backend-ului pentru a corespunde așteptărilor frontend-ului existent.

## Secvența evenimentelor de streaming

Când `stream: true`, API emite evenimente în această ordine:
1. `response.created` – obiectul răspuns inițializat
2. `response.in_progress` – generarea începe
3. `response.output_item.added` – elementul de ieșire creat
4. `response.content_part.added` – porțiunea de conținut începută
5. `response.output_text.delta` – fragmente de text (multiple, fiecare având `delta: string`)
6. `response.output_text.done` – generarea textului terminată
7. `response.content_part.done` – porțiunea de conținut terminată
8. `response.output_item.done` – elementul de ieșire terminat
9. `response.completed` – răspuns complet terminat

Pentru streaming text de bază, gestionați doar `response.output_text.delta` (pentru fragmentele de text) și `response.completed` (pentru terminare).

## Gestionarea erorilor de streaming în aplicații web

Când transmiteți în streaming într-o aplicație web, închideți iterația asincronă într-un bloc `try/except` și transmiteți erorile ca JSON astfel încât frontend-ul să le poată afișa elegant (ex. limitări de rată, erori tranzitorii):

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

> **De ce contează asta**: Azure OpenAI returnează `429 Too Many Requests` când limitează rata. Fără `try/except`, răspunsul de streaming moare silențios. Cu el, frontend-ul primește `{"error": "Too Many Requests"}` și poate afișa un prompt de reîncercare.

## Tipuri de evenimente streaming (SDK Python)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Format conversație
```python
# API-ul Responses acceptă formatul conversației prin intermediul unui array de intrare
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

## Gestionarea erorilor filtrului de conținut

Structura corpului erorii s-a schimbat de la Chat Completions la Responses API.

Înainte (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

După (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Diferențe cheie:
- Wrapper-ul `innererror` a **dispărut** — detaliile filtrului de conținut sunt acum la nivel înalt în `error.body`.
- `content_filter_result` (singular) → `content_filters` (plural, listă) conținând `content_filter_results` (plural) în fiecare intrare.
- Fiecare intrare din `content_filters` include `blocked`, `source_type` și `content_filter_results` cu detalii pe categorii (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Structura completă a corpului erorii filtrului de conținut în Responses API:
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

## Migrare HTTP brută (requests/httpx)

Dacă aplicația apelează direct REST-ul Azure OpenAI în loc să folosească SDK-ul:

Înainte (Chat Completions):
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

După (Responses API):
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

> **Notă**: `output_text` este o proprietate de confort a obiectului `Response` din SDK Python. Răspunsul JSON REST brut nu are un câmp la nivel înalt `output_text` — textul este în `output[0].content[0].text`.

## Conversație multi-turn
```python
# Construiește o conversație cu API-ul de Răspunsuri
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Adaugă răspunsul asistentului la conversație
messages.append({"role": "assistant", "content": response.output_text})

# Continuă conversația
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Conversație multi-turn tip conținut (input_text/output_text explicit):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Multi-turn prin `previous_response_id` (alternativ)

În loc să gestionați singur matricea conversației, puteți conecta răspunsurile
server-side folosind `previous_response_id`. API-ul memorează fiecare răspuns și
adaugă automat turele anterioare.

```python
# Prima tură
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Tururile ulterioare — doar transmite mesajul nou al utilizatorului + ID-ul răspunsului anterior
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Când să folosiți ce:**

| Abordare | Avantaje | Dezavantaje |
|---|---|---|
| matricea `input` (manuală) | Control complet asupra istoricului; puteți tăia/rezuma; nu este nevoie de stocare server-side (`store=False`) | Mai mult cod; gestionați voi matricea |
| `previous_response_id` | Cod mai simplu; lanțuire automată | Necesită `store=True` (implicit); conversația stocată server-side; nu puteți modifica istoria între ture |

> **Notă migrare:** Majoritatea aplicațiilor Chat Completions gestionează deja propria matrice de mesaje, deci conversia la matricea `input` este o migrare mai directă 1:1. Folosiți `previous_response_id` pentru cod nou sau când nu trebuie să manipulați istoricul conversațiilor.

## Modele de raționament seria O (o1, o3-mini, o3, o4-mini)

Modelele seria O au constrângeri unice de parametri când migrați la Responses API.

### Maparea parametrilor pentru seria O

| Chat Completions (seria O) | Responses API | Note |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Setați mare (4096+) — tokenii de raționament contează în limita de tokeni |
| `reasoning_effort` | `reasoning.effort` | Păstrați așa dacă este prezent (low/medium/high) |
| `temperature` | Înlăturați sau setați la `1` | Seria O acceptă doar `1` |
| `top_p` | Înlăturați | Nu este suportat pe seria O |
| `seed` | Înlăturați | Nu este suportat în Responses API |

### Seria O înainte/după

Înainte (Chat Completions cu seria O):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

După (Responses API):
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

> **Notă**: Modelele seria O pot acumula ieșirea în timpul raționamentului înainte să emită delta textului. Streaming-ul funcționează în continuare, dar primul eveniment `response.output_text.delta` poate sosi după un delay mai mare față de modelele GPT.

## Accesarea tokenilor de raționament
```python
# Modelele de raționament folosesc raționamentul intern — poți vedea câte token-uri de raționament au fost utilizate
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

> **Important**: Folosiți `max_output_tokens=1000` (nu 50–200) pentru a lua în calcul procesul intern de raționament al modelelor. Modelul folosește tokeni de raționament intern înainte de generarea ieșirii finale.

## Ieșire structurată — JSON Schema
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

## Utilizarea uneltelor

- Definiți funcții în `tools` cu **formatul plat Responses API** — `name`, `description` și `parameters` la nivel de top (nu încastrat sub `function`).
- Când modelul cere să apeleze o unealtă, executați-o în aplicație și includeți rezultatul uneltei în următoarea cerere ca un element `function_call_output` în `input`.
- Păstrați schemele minimale; validați intrările înainte de execuție.
- Când folosiți `strict: true`, toate proprietățile trebuie listate în `required` iar `additionalProperties: false` este obligatoriu.

> **⚠️ `pydantic_function_tool()` este incompatibil**: Helper-ul `openai.pydantic_function_tool()` încă generează vechiul format încastrat Chat Completions (`{"type": "function", "function": {"name": ...}}`). Nu-l folosiți împreună cu `responses.create()`. Definiți manual schemele uneltelor sau scrieți un wrapper pentru a plana ieșirea.

### Formatul definiției uneltei

Responses API folosește un format **plat** pentru unelte — `name`, `description`, `parameters` sunt chei la nivel de top (nu încapsulate în `function`).

**Înainte (Chat Completions — încapsulat):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**După (Responses API — plat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Exemplu complet:
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

Cu `strict: true` (aplicarea schemei):
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
            "required": ["city_name"],       # Toate proprietățile TREBUIE să fie listate
            "additionalProperties": False,   # Necesare pentru modul strict
        },
    }
]
```

### Circuit apel unealtă (execută și returnează rezultate)

Când modelul solicită apelarea unei unelte, folosiți elementele `response.output` + `function_call_output` — **nu** pattern-ul Chat Completions `role: assistant` + `role: tool`.

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
    # Adaugă elementele function_call ale modelului la conversație
    messages.extend(response.output)

    # Execută fiecare unealtă și adaugă rezultatele
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Obține răspunsul final cu rezultatele uneltelor
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Exemple few-shot apel unealtă

Când furnizați exemple few-shot de apeluri de unelte în `input`, folosiți elemente `function_call` și `function_call_output`. ID-urile trebuie să înceapă cu `fc_`.

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
# Exemplu de căutare web încorporată
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Intrare imagine

Elementele de conținut imagine își schimbă tipul de la `image_url` la `input_image`, iar URL-ul se transformă din obiect încastrat într-un șir plat.

### Intrare imagine — înainte (Chat Completions)
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

### Intrare imagine — după (Responses API, URL)
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

### Intrare imagine — după (Responses API, base64)
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

> **Schimbări cheie**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (obiect încastrat) → `"image_url": "..."` (șir plat — fie URL HTTPS, fie URI de date `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## Migrare Microsoft Agent Framework (MAF)

**Verificați mai întâi versiunea MAF** — migrarea depinde dacă sunteți pe MAF 1.0.0+ sau pe beta/rc pre-1.0.0.

Pentru verificare: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

În MAF 1.0.0+, `OpenAIChatClient` **folosește deja Responses API** — nu este nevoie de migrare.

Dacă baza de cod folosește vechiul `OpenAIChatCompletionClient` (care folosește `chat.completions.create`), înlocuiți-l cu `OpenAIChatClient`:

Înainte:
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

După:
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

### MAF pre-1.0.0 (versiuni beta/rc)

În MAF pre-1.0.0, `OpenAIChatClient` folosea Chat Completions. Actualizați la `agent-framework-openai>=1.0.0` unde `OpenAIChatClient` folosește Responses API implicit.

> **Notă**: API-urile `Agent`, `MCPStreamableHTTPTool` și alte API-uri MAF rămân neschimbate — se schimbă doar importul și instanțierea clasei client.

## Migrare LangChain (`langchain-openai`)

Adăugați `use_responses_api=True` la `ChatOpenAI()`. De asemenea, actualizați accesul la conținutul mesajului de la `.content` la `.text`.

Înainte:
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

# ... invocare agent ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

După:
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

# ... invocare agent ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Schimbări cheie**: (1) `use_responses_api=True` în constructor, (2) `.content` → `.text` pentru mesajele răspuns.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->