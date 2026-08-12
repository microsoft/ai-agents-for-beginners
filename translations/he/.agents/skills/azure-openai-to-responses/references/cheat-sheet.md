# גיליון רמאות API לתגובות (פייתון + Azure OpenAI)

> כל הקטעים שלמטה מניחים `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` ו-`client` כבר מאופשר (ראה הקמת לקוח).

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

## הקמת לקוח — EntraID (מומלץ)
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

## הקמת לקוח — מפתח API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## הקמת לקוח אסינכרוני — EntraID
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

## הקמת לקוח אסינכרוני — EntraID עם שוכר מפורש (רב-שוכר)

כאשר משאב Azure OpenAI נמצא ב**שוכר שונה** מזה המוגדר כבררת מחדל, העבר `tenant_id` במפורש לאישור הזהות. זה נפוץ בתרחישי פיתוח/בדיקה שבהם שוכר הבית של המפתח שונה מהשוכר של המשאב.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential עבור ייצור (Azure Container Apps, App Service, וכו')
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # זהות מנוהלת שהוקצתה למשתמש
)
# AzureDeveloperCliCredential לפיתוח מקומי — tenant_id מפורש הוא קריטי
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# שרשרת: נסה זהות מנוהלת קודם, חזור ל-azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## הגירת לקוח אסינכרוני — לפני/אחרי

לפני (מושהה):
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4.1",
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

## הגירת סינכרון מלאה — לפני/אחרי

לפני (ישן — Azure OpenAI Chat Completions):
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

אחרי (Responses API — נקודת קצה של Azure OpenAI v1):
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

## שידור (סינכרוני)
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

## שידור (אסינכרוני)
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

## שידור באפליקציית ווב — צורת backend אל frontend

בעת הגירת אפליקציית ווב שמשדרת SSE/JSONL ל-frontend, **פורמט הסיריאליזציה ב-backend** משתנה. עצב את פלט ה-backend החדש לשמר את דפוסי הגישה הקיימים של ה-frontend כך שה-frontend לא יצטרך שינויים.

**לפני** — backend של Chat Completions בדרך כלל סיריאלז כיל את מילון `choices[0]` של כל חלק:
```python
# ישן: מילון בחירה מלא מסודר לפי קטע
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
קריאה ב-frontend: `response.delta.content` (נתיב עמוק לאובייקט הבחירה).

**אחרי** — backend של Responses API משדר צורה מינימלית ששומרת על אותו נתיב גישה ב-frontend:
```python
# חדש: לשדר רק את מה שהחזית צריכה
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
ה-frontend עדיין קורא `response.delta.content` — **אין צורך בשינויים ב-frontend**.

> **תובנה מרכזית**: צורת השידור ב-Responses API (`event.type` + `event.delta`) שונה במהותה מ-Chat Completions (`chunk.choices[0].delta.content`). אבל החוזה בין backend ל-frontend הוא שלך להגדיר. עצב את פלט ה-backend להתאים למה שה-frontend כבר מצפה לו.

## רצף אירועים בשידור

כש`stream: true`, ה-API משדר אירועים בסדר זה:
1. `response.created` – אובייקט תגובה מאותחל
2. `response.in_progress` – ההפקה התחילה
3. `response.output_item.added` – פריט פלט נוצר
4. `response.content_part.added` – חלק תוכן התחיל
5. `response.output_text.delta` – חלקי טקסט (מרובים, לכל אחד יש `delta: string`)
6. `response.output_text.done` – הפקת הטקסט הסתיימה
7. `response.content_part.done` – חלק תוכן הסתיים
8. `response.output_item.done` – פריט פלט הסתיים
9. `response.completed` – התגובה המלאה הושלמה

לשידור טקסט בסיסי, התמודד רק עם `response.output_text.delta` (לחלקי הטקסט) ו-`response.completed` (לסיום).

## טיפול בשגיאות בשידור באפליקציות ווב

בעת שידור באפליקציית ווב, עטוף את האיטרציה האסינכרונית ב`try/except` והחזר שגיאות כ-JSON כדי שה-frontend יוכל להציג אותן בצורה נאותה (למשל, הגבלת קצב, תקלות חולפות):

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

