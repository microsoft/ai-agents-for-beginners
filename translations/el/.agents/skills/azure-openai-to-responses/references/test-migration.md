# Μεταφορά Υποδομής Δοκιμών

Όταν μεταφέρετε μια βάση κώδικα από το Chat Completions στο Responses API, **οι δοκιμές σπάνε με προβλέψιμους τρόπους**. Αυτή η αναφορά καλύπτει τι πρέπει να διορθώσετε.

---

## Προσομοίωση Ροών Απαντήσεων (Python pytest)

### Βασικές κλάσεις mock

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
            # Διατήρηση κενών: προσθέστε κενό πριν από όλες τις λέξεις εκτός της πρώτης
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

### Δρομολόγηση mock απαντήσεων ανά περιεχόμενο μηνύματος

Πραγματικές εφαρμογές παρέχουν διαφορετικές απαντήσεις με βάση το prompt. Δρομολογήστε με βάση το `input` (όχι τα `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Το API Απαντήσεων χρησιμοποιεί 'input' όχι 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Διαδρομές monkeypatch

| Τύπος πελάτη | Διαδρομή Monkeypatch |
|-------------|---------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **Προηγούμενο** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Μετά** (Responses): `openai.resources.responses.AsyncResponses.create`

### Πλήρες παράδειγμα fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Οι κλάσεις MockResponseEvent και AsyncResponseIterator εδώ ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Ενημέρωση mock fixtures

Αντικαταστήστε τα mocks βασισμένα σε `ChatCompletionChunk` με το παραπάνω πρότυπο `MockResponseEvent` / `AsyncResponseIterator`. Βασικές αλλαγές:

| Πριν (mock Chat Completions) | Μετά (mock Responses) |
|-------------------------------|-----------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` στο chunk | `event.type == "response.completed"` |
| Chunk `prompt_filter_results` ειδικό για Azure | Αφαιρέστε εντελώς |
| `content_filter_results` ανά επιλογή ειδικό για Azure | Αφαιρέστε εντελώς |
| `kwargs.get("messages")` στο mock | `kwargs.get("input")` στο mock |

---

## 2. Ενημέρωση snapshot / golden αρχείων

Εάν το σύνολο δοκιμών χρησιμοποιεί snapshot testing (π.χ., `pytest-snapshot`, syrupy ή χειροποίητα JSONL snapshots), το αναμενόμενο σχήμα εξόδου αλλάζει:

**Προηγούμενο** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Μετά** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Το νέο σχήμα είναι δραματικά πιο απλό — χωρίς πεδία `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` ή `content_filter_results`. Ενημερώστε ή αναδημιουργήστε όλα τα αρχεία snapshot.

> **Συμβουλή**: Εκτελέστε τις δοκιμές με `--snapshot-update` (pytest-snapshot) ή `--update-snapshots` (syrupy) μετά τη μετανάστευση για αυτόματη αναδημιουργία.

---

## 3. Ενημέρωση των assertions στις δοκιμές

Συνηθισμένες αποτυχίες assertions:

| Παλιά assertion | Πρόβλημα | Νέα assertion |
|----------------|----------|-------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` δεν έχει το attribute `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` και `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Δεν υπάρχει `api_version` στο `OpenAI` / `AsyncOpenAI` | Αφαιρέστε εντελώς |
| `isinstance(client, AsyncAzureOpenAI)` | Ο τύπος πελάτη άλλαξε | `isinstance(client, AsyncOpenAI)` |

---

## 4. Ενημέρωση μεταβλητών περιβάλλοντος στα test fixtures

Συχνά οι δοκιμές ορίζουν env vars μέσω `monkeypatch.setenv`. Ενημερώστε τα ως εξής:

| Παλιά env var | Νέα env var | Σημειώσεις |
|--------------|------------|----------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Τυπική σύμβαση Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Αφαιρέστε | Δεν χρειάζεται `api_version` |
| `AZURE_OPENAI_API_VERSION` | Αφαιρέστε | Δεν χρειάζεται `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Κρατήστε (ακόμα χρειάζεται για `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Κρατήστε (όνομα ανάπτυξης για παράμετρο `model`) |

---

## 5. Αναζήτηση κώδικα δοκιμών που χρειάζεται μετανάστευση

```bash
# Πρότυπα κληρονομιάς ειδικά για δοκιμές
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
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->