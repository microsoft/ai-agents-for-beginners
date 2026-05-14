[![כיצד לעצב סוכני AI טובים](../../../translated_images/he/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(לחץ על התמונה למעלה לצפייה בסרטון של השיעור)_

# תבנית עיצוב שימוש בכלים

כלים מעניינים כי הם מאפשרים לסוכני AI להחזיק במגוון רחב יותר של יכולות. במקום שלסוכן יש סט מוגבל של פעולות שהוא יכול לבצע, על ידי הוספת כלי, הסוכן יכול עכשיו לבצע מגוון רחב של פעולות. בפרק זה נבחן את תבנית העיצוב שימוש בכלים, שמתארת כיצד סוכני AI יכולים להשתמש בכלים מסוימים כדי להשיג את מטרותיהם.

## מבוא

בשיעור זה אנו רוצים לענות על השאלות הבאות:

- מהי תבנית העיצוב שימוש בכלי?
- באילו מקרים ניתן ליישם אותה?
- מהם האלמנטים/גושי הבניה הנדרשים ליישום תבנית העיצוב?
- מהם השיקולים המיוחדים לשימוש בתבנית עיצוב שימוש בכלים לבניית סוכני AI אמינים?

## מטרות הלמידה

לאחר השלמת שיעור זה, תוכל:

- להגדיר את תבנית העיצוב שימוש בכלים ואת מטרתה.
- לזהות מקרים בהם תבנית העיצוב שימוש בכלים ישימה.
- להבין את האלמנטים המרכזיים הנדרשים ליישום תבנית העיצוב.
- להכיר את השיקולים להבטחת האמינות של סוכני AI המשתמשים בתבנית עיצוב זו.

## מהי תבנית העיצוב שימוש בכלי?

תבנית העיצוב **שימוש בכלי** מתמקדת במתן יכולת למודלים גדולים של שפה (LLMs) לקיים אינטראקציה עם כלים חיצוניים כדי להשיג מטרות ספציפיות. כלים הם קוד שניתן להפעיל על-ידי סוכן לביצוע פעולות. כלי יכול להיות פונקציה פשוטה כמו מחשבון, או קריאת API לשירות צד שלישי כמו חיפוש מחירי מניות או תחזית מזג אוויר. בהקשר של סוכני AI, הכלים מיועדים להתבצע על ידי סוכנים בתגובה ל**קריאות פונקציה שנוצרו על ידי המודל**.

## באילו מקרים ניתן ליישם את תבנית העיצוב?

סוכני AI יכולים לנצל כלים כדי להשלים משימות מורכבות, לשלוף מידע, או לקבל החלטות. תבנית העיצוב שימוש בכלים משמשת לעיתים קרובות בסצenarיות הדורשים אינטראקציה דינמית עם מערכות חיצוניות, כגון בסיסי נתונים, שירותי רשת, או מפרשים של קוד. יכולת זו שימושית למספר מקרים שונים הכוללים:

- **שליפת מידע דינמית:** סוכנים יכולים לשאול APIs חיצוניים או בסיסי נתונים כדי לקבל נתונים מעודכנים (למשל, שאילתא על בסיס נתונים SQLite לניתוח נתונים, שליפת מחירי מניות או מידע על מזג אוויר).
- **הפעלה ופרשנות של קוד:** סוכנים יכולים להפעיל קוד או סקריפטים כדי לפתור בעיות מתמטיות, ליצור דוחות, או להריץ סימולציות.
- **אוטומציה של זרימות עבודה:** אוטומציה של משימות חזרתיות או רב-שלביות באמצעות שילוב כלים כמו מתזמנים, שירותי דואר אלקטרוני, או צינורות נתונים.
- **תמיכה בלקוחות:** סוכנים יכולים לקיים אינטראקציה עם מערכות CRM, פלטפורמות ניהול פניות, או מאגרי ידע כדי לפתור שאלות משתמשים.
- **יצירה ועריכת תוכן:** סוכנים יכולים להשתמש בכלים כמו בודקי דקדוק, מסכמים של טקסט, או מערכות להערכת בטיחות תוכן כדי לסייע במשימות יצירת תוכן.

## מהם האלמנטים/גושי הבניה הנדרשים ליישם את תבנית העיצוב שימוש בכלים?

גושי הבנייה הללו מאפשרים לסוכן AI לבצע מגוון רחב של משימות. נבחן את האלמנטים המרכזיים הנדרשים ליישום תבנית העיצוב שימוש בכלים:

- **סכמות פונקציות/כלים**: הגדרות מפורטות של הכלים הזמינים, כולל שם הפונקציה, המטרה, הפרמטרים הנדרשים, והפלט הצפוי. סכמות אלו מאפשרות ל-LLM להבין אילו כלים זמינים וכיצד לבנות בקשות תקפות.

- **לוגיקת הפעלת פונקציות**: קובעת מתי ואיך הכלים מופעלים בהתאם לכוונת המשתמש והקשר השיחה. זה יכול לכלול מודולים לתכנון, מכניזמים להפניית בקשות, או זרמים מותנים שקובעים את השימוש בכלים בדינמיות.

- **מערכת ניהול הודעות**: רכיבים שמנהלים את זרימת השיחה בין כניסות המשתמש, תגובות ה-LLM, קריאות הכלים ותוצאותיהם.

- **מסגרת אינטגרציה של כלים**: תשתית שמחברת את הסוכן לכלים שונים, בין אם פונקציות פשוטות או שירותים חיצוניים מורכבים.

- **ניהול שגיאות ואימות**: מנגנונים לטיפול בכישלונות בהפעלת כלים, אימות פרמטרים, וניהול תגובות לא צפויות.

- **ניהול מצב**: עוקב אחרי הקשר השיחה, אינטראקציות קודמות עם כלים ונתונים מתמשכים כדי להבטיח עקביות לאורך אינטראקציות מרובות.

בהמשך נבחן את קריאת פונקציות/כלים בפירוט רב יותר.

### קריאת פונקציות/כלים

קריאת פונקציות היא הדרך העיקרית שמאפשרת למודלים גדולים של שפה (LLMs) לקיים אינטראקציה עם כלים. ברוב המקרים תראה את המונחים 'פונקציה' ו'כלי' משמשים לסירוגין כי 'פונקציות' (גושי קוד חוזר) הן ה'כלים' שסוכנים משתמשים בהם לביצוע משימות. כדי שקוד של פונקציה יופעל, על ה-LLM להשוות בין בקשת המשתמש לתיאור הפונקציות. לשם כך נשלחת ל-LLM סכימה שמכילה את התיאורים של כל הפונקציות הזמינות. ה-LLM מחליף את הפונקציה המתאימה ביותר למשימה ומחזיר את שמה ואת הפרמטרים שלה. הפונקציה שנבחרה מופעלת, תגובתה נשלחת חזרה ל-LLM, שמשתמש במידע כדי להגיב לבקשת המשתמש.

כדי שמפתחים יוכלו ליישם קריאת פונקציות לסוכנים, יידרשו:

1. מודל LLM שתומך בקריאת פונקציות
2. סכימה המכילה תיאורי פונקציות
3. הקוד עבור כל פונקציה שתוארה

נשתמש בדוגמא של קבלת השעה הנוכחית בעיר כדי להמחיש:

1. **אתחול LLM שתומך בקריאת פונקציות:**

    לא כל הדגמים תומכים בקריאת פונקציות, לכן חשוב לבדוק שה-LLM שבו משתמשים אכן תומך. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> תומך בקריאת פונקציות. אפשר להתחיל ביצירת לקוח Azure OpenAI. 

    ```python
    # אתחול לקוח Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **יצירת סכימת פונקציה:**

    לאחר מכן נגדיר סכימת JSON שכוללת את שם הפונקציה, תיאור מה הפונקציה עושה, ושמות ותיאורים של פרמטרי הפונקציה.
    נשלח את הסכימה ללקוח שנוצר קודם, יחד עם בקשת המשתמש למצוא את השעה בסן פרנסיסקו. חשוב לציין ש**קריאת כלי** היא מה שמוחזר, **ולא** התשובה הסופית לשאלה. כפי שצויין קודם, ה-LLM מחזיר את שם הפונקציה שנבחרה למשימה והארגומנטים שיועברו אליה.

    ```python
    # תיאור הפונקציה לקריאת המודל
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
  
    # הודעת משתמש ראשונית
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # קריאת API ראשונה: לבקש מהמודל להשתמש בפונקציה
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # עיבוד התגובה של המודל
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **קוד הפונקציה הדרוש להשלמת המשימה:**

    כעת כאשר ה-LLM בחר איזו פונקציה להריץ, יש ליישם ולהריץ את הקוד שמבצע את המשימה.
    ניישם את הקוד לקבלת השעה הנוכחית בפייתון. נצטרך גם לכתוב קוד להוצאת השם והארגומנטים מתוך response_message כדי לקבל את התוצאה הסופית.

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
     # טיפול בקריאות פונקציה
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
  
      # קריאת API שנייה: קבלת התגובה הסופית מהמודל
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

קריאת פונקציות היא ליבת רוב, אם לא כל, תבניות העיצוב של שימוש בכלים לסוכנים, אולם יישום שלה מאפס יכול לעיתים להיות מאתגר.
כפי שלמדנו ב-[שיעור 2](../../../02-explore-agentic-frameworks), מסגרות סוכנים נותנות לנו גושי בניה מוכנים מראש ליישום שימוש בכלים.

## דוגמאות לשימוש בכלים עם מסגרות סוכנים

להלן כמה דוגמאות איך ניתן ליישם את תבנית העיצוב שימוש בכלים באמצעות מסגרות סוכנים שונות:

### מסגרת הסוכנים של מיקרוסופט

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> היא מסגרת AI בקוד פתוח לבניית סוכני AI. היא מפשטת את התהליך של קריאת פונקציות על-ידי מתן אפשרות להגדיר כלים כפונקציות Python עם הדקורטור `@tool`. המסגרת מטפלת בתקשורת הלוך ושוב בין המודל והקוד שלך. היא גם מספקת גישה לכלים מוכנים מראש כגון חיפוש קבצים ומפרש קוד באמצעות `AzureAIProjectAgentProvider`.

הדיאגרמה הבאה ממחישה את תהליך קריאת הפונקציות במסגרת הסוכנים של מיקרוסופט:

![function calling](../../../translated_images/he/functioncalling-diagram.a84006fc287f6014.webp)

במסגרת הסוכנים של מיקרוסופט, כלים מוגדרים כפונקציות עם הדקורטור. ניתן להפוך את פונקציית `get_current_time` שראינו קודם לכלי על-ידי שימוש בדקורטור `@tool`. המסגרת תסדר באופן אוטומטי את הפונקציה ופרמטריה, ותיצור את הסכימה לשליחה ל-LLM.

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

# צור סוכן והרץ עם הכלי
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### שירות סוכני Azure AI

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> היא מסגרת סוכנים חדשה שנועדה להעצים מפתחים לבנות, לפרוס ולשדרג בקלות סוכני AI איכותיים, גמישים ובטוחים מבלי הצורך לנהל משאבי מחשוב ואחסון בתשתית. היא שימושית במיוחד לאפליקציות ארגוניות מאחר והיא שירות מנוהל במלואו עם אבטחה ברמה ארגונית.

בהשוואה לפיתוח ישיר עם API של LLM, Azure AI Agent Service מציעה יתרונות כגון:

- קריאה אוטומטית לכלים – אין צורך לפרש קריאת כלי, להפעיל את הכלי ולטפל בתגובה; כל זה מתבצע בשרת
- ניהול מאובטח של נתונים – במקום לנהל את מצב השיחה בעצמך, ניתן להסתמך על 'threads' לשמירת כל המידע הדרוש
- כלים מוכנים לשימוש – כלים שמאפשרים אינטראקציה עם מקורות הנתונים שלך, כמו Bing, Azure AI Search ו-Azure Functions.

הכלים הזמינים בשירות סוכני Azure AI מחולקים לשתי קטגוריות:

1. כלים ידע:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">אפשרות עיגון עם חיפוש Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">חיפוש קבצים</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. כלים פעולה:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">קריאת פונקציות</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">מפרש קוד</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">כלים מוגדרים עם OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

שירות הסוכן מאפשר להשתמש בכלים אלו יחד כ'toolset'. השירות גם משתמש ב-'threads' ששומרים על היסטוריית ההודעות משיחה מסוימת.

דמיין שאתה סוכן מכירות בחברה בשם Contoso. אתה רוצה לפתח סוכן שיחה שיכול לענות על שאלות לגבי נתוני המכירות שלך.

התמונה הבאה ממחישה כיצד ניתן להשתמש בשירות סוכני Azure AI כדי לנתח את נתוני המכירות:

![Agentic Service In Action](../../../translated_images/he/agent-service-in-action.34fb465c9a84659e.webp)

כדי להשתמש בכל הכלים עם השירות, ניתן ליצור לקוח ולהגדיר כלי או toolset. ליישום מעשי נוכל להשתמש בקוד הפייתון הבא. ה-LLM יוכל להסתכל על ה-toolset ולהחליט האם להשתמש בפונקציה שיצר המשתמש, `fetch_sales_data_using_sqlite_query`, או במפרש הקוד המובנה בהתאם לבקשת המשתמש.

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

# לאתחל את ערכת הכלים
toolset = ToolSet()

# אתחול סוכן קריאת פונקציות עם הפונקציה fetch_sales_data_using_sqlite_query והוספתה לערכת הכלים
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# אתחול כלי Interpreter Code והוספתו לערכת הכלים.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## מהם השיקולים המיוחדים לשימוש בתבנית העיצוב שימוש בכלים לבניית סוכני AI אמינים?

חשש נפוץ בכתיבת שאילתות SQL דינמיות על ידי LLMs הוא בטיחות, בפרט הסיכון להזרקת SQL או פעולות זדוניות, כמו מחיקת או שינוי נתוני בסיס הנתונים. בעוד שהחששות האלה תקפים, ניתן למזערם ביעילות על-ידי תצורת הרשאות גישה מתאימה לבסיס הנתונים. ברוב בסיסי הנתונים, הדבר כרוך בהגדרת גישת קריאה בלבד (read-only). עבור שירותי בסיסי נתונים כמו PostgreSQL או Azure SQL, יש להקצות לאפליקציה תפקיד קריאה בלבד (SELECT).

הרצת האפליקציה בסביבה מאובטחת משפרת גם את ההגנה. בסביבות ארגוניות, נתונים בדרך כלל מחולצים ומעובדים ממערכות תפעוליות אל בסיס נתונים או מחסן נתונים בקריאה בלבד עם סכימה ידידותית למשתמש. גישה זו מבטיחה שהנתונים מאובטחים, מותאמים לביצועים ולנגישות, ושלאפליקציה יש גישה מוגבלת לקריאה בלבד.

## קודים לדוגמה

- פייתון: [מסגרת סוכנים](./code_samples/04-python-agent-framework.ipynb)
- .NET: [מסגרת סוכנים](./code_samples/04-dotnet-agent-framework.md)

## יש לך שאלות נוספות על תבניות עיצוב שימוש בכלים?

הצטרף ל-[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) כדי לפגוש לומדים אחרים, להשתתף בשעות משרד ולקבל תשובות לשאלותיך בנושא סוכני AI.

## משאבים נוספים

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">סדנת שירות סוכני Azure AI</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">סדנת כתיבת רב-סוכנים Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">סקירת מסגרת סוכני מיקרוסופט</a>

## שיעור קודם

[הבנת תבניות עיצוב סוכנים](../03-agentic-design-patterns/README.md)

## שיעור הבא
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->