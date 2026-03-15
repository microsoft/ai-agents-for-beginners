# สำรวจ Microsoft Agent Framework

![กรอบงานเอเจนต์](../../../translated_images/th/lesson-14-thumbnail.90df0065b9d234ee.webp)

### บทนำ

บทเรียนนี้จะครอบคลุม:

- ทำความเข้าใจ Microsoft Agent Framework: คุณสมบัติหลักและคุณค่า  
- สำรวจแนวคิดหลักของ Microsoft Agent Framework
- รูปแบบ MAF ขั้นสูง: เวิร์กโฟลว์, มิดเดิลแวร์ และหน่วยความจำ

## เป้าหมายการเรียนรู้

หลังจากทำบทเรียนนี้แล้ว คุณจะทราบวิธีการ:

- สร้าง AI Agents ที่พร้อมใช้งานในสภาพแวดล้อมการผลิตโดยใช้ Microsoft Agent Framework
- นำคุณสมบัติหลักของ Microsoft Agent Framework ไปประยุกต์ใช้กับกรณีการใช้งานเชิงตัวแทน (Agentic Use Cases)
- ใช้รูปแบบขั้นสูงรวมถึงเวิร์กโฟลว์ มิดเดิลแวร์ และการสังเกตการณ์

## ตัวอย่างโค้ด 

ตัวอย่างโค้ดสำหรับ [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) สามารถพบได้ใน repository นี้ภายใต้ไฟล์ `xx-python-agent-framework` และ `xx-dotnet-agent-framework`

## ทำความเข้าใจ Microsoft Agent Framework

![แนะนำกรอบงาน](../../../translated_images/th/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) เป็นกรอบงานรวมของ Microsoft สำหรับการสร้าง AI agents มันให้ความยืดหยุ่นในการรองรับกรณีการใช้งานเชิงตัวแทนหลากหลายรูปแบบที่พบได้ทั้งในสภาพแวดล้อมการผลิตและการวิจัย รวมถึง:

- **การจัดการแบบอนุกรมของเอเจนต์** ในสถานการณ์ที่ต้องการเวิร์กโฟลว์เป็นขั้นตอน
- **การจัดการแบบขนาน** ในสถานการณ์ที่เอเจนต์ต้องทำงานพร้อมกัน
- **การจัดการแชทกลุ่ม** ในสถานการณ์ที่เอเจนต์สามารถร่วมกันทำงานในภารกิจเดียว
- **การจัดการการส่งต่อ (Handoff)** ในสถานการณ์ที่เอเจนต์ส่งต่อภารกิจให้กันเมื่อซับทาสก์เสร็จสิ้น
- **การจัดการแบบ Magnetic** ในสถานการณ์ที่เอเจนต์ผู้จัดการสร้างและแก้ไขรายการภารกิจและประสานงานซับเอเจนต์เพื่อทำภารกิจให้เสร็จ

เพื่อมอบ AI Agents ในสภาพแวดล้อมการผลิต MAF ยังมีคุณสมบัติเพิ่มเติมสำหรับ:

- **การสังเกตการณ์ (Observability)** ผ่านการใช้ OpenTelemetry ที่ติดตามการกระทำของ AI Agent ทุกขั้นตอน รวมถึงการเรียกใช้งานเครื่องมือ การจัดการขั้นตอน การไหลของเหตุผล และการติดตามประสิทธิภาพผ่านแดชบอร์ดของ Microsoft Foundry
- **ความปลอดภัย (Security)** โดยการโฮสต์เอเจนต์แบบเนทีฟบน Microsoft Foundry ซึ่งรวมการควบคุมความปลอดภัยเช่นการเข้าถึงตามบทบาท การจัดการข้อมูลส่วนตัว และการป้องกันเนื้อหาในตัว
- **ความทนทาน (Durability)** เนื่องจากเธรดและเวิร์กโฟลว์ของเอเจนต์สามารถหยุดชั่วคราว กู้คืน และดำเนินต่อจากข้อผิดพลาดได้ ซึ่งทำให้รองรับกระบวนการที่ใช้เวลานานขึ้น
- **การควบคุม (Control)** โดยรองรับเวิร์กโฟลว์ที่มีมนุษย์อยู่ในวงจร (human-in-the-loop) ซึ่งภารกิจสามารถถูกกำหนดให้ต้องได้รับการอนุมัติจากมนุษย์

Microsoft Agent Framework ยังให้ความสำคัญกับความสามารถในการทำงานร่วมกันโดย:

