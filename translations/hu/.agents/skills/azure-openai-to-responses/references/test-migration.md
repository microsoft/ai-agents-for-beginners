# Teszt infrastruktúra átállítása

Amikor egy kódbázist a Chat Completions API-ról a Responses API-ra migrálsz, a **tesztek előre látható módon megszakadnak**. Ez a referencia bemutatja, hogy mit kell javítani.

---

## Streaming válaszok megtévesztő leképezése (Python pytest)

### Alapvető megtévesztő osztályok

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
            # Tartsd meg a szóközöket: szóközt szúrj be az összes szó elé az első kivételével
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

### Válaszok irányítása az üzenet tartalma alapján

A valós alkalmazások más választ adnak a prompt szerint. Irányítsd az `input` alapján (nem az `messages` alapján):

```python
async def mock_acreate(*args, **kwargs):
    # A válaszok API az 'input'-ot használja, nem a 'messages'-t
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch elérési utak

| Ügyféltípus | Monkeypatch elérési út |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (szinkron) | `openai.resources.responses.Responses.create` |

> **Előtte** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Utána** (Responses): `openai.resources.responses.AsyncResponses.create`

### Teljes fixture példa

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Itt találhatók a MockResponseEvent és AsyncResponseIterator osztályok ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Frissítsd a mock fixture-öket

Helyettesítsd a `ChatCompletionChunk` alapú mockokat a fentebb említett `MockResponseEvent` / `AsyncResponseIterator` mintával. Fontos változások:

| Előtte (Chat Completions mock) | Utána (Responses mock) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` a chunkban | `event.type == "response.completed"` |
| Azure-specifikus `prompt_filter_results` chunk | Teljesen eltávolítandó |
| Azure-specifikus `content_filter_results` minden választásnál | Teljesen eltávolítandó |
| `kwargs.get("messages")` a mockban | `kwargs.get("input")` a mockban |

---

## 2. Frissítsd a snapshot / golden fájlokat

Ha a tesztcsomag snapshot tesztelést használ (pl. `pytest-snapshot`, syrupy vagy kézzel írt JSONL snapshotokat), az elvárt kimenet formája megváltozik:

**Előtte** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Utána** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Az új forma drámaian egyszerűbb — nincs `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` vagy `content_filter_results` mező. Frissítsd vagy generáld újra az összes snapshot fájlt.

> **Tipp**: Tesztek futtatásához használd a `--snapshot-update` (pytest-snapshot) vagy `--update-snapshots` (syrupy) opciót az automatikus újrageneráláshoz migráció után.

---

## 3. Frissítsd a teszt feltételezéseket (assertion-öket)

Gyakori feltételezés törések:

| Régi feltételezés | Probléma | Új feltételezés |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | Az `AsyncOpenAI`-nek nincs `_azure_ad_token_provider` attribútuma | `isinstance(client, AsyncOpenAI)` és `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Nincs `api_version` az `OpenAI`/`AsyncOpenAI`-n | Teljesen eltávolítandó |
| `isinstance(client, AsyncAzureOpenAI)` | Ügyféltípus változott | `isinstance(client, AsyncOpenAI)` |

---

## 4. Frissítsd a környezeti változókat a teszt fixture-ökben

A tesztek gyakran állítanak be környezeti változókat `monkeypatch.setenv` segítségével. Ezeket frissítsd:

| Régi környezeti változó | Új környezeti változó | Megjegyzések |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Szabványos Azure Identity SDK konvenció |
| `AZURE_OPENAI_VERSION` | Eltávolítandó | Nincs szükség `api_version`-re |
| `AZURE_OPENAI_API_VERSION` | Eltávolítandó | Nincs szükség `api_version`-re |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Marad (továbbra is kell a `base_url`-hoz) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Marad (telepítés neve a `model` paraméterhez) |

---

## 5. Keresd meg a migrációt igénylő tesztkódokat

```bash
# Tesztre jellemző örökölt minták
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
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->