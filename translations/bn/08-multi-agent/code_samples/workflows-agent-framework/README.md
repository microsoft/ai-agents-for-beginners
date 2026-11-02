# Microsoft Agent Framework Workflow দিয়ে মাল্টি-এজেন্ট অ্যাপ্লিকেশন তৈরি

এই টিউটোরিয়ালটি আপনাকে Microsoft Agent Framework ব্যবহার করে মাল্টি-এজেন্ট অ্যাপ্লিকেশন বুঝতে এবং তৈরি করতে সাহায্য করবে। আমরা মাল্টি-এজেন্ট সিস্টেমের মূল ধারণাগুলি অন্বেষণ করব, ফ্রেমওয়ার্কের Workflow উপাদানের স্থাপত্যে ডুব দেব, এবং বিভিন্ন ওয়ার্কফ্লো প্যাটার্নের জন্য Python এবং .NET-এ ব্যবহারিক উদাহরণগুলি পর্যায়ক্রমে দেখব।

## 1\. মাল্টি-এজেন্ট সিস্টেম বোঝা

একটি AI এজেন্ট হলো এমন একটি সিস্টেম যা একটি সাধারণ লার্জ ল্যাংগুয়েজ মডেল (LLM)-এর ক্ষমতার বাইরে যায়। এটি তার পরিবেশকে অনুধাবন করতে পারে, সিদ্ধান্ত নিতে পারে এবং নির্দিষ্ট লক্ষ্য অর্জনে কার্যক্রম নিতে পারে। একটি মাল্টি-এজেন্ট সিস্টেমে কয়েকটি এজেন্ট একসাথে কাজ করে এমন একটি সমস্যা সমাধান করে যা একক এজেন্টের পক্ষে একা হারানো বা অসম্ভব হতে পারে।

### সাধারণ অ্যাপ্লিকেশন পরিস্থিতি

  * **জটিল সমস্যা সমাধান**: একটি বড় কাজকে (যেমন, একটি কোম্পানি-ব্যাপী ইভেন্ট পরিকল্পনা) ছোট ছোট উপ-কার্যগুলিতে ভাঙ্গা যা বিশেষায়িত এজেন্টরা পরিচালনা করে (যেমন, বাজেট এজেন্ট, লজিস্টিক্স এজেন্ট, মার্কেটিং এজেন্ট)।
  * **ভার্চুয়াল সহকারী**: একটি প্রধান সহকারী এজেন্ট বিভিন্ন কাজ যেমন সময়সূচি নির্ধারণ, গবেষণা এবং বুকিং অন্য বিশেষায়িত এজেন্টদের কাছে বরাদ্দ করে।
  * **স্বয়ংক্রিয় বিষয়বস্তু তৈরি**: একটি ওয়ার্কফ্লো যেখানে একটি এজেন্ট কনটেন্ট খসড়া করে, অন্যটি যথার্থতা এবং টোন যাচাই করে, এবং তৃতীয়টি এটি প্রকাশ করে।

### মাল্টি-এজেন্ট প্যাটার্ন

মাল্টি-এজেন্ট সিস্টেমগুলি বিভিন্ন প্যাটার্নে সংগঠিত হতে পারে, যা নির্ধারণ করে তারা কিভাবে ইন্টারঅ্যাক্ট করে:

  * **ক্রমাগত**: এজেন্টরা একটি পূর্বনির্ধারিত ক্রমে কাজ করে, যেমন একটি অ্যাসেম্বলি লাইন। একটি এজেন্টের আউটপুট পরবর্তী এজেন্টের ইনপুট হয়।
  * **সমলয়ীন (Concurrent)**: এজেন্টরা একটি কাজের বিভিন্ন অংশে সমান্তরালে কাজ করে এবং তাদের ফলাফল একত্রিত করা হয় শেষ পর্যন্ত।
  * **শর্তাধীন**: ওয়ার্কফ্লো একটি এজেন্টের আউটপুটের ভিত্তিতে বিভিন্ন পথ অনুসরণ করে, যেমন if-then-else বিবৃতির মতো।

## 2\. Microsoft Agent Framework Workflow স্থাপত্য

