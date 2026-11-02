# Migración de Infraestructura de Pruebas

Al migrar una base de código de Chat Completions a Responses API, **las pruebas fallan de maneras predecibles**. Esta referencia cubre qué corregir.

---

## Simulación de Respuestas Streaming (Python pytest)

### Clases centrales de simulación

```python
class MockResponseEvent:
    """Simulates a Responses API streaming event."""
    def __init__(self, event_type: str, delta: str | None = None):
        self.type = event_type
        self.delta = delta

class AsyncResponseIterator:
    """Async iterator that yields Responses API streaming events from a string answer."""
    def __init__(self, answer: str):
        self.event_index = 0
        self.events = []
        for i, word in enumerate(answer.split(" ")):
            # Conservar el espacio en blanco: anteponer un espacio a todas las palabras excepto a la primera
            if i > 0:
                word = " " + word
            self.events.append(MockResponseEvent("response.output_text.delta", delta=word))
        self.events.append(MockResponseEvent("response.completed"))

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.event_index < len(self.events):
            event = self.events[self.event_index]
            self.event_index += 1
            return event
        raise StopAsyncIteration
```

### Dirigir respuestas simuladas según el contenido del mensaje

Las aplicaciones reales sirven diferentes respuestas según el aviso. Dirige por `input` (no por `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # La API de respuestas utiliza 'input' y no 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Rutas para monkeypatch

| Tipo de cliente | Ruta para monkeypatch |
|-----------------|----------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sincrónico) | `openai.resources.responses.Responses.create` |

> **Antes** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Después** (Responses): `openai.resources.responses.AsyncResponses.create`

### Ejemplo completo de fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Clases MockResponseEvent y AsyncResponseIterator aquí ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Actualizar fixtures de simulación

Reemplaza mocks basados en `ChatCompletionChunk` con el patrón `MockResponseEvent` / `AsyncResponseIterator` arriba. Cambios clave:

| Antes (mock de Chat Completions) | Después (mock de Responses) |
|---------------------------------|-----------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` en chunk | `event.type == "response.completed"` |
| Chunk específico de Azure `prompt_filter_results` | Remover completamente |
| `content_filter_results` por opción específico de Azure | Remover completamente |
| `kwargs.get("messages")` en mock | `kwargs.get("input")` en mock |

---

## 2. Actualizar snapshots / archivos golden

Si la suite de pruebas usa snapshot testing (ej., `pytest-snapshot`, syrupy, o snapshots JSONL caseros), cambia la forma de la salida esperada:

**Antes** (streaming JSONL de Chat Completions):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Después** (streaming JSONL de Responses API):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

La nueva forma es dramáticamente más simple — sin campos `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, o `content_filter_results`. Actualiza o regenera todos los archivos snapshot.

> **Consejo**: Ejecuta pruebas con `--snapshot-update` (pytest-snapshot) o `--update-snapshots` (syrupy) tras migrar para auto-regenerar.

---

## 3. Actualizar aserciones de pruebas

Fallos comunes en aserciones:

| Aserción antigua | Problema | Nueva aserción |
|-----------------|----------|----------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` no tiene atributo `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` y `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | No hay `api_version` en `OpenAI`/`AsyncOpenAI` | Remover completamente |
| `isinstance(client, AsyncAzureOpenAI)` | Cambió tipo de cliente | `isinstance(client, AsyncOpenAI)` |

---

## 4. Actualizar variables de entorno en fixtures de prueba

Las pruebas usualmente fijan variables env con `monkeypatch.setenv`. Actualiza estas:

| Variable de entorno antigua | Variable de entorno nueva | Notas |
|----------------------------|--------------------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Convención estándar del SDK de Identidad de Azure |
| `AZURE_OPENAI_VERSION` | Remover | No se necesita `api_version` |
| `AZURE_OPENAI_API_VERSION` | Remover | No se necesita `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Mantener (todavía necesario para `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Mantener (nombre del despliegue para parámetro `model`) |

---

## 5. Buscar código de prueba que necesite migración

```bash
# Patrones heredados específicos de la prueba
rg "ChatCompletionChunk" tests/
rg "AsyncCompletions\.create" tests/
rg "chat\.completions" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results" tests/
rg "content_filter_results" tests/
rg "AZURE_OPENAI_VERSION|AZURE_OPENAI_API_VERSION" tests/
rg "AZURE_OPENAI_CLIENT_ID" tests/
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->