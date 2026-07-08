# פתרון בעיות, טבלת סיכונים ו-Gotchas

## פתרון בעיות אבחנות 400

| שגיאה | תיקון |
|-------|-----|
| `missing_required_parameter: tools[0].name` | הגדרת כלי משתמשת בפורמט ישן של Chat Completions מקונן | לשטח מ- `{"type": "function", "function": {"name": ...}}` ל- `{"type": "function", "name": ..., "parameters": ...}` — שם, תיאור ופרמטרים בלבלט העליון |
| `unknown_parameter: input[N].tool_calls` | תוצאות כלים במספר פניות משתמשות בפורמט ישן של Chat Completions | החלף `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` בפריטים של `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | כלי עם `strict: true` חסר מערך `required` | כשהוא `strict: true`, כל המאפיינים חייבים להיכלל ב-`required` ולכלול `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | כלי עם `strict: true` חסר `additionalProperties: false` | הוסף `"additionalProperties": false` לאובייקט הפרמטרים |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | מזהה של קריאה לפונקציה במצב Few-shot עם קידומת שגויה | מזהי קריאה לפונקציה חייבים להתחיל ב- `fc_` (למשל `fc_example1`), לא ב- `call_` |
| `missing_required_parameter: text.format.name` | הוסף מפתח `"name"` למילון הפורמט (למשל `"name": "Output"`) |
| `invalid_type: text.format` | ודא ש-`text.format` הוא מילון עם המפתחות `type`, `name`, `strict`, `schema` — לא מחרוזת |
| `invalid input content type` | השתמש בסוגי תוכן `input_text`/`output_text` במקום Chat `text` |
| `invalid input content type` (image) | תוכן תמונה עדיין משתמש ב- `"type": "image_url"` | שנה ל- `"type": "input_image"` |
| `Expected object, got string` על `image_url` | `image_url` עדיין אובייקט מקונן `{"url": "..."}` | שטח למחרוזת פשוטה: `"image_url": "https://..."` או `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` עבור `max_output_tokens` | המינימום הוא **16** ב-Azure OpenAI. השתמש ב-50+ למבחנים, 1000+ לייצור. |
| `429 Too Many Requests` במהלך סטרימינג | עומס הגבלת שיער. עוטף את הסטרימינג ב- `try/except`, מחזיר JSON שגיאה לקצה הלקוח, מיישם נסיונות חוזרים |
| `KeyError: 'innererror'` בשגיאת פילטר תוכן | מבנה גוף שגיאת פילטר התוכן השתנה ב-Responses API | Chat Completions השתמש ב- `error.body["innererror"]["content_filter_result"]`; Responses API משתמש ב- `error.body["content_filters"][0]["content_filter_results"]` (ברבים, בתוך מערך). שנה את כל הגישה ל-`innererror`. |

---

## טבלת סיכוני הגירה

