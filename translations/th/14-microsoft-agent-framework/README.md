# การสำรวจ Microsoft Agent Framework

![Agent Framework](../../../translated_images/th/lesson-14-thumbnail.90df0065b9d234ee.webp)

### บทนำ

บทเรียนนี้จะครอบคลุม:

- การทำความเข้าใจ Microsoft Agent Framework: คุณสมบัติหลักและคุณค่า  
- การสำรวจแนวคิดหลักของ Microsoft Agent Framework
- รูปแบบ MAF ขั้นสูง: โฟลว์งาน, มิดเดิลแวร์ และหน่วยความจำ

## เป้าหมายการเรียนรู้

หลังจากจบบทเรียนนี้ คุณจะรู้วิธี:

- สร้าง AI Agents ที่พร้อมใช้งานจริงโดยใช้ Microsoft Agent Framework
- นำคุณสมบัติหลักของ Microsoft Agent Framework ไปใช้กับกรณีการใช้งาน Agentic ของคุณ
- ใช้รูปแบบขั้นสูงได้แก่ โฟลว์งาน, มิดเดิลแวร์ และการสังเกตการณ์

## ตัวอย่างโค้ด 

ตัวอย่างโค้ดสำหรับ [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) สามารถพบได้ในที่เก็บนี้ภายใต้ไฟล์ `xx-python-agent-framework` และ `xx-dotnet-agent-framework`

## การทำความเข้าใจ Microsoft Agent Framework

![Framework Intro](../../../translated_images/th/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) เป็นกรอบงานแบบรวมศูนย์ของ Microsoft สำหรับการสร้าง AI agents ซึ่งมีความยืดหยุ่นในการรองรับกรณีการใช้งาน agentic หลากหลายรูปแบบทั้งในสภาพแวดล้อมการผลิตและการวิจัย รวมถึง:

- **การจัดลำดับขั้นตอน Agent แบบต่อเนื่อง** ในสถานการณ์ที่ต้องการโฟลว์งานแบบทีละขั้นตอน
- **การจัดลำดับงานพร้อมกัน** ในสถานการณ์ที่ agents ต้องทำงานให้เสร็จพร้อมกัน
- **การจัดลำดับแชทเป็นกลุ่ม** ในสถานการณ์ที่ agents สามารถทำงานร่วมกันในงานเดียว
- **การส่งต่อการจัดลำดับ** ในสถานการณ์ที่ agents ส่งงานย่อยต่อกันเมื่อเสร็จสิ้นงานย่อย ๆ
- **การจัดลำดับจูงใจ** ในสถานการณ์ที่ agent ผู้จัดการสร้างและแก้ไขรายการงานและจัดการการประสานงานของ subagents เพื่อให้งานเสร็จสมบูรณ์

เพื่อให้ AI Agents พร้อมสำหรับการใช้งานจริง, MAF ยังมีคุณสมบัติสำหรับ:

- **การสังเกตการณ์** ผ่านการใช้ OpenTelemetry ที่บันทึกการทำงานของ AI Agent ทุกขั้นตอนรวมถึงการเรียกใช้เครื่องมือ, ขั้นตอนการจัดลำดับ, โฟลว์การวิเคราะห์และการตรวจสอบประสิทธิภาพผ่านแดชบอร์ด Microsoft Foundry
- **ความปลอดภัย** โดยการโฮสต์ agents บน Microsoft Foundry ซึ่งรวมถึงการควบคุมด้านความปลอดภัยเช่นการเข้าถึงแบบมีบทบาท, การจัดการข้อมูลส่วนตัว และความปลอดภัยของเนื้อหาแบบ built-in
- **ความทนทาน** โดย threads และ workflow ของ agent สามารถหยุด, เริ่มใหม่และกู้คืนจากข้อผิดพลาดได้ ซึ่งช่วยให้กระบวนการทำงานระยะยาวเป็นไปได้
- **การควบคุม** ด้วยโฟลว์งานที่มีมนุษย์ร่วมในวงจรซึ่งงานจะถูกทำเครื่องหมายว่าต้องการการอนุมัติจากมนุษย์

Microsoft Agent Framework ยังเน้นให้สามารถทำงานร่วมกับระบบอื่นได้โดย:

