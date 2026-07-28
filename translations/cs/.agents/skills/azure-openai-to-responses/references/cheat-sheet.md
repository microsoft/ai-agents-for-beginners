# Rychlý přehled Responses API (Python + Azure OpenAI)

> Všechny níže uvedené ukázky předpokládají `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` a že `client` je již inicializován (viz nastavení klienta).

## Základní požadavek
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Nastavení klienta — EntraID (doporučeno)
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

## Nastavení klienta — API klíč
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Asynchronní nastavení klienta — EntraID
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

## Asynchronní nastavení klienta — EntraID s explicitním tenantem (multi-tenant)

Když je Azure OpenAI zdroj v **jiném tenantu** než výchozím, předávejte `tenant_id` explicitně do přihlašovacích údajů. To je běžné ve scénářích vývoje/testování, kde se domovský tenant vývojáře liší od tenantu zdroje.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential pro produkci (Azure Container Apps, App Service atd.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # spravovaná identita přiřazená uživatelem
)
# AzureDeveloperCliCredential pro lokální vývoj — explicitní tenant_id je klíčový
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Řetězec: nejprve zkusit managed identity, jinak fallback na azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migrace asynchronního klienta — před/po

Před (zastaralé):
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

Po:
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

## Plná synchronní migrace — před/po

Před (legacy — Azure OpenAI Chat Completions):
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

Po (Responses API — Azure OpenAI v1 endpoint):
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

## Streamování (synchronní)
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
        print()  # nový řádek na konci
```

## Streamování (asynchronní)
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

## Streamování webové aplikace — tvar backendu k frontendu

Při migraci webové aplikace, která streamuje SSE/JSONL na frontend, se **formát serializace backendu** změní. Navrhněte nový výstup backendu tak, aby zachoval stávající přístupové vzory frontendu, takže frontend nebude potřebovat žádné změny.

**Před** — Backend Chat Completions typicky serializoval slovník `choices[0]` každého kusu (`chunk`):
```python
# Staré: serializovaný celý slovník voleb na každý úsek
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend čte: `response.delta.content` (hluboká cesta do objektu choice).

**Po** — Backend Responses API vysílá minimální strukturu zachovávající stejnou přístupovou cestu frontendu:
```python
# Nové: vysílat pouze to, co frontend potřebuje
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend stále čte `response.delta.content` — **žádné změny frontendu nejsou potřeba**.

> **Klíčový poznatek**: Streamingový tvar Responses API (`event.type` + `event.delta`) je zásadně odlišný od Chat Completions (`chunk.choices[0].delta.content`). Ale smlouva mezi backendem a frontendem je na vás. Upravte výstup backendu tak, aby odpovídal tomu, co frontend očekává.

## Sekvence streamovacích událostí

Pokud je `stream: true`, API vyšle události v tomto pořadí:
1. `response.created` – inicializace odpovědi
2. `response.in_progress` – začátek generování
3. `response.output_item.added` – vytvoření výstupního prvku
4. `response.content_part.added` – začátek části obsahu
5. `response.output_text.delta` – textové kusy (několik, každý má `delta: string`)
6. `response.output_text.done` – dokončení generování textu
7. `response.content_part.done` – dokončení části obsahu
8. `response.output_item.done` – dokončení výstupního prvku
9. `response.completed` – kompletní odpověď hotová

Pro základní streamování textu zpracovávejte pouze `response.output_text.delta` (pro kusy textu) a `response.completed` (pro ukončení).

## Zpracování chyb při streamování ve webových aplikacích

Při streamování ve webové aplikaci zabalte asynchronní iteraci do `try/except` a chybové události vydejte jako JSON, aby je frontend mohl elegantně zobrazit (např. omezení počtu požadavků, dočasné chyby):

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

> **Proč je to důležité**: Azure OpenAI vrací `429 Too Many Requests` při překročení limitu rychlosti. Bez `try/except` streamovací odpověď tiše skončí. S ním frontend obdrží `{"error": "Too Many Requests"}` a může zobrazit výzvu k opětovnému pokusu.

## Typy streamovacích událostí (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Formát konverzace
```python
# Rozhraní Responses API podporuje formát konverzace prostřednictvím vstupního pole
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

