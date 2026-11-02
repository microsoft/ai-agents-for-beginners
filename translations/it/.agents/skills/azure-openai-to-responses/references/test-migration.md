# Migrazione dell'Infrastruttura di Test

Quando si migra una base di codice da Chat Completions all'API Responses, **i test si rompono in modi prevedibili**. Questo riferimento copre cosa correggere.

---

## Mocking delle Risposte in Streaming (Python pytest)

### Classi mock principali

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
            # Conserva gli spazi bianchi: anteponi uno spazio a tutte le parole tranne la prima
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

### Instradamento delle risposte mock in base al contenuto del messaggio

Le app reali forniscono risposte diverse in base al prompt. Instrada per `input` (non `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # L'API delle Risposte utilizza 'input' e non 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Percorsi da monkeypatchare

| Tipo di client | Percorso da monkeypatchare |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **Prima** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Dopo** (Responses): `openai.resources.responses.AsyncResponses.create`

### Esempio completo di fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... classi MockResponseEvent e AsyncResponseIterator qui ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Aggiornare le fixture mock

Sostituire i mock basati su `ChatCompletionChunk` con il pattern `MockResponseEvent` / `AsyncResponseIterator` sopra. Cambiamenti chiave:

| Prima (mock Chat Completions) | Dopo (mock Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` nel chunk | `event.type == "response.completed"` |
| Chunk specifico Azure `prompt_filter_results` | Rimuovere completamente |
| `content_filter_results` specifico Azure per scelta | Rimuovere completamente |
| `kwargs.get("messages")` nel mock | `kwargs.get("input")` nel mock |

---

## 2. Aggiornare i file snapshot / golden

Se la suite di test usa snapshot testing (es., `pytest-snapshot`, syrupy o snapshot JSONL personalizzati), la forma dell'output atteso cambia:

**Prima** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Dopo** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

La nuova forma è drasticamente più semplice — senza campi `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, o `content_filter_results`. Aggiornare o rigenerare tutti i file snapshot.

> **Consiglio**: Eseguire i test con `--snapshot-update` (pytest-snapshot) o `--update-snapshots` (syrupy) dopo la migrazione per rigenerarli automaticamente.

---

## 3. Aggiornare le asserzioni dei test

Guasti comuni nelle asserzioni:

| Vecchia asserzione | Problema | Nuova asserzione |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` non ha l'attributo `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` e `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Non esiste `api_version` su `OpenAI`/`AsyncOpenAI` | Rimuovere completamente |
| `isinstance(client, AsyncAzureOpenAI)` | Tipo client cambiato | `isinstance(client, AsyncOpenAI)` |

---

## 4. Aggiornare le variabili d'ambiente nelle fixture di test

I test spesso impostano variabili d'ambiente tramite `monkeypatch.setenv`. Aggiornarle così:

| Vecchia variabile d'ambiente | Nuova variabile d'ambiente | Note |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Convenzione standard Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Rimuovere | Non serve `api_version` |
| `AZURE_OPENAI_API_VERSION` | Rimuovere | Non serve `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Mantenere (ancora necessario per `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Mantenere (nome deployment per parametro `model`) |

---

## 5. Cercare codice di test che necessita migrazione

```bash
# Modelli legacy specifici per i test
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
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->