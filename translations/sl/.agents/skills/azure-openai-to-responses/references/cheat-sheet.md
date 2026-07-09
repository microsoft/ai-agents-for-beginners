# Vzvodski list za Responses API (Python + Azure OpenAI)

> Vsi spodnji primeri predpostavljajo `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` in da je `client` že inicializiran (glej nastavitev klienta).

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

## Nastavitev asinhronega klienta — EntraID
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

## Nastavitev asinhronega klienta — EntraID z izrecno najemniško enoto (multi-najemnik)

Ko je Azure OpenAI vir v **drugem najemniku** kot privzeti, posredujte `tenant_id` izrecno poverilnici. To je pogosto v razvojnih/testnih scenarijih, kjer se domači najemnik razvijalca razlikuje od najemnika vira.

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
    client_id=os.getenv("AZURE_CLIENT_ID")  # uporabniško dodeljena upravljana identiteta
)
# AzureDeveloperCliCredential za lokalni razvoj — izrecni tenant_id je ključnega pomena
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Veriga: najprej poskusi upravljano identiteto, nato preklopi na azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migracija asinhronega klienta — pred/po

Pred (zastarelo):
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

## Polna sinhrona migracija — pred/po

Pred (zastarelo — Azure OpenAI Chat Completions):
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

Po (Responses API — Azure OpenAI v1 končna točka):
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

## Pretakanje spletnih aplikacij — oblikovanje backend-do-frontend

Pri migraciji spletne aplikacije, ki pretaka SSE/JSONL na frontend, se **format seralizacije backenda** spremeni. Oblikujte nov izhod backenda tako, da ohranite obstoječe vzorce dostopa frontenda, da frontend ne potrebuje sprememb.

**Pred** — Chat Completions backend je običajno seraliziral slovar `choices[0]` za vsak kos:
```python
# Staro: serijaliziran celoten slovar izbir na kos
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend bere: `response.delta.content` (globoka pot do izbire objekta).

**Po** — Responses API backend oddaja minimalno obliko, ki ohranja enako pot dostopa frontenda:
```python
# Novo: oddajajte samo tisto, kar potrebuje frontend
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend še vedno bere `response.delta.content` — **spremembe frontenda niso potrebne**.

> **Ključni vpogled**: Oblika pretakanja Responses API (`event.type` + `event.delta`) je osnovno drugačna od Chat Completions (`chunk.choices[0].delta.content`). Vendar je pogodba med backendom in frontendom vaša definicija. Oblikujte izhod backenda tako, da ustreza pričakovanjem frontenda.

## Sekvenca dogodkov pretakanja

Ko je `stream: true`, API oddaja dogodke v tem vrstnem redu:
1. `response.created` – objekt odgovora inicializiran
2. `response.in_progress` – začetek generiranja
3. `response.output_item.added` – izhodni element ustvarjen
4. `response.content_part.added` – del vsebine začel
5. `response.output_text.delta` – kosci besedila (več, vsak ima `delta: string`)
6. `response.output_text.done` – generiranje besedila končano
7. `response.content_part.done` – del vsebine končan
8. `response.output_item.done` – izhodni element končan
9. `response.completed` – odgovor v celoti zaključen

Za osnovno pretakanje besedila obravnavajte samo `response.output_text.delta` (za kose besedila) in `response.completed` (za zaključek).

## Obravnava napak pri pretakanju v spletnih aplikacijah

Pri pretakanju v spletni aplikaciji zavijte asinhrono iteracijo v `try/except` in oddajajte napake kot JSON, da jih frontend lahko prijazno prikaže (npr. omejitve hitrosti, začasne napake):

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

> **Zakaj je to pomembno**: Azure OpenAI vrne `429 Too Many Requests` ob omejevanju hitrosti. Brez `try/except` tok pretakanja tiho preneha. Z `try/except` frontend prejme `{"error": "Too Many Requests"}` in lahko prikaže poziv za ponovni poskus.

