# Migrarea infrastructurii de testare

Când migrați o bază de cod de la Chat Completions la API-ul Responses, **teste se rup în moduri previzibile**. Această referință acoperă ce trebuie corectat.

---

## Mocking răspunsuri în streaming (Python pytest)

### Clase mock principale

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
            # Păstrează spațiile albe: adaugă un spațiu înaintea tuturor cuvintelor, cu excepția primului
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

Aplicațiile reale oferă răspunsuri diferite bazate pe prompt. Direcționați după `input` (nu `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # API-ul de răspunsuri folosește 'input', nu 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Căi pentru monkeypatch

| Tip client | Calea monkeypatch |
|-----------|--------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sincron) | `openai.resources.responses.Responses.create` |

> **Înainte** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **După** (Responses): `openai.resources.responses.AsyncResponses.create`

### Exemplu complet de fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Clasele MockResponseEvent și AsyncResponseIterator aici ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Actualizați fixture-urile mock

Înlocuiți mock-urile bazate pe `ChatCompletionChunk` cu modelul `MockResponseEvent` / `AsyncResponseIterator` de mai sus. Schimbările cheie:

| Înainte (mock Chat Completions) | După (mock Responses) |
|---------------------------------|-----------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` în chunk | `event.type == "response.completed"` |
| Chunk specific Azure `prompt_filter_results` | Se elimină complet |
| `content_filter_results` specific Azure per choice | Se elimină complet |
| `kwargs.get("messages")` în mock | `kwargs.get("input")` în mock |

---

## 2. Actualizați snapshot-urile / fișierele golden

Dacă suita de teste folosește teste de tip snapshot (ex., `pytest-snapshot`, syrupy sau snapshot-uri JSONL scrise manual), forma așteptată de output se schimbă:

**Înainte** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**După** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Noua formă este mult mai simplă — fără câmpuri `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` sau `content_filter_results`. Actualizați sau regenerați toate fișierele snapshot.

> **Sfat**: Rulați testele cu `--snapshot-update` (pytest-snapshot) sau `--update-snapshots` (syrupy) după migrare pentru a regenera automat.

---

## 3. Actualizați aserțiunile de test

Probleme comune în aserțiuni:

| Aserțiune veche | Problemă | Aserțiune nouă |
|---------------|----------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` nu are atribut `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` și `"/openai/v1/" în str(client.base_url)` |
| `client.api_version == "2024-..."` | Nu există `api_version` pe `OpenAI`/`AsyncOpenAI` | Se elimină complet |
| `isinstance(client, AsyncAzureOpenAI)` | Tip client schimbat | `isinstance(client, AsyncOpenAI)` |

---

## 4. Actualizați variabilele de mediu în fixture-urile de test

Testele adesea setează variabilele de mediu prin `monkeypatch.setenv`. Actualizați-le astfel:

| Variabilă mediu veche | Variabilă mediu nouă | Note |
|----------------------|---------------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Convenție standard Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Se elimină | Nu mai este necesară `api_version` |
| `AZURE_OPENAI_API_VERSION` | Se elimină | Nu mai este necesară `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Păstrați (încă necesar pentru `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Păstrați (numele deployment-ului pentru parametrul `model`) |

---

## 5. Căutați codul de test care are nevoie de migrare

```bash
# Modele vechi specifice testului
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