# Microsoft Agent Framework Workflow ကို အသုံးပြု၍ Multi-Agent Applications တည်ဆောက်ခြင်း

ဒီလမ်းညွှန်စာတမ်းက Microsoft Agent Framework ကို အသုံးပြုပြီး Multi-Agent Applications ကို နားလည်ရန်နှင့် တည်ဆောက်ရန်အတွက် လမ်းညွှန်ပေးပါမည်။ Multi-Agent Systems ရဲ့ အဓိကအကြောင်းအရာများကို လေ့လာပြီး Framework ရဲ့ Workflow component ရဲ့ Architecture ကို ဆန်းစစ်ကြည့်မည်။ Python နှင့် .NET တို့တွင် Workflow Patterns များအတွက် လက်တွေ့နမူနာများကိုလည်း လေ့လာမည်။

## 1\. Multi-Agent Systems ကို နားလည်ခြင်း

AI Agent ဆိုတာ သာမန် Large Language Model (LLM) ရဲ့ စွမ်းရည်ထက် ကျော်လွန်သော စနစ်တစ်ခုဖြစ်သည်။ ၎င်းသည် ပတ်ဝန်းကျင်ကို သိမြင်နိုင်ပြီး ဆုံးဖြတ်ချက်များကို ချမှတ်နိုင်သည်။ ထို့နောက် သတ်မှတ်ထားသော ရည်မှန်းချက်များကို ရောက်ရှိရန် လုပ်ဆောင်နိုင်သည်။ Multi-Agent System ဆိုတာ အများအပြား Agent များ ပေါင်းစည်းပြီး တစ်ဦးတည်းဖြင့် ဖြေရှင်းရန် ခက်ခဲသော ပြဿနာကို ဖြေရှင်းရန် ပူးပေါင်းလုပ်ဆောင်ခြင်းဖြစ်သည်။

### အသုံးချနိုင်သော လျှောက်လွှာအခြေအနေများ

  * **ပြဿနာများကို အဆင့်ဆင့် ဖြေရှင်းခြင်း**: အကြီးမားသော တာဝန်တစ်ခု (ဥပမာ- ကုမ္ပဏီအတွင်း အခမ်းအနားတစ်ခု စီစဉ်ခြင်း) ကို အထူးပြု Agent များ (ဥပမာ- Budget Agent, Logistics Agent, Marketing Agent) မှ အပိုင်းပိုင်းအလိုက် လုပ်ဆောင်ခြင်း။
  * **Virtual Assistants**: အဓိက Assistant Agent တစ်ဦးက Scheduling, Research, Booking စသည်တို့ကို အထူးပြု Agent များထံ ပေးအပ်ခြင်း။
  * **အလိုအလျောက် အကြောင်းအရာ ဖန်တီးခြင်း**: Agent တစ်ဦးက အကြောင်းအရာကို ရေးသားပြီး၊ တစ်ဦးက ၎င်းကို တိကျမှုနှင့် စတိုင်အတွက် ပြန်လည်သုံးသပ်ပြီး၊ တစ်ဦးက ထုတ်ဝေခြင်း။

### Multi-Agent Patterns

Multi-Agent Systems များကို အချို့သော Patterns များအတိုင်း စီမံနိုင်ပြီး ၎င်းတို့၏ အပြန်အလှန် ဆက်သွယ်မှုကို သတ်မှတ်ပေးသည်။

  * **Sequential**: Agents များသည် သတ်မှတ်ထားသော အစီအစဉ်အတိုင်း အဆင့်ဆင့် လုပ်ဆောင်သည်။ Agent တစ်ဦး၏ output သည် နောက်တစ်ဦး၏ input ဖြစ်သည်။
  * **Concurrent**: Agents များသည် တစ်ချိန်တည်းတွင် တာဝန်အပိုင်းအခြားများကို လုပ်ဆောင်ပြီး၊ ၎င်းတို့၏ ရလဒ်များကို နောက်ဆုံးတွင် စုပေါင်းသည်။
  * **Conditional**: Workflow သည် Agent တစ်ဦး၏ output အပေါ် မူတည်၍ အခြားလမ်းကြောင်းများကို လိုက်နာသည်။ ဥပမာ- if-then-else statement ကဲ့သို့။

