[![探索 AI 代理框架](../../../translated_images/zh-MO/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(按一下上方的圖片以觀看此課程的影片)_

# 探索 AI 代理框架

AI 代理框架是為簡化 AI 代理的建立、部署與管理而設計的軟體平台。這些框架提供開發者預先構建的元件、抽象層與工具，以利簡化複雜 AI 系統的開發。

這些框架透過為 AI 代理開發中常見的挑戰提供標準化的方法，幫助開發者專注於應用程式的獨特面向。它們能提升建置 AI 系統時的可擴充性、可及性與效率。

## 介紹 

本課程將涵蓋：

- 什麼是 AI 代理框架，以及它們讓開發者能達成什麼？
- 團隊如何利用這些框架快速原型、反覆迭代，並提升代理的能力？
- Microsoft 所建立的框架與工具之間有何差異（<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent 服務</a> 與 <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft 代理框架</a>）？
- 我可以直接整合現有的 Azure 生態系工具嗎？還是需要獨立解決方案？
- 什麼是 Azure AI Agents 服務，以及它如何協助我？

## 學習目標

本課程的目標是幫助你理解：

- AI 代理框架在 AI 開發中的角色。
- 如何運用 AI 代理框架來建構智慧代理。
- AI 代理框架所啟用的關鍵能力。
- Microsoft 代理框架與 Azure AI Agent Service 之間的差異。

## 什麼是 AI 代理框架，它們讓開發者能做什麼？

傳統的 AI 框架可以協助你將 AI 整合到應用程式中，並在以下方面提升應用程式的表現：

- **個人化**：AI 能分析使用者行為與偏好，提供個人化的建議、內容與體驗。
範例：像 Netflix 這類串流服務使用 AI 根據觀看紀錄推薦電影與節目，提升使用者參與度與滿意度。
- **自動化與效率**：AI 能自動化重複性工作、精簡工作流程，並提升營運效率。
範例：客服應用程式使用 AI 驅動的聊天機器人處理常見詢問，縮短回應時間並讓人類客服專注於較複雜的問題。
- **提升使用者體驗**：AI 能透過語音辨識、自然語言處理與預測文字等智慧功能，改善整體使用者體驗。
範例：像 Siri 與 Google Assistant 這類虛擬助理使用 AI 理解並回應語音指令，讓使用者更容易與裝置互動。

### 那聽起來都很棒，為什麼我們還需要 AI 代理框架？

AI 代理框架代表的不只是 AI 框架。它們被設計用以啟用可與使用者、其他代理與環境互動以達成特定目標的智慧代理建立。這些代理能展現自主行為、做出決策並適應變動條件。讓我們看一些由 AI 代理框架所啟用的關鍵能力：

- **代理之間的協作與協調**：支援建立多個能一起工作、溝通與協調以解決複雜任務的 AI 代理。
- **任務自動化與管理**：提供自動化多步工作流程、任務指派與代理之間動態任務管理的機制。
- **情境理解與適應**：賦予代理理解情境、適應變動環境並根據即時資訊做出決策的能力。

總結來說，代理讓你能做更多事，將自動化提升到另一個層次，建立能從環境中適應與學習的更智慧系統。

## 如何快速原型、反覆迭代與提升代理能力？

這是一個發展快速的領域，但大多數 AI 代理框架有一些共通之處，可以幫助你快速原型與迭代，特別是模組化元件、協作工具與即時學習。以下深入探討這些面向：

- **使用模組化元件**：AI SDK 提供預建元件，例如 AI 與記憶連接器、以自然語言或程式碼外掛進行的函式呼叫、提示範本等。
- **利用協作工具**：設計具有特定角色與任務的代理，讓它們測試並精進協作工作流程。
- **即時學習**：實作回饋迴路，讓代理從互動中學習並動態調整行為。

### 使用模組化元件

像 Microsoft 代理框架這類 SDK 提供預建元件，例如 AI 連接器、工具定義與代理管理。

**團隊如何使用這些元件**：團隊可以快速組裝這些元件以建立功能性原型，而不需從零開始，從而允許快速實驗與反覆迭代。

**實務運作方式**：你可以使用預建的解析器從使用者輸入中抽取資訊、使用記憶模組來儲存與檢索資料，以及使用提示產生器與使用者互動，全部都不需自行從頭建立這些元件。

**範例程式碼**。讓我們看一個範例，說明如何使用 Microsoft 代理框架與 `AzureAIProjectAgentProvider` 讓模型回應使用者輸入並進行工具呼叫：

``` python
# 微軟代理框架 Python 範例

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# 定義一個範例工具函數以預訂旅遊
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
    # 範例輸出：您2025年1月1日飛往紐約的航班已成功預訂。旅途愉快！✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

從這個範例可以看到，你如何利用預建的解析器從使用者輸入中擷取關鍵資訊，例如航班預訂請求的出發地、目的地與日期。這種模組化方法讓你能專注於高階邏輯。

### 利用協作工具

像 Microsoft 代理框架這類框架促進建立能協同工作的多個代理。

**團隊如何使用這些**：團隊可以設計具有特定角色與任務的代理，讓它們測試並精進協作工作流程，提升整體系統效率。

**實務運作方式**：你可以建立一組代理團隊，每個代理具備專門功能，例如資料擷取、分析或決策。這些代理可以相互溝通與分享資訊以達成共同目標，例如回應使用者查詢或完成任務。

**範例程式碼（Microsoft 代理框架）**：

```python
# 使用 Microsoft Agent Framework 創建多個協同工作的代理

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# 數據檢索代理
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# 數據分析代理
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# 按順序執行代理處理任務
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

前述程式碼展示了如何建立一個涉及多個代理共同工作的任務來分析資料。每個代理執行特定功能，並透過協調代理來執行該任務以達到期望結果。透過建立具專長角色的專用代理，你可以提升任務效率與效能。

### 即時學習

進階框架提供即時情境理解與適應的能力。

**團隊如何使用這些**：團隊可以實作回饋迴路，讓代理從互動中學習並動態調整行為，從而持續改進與精進能力。

**實務運作方式**：代理可以分析使用者回饋、環境資料與任務結果來更新其知識庫、調整決策演算法並隨時間提升效能。這種反覆的學習流程使代理能適應變動條件與使用者偏好，強化整體系統效能。

## Microsoft 代理框架與 Azure AI Agent Service 有何差異？

有許多比較方式，但讓我們從設計、能力與目標使用案例來檢視一些主要差異：

## Microsoft 代理框架 (MAF)

Microsoft 代理框架提供一個精簡的 SDK，用於使用 `AzureAIProjectAgentProvider` 建構 AI 代理。它使開發者能建立利用 Azure OpenAI 模型的代理，具備內建的工具呼叫、對話管理以及透過 Azure 身分的企業級安全性。

**使用案例**：建立具工具使用、多步工作流程與企業整合情境的生產就緒 AI 代理。

以下是 Microsoft 代理框架的一些重要核心概念：

- **代理**。代理透過 `AzureAIProjectAgentProvider` 建立，並以名稱、指示與工具進行配置。該代理可以：
  - **處理使用者訊息** 並使用 Azure OpenAI 模型產生回應。
  - **自動呼叫工具**，根據對話情境。
  - **在多次互動間維護對話狀態**。

  這裡有一段示範如何建立代理的程式碼片段：

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

- **工具**。框架支援將工具定義為代理可自動呼叫的 Python 函式。工具會在建立代理時註冊：

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

- **多代理協調**。你可以建立多個具有不同專長的代理並協調它們的工作：

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

- **Azure 身分整合**。框架使用 `AzureCliCredential`（或 `DefaultAzureCredential`）進行安全的無金鑰驗證，免除了直接管理 API 金鑰的需求。

## Azure AI Agent Service

Azure AI Agent Service 是在 Microsoft Ignite 2024 發表的較新服務。它允許開發與部署更靈活模型的 AI 代理，例如直接呼叫像 Llama 3、Mistral 與 Cohere 等開源 LLM。

Azure AI Agent Service 提供更強的企業安全機制與資料儲存方法，使其適合企業應用。

它與 Microsoft 代理框架 搭配即可即時使用，用於建置與部署代理。

該服務目前為公開預覽，並支援使用 Python 與 C# 來建構代理。

使用 Azure AI Agent Service Python SDK，我們可以建立一個帶有使用者自定義工具的代理：

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# 定義工具功能
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

Azure AI Agent Service 有以下核心概念：

- **代理**。Azure AI Agent Service 與 Microsoft Foundry 整合。在 AI Foundry 中，AI 代理扮演一個「智慧」微服務的角色，可用來回答問題（RAG）、執行動作或完全自動化工作流程。它透過將生成式 AI 模型的能力與能讓代理存取並與真實世界資料來源互動的工具結合來達成這些功能。以下是一個代理的範例：

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    在這個範例中，代理使用模型 `gpt-4o-mini` 建立，名稱為 `my-agent`，指示為 `You are helpful agent`。該代理配備了可執行程式碼解釋任務的工具與資源。

- **執行緒與訊息**。執行緒是另一個重要概念。它代表代理與使用者之間的對話或互動。執行緒可用來追蹤對話進度、儲存情境資訊與管理互動狀態。以下是一個執行緒的範例：

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

    在前述程式碼中，建立了一個執行緒。之後，向該執行緒傳送一則訊息。透過呼叫 `create_and_process_run`，要求代理在該執行緒上執行工作。最後，取回並記錄訊息以查看代理的回應。這些訊息指出使用者與代理之間對話的進度。也需理解訊息可以是不同類型，例如文字、影像或檔案，表示代理的工作可能產生影像或文字回應。作為開發者，你可以接著使用這些資訊進行進一步處理或呈現給使用者。

- **與 Microsoft 代理框架 整合**。Azure AI Agent Service 能與 Microsoft 代理框架 無縫運作，這表示你可以使用 `AzureAIProjectAgentProvider` 建構代理，並透過 Agent Service 部署它們以用於生產情境。

**使用案例**：Azure AI Agent Service 專為需要安全、可擴充且靈活 AI 代理部署的企業應用而設計。

## 這些方法之間有什麼不同？
 
乍看之下確實有重疊，但在設計、能力與目標使用案例上有一些關鍵差異：
 
- **Microsoft 代理框架 (MAF)**：是一個用於建置 AI 代理的生產就緒 SDK。它提供一個精簡的 API，用於建立具工具呼叫、對話管理與 Azure 身分整合的代理。
- **Azure AI Agent Service**：是在 Azure Foundry 中的代理平台與部署服務。它提供內建與 Azure OpenAI、Azure AI Search、Bing Search 與程式碼執行等服務的連接能力。
 
還是不確定該選哪一個？

### 使用情境
 
讓我們透過一些常見使用案例來幫助你做決定：
 
> Q: 我正在建置生產等級的 AI 代理應用，想快速上手
>

>A: Microsoft 代理框架 是一個很好的選擇。它透過 `AzureAIProjectAgentProvider` 提供簡單且 Python 化的 API，讓你只需幾行程式碼就能定義帶有工具與指示的代理。

>Q: 我需要具企業等級的部署並整合像 Search 與程式碼執行等 Azure 功能
>
> A: Azure AI Agent Service 最適合。它是一個平台服務，提供多模型、Azure AI Search、Bing Search 與 Azure Functions 等內建能力。你可以在 Foundry Portal 中建立代理並大規模部署。
 
> Q: 我還是有點混亂，只給我一個選項就好
>
> A: 先從 Microsoft 代理框架 開始建立你的代理，當你需要在生產環境中部署與擴展時再使用 Azure AI Agent Service。這種做法讓你能快速在代理邏輯上反覆迭代，同時保有一條明確的企業部署路徑。
 
讓我們用一張表總結主要差異：

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Streamlined agent SDK with tool calling | Agents, Tools, Azure Identity | Building AI agents, tool use, multi-step workflows |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

## 我可以直接整合現有的 Azure 生態系工具，還是需要獨立解決方案？
答案是肯定的，您可以將現有的 Azure 生態系統工具直接整合到 Azure AI Agent 服務，特別是因為它已被設計為能與其他 Azure 服務無縫運作。例如，您可以整合 Bing、Azure AI Search 與 Azure Functions。Microsoft Foundry 也有深度整合。

Microsoft Agent Framework 也透過 `AzureAIProjectAgentProvider` 和 Azure 身份整合 Azure 服務，讓您能從代理工具中直接呼叫 Azure 服務。

## 範例程式碼

- Python: [代理框架](./code_samples/02-python-agent-framework.ipynb)
- .NET: [代理框架](./code_samples/02-dotnet-agent-framework.md)

## 還對 AI 代理框架有更多問題嗎？

加入 [Microsoft Foundry 的 Discord](https://aka.ms/ai-agents/discord) 與其他學習者交流、參加辦公時間並獲得 AI 代理相關問題的解答。

## 參考資料

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent 服務</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI 回應</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent 服務</a>

## 上一課

[AI 代理與使用案例簡介](../01-intro-to-ai-agents/README.md)

## 下一課

[理解 Agentic 設計模式](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件已使用 AI 翻譯服務 Co-op Translator（https://github.com/Azure/co-op-translator）進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言版本應視為具權威性的來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯而引起的任何誤解或曲解，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->