# Cheat Sheet API Risposte (Python + Azure OpenAI)

> Tutti gli snippet sottostanti assumono `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` e che `client` sia già inizializzato (vedi configurazione client).

## Richiesta base
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Configurazione client — EntraID (consigliato)
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

## Configurazione client — chiave API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Configurazione client Async — EntraID
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

## Configurazione client Async — EntraID con tenant esplicito (multi-tenant)

Quando la risorsa Azure OpenAI si trova in un **tenant diverso** da quello predefinito, passa `tenant_id` esplicitamente alla credenziale. Questo è comune in scenari di sviluppo/test in cui il tenant di origine dello sviluppatore è diverso dal tenant della risorsa.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential per la produzione (Azure Container Apps, App Service, ecc.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # identità gestita assegnata dall'utente
)
# AzureDeveloperCliCredential per lo sviluppo locale — tenant_id esplicito è fondamentale
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Catena: prova prima l'identità gestita, in caso contrario usa la CLI azd
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migrazione client Async — prima/dopo

Prima (deprecato):
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

Dopo:
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

## Migrazione completa sincronizzata — prima/dopo

Prima (legacy — Azure OpenAI Chat Completions):
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

Dopo (Responses API — endpoint Azure OpenAI v1):
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

## Streaming (sincrono)
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
        print()  # nuova riga alla fine
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

## Streaming web app — struttura backend-to-frontend

Durante la migrazione di una web app che fa streaming SSE/JSONL a un frontend, cambia il **formato di serializzazione del backend**. Progetta il nuovo output backend per preservare i pattern di accesso esistenti del frontend così da non richiedere modifiche al frontend.

**Prima** — Il backend di Chat Completions serializzava tipicamente il dizionario `choices[0]` di ogni chunk:
```python
# Vecchio: dizionario di scelta completa serializzato per chunk
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Lettura frontend: `response.delta.content` (percorso dettagliato nell'oggetto scelta).

**Dopo** — Il backend Responses API emette una forma minima preservando lo stesso percorso di accesso frontend:
```python
# Nuovo: emettere solo ciò di cui il frontend ha bisogno
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Il frontend continua a leggere `response.delta.content` — **non sono necessarie modifiche al frontend**.

> **Insight chiave**: La forma di streaming Responses API (`event.type` + `event.delta`) è fondamentalmente diversa da Chat Completions (`chunk.choices[0].delta.content`). Ma il contratto backend-to-frontend è a tua definizione. Scolpisci l'output backend per corrispondere a ciò che il frontend si aspetta già.

## Sequenza eventi streaming

Quando `stream: true`, l'API emette eventi in quest'ordine:
1. `response.created` – oggetto risposta inizializzato
2. `response.in_progress` – generazione avviata
3. `response.output_item.added` – elemento output creato
4. `response.content_part.added` – parte contenuto iniziata
5. `response.output_text.delta` – blocchi di testo (multipli, ognuno con `delta: string`)
6. `response.output_text.done` – generazione testo terminata
7. `response.content_part.done` – parte contenuto terminata
8. `response.output_item.done` – elemento output terminato
9. `response.completed` – risposta completa

Per streaming base di testo, gestisci solo `response.output_text.delta` (per blocchi di testo) e `response.completed` (per il termine).

## Gestione errori streaming nelle web app

Durante lo streaming in una web app, racchiudi l'iterazione async in `try/except` e emetti errori come JSON in modo che il frontend possa mostrarli in maniera elegante (es. limiti di rate, errori transitori):

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

> **Perché è importante**: Azure OpenAI ritorna `429 Too Many Requests` durante limitazioni di rate. Senza `try/except`, la risposta in streaming cade silenziosamente. Con esso, il frontend riceve `{"error": "Too Many Requests"}` e può mostrare un prompt per riprovare.

