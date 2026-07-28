# Jinsi ya Kutumia Responses API (Python + Azure OpenAI)

> Vibonye vyote hapa chini vinadhani `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` na `client` tayari imesanifiwa (angalia usanidi wa mteja).

## Ombi la Msingi
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Usanidi wa Mteja — EntraID (inapendekezwa)
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

## Usanidi wa Mteja — API key
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Usanidi wa Mteja Asynchronous — EntraID
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

## Usanidi wa Mteja Asynchronous — EntraID na tenant wazi (multi-tenant)

Wakati rasilimali ya Azure OpenAI iko kwenye **tenant tofauti** na chaguo-msingi, pita `tenant_id` wazi kwa cheti. Hii ni kawaida katika mazingira ya maendeleo/mtihani ambapo tenant ya msanidi programu ni tofauti na tenant ya rasilimali.

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
    client_id=os.getenv("AZURE_CLIENT_ID")  # utambulisho wa msimamizi uliotengwa kwa mtumiaji
)
# AzureDeveloperCliCredential kwa maendeleo ya ndani — tenant_id mahususi ni muhimu
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Mnyororo: jaribu kwanza utambulisho wa msimamizi, kisha rudi kwenye azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Uhamisho wa mteja asynch — kabla/baada

Kabla (imeachwa nusu):
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

## Uhamisho wa usawazishaji kamili — kabla/baada

Kabla (mila — Azure OpenAI Chat Completions):
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

Baada (Responses API — mstari wa mwisho wa Azure OpenAI v1):
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

## Kuendesha mfululizo (sync)
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

## Kuendesha mfululizo (async)
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

## Kivinjari cha wavuti kinapitisha mfululizo — muundo kutoka backend hadi frontend

Wakati unahama app ya wavuti inayotiririsha SSE/JSONL hadi frontend, **muundo wa serialization wa backend** hubadilika. Tengeneza maelezo mapya ya backend ili kuhifadhi muundo wa upatikanaji wa frontend ili frontend isihitaji mabadiliko.

**Kabla** — Backend ya Chat Completions kawaida ilisera kila kipande cha `choices[0]` cha kamusi:
```python
# Kale: kamusi iliyoorodheshwa kamili ya uchaguzi kwa kila kipande
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend husoma: `response.delta.content` (njia ndefu ndani ya kitu cha chaguo).

**Baada** — Backend ya Responses API hutoa muundo mdogo unaohifadhi njia ile ile ya upatikanaji wa frontend:
```python
# Mpya: tooa tu kile ambacho sehemu ya mbele inahitaji
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend bado husoma `response.delta.content` — **hakuna mabadiliko yanayohitajika kwa frontend**.

> **Uelewa wa msingi**: Muundo wa kuendesha mfululizo wa Responses API (`event.type` + `event.delta`) ni tofauti kabisa na Chat Completions (`chunk.choices[0].delta.content`). Lakini mkataba wako kutoka backend hadi frontend ni wako kuufafanua. Tengeneza maelezo ya backend ili yalingane na yale yanayotarajiwa na frontend.

## Mfuatano wa matukio ya mfululizo

Wakati `stream: true`, API hutoka matukio kwa mpangilio huu:
1. `response.created` – kitu cha majibu kimeanzishwa
2. `response.in_progress` – uzalishaji umeanza
3. `response.output_item.added` – kipengele cha matokeo kimeundwa
4. `response.content_part.added` – sehemu ya maudhui imeanza
5. `response.output_text.delta` – vipande vya maandishi (vingi, kila kikiwa na `delta: string`)
6. `response.output_text.done` – uzalishaji wa maandishi umekamilika
7. `response.content_part.done` – sehemu ya maudhui imekamilika
8. `response.output_item.done` – kipengele cha matokeo kimekamilika
9. `response.completed` – jibu kamili limekamilika

Kwa kuendesha mfululizo wa maandishi wa msingi, shughulikia tu `response.output_text.delta` (kwa vipande vya maandishi) na `response.completed` (kwa kumaliza).

## Usimamizi wa makosa ya uelekevu wa mfululizo katika apps za wavuti

Wakati uko kwenye uelekevu wa mfululizo katika app ya wavuti, jifungie kurudia async katika `try/except` na toa makosa kama JSON ili frontend iweze kuyaonyesha kwa upole (mfano, vikwazo vya kiwango, kushindwa kwa muda mfupi):

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

