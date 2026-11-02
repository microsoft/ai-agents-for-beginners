# Testinfrastruktur-Migration

Beim Migrieren eines Codebases von Chat Completions zur Responses API **brechen Tests auf vorhersehbare Weise**. Diese Referenz erklärt, was zu beheben ist.

---

## Streaming-Antworten mocken (Python pytest)

### Kern-Mock-Klassen

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
            # Leerzeichen beibehalten: Füge vor alle Wörter außer dem ersten ein Leerzeichen ein
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

### Routing von Mock-Antworten anhand des Nachrichteninhalts

Echte Anwendungen liefern unterschiedliche Antworten basierend auf dem Prompt. Routen Sie nach `input` (nicht `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Die Responses-API verwendet 'input' und nicht 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch-Pfade

| Client-Typ | Monkeypatch-Pfad |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **Vorher** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Nachher** (Responses): `openai.resources.responses.AsyncResponses.create`

### Vollständiges Fixture-Beispiel

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent- und AsyncResponseIterator-Klassen hier ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Aktualisiere Mock-Fixtures

Ersetze auf `ChatCompletionChunk` basierende Mocks durch das oben gezeigte `MockResponseEvent` / `AsyncResponseIterator` Muster. Wichtige Änderungen:

| Vorher (Chat Completions Mock) | Nachher (Responses Mock) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` im Chunk | `event.type == "response.completed"` |
| Azure-spezifischer `prompt_filter_results` Chunk | Komplett entfernen |
| Azure-spezifische `content_filter_results` pro Wahl | Komplett entfernen |
| `kwargs.get("messages")` im Mock | `kwargs.get("input")` im Mock |

---

## 2. Aktualisiere Snapshot- / Golden-Dateien

Falls die Test-Suite Snapshot-Tests verwendet (z.B. `pytest-snapshot`, syrupy oder selbstgeschriebene JSONL-Snapshots), ändert sich die erwartete Ausgabeform:

**Vorher** (Chat Completions Streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Nachher** (Responses API Streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Die neue Form ist deutlich einfacher — keine Felder wie `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` oder `content_filter_results`. Aktualisiere oder generiere alle Snapshot-Dateien neu.

> **Tipp**: Führen Sie Tests mit `--snapshot-update` (pytest-snapshot) oder `--update-snapshots` (syrupy) nach der Migration aus, um Snapshots automatisch zu aktualisieren.

---

## 3. Aktualisiere Test-Assertions

Häufige Assertion-Fehler:

| Alte Assertion | Problem | Neue Assertion |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` hat kein Attribut `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` und `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Kein `api_version` auf `OpenAI`/`AsyncOpenAI` | Komplett entfernen |
| `isinstance(client, AsyncAzureOpenAI)` | Client-Typ geändert | `isinstance(client, AsyncOpenAI)` |

---

## 4. Aktualisiere Umgebungsvariablen in Test-Fixtures

Tests setzen oft Umgebungsvariablen über `monkeypatch.setenv`. Diese aktualisieren:

| Alte Env-Var | Neue Env-Var | Hinweise |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Standard Azure Identity SDK Konvention |
| `AZURE_OPENAI_VERSION` | Entfernen | Kein `api_version` benötigt |
| `AZURE_OPENAI_API_VERSION` | Entfernen | Kein `api_version` benötigt |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Beibehalten (weiterhin für `base_url` benötigt) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Beibehalten (Deployment-Name für `model` Parameter) |

---

## 5. Suche nach Testcode, der migriert werden muss

```bash
# Testspezifische Legacy-Muster
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
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->