# Atsakymų API greita nuoroda (Python + Azure OpenAI)

> Visi žemiau pateikti kodo fragmentai daro prielaidą, kad `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]`, o `client` jau yra inicijuotas (žr. kliento nustatymą).

## Pagrindinis užklausimas
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Kliento nustatymas — EntraID (rekomenduojama)
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

## Kliento nustatymas — API raktas
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Asinchroninis kliento nustatymas — EntraID
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

## Asinchroninis kliento nustatymas — EntraID su aiškiu nuomininko nurodymu (daugianuomininkis)

Kai Azure OpenAI ištekliai yra **kitame nuomininke** nei numatytasis, nurodykite `tenant_id` tiesiogiai kredencialui. Tai įprasta kūrimo/testavimo scenarijuose, kai kūrėjo pagrindinis nuomininkas skiriasi nuo išteklių nuomininko.

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
    client_id=os.getenv("AZURE_CLIENT_ID")  # vartotojo priskirta valdoma tapatybė
)
# AzureDeveloperCliCredential vietiniam vystymui — aiškus tenant_id yra labai svarbus
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Grandinė: pirmiausia bandykite valdomą tapatybę, jei nepavyksta, pereikite prie azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Asinchroninis kliento migravimas — prieš/po

Prieš (pasenęs):
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

## Viso sinchroninio migravimas — prieš/po

Prieš (senas — Azure OpenAI pokalbių užbaigimai):
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

Po (Atsakymų API — Azure OpenAI v1 galinis taškas):
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

## Srautinimas (sinchroninis)
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

## Srautinimas (asinchroninis)
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

## Tinklalapio programos srautinimas — nuo serverio prie kliento forma

Migravimo metu iš SSE/JSONL srautą siunčiančio tinklalapio programos backend keičiasi **serverio serializavimo formatas**. Sukurkite naują serverio išvestį taip, kad išlaikytumėte esamus kliento prieigos modelius, kad klientui nereikėtų keisti kodo.

**Prieš** — Pokalbių užbaigimų serveris dažniausiai serializuodavo kiekvieno gabalo `choices[0]` žodyną:
```python
# Senas: serializuotas pilnas pasirinkimų žodynas kiekvienam skaidiniui
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Klientas skaito: `response.delta.content` (gilus kelias į pasirinkimo objektą).

**Po** — Atsakymų API serveris siunčia minimalų formatą, išlaikantį tą patį kliento prieigos kelią:
```python
# Nauja: perduoti tik tai, ko reikia frontendui
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Klientas vis dar skaito `response.delta.content` — **nereikia pakeisti kliento kodo**.

> **Pagrindinė įžvalga**: Atsakymų API srautinio duomenų formatu (`event.type` + `event.delta`) iš esmės skiriasi nuo Pokalbių užbaigimų (`chunk.choices[0].delta.content`). Tačiau jūsų serverio ir kliento sutartis yra jūsų valioje. Formatuokite serverio išvestį pagal tai, ko klientas jau tikisi.

## Srautinio įvykio seka

Kai `stream: true`, API siunčia įvykius šia tvarka:
1. `response.created` – inicijuojamas atsakymo objektas
2. `response.in_progress` – pradėtas generavimas
3. `response.output_item.added` – sukurtas išvesties elementas
4. `response.content_part.added` – pradėtas turinio elementas
5. `response.output_text.delta` – teksto gabalai (keli, kiekvienas turi `delta: string`)
6. `response.output_text.done` – teksto generavimas baigtas
7. `response.content_part.done` – turinio elementas baigtas
8. `response.output_item.done` – išvesties elementas baigtas
9. `response.completed` – viso atsakymo pabaiga

Pagrindiniam teksto srautui apdoroti tvarkykite tik `response.output_text.delta` (teksto gabalams) ir `response.completed` (pabaigai).

## Srautinio klaidų valdymas tinklalapio programose

Srautinio duomenų gavimo metu tinklalapio programoje, apvyniokite asinchroninį iteravimą `try/except` bloku ir perduokite klaidas JSON formatu, kad klientas galėtų jas gražiai parodyti (pvz., ribojimai, laikini sutrikimai):

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

> **Kodėl tai svarbu**: Azure OpenAI siunčia `429 Too Many Requests` ribojant užklausų dažnį. Be `try/except` srautas tyliai nutrūksta. Su juo klientas gauna `{"error": "Too Many Requests"}` ir gali parodyti pakartojimo kvietimą.

