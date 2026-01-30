# בניית יישומים מרובי סוכנים עם Microsoft Agent Framework Workflow

מדריך זה יסביר כיצד להבין ולבנות יישומים מרובי סוכנים באמצעות Microsoft Agent Framework. נחקור את המושגים המרכזיים של מערכות מרובות סוכנים, נעמיק בארכיטקטורה של רכיב ה-Workflow של המסגרת, ונעבור על דוגמאות מעשיות ב-Python וב-.NET עבור דפוסי עבודה שונים.

## 1\. הבנת מערכות מרובות סוכנים

סוכן AI הוא מערכת שמתקדמת מעבר ליכולות של מודל שפה גדול (LLM) סטנדרטי. הוא יכול לתפוס את סביבתו, לקבל החלטות ולבצע פעולות כדי להשיג מטרות ספציפיות. מערכת מרובת סוכנים כוללת מספר סוכנים כאלה שמשתפים פעולה כדי לפתור בעיה שקשה או בלתי אפשרי לפתור באמצעות סוכן יחיד.

### תרחישי יישום נפוצים

  * **פתרון בעיות מורכבות**: פירוק משימה גדולה (לדוגמה, תכנון אירוע לכל החברה) למשימות קטנות שמטופלות על ידי סוכנים מתמחים (לדוגמה, סוכן תקציב, סוכן לוגיסטיקה, סוכן שיווק).
  * **עוזרים וירטואליים**: סוכן עוזר ראשי שמאציל משימות כמו תזמון, מחקר והזמנות לסוכנים מתמחים אחרים.
  * **יצירת תוכן אוטומטית**: תהליך שבו סוכן אחד כותב טיוטה, סוכן אחר בודק אותה מבחינת דיוק וטון, וסוכן שלישי מפרסם אותה.

### דפוסי מערכות מרובות סוכנים

מערכות מרובות סוכנים יכולות להיות מאורגנות בכמה דפוסים, אשר קובעים כיצד הן מתקשרות:

  * **רציף**: סוכנים עובדים בסדר מוגדר מראש, כמו פס ייצור. התפוקה של סוכן אחד הופכת לקלט עבור הבא בתור.
  * **מקבילי**: סוכנים עובדים במקביל על חלקים שונים של משימה, והתוצאות שלהם מאוגדות בסוף.
  * **תנאי**: תהליך העבודה עוקב אחר מסלולים שונים בהתאם לתפוקה של סוכן, בדומה להצהרת if-then-else.

## 2\. ארכיטקטורת Workflow של Microsoft Agent Framework

מערכת ה-Workflow של המסגרת היא מנוע תזמור מתקדם שנועד לנהל אינטראקציות מורכבות בין סוכנים מרובים. היא בנויה על ארכיטקטורה מבוססת גרף שמשתמשת במודל ביצוע בסגנון [Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), שבו העיבוד מתבצע בשלבים מסונכרנים הנקראים "supersteps".

### רכיבים מרכזיים

הארכיטקטורה מורכבת משלושה חלקים עיקריים:

1.  **Executors**: יחידות העיבוד הבסיסיות. בדוגמאות שלנו, `Agent` הוא סוג של executor. לכל executor יכולים להיות מספר מטפלי הודעות שמופעלים אוטומטית בהתאם לסוג ההודעה שהתקבלה.
2.  **Edges**: מגדירים את המסלול שהודעות עוברות בין ה-executors. ל-Edges יכולים להיות תנאים, שמאפשרים ניתוב דינמי של מידע דרך גרף ה-Workflow.
3.  **Workflow**: רכיב זה מתזמר את כל התהליך, מנהל את ה-executors, ה-edges, ואת זרימת הביצוע הכוללת. הוא מבטיח שהודעות מעובדות בסדר הנכון ומשדר אירועים לצורך תצפית.

*תרשים שממחיש את הרכיבים המרכזיים של מערכת ה-Workflow.*

מבנה זה מאפשר בניית יישומים חזקים וניתנים להרחבה באמצעות דפוסים בסיסיים כמו שרשראות רציפות, fan-out/fan-in לעיבוד מקבילי, ולוגיקת switch-case לזרימות תנאים.

## 3\. דוגמאות מעשיות וניתוח קוד

כעת, נחקור כיצד ליישם דפוסי עבודה שונים באמצעות המסגרת. נבחן קוד ב-Python וב-.NET עבור כל דוגמה.

