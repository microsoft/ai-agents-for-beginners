# مهاجرت زیرساخت تست

هنگام مهاجرت یک پایگاه کد از Chat Completions به Responses API، **تست‌ها به صورت پیش‌بینی‌پذیری خراب می‌شوند**. این مرجع مواردی که باید اصلاح شوند را پوشش می‌دهد.

---

## شبیه‌سازی پاسخ‌های استریمی (Python pytest)

### کلاس‌های اصلی شبیه‌سازی

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
            # حفظ فاصله‌های سفید: افزودن فاصله به ابتدای همه کلمات به جز کلمه اول
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

### مسیردهی پاسخ‌های شبیه‌سازی شده بر اساس محتوای پیام

برنامه‌های واقعی پاسخ‌های مختلفی بر اساس پرامپت ارائه می‌دهند. مسیردهی بر اساس `input` (نه `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # رابط کاربری پاسخ‌ها از 'input' استفاده می‌کند نه 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### مسیرهای Monkeypatch

| نوع کلاینت | مسیر Monkeypatch |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (همگام) | `openai.resources.responses.Responses.create` |

> **قبل** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **بعد** (Responses): `openai.resources.responses.AsyncResponses.create`

### نمونه کامل پیکربندی

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... کلاس‌های MockResponseEvent و AsyncResponseIterator اینجا ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. به‌روزرسانی پیکربندی‌های شبیه‌سازی شده

جایگزینی شبیه‌سازی‌های مبتنی بر `ChatCompletionChunk` با الگوی `MockResponseEvent` / `AsyncResponseIterator` بالا. تغییرات کلیدی:

| قبل (شبیه‌سازی Chat Completions) | بعد (شبیه‌سازی Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` در chunk | `event.type == "response.completed"` |
| chunk خاص Azure با `prompt_filter_results` | کاملاً حذف شود |
| فیلتر محتوای خاص Azure در هر انتخاب | کاملاً حذف شود |
| `kwargs.get("messages")` در شبیه‌سازی | `kwargs.get("input")` در شبیه‌سازی |

---

## 2. به‌روزرسانی فایل‌های snapshot / golden

اگر مجموعه تست از تست snapshot استفاده می‌کند (مانند `pytest-snapshot`، syrupy، یا snapshotهای JSONL ساخته شده دستی)، شکل خروجی مورد انتظار تغییر می‌کند:

**قبل** (JSONL استریمی Chat Completions):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**بعد** (JSONL استریمی Responses API):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

شکل جدید به طور چشمگیری ساده‌تر است — هیچ فیلد `function_call`، `refusal`، `role`، `tool_calls`، `index`، `logprobs`، یا `content_filter_results` وجود ندارد. همه فایل‌های snapshot را به‌روزرسانی یا بازتولید کنید.

> **نکته**: پس از مهاجرت، با گزینه `--snapshot-update` (pytest-snapshot) یا `--update-snapshots` (syrupy) تست‌ها را اجرا کنید تا به طور خودکار بازتولید شوند.

---

## 3. به‌روزرسانی_assertionهای تست

شکست‌های معمول در assertion:

| assertion قدیمی | مشکل | assertion جدید |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` ویژگی `_azure_ad_token_provider` ندارد | `isinstance(client, AsyncOpenAI)` و `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` دیگر `api_version` ندارد | کامل حذف شود |
| `isinstance(client, AsyncAzureOpenAI)` | نوع کلاینت تغییر کرده است | `isinstance(client, AsyncOpenAI)` |

---

## 4. به‌روزرسانی متغیرهای محیطی در پیکربندی‌های تست

تست‌ها اغلب متغیرهای محیطی را با `monkeypatch.setenv` تنظیم می‌کنند. این‌ها را به‌روزرسانی کنید:

| متغیر محیطی قدیمی | متغیر محیطی جدید | یادداشت‌ها |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | قرارداد استاندارد Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | حذف شود | دیگر نیازی به `api_version` نیست |
| `AZURE_OPENAI_API_VERSION` | حذف شود | دیگر نیازی به `api_version` نیست |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | نگه دارید (برای `base_url` همچنان لازم است) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | نگه دارید (نام استقرار برای پارامتر `model`) |

---

## 5. جستجو برای کد تستی که نیاز به مهاجرت دارد

```bash
# الگوهای قدیمی خاص تست
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
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->