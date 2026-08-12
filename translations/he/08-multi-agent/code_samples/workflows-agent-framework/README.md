# בניית יישומי רב-סוכנים עם זרימת עבודה של Microsoft Agent Framework

מדריך זה ינחה אותך להבנת בניית יישומי רב-סוכנים באמצעות Microsoft Agent Framework. נחקור את המושגים המרכזיים של מערכות רב-סוכנים, נדון בארכיטקטורת רכיב הזרימה של המסגרת, ונעבור על דוגמאות מעשיות ב-Python ו-.NET עבור תבניות זרימת עבודה שונות.

## 1\. הבנת מערכות רב-סוכנים

סוכן בינה מלאכותית הוא מערכת החורגת מהיכולות של מודל שפה גדול (LLM) סטנדרטי. הוא יכול לתפוס את הסביבה שלו, לקבל החלטות ולנקוט פעולות להשגת מטרות ספציפיות. מערכת רב-סוכנים כוללת מספר סוכנים שמשתפים פעולה לפתרון בעיה שקשה או בלתי אפשרי לסוכן יחיד להתמודד איתה לבד.

### תרחישי שימוש נפוצים

  * **פתרון בעיות מורכבות**: פירוק משימה גדולה (למשל תכנון אירוע רחב היקף בחברה) לתת-משימות הנמסרות לסוכנים מיומנים (למשל סוכן תקציב, סוכן לוגיסטיקה, סוכן שיווק).
  * **עוזרים וירטואליים**: סוכן עוזר ראשי שמפנה משימות כמו תיוג זמנים, מחקר והזמנות לסוכנים מיוחדים אחרים.
  * **יצירת תוכן אוטומטית**: זרימת עבודה שבה סוכן אחד כותב תוכן, אחר בודק דיוק וטון, וסוכן שלישי מפרסם את התוכן.

### דפוסי רב-סוכנים

מערכות רב-סוכנים יכולות להיות מאורגנות בכמה דפוסים, הקובעים כיצד הן מתקשרות ביניהן:

  * **רציף**: סוכנים פועלים לפי סדר מוגדר מראש, כמו קו ייצור. פלט של סוכן אחד הופך לקלט של הבא.
  * **מקביל**: סוכנים פועלים במקביל על חלקים שונים של המשימה, והתוצאות מתאגדות בסיום.
  * **תנאי**: זרימת העבודה עוקבת אחרי מסלולים שונים בהתאם לפלט של סוכן, בדומה לביטוי if-then-else.

## 2\. ארכיטקטורת זרימת העבודה של Microsoft Agent Framework

מערכת הזרימה של Agent Framework היא מנוע תזמור מתקדם שנועד לנהל אינטראקציות מורכבות בין סוכנים רבים. היא מבוססת על ארכיטקטורת גרף המשתמשת ב-[מודל ביצוע בסגנון Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), שבו העיבוד מתבצע בשלבים מסונכרנים הנקראים "supersteps".

### רכיבים מרכזיים

הארכיטקטורה מורכבת משלושה חלקים עיקריים:

1.  **מבצעים (Executors)**: אלה יחידות העיבוד היסודיות. בדוגמאות שלנו, `Agent` הוא סוג של מבצע. לכל מבצע יכולים להיות מספר מטפלי הודעות שמופעלים אוטומטית בהתאם לסוג ההודעה המתקבלת.
2.  **קצוות (Edges)**: מגדירים את המסלול שההודעות עוברות בין המבצעים. לקצוות יכולים להיות תנאים, המאפשרים ניתוב דינמי של המידע דרך גרף הזרימה.
3.  **זרימת עבודה (Workflow)**: רכיב זה מתזמן את התהליך כולו, מנהל את המבצעים, הקצוות וזרימת ההוצאה לפועל הכוללת. הוא מבטיח שההודעות מעובדות בסדר הנכון ומשדר אירועים לצפייה ומעקב.

*תרשים המתאר את הרכיבים המרכזיים של מערכת הזרימה.*

מבנה זה מאפשר בניית יישומים חזקים וסקלאביליים באמצעות דפוסים בסיסיים כמו שרשראות רציפות, fan-out/fan-in לעיבוד מקביל, ולוגיקת switch-case לזרימות מותנות.

## 3\. דוגמאות מעשיות וניתוח קוד

כעת נתבונן כיצד לממש דפוסי זרימת עבודה שונים באמצעות המסגרת. נבחן דוגמאות ב-Python וב-.NET לכל מקרה.

### מקרה 1: זרימת עבודה רציפה בסיסית

זהו הדפוס הפשוט ביותר, שבו פלט של סוכן אחד מועבר ישירות לאחר. התרחיש שלנו כולל סוכן `FrontDesk` במלון הממליץ על מסע, וההמלצה נבדקת על ידי סוכן `Concierge`.

