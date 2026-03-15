# חקירת Microsoft Agent Framework

![מסגרת הסוכנים](../../../translated_images/he/lesson-14-thumbnail.90df0065b9d234ee.webp)

### מבוא

השיעור הזה יכסה:

- הבנת Microsoft Agent Framework: תכונות עיקריות וערך  
- חקירת המושגים המרכזיים של Microsoft Agent Framework
- תבניות מתקדמות של MAF: תזרימי עבודה, Middleware, וזיכרון

## מטרות הלמידה

בסיום שיעור זה, תדעו כיצד:

- לבנות סוכני AI מוכנים לפרודקשן באמצעות Microsoft Agent Framework
- להפעיל את התכונות המרכזיות של Microsoft Agent Framework על מקרי שימוש סוכניים
- להשתמש בתבניות מתקדמות הכוללות תזרימי עבודה, Middleware וניטור/תצפית

## דוגמאות קוד 

דוגמאות קוד עבור [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) נמצאות במאגר זה תחת הקבצים `xx-python-agent-framework` ו-`xx-dotnet-agent-framework`.

## הבנת Microsoft Agent Framework

![הקדמת המסגרת](../../../translated_images/he/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) היא המסגרת המאוחדת של Microsoft לבניית סוכני AI. היא מציעה גמישות לטיפול במגוון רחב של מקרי שימוש סוכניים הנראים הן בסביבות פרודקשן והן במחקר, כולל:

- **תזמור סוכנים רציף (Sequential Agent orchestration)** בתרחישים שבהם יש צורך בזרימות עבודה שלב-אחר-שלב.
- **תזמור מקבילי (Concurrent orchestration)** בתרחישים שבהם סוכנים צריכים להשלים משימות במקביל.
- **תזמור שיחה קבוצתית (Group chat orchestration)** בתרחישים שבהם סוכנים יכולים לשתף פעולה על משימה אחת.
- **תזמור העברה (Handoff Orchestration)** בתרחישים שבהם סוכנים מעבירים את המשימה זה אל זה כאשר תתי-המשימות הושלמו.
- **תזמור מגנטי (Magnetic Orchestration)** בתרחישים שבהם סוכן מנהל יוצר ומעבד רשימת משימות ומטפל בתיאום של תת-סוכנים להשלמת המשימה.

כדי לספק סוכני AI בפרודקשן, MAF כוללת גם תכונות עבור:

- **Observability** באמצעות OpenTelemetry כאשר כל פעולה של סוכן ה-AI כולל קריאות כלים, שלבי תזמור, זרמי הסקה ומעקב ביצועים דרך לוחות המחוונים של Microsoft Foundry.
- **Security** על ידי אירוח סוכנים באופן מקורי על Microsoft Foundry הכולל בקרות אבטחה כגון גישה מבוססת תפקידים, טיפול בנתונים פרטיים ובטיחות תוכן מובנית.
- **Durability** שכן תהליכי סוכן ותזרימי עבודה יכולים להשהות, להמשיך ולהתאושש משגיאות מה שמאפשר תהליכים ארוכי-טווח.
- **Control** שכן תזרימי עבודה עם מעורבות אדם נתמכים, כאשר משימות מסומנות כדורשות אישור אנושי.

Microsoft Agent Framework מתמקדת גם באינטרופרביליות על ידי:

- **ללא תלות בענן** - סוכנים יכולים לפעול במכולות, באופן מקומי וברחבי מספר עננים שונים.
- **ללא תלות בספק** - סוכנים יכולים להיווצר באמצעות ה-SDK המועדף עליך כולל Azure OpenAI ו-OpenAI
- **שילוב תקנים פתוחים** - סוכנים יכולים להשתמש בפרוטוקולים כגון Agent-to-Agent (A2A) ו-Model Context Protocol (MCP) כדי לגלות ולהשתמש בסוכנים וכלים אחרים.
- **תוספים ומחברים** - ניתן ליצור חיבורים לשירותי נתונים וזיכרון כגון Microsoft Fabric, SharePoint, Pinecone ו-Qdrant.

בואו נבחן כיצד תכונות אלו מיושמות על חלק מהמושגים המרכזיים של Microsoft Agent Framework.

## המושגים המרכזיים של Microsoft Agent Framework

### סוכנים

![מסגרת הסוכנים](../../../translated_images/he/agent-components.410a06daf87b4fef.webp)

**יצירת סוכנים**

