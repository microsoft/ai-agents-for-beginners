# Microsoft Agent Framework Workflow ব্যবহার করে মাল্টি-এজেন্ট অ্যাপ্লিকেশন তৈরি করা

এই টিউটোরিয়ালটি আপনাকে Microsoft Agent Framework ব্যবহার করে মাল্টি-এজেন্ট অ্যাপ্লিকেশন তৈরি এবং বুঝতে সাহায্য করবে। আমরা মাল্টি-এজেন্ট সিস্টেমের মূল ধারণাগুলি অন্বেষণ করব, ফ্রেমওয়ার্কের Workflow কম্পোনেন্টের স্থাপত্য বিশ্লেষণ করব এবং Python এবং .NET-এ বিভিন্ন workflow প্যাটার্নের ব্যবহারিক উদাহরণ দেখব।

## ১। মাল্টি-এজেন্ট সিস্টেম বোঝা

একটি AI Agent হলো একটি সিস্টেম যা একটি সাধারণ Large Language Model (LLM)-এর ক্ষমতার বাইরে কাজ করে। এটি তার পরিবেশ উপলব্ধি করতে পারে, সিদ্ধান্ত নিতে পারে এবং নির্দিষ্ট লক্ষ্য অর্জনের জন্য পদক্ষেপ নিতে পারে। একটি মাল্টি-এজেন্ট সিস্টেমে একাধিক এজেন্ট একসঙ্গে কাজ করে এমন সমস্যার সমাধান করে যা একটি একক এজেন্টের পক্ষে সমাধান করা কঠিন বা অসম্ভব।

### সাধারণ অ্যাপ্লিকেশন দৃশ্যপট

  * **জটিল সমস্যা সমাধান**: একটি বড় কাজকে (যেমন, একটি কোম্পানি-ব্যাপী ইভেন্ট পরিকল্পনা) ছোট ছোট উপ-কার্যে ভাগ করা, যা বিশেষায়িত এজেন্ট দ্বারা পরিচালিত হয় (যেমন, বাজেট এজেন্ট, লজিস্টিক্স এজেন্ট, মার্কেটিং এজেন্ট)।
  * **ভার্চুয়াল অ্যাসিস্ট্যান্ট**: একটি প্রধান অ্যাসিস্ট্যান্ট এজেন্ট অন্যান্য বিশেষায়িত এজেন্টদের কাছে কাজ যেমন সময়সূচি তৈরি, গবেষণা এবং বুকিং অর্পণ করে।
  * **স্বয়ংক্রিয় কন্টেন্ট তৈরি**: একটি workflow যেখানে একটি এজেন্ট কন্টেন্ট ড্রাফট করে, অন্যটি সঠিকতা এবং টোন পর্যালোচনা করে, এবং তৃতীয়টি এটি প্রকাশ করে।

### মাল্টি-এজেন্ট প্যাটার্ন

মাল্টি-এজেন্ট সিস্টেম বিভিন্ন প্যাটার্নে সংগঠিত হতে পারে, যা তাদের পারস্পরিক ক্রিয়ার ধরন নির্ধারণ করে:

  * **Sequential**: এজেন্টরা পূর্বনির্ধারিত ক্রমে কাজ করে, যেমন একটি অ্যাসেম্বলি লাইন। একটি এজেন্টের আউটপুট পরবর্তী এজেন্টের ইনপুট হয়ে যায়।
  * **Concurrent**: এজেন্টরা একটি কাজের বিভিন্ন অংশে সমান্তরালভাবে কাজ করে, এবং তাদের ফলাফল শেষে একত্রিত করা হয়।
  * **Conditional**: workflow বিভিন্ন পথে চলে এজেন্টের আউটপুটের উপর ভিত্তি করে, যেমন একটি if-then-else বিবৃতি।

## ২। Microsoft Agent Framework Workflow স্থাপত্য

