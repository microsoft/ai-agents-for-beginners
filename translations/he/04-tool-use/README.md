[![איך לעצב סוכני AI טובים](../../../translated_images/he/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(לחצו על התמונה למעלה כדי לצפות בסרטון של השיעור הזה)_

# תבנית עיצוב שימוש בכלים

כלים הם מעניינים כי הם מאפשרים לסוכני AI מגוון רחב יותר של יכולות. במקום שלסוכן יהיה סט מוגבל של פעולות שהוא יכול לבצע, על ידי הוספת כלי, הסוכן יכול כעת לבצע מגוון רחב של פעולות. בפרק זה נסתכל על תבנית העיצוב לשימוש בכלים, שמתארת איך סוכני AI יכולים להשתמש בכלים ספציפיים כדי להשיג את מטרותיהם.

## מבוא

בשיעור זה, אנו מחפשים לענות על השאלות הבאות:

- מהי תבנית העיצוב לשימוש בכלים?
- לאילו מקרים ניתן להחיל אותה?
- מהם האלמנטים/בלוקים הבונים הנדרשים ליישום התבנית?
- מהן ההתייחסויות המיוחדות לשימוש בתבנית העיצוב לשימוש בכלים לבניית סוכני AI אמינים?

## יעדי למידה

לאחר השלמת שיעור זה, תוכל ל:

- להגדיר את תבנית העיצוב לשימוש בכלים ומטרתה.
- לזהות מקרים בהם ניתן להחיל את תבנית העיצוב לשימוש בכלים.
- להבין את האלמנטים המרכזיים הנדרשים ליישום התבנית.
- להכיר בהתייחסויות להבטחת אמינות בסוכני AI המשתמשים בתבנית עיצוב זו.

## מהי תבנית העיצוב לשימוש בכלים?

**תבנית העיצוב לשימוש בכלים** מתמקדת במתן היכולת ל-LLMs לאינטראקציה עם כלים חיצוניים כדי להשיג מטרות ספציפיות. כלים הם קוד שניתן להפעיל על ידי סוכן לביצוע פעולות. כלי יכול להיות פונקציה פשוטה כמו מחשבון, או קריאת API לשירות צד שלישי כמו חיפוש מחירי מניות או תחזית מזג אוויר. בהקשר של סוכני AI, כלים מתוכננים להיות מופעלים על ידי סוכנים בתגובה ל**קריאות פונקציה שנוצרו על ידי הדגם**.

## לאילו מקרים ניתן להחיל אותה?

סוכני AI יכולים לנצל כלים לביצוע משימות מורכבות, לשלוף מידע או לקבל החלטות. תבנית העיצוב לשימוש בכלים משמשת לעיתים תכופות בתרחישים הדורשים אינטראקציה דינמית עם מערכות חיצוניות, כגון בסיסי נתונים, שירותי רשת או מפרשי קוד. יכולת זו שימושית למספר מקרים שונים כולל:

- **שאיבת מידע דינמית:** סוכנים יכולים לשאול APIs חיצוניים או בסיסי נתונים כדי לקבל נתונים מעודכנים (למשל, שאילתא לבסיס נתונים SQLite לניתוח נתונים, שליפת מחירי מניות או מידע על מזג האוויר).
- **ביצוע ופרשנות של קוד:** סוכנים יכולים להפעיל קוד או סקריפטים לפתירת בעיות מתמטיות, יצירת דוחות או ביצוע סימולציות.
- **אוטומציה של זרימות עבודה:** אוטומציה של פעילויות חוזרות או רב-שלביות על ידי שילוב כלים כמו מתזמני משימות, שירותי דוא"ל או צינורות נתונים.
- **תמיכה בלקוחות:** סוכנים יכולים לאינטראקציה עם מערכות CRM, פלטפורמות ניהול כרטיסים או בסיסי ידע לפתירת שאלות משתמשים.
- **יצירה ועריכה של תוכן:** סוכנים יכולים לנצל כלים כמו בודקי דקדוק, מסכמים או מעריכי בטיחות תוכן כדי לסייע במשימות יצירת תוכן.

## מהם האלמנטים/הבלוקים הבונים הנדרשים ליישום תבנית העיצוב לשימוש בכלים?

בלוקים אלו מאפשרים לסוכן AI לבצע מגוון רחב של משימות. נבחן את האלמנטים המרכזיים הנדרשים ליישום תבנית העיצוב לשימוש בכלים:

- **סכימות פונקציה/כלי**: הגדרות מפורטות של כלים זמינים, כולל שם הפונקציה, מטרתה, הפרמטרים הנדרשים, והתוצאות הצפויות. סכימות אלו מאפשרות ל-LLM להבין אילו כלים זמינים ואיך לבנות בקשות תקפות.

- **לוגיקת ביצוע פונקציה**: קובעת כיצד ומתי מפעילים כלים בהתבסס על כוונת המשתמש והקשר השיחה. זה יכול לכלול מודולי תכנון, מנגנוני ניתוב או זרימות מותנות שקובעות שימוש בכלים בצורה דינמית.

- **מערכת ניהול הודעות**: רכיבים שמנהלים את זרימת השיחה בין קלטי המשתמש, תשובות LLM, קריאות כלים ותוצאות כלים.

- **מסגרת אינטגרציה לכלים**: תשתית שמחברת את הסוכן לכלים שונים, בין אם פונקציות פשוטות או שירותים חיצוניים מורכבים.

- **טיפול בשגיאות ואימות**: מנגנונים לניהול כשלים בביצוע כלים, אימות פרמטרים ולטפל בתגובות בלתי צפויות.

- **ניהול מצב**: עוקב אחר הקשר השיחה, אינטראקציות קודמות עם כלים ונתונים מתמשכים כדי להבטיח עקביות באינטראקציות רב-סבביות.

להלן נבחן את קריאת הפונקציה/הכלי בפירוט נוסף.
 
### קריאת פונקציה/כלי

קריאת פונקציה היא הדרך העיקרית לאפשר ל-LLMs לעשות אינטראקציה עם כלים. לעיתים קרובות תראה את המונחים 'פונקציה' ו'כלי' משמשים להחלפה מכיוון ש'פונקציות' (בלוקים של קוד שניתן לשימוש חוזר) הן ה'כלים' שסוכנים משתמשים כדי לבצע משימות. על מנת שקוד של פונקציה יופעל, LLM חייב להשוות את הבקשה של המשתמש לתיאור הפונקציות. לשם כך נשלחת סכימה המכילה את תיאורי כל הפונקציות הזמינות ל-LLM. ה-LLM בוחר אז את הפונקציה המתאימה ביותר למשימה ומחזיר את שמה והארגומנטים שלה. הפונקציה הנבחרת מופעלת, התגובה שלה נשלחת חזרה ל-LLM, אשר משתמש במידע כדי להגיב לבקשת המשתמש.

למפתחים שמעוניינים ליישם קריאת פונקציה עבור סוכנים, תצטרכו:

1. דגם LLM התומך בקריאת פונקציה
2. סכימה המכילה תיאורי פונקציות
3. הקוד לכל פונקציה שמתואר

נשתמש בדוגמה של קבלת השעה הנוכחית בעיר להמחשה:

1. **אתחול LLM שתומך בקריאת פונקציה:**

לא כל הדגמים תומכים בקריאת פונקציה, לכן חשוב לבדוק ש-LLM שבו אתה משתמש אכן תומך. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> תומך בקריאת פונקציה. נוכל להתחיל על ידי יצירת לקוח OpenAI מול Azure OpenAI **Responses API** (הנקודת קצה היציבה `/openai/v1/` — ללא צורך ב`api_version`).

    ```python
    # לאתחל את לקוח OpenAI עבור Azure OpenAI (API תגובות, נקודת קצה v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **יצירת סכמת פונקציה**:

לאחר מכן נגדיר סכמת JSON שמכילה את שם הפונקציה, תיאור מה הפונקציה עושה, ושמות ותיאורים של פרמטרי הפונקציה. 
לאחר מכן נעביר סכימה זו ללקוח שיצרנו קודם, יחד עם בקשת המשתמש למצוא את השעה בסן פרנסיסקו. דבר חשוב לציין הוא ש**קריאת כלי** היא מה שמוחזר, **ולא** התשובה הסופית לשאלה. כפי שצויין קודם, ה-LLM מחזיר את שם הפונקציה שבחר למשימה ואת הארגומנטים שיעברו אליה.

    ```python
    # תיאור פונקציה לקריאת המודל (פורמט כלי שטוח של API תגובות)
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # הודעת משתמש ראשונית
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # קריאת API ראשונה: לבקש מהמודל להשתמש בפונקציה
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # ממשק ה-API של התגובות מחזיר קריאות לכלי כפריטי function_call ב-response.output.
    # הוסף אותם לשיחה כדי שלמודל יהיה הקשר מלא בסיבוב הבא.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **הקוד לפונקציה הדרוש לביצוע המשימה:**

עכשיו כשה-LLM בחר איזו פונקציה יש להפעיל, הקוד שמבצע את המשימה צריך להתממש ולהיות מופעל.
נוכל לממש את הקוד לקבלת השעה הנוכחית בפייתון. נצטרך גם לכתוב קוד שיחלץ את השם והארגומנטים מתוך response_message כדי לקבל את התוצאה הסופית.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # לטפל בקריאות לפונקציות
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # להחזיר את תוצאת הכלי כפריט function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # קריאת API שנייה: לקבל את התגובה הסופית מהמודל
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

קריאת פונקציה היא ליבה של מרבית, אם לא כל, תבניות העיצוב לשימוש בכלים של סוכנים, אך יישום זה מאפס יכול להיות לפעמים מאתגר.
כפי שלמדנו ב-[שיעור 2](../../../02-explore-agentic-frameworks) מסגרות סוכנים מספקות לנו בלוקים לבניית שימוש בכלים מובנים מראש.
 
## דוגמאות לשימוש בכלים עם מסגרות סוכנים

הנה כמה דוגמאות כיצד ניתן ליישם את תבנית העיצוב לשימוש בכלים עם מסגרות סוכנים שונות:

### מסגרת סוכני מיקרוסופט

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">מסגרת סוכני מיקרוסופט</a> היא מסגרת AI בקוד פתוח לבניית סוכני AI. היא מפשטת את תהליך השימוש בקריאת פונקציה על ידי כך שמאפשרת להגדיר כלים כפונקציות פייתון עם הדקורטור `@tool`. המסגרת מנהלת את התקשורת בין הדגם לקוד שלך הלוך ושוב. היא גם מספקת גישה לכלים מובנים מראש כמו חיפוש קבצים ומפרש קוד דרך `FoundryChatClient`.

התרשים הבא מדגים את תהליך קריאת פונקציה במסגרת הסוכנים של מיקרוסופט:

![קריאת פונקציה](../../../translated_images/he/functioncalling-diagram.a84006fc287f6014.webp)

במסגרת סוכני מיקרוסופט, כלים מוגדרים כפונקציות עם דקורטור. נוכל להמיר את הפונקציה `get_current_time` שראינו קודם לכלי על ידי שימוש בדקורטור `@tool`. המסגרת תסדר אוטומטית את הפונקציה ופרמטריה, ותיצור סכימה שתישלח ל-LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# צור את הלקוח
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# צור סוכן והרץ עם הכלי
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### שירות סוכני מיקרוסופט Foundry

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">שירות סוכני מיקרוסופט Foundry</a> היא מסגרת סוכנים חדשה שנועדה להעצים מפתחים לבנות, לפרוס ולהגדיל סוכני AI איכותיים וניתנים להרחבה בבטחה מבלי צורך לנהל משאבי מחשוב ואחסון בסיסיים. השירות שימושי במיוחד ליישומי ארגונים כי הוא מנוהל לחלוטין עם אבטחה ברמת ארגון.

בהשוואה לפיתוח ישיר עם API של LLM, שירות סוכני Foundry של מיקרוסופט מספק מספר יתרונות, כולל:

- קריאת כלים אוטומטית – אין צורך לפענח קריאה לכלי, להפעיל את הכלי ולטפל בתגובה; הכל מתבצע בצד השרת
- ניהול מאובטח של נתונים – במקום לנהל את מצב השיחה בעצמך, תוכל להסתמך על 'שרשורים' לשמירת כל המידע הדרוש
- כלים מוכנים לשימוש – כלים בהם ניתן להשתמש לאינטראקציה עם מקורות הנתונים שלך, כמו Bing, Azure AI Search ו-Azure Functions.

הכלים הזמינים בשירות סוכני Foundry ניתן לחלק לשתי קטגוריות:

1. כלים ידע:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">חיפוש מבוסס Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">חיפוש קבצים</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. כלים פעולה:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">קריאת פונקציה</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">מפרש קוד</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">כלים מוגדרים על פי OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">פונקציות Azure</a>

שירות הסוכן מאפשר לנו להשתמש בכלים אלו יחד כ`toolset`. הוא גם משתמש ב`threads` ששומרים מעקב אחר היסטוריית ההודעות משיחה מסוימת.

דמיינו שאתה סוכן מכירות בחברה בשם Contoso. ברצונך לפתח סוכן שיחה שיכול לענות על שאלות לגבי נתוני המכירות שלך.

התמונה הבאה ממחישה כיצד תוכל להשתמש בשירות סוכני Microsoft Foundry לנתח את נתוני המכירות שלך:

![שירות סוכנים בפעולה](../../../translated_images/he/agent-service-in-action.34fb465c9a84659e.webp)

כדי להשתמש בכלים אלה עם השירות, נוכל ליצור לקוח ולהגדיר כלי או סט כלים. ליישום מעשי נוכל להשתמש בקוד פייתון הבא. ה-LLM יוכל לבחון את סט הכלים ולהחליט האם להשתמש בפונקציה שיצרת, `fetch_sales_data_using_sqlite_query`, או במפרש קוד מובנה תלוי בבקשת המשתמש.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # הפונקציה fetch_sales_data_using_sqlite_query שנמצאת בקובץ fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# אתחול ערכת הכלים
toolset = ToolSet()

# אתחול סוכן קריאות לפונקציות עם הפונקציה fetch_sales_data_using_sqlite_query והוספתה לערכת הכלים
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# אתחול כלי מתורגמן קוד והוספתו לערכת הכלים.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## מהם ההתייחסויות המיוחדות לשימוש בתבנית העיצוב לשימוש בכלים לבניית סוכני AI אמינים?

דאגה נפוצה עם SQL שנוצר דינמית על ידי LLMs היא אבטחה, בייחוד הסיכון של הזרקת SQL או פעולות זדוניות כמו מחיקה או עריכה של בסיס הנתונים. בעוד שהחששות האלה מוצדקים, ניתן להתמודד איתם ביעילות על ידי קביעת הרשאות גישה לבסיס הנתונים בצורה נכונה. ברוב בסיסי הנתונים יש להגדיר את בסיס הנתונים במצב קריאה בלבד. עבור שירותי בסיסי נתונים כמו PostgreSQL או Azure SQL, האפליקציה צריכה להיות מקבלת תפקיד קריאה בלבד (SELECT).

הרצת האפליקציה בסביבה מאובטחת מחזקת עוד יותר את ההגנה. בתרחישי ארגונים, הנתונים בדרך כלל מופקים ומומרים ממערכות תפעוליות לבסיס נתונים או מחסן נתונים במצב קריאה בלבד עם סכימה ידידותית למשתמש. גישה זו מבטיחה שהנתונים מאובטחים, מותאמים לביצועים ולנגישות, ושהאפליקציה מוגבלת עם גישה לקריאה בלבד.

## דוגמאות קוד

- פייתון: [מסגרת סוכן](./code_samples/04-python-agent-framework.ipynb)
- .NET: [מסגרת סוכן](./code_samples/04-dotnet-agent-framework.md)

## יש לכם שאלות נוספות על תבניות העיצוב לשימוש בכלים?

הצטרפו ל-[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) לפגוש לומדים אחרים, להשתתף בשעות קבלה ולקבל מענה לשאלות על סוכני AI.

## משאבים נוספים

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">סדנת שירות סוכני Azure AI</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">סדנת סוכנים מרובים - Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">סקירת מסגרת סוכני מיקרוסופט</a>


## בדיקת עשן לסוכן זה (אופציונלי)

לאחר שלמדת כיצד לפרוס סוכנים ב[שיעור 16](../16-deploying-scalable-agents/README.md), תוכל לבצע בדיקת עשן ל`TravelToolAgent` של השיעור הזה (האם הוא עדיין מפעיל את הכלים שלו ועונה?) עם [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). ראה [`tests/README.md`](../tests/README.md) כיצד להפעיל אותו.

## השיעור הקודם

[הבנת תבניות עיצוב אג'נטיות](../03-agentic-design-patterns/README.md)

## השיעור הבא

[RAG אג'נטי](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->