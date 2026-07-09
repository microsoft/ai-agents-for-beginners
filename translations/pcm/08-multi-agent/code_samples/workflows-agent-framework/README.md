# How To Build Multi-Agent Applications Wit Microsoft Agent Framework Workflow

Dis tutorial go help you sabi and build multi-agent applications using Microsoft Agent Framework. We go check di main tins wey dey multi-agent systems, look inside di framework Workflow component, and go through real examples for both Python and .NET for different workflow patterns.

## 1\. Wetin be Multi-Agent Systems

AI Agent na system wey pass wetin normal Large Language Model (LLM) fit do. E fit see im surroundings, make decision, and take action to meet specific goals. Multi-agent system mean say plenty of these agents go work together to solve wahala wey one agent alone no fit handle.

### Common Application Scenarios

  * **Complex Problem Solving**: Break big work (like plan company big event) into smaller small work wey specialized agents fit do (like budget agent, logistics agent, marketing agent).
  * **Virtual Assistants**: Main assistant agent dey give other specialized agents tasks like scheduling, research, and booking.
  * **Automated Content Creation**: Workflow wey one agent dey create draft content, another dey check am for correctness and style, then third one dey publish am.

### Multi-Agent Patterns

Multi-agent systems dey arranged for different patterns wey show how dem go interact:

  * **Sequential**: Agents dey work one by one for order, like assembly line. One agent output na the next agent input.
  * **Concurrent**: Agents dey work at the same time for different parts of task, then dem combine results at the end.
  * **Conditional**: Workflow follow different road based on agent output, like if-then-else statement.

## 2\. Microsoft Agent Framework Workflow Architecture

Agent Framework workflow system na advance kind engine wey organize how agents dem go interact. E use graph-based architecture wey get [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), wey dey process things step by step called "supersteps."

### Core Components

Architecture get three main parts:

1.  **Executors**: Na di main processing units. For our examples, `Agent` na executor type. Each executor fit get many message handlers wey automatic run based on message type.
2.  **Edges**: Dem show di path wey messages follow between executors. Edges get conditions wey fit route message differently inside workflow graph.
3.  **Workflow**: Dis one dey manage all di process, di executors, edges, and di flow of execution. E make sure messages process in correct order and dey stream events for monitoring.

*Diagram wey show main parts of workflow system.*

Dis structure make e easy to build strong and scalable applications using common patterns like sequential chains, fan-out/fan-in for parallel processing, and switch-case for conditional flows.

## 3\. Practical Examples and Code Analysis

Make we check how to implement different workflow patterns using di framework. We go see Python and .NET code for each example.

### Case 1: Basic Sequential Workflow

Dis na di simplest pattern, wey one agent output go straight to another agent. Our example na hotel `FrontDesk` agent wey go give travel advice, then `Concierge` agent go check am.

*Diagram for basic FrontDesk -\> Concierge workflow.*

#### Scenario Background

Traveler dey ask for recommendation for Paris.

1.  `FrontDesk` agent, e dey short and simple, recommend say make e visit Louvre Museum.
2.  `Concierge` agent, wey like authentic experience, receive the advice. E go check am, then give feedback say e better make e go local place wey no too touristy.

#### Python Implementation Analysis

