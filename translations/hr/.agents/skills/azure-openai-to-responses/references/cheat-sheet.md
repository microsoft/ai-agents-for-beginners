# Cheat Sheet za Responses API (Python + Azure OpenAI)

> Svi isječci u nastavku pretpostavljaju `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` i da je `client` već inicijaliziran (pogledajte postavljanje klijenta).

## Osnovni zahtjev
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Postavljanje klijenta — EntraID (preporučeno)
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

## Postavljanje klijenta — API ključ
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Postavljanje asinkronog klijenta — EntraID
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

## Postavljanje asinkronog klijenta — EntraID s eksplicitnim tenantom (višetenantski)

Kada je Azure OpenAI resurs u **drugom tenant-u** od zadanog, proslijedite `tenant_id` eksplicitno u credential. Ovo je često u scenarijima razvoja/testiranja gdje se preneseni tenant programera razlikuje od tenant resursa.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential za produkciju (Azure Container Apps, App Service, itd.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # korisnički dodijeljeni upravljani identitet
)
# AzureDeveloperCliCredential za lokalni razvoj — eksplicitni tenant_id je ključan
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Lanac: prvo pokušaj upravljanog identiteta, ako ne uspije, koristi azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migracija asinkronog klijenta — prije/nakon

Prije (zastarjelo):
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

Nakon:
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

## Potpuna sinhrona migracija — prije/nakon

Prije (naslijeđe — Azure OpenAI Chat Completions):
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

Nakon (Responses API — Azure OpenAI v1 endpoint):
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

## Streaming (sinkrono)
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
        print()  # novi red na kraju
```

## Streaming (asinkrono)
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

## Streaming web aplikacije — oblik backend-prema-frontendu

Prilikom migracije web aplikacije koja streama SSE/JSONL prema frontendu, **format serijalizacije na backendu** se mijenja. Dizajnirajte novi izlaz na backendu da sačuva postojeće obrasce pristupa frontend-a kako frontend ne bi trebao promjene.

**Prije** — Chat Completions backend je obično serijalizirao rječnik `choices[0]` za svaki chunk:
```python
# Staro: serijalizirani puni rječnik izbora po dijelu
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend čita: `response.delta.content` (duboki put u objekt izbora).

**Nakon** — Responses API backend ispušta minimalni oblik sačuvavajući isti frontend path:
```python
# Novo: emitirati samo ono što frontend treba
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend i dalje čita `response.delta.content` — **nije potrebna promjena frontenda**.

> **Ključni uvid**: Respondse API streaming oblik (`event.type` + `event.delta`) je suštinski drugačiji od Chat Completions (`chunk.choices[0].delta.content`). Ali vaš ugovor backend-prema-frontendu je na vama. Oblikujte izlaz backend-a da odgovara što frontend već očekuje.

## Redoslijed stream događaja

Kada je `stream: true`, API emitira događaje ovim redoslijedom:
1. `response.created` – inicijaliziran odgovor
2. `response.in_progress` – započeto generiranje
3. `response.output_item.added` – kreirana stavka izlaza
4. `response.content_part.added` – započeo dio sadržaja
5. `response.output_text.delta` – tekstualni dijelovi (više, svaki ima `delta: string`)
6. `response.output_text.done` – generiranje teksta završeno
7. `response.content_part.done` – dio sadržaja završen
8. `response.output_item.done` – stavka izlaza završena
9. `response.completed` – kompletan odgovor završen

Za osnovni streaming teksta, obradite samo `response.output_text.delta` (za tekstualne dijelove) i `response.completed` (za završetak).

## Obrada pogrešaka prilikom streaminga u web aplikacijama

Pri streamingu u web aplikaciji, omotajte asinkronu iteraciju u `try/except` i izdajte pogreške kao JSON kako frontend to može lijepo prikazati (npr. ograničenja brzine, privremeni neuspjesi):

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

> **Zašto je ovo važno**: Azure OpenAI vraća `429 Too Many Requests` tijekom ograničenja brzine. Bez `try/except`, streaming odgovor tiho prestaje. S njim, frontend prima `{"error": "Too Many Requests"}` i može prikazati prompt za ponovni pokušaj.

## Tipovi događaja streaminga (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Format razgovora
```python
# Responses API podržava format razgovora putem ulaznog niza
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

