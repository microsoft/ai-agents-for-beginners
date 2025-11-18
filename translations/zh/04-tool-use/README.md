<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T16:44:59+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "zh"
}
-->
[![如何设计优秀的AI代理](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.zh.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(点击上方图片观看本课视频)_

# 工具使用设计模式

工具的有趣之处在于，它们可以让AI代理具备更广泛的能力。通过添加工具，代理不再局限于一组有限的操作，而是可以执行多种多样的操作。在本章中，我们将探讨工具使用设计模式，该模式描述了AI代理如何使用特定工具来实现其目标。

## 简介

在本课中，我们将回答以下问题：

- 什么是工具使用设计模式？
- 它可以应用于哪些使用场景？
- 实现该设计模式需要哪些元素/构建模块？
- 使用工具使用设计模式构建可信赖的AI代理需要注意哪些特殊事项？

## 学习目标

完成本课后，您将能够：

- 定义工具使用设计模式及其目的。
- 识别适用工具使用设计模式的使用场景。
- 理解实现该设计模式所需的关键元素。
- 认识确保使用该设计模式的AI代理可信赖的注意事项。

## 什么是工具使用设计模式？

**工具使用设计模式**的核心是赋予LLM与外部工具交互的能力，以实现特定目标。工具是代理可以执行的代码，例如一个简单的函数（如计算器）或调用第三方服务的API（如股票价格查询或天气预报）。在AI代理的上下文中，工具被设计为由代理根据**模型生成的函数调用**来执行。

## 它可以应用于哪些使用场景？

AI代理可以利用工具完成复杂任务、检索信息或做出决策。工具使用设计模式通常用于需要与外部系统动态交互的场景，例如数据库、网络服务或代码解释器。这种能力适用于多种使用场景，包括：

- **动态信息检索**：代理可以查询外部API或数据库以获取最新数据（例如，查询SQLite数据库进行数据分析，获取股票价格或天气信息）。
- **代码执行与解释**：代理可以执行代码或脚本以解决数学问题、生成报告或进行模拟。
- **工作流自动化**：通过集成任务调度器、电子邮件服务或数据管道等工具，自动化重复或多步骤的工作流。
- **客户支持**：代理可以与CRM系统、工单平台或知识库交互以解决用户问题。
- **内容生成与编辑**：代理可以利用语法检查器、文本摘要工具或内容安全评估器等工具协助完成内容创作任务。

## 实现工具使用设计模式需要哪些元素/构建模块？

这些构建模块使AI代理能够执行广泛的任务。以下是实现工具使用设计模式所需的关键元素：

- **函数/工具模式**：对可用工具的详细定义，包括函数名称、用途、所需参数和预期输出。这些模式使LLM能够理解有哪些工具可用以及如何构造有效的请求。
- **函数执行逻辑**：管理工具的调用时机和方式，基于用户意图和对话上下文。这可能包括规划模块、路由机制或动态决定工具使用的条件流程。
- **消息处理系统**：管理用户输入、LLM响应、工具调用和工具输出之间的对话流程的组件。
- **工具集成框架**：连接代理与各种工具的基础设施，无论是简单的函数还是复杂的外部服务。
- **错误处理与验证**：处理工具执行中的失败，验证参数并管理意外响应的机制。
- **状态管理**：跟踪对话上下文、先前的工具交互和持久数据，以确保多轮交互的一致性。

接下来，我们将更详细地探讨函数/工具调用。

### 函数/工具调用

函数调用是使大型语言模型（LLM）与工具交互的主要方式。您会经常看到“函数”和“工具”交替使用，因为“函数”（可重用代码块）是代理用来完成任务的“工具”。为了调用函数的代码，LLM需要将用户请求与函数描述进行比较。为此，会向LLM发送包含所有可用函数描述的模式。LLM随后选择最适合任务的函数，并返回其名称和参数。选定的函数被调用，其响应被发送回LLM，LLM利用这些信息回应用户请求。

开发者要为代理实现函数调用，需要：

1. 支持函数调用的LLM模型
2. 包含函数描述的模式
3. 每个描述函数的代码

以下是一个获取城市当前时间的示例：

1. **初始化支持函数调用的LLM：**

    并非所有模型都支持函数调用，因此需要确认所使用的LLM是否支持。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a>支持函数调用。我们可以通过初始化Azure OpenAI客户端开始。

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **创建函数模式**：

    接下来，我们将定义一个包含函数名称、函数用途描述以及函数参数名称和描述的JSON模式。然后将此模式与用户请求（例如查找旧金山的时间）一起传递给之前创建的客户端。需要注意的是，返回的是一个**工具调用**，而**不是**问题的最终答案。如前所述，LLM返回的是为任务选择的函数名称以及将传递给它的参数。

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
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

    现在LLM已经选择了需要运行的函数，接下来需要实现并执行完成任务的代码。我们可以用Python实现获取当前时间的代码，同时需要编写代码从response_message中提取函数名称和参数以获得最终结果。

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

函数调用是大多数代理工具使用设计的核心，但从头开始实现它有时可能具有挑战性。正如我们在[第2课](../../../02-explore-agentic-frameworks)中所学，代理框架为我们提供了实现工具使用的预构建模块。

## 使用代理框架的工具使用示例

以下是使用不同代理框架实现工具使用设计模式的一些示例：

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a>是一个开源的AI框架，适用于使用大型语言模型（LLM）的.NET、Python和Java开发者。它通过一种称为<a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">序列化</a>的过程，自动向模型描述您的函数及其参数，从而简化了函数调用的过程。它还处理模型与代码之间的往返通信。使用Semantic Kernel这样的代理框架的另一个优势是，它允许您访问预构建的工具，例如<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">文件搜索</a>和<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">代码解释器</a>。

下图展示了使用Semantic Kernel进行函数调用的过程：

![函数调用](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.zh.png)

在Semantic Kernel中，函数/工具被称为<a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">插件</a>。我们可以将之前看到的`get_current_time`函数转换为一个插件，将其变成一个包含该函数的类。我们还可以导入`kernel_function`装饰器，该装饰器接收函数的描述。当您使用GetCurrentTimePlugin创建一个内核时，内核会自动序列化函数及其参数，在此过程中创建发送给LLM的模式。

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

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>是一个较新的代理框架，旨在帮助开发者安全地构建、部署和扩展高质量、可扩展的AI代理，而无需管理底层计算和存储资源。它特别适用于企业应用，因为它是一个具有企业级安全性的完全托管服务。

与直接使用LLM API开发相比，Azure AI Agent Service提供了一些优势，包括：

- 自动工具调用——无需解析工具调用、调用工具和处理响应；所有这些都在服务器端完成。
- 安全管理数据——无需管理自己的对话状态，可以依赖线程存储所需的所有信息。
- 开箱即用的工具——可以用来与数据源交互的工具，例如Bing、Azure AI Search和Azure Functions。

Azure AI Agent Service中的工具分为两类：

1. 知识工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing搜索基础</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">文件搜索</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI搜索</a>

2. 操作工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函数调用</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">代码解释器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI定义的工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service允许我们将这些工具组合为一个`工具集`。它还利用`线程`来跟踪特定对话的消息历史。

假设您是Contoso公司的一名销售代理，想要开发一个可以回答关于销售数据问题的对话代理。

下图展示了如何使用Azure AI Agent Service分析销售数据：

![代理服务运行示例](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.zh.jpg)

要使用服务中的任何工具，我们可以创建一个客户端并定义一个工具或工具集。实际实现时，我们可以使用以下Python代码。LLM将能够查看工具集，并根据用户请求决定是使用用户创建的函数`fetch_sales_data_using_sqlite_query`，还是使用预构建的代码解释器。

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用设计模式构建可信赖AI代理需要注意哪些特殊事项？

LLM动态生成SQL时的一个常见担忧是安全性，特别是SQL注入或恶意操作（如删除或篡改数据库）的风险。虽然这些担忧是合理的，但可以通过正确配置数据库访问权限有效缓解。对于大多数数据库，这涉及将数据库配置为只读模式。对于像PostgreSQL或Azure SQL这样的数据库服务，应用程序应被分配只读（SELECT）角色。
在安全环境中运行应用程序可以进一步增强保护。在企业场景中，数据通常从操作系统中提取并转换为一个只读数据库或数据仓库，并采用用户友好的模式。这种方法确保了数据的安全性、性能优化和可访问性，同时应用程序仅具有受限的只读访问权限。

## 示例代码

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## 对工具使用设计模式有更多疑问？

加入 [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)，与其他学习者交流，参加办公时间，并解答您关于 AI Agents 的问题。

## 其他资源

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## 上一课

[理解代理设计模式](../03-agentic-design-patterns/README.md)

## 下一课

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用本翻译而引起的任何误解或误读不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->