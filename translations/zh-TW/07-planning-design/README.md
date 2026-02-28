[![Planning Design Pattern](../../../translated_images/zh-TW/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(點擊上方圖片觀看本課程影片)_

# 規劃設計

## 介紹

本課程將涵蓋

* 定義清晰的整體目標並將複雜任務拆解為可管理的任務。
* 利用結構化輸出以提供更可靠且機器可讀的回應。
* 採用事件驅動的方式來處理動態任務和意外輸入。

## 學習目標

完成本課程後，您將了解：

* 為 AI 代理識別並設定整體目標，確保其清楚知道須達成的內容。
* 將複雜任務分解為可管理的子任務，並將其組織成邏輯序列。
* 為代理配置適當的工具（例如搜尋工具或數據分析工具）、決定何時以及如何使用它們，以及處理出現的意外情況。
* 評估子任務結果、衡量績效，並反覆調整行動以改善最終輸出。

## 定義整體目標與拆解任務

![Defining Goals and Tasks](../../../translated_images/zh-TW/defining-goals-tasks.d70439e19e37c47a.webp)

大多數現實世界的任務太複雜，無法一步完成。AI 代理需要一個簡潔的目標來指導其規劃和行動。例如，考慮以下目標：

    「生成 3 天的旅遊行程。」

雖然目標簡單明確，但仍需進一步細化。目標越清楚，代理（以及任何人類協作者）就越能專注於達成正確的成果，例如創建包含航班選項、飯店推薦和活動建議的完整行程。

### 任務拆解

將大型或複雜任務拆分成較小的、以目標為導向的子任務，更易於管理。
以旅遊行程為例，您可以將目標分解為：

* 航班預訂
* 飯店預訂
* 租車
* 個人化需求

接著，各子任務可以交給專責代理或流程處理。一個代理專門搜尋最佳航班優惠，另一個負責飯店預訂，依此類推。最後，一個協調或「下游」代理將這些結果整合為完整行程呈現給用戶。

此模組化方法也方便逐步增強。例如，您可以新增美食推薦或本地活動建議的專責代理，並隨時間優化行程。

### 結構化輸出

大型語言模型（LLM）可生成結構化輸出（例如 JSON），讓下游代理或服務更容易解析與處理。這在多代理情境中特別有用，因為我們能在收到規劃輸出後執行這些任務。

以下 Python 程式碼範例示範了簡單的規劃代理如何將目標拆解成子任務，並產生一個結構化計劃：

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
    assigned_agent: AgentEnum  # 我們想將任務分配給代理人

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

### 多代理協調的規劃代理

本範例中，一個語意路由代理接收使用者請求（例如：「我需要一個旅遊飯店方案。」）。

規劃者接著：

* 接收飯店方案：規劃者根據系統提示（包括可用代理清單）和使用者訊息，產生結構化的旅遊計劃。
* 列出代理及其工具：代理登錄表包含代理清單（如航班、飯店、租車及活動代理）及其可用函數或工具。
* 將計劃路由至相應代理：依子任務數量，規劃者會將訊息直接發送給專責代理（單任務情境）或透過群組聊天管理器協調多代理合作。
* 彙整結果摘要：最後，規劃者將產生的計劃概要呈現以利清晰理解。
以下 Python 程式碼展示這些步驟：

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
    assigned_agent: AgentEnum # 我們想將任務分配給代理

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

# 將回應內容載入為 JSON 後列印出來

pprint(json.loads(response_content))
```

接下來範例展示前述程式碼產生的輸出，您可以使用這結構化結果傳送至 `assigned_agent`，並將旅遊計劃摘要回報給最終用戶。

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

您可於 [這裡](07-python-agent-framework.ipynb) 找到包含上述程式碼範例的筆記本範例。

### 迭代規劃

某些任務需要反覆溝通或重新規劃，當子任務結果影響下一步時特別如此。例如，代理在預訂航班時發現意料之外的資料格式，可能需要調整策略後才繼續訂飯店事宜。

此外，使用者回饋（例如有人決定選擇較早的航班）也會觸發部分重新規劃。這種動態且迭代的方式確保最終方案符合真實限制和持續變化的使用者偏好。

例如程式碼

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. 與先前代碼相同，並傳遞使用者歷史記錄、當前方案

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
# .. 重新規劃並將任務分配給相應的代理者
```

若欲進行更全面的規劃，可參考 Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">部落格文章</a>，探討其解決複雜任務的方法。

## 摘要

本文示範如何創建一個能動態選擇可用代理的規劃者。規劃者的輸出拆解任務並指派代理，使其能執行相應工作。假設代理能存取執行任務所需的函數/工具。除了代理外，您還可加入其他模式，例如反思、摘要器和循環聊天等，以進一步自訂。

## 額外資源

Magentic One 是一個通用多代理系統，專門用於解決複雜任務，並在多個具挑戰性的代理標竿測試中取得卓越成果。參考資料：<a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>。此系統的協調者會建立任務專屬計劃，並將任務委派給可用代理。除了規劃外，協調者還會使用追蹤機制監控任務進度，並依需要重新規劃。

### 想了解更多關於規劃設計模式的問題？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ，與其他學習者交流、參加辦公時間，並獲得 AI 代理相關問題的解答。

## 上一課

[建立可信賴的 AI 代理](../06-building-trustworthy-agents/README.md)

## 下一課

[多代理設計模式](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。我們雖盡力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。文件原文應視為權威且具法定效力的版本。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->