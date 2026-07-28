# Skrót API Responses (Python + Azure OpenAI)

> Wszystkie poniższe fragmenty zakładają `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` oraz że `client` jest już zainicjalizowany (patrz konfiguracja klienta).

## Podstawowe żądanie
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Konfiguracja klienta — EntraID (zalecane)
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

## Konfiguracja klienta — klucz API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Asynchroniczna konfiguracja klienta — EntraID
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

## Asynchroniczna konfiguracja klienta — EntraID z wyraźnym tenantem (multi-tenant)

Gdy zasób Azure OpenAI znajduje się w **innym tenantcie** niż domyślny, przekaż `tenant_id` jawnie do poświadczenia. Jest to typowe w scenariuszach dev/test, gdzie domowy tenant dewelopera różni się od tenant resource.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential do produkcji (Azure Container Apps, App Service itp.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # tożsamość zarządzana przypisana do użytkownika
)
# AzureDeveloperCliCredential dla lokalnego rozwoju — jawne tenant_id jest kluczowe
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Łańcuch: najpierw spróbuj tożsamości zarządzanej, w razie niepowodzenia użyj azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migracja asynchroniczna klienta — przed/po

Przed (przestarzałe):
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

## Pełna synchronizacja migracji — przed/po

Przed (legacy — Azure OpenAI Chat Completions):
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

Po (Responses API — punkt końcowy Azure OpenAI v1):
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

## Strumieniowanie (sync)
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
        print()  # nowa linia na końcu
```

## Strumieniowanie (async)
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

## Streaming aplikacji web — kształt backendu do frontend

Podczas migracji aplikacji web, która przesyła SSE/JSONL do frontendu, **format serializacji backendu** się zmienia. Zaprojektuj nowy output backendu tak, aby zachować istniejące wzorce dostępu frontendu, by frontend nie wymagał zmian.

**Przed** — backend Chat Completions zazwyczaj serializował słownik `choices[0]` każdego fragmentu:
```python
# Stare: seryjny pełny słownik wyborów na kawałek
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend czyta: `response.delta.content` (głęboka ścieżka w obiekcie choice).

**Po** — backend Responses API wysyła minimalny kształt zachowujący tę samą ścieżkę dostępu frontendu:
```python
# Nowość: emituj tylko to, czego potrzebuje frontend
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend nadal czyta `response.delta.content` — **brak zmian frontendowych**.

> **Kluczowa obserwacja**: Kształt strumieniowania Responses API (`event.type` + `event.delta`) jest zasadniczo inny niż Chat Completions (`chunk.choices[0].delta.content`). Ale kontrakt backend-to-frontend definiujesz Ty. Kształtuj output backendu tak, aby odpowiadał temu, czego oczekuje frontend.

## Sekwencja zdarzeń strumieniowania

Przy `stream: true`, API emituje zdarzenia w tej kolejności:
1. `response.created` – obiekt odpowiedzi zainicjalizowany
2. `response.in_progress` – rozpoczęcie generowania
3. `response.output_item.added` – utworzono pozycję outputu
4. `response.content_part.added` – rozpoczęto część zawartości
5. `response.output_text.delta` – fragmenty tekstu (wiele, każdy ma `delta: string`)
6. `response.output_text.done` – zakończenie generowania tekstu
7. `response.content_part.done` – zakończono część zawartości
8. `response.output_item.done` – zakończono pozycję outputu
9. `response.completed` – pełna odpowiedź zakończona

Dla podstawowego strumieniowania tekstu obsługuj tylko `response.output_text.delta` (fragmenty tekstu) i `response.completed` (zakończenie).

## Obsługa błędów strumieniowania w aplikacjach web

Podczas strumieniowania w aplikacji web owiń asynchroniczną iterację w `try/except` i zwracaj błędy jako JSON, aby frontend mógł je wyświetlić elegancko (np. limity żądań, przejściowe błędy):

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

> **Dlaczego to ważne**: Azure OpenAI zwraca `429 Too Many Requests` podczas ograniczania limitu. Bez `try/except` odpowiedź strumieniowa cichnie. Z nim frontend otrzymuje `{"error": "Too Many Requests"}` i może pokazać zapytanie o ponowną próbę.

## Typy zdarzeń strumieniowania (SDK Python)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Format konwersacji
```python
# API Odpowiedzi obsługuje format konwersacji za pomocą tablicy wejściowej
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