## 2\. Microsoft Agent Framework Workflow Architecture

Agent Framework ရဲ့ Workflow System သည် Multi-Agent များအကြား အဆင့်မြင့် ဆက်သွယ်မှုများကို စီမံရန် ရည်ရွယ်ထားသော Orchestration Engine တစ်ခုဖြစ်သည်။ ၎င်းသည် [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf) ကို အခြေခံထားသော graph-based architecture တစ်ခုဖြစ်ပြီး၊ "supersteps" ဟုခေါ်သော Synchronization အဆင့်များတွင် လုပ်ဆောင်မှုများကို ပြုလုပ်သည်။

### အဓိက Components

Architecture သည် အဓိကအစိတ်အပိုင်း သုံးခုဖြင့် ဖွဲ့စည်းထားသည်-

1.  **Executors**: ၎င်းတို့သည် အခြေခံ လုပ်ဆောင်မှုယူနစ်များဖြစ်သည်။ ဥပမာ- `Agent` သည် Executor အမျိုးအစားတစ်ခုဖြစ်သည်။ Executor တစ်ခုစီတွင် Message Type အပေါ်မူတည်၍ အလိုအလျောက် ခေါ်ဆောင်သော Message Handlers များ ရှိနိုင်သည်။
2.  **Edges**: Message များသည် Executors အကြား သွားလာသော လမ်းကြောင်းကို သတ်မှတ်ပေးသည်။ Edges တွင် အခြေအနေများပါဝင်နိုင်ပြီး၊ Workflow Graph အတွင်း သတင်းအချက်အလက်များကို Dynamic Routing ပြုလုပ်နိုင်သည်။
3.  **Workflow**: ၎င်းသည် တစ်ခုလုံးကို စီမံခန့်ခွဲပြီး Executors, Edges, Execution Flow တို့ကို စီမံသည်။ Messages များကို သတ်မှတ်ထားသော အစီအစဉ်အတိုင်း လုပ်ဆောင်ရန်နှင့် Observability အတွက် Events များကို Streaming ပြုလုပ်သည်။

*Workflow System ရဲ့ အဓိက Components များကို ဖော်ပြသော အကြမ်းဖျင်းပုံစံ*

ဒီဖွဲ့စည်းပုံက Sequential Chains, Parallel Processing အတွက် Fan-Out/Fan-In, Conditional Flows အတွက် Switch-Case Logic ကဲ့သို့သော အခြေခံ Patterns များကို အသုံးပြု၍ ခိုင်ခံ့ပြီး အတိုင်းအတာကြီးမားသော Applications များကို တည်ဆောက်ရန် ခွင့်ပြုသည်။

## 3\. လက်တွေ့နမူနာများနှင့် Code Analysis

အခု Framework ကို အသုံးပြု၍ Workflow Patterns များကို အကောင်အထည်ဖော်ပုံကို လေ့လာကြမည်။ Python နှင့် .NET တို့တွင် နမူနာများကို ကြည့်ရှုမည်။

### Case 1: အခြေခံ Sequential Workflow

ဒီ Pattern သည် Agent တစ်ဦး၏ output ကို တိုက်ရိုက် နောက်တစ်ဦးထံ ပေးပို့သော အလွယ်ဆုံး Pattern ဖြစ်သည်။ ကျွန်ုပ်တို့၏ Scenario တွင် `FrontDesk` Agent က ခရီးသွားအကြံပေးချက်ကို ပြုလုပ်ပြီး၊ `Concierge` Agent က ၎င်းကို ပြန်လည်သုံးသပ်သည်။

