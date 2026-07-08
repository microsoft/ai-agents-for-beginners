---
name: azure-openai-to-responses
license: MIT
---
# העבר אפליקציות פייתון מ-Azure OpenAI Chat Completions ל-Responses API

> **הנחיות סמכותיות — עקוב במדויק**
>
> מיומנות זו מעבירה בסיסי קוד פייתון המשתמשים ב-Azure OpenAI Chat Completions
> ל-Responses API המאוחד. עקוב אחר ההוראות האלו במדויק.
> אל תמציא מיפויים של פרמטרים או צורות API חדשות.

---

## טריגרים

הפעל את המיומנות הזו כשהמשתמש רוצה:
- להעביר אפליקציית פייתון מ-Azure OpenAI Chat Completions ל-Responses API
- לשדרג שימוש ב-SDK של פייתון ל-OpenAI לצורת ה-API החדשה ביותר מול Azure OpenAI
- להכין קוד פייתון לדגמי GPT-5 או חדשים יותר שדורשים Responses על Azure
- לעבור מ-`AzureOpenAI`/`AsyncAzureOpenAI` ללקוח `OpenAI`/`AsyncOpenAI` סטנדרטי עם נקודת הקצה v1
- לתקן אזהרות התיישנות הקשורות לבוני `AzureOpenAI` או `api_version`

---

## ⚠️ תאימות דגמים — בדוק קודם

> **לפני ההעברה, ודא שהפריסה שלך של Azure OpenAI תומכת ב-Responses API.**

### 1. בדיקת עישון לפריסה שלך (הכי מהיר)

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

> **הערה**: ל-`max_output_tokens` יש **מינימום של 16** ב-Azure OpenAI. ערכים מתחת ל-16 מחזירים שגיאה 400. השתמש ב-50+ לבדקי עישון.

אם זה מחזיר 404, המודל בפריסה אינו תומך עדין ב-Responses — בדוק את ההפניה למטה או פרוס מחדש עם מודל נתמך.

### 2. בדוק דגמים זמינים באזור שלך (מומלץ)

הפעל את כלי התאימות המובנה לדגמים כדי לראות מה זמין עם תמיכה ב-Responses API באזור הספציפי שלך:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

זה שואל את Azure ARM חי ומציג מטריצת תאימות — איזה דגמים תומכים ב-Responses, פלט מובנה, כלים וכו'. השתמש ב-`--filter gpt-5.1,gpt-5.2` לצמצום התוצאות או ב-`--json` לאוטומציה.

### 3. הפניה מלאה לתמיכה בדגמים