Agent Framework-এর ওয়ার্কফ্লো সিস্টেম হল একটি উন্নত অর্কেস্ট্রেশন ইঞ্জিন যা একাধিক এজেন্টের জটিল ইন্টারঅ্যাকশন পরিচালনা করার জন্য ডিজাইন করা হয়েছে। এটি একটি গ্রাফ-ভিত্তিক স্থাপত্যের উপরে নির্মিত যা [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf) ব্যবহার করে, যেখানে প্রসেসিং "সুপারস্টেপ" নামে সমন্বিত ধাপে ঘটে।

### মূল উপাদানসমূহ

স্থাপত্যটি তিনটি প্রধান অংশ নিয়ে গঠিত:

1.  **Executors**: এগুলো মৌলিক প্রসেসিং ইউনিট। আমাদের উদাহরণগুলোতে, `Agent` হলো executor-এর একটি ধরনের। প্রতিটি executor-এর একাধিক মেসেজ হ্যান্ডলার থাকতে পারে যা মেসেজের প্রকারের উপর ভিত্তি করে স্বয়ংক্রিয়ভাবে আহ্বান করা হয়।
2.  **Edges**: এগুলো executor-গুলির মধ্যে মেসেজ যাওয়ার পথ নির্ধারণ করে। Edges-এ শর্ত থাকতে পারে, যা workflow গ্রাফের মাধ্যমে তথ্যের গতিপথ গতিশীলভাবে রুটিং করার সুযোগ দেয়।
3.  **Workflow**: এই উপাদানটি পুরো প্রক্রিয়াটিকে অর্কেস্ট্রেট করে, executors, edges এবং কার্য সম্পাদনের সামগ্রিক প্রবাহ পরিচালনা করে। এটি নিশ্চিত করে যে মেসেজ সঠিক ক্রমে প্রক্রিয়াকৃত হচ্ছে এবং পর্যবেক্ষণের জন্য ইভেন্ট স্ট্রিম করে।

*ওয়ার্কফ্লো সিস্টেমের মূল উপাদানগুলির একটি চিত্র।*

এই কাঠামোটি মৌলিক প্যাটার্ন যেমন ক্রমাগত চেইন, সমান্তরাল প্রক্রিয়াকরণের জন্য fan-out/fan-in, এবং শর্তাধীন প্রবাহের জন্য switch-case লজিক ব্যবহার করে দৃঢ় এবং স্কেলেবল অ্যাপ্লিকেশন তৈরি করতে দেয়।

## 3\. ব্যবহারিক উদাহরণ ও কোড বিশ্লেষণ

এখন, ফ্রেমওয়ার্ক ব্যবহার করে বিভিন্ন ওয়ার্কফ্লো প্যাটার্ন কিভাবে বাস্তবায়ন করবেন তা দেখি। প্রতিটি উদাহরণের জন্য আমরা Python এবং .NET কোড উভয়ই দেখব।

### কেস 1: মূল Sequential Workflow

এটি সবচেয়ে সহজ প্যাটার্ন, যেখানে একটি এজেন্টের আউটপুট সরাসরি অন্যটির কাছে পাঠানো হয়। আমাদের পরিস্থিতিতে একটি হোটেলের `FrontDesk` এজেন্ট যেটি ভ্রমণ সুপারিশ করে, যেটি পরের `Concierge` এজেন্ট দ্বারা পর্যালোচিত হয়।

*মূল FrontDesk -> Concierge ওয়ার্কফ্লো-এর চিত্র।*

#### পরিস্থিতির পটভূমি

একজন ভ্রমণকারী প্যারিসে একটি সুপারিশ চাইছেন।

1.  `FrontDesk` এজেন্ট, সংক্ষিপ্ততার জন্য ডিজাইন করা, Louvre Museum পরিদর্শনের পরামর্শ দেয়।
2.  `Concierge` এজেন্ট, যিনি প্রাধান্য দেন বাস্তব অভিজ্ঞতাকে, এই পরামর্শ গ্রহণ করেন, পর্যালোচনা করেন এবং আরও স্থানীয়, কম পর্যটকসদৃশ বিকল্প প্রস্তাব দেন।

#### Python বাস্তবায়ন বিশ্লেষণ

Python উদাহরণে, আমরা প্রথমে দুইটি এজেন্ট নির্ধারণ এবং তৈরি করি, প্রত্যেকের বিশেষ নির্দেশনা সহ।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# এজেন্টের ভূমিকা এবং নির্দেশাবলী নির্ধারণ করুন
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# এজেন্টের ইনস্টেন্স তৈরি করুন
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