## Obrada pogrešaka filtera sadržaja

Struktura tijela pogreške se promijenila iz Chat Completions u Responses API.

Prije (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Nakon (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Ključne razlike:
- `innererror` omot je **nestao** — detalji filtera sadržaja su sada na vrhnjem nivou `error.body`.
- `content_filter_result` (jednina) → `content_filters` (množina niz) koji sadrže `content_filter_results` (množina) unutar svake stavke.
- Svaka stavka u `content_filters` uključuje `blocked`, `source_type` i `content_filter_results` s detaljima po kategorijama (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Puni oblik tijela pogreške filtera sadržaja u Responses API:
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

## Migracija sirovog HTTP zahtjeva (requests/httpx)

Ako aplikacija direktno poziva Azure OpenAI REST umjesto SDK:

Prije (Chat Completions):
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

Nakon (Responses API):
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

> **Napomena**: `output_text` je korisna osobina (`property`) Python SDK `Response` objekta. Sirovi REST JSON odgovor nema polje `output_text` na najvišem nivou — tekst se nalazi na `output[0].content[0].text`.

## Više-krugovni razgovor
```python
# Izgradite razgovor s Responses API-jem
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Dodajte odgovor asistenta u razgovor
messages.append({"role": "assistant", "content": response.output_text})

# Nastavite razgovor
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Više-krugovni s tipiziranim sadržajem (eksplicitno `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Više-krugovni putem `previous_response_id` (alternativa)

Umjesto da sami upravljate nizom razgovora, možete nizati odgovore
server-sidere koristeći `previous_response_id`. API pohranjuje svaki odgovor i
automatski dodaje prethodne krugove.

```python
# Prvi potez
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Sljedeći potezi — samo proslijedite novu korisničku poruku + ID prethodnog odgovora
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Kada koristiti što:**

| Pristup | Prednosti | Nedostaci |
|---|---|---|
| `input` niz (ručno) | Potpuna kontrola povijesti; može se rezati/sažimati; nema server-sid pohrane (`store=False`) | Više koda; vi upravljate nizom |
| `previous_response_id` | Jednostavniji kod; automatsko nizanje | Zahtijeva `store=True` (zadano); razgovor se pohranjuje server-side; ne može mijenjati povijest između krugova |

> **Napomena o migraciji:** Većina Chat Completions aplikacija već upravlja svojim nizom poruka, tako da konverzija na `input` niz je direktna migracija 1:1. Koristite `previous_response_id` za novi kod ili kad ne trebate manipulirati poviješću razgovora.

## O-serija modela za rezoniranje (o1, o3-mini, o3, o4-mini)

O-serija modela ima posebna ograničenja parametara kod migracije na Responses API.

### Mapiranje parametara za o-seriju

| Chat Completions (o-serija) | Responses API | Napomene |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Postavite visoko (4096+) — rezonantski tokeni računaju se u limit |
| `reasoning_effort` | `reasoning.effort` | Ostavite kako je ako postoji (low/medium/high) |
| `temperature` | Uklonite ili postavite na `1` | O-serija prihvaća samo `1` |
| `top_p` | Uklonite | Nije podržano na o-seriji |
| `seed` | Uklonite | Nije podržano u Responses API |

### O-serija prije/nakon

Prije (Chat Completions s o-serijom):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Nakon (Responses API):
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

> **Napomena**: O-serija modeli mogu međuspremati izlaz tijekom rezoniranja prije ispuštanja tekstualnih delta podataka. Streaming i dalje radi ali prvi `response.output_text.delta` događaj može doći nakon dužeg kašnjenja nego s GPT modelima.

## Pristup rezonantnim tokenima
```python
# Modeli rezoniranja koriste interno rezoniranje — možete vidjeti koliko je tokena rezoniranja korišteno
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

> **Važno**: Koristite `max_output_tokens=1000` (ne 50–200) da računati za unutarnji rezonantni proces modela. Model koristi rezonantne tokene interno prije generiranja konačnog izlaza.

## Strukturirani izlaz — JSON Schema
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

## Korištenje alata

- Definirajte funkcije u `tools` s **ravan Responses API format** — `name`, `description` i `parameters` na najvišem nivou (nije ugniježđeni pod `function`).
- Kada model zatraži poziv alata, izvršite ga u vašoj aplikaciji i uključite rezultat alata u sljedeći zahtjev kao stavku `function_call_output` unutar `input`.
- Održavajte sheme minimalnima; validirajte ulaze prije izvršenja.
- Kada koristite `strict: true`, sva svojstva moraju biti navedena u `required` i `additionalProperties: false` je obavezno.

> **⚠️ `pydantic_function_tool()` nije kompatibilan**: Pomoćna funkcija `openai.pydantic_function_tool()` još uvijek generira stari ugniježđeni Chat Completions format (`{"type": "function", "function": {"name": ...}}`). Nemojte ga koristiti s `responses.create()`. Definirajte sheme alata ručno ili napišite omotač za njihovo izravnavanje.

### Format definicije alata

Responses API koristi **ravan** format alata — `name`, `description`, `parameters` su ključevi na najvišem nivou (nisu unutar `function`).

**Prije (Chat Completions — ugniježđeno):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Nakon (Responses API — ravan):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Cjelovit primjer:
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

Sa `strict: true` (primjena sheme):
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
            "required": ["city_name"],       # Sve svojstva MORAJU biti navedena
            "additionalProperties": False,   # Potrebno za strogi način rada
        },
    }
]
```

### Poziv alata (izvršenje i povrat rezultata)

Kada model traži poziv alata, koristite stavke `response.output` + `function_call_output` — **ne** obrazac Chat Completions `role: assistant` + `role: tool`.

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
    # Dodajte funkcijske pozive modela u razgovor
    messages.extend(response.output)

    # Izvršite svaki alat i dodajte rezultate
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Dohvatite konačni odgovor s rezultatima alata
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Primjeri nekoliko poziva alata

Kada dajete nekoliko primjera poziva alata u `input`, koristite stavke `function_call` i `function_call_output`. ID-ovi moraju počinjati s `fc_`.

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
# Primjer ugrađene web pretrage
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Ulaz slike

Stavke sadržaja slike mijenjaju tip iz `image_url` u `input_image`, a URL prelazi iz ugniježđenog objekta u ravni string.

### Ulaz slike — prije (Chat Completions)
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

### Ulaz slike — nakon (Responses API, URL)
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

### Ulaz slike — nakon (Responses API, base64)
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

> **Ključne promjene**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (ugnježđeni objekt) → `"image_url": "..."` (ravan string — HTTPS URL ili `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Migracija Microsoft Agent Framework (MAF)

