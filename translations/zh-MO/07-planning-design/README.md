[![Planning Design Pattern](../../../translated_images/zh-MO/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(點擊上方圖片觀看本課程視頻)_

# 規劃設計

## 簡介

本課程將涵蓋

* 定義明確的整體目標，並將複雜任務拆分成可管理的子任務。
* 利用結構化輸出來獲得更可靠及機器可讀的回應。
* 採用事件驅動方法處理動態任務及意外輸入。

## 學習目標

完成本課程後，您將了解：

* 為 AI 代理識別並設定整體目標，確保其清楚知道需要達成的事項。
* 將複雜任務拆解成可管理的子任務，並組織成邏輯順序。
* 配備代理適當的工具（例如搜尋工具或數據分析工具）、決定何時及如何使用，並處理突發情況。
* 評估子任務結果、測量效能，並針對行動進行調整以改善最終輸出。

## 定義整體目標及拆解任務

![Defining Goals and Tasks](../../../translated_images/zh-MO/defining-goals-tasks.d70439e19e37c47a.webp)

大部分現實世界的任務太過複雜，無法一氣呵成。AI 代理需要一個簡潔的目標來引導其規劃與行動。例如，考慮以下目標：

    "產生一個三日旅遊行程。"

雖然簡單易述，但仍需精煉。目標越明確，代理（與任何人類協作者）越能專注於達成正確的成果，例如制定全面的行程，包括航班選項、酒店推薦與活動建議。

### 任務拆解

大型或複雜的任務拆分成更小目標導向的子任務後更易處理。
以旅遊行程為例，您可以將目標拆解為：

* 航班預訂
* 酒店預訂
* 租車服務
* 個人化推薦

每個子任務可由專門的代理或流程負責。一個代理可能專攻搜尋最佳航班優惠，另一個聚焦酒店預訂，依此類推。然後由協調或「下游」代理將這些結果彙整成一個完整的行程供最終用戶使用。

此模組化方法亦利於逐步改進。例如，您可以新增專門針對餐飲推薦或當地活動建議的代理，並隨時間調整行程。

### 結構化輸出

大型語言模型（LLMs）可生成結構化輸出（例如 JSON），方便下游代理或服務解析與處理。這在多代理環境中特別有用，因為我們可以在規劃輸出收到後執行這些任務。

以下 Python 範例展示簡單的規劃代理將目標拆解成子任務並生成結構化計劃：

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

# 旅行子任務模型
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # 我們想將任務分配給代理

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

### 多代理協同的規劃代理

在此範例中，一個語義路由代理接收使用者請求（例如，「我需要旅遊的酒店計劃。」）。

規劃者接著：

* 接收酒店計劃：根據系統提示（包含可用代理詳情），規劃者會從使用者訊息生成結構化的旅遊計劃。
* 列出代理及其工具：代理註冊表持有各代理列表（例如航班、酒店、租車及活動）及其提供的功能或工具。
* 將計劃路由給相應代理：依子任務數量，規劃者會直接將訊息發送予專門代理（單一任務情況），或透過群組聊天管理器協調多代理合作。
* 彙整結果：最後，規劃者會總結生成的計劃以利清晰呈現。
以下 Python 範例程式碼展示這些步驟：

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
    assigned_agent: AgentEnum # 我哋想安排呢個任務俾代理人

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

# 載入為 JSON 後列印回應內容

pprint(json.loads(response_content))
```

下面是前述程式的輸出，您可利用此結構化輸出路由到`assigned_agent`，並將旅遊計劃彙整展示給最終用戶。

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

範例筆記本連結可參考[此處](07-python-agent-framework.ipynb)。

### 迭代式規劃

某些任務要求來回反覆或重新規劃，上一子任務的結果會影響下一步。例如代理在訂票時遇到意外的資料格式，需要調整策略後再繼續處理酒店預訂。

另外，使用者反饋（例如人類決定偏好較早航班）也可能觸發部分重新規劃。這種動態且迭代的策略能確保最終方案符合現實限制和不斷變化的使用者偏好。

範例程式碼

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. 同之前嘅代碼一樣，並傳遞用戶歷史記錄，同當前方案

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
# .. 重新規劃並將任務分派畀相應嘅代理
```

欲深入規劃，歡迎參考 Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">部落格文章</a>，介紹解決複雜任務的方法。

## 總結

本文示範如何建立可動態選擇已定義代理的規劃器。規劃器的輸出將任務拆分並指派給適用代理執行。假設代理擁有執行任務所需的函數/工具。除代理外，您亦能加入反思、總結以及輪流聊天等模式進行更自訂化設計。

## 附加資源

Magentic One - 一個通用多代理系統，用以解決複雜任務，並於多項挑戰性代理基準測試中取得優異成果。參考：<a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>。此實作中，協調器會規劃特定任務計劃並委派給可用代理。此外，協調者還會監控任務進展並視情況重新規劃。

### 對規劃設計模式有更多問題嗎？

歡迎加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，與其他學習者交流，參與開放諮詢時段並獲得 AI 代理相關問題解答。

## 上一課程

[建立可信賴的 AI 代理](../06-building-trustworthy-agents/README.md)

## 下一課程

[多代理設計模式](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們盡力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原文及其母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。本服務對因使用本翻譯而引起之任何誤解或誤釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->