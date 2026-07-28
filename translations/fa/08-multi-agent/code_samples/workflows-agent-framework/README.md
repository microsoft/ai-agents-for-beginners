# ساخت برنامه‌های چندعامله با استفاده از گردش کار Microsoft Agent Framework

این راهنما شما را در درک و ساخت برنامه‌های چندعامله با استفاده از Microsoft Agent Framework راهنمایی می‌کند. ما مفاهیم اصلی سیستم‌های چندعامله را بررسی می‌کنیم، به معماری مؤلفه گردش کار فریم‌ورک می‌پردازیم، و از طریق مثال‌های عملی به زبان‌های Python و .NET برای الگوهای مختلف گردش کار قدم خواهیم زد.

## 1\. درک سیستم‌های چندعامله

عامل هوش مصنوعی (AI Agent) سیستمی است که فراتر از توانایی‌های یک مدل زبان بزرگ استاندارد (LLM) عمل می‌کند. این سیستم می‌تواند محیط خود را درک کند، تصمیم بگیرد و اقداماتی برای رسیدن به اهداف خاص انجام دهد. یک سیستم چندعامله شامل چندین عامل است که همکارانه برای حل مشکلی که برای یک عامل واحد مشکل‌زا یا غیرممکن است، کار می‌کنند.

### سناریوهای معمول کاربردی

  * **حل مسائل پیچیده**: تقسیم یک وظیفه بزرگ (مثلاً برنامه‌ریزی یک رویداد شرکتی) به وظایف کوچکتر که توسط عوامل تخصصی مدیریت می‌شوند (مثلاً عامل بودجه، عامل لجستیک، عامل بازاریابی).
  * **دستیارهای مجازی**: یک عامل دستیار اصلی وظایفی مثل برنامه‌ریزی، تحقیق و رزرو را به عوامل تخصصی دیگر واگذار می‌کند.
  * **ایجاد محتوای خودکار**: گردش کاری که در آن یک عامل پیش‌نویس محتوا را می‌نویسد، عامل دیگر برای دقت و لحن آن را بررسی می‌کند، و عامل سوم آن را منتشر می‌کند.

### الگوهای چندعامله

سیستم‌های چندعامله می‌توانند در چند الگو سازماندهی شوند که نحوه تعامل آن‌ها را مشخص می‌کند:

  * **متوالی**: عوامل به ترتیب از پیش تعریف شده‌ای کار می‌کنند، مانند یک خط مونتاژ. خروجی یک عامل ورودی عامل بعدی است.
  * **همزمان**: عوامل به طور موازی روی بخش‌های مختلف یک وظیفه کار می‌کنند و نتایج آن‌ها در پایان جمع‌آوری می‌شود.
  * **شرطی**: گردش کار بر اساس خروجی یک عامل مسیرهای مختلفی را دنبال می‌کند، مانند یک عبارت if-then-else.

## ۲\. معماری گردش کار Microsoft Agent Framework