> **למה זה חשוב**: Azure OpenAI מחזיר `429 Too Many Requests` בעת הגבלת הקצב. בלי `try/except`, תגובת השידור מתה בשקט. איתו, ה-frontend מקבל `{"error": "Too Many Requests"}` ויכול להציג בקשת ניסיון חוזר.

## סוגי אירועי שידור (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## פורמט שיחה
```python
# ממשק ה-API של התגובות תומך בפורמט שיחה דרך מערך קלט
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

מבנה גוף השגיאה השתנה מ-Chat Completions ל-Responses API.

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

הבדלים מרכזיים:
- העיטוף `innererror` **נעלם** — פרטי מסנן התוכן נמצאים כעת ברמת שורש של `error.body`.
- `content_filter_result` (יחיד) → `content_filters` (מערך ברבים) שמכיל `content_filter_results` (ברבים) בתוך כל פריט.
- כל פריט ב-`content_filters` כולל `blocked`, `source_type`, ו-`content_filter_results` עם פרטים לפי קטגוריה (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

מבנה גוף שגיאת מסנן תוכן מלא של Responses API:
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

## הגירת HTTP גולמי (requests/httpx)

אם האפליקציה קוראת ישירות ל-Azure OpenAI REST במקום להשתמש ב-SDK:

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

> **הערה**: `output_text` היא תכונה נוחה באובייקט `Response` של Python SDK. תגובת ה-REST הגולמית לא מכילה שדה `output_text` על הרמה העליונה — הטקסט נמצא ב-`output[0].content[0].text`.

## שיחה רב-סיבובית
```python
# לבנות שיחה עם Responses API
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

