# Hoja de trucos de Responses API (Python + Azure OpenAI)

> Todos los fragmentos a continuación asumen `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` y que el `client` ya está inicializado (ver configuración del cliente).

## Solicitud básica
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Configuración del cliente — EntraID (recomendado)
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

## Configuración del cliente — clave API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Configuración del cliente asíncrono — EntraID
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

## Configuración del cliente asíncrono — EntraID con tenant explícito (multi-tenant)

Cuando el recurso de Azure OpenAI está en un **tenant diferente** al predeterminado, pasa `tenant_id` explícitamente a la credencial. Esto es común en escenarios de desarrollo/prueba donde el tenant principal del desarrollador difiere del tenant del recurso.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential para producción (Azure Container Apps, App Service, etc.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # identidad administrada asignada por el usuario
)
# AzureDeveloperCliCredential para desarrollo local — tenant_id explícito es crítico
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Cadena: intentar identidad administrada primero, retroceder a la CLI azd
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migración asíncrona del cliente — antes/después

Antes (obsoleto):
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

Después:
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

## Migración completa sincronizada — antes/después

Antes (antiguo — Azure OpenAI Chat Completions):
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

Después (Responses API — endpoint Azure OpenAI v1):
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

## Transmisión (sincrónica)
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
        print()  # nueva línea al final
```

## Transmisión (asíncrona)
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

## Transmisión en app web — forma backend a frontend

Al migrar una app web que transmite SSE/JSONL a un frontend, el **formato de serialización del backend** cambia. Diseña la salida nueva del backend para preservar los patrones de acceso existentes del frontend para que no necesite cambios.

**Antes** — El backend de Chat Completions típicamente serializaba el diccionario `choices[0]` de cada fragmento:
```python
# Antiguo: diccionario de elección completo serializado por fragmento
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
La lectura del frontend es: `response.delta.content` (ruta profunda en el objeto choice).

**Después** — El backend de Responses API emite una forma mínima que preserva la misma ruta de acceso del frontend:
```python
# Nuevo: emitir solo lo que el frontend necesita
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
El frontend sigue leyendo `response.delta.content` — **no se necesitan cambios en el frontend**.

> **Insight clave**: La forma de transmisión de Responses API (`event.type` + `event.delta`) es fundamentalmente diferente a Chat Completions (`chunk.choices[0].delta.content`). Pero el contrato backend-frontend es definible por ti. Modela la salida del backend para que coincida con lo que el frontend ya espera.

## Secuencia de eventos de streaming

Cuando `stream: true`, la API emite eventos en este orden:
1. `response.created` – objeto de respuesta inicializado
2. `response.in_progress` – generación iniciada
3. `response.output_item.added` – elemento de salida creado
4. `response.content_part.added` – parte del contenido iniciada
5. `response.output_text.delta` – fragmentos de texto (múltiples, cada uno tiene `delta: string`)
6. `response.output_text.done` – generación de texto finalizada
7. `response.content_part.done` – parte del contenido finalizada
8. `response.output_item.done` – elemento de salida finalizado
9. `response.completed` – respuesta completa terminada

Para streaming de texto básico, solo maneja `response.output_text.delta` (para fragmentos de texto) y `response.completed` (para finalización).

## Manejo de errores en streaming en apps web

Al hacer streaming en una app web, envuelve la iteración asíncrona en `try/except` y emite errores como JSON para que el frontend los muestre de forma amigable (por ejemplo, límites de tasa, fallas transitorias):

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

> **Por qué es importante**: Azure OpenAI devuelve `429 Too Many Requests` durante límites de tasa. Sin el `try/except`, la respuesta en streaming muere silenciosamente. Con él, el frontend recibe `{"error": "Too Many Requests"}` y puede mostrar un mensaje de reintento.

## Tipos de eventos de streaming (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Formato de conversación
```python
# La API de Respuestas soporta el formato de conversación mediante un array de entrada
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

