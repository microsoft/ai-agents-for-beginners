# Vpogledi API za odzive (Python + Azure OpenAI)

> Vsi spodnji odlomki predvidevajo `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` in da je `client` že inicializiran (glej nastavitev klienta).

## Osnovni zahtevek
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Nastavitev klienta — EntraID (priporočeno)
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

## Nastavitev klienta — API ključ
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Asinhrona nastavitev klienta — EntraID
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

## Asinhrona nastavitev klienta — EntraID z eksplicitnim najemnikom (več-najemniški)

Ko je Azure OpenAI vir v **drugem najemniku** kot privzetem, posredujte `tenant_id` eksplicitno v poverilnico. To je pogosto v scenarijih razvoja/testiranja, kjer je najemnik razvijalca drugačen od najemnika vira.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential za produkcijo (Azure Container Apps, App Service itd.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # upravljana identiteta, dodeljena uporabniku
)
# AzureDeveloperCliCredential za lokalni razvoj — izrecni tenant_id je ključnega pomena
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Veriga: najprej poskusi z upravljano identiteto, nato pa uporabi azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migracija asinhronega klienta — prej/pozneje

Pred tem (zastarelo):
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

Po tem:
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

## Popolna sinhrona migracija — prej/pozneje

Pred tem (legacy — Azure OpenAI Chat Completions):
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

Po tem (Responses API — Azure OpenAI v1 endpoint):
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

## Pretakanje (sinhrono)
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
        print()  # nova vrstica na koncu
```

## Pretakanje (asinhrono)
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

## Pretakanje spletne aplikacije — oblika backend-do-frontend

Pri migraciji spletne aplikacije, ki pretaka SSE/JSONL na frontend, se **format serijalizacije backend-a** spremeni. Oblikujte nov izhod backend-a tako, da ohranja obstoječe vzorce dostopa frontend-a, da frontend ne potrebuje sprememb.

**Prej** — Backend Chat Completions je običajno serijaliziral `choices[0]` slovar posameznega kosa:
```python
# Staro: serializiran popoln slovar izbire na kos
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend bere: `response.delta.content` (globoka pot v objekt izbire).

**Po tem** — Backend Responses API pošlje minimalno obliko, ki ohranja isto pot dostopa frontalnega dela:
```python
# Novo: oddajaj samo tisto, kar frontend potrebuje
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend še vedno bere `response.delta.content` — **spremembe frontend-a niso potrebne**.

> **Ključni vpogled**: Oblika pretakanja Responses API (`event.type` + `event.delta`) je temeljno drugačna od Chat Completions (`chunk.choices[0].delta.content`). Vendar pa je vaš dogovor backend-do-frontend tisti, ki ga definirate sami. Oblikujte izhod backend-a tako, da ustreza pričakovanjem frontend-a.

## Zaporedje dogodkov pretakanja

Ko je `stream: true`, API odda dogodke v tem vrstnem redu:
1. `response.created` – inicializiran odzivni objekt
2. `response.in_progress` – generiranje se je začelo
3. `response.output_item.added` – ustvarjen izhodni element
4. `response.content_part.added` – začel se je del vsebine
5. `response.output_text.delta` – besedilni kosi (več, vsak ima `delta: string`)
6. `response.output_text.done` – generiranje besedila končano
7. `response.content_part.done` – del vsebine končan
8. `response.output_item.done` – izhodni element končan
9. `response.completed` – celoten odziv dokončan

Za osnovno pretakanje besedila obravnavajte samo `response.output_text.delta` (za besedilne kose) in `response.completed` (za zaključek).

## Ravnanje z napakami pri pretakanju v spletnih aplikacijah

Pri pretakanju v spletni aplikaciji obkrožite asinhrono iteracijo z `try/except` in oddajajte napake v JSON formatu, da jih frontend lahko prikazuje prijazno (npr. omejitve hitrosti, začasne napake):

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

> **Zakaj je to pomembno**: Azure OpenAI vrača `429 Too Many Requests` med omejevanjem hitrosti. Brez `try/except` pretakanje tiho ugasne. Z njim frontend prejme `{"error": "Too Many Requests"}` in lahko prikaže poziv za ponovni poskus.

## Vrste dogodkov pretakanja (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Oblika pogovora
```python
# API za odzive podpira format pogovora preko vhodnega polja
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

