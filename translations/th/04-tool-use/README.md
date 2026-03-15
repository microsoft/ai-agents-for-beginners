[![วิธีออกแบบตัวแทน AI ที่ดี](../../../translated_images/th/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(คลิกที่รูปด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

# รูปแบบการออกแบบการใช้เครื่องมือ

เครื่องมือเป็นสิ่งที่น่าสนใจเพราะช่วยให้ตัวแทน AI มีขอบเขตความสามารถที่กว้างขึ้น แทนที่ตัวแทนจะมีชุดการกระทำที่จำกัด โดยการเพิ่มเครื่องมือ ตัวแทนสามารถใช้งานชุดการกระทำที่หลากหลายได้ ในบทนี้ เราจะมาดูรูปแบบการออกแบบการใช้เครื่องมือ (Tool Use Design Pattern) ซึ่งอธิบายว่าตัวแทน AI สามารถใช้เครื่องมือเฉพาะทางเพื่อให้บรรลุเป้าหมายได้อย่างไร

## บทนำ

ในบทเรียนนี้ เราตั้งใจจะตอบคำถามต่อไปนี้:

- รูปแบบการออกแบบการใช้เครื่องมือคืออะไร?
- มีกรณีการใช้งานใดบ้างที่สามารถนำไปใช้ได้?
- องค์ประกอบ/บล็อกพื้นฐานใดบ้างที่จำเป็นสำหรับการนำรูปแบบการออกแบบนี้ไปใช้งาน?
- สิ่งที่ต้องพิจารณาเป็นพิเศษเมื่อใช้รูปแบบการออกแบบการใช้เครื่องมือเพื่อสร้างตัวแทน AI ที่น่าเชื่อถือคืออะไร?

## เป้าหมายการเรียนรู้

หลังจากทำบทเรียนนี้เสร็จ คุณจะสามารถ:

- นิยามรูปแบบการออกแบบการใช้เครื่องมือและวัตถุประสงค์ของมัน
- ระบุกรณีการใช้งานที่เหมาะสมกับรูปแบบการออกแบบการใช้เครื่องมือ
- เข้าใจองค์ประกอบหลักที่จำเป็นในการนำรูปแบบการออกแบบไปใช้
- รับรู้ข้อพิจารณาต่าง ๆ เพื่อให้แน่ใจว่าตัวแทน AI ที่ใช้รูปแบบการออกแบบนี้มีความน่าเชื่อถือ

## รูปแบบการออกแบบการใช้เครื่องมือคืออะไร?

รูปแบบการออกแบบการใช้เครื่องมือ (Tool Use Design Pattern) มุ่งให้ความสามารถกับ LLMs ในการโต้ตอบกับเครื่องมือภายนอกเพื่อบรรลุเป้าหมายเฉพาะ เครื่องมือคือโค้ดที่ตัวแทนสามารถเรียกใช้งานเพื่อดำเนินการต่าง ๆ เครื่องมืออาจเป็นฟังก์ชันง่าย ๆ เช่น เครื่องคิดเลข หรือการเรียก API ไปยังบริการของบุคคลที่สาม เช่น การค้นหาราคาหุ้นหรือพยากรณ์อากาศ ในบริบทของตัวแทน AI เครื่องมือถูกออกแบบให้ถูกเรียกใช้งานโดยตัวแทนเพื่อตอบสนองต่อการ **เรียกฟังก์ชันที่สร้างโดยโมเดล** (model-generated function calls)

## มีกรณีการใช้งานใดบ้างที่สามารถนำไปใช้ได้?

ตัวแทน AI สามารถใช้เครื่องมือเพื่อทำภารกิจที่ซับซ้อน ดึงข้อมูล หรือช่วยในการตัดสินใจ รูปแบบการออกแบบการใช้เครื่องมือมักถูกใช้งานในสถานการณ์ที่ต้องการการโต้ตอบแบบไดนามิกกับระบบภายนอก เช่น ฐานข้อมูล บริการเว็บ หรือโปรแกรมตีความโค้ด ความสามารถนี้มีประโยชน์ในหลายกรณีการใช้งานต่าง ๆ รวมถึง:

- **การดึงข้อมูลแบบไดนามิก:** ตัวแทนสามารถสอบถาม API ภายนอกหรือฐานข้อมูลเพื่อดึงข้อมูลที่เป็นปัจจุบัน (เช่น การสอบถามฐานข้อมูล SQLite สำหรับการวิเคราะห์ข้อมูล การดึงราคาหุ้น หรือข้อมูลสภาพอากาศ)
- **การรันวิเคราะห์และตีความโค้ด:** ตัวแทนสามารถรันโค้ดหรือสคริปต์เพื่อแก้ปัญหาทางคณิตศาสตร์ สร้างรายงาน หรือรันการจำลองต่าง ๆ
- **การทำงานอัตโนมัติของเวิร์กโฟลว์:** ทำงานที่ซ้ำซ้อนหรือหลายขั้นตอนโดยรวมเครื่องมือเช่น ตัวจัดกำหนดงาน บริการอีเมล หรือสายการประมวลผลข้อมูล
- **การสนับสนุนลูกค้า:** ตัวแทนสามารถโต้ตอบกับระบบ CRM แพลตฟอร์มตั๋ว หรือฐานความรู้เพื่อตอบคำถามของผู้ใช้
- **การสร้างและแก้ไขเนื้อหา:** ตัวแทนสามารถใช้เครื่องมือตรวจไวยากรณ์ สรุปข้อความ หรือประเมินความปลอดภัยของเนื้อหาเพื่อช่วยในการสร้างเนื้อหา

## องค์ประกอบ/บล็อกพื้นฐานที่จำเป็นสำหรับการนำรูปแบบการออกแบบการใช้เครื่องมือไปใช้?

บล็อกพื้นฐานเหล่านี้ช่วยให้ตัวแทน AI สามารถทำงานหลากหลายได้ มาดูองค์ประกอบสำคัญที่จำเป็นในการนำรูปแบบการออกแบบการใช้เครื่องมือไปใช้:

- **สคีมา Function/Tool:** คำจำกัดความรายละเอียดของเครื่องมือที่พร้อมใช้งาน รวมถึงชื่อฟังก์ชัน วัตถุประสงค์ พารามิเตอร์ที่จำเป็น และผลลัพธ์ที่คาดหวัง สคีมาเหล่านี้ช่วยให้ LLM เข้าใจว่าเครื่องมือใดที่มีและวิธีการสร้างคำขอที่ถูกต้อง

- **ตรรกะการเรียกใช้งานฟังก์ชัน:** ควบคุมว่าควรเรียกใช้เครื่องมือเมื่อใดและอย่างไรตามความตั้งใจของผู้ใช้และบริบทการสนทนา อาจรวมถึงโมดูลวางแผน กลไกรูทติ้ง หรือโฟลว์แบบมีเงื่อนไขที่กำหนดการใช้เครื่องมือแบบไดนามิก

- **ระบบจัดการข้อความ:** ส่วนประกอบที่จัดการการไหลของการสนทนาระหว่างอินพุตของผู้ใช้ ตอบกลับของ LLM การเรียกเครื่องมือ และผลลัพธ์จากเครื่องมือ

- **กรอบการรวมเครื่องมือ:** โครงสร้างพื้นฐานที่เชื่อมต่อเอเจนต์กับเครื่องมือต่าง ๆ ไม่ว่าจะเป็นฟังก์ชันง่าย ๆ หรือบริการภายนอกที่ซับซ้อน

- **การจัดการข้อผิดพลาด & การตรวจสอบความถูกต้อง:** กลไกในการจัดการความล้มเหลวในการเรียกใช้เครื่องมือ ตรวจสอบพารามิเตอร์ และจัดการการตอบกลับที่ไม่คาดคิด

- **การจัดการสถานะ:** ติดตามบริบทการสนทนา การโต้ตอบกับเครื่องมือก่อนหน้า และข้อมูลถาวรเพื่อให้แน่ใจถึงความสอดคล้องในการโต้ตอบหลายเทิร์น

ต่อไป เรามาดูรายละเอียดของการเรียก Function/Tool กัน

### การเรียก Function/Tool

การเรียกฟังก์ชันเป็นวิธีหลักที่เราเปิดโอกาสให้ Large Language Models (LLMs) โต้ตอบกับเครื่องมือ คุณจะเห็นคำว่า 'Function' และ 'Tool' ถูกใช้สลับกันเพราะ 'ฟังก์ชัน' (บล็อกโค้ดที่นำกลับมาใช้ใหม่ได้) คือ 'เครื่องมือ' ที่ตัวแทนใช้ในการทำงาน เพื่อให้โค้ดของฟังก์ชันถูกเรียกใช้งาน โมเดลต้องเปรียบเทียบคำขอของผู้ใช้กับคำอธิบายของฟังก์ชัน ในการทำเช่นนี้ สคีมาที่มีคำอธิบายของฟังก์ชันทั้งหมดจะถูกส่งไปยัง LLM จากนั้น LLM จะเลือกฟังก์ชันที่เหมาะสมที่สุดสำหรับงานและส่งกลับชื่อและอาร์กิวเมนต์ ฟังก์ชันที่ถูกเลือกจะถูกเรียกใช้งาน ผลลัพธ์จะถูกส่งกลับไปยัง LLM ซึ่งจะใช้ข้อมูลนั้นเพื่อตอบคำขอของผู้ใช้

สำหรับนักพัฒนาเพื่ออิมพลีเมนต์การเรียกฟังก์ชันสำหรับเอเจนต์ คุณจะต้องมี:

1. โมเดล LLM ที่รองรับการเรียกฟังก์ชัน
2. สคีมาที่มีคำอธิบายฟังก์ชัน
3. โค้ดของแต่ละฟังก์ชันที่อธิบายไว้

ให้ยกตัวอย่างการดึงเวลาปัจจุบันในเมืองหนึ่งเพื่ออธิบาย:

1. **เริ่มต้น LLM ที่รองรับการเรียกฟังก์ชัน:**

    ไม่ใช่ทุกโมเดลที่รองรับการเรียกฟังก์ชัน ดังนั้นจึงสำคัญที่จะต้องตรวจสอบว่า LLM ที่คุณใช้รองรับหรือไม่     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> รองรับการเรียกฟังก์ชัน เราสามารถเริ่มต้นโดยการสร้าง client ของ Azure OpenAI ได้

    ```python
    # เริ่มต้นไคลเอนต์ Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **สร้างสคีมาฟังก์ชัน:**

    ต่อไปเราจะกำหนดสคีมา JSON ที่ประกอบด้วยชื่อฟังก์ชัน คำอธิบายของสิ่งที่ฟังก์ชันทำ และชื่อพร้อมคำอธิบายของพารามิเตอร์ของฟังก์ชัน
    จากนั้นเราจะนำสคีมานี้ไปส่งให้กับ client ที่สร้างไว้ก่อนหน้านี้ พร้อมกับคำขอของผู้ใช้ที่จะหาว่าเวลาตอนนี้ใน San Francisco เป็นอย่างไร สิ่งสำคัญที่ต้องทราบคือ **การเรียกเครื่องมือ** คือสิ่งที่ถูกส่งกลับมา **ไม่ใช่** คำตอบสุดท้ายตามคำถาม ตามที่กล่าวไว้ข้างต้น LLM จะส่งกลับชื่อของฟังก์ชันที่มันเลือกสำหรับงาน และอาร์กิวเมนต์ที่จะส่งให้กับฟังก์ชันนั้น

    ```python
    # คำอธิบายฟังก์ชันสำหรับให้โมเดลอ่าน
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
  
    # ข้อความเริ่มต้นของผู้ใช้
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
  
1. **โค้ดของฟังก์ชันที่จำเป็นในการทำงานให้สำเร็จ:**

    ตอนนี้เมื่อ LLM เลือกแล้วว่าจำเป็นต้องรันฟังก์ชันใด โค้ดที่ทำหน้าที่นั้นต้องถูกอิมพลีเมนต์และรัน
    เราสามารถอิมพลีเมนต์โค้ดเพื่อหาตอนปัจจุบันใน Python ได้ นอกจากนี้เรายังต้องเขียนโค้ดเพื่อดึงชื่อและอาร์กิวเมนต์จาก response_message เพื่อให้ได้ผลลัพธ์สุดท้าย

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

การเรียกฟังก์ชันเป็นแกนหลักของรูปแบบการใช้เครื่องมือสำหรับเอเจนต์ส่วนใหญ่ หากไม่ทั้งหมด อย่างไรก็ตามการอิมพลีเมนต์มันตั้งแต่ต้นอาจเป็นเรื่องท้าทาย
อย่างที่เราเรียนรู้ใน [Lesson 2](../../../02-explore-agentic-frameworks) แพลตฟอร์มเอเจนติกให้บล็อกพื้นฐานที่สร้างไว้ล่วงหน้าเพื่ออิมพลีเมนต์การใช้เครื่องมือได้

## ตัวอย่างการใช้เครื่องมือกับแพลตฟอร์มเอเจนติก

นี่คือตัวอย่างบางส่วนของวิธีที่คุณสามารถนำรูปแบบการออกแบบการใช้เครื่องมือไปใช้โดยใช้แพลตฟอร์มเอเจนติกต่าง ๆ:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> เป็นเฟรมเวิร์ก AI แบบโอเพนซอร์สสำหรับการสร้างตัวแทน AI มันช่วยให้งานการใช้การเรียกฟังก์ชันง่ายขึ้นด้วยการอนุญาตให้คุณนิยามเครื่องมือเป็นฟังก์ชัน Python พร้อมตัวตกแต่ง `@tool` เฟรมเวิร์กจะจัดการการสื่อสารไปมาระหว่างโมเดลและโค้ดของคุณโดยอัตโนมัติ นอกจากนี้ยังให้การเข้าถึงเครื่องมือที่สร้างไว้ล่วงหน้า เช่น File Search และ Code Interpreter ผ่าน `AzureAIProjectAgentProvider`

ไดอะแกรมด้านล่างแสดงกระบวนการของการเรียกฟังก์ชันกับ Microsoft Agent Framework:

![การเรียกฟังก์ชัน](../../../translated_images/th/functioncalling-diagram.a84006fc287f6014.webp)

ใน Microsoft Agent Framework เครื่องมือถูกนิยามเป็นฟังก์ชันที่มีตัวตกแต่ง เราสามารถแปลงฟังก์ชัน `get_current_time` ที่เห็นก่อนหน้านี้ให้เป็นเครื่องมือโดยใช้ตัวตกแต่ง `@tool` เฟรมเวิร์กจะทำการซีเรียลไลซ์ฟังก์ชันและพารามิเตอร์โดยอัตโนมัติ เพื่อสร้างสคีมาที่จะส่งไปยัง LLM

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

# สร้างเอเจนต์และรันด้วยเครื่องมือ
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> เป็นแพลตฟอร์มเอเจนติกรุ่นใหม่ที่ออกแบบมาเพื่อให้นักพัฒนาสามารถสร้าง ปรับใช้ และสเกลตัวแทน AI คุณภาพสูงที่ขยายได้อย่างปลอดภัยโดยไม่ต้องจัดการทรัพยากรคอมพิวต์และสตอเรจพื้นฐาน เหมาะอย่างยิ่งสำหรับแอปพลิเคชันองค์กรเนื่องจากเป็นบริการที่มีการจัดการเต็มรูปแบบพร้อมมาตรฐานความปลอดภัยระดับองค์กร

เมื่อเทียบกับการพัฒนาด้วย LLM API โดยตรง Azure AI Agent Service ให้ข้อได้เปรียบบางอย่าง รวมถึง:

- การเรียกเครื่องมืออัตโนมัติ – ไม่จำเป็นต้องแยกวิเคราะห์การเรียกเครื่องมือ เรียกใช้เครื่องมือ และจัดการผลลัพธ์; ทั้งหมดนี้ทำที่ฝั่งเซิร์ฟเวอร์
- การจัดการข้อมูลอย่างปลอดภัย – แทนที่จะจัดการสถานะการสนทนาเอง คุณสามารถพึ่งพา threads เพื่อเก็บข้อมูลทั้งหมดที่คุณต้องการ
- เครื่องมือพร้อมใช้งานทันที – เครื่องมือที่คุณสามารถใช้เพื่อโต้ตอบกับแหล่งข้อมูลของคุณ เช่น Bing, Azure AI Search, และ Azure Functions

เครื่องมือที่มีใน Azure AI Agent Service สามารถแบ่งเป็นสองหมวดหมู่:

1. เครื่องมือเชิงความรู้:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. เครื่องมือเชิงการกระทำ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service อนุญาตให้เราใช้เครื่องมือเหล่านี้ร่วมกันเป็น `toolset` ได้ นอกจากนี้ยังใช้ `threads` เพื่อเก็บประวัติข้อความจากการสนทนาแต่ละรายการ

ลองจินตนาการว่าคุณเป็นตัวแทนฝ่ายขายที่บริษัทชื่อ Contoso คุณต้องการพัฒนาตัวแทนสนทนาที่สามารถตอบคำถามเกี่ยวกับข้อมูลยอดขายของคุณได้

ภาพต่อไปนี้แสดงวิธีที่คุณอาจใช้ Azure AI Agent Service เพื่อวิเคราะห์ข้อมูลยอดขายของคุณ:

![การทำงานของบริการเอเจนต์](../../../translated_images/th/agent-service-in-action.34fb465c9a84659e.webp)

ในการใช้เครื่องมือใด ๆ กับบริการนี้ เราสามารถสร้าง client และกำหนดเครื่องมือหรือ toolset ในการใช้งานจริง เราสามารถใช้โค้ด Python ต่อไปนี้ โมเดลจะสามารถดู toolset และตัดสินใจว่าจะใช้ฟังก์ชันที่ผู้ใช้สร้าง `fetch_sales_data_using_sqlite_query` หรือ Code Interpreter ที่สร้างไว้ล่วงหน้าขึ้นอยู่กับคำขอของผู้ใช้

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

# เริ่มต้นเอเจนต์เรียกฟังก์ชันด้วยฟังก์ชัน fetch_sales_data_using_sqlite_query และเพิ่มเข้าไปในชุดเครื่องมือ
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# เริ่มต้นเครื่องมือ Code Interpreter และเพิ่มเข้าไปในชุดเครื่องมือ
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## สิ่งที่ต้องพิจารณาเป็นพิเศษเมื่อใช้รูปแบบการออกแบบการใช้เครื่องมือเพื่อสร้างตัวแทน AI ที่น่าเชื่อถือ?

ความกังวลทั่วไปกับ SQL ที่สร้างขึ้นแบบไดนามิกโดย LLMs คือความปลอดภัย โดยเฉพาะความเสี่ยงจากการโจมตีแบบ SQL injection หรือการกระทำที่เป็นอันตราย เช่น การลบหรือดัดแปลงฐานข้อมูล แม้ว่าข้อกังวลเหล่านี้จะมีเหตุผล แต่สามารถบรรเทาได้อย่างมีประสิทธิภาพโดยการกำหนดสิทธิ์การเข้าถึงฐานข้อมูลอย่างเหมาะสม สำหรับฐานข้อมูลส่วนใหญ่สิ่งนี้เกี่ยวข้องกับการกำหนดฐานข้อมูลให้เป็นแบบอ่านอย่างเดียว (read-only) สำหรับบริการฐานข้อมูลเช่น PostgreSQL หรือ Azure SQL ควรกำหนดบทบาทแอปให้เป็นแบบอ่านอย่างเดียว (SELECT)

การรันแอปในสภาพแวดล้อมที่ปลอดภัยยิ่งขึ้นจะเพิ่มการป้องกัน ในสถานการณ์องค์กร ข้อมูลมักถูกสกัดและแปลงจากระบบปฏิบัติการไปยังฐานข้อมูลแบบอ่านอย่างเดียวหรือคลังข้อมูล (data warehouse) ที่มีสคีมาเป็นมิตรกับผู้ใช้ แนวทางนี้ช่วยรับประกันว่าข้อมูลปลอดภัย ปรับแต่งเพื่อประสิทธิภาพและการเข้าถึง และแอปมีสิทธิ์เฉพาะแบบอ่านอย่างเดียว

## ตัวอย่างโค้ด

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## มีคำถามเพิ่มเติมเกี่ยวกับรูปแบบการออกแบบการใช้เครื่องมือไหม?

เข้าร่วม [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) เพื่อพบกับผู้เรียนคนอื่น ๆ เข้าร่วมชั่วโมงที่ปรึกษา และรับคำตอบสำหรับคำถามเกี่ยวกับ AI Agents ของคุณ

## แหล่งข้อมูลเพิ่มเติม

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## บทเรียนก่อนหน้า

[เข้าใจรูปแบบการออกแบบเอเจนติก](../03-agentic-design-patterns/README.md)

## บทเรียนถัดไป
[เอเจนติก RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ข้อจำกัดความรับผิดชอบ:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลด้วยปัญญาประดิษฐ์ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่มีอำนาจสำหรับข้อมูลดังกล่าว สำหรับข้อมูลที่มีความสำคัญ แนะนำให้ใช้การแปลโดยนักแปลมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใดๆ ที่เกิดขึ้นจากการใช้การแปลฉบับนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->