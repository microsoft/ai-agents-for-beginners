# مائیکروسافٹ ایجنٹ فریم ورک ورک فلو کے ساتھ ملٹی ایجنٹ ایپلیکیشنز کی تعمیر

یہ ٹیوٹوریل آپ کو مائیکروسافٹ ایجنٹ فریم ورک کے ذریعے ملٹی ایجنٹ ایپلیکیشنز کو سمجھنے اور بنانے میں رہنمائی فراہم کرے گا۔ ہم ملٹی ایجنٹ سسٹمز کے بنیادی تصورات کو دریافت کریں گے، فریم ورک کے ورک فلو کمپونینٹ کی فن تعمیر میں گہرائی میں جائیں گے، اور مختلف ورک فلو پیٹرنز کے لیے Python اور .NET دونوں میں عملی مثالوں کا جائزہ لیں گے۔

## 1\. ملٹی ایجنٹ سسٹمز کو سمجھنا

ایک AI ایجنٹ ایک ایسا نظام ہے جو معمول کے بڑے زبان ماڈل (LLM) کی صلاحیتوں سے آگے بڑھتا ہے۔ یہ اپنے ماحول کو محسوس کرسکتا ہے، فیصلے کرسکتا ہے، اور مخصوص مقاصد حاصل کرنے کے لیے کارروائیاں کرسکتا ہے۔ ایک ملٹی ایجنٹ سسٹم میں کئی ایسے ایجنٹ شامل ہوتے ہیں جو ایک ساتھ مل کر ایک مسئلہ حل کرتے ہیں جو ایک واحد ایجنٹ کے لیے اکیلے سنبھالنا مشکل یا ناممکن ہوتا۔

### عام ایپلیکیشن کے منظرنامے

  * **پیچیدہ مسئلے کا حل**: ایک بڑے کام کو (مثلاً، کمپنی کے وسیع ایونٹ کی منصوبہ بندی) چھوٹے ذیلی کاموں میں تقسیم کرنا جو تخصصی ایجنٹس کے ذریعے انجام دیے جاتے ہیں (مثلاً، بجٹ ایجنٹ، لاجسٹکس ایجنٹ، مارکیٹنگ ایجنٹ)۔
  * **ورچوئل اسسٹنٹس**: ایک بنیادی اسسٹنٹ ایجنٹ جو شیڈولنگ، تحقیق، اور بکنگ جیسے کام دوسرے تخصصی ایجنٹس کو سپرد کرتا ہے۔
  * **خودکار مواد تخلیق**: ایک ورک فلو جہاں ایک ایجنٹ مواد کا مسودہ تیار کرتا ہے، دوسرا درستگی اور انداز کے لیے نظرثانی کرتا ہے، اور تیسرا اسے شائع کرتا ہے۔

### ملٹی ایجنٹ پیٹرنز

ملٹی ایجنٹ سسٹمز کو کئی پیٹرنز میں منظم کیا جا سکتا ہے، جو ان کے تعامل کے طریقے کا تعین کرتے ہیں:

  * **تسلسل وار**: ایجنٹ ایک مقررہ ترتیب میں کام کرتے ہیں، جیسے اسمبلی لائن۔ ایک ایجنٹ کا آؤٹ پٹ اگلے کے ان پٹ میں تبدیل ہو جاتا ہے۔
  * **ہم وقت سازی**: ایجنٹ ایک کام کے مختلف حصوں پر بیک وقت کام کرتے ہیں، اور ان کے نتائج آخر میں مجموعہ کیے جاتے ہیں۔
  * **مشروط**: ورک فلو کسی ایجنٹ کے آؤٹ پٹ کی بنیاد پر مختلف راستے اختیار کرتا ہے، جیسا کہ if-then-else بیان میں ہوتا ہے۔

## 2\. مائیکروسافٹ ایجنٹ فریم ورک ورک فلو فن تعمیر