এরপর, `WorkflowBuilder` দিয়ে গ্রাফ তৈরি করা হয়। `front_desk_agent` শুরু পয়েন্ট হিসেবে নির্ধারণ করা হয় এবং একটি edge তৈরি করে এর আউটপুট `reviewer_agent`-এর সাথে সংযুক্ত করা হয়।

```python
# ০১.পাইথন-এজেন্ট-ফ্রেমওয়ার্ক-ওয়ার্কফ্লো-ঘিমডেল-বেসিক.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

অবশেষে, ওয়ার্কফ্লোটি প্রাথমিক ব্যবহারকারী প্রম্পট নিয়ে চালানো হয়।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run ওয়ার্কফ্লো চালায়; get_outputs() আউটপুট নির্বাহকের ফলাফল ফেরত দেয়।
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) বাস্তবায়ন বিশ্লেষণ

.NET বাস্তবায়ন খুবই অনুরূপ যুক্তি অনুসরণ করে। প্রথমে এজেন্ট নাম এবং নির্দেশনার জন্য কনস্ট্যান্ট নির্ধারণ করা হয়।

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

এজেন্টগুলো `AzureOpenAIClient` (Responses API) ব্যবহার করে তৈরি করা হয়, এবং `WorkflowBuilder` ক্রমাগত প্রবাহ সংজ্ঞায়িত করে `frontDeskAgent` থেকে `reviewerAgent`-এ একটি edge যোগ করে।

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

ব্যবহারকারীর মেসেজ দিয়ে ওয়ার্কফ্লো চালানো হয় এবং ফলাফলগুলো স্ট্রিম করে ফেরত দেওয়া হয়।

### কেস 2: মাল্টি-স্টেপ Sequential Workflow

এই প্যাটার্নটি মৌলিক ক্রমকে বাড়িয়ে আরও বেশি এজেন্ট অন্তর্ভুক্ত করে। এটি আদর্শ এমন প্রক্রিয়াগুলির জন্য যেগুলিতে বহু ধাপের পরিমার্জন বা রুপান্তর প্রয়োজন।

#### পরিস্থিতির পটভূমি

একজন ব্যবহারকারী একটি লিভিং রুমের ছবি দেয় এবং আসবাবপত্রের এক মূল্যছাড় চান।

1.  **Sales-Agent**: ছবির আসবাবপত্র শনাক্ত করে এবং একটি তালিকা তৈরি করে।
2.  **Price-Agent**: তালিকাভুক্ত আইটেমগুলোর বিস্তারিত মূল্য বিবরণ প্রদান করে — বাজেট, মধ্যম, এবং প্রিমিয়াম বিকল্প সহ।
3.  **Quote-Agent**: মূল্য নির্ধারিত তালিকা গ্রহণ করে এবং Markdown ফরম্যাটে একটি আনুষ্ঠানিক কোটেশন ডকুমেন্ট তৈরি করে।

*Sales -> Price -> Quote ওয়ার্কফ্লো-এর চিত্র।*

#### Python বাস্তবায়ন বিশ্লেষণ

তিনটি এজেন্ট নির্ধারণ করা হয়, প্রত্যেকের বিশেষায়িত ভূমিকা রয়েছে। `add_edge` ব্যবহার করে একটি চেইন তৈরি করা হয়: `sales_agent` -> `price_agent` -> `quote_agent`।

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# তিনটি বিশেষায়িত এজেন্ট তৈরি করুন
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# ধাপে ধাপে কর্মপ্রবাহ তৈরি করুন
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ইনপুট একটি `ChatMessage` যা পাঠ্য এবং ইমেজ URI উভয়ই অন্তর্ভুক্ত করে। ফ্রেমওয়ার্ক প্রতিটি এজেন্টের আউটপুট পরবর্তী এজেন্টের কাছে সরবরাহ করার কাজ পরিচালনা করে যতক্ষণ পর্যন্ত চূড়ান্ত কোটেশন তৈরি হয়।

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# ব্যবহারকারীর মেসেজে পাঠ্য এবং একটি চিত্র উভয়ই রয়েছে
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# ওয়ার্কফ্লো চালান
events = await workflow.run(message)
```