سیستم گردش کار Agent Framework یک موتور اورکستراسیون پیشرفته است که برای مدیریت تعاملات پیچیده بین چندین عامل طراحی شده است. این سیستم بر پایه معماری مبتنی بر گراف ساخته شده که از مدل اجرای [Pregel-style](https://kowshik.github.io/JPregel/pregel_paper.pdf) استفاده می‌کند، جایی که پردازش در گام‌های همزمان به نام "supersteps" انجام می‌شود.

### مؤلفه‌های اصلی

معماری شامل سه بخش اصلی است:

1.  **اجراکنندگان (Executors)**: این‌ها واحدهای پردازش اصلی هستند. در مثال‌های ما، `Agent` نوعی اجراکننده است. هر اجراکننده می‌تواند چندین هندلر پیام داشته باشد که بر اساس نوع پیام دریافتی به‌طور خودکار فراخوانی می‌شوند.
2.  **لبه‌ها (Edges)**: این‌ها مسیر رفتن پیام‌ها بین اجراکننده‌ها را تعریف می‌کنند. لبه‌ها می‌توانند شرایط داشته باشند که اجازه می‌دهد مسیردهی اطلاعات در گراف گردش کار به صورت پویا انجام شود.
3.  **گردش کار (Workflow)**: این مؤلفه کل فرآیند را هماهنگ می‌کند، اجراکننده‌ها، لبه‌ها و جریان کلی اجرا را مدیریت می‌کند. اطمینان می‌دهد که پیام‌ها به ترتیب درست پردازش می‌شوند و رویدادها را برای مشاهده‌پذیری جریان می‌دهد.

*یک نمودار که مؤلفه‌های اصلی سیستم گردش کار را نشان می‌دهد.*

این ساختار امکان ساخت برنامه‌های مقاوم و مقیاس‌پذیر با استفاده از الگوهای پایه مانند زنجیره‌های متوالی، fan-out/fan-in برای پردازش موازی، و منطق switch-case برای جریان‌های شرطی را فراهم می‌کند.

## ۳\. مثال‌های عملی و تحلیل کد

حال بیایید ببینیم چگونه می‌توان الگوهای مختلف گردش کار را با استفاده از این فریم‌ورک پیاده‌سازی کرد. برای هر مثال، کدهای Python و .NET را بررسی می‌کنیم.

### مورد ۱: گردش کار متوالی پایه

این ساده‌ترین الگو است که در آن خروجی یک عامل مستقیماً به عامل دیگری منتقل می‌شود. سناریوی ما شامل یک عامل `FrontDesk` در هتل است که یک توصیه سفر می‌دهد و سپس این توصیه توسط یک عامل `Concierge` بررسی می‌شود.

*نمودار گردش کار پایه FrontDesk -\> Concierge.*

#### پیش‌زمینه سناریو

یک مسافر درخواست توصیه‌ای برای پاریس می‌دهد.

1.  عامل `FrontDesk` که برای اختصار طراحی شده، پیشنهاد بازدید از موزه لوور را می‌دهد.
2.  عامل `Concierge` که تجربه‌های واقعی را اولویت می‌دهد، این پیشنهاد را دریافت می‌کند، بررسی می‌کند و بازخورد می‌دهد و پیشنهاد جایگزینی محلی و کمتر گردشگری ارائه می‌دهد.

#### تحلیل پیاده‌سازی Python

در مثال Python، ابتدا دو عامل تعریف و ساخته می‌شوند، هر کدام با دستورات مشخص.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# تعریف نقش‌ها و دستورالعمل‌های عامل
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# ایجاد نمونه‌های عامل
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

سپس از `WorkflowBuilder` برای ساخت گراف استفاده می‌شود. `front_desk_agent` به عنوان نقطه شروع تنظیم شده و یک لبه برای اتصال خروجی آن به `reviewer_agent` ایجاد می‌شود.

```python
# ۰۱.فریم‌ورک-عامل-پایتون-جریان‌کاری-ghmodel-پایه.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

در نهایت، گردش کار با پیام اولیه کاربر اجرا می‌شود.

```python
# ۰۱.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run روند کاری را اجرا می‌کند؛ get_outputs() نتیجه‌ی اجرای خروجی را برمی‌گرداند.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### تحلیل پیاده‌سازی .NET (C\#)

پیاده‌سازی .NET منطق بسیار مشابهی دنبال می‌کند. ابتدا ثابت‌هایی برای نام و دستورالعمل‌های عوامل تعریف می‌شوند.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

عوامل با استفاده از `AzureOpenAIClient` (API پاسخ‌ها) ساخته می‌شوند، سپس `WorkflowBuilder` جریان متوالی را با افزودن لبه‌ای از `frontDeskAgent` به `reviewerAgent` تعریف می‌کند.

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

گردش کار سپس با پیام کاربر اجرا شده و نتایج به صورت جریانی بازگردانده می‌شوند.

### مورد ۲: گردش کار متوالی چندمرحله‌ای

این الگو توالی پایه را گسترش می‌دهد تا شامل عوامل بیشتری باشد. این برای فرآیندهایی که نیاز به مراحل متعدد پالایش یا تبدیل دارند، ایده‌آل است.

#### پیش‌زمینه سناریو

یک کاربر تصویر یک اتاق نشیمن را ارائه می‌دهد و درخواست قیمت مبلمان دارد.

1.  **عامل فروش**: اقلام مبلمان را در تصویر شناسایی کرده و لیستی ایجاد می‌کند.
2.  **عامل قیمت**: لیست اقلام را گرفته و تجزیه و تحلیل دقیق قیمت ارائه می‌دهد، شامل گزینه‌های بودجه‌ای، میان رده و پریمیوم.
3.  **عامل پیشنهاد قیمت**: لیست قیمت‌گذاری شده را دریافت کرده و آن را به یک سند رسمی در قالب Markdown تبدیل می‌کند.

*نمودار گردش کار Sales -\> Price -\> Quote.*

#### تحلیل پیاده‌سازی Python

سه عامل تعریف شده‌اند که هر کدام نقش خاصی دارند. گردش کار با استفاده از `add_edge` زنجیره‌ای ایجاد کرده: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# سه عامل تخصصی بسازید
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# روند کاری متوالی را بسازید
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ورودی یک `ChatMessage` است که هم متن و هم URI تصویر را شامل می‌شود. فریم‌ورک خروجی هر عامل را به عامل بعدی منتقل می‌کند تا زمانی که پیشنهاد قیمت نهایی ایجاد شود.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# پیام کاربر شامل هر دو متن و تصویر است
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# اجرای روند کاری
events = await workflow.run(message)
```

#### تحلیل پیاده‌سازی .NET (C\#)

مثال .NET نسخه Python را بازتاب می‌دهد. سه عامل (`salesagent`, `priceagent`, `quoteagent`) ساخته می‌شوند و `WorkflowBuilder` آن‌ها را به ترتیب متصل می‌کند.

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

پیام کاربر با داده تصویر (به صورت بایت) و متن فرستاده شده ساخته می‌شود. متد `InProcessExecution.RunStreamingAsync` گردش کار را آغاز می‌کند و خروجی نهایی از جریان گرفته می‌شود.

### مورد ۳: گردش کار همزمان

این الگو زمانی استفاده می‌شود که کارها بتوانند به طور همزمان انجام شوند تا در زمان صرفه‌جویی شود. این الگو شامل "fan-out" به چند عامل و "fan-in" برای جمع‌آوری نتایج است.

#### پیش‌زمینه سناریو

یک کاربر درخواست برنامه‌ریزی سفر به سیاتل می‌دهد.

1.  **واسط (Fan-Out)**: درخواست کاربر به دو عامل به طور همزمان فرستاده می‌شود.
2.  **عامل تحقیق**: جاذبه‌ها، آب‌وهوا و نکات کلیدی سفر به سیاتل در دسامبر را تحقیق می‌کند.
3.  **عامل برنامه‌ریز**: به طور مستقل برنامه سفر روز به روز را ایجاد می‌کند.
4.  **جمع کننده (Fan-In)**: خروجی‌های هر دو عامل تحقیق و برنامه‌ریز جمع‌آوری شده و به عنوان نتیجه نهایی ارائه می‌شود.

*نمودار گردش کار همزمان عوامل Researcher و Planner.*

#### تحلیل پیاده‌سازی Python

`ConcurrentBuilder` ساخت این الگو را ساده می‌کند. کافی است لیست عوامل شرکت‌کننده را ارائه دهید و سازنده به‌طور خودکار منطق fan-out و fan-in مورد نیاز را ایجاد می‌کند.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder منطق پخش/جمع‌آوری همزمان را مدیریت می‌کند
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# اجرای جریان کار
events = await workflow.run("Plan a trip to Seattle in December")
```

فریم‌ورک اطمینان می‌دهد که `research_agent` و `plan_agent` به صورت موازی اجرا می‌شوند و خروجی نهایی آن‌ها در یک لیست جمع‌آوری می‌شود.

#### تحلیل پیاده‌سازی .NET (C\#)

در .NET، این الگو نیاز به تعریف صریح‌تری دارد. اجراکننده‌های سفارشی (`ConcurrentStartExecutor` و `ConcurrentAggregationExecutor`) برای مدیریت منطق fan-out و fan-in ساخته می‌شوند.

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

سپس `WorkflowBuilder` از `AddFanOutEdge` و `AddFanInEdge` برای ساخت گراف با این اجراکننده‌های سفارشی و عوامل استفاده می‌کند.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### مورد ۴: گردش کار شرطی

گردش کارهای شرطی منطق انشعاب را معرفی می‌کنند، به طوری که سیستم بتواند بر اساس نتایج میانی مسیرهای مختلف را انتخاب کند.

#### پیش‌زمینه سناریو

این گردش کار ایجاد و انتشار خودکار یک آموزش فنی را انجام می‌دهد.

1.  **عامل مبلّغ**: پیش‌نویس آموزش را بر اساس یک طرح کلی و آدرس‌های وب می‌نویسد.
2.  **عامل بازبین محتوا**: پیش‌نویس را بررسی می‌کند و چک می‌کند که تعداد کلمات بیش از ۲۰۰ باشد.
3.  **انشعاب شرطی**:
      * **اگر پذیرفته شد (`بله`)**: گردش کار به عامل «انتشار دهنده» می‌رود.
      * **اگر رد شد (`خیر`)**: گردش کار متوقف شده و دلیل رد شدن نمایش داده می‌شود.
۴.  **عامل انتشار**: اگر پیش‌نویس پذیرفته شود، این عامل محتوای آموزش را در یک فایل Markdown ذخیره می‌کند.

#### تحلیل پیاده‌سازی Python

این مثال از یک تابع سفارشی به نام `select_targets` برای پیاده‌سازی منطق شرطی استفاده می‌کند. این تابع به `add_multi_selection_edge_group` داده شده و گردش کار را بر اساس فیلد `review_result` از خروجی بازبین کنترل می‌کند.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# این تابع گام بعدی را بر اساس نتیجه بررسی تعیین می‌کند
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # اگر تایید شد، به اجرای‌کننده 'save_draft' ادامه دهید
        return [save_draft_id]
    else:
        # اگر رد شد، به اجرای‌کننده 'handle_review' برای گزارش شکست ادامه دهید
        return [handle_review_id]

# سازنده گردش کار از تابع انتخاب برای مسیر‌یابی استفاده می‌کند
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # لبه چند انتخابی منطق شرطی را پیاده‌سازی می‌کند
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

اجراکننده‌های سفارشی مانند `to_reviewer_result` برای تجزیه خروجی JSON عوامل به اشیاء typed استفاده می‌شوند که تابع انتخاب بتواند آن‌ها را بررسی کند.

#### تحلیل پیاده‌سازی .NET (C\#)

نسخه .NET همین رویکرد را با استفاده از تابع شرطی دارد. یک `Func<object?, bool>` برای بررسی ویژگی `Result` از شیء `ReviewResult` تعریف شده است.

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

پارامتر `condition` در متد `AddEdge` اجازه می‌دهد `WorkflowBuilder` مسیر انشعابی ایجاد کند. گردش کار فقط در صورتی لبه‌ به `publishExecutor` را دنبال می‌کند که شرط `GetCondition(expectedResult: "Yes")` برقرار باشد، وگرنه مسیر به `sendReviewerExecutor` می‌رود.

## نتیجه‌گیری

Microsoft Agent Framework Workflow پایه‌ای قوی و انعطاف‌پذیر برای هماهنگی سیستم‌های پیچیده چندعامله فراهم می‌کند. با بهره‌گیری از معماری مبتنی بر گراف و مؤلفه‌های اصلی آن، توسعه‌دهندگان می‌توانند گردش‌های کاری پیچیده را در هر دو زبان Python و .NET طراحی و پیاده‌سازی کنند. چه برنامه شما نیاز به پردازش متوالی ساده، اجرای موازی، یا منطق شرطی پویا داشته باشد، این فریم‌ورک ابزارهای لازم برای ساخت راه‌حل‌های هوش مصنوعی قدرتمند، مقیاس‌پذیر و نوع‌ایمن را فراهم می‌کند.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->