ایجنٹ فریم ورک کا ورک فلو سسٹم ایک جدید آرکیسٹریشن انجن ہے جو کئی ایجنٹس کے درمیان پیچیدہ تعاملات کو منظم کرنے کے لیے بنایا گیا ہے۔ یہ ایک گراف پر مبنی فن تعمیر پر مشتمل ہے جو [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf) استعمال کرتا ہے، جہاں پراسیسنگ "supersteps" کہلانے والے ہم وقت ساز مراحل میں ہوتی ہے۔

### بنیادی اجزاء

فن تعمیر تین اہم حصوں پر مشتمل ہے:

1.  **ایگزیکیوٹرز**: یہ بنیادی پراسیسنگ یونٹس ہوتے ہیں۔ ہماری مثالوں میں، ایک `Agent` ایک قسم کا ایگزیکیوٹر ہے۔ ہر ایگزیکیوٹر کے پاس کئی پیغام ہینڈلرز ہو سکتے ہیں جو موصول شدہ پیغام کی قسم کی بنیاد پر خودکار طور پر چلائے جاتے ہیں۔
2.  **ایجز**: یہ ایگزیکیوٹرز کے درمیان پیغامات کے راستے کو بیان کرتے ہیں۔ ایجز میں شرائط ہو سکتی ہیں، جو ورک فلو گراف کے ذریعے معلومات کے متحرک راستہ طے کرنے کی اجازت دیتی ہیں۔
3.  **ورک فلو**: یہ کمپونینٹ پورے عمل کو سنبھالتا ہے، ایگزیکیوٹرز، ایجز، اور عمومی اجرایہ کے بہاؤ کو منظم کرتا ہے۔ یہ یقینی بناتا ہے کہ پیغامات درست ترتیب میں پراسیس ہوں اور مشاہدے کے لیے ایونٹس کو اسٹریم کرتا ہے۔

*ورک فلو سسٹم کے بنیادی اجزاء کی وضاحتی خاکہ۔*

یہ ساخت مضبوط اور اسکیل ایبل ایپلیکیشنز بنانے کی اجازت دیتی ہے جیسا کہ بنیادی پیٹرنز جیسے تسلسلی چینز، فین آؤٹ/فین اِن برائے متوازی پراسیسنگ، اور مشروط بہاؤ کے لیے سوئچ کیس لاجک۔

## 3\. عملی مثالیں اور کوڈ تجزیہ

اب، آئیے دیکھتے ہیں کہ فریم ورک کے ذریعے مختلف ورک فلو پیٹرنز کو کیسے نافذ کیا جاتا ہے۔ ہم ہر مثال کے لیے Python اور .NET کوڈ دیکھیں گے۔

### کیس 1: بنیادی تسلسلی ورک فلو

یہ سب سے سادہ پیٹرن ہے، جہاں ایک ایجنٹ کا آؤٹ پٹ براہ راست دوسرے کو منتقل کیا جاتا ہے۔ ہمارے منظرنامے میں ایک ہوٹل کا `FrontDesk` ایجنٹ شامل ہے جو سفر کی تجویز دیتا ہے، جسے `Concierge` ایجنٹ نظرثانی کرتا ہے۔

*بنیادی FrontDesk -> Concierge ورک فلو کا خاکہ۔*

#### منظرنامے کا پس منظر

ایک مسافر پیرس میں تجویز طلب کرتا ہے۔

1.  `FrontDesk` ایجنٹ، جو مختصراً کام کے لیے ڈیزائن کیا گیا ہے، Louvre Museum کا دورہ کرنے کی تجویز دیتا ہے۔
2.  `Concierge` ایجنٹ، جو حقیقی تجربات کو ترجیح دیتا ہے، یہ تجویز وصول کرتا ہے۔ یہ سفارش کا جائزہ لیتا ہے اور تجاویز دیتا ہے، ایک زیادہ مقامی، کم سیاحوں والا متبادل تجویز کرتا ہے۔

#### Python نفاذ کا تجزیہ

