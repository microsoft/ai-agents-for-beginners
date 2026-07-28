[![规划设计模式](../../../translated_images/zh-CN/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(点击上方图片观看本课视频)_

# 规划设计

## 介绍

本课将涵盖

* 明确定义整体目标和将复杂任务拆分成可管理的子任务。
* 利用结构化输出实现更可靠且机器可读的响应。
* 采用事件驱动方法处理动态任务和意外输入。

## 学习目标

完成本课后，您将了解：

* 识别并设定AI代理的整体目标，确保其清晰知道需要完成的任务。
* 将复杂任务拆解成可管理的子任务并按逻辑顺序组织。
* 装备代理合适的工具（如搜索工具或数据分析工具），决定何时及如何使用，并处理意外情况。
* 评估子任务结果，衡量性能，并迭代行动以提升最终输出。

## 定义整体目标及拆解任务

![定义目标与任务](../../../translated_images/zh-CN/defining-goals-tasks.d70439e19e37c47a.webp)

现实中的大多数任务过于复杂，无法通过一步完成。AI代理需要一个简明的目标来指导其规划和行动。例如，考虑这个目标：

    “生成一份三天的旅行行程。”

虽然这个目标简单，但仍需细化。目标越明确，代理（及任何人类协作者）就越能专注于实现正确的结果，比如创建包含航班选项、酒店推荐和活动建议的全面行程。

### 任务拆解

将大型或复杂任务拆成更小的有目标子任务后，更易管理。
对于旅行行程示例，可以将目标拆分为：

* 机票预订
* 酒店预订
* 租车
* 个性化定制

每个子任务可以由专门的代理或流程处理。一个代理可能专门负责搜索最佳机票，另一个专注于酒店预订等。协调或“下游”代理可以将结果汇总成一份完整的行程提供给用户。

这种模块化方法也便于逐步增强。例如，可以添加专门的美食推荐或本地活动建议代理，并随着时间推进行程优化。

### 结构化输出

大语言模型（LLM）能够生成结构化输出（如JSON），使下游代理或服务更易解析和处理。这在多代理上下文中特别有用，我们可以在规划输出完成后执行相应任务。

以下Python代码演示了一个简单的规划代理如何拆解目标为子任务并生成结构化计划：

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

# 旅行子任务模型
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # 我们想把任务分配给代理

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# 定义用户消息
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

### 多代理编排的规划代理

示例中，一个语义路由代理接收用户请求（例如，“我需要一份旅行酒店计划。”）。

然后规划者执行：

* 接收酒店计划：规划者根据系统提示（含可用代理详情）处理用户消息，生成结构化的旅行计划。
* 列出代理及其工具：代理注册表包含代理列表（如机票、酒店、租车和活动代理）及其功能或工具。
* 路由计划给相应代理：根据子任务数量，规划者或将消息直接发给专门代理（单任务场景），或通过群聊管理器协调多代理协作。
* 总结结果：最后规划者总结生成的计划以便清晰展示。
以下Python代码示例展示了这些步骤：

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

# 旅行子任务模型

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # 我们想把任务分配给代理

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# 创建客户端

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# 定义用户信息

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

# 加载为JSON后打印响应内容

pprint(json.loads(response_content))
```

接下来是上述代码的输出，您可以利用该结构化输出路由到`assigned_agent`，并向最终用户汇总旅行计划。

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

之前代码示例的笔记本可在[这里](./code_samples/07-python-agent-framework.ipynb)获取。

### 迭代规划

有些任务需要来回调整或重新规划，一个子任务的结果会影响下一个。例如，代理在预订机票时发现意外的数据格式，可能需先调整策略再进行酒店预订。

此外，用户反馈（例如用户决定更早的航班）也会触发部分重新规划。这种动态迭代方法保证最终解决方案符合现实约束及不断变化的用户偏好。

示例代码

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. 与之前的代码相同，并传递用户历史记录、当前计划

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
# .. 重新规划并将任务发送给相应的代理
```

若想实现更全面的规划，可查看<a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One 博文</a>，了解复杂任务解决方案。

## 小结

本文示例了如何创建一个动态选择已定义代理的规划器。规划器输出分解任务并分配代理执行，假定代理可访问完成任务所需的函数/工具。除代理外，还可引入反思、总结和轮询聊天等模式以进一步定制。

## 额外资源

Magnetic One - 一款通用多代理系统，用于解决复杂任务，在多个挑战性代理基准测试中取得出色成绩。参考：<a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>。此实现中，编排者创建特定任务计划并将任务委派给可用代理。除了规划外，编排者还采用跟踪机制监控任务进度并根据需要重新规划。

### 有更多关于规划设计模式的问题吗？

加入[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，与其他学习者交流，参加答疑时间，解决您的AI代理问题。

## 上一课

[构建可信赖的AI代理](../06-building-trustworthy-agents/README.md)

## 下一课

[多代理设计模式](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->