## Manejo de errores de filtro de contenido

La estructura del cuerpo de error cambió de Chat Completions a Responses API.

Antes (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Después (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Diferencias clave:
- El wrapper `innererror` **desapareció** — los detalles del filtro de contenido ahora están en el nivel superior de `error.body`.
- `content_filter_result` (singular) → `content_filters` (array plural) conteniendo `content_filter_results` (plural) dentro de cada entrada.
- Cada entrada en `content_filters` incluye `blocked`, `source_type` y `content_filter_results` con detalles por categoría (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Forma completa del cuerpo de error del filtro de contenido en Responses API:
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

## Migración HTTP cruda (requests/httpx)

Si la app llama a Azure OpenAI REST directamente en lugar de usar el SDK:

Antes (Chat Completions):
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

Después (Responses API):
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

> **Nota**: `output_text` es una propiedad de conveniencia en el objeto `Response` del SDK Python. La respuesta JSON REST cruda no tiene un campo superior `output_text` — el texto está en `output[0].content[0].text`.

## Conversación multi-turno
```python
# Construir una conversación con la API de Respuestas
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Agregar la respuesta del asistente a la conversación
messages.append({"role": "assistant", "content": response.output_text})

# Continuar la conversación
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Multi-turno con tipo de contenido (explicito `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Multi-turno vía `previous_response_id` (alternativa)

En lugar de gestionar el array de conversación tú mismo, puedes encadenar respuestas
en el servidor usando `previous_response_id`. La API almacena cada respuesta y
antepone automáticamente los turnos previos.

```python
# Primer turno
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Turnos posteriores: solo pasa el nuevo mensaje del usuario + ID de la respuesta anterior
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Cuándo usar cada uno:**

| Enfoque | Ventajas | Desventajas |
|---|---|---|
| Array `input` (manual) | Control total sobre el historial; puedes recortar/resumir; no se necesita almacenamiento en servidor (`store=False`) | Más código; tú gestionas el array |
| `previous_response_id` | Código más simple; encadenado automático | Requiere `store=True` (por defecto); conversación almacenada en servidor; no se puede modificar el historial entre turnos |

> **Nota de migración:** La mayoría de apps de Chat Completions ya gestionan su propio array de mensajes, por lo que convertir a array `input` es una migración 1:1 más directa. Usa `previous_response_id` para código nuevo o si no necesitas manipular el historial.

## Modelos de razonamiento serie O (o1, o3-mini, o3, o4-mini)

Los modelos de serie O tienen restricciones únicas de parámetros al migrar a Responses API.

### Mapeo de parámetros para serie o

| Chat Completions (serie o) | Responses API | Notas |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Establecer alto (4096+) — los tokens de razonamiento cuentan contra el límite |
| `reasoning_effort` | `reasoning.effort` | Mantener igual si está presente (bajo/medio/alto) |
| `temperature` | Eliminar o establecer en `1` | La serie O solo acepta `1` |
| `top_p` | Eliminar | No soportado en serie O |
| `seed` | Eliminar | No soportado en Responses API |

### Serie O antes/después

Antes (Chat Completions con serie o):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Después (Responses API):
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

> **Nota**: Los modelos de serie O pueden almacenar en búfer la salida durante el razonamiento antes de emitir deltas de texto. El streaming sigue funcionando pero el primer evento `response.output_text.delta` puede llegar con más retraso que con modelos GPT.

## Accediendo a tokens de razonamiento
```python
# Los modelos de razonamiento usan razonamiento interno — puedes ver cuántos tokens de razonamiento se usaron
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

> **Importante**: Usa `max_output_tokens=1000` (no 50–200) para tener en cuenta el proceso interno de razonamiento de los modelos. El modelo usa tokens de razonamiento internamente antes de generar la salida final.

## Salida estructurada — JSON Schema
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

## Uso de herramientas

- Define funciones en `tools` con el **formato plano Responses API** — `name`, `description` y `parameters` a nivel superior (no anidados bajo `function`).
- Cuando el modelo solicita llamar una herramienta, ejecútala en tu app e incluye el resultado de la herramienta en la siguiente solicitud como un item `function_call_output` dentro de `input`.
- Mantén los esquemas mínimos; valida entradas antes de ejecutar.
- Al usar `strict: true`, todas las propiedades deben estar listadas en `required` y `additionalProperties: false` es obligatorio.

> **⚠️ `pydantic_function_tool()` es incompatible**: El helper `openai.pydantic_function_tool()` aún genera el formato anidado antiguo de Chat Completions (`{"type": "function", "function": {"name": ...}}`). No lo uses con `responses.create()`. Define esquemas de herramienta manualmente o escribe un wrapper para aplanar la salida.

### Formato de definición de herramienta

La Responses API usa un formato de herramienta **plano** — `name`, `description`, `parameters` son claves a nivel superior (no anidadas bajo `function`).

**Antes (Chat Completions — anidado):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Después (Responses API — plano):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Ejemplo completo:
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

Con `strict: true` (aplicación de esquema):
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
            "required": ["city_name"],       # Todas las propiedades DEBEN estar listadas
            "additionalProperties": False,   # Requerido para modo estricto
        },
    }
]
```

### Ida y vuelta de llamada a herramienta (ejecutar y devolver resultados)

Cuando el modelo solicita llamada a herramienta, usa items `response.output` + `function_call_output` — **no** el patrón Chat Completions `role: assistant` + `role: tool`.

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
    # Añadir los elementos function_call del modelo a la conversación
    messages.extend(response.output)

    # Ejecutar cada herramienta y añadir los resultados
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Obtener la respuesta final con los resultados de las herramientas
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Ejemplos few-shot de llamadas a herramientas

Al proveer ejemplos few-shot de llamadas a herramientas en `input`, usa items `function_call` y `function_call_output`. Los IDs deben comenzar con `fc_`.

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
# Ejemplo incorporado de búsqueda web
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Entrada de imagen

Los items de contenido de imagen cambian de tipo `image_url` a `input_image`, y la URL cambia de un objeto anidado a una cadena plana.

### Entrada de imagen — antes (Chat Completions)
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

### Entrada de imagen — después (Responses API, URL)
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

### Entrada de imagen — después (Responses API, base64)
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

> **Cambios clave**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (objeto anidado) → `"image_url": "..."` (cadena plana — puede ser URL HTTPS o URI Data `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## Migración Microsoft Agent Framework (MAF)

