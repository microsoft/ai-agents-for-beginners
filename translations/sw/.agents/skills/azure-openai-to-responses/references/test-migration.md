# Uhamishaji wa Miundombinu ya Ma jaribio

Wakati wa kuhama msimbo kutoka Chat Completions kwenda Responses API, **ma jaribio huvunjika kwa njia zinazotarajiwa**. Marejeleo haya yanaleta kinachohitaji kusahihishwa.

---

## Kuigiza Majibu ya Mtiririko (Python pytest)

### Madarasa ya msingi ya kuigiza

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
            # Hifadhi nafasi tupu: ongeza nafasi kwenye maneno yote isipokuwa neno la kwanza
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

### Kupangilia majibu ya kuigiza kwa maudhui ya ujumbe

Programu halisi hutumikia majibu tofauti kulingana na ombi. Pangilia kwa `input` (sio `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # APIs ya Majibu inatumia 'input' si 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Njia za Monkeypatch

| Aina ya Mteja | Njia ya Monkeypatch |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (synchronou) | `openai.resources.responses.Responses.create` |

> **Kabla** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Baada** (Responses): `openai.resources.responses.AsyncResponses.create`

### Mfano kamili wa fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Hapa ni Madarasa ya MockResponseEvent na AsyncResponseIterator ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Sasisha fixtures za kuigiza

Badilisha kuigiza kulikotumia `ChatCompletionChunk` na mfano wa `MockResponseEvent` / `AsyncResponseIterator` ulio juu. Mabadiliko muhimu:

| Kabla (kuigiza Chat Completions) | Baada (kuigiza Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` ndani ya chunk | `event.type == "response.completed"` |
| chunk maalum ya Azure `prompt_filter_results` | Ondoa kabisa |
| matokeo maalum ya Azure ya `content_filter_results` kwa kila chaguo | Ondoa kabisa |
| `kwargs.get("messages")` katika kuigiza | `kwargs.get("input")` katika kuigiza |

---

## 2. Sasisha faili za snapshot / za dhahabu

Ikiwa suite ya majaribio inatumia snapshot testing (mfano, `pytest-snapshot`, syrupy, au snapshot zilizotengenezwa kwa mkono za JSONL), mabadiliko katika sura inayotarajiwa yatafanyika:

**Kabla** (Chat Completions mtiririko JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Baada** (Responses API mtiririko JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Sura mpya ni rahisi sana — hakuna `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, au sehemu za `content_filter_results`. Sasisha au tengeneza upya faili zote za snapshot.

> **Ushauri**: Endesha majaribio na `--snapshot-update` (pytest-snapshot) au `--update-snapshots` (syrupy) baada ya kuhama ili kutengeneza upya kiotomatiki.

---

## 3. Sasisha matamko ya majaribio

Mafaili yanayovuruga zaidi:

| Tamko la zamani | Tatizo | Tamko jipya |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` haina sifa ya `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` na `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Hakuna `api_version` ndani ya `OpenAI`/`AsyncOpenAI` | Ondoa kabisa |
| `isinstance(client, AsyncAzureOpenAI)` | Aina ya mteja imebadilika | `isinstance(client, AsyncOpenAI)` |

---

## 4. Sasisha vigezo vya mazingira kwenye fixtures za majaribio

Mara nyingi majaribio huweka vigezo vya mazingira kupitia `monkeypatch.setenv`. Sasisha haya:

| Kigezo cha zamani cha mazingira | Kigezo kipya cha mazingira | Maelezo |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Kawaida ya Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Ondoa | Hakuna `api_version` inayohitajika |
| `AZURE_OPENAI_API_VERSION` | Ondoa | Hakuna `api_version` inayohitajika |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Hifadhi (bado inahitajika kwa `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Hifadhi (jina la uenezaji kwa kipengele cha `model`) |

---

## 5. Tafuta msimbo wa majaribio unaohitaji uhamishaji

```bash
# Mifumo ya kale maalum kwa majaribio
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