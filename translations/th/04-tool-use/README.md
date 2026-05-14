[![วิธีการออกแบบ AI Agents ที่ดี](../../../translated_images/th/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(คลิกที่ภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

# รูปแบบการออกแบบการใช้งานเครื่องมือ

เครื่องมือเป็นสิ่งที่น่าสนใจเพราะช่วยให้ AI agents มีความสามารถที่กว้างขึ้น แทนที่จะมีชุดการกระทำที่จำกัดโดยตัวเอง ด้วยการเพิ่มเครื่องมือ ตัวแทนสามารถทำงานได้หลากหลายขึ้น ในบทนี้เราจะมาดูรูปแบบการออกแบบการใช้งานเครื่องมือ ซึ่งอธิบายว่า AI agents สามารถใช้เครื่องมือเฉพาะเพื่อบรรลุเป้าหมายได้อย่างไร

## บทนำ

ในบทเรียนนี้ เราจะพยายามตอบคำถามต่อไปนี้:

- รูปแบบการออกแบบการใช้งานเครื่องมือคืออะไร?
- มีกรณีการใช้งานใดบ้างที่สามารถนำไปใช้ได้?
- องค์ประกอบ/โครงสร้างส่วนประกอบใดบ้างที่จำเป็นสำหรับการใช้งานรูปแบบการออกแบบนี้?
- มีข้อพิจารณาพิเศษใดบ้างสำหรับการใช้รูปแบบการออกแบบการใช้งานเครื่องมือเพื่อสร้าง AI agents ที่น่าเชื่อถือ?

## เป้าหมายการเรียนรู้

หลังจากทำบทเรียนนี้เสร็จสิ้น คุณจะสามารถ:

- นิยามรูปแบบการออกแบบการใช้งานเครื่องมือและวัตถุประสงค์ของมัน
- ระบุกรณีการใช้งานที่เหมาะสมกับการใช้รูปแบบการออกแบบการใช้งานเครื่องมือ
- เข้าใจองค์ประกอบสำคัญที่จำเป็นสำหรับการใช้งานรูปแบบการออกแบบนี้
- รับรู้ข้อพิจารณาสำหรับการประกันความน่าเชื่อถือของ AI agents ที่ใช้รูปแบบนี้

## รูปแบบการออกแบบการใช้งานเครื่องมือคืออะไร?

**รูปแบบการออกแบบการใช้งานเครื่องมือ** เน้นการให้ LLMs สามารถโต้ตอบกับเครื่องมือภายนอกเพื่อบรรลุเป้าหมายเฉพาะ เครื่องมือคือโค้ดที่ตัวแทนสามารถรันเพื่อทำงาน เครื่องมืออาจเป็นฟังก์ชันง่าย ๆ เช่น เครื่องคิดเลข หรือการเรียก API ไปยังบริการภายนอกเช่นการดูราคาหุ้นหรือพยากรณ์อากาศ ในบริบทของ AI agents เครื่องมือถูกออกแบบมาเพื่อนำไปใช้โดยตัวแทนตอบสนองต่อ **คำสั่งฟังก์ชันที่สร้างโดยโมเดล**

## มีกรณีการใช้งานใดบ้างที่สามารถนำไปใช้ได้?

AI Agents สามารถใช้เครื่องมือเพื่อทำงานที่ซับซ้อน ดึงข้อมูล หรือช่วยตัดสินใจ รูปแบบการออกแบบการใช้งานเครื่องมือมักใช้ในสถานการณ์ที่ต้องมีการโต้ตอบแบบไดนามิกกับระบบภายนอก เช่น ฐานข้อมูล บริการเว็บ หรือโปรแกรมแปลความหมายโค้ด ความสามารถนี้เหมาะกับกรณีการใช้งานหลายประเภท ได้แก่:

- **การดึงข้อมูลแบบไดนามิก:** ตัวแทนสามารถเรียกใช้ API ภายนอกหรือฐานข้อมูลเพื่อดึงข้อมูลล่าสุด (เช่น การค้นหาข้อมูลจากฐานข้อมูล SQLite เพื่อวิเคราะห์ข้อมูล การดึงราคาหุ้นหรือข้อมูลสภาพอากาศ)
- **การรันและแปลความหมายโค้ด:** ตัวแทนสามารถรันโค้ดหรือสคริปต์เพื่อแก้ไขปัญหาคณิตศาสตร์ สร้างรายงาน หรือจำลองสถานการณ์
- **การทำงานอัตโนมัติในขั้นตอนทำงาน:** อัตโนมัติงานที่ซ้ำซ้อนหรือประกอบด้วยหลายขั้นตอนโดยการรวมเครื่องมือเช่น ตัวจัดการงาน บริการอีเมล หรือสายข้อมูล
- **การสนับสนุนลูกค้า:** ตัวแทนสามารถโต้ตอบกับระบบ CRM, แพลตฟอร์มจัดการตั๋ว หรือฐานความรู้เพื่อแก้ไขปัญหาของผู้ใช้
- **การสร้างและแก้ไขเนื้อหา:** ตัวแทนสามารถใช้เครื่องมือตรวจสอบไวยากรณ์ สรุปข้อความ หรือประเมินความปลอดภัยของเนื้อหาเพื่อช่วยในงานสร้างสรรค์เนื้อหา

## องค์ประกอบ/โครงสร้างส่วนประกอบที่จำเป็นสำหรับการใช้งานรูปแบบการออกแบบการใช้งานเครื่องมือคืออะไร?

โครงสร้างส่วนประกอบเหล่านี้ช่วยให้ AI agent สามารถทำงานได้หลากหลาย มาดูองค์ประกอบสำคัญที่จำเป็นสำหรับการใช้งานรูปแบบการออกแบบการใช้งานเครื่องมือ:

- **ฟังก์ชัน/สคีมาของเครื่องมือ:** นิยามรายละเอียดของเครื่องมือที่มีอยู่ รวมถึงชื่อฟังก์ชัน วัตถุประสงค์ พารามิเตอร์ที่ต้องการ และผลลัพธ์ที่คาดหวัง สคีมเหล่านี้ช่วยให้ LLM เข้าใจว่าเครื่องมือไหนมีและวิธีขอใช้งานที่ถูกต้อง

- **ตรรกะการเรียกใช้ฟังก์ชัน:** กำหนดวิธีและเวลาที่เครื่องมือถูกเรียกใช้ตามเจตนาของผู้ใช้และบริบทของบทสนทนา อาจรวมถึงโมดูลการวางแผน กลไกการเส้นทาง หรือเงื่อนไขที่กำหนดการใช้งานเครื่องมือแบบไดนามิก

- **ระบบจัดการข้อความ:** ส่วนประกอบที่จัดการบทสนทนาระหว่างอินพุตของผู้ใช้ การตอบของ LLM การเรียกเครื่องมือ และผลลัพธ์จากเครื่องมือ

- **โครงสร้างการรวมเครื่องมือ:** โครงสร้างพื้นฐานที่เชื่อมโยงตัวแทนกับเครื่องมือต่าง ๆ ไม่ว่าจะเป็นฟังก์ชันง่าย ๆ หรือบริการภายนอกที่ซับซ้อน

- **การจัดการข้อผิดพลาดและการตรวจสอบความถูกต้อง:** กลไกจัดการความล้มเหลวในการรันเครื่องมือ ตรวจสอบพารามิเตอร์ และจัดการการตอบกลับที่ไม่คาดคิด

- **การจัดการสถานะ:** ติดตามบริบทของบทสนทนา ปฏิสัมพันธ์กับเครื่องมือก่อนหน้า และข้อมูลถาวรเพื่อรับประกันความสอดคล้องระหว่างหลายรอบของการสนทนา

ถัดไปมาดูรายละเอียดของการเรียกใช้ฟังก์ชัน/เครื่องมือกัน

### การเรียกใช้ฟังก์ชัน/เครื่องมือ

การเรียกใช้ฟังก์ชันเป็นวิธีหลักที่ช่วยให้ Large Language Models (LLMs) สามารถโต้ตอบกับเครื่องมือ คุณจะมักเห็นคำว่า 'Function' และ 'Tool' ใช้แทนกันได้เพราะ 'ฟังก์ชัน' (บล็อกของโค้ดที่นำกลับมาใช้ใหม่ได้) เป็น 'เครื่องมือ' ที่ตัวแทนใช้ทำงาน เพื่อให้โค้ดของฟังก์ชันถูกรัน LLM ต้องเปรียบเทียบคำขอของผู้ใช้กับคำอธิบายของฟังก์ชัน เพื่อทำสิ่งนี้ สคีมาที่มีคำอธิบายของฟังก์ชันทั้งหมดจะถูกส่งไปยัง LLM จากนั้น LLM จะเลือกฟังก์ชันที่เหมาะสมที่สุดสำหรับงานและส่งคืนชื่อและอาร์กิวเมนต์ ฟังก์ชันที่เลือกจะถูกเรียกใช้ ผลลัพธ์จะถูกส่งกลับไปยัง LLM ซึ่งใช้ข้อมูลนั้นเพื่อตอบคำถามของผู้ใช้

สำหรับนักพัฒนาที่ต้องการใช้งานการเรียกฟังก์ชันสำหรับเอเจนต์ คุณต้องมี:

1. โมเดล LLM ที่รองรับการเรียกฟังก์ชัน
2. สคีมาที่มีคำอธิบายฟังก์ชัน
3. โค้ดของแต่ละฟังก์ชันที่อธิบายไว้

สมมุติใช้ตัวอย่างการรับเวลาปัจจุบันในเมืองมาอธิบาย:

1. **เริ่มต้น LLM ที่รองรับการเรียกฟังก์ชัน:**

    ไม่ใช่ทุกโมเดลที่รองรับการเรียกฟังก์ชัน ดังนั้นจึงสำคัญที่จะต้องตรวจสอบว่า LLM ที่คุณใช้รองรับหรือไม่  
    <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> รองรับการเรียกฟังก์ชัน เราสามารถเริ่มต้นโดยการสร้าง client ของ Azure OpenAI  

    ```python
    # เริ่มต้นไคลเอนต์ Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **สร้างสคีมาฟังก์ชัน:**

    ต่อไปเราจะกำหนดสคีมา JSON ที่มีชื่อฟังก์ชัน คำอธิบายฟังก์ชัน และชื่อและคำอธิบายของพารามิเตอร์  
    จากนั้นเราจะส่งสคีมาไปยัง client ที่สร้างขึ้นก่อนหน้า พร้อมทั้งคำขอของผู้ใช้เพื่อหาว่าเวลาที่ซานฟรานซิสโกเป็นเวลาใด สิ่งที่สำคัญคือ **การเรียกเครื่องมือ** เท่านั้นที่ถูกส่งกลับมา **ไม่ใช่** คำตอบสุดท้ายของคำถาม ตามที่กล่าวไปก่อนหน้านี้ LLM จะส่งคืนชื่อฟังก์ชันที่เลือกสำหรับงาน และอาร์กิวเมนต์ที่จะส่งให้กับฟังก์ชันนั้น

    ```python
    # คำอธิบายฟังก์ชันสำหรับโมเดลในการอ่าน
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
   
    ```python
  
    # ข้อความผู้ใช้เริ่มต้น
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # การเรียก API ครั้งแรก: ขอให้โมเดลใช้ฟังก์ชัน
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # ประมวลผลการตอบกลับของโมเดล
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **โค้ดฟังก์ชันที่ใช้ทำงาน:**

    ตอนนี้ LLM ได้เลือกฟังก์ชันที่ต้องรันแล้ว เราต้องเขียนโค้ดเพื่อนำไปสู่การดำเนินงานและรันโค้ดนั้น  
    เราสามารถเขียนโค้ดเพื่อดึงเวลาปัจจุบันในภาษา Python ได้ นอกจากนี้เรายังต้องเขียนโค้ดเพื่อสกัดชื่อและอาร์กิวเมนต์จาก response_message เพื่อให้ได้ผลลัพธ์สุดท้าย

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
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # การเรียก API ครั้งที่สอง: รับคำตอบสุดท้ายจากโมเดล
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

การเรียกฟังก์ชันเป็นหัวใจของการออกแบบการใช้งานเครื่องมือของเอเจนต์ส่วนใหญ่ ถ้าไม่ใช่ทั้งหมด อย่างไรก็ตาม การลงมือทำจากศูนย์อาจจะท้าทายในบางครั้ง  
อย่างที่เราได้เรียนรู้ใน [บทเรียน 2](../../../02-explore-agentic-frameworks) เฟรมเวิร์กเอเจนต์ช่วยให้เรามีบล็อกที่สร้างไว้ล่วงหน้าเพื่อนำไปใช้งานการใช้เครื่องมือได้

## ตัวอย่างการใช้งานเครื่องมือด้วยเอเจนต์เฟรมเวิร์ก

นี่คือตัวอย่างบางส่วนของวิธีการใช้งานรูปแบบการออกแบบการใช้งานเครื่องมือโดยใช้เฟรมเวิร์กเอเจนต์ที่แตกต่างกัน:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> เป็นเฟรมเวิร์ก AI แบบโอเพนซอร์สสำหรับสร้าง AI agents ช่วยให้ง่ายต่อการใช้การเรียกฟังก์ชันโดยให้คุณกำหนดเครื่องมือเป็นฟังก์ชัน Python ที่ใช้ @tool ตกแต่งเฟรมเวิร์กจัดการการสื่อสารสองทางระหว่างโมเดลกับโค้ดของคุณ นอกจากนี้ยังให้เข้าถึงเครื่องมือที่สร้างไว้ล่วงหน้า เช่น File Search และ Code Interpreter ผ่าน `AzureAIProjectAgentProvider`

แผนภาพต่อไปนี้แสดงกระบวนการเรียกฟังก์ชันกับ Microsoft Agent Framework:

![function calling](../../../translated_images/th/functioncalling-diagram.a84006fc287f6014.webp)

ใน Microsoft Agent Framework เครื่องมือถูกกำหนดเป็นฟังก์ชันที่มีการตกแต่งด้วย @tool เราสามารถแปลงฟังก์ชัน `get_current_time` ที่ดูมาก่อนหน้านี้ให้เป็นเครื่องมือได้โดยใช้การตกแต่ง `@tool` เฟรมเวิร์กจะจัดการการแปลงฟังก์ชันและพารามิเตอร์ให้อยู่ในรูปแบบสคีมาเพื่อส่งไปยัง LLM โดยอัตโนมัติ

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# สร้างไคลเอนต์
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# สร้างเอเย่นต์และรันด้วยเครื่องมือ
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### บริการ Azure AI Agent

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">บริการ Azure AI Agent</a> เป็นเฟรมเวิร์กเอเจนต์รุ่นใหม่ที่ออกแบบมาเพื่อช่วยนักพัฒนาให้สร้าง ใช้งาน และขยาย AI agents ที่มีคุณภาพสูงและขยายขนาดได้อย่างปลอดภัยและง่ายดายโดยไม่ต้องจัดการกับทรัพยากรคอมพิวเตอร์และที่เก็บข้อมูลเอง เหมาะเป็นพิเศษกับการใช้งานในองค์กรเพราะเป็นบริการที่มีการจัดการเต็มรูปแบบพร้อมความปลอดภัยระดับองค์กร

เมื่อเทียบกับการพัฒนาด้วย LLM API โดยตรง บริการ Azure AI Agent มีข้อดีหลายประการ เช่น:

- การเรียกใช้เครื่องมืออัตโนมัติ – ไม่ต้องแยกวิเคราะห์การเรียกเครื่องมือ เรียกใช้เครื่องมือ และจัดการผลลัพธ์; ทั้งหมดนี้ทำบนเซิร์ฟเวอร์
- การจัดการข้อมูลอย่างปลอดภัย – แทนการจัดการสถานะของบทสนทนาเอง คุณสามารถใช้ threads ซึ่งเก็บประวัติข้อความจากการสนทนาแต่ละรายการ
- เครื่องมือพร้อมใช้งานทันที – มีเครื่องมือที่ใช้โต้ตอบกับแหล่งข้อมูลของคุณ เช่น Bing, Azure AI Search และ Azure Functions

เครื่องมือที่มีในบริการ Azure AI Agent แบ่งออกเป็นสองกลุ่ม:

1. เครื่องมือความรู้:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">แหล่งข้อมูลด้วย Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ค้นหาไฟล์</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. เครื่องมือปฏิบัติการ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">การเรียกใช้ฟังก์ชัน</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">โปรแกรมแปลความหมายโค้ด</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">เครื่องมือที่กำหนดโดย OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

บริการ Agent ช่วยให้เราสามารถใช้เครื่องมือเหล่านี้รวมกันเป็น `toolset` และยังใช้ `threads` ที่ติดตามประวัติข้อความจากการสนทนาใดสนทนาหนึ่งได้

สมมุติว่าคุณเป็นตัวแทนฝ่ายขายที่บริษัทชื่อ Contoso คุณต้องการสร้างตัวแทนสนทนาที่สามารถตอบคำถามเกี่ยวกับข้อมูลยอดขายของคุณ

ภาพต่อไปนี้แสดงวิธีที่คุณสามารถใช้บริการ Azure AI Agent ในการวิเคราะห์ข้อมูลยอดขายของคุณ:

![Agentic Service In Action](../../../translated_images/th/agent-service-in-action.34fb465c9a84659e.webp)

เพื่อใช้เครื่องมือใด ๆ กับบริการนี้ เราสามารถสร้าง client และกำหนดเครื่องมือหรือชุดเครื่องมือ ในการใช้งานจริง เราสามารถใช้โค้ด Python ดังต่อไปนี้ LLM จะสามารถดู toolset และตัดสินใจว่าจะใช้ฟังก์ชันที่ผู้ใช้สร้างขึ้น `fetch_sales_data_using_sqlite_query` หรือ Code Interpreter ที่สร้างไว้ล่วงหน้าขึ้นอยู่กับคำขอของผู้ใช้

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

# เริ่มตัวแทนเรียกฟังก์ชันด้วยฟังก์ชัน fetch_sales_data_using_sqlite_query และเพิ่มเข้าสู่ชุดเครื่องมือ
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# เริ่มเครื่องมือ Code Interpreter และเพิ่มเข้าสู่ชุดเครื่องมือ
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ข้อพิจารณาพิเศษสำหรับการใช้รูปแบบการออกแบบการใช้งานเครื่องมือเพื่อสร้าง AI agents ที่น่าเชื่อถือมีอะไรบ้าง?

ความกังวลที่พบบ่อยเกี่ยวกับ SQL ที่สร้างขึ้นแบบไดนามิกโดย LLM คือความปลอดภัย โดยเฉพาะความเสี่ยงของการโจมตี SQL injection หรือการกระทำที่เป็นอันตราย เช่น การลบหรือแก้ไขฐานข้อมูล แม้ว่าความกังวลเหล่านี้จะมีเหตุผล แต่สามารถลดความเสี่ยงได้อย่างมีประสิทธิภาพโดยการกำหนดสิทธิ์การเข้าถึงฐานข้อมูลอย่างเหมาะสม สำหรับฐานข้อมูลส่วนใหญ่หมายถึงการตั้งค่าให้ฐานข้อมูลเป็นแบบอ่านอย่างเดียว สำหรับบริการฐานข้อมูลเช่น PostgreSQL หรือ Azure SQL ควรกำหนดบทบาทของแอปเป็นแบบอ่านได้ (SELECT)

การรันแอปในสภาพแวดล้อมที่ปลอดภัยช่วยเพิ่มมาตรการป้องกันอีกด้วย ในสถานการณ์องค์กร ข้อมูลมักจะถูกสกัดและแปลงจากระบบปฏิบัติการเป็นฐานข้อมูลหรือคลังข้อมูลแบบอ่านอย่างเดียวที่มีสคีมาที่ใช้งานง่าย แนวทางนี้ช่วยให้ข้อมูลปลอดภัย มีประสิทธิภาพต่อการเข้าถึงและการทำงาน และแอปมีสิทธิ์ที่จำกัดเฉพาะการอ่านอย่างเดียว

## ตัวอย่างโค้ด

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## มีคำถามเพิ่มเติมเกี่ยวกับรูปแบบการออกแบบการใช้งานเครื่องมือไหม?

เข้าร่วมที่ [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) เพื่อพบปะกับผู้เรียนคนอื่น ๆ เข้าร่วมชั่วโมงสำนักงาน และรับคำตอบสำหรับคำถามเกี่ยวกับ AI Agents ของคุณ

## แหล่งข้อมูลเพิ่มเติม

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">เวิร์กช็อป Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">เวิร์กช็อป Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">ภาพรวม Microsoft Agent Framework</a>

## บทเรียนก่อนหน้า

[ทำความเข้าใจรูปแบบการออกแบบ Agentic](../03-agentic-design-patterns/README.md)

## บทเรียนถัดไป
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->