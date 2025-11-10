<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86273689a010b5efecaf7fa23104e0fb",
  "translation_date": "2025-11-07T08:41:38+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "he"
}
-->
# הגדרת הקורס

## מבוא

בשיעור זה נלמד כיצד להפעיל את דוגמאות הקוד של הקורס.

## הצטרפות ללומדים אחרים וקבלת עזרה

לפני שתתחילו לשכפל את המאגר שלכם, הצטרפו לערוץ [AI Agents For Beginners ב-Discord](https://aka.ms/ai-agents/discord) כדי לקבל עזרה בהגדרות, לשאול שאלות על הקורס או להתחבר ללומדים אחרים.

## שכפול או יצירת Fork למאגר זה

כדי להתחיל, אנא שכפלו או צרו Fork למאגר ה-GitHub. זה ייצור גרסה משלכם של חומרי הקורס כך שתוכלו להפעיל, לבדוק ולשנות את הקוד!

ניתן לעשות זאת על ידי לחיצה על הקישור ל-<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">יצירת Fork למאגר</a>.

כעת אמורה להיות לכם גרסת Fork משלכם של הקורס בקישור הבא:

![מאגר משוכפל](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.he.png)

### שכפול רדוד (מומלץ לסדנאות / Codespaces)

  >המאגר המלא יכול להיות גדול (~3 GB) כאשר מורידים את כל ההיסטוריה וכל הקבצים. אם אתם רק משתתפים בסדנה או זקוקים רק לכמה תיקיות שיעור, שכפול רדוד (או שכפול חלקי) מונע את רוב ההורדה הזו על ידי קיצור ההיסטוריה ו/או דילוג על קבצים.

#### שכפול רדוד מהיר — היסטוריה מינימלית, כל הקבצים

החליפו `<your-username>` בפקודות למטה עם כתובת ה-URL של ה-Fork שלכם (או כתובת ה-URL המקורית אם אתם מעדיפים).

כדי לשכפל רק את ההיסטוריה של ההתחייבות האחרונה (הורדה קטנה):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

כדי לשכפל ענף מסוים:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### שכפול חלקי (Sparse) — קבצים מינימליים + רק תיקיות נבחרות

זה משתמש בשכפול חלקי וב-Sparse-checkout (דורש Git 2.25+ ומומלץ להשתמש בגרסת Git מודרנית עם תמיכה בשכפול חלקי):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

עברו לתיקיית המאגר:

```bash|powershell
cd ai-agents-for-beginners
```

לאחר מכן ציינו אילו תיקיות אתם רוצים (הדוגמה למטה מראה שתי תיקיות):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

לאחר השכפול ואימות הקבצים, אם אתם זקוקים רק לקבצים ורוצים לפנות מקום (ללא היסטוריית Git), אנא מחקו את המטא-נתונים של המאגר (💀בלתי הפיך — תאבדו את כל הפונקציונליות של Git: אין התחייבויות, משיכות, דחיפות או גישה להיסטוריה).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### שימוש ב-GitHub Codespaces (מומלץ להימנע מהורדות גדולות מקומיות)

- צרו Codespace חדש למאגר זה דרך [ממשק המשתמש של GitHub](https://github.com/codespaces).  

- בטרמינל של ה-Codespace החדש שנוצר, הריצו אחת מפקודות השכפול הרדוד/החלקי לעיל כדי להביא רק את תיקיות השיעור שאתם צריכים לסביבת העבודה של ה-Codespace.
- אופציונלי: לאחר השכפול בתוך Codespaces, הסירו את .git כדי לשחרר מקום נוסף (ראו פקודות הסרה לעיל).
- הערה: אם אתם מעדיפים לפתוח את המאגר ישירות ב-Codespaces (ללא שכפול נוסף), שימו לב ש-Codespaces יבנה את סביבת ה-devcontainer וייתכן שעדיין יספק יותר ממה שאתם צריכים. שכפול עותק רדוד בתוך Codespace חדש נותן לכם יותר שליטה על השימוש בדיסק.

#### טיפים

- תמיד החליפו את כתובת ה-URL של השכפול עם ה-Fork שלכם אם אתם רוצים לערוך/להתחייב.
- אם תצטרכו מאוחר יותר יותר היסטוריה או קבצים, תוכלו להביא אותם או להתאים את ה-Sparse-checkout לכלול תיקיות נוספות.

## הפעלת הקוד

הקורס מציע סדרת מחברות Jupyter שתוכלו להפעיל כדי להתנסות בבניית סוכני AI.

דוגמאות הקוד משתמשות באחת מהאפשרויות הבאות:

**דורש חשבון GitHub - חינם**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. מסומן כ-(semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. מסומן כ-(autogen.ipynb)

**דורש מנוי Azure**:
3) Azure AI Foundry + Azure AI Agent Service. מסומן כ-(azureaiagent.ipynb)

אנו ממליצים לכם לנסות את כל שלושת סוגי הדוגמאות כדי לראות מה עובד הכי טוב עבורכם.

האפשרות שתבחרו תקבע אילו שלבי הגדרה תצטרכו לבצע בהמשך:

## דרישות

- Python 3.12+
  - **הערה**: אם אין לכם Python3.12 מותקן, ודאו שאתם מתקינים אותו. לאחר מכן צרו את ה-venv שלכם באמצעות python3.12 כדי להבטיח שהגרסאות הנכונות יותקנו מקובץ requirements.txt.
  
    >דוגמה

    יצירת ספריית Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    לאחר מכן הפעילו את סביבת ה-venv עבור:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: עבור דוגמאות הקוד המשתמשות ב-.NET, ודאו שאתם מתקינים את ה-[.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) או גרסה מאוחרת יותר. לאחר מכן, בדקו את גרסת ה-.NET SDK המותקנת:

    ```bash|powershell
    dotnet --list-sdks
    ```

- חשבון GitHub - לגישה ל-GitHub Models Marketplace
- מנוי Azure - לגישה ל-Azure AI Foundry
- חשבון Azure AI Foundry - לגישה ל-Azure AI Agent Service

הוספנו קובץ `requirements.txt` בתיקיית השורש של מאגר זה שמכיל את כל חבילות ה-Python הנדרשות להפעלת דוגמאות הקוד.

תוכלו להתקין אותן על ידי הרצת הפקודה הבאה בטרמינל בתיקיית השורש של המאגר:

```bash|powershell
pip install -r requirements.txt
```

אנו ממליצים ליצור סביבת Python וירטואלית כדי להימנע מקונפליקטים ובעיות.

## הגדרת VSCode

ודאו שאתם משתמשים בגרסת ה-Python הנכונה ב-VSCode.

![תמונה](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## הגדרה לדוגמאות המשתמשות ב-GitHub Models 

### שלב 1: קבלת GitHub Personal Access Token (PAT)

הקורס הזה משתמש ב-GitHub Models Marketplace, שמספק גישה חינמית למודלים של שפה גדולה (LLMs) שתשתמשו בהם לבניית סוכני AI.

כדי להשתמש ב-GitHub Models, תצטרכו ליצור [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

ניתן לעשות זאת על ידי מעבר ל-<a href="https://github.com/settings/personal-access-tokens" target="_blank">הגדרות Personal Access Tokens</a> בחשבון ה-GitHub שלכם.

אנא עקבו אחר [עקרון המינימום הנדרש](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) בעת יצירת הטוקן. משמעות הדבר היא שעליכם לתת לטוקן רק את ההרשאות שהוא צריך כדי להפעיל את דוגמאות הקוד בקורס זה.

1. בחרו באפשרות `Fine-grained tokens` בצד שמאל של המסך על ידי מעבר ל-**Developer settings**

   ![הגדרות מפתחים](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.he.png)

   לאחר מכן בחרו `Generate new token`.

   ![יצירת טוקן](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.he.png)

2. הזינו שם תיאורי לטוקן שלכם שמשקף את מטרתו, כך שיהיה קל לזהות אותו מאוחר יותר.

    🔐 המלצה על משך זמן לטוקן

    משך זמן מומלץ: 30 ימים  
    עבור גישה מאובטחת יותר, תוכלו לבחור תקופה קצרה יותר—כמו 7 ימים 🛡️  
    זו דרך מצוינת להציב יעד אישי ולהשלים את הקורס בזמן שהמומנטום הלימודי שלכם גבוה 🚀.

    ![שם הטוקן ותאריך תפוגה](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.he.png)

3. הגבילו את תחום הטוקן ל-Fork שלכם של מאגר זה.

    ![הגבלת תחום ל-Fork](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.he.png)

4. הגבלות הרשאות הטוקן: תחת **Permissions**, לחצו על לשונית **Account**, ולחצו על כפתור "+ Add permissions". תופיע רשימה נפתחת. חפשו **Models** וסמנו את התיבה עבורו.

    ![הוספת הרשאת Models](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.he.png)

5. ודאו את ההרשאות הנדרשות לפני יצירת הטוקן. ![אימות הרשאות](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.he.png)

6. לפני יצירת הטוקן, ודאו שאתם מוכנים לאחסן את הטוקן במקום מאובטח כמו כספת מנהל סיסמאות, מכיוון שהוא לא יוצג שוב לאחר יצירתו. ![אחסון טוקן בצורה מאובטחת](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.he.png)

העתיקו את הטוקן החדש שיצרתם זה עתה. כעת תוסיפו אותו לקובץ `.env` הכלול בקורס זה.

### שלב 2: יצירת קובץ `.env`

כדי ליצור את קובץ ה-`.env` שלכם, הריצו את הפקודה הבאה בטרמינל.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

זה יעתיק את קובץ הדוגמה וייצור `.env` בתיקייה שלכם, שם תמלאו את הערכים עבור משתני הסביבה.

עם הטוקן שהעתקתם, פתחו את קובץ ה-`.env` בעורך הטקסט המועדף עליכם והדביקו את הטוקן בשדה `GITHUB_TOKEN`.

![שדה טוקן GitHub](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.he.png)

כעת אמורים להיות לכם כל הכלים להפעלת דוגמאות הקוד של הקורס.

## הגדרה לדוגמאות המשתמשות ב-Azure AI Foundry וב-Azure AI Agent Service

### שלב 1: קבלת נקודת הקצה של פרויקט Azure שלכם

עקבו אחר השלבים ליצירת Hub ופרויקט ב-Azure AI Foundry שנמצאים כאן: [סקירת משאבי Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)

לאחר שיצרתם את הפרויקט שלכם, תצטרכו לקבל את מחרוזת החיבור לפרויקט שלכם.

ניתן לעשות זאת על ידי מעבר לדף **Overview** של הפרויקט שלכם בפורטל Azure AI Foundry.

![מחרוזת חיבור לפרויקט](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.he.png)

### שלב 2: יצירת קובץ `.env`

כדי ליצור את קובץ ה-`.env` שלכם, הריצו את הפקודה הבאה בטרמינל.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

זה יעתיק את קובץ הדוגמה וייצור `.env` בתיקייה שלכם, שם תמלאו את הערכים עבור משתני הסביבה.

עם הטוקן שהעתקתם, פתחו את קובץ ה-`.env` בעורך הטקסט המועדף עליכם והדביקו את הטוקן בשדה `PROJECT_ENDPOINT`.

### שלב 3: התחברות ל-Azure

כחלק מהמלצות אבטחה, נשתמש ב-[אימות ללא מפתח](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) כדי לאמת ל-Azure OpenAI עם Microsoft Entra ID. 

לאחר מכן, פתחו טרמינל והריצו `az login --use-device-code` כדי להתחבר לחשבון Azure שלכם.

לאחר שהתחברתם, בחרו את המנוי שלכם בטרמינל.

## משתני סביבה נוספים - Azure Search ו-Azure OpenAI 

עבור שיעור Agentic RAG - שיעור 5 - יש דוגמאות שמשתמשות ב-Azure Search וב-Azure OpenAI.

אם ברצונכם להפעיל דוגמאות אלו, תצטרכו להוסיף את משתני הסביבה הבאים לקובץ ה-`.env` שלכם:

### דף סקירה (פרויקט)

- `AZURE_SUBSCRIPTION_ID` - בדקו **פרטי פרויקט** בדף **Overview** של הפרויקט שלכם.

- `AZURE_AI_PROJECT_NAME` - הסתכלו בראש דף **Overview** של הפרויקט שלכם.

- `AZURE_OPENAI_SERVICE` - מצאו זאת בלשונית **Included capabilities** עבור **Azure OpenAI Service** בדף **Overview**.

### מרכז ניהול

- `AZURE_OPENAI_RESOURCE_GROUP` - עברו ל-**Project properties** בדף **Overview** של **Management Center**.

- `GLOBAL_LLM_SERVICE` - תחת **Connected resources**, מצאו את שם החיבור של **Azure AI Services**. אם לא מופיע, בדקו את **Azure portal** תחת קבוצת המשאבים שלכם עבור שם משאב AI Services.

### דף מודלים + נקודות קצה

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - בחרו את מודל ההטמעה שלכם (לדוגמה, `text-embedding-ada-002`) ורשמו את **Deployment name** מפרטי המודל.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - בחרו את מודל הצ'אט שלכם (לדוגמה, `gpt-4o-mini`) ורשמו את **Deployment name** מפרטי המודל.

### פורטל Azure

- `AZURE_OPENAI_ENDPOINT` - חפשו **Azure AI services**, לחצו עליו, ואז עברו ל-**Resource Management**, **Keys and Endpoint**, גללו למטה ל-"Azure OpenAI endpoints", והעתיקו את זה שאומר "Language APIs".

- `AZURE_OPENAI_API_KEY` - מאותו מסך, העתיקו את KEY 1 או KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - מצאו את משאב **Azure AI Search** שלכם, לחצו עליו, וראו **Overview**.

- `AZURE_SEARCH_API_KEY` - לאחר מכן עברו ל-**Settings** ואז ל-**Keys** כדי להעתיק את המפתח הראשי או המשני.

### דף חיצוני

- `
אם יש לכם בעיות בהפעלת ההגדרה הזו, הצטרפו ל-<a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> שלנו או <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">צרו בעיה</a>.

## השיעור הבא

אתם עכשיו מוכנים להפעיל את הקוד עבור הקורס הזה. למידה נעימה על העולם של סוכני AI!

[מבוא לסוכני AI ושימושים של סוכנים](../01-intro-to-ai-agents/README.md)

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.