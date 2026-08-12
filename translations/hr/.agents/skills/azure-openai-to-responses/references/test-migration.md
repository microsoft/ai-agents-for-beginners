# Migracija testne infrastrukture

Prilikom migracije kôdne baze s Chat Completions na Responses API, **testovi se kvare na predvidljive načine**. Ovaj referentni dokument pokriva što treba popraviti.

---

## Mockiranje streaming odgovora (Python pytest)

### Osnovne mock klase

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
            # Sačuvajte razmake: dodajte razmak ispred svih riječi osim prve
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

### Usmjeravanje mock odgovora prema sadržaju poruke

Stvarne aplikacije daju različite odgovore na temelju prompta. Usmjeravajte prema `input` (ne `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API koristi 'input', a ne 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Putanje za monkeypatch

| Tip klijenta | Putanja za monkeypatch |
|-------------|-----------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sinkroni) | `openai.resources.responses.Responses.create` |

> **Prije** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Nakon** (Responses): `openai.resources.responses.AsyncResponses.create`

### Potpuni primjer fixturea

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Ovdje su klase MockResponseEvent i AsyncResponseIterator ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Ažurirajte mock fixturee

Zamijenite mockove bazirane na `ChatCompletionChunk` s uzorkom `MockResponseEvent` / `AsyncResponseIterator` iznad. Ključne promjene:

| Prije (Chat Completions mock) | Nakon (Responses mock) |
|-------------------------------|-----------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` u chunku | `event.type == "response.completed"` |
| Chunk specifičan za Azure `prompt_filter_results` | Uklonite u potpunosti |
| Po izboru specifičan za Azure `content_filter_results` | Uklonite u potpunosti |
| `kwargs.get("messages")` u mocku | `kwargs.get("input")` u mocku |

---

## 2. Ažurirajte snapshot / zlatne datoteke

Ako test suite koristi snapshot testiranje (npr., `pytest-snapshot`, syrupy ili ručno rađene JSONL snapshotove), očekivani oblik izlaza se mijenja:

**Prije** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Nakon** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Novi oblik je drastično jednostavniji — bez polja `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` ili `content_filter_results`. Ažurirajte ili regenerirajte sve snapshot datoteke.

> **Savjet**: Pokrenite testove s `--snapshot-update` (pytest-snapshot) ili `--update-snapshots` (syrupy) nakon migracije da se automatski regeneriraju.

---

## 3. Ažurirajte testne tvrdnje

Česti razlozi pada tvrdnji:

| Stara tvrdnja | Problem | Nova tvrdnja |
|--------------|---------|-------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` nema atribut `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` i `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Nema `api_version` na `OpenAI`/`AsyncOpenAI` | Uklonite u potpunosti |
| `isinstance(client, AsyncAzureOpenAI)` | Tip klijenta se promijenio | `isinstance(client, AsyncOpenAI)` |

---

## 4. Ažurirajte varijable okoline u testnim fixtureima

Testovi često postavljaju varijable okoline putem `monkeypatch.setenv`. Ažurirajte ih:

| Stara varijabla | Nova varijabla | Napomene |
|-------------|--------------|---------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Standardna konvencija Azure Identity SDK-a |
| `AZURE_OPENAI_VERSION` | Uklonite | Nije potrebna `api_version` |
| `AZURE_OPENAI_API_VERSION` | Uklonite | Nije potrebna `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Zadržati (još uvijek potrebno za `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Zadržati (ime deploymenta za parametar `model`) |

---

## 5. Potražite testni kôd koji treba migrirati

```bash
# Naslijeđeni obrasci specifični za testiranje
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
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->