## Zpracování chyb filtru obsahu

Struktura těla chyby se změnila z Chat Completions na Responses API.

Před (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Po (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Klíčové rozdíly:
- Obal `innererror` **zmizel** — detaily filtru obsahu jsou nyní na nejvyšší úrovni `error.body`.
- `content_filter_result` (jednotné číslo) → `content_filters` (množné číslo, pole) obsahující uvnitř každé položky `content_filter_results` (množné číslo).
- Každá položka v `content_filters` zahrnuje `blocked`, `source_type` a `content_filter_results` s detailem podle kategorií (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Kompletní tvar těla chyby filtru obsahu Responses API:
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

## Migrace na nízké úrovni HTTP (requests/httpx)

Pokud aplikace volá Azure OpenAI REST přímo namísto SDK:

Před (Chat Completions):
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

Po (Responses API):
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

> **Poznámka**: `output_text` je pohodlná vlastnost v Python SDK objektu `Response`. Surová JSON REST odpověď nemá top-level pole `output_text` — text je v `output[0].content[0].text`.

## Vícekolové konverzace
```python
# Vytvořte konverzaci pomocí API odpovědí
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Přidejte odpověď asistenta do konverzace
messages.append({"role": "assistant", "content": response.output_text})

# Pokračujte v konverzaci
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Vícekolové s typovaným obsahem (explicitní `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Vícekolové pomocí `previous_response_id` (alternativa)

Místo správy pole konverzace sami můžete řetězit odpovědi
serverově pomocí `previous_response_id`. API ukládá každou odpověď a
automaticky předřadí předchozí kroky.

```python
# První tah
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Následující tahy — jednoduše předat novou uživatelskou zprávu + ID předchozí odpovědi
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Kdy co používat:**

| Přístup | Výhody | Nevýhody |
|---|---|---|
| Pole `input` (ručně) | Úplná kontrola nad historií; lze ořezávat/zhotovovat souhrny; není potřeba ukládání na serveru (`store=False`) | Více kódu; spravujete pole sami |
| `previous_response_id` | Jednodušší kód; automatické řetězení | Vyžaduje `store=True` (výchozí); konverzace je uložena serverově; není možné měnit historii mezi kroky |

> **Poznámka k migraci:** Většina aplikací Chat Completions již vlastní pole zpráv spravuje, takže přechod na pole `input` je přímější migrace 1:1. Použijte `previous_response_id` pro nový kód nebo když nepotřebujete manipulovat s historií konverzace.

## Modely řady O (o1, o3-mini, o3, o4-mini)

Modely řady O mají unikátní omezení parametrů při migraci na Responses API.

### Mapování parametrů pro řadu o

| Chat Completions (řada o) | Responses API | Poznámky |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | Nastavte vysoko (4096+) — počítání tokenů pro odvozování se započítává do limitu |
| `reasoning_effort` | `reasoning.effort` | Zachovejte stávající hodnotu, pokud je přítomna (low/medium/high) |
| `temperature` | Odstraňte nebo nastavte na `1` | Séria O přijímá pouze `1` |
| `top_p` | Odstraňte | Není podporováno v o-sérii |
| `seed` | Odstraňte | Není podporováno v Responses API |

### O-série před/po

Před (Chat Completions s o-sérií):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Po (Responses API):
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

> **Poznámka**: Modely o-série mohou během odvozování bufferovat výstup před vydáním textových delt. Streamování stále funguje, ale první událost `response.output_text.delta` může přijít po delší prodlevě než u modelů GPT.

## Přístup k tokenům odvozování
```python
# Modely uvažování používají vnitřní uvažování — můžete vidět, kolik uvažovacích tokenů bylo použito
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

> **Důležité**: Použijte `max_output_tokens=1000` (ne 50–200), aby bylo zohledněno interní odvozovací zpracování modelů. Model interně používá odvozovací tokeny před generováním konečného výstupu.

## Strukturovaný výstup — JSON Schema
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

## Použití nástrojů

- Definujte funkce v `tools` ve **flat formátu Responses API** — `name`, `description` a `parameters` na nejvyšší úrovni (ne zabalené pod `function`).
- Když model požádá o volání nástroje, proveďte ho ve vaší aplikaci a zahrňte výsledek nástroje do dalšího požadavku jako položku `function_call_output` uvnitř `input`.
- Udržujte schémata minimální; validujte vstupy před provedením.
- Při použití `strict: true` musí být všechny vlastnosti uvedeny v `required` a `additionalProperties: false` je povinné.

> **⚠️ `pydantic_function_tool()` je nekompatibilní**: Pomocník `openai.pydantic_function_tool()` stále generuje starý Chat Completions zanořený formát (`{"type": "function", "function": {"name": ...}}`). Nepoužívejte ho s `responses.create()`. Definujte schémata nástrojů ručně nebo napište wrapper pro zploštění výstupu.

### Formát definice nástroje

Responses API používá **flat** formát nástroje — `name`, `description`, `parameters` jsou klíče nejvyšší úrovně (ne zabalené pod `function`).

**Před (Chat Completions — zanořené):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Po (Responses API — flat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Kompletní příklad:
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

S `strict: true` (vynucení schématu):
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
            "required": ["city_name"],       # Všechny vlastnosti MUSÍ být uvedeny
            "additionalProperties": False,   # Požadováno pro přísný režim
        },
    }
]
```

### Cesta volání nástroje (provedení a návrat výsledků)

Když model požaduje volání nástroje, použijte položky `response.output` + `function_call_output` — **ne** vzor Chat Completions `role: assistant` + `role: tool`.

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
    # Přidejte položky function_call modelu do konverzace
    messages.extend(response.output)

    # Spusťte každý nástroj a přidejte výsledky
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Získejte konečnou odpověď s výsledky nástrojů
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Příklady volání nástrojů s několika šablonami (few-shot)

Když poskytujete příklady volání nástrojů v `input`, použijte položky `function_call` a `function_call_output`. ID musí začínat na `fc_`.

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
# Vestavěný příklad webového vyhledávání
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Vstup obrázku

Položky obsahu obrázku mění typ z `image_url` na `input_image` a URL se mění z vnořeného objektu na prostý řetězec.

### Vstup obrázku — před (Chat Completions)
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

### Vstup obrázku — po (Responses API, URL)
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

### Vstup obrázku — po (Responses API, base64)
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

> **Klíčové změny**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (vnořený objekt) → `"image_url": "..."` (prostý řetězec — buď HTTPS URL nebo `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Migrace Microsoft Agent Framework (MAF)

**Nejprve zkontrolujte vaši verzi MAF** — migrace závisí na tom, zda jste na MAF 1.0.0+ nebo na předchozí betaverzi/rc před 1.0.0.

K ověření: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

V MAF 1.0.0+ `OpenAIChatClient` **již používá Responses API** — migrace není potřeba.

Pokud kód používá starý `OpenAIChatCompletionClient` (který používá `chat.completions.create`), nahraďte ho `OpenAIChatClient`:

Před:
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

Po:
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

### MAF před 1.0.0 (beta/rc verze)

V předchozím MAF před 1.0.0 `OpenAIChatClient` používal Chat Completions. Upgradujte na `agent-framework-openai>=1.0.0`, kde `OpenAIChatClient` již implicitně používá Responses API.

> **Poznámka**: API `Agent`, `MCPStreamableHTTPTool` a další v MAF zůstávají beze změny — změní se jen import a instance klientské třídy.

## Migrace LangChain (`langchain-openai`)

Přidejte `use_responses_api=True` do `ChatOpenAI()`. Také aktualizujte přístup k obsahu zpráv z `.content` na `.text`.

Před:
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

# ... vyvolání agenta ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Po:
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

# ... vyvolání agenta ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Klíčové změny**: (1) `use_responses_api=True` v konstruktoru, (2) `.content` → `.text` u odpovědních zpráv.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->