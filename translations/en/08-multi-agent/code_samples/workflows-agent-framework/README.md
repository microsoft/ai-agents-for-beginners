# Building Multi-Agent Applications with Microsoft Agent Framework Workflow

This tutorial will help you understand and create multi-agent applications using the Microsoft Agent Framework. We'll cover the basics of multi-agent systems, delve into the architecture of the framework's Workflow component, and explore practical examples in Python and .NET for various workflow patterns.

## 1. Understanding Multi-Agent Systems

An AI Agent is a system that surpasses the capabilities of a standard Large Language Model (LLM). It can perceive its environment, make decisions, and take actions to achieve specific goals. A multi-agent system consists of multiple agents working together to solve problems that would be challenging or impossible for a single agent to handle alone.

### Common Application Scenarios

  * **Complex Problem Solving**: Breaking down a large task (e.g., planning a company-wide event) into smaller sub-tasks managed by specialized agents (e.g., a budget agent, a logistics agent, a marketing agent).
  * **Virtual Assistants**: A primary assistant agent delegating tasks like scheduling, research, and booking to other specialized agents.
  * **Automated Content Creation**: A workflow where one agent drafts content, another reviews it for accuracy and tone, and a third publishes it.

### Multi-Agent Patterns

Multi-agent systems can be organized in various patterns that define their interactions:

  * **Sequential**: Agents operate in a predefined order, like an assembly line. The output of one agent becomes the input for the next.
  * **Concurrent**: Agents work simultaneously on different parts of a task, and their results are combined at the end.
  * **Conditional**: The workflow follows different paths based on an agent's output, similar to an if-then-else statement.

## 2. The Microsoft Agent Framework Workflow Architecture

The Agent Framework's workflow system is an advanced orchestration engine designed to manage complex interactions between multiple agents. It uses a graph-based architecture with a [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), where processing occurs in synchronized steps called "supersteps."

### Core Components

The architecture consists of three main parts:

1. **Executors**: These are the basic processing units. In our examples, an `Agent` is a type of executor. Each executor can have multiple message handlers that are automatically triggered based on the type of message received.
2. **Edges**: These define the paths messages take between executors. Edges can include conditions, enabling dynamic routing of information through the workflow graph.
3. **Workflow**: This component orchestrates the entire process, managing executors, edges, and the overall execution flow. It ensures messages are processed in the correct order and streams events for observability.

*A diagram illustrating the core components of the workflow system.*

This structure enables the creation of robust and scalable applications using fundamental patterns like sequential chains, fan-out/fan-in for parallel processing, and switch-case logic for conditional flows.

## 3. Practical Examples and Code Analysis

Let's explore how to implement different workflow patterns using the framework. We'll examine Python and .NET code for each example.

### Case 1: Basic Sequential Workflow

This is the simplest pattern, where one agent's output is directly passed to another. In this scenario, a hotel `FrontDesk` agent makes a travel recommendation, which is then reviewed by a `Concierge` agent.

*Diagram of the basic FrontDesk -> Concierge workflow.*

#### Scenario Background

A traveler requests a recommendation for Paris.

1. The `FrontDesk` agent, focused on brevity, suggests visiting the Louvre Museum.
2. The `Concierge` agent, prioritizing authentic experiences, reviews the suggestion and provides feedback, recommending a more local, less touristy alternative.

#### Python Implementation Analysis

In the Python example, we first define and create the two agents, each with specific instructions.

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