*FrontDesk -\> Concierge Workflow ကို ဖော်ပြသော Diagram*

#### Scenario Background

ခရီးသွားတစ်ဦးက ပဲရစ်တွင် အကြံပေးချက်တစ်ခုကို မေးမြန်းသည်။

1.  `FrontDesk` Agent သည် အတိုချုံးအကြံပေးချက်များကို ရေးဆွဲရန် ရည်ရွယ်ထားပြီး Louvre ပြတိုက်သို့ သွားရန် အကြံပေးသည်။
2.  `Concierge` Agent သည် Authentic Experiences ကို ဦးစားပေးပြီး၊ အကြံပေးချက်ကို ပြန်လည်သုံးသပ်သည်။ ၎င်းသည် ပိုမိုဒေသဆိုင်ရာနှင့် ခရီးသွားများနည်းသော အစားထိုးအကြံပေးချက်ကို ပေးသည်။

#### Python Implementation Analysis

Python နမူနာတွင် အရင်ဆုံး Agent နှစ်ဦးကို သတ်မှတ်ပြီး ဖန်တီးသည်။

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

ထို့နောက် `WorkflowBuilder` ကို အသုံးပြု၍ Graph ကို တည်ဆောက်သည်။ `front_desk_agent` ကို Starting Point အဖြစ် သတ်မှတ်ပြီး၊ ၎င်း၏ output ကို `reviewer_agent` ထံ ချိတ်ဆက်ရန် Edge တစ်ခုကို ဖန်တီးသည်။

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

နောက်ဆုံးတွင် Workflow ကို Initial User Prompt ဖြင့် အကောင်အထည်ဖော်သည်။

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C\#) Implementation Analysis

.NET Implementation သည် အလားတူ Logic ကို လိုက်နာသည်။ အရင်ဆုံး Agent များ၏ နာမည်နှင့် Instruction များအတွက် Constants များကို သတ်မှတ်သည်။

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agents များကို `OpenAIClient` ကို အသုံးပြု၍ ဖန်တီးပြီး၊ `WorkflowBuilder` သည် Sequential Flow ကို သတ်မှတ်ရန် `frontDeskAgent` နှင့် `reviewerAgent` အကြား Edge ကို ထည့်သွင်းသည်။

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

Workflow ကို User Message ဖြင့် စတင်ပြီး၊ ရလဒ်များကို Streaming ပြုလုပ်သည်။

### Case 2: Multi-Step Sequential Workflow

ဒီ Pattern သည် အခြေခံ Sequence ကို တိုးချဲ့ပြီး Agent များပိုမိုပါဝင်သည်။ ၎င်းသည် အဆင့်ဆင့် ပြုပြင်ခြင်း သို့မဟုတ် Transformation လိုအပ်သော လုပ်ငန်းစဉ်များအတွက် အထူးသင့်လျော်သည်။

#### Scenario Background

User တစ်ဦးက Living Room ရဲ့ ပုံတစ်ပုံကို ပေးပြီး Furniture Quote တစ်ခုကို မေးမြန်းသည်။

1.  **Sales-Agent**: ပုံထဲမှ Furniture Items များကို ရှာဖွေပြီး စာရင်းတစ်ခုကို ဖန်တီးသည်။
2.  **Price-Agent**: Items စာရင်းကို ယူပြီး Budget, Mid-Range, Premium Options များပါဝင်သော Price Breakdown ကို ပေးသည်။
3.  **Quote-Agent**: Price List ကို Formal Quote Document (Markdown) အဖြစ် Format ပြုလုပ်သည်။

*Sales -\> Price -\> Quote Workflow ကို ဖော်ပြသော Diagram*

#### Python Implementation Analysis