- **เป็นอิสระจากคลาวด์** - Agents สามารถทำงานในคอนเทนเนอร์, บนระบบภายใน หรือบนคลาวด์ที่หลากหลาย
- **เป็นอิสระจากผู้ให้บริการ** - Agents สามารถสร้างผ่าน SDK ที่คุณชอบได้ เช่น Azure OpenAI และ OpenAI
- **รวมมาตรฐานแบบเปิด** - Agents สามารถใช้โปรโตคอลเช่น Agent-to-Agent (A2A) และ Model Context Protocol (MCP) เพื่อค้นหาและใช้ agents และเครื่องมืออื่นๆ
- **ปลั๊กอินและตัวเชื่อมต่อ** - สามารถเชื่อมต่อกับบริการข้อมูลและหน่วยความจำเช่น Microsoft Fabric, SharePoint, Pinecone และ Qdrant

มาดูว่าคุณสมบัติเหล่านี้ถูกประยุกต์ใช้กับแนวคิดหลักของ Microsoft Agent Framework อย่างไรบ้าง

## แนวคิดหลักของ Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/th/agent-components.410a06daf87b4fef.webp)

**การสร้าง Agents**

การสร้าง Agent เป็นการกำหนดบริการการอนุมาน (ผู้ให้บริการ LLM), 
ชุดคำสั่งที่ AI Agent จะปฏิบัติตาม และกำหนด `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

ข้างต้นใช้ `Azure OpenAI` แต่ agents สามารถสร้างได้โดยใช้บริการหลากหลายรวมถึง `Microsoft Foundry Agent Service`:

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

หรือ [MiniMax](https://platform.minimaxi.com/) ซึ่งให้ API ที่เข้ากันได้กับ OpenAI พร้อมหน้าต่างบริบทขนาดใหญ่ (สูงสุด 204K token):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

หรือ agents ระยะไกลโดยใช้โปรโตคอล A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**การรัน Agents**

Agents ถูกเรียกใช้โดยใช้เมธอด `.run` หรือ `.run_stream` สำหรับตอบแบบไม่สตรีมหรือแบบสตรีม

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

การเรียกใช้แต่ละครั้งสามารถมีตัวเลือกเพื่อปรับแต่งพารามิเตอร์ เช่น `max_tokens` ที่ agent ใช้, `tools` ที่ agent สามารถเรียกใช้ และแม้แต่ `model` ที่ใช้กับ agent นั้น

ซึ่งมีประโยชน์ในกรณีที่ต้องใช้โมเดลหรือเครื่องมือเฉพาะสำหรับทำงานให้สำเร็จตามคำขอของผู้ใช้

**เครื่องมือ**

เครื่องมือสามารถกำหนดได้ทั้งตอนสร้าง agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# เมื่อสร้าง ChatAgent โดยตรง

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

และตอนเรียกใช้ agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # เครื่องมือที่ให้มาสำหรับการรันครั้งนี้เท่านั้น )
```

**Agent Threads**

Agent Threads ใช้จัดการบทสนทนาหลายรอบ (multi-turn) โดย threads สามารถสร้างโดยวิธี:

- ใช้ `get_new_thread()` ซึ่งช่วยให้ thread นั้นถูกบันทึกเก็บไว้ใช้ในอนาคต
- สร้าง thread อัตโนมัติเมื่อรัน agent และ thread จะมีอายุแค่ระยะเวลารันนั้นเท่านั้น

การสร้าง thread ดูได้จากโค้ดตัวอย่างนี้:

```python
# สร้างเธรดใหม่
thread = agent.get_new_thread() # รันเอเจนต์ด้วยเธรดนั้น
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

จากนั้นคุณสามารถทำการซีเรียลไลซ์ thread เพื่อเก็บไว้ใช้ภายหลัง:

```python
# สร้างเธรดใหม่
thread = agent.get_new_thread() 

# รันตัวแทนด้วยเธรดนั้น

response = await agent.run("Hello, how are you?", thread=thread) 

# แปลงเธรดเป็นข้อมูลสำหรับจัดเก็บ

serialized_thread = await thread.serialize() 

