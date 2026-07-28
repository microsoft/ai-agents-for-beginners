[![חקירת מסגרות סוכני AI](../../../translated_images/he/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(לחץ על התמונה למעלה כדי לצפות בסרטון של השיעור)_

# חקור מסגרות סוכני AI

מסגרות סוכני AI הן פלטפורמות תוכנה שמטרתן לפשט את יצירת, פריסת וניהול סוכני AI. מסגרות אלו מספקות למפתחים רכיבים מוכנים, אבסטראקציות, וכלים שמייעלים את פיתוח מערכות AI מורכבות.

מסגרות אלה עוזרות למפתחים להתמקד בהיבטים הייחודיים של היישומים שלהם על ידי מתן גישות סטנדרטיות לאתגרים נפוצים בפיתוח סוכני AI. הן משפרות את היתכנות ההרחבה, הנגישות, והיעילות בבניית מערכות AI.

## מבוא 

שיעור זה יכסה:

- מהן מסגרות סוכני AI ומה הן מאפשרות למפתחים להשיג?
- כיצד צוותים יכולים להשתמש בהן כדי ליצור אבטיפוס, לבצע איטרציה ולשפר במהירות את יכולות הסוכן שלהם?
- מהם ההבדלים בין המסגרות והכלים שנוצרו על ידי מיקרוסופט (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> ו-<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- האם ניתן לשלב את כלים קיימים מאקוסיסטם Azure ישירות, או שיש צורך בפתרונות עצמאיים?
- מהו שירות Microsoft Foundry Agent וכיצד הוא עוזר לי?

## מטרות למידה

מטרות השיעור הן לעזור לך להבין:

- תפקיד מסגרות סוכני AI בפיתוח AI.
- כיצד לנצל את מסגרות סוכני AI לבניית סוכנים אינטליגנטיים.
- יכולות מפתח שמסגרות סוכני AI מאפשרות.
- ההבדלים בין Microsoft Agent Framework לבין Microsoft Foundry Agent Service.

## מהן מסגרות סוכני AI ומה הן מאפשרות למפתחים לעשות?

מסגרות AI מסורתיות יכולות לעזור לך לשלב AI באפליקציות שלך ולשפר אותן בדרכים הבאות:

- **התאמה אישית**: AI יכול לנתח התנהגות והעדפות משתמש כדי לספק המלצות, תוכן וחוויות מותאמות אישית.
דוגמה: שירותי סטרימינג כמו Netflix משתמשים ב-AI כדי להציע סרטים ותכניות בהתאם להיסטוריית הצפייה, מה שמשפר מעורבות וסיפוק המשתמשים.
- **אוטומציה ויעילות**: AI יכול לבצע אוטומציה של משימות חוזרות, לייעל תהליכים ולשפר את היעילות התפעולית.
דוגמה: אפליקציות שירות לקוחות משמשות בבוטים מבוססי AI לטיפול בפניות שכיחות, מה שמקצר זמני תגובה ומשחרר סוכנים אנושיים למשימות מורכבות יותר.
- **שיפור חווית המשתמש**: AI יכול לשפר את חווית המשתמש הכוללת באמצעות מאפיינים אינטליגנטיים כמו זיהוי קולי, עיבוד שפה טבעית וטקסט חיזוי.
דוגמה: עוזרים וירטואליים כמו Siri ו-Google Assistant משתמשים ב-AI כדי להבין ולהגיב לפקודות קוליות, מה שמקל על המשתמשים באינטראקציה עם המכשירים שלהם.

### כל זה נשמע נהדר, אז למה אנחנו צריכים את מסגרת הסוכן של AI?

מסגרות סוכני AI הן מעבר למסגרות AI רגילות. הן מיועדות לאפשר יצירת סוכנים אינטליגנטיים שיכולים לקיים אינטראקציה עם משתמשים, סוכנים אחרים והסביבה כדי להשיג מטרות ספציפיות. סוכנים אלו יכולים להפגין התנהגות אוטונומית, לקבל החלטות ולהסתגל לתנאים משתנים. בואו נסתכל על כמה יכולות מפתח שמסגרות סוכני AI מאפשרות:

- **שיתופי פעולה ותיאום בין סוכנים**: מאפשרים יצירת סוכנים מרובים שיכולים לעבוד יחד, לתקשר ולתאם לפתרון משימות מורכבות.
- **אוטומציה וניהול משימות**: מספקים מנגנונים לאוטומציה של תהליכים מרובי שלבים, הקצאת משימות וניהול משימות דינמי בין סוכנים.
- **הבנה הקשרית והסתגלות**: מציידים סוכנים ביכולת להבין הקשר, להסתגל לסביבות משתנות ולקבל החלטות בהתבסס על מידע בזמן אמת.

לסיכום, סוכנים מאפשרים לך לעשות יותר, לקחת את האוטומציה לרמה הבאה, ליצור מערכות אינטליגנטיות יותר שיכולות להסתגל וללמוד מהסביבה שלהן.

## כיצד ליצור אבטיפוס, לבצע איטרציה ולשפר במהירות את יכולות הסוכן?

זהו תחום דינמי ומהיר, אך ישנם אלמנטים משותפים ברוב מסגרות סוכני ה-AI שיכולים לעזור לך ליצור אבטיפוס במהירות ולבצע איטרציות, כגון רכיבים מודולריים, כלים שיתופיים ולמידה בזמן אמת. בואו נצלול אליהם:

- **שימוש ברכיבים מודולריים**: ערכות פיתוח SDK מציעות רכיבים מוכנים מראש כמו מחברים ל-AI וזיכרון, קריאת פונקציות באמצעות שפה טבעית או תוספים של קוד, תבניות פקודות ועוד.
- **ניצול כלים שיתופיים**: עיצוב סוכנים עם תפקידים ומשימות ספציפיים, המאפשר להם לבדוק ולשפר זרימות עבודה שיתופיות.
- **למידה בזמן אמת**: יישום לולאות משוב שבהן הסוכנים לומדים מהאינטראקציות ומכיילים את התנהגותם באופן דינמי.

### שימוש ברכיבים מודולריים

ערכות פיתוח כמו Microsoft Agent Framework מציעות רכיבים מוכנים מראש כמו מחברי AI, הגדרות כלים וניהול סוכנים.

**כיצד צוותים יכולים להשתמש בזה**: צוותים יכולים להרכיב במהירות רכיבים אלה ליצירת אבטיפוס פונקציונלי ללא צורך להתחיל מאפס, מה שמאפשר ניסויים ואיטרציות מהירות.

**איך זה עובד בפועל**: ניתן להשתמש בפרסר מוכן מראש כדי לחלץ מידע מקלט המשתמש, במודול זיכרון לאחסון ושליפה, ובגנרטור פקודות לאינטראקציה עם המשתמשים, הכל בלי צורך לבנות את הרכיבים מהיסוד.

**קוד לדוגמה**. בואו נבחן דוגמה של שימוש ב-Microsoft Agent Framework עם `FoundryChatClient` כדי לגרום למודל להגיב לכניסת משתמש באמצעות קריאת כלי:

``` python
# דוגמת פייתון למסגרת Microsoft Agent

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# הגדר פונקציה לדוגמה של כלי להזמנת נסיעות
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # פלט לדוגמה: הטיסה שלך לניו יורק ב-1 בינואר 2025 הוזמנה בהצלחה. נסיעה טובה! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

מה שניתן לראות בדוגמה זו הוא כיצד ניתן לנצל פרסר מוכן מראש לחלץ מידע מרכזי מכניסת המשתמש, כגון מקור, יעד ותאריך בקשת הזמנת טיסות. גישה מודולרית זו מאפשרת להתמקד בלוגיקה ברמת גבוהה.

### ניצול כלים שיתופיים

מסגרות כמו Microsoft Agent Framework מאפשרות יצירת סוכנים מרובים שיכולים לעבוד יחד.

**כיצד צוותים יכולים להשתמש בזה**: צוותים יכולים לעצב סוכנים עם תפקידים ומשימות ספציפיים, כדי לבדוק ולשפר זרימות עבודה שיתופיות ולהגביר את יעילות המערכת הכוללת.

**איך זה עובד בפועל**: ניתן ליצור צוות סוכנים שכל אחד מתמחה בפונקציה אחרת, כגון שליפת נתונים, ניתוח או קבלת החלטות. סוכנים אלה יכולים לתקשר ולשתף מידע כדי להשיג מטרה משותפת, כמו מענה לשאילתת משתמש או השלמת משימה.

**קוד לדוגמה (Microsoft Agent Framework)**:

```python
# יצירת סוכנים מרובים שעובדים יחד באמצעות מסגרת סוכן של מיקרוסופט

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# סוכן שליפת נתונים
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# סוכן ניתוח נתונים
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# הרצת סוכנים ברצף על משימה
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

מה שניתן לראות בקוד הקודם הוא כיצד ליצור משימה המערבת מספר סוכנים שעובדים יחד לניתוח נתונים. כל סוכן מבצע פונקציה ספציפית, והמשימה מתנהלת תוך תיאום הסוכנים להשגת התוצאה הרצויה. על ידי יצירת סוכנים ייעודיים עם תפקידים מיוחדים, ניתן לשפר את יעילות וביצועי המשימה.

### למידה בזמן אמת

מסגרות מתקדמות מספקות יכולות להבנת הקשר בזמן אמת והסתגלות.

**כיצד צוותים יכולים להשתמש בזה**: צוותים יכולים ליישם לולאות משוב שבהן סוכנים לומדים מהאינטראקציות ומכיילים את התנהגותם באופן דינמי, מה שמוביל לשיפור מתמיד ולטיוב היכולות.

**איך זה עובד בפועל**: סוכנים יכולים לנתח משוב ממשתמשים, נתוני סביבה ותוצאות משימות כדי לעדכן את בסיס הידע שלהם, לכייל אלגוריתמים לקבלת החלטות ולשפר ביצועים לאורך זמן. תהליך למידה איטרטיבי זה מאפשר לסוכנים להיערך לתנאים משתנים ולהעדפות המשתמשים, ומגביר את היעילות הכוללת של המערכת.

## מהם ההבדלים בין Microsoft Agent Framework לבין Microsoft Foundry Agent Service?

ישנן דרכים רבות להשוות בין הגישות הללו, אך בואו נבחן כמה הבדלים מרכזיים מבחינת התכנון, היכולות ומקרי השימוש הייעודיים:

## Microsoft Agent Framework (MAF)

מסגרת Microsoft Agent Framework מציעה ערכת SDK פשוטה ליצירת סוכני AI באמצעות `FoundryChatClient`. היא מאפשרת למפתחים ליצור סוכנים שמשתמשים במודלי Azure OpenAI עם קריאת כלים מובנית, ניהול שיחות ואבטחה ברמת ארגון דרך הזדהות Azure.

**מקרי שימוש**: בניית סוכני AI מוכנים לייצור בשימוש בכלים, תהליכים מרובי שלבים ותסריטי אינטגרציה ארגוניים.

הנה כמה מושגים מרכזיים חשובים במסגרת Microsoft Agent Framework:

- **סוכנים**. סוכן נוצר באמצעות `FoundryChatClient` ומוגדר עם שם, הנחיות וכלים. הסוכן יכול:
  - **לעבד הודעות משתמש** ולייצר תגובות באמצעות מודלי Azure OpenAI.
  - **לקרוא כלים** באופן אוטומטי על בסיס הקשר השיחה.
  - **לשמור על מצב השיחה** לאורך אינטראקציות מרובות.

  הנה קטע קוד המדגים כיצד ליצור סוכן:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **כלים**. המסגרת תומכת בהגדרת כלים כפונקציות פייתון שהסוכן יכול להפעיל באופן אוטומטי. הכלים נרשמים בעת יצירת הסוכן:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **תיאום בין סוכנים מרובים**. ניתן ליצור סוכנים מרובים עם התמחות שונה ולתאם את עבודתם:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **אינטגרציה לזיהוי Azure**. המסגרת משתמשת ב-`AzureCliCredential` (או `DefaultAzureCredential`) לאימות מאובטח ללא צורך במפתחות API, מה שמסיר את הצורך בניהול מפתחות ישירות.

## Microsoft Foundry Agent Service

שירות Microsoft Foundry Agent הוא תוספת חדשה יותר, שהוצגה בכנס Microsoft Ignite 2024. הוא מאפשר פיתוח ופריסת סוכני AI עם מודלים גמישים יותר, כמו קריאה ישירה למודלים פתוחים כגון Llama 3, Mistral ו-Cohere.

שירות Microsoft Foundry Agent מספק מנגנוני אבטחה חזקים יותר בדרגת ארגון ושיטות לאחסון נתונים, מה שהופך אותו מתאים ליישומים ארגוניים.

הוא עובד מחוץ לקופסה עם Microsoft Agent Framework לבניית ופריסת סוכנים.

שירות זה נמצא כרגע בבחינת פומבית ותומך בבניית סוכנים עם Python ו-C#.

באמצעות ערכת הפיתוח Python של שירות Microsoft Foundry Agent, ניתן ליצור סוכן עם כלי שהוגדר על ידי המשתמש:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# הגדר פונקציות כלי
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### מושגים מרכזיים

לשירות Microsoft Foundry Agent יש את המושגים המרכזיים הבאים:

- **סוכן**. שירות Microsoft Foundry Agent משתלב עם Microsoft Foundry. בתוך Microsoft Foundry, סוכן AI פועל כמיקרו-שירות "חכם" שיכול לענות על שאלות (RAG), לבצע פעולות, או לאוטומט תהליכי עבודה בעצמו. הוא משיג זאת על ידי שילוב כוחם של מודלים גנרטיביים עם כלים שמאפשרים לו לגשת למקורות נתונים בעולם האמיתי ולתקשר איתם. הנה דוגמה לסוכן:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    בדוגמה זו, סוכן נוצר עם המודל `gpt-4.1-mini`, שם `my-agent` והנחיות `You are helpful agent`. הסוכן מצויד בכלים ומשאבים לביצוע משימות פירוש קוד.

- **שרשור והודעות**. השרשור הוא מושג חשוב נוסף. הוא מייצג שיחה או אינטראקציה בין סוכן למשתמש. שרשורים יכולים לשמש למעקב אחר התקדמות שיחה, אחסון מידע הקשר וניהול מצב האינטראקציה. הנה דוגמה לשרשור:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # בקש מהסוכן לבצע עבודה על השרשור
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # אחזר ותיועד את כל ההודעות כדי לראות את תגובת הסוכן
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    בקוד הקודם, נוצר שרשור. לאחר מכן נשלחה הודעה לשרשור. על ידי קריאה ל-`create_and_process_run`, מבקשים מהסוכן לבצע עבודה בשרשור. בסוף ההודעות נשלפות ומתועדות לצפייה בתגובת הסוכן. ההודעות מציינות את התקדמות השיחה בין המשתמש לסוכן. חשוב גם להבין שההודעות יכולות להיות מסוגים שונים כמו טקסט, תמונה או קובץ, כלומר עבודת הסוכן נבעה לדוגמה בתמונה או במענה טקסטואלי לדוגמה. כמפתחים, אתם יכולים להשתמש במידע זה לעיבוד נוסף של התגובה או להצגתה למשתמש.

- **אינטגרציה עם Microsoft Agent Framework**. שירות Microsoft Foundry Agent פועל בצורה חלקה עם Microsoft Agent Framework, כלומר ניתן לבנות סוכנים באמצעות `FoundryChatClient` ולפרוס אותם באמצעות שירות הסוכנים עבור תרחישי ייצור.

**מקרי שימוש**: שירות Microsoft Foundry Agent מיועד ליישומים ארגוניים שדורשים פריסה מאובטחת, ניתנת להרחבה וגמישה של סוכני AI.

## מה ההבדל בין הגישות הללו?
 
זה נשמע שיש חפיפה, אך ישנם הבדלים מרכזיים בתכנון, ביכולות ובמקרי שימוש ייעודיים:
 
- **Microsoft Agent Framework (MAF)**: ערכת SDK מוכנה לייצור לבניית סוכני AI. מספקת API פשוט ליצירת סוכנים עם קריאת כלים, ניהול שיחה ואינטגרציית זיהוי Azure.
- **Microsoft Foundry Agent Service**: פלטפורמה ושירות פריסה ב-Microsoft Foundry לסוכנים. מציעה חיבור מובנה לשירותים כמו Azure OpenAI, Azure AI Search, Bing Search והפעלה של קוד.
 
עדיין לא בטוח מה לבחור?

### מקרי שימוש
 
בוא נבדוק אם נוכל לעזור לך על ידי מעבר על מספר מקרי שימוש נפוצים:
 
> ש: אני בונה אפליקציות סוכנים מבוססות AI לייצור ורוצה להתחיל במהירות
>

>ת: Microsoft Agent Framework היא בחירה מצוינת. היא מספקת API פייתוני פשוט דרך `FoundryChatClient` המאפשר להגדיר סוכנים עם כלים והנחיות בכמה שורות קוד בלבד.

>ש: אני צריך פריסה בדרג ארגוני עם אינטגרציות ל-Azure כמו Search והפעלה של קוד
>
> ת: Microsoft Foundry Agent Service הוא ההתאמה הטובה ביותר. זוהי פלטפורמה המספקת יכולות מובנות למודלים מרובים, Azure AI Search, Bing Search ו-Azure Functions. זה מקל לבנות סוכנים ב-Foundry Portal ולפרוס אותם בקנה מידה.
 
> ש: אני עדיין מבולבל, תן לי אפשרות אחת בלבד
>
> ת: התחל עם Microsoft Agent Framework כדי לבנות את הסוכנים שלך, ואז השתמש ב-Microsoft Foundry Agent Service כאשר תצטרך לפרוס ולהרחיב אותם בייצור. גישה זו מאפשרת לך לעשות איטרציות מהירות על הלוגיקה של הסוכן שלך תוך שמירה על דרך ברורה לפריסה ארגונית.
 
נסכם את ההבדלים המרכזיים בטבלה:

| מסגרת | מוקד | מושגי ליבה | מקרי שימוש |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK פשוט לסוכנים עם קריאת כלים | סוכנים, כלים, זיהוי Azure | בניית סוכני AI, שימוש בכלים, תהליכים מרובי שלבים |
| Microsoft Foundry Agent Service | מודלים גמישים, אבטחה ארגונית, יצירת קוד, קריאת כלים | מודולריות, שיתוף פעולה, תזמור תהליכים | פריסת סוכני AI מאובטחת, ניתנת להרחבה וגמישה |

## האם ניתן לשלב את כלים קיימים מאקוסיסטם Azure ישירות, או שצריך פתרונות עצמאיים?


התשובה היא כן, אתה יכול לשלב את כלי האקוסיסטם הקיימים שלך של Azure ישירות עם Microsoft Foundry Agent Service במיוחד, כיוון שהוא נבנה כדי לפעול בצורה חלקה עם שירותי Azure אחרים. לדוגמה, תוכל לשלב את Bing, Azure AI Search, ו-Azure Functions. יש גם אינטגרציה עמוקה עם Microsoft Foundry.

Microsoft Agent Framework משתלב גם עם שירותי Azure דרך `FoundryChatClient` וזהות Azure, המאפשרים לך לקרוא לשירותי Azure ישירות מכלי הסוכן שלך.

## דוגמאות קוד

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## יש לך שאלות נוספות על מסגרות סוכני AI?

הצטרף ל-[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) כדי להיפגש עם לומדים אחרים, להשתתף בשעות משרד ולקבל מענה לשאלותיך על סוכני AI.

## מקורות

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">שירות סוכני Azure</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - תגובות Azure OpenAI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## שיעור קודם

[מבוא לסוכני AI ומקרי שימוש](../01-intro-to-ai-agents/README.md)

## שיעור הבא

[הבנת תבניות עיצוב סוכניות](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->