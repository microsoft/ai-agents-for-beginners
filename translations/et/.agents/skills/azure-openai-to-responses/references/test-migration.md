# Testimistaristu migratsioon

Koodi baasi migreerimisel Chat Completions-ist Responses API-le, **testid purunevad prognoositaval viisil**. See juhend käsitleb, mida parandada.

---

## Streaming vastuste moki tegemine (Python pytest)

### Tuum moki klassid

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
            # Säilita tühik: lisa tühik kõigile sõnadele peale esimese
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

### Vastuste suunamine sõnumi sisu alusel

Tõelised rakendused pakuvad erinevaid vastuseid vastavalt promptile. Suuna `input` alusel (mitte `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API kasutab 'input', mitte 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatchi teed

| Kliendi tüüp | Monkeypatchi tee |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sünk) | `openai.resources.responses.Responses.create` |

> **Enne** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Pärast** (Responses): `openai.resources.responses.AsyncResponses.create`

### Täielik näide fikstiirist

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent ja AsyncResponseIterator klassid siin ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Uuenda moki fikstuurid

Asenda `ChatCompletionChunk` põhised mokid ülaltoodud `MockResponseEvent` / `AsyncResponseIterator` mustriga. Peamised muudatused:

| Enne (Chat Completions moki puhul) | Pärast (Responses moki puhul) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` tükk | `event.type == "response.completed"` |
| Azure-spetsiifiline `prompt_filter_results` tükk | Eemalda täielikult |
| Azure-spetsiifiline valiku kohta `content_filter_results` | Eemalda täielikult |
| `kwargs.get("messages")` mokis | `kwargs.get("input")` mokis |

---

## 2. Uuenda snapshot / golden faile

Kui testi komplekt kasutab snapshot testimist (nt `pytest-snapshot`, syrupy või käsitsi kirjutatud JSONL snapshots), muutub oodatud väljundi kuju:

**Enne** (Chat Completions voostav JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Pärast** (Responses API voostav JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Uus kuju on oluliselt lihtsam — puuduvad väljad `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` või `content_filter_results`. Uuenda või regenereeri kõik snapshot failid.

> **Vihje**: Käivita testid parameetriga `--snapshot-update` (pytest-snapshot) või `--update-snapshots` (syrupy) pärast migreerimist, et automaatselt uuendada.

---

## 3. Uuenda testi kinnitusi

Levinud kinnituste riknemised:

| Vana kinnitus | Probleem | Uus kinnitus |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI`-l puudub `_azure_ad_token_provider` atribuut | `isinstance(client, AsyncOpenAI)` ja `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI`-l puudub `api_version` | Eemalda täielikult |
| `isinstance(client, AsyncAzureOpenAI)` | Kliendi tüüp on muutunud | `isinstance(client, AsyncOpenAI)` |

---

## 4. Uuenda keskkonnamuutujad testi fikstuurides

Testid seadistavad tihti keskkonnamuutujaid kasutades `monkeypatch.setenv`. Uuenda neid:

| Vana keskkonnamuutuja | Uus keskkonnamuutuja | Märkused |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Standardne Azure Identity SDK konventsioon |
| `AZURE_OPENAI_VERSION` | Eemalda | Ei ole `api_version` enam vaja |
| `AZURE_OPENAI_API_VERSION` | Eemalda | Ei ole `api_version` enam vaja |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Hoia (vajalik jätkuvalt `base_url` jaoks) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Hoia (juurutuse nimi `model` argumendi jaoks) |

---

## 5. Otsi testikoodi, mis vajab migreerimist

```bash
# Testi-spetsiifilised pärandmustrid
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
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->