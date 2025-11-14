<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b39c052ef109db90ad9251183791e2d6",
  "translation_date": "2025-11-11T11:58:45+00:00",
  "source_file": "08-multi-agent/code_samples/workflows-agent-framework/README.md",
  "language_code": "pcm"
}
-->
# How to Build Multi-Agent Applications wit Microsoft Agent Framework Workflow

Dis tutorial go show you how you fit sabi and build multi-agent applications wit Microsoft Agent Framework. We go look di main idea of multi-agent systems, check di architecture of di framework Workflow part, and do practical examples for Python and .NET for different workflow patterns.

## 1\. Wetin Be Multi-Agent Systems

AI Agent na system wey dey do pass wetin normal Large Language Model (LLM) fit do. E fit see wetin dey happen for e environment, make decisions, and do actions to achieve di goals wey dem give am. Multi-agent system na when plenty of dis agents dey work together to solve problem wey one agent no fit handle alone.

### Common Ways People Dey Use Am

  * **Solve Big Problems**: Break big work (like planning company event) into small-small work wey different agents go handle (like budget agent, logistics agent, marketing agent).
  * **Virtual Assistants**: One main assistant agent go dey give work like scheduling, research, and booking to other agents wey sabi di work well.
  * **Automated Content Creation**: Workflow wey one agent go write content, another one go check am for correct grammar and tone, and di last one go publish am.

### Multi-Agent Patterns

Multi-agent systems fit dey arranged in different ways, wey go show how dem go work together:

  * **Sequential**: Agents go dey work one after di other, like assembly line. Wetin one agent do go be di input for di next one.
  * **Concurrent**: Agents go dey work at di same time for different parts of di work, and dem go join di results together at di end.
  * **Conditional**: Workflow go follow different road based on wetin one agent do, like if-then-else statement.

## 2\. Di Microsoft Agent Framework Workflow Architecture

Di Agent Framework workflow system na advanced engine wey dey manage how plenty agents go work together. E dey use graph-based architecture wey dey follow [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), where processing dey happen step by step, dem dey call am "supersteps."

### Main Parts

Di architecture get three main parts:

1.  **Executors**: Na di main processing units. For our example, `Agent` na one type of executor. Each executor fit get plenty message handlers wey go dey work automatically based on di type of message wey e receive.
2.  **Edges**: Na di road wey messages go follow between executors. Edges fit get conditions, wey go allow dynamic routing of information for di workflow graph.
3.  **Workflow**: Dis one dey control di whole process, e dey manage di executors, edges, and how di execution go flow. E dey make sure say messages dey process in di correct order and e dey stream events for monitoring.

*Diagram wey dey show di main parts of di workflow system.*

Dis structure dey allow people build strong and scalable applications using basic patterns like sequential chains, fan-out/fan-in for parallel processing, and switch-case logic for conditional flows.

## 3\. Practical Examples and Code Analysis

Make we check how to use di framework build different workflow patterns. We go look Python and .NET code for each example.

### Case 1: Basic Sequential Workflow

Dis na di simplest pattern, where one agent go pass e output directly to another one. Di example na hotel `FrontDesk` agent wey dey make travel recommendation, and `Concierge` agent go review am.

*Diagram of di basic FrontDesk -\> Concierge workflow.*

#### Scenario Background

Traveler dey ask for recommendation for Paris.

1.  Di `FrontDesk` agent go suggest make dem visit Louvre Museum.
2.  Di `Concierge` agent go review di suggestion and give feedback, suggest better local place wey no too dey touristy.

#### Python Implementation Analysis

For di Python example, we go first define and create di two agents, each one get e own instructions.

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

