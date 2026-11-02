[![探索 AI Agent 框架](../../../translated_images/zh-TW/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(點擊上方圖片觀看本課程影片)_

# 探索 AI Agent 框架

AI agent 框架是設計用來簡化 AI agent 創建、部署及管理的軟體平台。這些框架為開發者提供了預建元件、抽象化和工具，能夠簡化複雜 AI 系統的開發。

這些框架幫助開發者專注於他們應用的獨特面向，提供對 AI agent 開發中常見挑戰的標準化解決方案。它們提升了建立 AI 系統的可擴展性、易用性與效率。

## 簡介

這堂課將涵蓋：

- 什麼是 AI Agent 框架，開發者可以透過它實現什麼目標？
- 團隊如何利用這些框架快速原型、迭代並提升 agent 的能力？
- 微軟開發的框架與工具（<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> 與 <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>）有何差異？
- 我能否直接與現有的 Azure 生態系統工具整合，還是需要獨立解決方案？
- 什麼是 Microsoft Foundry Agent Service，它如何幫助我？

## 學習目標

本課程的目標是幫助您理解：

- AI Agent 框架在 AI 開發中的角色。
- 如何運用 AI Agent 框架構建智慧代理。
- AI Agent 框架所提供的關鍵能力。
- Microsoft Agent Framework 與 Microsoft Foundry Agent Service 之間的差異。

## 什麼是 AI Agent 框架，能讓開發者做什麼？

傳統 AI 框架可以協助您將 AI 整合到應用程式中，並提升以下面向：

- <strong>個人化</strong>：AI 可分析使用者行為和偏好，提供個人化的推薦、內容及體驗。
範例：像 Netflix 這樣的串流服務會依據觀看歷史主動推薦電影與節目，提升使用者參與度與滿意度。
- <strong>自動化與效率提升</strong>：AI 可自動執行重複性工作，簡化工作流，提升營運效率。
範例：客戶服務應用程式使用 AI 驅動的聊天機器人處理常見查詢，縮短回應時間，並將人力釋放給更複雜的問題。
- <strong>增強使用者體驗</strong>：AI 可提供語音辨識、自然語言處理及預測文字等智慧功能，改善整體使用體驗。
範例：虛擬助理如 Siri 與 Google Assistant 使用 AI 理解並回應語音指令，讓使用者更輕鬆互動。

### 聽起來都很棒，那為什麼我們還需要 AI Agent 框架？

AI Agent 框架不只是一般的 AI 框架。它們專為創建智慧代理設計，這些代理能與使用者、其他代理及環境互動，以達成特定目標。這些代理能展現自主行為、做決策並適應變化條件。來看看 AI Agent 框架帶來的一些主要能力：

- <strong>代理協作與協調</strong>：能創建多個 AI 代理協同工作、溝通並協調解決複雜任務。
- <strong>任務自動化與管理</strong>：提供多步驟工作流自動化、任務委派與動態任務管理機制。
- <strong>情境理解與適應</strong>：提供代理理解環境情境、適應變化並基於即時信息做決策的能力。

總結來說，代理能讓您達成更多、自動化更高階，創造更智慧、可適應且能從環境學習的系統。

## 如何快速原型、迭代並提升代理能力？

這個領域快速演進，但多數 AI Agent 框架中共有幾個要素可助您快速原型與迭代，即模組化元件、協作工具與即時學習。以下深入介紹：

- <strong>使用模組化元件</strong>：AI SDK 提供預建元件，如 AI 與記憶體連接器、以自然語言或程式插件調用函數、提示模板等。
- <strong>運用協作工具</strong>：設計具特定角色與任務的代理，讓它們測試並精進協作工作流。
- <strong>即時學習</strong>：實作回饋迴路，讓代理從互動中學習並動態調整行為。

### 使用模組化元件

像 Microsoft Agent Framework 這類 SDK 提供預建元件，如 AI 連接器、工具定義與代理管理。

<strong>團隊如何運用</strong>：團隊可快速組裝這些元件，創建功能性原型，避免從零開始，促進快速試驗與迭代。

<strong>實務運作方式</strong>：您可以使用預建的解析器從使用者輸入提取資訊、利用記憶模組儲存和檢索資料，以及使用提示生成器與使用者互動，全部不需從頭構建這些元件。

<strong>範例程式碼</strong>。以下範例展示如何使用 Microsoft Agent Framework 與 `FoundryChatClient` 讓模型對使用者輸入呼叫工具並回應：

``` python
# 微軟 Agent Framework Python 範例

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# 定義一個範例工具函數來預訂旅行
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
    # 範例輸出：您在 2025 年 1 月 1 日飛往紐約的航班已成功預訂。祝您旅途愉快！ ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

從這個範例中您能看到如何利用預建解析器從使用者輸入中提取航班訂票的起點、終點與日期等關鍵資訊。這種模組化方式讓您能專注於高階邏輯。

### 運用協作工具

像 Microsoft Agent Framework 的框架促使創建多個可協同合作的代理。

<strong>團隊如何運用</strong>：團隊可以設計具體角色與任務的代理，讓它們測試並優化協作工作流，以提升整體系統效率。

<strong>實務運作方式</strong>：您可建立一組代理，每個代理專精特定功能，如資料擷取、分析或決策。這些代理能溝通並共享資訊，以達成共同目標，如回答使用者查詢或完成任務。

**範例程式碼（Microsoft Agent Framework）**：

```python
# 使用 Microsoft Agent Framework 建立多個協同工作的代理人

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# 資料擷取代理人
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# 資料分析代理人
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# 依序執行代理人完成任務
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

從前述程式碼您可以看到如何建立一個涉及多個代理協同分析資料的任務。每個代理擔當特定功能，並通過協調代理完成任務。藉由創建具專業角色的專用代理，您可以提升任務效率與表現。

### 即時學習

進階框架提供即時情境理解與適應功能。

<strong>團隊如何運用</strong>：團隊可實作回饋迴路，讓代理從互動中學習並動態調整行為，持續提升能力。

<strong>實務運作方式</strong>：代理能分析使用者回饋、環境資料與任務結果，更新知識庫，調整決策演算法，並隨時間提升表現。這類迭代學習過程促使代理適應變化環境與使用者偏好，增強系統整體效能。

## Microsoft Agent Framework 與 Microsoft Foundry Agent Service 有什麼差別？

兩者間有多種比較角度，以下是設計理念、能力與目標使用場景的主要差異：

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework 提供簡化的 SDK，使用 `FoundryChatClient` 來搭建 AI 代理。它讓開發者能建立利用 Azure OpenAI 模型，具備內建工具呼叫、對話管理及透過 Azure 身份進行企業級安全防護的代理。

<strong>使用場景</strong>：打造具備工具使用、多步驟工作流與企業整合的生產等級 AI 代理。

這是 Microsoft Agent Framework 的一些重要核心概念：

- <strong>代理</strong>。透過 `FoundryChatClient` 建立代理，配置名稱、說明與工具。代理可：
  - <strong>處理使用者訊息</strong>，使用 Azure OpenAI 模型生成回應。
  - <strong>根據對話上下文自動呼叫工具</strong>。
  - <strong>維持多輪對話狀態</strong>。

  以下為建立代理的程式碼片段：

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

- <strong>工具</strong>。框架支援將工具定義為代理可自動呼叫的 Python 函數。工具在建立代理時註冊：

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

- <strong>多代理協調</strong>。可建立多個專精不同領域的代理並協調作業：

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

- **Azure 身份整合**。框架使用 `AzureCliCredential`（或 `DefaultAzureCredential`）進行安全且無需管理 API 金鑰的驗證。

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service 是較新的方案，於 Microsoft Ignite 2024 發表。它容許開發和部署具有彈性模型的 AI 代理，像是直接呼叫開源大規模語言模型（LLM），如 Llama 3、Mistral 和 Cohere。

Microsoft Foundry Agent Service 提供較強的企業安全機制與資料存取方法，非常適合企業應用。

它可與 Microsoft Agent Framework 無縫搭配使用，方便建構與部署代理。

此服務目前為公開預覽，支援使用 Python 及 C# 建構代理。

使用 Microsoft Foundry Agent Service 的 Python SDK，我們可以建立擁有使用者定義工具的代理：

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# 定義工具函式
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

Microsoft Foundry Agent Service 有以下核心概念：

- <strong>代理</strong>。Foundry Agent Service 整合進 Microsoft Foundry。AI 代理在 Microsoft Foundry 中充當「智慧」微服務，可用於回答問題（RAG）、執行動作，或完全自動化工作流程。它結合生成式 AI 模型強大能力與可訪問和互動真實數據來源的工具。以下為一個代理範例：

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    在此範例中，建立了模型為 `gpt-5-mini`、名稱為 `my-agent` 且指令為「You are helpful agent」的代理。該代理配備了能執行程式碼解譯任務的工具與資源。

- <strong>對話串與訊息</strong>。對話串是一項重要概念，代表代理與使用者之間的對話或互動。對話串可用於追蹤對話進度、儲存情境資訊及管理互動狀態。以下為對話串範例：

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # 請代理執行該執行緒上的工作
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # 擷取並記錄所有訊息以查看代理的回應
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    在之前的程式碼中，建立了一個對話串，接著向該對話串送出訊息。呼叫 `create_and_process_run` 後，代理被邀請在此串中執行工作。最後，取得並紀錄訊息以查看代理回應。這些訊息顯示使用者與代理對話的進展。也需要理解訊息類型可能不同，像是文字、圖片或檔案，表示代理工作成果可能是一張圖片或文本回應。作為開發者，您可以進一步利用這些資訊來處理回應或呈現給使用者。

- **與 Microsoft Agent Framework 整合**。Microsoft Foundry Agent Service 無縫搭配 Microsoft Agent Framework，表示您可使用 `FoundryChatClient` 建立代理，並透過 Agent Service 部署於生產環境。

<strong>使用場景</strong>：Microsoft Foundry Agent Service 適合需安全、可擴展且彈性代理部署的企業應用。

## 這些方案有什麼差異？
 
表面看來似乎有重疊，但在設計理念、能力與目標使用場景上仍有主要差異：
 
- **Microsoft Agent Framework (MAF)**：一套生產就緒的 SDK，可用於建構具工具呼叫、對話管理及 Azure 身份整合功能的 AI 代理。
- **Microsoft Foundry Agent Service**：一個 Microsoft Foundry 中的代理平台與部署服務，提供內建連接到 Azure OpenAI、Azure AI Search、Bing Search 和程式碼執行等多項服務。
 
還是不確定該怎麼選？

### 使用場景
 
讓我們透過幾個常見使用案例來協助您判斷：
 
> 問：我正在打造生產用 AI 代理應用，想快速入門
>

>答：Microsoft Agent Framework 是不錯的選擇。它提供透過 `FoundryChatClient` 使用的簡潔 Python API，可讓您用少量程式碼定義具工具與指令的代理。

>問：我需要企業級部署，整合 Azure 服務如搜尋與程式碼執行
>
> 答：Microsoft Foundry Agent Service 是最佳選擇。它是一個平台服務，提供多種模型、Azure AI Search、Bing Search 及 Azure Functions 等內建功能。您可輕鬆在 Foundry 入口網站建構代理並大規模部署。
 
> 問：我還是很困惑，給我一個選項就好
>
> 答：先用 Microsoft Agent Framework 建構代理，當需要部署及擴展到生產環境時，再使用 Microsoft Foundry Agent Service。此策略讓您能快速在代理邏輯上迭代，且擁有明確的企業部署路徑。
 
以下透過表格總結兩者主要差異：

| 框架 | 重點 | 核心概念 | 使用場景 |
| --- | --- | --- | --- |
| Microsoft Agent Framework | 精簡的代理 SDK，具工具呼叫功能 | 代理、工具、Azure 身份 | 建構 AI 代理、工具使用、多步驟工作流 |
| Microsoft Foundry Agent Service | 彈性模型、企業安全、程式碼產生、工具呼叫 | 模組化、協作、流程編排 | 安全、可擴展與彈性 AI 代理部署 |

## 我能否直接整合現有 Azure 生態系統工具，還是需要獨立解決方案？


答案是肯定的，您可以將現有的 Azure 生態系統工具直接與 Microsoft Foundry Agent Service 整合，特別是因為它是為了與其他 Azure 服務無縫協作而建構的。您例如可以整合 Bing、Azure AI 搜尋和 Azure Functions。與 Microsoft Foundry 也有深度整合。

Microsoft Agent Framework 也可透過 `FoundryChatClient` 和 Azure 身分識別整合 Azure 服務，讓您能直接從代理工具呼叫 Azure 服務。

## 範例程式碼

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## 對 AI Agent Framework 有更多問題嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，與其他學習者交流，參加辦公時間，並獲得您的 AI Agent 問題解答。

## 參考資料

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## 前一課程

[AI Agent 與代理使用案例介紹](../01-intro-to-ai-agents/README.md)

## 下一課程

[理解 Agentic 設計模式](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->