# 探索微软代理框架

![Agent Framework](../../../translated_images/zh-CN/lesson-14-thumbnail.90df0065b9d234ee.webp)

### 介绍

本课将涵盖：

- 了解微软代理框架：关键特性和价值  
- 探索微软代理框架的核心概念
- 进阶 MAF 模式：工作流程、中间件和记忆

## 学习目标

完成本课后，您将能够：

- 使用微软代理框架构建生产就绪的 AI 代理
- 将微软代理框架的核心特性应用于您的代理用例
- 使用包括工作流程、中间件和可观察性在内的高级模式

## 代码示例 

[微软代理框架 (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) 的代码示例可以在本仓库的 `xx-python-agent-framework` 和 `xx-dotnet-agent-framework` 文件中找到。

## 了解微软代理框架

![Framework Intro](../../../translated_images/zh-CN/framework-intro.077af16617cf130c.webp)

[微软代理框架 (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) 是微软用于构建 AI 代理的统一框架。它具备灵活性，能够满足生产和研究环境中广泛的代理用例，包括：

- <strong>顺序代理编排</strong>，适用于需逐步完成工作流程的场景。
- <strong>并发编排</strong>，适用于代理需同时完成任务的场景。
- <strong>群聊编排</strong>，适用于多个代理协同完成一个任务的场景。
- <strong>交接编排</strong>，适用于代理在完成子任务后相互交接任务的场景。
- <strong>磁性编排</strong>，适用于经理代理创建并修改任务列表，协调子代理完成任务的场景。

为了在生产环境中交付 AI 代理，MAF 还包括以下功能：

- <strong>可观察性</strong>，通过使用 OpenTelemetry，AI 代理的每个动作都可以被监控，包括工具调用、编排步骤、推理流程及通过 Microsoft Foundry 仪表板进行的性能监控。
- <strong>安全性</strong>，代理原生托管于 Microsoft Foundry，具备基于角色的访问控制、私有数据处理及内置内容安全等安全控制。
- <strong>持久性</strong>，代理线程和工作流程能够暂停、恢复及从错误中恢复，支持长时间运行的进程。
- <strong>控制</strong>，支持人工流程，任务可标记为需要人工审批。

微软代理框架还专注于实现互操作性：

- <strong>云中立性</strong>——代理可运行于容器、本地及多个不同云环境。
- <strong>提供商中立性</strong>——代理可通过您首选的 SDK 创建，包括 Azure OpenAI 和 OpenAI
- <strong>集成开放标准</strong>——代理可使用代理间协议 (Agent-to-Agent, A2A) 和模型上下文协议 (Model Context Protocol, MCP) 来发现并调用其他代理和工具。
- <strong>插件和连接器</strong>——可连接到数据和记忆服务，如 Microsoft Fabric、SharePoint、Pinecone 和 Qdrant。

让我们看看这些功能如何应用于微软代理框架的一些核心概念。

## 微软代理框架核心概念

### 代理

![Agent Framework](../../../translated_images/zh-CN/agent-components.410a06daf87b4fef.webp)

<strong>创建代理</strong>

创建代理通过定义推理服务（LLM 提供者）、
一套供 AI 代理遵循的指令，以及一个分配的 `name` 实现：


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

上述使用的是 `Azure OpenAI`，但代理可以使用包括 `Microsoft Foundry Agent Service` 在内的多种服务创建：

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI 的 `Responses`、`ChatCompletion` API

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

或者 [MiniMax](https://platform.minimaxi.com/)，它提供了支持大上下文窗口（最高达204K标记）的 OpenAI 兼容 API：

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

或使用 A2A 协议的远程代理：

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

<strong>运行代理</strong>

代理通过 `.run` 或 `.run_stream` 方法运行，以获取非流式或流式响应。

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

每次代理运行都可以有选项来自定义参数，比如代理使用的 `max_tokens`，代理能够调用的 `tools`，甚至是用于代理的 `model` 本身。

当完成用户任务需要特定模型或工具时，这非常有用。

<strong>工具</strong>

工具可以在定义代理时定义：

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# 当直接创建一个 ChatAgent 时

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

也可以在运行代理时定义：

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # 仅为此次运行提供的工具 )
```

<strong>代理线程</strong>

代理线程用于处理多轮对话。线程可以通过以下方式创建：

- 使用 `get_new_thread()`，允许随时间保存线程
- 在运行代理时自动创建线程，且线程仅在当前运行期间存在。

创建线程的代码如下：

```python
# 创建一个新线程。
thread = agent.get_new_thread() # 使用该线程运行代理。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

之后可以序列化线程以便后续使用：

```python
# 创建一个新线程。
thread = agent.get_new_thread() 

# 使用线程运行代理。

response = await agent.run("Hello, how are you?", thread=thread) 

# 序列化线程以便存储。

serialized_thread = await thread.serialize() 

# 从存储加载后反序列化线程状态。

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

<strong>代理中间件</strong>

代理与工具和大语言模型交互以完成用户任务。在某些场景下，我们希望在这些交互之间执行或跟踪操作。代理中间件使我们能够通过以下方式实现这一点：

<em>函数中间件</em>

此中间件允许我们在代理和它调用的函数/工具之间执行一个操作。比如，在函数调用时进行一些日志记录。

下面代码中 `next` 定义是否调用下一个中间件或实际函数。

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # 预处理：函数执行前记录日志
    print(f"[Function] Calling {context.function.name}")

    # 继续执行下一个中间件或函数
    await next(context)

    # 后处理：函数执行后记录日志
    print(f"[Function] {context.function.name} completed")
```

<em>聊天中间件</em>

该中间件允许我们在代理和大语言模型请求之间执行或记录一个操作。

它包含了发送给 AI 服务的重要信息，如 `messages`。

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # 预处理：在调用AI之前记录日志
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # 继续下一个中间件或AI服务
    await next(context)

    # 后处理：在AI响应后记录日志
    print("[Chat] AI response received")

```

<strong>代理记忆</strong>

如 `Agentic Memory` 课程所述，记忆是使代理跨不同上下文操作的重要元素。MAF 提供了几种不同类型的记忆：

<em>内存存储</em>

这是在应用运行时线程中存储的记忆。

```python
# 创建一个新线程。
thread = agent.get_new_thread() # 使用该线程运行代理。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

<em>持久消息</em>

该记忆用于存储跨不同会话的对话历史。通过 `chat_message_store_factory` 定义：

```python
from agent_framework import ChatMessageStore

# 创建自定义消息存储
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

<em>动态记忆</em>

此记忆在代理运行前加入上下文中。它们可以存储在外部服务如 mem0 中：

```python
from agent_framework.mem0 import Mem0Provider

# 使用 Mem0 实现高级内存功能
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

<strong>代理可观测性</strong>


可观察性对于构建可靠且易维护的智能系统非常重要。MAF 集成了 OpenTelemetry，提供追踪和计量功能以增强可观察性。

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # 做某事
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### 工作流

MAF 提供预定义步骤的工作流，用于完成任务，这些步骤中包含 AI 代理作为组件。

工作流由不同的组件组成，以实现更好的控制流。工作流还支持<strong>多代理编排</strong>和<strong>检查点</strong>以保存工作流状态。

工作流的核心组件有：

<strong>执行器</strong>

执行器接收输入消息，执行分配的任务，然后产生输出消息，推动工作流向完成更大任务的方向前进。执行器可以是 AI 代理或自定义逻辑。

<strong>边</strong>

边用于定义工作流中消息的流向，分为以下几种：

<em>直接边</em> – 执行器之间的一对一简单连接：

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

<em>条件边</em> – 在满足某些条件后激活。例如，当酒店房间不可用时，执行器可以建议其他选项。

*开关-分支边* – 根据定义的条件将消息路由到不同的执行器。例如，如果旅客拥有优先访问权，他们的任务将通过另一个工作流处理。

<em>分发边</em> – 发送一个消息到多个目标。

<em>汇聚边</em> – 从多个执行器收集多条消息并发送到一个目标。

<strong>事件</strong>

为了更好地观察工作流执行情况，MAF 提供了内建的执行事件，包括：

- `WorkflowStartedEvent`  - 工作流开始执行
- `WorkflowOutputEvent` - 工作流产生输出
- `WorkflowErrorEvent` - 工作流遇到错误
- `ExecutorInvokeEvent`  - 执行器开始处理
- `ExecutorCompleteEvent`  -  执行器完成处理
- `RequestInfoEvent` - 请求发起

## 高级 MAF 模式

上面章节涵盖了 Microsoft Agent Framework 的关键概念。随着你构建更复杂的代理，请考虑以下一些高级模式：

- <strong>中间件组合</strong>：通过函数和聊天中间件链多个中间件处理器（日志、身份验证、速率限制），实现对代理行为的精细控制。
- <strong>工作流检查点</strong>：使用工作流事件和序列化来保存和恢复长时间运行的代理进程。
- <strong>动态工具选择</strong>：结合基于工具描述的检索增强生成（RAG）和 MAF 的工具注册，只展示每次查询相关的工具。
- <strong>多代理交接</strong>：使用工作流边和条件路由来编排专业代理之间的任务交接。

## 在 Microsoft Foundry 上托管 LangChain / LangGraph 代理

Microsoft Agent Framework 是<strong>框架互操作的</strong>——你不必局限于用 MAF 编写的代理。如果你已有基于 **LangChain** 或 **LangGraph** 构建的代理，可以将其作为<strong>Microsoft Foundry 托管代理</strong>运行，Foundry 负责运行时、会话、扩展性、身份和协议端点管理，而代理逻辑仍在 LangGraph 中。

这是通过 `langchain_azure_ai.agents.hosting` 包实现的，它以 Foundry 托管代理使用的相同协议导出已编译的 LangGraph 图。

**1. 安装托管扩展：**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` 扩展安装 Foundry 协议库：`azure-ai-agentserver-responses`（兼容 OpenAI 的 `/responses` 端点）和 `azure-ai-agentserver-invocations`（通用的 `/invocations` 端点）。

**2. 选择托管协议：**

| 协议 | 主机类 | 端点 | 适用场景 |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | 需要兼容 OpenAI 的聊天、流式传输、响应历史和对话线程 — 推荐用于对话型代理。 |
| **Invocations** | `InvocationsHostServer` | `/invocations` | 需要自定义 JSON 结构、Webhook 风格端点或非对话处理。 |

因为<strong>Responses API 是 Foundry 中代理风格开发的主API</strong>，大多数代理建议从 `ResponsesHostServer` 开始。

**3. 配置环境变量**（先执行 `az login` 以便 `DefaultAzureCredential` 验证身份）：

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

当代理以后作为托管代理在 Foundry 运行时，平台会自动注入 `FOUNDRY_PROJECT_ENDPOINT`。

**4. 通过 Responses 协议公开 LangGraph 代理：**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI 这里的目标是 Foundry 项目的兼容 OpenAI 的（响应）端点。
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

本地运行命令为 `python main.py`，然后发送一个 Responses 请求到 `http://localhost:8088/responses`。

**关键行为：**

- <strong>对话</strong>：客户端通过传递 `previous_response_id` 或 `conversation` ID 来继续对话。如果你的图是用 LangGraph 检查点编译的，Foundry 会将对话状态与检查点关联（生产环境使用持久化检查点，本地测试使用 `MemorySaver` 即可）。
- <strong>人机交互</strong>：如果图中使用 LangGraph 的 `interrupt()`，`ResponsesHostServer` 会将待处理中断显示为 Responses 的 `function_call` / `mcp_approval_request` 项，客户端通过匹配的 `function_call_output` / `mcp_approval_response` 继续。
- **部署到 Foundry**：使用 Azure Developer CLI — 运行命令 `azd ext install azure.ai.agents`，`azd ai agent init -m <manifest>`，`azd ai agent run`（本地，需要 Docker），然后 `azd provision` 和 `azd deploy`。托管代理的部署需要 **Foundry 项目管理员** 角色。

这个示例的可运行版本位于 [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)。完整演示（Invocations 协议、自定义请求模式和故障排除）请参见 [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)。

## 代码示例

Microsoft Agent Framework 的代码示例可以在本仓库的 `xx-python-agent-framework` 和 `xx-dotnet-agent-framework` 文件夹中找到。

## 还有关于 Microsoft Agent Framework 的更多问题吗？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，与其他学习者交流，参加问答时间，解决你的 AI 代理问题。
## 上一课

[AI 代理的记忆](../13-agent-memory/README.md)

## 下一课

[构建计算机使用代理 (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->