### מקרה 1: Workflow רציף בסיסי

זהו הדפוס הפשוט ביותר, שבו התפוקה של סוכן אחד מועברת ישירות לסוכן אחר. התרחיש שלנו כולל סוכן `FrontDesk` של המלון שממליץ על טיול, ולאחר מכן סוכן `Concierge` שבודק את ההמלצה.

*תרשים של Workflow בסיסי FrontDesk -> Concierge.*

#### רקע התרחיש

מטייל מבקש המלצה בפריז.

1.  סוכן `FrontDesk`, שמתמקד בקיצור, מציע לבקר במוזיאון הלובר.
2.  סוכן `Concierge`, שמעדיף חוויות אותנטיות, מקבל את ההצעה. הוא בודק את ההמלצה ומספק משוב, ומציע חלופה מקומית ופחות תיירותית.

#### ניתוח יישום ב-Python

בדוגמה ב-Python, אנו קודם מגדירים ויוצרים את שני הסוכנים, כל אחד עם הוראות ספציפיות.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

לאחר מכן, משתמשים ב-`WorkflowBuilder` כדי לבנות את הגרף. סוכן `front_desk_agent` מוגדר כנקודת ההתחלה, ונוצר edge שמחבר את התפוקה שלו ל-`reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

לבסוף, ה-Workflow מבוצע עם ההנחיה הראשונית של המשתמש.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### ניתוח יישום ב-.NET (C#)

היישום ב-.NET עוקב אחר לוגיקה דומה מאוד. תחילה, מוגדרים קבועים עבור שמות הסוכנים וההוראות שלהם.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

הסוכנים נוצרים באמצעות `OpenAIClient`, ולאחר מכן `WorkflowBuilder` מגדיר את הזרימה הרציפה על ידי הוספת edge מ-`frontDeskAgent` ל-`reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

ה-Workflow מופעל עם הודעת המשתמש, והתוצאות משודרות בחזרה.

### מקרה 2: Workflow רציף רב-שלבי

דפוס זה מרחיב את הרצף הבסיסי לכלול יותר סוכנים. הוא אידיאלי לתהליכים שדורשים מספר שלבי עיבוד או שינוי.

#### רקע התרחיש

משתמש מספק תמונה של סלון ומבקש הצעת מחיר לריהוט.

1.  **Sales-Agent**: מזהה את פריטי הריהוט בתמונה ויוצר רשימה.
2.  **Price-Agent**: לוקח את רשימת הפריטים ומספק פירוט מחירים, כולל אפשרויות תקציב, ביניים ופרימיום.
3.  **Quote-Agent**: מקבל את הרשימה עם המחירים ומעצב אותה למסמך הצעת מחיר פורמלי ב-Markdown.

*תרשים של Workflow Sales -> Price -> Quote.*

#### ניתוח יישום ב-Python

שלושה סוכנים מוגדרים, כל אחד עם תפקיד ייחודי. ה-Workflow נבנה באמצעות `add_edge` ליצירת שרשרת: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

הקלט הוא `ChatMessage` שכולל גם טקסט וגם URI של התמונה. המסגרת מטפלת בהעברת התפוקה של כל סוכן לבא בתור ברצף עד שהצעת המחיר הסופית נוצרת.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# The user message contains both text and an image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Run the workflow
async for event in workflow.run_stream(message):
    ...