For Python example, we go first define and create the two agents, each get im own instruction.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define wetin agent dem go do and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Make agent instances
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Next, `WorkflowBuilder` dey use to build the graph. `front_desk_agent` na starting point, then dem create edge to connect im output to `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Finally, workflow run with initial user prompt.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run dey execute di workflow; get_outputs() go return di output wey di executor produce.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) Implementation Analysis

.NET one follow very similar logic. Dem first define constants for agent names and instructions.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agents create using `AzureOpenAIClient` (Responses API), then `WorkflowBuilder` define sequential flow, add edge from `frontDeskAgent` to `reviewerAgent`.

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

Then workflow run na with user message and results stream back.

### Case 2: Multi-Step Sequential Workflow

Dis pattern extend basic sequence to include more agents. E good for process wey need more stages to improve or change.

#### Scenario Background

User give picture of living room and ask for furniture quote.

1.  **Sales-Agent**: Identify furniture for the picture and make list.
2.  **Price-Agent**: Take the list and break down price, show budget, mid-range, and premium options.
3.  **Quote-Agent**: Take priced list then format am to formal quote in Markdown.

*Diagram of Sales -\> Price -\> Quote workflow.*

#### Python Implementation Analysis

Three agents define, each get specialized role. Workflow build with `add_edge` to chain: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Make three specialized agents
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Build di workflow wey dey go one by one
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Input na `ChatMessage` wey get text and image URI. Framework dey pass output from one agent to next until quote done.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Di user message get both text and one piksha
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

.NET example na similar to Python version. Three agents (`salesagent`, `priceagent`, `quoteagent`) create. `WorkflowBuilder` link dem one by one.

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

User message get image data (bytes) and text. `InProcessExecution.StreamAsync` dey start workflow, final output come from the stream.

### Case 3: Concurrent Workflow

Dis pattern for when work fit happen at the same time to save time. E get "fan-out" to many agents and "fan-in" to gather results.

#### Scenario Background

User wan plan trip go Seattle.

1.  **Dispatcher (Fan-Out)**: User request go two agents at once.
2.  **Researcher-Agent**: Research places, weather, and wetin todo for Seattle trip for December.
3.  **Plan-Agent**: Create detailed day-by-day travel plan.
4.  **Aggregator (Fan-In)**: Collect output from researcher and planner join am as final result.

*Diagram for concurrent Researcher and Planner workflow.*

#### Python Implementation Analysis

`ConcurrentBuilder` dey make am easy to build dis pattern. You just list the agents and builder create fan-out and fan-in logic automatically.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder dey handle di fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run di workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework make sure say `research_agent` and `plan_agent` dey run parallel, their final results join for list.

#### .NET (C\#) Implementation Analysis

For .NET, dis pattern need explicit definition. Custom executors (`ConcurrentStartExecutor` and `ConcurrentAggregationExecutor`) create to handle fan-out and fan-in logic.

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

Then `WorkflowBuilder` use `AddFanOutEdge` and `AddFanInEdge` to build graph with custom executors and agents.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Case 4: Conditional Workflow

Conditional workflows get branching logic, wey allow system to follow different road based on intermediate results.

#### Scenario Background

Dis workflow na automation for creating and publishing technical tutorial.

1.  **Evangelist-Agent**: Write draft of tutorial based on outline and URLs.
2.  **ContentReviewer-Agent**: Check draft. E check if word count pass 200.
3.  **Conditional Branch**:
      * **If Approved (`Yes`)**: Workflow continue to `Publisher-Agent`.
      * **If Rejected (`No`)**: Workflow stop and show reason why e reject.
4.  **Publisher-Agent**: If draft approve, dis agent save content to Markdown file.

#### Python Implementation Analysis

This example use custom function `select_targets` to run conditional logic. E pass to `add_multi_selection_edge_group` and guide workflow based on `review_result` from reviewer output.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Dis function go decide wetin to do next based on di review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If dem approve am, make you go di 'save_draft' executor
        return [save_draft_id]
    else:
        # If dem no approve am, make you go di 'handle_review' executor to yarn say e fail
        return [handle_review_id]

# Di workflow builder dey use di selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Di multi-selection edge dey do di conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Custom executors like `to_reviewer_result` dey parse JSON output from agents and convert am to strong-typed objects wey selection function fit check.

#### .NET (C\#) Implementation Analysis

.NET version use similar way with condition function. `Func<object?, bool>` define to check `Result` property of `ReviewResult` object.

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

`AddEdge` method `condition` parameter allow `WorkflowBuilder` create branching road. Workflow go follow edge to `publishExecutor` if condition `GetCondition(expectedResult: "Yes")` true. If no, e follow path to `sendReviewerExecutor`.

## Conclusion

Microsoft Agent Framework Workflow na strong and flexible foundation to organize complex multi-agent systems. Using graph-based architecture and core parts, developers fit design and build advanced workflows for Python and .NET. Whether your app need simple sequential processing, parallel execution, or dynamic conditional logic, dis framework get tools to build powerful, scalable, and safe AI-powered solutions.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->