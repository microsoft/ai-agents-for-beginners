# Migrarea infrastructurii de testare

Când se migrează o bază de cod de la Chat Completions la Responses API, **teste se rup în moduri previzibile**. Această referință acoperă ce trebuie corectat.

---

## Mocking răspunsurilor streaming (Python pytest)

### Clase mock de bază

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
            # Preserve whitespace: prepend space to all words except the first
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

### Direcționarea răspunsurilor mock după conținutul mesajului

Aplicațiile reale oferă răspunsuri diferite bazate pe solicitare. Direcționează după `input` (nu `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API uses 'input' not 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch căi

| Tip client | Cale monkeypatch |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **Înainte** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **După** (Responses): `openai.resources.responses.AsyncResponses.create`

### Exemplu complet fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent and AsyncResponseIterator classes here ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Actualizează fixture-urile mock

Înlocuiește mock-urile bazate pe `ChatCompletionChunk` cu modelul `MockResponseEvent` / `AsyncResponseIterator` de mai sus. Schimbări cheie:

| Înainte (mock Chat Completions) | După (mock Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` în chunk | `event.type == "response.completed"` |
| Chunk `prompt_filter_results` specific Azure | Elimină complet |
| `content_filter_results` per alegere specific Azure | Elimină complet |
| `kwargs.get("messages")` în mock | `kwargs.get("input")` în mock |

---

## 2. Actualizează snapshot-urile / fișierele golden

Dacă suita de testare utilizează testarea cu snapshot-uri (de exemplu, `pytest-snapshot`, syrupy, sau snapshot-uri JSONL făcute manual), forma output-ului așteptat se schimbă:

**Înainte** (streaming JSONL Chat Completions):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**După** (streaming JSONL Responses API):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Noua formă este mult mai simplă — fără câmpuri `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, sau `content_filter_results`. Actualizează sau regenerează toate fișierele snapshot.

> **Sfat**: Rulează testele cu `--snapshot-update` (pytest-snapshot) sau `--update-snapshots` (syrupy) după migrare pentru regenereare automată.

---

## 3. Actualizează afirmațiile din teste

Problema comună a afirmațiilor sparte:

| Afirmație veche | Problemă | Afirmație nouă |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` nu are atributul `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` și `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Nu există `api_version` pe `OpenAI`/`AsyncOpenAI` | Elimină complet |
| `isinstance(client, AsyncAzureOpenAI)` | Tip client schimbat | `isinstance(client, AsyncOpenAI)` |

---

## 4. Actualizează variabilele de mediu în fixture-urile de test

Testele setează deseori variabile de mediu prin `monkeypatch.setenv`. Actualizează acestea:

| Variabilă mediu veche | Variabilă mediu nouă | Note |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Convenție standard SDK Azure Identity |
| `AZURE_OPENAI_VERSION` | Elimină | Nu mai este nevoie de `api_version` |
| `AZURE_OPENAI_API_VERSION` | Elimină | Nu mai este nevoie de `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Păstrează (încă necesar pentru `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Păstrează (numele deploymentului pentru parametrul `model`) |

---

## 5. Caută codul de testare care trebuie migrat

```bash
# Test-specific legacy patterns
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
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->