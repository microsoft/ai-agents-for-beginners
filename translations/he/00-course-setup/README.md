# הגדרת הקורס

## הקדמה

בשיעור זה תלמדו כיצד להריץ את דוגמאות הקוד של הקורס.

## הצטרף ללומדים אחרים וקבל עזרה

לפני שתתחיל לשכפל את המאגר שלך, הצטרף לערוץ [AI Agents For Beginners Discord](https://aka.ms/ai-agents/discord) לקבלת עזרה בהגדרה, שאלות על הקורס, או להתחבר עם לומדים אחרים.

## שכפל או פורק את המאגר הזה

כדי להתחיל, אנא שכפל או פורק את מאגר GitHub. זה ייצור לך עותק משלך של חומר הקורס כך שתוכל להריץ, לבדוק ולשנות את הקוד!

ניתן לעשות זאת על ידי לחיצה על הקישור ל־<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">פורק את המאגר</a>

כעת אמור להיות לך גרסה משוכפלת משלך של קורס זה בקישור הבא:

![פורק מאגר](../../../translated_images/he/forked-repo.33f27ca1901baa6a.webp)

### שכפול שטחי (מומלץ לסדנאות / Codespaces)

  >המאגר המלא יכול להיות גדול (~3 GB) כאשר מורידים היסטוריה מלאה וכל הקבצים. אם אתה משתתף רק בסדנה או צריך רק כמה תיקיות שיעורים, שכפול שטחי (או שכפול סרוק) יוריד פחות הרבה יותר.

#### שכפול שטחי מהיר — היסטוריה מינימלית, כל הקבצים

החלף את `<your-username>` בהוראות מטה עם כתובת הפורק שלך (או את כתובת המקור אם אתה מעדיף).

לשכפל רק את היסטוריית הוועדות העדכנית (הורדה קטנה):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

לשכפל ענף ספציפי:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### שכפול חלקי (סרוק) — בלובים מינימליים + רק תיקיות נבחרות

משתמש בשכפול חלקי וב־sparse-checkout (דורש Git 2.25+ ומומלץ להשתמש בגרסה מודרנית של Git עם תמיכת שכפול חלקי):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

עבור לתיקיית המאגר:

```bash
cd ai-agents-for-beginners
```

לאחר מכן ציין אילו תיקיות אתה רוצה (לדוגמה למטה מראה שתי תיקיות):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

לאחר שהשכפול ואימות הקבצים, אם אתה צריך רק קבצים ורוצה לפנות מקום (בלי היסטוריית git), מחק את מטא־דאטה המאגר (💀פעולה בלתי הפיכה — תאבד את כל יכולות Git):

```bash
# זש/באש
rm -rf .git
```

```powershell
# פאוארשל
Remove-Item -Recurse -Force .git
```

#### שימוש ב־GitHub Codespaces (מומלץ להימנע מהורדות גדולות מקומיות)

- צור קודספייס חדש למאגר זה דרך ה-[ממשק GitHub](https://github.com/codespaces).  

- במסוף הקודספייס החדש, הרץ אחת מהפקודות לשכפול שטחי/סרוק למעלה כדי להביא רק את תיקיות השיעורים שאתה צריך לסביבת העבודה ב־Codespace.
- אופציונלי: אחרי שכפול בתוך Codespaces, הסר את .git לפנות מקום נוסף (ראה פקודות הסרה למעלה).
- הערה: אם אתה מעדיף לפתוח את המאגר ישירות ב־Codespaces (בלי שכפול נוסף), שים לב ש־Codespaces יבנה את סביבת devcontainer ועדיין עשוי להעמיס יותר ממה שאתה צריך.

#### טיפים

- תמיד החלף את כתובת השכפול עם הפורק שלך אם ברצונך לערוך/להתחייב.
- אם תזדקק מאוחר יותר ליותר היסטוריה או קבצים, תוכל להביא אותם או להתאים את sparse-checkout לכלול תיקיות נוספות.

## הרצת הקוד

קורס זה מציע סדרת מחברות Jupyter שניתן להריץ לקבלת ניסיון מעשי בבניית סוכני AI.

דוגמאות הקוד משתמשות ב־**Microsoft Agent Framework (MAF)** עם `FoundryChatClient`, שמתחבר ל־**Microsoft Foundry Agent Service V2** (ממשק Responses API) דרך **Microsoft Foundry**.

כל מחברות ה־Python מתויגות בקבצים בשם `*-python-agent-framework.ipynb`.

## דרישות

- Python 3.12+
  - **הערה**: אם אין לך Python 3.12 מותקן, וודא להתקין אותו. לאחר מכן צור את סביבת ה־venv שלך באמצעות python3.12 כדי לוודא שהגרסאות המתאימות מותקנות לפי קובץ requirements.txt.
  
    >דוגמה

    צור תיקיית סביבת Python וירטואלית:

    ```bash
    python -m venv venv
    ```

    לאחר מכן הפעל את סביבת ה־venv עבור:

    ```bash
    # זש/באש
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: עבור דוגמאות הקוד שמשתמשות ב־.NET, וודא להתקין [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) או גרסה מאוחרת יותר. לאחר מכן בדוק את גרסת ה־.NET SDK המותקנת:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — דרוש לאימות. התקן מ־[aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — גישה ל־Microsoft Foundry ושירות הסוכנים Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — פרויקט עם מודל מועלה (למשל, `gpt-5-mini`). ראה [שלב 1](#שלב-1-צור-פרויקט-microsoft-foundry) למטה.

כללנו קובץ `requirements.txt` בשורש המאגר שכולל את כל חבילות Python הנדרשות להרצת דוגמאות הקוד.

אפשר להתקין אותן על ידי הרצת הפקודה הבאה במסוף בשורש המאגר:

```bash
pip install -r requirements.txt
```

אנו ממליצים ליצור סביבת Python וירטואלית כדי להימנע מכל התנגשויות ובעיות.

## הגדרת VSCode

ודא שאתה משתמש בגרסת Python הנכונה ב־VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## הגדרת Microsoft Foundry ושירות סוכני Microsoft Foundry

### שלב 1: צור פרויקט Microsoft Foundry

אתה צריך **hub** ו־**project** ב־Microsoft Foundry עם מודל מועלה כדי להריץ את המחברות.

1. עבור ל-[ai.azure.com](https://ai.azure.com) והתחבר עם חשבון Azure שלך.
2. צור **hub** (או השתמש בקיים). עיין: [סקירת משאבי hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. בתוך ה־hub, צור **project**.
4. העלה מודל (למשל, `gpt-5-mini`) מתוך **Models + Endpoints** → **Deploy model**.

### שלב 2: קבל את נקודת הסיום של הפרויקט ושם פריסת המודל

מתוך הפרויקט שלך בפורטל Microsoft Foundry:

- **נקודת סיום של הפרויקט** — עבור לדף **Overview** והעתק את כתובת נקודת הסיום.

![מחרוזת חיבור לפרויקט](../../../translated_images/he/project-endpoint.8cf04c9975bbfbf1.webp)

- **שם פריסת המודל** — עבור אל **Models + Endpoints**, בחר במודל שהועלה, וציין את **Deployment name** (למשל, `gpt-5-mini`).

### שלב 3: התחבר ל־Azure עם `az login`

רוב המחברות מאמתות באמצעות **התחברות דרך Azure CLI** — שימוש ב־`AzureCliCredential` או `DefaultAzureCredential` (ששואבים את סשן `az login`) מחבילת `azure-identity` — לכן אינן דורשות מפתחות API. כמה שיעורים ואינטגרציות אופציונליות דורשות מפתחות API; בדוק בקדם דרישות של כל שיעור לקביעת משתני סביבה נוספים. דרושה התחברות דרך Azure CLI.

1. **התקן את Azure CLI** אם לא התקנת עדיין: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **התחבר** על ידי הרצת:

    ```bash
    az login
    ```

    או אם אתה בסביבת מרחוק/Codespace ללא דפדפן:

    ```bash
    az login --use-device-code
    ```

3. **בחר את המנוי שלך** אם תתבקש — בחר את זה שמכיל את פרויקט Foundry שלך.

4. **וודא** שאתה מחובר:

    ```bash
    az account show
    ```

> **למה `az login`?** המחברות מאמתות באמצעות `AzureCliCredential` (או `DefaultAzureCredential`, שגם שואב את התחברות Azure CLI שלך) מחבילת `azure-identity`. משמעות הדבר שסשן Azure CLI שלך מספק את האישורים — ללא מפתחות API או סודות בקובץ `.env`. זוהי [שיטת אבטחה מומלצת](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### שלב 4: צור את קובץ `.env` שלך

העתק את קובץ הדוגמה:

```bash
# זש/באש
cp .env.example .env
```

```powershell
# פאוורשל
Copy-Item .env.example .env
```

פתח את `.env` ומלא את שני הערכים האלו:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| משתנה | מקום למצוא אותו |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | פורטל Foundry → הפרויקט שלך → דף **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | פורטל Foundry → **Models + Endpoints** → שם המודל שהועלה |

זהו זה עבור רוב השיעורים! המחברות יאמתו אוטומטית דרך סשן `az login`.

### שלב 5: התקן את התלויות של Python

```bash
pip install -r requirements.txt
```

מומלץ להריץ זאת בתוך סביבת הווירטואלית שיצרת קודם.

## הגדרה אופציונלית: חיפוש Azure AI (שיעורים 5 ו־16)

מחברות שיעור 5 (Agentic RAG) ושיעור 16 פועלות מיד עם **מאגר ידע בזיכרון** — אין צורך במשאבים נוספים של Azure. אם תרצה לגבות אותן באינדקס אמיתי של **Azure AI Search**, שים לב שמחברת שיעור 16 משתמשת כרגע באימות מבוסס מפתחות: היא עוברת מחיפוש בזיכרון ל־Azure AI Search רק כשגם `AZURE_SEARCH_SERVICE_ENDPOINT` וגם `AZURE_SEARCH_API_KEY` מוגדרים, ואחרת נשארת בחיפוש בזיכרון — לכן להפעלתה על אינדקס אמיתי יש להגדיר גם מפתח אדמין. אימות ללא מפתחות עם Microsoft Entra ID (RBAC) הוא הגישה המומלצת לקוד הפרודקשן שלך, בהתאם לזרימת ה־`az login` שבקורס.

השלבים ב־RBAC למטה חלים על דוגמאות במדריך ההגדרה ועל הקוד שלך. הם לא מאפשרים אימות ללא מפתחות במחברת שיעור 16 שעדיין דורשת גם נקודת קצה וגם מפתח אדמין לשימוש ב־Azure AI Search.

1. **אפשר גישה מבוססת תפקידים** על שירות החיפוש שלך:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **הענק לעצמך את התפקידים הנדרשים** (יצירה/טעינת אינדקסים ושאילתות):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **הוסף את נקודת הסיום** אל קובץ `.env` שלך:

| משתנה | מקום למצוא אותו |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | פורטל Azure → משאב **Azure AI Search** שלך → **Overview** → כתובת URL |
| `AZURE_SEARCH_API_KEY` | דרוש (עם נקודת הסיום) להפעיל Azure AI Search במחברת שיעור 16, שמשתמשת באימות מבוסס מפתח. פורטל Azure → **Settings** → **Keys** → מפתח אדמין ראשי |

> **למה ללא מפתחות?** מפתחות אדמין מעניקים גישה מלאה לכתיבה לשירות החיפוש שלך ועלולים לדלוף דרך קבצי `.env`. עם RBAC, משמשת זהות ה־`az login` שלך — אותה שיטת אימות ללא מפתחות עם Entra ID שהמחברות משתמשות בה (באמצעות `AzureCliCredential` / `DefaultAzureCredential`). ראה [התחברות ל־Azure AI Search באמצעות תפקידים](https://learn.microsoft.com/azure/search/search-security-rbac).

ראה את [מדריך ההגדרה של Azure AI Search](./AzureSearch.md) לדוגמאות מלאות ליצירת אינדקס ב־Python ו־.NET.

## הגדרה נוספת לשיעורים שקוראים ל־Azure OpenAI ישירות (שיעורים 6 ו־8)

כמה מחברות בשיעורים 6 ו־8 קוראות ל־**Azure OpenAI** ישירות (באמצעות **Responses API**) במקום דרך פרויקט Microsoft Foundry. דוגמאות קוד אלו השתמשו בעבר ב־GitHub Models, שזה מיושן ואינו תומך ב־Responses API. הוסף משתנים אלו לקובץ `.env` שלך:

| משתנה | מקום למצוא אותו |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | פורטל Azure → משאב **Azure OpenAI** שלך → **Keys and Endpoint** → נקודת סיום (למשל, `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | שם המודל שהועלה (למשל, `gpt-5-mini`) שתומך בממשק Responses API |
| `AZURE_OPENAI_API_KEY` | אופציונלי — רק אם אתה משתמש באימות מבוסס מפתח במקום `az login` / Entra ID |

> ממשק Responses API משתמש בנקודת הסיום היציבה `/openai/v1/`, לכן לא דרוש `api-version`. התחבר עם `az login` לשימוש באימות ללא מפתחות עם Entra ID.

## ספק חלופי: MiniMax (תואם ל־OpenAI)

[MiniMax](https://platform.minimaxi.com/) מספקת מודלים עם הקשר גדול (עד 204K תווים) דרך API תואם OpenAI. מאחר ש־`OpenAIChatClient` במסגרת Microsoft Agent Framework פועל עם כל נקודת קצה תואמת OpenAI, ניתן להשתמש ב־MiniMax כספק חלופי לשיעורים שמשתמשים ב־`OpenAIChatClient`.

הוסף משתנים אלו לקובץ `.env` שלך:

| משתנה | מקום למצוא אותו |
|----------|-----------------|
| `MINIMAX_API_KEY` | [פלטפורמת MiniMax](https://platform.minimaxi.com/) → מפתחות API |
| `MINIMAX_BASE_URL` | השתמש ב־`https://api.minimax.io/v1` (הערך ברירת המחדל) |
| `MINIMAX_MODEL_ID` | שם המודל לשימוש (למשל, `MiniMax-M3`) |

**דגמי דוגמה**: `MiniMax-M3` (מומלץ), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (תגובתית מהירה יותר). שמות המודלים והזמינות עלולים להשתנות עם הזמן, והגישה למודל מסוים עשויה להיות מותנית בחשבון שלך.

דוגמאות הקוד שמשתמשות ב־`OpenAIChatClient` (לדוגמה, שיטת העבודה להזמנת מלון בשיעור 14) יזהו וישתמשו אוטומטית עם ההגדרות שלך ל־MiniMax כש־`MINIMAX_API_KEY` מוגדר.


## ספק חלופי: Foundry Local (הרצת מודלים על המכשיר)

[Foundry Local](https://foundrylocal.ai) הוא סביבה קלת משקל שמורידה, מנהלת ומשרתת מודלים של שפה **בכללותם על המחשב שלך** דרך API תואם OpenAI — ללא צורך בענן.

מכיוון ש-`OpenAIChatClient` במסגרת Microsoft Agent Framework עובד עם כל נקודת קצה תואמת OpenAI, Foundry Local היא חלופה מקומית להחלפה ל-Azure OpenAI.

**1. התקן את Foundry Local**

```bash
# ווינדוז
winget install Microsoft.FoundryLocal

# מק או אס
brew install foundrylocal
```

**2. הורד והרץ מודל** (זה גם מפעיל את השירות המקומי):

```bash
foundry model list          # ראה דגמים זמינים
foundry model run phi-4-mini
```

**3. התקן את SDK של Python** המשמש לגילוי נקודת הקצה המקומית:

```bash
pip install foundry-local-sdk
```

**4. הפנה את Microsoft Agent Framework למודל המקומי שלך:**

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

> **הערה:** Foundry Local חושף נקודת קצה **Chat Completions** תואמת OpenAI. השתמש בה לפיתוח מקומי ותסריטים לא מקוונים. לטווח מלא של תכונות **Responses API** (שיחות עם מצב וכו'), השתמש ב-Azure OpenAI או בפרויקט Microsoft Foundry.

## הגדרה נוספת לשיעור 8 (זרימת עבודה של Bing Grounding)

פנקס העבודה של זרימת העבודה המותנית בשיעור 8 משתמש ב**Bing grounding** דרך Microsoft Foundry. אם אתה מתכנן להריץ את הדוגמה הזו, הוסף משתנה זה לקובץ `.env` שלך:

| משתנה | מקום למצוא |
|----------|-----------------|
| `BING_CONNECTION_ID` | פורטל Microsoft Foundry → הפרויקט שלך → **Management** → **Connected resources** → חיבור ה-Bing שלך → העתק את מזהה החיבור |

## פתרון תקלות

### שגיאות אימות תעודת SSL ב-macOS

אם אתה ב-macOS ונתקל בשגיאה כמו:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

זוהי בעיה מוכרת עם Python ב-macOS שבה תעודות ה-SSL של המערכת לא מהימנות אוטומטית. נסה את הפתרונות הבאים לפי הסדר:

**אפשרות 1: הרץ את סקריפט Install Certificates של Python (מומלץ)**

```bash
# החלף את 3.XX בגרסת הפייתון המותקנת שלך (למשל, 3.12 או 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**אפשרות 2: השתמש ב־`connection_verify=False` בפנקס העבודה שלך (רק בפנקסי העבודה של GitHub Models)**

בפנקס העבודה של Lesson 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), יש כבר פתרון מושהה בתור הערה. הסר את ההערה `connection_verify=False` כאשר אתה נתקע בשגיאות תעודה:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # השבת את אימות ה-SSL אם אתה נתקל בשגיאות בתעודה
)
```

> **⚠️ אזהרה:** נטרול אימות SSL (`connection_verify=False`) מפחית אבטחה בכך שמדלג על אימות התעודה. השתמש בזה רק כפתרון זמני בסביבת פיתוח. לעולם אל תשתמש בזה בפרודקשן.

**אפשרות 3: התקן והשתמש ב־`truststore`**

```bash
pip install truststore
```

לאחר מכן הוסף את הבא בראש הפנקס שלך או הסקריפט לפני ביצוע קריאות רשת:

```python
import truststore
truststore.inject_into_ssl()
```

## תקוע במקום כלשהו?

אם יש לך בעיות בהרצת ההגדרה הזו, הצטרף ל-<a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> או <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">צור דיווח</a>.

## השיעור הבא

אתה עכשיו מוכן להריץ את הקוד של הקורס הזה. למידה מהנה על עולם סוכני ה-AI!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->