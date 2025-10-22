<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T17:37:57+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "he"
}
-->
[![סוכני AI אמינים](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.he.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(לחצו על התמונה למעלה לצפייה בסרטון של השיעור הזה)_

# בניית סוכני AI אמינים

## הקדמה

בשיעור זה נעסוק ב:

- כיצד לבנות ולפרוס סוכני AI בטוחים ויעילים.
- שיקולי אבטחה חשובים בעת פיתוח סוכני AI.
- כיצד לשמור על פרטיות נתונים ומשתמשים בעת פיתוח סוכני AI.

## מטרות למידה

לאחר השלמת השיעור, תדעו כיצד:

- לזהות ולהפחית סיכונים בעת יצירת סוכני AI.
- ליישם אמצעי אבטחה כדי להבטיח ניהול נכון של נתונים וגישה.
- ליצור סוכני AI ששומרים על פרטיות נתונים ומספקים חוויית משתמש איכותית.

## בטיחות

נתחיל בבניית יישומים סוכניים בטוחים. בטיחות פירושה שהסוכן מבצע את הפעולות כפי שתוכנן. כמי שבונים יישומים סוכניים, יש לנו שיטות וכלים למקסם את הבטיחות:

### בניית מסגרת הודעות מערכת

אם אי פעם בניתם יישום AI באמצעות מודלים שפתיים גדולים (LLMs), אתם יודעים את החשיבות של עיצוב הנחיית מערכת חזקה או הודעת מערכת. הנחיות אלו קובעות את הכללים, ההוראות וההנחיות לממשק של ה-LLM עם המשתמש והנתונים.

עבור סוכני AI, הנחיית המערכת חשובה אף יותר, שכן הסוכנים זקוקים להוראות מאוד ספציפיות כדי להשלים את המשימות שתוכננו עבורם.

כדי ליצור הנחיות מערכת בקנה מידה, ניתן להשתמש במסגרת הודעות מערכת לבניית סוכן אחד או יותר ביישום שלנו:

![בניית מסגרת הודעות מערכת](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.he.png)

#### שלב 1: יצירת הודעת מערכת מטא

הנחיית המטא תשמש את ה-LLM ליצירת הנחיות מערכת עבור הסוכנים שאנחנו יוצרים. אנו מעצבים אותה כתבנית כך שנוכל ליצור סוכנים מרובים ביעילות אם יש צורך.

להלן דוגמה להודעת מערכת מטא שניתן לתת ל-LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### שלב 2: יצירת הנחיה בסיסית

השלב הבא הוא ליצור הנחיה בסיסית שמתארת את סוכן ה-AI. יש לכלול את תפקיד הסוכן, המשימות שהסוכן יבצע וכל אחריות נוספת של הסוכן.

להלן דוגמה:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### שלב 3: מתן הודעת מערכת בסיסית ל-LLM

כעת ניתן לייעל את הודעת המערכת על ידי מתן הודעת המטא כהודעת מערכת והודעת המערכת הבסיסית שלנו.

זה יפיק הודעת מערכת שמתוכננת טוב יותר להנחות את סוכני ה-AI שלנו:

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

#### שלב 4: איטרציה ושיפור

הערך של מסגרת הודעות המערכת הוא היכולת להקל על יצירת הודעות מערכת עבור סוכנים מרובים וכן לשפר את הודעות המערכת לאורך זמן. נדיר שתהיה הודעת מערכת שעובדת בפעם הראשונה עבור כל מקרי השימוש שלכם. היכולת לבצע שינויים קטנים ושיפורים על ידי שינוי הודעת המערכת הבסיסית והרצתה דרך המערכת תאפשר לכם להשוות ולהעריך תוצאות.

## הבנת איומים

כדי לבנות סוכני AI אמינים, חשוב להבין ולהפחית את הסיכונים והאיומים על הסוכן. בואו נבחן כמה מהאיומים השונים על סוכני AI וכיצד ניתן לתכנן ולהתכונן אליהם טוב יותר.

![הבנת איומים](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.he.png)

### משימות והוראות

**תיאור:** תוקפים מנסים לשנות את ההוראות או המטרות של סוכן ה-AI באמצעות הנחיות או מניפולציה של קלטים.

**הפחתה:** בצעו בדיקות אימות ומסנני קלט כדי לזהות הנחיות מסוכנות פוטנציאליות לפני שהן מעובדות על ידי סוכן ה-AI. מכיוון שהתקפות אלו דורשות בדרך כלל אינטראקציה תכופה עם הסוכן, הגבלת מספר הפניות בשיחה היא דרך נוספת למנוע סוגי התקפות אלו.

### גישה למערכות קריטיות

**תיאור:** אם לסוכן AI יש גישה למערכות ושירותים שמאחסנים נתונים רגישים, תוקפים יכולים לפגוע בתקשורת בין הסוכן לשירותים אלו. אלו יכולים להיות התקפות ישירות או ניסיונות עקיפים להשיג מידע על מערכות אלו דרך הסוכן.

**הפחתה:** סוכני AI צריכים לקבל גישה למערכות רק על בסיס צורך בלבד כדי למנוע סוגי התקפות אלו. התקשורת בין הסוכן למערכת צריכה להיות מאובטחת. יישום אימות ובקרת גישה הוא דרך נוספת להגן על מידע זה.

### עומס יתר על משאבים ושירותים

**תיאור:** סוכני AI יכולים לגשת לכלים ושירותים שונים כדי להשלים משימות. תוקפים יכולים להשתמש ביכולת זו כדי לתקוף את השירותים הללו על ידי שליחת כמות גדולה של בקשות דרך סוכן ה-AI, מה שעלול לגרום לכשלים במערכת או עלויות גבוהות.

**הפחתה:** יישמו מדיניות להגבלת מספר הבקשות שסוכן AI יכול לבצע לשירות. הגבלת מספר הפניות והבקשות לסוכן ה-AI היא דרך נוספת למנוע סוגי התקפות אלו.

### הרעלת בסיס ידע

**תיאור:** סוג זה של התקפה אינו מכוון ישירות לסוכן ה-AI אלא לבסיס הידע ושירותים אחרים שהסוכן ישתמש בהם. זה יכול לכלול השחתת נתונים או מידע שהסוכן ישתמש בהם כדי להשלים משימה, מה שיוביל לתגובות מוטות או לא מכוונות למשתמש.

**הפחתה:** בצעו אימות קבוע של הנתונים שהסוכן ישתמש בהם בתהליכי העבודה שלו. ודאו שהגישה לנתונים אלו מאובטחת ומשתנה רק על ידי אנשים מהימנים כדי להימנע מסוג התקפה זה.

### שגיאות מתגלגלות

**תיאור:** סוכני AI ניגשים לכלים ושירותים שונים כדי להשלים משימות. שגיאות שנגרמות על ידי תוקפים יכולות להוביל לכשלים במערכות אחרות שהסוכן מחובר אליהן, מה שגורם להתקפה להפוך לנרחבת יותר וקשה יותר לפתרון.

**הפחתה:** אחת הדרכים להימנע מכך היא לגרום לסוכן ה-AI לפעול בסביבה מוגבלת, כמו ביצוע משימות במיכל Docker, כדי למנוע התקפות ישירות על המערכת. יצירת מנגנוני גיבוי ולוגיקת ניסיון חוזר כאשר מערכות מסוימות מגיבות עם שגיאה היא דרך נוספת למנוע כשלים מערכתיים גדולים יותר.

## אדם בתהליך

דרך יעילה נוספת לבנות מערכות סוכני AI אמינות היא שימוש במעורבות אדם בתהליך. זה יוצר זרימה שבה משתמשים יכולים לספק משוב לסוכנים במהלך הריצה. משתמשים למעשה פועלים כסוכנים במערכת רב-סוכנים על ידי מתן אישור או הפסקת התהליך.

![אדם בתהליך](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.he.png)

להלן קטע קוד שמשתמש ב-AutoGen כדי להראות כיצד מושג זה מיושם:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## סיכום

בניית סוכני AI אמינים דורשת עיצוב קפדני, אמצעי אבטחה חזקים ואיטרציה מתמשכת. על ידי יישום מערכות הנחיה מטא מובנות, הבנת איומים פוטנציאליים ויישום אסטרטגיות הפחתה, מפתחים יכולים ליצור סוכני AI בטוחים ויעילים. בנוסף, שילוב גישה של אדם בתהליך מבטיח שסוכני AI יישארו מותאמים לצרכי המשתמש תוך מזעור סיכונים. ככל שה-AI ממשיך להתפתח, שמירה על גישה פרואקטיבית בנוגע לאבטחה, פרטיות ושיקולים אתיים תהיה המפתח לטיפוח אמון ואמינות במערכות מבוססות AI.

### יש לכם עוד שאלות על בניית סוכני AI אמינים?

הצטרפו ל-[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) כדי לפגוש לומדים אחרים, להשתתף בשעות קבלה ולקבל תשובות לשאלות שלכם על סוכני AI.

## משאבים נוספים

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">סקירה של AI אחראי</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">הערכת מודלים של AI גנרטיבי ויישומי AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">הודעות מערכת בטיחות</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">תבנית הערכת סיכונים</a>

## שיעור קודם

[Agentic RAG](../05-agentic-rag/README.md)

## שיעור הבא

[תבנית עיצוב תכנון](../07-planning-design/README.md)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.