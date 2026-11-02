[![探索 AI 代理框架](../../../translated_images/zh-HK/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(按上方圖片觀看本課程影片)_

# 探索 AI 代理框架

AI 代理框架是設計用來簡化 AI 代理創建、部署與管理的軟件平台。這些框架為開發者提供預先建置的元件、抽象層和工具，協助簡化複雜 AI 系統的開發流程。

這些框架幫助開發者專注於應用程式的獨特面向，藉由提供標準化的解決方案來應對 AI 代理開發中的常見挑戰，提升 AI 系統的擴展性、可訪問性與效率。

## 簡介

本課程將涵蓋：

- 什麼是 AI 代理框架，它讓開發者能達成什麼目標？
- 團隊如何利用這些框架快速原型、迭代和提升代理的功能？
- 微軟所打造的框架和工具（<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> 與 <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>）有何差異？
- 我可以直接整合現有的 Azure 生態系工具，還是需要獨立方案？
- 什麼是 Microsoft Foundry Agent Service，如何幫助我？

## 學習目標

本課程目標是幫助你理解：

- AI 代理框架在 AI 開發中的角色。
- 如何利用 AI 代理框架打造智慧代理。
- AI 代理框架所能啟用的關鍵功能。
- 微軟代理框架與 Microsoft Foundry Agent Service 的差異。

## 什麼是 AI 代理框架，它讓開發者能做什麼？

傳統 AI 框架可以幫助你將 AI 整合進應用程式，並透過以下方式提升這些應用程式：

- <strong>個人化</strong>：AI 能分析用戶行為與偏好，提供個人化推薦、內容及體驗。
範例：Netflix 等串流服務利用 AI 根據觀看歷史推薦電影與劇集，提升用戶參與度與滿意度。
- <strong>自動化與效率</strong>：AI 能自動化重複工作，精簡工作流程並提升營運效率。
範例：客服應用透過 AI 驅動的聊天機器人處理常見詢問，縮短回應時間並釋放人工作更多複雜任務。
- <strong>強化使用者體驗</strong>：AI 提供語音識別、自然語言處理及預測文字等智慧功能，提升整體使用體驗。
範例：Siri 與 Google Assistant 等虛擬助理運用 AI 理解與回應語音指令，讓用戶更輕鬆操作裝置。

### 聽起來很棒，那為何我們還需要 AI 代理框架？

AI 代理框架不僅是 AI 框架，它們設計用來創建能與用戶、其他代理和環境互動以達成特定目標的智慧代理。這些代理能展現自主行為、做出決策，並適應變化條件。以下是一些 AI 代理框架所啟用的重要功能：

- <strong>代理協作與協調</strong>：可創建多個 AI 代理，讓它們能合作、通訊和協調解決複雜任務。
- <strong>任務自動化與管理</strong>：提供自動化多步驟工作流程、任務指派與動態任務管理機制。
- <strong>情境理解與適應</strong>：讓代理能理解上下文、適應變化環境，並基於即時資訊做出決策。

總結來說，代理讓你做到更多，將自動化提升到更高層次，創造能從環境學習並適應的更智慧系統。

## 如何快速原型、迭代並提升代理功能？

這是一個快速變動的領域，但多數 AI 代理框架共有能幫助你快速原型並迭代的特質，像是模組化元件、協作工具和即時學習。以下深入說明這些要素：

- <strong>使用模組化元件</strong>：AI SDK 提供預建元件，如 AI 和記憶連接器、利用自然語言或程式插件呼叫函式、提示模板等。
- <strong>利用協作工具</strong>：設計具特定角色與任務的代理，使其能測試與精煉協作工作流程。
- <strong>即時學習</strong>：實作反饋迴路，代理從互動中學習並動態調整行為。

### 使用模組化元件

像 Microsoft Agent Framework 的 SDK 提供預先建置的元件，如 AI 連接器、工具定義和代理管理。

<strong>團隊如何使用</strong>：團隊能快速組裝這些元件來建立功能性原型，免除從零開始，促進快速實驗與迭代。

<strong>實務運用方式</strong>：你可以使用預建解析器從用戶輸入提取訊息，利用記憶模組儲存與取用資料，並用提示生成器與用戶互動，所有元件均無需自行構建。

<strong>範例程式碼</strong>。以下展示如何使用 Microsoft Agent Framework 的 `FoundryChatClient`，使模型能透過工具呼叫回應用戶輸入：

``` python
# 微軟代理框架 Python 範例

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# 定義一個預訂旅行的範例工具函數
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
    # 範例輸出：您於2025年1月1日的飛往紐約的航班已成功預訂。祝旅途愉快！✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

從此範例你可以看到如何利用預建解析器從用戶輸入中抽取關鍵資訊，如航班訂票請求的出發地、目的地與日期。這種模組化方式讓你能專注於高層邏輯。

### 利用協作工具

像 Microsoft Agent Framework 這類框架促進多代理合作建立。

<strong>團隊如何使用</strong>：團隊能設計具特定角色和任務的代理，以測試與改進協作工作流程，提升整體系統效率。

<strong>實務運用方式</strong>：你可建立一組代理，每個代理有專門功能，如資料檢索、分析或決策。這些代理可通訊並共享資訊，以達成共同目標，如回應用戶查詢或完成任務。

**範例程式碼（Microsoft Agent Framework）**：

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

# 數據擷取代理
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# 數據分析代理
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

從前述程式碼可見，如何建立涵蓋多個代理協作分析資料的任務。每個代理執行特定職能，並透過協調完成目標。透過創建具專門角色的代理，能提升任務效率和效能。

### 即時學習

進階框架提供即時情境理解與適應功能。

<strong>團隊如何使用</strong>：團隊可實施反饋迴路，讓代理從互動中學習並動態調整行為，持續改善與精煉功能。

<strong>實務運用方式</strong>：代理能分析用戶回饋、環境數據及任務結果，更新知識庫，調整決策算法，並隨時間提升效能。這種持續迭代的學習過程使代理適應變化條件和用戶偏好，強化系統整體效益。

## 微軟代理框架（Microsoft Agent Framework）與 Microsoft Foundry Agent Service 有何差異？

這兩者有多種比較角度，以下從設計、功能與目標使用情境說明幾項主要差異：

## 微軟代理框架 (MAF)

微軟代理框架提供簡化的 SDK，讓開發者透過 `FoundryChatClient` 建立 AI 代理。它使開發者能利用 Azure OpenAI 模型，具備內建工具呼叫、對話管理和企業級透過 Azure 身份驗證的安全措施。

<strong>使用案例</strong>：用於建置具工具使用、多步驟工作流程與企業整合場景的生產等級 AI 代理。

以下是微軟代理框架的重要核心概念：

- <strong>代理</strong>。代理透過 `FoundryChatClient` 創建並配置名稱、指令與工具。代理能：
  - <strong>處理用戶訊息</strong>，並利用 Azure OpenAI 模型生成回應。
  - <strong>根據對話上下文自動呼叫工具</strong>。
  - <strong>維持多輪對話狀態</strong>。

  下面程式碼片段展示如何創建代理：

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

- <strong>工具</strong>。此框架支援以 Python 函式定義代理可自動調用的工具，這些工具於代理創建時註冊：

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

- <strong>多代理協調</strong>。你可創建多個專精不同領域的代理，並協調其工作：

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

- **Azure 身份整合**。框架使用 `AzureCliCredential`（或 `DefaultAzureCredential`）提供安全、免管理 API 金鑰的身份驗證。

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service 是較近期推出的服務，於 Microsoft Ignite 2024 發布。它允許開發與部署使用更靈活模型的 AI 代理，例如直接調用開源大語言模型如 Llama 3、Mistral 和 Cohere。

Microsoft Foundry Agent Service 提供更強的企業安全機制與數據儲存方式，適合企業級應用。

它即時與微軟代理框架整合，方便建立和部署代理。

目前此服務處於公開預覽階段，支持以 Python 和 C# 建立代理。

使用 Microsoft Foundry Agent Service Python SDK，可以創建配有自訂工具的代理：

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

Microsoft Foundry Agent Service 擁有以下核心概念：

- <strong>代理</strong>。Microsoft Foundry Agent Service 與 Microsoft Foundry 整合。在 Microsoft Foundry 內，AI 代理充當「智慧」微服務，用於回答問題 (RAG)、執行動作或完全自動化工作流程。它結合生成式 AI 模型與工具，使其能存取並互動真實資料來源。以下為代理範例：

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    範例中代理使用模型 `gpt-5-mini`，命名為 `my-agent`，指令為「你是有幫助的代理」。代理配備工具和資源以執行程式碼解釋任務。

- <strong>線程與訊息</strong>。線程是另一重要概念，代表代理與用戶間的對話或互動。線程用來追蹤對話進程、儲存上下文資料與管理互動狀態。以下為線程範例：

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # 要求代理在該線程上執行工作
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # 抓取並記錄所有訊息以查看代理的回應
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    上述程式碼中創建了一個線程，接著向線程發送訊息。透過呼叫 `create_and_process_run`，代理被要求在該線程上執行工作。最後擷取訊息並記錄，以查看代理回應。訊息顯示用戶與代理間對話的進行情況。同時須知訊息可為文字、影像或檔案，意味代理工作可能產生影像或文字回應等多種輸出。作為開發者，你可利用這些資訊進一步處理回應或呈現給用戶。

- <strong>與微軟代理框架整合</strong>。Microsoft Foundry Agent Service 可無縫與微軟代理框架合作，讓你能使用 `FoundryChatClient` 建立代理，並透過代理服務於生產環境部署。

<strong>使用案例</strong>：Microsoft Foundry Agent Service 設計用於需安全、可擴展與靈活 AI 代理部署的企業應用。

## 這些方案差異為何？
 
確實兩者有重疊，但在設計、功能與目標使用情境上具關鍵不同：
 
- **微軟代理框架 (MAF)**：為適用於生產的 SDK，提供簡潔 API 建立具工具呼叫、對話管理及 Azure 身份整合的代理。
- **Microsoft Foundry Agent Service**：為 Microsoft Foundry 中的代理平台與部署服務，內建連接 Azure OpenAI、Azure AI Search、Bing Search 及程式碼執行服務。
 
還是不確定該選哪一個？

### 使用情境
 
讓我們透過幾個常見使用案例幫助你決定：
 
> 問：我正在建立生產等級 AI 代理應用，希望快速起步
>

>答：微軟代理框架是不錯的選擇。它透過 `FoundryChatClient` 提供簡潔且 Python 化的 API，讓你用幾行程式碼定義帶有工具和指令的代理。

>問：我需要企業等級部署，並整合 Azure 搜尋與程式碼執行等服務
>
> 答：Microsoft Foundry Agent Service 更適合。它是平台服務，內建多型模型、Azure AI 搜尋、Bing 搜尋與 Azure Functions，讓你能在 Foundry Portal 輕鬆建立代理並大規模部署。
 
> 問：我仍然感到困惑，請只告訴我一個選擇
>
> 答：先使用微軟代理框架建立代理，當需要生產部署和擴展時再利用 Microsoft Foundry Agent Service。這樣你能快速迭代代理邏輯，同時保有清晰企業部署路徑。
 
我們整理主要差異如下表：

| 框架 | 專注點 | 核心概念 | 使用案例 |
| --- | --- | --- | --- |
| 微軟代理框架 | 簡化代理 SDK 且具工具呼叫 | 代理、工具、Azure 身份 | 建立 AI 代理、使用工具、多步驟工作流程 |
| Microsoft Foundry Agent Service | 彈性模型，企業安全，代碼生成，工具呼叫 | 模組化、協作、流程編排 | 安全、可擴展且靈活的 AI 代理部署 |

## 我可以直接整合現有的 Azure 生態系工具，還是需要獨立方案？


答案是肯定的，你可以直接將現有的 Azure 生態系統工具與 Microsoft Foundry Agent Service 整合，尤其是因為它是專門為與其他 Azure 服務無縫協作而構建的。舉例來說，你可以整合 Bing、Azure AI 搜尋和 Azure Functions。Microsoft Foundry 也提供深度整合。

Microsoft Agent Framework 也通過 `FoundryChatClient` 和 Azure 身份整合 Azure 服務，讓你可以直接從代理工具呼叫 Azure 服務。

## 範例程式碼

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## 有更多關於 AI 代理框架的問題嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，與其他學習者互動，參加辦公時間，並解決你的 AI 代理相關問題。

## 參考資料

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## 之前的課程

[AI 代理介紹與代理用例](../01-intro-to-ai-agents/README.md)

## 下一堂課

[理解 Agentic 設計模式](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->