- **ไม่ผูกกับคลาวด์ใดๆ (Being Cloud-agnostic)** - เอเจนต์สามารถรันในคอนเทนเนอร์ บนเซิร์ฟเวอร์ภายในองค์กร และข้ามหลายคลาวด์ต่างๆ
- **ไม่ผูกกับผู้ให้บริการใดๆ (Being Provider-agnostic)** - เอเจนต์สามารถถูกสร้างผ่าน SDK ที่คุณต้องการรวมถึง Azure OpenAI และ OpenAI
- **รวมมาตรฐานเปิด (Integrating Open Standards)** - เอเจนต์สามารถใช้โปรโตคอลเช่น Agent-to-Agent (A2A) และ Model Context Protocol (MCP) เพื่อค้นหาและใช้งานเอเจนต์และเครื่องมืออื่นๆ
- **ปลั๊กอินและคอนเน็กเตอร์ (Plugins and Connectors)** - สามารถเชื่อมต่อกับบริการข้อมูลและหน่วยความจำเช่น Microsoft Fabric, SharePoint, Pinecone และ Qdrant

มาดูกันว่าแอปพลิเคชันของคุณสมบัติเหล่านี้ถูกนำไปใช้กับแนวคิดหลักของ Microsoft Agent Framework อย่างไร

## แนวคิดหลักของ Microsoft Agent Framework

### เอเจนต์

![กรอบงานเอเจนต์](../../../translated_images/th/agent-components.410a06daf87b4fef.webp)

**การสร้างเอเจนต์**

การสร้างเอเจนต์ทำได้โดยการกำหนดบริการอนุมาน (LLM Provider) ชุดคำสั่งให้ AI Agent ปฏิบัติตาม และการกำหนด `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

ด้านบนเป็นการใช้ `Azure OpenAI` แต่เอเจนต์สามารถถูกสร้างโดยใช้บริการหลากหลายรวมถึง `Microsoft Foundry Agent Service`:

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

หรือเอเจนต์จากระยะไกลโดยใช้โปรโตคอล A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**การรันเอเจนต์**

เอเจนต์ถูกเรียกใช้โดยใช้เมธอด `.run` หรือ `.run_stream` สำหรับการตอบกลับแบบไม่สตรีมหรือแบบสตรีม

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

การรันเอเจนต์แต่ละครั้งยังสามารถมีตัวเลือกเพื่อปรับแต่งพารามิเตอร์เช่น `max_tokens` ที่เอเจนต์ใช้, `tools` ที่เอเจนต์สามารถเรียกใช้, และแม้แต่ `model` ที่เอเจนต์ใช้

สิ่งนี้มีประโยชน์ในกรณีที่ต้องใช้โมเดลหรือเครื่องมือเฉพาะสำหรับการทำงานให้เสร็จสิ้นตามที่ผู้ใช้ต้องการ

**เครื่องมือ (Tools)**

เครื่องมือสามารถกำหนดได้ทั้งเมื่อกำหนดเอเจนต์:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# เมื่อสร้าง ChatAgent โดยตรง

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

และยังสามารถกำหนดได้เมื่อรันเอเจนต์:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # เครื่องมือที่จัดเตรียมให้สำหรับการรันนี้เท่านั้น )
```

**เธรดของเอเจนต์ (Agent Threads)**

เธรดของเอเจนต์ใช้จัดการการสนทนาหลายตา (multi-turn) เธรดสามารถถูกสร้างได้โดย:

- ใช้ `get_new_thread()` ซึ่งทำให้เธรดนั้นถูกบันทึกไว้ได้เมื่อเวลาผ่านไป
- สร้างเธรดโดยอัตโนมัติเมื่อรันเอเจนต์ และเธรดนั้นจะมีอายุแค่ระหว่างการรันปัจจุบันเท่านั้น

ในการสร้างเธรด โค้ดจะมีลักษณะดังนี้:

```python
# สร้างเธรดใหม่.
thread = agent.get_new_thread() # รันเอเจนต์ด้วยเธรด.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

จากนั้นคุณสามารถซีเรียลไลซ์เธรดเพื่อเก็บไว้ใช้ภายหลังได้:

```python
# สร้างเธรดใหม่.
thread = agent.get_new_thread() 

# รันเอเจนต์ด้วยเธรดนั้น.

response = await agent.run("Hello, how are you?", thread=thread) 

# ซีเรียลไลซ์เธรดเพื่อการจัดเก็บ.

serialized_thread = await thread.serialize() 

# ดีซีเรียลไลซ์สถานะเธรดหลังจากโหลดจากการจัดเก็บ.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**มิดเดิลแวร์ของเอเจนต์ (Agent Middleware)**

เอเจนต์โต้ตอบกับเครื่องมือและ LLM เพื่อทำงานของผู้ใช้ให้เสร็จ ในบางสถานการณ์ เราอาจต้องการดำเนินการหรือติดตามระหว่างการโต้ตอบเหล่านี้ มิดเดิลแวร์ของเอเจนต์ช่วยให้เราทำสิ่งนี้ได้ผ่าน:

