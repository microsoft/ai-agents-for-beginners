# ಪರೀಕ್ಷೆ ಮೂಲಸೌಕರ್ಯ ವರ್ಗಾವಣೆ

ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳಿಂದ ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಗೆ ಕೋಡ್‌ಬೇಸ್ ಅನ್ನು ವರ್ಗಾಯಿಸುವಾಗ, **ಪರೀಕ್ಷೆಗಳು ನಿರೀಕ್ಷಿತ ರೀತಿಯಲ್ಲಿ ಹಾಳಾಗುತ್ತವೆ**. ಏನು ಸರಿಪಡಿಸಬೇಕೆಂಬುದನ್ನು ಈ ಉಲ್ಲೇಖವು ಒಳಗೊಂಡಿದೆ.

---

## ಸ್ಟ್ರೀಮಿಂಗ್ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನಕಲು ಮಾಡುವುದು (Python pytest)

### ಮೂಲ ನಕಲಿ ವರ್ಗಗಳು

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
            # ಶ್ವೇತಸ್ಥಳವನ್ನು ಉಳಿಸಿ: ಮೊದಲ ಪದವನ್ನು ಹೊರತುಪಡಿಸಿ ಎಲ್ಲ ಪದಗಳಿಗೂ ಮುಂಭಾಗದಲ್ಲಿ ಖಾಲಿ ಜಾಗ ಸೇರಿಸಿ
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

### ಸಂದೇಶ ವಿಷಯದ ಮೂಲಕ ನಕಲಿ ಪ್ರತಿಕ್ರಿಯೆಗಳ ಮಾರ್ಗನಿರ್ದೇಶನ

ನಿಜವಾದ ಆಪ್‌ಗಳು ಪ್ರಾಂಪ್ಟ್ ಆಧಾರಿತವಾಗಿ ವಿಭಿನ್ನ ಉತ್ತರಗಳನ್ನು ನೀಡುತ್ತವೆ. `input` (ಮತ್ತು ಸಂದೇಶಗಳು ಅಲ್ಲ) ಮೂಲಕ ಮಾರ್ಗನಿರ್ದೇಶನ ಮಾಡಿ:

```python
async def mock_acreate(*args, **kwargs):
    # ಪ್ರತಿಕ್ರಿಯೆಗಳು API 'input' ಅನ್ನು ಬಳಸಿ 'messages' ಅನ್ನು ಅಲ್ಲ
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### ಮಾನ್ಕೀಪ್ಯಾಚ್ ಪಥಗಳು

| ಕ್ಲೈಂಟ್ ಪ್ರಕಾರ | ಮಾನ್ಕೀಪ್ಯಾಚ್ ಪಥ |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (ಸಿಂಕ್) | `openai.resources.responses.Responses.create` |

> **ಹಿಂದೇ** (ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳು): `openai.resources.chat.AsyncCompletions.create`
> **ಈಗ** (ಪ್ರತಿಕ್ರಿಯೆಗಳು): `openai.resources.responses.AsyncResponses.create`

### ಸಂಪೂರ್ಣ ಫಿಕ್ಸ್ಚರ್ ಉದಾಹರಣೆ

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... ಇಲ್ಲಿ MockResponseEvent ಮತ್ತು AsyncResponseIterator ವರ್ಗಗಳು ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. ನಕಲಿ ಫಿಕ್ಸ್ಚರ್‌ಗಳನ್ನು ನವೀಕರಿಸಿ

`ChatCompletionChunk` ಆಧಾರಿತ ನಕಲಿ ವಸ್ತುಗಳನ್ನು ಮೇಲಿನ `MockResponseEvent` / `AsyncResponseIterator` ಮಾದರಿಯಿಂದ ಬದಲಿಸಿ. ಪ್ರಮುಖ ಬದಲಾವಣೆಗಳು:

| ಹಿಂದೆ (ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ ನಕಲಿ) | ಈಗ (ಪ್ರತಿಕ್ರಿಯೆಗಳು ನಕಲಿ) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| ಕುಂಡಲದಲ್ಲಿ `finish_reason="stop"` | `event.type == "response.completed"` |
| ಆಸ್ಯೂರ್-ನಿರ್ದಿಷ್ಟ `prompt_filter_results` ಕುಂಡಲ | ಸಂಪೂರ್ಣವಾಗಿ ತೆಗೆದುಹಾಕಿ |
| ಆಸ್ಯೂರ್-ನಿರ್ದಿಷ್ಟ `content_filter_results` ಪ್ರತಿ ಆಯ್ಕೆಗಾಗಿ | ಸಂಪೂರ್ಣವಾಗಿ ತೆಗೆದುಹಾಕಿ |
| ನಕಲಿಯಲ್ಲಿ `kwargs.get("messages")` | ನಕಲಿಯಲ್ಲಿ `kwargs.get("input")` |

---

## 2. ಸ್ನ್ಯಾಪ್‌ಶಾಟ್ / ಗೋಲ್ಡನ್ ಫೈಲ್‌ಗಳನ್ನು ನವೀಕರಿಸಿ

ಪರೀಕ್ಷಾ ಸಮೂಹವು ಸ್ನ್ಯಾಪ್‌ಶಾಟ್ ಪರೀಕ್ಷೆ (ಉದಾ., `pytest-snapshot`, syrupy, ಅಥವಾ ಕೈಯಿಂದ ರಚಿಸಲಾದ JSONL ಸ್ನ್ಯಾಪ್‌ಶಾಟ್‌ಗಳು) ಬಳಸಿದರೆ, ನಿರೀಕ್ಷಿತ ಔಟ್‌ಪುಟ್ ಆಕಾರ ಬದಲಾಗುತ್ತದೆ:

**ಹಿಂದೇ** (ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳ ಸ್ಟ್ರೀಮಿಂಗ್ JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**ಈಗ** (ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಸ್ಟ್ರೀಮಿಂಗ್ JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

ಹೊಸ ಆಕಾರ ಬಹಳ ಸರಳವಾಗಿದೆ — ಯಾವುದೇ `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, ಅಥವಾ `content_filter_results` ಕ್ಷೇತ್ರಗಳಿಲ್ಲ. ಎಲ್ಲಾ ಸ್ನ್ಯಾಪ್‌ಶಾಟ್ ಫೈಲ್‌ಗಳನ್ನು ನವೀಕರಿಸಿ ಅಥವಾ ಮರುರಚಿಸಿ.

