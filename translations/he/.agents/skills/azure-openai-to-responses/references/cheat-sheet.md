# דף רמאות API תגובות (Python + Azure OpenAI)

> כל הקטעים למטה מניחים ש־`deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` ו־`client` כבר מאותחל (ראה הגדרת הלקוח).

## בקשה בסיסית
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## הגדרת לקוח — EntraID (מומלץ)
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = OpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## הגדרת לקוח — מפתח API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## הגדרת לקוח אסינכרוני — EntraID
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AsyncOpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## הגדרת לקוח אסינכרוני — EntraID עם שוכר מפורש (רב-שוכרים)

כאשר משאב Azure OpenAI נמצא ב**שוכר שונה** מהברירת מחדל, העבר `tenant_id` במפורש לאישור. זה שכיח בתרחישי פיתוח/בדיקה שבהם שוכר הבית של המפתח שונה מזה של המשאב.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential לייצור (אזור אשכול מכולות Azure, שירות אפליקציות וכו')
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # זהות מנוהלת שהוקצתה למשתמש
)
# AzureDeveloperCliCredential לפיתוח מקומי — tenant_id מפורש הוא קריטי
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# שרשרת: נסה תחילה זהות מנוהלת, חזור לשורת הפקודה azd
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## מעבר לקוח אסינכרוני — לפני/אחרי

לפני (מיושן):
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

אחרי:
```python
from openai import AsyncOpenAI

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)

resp = await client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## מעבר סינכרוני מלא — לפני/אחרי

לפני (מסורתי — Chat Completions של Azure OpenAI):
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

אחרי (Responses API — נקודת הקצה של Azure OpenAI v1):
```python
from openai import OpenAI
import os

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## הזרמת טקסט (סינכרוני)
```python
stream = client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()  # מעבר שורה בסוף
```

## הזרמת טקסט (אסינכרוני)
```python
stream = await client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
async for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()
```

## הזרמה באפליקציית ווב — צורת backend ל־frontend

בעת מעבר אפליקציית ווב עם שידורי SSE/JSONL ל־frontend, תבנית הסריאליזציה של ה־backend משתנה. עצב את הפלט החדש של ה־backend לשמור על דפוסי הגישה הקיימים של ה־frontend כך שלא נדרשות שינויים ב־frontend.

**לפני** — Backend של Chat Completions בדרך כלל סיריאליזציה של המילון `choices[0]` של כל מקטע:
```python
# ישן: מילון בחירה מלא בסידור טורי לכל מקטע
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend קורא: `response.delta.content` (מסלול עמוק בתוך אובייקט הבחירה).

**אחרי** — Backend של Responses API מפיק צורה מינימלית שומרת על אותו מסלול גישה ב־frontend:
```python
# חדש: להוציא לפועל רק את מה שהחזית צריכה
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend קורא עדיין `response.delta.content` — **אין צורך בשינויים ב־frontend**.

> **תובנה מרכזית**: צורת הזרמת Responses API (`event.type` + `event.delta`) שונה יסודית מ־Chat Completions (`chunk.choices[0].delta.content`). אבל חוזה ה־backend ל־frontend הוא שלכם להגדיר. עצבו את הפלט של ה־backend כך שיתאים למה שה־frontend כבר מצפה לו.

## רצף אירועי הזרמה

כאשר `stream: true`, ה־API מפיק אירועים בסדר הבא:
1. `response.created` – אובייקט התגובה אותחל
2. `response.in_progress` – יצירת התגובה החלה
3. `response.output_item.added` – פריט פלט נוצר
4. `response.content_part.added` – התחלת חלק תוכן
5. `response.output_text.delta` – מקטעי טקסט (רבים, כל אחד עם `delta: string`)
6. `response.output_text.done` – סיום יצירת הטקסט
7. `response.content_part.done` – סיום חלק התוכן
8. `response.output_item.done` – סיום פריט הפלט
9. `response.completed` – תגובה מלאה הושלמה

עבור הזרמת טקסט בסיסית, יש לטפל רק ב־`response.output_text.delta` (עבור מקטעי הטקסט) ו־`response.completed` (לסיום).

## טיפול בשגיאות הזרמה באפליקציות ווב

בעת הזרמה באפליקציית ווב, עטפו את האיטרציה האסינכרונית ב־`try/except` והחזירו שגיאות כ־JSON כדי שה־frontend יוכל להציגן בצורה נעימה (למשל, מגבלות תעבורה, כשל זמני):

