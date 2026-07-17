# Atsakymų API Greitasis vadovas (Python + Azure OpenAI)

> Visi žemiau pateikti kodų fragmentai daro prielaidą, kad `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` ir `client` jau inicializuotas (žr. kliento sąranką).

## Pagrindinis užklausos pavyzdys
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Kliento sąranka — EntraID (rekomenduojama)
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

## Kliento sąranka — API raktas
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Asinchroninė kliento sąranka — EntraID
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

## Asinchroninė kliento sąranka — EntraID su aiškiu nuomininko nurodymu (daugiarahmenė)

Kai Azure OpenAI resursas yra **kitoje nuomininko aplinkoje** nei numatytoji, perduokite `tenant_id` tiesiogiai autentifikacijai. Tai būdinga kūrimo/testavimo scenarijuose, kai kūrėjo pagrindinis nuomininkas skiriasi nuo resurso nuomininko.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential gamybai (Azure Container Apps, App Service ir kt.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # vartotojo priskirta valdomoji tapatybė
)
# AzureDeveloperCliCredential vietinei plėtrai – būtinas aiškus tenant_id nurodymas
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Grandinė: pirmiausia bandyti valdomą tapatybę, jei nepavyksta – pereiti prie azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Asinchroninio kliento migracija — prieš/po

Prieš (naudojant pasenusią):
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

## Pilna sinchroninė migracija — prieš/po

Prieš (senovinė – Azure OpenAI Pokalbių papildiniai):
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

Po (Responses API — Azure OpenAI v1 galutinis taškas):
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

## Srautinis perdavimas (sinchroninis)
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
        print()  # nauja eilutė pabaigoje
```

## Srautinis perdavimas (asinchroninis)
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

## Internetinės svetainės srautas — backend-to-frontend struktūra

Migravimo metu, kai internetinė svetainė perduoda SSE/JSONL į frontend'ą, **backend serializacijos formatas** keičiasi. Sukurkite naują backend'ą taip, kad būtų išlaikyti dabartiniai frontend'o prieigos būdai, kad nereikėtų keisti frontend'o.

**Prieš** — Pokalbių papildinių backend'as paprastai seralizuodavo kiekvieno bloko `choices[0]` žodyną:
```python
# Senas: serijinis pilnas pasirinkimo žodynas kiekvienam segmentui
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend perskaito: `response.delta.content` (gilus kelias į pasirinkimo objektą).

**Po** — Responses API backend'as generuoja minimalų formatą išlaikantį tą patį frontend'o prieigos kelią:
```python
# Nauja: perduoti tik tai, ko reikia frontendui
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend vis dar skaito `response.delta.content` — **nereikia jokių frontend'o pakeitimų**.

> **Pagrindinis įžvalga**: Responses API srauto forma (`event.type` + `event.delta`) iš esmės skiriasi nuo Pokalbių papildinių (`chunk.choices[0].delta.content`). Tačiau jūsų backend-to-frontend sutartį galite apibrėžti patys. Formuokite backend'o išvestį atitikti tai, ko frontend'as jau tikisi.

## Srautinio įvykio seka

Kai `stream: true`, API išmeta įvykius šia tvarka:
1. `response.created` – atsakymo objektas inicijuotas
2. `response.in_progress` – generavimas pradėtas
3. `response.output_item.added` – išvesties elementas sukurtas
4. `response.content_part.added` – turinio dalis pradėta
5. `response.output_text.delta` – teksto fragmentai (daugybė, kiekvienas turi `delta: string`)
6. `response.output_text.done` – teksto generavimas baigtas
7. `response.content_part.done` – turinio dalis baigta
8. `response.output_item.done` – išvesties elementas baigtas
9. `response.completed` – pilnas atsakymas baigtas

Baziniam teksto srautui apdoroti tvarkykite tik `response.output_text.delta` (teksto fragmentams) ir `response.completed` (užbaigimui).

## Klaidų valdymas sraute internetinėse svetainėse

Kai srautas vyksta internetinėje svetainėje, apsupkite asinchroninę iteraciją `try/except` bloku ir skleiskite klaidas JSON formatu, kad frontend'as galėtų jas gražiai atvaizduoti (pvz., ribojimai, laikinės klaidos):

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


> **Kodėl tai svarbu**: Azure OpenAI grąžina `429 Too Many Requests` ribojant užklausų skaičių. Be `try/except`, srautinė atsakymo dalis tyliai nutrūksta. Su juo frontend gauna `{"error": "Too Many Requests"}` ir gali parodyti pakartotinį bandymą.

## Srautinio perdavimo įvykių tipai (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Pokalbio formatas
```python
# Atsakymų API palaiko pokalbio formatą naudojant įvesties masyvą
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

