---
name: azure-openai-to-responses
license: MIT
---
# הגירת אפליקציות פייתון מ-Azure OpenAI Chat Completions ל-Responses API

> **הנחיה מחייבת — עקוב במדויק**
>
> מיומנות זו מיגרת בסיסי קוד בפייתון המשתמשים ב-Azure OpenAI Chat Completions
> ל-API המאוחד Responses. עקוב אחרי ההוראות במדויק.
> אל תתעסק במיפויי פרמטרים או תמציא צורות API חדשות.

---

## טריגרים

הפעל מיומנות זו כאשר המשתמש רוצה:
- להגר אפליקציית פייתון מ-Azure OpenAI Chat Completions ל-Responses API
- לשדרג שימוש ב-Python OpenAI SDK לצורת API העדכנית ביותר נגד Azure OpenAI
- להכין קוד פייתון למודלים GPT-5 או חדשים יותר שדורשים Responses על Azure
- לעבור מ-`AzureOpenAI`/`AsyncAzureOpenAI` ללקוח הסטנדרטי `OpenAI`/`AsyncOpenAI` עם נקודת קצה v1
- לתקן אזהרות התיישנות שקשורות לבנאי `AzureOpenAI` או `api_version`

---

## ⚠️ תאימות מודלים — בדוק קודם

> **לפני ההגירה, אמת שהפריסה שלך של Azure OpenAI תומכת ב-Responses API.**

### 1. בדיקת עשן של הפריסה שלך (הכי מהיר)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **הערה**: ל-`max_output_tokens` יש **מינימום של 16** ב-Azure OpenAI. ערכים מתחת ל-16 מחזירים שגיאת 400. השתמש ב-50+ לבדיקות עשן.

אם זה מחזיר 404, דגם הפריסה אינו תומך ב-Responses עדיין — בדוק את ההפניה למטה או פרוס מחדש עם דגם נתמך.

### 2. בדוק דגמים זמינים באזור שלך (מומלץ)

הפעל את כלי התאימות המובנה למודלים כדי לראות מה זמין עם תמיכה ב-Responses API באזור הספציפי שלך:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

זה שואל את Azure ARM בשידור חי ומציג מטריצת תאימות — אילו דגמים תומכים ב-Responses, ביציאת נתונים מובנית, כלים וכו'. השתמש ב-`--filter gpt-5.1,gpt-5.2` לכווץ תוצאות או ב-`--json` לסקריפטים.

### 3. הפניה מלאה לתמיכה בדגמים

