# חקירת מסגרת Microsoft Agent  

![Agent Framework](../../../translated_images/he/lesson-14-thumbnail.90df0065b9d234ee.webp)  

### מבוא  

שיעור זה יכסה:  

- הבנת מסגרת Microsoft Agent: תכונות מפתח וערך  
- חקר המושגים המרכזיים של מסגרת Microsoft Agent  
- דפוסי MAF מתקדמים: Workflows, Middleware וזיכרון  

## יעדי למידה  

לאחר סיום שיעור זה, תדעו כיצד:  

- לבנות סוכני AI מוכנים לייצור באמצעות מסגרת Microsoft Agent  
- להחיל את התכונות המרכזיות של מסגרת Microsoft Agent על מקרים שימושיים סוכנתיים שלכם  
- להשתמש בדפוסים מתקדמים כולל workflows, middleware, ותצפית  

## דוגמאות קוד  

דוגמאות קוד עבור [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) נמצאות במאגר זה תחת הקבצים `xx-python-agent-framework` ו- `xx-dotnet-agent-framework`.  

## הבנת מסגרת Microsoft Agent  

![Framework Intro](../../../translated_images/he/framework-intro.077af16617cf130c.webp)  

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) היא מסגרת מאוחדת של מיקרוסופט לבניית סוכני AI. היא מציעה גמישות לטיפול במגוון רחב של מקרים שימושיים סוכנתיים הנצפים הן בסביבות ייצור והן במחקר, כולל:  

- **אורקסטרציה סדרתית** בתרחישים שבהם נדרשים Workflows שלב אחר שלב.  
- **אורקסטרציה מקבילית** בתרחישים שבהם סוכנים צריכים להשלים משימות בו זמנית.  
- **אורקסטרציית שיחת קבוצה** בתרחישים שבהם סוכנים יכולים לשתף פעולה יחד על משימה אחת.  
- **אורקסטרציית handoff** בתרחישים שבהם סוכנים מעבירים את המשימה זה לזה כשהמשימות המשניות המוקצות הושלמו.  
- **אורקסטרציה מגנטית** בתרחישים שבהם סוכן מנהל יוצר ומעדכן רשימת משימות ומטפל בתיאום של סוכנים משניים להשלמת המשימה.  

כדי לספק סוכני AI בייצור, ל-MAF גם יש תכונות לכלול עבור:  

- **תצפית** באמצעות שימוש ב-OpenTelemetry שבה כל פעולה של סוכן ה-AI כולל קריאת כלי, שלבי אורקסטרציה, זרמי נימוק ומעקב ביצועים דרך דשבורדים של Microsoft Foundry.  
- **אבטחה** על ידי אירוח סוכנים בצורה מקומית ב-Microsoft Foundry הכולל בקרים כמו גישה מבוססת תפקיד, טיפול בנתונים פרטיים ובטיחות תוכן מובנית.  
- **עמידות** כפי ששרשורי סוכן ו-Workflows יכולים להשהות, להמשיך ולהתאושש מטעויות, מה שמאפשר תהליכים ארוכי טווח.  
- **שליטה** תומך ב- workflows בהם יש מעורבות אדם שבהן משימות מסומנות ככאלה שדורשות אישור אנושי.  

מסגרת Microsoft Agent מתמקדת גם באינטרופרביליות על ידי:  

- **היותה בלתי תלויה בענן** - סוכנים יכולים לפעול במכולות, מקומי ועל פני עננים שונים.  
- **היותה בלתי תלויה בספק** - סוכנים יכולים להיווצר באמצעות ה-SDK המועדף עליך כולל Azure OpenAI ו-OpenAI  
- **שילוב תקנים פתוחים** - סוכנים יכולים להשתמש בפרוטוקולים כגון Agent-to-Agent(A2A) ו-Model Context Protocol (MCP) כדי לגלות ולהשתמש בסוכנים וכלים אחרים.  
- **תוספים וחיבורים** - ניתן ליצור חיבורים לשירותי נתונים וזיכרון כמו Microsoft Fabric, SharePoint, Pinecone ו-Qdrant.  

בואו נסתכל כיצד תכונות אלה מיושמות בכמה מהמושגים המרכזיים של מסגרת Microsoft Agent.  

## מושגי יסוד של מסגרת Microsoft Agent  

### סוכנים  

![Agent Framework](../../../translated_images/he/agent-components.410a06daf87b4fef.webp)  

**יצירת סוכנים**  

