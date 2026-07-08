# בניית יישומי רב-נותני שירות עם זרימת העבודה של Microsoft Agent Framework

מדריך זה ינחה אותך בהבנת ובבניית יישומי רב-נותני שירות באמצעות Microsoft Agent Framework. נחקור את המושגים המרכזיים של מערכות רב-נותני שירות, נצלול לארכיטקטורת מרכיב זרימת העבודה במסגרת, ונעסוק בדוגמאות מעשיות הן בפייתון והן ב-.NET עבור תבניות זרימת עבודה שונות.

## 1\. הבנת מערכות רב-נותני שירות

סוכן AI הוא מערכת החורגת מהיכולות של מודל שפה גדול (LLM) סטנדרטי. הוא יכול לתפוס את סביבתו, לקבל החלטות, ולנקוט בפעולות להשגת מטרות ספציפיות. מערכת רב-נותני שירות כוללת מספר סוכנים אלו הפועלים בשיתוף לפתרון בעיה שיהיה קשה או בלתי אפשרי לסוכן יחיד להתמודד איתה לבד.

### תרחישי יישום נפוצים

  * **פתרון בעיות מורכבות**: חלוקת משימה גדולה (למשל, תכנון אירוע ארגוני) לתת-משימות קטנות המנוהלות על ידי סוכנים מיוחדים (למשל, סוכן תקציב, סוכן לוגיסטיקה, סוכן שיווק).
  * **עוזרים וירטואליים**: סוכן עוזר ראשי שמפנה משימות כמו תזמון, מחקר, והזמנות לסוכנים מיוחדים אחרים.
  * **יצירת תוכן אוטומטית**: זרימת עבודה שבה סוכן אחד מנסח תוכן, אחר בודק את דיוקו וטונו, ושלישי מפרסם אותו.

### תבניות רב-סוכניות

מערכות רב-נותני שירות יכולות להיות מאורגנות בכמה תבניות, אשר קובעות כיצד הן מתקשרות:

  * **רציף**: סוכנים פועלים בסדר מוגדר מראש, כמו קו ייצור. הפלט של סוכן אחד הופך לקלט של הבא.
  * **מקביל**: הסוכנים עובדים בו-זמנית על חלקים שונים של משימה, ותוצאותיהם נאספות בסיום.
  * **תנאי**: זרימת העבודה פועלת בדרכים שונות בהתאם לפלט של סוכן, בדומה לפקודת if-then-else.

## 2\. ארכיטקטורת זרימת העבודה של Microsoft Agent Framework

מערכת זרימת העבודה במסגרת Agent Framework היא מנוע אדרכה מתקדם שנועד לנהל אינטראקציות מורכבות בין סוכנים מרובים. היא מבוססת על ארכיטקטורת גרף המשתמשת ב-[מודל ביצוע בסגנון Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), שבו העיבוד מתרחש בשלבים מסונכרנים הנקראים "supersteps".

### מרכיבים מרכזיים

הארכיטקטורה מורכבת משלושה חלקים עיקריים:

1.  **מבצעים (Executors)**: אלו יחידות העיבוד הבסיסיות. בדוגמאות שלנו, `Agent` הוא סוג של מבצע. לכל מבצע יכולים להיות מטפלי הודעות מרובים שנקראים אוטומטית בהתאם לסוג ההודעה שהתקבלה.
2.  **קשתות (Edges)**: מגדירות את המסלול שהודעות עוברות בין מבצעים. לקשתות יכולות להיות תנאים, המאפשרים ניתוב דינמי של מידע דרך גרף זרימת העבודה.
3.  **זרימת עבודה (Workflow)**: רכיב זה מנחה את כל התהליך, מנהל את המבצעים, הקשתות וזרימת ההרצה הכוללת. הוא מבטיח שההודעות מעובדות בסדר הנכון ומזרם אירועים לצורך נראות.

*דיאגרמה המדגימה את המרכיבים המרכזיים של מערכת זרימת העבודה.*

מבנה זה מאפשר בנייה של יישומים יציבים וניתנים להרחבה באמצעות תבניות יסוד כמו שרשרות רציפות, fan-out/fan-in לעיבוד מקביל, ולוגיקת switch-case לזרימות תנאיות.

## 3\. דוגמאות מעשיות וניתוח קוד

כעת נבחן כיצד ליישם תבניות זרימת עבודה שונות באמצעות המסגרת. נסקור קוד בפייתון וב-.NET עבור כל דוגמה.

### מקרה 1: זרימת עבודה בסיסית רציפה

זוהי התבנית הפשוטה ביותר, שבה פלט סוכן אחד מועבר ישירות לאחר. התרחיש שלנו כולל סוכן `FrontDesk` של בית המלון הממליץ על נסיעה, שאחר כך נבדק על ידי סוכן `Concierge`.

