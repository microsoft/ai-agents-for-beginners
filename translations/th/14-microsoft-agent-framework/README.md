# การสำรวจ Microsoft Agent Framework

![Agent Framework](../../../translated_images/th/lesson-14-thumbnail.90df0065b9d234ee.webp)

### บทนำ

บทเรียนนี้จะครอบคลุม:

- ความเข้าใจ Microsoft Agent Framework: ฟีเจอร์หลักและคุณค่า  
- การสำรวจแนวคิดหลักของ Microsoft Agent Framework
- รูปแบบขั้นสูงของ MAF: โฟลว์งาน, มิดเดิลแวร์, และหน่วยความจำ

## เป้าหมายการเรียนรู้

หลังจากจบบทเรียนนี้ คุณจะสามารถ:

- สร้างเอเจนต์ AI พร้อมใช้งานจริงโดยใช้ Microsoft Agent Framework
- นำฟีเจอร์หลักของ Microsoft Agent Framework ไปประยุกต์ใช้กับกรณีใช้งานที่ต้องการเอเจนต์
- ใช้รูปแบบขั้นสูงรวมถึงโฟลว์งาน, มิดเดิลแวร์ และการสังเกตการณ์

## ตัวอย่างโค้ด 

ตัวอย่างโค้ดสำหรับ [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) สามารถพบได้ในรีโพซิทอรีนี้ภายใต้ไฟล์ `xx-python-agent-framework` และ `xx-dotnet-agent-framework`

## ความเข้าใจ Microsoft Agent Framework

![Framework Intro](../../../translated_images/th/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) เป็นเฟรมเวิร์กแบบรวมของ Microsoft สำหรับการสร้างเอเจนต์ AI ให้ความยืดหยุ่นในการจัดการกรณีใช้งานเอเจนต์ที่หลากหลายในสภาพแวดล้อมการผลิตและการวิจัย เช่น:

- **การจัดลำดับเอเจนต์ตามลำดับ** ในสถานการณ์ที่ต้องมีโฟลว์งานทีละขั้นตอน
- **การจัดลำดับพร้อมกัน** ในสถานการณ์ที่เอเจนต์ต้องทำงานหลายงานพร้อมกัน
- **การจัดลำดับแชทกลุ่ม** ในสถานการณ์ที่เอเจนต์สามารถทำงานร่วมกันในงานเดียว
- **การส่งต่อการจัดลำดับ** ในสถานการณ์ที่เอเจนต์ส่งต่องานให้กันเมื่อเสร็จงานย่อย
- **การจัดลำดับแม่เหล็ก** ในสถานการณ์ที่เอเจนต์ผู้จัดการสร้างและแก้ไขรายการงานและประสานงานเอเจนต์ย่อยเพื่อทำงานให้เสร็จ

เพื่อส่งมอบเอเจนต์ AI ในสภาพแวดล้อมการผลิต MAF ยังมีฟีเจอร์เพิ่มเติมสำหรับ:

- **การสังเกตการณ์** ผ่านการใช้ OpenTelemetry ซึ่งทุกการกระทำของเอเจนต์ AI รวมถึงการเรียกเครื่องมือ, ขั้นตอนการจัดลำดับ, การไหลของเหตุผล และการติดตามประสิทธิภาพผ่านแดชบอร์ด Microsoft Foundry
- **ความปลอดภัย** โดยโฮสต์เอเจนต์โดยตรงบน Microsoft Foundry ซึ่งมีการควบคุมความปลอดภัย เช่น การเข้าถึงตามบทบาท, การจัดการข้อมูลส่วนตัว และความปลอดภัยของเนื้อหาที่มีในตัว
- **ความทนทาน** เนื่องจากเธรดและโฟลว์งานของเอเจนต์สามารถหยุดพัก, ดำเนินต่อ และกู้คืนจากข้อผิดพลาดได้ ทำให้สามารถประมวลผลงานที่ใช้เวลานานขึ้น
- **การควบคุม** โดยสนับสนุนโฟลว์งานที่มนุษย์มีส่วนร่วม โดยงานสามารถถูกตั้งค่าให้ต้องการการอนุมัติจากมนุษย์

Microsoft Agent Framework ยังมุ่งเน้นความสามารถในการทำงานข้ามระบบโดย:

- **ไม่ขึ้นกับคลาวด์** — เอเจนต์สามารถทำงานในคอนเทนเนอร์, บนเซิร์ฟเวอร์ส่วนตัว และบนคลาวด์ที่หลากหลาย
- **ไม่ขึ้นกับผู้ให้บริการ** — เอเจนต์สามารถสร้างผ่าน SDK ที่คุณชอบ รวมถึง Azure OpenAI และ OpenAI
- **การรวมมาตรฐานเปิด** — เอเจนต์สามารถใช้โปรโตคอล เช่น Agent-to-Agent (A2A) และ Model Context Protocol (MCP) เพื่อค้นหาและใช้งานเอเจนต์และเครื่องมืออื่น
- **ปลั๊กอินและตัวเชื่อมต่อ** — สามารถเชื่อมต่อกับบริการข้อมูลและหน่วยความจำ เช่น Microsoft Fabric, SharePoint, Pinecone และ Qdrant

มาดูว่าฟีเจอร์เหล่านี้ถูกนำไปใช้กับแนวคิดหลักของ Microsoft Agent Framework อย่างไร

## แนวคิดหลักของ Microsoft Agent Framework

### เอเจนต์

![Agent Framework](../../../translated_images/th/agent-components.410a06daf87b4fef.webp)

**การสร้างเอเจนต์**

การสร้างเอเจนต์ทำโดยการกำหนดบริการการนิยาม (ผู้ให้บริการ LLM),  
ชุดคำสั่งสำหรับเอเจนต์ AI ให้ปฏิบัติตาม และกำหนด `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

ด้านบนใช้ `Azure OpenAI` แต่เอเจนต์สามารถสร้างโดยใช้บริการหลากหลายรวมถึง `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