## Srautinio įvykių tipai (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Pokalbio formatas
```python
# Atsakymų API palaiko pokalbio formatą per įvesties masyvą
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

## Turinį filtruojančių klaidų valdymas

Klaidos kūno struktūra pasikeitė nuo Pokalbių užbaigimų iki Atsakymų API.

Prieš (Pokalbių užbaigimai):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Po (Atsakymų API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Pagrindiniai skirtumai:
- `innererror` wrapper'is **nebegali būti** — turinio filtravimo detalės dabar yra viršutiniame `error.body` lygyje.
- `content_filter_result` (vienaskaita) → `content_filters` (daugybė masyve) turintys `content_filter_results` (daugybę) kiekviename įraše.
- Kiekvienas įrašas `content_filters` turi `blocked`, `source_type` ir `content_filter_results` su detalėmis pagal kategorijas (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Pilnas Atsakymų API turinio filtravimo klaidos struktūros pavyzdys:
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

## Žemos lygio HTTP migravimas (requests/httpx)

Jei programa tiesiogiai kviečia Azure OpenAI REST, vietoje SDK:

Prieš (Pokalbių užbaigimai):
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

Po (Atsakymų API):
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

> **Pastaba**: `output_text` yra patogumo savybė Python SDK `Response` objekte. Originalus REST JSON atsakymas neturi viršutinio `output_text` lauko — tekstas yra `output[0].content[0].text`.

## Daugiatūrio pokalbis
```python
# Sukurkite pokalbį naudodami Atsakymų API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Pridėti asistento atsakymą prie pokalbio
messages.append({"role": "assistant", "content": response.output_text})