> **ಟಿಪ್**: ಸ್ವಯಂಚಾಲಿತ ಪುನર્જನನಗೊಳಿಸಲು ವರ್ಗಾಯಿಸಿದ ನಂತರ `--snapshot-update` (pytest-snapshot) ಅಥವಾ `--update-snapshots` (syrupy) ಜೊತೆ ಪರೀಕ್ಷೆಗಳನ್ನು ಚಲಾಯಿಸಿ.

---

## 3. ಪರೀಕ್ಷೆ ದೃಢೀಕರಣಗಳನ್ನು ನವೀಕರಿಸಿ

ಸಾಮಾನ್ಯ ದೃಢೀಕರಣ ಮುರಿತಗಳು:

| ಹಳೆಯ ದೃಢೀಕರಣ | проблема | ಹೊಸ ದೃಢೀಕರಣ |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` ನಲ್ಲಿ `_azure_ad_token_provider` ಗುಣಲಕ್ಷಣವಿಲ್ಲ | `isinstance(client, AsyncOpenAI)` ಮತ್ತು `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` ನಲ್ಲಿ `api_version` ಇಲ್ಲ | ಸಂಪೂರ್ಣವಾಗಿ ತೆಗೆದುಹಾಕಿ |
| `isinstance(client, AsyncAzureOpenAI)` | ಕ್ಲೈಂಟ್ ಪ್ರಕಾರ ಬದಲಾಗಿದೆ | `isinstance(client, AsyncOpenAI)` |

---

## 4. ಪರೀಕ್ಷಾ ಫಿಕ್ಸ್ಚರ್‌ಗಳಲ್ಲಿ ಪರಿಸರ 변ಿಲನವನ್ನು ನವೀಕರಿಸಿ

ಪರೀಕ್ಷೆಗಳು ಸಾಮಾನ್ಯವಾಗಿ `monkeypatch.setenv` ಮೂಲಕ ಪರಿಸರ ಬದಲಾಗಿಸುತ್ತವೆ. ಇದನ್ನು ನವೀಕರಿಸಿ:

| ಹಳೆಯ ಪರಿಸರ변ಿಲ | ಹೊಸ ಪರಿಸರ변ಿಲ | ಗಮನಿಕೆಗಳು |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | ಸಾಂಪ್ರದಾಯಿಕ ಆಸ್ಯೂರ್ ಐಡೆಂಟಿಟಿ SDK ಪ್ರಕಾರ |
| `AZURE_OPENAI_VERSION` | ತೆಗೆದುಹಾಕಿ | ಯಾವುದೇ `api_version` ಅಗತ್ಯವಿಲ್ಲ |
| `AZURE_OPENAI_API_VERSION` | ತೆಗೆದುಹಾಕಿ | ಯಾವುದೇ `api_version` ಅಗತ್ಯವಿಲ್ಲ |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | ಉಳಿಸಿ (ಇನ್ನೂ `base_url`ಗಾಗಿ ಬೇಕಾಗಿದೆ) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | ಉಳಿಸಿ (`model` ಪ್ಯಾರಾಮ್‌ಗಾಗಿ ನಿಯೋಜನೆಯ ಹೆಸರು) |

---

## 5. ವರ್ಗಾವಣೆಗೆ ಅಗತ್ಯವಿರುವ ಪರೀಕ್ಷಾ ಕೋಡ್ ಅನ್ನು ಹುಡುಕಿ

```bash
# ಪರೀಕ್ಷಾ ನಿರ್ದಿಷ್ಟ ಹಳೆಯ ಮಾದರಿಗಳು
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