## Vrste dogodkov pretakanja (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Oblika pogovora
```python
# Responses API podpira format pogovora preko vhodne tabele
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

## Obravnava napak filtra vsebine

Struktura telesa napake se je spremenila iz Chat Completions v Responses API.

Pred (Chat Completions):
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

Ključne razlike:
- Ovitek `innererror` je **odpravljen** — podrobnosti filtra vsebine so zdaj na najvišji ravni `error.body`.
- `content_filter_result` (ednina) → `content_filters` (množina polje) vsebuje `content_filter_results` (množina) v vsaki vnosni enoti.
- Vsaka enota v `content_filters` vključuje `blocked`, `source_type` in `content_filter_results` z detajli po kategorijah (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Polna struktura telesa napake filtra vsebine Responses API:
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

## Raw HTTP migracija (requests/httpx)

Če aplikacija kliče Azure OpenAI REST neposredno namesto preko SDK:

Pred (Chat Completions):
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

> **Opomba**: `output_text` je priročna lastnost objekta `Response` v Python SDK. Surov REST JSON odgovor nima vrhnjega polja `output_text` — besedilo je v `output[0].content[0].text`.

## Večkrožni pogovor
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

Vsebinsko označen večkrožni (izrecno `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Večkrožni preko `previous_response_id` (alternativa)

Namesto, da upravljate polje pogovora sami, lahko povežete odgovore
na strežniški strani z uporabo `previous_response_id`. API shrani vsak odgovor in
samodejno predponira prejšnje korake.

```python
# Prvi potez
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Naslednji potezi — preprosto pošljite novo uporabniško sporočilo + ID prejšnjega odgovora
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Kdaj uporabiti kaj:**

| Pristop | Prednosti | Slabosti |
|---|---|---|
| polje `input` (ročni) | Poln nadzor nad zgodovino; lahko obrežete/povzamete; ni potrebno shranjevanje na strežniku (`store=False`) | Več kode; vi upravljate polje |
| `previous_response_id` | Enostavnejša koda; samodejno povezovanje | Zahteva `store=True` (privzeto); pogovor shranjen na strežniku; ne morete spreminjati zgodovine med koraki |

> **Opomba o migraciji:** Večina aplikacij Chat Completions že upravlja svoje lastno polje sporočil, zato je pretvorba v polje `input` bolj neposredna 1:1 migracija. Uporabite `previous_response_id` za novo kodo ali kadar ne potrebujete manipulacije zgodovine pogovora.

## Modeli O-serije za razmišljanje (o1, o3-mini, o3, o4-mini)

Modeli O-serije imajo posebne omejitve parametrov pri migraciji na Responses API.

### Preslikava parametrov za o-serijo

| Chat Completions (o-serija) | Responses API | Opombe |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Nastavite visoko (4096+) — tokni za razmišljanje štejejo v omejitev |
| `reasoning_effort` | `reasoning.effort` | Ohranite kot je, če je prisotno (low/medium/high) |
| `temperature` | Odstranite ali nastavite na `1` | O-serija sprejema samo `1` |
| `top_p` | Odstranite | Ni podprto na o-seriji |
| `seed` | Odstranite | Ni podprto v Responses API |

### O-serija pred/po

Pred (Chat Completions z o-serijo):
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

> **Opomba**: Modeli O-serije lahko pred oddajo tekstovnih delta najprej buferirajo izhod med razmišljanjem. Pretakanje še vedno deluje, a prvi dogodek `response.output_text.delta` lahko pride z daljšim zamikom kot pri GPT modelih.

## Dostop do tokenov razmišljanja
```python
# Modeli sklepanja uporabljajo notranje sklepanja — lahko vidite, koliko sklepnih žetonov je bilo uporabljenih
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

> **Pomembno**: Uporabite `max_output_tokens=1000` (ne 50–200), da upoštevate notranji proces razmišljanja modelov. Model znotraj uporablja tokne razmišljanja pred generiranjem končnega izhoda.

