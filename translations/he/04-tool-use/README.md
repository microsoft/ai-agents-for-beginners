[![כיצד לעצב סוכני AI טובים](../../../translated_images/he/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(לחצו על התמונה למעלה לצפייה בווידאו של השיעור)_

# תבנית עיצוב שימוש בכלים

כלים מעניינים כי הם מאפשרים לסוכני AI להחזיק בטווח רחב יותר של יכולות. במקום שהסוכן יוכל לבצע רק סט מוגבל של פעולות, על ידי הוספת כלי, הסוכן יכול כעת לבצע מגוון רחב של פעולות. בפרק זה נבחן את תבנית העיצוב שימוש בכלים, המתארת כיצד סוכני AI יכולים להשתמש בכלים ספציפיים כדי להשיג את מטרותיהם.

## מבוא

בשיעור זה אנחנו מעוניינים לענות על השאלות הבאות:

- מהי תבנית עיצוב שימוש בכלים?
- לאילו מקרים ניתן ליישם אותה?
- מהם האלמנטים/הלבנים הנדרשים ליישום תבנית העיצוב?
- מהן ההתחשבויות המיוחדות לשימוש בתבנית עיצוב שימוש בכלים לבניית סוכני AI אמינים?

## מטרות הלמידה

בסיום שיעור זה תוכלו:

- להגדיר את תבנית עיצוב שימוש בכלים ואת מטרתה.
- לזהות מקרים בהם תבנית עיצוב זו ניתנת ליישום.
- להבין את האלמנטים המרכזיים הדרושים ליישום התבנית.
- לזהות שיקולים להבטחת אמינות בסוכני AI המשתמשים בתבנית עיצוב זו.

## מהי תבנית עיצוב שימוש בכלים?

תבנית העיצוב **שימוש בכלים** מתמקדת במתן יכולת למודלי שפה גדולים (LLMs) לקיים אינטראקציה עם כלים חיצוניים כדי להשיג מטרות ספציפיות. כלים הם קוד שניתן להפעילו על ידי סוכן לביצוע פעולות. כלי יכול להיות פונקציה פשוטה כמו מחשבון, או קריאת API לשירות צד שלישי כגון חיפוש מחירי מניות או תחזית מזג אוויר. בהקשר של סוכני AI, כלים מיועדים להיות מופעלים על ידי סוכנים בתגובה ל**קריאות פונקציה שנוצרות על ידי המודל**.

## לאילו שימושים ניתן ליישם אותה?

סוכני AI יכולים לנצל כלים כדי להשלים משימות מורכבות, לאחזר מידע או לקבל החלטות. תבנית עיצוב שימוש בכלים משמשת לעיתים קרובות בתרחישים הדורשים אינטראקציה דינמית עם מערכות חיצוניות, כגון מסדי נתונים, שירותי רשת או מפרשי קוד. יכולת זו שימושית למספר מקרים שונים כגון:

- **שליפת מידע דינמית:** סוכנים יכולים לשאול APIs או מסדי נתונים חיצוניים כדי ללקט נתונים מעודכנים (למשל, שאילתא במסד SQLite לניתוח נתונים, קבלת מחירי מניות או מידע על מזג האוויר).
- **ביצוע ופענוח קוד:** סוכנים יכולים להפעיל קוד או סקריפטים לפתרון בעיות מתמטיות, יצירת דוחות או ביצוע סימולציות.
- **אוטומציה של זרימות עבודה:** אוטומציה של זרימות עבודה חוזרות או מרובות שלבים באמצעות שילוב כלים כמו מתזמנים, שירותי דוא"ל או צינורות נתונים.
- **תמיכה בלקוחות:** סוכנים יכולים לקיים אינטראקציה עם מערכות CRM, פלטפורמות כרטיסים או מאגרי ידע לפתרון שאילתות משתמש.
- **יצירה ועריכת תוכן:** סוכנים יכולים להשתמש בכלים כמו בודקי דקדוק, מסכמי טקסט או מערכות להערכת בטיחות תוכן לסיוע במשימות יצירת תוכן.

## מהם האלמנטים/הלבנים הנדרשים ליישום תבנית עיצוב שימוש בכלים?

הלבנים האלו מאפשרים לסוכן AI לבצע מגוון רחב של משימות. הבה נבחן את האלמנטים המרכזיים הדרושים ליישום תבנית עיצוב שימוש בכלים:

- **סכמות פונקציות/כלים**: הגדרות מפורטות של הכלים הזמינים, כולל שם הפונקציה, מטרתה, הפרמטרים הדרושים והפלטים הצפויים. סכמות אלה מאפשרות ל-LLM להבין אילו כלים זמינים וכיצד לבנות בקשות תקפות.

- **לוגיקת ביצוע פונקציות**: מגדירה כיצד ומתי להפעיל כלים בהתבסס על כוונת המשתמש והקשר השיחה. זה יכול לכלול מודולי תכנון, מנגנוני ניתוב או זרמים תנאים שקובעים שימוש דינמי בכלים.

- **מערכת טיפול בהודעות**: רכיבים שמנהלים את מהלך השיחה בין קלטי המשתמש, תגובות ה-LLM, קריאות לכלים ותוצאות הכלים.

- **מסגרת אינטגרציה של כלים**: תשתית שמחברת את הסוכן לכלים שונים, בין אם פונקציות פשוטות או שירותים חיצוניים מורכבים.

- **טיפול בשגיאות ואימות**: מנגנונים לטיפול בכשלונות בביצוע הכלי, אימות פרמטרים וניהול תגובות בלתי צפויות.

- **ניהול מצב**: עוקב אחרי הקשר השיחה, אינטראקציות קודמות עם כלים ונתונים מתמשכים להבטחת עקביות במהלך שיחות מרובות שלבים.

נעבור כעת לפירוט נוסף על קריאת פונקציות/כלים.
 
### קריאת פונקציות/כלים

קריאת פונקציות היא הדרך העיקרית שבאמצעותה מאפשרים למודלים גדולים של שפה (LLMs) לקיים אינטראקציה עם כלים. לעיתים קרובות תראו ש'פונקציה' ו'כלי' משמשים להחלפה זה עם זה משום ש'פונקציות' (קטעי קוד שניתן להשתמש בהם שוב) הן הכלים שהסוכנים משתמשים בהם לצורך ביצוע משימות. כדי שהקוד של פונקציה יופעל, ה-LLM חייב להשוות את הבקשה של המשתמש עם תיאור הפונקציה. לשם כך נשלח ל-LLM סכימה הכוללת תיאורים של כל הפונקציות הזמינות. ה-LLM בוחר אז את הפונקציה המתאימה ביותר למשימה ומחזיר את שמה וארגומנטיה. הפונקציה שנבחרה מופעלת, תגובתה נשלחת חזרה ל-LLM שמשתמש במידע כדי להגיב לבקשת המשתמש.

כדי שמפתחים יוכלו ליישם קריאת פונקציות לסוכנים, תצטרכו:

1. מודל LLM התומך בקריאת פונקציות
2. סכימה הכוללת תיאורי פונקציות
3. הקוד של כל פונקציה שמתואר

נשתמש בדוגמה של קבלת השעה הנוכחית בעיר כדי להמחיש:

1. **הפעלת מודל LLM התומך בקריאת פונקציות:**

    לא כל המודלים תומכים בקריאת פונקציות, לכן חשוב לבדוק שה-LLM שאתם משתמשים בו עושה זאת. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> תומך בקריאת פונקציות. נתחיל ביצירת לקוח Azure OpenAI.

    ```python
    # אתחל את לקוח Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **יצירת סכמת פונקציה:**

    כעת נגדיר סכימת JSON הכוללת את שם הפונקציה, תיאור מה הפונקציה עושה, ושמות ותיאורים של פרמטרי הפונקציה.
    לאחר מכן נעביר סכימה זו ללקוח שנוצר קודם, יחד עם בקשת המשתמש למצוא את השעה בסן פרנסיסקו. חשוב לציין ש**קריאת כלי** היא מה שמוחזר, **ולא** התשובה הסופית לשאלה. כפי שצוין קודם, ה-LLM מחזיר את שם הפונקציה שנבחרה למשימה ואת הארגומנטים שיועברו לה.

    ```python
    # תיאור הפונקציה למודל לקריאה
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
   
    ```python
  
    # הודעת משתמש התחלתית
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # קריאת API ראשונה: בקש מהמודל להשתמש בפונקציה
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # עיבוד תגובת המודל
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **קוד הפונקציה הנדרש לביצוע המשימה:**

    כעת שה-LLM בחר איזו פונקציה יש להריץ, יש ליישם ולהפעיל את הקוד שמבצע את המשימה.
    נוכל לממש את הקוד לקבלת השעה הנוכחית בפייתון. כמו כן, נצטרך לכתוב קוד לחילוץ השם והארגומנטים מתוך response_message כדי לקבל את התוצאה הסופית.

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
     # טיפול בקריאות לפונקציות
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # קריאה שנייה ל-API: קבלת התגובה הסופית מהמודל
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```
 
קריאת פונקציות היא בלב ליבה של רוב, אם לא כל, תבניות עיצוב השימוש בכלים לסוכנים, אך יישומה מאפס יכול להיות מאתגר לפעמים.
כפי שלמדנו ב-[שיעור 2](../../../02-explore-agentic-frameworks) מסגרות agentic מספקות לנו לבנים מוכנות מראש ליישום שימוש בכלים.
 
## דוגמאות לשימוש בכלים עם מסגרות Agentic

להלן כמה דוגמאות כיצד ניתן ליישם את תבנית העיצוב שימוש בכלים באמצעות מסגרות agentic שונות:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> היא מסגרת AI בקוד פתוח לפיתוחי .NET, Python ו-Java עם מודלים גדולים של שפה (LLMs). היא מפשטת את תהליך השימוש בקריאות פונקציות על ידי תיאור אוטומטי של הפונקציות ופרמטריהן למודל בתהליך הנקרא <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">סריאליזציה</a>. היא גם מנהלת את התקשורת ההדדית בין המודל לקוד שלך. יתרון נוסף בשימוש במסגרת agentic כמו Semantic Kernel הוא שהיא מאפשרת גישה לכלים מוכנים מראש כמו <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">חיפוש קבצים</a> ו-<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">מפרש קוד</a>.

התמונה הבאה ממחישה את תהליך קריאת הפונקציות עם Semantic Kernel:

![function calling](../../../translated_images/he/functioncalling-diagram.a84006fc287f6014.webp)

ב-Semantic Kernel פונקציות/כלים נקראים <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">תוספים</a>. נוכל להמיר את הפונקציה `get_current_time` שראינו קודם לתוסף על ידי הפיכתה למחלקה עם הפונקציה בתוכה. נוכל גם לייבא את הדקורטור `kernel_function`, שלוקח את תיאור הפונקציה. כאשר ניצור Kernel עם GetCurrentTimePlugin, הקוד יסריאליז את הפונקציה ופרמטריה אוטומטית, וייצר את הסכימה שנשלחת ל-LLM בתהליך.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# צור את הליבה
kernel = Kernel()

# צור את התוסף
get_current_time_plugin = GetCurrentTimePlugin(location)

# הוסף את התוסף לליבה
kernel.add_plugin(get_current_time_plugin)
```
  
### שירות Azure AI Agent

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">שירות Azure AI Agent</a> היא מסגרת agentic חדשה שנועדה לאפשר למפתחים לבנות, לפרוס ולהרחיב סוכני AI אמינים ובטוחים ללא הצורך לנהל את משאבי החישוב והאחסון התשתיתיים. השירות שימושי במיוחד לאפליקציות ארגוניות שכן הוא שירות מנוהל במלואו ברמת אבטחה ארגונית.

בהשוואה לפיתוח ישיר עם ממשק ה-API של LLM, שירות Azure AI Agent מספק מספר יתרונות, כולל:

- קריאת כלים אוטומטית – אין צורך לפרש קריאת כלי, להפעיל את הכלי ולטפל בתגובה; כל זה מתבצע בצד השרת
- ניהול מאובטח של נתונים – במקום לנהל את מצב השיחה בעצמך, אפשר לסמוך על שרשורים (threads) לאחסון כל המידע הנדרש
- כלים מוכנים מראש – כלים שניתן להשתמש בהם כדי לקיים אינטראקציה עם מקורות הנתונים שלך, כמו Bing, Azure AI Search ו-Azure Functions.

הכלים הזמינים בשירות Azure AI Agent מתחלקים לשתי קטגוריות:

1. כלים מבוססי ידע:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">עיגון עם חיפוש Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">חיפוש קבצים</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. כלים לפעולות:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">קריאת פונקציות</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">מפרש קוד</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">כלים מוגדרים ב-OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

שירות ה-Agent מאפשר לנו להשתמש בכלים אלו יחד כ`toolset`. הוא גם משתמש ב`threads` שמנטרים את היסטוריית ההודעות משיחה ספציפית.

תדמיינו שאתם סוכן מכירות בחברה בשם Contoso. אתם רוצים לפתח סוכן שיחה שיכול לענות על שאלות בנוגע לנתוני המכירה שלכם.

התמונה הבאה ממחישה כיצד ניתן להשתמש בשירות Azure AI Agent לניתוח נתוני המכירות:

![Agentic Service In Action](../../../translated_images/he/agent-service-in-action.34fb465c9a84659e.webp)

כדי להשתמש בכלים אלה עם השירות, ניתן ליצור לקוח ולהגדיר כלי או toolset. ליישום מעשי ניתן להשתמש בקוד פייתון הבא. ה-LLM יוכל לבחון את ה-toolset ולהחליט אם להשתמש בפונקציה שהמשתמש יצר, `fetch_sales_data_using_sqlite_query`, או במפרש הקוד המובנה בהתאם לבקשת המשתמש.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # פונקציית fetch_sales_data_using_sqlite_query שניתן למצוא בקובץ fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# אתחול סט הכלים
toolset = ToolSet()

# אתחול סוכן קריאת פונקציות עם הפונקציה fetch_sales_data_using_sqlite_query והוספתה לסט הכלים
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# אתחול כלי מפרש הקוד והוספתו לסט הכלים.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## מהן ההתחשבויות המיוחדות לשימוש בתבנית עיצוב שימוש בכלים לבניית סוכני AI אמינים?

חשש נפוץ לגבי SQL שנוצר דינמית על ידי LLMs הוא אבטחה, במיוחד הסיכון להזרקת SQL או פעולות זדוניות כגון מחיקה או מניפולציה במסד הנתונים. למרות חששות אלו תקפים, ניתן למזערם ביעילות על ידי הקונפיגורציה הנכונה של הרשאות גישה למסד הנתונים. ברוב מסדי הנתונים זה כולל הגדרת מסד הנתונים לקריאה בלבד. עבור שירותי מסדי נתונים כמו PostgreSQL או Azure SQL, יש להקצות לאפליקציה תפקיד קריאה בלבד (SELECT).
הרצת האפליקציה בסביבה מאובטחת משפרת עוד יותר את ההגנה. בתרחישים ארגוניים, הנתונים בדרך כלל נוצרים ומעובדים ממערכות תפעוליות למסד נתונים או מחסן נתונים לקריאה בלבד עם סכימה ידידותית למשתמש. גישה זו מבטיחה שהנתונים מאובטחים, מותאמים לביצועים ונגישות, ושהאפליקציה מוגבלת לגישה לקריאה בלבד.

## דוגמאות קוד

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## יש לך עוד שאלות על דפוסי עיצוב לכלי?

הצטרף ל-[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) כדי לפגוש לומדים נוספים, להשתתף בשעות קבלה ולקבל מענה לשאלות שלך בנושא סוכני AI.

## משאבים נוספים

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">סדנת שירות סוכני Azure AI</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">סדנת סוכנים מרובי כתיבה יצירתית של Contoso</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">מדריך קריאת פונקציות ב-Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">מתרגם קוד של Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">כלי Autogen</a>

## שיעור קודם

[הבנת דפוסי עיצוב סוכניים](../03-agentic-design-patterns/README.md)

## שיעור הבא

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדייק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי של אנשים. איננו אחראים לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->