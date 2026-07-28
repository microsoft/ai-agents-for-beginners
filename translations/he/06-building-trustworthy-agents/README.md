[![סוכני AI אמינים](../../../translated_images/he/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(לחצו על התמונה למעלה כדי לצפות בסרטון של השיעור)_

# בניית סוכני AI אמינים

## מבוא

שיעור זה יכסה:

- כיצד לבנות ולפרוס סוכני AI בטוחים ויעילים
- שיקולי אבטחה חשובים בפיתוח סוכני AI.
- כיצד לשמור על פרטיות נתונים ומשתמשים בפיתוח סוכני AI.

## מטרות הלמידה

לאחר שתשלים שיעור זה, תדע כיצד:

- לזהות ולהפחית סיכונים ביצירת סוכני AI.
- ליישם אמצעי אבטחה כדי להבטיח ניהול נכון של נתונים וגישה.
- ליצור סוכני AI ששומרים על פרטיות הנתונים ומספקים חווית משתמש איכותית.

## בטיחות

נתחיל מלהסתכל על בניית אפליקציות סוכניות בטוחות. בטיחות משמעותה שהסוכן האינטליגנציה המלאכותית מבצע כפי שתוכנן. כבוני אפליקציות סוכניות, יש לנו שיטות וכלים למקסם את הבטיחות:

### בניית מסגרת הודעת מערכת

אם אי פעם בניתם אפליקציית AI באמצעות מודלים שפתיים גדולים (LLMs), אתם יודעים את חשיבות עיצוב הנחיית מערכת יציבה או הודעת מערכת. הנחיות אלו קובעות את הכללים המטא, ההוראות וההנחיות לאופן שבו ה-LLM יתקשר עם המשתמש והנתונים.

עבור סוכני AI, הנחיית המערכת חשובה אף יותר שכן הסוכנים יצטרכו הוראות מאוד ספציפיות כדי להשלים את המשימות שתכננו עבורם.

כדי ליצור הנחיות מערכת ניתנות להרחבה, נוכל להשתמש במסגרת הודעת מערכת לבניית סוכן או יותר באפליקציה שלנו:

![בניית מסגרת הודעת מערכת](../../../translated_images/he/system-message-framework.3a97368c92d11d68.webp)

#### שלב 1: יצירת הודעת מערכת מטא

ההנחיה המטא תשמש את ה-LLM כדי ליצור את הנחיות המערכת עבור הסוכנים שניצור. אנו מעצבים אותה כתבנית כדי שנוכל לייצר מספר סוכנים ביעילות במידת הצורך.

הנה דוגמה להודעת מערכת מטא שניתן ל-LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### שלב 2: יצירת הנחיה בסיסית

השלב הבא הוא ליצור הנחיה בסיסית שמתארת את סוכן ה-AI. יש לכלול את תפקיד הסוכן, המשימות שהסוכן ימלא וכל אחריות אחרת של הסוכן.

הנה דוגמה:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### שלב 3: מתן הודעת מערכת בסיסית ל-LLM

כעת נוכל לאופטימיז את הודעת המערכת על ידי מתן הודעת המערכת המטא והודעת המערכת הבסיסית שלנו.

זה יפיק הודעת מערכת שתוכננה טוב יותר להנחות את סוכני ה-AI שלנו:

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

#### שלב 4: חזרה ושיפור

הערך של מסגרת הודעת המערכת הזו הוא ביכולת להרחיב בקלות יצירת הודעות מערכת מרובות סוכנים וגם לשפר את הודעות המערכת שלך לאורך זמן. נדיר שיהיה לך הודעת מערכת שעובדת במלואה בפעם הראשונה למקרה השימוש שלך. היכולת לבצע שינויים קלים ושיפורים על ידי שינוי הודעת המערכת הבסיסית והרצתה במערכת תאפשר השוואה והערכה של תוצאות.

## הבנת איומים

כדי לבנות סוכני AI אמינים חשוב להבין ולהפחית סיכונים ואיומים כלפי סוכן ה-AI שלך. נבחן רק חלק מהאיומים השונים לסוכני AI וכיצד ניתן לתכנן ולהתכונן טוב יותר אליהם.

![הבנת איומים](../../../translated_images/he/understanding-threats.89edeada8a97fc0f.webp)

### משימה והנחיה

**תיאור:** תוקפים מנסים לשנות את ההנחיות או יעדי סוכן ה-AI באמצעות הנחיה או מניפולציה של קלטים.

**הפחתה**: יש לבצע בדיקות אימות ומסנני קלט לאיתור הנחיות פוטנציאליות מסוכנות לפני שהסוכן מעבד אותן. מאחר שתקיפות כאלה דורשות אינטראקציה תכופה עם הסוכן, הגבלת מספר סבבי שיחה היא דרך נוספת למנוע סוג זה של התקפות.

### גישה למערכות קריטיות

**תיאור:** אם לסוכן AI יש גישה למערכות ושירותים המאחסנים נתונים רגישים, תוקפים עלולים לפגוע בתקשורת בין הסוכן לשירותים אלו. אלו יכולים להיות התקפות ישירות או ניסיונות עקיפים להשיג מידע על מערכות אלו דרך הסוכן.

**הפחתה**: לסוכני AI יש לאפשר גישה למערכות רק על בסיס הצורך כדי למנוע התקפות מסוג זה. התקשורת בין הסוכן למערכת גם צריכה להיות מאובטחת. יישום אימות ושליטה בגישה הם דרכים נוספות להגן על מידע זה.

### עומס יתר על משאבים ושירותים

**תיאור:** סוכני AI יכולים לגשת לכלים ושירותים שונים כדי להשלים משימות. תוקפים יכולים לנצל יכולת זו כדי לתקוף שירותים אלה על ידי שליחת נפח גבוה של בקשות דרך סוכן ה-AI, מה שעלול לגרום לכשלי מערכת או לעלויות גבוהות.

**הפחתה:** יש ליישם מדיניות להגבלת מספר הבקשות שסוכן AI יכול לעשות לשירות. הגבלת מספר סבבי שיחה ובקשות לסוכן ה-AI שלך היא דרך נוספת למנוע מתקפות מסוג זה.

### הרעלת בסיס ידע

**תיאור:** סוג זה של התקפה אינו פוגע ישירות בסוכן ה-AI אלא בבסיס הידע ובשירותים אחרים שהסוכן ישתמש בהם. זה יכול לכלול זיהום הנתונים או המידע שהסוכן ישתמש בהם להשלים משימה, מה שעלול להוביל לתגובות מוטות או לא רצויות למשתמש.

**הפחתה:** יש לבצע אימות סדיר של הנתונים שהסוכן ישתמש בהם במהלך העבודה. להבטיח שהגישה למידע זה תהיה מאובטחת ורק אנשים מהימנים ישנו את הנתונים כדי למנוע התקפה מסוג זה.

### טעויות מפושטות

**תיאור:** סוכני AI ניגשים לכלים ולשירותים שונים להשלים משימות. שגיאות הנגרמות על ידי תוקפים עלולות לגרום לכשלי מערכות אחרות שאליהן הסוכן מחובר, מה שהופך את ההתקפה לנרחבת וקשה יותר לאיתור ותיקון.

**הפחתה**: דרך למנוע זאת היא לגרום לסוכן ה-AI לפעול בסביבה מוגבלת, כגון ביצוע משימות במכולת Docker, כדי למנוע התקפות ישירות על המערכת. יצירת מנגנוני גיבוי ולוגיקה לחזרה כאשר מערכות מסוימות מגיבות בשגיאה היא דרך נוספת למנוע כשלי מערכת גדולים יותר.

## אדם בתווך (Human-in-the-Loop)

דרך יעילה נוספת לבנות מערכות סוכני AI אמינים היא שימוש באדם בתווך. זה יוצר זרימה שבה משתמשים יכולים לספק משוב לסוכנים במהלך הריצה. המשתמשים מתפקדים למעשה כסוכנים במערכת רב-סוכנית על ידי מתן אישור או סיום התהליך הרץ.

![אדם בתווך](../../../translated_images/he/human-in-the-loop.5f0068a678f62f4f.webp)

הנה קטע קוד המשתמש במסגרת Microsoft Agent להדגים כיצד מושג זה מיושם:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# צור את הספק עם אישור של אדם בתהליך
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# צור את הסוכן עם שלב אישור אנושי
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# המשתמש יכול לבדוק ולאשר את התגובה
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## סיכום

בניית סוכני AI אמינים דורשת עיצוב זהיר, אמצעי אבטחה חזקים וחזרה מתמשכת. על ידי יישום מערכות הנחיות מטא מובנות, הבנת איומים פוטנציאליים, ויישום אסטרטגיות הפחתה, מפתחים יכולים ליצור סוכני AI שהם גם בטוחים וגם יעילים. בנוסף, שילוב גישת אדם בתווך מבטיח שהסוכנים יישארו תואמים לצרכי המשתמשים תוך הקטנת סיכונים. ככל שה-AI ממשיך להתפתח, שמירה על גישה פרואקטיבית באבטחה, פרטיות ושיקולים אתיים תהיה המפתח לטיפוח אמון ואמינות במערכות מונעות AI.

## דוגמאות קוד

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): הדגמה שלב אחר שלב של מסגרת הודעת מערכת מטא.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): שערי אישור לפני פעולה, דירוג סיכונים, ויומן ביקורת לסוכנים אמינים.

### יש לך עוד שאלות על בניית סוכני AI אמינים?

הצטרף ל-[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) כדי לפגוש לומדים אחרים, להשתתף בשעות קבלה ולקבל מענה לשאלות על סוכני AI.

## משאבים נוספים

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">סקירה כללית על AI אחראי</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">הערכת מודלים של AI מחולל ויישומי AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">הודעות מערכת לבטיחות</a>
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