## Strukturiran izhod — JSON shema
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

- Definirajte funkcije v `tools` z **plosko obliko Responses API** — `name`, `description` in `parameters` na vrhnji ravni (ne gnezdeno pod `function`).
- Ko model zahteva klic orodja, ga izvedite v svoji aplikaciji in vključite rezultat orodja v naslednji zahtevek kot element `function_call_output` znotraj `input`.
- Ohranite sheme minimalne; validirajte vhode pred izvajanjem.
- Ko uporabljate `strict: true`, morajo biti vse lastnosti na seznamu `required` in obvezna je nastavitev `additionalProperties: false`.

> **⚠️ `pydantic_function_tool()` ni združljiv**: Pomočnik `openai.pydantic_function_tool()` še vedno generira staro gnezdeno obliko Chat Completions (`{"type": "function", "function": {"name": ...}}`). Ne uporabljajte ga z `responses.create()`. Definirajte sheme orodij ročno ali napišite ovijalec za ploskovanje izhoda.

### Oblika definicije orodja

Responses API uporablja **plosko** obliko orodja — `name`, `description`, `parameters` so ključ na vrhnji ravni (ne gnezdeno pod `function`).

**Pred (Chat Completions — gnezdeno):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Po (Responses API — plosko):**
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

Z `strict: true` (prisila sheme):
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
            "required": ["city_name"],       # Vse lastnosti MORAJO biti navedene
            "additionalProperties": False,   # Potrebno za strogi način
        },
    }
]
```

### Klic orodja s povratkom (izvedite in vrnite rezultate)

Ko model zahteva klic orodja, uporabite elemente `response.output` + `function_call_output` — **ne** vzorec Chat Completions `role: assistant` + `role: tool`.

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
    # Dodaj elemente function_call modela v pogovor
    messages.extend(response.output)

    # Zaženi vsako orodje in dodaj rezultate
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Pridobi končni odgovor z rezultati orodij
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Primeri nekaj klicev orodja

Ko zagotavljate nekaj primerov klicev orodij v `input`, uporabite elemente `function_call` in `function_call_output`. ID-ji morajo začeti z `fc_`.

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

Predmeti vsebine slike spremenijo tip iz `image_url` v `input_image`, URL pa se spremeni iz gnezdenega objekta v plosko nizko vrednost.

### Vnos slike — pred (Chat Completions)
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

### Vnos slike — po (Responses API, URL)
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

### Vnos slike — po (Responses API, base64)
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

**Najprej preverite svojo različico MAF** — migracija je odvisna od tega, ali ste na MAF 1.0.0+ ali pred 1.0.0 beta/rc različici.

Za preverjanje: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

V MAF 1.0.0+ `OpenAIChatClient` **že uporablja Responses API** — migracija ni potrebna.

Če koda uporablja zastareli `OpenAIChatCompletionClient` (ki uporablja `chat.completions.create`), ga zamenjajte z `OpenAIChatClient`:

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

### MAF pred 1.0.0 (beta/rc izdaje)

V pred-1.0.0 MAF je `OpenAIChatClient` uporabljal Chat Completions. Nadgradite na `agent-framework-openai>=1.0.0`, kjer `OpenAIChatClient` po privzetku uporablja Responses API.

> **Opomba**: API-ji `Agent`, `MCPStreamableHTTPTool` in drugi MAF ostajajo nespremenjeni — spremeni se samo uvoz in instanciranje razreda klienta.

## Migracija LangChain (`langchain-openai`)

Dodajte `use_responses_api=True` v `ChatOpenAI()`. Posodobite tudi dostop do vsebine sporočil iz `.content` na `.text`.

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

# ... klic agenta ...
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

# ... klic agenta ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Ključne spremembe**: (1) `use_responses_api=True` v konstruktorju, (2) `.content` → `.text` pri sporočilih odziva.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->