Python کی مثال میں، ہم پہلے دونوں ایجنٹس کو متعین اور تخلیق کرتے ہیں، ہر ایک کے مخصوص ہدایات کے ساتھ۔

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# ایجنٹ کے کردار اور ہدایات کی تعریف کریں
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# ایجنٹ کی مثالیں بنائیں
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

بعد میں، `WorkflowBuilder` کو گراف بنانے کے لیے استعمال کیا جاتا ہے۔ `front_desk_agent` کو آغاز کا نقطہ مقرر کیا جاتا ہے، اور اس کے آؤٹ پٹ کو `reviewer_agent` سے جوڑنے کے لیے ایک کنارہ بنایا جاتا ہے۔

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

آخر میں، ورک فلو ابتدائی صارف پرامپٹ کے ساتھ چلایا جاتا ہے۔

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# رن ورک فلو کو چلاتا ہے؛ get_outputs() آؤٹ پٹ ایگزیکیوٹر کے نتیجے کو واپس کرتا ہے۔
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C#) نفاذ کا تجزیہ

.NET نفاذ بہت مشابہہ منطق پر عمل کرتا ہے۔ پہلے ایجنٹس کے نام اور ہدایات کے لیے مستقل متعین کیے جاتے ہیں۔

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

ایجنٹس کو `AzureOpenAIClient` (Responses API) استعمال کر کے تخلیق کیا جاتا ہے، اور پھر `WorkflowBuilder` تسلسلی بہاؤ کو `frontDeskAgent` سے `reviewerAgent` کی طرف ایک کنارہ شامل کر کے متعین کرتا ہے۔

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

پھر ورک فلو صارف کے پیغام کے ساتھ چلایا جاتا ہے، اور نتائج واپس اسٹریم کیے جاتے ہیں۔

### کیس 2: ملٹی اسٹیپ تسلسلی ورک فلو

یہ پیٹرن بنیادی سلسلے کو زیادہ ایجنٹس شامل کر کے بڑھاتا ہے۔ یہ ایسے عمل کے لیے مثالی ہے جنہیں متعدد مراحل کی درستگی یا تبدیلی کی ضرورت ہوتی ہے۔

#### منظرنامے کا پس منظر

ایک صارف ایک لونگ روم کی تصویر دیتا ہے اور فرنیچر کی قیمت کا کوٹیشن طلب کرتا ہے۔

1.  **Sales-Agent**: تصویر میں فرنیچر کی اشیاء کی شناخت کرتا ہے اور فہرست بناتا ہے۔
2.  **Price-Agent**: اشیاء کی فہرست لیتا ہے اور تفصیلی قیمت فراہم کرتا ہے، بشمول بجٹ، درمیانی اور پریمیم آپشنز۔
3.  **Quote-Agent**: قیمت شدہ فہرست وصول کرتا ہے اور اسے مارک ڈاؤن میں رسمی کوٹیشن دستاویز میں ترتیب دیتا ہے۔

*Sales -> Price -> Quote ورک فلو کا خاکہ۔*

#### Python نفاذ کا تجزیہ

