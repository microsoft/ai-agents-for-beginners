# ٹیسٹ انفراسٹرکچر کی نقل مکانی

جب کسی کوڈ بیس کو چیٹ کمپلیشنز سے ریسپانسز API میں منتقل کیا جاتا ہے، تو **ٹیسٹس متوقع طریقوں سے خراب ہوتے ہیں**۔ یہ حوالہ بتاتا ہے کہ کیا ٹھیک کرنا ہے۔

---

## اسٹریم کرنے والے ریسپانسز کا موک بنانا (Python pytest)

### بنیادی موک کلاسز

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
            # خالی جگہ برقرار رکھیں: پہلے کے علاوہ تمام الفاظ کے شروع میں جگہ شامل کریں
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

### پیغام کے مواد کی بنیاد پر موک ریسپانسز کی روٹنگ

اصلی ایپس پرامپٹ کی بنیاد پر مختلف جوابات دیتے ہیں۔ `input` کے ذریعے روٹ کریں (نہ کہ `messages` کے ذریعے):

```python
async def mock_acreate(*args, **kwargs):
    # جوابات API 'input' استعمال کرتی ہے نہ کہ 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### منکی پیچ پاتھس

| کلائنٹ کی قسم | منکی پیچ پاتھ |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (سنک) | `openai.resources.responses.Responses.create` |

> **پہلے** (چیٹ کمپلیشنز): `openai.resources.chat.AsyncCompletions.create`
> **بعد میں** (ریسپانسز): `openai.resources.responses.AsyncResponses.create`

### مکمل فکچر کی مثال

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent اور AsyncResponseIterator کلاسز یہاں ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. موک فکچرز کو اپ ڈیٹ کریں

`ChatCompletionChunk` پر مبنی موکس کو اوپر بیان کیے گئے `MockResponseEvent` / `AsyncResponseIterator` پیٹرن سے تبدیل کریں۔ اہم تبدیلیاں:

| پہلے (چیٹ کمپلیشنز موک) | بعد (ریسپانسز موک) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` چنک میں | `event.type == "response.completed"` |
| Azure مخصوص `prompt_filter_results` چنک | مکمل طور پر ہٹا دیں |
| Azure مخصوص `content_filter_results` ہر چوائس کے لیے | مکمل طور پر ہٹا دیں |
| موک میں `kwargs.get("messages")` | موک میں `kwargs.get("input")` |

---

## 2. اسنیپ شاٹ / گولڈن فائلز کو اپ ڈیٹ کریں

اگر ٹیسٹ سوئٹ اسنیپ شاٹ ٹیسٹنگ استعمال کرتا ہے (مثلاً `pytest-snapshot`, syrupy، یا ہینڈ رولڈ JSONL اسنیپ شاٹس)، تو متوقع آؤٹ پٹ کی شکل بدلتی ہے:

**پہلے** (چیٹ کمپلیشنز اسٹریم کرنے والے JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**بعد میں** (ریسپانسز API اسٹریم کرنے والے JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

نئی شکل بہ نسبت بہت آسان ہے — کوئی `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, یا `content_filter_results` فیلڈز نہیں۔ تمام اسنیپ شاٹ فائلز کو اپ ڈیٹ یا دوبارہ بنائیں۔

> **تجویز**: نقل مکانی کے بعد خودکار دوبارہ جنریشن کے لیے `--snapshot-update` (pytest-snapshot) یا `--update-snapshots` (syrupy) کے ساتھ ٹیسٹ چلائیں۔

---

## 3. ٹیسٹ اسیرشنز کو اپ ڈیٹ کریں

عام اسیرشن خرابیاں:

| پرانی اسیرشن | مسئلہ | نئی اسیرشن |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` میں `_azure_ad_token_provider` ایٹریبیوٹ نہیں ہے | `isinstance(client, AsyncOpenAI)` اور `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` پر `api_version` نہیں ہے | مکمل طور پر ہٹا دیں |
| `isinstance(client, AsyncAzureOpenAI)` | کلائنٹ کی قسم بدل گئی ہے | `isinstance(client, AsyncOpenAI)` |

---

## 4. ٹیسٹ فکچر میں ماحولیاتی متغیرات کو اپ ڈیٹ کریں

ٹیسٹس عموماً `monkeypatch.setenv` کے ذریعے env vars سیٹ کرتے ہیں۔ ان کو اپ ڈیٹ کریں:

| پرانا env var | نیا env var | نوٹس |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | معیاری Azure شناخت SDK کنونشن |
| `AZURE_OPENAI_VERSION` | ہٹا دیں | `api_version` کی ضرورت نہیں |
| `AZURE_OPENAI_API_VERSION` | ہٹا دیں | `api_version` کی ضرورت نہیں |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | رکھیں (اب بھی `base_url` کے لیے ضروری) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | رکھیں (`model` پیرا میٹر کے لیے ڈپلائمنٹ کا نام) |

---

## 5. ایسے ٹیسٹ کوڈ کی تلاش کریں جسے نقل مکانی کی ضرورت ہو

```bash
# ٹیسٹ مخصوص وراثتی پیٹرنز
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
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->