# แปลงข้อมูลเธรดกลับเป็นสถานะหลังจากโหลดจากที่จัดเก็บ

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agents มีปฏิสัมพันธ์กับเครื่องมือและ LLM เพื่อทำงานของผู้ใช้ ในบางสถานการณ์ เราอาจต้องทำการประมวลผลหรือบันทึกข้อมูลระหว่างการโต้ตอบเหล่านี้ Agent middleware ทำให้เราทำเช่นนี้ได้โดย:

*Function Middleware*

middleware นี้ช่วยให้เราสามารถดำเนินการบางอย่างระหว่าง agent และฟังก์ชัน/เครื่องมือที่เรียกใช้ได้ ตัวอย่างเช่น การบันทึกล็อกเมื่อมีการเรียกฟังก์ชัน

ในโค้ดด้านล่าง `next` จะกำหนดว่าควรเรียก middleware ถัดไปหรือฟังก์ชันจริง

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # การประมวลผลล่วงหน้า: บันทึกก่อนการเรียกใช้ฟังก์ชัน
    print(f"[Function] Calling {context.function.name}")

    # ดำเนินการต่อไปยังมิดเดิลแวร์หรือการเรียกใช้ฟังก์ชันถัดไป
    await next(context)

    # การประมวลผลภายหลัง: บันทึกหลังจากเรียกใช้ฟังก์ชัน
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

middleware นี้ช่วยให้เราสามารถดำเนินการหรือบันทึกระหว่าง agent กับคำขอไปยัง LLM

มีข้อมูลสำคัญเช่น `messages` ที่ส่งไปยังบริการ AI

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # การประมวลผลก่อนหน้า: บันทึกก่อนเรียก AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # ดำเนินการต่อไปยังมิดเดิลแวร์หรือบริการ AI ถัดไป
    await next(context)

    # การประมวลผลหลัง: บันทึกหลังจากได้รับตอบกลับจาก AI
    print("[Chat] AI response received")

```

**Agent Memory**

ดังที่ได้กล่าวในบทเรียน `Agentic Memory` หน่วยความจำเป็นองค์ประกอบสำคัญในการทำให้ agent ทำงานได้ในหลายบริบท MAF มีหน่วยความจำหลายประเภท:

*หน่วยความจำในตัว (In-Memory Storage)*

หน่วยความจำนี้ถูกเก็บใน threads ในระหว่างการรันแอปพลิเคชัน

```python
# สร้างเธรดใหม่
thread = agent.get_new_thread() # รันเอเจนต์ด้วยเธรดนั้น
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*ข้อความที่เก็บถาวร (Persistent Messages)*

หน่วยความจำนี้ใช้เก็บประวัติการสนทนาข้าม session ต่าง ๆ กำหนดโดย `chat_message_store_factory` :

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

*หน่วยความจำไดนามิก (Dynamic Memory)*

หน่วยความจำนี้ถูกเพิ่มในบริบทก่อนที่ agents จะทำงาน หน่วยความจำเหล่านี้สามารถเก็บในบริการภายนอกเช่น mem0:

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

**การสังเกตการณ์ของ Agent (Agent Observability)**

การสังเกตการณ์เป็นสิ่งสำคัญสำหรับการสร้างระบบ agentic ที่น่าเชื่อถือและดูแลรักษาง่าย MAF ผสานรวมกับ OpenTelemetry เพื่อให้มีการติดตามและเครื่องมือวัดเพื่อการสังเกตการณ์ที่ดีขึ้น

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # ทำบางสิ่ง
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### โฟลว์งาน (Workflows)

MAF มีโฟลว์งานที่เป็นขั้นตอนที่กำหนดไว้ล่วงหน้าเพื่อทำงานให้เสร็จ รวม AI agents เป็นส่วนประกอบในแต่ละขั้นตอน

โฟลว์งานประกอบด้วยส่วนประกอบต่าง ๆ ที่ช่วยให้ควบคุมการไหลของงานได้ดีขึ้น โฟลว์งานยังสนับสนุน **การจัดลำดับหลาย agents** และ **การบันทึกสถานะ (checkpointing)** เพื่อเก็บสถานะของงาน

ส่วนประกอบหลักของโฟลว์งานคือ:

**Executors**

Executors รับข้อความอินพุต, ทำงานที่ได้รับมอบหมาย และสร้างข้อความผลลัพธ์ ทำให้งานโฟลว์เดินหน้าต่อไปเพื่อทำงานใหญ่ให้เสร็จ Executors อาจเป็น AI agent หรือเป็นตรรกะกำหนดเองได้