Agents သုံးဦးကို သတ်မှတ်ပြီး၊ ၎င်းတို့၏ အထူးပြုလုပ်ငန်းများကို ဖော်ပြသည်။ Workflow ကို `add_edge` ကို အသုံးပြု၍ Chain တစ်ခုကို ဖန်တီးသည်- `sales_agent` -\> `price_agent` -\> `quote_agent`။

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Input သည် Text နှင့် Image URI ပါဝင်သော `ChatMessage` ဖြစ်သည်။ Framework သည် Agent တစ်ဦး၏ output ကို နောက်တစ်ဦးထံ ပေးပို့ပြီး နောက်ဆုံး Quote ကို ဖန်တီးသည်။

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

#### .NET (C\#) Implementation Analysis

.NET နမူနာသည် Python Version ကို အလားတူလိုက်နာသည်။ Agents သုံးဦး (`salesagent`, `priceagent`, `quoteagent`) ကို ဖန်တီးသည်။ `WorkflowBuilder` သည် Sequential Flow ကို ချိတ်ဆက်သည်။

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

User Message ကို Image Data (bytes) နှင့် Text Prompt ပါဝင်သော Message အဖြစ် ဖန်တီးသည်။ `InProcessExecution.StreamAsync` Method သည် Workflow ကို စတင်ပြီး၊ နောက်ဆုံး output ကို Stream မှာ ရယူသည်။

### Case 3: Concurrent Workflow

ဒီ Pattern သည် တာဝန်များကို တစ်ချိန်တည်းတွင် လုပ်ဆောင်နိုင်သောအခါ အချိန်ကို ချွေတာရန် အသုံးပြုသည်။ ၎င်းသည် "Fan-Out" ကို Multiple Agents များထံ ပေးပို့ပြီး၊ "Fan-In" ကို Aggregation ပြုလုပ်ရန် အသုံးပြုသည်။

#### Scenario Background

User တစ်ဦးက Seattle ခရီးစဉ်ကို စီစဉ်ရန် မေးမြန်းသည်။

1.  **Dispatcher (Fan-Out)**: User ရဲ့ Request ကို Agents နှစ်ဦးထံ တစ်ချိန်တည်း ပေးပို့သည်။
2.  **Researcher-Agent**: Seattle ရဲ့ Attractions, Weather, December ခရီးစဉ်အတွက် Key Considerations များကို သုတေသနပြုသည်။
3.  **Plan-Agent**: ခရီးစဉ်ရဲ့ Day-by-Day Itinerary ကို တစ်ဦးတည်း လွတ်လပ်စွာ ဖန်တီးသည်။
4.  **Aggregator (Fan-In)**: Researcher နှင့် Planner ရဲ့ output များကို စုပေါင်းပြီး နောက်ဆုံးရလဒ်အဖြစ် တင်ပြသည်။

*Concurrent Researcher နှင့် Planner Workflow ကို ဖော်ပြသော Diagram*

#### Python Implementation Analysis

`ConcurrentBuilder` သည် ဒီ Pattern ကို ဖန်တီးရန် လွယ်ကူစေသည်။ Participating Agents များကို ရေးသားပြီး၊ Builder သည် Fan-Out နှင့် Fan-In Logic ကို အလိုအလျောက် ဖန်တီးသည်။

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework သည် `research_agent` နှင့် `plan_agent` ကို တစ်ချိန်တည်းတွင် လုပ်ဆောင်စေပြီး၊ ၎င်းတို့၏ Final Outputs ကို List အဖြစ် စုပေါင်းသည်။

#### .NET (C\#) Implementation Analysis

.NET တွင် ဒီ Pattern ကို ပိုမိုရှင်းလင်းစွာ သတ်မှတ်ရန် လိုအပ်သည်။ Custom Executors (`ConcurrentStartExecutor` နှင့် `ConcurrentAggregationExecutor`) များကို Fan-Out နှင့် Fan-In Logic ကို စီမံရန် ဖန်တီးသည်။

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