> **Kwa nini hili ni muhimu**: Azure OpenAI hurudisha `429 Too Many Requests` wakati wa kuweka viwango. Bila `try/except`, jibu la mfululizo hufa kimya kimya. Ukiwa na hili, frontend inapokea `{"error": "Too Many Requests"}` na inaweza kuonyesha ombi la jaribio tena.

## Aina za matukio ya mfululizo (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Muundo wa mazungumzo
```python
# API ya Majibu inaunga mkono muundo wa mazungumzo kupitia safu ya ingizo
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

## Usimamizi wa makosa ya kichujio cha maudhui

Muundo wa mwili wa kosa umebadilika kutoka Chat Completions hadi Responses API.

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
- Kifuniko cha `innererror` kime **ondolewa** — maelezo ya kichujio cha maudhui sasa yako safu ya juu ya `error.body`.
- `content_filter_result` (moja) → `content_filters` (orodha nyingi) zenye `content_filter_results` (nyingi) ndani ya kila kipengele.
- Kila kipengele katika `content_filters` kina `blocked`, `source_type`, na `content_filter_results` zenye maelezo kwa aina (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Muundo kamili wa mwili wa kosa la kichujio cha maudhui katika Responses API:
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

## Uhamiaji wa HTTP ghafi (requests/httpx)

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

> **Kumbuka**: `output_text` ni sifa ya urahisi kwenye kitu cha Python SDK `Response`. Jibu halisi la JSON la REST halina uwanja wa `output_text` wa safu ya juu — maandishi yako katika `output[0].content[0].text`.

## Mazungumzo ya mizunguko mingi
```python
# Jenga mazungumzo na API ya Majibu
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

Mizunguko mingi yenye aina ya maudhui (wazi `input_text`/`output_text`):
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

Badala ya kusimamia mwenyewe orodha ya mazungumzo, unaweza kuunganisha majibu
upande wa seva kwa kutumia `previous_response_id`. API huhifadhi kila jibu na
kiotomatiki huambatanisha mizunguko ya awali.

```python
# Zamu ya kwanza
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Zamu zinazofuata — tumia tu ujumbe mpya wa mtumiaji + kitambulisho cha majibu ya awali
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
| orodha ya `input` (manual) | Udhibiti kamili wa historia; unaweza kukata/kufupisha; haina haja ya kuhifadhi upande wa seva (`store=False`) | Msimbo mwingi; wewe husimamia orodha |
| `previous_response_id` | Msimbo rahisi; ufuatiliaji wa kiotomatiki | Inahitaji `store=True` (chaguo-msingi); mazungumzo huhifadhiwa upande seva; huwezi kubadilisha historia kati ya mizunguko |

> **Kumbusho la uhamisho:** Apps nyingi za Chat Completions tayari husimamia orodha zao za ujumbe, kwa hivyo kubadilisha kuwa orodha ya `input` ni uhamisho wa moja kwa moja 1:1. Tumia `previous_response_id` kwa msimbo mpya au wakati hauitaji kubadili historia ya mazungumzo.

## Modeli za uelewa wa mfululizo wa O (o1, o3-mini, o3, o4-mini)

Modeli za mfululizo wa O zina vizingiti maalum vya vigezo wakati wa kuhamia Responses API.

### Ramani ya vigezo kwa mfululizo wa O

| Chat Completions (mfululizo wa O) | Responses API | Maelezo |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Weka juu (4096+) — token za uelewa huhesabiwa dhidi ya kikomo |
| `reasoning_effort` | `reasoning.effort` | Acika kama ilivyo ikiwa ipo (chini/kati/juu) |
| `temperature` | Ondoa au weweka hadi `1` | Mfululizo wa O hupokea tu `1` |
| `top_p` | Ondoa | Haitegemezwe katika mfululizo wa O |
| `seed` | Ondoa | Haitegemezwe katika Responses API |

### Mfululizo wa O kabla/baada

Kabla (Chat Completions na mfululizo wa O):
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

> **Kumbuka**: Modeli za mfululizo wa O zinaweza kuhifadhi matokeo wakati wa uelewa kabla ya kutoa maandishi madogo. Kuendesha mfululizo bado kunaendelea na tukio la kwanza la `response.output_text.delta` linaweza kuja baada ya kuchelewa kwa muda mrefu zaidi kuliko modeli za GPT.

## Kupata token za uelewa
```python
# Mifano ya mantiki hutumia mantiki ya ndani — unaweza kuona ni tokeni ngapi za mantiki zilizotumika
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

