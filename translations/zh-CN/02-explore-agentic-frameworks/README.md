[![探索AI代理框架](../../../translated_images/zh-CN/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(点击上方图片观看本课视频)_

# 探索AI代理框架

AI代理框架是为简化AI代理的创建、部署和管理而设计的软件平台。这些框架为开发者提供了预构建的组件、抽象和工具，简化了复杂AI系统的开发过程。

这些框架通过为AI代理开发中常见的挑战提供标准化的方法，帮助开发者专注于应用的独特方面。它们提升了构建AI系统的可扩展性、可访问性和效率。

## 介绍

本课将涵盖：

- 什么是AI代理框架，它们能让开发者实现什么？
- 团队如何利用它们快速原型设计、迭代并提升代理能力？
- 微软创建的框架和工具（<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a>和<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>）有什么区别？
- 我能否直接集成现有Azure生态工具，还是必须使用独立解决方案？
- 什么是Microsoft Foundry Agent Service？它如何帮助我？

## 学习目标

本课的目标是帮助你理解：

- AI代理框架在AI开发中的作用。
- 如何利用AI代理框架构建智能代理。
- AI代理框架支持的关键能力。
- Microsoft Agent Framework与Microsoft Foundry Agent Service的区别。

## 什么是AI代理框架，它们能实现什么？

传统AI框架可以帮助你将AI集成到应用中，并提升应用的性能，具体体现在以下方面：

- <strong>个性化</strong>：AI可以分析用户行为和偏好，提供个性化推荐、内容和体验。
例如：Netflix等流媒体服务使用AI根据观看历史推荐电影和节目，提升用户参与度和满意度。
- <strong>自动化和效率</strong>：AI可以自动执行重复任务、简化工作流程，提高运营效率。
例如：客户服务应用利用AI驱动的聊天机器人处理常见咨询，缩短响应时间并让人工客服专注于更复杂问题。
- <strong>增强用户体验</strong>：AI通过语音识别、自然语言处理和预测文本等智能功能改善整体用户体验。
例如：Siri和Google Assistant等虚拟助手使用AI理解并响应语音命令，方便用户与设备交互。

### 听起来很不错，为什么我们还需要AI代理框架？

AI代理框架不仅仅是AI框架。它们旨在支持智能代理的创建，这些代理可以与用户、其他代理及环境互动以实现特定目标。这些代理能表现出自主行为，做出决策，并适应变化的条件。下面介绍AI代理框架支持的一些关键能力：

- <strong>代理协作与协调</strong>：支持创建多个AI代理，它们能够协同工作、交流和协调解决复杂任务。
- <strong>任务自动化和管理</strong>：提供自动化多步骤工作流、任务委派和动态任务管理的机制。
- <strong>上下文理解和适应</strong>：赋予代理理解上下文、适应变化环境且基于实时信息做决策的能力。

总结来说，代理让你能够做更多事情，将自动化提升到新高度，构建能够适应和学习其环境的更智能系统。

## 如何快速原型设计、迭代和提升代理能力？

这是一个快速发展的领域，但大多数AI代理框架都有一些共通点，可帮助你快速原型设计和迭代，主要包括模块化组件、协作工具和实时学习。让我们深入了解：

- <strong>使用模块化组件</strong>：AI SDK提供预构建组件，如AI和内存连接器、自然语言或代码插件调用功能、提示模板等。
- <strong>利用协作工具</strong>：设计具备特定角色和任务的代理，使它们能够测试和优化协作工作流。
- <strong>实时学习</strong>：实现反馈循环，代理从交互中学习并动态调整行为。

### 使用模块化组件

微软Agent Framework等SDK提供预构建组件，如AI连接器、工具定义和代理管理。

<strong>团队如何使用</strong>：团队可以快速组装这些组件创建功能性原型，无需从零开始构建，支持快速实验与迭代。

<strong>实际应用</strong>：你可以使用预构建的解析器提取用户输入中的信息，利用内存模块存储和检索数据，并使用提示生成器与用户交互，均不需从头搭建这些组件。

<strong>示例代码</strong>。来看一个示例，说明如何使用`FoundryChatClient`的Microsoft Agent Framework，使模型通过工具调用响应用户输入：

``` python
# 微软代理框架 Python 示例

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# 定义一个示例工具函数以预订旅行
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # 示例输出：您2025年1月1日飞往纽约的航班已成功预订。祝旅途愉快！✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

从该示例中你可以看到，如何利用预构建解析器提取用户输入中的关键信息，如航班预订请求的起点、终点和日期。这种模块化方法让你专注于高层逻辑。

### 利用协作工具

微软Agent Framework等框架便于创建多个可协同工作的代理。

<strong>团队如何使用</strong>：团队可以设计具备特定角色和任务的代理，测试和优化协同工作流，提高整体系统效率。

<strong>实际应用</strong>：你可以创建一个代理团队，每个代理专注于数据检索、分析或决策等特定功能。代理间可以通讯共享信息，实现共同目标，如回答用户查询或完成任务。

**示例代码（微软Agent Framework）**：

```python
# 使用 Microsoft Agent Framework 创建多个协作的代理

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# 数据检索代理
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# 数据分析代理
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# 顺序运行任务代理
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

该代码示例展示了如何创建涉及多个代理协作分析数据的任务。每个代理执行特定功能，任务通过协调代理完成预期结果。通过创建具备专职角色的代理，提升任务效率和性能。

### 实时学习

先进框架支持实时上下文理解与适应能力。

<strong>团队如何使用</strong>：团队可以实现反馈循环，让代理从交互中学习，动态调整行为，从而持续改进和完善能力。

<strong>实际应用</strong>：代理可分析用户反馈、环境数据及任务结果，不断更新知识库，调整决策算法，提高性能。该迭代学习流程使代理适应环境变化和用户偏好，增强整体系统效能。

## Microsoft Agent Framework与Microsoft Foundry Agent Service有什么区别？

这里有许多对比方式，下面重点介绍它们在设计、能力和目标用例上的关键差异：

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework提供了一个简化的SDK，通过`FoundryChatClient`构建AI代理。它支持利用Azure OpenAI模型的内置工具调用、对话管理和通过Azure身份实现企业级安全。

<strong>用例</strong>：构建具备工具使用、多步骤工作流及企业集成场景的生产级AI代理。

Microsoft Agent Framework的几个重要核心概念：

- **代理（Agents）**。代理通过`FoundryChatClient`创建，配置名称、指令和工具。代理可以：
  - <strong>处理用户消息</strong>，并使用Azure OpenAI模型生成响应。
  - <strong>根据对话上下文自动调用工具</strong>。
  - <strong>维护跨多次交互的会话状态</strong>。

  下面是创建代理的代码片段：

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **工具（Tools）**。框架支持以Python函数定义工具，代理可自动调用。工具在创建代理时注册：

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- <strong>多代理协调</strong>。可以创建多名专精不同领域的代理，并协调它们的工作：

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure身份集成**。框架使用`AzureCliCredential`（或`DefaultAzureCredential`）实现安全的无秘钥认证，免除直接管理API密钥的需求。

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service是微软在Ignite 2024上推出的较新服务。它支持更灵活的模型，如直接调用开源大语言模型（LLM）Llama 3、Mistral和Cohere，实现AI代理的开发和部署。

Microsoft Foundry Agent Service提供更强的企业安全机制和数据存储方案，适合企业级应用。

它可以无缝与Microsoft Agent Framework协作，共同构建和部署代理。

该服务目前处于公开预览阶段，支持Python和C#构建代理。

使用Microsoft Foundry Agent Service Python SDK，可以创建带有用户定义工具的代理：

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
        model="gpt-5-mini",
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

Microsoft Foundry Agent Service包括以下核心概念：

- **代理（Agent）**。Microsoft Foundry Agent Service集成于Microsoft Foundry。在Foundry中，AI代理作为“智能”微服务，用于回答问题（RAG）、执行操作或完全自动化工作流程。它通过结合生成式AI模型能力与访问和交互真实数据源的工具实现功能。下面是一个代理示例：

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    在该示例中，代理创建时使用模型`gpt-5-mini`，名称为`my-agent`，指令为`You are helpful agent`。该代理配备工具和资源以执行代码解读任务。

- **线程和消息（Thread and messages）**。线程是另一个重要概念。它代表代理与用户之间的对话或交互。线程用于跟踪对话进展，存储上下文信息及管理交互状态。示例代码如下：

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # 让代理在该线程上执行工作
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # 获取并记录所有消息以查看代理的响应
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    在上述代码中，创建了一个线程。随后向线程发送消息。调用`create_and_process_run`后，请求代理在该线程上执行工作。最后获取消息并记录日志，查看代理的响应。消息显示了用户和代理之间对话的进展。还需了解消息类型可能包括文本、图片或文件，即代理的工作成果可能是图片或文本响应。作为开发者，你可以利用这些信息进一步处理响应或呈现给用户。

- **与Microsoft Agent Framework集成**。Microsoft Foundry Agent Service与Microsoft Agent Framework无缝协作，意味着你可以使用`FoundryChatClient`构建代理，并通过Agent Service进行生产环境部署。

<strong>用例</strong>：Microsoft Foundry Agent Service设计用于需要安全、可扩展和灵活AI代理部署的企业应用。

## 这些方法有何区别？
 
看起来确实有重叠，但在设计、能力和目标用例上存在关键区别：
 
- **Microsoft Agent Framework (MAF)**：是构建AI代理的生产级SDK，提供简洁API，支持工具调用、会话管理和Azure身份集成。
- **Microsoft Foundry Agent Service**：是微软Foundry中的代理平台和部署服务，内建对Azure OpenAI、Azure AI搜索、Bing搜索和代码执行的连接。
 
仍然不确定选择哪个？

### 用例
 
让我们通过一些常见用例帮你理清：
 
> 问：我想快速开始构建生产级AI代理应用
>

>答：Microsoft Agent Framework是不错的选择。它通过`FoundryChatClient`提供了简单的Python风格API，仅需几行代码即可定义带工具和指令的代理。

>问：我需要具备Azure搜索和代码执行等集成的企业级部署
>
> 答：Microsoft Foundry Agent Service最合适。该服务平台支持多种模型，集成Azure AI搜索、Bing搜索和Azure功能，实现支持Foundry Portal中构建代理并大规模部署。
 
> 问：我还是有点糊涂，给我一个推荐
>
> 答：先用Microsoft Agent Framework构建代理，当需要生产环境部署和扩展时，再使用Microsoft Foundry Agent Service。此方法既能快速迭代代理逻辑，也提供清晰的企业部署路径。
 
让我们用表格总结主要差异：

| 框架 | 重点 | 核心概念 | 用例 |
| --- | --- | --- | --- |
| Microsoft Agent Framework | 简化的代理SDK，支持工具调用 | 代理、工具、Azure身份 | 构建AI代理、工具使用、多步骤工作流 |
| Microsoft Foundry Agent Service | 灵活模型，企业安全，代码生成，工具调用 | 模块化、协作、流程编排 | 安全、可扩展且灵活的AI代理部署 |

## 我能否直接集成现有Azure生态工具，还是必须使用独立解决方案？


答案是肯定的，您可以将现有的 Azure 生态系统工具直接集成到 Microsoft Foundry Agent Service，特别是因为它已被设计为与其他 Azure 服务无缝协作。例如，您可以集成 Bing、Azure AI Search 和 Azure Functions。Microsoft Foundry 也有深度集成。

Microsoft Agent Framework 还通过 `FoundryChatClient` 和 Azure 身份集成了 Azure 服务，允许您直接从代理工具调用 Azure 服务。

## 示例代码

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## 关于 AI Agent Frameworks 有更多问题吗？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，与其他学习者交流，参加办公时间并获得您的 AI Agents 问题的解答。

## 参考资料

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## 上一课

[AI Agents 介绍及代理用例](../01-intro-to-ai-agents/README.md)

## 下一课

[理解 Agentic 设计模式](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->