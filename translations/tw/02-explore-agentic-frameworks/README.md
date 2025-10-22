<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86b9c2b24da3b3e61711182ffa72601c",
  "translation_date": "2025-09-29T22:03:01+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "tw"
}
-->
[![探索 AI Agent 框架](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.tw.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(點擊上方圖片觀看本課程的影片)_

# 探索 AI Agent 框架

AI Agent 框架是專為簡化 AI Agent 的創建、部署和管理而設計的軟體平台。這些框架為開發者提供了預建的元件、抽象層和工具，從而加速複雜 AI 系統的開發。

這些框架透過提供標準化的方法來解決 AI Agent 開發中的常見挑戰，幫助開發者專注於應用程式的獨特方面。它們提升了 AI 系統的可擴展性、可訪問性和效率。

## 課程介紹

本課程將涵蓋：

- 什麼是 AI Agent 框架？它能幫助開發者實現什麼？
- 團隊如何利用這些框架快速原型設計、迭代並提升 Agent 的能力？
- 微軟的 <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>、<a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> 和 <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> 所創建的框架和工具有何不同？
- 我可以直接整合現有的 Azure 生態系統工具，還是需要獨立的解決方案？
- 什麼是 Azure AI Agents 服務？它如何幫助我？

## 學習目標

本課程的目標是幫助你了解：

- AI Agent 框架在 AI 開發中的角色。
- 如何利用 AI Agent 框架來構建智能 Agent。
- AI Agent 框架所啟用的關鍵功能。
- AutoGen、Semantic Kernel 和 Azure AI Agent Service 之間的差異。

## 什麼是 AI Agent 框架？它能幫助開發者實現什麼？

傳統的 AI 框架可以幫助你將 AI 整合到應用程式中，並使這些應用程式在以下方面更出色：

- **個性化**：AI 可以分析使用者行為和偏好，提供個性化的推薦、內容和體驗。
  範例：像 Netflix 這樣的串流服務使用 AI 根據觀看歷史推薦電影和節目，提升使用者的參與度和滿意度。
- **自動化和效率**：AI 可以自動化重複性任務、簡化工作流程並提高運營效率。
  範例：客戶服務應用程式使用 AI 驅動的聊天機器人處理常見詢問，縮短響應時間並釋放人類代理處理更複雜的問題。
- **提升使用者體驗**：AI 可以通過提供智能功能（如語音識別、自然語言處理和預測文本）改善整體使用者體驗。
  範例：像 Siri 和 Google Assistant 這樣的虛擬助手使用 AI 理解並響應語音指令，使使用者更容易與設備互動。

### 聽起來很棒對吧，那為什麼我們需要 AI Agent 框架？

AI Agent 框架不僅僅是 AI 框架，它們旨在創建能與使用者、其他 Agent 和環境互動以實現特定目標的智能 Agent。這些 Agent 可以表現出自主行為、做出決策並適應不斷變化的條件。以下是 AI Agent 框架所啟用的一些關鍵功能：

- **Agent 協作與協調**：支持創建多個 AI Agent，這些 Agent 可以共同工作、溝通並協調以解決複雜任務。
- **任務自動化與管理**：提供機制來自動化多步工作流程、任務分配以及 Agent 之間的動態任務管理。
- **上下文理解與適應**：使 Agent 能夠理解上下文、適應不斷變化的環境並根據實時信息做出決策。

總結來說，Agent 讓你能做得更多，將自動化提升到新的層次，創建能夠從環境中學習和適應的更智能系統。

## 如何快速原型設計、迭代並提升 Agent 的能力？

這是一個快速變化的領域，但大多數 AI Agent 框架都有一些共同點，可以幫助你快速原型設計和迭代，主要包括模組化元件、協作工具和實時學習。讓我們深入了解這些：

- **使用模組化元件**：AI SDK 提供預建元件，例如 AI 和記憶體連接器、使用自然語言或程式碼插件進行函數調用、提示模板等。
- **利用協作工具**：設計具有特定角色和任務的 Agent，測試並完善協作工作流程。
- **實時學習**：實施反饋迴路，使 Agent 從互動中學習並動態調整其行為。

### 使用模組化元件

像 Microsoft Semantic Kernel 和 LangChain 這樣的 SDK 提供預建元件，例如 AI 連接器、提示模板和記憶體管理。

**團隊如何使用這些**：團隊可以快速組裝這些元件以創建功能原型，而無需從零開始，從而進行快速實驗和迭代。

**實際運作方式**：你可以使用預建的解析器從使用者輸入中提取信息，使用記憶體模組存儲和檢索數據，並使用提示生成器與使用者互動，而無需從零開始構建這些元件。

**範例程式碼**。以下是如何使用 Semantic Kernel Python 和 .Net 的預建 AI 連接器進行自動函數調用以響應使用者輸入的範例：

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

從這個範例中可以看到如何利用預建的解析器從使用者輸入中提取關鍵信息，例如航班預訂請求的出發地、目的地和日期。這種模組化方法使你能專注於高層邏輯。

### 利用協作工具

像 CrewAI、Microsoft AutoGen 和 Semantic Kernel 這樣的框架促進了多個 Agent 的創建，這些 Agent 可以共同工作。

**團隊如何使用這些**：團隊可以設計具有特定角色和任務的 Agent，測試並完善協作工作流程，提升整體系統效率。

**實際運作方式**：你可以創建一個 Agent 團隊，其中每個 Agent 都有專門的功能，例如數據檢索、分析或決策。這些 Agent 可以溝通並共享信息以實現共同目標，例如回答使用者查詢或完成任務。

**範例程式碼 (AutoGen)**：

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

在前面的程式碼中，你可以看到如何創建一個涉及多個 Agent 協作分析數據的任務。每個 Agent 執行特定功能，任務通過協調 Agent 來實現預期結果。通過創建具有專門角色的專用 Agent，可以提高任務效率和性能。

### 實時學習

高級框架提供了實時上下文理解和適應的能力。

**團隊如何使用這些**：團隊可以實施反饋迴路，使 Agent 從互動中學習並動態調整其行為，從而持續改進和完善能力。

**實際運作方式**：Agent 可以分析使用者反饋、環境數據和任務結果，更新其知識庫、調整決策算法並隨時間提高性能。這種迭代學習過程使 Agent 能夠適應不斷變化的條件和使用者偏好，提升整體系統效能。

## AutoGen、Semantic Kernel 和 Azure AI Agent Service 框架之間有何不同？

比較這些框架的方法有很多，但我們來看看它們在設計、功能和目標使用案例方面的一些主要差異：

## AutoGen

AutoGen 是由微軟研究院的 AI Frontiers Lab 開發的開源框架。它專注於事件驅動的分散式 *agentic* 應用程式，支持多個 LLMs 和 SLMs、工具以及高級多 Agent 設計模式。

AutoGen 的核心概念是 Agent，它是能夠感知環境、做出決策並採取行動以實現特定目標的自主實體。Agent 通過非同步消息進行通信，使其能夠獨立並並行工作，提升系統的可擴展性和響應能力。

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agent 基於 Actor 模型</a>。根據維基百科，Actor 是 _並行計算的基本構建塊。Actor 在接收到消息後可以：做出本地決策、創建更多 Actor、發送更多消息以及確定如何響應接收到的下一條消息_。

**使用案例**：自動化程式碼生成、數據分析任務以及為規劃和研究功能構建自定義 Agent。

以下是 AutoGen 的一些重要核心概念：

- **Agent**。Agent 是一個軟體實體：
  - **通過消息進行通信**，這些消息可以是同步或非同步的。
  - **維護自己的狀態**，該狀態可以由接收到的消息修改。
  - **執行動作**以響應接收到的消息或其狀態的變化。這些動作可能會修改 Agent 的狀態並產生外部效果，例如更新消息日誌、發送新消息、執行程式碼或進行 API 調用。
    
  以下是一段簡短的程式碼片段，展示如何創建具有聊天功能的 Agent：

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
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
    
    在前面的程式碼中，`MyAgent` 被創建並繼承自 `RoutedAgent`。它有一個消息處理器，該處理器打印消息的內容，然後使用 `AssistantAgent` 委託發送響應。特別注意如何將 `self._delegate` 分配給 `AssistantAgent` 的實例，這是一個預建的 Agent，可以處理聊天完成。

    接下來，讓 AutoGen 知道這個 Agent 類型並啟動程式：

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    在前面的程式碼中，Agent 被註冊到運行時，然後向 Agent 發送消息，結果如下：

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **多 Agent**。AutoGen 支持創建多個 Agent，這些 Agent 可以共同工作以完成複雜任務。Agent 可以通信、共享信息並協調其行動以更高效地解決問題。要創建多 Agent 系統，你可以定義具有專門功能和角色的不同類型的 Agent，例如數據檢索、分析、決策和使用者互動。以下是這樣的創建方式的範例：

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

    在前面的程式碼中，我們有一個 `GroupChatManager` 被註冊到運行時。這個管理器負責協調不同類型的 Agent（如作家、插畫師、編輯和使用者）之間的互動。

- **Agent 運行時**。框架提供了一個運行時環境，支持 Agent 之間的通信，管理它們的身份和生命週期，並強制執行安全和隱私邊界。這意味著你可以在安全和受控的環境中運行你的 Agent，確保它們能夠安全高效地互動。以下是兩種運行時的介紹：
  - **獨立運行時**。這是單進程應用程式的良好選擇，其中所有 Agent 都使用相同的程式語言實現並在同一進程中運行。以下是其工作方式的示意圖：
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">獨立運行時</a>   
應用程式堆疊

    *Agent 通過運行時通過消息進行通信，運行時管理 Agent 的生命週期*

  - **分散式 Agent 運行時**，適合多進程應用程式，其中 Agent 可以使用不同的程式語言實現並在不同的機器上運行。以下是其工作方式的示意圖：
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">分散式運行時</a>

## Semantic Kernel + Agent 框架

Semantic Kernel 是一個企業級 AI 編排 SDK。它由 AI 和記憶體連接器以及 Agent 框架組成。

首先介紹一些核心元件：

- **AI 連接器**：這是一個介面，用於與外部 AI 服務和數據源進行互動，支持 Python 和 C#。

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
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

    這裡是一個簡單的範例，展示如何創建 Kernel 並添加聊天完成服務。Semantic Kernel 創建了一個與外部 AI 服務的連接，在此例中是 Azure OpenAI Chat Completion。

- **插件**：這些封裝了應用程式可以使用的功能。既有現成的插件，也可以創建自定義插件。一個相關的概念是 "提示函數"。與提供自然語言提示進行函數調用不同，你可以向模型廣播某些函數。根據當前聊天上下文，模型可能選擇調用其中一個函數來完成請求或查詢。以下是一個範例：

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```

    這裡，你首先有一個模板提示 `skPrompt`，它為使用者輸入文本 `$userInput` 留出空間。然後你創建 Kernel 函數 `SummarizeText`，並將其導入到 Kernel 中，插件名稱為 `SemanticFunctions`。注意函數的名稱，它幫助 Semantic Kernel 理解函數的作用以及何時應該調用。

- **原生函數**：框架還可以直接調用原生函數來執行任務。以下是一個直接從文件中檢索內容的函數範例：

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

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```

- **記憶體**：抽象並簡化 AI 應用程式的上下文管理。記憶體的概念是 LLM 應該知道的內容。你可以將這些信息存儲在向量存儲中，最終成為內存數據庫或向量數據庫或類似的存儲。以下是一個非常簡化的範例，展示如何將 *事實* 添加到記憶體中：

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

這些事實會被存儲在記憶集合 `SummarizedAzureDocs` 中。這是一個非常簡化的例子，但您可以看到如何將資訊存儲在記憶中供 LLM 使用。

這就是 Semantic Kernel 框架的基本概念，那麼 Agent Framework 呢？

## Azure AI Agent Service

Azure AI Agent Service 是最近新增的功能，於 Microsoft Ignite 2024 推出。它允許使用更靈活的模型來開發和部署 AI 代理，例如直接調用開源 LLMs，如 Llama 3、Mistral 和 Cohere。

Azure AI Agent Service 提供更強大的企業安全機制和資料存儲方法，使其適合企業應用。

它可以直接與多代理協作框架（如 AutoGen 和 Semantic Kernel）配合使用。

此服務目前處於公開預覽階段，支持使用 Python 和 C# 來構建代理。

使用 Semantic Kernel Python，我們可以創建一個具有使用者定義插件的 Azure AI Agent：

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### 核心概念

Azure AI Agent Service 包含以下核心概念：

- **代理（Agent）**。Azure AI Agent Service 與 Azure AI Foundry 集成。在 AI Foundry 中，AI 代理充當一個「智能」微服務，可用於回答問題（RAG）、執行操作或完全自動化工作流程。它通過結合生成式 AI 模型的能力與工具來訪問和互動真實世界的資料來源。以下是一個代理的例子：

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    在此例子中，創建了一個代理，使用模型 `gpt-4o-mini`，名稱為 `my-agent`，指令為 `You are helpful agent`。該代理配備了工具和資源來執行代碼解釋任務。

- **線程和消息（Thread and messages）**。線程是另一個重要概念。它表示代理和使用者之間的對話或互動。線程可用於跟蹤對話進度、存儲上下文資訊以及管理互動的狀態。以下是一個線程的例子：

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

    在上述代碼中，創建了一個線程。接著，向線程發送了一條消息。通過調用 `create_and_process_run`，代理被要求在該線程上執行工作。最後，消息被提取並記錄下來以查看代理的回應。這些消息表明了使用者與代理之間對話的進展。還需要了解的是，消息可以是不同類型的，例如文本、圖片或文件，這些是代理的工作結果，例如生成了一張圖片或文本回應。作為開發者，您可以使用這些資訊進一步處理回應或將其呈現給使用者。

- **與其他 AI 框架集成**。Azure AI Agent Service 可以與其他框架（如 AutoGen 和 Semantic Kernel）互動，這意味著您可以在其中一個框架中構建部分應用，並使用 Agent Service 作為協作器，或者完全在 Agent Service 中構建應用。

**使用案例**：Azure AI Agent Service 專為需要安全、可擴展和靈活的 AI 代理部署的企業應用而設計。

## 這些框架之間有什麼區別？

看起來這些框架之間有很多重疊，但它們在設計、功能和目標使用案例方面有一些關鍵差異：

- **AutoGen**：是一個專注於多代理系統前沿研究的實驗框架。它是實驗和原型設計複雜多代理系統的最佳選擇。
- **Semantic Kernel**：是一個面向企業代理應用的生產就緒代理庫。專注於事件驅動的分佈式代理應用，支持多個 LLMs 和 SLMs、工具以及單/多代理設計模式。
- **Azure AI Agent Service**：是一個 Azure Foundry 中的代理平台和部署服務。它提供與 Azure Found 支持的服務（如 Azure OpenAI、Azure AI Search、Bing Search 和代碼執行）的連接。

仍然不確定該選擇哪一個？

### 使用案例

讓我們通過一些常見的使用案例來幫助您：

> 問：我正在進行實驗、學習並構建概念驗證代理應用，我希望能快速構建和實驗。
>

> 答：AutoGen 是此場景的良好選擇，因為它專注於事件驅動的分佈式代理應用，並支持高級多代理設計模式。

> 問：為什麼 AutoGen 比 Semantic Kernel 和 Azure AI Agent Service 更適合這個使用案例？
>
> 答：AutoGen 專門設計用於事件驅動的分佈式代理應用，非常適合自動化代碼生成和資料分析任務。它提供了必要的工具和功能，可以高效地構建複雜的多代理系統。

> 問：聽起來 Azure AI Agent Service 也可以用於此場景，它有代碼生成工具和更多功能？
>
> 答：是的，Azure AI Agent Service 是一個代理平台服務，並內建支持多個模型、Azure AI Search、Bing Search 和 Azure Functions。它使您可以輕鬆在 Foundry Portal 中構建代理並進行大規模部署。

> 問：我還是很困惑，直接給我一個選擇吧。
>
> 答：一個很好的選擇是先在 Semantic Kernel 中構建您的應用，然後使用 Azure AI Agent Service 部署您的代理。這種方法使您能夠輕鬆持久化您的代理，同時利用 Semantic Kernel 構建多代理系統的能力。此外，Semantic Kernel 在 AutoGen 中有一個連接器，使得同時使用這兩個框架變得容易。

讓我們用表格來總結關鍵差異：

| 框架 | 重點 | 核心概念 | 使用案例 |
| --- | --- | --- | --- |
| AutoGen | 事件驅動的分佈式代理應用 | 代理、角色、功能、資料 | 代碼生成、資料分析任務 |
| Semantic Kernel | 理解和生成類似人類的文本內容 | 代理、模組化組件、協作 | 自然語言理解、內容生成 |
| Azure AI Agent Service | 靈活模型、企業安全、代碼生成、工具調用 | 模組化、協作、流程協作 | 安全、可擴展且靈活的 AI 代理部署 |

每個框架的理想使用案例是什麼？

## 我可以直接整合現有的 Azure 生態系統工具，還是需要獨立解決方案？

答案是肯定的，您可以直接整合現有的 Azure 生態系統工具，特別是 Azure AI Agent Service，因為它已被設計為與其他 Azure 服務無縫協作。例如，您可以整合 Bing、Azure AI Search 和 Azure Functions。此外，它還與 Azure AI Foundry 深度集成。

對於 AutoGen 和 Semantic Kernel，您也可以整合 Azure 服務，但可能需要從代碼中調用 Azure 服務。另一種整合方式是使用 Azure SDKs 從代理中與 Azure 服務互動。此外，如前所述，您可以使用 Azure AI Agent Service 作為協作器，來協作由 AutoGen 或 Semantic Kernel 構建的代理，這將使得訪問 Azure 生態系統更加容易。

### 對 AI Agent 框架有更多疑問？

加入 [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)，與其他學習者交流，參加辦公時間並解答您的 AI 代理相關問題。

## 參考資料

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel 和 AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">使用 Azure AI Agent Service 與 AutoGen / Semantic Kernel 構建多代理解決方案</a>

## 上一課

[AI 代理和代理使用案例介紹](../01-intro-to-ai-agents/README.md)

## 下一課

[理解代理設計模式](../03-agentic-design-patterns/README.md)

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。