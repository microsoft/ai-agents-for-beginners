# Vastuste API kiirjuhend (Python + Azure OpenAI)

> Kõik alljärgnevad näited eeldavad, et `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` ja `client` on juba initsialiseeritud (vaata kliendi seadistust).

## Põhipäring
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

## Asünkroonne kliendi seadistamine — EntraID väljendusrikka rentniku (multi-tenant) korral

Kui Azure OpenAI ressurss on **teises rentnikus** kui vaikimisi, siis anna `tenant_id` mandaatidele selgesõnaliselt üle. See on tavaline arenduse/testimise olukordades, kus arendaja kodurentnik erineb ressursi rentnikust.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential tootmiseks (Azure Container Apps, App Service jne)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # kasutaja määratud hallatud identiteet
)
# AzureDeveloperCliCredential kohaliku arenduse jaoks — selge tenant_id on väga oluline
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Ahel: proovi esmalt hallatud identiteeti, vajadusel kasuta azd CLI-d
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

Enne (välistatud):
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

## Täis sünkroonse migratsioon — enne/pärast

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
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

Pärast (Vastuste API — Azure OpenAI v1 lõpp-punkt):
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

## Veebiäpi voogedastus — tagapõhjast esipaneelile kuju

Kui migreerid veebirakendust, mis voogedastab SSE/JSONL esipaneelile, muutub **tagapõhja serialiseerimisvorming**. Kujunda uus tagapõhja väljund nii, et esipaneeli olemasolevad pääsupunktid säiliksid, nii et esipaneel ei vajaks muudatusi.

**Enne** — Chat Completions tagapõhi serialiseeris tavaliselt iga tükki `choices[0]` sõnastiku:
```python
# Vananenud: iga osa kohta serialiseeritud täielik valiku sõnastik
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Esipaneel loeb: `response.delta.content` (sügav rada valiku objektis).

**Pärast** — Vastuste API tagapõhi väljastab minimaalse kujunduse, mis säilitab sama pääsupunkti esipaneelile:
```python
# Uus: väljastada ainult see, mida frontend vajab
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Esipaneel loeb endiselt `response.delta.content` — **esipaneeli muudatusi pole vaja**.

> **Oluline tähelepanek**: Vastuste API voogedastuse kuju (`event.type` + `event.delta`) on põhimõtteliselt erinev Chat Completions'ist (`chunk.choices[0].delta.content`). Aga sinu tagapõhja-esipaneeli leping on sinu loodav. Kujunda tagapõhja väljund sellele vastavaks, mida esipaneel juba ootab.

## Voogedastusürituste järjestus

Kui `stream: true`, API väljastab sündmused selles järjekorras:
1. `response.created` – vastuse objekt loodud
2. `response.in_progress` – genereerimine algas
3. `response.output_item.added` – väljundi ese loodud
4. `response.content_part.added` – sisuosa algas
5. `response.output_text.delta` – tekstitükid (mitu, igaühel omadus `delta: string`)
6. `response.output_text.done` – teksti genereerimine lõpetatud
7. `response.content_part.done` – sisuosa lõpetatud
8. `response.output_item.done` – väljundi ese lõpetatud
9. `response.completed` – kogu vastus täiesti valmis

Põhiteksti voogedastuseks käsitle ainult `response.output_text.delta` (tekstitükkide jaoks) ja `response.completed` (lõpuleviimiseks).

## Veebirakenduse voogedastuse vigade käsitlemine

Veebirakenduse voogedastamisel pane asünkroonne iteratsioon `try/except` plokki ja edasta vead JSON-ina, et esipaneel saaks need kenasti kuvada (nt päringupiirangud, ajutised tõrked):

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

> **Miks see oluline on**: Azure OpenAI tagastab päringupiirangu ajal koodi `429 Too Many Requests`. Ilma `try/except` plokita voogedastus katkeb vaikselt. Selle plokiga saab esipaneel `{"error": "Too Many Requests"}` ja võib kuvada kordusnupu.