`WorkflowBuilder` သည် `AddFanOutEdge` နှင့် `AddFanInEdge` ကို အသုံးပြု၍ Custom Executors နှင့် Agents များကို Graph အဖြစ် တည်ဆောက်သည်။

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Case 4: Conditional Workflow

Conditional Workflows သည် Branching Logic ကို ထည့်သွင်းပြီး၊ Intermediate Results အပေါ်မူတည်၍ အခြားလမ်းကြောင်းများကို လိုက်နာစေသည်။

#### Scenario Background

ဒီ Workflow သည် Technical Tutorial တစ်ခုကို ဖန်တီးပြီး ထုတ်ဝေခြင်းကို အလိုအလျောက် ပြုလုပ်သည်။

1.  **Evangelist-Agent**: Outline နှင့် URLs ကို အခြေခံ၍ Tutorial Draft ကို ရေးသားသည်။
2.  **ContentReviewer-Agent**: Draft ကို ပြန်လည်သုံးသပ်သည်။ Word Count သည် 200 စကားလုံးထက် ကျော်လွန်ကြောင်း စစ်ဆေးသည်။
3.  **Conditional Branch**:
      * **If Approved (`Yes`)**: Workflow သည် `Publisher-Agent` ထံ ဆက်လက်လုပ်ဆောင်သည်။
      * **If Rejected (`No`)**: Workflow သည် ရုပ်သိမ်းပြီး Reject Reason ကို Output အဖြစ် ပေးသည်။
4.  **Publisher-Agent**: Draft ကို အတည်ပြုလျှင် Content ကို Markdown File အဖြစ် သိမ်းဆည်းသည်။

#### Python Implementation Analysis

ဒီနမူနာတွင် Conditional Logic ကို အကောင်အထည်ဖော်ရန် `select_targets` ဟုခေါ်သော Custom Function ကို အသုံးပြုသည်။ ဒီ Function ကို `add_multi_selection_edge_group` ထဲသို့ ပေးပြီး၊ `review_result` Field အပေါ်မူတည်၍ Workflow ကို ဦးတည်စေသည်။

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

Custom Executors များဖြစ်သော `to_reviewer_result` ကို အသုံးပြု၍ Agents output JSON ကို Strongly-Typed Objects အဖြစ် ပြောင်းလဲသည်။

#### .NET (C\#) Implementation Analysis

.NET Version သည် အလားတူ Approach ကို အသုံးပြုသည်။ Condition Function ကို `Func<object?, bool>` အဖြစ် သတ်မှတ်ပြီး၊ `ReviewResult` Object ရဲ့ `Result` Property ကို စစ်ဆေးသည်။

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

`AddEdge` Method ရဲ့ `condition` Parameter သည် `WorkflowBuilder` ကို Branching Path တစ်ခု ဖန်တီးရန် ခွင့်ပြုသည်။ Workflow သည် `GetCondition(expectedResult: "Yes")` က True ပြုလုပ်လျှင်သာ `publishExecutor` ထံ Edge ကို လိုက်နာသည်။ မဟုတ်လျှင် `sendReviewerExecutor` Path ကို လိုက်နာသည်။

## နိဂုံး

Microsoft Agent Framework Workflow သည် Multi-Agent Systems များကို စီမံရန် ခိုင်ခံ့ပြီး Flexible ဖြစ်သော အခြေခံကို ပေးသည်။ ၎င်း၏ Graph-Based Architecture နှင့် Core Components များကို အသုံးပြု၍ Developer များသည် Python နှင့် .NET တို့တွင် အဆင့်မြင့် Workflow များကို Design နှင့် Implement ပြုလုပ်နိုင်သည်။ သင့် Application သည် Simple Sequential Processing, Parallel Execution, Dynamic Conditional Logic တို့လိုအပ်ပါက Framework သည် အစွမ်းထက်၊ Scalable, Type-Safe AI-Powered Solutions များကို တည်ဆောက်ရန် လိုအပ်သော Tools များကို ပေးသည်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုမှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။