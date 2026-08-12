# פתרון בעיות, טבלת סיכונים ו"מלכודות"

## פתרון בעיות 400s

| שגיאה | תיקון |
|-------|-----|
| `missing_required_parameter: tools[0].name` | הגדרת הכלי משתמשת בפורמט מקונן ישן של סיום שיחה | ליישר מ- `{"type": "function", "function": {"name": ...}}` ל- `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters במישור העליון |
| `unknown_parameter: input[N].tool_calls` | תוצאות כלים במספר סבבים משתמשות בפורמט ישן של סיום שיחה | החליף `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` בפריטים של `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | כלי עם `strict: true` חסר מערך `required` | כש- `strict: true`, כל המאפיינים חייבים להיות ברשימת `required` ו- `additionalProperties: false` חייב להיות מוגדר |
| `invalid_function_parameters: 'additionalProperties' is required` | כלי עם `strict: true` חסר `additionalProperties: false` | הוסף `"additionalProperties": false` לאובייקט הפרמטרים |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | מזהה function_call ב-few-shot עם קידומת שגויה | מזהי קריאות פונקציה חייבים להתחיל ב- `fc_` (לדוגמה, `fc_example1`), לא ב- `call_` |
| `missing_required_parameter: text.format.name` | הוסף מפתח `"name"` למילון הפורמט (לדוגמה, `"name": "Output"`) |
| `invalid_type: text.format` | ודא ש- `text.format` הוא מילון עם מפתחות `type`, `name`, `strict`, `schema` — לא מחרוזת |
| `invalid input content type` | השתמש בסוגי תוכן `input_text`/`output_text` במקום Chat `text` |
| `invalid input content type` (תמונה) | תוכן תמונה עדיין משתמש ב- `"type": "image_url"` | שנה ל- `"type": "input_image"` |
| `Expected object, got string` על `image_url` | `image_url` עדיין אובייקט מקונן `{"url": "..."}` | יש ליישר למחרוזת רגילה: `"image_url": "https://..."` או `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` עבור `max_output_tokens` | המינימום הוא **16** ב-Azure OpenAI. השתמש ב-50+ למבחנים, 1000+ לייצור. |
| `429 Too Many Requests` במהלך סטרימינג | מוגבל בקצב. עטוף סטרימינג ב- `try/except`, החזר שגיאת JSON לפרונטאנד, יישם נסיונות חוזרים/המתנה. |
| `KeyError: 'innererror'` בשגיאת מסנן תוכן | מבנה גוף שגיאת מסנן תוכן השתנה ב-Responses API | Chat Completions השתמש ב- `error.body["innererror"]["content_filter_result"]`; Responses API משתמש ב- `error.body["content_filters"][0]["content_filter_results"]` (ברבים, בתוך מערך). הכר את כל הגישה ל- `innererror`. |

---

## טבלת סיכונים במיגרציה

