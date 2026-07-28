# חקר מסגרת Microsoft Agent  

![Agent Framework](../../../translated_images/he/lesson-14-thumbnail.90df0065b9d234ee.webp)

### הקדמה  

שיעור זה יכסה:  

- הבנת מסגרת Microsoft Agent: תכונות מפתח וערך  
- חקר המושגים המרכזיים של מסגרת Microsoft Agent  
- דפוסי MAF מתקדמים: זרימות עבודה, middleware וזיכרון  

## מטרות הלמידה  

לאחר סיום שיעור זה, תדע כיצד:  

- לבנות סוכני AI מוכנים לייצור באמצעות מסגרת Microsoft Agent  
- ליישם את התכונות המרכזיות של מסגרת Microsoft Agent למקרי שימוש סוכניים שלך  
- להשתמש בדפוסים מתקדמים הכוללים זרימות עבודה, middleware ותצפית  

## דוגמאות קוד  

דוגמאות קוד ל-[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) נמצאות במאגר זה תחת הקבצים `xx-python-agent-framework` ו- `xx-dotnet-agent-framework`.  

## הבנת מסגרת Microsoft Agent  

![Framework Intro](../../../translated_images/he/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) היא מסגרת מאוחדת של מיקרוסופט לבניית סוכני AI. היא מציעה גמישות להתמודדות עם מגוון רחב של מקרי שימוש סוכניים שנראים הן בייצור והן בסביבות מחקר, כולל:  

- **תזמור סוכנים רציף** בתרחישים בהם דרושות זרימות עבודה שלב-אחר-שלב.  
- **תזמור מקביל** בתרחישים בהם סוכנים צריכים להשלים משימות בו-זמנית.  
- **תזמור שיחה קבוצתית** בתרחישים בהם סוכנים יכולים לשתף פעולה יחד על משימה אחת.  
- **תזמור מסירת משימות** בתרחישים בהם הסוכנים מעבירים את המשימה זה לזה כאשר המשימות המשניות הושלמו.  
- **תזמור מגנטי** בתרחישים בהם סוכן מנהל יוצר ומעדכן רשימת משימות ומנהל את התיאום בין סוכנים משניים להשלמת המשימה.  

לצורך אספקת סוכני AI בייצור, למסגרת MAF כלולים גם תכונות עבור:  

- **תצפית** באמצעות OpenTelemetry כאשר כל פעולה של סוכן ה-AI, כולל קריאת כלים, שלבי תזמור, זרמי הסקה ומעקב ביצועים דרך לוחות בקרה של Microsoft Foundry.  
- **אבטחה** על ידי אירוח סוכנים באופן מקומי ב-Microsoft Foundry הכולל בקרות אבטחה כגון גישה מבוססת תפקיד, טיפול בנתונים פרטיים ובטיחות תוכן מובנית.  
- **עמידות** מכיוון ששרשורי סוכנים וזרימות עבודה יכולים להפסיק, להמשיך ולהתאושש מטעויות מה שמאפשר תהליכים ארוכים יותר.  
- **בקרה** כיוון שזרימות עבודה של human-in-the-loop נתמכות כאשר משימות מסומנות ככאלו שדורשות אישור אדם.  

מסגרת Microsoft Agent גם מתמקדת באינטרופרביליות על ידי:  

- **א-עננית** - סוכנים יכולים לפעול במכולות, באתר ומעל מספר עננים שונים.  
- **א-ספקית** - סוכנים יכולים להיווצר באמצעות SDK מועדף כולל Azure OpenAI ו-OpenAI.  
- **שילוב תקנים פתוחים** - סוכנים יכולים להשתמש בפרוטוקולים כגון Agent-to-Agent (A2A) ו-Model Context Protocol (MCP) לגילוי ושימוש בסוכנים וכלים אחרים.  
- **תוספים ומחברים** - ניתן לבצע חיבורים לשירותי נתונים וזיכרון כגון Microsoft Fabric, SharePoint, Pinecone ו-Qdrant.  

בואו נבחן כיצד תכונות אלו מיושמות על חלק מהמושגים המרכזיים של מסגרת Microsoft Agent.  

## מושגים מרכזיים של מסגרת Microsoft Agent  

### סוכנים  

![Agent Framework](../../../translated_images/he/agent-components.410a06daf87b4fef.webp)

**יצירת סוכנים**  

יצירת סוכן מתבצעת על ידי הגדרת שירות ההסקה (LLM Provider),  
קבוצת הוראות שעל סוכן ה-AI לעקוב אחריהן, ושם מותאם (`name`):  

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

