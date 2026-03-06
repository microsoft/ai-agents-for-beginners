[![規劃設計模式](../../../translated_images/zh-HK/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(點擊上方圖片以觀看本課的影片)_

# 規劃設計

## 簡介

本課會涵蓋

* 設定清晰的整體目標，並將複雜任務拆分為可管理的小任務。
* 利用結構化輸出以獲得更可靠、機器可讀的回應。
* 應用事件驅動的方法來處理動態任務與未預期的輸入。

## 學習目標

完成本課後，你將了解：

* 為 AI 代理設定並辨識整體目標，確保其清楚知道需要達成的事項。
* 將複雜任務分解為可管理的子任務，並將它們組織成邏輯性的執行順序。
* 為代理配備適當的工具（例如搜尋工具或資料分析工具），並決定何時以及如何使用這些工具，同時處理出現的意外情況。
* 評估子任務結果、衡量效能，並透過反覆調整行動以改進最終輸出。

## 定義整體目標與將任務拆解

![定義目標與任務](../../../translated_images/zh-HK/defining-goals-tasks.d70439e19e37c47a.webp)

大多數現實世界的任務過於複雜，無法以單一步驟完成。AI 代理需要一個簡明的目標來引導其規劃與行動。例如，考慮以下目標：

    "生成一個為期3天的旅遊行程。"

雖然陳述簡單，但仍需細化。目標越清晰，代理（以及任何人類協作者）就越能專注於達成正確的結果，例如建立包含航班選項、酒店推薦與活動建議的完整行程。

### 任務拆解

當大型或複雜的任務被拆分為較小、以目標為導向的子任務時，會變得較易處理。
以旅遊行程為例，你可以將目標拆解為：

* 機票預訂
* 酒店預訂
* 租車
* 個人化

然後，各子任務可以由專門的代理或流程來處理。一個代理可能專攻搜尋最佳機票優惠，另一個則專注於酒店預訂，如此類推。最後，一個協調或「下游」代理可以將這些結果彙整為一個統一的行程提供給最終使用者。

這種模組化的方法也允許逐步增強。例如，你可以加入專門負責餐飲推薦或當地活動建議的代理，並隨時間細化行程。

### 結構化輸出

大型語言模型（LLM）可以產生結構化輸出（例如 JSON），讓下游代理或服務更容易解析與處理。這在多代理情境中特別有用，因為在收到規劃輸出後，我們可以據此執行這些任務。

下列 Python 範例展示一個簡單的規劃代理，將目標拆解為子任務並生成結構化計劃：

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# 旅遊子任務模型
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # 我們想把任務指派給代理人

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# 定義用戶訊息
system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text
pprint(json.loads(response_content))
```

### 具有多代理協調的規劃代理

在這個範例中，一個 Semantic Router Agent 接收到使用者請求（例如：「我需要一個旅程中的酒店規劃。」）。

規劃器接著會：

* 接收酒店計劃：規劃器接收使用者的訊息，並根據系統提示（包括可用代理的相關細節）產生一個結構化的旅遊計劃。
* 列出代理和其工具：代理註冊表包含代理清單（例如負責機票、酒店、租車與活動的代理）以及它們提供的功能或工具。
* 將計劃路由到相應代理：視子任務數量，規劃器要麼直接將訊息傳送給專門的代理（單一任務情況），要麼透過群組聊天管理器協調多代理協作。
* 總結結果：最後，規劃器會總結所產生的計劃以便說明。
下列 Python 範例程式碼說明這些步驟：

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# 旅遊子任務模型

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # 我們想把任務指派畀代理

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# 建立客戶端

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# 定義用戶訊息

system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text

# 將回應內容載入為 JSON 後列印

pprint(json.loads(response_content))
```

下方為前述程式的輸出，接著你可以使用此結構化輸出路由到 `assigned_agent` 並將旅遊計劃摘要給終端使用者。

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

上述程式範例的示例 notebook 可在 [這裡](07-python-agent-framework.ipynb) 取得。

### 迭代規劃

某些任務需要來回互動或重新規劃，其中一個子任務的結果會影響下一步。例如，如果代理在預訂機票時發現意外的資料格式，它可能需要在繼續處理酒店預訂之前調整策略。

此外，使用者回饋（例如人類決定偏好較早的航班）也可能觸發部分重新規劃。這種動態、迭代的方法可確保最終解決方案符合現實世界限制與使用者偏好演進。

例如 範例程式碼

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. 與之前的程式碼相同，並傳遞使用者的歷史記錄及目前計劃

system_prompt = """You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(
    input=user_message,
    instructions=system_prompt,
    context=f"Previous travel plan - {TravelPlan}",
)
# .. 重新規劃，並將任務發送到相應的代理
```

要進行更全面的規劃，請查看 Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">部落格文章</a>，以解決複雜任務。

## 摘要

在本文中，我們看了一個示例，說明如何建立一個可以動態選擇已定義可用代理的規劃器。規劃器的輸出會將任務拆解並指派代理以便執行。假設這些代理可存取執行任務所需的函式/工具。除了代理之外，你還可以加入其他模式，例如反思（reflection）、摘要器（summarizer）與輪詢式聊天（round robin chat）來進一步自訂。

## 其他資源

Magentic One - A Generalist multi-agent system for solving complex tasks and has achieved impressive results on multiple challenging agentic benchmarks. Reference: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. 在此實作中，協調者會建立任務專屬的計劃並將這些任務委派給可用的代理。除了規劃之外，協調者也採用追蹤機制來監控任務進度，並在需要時重新規劃。

### 對規劃設計模式還有更多疑問嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者交流、參加辦公時間，並讓你的 AI 代理問題得到解答。

## 前一課

[建立可信賴的 AI 代理](../06-building-trustworthy-agents/README.md)

## 下一課

[多代理設計模式](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件已使用 AI 翻譯服務 Co‑op Translator（https://github.com/Azure/co-op-translator）進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言的原文應被視為具權威性的來源。若涉及重要資訊，建議採用專業人工翻譯。我們不會對因使用此翻譯而導致的任何誤解或錯誤詮釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->