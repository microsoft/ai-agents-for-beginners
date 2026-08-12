# Testinfrastruktur Migration

Når man migrerer en kodebase fra Chat Completions til Responses API, **brydes tests på forudsigelige måder**. Denne reference dækker hvad der skal rettes.

---

## Mocking Streaming Svar (Python pytest)

### Kerne mock klasser

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
            # Bevar mellemrum: tilføj mellemrum før alle ord undtagen det første
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

### Rute mock svar efter beskedindhold

Rigtige apps leverer forskellige svar baseret på prompten. Ruter efter `input` (ikke `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API bruger 'input' ikke 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch stier

| Klient type | Monkeypatch sti |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **Før** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Efter** (Responses): `openai.resources.responses.AsyncResponses.create`

### Fuld fixture eksempel

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent og AsyncResponseIterator klasser her ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Opdater mock fixtures

Erstat `ChatCompletionChunk`-baserede mocks med `MockResponseEvent` / `AsyncResponseIterator` mønsteret ovenfor. Vigtige ændringer:

| Før (Chat Completions mock) | Efter (Responses mock) |
|-----------------------------|-----------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` i chunk | `event.type == "response.completed"` |
| Azure-specifik `prompt_filter_results` chunk | Fjern helt |
| Azure-specifik `content_filter_results` per valg | Fjern helt |
| `kwargs.get("messages")` i mock | `kwargs.get("input")` i mock |

---

## 2. Opdater snapshot / golden filer

Hvis testsuiten bruger snapshot testing (f.eks. `pytest-snapshot`, syrupy, eller hjemmelavede JSONL snapshots), ændrer den forventede output-form:

**Før** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Efter** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Den nye form er markant simplere — ingen `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` eller `content_filter_results` felter. Opdater eller genskab alle snapshot filer.

> **Tip**: Kør tests med `--snapshot-update` (pytest-snapshot) eller `--update-snapshots` (syrupy) efter migration for automatisk genoprettelse.

---

## 3. Opdater test påstande

Almindelige påstandsfejl:

| Gammel påstand | Problem | Ny påstand |
|---------------|---------|------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` har ikke `_azure_ad_token_provider` attribut | `isinstance(client, AsyncOpenAI)` og `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Ingen `api_version` på `OpenAI`/`AsyncOpenAI` | Fjern helt |
| `isinstance(client, AsyncAzureOpenAI)` | Klient type ændret | `isinstance(client, AsyncOpenAI)` |

---

## 4. Opdater miljøvariabler i test fixtures

Tests sætter ofte miljøvariabler via `monkeypatch.setenv`. Opdater disse:

| Gammel env var | Ny env var | Noter |
|-------------|------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Standard Azure Identity SDK konvention |
| `AZURE_OPENAI_VERSION` | Fjern | Ingen `api_version` nødvendig |
| `AZURE_OPENAI_API_VERSION` | Fjern | Ingen `api_version` nødvendig |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Behold (stadig nødvendig for `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Behold (deployments navn for `model` param) |

---

## 5. Søg efter testkode der skal migreres

```bash
# Test-specifikke ældre mønstre
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
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->