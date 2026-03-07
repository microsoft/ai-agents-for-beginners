[![Exploring AI Agent Frameworks](../../../translated_images/th/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(คลิกที่รูปภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

# สำรวจเฟรมเวิร์กตัวแทน AI

เฟรมเวิร์กตัวแทน AI คือแพลตฟอร์มซอฟต์แวร์ที่ออกแบบมาเพื่อช่วยให้การสร้าง การใช้งาน และการจัดการตัวแทน AI ง่ายขึ้น เฟรมเวิร์กเหล่านี้ให้ส่วนประกอบสำเร็จรูป นามธรรม และเครื่องมือต่างๆ แก่นักพัฒนา เพื่ออำนวยความสะดวกในการพัฒนาระบบ AI ที่ซับซ้อน

เฟรมเวิร์กเหล่านี้ช่วยให้นักพัฒนาสามารถมุ่งเน้นไปที่แง่มุมเฉพาะของแอปพลิเคชัน โดยให้แนวทางมาตรฐานสำหรับความท้าทายทั่วไปในการพัฒนาตัวแทน AI ช่วยเพิ่มความสามารถในการขยายการใช้งาน ความเข้าถึง และประสิทธิภาพในการสร้างระบบ AI

## บทนำ

บทเรียนนี้จะครอบคลุม:

- เฟรมเวิร์กตัวแทน AI คืออะไร และช่วยให้นักพัฒนาทำอะไรได้บ้าง?
- ทีมงานสามารถใช้เฟรมเวิร์กเหล่านี้ในการสร้างต้นแบบได้อย่างรวดเร็ว ปรับปรุง และพัฒนาขีดความสามารถของตัวแทนได้อย่างไร?
- ความแตกต่างระหว่างเฟรมเวิร์กและเครื่องมือที่สร้างโดย Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> และ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) คืออะไร?
- ฉันสามารถใช้งานเครื่องมือในระบบนิเวศ Azure ที่มีอยู่แล้วโดยตรงได้ไหม หรือจำเป็นต้องใช้โซลูชันแยกต่างหาก?
- บริการ Azure AI Agents คืออะไร และช่วยฉันได้อย่างไร?

## เป้าหมายการเรียนรู้

เป้าหมายของบทเรียนนี้คือช่วยให้คุณเข้าใจ:

- บทบาทของเฟรมเวิร์กตัวแทน AI ในการพัฒนา AI
- วิธีใช้เฟรมเวิร์กตัวแทน AI เพื่อสร้างตัวแทนอัจฉริยะ
- ความสามารถหลักที่เฟรมเวิร์กตัวแทน AI ช่วยให้เป็นไปได้
- ความแตกต่างระหว่าง Microsoft Agent Framework กับ Azure AI Agent Service

## เฟรมเวิร์กตัวแทน AI คืออะไร และช่วยให้นักพัฒนาทำอะไรได้บ้าง?

เฟรมเวิร์ก AI แบบดั้งเดิมสามารถช่วยคุณรวม AI เข้ากับแอปพลิเคชันของคุณและพัฒนาแอปเหล่านี้ได้ดังนี้:

- **การปรับแต่งเฉพาะบุคคล**: AI สามารถวิเคราะห์พฤติกรรมและความชอบของผู้ใช้ เพื่อเสนอคำแนะนำ เนื้อหา และประสบการณ์ที่ปรับให้เหมาะสมกับบุคคล
ตัวอย่าง: บริการสตรีมมิ่งอย่าง Netflix ใช้ AI เพื่อแนะนำภาพยนตร์และรายการตามประวัติการรับชม ช่วยเพิ่มการมีส่วนร่วมและความพึงพอใจของผู้ใช้
- **การทำงานอัตโนมัติและประสิทธิภาพ**: AI สามารถทำงานที่ซ้ำซ้อนโดยอัตโนมัติ ปรับปรุงกระบวนการทำงาน และเพิ่มประสิทธิภาพการดำเนินงาน
ตัวอย่าง: แอปบริการลูกค้าใช้แชทบ็อตที่ขับเคลื่อนด้วย AI เพื่อจัดการคำถามทั่วไป ลดเวลาตอบกลับ และปล่อยให้เจ้าหน้าที่ดูแลปัญหาที่ซับซ้อนกว่า
- **ประสบการณ์ผู้ใช้ที่ดีขึ้น**: AI สามารถเพิ่มประสบการณ์ผู้ใช้โดยรวมด้วยฟีเจอร์อัจฉริยะ เช่น การรู้จำเสียง การประมวลผลภาษาธรรมชาติ และการคาดเดาข้อความ
ตัวอย่าง: ผู้ช่วยเสมือน เช่น Siri และ Google Assistant ใช้ AI เพื่อเข้าใจและตอบคำสั่งเสียง ทำให้ผู้ใช้โต้ตอบกับอุปกรณ์ได้ง่ายขึ้น

### ฟังดูดีใช่ไหม แล้วทำไมเราจึงต้องใช้เฟรมเวิร์กตัวแทน AI?

เฟรมเวิร์กตัวแทน AI ไม่ใช่แค่เฟรมเวิร์ก AI ธรรมดา แต่ถูกออกแบบมาเพื่อสร้างตัวแทนอัจฉริยะที่สามารถโต้ตอบกับผู้ใช้ ตัวแทนอื่น และสภาพแวดล้อม เพื่อบรรลุเป้าหมายเฉพาะ ตัวแทนเหล่านี้สามารถทำงานโดยอิสระ ตัดสินใจ และปรับตัวตามสภาพแวดล้อมที่เปลี่ยนแปลงได้ มาดูความสามารถหลักที่เฟรมเวิร์กตัวแทน AI ช่วยให้เกิดขึ้น:

- **ความร่วมมือและการประสานงานของตัวแทน**: สร้างตัวแทน AI หลายตัวที่สามารถทำงานร่วมกัน สื่อสาร และประสานงานเพื่อแก้ปัญหาที่ซับซ้อนได้
- **การทำงานอัตโนมัติและการจัดการงาน**: มีระบบการทำงานอัตโนมัติแบบหลายขั้นตอน การมอบหมายงาน และการจัดการงานแบบไดนามิกระหว่างตัวแทน
- **ความเข้าใจบริบทและการปรับตัว**: เติมเต็มตัวแทนด้วยความสามารถในการเข้าใจบริบท ปรับตัวให้เข้ากับสภาพแวดล้อมที่เปลี่ยนแปลง และตัดสินใจตามข้อมูลเรียลไทม์

สรุปก็คือตัวแทนช่วยให้คุณทำได้มากขึ้น ยกระดับงานอัตโนมัติ สร้างระบบอัจฉริยะที่สามารถปรับตัวและเรียนรู้จากสภาพแวดล้อมได้

## วิธีสร้างต้นแบบ ทดลอง และปรับปรุงขีดความสามารถของตัวแทนอย่างรวดเร็ว?

สภาพแวดล้อมนี้เปลี่ยนแปลงอย่างรวดเร็ว แต่มีสิ่งที่เป็นแนวทางร่วมกันในเฟรมเวิร์กตัวแทน AI ส่วนใหญ่ที่ช่วยให้คุณสร้างต้นแบบและปรับปรุงได้อย่างรวดเร็ว ได้แก่ ส่วนประกอบโมดูล เครื่องมือร่วมมือ และการเรียนรู้แบบเรียลไทม์ มาดูรายละเอียด:

- **ใช้ส่วนประกอบโมดูล**: SDK AI มีส่วนประกอบสำเร็จรูป เช่น ตัวเชื่อม AI และหน่วยความจำ การเรียกฟังก์ชันด้วยภาษาธรรมชาติหรือปลั๊กอินโค้ด เทมเพลตคำสั่ง และอื่นๆ
- **ใช้เครื่องมือร่วมมือ**: ออกแบบตัวแทนด้วยบทบาทและหน้าที่เฉพาะ เพื่อให้ทดสอบและปรับปรุงกระบวนการทำงานร่วมกันได้
- **เรียนรู้แบบเรียลไทม์**: ใช้วงจรตอบรับที่ตัวแทนเรียนรู้จากการโต้ตอบและปรับพฤติกรรมอย่างไดนามิก

### ใช้ส่วนประกอบโมดูล

SDK เช่น Microsoft Agent Framework มีส่วนประกอบสำเร็จรูป เช่น ตัวเชื่อม AI การกำหนดเครื่องมือ และการจัดการตัวแทน

**ทีมสามารถใช้ได้อย่างไร**: ทีมสามารถประกอบส่วนประกอบเหล่านี้ได้อย่างรวดเร็วเพื่อสร้างต้นแบบที่ใช้งานได้ โดยไม่ต้องเริ่มจากศูนย์ ช่วยให้ทดลองและปรับปรุงได้เร็วขึ้น

**การทำงานในทางปฏิบัติ**: คุณสามารถใช้ตัวแยกวิเคราะห์ที่สร้างไว้แล้วเพื่อดึงข้อมูลจากอินพุตของผู้ใช้ โมดูลหน่วยความจำเพื่อจัดเก็บและเรียกข้อมูล และตัวสร้างคำสั่งเพื่อโต้ตอบกับผู้ใช้ โดยไม่ต้องสร้างส่วนประกอบเหล่านี้ใหม่

**ตัวอย่างโค้ด** มาดูตัวอย่างการใช้ Microsoft Agent Framework กับ `AzureAIProjectAgentProvider` เพื่อให้โมเดลตอบกลับการป้อนข้อมูลผู้ใช้ด้วยการเรียกเครื่องมือ:

``` python
# ตัวอย่าง Microsoft Agent Framework สำหรับ Python

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# กำหนดฟังก์ชันตัวอย่างเพื่อจองการเดินทาง
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # ตัวอย่างผลลัพธ์: เที่ยวบินของคุณไปยังนิวยอร์กในวันที่ 1 มกราคม 2025 ได้รับการจองเรียบร้อยแล้ว เดินทางปลอดภัย! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

สิ่งที่คุณเห็นจากตัวอย่างนี้คือวิธีใช้ตัวแยกวิเคราะห์สำเร็จรูปเพื่อดึงข้อมูลสำคัญจากอินพุตผู้ใช้ เช่น จุดต้นทาง จุดหมาย และวันที่ของคำขอจองเที่ยวบิน วิธีการแบบโมดูลนี้ช่วยให้คุณสามารถมุ่งเน้นที่ตรรกะในระดับสูงได้

### ใช้เครื่องมือร่วมมือ

เฟรมเวิร์กอย่าง Microsoft Agent Framework อำนวยความสะดวกในการสร้างตัวแทนหลายตัวที่ทำงานร่วมกันได้

**ทีมสามารถใช้ได้อย่างไร**: ทีมสามารถออกแบบตัวแทนด้วยบทบาทและหน้าที่เฉพาะ เพื่อทดสอบและปรับปรุงกระบวนการทำงานร่วมกัน และเพิ่มประสิทธิภาพระบบโดยรวม

**การทำงานในทางปฏิบัติ**: คุณสามารถสร้างทีมตัวแทนที่แต่ละตัวมีหน้าที่เฉพาะ เช่น การดึงข้อมูล การวิเคราะห์ หรือการตัดสินใจ ตัวแทนเหล่านี้สามารถสื่อสารและแชร์ข้อมูลเพื่อบรรลุเป้าหมายร่วม เช่น ตอบคำถามผู้ใช้หรือทำงานให้เสร็จ

**ตัวอย่างโค้ด (Microsoft Agent Framework)**:

```python
# การสร้างเอเจนต์หลายตัวที่ทำงานร่วมกันโดยใช้ Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# เอเจนต์ดึงข้อมูล
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# เอเจนต์วิเคราะห์ข้อมูล
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# เรียกใช้งานเอเจนต์ตามลำดับสำหรับงาน
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

โค้ดก่อนหน้านี้แสดงวิธีสร้างงานที่เกี่ยวข้องกับตัวแทนหลายตัวทำงานร่วมกันเพื่อวิเคราะห์ข้อมูล ตัวแทนแต่ละตัวทำหน้าที่เฉพาะเจาะจง และงานจะถูกดำเนินการโดยการประสานงานตัวแทนเพื่อให้ได้ผลลัพธ์ตามต้องการ การสร้างตัวแทนเฉพาะที่มีบทบาทพิเศษช่วยเพิ่มประสิทธิภาพและประสิทธิผลของงาน

### เรียนรู้แบบเรียลไทม์

เฟรมเวิร์กขั้นสูงมีความสามารถในการเข้าใจบริบทแบบเรียลไทม์และปรับตัว

**ทีมสามารถใช้ได้อย่างไร**: ทีมสามารถติดตั้งวงจรตอบรับที่ตัวแทนเรียนรู้จากการโต้ตอบและปรับพฤติกรรมตามสถานการณ์แบบไดนามิก นำไปสู่การปรับปรุงและพัฒนาขีดความสามารถอย่างต่อเนื่อง

**การทำงานในทางปฏิบัติ**: ตัวแทนสามารถวิเคราะห์คำติชมของผู้ใช้ ข้อมูลสภาพแวดล้อม และผลลัพธ์ของงาน เพื่ออัปเดตฐานความรู้ ปรับอัลกอริทึมการตัดสินใจ และเพิ่มประสิทธิภาพเมื่อเวลาผ่านไป กระบวนการเรียนรู้แบบทำซ้ำนี้ช่วยให้ตัวแทนปรับตัวตามเงื่อนไขที่เปลี่ยนและความชอบของผู้ใช้ เพิ่มประสิทธิผลโดยรวมของระบบ

## ความแตกต่างระหว่าง Microsoft Agent Framework กับ Azure AI Agent Service คืออะไร?

มีหลายวิธีในการเปรียบเทียบแนวทางเหล่านี้ แต่เราจะมาดูความแตกต่างสำคัญในด้านการออกแบบ ความสามารถ และกรณีการใช้งานเป้าหมายกัน:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework เป็น SDK ที่ออกแบบมาอย่างเรียบง่ายสำหรับการสร้างตัวแทน AI ด้วย `AzureAIProjectAgentProvider` ช่วยให้นักพัฒนาสร้างตัวแทนที่ใช้โมเดล Azure OpenAI พร้อมฟีเจอร์เรียกใช้เครื่องมือในตัว การจัดการการสนทนา และความปลอดภัยระดับองค์กรผ่าน Azure identity

**กรณีการใช้งาน**: สร้างตัวแทน AI สำหรับใช้งานจริงที่มีการใช้เครื่องมือ กรณีงานหลายขั้นตอน และการผสานรวมในองค์กร

นี่คือแนวคิดหลักของ Microsoft Agent Framework:

- **ตัวแทน (Agents)** ตัวแทนถูกสร้างผ่าน `AzureAIProjectAgentProvider` และตั้งค่าชื่อ คำแนะนำ และเครื่องมือต่างๆ ตัวแทนจะ:
  - **ประมวลผลข้อความผู้ใช้** และสร้างคำตอบโดยใช้โมเดล Azure OpenAI
  - **เรียกใช้เครื่องมือ** โดยอัตโนมัติ ตามบริบทการสนทนา
  - **รักษาสถานะการสนทนา** ในหลายรอบโต้ตอบ

  นี่คือตัวอย่างโค้ดการสร้างตัวแทน:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **เครื่องมือ (Tools)** เฟรมเวิร์กรองรับการนิยามเครื่องมือเป็นฟังก์ชัน Python ที่ตัวแทนสามารถเรียกใช้ได้อัตโนมัติ เครื่องมือจะถูกลงทะเบียนเมื่อตอนสร้างตัวแทน:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **การประสานงานหลายตัวแทน (Multi-Agent Coordination)** คุณสามารถสร้างตัวแทนหลายตัวที่มีความชำนาญต่างกัน และประสานงานงานของพวกเขา:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **การผสาน Azure Identity** เฟรมเวิร์กใช้ `AzureCliCredential` (หรือ `DefaultAzureCredential`) สำหรับการตรวจสอบตัวตนแบบปลอดภัยโดยไม่ใช้กุญแจ API จึงไม่ต้องจัดการกุญแจเอง

## Azure AI Agent Service

Azure AI Agent Service เป็นบริการใหม่ที่เปิดตัวในงาน Microsoft Ignite 2024 ช่วยให้พัฒนาและปรับใช้ตัวแทน AI ด้วยโมเดลที่ยืดหยุ่นมากขึ้น เช่น การเรียกใช้โมเดล LLM โอเพนซอร์สโดยตรง เช่น Llama 3, Mistral และ Cohere

Azure AI Agent Service มีระบบความปลอดภัยระดับองค์กรและวิธีจัดเก็บข้อมูลที่แข็งแกร่ง ทำให้เหมาะสำหรับแอปพลิเคชันองค์กร

ทำงานร่วมกับ Microsoft Agent Framework อย่างราบรื่นสำหรับสร้างและปรับใช้ตัวแทน

บริการนี้อยู่ในสถานะ Public Preview สนับสนุนภาษา Python และ C# สำหรับสร้างตัวแทน

โดยใช้ Azure AI Agent Service Python SDK เราสามารถสร้างตัวแทนพร้อมเครื่องมือที่ผู้ใช้กำหนดได้:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# กำหนดฟังก์ชันของเครื่องมือ
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### แนวคิดหลัก

Azure AI Agent Service มีแนวคิดหลักดังนี้:

- **ตัวแทน (Agent)** Azure AI Agent Service บูรณาการกับ Microsoft Foundry ภายใน AI Foundry ตัวแทน AI คือ "ไมโครเซอร์วิสอัจฉริยะ" ที่ใช้ตอบคำถาม (RAG) ทำงาน หรืออัตโนมัติเต็มรูปแบบของเวิร์กโฟลว์ โดยนำพลังจากโมเดล AI สร้างสรรค์มารวมกับเครื่องมือที่ให้เข้าถึงและโต้ตอบกับแหล่งข้อมูลจริง ตัวอย่างตัวแทน:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ในตัวอย่างนี้ ตัวแทนถูกสร้างด้วยโมเดล `gpt-4o-mini` ชื่อ `my-agent` และคำสั่ง `You are helpful agent` ตัวแทนมีเครื่องมือและทรัพยากรสำหรับงานตีความโค้ด

- **เธรดและข้อความ (Thread and messages)** เธรดเป็นแนวคิดสำคัญอีกอย่าง แสดงถึงการสนทนาหรือการโต้ตอบระหว่างตัวแทนกับผู้ใช้ เธรดใช้ติดตามความคืบหน้าการสนทนา เก็บข้อมูลบริบท และจัดการสถานะการโต้ตอบ ตัวอย่างเธรด:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    ในโค้ดก่อนหน้า เธรดถูกสร้างขึ้น จากนั้นส่งข้อความเข้าเธรด ผ่าน `create_and_process_run` ขอให้ตัวแทนทำงานบนเธรด สุดท้ายดึงและบันทึกข้อความเพื่อดูคำตอบของตัวแทน ข้อความเหล่านี้แสดงความก้าวหน้าการสนทนาระหว่างผู้ใช้กับตัวแทน สำคัญที่ต้องเข้าใจว่า ข้อความอาจมีหลายประเภท เช่น ข้อความ รูปภาพ หรือไฟล์ ซึ่งเป็นผลลัพธ์จากงานของตัวแทน เช่น ภาพ หรือคำตอบข้อความ ในฐานะนักพัฒนา คุณสามารถใช้ข้อมูลนี้เพื่อต่อประมวลผลหรือนำเสนอแก่ผู้ใช้

- **การผสานกับ Microsoft Agent Framework** Azure AI Agent Service ทำงานร่วมกับ Microsoft Agent Framework ได้อย่างไร้รอยต่อ หมายความว่าคุณสามารถสร้างตัวแทนด้วย `AzureAIProjectAgentProvider` และปรับใช้ผ่าน Agent Service สำหรับการใช้งานจริง

**กรณีการใช้งาน**: Azure AI Agent Service เหมาะสำหรับแอปพลิเคชันองค์กรที่ต้องการการปรับใช้ตัวแทน AI ที่ปลอดภัย ขยายได้ และยืดหยุ่น

## ความแตกต่างระหว่างแนวทางเหล่านี้คืออะไร?

ดูเหมือนจะมีความทับซ้อน แต่มีความแตกต่างสำคัญในด้านการออกแบบ ความสามารถ และกรณีใช้งานเป้าหมาย:

- **Microsoft Agent Framework (MAF)**: เป็น SDK สำหรับสร้างตัวแทน AI พร้อมใช้งานจริง มี API ที่เรียบง่ายสำหรับสร้างตัวแทนพร้อมฟีเจอร์เรียกเครื่องมือ การจัดการบทสนทนา และการเชื่อมต่อกับ Azure Identity
- **Azure AI Agent Service**: เป็นแพลตฟอร์มและบริการปรับใช้ใน Azure Foundry สำหรับตัวแทน มีการเชื่อมต่อในตัวกับบริการต่างๆ เช่น Azure OpenAI, Azure AI Search, Bing Search และการรันโค้ด

ยังไม่แน่ใจว่าจะเลือกแบบไหน?

### กรณีการใช้งาน

ลองดูว่าช่วยคุณได้ไหมจากกรณีทั่วไปต่อไปนี้:

> Q: ฉันกำลังสร้างแอปตัวแทน AI สำหรับใช้งานจริง และต้องการเริ่มต้นอย่างรวดเร็ว
>

>A: Microsoft Agent Framework เป็นตัวเลือกที่ยอดเยี่ยม มี API แบบ Python ง่ายๆ ผ่าน `AzureAIProjectAgentProvider` ที่ช่วยคุณกำหนดตัวแทนพร้อมเครื่องมือและคำสั่งเพียงไม่กี่บรรทัดโค้ด

>Q: ฉันต้องการปรับใช้ระดับองค์กร พร้อมการผสานกับ Azure เช่น Search และการรันโค้ด
>
> A: Azure AI Agent Service เหมาะที่สุด เป็นบริการแพลตฟอร์มที่มีฟีเจอร์ในตัวสำหรับโมเดลหลายตัว Azure AI Search, Bing Search และ Azure Functions สร้างตัวแทนได้ง่ายจาก Foundry Portal และปรับใช้ในระดับใหญ่

> Q: ฉันยังสับสน ขอแบบเลือกอย่างเดียว
>
> A: เริ่มจาก Microsoft Agent Framework เพื่อสร้างตัวแทนก่อน จากนั้นใช้ Azure AI Agent Service เมื่อต้องการปรับใช้และขยายในสภาพแวดล้อมใช้งานจริง วิธีนี้ช่วยให้ทดลองและปรับปรุงตรรกะตัวแทนได้เร็ว พร้อมมีเส้นทางชัดเจนไปสู่การปรับใช้ในองค์กร

สรุปความแตกต่างหลักในตาราง:

| Framework | จุดสนใจ | แนวคิดหลัก | กรณีใช้งาน |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK ตัวแทนที่เรียบง่ายพร้อมฟีเจอร์เรียกเครื่องมือ | ตัวแทน, เครื่องมือ, Azure Identity | สร้างตัวแทน AI, ใช้เครื่องมือ, งานหลายขั้นตอน |
| Azure AI Agent Service | โมเดลยืดหยุ่น, ความปลอดภัยองค์กร, การสร้างโค้ด, เรียกเครื่องมือ | ความโมดูล, ความร่วมมือ, การจัดการเวิร์กโฟลว์ | การปรับใช้ตัวแทน AI ที่ปลอดภัย ขยายได้ และยืดหยุ่น |

## ฉันสามารถใช้งานเครื่องมือในระบบนิเวศ Azure ที่มีอยู่แล้วโดยตรงได้ไหม หรือจำเป็นต้องใช้โซลูชันแยกต่างหาก?
คำตอบคือใช่ คุณสามารถผสานรวมเครื่องมือระบบนิเวศ Azure ที่มีอยู่ของคุณโดยตรงกับ Azure AI Agent Service ได้โดยเฉพาะอย่างยิ่ง เนื่องจากถูกสร้างขึ้นให้ทำงานร่วมกับบริการ Azure อื่น ๆ ได้อย่างราบรื่น ตัวอย่างเช่น คุณสามารถผสานรวม Bing, Azure AI Search และ Azure Functions ได้ นอกจากนี้ยังมีการผสานรวมอย่างลึกซึ้งกับ Microsoft Foundry

Microsoft Agent Framework ยังผสานรวมกับบริการของ Azure ผ่าน `AzureAIProjectAgentProvider` และ Azure identity ทำให้คุณสามารถเรียกใช้บริการ Azure ได้โดยตรงจากเครื่องมือ agent ของคุณ

## Sample Codes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## มีคำถามเพิ่มเติมเกี่ยวกับ AI Agent Framework หรือไม่?

เข้าร่วม [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) เพื่อพบปะกับผู้เรียนคนอื่น ๆ เข้าร่วม office hours และรับคำตอบสำหรับคำถามเกี่ยวกับ AI Agents ของคุณ

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## บทเรียนก่อนหน้า

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## บทเรียนถัดไป

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะเรามุ่งมั่นเพื่อความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่ถูกต้อง สำหรับข้อมูลที่สำคัญ ควรใช้บริการแปลภาษามนุษย์อย่างมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->