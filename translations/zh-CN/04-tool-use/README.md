[![如何设计优秀的 AI 代理](../../../translated_images/zh-CN/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(点击上方图片观看本课视频)_

# 工具使用设计模式

工具很有趣，因为它们使 AI 代理拥有更广泛的能力范围。代理不再仅限于执行有限的一组操作，通过添加工具，代理现在可以执行各种操作。在本章中，我们将介绍工具使用设计模式，该模式描述了 AI 代理如何使用特定工具来实现其目标。

## 简介

在本课中，我们希望回答以下问题：

- 什么是工具使用设计模式？
- 它适用于哪些用例？
- 实现该设计模式需要哪些元素/构建模块？
- 使用工具使用设计模式构建可信 AI 代理的特别注意事项有哪些？

## 学习目标

完成本课后，您将能够：

- 定义工具使用设计模式及其目的。
- 识别适用工具使用设计模式的用例。
- 了解实现设计模式所需的关键元素。
- 认识使用该设计模式确保 AI 代理可信度的考虑事项。

## 什么是工具使用设计模式？

**工具使用设计模式**侧重于赋予大型语言模型（LLM）与外部工具交互以实现特定目标的能力。工具是可以由代理执行的代码块，用于完成操作。工具可以是简单的函数，比如计算器，也可以是调用第三方服务的 API，例如股票价格查询或天气预报。在 AI 代理的上下文中，工具被设计为响应**模型生成的函数调用**由代理执行。

## 它适用于哪些用例？

AI 代理可以利用工具完成复杂任务、检索信息或做出决策。工具使用设计模式常用于需要与外部系统动态交互的场景，如数据库、Web 服务或代码解释器。此能力适用于多种用例，包括：

- **动态信息检索：**代理可查询外部 API 或数据库以获取最新数据（例如查询 SQLite 数据库进行数据分析，获取股价或天气信息）。
- **代码执行与解释：**代理可执行代码或脚本来解决数学问题、生成报告或进行模拟。
- **工作流自动化：**通过集成任务调度器、电子邮件服务或数据管道等工具，实现重复或多步骤工作流的自动化。
- **客户支持：**代理可与 CRM 系统、工单平台或知识库交互，以解决用户查询。
- **内容生成与编辑：**代理可利用语法检查器、文本摘要工具或内容安全评估器等工具协助内容创作任务。

## 实现工具使用设计模式所需的元素/构建模块有哪些？

这些构建模块使 AI 代理能够执行广泛任务。下面是实现工具使用设计模式的关键元素：

- **函数/工具模式定义**：包含可用工具的详细定义，包括函数名称、目的、所需参数和预期输出。这些模式让 LLM 理解有哪些工具可用以及如何构造有效请求。

- **函数执行逻辑**：管理何时以及如何根据用户意图和对话上下文调用工具。可能包括规划模块、路由机制或动态确定工具使用的条件流程。

- **消息处理系统**：管理用户输入、LLM 响应、工具调用及工具输出之间的对话流。

- **工具集成框架**：连接代理与各种工具的基础设施，无论是简单函数还是复杂的外部服务。

- **错误处理与验证**：处理工具执行失败、参数验证及意外响应的机制。

- **状态管理**：跟踪对话上下文、先前工具交互及持久数据，确保多轮交互的一致性。

接下来，我们将更详细地讲解函数/工具调用。

### 函数/工具调用

函数调用是使大型语言模型（LLM）与工具交互的主要方式。常会看到“函数”和“工具”交替使用，因为“函数”（可复用代码块）就是代理用来完成任务的“工具”。为了调用函数代码，LLM 必须将用户请求与函数描述进行匹配。为此，会向 LLM 发送包含所有可用函数描述的模式（schema）。LLM 会选择最适合该任务的函数，并返回其名称与参数。随后调用该函数，函数响应返回给 LLM，LLM 使用这些信息回应用户请求。

开发者实现代理的函数调用时需要：

1. 支持函数调用的 LLM 模型
2. 包含函数描述的模式（schema）
3. 描述的各函数代码

以获取某城市当前时间为例说明：

1. **初始化支持函数调用的 LLM：**

    并非所有模型都支持函数调用，因此需确认所用 LLM 支持。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支持函数调用。我们可以从初始化 Azure OpenAI 客户端开始。

    ```python
    # 初始化 Azure OpenAI 客户端
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **创建函数模式：**

    接下来定义包含函数名称、功能描述及函数参数名称和描述的 JSON 模式。
    然后将此模式与用户请求（例如查询旧金山时间）一起传给先前建立的客户端。需要注意的是，返回的结果是**工具调用**，而**非**问题的最终答案。如前所述，LLM 返回它为任务选择的函数名称及将传递的参数。

    ```python
    # 供模型读取的功能描述
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
  
    # 第一次API调用：请求模型使用函数
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # 处理模型的回复
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **完成任务所需的函数代码：**

    既然 LLM 已选择执行哪个函数，就需要实现该函数的代码并执行。
    我们可以用 Python 实现获取当前时间的代码。还需编写从 response_message 中提取函数名称和参数以获取最终结果的代码。

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

函数调用是大多数（如果不是全部）代理工具使用设计的核心，但从零实现有时存在挑战。
正如我们在[第 2 课](../../../02-explore-agentic-frameworks)中了解到的，代理框架为我们提供了预构建的构建模块，以实现工具使用。

## 使用代理框架的工具使用示例

以下是使用不同代理框架实现工具使用设计模式的一些示例：

### 语义内核（Semantic Kernel）

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> 是一个开源 AI 框架，面向 .NET、Python 和 Java 开发者，用于处理大型语言模型（LLM）。它通过一种称为<a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">序列化</a>的过程，自动向模型描述函数及其参数，从而简化函数调用。此外它还处理模型与代码间的往返通信。使用如 Semantic Kernel 这样的代理框架的另一个优势是，可以访问预构建工具，如<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">文件搜索</a>和<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">代码解释器</a>。

下图展示了使用 Semantic Kernel 进行函数调用的流程：

![function calling](../../../translated_images/zh-CN/functioncalling-diagram.a84006fc287f6014.webp)

在 Semantic Kernel 中，函数/工具被称为<a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">插件</a>。我们可以将之前的 `get_current_time` 函数通过封装为带函数的类转换成插件。还可导入 `kernel_function` 装饰器，传入函数描述。当用 GetCurrentTimePlugin 创建内核时，内核会自动序列化函数及其参数，创建发送给 LLM 的模式。

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# 创建内核
kernel = Kernel()

# 创建插件
get_current_time_plugin = GetCurrentTimePlugin(location)

# 将插件添加到内核
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI 代理服务

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI 代理服务</a> 是一个较新的代理框架，旨在帮助开发者安全构建、部署和扩展高质量且可扩展的 AI 代理，无需管理底层计算和存储资源。该服务对企业应用尤为有用，因为它是一个完全托管的服务，具备企业级安全。

与直接使用 LLM API 开发相比，Azure AI 代理服务的优势包括：

- 自动工具调用——无需解析工具调用、调用工具及处理响应；所有操作均在服务器端完成
- 数据安全管理——无需自行管理对话状态，可依赖线程存储全部所需信息
- 即用型工具——提供多种工具以与数据源交互，如 Bing、Azure AI 搜索和 Azure Functions。

Azure AI 代理服务中的工具分为两类：

1. 知识工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">基于 Bing 搜索的基础支持</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">文件搜索</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 搜索</a>

2. 行动工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函数调用</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">代码解释器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 定义工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

代理服务使我们能够将这些工具作为一个 `toolset` 一起使用。它还利用了`threads`，用于跟踪特定对话的消息历史。

假设你是 Contoso 公司的销售代理，想开发一个可以回答关于销售数据问题的对话代理。

下图演示了如何使用 Azure AI 代理服务分析销售数据：

![Agentic Service In Action](../../../translated_images/zh-CN/agent-service-in-action.34fb465c9a84659e.webp)

要使用服务中的任一工具，我们可以创建客户端并定义工具或工具集。以下 Python 代码演示了该实现。LLM 会查看工具集，并根据用户请求决定使用用户创建的函数 `fetch_sales_data_using_sqlite_query` 还是预构建的代码解释器。

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query 函数，位于 fetch_sales_data_functions.py 文件中。
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

## 使用工具使用设计模式构建可信 AI 代理的特别注意事项有哪些？

LLM 动态生成的 SQL 最常见的担忧是安全性，特别是 SQL 注入或恶意操作（如删除或篡改数据库）的风险。尽管这些担忧是合理的，但通过正确配置数据库访问权限可以有效缓解。对于大多数数据库，需将数据库配置为只读。在 PostgreSQL 或 Azure SQL 等数据库服务中，应用应被分配只读（SELECT）角色。
在安全环境中运行应用程序可以进一步增强保护。在企业场景中，数据通常从运营系统中提取并转换到一个只读数据库或数据仓库，且采用用户友好的架构。这种方法确保数据安全、性能和可访问性得到优化，并且应用程序具有受限的只读访问权限。

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Got More Questions about the Tool Use Design Patterns?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso 创意写作多代理研讨会</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel 函数调用教程</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel 代码解释器</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen 工具</a>

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文档由AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)翻译完成。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。请以文档的原始语言版本为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译版本所产生的任何误解或误释，我们不承担任何责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->