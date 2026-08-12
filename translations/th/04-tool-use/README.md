[![วิธีการออกแบบเอเย่นต์ AI ที่ดี](../../../translated_images/th/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(คลิกที่ภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

# รูปแบบการออกแบบการใช้เครื่องมือ

เครื่องมือเป็นสิ่งที่น่าสนใจเพราะช่วยให้อเจนต์ AI มีความสามารถที่หลากหลายมากขึ้น แทนที่จะให้อเจนต์มีชุดของการกระทำที่จำกัด แค่เพิ่มเครื่องมือเข้าไปก็ทำให้อเจนต์สามารถทำงานได้หลากหลายขึ้น ในบทนี้เราจะมาดูรูปแบบการออกแบบการใช้เครื่องมือ ซึ่งอธิบายวิธีที่อเจนต์ AI สามารถใช้เครื่องมือเฉพาะเพื่อบรรลุเป้าหมายของตน

## บทนำ

ในบทเรียนนี้ เราจะตอบคำถามดังต่อไปนี้:

- รูปแบบการออกแบบการใช้เครื่องมือคืออะไร?
- กรณีการใช้งานใดที่สามารถนำไปใช้ได้?
- องค์ประกอบ/บล็อกพื้นฐานใดที่จำเป็นสำหรับการใช้งานรูปแบบการออกแบบนี้?
- การพิจารณาพิเศษอะไรบ้างสำหรับการใช้รูปแบบการออกแบบการใช้เครื่องมือในการสร้างอเจนต์ AI ที่น่าเชื่อถือ?

## เป้าหมายการเรียนรู้

หลังจากทำบทเรียนนี้จบ คุณจะสามารถ:

- นิยามรูปแบบการออกแบบการใช้เครื่องมือและวัตถุประสงค์ของมัน
- ระบุกรณีการใช้งานที่เหมาะสมกับรูปแบบการออกแบบการใช้เครื่องมือ
- เข้าใจองค์ประกอบหลักที่จำเป็นในการใช้งานรูปแบบการออกแบบ
- ตระหนักถึงข้อควรพิจารณาเพื่อให้มั่นใจว่าอเจนต์ AI ที่ใช้รูปแบบนี้มีความน่าเชื่อถือ

## รูปแบบการออกแบบการใช้เครื่องมือคืออะไร?

**รูปแบบการออกแบบการใช้เครื่องมือ** มุ่งเน้นที่การให้โมเดลภาษาใหญ่ (LLM) สามารถโต้ตอบกับเครื่องมือภายนอกเพื่อบรรลุเป้าหมายเฉพาะ เครื่องมือเป็นโค้ดที่อเจนต์สามารถเรียกใช้เพื่อทำงานต่าง ๆ ได้ เครื่องมืออาจเป็นฟังก์ชันง่าย ๆ เช่น เครื่องคิดเลข หรือเป็นการเรียก API ไปยังบริการภายนอก เช่น การค้นหาราคาหุ้น หรือการพยากรณ์อากาศ ในบริบทของอเจนต์ AI เครื่องมือได้รับการออกแบบให้เรียกใช้โดยอเจนต์เมื่อตอบสนองต่อ **การเรียกฟังก์ชันที่โมเดลสร้างขึ้น**

## กรณีการใช้งานที่สามารถนำไปใช้ได้มีอะไรบ้าง?

อเจนต์ AI สามารถใช้เครื่องมือเพื่อทำงานที่ซับซ้อน รับข้อมูล หรือทำการตัดสินใจ รูปแบบการออกแบบการใช้เครื่องมือมักถูกใช้ในสถานการณ์ที่ต้องมีการโต้ตอบแบบไดนามิกกับระบบภายนอก เช่น ฐานข้อมูล บริการเว็บ หรือการแปลความหมายโค้ด ความสามารถนี้เหมาะสมสำหรับกรณีการใช้งานต่าง ๆ ได้แก่:

- **การดึงข้อมูลแบบไดนามิก:** อเจนต์สามารถสอบถาม API ภายนอกหรือฐานข้อมูลเพื่อดึงข้อมูลที่เป็นปัจจุบัน (เช่น การสอบถามฐานข้อมูล SQLite เพื่อวิเคราะห์ข้อมูล, ดึงราคาหุ้น หรือข้อมูลสภาพอากาศ)
- **การดำเนินการและแปลความหมายโค้ด:** อเจนต์สามารถรันโค้ดหรือสคริปต์เพื่อแก้ปัญหาทางคณิตศาสตร์ สร้างรายงาน หรือจำลองสถานการณ์
- **การทำงานอัตโนมัติของเวิร์กโฟลว์:** อัตโนมัติงานที่ซ้ำซ้อนหรือหลายขั้นตอนด้วยการผสานรวมเครื่องมือต่าง ๆ เช่น โปรแกรมจัดตารางงาน บริการอีเมล หรือสายข้อมูล
- **การสนับสนุนลูกค้า:** อเจนต์สามารถโต้ตอบกับระบบ CRM แพลตฟอร์มการสนับสนุน หรือฐานความรู้เพื่อตอบคำถามผู้ใช้
- **การสร้างและแก้ไขเนื้อหา:** อเจนต์สามารถใช้เครื่องมือตรวจสอบไวยากรณ์ สรุปข้อความ หรือประเมินความปลอดภัยของเนื้อหาเพื่อช่วยงานสร้างเนื้อหา

## องค์ประกอบ/บล็อกพื้นฐานที่จำเป็นในการใช้งานรูปแบบการออกแบบการใช้เครื่องมือมีอะไรบ้าง?

บล็อกเหล่านี้ช่วยให้อเจนต์ AI สามารถทำงานได้หลากหลาย มาดูองค์ประกอบหลักสำหรับใช้งานรูปแบบการออกแบบการใช้เครื่องมือกัน:

- **โครงสร้างฟังก์ชัน/เครื่องมือ:** นิยามรายละเอียดของเครื่องมือที่ใช้ได้ รวมชื่อฟังก์ชัน จุดประสงค์ พารามิเตอร์ที่ต้องการ และผลลัพธ์ที่คาดหวัง โครงสร้างเหล่านี้ช่วยให้ LLM เข้าใจว่าเครื่องมืออะไรบ้างที่ใช้ได้และวิธีการสร้างคำขอที่ถูกต้อง

- **ตรรกะการเรียกฟังก์ชัน:** ควบคุมวิธีและเวลาที่เครื่องมือถูกเรียกใช้ตามเจตนาของผู้ใช้และบริบทการสนทนา อาจรวมถึงโมดูลการวางแผน กลไกการส่งต่อ หรือลำดับเงื่อนไขที่กำหนดการใช้เครื่องมือแบบไดนามิก

- **ระบบจัดการข้อความ:** ส่วนประกอบที่จัดการการไหลของการสนทนาระหว่างอินพุตของผู้ใช้ การตอบของ LLM การเรียกเครื่องมือ และผลลัพธ์จากเครื่องมือ

- **โครงสร้างการรวมเครื่องมือ:** โครงสร้างพื้นฐานที่เชื่อมโยงอเจนต์กับเครื่องมือต่าง ๆ ไม่ว่าจะเป็นฟังก์ชันง่าย ๆ หรือบริการภายนอกที่ซับซ้อน

- **การจัดการข้อผิดพลาดและการตรวจสอบ:** กลไกจัดการความล้มเหลวในการรันเครื่องมือ ตรวจสอบพารามิเตอร์ และจัดการกับการตอบสนองที่ไม่คาดคิด

- **การจัดการสถานะ:** ติดตามบริบทการสนทนา การโต้ตอบกับเครื่องมือก่อนหน้า และข้อมูลถาวรเพื่อให้มั่นใจในความสม่ำเสมอในการสนทนาหลายรอบ

ต่อไปเรามาดูรายละเอียดของการเรียกฟังก์ชัน/เครื่องมือกัน
 
### การเรียกฟังก์ชัน/เครื่องมือ

การเรียกฟังก์ชันเป็นวิธีหลักที่ทำให้โมเดลภาษาใหญ่ (LLMs) สามารถโต้ตอบกับเครื่องมือได้ คุณจะเห็นคำว่า 'ฟังก์ชัน' และ 'เครื่องมือ' ใช้สลับกันเพราะ 'ฟังก์ชัน' (ชุดโค้ดที่นำกลับมาใช้ใหม่ได้) คือ 'เครื่องมือ' ที่อเจนต์ใช้ทำงาน เพื่อให้โค้ดฟังก์ชันถูกเรียกใช้ LLM ต้องเปรียบเทียบคำขอของผู้ใช้กับคำอธิบายของฟังก์ชัน โดยจะส่งสคีมาที่มีคำอธิบายของฟังก์ชันทั้งหมดให้ LLM เลือกฟังก์ชันที่เหมาะสมที่สุดสำหรับงานและส่งคืนชื่อฟังก์ชันพร้อมอาร์กิวเมนต์ ฟังก์ชันที่เลือกจะถูกเรียกใช้และผลตอบกลับจะถูกส่งกลับไปที่ LLM ซึ่งใช้ข้อมูลนั้นเพื่อตอบกลับคำขอของผู้ใช้

สำหรับนักพัฒนาที่ต้องการใช้งานการเรียกฟังก์ชันสำหรับอเจนต์ จำเป็นต้องมี:

1. โมเดล LLM ที่รองรับการเรียกฟังก์ชัน
2. สคีมาที่มีคำอธิบายฟังก์ชัน
3. โค้ดสำหรับแต่ละฟังก์ชันที่ถูกอธิบายไว้

มาดูตัวอย่างการดึงเวลาปัจจุบันในเมืองหนึ่งเพื่ออธิบาย:

1. **เริ่มต้นใช้งาน LLM ที่รองรับการเรียกฟังก์ชัน:**

    ไม่ใช่ทุกรุ่นที่รองรับการเรียกฟังก์ชัน ดังนั้นต้องตรวจสอบว่า LLM ที่ใช้รองรับหรือไม่     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> รองรับการเรียกฟังก์ชัน เริ่มกันด้วยการเริ่มต้นไคลเอ็นต์ OpenAI กับ Azure OpenAI **Responses API** (จุดเชื่อมต่อที่เสถียร `/openai/v1/` — ไม่ต้องใช้ `api_version`)

    ```python
    # เริ่มต้นไคลเอนต์ OpenAI สำหรับ Azure OpenAI (API ตอบกลับ, จุดสิ้นสุด v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **สร้างสคีมาฟังก์ชัน:**

    ต่อไปเราจะกำหนดสคีมา JSON ที่ประกอบด้วยชื่อฟังก์ชัน คำอธิบายของฟังก์ชัน และชื่อกับคำอธิบายของพารามิเตอร์สำหรับฟังก์ชันนั้น
    จากนั้นนำสคีมานี้ส่งไปยังไคลเอ็นต์ที่สร้างไว้ก่อนหน้าพร้อมกับคำขอของผู้ใช้ที่ต้องการเวลาที่เมืองซานฟรานซิสโก สิ่งสำคัญคือ **การเรียกเครื่องมือ** คือสิ่งที่ถูกส่งกลับมา **ไม่ใช่** คำตอบสุดท้ายของคำถาม อย่างที่บอกไว้ก่อนหน้านี้ LLM จะส่งคืนชื่อฟังก์ชันที่เลือกสำหรับงานและอาร์กิวเมนต์ที่จะส่งให้ฟังก์ชันนั้น

    ```python
    # คำอธิบายฟังก์ชันสำหรับโมเดลเพื่ออ่าน (รูปแบบเครื่องมือแผ่นข้อมูล API การตอบกลับ)
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # ข้อความผู้ใช้เริ่มต้น
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # การเรียก API ครั้งแรก: ขอให้โมเดลใช้ฟังก์ชัน
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API ส่งคืนการเรียกเครื่องมือในรูปแบบ function_call ใน response.output
    # แนบพวกมันไปยังบทสนทนาเพื่อให้โมเดลมีบริบทครบถ้วนในรอบถัดไป
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **โค้ดฟังก์ชันที่จำเป็นสำหรับทำงานนี้:**

    เมื่อ LLM เลือกฟังก์ชันที่ต้องรันได้แล้ว ต้องมีการเขียนและรันโค้ดเพื่อทำงานนี้
    เราสามารถเขียนโค้ดเพื่อดึงเวลาปัจจุบันด้วย Python ได้ และจำเป็นต้องเขียนโค้ดเพื่อดึงชื่อและอาร์กิวเมนต์จาก response_message เพื่อรับผลลัพธ์สุดท้ายด้วย

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # จัดการการเรียกฟังก์ชัน
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # ส่งคืนผลลัพธ์ของเครื่องมือในรูปแบบ item function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # การเรียก API ครั้งที่สอง: รับคำตอบสุดท้ายจากโมเดล
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

การเรียกฟังก์ชันเป็นหัวใจของรูปแบบการออกแบบเครื่องมือสำหรับอเจนต์ส่วนใหญ่ถ้าไม่ทั้งหมด แต่การทำเองตั้งแต่เริ่มต้นบางครั้งก็มีความท้าทาย
ตามที่เราเรียนรู้ใน [บทเรียน 2](../../../02-explore-agentic-frameworks) เฟรมเวิร์กอเจนติกช่วยให้เรามีบล็อกพื้นฐานสำเร็จรูปสำหรับการใช้งานเครื่องมือ
 
## ตัวอย่างการใช้เครื่องมือกับ Agentic Frameworks

ต่อไปนี้คือตัวอย่างวิธีการใช้งานรูปแบบการออกแบบการใช้เครื่องมือด้วยเฟรมเวิร์กอเจนติกต่าง ๆ:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> เป็นเฟรมเวิร์ก AI แบบโอเพนซอร์สสำหรับสร้างอเจนต์ AI ทำให้ง่ายต่อการใช้การเรียกฟังก์ชันด้วยการกำหนดเครื่องมือเป็นฟังก์ชัน Python ที่มี `@tool` decorator เฟรมเวิร์กจะจัดการการสื่อสารระหว่างโมเดลกับโค้ดของคุณโดยอัตโนมัติ และยังให้เครื่องมือสำเร็จรูปอย่าง File Search และ Code Interpreter ผ่าน `FoundryChatClient`

แผนภาพต่อไปนี้แสดงกระบวนการเรียกฟังก์ชันกับ Microsoft Agent Framework:

![function calling](../../../translated_images/th/functioncalling-diagram.a84006fc287f6014.webp)

กับ Microsoft Agent Framework เครื่องมือถูกกำหนดเป็นฟังก์ชันที่ถูกตกแต่ง เราสามารถแปลงฟังก์ชัน `get_current_time` ที่เห็นก่อนหน้านี้ให้เป็นเครื่องมือด้วย `@tool` decorator เฟรมเวิร์กจะทำการแปลงฟังก์ชันและพารามิเตอร์เป็นสคีมาเพื่อส่งให้ LLM โดยอัตโนมัติ

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# สร้างไคลเอนต์
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# สร้างเอเจนต์และรันด้วยเครื่องมือ
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> เป็นเฟรมเวิร์กอเจนติกรุ่นใหม่ที่ออกแบบมาเพื่อช่วยนักพัฒนาในการสร้าง ปล่อย และขยายอเจนต์ AI ที่มีคุณภาพสูงและขยายได้อย่างปลอดภัยโดยไม่ต้องดูแลทรัพยากรคอมพิวเตอร์และจัดเก็บข้อมูลเบื้องหลัง เป็นประโยชน์อย่างยิ่งสำหรับแอปพลิเคชันองค์กรเพราะเป็นบริการที่ได้รับการบริหารจัดการเต็มรูปแบบพร้อมความปลอดภัยระดับองค์กร

เมื่อเปรียบเทียบกับการพัฒนาด้วย API LLM โดยตรง Microsoft Foundry Agent Service มีข้อดีหลายอย่าง รวมถึง:

- การเรียกเครื่องมือแบบอัตโนมัติ – ไม่จำเป็นต้องวิเคราะห์การเรียกเครื่องมือ เรียกใช้เครื่องมือ หรือจัดการผลลัพธ์ เพราะทั้งหมดนี้ทำที่ฝั่งเซิร์ฟเวอร์
- การจัดการข้อมูลอย่างปลอดภัย – แทนที่จะจัดการสถานะการสนทนาเอง คุณสามารถใช้ threads เพื่อเก็บข้อมูลทั้งหมดที่ต้องการ
- เครื่องมือพร้อมใช้งานทันที – เครื่องมือสำหรับโต้ตอบกับแหล่งข้อมูล เช่น Bing, Azure AI Search, และ Azure Functions

เครื่องมือใน Microsoft Foundry Agent Service ถูกแบ่งออกเป็นสองประเภท:

1. เครื่องมือความรู้:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. เครื่องมือปฏิบัติการ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">เครื่องมือที่กำหนดโดย OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

บริการ Agent นี้ช่วยให้เราสามารถใช้เครื่องมือเหล่านี้ร่วมกันเป็น `toolset` และยังใช้ `threads` เพื่อเก็บประวัติข้อความจากแต่ละการสนทนา

สมมติว่าคุณเป็นตัวแทนขายของบริษัท Contoso คุณต้องการพัฒนาอเจนต์สนทนาที่สามารถตอบคำถามเกี่ยวกับข้อมูลการขายของคุณ

ภาพต่อไปนี้แสดงวิธีที่คุณสามารถใช้ Microsoft Foundry Agent Service ในการวิเคราะห์ข้อมูลการขายของคุณ:

![Agentic Service In Action](../../../translated_images/th/agent-service-in-action.34fb465c9a84659e.webp)

ในการใช้เครื่องมือใด ๆ เหล่านี้กับบริการ เราสามารถสร้างไคลเอ็นต์และกำหนดเครื่องมือหรือชุดเครื่องมือ เพื่อใช้งานจริง เราสามารถใช้โค้ด Python ต่อไปนี้ LLM จะสามารถดูที่ชุดเครื่องมือและตัดสินใจว่าจะใช้ฟังก์ชันที่ผู้ใช้สร้างขึ้น `fetch_sales_data_using_sqlite_query` หรือ Code Interpreter ที่สร้างไว้ล่วงหน้าตามคำขอของผู้ใช้

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # ฟังก์ชัน fetch_sales_data_using_sqlite_query ซึ่งสามารถพบได้ในไฟล์ fetch_sales_data_functions.py
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# เริ่มต้นชุดเครื่องมือ
toolset = ToolSet()

# เริ่มต้นตัวแทนเรียกใช้ฟังก์ชันด้วยฟังก์ชัน fetch_sales_data_using_sqlite_query และเพิ่มเข้าไปในชุดเครื่องมือ
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# เริ่มต้นเครื่องมือ Code Interpreter และเพิ่มเข้าไปในชุดเครื่องมือ
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ข้อควรพิจารณาพิเศษสำหรับการใช้รูปแบบการออกแบบการใช้เครื่องมือเพื่อสร้างอเจนต์ AI ที่น่าเชื่อถือ

ความกังวลทั่วไปกับ SQL ที่สร้างแบบไดนามิกโดย LLM คือความปลอดภัย โดยเฉพาะความเสี่ยงของ SQL injection หรือการกระทำที่เป็นอันตราย เช่น การลบหรือแก้ไขฐานข้อมูล แม้ว่าความกังวลเหล่านี้จะมีเหตุผล แต่สามารถลดความเสี่ยงได้อย่างมีประสิทธิภาพด้วยการตั้งค่าการเข้าถึงฐานข้อมูลอย่างถูกต้อง สำหรับฐานข้อมูลส่วนใหญ่จะตั้งให้ฐานข้อมูลเป็นอ่านอย่างเดียว สำหรับบริการฐานข้อมูลเช่น PostgreSQL หรือ Azure SQL แอปควรได้รับบทบาทอ่านอย่างเดียว (SELECT)

การรันแอปในสภาพแวดล้อมที่ปลอดภัยช่วยเพิ่มการป้องกันมากขึ้น ในสถานการณ์องค์กร ข้อมูลมักถูกดึงและแปลงจากระบบปฏิบัติการไปยังฐานข้อมูลอ่านอย่างเดียวหรือ data warehouse ที่มีสคีมาใช้งานง่าย วิธีนี้ช่วยให้ข้อมูลปลอดภัย ประสิทธิภาพดี และแอปมีสิทธิ์เข้าถึงแบบอ่านอย่างเดียวอย่างจำกัด

## ตัวอย่างโค้ด

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## มีคำถามเพิ่มเติมเกี่ยวกับรูปแบบการออกแบบการใช้เครื่องมือไหม?

เข้าร่วม [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) เพื่อพบกับผู้เรียนคนอื่น เข้าร่วมชั่วโมงพูดคุย และถามคำถามเกี่ยวกับอเจนต์ AI ของคุณ

## แหล่งข้อมูลเพิ่มเติม

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">เวิร์กช็อป Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">เวิร์กช็อป Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">ภาพรวม Microsoft Agent Framework</a>


## การทดสอบแบบ Smoke-Testing สำหรับเอเจนต์นี้ (ไม่บังคับ)

หลังจากที่คุณเรียนรู้การปรับใช้เอเจนต์ในบทเรียนที่ [Lesson 16](../16-deploying-scalable-agents/README.md) แล้ว คุณสามารถทดสอบแบบ smoke-test สำหรับ `TravelToolAgent` ของบทเรียนนี้ (มันยังคงเรียกใช้เครื่องมือและตอบคำถามไหม?) ด้วย [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) ดูที่ [`tests/README.md`](../tests/README.md) สำหรับวิธีการรัน

## บทเรียนก่อนหน้า

[การทำความเข้าใจรูปแบบการออกแบบเอเจนต์](../03-agentic-design-patterns/README.md)

## บทเรียนถัดไป

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->