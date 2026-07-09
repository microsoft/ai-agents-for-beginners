# Odkaz na API odpovedí (Python + Azure OpenAI)

> Všetky níže uvedené ukážky predpokladajú `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` a že `client` je už inicializovaný (pozri nastavenie klienta).

## Základný požiadavok
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Nastavenie klienta — EntraID (odporúčané)
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

## Nastavenie klienta — API kľúč
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Asynchrónne nastavenie klienta — EntraID
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

## Asynchrónne nastavenie klienta — EntraID s explicitným tenantom (multi-tenant)

Keď je Azure OpenAI zdroj v **inom tenante** než predvolený, odovzdajte `tenant_id` explicitne do poverenia. Toto je bežné v dev/test scenároch, kde sa domovský tenant vývojára líši od tenanta zdroja.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential pre produkciu (Azure Container Apps, App Service, atď.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # používateľom priradená spravovaná identita
)
# AzureDeveloperCliCredential pre lokálny vývoj — explicitný tenant_id je kritický
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Reťazec: najprv skúsiť spravovanú identitu, potom použiť azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migrácia asynchrónneho klienta — pred/po

Predtým (zastaralé):
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

Po migrácii:
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

## Plná synchronná migrácia — pred/po

Predtým (legacy — Azure OpenAI Chat Completions):
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

Po migrácii (Responses API — Azure OpenAI endpoint v1):
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

## Streamovanie (synchronné)
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
        print()  # nový riadok na konci
```

## Streamovanie (asynchronné)
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

## Streamovanie webovej aplikácie — štruktúra backend k frontend

Pri migrácii webovej aplikácie, ktorá streamuje SSE/JSONL do frontendu, sa **formát sériovej verzie backendu** mení. Navrhnite nový backendový výstup tak, aby zachoval existujúce prístupy frontendu, aby neboli potrebné žiadne zmeny na fronte.

**Predtým** — backend Chat Completions obvykle serializoval slovník `choices[0]` každého kúsku:
```python
# Pôvodné: serializovaný úplný slovník výberu pre každý chunk
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend číta: `response.delta.content` (hlboká cesta do objektu voľby).

**Potom** — backend Responses API vysiela minimálny tvar zachovávajúci rovnakú cestu prístupu pre frontend:
```python
# Nové: vysielať iba to, čo frontend potrebuje
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend stále číta `response.delta.content` — **žiadne zmeny na fronte nie sú potrebné**.

> **Kľúčový postreh**: Streamingový tvar Responses API (`event.type` + `event.delta`) je fundamentálne odlišný od Chat Completions (`chunk.choices[0].delta.content`). Ale vaša zmluva backend k frontend je len na vás. Navrhnite backendový výstup tak, aby zodpovedal tomu, čo frontend už očakáva.

## Sekvencia streamovacích udalostí

Keď je `stream: true`, API vydáva udalosti v tomto poradí:
1. `response.created` – inicializovaný objekt odpovede
2. `response.in_progress` – generovanie začalo
3. `response.output_item.added` – vytvorená položka výstupu
4. `response.content_part.added` – začala časť obsahu
5. `response.output_text.delta` – textové kúsky (viacero, každý obsahuje `delta: string`)
6. `response.output_text.done` – generovanie textu skončené
7. `response.content_part.done` – časť obsahu dokončená
8. `response.output_item.done` – položka výstupu dokončená
9. `response.completed` – celá odpoveď dokončená

Pre základné textové streamovanie zvládajte len `response.output_text.delta` (textové kúsky) a `response.completed` (ukončenie).

## Riešenie chýb pri streamovaní vo webových aplikáciách

Pri streamovaní vo webovej aplikácii obalte asynchrónnu iteráciu do `try/except` a vráťte chyby ako JSON, aby ich frontend vedel pekne zobraziť (napr. limity požiadaviek, prechodné zlyhania):

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

> **Prečo je to dôležité**: Azure OpenAI vracia `429 Too Many Requests` pri prekročení limitov. Bez `try/except` streamovanie ticho zanikne. S ním frontend dostane `{"error": "Too Many Requests"}` a môže vyzvať používateľa na opakovanie pokusu.

## Typy streamovacích udalostí (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Formát konverzácie
```python
# Rozhranie Responses API podporuje formát konverzácie prostredníctvom poľa vstupov
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

