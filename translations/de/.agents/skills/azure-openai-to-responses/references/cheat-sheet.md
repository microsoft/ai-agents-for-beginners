# Responses API-Spickzettel (Python + Azure OpenAI)

> Alle Snippets unten setzen voraus, dass `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` und `client` bereits initialisiert ist (siehe Client-Setup).

## Grundlegende Anfrage
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Client-Setup — EntraID (empfohlen)
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

## Client-Setup — API-Schlüssel
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Asynchrones Client-Setup — EntraID
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

## Asynchrones Client-Setup — EntraID mit explizitem Mandanten (Multi-Tenant)

Wenn sich die Azure OpenAI-Ressource in einem **anderen Mandanten** als dem Standardmandanten befindet, geben Sie `tenant_id` explizit an die Credential weiter. Dies ist in Entwicklungs-/Test-Szenarien üblich, bei denen der Heimmandant des Entwicklers vom Ressourcenmandanten abweicht.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential für die Produktion (Azure Container Apps, App Service, etc.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # benutzerzugeordnete verwaltete Identität
)
# AzureDeveloperCliCredential für lokale Entwicklung — explizite tenant_id ist kritisch
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Kette: zuerst Managed Identity versuchen, bei Misserfolg auf azd CLI zurückgreifen
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Asynchroner Client-Migrationsvergleich — vorher/nachher

Vorher (veraltet):
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

Nachher:
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

## Vollständige synchrone Migration — vorher/nachher

Vorher (Legacy — Azure OpenAI Chat Completions):
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

Nachher (Responses API — Azure OpenAI v1-Endpunkt):
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
        print()  # Neue Zeile am Ende
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

## Web-App-Streaming — Backend-zu-Frontend-Struktur

Beim Migrieren einer Web-App, die SSE/JSONL an ein Frontend streamt, ändert sich das **Backend-Seriellformat**. Gestalten Sie die neue Backend-Ausgabe so, dass sie die bestehenden Zugriffswege im Frontend beibehält, damit das Frontend keine Änderungen benötigt.

**Vorher** — Chat Completions Backend hat typischerweise das `choices[0]`-Dictionary jedes Chunks serialisiert:
```python
# Alt: serialisiertes vollständiges Auswahl-Dict pro Chunk
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend liest: `response.delta.content` (tiefer Pfad im Choice-Objekt).

**Nachher** — Responses API Backend gibt eine minimale Struktur aus, die denselben Frontend-Zugriffspfad bewahrt:
```python
# Neu: Nur das ausgeben, was das Frontend benötigt
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend liest weiterhin `response.delta.content` — **keine Frontend-Änderungen erforderlich**.

> **Wichtige Erkenntnis**: Die Streaming-Struktur der Responses API (`event.type` + `event.delta`) unterscheidet sich grundlegend von Chat Completions (`chunk.choices[0].delta.content`). Aber Ihr Backend-zu-Frontend-Vertrag ist von Ihnen festlegbar. Formen Sie die Backend-Ausgabe so, dass sie dem entspricht, was das Frontend bereits erwartet.

## Reihenfolge der Streaming-Ereignisse

Wenn `stream: true`, gibt die API Ereignisse in folgender Reihenfolge aus:
1. `response.created` – Antwortobjekt initialisiert
2. `response.in_progress` – Generierung gestartet
3. `response.output_item.added` – Ausgabeelement erstellt
4. `response.content_part.added` – Inhaltsabschnitt gestartet
5. `response.output_text.delta` – Textabschnitte (mehrere, jeweils mit `delta: string`)
6. `response.output_text.done` – Textgenerierung beendet
7. `response.content_part.done` – Inhaltsabschnitt beendet
8. `response.output_item.done` – Ausgabeelement beendet
9. `response.completed` – gesamte Antwort abgeschlossen

Für einfaches Text-Streaming behandeln Sie nur `response.output_text.delta` (für Textabschnitte) und `response.completed` (für das Ende).

## Fehlerbehandlung beim Streaming in Web-Apps

Beim Streaming in einer Web-App umschließen Sie die asynchrone Iteration mit `try/except` und geben Fehler als JSON aus, damit das Frontend diese elegant anzeigen kann (z.B. Ratenbegrenzungen, temporäre Ausfälle):

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


> **Warum das wichtig ist**: Azure OpenAI gibt während der Rate-Limitierung `429 Too Many Requests` zurück. Ohne das `try/except` stirbt die Streaming-Antwort stillschweigend ab. Mit ihm erhält das Frontend `{"error": "Too Many Requests"}` und kann eine Wiederholungsaufforderung anzeigen.

