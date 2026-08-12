[![規劃設計模式](../../../translated_images/zh-TW/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(點擊上方圖片觀看本課程影片)_

# 規劃設計

## 介紹

本課程將涵蓋

* 定義清晰的整體目標並將複雜任務拆分成可管理的任務。
* 利用結構化輸出以獲得更可靠且適合機器閱讀的回應。
* 採用事件驅動方法來處理動態任務及意外輸入。

## 學習目標

完成本課後，你將了解：

* 識別並設定 AI 代理的整體目標，確保其清楚了解需要達成的目標。
* 將複雜任務拆解為可管理的子任務，並將其組織成合乎邏輯的順序。
* 配備代理所需的合適工具（例如搜尋工具或數據分析工具），決定何時及如何使用，並處理意外情況。
* 評估子任務結果、衡量績效，並反覆調整行動以改進最終成果。

## 定義整體目標與拆解任務

![目標與任務定義](../../../translated_images/zh-TW/defining-goals-tasks.d70439e19e37c47a.webp)

大多數真實世界的任務過於複雜，無法一步完成。AI 代理需要一個簡潔的目標來指導其規劃與行動。例如，考慮以下目標：

    「生成三天的旅遊行程規劃。」

雖然目標簡單明確，但仍需精煉。目標越清晰，代理（及任何人類協作者）越能專注於達到正確的成果，例如建立包含航班選擇、飯店推薦和活動建議的完整行程。

### 任務拆解

將大型或複雜任務拆分為較小、目標導向的子任務會更容易管理。
以旅遊行程為例，你可以將目標拆解成：

* 航班預訂
* 飯店預訂
* 租車服務
* 個人化需求

每個子任務可由專責的代理或流程處理。一個代理可能專門尋找最佳航班優惠，另一個專注於飯店預訂，如此類推。一個協調者或「下游」代理則會將這些結果彙整成一份完整的行程提供給終端用戶。

這種模組化方法亦可逐步增強。例如，你可以增加專門針對美食推薦或當地活動建議的代理，並隨時間優化行程。

### 結構化輸出

大型語言模型（LLM）可以產生結構化輸出（如 JSON），方便下游代理或服務解析與處理。這在多代理情境中特別有用，我們可以在獲得規劃輸出後執行這些任務。

以下 Python 範例示範一個簡單的規劃代理如何將目標拆解為子任務並生成結構化計劃：

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
    assigned_agent: AgentEnum  # 我們想要把任務分配給代理人

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

### 多代理協調的規劃代理

在此範例中，一個語意路由代理接收使用者請求（例如「我需要我的旅行飯店規劃」）。

接著規劃者會：

* 接收飯店規劃：規劃者根據系統提示（包含可用代理資訊），從用戶訊息產生結構化旅遊規劃。
* 列出代理與其工具：代理登記表列出多個代理（如航班、飯店、租車及活動）及其提供的功能或工具。
* 路由規劃至相應代理：視子任務數量，規劃者直接發送訊息給專責代理（單一任務場景）或透過群組聊天室管理器協調多代理合作。
* 彙整結果摘要：最後，規劃者為生成的計劃做簡要總結。
以下 Python 範例說明上述步驟：

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

# 以 JSON 載入後列印回應內容

pprint(json.loads(response_content))
```

接下來是前段程式碼的輸出結果，您可以使用此結構化輸出路由至 `assigned_agent`，並將旅遊規劃彙整摘要給終端用戶。

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

可於此處 [範例筆記本](./code_samples/07-python-agent-framework.ipynb) 取得完整前述程式碼範例。

### 反覆規劃

有些任務需進行多次往返或重新規劃，其中一個子任務的結果會影響下一步。例如，代理在訂航班時若發現意外的資料格式，可能得先調整策略，再繼續飯店訂房。

此外，使用者回饋（如人員決定改訂較早航班）也可能觸發部分重規劃。此動態反覆方法確保最終方案貼合實際限制及不斷變動的使用者偏好。

例：範例程式碼

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. 與之前的代碼相同，並傳遞用戶歷史和當前計劃

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

想要更完整規劃可參考 Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">博客文章</a>，專為解決複雜任務而設的通用多代理系統。

## 總結

本文展示了如何建立可動態選擇定義中代理的規劃者。規劃者輸出將任務拆解並指派代理執行，假設代理具備執行任務所需的功能/工具。除代理外，你還可以結合反思、摘要以及輪流聊天等模式做進一步定制。

## 其他資源

Magentic One - 一般性多代理系統，可解決複雜任務，並在多個挑戰性代理基準中取得優異表現。參考資料：<a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>。實作中，協調者會製作任務專屬計劃並將任務委派給可用代理，此外，亦有追蹤機制監控任務進度並於必要時重新規劃。

### 對規劃設計模式有更多疑問嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者交流，參加辦公時間，並解決你的 AI 代理問題。

## 上一課

[建立值得信賴的 AI 代理](../06-building-trustworthy-agents/README.md)

## 下一課

[多代理設計模式](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->