**Prvo provjerite verziju MAF-a** — migracija ovisi o tome koristite li MAF 1.0.0+ ili pre-1.0.0 beta/rc verziju.

Za provjeru: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

U MAF 1.0.0+ `OpenAIChatClient` **već koristi Responses API** — nema potrebe za migracijom.

Ako kod koristi nasljeđeni `OpenAIChatCompletionClient` (koji koristi `chat.completions.create`), zamijenite ga s `OpenAIChatClient`:

Prije:
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

Nakon:
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

### MAF pre-1.0.0 (beta/rc izdanja)

U pre-1.0.0 MAF, `OpenAIChatClient` je koristio Chat Completions. Nadogradite na `agent-framework-openai>=1.0.0` gdje `OpenAIChatClient` koristi Responses API prema zadanim postavkama.

> **Napomena**: `Agent`, `MCPStreamableHTTPTool` i ostali MAF API-ji ostaju nepromijenjeni — mijenja se samo uvoz i instanciranje klase klijenta.

## Migracija LangChain (`langchain-openai`)

Dodajte `use_responses_api=True` u `ChatOpenAI()`. Također ažurirajte pristup sadržaju poruke sa `.content` na `.text`.

Prije:
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

# ... poziv agenta ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Nakon:
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

# ... poziv agenta ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Ključne promjene**: (1) `use_responses_api=True` u konstruktoru, (2) `.content` → `.text` na odgovorima poruka.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->