## Obsługa błędów filtra treści

Struktura ciała błędu zmieniła się z Chat Completions na Responses API.

Przed (Chat Completions):
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

Kluczowe różnice:
- Wrapper `innererror` **usunął się** — szczegóły filtra treści są teraz na najwyższym poziomie `error.body`.
- `content_filter_result` (pojedynczy) → `content_filters` (liczba mnoga tablica) zawierająca `content_filter_results` (liczba mnoga) w każdym wpisie.
- Każdy wpis w `content_filters` zawiera `blocked`, `source_type` i `content_filter_results` z detalami per kategoria (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Pełny kształt ciała błędu filtra treści Responses API:
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

## Surowa migracja HTTP (requests/httpx)

Jeśli aplikacja wywołuje bezpośrednio REST Azure OpenAI zamiast używać SDK:

Przed (Chat Completions):
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

> **Uwaga**: `output_text` to wygodna właściwość obiektu `Response` w Python SDK. Surowa odpowiedź JSON REST nie ma pola na najwyższym poziomie `output_text` — tekst znajduje się w `output[0].content[0].text`.

## Wieloetapowa konwersacja
```python
# Zbuduj rozmowę z użyciem Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Dodaj odpowiedź asystenta do rozmowy
messages.append({"role": "assistant", "content": response.output_text})

# Kontynuuj rozmowę
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Wieloetapowa konwersacja z typowaną treścią (jawne `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Wieloetapowa przez `previous_response_id` (alternatywa)

Zamiast samemu zarządzać tablicą konwersacji, możesz łączyć odpowiedzi
po stronie serwera za pomocą `previous_response_id`. API przechowuje każdą odpowiedź i
automatycznie dopisuje wcześniejsze kroki.

```python
# Pierwsza tura
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Kolejne tury — wystarczy przekazać nową wiadomość użytkownika + ID poprzedniej odpowiedzi
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Kiedy stosować które:**

| Podejście | Zalety | Wady |
|---|---|---|
| tablica `input` (ręczna) | Pełna kontrola nad historią; można przycinać/podsumowywać; brak potrzeby przechowywania po stronie serwera (`store=False`) | Więcej kodu; sam zarządzasz tablicą |
| `previous_response_id` | Prostszy kod; automatyczne łączenie | Wymaga `store=True` (domyślne); konwersacja przechowywana po stronie serwera; niemożność modyfikacji historii między krokami |

> **Uwaga migracyjna:** Większość aplikacji Chat Completions już zarządza własną tablicą wiadomości, dlatego konwersja na tablicę `input` jest bardziej bezpośrednią migracją 1:1. Używaj `previous_response_id` dla nowego kodu lub gdy nie potrzebujesz manipulować historią.

## Modele rozumujące serii O (o1, o3-mini, o3, o4-mini)

Modele serii O mają unikalne ograniczenia parametrów podczas migracji do Responses API.

### Mapowanie parametrów dla serii o

| Chat Completions (seria o) | Responses API | Uwagi |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Ustaw wysoko (4096+) — tokeny rozumowania liczą się do limitu |
| `reasoning_effort` | `reasoning.effort` | Zachowaj jak jest (low/medium/high), jeśli obecny |
| `temperature` | Usuń lub ustaw na `1` | Seria o akceptuje tylko wartość `1` |
| `top_p` | Usuń | Nieobsługiwane w serii o |
| `seed` | Usuń | Nieobsługiwane w Responses API |

### Seria o przed/po

Przed (Chat Completions z serią o):
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

> **Uwaga**: Modele serii o mogą buforować output podczas rozumowania przed emisją deltat tekstu. Strumieniowanie działa dalej, ale pierwsze zdarzenie `response.output_text.delta` może nadejść z większym opóźnieniem niż w modelach GPT.

## Dostęp do tokenów rozumowania
```python
# Modele rozumowania używają wewnętrznego rozumowania — możesz zobaczyć, ile tokenów rozumowania zostało użytych
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

> **Ważne**: Używaj `max_output_tokens=1000` (nie 50–200), aby uwzględnić wewnętrzny proces rozumowania modeli. Model używa tokenów rozumowania wewnętrznie przed wygenerowaniem finalnego outputu.

## Strukturalny output — JSON Schema
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

## Użycie narzędzi

- Definiuj funkcje w `tools` z **płaskim formatem Responses API** — `name`, `description` i `parameters` na najwyższym poziomie (nie zagnieżdżone pod `function`).
- Gdy model poprosi o wywołanie narzędzia, wykonaj je w swojej aplikacji i dołącz wynik narzędzia w kolejnym żądaniu jako element `function_call_output` w `input`.
- Utrzymuj schematy minimalne; waliduj wejścia przed wykonaniem.
- Przy użyciu `strict: true` wszystkie właściwości muszą być wymienione w `required` i wymagane jest `additionalProperties: false`.

> **⚠️ `pydantic_function_tool()` jest niekompatybilne**: Pomocnik `openai.pydantic_function_tool()` wciąż generuje stary zagnieżdżony format Chat Completions (`{"type": "function", "function": {"name": ...}}`). Nie używaj go z `responses.create()`. Definiuj schematy narzędzi ręcznie lub napisz wrapper spłaszczający output.

### Format definicji narzędzia

Responses API używa **płaskiego** formatu narzędzi — `name`, `description`, `parameters` to klucze na najwyższym poziomie (nie zagnieżdżone pod `function`).

**Przed (Chat Completions — zagnieżdżone):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Po (Responses API — płaskie):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Pełny przykład:
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

Z `strict: true` (wymuszanie schematu):
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
            "required": ["city_name"],       # Wszystkie właściwości MUSZĄ być wymienione
            "additionalProperties": False,   # Wymagane dla trybu ścisłego
        },
    }
]
```

### Wywołanie narzędzia — wykonanie i zwrócenie wyników

Gdy model prosi o wywołanie narzędzia, używaj elementów `response.output` + `function_call_output` — **nie** wzorca Chat Completions `role: assistant` + `role: tool`.

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
    # Dodaj elementy function_call modelu do rozmowy
    messages.extend(response.output)

    # Wykonaj każde narzędzie i dodaj wyniki
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Uzyskaj ostateczną odpowiedź z wynikami narzędzi
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Przykłady wywołań narzędzi few-shot

Podając few-shot przykłady wywołań narzędzi w `input`, używaj elementów `function_call` i `function_call_output`. ID muszą zaczynać się od `fc_`.

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
# Przykład wbudowanego wyszukiwania w sieci
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Wejście obrazu

Elementy zawartości obrazów zmieniają typ z `image_url` na `input_image`, a URL zmienia się z obiektu zagnieżdżonego na płaski string.

### Wejście obrazu — przed (Chat Completions)
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

### Wejście obrazu — po (Responses API, URL)
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

### Wejście obrazu — po (Responses API, base64)
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

> **Kluczowe zmiany**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (obiekt zagnieżdżony) → `"image_url": "..."` (płaski string — URL HTTPS lub `data:image/...;base64,...` URI danych), (3) `"type": "text"` → `"type": "input_text"`.

## Migracja Microsoft Agent Framework (MAF)

**Najpierw sprawdź swoją wersję MAF** — migracja zależy od tego, czy masz MAF 1.0.0+ czy przed-1.0.0 beta/rc.

Aby sprawdzić: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

W MAF 1.0.0+, `OpenAIChatClient` **już używa Responses API** — nie wymaga migracji.

Jeśli kod używa legacy `OpenAIChatCompletionClient` (który używa `chat.completions.create`), zamień go na `OpenAIChatClient`:

Przed:
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

### MAF przed-1.0.0 (wydania beta/rc)

W MAF przed 1.0.0 `OpenAIChatClient` używał Chat Completions. Zaktualizuj do `agent-framework-openai>=1.0.0`, gdzie `OpenAIChatClient` domyślnie używa Responses API.

> **Uwaga**: API `Agent`, `MCPStreamableHTTPTool` i inne pozostają bez zmian — zmienia się tylko import i instancja klienta.

## Migracja LangChain (`langchain-openai`)

Dodaj `use_responses_api=True` do `ChatOpenAI()`. Zaktualizuj też dostęp do treści wiadomości z `.content` na `.text`.

Przed:
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

# ... wywołanie agenta ...
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

# ... wywołanie agenta ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Kluczowe zmiany**: (1) `use_responses_api=True` w konstruktorze, (2) `.content` → `.text` w wiadomościach odpowiedzi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->