## Tipi eventi streaming (SDK Python)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Formato conversazione
```python
# L'API delle Risposte supporta il formato conversazione tramite array di input
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

## Gestione errori filtro contenuti

La struttura del corpo errore è cambiata da Chat Completions a Responses API.

Prima (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Dopo (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Differenze chiave:
- Il wrapper `innererror` è **sparito** — i dettagli del filtro contenuti sono ora a livello superiore in `error.body`.
- Da `content_filter_result` (singolare) a `content_filters` (array plurale) contenente `content_filter_results` (plurale) dentro ogni voce.
- Ogni voce in `content_filters` include `blocked`, `source_type`, e `content_filter_results` con dettagli per categoria (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Forma completa corpo errore filtro contenuti Responses API:
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

## Migrazione da HTTP raw (requests/httpx)

Se l'app chiama Azure OpenAI REST direttamente invece di usare l'SDK:

Prima (Chat Completions):
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

Dopo (Responses API):
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

> **Nota**: `output_text` è una proprietà di comodità sull'oggetto `Response` dell'SDK Python. La risposta REST JSON raw non ha un campo `output_text` a livello superiore — il testo è in `output[0].content[0].text`.

## Conversazione multi-turno
```python
# Costruisci una conversazione con l'API delle Risposte
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Aggiungi la risposta dell'assistente alla conversazione
messages.append({"role": "assistant", "content": response.output_text})

