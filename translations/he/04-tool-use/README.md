<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T17:51:25+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "he"
}
-->
[![איך לעצב סוכני AI טובים](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.he.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(לחצו על התמונה למעלה לצפייה בסרטון של השיעור הזה)_

# תבנית עיצוב שימוש בכלים

כלים הם מעניינים מכיוון שהם מאפשרים לסוכני AI להרחיב את טווח היכולות שלהם. במקום שלסוכן תהיה קבוצה מוגבלת של פעולות שהוא יכול לבצע, על ידי הוספת כלי, הסוכן יכול כעת לבצע מגוון רחב של פעולות. בפרק זה, נבחן את תבנית עיצוב שימוש בכלים, שמתארת כיצד סוכני AI יכולים להשתמש בכלים ספציפיים כדי להשיג את מטרותיהם.

## הקדמה

בשיעור זה, אנו מחפשים לענות על השאלות הבאות:

- מהי תבנית עיצוב שימוש בכלים?
- לאילו מקרי שימוש ניתן ליישם אותה?
- מהם האלמנטים/אבני הבניין הדרושים ליישום תבנית העיצוב?
- מהם השיקולים המיוחדים לשימוש בתבנית עיצוב שימוש בכלים לבניית סוכני AI אמינים?

## מטרות למידה

לאחר השלמת השיעור, תוכלו:

- להגדיר את תבנית עיצוב שימוש בכלים ואת מטרתה.
- לזהות מקרי שימוש שבהם תבנית עיצוב שימוש בכלים רלוונטית.
- להבין את האלמנטים המרכזיים הדרושים ליישום תבנית העיצוב.
- לזהות שיקולים להבטחת אמינות סוכני AI המשתמשים בתבנית עיצוב זו.

## מהי תבנית עיצוב שימוש בכלים?

**תבנית עיצוב שימוש בכלים** מתמקדת במתן יכולת ל-LLMs (מודלים שפתיים גדולים) לתקשר עם כלים חיצוניים כדי להשיג מטרות ספציפיות. כלים הם קוד שניתן להפעיל על ידי סוכן כדי לבצע פעולות. כלי יכול להיות פונקציה פשוטה כמו מחשבון, או קריאת API לשירות צד שלישי כמו חיפוש מחירי מניות או תחזית מזג אוויר. בהקשר של סוכני AI, כלים מתוכננים להיות מופעלים על ידי סוכנים בתגובה ל**קריאות פונקציה שנוצרו על ידי המודל**.

## לאילו מקרי שימוש ניתן ליישם אותה?

סוכני AI יכולים לנצל כלים כדי להשלים משימות מורכבות, לאחזר מידע או לקבל החלטות. תבנית עיצוב שימוש בכלים משמשת לעיתים קרובות בתרחישים הדורשים אינטראקציה דינמית עם מערכות חיצוניות, כמו מסדי נתונים, שירותי אינטרנט או מפרשי קוד. יכולת זו שימושית למספר מקרי שימוש שונים, כולל:

- **אחזור מידע דינמי:** סוכנים יכולים לשאול APIs חיצוניים או מסדי נתונים כדי לאחזר נתונים עדכניים (לדוגמה, שאילת מסד נתונים SQLite לניתוח נתונים, אחזור מחירי מניות או מידע על מזג אוויר).
- **ביצוע ופירוש קוד:** סוכנים יכולים להפעיל קוד או סקריפטים כדי לפתור בעיות מתמטיות, ליצור דוחות או לבצע סימולציות.
- **אוטומציה של תהליכים:** אוטומציה של תהליכים חוזרים או רב-שלביים על ידי שילוב כלים כמו מתזמני משימות, שירותי דוא"ל או צינורות נתונים.
- **תמיכה בלקוחות:** סוכנים יכולים לתקשר עם מערכות CRM, פלטפורמות כרטיסים או בסיסי ידע כדי לפתור שאלות משתמשים.
- **יצירה ועריכה של תוכן:** סוכנים יכולים לנצל כלים כמו בודקי דקדוק, מסכמי טקסטים או מעריכי בטיחות תוכן כדי לסייע במשימות יצירת תוכן.

## מהם האלמנטים/אבני הבניין הדרושים ליישום תבנית עיצוב שימוש בכלים?

אבני הבניין הללו מאפשרות לסוכן AI לבצע מגוון רחב של משימות. בואו נבחן את האלמנטים המרכזיים הדרושים ליישום תבנית עיצוב שימוש בכלים:

- **סכמות פונקציה/כלי:** הגדרות מפורטות של הכלים הזמינים, כולל שם הפונקציה, מטרתה, הפרמטרים הנדרשים והתוצאות הצפויות. סכמות אלו מאפשרות ל-LLM להבין אילו כלים זמינים וכיצד לבנות בקשות תקפות.

- **לוגיקת ביצוע פונקציה:** מגדירה כיצד ומתי כלים מופעלים בהתבסס על כוונת המשתמש והקשר השיחה. זה עשוי לכלול מודולי תכנון, מנגנוני ניתוב או זרימות מותנות שקובעות שימוש בכלים באופן דינמי.

- **מערכת ניהול הודעות:** רכיבים שמנהלים את זרימת השיחה בין קלטי המשתמש, תגובות LLM, קריאות כלים ותוצאות כלים.

- **מסגרת אינטגרציה של כלים:** תשתית שמחברת את הסוכן לכלים שונים, בין אם הם פונקציות פשוטות או שירותים חיצוניים מורכבים.

- **ניהול שגיאות ואימות:** מנגנונים לטיפול בכשלים בביצוע כלים, אימות פרמטרים וניהול תגובות בלתי צפויות.

- **ניהול מצב:** עוקב אחר הקשר השיחה, אינטראקציות קודמות עם כלים ונתונים מתמשכים כדי להבטיח עקביות באינטראקציות מרובות.

בהמשך, נבחן את קריאות הפונקציה/כלי בפירוט רב יותר.

### קריאות פונקציה/כלי

קריאת פונקציה היא הדרך העיקרית שבה אנו מאפשרים ל-LLMs לתקשר עם כלים. לעיתים קרובות תראו את המונחים 'פונקציה' ו'כלי' משמשים לסירוגין מכיוון ש'פונקציות' (בלוקים של קוד לשימוש חוזר) הן ה'כלים' שהסוכנים משתמשים בהם כדי לבצע משימות. כדי שקוד הפונקציה יופעל, LLM חייב להשוות את בקשת המשתמש לתיאור הפונקציה. לשם כך, סכימה המכילה את התיאורים של כל הפונקציות הזמינות נשלחת ל-LLM. ה-LLM בוחר את הפונקציה המתאימה ביותר למשימה ומחזיר את שמה ואת הפרמטרים שלה. הפונקציה שנבחרה מופעלת, תגובתה נשלחת חזרה ל-LLM, שמשתמש במידע כדי להגיב לבקשת המשתמש.

כדי שמפתחים יוכלו ליישם קריאת פונקציה עבור סוכנים, תצטרכו:

1. מודל LLM שתומך בקריאת פונקציות
2. סכימה המכילה תיאורי פונקציות
3. הקוד עבור כל פונקציה שמתוארת

בואו נשתמש בדוגמה של קבלת השעה הנוכחית בעיר כדי להמחיש:

1. **אתחול LLM שתומך בקריאת פונקציות:**

    לא כל המודלים תומכים בקריאת פונקציות, לכן חשוב לבדוק שה-LLM שבו אתם משתמשים כן תומך. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> תומך בקריאת פונקציות. ניתן להתחיל על ידי אתחול לקוח Azure OpenAI.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **יצירת סכימת פונקציה:**

    לאחר מכן נגדיר סכימת JSON שמכילה את שם הפונקציה, תיאור של מה שהפונקציה עושה, ושמות ותיאורים של הפרמטרים שלה. 
    לאחר מכן נעביר את הסכימה הזו ללקוח שיצרנו קודם, יחד עם בקשת המשתמש למצוא את השעה בסן פרנסיסקו. חשוב לציין שמה שמוחזר הוא **קריאת כלי**, **לא** התשובה הסופית לשאלה. כפי שצוין קודם, ה-LLM מחזיר את שם הפונקציה שהוא בחר למשימה ואת הפרמטרים שיועברו אליה.

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
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

    כעת, כשה-LLM בחר איזו פונקציה צריכה להתבצע, יש ליישם ולהפעיל את הקוד שמבצע את המשימה. 
    ניתן ליישם את הקוד לקבלת השעה הנוכחית בפייתון. כמו כן, נצטרך לכתוב את הקוד שמוציא את השם והפרמטרים מתוך response_message כדי לקבל את התוצאה הסופית.

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

קריאת פונקציות היא בלב רוב, אם לא כל, עיצובי שימוש בכלים של סוכנים, אך יישומה מאפס יכול להיות מאתגר לעיתים. 
כפי שלמדנו ב-[שיעור 2](../../../02-explore-agentic-frameworks) מסגרות סוכנים מספקות לנו אבני בניין מוכנות מראש ליישום שימוש בכלים.

## דוגמאות לשימוש בכלים עם מסגרות סוכנים

להלן כמה דוגמאות כיצד ניתן ליישם את תבנית עיצוב שימוש בכלים באמצעות מסגרות סוכנים שונות:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> היא מסגרת AI בקוד פתוח עבור מפתחים ב-.NET, פייתון וג'אווה העובדים עם מודלים שפתיים גדולים (LLMs). היא מפשטת את תהליך השימוש בקריאת פונקציות על ידי תיאור אוטומטי של הפונקציות והפרמטרים שלהן למודל באמצעות תהליך שנקרא <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializing</a>. היא גם מנהלת את התקשורת בין המודל לקוד שלכם. יתרון נוסף בשימוש במסגרת סוכנים כמו Semantic Kernel הוא שהיא מאפשרת לכם לגשת לכלים מוכנים מראש כמו <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> ו-<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

התרשים הבא ממחיש את תהליך קריאת הפונקציות עם Semantic Kernel:

![קריאת פונקציות](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.he.png)

ב-Semantic Kernel פונקציות/כלים נקראים <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. ניתן להמיר את פונקציית `get_current_time` שראינו קודם לפלאגין על ידי הפיכתה למחלקה עם הפונקציה בתוכה. ניתן גם לייבא את הדקורטור `kernel_function`, שמקבל את תיאור הפונקציה. כאשר יוצרים Kernel עם GetCurrentTimePlugin, ה-Kernel ייצור באופן אוטומטי את הסכימה לשליחה ל-LLM בתהליך.

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

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> היא מסגרת סוכנים חדשה יותר שמיועדת להעצים מפתחים לבנות, לפרוס ולסקור סוכני AI איכותיים ומורחבים בצורה מאובטחת, מבלי לנהל את משאבי המחשוב והאחסון הבסיסיים. היא שימושית במיוחד ליישומים ארגוניים מכיוון שהיא שירות מנוהל לחלוטין עם אבטחה ברמה ארגונית.

בהשוואה לפיתוח ישיר עם API של LLM, Azure AI Agent Service מספקת כמה יתרונות, כולל:

- קריאת כלים אוטומטית – אין צורך לנתח קריאת כלי, להפעיל את הכלי ולנהל את התגובה; כל זה נעשה כעת בצד השרת
- ניהול נתונים מאובטח – במקום לנהל את מצב השיחה בעצמכם, תוכלו להסתמך על threads לאחסון כל המידע הדרוש לכם
- כלים מוכנים מראש – כלים שניתן להשתמש בהם כדי לתקשר עם מקורות הנתונים שלכם, כמו Bing, Azure AI Search ו-Azure Functions.

הכלים הזמינים ב-Azure AI Agent Service יכולים להתחלק לשתי קטגוריות:

1. כלים מבוססי ידע:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding עם Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. כלים מבוססי פעולה:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">קריאת פונקציות</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">כלים מוגדרים על ידי OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

שירות הסוכנים מאפשר לנו להשתמש בכלים אלו יחד כ-`toolset`. הוא גם משתמש ב-`threads` שעוקבים אחר היסטוריית ההודעות משיחה מסוימת.

דמיינו שאתם סוכן מכירות בחברה בשם Contoso. אתם רוצים לפתח סוכן שיחה שיכול לענות על שאלות לגבי נתוני המכירות שלכם.

התמונה הבאה ממחישה כיצד תוכלו להשתמש ב-Azure AI Agent Service לניתוח נתוני המכירות שלכם:

![שירות סוכנים בפעולה](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.he.jpg)

כדי להשתמש בכל אחד מהכלים הללו עם השירות, ניתן ליצור לקוח ולהגדיר כלי או קבוצת כלים. כדי ליישם זאת באופן מעשי, ניתן להשתמש בקוד פייתון הבא. ה-LLM יוכל להסתכל על קבוצת הכלים ולהחליט האם להשתמש בפונקציה שנוצרה על ידי המשתמש, `fetch_sales_data_using_sqlite_query`, או ב-Code Interpreter המוכן מראש, בהתאם לבקשת המשתמש.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## מהם השיקולים המיוחדים לשימוש בתבנית עיצוב שימוש בכלים לבניית סוכני AI אמינים?

דאגה נפוצה עם SQL שנוצר באופן דינמי על ידי LLMs היא אבטחה, במיוחד הסיכון להזרקת SQL או פעולות זדוניות, כמו מחיקת או שינוי מסד הנתונים. בעוד שדאגות אלו תקפות, ניתן להתמודד איתן ביעילות על ידי הגדרת הרשאות גישה למסד הנתונים בצורה נכונה. עבור רוב מסדי הנתונים, זה כולל הגדרת המסד כקריאה בלבד. עבור שירותי מסדי נתונים כמו PostgreSQL או Azure SQL, האפליקציה צריכה להיות מוקצית תפקיד קריאה בלבד (SELECT).
הרצת האפליקציה בסביבה מאובטחת משפרת עוד יותר את ההגנה. בתרחישים ארגוניים, נתונים בדרך כלל נשלפים ומעובדים ממערכות תפעוליות לתוך מסד נתונים לקריאה בלבד או מחסן נתונים עם סכימה ידידותית למשתמש. גישה זו מבטיחה שהנתונים מאובטחים, מותאמים לביצועים ונגישות, ושלאפליקציה יש גישה מוגבלת לקריאה בלבד.

## דוגמאות קוד

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## יש לכם עוד שאלות על דפוסי עיצוב לשימוש בכלי?

הצטרפו ל-[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) כדי לפגוש לומדים אחרים, להשתתף בשעות קבלה ולקבל תשובות לשאלות שלכם על AI Agents.

## משאבים נוספים

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">סדנת Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">סדנת Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">מדריך קריאה לפונקציות ב-Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">מפרש קוד ב-Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">כלי Autogen</a>

## שיעור קודם

[הבנת דפוסי עיצוב סוכנים](../03-agentic-design-patterns/README.md)

## שיעור הבא

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי בני אדם. איננו נושאים באחריות לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->