- **שאילתה חיונית**: `python migrate.py models` (ראה למעלה — אזור-ספציפי, תמיד מעודכן)
- **עיין בזמינות**: [טבלת סיכום דגמים וזמינות אזורים](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **התחלת מהירה והנחיות**: **https://aka.ms/openai/start**

### ⚠️ מגבלות דגמים ישנים יותר

> **אזהרה**: דגמים ישנים יותר (למשל, `gpt-4o`, `gpt-4`) עשויים שלא לתמוך במלוא תכונות Responses API.
>
> מגבלות ידועות בדגמים ישנים:
> - **פרמטר `reasoning`**: לא נתמך ב-`gpt-4o-mini`, `gpt-4o` ורבים מדגמים ללא יכולת הסקה. העבר את `reasoning` רק אם כבר היה בקוד המקורי.
> - **פרמטר `seed`**: אינו נתמך כלל ב-Responses API — הסר מכל הבקשות.
> - **פלט מובנה באמצעות `text.format`**: דגמים ישנים עלולים לא לאכוף סכמה JSON עם `strict: true` בצורה אמינה.
> - **ניהול כלים**: GPT-5+ מנהל קריאות כלים כחלק מההסקה הפנימית. דגמים ישנים עדיין עובדים עם Responses אך חסר אינטגרציה עמוקה זו.
> - **הגבלות טמפרטורה**: כשממירים ל-`gpt-5`, יש להוריד או לקבוע לטמפרטורה ערך של `1`. בדגמים ישנים אין הגבלה כזו.

### דגמי הסקה מסדרת O (o1, o3-mini, o3, o4-mini)

לדגמי סדרת O יש הגבלות פרמטר ייחודיות. כשמעבירים אפליקציות הפונות לדגמי סדרת O:

- **`temperature`**: חייב להיות `1` (או להיטמע). דגמי סדרת O לא מקבלים ערכים אחרים.
- **`max_completion_tokens` → `max_output_tokens`**: אפליקציות המשתמשות ב-`max_completion_tokens` הספציפי ל-Azure חייבות לעבור ל-`max_output_tokens`. קבע ערכים גבוהים (4096+) כי טוקני הסקה נספרים נגד המגבלה.
- **`reasoning_effort`**: אם האפליקציה משתמשת ב-`reasoning_effort` (נמוך/בינוני/גבוה), השאר אותו — Responses API תומך בפרמטר זה לדגמי סדרת O.
- **התנהגות סטרימינג**: דגמי סדרת O עשויים לאגור פלט עד שההסקה תסתיים לפני שידור אירועים טקסט דלטא. סטרימינג עדיין פועל, אך ה-`response.output_text.delta` הראשון עשוי להתעכב יותר מאשר בדגמי GPT.
- **`top_p`**: לא נתמך בסדרת O — הסר אם קיים.
- **שימוש בכלים**: לדגמי סדרת O יש תמיכה בכלים דרך Responses API כמו בדגמי GPT, אך איכות ניהול קריאות כלים משתנה לפי דגם.

**פעולה — ייעוץ מודל יזום**: במהלך סריקת הקוד, בדוק לאיזה דגם האפליקציה פונה (שמות פריסה, משתני סביבה, קונפיגורציה). אם הדגם הוא `gpt-4o` או ישן יותר (לא `gpt-4.1+`), הודע למשתמש מראש:
- ההעברה תעבוד עבור טקסט בסיסי, שיחה, סטרימינג וכלים במודל הנוכחי שלו.
- דגמים חדשים יותר (`gpt-5.1`, `gpt-5.2`) מציעים ניהול טוב יותר של כלים, אכיפת פלט מובנה, הסקה וזמינות בין אזורית.
- כדאי לשקול שדרוג של הפריסה כשהם מוכנים — זה לא חוסם את ההעברה.

אל תחסום או תסרב להעביר לפי גרסת המודל. הייעוץ הוא למידע בלבד.

### דגמי GitHub אינם תומכים ב-Responses API

> **דגמי GitHub (`models.github.ai`, `models.inference.ai.azure.com`) אינם תומכים ב-Responses API.**

אם בסיס הקוד כולל נתיב קוד לדגמי GitHub (חפש `base_url` המצביע ל-`models.github.ai` או `models.inference.ai.azure.com`), **הסר אותו לחלוטין** במהלך ההעברה. Responses API דורש Azure OpenAI, OpenAI או נקודת קצה מקומית תואמת (למשל Ollama עם תמיכה ב-Responses).

פעולה במהלך הסריקה:
- סמן כל נתיב קוד לדגמי GitHub להסרה.

---

## מעבר במסגרת עבודה

אפליקציות רבות משתמשות במסגרת עבודה ברמה גבוהה מעל OpenAI. כשמעבירים את אלה, ה-API של המסגרת משתנה — לא רק הקריאות הפנימיות ל-OpenAI.

### Microsoft Agent Framework (MAF)

**בדוק את גרסת MAF שלך קודם** — המעבר תלוי אם אתה על MAF 1.0.0+ או בגרסת בטא/RC לפני 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **כבר משתמש ב-Responses API** — אין צורך במעבר. אם בסיס הקוד משתמש ב-`OpenAIChatCompletionClient` הישן (שמשתמש ב-`chat.completions.create`), החלף אותו ב-`OpenAIChatClient`.

| לפני | אחרי |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

לבדוק את הגרסה שלך: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)" `

#### MAF לפני 1.0.0 (גרסאות בטא/RC)

ב-MAF לפני 1.0.0, `OpenAIChatClient` השתמש ב-Chat Completions. שדרג ל-`agent-framework-openai>=1.0.0` שבו `OpenAIChatClient` משתמש כברירת מחדל ב-Responses API.

אין שינויים נוספים נדרשים — ה-API של ה-Agent והכלים נשארים כפי שהם.

### LangChain (`langchain-openai`)