| סימפטום | טעות סבירה | תיקון |
|---------|---------------|-----|
| `output_text` ריק / תגובה מקוצצת | `max_output_tokens` נמוך מדי לדגמי הסקת מסקנות | הגדר `max_output_tokens=1000` או יותר — אסימוני הסקה נספרים למגבלה |
| `400 invalid_type: text.format` | נמסר מחרוזת `response_format` במקום מילון `text.format` | השתמש ב- `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` ב- `/openai/v1/responses` | `base_url` שגוי — חסר סיומת `/openai/v1/` | ודא `base_url=f"{endpoint}/openai/v1/"` (עם סלאש בסוף) |
| `401 Unauthorized` לאחר מעבר ל- `OpenAI()` | `api_key` לא הוגדר או ספק אותות לא הועבר נכון | ל-EntraID: `api_key=token_provider` (הקריאבל). למפתח API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| המודל מחזיר `deployment not found` | פרמטר `model` אינו תואם לשם הפריסה שלך ב-Azure | השתמש ב- `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — זה שם הפריסה, לא שם המודל |
| `json.loads(resp.output_text)` מעלה `JSONDecodeError` | הסכמה לא מאוכפת או המודל לא תומך ב-JSON מחמיר | ודא `"strict": True` בסכמה, ואמת תמיכה ביציאה מובנית במודל |
| סטרימינג לא מחזיר אירועי `delta` | בודק סוג אירוע שגוי | סנן לפי `event.type == "response.output_text.delta"`, לא Chat `chat.completion.chunk` |
| שגיאת 400 על קלט תמונה לאחר הגירה | סוג תוכן תמונה לא עודכן | שנה `"type": "image_url"` → `"type": "input_image"` ושטח `"image_url": {"url": "..."}` → `"image_url": "..."` (מחרוזת פשוטה) |
| קריאות לכלי מסתובבות אינסופית | חסר תוצאת כלי ב- `input` לפנייה הבאה | לאחר ביצוע כלי, הוסף פריט `{"type": "function_call_output", "call_id": ..., "output": ...}` ל- `input` בבקשה הבאה |
| שגיאת `temperature` עם GPT-5 או סדרת o | ערך `temperature` מפורש שאינו 1 | הסר `temperature` או הגדר ל- `1` לדגמי GPT-5 וסדרת o (o1, o3-mini, o3, o4-mini) |
| שגיאת `top_p` עם סדרת o | `top_p` לא נתמכת | הסר את `top_p` כשמכוונים לדגמי סדרת o |
| `max_completion_tokens` לא מוכר | שימוש בפרמטר ספציפי ל-Azure | החלף `max_completion_tokens` ב- `max_output_tokens`. הגדר ל- 4096+ לסדרת o (אסימוני הסקה נספרים למגבלה). |
| פלט ריק/מקוצץ מסדרת o | `max_output_tokens` נמוך מדי | סדרת o משתמשת באסימוני הסקה פנימיים. הגדר `max_output_tokens=4096` או יותר — לא 500–1000. |
| `400 integer_below_min_value` עבור `max_output_tokens` | ערך מתחת ל-16 | Azure OpenAI מחייב `max_output_tokens >= 16`. השתמש ב-50+ למבחני עשן, 1000+ לייצור. |
| `429 Too Many Requests` באמצע סטרימינג | הגבלה על ידי Azure OpenAI | הסטרים נשבר בשקט ללא טיפול בשגיאה. עוטף תמיד `async for event in await coroutine:` ב- `try/except` ומחזיר `{"error": str(e)}` לקצה הלקוח. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | טננט שגוי או לא מחובר | העבר `tenant_id=os.getenv("AZURE_TENANT_ID")` במפורש. הרץ `azd auth login --tenant <tenant-id>` במכונה המקומית. |
| `404 Not Found` בשימוש ב-GitHub Models (`models.github.ai`) | GitHub Models לא תומכים ב-Responses API | הסר לחלוטין את מסלול הקוד של GitHub Models. השתמש ב-Azure OpenAI, OpenAI, או נקודת קצה מקומית תואמת (למשל Ollama עם תמיכה ב-Responses). |
| MAF `OpenAIChatCompletionClient` עדיין משתמש ב-Chat Completions | שימוש בלקוח MAF ישן בגרסה 1.0.0+ | ב- MAF 1.0.0+ `OpenAIChatClient` משתמש ב-Responses API כברירת מחדל. החלף `OpenAIChatCompletionClient` ב- `OpenAIChatClient`. לגרסאות לפני 1.0.0, שדרג ל- `agent-framework-openai>=1.0.0`. |
| סוכן LangChain מחזיר ריק או נכשל עם קריאות כלים | `ChatOpenAI` לא משתמש ב-Responses API | הוסף `use_responses_api=True` ל- `ChatOpenAI(...)`. גם שנה `.content` ל- `.text` בהודעות התגובה. |
| `KeyError: 'innererror'` בטיפול בשגיאת פילטר תוכן | מבנה גוף השגיאה השתנה ב-Responses API | שנה `error.body["innererror"]["content_filter_result"]["jailbreak"]` ל- `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. המעטפת `innererror` בוטלה; פרטי פילטר התוכן נמצאים כעת במערך עליון `content_filters` עם `content_filter_results` (ברבים) בכל כניסה. |
| קריאה HTTP גולמית ל- `/openai/deployments/.../chat/completions` מחזירה 404 | נקודת קצה ישנה של Chat Completions REST | שנה את כתובת ה-URL ל- `/openai/v1/responses`. שנה גוף הבקשה: מ- `messages` ל- `input`, הוסף `max_output_tokens` + `store: false`, הסר פרמטר שאילתה `api-version`. שנה ניתוח תגובה: `choices[0].message.content` ל- `output[0].content[0].text` (הערה: `output_text` הוא מאפיין נוחות ב-SDK, לא ב-JSON הגולמי של REST). |

