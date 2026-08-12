# Migracija testne infrastrukture

Pri migraciji kode iz Chat Completions na Responses API, **testi odpovejo na predvidljive načine**. Ta referenca zajema, kaj popraviti.

---

## Mockanje pretočnih odgovorov (Python pytest)

### Osnovne mock razrede

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
            # Ohranite presledke: pred vse besede razen prve dodajte presledek
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

### Usmerjanje mock odgovorov glede na vsebino sporočila

Resnični programi dajejo različne odgovore glede na poziv. Usmerjaj po `input` (ne `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # API za odgovore uporablja 'input', ne 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch poti

| Tip odjemalca | Monkeypatch pot |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sinhroni) | `openai.resources.responses.Responses.create` |

> **Pred** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Po** (Responses): `openai.resources.responses.AsyncResponses.create`

### Popoln primer fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Tukaj so razredi MockResponseEvent in AsyncResponseIterator ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Posodobitev mock fixture-ov

Zamenjajte mocke na osnovi `ChatCompletionChunk` z zgornjim vzorcem `MockResponseEvent` / `AsyncResponseIterator`. Ključne spremembe:

| Pred (mock Chat Completions) | Po (mock Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` v koščku | `event.type == "response.completed"` |
| Azure-specifični `prompt_filter_results` košček | Popolnoma odstranite |
| Azure-specifični `content_filter_results` za izbiro | Popolnoma odstranite |
| `kwargs.get("messages")` v mocku | `kwargs.get("input")` v mocku |

---

## 2. Posodobitev snapshot / zlatih datotek

Če testni paket uporablja snapshot testiranje (npr. `pytest-snapshot`, syrupy ali ročno narejene JSONL snapshote), se pričakovana oblika izhoda spremeni:

**Pred** (Chat Completions pretočni JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Po** (Responses API pretočni JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Nova oblika je bistveno enostavnejša — brez polj `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` ali `content_filter_results`. Posodobite ali regenerirajte vse snapshot datoteke.

> **Namig**: Po migraciji zaženite teste z `--snapshot-update` (pytest-snapshot) ali `--update-snapshots` (syrupy), da se snapshoti samodejno posodobijo.

---

## 3. Posodobitev testnih trditev

Pogoste napake pri trditvah:

| Stara trditev | Težava | Nova trditev |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` nima atributa `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` in `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Ni `api_version` na `OpenAI`/`AsyncOpenAI` | Odstranite popolnoma |
| `isinstance(client, AsyncAzureOpenAI)` | Tip odjemalca se je spremenil | `isinstance(client, AsyncOpenAI)` |

---

## 4. Posodobitev okoljskih spremenljivk v testnih fixture-ih

Testi pogosto nastavljajo okoljske spremenljivke preko `monkeypatch.setenv`. Posodobite jih:

| Stara okoljska spremenljivka | Nova okoljska spremenljivka | Opombe |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Standardna konvencija Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Odstranite | Ni potrebe po `api_version` |
| `AZURE_OPENAI_API_VERSION` | Odstranite | Ni potrebe po `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Ohranite (še vedno potrebno za `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Ohranite (ime nameščanja za `model` parameter) |

---

## 5. Poiščite testno kodo, ki potrebuje migracijo

```bash
# Dedni vzorci, specifični za testiranje
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
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->