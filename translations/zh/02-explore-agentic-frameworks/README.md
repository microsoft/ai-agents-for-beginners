# 探索 AI Agent 框架

AI Agent 框架是专为简化 AI Agent 的创建、部署和管理而设计的软件平台。这些框架为开发者提供了预构建的组件、抽象和工具，从而简化了复杂 AI 系统的开发流程。

通过为 AI Agent 开发中的常见挑战提供标准化的方法，这些框架帮助开发者专注于应用的独特部分。它们提升了构建 AI 系统的可扩展性、可访问性和效率。

## 简介

本课程将涵盖以下内容：

- 什么是 AI Agent 框架？它能让开发者实现什么？
- 团队如何利用这些框架快速原型设计、迭代并提升 Agent 的能力？
- 微软开发的框架和工具（[Autogen](https://aka.ms/ai-agents/autogen) / [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel) / [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service)）之间有什么区别？
- 我可以直接集成现有的 Azure 生态系统工具，还是需要独立的解决方案？
- 什么是 Azure AI Agent Service？它如何帮助我？

## 学习目标

本课程的目标是帮助你理解：

- AI Agent 框架在 AI 开发中的作用。
- 如何利用 AI Agent 框架构建智能 Agent。
- AI Agent 框架所支持的关键功能。
- Autogen、Semantic Kernel 和 Azure AI Agent Service 之间的差异。

## 什么是 AI Agent 框架？它能让开发者实现什么？

传统的 AI 框架可以帮助你将 AI 集成到应用中，并通过以下方式提升应用性能：

- **个性化**：AI 可以分析用户行为和偏好，提供个性化的推荐、内容和体验。
  示例：流媒体服务（如 Netflix）利用 AI 根据观看历史推荐电影和节目，从而提升用户参与度和满意度。
- **自动化和效率**：AI 能够自动化重复性任务、优化工作流程并提高运营效率。
  示例：客户服务应用利用 AI 驱动的聊天机器人处理常见查询，从而减少响应时间，并将人类员工解放出来处理更复杂的问题。
- **增强用户体验**：AI 可以通过语音识别、自然语言处理和预测性文本等智能功能提升整体用户体验。
  示例：虚拟助手（如 Siri 和 Google Assistant）利用 AI 理解并响应语音命令，使用户更容易与设备互动。

### 听起来很棒，对吧？那么为什么我们还需要 AI Agent 框架？

AI Agent 框架不仅仅是 AI 框架。它们旨在支持创建能够与用户、其他 Agent 和环境交互以实现特定目标的智能 Agent。这些 Agent 可以表现出自主行为、做出决策并适应变化的条件。以下是 AI Agent 框架所支持的一些关键功能：

- **Agent 协作与协调**：支持创建多个 AI Agent，能够协作、沟通并协调以解决复杂任务。
- **任务自动化与管理**：提供自动化多步骤工作流、任务分配和动态任务管理的机制。
- **上下文理解与适应**：使 Agent 具备理解上下文、适应变化的环境并基于实时信息做出决策的能力。

总结来说，Agent 让你可以做得更多，提升自动化水平，创建能够从环境中学习和适应的更智能的系统。

## 如何快速原型设计、迭代并提升 Agent 的能力？

这是一个快速发展的领域，但大多数 AI Agent 框架都具备一些共性，可以帮助你快速原型设计和迭代，主要包括模块化组件、协作工具和实时学习。让我们深入探讨这些内容：

- **使用模块化组件**：AI 框架提供预构建的组件，例如提示、解析器和内存管理。
- **利用协作工具**：为 Agent 设计特定的角色和任务，测试并优化协作工作流。
- **实时学习**：实现反馈循环，使 Agent 从交互中学习并动态调整行为。

### 使用模块化组件

像 LangChain 和 Microsoft Semantic Kernel 这样的框架提供了预构建的组件，例如提示、解析器和内存管理。

**团队如何使用这些组件**：团队可以快速组装这些组件，创建一个功能性原型，而无需从头开始，从而实现快速实验和迭代。

**实际工作原理**：你可以使用预构建的解析器从用户输入中提取信息、使用内存模块存储和检索数据，并使用提示生成器与用户交互，而无需从头构建这些组件。

**示例代码**：以下是一个使用预构建解析器从用户输入中提取信息的示例：

```python
from langchain import Parser

parser = Parser()
user_input = "Book a flight from New York to London on July 15th"

parsed_data = parser.parse(user_input)

print(parsed_data)
# Output: {'origin': 'New York', 'destination': 'London', 'date': 'July 15th'}
```

从这个示例中可以看出，你可以利用预构建的解析器从用户输入中提取关键信息，例如航班预订请求的出发地、目的地和日期。这种模块化方法使你可以专注于高层逻辑。

### 利用协作工具

像 CrewAI 和 Microsoft Autogen 这样的框架可以帮助创建能够协作的多个 Agent。

**团队如何使用这些工具**：团队可以为 Agent 设计特定的角色和任务，从而测试和优化协作工作流，提高整体系统效率。

**实际工作原理**：你可以创建一个 Agent 团队，其中每个 Agent 都有特定的功能，例如数据检索、分析或决策。这些 Agent 可以通过通信和信息共享来实现共同目标，例如回答用户查询或完成任务。

**示例代码（Autogen）**：

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

上述代码展示了如何创建一个任务，该任务涉及多个 Agent 协作分析数据。每个 Agent 执行特定功能，通过协调这些 Agent 来实现预期结果。通过为每个 Agent 分配专门的角色，可以提升任务效率和性能。

### 实时学习

高级框架提供了实时上下文理解和适应的能力。

**团队如何使用这些能力**：团队可以实现反馈循环，使 Agent 从交互中学习并动态调整行为，从而不断改进和优化功能。

**实际工作原理**：Agent 可以分析用户反馈、环境数据和任务结果，更新知识库、调整决策算法并随着时间的推移提升性能。这种迭代学习过程使 Agent 能够适应变化的条件和用户偏好，从而增强整体系统的有效性。

## Autogen、Semantic Kernel 和 Azure AI Agent Service 框架之间的差异是什么？

可以通过多种方式比较这些框架，但我们将从设计、功能和目标使用场景的角度来分析它们的主要区别：

### Autogen

由 Microsoft Research 的 AI Frontiers Lab 开发的开源框架，专注于事件驱动的分布式 *agentic* 应用，支持多个 LLM 和 SLM、工具以及高级多 Agent 设计模式。

Autogen 的核心理念是基于 Agent，这些 Agent 是可以感知环境、做出决策并采取行动以实现特定目标的自主实体。Agent 通过异步消息进行通信，使它们能够独立并行工作，从而增强系统的可扩展性和响应性。

Agent 基于 [Actor 模型](https://en.wikipedia.org/wiki/Actor_model)。根据 Wikipedia 的定义，Actor 是 _并发计算的基本构建块。Actor 在接收到消息时，可以：做出本地决策、创建更多 Actor、发送更多消息以及决定如何响应接收到的下一条消息_。

**使用场景**：自动化代码生成、数据分析任务，以及为规划和研究功能构建自定义 Agent。

Autogen 的一些核心概念包括：

- **Agent**：Agent 是一个软件实体，能够：
  - **通过消息通信**，这些消息可以是同步的或异步的。
  - **维护自己的状态**，状态可以通过接收到的消息进行修改。
  - **执行操作**，这些操作可能会修改 Agent 的状态并产生外部效果，例如更新消息日志、发送新消息、执行代码或进行 API 调用。

  以下是一个创建具有聊天功能的 Agent 的简短代码片段：

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAssistant(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```

    在上述代码中，`MyAssistant` has been created and inherits from `RoutedAgent`. It has a message handler that prints the content of the message and then sends a response using the `AssistantAgent` delegate. Especially note how we assign to `self._delegate` an instance of `AssistantAgent` 是一个预构建的 Agent，能够处理聊天完成任务。

  接下来，让 Autogen 知道这种 Agent 类型并启动程序：

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    在上述代码中，Agent 被注册到运行时，并向 Agent 发送了一条消息，产生如下输出：

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **多 Agent 支持**：Autogen 支持创建多个 Agent，它们可以协作以更高效地解决复杂任务。通过定义具有专门功能和角色的不同类型的 Agent，例如数据检索、分析、决策和用户交互，可以创建一个多 Agent 系统。以下是一个这样的创建示例：

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    上述代码中，我们有一个 `GroupChatManager`，它被注册到运行时。此管理器负责协调不同类型 Agent（如撰稿人、插画师、编辑和用户）之间的交互。

- **Agent 运行时**：框架提供了一个运行时环境，用于支持 Agent 之间的通信、管理其身份和生命周期，并执行安全和隐私边界。这意味着你可以在一个安全且受控的环境中运行 Agent，确保它们能够安全高效地交互。以下是两种运行时的介绍：
  - **独立运行时**：适用于单进程应用，其中所有 Agent 都用同一种编程语言实现并运行在同一进程中。以下是其工作原理的示意图：
  
    ![独立运行时](https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg)  
    应用栈

    *Agent 通过运行时通过消息进行通信，运行时管理 Agent 的生命周期。*

  - **分布式运行时**：适用于多进程应用，其中 Agent 可以用不同的编程语言实现并运行在不同的机器上。以下是其工作原理的示意图：
  
    ![分布式运行时](https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg)

### Semantic Kernel + Agent Framework

Semantic Kernel 包含两部分：Semantic Kernel Agent Framework 和 Semantic Kernel 本身。

先谈谈 Semantic Kernel 的核心概念：

- **连接**：与外部 AI 服务和数据源的接口。

    ```csharp
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    这里是一个简单的示例，展示了如何创建一个 Kernel 并添加一个聊天完成服务。Semantic Kernel 创建了一个与外部 AI 服务（此处为 Azure OpenAI Chat Completion）的连接。

- **插件**：封装了应用程序可以使用的功能。既有现成的插件，也可以创建自定义插件。这里还有一个“语义函数”的概念。之所以称为语义函数，是因为你提供了语义信息，帮助 Semantic Kernel 决定需要调用该函数。以下是一个示例：

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // Register the function
    kernel.CreateSemanticFunction(
        promptTemplate: skPrompt,
        functionName: "SummarizeText",
        pluginName: "SemanticFunctions"
    );
    ```

    在此示例中，你首先有一个模板提示 `skPrompt` that leaves room for the user to input text, `$userInput`. Then you register the function `SummarizeText` with the plugin `SemanticFunctions`。注意函数的名称，它帮助 Semantic Kernel 理解该函数的用途以及何时应该调用它。

- **本地函数**：框架还可以直接调用本地函数来执行任务。以下是一个检索文件内容的本地函数示例：

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";
    
    var nativeFunctions = new NativeFunctions();
    kernel.ImportFunctions(nativeFunctions, plugInName);
    ```

- **规划器**：规划器根据用户输入协调执行计划和策略。规划器的作用是表达任务的执行方式，然后作为 Semantic Kernel 的执行指令。它随后调用必要的函数来完成任务。以下是一个计划示例：

    ```csharp
    string planDefinition = "Read content from a local file and summarize the content.";
    SequentialPlanner sequentialPlanner = new SequentialPlanner(kernel);
    
    string assetsFolder = @"../../assets";
    string fileName = Path.Combine(assetsFolder,"docs","06_SemanticKernel", "aci_documentation.txt");
    
    ContextVariables contextVariables = new ContextVariables();
    contextVariables.Add("fileName", fileName);
    
    var customPlan = await sequentialPlanner.CreatePlanAsync(planDefinition);
    
    // Execute the plan
    KernelResult kernelResult = await kernel.RunAsync(contextVariables, customPlan);
    Console.WriteLine($"Summarization: {kernelResult.GetValue<string>()}");
    ```

    特别注意 `planDefinition` which is a simple instruction for the planner to follow. The appropriate functions are then called based on this plan, in this case our semantic function `SummarizeText` and the native function `RetrieveLocalFile`。
- **内存**：抽象并简化 AI 应用的上下文管理。内存的概念是 LLM 应该了解的信息。你可以将这些信息存储在向量存储中，最终可以是内存数据库、向量数据库或类似数据库。以下是一个非常简化的场景示例，其中将 *事实* 添加到内存中：

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

    这些事实随后存储在内存集合 `SummarizedAzureDocs` 中。这是一个非常简化的示例，但你可以看到如何将信息存储到内存中供 LLM 使用。

这就是 Semantic Kernel 框架的基础知识，那么它的 Agent Framework 是什么？

### Azure AI Agent Service

Azure AI Agent Service 是一个较新的补充，于 Microsoft Ignite 2024 上推出。它支持开发和部署更灵活的 AI Agent，例如直接调用开源 LLM（如 Llama 3、Mistral 和 Cohere）。

Azure AI Agent Service 提供更强的企业安全机制和数据存储方法，非常适合企业应用。

它可以与 Autogen 和 Semantic Kernel 等多 Agent 协作框架无缝协作。

该服务目前处于公测阶段，支持用 Python 和 C# 构建 Agent。

#### 核心概念

Azure AI Agent Service 的核心概念包括：

- **Agent**：Azure AI Agent Service 与 Azure AI Foundry 集成。在 AI Foundry 中，AI Agent 充当“智能”微服务，可以用于回答问题（RAG）、执行操作或完全自动化工作流。它通过结合生成式 AI 模型的能力与访问和交互真实数据源的工具实现这些目标。以下是一个 Agent 示例：

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    在此示例中，创建了一个模型为 `gpt-4o-mini`, a name `my-agent`, and instructions `You are helpful agent` 的 Agent。该 Agent 配备了工具和资源，用于执行代码解释任务。

- **线程和消息**：线程是另一个重要概念。它表示 Agent 和用户之间的对话或交互。线程可用于跟踪对话进度、存储上下文信息以及管理交互的状态。以下是一个线程示例：

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    在上述代码中，创建了一个线程。然后向线程发送了一条消息。通过调用 `create_and_process_run`，要求 Agent 在该线程上执行任务。最后，获取并记录消息以查看 Agent 的响应。这些消息表明用户与 Agent 之间对话的进展。还需要注意的是，消息可以是文本、图像或文件等不同类型，例如 Agent 的工作结果可能是图像或文本响应。作为开发者，你可以利用这些信息进一步处理响应或将其呈现给用户。

- **与其他 AI 框架集成**：Azure AI Agent Service 可以与其他框架（如 Autogen 和 Semantic Kernel）交互，这意味着你可以在这些框架之一中构建应用的一部分，并例如将 Agent Service 用作协调器，或者完全使用 Agent Service 构建应用。

**使用场景**：Azure AI Agent Service 专为需要安全、可扩展且灵活的 AI Agent 部署的企业应用设计。

## 这些框架之间的区别是什么？

虽然这些框架之间似乎有很多重叠，但在设计、功能和目标使用场景方面，它们仍然有一些关键区别：

- **Autogen**：专注于事件驱动的分布式 Agentic 应用，支持多个 LLM 和 SLM、工具以及高级多 Agent 设计模式。
- **Semantic Kernel**：专注于理解和生成类人文本内容，通过捕捉更深层次的语义意义来实现。它旨在自动化复杂的工作流并根据项目目标启动任务。
- **Azure AI Agent Service**：提供更灵活的模型，例如直接调用开源 LLM（如 Llama 3、Mistral 和 Cohere）。它提供更强的企业安全机制和数据存储方法，非常适合企业应用。

仍然不确定该选择哪个？

### 使用场景

让我们通过一些常见的使用场景来帮助你选择：

> **问**：我的团队正在开发一个项目，涉及自动化代码生成和数据分析任务。我们应该选择哪个框架？
>
> **答**：Autogen 是一个不错的选择，因为它专注于事件驱动的分布式 Agentic 应用，并支持高级多 Agent 设计模式。

> **问**：在这个使用场景中，Autogen 比 Semantic Kernel 和 Azure AI Agent Service 更好的原因是什么？
>
> **答**：Autogen 专为事件驱动的分布式 Agentic 应用设计，非常适合自动化代码生成和数据分析任务。它提供了必要的工具和功能，可以高效地构建复杂的多 Agent 系统。

> **问**：听起来 Azure AI Agent Service 也适合这个场景，它也有代码生成工具，对吗？
>
> **答**：是的，Azure AI Agent Service 也支持代码生成和数据分析任务，但它可能更适合需要安全、可扩展且灵活的 AI Agent 部署的企业应用。Autogen 更专注于事件驱动的分布式 Agentic 应用和高级多 Agent 设计模式。

> **问**：所以你的意思是，如果我想要企业级的解决方案，我应该选择 Azure AI Agent Service？
>
> **答**：是的，Azure AI Agent Service 专为需要安全、可扩展且灵活的 AI Agent 部署的企业应用设计。它提供更强的企业安全机制和数据存储方法，非常适合企业使用场景。

### 总结关键差异表格

| 框架                   | 重点                                     | 核心概念               | 使用场景                             |
| ---------------------- | ---------------------------------------- | ---------------------- | ------------------------------------ |
| Autogen                | 事件驱动型分布式代理应用程序             | 代理、角色、功能、数据 | 代码生成、数据分析任务               |
| Semantic Kernel        | 理解并生成类似人类的文本内容             | 代理、模块化组件、协作 | 自然语言理解、内容生成               |
| Azure AI Agent Service | 灵活的模型、企业安全、代码生成、工具调用 | 模块化、协作、流程编排 | 安全、可扩展且灵活的人工智能代理部署 |

这些框架各自的理想用例是什么？
- **AutoGen**：事件驱动型、分布式代理应用程序，高级多代理设计模式。适用于代码生成、数据分析任务的自动化。 
- **Semantic Kernel**：理解并生成类似人类的文本内容，自动化复杂的工作流程，根据项目目标启动任务。适用于自然语言理解、内容生成。
- **Azure AI Agent Service**：灵活的模型、企业级安全机制、数据存储方法。适用于在企业应用程序中安全、可扩展且灵活地部署 AI 代理。

## 我可以直接集成现有的 Azure 生态系统工具，还是需要独立的解决方案？  
答案是肯定的，您可以将现有的 Azure 生态系统工具直接与 Azure AI Agent Service 集成，尤其是因为它已被设计为能够与其他 Azure 服务无缝协作。例如，您可以集成 Bing、Azure AI Search 和 Azure Functions。此外，它还与 Azure AI Foundry 有深度集成。  

对于 Autogen 和 Semantic Kernel，您也可以与 Azure 服务集成，但可能需要从代码中调用 Azure 服务。另一种集成方式是使用 Azure SDK，通过您的代理与 Azure 服务交互。此外，如前所述，您可以使用 Azure AI Agent Service 作为在 Autogen 或 Semantic Kernel 中构建的代理的协调器，这将使您轻松访问 Azure 生态系统。  

## 参考  
- [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357)  
- [2] - [Semantic Kernel and Autogen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/)  
- [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp)  
- [4] - [Azure AI Agent service](https://learn.microsoft.com/azure/ai-services/agents/overview)  
- [5] - [Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution](https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121)  

**免责声明**:  
本文档使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文的母语版本为权威来源。对于关键信息，建议寻求专业人工翻译。因使用本翻译而引起的任何误解或误读，我们概不负责。