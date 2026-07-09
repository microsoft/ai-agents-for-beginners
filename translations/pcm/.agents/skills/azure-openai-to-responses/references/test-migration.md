# Test Infraestructure Migration

When you dey migrate codebase from Chat Completions go Responses API, **tests go break for ways wey you fit predict**. Dis refence go show wetin to fix.

---

## Mocking Streaming Responses (Python pytest)

### Core mock classes

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
            # Make space dey: put space before all word dem except di first one
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

### Routing mock responses by message content

Real apps dey serve different answers based on prompt. Route by `input` (no be `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API de use 'input' no be 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch paths

| Client type | Monkeypatch path |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **Before** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **After** (Responses): `openai.resources.responses.AsyncResponses.create`

### Full fixture example

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent and AsyncResponseIterator classes dey here ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Update mock fixtures

Replace `ChatCompletionChunk`-based mocks with the `MockResponseEvent` / `AsyncResponseIterator` pattern wey dey top. Key changes:

| Before (Chat Completions mock) | After (Responses mock) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` inside chunk | `event.type == "response.completed"` |
| Azure-specific `prompt_filter_results` chunk | Remove am full |
| Azure-specific `content_filter_results` per choice | Remove am full |
| `kwargs.get("messages")` for mock | `kwargs.get("input")` for mock |

---

## 2. Update snapshot / golden files

If test suite dey use snapshot testing (e.g., `pytest-snapshot`, syrupy, or hand-rolled JSONL snapshots), the expected output shape don change:

**Before** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**After** (Responses API streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

The new shape na serious simple — no `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, or `content_filter_results` fields again. Update or regenerate all snapshot files.

> **Tip**: Run tests with `--snapshot-update` (pytest-snapshot) or `--update-snapshots` (syrupy) after you don migrate so dat e go auto-regenerate.

---

## 3. Update test assertions

Common assertion breaks:

| Old assertion | Wahala | New assertion |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` no get `_azure_ad_token_provider` attribute | `isinstance(client, AsyncOpenAI)` and `"/openai/v1/" dey inside str(client.base_url)` |
| `client.api_version == "2024-..."` | No `api_version` on `OpenAI`/`AsyncOpenAI` | Remove am full |
| `isinstance(client, AsyncAzureOpenAI)` | Client type don change | `isinstance(client, AsyncOpenAI)` |

---

## 4. Update environment variables for test fixtures

Tests dey often set env vars via `monkeypatch.setenv`. Update these ones:

| Old env var | New env var | Notes |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Standard Azure Identity SDK convention |
| `AZURE_OPENAI_VERSION` | Remove am | No `api_version` needed |
| `AZURE_OPENAI_API_VERSION` | Remove am | No `api_version` needed |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Keep am (still dey needed for `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Keep am (deployment name for `model` param) |

---

## 5. Search for test code wey need migration

```bash
# Test-specific old-style patterns
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
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->