#### .NET (C\#) বাস্তবায়ন বিশ্লেষণ

.NET উদাহরণটি Python সংস্করণের প্রতিফলন। তিনটি এজেন্ট (`salesagent`, `priceagent`, `quoteagent`) তৈরি করা হয়। `WorkflowBuilder` তাদের ক্রমাগত সংযুক্ত করে।

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

ব্যবহারকারীর মেসেজটি উভয় ইমেজ তথ্য (বাইট আকারে) এবং টেক্সট প্রম্পটের সাথে তৈরি হয়। `InProcessExecution.RunStreamingAsync` মেথড ওয়ার্কফ্লো আরম্ভ করে এবং চূড়ান্ত আউটপুট স্ট্রীম থেকে ক্যাপচার করে।

### কেস 3: Concurrent Workflow

এই প্যাটার্নটি তখন ব্যবহৃত হয় যখন কাজগুলি একসাথে করা যায় সময় বাঁচাতে। এতে "fan-out" থাকে বহু এজেন্টের কাছে এবং "fan-in" থাকে ফলাফলসমূহ একত্রিত করার জন্য।

#### পরিস্থিতির পটভূমি

একজন ব্যবহারকারী সিয়াটল ভ্রমণের পরিকল্পনা করতে চান।

1.  **Dispatcher (Fan-Out)**: ব্যবহারকারীর অনুরোধ দুটি এজেন্টকে একই সময়ে পাঠানো হয়।
2.  **Researcher-Agent**: সিয়াটল-এর দর্শনীয় স্থান, আবহাওয়া, এবং ডিসেম্বরের জন্য মূল বিষয়সমূহ গবেষণা করে।
3.  **Plan-Agent**: স্বতন্ত্রভাবে একটি বিস্তারিত দিনের প্রতিদিনের ভ্রমণসূচি তৈরি করে।
4.  **Aggregator (Fan-In)**: গবেষক এবং পরিকল্পনাকারীর উভয় আউটপুট সংগ্রহ করে একত্রে চূড়ান্ত ফলাফল হিসেবে উপস্থাপন করা হয়।

*Concurrent Researcher এবং Planner ওয়ার্কফ্লো-এর চিত্র।*

#### Python বাস্তবায়ন বিশ্লেষণ

