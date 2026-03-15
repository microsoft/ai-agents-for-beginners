[![איך לעצב סוכני בינה מלאכותית טובים](../../../translated_images/he/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(לחץ על התמונה למעלה לצפייה בסרטון של השיעור)_

# דפוס העיצוב לשימוש בכלים

כלים מעניינים מכיוון שהם מאפשרים לסוכני בינה מלאכותית טיפוס רחב יותר של יכולות. במקום שהסוכן יוגבל למערך פעולות מצומצם שהוא יכול לבצע, על ידי הוספת כלי, הסוכן יכול כעת לבצע מגוון רחב של פעולות. בפרק זה נבחן את דפוס העיצוב לשימוש בכלים, המתאר כיצד סוכני בינה מלאכותית יכולים להשתמש בכלים ספציפיים כדי להשיג את מטרותיהם.

## מבוא

בשיעור זה אנו מנסים לענות על השאלות הבאות:

- מהו דפוס העיצוב לשימוש בכלים?
- באילו תרחישים ניתן ליישם אותו?
- מהם האלמנטים/בלוקי הבנייה הדרושים ליישום דפוס העיצוב?
- מהם השיקולים המיוחדים לשימוש בדפוס העיצוב לשימוש בכלים כדי לבנות סוכני בינה אמינים?

## מטרות למידה

לאחר השלמת שיעור זה, תוכל/י:

- להגדיר את דפוס העיצוב לשימוש בכלים ואת מטרתו.
- לזהות תרחישי שימוש שבהם דפוס העיצוב לשימוש בכלים רלוונטי.
- להבין את האלמנטים המרכזיים הדרושים ליישום דפוס העיצוב.
- להכיר שיקולים להבטחת אמינות בסוכנים המשתמשים בדפוס עיצוב זה.

## מהו דפוס העיצוב לשימוש בכלים?

הדפוס **דפוס העיצוב לשימוש בכלים** מתמקד במתן היכולת ל-LLMs לקיים אינטראקציה עם כלים חיצוניים על מנת להשיג מטרות ספציפיות. כלים הם קוד שניתן לבצע על-ידי סוכן כדי לבצע פעולות. כלי יכול להיות פונקציה פשוטה כמו מחשבון, או קריאת API לשירות צד שלישי כמו בדיקת מחיר מניה או תחזית מזג אוויר. בהקשר של סוכני בינה מלאכותית, כלים מעוצבים כך שיופעלו על-ידי סוכנים בתגובה ל**קריאות לפונקציות שנוצרות על ידי המודל**.

## באילו תרחישים ניתן ליישם אותו?

סוכני בינה מלאכותית יכולים לנצל כלים כדי להשלים משימות מורכבות, לשלוף מידע או לקבל החלטות. דפוס העיצוב לשימוש בכלים משמש לעתים קרובות בתרחישים הדורשים אינטראקציה דינמית עם מערכות חיצוניות, כגון מסדי נתונים, שירותי רשת או מפרשי קוד. יכולת זו שימושית למספר מקרים שונים הכוללים:

- **שליפת מידע דינאמית:** סוכנים יכולים לשאול APIs חיצוניים או מסדי נתונים כדי לאחזר נתונים מעודכנים (למשל, שאילתה למסד נתונים SQLite לניתוח נתונים, שליפת מחירי מניות או מידע מזג אוויר).
- **הרצת קוד ופירושו:** סוכנים יכולים להריץ קוד או סקריפטים כדי לפתור בעיות מתמטיות, ליצור דוחות או לבצע סימולציות.
- **אוטומציה של זרימות עבודה:** אוטומציה של תהליכים חוזרים או מרובי שלבים על-ידי אינטגרציה של כלים כמו מתזמני משימות, שירותי דואר אלקטרוני או צינורות נתונים.
- **תמיכת לקוחות:** סוכנים יכולים לקיים אינטראקציה עם מערכות CRM, פלטפורמות ניהול כרטיסים או מאגרי ידע כדי לפתור פניות משתמשים.
- **יצירה ועריכה של תוכן:** סוכנים יכולים להשתמש בכלים כמו בודקי דקדוק, מסכמי טקסט או מעריכי בטיחות תכנים כדי לסייע במשימות יצירת תוכן.

## מהם האלמנטים/בלוקי הבנייה הדרושים ליישום דפוס העיצוב לשימוש בכלים?

בלוקי הבנייה הללו מאפשרים לסוכן הבינה לבצע מגוון רחב של משימות. בואו נסתכל על המרכיבים המרכזיים הדרושים ליישום דפוס העיצוב לשימוש בכלים:

- **סכמות של פונקציות/כלים**: הגדרות מפורטות של הכלים הזמינים, כולל שם הפונקציה, מטרתה, הפרמטרים הנדרשים והתפוקות הצפויות. סכמות אלה מאפשרות ל-LLM להבין אילו כלים זמינים ואיך ליצור בקשות תקפות.
- **לוגיקת ביצוע פונקציות**: קובעת כיצד ומתי קוראים לכלים בהתבסס על כוונת המשתמש והקשר השיחה. זה יכול לכלול מודולי תכנון, מנגנוני ניתוב או זרימות מותנות שמקבלות החלטה על שימוש בכלים בדינמיקה.
- **מערכת ניהול הודעות**: רכיבים שמנהלים את זרימת השיחה בין קלטי המשתמש, תגובות ה-LLM, קריאות לכלים ותוצאות הכלים.
- **מסגרת לאינטגרציה של כלים**: תשתית שמחברת את הסוכן לכלים שונים, בין אם מדובר בפונקציות פשוטות או בשירותים חיצוניים מורכבים.
- **טיפול בשגיאות ואימות**: מנגנונים לטיפול בכשלים בביצוע כלי, אימות פרמטרים וניהול תגובות בלתי צפויות.
- **ניהול מצב**: מעקב אחרי הקשר השיחה, אינטראקציות קודמות עם כלים ונתונים מתמשכים כדי להבטיח עקביות לאורך אינטראקציות מרובות סבבים.

בהמשך, נבחן את קריאת פונקציות/כלים בפירוט רב יותר.
 
### קריאת פונקציות/כלים

קריאת פונקציות היא הדרך העיקרית שמאפשרת למודלים לשפה גדולים (LLMs) לקיים אינטראקציה עם כלים. תתקל לעתים קרובות בשימוש במונחים 'Function' ו-'Tool' לסירוגין כי 'functions' (בלוקים של קוד שניתן לשימוש חוזר) הם ה'כלים' שהסוכנים משתמשים בהם כדי לבצע משימות. כדי שניתן יהיה לקרוא לקוד של פונקציה, ה-LLM חייב להשוות את בקשת המשתמש לתיאור הפונקציות. לשם כך נשלחת ל-LLM סכמה המכילה את התיאורים של כל הפונקציות הזמינות. ה-LLM ואז בוחר את הפונקציה המתאימה ביותר למשימה ומחזיר את שמה ואת הטיעונים שלה. הפונקציה שנבחרה מופעלת, התגובה שלה נשלחת חזרה ל-LLM, שהופך את המידע לתשובה לבקשת המשתמש.

כדי שמפתחים יוכלו ליישם קריאת פונקציות עבור סוכנים, תצטרכו:

1. מודל LLM שתומך בקריאת פונקציות
2. סכמה המכילה תיאורי פונקציות
3. הקוד עבור כל פונקציה שמתוארת

בואו נשתמש בדוגמה של קבלת השעה הנוכחית בעיר להמחשה:

1. **אתחול מודל LLM שתומך בקריאת פונקציות:**

    לא כל הדגמים תומכים בקריאת פונקציות, לכן חשוב לבדוק שה-LLM שבו אתם משתמשים תומך בכך.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> תומך בקריאת פונקציות. נוכל להתחיל על-ידי איתחול הלקוח של Azure OpenAI. 

    ```python
    # אתחל את לקוח Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **יצירת סכמה של פונקציה**:

    לאחר מכן נגדיר סכמה ב-JSON שמכילה את שם הפונקציה, תיאור מה הפונקציה עושה, ושמות ותיאורים של פרמטרי הפונקציה.
    לאחר מכן נעביר סכמה זו ללקוח שנוצר קודם, יחד עם בקשת המשתמש למצוא את השעה בסן פרנסיסקו. מה שחשוב לציין הוא שקריאת כלי היא מה שמוחזר, ולא התשובה הסופית לשאלה. כפי שהוזכר קודם, ה-LLM מחזיר את שם הפונקציה שבחר למשימה ואת הטיעונים שיעברו אליה.

    ```python
    # תיאור פונקציה לקריאה על ידי המודל
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
  
    # הודעת המשתמש הראשונית
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # קריאת API ראשונית: בקש מהמודל להשתמש בפונקציה
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # עבד את תגובת המודל
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **הקוד של הפונקציה הנדרש לביצוע המשימה:**

    עכשיו כאשר ה-LLM בחר איזו פונקציה יש להריץ, יש ליישם ולהריץ את הקוד שמבצע את המשימה.
    נוכל לממש את הקוד לקבלת השעה הנוכחית ב-Python. נצטרך גם לכתוב את הקוד לחלץ את השם והארגומנטים מתוך response_message כדי לקבל את התוצאה הסופית.

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
     # טפל בקריאות לפונקציות
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
  
      # קריאת API שנייה: קבל את התגובה הסופית מהמודל
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

קריאת פונקציות היא בלב רוב, אם לא כל, יישומי דפוס העיצוב לשימוש בכלים, אך יישום שלה מאפס יכול להיות מאתגר לעיתים.
כפי שלמדנו ב-[שיעור 2](../../../02-explore-agentic-frameworks), מסגרות agentic מספקות לנו בלוקים שבנו מראש כדי ליישם שימוש בכלים.
 
## דוגמאות לשימוש בכלים עם מסגרות agentic

להלן כמה דוגמאות לאופן שבו ניתן ליישם את דפוס העיצוב לשימוש בכלים באמצעות מסגרות agentic שונות:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> היא מסגרת AI קוד-פתוח לבניית סוכני בינה מלאכותית. היא מפשטת את תהליך קריאת הפונקציות על-ידי כך שהיא מאפשרת להגדיר כלים כפונקציות Python עם הדקורטור `@tool`. המסגרת מטפלת בתקשורת הלוך-ושוב בין המודל לבין הקוד שלכם. היא גם מספקת גישה לכלים מובנים מראש כמו חיפוש קבצים (File Search) ומפרש קוד (Code Interpreter) דרך ה-`AzureAIProjectAgentProvider`.

הדיאגרמה הבאה ממחישה את תהליך קריאת הפונקציות עם Microsoft Agent Framework:

![קריאת פונקציות](../../../translated_images/he/functioncalling-diagram.a84006fc287f6014.webp)

ב-Microsoft Agent Framework, כלים מוגדרים כפונקציות עם דקורטורים. אנו יכולים להמיר את הפונקציה `get_current_time` שראינו קודם לכלי על-ידי שימוש בדקורטור `@tool`. המסגרת תסדר באופן אוטומטי את הפונקציה ואת הפרמטרים שלה, ותייצר את הסכמה שתשלח ל-LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# צור את הלקוח
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# צור סוכן והרץ אותו באמצעות הכלי
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> היא מסגרת סוכנים חדשה יותר שמטרתה להעצים מפתחים לבנות, לפרוס ולשכפל סוכני בינה איכותיים ומורחבים בצורה מאובטחת, ללא צורך בניהול המשאבים המחשוביים והאחסון הבסיסיים. היא שימושית במיוחד לאפליקציות ארגוניות שכן היא שירות מנוהל לחלוטין ברמת אבטחה ארגונית.

בהשוואה לפיתוח ישיר עם API של LLM, Azure AI Agent Service מספקת כמה יתרונות, כולל:

- קריאה אוטומטית לכלים – אין צורך לנתח קריאת כלי, להפעיל את הכלי ולנהל את התגובה; כל זאת מתבצע כעת בצד השרת
- ניהול נתונים מאובטח – במקום לנהל את מצב השיחה בעצמכם, ניתן להסתמך על threads לאחסון כל המידע הדרוש
- כלים מוכנים לשימוש – כלים שניתן להשתמש בהם כדי לאינטראקט עם מקורות הנתונים שלכם, כגון Bing, Azure AI Search ו-Azure Functions.

הכלים הזמינים ב-Azure AI Agent Service ניתנים לחלוקה לשתי קטגוריות:

1. כלים לידע:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">עיגון עם חיפוש Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">חיפוש קבצים</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. כלים לפעולה:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">קריאת פונקציות</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">מפרש קוד</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">כלים המוגדרים ב-OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

שירות הסוכנים מאפשר לנו להשתמש בכלים אלה יחד כ-`toolset`. הוא גם מנצל `threads` שמתעדים את היסטוריית ההודעות משיחה מסוימת.

דמיינו שאתם נציגי מכירות בחברה בשם Contoso. אתם רוצים לפתח סוכן שיחה שיכול לענות על שאלות אודות נתוני המכירות שלכם.

התמונה הבאה ממחישה כיצד ניתן להשתמש ב-Azure AI Agent Service כדי לנתח את נתוני המכירות שלכם:

![שירות סוכני בפעולה](../../../translated_images/he/agent-service-in-action.34fb465c9a84659e.webp)

כדי להשתמש בכלים אלה עם השירות ניתן ליצור לקוח ולהגדיר כלי או toolset. ליישום מעשי ניתן להשתמש בקוד Python הבא. ה-LLM יוכל להסתכל על ה-toolset ולהחליט האם להשתמש בפונקציה שיצר המשתמש, `fetch_sales_data_using_sqlite_query`, או במפרש הקוד המובנה בהתאם לבקשת המשתמש.

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

# אתחול ערכת כלים
toolset = ToolSet()

# אתחול סוכן שמפעיל פונקציות עם הפונקציה fetch_sales_data_using_sqlite_query והוספתו לערכת הכלים
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# אתחול כלי מפרש הקוד והוספתו לערכת הכלים.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## מהם השיקולים המיוחדים לשימוש בדפוס העיצוב לשימוש בכלים כדי לבנות סוכני בינה אמינים?

דאגה נפוצה לגבי SQL שנוצר באופן דינמי על-ידי LLMs היא אבטחה, במיוחד הסיכון של SQL injection או פעולות זדוניות, כגון מחיקה או מניפולציה של בסיס הנתונים. בעוד שדאגות אלה מוצדקות, ניתן להפחית אותן ביעילות על-ידי קביעת הרשאות גישה למסד הנתונים כראוי. עבור רוב מסדי הנתונים זה כולל קונפיגורציה של מסד הנתונים במצב קריאה בלבד. עבור שירותי מסדי נתונים כמו PostgreSQL או Azure SQL, יש להקצות לאפליקציה תפקיד קריאה בלבד (SELECT).

הרצת האפליקציה בסביבה מאובטחת מחזקת עוד יותר את ההגנה. בתרחישים ארגוניים, הנתונים בדרך כלל מופקים ומעובדים ממערכות תפעוליות אל מסד נתונים לקריאה בלבד או לאחסון נתונים (data warehouse) עם סכימה ידידותית למשתמש. גישה זו מבטיחה שהנתונים מאובטחים, מותאמים לביצועים ונגישים, וכי לאפליקציה יש גישה מוגבלת לקריאה בלבד.

## קודי דוגמה

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## יש לך שאלות נוספות לגבי דפוסי העיצוב לשימוש בכלים?

הצטרפו ל-[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) כדי להיפגש עם לומדים נוספים, להשתתף בשעות מענה ולקבל תשובות על שאלותיכם בנושא סוכני בינה מלאכותית.

## משאבים נוספים

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">סדנת Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">סדנת Contoso Creative Writer עבור סוכני Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">סקירת Microsoft Agent Framework</a>

## שיעור קודם

[הבנת דפוסי עיצוב סוכניים](../03-agentic-design-patterns/README.md)

## השיעור הבא
[סוכני RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
הצהרת אי-אחריות:
מסמך זה תורגם באמצעות שירות תרגום בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). אף שאנו שואפים לדיוק, יש לשים לב כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש לראות במסמך המקורי בשפתו כמקור הסמכותי. לגבי מידע קריטי, מומלץ להסתייע בתרגום מקצועי שנערך על ידי מתרגם אנושי. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->