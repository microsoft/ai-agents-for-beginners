[![探索 AI 代理框架](../../../translated_images/zh-CN/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(点击上方图片以查看本课视频)_

# 探索 AI 代理框架

AI 代理框架是旨在简化 AI 代理的创建、部署和管理的软件平台。这些框架为开发者提供预构建的组件、抽象和工具，从而简化构建复杂 AI 系统的过程。

这些框架通过为 AI 代理开发中常见的挑战提供标准化方法，帮助开发者专注于应用的独特方面。它们增强了构建 AI 系统时的可扩展性、可访问性和效率。

## 介绍 

本课将涵盖：

- 什么是 AI 代理框架，以及它们使开发者能够实现什么？
- 团队如何使用这些框架快速原型、迭代并改进代理的能力？
- 由 Microsoft 创建的框架和工具（<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI 代理服务</a> 和 <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent 框架</a>）之间有什么区别？
- 我能否直接集成我现有的 Azure 生态系统工具，还是需要独立的解决方案？
- 什么是 Azure AI 代理服务，它如何帮助我？

## 学习目标

本课的目标是帮助你理解：

- AI 代理框架在 AI 开发中的作用。
- 如何利用 AI 代理框架构建智能代理。
- AI 代理框架所支持的关键能力。
- Microsoft Agent 框架与 Azure AI 代理服务之间的差异。

## 什么是 AI 代理框架，它们使开发者能够做什么？

传统的 AI 框架可以帮助你将 AI 集成到应用中，并在以下方面提升这些应用：

- **个性化**：AI 可以分析用户行为和偏好，提供个性化的推荐、内容和体验。
示例：像 Netflix 这样的流媒体服务使用 AI 根据观看历史推荐电影和节目，提升用户参与度和满意度。
- **自动化与效率**：AI 可以自动化重复性任务、简化工作流并提高运营效率。
示例：客户服务应用使用 AI 驱动的聊天机器人处理常见咨询，缩短响应时间，并让人工客服处理更复杂的问题。
- **增强的用户体验**：AI 可以通过提供语音识别、自然语言处理和预测文本等智能功能来改善整体用户体验。
示例：像 Siri 和 Google Assistant 这样的虚拟助手使用 AI 理解并回应语音指令，使用户更容易与设备交互。

### 这听起来很棒，那为什么我们还需要 AI 代理框架？

AI 代理框架不仅仅是普通的 AI 框架。它们旨在支持创建能够与用户、其他代理和环境交互以实现特定目标的智能代理。这些代理可以表现出自主行为、做出决策并适应变化的条件。下面来看一些 AI 代理框架支持的关键能力：

- **代理协作与协调**：支持创建多个 AI 代理彼此协作、通信和协调以解决复杂任务。
- **任务自动化与管理**：提供用于自动化多步骤工作流、任务委派和代理间动态任务管理的机制。
- **上下文理解与适应**：为代理提供理解上下文、适应变化环境并根据实时信息做出决策的能力。

总之，代理让你能做更多事，将自动化提升到新的水平，创建能够从其环境中适应和学习的更智能系统。

## 如何快速原型、迭代并改进代理的能力？

这是一个变化迅速的领域，但大多数 AI 代理框架都有一些共通点，可以帮助你快速原型和迭代，主要包括模块化组件、协作工具和实时学习。让我们深入了解这些方面：

- **使用模块化组件**：AI SDK 提供预构建组件，如 AI 和 Memory 连接器、使用自然语言或代码插件进行的函数调用、提示模板等。
- **利用协作工具**：为代理设计特定角色和任务，使它们能够测试并改进协作工作流。
- **实时学习**：实现反馈回路，使代理从交互中学习并动态调整其行为。

### 使用模块化组件

像 Microsoft Agent 框架这样的 SDK 提供预构建组件，例如 AI 连接器、工具定义和代理管理。

**团队如何使用这些**：团队可以快速组合这些组件来创建功能性原型，而无需从头开始构建，从而实现快速实验和迭代。

**在实践中的工作方式**：你可以使用预构建的解析器从用户输入中提取信息，使用内存模块存储和检索数据，并使用提示生成器与用户交互，而无需从零开始构建这些组件。

**示例代码**。让我们看一个示例，展示如何使用 Microsoft Agent 框架和 `AzureAIProjectAgentProvider` 让模型通过工具调用来响应用户输入：

``` python
# 微软代理框架 Python 示例

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# 定义一个预订旅行的示例工具函数
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # 示例输出：您于2025年1月1日飞往纽约的航班已成功预订。祝您旅途愉快！✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

从此示例中你可以看到如何利用预构建的解析器从用户输入中提取关键信息，例如航班预订请求的出发地、目的地和日期。这种模块化方法让你可以专注于高层逻辑。

### 利用协作工具

像 Microsoft Agent 框架这样的框架便于创建可以协同工作的多个代理。

**团队如何使用这些**：团队可以为代理设计特定角色和任务，使其能够测试并改进协作工作流，从而提高整体系统效率。

**在实践中的工作方式**：你可以创建一个代理团队，每个代理具有专门的功能，例如数据检索、分析或决策。这些代理可以互相通信并共享信息，以实现共同目标，比如回答用户查询或完成任务。

**示例代码（Microsoft Agent 框架）**：

```python
# 使用微软代理框架创建多个协同工作的代理

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# 数据检索代理
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# 数据分析代理
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# 按顺序运行代理以完成任务
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

上面的代码演示了如何创建一个涉及多个代理协同分析数据的任务。每个代理执行特定功能，任务通过协调这些代理来实现期望的结果。通过创建具有专门角色的专用代理，可以提高任务效率和性能。

### 实时学习

高级框架提供实时上下文理解和适应的能力。

**团队如何使用这些**：团队可以实现反馈回路，使代理从交互中学习并动态调整其行为，从而持续改进和优化能力。

**在实践中的工作方式**：代理可以分析用户反馈、环境数据和任务结果，以更新其知识库、调整决策算法并随着时间提高性能。这种迭代学习过程使代理能够适应变化的条件和用户偏好，从而增强整体系统效果。

## Microsoft Agent 框架与 Azure AI 代理服务有什么区别？

有很多比较这些方法的方式，但让我们从设计、能力和目标用例方面来看一些关键差异：

## Microsoft Agent 框架 (MAF)

Microsoft Agent 框架提供了一个用于使用 `AzureAIProjectAgentProvider` 构建 AI 代理的简化 SDK。它使开发者能够创建利用 Azure OpenAI 模型的代理，具有内置的工具调用、会话管理以及通过 Azure 身份提供的企业级安全性。

**用例**：构建具备工具使用、多步骤工作流和企业集成场景的生产就绪 AI 代理。

以下是 Microsoft Agent 框架的一些重要核心概念：

- **代理**。代理通过 `AzureAIProjectAgentProvider` 创建，并配置名称、指令和工具。代理可以：
  - **处理用户消息** 并使用 Azure OpenAI 模型生成响应。
  - **根据对话上下文自动调用工具**。
  - **在多次交互中维护会话状态**。

  下面是一个显示如何创建代理的代码片段：

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **工具**。该框架支持将工具定义为代理可以自动调用的 Python 函数。工具在创建代理时注册：

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **多代理协调**。你可以创建具有不同专业化的多个代理并协调它们的工作：

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure 身份集成**。该框架使用 `AzureCliCredential`（或 `DefaultAzureCredential`）进行安全的无密钥认证，消除了直接管理 API 密钥的需要。

## Azure AI 代理服务

Azure AI 代理服务是较新的补充，于 Microsoft Ignite 2024 上推出。它允许使用更灵活的模型来开发和部署 AI 代理，例如直接调用开源的大型语言模型（LLM），如 Llama 3、Mistral 和 Cohere。

Azure AI 代理服务提供更强的企业安全机制和数据存储方法，使其适用于企业级应用。

它与用于构建和部署代理的 Microsoft Agent 框架开箱即用地协同工作。

该服务目前处于公开预览阶段，支持使用 Python 和 C# 构建代理。

使用 Azure AI 代理服务 Python SDK，我们可以创建一个带有用户定义工具的代理：

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# 定义工具函数
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### 核心概念

Azure AI 代理服务具有以下核心概念：

- **代理**。Azure AI 代理服务与 Microsoft Foundry 集成。在 AI Foundry 中，AI 代理充当可用于回答问题（RAG）、执行操作或完全自动化工作流的“智能”微服务。它通过将生成式 AI 模型的能力与允许其访问和交互真实数据源的工具相结合来实现这一点。下面是一个代理示例：

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    在此示例中，创建了一个使用模型 `gpt-4o-mini`、名称为 `my-agent`、指令为 `You are helpful agent` 的代理。该代理配备了用于执行代码解释任务的工具和资源。

- **线程和消息**。线程是另一个重要概念。它表示代理与用户之间的对话或交互。线程可用于跟踪对话进展、存储上下文信息并管理交互状态。下面是一个线程的示例：

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

    在前面的代码中，创建了一个线程。随后，向该线程发送了一条消息。通过调用 `create_and_process_run`，请求代理在该线程上执行工作。最后，消息被获取并记录以查看代理的响应。消息指示了用户与代理之间对话的进展。同样重要的是要理解，消息可以是不同类型，例如文本、图像或文件，例如代理的工作可能产生了图像或文本响应。作为开发者，你可以使用这些信息进一步处理响应或将其呈现给用户。

- **与 Microsoft Agent 框架集成**。Azure AI 代理服务可与 Microsoft Agent 框架无缝配合，这意味着你可以使用 `AzureAIProjectAgentProvider` 构建代理，并通过代理服务将它们部署到生产场景中。

**用例**：Azure AI 代理服务面向需要安全、可扩展且灵活的 AI 代理部署的企业应用。

## 这些方法之间的区别是什么？
 
听起来确实有重叠，但在设计、能力和目标用例方面存在一些关键差异：
 
- **Microsoft Agent 框架 (MAF)**：是一个用于构建 AI 代理的生产就绪 SDK。它提供了一个简化的 API，用于创建具有工具调用、会话管理和 Azure 身份集成的代理。
- **Azure AI 代理服务**：是在 Azure Foundry 中的一个平台和部署服务，适用于代理。它提供与 Azure OpenAI、Azure AI Search、Bing Search 和代码执行等服务的内置连接。
 
仍然不确定选择哪个？

### 用例
 
让我们通过一些常见用例来帮助你决策：
 
> Q: 我正在构建生产级 AI 代理应用，并希望快速入门
>

> A: Microsoft Agent 框架是一个很好的选择。它通过 `AzureAIProjectAgentProvider` 提供简单、Python 风格的 API，使你只需几行代码即可定义带有工具和指令的代理。

>Q: 我需要具有企业级部署并能与 Azure 集成（如 Search 和代码执行）
>
> A: Azure AI 代理服务更合适。它是一个平台服务，为多模型、Azure AI Search、Bing Search 和 Azure Functions 等提供内置能力。它使你能够在 Foundry 门户中轻松构建代理并进行规模化部署。
 
> Q: 我仍然很困惑，只想要一个选项
>
> A: 先从 Microsoft Agent 框架开始构建你的代理，然后在需要在生产中部署和扩展时使用 Azure AI 代理服务。这种方法让你可以快速迭代代理逻辑，同时有一条明确的企业部署路径。
 
让我们总结一下关键差异：

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent 框架 | 带工具调用的精简代理 SDK | 代理、工具、Azure 身份 | 构建 AI 代理、工具使用、多步骤工作流 |
| Azure AI 代理服务 | 灵活模型、企业安全、代码生成、工具调用 | 模块化、协作、流程编排 | 安全、可扩展且灵活的 AI 代理部署 |

## 我能否直接集成我现有的 Azure 生态系统工具，还是需要独立的解决方案？
答案是肯定的，您可以将现有的 Azure 生态系统工具直接与 Azure AI Agent Service 集成，特别是因为它已被构建为与其他 Azure 服务无缝协作。例如，您可以集成 Bing、Azure AI Search 和 Azure Functions。与 Microsoft Foundry 也有深度集成。

Microsoft Agent Framework 还通过 `AzureAIProjectAgentProvider` 和 Azure identity 与 Azure 服务集成，使您可以直接从代理工具调用 Azure 服务。

## 示例代码

- Python: [代理框架](./code_samples/02-python-agent-framework.ipynb)
- .NET: [代理框架](./code_samples/02-dotnet-agent-framework.md)

## 还有关于 AI 代理框架的问题吗？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 与其他学习者交流，参加答疑时间，并获得您关于 AI 代理的问题解答。

## 参考资料

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure 代理服务</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft 代理框架 - Azure OpenAI 响应</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI 代理服务</a>

## 上一课

[AI 代理及其用例简介](../01-intro-to-ai-agents/README.md)

## 下一课

[理解代理式设计模式](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免责声明：
本文件已使用 AI 翻译服务 Co-op Translator (https://github.com/Azure/co-op-translator) 进行翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原文（原始语言版本）应被视为权威来源。对于关键信息，建议采用专业人工翻译。因使用本翻译而导致的任何误解或误释，我们不承担任何责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->