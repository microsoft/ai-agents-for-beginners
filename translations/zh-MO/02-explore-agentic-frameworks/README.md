[![探索 AI 代理框架](../../../translated_images/zh-MO/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(點擊上方圖片觀看本課程影片)_

# 探索 AI 代理框架

AI 代理框架是設計用來簡化 AI 代理創建、部署及管理的軟件平台。這些框架為開發者提供了預先建構的組件、抽象層及工具，讓開發複雜 AI 系統更為流暢。

這些框架幫助開發者專注於應用的獨特面向，透過標準化的方法解決 AI 代理開發中的共通挑戰。它們提升了 AI 系統建置的可擴展性、易用性及效率。

## 介紹

本課程將涵蓋：

- 什麼是 AI 代理框架，以及它們讓開發者能實現什麼？
- 團隊如何利用這些框架快速建立原型、反覆調整與改進代理的能力？
- 微軟建立的框架與工具（<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> 與 <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>）有何不同？
- 我能否直接整合既有的 Azure 生態系工具，或必須使用獨立方案？
- 什麼是 Microsoft Foundry Agent Service，它如何協助我？

## 學習目標

本課程目標是協助你了解：

- AI 代理框架在 AI 開發中的角色。
- 如何利用 AI 代理框架建構智能代理。
- AI 代理框架賦予的關鍵能力。
- 微軟 Agent Framework 與 Microsoft Foundry Agent Service 的差異。

## 什麼是 AI 代理框架，它們讓開發者能做什麼？

傳統的 AI 框架可以幫助你在應用中整合 AI，並在以下方面提升應用：

- <strong>個人化</strong>：AI 能分析用戶行為與偏好，提供個人化推薦、內容與體驗。
範例：串流服務如 Netflix 利用 AI 根據觀看歷史推薦電影與節目，提升用戶參與度及滿意度。
- <strong>自動化與效率</strong>：AI 可自動化重覆任務、簡化工作流程、提升營運效率。
範例：客服應用使用 AI 聊天機器人處理常見詢問，減少回應時間，並讓人工客服專注於較複雜問題。
- <strong>增強用戶體驗</strong>：AI 透過語音識別、自然語言處理及預測文字等智能特性，改善整體用戶體驗。
範例：虛擬助理 Siri 和 Google Assistant 利用 AI 理解並回應語音指令，讓用戶更輕鬆與裝置互動。

### 聽起來很棒，那為什麼我們還需要 AI 代理框架？

AI 代理框架代表了超越普通 AI 框架的東西。它們旨在創造能與用戶、其他代理及環境互動，以達成特定目標的智能代理。這些代理能展現自主行為，做決策，並對變化條件作出調整。讓我們看看 AI 代理框架賦予的一些關鍵能力：

- <strong>代理協作與協調</strong>：支持建立多個代理共同工作、溝通並協調解決複雜任務。
- <strong>任務自動化與管理</strong>：提供自動化多步工作流程、任務分派及動態任務管理機制。
- <strong>上下文理解與適應</strong>：賦予代理理解上下文、適應環境變化及基於即時資訊做決策的能力。

總結來說，代理讓你能做更多，提升自動化層級，創造能因應且從環境學習的更智能系統。

## 如何快速建立原型、反覆調整並改進代理的能力？

這個領域發展迅速，但大多數 AI 代理框架有一些共同特點能幫助快速原型及調整，主要是模組化組件、協作工具及即時學習。讓我們深入看看：

- <strong>使用模組化組件</strong>：AI SDK 提供預先建構組件，如 AI 與記憶連接器、使用自然語言或程式碼外掛呼叫函數、提示模板等。
- <strong>利用協作工具</strong>：設計特定角色與任務的代理，讓它們測試並優化協作工作流程。
- <strong>即時學習</strong>：實作回饋循環，讓代理從互動中學習並動態調整行為。

### 使用模組化組件

像是 Microsoft Agent Framework 提供預建組件，如 AI 連接器、工具定義及代理管理。

<strong>團隊如何利用</strong>：團隊可快速組裝這些組件，建立功能性原型，無需從零開始，利於快速嘗試與調整。

<strong>實際運作方式</strong>：你可使用預建分析器從用戶輸入擷取資訊，利用記憶模組存取資料，並用提示產生器與用戶互動，無需重建基礎組件。

<strong>程式碼範例</strong>。以下示範如何使用 Microsoft Agent Framework 與 `FoundryChatClient` 讓模型藉由呼叫工具回應用戶輸入：

``` python
# 微軟代理框架 Python 範例

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# 定義一個用來預訂旅遊的示範工具函數
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
    # 範例輸出：您於 2025 年 1 月 1 日飛往紐約的航班已成功預訂。祝旅途愉快！✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

從此示例你可看到，如何利用預建分析器從用戶輸入擷取關鍵資訊，如航班訂票的起點、終點與日期。此模組化方式讓你專注於高階邏輯。

### 利用協作工具

微軟 Agent Framework 之類的框架促進多個代理共同協作。

<strong>團隊如何利用</strong>：團隊可設計專門功能與任務的代理，借此測試並完善協作流程，提升系統整體效率。

<strong>實際運作方式</strong>：你可建立一組代理團隊，每個代理負責特定功能，如資料檢索、分析或決策。這些代理可溝通並共享資訊，以達成共同目標，例如回答用戶查詢或完成任務。

**程式碼範例（Microsoft Agent Framework）**：

```python
# 使用 Microsoft Agent Framework 建立多個協同工作的代理

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# 資料擷取代理
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# 資料分析代理
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# 按序執行代理完成任務
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

前述程式碼示範如何建立涉多個代理協作分析資料的任務。每個代理執行特定功能，任務透過協調代理達成預期結果。透過專職代理分工，可提升任務效率與效能。

### 即時學習

先進框架提供即時上下文理解與調適能力。

<strong>團隊如何利用</strong>：團隊可實作回饋循環，使代理從互動中學習，動態調整行為，持續提升與精進能力。

<strong>實際運作方式</strong>：代理分析用戶回饋、環境資料與任務結果，更新知識庫、調整決策演算法，隨時間提升效能。此反覆學習流程使代理能適應變動條件與用戶偏好，增強整體系統效能。

## 微軟 Agent Framework 與 Microsoft Foundry Agent Service 有何差異？

有多種比較方式，但讓我們集中於設計、能力與目標使用場景的主要差異：

## 微軟 Agent Framework (MAF)

微軟 Agent Framework 提供簡化的 SDK，利用 `FoundryChatClient` 建立 AI 代理。開發者可建置整合 Azure OpenAI 模型、具備內建工具呼叫、對話管理及企業級安全的代理。

<strong>使用情境</strong>：構建具工具利用、多步工作流程及企業整合場景的生產就緒 AI 代理。

微軟 Agent Framework 的重要核心概念包括：

- <strong>代理</strong>。代理透過 `FoundryChatClient` 創建，並設定名稱、指令與工具。代理可：
  - <strong>處理用戶消息</strong>，並利用 Azure OpenAI 模型產生回應。
  - <strong>自動呼叫工具</strong>，根據對話上下文進行。
  - <strong>維持多次互動的對話狀態</strong>。

  以下是建立代理的程式碼片段：

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

- <strong>工具</strong>。框架支持定義 Python 函數作為代理自動調用的工具。工具於建立代理時註冊：

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

- <strong>多代理協作</strong>。你可建立具不同專長的多個代理，並協調其工作：

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

- **Azure 身份整合**。框架使用 `AzureCliCredential`（或 `DefaultAzureCredential`）進行安全的無鍵認證，免除直接管理 API 金鑰。

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service 是較近期推出的服務，於 Microsoft Ignite 2024 發布。它允許以更靈活的模型開發及部署 AI 代理，例如直接呼叫開源大型語言模型如 Llama 3、Mistral 與 Cohere。

Microsoft Foundry Agent Service 提供更強的企業安全機制及資料儲存方式，適用於企業級應用。

它可與 Microsoft Agent Framework 無縫搭配，用於代理的建置與部署。

本服務目前為公開預覽，支持 Python 與 C# 建置代理。

使用 Microsoft Foundry Agent Service Python SDK，我們可建立帶有自訂工具的代理：

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# 定義工具函數
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
        model="gpt-4.1-mini",
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

Microsoft Foundry Agent Service 包含以下核心概念：

- <strong>代理</strong>。Microsoft Foundry Agent Service 整合於 Microsoft Foundry。於 Foundry 裡，AI 代理充當「智慧」微服務，可用於問答（RAG）、執行動作或全自動化工作流程。透過結合生成式 AI 模型與允許存取及互動真實世界資料來源的工具實現此功能。以下為代理範例：

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    在此範例中，代理以模型 `gpt-4.1-mini`、名稱 `my-agent` 與指令 `You are helpful agent` 建立。代理配備工具與資源以執行程式碼解譯任務。

- <strong>對話串與訊息</strong>。對話串是另一重要概念。它代表代理與用戶間的對話或互動。對話串可用於追蹤對話進度、儲存上下文資訊與管理狀態。以下為對話串範例：

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # 請代理於該線程上執行工作
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # 擷取並記錄所有訊息以查看代理的回應
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    上述程式碼中，建立了對話串，並送出訊息。呼叫 `create_and_process_run` 後，代理在該對話串上執行工作。最後取得並記錄訊息以查看代理回應。這些訊息顯示用戶與代理間對話的進度。訊息可能有多種類型，如文字、圖片或檔案，代表代理工作所產生的如圖片或文字回應。開發者可利用此資訊進一步處理回應或呈現予用戶。

- **整合 Microsoft Agent Framework**。Microsoft Foundry Agent Service 與 Microsoft Agent Framework 無縫合作，意味著你可用 `FoundryChatClient` 建構代理，並經由 Agent Service 部署至生產環境。

<strong>使用情境</strong>：Microsoft Foundry Agent Service 專為需安全、可擴展且彈性 AI 代理部署的企業應用而設計。

## 這些方法有何差異？
 
確實存在重疊，但設計、能力與目標使用場景有關鍵不同：
 
- **微軟 Agent Framework (MAF)**：為建構 AI 代理提供生產就緒 SDK。它提供用於建立具工具呼叫、對話管理及 Azure 身份整合的簡化 API。
- **Microsoft Foundry Agent Service**：為 Microsoft Foundry 內針對代理的平台及部署服務。它內建連接 Azure OpenAI、Azure AI Search、Bing Search 及程式碼執行等服務。
 
仍不確定該選哪一個？

### 使用情境
 
讓我們透過常見使用情境來協助你判斷：
 
> 問：我正在建構生產等級 AI 代理應用，想快速開始
>

> 答：微軟 Agent Framework 是很棒的選擇。它透過 `FoundryChatClient` 提供簡單、Pythonic 的 API，讓你能用少量程式碼定義帶有工具與指令的代理。

> 問：我需要企業級部署，並整合 Azure Search 與程式碼執行等功能
>
> 答：Microsoft Foundry Agent Service 是最佳選擇。它是平台服務，內建多種模型、Azure AI Search、Bing Search 與 Azure Functions，讓你輕鬆在 Foundry Portal 創建並大規模部署代理。
 
> 問：我還是很困惑，就給我一個選項吧
>
> 答：先使用微軟 Agent Framework 建構代理，待需要生產部署與擴展時，再轉用 Microsoft Foundry Agent Service。此路徑能快速迭代代理邏輯，同時有清晰的企業部署途徑。
 
我們來以表格總結主要差異：

| 架構 | 重點 | 核心概念 | 使用情境 |
| --- | --- | --- | --- |
| 微軟 Agent Framework | 精簡代理 SDK 與工具呼叫 | 代理、工具、Azure 身份 | 建構 AI 代理、工具使用、多步工作流程 |
| Microsoft Foundry Agent Service | 彈性模型、企業安全、程式碼生成、工具呼叫 | 模組化、協作、流程編排 | 安全、可擴展且彈性的 AI 代理部署 |

## 我可以直接整合既有的 Azure 生態系工具，還是必須使用獨立方案？


答案是肯定的，你可以將現有的 Azure 生態系統工具直接整合到 Microsoft Foundry Agent Service，特別是因為它是專為與其他 Azure 服務無縫合作而建構的。例如，你可以整合 Bing、Azure AI 搜尋和 Azure Functions。Microsoft Foundry 也有深入的整合。

Microsoft Agent Framework 也透過 `FoundryChatClient` 和 Azure 身份驗證整合 Azure 服務，讓你可以直接從代理工具呼叫 Azure 服務。

## 範例程式碼

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## 有更多關於 AI 代理框架的問題嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者交流，參加線上辦公時間並獲得你的 AI 代理問題的解答。

## 參考資料

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## 上一課

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## 下一課

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->