---

## Gotchas

1. אם השתמשת קודם ב-Chat Completions למצב שיחה, נהל את המצב שלך במפורש עם Responses.
2. העדף `max_output_tokens` מעל `max_tokens` הישן.
3. בעת מעבר ל- `gpt-5`, ודא ש-`temperature` לא מוגדר או שהוגדר ל- `1`.
4. החלף Chat `content[].type: "text"` ב-Responses `content[].type: "input_text"` לקלטי משתמש/מערכת.
5. עבור `text.format`, ספק מילון תקני (למשל `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), לא מחרוזת פשוטה.
6. הפרמטר `seed` אינו נתמך ב-Responses; הסר אותו מהבקשות.
7. **הסקת מסקנות**: כלול `reasoning` רק אם הקוד המקורי כבר השתמש בו. אל תוסיף `reasoning` לקריאות API שלא היו בהן — דגמים רבים (למשל gpt-4o-mini) אינם תומכים בפרמטר זה.
8. **גודל `max_output_tokens`**: לדגמי הסקת מסקנות (GPT-5-mini, GPT-5, o-series), השתמש ב- `max_output_tokens=4096` או יותר — לא 50–1000. המודל משתמש באסימוני הסקה פנימיים לפני יצירת הפלט הנראה; מגבלות נמוכות מדי גורמות לתגובות מקוצצות או ריקות.
9. **`max_completion_tokens` בסדרת O**: אם הקוד המקורי השתמש ב- `max_completion_tokens` (ספציפי ל-Azure עבור סדרת o), החלף ב- `max_output_tokens`. Responses API אינו מקבל `max_completion_tokens`.
10. **`reasoning_effort` בסדרת O**: אם הקוד המקורי משתמש ב- `reasoning_effort` (נמוך/בינוני/גבוה), העבר ל- `reasoning={"effort": "<value>"}` בקריאת ה-Responses API.
11. **עיכוב סטרימינג בסדרת O**: דגמי סדרת o מבצעים הסקת מסקנות פנימית לפני יצירת הפלט. בסטרימינג, צפה לעיכוב ארוך יותר לפני אירוע `response.output_text.delta` הראשון. זה נורמלי — המודל מבצע הסקה, לא תקוע.
9. **`_azure_ad_token_provider` נעלם**: ל- `AsyncOpenAI` / `OpenAI` אין תכונה `_azure_ad_token_provider`. מבחנים או קוד שניגשים אליה יכשלו ב- `AttributeError`. ספק האותות מועבר כ- `api_key` ואינו ניתן לבדיקה באובייקט הלקוח.
10. **קבצי Snapshot / זהב**: אם ערכת המבחנים משתמשת בבדיקות snapshot, **כל** קבצי ה-snapshot המכילים מבני סטרימינג של Chat Completions (`choices[0]`, `content_filter_results`, `function_call`, וכו') חייבים להיות מעודכנים למבנה החדש של Responses. זה קל לפספס וגורם לכשל בטעויות snapshot.
11. **נתיב monkeypatch של Mock**: יעד ה-monkeypatch משתנה מ- `openai.resources.chat.AsyncCompletions.create` ל- `openai.resources.responses.AsyncResponses.create` (או `Responses.create` לסינכרוני). שימוש בנתיב הישן לא עושה כלום בשקט — ה-mock לא יירט, והמבחנים פונים ל-API האמיתי או נכשל.
12. **`input` לא `messages`**: פונקציות mock חייבות לקרוא `kwargs.get("input")` ולא `kwargs.get("messages")`. Responses API משתמש ב- `input` להיסטוריית שיחה.
13. **שם משתנה סביבה**: Azure Identity SDK משתמש ב- `AZURE_CLIENT_ID` (לא ב- `AZURE_OPENAI_CLIENT_ID`) ל- `ManagedIdentityCredential(client_id=...)`. שנה במבחנים, קבצי `.env`, הגדרות אפליקציה ומבנה/תשתית Bicep.
14. **הקטן המינימלי של `max_output_tokens` הוא 16**: Azure OpenAI דוחה ערכים מתחת ל-16 עם שגיאת `400 integer_below_min_value`. השתמש ב-50 למבחני עשן, 1000+ לייצור. ב-`max_tokens` הישן לא היה מינימום כזה.
15. **`tenant_id` ל-`AzureDeveloperCliCredential`**: כשמשאב Azure OpenAI נמצא בטננט שונה, חובה להעביר `tenant_id` במפורש — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. בלעדיו, האישורים ישתמשו בשקט בטננט שגוי ויחזירו `401`.
16. **הגבלות קצב מופיעות בצורה שונה בסטרימינג**: עם Chat Completions, שגיאת 429 בדרך כלל מנעה התחלת סטרים. עם סטרימינג של Responses API, שגיאת 429 יכולה להתרחש **באמצע סטרים** — האיטרטור האסינכרוני מעלה חריגה. עטוף תמיד את לולאת הסטרימינג ב- `try/except` והחזר שורת JSON של שגיאה כדי שהממשק יוכל לטפל בה בצורה חלקה.

17. **טיפול שגיאות בזרימה חובה לאפליקציות ווב**: התבנית `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` היא קריטית. בלעדיה, זרם ה-SSE/JSONL מת כשקט על כל שגיאת שרת וה-frontend נתקע.
18. **הגדרות כלים חייבות להשתמש בפורמט שטוח**: ה-API של Responses מצפה ל-`{"type": "function", "name": ..., "parameters": ...}` — ולא לפורמט המקונן של Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. זו השגיאה הנפוצה ביותר במיגרציה בקוד הקריאה לפונקציות.
19. **`pydantic_function_tool()` אינו תואם**: העזר `openai.pydantic_function_tool()` עדיין יוצר את הפורמט המקונן הישן. אל תשתמש בו עם `responses.create()`. הגדר סכמות כלי ידנית או שטח את הפלט.
20. **תוצאות כלים משתמשות ב-`function_call_output`, לא ב-`role: tool`**: לאחר ביצוע כלי, הוסף `{"type": "function_call_output", "call_id": ..., "output": ...}` — לא `{"role": "tool", "tool_call_id": ..., "content": ...}`. לבקשת הכלי של העוזר, השתמש ב-`messages.extend(response.output)` — לא במילון ידני של `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` דורש `required` + `additionalProperties: false`**: בשימוש ב-`strict: true` בכלי, כל מאפיין חייב להופיע במערך `required` ו-`additionalProperties` חייב להיות `false`. העדר אחד מהם גורם לשגיאת 400.
22. **לקריאות פונקציה יש קידומות ספציפיות**: במתן פריטים בודדים של `function_call` ב-`input`, שדה ה-`id` חייב להתחיל ב-`fc_` ושדה ה-`call_id` חייב להתחיל ב-`call_` (למשל `"id": "fc_example1", "call_id": "call_example1"`). שימוש בקידומת הישנה של Chat Completions `call_` עבור `id` נדחה.
23. **GitHub Models אינם תומכים ב-Responses API**: אם האפליקציה כוללת נתיב קוד ל-GitHub Models (`base_url` מצביע על `models.github.ai` או `models.inference.ai.azure.com`), הסר אותו לחלוטין. אין נתיב מיגרציה — החלף ל-Azure OpenAI, OpenAI, או נקודת קצה מקומית תואמת.
24. **מבנה גוף שגיאות של מסנן תוכן השתנה**: שגיאות Chat Completions השתמשו ב-`error.body["innererror"]["content_filter_result"]` (יחיד). שגיאות Responses API משתמשות ב-`error.body["content_filters"][0]["content_filter_results"]` (ברבים, בתוככי מערך). המפתח `innererror` כבר לא קיים. קוד שניגש ישירות ל-`innererror` יגרום ל-`KeyError` בזמן ריצה — זה קל לפספס במיגרציה כי זה מתגלה רק כשהמסנן אכן מופעל. תמיד חפש `innererror` במהלך מיגרציה.
25. **קריאות HTTP גולמיות דורשות כתובת URL + גוף משודרג**: אפליקציות שקוראות ישירות ל-Azure OpenAI REST (באמצעות `requests`, `httpx`, `aiohttp`) עם `/openai/deployments/{name}/chat/completions?api-version=...` חייבות לעבור ל-`/openai/v1/responses`. גוף הבקשה משתמש ב-`input` במקום `messages`, דורש את `max_output_tokens` ואת `store`, ופרמטר השאילתה `api-version` מושמט. טקסט גוף התגובה נמצא ב-`output[0].content[0].text` — **לא** ב-`output_text`, שהוא שדה נוחות ב-SDK שלא קיים ב-JSON הגולמי של ה-REST.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->