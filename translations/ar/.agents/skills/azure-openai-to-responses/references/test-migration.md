# ترحيل بنية الاختبار التحتية

عند ترحيل قاعدة الشفرة من Chat Completions إلى Responses API، **تفشل الاختبارات بطرق متوقعة**. يغطي هذا المرجع ما يجب إصلاحه.

---

## تمثيل استجابات البث الوهمية (Python pytest)

### الفئات الوهمية الأساسية

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
            # الاحتفاظ بالمسافات البيضاء: أضف مسافة قبل جميع الكلمات ما عدا الكلمة الأولى
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

### توجيه الاستجابات الوهمية حسب محتوى الرسالة

تخدم التطبيقات الحقيقية إجابات مختلفة بناءً على الموجه. وجه حسب `input` (ليس `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # API الردود يستخدم 'input' وليس 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### مسارات التغير المؤقت (Monkeypatch)

| نوع العميل | مسار التغير المؤقت (Monkeypatch) |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (تزامني) | `openai.resources.responses.Responses.create` |

> **قبل** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **بعد** (Responses): `openai.resources.responses.AsyncResponses.create`

### مثال كامل للترتيب الثابت (fixture)

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... فئات MockResponseEvent و AsyncResponseIterator هنا ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. تحديث الترتيبات الوهمية (mock fixtures)

استبدل الوهميات المعتمدة على `ChatCompletionChunk` بنمط `MockResponseEvent` / `AsyncResponseIterator` أعلاه. التغييرات الأساسية:

| قبل (وهمية Chat Completions) | بعد (وهمية Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` في الشظية | `event.type == "response.completed"` |
| شظية `prompt_filter_results` خاصة بـ Azure | إزالة كاملة |
| `content_filter_results` خاصة بـ Azure لكل اختيار | إزالة كاملة |
| `kwargs.get("messages")` في الوهميات | `kwargs.get("input")` في الوهميات |

---

## 2. تحديث ملفات اللقطات / الذهبية

إذا كان طقم الاختبار يستخدم اختبار اللقطات (مثل `pytest-snapshot`، syrupy، أو لقطات JSONL مخصصة)، يتغير شكل الإخراج المتوقع:

**قبل** (بث JSONL لـ Chat Completions):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**بعد** (بث JSONL لـ Responses API):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

الشكل الجديد أبسط بشكل كبير — لا توجد حقول `function_call`، `refusal`، `role`، `tool_calls`، `index`، `logprobs`، أو `content_filter_results`. حدّث أو أعد توليد جميع ملفات اللقطات.

> **نصيحة**: شغّل الاختبارات مع الخيار `--snapshot-update` (pytest-snapshot) أو `--update-snapshots` (syrupy) بعد الترحيل لإعادة التوليد تلقائيًا.

---

## 3. تحديث تأكيدات الاختبار (assertions)

أعطال التأكيد الشائعة:

| تأكيد قديم | المشكلة | تأكيد جديد |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | لا يوجد الخاصية `_azure_ad_token_provider` في `AsyncOpenAI` | `isinstance(client, AsyncOpenAI)` و `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | لا توجد `api_version` على `OpenAI`/`AsyncOpenAI` | إزالة كاملة |
| `isinstance(client, AsyncAzureOpenAI)` | تم تغيير نوع العميل | `isinstance(client, AsyncOpenAI)` |

---

## 4. تحديث متغيرات البيئة في ترتيب الاختبارات

غالبًا ما تضبط الاختبارات متغيرات البيئة عبر `monkeypatch.setenv`. قم بتحديثها كما يلي:

| متغير بيئة قديم | متغير بيئة جديد | ملاحظات |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | اتفاقية معيارية لمكتبة Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | إزالة | لا حاجة لـ `api_version` |
| `AZURE_OPENAI_API_VERSION` | إزالة | لا حاجة لـ `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | استمر في الاستخدام (لا يزال مطلوبًا للـ `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | استمر في الاستخدام (اسم النشر لـ `model` المعامل) |

---

## 5. ابحث عن كود الاختبار الذي يحتاج إلى الترحيل

```bash
# أنماط قديمة خاصة بالاختبار
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
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->