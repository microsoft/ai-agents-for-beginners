# Testavimo infrastruktūros migracija

Migruojant kodo bazę nuo Chat Completions prie Responses API, **testai nutrūksta numatomais būdais**. Ši nuoroda apima, ką taisyti.

---

## Srauto atsakymų imituojimas (Python pytest)

### Pagrindinės imitavimo klasės

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
            # Išlaikyti tarpą: pridėti tarpą prie visų žodžių, išskyrus pirmąjį
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

### Maršrutuoti imituojamus atsakymus pagal žinutės turinį

Tikros programos pateikia skirtingus atsakymus pagal užklausą. Maršrutuokite pagal `input` (ne `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Atsakymai API naudoja 'input', o ne 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Keliavimo kelių pertvarkymas

| Kliento tipas | Keliavimo kelias |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sinchroninis) | `openai.resources.responses.Responses.create` |

> **Ankstesnis** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Vėlesnis** (Responses): `openai.resources.responses.AsyncResponses.create`

### Pilnas pavyzdys su fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Čia yra MockResponseEvent ir AsyncResponseIterator klasės ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Atnaujinkite imitavimo fixture'us

Pakeiskite `ChatCompletionChunk` pagrįstus imitavimus į aukščiau pateiktą `MockResponseEvent` / `AsyncResponseIterator` šabloną. Pagrindiniai pakeitimai:

| Ankstesnis (Chat Completions imitavimas) | Vėlesnis (Responses imitavimas) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` į gabalėlį | `event.type == "response.completed"` |
| Azure specifinis `prompt_filter_results` gabalėlis | Pašalinkite visiškai |
| Azure specifinis `content_filter_results` kiekvienam pasirinkimui | Pašalinkite visiškai |
| `kwargs.get("messages")` imitavime | `kwargs.get("input")` imitavime |

---

## 2. Atnaujinkite snapshot / golden failus

Jei testų paketas naudoja snapshot testavimą (pvz., `pytest-snapshot`, syrupy arba ranka rašyti JSONL snapshot'ai), tikėtinas išvesties formatas pasikeičia:

**Ankstesnis** (Chat Completions srauto JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Vėlesnis** (Responses API srauto JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Naujas formatas yra ženkliai paprastesnis — nėra jokių laukų `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` ar `content_filter_results`. Atitinkamai atnaujinkite arba sugeneruokite visus snapshot failus iš naujo.

> **Patvirtinimas**: Iš naujo paleiskite testus su `--snapshot-update` (pytest-snapshot) arba `--update-snapshots` (syrupy) po migracijos, kad automatiškai sugeneruotumėte.

---

## 3. Atnaujinkite testavimo patvirtinimus

Dažni patvirtinimų gedimai:

| Senas patvirtinimas | Problema | Naujas patvirtinimas |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` neturi atributo `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` ir `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI` / `AsyncOpenAI` nėra `api_version` | Pašalinkite visiškai |
| `isinstance(client, AsyncAzureOpenAI)` | Kliento tipas pasikeitė | `isinstance(client, AsyncOpenAI)` |

---

## 4. Atnaujinkite aplinkos kintamuosius testų fixture'uose

Testai dažnai nustato aplinkos kintamuosius naudojant `monkeypatch.setenv`. Atnaujinkite juos:

| Senas aplinkos kintamasis | Naujas aplinkos kintamasis | Pastabos |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Standartinė Azure Identity SDK konvencija |
| `AZURE_OPENAI_VERSION` | Pašalinkite | `api_version` nereikia |
| `AZURE_OPENAI_API_VERSION` | Pašalinkite | `api_version` nereikia |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Palikite (vis dar reikalingas `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Palikite (diegiamos aplinkos pavadinimas `model` parametrui) |

---

## 5. Ieškokite testų kodo, kurį reikia migruoti

```bash
# Testams būdingi paveldimi šablonai
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
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->