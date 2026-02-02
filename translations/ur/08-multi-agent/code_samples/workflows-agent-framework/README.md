# Microsoft Agent Framework Workflow کے ساتھ ملٹی ایجنٹ ایپلیکیشنز بنانا

یہ ٹیوٹوریل آپ کو Microsoft Agent Framework کا استعمال کرتے ہوئے ملٹی ایجنٹ ایپلیکیشنز کو سمجھنے اور بنانے کے عمل میں رہنمائی کرے گا۔ ہم ملٹی ایجنٹ سسٹمز کے بنیادی تصورات کو دریافت کریں گے، فریم ورک کے ورک فلو جزو کی آرکیٹیکچر میں گہرائی سے جائیں گے، اور Python اور .NET میں مختلف ورک فلو پیٹرنز کے عملی مثالوں کا جائزہ لیں گے۔

## 1\. ملٹی ایجنٹ سسٹمز کو سمجھنا

AI ایجنٹ ایک ایسا نظام ہے جو ایک عام Large Language Model (LLM) کی صلاحیتوں سے آگے بڑھتا ہے۔ یہ اپنے ماحول کو سمجھ سکتا ہے، فیصلے کر سکتا ہے، اور مخصوص اہداف حاصل کرنے کے لیے اقدامات کر سکتا ہے۔ ملٹی ایجنٹ سسٹم میں کئی ایجنٹس شامل ہوتے ہیں جو مل کر ایسے مسئلے کو حل کرتے ہیں جو ایک واحد ایجنٹ کے لیے مشکل یا ناممکن ہو۔

### عام ایپلیکیشن کے منظرنامے

  * **پیچیدہ مسئلہ حل کرنا**: ایک بڑے کام (جیسے کمپنی کے وسیع ایونٹ کی منصوبہ بندی) کو چھوٹے ذیلی کاموں میں تقسیم کرنا، جنہیں خصوصی ایجنٹس (جیسے بجٹ ایجنٹ، لاجسٹکس ایجنٹ، مارکیٹنگ ایجنٹ) سنبھالتے ہیں۔
  * **ورچوئل اسسٹنٹس**: ایک بنیادی اسسٹنٹ ایجنٹ جو شیڈولنگ، تحقیق، اور بکنگ جیسے کاموں کو دوسرے خصوصی ایجنٹس کو تفویض کرتا ہے۔
  * **خودکار مواد تخلیق**: ایک ورک فلو جہاں ایک ایجنٹ مواد کا مسودہ تیار کرتا ہے، دوسرا اسے درستگی اور لہجے کے لیے جائزہ لیتا ہے، اور تیسرا اسے شائع کرتا ہے۔

### ملٹی ایجنٹ پیٹرنز

ملٹی ایجنٹ سسٹمز کو کئی پیٹرنز میں منظم کیا جا سکتا ہے، جو ان کے تعامل کا تعین کرتے ہیں:

  * **تسلسل وار**: ایجنٹس ایک مقررہ ترتیب میں کام کرتے ہیں، جیسے اسمبلی لائن۔ ایک ایجنٹ کا آؤٹ پٹ اگلے ایجنٹ کے لیے ان پٹ بن جاتا ہے۔
  * **متوازی**: ایجنٹس ایک کام کے مختلف حصوں پر ایک ساتھ کام کرتے ہیں، اور ان کے نتائج آخر میں جمع کیے جاتے ہیں۔
  * **مشروط**: ورک فلو مختلف راستوں پر چلتا ہے، ایجنٹ کے آؤٹ پٹ کی بنیاد پر، جیسے if-then-else بیان۔

## 2\. Microsoft Agent Framework Workflow آرکیٹیکچر

ایجنٹ فریم ورک کا ورک فلو سسٹم ایک جدید آرکیسٹریشن انجن ہے جو متعدد ایجنٹس کے درمیان پیچیدہ تعاملات کو منظم کرنے کے لیے ڈیزائن کیا گیا ہے۔ یہ ایک گراف پر مبنی آرکیٹیکچر پر بنایا گیا ہے جو [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf) استعمال کرتا ہے، جہاں پروسیسنگ "supersteps" کہلانے والے ہم آہنگ مراحل میں ہوتی ہے۔

### بنیادی اجزاء

آرکیٹیکچر تین اہم حصوں پر مشتمل ہے:

1.  **Executors**: یہ بنیادی پروسیسنگ یونٹس ہیں۔ ہمارے مثالوں میں، `Agent` ایک قسم کا executor ہے۔ ہر executor کے پاس متعدد میسج ہینڈلرز ہو سکتے ہیں جو موصول ہونے والے میسج کی قسم کی بنیاد پر خود بخود فعال ہوتے ہیں۔
2.  **Edges**: یہ وہ راستے ہیں جن پر میسجز executors کے درمیان سفر کرتے ہیں۔ Edges میں شرائط ہو سکتی ہیں، جو ورک فلو گراف کے ذریعے معلومات کی متحرک روٹنگ کی اجازت دیتی ہیں۔
3.  **Workflow**: یہ جزو پورے عمل کو منظم کرتا ہے، executors، edges، اور مجموعی طور پر عمل کے بہاؤ کو سنبھالتا ہے۔ یہ یقینی بناتا ہے کہ میسجز صحیح ترتیب میں پروسیس ہوں اور مشاہدہ کے لیے ایونٹس کو اسٹریم کرتا ہے۔

*ورک فلو سسٹم کے بنیادی اجزاء کی وضاحت کرنے والا ایک خاکہ۔*

یہ ساخت بنیادی پیٹرنز جیسے تسلسل وار چینز، متوازی پروسیسنگ کے لیے fan-out/fan-in، اور مشروط بہاؤ کے لیے switch-case منطق کا استعمال کرتے ہوئے مضبوط اور قابل توسیع ایپلیکیشنز بنانے کی اجازت دیتی ہے۔

## 3\. عملی مثالیں اور کوڈ تجزیہ

اب، آئیے فریم ورک کا استعمال کرتے ہوئے مختلف ورک فلو پیٹرنز کو نافذ کرنے کا طریقہ دریافت کریں۔ ہم ہر مثال کے لیے Python اور .NET کوڈ دیکھیں گے۔

### کیس 1: بنیادی تسلسل وار ورک فلو

یہ سب سے آسان پیٹرن ہے، جہاں ایک ایجنٹ کا آؤٹ پٹ براہ راست دوسرے کو منتقل کیا جاتا ہے۔ ہمارا منظرنامہ ایک ہوٹل کے `FrontDesk` ایجنٹ پر مشتمل ہے جو سفر کی سفارش کرتا ہے، جسے پھر ایک `Concierge` ایجنٹ جائزہ لیتا ہے۔

*بنیادی FrontDesk -> Concierge ورک فلو کا خاکہ۔*

#### منظرنامے کا پس منظر

ایک مسافر پیرس میں سفارش طلب کرتا ہے۔

1.  `FrontDesk` ایجنٹ، جو اختصار کے لیے ڈیزائن کیا گیا ہے، Louvre Museum کا دورہ کرنے کی تجویز دیتا ہے۔
2.  `Concierge` ایجنٹ، جو مستند تجربات کو ترجیح دیتا ہے، اس تجویز کو وصول کرتا ہے۔ یہ سفارش کا جائزہ لیتا ہے اور ایک زیادہ مقامی، کم سیاحتی متبادل تجویز کرتا ہے۔

#### Python نفاذ کا تجزیہ

Python مثال میں، ہم پہلے دو ایجنٹس کو مخصوص ہدایات کے ساتھ تعریف اور تخلیق کرتے ہیں۔

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

اس کے بعد، `WorkflowBuilder` کا استعمال گراف بنانے کے لیے کیا جاتا ہے۔ `front_desk_agent` کو نقطہ آغاز کے طور پر مقرر کیا جاتا ہے، اور اس کے آؤٹ پٹ کو `reviewer_agent` سے جوڑنے کے لیے ایک edge بنایا جاتا ہے۔

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

آخر میں، ورک فلو کو ابتدائی صارف کے پرامپٹ کے ساتھ چلایا جاتا ہے۔

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) نفاذ کا تجزیہ

.NET نفاذ بہت ملتی جلتی منطق پر عمل کرتا ہے۔ پہلے، ایجنٹس کے ناموں اور ہدایات کے لیے constants کی تعریف کی جاتی ہے۔

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

ایجنٹس کو `OpenAIClient` کا استعمال کرتے ہوئے تخلیق کیا جاتا ہے، اور پھر `WorkflowBuilder` تسلسل وار بہاؤ کی وضاحت کرتا ہے، `frontDeskAgent` سے `reviewerAgent` تک edge شامل کر کے۔

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

ورک فلو پھر صارف کے پیغام کے ساتھ چلایا جاتا ہے، اور نتائج کو اسٹریم کیا جاتا ہے۔

### کیس 2: ملٹی اسٹیپ تسلسل وار ورک فلو

