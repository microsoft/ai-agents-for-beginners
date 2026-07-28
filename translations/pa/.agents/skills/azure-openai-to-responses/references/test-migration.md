# ਟੈਸਟ ਢਾਂਚਾ ਮਾਈਗ੍ਰੇਸ਼ਨ

ਜਦੋਂ ਕੋਡਬੇਸ ਨੂੰ Chat Completions ਤੋਂ Responses API ਵਿੱਚ ਮਾਈਗ੍ਰੇਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, **ਟੈਸਟ ਪਰੇਡਿਕਟੇਬਲ ਢੰਗ ਨਾਲ ਟੁੱਟ ਜਾਂਦੇ ਹਨ**। ਇਹ ਸੰਦਰਭ ਇਸ ਗੱਲ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ ਕਿ ਕੀ ਠੀਕ ਕਰਨਾ ਹੈ।

---

## ਸਟ੍ਰੀਮਿੰਗ ਜਵਾਬਾਂ ਦੀ ਮੌਕਿੰਗ (Python pytest)

### ਮੁੱਖ ਮੌਕ ਕਲਾਸਾਂ

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
            # ਵ੍ਹਾਈਟਸਪੇਸ ਨੂੰ ਸੰਭਾਲੋ: ਪਹਿਲੇ ਸ਼ਬਦ ਤੋਂ ਇਲਾਵਾ ਸਾਰੇ ਸ਼ਬਦਾਂ ਦੇ ਅੱਗੇ ਸਪੇਸ ਜੋੜੋ
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

### ਸੁਨੇਹੇ ਦੀ ਸਮੱਗਰੀ ਅਨੁਸਾਰ ਰੂਟਿੰਗ ਮੌਕ ਜਵਾਬ

ਅਸਲ ਐਪ ਵੱਖ ਵੱਖ ਉੱਤਰ ਦਿੰਦੇ ਹਨ ਜੋ ਪ੍ਰਾਂਪਟ 'ਤੇ ਅਧਾਰਿਤ ਹਨ। `input` (ਨਾ ਕਿ `messages`) ਨਾਲ ਰੂਟ ਕਰੋ:

```python
async def mock_acreate(*args, **kwargs):
    # Responses API 'input' ਵਰਤਦਾ ਹੈ ਨਾ ਕਿ 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### ਮੰਕੀਪੈਚ ਪਾਥ

| ਕਲਾਇੰਟ ਕਿਸਮ | ਮੰਕੀਪੈਚ ਪਾਥ |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (ਸਿੰਕ) | `openai.resources.responses.Responses.create` |

> **ਪਹਿਲਾਂ** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **ਬਾਅਦ** (Responses): `openai.resources.responses.AsyncResponses.create`

### ਪੂਰਾ ਫਿਕਸਚਰ ਉਦਾਹਰਣ

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... ਇਥੇ MockResponseEvent ਅਤੇ AsyncResponseIterator ਕਲਾਸਾਂ ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. ਮੌਕ ਫਿਕਸਚਰ ਅੱਪਡੇਟ ਕਰੋ

`ChatCompletionChunk`-ਆਧਾਰਿਤ ਮੌਕ ਨੂੰ ਉੱਪਰ ਦਿੱਤੇ `MockResponseEvent` / `AsyncResponseIterator` ਪੈਟਰਨ ਨਾਲ ਬਦਲੋ। ਮੁੱਖ ਬਦਲਾਅ:

| ਪਹਿਲਾਂ (Chat Completions ਮੌਕ) | ਬਾਅਦ (Responses ਮੌਕ) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| ਚੰਕ ਵਿੱਚ `finish_reason="stop"` | `event.type == "response.completed"` |
| ਏਜ਼ੁਰ ਵਿਸ਼ੇਸ਼ `prompt_filter_results` ਚੰਕ | ਪੂਰੀ ਤਰ੍ਹਾਂ ਹਟਾਓ |
| ਪ੍ਰਤੀ ਚੋਣ ਏਜ਼ੁਰ ਵਿਸ਼ੇਸ਼ `content_filter_results` | ਪੂਰੀ ਤਰ੍ਹਾਂ ਹਟਾਓ |
| ਮੌਕ ਵਿੱਚ `kwargs.get("messages")` | ਮੌਕ ਵਿੱਚ `kwargs.get("input")` |

---

## 2. ਸ્નੈਪਸ਼ਾਟ / ਗੋਲਡਨ ਫਾਈਲਾਂ ਅੱਪਡੇਟ ਕਰੋ

ਜੇ ਟੈਸਟ ਸੂਟ ਸਨੈਪਸ਼ਾਟ ਟੈਸਟਿੰਗ ਵਰਗਾ ਵਰਤਦਾ ਹੈ (ਉਦਾਹਰਣ ਲਈ, `pytest-snapshot`, syrupy, ਜਾਂ ਹੱਥ ਨਾਲ ਬਣਾਈ JSONL ਸਨੈਪਸ਼ਾਟ ), ਉਮੀਦ ਕੀਤੀ ਗਈ ਆਉਟਪੁੱਟ ਦੀ ਸ਼ਕਲ ਬਦਲਦੀ ਹੈ:

**ਪਹਿਲਾਂ** (Chat Completions ਸਟ੍ਰੀਮਿੰਗ JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**ਬਾਅਦ** (Responses API ਸਟ੍ਰੀਮਿੰਗ JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

ਨਵੀਂ ਸ਼ਕਲ ਬਹੁਤ ਹੀ ਸਧਾਰਣ ਹੈ — ਕੋਈ `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, ਜਾਂ `content_filter_results` ਫੀਲਡ ਨਹੀਂ। ਸਭ ਸਨੈਪਸ਼ਾਟ ਫਾਈਲਾਂ ਅੱਪਡੇਟ ਜਾਂ ਦੁਬਾਰਾ ਬਣਾਓ।

