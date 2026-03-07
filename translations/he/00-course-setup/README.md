# התקנת הקורס

## הקדמה

השיעור הזה ילמד כיצד להריץ את דוגמאות הקוד של הקורס.

## הצטרפו ללומדים אחרים וקבלו עזרה

לפני שתתחילו לשכפל את המאגר שלכם, הצטרפו אל [ערוץ הדיסקורד AI Agents For Beginners](https://aka.ms/ai-agents/discord) כדי לקבל עזרה בהתקנה, לשאול שאלות לגבי הקורס, או להתחבר עם לומדים אחרים.

## שכפלו או שמרו על המאגר הזה

כדי להתחיל, אנא שכפלו או שמרו עותק של מאגר ה-GitHub. כך תוכלו לקבל גרסה משלכם של חומרי הקורס ולהריץ, לבדוק ולשנות את הקוד!

ניתן לעשות זאת ע"י לחיצה על הקישור ל- <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">שמירת עותק של המאגר</a>

כעת יש לכם עותק שמור משלכם של הקורס בקישור הבא:

![Forked Repo](../../../translated_images/he/forked-repo.33f27ca1901baa6a.webp)

### שכפול רדוד (מומלץ לסדנה / Codespaces)

  >מאגר מלא עלול להיות גדול (~3 ג'יגה-בייט) בעת הורדת ההיסטוריה המלאה וכל הקבצים. אם אתם משתתפים רק בסדנה או צריכים רק כמה תיקיות של שיעורים, שכפול רדוד (או שכפול חסר) ימנע את רוב ההורדה ע"י קיצור ההיסטוריה ו/או דילוג על blobs.

#### שכפול רדוד מהיר — היסטוריה מינימלית, כל הקבצים

החליפו את `<your-username>` בפקודות למטה עם כתובת ה-fork שלכם (או את כתובת ה-upstream אם אתם מעדיפים).

שכפול רק היסטוריית ההתחייבויות העדכנית ביותר (הורדה קטנה):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

לשכפל סניף ספציפי:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### שכפול חלקי (חסר) — blobs מינימליים + רק תיקיות נבחרות

זה משתמש בשכפול חלקי וב-sparse-checkout (דורש Git 2.25+ ומומלץ להשתמש ב-Git מודרני עם תמיכה בשכפול חלקי):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

נווטו לתיקיית המאגר:

```bash|powershell
cd ai-agents-for-beginners
```

ואז ציינו אילו תיקיות אתם רוצים (בדוגמה למטה שתי תיקיות):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

לאחר השכפול ובדיקת הקבצים, אם אתם צריכים רק את הקבצים ורוצים לפנות מקום (ללא היסטוריית git), אנא מחקו את המידע המטא של המאגר (💀בלתי הפיך — תאבדו את כל פונקציות Git: אין התחייבויות, משיכות, דחיפות או גישה להיסטוריה).

```bash
# זש/בש
rm -rf .git
```

```powershell
# פאוורשֶל
Remove-Item -Recurse -Force .git
```

#### שימוש ב-GitHub Codespaces (מומלץ כדי להימנע מהורדות כבדות מקומיות)

- צרו Codespace חדש עבור מאגר זה דרך [ממשק GitHub](https://github.com/codespaces).  

- בטרמינל של ה-Codespace שנוצר הריצו אחת מהפקודות לשכפול רדוד/חסר שלמעלה כדי להביא רק את תיקיות השיעורים שאתם צריכים לחלל העבודה של Codespace.
- אופציונלי: לאחר השכפול בתוך Codespaces, מחקו את הקבצים .git כדי לפנות מקום נוסף (ראו פקודות המחיקה למעלה).
- שימו לב: אם אתם מעדיפים לפתוח את המאגר ישירות ב-Codespaces (בלי שכפול נוסף), קחו בחשבון ש-Codespaces יבנה את סביבת devcontainer ואולי יספק יותר ממה שאתם צריכים. שכפול רדוד בתוך Codespace חדש נותן לכם יותר שליטה על שימוש בדיסק.

#### טיפים

- תמיד החליפו את כתובת השכפול לכתובת ה-fork שלכם אם אתם רוצים לערוך או להתחייב.
- אם תצטרכו בהמשך היסטוריה או קבצים נוספים, תוכלו להביא אותם או להתאים את sparse-checkout לכלול תיקיות נוספות.

## הרצת הקוד

הקורס מציע סדרת Jupyter Notebooks שניתן להריץ כדי לקבל ניסיון מעשי בבניית סוכני AI.

דוגמאות הקוד משתמשות ב-**Microsoft Agent Framework (MAF)** עם `AzureAIProjectAgentProvider`, שמתחבר ל-**Azure AI Agent Service V2** (ממשק Responses API) דרך **Microsoft Foundry**.

כל מחברות הפייתון מסומנות כ-`*-python-agent-framework.ipynb`.

## דרישות

- Python 3.12+
  - **הערה**: אם אין ברשותכם Python3.12 מותקן, וודאו להתקין אותו. לאחר מכן צרו סביבה וירטואלית (venv) באמצעות python3.12 כדי להבטיח טעמים נכונים מותקנים מקובץ requirements.txt.
  
    >דוגמה

    יצירת תיקיית venv לפייתון:

    ```bash|powershell
    python -m venv venv
    ```

    לאחר מכן הפעלת סביבה וירטואלית עבור:

    ```bash
    # זש/באש
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: לדוגמאות הקוד שמשתמשות ב-.NET, ודאו שתקינו את [SDK של .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) או גרסה מאוחרת יותר. לאחר מכן בדקו את גרסת ה-SDK שלכם:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — נדרש לאימות. התקינו מ-[aka.ms/installazurecli](https://aka.ms/installazurecli).
- **מנוי Azure** — לגישה ל-Microsoft Foundry ושירות Azure AI Agent.
- **פרויקט Microsoft Foundry** — פרויקט עם דגם פרוס (למשל, `gpt-4o`). ראו [שלב 1](../../../00-course-setup) למטה.

כלול קובץ `requirements.txt` בשורש המאגר שמכיל את כל הספריות הנדרשות של פייתון כדי להריץ את דוגמאות הקוד.

ניתן להתקין אותם ע"י הרצת הפקודה הבאה בטרמינל שלכם בשורש המאגר:

```bash|powershell
pip install -r requirements.txt
```

אנו ממליצים ליצור סביבה וירטואלית בפייתון כדי למנוע קונפליקטים ובעיות.

## הגדרת VSCode

ודאו שאתם משתמשים בגרסת הפייתון הנכונה ב-VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## התקנת Microsoft Foundry ושירות Azure AI Agent

### שלב 1: יצירת פרויקט Microsoft Foundry

אתם צריכים **hub** ו-**project** ב-Azure AI Foundry עם דגם פרוס כדי להריץ את המחברות.

1. עברו ל-[ai.azure.com](https://ai.azure.com) והתחברו עם חשבון Azure שלכם.
2. צרו **hub** (או השתמשו בקיים). ראו: [סקירת משאבי Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. בתוך ה-hub, צרו **project**.
4. פרסמו דגם (למשל, `gpt-4o`) מ-**Models + Endpoints** → **Deploy model**.

### שלב 2: שליפת ה-Endpoint ושם פריסת הדגם של הפרויקט

מהפרויקט שלכם בפורטל Microsoft Foundry:

- **Project Endpoint** — עברו לדף **Overview** והעתיקו את כתובת ה-URL של ה-endpoint.

![Project Connection String](../../../translated_images/he/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — עברו ל-**Models + Endpoints**, בחרו בדגם הפרוס שלכם, ורשמו את שם הפריסה (למשל, `gpt-4o`).

### שלב 3: התחברו ל-Azure עם `az login`

כל המחברות משתמשות ב-**`AzureCliCredential`** לאימות — אין צורך במפתחות API. זה דורש שתהיו מחוברים דרך Azure CLI.

1. **התקינו את Azure CLI** אם עדיין לא עשיתם זאת: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **התחברו** באמצעות הרצת:

    ```bash|powershell
    az login
    ```

    או, אם אתם בסביבה מרוחקת/Codespace ללא דפדפן:

    ```bash|powershell
    az login --use-device-code
    ```

3. **בחרו את המנוי** במקרה שמבקשים — בחרו זה שמכיל את פרויקט Foundry שלכם.

4. **וודאו** שאתם מחוברים:

    ```bash|powershell
    az account show
    ```

> **למה `az login`?** המחברות מאמתות באמצעות `AzureCliCredential` מחבילת `azure-identity`. משמעות הדבר היא שהסשן שלכם ב-Azure CLI מספק את האישורים — ללא מפתחות API או סודות בקובץ `.env`. זהו [נהוג אבטחה מומלץ](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### שלב 4: צרו את הקובץ `.env` שלכם

העתיקו את קובץ הדוגמה:

```bash
# זש/bash
cp .env.example .env
```

```powershell
# פאוורשל
Copy-Item .env.example .env
```

פתחו את `.env` ומלאו את שני הערכים הבאים:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| משתנה | היכן למצוא |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | פורטל Foundry → הפרויקט שלכם → דף **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | פורטל Foundry → **Models + Endpoints** → שם הדגם שפורסמתם |

זהו! עבור רוב השיעורים המחברות יאמתו אוטומטית דרך סשן ה-`az login` שלכם.

### שלב 5: התקנת הספריות בפייתון

```bash|powershell
pip install -r requirements.txt
```

מומלץ להריץ זאת בתוך סביבה וירטואלית שיצרתם קודם לכן.

## התקנות נוספות לשיעור 5 (Agentic RAG)

השיעור 5 משתמש ב-**Azure AI Search** ליצירת תוכן משופר ע"י אחזור. אם אתם מתכננים להריץ את השיעור הזה, הוסיפו את המשתנים האלה לקובץ `.env` שלכם:

| משתנה | היכן למצוא |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | פורטל Azure → משאב **Azure AI Search** שלכם → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | פורטל Azure → משאב **Azure AI Search** שלכם → **Settings** → **Keys** → מפתח מנהל ראשי |

## התקנות נוספות לשיעור 6 ושיעור 8 (GitHub Models)

כמה מחברות בשיעורים 6 ו-8 משתמשות ב-**GitHub Models** במקום Azure AI Foundry. אם אתם מתכננים להריץ דוגמאות אלה, הוסיפו את המשתנים האלו ל-`.env` שלכם:

| משתנה | היכן למצוא |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | השתמשו ב-`https://models.inference.ai.azure.com` (הערך ברירת מחדל) |
| `GITHUB_MODEL_ID` | שם הדגם לשימוש (למשל `gpt-4o-mini`) |

## התקנות נוספות לשיעור 8 (זרימת עבודה Bing Grounding)

מחברת זרימת העבודה המותנית בשיעור 8 משתמשת ב-**Bing grounding** דרך Azure AI Foundry. אם אתם מתכננים להריץ דוגמא זו, הוסיפו משתנה זה ל-`.env` שלכם:

| משתנה | היכן למצוא |
|----------|-----------------|
| `BING_CONNECTION_ID` | פורטל Azure AI Foundry → הפרויקט שלכם → **Management** → **Connected resources** → החיבור שלכם ל-Bing → העתיקו את מזהה החיבור |

## פתרון בעיות

### שגיאות אימות תעודת SSL במערכת macOS

אם אתם במערכת macOS ומקבלים שגיאה כמו:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

זו בעיה ידועה בפייתון על macOS שבה תעודות ה-SSL של המערכת אינן מהימנות אוטומטית. נסו את הפתרונות הבאים בסדר:

**אפשרות 1: הריצו את סקריפט התקנת התעודות של פייתון (מומלץ)**

```bash
# החלף את 3.XX בגרסת הפייתון המותקנת שלך (למשל, 3.12 או 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**אפשרות 2: השתמשו ב-`connection_verify=False` במחברת שלכם (רק למחברות GitHub Models)**

במחברת של שיעור 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), יש כבר פיתרון מוסבר עם הערה. הסירו את ההערה מ-`connection_verify=False` כשהלקוח נוצר:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # ביטול אימות SSL אם אתה נתקל בשגיאות בתעודה
)
```

> **⚠️ אזהרה:** השבתת אימות SSL (`connection_verify=False`) מפחיתה את האבטחה בכך שמדלגת על אימות התעודה. השתמשו בזה רק כפתרון זמני בסביבות פיתוח, לעולם לא בייצור.

**אפשרות 3: התקינו והשתמשו ב-`truststore`**

```bash
pip install truststore
```

ואז הוסיפו את השורה הבאה בתחילת המחברת או הסקריפט לפני כל קריאות רשת:

```python
import truststore
truststore.inject_into_ssl()
```

## תקועים איפשהו?

אם יש לכם בעיות בהרצת ההתקנה הזו, הצטרפו אלינו ב-<a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> או <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">צרו בעיה חדשה</a>.

## השיעור הבא

כעת אתם מוכנים להריץ את הקוד של הקורס הזה. לימוד מוצלח על עולם סוכני ה-AI!

[מבוא לסוכני AI ושימושי סוכנים](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). אף שאנו שואפים לדייק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור מהווה את המקור המוסמך. עבור מידע קריטי מומלץ להיעזר בתרגום מקצועי של אדם. אנו לא נישא באחריות לכל אי-הבנה או פרשנות שגויה הנובעת מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->