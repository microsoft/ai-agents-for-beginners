# Responses API spikker (Python + Azure OpenAI)

> Kõik alljärgnevad näited eeldavad, et `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` ja `client` on juba initsialiseeritud (vt kliendi seadistust).

## Põhi päring
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Kliendi seadistamine — EntraID (soovitatav)
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

## Kliendi seadistamine — API võti
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Asünkroonne kliendi seadistamine — EntraID
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

## Asünkroonne kliendi seadistamine — EntraID koos otsese rentniku määramisega (multi-tenant)

Kui Azure OpenAI ressurss asub **teises rentnikus** kui vaikeväärtus, siis edasta `tenant_id` tunnistajale otseselt. See on tavaline arendus-/testimisscenario, kus arendaja kodu rentnik on erinev ressursi rentnikust.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential tootmiskeskkonnale (Azure Container Apps, App Service jne)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # kasutaja määratud hallatud identiteet
)
# AzureDeveloperCliCredential kohalikuks arenduseks — tenant_id on hädavajalik
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Ahel: kõigepealt proovige hallatud identiteeti, seejärel azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Asünkroonse kliendi migratsioon — enne/pärast

Enne (aegunud):
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

Pärast:
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

## Täis-sünkroon migratsioon — enne/pärast

Enne (pärand — Azure OpenAI Chat Completions):
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

Pärast (Responses API — Azure OpenAI v1 lõpp-punkt):
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

## Voogedastus (sünkroonne)
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
        print()  # reavahetus lõpus
```

## Voogedastus (asünkroonne)
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

## Veebirakenduse voogedastus — tagaotsast esiotsa kujundus

Veebirakenduse migreerimisel, mis voogedastab SSE/JSONL esiotsale, **tagaotsa serialiseerimisvorming** muutub. Kujunda uus tagaotsa väljund nii, et esiotsa juurdepääsupatternid säiliksid ja esiotsal ei oleks vaja muudatusi.

**Enne** — Chat Completions tagaots tavaliselt serialiseeris iga tüki `choices[0]` sõnastiku:
```python
# Vana: serialiseeritud täielik valikute sõnastik iga tükikese kohta
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Esiotsa lugemine: `response.delta.content` (sügav tee valiku objekti sees).

**Pärast** — Responses API tagaots output on minimaalne kuju, mis säilitab sama esiotsa juurdepääsu tee:
```python
# Uus: edastada ainult seda, mida frontend vajab
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Esiots loeb endiselt `response.delta.content` — **esiotsa muudatusi pole vaja**.

> **Oluline sisend**: Responses API voogedastuse kuju (`event.type` + `event.delta`) on algeliselt erinev Chat Completions’ist (`chunk.choices[0].delta.content`). Kuid tagaotsi ja esiotsa kokkulepe on sinu otsustada. Kujunda tagaotsa väljund vastavalt, mida esiots juba ootab.

## Voogedastuse sündmuse järjekord

Kui `stream: true`, API edastab sündmused selles järjekorras:
1. `response.created` – vastuse objekt initsialiseeritud
2. `response.in_progress` – genereerimine alanud
3. `response.output_item.added` – väljundi element loodud
4. `response.content_part.added` – sisutükk alustatud
5. `response.output_text.delta` – tekstilõigud (mitu, igaüks omab `delta: string`)
6. `response.output_text.done` – teksti genereerimine lõpetatud
7. `response.content_part.done` – sisutükk lõpetatud
8. `response.output_item.done` – väljundi element lõpetatud
9. `response.completed` – kogu vastus lõpetatud

Põhiteksti voogedastusel käsitle vaid `response.output_text.delta` (tekstitükkide jaoks) ja `response.completed` (lõpetuseks).

## Voogedastuse vigade haldamine veebirakendustes

Veebirakenduse voogedastuse puhul kasta asünkroonne iteratsioon `try/except` sisse ja anna vead JSON-formaadis edasi, et esiots saaks neid kenasti kuvada (nt päringupiirangud, ajutised tõrked):

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

> **Miks see oluline on**: Azure OpenAI tagastab päringupiirangu ajal `429 Too Many Requests` koodi. Ilma `try/except`-ita voogedastus lihtsalt katkevad vaikides. Sellega saab esiots `{"error": "Too Many Requests"}` ja kuvab kordamissoovi.

## Voogedastuse sündmuste tüübid (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Vestluse formaat
```python
# Responses API toetab vestlusvormingut sisendmassivi kaudu
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