## Turinio filtro klaidų apdorojimas

Klaidos duomenų struktūra pasikeitė iš Chat Completions į Responses API.

Anksčiau (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Vėliau (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Pagrindiniai skirtumai:
- `innererror` apvalkalas yra **pašalintas** — turinio filtro detalės dabar yra aukščiausiame `error.body` lygyje.
- `content_filter_result` (vienaskaita) → `content_filters` (daugiskaita masyvas), kuriame yra `content_filter_results` (daugiskaita) kiekviename įraše.
- Kiekvienas `content_filters` įrašas apima `blocked`, `source_type` ir `content_filter_results` su atskirų kategorijų detalėmis (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Pilna Responses API turinio filtro klaidos duomenų struktūra:
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

## Žemo lygio HTTP migracija (requests/httpx)

Jei programa kviečia Azure OpenAI REST tiesiogiai, o ne per SDK:

Anksčiau (Chat Completions):
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

Vėliau (Responses API):
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

> **Pastaba**: `output_text` yra patogumo savybė Python SDK `Response` objekte. Žaliavinis REST JSON atsakymas neturi aukščiausio lygio `output_text` lauko — tekstas yra `output[0].content[0].text`.

## Daugiasvirtis pokalbis
```python
# Sukurkite pokalbį su Atsakymų API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Pridėkite asistento atsakymą prie pokalbio
messages.append({"role": "assistant", "content": response.output_text})

# Tęskite pokalbį
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Turinio tipizuotas daugiasvirtis (aiškūs `input_text` / `output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Daugiasvirtis naudojant `previous_response_id` (alternatyva)

Vietoje pokalbio masyvo valdymo savarankiškai, galite grandinti atsakymus
serverio pusėje naudodami `previous_response_id`. API saugo kiekvieną atsakymą ir
automatiškai prideda ankstesnius ėjimus.

```python
# Pirmas ėjimas
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Vėlesni ėjimai — tiesiog perduokite naują vartotojo žinutę + ankstesnio atsakymo ID
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Kada pasirinkti kurį:**

| Požiūris | Privalumai | Trūkumai |
|---|---|---|
| `input` masyvas (rankinis) | Pilnas kontrolės įrašų istorijai; galima trumpinti / apibendrinti; nereikia serverio saugyklos (`store=False`) | Daugiau kodo; jūs valdote masyvą |
| `previous_response_id` | Paprastesnis kodas; automatinis grandinimas | Reikalingas `store=True` (numatytasis); pokalbis saugomas serveryje; negalima keisti istorijos tarp ėjimų |

> **Migracijos pastaba:** Dauguma Chat Completions programėlių jau valdo savo žinučių masyvą, todėl konvertavimas į `input` masyvą yra tiesioginė 1:1 migracija. Naudokite `previous_response_id` naujam kodui arba kai nereikia valdyti pokalbio istorijos.

## O serijos samprotavimo modeliai (o1, o3-mini, o3, o4-mini)

O serijos modeliai turi unikalius parametrų apribojimus pereinant prie Responses API.

### Parametrų susiejimas o serijai

| Chat Completions (o serija) | Responses API | Pastabos |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | Nustatyti aukštą (4096+) — samprotavimo žetonai atskaitomi limitui |
| `reasoning_effort` | `reasoning.effort` | Palikti kaip yra, jei yra (low/medium/high) |
| `temperature` | Pašalinti arba nustatyti į `1` | Tik O-serija priima `1` |
| `top_p` | Pašalinti | Nėra palaikomas o-serijoje |
| `seed` | Pašalinti | Nėra palaikomas Responses API |

### O-serijos prieš/po

Prieš (Chat Completions su o-serija):
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

> **Pastaba**: O-serijos modeliai gali kaupinti išvestį samprotavimo metu prieš išsiunčiant teksto delta dalis. Srautinė transliacija vis dar veikia, tačiau pirmasis `response.output_text.delta` įvykis gali atvykti vėliau nei su GPT modeliais.

## Samprotavimo žetonų pasiekimas
```python
# Loginiai modeliai naudoja vidinį mąstymą — galite matyti, kiek loginio mąstymo žetonų buvo panaudota
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

> **Svarbu**: Naudokite `max_output_tokens=1000` (o ne 50–200), kad atsižvelgtumėte į samprotavimo modelių vidinius samprotavimo procesus. Modelis viduje naudoja samprotavimo žetonus prieš generuodamas galutinę išvestį.

## Struktūrizuota išvestis — JSON schema
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

## Įrankių naudojimas

- Apibrėžkite funkcijas `tools` naudodami **plokščią Responses API formatą** — `name`, `description` ir `parameters` yra viršutiniame lygyje (ne įdėti po `function`).
- Kai modelis prašo iškviesti įrankį, vykdykite jį programėlėje ir įtraukite įrankio rezultatą į kitą užklausą kaip `function_call_output` elementą `input` viduje.
- Laikykitės minimalios schemos; prieš vykdymą patvirtinkite įvestis.
- Naudojant `strict: true`, visi savybės privalo būti nurodytos `required` ir `additionalProperties: false` yra privalomas.

> **⚠️ `pydantic_function_tool()` yra nesuderinamas**: `openai.pydantic_function_tool()` pagalbinė funkcija vis dar generuoja seną Chat Completions įdėtą formatą (`{"type": "function", "function": {"name": ...}}`). Nenaudokite jos su `responses.create()`. Apibrėžkite įrankių schemas rankiniu būdu arba parašykite apvyniojimą, kad ištiesintumėte išvestį.

### Įrankio apibrėžimo formatas

Responses API naudoja **plokščią** įrankių formatą — `name`, `description`, `parameters` yra viršutinių raktų lygmenyje (ne po `function`).

**Prieš (Chat Completions — įdėta):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Po (Responses API — plokščia):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Pilnas pavyzdys:
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

Naudojant `strict: true` (schemos tikrinimas):
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
            "required": ["city_name"],       # Reikšmės PRIVALO būti nurodytos
            "additionalProperties": False,   # Privaloma griežtam režimui
        },
    }
]
```

### Įrankio kvietimo sugrįžtamoji eiga (vykdyti ir grąžinti rezultatus)

Kai modelis prašo įrankio kvietimo, naudokite `response.output` elementus + `function_call_output` — **ne** Chat Completions `role: assistant` + `role: tool` modelį.

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
    # Pridėti modelio function_call elementus į pokalbį
    messages.extend(response.output)

    # Vykdyti kiekvieną įrankį ir pridėti rezultatus
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Gauti galutinį atsakymą su įrankių rezultatais
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Pavyzdžiai, kaip vykdyti kelių-šūvių (few-shot) įrankių kvietimus

Pateikiant kelių-šūvių įrankio kvietimo pavyzdžius `input`, naudokite `function_call` ir `function_call_output` elementus. ID turi prasidėti `fc_`.

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
# Įmontuoto interneto paieškos pavyzdys
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Vaizdo įvestis

Vaizdo turinio elementų tipas keičiasi iš `image_url` į `input_image` ir URL keičiasi iš įdėto objekto į plokščią eilutę.

### Vaizdo įvestis — prieš (Chat Completions)
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

### Vaizdo įvestis — po (Responses API, URL)
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

### Vaizdo įvestis — po (Responses API, base64)
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

> **Pagrindiniai pakeitimai**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (įdėtas objektas) → `"image_url": "..."` (plokščia eilutė — HTTPS URL arba `data:image/...;base64,...` duomenų URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) migracija

**Pirmiausia patikrinkite savo MAF versiją** — migracija priklauso nuo to, ar turite MAF 1.0.0+ versiją, ar ankstesnę pre-1.0.0 beta/rc.

Patikrinimui: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ `OpenAIChatClient` **jau naudoja Responses API** — migracija nereikalinga.

Jei kodų bazė naudoja senamadišką `OpenAIChatCompletionClient` (naudojantį `chat.completions.create`), pakeiskite jį į `OpenAIChatClient`:

Prieš:
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

### MAF versija prieš 1.0.0 (beta/rc versijos)

Ankstyvoje MAF versijoje, `OpenAIChatClient` naudojo Chat Completions. Atnaujinkite į `agent-framework-openai>=1.0.0`, kur `OpenAIChatClient` pagal numatytuosius nustatymus naudoja Responses API.

> **Pastaba**: `Agent`, `MCPStreamableHTTPTool` ir kitos MAF API išlieka nepakitusios — keičiasi tik kliento klasės importavimas ir kūrimas.

## LangChain (`langchain-openai`) migracija

Pridėkite `use_responses_api=True` prie `ChatOpenAI()`. Taip pat atnaujinkite žinučių turinio pasiekimą iš `.content` į `.text`.

Prieš:
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

# ... agento kvietimas ...
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

# ... agento kvietimas ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Pagrindiniai pakeitimai**: (1) konstruktoriuje `use_responses_api=True`, (2) `.content` → `.text` atsakymų žinutėse.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->