# Migrácia testovacej infraštruktúry

Pri migrácii kódu zo Chat Completions na Responses API sa **testy rozbijú predvídateľným spôsobom**. Tento referenčný materiál pokrýva, čo je potrebné opraviť.

---

## Mockovanie streamovaných odpovedí (Python pytest)

### Základné mock triedy

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
            # Zachovať medzery: pred každé slovo okrem prvého pridať medzeru
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

### Smerovanie mock odpovedí podľa obsahu správy

Skutočné aplikácie poskytujú rôzne odpovede podľa promptu. Smerujte podľa `input` (nie `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API používa 'input', nie 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch cesty

| Typ klienta | Monkeypatch cesta |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (synchrónny) | `openai.resources.responses.Responses.create` |

> **Predtým** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Potom** (Responses): `openai.resources.responses.AsyncResponses.create`

### Kompletný príklad fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Triedy MockResponseEvent a AsyncResponseIterator tu ...

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

Nahraďte mocky založené na `ChatCompletionChunk` vzorom `MockResponseEvent` / `AsyncResponseIterator` vyššie. Kľúčové zmeny:

| Predtým (Chat Completions mock) | Potom (Responses mock) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` v kúsku | `event.type == "response.completed"` |
| Azure-špecifický `prompt_filter_results` kúsok | Odstrániť úplne |
| Azure-špecifický `content_filter_results` pre voľbu | Odstrániť úplne |
| `kwargs.get("messages")` v mocku | `kwargs.get("input")` v mocku |

---

## 2. Aktualizujte snapshot / zlaté súbory

Ak testovacia sada používa snapshot testovanie (napr. `pytest-snapshot`, syrupy alebo vlastné JSONL snapshoty), mení sa očakávaný tvar výstupu:

**Predtým** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Potom** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Nový tvar je výrazne jednoduchší — žiadne polia `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` alebo `content_filter_results`. Aktualizujte alebo znovu vygenerujte všetky snapshot súbory.

> **Tip**: Po migrácii spustite testy s `--snapshot-update` (pytest-snapshot) alebo `--update-snapshots` (syrupy) pre automatickú obnovu.

---

## 3. Aktualizujte testovacie overenia

Bežné chyby overenia:

| Staré overenie | Problém | Nové overenie |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` nemá atribút `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` a `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` nemajú `api_version` | Odstrániť úplne |
| `isinstance(client, AsyncAzureOpenAI)` | Typ klienta sa zmenil | `isinstance(client, AsyncOpenAI)` |

---

## 4. Aktualizujte premenné prostredia v testovacích fixture

Testy často nastavujú env premenné cez `monkeypatch.setenv`. Aktualizujte tieto:

| Staré env var | Nové env var | Poznámky |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Štandardná konvencia Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Odstrániť | Nie je potrebné `api_version` |
| `AZURE_OPENAI_API_VERSION` | Odstrániť | Nie je potrebné `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Ponechať (stále potrebné pre `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Ponechať (názov nasadenia pre `model` parameter) |

---

## 5. Vyhľadajte testovací kód, ktorý potrebuje migráciu

```bash
# Testovo špecifické dedičné vzory
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
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->