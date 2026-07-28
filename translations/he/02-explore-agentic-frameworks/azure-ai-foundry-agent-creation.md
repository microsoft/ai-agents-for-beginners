# פיתוח שירות סוכן Microsoft Foundry  

בתרגיל זה, תשתמש בכלי Microsoft Foundry Agent Service ב-[פורטל Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) כדי ליצור סוכן להזמנת טיסות. הסוכן יוכל לתקשר עם משתמשים ולספק מידע על טיסות.  

## דרישות מוקדמות  

כדי להשלים את התרגיל, אתה זקוק לדברים הבאים:  
1. חשבון Azure עם מנוי פעיל. [צור חשבון בחינם](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).  
2. הרשאות ליצירת מרכז Microsoft Foundry או שמישהו ייצור עבורך אחד.  
    - אם התפקיד שלך הוא Contributor או Owner, תוכל לעקוב אחר השלבים במדריך זה.  

## יצירת מרכז Microsoft Foundry  

> **הערה:** Microsoft Foundry נקרא בעבר Azure AI Studio.  

1. עקוב אחרי ההנחיות בפוסט הבלוג של [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) ליצירת מרכז Microsoft Foundry.  
2. כאשר הפרויקט שלך נוצר, סגור כל טיפים שמופיעים ועיין בדף הפרויקט בפורטל Microsoft Foundry, שיראה דומה לתמונה הבאה:  

    ![פרויקט Microsoft Foundry](../../../translated_images/he/azure-ai-foundry.88d0c35298348c2f.webp)  

## פריסת מודל  

1. בפאנל השמאלי של הפרויקט שלך, בקטגוריית **הנכסים שלי**, בחר בדף **מודלים + נקודות קצה**.  
2. בדף **מודלים + נקודות קצה**, בכרטיסיית **פריסות מודלים**, בתפריט **+ פריסת מודל**, בחר **פריסת מודל בסיסי**.  
3. חפש את המודל `gpt-5-mini` ברשימה, ואז בחר ואשר אותו.  

    > **הערה**: הקטנת TPM עוזרת למנוע שימוש יתר במכסת השימוש הזמינה במנוי שבו אתה משתמש.  

    ![מודל הופשר](../../../translated_images/he/model-deployment.3749c53fb81e18fd.webp)  

## יצירת סוכן  

כעת כשפרסת מודל, תוכל ליצור סוכן. סוכן הוא מודל שיחה מבוסס בינה מלאכותית שניתן להשתמש בו לתקשורת עם המשתמשים.  

1. בפאנל השמאלי של הפרויקט שלך, בקטגוריית **בנה והתאמה אישית**, בחר בדף **סוכנים**.  
2. לחץ על **+ צור סוכן** כדי ליצור סוכן חדש. בתיבת הדו-שיח **הגדרת סוכן**:  
    - הזן שם לסוכן, כמו `FlightAgent`.  
    - ודא שהפריסה של המודל `gpt-5-mini` שיצרת קודם נבחרה.  
    - הגדר את **ההוראות** בהתאם להנחיות שברצונך שהסוכן יעקוב אחריהן. הנה דוגמה:  
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]  
> עבור הנחיית פרומפט מפורטת, תוכל לעיין ב-[מאגר זה](https://github.com/ShivamGoyal03/RoamMind) למידע נוסף.  
    
> בנוסף, ניתן להוסיף **בסיס ידע** ו**פעולות** כדי לשפר את יכולות הסוכן לספק מידע נוסף ולבצע משימות אוטומטיות המבוססות על בקשות משתמש. לתרגיל זה תוכל לדלג על שלבים אלו.  
    
![הגדרת סוכן](../../../translated_images/he/agent-setup.9bbb8755bf5df672.webp)  

3. כדי ליצור סוכן עם מספר בינה מלאכותית, פשוט לחץ על **סוכן חדש**. הסוכן שנוצר יוצג אז בדף הסוכנים.  


## בדיקת הסוכן  

לאחר יצירת הסוכן, תוכל לבדוק כיצד הוא מגיב לשאילתות משתמשים במחולל הפורטל Microsoft Foundry.  

1. בראש הפאנל **הגדרה** של הסוכן, בחר ב**נסה במגרש המשחקים**.  
2. בפאנל **מגרש המשחקים** תוכל לתקשר עם הסוכן על ידי הקלדת שאילתות בחלון הצ’אט. לדוגמה, תוכל לבקש מהסוכן לחפש טיסות מסיאטל לניו יורק בתאריך 28.  

    > **הערה**: ייתכן שהסוכן לא יספק תגובות מדויקות, מאחר שבתרגיל זה לא נעשה שימוש בנתונים בזמן אמת. המטרה היא לבדוק את יכולת הסוכן להבין ולהגיב לבקשות המשתמש על פי ההוראות שניתנו.  

    ![מגרש משחקים של סוכן](../../../translated_images/he/agent-playground.dc146586de715010.webp)  

3. לאחר בדיקת הסוכן, תוכל להמשיך להתאים אותו על ידי הוספת כוונות, נתוני אימון ופעולות נוספות כדי לשפר את יכולותיו.  

## ניקוי משאבים  

לאחר שסיימת לבדוק את הסוכן, תוכל למחוק אותו כדי למנוע עלויות נוספות.  
1. פתח את [פורטל Azure](https://portal.azure.com) וצפה בתוכן קבוצת המשאבים שבה פרסת את משאבי המרכז שהשתמשת בהם בתרגיל זה.  
2. בסרגל הכלים, בחר **מחק קבוצת משאבים**.  
3. הזן את שם קבוצת המשאבים ואשר את רצונך למחוק אותה.  

## משאבים  

- [תיעוד Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)  
- [פורטל Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)  
- [התחלה עם Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)  
- [יסודות סוכני בינה מלאכותית ב-Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)  
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->