**Edges**

Edges ใช้กำหนดไหลของข้อความในโฟลว์งาน ซึ่งอาจเป็น:

*Direct Edges* - การเชื่อมต่อแบบหนึ่งต่อหนึ่งอย่างง่ายระหว่าง executors:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - เปิดใช้งานหลังจากเงื่อนไขบางประการเป็นจริง เช่น เมื่อห้องพักโรงแรมไม่ว่าง executor จะเสนอทางเลือกอื่น

*Switch-case Edges* - นำทางข้อความไปยัง executors ต่าง ๆ ตามเงื่อนไขที่กำหนด เช่น หากลูกค้าการเดินทางมีสิทธิ์เข้าถึงพิเศษและงานของพวกเขาจะถูกจัดการผ่านโฟลว์งานอื่น

*Fan-out Edges* - ส่งข้อความหนึ่งไปยังเป้าหมายหลายรายการ

*Fan-in Edges* - รวบรวมหลายข้อความจาก executors ต่าง ๆ แล้วส่งไปยังเป้าหมายเดียว

**Events**

เพื่อให้การสังเกตโฟลว์งานดีขึ้น MAF มีเหตุการณ์ในตัวสำหรับการทำงาน เช่น:

- `WorkflowStartedEvent`  - เริ่มการทำงานของโฟลว์งาน
- `WorkflowOutputEvent` - โฟลว์งานผลิตผลลัพธ์
- `WorkflowErrorEvent` - โฟลว์งานพบข้อผิดพลาด
- `ExecutorInvokeEvent`  - Executor เริ่มประมวลผล
- `ExecutorCompleteEvent`  - Executor เสร็จสิ้นการประมวลผล
- `RequestInfoEvent` - มีการร้องขอ

## รูปแบบ MAF ขั้นสูง

ส่วนข้างต้นครอบคลุมแนวคิดหลักของ Microsoft Agent Framework เมื่อคุณสร้าง agents ที่ซับซ้อนขึ้น นี่คือรูปแบบขั้นสูงที่ควรพิจารณา:

- **การประสานมิดเดิลแวร์ (Middleware Composition)**: เชื่อมต่อมิดเดิลแวร์หลาย ๆ ตัว (ล็อก, การยืนยันตัวตน, การจำกัดอัตรา) ด้วย function และ chat middleware เพื่อควบคุมพฤติกรรม agent อย่างละเอียด
- **การบันทึกสถานะของโฟลว์งาน (Workflow Checkpointing)**: ใช้เหตุการณ์โฟลว์งานและการซีเรียลไลซ์เพื่อบันทึกและทำงาน agent ระยะยาวต่อเนื่องได้
- **การเลือกเครื่องมือแบบไดนามิก (Dynamic Tool Selection)**: รวม RAG กับคำอธิบายเครื่องมือและการลงทะเบียนเครื่องมือของ MAF เพื่อแสดงเฉพาะเครื่องมือที่เกี่ยวข้องกับคำถามนั้น ๆ
- **การส่งต่อหลาย agents (Multi-Agent Handoff)**: ใช้ edges ของโฟลว์งานและการนำทางตามเงื่อนไขเพื่อจัดลำดับการส่งต่อระหว่าง agents ที่เชี่ยวชาญต่าง ๆ

## การโฮสต์ LangChain / LangGraph Agents บน Microsoft Foundry

Microsoft Agent Framework เป็น **framework-interoperable** — คุณไม่จำกัดแค่ agents ที่เขียนด้วย MAF เท่านั้น ถ้าคุณมี agent ที่สร้างด้วย **LangChain** หรือ **LangGraph** อยู่แล้ว คุณสามารถรันมันในฐานะ **agent ที่โฮสต์บน Microsoft Foundry** เพื่อให้ Foundry ดูแล runtime, sessions, การปรับขนาด, ตัวตน และจุดเชื่อมต่อโปรโตคอล ในขณะที่ตรรกะ agent ของคุณยังคงอยู่ใน LangGraph

สิ่งนี้ทำได้ด้วยแพ็กเกจ `langchain_azure_ai.agents.hosting` ซึ่งเปิดใช้กราฟ LangGraph ที่คอมไพล์แล้วผ่านโปรโตคอลเดียวกับที่ agent ที่โฮสต์บน Foundry ใช้

