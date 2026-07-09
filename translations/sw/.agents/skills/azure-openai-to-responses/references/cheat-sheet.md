# Karatasi ya Mwongozo wa Responses API (Python + Azure OpenAI)

> Vipande vyote hapa chini vinadhani `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` na `client` tayari imeanzishwa (angalia usanidi wa mteja).

## Ombi la msingi
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Usanidi wa mteja — EntraID (inayopendekezwa)
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

## Usanidi wa mteja — Kitufe cha API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Usanidi wa mteja async — EntraID
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

## Usanidi wa mteja async — EntraID na nyumba ya wapangaji wazi (multi-tenant)

Wakati rasilimali ya Azure OpenAI iko katika **mpangaji tofauti** tofauti na default, pita `tenant_id` wazi kwa cheti cha uthibitisho. Hii ni kawaida katika hali za maendeleo/majaribio ambapo mpangaji wa nyumbani wa msanidi programu ni tofauti na mpangaji wa rasilimali.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential kwa uzalishaji (Azure Container Apps, App Service, n.k.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # utambulisho uliopewa mtumiaji ulioendeshwa
)
# AzureDeveloperCliCredential kwa maendeleo ya ndani — tenant_id wazi ni muhimu
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Mnyororo: jaribu utambulisho unaodhibitiwa kwanza, acha CLI ya azd
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Uhamisho wa mteja async — kabla/baada

Kabla (haipitiki):
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

Baada:
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

## Uhamisho kamili wa sinkroni — kabla/baada

Kabla (ya zamani — Azure OpenAI Chat Completions):
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

Baada (Responses API — sehemu ya Azure OpenAI v1):
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

## Uendelezaji wa moja kwa moja (sinkroni)
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
        print()  # mstari mpya mwishoni
```

## Uendelezaji wa moja kwa moja (async)
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

## Uendelezaji wa wavuti — muundo kutoka nyuma-kwenda-mbele

Unapohamisha programu ya wavuti inayotumia utiririshaji SSE/JSONL kwa mbele, **muundo wa serialization wa nyuma** hubadilika. Tengeneza matokeo mapya ya nyuma ili kuhifadhi njia za upatikanaji za mbele zilizopo ili mbele isihitaji mabadiliko yoyote.

**Kabala** — Chat Completions kwa kawaida iliyotumia serialization ya kamusi ya kila kipande `choices[0]`:
```python
# Zamani: kamusi kamili iliyo serializa kwa kila kipande
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Kusoma mbele: `response.delta.content` (njia kwa kina ndani ya kitu cha chaguo).

**Baada** — Responses API ya nyuma hutuma muundo mdogo unaoendeleza njia ile ile ya upatikanaji wa mbele:
```python
# Mpya: toa tu kilichohitajika na sehemu ya mbele
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Mbele bado inasoma `response.delta.content` — **pasipo mabadiliko ya mbele**.

> **Kidokezo muhimu**: Muundo wa utiririshaji wa Responses API (`event.type` + `event.delta`) ni tofauti kabisa na Chat Completions (`chunk.choices[0].delta.content`). Lakini mkataba wako wa nyuma-kwenda-mbele ni wako kuamua. Tengeneza matokeo ya nyuma kuyaendana na matarajio ya mbele.

## Mfuatano wa matukio ya utiririshaji

Unapokuwa na `stream: true`, API hutuma matukio kwa mpangilio huu:
1. `response.created` – kitu cha majibu kimeanzishwa
2. `response.in_progress` – kizazi kimeanza
3. `response.output_item.added` – kipengele cha matokeo kimeundwa
4. `response.content_part.added` – sehemu ya maudhui imeanza
5. `response.output_text.delta` – vipande vya maandishi (vingi, kila kikiwa na `delta: string`)
6. `response.output_text.done` – kizazi cha maandishi kimekamilika
7. `response.content_part.done` – sehemu ya maudhui imekamilika
8. `response.output_item.done` – kipengele cha matokeo kimekamilika
9. `response.completed` – majibu kamili yamekamilika

Kwa utiririshaji wa maandishi wa msingi, shughulikia tu `response.output_text.delta` (kwa vipande vya maandishi) na `response.completed` (kwa kumaliza).

## Ushughulikiaji wa makosa ya utiririshaji katika programu za wavuti

Unapotiririsha katika programu ya wavuti, funika mzunguko wa async kwa `try/except` na toa makosa kama JSON ili mbele iweze kuonyesha kwa heshima (mfano, mipaka ya kasi, kushindwa kwa muda):

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

> **Kwa nini hili ni muhimu**: Azure OpenAI hurejelea `429 Too Many Requests` wakati wa mipaka ya kasi. Bila `try/except`, jibu la utiririshaji linaisha kimya. Ukiwa na, mbele hupokea `{"error": "Too Many Requests"}` na inaweza kuonyesha amri ya kujaribu tena.

## Aina za matukio ya utiririshaji (SDK ya Python)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Muundo wa mazungumzo
```python
# API ya Majibu inaunga mkono muundo wa mazungumzo kupitia safu ya pembejeo
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

