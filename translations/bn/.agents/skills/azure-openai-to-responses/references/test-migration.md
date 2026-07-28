# টেস্ট অবকাঠামোর মাইগ্রেশন

যখন একটি কোডবেস Chat Completions থেকে Responses API তে মাইগ্রেট করা হয়, **টেস্টগুলি পূর্বানুমিত উপায়ে ভেঙে যায়**। এই রেফারেন্সে কী ঠিক করতে হবে তা আলোচনা করা হয়েছে।

---

## স্ট্রিমিং রেসপন্স (Python pytest) মক করা

### প্রধান মক ক্লাসসমূহ

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
            # স্পেস সংরক্ষণ করুন: প্রথম শব্দ ছাড়া সব শব্দের আগে স্পেস যোগ করুন
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

### মেসেজ কন্টেন্ট দ্বারা মক রেসপন্স রাউটিং করা

বাস্তব অ্যাপ্লিকেশনগুলো প্রম্পটের ভিত্তিতে বিভিন্ন উত্তর প্রদান করে। `input` দ্বারা রাউট করুন (না `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API 'input' ব্যবহার করে 'messages' নয়
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### মাঙ্কিপ্যাচ পথসমূহ

| ক্লায়েন্ট টাইপ | মাঙ্কিপ্যাচ পথ |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (sync) | `openai.resources.responses.Responses.create` |

> **আগে** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **পরে** (Responses): `openai.resources.responses.AsyncResponses.create`

### পূর্ণ ফিক্সচার উদাহরণ

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent এবং AsyncResponseIterator ক্লাসগুলি এখানে ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## ১। মক ফিক্সচার আপডেট করুন

`ChatCompletionChunk`-ভিত্তিক মকগুলিকে উপরের `MockResponseEvent` / `AsyncResponseIterator` প্যাটার্ন দিয়ে প্রতিস্থাপন করুন। মূল পরিবর্তনগুলি:

| আগে (Chat Completions মক) | পরে (Responses মক) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` ইন চঙ্ক | `event.type == "response.completed"` |
| Azure-নির্দিষ্ট `prompt_filter_results` চঙ্ক | সম্পূর্ণরূপে অপসারণ করুন |
| Azure-নির্দিষ্ট `content_filter_results` প্রতি চয়েস | সম্পূর্ণরূপে অপসারণ করুন |
| মকে `kwargs.get("messages")` | মকে `kwargs.get("input")` |

---

## ২। স্ন্যাপশট / গোল্ডেন ফাইল আপডেট করুন

যদি টেস্ট স্যুট স্ন্যাপশট টেস্টিং ব্যবহার করে (যেমন `pytest-snapshot`, syrupy, বা নিজস্ব JSONL স্ন্যাপশট), প্রত্যাশিত আউটপুটের গঠন পরিবর্তিত হয়:

**আগে** (Chat Completions স্ট্রিমিং JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**পরে** (Responses API স্ট্রিমিং JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

নতুন গঠন অত্যন্ত সরল — কোন `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, অথবা `content_filter_results` ক্ষেত্র নেই। সব স্ন্যাপশট ফাইল আপডেট করুন বা পুনরুজ্জীবিত করুন।

> **টিপ**: মাইগ্রেশনের পরে স্বয়ংক্রিয় পুনর্গঠনের জন্য `--snapshot-update` (pytest-snapshot) অথবা `--update-snapshots` (syrupy) দিয়ে টেস্ট চালান।

---

## ৩। টেস্ট আশ্বাসন আপডেট করুন

সাধারণ আশ্বাসন ভঙ্গ:

| পুরাতন আশ্বাসন | সমস্যা | নতুন আশ্বাসন |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` এ `_azure_ad_token_provider` attribute নেই | `isinstance(client, AsyncOpenAI)` এবং `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` এ `api_version` নেই | সম্পূর্ণরূপে সরিয়ে দিন |
| `isinstance(client, AsyncAzureOpenAI)` | ক্লায়েন্ট টাইপ বদলেছে | `isinstance(client, AsyncOpenAI)` |

---

## ৪। টেস্ট ফিক্সচারে পরিবেশ ভেরিয়েবল আপডেট করুন

টেস্টগুলো প্রায়শই `monkeypatch.setenv` এর মাধ্যমে env var সেট করে। এগুলো আপডেট করুন:

| পুরাতন env var | নতুন env var | নোটস |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | স্ট্যান্ডার্ড Azure Identity SDK রীতি |
| `AZURE_OPENAI_VERSION` | অপসারণ করুন | কোন `api_version` দরকার নেই |
| `AZURE_OPENAI_API_VERSION` | অপসারণ করুন | কোন `api_version` দরকার নেই |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | রাখুন (এখনো `base_url` এর জন্য দরকার) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | রাখুন (`model` প্যারামের জন্য ডিপ্লয়মেন্ট নাম) |

---

## ৫। যে টেস্ট কোড মাইগ্রেশন প্রয়োজন তা অনুসন্ধান করুন

```bash
# পরীক্ষার-নির্দিষ্ট ঐতিহ্যবাহী প্যাটার্নগুলি
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
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->