*דיאגרמה של זרימת עבודה בסיסית FrontDesk -> Concierge.*

#### רקע התרחיש

נוסע מבקש המלצה בפריז.

1.  סוכן `FrontDesk`, המתוכנן בקצרה, מציע ביקור במוזיאון הלובר.
2.  סוכן `Concierge`, שמעדיף חוויות אותנטיות, מקבל את ההצעה. הוא בודק את ההמלצה ומספק משוב, מציע אלטרנטיבה מקומית פחות תיירותית.

#### ניתוח מימוש בפייתון

בדוגמת הפייתון, קודם מגדירים ויוצרים את שני הסוכנים, כל אחד עם הנחיות ספציפיות.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# הגדר תפקידים והוראות לסוכן
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# צור מופעים של סוכנים
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

לאחר מכן, משתמשים ב-`WorkflowBuilder` כדי לבנות את הגרף. `front_desk_agent` מוגדר כנקודת התחלה, ויוצרת קשת שמחברת את פלטו אל `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

בסיום, זרימת העבודה מורצת עם הפקודה הראשונית של המשתמש.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# הפעלת הזרימה; get_outputs() מחזירה את התוצאה של המבצע הפלט.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### ניתוח מימוש ב-.NET (C#)

המימוש ב-.NET עוקב אחרי לוגיקה דומה מאד. תחילה מגדירים קבועים לשמות הסוכנים וההנחיות שלהם.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

הסוכנים נוצרים באמצעות `AzureOpenAIClient` (Responses API), ואז `WorkflowBuilder` מגדיר את הזרימה הרציפה על ידי הוספת קשת מ-`frontDeskAgent` אל `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

את זרימת העבודה מפעילים עם הודעת המשתמש, והתוצאות מוזרמות חזרה.

### מקרה 2: זרימת עבודה רציפה מרובת שלבים

תבנית זו מרחיבה את הרצף הבסיסי לכלול יותר סוכנים. היא אידיאלית לתהליכים שדורשים מספר שלבי גימור או המרה.

#### רקע התרחיש

משתמש מספק תמונה של חדר מגורים ומבקש הצעת מחיר לרהיטים.

1.  **סוכן מכירות**: מזהה את פריטי הריהוט בתמונה ויוצר רשימה.
2.  **סוכן מחירים**: מקבל את הרשימה ומספק פירוט מחירים, כולל אפשרויות תקציב, ביניים ופרימיום.
3.  **סוכן הצעות מחיר**: מקבל את הרשימה המחושבת ומעצב אותה למסמך הצעת מחיר רשמי ב-Markdown.

*דיאגרמה של זרימת עבודה Sales -> Price -> Quote.*

#### ניתוח מימוש בפייתון

שלושה סוכנים מוגדרים, כל אחד עם תפקיד מיוחד. זרימת העבודה נבנית באמצעות `add_edge` לשרשרת: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# צור שלושה סוכנים מתמחים
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# בנה את רצף תהליך העבודה
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

הקלט הוא `ChatMessage` הכולל טקסט ו-URI לתמונה. המסגרת מטפלת בהעברת פלט כל סוכן לבא אחריו ברצף עד ליצירת ההצעה הסופית.

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

# הרץ את תהליך העבודה
events = await workflow.run(message)
```

#### ניתוח מימוש ב-.NET (C#)

דוגמת ה-.NET משקפת את גרסת הפייתון. יוצרים שלושה סוכנים (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` מקשר ביניהם ברצף.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent priceagent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent quoteagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

הודעת המשתמש נבנית עם נתוני התמונה (בבתים) והפקודה הטקסטואלית. שיטת `InProcessExecution.StreamAsync` משיקה את זרימת העבודה, והפלט הסופי נאסף מהזרם.

### מקרה 3: זרימת עבודה מקבילה

תבנית זו משמשת כאשר משימות ניתן לבצע במקביל לחיסכון בזמן. היא כוללת "fan-out" למספר סוכנים ו-"fan-in" לאיסוף התוצאות.

#### רקע התרחיש

משתמש מבקש לתכנן טיול לסיאטל.

1.  **Dispatcher (Fan-Out)**: בקשת המשתמש נשלחת לשני סוכנים בו-זמנית.
2.  **סוכן מחקר**: חוקר אטרקציות, מזג אוויר ושיקולים מרכזיים לטיול בסיאטל בדצמבר.
3.  **סוכן תכנון**: יוצר באופן עצמאי מסלול טיול מפורט יום-יום.
4.  **Aggregator (Fan-In)**: התוצרים מהחוקר ומהמתכנן נאספים ומוצגים יחד כתוצאה הסופית.

