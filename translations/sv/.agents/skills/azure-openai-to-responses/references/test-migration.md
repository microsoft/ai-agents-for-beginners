# Migrering av testinfrastruktur

När man migrerar en kodbas från Chat Completions till Responses API bryts **tester på förutsägbara sätt**. Denna referens täcker vad som behöver åtgärdas.

---

## Mocka strömmande svar (Python pytest)

### Kärnmockklasser

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
            # Behåll mellanslag: lägg till ett mellanslag före alla ord utom det första
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

### Ranka mock-svar efter meddelandeinnehåll

Riktiga appar levererar olika svar beroende på prompten. Rankning efter `input` (inte `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API använder 'input' inte 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch-vägar

| Klienttyp | Monkeypatch-väg |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (synkron) | `openai.resources.responses.Responses.create` |

> **Före** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Efter** (Responses): `openai.resources.responses.AsyncResponses.create`

### Komplett fixture-exempel

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent och AsyncResponseIterator klasser här ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Uppdatera mock-fixturer

Ersätt `ChatCompletionChunk`-baserade mocks med mönstret `MockResponseEvent` / `AsyncResponseIterator` ovan. Viktiga ändringar:

| Före (Chat Completions mock) | Efter (Responses mock) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` i chunk | `event.type == "response.completed"` |
| Azure-specifik `prompt_filter_results`-chunk | Ta bort helt |
| Azure-specifik `content_filter_results` per val | Ta bort helt |
| `kwargs.get("messages")` i mock | `kwargs.get("input")` i mock |

---

## 2. Uppdatera snapshot- / golden-filer

Om testsviten använder snapshot-testning (t.ex. `pytest-snapshot`, syrupy, eller egenhändigt gjorda JSONL-snapshots) ändras den förväntade output-strukturen:

**Före** (Chat Completions strömmande JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Efter** (Responses API strömmande JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Den nya formen är dramatiskt enklare — inga `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` eller `content_filter_results`-fält. Uppdatera eller generera om alla snapshot-filer.

> **Tips**: Kör tester med `--snapshot-update` (pytest-snapshot) eller `--update-snapshots` (syrupy) efter migrering för att automatiskt uppdatera snapshots.

---

## 3. Uppdatera testassertioner

Vanliga orsaker till att assertioner bryts:

| Gammal assertion | Problem | Ny assertion |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` har inget `_azure_ad_token_provider`-attribut | `isinstance(client, AsyncOpenAI)` och `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Ingen `api_version` på `OpenAI`/`AsyncOpenAI` | Ta bort helt |
| `isinstance(client, AsyncAzureOpenAI)` | Klienttyp ändrad | `isinstance(client, AsyncOpenAI)` |

---

## 4. Uppdatera miljövariabler i test-fixturer

Tester sätter ofta miljövariabler via `monkeypatch.setenv`. Uppdatera dessa:

| Gammal env var | Ny env var | Noteringar |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Standard Azure Identity SDK-konvention |
| `AZURE_OPENAI_VERSION` | Ta bort | Ingen `api_version` behövs |
| `AZURE_OPENAI_API_VERSION` | Ta bort | Ingen `api_version` behövs |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Behåll (behövs fortfarande för `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Behåll (deploymentsnamn för `model`-param) |

---

## 5. Sök efter testkod som behöver migreras

```bash
# Test-specifika äldre mönster
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
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->