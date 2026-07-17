# Test Infrastructure Migration

When migrating a codebase from Chat Completions to Responses API, **tests break in predictable ways**. This reference covers what to fix.

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
            # Preserve whitespace: prepend space to all words except the first
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

Real apps serve different answers based on the prompt. Route by `input` (not `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API uses 'input' not 'messages'
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
    # ... MockResponseEvent and AsyncResponseIterator classes here ...

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

Replace `ChatCompletionChunk`-based mocks with the `MockResponseEvent` / `AsyncResponseIterator` pattern above. Key changes:

| Before (Chat Completions mock) | After (Responses mock) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` in chunk | `event.type == "response.completed"` |
| Azure-specific `prompt_filter_results` chunk | Remove entirely |
| Azure-specific `content_filter_results` per choice | Remove entirely |
| `kwargs.get("messages")` in mock | `kwargs.get("input")` in mock |

---

## 2. Update snapshot / golden files

If the test suite uses snapshot testing (e.g., `pytest-snapshot`, syrupy, or hand-rolled JSONL snapshots), the expected output shape changes:

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

The new shape is dramatically simpler — no `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, or `content_filter_results` fields. Update or regenerate all snapshot files.

> **Tip**: Run tests with `--snapshot-update` (pytest-snapshot) or `--update-snapshots` (syrupy) after migrating to auto-regenerate.

---

## 3. Update test assertions

Common assertion breakages:

| Old assertion | Problem | New assertion |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` has no `_azure_ad_token_provider` attribute | `isinstance(client, AsyncOpenAI)` and `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | No `api_version` on `OpenAI`/`AsyncOpenAI` | Remove entirely |
| `isinstance(client, AsyncAzureOpenAI)` | Client type changed | `isinstance(client, AsyncOpenAI)` |

---

## 4. Update environment variables in test fixtures

Tests often set env vars via `monkeypatch.setenv`. Update these:

| Old env var | New env var | Notes |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Standard Azure Identity SDK convention |
| `AZURE_OPENAI_VERSION` | Remove | No `api_version` needed |
| `AZURE_OPENAI_API_VERSION` | Remove | No `api_version` needed |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Keep (still needed for `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Keep (deployment name for `model` param) |

---

## 5. Search for test code that needs migration

```bash
# Test-specific legacy patterns
rg "ChatCompletionChunk" tests/
rg "AsyncCompletions\.create" tests/
rg "chat\.completions" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results" tests/
rg "content_filter_results" tests/
rg "AZURE_OPENAI_VERSION|AZURE_OPENAI_API_VERSION" tests/
rg "AZURE_OPENAI_CLIENT_ID" tests/
```
