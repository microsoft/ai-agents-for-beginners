[![חקירת מסגרות סוכני AI](../../../translated_images/he/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(לחצו על התמונה למעלה כדי לצפות בסרטון של השיעור הזה)_

# חקר מסגרות סוכני AI

מסגרות סוכני AI הן פלטפורמות תוכנה שנועדו לפשט את יצירתם, הפריסה והניהול של סוכני AI. מסגרות אלו מספקות למפתחים רכיבים מוכנים, הפשטות וכלים שמייעלים את פיתוח מערכות AI מורכבות.

מסגרות אלו מסייעות למפתחים להתמקד בהיבטים הייחודיים של היישומים שלהם על ידי מתן גישות סטנדרטיות לאתגרים נפוצים בפיתוח סוכני AI. הן משפרות את סקלאביליות, הנגישות והיעילות בבניית מערכות AI.

## מבוא

בשיעור זה נכסה:

- מה הן מסגרות סוכני AI ומה הן מאפשרות למפתחים להשיג?
- כיצד צוותים יכולים להשתמש בהן כדי ליצור אב-טיפוס במהירות, לאטום ולשפר את יכולות הסוכן שלהם?
- מהם ההבדלים בין המסגרות והכלים שיצרה מיקרוסופט (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> ו-<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- האם אני יכול לשלב את כלי האקוסיסטם של Azure הקיימים אצלי ישירות, או שאני זקוק לפתרונות עצמאים?
- מהו Microsoft Foundry Agent Service וכיצד הוא עוזר לי?

## מטרות הלמידה

מטרות השיעור הן לסייע לך להבין:

- את התפקיד של מסגרות סוכני AI בפיתוח AI.
- כיצד לנצל מסגרות סוכני AI לבניית סוכנים אינטיליגנטיים.
- את היכולות המרכזיות שהן מאפשרות.
- את ההבדלים בין Microsoft Agent Framework ל-Microsoft Foundry Agent Service.

## מהן מסגרות סוכני AI ומה הן מאפשרות למפתחים לעשות?

מסגרות AI מסורתיות יכולות לעזור לך לשלב AI באפליקציות שלך ולשפר אותן בדרכים הבאות:

- **התאמה אישית**: AI יכול לנתח התנהגות והעדפות משתמשים כדי לספק המלצות, תוכן וחוויות מותאמות אישית.
דוגמה: שירותי סטרימינג כמו Netflix משתמשים ב-AI כדי להציע סרטים ותוכניות על בסיס היסטוריית צפייה, מה שמגביר מעורבות ושביעות רצון של המשתמשים.
- **אוטומציה ויעילות**: AI יכול לאוטומט משימות חוזרות, לייעל תהליכי עבודה ולשפר את היעילות התפעולית.
דוגמה: אפליקציות שירות לקוחות משתמשות בצ'אטבוטים מופעלים ב-AI לטיפול בפניות נפוצות, מקצרות זמני תגובה ומשחררות סוכני אנוש לטיפול בנושאים מורכבים יותר.
- **שיפור חווית המשתמש**: AI יכול לשפר את חוויית המשתמש הכוללת באמצעות תכונות אינטליגנטיות כמו זיהוי קול, עיבוד שפה טבעית וטקסט חזוי.
דוגמה: עוזרים וירטואליים כמו Siri ו-Google Assistant משתמשים ב-AI כדי להבין ולהגיב לפקודות קוליות, מה שמקל על המשתמשים באינטראקציה עם המכשירים שלהם.

### כל זה נשמע נהדר, אז למה אנחנו צריכים את מסגרת סוכן ה-AI?

מסגרות סוכני AI הן יותר מאשר מסגרות AI רגילות. הן מיועדות לאפשר יצירת סוכנים אינטיליגנטיים שיכולים לקיים אינטראקציה עם משתמשים, סוכנים אחרים, והסביבה להשגת מטרות ספציפיות. סוכנים אלו עשויים להפגין התנהגות אוטונומית, לקבל החלטות ולהסתגל לתנאים משתנים. בואו נבחן כמה יכולות מרכזיות שמסגרות סוכני AI מאפשרות:

- **שיתוף פעולה ותיאום בין סוכנים**: מאפשר יצירת מספר סוכני AI שעובדים יחד, מתקשרים ומתאמים לפתירת משימות מורכבות.
- **אוטומציה וניהול משימות**: מספק מנגנונים לאוטומציה של תהליכי עבודה מרובי שלבים, הקדמת משימות, וניהול דינמי של משימות בין הסוכנים.
- **הבנת הקשר והסתגלות**: מצייד סוכנים ביכולת להבין הקשר, להסתגל לסביבות משתנות, ולקבל החלטות המבוססות על מידע בזמן אמת.

לסיכום, סוכנים מאפשרים לך לעשות יותר, לקחת את האוטומציה לרמה הבאה, וליצור מערכות אינטיליגנטיות יותר שיכולות להסתגל וללמוד מהסביבה שלהן.

## כיצד ליצור אב-טיפוס במהירות, לאטום ולשפר את יכולות הסוכן?

זוהי סביבה דינמית ומהירה, אך ישנם אלמנטים משותפים לרוב מסגרות סוכני ה-AI שמסייעים באב-טיפוס ובלולאות איטרציה מהירות: רכיבי מודולים, כלים לשיתוף פעולה ולמידה בזמן אמת. בואו נעמיק בהם:

- **השתמשו ברכיבי מודולים**: SDK של AI מספקים רכיבים מוכנים כמו מחברים ל-AI ולזיכרון, קריאת פונקציות באמצעות שפה טבעית או תוספים, תבניות פרומפט ועוד.
- **נצלו כלים לשיתוף פעולה**: עצבו סוכנים עם תפקידים ומשימות ספציפיות, כדי לאפשר בדיקה והטמעה של תהליכי עבודה משותפים.
- **למידה בזמן אמת**: טמיעו לולאות משוב שבהן הסוכנים לומדים מאינטראקציות ומתאימים את התנהגותם באופן דינמי.

### השתמשו ברכיבי מודולים

SDKs כמו Microsoft Agent Framework מציעים רכיבים מוכנים כגון מחברי AI, הגדרות כלים וניהול סוכנים.

**כיצד צוותים יכולים להשתמש בזה**: ניתן להרכיב מהר רכיבים אלו כדי ליצור אב-טיפוס פונקציונלי מבלי להתחיל מאפס, מה שמאפשר ניסוי מהיר ואיטרציה.

**כיצד זה עובד בפועל**: ניתן להשתמש בפרסר מוכן לחילוץ מידע מקלט משתמש, במודול זיכרון לאחסון ושליפה, ובמחולל פרומפט לאינטראקציה עם המשתמשים, והכל ללא בניית הרכיבים עצמם מאפס.

**קוד לדוגמה**. נבחן דוגמה לשימוש ב-Microsoft Agent Framework יחד עם `FoundryChatClient` לגרום למודל להגיב לקלט המשתמש עם קריאת כלים:

``` python
# דוגמה למסגרת סוכן של מיקרוסופט בפייתון

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# הגדר פונקציית כלי לדוגמה להזמנת נסיעות
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
    # פלט לדוגמה: הטיסה שלך לנью יורק ב-1 בינואר 2025 הוזמנה בהצלחה. נסיעה טובה! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

מה שניתן לראות בדוגמה זו הוא כיצד ניתן לנצל פרסר מוכן לחלוץ מידע מרכזי מקלט המשתמש, כגון מקור, יעד ותאריך בקשת הזמנת טיסה. גישה מודולרית זו מאפשרת להתמקד בלוגיקה ברמה גבוהה.

### נצלו כלים לשיתוף פעולה

מסגרות כגון Microsoft Agent Framework מקלות על יצירת סוכנים מרובים שיכולים לעבוד יחד.

**כיצד צוותים יכולים להשתמש בזה**: צוותים יכולים לעצב סוכנים בעלי תפקידים ומשימות ספציפיות, כדי לבדוק ולשפר תהליכי עבודה משותפים ולשפר יעילות כוללת של המערכת.

**כיצד זה עובד בפועל**: ניתן ליצור צוות סוכנים שכל אחד ממנו ממלא פונקציה מתמחה, כגון שליפת מידע, ניתוח או קבלת החלטות. סוכנים אלו יכולים לתקשר ולשתף מידע כדי להשיג מטרה משותפת, כמו מענה לשאילתת משתמש או השלמת משימה.

**קוד לדוגמה (Microsoft Agent Framework)**:

```python
# יצירת סוכנים מרובים שעובדים יחד באמצעות מסגרת הסוכן של מיקרוסופט

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# סוכן משיכת נתונים
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

מה שניתן לראות בקוד הקודם הוא כיצד ליצור משימה הכוללת סוכנים מרובים שעובדים ביחד לניתוח נתונים. כל סוכן מבצע פונקציה ספציפית, והמשימה מתבצעת בתיאום בין הסוכנים להשגת התוצאה הרצויה. באמצעות יצירת סוכנים ייעודיים עם תפקידים מיוחדים, ניתן לשפר את יעילות וביצועי המשימה.

### למידה בזמן אמת

מסגרות מתקדמות מספקות יכולות להבנת הקשר והסתגלות בזמן אמת.

**כיצד צוותים יכולים להשתמש בזה**: צוותים יכולים ליישם לולאות משוב שבהן הסוכנים לומדים מאינטראקציות ומתאימים את התנהגותם באופן דינמי, מה שמוביל לשיפור ושכלול מתמשך של היכולות.

**כיצד זה עובד בפועל**: סוכנים יכולים לנתח משוב משתמש, נתוני סביבה ותוצאות משימות כדי לעדכן את בסיס הידע שלהם, להתאים אלגוריתמי קבלת החלטות ולשפר ביצועים לאורך זמן. תהליך למידה איטרטיבי זה מאפשר לסוכנים להסתגל לתנאים משתנים ולהעדפות משתמש, ובכך משפר את אפקטיביות המערכת הכוללת.

## מהם ההבדלים בין Microsoft Agent Framework ו-Microsoft Foundry Agent Service?

קיימות דרכים רבות להשוות גישות אלו, אך נסתכל על כמה הבדלים מרכזיים מבחינת עיצוב, יכולות ומקרי שימוש יעד:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework מספק SDK ממוקד לפיתוח סוכני AI באמצעות `FoundryChatClient`. הוא מאפשר למפתחים ליצור סוכנים שמשתמשים במודלים של Azure OpenAI עם קריאת כלים מובנית, ניהול שיחות, ואבטחה ברמת ארגונית דרך זהות Azure.

**מקרי שימוש**: בניית סוכני AI מוכנים לייצור עם שימוש בכלים, תהליכי עבודה מרובי שלבים, וסצנרי אינטגרציה ארגונית.

להלן כמה מושגים מרכזיים ב-Microsoft Agent Framework:

- **סוכנים**. סוכן נוצר דרך `FoundryChatClient` ומוגדר עם שם, הוראות וכלים. הסוכן יכול:
  - **לעבד הודעות משתמש** ולייצר תגובות באמצעות מודלים של Azure OpenAI.
  - **לקרוא לכלים** באופן אוטומטי בהתבסס על הקשר השיחה.
  - **לשמור מצב שיחה** לאורך מספר אינטראקציות.

  כאן קטע קוד המדגים יצירת סוכן:

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

- **כלים**. המסגרת תומכת בהגדרת כלים בתור פונקציות Python שהסוכן יכול להפעיל באופן אוטומטי. הכלים נרשמים בעת יצירת הסוכן:

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

- **תיאום בין סוכנים מרובים**. ניתן ליצור סוכנים מרובים עם התמחות שונות ולתאם את עבודתם:

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

- **אינטגרציה עם זהות Azure**. המסגרת משתמשת ב-`AzureCliCredential` (או `DefaultAzureCredential`) לאימות מאובטח ללא צורך במפתחות API, ומפשטת את הניהול.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service הוא תוסף חדש יחסית שהוצג בכנס Microsoft Ignite 2024. הוא מאפשר פיתוח והפצה של סוכני AI עם מודלים גמישים יותר, כגון קריאה ישירה למודלים פתוחים כמו Llama 3, Mistral ו-Cohere.

Microsoft Foundry Agent Service מספק מנגנוני אבטחה ארגוניים חזקים ושיטות לאחסון נתונים, מה שהופך אותו מתאים ליישומים ארגוניים.

הוא עובד ישירות עם Microsoft Agent Framework לבניית סוכנים ולפריסתם.

שירות זה נמצא כעת ב-Preview ציבורי ותומך ב-Python ו-C# לבניית סוכנים.

באמצעות Microsoft Foundry Agent Service Python SDK ניתן ליצור סוכן עם כלי מוגדר על ידי המשתמש:

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
        model="gpt-5-mini",
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

ל-Microsoft Foundry Agent Service יש את המושגים המרכזיים הבאים:

- **סוכן**. השירות משולב עם Microsoft Foundry. בתוך Foundry, סוכן AI מתפקד כמיקרו-שירות "חכם" שיכול לענות על שאלות (RAG), לבצע פעולות או לאוטומט תהליכים באופן מלא. זאת באמצעות שילוב של מודלי AI גנרטיביים וכלים המאפשרים גישה לאינפורמציה אמיתית וסינכרון איתה. דוגמה לסוכן:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    בדוגמה זו, סוכן נוצר עם מודל `gpt-5-mini`, שם `my-agent`, והוראות `You are helpful agent`. הסוכן מצויד בכלים ומשאבים לביצוע משימות פרשנות קוד.

- **שרשור והודעות**. השרשור הוא מושג חשוב נוסף. הוא מייצג שיחה או אינטראקציה בין סוכן למשתמש. השרשורים משמשים למעקב אחר התקדמות שיחה, אחסון מידע הקשר וניהול מצב האינטראקציה. דוגמה לשרשור:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # בקש מהסוכן לבצע עבודה על התהליך
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # קבל והקליט את כל ההודעות כדי לראות את תגובת הסוכן
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    בקוד הקודם נוצר שרשור. לאחר מכן נשלחה הודעה לשרשור. באמצעות קריאה ל-`create_and_process_run`, מבקשים מהסוכן לבצע עבודה בשרשור. בסוף, ההודעות מתקבלות ונרשמות לצפייה בתשובת הסוכן. ההודעות מצביעות על התקדמות השיחה בין המשתמש לסוכן. חשוב להבין שההודעות יכולות להיות מסוגים שונים כגון טקסט, תמונה או קובץ, כלומר עבודת הסוכן הביאה לתוצאה כמו תמונה או תגובת טקסט. כמפתח, ניתן להשתמש במידע זה לעיבוד נוסף או להצגתו למשתמש.

- **משולב עם Microsoft Agent Framework**. Microsoft Foundry Agent Service עובד באופן חלק עם Microsoft Agent Framework, מה שמאפשר לבנות סוכנים באמצעות `FoundryChatClient` ולפרסמם דרך השירות לסביבות ייצור.

**מקרי שימוש**: Microsoft Foundry Agent Service מיועד ליישומים ארגוניים שדורשים פריסה מאובטחת, סקלאבילית וגמישה של סוכני AI.

## מה ההבדל בין הגישות?
 
אמנם יש חפיפות, אך קיימים הבדלים מרכזיים בעיצוב, יכולות ומקרי השימוש:
 
- **Microsoft Agent Framework (MAF)**: SDK מוכן לייצור לבניית סוכני AI. מספק API ממוקד ליצירת סוכנים עם קריאת כלים, ניהול שיחות ואינטגרציה עם זהות Azure.
- **Microsoft Foundry Agent Service**: פלטפורמה ושירות פריסה ב-Microsoft Foundry לסוכנים. מציע חיבורים מובנים לשירותים כמו Azure OpenAI, Azure AI Search, Bing Search והפעלה של קוד.
 
עדיין לא בטוח איזה לבחור?

### מקרי שימוש
 
בואו נבדוק עם כמה מקרי שימוש נפוצים:
 
> ש: אני בונה יישומי סוכני AI לייצור ורוצה להתחיל במהירות
>

> ת: Microsoft Agent Framework הוא בחירה מצוינת. הוא מספק API פשוט בפייתון דרך `FoundryChatClient` שמאפשר להגדיר סוכנים עם כלים והוראות בכמה שורות קוד בלבד.

> ש: אני צריך פריסה ברמת ארגון עם אינטגרציות Azure כמו חיפוש והפעלה של קוד
>
> ת: Microsoft Foundry Agent Service מתאים ביותר. זו פלטפורמה שמספקת יכולות מובנות למודלים רבים, Azure AI Search, Bing Search ו-Azure Functions. הוא מקל על בניית הסוכנים ב-Foundry Portal ופריסתם בסקלה.
 
> ש: אני עדיין מבולבל, תן לי רק אפשרות אחת
>
> ת: התחל עם Microsoft Agent Framework לבניית הסוכנים שלך, ואז השתמש ב-Microsoft Foundry Agent Service כשתצטרך לפרוס ולסקלא אותם בייצור. גישה זו מאפשרת לך לאטום במהירות על הלוגיקה של הסוכן עם דרך ברורה לפריסה ארגונית.
 
נסכם את ההבדלים המרכזיים בטבלה:

| מסגרת | מיקוד | מושגים מרכזיים | מקרי שימוש |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK ממוקד לסוכן עם קריאת כלים | סוכנים, כלים, זהות Azure | בניית סוכני AI, שימוש בכלים, תהליכים מרובי שלבים |
| Microsoft Foundry Agent Service | מודלים גמישים, אבטחה ארגונית, יצירת קוד, קריאת כלים | מודולריות, שיתוף פעולה, תזמור תהליכים | פריסה מאובטחת, סקלאבילית וגמישה של סוכני AI |

## האם ניתן לשלב את כלי אקוסיסטם Azure הקיימים ישירות, או שיש צורך בפתרונות עצמאיים?


התשובה היא כן, ניתן לשלב את כלי האקוסיסטם הקיימים שלך של Azure ישירות עם שירות ה-Agent של Microsoft Foundry במיוחד, שכן הוא נבנה לעבוד בצורה חלקה עם שירותי Azure אחרים. לדוגמה, תוכל לשלב את Bing, Azure AI Search, ו-Azure Functions. יש גם אינטגרציה עמוקה עם Microsoft Foundry.

מסגרת הסוכנים של Microsoft משתלבת גם עם שירותי Azure דרך `FoundryChatClient` וזהות Azure, המאפשרת לך לקרוא לשירותי Azure ישירות מכלי הסוכן שלך.

## דוגמאות קוד

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## יש לך עוד שאלות לגבי מסגרות עבודה לסוכני AI?

הצטרף ל-[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) כדי לפגוש לומדים אחרים, להשתתף בשעות קבלת קהל ולקבל מענה לשאלותיך על סוכני AI.

## מקורות

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">שירות סוכן Azure</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">מסגרת סוכן Microsoft - תגובות Azure OpenAI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">שירות סוכן Microsoft Foundry</a>

## שיעור קודם

[הקדמה לסוכני AI ומקרי שימוש בהם](../01-intro-to-ai-agents/README.md)

## שיעור הבא

[הבנת דפוסי עיצוב סוכנייתיים](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->