*Function Middleware*

มิดเดิลแวร์นี้อนุญาตให้เราดำเนินการระหว่างเอเจนต์กับฟังก์ชัน/เครื่องมือที่มันจะเรียกใช้งาน ตัวอย่างของการใช้งานคือเมื่อต้องการบันทึกล็อกของการเรียกฟังก์ชัน

ในโค้ดด้านล่าง `next` กำหนดว่าควรเรียกมิดเดิลแวร์ถัดไปหรือตัวฟังก์ชันจริง

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # การประมวลผลล่วงหน้า: บันทึกก่อนการเรียกใช้ฟังก์ชัน
    print(f"[Function] Calling {context.function.name}")

    # ดำเนินการต่อไปยังมิดเดิลแวร์ถัดไปหรือการเรียกใช้ฟังก์ชัน
    await next(context)

    # การประมวลผลภายหลัง: บันทึกหลังการเรียกใช้ฟังก์ชัน
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

มิดเดิลแวร์นี้อนุญาตให้เราดำเนินการหรือบันทึกล็อกระหว่างเอเจนต์กับคำขอที่ส่งไปยัง LLM

สิ่งนี้ประกอบด้วยข้อมูลสำคัญเช่น `messages` ที่ถูกส่งไปยังบริการ AI

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # การประมวลผลก่อน: บันทึกก่อนเรียกใช้งาน AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # ดำเนินการไปยังมิดเดิลแวร์หรือบริการ AI ถัดไป
    await next(context)

    # การประมวลผลภายหลัง: บันทึกหลังการตอบกลับของ AI
    print("[Chat] AI response received")

```

**หน่วยความจำของเอเจนต์ (Agent Memory)**

ตามที่กล่าวไว้ในบทเรียน `Agentic Memory` หน่วยความจำเป็นองค์ประกอบสำคัญที่ทำให้เอเจนต์สามารถทำงานในบริบทต่างๆ ได้ MAF เสนอหน่วยความจำหลายชนิด:

*การเก็บในหน่วยความจำภายใน (In-Memory Storage)*

นี่คือหน่วยความจำที่เก็บไว้ในเธรดระหว่าง runtime ของแอปพลิเคชัน

```python
# สร้างเธรดใหม่.
thread = agent.get_new_thread() # รันเอเจนต์ด้วยเธรดนั้น.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*ข้อความที่คงทน (Persistent Messages)*

หน่วยความจำนี้ใช้เมื่อเก็บประวัติการสนทนาข้ามเซสชันต่างๆ ถูกกำหนดโดยใช้ `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# สร้างที่เก็บข้อความแบบกำหนดเอง
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*หน่วยความจำไดนามิก (Dynamic Memory)*

หน่วยความจำนี้ถูกเพิ่มเข้าไปในบริบทก่อนที่เอเจนต์จะถูกรัน หน่วยความจำเหล่านี้สามารถเก็บในบริการภายนอกเช่น mem0:

```python
from agent_framework.mem0 import Mem0Provider

# ใช้ Mem0 สำหรับความสามารถหน่วยความจำขั้นสูง
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

**การสังเกตการณ์เอเจนต์ (Agent Observability)**

การสังเกตการณ์เป็นสิ่งสำคัญในการสร้างระบบเชิงตัวแทนที่เชื่อถือได้และดูแลรักษาได้ MAF ผนวกรวมกับ OpenTelemetry เพื่อให้การติดตาม (tracing) และเมตริกส์สำหรับการสังเกตการณ์ที่ดีขึ้น

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

### เวิร์กโฟลว์

MAF นำเสนอเวิร์กโฟลว์ซึ่งเป็นขั้นตอนที่กำหนดไว้ล่วงหน้าเพื่อทำภารกิจให้เสร็จและรวม AI agents เป็นส่วนประกอบในขั้นตอนเหล่านั้น

เวิร์กโฟลว์ประกอบด้วยส่วนประกอบต่างๆ ที่ช่วยให้การควบคุมการไหลของงานดีขึ้น นอกจากนี้เวิร์กโฟลว์ยังรองรับ **การจัดการหลายเอเจนต์ (multi-agent orchestration)** และ **การเก็บจุดเช็คพอยต์ (checkpointing)** เพื่อบันทึกสถานะของเวิร์กโฟลว์

ส่วนประกอบหลักของเวิร์กโฟลว์คือ:

**ผู้ปฏิบัติ (Executors)**

Executors รับข้อความนำเข้า ดำเนินงานที่ได้รับมอบหมาย แล้วผลิตข้อความผลลัพธ์ ซึ่งเป็นการขับเคลื่อนเวิร์กโฟลว์ไปสู่การทำภารกิจที่ใหญ่ขึ้นให้เสร็จ Executors อาจเป็นเอเจนต์ AI หรือเป็นลอจิกที่กำหนดเอง

