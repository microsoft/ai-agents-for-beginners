[![探索 AI 代理框架](../../../translated_images/zh-TW/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(點擊上方圖片觀看本課程的影片)_

# Explore AI Agent Frameworks

AI 代理框架是設計來簡化 AI 代理的建立、部署與管理的軟體平台。這些框架為開發人員提供預建的元件、抽象層與工具，讓開發複雜 AI 系統的流程更為順暢。

這些框架透過對常見 AI 代理開發挑戰提供標準化方法，協助開發人員將注意力放在應用程式的獨特部分。它們提升了可擴充性、可及性與建置 AI 系統的效率。

## Introduction 

本課程將涵蓋：

- 什麼是 AI 代理框架，以及它們能讓開發人員達成什麼目標？
- 團隊如何利用這些框架快速建立原型、反覆開發與改進代理的能力？
- 由 Microsoft 所建立的框架與工具（<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> 與 <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>）之間有何差異？
- 我可以直接整合現有的 Azure 生態系工具，還是需要獨立解決方案？
- 什麼是 Azure AI Agents service，以及它如何協助我？

## Learning goals

本課程的目標是幫助你理解：

- AI 代理框架在 AI 開發中的角色。
- 如何利用 AI 代理框架來建構智能代理。
- AI 代理框架所啟用的關鍵能力。
- Microsoft Agent Framework 與 Azure AI Agent Service 之間的差異。

## What are AI Agent Frameworks and what do they enable developers to do?

傳統的 AI 框架能協助你將 AI 整合到應用程式中，並透過以下方式改善這些應用程式：

- **個人化**：AI 能夠分析使用者行為與偏好，提供個人化的建議、內容與體驗。
Example: 像 Netflix 這類的串流服務使用 AI 根據觀看記錄來建議電影與節目，提升使用者參與度與滿意度。
- **自動化與效率提升**：AI 可以自動化重複性任務、精簡工作流程並改善營運效率。
Example: 客服應用程式使用 AI 驅動的聊天機器人處理常見詢問，減少回應時間並讓人工客服可以專注於更複雜的問題。
- **強化使用者體驗**：AI 能透過語音識別、自然語言處理與預測文字等智慧功能改善整體使用者體驗。
Example: 像 Siri 與 Google Assistant 的虛擬助理使用 AI 理解並回應語音指令，使使用者更容易與裝置互動。

### That all sounds great right, so why do we need the AI Agent Framework?

AI 代理框架代表的不只是一般的 AI 框架。它們的設計目的是促成具備智能的代理，這些代理可以與使用者、其他代理與環境互動，以達成特定目標。這些代理能展現自主行為、做出決策，並適應不斷變化的條件。讓我們來看看 AI 代理框架所啟用的一些關鍵能力：

- **代理協作與協調**：支援建立多個 AI 代理共同工作、溝通與協調，以解決複雜任務。
- **任務自動化與管理**：提供自動化多步驟工作流程、任務委派以及代理間動態任務管理的機制。
- **情境理解與適應**：賦予代理理解情境、適應變動環境並根據即時資訊做出決策的能力。

總結來說，代理讓你可以做更多事，將自動化推向下一個層次，建立能從環境中適應與學習的更智慧系統。

## How to quickly prototype, iterate, and improve the agent’s capabilities?

這是一個快速演進的領域，但大多數 AI 代理框架有一些共通的元素，可以幫助你快速建立原型並反覆開發，主要包括模組化元件、協作工具與即時學習。我們來深入看看這些要點：

- **使用模組化元件**：AI SDK 提供預建元件，例如 AI 與記憶體連接器、以自然語言或程式碼插件進行的 function calling、提示模板等。
- **利用協作工具**：設計具特定角色與任務的代理，讓它們測試並精練協作工作流程。
- **即時學習**：實作回饋迴路，讓代理從互動中學習並動態調整其行為。

### Use Modular Components

像 Microsoft Agent Framework 這類的 SDK 提供預建元件，例如 AI 連接器、工具定義與代理管理。

**團隊如何使用這些元件**：團隊可以快速組裝這些元件以建立功能性原型，而不需從頭開始，從而加速實驗與反覆開發。

**實務上的運作方式**：你可以使用預建的解析器來從使用者輸入中提取資訊、使用記憶模組來儲存與檢索資料，並使用提示產生器與使用者互動，全部都不需要從零建立這些元件。

**範例程式碼**. 讓我們看看如何使用 Microsoft Agent Framework 與 `AzureAIProjectAgentProvider` 來讓模型在回應使用者輸入時呼叫工具：

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
    # 範例輸出：您於 2025 年 1 月 1 日飛往紐約的機票已成功預訂。祝旅途愉快！✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

從這個範例中你可以看到如何利用預建的解析器從使用者輸入中抽取關鍵資訊，例如班機訂位請求的出發地、目的地與日期。這種模組化的方法讓你可以專注於高階邏輯。

### Leverage Collaborative Tools

像 Microsoft Agent Framework 這類的框架促成建立多個可以一起合作的代理。

**團隊如何使用這些**：團隊可以設計具特定角色與任務的代理，讓它們測試並精練協作工作流程，提升整體系統效率。

**實務上的運作方式**：你可以建立一個代理團隊，每個代理都有專門的功能，例如資料檢索、分析或決策。這些代理可以互相溝通並分享資訊，以達成共同目標，例如回答使用者查詢或完成任務。

**範例程式碼 (Microsoft Agent Framework)**：

```python
# 使用 Microsoft Agent Framework 創建多個協同工作的代理

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# 資料擷取代理
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# 資料分析代理
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# 按順序執行代理以完成任務
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

在前面的程式碼中，你可以看到如何建立一個涉及多個代理一起分析資料的任務。每個代理執行特定功能，並透過協調代理來達成預期結果。透過建立具專門角色的專屬代理，你可以提升任務效率與效能。

### Learn in Real-Time

進階框架提供即時情境理解與適應的能力。

**團隊如何使用這些**：團隊可以實作回饋迴路，讓代理從互動中學習並動態調整其行為，從而持續改進與精練能力。

**實務上的運作方式**：代理可以分析使用者回饋、環境資料與任務結果來更新其知識庫、調整決策演算法並隨著時間提升效能。這種反覆的學習過程讓代理能夠適應變動條件與使用者偏好，增強整體系統效能。

## What are the differences between the Microsoft Agent Framework and Azure AI Agent Service?

有很多方式可以比較這些方法，但讓我們從設計、能力與目標使用情境來看一些關鍵差異：

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework 提供一個簡化的 SDK，透過 `AzureAIProjectAgentProvider` 建構 AI 代理。它使開發人員能建立利用 Azure OpenAI 模型的代理，並具備內建的工具呼叫、對話管理以及透過 Azure 身分驗證的企業級安全性。

**使用情境**：建立具工具使用能力、多步驟工作流程與企業整合場景的生產就緒 AI 代理。

以下是 Microsoft Agent Framework 的一些重要核心概念：

- **Agents**。代理是透過 `AzureAIProjectAgentProvider` 建立並以名稱、指示與工具來設定。代理可以：
  - **處理使用者訊息** 並使用 Azure OpenAI 模型產生回應。
  - **根據對話情境自動呼叫工具**。
  - **在多次互動中維持對話狀態**。

  下面是一段顯示如何建立代理的程式碼片段：

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

- **Tools**。該框架支援將工具定義為代理可以自動呼叫的 Python 函式。工具會在建立代理時註冊：

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

- **Azure 身分整合**。該框架使用 `AzureCliCredential`（或 `DefaultAzureCredential`）來達成安全、無金鑰的驗證，免去了直接管理 API 金鑰的需求。

## Azure AI Agent Service

Azure AI Agent Service 是較新的服務，於 Microsoft Ignite 2024 發表。它允許使用更具彈性的模型來開發與部署 AI 代理，例如直接呼叫像 Llama 3、Mistral 與 Cohere 等開源 LLM。

Azure AI Agent Service 提供更強的企業安全機制與資料儲存方法，使其適合企業應用。

它與 Microsoft Agent Framework 開箱即用地整合，方便建立與部署代理。

此服務目前屬於公開預覽（Public Preview），並支援使用 Python 與 C# 來建構代理。

使用 Azure AI Agent Service 的 Python SDK，我們可以建立一個帶有使用者定義工具的代理：

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

### Core concepts

Azure AI Agent Service 有以下核心概念：

- **Agent**。Azure AI Agent Service 與 Microsoft Foundry 整合。在 AI Foundry 中，AI 代理作為一個「智慧」微服務，可用來回答問題（RAG）、執行操作或完全自動化工作流程。它透過將生成式 AI 模型的能力與允許存取與互動真實世界資料來源的工具結合來實現這些功能。以下是一個代理的範例：

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    在此範例中，代理是使用模型 `gpt-4o-mini`、名稱 `my-agent` 與指示 `You are helpful agent` 建立。該代理配備了執行程式碼解析任務的工具與資源。

- **Thread and messages**。Thread（執行緒）是另一個重要概念。它代表代理與使用者之間的對話或互動。Thread 可用來追蹤對話進度、儲存上下文資訊以及管理互動狀態。以下是一個 thread 的範例：

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

    在前面的程式碼中，建立了一個 thread。接著，向該 thread 發送了一則訊息。透過呼叫 `create_and_process_run`，代理會被要求在該 thread 上執行工作。最後，訊息被擷取並記錄，以查看代理的回應。這些訊息表示使用者與代理之間對話的進展。同時也重要的是要理解，這些訊息可以有不同的類型，例如文字、影像或檔案，這表示代理的工作可能產生影像或文字回應等。例如，作為開發人員，你可以利用這些資訊進一步處理回應或呈現給使用者。

- **Integrates with the Microsoft Agent Framework**。Azure AI Agent Service 與 Microsoft Agent Framework 無縫整合，這表示你可以使用 `AzureAIProjectAgentProvider` 建構代理，並通過 Agent Service 將它們部署到生產環境。

**使用情境**：Azure AI Agent Service 為需要安全、可擴充且具彈性 AI 代理部署的企業應用而設計。

## What's the difference between these approaches?
 
看起來確實有重疊，但在設計、能力與目標使用情境方面有一些關鍵差異：
 
- **Microsoft Agent Framework (MAF)**：是一個用於建構 AI 代理的生產就緒 SDK。它提供一個簡化的 API 來建立具有工具呼叫、對話管理與 Azure 身分整合的代理。
- **Azure AI Agent Service**：是一個在 Azure Foundry 中針對代理的平臺與部署服務。它提供與 Azure OpenAI、Azure AI Search、Bing Search 與程式碼執行等服務的內建連接性。
 
還是不確定該選哪個？

### Use Cases
 
讓我們透過一些常見的使用情境來幫助你做決定：
 
> Q: I'm building production AI agent applications and want to get started quickly
>

> A: The Microsoft Agent Framework is a great choice. It provides a simple, Pythonic API via `AzureAIProjectAgentProvider` that lets you define agents with tools and instructions in just a few lines of code.

>Q: I need enterprise-grade deployment with Azure integrations like Search and code execution
>
> A: Azure AI Agent Service is the best fit. It's a platform service that provides built-in capabilities for multiple models, Azure AI Search, Bing Search and Azure Functions. It makes it easy to build your agents in the Foundry Portal and deploy them at scale.
 
> Q: I'm still confused, just give me one option
>
> A: Start with the Microsoft Agent Framework to build your agents, and then use Azure AI Agent Service when you need to deploy and scale them in production. This approach lets you iterate quickly on your agent logic while having a clear path to enterprise deployment.
 
讓我們以表格總結關鍵差異：

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Streamlined agent SDK with tool calling | Agents, Tools, Azure Identity | Building AI agents, tool use, multi-step workflows |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

## Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?
答案是肯定的，您可以將現有的 Azure 生態系工具直接整合到 Azure AI Agent Service，特別是它已被建置為能與其他 Azure 服務無縫運作。例如，您可以整合 Bing、Azure AI Search 和 Azure Functions。它也與 Microsoft Foundry 有深入整合。

Microsoft Agent Framework 也透過 `AzureAIProjectAgentProvider` 和 Azure identity 與 Azure 服務整合，讓您可以從代理工具直接呼叫 Azure 服務。

## 範例程式碼

- Python: [代理框架](./code_samples/02-python-agent-framework.ipynb)
- .NET: [代理框架](./code_samples/02-dotnet-agent-framework.md)

## 還有關於 AI 代理框架的更多問題嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者見面、參加辦公時間，並獲得您對 AI 代理的問題解答。

## 參考資料

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent 服務</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI 回應</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent 服務</a>

## 前一課

[AI 代理與使用案例簡介](../01-intro-to-ai-agents/README.md)

## 下一課

[理解代理式設計模式](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件為使用 AI 翻譯服務「Co-op Translator」（https://github.com/Azure/co-op-translator）所翻譯。雖然我們力求準確，但請注意，自動翻譯可能含有錯誤或不準確之處。原始文件的母語版本應視為具有權威性的版本。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而導致的任何誤解或曲解負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->