הוסף `use_responses_api=True` ל-`ChatOpenAI()`. עדכן גם את הגישה לתגובה מ-`.content` ל-`.text`.

| לפני | אחרי |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

לדוגמאות קוד מלאות לפני/אחרי, ראה [cheat-sheet.md](./references/cheat-sheet.md).

---

## הנחיית מעבר בחזית

> **Responses API הוא עניין בצד שרת.** יש להעביר את ה-backend בפייתון; חוזה ה-HTTP של החזית צריך להישאר ללא שינוי אלא אם ה-backend הוא מעבר דק בלבד — במקרה כזה שקול לאמץ את צורת הבקשה של Responses כדי לבטל שכבת תרגום. אם החזית קוראת ל-OpenAI ישירות עם מפתח בצד הלקוח, העבר קריאות אלו ל-backend קודם.

### התיישנות `@microsoft/ai-chat-protocol`

חבילת npm `@microsoft/ai-chat-protocol` מיושנת ויש להחליפה ב-[`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). אם אתה נתקל בה בחזית:

1. החלף את תג הסקריפט מה-CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
 2. הסר את יצירת מופע `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. החלף את `client.getStreamedCompletion(messages)` בקריאה ישירה ל-`fetch()` לנקודת קצה סטרימינג ב-backend.
4. החלף את `for await (const response of result)` ב-`for await (const chunk of readNDJSONStream(response.body))`.
5. עדכן גישה מאפיינים מ-`response.delta.content` / `response.error` ל-`chunk.delta.content` / `chunk.error`.

---

## מטרות

- לאסוף את כל אתרי הקריאה בפייתון המשתמשים ב-Chat Completions או Completions ישנות מול Azure OpenAI.
- להציע תוכנית ושרשור מעבר לבסיס הקוד בפייתון.
- לבצע עריכות בטוחות ומינימליות למעבר ל-Responses API.
- לעדכן קוראים לצריכת סכמת הפלט של Responses; ללא עטיפות תאימות לאחור.
- להריץ בדיקות/בדיקות סטטיות; לתקן תקלות טפלות שנוצרו עקב המעבר.
- להכין מערכי שינויים קטנים לניטור ולספק סיכום סופי עם דיפים (לא לבצע commit).

---

## כללי זהירות

- לתקן רק קבצים בתוך סביבת git. לעולם אל תכתוב מחוץ לה.
- אל תשמור שימרים לתאימות לאחור; העבר את הקוד לצורת ה-API החדשה.
- אל תשאיר הערות מעבר או גיבויים.
- שמור על סמאנטיקת סטרימינג אם הייתה בשימוש קודם; אחרת השתמש ללא סטרימינג.
- בקש אישור לפני הרצת פקודות או קריאות רשת אם במצב אישור.
- אל תריץ `git add`/`git commit`/`git push`; הפק רק תיקוני working-tree.

---

## שלב 0: מעבר לקוח Azure OpenAI (דרישת מוקדם)

אם בסיס הקוד משתמש בבוני `AzureOpenAI` או `AsyncAzureOpenAI`, עבור תחילה לבוני הסטנדרט `OpenAI` / `AsyncOpenAI`. הבוני ה-Azure הספציפיים מיושנים ב-`openai>=1.108.1`.

### למה שביל API v1?

נקודת הקצה החדשה `/openai/v1` משתמשת בלקוח הסטנדרט `OpenAI()` במקום `AzureOpenAI()`, אינה דורשת פרמטר `api_version`, ופועלת זהה ב-OpenAI ו-Azure OpenAI. אותו קוד לקוח עמיד לעתיד — אין צורך בניהול גרסאות.

### שינויים עיקריים

| לפני | אחרי |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | הסר לחלוטין |

### רשימת ניקוי

- הסר את הטיעון `api_version` מהקונסטרקטור של הלקוח.
- הסר משתני סביבה `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` מתוך `.env`, הגדרות אפליקציה וקבצי Bicep/תשתית.
- שנה `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` ב-`.env`, הגדרות אפליקציה, Bicep/תשתית, ותבניות בדיקה (קונבנציה סטנדרטית של Azure Identity SDK).
- ודא שימוש ב-`openai>=1.108.1` ב-`requirements.txt` או `pyproject.toml`.

### מעבר משתני סביבה

| משתנה סביבה ישן | פעולה | הערות |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **הסר** | לא נדרש `api_version` עם נקודת קצה v1 |
| `AZURE_OPENAI_API_VERSION` | **הסר** | אותו הדבר כמו למעלה |
| `AZURE_OPENAI_CLIENT_ID` | **שנה שם** → `AZURE_CLIENT_ID` | קונבנציה סטנדרטית של Azure Identity SDK עבור `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **השאר** | עדיין נדרש ליצירת `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **השאר** | משמש כפרמטר `model` ב-`responses.create` |
| `AZURE_OPENAI_API_KEY` | **השאר** | משמש כמפתח API לאימות מבוסס מפתח |

לדוגמאות קוד הגדרת לקוח (סינכרוני, אסינכרוני, EntraID, מפתח API, ריבוי שוכנים), ראה [cheat-sheet.md](./references/cheat-sheet.md).

---

## שלב 1: זיהוי אתרי קריאה ישנים

הרץ את הסקריפט [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) למציאת כל אתרי הקריאה שדורשים מעבר:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

או הפעל חיפושים אלה ידנית — כל התאמה היא יעד למעבר:

```bash
# קריאות API מיושנות (חייב לכתוב מחדש)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# בוני לקוח Azure מיושנים (חייב להחליף)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# דפוסי גישה למבנה התגובה (חייב לעדכן)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# הגדרות כלים בפורמט מקונן ישן (חייב ליישר)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# תוצאות כלים בפורמט ישן (חייב להמיר ל-function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# פרמטרים מיושנים (חייב להסיר או לשנות שם)
rg "response_format"
rg "max_tokens\b"        # שנה שם ל-max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# משתני סביבה מיושנים (לנקות)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # צריך להיות AZURE_CLIENT_ID

# נקודות קצה של מודלים ב-GitHub (חייב להסיר — API תגובות לא נתמך)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# דפוסי מורשת ברמת המסגרת (חייב לעדכן)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: החלף ל-OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: צריך use_responses_api=True

# תשתית בדיקות (חייב לעדכן)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# גישה לגוף שגיאת מסנן תוכן (חייב לעדכן — המבנה השתנה)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # צורה יחידה ישנה — כעת content_filter_results (רבים) בתוך מערך content_filters

# קריאות HTTP גולמיות לנקודת הסיום Chat Completions (חייב לעדכן URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### איוריסטיקות (זיהוי וכתיבה מחדש)

- **לקוח Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **מחוללי לקוח Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **כלים**: המרת הגדרות כלי-קריאת פונקציה מפורמט מקונן (`{"type": "function", "function": {"name": ...}}`) לפורמט שטוח Responses (`{"type": "function", "name": ...}`); השתמש ב-`tool_choice`; החזר תוצאות כלים כפריטים מסוג `{"type": "function_call_output", "call_id": ..., "output": ...}` (ולא `{"role": "tool", ...}`).
- **סיבובי כלים**: כשהמודל מחזיר קריאות פונקציה, יש לצרף את פריטי `response.output` לשיחה (ולא מילון ידני של `{"role": "assistant", "tool_calls": [...]}`), ואז לצרף פריטי `function_call_output` לכל תוצאה.
- **דוגמאות כלי מזעריות**: אם בשיחה קיימות דוגמאות קריאה לכלים מקודדות, המר אותן לפריטים של `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. מזהי הפריטים חייבים להתחיל ב-`fc_`.
- **`pydantic_function_tool()`**: העזרן הזה עדיין מייצר את הפורמט המקונן הישן ואינו **תואם** ל-`responses.create()`. החלף בהגדרות כלים ידניות או במעטפת של שטיחה.
- **ריבוי סבבים**: שמור היסטוריית שיחה באפליקציה; העבר סבבים קודמים בפריטי `input`.
- **עיצוב**: החלף את `response_format` ברמת העליונה של Chat ב-`text.format` ב-Responses. צורה קנונית: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **פריטי תוכן**: החלף את `content[].type: "text"` ב-Chat לפריטי Responses `content[].type: "input_text"` בסבבים של המשתמש/מערכת.
- **פריטי תוכן עם תמונות**: החלף את `content[].type: "image_url"` ב-Chat לפריטי Responses `content[].type: "input_image"`. שדה `image_url` משתנה מאובייקט מקונן `{"url": "..."}` למחרוזת שטוחה. ראו את עלון העזר לדוגמאות לפני/אחרי.
- **מאמץ הסקה**: **העבר רק אם ה-"reasoning" כבר קיים בקוד המקורי**.
- **טיפול בשגיאות סינון תוכן**: מבנה גוף השגיאה השתנה. Chat Completions השתמש ב-`error.body["innererror"]["content_filter_result"]` (יחיד); Responses API משתמש ב-`error.body["content_filters"][0]["content_filter_results"]` (רבים בתוך מערך). גישה ל-`innererror` תגרום ל-`KeyError`. יש לשכתב לשימוש בנתיב החדש.
- **קריאות HTTP גולמיות**: אם האפליקציה מבצעת קריאות ישירות ל-Azure OpenAI REST API (דרך `requests`, `httpx` וכו') עם `/openai/deployments/{name}/chat/completions?api-version=...`, יש לשכתב ל-`/openai/v1/responses`. גוף הבקשה משתנה: `messages` → `input`, מוסיפים `max_output_tokens` ו-`store: false`, מסירים את פרמטר השאילתה `api-version`. גוף התגובה משתנה: `choices[0].message.content` → `output[0].content[0].text` (הערה: `output_text` הוא מאפיין נוחות ב-SDK שלא נמצא ב- JSON דרך REST גולמי).

---

## שלב 2: ביצוע ההגירה

### הערות על ההגירה (Chat Completions → Responses)

- **למה להגר**: Responses הוא ה-API המאוחד לטקסט, כלים וזרימה; Chat Completions הוא ממשק ישן. עם GPT-5, Responses הוא חובה לביצועים מיטביים.
- **HTTP**: נקודת הקצה של Azure משתנה מ-`/openai/deployments/{name}/chat/completions` ל-`/openai/v1/responses`.
- **שדות**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` נשאר ללא שינוי.
- **עיצוב**: `response_format` → `text.format` עם אובייקט תקין.
- **פריטי תוכן**: החלף את `content[].type: "text"` ב-Chat בפריטי Responses `content[].type: "input_text"` בסבבי מערכת/משתמש.
- **פריטי תוכן עם תמונות**: החלף את `content[].type: "image_url"` ב-Chat בפריטי Responses `content[].type: "input_image"`. שטח את שדה `image_url` מ-`{"image_url": {"url": "..."}}` ל-`{"image_url": "..."}` (מחרוזת פשוטה — כתובת URL באמצעות HTTPS או URI של נתוני `data:image/...;base64,...`).

### מפת פרמטרים עזר

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (מערך פריטים) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (אובייקט) |
| `temperature` | `temperature` (ללא שינוי) |
| `stop` | `stop` (ללא שינוי) |
| `frequency_penalty` | `frequency_penalty` (ללא שינוי) |
| `presence_penalty` | `presence_penalty` (ללא שינוי) |
| `tools` / קריאת פונקציה | `tools` (ללא שינוי) |
| `seed` | **הסר** (לא נתמך) |
| `store` | `store` (הוגדר כ-`false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (מחרוזת שטוחה) |

לדוגמאות קוד של מלא לפני/אחרי, ראו [cheat-sheet.md](./references/cheat-sheet.md).

עבור הגירת תשתית בדיקות (מוקים, snapshots, assertions), ראו [test-migration.md](./references/test-migration.md).

לפתרון בעיות שגיאות וטעויות נפוצות, ראו [troubleshooting.md](./references/troubleshooting.md).

---

## שמירת נתונים ומצב

- קבע `store: false` בכל בקשות Responses.
- אל תסתמך על מזהי הודעות קודמות או הקשר המאוחסן בשרת; שמור מצב מנוהל קליינט והקטן מטא-דאטה.

---

## קריטריוני קבלה

### שערים ברמת הקוד (כולם חייבים לעבור)

- [ ] אפס התאמות עבור `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` בקבצים שהוגרו.
- [ ] אפס התאמות עבור `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — כל המחוללים משתמשים ב-`OpenAI`/`AsyncOpenAI` עם נקודת הקצה v1.
- [ ] אפס התאמות עבור `rg "models\.github\.ai|models\.inference\.ai\.azure"` — מסלולי הקוד של GitHub Models הוסרו.
- [ ] אפס התאמות עבור `rg "OpenAIChatCompletionClient"` — קוד MAF 1.0.0+ משתמש ב-`OpenAIChatClient` (שמשתמש ב-Responses API). לגירסאות לפני 1.0.0, שדרג ל-`agent-framework-openai>=1.0.0`.
- [ ] כל קריאות `ChatOpenAI(...)` כוללות `use_responses_api=True`.
- [ ] אפס התאמות עבור `rg "choices\[0\]"` — כל גישה לתגובות משתמשת ב-`resp.output_text` או במבנה פלט Responses.
- [ ] אין `response_format` ברמת עליונה; כל הפלט המובנה משתמש ב-`text={"format": {...}}`.
- [ ] `openai>=1.108.1` ו-`azure-identity` ב-`requirements.txt` או `pyproject.toml`; תלויים מותקנים מחדש.
- [ ] `store=False` מוגדר בכל קריאה ל-`responses.create`.
- [ ] אין `api_version` בבניית הלקוח; `AZURE_OPENAI_API_VERSION` הוסר מקבצי הסביבה והתשתית.

### שערים בתשתית בדיקות (כולם חייבים לעבור)

- [ ] אפס התאמות עבור `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] אפס התאמות עבור `rg "_azure_ad_token_provider" tests/` — האשירות עודכנו לבדוק `isinstance(client, AsyncOpenAI)` או `base_url`.
- [ ] אפס התאמות עבור `rg "prompt_filter_results|content_filter_results" tests/` — מוקים ספציפיים ל-Azure הוסרו.
- [ ] מוקים משתמשים ב-`kwargs.get("input")` ולא ב-`kwargs.get("messages")`.
- [ ] קבצי Snapshot / golden עודכנו לצורת זרימה של Responses (ללא `choices[0]`, `function_call`, `logprobs` וכו').
- [ ] `pytest` עובר ללא כשלונות לאחר כל עדכוני הבדיקות.

### שערים התנהגותיים (אימות ידני או באמצעות מסגרת בדיקות)

- [ ] **השלמה בסיסית**: `responses.create` לא זורם מחזיר `output_text` שאינו ריק.
- [ ] **שוויון בזרימה**: אם הקוד המקורי השתמש בזרימה, הקוד שהוגר זורם ומניב אירועי `response.output_text.delta` עם דלתות שאינן ריקות.
- [ ] **פלט מובנה**: אם משתמשים ב-`text.format` עם `json_schema`, `json.loads(resp.output_text)` מצליח והתוצאה תואמת את הסכמה.
- [ ] **לולאת קריאות כלי**: אם משתמשים בכלים, המודל מבצע קריאות כלים, האפליקציה מריצה אותן, והבקשה ההמשכית מחזירה פלט סופי ב-`output_text` (ללא לולאה אינסופית).
- [ ] **שוויון אסינכרוני**: אם השתמשו ב-`AsyncAzureOpenAI`, מקביל ב-`AsyncOpenAI` עובד עם `await`.
- [ ] **שיעור שגיאות**: אין שגיאות חדשות מסוג 400/401/404 ביחס לרמת הבסיס לפני ההגירה.

### תוצרים

- הסיכום כולל קבצים נערכים, ספירות לפני/אחרי של אתרי קריאה ישנים, ושלבים הבאים.
- השינויים הם רק עריכות בעץ העבודה (ללא commits).

---

## דרישות גרסת SDK

| חבילה | גרסה מינימום |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | העדכנית ביותר (לתעודת EntraID) |

---

## הפניות

- [עלון עזר — כל קטעי הקוד](./references/cheat-sheet.md)
- [הגירת בדיקות — מוקים, snapshots, assertions](./references/test-migration.md)
- [פתרון בעיות — טבלאות סיכונים, משוכות](./references/troubleshooting.md)
- [detect_legacy.py — סורק אוטומטי](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [ערכת התחלה Azure OpenAI](https://aka.ms/openai/start)
- [תיעוד Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [מחזור חיי גרסת Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [מדריך OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->