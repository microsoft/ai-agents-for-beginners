[![Planning Design Pattern](../../../translated_images/zh-MO/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(點擊上方圖片觀看本課程影片)_

# 規劃設計

## 介紹

本課程將涵蓋

* 定義明確的整體目標並將複雜任務拆解為可管理的子任務。
* 利用結構化輸出來獲得更可靠且機器可讀的回應。
* 採用事件驅動方式來處理動態任務與意外輸入。

## 學習目標

完成本課後，您將了解：

* 識別並設定 AI 代理的整體目標，確保其明確知道需達成的事項。
* 將複雜任務分解為可管理的子任務並組織成合邏輯的順序。
* 配備代理所需的工具（如搜尋工具或資料分析工具）、決定何時及如何使用，並處理突發狀況。
* 評估子任務成果、衡量效能，並依據行動不斷迭代改善最終輸出。

## 定義整體目標與任務拆解

![Defining Goals and Tasks](../../../translated_images/zh-MO/defining-goals-tasks.d70439e19e37c47a.webp)

大多數現實任務複雜度過高，無法一步完成。AI 代理需要一個簡潔的目標來指引其規劃與行動。例如以下目標：

    "生成三天旅遊行程表。"

雖然這目標簡單陳述，但仍需細化。目標越清晰，代理（及任何人類協作者）越能專注於達成正確成果，例如創建包含航班選項、飯店推薦和活動建議的完整行程。

### 任務拆解

將龐大或複雜任務拆解為較小、目標導向的子任務能使其更可管理。
以旅遊行程為例，可以將目標拆解為：

* 訂機票
* 訂飯店
* 租車
* 個人化需求

每個子任務可由專門代理或流程負責。某代理可能專門搜尋最佳機票優惠，另一個專注飯店訂房，依此類推。再由一個協調或「下游」代理彙整這些結果，提供給終端用戶一個完整行程。

此模組化方法也方便逐步增強。例如，可以新增專門負責餐飲推薦或本地活動建議的代理，並隨時間精進行程。

### 結構化輸出

大型語言模型（LLM）可產生結構化輸出（如 JSON），這讓下游代理或服務更易解析與處理。此技術在多代理場景尤其有用，因為在接收規劃輸出後即可執行相關任務。

以下 Python 範例示範一個簡單的規劃代理如何將目標拆解為子任務並產生結構化計畫：

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.foundry import FoundryChatClient
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
    assigned_agent: AgentEnum  # 我們想要分配任務給代理人

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

### 具多代理協作的規劃代理

此範例中，語義路由代理接收使用者請求（例如「我需要旅遊飯店計畫。」）。

規劃者的步驟如下：

* 接收飯店計畫：規劃者根據系統提示（含可用代理細節）利用使用者訊息，產生結構化旅遊計畫。
* 列出代理與其工具：代理註冊表包含代理清單（如負責機票、飯店、租車與活動者）及其功能或工具。
* 將計畫路由至相應代理：依子任務數量，規劃者要麼直接發訊息給單一代理（單任務情境），要麼透過群組聊天管理器協調多代理協作。
* 總結結果：最後，規劃者對產生的計畫進行摘要以便清楚呈現。
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
    assigned_agent: AgentEnum # 我們想將任務指派給代理

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# 創建客戶端

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

下方是前述程式的輸出，您可利用此結構化輸出路由至 `assigned_agent`，並將旅遊計畫摘要給終端用戶。

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

範例筆記本含以上程式碼，請參閱 [這裡](./code_samples/07-python-agent-framework.ipynb)。

### 迭代式規劃

有些任務需要反覆溝通或重新規劃，其中一個子任務的結果會影響下一個。例如，代理在訂機票時遇到意外資料格式，可能需改變策略後才能繼續到飯店訂房階段。

此外，使用者反饋（例如人類決定偏好較早航班）也能觸發部分重新規劃。這種動態迭代方式保證最終解決方案符合現實限制及持續變化的使用者偏好。

例如範例程式碼

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. 同前一段代碼，並傳遞用戶歷史記錄、當前計劃

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
# .. 重新規劃並將任務發送給各自的代理人
```

欲進行更完整規劃，請參考 Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> 以解決複雜任務。

## 摘要

本文探討示範如何創建一個能動態選擇定義代理的規劃者。規劃者輸出拆解任務並分派代理以執行。假設代理可使用所需功能與工具。除了代理，還可包含反思、摘要和輪詢聊天等模式來進一步自訂。

## 額外資源

Magnetic One — 一個通才型多代理系統，能解決複雜任務並在多項具挑戰性的代理基準測試中取得優異成績。參考資料：<a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>。此實作中，協調器建立任務專屬規劃並將任務委派給可用代理。協調器除規劃外，還運用追蹤機制監控任務進展並依需求重新規劃。

### 對規劃設計模式有更多疑問嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，與其他學習者交流，參加諮詢時段，並獲得 AI 代理相關問題解答。

## 前一課

[建構值得信賴的 AI 代理](../06-building-trustworthy-agents/README.md)

## 下一課

[多代理設計模式](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->