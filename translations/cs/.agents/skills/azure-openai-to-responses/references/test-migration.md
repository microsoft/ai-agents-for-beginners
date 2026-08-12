# Migrace testovací infrastruktury

Při migraci kódu z Chat Completions na Responses API **testy selhávají předvídatelnými způsoby**. Tento referenční dokument popisuje, co je potřeba opravit.

---

## Mockování streamovaných odpovědí (Python pytest)

### Základní mock třídy

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
            # Zachovat mezery: přidat mezeru před všechna slova kromě prvního
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

### Přesměrování mock odpovědí podle obsahu zprávy

Skutečné aplikace poskytují různé odpovědi na základě promptu. Přesměrujte podle `input` (nikoli `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # API odpovědí používá 'input' nikoli 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Cesty pro monkeypatch

| Typ klienta | Cesta pro monkeypatch |
|-------------|----------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **Předtím** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Poté** (Responses): `openai.resources.responses.AsyncResponses.create`

### Kompletní příklad fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Třídy MockResponseEvent a AsyncResponseIterator zde ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Aktualizujte mock fixture

Nahraďte mocky založené na `ChatCompletionChunk` vzorem `MockResponseEvent` / `AsyncResponseIterator` výše. Klíčové změny:

| Předtím (mock Chat Completions) | Poté (mock Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` v chunku | `event.type == "response.completed"` |
| Azure-specifický chunk `prompt_filter_results` | Odstranit úplně |
| Azure-specifický `content_filter_results` na každou volbu | Odstranit úplně |
| `kwargs.get("messages")` v mocku | `kwargs.get("input")` v mocku |

---

## 2. Aktualizujte snapshot / golden soubory

Pokud testovací sada používá snapshot testování (např. `pytest-snapshot`, syrupy nebo ručně vytvořené JSONL snapshoty), očekávaný tvar výstupu se mění:

**Předtím** (Chat Completions streamované JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Poté** (Responses API streamované JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Nový tvar je výrazně jednodušší — žádná pole `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` ani `content_filter_results`. Aktualizujte nebo znovu vygenerujte všechny snapshot soubory.

> **Tip**: Po migraci spusťte testy s `--snapshot-update` (pytest-snapshot) nebo `--update-snapshots` (syrupy) pro automatickou obnovu.

---

## 3. Aktualizujte asserty testů

Časté problémy s asserty:

| Starý assert | Problém | Nový assert |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` nemá atribut `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` a `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Žádné `api_version` na `OpenAI`/`AsyncOpenAI` | Odstranit úplně |
| `isinstance(client, AsyncAzureOpenAI)` | Typ klienta se změnil | `isinstance(client, AsyncOpenAI)` |

---

## 4. Aktualizujte proměnné prostředí ve fixturech

Testy často nastavují proměnné prostředí přes `monkeypatch.setenv`. Aktualizujte je takto:

| Stará proměnná | Nová proměnná | Poznámky |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Standardní konvence Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Odstranit | Není potřeba `api_version` |
| `AZURE_OPENAI_API_VERSION` | Odstranit | Není potřeba `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Zachovat (stále potřeba pro `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Zachovat (název nasazení pro parametr `model`) |

---

## 5. Vyhledejte testovací kód, který je potřeba migrovat

```bash
# Test-specifické zastaralé vzory
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
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->