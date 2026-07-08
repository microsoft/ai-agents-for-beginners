# יומן שינויים

כל השינויים הבולטים בקורס **סוכני AI למתחילים** מתועד בקובץ זה.

## [לא שוחרר] — 2026-07-06

גרסה זו מגדילה את הקורס ל-**Azure OpenAI Responses API**, מאחדת את שמות המוצרים ב-**Microsoft Foundry** וב-**Microsoft Agent Framework (MAF)**, מפסיקה את השימוש בדגמי GitHub, מעדכנת גרסאות SDK, ומוסיפה תוכן חדש על דגמים מקומיים ואירוח מסגרות נוספות ב-Foundry.

### נוספו

- **כישור העברה** — הותקן הכישור של הסוכן [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) (מ-[Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) תחת `.agents/skills/`, כולל הפניות וסקריפט סריקה.
- **Foundry במחשב מקומי (הפעלת דגמים במכשיר)** — פרק חדש "ספק חלופי: Foundry Local" ב-[00-course-setup/README.md](./00-course-setup/README.md) שמתאר התקנה (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` וחיבור `FoundryLocalManager` ל-Microsoft Agent Framework דרך `OpenAIChatClient`.
- **אירוח סוכני LangChain / LangGraph ב-Microsoft Foundry** — פרק חדש ב-[14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) ודוגמת קוד להפעלה [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) בשימוש ב-`langchain-azure-ai[hosting]` ו-`ResponsesHostServer` (פרוטוקול `/responses`), בהתבסס על [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **פרויקט Opal של מיקרוסופט** — פרק חדש "דוגמה מהעולם האמיתי: פרויקט Opal של מיקרוסופט" ב-[15-browser-use/README.md](./15-browser-use/README.md) שמציג את Opal כסוכן שימוש מחשב ארגוני וממפה אותו למושגי הקורס (מעורבות אדם, אמון/אבטחה, תכנון, כישורים).
- **דוגמה שנייה בשיעור 02 Python** — נוסף [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (ראה "שונה" — הועבר מהמחברת Semantic Kernel לשעבר) וקישור אליה בקובץ README של השיעור.
- נוסף פרק **דגמים וספקים** ל-[STUDY_GUIDE.md](./STUDY_GUIDE.md).

### שונה

- **השלמות שיחה → Responses API (Python).** דוגמאות שפנו במישרין לדגם עברו מ-Chat Completions ל-Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), תוך שימוש בלקוח `OpenAI` כנגד נקודת הקצה היציבה של Azure OpenAI `/openai/v1/` (ללא `api_version`). דוגמאות מושפעות כוללות:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — ההליכה המלאה של קריאת הפונקציה (סקמת הכלים הומרה לפורמט Responses, תוצאות הכלי הוחזרו כ-`function_call_output`, `max_output_tokens` וכו').
- **דגמי GitHub → Azure OpenAI.** דגמי GitHub הוקפאו (יפסיקו לפעול **ביולי 2026**) ואינם תומכים ב-Responses API. כל דרכי הקוד לדגמי GitHub הומרו ל-Azure OpenAI / Microsoft Foundry בדוגמאות פייתון ו-.NET:
  - פייתון: מחברות עבודה של שיעור 08 (`01`–`03`), שיעור 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + מסמכי `.md` נלווים, ומחברות עבודה/`.md` של שיעור 08 dotNET (`01`–`03`) משתמשות כעת ב-`AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` עם `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** המחברת לשעבר `02-semantic-kernel.ipynb` נוסחה מחדש לשימוש ב-Microsoft Agent Framework עם Azure OpenAI (Responses API) ושונה שמה ל-`02-python-agent-framework-azure-openai.ipynb`.
- **סטנדרטיזציה על `FoundryChatClient` + `as_agent`.** קוד ה-README והמחברות שהפנו ל-`AzureAIProjectAgentProvider` סטנדרטיזו לתבנית הקנונית של שיעור 01 ודוגמאות המסגרת עצמן: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` עם `provider.as_agent(...)`. עודכן ב-README ובמחברות של שיעורים 02–14 (למשל, זיכרון בשיעור 13, כל מחברות שיעור 14, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **שם מוצר.** שונה בכל תוכן האנגלית:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (לא שונה: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", ושמות משתני סביבה.)
- **תלויות** ([requirements.txt](../../requirements.txt)):
  - נעצרו על `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - נעצר על `openai>=1.108.1` (מינימום ל-Responses API).
  - הוסר `azure-ai-inference` (השתמשו בו רק בדוגמאות GitHub Models שהועברו).
- **הגדרת סביבה** ([.env.example](../../.env.example)): הוסרו משתני GitHub Models (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); נוספו `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, ואפשרי `AZURE_OPENAI_API_KEY`; עודכנו שמות של Microsoft Foundry.
- **תיעוד** — עודכן ב-[00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), ו-[STUDY_GUIDE.md](./STUDY_GUIDE.md) לגבי האמור מעלה (הגדרת משתני סביבה, קטע אימות, הדרכת ספקים, שמות).

### הוסר

- שלבים למעבר לדגמי GitHub ומשתני סביבה מדפי ההתקנה (הוחלפו ב-Azure OpenAI / Microsoft Foundry).

### אבטחה / פרטיות (ניקוי שיתוף פומבי)

- נמחקו תוצאות הרצת מחברות Jupyter שדלפו את **מזהה המנוי האמיתי של Azure**, שמות קבוצות משאבים / משאבים, ומזהה חיבור Bing, וכן **נתיבי קבצים מקומיים ושמות משתמשים של המפתח**, ב:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- אותר שאינו קיים מפתחות API, אסימונים, מזהי מנוי או נתיבים אישיים בתוכן האנגלי שעבר מעקב (הפניות ל-`GITHUB_TOKEN` שנותרו הן אסימוני GitHub Actions בזרימות עבודה ו-PAT של שרת GitHub MCP בהתקנת שיעור 11 — שניהם לגיטימיים ולא קשורים ל-GitHub Models).

### הערות ומגבלות ידועות

- **לא בוצעו/לא קומפלו.** אלו דוגמאות חינוכיות שהותאמו לשם נכונות API/שמות; לא הורצו מול משאבי Azure חיים, ודוגמאות .NET לא אוחדו בסביבה זו. יש לוודא מול פריסת Microsoft Foundry / Azure OpenAI שלכם.
- **הפריסה חייבת לתמוך ב-Responses API.** יש להשתמש בפריסה כגון `gpt-4o-mini`, `gpt-4.1`, או דגם `gpt-5.x`. דגמים ישנים תומכים בפונקציונליות יסודית של Responses אך לא בכל התכונות.
- **גרסת agent-framework.** הדוגמאות מיועדות לגרסה העדכנית ביותר של MAF (`>=1.10.0`). הקריאה הקנונית ליצירת סוכן היא `client.as_agent(...)`; API אומתו מול התיעוד הפומבי ומבנה מותקן. אם אתם משתמשים בגרסה שונה, יש לוודא זמינות מתודות (`as_agent` לעומת `create_agent`).
- **מחברת עבודה של שיעור 08, 04** שומרת במכוון על `AzureAIAgentClient` (מ-`agent-framework-azure-ai`) מאחר שהיא משתמשת בכלי אירוח Microsoft Foundry Agent Service (אחיזת Bing, פרשן קוד); היא כבר מבוססת Responses.
- **פריסת ברירת מחדל ל-.NET.** שתי דוגמאות עבודה של שיעור 08 dotNET שנתנו קוד קשה ל-`gpt-4o` מומרות להשתמש כברירת מחדל ב-`AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). אם דוגמה דורשת קלט מולטימודלי/חזותי, יש להגדיר את `AZURE_OPENAI_DEPLOYMENT` לדגם מתאים.
- **Foundry Local** מציע נקודת קצה של **Chat Completions** תואמת OpenAI ומיועד לפיתוח מקומי; יש להשתמש ב-Azure OpenAI / Microsoft Foundry לכיסוי מלא של תכונות Responses API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->