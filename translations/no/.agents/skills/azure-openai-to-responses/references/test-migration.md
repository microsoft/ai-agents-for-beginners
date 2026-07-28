# Migrering av testinfrastruktur

Når du migrerer en kodebase fra Chat Completions til Responses API, **brytes tester på forutsigbare måter**. Denne referansen dekker hva som må fikses.

---

## Mocking av strømmede svar (Python pytest)

### Kjerne mock-klasser

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
            # Behold hvite mellomrom: legg til mellomrom foran alle ord unntatt det første
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

### Ruteføring av mock-svar basert på meldingens innhold

Ekte apper leverer forskjellige svar basert på prompten. Rutefør etter `input` (ikke `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API bruker 'input' ikke 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch-stier

| Klienttype | Monkeypatch-sti |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (synkron) | `openai.resources.responses.Responses.create` |

> **Før** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Etter** (Responses): `openai.resources.responses.AsyncResponses.create`

### Fullt eksempel på fixture

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

## 1. Oppdater mock-fixtures

Erstatt `ChatCompletionChunk`-baserte mocks med `MockResponseEvent` / `AsyncResponseIterator`-mønsteret over. Viktige endringer:

| Før (Chat Completions mock) | Etter (Responses mock) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` i chunk | `event.type == "response.completed"` |
| Azure-spesifikk `prompt_filter_results` chunk | Fjern helt |
| Azure-spesifikk `content_filter_results` per valg | Fjern helt |
| `kwargs.get("messages")` i mock | `kwargs.get("input")` i mock |

---

## 2. Oppdater snapshot / golden-filer

Hvis testsuiten bruker snapshot-testing (f.eks. `pytest-snapshot`, syrupy, eller egendefinerte JSONL snapshots), endres den forventede utdataformen:

**Før** (Chat Completions strømmet JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Etter** (Responses API strømmet JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Den nye formen er dramatisk enklere — ingen `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, eller `content_filter_results` felter. Oppdater eller regenerer alle snapshot-filer.

> **Tips**: Kjør tester med `--snapshot-update` (pytest-snapshot) eller `--update-snapshots` (syrupy) etter migrering for automatisk regenerering.

---

## 3. Oppdater testassertasjoner

Vanlige brudd i assertasjoner:

| Gammel assertasjon | Problem | Ny assertasjon |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` har ikke `_azure_ad_token_provider` attributt | `isinstance(client, AsyncOpenAI)` og `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Ingen `api_version` på `OpenAI`/`AsyncOpenAI` | Fjern helt |
| `isinstance(client, AsyncAzureOpenAI)` | Klienttypen endret | `isinstance(client, AsyncOpenAI)` |

---

## 4. Oppdater miljøvariabler i test-fixtures

Tester setter ofte miljøvariabler via `monkeypatch.setenv`. Oppdater disse:

| Gammel miljøvariabel | Ny miljøvariabel | Notater |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Standard Azure Identity SDK-konvensjon |
| `AZURE_OPENAI_VERSION` | Fjern | Ingen `api_version` nødvendig |
| `AZURE_OPENAI_API_VERSION` | Fjern | Ingen `api_version` nødvendig |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Behold (fortsatt nødvendig for `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Behold (distribusjonsnavn for `model`-parameteren) |

---

## 5. Søk etter testkode som trenger migrering

```bash
# Testspesifikke eldre mønstre
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
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->