# Reference API odpovědí (Python + Azure OpenAI)

> Všechny níže uvedené úryvky předpokládají `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` a že `client` je již inicializován (viz nastavení klienta).

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

## Asynchronní nastavení klienta — EntraID s explicitním tenantem (multi-tenancy)

Když je zdroj Azure OpenAI v **jiném tenantovi** než je výchozí, předávejte `tenant_id` explicitně v přihlašovacích údajích. To je běžné v scénářích vývoje/testování, kde se domovský tenant vývojáře liší od tenant zdroje.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential pro produkci (Azure Container Apps, App Service, atd.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # spravovaná identita přiřazená uživatelem
)
# AzureDeveloperCliCredential pro místní vývoj — explicitní tenant_id je zásadní
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Řetězec: nejprve zkusit spravovanou identitu, poté se vrátit k azd CLI
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

Před (deprecated):
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

## Migrace kompletní synchronní — před/po

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
    model="gpt-4o",
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
        print()  # nový řádek na konci
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

## Streaming webové aplikace — tvar backend→frontend

Při migraci webové aplikace, která streamuje SSE/JSONL do frontendu, se **serializační formát backendu** mění. Navrhněte nový výstup backendu tak, aby zachoval stávající přístupové vzory frontendu, takže frontend nebude potřebovat změny.

**Předtím** — Chat Completions backend obvykle serializoval `choices[0]` slovník každého chunku:
```python
# Stará verze: serializovaný celý slovník voleb na úsek
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend čte: `response.delta.content` (hluboká cesta do objektu choice).

**Poté** — Responses API backend vysílá minimální tvar zachovávající stejnou frontendovou přístupovou cestu:
```python
# Nové: vysílat pouze to, co frontend potřebuje
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend stále čte `response.delta.content` — **žádné změny frontendu nejsou potřeba**.

> **Klíčový postřeh**: Streaming tvar Responses API (`event.type` + `event.delta`) je zásadně odlišný od Chat Completions (`chunk.choices[0].delta.content`). Ale smlouva backend→frontend je na vás. Přizpůsobte backendový výstup tak, aby odpovídal tomu, co frontend již očekává.

## Sekvence streamovacích událostí

Při `stream: true` API vydává události v tomto pořadí:
1. `response.created` – inicializace objektu odpovědi
2. `response.in_progress` – zahájení generování
3. `response.output_item.added` – vytvořen výstupní prvek
4. `response.content_part.added` – zahájení části obsahu
5. `response.output_text.delta` – textové kousky (vícero, každý má `delta: string`)
6. `response.output_text.done` – dokončení generování textu
7. `response.content_part.done` – dokončení části obsahu
8. `response.output_item.done` – dokončení výstupního prvku
9. `response.completed` – dokončení celé odpovědi

Pro základní textový streaming zpracovávejte pouze `response.output_text.delta` (pro textové části) a `response.completed` (pro dokončení).

## Zpracování chyb streamingu ve webových aplikacích

Při streamování ve webové aplikaci zabalte asynchronní iteraci do `try/except` a chybové stavy vydejte jako JSON, aby je frontend mohl hezky zobrazit (např. rate limiting, přechodné chyby):

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

> **Proč je to důležité**: Azure OpenAI vrací `429 Too Many Requests` při omezení rychlosti. Bez `try/except` streamování tichounce skončí. S ním frontend obdrží `{"error": "Too Many Requests"}` a může zobrazit výzvu k opakování.

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

Struktura chybové zprávy se změnila z Chat Completions na Responses API.