יצירת סוכן נעשית על ידי הגדרת שירות ההסקה (LLM Provider), סט הוראות שהסוכן אמור לעקוב אחריהן, ושם מוקצה `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

מעלה משתמש ב-`Azure OpenAI`, אך ניתן ליצור סוכנים באמצעות מגוון שירותים כולל `Microsoft Foundry Agent Service`:

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

או סוכנים מרוחקים באמצעות פרוטוקול A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**הרצת סוכנים**

סוכנים מורצים באמצעות המתודות `.run` או `.run_stream` עבור תגובות לא-סטרימינג או תגובות סטרימינג.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

לכל הרצה של סוכן יכולות להיות גם אפשרויות להתאמת פרמטרים כגון `max_tokens` שהסוכן משתמש בו, `tools` שהסוכן יכול לקרוא, ואף ה-`model` עצמו המשמש את הסוכן.

זה שימושי במקרים שבהם נדרשים מודלים או כלים מסוימים להשלמת המשימה של המשתמש.

**כלים**

ניתן להגדיר כלים הן בעת הגדרת הסוכן:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# כאשר יוצרים את ה-ChatAgent ישירות

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

וגם בעת הרצת הסוכן:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # הכלי מסופק רק עבור ריצה זו )
```

**שרשורי סוכן**

שרשורי סוכן משמשים לטיפול בשיחות מרובות סיבובים. ניתן ליצור שרשורים באחד מהשניים:

- שימוש ב-`get_new_thread()` שמאפשר לשמור את השרשור לאורך זמן
- יצירת שרשור אוטומטית בעת הרצת סוכן כשהשרשור קיים רק במהלך ההרצה הנוכחית.

ליצירת שרשור, הקוד נראה כך:

```python
# צור חוט ביצוע חדש.
thread = agent.get_new_thread() # הפעל את הסוכן באמצעות חוט הביצוע.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

ניתן אז לסריאליז את השרשור כדי לאחסן אותו לשימוש עתידי:

```python
# צור חוט חדש.
thread = agent.get_new_thread() 

# הרץ את הסוכן עם החוט.

response = await agent.run("Hello, how are you?", thread=thread) 

# בצע סיריאליזציה של החוט לאחסון.

serialized_thread = await thread.serialize() 

# בצע דסיריאליזציה של מצב החוט לאחר טעינה מהאחסון.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware של סוכן**

סוכנים מתקשרים עם כלים ו-LLMs כדי להשלים את משימות המשתמש. בסיטואציות מסוימות, נרצה לבצע או לעקוב אחר פעולות בין האינטראקציות הללו. ה-Middleware של הסוכן מאפשר לנו לעשות זאת באמצעות:

*Function Middleware*

Middleware זה מאפשר לנו לבצע פעולה בין הסוכן לבין פונקציה/כלי שהוא יקרא. דוגמה לשימוש תהיה כאשר תרצה לבצע רישום (logging) על קריאת הפונקציה.

בקוד שלמטה `next` מגדיר האם יש לקרוא למידלוואר הבא או לפונקציה עצמה.

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

    # עיבוד לאחר הביצוע: רישום לאחר ביצוע הפונקציה
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Middleware זה מאפשר לנו לבצע או לרשום פעולה בין הסוכן לבין הבקשות ל-LLM.

זה מכיל מידע חשוב כגון ה-`messages` שנשלחות לשירות ה-AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # עיבוד מקדים: רישום לפני קריאה ל-AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # המשך לרכיב התווך הבא או לשירות ה-AI
    await next(context)

    # עיבוד לאחר מכן: רישום לאחר תגובת ה-AI
    print("[Chat] AI response received")

```

**זיכרון הסוכן**

כפי שנדון בשיעור `Agentic Memory`, זיכרון הוא אלמנט חשוב כדי לאפשר לסוכן לפעול בהקשרים שונים. MAF מציעה מספר סוגי זיכרונות שונים:

*In-Memory Storage*

זהו הזיכרון המאוחסן בשרשורים במהלך זמן ריצת היישום.

```python
# צור חוט חדש.
thread = agent.get_new_thread() # הרץ את הסוכן עם החוט.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

זיכרון זה משמש לאחסון היסטוריית שיחה על פני מושבים (sessions) שונים. הוא מוגדר באמצעות `chat_message_store_factory` :

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

*Dynamic Memory*

זיכרון זה נוסף להקשר לפני הרצת הסוכנים. זיכרונות אלו יכולים להיות מאוחסנים בשירותים חיצוניים כגון mem0:

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

**נראות של הסוכן**