```python
@stream_with_context
async def response_stream():
    chat_coroutine = client.responses.create(
        model=deployment,
        input=all_messages,
        max_output_tokens=1000,
        stream=True,
        store=False,
    )
    try:
        async for event in await chat_coroutine:
            if event.type == "response.output_text.delta":
                yield json.dumps({"delta": {"content": event.delta}}) + "\n"
            elif event.type == "response.completed":
                yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
    except Exception as e:
        current_app.logger.error(e)
        yield json.dumps({"error": str(e)}) + "\n"
```

> **למה זה חשוב**: Azure OpenAI מחזירה `429 Too Many Requests` בעת הגבלת תעבורה. ללא `try/except` התשובה בזרם מתה בשקט. איתה, ה־frontend מקבל `{"error": "Too Many Requests"}` ויכול להציג בקשת ניסיון חוזר.

## סוגי אירועי הזרמה (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## פורמט שיחה
```python
# ממשק התגובות תומך בפורמט שיחה באמצעות מערך קלט
response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are an Azure cloud architect."},
        {"role": "user", "content": "Design a scalable web application architecture."},
    ],
    max_output_tokens=1000,
)
print(response.output_text)
```

## טיפול בשגיאות מסנן תוכן

מבנה גוף השגיאה השתנה מ־Chat Completions ל־Responses API.

