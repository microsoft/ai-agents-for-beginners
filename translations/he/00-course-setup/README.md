# הגדרת הקורס

## מבוא

שיעור זה יכסה כיצד להריץ את דוגמאות הקוד של הקורס הזה.

## הצטרפות ללומדים אחרים וקבלת עזרה

לפני שאתה מתחיל לשכפל את המאגר שלך, הצטרף ל-[ערוץ ה-Discord של AI Agents For Beginners](https://aka.ms/ai-agents/discord) לקבלת עזרה בהגדרה, שאלות על הקורס, או להתחבר עם לומדים אחרים.

## שכפל או הפרד מאגר זה

כדי להתחיל, אנא שכפל או הפרד את מאגר GitHub. זה ייצור עבורך גרסה משולפת של חומר הקורס כדי שתוכל להריץ, לבדוק, ולהתאים את הקוד!

ניתן לעשות זאת על ידי לחיצה על הקישור ל- <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">הפרדת המאגר</a>

כעת אמורה להיות לך גרסה משולפת של הקורס בקישור הבא:

![Forked Repo](../../../translated_images/he/forked-repo.33f27ca1901baa6a.webp)

### שכפול רדוד (מומלץ לסדנה / Codespaces)

  >המאגר המלא יכול להיות גדול (~3 GB) כאשר אתה מוריד היסטוריה מלאה וכל הקבצים. אם אתה משתתף רק בסדנה או צריך רק כמה תיקיות של שיעורים, שכפול רדוד (או שכפול דליל) יוריד הרבה פחות.

#### שכפול רדוד מהיר — היסטוריה מינימלית, כל הקבצים

החלף את `<your-username>` בפקודות למטה עם כתובת ה-URL של ההפרדה שלך (או כתובת ה-URL של המקור אם אתה מעדיף).

לשכפל רק את ההיסטוריה של הקומיט האחרון (הורדה קטנה):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

לשכפל סניף ספציפי:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### שכפול חלקי (דליל) — בלובים מינימליים + רק תיקיות נבחרות

זה משתמש בשכפול חלקי ושליפת sparse (דורש Git 2.25+ ומומלץ להשתמש בגיט מודרני עם תמיכה בשכפול חלקי):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

עבור לתיקיית המאגר:

```bash
cd ai-agents-for-beginners
```

לאחר מכן ציין אילו תיקיות אתה רוצה (הדוגמה למטה מציגה שתי תיקיות):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

לאחר השכפול ואימות הקבצים, אם אתה צריך רק את הקבצים ורוצה לשחרר מקום (ללא היסטוריית גיט), מחק את מטא-דאטת המאגר (💀לא הפיך — תאבד את כל פונקציונליות Git):

```bash
# זש/בש
rm -rf .git
```

```powershell
# פאורשל
Remove-Item -Recurse -Force .git
```

#### שימוש ב-GitHub Codespaces (מומלץ להימנע מהורדות מקומיות גדולות)

- צור Codespace חדש למאגר זה דרך [ממשק GitHub](https://github.com/codespaces).  

- בטרמינל של ה-Codespace שנוצר, הרץ אחת מפקודות השכפול הרדוד/הדליל שלמעלה כדי להביא רק את תיקיות השיעורים שאתה צריך לתוך סביבת העבודה של Codespace.
- אופציונלי: לאחר השכפול בתוך Codespaces, הסר את .git כדי לפנות מקום נוסף (ראה פקודות ההסרה למעלה).
- הערה: אם אתה מעדיף לפתוח את המאגר ישירות ב-Codespaces (בלי שכפול נוסף), הייה מודע כי Codespaces יבנה את סביבת הפיתוח וייתכן ועדיין יספק יותר ממה שאתה צריך.

#### טיפים

- תמיד החלף את כתובת השכפול עם ההפרדה שלך אם ברצונך לערוך/לבצע קומיט.
- אם תזדקק מאוחר יותר להיסטוריה או לקבצים נוספים, ניתן להביא אותם או להתאים את ה-sparse-checkout לכלול תיקיות נוספות.

## הרצת הקוד

הקורס מציע סדרת מחברות Jupyter שאתה יכול להריץ כדי לקבל ניסיון מעשי בבניית סוכני AI.

דוגמאות הקוד משתמשות ב-**Microsoft Agent Framework (MAF)** עם `FoundryChatClient`, שמתחבר ל-**Microsoft Foundry Agent Service V2** (ממשק ה-Responses API) דרך **Microsoft Foundry**.

כל מחברות הפייתון מתויגות כ-`*-python-agent-framework.ipynb`.

## דרישות

- פייתון 3.12+
  - **הערה**: אם אין לך פייתון 3.12 מותקן, ודא להתקינו. לאחר מכן צור את סביבת ה-venv שלך באמצעות python3.12 כדי לוודא שגרסאות נכונות מותקנות מתוך קובץ requirements.txt.
  
    >דוגמה

    צור תיקיית סביבת פייתון וירטואלית:

    ```bash
    python -m venv venv
    ```

    לאחר מכן הפעל את סביבת ה-venv עבור:

    ```bash
    # זש/בש
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: עבור דוגמאות הקוד המשתמשות ב-.NET, ודא להתקין את [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) או מאוחר יותר. לאחר מכן, בדוק את גרסת ה-SDK שלך:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — דרוש לאימות. התקן מ-[aka.ms/installazurecli](https://aka.ms/installazurecli).
- **מנוי Azure** — לגישה ל-Microsoft Foundry ול-Microsoft Foundry Agent Service.
- **פרויקט Microsoft Foundry** — פרויקט עם מודל פרוס (למשל, `gpt-5-mini`). ראה [שלב 1](#שלב-1-צור-פרויקט-microsoft-foundry) למטה.

כללנו קובץ `requirements.txt` בשורש המאגר שמכיל את כל החבילות הנדרשות עבור פייתון להרצת דוגמאות הקוד.

תוכל להתקין אותן על ידי הרצת הפקודה הבאה בטרמינל שלך בשורש המאגר:

```bash
pip install -r requirements.txt
```

אנו ממליצים ליצור סביבת עבודה וירטואלית בפייתון כדי להימנע מקונפליקטים ובעיות.

## הגדרת VSCode

ודא שאתה משתמש בגרסת הפייתון הנכונה ב-VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## הגדרת Microsoft Foundry ו-Microsoft Foundry Agent Service

### שלב 1: צור פרויקט Microsoft Foundry

אתה צריך **hub** ו-**פרויקט** ב-Microsoft Foundry עם מודל פרוס כדי להריץ את המחברות.

1. עבור ל-[ai.azure.com](https://ai.azure.com) והתחבר עם חשבון Azure שלך.
2. צור **hub** (או השתמש בקיים). ראה: [סקירת משאבי Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. בתוך ה-hub, צור **פרויקט**.
4. פרוס מודל (למשל, `gpt-5-mini`) מ-**Models + Endpoints** → **Deploy model**.

### שלב 2: קבל את כתובת ה-endpoint והשם של פריסת המודל בפרויקט שלך

מפורטל הפרויקט שלך ב-Microsoft Foundry:

- **כתובת Endpoint של הפרויקט** — עבור לעמוד ה-**Overview** והעתק את כתובת ה-URL של ה-endpoint.

![Project Connection String](../../../translated_images/he/project-endpoint.8cf04c9975bbfbf1.webp)

- **שם פריסת המודל** — עבור ל-**Models + Endpoints**, בחר את המודל שהפרסת, ורשום את **שם הפריסה** (למשל, `gpt-5-mini`).

### שלב 3: התחבר ל-Azure עם `az login`

רוב המחברות מאמתות דרך **כניסה עם Azure CLI** — באמצעות `AzureCliCredential` או `DefaultAzureCredential` (ששתי הסביבות לקוחות תופסות את סשן ה-`az login` שלך) מחבילת `azure-identity` — לכן אינן דורשות מפתחות API. כמה שיעורים ואינטגרציות אופציונליות משתמשות במפתחות API; בדוק את דרישות המקדימות של כל שיעור למידע נוסף על משתני סביבה. דרוש שתהיה מחובר דרך Azure CLI.

1. **התקן את Azure CLI** אם עדיין לא עשית זאת: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **התחבר** על ידי הרצת הפקודה:

    ```bash
    az login
    ```

    או אם אתה בסביבה מרוחקת/Codespace ללא דפדפן:

    ```bash
    az login --use-device-code
    ```

3. **בחר את המנוי שלך** אם תתבקש — בחר את זה שכולל את פרויקט Foundry שלך.

4. **וודא** שהתחברת:

    ```bash
    az account show
    ```

> **למה `az login`?** המחברות מאמתות באמצעות `AzureCliCredential` (או `DefaultAzureCredential`, שגם תופס את כניסת ה-CLI שלך) מחבילת `azure-identity`. פירוש הדבר שסשן Azure CLI שלך מספק את האישורים — לא מפתחות API או סודות בקובץ `.env`. זו [פרקטיקה מומלצת לאבטחה](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### שלב 4: צור את קובץ ה-`.env` שלך

העתק את קובץ הדוגמה:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# פאוארשל
Copy-Item .env.example .env
```

פתח את `.env` ומלא את שני הערכים הבאים:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| משתנה | היכן למצוא אותו |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | פורטל Foundry → הפרויקט שלך → עמוד **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | פורטל Foundry → **Models + Endpoints** → שם המודל שהפרסת |

זהו זה לרוב השיעורים! המחברות יאמתו אוטומטית דרך הסשן שלך ב-`az login`.

### שלב 5: התקן את תלות הפייתון

```bash
pip install -r requirements.txt
```

אנו ממליצים להריץ זאת בתוך סביבת העבודה הווירטואלית שיצרת קודם.

## הגדרה אופציונלית: חיפוש Azure AI (שיעורים 5 ו-16)

מחברות שיעור 5 (Agentic RAG) ושיעור 16 פועלות מתוך הקופסה עם **בסיס ידע בזיכרון** — ללא משאבי Azure נוספים נדרשים. אם אתה רוצה לתמוך בהן באמצעות אינדקס **Azure AI Search** אמיתי, שים לב שמחברת שיעור 16 כרגע משתמשת באימות מבוסס מפתח: היא עוברת מחיפוש בזיכרון ל-Azure AI Search רק כאשר **גם** `AZURE_SEARCH_SERVICE_ENDPOINT` **וגם** `AZURE_SEARCH_API_KEY` מוגדרים, ואחרת נשארת על חיפוש בזיכרון — לכן להריץ אותה עם אינדקס אמיתי עליך להגדיר גם את מפתח המנהל. אימות ללא מפתח עם Microsoft Entra ID (RBAC) הוא הגישה המומלצת לקוד הייצור שלך, בהתאם לזרימת `az login` שמופעלת בכל שאר הקורס.

שלבי ה-RBAC למטה חלים על דוגמאות המדריך ועל הקוד שלך. הם אינם מפעילים אימות ללא מפתח במחברת שיעור 16; שיעור 16 עדיין דורש גם את כתובת ה-endpoint וגם את מפתח המנהל לשימוש ב-Azure AI Search.

1. **הפעל גישת מבוססת תפקידים** בשירות החיפוש שלך:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **הקצה לעצמך את התפקידים הנדרשים** (יצירה/טעינת אינדקסים ושאילתות):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **הוסף את ה-endpoint** לקובץ `.env` שלך:

| משתנה | היכן למצוא אותו |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | פורטל Azure → משאב **Azure AI Search** שלך → **Overview** → כתובת URL |
| `AZURE_SEARCH_API_KEY` | נדרש (עם ה-endpoint) להפעלת Azure AI Search במחברת שיעור 16, שמשתמש באימות מבוסס מפתח. פורטל Azure → **Settings** → **Keys** → מפתח מנהל ראשי |

> **למה ללא מפתח?** מפתחות מנהל נותנים גישה מלאה לכתיבה בשירות החיפוש שלך ועלולים לדלוף דרך קבצי `.env`. עם RBAC, זהות ה-`az login` שלך משמשת במקום זאת — אותו דפוס Entra ID ללא מפתחות שהמחברות בקורס משתמשות בו (באמצעות `AzureCliCredential` / `DefaultAzureCredential`). ראה [חיבור ל-Azure AI Search באמצעות תפקידים](https://learn.microsoft.com/azure/search/search-security-rbac).

ראה את [מדריך ההגדרה של Azure AI Search](./AzureSearch.md) לדוגמאות מלאות ליצירת אינדקס בפייתון וב-.NET.

## הגדרה נוספת לשיעורים שקוראים ל-Azure OpenAI ישירות (שיעורים 6 ו-8)

כמה מחברות בשיעורים 6 ו-8 קוראות ל-**Azure OpenAI** ישירות (באמצעות **Responses API**) במקום לעבור דרך פרויקט Microsoft Foundry. דוגמאות אלו השתמשו בעבר במודלים של GitHub, שהינם מיושנים ואינם תומכים בממשק Responses API. הוסף את המשתנים הבאים לקובץ ה-`.env` שלך:

| משתנה | היכן למצוא אותו |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | פורטל Azure → משאב **Azure OpenAI** שלך → **Keys and Endpoint** → Endpoint (למשל `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | שם המודל שהפרסת (למשל `gpt-5-mini`) שתומך ב-Responses API |
| `AZURE_OPENAI_API_KEY` | אופציונלי — רק אם אתה משתמש באימות מבוסס מפתח במקום `az login` / Entra ID |

> ממשק Responses API משתמש ב-endpoint היציב `/openai/v1/`, לכן אין צורך בגרסת API. התחבר עם `az login` כדי להשתמש באימות Entra ID ללא מפתחות.

## ספק חלופי: MiniMax (תואם OpenAI)

[MiniMax](https://platform.minimaxi.com/) מספק מודלים בהקשר רחב (עד 204K טוקנים) דרך API תואם OpenAI. מאחר ש-`OpenAIChatClient` במסגרת Microsoft Agent Framework עובד עם כל endpoint תואם OpenAI, תוכל להשתמש ב-MiniMax כתחליף לשיעורים המשתמשים ב-`OpenAIChatClient`.

הוסף את המשתנים הבאים לקובץ ה-`.env` שלך:

| משתנה | היכן למצוא אותו |
|----------|-----------------|
| `MINIMAX_API_KEY` | [פלטפורמת MiniMax](https://platform.minimaxi.com/) → מפתחות API |
| `MINIMAX_BASE_URL` | השתמש ב-`https://api.minimax.io/v1` (ערך ברירת מחדל) |
| `MINIMAX_MODEL_ID` | שם המודל לשימוש (למשל, `MiniMax-M3`) |

**דוגמות מודלים**: `MiniMax-M3` (מומלץ), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (תגובות מהירות יותר). שמות הזמינות של המודלים עשויים להשתנות עם הזמן, והגישה למודל מסוים עשויה להיות תלויה בחשבונך.

דוגמאות הקוד שמשתמשות ב-`OpenAIChatClient` (למשל, זרימת העבודה להזמנת מלון בשיעור 14) יזהו אוטומטית וישתמשו בתצורת MiniMax שלך כאשר `MINIMAX_API_KEY` מוגדר.


## ספק חלופי: Novita AI (תואם OpenAI)

[Novita AI](https://novita.ai/llm-api) מציעה API תואם OpenAI עבור LLMs בקוד פתוח וחדשים (DeepSeek, Llama, Qwen, ועוד). מאחר ו-`OpenAIChatClient` במסגרת Microsoft Agent Framework עובד עם כל נקודת קצה תואמת OpenAI, ניתן להשתמש ב-Novita AI כחלופה קלה ל-Azure OpenAI או OpenAI.

הוסף משתנים אלה לקובץ ה-`.env` שלך:

| משתנה | היכן למצוא אותו |
|----------|-----------------|
| `NOVITA_API_KEY` | [לוח הבקרה של Novita AI](https://novita.ai/settings/key-management) → מפתחות API |
| `NOVITA_BASE_URL` | השתמש ב- `https://api.novita.ai/openai/v1` (ערך ברירת מחדל) |
| `NOVITA_MODEL_ID` | שם המודל לשימוש (לדוגמה, `moonshotai/kimi-k3`) |

**דוגמאות למודלים**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI מארחת גם משפחות רבות נוספות של מודלים בקוד פתוח (Llama, Qwen, GLM, ועוד) — בדוק את [ספריית המודלים של Novita AI](https://novita.ai/llm-api) לרשימת המודלים הזמינים הנוכחית ולמזהי המודלים שלהם.

הדוגמאות הנוכחיות אינן משתמשות אוטומטית במשתני `NOVITA_*`. כדי להשתמש ב-Novita AI, העבר את הערכים האלה במפורש בעת הקמת `OpenAIChatClient` בדוגמה שאתה מריץ.

## ספק חלופי: Foundry Local (הרץ מודלים במכשיר)

[Foundry Local](https://foundrylocal.ai) הוא ראנטיים קל משקל שמוריד, מנהל ומשרת מודלי שפה **ממש במחשב האישי שלך** דרך API תואם OpenAI — ללא צורך בענן.

מאחר ו-`OpenAIChatClient` במסגרת Microsoft Agent Framework עובד עם כל נקודת קצה תואמת OpenAI, Foundry Local היא חלופה מקומית שתוכל להחליף את Azure OpenAI.

**1. התקן את Foundry Local**

```bash
# חלונות
winget install Microsoft.FoundryLocal

# מק או אס
brew install foundrylocal
```

**2. הורד והריץ מודל** (פעולה זו גם מפעילה את השירות המקומי):

```bash
foundry model list          # ראה דגמים זמינים
foundry model run phi-4-mini
```

**3. התקן את ערכת הפיתוח של Python** המשמשת לגלות את נקודת הקצה המקומית:

```bash
pip install foundry-local-sdk
```

**4. כוון את Microsoft Agent Framework למודל המקומי שלך:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# מוריד (אם צריך) ומפעיל את המודל מקומית, ואז מגלה את נקודת הקצה/הפורט.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # לדוגמה http://localhost:<port>/v1
    api_key=manager.api_key,        # תמיד "לא נדרש" עבור Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **הערה:** Foundry Local חושף נקודת קצה עבור **Chat Completions** תואמת OpenAI. השתמש בה לפיתוח מקומי ותסריטי עבודה לא מקוונים. עבור סט הפיצ'רים המלא של **Responses API** (שיחות עם מצבי שימור וכו'), השתמש ב-Azure OpenAI או בפרויקט Microsoft Foundry.

## הגדרות נוספות לשיעור 8 (זרימת עבודה של Bing Grounding)

פנקס העבודה של זרימת העבודה המותנית בשיעור 8 משתמש ב-**Bing grounding** דרך Microsoft Foundry. אם אתה מתכנן להריץ את הדוגמה הזו, הוסף משתנה זה לקובץ ה-`.env` שלך:

| משתנה | היכן למצוא אותו |
|----------|-----------------|
| `BING_CONNECTION_ID` | פורטל Microsoft Foundry → הפרויקט שלך → **ניהול** → **משאבים מחוברים** → החיבור שלך ל-Bing → העתק את מזהה החיבור |

## פתרון בעיות

### שגיאות אימות תעודת SSL ב-macOS

אם אתה ב-macOS ומתקל בשגיאה כמו:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

זו בעיה ידועה בפייתון במק, שבה תעודות ה-SSL של המערכת אינן נאמנות אוטומטית. נסה את הפתרונות הבאים לפי הסדר:

**אפשרות 1: הרץ את סקריפט התקנת התעודות של פייתון (מומלץ)**

```bash
# החלף את 3.XX בגירסת פייתון המותקנת שלך (למשל, 3.12 או 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**אפשרות 2: השתמש ב- `connection_verify=False` בפנקס העבודה שלך (רק לפנקסי GitHub Models)**

בפנקס העבודה של שיעור 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), הפתרון כבר מיושם כמושג בהערה. הסר את ההערה מ-`connection_verify=False` כשאתה נתקל בבעיות תעודה:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # השבת אימות SSL אם אתה נתקל בשגיאות בתעודה
)
```

> **⚠️ אזהרה:** כיבוי אימות SSL (`connection_verify=False`) מפחית את האבטחה על ידי דילוג על אימות תעודה. השתמש בכך רק כפתרון זמני בסביבות פיתוח. אל תשתמש בכך בסביבת ייצור.

**אפשרות 3: התקן והשתמש ב-`truststore`**

```bash
pip install truststore
```

לאחר מכן הוסף את הדברים הבאים בתחילת פנקס העבודה או הסקריפט שלך לפני קריאות רשת כלשהן:

```python
import truststore
truststore.inject_into_ssl()
```

## תקוע איפשהו?

אם יש לך בעיות בהרצת ההתקנה הזו, הצטרף אל ה- <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> או <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">צור Issue</a>.

## השיעור הבא

אתה מוכן עכשיו להריץ את הקוד של הקורס הזה. למידה נעימה על עולם סוכני ה-AI! 

[הקדמה לסוכני AI ומקרי שימוש שלהם](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->