تین ایجنٹس متعین کیے گئے ہیں، ہر ایک کا مخصوص کردار ہے۔ ورک فلو `add_edge` استعمال کرتے ہوئے چین بنایا جاتا ہے: `sales_agent` -> `price_agent` -> `quote_agent`۔

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# تین ماہر ایجنٹ بنائیں
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# متواتر ورک فلو تیار کریں
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ان پٹ ایک `ChatMessage` ہے جس میں متن اور تصویر URI دونوں شامل ہیں۔ فریم ورک ہر ایجنٹ کا آؤٹ پٹ اگلے کو پاس کرنے کا انتظام کرتا ہے یہاں تک کہ حتمی کوٹیشن تیار ہو جائے۔

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# صارف کے پیغام میں متن اور تصویر دونوں شامل ہیں
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# ورک فلو چلائیں
events = await workflow.run(message)
```

#### .NET (C#) نفاذ کا تجزیہ

.NET کی مثال Python ورژن کی عکاسی کرتی ہے۔ تین ایجنٹس (`salesagent`, `priceagent`, `quoteagent`) تخلیق کیے جاتے ہیں۔ `WorkflowBuilder` انہیں تسلسل وار جوڑتا ہے۔

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

صارف کا پیغام دونوں امیج ڈیٹا (بائٹس کے طور پر) اور متن پرامپٹ کے ساتھ بنایا جاتا ہے۔ `InProcessExecution.RunStreamingAsync` میتھڈ ورک فلو شروع کرتا ہے، اور حتمی آؤٹ پٹ اسٹریم سے حاصل کیا جاتا ہے۔

### کیس 3: ہم وقت ساز ورک فلو

یہ پیٹرن اس وقت استعمال ہوتا ہے جب کام بیک وقت انجام دیے جا سکتے ہیں تاکہ وقت بچایا جا سکے۔ اس میں کئی ایجنٹس کو "فین آؤٹ" اور نتیجے کو "فین اِن" کیا جاتا ہے۔

#### منظرنامے کا پس منظر

ایک صارف سیئٹل کے لیے سفر کی منصوبہ بندی طلب کرتا ہے۔

1.  **Dispatcher (Fan-Out)**: صارف کی درخواست بیک وقت دو ایجنٹس کو بھیجی جاتی ہے۔
2.  **Researcher-Agent**: سیئٹل میں دسمبر کے مہینے کے لیے سیاحتی مقامات، موسم، اور اہم عوامل پر تحقیق کرتا ہے۔
3.  **Plan-Agent**: آزادانہ طور پر روزانہ کے حساب سے تفصیلی سفری منصوبہ تیار کرتا ہے۔
4.  **Aggregator (Fan-In)**: محقق اور منصوبہ ساز دونوں کے نتائج جمع کر کے حتمی نتیجہ پیش کرتا ہے۔

*ہم وقت ساز Researcher اور Planner ورک فلو کا خاکہ۔*

#### Python نفاذ کا تجزیہ

`ConcurrentBuilder` اس پیٹرن کی تخلیق کو آسان بناتا ہے۔ آپ بس شامل ایجنٹس کی فہرست دیتے ہیں، اور بلڈر خود بخود ضروری فین آؤٹ اور فین اِن لاجک بناتا ہے۔

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder فین آؤٹ/فین ان لاجک کو سنبھالتا ہے
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# ورک فلو چلائیں
events = await workflow.run("Plan a trip to Seattle in December")
```

فریم ورک یقینی بناتا ہے کہ `research_agent` اور `plan_agent` متوازی طور پر چلیں، اور ان کے حتمی نتائج فہرست میں جمع کیے جائیں۔

#### .NET (C#) نفاذ کا تجزیہ

.NET میں، اس پیٹرن کے لیے زیادہ واضح تعریف کی ضرورت ہوتی ہے۔ کسٹم ایگزیکیوٹرز (`ConcurrentStartExecutor` اور `ConcurrentAggregationExecutor`) کو فین آؤٹ اور فین اِن لاجک کے لیے تخلیق کیا جاتا ہے۔

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

اس کے بعد `WorkflowBuilder` ان کسٹم ایگزیکیوٹرز اور ایجنٹس کے ساتھ گراف بنانے کے لیے `AddFanOutEdge` اور `AddFanInEdge` استعمال کرتا ہے۔

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### کیس 4: مشروط ورک فلو

مشروط ورک فلو شاخ دار منطق متعارف کراتے ہیں، جس سے نظام درمیانی نتائج کی بنیاد پر مختلف راستے اختیار کر سکتا ہے۔

#### منظرنامے کا پس منظر

یہ ورک فلو ایک تکنیکی ٹیوٹوریل کی تخلیق اور اشاعت کو خودکار بناتا ہے۔