## Riešenie chýb filtra obsahu

Štruktúra tela chyby sa zmenila z Chat Completions na Responses API.

Predtým (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Potom (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Kľúčové rozdiely:
- Wrapper `innererror` **zmizol** — detaily filtra obsahu sú teraz na vrchnej úrovni `error.body`.
- `content_filter_result` (jednotné číslo) → `content_filters` (množné číslo poľa) obsahujúce `content_filter_results` (množné číslo) v každej položke.
- Každá položka v `content_filters` obsahuje `blocked`, `source_type` a `content_filter_results` s detailami pre kategórie (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Kompletne tvar tela chyby filtra obsahu Responses API:
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

## Migrácia cez "raw" HTTP (requests/httpx)

Ak aplikácia volá Azure OpenAI REST priamo namiesto použitia SDK:

Predtým (Chat Completions):
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

Potom (Responses API):
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

> **Poznámka**: `output_text` je pohodlná vlastnosť objektu `Response` v Python SDK. Surová REST JSON odpoveď nemá na vrchnej úrovni pole `output_text` — text je v `output[0].content[0].text`.

## Multi-turn konverzácia
```python
# Vytvorte konverzáciu pomocou Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Pridajte odpoveď asistenta do konverzácie
messages.append({"role": "assistant", "content": response.output_text})

# Pokračujte v konverzácii
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Multi-turn s typovaným obsahom (explicitné `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Multi-turn cez `previous_response_id` (alternatíva)

Namiesto spravovania poľa konverzácie sami, môžete reťaziť odpovede
na serverovej strane pomocou `previous_response_id`. API ukladá každú odpoveď a
automaticky pripája predchádzajúce kolá.

```python
# Prvý ťah
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Následné ťahy — stačí odoslať novú správu používateľa + ID predchádzajúcej odpovede
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Kedy použiť ktorý prístup:**

| Prístup | Výhody | Nevýhody |
|---|---|---|
| pole `input` (manuálne) | Plná kontrola histórie; možnosť orezania/zhrnutia; nie je potrebné ukladanie na serveri (`store=False`) | Viac kódu; vy spravujete pole |
| `previous_response_id` | Jednoduchší kód; automatické reťazenie | Vyžaduje `store=True` (štandardné); konverzácia uložená na serveri; nemožno meniť históriu medzi kolami |

> **Poznámka k migrácii:** Väčšina Chat Completions aplikácií už spravuje vlastné pole správ, takže konverzia na pole `input` je priama migrácia 1:1. Použite `previous_response_id` pre nový kód alebo ak nepotrebujete manipulovať s históriou konverzácie.

## O-series modely na uvažovanie (o1, o3-mini, o3, o4-mini)

Modely série O majú pri migrácii na Responses API špecifické obmedzenia parametrov.

### Mapovanie parametrov pre sériu O

| Chat Completions (séria O) | Responses API | Poznámky |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Nastavte na vysokú hodnotu (4096+) — tokeny uvažovania sa počítajú do limitu |
| `reasoning_effort` | `reasoning.effort` | Ponechajte ak je prítomný (low/medium/high) |
| `temperature` | Odstráňte alebo nastavte na `1` | Séria O akceptuje iba `1` |
| `top_p` | Odstráňte | Nie je podporované na sérii O |
| `seed` | Odstráňte | Nie je podporované v Responses API |

### Séria O pred/po

Predtým (Chat Completions so sériou O):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Po migrácii (Responses API):
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

> **Poznámka**: Modely série O môžu počas uvažovania bufferingovať výstup pred emitovaním textových delta udalostí. Streamovanie stále funguje, ale prvá udalosť `response.output_text.delta` môže prísť s väčším oneskorením ako u GPT modelov.

## Prístup k tokenom uvažovania
```python
# Modely uvažovania používajú vnútorné uvažovanie — môžete vidieť, koľko tokenov uvažovania bolo použitých
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

> **Dôležité**: Použite `max_output_tokens=1000` (nie 50–200) kvôli internému procesu uvažovania modelov. Model používa tokeny uvažovania interne pred generovaním konečného výstupu.

## Štruktúrovaný výstup — JSON schéma
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

## Použitie nástrojov

- Definujte funkcie v `tools` s **plochým formátom Responses API** — `name`, `description` a `parameters` na vrchnej úrovni (nie vnorené pod `function`).
- Keď model požiada o volanie nástroja, vykonajte ho vo vašej aplikácii a výsledok nástroja zahrňte v nasledujúcej požiadavke ako položku `function_call_output` v `input`.
- Udržujte schémy minimalistické; validujte vstupy pred vykonaním.
- Pri použití `strict: true` musia byť všetky vlastnosti uvedené v `required` a `additionalProperties: false` je povinné.

> **⚠️ `pydantic_function_tool()` je nekompatibilný**: Pomocník `openai.pydantic_function_tool()` stále generuje starý vnorený formát Chat Completions (`{"type": "function", "function": {"name": ...}}`). Nepoužívajte ho s `responses.create()`. Definujte schémy nástrojov manuálne alebo napíšte wrapper na ploché rozbalenie výstupu.

### Formát definície nástroja

Responses API používa **plochý** formát nástroja — `name`, `description`, `parameters` sú kľúče na vrchnej úrovni (nie vnorené pod `function`).

**Predtým (Chat Completions — vnorené):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Potom (Responses API — ploché):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Kompletný príklad:
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

So `strict: true` (presadzovanie schémy):
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
            "required": ["city_name"],       # Všetky vlastnosti MUSIA byť uvedené
            "additionalProperties": False,   # Povinné pre prísny režim
        },
    }
]
```

### Kolo volania nástroja (vykonanie a návrat výsledkov)

Keď model požiada o volanie nástroja, použite položky `response.output` + `function_call_output` — **nie** vzor `role: assistant` + `role: tool` z Chat Completions.

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
    # Pridajte položky function_call modelu do konverzácie
    messages.extend(response.output)

    # Spustite každý nástroj a pridajte výsledky
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Získajte konečnú odpoveď s výsledkami nástrojov
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Príklady volaní nástroja s pár ukážkami (Few-shot)

Pri poskytovaní pár ukážok volaní nástroja v `input` používajte položky `function_call` a `function_call_output`. ID musia začínať na `fc_`.

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
# Príklad vstavaného webového vyhľadávania
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Vstup obrázka

Položky obsahu obrázka menia typ z `image_url` na `input_image` a URL sa mení z vnoreného objektu na plochý reťazec.

### Vstup obrázka — predtým (Chat Completions)
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

### Vstup obrázka — potom (Responses API, URL)
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

### Vstup obrázka — potom (Responses API, base64)
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

> **Kľúčové zmeny**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (vnorený objekt) → `"image_url": "..."` (plochý reťazec — buď HTTPS URL alebo `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Migrácia Microsoft Agent Framework (MAF)

