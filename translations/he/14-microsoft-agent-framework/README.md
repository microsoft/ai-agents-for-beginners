# חקר מסגרת סוכן מיקרוסופט

![Agent Framework](../../../translated_images/he/lesson-14-thumbnail.90df0065b9d234ee.webp)

### מבוא

שיעור זה יכלול:

- הבנת מסגרת סוכן מיקרוסופט: תכונות מפתח וערך  
- חקירת המושגים המרכזיים של מסגרת סוכן מיקרוסופט
- דפוסי MAF מתקדמים: זרימות עבודה, תיווך וזיכרון

## מטרות הלמידה

לאחר סיום השיעור, תדעו כיצד:

- לבנות סוכני AI מוכנים לייצור באמצעות מסגרת סוכן מיקרוסופט
- ליישם את התכונות המרכזיות של מסגרת סוכן מיקרוסופט למקרי השימוש הסוכניים שלכם
- להשתמש בדפוסים מתקדמים כולל זרימות עבודה, תיווך, ויכולת תצפית

## דוגמאות קוד

דוגמאות קוד ל[מסגרת סוכן מיקרוסופט (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) נמצאות במאגר זה תחת הקבצים `xx-python-agent-framework` ו-`xx-dotnet-agent-framework`.

## הבנת מסגרת סוכן מיקרוסופט

![Framework Intro](../../../translated_images/he/framework-intro.077af16617cf130c.webp)

[מסגרת סוכן מיקרוסופט (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) היא המסגרת המאוחדת של מיקרוסופט לבניית סוכני AI. היא מציעה גמישות לענות על מגוון רחב של מקרי שימוש סוכניים הנצפים הן בסביבות ייצור והן במחקר, כולל:

- **תזמור סוכנים עוקב** בתרחישים בהם יש צורך בזרימות עבודה שלב אחרי שלב.
- **תזמור סימולטני** בתרחישים בהם סוכנים צריכים להשלים משימות בו זמנית.
- **תזמור שיח קבוצתי** בתרחישים בהם סוכנים משתפים פעולה יחד על משימה אחת.
- **תזמור העברה** בתרחישים בהם הסוכנים מעבירים אחד לשני את המשימה כאשר תת-המשימות הושלמו.
- **תזמור מגנטי** בתרחישים בהם סוכן מנהל יוצר ומעדכן רשימת משימות ומטפל בתיאום של סוכנים-משניים כדי להשלים את המשימה.

על מנת לספק סוכני AI בייצור, MAF כוללת גם תכונות עבור:

- **יכולת תצפית** באמצעות שימוש ב-OpenTelemetry כאשר כל פעולה של סוכן ה-AI כולל קריאת כלים, שלבי תזמור, זרימות חשיבה ומעקב ביצועים דרך לוחות ניהול של Microsoft Foundry.
- **אבטחה** על ידי אירוח סוכנים באופן מקומי ב-Microsoft Foundry הכולל בקרות אבטחה כגון גישת תפקיד, טיפול בנתונים פרטיים ובטיחות תוכן מובנית.
- **עמידות** כיוון ששרשורי הסוכן וזרימות העבודה יכולים להשהות, להמשיך ולהתאושש משגיאות, מה שמאפשר תהליכים שרצים לאורך זמן רב.
- **בקרה** מאחר שזרימות עבודה עם מעורבות אנושית נתמכות, כאשר משימות מסומנות כמצריכות אישור אנושי.

מסגרת סוכן מיקרוסופט מתמקדת גם באינטרופרביליות על ידי:

- **היותה בלתי תלויה בענן** – סוכנים יכולים לפעול במכולות, מקומית ועל פני עננים מרובים שונים.
- **היותה בלתי תלויה בספק** – סוכנים יכולים להיווצר באמצעות SDK המועדף עליך כולל Azure OpenAI ו-OpenAI.
- **שילוב תקנים פתוחים** – סוכנים יכולים להשתמש בפרוטוקולים כמו Agent-to-Agent (A2A) ו-Model Context Protocol (MCP) כדי לגלות ולהשתמש בסוכנים וכלים אחרים.
- **תוספים ומחברים** – ניתן לבצע חיבורים לשירותי נתונים וזיכרון כמו Microsoft Fabric, SharePoint, Pinecone ו-Qdrant.

בואו נבחן כיצד תכונות אלו מיושמות על חלק מהמושגים המרכזיים של מסגרת סוכן מיקרוסופט.

## מושגים מרכזיים של מסגרת סוכן מיקרוסופט

### סוכנים

![Agent Framework](../../../translated_images/he/agent-components.410a06daf87b4fef.webp)

**יצירת סוכנים**

יצירת סוכן מתבצעת על ידי הגדרת שירות ההסקה (ספק LLM),  
קבוצת הוראות שעל סוכן ה-AI לבצע, ו`name` שיוקצה לו:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

לעיל נעשה שימוש ב`Azure OpenAI` אך סוכנים יכולים להיווצר באמצעות מגוון שירותים כולל `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

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

סוכנים מורצים באמצעות המתודות `.run` או `.run_stream` לקבלת תגובות לא בזרם או בזרם.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

לכל הפעלה של סוכן יכולות להיות גם אפשרויות להתאמת פרמטרים כגון `max_tokens` שהסוכן משתמש בהם, `tools` שהסוכן יכול לקרוא להן, ואף `model` עצמו בו נעשה שימוש לסוכן.

זה שימושי במקרים בהם נדרשים מודלים או כלים ספציפיים להשלמת משימת המשתמש.

**כלים**

כלים יכולים להיות מוגדרים גם בעת הגדרת הסוכן:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# כאשר יוצרים סוכן שיחה ישירות

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

וגם בעת הפעלת הסוכן:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # כלי שסופק לריצה זו בלבד )
```

**שרשורי סוכן**

שרשורי סוכן משמשים לטיפול בשיחות רב סבביות. ניתן ליצור שרשורים באמצעות:

- שימוש ב-`get_new_thread()` המאפשר לשמור את השרשור לאורך זמן
- יצירת שרשור באופן אוטומטי בעת הרצת סוכן כששרשור זה נמשך רק במהלך ההרצה הנוכחית.

ליצירת שרשור, קוד נראה כך:

```python
# צור שרשור חדש.
thread = agent.get_new_thread() # הפעל את הסוכן עם השרשור.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

לאחר מכן ניתן לסריאליזציה של השרשור לשם אחסון לשימוש מאוחר יותר:

```python
# צור נושא חדש.
thread = agent.get_new_thread() 

# הפעל את הסוכן עם הנושא.

response = await agent.run("Hello, how are you?", thread=thread) 

# שבה את הנושא לאחסון.

serialized_thread = await thread.serialize() 

# פתח את מצב הנושא לאחר טעינה מהאחסון.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**תיווך סוכן**

סוכנים מתקשרים עם כלים ו-LLMs כדי להשלים משימות של משתמשים. בתרחישים מסוימים, אנו רוצים לבצע או לעקוב אחרי פעולות בין אינטראקציות אלו. תיווך הסוכן מאפשר לנו לעשות זאת באמצעות:

*תיווך פונקציות*

תיווך זה מאפשר לנו לבצע פעולה בין הסוכן לפונקציה/כלי שהוא יקרא להם. דוגמה כאשר זה ישמש היא כאשר תרצו לבצע רישום של קריאת הפונקציה.

בקוד למטה `next` מגדיר אם יש לקרוא לתיווך הבא או לפונקציה עצמו.

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

    # עיבוד לאחר מכן: רישום אחרי ביצוע הפונקציה
    print(f"[Function] {context.function.name} completed")
```

*תיווך שיחה*

תיווך זה מאפשר לנו לבצע או לרשום פעולה בין הסוכן לבין הבקשות בין ה-LLM.

זה כולל מידע חשוב כמו ה`messages` שנשלחים לשירות ה-AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # עיבוד מקדים: רישום לפני קריאת AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # המשך לשכבת ביניים הבאה או לשירות AI
    await next(context)

    # עיבוד לאחר פעולה: רישום לאחר תגובת AI
    print("[Chat] AI response received")

```

**זיכרון סוכן**

כפי שנלמד ב`Agentic Memory` השיעור, זיכרון הוא אלמנט חשוב לאפשר לסוכן לפעול בהקשרים שונים. ל-MAF יש סוגים שונים של זיכרונות:

*אחסון בזיכרון פנימי*

זיכרון זה נשמר בשרשורים במהלך זמן הריצה של היישום.

```python
# צור אשכול חדש.
thread = agent.get_new_thread() # הרץ את הסוכן עם האשכול.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*הודעות מתמשכות*

זיכרון זה משמש בעת אחסון היסטוריית שיחה על פני סשנים שונים. הוא מוגדר באמצעות `chat_message_store_factory`:

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

זיכרון זה נוסף להקשר לפני הפעלת סוכנים. זיכרונות אלו יכולים להישמר בשירותים חיצוניים כמו mem0:

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

**יכולת תצפית לסוכן**

יכולת תצפית חשובה לבניית מערכות סוכנים אמינות וניתנות לתחזוקה. MAF משתלבת עם OpenTelemetry כדי לספק מעקב ומדדים לשיפור היכולת תצפית.

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

MAF מציעה זרימות עבודה שהן שלבים מוגדרים מראש להשלמת משימה וכוללות סוכני AI כרכיבים באותם שלבים.

זרימות עבודה מורכבות ממרכיבים שונים המאפשרים זרימת בקרה טובה יותר. זרימות עבודה מאפשרות גם **תזמור ריבוי סוכנים** ו**שמירת נקודות ביקורת** לשמירת מצבי זרימה.

מרכיבי הליבה של זרימת עבודה הם:

**מבצעים**

מבצעים מקבלים הודעות קלט, מבצעים את המשימות שהוקצו להם, ואז מפיקים הודעת פלט. זה מזיז את זרימת העבודה קדימה לעבר השלמת המשימה הרחבה יותר. מבצעים יכולים להיות סוכן AI או לוגיקה מותאמת.

**קשתות**

קשתות משמשות כדי להגדיר את זרימת ההודעות בזרימת עבודה. אלה יכולים להיות:

*קשתות ישירות* - חיבורים פשוטים אחד לאחד בין מבצעים:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*קשתות מותנות* - מופעלות לאחר שמתקיים תנאי מסוים. לדוגמה, כאשר חדרי מלון אינם זמינים, מבצע יכול להציע אפשרויות אחרות.

*קשתות כולל-מקרה* - מפנות הודעות למבצעים שונים בהתבסס על תנאים מוגדרים. לדוגמה, אם ללקוח נסיעות יש גישה בעדיפות, המשימות שלו יטופלו דרך זרימת עבודה אחרת.

*קשתות פיזור* - שולח הודעה אחת למספר יעדים.

*קשתות איסוף* - אוסף מספר הודעות ממבצעים שונים ושולח ליעד אחד.

**אירועים**

לספק יכולת תצפית טובה יותר על זרימות העבודה, MAF מציע אירועים מובנים לביצוע כולל:

- `WorkflowStartedEvent`  - התחלת ביצוע זרימת עבודה
- `WorkflowOutputEvent` - זרימת עבודה מפיקה פלט
- `WorkflowErrorEvent` - זרימת עבודה נתקלה בשגיאה
- `ExecutorInvokeEvent`  - המבצע מתחיל עיבוד
- `ExecutorCompleteEvent`  -  המבצע מסיים עיבוד
- `RequestInfoEvent` - בקשה הוצאה לפועל

## דפוסי MAF מתקדמים

הסעיפים שלמעלה מכסים את המושגים המרכזיים של מסגרת סוכן מיקרוסופט. כאשר אתם בונים סוכנים מורכבים יותר, הנה כמה דפוסים מתקדמים לשקול:

- **קומפוזיציית תיווך**: שרשר ריבוי מטפלי תיווך (רישום, אימות, הגבלת קצב) באמצעות תיווך פונקציות ושיחה לשליטה מדויקת בהתנהגות הסוכן.
- **שמירת נקודות ביקורת בזרימות עבודה**: שימוש באירועי זרימות עבודה וסריאליזציה לשמירה וחידוש תהליכים ארוכי טווח של סוכנים.
- **בחירת כלים דינמית**: שילוב RAG לתיאורי כלים עם רישום הכלים של MAF להצגת כלים רלוונטיים בלבד לפי השאילתה.
- **העברת ריבוי סוכנים**: שימוש בקשתות זרימות עבודה וניתוב מותנה כדי לתזמר העברות בין סוכנים מתמחים.

## אירוח סוכני LangChain / LangGraph ב-Microsoft Foundry

מסגרת סוכן מיקרוסופט היא **אינטרופרבילית במסגרת** — אינכם מוגבלים לסוכנים שכתובים עם MAF. אם יש לכם כבר סוכן שנבנה עם **LangChain** או **LangGraph**, תוכלו להריץ אותו כסוכן **מאוחסן ב-Microsoft Foundry** כך ש-Foundry תנהל את זמן הריצה, הסשנים, הסקלינג, הזהות ונקודות הקצה של הפרוטוקול עבורכם, בעוד הלוגיקה של הסוכן נשארת ב-LangGraph.

זאת נעשה באמצעות החבילה `langchain_azure_ai.agents.hosting`, שמציגה גרף LangGraph מאוחד מעל אותם פרוטוקולים בהם משתמשים סוכני Foundry המאוחסנים.

**1. התקינו את ה-extra של אירוח:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

ה-extra של `hosting` מתקין את ספריות הפרוטוקול של Foundry: `azure-ai-agentserver-responses` (נקודת הקצה `/responses` תואמת OpenAI) ו-`azure-ai-agentserver-invocations` (נקודת הקצה הכללית `/invocations`).

**2. בחרו פרוטוקול אירוח:**

| פרוטוקול | מחלקת האחסון | נקודת סיום | מתי להשתמש |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | רוצים שיח תואם OpenAI, הזרמה, היסטוריית תגובות, ושרשורי שיחות — ברירת המחדל המומלצת לסוכני שיחה. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | זקוקים לצורת JSON מותאמת אישית, נקודת קצה בסגנון webhook, או עיבוד לא-שיחתי. |

כיוון ש**API התגובות הוא ה-API הראשי לפיתוח סגנון סוכן ב-Foundry**, התחילו עם `ResponsesHostServer` עבור רוב הסוכנים.

**3. הגדרת משתני סביבה** (`az login` תחילה כדי ש-`DefaultAzureCredential` יוכל לאמת):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

כאשר הסוכן מורץ מאוחר יותר כסוכן מאוחסן ב-Foundry, הפלטפורמה מזריקה אוטומטית את `FOUNDRY_PROJECT_ENDPOINT`.

**4. חשפו סוכן LangGraph מעל פרוטוקול התגובות:**

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI כאן פונה לנקודת הקצה של Foundry התואמת ל-OpenAI (Responses).
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

הריצו אותו מקומית עם `python main.py`, ואז שלחו בקשת Responses אל `http://localhost:8088/responses`.

**התנהגויות מפתח:**

- **שיחות**: לקוחות ממשיכים שיחה על ידי העברת `previous_response_id` או מזהה `conversation`. אם הגרף שלכם מקומפל עם בודק נקודות ביקורת LangGraph, Foundry מקשר מצב השיחה לנקודת הביקורת (השתמשו בבודק נקודות ביקורת עמיד בייצור; `MemorySaver` מספיק לבדיקות מקומיות).
- **מעורבות אנושית**: אם הגרף שלכם משתמש ב-LangGraph ב`interrupt()`, `ResponsesHostServer` מעלה את ההפסקה הממתינה כאובייקט `function_call` / `mcp_approval_request` ב-Responses, והלקוחות ממשיכים עם `function_call_output` / `mcp_approval_response` התואמים.
- **פריסה ב-Foundry**: השתמשו ב-Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (מקומי, דורש Docker), ואז `azd provision` ו-`azd deploy`. פריסה כסוכן מאוחסן דורשת את תפקיד **Foundry Project Manager**.

גרסה שאפשר להריץ של דוגמה זו נמצאת ב-[code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). להדרכה מלאה (פרוטוקול Invocations, סכימות בקשה מותאמות אישית, ופתרון בעיות), ראה [אירוח סוכני LangGraph כסוכנים מאוחסנים ב-Foundry](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## דוגמאות קוד

דוגמאות קוד למסגרת סוכן מיקרוסופט נמצאות במאגר זה תחת הקבצים `xx-python-agent-framework` ו-`xx-dotnet-agent-framework`.

## יש לך שאלות נוספות על מסגרת סוכן מיקרוסופט?

הצטרף אל [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) כדי לפגוש לומדים אחרים, להשתתף בשעות פעילות ולקבל תשובות לשאלותיך על סוכני AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->