`ConcurrentBuilder` এই প্যাটার্ন তৈরিকে সহজ করে তোলে। শুধু অংশগ্রহণকারী এজেন্ট গুলো তালিকাভুক্ত করুন, এবং বিল্ডার স্বয়ংক্রিয়ভাবে প্রয়োজনীয় fan-out এবং fan-in লজিক তৈরি করে।

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder ফ্যান-আউট/ফ্যান-ইন লজিক পরিচালনা করে
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# কর্মপ্রবাহ চালান
events = await workflow.run("Plan a trip to Seattle in December")
```

ফ্রেমওয়ার্ক নিশ্চিত করে যে `research_agent` এবং `plan_agent` সমান্তরালে কাজ করে, এবং তাদের চূড়ান্ত আউটপুট একটি তালিকায় সংগৃহীত হয়।

#### .NET (C\#) বাস্তবায়ন বিশ্লেষণ

.NET-এ এই প্যাটার্নের জন্য আরও স্পষ্ট সংজ্ঞা প্রয়োজন। কাস্টম executors (`ConcurrentStartExecutor` এবং `ConcurrentAggregationExecutor`) তৈরি করা হয় fan-out এবং fan-in লজিক পরিচালনার জন্য।

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

এরপর `WorkflowBuilder` এই কাস্টম executors এবং এজেন্টের সাথে গ্রাফ তৈরির জন্য `AddFanOutEdge` এবং `AddFanInEdge` ব্যবহার করে।

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### কেস 4: Conditional Workflow

শর্তাধীন ওয়ার্কফ্লো শাখা লজিক প্রবর্তন করে, যা সিস্টেমের মধ্যবর্তী ফলাফলের উপর ভিত্তি করে বিভিন্ন পথ গ্রহণের অনুমতি দেয়।

#### পরিস্থিতির পটভূমি

এই ওয়ার্কফ্লো একটি প্রযুক্তিগত টিউটোরিয়ালের তৈরি এবং প্রকাশ স্বয়ংক্রিয় করে।

1.  **Evangelist-Agent**: একটি নির্দিষ্ট আউটলাইন এবং URL এর ভিত্তিতে টিউটোরিয়ালের খসড়া লেখে।
2.  **ContentReviewer-Agent**: খসড়াটি পর্যালোচনা করে। চেক করে শব্দ সংখ্যা ২০০ এর বেশি কিনা।
3.  **Conditional Branch**:
      * **যদি অনুমোদিত (`Yes`)**: ওয়ার্কফ্লো `Publisher-Agent` এর দিকে এগিয়ে যায়।
      * **যদি প্রত্যাখ্যাত (`No`)**: ওয়ার্কফ্লো বন্ধ হয়ে যায় এবং প্রত্যাখ্যানের কারণ প্রকাশ করে।
4.  **Publisher-Agent**: খসড়া অনুমোদিত হলে, এই এজেন্ট বিষয়বস্তু Markdown ফাইলে সংরক্ষণ করে।

#### Python বাস্তবায়ন বিশ্লেষণ

এই উদাহরণে একটি কাস্টম ফাংশন `select_targets` ব্যবহার করা হয়েছে শর্তাধীন লজিক বাস্তবায়নের জন্য। এই ফাংশনটি `add_multi_selection_edge_group` এ পাস করা হয় এবং রিভিউअर এর আউটপুটের `review_result` ক্ষেত্রের ভিত্তিতে ওয়ার্কফ্লো পরিচালিত হয়।

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# এই ফাংশন পর্যালোচনা ফলাফলের ভিত্তিতে পরবর্তী ধাপ নির্ধারণ করে
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # অনুমোদিত হলে, 'save_draft' executor এ অগ্রসর হন
        return [save_draft_id]
    else:
        # প্রত্যাখ্যাত হলে, ব্যর্থতার প্রতিবেদন করার জন্য 'handle_review' executor এ অগ্রসর হন
        return [handle_review_id]

# ওয়ার্কফ্লো বিল্ডার রাউটিংয়ের জন্য নির্বাচন ফাংশন ব্যবহার করে
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # মাল্টি-সিলেকশন এজ শর্তাধীন লজিক প্রয়োগ করে
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

`to_reviewer_result` মত কাস্টম executors এজেন্ট থেকে JSON আউটপুট পার্স করে তা শক্তিশালী-টাইপযুক্ত অবজেক্টে রূপান্তর করে যা নির্বাচন ফাংশন পর্যবেক্ষণ করতে পারে।

#### .NET (C\#) বাস্তবায়ন বিশ্লেষণ

.NET সংস্করণেও অনুরূপ পন্থা ব্যবহার করে একটি শর্ত ফাংশন। একটি `Func<object?, bool>` সংজ্ঞায়িত করা হয়েছে `ReviewResult` অবজেক্টের `Result` প্রপার্টি পরীক্ষা করার জন্য।

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

`AddEdge` মেথডের `condition` প্যারামিটার `WorkflowBuilder` কে শাখা পথ তৈরি করতে দেয়। যদি `GetCondition(expectedResult: "Yes")` শর্ত সত্য হয়, ওয়ার্কফ্লো `publishExecutor` তে চলে যাবে। অন্যথায়, এটি `sendReviewerExecutor` এর দিকে যাবে।

## উপসংহার

Microsoft Agent Framework Workflow জটিল, মাল্টি-এজেন্ট সিস্টেম অর্কেস্ট্রেট করার জন্য একটি দৃঢ় এবং নমনীয় ভিত্তি প্রদান করে। এর গ্রাফ-ভিত্তিক স্থাপত্য এবং মূল উপাদানগুলি ব্যবহার করে, বিকাশকারীরা Python এবং .NET উভয় ভাষায় উন্নত ওয়ার্কফ্লো ডিজাইন এবং বাস্তবায়ন করতে পারেন। আপনার অ্যাপ্লিকেশন সহজ ক্রমাগত প্রক্রিয়াকরণ, সমান্তরাল কার্যকরী, অথবা গতিশীল শর্তাধীন লজিক প্রয়োজন হোক, ফ্রেমওয়ার্কটি শক্তিশালী, স্কেলেবল, এবং টাইপ-সুরক্ষিত AI-চালিত সমাধান নির্মাণের জন্য সরঞ্জাম সরবরাহ করে।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->