## Sisufiltri vigade käsitlemine

Vigade keha struktuur muutus Chat Completionsist Responses API poolel.

Enne (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Pärast (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Peamised erinevused:
- `innererror` ümbris on **kadunud** — sisufiltri detailid on nüüd `error.body` peatasandil.
- `content_filter_result` (ainsus) → `content_filters` (mitmus massiiv) sisaldab igas kirjes `content_filter_results` (mitmus).
- Igas `content_filters` kirjes on `blocked`, `source_type` ja `content_filter_results` iga kategooria detailidega (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Täielik Responses API sisufiltri veakoodi keha kuju:
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

## Toores HTTP migratsioon (requests/httpx)

Kui rakendus kutsub Azure OpenAI REST otse SDK asemel:

Enne (Chat Completions):
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

Pärast (Responses API):
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

> **Märkus**: `output_text` on mugavusomadus Python SDK `Response` objektil. Toores REST JSON vastusel puudub tipp-tasemel `output_text` väli — tekst on `output[0].content[0].text`.

## Mitmevaatuseline vestlus
```python
# Koosta vestlus Responses API abil
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Lisa assistendi vastus vestlusse
messages.append({"role": "assistant", "content": response.output_text})

# Jätka vestlust
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Sisu tüübitud mitmevaatuseline (ekspliktiivne `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Mitmevaatuseline läbi `previous_response_id` (alternatiiv)

Oma vestluse massiivi haldamise asemel saad vastuseid serveripoolel ahelda
`previous_response_id` abil. API salvestab iga vastuse ja automaatselt lisab varasemad voorud ette.


```python
# Esimene voor
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Järgmised voorud — lihtsalt edasta uus kasutaja sõnum + eelmine vastuse ID
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Millal kasutada kumba:**

| Lähenemine | Eelised | Puudused |
|---|---|---|
| `input` massiiv (manuaalne) | Täielik kontroll ajaloo üle; saab lühendada/kokku võtta; serveripoolset salvestust ei vaja (`store=False`) | Rohkem koodi; sina haldad massiivi |
| `previous_response_id` | Lihtsam kood; automaatne aheldus | Vajab `store=True` (vaikimisi); vestlus salvestatakse serverisse; ei saa vahepeal ajaloo muuta |

> **Migreerimise märkus:** Enamik Chat Completions rakendusi haldab juba ise sõnumite massiivi, seega konverteerimine `input` massiiviks on otsene 1:1 migratsioon. Kasuta `previous_response_id` uuteks koodideks või kui ajalugu pole vaja muuta.

## O-seeria põhjendusmudelid (o1, o3-mini, o3, o4-mini)

O-seeria mudelitel on Responses API-le migratsioonil unikaalsed parameetripiirangud.

### Parameetrite kaardistus o-seeriale

| Chat Completions (o-seeria) | Responses API | Märkused |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | Määra kõrgeks (4096+) — arutluskäiguks kasutatud tokenid arvestatakse limiidi sisse |
| `reasoning_effort` | `reasoning.effort` | Säilita sama seisukohal kui olemas (madal/keskmine/kõrge) |
| `temperature` | Eemalda või määra `1` | O-seeria aktsepteerib ainult `1` |
| `top_p` | Eemalda | O-seerias ei toetata |
| `seed` | Eemalda | Responses API ei toeta |

### O-seeria enne/pärast

Enne (Chat Completions o-seeriaga):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Pärast (Responses API):
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

> **Märkus**: O-seeria mudelid võivad arutluse ajal väljundit vahemällu salvestada enne tekstimuudatuste väljastamist. Voogedastus töötab siiski, kuid esimene `response.output_text.delta` sündmus võib GPT mudelitega võrreldes hilineda.

## Arutluse tokenite kättesaamine
```python
# Järeldusmudelid kasutavad sisemist järeldamist — näete, mitu järeldussümbolit kasutati
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

> **Oluline**: Kasuta `max_output_tokens=1000` (mitte 50–200), et arvestada arutlusteenusega seotud mudeli sisemist arutlusprotsessi. Mudel kasutab sisemiselt arutluse tokeneid enne lõpliku väljundi genereerimist.

## Struktureeritud väljund — JSON skeem
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

## Tööriistade kasutamine

- Määra funktsioonid `tools` sees **Responses API lameda formaadi** järgi — `name`, `description` ja `parameters` on kõrgtasandi võtmed (ei ole pesastatud `function` alla).
- Kui mudel küsib tööriista kutsumist, täida see oma rakenduses ja lisa tööriista tulemus järgmise päringu `function_call_output` elemendina `input` sees.
- Hoia skeemid minimaalsed; valideeri sisendid enne täitmist.
- Kui kasutad `strict: true`, peavad kõik omadused olema välja toodud `required` sees ning `additionalProperties: false` on kohustuslik.

> **⚠️ `pydantic_function_tool()` on mittevastav**: `openai.pydantic_function_tool()` abi vahend genereerib endiselt vana Chat Completions pesastatud formaadi (`{"type": "function", "function": {"name": ...}}`). Ära kasuta seda koos `responses.create()`-ga. Määra tööriistade skeemid käsitsi või kirjuta ümbris väljundi lamedamaks muutmiseks.

### Tööriista defineerimise formaat

Responses API kasutab **lamedat** tööriista formaati — `name`, `description`, `parameters` on kõrgtasandi võtmed (ei ole pesastatud `function` alla).

**Enne (Chat Completions — pesastatud):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Pärast (Responses API — lame):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Täielik näide:
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

Kasutades `strict: true` (skeemi rakendamine):
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
            "required": ["city_name"],       # Kõik omadused PEAVAD olema loetletud
            "additionalProperties": False,   # Nõutud range režiimi jaoks
        },
    }
]
```

### Tööriistakutse ringkäik (täida ja tagasta tulemused)

Kui mudel nõuab tööriista kutsumist, kasuta `response.output` elemente + `function_call_output` — **mitte** Chat Completions `role: assistant` + `role: tool` mustrit.

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
    # Lisa mudeli function_call üksused vestlusse
    messages.extend(response.output)

    # Käivita iga tööriist ja lisa tulemused
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Hangi lõplik vastus koos tööriista tulemustega
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Mõned näited tööriistakutsetest väikeses mahus

Kui pakud `input` sees mõne proovinäite tööriistakutsetest, kasuta `function_call` ja `function_call_output` elemente. ID-d peavad algama `fc_`.

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
# Sisseehitatud veebipõhise otsingu näide
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Pildi sisend

Pildisisu elementide tüüp muutub `image_url`-st `input_image`-ks ja URL muutub pesastatud objektist lamedaks stringiks.

### Pildi sisend — enne (Chat Completions)
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

### Pildi sisend — pärast (Responses API, URL)
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

### Pildi sisend — pärast (Responses API, base64)
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

> **Olulised muudatused**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (pesastatud objekt) → `"image_url": "..."` (lame string — kas HTTPS URL või `data:image/...;base64,...` andmeURI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Frameworki (MAF) migratsioon

**Kontrolli esmalt oma MAF versiooni** — migratsioon sõltub sellest, kas oled MAF 1.0.0+ või eelversiooni (beta/rc) peal.

Kontrollimiseks: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ kasutab `OpenAIChatClient` **juba Responses API-t** — migratsiooni pole vaja.

Kui koodibaas kasutab vana `OpenAIChatCompletionClient` (mis kasutab `chat.completions.create`), asenda see `OpenAIChatClient`-ga:

Enne:
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

Pärast:
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

### MAF pre-1.0.0 (beta/rc väljaanded)

Pre-1.0.0 MAF-is kasutas `OpenAIChatClient` Chat Completions. Uuenda `agent-framework-openai>=1.0.0` peale, kus `OpenAIChatClient` kasutab vaikimisi Responses API-t.

> **Märkus**: `Agent`, `MCPStreamableHTTPTool` ja muud MAF API-d jäävad muutumatuks — muutub ainult kliendiklassi import ja instantsimine.

## LangChain (`langchain-openai`) migratsioon

Lisa `use_responses_api=True` `ChatOpenAI()` konstruktorisse. Värskenda ka sõnumi sisu ligipääsu `.content` asemel `.text` kasutamiseks.

Enne:
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

# ... agendi käivitamine ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Pärast:
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

# ... agendi kutsumine ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Olulisemad muudatused**: (1) `use_responses_api=True` konstruktoris, (2) `.content` → `.text` vastussõnumitel.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->