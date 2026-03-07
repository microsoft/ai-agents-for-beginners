[![รูปแบบการวางแผน](../../../translated_images/th/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(คลิกที่รูปภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

# การออกแบบการวางแผน

## เกริ่นนำ

บทเรียนนี้จะครอบคลุม

* การกำหนดเป้าหมายโดยรวมที่ชัดเจนและการแยกงานที่ซับซ้อนออกเป็นงานย่อยที่จัดการได้
* การใช้ผลลัพธ์ที่มีโครงสร้างเพื่อให้ได้คำตอบที่เชื่อถือได้และอ่านโดยเครื่องได้ง่ายขึ้น
* การนำแนวทางขับเคลื่อนด้วยเหตุการณ์มาใช้เพื่อจัดการงานที่เปลี่ยนแปลงได้และข้อมูลนำเข้าที่ไม่คาดคิด

## จุดมุ่งหมายการเรียนรู้

หลังจากเรียนบทเรียนนี้ คุณจะเข้าใจเกี่ยวกับ:

* ระบุและตั้งเป้าหมายโดยรวมสำหรับเอเยนต์ AI เพื่อให้แน่ใจว่าเข้าใจอย่างชัดเจนว่าต้องบรรลุอะไร
* แยกงานที่ซับซ้อนออกเป็นงานย่อยที่จัดการได้และจัดเรียงเป็นลำดับเชิงตรรกะ
* เตรียมเครื่องมือที่เหมาะสมให้กับเอเยนต์ (เช่น เครื่องมือค้นหา หรือเครื่องมือวิเคราะห์ข้อมูล) ตัดสินใจว่าจะใช้เมื่อใดและอย่างไร และจัดการกับสถานการณ์ที่ไม่คาดคิดที่เกิดขึ้น
* ประเมินผลลัพธ์ของงานย่อย วัดประสิทธิภาพ และปรับวนการกระทำเพื่อปรับปรุงผลลัพธ์สุดท้าย

## การกำหนดเป้าหมายโดยรวมและการแยกงานออกเป็นส่วนย่อย

![การกำหนดเป้าหมายและงาน](../../../translated_images/th/defining-goals-tasks.d70439e19e37c47a.webp)

Most real-world tasks are too complex to tackle in a single step. An AI agent needs a concise objective to guide its planning and actions. For example, consider the goal:

    "สร้างแผนการเดินทาง 3 วัน"

While it is simple to state, it still needs refinement. The clearer the goal, the better the agent (and any human collaborators) can focus on achieving the right outcome, such as creating a comprehensive itinerary with flight options, hotel recommendations, and activity suggestions.

### การแยกงานออกเป็นส่วนย่อย

Large or intricate tasks become more manageable when split into smaller, goal-oriented subtasks.
For the travel itinerary example, you could decompose the goal into:

* การจองเที่ยวบิน
* การจองโรงแรม
* การเช่ารถ
* การปรับแต่งส่วนบุคคล

Each subtask can then be tackled by dedicated agents or processes. One agent might specialize in searching for the best flight deals, another focuses on hotel bookings, and so on. A coordinating or “downstream” agent can then compile these results into one cohesive itinerary to the end user.

This modular approach also allows for incremental enhancements. For instance, you could add specialized agents for Food Recommendations or Local Activity Suggestions and refine the itinerary over time.

### ผลลัพธ์ที่มีโครงสร้าง

Large Language Models (LLMs) can generate structured output (e.g. JSON) that is easier for downstream agents or services to parse and process. This is especially useful in a multi-agent context, where we can action these tasks after the planning output is received.

The following Python snippet demonstrates a simple planning agent decomposing a goal into subtasks and generating a structured plan:

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

# โมเดลงานย่อยการเดินทาง
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # เราต้องการมอบหมายงานให้ตัวแทน

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# กำหนดข้อความของผู้ใช้
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

### เอเยนต์วางแผนกับการประสานงานแบบหลายเอเยนต์

In this example, a Semantic Router Agent receives a user request (e.g., "ฉันต้องการแผนโรงแรมสำหรับการเดินทางของฉัน.").

The planner then:

* รับแผนโรงแรม: ตัววางแผนจะรับข้อความของผู้ใช้และโดยอาศัย system prompt (รวมถึงรายละเอียดเอเยนต์ที่มีอยู่) จะสร้างแผนการเดินทางที่มีโครงสร้าง
* แสดงรายการเอเยนต์และเครื่องมือที่พวกเขามี: registry ของเอเยนต์จะเก็บรายการเอเยนต์ (เช่น สำหรับเที่ยวบิน โรงแรม การเช่ารถ และกิจกรรม) พร้อมกับฟังก์ชันหรือเครื่องมือที่พวกเขานำเสนอ
* ส่งแผนไปยังเอเยนต์ที่เกี่ยวข้อง: ขึ้นอยู่กับจำนวนงานย่อย ตัววางแผนอาจส่งข้อความไปยังเอเยนต์เฉพาะโดยตรง (สำหรับกรณีงานเดียว) หรือประสานงานผ่านผู้จัดการแชทกลุ่มสำหรับการทำงานร่วมกันแบบหลายเอเยนต์
* สรุปผลลัพธ์: สุดท้าย ตัววางแผนจะสรุปแผนที่สร้างขึ้นเพื่อความชัดเจน
The following Python code sample illustrates these steps:

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

# โมเดลงานย่อยการเดินทาง

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # เราต้องการมอบหมายงานให้กับเอเจนต์

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# สร้างไคลเอนต์

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# กำหนดข้อความของผู้ใช้

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

# พิมพ์เนื้อหาการตอบกลับหลังจากโหลดเป็น JSON

pprint(json.loads(response_content))
```

What follows is the output from the previous code and you can then use this structured output to route to `assigned_agent` and summarize the travel plan to the end user.

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

An example notebook with the previous code sample is available [ที่นี่](07-python-agent-framework.ipynb).

### การวางแผนแบบวนซ้ำ

Some tasks require a back-and-forth or re-planning, where the outcome of one subtask influences the next. For example, if the agent discovers an unexpected data format while booking flights, it might need to adapt its strategy before moving on to hotel bookings.

Additionally, user feedback (e.g. a human deciding they prefer an earlier flight) can trigger a partial re-plan. This dynamic, iterative approach ensures that the final solution aligns with real-world constraints and evolving user preferences.

ตัวอย่างโค้ด เช่น

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. เช่นเดียวกับโค้ดก่อนหน้าและส่งต่อประวัติผู้ใช้และแผนปัจจุบัน

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
# .. วางแผนใหม่และส่งงานไปยังเอเจนต์ที่เกี่ยวข้อง
```

For more comprehensive planning do checkout Magentic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">บล็อกโพสต์</a> for solving complex tasks.

## สรุป

In this article we have looked at an example of how we can create a planner that can dynamically select the available agents defined. The output of the Planner decomposes the tasks and assigns the agents so they can be executed. It is assumed the agents have access to the functions/tools that are required to perform the task. In addition to the agents you can include other patterns like reflection, summarizer, and round robin chat to further customize.

## แหล่งข้อมูลเพิ่มเติม

Magentic One - A Generalist multi-agent system for solving complex tasks and has achieved impressive results on multiple challenging agentic benchmarks. Reference: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. In this implementation the orchestrator creates task specific plans and delegates these tasks to the available agents. In addition to planning the orchestrator also employs a tracking mechanism to monitor the progress of the task and re-plans as required.

### มีคำถามเพิ่มเติมเกี่ยวกับรูปแบบการออกแบบการวางแผนไหม?

เข้าร่วม the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) เพื่อพบกับผู้เรียนคนอื่น ๆ เข้าร่วมชั่วโมงตอบคำถาม และให้คำถามเกี่ยวกับ AI Agents ของคุณได้รับการตอบ

## บทเรียนก่อนหน้า

[การสร้างเอเยนต์ AI ที่เชื่อถือได้](../06-building-trustworthy-agents/README.md)

## บทเรียนถัดไป

[รูปแบบการออกแบบหลายเอเยนต์](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
คำปฏิเสธความรับผิด:
เอกสารฉบับนี้ถูกแปลโดยใช้บริการแปลภาษา AI Co-op Translator (https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อนได้ ควรถือว่าเอกสารต้นฉบับเป็นแหล่งข้อมูลที่มีอำนาจและเชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ ขอแนะนำให้ใช้การแปลโดยนักแปลมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดจากการใช้การแปลฉบับนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->