- **שאל חי**: `python migrate.py models` (ראה למעלה — אזור ספציפי, תמיד מעודכן)
- **עיין בזמינות**: [טבלת סיכום דגמים וזמינות אזור](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **התחלה מהירה והנחיה**: **https://aka.ms/openai/start**

### ⚠️ מגבלות דגמים ישנים

> **אזהרה**: דגמים ישנים יותר (לפני `gpt-4.1`) ייתכן ואינם תומכים בכל תכונות ה-Responses API במלואן.
>
> מגבלות ידועות עם דגמים ישנים:
> - **פרמטר `reasoning`**: אינו נתמך בהרבה דגמים שאינם למטרות הסקה. העבר את `reasoning` רק אם היה קיים בקוד המקורי.
> - **פרמטר `seed`**: אינו נתמך בכלל ב-Responses API — הסר מכל הבקשות.
> - **פלט מובנה דרך `text.format`**: דגמים ישנים עשויים לא לאכוף במדויק סכמות JSON עם `strict: true`.
> - **אורקסטרציה של כלים**: GPT-5 ומעלה מארגנים קריאות כלים כחלק מההסקה הפנימית. דגמים ישנים ב-Responses עדיין עובדים אך חסרה אינטגרציה עמוקה זו.
> - **מגבלות טמפרטורה**: בהגירה ל-`gpt-5` יש לדחות את הטמפרטורה או לקבועה ל-`1`. לדגמים ישנים אין מגבלה זו.

### דגמי הסקה מסדרת O (o1, o3-mini, o3, o4-mini)

לדגמי סדרת O יש מגבלות פרמטרים ייחודיות. בהגירת אפליקציות המיועדות לדגמי סדרת O:

- **`temperature`**: חייב להיות `1` (או להישמט). דגמי סדרת O אינם מקבלים ערכים אחרים.
- **`max_completion_tokens` → `max_output_tokens`**: אפליקציות המשתמשות ב-`max_completion_tokens` הייחודי ל-Azure חייבות לעבור ל-`max_output_tokens`. יש להגדיר ערכים גבוהים (4096+) כי אסימוני הסקה נספרים נגד המגבלה.
- **`reasoning_effort`**: אם האפליקציה משתמשת ב-`reasoning_effort` (נמוך/בינוני/גבוה), יש לשמור עליו — ה-Responses API תומך בפרמטר זה לדגמי סדרת O.
- **התנהגות סטרימינג**: דגמי סדרת O עשויים לאגור פלט עד לסיום ההסקה לפני שיוצרים אירועי דלתא טקסט. סטרימינג עדיין עובד, אך `response.output_text.delta` ראשוני עשוי להגיע מעכב יותר מאשר בדגמי GPT.
- **`top_p`**: אינו נתמך בסדרת O — הסר אם קיים.
- **שימוש בכלים**: דגמי סדרת O תומכים בכלים דרך Responses API כפי שמודלים GPT תומכים, אך איכות אורקסטרציית קריאות כלים משתנה לפי דגם.

**פעולה — ייעוץ מודל יזום**: במהלך שלב הסריקה, בדוק לאיזה דגם האפליקציה מיועדת (שמות פריסה, משתני סביבת עבודה, קונפיגורציה). אם הדגם מקדים ל-`gpt-4.1` (לא gpt-4.1+), אמור למשתמש מראש:
- ההגירה תעבוד לטקסט בסיסי, צ'אט, סטרימינג וכלים בדגם הקיים שלהם.
- דגמים חדשים (`gpt-5.1`, `gpt-5.2`) מציעים אורקסטרציית כלים טובה יותר, אכיפת פלט מובנה, הסקה וזמינות בין-אזורית.
- עליהם לשקול שדרוג הפריסה כשהם מוכנים — זה לא חוסם את ההגירה.

אל תחסום או תסרב להגר לפי גרסת המודל. הייעוץ הוא לצורך מידע בלבד.

### דגמי GitHub אינם תומכים ב-Responses API

> **דגמי GitHub (`models.github.ai`, `models.inference.ai.azure.com`) אינם תומכים ב-Responses API.**

אם בסיס הקוד כולל נתיב קוד לדגמי GitHub (חפש `base_url` המכוון ל-`models.github.ai` או `models.inference.ai.azure.com`), **הסר אותו לגמרי** במהלך ההגירה. ה-Responses API דורש Azure OpenAI, OpenAI או נקודת קצה מקומית תואמת (למשל Ollama עם תמיכה ב-Responses).

פעולה במהלך הסריקה:
- סמן כל נתיב קוד לדגמי GitHub להסרה.

---

## הגירת מסגרת עבודה

אפליקציות רבות משתמשות במסגרת עבודה ברמת גבוה מעל OpenAI. בהגירת אלו, ה-API של המסגרת משתנה — לא רק הקריאות התחתונות ל-OpenAI.

### מסגרת סוכנים של מיקרוסופט (MAF)

**בדוק תחילה את גרסת MAF שלך** — ההגירה תלויה אם אתה על MAF 1.0.0+ או ביטא/RC לפני 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **כבר משתמש ב-Responses API** — אין צורך בהגירה. אם בסיס הקוד משתמש ב-`OpenAIChatCompletionClient` הישן (שמשתמש ב-`chat.completions.create`), החלף ל-`OpenAIChatClient`.

| לפני | אחרי |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

לבדוק גרסה: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF לפני 1.0.0 (הוצאות ביטא/RC)

ב-MAF לפני 1.0.0, `OpenAIChatClient` השתמש ב-Chat Completions. שדרג ל-`agent-framework-openai>=1.0.0` שבו `OpenAIChatClient` כבר משתמש ב-Responses API כברירת מחדל.

אין שינוי נוסף דרוש — ה-API של `Agent` והכלים נשארים זהים.

### LangChain (`langchain-openai`)

הוסף `use_responses_api=True` ל-`ChatOpenAI()`. גם עדכן גישה לתגובה מ-`.content` ל-`.text`.

| לפני | אחרי |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

לדוגמאות קוד מלאות לפני/אחרי, ראה [cheat-sheet.md](./references/cheat-sheet.md).

---

## הנחיות הגירת פרונטאנד

> **Responses API הוא נושא צד-שרת.** הגר את הבקאנד בפייתון שלך; חוזה HTTP בצד הפרונטאנד צריך להישאר ללא שינוי אלא אם הבקאנד שלך הוא מעקף דק — במקרה זה שקול לאמץ את צורת הבקשה של Responses כדי לבטל שכבת תרגום. אם הפרונטאנד קורא ל-OpenAI ישירות עם מפתח בצד לקוח, העבר את הקריאות לבקאנד קודם.

### הפסקת שימוש ב-`@microsoft/ai-chat-protocol`

חבילת ה-npm `@microsoft/ai-chat-protocol` הוסרה ויש להחליפה ב-[`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). אם נתקל בה בפרונטאנד:

1. החלף את תגית סקריפט CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. הסר יצירת מופע `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. החלף את `client.getStreamedCompletion(messages)` בקריאה ישירה ל-`fetch()` לנקודת הקצה סטרימינג בבקאנד.
4. החלף `for await (const response of result)` ב-`for await (const chunk of readNDJSONStream(response.body))`.
5. עדכן גישה למאפיינים מ-`response.delta.content` / `response.error` ל-`chunk.delta.content` / `chunk.error`.

---

## מטרות

- למנות את כל אתרי הקריאה בפייתון המשתמשים ב-Chat Completions או ב-Completions ישן נגד Azure OpenAI.
- להציע תוכנית והסדר הגירה עבור בסיס הקוד בפייתון.
- לבצע שינויים מינימליים ובטוחים לעבור ל-Responses API.
- לעדכן קוראים לצריכת סכמת הפלט של Responses; ללא עטיפות תאימות אחורית.
- להריץ בדיקות/לינטים; לתקן תקלות משניות שנגרמו מההגירה.
- להכין קבוצות שינויים קטנות וכנות לסקירה ולספק סיכום סופי עם הבדלים (לא לבצע commit).

---

## כללי שמירת גבולות

- לשנות רק קבצים בתוך סביבת ה-git. לעולם אל תכתוב מחוץ לה.
- אל תשמור התאמות תאימות לאחור; הגר את הקוד לצורת ה-API החדשה.
- אל תשאיר הערות מעבר/מעבר או קבצי גיבוי.
- שמור על סמנטיקת סטרימינג אם הייתה בשימוש קודם; אחרת השתמש ללא סטרימינג.
- בקש אישור לפני הרצת פקודות או קריאות רשת אם במצב אישורים.
- אל תריץ `git add`/`git commit`/`git push`; הפק רק שינויים בעץ העבודה.

---

## שלב 0: הגירת לקוח Azure OpenAI (דרישה מוקדמת)

אם בסיס הקוד משתמש בבנאי `AzureOpenAI` או `AsyncAzureOpenAI`, הגר תחילה לבנאי הסטנדרטי `OpenAI` / `AsyncOpenAI`. בנאים ייחודיים ל-Azure אינם נתמכים ב-`openai>=1.108.1`.

### למה נקודת קצה v1?

נקודת הקצה החדשה `/openai/v1` משתמשת בלקוח הסטנדרטי `OpenAI()` במקום `AzureOpenAI()`, אינה דורשת פרמטר `api_version`, ופועלת זהה ב-OpenAI וב-Azure OpenAI. קוד הלקוח זהה והכין לעתיד — ללא צורך בניהול גרסאות.

### שינויים עיקריים

| לפני | אחרי |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | הסרה מלאה |

### רשימת ניקוי

- הסר את ארגומנט `api_version` מבניית הלקוח.
- הסר משתני סביבה `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` מקובץ `.env`, הגדרות אפליקציה וקבצי Bicep/תשתית.
- שנה את `AZURE_OPENAI_CLIENT_ID` ל־`AZURE_CLIENT_ID` בקובץ `.env`, הגדרות אפליקציה, Bicep/תשתית ודגמי בדיקה (הסכם סטנדרטי של Azure Identity SDK).
- ודא `openai>=1.108.1` בקובץ `requirements.txt` או `pyproject.toml`.

### הגירת משתני סביבה

| משתנה סביבה ישן | פעולה | הערות |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **הסר** | אין צורך ב-`api_version` עם נקודת הקצה v1 |
| `AZURE_OPENAI_API_VERSION` | **הסר** | כמו למעלה |
| `AZURE_OPENAI_CLIENT_ID` | **שנה שם** → `AZURE_CLIENT_ID` | הסכם סטנדרטי של Azure Identity SDK ל-`ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **שמור** | עדיין דרוש לבניית `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **שמור** | משמש כפרמטר `model` ב-`responses.create` |
| `AZURE_OPENAI_API_KEY` | **שמור** | משמש כ-`api_key` לאימות עם מפתח |

לדוגמאות קוד של פעולת הלקוח (סינכרוני, אסינכרוני, EntraID, מפתח API, מולטי טננט), ראה [cheat-sheet.md](./references/cheat-sheet.md).

---

## שלב 1: זיהוי אתרי קריאה ישנים

הפעל את הסקריפט [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) כדי למצוא את כל אתרי הקריאה שצריך להגר:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

או בצע חיפושים אלו ידנית — כל התאמה היא יעד להגרה:

```bash
# קריאות API ישנות (חייבים לשכתב)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# בוני לקוח Azure מיושנים (חייבים להחליף)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# דפוסי גישה לצורת התגובה (חייבים לעדכן)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# הגדרות כלים בפורמט מקונן ישן (חייב לפשט)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# תוצאות כלים בפורמט ישן (חייב להמיר ל-function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# פרמטרים מיושנים (חייבים להסיר או לשנות שם)
rg "response_format"
rg "max_tokens\b"        # שנה שם ל- max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# משתני סביבה מיושנים (לנקות)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # צריך להיות AZURE_CLIENT_ID

# נקודות קצה של מודלים ב-GitHub (חייב להסיר — API לתגובות לא נתמך)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# דפוסי מורשת ברמת התשתית (חייבים לעדכן)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: להחליף עם OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: צריך use_responses_api=True

# תשתית לבדיקות (חייבת לעדכן)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# גישת גוף שגיאת סינון תוכן (חייב לעדכן — המבנה השתנה)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # צורת יחיד ישנה — עכשיו content_filter_results (רבים) בתוך מערך content_filters

# קריאות HTTP גולמיות לנקודת הסיום Chat Completions (חייב לעדכן URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### היוריסטיקות (גילוי וכתיבה מחדש)

- **לקוח Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **קונסטרוקטורים של לקוח Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **כלים**: המרת הגדרות כלי-קריאה לפונקציה מפורמט מקונן (`{"type": "function", "function": {"name": ...}}`) לפורמט Responses שטוח (`{"type": "function", "name": ...}`); השתמש ב-`tool_choice`; החזר תוצאות כלי כפריטים מסוג `{"type": "function_call_output", "call_id": ..., "output": ...}` (ולא `{"role": "tool", ...}`).
- **סיורים של כלים**: כאשר המודל מחזיר קריאות פונקציה, הוסף פריטי `response.output` לשיחה (ולא מילון ידני `{"role": "assistant", "tool_calls": [...]}`), ואז הוסף פריטי `function_call_output` עבור כל תוצאה.
- **דוגמאות כלים עם מספר דוגמאות**: אם השיחה כוללת דוגמאות קריאה לכלי מקודדות בקוד, המר אותם לפריטים `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. מזהים חייבים להתחיל ב-`fc_`.
- **`pydantic_function_tool()`**: העזר הזה עדיין מייצר את הפורמט המקונן הישן ואינו **תואם** ל-`responses.create()`. החלף בהגדרות כלי ידניות או עטיפה שמשטיחה.
- **רב-סיבובים**: שמור היסטוריית שיחה באפליקציה; העבר סיבובים קודמים כפריטי `input`.
- **עיצוב**: החלף את `response_format` של Chat בשכבת על ב-Responses עם `text.format`. צורה קאנונית: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **פריטי תוכן**: החלף `content[].type: "text"` של Chat ל-`content[].type: "input_text"` ב-Responses עבור תורות של משתמש/מערכת.
- **פריטי תוכן תמונה**: החלף `content[].type: "image_url"` של Chat ל-`content[].type: "input_image"` ב-Responses. השדה `image_url` משתנה מאובייקט מקונן `{"url": "..."}` למחרוזת שטוחה. ראה את דף המרמה לדוגמאות לפני/אחרי.
- **מאמץ טיעון**: **העבר רק את `reasoning` אם כבר קיים בקוד המקורי**.
- **טיפול בשגיאות סינון תוכן**: מבנה גוף השגיאה השתנה. Chat Completions השתמש ב-`error.body["innererror"]["content_filter_result"]` (יחיד); Responses API משתמש ב-`error.body["content_filters"][0]["content_filter_results"]` (רבים בתוך מערך). קוד שניגש ל-`innererror` יגרום ל-`KeyError`. מחדש לנתיב חדש.
- **קריאות HTTP גולמיות**: אם האפליקציה עושה קריאה ישירה ל-Azure OpenAI REST API (דרך `requests`, `httpx`, וכו') באמצעות `/openai/deployments/{name}/chat/completions?api-version=...`, המיר ל-`/openai/v1/responses`. גוף הבקשה משתנה: `messages` → `input`, הוסף `max_output_tokens` ו-`store: false`, הסר פרמטר שאילתה `api-version`. גוף התגובה משתנה: `choices[0].message.content` → `output[0].content[0].text` (שים לב: `output_text` הוא מאפיין נוחות SDK שאינו קיים ב-JSON גולמי).

---

## שלב 2: הפעלת ההגירה

### הערות על ההגירה (Chat Completions → Responses)

- **מדוע להגיר**: Responses היא ה-API המאוחדת לטקסט, כלים וזרימה; Chat Completions הוא מורשת. עם GPT-5, Responses נדרש עבור ביצועים מיטביים.
- **HTTP**: נקודת הקצה של Azure משתנה מ-`/openai/deployments/{name}/chat/completions` ל-`/openai/v1/responses`.
- **שדות**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` נשאר ללא שינוי.
- **עיצוב**: `response_format` → `text.format` כאובייקט נכון.
- **פריטי תוכן**: החלף `content[].type: "text"` של Chat ל-`content[].type: "input_text"` ב-Responses עבור תורות מערכת/משתמש.
- **פריטי תוכן תמונה**: החלף `content[].type: "image_url"` של Chat ל-`content[].type: "input_image"` ב-Responses. שטח את השדה `image_url` מ-`{"image_url": {"url": "..."}}` ל-`{"image_url": "..."}` (מחרוזת פשוטה — כתובת URL ב-HTTPS או URI של נתונים מסוג `data:image/...;base64,...`).

### מפתחות פרמטרים להתייחסות

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (מערך פריטים) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (אובייקט) |
| `temperature` | `temperature` (לא משתנה) |
| `stop` | `stop` (לא משתנה) |
| `frequency_penalty` | `frequency_penalty` (לא משתנה) |
| `presence_penalty` | `presence_penalty` (לא משתנה) |
| `tools` / קריאות לפונקציה | `tools` (לא משתנה) |
| `seed` | **הסר** (לא נתמך) |
| `store` | `store` (נקבע ל-`false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (מחרוזת שטוחה) |

לדוגמאות קוד מלאות לפני/אחרי, ראה [cheat-sheet.md](./references/cheat-sheet.md).

להגירת תשתית בדיקות (מוקים, תמונות מצב, ואישורים), ראה [test-migration.md](./references/test-migration.md).

לפתרון תקלות וטעויות, ראה [troubleshooting.md](./references/troubleshooting.md).

---

## שמירת מידע ומצב

- קבע `store: false` בכל בקשות Responses.
- אל תסתמך על מזהי הודעות קודמות או הקשר שנשמר בשרת; שמור מצב מנוהל-לקוח וצמצם מטא-דאטה.

---

## קריטריוני קבלה

### שערים ברמת הקוד (כולם חייבים לעבור)

- [ ] אין התאמות עבור `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` בקבצים שהוגרו.
- [ ] אין התאמות עבור `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — כל הקונסטרוקטורים משתמשים ב-`OpenAI`/`AsyncOpenAI` עם נקודת הקצה v1.
- [ ] אין התאמות עבור `rg "models\.github\.ai|models\.inference\.ai\.azure"` — נתיבי קוד מודלים של GitHub הוסרו.
- [ ] אין התאמות עבור `rg "OpenAIChatCompletionClient"` — קוד MAF 1.0.0+ משתמש ב-`OpenAIChatClient` (שמשתמש ב-Responses API). בגרסאות לפני 1.0.0, שדרג ל-`agent-framework-openai>=1.0.0`.
- [ ] כל קריאות `ChatOpenAI(...)` כוללות `use_responses_api=True`.
- [ ] אין התאמות עבור `rg "choices\[0\]"` — כל גישות לתגובה משתמשות ב-`resp.output_text` או סכמת הפלט של Responses.
- [ ] אין `response_format` ברמת על; כל הפלט המובנה משתמש ב-`text={"format": {...}}`.
- [ ] `openai>=1.108.1` ו-`azure-identity` בקבצי `requirements.txt` או `pyproject.toml`; תלותות הותקנו מחדש.
- [ ] `store=False` מוגדר בכל קריאה ל-`responses.create`.
- [ ] אין `api_version` בבניית הלקוח; `AZURE_OPENAI_API_VERSION` הוסר מקבצי הסביבה והתשתית.

### שערים בתשתית בדיקות (כולם חייבים לעבור)

- [ ] אין התאמות עבור `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] אין התאמות עבור `rg "_azure_ad_token_provider" tests/` — אישורים עודכנו לבדוק `isinstance(client, AsyncOpenAI)` או `base_url`.
- [ ] אין התאמות עבור `rg "prompt_filter_results|content_filter_results" tests/` — מוקים ספציפיים ל-Azure להסינון הוסרו.
- [ ] מוקים משתמשים ב-`kwargs.get("input")` ולא ב-`kwargs.get("messages")`.
- [ ] קבצי snapshot / golden מעודכנים לצורת הזרימה של Responses (ללא `choices[0]`, `function_call`, `logprobs` וכו').
- [ ] `pytest` עובר ללא כשלונות לאחר כל עדכוני הבדיקות.

### שערים התנהגותיים (בדיקה ידנית או דרך מסגרת בדיקות)

- [ ] **השלמה בסיסית**: `responses.create` שאינה זורמת מחזירה `output_text` שאינו ריק.
- [ ] **עקיבות בזרימה**: אם הקוד המקורי השתמש בזרימה, הקוד שהוגר זורם ומפיק אירועים `response.output_text.delta` עם דלתא לא ריקה.
- [ ] **פלט מובנה**: אם משתמשים ב-`text.format` עם `json_schema`, `json.loads(resp.output_text)` מצליח ותואם לסכמה.
- [ ] **לולאת קריאה לכלים**: אם משתמשים בכלים, המודל מוציא קריאות כלים, האפליקציה מבצעת אותן, והבקשה הבאה מחזירה פלט סופי `output_text` (ללא לולאה אינסופית).
- [ ] **עקיבות אסינכרונית**: אם השתמשו ב-`AsyncAzureOpenAI`, מקביל ב-`AsyncOpenAI` עובד עם `await`.
- [ ] **שיעור שגיאות**: אין שגיאות חדשות מסוג 400/401/404 בהשוואה לקו הבסיס לפני ההגירה.

### תוצרי עבודה

- התקציר כולל קבצים שנערכו, מונים לפני/אחרי של אתרי קריאה מורשת, ושלבים הבאים.
- השינויים הם רק עריכות בעץ העבודה (ללא commits).

---

## דרישות גרסת SDK

| חבילה | גרסה מינימלית |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | העדכנית ביותר (לאימות EntraID) |

---

## מקורות

- [גיליון רמאות — כל קטעי הקוד](./references/cheat-sheet.md)
- [הגירת בדיקות — מוקים, תמונות מצב, אישורים](./references/test-migration.md)
- [פתרון תקלות — שגיאות, טבלת סיכונים, מרעין בישין](./references/troubleshooting.md)
- [detect_legacy.py — סורק אוטומטי](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [מסמכי Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [מחזור חיים של גרסת Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API reference](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->