יצירת סוכן נעשית על ידי הגדרת שירות המסקנה (ספק LLM),  
סט של הוראות שעל סוכן ה-AI לעקוב אחריהן, ושם שהוקצה ל-`name`:  

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```
  
הקוד לעיל משתמש ב-`Azure OpenAI` אך סוכנים יכולים להיווצר באמצעות מגוון שירותים כולל `Microsoft Foundry Agent Service`:  

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```
  
APIs של OpenAI `Responses`, `ChatCompletion`  

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```
  
```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```
  
או [MiniMax](https://platform.minimaxi.com/), המציע API תואם OpenAI עם חלונות הקשר גדולים (עד 204K טוקנים):  

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```
  
או סוכנים מרוחקים המשתמשים בפרוטוקול A2A:  

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```
  
**הרצת סוכנים**  

סוכנים מופעלים באמצעות שיטות `.run` או `.run_stream` לתגובות לא סטרימינג או סטרימינג.  

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```
  
```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```
  
ניתן גם לכלול רשימת אפשרויות לכל הרצה כדי להתאים פרמטרים כגון `max_tokens` בהם הסוכן משתמש, `tools` שהסוכן יכול לקרוא להם, ואפילו את `model` עצמו המשמש את הסוכן.  

זה שימושי במקרים שבהם נדרשים דגמים או כלים ספציפיים להשלמת משימת המשתמש.  

**כלים**  

כלים יכולים להיות מוגדרים הן בעת הגדרת הסוכן:  

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# כאשר יוצרים ChatAgent ישירות

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```
  
וגם בעת הרצת הסוכן:  

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # כלי שסופק רק להרצה זו )
```
  
**שרשורי סוכן**  

שרשורי סוכן משמשים לטיפול בשיחות רב-סיבוביות. שרשורים יכולים להיווצר על ידי:  

- שימוש ב-`get_new_thread()` שמאפשר לשמור את השרשור לאורך זמן  
- יצירת שרשור אוטומטית במהלך הרצת סוכן, שבו השרשור קיים רק במהלך ההרצה הנוכחית.  

ליצירת שרשור, הקוד נראה כך:  

```python
# צור נושא חדש.
thread = agent.get_new_thread() # הפעל את הסוכן עם הנושא.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```
  
ניתן גם לסדרל את השרשור לאחסון לשימוש מאוחר יותר:  

```python
# צור אשכול חדש.
thread = agent.get_new_thread() 

# הפעל את הסוכן עם האשכול.

response = await agent.run("Hello, how are you?", thread=thread) 

# סדר את האשכול לאחסון.

serialized_thread = await thread.serialize() 

# דה-סדר את מצב האשכול לאחר הטעינה מהאחסון.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```
  
**Middleware של סוכן**  

סוכנים מתקשרים עם כלים ו-LLMs להשלים משימות של המשתמש. בתרחישים מסוימים, אנו רוצים לבצע או לעקוב בין האינטראקציות האלה. ה-Middleware של הסוכן מאפשר לנו לעשות זאת באמצעות:  

*Middleware של פונקציה*  

Middleware זה מאפשר לנו לבצע פעולה בין הסוכן ופונקציה/כלי שהוא יקרא לה. דוגמה לשימוש כזה היא כאשר רוצים לבצע רישום קריאה לפונקציה.  

בקוד למטה `next` מגדיר אם יש לקרוא ל-middleware הבא או לפונקציה עצמה.  

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # עיבוד מקדים: רישום לפני ביצוע הפונקציה
    print(f"[Function] Calling {context.function.name}")

    # המשך למידלוואר הבא או לביצוע הפונקציה
    await next(context)

    # עיבוד שלאחר מכן: רישום אחרי ביצוע הפונקציה
    print(f"[Function] {context.function.name} completed")
```
  
*Middleware של שיחה*  

Middleware זה מאפשר לנו לבצע או לרשום פעולה בין הסוכן לבין הבקשות שבין ה-LLM.  

זה מכיל מידע חשוב כגון `messages` שנשלחות לשירות ה-AI.  

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # עיבוד מקדים: רישום לפני קריאת בינה מלאכותית
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # המשך למידלוור הבא או שירות הבינה המלאכותית
    await next(context)

    # עיבוד לאחר מכן: רישום אחרי תגובת הבינה המלאכותית
    print("[Chat] AI response received")

```
  
**זיכרון סוכן**  

כפי שנלמד בשיעור `Agentic Memory`, זיכרון הוא אלמנט חשוב לאפשר לסוכן לפעול בהקשרים שונים. ל-MAF יש כמה סוגי זיכרון שונים:  

*אחסון בזיכרון*  

