[![วิธีออกแบบเอเจนต์ AI ที่ดี](../../../translated_images/th/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(คลิกที่รูปภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

# รูปแบบการออกแบบการใช้เครื่องมือ

เครื่องมือน่าสนใจเพราะช่วยให้เอเจนต์ AI มีขอบเขตความสามารถที่กว้างขึ้น แทนที่เอเจนต์จะมีชุดการกระทำจำกัดที่สามารถทำได้ การเพิ่มเครื่องมือเข้าไป เอเจนต์จึงสามารถทำการกระทำได้หลากหลายมากขึ้น ในบทนี้ เราจะมาดูรูปแบบการออกแบบการใช้เครื่องมือ ซึ่งอธิบายว่าเอเจนต์ AI สามารถใช้เครื่องมือเฉพาะเพื่อบรรลุเป้าหมายอย่างไร

## บทนำ

ในบทเรียนนี้ เราต้องการหาคำตอบสำหรับคำถามดังต่อไปนี้:

- รูปแบบการออกแบบการใช้เครื่องมือคืออะไร?
- กรณีการใช้งานใดบ้างที่สามารถนำไปใช้ได้?
- ส่วนประกอบ/บล็อกการสร้างใดบ้างที่จำเป็นสำหรับการใช้รูปแบบการออกแบบนี้?
- การพิจารณาพิเศษใดที่ควรมีเมื่อนำรูปแบบการออกแบบการใช้เครื่องมือนี้ไปใช้สร้างเอเจนต์ AI ที่น่าเชื่อถือ?

## เป้าหมายการเรียนรู้

หลังจากเรียนบทนี้เสร็จ คุณจะสามารถ:

- นิยามรูปแบบการออกแบบการใช้เครื่องมือและจุดประสงค์ได้
- ระบุกรณีการใช้งานที่สามารถใช้รูปแบบการออกแบบนี้ได้
- เข้าใจส่วนประกอบสำคัญในการใช้รูปแบบการออกแบบนี้
- รับรู้ถึงข้อควรพิจารณาในการสร้างเอเจนต์ AI ที่น่าเชื่อถือโดยใช้รูปแบบการออกแบบนี้

## รูปแบบการออกแบบการใช้เครื่องมือคืออะไร?

**รูปแบบการออกแบบการใช้เครื่องมือ** มุ่งเน้นที่การให้ LLM มีความสามารถในการโต้ตอบกับเครื่องมือภายนอกเพื่อบรรลุเป้าหมายเฉพาะ เครื่องมือคือโค้ดที่เอเจนต์สามารถเรียกใช้เพื่อทำการกระทำต่าง ๆ เครื่องมืออาจเป็นฟังก์ชันง่าย ๆ เช่น เครื่องคิดเลข หรือการเรียก API ไปยังบริการภายนอกอย่างการดูราคาหุ้นหรือพยากรณ์อากาศ ในบริบทของเอเจนต์ AI เครื่องมือถูกออกแบบมาให้เอเจนต์เรียกใช้เมื่อได้รับคำสั่งฟังก์ชันที่สร้างโดยโมเดล

## กรณีการใช้งานใดบ้างที่สามารถนำไปใช้ได้?

เอเจนต์ AI สามารถใช้เครื่องมือเพื่อทำงานที่ซับซ้อน ดึงข้อมูล หรือทำการตัดสินใจ รูปแบบการออกแบบการใช้เครื่องมือมักถูกใช้ในสถานการณ์ที่ต้องมีการโต้ตอบแบบไดนามิกกับระบบภายนอก เช่น ฐานข้อมูล บริการเว็บ หรือเครื่องมือแปลความหมายโค้ด ความสามารถนี้เหมาะสำหรับกรณีการใช้งานต่าง ๆ ได้แก่:

- **การดึงข้อมูลไดนามิก:** เอเจนต์สามารถสอบถาม API ภายนอกหรือฐานข้อมูลเพื่อดึงข้อมูลปัจจุบัน (เช่น การสอบถามฐานข้อมูล SQLite เพื่อวิเคราะห์ข้อมูล ดึงราคาหุ้น หรือข้อมูลสภาพอากาศ)
- **การรันโค้ดและการแปลความหมาย:** เอเจนต์สามารถรันโค้ดหรือสคริปต์เพื่อแก้ปัญหาคณิตศาสตร์ สร้างรายงาน หรือจำลองเหตุการณ์
- **การอัตโนมัติใน workflow:** อัตโนมัติกระบวนการทำงานซ้ำซ้อนหรือหลายขั้นตอนโดยรวมเครื่องมือเช่น โปรแกรมจัดตารางงาน บริการอีเมล หรือ pipeline ข้อมูล
- **บริการลูกค้า:** เอเจนต์สามารถโต้ตอบกับระบบ CRM แพลตฟอร์มตั๋ว หรือฐานความรู้เพื่อแก้ไขคำถามของผู้ใช้
- **การสร้างและแก้ไขเนื้อหา:** เอเจนต์สามารถใช้เครื่องมือตรวจไวยากรณ์ สรุปข้อความ หรือประเมินความปลอดภัยเนื้อหาเพื่อช่วยงานสร้างเนื้อหา

## ส่วนประกอบ/บล็อกการสร้างที่จำเป็นในการใช้รูปแบบการออกแบบการใช้เครื่องมือคืออะไร?

บล็อกการสร้างเหล่านี้ช่วยให้เอเจนต์ AI สามารถทำงานได้หลายประเภท มาดูส่วนประกอบหลักสำหรับใช้รูปแบบการออกแบบการใช้เครื่องมือกัน:

- **ฟังก์ชัน/Schema ของเครื่องมือ:** คำนิยามรายละเอียดของเครื่องมือที่มีอยู่ รวมถึงชื่อฟังก์ชัน จุดประสงค์ พารามิเตอร์ที่ต้องการ และผลลัพธ์ที่คาดหวัง schema เหล่านี้ช่วยให้ LLM เข้าใจว่าเครื่องมือใดมีให้ใช้และวิธีสร้างคำขอที่ถูกต้อง

- **ตรรกะการเรียกใช้ฟังก์ชัน:** ควบคุมว่าจะเรียกใช้เครื่องมือเมื่อใดและอย่างไรตามเจตนาผู้ใช้และบริบทการสนทนา อาจรวมถึงโมดูลวางแผน กลไกจัดเส้นทาง หรือกระบวนการเงื่อนไขที่กำหนดการใช้เครื่องมือแบบไดนามิก

- **ระบบจัดการข้อความ:** ส่วนประกอบที่จัดการการไหลของบทสนทนาระหว่างข้อความผู้ใช้ คำตอบ LLM การเรียกเครื่องมือ และผลลัพธ์ของเครื่องมือ

- **โครงสร้างการรวมเครื่องมือ:** โครงสร้างพื้นฐานที่เชื่อมต่อเอเจนต์กับเครื่องมือต่าง ๆ ไม่ว่าจะเป็นฟังก์ชันง่ายหรืองานบริการภายนอกที่ซับซ้อน

- **การจัดการข้อผิดพลาดและการตรวจสอบ:** กลไกจัดการความล้มเหลวในการรันเครื่องมือ ตรวจสอบพารามิเตอร์ และจัดการการตอบกลับที่ไม่คาดคิด

- **การจัดการสถานะ:** ติดตามบริบทการสนทนา ปฏิสัมพันธ์กับเครื่องมือก่อนหน้า และข้อมูลถาวรเพื่อให้มั่นใจในความสอดคล้องของการสนทนาหลายรอบ

ต่อไป เราจะดูรายละเอียดเกี่ยวกับการเรียกใช้ฟังก์ชัน/เครื่องมือ

### การเรียกใช้ฟังก์ชัน/เครื่องมือ

การเรียกใช้ฟังก์ชันเป็นวิธีหลักที่ช่วยให้ Large Language Models (LLMs) โต้ตอบกับเครื่องมือได้ คุณจะเห็นคำว่า 'Function' และ 'Tool' ใช้แทนกันได้ เพราะ 'functions' (บล็อกโค้ดที่ใช้ซ้ำได้) คือ 'tools' ที่เอเจนต์ใช้ทำงาน เพื่อให้โค้ดฟังก์ชันถูกเรียกใช้ LLM ต้องเปรียบเทียบคำขอของผู้ใช้กับคำอธิบายของฟังก์ชัน เพื่อทำเช่นนี้ จะมี schema ที่มีคำอธิบายของฟังก์ชันทั้งหมดส่งไปยัง LLM ซึ่ง LLM จะเลือกฟังก์ชันที่เหมาะสมที่สุดกับงานและส่งชื่อกับอาร์กิวเมนต์กลับมา ฟังก์ชันที่ถูกเลือกจะถูกเรียกใช้ ผลลัพธ์ถูกส่งกลับไปยัง LLM ซึ่งใช้ข้อมูลนั้นเพื่อตอบคำขอของผู้ใช้

สำหรับนักพัฒนาที่ต้องการใช้งานการเรียกฟังก์ชันสำหรับเอเจนต์ คุณจะต้องมี:

1. โมเดล LLM ที่รองรับการเรียกใช้ฟังก์ชัน
2. Schema ที่มีคำอธิบายฟังก์ชัน
3. โค้ดสำหรับแต่ละฟังก์ชันที่อธิบายไว้

สมมุติว่าเราจะดูตัวอย่างการขอเวลาปัจจุบันในเมืองหนึ่ง:

1. **เริ่มต้น LLM ที่รองรับการเรียกใช้ฟังก์ชัน:**

    โมเดลไม่ใช่ทุกรุ่นที่รองรับการเรียกฟังก์ชัน จึงควรตรวจสอบว่าโมเดลที่ใช้รองรับ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> รองรับการเรียกใช้ฟังก์ชัน เราสามารถเริ่มจากการสร้างไคลเอนต์ Azure OpenAI 

    ```python
    # เริ่มต้นไคลเอนต์ Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **สร้าง Schema ฟังก์ชัน:**

    ต่อไปเราจะกำหนด JSON schema ที่มีชื่อฟังก์ชัน คำอธิบายว่าฟังก์ชันทำอะไร และชื่อกับคำอธิบายของพารามิเตอร์ฟังก์ชัน
    แล้วนำ schema นี้ส่งให้กับไคลเอนต์ที่สร้างไว้ก่อนหน้า พร้อมคำขอจากผู้ใช้เพื่อหาช่วงเวลาในซานฟรานซิสโก สิ่งสำคัญที่ต้องสังเกตคือ **การเรียกใช้งานเครื่องมือ** คือสิ่งที่ได้คืนมา **ไม่ใช่** คำตอบสุดท้ายของคำถาม อย่างที่กล่าวไว้ก่อนหน้านี้ LLM คืนชื่อฟังก์ชันที่เลือกและอาร์กิวเมนต์ที่จะส่งให้

    ```python
    # คำอธิบายฟังก์ชันสำหรับให้แบบจำลองอ่าน
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
  
    # ข้อความผู้ใช้เบื้องต้น
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # การเรียก API ครั้งแรก: ขอให้โมเดลใช้ฟังก์ชัน
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # ประมวลผลคำตอบของโมเดล
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **โค้ดฟังก์ชันที่ต้องการทำงาน:**

    เมื่อ LLM เลือกฟังก์ชันที่จะรัน โค้ดที่ทำงานนั้นต้องถูกเขียนและเรียกใช้
    เราสามารถเขียนโค้ดเพื่อดึงเวลาปัจจุบันในภาษา Python และต้องเขียนโค้ดดึงชื่อกับอาร์กิวเมนต์จาก response_message เพื่อให้ได้ผลลัพธ์สุดท้าย

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
  
      # การเรียกใช้ API ครั้งที่สอง: รับคำตอบสุดท้ายจากโมเดล
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

การเรียกฟังก์ชันเป็นหัวใจหลักของรูปแบบการใช้เครื่องมือสำหรับเอเจนต์ส่วนใหญ่ แม้ว่าการเขียนระบบนี้เองตั้งแต่ต้นมักจะท้าทาย
อย่างที่เราได้เรียนรู้ใน [Lesson 2](../../../02-explore-agentic-frameworks) เฟรมเวิร์กเอเจนต์ิกช่วยให้เรามีบล็อกการสร้างพร้อมใช้เพื่อนำรูปแบบการใช้เครื่องมือไปใช้งานจริง
 
## ตัวอย่างการใช้เครื่องมือกับ Agentic Frameworks

นี่คือตัวอย่างการใช้งานรูปแบบการออกแบบการใช้เครื่องมือด้วย Agentic Frameworks ที่แตกต่างกัน:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> คือเฟรมเวิร์ก AI โอเพนซอร์สสำหรับนักพัฒนา .NET, Python, และ Java ที่ทำงานกับ Large Language Models (LLMs) ช่วยให้ง่ายขึ้นในการใช้ฟังก์ชันเรียกใช้งานโดยการอธิบายฟังก์ชันและพารามิเตอร์ให้โมเดลผ่านกระบวนการที่เรียกว่า <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializing</a> นอกจากนี้ยังจัดการการสื่อสารระหว่างโมเดลกับโค้ดของคุณ อีกข้อดีของการใช้เฟรมเวิร์กเอเจนต์ิกเช่น Semantic Kernel คือช่วยให้เข้าถึงเครื่องมือพร้อมใช้เช่น <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> และ <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>

แผนภาพต่อไปนี้แสดงขั้นตอนการเรียกใช้ฟังก์ชันด้วย Semantic Kernel:

![function calling](../../../translated_images/th/functioncalling-diagram.a84006fc287f6014.webp)

ใน Semantic Kernel ฟังก์ชัน/เครื่องมือเรียกว่า <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a> เราสามารถแปลงฟังก์ชัน `get_current_time` ที่เห็นก่อนหน้าให้เป็นปลั๊กอินโดยเปลี่ยนเป็นคลาสที่มีฟังก์ชันในนั้นได้ นอกจากนี้เรายังสามารถนำเข้า decorator ชื่อ `kernel_function` ซึ่งรับคำอธิบายฟังก์ชัน เมื่อสร้าง kernel กับ GetCurrentTimePlugin kernel จะทำการ serialize ฟังก์ชันและพารามิเตอร์โดยอัตโนมัติ สร้าง schema เพื่อส่งให้ LLM

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

# สร้างเคอร์เนล
kernel = Kernel()

# สร้างปลั๊กอิน
get_current_time_plugin = GetCurrentTimePlugin(location)

# เพิ่มปลั๊กอินเข้าสู่เคอร์เนล
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> คือเฟรมเวิร์กเอเจนต์ิกรุ่นใหม่ที่ออกแบบมาเพื่อให้นักพัฒนาสามารถสร้าง ปรับใช้ และขยายเอเจนต์ AI คุณภาพสูงที่ขยายได้อย่างปลอดภัยโดยไม่ต้องจัดการทรัพยากรคอมพิวเตอร์และจัดเก็บข้อมูลเบื้องหลัง เหมาะอย่างยิ่งสำหรับแอปพลิเคชันองค์กรเพราะเป็นบริการที่บริหารจัดการเต็มรูปแบบพร้อมความปลอดภัยระดับองค์กร

เมื่อเทียบกับการพัฒนาด้วย API LLM โดยตรง Azure AI Agent Service มีข้อดีหลายประการรวมถึง:

- การเรียกใช้เครื่องมือโดยอัตโนมัติ – ไม่ต้องแยกวิเคราะห์การเรียกเครื่องมือเอง เรียกใช้เครื่องมือ และจัดการการตอบกลับ ทุกอย่างถูกทำบนเซิร์ฟเวอร์
- การจัดการข้อมูลอย่างปลอดภัย – แทนที่จะต้องจัดการสถานะการสนทนาเอง สามารถใช้ `threads` เพื่อเก็บข้อมูลทั้งหมดที่ต้องการได้
- เครื่องมือพร้อมใช้ – เครื่องมือที่ใช้โต้ตอบกับแหล่งข้อมูล เช่น Bing, Azure AI Search และ Azure Functions

เครื่องมือใน Azure AI Agent Service แบ่งเป็นสองประเภท:

1. เครื่องมือความรู้:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">การผูกโยงกับ Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ค้นหาไฟล์</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. เครื่องมือดำเนินการ:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">การเรียกใช้ฟังก์ชัน</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">เครื่องมือที่กำหนดด้วย OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service ช่วยให้เราใช้เครื่องมือเหล่านี้ร่วมกันเป็น `toolset` และใช้ `threads` เพื่อเก็บประวัติข้อความจากการสนทนาหนึ่ง ๆ

สมมติว่าคุณเป็นเอเจนต์ฝ่ายขายที่บริษัท Contoso คุณต้องการพัฒนาเอเจนต์สนทนาที่สามารถตอบคำถามเกี่ยวกับข้อมูลการขายของคุณได้

ภาพต่อไปนี้แสดงวิธีที่คุณจะใช้ Azure AI Agent Service วิเคราะห์ข้อมูลการขาย:

![Agentic Service In Action](../../../translated_images/th/agent-service-in-action.34fb465c9a84659e.webp)

เพื่อใช้เครื่องมือเหล่านี้กับบริการ เราสามารถสร้างไคลเอนต์และกำหนดเครื่องมือหรือชุดเครื่องมือ ในทางปฏิบัติ เราสามารถใช้โค้ด Python ดังต่อไปนี้ LLM จะดูชุดเครื่องมือแล้วตัดสินใจว่าจะใช้ฟังก์ชันที่ผู้ใช้สร้างเอง `fetch_sales_data_using_sqlite_query` หรือ Code Interpreter ที่มีมาให้ขึ้นอยู่กับคำขอของผู้ใช้

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # ฟังก์ชัน fetch_sales_data_using_sqlite_query ที่สามารถพบได้ในไฟล์ fetch_sales_data_functions.py
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# เริ่มต้นชุดเครื่องมือ
toolset = ToolSet()

# เริ่มต้นตัวแทนเรียกฟังก์ชันด้วยฟังก์ชัน fetch_sales_data_using_sqlite_query และเพิ่มลงในชุดเครื่องมือ
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# เริ่มต้นเครื่องมือ Code Interpreter และเพิ่มลงในชุดเครื่องมือ
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ข้อควรพิจารณาพิเศษในการใช้รูปแบบการออกแบบการใช้เครื่องมือเพื่อสร้างเอเจนต์ AI ที่น่าเชื่อถือคืออะไร?

ข้อกังวลทั่วไปเกี่ยวกับ SQL ที่สร้างแบบไดนามิกโดย LLM คือเรื่องความปลอดภัย โดยเฉพาะความเสี่ยงจาก SQL injection หรือการกระทำที่ประสงค์ร้าย เช่น การลบหรือดัดแปลงฐานข้อมูล แม้ข้อกังวลเหล่านี้จะมีเหตุผล แต่สามารถลดความเสี่ยงได้อย่างมีประสิทธิภาพโดยการกำหนดสิทธิ์การเข้าถึงฐานข้อมูลอย่างถูกต้อง สำหรับฐานข้อมูลส่วนใหญ่จะเป็นการตั้งค่าฐานข้อมูลให้เป็นโหมดอ่านอย่างเดียว สำหรับบริการฐานข้อมูลอย่าง PostgreSQL หรือ Azure SQL ควรกำหนดบทบาทแอปให้เป็นแบบอ่านอย่างเดียว (SELECT) เท่านั้น
การรันแอปในสภาพแวดล้อมที่ปลอดภัยช่วยเสริมความคุ้มครองได้มากขึ้น ในสถานการณ์องค์กร ข้อมูลมักจะถูกดึงและแปลงจากระบบปฏิบัติการไปยังฐานข้อมูลหรือคลังข้อมูลที่เป็นแบบอ่านอย่างเดียวพร้อมสคีมาที่ใช้งานง่าย วิธีนี้ช่วยให้ข้อมูลปลอดภัย ถูกปรับเพื่อประสิทธิภาพและการเข้าถึง และแอปจะมีสิทธิ์เข้าถึงแบบอ่านอย่างเดียวที่จำกัด

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Got More Questions about the Tool Use Design Patterns?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">เวิร์กช็อปบริการ Azure AI Agents</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">เวิร์กช็อป Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">คู่มือการเรียกใช้งานฟังก์ชัน Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">โปรแกรมแปลความหมายโค้ด Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความแม่นยำ โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมถือเป็นแหล่งข้อมูลที่มีความน่าเชื่อถือสูงสุด สำหรับข้อมูลที่มีความสำคัญ ควรใช้บริการแปลโดยผู้เชี่ยวชาญด้านภาษาที่เป็นมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใดๆ ที่เกิดจากการใช้การแปลฉบับนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->