**Edges**

Edges ใช้เพื่อกำหนดการไหลของข้อความในเวิร์กโฟลว์ ซึ่งอาจเป็น:

*Direct Edges* - การเชื่อมต่อแบบหนึ่งต่อหนึ่งอย่างง่ายระหว่าง executors:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - ถูกเปิดใช้งานหลังจากเงื่อนไขบางอย่างเป็นจริง เช่น เมื่อห้องพักโรงแรมไม่ว่าง executor หนึ่งสามารถเสนอทางเลือกอื่นได้

*Switch-case Edges* - นำทางข้อความไปยัง executors ต่างๆ ตามเงื่อนไขที่กำหนด เช่น หากลูกค้าเดินทางมีสิทธิ์พิเศษ งานของพวกเขาอาจถูกจัดการผ่านเวิร์กโฟลว์อื่น

*Fan-out Edges* - ส่งข้อความหนึ่งไปยังเป้าหมายหลายแห่ง

*Fan-in Edges* - รวบรวมข้อความหลายรายการจาก executors ต่างๆ แล้วส่งไปยังเป้าหมายเดียว

**เหตุการณ์ (Events)**

เพื่อให้การสังเกตเวิร์กโฟลว์ดียิ่งขึ้น MAF มีเหตุการณ์ในตัวสำหรับการประมวลผลรวมถึง:

- `WorkflowStartedEvent`  - การเริ่มต้นการประมวลผลของเวิร์กโฟลว์
- `WorkflowOutputEvent` - เวิร์กโฟลว์สร้างผลลัพธ์
- `WorkflowErrorEvent` - เวิร์กโฟลว์พบข้อผิดพลาด
- `ExecutorInvokeEvent`  - Executor เริ่มการประมวลผล
- `ExecutorCompleteEvent`  -  Executor เสร็จสิ้นการประมวลผล
- `RequestInfoEvent` - มีการออกคำขอ

## รูปแบบ MAF ขั้นสูง

ส่วนที่กล่าวมาข้างต้นครอบคลุมแนวคิดหลักของ Microsoft Agent Framework ขณะที่คุณสร้างเอเจนต์ที่ซับซ้อนยิ่งขึ้น นี่คือรูปแบบขั้นสูงที่ควรพิจารณา:

- **การประกอบมิดเดิลแวร์ (Middleware Composition)**: เชนหลายตัวจัดการมิดเดิลแวร์ (การบันทึกล็อก การตรวจสอบสิทธิ์ จำกัดอัตราการเรียก) โดยใช้ function และ chat middleware เพื่อการควบคุมพฤติกรรมเอเจนต์อย่างละเอียด
- **การเก็บจุดเช็คพอยต์ของเวิร์กโฟลว์ (Workflow Checkpointing)**: ใช้เหตุการณ์ของเวิร์กโฟลว์และการซีเรียลไลซ์เพื่อบันทึกและดำเนินการต่อกระบวนการเอเจนต์ที่ทำงานเป็นเวลานาน
- **การเลือกเครื่องมือแบบไดนามิก (Dynamic Tool Selection)**: รวม RAG บนคำอธิบายเครื่องมือกับการลงทะเบียนเครื่องมือของ MAF เพื่อแสดงเฉพาะเครื่องมือที่เกี่ยวข้องต่อคำถาม
- **การส่งต่อระหว่างหลายเอเจนต์ (Multi-Agent Handoff)**: ใช้ edges ของเวิร์กโฟลว์และการกำหนดเส้นทางตามเงื่อนไขเพื่อจัดการการส่งต่อระหว่างเอเจนต์ที่มีความเชี่ยวชาญเฉพาะด้าน

## ตัวอย่างโค้ด 

ตัวอย่างโค้ดสำหรับ Microsoft Agent Framework สามารถพบได้ใน repository นี้ภายใต้ไฟล์ `xx-python-agent-framework` และ `xx-dotnet-agent-framework`

## มีคำถามเพิ่มเติมเกี่ยวกับ Microsoft Agent Framework ไหม?

เข้าร่วม [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) เพื่อพบกับผู้เรียนคนอื่นๆ เข้าร่วมชั่วโมงให้คำปรึกษา และขอคำตอบสำหรับคำถามเกี่ยวกับ AI Agents ของคุณ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ข้อจำกัดความรับผิด:
เอกสารฉบับนี้ถูกแปลโดยใช้บริการแปลด้วยปัญญาประดิษฐ์ [Co-op Translator](https://github.com/Azure/co-op-translator). แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อนได้ เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลหลักที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ แนะนำให้ใช้การแปลโดยนักแปลมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลฉบับนี้.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->