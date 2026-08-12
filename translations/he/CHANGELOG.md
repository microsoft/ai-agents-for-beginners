# יומן שינויים

כל השינויים החשובים בקורס **סוכני AI למתחילים** מתועדים בקובץ זה.

## [שוחרר] — 2026-07-14

שחרור זה מעביר את הקורס משני דגמים שהוכרזו כמיושנים לאחרונה, מגרה את המחברות שנותרו ל-API היציב של Microsoft Agent Framework, ומאמת את מחברות הפייתון מול פריסת Microsoft Foundry חיה.

### שונה

- **הועברו מדגמים מיושנים (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** שני `gpt-4.1` ו-`gpt-4.1-mini` הוכרזו כמיושנים (תאריך פרישה פורסם **14 אוקטובר 2026**). הוחלפו כל ההפניות בקורס (מסמכים, `.env.example`, מחברות ודוגמאות ב-Python/.NET) ל-`gpt-5-mini` שאינו מיושן. הדוגמה לניתוב מודל בשיעור 16 שומרת על ניגוד קטן/גדול באמצעות `gpt-5-nano` (קטן) ו-`gpt-5-mini` (גדול). קבצים של צד שלישי [15-browser-use/llms.txt](../../15-browser-use/llms.txt), טקסט היסטורי של מודלים ב-GitHub, והערות יכולת לכישורי `azure-openai-to-responses` לא שונו בכוונה.
- **מחברת המסירה של שיעור 14 הועברה ל-API היציב.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) משתמשת כעת ב-`agent_framework.orchestrations.HandoffBuilder` עם `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, סטרימינג מבוסס `event.type`, ו-`FoundryChatClient` (מחליף את הסמלים שהוסרו לפני גרסה 1.0: `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **מחברת הלולאת אדם בשיעור 14 הועברה ל-API היציב.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) עוצרת כעת באמצעות `ctx.request_info(...)` + `@response_handler` (מחליף את `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` שהוסרו), בונה באמצעות `WorkflowBuilder(start_executor=..., output_executors=[...])`, מנהלת פלט מובנה עם `default_options={"response_format": ...}`, ומשתמשת בתשובה מתוכנתת כך שהמחברת פועלת ללא צורך בהתערבות (ללא חסימת `input()`).
- **הגדרות סביבה** ([.env.example](../../.env.example)): הועברו שמות פריסות המודל ל-`gpt-5-mini`; נוספו `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (ניתוב שיעור 16) ו-`AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` שהיה חסר בעבר (שימוש בדפדפן בשיעור 15).
- **תלויות** ([requirements.txt](../../requirements.txt)): נעצו את `agent-framework`, `agent-framework-foundry`, ו-`agent-framework-openai` לגרסה `~=1.10.0` עבור סט עקבי ומאומת (גרסה 1.11.0 כוללת שינויים ניסיוניים משמעותיים לממשקים שמשתמשים בהם בשיעורים אלה).

### הערות ומגבלות ידועות

- **אימות כנגד Microsoft Foundry חיה.** מחברות הפייתון הורצו ללא ממשק גרפי עם `nbconvert` בפרויקט Microsoft Foundry תוך שימוש ב-`gpt-5-mini` (ו-`gpt-5-nano` לניתוב שיעור 16). יש לפרוס דגמים שווי ערך שאינם מיושנים בפרויקט שלכם; המחברות קוראות את שם הפריסה מ-`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **עדיין נדרשים משאבים נוספים לכמה שיעורים.** שיעור 05 זקוק ל-Azure AI Search; זרימת העבודה של שיעור 08 המושתתת על Bing (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) צריכה חיבור ל-Bing וכלים מתארחים של שירות סוכני Microsoft Foundry; שיעור 13 (Cognee) ושיעור 17 (Foundry Local) זקוקים לסביבות ריצה משלהם.

## [שוחרר] — 2026-07-13

שחרור זה מוסיף שני שיעורים חדשים שסוגרים את סביבת הפריסה — סקיילינג של סוכנים אל Microsoft Foundry ופריסה לעמדת עבודה אחת בלבד — בנוסף לצינור בדיקות עישון, ניווט קורס מרענן, מיומנויות לומדים חדשות ומיתוג מעודכן.

### נוסף

