# ಪರೀಕ್ಷಾ ಮೂಲಸೌಕರ್ಯ ವರ್ಗಾವಣೆ

Chat Completions ನಿಂದ Responses API ಗೆ ಕೋಡ್ ಬೇಸ್ ವರ್ಗಾಯಿಸುವಾಗ, **ಪರೀಕ್ಷೆಗಳು ನಿರೀಕ್ಷಿತ ರೀತಿಗಳಲ್ಲಿ ನಟಿಸುತ್ತವೆ**. ಏನು ಸರಿಪಡಿಸಬೇಕು ಎಂಬುದನ್ನು ಈ ಸೂಚಿ ಆವರಿಸುತ್ತದೆ.

---

## ಸ್ಟ್ರೀಮಿಂಗ್ ದೃಢೀಕರಣಗಳನ್ನು ಮಾಕ್ ಮಾಡುವುದು (Python pytest)

### ಕೋರ್ ಮಾಕ್ ವರ್ಗಗಳು

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
            # ಬಿಳಿ ಸ್ಥಳವನ್ನು ಉಳಿಸಿ: ಮೊದಲವು ತೊಡಗಿಸದಂತೆ ಎಲ್ಲ ಪದಗಳ ಮೊದಲಿಗೆ ಖಾಲಿ ಜಾಗವನ್ನು ಜೋಡಿಸಿ
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

### ಸಂದೇಶ ವಿಷಯದ ಮೂಲಕ ಮಾಕ್ ಉತ್ತರಗಳನ್ನು ಮಾರ್ಗದರ್ಶನ ಮಾಡುವುದು

ನಿಜವಾದ ಆ್ಯಪ್‌ಗಳು ಪ್ರಾಂಪ್ಟ್ ಆಧಾರಿತವಾಗಿ ವಿಭಿನ್ನ ಉತ್ತರಗಳನ್ನು ನೀಡುತ್ತವೆ. `input` (ಸಂದೇಶಗಳು ಅಲ್ಲ) ಮೂಲಕ ಮಾರ್ಗದರ್ಶನ ಮಾಡಿ:

```python
async def mock_acreate(*args, **kwargs):
    # ಪ್ರತಿಕ್ರಿಯೆಗಳು API 'input' ಬಳಸುತ್ತದೆ, 'messages' ಅಲ್ಲ
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### ಮನಕಿ ಪ್ಯಾಚ್ ಮಾರ್ಗಗಳು

| ಕ್ಲೈಂಟ್ ಪ್ರಕಾರ | ಮನಕಿ ಪ್ಯಾಚ್ ಮಾರ್ಗ |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (ಸಿಂಕ್) | `openai.resources.responses.Responses.create` |

> **ಮೊದಲು** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **ನಂತರ** (Responses): `openai.resources.responses.AsyncResponses.create`

### ಸಂಪೂರ್ಣ ಫಿಕ್ಸ್ಚರ್ ಉದಾಹರಣೆ

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent ಮತ್ತು AsyncResponseIterator ವರ್ಗಗಳು ಇಲ್ಲಿ ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. ಮಾಕ್ ಫಿಕ್ಸ್ಚರ್‌ಗಳನ್ನು ಅಪ್ಡೇಟ್ ಮಾಡಿ

`ChatCompletionChunk` ಆಧಾರಿತ ಮಾಕ್ಗಳನ್ನು ಮೇಲಿನ `MockResponseEvent` / `AsyncResponseIterator` ಮಾದರಿಯಿಂದ ಬದಲಾಯಿಸಿ. ಪ್ರಮುಖ ಬದಲಾವಣೆಗಳು:

| ಹಳೆಯದು (Chat Completions ಮಾಕ್) | ಹೊಸದು (Responses ಮಾಕ್) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| ಚಂಕ್ ನಲ್ಲಿ `finish_reason="stop"` | `event.type == "response.completed"` |
| Azure-ವಿಶೇಷ `prompt_filter_results` ಚಂಕ್ | ಸಂಪೂರ್ಣವಾಗಿ ತೆಗೆದುಹಾಕಿ |
| Azure-ವಿಶೇಷ `content_filter_results` ಪ್ರತಿ ಆಯ್ಕೆಯಲ್ಲಿ | ಸಂಪೂರ್ಣವಾಗಿ ತೆಗೆದುಹಾಕಿ |
| ಮಾಕ್ ನಲ್ಲಿ `kwargs.get("messages")` | ಮಾಕ್ ನಲ್ಲಿ `kwargs.get("input")` |

---

## 2. ಸ్నಾಪ್‌ಶಾಟ್ / ಗೋಲ್ಡನ್ ಫೈಲ್‌ಗಳನ್ನು ಅಪ್ಡೇಟ್ ಮಾಡಿ

ಪರೀಕ್ಷಾ ಸ್ಯೂಟ್ ಸ্নಾಪ್‌ಶಾಟ್ ಟೆಸ್ಟಿಂಗ್ ಅನ್ನು ಬಳಸಿದರೆ (ಉದಾ. `pytest-snapshot`, syrupy, ಅಥವಾ ಸ್ವ-ರಚಿತ JSONL ಸ್ನಾಪ್‌ಶಾಟ್‌ಗಳು), ನಿರೀಕ್ಷಿತ ಔಟ್‌ಪುಟ್ ಆಕಾರ ಬದಲಾಗುತ್ತದೆ:

**ಮೊದಲು** (Chat Completions ಸ್ಟ್ರೀಮಿಂಗ್ JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**ನಂತರ** (Responses API ಸ್ಟ್ರೀಮಿಂಗ್ JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

ಹೊಸ ಆಕಾರವು ಬಹುಮಟ್ಟಿಗೆ ಸರಳವಾಗಿದೆ — `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, ಅಥವಾ `content_filter_results` ಕ್ಷೇತ್ರಗಳಿಲ್ಲ. ಎಲ್ಲಾ ಸ্নಾಪ್‌ಶಾಟ್ ಫೈಲ್‌ಗಳನ್ನು ಅಪ್ಡೇಟ್ ಮಾಡಿ ಅಥವಾ ಪುನರ್ರಚಿಸಿ.