```

#### ניתוח יישום ב-.NET (C#)

הדוגמה ב-.NET משקפת את הגרסה ב-Python. שלושה סוכנים (`salesagent`, `priceagent`, `quoteagent`) נוצרים. `WorkflowBuilder` מקשר אותם ברצף.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

הודעת המשתמש נבנית עם נתוני התמונה (כבתים) והטקסט. שיטת `InProcessExecution.StreamAsync` מפעילה את ה-Workflow, והתפוקה הסופית נתפסת מהזרם.

### מקרה 3: Workflow מקבילי

דפוס זה משמש כאשר ניתן לבצע משימות בו-זמנית כדי לחסוך זמן. הוא כולל "fan-out" למספר סוכנים ו-"fan-in" לאיגוד התוצאות.

#### רקע התרחיש

משתמש מבקש לתכנן טיול לסיאטל.

1.  **Dispatcher (Fan-Out)**: בקשת המשתמש נשלחת לשני סוכנים בו-זמנית.
2.  **Researcher-Agent**: חוקר אטרקציות, מזג אוויר ושיקולים מרכזיים לטיול בסיאטל בדצמבר.
3.  **Plan-Agent**: יוצר באופן עצמאי מסלול טיול מפורט לפי ימים.
4.  **Aggregator (Fan-In)**: התפוקות משני הסוכנים נאספות ומוצגות יחד כתוצאה סופית.

*תרשים של Workflow מקבילי Researcher ו-Planner.*

#### ניתוח יישום ב-Python

ה-`ConcurrentBuilder` מפשט את יצירת דפוס זה. פשוט מציינים את הסוכנים המשתתפים, וה-builder יוצר אוטומטית את לוגיקת ה-fan-out וה-fan-in הנדרשת.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

המסגרת מבטיחה שה-`research_agent` וה-`plan_agent` מבוצעים במקביל, והתפוקות הסופיות שלהם נאספות לרשימה.

#### ניתוח יישום ב-.NET (C#)

ב-.NET, דפוס זה דורש הגדרה מפורשת יותר. Executors מותאמים אישית (`ConcurrentStartExecutor` ו-`ConcurrentAggregationExecutor`) נוצרים כדי לטפל בלוגיקת ה-fan-out וה-fan-in.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

ה-`WorkflowBuilder` משתמש ב-`AddFanOutEdge` וב-`AddFanInEdge` כדי לבנות את הגרף עם ה-executors המותאמים והסוכנים.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### מקרה 4: Workflow תנאי

Workflows תנאיים מציגים לוגיקת הסתעפות, שמאפשרת למערכת לבחור מסלולים שונים בהתאם לתוצאות ביניים.

#### רקע התרחיש

Workflow זה מבצע אוטומציה ליצירה ופרסום של מדריך טכני.

1.  **Evangelist-Agent**: כותב טיוטה של המדריך בהתבסס על מתווה ו-URLs נתונים.
2.  **ContentReviewer-Agent**: בודק את הטיוטה. הוא בודק אם מספר המילים עולה על 200.
3.  **הסתעפות תנאית**:
      * **אם מאושר (`Yes`)**: ה-Workflow ממשיך ל-`Publisher-Agent`.
      * **אם נדחה (`No`)**: ה-Workflow נעצר ומציג את סיבת הדחייה.
4.  **Publisher-Agent**: אם הטיוטה מאושרת, סוכן זה שומר את התוכן לקובץ Markdown.

#### ניתוח יישום ב-Python

בדוגמה זו משתמשים בפונקציה מותאמת אישית, `select_targets`, כדי ליישם את הלוגיקה התנאית. פונקציה זו מועברת ל-`add_multi_selection_edge_group` ומכוונת את ה-Workflow בהתבסס על השדה `review_result` מתפוקת הסוקר.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# This function determines the next step based on the review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If approved, proceed to the 'save_draft' executor
        return [save_draft_id]
    else:
        # If rejected, proceed to the 'handle_review' executor to report failure
        return [handle_review_id]

# The workflow builder uses the selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # The multi-selection edge implements the conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Executors מותאמים אישית כמו `to_reviewer_result` משמשים לניתוח פלט JSON מהסוכנים ולהמרתו לאובייקטים חזקים שהפונקציה יכולה לבדוק.

#### ניתוח יישום ב-.NET (C#)

הגרסה ב-.NET משתמשת בגישה דומה עם פונקציית תנאי. מוגדר `Func<object?, bool>` כדי לבדוק את המאפיין `Result` של אובייקט `ReviewResult`.

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

הפרמטר `condition` של שיטת `AddEdge` מאפשר ל-`WorkflowBuilder` ליצור מסלול הסתעפות. ה-Workflow יעקוב אחר ה-edge ל-`publishExecutor` רק אם התנאי `GetCondition(expectedResult: "Yes")` מחזיר true. אחרת, הוא יעקוב אחר המסלול ל-`sendReviewerExecutor`.

## סיכום

Microsoft Agent Framework Workflow מספק בסיס חזק וגמיש לתזמור מערכות מורכבות מרובות סוכנים. באמצעות ארכיטקטורה מבוססת גרף ורכיבים מרכזיים, מפתחים יכולים לעצב וליישם Workflows מתוחכמים ב-Python וב-.NET. בין אם היישום שלך דורש עיבוד רציף פשוט, ביצוע מקבילי או לוגיקה תנאית דינמית, המסגרת מציעה את הכלים לבניית פתרונות AI חזקים, ניתנים להרחבה ובטוחים.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.