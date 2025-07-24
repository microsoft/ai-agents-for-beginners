<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c6a79c8f2b56a80370ff7e447765524f",
  "translation_date": "2025-07-24T08:39:01+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "he"
}
-->
# הגדרת הקורס

## מבוא

בשיעור זה נלמד כיצד להריץ את דוגמאות הקוד של הקורס.

## שכפול או יצירת Fork למאגר זה

כדי להתחיל, יש לשכפל או ליצור Fork למאגר ה-GitHub. פעולה זו תיצור גרסה משלכם של חומרי הקורס, כך שתוכלו להריץ, לבדוק ולשנות את הקוד!

ניתן לעשות זאת על ידי לחיצה על הקישור ל-

![מאגר משוכפל](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.he.png)

## הרצת הקוד

הקורס מציע סדרת מחברות Jupyter שניתן להריץ כדי להתנסות בבניית סוכני AI.

דוגמאות הקוד משתמשות באחת מהאפשרויות הבאות:

**דורש חשבון GitHub - חינם**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. מסומן כ-(semantic-kernel.ipynb)  
2) AutoGen Framework + GitHub Models Marketplace. מסומן כ-(autogen.ipynb)  

**דורש מנוי Azure**:  
3) Azure AI Foundry + Azure AI Agent Service. מסומן כ-(azureaiagent.ipynb)  

אנו ממליצים לנסות את כל שלושת סוגי הדוגמאות כדי לראות מה מתאים לכם ביותר.

האפשרות שתבחרו תקבע אילו שלבי הגדרה תצטרכו לבצע בהמשך:

## דרישות

- Python 3.12+  
  - **הערה**: אם אין לכם Python 3.12 מותקן, ודאו שאתם מתקינים אותו. לאחר מכן, צרו סביבה וירטואלית (venv) באמצעות python3.12 כדי להבטיח התקנה נכונה של הגרסאות מתוך קובץ requirements.txt.  
- חשבון GitHub - לגישה ל-GitHub Models Marketplace  
- מנוי Azure - לגישה ל-Azure AI Foundry  
- חשבון Azure AI Foundry - לגישה ל-Azure AI Agent Service  

כלול במאגר זה קובץ `requirements.txt` שמכיל את כל חבילות ה-Python הנדרשות להרצת דוגמאות הקוד.

ניתן להתקין אותן על ידי הרצת הפקודה הבאה בטרמינל בתיקיית השורש של המאגר:

```bash
pip install -r requirements.txt
```  
מומלץ ליצור סביבה וירטואלית של Python כדי למנוע קונפליקטים ובעיות.

## הגדרת VSCode
ודאו שאתם משתמשים בגרסת ה-Python הנכונה ב-VSCode.