| סימפטום | טעות סבירה | תיקון |
|---------|---------------|-----|
| `output_text` ריק/מוטמע | `max_output_tokens` נמוך מדי עבור דגמי הסקה | הגדר `max_output_tokens=1000` או יותר — אסימוני הסקה נספרים נגד הגבול |
| `400 invalid_type: text.format` | עבר מחרוזת `response_format` במקום מילון `text.format` | השתמש ב- `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` ב- `/openai/v1/responses` | כתובת `base_url` שגויה — חסר סיומת `/openai/v1/` | ודא ש- `base_url=f"{endpoint}/openai/v1/"` (עם סלאש בסוף) |
| `401 Unauthorized` לאחר מעבר ל- `OpenAI()` | `api_key` לא מוגדר או ספק הטוקן לא הועבר כראוי | עבור EntraID: `api_key=token_provider` (הקריאבל). עבור מפתח API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| דגם מחזיר `deployment not found` | פרמטר `model` לא תואם את שם פריסת Azure שלך | השתמש ב- `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — זה שם הפריסה, לא שם הדגם |
| `json.loads(resp.output_text)` מעורר `JSONDecodeError` | הסכמה לא אכפתית או הדגם לא תומך ב-JSON קפדני | ודא ש- `"strict": True` בהסכמה, וודא שהדגם תומך בפלט מובנה |
| סטרימינג לא מחזיר אירועי `delta` | בדיקה של סוג אירוע שגוי | סנן ב- `event.type == "response.output_text.delta"`, לא ב- `chat.completion.chunk` של הצ'אט |
| שגיאת `400` בקלט תמונה אחרי מיגרציה | סוג תוכן תמונה לא עודכן | שנה `"type": "image_url"` → `"type": "input_image"` ויישר `"image_url": {"url": "..."}` → `"image_url": "..."` (מחרוזת רגילה) |
| קריאות כלי במעגל אינסופי | חוסר תוצאות כלי ב- `input` בהמשך | לאחר הפעלת כלי, הוסף פריט `{"type": "function_call_output", "call_id": ..., "output": ...}` לקלט בבקשה הבאה |
| שגיאת `temperature` עם GPT-5 או סדרת o | ערך `temperature` מפורש שאינו 1 | הסר את `temperature` או הגדר ל- `1` עבור דגמי GPT-5 וסדרת o (o1, o3-mini, o3, o4-mini) |
| שגיאת `top_p` עם סדרת o | `top_p` לא נתמך | הסר את `top_p` כאשר מכוונים לדגמי סדרת o |
| `max_completion_tokens` לא מוכרת | שימוש בפרמטר ספציפי ל-Azure | החלף `max_completion_tokens` ב- `max_output_tokens`. הגדר ל-4096+ עבור סדרת o (אסימוני הסקה נספרים נגד הגבול). |
| פלט ריק/מוטמע מסדרת o | `max_output_tokens` נמוך מדי | סדרת o משתמשת באסימוני הסקה פנימיים. הגדר `max_output_tokens=4096` או יותר — לא 500–1000. |
| `400 integer_below_min_value` עבור `max_output_tokens` | ערך מתחת ל-16 | Azure OpenAI דורש `max_output_tokens >= 16`. השתמש ב-50+ למבחני עשן, 1000+ לייצור. |
| `429 Too Many Requests` באמצע סטרימינג | מגבלת קצב על ידי Azure OpenAI | שבר סטרים שקט ללא טיפול בשגיאות. תמיד עטוף `async for event in await coroutine:` ב- `try/except` והחזר `{"error": str(e)}` לפרונטאנד. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | טenant שגוי או לא מחובר | העבר `tenant_id=os.getenv("AZURE_TENANT_ID")` במפורש. הרץ מקומית `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` בשימוש בדגמי GitHub (`models.github.ai`) | דגמי GitHub אינם תומכים ב-Responses API | הסר לחלוטין את מסלול הקוד של דגמי GitHub. השתמש ב-Azure OpenAI, OpenAI או נקודת קצה מקומית תואמת (למשל Ollama עם תמיכה ב-Responses). |
| MAF `OpenAIChatCompletionClient` עדיין משתמש ב-Chat Completions | שימוש בלקוח MAF ישן בגרסת 1.0.0+ | ב-MAF 1.0.0+, `OpenAIChatClient` משתמש ב-Responses API כברירת מחדל. החלף `OpenAIChatCompletionClient` ב- `OpenAIChatClient`. לגרסאות קודמות ל-1.0.0, שדרג ל- `agent-framework-openai>=1.0.0`. |
| סוכן LangChain מחזיר ריק או נכשל עם קריאות כלי | `ChatOpenAI` לא משתמש ב-Responses API | הוסף `use_responses_api=True` ל- `ChatOpenAI(...)`. גם שנה `.content` → `.text` בהודעות תגובה. |
| `KeyError: 'innererror'` בטיפול בשגיאות מסנן תוכן | מבנה גוף השגיאה השתנה ב-Responses API | שנה `error.body["innererror"]["content_filter_result"]["jailbreak"]` ל- `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. עטיפת `innererror` נעלמה; פרטי מסנן התוכן עכשיו במערך עליון `content_filters` עם `content_filter_results` (ברבים) בכל פריט. |
| קריאה HTTP גולמית ל- `/openai/deployments/.../chat/completions` מחזירה 404 | נקודת קצה REST ישנה של Chat Completions | שנה את ה-URL ל- `/openai/v1/responses`. שנה גוף הבקשה: `messages` → `input`, הוסף `max_output_tokens` + `store: false`, הסר פרמטר שאילתא `api-version`. שנה ניתוח תגובה: `choices[0].message.content` → `output[0].content[0].text` (הערה: `output_text` היא נכס נוחות ב-SDK, לא ב-JSON הגולמי של ה-REST). |

---

## מלכודות