נראות חשובה לבניית מערכות סוכניות אמינות וניתנות לתחזוקה. MAF משתלבת עם OpenTelemetry כדי לספק טרייסינג ומדדים לנראות טובה יותר.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # עשה משהו
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### תזרימי עבודה

MAF מציעה תזרימי עבודה שהם שלבים מוגדרים מראש להשלמת משימה וכוללים סוכני AI כמרכיבים בשלבים אלה.

תזרימי עבודה מורכבים מרכיבים שונים שמאפשרים זרימת בקרה טובה יותר. תזרימי עבודה גם מאפשרים **multi-agent orchestration** ו-**checkpointing** כדי לשמור מצבי תזרימ עבודה.

הרכיבים המרכזיים של תזרימ עבודה הם:

**Executors**

Executors מקבלים הודעות קלט, מבצעים את המשימות שהוקצו להם ואז מייצרים הודעת פלט. זה מקדם את תזרימ העבודה לקראת השלמת המשימה הגדולה יותר. Executors יכולים להיות סוכן AI או לוגיקה מותאמת.

**Edges**

Edges משמשים להגדיר את זרימת ההודעות בתזרימ עבודה. אלה יכולים להיות:

*Direct Edges* - חיבורים פשוטים אחד-ל-אחד בין Executors:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - מופעלים לאחר שמתקיים תנאי מסוים. לדוגמה, כאשר חדרי המלון אינם זמינים, Executor יכול להציע אפשרויות אחרות.

*Switch-case Edges* - מנתבים הודעות ל-Executors שונים על בסיס תנאים מוגדרים. לדוגמה, אם ללקוח הנוסע יש גישת עדיפות והמשימות שלו יטופלו באמצעות תזרימ עבודה אחר.

*Fan-out Edges* - שולחים הודעה אחת למספר יעדים.

*Fan-in Edges* - אוספים הודעות מרובות ממספר Executors ושולחים ליעד אחד.

**אירועים**

כדי לספק נראות טובה יותר לתזרימי עבודה, MAF מציעה אירועים מובנים לביצוע הכוללים:

- `WorkflowStartedEvent`  - התחלת ביצוע של תזרימ העבודה
- `WorkflowOutputEvent` - תזרим עבודה מייצר פלט
- `WorkflowErrorEvent` - תזרימ עבודה נתקל בשגיאה
- `ExecutorInvokeEvent`  - ה-Executor מתחיל בעיבוד
- `ExecutorCompleteEvent`  - ה-Executor מסיים עיבוד
- `RequestInfoEvent` - בקשה נשלחת

## תבניות מתקדמות של MAF

הסעיפים לעיל מכסים את המושגים המרכזיים של Microsoft Agent Framework. כאשר תבנו סוכנים מורכבים יותר, הנה כמה תבניות מתקדמות שכדאי לשקול:

- **הרכבת Middleware**: שרשרו מספר מטפלי middleware (רישום, אימות, הגבלת קצב) באמצעות function ו-chat middleware לשליטה מדויקת בהתנהגות הסוכן.
- **Checkpointing של תזרימי עבודה**: השתמשו באירועי תזרימ עבודה ובסריאליזציה כדי לשמור ולהמשיך תהליכים ארוכי-טווח של סוכנים.
- **בחירה דינמית של כלים**: שלבו RAG על תיאורי כלים עם רישום הכלים של MAF כדי להציג רק כלים רלוונטיים לכל שאילתה.
- **העברת משימות בין כמה סוכנים**: השתמשו ב-edges של תזרימי עבודה וניתוב מותנה כדי לתזמר העברות בין סוכנים מתמחים.

## דוגמאות קוד 

דוגמאות קוד עבור Microsoft Agent Framework נמצאות במאגר זה תחת הקבצים `xx-python-agent-framework` ו-`xx-dotnet-agent-framework`.

## יש לכם שאלות נוספות לגבי Microsoft Agent Framework?

הצטרפו ל [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) כדי להיפגש עם לומדים אחרים, להשתתף בשעות ייעוץ ולקבל תשובות לשאלותיכם לגבי סוכני ה-AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
הצהרת אחריות:
מסמך זה תורגם בעזרת שירות תרגום מבוסס בינה מלאכותית Co-op Translator (https://github.com/Azure/co-op-translator). אף שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי‑דיוקים. המסמך המקורי בשפתו מהווה את הגרסה הסמכותית. למידע קריטי מומלץ להיעזר בתרגום מקצועי שנערך על ידי מתרגם אנושי. איננו אחראים לכל אי‑הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->