1.  **Evangelist-Agent**: دی گئی خاکہ اور URLs کی بنیاد پر ٹیوٹوریل کا مسودہ لکھتا ہے۔
2.  **ContentReviewer-Agent**: مسودہ کا جائزہ لیتا ہے۔ چیک کرتا ہے کہ لفظوں کی تعداد 200 سے زیادہ ہو۔
3.  **Conditional Branch**:
      * **اگر منظور ہو (`Yes`)**: ورک فلو `Publisher-Agent` کی طرف بڑھتا ہے۔
      * **اگر مسترد ہو (`No`)**: ورک فلو رک جاتا ہے اور مستردگی کی وجہ بتاتا ہے۔
4.  **Publisher-Agent**: اگر مسودہ منظور ہو، یہ ایجنٹ مواد کو مارک ڈاؤن فائل میں محفوظ کرتا ہے۔

#### Python نفاذ کا تجزیہ

اس مثال میں `select_targets` نامی کسٹم فنکشن استعمال ہوتا ہے جو مشروط منطق کو نافذ کرتا ہے۔ یہ فنکشن `add_multi_selection_edge_group` کو دیا جاتا ہے اور `review_result` فیلڈ کی بنیاد پر ورک فلو کو ہدایت دیتا ہے۔

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# یہ فنکشن جائزہ کے نتیجے کی بنیاد پر اگلا قدم طے کرتا ہے
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # اگر منظور ہو جائے تو 'save_draft' ایگزیکیوٹر کی طرف بڑھیں
        return [save_draft_id]
    else:
        # اگر مسترد ہو جائے تو ناکامی کی رپورٹنگ کے لیے 'handle_review' ایگزیکیوٹر کی طرف بڑھیں
        return [handle_review_id]

# ورک فلو بلڈر راؤٹنگ کے لیے سیلیکشن فنکشن استعمال کرتا ہے
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # ملٹی سیلیکشن ایج مشروط منطق کو نافذ کرتا ہے
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

کسٹم ایگزیکیوٹرز جیسے `to_reviewer_result` ایجنٹس کے JSON آؤٹ پٹ کو پارس کرتے ہیں اور اسے مضبوط قسم کے آبجیکٹس میں تبدیل کرتے ہیں تاکہ انتخابی فنکشن جانچ سکے۔

#### .NET (C#) نفاذ کا تجزیہ

.NET ورژن اسی طرح کے نقطہ نظر کا استعمال کرتا ہے ایک کنڈیشن فنکشن کے ساتھ۔ `Func<object?, bool>` تعریف کی جاتی ہے تاکہ `ReviewResult` آبجیکٹ کی `Result` پراپرٹی کی جانچ کی جا سکے۔

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

`AddEdge` میتھڈ کے `condition` پیرامیٹر سے `WorkflowBuilder` کو شاخ دار راستہ بنانے کی اجازت ملتی ہے۔ ورک فلو صرف اس کنارہ کی پیروی کرے گا جو `publishExecutor` کی طرف ہے اگر شرط `GetCondition(expectedResult: "Yes")` درست ہو۔ ورنہ یہ `sendReviewerExecutor` کی طرف جائے گا۔

## اختتامیہ

مائیکروسافٹ ایجنٹ فریم ورک ورک فلو پیچیدہ، ملٹی ایجنٹ سسٹمز کے آرکیسٹریشن کے لیے ایک مضبوط اور لچکدار بنیاد فراہم کرتا ہے۔ اس کے گراف پر مبنی فن تعمیر اور بنیادی اجزاء کا فائدہ اٹھاتے ہوئے، ڈیولپرز Python اور .NET دونوں میں پیچیدہ ورک فلو ڈیزائن اور نفاذ کر سکتے ہیں۔ چاہے آپ کی ایپلیکیشن کو سادہ تسلسلی پراسیسنگ، متوازی اجرا، یا متحرک مشروط منطق کی ضرورت ہو، فریم ورک AI پر مبنی طاقتور، اسکیل ایبل، اور ٹائپ-سیف حل تیار کرنے کے آلات فراہم کرتا ہے۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->