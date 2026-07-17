# Di Build Multi-Agent Applications Wit Microsoft Agent Framework Workflow

Dis tutorial go guide you how you go fit understand and build multi-agent applications using Microsoft Agent Framework. We go explore di main concepts of multi-agent systems, check di architecture of di framework Workflow component, and go through practical example for both Python and .NET wey dey different workflow patterns.

## 1\. Understanding Multi-Agent Systems

AI Agent na system wey pass di power of normal Large Language Model (LLM). E fit see im environment, take decision, and do action to reach specific goals. Multi-agent system mean say many of these agents dey work together to solve problem wey one agent alone no go fit handle.

### Common Application Scenarios

  * **Complex Problem Solving**: Divide big work (e.g., plan company-wide event) into small small task wey specialized agents like budget agent, logistics agent, marketing agent go handle.
  * **Virtual Assistants**: Main assistant agent go distribute work like scheduling, research, and booking to other specialized agents.
  * **Automated Content Creation**: Workflow weh one agent go draft content, another one dey review am for accuracy and tone, and third one go publish am.

### Multi-Agent Patterns

Multi-agent systems fit organize inside different patterns wey tell how dem dey interact:

  * **Sequential**: Agents dey work one after another like for assembly line. Output from one agent na input for next.
  * **Concurrent**: Agents dey work for parallel on different parts of task, and dem collect their results at end.
  * **Conditional**: Workflow follow different path based on output of agent, like if-then-else statement.

## 2\. Di Microsoft Agent Framework Workflow Architecture

Agent Framework workflow system na advanced coordination engine wey designed to manage complex interaction between many agents. E built on graph-based architecture wey use [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), weh processing dey happen for synchronized steps wey dem call "supersteps."

### Core Components

Di architecture get three main parts:

1.  **Executors**: Dem be di main processing units. For our example, `Agent` na one type executor. Each executor fit get many message handlers wey dem go call automatically based on di type of message wey dem receive.
2.  **Edges**: Dem dey show di path wey messages go waka between executors. Edges fit get conditions, wey allow dynamic routing of messages for the workflow graph.
3.  **Workflow**: Dis component na di control wey dey manage di whole process, e dey manage executors, edges, and di general flow of execution. E dey make sure say message dey process in correct order and e dey stream events to allow observation.

*Diagram wey dey show di main components of di workflow system.*

Dis structure allow build strong and scalable applications using basic patterns like sequential chains, fan-out/fan-in for parallel work, and switch-case logic for conditional flows.

## 3\. Practical Examples and Code Analysis

Now, make we look how to implement different workflow patterns using di framework. We go check both Python and .NET code for every example.

### Case 1: Basic Sequential Workflow

Dis na di simplest pattern wey one agent output go pass directly to another. Our scenario get hotel `FrontDesk` agent wey fit make travel recommendation, and di `Concierge` agent go review am.

*Diagram of di basic FrontDesk -\> Concierge workflow.*

#### Scenario Background

Traveler ask for recommendation for Paris.

1.  `FrontDesk` agent, wey get brief instruction, recommend make e visit Louvre Museum.
2.  `Concierge` agent, wey dey prioritize authentic experience, go receive di suggestion. E go check di recommendation and give feedback, say make e choose more local option wey no too touristy.

#### Python Implementation Analysis

For Python example, we define and create two agents, each get their own instruction.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Next, `WorkflowBuilder` dey use to build di graph. `front_desk_agent` na di starting point, and dem create edge to connect di output to `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Lastly, di workflow go run with initial user prompt.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run dey run di workflow; get_outputs() go return di output wey di executor produce.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) Implementation Analysis

Di .NET implementation get almost di same logic. First dem define constants for di agents' names and instructions.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Di agents dem create using `AzureOpenAIClient` (Responses API), and `WorkflowBuilder` define di sequential flow by adding edge from `frontDeskAgent` to `reviewerAgent`.

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

Den di workflow run with user message, and results dem stream back.

### Case 2: Multi-Step Sequential Workflow

Dis pattern extend di basic sequence to include more agents. E good for process wey need many stages of refinement or transformation.

#### Scenario Background

User provide image of living room and ask for furniture quote.

1.  **Sales-Agent**: Identify furniture inside di image and create list.
2.  **Price-Agent**: Take di list and give detailed price breakdown, include budget, mid-range, and premium choices.
3.  **Quote-Agent**: Get di priced list and format am into formal quote document for Markdown.

*Diagram of Sales -\> Price -\> Quote workflow.*

#### Python Implementation Analysis

Three agents define, each get special role. Workflow built using `add_edge` to create chain: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Make tri speshal agent dem
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Build di work wey go follow one after di oda
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Input na `ChatMessage` wey get text and image URI. Framework go handle passing output from one agent go the next until final quote done.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Di user message get both text and picture
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Make you run di workflow
events = await workflow.run(message)
```