یہ پیٹرن بنیادی تسلسل کو مزید ایجنٹس شامل کرنے کے لیے بڑھاتا ہے۔ یہ ان عملوں کے لیے مثالی ہے جنہیں کئی مراحل کی اصلاح یا تبدیلی کی ضرورت ہوتی ہے۔

#### منظرنامے کا پس منظر

ایک صارف ایک رہائشی کمرے کی تصویر فراہم کرتا ہے اور فرنیچر کے کوٹ کی درخواست کرتا ہے۔

1.  **Sales-Agent**: تصویر میں موجود فرنیچر آئٹمز کی شناخت کرتا ہے اور ایک فہرست بناتا ہے۔
2.  **Price-Agent**: آئٹمز کی فہرست لیتا ہے اور بجٹ، درمیانی رینج، اور پریمیم آپشنز سمیت تفصیلی قیمت کا تجزیہ فراہم کرتا ہے۔
3.  **Quote-Agent**: قیمت شدہ فہرست وصول کرتا ہے اور اسے Markdown میں ایک رسمی کوٹ دستاویز میں فارمیٹ کرتا ہے۔

*Sales -> Price -> Quote ورک فلو کا خاکہ۔*

#### Python نفاذ کا تجزیہ

تین ایجنٹس کی تعریف کی جاتی ہے، ہر ایک کے پاس ایک مخصوص کردار ہوتا ہے۔ ورک فلو `add_edge` کا استعمال کرتے ہوئے ایک چین بنانے کے لیے تعمیر کیا جاتا ہے: `sales_agent` -> `price_agent` -> `quote_agent`۔

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ان پٹ ایک `ChatMessage` ہے جس میں متن اور تصویر کا URI شامل ہوتا ہے۔ فریم ورک ہر ایجنٹ کے آؤٹ پٹ کو اگلے ایجنٹ تک پہنچانے کا انتظام کرتا ہے، جب تک کہ حتمی کوٹ تیار نہ ہو جائے۔

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

#### .NET (C#) نفاذ کا تجزیہ

.NET مثال Python ورژن کی عکاسی کرتی ہے۔ تین ایجنٹس (`salesagent`, `priceagent`, `quoteagent`) تخلیق کیے جاتے ہیں۔ `WorkflowBuilder` انہیں تسلسل وار جوڑتا ہے۔

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

صارف کا پیغام تصویر کے ڈیٹا (bytes کی صورت میں) اور متن پرامپٹ کے ساتھ بنایا جاتا ہے۔ `InProcessExecution.StreamAsync` طریقہ ورک فلو کو شروع کرتا ہے، اور حتمی آؤٹ پٹ اسٹریم سے حاصل کیا جاتا ہے۔

### کیس 3: متوازی ورک فلو

یہ پیٹرن اس وقت استعمال ہوتا ہے جب کام ایک ساتھ انجام دیے جا سکتے ہوں تاکہ وقت بچایا جا سکے۔ اس میں "fan-out" کئی ایجنٹس کو اور "fan-in" نتائج کو جمع کرنے کے لیے شامل ہوتا ہے۔

#### منظرنامے کا پس منظر

ایک صارف سیئٹل کا سفر منصوبہ بنانے کی درخواست کرتا ہے۔

1.  **Dispatcher (Fan-Out)**: صارف کی درخواست کو ایک ہی وقت میں دو ایجنٹس کو بھیجا جاتا ہے۔
2.  **Researcher-Agent**: سیئٹل میں دسمبر کے دوران سفر کے لیے کشش، موسم، اور کلیدی غور و فکر کی تحقیق کرتا ہے۔
3.  **Plan-Agent**: آزادانہ طور پر دن بہ دن تفصیلی سفر کا منصوبہ بناتا ہے۔
4.  **Aggregator (Fan-In)**: محقق اور منصوبہ ساز دونوں کے آؤٹ پٹس کو جمع کیا جاتا ہے اور حتمی نتیجے کے طور پر پیش کیا جاتا ہے۔

*متوازی Researcher اور Planner ورک فلو کا خاکہ۔*

#### Python نفاذ کا تجزیہ

`ConcurrentBuilder` اس پیٹرن کی تخلیق کو آسان بناتا ہے۔ آپ صرف شامل ایجنٹس کی فہرست دیتے ہیں، اور بلڈر خود بخود ضروری fan-out اور fan-in منطق تخلیق کرتا ہے۔

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

فریم ورک اس بات کو یقینی بناتا ہے کہ `research_agent` اور `plan_agent` متوازی طور پر عمل کریں، اور ان کے حتمی آؤٹ پٹس کو ایک فہرست میں جمع کیا جائے۔

