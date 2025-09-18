<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43069833a0412210ad5c3cc93d9c2146",
  "translation_date": "2025-09-18T15:00:04+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "th"
}
-->
[![Planning Design Pattern](../../../translated_images/lesson-7-thumbnail.f7163ac557bea1236242cc86b178c3f1bbf5eb07b87f9cd7c256b366e32bcbb6.th.png)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(คลิกที่ภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

# การออกแบบการวางแผน

## บทนำ

บทเรียนนี้จะครอบคลุมถึง

* การกำหนดเป้าหมายโดยรวมที่ชัดเจนและการแบ่งงานที่ซับซ้อนออกเป็นงานย่อยที่จัดการได้
* การใช้ผลลัพธ์ที่มีโครงสร้างเพื่อให้ได้คำตอบที่เชื่อถือได้และอ่านได้โดยเครื่อง
* การใช้แนวทางที่ขับเคลื่อนด้วยเหตุการณ์เพื่อจัดการงานแบบไดนามิกและข้อมูลที่ไม่คาดคิด

## เป้าหมายการเรียนรู้

หลังจากจบบทเรียนนี้ คุณจะเข้าใจเกี่ยวกับ:

* การระบุและตั้งเป้าหมายโดยรวมสำหรับ AI agent เพื่อให้แน่ใจว่า agent รู้ว่าต้องบรรลุอะไร
* การแบ่งงานที่ซับซ้อนออกเป็นงานย่อยที่จัดการได้และจัดลำดับงานเหล่านั้นในลำดับที่มีเหตุผล
* การเตรียม agent ด้วยเครื่องมือที่เหมาะสม (เช่น เครื่องมือค้นหาหรือเครื่องมือวิเคราะห์ข้อมูล) การตัดสินใจว่าเมื่อใดและอย่างไรที่จะใช้เครื่องมือเหล่านี้ และการจัดการสถานการณ์ที่ไม่คาดคิด
* การประเมินผลลัพธ์ของงานย่อย วัดผลการดำเนินงาน และปรับปรุงการดำเนินการเพื่อเพิ่มคุณภาพของผลลัพธ์สุดท้าย

## การกำหนดเป้าหมายโดยรวมและการแบ่งงาน

![Defining Goals and Tasks](../../../translated_images/defining-goals-tasks.d70439e19e37c47ac76c48b209a4eb515bea5b8a5207f6b2e7b5e597f09ccf6a.th.png)

งานในโลกจริงส่วนใหญ่มีความซับซ้อนเกินกว่าจะจัดการได้ในขั้นตอนเดียว AI agent จำเป็นต้องมีวัตถุประสงค์ที่ชัดเจนเพื่อเป็นแนวทางในการวางแผนและการดำเนินการ ตัวอย่างเช่น ลองพิจารณาเป้าหมาย:

    "สร้างแผนการเดินทาง 3 วัน"

แม้ว่าเป้าหมายนี้จะดูเรียบง่าย แต่ยังต้องมีการปรับแต่งเพิ่มเติม ยิ่งเป้าหมายชัดเจนมากเท่าไร agent (และผู้ร่วมงานที่เป็นมนุษย์) ก็จะสามารถมุ่งเน้นไปที่การบรรลุผลลัพธ์ที่ถูกต้องได้ดีขึ้น เช่น การสร้างแผนการเดินทางที่ครอบคลุมพร้อมตัวเลือกเที่ยวบิน คำแนะนำโรงแรม และกิจกรรมที่น่าสนใจ

### การแบ่งงาน

งานที่ใหญ่หรือซับซ้อนจะจัดการได้ง่ายขึ้นเมื่อแบ่งออกเป็นงานย่อยที่มีเป้าหมายชัดเจน ตัวอย่างเช่น สำหรับแผนการเดินทาง คุณสามารถแบ่งเป้าหมายออกเป็น:

* การจองเที่ยวบิน
* การจองโรงแรม
* การเช่ารถ
* การปรับแต่งตามความต้องการ

งานย่อยแต่ละงานสามารถจัดการได้โดย agent หรือกระบวนการเฉพาะทาง ตัวอย่างเช่น agent หนึ่งอาจเชี่ยวชาญในการค้นหาข้อเสนอเที่ยวบินที่ดีที่สุด อีกตัวหนึ่งเน้นการจองโรงแรม เป็นต้น จากนั้น agent ที่ทำหน้าที่ประสานงานหรือ "downstream" สามารถรวบรวมผลลัพธ์เหล่านี้เป็นแผนการเดินทางที่สมบูรณ์สำหรับผู้ใช้งาน

วิธีการแบบแยกส่วนนี้ยังช่วยให้สามารถปรับปรุงได้ทีละขั้นตอน ตัวอย่างเช่น คุณสามารถเพิ่ม agent เฉพาะทางสำหรับคำแนะนำด้านอาหารหรือกิจกรรมในพื้นที่ และปรับปรุงแผนการเดินทางให้ดีขึ้นเรื่อย ๆ

### ผลลัพธ์ที่มีโครงสร้าง

Large Language Models (LLMs) สามารถสร้างผลลัพธ์ที่มีโครงสร้าง (เช่น JSON) ซึ่งง่ายต่อการแยกวิเคราะห์และประมวลผลโดย agent หรือบริการที่เกี่ยวข้องในขั้นตอนถัดไป สิ่งนี้มีประโยชน์อย่างยิ่งในบริบทของ multi-agent ซึ่งเราสามารถดำเนินการตามงานเหล่านี้หลังจากได้รับผลลัพธ์การวางแผน

สำหรับภาพรวมอย่างรวดเร็ว

ตัวอย่างโค้ด Python ด้านล่างแสดง agent การวางแผนที่เรียบง่ายซึ่งแบ่งเป้าหมายออกเป็นงานย่อยและสร้างแผนที่มีโครงสร้าง:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.azure import AzureAIChatCompletionClient
from azure.core.credentials import AzureKeyCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

client = AzureAIChatCompletionClient(
    model="gpt-4o-mini",
    endpoint="https://models.inference.ai.azure.com",
    # To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
    # Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
    model_info={
        "json_output": False,
        "function_calling": True,
        "vision": True,
        "family": "unknown",
    },
)

# Define the user message
messages = [
    SystemMessage(content="""You are an planner agent.
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
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(
        content="Create a travel plan for a family of 2 kids from Singapore to Melboune", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": 'json_object'})

response_content: Optional[str] = response.content if isinstance(
    response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string" )

pprint(json.loads(response_content))

# # Ensure the response content is a valid JSON string before loading it
# response_content: Optional[str] = response.content if isinstance(
#     response.content, str) else None
# if response_content is None:
#     raise ValueError("Response content is not a valid JSON string")

# # Print the response content after loading it as JSON
# pprint(json.loads(response_content))

# Validate the response content with the MathReasoning model
# TravelPlan.model_validate(json.loads(response_content))
```

### Agent การวางแผนที่มีการประสานงานหลาย agent

ในตัวอย่างนี้ Semantic Router Agent จะรับคำขอจากผู้ใช้ (เช่น "ฉันต้องการแผนโรงแรมสำหรับการเดินทางของฉัน")

จากนั้น planner จะ:

* รับแผนโรงแรม: planner จะรับข้อความของผู้ใช้และสร้างแผนการเดินทางที่มีโครงสร้างโดยอิงจาก system prompt (รวมถึงรายละเอียด agent ที่มีอยู่)
* แสดงรายการ agent และเครื่องมือของพวกเขา: registry ของ agent จะเก็บรายการ agent (เช่น สำหรับเที่ยวบิน โรงแรม การเช่ารถ และกิจกรรม) พร้อมฟังก์ชันหรือเครื่องมือที่พวกเขาเสนอ
* ส่งแผนไปยัง agent ที่เกี่ยวข้อง: ขึ้นอยู่กับจำนวนงานย่อย planner จะส่งข้อความไปยัง agent เฉพาะ (สำหรับสถานการณ์ที่มีงานเดียว) หรือประสานงานผ่าน group chat manager สำหรับการทำงานร่วมกันของหลาย agent
* สรุปผลลัพธ์: สุดท้าย planner จะสรุปแผนที่สร้างขึ้นเพื่อความชัดเจน

ตัวอย่างโค้ด Python ด้านล่างแสดงขั้นตอนเหล่านี้:

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

# Travel SubTask Model

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Create the client with type-checked environment variables

client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

from pprint import pprint

# Define the user message

messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": TravelPlan})

# Ensure the response content is a valid JSON string before loading it

response_content: Optional[str] = response.content if isinstance(response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string")

# Print the response content after loading it as JSON

pprint(json.loads(response_content))
```

ผลลัพธ์จากโค้ดก่อนหน้านี้สามารถใช้เพื่อส่งไปยัง `assigned_agent` และสรุปแผนการเดินทางให้กับผู้ใช้งาน

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

ตัวอย่าง notebook ที่มีโค้ดตัวอย่างก่อนหน้านี้สามารถดูได้ [ที่นี่](07-autogen.ipynb)

### การวางแผนแบบวนซ้ำ

งานบางอย่างต้องการการปรับเปลี่ยนหรือการวางแผนใหม่ โดยที่ผลลัพธ์ของงานย่อยหนึ่งมีผลต่อขั้นตอนถัดไป ตัวอย่างเช่น หาก agent พบรูปแบบข้อมูลที่ไม่คาดคิดขณะจองเที่ยวบิน อาจต้องปรับกลยุทธ์ก่อนดำเนินการจองโรงแรม

นอกจากนี้ ข้อเสนอแนะจากผู้ใช้ (เช่น การเลือกเที่ยวบินที่ออกเดินทางเร็วกว่า) อาจกระตุ้นให้มีการวางแผนใหม่บางส่วน วิธีการแบบไดนามิกและวนซ้ำนี้ช่วยให้มั่นใจได้ว่าผลลัพธ์สุดท้ายสอดคล้องกับข้อจำกัดในโลกจริงและความต้องการที่เปลี่ยนแปลงของผู้ใช้

ตัวอย่างเช่น โค้ดตัวอย่าง:

```python
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
#.. same as previous code and pass on the user history, current plan
messages = [
    SystemMessage(content="""You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
    AssistantMessage(content=f"Previous travel plan - {TravelPlan}", source="assistant")
]
# .. re-plan and send the tasks to respective agents
```

สำหรับการวางแผนที่ครอบคลุมมากขึ้น ลองดู Magnetic One สำหรับการแก้ปัญหางานที่ซับซ้อน

## สรุป

ในบทความนี้เราได้ดูตัวอย่างวิธีการสร้าง planner ที่สามารถเลือก agent ที่มีอยู่ได้อย่างไดนามิก ผลลัพธ์ของ planner จะทำการแบ่งงานและกำหนด agent เพื่อให้สามารถดำเนินการได้ โดยถือว่า agent มีเครื่องมือ/ฟังก์ชันที่จำเป็นในการทำงาน นอกจาก agent แล้ว คุณยังสามารถเพิ่มรูปแบบอื่น ๆ เช่น reflection, summarizer และ round robin chat เพื่อปรับแต่งเพิ่มเติม

## แหล่งข้อมูลเพิ่มเติม

AutoGen Magnetic One - ระบบ multi-agent แบบทั่วไปสำหรับการแก้ปัญหางานที่ซับซ้อนและได้ผลลัพธ์ที่น่าประทับใจในหลาย benchmark ที่ท้าทายสำหรับ agentic อ้างอิง:

ในระบบนี้ orchestrator จะสร้างแผนเฉพาะงานและมอบหมายงานเหล่านี้ให้กับ agent ที่มีอยู่ นอกจากการวางแผน orchestrator ยังใช้กลไกการติดตามเพื่อเฝ้าดูความคืบหน้าของงานและวางแผนใหม่ตามความจำเป็น

### มีคำถามเพิ่มเติมเกี่ยวกับรูปแบบการออกแบบการวางแผน?

เข้าร่วม [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) เพื่อพบปะกับผู้เรียนคนอื่น ๆ เข้าร่วม office hours และรับคำตอบสำหรับคำถามเกี่ยวกับ AI Agents ของคุณ

## บทเรียนก่อนหน้า

[การสร้าง AI Agents ที่น่าเชื่อถือ](../06-building-trustworthy-agents/README.md)

## บทเรียนถัดไป

[รูปแบบการออกแบบ Multi-Agent](../08-multi-agent/README.md)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้