> **ಸಲಹೆ**: ಸ್ವಯಂಚಾಲಿತ ಪುನರುತ್ಪಾದನೆಗಾಗಿ ವರ್ಗಾವಣೆಯ ನಂತರ `--snapshot-update` (pytest-snapshot) ಅಥವಾ `--update-snapshots` (syrupy) ಒದಗಿಸಿ ಟೆಸ್ಟ್‌ಗಳನ್ನು ಚಾಲನೆ ಮಾಡಿ.

---

## 3. ಟೆಸ್ಟ್ ದೃಢೀಕರಣಗಳನ್ನು ಅಪ್ಡೇಟ್ ಮಾಡಿ

ಸಾಮಾನ್ಯ ದೃಢೀಕರಣ ವಿಫಲತೆಗಳು:

| ಹಳೆಯ ದೃಢೀಕರಣ | ಸಮಸ್ಯೆ | ಹೊಸ ದೃಢೀಕರಣ |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` ನಲ್ಲಿ `_azure_ad_token_provider` ಗುಣಲಕ್ಷಣವಿಲ್ಲ | `isinstance(client, AsyncOpenAI)` ಮತ್ತು `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` ನಲ್ಲಿ `api_version` ಇಲ್ಲ | ಸಂಪೂರ್ಣವಾಗಿ ತೆಗೆದುಹಾಕಿ |
| `isinstance(client, AsyncAzureOpenAI)` | ಕ್ಲೈಂಟ್ ಪ್ರಕಾರ ಬದಲಾಗಿದೆ | `isinstance(client, AsyncOpenAI)` |

---

## 4. ಪರೀಕ್ಷಾ ಫಿಕ್ಸ್ಚರ್‌ಗಳಲ್ಲಿ ಪರಿಸರ ಚರಗಳನ್ನು (environment variables) ಅಪ್ಡೇಟ್ ಮಾಡಿ

ಟೆಸ್ಟ್‌ಗಳು ಹೆಚ್ಚಾಗಿ `monkeypatch.setenv` ಮೂಲಕ ಪರಿಸರ ಚರಗಳನ್ನು ಹೊಂದಿಸುತ್ತವೆ. ಅವುಗಳನ್ನು ಅಪ್ಡೇಟ್ ಮಾಡಿ:

| ಹಳೆಯ ಪರಿಸರ ಚರ | ಹೊಸ ಪರಿಸರ ಚರ | ಟಿಪ್ಪಣಿಗಳು |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | ಸ್ಟ್ಯಾಂಡರ್ಡ್ Azure ಐಡೆಂಟಿಟಿ SDK ನಿಯಮಾವಳಿ |
| `AZURE_OPENAI_VERSION` | ತೆಗೆಯಿರಿ | `api_version` ಅಗತ್ಯವಿಲ್ಲ |
| `AZURE_OPENAI_API_VERSION` | ತೆಗೆಯಿರಿ | `api_version` ಅಗತ್ಯವಿಲ್ಲ |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | ಉಳಿಸಿರಿ (`base_url` ಗೆ ಇನ್ನೂ ಬೇಕು) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | ಉಳಿಸಿರಿ (`model` ಪರಿಮಾಣಕ್ಕಾಗಿ ನಿಯೋಜನೆ ಹೆಸರು) |

---

## 5. ವರ್ಗಾವಣೆಗೆ ಅಗತ್ಯವಿರುವ ಪರೀಕ್ಷಾ ಕೋಡ್ ಹುಡುಕಿ

```bash
# ಪರೀಕ್ಷಾ-ವಿಶಿಷ್ಟ ಇತಿಹಾಸಾತ್ಮಕ ಮಾದರಿಗಳು
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
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->