לעיל נעשה שימוש ב-`Azure OpenAI` אך סוכנים יכולים להיווצר באמצעות מגוון שירותים כולל `Microsoft Foundry Agent Service`:  

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

ממשקי API של OpenAI `Responses`, `ChatCompletion`  

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

או [MiniMax](https://platform.minimaxi.com/), המספק API תואם OpenAI עם חלונות הקשר גדולים (עד 204K טוקנים):  

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

או סוכנים מרוחקים באמצעות פרוטוקול A2A:  

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**הרצת סוכנים**  

סוכנים מורצים באמצעות המתודות `.run` או `.run_stream` לקבלת תגובות לא-מזרימות או מזרימות.  

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

להרצת כל סוכן יכולה להיות גם אפשרות להתאים פרמטרים כגון `max_tokens` בו משתמש הסוכן, `tools` שהסוכן יכול לקרוא להם, ואפילו ה-`model` המשמש את הסוכן עצמו.  

זה שימושי במקרים בהם נדרשים דגמים וכלים ספציפיים להשלמת משימת המשתמש.  

**כלים**  

כלים יכולים להיות מוגדרים גם בעת הגדרת הסוכן:  

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# כאשר יוצרים סוכן צ'אט ישירות

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

וגם בעת הרצת הסוכן:  

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # כלי המסופק רק להרצה זו )
```

**שרשורי סוכן**  

שרשורי סוכן משמשים לניהול שיחות מרובות סבבים. שרשורים יכולים להיווצר על ידי:  

- שימוש ב-`get_new_thread()` שמאפשר לשמור את השרשור לאורך זמן  
- יצירת שרשור אוטומטית בעת הרצת סוכן, כאשר השרשור קיים רק במהלך ההרצה הנוכחית.  

ליצירת שרשור, הקוד נראה כך:  

```python
# צור תהליך חדש.
thread = agent.get_new_thread() # הפעל את הסוכן עם התהליך.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

לאחר מכן ניתן לסריאליזציה של השרשור לאחסון לשימוש מאוחר יותר:  

```python
# צור נושא חדש.
thread = agent.get_new_thread() 

# הפעל את הסוכן עם הנושא.

response = await agent.run("Hello, how are you?", thread=thread) 

# סדר את הנושא לאחסון.

serialized_thread = await thread.serialize() 

# המרת מצב הנושא לאחר טעינה מהאחסון.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware של סוכן**  

סוכנים מתקשרים עם כלים ו-LLMs להשלמת משימות משתמש. בתרחישים מסוימים, אנו רוצים לבצע או לעקוב בין האינטראקציות הללו. Middleware של סוכן מאפשר זאת על ידי:  

*Middleware פונקציונלי*  

Middleware זה מאפשר לבצע פעולה בין הסוכן לפונקציה/כלי שהוא קורא לו. דוגמה לשימוש היא ביצוע רישום יומן במהלך קריאת פונקציה.  

בקוד למטה, `next` מגדיר אם יש לקרוא ל-middleware הבא או לפונקציה עצמה.  

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # עיבוד מקדים: רישום לפני ביצוע הפונקציה
    print(f"[Function] Calling {context.function.name}")

    # המשך למידלוור הבא או לביצוע הפונקציה
    await next(context)

    # עיבוד לאחר ביצוע: רישום אחרי ביצוע הפונקציה
    print(f"[Function] {context.function.name} completed")
```

*Middleware שיחתית*  

Middleware זה מאפשר לבצע או לרשום פעולה בין הסוכן לבין הבקשות בין ה-LLM.  

זה כולל מידע חשוב כגון ההודעות (`messages`) שנשלחות לשירות ה-AI.  

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # עיבוד מקדים: רישום לפני קריאה ל-AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # המשך למידלוור או שירות AI הבא
    await next(context)

    # עיבוד לאחר מעשה: רישום לאחר תגובת AI
    print("[Chat] AI response received")

```

**זיכרון סוכן**  

כפי שכוסה בשיעור `Agentic Memory`, הזיכרון הוא אלמנט חשוב לאפשר לסוכן לפעול בהקשרים שונים. ל-MAF יש כמה סוגי זיכרונות:  

*אחסון בזיכרון*  

זהו הזיכרון המאוחסן בשרשורים במהלך זמן ריצה של האפליקציה.  

```python
# צור נושא חדש.
thread = agent.get_new_thread() # הפעל את הסוכן עם הנושא.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*הודעות מתמשכות*  

זיכרון זה משמש לאחסון היסטוריית שיחות במגוון סשנים. הוא מוגדר באמצעות `chat_message_store_factory`:  

```python
from agent_framework import ChatMessageStore

# צור מאגר הודעות מותאם אישית
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*זיכרון דינמי*  

זיכרון זה מתווסף להקשר לפני הרצת הסוכנים. זיכרונות אלו ניתנים לאחסון בשירותים חיצוניים כגון mem0:  

```python
from agent_framework.mem0 import Mem0Provider

# שימוש ב-Mem0 עבור יכולות זיכרון מתקדמות
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**תצפית על סוכן**  

תצפית חשובה לבניית מערכות סוכניות אמינות וניתנות לתחזוקה. MAF משתלב עם OpenTelemetry כדי לספק מעקב ומדדים לתצפית טובה יותר.  

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # לעשות משהו
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### זרימות עבודה  

MAF מציעה זרימות עבודה המהוות שלבים מוגדרים מראש להשלמת משימה וכוללות סוכני AI כמרכיבים באותם שלבים.  

זרימות עבודה מורכבות ממרכיבים שונים המאפשרים זרימת בקרה טובה יותר. זרימות עבודה מאפשרות גם **תזמור מרובה-סוכנים** ו-**שמירת נקודות בדיקה** לשמירת מצבי הזרימה.  

המרכיבים המרכזיים של זרימת עבודה הם:  

**מבצעים**  

מבצעים מקבלים הודעות קלט, מבצעים את המשימות שהוקצו להם, ואז מייצרים הודעת פלט. זה מקדם את זרימת העבודה לקראת השלמת המשימה הרחבה יותר. מבצעים יכולים להיות סוכן AI או לוגיקה מותאמת אישית.  

**קצוות**  

קצוות משמשים להגדרת זרימת ההודעות בזרימת עבודה. אלה יכולים להיות:  

*קצוות ישירים* - חיבורים פשוטים אחד-על-אחד בין מבצעים:  

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*קצוות מותנים* - מופעלים לאחר שמתקיים תנאי מסוים. לדוגמה, כשחדרי מלון אינם זמינים, מבצע יכול להציע אפשרויות אחרות.  

*קצוות מקרה החלפה* - מנתבים הודעות למבצעים שונים על בסיס תנאים מוגדרים. לדוגמה, אם ללקוח נסיעות יש גישה מועדפת, משימותיו יטופלו דרך זרימת עבודה אחרת.  

*קצוות פיצול* - שולחים הודעה אחת למספר יעדים.  

*קצוות איסוף* - אוספים מספר הודעות ממבצעים שונים ושולחים ליעד אחד.  

**אירועים**  

לצורך תצפית טובה יותר על זרימות עבודה, MAF מציעה אירועים מובנים לביצוע כולל:  

- `WorkflowStartedEvent`  - התחלת ביצוע הזרימה  
- `WorkflowOutputEvent` - הזרימה מפיקה פלט  
- `WorkflowErrorEvent` - זרימת עבודה נתקלת בשגיאה  
- `ExecutorInvokeEvent`  - מבצע מתחיל עיבוד  
- `ExecutorCompleteEvent`  -  מבצע מסיים עיבוד  
- `RequestInfoEvent` - מתבצעת בקשה  

## דפוסי MAF מתקדמים  

הקטעים למעלה מכסים את המושגים המרכזיים של מסגרת Microsoft Agent. כשאתה בונה סוכנים מורכבים יותר, הנה כמה דפוסים מתקדמים לשקול:  

- **קומפוזיציית middleware**: שרשרת של מספר מטפלי middleware (רישום, אימות, הגבלת קצב) באמצעות middleware פונקציונלי ושיחתית לשליטה מדויקת בהתנהגות הסוכן.  
- **שמירת נקודות בדיקה בזרימות עבודה**: שימוש באירועים וסריאליזציה בזרימות עבודה לשמירה והמשך תהליכים סוכניים ארוכי טווח.  
- **בחירת כלים דינמית**: שילוב RAG מעל תיאורי כלים עם הרשמת הכלים של MAF להצגת כלים רלוונטיים בלבד לשאילתא.  
- **מסירת משימות מרובת סוכנים**: שימוש בקצוות זרימת עבודה וניתוב מותנה לתזמור מסירות בין סוכנים מיוחדים.  

## אירוח סוכני LangChain / LangGraph ב-Microsoft Foundry  

מסגרת Microsoft Agent היא **רב-פלטפורמית** — אינך מוגבל לסוכנים שנכתבו עם MAF. אם כבר יש לך סוכן שבנוי עם **LangChain** או **LangGraph**, תוכל להריץ אותו כסוכן **מארח ב-Microsoft Foundry** כך ש-Foundry תנהל את זמן הריצה, הסשנים, הסקיילינג, הזהות ונקודות הקצה של הפרוטוקול עבורך, בעוד שהלוגיקה של הסוכן שלך נשארת ב-LangGraph.  

זה נעשה עם החבילה `langchain_azure_ai.agents.hosting`, החשופה גרף LangGraph מותאם-קומפילציה מעל אותן פרוטוקולים בהם משתמשים סוכנים מאוחסנים ב-Foundry.  

**1. התקן את התוסף לאירוח:**  

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

תוסף ה-`hosting` מתקין את ספריות הפרוטוקול Foundry: `azure-ai-agentserver-responses` (נקודת הקצה התואמת OpenAI `/responses`) ו-`azure-ai-agentserver-invocations` (נקודת הקצה הגנרית `/invocations`).  

**2. בחר פרוטוקול אירוח:**  

| פרוטוקול | מחלקת מארח | נקודת קצה | שימוש בעת |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | רוצים צ'אט תואם OpenAI, מזרימה, היסטוריית תגובות ושרשרי שיחה — ברירת המחדל המומלצת לסוכנים שיחותיים. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | צריך צורת JSON מותאמת אישית, נקודת קצה בסגנון webhook, או עיבוד לא שיחותי. |

כיוון ש-**Responses API הוא ה-API הראשי לפיתוח סגנון סוכן ב-Foundry**, מומלץ להתחיל עם `ResponsesHostServer` לרוב הסוכנים.  

**3. הגדר משתני סביבה** (`az login` קודם כדי ש-`DefaultAzureCredential` יוכל לאמת):  

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

כאשר הסוכן ירוץ מאוחר יותר כסוכן מאוחסן ב-Foundry, הפלטפורמה תזריק אוטומטית את `FOUNDRY_PROJECT_ENDPOINT`.  

**4. חשוף סוכן LangGraph על פרוטוקול Responses:**  

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI כאן פונה לנקודת הקצה התואמת ל-OpenAI (Responses) של פרויקט Foundry.
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

הרץ אותו באופן מקומי עם `python main.py`, ואז שלח בקשת Responses ל-`http://localhost:8088/responses`.  

**התנהגויות מרכזיות:**  

- **שיחות**: לקוחות ממשיכים שיחה על ידי העברת `previous_response_id` או מזהה `conversation`. אם הגרף שלך מקומפל עם LangGraph checkpointer, Foundry מקשרת את מצב השיחה לנקודת הבדיקה (יש להשתמש בנקודת בדיקה עמידה בייצור; `MemorySaver` מספק למבחן מקומי).  
- **Human-in-the-loop**: אם הגרף שלך משתמש בפונקציית LangGraph `interrupt()`, `ResponsesHostServer` מציג את ההפסקה הממתינה כאובייקט `function_call` / `mcp_approval_request` ב-Responses, והלקוחות ממשיכים עם `function_call_output` / `mcp_approval_response` תואמים.  
- **פריסה ב-Foundry**: השתמש ב-Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (מקומי, דורש Docker), ואז `azd provision` ו-`azd deploy`. פריסת סוכן מאוחסן דורשת את התפקיד **Foundry Project Manager**.  

גרסה רצה של דוגמה זו קיימת ב-[code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). למדריך המלא (פרוטוקול Invocations, סכמה מותאמת אישית לבקשות ופתרון תקלות), ראה [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).  

## דוגמאות קוד  

דוגמאות קוד למסגרת Microsoft Agent נמצאות במאגר זה תחת הקבצים `xx-python-agent-framework` ו- `xx-dotnet-agent-framework`.  

## שאלות נוספות על מסגרת Microsoft Agent?  

הצטרף ל-[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) כדי להיפגש עם לומדים אחרים, להשתתף בשעות משרד ולקבל תשובות לשאלותיך על סוכני AI.  
## שיעור קודם  

[זיכרון לסוכני AI](../13-agent-memory/README.md)  

## שיעור הבא  

[בניית סוכני שימוש במחשב (CUA)](../15-browser-use/README.md)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->