> **ਸੁਝਾਅ**: ਮਾਈਗ੍ਰੇਟ ਕਰਨ ਤੋਂ ਬਾਅਦ ਟੈਸਟ ਨੂੰ `--snapshot-update` (pytest-snapshot) ਜਾਂ `--update-snapshots` (syrupy) ਨਾਲ ਚਲਾਓ ਤਾਂ ਜੋ ਇਹ ਆਪਣੇ ਆਪ ਨਵੀਆਂ ਸਨੈਪਸ਼ਾਟ ਤਿਆਰ ਕਰ ਲਵੇ।

---

## 3. ਟੈਸਟ ਅਸਰਸ਼ਨ ਅੱਪਡੇਟ ਕਰੋ

ਆਮ ਅਸਰਸ਼ਨ ਬਿਗੜਨ:

| ਪੁਰਾਣਾ ਅਸਰਸ਼ਨ | ਸਮੱਸਿਆ | ਨਵਾਂ ਅਸਰਸ਼ਨ |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` ਕੋਲ `_azure_ad_token_provider` ਐਟ੍ਰਿਬਿਊਟ ਨਹੀਂ | `isinstance(client, AsyncOpenAI)` ਅਤੇ `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` ਤੇ ਕੋਈ `api_version` ਨਹੀਂ | ਪੂਰੀ ਤਰ੍ਹਾਂ ਹਟਾਓ |
| `isinstance(client, AsyncAzureOpenAI)` | ਕਲਾਇੰਟ ਕਿਸਮ ਬਦਲੀ ਹੈ | `isinstance(client, AsyncOpenAI)` |

---

## 4. ਟੈਸਟ ਫਿਕਸਚਰ ਵਿਚ ਵਾਤਾਵਰਨ ਵੈਰੀਏਬਲ ਅੱਪਡੇਟ ਕਰੋ

ਟੈਸਟ ਅਕਸਰ `monkeypatch.setenv` ਰਾਹੀਂ env vars ਸੈੱਟ ਕਰਦੇ ਹਨ। ਇਹਨਾਂ ਨੂੰ ਅੱਪਡੇਟ ਕਰੋ:

| ਪੁਰਾਣਾ env var | ਨਵਾਂ env var | ਨੋਟਸ |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | ਮਿਆਰੀ ਏਜ਼ੁਰ ਆਈਡੈਂਟੀਟੀ SDK ਕਨਵੇਂਸ਼ਨ |
| `AZURE_OPENAI_VERSION` | ਹਟਾਓ | ਕੋਈ `api_version` ਲੋੜੀਂਦੀ ਨਹੀਂ |
| `AZURE_OPENAI_API_VERSION` | ਹਟਾਓ | ਕੋਈ `api_version` ਲੋੜੀਂਦੀ ਨਹੀਂ |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | ਰੱਖੋ (ਹੁਣ ਵੀ `base_url` ਲਈ ਜ਼ਰੂਰੀ) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | ਰੱਖੋ (`model` ਪੈਰਾਮੀਟਰ ਲਈ ਡਿਪਲੋਇਮੈਂਟ ਨਾਮ) |

---

## 5. ਮਾਈਗਰੇਸ਼ਨ ਲਈ ਟੈਸਟ ਕੋਡ ਦੀ ਖੋਜ ਕਰੋ

```bash
# ਟੈਸਟ-ਵਿਸ਼ੇਸ਼ ਪੁਰਾਣੇ ਪੈਟਰਨ
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
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->