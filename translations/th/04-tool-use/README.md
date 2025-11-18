<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T17:33:57+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "th"
}
-->
[![วิธีออกแบบ AI Agents ที่ดี](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.th.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(คลิกที่ภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

# รูปแบบการออกแบบการใช้เครื่องมือ

เครื่องมือเป็นสิ่งที่น่าสนใจเพราะช่วยให้ AI Agents มีความสามารถที่หลากหลายมากขึ้น แทนที่ตัว Agent จะมีชุดการกระทำที่จำกัด เมื่อเพิ่มเครื่องมือเข้าไป ตัว Agent จะสามารถทำการกระทำได้หลากหลายมากขึ้น ในบทนี้ เราจะมาดูรูปแบบการออกแบบการใช้เครื่องมือ ซึ่งอธิบายว่า AI Agents สามารถใช้เครื่องมือเฉพาะเพื่อบรรลุเป้าหมายได้อย่างไร

## บทนำ

ในบทเรียนนี้ เราจะพยายามตอบคำถามต่อไปนี้:

- รูปแบบการออกแบบการใช้เครื่องมือคืออะไร?
- มีกรณีการใช้งานใดบ้างที่สามารถนำไปใช้ได้?
- องค์ประกอบ/ส่วนประกอบที่จำเป็นในการนำรูปแบบการออกแบบนี้ไปใช้มีอะไรบ้าง?
- มีข้อควรพิจารณาอะไรบ้างในการใช้รูปแบบการออกแบบการใช้เครื่องมือเพื่อสร้าง AI Agents ที่น่าเชื่อถือ?

## เป้าหมายการเรียนรู้

หลังจากจบบทเรียนนี้ คุณจะสามารถ:

- อธิบายรูปแบบการออกแบบการใช้เครื่องมือและวัตถุประสงค์ของมัน
- ระบุกรณีการใช้งานที่รูปแบบการออกแบบการใช้เครื่องมือสามารถนำไปใช้ได้
- เข้าใจองค์ประกอบสำคัญที่จำเป็นในการนำรูปแบบการออกแบบนี้ไปใช้
- ตระหนักถึงข้อควรพิจารณาเพื่อให้มั่นใจในความน่าเชื่อถือของ AI Agents ที่ใช้รูปแบบการออกแบบนี้

## รูปแบบการออกแบบการใช้เครื่องมือคืออะไร?

**รูปแบบการออกแบบการใช้เครื่องมือ** มุ่งเน้นไปที่การให้ LLMs มีความสามารถในการโต้ตอบกับเครื่องมือภายนอกเพื่อบรรลุเป้าหมายเฉพาะ เครื่องมือคือโค้ดที่สามารถถูกเรียกใช้โดย Agent เพื่อทำการกระทำต่างๆ เครื่องมืออาจเป็นฟังก์ชันง่ายๆ เช่น เครื่องคิดเลข หรือการเรียก API ไปยังบริการของบุคคลที่สาม เช่น การค้นหาราคาหุ้นหรือพยากรณ์อากาศ ในบริบทของ AI Agents เครื่องมือถูกออกแบบมาให้ถูกเรียกใช้โดย Agents เพื่อตอบสนองต่อ **การเรียกฟังก์ชันที่สร้างโดยโมเดล**

## มีกรณีการใช้งานใดบ้างที่สามารถนำไปใช้ได้?

AI Agents สามารถใช้เครื่องมือเพื่อทำงานที่ซับซ้อน ดึงข้อมูล หรือทำการตัดสินใจ รูปแบบการออกแบบการใช้เครื่องมือมักถูกใช้ในสถานการณ์ที่ต้องการการโต้ตอบแบบไดนามิกกับระบบภายนอก เช่น ฐานข้อมูล บริการเว็บ หรือเครื่องมือแปลโค้ด ความสามารถนี้มีประโยชน์ในกรณีการใช้งานที่หลากหลาย เช่น:

- **การดึงข้อมูลแบบไดนามิก:** Agents สามารถเรียก API ภายนอกหรือฐานข้อมูลเพื่อดึงข้อมูลล่าสุด (เช่น การค้นหาฐานข้อมูล SQLite เพื่อวิเคราะห์ข้อมูล การดึงราคาหุ้นหรือข้อมูลสภาพอากาศ)
- **การรันและแปลโค้ด:** Agents สามารถรันโค้ดหรือสคริปต์เพื่อแก้ปัญหาทางคณิตศาสตร์ สร้างรายงาน หรือทำการจำลอง
- **การทำงานอัตโนมัติในกระบวนการทำงาน:** การทำงานซ้ำๆ หรือกระบวนการหลายขั้นตอนโดยการรวมเครื่องมือ เช่น ตัวจัดการงาน บริการอีเมล หรือสายข้อมูล
- **การสนับสนุนลูกค้า:** Agents สามารถโต้ตอบกับระบบ CRM แพลตฟอร์มการจัดการตั๋ว หรือฐานความรู้เพื่อแก้ไขคำถามของผู้ใช้
- **การสร้างและแก้ไขเนื้อหา:** Agents สามารถใช้เครื่องมือ เช่น ตัวตรวจสอบไวยากรณ์ ตัวสรุปข้อความ หรือผู้ประเมินความปลอดภัยของเนื้อหาเพื่อช่วยในงานสร้างเนื้อหา

## องค์ประกอบ/ส่วนประกอบที่จำเป็นในการนำรูปแบบการออกแบบการใช้เครื่องมือไปใช้มีอะไรบ้าง?

องค์ประกอบเหล่านี้ช่วยให้ AI Agent สามารถทำงานที่หลากหลายได้ มาดูองค์ประกอบสำคัญที่จำเป็นในการนำรูปแบบการออกแบบการใช้เครื่องมือไปใช้:

- **Schemas ของฟังก์ชัน/เครื่องมือ:** คำอธิบายรายละเอียดของเครื่องมือที่มีอยู่ รวมถึงชื่อฟังก์ชัน วัตถุประสงค์ พารามิเตอร์ที่จำเป็น และผลลัพธ์ที่คาดหวัง Schemas เหล่านี้ช่วยให้ LLM เข้าใจว่าเครื่องมือใดที่มีอยู่และวิธีสร้างคำขอที่ถูกต้อง
- **ตรรกะการเรียกใช้ฟังก์ชัน:** กำหนดวิธีและเวลาที่เครื่องมือถูกเรียกใช้ตามเจตนาของผู้ใช้และบริบทของการสนทนา อาจรวมถึงโมดูลวางแผน กลไกการกำหนดเส้นทาง หรือโฟลว์ตามเงื่อนไขที่กำหนดการใช้เครื่องมือแบบไดนามิก
- **ระบบจัดการข้อความ:** ส่วนประกอบที่จัดการการไหลของการสนทนาระหว่างอินพุตของผู้ใช้ การตอบสนองของ LLM การเรียกเครื่องมือ และผลลัพธ์ของเครื่องมือ
- **กรอบการรวมเครื่องมือ:** โครงสร้างพื้นฐานที่เชื่อมต่อ Agent กับเครื่องมือต่างๆ ไม่ว่าจะเป็นฟังก์ชันง่ายๆ หรือบริการภายนอกที่ซับซ้อน
- **การจัดการข้อผิดพลาดและการตรวจสอบ:** กลไกในการจัดการความล้มเหลวในการเรียกใช้เครื่องมือ ตรวจสอบพารามิเตอร์ และจัดการการตอบสนองที่ไม่คาดคิด
- **การจัดการสถานะ:** ติดตามบริบทของการสนทนา การโต้ตอบกับเครื่องมือก่อนหน้า และข้อมูลที่คงอยู่เพื่อให้มั่นใจในความสอดคล้องในปฏิสัมพันธ์หลายรอบ

ต่อไป มาดูการเรียกฟังก์ชัน/เครื่องมือในรายละเอียดเพิ่มเติม

### การเรียกฟังก์ชัน/เครื่องมือ

การเรียกฟังก์ชันเป็นวิธีหลักที่เราเปิดโอกาสให้ Large Language Models (LLMs) โต้ตอบกับเครื่องมือ คุณมักจะเห็นคำว่า 'ฟังก์ชัน' และ 'เครื่องมือ' ใช้แทนกันได้ เพราะ 'ฟังก์ชัน' (บล็อกของโค้ดที่นำกลับมาใช้ใหม่ได้) คือ 'เครื่องมือ' ที่ Agents ใช้ในการทำงานต่างๆ เพื่อให้โค้ดของฟังก์ชันถูกเรียกใช้ LLM ต้องเปรียบเทียบคำขอของผู้ใช้กับคำอธิบายของฟังก์ชัน ในการทำเช่นนี้ Schema ที่มีคำอธิบายของฟังก์ชันทั้งหมดที่มีอยู่จะถูกส่งไปยัง LLM จากนั้น LLM จะเลือกฟังก์ชันที่เหมาะสมที่สุดสำหรับงานและส่งคืนชื่อและอาร์กิวเมนต์ ฟังก์ชันที่เลือกจะถูกเรียกใช้ และผลลัพธ์จะถูกส่งกลับไปยัง LLM ซึ่งใช้ข้อมูลนั้นเพื่อตอบสนองคำขอของผู้ใช้

สำหรับนักพัฒนาในการนำการเรียกฟังก์ชันไปใช้สำหรับ Agents คุณจะต้องมี:

1. โมเดล LLM ที่รองรับการเรียกฟังก์ชัน
2. Schema ที่มีคำอธิบายฟังก์ชัน
3. โค้ดสำหรับแต่ละฟังก์ชันที่อธิบายไว้

ลองใช้ตัวอย่างการดึงเวลาปัจจุบันในเมืองหนึ่งเพื่ออธิบาย:

1. **เริ่มต้น LLM ที่รองรับการเรียกฟังก์ชัน:**

    ไม่ใช่ทุกโมเดลที่รองรับการเรียกฟังก์ชัน ดังนั้นจึงสำคัญที่จะต้องตรวจสอบว่า LLM ที่คุณใช้นั้นรองรับหรือไม่ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> รองรับการเรียกฟังก์ชัน เราสามารถเริ่มต้นด้วยการสร้างไคลเอนต์ Azure OpenAI

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **สร้าง Schema ของฟังก์ชัน:**

    ต่อไปเราจะกำหนด Schema JSON ที่มีชื่อฟังก์ชัน คำอธิบายของสิ่งที่ฟังก์ชันทำ และชื่อและคำอธิบายของพารามิเตอร์ฟังก์ชัน จากนั้นเราจะนำ Schema นี้ไปส่งให้กับไคลเอนต์ที่สร้างไว้ก่อนหน้านี้ พร้อมกับคำขอของผู้ใช้เพื่อค้นหาเวลาในซานฟรานซิสโก สิ่งที่สำคัญที่ต้องสังเกตคือ **การเรียกเครื่องมือ** คือสิ่งที่ถูกส่งคืน **ไม่ใช่** คำตอบสุดท้ายของคำถาม ดังที่กล่าวไว้ก่อนหน้านี้ LLM จะส่งคืนชื่อของฟังก์ชันที่เลือกสำหรับงาน และอาร์กิวเมนต์ที่จะส่งไปยังฟังก์ชันนั้น

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **โค้ดของฟังก์ชันที่จำเป็นในการทำงาน:**

    ตอนนี้ LLM ได้เลือกฟังก์ชันที่ต้องการรันแล้ว โค้ดที่ทำงานนั้นจำเป็นต้องถูกนำไปใช้และรัน เราสามารถนำโค้ดไปใช้เพื่อดึงเวลาปัจจุบันใน Python นอกจากนี้เรายังต้องเขียนโค้ดเพื่อดึงชื่อและอาร์กิวเมนต์จาก response_message เพื่อให้ได้ผลลัพธ์สุดท้าย

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

การเรียกฟังก์ชันเป็นหัวใจสำคัญของการออกแบบการใช้เครื่องมือของ Agent ส่วนใหญ่ หากไม่ใช่ทั้งหมด อย่างไรก็ตาม การนำไปใช้ตั้งแต่เริ่มต้นอาจเป็นเรื่องท้าทาย
ดังที่เราได้เรียนรู้ใน [บทเรียนที่ 2](../../../02-explore-agentic-frameworks) กรอบการทำงานของ Agentic มอบส่วนประกอบที่สร้างไว้ล่วงหน้าเพื่อช่วยในการนำการใช้เครื่องมือไปใช้

## ตัวอย่างการใช้เครื่องมือกับกรอบการทำงานของ Agentic

นี่คือตัวอย่างบางส่วนของวิธีที่คุณสามารถนำรูปแบบการออกแบบการใช้เครื่องมือไปใช้โดยใช้กรอบการทำงานของ Agentic ต่างๆ:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> เป็นกรอบการทำงาน AI แบบโอเพ่นซอร์สสำหรับนักพัฒนา .NET, Python และ Java ที่ทำงานกับ Large Language Models (LLMs) มันช่วยให้การใช้การเรียกฟังก์ชันง่ายขึ้นโดยอธิบายฟังก์ชันและพารามิเตอร์ของคุณไปยังโมเดลโดยอัตโนมัติผ่านกระบวนการที่เรียกว่า <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">การทำให้เป็นอนุกรม</a> นอกจากนี้ยังจัดการการสื่อสารระหว่างโมเดลและโค้ดของคุณ ข้อดีอีกประการของการใช้กรอบการทำงานของ Agentic เช่น Semantic Kernel คือช่วยให้คุณเข้าถึงเครื่องมือที่สร้างไว้ล่วงหน้า เช่น <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> และ <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>

แผนภาพต่อไปนี้แสดงกระบวนการเรียกฟังก์ชันด้วย Semantic Kernel:

![การเรียกฟังก์ชัน](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.th.png)

ใน Semantic Kernel ฟังก์ชัน/เครื่องมือถูกเรียกว่า <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a> เราสามารถแปลงฟังก์ชัน `get_current_time` ที่เราเห็นก่อนหน้านี้ให้เป็น Plugin ได้โดยการเปลี่ยนให้เป็นคลาสที่มีฟังก์ชันอยู่ในนั้น นอกจากนี้เรายังสามารถนำเข้า `kernel_function` decorator ซึ่งรับคำอธิบายของฟังก์ชัน เมื่อคุณสร้าง Kernel ด้วย GetCurrentTimePlugin Kernel จะทำให้ฟังก์ชันและพารามิเตอร์ของมันเป็นอนุกรมโดยอัตโนมัติ สร้าง Schema เพื่อส่งไปยัง LLM ในกระบวนการนี้

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> เป็นกรอบการทำงานของ Agentic ใหม่ที่ออกแบบมาเพื่อช่วยให้นักพัฒนาสร้าง ปรับใช้ และขยาย AI Agents ที่มีคุณภาพสูงและขยายได้อย่างปลอดภัย โดยไม่จำเป็นต้องจัดการทรัพยากรคอมพิวเตอร์และการจัดเก็บข้อมูลพื้นฐาน มันมีประโยชน์โดยเฉพาะสำหรับแอปพลิเคชันในองค์กร เนื่องจากเป็นบริการที่มีการจัดการเต็มรูปแบบพร้อมความปลอดภัยระดับองค์กร

เมื่อเปรียบเทียบกับการพัฒนาด้วย LLM API โดยตรง Azure AI Agent Service มีข้อได้เปรียบบางประการ รวมถึง:

- การเรียกเครื่องมืออัตโนมัติ – ไม่จำเป็นต้องแยกวิเคราะห์การเรียกเครื่องมือ เรียกใช้เครื่องมือ และจัดการการตอบสนอง ทั้งหมดนี้ทำบนเซิร์ฟเวอร์
- การจัดการข้อมูลอย่างปลอดภัย – แทนที่จะจัดการสถานะการสนทนาด้วยตัวเอง คุณสามารถพึ่งพา threads เพื่อจัดเก็บข้อมูลทั้งหมดที่คุณต้องการ
- เครื่องมือที่มีอยู่ในตัว – เครื่องมือที่คุณสามารถใช้เพื่อโต้ตอบกับแหล่งข้อมูลของคุณ เช่น Bing, Azure AI Search และ Azure Functions

เครื่องมือที่มีอยู่ใน Azure AI Agent Service สามารถแบ่งออกเป็นสองประเภท:

1. เครื่องมือความรู้:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">การเชื่อมโยงกับ Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. เครื่องมือการกระทำ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">การเรียกฟังก์ชัน</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">เครื่องมือที่กำหนดโดย OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service ช่วยให้เราสามารถใช้เครื่องมือเหล่านี้ร่วมกันเป็น `toolset` นอกจากนี้ยังใช้ `threads` ซึ่งติดตามประวัติของข้อความจากการสนทนาเฉพาะ

ลองจินตนาการว่าคุณเป็นตัวแทนฝ่ายขายในบริษัทชื่อ Contoso คุณต้องการพัฒนา Agent การสนทนาที่สามารถตอบคำถามเกี่ยวกับข้อมูลการขายของคุณ

ภาพต่อไปนี้แสดงให้เห็นว่าคุณสามารถใช้ Azure AI Agent Service เพื่อวิเคราะห์ข้อมูลการขายของคุณได้อย่างไร:

![Agentic Service In Action](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.th.jpg)

ในการใช้เครื่องมือเหล่านี้กับบริการ เราสามารถสร้างไคลเอนต์และกำหนดเครื่องมือหรือชุดเครื่องมือได้ ในการนำไปใช้จริง เราสามารถใช้โค้ด Python ต่อไปนี้ LLM จะสามารถดูชุดเครื่องมือและตัดสินใจว่าจะใช้ฟังก์ชันที่ผู้ใช้สร้างขึ้น `fetch_sales_data_using_sqlite_query` หรือ Code Interpreter ที่สร้างไว้ล่วงหน้าขึ้นอยู่กับคำขอของผู้ใช้

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ข้อควรพิจารณาพิเศษสำหรับการใช้รูปแบบการออกแบบการใช้เครื่องมือเพื่อสร้าง AI Agents ที่น่าเชื่อถือมีอะไรบ้าง?

ข้อกังวลทั่วไปเกี่ยวกับ SQL ที่สร้างแบบไดนามิกโดย LLMs คือความปลอดภัย โดยเฉพาะความเสี่ยงของการโจมตี SQL Injection หรือการกระทำที่เป็นอันตราย เช่น การลบหรือแก้ไขฐานข้อมูล แม้ว่าข้อกังวลเหล่านี้จะมีความสำคัญ แต่สามารถลดความเสี่ยงได้อย่างมีประสิทธิภาพโดยการกำหนดค่าการอนุญาตการเข้าถึงฐานข้อมูลอย่างเหมาะสม สำหรับฐานข้อมูลส่วนใหญ่ การกำหนดค่าฐานข้อมูลให้อ่านได้อย่างเดียว
การรันแอปในสภาพแวดล้อมที่ปลอดภัยช่วยเพิ่มการป้องกันได้มากขึ้น ในสถานการณ์ขององค์กร ข้อมูลมักจะถูกดึงและแปลงจากระบบปฏิบัติการไปยังฐานข้อมูลแบบอ่านอย่างเดียวหรือคลังข้อมูลที่มีโครงสร้างที่ใช้งานง่าย วิธีนี้ช่วยให้มั่นใจได้ว่าข้อมูลมีความปลอดภัย ถูกปรับแต่งเพื่อประสิทธิภาพและการเข้าถึง และแอปมีการเข้าถึงแบบจำกัดเฉพาะการอ่านเท่านั้น

## ตัวอย่างโค้ด

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## มีคำถามเพิ่มเติมเกี่ยวกับการใช้ Tool Design Patterns?

เข้าร่วม [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) เพื่อพบปะกับผู้เรียนคนอื่นๆ เข้าร่วมช่วง Office Hours และรับคำตอบสำหรับคำถามเกี่ยวกับ AI Agents ของคุณ

## แหล่งข้อมูลเพิ่มเติม

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## บทเรียนก่อนหน้า

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## บทเรียนถัดไป

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์ที่เป็นมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->