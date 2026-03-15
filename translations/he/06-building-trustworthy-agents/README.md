[![סוכני AI אמינים](../../../translated_images/he/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(לחצו על התמונה למעלה כדי לצפות בסרטון של השיעור הזה)_

# בניית סוכני AI אמינים

## מבוא

בשיעור זה נכסה:

- כיצד לבנות ולפרוס סוכני AI בטוחים ויעילים
- שיקולי אבטחה חשובים בעת פיתוח סוכני AI.
- כיצד לשמור על פרטיות הנתונים והמשתמש בעת פיתוח סוכני AI.

## מטרות למידה

בסיום השיעור תדעו כיצד:

- לזהות ולהפחית סיכונים בעת יצירת סוכני AI.
- ליישם אמצעי אבטחה כדי להבטיח שהנתונים והגישה מנוהלים כראוי.
- ליצור סוכני AI שמשמרים את פרטיות הנתונים ומספקים חוויית משתמש איכותית.

## בטיחות

נבחן קודם את בניית יישומים סוכניים בטוחים. בטיחות פירושה שהסוכן מבצע את פעולותיו כפי שתוכנן. כבוני יישומים סוכניים, יש לנו שיטות וכלים למקסום הבטיחות:

### בניית מסגרת הודעת מערכת

אם אי פעם בניתם יישום AI שמבוסס על מודלים שפתיים גדולים (LLMs), אתם מבינים את החשיבות של עיצוב הנחיית מערכת חזקה או הודעת מערכת. הנחיות אלו קובעות את הכללים המטא, ההוראות וההנחיות לאופן שבו ה-LLM יתקשר עם המשתמש והנתונים.

עבור סוכני AI, הנחיית המערכת חשובה אפילו יותר כי הסוכנים יזדקקו להוראות מאוד ספציפיות כדי להשלים את המשימות שעיצבנו עבורם.

כדי ליצור הנחיות מערכת שניתנות להרחבה, אנו יכולים להשתמש במסגרת הודעת מערכת לבניית סוכן אחד או יותר ביישום שלנו:

![בניית מסגרת הודעת מערכת](../../../translated_images/he/system-message-framework.3a97368c92d11d68.webp)

#### שלב 1: יצירת הודעת מערכת מטא 

ההנחיה המטא תשמש את ה-LLM ליצירת הנחיות מערכת עבור הסוכנים שאנחנו יוצרים. אנו מעצבים אותה כתבנית כדי שנוכל ליצור מספר סוכנים ביעילות במידת הצורך.

להלן דוגמה להודעת מערכת מטא שנעניק ל-LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### שלב 2: יצירת הנחיה בסיסית

השלב הבא הוא ליצור הנחיה בסיסית לתיאור סוכן ה-AI. עליכם לכלול את תפקיד הסוכן, המשימות שהסוכן ישלים, וכל אחריות נוספת של הסוכן.

הנה דוגמה:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### שלב 3: ספק הודעת מערכת בסיסית ל-LLM

כעת נוכל לייעל הודעת מערכת זו על ידי סיפוק הודעת המערכת המטא כהודעת מערכת יחד עם הודעת המערכת הבסיסית שלנו.

זה יפיק הודעת מערכת שתהיה מעוצבת טוב יותר להנחיית סוכני ה-AI שלנו:

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

#### שלב 4: חזור ושפר

ערך מסגרת הודעת המערכת הזו הוא בכך שהיא מאפשרת להרחיב את יצירת הודעות מערכת עבור מספר סוכנים בקלות וכן לשפר את הודעות המערכת שלכם עם הזמן. נדיר שיהיה לכם הודעת מערכת שעובדת בפעם הראשונה עבור כל מקרה השימוש. היכולת לבצע שינויים קטנים ושיפורים על ידי שינוי הודעת המערכת הבסיסית והרצתה דרך המערכת תאפשר לכם להשוות ולהעריך תוצאות.

## הבנת איומים

כדי לבנות סוכני AI אמינים, חשוב להבין ולהפחית את הסיכונים והאיומים נגד הסוכן שלכם. נסקור כמה מהאיומים השונים כלפי סוכני AI וכיצד תוכלו לתכנן ולהתכונן אליהם בצורה טובה יותר.

![הבנת איומים](../../../translated_images/he/understanding-threats.89edeada8a97fc0f.webp)

### משימה והנחיה

**תיאור:** תוקפים מנסים לשנות את ההוראות או המטרות של סוכן ה-AI באמצעות הנחיה או מניפולציה של הקלטים.

**הפחתה**: הריצו בדיקות אימות ומסנני קלט כדי לזהות הנחיות שעלולות להיות מסוכנות לפני שהן מעובדות על ידי סוכן ה-AI. מכיוון שתקיפות אלו בדרך כלל דורשות אינטראקציות תכופות עם הסוכן, הגבלת מספר הסבבים בשיחה היא דרך נוספת למנוע סוגי תקיפות אלה.

### גישה למערכות קריטיות

**תיאור**: אם לסוכן AI יש גישה למערכות ושירותים המאחסנים נתונים רגישים, תוקפים יכולים להפריע או לפגוע בתקשורת בין הסוכן לשירותים אלה. אלו יכולות להיות תקיפות ישירות או ניסיונות עקיפים להשיג מידע על מערכות אלה דרך הסוכן.

**הפחתה**: יש להעניק לסוכני AI גישה למערכות רק על בסיס צורך בלבד כדי למנוע סוגי תקיפות אלה. גם התקשורת בין הסוכן למערכת צריכה להיות מאובטחת. יישום אימות ושליטה בגישה הוא דרך נוספת להגן על מידע זה.

### הצפה של משאבים ושירותים

**תיאור:** סוכני AI יכולים לגשת לכלים ושירותים שונים כדי להשלים משימות. תוקפים יכולים להשתמש ביכולת זו כדי לתקוף שירותים אלה על ידי שליחת נפח גבוה של בקשות דרך סוכן ה-AI, מה שעשוי לגרום לקריסות מערכת או לעלויות גבוהות.

**הפחתה:** יש להטמיע מדיניות להגבלת מספר הבקשות שסוכן AI יכול לבצע לשירות. הגבלת מספר הסבבים בשיחה ובקשות לסוכן ה-AI היא דרך נוספת למנוע סוגי תקיפות אלה.

### הרעלת מאגר הידע

**תיאור:** סוג תקיפה זה לא פוגעת בסוכן ה-AI ישירות אלא פוגעת במאגר הידע ובשירותים אחרים שהסוכן ישתמש בהם. זה יכול לכלול השחתת הנתונים או המידע שהסוכן ישתמש בו להשלמת משימה, מה שיכול להוביל לתגובות מוטות או בלתי מכוונות כלפי המשתמש.

**הפחתה:** בצעו אימות קבוע של הנתונים שהסוכן ישתמש בהם במהלך זרימות העבודה שלו. הבטיחו שהגישה לנתונים אלה מאובטחת וששינויים יבוצעו רק על ידי אנשים מהימנים כדי להימנע מסוג תקיפה זה.

### שגיאות מצטברות

**תיאור:** סוכני AI ניגשים לכלים ושירותים שונים כדי להשלים משימות. שגיאות שנגרמות על ידי תוקפים יכולות להוביל לכשלים במערכות נוספות שאליהן הסוכן מחובר, מה שהופך את התקיפה לנרחבת יותר וקשה יותר לאבחון.

**הפחתה**: אחת הדרכים להימנע מכך היא להפעיל את סוכן ה-AI בסביבה מוגבלת, למשל ביצוע משימות בתוך Docker container, כדי למנוע תקיפות ישירות על המערכת. יצירת מנגנוני גיבוי ולוגיקת ניסיון מחודשת כאשר מערכות מסוימות משיבות בשגיאה היא דרך נוספת למנוע כשלים מערכתיים גדולים יותר.

## אדם בלולאה

דרך נוספת ויעילה לבניית מערכות סוכני AI מהימנות היא שימוש בגישה של אדם בלולאה. זה יוצר זרימה שבה משתמשים יכולים לספק משוב לסוכנים במהלך הריצה. המשתמשים למעשה פועלים כסוכנים במערכת מרובת סוכנים ובאמצעות מתן אישור או עצירת התהליך הרץ.

![אדם בלולאה](../../../translated_images/he/human-in-the-loop.5f0068a678f62f4f.webp)

להלן קטע קוד המשתמש ב-Microsoft Agent Framework כדי להדגים כיצד מושג זה מיושם:

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

# המשתמש יכול לעיין ולאשר את התגובה
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## מסקנה

בניית סוכני AI אמינים דורשת תכנון זהיר, אמצעי אבטחה חזקים וחזרה מתמדת. באמצעות יישום מערכות הנחיה מטא מובנות, הבנת האיומים הפוטנציאליים ויישום אסטרטגיות הפחתה, מפתחים יכולים ליצור סוכני AI שיהיו גם בטוחים וגם יעילים. בנוסף, שילוב גישת אדם בלולאה מבטיח שהסוכנים יישארו מיושרים עם צרכי המשתמש תוך הפחתת סיכונים. ככל ש-AI יתפתח, שמירה על גישה יזומה בנושאי אבטחה, פרטיות ושיקולים אתיים תהיה חיונית לטיפוח אמון ואמינות במערכות מונעות AI.

### יש לכם שאלות נוספות על בניית סוכני AI אמינים?

הצטרפו ל-[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) כדי לפגוש לומדים אחרים, להשתתף בשעות ייעוץ ולקבל תשובות לשאלות על סוכני ה-AI שלכם.

## משאבים נוספים

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">סקירה על שימוש אחראי ב-AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">הערכת מודלים גנרטיביים של AI ויישומי AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">הודעות מערכת לבטיחות</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">תבנית הערכת סיכונים</a>

## שיעור קודם

[RAG סוכני](../05-agentic-rag/README.md)

## השיעור הבא

[תבנית עיצוב לתכנון](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**הצהרת אי-אחריות**:
מסמך זה תורגם בעזרת שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). אמנם אנו שואפים לדיוק, אך יש לדעת שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו כמקור הסמכות. למידע קריטי מומלץ להיעזר בתרגום מקצועי על ידי מתרגם אנושי. איננו אחראים לכל אי-הבנה או לפרשנות שגויה הנובעים משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->