שיחה רב-סיבובית עם סוג תוכן (מפורש `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### שיחה רב-סיבובית באמצעות `previous_response_id` (חלופה)

במקום לנהל בעצמך את מערך השיחה, אפשר לקשר תגובות
בצד השרת באמצעות `previous_response_id`. ה-API שומר כל תגובה
ומוסיף אוטומטית את הסיבובים הקודמים.

```python
# תור ראשון
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# תורים הבאים — פשוט העבר את הודעת המשתמש החדשה + מזהה התגובה הקודמת
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**מתי להשתמש באיזה:**

| גישה | יתרונות | חסרונות |
|---|---|---|
| מערך `input` (ידני) | שליטה מלאה על ההיסטוריה; אפשר לקצץ/לסכם; אין צורך באחסון בצד השרת (`store=False`) | יותר קוד; אתה מנהל את המערך |
| `previous_response_id` | קוד פשוט יותר; קישור אוטומטי | דורש `store=True` (ברירת מחדל); השיחה נשמרת בצד השרת; לא ניתן לשנות היסטוריה בין סיבובים |

> **הערת הגירה:** רוב אפליקציות Chat Completions כבר מנהלות מערך הודעות פרטי, לכן המרת למערך `input` היא הגירה ישירה יותר. השתמש ב-`previous_response_id` לקוד חדש או כשאין צורך לשנות היסטורית שיחה.

## דגמי זיהוי סדרת O (o1, o3-mini, o3, o4-mini)

לדגמי סדרת O יש הגבלות פרמטר ייחודיות בעת ההגירה ל-Responses API.

### מיפוי פרמטרים לסדרת O

| Chat Completions (סדרת O) | Responses API | הערות |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | הגדר גבוה (4096+) — טוקנים של ההיגיון נספרים בגבול |
| `reasoning_effort` | `reasoning.effort` | השאר כמו שהוא אם קיים (נמוך/בינוני/גבוה) |
| `temperature` | הסר או הגדר ל`1` | סדרת O מקבלת רק `1` |
| `top_p` | הסר | לא נתמך בסדרת O |
| `seed` | הסר | לא נתמך ב-Responses API |

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

> **הערה**: דגמי סדרת O עשויים לאגור פלט במהלך ההיגיון לפני שליחת דלתא של טקסט. השידור עדיין פועל אך אירוע ה-`response.output_text.delta` הראשון עשוי להגיע באיחור יחסית לדגמי GPT.

## גישה לטוקנים של היגיון
```python
# מודלים של היגיון משתמשים בהיגיון פנימי — ניתן לראות כמה אסימוני היגיון שומשו
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

> **חשוב**: השתמש ב-`max_output_tokens=1000` (ולא 50–200) כדי לקחת בחשבון את תהליך ההיגיון הפנימי של דגמי ההיגיון. המודל משתמש בטוקני היגיון לפני יצירת הפלט הסופי.

## פלט מבנה — סכמת JSON
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

- הגדר פונקציות ב-`tools` בפורמט **שטוח של Responses API** — `name`, `description`, ו-`parameters` ברמה העליונה (לא מקוננים תחת `function`).
- כשהמודל מבקש קריאה לכלי, בצע זאת באפליקציה שלך וכלול את תוצאת הכלי בבקשה הבאה כפריט `function_call_output` בתוך `input`.
- שמור על סכמות מינימליות; אמת קלטים לפני ביצוע.
- בעת שימוש ב-`strict: true`, כל התכונות חייבות להיות ברשימת `required` ו-`additionalProperties: false` הוא חובה.

> **⚠️ `pydantic_function_tool()` אינו תואם**: הפונקציה `openai.pydantic_function_tool()` עדיין מייצרת את פורמט הצימוד הישן של Chat Completions (`{"type": "function", "function": {"name": ...}}`). אל תשתמש בה עם `responses.create()`. הגדר סכמות כלים ידנית או כתוב עטיפה להשטחת הפלט.

### פורמט הגדרת כלי

ה-Responses API משתמש בפורמט כלי **שטוח** — `name`, `description`, `parameters` הם מפתחות עליונים (לא מקוננים תחת `function`).

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
            "required": ["city_name"],       # כל התכונות חייבות להיות רשומות
            "additionalProperties": False,   # נחוץ עבור מצב מחמיר
        },
    }
]
```

### קריאת כלי סיבובית (ביצוע והחזרת תוצאות)

כאשר המודל מבקש קריאה לכלי, השתמש בפריטי `response.output` + `function_call_output` — **לא** בתבנית `role: assistant` + `role: tool` של Chat Completions.

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
    # הוסף את פריטי function_call של הדגם לשיחה
    messages.extend(response.output)

    # הפעל כל כלי והוסף את התוצאות
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

### דוגמאות לקריאת כלי עם כמה אירועים מוקדמים

כשמספקים דוגמאות לקריאות כלי ב-`input`, השתמש בפריטי `function_call` ו-`function_call_output`. מזהים חייבים להתחיל עם `fc_`.

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
# דוגמה לחיפוש מובנה באינטרנט
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## קלט תמונה

פריטי תוכן תמונה משתנים מסוג `image_url` ל-`input_image`, וכתובת ה-URL משתנה מאובייקט מקונן למחרוזת שטוחה.

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

> **שינויים מרכזיים**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (אובייקט מקונן) → `"image_url": "..."` (מחרוזת שטוחה — או כתובת HTTPS או URI של נתוני base64 `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## הגירת מסגרת סוכן מיקרוסופט (MAF)

**בדוק תחילה את גרסת MAF שלך** — ההגירה תלויה אם אתה בגרסה 1.0.0+ או ב-beta/rc שלפני 1.0.0.

לבדיקה: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

ב-MAF 1.0.0+, `OpenAIChatClient` **כבר משתמש ב-Responses API** — לא נדרשת הגירה.

אם בסיס הקוד משתמש ב-`OpenAIChatCompletionClient` הישן (שמשתמש ב-`chat.completions.create`), החלף אותו ב-`OpenAIChatClient`:

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

### MAF לפני 1.0.0 (גרסאות beta/rc)

ב-MAF לפני 1.0.0, `OpenAIChatClient` השתמש ב-Chat Completions. עדכן ל-`agent-framework-openai>=1.0.0` שבו `OpenAIChatClient` משתמש כברירת מחדל ב-Responses API.

> **הערה**: ה-`Agent`, `MCPStreamableHTTPTool` ו-APIs אחרים של MAF נותרו ללא שינוי — רק ייבוא המחלקה וההכנסה שלו משתנים.

## הגירת LangChain (`langchain-openai`)

הוסף `use_responses_api=True` ל-`ChatOpenAI()`. גם עדכן גישה לתוכן הודעות מ-`.content` ל-`.text`.

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

> **שינויים מרכזיים**: (1) `use_responses_api=True` בבונה, (2) `.content` → `.text` בהודעות התגובה.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->