# ساخت برنامه‌های چندعاملی با جریان کاری Microsoft Agent Framework

این آموزش شما را در درک و ساخت برنامه‌های چندعاملی با استفاده از Microsoft Agent Framework راهنمایی می‌کند. ما مفاهیم اصلی سیستم‌های چندعاملی را بررسی می‌کنیم، به معماری مؤلفه جریان کاری این فریم‌ورک می‌پردازیم و مثال‌های عملی در پایتون و .NET برای الگوهای مختلف جریان کاری ارائه می‌دهیم.

## 1. درک سیستم‌های چندعاملی

یک عامل هوش مصنوعی سیستمی است که فراتر از قابلیت‌های یک مدل زبان بزرگ (LLM) استاندارد عمل می‌کند. این عامل می‌تواند محیط خود را درک کند، تصمیم‌گیری کند و اقداماتی را برای دستیابی به اهداف خاص انجام دهد. یک سیستم چندعاملی شامل چندین عامل است که با همکاری یکدیگر مشکلی را حل می‌کنند که برای یک عامل واحد دشوار یا غیرممکن است.

### سناریوهای رایج کاربرد

  * **حل مسائل پیچیده**: تقسیم یک وظیفه بزرگ (مانند برنامه‌ریزی یک رویداد در سطح شرکت) به وظایف کوچک‌تر که توسط عوامل تخصصی انجام می‌شود (مانند عامل بودجه، عامل لجستیک، عامل بازاریابی).
  * **دستیارهای مجازی**: یک عامل دستیار اصلی وظایفی مانند زمان‌بندی، تحقیق و رزرو را به عوامل تخصصی دیگر واگذار می‌کند.
  * **ایجاد محتوای خودکار**: یک جریان کاری که در آن یک عامل محتوا را پیش‌نویس می‌کند، عامل دیگر آن را از نظر دقت و لحن بررسی می‌کند و عامل سوم آن را منتشر می‌کند.

### الگوهای چندعاملی

سیستم‌های چندعاملی می‌توانند به چندین الگو سازماندهی شوند که نحوه تعامل آن‌ها را تعیین می‌کند:

  * **توالی**: عوامل به ترتیب مشخصی کار می‌کنند، مانند یک خط مونتاژ. خروجی یک عامل به عنوان ورودی عامل بعدی استفاده می‌شود.
  * **هم‌زمان**: عوامل به صورت موازی روی بخش‌های مختلف یک وظیفه کار می‌کنند و نتایج آن‌ها در پایان جمع‌آوری می‌شود.
  * **شرطی**: جریان کاری بر اساس خروجی یک عامل مسیرهای مختلفی را دنبال می‌کند، مشابه یک عبارت if-then-else.

## 2. معماری جریان کاری Microsoft Agent Framework