หรือ [MiniMax](https://platform.minimaxi.com/) ซึ่งให้ API ใกล้เคียงกับ OpenAI พร้อมหน้าต่างบริบทขนาดใหญ่ (สูงสุด 204K โทเคน):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

หรือเอเจนต์ระยะไกลโดยใช้โปรโตคอล A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**การรันเอเจนต์**

เอเจนต์ถูกเรียกใช้โดยเมธอด `.run` หรือ `.run_stream` สำหรับการตอบสนองแบบไม่สตรีมหรือสตรีมมิ่ง

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

การรันแต่ละครั้งของเอเจนต์ยังมีตัวเลือกในการปรับแต่งพารามิเตอร์ เช่น `max_tokens` ที่ใช้โดยเอเจนต์, `tools` ที่เอเจนต์สามารถเรียกใช้งาน และแม้แต่ `model` ที่ใช้สำหรับเอเจนต์

สิ่งนี้มีประโยชน์ในกรณีที่ต้องการโมเดลหรือเครื่องมือเฉพาะสำหรับทำงานตามคำขอผู้ใช้

**เครื่องมือ**

เครื่องมือสามารถกำหนดได้ทั้งตอนสร้างเอเจนต์:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# เมื่อสร้าง ChatAgent โดยตรง

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

และตอนรันเอเจนต์:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # เครื่องมือที่ให้ไว้สำหรับการรันนี้เท่านั้น )
```

**เธรดของเอเจนต์**

เธรดของเอเจนต์ใช้จัดการบทสนทนาหลายรอบ เธรดสามารถสร้างได้โดย:

- ใช้ `get_new_thread()` เพื่อให้เธรดถูกบันทึกไว้ตามเวลา
- สร้างเธรดโดยอัตโนมัติเมื่อตอนเรียกใช้งานเอเจนต์และเธรดนี้จะคงอยู่เฉพาะรอบปัจจุบัน

การสร้างเธรดตัวอย่างโค้ดเป็นแบบนี้:

```python
# สร้างเธรดใหม่
thread = agent.get_new_thread() # รันเอเย่นต์กับเธรดนั้น
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

คุณสามารถซีเรียลไลซ์เธรดเพื่อเก็บไว้ใช้ภายหลัง:

```python
# สร้างเธรดใหม่
thread = agent.get_new_thread() 

# รันเอเจนต์ด้วยเธรดนั้น

response = await agent.run("Hello, how are you?", thread=thread) 

# ทำการซีเรียลไลซ์เธรดเพื่อเก็บในที่จัดเก็บ

serialized_thread = await thread.serialize() 

# ทำการดีซีเรียลไลซ์สถานะเธรดหลังจากโหลดจากที่จัดเก็บ

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**มิดเดิลแวร์ของเอเจนต์**

เอเจนต์โต้ตอบกับเครื่องมือและ LLM เพื่อตอบสนองงานของผู้ใช้ ในบางสถานการณ์เราต้องการรันหรือบันทึกการโต้ตอบระหว่างนั้น มิดเดิลแวร์เอเจนต์ช่วยให้ทำเช่นนี้ได้ผ่าน:

*มิดเดิลแวร์ฟังก์ชัน*

มิดเดิลแวร์นี้ช่วยให้รันการกระทำระหว่างเอเจนต์และฟังก์ชัน/เครื่องมือที่เรียกใช้งาน ตัวอย่างคือการบันทึกล็อกเมื่อเรียกฟังก์ชัน

ในโค้ดด้านล่าง `next` กำหนดว่าจะเรียกมิดเดิลแวร์ถัดไปหรือฟังก์ชันจริง

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # การประมวลผลล่วงหน้า: บันทึกก่อนการเรียกใช้งานฟังก์ชัน
    print(f"[Function] Calling {context.function.name}")

    # ดำเนินการต่อไปยัง middleware ตัวถัดไปหรือการเรียกใช้งานฟังก์ชัน
    await next(context)

    # การประมวลผลหลัง: บันทึกหลังการเรียกใช้งานฟังก์ชัน
    print(f"[Function] {context.function.name} completed")
```

*มิดเดิลแวร์แชท*

มิดเดิลแวร์นี้ช่วยรันหรือบันทึกการกระทำระหว่างเอเจนต์และคำขอของ LLM

ซึ่งมีข้อมูลสำคัญ เช่น `messages` ที่ส่งไปยังบริการ AI

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # การประมวลผลล่วงหน้า: บันทึกก่อนเรียกใช้ AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # ดำเนินการต่อไปยังมิดเดิลแวร์หรืบริการ AI ถัดไป
    await next(context)

    # การประมวลผลภายหลัง: บันทึกหลังจากได้รับการตอบกลับจาก AI
    print("[Chat] AI response received")

```

**หน่วยความจำของเอเจนต์**

ตามที่กล่าวในบทเรียน `Agentic Memory`, หน่วยความจำเป็นองค์ประกอบสำคัญที่ช่วยให้เอเจนต์ทำงานได้ในบริบทต่าง ๆ MAF มีหน่วยความจำหลายแบบ:

*หน่วยความจำในแอป*

คือหน่วยความจำที่เก็บในเธรดระหว่างรันไทม์แอปพลิเคชัน

```python
# สร้างเธรดใหม่
thread = agent.get_new_thread() # รันเอเจนต์ด้วยเธรดนั้น
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*ข้อความถาวร*

หน่วยความจำนี้ใช้เก็บประวัติการสนทนาในหลายเซสชัน กำหนดโดย `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# สร้างที่เก็บข้อความที่กำหนดเอง
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*หน่วยความจำไดนามิก*

หน่วยความจำนี้เพิ่มเข้าในบริบทก่อนรันเอเจนต์ อาจเก็บไว้ในบริการภายนอก เช่น mem0:

```python
from agent_framework.mem0 import Mem0Provider

# ใช้ Mem0 สำหรับความสามารถของหน่วยความจำขั้นสูง
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**การสังเกตการณ์ของเอเจนต์**

การสังเกตการณ์มีความสำคัญในการสร้างระบบเอเจนต์ที่น่าเชื่อถือและดูแลรักษาง่าย MAF รวมกับ OpenTelemetry สำหรับการติดตามและวัดผลที่ดีกว่า

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # ทำบางอย่าง
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### โฟลว์งาน

MAF มีโฟลว์งานที่เป็นขั้นตอนกำหนดล่วงหน้าเพื่อทำงานให้เสร็จ รวมเอเจนต์ AI เป็นส่วนประกอบในขั้นตอนเหล่านั้น

โฟลว์งานประกอบด้วยส่วนต่าง ๆ ที่ช่วยควบคุมการทำงาน โฟลว์งานยังสนับสนุน **การจัดลำดับเอเจนต์หลายตัว** และ **การบันทึกสถานะ** เพื่อเก็บสถานะโฟลว์งาน

ส่วนประกอบหลักของโฟลว์งานคือ:

**ผู้ดำเนินการ**

ผู้ดำเนินการรับข้อความอินพุต, ทำงานที่มอบหมาย และสร้างข้อความเอาต์พุต ช่วยให้โฟลว์งานเดินหน้าสู่การทำงานใหญ่ให้เสร็จ ผู้ดำเนินการอาจเป็นเอเจนต์ AI หรือโลจิกที่กำหนดเอง

**เส้นทาง**

เส้นทางใช้กำหนดการไหลของข้อความในโฟลว์งาน โดยอาจเป็น:

*เส้นทางตรง* — การเชื่อมต่อง่าย ๆ แบบหนึ่งต่อหนึ่งระหว่างผู้ดำเนินการ:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*เส้นทางมีเงื่อนไข* — เปิดใช้งานเมื่อตรงตามเงื่อนไข เช่น เมื่อห้องพักโรงแรมไม่ว่าง ผู้ดำเนินการอาจแนะนำตัวเลือกอื่น

*เส้นทางแบบสวิตช์* — เส้นทางข้อความไปยังผู้ดำเนินการต่าง ๆ ตามเงื่อนไข เช่น ถ้าลูกค้าเดินทางมีสิทธิ์เข้าถึงพิเศษ งานจะถูกจัดการโดยโฟลว์งานอื่น

*เส้นทางแฟน-เอาท์* — ส่งข้อความเดียวไปยังหลายเป้าหมาย

*เส้นทางแฟน-อิน* — รวบรวมข้อความหลายข้อความจากผู้ดำเนินการหลายตัวและส่งไปยังเป้าหมายเดียว

**เหตุการณ์**

เพื่อให้สังเกตการณ์โฟลว์งานได้ดีขึ้น MAF มีเหตุการณ์ในตัวสำหรับสถานะการทำงาน เช่น:

- `WorkflowStartedEvent` — โฟลว์งานเริ่มทำงาน
- `WorkflowOutputEvent` — โฟลว์งานสร้างเอาต์พุต
- `WorkflowErrorEvent` — โฟลว์งานพบข้อผิดพลาด
- `ExecutorInvokeEvent` — ผู้ดำเนินการเริ่มทำงาน
- `ExecutorCompleteEvent` — ผู้ดำเนินการทำงานเสร็จสิ้น
- `RequestInfoEvent` — มีการส่งคำขอ

## รูปแบบขั้นสูงของ MAF

ส่วนข้างต้นครอบคลุมแนวคิดหลักของ Microsoft Agent Framework เมื่อคุณสร้างเอเจนต์ที่ซับซ้อนขึ้น ต่อไปนี้เป็นรูปแบบขั้นสูงที่ควรพิจารณา:

- **การประกอบมิดเดิลแวร์**: เชื่อมต่อมิดเดิลแวร์หลายตัว (เช่น การบันทึก, การยืนยันตัวตน, การจำกัดอัตรา) โดยใช้มิดเดิลแวร์ฟังก์ชันและแชทเพื่อควบคุมพฤติกรรมเอเจนต์อย่างละเอียด
- **การบันทึกสถานะโฟลว์งาน**: ใช้เหตุการณ์โฟลว์งานและการซีเรียลไลซ์เพื่อบันทึกและดำเนินงานเอเจนต์ที่ทำงานระยะยาว
- **การเลือกเครื่องมือแบบไดนามิก**: รวม RAG กับคำอธิบายเครื่องมือและการลงทะเบียนเครื่องมือของ MAF เพื่อแสดงเฉพาะเครื่องมือที่เกี่ยวข้องต่อคำขอ
- **การส่งต่อเอเจนต์หลายตัว**: ใช้เส้นทางโฟลว์งานและการกำหนดเงื่อนไขเส้นทางเพื่อจัดลำดับการส่งต่องานระหว่างเอเจนต์เฉพาะทาง

## การโฮสต์ LangChain / LangGraph Agent บน Microsoft Foundry

Microsoft Agent Framework เป็น **เฟรมเวิร์กที่ทำงานร่วมได้** — คุณไม่จำกัดเฉพาะเอเจนต์ที่เขียนด้วย MAF หากคุณมีเอเจนต์ที่สร้างด้วย **LangChain** หรือ **LangGraph** อยู่แล้ว สามารถรันเป็น **เอเจนต์โฮสต์ใน Microsoft Foundry** เพื่อให้ Foundry จัดการรันไทม์, เซสชัน, การปรับขนาด, ตัวตน และจุดปลายโปรโตคอล ในขณะที่ตรรกะเอเจนต์ยังคงอยู่ใน LangGraph

สิ่งนี้ทำได้โดยใช้แพ็กเกจ `langchain_azure_ai.agents.hosting` ซึ่งเปิดเผยกราฟ LangGraph ที่คอมไพล์ผ่านโปรโตคอลเดียวกับที่เอเจนต์โฮสต์ใน Foundry ใช้

**1. ติดตั้ง hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

ตัวเลือก `hosting` จะติดตั้งไลบรารีโปรโตคอล Foundry ได้แก่ `azure-ai-agentserver-responses` (จุดเชื่อมต่อ `/responses` ที่เข้ากันกับ OpenAI) และ `azure-ai-agentserver-invocations` (จุดเชื่อมต่อ `/invocations` แบบทั่วไป)

**2. เลือกโปรโตคอลโฮสต์:**

| โปรโตคอล | คลาสโฮสต์ | จุดปลาย | ใช้เมื่อ |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | ต้องการแชทที่เหมือน OpenAI, สตรีมมิ่ง, ประวัติการตอบ, และการจัดการบทสนทนา — แนะนำสำหรับเอเจนต์ที่สนทนา |
| **Invocations** | `InvocationsHostServer` | `/invocations` | ต้องการรูปร่าง JSON ที่กำหนดเอง, จุดเชื่อมต่อแบบ webhook, หรือการประมวลผลที่ไม่ใช่สนทนา |

เนื่องจาก **Responses API เป็น API หลักสำหรับการพัฒนาเอเจนต์สไตล์ใน Foundry** ให้เริ่มที่ `ResponsesHostServer` สำหรับเอเจนต์ส่วนใหญ่

**3. ตั้งค่าตัวแปรสภาพแวดล้อม** (`az login` ก่อนเพื่อให้ `DefaultAzureCredential` ยืนยันตัวตนได้):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

เมื่อเอเจนต์รันเป็นเอเจนต์โฮสต์ใน Foundry ระบบจะฉีดค่า `FOUNDRY_PROJECT_ENDPOINT` ให้อัตโนมัติ

**4. เปิดเผยเอเจนต์ LangGraph ผ่านโปรโตคอล Responses:**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI ที่นี่มุ่งเป้าไปที่ปลายทาง OpenAI-compatible (Responses) ของโครงการ Foundry.
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

รันในเครื่องด้วย `python main.py` แล้วส่งคำขอ Responses ไปที่ `http://localhost:8088/responses`

**พฤติกรรมหลัก:**

- **การสนทนา**: ลูกค้าสามารถดำเนินการต่อบทสนทนาด้วยการส่ง `previous_response_id` หรือ ID `conversation` หากกราฟคอมไพล์ด้วย LangGraph checkpointer, Foundry จะเชื่อมสถานะบทสนทนากับจุดตรวจสอบ (ใช้ durable checkpointer ในการผลิต; `MemorySaver` เหมาะกับการทดสอบในเครื่อง)
- **มนุษย์ในวงจร**: หากกราฟใช้ LangGraph `interrupt()`, `ResponsesHostServer` จะแสดงการหยุดชั่วคราวในฐานะ item `function_call` / `mcp_approval_request` ของ Responses และลูกค้าจะทำงานต่อด้วย `function_call_output` / `mcp_approval_response` ที่ตรงกัน
- **ปรับใช้ใน Foundry**: ใช้ Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ในเครื่อง, ต้องใช้ Docker), แล้ว `azd provision` และ `azd deploy` การปรับใช้เอเจนต์โฮสต์ต้องการบทบาท **Foundry Project Manager**

เวอร์ชันตัวอย่างที่รันได้ของตัวอย่างนี้อยู่ใน [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) สำหรับการสอนเต็มรูปแบบ (โปรโตคอล Invocations, สคีมา request ที่กำหนดเอง และการแก้ปัญหา) ดูที่ [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)

## ตัวอย่างโค้ด 

ตัวอย่างโค้ดสำหรับ Microsoft Agent Framework สามารถพบได้ในรีโพซิทอรีนี้ภายใต้ไฟล์ `xx-python-agent-framework` และ `xx-dotnet-agent-framework`

## มีคำถามเพิ่มเติมเกี่ยวกับ Microsoft Agent Framework หรือไม่?

เข้าร่วม [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) เพื่อพบกับผู้เรียนคนอื่น ๆ, เข้าชมชั่วโมงทำงานและรับคำตอบเกี่ยวกับเอเจนต์ AI ของคุณ
## บทเรียนก่อนหน้า

[Memory for AI Agents](../13-agent-memory/README.md)

## บทเรียนถัดไป

[Building Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->