1. אם השתמשת בעבר ב-Chat Completions לניהול סטטוס שיחה, נהל את הסטטוס שלך במפורש עם Responses.
2. העדף `max_output_tokens` על פני `max_tokens` ישן.
3. בעת מיגרציה ל- `gpt-5`, ודא ש- `temperature` לא מוגדר או מוגדר ל- `1`.
4. החלף Chat `content[].type: "text"` ב-Responses `content[].type: "input_text"` לקלטי משתמש/מערכת.
5. עבור `text.format`, ספק מילון תקין (לדוגמה, `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), לא מחרוזת פשוטה.
6. פרמטר `seed` לא נתמך ב-Responses; הסר אותו מהבקשות.
7. **הסקה**: כלול `reasoning` רק אם הקוד המקורי כבר השתמש בו. אל תוסיף `reasoning` לקריאות API שלא השתמשו בו — דגמים רבים שאינם להסיקה אינם תומכים בפרמטר זה.
8. **גודל `max_output_tokens`**: עבור דגמי הסקה (GPT-5-mini, GPT-5, סדרת o), השתמש ב- `max_output_tokens=4096` או יותר — לא 50–1000. הדגם משתמש באסימוני הסקה פנימיים לפני יצירת פלט נראה לעין; גבולות נמוכים מדי גורמים לפלט מוטמע או ריק.
9. **`max_completion_tokens` לסדרת o**: אם הקוד המקורי השתמש ב- `max_completion_tokens` (ספציפי ל-Azure לסדרת o), החלף ל- `max_output_tokens`. Responses API אינו מקבל `max_completion_tokens`.
10. **`reasoning_effort` לסדרת o**: אם הקוד המקורי משתמש ב- `reasoning_effort` (נמוך/בינוני/גבוה), המיגר ל- `reasoning={"effort": "<value>"}` בקריאת Responses API.
11. **עיכוב סטרימינג בסדרת o**: דגמי סדרת o מבצעים הסקה פנימית לפני יצירת הפלט. בסטרימינג, צפה לעיכוב ארוך יותר לפני האירוע הראשון `response.output_text.delta`. זה נורמלי — הדגם בהסקה, לא תקוע.
9. **`_azure_ad_token_provider` נעלם**: ל- `AsyncOpenAI` / `OpenAI` אין מאפיין `_azure_ad_token_provider`. בדיקות או קוד המנסים לגשת אליו יכשלו ב- `AttributeError`. ספק הטוקן מועבר כ- `api_key` ואינו ניתן לבדיקה באובייקט הלקוח.
10. **קבצי Snapshot / Golden**: אם חבילת הבדיקות משתמשת בבדיקות snapshot, **כל** קובצי snapshot המכילים צורות סטרימינג של Chat Completions (`choices[0]`, `content_filter_results`, `function_call` וכו') חייבים להתעדכן לצורת Responses החדשה. זה קל לפספס וגורם לכשלות בהצלבת snapshot.
11. **מסלול monkeypatch לדיקה**: מטרה של monkeypatch משנה מ- `openai.resources.chat.AsyncCompletions.create` ל- `openai.resources.responses.AsyncResponses.create` (או `Responses.create` בסינכרוני). שימוש במסלול הישן אינו עושה כלום בשקט — המוק לא יתפוס, והבדיקות יפלו או יכוונו ל-API אמיתי.
12. **`input` לא `messages`**: פונקציות מידול חייבות לקרוא `kwargs.get("input")` ולא `kwargs.get("messages")`. Responses API משתמש ב- `input` להיסטוריית שיחה.
13. **שמות משתני סביבה**: Azure Identity SDK משתמש ב- `AZURE_CLIENT_ID` (לא ב- `AZURE_OPENAI_CLIENT_ID`) עבור `ManagedIdentityCredential(client_id=...)`. שנה זאת בבדיקות, בקבצי `.env`, בהגדרות האפליקציה וב-Bicep/תשתית.
14. **מינימום `max_output_tokens` הוא 16**: Azure OpenAI דוחה ערכים מתחת ל-16 עם `400 integer_below_min_value`. השתמש ב-50 למבחני עשן, 1000+ לייצור. `max_tokens` הישן לא דרש מינימום כזה.
15. **`tenant_id` ל- `AzureDeveloperCliCredential`**: כשהמשאב Azure OpenAI נמצא ב-tenant שונה, חייבים להעביר במפורש `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. בלעדיו, האישורים משתמשים בשקט ב-tenant הלא נכון ומחזירים `401`.
16. **מגבלות קצב מציגות את עצמן שונה בסטרימינג**: עם Chat Completions, 429 בדרך כלל מנע את תחילת הזרם. עם סטרימינג ב-Responses API, 429 יכול להתרחש **באמצע הזרם** — האיטרטור האסינכרוני זורק חריגה. תמיד עטוף את לולאת הסטרימינג ב- `try/except` והחזר שורה של JSON שגיאה כדי שהפרונטאנד יוכל לטפל בזה בעדינות.

17. **טיפול בשגיאות בשידור חי הוא חובה לאפליקציות ווב**: הדפוס `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` הוא קריטי. בלעדיו, זרם SSE/JSONL מת למוות שקט בכל שגיאת צד שרת והפרונטאנד תקוע.
18. **הגדרות כלים חייבות להשתמש בפורמט שטוח**: ה-API של Responses מצפה ל-`{"type": "function", "name": ..., "parameters": ...}` — לא את פורמט הנסטינג של Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. זו השגיאה הנפוצה ביותר במעבר לקוד הפונקציות.
19. **`pydantic_function_tool()` לא תואם**: העזר `openai.pydantic_function_tool()` עדיין מייצר את הפורמט הנסטינג הישן. אל תשתמש בו עם `responses.create()`. הגדירו סכימות כלים ידנית או שטחו את הפלט.
20. **תוצאות כלי משתמשות ב-`function_call_output`, לא ב-`role: tool`**: לאחר ביצוע כלי, הוסיפו `{"type": "function_call_output", "call_id": ..., "output": ...}` — לא `{"role": "tool", "tool_call_id": ..., "content": ...}`. עבור בקשת הכלי של העוזר, השתמשו ב-`messages.extend(response.output)` — ולא במילון ידני של `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` דורש `required` + `additionalProperties: false`**: במהלך שימוש ב-`strict: true` על כלי, כל מאפיין חייב להופיע במערך `required` ו-`additionalProperties` חייב להיות `false`. היעדרות של אחד מהם גורמת לשגיאת 400.
22. **למזהי קריאות פונקציה יש תחיליות ספציפיות**: כשמספקים פריטי `function_call` ב-few-shot ב-`input`, שדה ה-`id` חייב להתחיל ב-`fc_` ושדה ה-`call_id` חייב להתחיל ב-`call_` (למשל `"id": "fc_example1", "call_id": "call_example1"`). שימוש בקידומת הישנה של Chat Completions `call_` עבור `id` נדחה.
23. **GitHub Models אינה תומכת ב-Responses API**: אם לאפליקציה יש נתיב קוד GitHub Models (`base_url` שמפנה ל-`models.github.ai` או `models.inference.ai.azure.com`), הסירו אותו לחלוטין. אין נתיב העברה — עברו ל-Azure OpenAI, OpenAI, או נקודת קצה מקומית תואמת.
24. **מבנה גוף שגיאת מסנן תוכן השתנה**: שגיאות Chat Completions השתמשו ב-`error.body["innererror"]["content_filter_result"]` (יחיד). שגיאות Responses API משתמשות ב-`error.body["content_filters"][0]["content_filter_results"]` (רבים, בתוך מערך). המפתח `innererror` כבר לא קיים. קוד שניגש ישירות ל-`innererror` יגרום ל-`KeyError` בזמן ריצה — קל לפספס זאת במעבר כי זה קורה רק כשהמסנן תוכן באמת מופעל. תמיד חפשו `innererror` במהלך המעבר.
25. **קריאות HTTP גולמיות דורשות שינוי ב-כתובת ובגוף**: אפליקציות שקוראות ל-Azure OpenAI REST ישירות (באמצעות `requests`, `httpx`, `aiohttp`) שמשתמשות ב-`/openai/deployments/{name}/chat/completions?api-version=...` חייבות לעבור ל-`/openai/v1/responses`. גוף הבקשה משתמש ב-`input` במקום `messages`, דורש `max_output_tokens` ו-`store`, ופרמטר השאילתה `api-version` מוסר. טקסט גוף התגובה נמצא ב-`output[0].content[0].text` — **לא** ב-`output_text`, שהוא תכונת נוחות של SDK שאינה קיימת ב-JSON הגולמי של REST.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->