Next, we go use `WorkflowBuilder` build di graph. Di `front_desk_agent` go be di starting point, and we go create edge wey go connect e output to di `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Finally, we go run di workflow wit di user prompt.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C\#) Implementation Analysis

Di .NET implementation dey similar. First, we go define constants for di agents' names and instructions.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

We go create di agents wit `OpenAIClient`, and then use `WorkflowBuilder` define di sequential flow by adding edge from `frontDeskAgent` to `reviewerAgent`.

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

Di workflow go run wit di user message, and we go stream di results back.

### Case 2: Multi-Step Sequential Workflow

Dis pattern dey add more agents to di basic sequence. E dey good for processes wey need plenty stages of refinement or transformation.

#### Scenario Background

User go provide image of living room and ask for furniture quote.

1.  **Sales-Agent**: E go identify di furniture items for di image and create list.
2.  **Price-Agent**: E go take di list of items and give detailed price breakdown, including budget, mid-range, and premium options.
3.  **Quote-Agent**: E go take di priced list and format am into formal quote document for Markdown.

*Diagram of di Sales -\> Price -\> Quote workflow.*

#### Python Implementation Analysis

We go define three agents, each one get e own role. Di workflow go dey build wit `add_edge` to create chain: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Di input na `ChatMessage` wey get text and image URI. Di framework go handle how di output of each agent go pass to di next one until di final quote dey ready.

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

Di .NET example dey same as di Python version. We go create three agents (`salesagent`, `priceagent`, `quoteagent`). Di `WorkflowBuilder` go link dem sequentially.

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

Di user message go get di image data (as bytes) and di text prompt. Di `InProcessExecution.StreamAsync` method go start di workflow, and we go collect di final output from di stream.

### Case 3: Concurrent Workflow

Dis pattern dey good when tasks fit dey do at di same time to save time. E dey involve "fan-out" to plenty agents and "fan-in" to join di results.

#### Scenario Background

User dey ask to plan trip to Seattle.

1.  **Dispatcher (Fan-Out)**: Di user request go go to two agents at di same time.
2.  **Researcher-Agent**: E go research attractions, weather, and key things for trip to Seattle for December.
3.  **Plan-Agent**: E go create detailed day-by-day travel plan.
4.  **Aggregator (Fan-In)**: Di outputs from di researcher and planner go join together as di final result.

*Diagram of di concurrent Researcher and Planner workflow.*

#### Python Implementation Analysis

Di `ConcurrentBuilder` dey make dis pattern easy. You go just list di agents wey go work, and di builder go automatically create di fan-out and fan-in logic.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Di framework go make sure say `research_agent` and `plan_agent` dey work at di same time, and e go join their final outputs into one list.

#### .NET (C\#) Implementation Analysis

For .NET, dis pattern need more explicit definition. Custom executors (`ConcurrentStartExecutor` and `ConcurrentAggregationExecutor`) go handle di fan-out and fan-in logic.

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

Di `WorkflowBuilder` go use `AddFanOutEdge` and `AddFanInEdge` build di graph wit di custom executors and di agents.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Case 4: Conditional Workflow

Conditional workflows dey add branching logic, wey go allow di system follow different road based on wetin e get from di agents.

#### Scenario Background

Dis workflow dey automate how to create and publish technical tutorial.

1.  **Evangelist-Agent**: E go write draft of di tutorial based on outline and URLs wey dem give am.
2.  **ContentReviewer-Agent**: E go review di draft. E go check if di word count pass 200 words.
3.  **Conditional Branch**:
      * **If Approved (`Yes`)**: Di workflow go continue to `Publisher-Agent`.
      * **If Rejected (`No`)**: Di workflow go stop and show why dem reject am.
4.  **Publisher-Agent**: If dem approve di draft, dis agent go save di content as Markdown file.

#### Python Implementation Analysis

Dis example dey use custom function, `select_targets`, to do di conditional logic. Dis function dey pass to `add_multi_selection_edge_group` and e dey direct di workflow based on di `review_result` field from di reviewer output.

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

Custom executors like `to_reviewer_result` dey parse di JSON output from di agents and change am to objects wey di selection function fit check.

#### .NET (C\#) Implementation Analysis

Di .NET version dey use similar way wit condition function. `Func<object?, bool>` dey check di `Result` property of di `ReviewResult` object.

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

Di `AddEdge` method `condition` parameter dey allow di `WorkflowBuilder` create branching path. Di workflow go only follow di edge to `publishExecutor` if di condition `GetCondition(expectedResult: "Yes")` return true. If not, e go follow di road to `sendReviewerExecutor`.

## Conclusion

Di Microsoft Agent Framework Workflow na strong and flexible tool wey dey help manage how plenty agents go work together. Wit di graph-based architecture and di main parts, developers fit design and build advanced workflows for Python and .NET. Whether your application need simple sequential processing, parallel execution, or conditional logic, di framework get di tools to build powerful, scalable, and type-safe AI-powered solutions.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg make you sabi say automated translations fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->