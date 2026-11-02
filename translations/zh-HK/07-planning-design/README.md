[![Planning Design Pattern](../../../translated_images/zh-HK/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(點擊上方圖片觀看本課堂影片)_

# 規劃設計

## 介紹

本課程將涵蓋

* 定義明確的整體目標並將複雜任務拆解為可管理的任務。
* 利用結構化輸出以獲得更可靠且機器可讀的回應。
* 採用事件驅動方式應對動態任務和意外輸入。

## 學習目標

完成本課程後，你將了解：

* 識別並設定 AI 代理的整體目標，確保其清楚了解需要達成的事項。
* 將複雜任務拆分為可管理的子任務並將其組織為合邏輯的順序。
* 為代理配備適當的工具（如搜尋工具或數據分析工具），並決定其使用時機與方式，且應對意外狀況。
* 評估子任務成果、衡量效能，並對行動進行迭代以提升最終輸出。

## 定義整體目標與任務拆解

![定義目標與任務](../../../translated_images/zh-HK/defining-goals-tasks.d70439e19e37c47a.webp)

大多數現實任務過於複雜，無法一步完成。AI 代理需要一個簡明的目標來指導其規劃與行動。例如，考慮目標：

    "產生一個三天的旅遊行程。"

雖然敘述簡單，但仍需細化。目標越清晰，代理（及任何人類協作者）越能專注於達成正確成果，例如建立包含航班選項、住宿推薦和活動建議的完整行程。

### 任務拆解

大型或複雜任務透過拆解為較小、以目標為導向的子任務，可以更易於管理。
以旅遊行程為例，你可以將目標拆解為：

* 航班預訂
* 酒店預訂
* 租車
* 個人化需求

然後每個子任務可由專責代理或流程處理。有代理專注於搜尋最佳航班優惠，另一個負責酒店預訂，以此類推。一個協調或「下游」代理則整合這些結果，向最終使用者呈現一個完整行程。

此模組化方法也允許逐步增強。例如，你可以新增專門的代理負責美食推薦或本地活動建議，並隨時間調整行程。

### 結構化輸出

大型語言模型（LLMs）可產生結構化輸出（例如 JSON），下游代理或服務更易分析與處理。這在多代理場景中特別有用，我們可在取得規劃輸出後立即執行相關任務。

以下 Python 範例展示了一個簡單規劃代理將目標拆解為子任務並產生結構化計劃的流程：

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

# 旅行子任務模型
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # 我們想將任務分配給代理

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# 定義用戶信息
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

在此範例中，語意路由代理接收使用者需求（例如「我需要一份旅遊酒店計劃。」）。

規劃者接著：

* 接收酒店計劃：規劃者根據系統提示（包含可用代理細節）生成結構化旅遊計劃。
* 列出代理與其工具：代理註冊表包含代理清單（如航班、酒店、租車與活動）及其功能或工具。
* 路由計劃給對應代理：依子任務數量，規劃者或直接發送訊息給專責代理（單任務情境），或透過群組聊天管理員協調多代理合作。
* 彙整結果：最終，規劃者對產生計劃進行摘要說明以增進清晰度。
以下 Python 範例程式碼示範這些步驟：

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

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# 建立客戶端

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

# 在將回應內容載入為 JSON 後列印出來

pprint(json.loads(response_content))
```

接下來是上一段程式的輸出，你可以使用此結構化輸出將任務分派給 `assigned_agent` 並向最終用戶總結旅遊計劃。

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

先前程式範例的筆記本示例可於[此處](./code_samples/07-python-agent-framework.ipynb)取得。

### 迭代規劃

某些任務需要來回溝通或重新規劃，其中一個子任務結果會影響下一步。例如，代理在預訂航班時發現意外的資料格式，可能得先調整策略，才能繼續安排酒店預訂。

此外，使用者回饋（如有人決定偏好較早航班）也會觸發部分重新規劃。這種動態、迭代方法可確保最終方案符合現實限制與不斷變化的使用者偏好。

例如範例程式碼

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. 同以前嘅代碼一樣，並傳遞用戶歷史、當前計劃

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
# .. 重新計劃並將任務發送到相應嘅代理
```

若需更全面的規劃，請參見 Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">部落格文章</a>，介紹其用於解決複雜任務的系統。

## 小結

本文展示了如何創建一個能動態選擇已定義代理的規劃器。規劃器的輸出將任務拆解並分派給代理執行，前提是假設代理具備執行任務所需功能／工具。除代理外，你還能結合反思模式、摘要器和循環聊天等方式進一步自訂。

## 附加資源

Magnetic One - 一個通用多代理系統，用於解決複雜任務，在多個挑戰性代理基準測試中取得傑出成果。參考資料：<a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>。本實作的協調者會創建特定任務計劃並將任務委派給可用代理。此外，協調者還會採用追蹤機制監控任務進度並按需重新規劃。

### 對規劃設計模式有更多問題嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，與其他學習者交流，參加辦公時間，並獲得 AI 代理相關問題的解答。

## 上一課

[打造可信賴的 AI 代理](../06-building-trustworthy-agents/README.md)

## 下一課

[多代理設計模式](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->