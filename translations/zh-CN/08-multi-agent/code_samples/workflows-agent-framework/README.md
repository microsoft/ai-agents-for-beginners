# 使用 Microsoft Agent Framework Workflow 构建多代理应用程序

本教程将引导您了解并使用 Microsoft Agent Framework 构建多代理应用程序。我们将探讨多代理系统的核心概念，深入研究框架 Workflow 组件的架构，并通过 Python 和 .NET 的实际示例演示不同的工作流模式。

## 1\. 了解多代理系统

AI 代理是一种超越标准大型语言模型（LLM）能力的系统。它能够感知环境、做出决策并采取行动以实现特定目标。多代理系统涉及多个代理协作解决单个代理难以处理的问题。

### 常见应用场景

  * **复杂问题解决**：将一个大型任务（例如规划公司范围的活动）分解为由专业代理处理的小任务（例如预算代理、物流代理、营销代理）。
  * **虚拟助手**：一个主助手代理将任务（如日程安排、研究和预订）委派给其他专业代理。
  * **自动内容创建**：一个代理起草内容，另一个代理审查内容的准确性和语气，第三个代理发布内容。

### 多代理模式

多代理系统可以按照不同的模式组织，这些模式决定了代理之间的交互方式：

  * **顺序模式**：代理按照预定顺序工作，类似于流水线。一个代理的输出成为下一个代理的输入。
  * **并发模式**：代理并行处理任务的不同部分，最终将结果汇总。
  * **条件模式**：工作流根据代理的输出遵循不同的路径，类似于 if-then-else 语句。

## 2\. Microsoft Agent Framework Workflow 架构

Agent Framework 的工作流系统是一个高级编排引擎，旨在管理多个代理之间的复杂交互。它基于图形架构，使用 [Pregel 风格的执行模型](https://kowshik.github.io/JPregel/pregel_paper.pdf)，其中处理在称为“超级步骤”的同步步骤中进行。

### 核心组件

该架构由三个主要部分组成：

1.  **执行器**：这些是基本的处理单元。在我们的示例中，`Agent` 是一种执行器。每个执行器可以有多个消息处理器，这些处理器会根据接收到的消息类型自动调用。
2.  **边**：定义消息在执行器之间传递的路径。边可以设置条件，从而允许信息动态路由通过工作流图。
3.  **工作流**：负责编排整个过程，管理执行器、边以及整体执行流程。它确保消息按正确顺序处理，并流式传输事件以便于观察。

*一个展示工作流系统核心组件的图示。*

这种结构允许使用基本模式（如顺序链、并行处理的扇出/扇入以及条件流的 switch-case 逻辑）构建强大且可扩展的应用程序。

## 3\. 实际示例和代码分析

接下来，我们将探索如何使用框架实现不同的工作流模式。我们将分别查看每个示例的 Python 和 .NET 代码。

### 案例 1：基本顺序工作流

这是最简单的模式，其中一个代理的输出直接传递给另一个代理。我们的场景涉及一个酒店 `FrontDesk` 代理提供旅行推荐，然后由 `Concierge` 代理进行审查。

*一个展示基本 FrontDesk -\> Concierge 工作流的图示。*

#### 场景背景

一位旅客询问巴黎的推荐活动。

1.  `FrontDesk` 代理设计简洁，建议参观卢浮宫。
2.  `Concierge` 代理优先考虑真实体验，接收建议后进行审查，并提供更本地化、非游客化的替代方案。

#### Python 实现分析

在 Python 示例中，我们首先定义并创建两个代理，每个代理都有特定的指令。

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

接下来，使用 `WorkflowBuilder` 构建图。将 `front_desk_agent` 设置为起点，并创建一条边将其输出连接到 `reviewer_agent`。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

最后，使用初始用户提示执行工作流。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) 实现分析

.NET 实现遵循非常类似的逻辑。首先，为代理的名称和指令定义常量。

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

使用 `OpenAIClient` 创建代理，然后通过 `WorkflowBuilder` 定义顺序流程，添加一条边从 `frontDeskAgent` 到 `reviewerAgent`。

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

工作流随后运行用户消息，并将结果流式传输回。

### 案例 2：多步骤顺序工作流

此模式扩展了基本顺序模式，包含更多代理。它非常适合需要多个阶段的精炼或转换的流程。

#### 场景背景

用户提供了一张客厅的图片，并要求提供家具报价。

