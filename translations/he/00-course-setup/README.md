<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T11:50:51+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "he"
}
-->
# הגדרת הקורס

## מבוא

השיעור הזה יעסוק כיצד להריץ את דוגמאות הקוד של הקורס הזה.

## הצטרפות ללומדים אחרים וקבלת עזרה

לפני שתתחילו לשכפל את המאגר שלכם, הצטרפו לערוץ [AI Agents For Beginners ב-Discord](https://aka.ms/ai-agents/discord) כדי לקבל עזרה בהגדרות, לשאול שאלות על הקורס או להתחבר ללומדים אחרים.

## שכפול או יצירת מאגר נגזר

כדי להתחיל, אנא שכפלו או צרו מאגר נגזר ממאגר ה-GitHub. זה ייצור גרסה משלכם של חומרי הקורס כך שתוכלו להריץ, לבדוק ולשנות את הקוד!

ניתן לעשות זאת על ידי לחיצה על הקישור ל-<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">יצירת מאגר נגזר</a>

כעת אמור להיות לכם גרסה נגזרת משלכם של הקורס בקישור הבא:

![מאגר נגזר](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.he.png)

### שכפול רדוד (מומלץ לסדנאות / Codespaces)

  >המאגר המלא יכול להיות גדול (~3 GB) כאשר מורידים את כל ההיסטוריה וכל הקבצים. אם אתם רק משתתפים בסדנה או זקוקים רק לכמה תיקיות שיעורים, שכפול רדוד (או שכפול חלקי) ימנע את רוב ההורדה הזו על ידי קיצור ההיסטוריה ו/או דילוג על קבצים.

#### שכפול רדוד מהיר — היסטוריה מינימלית, כל הקבצים

החליפו את `<your-username>` בכתובת ה-URL של המאגר הנגזר שלכם (או בכתובת ה-URL המקורית אם אתם מעדיפים).

כדי לשכפל רק את ההיסטוריה של הקומיט האחרון (הורדה קטנה):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

כדי לשכפל ענף ספציפי:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### שכפול חלקי — קבצים מינימליים + רק תיקיות נבחרות

זה משתמש בשכפול חלקי וב-sparse-checkout (דורש Git 2.25+ ומומלץ להשתמש בגרסת Git מודרנית עם תמיכה בשכפול חלקי):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

עברו לתיקיית המאגר:

עבור bash:

```bash
cd ai-agents-for-beginners
```

עבור Powershell:

```powershell
Set-Location ai-agents-for-beginners
```

לאחר מכן ציינו אילו תיקיות אתם רוצים (הדוגמה למטה מציגה שתי תיקיות):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

לאחר השכפול ואימות הקבצים, אם אתם זקוקים רק לקבצים ורוצים לפנות מקום (ללא היסטוריית git), אנא מחקו את המטא-נתונים של המאגר (💀בלתי הפיך — תאבדו את כל הפונקציונליות של Git: אין קומיטים, משיכות, דחיפות או גישה להיסטוריה).

עבור Linux/macOS:

```bash
rm -rf .git
```

עבור Windows:

```powershell
Remove-Item -Recurse -Force .git
```

#### שימוש ב-GitHub Codespaces (מומלץ כדי להימנע מהורדות גדולות מקומיות)

- צרו Codespace חדש עבור המאגר הזה דרך [ממשק המשתמש של GitHub](https://github.com/codespaces).  

- בטרמינל של ה-Codespace החדש שנוצר, הריצו אחת מהפקודות לשכפול רדוד/חלקי שהוזכרו לעיל כדי להביא רק את תיקיות השיעורים שאתם צריכים לתוך סביבת העבודה של Codespace.
- אופציונלי: לאחר השכפול בתוך Codespaces, הסירו את .git כדי לשחרר מקום נוסף (ראו את פקודות ההסרה לעיל).
- הערה: אם אתם מעדיפים לפתוח את המאגר ישירות ב-Codespaces (ללא שכפול נוסף), שימו לב ש-Codespaces יבנה את סביבת devcontainer וייתכן שעדיין יכין יותר ממה שאתם צריכים. שכפול רדוד בתוך Codespace חדש נותן לכם יותר שליטה על השימוש בדיסק.

#### טיפים

- תמיד החליפו את כתובת ה-URL של השכפול במאגר הנגזר שלכם אם אתם רוצים לערוך/לשמור שינויים.
- אם תצטרכו מאוחר יותר יותר היסטוריה או קבצים, תוכלו להביא אותם או להתאים את ה-sparse-checkout כדי לכלול תיקיות נוספות.

## הרצת הקוד

הקורס הזה מציע סדרת מחברות Jupyter שתוכלו להריץ כדי לקבל ניסיון מעשי בבניית סוכני AI.

דוגמאות הקוד משתמשות באחת מהאפשרויות הבאות:

**נדרש חשבון GitHub - חינם**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. מסומן כ-(semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. מסומן כ-(autogen.ipynb)

**נדרש מנוי Azure**:
3) Azure AI Foundry + Azure AI Agent Service. מסומן כ-(azureaiagent.ipynb)

אנו ממליצים לכם לנסות את כל שלושת סוגי הדוגמאות כדי לראות איזו מהן מתאימה לכם ביותר.

האפשרות שתבחרו תקבע אילו שלבי הגדרה תצטרכו לבצע בהמשך:

## דרישות

- Python 3.12+
  - **NOTE**: אם אין לכם Python3.12 מותקן, ודאו שאתם מתקינים אותו. לאחר מכן צרו את venv שלכם באמצעות python3.12 כדי להבטיח שהגרסאות הנכונות יותקנו מקובץ requirements.txt.
  
    >דוגמה

    יצירת תיקיית Python venv:

    ``` bash
    python3 -m venv venv
    ```

    לאחר מכן הפעילו את סביבת venv עבור:

    macOS ו-Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- חשבון GitHub - לגישה ל-GitHub Models Marketplace
- מנוי Azure - לגישה ל-Azure AI Foundry
- חשבון Azure AI Foundry - לגישה ל-Azure AI Agent Service

הוספנו קובץ `requirements.txt` בשורש של המאגר הזה שמכיל את כל חבילות ה-Python הנדרשות להרצת דוגמאות הקוד.

תוכלו להתקין אותן על ידי הרצת הפקודה הבאה בטרמינל בשורש של המאגר:

```bash
pip install -r requirements.txt
```

אנו ממליצים ליצור סביבת Python וירטואלית כדי להימנע מכל קונפליקטים ובעיות.

## הגדרת VSCode
ודאו שאתם משתמשים בגרסה הנכונה של Python ב-VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## הגדרה לדוגמאות באמצעות GitHub Models 

### שלב 1: השגת אסימון הגישה האישית שלכם ב-GitHub (PAT)

הקורס הזה משתמש ב-GitHub Models Marketplace, המספק גישה חינמית למודלים של שפה גדולה (LLMs) שתשתמשו בהם לבניית סוכני AI.

כדי להשתמש במודלים של GitHub, תצטרכו ליצור [אסימון גישה אישית ב-GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

ניתן לעשות זאת על ידי מעבר ל-<a href="https://github.com/settings/personal-access-tokens" target="_blank">הגדרות אסימוני גישה אישית</a> בחשבון ה-GitHub שלכם.

אנא עקבו אחר [עקרון המינימום הנדרש](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) בעת יצירת האסימון. משמעות הדבר היא שעליכם להעניק לאסימון רק את ההרשאות שהוא צריך כדי להריץ את דוגמאות הקוד בקורס הזה.

1. בחרו באפשרות `Fine-grained tokens` בצד השמאלי של המסך על ידי מעבר ל-**Developer settings**
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.he.png)

    לאחר מכן בחרו ב-`Generate new token`.

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.he.png)

2. הזינו שם תיאורי לאסימון שלכם שמשקף את מטרתו, כך שיהיה קל לזהות אותו מאוחר יותר.


    🔐 המלצה על משך זמן האסימון

    משך זמן מומלץ: 30 ימים
    עבור גישה מאובטחת יותר, תוכלו לבחור תקופה קצרה יותר—כמו 7 ימים 🛡️
    זו דרך מצוינת להציב מטרה אישית ולסיים את הקורס בזמן שהמומנטום הלימודי שלכם גבוה 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.he.png)

