[![סוכני AI אמינים](../../../translated_images/he/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(לחצו על התמונה למעלה לצפייה בסרטון של השיעור)_

# בניית סוכני AI אמינים

## מבוא

בשיעור זה נכסה:

- כיצד לבנות ולפרוס סוכני AI בטוחים ויעילים
- שיקולי אבטחה חשובים בעת פיתוח סוכני AI.
- כיצד לשמור על פרטיות הנתונים והמשתמש בעת פיתוח סוכני AI.

## מטרות הלמידה

בסיום שיעור זה, תדעו כיצד:

- לזהות ולהפחית סיכונים ביצירת סוכני AI.
- ליישם אמצעי אבטחה כדי להבטיח שניהול הנתונים והגישה נעשים כראוי.
- ליצור סוכני AI שמקפידים על פרטיות הנתונים ומספקים חוויית משתמש איכותית.

## בטיחות

נבחן תחילה בניית יישומים סוכניים בטוחים. בטיחות משמעותה שהסוכן מבצע את תפקידו כמתוכנן. כבוני יישומים סוכניים, יש לנו שיטות וכלים למקסום הבטיחות:

### בניית מסגרת הודעות מערכת

אם יצרתם אי פעם יישום AI המשתמש במודלים שפתיים גדולים (LLMs), אתם יודעים את חשיבות תכנון קלט מערכת איתן או הודעת מערכת. קלטים אלה מגדירים את הכללים המטא, ההוראות וההנחיות לאופן שבו ה-LLM יתקשר עם המשתמש והנתונים.

עבור סוכני AI, קלט המערכת אפילו חשוב יותר שכן הסוכנים יצטרכו הוראות מאוד ספציפיות כדי להשלים את המשימות שעיצבנו עבורם.

כדי ליצור קלטי מערכת ניתנים להרחבה, נוכל להשתמש במסגרת הודעות מערכת לבניית סוכן אחד או יותר ביישום שלנו:

![Building a System Message Framework](../../../translated_images/he/system-message-framework.3a97368c92d11d68.webp)

#### שלב 1: צור הודעת מערכת מטא

קלט המטא ישמש את ה-LLM ליצירת קלטי מערכת עבור הסוכנים שנבנה. אנו מעצבים זאת כתבנית כדי שנוכל ליצור ביעילות סוכנים רבים במידת הצורך.

הנה דוגמה להודעת מערכת מטא שנעניק ל-LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### שלב 2: צור קלט בסיסי

השלב הבא הוא ליצור קלט בסיסי לתיאור סוכן ה-AI. יש לכלול את תפקיד הסוכן, המשימות שהסוכן ישלים וכל אחריות נוספת של הסוכן.

הנה דוגמה:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### שלב 3: ספק הודעת מערכת בסיסית ל-LLM

כעת נוכל לייעל הודעת מערכת זו על ידי מתן הודעת המערכת המטא וכן הודעת המערכת הבסיסית שלנו.

זה יפיק הודעת מערכת שתוכננה טוב יותר להנחיית סוכני ה-AI שלנו:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### שלב 4: חזור ופתח

הערך של מסגרת הודעות מערכת זו הוא ביכולת להרחיב את יצירת הודעות מערכת עבור סוכנים רבים בקלות וכן לשפר את הודעות המערכת שלכם לאורך זמן. נדיר שיהיה לכם הודעת מערכת שעובדת בפעם הראשונה עבור מקרה השימוש המלא שלכם. היכולת לבצע התאמות ושיפורים קטנים על ידי שינוי הודעת המערכת הבסיסית והרצתה דרך המערכת תאפשר לכם להשוות ולהעריך תוצאות.

## הבנת איומים

כדי לבנות סוכני AI אמינים, חשוב להבין ולהפחית את הסיכונים והאיומים לסוכן ה-AI שלכם. נבחן רק כמה מן האיומים השונים לסוכני AI וכיצד תוכלו לתכנן ולהיערך טוב יותר אליהם.

![Understanding Threats](../../../translated_images/he/understanding-threats.89edeada8a97fc0f.webp)

### משימה והוראות

**תיאור:** תוקפים מנסים לשנות את ההוראות או היעדים של סוכן ה-AI באמצעות קלטים או מניפולציות.

**הפחתה**: בצעו בדיקות אימות וסינונים של הקלטים כדי לזהות קלטים מסוכנים לפני שהסוכן מעבד אותם. מאחר שתקיפות אלו דורשות לרוב אינטראקציה תכופה עם הסוכן, הגבלת מספר הסבבים בשיחה היא דרך נוספת למנוע התקפות מסוג זה.

### גישה למערכות קריטיות

**תיאור**: אם לסוכן ה-AI יש גישה למערכות ולשירותים שמאחסנים נתונים רגישים, תוקפים עלולים לפגוע בתקשורת בין הסוכן לשירותים אלו. זו יכולה להיות תקיפה ישירה או ניסיון עקיף לקבל מידע על מערכות אלו דרך הסוכן.

**הפחתה**: לסוכני AI יש לאפשר גישה למערכות רק לפי צורך כדי למנוע התקפות מסוג זה. התקשורת בין הסוכן למערכת צריכה להיות מאובטחת. יישום אימות ובקרת גישה הוא דרך נוספת להגן על מידע זה.

### עומס יתר על משאבים ושירותים

**תיאור**: סוכני AI יכולים לגשת לכלים ושירותים שונים להשלמת משימות. תוקפים עלולים לנצל יכולת זו כדי לתקוף את השירותים על ידי שליחת נפח גבוה של בקשות דרך סוכן ה-AI, מה שעשוי לגרום לכשלי מערכת או עלויות גבוהות.

**הפחתה**: יישמו מדיניות להגבלת מספר הבקשות שסוכן AI יכול לבצע לשירות. הגבלת מספר הסבבים והבקשות לסוכן היא דרך נוספת למנוע התקפות מסוג זה.

### הרעלת בסיס ידע

**תיאור**: סוג תקיפה זה אינו מכוון ישירות לסוכן ה-AI אלא לבסיס הידע ולשירותים אחרים שהסוכן ישתמש בהם. זה עשוי לכלול פגיעה בנתונים או במידע שהסוכן ייעזר בו להשלמת משימה, מה שיוביל לתגובות מוטות או לא מכוונות למשתמש.

**הפחתה**: בצעו אימות תקופתי של הנתונים שבהם הסוכן משתמש בזרימות העבודה שלו. ודאו שהגישה לנתונים אלו מאובטחת ומשתנה רק על ידי אנשים מהימנים כדי להימנע מסוג זה של תקיפה.

### שגיאות מתגלגלות

**תיאור**: סוכני AI ניגשים לכלים ושירותים שונים להשלמת משימות. שגיאות שנגרמות על ידי תוקפים עלולות לגרום לכשלים במערכות אחרות שהסוכן מחובר אליהן, מה שמרחיב את ההתקפה ומקשה על איתור התקלות.

**הפחתה**: שיטה למניעת זאת היא שהסוכן יפעל בסביבה מוגבלת, כמו ביצוע משימות בתוך מיכל Docker, כדי למנוע התקפות ישירות על המערכת. יצירת מנגנוני גיבוי ולוגיקת ניסיון חוזר בעת תגובה בשגיאה ממערכת מסוימת היא דרך נוספת למנוע כשלים מערכתיים גדולים יותר.

## אדם בתהליך (Human-in-the-Loop)

דרך אפקטיבית נוספת לבנות מערכות סוכני AI אמינים היא שימוש באדם בתהליך. זה יוצר זרימה שבה משתמשים יכולים לספק משוב לסוכנים במהלך ההרצה. המשתמשים למעשה פועלים כסוכנים במערכת רב-סוכנית ומספקים אישור או הפסקת התהליך הרציף.

![Human in The Loop](../../../translated_images/he/human-in-the-loop.5f0068a678f62f4f.webp)

להלן קוד הממחיש שימוש במסגרת Microsoft Agent להדגים כיצד מושג זה מיושם:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# צור את הספק עם אישור אנושי בתהליך
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# צור את הסוכן עם שלב אישור אנושי
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# המשתמש יכול לסקור ולאשר את התגובה
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## סיכום

בניית סוכני AI אמינים דורשת תכנון קפדני, אמצעי אבטחה חזקים וחזרה מתמשכת. באמצעות יישום מערכות מטא קלט מובנות, הבנת איומים פוטנציאליים והפעלת אסטרטגיות הפחתה, מפתחים יכולים ליצור סוכני AI בטוחים ויעילים. בנוסף, שילוב גישת אדם בתהליך מבטיח שהסוכנים יישארו מיושרים עם צרכי המשתמש תוך הפחתת סיכונים. ככל שה-AI ממשיך להתפתח, שמירה על גישה פרואקטיבית בנושאי אבטחה, פרטיות ושיקולים אתיים תהיה מפתח לטיפוח אמון ואמינות במערכות מונעות AI.

## דוגמאות קוד

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): הדגמה שלב אחר שלב של מסגרת הודעות המטא.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): שערי אישור מקדימים, דירוג סיכונים ורישום ביקורת לסוכנים אמינים.

### יש לך שאלות נוספות על בניית סוכני AI אמינים?

הצטרפו ל-[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) לפגוש לומדים נוספים, להשתתף בשעות משרדים ולקבל מענה לשאלות בנוגע לסוכני AI.

## משאבים נוספים

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">סקירת AI אחראי</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">הערכת דגמי AI גנרטיביים ויישומי AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">הודעות מערכת בטיחות</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">תבנית הערכת סיכונים</a>

## שיעור קודם

[Agentic RAG](../05-agentic-rag/README.md)

## שיעור הבא

[תבנית תכנון](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->