זהו הזיכרון המאוחסן בשרשורים במהלך זמן ריצת האפליקציה.  

```python
# צור אגף חדש.
thread = agent.get_new_thread() # הרץ את הסוכן עם האגף.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```
  
*הודעות מתמשכות*  

זיכרון זה משמש לאחסון היסטוריית שיחות בין סשנים שונים. הוא מוגדר באמצעות ה-`chat_message_store_factory`:  

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

זיכרון זה מתווסף להקשר לפני הרצת הסוכנים. זיכרונות אלה יכולים להיאגר בשירותים חיצוניים כגון mem0:  

```python
from agent_framework.mem0 import Mem0Provider

# שימוש ב-Mem0 ליכולות זיכרון מתקדמות
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

תצפית חשובה לבניית מערכות סוכנים אמינות וניתנות לתחזוקה. MAF משתלב עם OpenTelemetry כדי לספק מעקבים ומדדים לתצפית טובה יותר.  

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
  
### Workflows  

ל-MAF יש workflows שהן שלבים מוגדרים מראש להשלמת משימה וכוללות סוכני AI כמרכיבים באותם שלבים.  

Workflows מורכבות ממרכיבים שונים המאפשרים זרימת שליטה טובה יותר. Workflows מאפשרות גם **אורקסטרציה של סוכנים מרובים** ו-**קביעת נקודות ביקורת** לשמירת מצבי Workflow.  

המרכיבים העיקריים של workflow הם:  

**מבצעים**  

מבצעים מקבלים הודעות קלט, מבצעים את המשימות שהוקצו להם, ואז מפיקים הודעת פלט. זה מזיז את הworkflow קדימה לקראת השלמת המשימה הגדולה. המבצעים יכולים להיות סוכן AI או לוגיקה מותאמת אישית.  

**קשתות**  

קשתות משמשות להגדיר את זרימת ההודעות ב-workflow. אלה יכולות להיות:  

*קשתות ישירות* - חיבורים פשוטים אחד על אחד בין מבצעים:  

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```
  
*קשתות מותנות* - מופעלות לאחר שמתקיים תנאי מסוים. לדוגמה, כאשר חדרי מלון אינם זמינים, מבצע יכול להציע אפשרויות אחרות.  

*קשתות switch-case* - מנתבות הודעות למבצעים שונים בהתאם לתנאים שהוגדרו. לדוגמה, אם ללקוח הנסיעות יש גישה מועדפת, המשימות שלו ינוהלו דרך workflow אחר.  

*קשתות פאן-אאוט* - שולחות הודעה אחת לריבוי יעדים.  

*קשתות פאן-אין* - אוספות הודעות מרובות ממבצעים שונים ושולחות ליעד אחד.  

**אירועים**  

כדי לספק תצפית טובה יותר ל-workflows, MAF מציעה אירועים מובנים לביצוע כולל:  

- `WorkflowStartedEvent` - התחלת ביצוע workflow  
- `WorkflowOutputEvent` - ה-Workflow מפיק פלט  
- `WorkflowErrorEvent` - ה-Workflow נתקל בשגיאה  
- `ExecutorInvokeEvent` - המבצע מתחיל לעבד  
- `ExecutorCompleteEvent` - המבצע מסיים לעבד  
- `RequestInfoEvent` - בקשה הונפקה  

## דפוסי MAF מתקדמים  

הסעיפים שלמעלה מכסים את המושגים המרכזיים של מסגרת Microsoft Agent. ככל שתבנו סוכנים מורכבים יותר, הנה כמה דפוסים מתקדמים שיש לקחת בחשבון:  

- **קומפוזיציית Middleware**: שרשור מספר מטפלי middleware (רישום, אימות, הגבלת קצב) באמצעות middleware של פונקציה ושיחה לשליטה עדינה בהתנהגות הסוכן.  
- **נקודות ביקורת ב-Workflow**: שימוש באירועי Workflow וסידור כדי לשמור ולהמשיך תהליכים ארוכי טווח של סוכנים.  
- **בחירת כלי דינמית**: שילוב RAG על תיאורי כלי עם רישום הכלים של MAF כדי להציג רק כלים רלוונטיים לכל שאילתה.  
- **העברת סוכנים מרובת משתתפים**: שימוש בקשתות Workflow וניתוב מותנה לאורקסטרציה של העברות בין סוכנים מומחים.  

## אירוח סוכני LangChain / LangGraph ב-Microsoft Foundry  