3. הגבילו את טווח האסימון למאגר הנגזר שלכם.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.he.png)

4. הגבלות על הרשאות האסימון: תחת **Permissions**, לחצו על לשונית **Account**, ולחצו על כפתור "+ Add permissions". תופיע תיבת בחירה. חפשו את **Models** וסמנו את התיבה עבורו.
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.he.png)

5. ודאו את ההרשאות הנדרשות לפני יצירת האסימון. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.he.png)

6. לפני יצירת האסימון, ודאו שאתם מוכנים לשמור את האסימון במקום בטוח כמו כספת מנהל סיסמאות, מכיוון שהוא לא יוצג שוב לאחר יצירתו. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.he.png)

העתיקו את האסימון החדש שיצרתם. כעת תוסיפו אותו לקובץ `.env` הכלול בקורס הזה.


### שלב 2: יצירת קובץ `.env`

כדי ליצור את קובץ ה-`.env` שלכם, הריצו את הפקודה הבאה בטרמינל.

```bash
cp .env.example .env
```

זה יעתיק את קובץ הדוגמה ויצור `.env` בתיקייה שלכם, שם תמלאו את הערכים עבור משתני הסביבה.

עם האסימון שהעתקתם, פתחו את קובץ ה-`.env` בעורך הטקסט המועדף עליכם והדביקו את האסימון בשדה `GITHUB_TOKEN`.
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.he.png)


כעת אמורים להיות לכם הכלים להריץ את דוגמאות הקוד של הקורס הזה.

## הגדרה לדוגמאות באמצעות Azure AI Foundry ו-Azure AI Agent Service

