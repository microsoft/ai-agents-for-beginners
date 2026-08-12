# Migracja infrastruktury testowej

Podczas migracji bazy kodu z Chat Completions do Responses API **testy psują się w przewidywalny sposób**. Ten przewodnik opisuje, co naprawić.

---

## Mockowanie odpowiedzi strumieniowych (Python pytest)

### Główne klasy mockujące

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
            # Zachowaj odstępy: dodaj spację przed wszystkimi słowami oprócz pierwszego
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

### Kierowanie mockowanych odpowiedzi według treści wiadomości

Prawdziwe aplikacje zwracają różne odpowiedzi w zależności od promptu. Kieruj według `input` (nie `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # API odpowiedzi używa 'input', nie 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Ścieżki do monkeypatchingu

| Typ klienta | Ścieżka monkeypatch |
|-------------|---------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (synchroniczny) | `openai.resources.responses.Responses.create` |

> **Przed** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Po** (Responses): `openai.resources.responses.AsyncResponses.create`

### Pełny przykład fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Klasy MockResponseEvent i AsyncResponseIterator tutaj ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Zaktualizuj mocki testowe

Zastąp mocki oparte na `ChatCompletionChunk` wzorcem `MockResponseEvent` / `AsyncResponseIterator` powyżej. Kluczowe zmiany:

| Przed (mock Chat Completions) | Po (mock Responses) |
|-------------------------------|--------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` w chunku | `event.type == "response.completed"` |
| Chunk `prompt_filter_results` specyficzny dla Azure | Usuń całkowicie |
| `content_filter_results` na opcję, specyficzne dla Azure | Usuń całkowicie |
| `kwargs.get("messages")` w mocku | `kwargs.get("input")` w mocku |

---

## 2. Zaktualizuj pliki snapshot / golden

Jeśli w zestawie testowym używasz testowania snapshotów (np. `pytest-snapshot`, syrupy lub własnych snapshotów JSONL), kształt oczekiwanych wyników się zmienia:

**Przed** (strumieniowy JSONL Chat Completions):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Po** (strumieniowy JSONL Responses API):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Nowy format jest znacznie prostszy — brak pól `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` czy `content_filter_results`. Zaktualizuj lub wygeneruj ponownie wszystkie pliki snapshot.

> **Wskazówka**: Uruchom testy z `--snapshot-update` (pytest-snapshot) lub `--update-snapshots` (syrupy) po migracji, aby automatycznie odświeżyć snapshoty.

---

## 3. Zaktualizuj asercje testowe

Najczęstsze problemy z asercjami:

| Stara asercja | Problem | Nowa asercja |
|--------------|---------|------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` nie ma atrybutu `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` oraz `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Brak `api_version` w `OpenAI`/`AsyncOpenAI` | Usuń całkowicie |
| `isinstance(client, AsyncAzureOpenAI)` | Zmiana typu klienta | `isinstance(client, AsyncOpenAI)` |

---

## 4. Zaktualizuj zmienne środowiskowe w fixture testowych

Testy często ustawiają zmienne środowiskowe przez `monkeypatch.setenv`. Zaktualizuj je:

| Stara zmienna | Nowa zmienna | Uwagi |
|--------------|-------------|--------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Standardowa konwencja Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Usuń | Niepotrzebne `api_version` |
| `AZURE_OPENAI_API_VERSION` | Usuń | Niepotrzebne `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Zachowaj (wciąż potrzebne dla `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Zachowaj (nazwa deploymentu dla parametru `model`) |

---

## 5. Wyszukaj kod testowy, który wymaga migracji

```bash
# Wzorce dziedzictwa specyficzne dla testów
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
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->