*תרשים זרימת העבודה הבסיסית FrontDesk -> Concierge.*

#### רקע התרחיש

נוסע מבקש המלצה בפריז.

1.  סוכן `FrontDesk`, המיועד לתמציתיות, מציע לבקר במוזיאון הלובר.
2.  סוכן `Concierge`, שמעריך חוויות אותנטיות, מקבל את ההצעה. הוא בודק אותה ומספק משוב, מציע אלטרנטיבה יותר מקומית ופחות תיירותית.

#### ניתוח מימוש ב-Python

בדוגמא ב-Python אנו מגדירים ויוצרים את שני הסוכנים, כל אחד עם הוראות ספציפיות.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# הגדר תפקידים והוראות לסוכן
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# צור מופעי סוכן
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

לאחר מכן, נעשה שימוש ב-`WorkflowBuilder` לבניית הגרף. סוכן `front_desk_agent` מוגדר כנקודת התחלה, ונוצר קצה המקשר את הפלט שלו לסוכן `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

בסופו של דבר, זרימת העבודה מורצת עם הפקודה ההתחלתית של המשתמש.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run מפעיל את זרימת העבודה; get_outputs() מחזיר את תוצאת המבצע של הפלט.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### ניתוח מימוש ב-.NET (C#)

מימוש ה-.NET עוקב אחר לוגיקה דומה מאוד. תחילה מוגדרים קבועים עבור שמות והוראות הסוכנים.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

הסוכנים נוצרים בעזרת `AzureOpenAIClient` (Responses API), ואז `WorkflowBuilder` מגדיר את הזרימה הרציפה בכך שמוסיף קצה מ-`frontDeskAgent` אל `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

זרימת העבודה מורצת עם הודעת המשתמש, והתוצאות משודרות בחזרה.

### מקרה 2: זרימת עבודה רציפה מרובת שלבים

דפוס זה מרחיב את הרצף הבסיסי לכלול יותר סוכנים. הוא אידיאלי לתהליכים שדורשים שלבי עיבוד או שינוי מרובים.

#### רקע התרחיש

משתמש מספק תמונה של חדר מגורים ומבקש הצעת מחיר לריהוט.

1.  **סוכן מכירות**: מזהה את פריטי הריהוט בתמונה ויוצר רשימה.
2.  **סוכן מחירים**: מקבל את רשימת הפריטים ומספק פירוט מחירים, כולל אפשרויות תקציב, בינוניות ופרימיום.
3.  **סוכן הצעות מחיר**: מקבל את הרשימה המאורגנת ומעצב אותה למסמך הצעת מחיר רשמית בפורמט Markdown.

*תרשים זרימת העבודה Sales -> Price -> Quote.*

#### ניתוח מימוש ב-Python

מוגדרים שלושה סוכנים, כל אחד עם תפקיד מיוחד. זרימת העבודה נבנית באמצעות `add_edge` ליצירת שרשרת: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# צור שלושה סוכנים מתמחים
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# בנה את זרימת העבודה הסדרתי
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

הקלט הוא `ChatMessage` הכולל גם טקסט וגם URI לתמונה. המסגרת מנהלת העברת הפלט של כל סוכן לסוכן הבא ברצף עד להפקת הצעת המחיר הסופית.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# הודעת המשתמש מכילה גם טקסט וגם תמונה
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# הפעל את זרימת העבודה
events = await workflow.run(message)
```

#### ניתוח מימוש ב-.NET (C#)

דוגמת ה-.NET משקפת את גרסת הפייתון. שלושה סוכנים (`salesagent`, `priceagent`, `quoteagent`) נוצרים. `WorkflowBuilder` מקשר ביניהם בצורה רציפה.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

הודעת המשתמש בנויה עם נתוני תמונה (בבתים) והטקסט. שיטת `InProcessExecution.RunStreamingAsync` מפעילה את זרימת העבודה, והפלט הסופי נקלט מהזרם.

### מקרה 3: זרימת עבודה מקבילה

דפוס זה משמש כאשר משימות יכולות להתבצע בו זמנית לחיסכון בזמן. הוא כולל "פירוק" ל"מאות סוכנים" ו"אגירה" לאיסוף התוצאות.

#### רקע התרחיש

משתמש מבקש לתכנן טיול לסיאטל.

1.  **Dispatcher (Fan-Out)**: בקשת המשתמש נשלחת לשני סוכנים בו זמנית.
2.  **סוכן מחקר**: מחקר אטרקציות, מזג אוויר והתחשבות מרכזית לטיול בסיאטל בדצמבר.
3.  **סוכן תכנון**: יוצר תוכנית מסע מפורטת יום-יום באופן עצמאי.
4.  **Aggregator (Fan-In)**: איסוף ופירוט התוצאות משני הסוכנים ומצגתם כעת התוצאה הסופית.

*תרשים זרימת העבודה המקבילה Researcher ו-Planner.*

#### ניתוח מימוש ב-Python

`ConcurrentBuilder` מפשט את יצירת דפוס זה. פשוט מרשימים את הסוכנים המשתתפים, והבונה יוצר אוטומטית לוגיקת fan-out ו-fan-in הדרושה.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder מטפל בלוגיקת החלוקה/איחוד
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# הפעל את זרימת העבודה
events = await workflow.run("Plan a trip to Seattle in December")
```

