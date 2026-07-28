# Uhamisho wa Miundombinu ya Mtihani

Unapohamisha msimbo kutoka Chat Completions kwenda Responses API, **mitihani huvunjika kwa njia zinazoweza kutabirika**. Marejeleo haya yanahusu nini cha kuboresha.

---

## Kuiga Majibu ya Mtiririko (Python pytest)

### Madarasa ya msingi ya kuiga

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
            # Hifadhi nafasi tupu: ongeza nafasi mbele ya maneno yote isipokuwa la kwanza
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

### Kupangilia majibu ya kuiga kulingana na maudhui ya ujumbe

Programu halisi hutumikia majibu tofauti kulingana na amri. Panga kwa `input` (si `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # API ya Majibu inatumia 'input' si 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Njia za monkeypatch

| Aina ya Klienti | Njia ya Monkeypatch |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (synchronus) | `openai.resources.responses.Responses.create` |

> **Kabla** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Baada** (Responses): `openai.resources.responses.AsyncResponses.create`

### Mfano kamili wa fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Darasa la MockResponseEvent na AsyncResponseIterator hapa ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Sasisha fixtures za kuiga

Badilisha mocks zinazotegemea `ChatCompletionChunk` kwa kutumia kiolezo cha `MockResponseEvent` / `AsyncResponseIterator` kama ulivyo juu. Mabadiliko muhimu:

| Kabla (Chat Completions mock) | Baada (Responses mock) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` ndani ya chunk | `event.type == "response.completed"` |
| Chunk maalum ya Azure `prompt_filter_results` | Ondoa kabisa |
| Matokeo maalum ya Azure `content_filter_results` kwa kila chaguo | Ondoa kabisa |
| `kwargs.get("messages")` katika mock | `kwargs.get("input")` katika mock |

---

## 2. Sasisha faili za snapshot / golden

Ikiwa suite ya mtihani inatumia upimaji snapshot (mfano, `pytest-snapshot`, syrupy, au snapshots za JSONL zilizotengenezwa kwa mkono), muundo wa matokeo unabadilika:

**Kabla** (Chat Completions JSONL ya mtiririko):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Baada** (Responses API JSONL ya mtiririko):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Muundo mpya ni rahisi sana — hakuna nyanja za `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, au `content_filter_results`. Sasisha au tengeneza upya faili zote za snapshot.

> **Kidokezo**: Endesha mitihani kwa `--snapshot-update` (pytest-snapshot) au `--update-snapshots` (syrupy) baada ya uhamisho ili zitengeneze upya moja kwa moja.

---

## 3. Sasisha uthibitisho za mtihani

Mavunjiko ya kawaida ya uthibitisho:

| Uthibitisho wa zamani | Tatizo | Uthibitisho mpya |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` haina sifa ya `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` na `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Hakuna `api_version` kwenye `OpenAI`/`AsyncOpenAI` | Ondoa kabisa |
| `isinstance(client, AsyncAzureOpenAI)` | Aina ya klienti imebadilika | `isinstance(client, AsyncOpenAI)` |

---

## 4. Sasisha mabadiliko ya mazingira katika fixtures za mtihani

Mitihani mara nyingi huweka env vars kupitia `monkeypatch.setenv`. Sasisha hizi:

| Envari ya zamani | Envari mpya | Maelezo |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Kanuni ya kawaida ya Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Ondoa | Hakuna `api_version` inahitajika |
| `AZURE_OPENAI_API_VERSION` | Ondoa | Hakuna `api_version` inahitajika |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Hifadhi (bado inahitajika kwa `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Hifadhi (jina la deployment kwa param ya `model`) |

---

## 5. Tafuta msimbo wa mtihani unaohitaji uhamisho

```bash
# Mifumo ya urithi maalum kwa mtihani
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
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->