Agent Framework-এর workflow সিস্টেম একটি উন্নত অর্কেস্ট্রেশন ইঞ্জিন যা একাধিক এজেন্টের মধ্যে জটিল ইন্টারঅ্যাকশন পরিচালনা করতে ডিজাইন করা হয়েছে। এটি একটি গ্রাফ-ভিত্তিক স্থাপত্যের উপর নির্মিত যা একটি [Pregel-স্টাইল এক্সিকিউশন মডেল](https://kowshik.github.io/JPregel/pregel_paper.pdf) ব্যবহার করে, যেখানে প্রক্রিয়াকরণ "supersteps" নামে পরিচিত সিঙ্ক্রোনাইজড ধাপে ঘটে।

### মূল উপাদান

স্থাপত্যটি তিনটি প্রধান অংশ নিয়ে গঠিত:

1.  **Executors**: এগুলো হলো মৌলিক প্রসেসিং ইউনিট। আমাদের উদাহরণে, একটি `Agent` হলো একটি executor-এর ধরন। প্রতিটি executor-এর একাধিক মেসেজ হ্যান্ডলার থাকতে পারে যা প্রাপ্ত মেসেজের ধরন অনুযায়ী স্বয়ংক্রিয়ভাবে আহ্বান করা হয়।
2.  **Edges**: এগুলো executor-এর মধ্যে মেসেজ যাওয়ার পথ নির্ধারণ করে। Edges-এ শর্ত থাকতে পারে, যা workflow গ্রাফের মাধ্যমে তথ্যের গতিপথকে গতিশীলভাবে রাউট করতে দেয়।
3.  **Workflow**: এই কম্পোনেন্ট পুরো প্রক্রিয়াটি অর্কেস্ট্রেট করে, executors, edges এবং সামগ্রিক execution flow পরিচালনা করে। এটি নিশ্চিত করে যে মেসেজগুলি সঠিক ক্রমে প্রক্রিয়াকৃত হয় এবং পর্যবেক্ষণের জন্য ইভেন্ট স্ট্রিম করে।

*workflow সিস্টেমের মূল উপাদানগুলির একটি চিত্র।*

এই কাঠামোটি sequential চেইন, parallel প্রসেসিংয়ের জন্য fan-out/fan-in এবং conditional flows-এর জন্য switch-case লজিকের মতো মৌলিক প্যাটার্ন ব্যবহার করে শক্তিশালী এবং স্কেলযোগ্য অ্যাপ্লিকেশন তৈরি করতে দেয়।

## ৩। ব্যবহারিক উদাহরণ এবং কোড বিশ্লেষণ

এখন, আমরা framework ব্যবহার করে বিভিন্ন workflow প্যাটার্ন বাস্তবায়নের উদাহরণ দেখব। প্রতিটি উদাহরণের জন্য আমরা Python এবং .NET কোড বিশ্লেষণ করব।

### কেস ১: Basic Sequential Workflow

এটি সবচেয়ে সহজ প্যাটার্ন, যেখানে একটি এজেন্টের আউটপুট সরাসরি অন্য এজেন্টে পাঠানো হয়। আমাদের দৃশ্যপট একটি হোটেল `FrontDesk` এজেন্টকে নিয়ে, যা একটি ভ্রমণ সুপারিশ করে এবং এটি `Concierge` এজেন্ট দ্বারা পর্যালোচনা করা হয়।

*Basic FrontDesk -> Concierge workflow-এর একটি চিত্র।*

#### দৃশ্যপটের পটভূমি

একজন ভ্রমণকারী প্যারিসে একটি সুপারিশ চান।

1.  `FrontDesk` এজেন্ট, যা সংক্ষিপ্ততার জন্য ডিজাইন করা হয়েছে, লুভর মিউজিয়াম পরিদর্শনের সুপারিশ করে।
2.  `Concierge` এজেন্ট, যা প্রামাণিক অভিজ্ঞতাকে অগ্রাধিকার দেয়, এই সুপারিশটি গ্রহণ করে। এটি সুপারিশটি পর্যালোচনা করে এবং একটি আরও স্থানীয়, কম পর্যটকপূর্ণ বিকল্প প্রস্তাব করে।

#### Python বাস্তবায়ন বিশ্লেষণ

Python উদাহরণে, আমরা প্রথমে দুটি এজেন্ট সংজ্ঞায়িত এবং তৈরি করি, প্রতিটি নির্দিষ্ট নির্দেশনা সহ।

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

এরপর, `WorkflowBuilder` ব্যবহার করে গ্রাফ তৈরি করা হয়। `front_desk_agent`-কে প্রারম্ভিক পয়েন্ট হিসেবে সেট করা হয় এবং এর আউটপুট `reviewer_agent`-এর সাথে সংযোগ করতে একটি edge তৈরি করা হয়।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

অবশেষে, workflow ব্যবহারকারীর প্রাথমিক প্রম্পট দিয়ে কার্যকর করা হয়।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) বাস্তবায়ন বিশ্লেষণ

.NET বাস্তবায়ন খুবই অনুরূপ যুক্তি অনুসরণ করে। প্রথমে, এজেন্টের নাম এবং নির্দেশনার জন্য constants সংজ্ঞায়িত করা হয়।

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

`OpenAIClient` ব্যবহার করে এজেন্ট তৈরি করা হয়, এবং তারপর `WorkflowBuilder` sequential flow সংজ্ঞায়িত করে `frontDeskAgent` থেকে `reviewerAgent`-এ একটি edge যোগ করে।

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

