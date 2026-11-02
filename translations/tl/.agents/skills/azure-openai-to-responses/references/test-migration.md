# Migrasyon ng Test Infrastructure

Kapag nililipat ang isang codebase mula sa Chat Completions papuntang Responses API, **ang mga tests ay nasisira sa mga predictable na paraan**. Sinasaklaw ng reference na ito kung ano ang dapat ayusin.

---

## Pagmomock ng Streaming Responses (Python pytest)

### Core mock na mga klase

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
            # Panatilihin ang whitespace: ilagay ang espasyo sa harap ng lahat ng salita maliban sa una
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

### Pagruruta ng mock responses base sa nilalaman ng mensahe

Ang mga totoong apps ay naghahain ng iba't ibang sagot base sa prompt. Magruta gamit ang `input` (hindi `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Ang Responses API ay gumagamit ng 'input' hindi 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Mga path na imomonkeypatch

| Uri ng Client | Monkeypatch path |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **Dati** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Ngayon** (Responses): `openai.resources.responses.AsyncResponses.create`

### Buong halimbawa ng fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Mga klase ng MockResponseEvent at AsyncResponseIterator dito ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. I-update ang mock fixtures

Palitan ang `ChatCompletionChunk`-based na mocks ng pattern na `MockResponseEvent` / `AsyncResponseIterator` sa itaas. Mga pangunahing pagbabago:

| Dati (Chat Completions mock) | Ngayon (Responses mock) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` sa chunk | `event.type == "response.completed"` |
| Azure-specific na `prompt_filter_results` chunk | Alisin nang buo |
| Azure-specific na `content_filter_results` bawat choice | Alisin nang buo |
| `kwargs.get("messages")` sa mock | `kwargs.get("input")` sa mock |

---

## 2. I-update ang snapshot / mga golden file

Kung gumagamit ang test suite ng snapshot testing (hal., `pytest-snapshot`, syrupy, o custom na JSONL snapshots), nagbabago ang hinahanap na hugis ng output:

**Dati** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Ngayon** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Mas simple nang husto ang bagong hugis — walang `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, o mga field na `content_filter_results`. I-update o i-regenerate ang lahat ng snapshot files.

> **Tip**: Patakbuhin ang mga tests gamit ang `--snapshot-update` (pytest-snapshot) o `--update-snapshots` (syrupy) pagkatapos ng migrasyon upang awtomatikong i-regenerate.

---

## 3. I-update ang mga test assertion

Mga karaniwang pagka-break ng assertion:

| Lumang assertion | Problema | Bagong assertion |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | Walang `_azure_ad_token_provider` attribute ang `AsyncOpenAI` | `isinstance(client, AsyncOpenAI)` at `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Walang `api_version` sa `OpenAI`/`AsyncOpenAI` | Alisin nang buo |
| `isinstance(client, AsyncAzureOpenAI)` | Nagbago ang uri ng Client | `isinstance(client, AsyncOpenAI)` |

---

## 4. I-update ang mga environment variable sa test fixtures

Madalas mag-set ang mga tests ng env vars sa pamamagitan ng `monkeypatch.setenv`. I-update ito:

| Lumang env var | Bagong env var | Mga Tala |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Karaniwang convention ng Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Alisin | Hindi na kailangan ng `api_version` |
| `AZURE_OPENAI_API_VERSION` | Alisin | Hindi na kailangan ng `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Panatilihin (kailangan pa rin para sa `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Panatilihin (pangalan ng deployment para sa `model` param) |

---

## 5. Hanapin ang test code na kailangang ilipat

```bash
# Mga partikular na legacy na pattern para sa pagsubok
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
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->