## Streaming-Eventtypen (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Gesprächsformat
```python
# Die Responses-API unterstützt das Gesprächsformat über ein Eingabearray
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

## Behandlung von Content-Filter-Fehlern

Die Fehlerkörperstruktur hat sich von Chat Completions zur Responses API geändert.

Vorher (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Nachher (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Wichtige Unterschiede:
- Der `innererror` Wrapper ist **entfallen** — Details zum Content-Filter befinden sich jetzt auf der obersten Ebene von `error.body`.
- `content_filter_result` (Singular) → `content_filters` (Plural-Array), das `content_filter_results` (Plural) innerhalb jedes Eintrags enthält.
- Jeder Eintrag in `content_filters` enthält `blocked`, `source_type` und `content_filter_results` mit Details pro Kategorie (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Vollständige Struktur des Content-Filter-Fehlerkörpers der Responses API:
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

## Rohes HTTP-Migration (requests/httpx)

Wenn die App Azure OpenAI REST direkt anruft, statt das SDK zu verwenden:

Vorher (Chat Completions):
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

Nachher (Responses API):
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

> **Hinweis**: `output_text` ist eine Komfort-Eigenschaft des `Response`-Objekts im Python SDK. Die rohe REST-JSON-Antwort hat kein top-level Feld `output_text` — der Text befindet sich unter `output[0].content[0].text`.

## Mehrfach-Runden-Gespräche
```python
# Erstellen Sie ein Gespräch mit der Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Fügen Sie die Antwort des Assistenten zum Gespräch hinzu
messages.append({"role": "assistant", "content": response.output_text})