המסגרת מבטיחה שה-`research_agent` וה-`plan_agent` יפעלו במקביל, והתוצאות הסופיות שלהם ייאספו לרשימה.

#### ניתוח מימוש ב-.NET (C#)

ב-.NET יש להגדיר זאת באופן מפורש יותר. מבצעים מותאמים אישית (`ConcurrentStartExecutor` ו-`ConcurrentAggregationExecutor`) נבנים לטיפול בלוגיקת fan-out ו-fan-in.

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

`WorkflowBuilder` משתמש ב-`AddFanOutEdge` ו-`AddFanInEdge` לבניית הגרף עם המבצעים המותאמים והסוכנים.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### מקרה 4: זרימת עבודה מותנית

זרימות עבודה מותנות מציגות לוגיקת הסתעפות, המאפשרת למערכת לבחור מסלולים שונים לפי תוצאות ביניים.

#### רקע התרחיש

זרימת עבודה זו מונעת אוטומטית יצירה ופרסום של מדריך טכני.

1.  **סוכן פרזנטור**: כותב טיוטה של המדריך על בסיס מתווה וכתובות URL נתונות.
2.  **סוכן בוחן תוכן**: בודק את הטיוטה. בודק האם מספר המילים מעל 200.
3.  **התפצלות מותנית**:
      * **אם מאושר (`כן`)**: זרימת העבודה ממשיכה אל `Publisher-Agent`.
      * **אם נדחה (`לא`)**: זרימת העבודה נעצרת ומודפסת סיבת הדחייה.
4.  **סוכן מפרסם**: אם הטיוטה מאושרת, הסוכן שומר את התוכן כקובץ Markdown.

#### ניתוח מימוש ב-Python

דוגמה זו משתמשת בפונקציה מותאמת אישית `select_targets` ליישום הלוגיקה המותנית. פונקציה זו מועברת ל-`add_multi_selection_edge_group` ומכוונת את זרימת העבודה בהתבסס על שדה `review_result` מפלט הבוחן.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# פונקציה זו קובעת את הצעד הבא בהתבסס על תוצאת הסקירה
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # אם מאושר, המשך למבצע 'save_draft'
        return [save_draft_id]
    else:
        # אם נדחה, המשך למבצע 'handle_review' לדיווח על כישלון
        return [handle_review_id]

# בנאי זרימת העבודה משתמש בפונקציית הבחירה לניתוב
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # הקצה מרובה הבחירה מיישם את הלוגיקה התנאי
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

מבצעים מותאמים כמו `to_reviewer_result` משמשים לפירוש פלט JSON מהסוכנים והמרתו לאובייקטים טיפוסיים שהפונקציה יכולה לבדוק.

#### ניתוח מימוש ב-.NET (C#)

בגרסת ה-.NET משתמשים בגישה דומה עם פונקציית תנאי. מוגדר `Func<object?, bool>` לבדיקת תכונת `Result` של אובייקט `ReviewResult`.

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

פרמטר ה-`condition` בשיטה `AddEdge` מאפשר ל-`WorkflowBuilder` ליצור מסלול התפצלות. זרימת העבודה תעקוב אחר הקצה אל `publishExecutor` רק אם התנאי `GetCondition(expectedResult: "Yes")` מחזיר true. אחרת, היא תעקוב אחרי המסלול אל `sendReviewerExecutor`.

## סיכום

Microsoft Agent Framework Workflow מספק בסיס חזק וגמיש לתזמור מערכות רב-סוכנים מורכבות. באמצעות ארכיטקטורת הגרפים והרכיבים המרכזיים, מפתחים יכולים לתכנן ולממש זרימות עבודה מתקדמות ב-Python וב-.NET. בין אם היישום שלך דורש עיבוד רציף פשוט, הרצה מקבילה או לוגיקה מותנית דינמית, המסגרת מציעה כלים לבניית פתרונות חכמים, סקלאביליים ובטוחים טיפוסית עם בינה מלאכותית.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->