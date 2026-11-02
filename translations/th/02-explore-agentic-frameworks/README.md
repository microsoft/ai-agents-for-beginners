[![สำรวจโครงสร้างเอเจนต์ AI](../../../translated_images/th/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(คลิกที่รูปภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

# สำรวจโครงสร้างเอเจนต์ AI

โครงสร้างเอเจนต์ AI คือแพลตฟอร์มซอฟต์แวร์ที่ออกแบบมาเพื่อให้ง่ายต่อการสร้าง, นำไปใช้, และจัดการเอเจนต์ AI โครงสร้างเหล่านี้ให้ส่วนประกอบที่สร้างไว้ล่วงหน้า, การแบ่งนามธรรม, และเครื่องมือที่ช่วยให้การพัฒนาระบบ AI ที่ซับซ้อนเป็นไปอย่างราบรื่น

โครงสร้างเหล่านี้ช่วยให้นักพัฒนาสามารถมุ่งเน้นไปที่แง่มุมเฉพาะของแอปพลิเคชันของตนโดยให้แนวทางมาตรฐานสำหรับความท้าทายทั่วไปในการพัฒนาเอเจนต์ AI พวกเขาช่วยเพิ่มขีดความสามารถในการขยาย, การเข้าถึง, และประสิทธิภาพในการสร้างระบบ AI

## บทนำ

บทเรียนนี้จะครอบคลุม:

- โครงสร้างเอเจนต์ AI คืออะไรและช่วยให้นักพัฒนาทำอะไรได้บ้าง?
- ทีมสามารถใช้สิ่งเหล่านี้เพื่อสร้างต้นแบบ ทบทวน และปรับปรุงความสามารถของเอเจนต์ได้อย่างไรอย่างรวดเร็ว?
- ความแตกต่างระหว่างโครงสร้างและเครื่องมือที่ Microsoft สร้างขึ้น (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> และ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) มีอะไรบ้าง?
- ฉันสามารถรวมเครื่องมือในระบบนิเวศ Azure ที่มีอยู่โดยตรงได้ไหม หรือจำเป็นต้องใช้โซลูชันแยกต่างหาก?
- Microsoft Foundry Agent Service คืออะไร และช่วยฉันได้อย่างไร?

## เป้าหมายการเรียนรู้

เป้าหมายของบทเรียนนี้คือช่วยให้คุณเข้าใจ:

- บทบาทของโครงสร้างเอเจนต์ AI ในการพัฒนา AI
- วิธีใช้โครงสร้างเอเจนต์ AI ในการสร้างเอเจนต์อัจฉริยะ
- ความสามารถหลักที่โครงสร้างเอเจนต์ AI อำนวยความสะดวก
- ความแตกต่างระหว่าง Microsoft Agent Framework และ Microsoft Foundry Agent Service

## โครงสร้างเอเจนต์ AI คืออะไรและช่วยให้นักพัฒนาทำอะไรได้บ้าง?

โครงสร้าง AI แบบดั้งเดิมช่วยให้คุณรวม AI เข้ากับแอปของคุณและทำให้แอปเหล่านี้ดีขึ้นได้ในด้านต่างๆ ดังนี้:

- **การปรับแต่งส่วนบุคคล**: AI สามารถวิเคราะห์พฤติกรรมและความชอบของผู้ใช้เพื่อให้คำแนะนำ, เนื้อหา, และประสบการณ์ที่เฉพาะตัว
ตัวอย่าง: บริการสตรีมมิ่งอย่าง Netflix ใช้ AI เพื่อแนะนำภาพยนตร์และรายการตามประวัติการชม ช่วยเพิ่มการมีส่วนร่วมและความพึงพอใจของผู้ใช้
- **การทำงานอัตโนมัติและประสิทธิภาพ**: AI สามารถทำงานซ้ำซ้อนอัตโนมัติ, ปรับปรุงกระบวนงาน, และเพิ่มประสิทธิภาพในการดำเนินงาน
ตัวอย่าง: แอปบริการลูกค้าใช้แชทบอทที่ขับเคลื่อนด้วย AI เพื่อจัดการคำถามทั่วไป ลดเวลาตอบกลับและปล่อยให้นักบริการลูกค้าทำงานในเรื่องที่ซับซ้อนมากขึ้น
- **เพิ่มประสบการณ์ผู้ใช้**: AI ช่วยปรับปรุงประสบการณ์ผู้ใช้โดยรวมด้วยฟีเจอร์อัจฉริยะ เช่น การรู้จำเสียง, การประมวลผลภาษาธรรมชาติ, และการทำนายข้อความ
ตัวอย่าง: ผู้ช่วยเสมือนอย่าง Siri และ Google Assistant ใช้ AI เพื่อเข้าใจและตอบคำสั่งเสียง ช่วยให้ผู้ใช้โต้ตอบกับอุปกรณ์ได้ง่ายขึ้น

### สิ่งเหล่านี้ฟังดูดีเลยใช่ไหม ทำไมเราจึงต้องใช้โครงสร้างเอเจนต์ AI?

โครงสร้างเอเจนต์ AI เป็นมากกว่าการเป็นโครงสร้าง AI ทั่วไป มันได้รับการออกแบบมาเพื่อให้สามารถสร้างเอเจนต์อัจฉริยะที่สามารถโต้ตอบกับผู้ใช้, เอเจนต์อื่นๆ, และสภาพแวดล้อมเพื่อบรรลุเป้าหมายเฉพาะได้ เอเจนต์เหล่านี้สามารถแสดงพฤติกรรมอิสระ, ตัดสินใจ, และปรับตัวให้เข้ากับสภาพแวดล้อมที่เปลี่ยนแปลงได้ มาดูความสามารถหลักบางประการที่โครงสร้างเอเจนต์ AI อำนวยความสะดวก:

- **การทำงานร่วมและการประสานงานของเอเจนต์**: ช่วยสร้างเอเจนต์ AI หลายตัวที่สามารถทำงานร่วมกัน, สื่อสาร, และประสานงานเพื่อแก้ไขงานที่ซับซ้อนได้
- **การทำงานอัตโนมัติและการจัดการงาน**: มีกลไกสำหรับทำงานตามกระบวนการหลายขั้นตอนอัตโนมัติ, มอบหมายงาน, และจัดการงานแบบไดนามิกระหว่างเอเจนต์
- **ความเข้าใจบริบทและการปรับตัว**: ให้อุปกรณ์เอเจนต์ความสามารถในการเข้าใจบริบท, ปรับตัวเข้ากับสภาพแวดล้อมที่เปลี่ยนแปลง, และตัดสินใจตามข้อมูลแบบเรียลไทม์

สรุปแล้ว เอเจนต์ช่วยให้คุณทำอะไรได้มากขึ้น, ยกระดับการทำงานอัตโนมัติ, สร้างระบบที่ชาญฉลาดซึ่งสามารถปรับตัวและเรียนรู้จากสภาพแวดล้อมได้

## วิธีการสร้างต้นแบบอย่างรวดเร็ว, ทบทวน, และปรับปรุงความสามารถของเอเจนต์?

นี่คือแนวทางที่เปลี่ยนแปลงอย่างรวดเร็ว แต่มีสิ่งบางอย่างที่พบได้ทั่วไปในโครงสร้างเอเจนต์ AI หลายตัวที่ช่วยให้คุณสร้างต้นแบบและทบทวนได้อย่างรวดเร็ว ได้แก่ ส่วนประกอบแบบโมดูล, เครื่องมือทำงานร่วมกัน, และการเรียนรู้แบบเรียลไทม์ มาดูรายละเอียดแต่ละข้อ:

- **ใช้ส่วนประกอบแบบโมดูล**: SDK AI มีส่วนประกอบที่สร้างไว้ล่วงหน้า เช่น ตัวเชื่อมต่อ AI และหน่วยความจำ, การเรียกใช้ฟังก์ชันด้วยภาษาธรรมชาติหรือปลั๊กอินโค้ด, เทมเพลตพรอมต์ และอื่น ๆ
- **ใช้ประโยชน์จากเครื่องมือทำงานร่วมกัน**: ออกแบบเอเจนต์โดยกำหนดบทบาทและงานเฉพาะ เพื่อให้ทดสอบและปรับปรุงกระบวนการทำงานร่วมกัน
- **เรียนรู้แบบเรียลไทม์**: นำวงจรป้อนกลับมาใช้ ที่ซึ่งเอเจนต์เรียนรู้จากการโต้ตอบและปรับพฤติกรรมของตนแบบไดนามิก

### ใช้ส่วนประกอบแบบโมดูล

SDK เช่น Microsoft Agent Framework มีส่วนประกอบที่สร้างไว้ล่วงหน้า เช่น ตัวเชื่อมต่อ AI, การกำหนดเครื่องมือ, และการจัดการเอเจนต์

**ทีมสามารถใช้สิ่งเหล่านี้อย่างไร**: ทีมสามารถประกอบส่วนประกอบเหล่านี้อย่างรวดเร็วเพื่อสร้างต้นแบบที่ใช้งานได้โดยไม่ต้องเริ่มสร้างจากศูนย์ เปิดโอกาสให้ทดลองและทบทวนอย่างรวดเร็ว

**การใช้งานจริง**: คุณสามารถใช้ตัวแบ่งวิเคราะห์ที่สร้างไว้ล่วงหน้าสำหรับดึงข้อมูลจากอินพุตของผู้ใช้ หน่วยความจำสำหรับเก็บและดึงข้อมูล และเครื่องสร้างพรอมต์สำหรับโต้ตอบกับผู้ใช้ ทั้งหมดนี้โดยไม่ต้องสร้างส่วนประกอบเองทั้งหมด

**ตัวอย่างโค้ด** มาดูตัวอย่างวิธีใช้ Microsoft Agent Framework พร้อม `FoundryChatClient` เพื่อให้โมเดลตอบสนองอินพุตของผู้ใช้ด้วยการเรียกใช้เครื่องมือ:

``` python
# ตัวอย่าง Microsoft Agent Framework ในภาษา Python

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# กำหนดฟังก์ชันเครื่องมือตัวอย่างสำหรับการจองการเดินทาง
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # ตัวอย่างผลลัพธ์: เที่ยวบินของคุณไปยังนิวยอร์กในวันที่ 1 มกราคม 2025 ได้จองเรียบร้อยแล้ว เดินทางปลอดภัย! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

สิ่งที่คุณเห็นในตัวอย่างนี้คือวิธีใช้ตัวแบ่งวิเคราะห์ที่สร้างไว้ล่วงหน้าเพื่อดึงข้อมูลสำคัญจากอินพุตของผู้ใช้ เช่น จุดเริ่มต้น, จุดหมายปลายทาง, และวันที่ของการจองเที่ยวบิน วิธีการแบบโมดูลนี้ช่วยให้คุณมุ่งเน้นที่ตรรกะระดับสูงได้

### ใช้ประโยชน์จากเครื่องมือทำงานร่วมกัน

โครงสร้างอย่าง Microsoft Agent Framework ช่วยในการสร้างเอเจนต์หลายตัวที่สามารถทำงานร่วมกันได้

**ทีมสามารถใช้สิ่งเหล่านี้อย่างไร**: ทีมสามารถออกแบบเอเจนต์ตามบทบาทและงานเฉพาะ เพื่อทดสอบและปรับปรุงกระบวนการทำงานร่วมกัน และปรับปรุงประสิทธิภาพของระบบโดยรวม

**การใช้งานจริง**: คุณสามารถสร้างทีมเอเจนต์ แต่ละตัวมีฟังก์ชันเฉพาะ เช่น การดึงข้อมูล, การวิเคราะห์, หรือการตัดสินใจ เอเจนต์เหล่านี้สามารถสื่อสารและแลกเปลี่ยนข้อมูลเพื่อบรรลุเป้าหมายร่วมกัน เช่น ตอบคำถามของผู้ใช้หรือทำงานให้เสร็จ

**ตัวอย่างโค้ด (Microsoft Agent Framework)**:

```python
# การสร้างเอเย่นต์หลายตัวที่ทำงานร่วมกันโดยใช้ Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# เอเย่นต์ดึงข้อมูล
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# เอเย่นต์วิเคราะห์ข้อมูล
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# รันเอเย่นต์ตามลำดับบนงานหนึ่งงาน
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

สิ่งที่คุณเห็นในโค้ดนี้คือการสร้างงานที่เกี่ยวข้องกับเอเจนต์หลายตัวทำงานร่วมกันเพื่อวิเคราะห์ข้อมูล เอเจนต์แต่ละตัวทำหน้าที่เฉพาะ และงานนี้จะดำเนินการโดยการประสานงานระหว่างเอเจนต์เพื่อให้ได้ผลลัพธ์ที่ต้องการ การสร้างเอเจนต์เฉพาะกิจที่มีบทบาทเฉพาะจะช่วยเพิ่มประสิทธิภาพและสมรรถภาพของงาน

### เรียนรู้แบบเรียลไทม์

โครงสร้างขั้นสูงมีความสามารถในการเข้าใจบริบทและปรับตัวแบบเรียลไทม์

**ทีมสามารถใช้สิ่งเหล่านี้อย่างไร**: ทีมสามารถใช้วงจรป้อนกลับที่เอเจนต์เรียนรู้จากการโต้ตอบและปรับพฤติกรรมอย่างต่อเนื่อง นำไปสู่การพัฒนาและปรับปรุงความสามารถอย่างต่อเนื่อง

**การใช้งานจริง**: เอเจนต์สามารถวิเคราะห์ความคิดเห็นของผู้ใช้, ข้อมูลสภาพแวดล้อม, และผลลัพธ์ของงาน เพื่ออัปเดตฐานความรู้, ปรับปรุงอัลกอริทึมการตัดสินใจ และพัฒนาประสิทธิภาพขึ้นเมื่อเวลาผ่านไป กระบวนการเรียนรู้ซ้ำนี้ช่วยให้เอเจนต์ปรับตัวให้เข้ากับสภาพแวดล้อมและความชื่นชอบของผู้ใช้ เพิ่มประสิทธิภาพโดยรวมของระบบ

## ความแตกต่างระหว่าง Microsoft Agent Framework และ Microsoft Foundry Agent Service คืออะไร?

มีหลายวิธีเปรียบเทียบแนวทางเหล่านี้ แต่เรามาดูความแตกต่างหลักๆ ในแง่ของการออกแบบ, ความสามารถ, และกรณีการใช้งานเป้าหมาย:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework เป็น SDK ที่ออกแบบมาให้ใช้งานง่ายสำหรับการสร้างเอเจนต์ AI ด้วย `FoundryChatClient` มันช่วยให้นักพัฒนาสร้างเอเจนต์ที่ใช้โมเดล Azure OpenAI โดยมีฟีเจอร์การเรียกใช้เครื่องมือในตัว, การจัดการการสนทนา, และความปลอดภัยระดับองค์กรผ่าน Azure identity

**กรณีการใช้งาน**: การสร้างเอเจนต์ AI ที่พร้อมใช้งานจริงพร้อมความสามารถเรียกใช้เครื่องมือ, กระบวนการหลายขั้นตอน และการผนวกรวมกับองค์กร

นี่คือแนวคิดหลักบางส่วนของ Microsoft Agent Framework:

- **เอเจนต์**. เอเจนต์ถูกสร้างผ่าน `FoundryChatClient` และตั้งค่าด้วยชื่อ, คำแนะนำ, และเครื่องมือ เอเจนต์สามารถ:
  - **ประมวลผลข้อความของผู้ใช้** และสร้างการตอบกลับโดยใช้โมเดล Azure OpenAI
  - **เรียกใช้เครื่องมือ** อัตโนมัติขึ้นอยู่กับบริบทการสนทนา
  - **รักษาสถานะการสนทนา** ได้ในหลายๆ การโต้ตอบ

  นี่คือตัวอย่างโค้ดแสดงวิธีสร้างเอเจนต์:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **เครื่องมือ**. โครงสร้างรองรับการกำหนดเครื่องมือเป็นฟังก์ชันภาษา Python ที่เอเจนต์สามารถเรียกใช้อัตโนมัติ เครื่องมือจะถูกลงทะเบียนเมื่อสร้างเอเจนต์:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **การประสานงานหลายเอเจนต์**. คุณสามารถสร้างเอเจนต์หลายตัวด้วยความเชี่ยวชาญต่างกันและประสานงานการทำงานของพวกเขาได้:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **การผนวกรวม Azure Identity**. โครงสร้างใช้ `AzureCliCredential` (หรือ `DefaultAzureCredential`) เพื่อการยืนยันตัวตนที่ปลอดภัยโดยไม่ต้องใช้คีย์ API ซึ่งช่วยให้ไม่ต้องจัดการคีย์โดยตรง

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service คือส่วนเสริมล่าสุด เปิดตัวในงาน Microsoft Ignite 2024 มันอนุญาตให้พัฒนาและนำไปใช้เอเจนต์ AI ด้วยโมเดลที่ยืดหยุ่นมากขึ้น เช่น เรียกใช้ LLMs โอเพนซอร์สโดยตรงอย่าง Llama 3, Mistral, และ Cohere

Microsoft Foundry Agent Service มีวิธีการรักษาความปลอดภัยสำหรับองค์กรที่เข้มแข็งและวิธีการเก็บข้อมูลที่เหมาะสำหรับแอปพลิเคชันองค์กร

มันทำงานได้ทันทีร่วมกับ Microsoft Agent Framework ในการสร้างและนำเอเจนต์ไปใช้งาน

บริการนี้อยู่ในสถานะ Public Preview และรองรับ Python และ C# สำหรับการสร้างเอเจนต์

ด้วย Microsoft Foundry Agent Service Python SDK เราสามารถสร้างเอเจนต์ที่มีเครื่องมือกำหนดเองได้:

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
        model="gpt-5-mini",
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

Microsoft Foundry Agent Service มีแนวคิดหลักดังนี้:

- **เอเจนต์**. Microsoft Foundry Agent Service ผนวกรวมกับ Microsoft Foundry ภายใน Microsoft Foundry เอเจนต์ AI ทำงานเป็นไมโครเซอร์วิส "อัจฉริยะ" ที่ใช้ตอบคำถาม (RAG), ปฏิบัติการ หรืออัตโนมัติกระบวนการทำงานโดยสมบูรณ์ มันทำได้โดยรวมพลังของโมเดล generative AI กับเครื่องมือที่ช่วยให้เข้าถึงและโต้ตอบกับแหล่งข้อมูลจริงได้ นี่คือตัวอย่างเอเจนต์:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ในตัวอย่างนี้ สร้างเอเจนต์ด้วยโมเดล `gpt-5-mini`, ชื่อ `my-agent`, และคำแนะนำ `You are helpful agent` เอเจนต์นี้มีเครื่องมือและทรัพยากรสำหรับทำงานตีความโค้ด

- **เธรดและข้อความ**. เธรดเป็นแนวคิดสำคัญอีกอย่างหนึ่ง แสดงถึงการสนทนาหรือการโต้ตอบระหว่างเอเจนต์กับผู้ใช้ เธรดใช้เพื่อติดตามความก้าวหน้าของการสนทนา, เก็บข้อมูลบริบท และจัดการสถานะของการโต้ตอบ นี่คือตัวอย่างเธรด:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # ขอให้ตัวแทนดำเนินงานบนเธรด
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # ดึงและบันทึกข้อความทั้งหมดเพื่อดูการตอบสนองของตัวแทน
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    ในโค้ดก่อนหน้านี้ สร้างเธรด จากนั้นส่งข้อความไปยังเธรด โดยเรียก `create_and_process_run` เพื่อให้เอเจนต์ทำงานกับเธรด สุดท้าย ดึงข้อความมาและบันทึกเพื่อตรวจสอบการตอบกลับของเอเจนต์ ข้อความเหล่านี้แสดงความคืบหน้าของการสนทนาระหว่างผู้ใช้กับเอเจนต์ สิ่งสำคัญอีกประการคือข้อความสามารถมีหลายประเภท เช่น ข้อความ, รูปภาพ, หรือไฟล์ ซึ่งเป็นผลลัพธ์การทำงานของเอเจนต์คุณสามารถใช้ข้อมูลนี้เพื่อประมวลผลการตอบกลับเพิ่มเติมหรือแสดงต่อผู้ใช้ได้

- **ผนวกรวมกับ Microsoft Agent Framework**. Microsoft Foundry Agent Service ทำงานร่วมกับ Microsoft Agent Framework ได้อย่างราบรื่น ซึ่งหมายความว่าคุณสามารถสร้างเอเจนต์โดยใช้ `FoundryChatClient` และนำไปใช้งานผ่าน Agent Service สำหรับสถานการณ์ใช้งานจริง

**กรณีการใช้งาน**: Microsoft Foundry Agent Service ออกแบบมาสำหรับแอปพลิเคชันองค์กรที่ต้องการการนำไปใช้เอเจนต์ AI ที่ปลอดภัย, ขยายตัวได้, และยืดหยุ่น

## ความแตกต่างระหว่างแนวทางเหล่านี้คืออะไร?
 
แม้ว่าจะดูเหมือนมีการทับซ้อนกัน แต่ก็มีความแตกต่างหลักในแง่ของการออกแบบ, ความสามารถ, และกรณีการใช้งานเป้าหมาย:
 
- **Microsoft Agent Framework (MAF)**: SDK ที่พร้อมใช้ในงานผลิตสำหรับสร้างเอเจนต์ AI ให้ API ที่เรียบง่ายสำหรับสร้างเอเจนต์ด้วยการเรียกใช้เครื่องมือ, การจัดการสนทนา, และการผนวกรวม Azure identity
- **Microsoft Foundry Agent Service**: แพลตฟอร์มและบริการนำไปใช้ภายใน Microsoft Foundry สำหรับเอเจนต์ มีการเชื่อมต่อในตัวกับบริการ เช่น Azure OpenAI, Azure AI Search, Bing Search และการประมวลผลโค้ด
 
ยังไม่แน่ใจว่าจะเลือกใช้อันไหน?

### กรณีใช้งาน
 
มาลองดูว่าช่วยคุณได้ไหมโดยผ่านกรณีใช้งานทั่วไป:
 
> ถาม: ฉันกำลังสร้างเอเจนต์ AI สำหรับงานผลิตและต้องการเริ่มต้นอย่างรวดเร็ว
>

>ตอบ: Microsoft Agent Framework เป็นตัวเลือกที่ยอดเยี่ยม มันให้ API สะดวกใน Python ผ่าน `FoundryChatClient` ที่ช่วยให้กำหนดเอเจนต์พร้อมเครื่องมือและคำแนะนำในไม่กี่บรรทัดโค้ด

>ถาม: ฉันต้องการการนำไปใช้ระดับองค์กรพร้อมการผนวกรวมกับ Azure เช่น Search และการประมวลผลโค้ด
>
> ตอบ: Microsoft Foundry Agent Service เหมาะสมที่สุด เป็นแพลตฟอร์มที่มีความสามารถในตัวสำหรับโมเดลหลายตัว, Azure AI Search, Bing Search และ Azure Functions ช่วยให้สร้างเอเจนต์ใน Foundry Portal และนำไปใช้ในระดับใหญ่ได้ง่าย
 
> ถาม: ฉันยังสับสน ช่วยเลือกตัวเลือกเดียวให้ฉันหน่อย
>
> ตอบ: เริ่มจาก Microsoft Agent Framework เพื่อสร้างเอเจนต์ของคุณก่อน จากนั้นใช้ Microsoft Foundry Agent Service เมื่อต้องการนำไปใช้งานและขยายระบบในงานผลิต วิธีนี้ทำให้คุณสามารถทบทวนตรรกะเอเจนต์ได้เร็ว พร้อมเส้นทางที่ชัดเจนไปสู่การนำไปใช้ระดับองค์กร
 
สรุปความแตกต่างหลักในตาราง:

| โครงสร้าง | จุดเน้น | แนวคิดหลัก | กรณีใช้งาน |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK เอเจนต์ที่เรียบง่ายพร้อมฟังก์ชันเรียกใช้เครื่องมือ | เอเจนต์, เครื่องมือ, Azure Identity | สร้างเอเจนต์ AI, การใช้เครื่องมือ, กระบวนการหลายขั้นตอน |
| Microsoft Foundry Agent Service | โมเดลยืดหยุ่น, ความปลอดภัยองค์กร, การสร้างโค้ด, การเรียกใช้เครื่องมือ | โมดูล, การทำงานร่วมกัน, การจัดการกระบวนการ | การนำเอเจนต์ AI ไปใช้ที่ปลอดภัย, ขยายตัวได้และยืดหยุ่น |

## ฉันสามารถรวมเครื่องมือในระบบนิเวศ Azure ที่มีอยู่ได้โดยตรงหรือจำเป็นต้องใช้โซลูชันแยกต่างหาก?


คำตอบคือ ใช่ คุณสามารถรวมเครื่องมือระบบนิเวศ Azure ที่มีอยู่ของคุณเข้ากับ Microsoft Foundry Agent Service ได้โดยตรงโดยเฉพาะ เนื่องจากถูกสร้างขึ้นให้ทำงานร่วมกับบริการ Azure อื่นๆ ได้อย่างราบรื่น ตัวอย่างเช่น คุณสามารถรวม Bing, Azure AI Search และ Azure Functions ได้ นอกจากนี้ยังมีการผสานรวมลึกกับ Microsoft Foundry

Microsoft Agent Framework ยังผสานรวมกับบริการ Azure ผ่าน `FoundryChatClient` และตัวตน Azure ช่วยให้คุณเรียกใช้บริการ Azure โดยตรงจากเครื่องมือเอเย่นต์ของคุณได้

## ตัวอย่างโค้ด

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## มีคำถามเพิ่มเติมเกี่ยวกับ AI Agent Framework หรือไม่?

เข้าร่วม [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) เพื่อพบปะกับผู้เรียนคนอื่นๆ เข้าร่วมชั่วโมงประชุมและสอบถามคำถามเกี่ยวกับ AI Agents ของคุณ

## แหล่งข้อมูลอ้างอิง

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">บริการเอเย่นต์ Azure</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - การตอบสนอง Azure OpenAI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## บทเรียนก่อนหน้า

[แนะนำ AI Agents และกรณีการใช้งาน Agent](../01-intro-to-ai-agents/README.md)

## บทเรียนถัดไป

[ทำความเข้าใจแบบแผนการออกแบบ Agentic](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->