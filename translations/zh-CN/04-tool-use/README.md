[![如何设计优秀的 AI 代理](../../../translated_images/zh-CN/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(点击上方图片观看本课的视频)_

# 工具使用设计模式

工具很有趣，因为它们允许 AI 代理具备更广泛的能力。代理不是只有一组有限的行动，而是通过添加工具，代理现在可以执行更广泛的动作。本章将介绍工具使用设计模式，描述 AI 代理如何使用特定工具来实现它们的目标。

## 介绍

在本课中，我们将解答以下问题：

- 什么是工具使用设计模式？
- 它可以应用于哪些用例？
- 实现该设计模式需要哪些元素/构建模块？
- 使用工具使用设计模式构建可信任的 AI 代理有哪些特别的注意事项？

## 学习目标

完成本课后，您将能够：

- 定义工具使用设计模式及其目的。
- 识别适用工具使用设计模式的用例。
- 了解实现该设计模式所需的关键元素。
- 认识使用该设计模式构建 AI 代理时确保可信性的考虑事项。

## 什么是工具使用设计模式？

**工具使用设计模式**聚焦于赋予大型语言模型（LLM）与外部工具交互以实现特定目标的能力。工具是代理可执行的代码以完成动作。工具可以是简单的函数，例如计算器，或者是调用第三方服务的 API，如股票价格查询或天气预报。在 AI 代理的上下文中，工具被设计为响应**模型生成的函数调用**由代理执行。

## 它可以应用于哪些用例？

AI 代理可以利用工具完成复杂任务、检索信息或做出决策。工具使用设计模式常用于需要动态与外部系统交互的场景，如数据库、网页服务或代码解释器。它适用于多种不同的用例，包括：

- **动态信息检索：** 代理可以查询外部 API 或数据库以获取最新数据（例如，查询 SQLite 数据库进行数据分析，获取股票价格或天气信息）。
- **代码执行和解释：** 代理可以执行代码或脚本解决数学问题、生成报告或进行模拟。
- **工作流程自动化：** 通过集成任务调度器、电子邮件服务或数据管道等工具自动化重复或多步骤的工作流程。
- **客户支持：** 代理可以与 CRM 系统、工单平台或知识库交互以解决用户查询。
- **内容生成与编辑：** 代理可利用语法检查器、文本摘要器或内容安全评估工具协助内容创作任务。

## 实现工具使用设计模式需要哪些元素/构建模块？

这些构建模块允许 AI 代理执行广泛的任务。以下是实现工具使用设计模式所需的关键元素：

- **函数/工具 schema**：详细定义可用工具，包括函数名称、用途、所需参数和预期输出。这些 schema 使 LLM 理解可用工具及如何构造有效请求。

- **函数执行逻辑**：根据用户意图和对话上下文控制何时及如何调用工具。这可能包括规划模块、路由机制或决定工具动态使用的条件流程。

- **消息处理系统**：管理用户输入、LLM 响应、工具调用以及工具输出之间的对话流程的组件。

- **工具集成框架**：连接代理与各种工具的基础设施，无论是简单函数还是复杂的外部服务。

- **错误处理与验证**：处理工具执行失败、参数验证和应对意外响应的机制。

- **状态管理**：跟踪对话上下文、先前的工具交互和持久数据，确保多轮交互的一致性。

接下来，我们将详细介绍函数/工具调用。

### 函数/工具调用

函数调用是使大型语言模型（LLM）与工具交互的主要方式。通常会看到“函数”和“工具”这两个词可以互换使用，因为“函数”（可重用代码块）是代理用来完成任务的“工具”。为了调用函数的代码，LLM 必须根据用户请求与函数描述进行比对。为此，会将包含所有可用函数描述的 schema 发送给 LLM。然后，LLM 选择最适合任务的函数，返回其名称和参数。被选函数则被调用，其响应发送回 LLM，LLM 使用这些信息来回复用户请求。

开发者实现代理函数调用时，需要：

1. 支持函数调用的 LLM 模型
2. 包含函数描述的 schema
3. 每个函数对应的代码

使用获取某个城市当前时间的例子来说明：

1. **初始化支持函数调用的 LLM：**

    并非所有模型均支持函数调用，因此需要确认你使用的 LLM 支持。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支持函数调用。我们可以先初始化 Azure OpenAI 客户端。

    ```python
    # 初始化 Azure OpenAI 客户端
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **创建函数 schema**：

    接下来定义一个 JSON schema，包含函数名称、函数作用描述、函数参数的名称和描述。
    然后，将该 schema 与用户关于查询旧金山时间的请求一起传递给之前创建的客户端。需要注意的是，返回的是**工具调用**，不是问题的最终答案。如前所述，LLM 返回选中的函数名称及将传递给它的参数。

    ```python
    # 供模型读取的函数描述
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
  
    # 第一次API调用：请求模型使用该功能
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
  
1. **执行任务所需的函数代码**：

    既然 LLM 已选出需要运行的函数，就必须实现并执行该函数的代码。
    我们可以用 Python 实现获取当前时间的代码。还需编写从 response_message 中提取名称和参数代码以获得最终结果。

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
  
      # 第二次API调用：从模型获取最终响应
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

函数调用是几乎所有代理工具使用设计的核心，但从零开始实现有时会比较困难。
正如在[第2课](../../../02-explore-agentic-frameworks)中所学，代理框架为我们提供了预构建的构件来实现工具使用。

## 使用代理框架的工具使用示例

以下是使用不同代理框架实现工具使用设计模式的一些示例：

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> 是一个开源的 AI 代理构建框架。它简化了函数调用的使用过程，允许你通过 `@tool` 装饰器定义 Python 函数作为工具。框架会处理模型与代码之间的来回通讯。它还通过 `AzureAIProjectAgentProvider` 提供了预构建工具，如文件搜索和代码解释器。

下图说明了在 Microsoft Agent Framework 中函数调用的流程：

![函数调用](../../../translated_images/zh-CN/functioncalling-diagram.a84006fc287f6014.webp)

在 Microsoft Agent Framework 中，工具定义为被装饰的函数。我们可以用 `@tool` 装饰器将之前看到的 `get_current_time` 函数转换成工具。框架会自动序列化函数及其参数，创建发送给 LLM 的 schema。

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

# 创建代理并使用该工具运行
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> 是较新的代理框架，旨在帮助开发者安全构建、部署和扩展高质量且可扩展的 AI 代理，无需管理底层计算和存储资源。它对企业应用尤为有用，因为它是完全托管的服务，提供企业级安全性。

与直接使用 LLM API 开发相比，Azure AI Agent Service 提供若干优势，包括：

- 自动工具调用 —— 无需自己解析工具调用、调用工具和处理响应；这些在服务器端自动完成
- 安全管理数据 —— 不需自行管理对话状态，可依赖线程存储所需所有信息
- 开箱即用工具 —— 可用以交互数据源的工具，如 Bing、Azure AI 搜索和 Azure Functions。

Azure AI Agent Service 中可用工具分为两类：

1. 知识类工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">基于 Bing 搜索的事实依据</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">文件搜索</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 搜索</a>

2. 操作类工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函数调用</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">代码解释器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 定义工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service 使我们可以将这些工具作为一个 `toolset` 一起使用。它还利用 `threads` 跟踪特定会话的消息历史。

假设你是 Contoso 公司的一名销售代理，想开发一个对销售数据提问的对话型代理。

下图展示了如何使用 Azure AI Agent Service 来分析销售数据：

![代理服务实况](../../../translated_images/zh-CN/agent-service-in-action.34fb465c9a84659e.webp)

要使用服务中的任何这些工具，可以创建客户端并定义工具或工具集。以下 Python 代码展示了具体实现。LLM 能根据用户请求查看工具集，决定调用用户自定义函数 `fetch_sales_data_using_sqlite_query`，还是预构建的代码解释器。

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
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用设计模式构建可信 AI 代理的特别注意事项？

LLM 动态生成的 SQL 常见的担忧是安全性，特别是 SQL 注入或恶意操作风险，如删除或篡改数据库。尽管这些问题存在，但通过合理配置数据库访问权限可以有效缓解。对大多数数据库而言，可配置为只读。对 PostgreSQL 或 Azure SQL 等数据库服务，应用应分配只读（SELECT）角色。

将应用运行在安全环境中进一步加强保护。在企业场景下，数据通常从业务系统抽取并转换到具有用户友好 schema 的只读数据库或数据仓库。这样做确保数据安全，性能和可访问性优化，同时应用拥有受限只读权限。

## 代码示例

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## 关于工具使用设计模式有更多问题？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，与其他学习者交流，参加答疑时段，获取 AI 代理相关问题的解答。

## 其他资源

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents 服务工作坊</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso 创意写作多代理工作坊</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework 概述</a>

## 之前的课

[理解代理设计模式](../03-agentic-design-patterns/README.md)

## 下一课
[智能代理检索增强生成（Agentic RAG）](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由人工智能翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。请以原始语言版本的文件作为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用本翻译而引起的任何误解或错误解释承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->