#### .NET (C#) نفاذ کا تجزیہ

.NET میں، اس پیٹرن کے لیے زیادہ واضح تعریف کی ضرورت ہوتی ہے۔ کسٹم executors (`ConcurrentStartExecutor` اور `ConcurrentAggregationExecutor`) fan-out اور fan-in منطق کو سنبھالنے کے لیے تخلیق کیے جاتے ہیں۔

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

`WorkflowBuilder` پھر `AddFanOutEdge` اور `AddFanInEdge` کا استعمال کرتے ہوئے گراف کو ان کسٹم executors اور ایجنٹس کے ساتھ تعمیر کرتا ہے۔

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### کیس 4: مشروط ورک فلو

مشروط ورک فلو شاخوں کی منطق متعارف کراتے ہیں، جو نظام کو درمیانی نتائج کی بنیاد پر مختلف راستے اختیار کرنے کی اجازت دیتے ہیں۔

#### منظرنامے کا پس منظر

یہ ورک فلو ایک تکنیکی ٹیوٹوریل کی تخلیق اور اشاعت کو خودکار بناتا ہے۔

1.  **Evangelist-Agent**: دیے گئے خاکے اور URLs کی بنیاد پر ٹیوٹوریل کا مسودہ تیار کرتا ہے۔
2.  **ContentReviewer-Agent**: مسودے کا جائزہ لیتا ہے۔ یہ چیک کرتا ہے کہ آیا لفظوں کی تعداد 200 سے زیادہ ہے۔
3.  **مشروط شاخ**:
      * **اگر منظور شدہ (`Yes`)**: ورک فلو `Publisher-Agent` کی طرف بڑھتا ہے۔
      * **اگر مسترد شدہ (`No`)**: ورک فلو رک جاتا ہے اور مسترد ہونے کی وجہ آؤٹ پٹ کرتا ہے۔
4.  **Publisher-Agent**: اگر مسودہ منظور ہو جائے، تو یہ ایجنٹ مواد کو Markdown فائل میں محفوظ کرتا ہے۔

#### Python نفاذ کا تجزیہ

اس مثال میں ایک کسٹم فنکشن، `select_targets`، مشروط منطق کو نافذ کرنے کے لیے استعمال کیا جاتا ہے۔ یہ فنکشن `add_multi_selection_edge_group` کو پاس کیا جاتا ہے اور `review_result` فیلڈ کی بنیاد پر ورک فلو کو ہدایت دیتا ہے۔

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

کسٹم executors جیسے `to_reviewer_result` ایجنٹس کے JSON آؤٹ پٹ کو تجزیہ کرتے ہیں اور اسے مضبوطی سے ٹائپ شدہ اشیاء میں تبدیل کرتے ہیں جنہیں انتخابی فنکشن معائنہ کر سکتا ہے۔

#### .NET (C#) نفاذ کا تجزیہ

.NET ورژن ایک مشروط فنکشن کے ساتھ اسی طرح کے طریقے کا استعمال کرتا ہے۔ ایک `Func<object?, bool>` تعریف کی جاتی ہے تاکہ `ReviewResult` آبجیکٹ کی `Result` پراپرٹی کو چیک کیا جا سکے۔

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

`AddEdge` طریقہ کے `condition` پیرامیٹر کی اجازت دیتا ہے کہ `WorkflowBuilder` ایک شاخ والا راستہ تخلیق کرے۔ ورک فلو صرف اس وقت `publishExecutor` کی طرف edge کی پیروی کرے گا جب شرط `GetCondition(expectedResult: "Yes")` درست لوٹائے۔ بصورت دیگر، یہ `sendReviewerExecutor` کی طرف راستہ اختیار کرے گا۔

## نتیجہ

Microsoft Agent Framework Workflow پیچیدہ، ملٹی ایجنٹ سسٹمز کو منظم کرنے کے لیے ایک مضبوط اور لچکدار بنیاد فراہم کرتا ہے۔ اس کے گراف پر مبنی آرکیٹیکچر اور بنیادی اجزاء کا فائدہ اٹھا کر، ڈویلپرز Python اور .NET میں نفیس ورک فلو ڈیزائن اور نافذ کر سکتے ہیں۔ چاہے آپ کی ایپلیکیشن کو سادہ تسلسل وار پروسیسنگ، متوازی عمل درآمد، یا متحرک مشروط منطق کی ضرورت ہو، فریم ورک طاقتور، قابل توسیع، اور ٹائپ سیف AI سے چلنے والے حل بنانے کے لیے ٹولز فراہم کرتا ہے۔

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