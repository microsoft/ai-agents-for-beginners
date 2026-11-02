# מעבר תשתית בדיקות

בעת מעבר בסיס קוד מ-Chat Completions ל-Responses API, **הבדיקות נשברות בדרכים צפויות**. הפניה הזו מכסה מה צריך לתקן.

---

## זיווג תגובות סטרימינג (pytest בפייתון)

### מחלקות זיווג מרכזיות

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
            # לשמור על רווחים: להוסיף רווח לפני כל מילים מלבד הראשונה
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

### ניתוב תגובות מזורגות לפי תוכן ההודעה

אפליקציות אמיתיות מגישות תשובות שונות לפי הפקודה. נווט לפי `input` (ולא `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # ממשק התגובות משתמש ב'input' ולא ב'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### נתיבי מונקיפאץ'

| סוג לקוח | נתיב מונקיפאץ' |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (סינכרוני) | `openai.resources.responses.Responses.create` |

> **לפני** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **אחרי** (Responses): `openai.resources.responses.AsyncResponses.create`

### דוגמת תיקון מלאה

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... מחלקות MockResponseEvent ו-AsyncResponseIterator כאן ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. עדכון תיקוני דמה

החלף זיווגים המבוססים על `ChatCompletionChunk` בתבנית `MockResponseEvent` / `AsyncResponseIterator` שמעלה. שינויים עיקריים:

| לפני (זיווג Chat Completions) | אחרי (זיווג Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` ב-chunk | `event.type == "response.completed"` |
| chunk ספציפי ל-Azure בשם `prompt_filter_results` | הסר לחלוטין |
| `content_filter_results` ספציפי ל-Azure לכל בחירה | הסר לחלוטין |
| `kwargs.get("messages")` בזיווג | `kwargs.get("input")` בזיווג |

---

## 2. עדכון קבצי סנאפשוט / גולדן

אם מארז הבדיקות משתמש בבחינת סנאפשוט (למשל, `pytest-snapshot`, syrupy, או סנאפשוט JSONL בעבודת יד), צורת הפלט הצפויה משתנה:

**לפני** (סטרימינג JSONL של Chat Completions):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**אחרי** (סטרימינג JSONL של Responses API):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

הצורה החדשה פשוטה באופן דרמטי — ללא שדות `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, או `content_filter_results`. עדכן או הפקד מחדש את כל קבצי הסנאפשוט.

> **טיפ**: הרץ בדיקות עם `--snapshot-update` (pytest-snapshot) או `--update-snapshots` (syrupy) אחרי המעבר כדי לחדש אוטומטית.

---

## 3. עדכון הטענות בבדיקות

תקלות נפוצות בהטענות:

| הטענה ישנה | בעיה | הטענה חדשה |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | ל-`AsyncOpenAI` אין תכונה `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` ו-`"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | אין `api_version` ב-`OpenAI`/`AsyncOpenAI` | הסר לחלוטין |
| `isinstance(client, AsyncAzureOpenAI)` | סוג הלקוח השתנה | `isinstance(client, AsyncOpenAI)` |

---

## 4. עדכון משתני סביבה בתיקוני בדיקה

בדיקות לעיתים מגדירות משתני סביבה דרך `monkeypatch.setenv`. עדכן את אלה:

| משתנה סביבה ישן | משתנה סביבה חדש | הערות |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | קונבנציית SDK זהות Azure סטנדרטית |
| `AZURE_OPENAI_VERSION` | הסר | אין צורך ב-`api_version` |
| `AZURE_OPENAI_API_VERSION` | הסר | אין צורך ב-`api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | שמור (עדיין דרוש ל-`base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | שמור (שם פריסה לפרמטר `model`) |

---

## 5. חפש קוד בדיקה שצריך מעבר

```bash
# תבניות מורשת ספציפיות למבחן
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
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->