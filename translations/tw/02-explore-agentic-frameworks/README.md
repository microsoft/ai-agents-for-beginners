<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d3ceafa2939ede602b96d6bd412c5cbf",
  "translation_date": "2025-03-28T14:09:57+00:00",
  "source_file": "02-explore-agentic-frameworks\\README.md",
  "language_code": "tw"
}
-->
[![探索 AI 代理框架](../../../translated_images/lesson-2-thumbnail.807a3a4fc57057096d10678bf84638d17d50c50239014e75a7708731a33bb802.tw.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(點擊上方圖片觀看本課程影片)_

# 探索 AI 代理框架

AI 代理框架是專門設計用來簡化 AI 代理創建、部署和管理的軟體平台。這些框架為開發者提供預建的組件、抽象層及工具，以簡化複雜 AI 系統的開發。

透過提供標準化的方法來解決 AI 代理開發中的常見挑戰，這些框架幫助開發者專注於應用程式的獨特方面，同時提升系統的可擴展性、可訪問性和效率。

## 介紹

本課程將涵蓋：

- 什麼是 AI 代理框架？它能幫助開發者實現哪些目標？
- 團隊如何使用這些框架快速原型設計、迭代及提升代理能力？
- 微軟所創建的框架和工具之間有何差異？
- 我可以直接整合現有的 Azure 生態系統工具，還是需要獨立的解決方案？
- 什麼是 Azure AI Agents 服務，它能如何幫助我？

## 學習目標

本課程的目標是幫助你了解：

- AI 代理框架在 AI 開發中的角色。
- 如何利用 AI 代理框架構建智能代理。
- AI 代理框架所啟用的關鍵功能。
- AutoGen、Semantic Kernel 和 Azure AI Agent Service 的差異。

## 什麼是 AI 代理框架？它能幫助開發者實現哪些目標？

傳統的 AI 框架可以幫助你將 AI 整合到應用程式中，並使這些應用程式變得更好：

- **個性化**：AI 可以分析使用者行為和偏好，提供個性化的推薦、內容和體驗。
  範例：像 Netflix 這樣的串流服務使用 AI 根據觀看歷史推薦電影和節目，提升使用者的參與度和滿意度。
- **自動化和效率**：AI 可以自動化重複性任務、簡化工作流程並提升運營效率。
  範例：客戶服務應用程式使用 AI 驅動的聊天機器人處理常見查詢，縮短響應時間並讓人類代理專注於更複雜的問題。
- **提升使用者體驗**：AI 可以通過提供智能功能（如語音識別、自然語言處理和預測文字）來改善整體使用者體驗。
  範例：像 Siri 和 Google Assistant 這樣的虛擬助理使用 AI 理解並回應語音命令，讓使用者更輕鬆地與設備互動。

### 聽起來很棒對吧，那為什麼還需要 AI 代理框架？

AI 代理框架不僅僅是 AI 框架，它們旨在創建能與使用者、其他代理及環境交互以實現特定目標的智能代理。這些代理能表現出自主行為、做出決策並適應不斷變化的條件。以下是 AI 代理框架啟用的一些關鍵功能：

- **代理協作與協調**：支持創建多個 AI 代理，讓它們能共同工作、溝通並協調以解決複雜任務。
- **任務自動化與管理**：提供機制以自動化多步工作流程、任務委派及代理間的動態任務管理。
- **上下文理解與適應**：使代理具備理解上下文、適應環境變化並根據即時信息做出決策的能力。

總結來說，代理可以幫助你做得更多，將自動化提升到新的層次，創建能適應並從環境中學習的更智能系統。

## 如何快速原型設計、迭代及提升代理能力？

這是一個快速變化的領域，但大多數 AI 代理框架中有一些共同點可以幫助你快速原型設計和迭代，包括模組化組件、協作工具及即時學習。讓我們深入了解：

- **使用模組化組件**：AI SDK 提供預建的組件，例如 AI 和記憶體連接器、使用自然語言或代碼插件進行功能調用、提示模板等。
- **利用協作工具**：設計具有特定角色和任務的代理，測試並完善協作工作流程。
- **即時學習**：實施反饋迴路，使代理從交互中學習並動態調整行為。

### 使用模組化組件

像 Microsoft Semantic Kernel 和 LangChain 的 SDK 提供了預建的組件，例如 AI 連接器、提示模板和記憶體管理。

**團隊如何使用這些**：團隊可以快速組裝這些組件以創建功能性原型，而無需從頭開始，從而實現快速實驗和迭代。

**實際操作如何運作**：你可以使用預建的解析器從使用者輸入中提取信息，使用記憶體模組存儲和檢索數據，並使用提示生成器與使用者交互，無需從頭構建這些組件。

**範例代碼**。以下是使用 Semantic Kernel Python 和 .Net 的預建 AI 連接器進行自動功能調用以回應使用者輸入的範例：

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

從這個範例中可以看到，你如何利用預建的解析器從使用者輸入中提取關鍵信息，例如航班預訂請求的起點、目的地和日期。這種模組化方法讓你能專注於高層次邏輯。

### 利用協作工具

像 CrewAI、Microsoft AutoGen 和 Semantic Kernel 的框架促進了多個代理的創建，使它們能共同工作。

**團隊如何使用這些**：團隊可以設計具有特定角色和任務的代理，測試並完善協作工作流程，提升整體系統效率。

**實際操作如何運作**：你可以創建一組代理，每個代理都有專門功能，例如數據檢索、分析或決策。這些代理可以溝通並共享信息以達成共同目標，例如回答使用者查詢或完成任務。

**範例代碼（AutoGen）**：

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

在之前的代碼中，你看到如何創建一個任務，涉及多個代理共同分析數據。每個代理執行特定功能，並通過協調代理來完成所需的結果。通過創建具有專門角色的代理，你可以提升任務效率和性能。

### 即時學習

高級框架提供即時上下文理解和適應的能力。

**團隊如何使用這些**：團隊可以實施反饋迴路，使代理從交互中學習並動態調整行為，從而持續改進和能力完善。

**實際操作如何運作**：代理可以分析使用者反饋、環境數據及任務結果，以更新其知識庫、調整決策算法並隨時間提升性能。這種迭代學習過程使代理能適應變化的條件和使用者偏好，提升整體系統效能。

## AutoGen、Semantic Kernel 和 Azure AI Agent Service 之間有什麼不同？

有很多方法可以比較這些框架，但讓我們從設計、功能和目標使用案例的角度來看看一些關鍵差異：
模組化、協作、流程編排 | 安全、可擴展且靈活的 AI 代理部署 | 這些框架的理想使用案例是什麼？

## 我可以直接整合現有的 Azure 生態系統工具，還是需要獨立解決方案？

答案是肯定的，你可以直接將現有的 Azure 生態系統工具整合到 Azure AI Agent Service 中，特別是因為它被設計為與其他 Azure 服務無縫協作。例如，你可以整合 Bing、Azure AI Search 和 Azure Functions。它還與 Azure AI Foundry 有深度整合。

對於 AutoGen 和 Semantic Kernel，你也可以與 Azure 服務整合，但可能需要從代碼中調用 Azure 服務。另一種整合方式是使用 Azure SDKs，讓你的代理與 Azure 服務互動。此外，如前所述，你可以使用 Azure AI Agent Service 作為 AutoGen 或 Semantic Kernel 中構建代理的編排器，從而輕鬆訪問 Azure 生態系統。

## 參考資料

## 上一課

[AI 代理與代理使用案例簡介](../01-intro-to-ai-agents/README.md)

## 下一課

[理解代理設計模式](../03-agentic-design-patterns/README.md)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或錯誤解釋概不負責。