מסגרת Microsoft Agent היא **אינטרופרבילית במסגרת** — אינך מוגבל לסוכנים שנכתבו עם MAF. אם כבר יש לך סוכן שנבנה עם **LangChain** או **LangGraph**, ניתן להפעילו כסוכן **מארח ב-Microsoft Foundry** כך ש-Foundry תנהל את סביבות הריצה, הסשנים, האיזון, הזהות ונקודות הקצה של הפרוטוקול עבורך, בעוד שהלוגיקה של הסוכן נשארת ב-LangGraph.  

זה נעשה עם החבילה `langchain_azure_ai.agents.hosting`, הפותחת גרף קומפילציית LangGraph על פני אותם פרוטוקולים שסוכני Foundry משתמשים בהם.  

**1. התקן את התוסף לאירוח:**  

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```
  
התוסף `hosting` מתקין את ספריות פרוטוקול Foundry: `azure-ai-agentserver-responses` (נקודת הקצה `/responses` התואמת ל-OpenAI) ו-`azure-ai-agentserver-invocations` (נקודת הקצה הכללית `/invocations`).  

**2. בחר פרוטוקול אירוח:**  

| פרוטוקול | מחלקת מארח | נקודת קצה | שימוש כאשר |  
|----------|-----------|----------|----------|  
| **Responses** | `ResponsesHostServer` | `/responses` | ברצונך לצ'אט תואם OpenAI, סטרימינג, היסטוריית תגובות ושרשור שיחות — ברירת המחדל המומלצת לסוכנים שיחותיים. |  
| **Invocations** | `InvocationsHostServer` | `/invocations` | אתה צריך צורת JSON מותאמת אישית, נקודת קצה בסגנון webhook או עיבוד לא שיחתי. |  

מאחר ש-**Responses API הוא ה-API העיקרי לפיתוח בסגנון סוכן ב-Foundry**, התחל עם `ResponsesHostServer` עבור רוב הסוכנים.  

**3. הגדר משתני סביבה** (`az login` קודם כדי ש-`DefaultAzureCredential` תוכל לאמת):  

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```
  
כשסוכן יפעל מאוחר יותר כסוכן מארח ב-Foundry, הפלטפורמה תזריק אוטומטית את `FOUNDRY_PROJECT_ENDPOINT`.  

**4. חשוף סוכן LangGraph באמצעות פרוטוקול Responses:**  

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

    # ChatOpenAI כאן ממקדת את נקודת הקצה התואמת ל-OpenAI (תשובות) של פרויקט Foundry.
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
  
הרץ אותו מקומית עם `python main.py`, ואז שלח בקשת Responses ל- `http://localhost:8088/responses`.  

**התנהגויות עיקריות:**  

- **שיחות**: לקוחות ממשיכים שיחה על ידי העברת `previous_response_id` או מזהה `conversation`. אם הגרף שלך קומפייל עם בודק LangGraph, Foundry מקשרת את מצב השיחה לנקודת הביקורת (השתמש בבודק עמיד לייצור; `MemorySaver` מתאים לבדיקות מקומיות).  
- **אדם בלולאה**: אם הגרף שלך משתמש ב-LangGraph `interrupt()`, `ResponsesHostServer` מציג את ההפסקה התלויה כפריט `function_call` / `mcp_approval_request` ב-Responses, ולקוחות ממשיכים עם `function_call_output` / `mcp_approval_response` תואם.  
- **פריסה ב-Foundry**: השתמש ב-CLI למפתח Azure — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (מקומי, דורש Docker), ואז `azd provision` ו- `azd deploy`. פריסת סוכן מארח דורשת את התפקיד **Foundry Project Manager**.  

גרסה ניתנת להרצה של דוגמה זו קיימת ב-[code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). לקבלת ההדרכה המלאה (פרוטוקול Invocations, סכימות בקשה מותאמות אישית ופתרון תקלות) ראה [אירוח סוכני LangGraph כסוכנים מאוחסנים ב-Foundry](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).  

## דוגמאות קוד  

דוגמאות קוד עבור מסגרת Microsoft Agent זמינות במאגר זה תחת הקבצים `xx-python-agent-framework` ו-`xx-dotnet-agent-framework`.  

## יש לכם שאלות נוספות על מסגרת Microsoft Agent?  

הצטרפו ל-[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) כדי להיפגש עם לומדים אחרים, להשתתף בשעות משרדים ולקבל תשובות לשאלות על סוכני ה-AI שלכם.  
## שיעור קודם  

[זיכרון לסוכני AI](../13-agent-memory/README.md)  

## שיעור הבא  

[בניית סוכני שימוש במחשב (CUA)](../15-browser-use/README.md)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->