*דיאגרמה של זרימת עבודה משותפת לחוקר ולמתכנן.*

#### ניתוח מימוש בפייתון

ה-`ConcurrentBuilder` מפשט את יצירת התבנית הזו. פשוט מפורטים הסוכנים המשתתפים, והבונה יוצר אוטומטית את לוגיקת ה-fan-out וה-fan-in הנדרשת.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder מטפל בלוגיקת פיצול ואיחוד
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# הפעל את זרימת העבודה
events = await workflow.run("Plan a trip to Seattle in December")
```

המסגרת מוודאת שה-`research_agent` וה-`plan_agent` מבצעים במקביל, ותוצאותיהם הסופיות נאספות לרשימה.

#### ניתוח מימוש ב-.NET (C#)

ב-.NET תבנית זו דורשת הגדרה מפורשת יותר. נוצרים מבצעים מותאמים אישית (`ConcurrentStartExecutor` ו-`ConcurrentAggregationExecutor`) לטיפול בלוגיקת ה-fan-out וה-fan-in.

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

לאחר מכן, `WorkflowBuilder` משתמש ב-`AddFanOutEdge` וב-`AddFanInEdge` לבניית הגרף עם המבצעים המותאמים אישית והסוכנים.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### מקרה 4: זרימת עבודה מותנית

זרימות עבודה מותנות מציגות לוגיקת התפצלות, ומאפשרות למערכת לבחור בדרכים שונות בהתאם לתוצאות ביניים.

#### רקע התרחיש

זרימת עבודה זו מיישמת אוטומציה של יצירה ופרסום של מדריך טכני.

1.  **סוכן Evanלגיסט**: כותב טיוטת המדריך על בסיס מתווה וכתובות URL נתונות.
2.  **סוכן ContentReviewer**: בודק את הטיוטה. בודק אם מספר המילים עולה על 200.
3.  **סניף מותנה**:
      * **אם מאושר (`כן`)**: הזרימה ממשיכה לסוכן ה-Publisher.
      * **אם נדחה (`לא`)**: הזרימה נעצרת ומפיקה את סיבת הדחייה.
4.  **סוכן Publisher**: אם הטיוטה מאושרת, סוכן זה שומר את התוכן לקובץ Markdown.

#### ניתוח מימוש בפייתון

דוגמה זו משתמשת בפונקציה מותאמת אישית, `select_targets`, ליישום הלוגיקה המותנית. פונקציה זו מועברת ל-`add_multi_selection_edge_group` ומכוונת את זרימת העבודה בהתבסס על שדה `review_result` מהפלט של הסוקר.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# פונקציה זו קובעת את השלב הבא בהתבסס על תוצאת הסקירה
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # אם מאושר, המשך למבצע 'save_draft'
        return [save_draft_id]
    else:
        # אם נדחה, המשך למבצע 'handle_review' לדווח על כישלון
        return [handle_review_id]

# בונה תהליך העבודה משתמש בפונקציית הבחירה לניתוב
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # הקצה עם הבחירה המרובה מיישם את הלוגיקה המותנית
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

מבצעים מותאמים אישית כמו `to_reviewer_result` משמשים לניתוח פלט JSON מהסוכנים ולהמרתו לאובייקטים מסוגח הניתנים לבחינה על ידי פונקציית הבחירה.

#### ניתוח מימוש ב-.NET (C#)

גרסת ה-.NET משתמשת בגישה דומה עם פונקציית תנאי. מוגדר `Func<object?, bool>` לבדיקה של תכונת `Result` של אובייקט `ReviewResult`.

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

פרמטר `condition` של שיטת `AddEdge` מאפשר ל-`WorkflowBuilder` ליצור מסלול התפצלות. זרימת העבודה תעקוב אחרי הקשת ל-`publishExecutor` רק אם התנאי `GetCondition(expectedResult: "Yes")` מחזיר אמת. אחרת, הזרימה תעקוב אחרי המסלול ל-`sendReviewerExecutor`.

## סיכום

Microsoft Agent Framework Workflow מספקת בסיס חזק וגמיש לאדריכלות מערכות מורכבות רב-סוכניות. באמצעות הארכיטקטורה מבוססת הגרף ומרכיביה המרכזיים, מפתחים יכולים לעצב וליישם זרימות עבודה מתקדמות בפייתון וב-.NET. בין אם היישום שלך דורש עיבוד רציף פשוט, ביצוע מקביל, או לוגיקה דינמית מותנית, המסגרת מציעה את הכלים לבניית פתרונות AI רבי עוצמה, ניתנים להרחבה ובטוחים טיפוסית.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->