workflow ব্যবহারকারীর বার্তা দিয়ে চালানো হয়, এবং ফলাফল স্ট্রিম করা হয়।

### কেস ২: Multi-Step Sequential Workflow

এই প্যাটার্নটি মৌলিক ক্রমকে প্রসারিত করে আরও এজেন্ট অন্তর্ভুক্ত করে। এটি এমন প্রক্রিয়ার জন্য আদর্শ যা একাধিক পর্যায়ে refinement বা transformation প্রয়োজন।

#### দৃশ্যপটের পটভূমি

একজন ব্যবহারকারী একটি লিভিং রুমের ছবি প্রদান করেন এবং একটি আসবাবপত্র কোট চান।

1.  **Sales-Agent**: ছবিতে থাকা আসবাবপত্র আইটেমগুলি সনাক্ত করে এবং একটি তালিকা তৈরি করে।
2.  **Price-Agent**: আইটেমগুলির তালিকা নিয়ে বাজেট, মধ্যম-শ্রেণী এবং প্রিমিয়াম বিকল্প সহ বিস্তারিত মূল্য বিশ্লেষণ প্রদান করে।
3.  **Quote-Agent**: মূল্যযুক্ত তালিকা গ্রহণ করে এবং Markdown-এ একটি আনুষ্ঠানিক কোট ডকুমেন্টে রূপান্তর করে।

*Sales -> Price -> Quote workflow-এর একটি চিত্র।*

#### Python বাস্তবায়ন বিশ্লেষণ

তিনটি এজেন্ট সংজ্ঞায়িত করা হয়, প্রতিটি একটি বিশেষ ভূমিকা সহ। workflow তৈরি করা হয় `add_edge` ব্যবহার করে একটি চেইন তৈরি করতে: `sales_agent` -> `price_agent` -> `quote_agent`।

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ইনপুটটি একটি `ChatMessage` যা টেক্সট এবং ছবির URI অন্তর্ভুক্ত করে। framework প্রতিটি এজেন্টের আউটপুট পরবর্তী এজেন্টে পাঠানোর প্রক্রিয়া পরিচালনা করে যতক্ষণ না চূড়ান্ত কোট তৈরি হয়।

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

#### .NET (C#) বাস্তবায়ন বিশ্লেষণ

.NET উদাহরণটি Python সংস্করণকে প্রতিফলিত করে। তিনটি এজেন্ট (`salesagent`, `priceagent`, `quoteagent`) তৈরি করা হয়। `WorkflowBuilder` তাদের sequentially সংযুক্ত করে।

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

ব্যবহারকারীর বার্তা ছবির ডেটা (bytes হিসেবে) এবং টেক্সট প্রম্পট সহ তৈরি করা হয়। `InProcessExecution.StreamAsync` পদ্ধতি workflow শুরু করে, এবং চূড়ান্ত আউটপুট স্ট্রিম থেকে সংগ্রহ করা হয়।

### কেস ৩: Concurrent Workflow

এই প্যাটার্নটি ব্যবহার করা হয় যখন কাজগুলি একসঙ্গে সম্পন্ন করা যায় সময় বাঁচানোর জন্য। এটি "fan-out" করে একাধিক এজেন্টে এবং "fan-in" করে ফলাফল একত্রিত করে।

#### দৃশ্যপটের পটভূমি

একজন ব্যবহারকারী সিয়াটলে একটি ভ্রমণ পরিকল্পনা করতে চান।

1.  **Dispatcher (Fan-Out)**: ব্যবহারকারীর অনুরোধ একসঙ্গে দুটি এজেন্টে পাঠানো হয়।
2.  **Researcher-Agent**: সিয়াটলে ডিসেম্বর মাসে আকর্ষণ, আবহাওয়া এবং গুরুত্বপূর্ণ বিবেচনা নিয়ে গবেষণা করে।
3.  **Plan-Agent**: স্বাধীনভাবে একটি বিস্তারিত দিন-প্রতি-দিন ভ্রমণ পরিকল্পনা তৈরি করে।
4.  **Aggregator (Fan-In)**: গবেষক এবং পরিকল্পনাকারীর আউটপুট সংগ্রহ করে এবং একসঙ্গে চূড়ান্ত ফলাফল হিসেবে উপস্থাপন করে।

*Concurrent Researcher এবং Planner workflow-এর একটি চিত্র।*

#### Python বাস্তবায়ন বিশ্লেষণ

`ConcurrentBuilder` এই প্যাটার্ন তৈরি করা সহজ করে তোলে। আপনি শুধু অংশগ্রহণকারী এজেন্টদের তালিকা দেন, এবং builder স্বয়ংক্রিয়ভাবে প্রয়োজনীয় fan-out এবং fan-in লজিক তৈরি করে।

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