## Ravnanje z napako filtrov vsebin

Struktura telesa napake se je spremenila od Chat Completions do Responses API.

Pred tem (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Po tem (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Ključne razlike:
- Ovitek `innererror` je **izgubljen** — podrobnosti filtra vsebine so sedaj na vrhnji ravni `error.body`.
- `content_filter_result` (ednina) → `content_filters` (množina), ki vsebuje `content_filter_results` (množina) v vsakem vnosu.
- Vsak vnos v `content_filters` vsebuje `blocked`, `source_type` ter `content_filter_results` s podrobnostmi po kategorijah (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Celotna oblika telesa napake filtrov vsebin Responses API:
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

## Migracija surovega HTTP (requests/httpx)

Če aplikacija kliče Azure OpenAI REST neposredno namesto uporabe SDK:

Pred tem (Chat Completions):
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

Po tem (Responses API):
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

> **Opomba**: `output_text` je priročna lastnost Python SDK `Response` objekta. Surovi REST JSON odgovor nima vrhnjega polja `output_text` — besedilo je v `output[0].content[0].text`.

## Večkratni pogovor (multi-turn conversation)
```python
# Zgradi pogovor z Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Dodaj odgovor asistenta v pogovor
messages.append({"role": "assistant", "content": response.output_text})

# Nadaljuj pogovor
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Večkratni pogovor z različnimi vsebinami (eksplicitno `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Večkratno pogovarjanje preko `previous_response_id` (alternativa)

Namesto, da ročno upravljate niz pogovorov, lahko verižite odzive
na strežniški strani z `previous_response_id`. API shrani vsak odgovor in
samodejno preda prejšnje vrstice.

```python
# Prvi potez
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Naslednji potezi — samo pošljite novo uporabniško sporočilo + ID prejšnjega odgovora
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Kdaj uporabiti kateri pristop:**

| Pristop | Prednosti | Slabosti |
|---|---|---|
| `input` niz (ročno) | Popoln nadzor nad zgodovino; možno rezanje/povzemanje; brez potrebe po shranjevanju strežniško (`store=False`) | Več kode; sami upravljate niz |
| `previous_response_id` | Enostavnejša koda; samodejno verižanje | Zahteva `store=True` (privzeto); pogovor je shranjen na strežniški strani; ne morete spreminjati zgodovine med zavoji |

> **Opomba o migraciji:** Večina Chat Completions aplikacij že upravlja svojo lastno polje sporočil, zato je pretvorba v `input` niz bolj neposredna migracija 1:1. Uporabite `previous_response_id` za novo kodo ali ko ni potrebe po manipulaciji s zgodovino pogovora.

## Modeli serije O (o1, o3-mini, o3, o4-mini)

Modeli serije O imajo posebne omejitve parametrov pri migraciji na Responses API.

### Preslikava parametrov za serijo O

| Chat Completions (serija O) | Responses API | Opombe |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Nastavite visoko (4096+) — števec razmišljalskih tokenov se upošteva pri omejitvi |
| `reasoning_effort` | `reasoning.effort` | Ohranite kot je, če je prisoten (nizka/srednja/visoka) |
| `temperature` | Odstranite ali nastavite na `1` | Serija O sprejema le `1` |
| `top_p` | Odstranite | Ni podprto za serijo O |
| `seed` | Odstranite | Ni podprto v Responses API |

### Serija O prej/po

Pred tem (Chat Completions z serijo O):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Po tem (Responses API):
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

> **Opomba**: Modeli serije O lahko med razmišljanjem zbirajo izhodne podatke, preden pošljejo tekstovne delte. Pretakanje še vedno deluje, a prvi dogodek `response.output_text.delta` lahko pride po daljši zakasnitvi kot pri GPT modelih.

## Dostop do razmišljalskih tokenov
```python
# Modeli sklepanja uporabljajo notranje sklepanja — lahko vidite, koliko sklepanjskih žetonov je bilo uporabljenih
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

> **Pomembno**: Uporabite `max_output_tokens=1000` (ne 50–200), da upoštevate notranji proces razmišljanja modelov. Model interno uporablja razmišljalske tokene pred generiranjem končnega izhoda.

## Strukturiran izhod — JSON Schema
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

## Uporaba orodij

- Določite funkcije v `tools` z **ploskim formatom Responses API** — `name`, `description` in `parameters` na vrhnji ravni (ne gnezdeni pod `function`).
- Ko model zahteva klic orodja, ga izvedite v vaši aplikaciji in vključite rezultat orodja v naslednji zahtevek kot `function_call_output` element v `input`.
- Ohranjajte minimalne sheme; preverjajte vnose pred izvedbo.
- Pri uporabi `strict: true` morajo biti vse lastnosti navedene v `required` in `additionalProperties: false` je obvezno.

> **⚠️ `pydantic_function_tool()` ni združljiv**: Pomočnik `openai.pydantic_function_tool()` še vedno generira staro gnezdeno obliko Chat Completions (`{"type": "function", "function": {"name": ...}}`). Ne uporabljajte ga z `responses.create()`. Določite sheme orodij ročno ali napišite ovijalnik za sploščitev izhoda.

### Format definicije orodja

Responses API uporablja **ploski** format orodja — `name`, `description`, `parameters` so vrhnje tipke (ne gnezdene pod `function`).

**Prej (Chat Completions — gnezdeno):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Po tem (Responses API — plosko):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Celoten primer:
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

Z `strict: true` (izvrševanje sheme):
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
            "required": ["city_name"],       # Vse lastnosti MORAJO biti naštete
            "additionalProperties": False,   # Zahtevano za strogi način
        },
    }
]
```

### Krožni klic orodja (izvedba in vračanje rezultatov)

Ko model zahteva klic orodja, uporabite `response.output` elemente + `function_call_output` — **ne** vzorec Chat Completions `role: assistant` + `role: tool`.

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
    # Dodajte elemente function_call modela v pogovor
    messages.extend(response.output)

    # Zaženite vsak pripomoček in dodajte rezultate
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Pridobite končni odgovor z rezultati pripomočkov
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Primeri klicev orodij z malo primeri

Ko podajate nekaj primerov klicev orodij v `input`, uporabite `function_call` in `function_call_output` elemente. ID-ji morajo začeti z `fc_`.

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
# Primer vgrajenega spletnega iskanja
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Vnos slike

Elementi vsebine slike spremenijo tip iz `image_url` v `input_image`, URL pa iz gnezdenega objekta v plosko niz.

### Vnos slike — prej (Chat Completions)
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

### Vnos slike — po tem (Responses API, URL)
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

### Vnos slike — po tem (Responses API, base64)
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

> **Ključne spremembe**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (gnezden objekt) → `"image_url": "..."` (ploski niz — bodisi HTTPS URL ali `data:image/...;base64,...` podatkovni URI), (3) `"type": "text"` → `"type": "input_text"`.

## Migracija Microsoft Agent Framework (MAF)

**Najprej preverite svojo različico MAF** — migracija je odvisna od tega, ali ste na MAF 1.0.0+ ali beta/rc pred 1.0.0.

Za preverjanje: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

V MAF 1.0.0+ `OpenAIChatClient` **že uporablja Responses API** — migracija ni potrebna.

Če koda uporablja legacy `OpenAIChatCompletionClient` (ki uporablja `chat.completions.create`), ga zamenjajte z `OpenAIChatClient`:

Pred tem:
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

Po tem:
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

### MAF pred 1.0.0 (beta/rc izdaje)

Pred 1.0.0 MAF je `OpenAIChatClient` uporabljal Chat Completions. Nadgradite na `agent-framework-openai>=1.0.0`, kjer `OpenAIChatClient` privzeto uporablja Responses API.

> **Opomba**: API-ji `Agent`, `MCPStreamableHTTPTool` in ostali MAF ostajajo nespremenjeni — spremeni se samo uvoz in instanciacija razreda klienta.

## Migracija LangChain (`langchain-openai`)

Dodajte `use_responses_api=True` v `ChatOpenAI()`. Prav tako posodobite dostop do vsebine sporočila iz `.content` v `.text`.

Pred tem:
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

# ... klic agenta ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Po tem:
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

# ... klic agenta ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Ključne spremembe**: (1) `use_responses_api=True` v konstruktorju, (2) `.content` → `.text` na odzivnih sporočilih.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->