## Ushughulikiaji wa makosa ya chujio la maudhui

Muundo wa mwili wa makosa umebadilika kutoka Chat Completions kwenda Responses API.

Kabla (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Baada (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Tofauti kuu:
- Kifuniko cha `innererror` kimeondoka — maelezo ya chujio la maudhui sasa yuko ngazi ya juu ya `error.body`.
- `content_filter_result` (moja) → `content_filters` (orodha nyingi) zenye `content_filter_results` ndani ya kila kipengee.
- Kila kipengee katika `content_filters` kinajumuisha `blocked`, `source_type`, na `content_filter_results` na maelezo kwa kila aina (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Muundo kamili wa mwili wa makosa ya chujio la maudhui wa Responses API:
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

## Uhamisho wa raw HTTP (requests/httpx)

Ikiwa app inaita Azure OpenAI REST moja kwa moja badala ya kutumia SDK:

Kabla (Chat Completions):
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

Baada (Responses API):
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

> **Kumbuka**: `output_text` ni mali ya urahisi kwenye kitu cha `Response` cha SDK ya Python. Jibu halisi la JSON la REST halina sehemu ya juu ya `output_text` — maandishi yako kwenye `output[0].content[0].text`.

## Mazungumzo ya mizunguko mingi
```python
# Tengeneza mazungumzo na API ya Majibu
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Ongeza jibu la msaidizi kwenye mazungumzo
messages.append({"role": "assistant", "content": response.output_text})

# Endelea na mazungumzo
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Mazungumzo ya mizunguko mingi yenye aina za maudhui (wazi `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Mizunguko mingi kupitia `previous_response_id` (mbadala)

Badala ya kusimamia orodha ya mazungumzo mwenyewe, unaweza kuunganisha majibu
upande wa server kwa kutumia `previous_response_id`. API huhifadhi kila jibu na
kiotomatiki huongeza mizunguko ya awali.

```python
# Zamu ya kwanza
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Zamu zinazofuata — tumia tu ujumbe mpya wa mtumiaji + kitambulisho cha jibu la awali
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Lini kutumia ipi:**

| Njia | Faida | Hasara |
|---|---|---|
| orodha ya `input` (ya mkono) | Udhibiti kamili juu ya historia; unaweza kukata/kufupisha; hakuna uhifadhi upande wa server unahitajika (`store=False`) | Msimbo zaidi; wewe unasimamia orodha |
| `previous_response_id` | Msimbo rahisi; uunganisho wa moja kwa moja | Inahitaji `store=True` (chaguo-msingi); mazungumzo huhifadhiwa upande wa server; huwezi kubadilisha historia kati ya mizunguko |

> **Kumbuka kuhusu uhamisho:** Programu nyingi za Chat Completions tayari husimamia orodha yao ya ujumbe, hivyo kubadili kuwa orodha `input` ni uhamisho wa moja kwa moja 1:1. Tumia `previous_response_id` kwa msimbo mpya au wakati huna haja ya kubadilisha historia ya mazungumzo.

## Modeli za mfululizo wa O (o1, o3-mini, o3, o4-mini)

Modeli za mfululizo wa O zina vizingiti maalum vya parameta wakati wa kuhamia Responses API.

### Ramani ya parameta kwa mfululizo wa o

| Chat Completions (mfululizo wa o) | Responses API | Maelezo |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Weka juu (4096+) — tokene za mawazo zinahesabiwa dhidi ya kikomo |
| `reasoning_effort` | `reasoning.effort` | Ziweke kama zilivyo ikiwa zipo (chini/wastani/juu) |
| `temperature` | Ondoa au weka `1` | Mfululizo wa o unakubali tu `1` |
| `top_p` | Ondoa | Hauiungi mkono mfululizo wa o |
| `seed` | Ondoa | Hauiungi mkono katika Responses API |

### Mfululizo wa o kabla/baada

Kabla (Chat Completions na mfululizo wa o):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Baada (Responses API):
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

> **Kumbuka**: Modeli za mfululizo wa O zinaweza kuweka matokeo akiba wakati wa mawazo kabla ya kutoa matukio ya maandishi. Utiririshaji bado unafanya kazi lakini tukio la kwanza la `response.output_text.delta` linaweza kuja baada ya kuchelewa zaidi ikilinganishwa na modeli za GPT.

## Kupata tokene za mawazo
```python
# Mifano ya uelewa hutumia uelewa wa ndani — unaweza kuona idadi ya tokeni za uelewa zilizotumika
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

> **Muhimu**: Tumia `max_output_tokens=1000` (sio 50–200) kuzingatia mchakato wa ndani wa mawazo wa modeli za mawazo. Modeli hutumia tokeni za mawazo ndani kabla ya kuzalisha matokeo ya mwisho.

## Matokeo yaliyojengwa — JSON Schema
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

## Matumizi ya zana

- Tambua kazi katika `tools` kwa **muundo mflat wa Responses API** — `name`, `description`, na `parameters` ziko ngazi ya juu (si chini ya `function`).
- Ukiona modeli ikaagiza kuita zana, itekeleze kwenye app yako na weka matokeo ya zana katika ombi lijalo kama kipengee cha `function_call_output` ndani ya `input`.
- Hakikisha schemas ni ndogo; hakiki maingizo kabla ya kutekeleza.
- Ukitumia `strict: true`, mali zote lazima zilistwe katika `required` na `additionalProperties: false` ni lazima.

> **⚠️ `pydantic_function_tool()` haifanyi kazi**: Msaidizi `openai.pydantic_function_tool()` bado hutengeneza muundo wa zamani wa Chat Completions uliotengenezwa ndani (`{"type": "function", "function": {"name": ...}}`). Usitumie na `responses.create()`. Tambua schemas za zana kama kawaida au andika wrapper ya kuzipa flat.

### Muundo wa kufafanua zana

Responses API hutumia muundo wa zana **mflat** — `name`, `description`, `parameters` ni funguo za ngazi ya juu (si chini ya `function`).

**Kabala (Chat Completions — nested):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Baada (Responses API — mflat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Mfano kamili:
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

Ukiwa na `strict: true` (kufuatilia schema):
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
            "required": ["city_name"],       # Mali zote ZINAHITAJI kuorodheshwa
            "additionalProperties": False,   # Inahitajika kwa hali kali
        },
    }
]
```

### Mzunguko wa kuitwa zana (tekeleza na rudisha matokeo)

Wakati modeli ikaagiza kuita zana, tumia vipengee vya `response.output` + `function_call_output` — **si** utaratibu wa Chat Completions `role: assistant` + `role: tool`.

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
    # Ongeza vitu vya function_call vya modeli kwenye mazungumzo
    messages.extend(response.output)

    # Tekeleza kila chombo na ongeza matokeo
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Pata jibu la mwisho pamoja na matokeo ya chombo
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Mifano michache ya kuitwa zana

Unapotoa mifano michache ya kuitwa zana katika `input`, tumia vipengee vya `function_call` na `function_call_output`. IDs lazima ziwe na `fc_` mwanzoni.

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
# Mfano wa utafutaji wa wavuti uliojengewa ndani
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Ingizo la picha

Vipengee vya maudhui ya picha hubadilisha aina kutoka `image_url` kuwa `input_image`, na URL hubadilika kutoka kitu kilichozamishwa kuwa herufi moja mviringo.

### Ingizo la picha — kabla (Chat Completions)
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

### Ingizo la picha — baada (Responses API, URL)
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

### Ingizo la picha — baada (Responses API, base64)
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

> **Mabadiliko muhimu**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (kitu kilichozamishwa) → `"image_url": "..."` (herufi moja — iwe URL ya HTTPS au `data:image/...;base64,...` URI ya data), (3) `"type": "text"` → `"type": "input_text"`.

## Uhamisho wa Microsoft Agent Framework (MAF)

**Kagua toleo lako la MAF kwanza** — uhamisho hutegemea kama uko MAF 1.0.0+ au toleo la beta/rc la kabla ya 1.0.0.

Kwa ukaguzi: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Katika MAF 1.0.0+, `OpenAIChatClient` **inatumia tayari Responses API** — hamu haina haja.

Ikiwa msimbo hutumia `OpenAIChatCompletionClient` ya kale (inayotumia `chat.completions.create`), badilisha na `OpenAIChatClient`:

Kabla:
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

Baada:
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

### MAF kabla ya 1.0.0 (toleo beta/rc)

Katika MAF kabla ya 1.0.0, `OpenAIChatClient` ilitumia Chat Completions. Boresha hadi `agent-framework-openai>=1.0.0` ambapo `OpenAIChatClient` inatumia Responses API kama chaguo-msingi.

> **Kumbuka**: API za `Agent`, `MCPStreamableHTTPTool`, na nyingine za MAF hazijabadilika — tu kuuza na kusanidi mteja kung'ang'ania.

## Uhamisho wa LangChain (`langchain-openai`)

Ongeza `use_responses_api=True` kwa `ChatOpenAI()`. Pia sasisha upatikanaji wa maudhui ya ujumbe kutoka `.content` kwenda `.text`.

Kabla:
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

# ... kuitwa kwa wakala ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Baada:
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

# ... kiitishaji cha wakala ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Mabadiliko muhimu**: (1) `use_responses_api=True` kwenye mjenzi, (2) `.content` → `.text` kwenye ujumbe wa majibu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->