#### .NET (C\#) Implementation Analysis

.NET example na copy of Python version. Three agents (`salesagent`, `priceagent`, `quoteagent`) create. `WorkflowBuilder` link dem in sequence.

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

User message get image data (as bytes) and text prompt. `InProcessExecution.RunStreamingAsync` start di workflow, and final output dey capture from stream.

### Case 3: Concurrent Workflow

Dis pattern dey use when task fit run at di same time to save time. E get "fan-out" to multiple agents and "fan-in" to collect results.

#### Scenario Background

User ask to plan trip to Seattle.

1.  **Dispatcher (Fan-Out)**: User request send to two agents at once.
2.  **Researcher-Agent**: Research attractions, weather, key things for trip go Seattle for December.
3.  **Plan-Agent**: Independently create detailed daily travel plan.
4.  **Aggregator (Fan-In)**: Collect output from researcher and planner and show all together as final result.

*Diagram of concurrent Researcher and Planner workflow.*

#### Python Implementation Analysis

`ConcurrentBuilder` make dis pattern easy to create. You just list di agents, and di builder go create fan-out and fan-in logic automatically.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder na im dey handle di fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run di workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework make sure say `research_agent` and `plan_agent` run parallel, and their final results gather into list.

#### .NET (C\#) Implementation Analysis

For .NET, you need define am more clearly. Custom executors (`ConcurrentStartExecutor` and `ConcurrentAggregationExecutor`) dey create to manage fan-out and fan-in logic.

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

`WorkflowBuilder` then use `AddFanOutEdge` and `AddFanInEdge` to build graph with these custom executors and agents.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Case 4: Conditional Workflow

Conditional workflows get branch logic, wey make system take different path based on intermediate results.

#### Scenario Background

Dis workflow dey automate creation and publication of technical tutorial.

1.  **Evangelist-Agent**: Write draft of tutorial based on outline and URLs.
2.  **ContentReviewer-Agent**: Review di draft. E check if word count dey pass 200 words.
3.  **Conditional Branch**:
      * **If Approved (`Yes`)**: Workflow go continue to `Publisher-Agent`.
      * **If Rejected (`No`)**: Workflow go stop and output di reason why e reject am.
4.  **Publisher-Agent**: If draft approved, dis agent go save di content to Markdown file.

#### Python Implementation Analysis

Dis example use custom function, `select_targets`, to do conditional logic. Dis function dey pass to `add_multi_selection_edge_group` and e guide workflow based on `review_result` field from reviewer output.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Dis function go find di next step based on di review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If e approved, go ahead go di 'save_draft' executor
        return [save_draft_id]
    else:
        # If e reject, go di 'handle_review' executor make e report say e fail
        return [handle_review_id]

# Di workflow builder dey use di selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Di multi-selection edge dey implement di conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Custom executors like `to_reviewer_result` dey use to parse di JSON output from agent and convert am to strong typed objects wey the selection function fit check.

#### .NET (C\#) Implementation Analysis

.NET version use similar approach with condition function. `Func<object?, bool>` dey define to check `Result` property of `ReviewResult` object.

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

`AddEdge` method condition parameter allow `WorkflowBuilder` create branch path. Workflow go follow edge to `publishExecutor` only if condition `GetCondition(expectedResult: "Yes")` return true. Otherwise, e go path to `sendReviewerExecutor`.

## Conclusion

Microsoft Agent Framework Workflow dey provide strong and flexible foundation to orchestrate complex multi-agent system. Using im graph-based architecture and core parts, developers fit design and build sophisticated workflows for both Python and .NET. Whether your app need simple sequential processing, parallel execution, or dynamic conditional logic, di framework get tools to build powerful, scalable, and type-safe AI-powered solutions.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->