- **שיעור 16 — פריסת סוכנים סקלאביליים עם Microsoft Foundry.** שיעור חדש [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) ומחברת להרצה [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) שבונה סוכן תמיכה בלקוחות ייצור (כלים, RAG, זיכרון, ניתוב מודל, מטמון תגובות, אישור אדם, שער הערכה, ועקבות OpenTelemetry), עם דיאגרמות פיתוח/פריסה/ריצה של Mermaid, בדיקת ידע, מטלה ואתגר.
- **שיעור 17 — יצירת סוכני AI מקומיים עם Foundry Local ו-Qwen.** שיעור חדש [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) ומחברת [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) שבונה עוזר הנדסי הפועל כולו על המכשיר (קריאת פונקציות Qwen דרך Foundry Local, כלים עם סנדהבוקס לקבצים, RAG מקומי עם Chroma, MCP מקומי אופציונלי), עם דיאגרמות רק מקומיות / RAG מקומי / קריאת כלים, בדיקת ידע, מטלה ואתגר.
- **צינור בדיקות עישון.** זרימת עבודה חדשה [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) בתוספת קטלוגים לפי שיעור תחת [tests/](./tests/README.md) עבור סוכני הפריסה בשיעורים 01, 04, 05 ו-16, עם README אינדקס שממפה כל קטלוג לשיעור ולשם הסוכן המאוחסן. שיעור 16 מקבל קטע "אימות סוכן פרוס עם בדיקות עישון"; שיעורים 01/04/05 מקבלים מצביע בדיקות עישון אופציונלי.
- **מיומנויות לומדים.** מיומנויות סוכן חדשות תחת `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (שמארזות את ההנחיות לשיעורים 16 ו-17), ו-[testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (כיצד לאמת דוגמאות מחברת מול Microsoft Foundry / Azure OpenAI בשידור חי).
- **מריץ אימות מחברות.** [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) חדש שמריץ כל מחברת פייתון ללא ממשק עם `nbconvert` ומדפיס מטריצת PASS/FAIL (בנוסף ל-`results.json`). מגלה אוטומטית את שורש הריפו ופייתון, מחריג ברירת מחדל מחברות שאינן שייכות לקורס (`.venv`, `site-packages`, `translations`, נכסי תבנית כישור) ו-`.NET`, ותומך ב-`-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, ו-`-Python`.
- **ניווט הקורס.** נוספו קישורי שיעור קודם/הבא לשיעורים 11–15 (שהיו חסרים בעבר) כך שכל הקורס מקושר רציף 00 → 18 בשתי הכיוונים.
- **תמונות מוקטנות חדשות.** תמונות מוקטנות לשיעורים 16 ו-17, בתוספת תמונת ריפו חברתית מרעננת [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (מפרסמת כעת את שני השיעורים החדשים ואת ה-URL `aka.ms/ai-agents-beginners`).
- **תלויות** ([requirements.txt](../../requirements.txt)): נוספו `foundry-local-sdk` ו-`chromadb` לשיעור 17.

### שונה

- **טבלת שיעור ראשית ב-[README.md](./README.md):** שיעורים 16 ו-17 מקשרים כעת לתוכן שלהם (לפני כן "בקרוב"); תמונת הריפו פונתה ל-`repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md):** נוספו שיעורים 16 ו-17 להדרכה שיעור לפי שיעור ולמסלולי הלימוד, וקטע "אימות סוכנים פרוסים עם בדיקות עישון".
- **[AGENTS.md](./AGENTS.md):** עודכן ספירת השיעורים/תיאור (00–18), נוספה סקציית אימות לבדיקה עם בדיקות עישון, ודוגמאות שמות דגימת שיעור 16/17.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md):** "שיעור קודם" מצביע כעת על שיעור 17 (היה שיעור 15), סוגר את השרשרת.
- **איחוד הפניות לדגמים שאינם מיושנים.** הוחלפו כל הפניות ל-`gpt-4o` / `gpt-4o-mini` ברחבי הקורס (מסמכים, `.env.example`, מחברות ודוגמאות Python/.NET) ל-`gpt-4.1-mini` — `gpt-4o` (כל הגרסאות) פורש ב-2026. הדוגמה לניתוב מודל בשיעור 16 שומרת ניגוד קטן/גדול עם `gpt-4.1-mini` (קטן) ו-`gpt-4.1` (גדול). מחברות הפייתון בוחרות כעת את המודל מתוך משתני סביבה (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) במקום קידוד קשיח של שם המודל.

### הערות ומגבלות ידועות

- **לא בוצע מול Azure חיה.** המחברות של השיעורים החדשים הן דוגמאות חינוכיות; הריצו ואמתו אותן מול מערכת Microsoft Foundry / Foundry Local שלכם. זרימת העבודה של בדיקות העישון מחייבת לפרוס את סוכן השיעור ולהגדיר סודות Azure OIDC (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) עם תפקיד **Azure AI User** ברמת הפרויקט ב-Foundry.
- **שיעור 17 הוא מקומי בלבד.** אין לו נקודת קצה Foundry Responses, לכן פעולת בדיקות העישון אינה רלוונטית; אמתו אותו על ידי הרצת המחברת על עמדת העבודה שלכם.

## [שוחרר] — 2026-07-06

שחרור זה מגרה את הקורס ל-**Azure OpenAI Responses API**, מאחד שמות מוצר ב-**Microsoft Foundry** ו-**Microsoft Agent Framework (MAF)**, פורש את GitHub Models, מעדכן גרסאות SDK, ומוסיף תוכן חדש על דגמים מקומיים ואירוח מסגרות אחרות על Foundry.

### נוסף

- **כישור הגירה** — הותקן כישור סוכן [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (מ-[Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) תחת `.agents/skills/`, כולל הפניותיו וסקריפט הסריקה שלו.
- **Foundry Local (הרצת דגמים על המכשיר)** — קטע חדש "ספק אלטרנטיבי: Foundry Local" ב-[00-course-setup/README.md](./00-course-setup/README.md) שמתאר התקנה (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, וחיבור `FoundryLocalManager` ל-Microsoft Agent Framework באמצעות `OpenAIChatClient`.
- **אירוח סוכני LangChain / LangGraph על Microsoft Foundry** — קטע חדש ב-[14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) בתוספת דוגמת הרצה [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) שמשתמש ב-`langchain-azure-ai[hosting]` ו-`ResponsesHostServer` (פרוטוקול `/responses`), מבוסס על [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — קטע חדש "דוגמה מהעולם האמיתי: Microsoft Project Opal" ב-[15-browser-use/README.md](./15-browser-use/README.md) שמציג את Opal כסוכן שימוש מחשב ארגוני וממפה אותו למושאי הקורס (אדם בלולאה, אמון/אבטחה, תכנון, מיומנויות).
- **דוגמת פייתון שנייה לשיעור 02** — נוספה [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (ראה "שונה" — הוגרה ממרכז המכיל הקודם של Semantic Kernel) וקושרה ב-README השיעור.
- נוספה סקציית "מודלים ונותני שירות" ל-[STUDY_GUIDE.md](./STUDY_GUIDE.md).

### שונה

- **Chat Completions → Responses API (פייתון).** דוגמאות שקראו למודל ישירות הועברו מ-Chat Completions ל-Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), תוך שימוש בלקוח `OpenAI` נגד נקודת הקצה היציבה של Azure OpenAI `/openai/v1/` (ללא `api_version`). דוגמאות שנפגעו כוללות:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — הסבר מלא על פונקציית הקריאה (סכמת הכלים הונפה לפורמט Responses, תוצאות הכלים הוחזרו כ-`function_call_output`, `max_output_tokens`, וכו׳).

- **דגמי GitHub → Azure OpenAI.** דגמי GitHub מוצהרים כמיושנים (פורשים **יולי 2026**) ואינם תומכים ב-Responses API. כל מסלולי הקוד של דגמי GitHub הומרו ל-Azure OpenAI / Microsoft Foundry בדוגמאות של Python ו-.NET:
  - Python: מחברות זרימת עבודה של שיעור 08 (`01`–`03`), שיעור 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + מסמכי `.md` נלווים, ומחברות זרימת עבודה של שיעור 08 dotNET/`.md` (`01`–`03`) משתמשות כעת ב-`AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` עם `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** ה-`02-semantic-kernel.ipynb` הקודם נכתב מחדש לשימוש במסגרת Microsoft Agent Framework עם Azure OpenAI (Responses API) ושמו שונה ל-`02-python-agent-framework-azure-openai.ipynb`.
- **התאמה סטנדרטית על `FoundryChatClient` + `as_agent`.** קוד README ומחברת שהפנה ל-`AzureAIProjectAgentProvider` תוקן למערכת הקאנונית בשימוש בשיעור 01 ובדוגמאות המסגרת: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` עם `provider.as_agent(...)`. עודכן בכל README ומחברות של שיעורים 02–14 (לדוגמה, זיכרון בשיעור 13, כל מחברות שיעור 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **כינויים של מוצר.** שונה בתוכן באנגלית כולו:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (ללא שינוי: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", ושמות משתני סביבה.)
- **תלויות** ([requirements.txt](../../requirements.txt)):
  - נעשית נעילה לגרסאות `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - נעשית נעילה ל-`openai>=1.108.1` (מינימום ל-Responses API).
  - הוסר `azure-ai-inference` (ששימש רק בדוגמאות המהגורות של דגמי GitHub).
- **קביעת סביבה** ([.env.example](../../.env.example)): הוסרו משתני GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); נוספו `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, ואופציונלי `AZURE_OPENAI_API_KEY`; עודכן השמות ל-Microsoft Foundry.
- **תיעוד** — עודכן ב-[00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), ו-[STUDY_GUIDE.md](./STUDY_GUIDE.md) עבור האמור לעיל (קביעת משתני סביבה, קטע בדיקה, הנחיות ספק, שמות).

### הוסר

- שלבי כניסה ומשתני סביבה של דגמי GitHub מהמסמכי ההגדרות (הוחלף ב-Azure OpenAI / Microsoft Foundry).

### אבטחה / פרטיות (ניקוי שיתוף ציבורי)

- נקו תוצאות הפעלת מחברות Jupyter שדלפו מזהה מנוי **Azure אמיתי**, שמות קבוצות משאבים / משאבים, ומזהה חיבור Bing, בנוסף לנתיבי קבצים מקומיים ושמות משתמשים של מפתח:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- אומת כי לא נותרו מפתחות API, טוקנים, מזהי מנוי, או נתיבים אישיים בתוכן האנגלי שעובר מעקב (הפניות ל-`GITHUB_TOKEN` שנשארו הן לטוקן GitHub Actions בזרימות עבודה ו-PAT של שרת GitHub MCP בהגדרת שיעור 11 — שניהם לגיטימיים ולא קשורים לדגמי GitHub).

### הערות ומגבלות ידועות

- **לא הופעל/הורץ קוד.** אלו דוגמאות חינוכיות שהותאמו ללכידות API / שמות; לא הופעלו מול משאבי Azure חיים, ודוגמאות ה-.NET לא הורצו בסביבה זו. יש לאמת מול הפריסה האישית שלכם של Microsoft Foundry / Azure OpenAI.
- **פריסת המודל חייבת לתמוך ב-Responses API.** השתמשו בפריסה כגון `gpt-4.1-mini`, `gpt-4.1`, או מודל `gpt-5.x`. דגמים ישנים תומכים בפונקציונליות מרכזית של Responses אך לא בכל התכונות.
- **גרסת הסוכנות:** הדוגמאות מיועדות לגרסת MAF האחרונה (`>=1.10.0`). הקריאה הקאנונית ליצירת סוכן היא `client.as_agent(...)`; APIs אומתו מול תיעוד המסגרת וגרסה מותקנת. אם נעשית נעילה לגרסה שונה, ודאו זמינות שיטות (`as_agent` לעומת `create_agent`).
- **מחברת זרימת עבודה של שיעור 08 מס' 04** שומרת בכוונה על `AzureAIAgentClient` (מ-`agent-framework-azure-ai`) מכיוון שהיא משתמשת בכלי שירות סוכן Microsoft Foundry המותאמים (בינג, מפרש קוד); היא מבוססת Responses.
- **פריסת ברירת מחדל ב-.NET.** שתי דוגמאות זרימת עבודה של שיעור 08 dotNET קודמות קבעו למודל ספציפי; כעת כברירת מחדל משתמשות ב-`AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). אם דוגמה סומכת על קלט מולטימודאלי/ראייה, לקבוע את `AZURE_OPENAI_DEPLOYMENT` למודל מתאים.
- **Foundry Local** חושף נקודת קצה תואמת OpenAI של **שיחות Completion** ומתוכנן לפיתוח מקומי; השתמשו ב-Azure OpenAI / Microsoft Foundry לשימוש מלא בתכונות Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->