### שלב 1: השגת נקודת הקצה של הפרויקט שלכם ב-Azure


עקבו אחר השלבים ליצירת hub ופרויקט ב-Azure AI Foundry שנמצאים כאן: [סקירת משאבי Hub](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)


לאחר שיצרתם את הפרויקט שלכם, תצטרכו להשיג את מחרוזת החיבור לפרויקט שלכם.

ניתן לעשות זאת על ידי מעבר לדף **Overview** של הפרויקט שלכם בפורטל Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.he.png)

### שלב 2: יצירת קובץ `.env`

כדי ליצור את קובץ ה-`.env` שלכם, הריצו את הפקודה הבאה בטרמינל.

```bash
cp .env.example .env
```

זה יעתיק את קובץ הדוגמה ויצור `.env` בתיקייה שלכם, שם תמלאו את הערכים עבור משתני הסביבה.

עם האסימון שהעתקתם, פתחו את קובץ ה-`.env` בעורך הטקסט המועדף עליכם והדביקו את האסימון בשדה `PROJECT_ENDPOINT`.

### שלב 3: התחברות ל-Azure

כחלק מהמלצות אבטחה, נשתמש ב-[אימות ללא מפתח](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) כדי להתחבר ל-Azure OpenAI עם Microsoft Entra ID. 

לאחר מכן, פתחו טרמינל והריצו `az login --use-device-code` כדי להתחבר לחשבון Azure שלכם.

לאחר ההתחברות, בחרו את המנוי שלכם בטרמינל.


## משתני סביבה נוספים - Azure Search ו-Azure OpenAI 

עבור שיעור Agentic RAG - שיעור 5 - יש דוגמאות שמשתמשות ב-Azure Search וב-Azure OpenAI.

אם אתם רוצים להריץ את הדוגמאות האלה, תצטרכו להוסיף את משתני הסביבה הבאים לקובץ ה-`.env` שלכם:

### דף סקירה כללית (פרויקט)

- `AZURE_SUBSCRIPTION_ID` - בדקו את **פרטי הפרויקט** בדף **Overview** של הפרויקט שלכם.

- `AZURE_AI_PROJECT_NAME` - הסתכלו בראש דף **Overview** של הפרויקט שלכם.

- `AZURE_OPENAI_SERVICE` - מצאו זאת בלשונית **Included capabilities** עבור **Azure OpenAI Service** בדף **Overview**.

### מרכז ניהול

- `AZURE_OPENAI_RESOURCE_GROUP` - עברו ל-**Project properties** בדף **Overview** של **מרכז הניהול**.

- `GLOBAL_LLM_SERVICE` - תחת **Connected resources**, מצאו את שם החיבור של **Azure AI Services**. אם לא מופיע, בדקו את **פורטל Azure** תחת קבוצת המשאבים שלכם עבור שם משאב AI Services.

### דף מודלים + נקודות קצה

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - בחרו את מודל ההטמעה שלכם (לדוגמה, `text-embedding-ada-002`) ורשמו את **שם הפריסה** מפרטי המודל.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - בחרו את מודל הצ'אט שלכם (לדוגמה, `gpt-4o-mini`) ורשמו את **שם הפריסה** מפרטי המודל.

### פורטל Azure

- `AZURE_OPENAI_ENDPOINT` - חפשו את **שירותי Azure AI**, לחצו עליו, ואז עברו ל-**Resource Management**, **Keys and Endpoint**, גללו למטה ל-"Azure OpenAI endpoints", והעתיקו את זה שאומר "Language APIs".

- `AZURE_OPENAI_API_KEY` - מאותו מסך, העתיקו את KEY 1 או KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - מצאו את משאב **Azure AI Search** שלכם, לחצו עליו, וראו **Overview**.

- `AZURE_SEARCH_API_KEY` - לאחר מכן עברו ל-**Settings** ואז ל-**Keys** כדי להעתיק את המפתח הראשי או המשני.

### דף חיצוני

- `AZURE_OPENAI_API_VERSION` - בקרו בדף [מחזור חיים של גרסת API](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) תחת **Latest GA API release**.

### הגדרת אימות ללא מפתח

במקום להכניס את האישורים שלכם באופן ידני, נשתמש בחיבור ללא מפתח עם Azure OpenAI. לשם כך, נייבא את `DefaultAzureCredential` ולאחר מכן נקרא לפונקציה `DefaultAzureCredential` כדי לקבל את האישורים.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## נתקעתם איפשהו?
אם יש לכם בעיות בהפעלת ההגדרות הללו, הצטרפו ל-<a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> שלנו או <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">צרו בעיה חדשה</a>.

## השיעור הבא

אתם מוכנים עכשיו להפעיל את הקוד של הקורס הזה. למידה נעימה על עולם סוכני הבינה המלאכותית!

[מבוא לסוכני בינה מלאכותית ושימושים בסוכנים](../01-intro-to-ai-agents/README.md)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.