framework নিশ্চিত করে যে `research_agent` এবং `plan_agent` সমান্তরালভাবে কার্যকর হয়, এবং তাদের চূড়ান্ত আউটপুট একটি তালিকায় সংগ্রহ করা হয়।

#### .NET (C#) বাস্তবায়ন বিশ্লেষণ

.NET-এ এই প্যাটার্নটি আরও স্পষ্ট সংজ্ঞা প্রয়োজন। কাস্টম executors (`ConcurrentStartExecutor` এবং `ConcurrentAggregationExecutor`) fan-out এবং fan-in লজিক পরিচালনা করতে তৈরি করা হয়।

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

`WorkflowBuilder` তারপর `AddFanOutEdge` এবং `AddFanInEdge` ব্যবহার করে গ্রাফ তৈরি করে এই কাস্টম executors এবং এজেন্টদের সাথে।

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### কেস ৪: Conditional Workflow

Conditional workflow-এ branching logic অন্তর্ভুক্ত থাকে, যা সিস্টেমকে মধ্যবর্তী ফলাফলের উপর ভিত্তি করে বিভিন্ন পথে যেতে দেয়।

#### দৃশ্যপটের পটভূমি

এই workflow একটি টেকনিক্যাল টিউটোরিয়াল তৈরি এবং প্রকাশের প্রক্রিয়া স্বয়ংক্রিয় করে।

1.  **Evangelist-Agent**: প্রদত্ত outline এবং URLs-এর উপর ভিত্তি করে টিউটোরিয়ালের একটি ড্রাফট লেখে।
2.  **ContentReviewer-Agent**: ড্রাফট পর্যালোচনা করে। এটি চেক করে যে শব্দ সংখ্যা ২০০-এর বেশি কিনা।
3.  **Conditional Branch**:
      * **If Approved (`Yes`)**: workflow `Publisher-Agent`-এ এগিয়ে যায়।
      * **If Rejected (`No`)**: workflow থেমে যায় এবং প্রত্যাখ্যানের কারণ আউটপুট করে।
4.  **Publisher-Agent**: যদি ড্রাফট অনুমোদিত হয়, এই এজেন্ট কন্টেন্টটি Markdown ফাইলে সংরক্ষণ করে।

#### Python বাস্তবায়ন বিশ্লেষণ

এই উদাহরণে একটি কাস্টম ফাংশন, `select_targets`, conditional logic বাস্তবায়নের জন্য ব্যবহার করা হয়। এই ফাংশনটি `add_multi_selection_edge_group`-এ পাস করা হয় এবং `review_result` ফিল্ডের উপর ভিত্তি করে workflow পরিচালনা করে।

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

কাস্টম executors যেমন `to_reviewer_result` এজেন্টদের JSON আউটপুট পার্স করতে এবং এটি শক্তভাবে টাইপ করা অবজেক্টে রূপান্তর করতে ব্যবহার করা হয় যা selection ফাংশন পরিদর্শন করতে পারে।

#### .NET (C#) বাস্তবায়ন বিশ্লেষণ

.NET সংস্করণে একটি condition ফাংশন ব্যবহার করে একই পদ্ধতি অনুসরণ করা হয়। একটি `Func<object?, bool>` সংজ্ঞায়িত করা হয় `ReviewResult` অবজেক্টের `Result` প্রপার্টি চেক করতে।

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

`AddEdge` পদ্ধতির `condition` প্যারামিটার `WorkflowBuilder`-কে একটি branching path তৈরি করতে দেয়। workflow শুধুমাত্র `publishExecutor`-এ edge অনুসরণ করবে যদি condition `GetCondition(expectedResult: "Yes")` true ফেরত দেয়। অন্যথায়, এটি `sendReviewerExecutor`-এর পথে চলে।

## উপসংহার

Microsoft Agent Framework Workflow মাল্টি-এজেন্ট সিস্টেম অর্কেস্ট্রেট করার জন্য একটি শক্তিশালী এবং নমনীয় ভিত্তি প্রদান করে। এর গ্রাফ-ভিত্তিক স্থাপত্য এবং মূল উপাদানগুলিকে কাজে লাগিয়ে, ডেভেলপাররা Python এবং .NET-এ উন্নত workflow ডিজাইন এবং বাস্তবায়ন করতে পারে। আপনার অ্যাপ্লিকেশন যদি সহজ sequential প্রসেসিং, parallel execution বা dynamic conditional logic প্রয়োজন করে, framework শক্তিশালী, স্কেলযোগ্য এবং টাইপ-সেফ AI-চালিত সমাধান তৈরি করার জন্য প্রয়োজনীয় সরঞ্জাম সরবরাহ করে।

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।