Předtím (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Poté (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Klíčové rozdíly:
- Wrapper `innererror` je **pryč** — detaily obsahu filtru jsou nyní na vrchní úrovni `error.body`.
- `content_filter_result` (jednotné číslo) → `content_filters` (množné pole) obsahující `content_filter_results` (množné číslo) uvnitř každé položky.
- Každá položka v `content_filters` obsahuje `blocked`, `source_type` a `content_filter_results` s detaily podle kategorií (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Kompletní tvar těla chyby filtru obsahu v Responses API:
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

## Migrace přes surové HTTP (requests/httpx)

Pokud aplikace volá Azure OpenAI REST přímo místo SDK:

Předtím (Chat Completions):
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

Poté (Responses API):
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

> **Poznámka**: `output_text` je pohodlná vlastnost v objektu `Response` Python SDK. Surová REST JSON odpověď nemá vrchní pole `output_text` — text je v `output[0].content[0].text`.

## Vícekolová konverzace
```python
# Vytvořit konverzaci pomocí Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Přidat odpověď asistenta do konverzace
messages.append({"role": "assistant", "content": response.output_text})

# Pokračovat v konverzaci
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Vícekolová konverzace s typem obsahu (explicitní `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Vícekolová konverzace přes `previous_response_id` (alternativa)

Místo správy pole konverzace vy sami můžete řetězit odpovědi
na serveru pomocí `previous_response_id`. API si uchovává každou odpověď a
automaticky předchází předchozí kola.

```python
# První tah
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Následující tahy — stačí předat novou uživatelskou zprávu + ID předchozí odpovědi
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Kdy použít co:**

| Přístup | Výhody | Nevýhody |
|---|---|---|
| `input` pole (manuální) | Plná kontrola nad historií; lze ořezávat/summarizovat; nepotřebuje serverové uložení (`store=False`) | Více kódu; spravujete pole sami |
| `previous_response_id` | Jednodušší kód; automatické řetězení | Vyžaduje `store=True` (výchozí); konverzace se ukládá na serveru; nelze upravovat historii mezi koly |

> **Poznámka k migraci:** Většina aplikací Chat Completions již spravuje své pole zpráv, takže konverze na `input` pole je přímá 1:1 migrace. Použijte `previous_response_id` pro nový kód nebo pokud nepotřebujete upravovat historii konverzace.

## Modely řady O (o1, o3-mini, o3, o4-mini)

Modely řady O mají specifická omezení parametrů při migraci na Responses API.

### Mapování parametrů pro řadu O

| Chat Completions (řada O) | Responses API | Poznámky |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Nastavit vysokou hodnotu (4096+) — tokeny reasoning se počítají do limitu |
| `reasoning_effort` | `reasoning.effort` | Zachovat, pokud je přítomno (low/medium/high) |
| `temperature` | Odstranit nebo nastavit na `1` | Řada O přijímá pouze hodnotu `1` |
| `top_p` | Odstranit | Není podporováno na řadě O |
| `seed` | Odstranit | Není podporováno v Responses API |

### Řada O před/po

Před (Chat Completions s řadou O):
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

> **Poznámka**: Modely řady O mohou akumulovat výstup během reasoning, než začnou odesílat textové delty. Streaming stále funguje, ale první událost `response.output_text.delta` může přijít s delším zpožděním než u GPT modelů.

## Přístup k reasoning tokenům
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

> **Důležité**: Použijte `max_output_tokens=1000` (ne 50–200) kvůli internímu procesu reasoning modelů. Model uvnitř používá reasoning tokeny před samotnou generací výsledku.

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

- Definujte funkce v `tools` ve **flat formátu Responses API** — `name`, `description` a `parameters` v hlavní úrovni (nikoli zanořené pod `function`).
- Když model požaduje zavolat nástroj, proveďte ho ve své aplikaci a zahrňte výsledek nástroje do dalšího požadavku jako položku `function_call_output` v `input`.
- Udržujte schémata minimalistická; ověřujte vstupy před vykonáním.
- Při použití `strict: true` musí být všechny vlastnosti uvedeny v `required` a `additionalProperties: false` je povinné.

> **⚠️ `pydantic_function_tool()` není kompatibilní**: Pomocník `openai.pydantic_function_tool()` stále generuje starý zanořený formát Chat Completions (`{"type": "function", "function": {"name": ...}}`). Nepoužívejte ho s `responses.create()`. Definujte schémata nástrojů ručně nebo napište wrapper, který výstup zploští.

### Formát definice nástroje

Responses API používá **flat** formát nástroje — `name`, `description`, `parameters` jsou klíče v top-level (nikoli zanořené pod `function`).

**Předtím (Chat Completions — zanořené):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Poté (Responses API — flat):**
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
            "additionalProperties": False,   # Vyžadováno pro přísný režim
        },
    }
]
```

### Volání nástroje tam a zpět (provede se a vrátí výsledky)

Když model žádá o volání nástroje, použijte položky `response.output` + `function_call_output` — **ne** vzor Chat Completions `role: assistant` + `role: tool`.

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

    # Proveďte každý nástroj a přidejte výsledky
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

### Příklady volání nástroje s few-shot

Při poskytování příkladů few-shot volání nástroje v `input` použijte položky `function_call` a `function_call_output`. ID musí začínat na `fc_`.

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
# Příklad vestavěného vyhledávání na webu
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Vstup obrázku

Typy položek obsahu obrázku se změnily z `image_url` na `input_image` a URL se změnilo z vnořeného objektu na plochý řetězec.

### Vstup obrázku — předtím (Chat Completions)
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

### Vstup obrázku — poté (Responses API, URL)
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

### Vstup obrázku — poté (Responses API, base64)
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

> **Klíčové změny**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (vnořený objekt) → `"image_url": "..."` (plochý řetězec — buď HTTPS URL nebo `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Migrace Microsoft Agent Framework (MAF)

**Nejprve si zkontrolujte verzi MAF** — migrace závisí na tom, zda máte MAF 1.0.0+ nebo předběžnou beta/rc verzi pod 1.0.0.

Pro kontrolu: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

V MAF 1.0.0+ `OpenAIChatClient` **již používá Responses API** — migrace není potřeba.

Pokud kód používá legacy `OpenAIChatCompletionClient` (který používá `chat.completions.create`), nahraďte ho `OpenAIChatClient`:

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

V předběžném MAF pod 1.0.0 používal `OpenAIChatClient` Chat Completions. Aktualizujte na `agent-framework-openai>=1.0.0`, kde `OpenAIChatClient` používá Responses API jako výchozí.

> **Poznámka**: API `Agent`, `MCPStreamableHTTPTool` a další MAF zůstávají nezměněna — mění se jen import a vytváření instance klienta.

## Migrace LangChain (`langchain-openai`)

Přidejte `use_responses_api=True` do `ChatOpenAI()`. Aktualizujte také přístup k obsahu zpráv z `.content` na `.text`.

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

> **Klíčové změny**: (1) `use_responses_api=True` v konstruktoru, (2) `.content` → `.text` na odpovědních zprávách.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->