1.  **Sales-Agent**：识别图片中的家具项目并创建列表。
2.  **Price-Agent**：根据项目列表提供详细的价格细分，包括预算、中档和高端选项。
3.  **Quote-Agent**：接收定价列表并将其格式化为 Markdown 格式的正式报价文档。

*一个展示 Sales -\> Price -\> Quote 工作流的图示。*

#### Python 实现分析

定义三个代理，每个代理都有专门的角色。使用 `add_edge` 构建工作流链：`sales_agent` -\> `price_agent` -\> `quote_agent`。

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

输入是一个包含文本和图片 URI 的 `ChatMessage`。框架处理每个代理的输出并将其传递给下一个代理，直到生成最终报价。

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

#### .NET (C#) 实现分析

.NET 示例与 Python 版本类似。创建三个代理（`salesagent`、`priceagent`、`quoteagent`）。使用 `WorkflowBuilder` 将它们按顺序链接。

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

用户消息包含图片数据（以字节形式）和文本提示。使用 `InProcessExecution.StreamAsync` 方法启动工作流，并从流中捕获最终输出。

### 案例 3：并发工作流

此模式用于任务可以同时执行以节省时间的情况。它包括“扇出”到多个代理和“扇入”以汇总结果。

#### 场景背景

用户要求规划一次去西雅图的旅行。

1.  **Dispatcher (扇出)**：用户请求同时发送给两个代理。
2.  **Researcher-Agent**：研究西雅图 12 月的景点、天气和关键注意事项。
3.  **Plan-Agent**：独立创建详细的每日旅行行程。
4.  **Aggregator (扇入)**：收集研究员和规划员的输出，并将其作为最终结果一起呈现。

*一个展示并发 Researcher 和 Planner 工作流的图示。*

#### Python 实现分析

`ConcurrentBuilder` 简化了此模式的创建。只需列出参与的代理，构建器会自动创建必要的扇出和扇入逻辑。

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

框架确保 `research_agent` 和 `plan_agent` 并行执行，并将它们的最终输出汇总到一个列表中。

#### .NET (C#) 实现分析

在 .NET 中，此模式需要更明确的定义。创建自定义执行器（`ConcurrentStartExecutor` 和 `ConcurrentAggregationExecutor`）以处理扇出和扇入逻辑。

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

然后，`WorkflowBuilder` 使用 `AddFanOutEdge` 和 `AddFanInEdge` 构建图，包含这些自定义执行器和代理。

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### 案例 4：条件工作流

条件工作流引入分支逻辑，允许系统根据中间结果采取不同路径。

#### 场景背景

此工作流自动创建并发布技术教程。

1.  **Evangelist-Agent**：根据给定的大纲和 URL 编写教程草稿。
2.  **ContentReviewer-Agent**：审查草稿，检查字数是否超过 200 字。
3.  **条件分支**：
      * **如果通过（`Yes`）**：工作流继续到 `Publisher-Agent`。
      * **如果拒绝（`No`）**：工作流停止并输出拒绝原因。
4.  **Publisher-Agent**：如果草稿通过审核，此代理将内容保存为 Markdown 文件。

#### Python 实现分析

此示例使用自定义函数 `select_targets` 实现条件逻辑。该函数传递给 `add_multi_selection_edge_group`，并根据审查者输出的 `review_result` 字段指导工作流。

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

使用自定义执行器（如 `to_reviewer_result`）解析代理的 JSON 输出，并将其转换为强类型对象供选择函数检查。

#### .NET (C#) 实现分析

.NET 版本使用类似的方法，通过条件函数实现逻辑。定义一个 `Func<object?, bool>` 来检查 `ReviewResult` 对象的 `Result` 属性。

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

`AddEdge` 方法的 `condition` 参数允许 `WorkflowBuilder` 创建分支路径。工作流仅在条件 `GetCondition(expectedResult: "Yes")` 返回 true 时遵循到 `publishExecutor` 的边，否则遵循到 `sendReviewerExecutor` 的路径。

## 结论

Microsoft Agent Framework Workflow 提供了一个强大且灵活的基础，用于编排复杂的多代理系统。通过利用其基于图形的架构和核心组件，开发者可以在 Python 和 .NET 中设计和实现复杂的工作流。无论您的应用程序需要简单的顺序处理、并行执行还是动态条件逻辑，框架都提供了构建强大、可扩展且类型安全的 AI 驱动解决方案的工具。

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误读，我们概不负责。