## Voogedastussündmuste tüübid (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Vestluse formaat
```python
# Vastuste API toetab vestlusvormingut sisendmassivi kaudu
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

## Sisu filtri vigade käsitlemine

Vigade keha struktuur muutus Chat Completions’ist Vastuste API-le üle minnes.

Enne (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Pärast (Vastuste API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Peamised erinevused:
- `innererror` konteiner on **kadunud** — sisu filtri detailid on nüüd `error.body` ülemisel tasemel.
- `content_filter_result` (ainsus) → `content_filters` (mitmus, massiiv) sisaldab sees `content_filter_results` (mitmus) iga kirje kohta.
- Iga kirje `content_filters` sisaldab `blocked`, `source_type` ja `content_filter_results` koos kategooriapõhiste detailidega (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Täielik Vastuste API sisu filtri vigade keha kuju:
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

## Tavaline HTTP migratsioon (requests/httpx)

Kui rakendus kutsub Azure OpenAI REST otse ilma SDK-d kasutamata:

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

Pärast (Vastuste API):
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

> **Märkus**: `output_text` on mugavuse omadus Python SDK `Response` objektil. Toores REST JSON vastus ei oma ülemise taseme `output_text`-välja — tekst on `output[0].content[0].text`.

## Mitmekordne vestlus
```python
# Koosta vestlus Responses API-ga
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Lisa assistendi vastus vestlusele
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