![תמונה](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## הגדרה לדוגמאות המשתמשות ב-GitHub Models 

### שלב 1: קבלת GitHub Personal Access Token (PAT)

הקורס משתמש ב-GitHub Models Marketplace, שמספק גישה חינמית למודלים של שפה גדולה (LLMs) שתשתמשו בהם לבניית סוכני AI.

כדי להשתמש ב-GitHub Models, תצטרכו ליצור [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

ניתן לעשות זאת על ידי כניסה ל-

אנא עקבו אחר [עקרון המינימום הנדרש](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) בעת יצירת הטוקן. משמעות הדבר היא שעליכם להעניק לטוקן רק את ההרשאות הנדרשות להרצת דוגמאות הקוד בקורס זה.

1. בחרו באפשרות `Fine-grained tokens` בצד השמאלי של המסך.

    לאחר מכן בחרו `Generate new token`.

    ![יצירת טוקן](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.he.png)

1. הזינו שם תיאורי לטוקן שמשקף את מטרתו, כך שיהיה קל לזהות אותו מאוחר יותר. הגדירו תאריך תפוגה (מומלץ: 30 ימים; ניתן לבחור תקופה קצרה יותר כמו 7 ימים אם אתם מעדיפים גישה מאובטחת יותר).

    ![שם ותאריך תפוגה לטוקן](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.he.png)

1. הגבילו את תחום הטוקן ל-Fork של מאגר זה.

    ![הגבלת תחום למאגר משוכפל](../../../translated_images/select-fork-repository.4497f6bb05ccd6b474ed134493a815fc34f94f89db2b1630c494adff7b5b558a.he.png)

1. הגבלות על הרשאות הטוקן: תחת **Permissions**, הפעילו את **Account Permissions**, עברו ל-**Models** ואפשרו רק את גישת הקריאה הנדרשת עבור GitHub Models.

    ![הרשאות חשבון](../../../translated_images/account-permissions.de1806fad33a72c6194d2688cf2c10f2adb9ff7a5c1041a2329cbef46bffbba0.he.png)

    ![גישה לקריאה למודלים](../../../translated_images/models-read-access.c00bc44e28c40450a85542e19f8e8c68284c71861c076b7dbc078b4c7e51faa6.he.png)

העתיקו את הטוקן החדש שיצרתם. כעת תוסיפו אותו לקובץ `.env` הכלול בקורס זה.

### שלב 2: יצירת קובץ `.env`

כדי ליצור את קובץ ה-`.env`, הריצו את הפקודה הבאה בטרמינל.

```bash
cp .env.example .env
```

פקודה זו תעתיק את קובץ הדוגמה ותיצור `.env` בתיקייה שלכם, שם תמלאו את הערכים עבור משתני הסביבה.

עם הטוקן שהעתקתם, פתחו את קובץ ה-`.env` בעורך הטקסט המועדף עליכם והדביקו את הטוקן בשדה `GITHUB_TOKEN`.

כעת תוכלו להריץ את דוגמאות הקוד של הקורס.

## הגדרה לדוגמאות המשתמשות ב-Azure AI Foundry וב-Azure AI Agent Service

### שלב 1: קבלת נקודת הקצה של פרויקט Azure שלכם

עקבו אחר השלבים ליצירת Hub ופרויקט ב-Azure AI Foundry בקישור הבא: [סקירת משאבי Hub](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

לאחר שיצרתם את הפרויקט, תצטרכו לקבל את מחרוזת החיבור של הפרויקט.

ניתן לעשות זאת על ידי מעבר לעמוד **Overview** של הפרויקט בפורטל Azure AI Foundry.

![מחרוזת חיבור לפרויקט](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.he.png)

### שלב 2: יצירת קובץ `.env`

כדי ליצור את קובץ ה-`.env`, הריצו את הפקודה הבאה בטרמינל.

```bash
cp .env.example .env
```

פקודה זו תעתיק את קובץ הדוגמה ותיצור `.env` בתיקייה שלכם, שם תמלאו את הערכים עבור משתני הסביבה.

עם הטוקן שהעתקתם, פתחו את קובץ ה-`.env` בעורך הטקסט המועדף עליכם והדביקו את הטוקן בשדה `PROJECT_ENDPOINT`.

### שלב 3: התחברות ל-Azure

כחלק מהמלצות האבטחה, נשתמש ב-[אימות ללא מפתח](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) כדי לאמת את Azure OpenAI עם Microsoft Entra ID.

לאחר מכן, פתחו טרמינל והריצו `az login --use-device-code` כדי להתחבר לחשבון Azure שלכם.

לאחר ההתחברות, בחרו את המנוי שלכם בטרמינל.

## משתני סביבה נוספים - Azure Search ו-Azure OpenAI

עבור שיעור Agentic RAG - שיעור 5 - יש דוגמאות המשתמשות ב-Azure Search וב-Azure OpenAI.

אם ברצונכם להריץ דוגמאות אלו, תצטרכו להוסיף את משתני הסביבה הבאים לקובץ ה-`.env` שלכם:

### עמוד סקירה כללית (פרויקט)

- `AZURE_SUBSCRIPTION_ID` - בדקו את **פרטי הפרויקט** בעמוד **Overview** של הפרויקט שלכם.

- `AZURE_AI_PROJECT_NAME` - הסתכלו בראש עמוד **Overview** של הפרויקט שלכם.

- `AZURE_OPENAI_SERVICE` - מצאו זאת בלשונית **Included capabilities** עבור **Azure OpenAI Service** בעמוד **Overview**.

### מרכז ניהול

- `AZURE_OPENAI_RESOURCE_GROUP` - עברו ל-**Project properties** בעמוד **Overview** של **Management Center**.

- `GLOBAL_LLM_SERVICE` - תחת **Connected resources**, מצאו את שם החיבור של **Azure AI Services**. אם אינו מופיע, בדקו בפורטל Azure תחת קבוצת המשאבים שלכם את שם משאבי ה-AI Services.

### עמוד מודלים + נקודות קצה

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - בחרו את מודל ההטמעה שלכם (לדוגמה, `text-embedding-ada-002`) ורשמו את **שם הפריסה** מתוך פרטי המודל.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - בחרו את מודל הצ'אט שלכם (לדוגמה, `gpt-4o-mini`) ורשמו את **שם הפריסה** מתוך פרטי המודל.

### פורטל Azure

- `AZURE_OPENAI_ENDPOINT` - חפשו את **Azure AI services**, לחצו עליו, ואז עברו ל-**Resource Management**, **Keys and Endpoint**, גללו למטה ל-"Azure OpenAI endpoints", והעתיקו את זה שמסומן "Language APIs".

- `AZURE_OPENAI_API_KEY` - מאותו מסך, העתיקו את KEY 1 או KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - מצאו את משאב **Azure AI Search**, לחצו עליו, וצפו ב-**Overview**.

- `AZURE_SEARCH_API_KEY` - לאחר מכן עברו ל-**Settings** ואז ל-**Keys** כדי להעתיק את המפתח הראשי או המשני.

### עמוד חיצוני

- `AZURE_OPENAI_API_VERSION` - בקרו בעמוד [מחזור חיי גרסאות API](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) תחת **Latest GA API release**.

### הגדרת אימות ללא מפתח

במקום להכניס את האישורים שלכם באופן ידני, נשתמש בחיבור ללא מפתח עם Azure OpenAI. לשם כך, נייבא את `DefaultAzureCredential` ונקרא לפונקציה `DefaultAzureCredential` כדי לקבל את האישורים.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## נתקעתם איפשהו?

אם יש לכם בעיות בהרצת ההגדרות, הצטרפו ל-

## השיעור הבא

כעת אתם מוכנים להריץ את הקוד של הקורס. למידה מהנה על עולם סוכני ה-AI!

[מבוא לסוכני AI ושימושים](../01-intro-to-ai-agents/README.md)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי בני אדם. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.