**Verifica tu versión de MAF primero** — la migración depende de si estás en MAF 1.0.0+ o en beta/rc pre-1.0.0.

Para verificar: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

En MAF 1.0.0+, `OpenAIChatClient` **ya usa Responses API** — no se requiere migración.

Si el código usa el antiguo `OpenAIChatCompletionClient` (que usa `chat.completions.create`), reemplázalo por `OpenAIChatClient`:

Antes:
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

Después:
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

### MAF pre-1.0.0 (lanzamientos beta/rc)

En MAF pre-1.0.0, `OpenAIChatClient` usaba Chat Completions. Actualiza a `agent-framework-openai>=1.0.0` donde `OpenAIChatClient` usa Responses API por defecto.

> **Nota**: Las APIs `Agent`, `MCPStreamableHTTPTool` y otras de MAF permanecen sin cambios — solo cambian la importación y creación de instancia de la clase client.

## Migración LangChain (`langchain-openai`)

Agrega `use_responses_api=True` a `ChatOpenAI()`. También actualiza el acceso al contenido del mensaje de `.content` a `.text`.

Antes:
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

# ... invocación del agente ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Después:
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

# ... invocación del agente ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Cambios clave**: (1) `use_responses_api=True` en el constructor, (2) `.content` → `.text` en los mensajes de respuesta.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->