Sisu-tüüpiline mitmekordne pööramine (selgelt määratletud `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Mitmekordne pööramine `previous_response_id` abil (alternatiiv)

Selle asemel, et hallata vestluse massiivi ise, saad reas serveripoolset vastuste
kettumist `previous_response_id`-ga. API salvestab iga vastuse ja
lisab automaatselt eelmised pöörded ettepoole.

```python
# Esimene käik
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Järgmised käigud — lihtsalt edasta uus kasutaja sõnum + eelmise vastuse ID
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Millal kasutada kumba:**

| Lähenemine | Plussid | Miinused |
|---|---|---|
| `input` massiiv (manuaalne) | Täielik kontroll ajaloo üle; saab kärpida/summariseerida; ei vaja serveripoolset salvestust (`store=False`) | Rohkem koodi; ise haldad massiivi |
| `previous_response_id` | Lihtsam kood; automaatne kettumine | Vajab `store=True` (vaikimisi); vestlus salvestatakse serveris; ei saa muuta ajaloo pöördeid |

> **Migratsioonimärkus:** Enamik Chat Completions rakendusi haldavad juba oma sõnumimassiivi, seega `input` massiivile üleminek on otsekohene 1:1 migratsioon. Kasuta `previous_response_id` uues koodis või kui vestluse ajaloo manipuleerimine pole vajalik.

## O-seeria loogika mudelid (o1, o3-mini, o3, o4-mini)

O-seeria mudelitel on unikaalsed parameetri piirangud vastuste API-le migratsioonil.

### Parameetrite seostamine o-seeriale

| Chat Completions (o-seeria) | Vastuste API | Märkused |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | Määra kõrgeks (4096+) — järeldamise tokenid loevad limiiti vastu |
| `reasoning_effort` | `reasoning.effort` | Hoia olemasolevana (low/medium/high) |
| `temperature` | Eemalda või määra `1` | O-seeria aktsepteerib ainult `1` |
| `top_p` | Eemalda | O-seerial pole toetatud |
| `seed` | Eemalda | Pole toetatud Responses API-s |

### O-seeria enne/pärast

Enne (Chat Completions koos o-seeriaga):
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

> **Märkus**: O-seeria mudelid võivad järeldamisel väljundit vahemälustada enne teksti deltakomponentide edastamist. Striimimine toimib endiselt, kuid esimene `response.output_text.delta` sündmus võib saabuda kauem hiljem kui GPT mudelite puhul.

## Järeldamistokenite kasutamine
```python
# Mõtlemismudelid kasutavad sisemist arutlust — näete, kui palju arutluse tokeneid kasutati
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

> **Oluline**: Kasuta `max_output_tokens=1000` (mitte 50–200) arvestamaks järeldusmudelite sisemist järeldamisprotsessi. Mudel kasutab järeldamistokeneid sisemiselt enne lõpliku väljundi genereerimist.

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

- Määra funktsioonid `tools` sees **flat Responses API formaadis** — `name`, `description` ja `parameters` on tipptasandi võtmed (mitte pesastatud `function` jaotisesse).
- Kui mudel palub tööriista kasutada, käivita see enda rakenduses ja lisa tööriista tulemus järgmisesse päringusse `function_call_output` üksusena `input` sees.
- Hoia skeemid minimaalsed; valideeri sisendid enne täitmist.
- Kui kasutad `strict: true`, peavad kõik omadused olema `required` all ja `additionalProperties: false` on kohustuslik.

> **⚠️ `pydantic_function_tool()` on ebakompatible**: `openai.pydantic_function_tool()` abistaja genereerib endiselt vana Chat Completions pesastatud formaadi (`{"type": "function", "function": {"name": ...}}`). Ära kasuta seda koos `responses.create()` meetodiga. Määra tööriista skeemid käsitsi või kirjuta wrapper väljundi lamestamiseks.

### Tööriista definitsiooni formaat

Responses API kasutab **flat** tööriistade formaati — `name`, `description`, `parameters` on tippkirjed (mitte `function` sees).

**Enne (Chat Completions — pesastatud):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Pärast (Responses API — flat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Täispikk näide:
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

Koos `strict: true` (skeemi nõudmine):
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
            "additionalProperties": False,   # Nõutud rangeks režiimiks
        },
    }
]
```

### Tööriistakutse ringkäik (täida ja tagasta tulemused)

Kui mudel palub tööriista kutsuda, kasuta `response.output` üksusi + `function_call_output` — **mitte** Chat Completions `role: assistant` + `role: tool` mustrit.

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

    # Hangi lõplik vastus tööriista tulemustega
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Mõne näidiska tööriistakutsete näited

Kui pakud tööriistakutsete mõne näidise `input` sees, kasuta `function_call` ja `function_call_output` üksusi. ID-d peavad algama `fc_`.

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
# Sisseehitatud veebiotsingu näide
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Pildi sisend

Pildisisu üksuste tüüp muutub `image_url`-lt `input_image`-ks ja URL muutub pesastatud objektist flat stringiks.

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

> **Olulised muudatused**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (pesastatud objekt) → `"image_url": "..."` (flat string — kas HTTPS URL või `data:image/...;base64,...` andme URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) migratsioon

**Kontrolli esmalt oma MAF versiooni** — migratsioon sõltub, kas kasutad MAF 1.0.0+ või eel-1.0.0 beta/rc versiooni.

Kontrollimiseks: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ versioonis kasutab `OpenAIChatClient` **juba Responses API-t** — migratsioon pole vajalik.

Kui koodibaas kasutab vana `OpenAIChatCompletionClient` (mis kasutab `chat.completions.create`), asenda see `OpenAIChatClient`:

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

### MAF pre-1.0.0 (beta/rc versioonid)

Vanemas kui 1.0.0 MAF-is kasutas `OpenAIChatClient` Chat Completionsit. Uuenda `agent-framework-openai>=1.0.0` peale, kus `OpenAIChatClient` kasutab vaikimisi Responses API-t.

> **Märkus**: `Agent`, `MCPStreamableHTTPTool` ja teised MAF API-d jäävad muutumatuks — ainult kliendiklassi import ja instantsi loomine muutuvad.

## LangChain (`langchain-openai`) migratsioon

Lisa `use_responses_api=True` `ChatOpenAI()` konstruktorisse. Uuenda ka sõnumite sisu ligipääs `.content` pealt `.text` peale.

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

# ... agendi väljakutse ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Olulised muudatused**: (1) `use_responses_api=True` konstruktoris, (2) `.content` → `.text` vastussõnumitel.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->