Next, the `WorkflowBuilder` is used to construct the graph. The `front_desk_agent` is set as the starting point, and an edge is created to connect its output to the `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Finally, the workflow is executed with the initial user prompt.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) Implementation Analysis

The .NET implementation follows a similar logic. First, constants are defined for the agents' names and instructions.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

The agents are created using an `OpenAIClient`, and then the `WorkflowBuilder` defines the sequential flow by adding an edge from the `frontDeskAgent` to the `reviewerAgent`.

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

The workflow is then run with the user's message, and the results are streamed back.

### Case 2: Multi-Step Sequential Workflow

This pattern extends the basic sequence to include more agents. It's ideal for processes requiring multiple stages of refinement or transformation.

#### Scenario Background

A user provides an image of a living room and requests a furniture quote.

1. **Sales-Agent**: Identifies the furniture items in the image and creates a list.
2. **Price-Agent**: Takes the list of items and provides a detailed price breakdown, including budget, mid-range, and premium options.
3. **Quote-Agent**: Receives the priced list and formats it into a formal quote document in Markdown.

*Diagram of the Sales -> Price -> Quote workflow.*

#### Python Implementation Analysis

Three agents are defined, each with a specialized role. The workflow is constructed using `add_edge` to create a chain: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

The input is a `ChatMessage` that includes both text and the image URI. The framework handles passing the output of each agent to the next in the sequence until the final quote is generated.

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

#### .NET (C#) Implementation Analysis

The .NET example mirrors the Python version. Three agents (`salesagent`, `priceagent`, `quoteagent`) are created. The `WorkflowBuilder` links them sequentially.

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

The user's message is constructed with both the image data (as bytes) and the text prompt. The `InProcessExecution.StreamAsync` method initiates the workflow, and the final output is captured from the stream.

### Case 3: Concurrent Workflow

This pattern is used when tasks can be performed simultaneously to save time. It involves a "fan-out" to multiple agents and a "fan-in" to aggregate the results.

#### Scenario Background

A user requests a trip plan for Seattle.

1. **Dispatcher (Fan-Out)**: The user's request is sent to two agents simultaneously.
2. **Researcher-Agent**: Researches attractions, weather, and key considerations for a trip to Seattle in December.
3. **Plan-Agent**: Independently creates a detailed day-by-day travel itinerary.
4. **Aggregator (Fan-In)**: The outputs from both the researcher and the planner are collected and presented together as the final result.

*Diagram of the concurrent Researcher and Planner workflow.*

#### Python Implementation Analysis

The `ConcurrentBuilder` simplifies the creation of this pattern. You list the participating agents, and the builder automatically creates the necessary fan-out and fan-in logic.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

The framework ensures that the `research_agent` and `plan_agent` execute in parallel, and their final outputs are collected into a list.

#### .NET (C#) Implementation Analysis

In .NET, this pattern requires a more explicit definition. Custom executors (`ConcurrentStartExecutor` and `ConcurrentAggregationExecutor`) are created to handle the fan-out and fan-in logic.

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

The `WorkflowBuilder` then uses `AddFanOutEdge` and `AddFanInEdge` to construct the graph with these custom executors and the agents.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Case 4: Conditional Workflow

Conditional workflows introduce branching logic, allowing the system to take different paths based on intermediate results.

#### Scenario Background

This workflow automates the creation and publication of a technical tutorial.

1. **Evangelist-Agent**: Writes a draft of the tutorial based on a given outline and URLs.
2. **ContentReviewer-Agent**: Reviews the draft. It checks if the word count exceeds 200 words.
3. **Conditional Branch**:
      * **If Approved (`Yes`)**: The workflow proceeds to the `Publisher-Agent`.
      * **If Rejected (`No`)**: The workflow stops and outputs the reason for rejection.
4. **Publisher-Agent**: If the draft is approved, this agent saves the content to a Markdown file.

#### Python Implementation Analysis

This example uses a custom function, `select_targets`, to implement the conditional logic. This function is passed to `add_multi_selection_edge_group` and directs the workflow based on the `review_result` field from the reviewer's output.

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

Custom executors like `to_reviewer_result` are used to parse the JSON output from the agents and convert it into strongly-typed objects that the selection function can inspect.

#### .NET (C#) Implementation Analysis

The .NET version uses a similar approach with a condition function. A `Func<object?, bool>` is defined to check the `Result` property of the `ReviewResult` object.

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

The `AddEdge` method's `condition` parameter allows the `WorkflowBuilder` to create a branching path. The workflow will only follow the edge to `publishExecutor` if the condition `GetCondition(expectedResult: "Yes")` returns true. Otherwise, it follows the path to `sendReviewerExecutor`.

## Conclusion

The Microsoft Agent Framework Workflow provides a powerful and flexible foundation for orchestrating complex, multi-agent systems. By leveraging its graph-based architecture and core components, developers can design and implement sophisticated workflows in both Python and .NET. Whether your application requires simple sequential processing, parallel execution, or dynamic conditional logic, the framework offers the tools to build scalable, type-safe, AI-powered solutions.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.