> **Muhimu**: Tumia `max_output_tokens=1000` (si 50–200) kutokana na mchakato wa ndani wa uelewa wa modeli. Modeli hutumia token za uelewa ndani kabla ya kuzalisha matokeo ya mwisho.

## Matokeo yaliyo na muundo — JSON Schema
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

- Fafanua kazi katika `tools` kwa **muundo mlalo wa Responses API** — `name`, `description`, na `parameters` katika ngazi ya juu (si ndani ya `function`).
- Wakati modeli inaomba kuitisha zana, tekeleza ndani ya app yako na jumuisha matokeo ya zana katika ombi lijalo kama kipengele cha `function_call_output` ndani ya `input`.
- Hifadhi schemata kuwa ndogo; hakikisha kuhalalisha pembejeo kabla ya utekelezaji.
- Wakati una tumia `strict: true`, mali zote lazima zijiandikishe katika `required` na `additionalProperties: false` ni lazima.

> **⚠️ `pydantic_function_tool()` hainalingani**: Msaidizi `openai.pydantic_function_tool()` bado hutengeneza muundo wa zamani wa ndani wa Chat Completions (`{"type": "function", "function": {"name": ...}}`). Usitumiwe na `responses.create()`. Fafanua schemata za zana kwa mikono au andika kifuniko cha kuleta nje maelezo.

### Muundo wa ufafanuzi wa zana

Responses API hutumia muundo **mlalo** wa zana — `name`, `description`, `parameters` ni funguo za ngazi ya juu (si ndani ya `function`).

**Kablia (Chat Completions — ndani):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Baada (Responses API — mlalo):**
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

Ukiwa na `strict: true` (utekelezaji wa schema):
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
            "required": ["city_name"],       # Mali zote HITUPEWA
            "additionalProperties": False,   # Inahitajika kwa hali kali
        },
    }
]
```

### Mzunguko wa kuitisha zana (tekeleza na rudisha matokeo)

Wakati modeli inaomba kuitisha zana, tumia vipengele vya `response.output` + `function_call_output` — **siyo** mfano wa Chat Completions `role: assistant` + `role: tool`.

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
    # Ongeza vitu vya function_call vya mfano kwenye mazungumzo
    messages.extend(response.output)

    # Tekeleza kila chombo na ongeza matokeo
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Pata jibu la mwisho lenye matokeo ya chombo
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Mifano michache ya kuitisha zana

Wakati unatoa mifano michache ya kuitisha zana katika `input`, tumia vipengele vya `function_call` na `function_call_output`. Vitambulisho lazima viaanze na `fc_`.

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
# Mfano wa utafutaji wa wavuti uliojengwa ndani
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Ingizo la picha

Vipengele vya maudhui ya picha hubadilisha aina kutoka `image_url` hadi `input_image`, na URL hubadilika kutoka kitu kilicho ndani hadi kamba moja.

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

> **Mabadiliko makubwa**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (kitu kilicho ndani) → `"image_url": "..."` (kamba moja — URL ya HTTPS au `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Uhamisho wa Microsoft Agent Framework (MAF)

**Kagua toleo la MAF kwanza** — uhamisho hutegemea ikiwa uko kwenye MAF 1.0.0+ au toleo la beta/rc la kabla ya 1.0.0.

Kwa kuangalia: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Katika MAF 1.0.0+, `OpenAIChatClient` **tayari hutumia Responses API** — hamna haja ya uhamisho.

Ikiwa msimbo unatumia zamani `OpenAIChatCompletionClient` (inayotumia `chat.completions.create`), badilisha kuwa `OpenAIChatClient`:

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

### MAF kabla ya 1.0.0 (beta/rc)

Katika MAF kabla ya 1.0.0, `OpenAIChatClient` ilitumia Chat Completions. Boresha kuwa `agent-framework-openai>=1.0.0` ambapo `OpenAIChatClient` hutumia Responses API kama chaguo-msingi.

> **Kumbuka**: `Agent`, `MCPStreamableHTTPTool`, na API nyingine za MAF hazijabadilika — tu mabadiliko ya kuingiza na kuanzisha darasa ya mteja.

## Uhamisho wa LangChain (`langchain-openai`)

Ongeza `use_responses_api=True` kwa `ChatOpenAI()`. Pia sasisha upatikanaji wa maudhui ya ujumbe kutoka `.content` hadi `.text`.

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

# ... mwito wa wakala ...
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

# ... kuitwa kwa wakala ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Mabadiliko muhimu**: (1) `use_responses_api=True` katika muanzishaji, (2) `.content` → `.text` kwa ujumbe wa majibu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->