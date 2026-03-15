[![חקירת מסגרות סוכני AI](../../../translated_images/he/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(לחצו על התמונה למעלה לצפייה בסרטון השיעור)_

# חקור מסגרות סוכני AI

מסגרות לסוכני AI הן פלטפורמות תוכנה שנועדו לפשט את יצירת, פרישת וניהול סוכני AI. מסגרות אלו מספקות למפתחים רכיבים מוכנים, הפשטות, וכלים שמייעלים את פיתוח מערכות AI מורכבות.

מסגרות אלה מסייעות למפתחים להתמקד בהיבטים הייחודיים של היישומים שלהם על ידי מתן גישות סטנדרטיות לאתגרים נפוצים בפיתוח סוכני AI. הן משפרות את הסקלביליות, הנגישות, והיעילות בבניית מערכות AI.

## מבוא

השיעור יכלול:

- מה הן מסגרות סוכני AI ומה הן מאפשרות למפתחים להשיג?
- כיצד צוותים יכולים להשתמש בהן כדי לדגם במהירות, לאטור ולשפר את יכולות הסוכן שלהם?
- מה ההבדלים בין המסגרות והכלים שיצרה מיקרוסופט (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> ו-<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- האם אני יכול לשלב ישירות את כלי האקוסיסטם הקיימים של Azure שלי, או שצריך פתרונות עצמאיים?
- מהו שירות Azure AI Agents וכיצד זה עוזר לי?

## מטרות הלמידה

מטרות השיעור הן לעזור לך להבין:

- תפקיד מסגרות סוכני AI בפיתוח AI.
- כיצד לנצל את מסגרות סוכני AI לבניית סוכנים חכמים.
- יכולות מפתח המופעלות על ידי מסגרות סוכני AI.
- ההבדלים בין Microsoft Agent Framework לשירות Azure AI Agent.

## מהן מסגרות סוכני AI ומה הן מאפשרות למפתחים לעשות?

מסגרות AI מסורתיות יכולות לסייע לך לשלב AI באפליקציות שלך ולשפר אותן בדרכים הבאות:

- **התאמה אישית**: AI יכול לנתח התנהגות משתמש והעדפות כדי לספק המלצות מותאמות, תוכן וחוויות מותאמות אישית. דוגמה: שירותי סטרימינג כמו Netflix משתמשים ב-AI כדי להציע סרטים ותכניות בהתאם להיסטוריית הצפייה, משפרים מעורבות ושביעות רצון משתמש.
- **אוטומציה ויעילות**: AI יכול לאוטומט משימות חוזרות, לייעל תהליכים ולשפר יעילות תפעולית. דוגמה: אפליקציות שירות לקוחות משתמשות בצ'אטבוטים מבוססי AI כדי לטפל בפניות נפוצות, מקצרות זמני תגובה ומשחררות סוכנים אנושיים לטיפול בנושאים מורכבים יותר.
- **חוויית משתמש משופרת**: AI יכול לשפר את חוויית המשתמש על ידי מתן תכונות חכמות כגון זיהוי קולי, עיבוד שפה טבעית וטקסט תחזיתי. דוגמה: עוזרות וירטואליות כמו Siri ו-Google Assistant משתמשות ב-AI כדי להבין ולהגיב לפקודות קוליות, ומקלות על האינטראקציה עם המכשירים.

### כל זה נשמע מצוין, אז מדוע אנו זקוקים למסגרת סוכני AI?

מסגרות סוכני AI מייצגות משהו מעבר למסגרות AI פשוטות. הן מיועדות לאפשר יצירת סוכנים חכמים שיכולים לקיים אינטראקציה עם משתמשים, סוכנים אחרים והסביבה כדי להשיג מטרות מסוימות. סוכנים אלו יכולים להציג התנהגות אוטונומית, לקבל החלטות ולהסתגל לתנאים משתנים. הנה כמה יכולות מרכזיות שמאפשרות מסגרות סוכני AI:

- **שיתוף פעולה ותיאום בין סוכנים**: מאפשר יצירת סוכני AI מרובים שיכולים לעבוד ביחד, לתקשר ולתאם כדי לפתור משימות מורכבות.
- **אוטומציה וניהול משימות**: מספקים מנגנונים לאוטומציה של תהליכים מרובי שלבים, הפניית משימות וניהול דינמי של משימות בין הסוכנים.
- **הבנה קונטקסטואלית והסתגלות**: מציידים סוכנים עם היכולת להבין הקשר, להסתגל לסביבות משתנות ולקבל החלטות בהתבסס על מידע בזמן אמת.

לסיכום, סוכנים מאפשרים לך לעשות יותר, לקחת את האוטומציה לרמה הבאה, וליצור מערכות חכמות שיכולות להסתגל וללמוד מהסביבה שלהן.

## כיצד לדגם במהירות, לאטור ולשפר את יכולות הסוכן?

שוק זה מתקדם במהירות, אבל יש כמה אלמנטים נפוצים ברוב מסגרות סוכני AI שיכולים לסייע לך לדגם במהירות ולאטור, כגון רכיבי מודול, כלים לשיתוף פעולה ולמידה בזמן אמת. נבחן אותם:

- **השתמש ברכיבים מודולריים**: ערכות פיתוח (SDK) של AI מציעות רכיבים מוכנים כגון מחברים ל-AI ולזיכרון, קריאות פונקציה באמצעות שפה טבעית או תוספי קוד, תבניות הנעה ועוד.
- **נצל כלים לשיתוף פעולה**: עצב סוכנים עם תפקידים ותחומי אחריות ספציפיים, המאפשרים להם לבחון ולשפר תהליכי עבודה שיתופיים.
- **למד בזמן אמת**: הפעל לולאות משוב בהן סוכנים לומדים מאינטראקציות ומתאימים את התנהגותם באופן דינמי.

### השתמש ברכיבים מודולריים

SDKs כמו Microsoft Agent Framework מציעים רכיבים מוכנים כגון מחברי AI, הגדרות כלים וניהול סוכנים.

**כיצד צוותים יכולים להשתמש בזה**: צוותים יכולים להרכיב במהירות את הרכיבים הללו כדי ליצור אבטיפוס פונקציונלי מבלי להתחיל מאפס, מה שמאפשר ניסוי מהיר ולאטור.

**איך זה עובד בפועל**: ניתן להשתמש במנתח מידע מוכן כדי לחלץ מידע מהקלט של המשתמש, במודול זיכרון לאחסון ושליפה של נתונים, ובמחולל תבניות כדי לתקשר עם המשתמשים, הכל מבלי לבנות רכיבים אלו מאפס.

**דוגמת קוד**. נבחן דוגמה של שימוש ב-Microsoft Agent Framework עם `AzureAIProjectAgentProvider` לקבלת תגובה בקלט המשתמש עם קריאת כלים:

``` python
# דוגמה למסגרת Microsoft Agent בפייתון

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# הגדר פונקציית כלי לדוגמה להזמנת נסיעות
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # פלט לדוגמה: טיסתך לניו יורק ב־1 בינואר 2025 הוזמנה בהצלחה. נסיעה בטוחה! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

מה שניתן לראות בדוגמה זו הוא איך ניתן להשתמש במנתח מידע מוכן כדי לחלץ פרטים מרכזיים מהקלט של המשתמש, כגון מקור, יעד ותאריך בקשת הזמנת טיסה. גישה מודולרית זו מאפשרת להתמקד בלוגיקה ברמה גבוהה.

### נצל כלים לשיתוף פעולה

מסגרות כמו Microsoft Agent Framework מאפשרות יצירת מספר סוכנים שיכולים לעבוד יחד.

**כיצד צוותים יכולים להשתמש בזה**: צוותים יכולים לעצב סוכנים עם תפקידים ותחומי אחריות ספציפיים, המאפשרים להם לבחון ולשפר תהליכי עבודה שיתופיים ולשפר את יעילות המערכת הכוללת.

**איך זה עובד בפועל**: ניתן ליצור צוות סוכנים שכל סוכן מתמחה בפונקציה מסוימת, כגון אחזור נתונים, ניתוח או קבלת החלטות. סוכנים אלו יכולים לתקשר ולחלוק מידע כדי להשיג מטרה משותפת, כגון מענה לשאילתת משתמש או השלמת משימה.

**דוגמת קוד (Microsoft Agent Framework)**:

```python
# יצירת מספר סוכנים שעובדים ביחד באמצעות Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# סוכן אחזור נתונים
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# סוכן ניתוח נתונים
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# להריץ סוכנים ברצף על משימה
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

בדוגמה בקוד הקודם ניתן לראות איך ליצור משימה הכוללת סוכנים מרובים שעובדים יחד לניתוח נתונים. כל סוכן מבצע פונקציה ייעודית, והמשימה מתבצעת באמצעות תיאום בין הסוכנים כדי להשיג את התוצאה הרצויה. על ידי יצירת סוכנים ייעודיים בעלי תפקידים מיוחדים, ניתן לשפר את יעילות וביצוע המשימה.

### למד בזמן אמת

מסגרות מתקדמות מספקות יכולות להבנת הקשר בזמן אמת והסתגלות.

**כיצד צוותים יכולים להשתמש בזה**: ניתן ליישם לולאות משוב בהן הסוכנים לומדים מאינטראקציות ומתאימים את התנהגותם באופן דינמי, מה שמוביל לשיפור ולדייקנות מתמשכת של היכולות.

**איך זה עובד בפועל**: סוכנים יכולים לנתח משוב משתמש, נתוני סביבה ותוצאות משימות כדי לעדכן את בסיס הידע שלהם, לכוונן אלגוריתמים לקבלת החלטות ולשפר ביצועים לאורך זמן. תהליך למידה איטרטיבי זה מאפשר לסוכנים להסתגל לתנאים משתנים והעדפות משתמשים, ומשפר את היעילות הכוללת של המערכת.

## מה ההבדלים בין Microsoft Agent Framework לשירות Azure AI Agent?

יש דרכים רבות להשוות בין הגישות, אך נבחן כמה הבדלים מרכזיים בעיצוב, יכולות ומקרי שימוש:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework מספק SDK פשוט לבניית סוכני AI באמצעות `AzureAIProjectAgentProvider`. הוא מאפשר למפתחים ליצור סוכנים המשתמשים במודלים של Azure OpenAI עם קריאות כלים מובנות, ניהול שיחות ואבטחה ארגונית דרך זהות Azure.

**מקרי שימוש**: בניית סוכני AI מוכנים לייצור עם שימוש בכלים, תהליכים מרובי שלבים ותרחישי אינטגרציה ארגוניים.

הנה כמה מושגים מרכזיים ב-Microsoft Agent Framework:

- **סוכנים**: סוכן נוצר באמצעות `AzureAIProjectAgentProvider` ומוגדר עם שם, הוראות וכלים. הסוכן יכול:
  - **לעבד הודעות משתמש** וליצור תגובות באמצעות מודלים של Azure OpenAI.
  - **לקרוא לכלים** אוטומטית על בסיס הקשר השיחה.
  - **לשמור מצב שיחה** לאורך אינטראקציות מרובות.

  להלן קטע קוד המדגים יצירת סוכן:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **כלים**: המסגרת תומכת בהגדרת כלים כפונקציות Python שהסוכן יכול להפעיל אוטומטית. הכלים נרשמים בעת יצירת הסוכן:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **תיאום רב-סוכני**: ניתן ליצור סוכנים מרובים עם התמחות שונה ולתאם את עבודתם:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **אינטגרציה עם זהות Azure**: המסגרת משתמשת ב-`AzureCliCredential` (או ב-`DefaultAzureCredential`) לאימות מאובטח וללא צורך במפתחות API, מה שמפשט את ניהול האבטחה.

## שירות Azure AI Agent

שירות Azure AI Agent הוא תוספת חדשה, שהוצגה ב-Microsoft Ignite 2024. הוא מאפשר פיתוח ופריסה של סוכני AI עם מודלים גמישים יותר, כגון קריאה ישירה למודלים פתוחים כמו Llama 3, Mistral ו-Cohere.

שירות Azure AI Agent מספק מנגנוני אבטחה ארגוניים חזקים ושיטות אחסון נתונים, מה שהופך אותו מתאים לאפליקציות ארגוניות.

השירות עובד מחוץ לקופסה עם Microsoft Agent Framework לבניית ופריסת סוכנים.

השירות נמצא כעת בגרסת תצוגה ציבורית, ותומך ב-Python ו-C# לבניית סוכנים.

באמצעות SDK של שירות Azure AI Agent ב-Python, ניתן ליצור סוכן עם כלי שהוגדר ע"י המשתמש:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# הגדר פונקציות לכלי
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
        model="gpt-4o-mini",
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

לשירות Azure AI Agent קיימים המושגים המרכזיים הבאים:

- **סוכן**: שירות Azure AI Agent משתלב עם Microsoft Foundry. בתוך AI Foundry, סוכן AI משמש כמיקרו-שירות "חכם" שניתן להשתמש בו למענה על שאלות (RAG), ביצוע פעולות או אוטומציה מלאה של תהליכים. הוא משיג זאת על ידי שילוב כוחם של מודלים גנרטיביים עם כלים המאפשרים גישה לאותם מקורות נתונים חיצוניים ותקשורת איתם. משמעות דוגמה לסוכן:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    בדוגמה זו, סוכן נוצר עם דגם `gpt-4o-mini`, שם `my-agent` והוראות `You are helpful agent`. הסוכן מצויד בכלים ובמשאבים לביצוע משימות פרשנות קוד.

- **שרשורים והודעות**: השרשור הוא מושג חשוב נוסף. הוא מייצג שיחה או אינטראקציה בין סוכן למשתמש. אפשר להשתמש בשרשורים למעקב אחר התקדמות השיחה, אחסון מידע קונטקסטואלי וניהול מצב האינטראקציה. הנה דוגמה לשרשור:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    בקוד שלמעלה נוצר שרשור. לאחר מכן נשלחה הודעה לשרשור. על ידי קריאה ל-`create_and_process_run`, מבקשים מהסוכן לבצע עבודה בשרשור. בסיום, ההודעות נשלפות ונרשמות לצפייה בתגובת הסוכן. ההודעות מצביעות על התקדמות השיחה בין המשתמש לסוכן. חשוב להבין שההודעות יכולות להיות מסוגים שונים כמו טקסט, תמונה או קובץ, כלומר עבודת הסוכן הורידה לפועל למשל תמונה או תגובת טקסט. כמפתח, ניתן להשתמש במידע זה להמשך עיבוד התגובה או להצגתה למשתמש.

- **אינטגרציה עם Microsoft Agent Framework**: שירות Azure AI Agent עובד בשלמות עם Microsoft Agent Framework, כלומר ניתן לבנות סוכנים באמצעות `AzureAIProjectAgentProvider` ולפרוס אותם דרך שירות הסוכנים לתרחישי ייצור.

**מקרי שימוש**: שירות Azure AI Agent מיועד לאפליקציות ארגוניות שדורשות פריסה בטוחה, סקלבילית וגמישה של סוכני AI.

## מה ההבדל בין הגישות?

נראה שיש חפיפה, אך יש גם הבדלים מרכזיים בעיצוב, יכולות ומקרי שימוש:

- **Microsoft Agent Framework (MAF)**: ערכת פיתוח מוכנה לייצור לבניית סוכני AI. מספקת API פשוט ליצירת סוכנים עם קריאת כלים, ניהול שיחות ואינטגרציה עם זהות Azure.
- **שירות Azure AI Agent**: פלטפורמה ושירות פריסה ב-Azure Foundry עבור סוכנים. כולל קישוריות מובנית לשירותים כגון Azure OpenAI, Azure AI Search, Bing Search והפעלת קוד.

עדיין לא בטוח מה לבחור?

### מקרי שימוש

נראה אם נוכל לעזור על ידי מעבר על כמה מקרי שימוש נפוצים:

> ש: אני בונה יישומי סוכני AI לייצור ורוצה להתחיל במהירות
>

>ת: Microsoft Agent Framework הוא בחירה מצוינת. הוא מספק API פשוט בסגנון Python דרך `AzureAIProjectAgentProvider` שמאפשר להגדיר סוכנים עם כלים והוראות בכמה שורות קוד בלבד.

> ש: אני צריך פריסה ארגונית עם אינטגרציות Azure כמו חיפוש והפעלת קוד
>
> ת: שירות Azure AI Agent הוא הבחירה הטובה ביותר. זהו שירות פלטפורמה שמספק יכולות מובנות למודלים מרובים, Azure AI Search, Bing Search ופונקציות Azure. הוא מאפשר בניית סוכנים בפורטל Foundry ופריסה בקנה מידה.

> ש: אני עדיין מבולבל, תן לי אפשרות אחת בלבד
>
> ת: התחל עם Microsoft Agent Framework לבניית הסוכנים, ולאחר מכן השתמש בשירות Azure AI Agent כשאתה צריך לפרוס ולסקל אותם בייצור. גישה זו מאפשרת לך לאטור במהירות את הלוגיקה של הסוכן תוך שמירה על נתיב ברור לפריסה ארגונית.

נסכם את ההבדלים המרכזיים בטבלה:

| מסגרת | מוקד | מושגים מרכזיים | מקרי שימוש |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK פשוט לסוכנים עם קריאת כלים | סוכנים, כלים, זהות Azure | בניית סוכני AI, שימוש בכלים, תהליכים מרובי שלבים |
| Azure AI Agent Service | מודלים גמישים, אבטחה ארגונית, יצירת קוד, קריאת כלים | מודולריות, שיתוף פעולה, ארגון תהליכים | פריסה בטוחה, סקלבילית וגמישה של סוכני AI |

## האם אני יכול לשלב ישירות את כלי האקוסיסטם הקיימים של Azure שלי, או שצריך פתרונות עצמאיים?
התשובה היא כן, ניתן לשלב את כלי המערכת האקולוגית של Azure הקיימים ישירות עם שירות Azure AI Agent במיוחד, מכיוון שהוא בנוי לעבוד בצורה חלקה עם שירותי Azure אחרים. לדוגמה, תוכל לשלב את Bing, Azure AI Search, ו-Azure Functions. יש גם אינטגרציה עמוקה עם Microsoft Foundry.

מסגרת Microsoft Agent Framework משתלבת גם היא עם שירותי Azure דרך `AzureAIProjectAgentProvider` וזהות Azure, ומאפשרת לך לקרוא לשירותי Azure ישירות מכלי הסוכן שלך.

## דוגמאות קוד

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## יש לך שאלות נוספות על מסגרות AI Agent?

הצטרף ל-[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) כדי להיפגש עם לומדים נוספים, להשתתף בשעות משרד ולקבל מענה לשאלות שלך על סוכני AI.

## מקורות

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">שירות Azure Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - תגובות Azure OpenAI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">שירות Azure AI Agent</a>

## השיעור הקודם

[מבוא לסוכני AI ומקרי שימוש](../01-intro-to-ai-agents/README.md)

## השיעור הבא

[הבנת תבניות עיצוב סוכניות](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל טעויות או אי-דיוקים. המסמך המקורי בשפת המקור נחשב למקור הסמכותי. למידע קריטי מומלץ לפנות לשירות תרגום מקצועי על ידי אדם. אין אנו אחראים לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->