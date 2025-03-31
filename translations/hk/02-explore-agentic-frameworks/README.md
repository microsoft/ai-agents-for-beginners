<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d3ceafa2939ede602b96d6bd412c5cbf",
  "translation_date": "2025-03-28T11:42:11+00:00",
  "source_file": "02-explore-agentic-frameworks\\README.md",
  "language_code": "hk"
}
-->
[![探索 AI Agent 框架](../../../translated_images/lesson-2-thumbnail.807a3a4fc57057096d10678bf84638d17d50c50239014e75a7708731a33bb802.hk.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(點擊上方圖片觀看本課程影片)_

# 探索 AI Agent 框架

AI Agent 框架是一種軟件平台，旨在簡化 AI agent 的創建、部署和管理。這些框架為開發者提供了預建的組件、抽象層和工具，幫助他們更高效地開發複雜的 AI 系統。

這些框架通過標準化方法解決 AI agent 開發中的常見挑戰，幫助開發者專注於應用的獨特方面。同時，它們也提升了 AI 系統的可擴展性、可用性和效率。

## 簡介

本課程將涵蓋：

- AI Agent 框架是什麼？它能幫助開發者實現什麼目標？
- 團隊如何利用這些框架快速原型設計、迭代並提升 agent 的能力？
- 微軟開發的框架和工具之間有什麼區別？
- 我是否可以直接整合現有的 Azure 生態系統工具，還是需要獨立解決方案？
- Azure AI Agents 服務是什麼，它如何幫助我？

## 學習目標

本課程的目標是幫助你了解：

- AI Agent 框架在 AI 開發中的角色。
- 如何利用 AI Agent 框架構建智能代理。
- AI Agent 框架所啟用的主要功能。
- AutoGen、Semantic Kernel 和 Azure AI Agent Service 的差異。

## AI Agent 框架是什麼？它能幫助開發者做什麼？

傳統的 AI 框架可以幫助你將 AI 整合到應用中，並提升應用的以下方面：

- **個性化**：AI 可以分析用戶行為和偏好，提供個性化的推薦、內容和體驗。
  範例：像 Netflix 這樣的流媒體服務利用 AI 根據觀看歷史推薦電影和節目，提升用戶參與度和滿意度。
- **自動化與效率**：AI 可以自動化重複性任務、簡化工作流程並提高運營效率。
  範例：客服應用使用 AI 驅動的聊天機器人處理常見查詢，縮短響應時間，讓人工客服專注於更複雜的問題。
- **提升用戶體驗**：AI 可以通過提供智能功能（如語音識別、自然語言處理和預測文本）改善整體用戶體驗。
  範例：虛擬助手如 Siri 和 Google Assistant 使用 AI 理解並響應語音指令，使用戶更容易與設備互動。

### 聽起來很棒，那為什麼我們需要 AI Agent 框架？

AI Agent 框架不僅僅是 AI 框架。它們旨在創建能與用戶、其他代理和環境互動以實現特定目標的智能代理。這些代理能展現自主行為、做出決策並適應變化的環境。以下是 AI Agent 框架啟用的一些主要功能：

- **代理協作與協調**：支持創建多個 AI 代理，讓它們能協作、通信並協同完成複雜任務。
- **任務自動化與管理**：提供多步工作流的自動化、任務分配以及代理之間的動態任務管理機制。
- **上下文理解與適應**：賦予代理理解上下文、適應變化環境並根據實時信息做出決策的能力。

總結來說，代理讓你能做更多事情，將自動化提升到新的層次，創建能從環境中學習和適應的更智能系統。

## 如何快速原型設計、迭代並提升代理的能力？

這是一個快速變化的領域，但大多數 AI Agent 框架都有一些共同特點，能幫助你快速原型設計和迭代，主要包括模塊化組件、協作工具和實時學習。以下是詳細內容：

- **使用模塊化組件**：AI SDK 提供預建的組件，如 AI 和記憶連接器、自然語言或代碼插件功能調用、提示模板等。
- **利用協作工具**：設計具有特定角色和任務的代理，測試和完善協作工作流。
- **實時學習**：實施反饋迴路，讓代理從交互中學習並動態調整其行為。

### 使用模塊化組件

像 Microsoft Semantic Kernel 和 LangChain 這樣的 SDK 提供預建的組件，如 AI 連接器、提示模板和記憶管理。

**團隊如何使用這些**：團隊可以快速組裝這些組件，創建功能性原型，而無需從零開始，從而進行快速試驗和迭代。

**實際運作方式**：你可以使用預建的解析器從用戶輸入中提取信息，使用記憶模塊存儲和檢索數據，以及使用提示生成器與用戶交互，所有這些都不需要從頭開始構建。

**範例代碼**：以下是使用 Semantic Kernel Python 和 .Net 的預建 AI 連接器的範例代碼，它使用自動函數調用來讓模型響應用戶輸入：

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

從這個範例中可以看到，你如何利用預建的解析器從用戶輸入中提取關鍵信息，例如航班預訂請求的出發地、目的地和日期。這種模塊化方法讓你能專注於高層次邏輯。

### 利用協作工具

像 CrewAI、Microsoft AutoGen 和 Semantic Kernel 這樣的框架能促進多個代理的創建，讓它們能協作完成任務。

**團隊如何使用這些**：團隊可以設計具有特定角色和任務的代理，測試並完善協作工作流，提高整個系統的效率。

**實際運作方式**：你可以創建一個代理團隊，每個代理都有專門功能，如數據檢索、分析或決策。這些代理可以通信並共享信息，以達成共同目標，例如回答用戶查詢或完成任務。

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

在上述代碼中，你可以看到如何創建一個涉及多個代理協作分析數據的任務。每個代理執行特定功能，通過協調代理執行任務來達成預期結果。通過創建專門角色的代理，你可以提高任務效率和性能。

### 實時學習

高級框架提供實時上下文理解和適應的能力。

**團隊如何使用這些**：團隊可以實施反饋迴路，讓代理從交互中學習並動態調整其行為，從而持續改進和完善能力。

**實際運作方式**：代理可以分析用戶反饋、環境數據和任務結果，更新其知識庫、調整決策算法並提高性能。這種迭代學習過程使代理能適應變化的條件和用戶偏好，提升整體系統的效能。

## AutoGen、Semantic Kernel 和 Azure AI Agent Service 框架有什麼不同？

這些框架有許多相似之處，但我們可以從設計、功能和目標使用場景來看它們的主要差異：

## AutoGen

AutoGen 是由微軟研究的 AI Frontiers Lab 開發的一個開源框架。它專注於事件驅動的分佈式 *agentic* 應用，支持多個 LLM 和 SLM、工具以及高級多代理設計模式。

AutoGen 的核心概念是代理，它是一種自主實體，能感知環境、做出決策並採取行動以實現特定目標。代理通過異步消息進行通信，允許它們獨立並行工作，提升系統的可擴展性和響應性。
模組化、協作、流程編排 | 安全、可擴展且靈活的 AI 代理部署 | 這些框架各自最理想的使用場景是什麼？

## 我可以直接整合現有的 Azure 生態系統工具，還是需要獨立的解決方案？

答案是可以的，你可以直接將現有的 Azure 生態系統工具與 Azure AI Agent Service 整合，特別是因為它已經被設計成與其他 Azure 服務無縫配合。例如，你可以整合 Bing、Azure AI Search 和 Azure Functions。此外，還有與 Azure AI Foundry 的深度整合。

對於 AutoGen 和 Semantic Kernel，你同樣可以整合 Azure 服務，但可能需要從你的程式碼中調用 Azure 服務。另一種整合方式是使用 Azure SDKs，讓你的代理與 Azure 服務互動。

另外，如前所述，你也可以使用 Azure AI Agent Service 作為 AutoGen 或 Semantic Kernel 建立的代理的編排器，這樣可以更輕鬆地訪問 Azure 生態系統。

## 參考資料

---

## 前一課程

[AI 代理與代理使用案例簡介](../01-intro-to-ai-agents/README.md)

## 下一課程

[理解代理設計模式](../03-agentic-design-patterns/README.md)

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議尋求專業的人工翻譯。我們對因使用本翻譯而引起的任何誤解或錯誤解釋不承擔責任。