לפני (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

אחרי (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

הבדלים עיקריים:
- עטיפת `innererror` **נעלמה** — פרטי מסנן התוכן נמצאים כעת ברמת השגיאה העליונה של `error.body`.
- `content_filter_result` (יחיד) → `content_filters` (מערך רבים) הכולל `content_filter_results` (רבים) בתוך כל כניסה.
- כל כניסה ב־`content_filters` כוללת `blocked`, `source_type`, ו־`content_filter_results` עם פרטים לפי קטגוריה (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

מבנה גוף שגיאה של מסנן תוכן ב־Responses API במלואו:
```json
{
  "message": "The response was filtered...",
  "type": "invalid_request_error",
  "param": "prompt",
  "code": "content_filter",
  "content_filters": [
    {
      "blocked": true,
      "source_type": "prompt",
      "content_filter_results": {
        "jailbreak": { "detected": true, "filtered": true },
        "hate": { "filtered": false, "severity": "safe" },
        "sexual": { "filtered": false, "severity": "safe" },
        "violence": { "filtered": false, "severity": "safe" },
        "self_harm": { "filtered": false, "severity": "safe" }
      }
    }
  ]
}
```

## מעבר HTTP גולמי (requests/httpx)

אם האפליקציה קוראת ישירות ל־REST של Azure OpenAI במקום להשתמש ב־SDK:

לפני (Chat Completions):
```python
endpoint = f"{azure_endpoint}/openai/deployments/{deployment}/chat/completions?api-version=2024-03-01-preview"
data = {
    "messages": [{"role": "user", "content": query}],
    "model": model_name,
    "temperature": 0,
}
response = requests.post(endpoint, headers=headers, json=data)
message = response.json()["choices"][0]["message"]["content"]
```

אחרי (Responses API):
```python
endpoint = f"{azure_endpoint}/openai/v1/responses"
data = {
    "model": deployment,
    "input": [{"role": "user", "content": query}],
    "temperature": 0,
    "max_output_tokens": 1000,
    "store": False,
}
response = requests.post(endpoint, headers=headers, json=data)
output_text = response.json()["output"][0]["content"][0]["text"]
```

> **הערה**: `output_text` היא תכונה נוחה באובייקט `Response` ב־Python SDK. תגובת JSON גולמית ב־REST אינה מכילה שדה `output_text` ברמת עליונה — הטקסט נמצא ב־`output[0].content[0].text`.

## שיחה מרובת סיבובים
```python
# לבנות שיחה עם API תגובות
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# להוסיף את תגובת העוזר לשיחה
messages.append({"role": "assistant", "content": response.output_text})

# להמשיך את השיחה
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

שיחה מרובת סיבובים עם טיפוס תוכן (`input_text`/`output_text` מפורשים):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### שיחה מרובת סיבובים באמצעות `previous_response_id` (אלטרנטיבי)

במקום לנהל את מערך השיחה בעצמכם, ניתן לקשר תגובות
בצד השרת באמצעות `previous_response_id`. ה־API שומר כל תגובה ומוסיף אוטומטית את התורות הקודמים.


```python
# סיבוב ראשון
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# סיבובים הבאים — פשוט העבר את ההודעה החדשה של המשתמש + מזהה התגובה הקודמת
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**מתי להשתמש באיזו שיטה:**

| גישה | יתרונות | חסרונות |
|---|---|---|
| מערך `input` (ידני) | שליטה מלאה על ההיסטוריה; אפשר לקצר/לסכם; אין צורך באחסון צד שרת (`store=False`) | יותר קוד; את/ה מנהל/ת את המערך |
| `previous_response_id` | קוד פשוט יותר; שרשור אוטומטי | דורש `store=True` (ברירת מחדל); שיחה נשמרת בצד השרת; אי אפשר לשנות היסטוריה בין הסיבובים |

> **הערת מעבר:** רוב אפליקציות Chat Completions כבר מנהלות את מערך ההודעות שלהן, לכן המרה למערך `input` היא מעבר ישיר 1:1. השתמשו ב־`previous_response_id` לקוד חדש או כשאין צורך במניפולציה של היסטוריית השיחה.

## דגמי הסברה סדרה O (o1, o3-mini, o3, o4-mini)

לדגמי סדרה O יש מגבלות פרמטרים ייחודיות בעת המעבר ל־Responses API.

### מיפוי פרמטרים לסדרת O

| Chat Completions (סדרת O) | Responses API | הערות |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | קבע גבוה (4096+) — טוקנים להסברה נספרים במגבלה |
| `reasoning_effort` | `reasoning.effort` | השאר כפי שהוא אם קיים (נמוך/בינוני/גבוה) |
| `temperature` | הסר או קבע ל־`1` | סדרת O מקבלת רק `1` |
| `top_p` | הסר | לא נתמך בסדרת O |
| `seed` | הסר | לא נתמך ב־Responses API |

### סדרת O לפני/אחרי

לפני (Chat Completions עם סדרת O):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

אחרי (Responses API):
```python
resp = client.responses.create(
    model=deployment,
    input="Solve this step by step: 2x + 5 = 13",
    max_output_tokens=4096,
    reasoning={"effort": "medium"},
    store=False,
)
print(resp.output_text)
```

> **הערה**: לדגמי סדרת O עשוי להיות מאגר פלט בזמן ההסברה לפני שהם מפיקים דלתות טקסט. הזרמה עדיין עובדת אך אירוע ה־`response.output_text.delta` הראשון עשוי להגיע באיחור ארוך יותר מאשר בדגמי GPT.

## גישה לטוקנים של הסברה
```python
# מודלים של הסקת מסיקים משתמשים בהסקה פנימית — אתה יכול לראות כמה אסימוני הסקה שומשו
response = client.responses.create(
    model=deployment,
    input="Explain quantum computing in simple terms",
    max_output_tokens=1000,
)
print(response.output_text)
print(f"Status: {response.status}")
print(f"Reasoning tokens: {response.usage.output_tokens_details.reasoning_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
```

> **חשוב**: השתמש ב־`max_output_tokens=1000` (ולא 50–200) כדי לקחת בחשבון את תהליך ההסברה הפנימי של דגמי ההסברה. המודל משתמש בטוקני הסברה פנימיים לפני יצירת הפלט הסופי.

## פלט מובנה — סכמת JSON
```python
resp = client.responses.create(
    model=deployment,
    input="What is the capital of France?",
    max_output_tokens=500,
    text={
        "format": {
            "type": "json_schema",
            "name": "Output",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {"answer": {"type": "string"}},
                "required": ["answer"],
                "additionalProperties": False,
            },
        }
    },
    store=False,
)
import json
data = json.loads(resp.output_text)
print(data["answer"])
```

## שימוש בכלים

- הגדר פונקציות ב־`tools` עם **פורמט Responses API שטוח** — `name`, `description`, ו־`parameters` ברמה עליונה (לא מקוננים תחת `function`).
- כאשר המודל מבקש לקרוא לכלי, הפעל אותו באפליקציה שלך וכלול את תוצאת הכלי בבקשה הבאה כפריט `function_call_output` בתוך `input`.
- שמור על סכמות מינימליות; אמת קלטים לפני ביצוע.
- בעת שימוש ב־`strict: true`, כל התכונות חייבות להיות ברשימת `required` ו־`additionalProperties: false` הוא חובה.

> **⚠️ `pydantic_function_tool()` אינה תואמת**: הפונקציה העזר `openai.pydantic_function_tool()` עדיין מייצרת את פורמט Chat Completions המקונן הישן (`{"type": "function", "function": {"name": ...}}`). אין להשתמש בה עם `responses.create()`. הגדירו סכמות כלים ידנית או כתבו עטיפה להשטחת הפלט.

### פורמט הגדרת כלי

ה־Responses API משתמש בפורמט כלי **שטוח** — `name`, `description`, `parameters` הם מפתחות ברמה עליונה (לא מקוננים תחת `function`).

**לפני (Chat Completions — מקונן):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**אחרי (Responses API — שטוח):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

דוגמה מלאה:
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are a weather chatbot."},
        {"role": "user", "content": "What's the weather in Berkeley?"},
    ],
    tools=tools,
    tool_choice="auto",
    store=False,
)
```

עם `strict: true` (אכיפת סכימה):
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],       # על כל התכונות להיות רשומות
            "additionalProperties": False,   # דרוש במצב קפדני
        },
    }
]
```

### סבב קריאת כלי (ביצוע והחזרת תוצאות)

כאשר המודל מבקש קריאת כלי, השתמש בפריטי `response.output` + `function_call_output` — **לא** בדפוס Chat Completions של `role: assistant` + `role: tool`.

```python
import json

messages = [
    {"role": "system", "content": "You are a weather chatbot."},
    {"role": "user", "content": "Is it sunny in Berkeley?"},
]

response = client.responses.create(
    model=deployment, input=messages, tools=tools, store=False,
)

tool_calls = [item for item in response.output if item.type == "function_call"]
if tool_calls:
    # הוסף את פריטי קריאת הפונקציה של המודל לשיחה
    messages.extend(response.output)

    # בצע כל כלי והוסף את התוצאות
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # קבל תגובה סופית עם תוצאות הכלים
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### דוגמאות קריאת כלי ב־few-shot

בעת מתן דוגמאות מעטות לקריאות כלים ב־`input`, השתמש בפריטי `function_call` ו־`function_call_output`. המזהים חייבים להתחיל ב־`fc_`.

```python
messages = [
    {"role": "system", "content": "You are a product search assistant."},
    {"role": "user", "content": "Find climbing gear for outdoors"},
    {
        "type": "function_call",
        "id": "fc_example1",
        "call_id": "call_example1",
        "name": "search_database",
        "arguments": '{"search_query": "climbing gear outdoor"}',
    },
    {
        "type": "function_call_output",
        "call_id": "call_example1",
        "output": "Results: ...",
    },
    {"role": "user", "content": "Now find shoes under $50"},
]
```

```python
# דוגמה לחיפוש אינטרנט מובנה
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## קלט תמונה

פריטי תוכן תמונה משנים את סוגם מ־`image_url` ל־`input_image`, וקישור ה־URL משתנה מאובייקט מקונן למחרוזת שטוחה.

### קלט תמונה — לפני (Chat Completions)
```python
resp = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

### קלט תמונה — אחרי (Responses API, URL)
```python
resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": "https://example.com/image.jpg",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

### קלט תמונה — אחרי (Responses API, base64)
```python
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image("path_to_your_image.jpg")

resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

> **שינויים עיקריים**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (אובייקט מקונן) → `"image_url": "..."` (מחרוזת שטוחה — או כתובת HTTPS או URI של נתוני `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## מעבר Microsoft Agent Framework (MAF)

**בדוק את גרסת ה־MAF שלך קודם** — המעבר תלוי האם אתה ב־MAF 1.0.0+ או בגרסת בטא/RC לפני 1.0.0.

לבדיקה: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

ב־MAF 1.0.0+, `OpenAIChatClient` **כבר משתמש ב־Responses API** — לא נדרש מעבר.

אם קוד הבסיס משתמש ב־`OpenAIChatCompletionClient` הישן (שמשתמש ב־`chat.completions.create`), החליפו אותו ב־`OpenAIChatClient`:

לפני:
```python
from agent_framework.openai import OpenAIChatCompletionClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatCompletionClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

אחרי:
```python
from agent_framework.openai import OpenAIChatClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

### MAF לפני 1.0.0 (בטא/RC)

ב־MAF לפני 1.0.0, `OpenAIChatClient` השתמש ב־Chat Completions. שדרגו ל־`agent-framework-openai>=1.0.0` שבה `OpenAIChatClient` משתמש כברירת מחדל ב־Responses API.

> **הערה**: ה־APIs של `Agent`, `MCPStreamableHTTPTool` ושאר MAF נותרו ללא שינוי — רק ייבוא ויצירת מופע של מחלקת הלקוח משתנים.

## מעבר LangChain (`langchain-openai`)

הוסף `use_responses_api=True` ל־`ChatOpenAI()`. עדכן גם גישת תוכן ההודעות מ־`.content` ל־`.text`.

לפני:
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
)

# ... קריאת סוכן ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

אחרי:
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
    use_responses_api=True,
)

# ... קריאת סוכן ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **שינויים מרכזיים**: (1) `use_responses_api=True` בבונה, (2) `.content` → `.text` בהודעות תגובה.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->