# Tęsti pokalbį
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Turinys su tipais daugiatūriam pokalbiui (aiškūs `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Daugiatūris per `previous_response_id` (alternatyva)

Vietoje to, kad patys valdytumėte pokalbio masyvą, galite grandinti atsakymus
serverio pusėje naudodami `previous_response_id`. API saugo kiekvieną atsakymą ir
automatiškai prideda ankstesnius posūkius.

```python
# Pirmas ėjimas
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Vėlesni ėjimai – tiesiog perduokite naują naudotojo žinutę + ankstesnį atsakymo ID
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Kada naudoti kurį:**

| Požiūris | Privalumai | Trūkumai |
|---|---|---|
| `input` masyvas (rankinis) | Pilnas valdymas istorijai; galite apkarpyti / apibendrinti; nereikia serverio pusės saugojimo (`store=False`) | Daugiau kodo; patys valdote masyvą |
| `previous_response_id` | Paprastesnis kodas; automatinė grandinėlė | Reikalingas `store=True` (numatytasis); pokalbis saugomas serverio pusėje; negalima keisti istorijos tarp posūkių |

> **Migravimo pastaba:** Daugelis Pokalbių užbaigimų programų jau valdo savo žinučių masyvą, todėl konvertavimas į `input` masyvą yra tiesioginis 1:1 migravimas. Naudokite `previous_response_id` naujame kode arba kai nereikia keisti pokalbio istorijos.

## O serijos samprotavimo modeliai (o1, o3-mini, o3, o4-mini)

O serijos modeliai turi unikalius parametrų apribojimus migracijos į Atsakymų API metu.

### Parametrų atitikmenys o serijai

| Pokalbių užbaigimai (o serija) | Atsakymai API | Pastabos |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | Nustatykite aukštą (4096+) — samprotavimo žetonai skaičiuojami į ribą |
| `reasoning_effort` | `reasoning.effort` | Palikite kaip yra, jei yra (žemas/vidutinis/aukštas) |
| `temperature` | Pašalinkite arba nustatykite į `1` | O-serija priima tik `1` |
| `top_p` | Pašalinkite | Nesuportuojama o-serijoje |
| `seed` | Pašalinkite | Nesuportuojama Responses API |

### O-serija prieš / po

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

> **Pastaba**: O-serijos modeliai gali kaupoti išeitį samprotavimo metu prieš išvestant teksto pokyčius. Srautavimas vis dar veikia, bet pirmasis `response.output_text.delta` įvykis gali pasirodyti su ilgesniu vėlavimu nei GPT modelių atveju.

## Prieiga prie samprotavimo žetonų
```python
# Samprotavimo modeliai naudoja vidinį samprotavimą — galite pamatyti, kiek samprotavimo ženklų buvo panaudota
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

> **Svarbu**: Naudokite `max_output_tokens=1000` (ne 50–200), kad atitiktumėte samprotavimo modelių vidinį samprotavimo procesą. Modelis viduje naudoja samprotavimo žetonus prieš sukuriant galutinį rezultatai.

## Struktūruota išvestis — JSON schema
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

- Apibrėžkite funkcijas `tools` naudodami **flat Responses API formatą** — `name`, `description` ir `parameters` yra viršutiniame lygmenyje (ne po `function`).
- Kai modelis prašo iškviesti įrankį, vykdykite jį savo programoje ir įtraukite įrankio rezultatą į sekantį užklausą kaip `function_call_output` elementą `input`.
- Laikykite schemas minimalias; prieš vykdymą patikrinkite įvestis.
- Naudojant `strict: true`, visos savybės turi būti išvardytos `required` ir `additionalProperties: false` yra privalomas.

> **⚠️ `pydantic_function_tool()` nesuderinamas**: `openai.pydantic_function_tool()` pagalbinė funkcija vis dar generuoja seną Chat Completions įdėtą formatą (`{"type": "function", "function": {"name": ...}}`). Nenaudokite su `responses.create()`. Apibrėžkite įrankio schemas rankiniu būdu arba sukurkite apvalkalą, kuris suplokština išeitį.

### Įrankio apibrėžimo formatas

Responses API naudoja **flat** įrankio formatą — `name`, `description`, `parameters` yra viršutinio lygmens raktai (ne po `function`).

**Prieš (Chat Completions — įdėta):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Po (Responses API — flat):**
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

Su `strict: true` (schema laikymasis):
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
            "required": ["city_name"],       # Visos savybės TURI būti išvardytos
            "additionalProperties": False,   # Būtina griežtam režimui
        },
    }
]
```

### Įrankių kvietimo ciklas (vykdymas ir rezultatų grąžinimas)

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
    # Pridėkite modelio function_call elementus prie pokalbio
    messages.extend(response.output)

    # Vykdykite kiekvieną įrankį ir pridėkite rezultatus
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Gaukite galutinį atsakymą su įrankių rezultatais
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Keletas pavyzdžių, kaip kviečiami įrankiai

Kai pateikiate keletą pavyzdžių su įrankių kvietimais `input`, naudokite `function_call` ir `function_call_output` elementus. ID turi prasidėti `fc_`.

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

## Vaizdų įvestis

Vaizdo turinio elementų tipas keičiasi iš `image_url` į `input_image`, o URL keičiasi iš įdėto objekto į plokščią tekstą.

### Vaizdų įvestis — prieš (Chat Completions)
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

### Vaizdų įvestis — po (Responses API, URL)
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

### Vaizdų įvestis — po (Responses API, base64)
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

> **Pagrindiniai pakeitimai**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (įdėtas objektas) → `"image_url": "..."` (plokščias tekstas — HTTPS URL arba `data:image/...;base64,...` duomenų URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) migracija

**Pirmiausia patikrinkite savo MAF versiją** — migracija priklauso nuo to, ar turite MAF 1.0.0+ ar pre-1.0.0 beta/rc versiją.

Patikrinimui: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Dėl MAF 1.0.0+ `OpenAIChatClient` **jau naudoja Responses API** — migracija nereikalinga.

Jei kodo bazė naudoja legacy `OpenAIChatCompletionClient` (kuris naudoja `chat.completions.create`), pakeiskite jį į `OpenAIChatClient`:

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

### MAF pre-1.0.0 (beta/rc leidimai)

Pre-1.0.0 MAF, `OpenAIChatClient` naudojo Chat Completions. Atnaujinkite į `agent-framework-openai>=1.0.0`, kur `OpenAIChatClient` pagal nutylėjimą naudoja Responses API.

> **Pastaba**: `Agent`, `MCPStreamableHTTPTool` ir kiti MAF API lieka nepakitę — keičiasi tik kliento klasės importas ir instancijavimas.

## LangChain (`langchain-openai`) migracija

Pridėkite `use_responses_api=True` į `ChatOpenAI()`. Taip pat atnaujinkite žinučių turinio prieigą iš `.content` į `.text`.

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

# ... agente kvietimas ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Pagrindiniai pakeitimai**: (1) konstruktoriuje `use_responses_api=True`, (2) `.content` → `.text` atsakymų žinutėse.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->