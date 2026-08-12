# הגדרת הקורס

## מבוא

בשיעור זה נלמד כיצד להריץ את דוגמאות הקוד מהקורס הזה.

## הצטרף ללומדים אחרים וקבל עזרה

לפני שתתחיל לשכפל את המאגר שלך, הצטרף ל-[ערוץ דיסקורד של AI Agents למתחילים](https://aka.ms/ai-agents/discord) כדי לקבל עזרה בהתקנה, שאלות על הקורס, או להתחבר ללומדים אחרים.

## שכפל או פצל את המאגר הזה

כדי להתחיל, אנא שכפל או פצל את מאגר GitHub. זה ייצור לך עותק משלך של חומרי הקורס כדי שתוכל להריץ, לבדוק ולשנות את הקוד!

ניתן לעשות זאת על ידי לחיצה על הקישור ל־ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">פיצול המאגר</a>

עכשיו יש לך עותק מפוצל משלך של הקורס בקישור הבא:

![Forked Repo](../../../translated_images/he/forked-repo.33f27ca1901baa6a.webp)

### שכפול שטחי (מומלץ לסדנאות / Codespaces)

  >מאגר מלא יכול להיות גדול (~3 GB) כאשר מורידים את ההיסטוריה המלאה ואת כל הקבצים. אם אתה משתתף רק בסדנה או צריך רק כמה תיקיות שיטבחו, שכפול שטחי (או שכפול דליל) מתעלם מהרוב של ההורדה על ידי קיצור ההיסטוריה ו/או דילוג על בלובים.

#### שכפול שטחי מהיר — היסטוריה מינימלית, כל הקבצים

החלף את `<your-username>` בפקודות למטה עם כתובת ה-URL של הפיצול שלך (או כתובת ה-URL העליונה אם אתה מעדיף).

לשכפל רק את ההיסטוריה של הקומיט האחרון (הורדה קטנה):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

לשכפל ענף ספציפי:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### שכפול חלקי (דליל) — בלובים מינימליים + רק תיקיות נבחרות

משתמש בשכפול חלקי ו-sparse-checkout (דורש Git 2.25+ ומומלץ Git מודרני עם תמיכה בשכפול חלקי):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

עבור לתיקיית המאגר:

```bash|powershell
cd ai-agents-for-beginners
```

לאחר מכן ציין אילו תיקיות אתה רוצה (דוגמה למטה מציגה שתי תיקיות):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

לאחר השכפול ואימות הקבצים, אם אתה צריך רק את הקבצים ורוצה לפנות מקום (בלי היסטוריית git), אנא מחק את מטא-נתוני המאגר (💀בלתי הפיך — תאבד את כל פונקציונליות Git: לא יהיו קומיטים, משיכות, דחיפות או גישה להיסטוריה).

```bash
# זש/באש
rm -rf .git
```

```powershell
# פאוארשל
Remove-Item -Recurse -Force .git
```

#### שימוש ב-GitHub Codespaces (מומלץ כדי להימנע מהורדות גדולות מקומית)

- צור Codespace חדש עבור המאגר הזה דרך [ממשק GitHub](https://github.com/codespaces).  

- במסוף של ה-Codespace החדש, הרץ אחת מפקודות השכפול השטחי/הדליל למעלה כדי להביא רק את תיקיות השיעורים שאתה צריך לסביבת Codespace.
- אופציונלי: לאחר השכפול בתוך Codespaces, הסר את .git כדי לשחרר מקום נוסף (ראה פקודות ההסרה למעלה).
- הערה: אם אתה מעדיף לפתוח את המאגר ישירות ב-Codespaces (בלי שכפול נוסף), שים לב ש-Codespaces יבנה את סביבת devcontainer ועדיין עשוי לספק יותר ממה שאתה צריך. שכפול שטחי בתוך Codespace חדש נותן לך יותר שליטה על שימוש בדיסק.

#### טיפים

- תמיד החלף את כתובת השכפול לכתובת הפיצול שלך אם ברצונך לערוך/לקומיט.
- אם תצטרך מאוחר יותר היסטוריה או קבצים נוספים, תוכל לאחזר אותם או להתאים את sparse-checkout לכלול תיקיות נוספות.

## הרצת הקוד

הקורס מציע סדרת מחברות Jupyter שתוכל להריץ כדי לקבל ניסיון מעשי בבניית סוכני AI.

דוגמאות הקוד משתמשות ב**Microsoft Agent Framework (MAF)** עם `FoundryChatClient`, שמתחבר ל-**Microsoft Foundry Agent Service V2** (ממשק Responses API) דרך **Microsoft Foundry**.

כל מחברות הפייתון מסומנות כ־`*-python-agent-framework.ipynb`.

## דרישות

- Python 3.12+
  - **הערה**: אם אין לך פייתון 3.12 מותקן, ודא שאתה מתקין אותו. לאחר מכן צור את סביבת ה-venv שלך באמצעות python3.12 כדי להבטיח שהגרסאות הנכונות מותקנות מקובץ requirements.txt.
  
    >דוגמה

    צור ספריית Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    לאחר מכן הפעל את סביבת ה-venv ל:

    ```bash
    # זש/בש
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: לקוד הדוגמה המשתמש ב-.NET, ודא שהתקנת [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) או גרסה מאוחרת יותר. לאחר מכן, בדוק את גרסת ה-SDK של .NET שהתקנת:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — דרוש לאימות. התקן מ-[aka.ms/installazurecli](https://aka.ms/installazurecli).
- **מנוי Azure** — לגישה ל-Microsoft Foundry ול-Microsoft Foundry Agent Service.
- **פרויקט Microsoft Foundry** — פרויקט עם מודל מתפרש (למשל `gpt-5-mini`). ראה [שלב 1](#שלב-1-צור-פרויקט-ב-microsoft-foundry) למטה.

כללנו קובץ `requirements.txt` בשורש המאגר שמכיל את כל חבילות הפייתון הנדרשות כדי להריץ את דוגמאות הקוד.

אתה יכול להתקין אותם על ידי הרצת הפקודה הבאה במסוף שלך בשורש המאגר:

```bash|powershell
pip install -r requirements.txt
```

אנו ממליצים ליצור סביבת פייתון וירטואלית כדי למנוע התנגשויות ובעיות.

## הגדרת VSCode

ודא שאתה משתמש בגרסת הפייתון הנכונה ב-VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## הגדרת Microsoft Foundry ו-Microsoft Foundry Agent Service

### שלב 1: צור פרויקט ב-Microsoft Foundry

אתה צריך **hub** ו**פרויקט** ב-Microsoft Foundry עם מודל מתפרש כדי להריץ את המחברות.

1. עבור ל-[ai.azure.com](https://ai.azure.com) והתחבר עם חשבון Azure שלך.
2. צור **hub** (או השתמש ב-קיים). ראה: [סקירת משאבי Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. בתוך ה-hub, צור **פרויקט**.
4. פרוש מודל (למשל `gpt-5-mini`) מתוך **Models + Endpoints** → **Deploy model**.

### שלב 2: קבל את נקודת הקצה של הפרויקט ושם פריסת המודל שלך

מתוך הפרויקט שלך בפורטל Microsoft Foundry:

- **נקודת הקצה של הפרויקט** — עבור לדף **סקירה כללית** והעתק את כתובת ה-URL של נקודת הקצה.

![Project Connection String](../../../translated_images/he/project-endpoint.8cf04c9975bbfbf1.webp)

- **שם פריסת המודל** — עבור ל-**Models + Endpoints**, בחר במודל המתפרש שלך, ורשום את **שם הפריסה** (למשל `gpt-5-mini`).

### שלב 3: היכנס ל-Azure עם `az login`

כל המחברות משתמשות ב-**`AzureCliCredential`** לאימות — ללא מפתחות API לטפל בהם. זה דורש שאתה תחובר דרך Azure CLI.

1. **התקן את Azure CLI** אם עדיין לא עשית זאת: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **התחבר** על ידי הרצת:

    ```bash|powershell
    az login
    ```

    או אם אתה בסביבת remote/Codespace ללא דפדפן:

    ```bash|powershell
    az login --use-device-code
    ```

3. **בחר את המנוי שלך** אם מתבקש — בחר את זה שמכיל את פרויקט Foundry שלך.

4. **אמת** שאתה מחובר:

    ```bash|powershell
    az account show
    ```

> **למה `az login`?** המחברות מאמתות באמצעות `AzureCliCredential` מחבילת `azure-identity`. המשמעות היא ש-session ה-Azure CLI שלך מספק את האישורים — ללא מפתחות API או סודות בקובץ `.env`. זוהי [שיטת עבודה בטיחותית מומלצת](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### שלב 4: צור את קובץ `.env` שלך

העתיק את קובץ הדוגמה:

```bash
# זש/בש
cp .env.example .env
```

```powershell
# פאוורשל
Copy-Item .env.example .env
```

פתח את `.env` ומלא את שני הערכים האלה:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| משתנה | היכן למצוא |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | פורטל Foundry → הפרויקט שלך → דף **סקירה כללית** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | פורטל Foundry → **Models + Endpoints** → שם המודל המתפרש שלך |

זה כל מה שצריך עבור רוב השיעורים! המחברות יאמתו אוטומטית דרך session ה-`az login` שלך.

### שלב 5: התקן את התלויות של פייתון

```bash|powershell
pip install -r requirements.txt
```

אנו ממליצים להריץ זאת בתוך סביבת הוירטואלית שיצרת קודם לכן.

## הגדרות נוספות לשיעור 5 (Agentic RAG)

שיעור 5 משתמש ב**Azure AI Search** בשביל יצירת תוכן המוגבר על ידי חיפוש. אם אתה מתכוון להריץ את השיעור הזה, הוסף את המשתנים האלה לקובץ ה-`.env` שלך:

| משתנה | היכן למצוא |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | פורטל Azure → משאב **Azure AI Search** שלך → **סקירה כללית** → כתובת URL |
| `AZURE_SEARCH_API_KEY` | פורטל Azure → משאב **Azure AI Search** שלך → **הגדרות** → **מפתחות** → מפתח מנהל ראשי |

## הגדרות נוספות לשיעורים שקוראים ל-Azure OpenAI ישירות (שיעורים 6 ו-8)

כמה מחברות בשיעורים 6 ו-8 קוראות ל**Azure OpenAI** ישירות (באמצעות **Responses API**) במקום לעבור דרך פרויקט Microsoft Foundry. דוגמאות אלה השתמשו בעבר ב-GitHub Models, שכבר אינו פעיל (ייפסק ביולי 2026) ואינו תומך ב-Responses API. אם אתה מתכנן להריץ דוגמאות אלו, הוסף את המשתנים האלה לקובץ ה-`.env` שלך:

| משתנה | היכן למצוא |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | פורטל Azure → משאב **Azure OpenAI** שלך → **מפתחות ונקודת קצה** → נקודת קצה (למשל `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | שם המודל המתפרש שלך (למשל `gpt-5-mini`) שתומך ב-Responses API |
| `AZURE_OPENAI_API_KEY` | אופציונלי — רק אם אתה משתמש באימות מבוסס מפתח במקום `az login` / Entra ID |

> Responses API משתמש בנקודת הקצה היציבה `/openai/v1/`, לכן אין צורך בפרמטר `api-version`. התחבר עם `az login` כדי להשתמש באימות Entra ID ללא מפתח.

## ספק חלופי: MiniMax (תואם OpenAI)

[MiniMax](https://platform.minimaxi.com/) מספק מודלים עם הקשר גדול (עד 204K תווים) דרך API תואם OpenAI. מאחר ש-`OpenAIChatClient` במסגרת Microsoft Agent Framework פועל עם כל נקודת קצה תואמת OpenAI, ניתן להשתמש ב-MiniMax כחלופה עקיפה ל-Azure OpenAI או OpenAI.

הוסף את המשתנים האלה לקובץ ה-`.env` שלך:

| משתנה | היכן למצוא |
|----------|-----------------|
| `MINIMAX_API_KEY` | [פלטפורמת MiniMax](https://platform.minimaxi.com/) → מפתחות API |
| `MINIMAX_BASE_URL` | השתמש ב- `https://api.minimax.io/v1` (ערך ברירת מחדל) |
| `MINIMAX_MODEL_ID` | שם המודל לשימוש (למשל, `MiniMax-M3`) |

**דגמי דוגמה**: `MiniMax-M3` (מומלץ), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (תגובות מהירות יותר). שמות הדגמים וזמינותם עשויים להשתנות עם הזמן, והגישה למודל מסוים עשויה להיות תלויה בחשבון או באיזור שלך — בדוק את [פלטפורמת MiniMax](https://platform.minimaxi.com/) לרשימה העדכנית. אם `MiniMax-M3` אינו זמין לחשבונך, הגדר את `MINIMAX_MODEL_ID` למודל שיש לך גישה אליו (למשל `MiniMax-M2.7`).

דוגמאות הקוד שמשתמשות ב־`OpenAIChatClient` (למשל, תהליך הזמנת מלון בשיעור 14) יזהו ויישמו אוטומטית את תצורת MiniMax שלך כש־`MINIMAX_API_KEY` מוגדר.

## ספק חלופי: Foundry Local (הרץ מודלים על המכשיר)

[Foundry Local](https://foundrylocal.ai) הוא סביבת ריצה קלת משקל שמורידה, מנהלת ומספקת מודלים לשפה **במכונה שלך בלבד** דרך API תואם OpenAI — ללא ענן, ללא מנוי Azure, וללא מפתחות API. זו אפשרות מעולה לפיתוח לא מקוון, להתנסויות ללא עלות ענן, או לשמירת נתונים על המכשיר.

מאחר ש-`OpenAIChatClient` במסגרת Microsoft Agent Framework פועל עם כל נקודת קצה תואמת OpenAI, Foundry Local היא חלופה מקומית ישירה לא Azure OpenAI.

**1. התקן את Foundry Local**

```bash
# חלונות
winget install Microsoft.FoundryLocal

# מקאו
brew install foundrylocal
```

**2. הורד והפעל מודל** (זה גם מפעיל את השירות המקומי):

```bash
foundry model list          # ראה דגמים זמינים
foundry model run phi-4-mini
```

**3. התקן את SDK של פייתון** המשמש לגילוי נקודת הקצה המקומית:

```bash
pip install foundry-local-sdk
```

**4. הצבע את Microsoft Agent Framework למודל המקומי שלך:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# מוריד (אם נדרש) ומפעיל את המודל מקומית, ואז מוצא את נקודת הקצה/הפורט.
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

> **הערה:** Foundry Local חושף נקודת קצה תואמת OpenAI עבור **שיחות השלמה**. השתמש בו לפיתוח מקומי ותסריטים לא מקוונים. עבור הסט המלא של תכונות **Responses API** (שיחות ממושכות, התנסחות עמוקה עם כלים, ופיתוח בסגנון סוכן), הפנה ל-**Azure OpenAI** או לפרויקט **Microsoft Foundry** כפי שמוצג בשיעורים. ראה את [התיעוד של Foundry Local](https://foundrylocal.ai) עבור קטלוג המודלים העדכני ותמיכה בפלטפורמה.

## הגדרות נוספות לשיעור 8 (תהליך Bing Grounding)


פנקס העבודה של תהליך הבקרה בשיעור 8 משתמש ב**בסיס Bing** דרך Microsoft Foundry. אם אתם מתכננים להריץ את הדוגמה הזו, הוסיפו משתנה זה לקובץ ה-`.env` שלכם:

| משתנה | איפה למצוא אותו |
|----------|-----------------|
| `BING_CONNECTION_ID` | פורטל Microsoft Foundry → הפרויקט שלכם → **ניהול** → **משאבים מחוברים** → חיבור Bing שלכם → העתקת מזהה החיבור |

## פתרון תקלות

### שגיאות אימות תעודת SSL במק־אוס

אם אתם במק־אוס ונתקלים בשגיאה כמו:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

זו בעיה מוכרת ב-Python במק־אוס שבה תעודות ה-SSL של המערכת אינן מהימנות אוטומטית. נסו את הפתרונות הבאים לפי הסדר:

**אפשרות 1: הרצת סקריפט התקנת התעודות של Python (מומלץ)**

```bash
# החלף 3.XX בגרסת פייתון המותקנת שלך (למשל, 3.12 או 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**אפשרות 2: השתמשו ב-`connection_verify=False` בפנקס העבודה שלכם (רק לפנקסי עבודה של GitHub Models)**

בפנקס העבודה של שיעור 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), יש כבר פתרון עקיפין שמומלץ. הסירו את ההערה מ-`connection_verify=False` כאשר יוצרים את הלקוח:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # ביטול אימות SSL אם מופיעים שגיאות בתעודה
)
```

> **⚠️ אזהרה:** השבתת אימות SSL (`connection_verify=False`) מפחיתה את האבטחה על ידי דילוג על אימות התעודה. השתמשו בזה רק כפתרון זמני בסביבות פיתוח, לעולם לא בייצור.

**אפשרות 3: התקנת ושימוש ב-`truststore`**

```bash
pip install truststore
```

לאחר מכן הוסיפו את הקוד הבא בראש פנקס העבודה או הסקריפט שלכם לפני כל קריאות רשת:

```python
import truststore
truststore.inject_into_ssl()
```

## תקועים איפשהו?

אם יש לכם בעיות בהרצת ההתקנה הזו, הצטרפו לקהילה שלנו ב- <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> או <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">צרו מדווחת בעיה</a>.

## השיעור הבא

כעת אתם מוכנים להריץ את הקוד של הקורס הזה. למידה מהנה על עולם הסוכנים של AI! 

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->