# Continua la conversazione
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Multi-turno con tipi contenuto (esplicito `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Multi-turno via `previous_response_id` (alternativa)

Invece di gestire l'array conversazione manualmente, puoi concatenare risposte
lato server usando `previous_response_id`. L'API memorizza ogni risposta e
premette automaticamente i turni precedenti.

```python
# Primo turno
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Turni successivi — basta passare il nuovo messaggio dell'utente + ID della risposta precedente
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Quando usare quale:**

| Approccio | Pro | Contro |
|---|---|---|
| Array `input` (manuale) | Controllo completo sulla cronologia; possibilità di rifilare/riassumere; nessuna memorizzazione lato server necessaria (`store=False`) | Più codice; gestisci tu l'array |
| `previous_response_id` | Codice più semplice; concatenazione automatica | Richiede `store=True` (default); conversazione memorizzata lato server; non puoi modificare la storia tra i turni |

> **Nota migrazione:** La maggior parte delle app Chat Completions già gestisce il proprio array messaggi, quindi la conversione a array `input` è una migrazione 1:1 più diretta. Usa `previous_response_id` per codice nuovo o quando non hai bisogno di manipolare la cronologia conversazione.

## Modelli di ragionamento serie O (o1, o3-mini, o3, o4-mini)

I modelli della serie O hanno vincoli unici di parametro nella migrazione alla Responses API.

### Mappatura parametri per serie O

| Chat Completions (serie O) | Responses API | Note |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Imposta alto (4096+) — i token di ragionamento sono conteggiati nel limite |
| `reasoning_effort` | `reasoning.effort` | Mantieni così se presente (low/medium/high) |
| `temperature` | Rimuovi o imposta a `1` | La serie O accetta solo `1` |
| `top_p` | Rimuovi | Non supportato sulla serie O |
| `seed` | Rimuovi | Non supportato nelle Responses API |

### Serie O prima/dopo

Prima (Chat Completions con serie O):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Dopo (Responses API):
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

> **Nota**: I modelli della serie O potrebbero bufferizzare l'output durante il ragionamento prima di emettere i delta di testo. Lo streaming funziona comunque ma il primo evento `response.output_text.delta` può arrivare con un ritardo maggiore rispetto ai modelli GPT.

## Accesso ai token di ragionamento
```python
# I modelli di ragionamento usano il ragionamento interno — puoi vedere quanti token di ragionamento sono stati usati
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

> **Importante**: Usa `max_output_tokens=1000` (non 50–200) per considerare il processo interno di ragionamento dei modelli. Il modello usa token di ragionamento internamente prima di generare l'output finale.

## Output strutturato — JSON Schema
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

## Uso degli strumenti

- Definisci le funzioni in `tools` con il **formato flat Responses API** — `name`, `description`, e `parameters` a livello superiore (non annidati sotto `function`).
- Quando il modello chiede di chiamare uno strumento, eseguilo nella tua app e includi il risultato dello strumento nella richiesta successiva come voce `function_call_output` dentro `input`.
- Mantieni gli schemi minimi; valida gli input prima dell'esecuzione.
- Quando usi `strict: true`, tutte le proprietà devono essere elencate in `required` e `additionalProperties: false` è obbligatorio.

> **⚠️ `pydantic_function_tool()` non è compatibile**: L'helper `openai.pydantic_function_tool()` genera ancora il vecchio formato annidato Chat Completions (`{"type": "function", "function": {"name": ...}}`). Non usarlo con `responses.create()`. Definisci manualmente gli schemi degli strumenti o scrivi un wrapper per appiattire l'output.

### Formato definizione strumenti

L'API Responses usa un formato strumento **flat** — `name`, `description`, `parameters` sono chiavi a livello superiore (non annidate sotto `function`).

**Prima (Chat Completions — annidato):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Dopo (Responses API — flat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Esempio completo:
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

Con `strict: true` (forzatura schema):
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
            "required": ["city_name"],       # Tutte le proprietà DEVONO essere elencate
            "additionalProperties": False,   # Richiesto per la modalità rigorosa
        },
    }
]
```

### Chiamata strumento round-trip (esegui e ritorna risultati)

Quando il modello richiede una chiamata strumento, usa gli elementi `response.output` + `function_call_output` — **non** il pattern Chat Completions `role: assistant` + `role: tool`.

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
    # Aggiungi gli elementi function_call del modello alla conversazione
    messages.extend(response.output)

    # Esegui ogni strumento e aggiungi i risultati
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Ottieni la risposta finale con i risultati degli strumenti
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Esempi few-shot di chiamate strumento

Quando fornisci esempi few-shot di chiamate strumento in `input`, usa gli elementi `function_call` e `function_call_output`. Gli ID devono iniziare con `fc_`.

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
# Esempio di ricerca web integrata
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Input immagine

Gli elementi di contenuto immagine cambiano tipo da `image_url` a `input_image`, e l'URL cambia da oggetto annidato a stringa flat.

### Input immagine — prima (Chat Completions)
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

### Input immagine — dopo (Responses API, URL)
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

### Input immagine — dopo (Responses API, base64)
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

> **Cambiamenti chiave**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (oggetto annidato) → `"image_url": "..."` (stringa flat — URL HTTPS o URI dati `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## Migrazione Microsoft Agent Framework (MAF)

**Controlla prima la tua versione MAF** — la migrazione dipende se sei su MAF 1.0.0+ o beta/rc pre-1.0.0.

Per controllare: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

In MAF 1.0.0+, `OpenAIChatClient` **usa già le Responses API** — nessuna migrazione necessaria.

Se il codice usa il legacy `OpenAIChatCompletionClient` (che usa `chat.completions.create`), sostituiscilo con `OpenAIChatClient`:

Prima:
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

Dopo:
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

### MAF pre-1.0.0 (beta/rc)

In MAF pre-1.0.0, `OpenAIChatClient` usava Chat Completions. Aggiorna a `agent-framework-openai>=1.0.0` dove `OpenAIChatClient` usa Responses API di default.

> **Nota**: Le API `Agent`, `MCPStreamableHTTPTool` e altre MAF restano invariate — cambia solo l'import e l'istanza della classe client.

## Migrazione LangChain (`langchain-openai`)

Aggiungi `use_responses_api=True` a `ChatOpenAI()`. Aggiorna anche l’accesso al contenuto messaggi da `.content` a `.text`.

Prima:
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

# ... invocazione dell'agente ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Dopo:
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

# ... invocazione dell'agente ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Cambiamenti chiave**: (1) `use_responses_api=True` nel costruttore, (2) `.content` → `.text` nei messaggi di risposta.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->