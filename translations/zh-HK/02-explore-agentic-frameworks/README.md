[![探索 AI 智能代理框架](../../../translated_images/zh-HK/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(點擊上方圖片觀看本課程影片)_

# 探索 AI 智能代理框架

AI 智能代理框架是設計用來簡化 AI 智能代理創建、部署及管理的軟體平台。這些框架為開發者提供了預先建立好的組件、抽象層和工具，有助於簡化複雜 AI 系統的開發。

這些框架透過提供解決 AI 智能代理開發中常見挑戰的標準化方法，幫助開發者專注於應用的獨特面向。它們提升了建立 AI 系統的可擴充性、易用性和效率。

## 介紹

本課程將涵蓋：

- 什麼是 AI 智能代理框架，它讓開發者能達成什麼目標？
- 團隊如何利用這些框架快速原型設計、迭代並提升代理的能力？
- 微軟創建的框架和工具（<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI 智能代理服務</a> 與 <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">微軟智能代理框架</a>）有何不同？
- 我能否直接整合現有 Azure 生態系統工具，還是需要獨立解決方案？
- 什麼是 Azure AI 智能代理服務，它如何協助我？

## 學習目標

本課程的目標是幫助你理解：

- AI 智能代理框架在 AI 開發中的角色。
- 如何運用 AI 智能代理框架建構智慧代理。
- AI 智能代理框架所提供的關鍵能力。
- 微軟智能代理框架與 Azure AI 智能代理服務的差異。

## 什麼是 AI 智能代理框架，它讓開發者能做什麼？

傳統 AI 框架可以幫助你將 AI 整合到應用程式中，並從以下幾方面提升應用程式功能：

- **個人化**：AI 分析用戶行為和偏好，提供個人化推薦、內容和體驗。  
  範例：Netflix 等串流平台利用 AI 根據觀看歷史推薦電影和節目，提升用戶參與度和滿意度。  
- **自動化和效率**：AI 可自動化重複性任務，優化工作流程，提升營運效率。  
  範例：客服應用利用 AI 聊天機器人處理常見問題，縮短回應時間，讓人員專注處理複雜問題。  
- **提升用戶體驗**：AI 提供語音識別、自然語言處理和預測文字等智能功能，改善整體用戶體驗。  
  範例：Siri 和 Google 助理用 AI 理解並回應語音指令，使用戶更輕鬆與設備互動。

### 聽起來不錯，那為什麼我們需要 AI 智能代理框架？

AI 智能代理框架不只是傳統 AI 框架，它們被設計來創建能與用戶、其他代理及環境互動以達成特定目標的智慧代理。這些代理可以展現自主行為、做決策並適應變動條件。讓我們看幾個由 AI 智能代理框架實現的關鍵能力：

- **代理協作與協調**：支援多個 AI 代理合作、溝通與協調，解決複雜任務。
- **任務自動化與管理**：提供機制自動化多步驟工作流程、任務委派及動態任務管理。
- **情境理解與適應**：賦予代理理解上下文、適應變化環境並根據即時資訊做決策的能力。

總結來說，透過代理，你能做更多事情，推動自動化到新層次，打造能適應並學習其環境的智慧系統。

## 如何快速原型設計、迭代並提升代理能力？

這是個快速演進的領域，但大多數 AI 智能代理框架共有幾個能幫助你快速原型和迭代的要素，主要是模組化組件、協作工具及即時學習。讓我們深入探討：

- **使用模組化組件**：AI SDK 提供預建的組件，如 AI 與記憶連接器、利用自然語言或程式碼插件呼叫函數、提示模板等。
- **利用協作工具**：設計有特定角色與任務的代理，能測試與優化協同行工作流程。
- **即時學習**：實作反饋迴路，讓代理從互動中學習並動態調整行為。

### 使用模組化組件

像微軟智能代理框架提供 AI 連接器、工具定義和代理管理等預建組件。

**團隊如何運用**：團隊可迅速組裝這些組件，創造功能原型，無需從零開始，快速試驗和迭代。

**實務運作**：你可以使用預建解析器從用戶輸入提取資訊，利用記憶模組儲存與檢索資料，以及使用提示生成器與用戶互動，無需自行開發這些組件。

**範例程式碼**。以下展示如何用微軟智能代理框架搭配 `AzureAIProjectAgentProvider`，讓模型對用戶輸入進行工具呼叫回應：

``` python
# Microsoft Agent Framework Python 範例

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# 定義一個範例工具函數以預訂旅程
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
    # 範例輸出: 您已成功預訂了2025年1月1日飛往紐約的航班。祝旅途愉快！ ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```
  
這個例子顯示如何利用預建解析器從用戶輸入中萃取重要訊息，如航班訂票的起點、終點和日期。這種模組化方法讓你能專注於高階邏輯。

### 利用協作工具

像微軟智能代理框架支持建立多個合作代理。

**團隊如何運用**：團隊可以設計有特定角色和任務的代理，協助測試和優化協作流程，提高整體系統效率。

**實務運作**：你可建立一組代理， 每個代理專責如數據檢索、分析或決策。這些代理能互相溝通共享資訊，以完成共同目標，如回答用戶查詢或完成任務。

**範例程式碼（微軟智能代理框架）**：

```python
# 使用 Microsoft Agent Framework 建立多個協同工作的代理人

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# 資料擷取代理人
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# 資料分析代理人
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# 按順序於一項任務上執行代理人
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```
  
上述程式碼展示如何創建涉及多個代理協作分析數據的任務。每個代理負責特定功能，透過協調執行任務達成預期結果。透過創建具專業角色的代理，提升任務效率與效能。

### 即時學習

進階框架支援即時情境理解與適應能力。

**團隊如何運用**：團隊可實作反饋迴路，讓代理從互動吸收經驗並動態調整行為，持續改善和精進能力。

**實務運作**：代理能分析用戶回饋、環境資料及任務結果，更新知識庫、調整決策演算法，隨時間提升效能。這種反覆學習流程使代理可適應變化的條件和用戶偏好，增強整體系統效益。

## 微軟智能代理框架與 Azure AI 智能代理服務有何不同？

可從設計理念、能力和目標使用情境來比較這兩種方案：

## 微軟智能代理框架（MAF）

微軟智能代理框架提供簡化的 SDK，使用 `AzureAIProjectAgentProvider` 來建立 AI 代理。它讓開發者能打造利用 Azure OpenAI 模型的代理，內建工具呼叫、對話管理及透過 Azure 身份驗證提供企業級安全。

**使用場景**：建立具備工具使用、多步驟工作流程及企業整合的生產等級 AI 代理。

以下是微軟智能代理框架的重要核心概念：

- **代理 (Agents)**。代理透過 `AzureAIProjectAgentProvider` 建立，配置名稱、指令和工具。代理能：
  - **處理用戶訊息**並使用 Azure OpenAI 模型生成回應。
  - **基於對話上下文自動呼叫工具**。
  - **維持多次互動的對話狀態**。

  以下程式碼示範如何建立代理：

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
  
- **工具 (Tools)**。框架支援定義能被代理自動調用的 Python 函數工具。工具在建立代理時註冊：

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
  
- **多代理協調**。可創建具有不同專長的多個代理並協調運作：

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
  
- **Azure 身份驗證整合**。框架使用 `AzureCliCredential`（或 `DefaultAzureCredential`）實現安全無密鑰驗證，無需直接管理 API 金鑰。

## Azure AI 智能代理服務

Azure AI 智能代理服務是較近期推出的產品，於 Microsoft Ignite 2024 發布。它支援開發和部署更彈性的 AI 代理模型，例如可直接呼叫開源大型語言模型（LLM）如 Llama 3、Mistral 和 Cohere。

Azure AI 智能代理服務提供更強的企業安全機制和資料存儲方案，適合企業應用。

它與微軟智能代理框架無縫整合，便於建立和部署代理。

該服務目前為公開預覽，支援 Python 和 C# 開發代理。

使用 Azure AI 智能代理服務 Python SDK 時，我們可以建立帶有自定義工具的代理：

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

Azure AI 智能代理服務具有以下核心概念：

- **代理 (Agent)**。Azure AI 智能代理服務與 Microsoft Foundry 整合。在 AI Foundry 中，AI 代理是一種「智慧」微服務，用於回答問題（RAG）、執行動作或全面自動化工作流程。它結合生成 AI 模型的威力與可存取及操作真實世界數據來源的工具。以下是代理範例：

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```
  
    此範例中，代理使用模型 `gpt-4o-mini`，名為 `my-agent`，指令為「你是有幫助的代理」。代理裝備有工具和資源以執行程式碼解釋任務。

- **對話串 (Thread) 與訊息**。對話串是另一重要概念，代表代理與用戶間的對話或互動。對話串用來追蹤對話進度、儲存上下文資訊及管理互動狀態。以下是對話串範例：

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
  
    上述程式碼先建立一個對話串，接著向對話串傳送訊息。呼叫 `create_and_process_run` 時，代理被要求在該對話串上執行工作。最後擷取並記錄訊息以查看代理回應。訊息代表用戶與代理間對話的進展。也要理解訊息可包含文本、圖片或檔案等不同類型，即代理的工作成果可能是圖像或文本回覆。開發者可利用這些資訊進一步處理回應或呈現給用戶。

- **與微軟智能代理框架整合**。Azure AI 智能代理服務與微軟智能代理框架無縫協作，也就是說可以用 `AzureAIProjectAgentProvider` 建立代理，再透過代理服務部署到生產環境。

**使用場景**：Azure AI 智能代理服務適用於需要安全、可擴充及彈性 AI 代理部署的企業應用。

## 這些方案的差異是什麼？

兩者確實有重疊，但在設計、能力與目標使用情境上有幾個關鍵差異：

- **微軟智能代理框架 (MAF)**：生產等級的 AI 代理 SDK，提供簡化的 API，支援工具呼叫、對話管理和 Azure 身份集成。
- **Azure AI 智能代理服務**：基於 Azure Foundry 的代理平台與部署服務，內建對 Azure OpenAI、Azure AI 搜尋、Bing 搜尋及程式碼執行等服務的連接。

還是不確定該怎麼選？

### 使用情境

讓我們看看一些常見使用情境來協助你：

> 問：我想快速開始建立生產用 AI 代理應用，該怎麼做？

> 答：微軟智能代理框架是不錯的選擇。它透過 `AzureAIProjectAgentProvider` 提供簡潔且符合 Python 風格的 API，讓你用幾行程式碼定義帶工具和指令的代理。

> 問：我需要企業級部署，並整合像搜尋與程式碼執行等 Azure 服務，該選哪個？

> 答：Azure AI 智能代理服務最合適。它是個平台服務，具備多模型、Azure AI 搜尋、Bing 搜尋及 Azure Functions 的內建功能，方便你在 Foundry 入口網站建立代理並大規模部署。

> 問：我還是搞不清楚，給我一個選擇吧！

> 答：先用微軟智能代理框架開發代理，當需要生產部署與擴展時，再用 Azure AI 智能代理服務。這樣你能快速迭代代理邏輯，並清楚走向企業部署。

以下是主要差異的摘要表：

| 框架 | 聚焦 | 核心概念 | 使用情境 |
| --- | --- | --- | --- |
| 微軟智能代理框架 | 精簡的代理 SDK + 工具呼叫 | 代理、工具、Azure 身份驗證 | 建構 AI 代理、工具應用、多步驟工作流程 |
| Azure AI 智能代理服務 | 彈性模型、企業安全、程式碼生成、工具呼叫 | 模組化、協作、流程編排 | 安全、擴充及彈性 AI 代理部署 |

## 我能否直接整合現有 Azure 生態系統工具，還是需要獨立解決方案？
答案是肯定的，你可以直接將你現有的 Azure 生態系統工具與 Azure AI Agent Service 整合，尤其是它已經設計為能與其他 Azure 服務無縫配合。例如，你可以整合 Bing、Azure AI Search 以及 Azure Functions。它也與 Microsoft Foundry 有深度整合。

Microsoft Agent Framework 也透過 `AzureAIProjectAgentProvider` 以及 Azure 身份，與 Azure 服務整合，讓你能夠直接從代理工具呼叫 Azure 服務。

## Sample Codes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Got More Questions about AI Agent Frameworks?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Previous Lesson

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Next Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件乃使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件以其母語版本為權威資料來源。對於重要資訊，建議聘請專業人類譯者進行翻譯。對於因使用本翻譯而產生的任何誤解或誤釋，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->