**1. ติดตั้ง hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` extra จะติดตั้งไลบรารีโปรโตคอล Foundry: `azure-ai-agentserver-responses` (จุดเชื่อมต่อ `/responses` ที่เข้ากันได้กับ OpenAI) และ `azure-ai-agentserver-invocations` (จุดเชื่อมต่อทั่วไป `/invocations`)

**2. เลือกโปรโตคอลโฮสต์:**

| Protocol | คลาสโฮสต์ | Endpoint | ใช้เมื่อ |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | คุณต้องการ chat, สตรีม, ประวัติการตอบ และ threading แบบ OpenAI-compatible — เป็นค่าเริ่มต้นที่แนะนำสำหรับ agents แบบสนทนา |
| **Invocations** | `InvocationsHostServer` | `/invocations` | คุณต้องการ JSON รูปแบบกำหนดเอง, จุดเชื่อมต่อแบบ webhook, หรือการประมวลผลที่ไม่ใช่การสนทนา |

เนื่องจาก **API Responses เป็น API หลักสำหรับการพัฒนา agent-style ใน Foundry** ให้เริ่มที่ `ResponsesHostServer` สำหรับ agents ส่วนใหญ่

**3. ตั้งค่าตัวแปรสภาพแวดล้อม** (`az login` ก่อนเพื่อ `DefaultAzureCredential` จะได้ทำการยืนยันตัวตน):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

เมื่อ agent รันในฐานะ agent ที่โฮสต์บน Foundry แพลตฟอร์มจะใส่ค่า `FOUNDRY_PROJECT_ENDPOINT` ให้โดยอัตโนมัติ

**4. เปิดเผย agent LangGraph ผ่านโปรโตคอล Responses:**

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

    # ChatOpenAI ที่นี่มุ่งเป้าไปที่จุดสิ้นสุดที่รองรับ OpenAI (Responses) ของโครงการ Foundry.
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

รันแบบโลคอลด้วย `python main.py` แล้วส่งคำร้องขอ Responses ไปที่ `http://localhost:8088/responses`

**พฤติกรรมหลัก:**

- **การสนทนา**: ลูกค้าสามารถดำเนินการสนทนาต่อด้วยการส่ง `previous_response_id` หรือ ID `conversation` หากกราฟคอมไพล์ด้วย LangGraph checkpointer, Foundry จะเก็บสถานะสนทนาไว้กับจุดบันทึก (ใช้ durable checkpointer ในโปรดักชัน; `MemorySaver` เหมาะสำหรับทดสอบโลคอล)
- **มนุษย์ในวงจร (Human-in-the-loop)**: หากกราฟใช้ LangGraph `interrupt()`, `ResponsesHostServer` จะแสดง interrupt ที่รอดำเนินการเป็นไอเท็ม Responses `function_call` / `mcp_approval_request`, ลูกค้าจะดำเนินการต่อด้วย `function_call_output` / `mcp_approval_response` ที่ตรงกัน
- **ดีพลอยบน Foundry**: ใช้ Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (โลคอล, ต้องมี Docker), แล้ว `azd provision` และ `azd deploy` การดีพลอย agent ที่โฮสต์ต้องมีบทบาท **Foundry Project Manager**

ตัวอย่างโค้ดที่รันได้ของนี้อยู่ใน [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) สำหรับคำแนะนำเต็ม (โปรโตคอล Invocations, เงื่อนไขคำขอกำหนดเอง และการแก้ปัญหา) ดูที่ [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)

## ตัวอย่างโค้ด 

ตัวอย่างโค้ดสำหรับ Microsoft Agent Framework พบได้ในที่เก็บนี้ภายใต้ไฟล์ `xx-python-agent-framework` และ `xx-dotnet-agent-framework`

## มีคำถามเพิ่มเติมเกี่ยวกับ Microsoft Agent Framework ไหม?

เข้าร่วมใน [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) เพื่อพบกับผู้เรียนท่านอื่น ๆ เข้าร่วมชั่วโมงตอบคำถาม และได้รับคำตอบเกี่ยวกับ AI Agents
## บทเรียนก่อนหน้า

[Memory for AI Agents](../13-agent-memory/README.md)

## บทเรียนถัดไป

[Building Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->