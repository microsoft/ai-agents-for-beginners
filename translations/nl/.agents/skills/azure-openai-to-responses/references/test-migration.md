# Testinfrastructuur Migratie

Bij het migreren van een codebasis van Chat Completions naar Responses API, **breken tests op voorspelbare manieren**. Deze referentie beschrijft wat er gerepareerd moet worden.

---

## Mocken van Streaming Responses (Python pytest)

### Kern mock klassen

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
            # Witruimte behouden: voeg een spatie toe voor alle woorden behalve het eerste
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

### Mock responses routeren op berichtinhoud

Echte apps geven verschillende antwoorden afhankelijk van de prompt. Routeren op `input` (niet `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API gebruikt 'input' niet 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch paden

| Client type | Monkeypatch pad |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **Voorheen** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Daarna** (Responses): `openai.resources.responses.AsyncResponses.create`

### Volledig fixture voorbeeld

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent en AsyncResponseIterator klassen hier ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Update mock fixtures

Vervang `ChatCompletionChunk`-gebaseerde mocks door het `MockResponseEvent` / `AsyncResponseIterator` patroon hierboven. Belangrijke wijzigingen:

| Voorheen (Chat Completions mock) | Daarna (Responses mock) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` in chunk | `event.type == "response.completed"` |
| Azure-specifieke `prompt_filter_results` chunk | Helemaal verwijderen |
| Azure-specifieke `content_filter_results` per keuze | Helemaal verwijderen |
| `kwargs.get("messages")` in mock | `kwargs.get("input")` in mock |

---

## 2. Update snapshot / golden files

Als de testsuite snapshot testing gebruikt (bijv. `pytest-snapshot`, syrupy, of zelfgemaakte JSONL snapshots), verandert de verwachte output structuur:

**Voorheen** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Daarna** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

De nieuwe structuur is veel eenvoudiger — geen `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, of `content_filter_results` velden. Werk alle snapshot bestanden bij of genereer opnieuw.

> **Tip**: Voer tests uit met `--snapshot-update` (pytest-snapshot) of `--update-snapshots` (syrupy) na migratie om automatisch te updaten.

---

## 3. Update test beweringen

Veelvoorkomende breukpunten in beweringen:

| Oude bewering | Probleem | Nieuwe bewering |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` heeft geen `_azure_ad_token_provider` attribuut | `isinstance(client, AsyncOpenAI)` en `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Geen `api_version` op `OpenAI`/`AsyncOpenAI` | Helemaal verwijderen |
| `isinstance(client, AsyncAzureOpenAI)` | Client type is veranderd | `isinstance(client, AsyncOpenAI)` |

---

## 4. Update omgevingsvariabelen in test fixtures

Tests zetten vaak env vars via `monkeypatch.setenv`. Werk deze bij:

| Oude env var | Nieuwe env var | Aantekeningen |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Standaard Azure Identity SDK conventie |
| `AZURE_OPENAI_VERSION` | Verwijderen | Geen `api_version` meer nodig |
| `AZURE_OPENAI_API_VERSION` | Verwijderen | Geen `api_version` meer nodig |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Blijven (nog steeds nodig voor `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Blijven (deployment naam voor `model` parameter) |

---

## 5. Zoek testcode die gemigreerd moet worden

```bash
# Testspecifieke legacy-patronen
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
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->