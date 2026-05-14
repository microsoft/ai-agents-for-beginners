[![如何设计优秀的 AI 代理](../../../translated_images/zh-CN/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(点击上方图片观看本课视频)_

# 工具使用设计模式

工具之所以有趣，是因为它们允许 AI 代理具备更广泛的能力。代理不再局限于执行有限的一组动作，通过添加工具，代理现在可以执行更广泛的操作。本章将探讨工具使用设计模式，它描述了 AI 代理如何使用特定工具来实现其目标。

## 介绍

在本课中，我们将尝试回答以下问题：

- 什么是工具使用设计模式？
- 它可以应用于哪些用例？
- 实现该设计模式需要哪些元素/构建块？
- 使用工具使用设计模式构建值得信赖的 AI 代理有哪些特殊考虑？

## 学习目标

完成本课后，您将能够：

- 定义工具使用设计模式及其目的。
- 识别适用工具使用设计模式的用例。
- 理解实现该设计模式所需的关键元素。
- 识别使用该设计模式构建值得信赖的 AI 代理时的考虑事项。

## 什么是工具使用设计模式？

<strong>工具使用设计模式</strong>聚焦于赋予大型语言模型（LLM）与外部工具交互以实现特定目标的能力。工具是代理执行动作时可调用的代码。工具可以是简单的函数，比如计算器，或是对第三方服务（如股票价格查询或天气预报）的 API 调用。在 AI 代理的上下文中，工具被设计为响应 <strong>模型生成的函数调用</strong> 被代理执行。

## 它可以应用于哪些用例？

AI 代理可以利用工具完成复杂任务、检索信息或做出决策。工具使用设计模式常用于需要与外部系统动态交互的场景，例如数据库、网络服务或代码解释器。此能力适用于多种用例，包括：

- **动态信息检索：** 代理可查询外部 API 或数据库以获取最新数据（例如查询 SQLite 数据库进行数据分析，获取股票价格或天气信息）。
- **代码执行与解释：** 代理可执行代码或脚本解决数学问题，生成报告，或进行仿真。
- **工作流自动化：** 通过集成任务调度器、电子邮件服务或数据管道，实现重复或多步骤工作流自动化。
- **客户支持：** 代理可与 CRM 系统、工单平台或知识库交互以解决用户查询。
- **内容生成与编辑：** 代理可利用语法检查器、文本摘要器或内容安全评估工具协助内容创作任务。

## 实现工具使用设计模式所需的元素/构建块

这些构建块使 AI 代理能够执行丰富多样的任务。下面是实现工具使用设计模式的关键元素：

- **函数/工具模式（Schemas）**：可用工具的详细定义，包括函数名、用途、所需参数和预期输出。这些模式使 LLM 理解有哪些工具和如何构造有效请求。
- <strong>函数执行逻辑</strong>：管理何时以及如何根据用户意图和对话上下文调用工具。可能包括规划器模块、路由机制或动态确定工具使用的条件流程。
- <strong>消息处理系统</strong>：管理用户输入、LLM 响应、工具调用和工具输出之间对话流程的组件。
- <strong>工具集成框架</strong>：将代理连接到各种工具的基础设施，无论是简单函数还是复杂外部服务。
- <strong>错误处理与校验</strong>：处理工具执行失败、参数验证和意外响应的机制。
- <strong>状态管理</strong>：跟踪对话上下文、先前工具交互和持久数据，确保多轮交互的一致性。

接下来，我们详细看一下函数/工具调用。

### 函数/工具调用

函数调用是我们使大型语言模型（LLM）与工具交互的主要方式。你会发现“函数”和“工具”经常互用，因为“函数”（可复用的代码块）就是代理用来完成任务的“工具”。为了调用函数代码，LLM 需要根据用户请求与函数描述进行匹配。为此，会发送包含所有可用函数描述的模式给 LLM。LLM 然后选择最合适的函数，并返回函数名称和参数。所选函数被调用，其响应返回给 LLM，LLM 利用该信息回应用户请求。

开发者实现函数调用需要：

1. 支持函数调用的 LLM 模型
2. 包含函数描述的模式
3. 各函数的代码实现

以获取某城市当前时间的示例说明：

1. **初始化支持函数调用的 LLM：**

    并非所有模型都支持函数调用，需确认所用 LLM 支持。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支持函数调用。我们可以先初始化 Azure OpenAI 客户端。

    ```python
    # 初始化 Azure OpenAI 客户端
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```
  
1. **创建函数模式：**

    接着定义一个 JSON 模式，包含函数名、函数功能描述及参数名和描述。
    将此模式连同用户请求（如查询旧金山时间）一并传递给客户端。重要的是，返回的是一个 <strong>工具调用</strong>，<strong>而非问题的最终答案</strong>。正如前述，LLM 返回为任务选择的函数名称及参数。

    ```python
    # 给模型阅读的功能描述
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # 初始用户消息
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # 第一次API调用：请求模型使用该函数
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # 处理模型的响应
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **执行任务所需的函数代码：**

    既然 LLM 已选择待调用函数，需实现并执行完成任务的代码。
    我们用 Python 实现获取当前时间的代码。还需要编写代码从 response_message 中提取函数名和参数以得到最终结果。

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # 处理函数调用
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # 第二次API调用：获取模型的最终响应
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```
  
函数调用是大多数乃至所有代理工具使用设计的核心，但从零实现有时较为复杂。正如我们在[第二课](../../../02-explore-agentic-frameworks) 学到的，agentic 框架为我们提供了预构建的构建块来实现工具使用。

## 使用 Agentic 框架的工具使用示例

以下展示了如何使用不同的 agentic 框架实现工具使用设计模式：

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> 是一款开源 AI 框架，用于构建 AI 代理。它通过允许以 Python 函数并使用 `@tool` 装饰器定义工具，简化了函数调用过程。框架处理模型与代码之间的通信。它还通过 `AzureAIProjectAgentProvider` 提供访问文件搜索和代码解释器等预构建工具的能力。

下图展示了 Microsoft Agent Framework 中函数调用的流程：

![function calling](../../../translated_images/zh-CN/functioncalling-diagram.a84006fc287f6014.webp)

在 Microsoft Agent Framework 中，工具定义为带装饰器的函数。我们可以使用 `@tool` 装饰器将前面示例中的 `get_current_time` 函数转换成工具。框架会自动序列化函数及其参数，创建要发送给 LLM 的模式。

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# 创建客户端
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# 创建一个代理并使用工具运行
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> 是一个较新的 agentic 框架，旨在帮助开发者安全地构建、部署和扩展高质量且可扩展的 AI 代理，无需管理底层计算和存储资源。它特别适用于企业应用，因其为全托管服务，具有企业级安全性。

与直接调用 LLM API 开发相比，Azure AI Agent Service 有以下优势：

- 自动工具调用 — 无需解析工具调用、执行工具及处理响应，这些均由服务端完成
- 安全管理数据 — 不用自行管理对话状态，可依赖线程存储所有所需信息
- 开箱即用工具 — 包括与数据源交互的工具，如 Bing、Azure AI 搜索和 Azure Functions

Azure AI Agent Service 中可用的工具分为两类：

1. 知识工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">基于 Bing 搜索的知识定位</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">文件搜索</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 搜索</a>

2. 行动工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函数调用</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">代码解释器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 定义工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

代理服务允许我们将这些工具作为 `toolset` 一起使用。它还使用 `threads`，用于跟踪特定对话的消息历史。

假设你是 Contoso 公司的一名销售代理，希望开发一个能够回答关于销售数据问题的对话代理。

下图演示了如何使用 Azure AI Agent Service 分析销售数据：

![Agentic Service In Action](../../../translated_images/zh-CN/agent-service-in-action.34fb465c9a84659e.webp)

要使用服务中的任何工具，我们可以创建客户端并定义工具或工具集。实际开发中可使用以下 Python 代码。LLM 能查看工具集，基于用户请求决定使用用户创建的函数 `fetch_sales_data_using_sqlite_query`，或使用预构建的代码解释器。

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query 函数，可以在 fetch_sales_data_functions.py 文件中找到。
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# 初始化工具集
toolset = ToolSet()

# 使用 fetch_sales_data_using_sqlite_query 函数初始化函数调用代理，并将其添加到工具集中
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# 初始化代码解释器工具并将其添加到工具集中。
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```
  
## 使用工具使用设计模式构建值得信赖 AI 代理的特殊考虑

LLM 动态生成的 SQL 语句常被关注安全问题，尤其是 SQL 注入或恶意操作风险，如删除或篡改数据库。虽然这些担忧存在，但通过合理配置数据库访问权限可以有效防范。多数据库通常可将数据库配置为只读。对于 PostgreSQL 或 Azure SQL 等数据库服务，应用应被分配只读（SELECT）角色。

在安全环境中运行应用进一步强化保护。企业场景中，数据通常从生产系统抽取并转换到只读数据库或数据仓库，采用便于使用的 schema。此方式确保数据安全、性能和可访问性优化，且应用仅拥有受限的只读权限。

## 示例代码

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## 关于工具使用设计模式还有更多问题？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 与其他学习者交流，参加答疑时段并获得您的 AI 代理相关问题解答。

## 额外资源

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service 研讨会</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso 创意写作多代理研讨会</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework 概述</a>

## 上一课

[理解 Agentic 设计模式](../03-agentic-design-patterns/README.md)

## 下一课
[主体能动型RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->