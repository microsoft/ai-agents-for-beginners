[![Planning Design Pattern](../../../translated_images/zh-TW/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(點擊上方圖片觀看本課程影片)_

# 規劃設計

## 簡介

本課程將涵蓋

* 定義明確的整體目標並將複雜任務拆解為可管理的子任務。
* 利用結構化輸出以獲得更可靠且機器可讀的回應。
* 採用事件驅動的方法來處理動態任務和意外輸入。

## 學習目標

完成本課程後，您將了解：

* 識別並設定 AI 代理的整體目標，確保其明確知道需要達成的事項。
* 將複雜任務拆解為可管理的子任務，並將其組織成邏輯序列。
* 為代理配備合適的工具（例如搜尋工具或數據分析工具），決定何時以及如何使用這些工具，並處理突發情況。
* 評估子任務結果、衡量效能，並迭代行動以改善最終輸出。

## 定義整體目標並拆解任務

![Defining Goals and Tasks](../../../translated_images/zh-TW/defining-goals-tasks.d70439e19e37c47a.webp)

大多數現實世界的任務過於複雜，無法一蹴而就。AI 代理需要一個簡潔的目標來指導其規劃和行動。例如，考慮以下目標：

    「生成一個三天的旅遊行程。」

雖然這個目標表述簡單，但仍需要進一步細化。目標越明確，代理（以及任何人類協作者）就越能專注於達成正確結果，例如創建包含航班選擇、旅館推薦和活動建議的完整行程。

### 任務分解

大型或複雜任務在拆分為較小的、以目標為導向的子任務後會更易於管理。
以旅遊行程為例，您可以將目標拆解為：

* 航班預訂
* 旅館預訂
* 租車
* 個人化設定

每個子任務都可以由專門的代理或流程來處理。一個代理可能專注於搜尋最佳航班優惠，另一個則專注於旅館預訂，如此類推。協調或「下游」代理再將這些結果彙整成一個完整行程給最終用戶。

這種模組化方法也方便逐步優化。例如，您可以新增專門負責食物推薦或當地活動建議的代理，並隨時間細化行程。

### 結構化輸出

大型語言模型（LLM）能生成結構化輸出（例如 JSON），方便下游代理或服務解析和處理。在多代理環境中特別有用，因為我們可以在接收到規劃輸出後執行相關任務。

以下 Python 範例展示了一個簡單規劃代理如何將目標拆解為子任務並生成結構化計畫：

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
    assigned_agent: AgentEnum  # 我們想將任務分配給代理人

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# 定義使用者訊息
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

### 具備多代理協調的規劃代理

此範例中，語義路由代理接收用戶請求（例如「我需要旅行的旅館計畫」）。

規劃者接著：

* 接收旅館計畫：基於系統提示（包括可用代理詳情），規劃者根據用戶消息生成結構化的旅行計畫。
* 列出代理與其工具：代理註冊表包含一份代理清單（例如航班、旅館、租車及活動）及其所提供的功能或工具。
* 將計畫路由給相應代理：依子任務數量，規劃者會直接將消息發送給專門代理（單一任務情況）或透過群組聊天管理器協調多代理合作。
* 總結結果：最後，規劃者總結產生的計畫以便清晰呈現。
以下 Python 程式碼示範這些步驟：

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

# 旅行子任務模型

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # 我們想要將任務分配給代理人

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

# 定義使用者訊息

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

接下來是上面程式碼的輸出，您可以使用該結構化輸出路由至 `assigned_agent`，並向最終用戶總結旅行計畫。

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

包含上述程式碼的範例筆記本可至[這裡](07-python-agent-framework.ipynb)取得。

### 迭代規劃

有些任務需要來回交互或重新規劃，其中一個子任務的結果會影響下一個子任務。例如，代理在預訂航班時發現意外的資料格式，可能需要調整策略後再繼續旅館預訂。

此外，使用者回饋（例如人類決定希望搭乘較早班機）也會觸發部分重新規劃。這種動態、迭代的方法確保最終方案符合現實限制與不斷變化的使用者偏好。

例如範例程式碼

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. 與先前代碼相同，並傳遞使用者歷史、當前計劃

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
# .. 重新規劃並將任務發送給相應的代理
```

若想要更全面的規劃，可參考 Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">部落格文章</a>，探討如何解決複雜任務。

## 總結

本文示範了如何打造一個能動態選擇定義代理的規劃者。規劃者輸出拆解任務並分派代理以執行，假設代理擁有所需的功能/工具來完成任務。除了代理外，您還可以加入像反思、摘要和輪詢聊天等模式，以進一步自訂。

## 其他資源

Magentic One - 一個通用型多代理系統，可解決複雜任務，在多項具挑戰性的代理基準測試中表現優異。參考：<a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>。此實作中，協調者會建立特定任務計畫並將任務委派給可用代理。此外，協調者還會運用追蹤機制監控任務進度，並在必要時重新規劃。

### 想更深入了解規劃設計模式嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，與其他學習者交流、參加辦公時間並獲得 AI 代理相關問題的解答。

## 上一課

[建立值得信賴的 AI 代理](../06-building-trustworthy-agents/README.md)

## 下一課

[多代理設計模式](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為具權威性的參考來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->