# Fahren Sie mit dem Gespräch fort
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Content-typed Mehrfach-Runden (explizit `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Mehrfach-Runden über `previous_response_id` (Alternative)

Statt das Gesprächsarray selbst zu verwalten, können Sie Antworten
serverseitig mit `previous_response_id` verketten. Die API speichert jede Antwort und
fügt automatisch vorherige Runden voran.

```python
# Erste Runde
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Folgende Runden — einfach die neue Benutzeranfrage + vorherige Antwort-ID übergeben
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Wann man welche Methode verwendet:**

| Ansatz | Vorteile | Nachteile |
|---|---|---|
| `input`-Array (manuell) | Volle Kontrolle über den Verlauf; kann gekürzt/zusammengefasst werden; keine serverseitige Speicherung nötig (`store=False`) | Mehr Code; Sie verwalten das Array |
| `previous_response_id` | Einfacherer Code; automatische Verkettung | Benötigt `store=True` (Standard); Gespräch wird serverseitig gespeichert; Verlauf lässt sich zwischen den Runden nicht ändern |

> **Migrationshinweis:** Die meisten Chat Completions Apps verwalten bereits ihr eigenes Nachrichtenarray, daher ist die Umstellung auf das `input`-Array eine direktere 1:1-Migration. Verwenden Sie `previous_response_id` für neuen Code oder wenn Sie den Gesprächsverlauf nicht manipulieren müssen.

## O-Serie Reasoning-Modelle (o1, o3-mini, o3, o4-mini)

O-Serie-Modelle haben bei der Migration zur Responses API einzigartige Parameterbeschränkungen.

### Parameterzuordnung für die O-Serie

| Chat Completions (O-Serie) | Responses API | Anmerkungen |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | Setze hoch (4096+) — Begründungs-Token zählen zum Limit |
| `reasoning_effort` | `reasoning.effort` | Bei Vorhandensein unverändert lassen (niedrig/mittel/hoch) |
| `temperature` | Entfernen oder auf `1` setzen | O-Serie akzeptiert nur `1` |
| `top_p` | Entfernen | Nicht unterstützt in der O-Serie |
| `seed` | Entfernen | Nicht unterstützt in der Responses API |

### O-Serie vorher/nachher

Vorher (Chat Completions mit O-Serie):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Nachher (Responses API):
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

> **Hinweis**: O-Serien-Modelle können die Ausgabe während des Begründungsvorgangs puffern, bevor Textdeltas ausgegeben werden. Streaming funktioniert weiterhin, aber das erste `response.output_text.delta`-Ereignis kann später eintreffen als bei GPT-Modellen.

## Zugriff auf Begründungs-Token
```python
# Schlussfolgerungsmodelle verwenden interne Schlussfolgerungen — Sie können sehen, wie viele Schlussfolgerungstokens verwendet wurden
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

> **Wichtig**: Verwenden Sie `max_output_tokens=1000` (nicht 50–200), um den internen Begründungsprozess der Modelle zu berücksichtigen. Das Modell verwendet intern Begründungs-Token, bevor es die finale Ausgabe generiert.

## Strukturierte Ausgabe — JSON-Schema
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

## Werkzeugnutzung

- Definieren Sie Funktionen in `tools` mit dem **flachen Responses API Format** — `name`, `description` und `parameters` auf oberster Ebene (nicht unter `function` verschachtelt).
- Wenn das Modell den Aufruf eines Werkzeugs anfordert, führen Sie es in Ihrer App aus und fügen Sie das Werkzeugergebnis im nächsten Request als `function_call_output`-Element innerhalb von `input` ein.
- Halten Sie Schemas minimal; validieren Sie Eingaben vor der Ausführung.
- Bei Verwendung von `strict: true` müssen alle Eigenschaften in `required` aufgelistet sein und `additionalProperties: false` ist obligatorisch.

> **⚠️ `pydantic_function_tool()` ist inkompatibel**: Der Helfer `openai.pydantic_function_tool()` generiert weiterhin das alte verschachtelte Chat Completions-Format (`{"type": "function", "function": {"name": ...}}`). Verwenden Sie es nicht mit `responses.create()`. Definieren Sie Werkzeugschemas manuell oder schreiben Sie einen Wrapper, um die Ausgabe zu glätten.

### Format der Werkzeugdefinition

Die Responses API verwendet ein **flaches** Werkzeugformat — `name`, `description`, `parameters` sind Schlüssel auf oberster Ebene (nicht unter `function` verschachtelt).

**Vorher (Chat Completions — verschachtelt):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Nachher (Responses API — flach):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Komplettes Beispiel:
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

Mit `strict: true` (Schema Erzwingung):
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
            "required": ["city_name"],       # Alle Eigenschaften MÜSSEN aufgelistet werden
            "additionalProperties": False,   # Erforderlich für den strengen Modus
        },
    }
]
```

### Werkzeugaufruf Rundreise (ausführen und Ergebnisse zurückgeben)

Wenn das Modell einen Werkzeugaufruf anfordert, verwenden Sie `response.output`-Elemente + `function_call_output` — **nicht** das Chat Completions `role: assistant` + `role: tool`-Muster.

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
    # Fügen Sie die function_call-Elemente des Modells zum Gespräch hinzu
    messages.extend(response.output)

    # Führen Sie jedes Tool aus und fügen Sie die Ergebnisse hinzu
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Holen Sie die endgültige Antwort mit den Tool-Ergebnissen ab
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Beispiele für Few-shot Werkzeugaufrufe

Wenn Sie Few-shot-Beispiele für Werkzeugaufrufe in `input` bereitstellen, verwenden Sie `function_call` und `function_call_output`-Elemente. IDs müssen mit `fc_` beginnen.

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
# Beispiel für integrierte Websuche
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Bildeingabe

Bildinhalte ändern den Typ von `image_url` zu `input_image` und die URL ändert sich von einem verschachtelten Objekt zu einem flachen String.

### Bildeingabe — vorher (Chat Completions)
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

### Bildeingabe — nachher (Responses API, URL)
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

### Bildeingabe — nachher (Responses API, base64)
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

> **Wesentliche Änderungen**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (verschachteltes Objekt) → `"image_url": "..."` (flacher String — entweder HTTPS-URL oder `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Migration des Microsoft Agent Framework (MAF)

**Überprüfen Sie zuerst Ihre MAF-Version** — die Migration hängt davon ab, ob Sie MAF 1.0.0+ oder eine Pre-1.0.0 Beta/RC verwenden.

Zur Überprüfung: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

In MAF 1.0.0+ verwendet `OpenAIChatClient` **bereits die Responses API** — keine Migration erforderlich.

Wenn der Code die veraltete `OpenAIChatCompletionClient` (die `chat.completions.create` verwendet) nutzt, ersetzen Sie sie durch `OpenAIChatClient`:

Vorher:
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

Nachher:
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

### MAF vor 1.0.0 (Beta/RC-Versionen)

In MAF vor 1.0.0 verwendete `OpenAIChatClient` Chat Completions. Aktualisieren Sie auf `agent-framework-openai>=1.0.0`, wo `OpenAIChatClient` standardmäßig die Responses API nutzt.

> **Hinweis**: Die APIs `Agent`, `MCPStreamableHTTPTool` und weitere von MAF bleiben unverändert – nur der Import und die Instanziierung der Client-Klasse ändern sich.

## LangChain (`langchain-openai`) Migration

Fügen Sie `use_responses_api=True` zu `ChatOpenAI()` hinzu. Aktualisieren Sie außerdem den Zugriff auf Nachrichteninhalte von `.content` auf `.text`.

Vorher:
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

# ... Agentenaufruf ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Nachher:
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

# ... Agentenaufruf ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Wesentliche Änderungen**: (1) `use_responses_api=True` im Konstruktor, (2) `.content` → `.text` bei Antwortnachrichten.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->