سیستم جریان کاری این فریم‌ورک یک موتور ارکستراسیون پیشرفته است که برای مدیریت تعاملات پیچیده بین عوامل متعدد طراحی شده است. این سیستم بر اساس معماری مبتنی بر گراف ساخته شده است که از مدل اجرایی [Pregel-style](https://kowshik.github.io/JPregel/pregel_paper.pdf) استفاده می‌کند، جایی که پردازش در مراحل هماهنگ به نام "سوپرمرحله‌ها" انجام می‌شود.

### اجزای اصلی

معماری از سه بخش اصلی تشکیل شده است:

1. **اجراکننده‌ها**: این‌ها واحدهای پردازشی بنیادی هستند. در مثال‌های ما، یک `Agent` نوعی اجراکننده است. هر اجراکننده می‌تواند چندین هندلر پیام داشته باشد که به طور خودکار بر اساس نوع پیام دریافتی فراخوانی می‌شوند.
2. **لبه‌ها**: این‌ها مسیرهایی را تعریف می‌کنند که پیام‌ها بین اجراکننده‌ها طی می‌کنند. لبه‌ها می‌توانند شرایطی داشته باشند که امکان مسیریابی پویا اطلاعات از طریق گراف جریان کاری را فراهم می‌کند.
3. **جریان کاری**: این مؤلفه کل فرآیند را ارکستراسیون می‌کند، اجراکننده‌ها، لبه‌ها و جریان کلی اجرا را مدیریت می‌کند. همچنین اطمینان حاصل می‌کند که پیام‌ها به ترتیب صحیح پردازش می‌شوند و رویدادها را برای مشاهده‌پذیری جریان می‌دهد.

*یک نمودار که اجزای اصلی سیستم جریان کاری را نشان می‌دهد.*

این ساختار امکان ساخت برنامه‌های قدرتمند و مقیاس‌پذیر را با استفاده از الگوهای بنیادی مانند زنجیره‌های ترتیبی، پردازش موازی fan-out/fan-in و منطق switch-case برای جریان‌های شرطی فراهم می‌کند.

## 3. مثال‌های عملی و تحلیل کد

اکنون به بررسی نحوه پیاده‌سازی الگوهای مختلف جریان کاری با استفاده از این فریم‌ورک می‌پردازیم. ما کدهای پایتون و .NET را برای هر مثال بررسی خواهیم کرد.

### مورد 1: جریان کاری ترتیبی ساده

این ساده‌ترین الگو است که در آن خروجی یک عامل مستقیماً به عامل دیگر منتقل می‌شود. سناریوی ما شامل یک عامل `FrontDesk` هتل است که توصیه‌ای برای سفر ارائه می‌دهد و سپس توسط یک عامل `Concierge` بررسی می‌شود.

*نمودار جریان کاری FrontDesk -> Concierge ساده.*

#### پیش‌زمینه سناریو

یک مسافر درخواست توصیه‌ای برای پاریس می‌کند.

1. عامل `FrontDesk` که برای اختصار طراحی شده است، پیشنهاد بازدید از موزه لوور را می‌دهد.
2. عامل `Concierge` که تجربیات اصیل را در اولویت قرار می‌دهد، این پیشنهاد را دریافت می‌کند. آن را بررسی کرده و بازخوردی ارائه می‌دهد، پیشنهاد جایگزینی محلی و کمتر توریستی را ارائه می‌دهد.

#### تحلیل پیاده‌سازی در پایتون

در مثال پایتون، ابتدا دو عامل تعریف و ایجاد می‌شوند که هر کدام دستورالعمل‌های خاص خود را دارند.

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

سپس از `WorkflowBuilder` برای ساخت گراف استفاده می‌شود. عامل `front_desk_agent` به عنوان نقطه شروع تنظیم شده و یک لبه برای اتصال خروجی آن به `reviewer_agent` ایجاد می‌شود.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

در نهایت، جریان کاری با درخواست اولیه کاربر اجرا می‌شود.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### تحلیل پیاده‌سازی در .NET (C#)

پیاده‌سازی .NET منطق بسیار مشابهی را دنبال می‌کند. ابتدا ثابت‌هایی برای نام‌ها و دستورالعمل‌های عوامل تعریف می‌شوند.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

عوامل با استفاده از `OpenAIClient` ایجاد می‌شوند و سپس `WorkflowBuilder` جریان ترتیبی را با افزودن یک لبه از `frontDeskAgent` به `reviewerAgent` تعریف می‌کند.

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

سپس جریان کاری با پیام کاربر اجرا می‌شود و نتایج به صورت جریان بازگردانده می‌شوند.

### مورد 2: جریان کاری ترتیبی چندمرحله‌ای

این الگو جریان ترتیبی ساده را گسترش می‌دهد تا شامل عوامل بیشتری شود. این الگو برای فرآیندهایی که نیاز به مراحل متعدد پالایش یا تبدیل دارند، ایده‌آل است.

#### پیش‌زمینه سناریو

یک کاربر تصویری از یک اتاق نشیمن ارائه می‌دهد و درخواست قیمت‌گذاری مبلمان می‌کند.

1. **Sales-Agent**: اقلام مبلمان موجود در تصویر را شناسایی کرده و لیستی ایجاد می‌کند.
2. **Price-Agent**: لیست اقلام را گرفته و جزئیات قیمت‌گذاری شامل گزینه‌های بودجه‌ای، میان‌رده و لوکس را ارائه می‌دهد.
3. **Quote-Agent**: لیست قیمت‌گذاری شده را دریافت کرده و آن را به یک سند نقل‌قول رسمی در قالب Markdown تبدیل می‌کند.

*نمودار جریان کاری Sales -> Price -> Quote.*

#### تحلیل پیاده‌سازی در پایتون

سه عامل تعریف می‌شوند که هر کدام نقش تخصصی دارند. جریان کاری با استفاده از `add_edge` برای ایجاد یک زنجیره: `sales_agent` -> `price_agent` -> `quote_agent` ساخته می‌شود.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ورودی یک `ChatMessage` است که شامل متن و URI تصویر است. فریم‌ورک خروجی هر عامل را به عامل بعدی در توالی منتقل می‌کند تا زمانی که نقل‌قول نهایی تولید شود.

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

#### تحلیل پیاده‌سازی در .NET (C#)

مثال .NET نسخه پایتون را منعکس می‌کند. سه عامل (`salesagent`, `priceagent`, `quoteagent`) ایجاد می‌شوند. `WorkflowBuilder` آن‌ها را به صورت ترتیبی پیوند می‌دهد.

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

پیام کاربر با داده‌های تصویر (به صورت بایت) و متن درخواست ساخته می‌شود. روش `InProcessExecution.StreamAsync` جریان کاری را آغاز می‌کند و خروجی نهایی از جریان گرفته می‌شود.

### مورد 3: جریان کاری هم‌زمان

این الگو زمانی استفاده می‌شود که وظایف بتوانند به طور هم‌زمان انجام شوند تا زمان صرفه‌جویی شود. این الگو شامل "fan-out" به چندین عامل و "fan-in" برای جمع‌آوری نتایج است.

#### پیش‌زمینه سناریو

یک کاربر درخواست برنامه‌ریزی سفر به سیاتل را می‌کند.

1. **Dispatcher (Fan-Out)**: درخواست کاربر به طور هم‌زمان به دو عامل ارسال می‌شود.
2. **Researcher-Agent**: جاذبه‌ها، آب‌وهوا و نکات کلیدی برای سفر به سیاتل در دسامبر را بررسی می‌کند.
3. **Plan-Agent**: به طور مستقل یک برنامه سفر روزانه دقیق ایجاد می‌کند.
4. **Aggregator (Fan-In)**: خروجی‌های محقق و برنامه‌ریز جمع‌آوری شده و به عنوان نتیجه نهایی ارائه می‌شوند.

*نمودار جریان کاری هم‌زمان Researcher و Planner.*

#### تحلیل پیاده‌سازی در پایتون

`ConcurrentBuilder` ایجاد این الگو را ساده می‌کند. شما فقط عوامل شرکت‌کننده را لیست می‌کنید و سازنده به طور خودکار منطق fan-out و fan-in لازم را ایجاد می‌کند.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

فریم‌ورک اطمینان حاصل می‌کند که `research_agent` و `plan_agent` به طور موازی اجرا می‌شوند و خروجی‌های نهایی آن‌ها در یک لیست جمع‌آوری می‌شوند.

#### تحلیل پیاده‌سازی در .NET (C#)

در .NET، این الگو نیاز به تعریف صریح‌تر دارد. اجراکننده‌های سفارشی (`ConcurrentStartExecutor` و `ConcurrentAggregationExecutor`) برای مدیریت منطق fan-out و fan-in ایجاد می‌شوند.

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

### مورد 4: جریان کاری شرطی

جریان‌های کاری شرطی منطق شاخه‌ای را معرفی می‌کنند و به سیستم اجازه می‌دهند بر اساس نتایج میانی مسیرهای مختلفی را دنبال کند.

#### پیش‌زمینه سناریو

این جریان کاری ایجاد و انتشار خودکار یک آموزش فنی را انجام می‌دهد.

1. **Evangelist-Agent**: پیش‌نویس آموزش را بر اساس یک طرح کلی و URLهای داده شده می‌نویسد.
2. **ContentReviewer-Agent**: پیش‌نویس را بررسی می‌کند. بررسی می‌کند که آیا تعداد کلمات بیش از 200 کلمه است.
3. **شاخه شرطی**:
      * **اگر تأیید شد (`Yes`)**: جریان کاری به `Publisher-Agent` ادامه می‌دهد.
      * **اگر رد شد (`No`)**: جریان کاری متوقف شده و دلیل رد شدن را خروجی می‌دهد.
4. **Publisher-Agent**: اگر پیش‌نویس تأیید شود، این عامل محتوا را به یک فایل Markdown ذخیره می‌کند.

#### تحلیل پیاده‌سازی در پایتون

این مثال از یک تابع سفارشی، `select_targets`، برای پیاده‌سازی منطق شرطی استفاده می‌کند. این تابع به `add_multi_selection_edge_group` منتقل شده و جریان کاری را بر اساس فیلد `review_result` از خروجی بازبین هدایت می‌کند.

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

اجراکننده‌های سفارشی مانند `to_reviewer_result` برای تجزیه خروجی JSON از عوامل و تبدیل آن به اشیاء نوعی که تابع انتخاب می‌تواند بررسی کند، استفاده می‌شوند.

#### تحلیل پیاده‌سازی در .NET (C#)

نسخه .NET از رویکرد مشابهی با یک تابع شرطی استفاده می‌کند. یک `Func<object?, bool>` تعریف می‌شود تا ویژگی `Result` از شیء `ReviewResult` را بررسی کند.

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

پارامتر `condition` روش `AddEdge` به `WorkflowBuilder` اجازه می‌دهد یک مسیر شاخه‌ای ایجاد کند. جریان کاری فقط لبه به `publishExecutor` را دنبال می‌کند اگر شرط `GetCondition(expectedResult: "Yes")` مقدار true را برگرداند. در غیر این صورت، مسیر به `sendReviewerExecutor` دنبال می‌شود.

## نتیجه‌گیری

Microsoft Agent Framework Workflow یک پایه قدرتمند و انعطاف‌پذیر برای ارکستراسیون سیستم‌های پیچیده چندعاملی فراهم می‌کند. با استفاده از معماری مبتنی بر گراف و اجزای اصلی آن، توسعه‌دهندگان می‌توانند جریان‌های کاری پیچیده را در پایتون و .NET طراحی و پیاده‌سازی کنند. چه برنامه شما نیاز به پردازش ترتیبی ساده، اجرای موازی یا منطق شرطی پویا داشته باشد، این فریم‌ورک ابزارهایی را برای ساخت راه‌حل‌های قدرتمند، مقیاس‌پذیر و ایمن ارائه می‌دهد.

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.