**Najprv skontrolujte vašu verziu MAF** — migrácia závisí od toho, či ste na MAF 1.0.0+ alebo predverzii beta/rc.

Na kontrolu: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

V MAF 1.0.0+ `OpenAIChatClient` **už používa Responses API** — migrácia nie je potrebná.

Ak kód používa legacy `OpenAIChatCompletionClient` (ktorý používa `chat.completions.create`), nahraďte ho `OpenAIChatClient`:

Pred:
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

### MAF pred 1.0.0 (beta/rc verzie)

V predverzii MAF 1.0.0 používal `OpenAIChatClient` Chat Completions. Aktualizujte na `agent-framework-openai>=1.0.0`, kde `OpenAIChatClient` používa Responses API ako predvolené.

> **Poznámka**: `Agent`, `MCPStreamableHTTPTool` a iné MAF API ostávajú nezmenené — zmení sa iba import a inštancovanie klienta.

## Migrácia LangChain (`langchain-openai`)

Pridajte `use_responses_api=True` do `ChatOpenAI()`. Aktualizujte prístup k obsahu správ z `.content` na `.text`.

Pred:
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

# ... vyvolanie agenta ...
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

# ... vyvolanie agenta ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Kľúčové zmeny**: (1) `use_responses_api=True` v konštruktore, (2) `.content` → `.text` na odpovediach správ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->