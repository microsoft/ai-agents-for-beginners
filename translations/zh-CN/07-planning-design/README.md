[![规划设计模式](../../../translated_images/zh-CN/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(点击上方图片观看本课视频)_

# 规划设计

## 介绍

本课内容包括

* 明确总体目标并将复杂任务拆分为可管理的子任务。
* 利用结构化输出实现更可靠且机器可读的响应。
* 采用事件驱动方法处理动态任务和意外输入。

## 学习目标

完成本课后，您将了解：

* 识别并设定AI代理的总体目标，确保其明确知道需实现的内容。
* 将复杂任务分解为可管理的子任务，并按逻辑顺序组织它们。
* 为代理配备合适工具（如搜索工具或数据分析工具），决定何时及如何使用，并处理意外情况出现。
* 评估子任务结果，衡量绩效，并迭代操作以改进最终输出。

## 定义总体目标与任务拆分

![定义目标与任务](../../../translated_images/zh-CN/defining-goals-tasks.d70439e19e37c47a.webp)

大多数现实世界任务过于复杂，无法一步完成。AI代理需要简明目标来指导其规划和行动。例如，设定目标：

    “生成一个三天的旅游行程。”

虽然表述简单，但仍需细化。目标越清晰，代理（及任何人类协作者）就越能专注实现正确结果，如创建包含航班选项、酒店推荐和活动建议的完整行程。

### 任务拆分

将大型或复杂任务拆分成更小、更具目标性的子任务可提升可管理性。
针对旅游行程示例，您可以将目标拆分为：

* 机票预订
* 酒店预订
* 租车服务
* 个性化定制

然后由专门代理或流程处理各子任务。比如，一个代理专注搜索最佳机票，一个负责酒店预订，等等。最后由协调或“下游”代理将这些结果汇总，向最终用户提供完整行程。

这种模块化方式还便于逐步增强。例如，您可以增加专门负责美食推荐或本地活动建议的代理，随时间改进行程。

### 结构化输出

大型语言模型（LLM）能生成结构化输出（如JSON），便于下游代理或服务解析处理。在多代理场景中特别有用，可在接收规划输出后执行相应任务。

以下Python代码示例展示了一个简单规划代理如何将目标拆分为子任务并生成结构化计划：

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

# 旅行子任务模型
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # 我们想要将任务分配给代理

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

此示例中，语义路由代理接收用户请求（如“我需要我的旅行酒店计划。”）。

规划者则：

* 接收酒店计划：规划者依据用户消息及系统提示（包括可用代理详情），生成结构化旅游计划。
* 列出代理及其工具：代理注册表包含代理列表（如机票、酒店、租车、活动）及其提供的函数或工具。
* 将计划路由至相应代理：根据子任务数量，规划者要么直接发送消息给专用代理（单任务场景），要么通过群聊管理器协调多代理协作。
* 汇总结果：最终，规划者汇总生成计划以便清晰呈现。
以下Python代码示例说明了这些步骤：

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
    assigned_agent: AgentEnum # 我们想将任务分配给代理

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# 创建客户端

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# 定义用户消息

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

下方为前述代码的输出，您可利用此结构化输出将任务路由至`assigned_agent`，并向最终用户总结行程计划。

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

含上述代码示例的笔记本范例可在 [这里](07-python-agent-framework.ipynb) 获取。

### 迭代规划

部分任务需来回调整或重新规划，因一子任务结果会影响下一步。如代理在预订机票时发现意外数据格式，可能需要先调整策略再继续处理酒店预订。

此外，用户反馈（如人类决定更早的航班）可触发部分重新规划。这种动态迭代方式确保最终方案符合现实限制及不断变化的用户偏好。

示例代码

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. 与之前的代码相同，并传递用户历史、当前计划

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
# .. 重新规划并将任务发送给各自的代理
```

想要更全面的规划，请查看Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">博客文章</a>，了解其解决复杂任务的方案。

## 总结

本文示例展示了如何创建一个规划者，能够动态选择定义的可用代理。规划者输出将任务拆分并分配代理执行。假设代理可访问完成任务所需的函数/工具。除代理外，还可包括反思、摘要、轮询聊天等模式以实现更细致定制。

## 额外资源

Magnetic One —— 一个用于解决复杂任务的通用多代理系统，在多个挑战性的代理基准测试中取得了优异成绩。参考：<a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>。该实现中，编排者创建特定任务计划并委派给可用代理，此外还采用跟踪机制监控任务进展并根据需要调整规划。

### 关于规划设计模式还有疑问？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，与其他学习者交流，参加答疑时段，解决您的AI代理相关问题。

## 前一课

[构建可信赖的AI代理](../06-building-trustworthy-agents/README.md)

## 下一课

[多代理设计模式](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件采用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。原文文件及其原始语言版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->