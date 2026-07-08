# การสร้างแอปพลิเคชันหลายเอเจนต์ด้วย Microsoft Agent Framework Workflow

บทช่วยสอนนี้จะแนะนำคุณเกี่ยวกับการทำความเข้าใจและการสร้างแอปพลิเคชันหลายเอเจนต์โดยใช้ Microsoft Agent Framework เราจะสำรวจแนวคิดหลักของระบบหลายเอเจนต์ ดำดิ่งสู่สถาปัตยกรรมของส่วนประกอบ Workflow ของเฟรมเวิร์ก และเดินผ่านตัวอย่างใช้งานจริงในทั้ง Python และ .NET สำหรับรูปแบบโฟลว์งานที่แตกต่างกัน

## 1\. ความเข้าใจระบบหลายเอเจนต์

AI Agent คือระบบที่ก้าวข้ามความสามารถของโมเดลภาษาขนาดใหญ่ (LLM) ทั่วไป มันสามารถรับรู้สภาพแวดล้อม ตัดสินใจ และดำเนินการเพื่อบรรลุเป้าหมายเฉพาะ ระบบหลายเอเจนต์เกี่ยวข้องกับเอเจนต์หลายตัวที่ทำงานร่วมกันเพื่อแก้ปัญหาที่จะเป็นเรื่องยากหรือเป็นไปไม่ได้ที่เอเจนต์ตัวเดียวจะจัดการได้

### สถานการณ์การใช้งานทั่วไป

  * **การแก้ปัญหาที่ซับซ้อน**: การแบ่งงานขนาดใหญ่ (เช่น การวางแผนกิจกรรมทั่วทั้งบริษัท) เป็นงานย่อยที่จัดการโดยเอเจนต์เฉพาะทาง (เช่น เอเจนต์งบประมาณ, เอเจนต์โลจิสติกส์, เอเจนต์การตลาด)
  * **ผู้ช่วยเสมือน**: เอเจนต์ผู้ช่วยหลักที่มอบหมายงานอย่างการนัดหมาย, การวิจัย และการจอง ให้แก่อเจนต์เฉพาะทางอื่นๆ
  * **การสร้างเนื้อหาแบบอัตโนมัติ**: โฟลว์งานที่เอเจนต์หนึ่งร่างเนื้อหา, อีกเอเจนต์ตรวจสอบความถูกต้องและโทนเสียง และเอเจนต์ที่สามเผยแพร่เนื้อหา

### รูปแบบหลายเอเจนต์

ระบบหลายเอเจนต์สามารถจัดระเบียบในหลายรูปแบบ ซึ่งกำหนดวิธีที่พวกเขาสื่อสารกัน:

  * **แบบทวนลำดับ**: เอเจนต์ทำงานตามลำดับที่กำหนดไว้ เช่น สายการผลิต ผลลัพธ์ของเอเจนต์หนึ่งจะกลายเป็นข้อมูลนำเข้าของเอเจนต์ถัดไป
  * **แบบพร้อมกัน**: เอเจนต์ทำงานพร้อมกันในส่วนต่างๆ ของงาน และผลลัพธ์ของพวกเขาจะถูกรวมในตอนท้าย
  * **แบบมีเงื่อนไข**: โฟลว์งานดำเนินไปตามเส้นทางต่างๆ ขึ้นอยู่กับผลลัพธ์ของเอเจนต์ คล้ายกับคำสั่ง if-then-else

## 2\. สถาปัตยกรรม Microsoft Agent Framework Workflow

ระบบโฟลว์งานของ Agent Framework คือเครื่องมือออร์เคสตราที่ทันสมัยออกแบบมาเพื่อจัดการปฏิสัมพันธ์ที่ซับซ้อนระหว่างหลายเอเจนต์ มันถูกรวมบนสถาปัตยกรรมแบบกราฟที่ใช้ [รูปแบบการประมวลผลแบบ Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf) ซึ่งกระบวนการเกิดขึ้นในขั้นตอนที่ซิงโครไนซ์เรียกว่า "supersteps"

### ส่วนประกอบหลัก

สถาปัตยกรรมประกอบด้วยสามส่วนหลัก:

1.  **Executors**: เป็นหน่วยประมวลผลพื้นฐาน ในตัวอย่างของเรา `Agent` คือประเภทของ executor หนึ่ง executor แต่ละตัวสามารถมีตัวจัดการข้อความหลายตัวที่ถูกเรียกใช้โดยอัตโนมัติตามประเภทของข้อความที่ได้รับ
2.  **Edges**: กำหนดเส้นทางที่ข้อความเคลื่อนที่ระหว่าง executor อาจมีเงื่อนไขที่อนุญาตให้ข้อมูลผ่านกราฟโฟลว์งานได้แบบไดนามิก
3.  **Workflow**: ส่วนประกอบนี้เป็นตัวจัดการทั้งกระบวนการ ควบคุม executors, edges และการไหลโดยรวมของการทำงาน มันรับประกันว่าข้อความถูกประมวลผลตามลำดับที่ถูกต้องและสตรีมเหตุการณ์เพื่อการสังเกตการณ์

*แผนภาพที่แสดงส่วนประกอบหลักของระบบโฟลว์งาน*

โครงสร้างนี้ช่วยให้สร้างแอปพลิเคชันที่ทนทานและปรับขนาดได้โดยใช้รูปแบบพื้นฐานเช่น ลำดับสาย, fan-out/fan-in สำหรับประมวลผลคู่ขนาน และตรรกะ switch-case สำหรับการไหลที่มีเงื่อนไข

## 3\. ตัวอย่างใช้งานจริงและวิเคราะห์โค้ด

ตอนนี้มาดูกันว่าเราจะนำรูปแบบโฟลว์งานต่างๆ ไปใช้งานโดยใช้เฟรมเวิร์กนี้ได้อย่างไร เราจะดูทั้งโค้ด Python และ .NET ในแต่ละตัวอย่าง

### กรณีที่ 1: โฟลว์งานแบบทวนลำดับพื้นฐาน

นี่คือรูปแบบที่ง่ายที่สุด ที่เอเจนต์ตัวหนึ่งส่งออกผลไปยังเอเจนต์อีกตัวโดยตรง สถานการณ์ของเราคือเอเจนต์ `FrontDesk` โรงแรมที่แนะนำการเดินทาง และได้รับการตรวจสอบโดยเอเจนต์ `Concierge`

*แผนภาพโฟลว์งานพื้นฐาน FrontDesk -> Concierge*

#### เบื้องหลังสถานการณ์

นักเดินทางขอคำแนะนำในกรุงปารีส

1.  เอเจนต์ `FrontDesk` ออกแบบมาให้กระชับ แนะนำให้ไปเยี่ยมชมพิพิธภัณฑ์ลูฟวร์
2.  เอเจนต์ `Concierge` ซึ่งให้ความสำคัญกับประสบการณ์แท้จริง รับการแนะนำนี้ ตรวจสอบคำแนะนำ และให้ข้อเสนอแนะ แนะนำทางเลือกที่เป็นท้องถิ่นมากขึ้นและไม่ใช่สถานที่ท่องเที่ยวมากเกินไป

#### วิเคราะห์การใช้งาน Python

ในตัวอย่าง Python ก่อนอื่นเราจะนิยามและสร้างสองเอเจนต์ โดยแต่ละตัวมีคำแนะนำเฉพาะ

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# กำหนดบทบาทและคำแนะนำของเอเจนต์
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# สร้างอินสแตนซ์ของเอเจนต์
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

ถัดไปใช้ `WorkflowBuilder` เพื่อสร้างกราฟ กำหนด `front_desk_agent` เป็นจุดเริ่มต้น และสร้าง edge เพื่อเชื่อมผลลัพธ์ของมันกับ `reviewer_agent`

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

สุดท้ายรัน workflow ด้วยคำพูดเริ่มต้นของผู้ใช้

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run ดำเนินการ workflow; get_outputs() คืนค่าผลลัพธ์ของตัวดำเนินการผลลัพธ์.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### วิเคราะห์การใช้งาน .NET (C\#)

เวอร์ชัน .NET ใช้ตรรกะที่คล้ายกันมาก ก่อนอื่นกำหนดค่าคงที่สำหรับชื่อและคำแนะนำของเอเจนต์

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

สร้างเอเจนต์โดยใช้ `AzureOpenAIClient` (Responses API) จากนั้น `WorkflowBuilder` กำหนดการไหลแบบทวนลำดับโดยเพิ่ม edge จาก `frontDeskAgent` ไปยัง `reviewerAgent`

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

จากนั้นรัน workflow ด้วยข้อความของผู้ใช้ และผลลัพธ์จะถูกสตรีมกลับมา

### กรณีที่ 2: โฟลว์งานแบบทวนลำดับหลายขั้นตอน

รูปแบบนี้ขยายลำดับพื้นฐานเพื่อรวมเอเจนต์มากขึ้น เหมาะสำหรับกระบวนการที่ต้องการหลายขั้นตอนของการปรับปรุงหรือแปลงข้อมูล

#### เบื้องหลังสถานการณ์

ผู้ใช้ให้ภาพของห้องนั่งเล่นและขอใบเสนอราคาสำหรับเฟอร์นิเจอร์

1.  **Sales-Agent**: ระบุรายการเฟอร์นิเจอร์ในภาพและสร้างรายการ
2.  **Price-Agent**: รับรายการสินค้าและให้รายละเอียดราคาพร้อมงบประมาณ ตัวเลือกระดับกลาง และระดับพรีเมียม
3.  **Quote-Agent**: รับรายการราคาที่ได้รับและจัดฟอร์แมตเป็นเอกสารใบเสนอราคาในรูปแบบ Markdown

*แผนภาพโฟลว์งาน Sales -> Price -> Quote*

#### วิเคราะห์การใช้งาน Python

กำหนดเอเจนต์สามตัว โดยแต่ละตัวมีบทบาทเฉพาะ workflow ถูกสร้างโดยใช้ `add_edge` เพื่อสร้างลำดับ: `sales_agent` -> `price_agent` -> `quote_agent`

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# สร้างตัวแทนเฉพาะทางสามตัว
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# สร้างลำดับการทำงานแบบต่อเนื่อง
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ข้อมูลนำเข้าเป็น `ChatMessage` ที่รวมข้อความและ URI รูปภาพ เฟรมเวิร์กจัดการการส่งต่อผลลัพธ์ของเอเจนต์แต่ละตัวไปยังถัดไปในลำดับจนได้ใบเสนอราคาสุดท้าย

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# ข้อความของผู้ใช้มีทั้งข้อความและรูปภาพ
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# รันเวิร์กโฟลว์
events = await workflow.run(message)
```

#### วิเคราะห์การใช้งาน .NET (C\#)

ตัวอย่าง .NET สะท้อนเวอร์ชัน Python สร้างเอเจนต์สามตัว (`salesagent`, `priceagent`, `quoteagent`) `WorkflowBuilder` เชื่อมโยงพวกเขาแบบทวนลำดับ

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent priceagent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent quoteagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

ข้อความของผู้ใช้สร้างด้วยข้อมูลภาพ (ในรูปแบบไบต์) และข้อความคำสั่ง รันโดย `InProcessExecution.StreamAsync` และจับผลลัพธ์สุดท้ายจากสตรีม

### กรณีที่ 3: โฟลว์งานแบบพร้อมกัน

รูปแบบนี้ใช้เมื่อภารกิจสามารถทำพร้อมกันเพื่อลดเวลา โดยเป็นการ "แฟนเอาท์" ไปยังหลายเอเจนต์ และ "แฟนอิน" เพื่อรวบรวมผลลัพธ์

#### เบื้องหลังสถานการณ์

ผู้ใช้ขอวางแผนทริปไปซีแอตเทิล

1.  **Dispatcher (Fan-Out)**: คำขอของผู้ใช้ถูกส่งไปยังสองเอเจนต์พร้อมกัน
2.  **Researcher-Agent**: วิจัยสถานที่ท่องเที่ยว สภาพอากาศ และข้อควรระวังของทริปในฤดูธันวาคมที่ซีแอตเทิล
3.  **Plan-Agent**: สร้างแผนการเดินทางละเอียดตามวันอย่างอิสระ
4.  **Aggregator (Fan-In)**: รวบรวมผลลัพธ์จากทั้งนักวิจัยและนักวางแผน และนำเสนอเป็นผลลัพธ์สุดท้าย

*แผนภาพโฟลว์งาน concurrent ของ Researcher และ Planner*

#### วิเคราะห์การใช้งาน Python

`ConcurrentBuilder` ช่วยให้ง่ายต่อการสร้างรูปแบบนี้ แค่ระบุรายชื่อเอเจนต์ที่เข้าร่วม และบิลเดอร์จะสร้างแฟนเอาท์และแฟนอินโดยอัตโนมัติ

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder จัดการตรรกะการกระจายและรวบรวม
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# รันเวิร์กโฟลว์
events = await workflow.run("Plan a trip to Seattle in December")
```

เฟรมเวิร์กรับประกันว่า `research_agent` และ `plan_agent` ทำงานพร้อมกัน และรวบรวมผลลัพธ์สุดท้ายลงในรายการ

#### วิเคราะห์การใช้งาน .NET (C\#)

ใน .NET รูปแบบนี้ต้องมีการกำหนดชัดเจนมากขึ้น สร้าง custom executors (`ConcurrentStartExecutor` และ `ConcurrentAggregationExecutor`) เพื่อจัดการแฟนเอาท์และแฟนอิน

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

`WorkflowBuilder` ใช้ `AddFanOutEdge` และ `AddFanInEdge` เพื่อสร้างกราฟพร้อมกับ executors และเอเจนต์เหล่านี้

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### กรณีที่ 4: โฟลว์งานแบบมีเงื่อนไข

โฟลว์งานแบบมีเงื่อนไขเพิ่มตรรกะการแยกทางเลือก ช่วยให้ระบบดำเนินไปตามเส้นทางต่างกันขึ้นอยู่กับผลลัพธ์ระหว่างกลาง

#### เบื้องหลังสถานการณ์

โฟลว์งานนี้อัตโนมัติการสร้างและการเผยแพร่บทเรียนเชิงเทคนิค

1.  **Evangelist-Agent**: เขียนร่างบทเรียนตามโครงร่างและ URL ที่ให้มา
2.  **ContentReviewer-Agent**: ตรวจสอบร่าง โดยตรวจว่าจำนวนคำเกิน 200 คำหรือไม่
3.  **สาขาเงื่อนไข**:
      * **อนุมัติ (`Yes`)**: โปรแกรมดำเนินไปยัง `Publisher-Agent`
      * **ปฏิเสธ (`No`)**: โฟลว์งานหยุดและแสดงเหตุผลการปฏิเสธ
4.  **Publisher-Agent**: ถ้าร่างได้รับการอนุมัติ เอเจนต์นี้บันทึกเนื้อหาเป็นไฟล์ Markdown

#### วิเคราะห์การใช้งาน Python

ตัวอย่างนี้ใช้ฟังก์ชันกำหนดเอง `select_targets` เพื่อใช้ตรรกะมีเงื่อนไข ส่งฟังก์ชันนี้ให้กับ `add_multi_selection_edge_group` และกำหนดโฟลว์งานตามฟิลด์ `review_result` จากผลลัพธ์ของผู้ตรวจสอบ

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# ฟังก์ชันนี้ใช้กำหนดขั้นตอนถัดไปตามผลการตรวจสอบ
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # หากได้รับการอนุมัติ ให้ดำเนินการต่อไปยังตัวดำเนินการ 'save_draft'
        return [save_draft_id]
    else:
        # หากถูกปฏิเสธ ให้ดำเนินการต่อไปยังตัวดำเนินการ 'handle_review' เพื่อรายงานความล้มเหลว
        return [handle_review_id]

# ตัวสร้างเวิร์กโฟลว์ใช้ฟังก์ชันการเลือกสำหรับการกำหนดเส้นทาง
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # ขอบเขตการเลือกหลายรายการเป็นการใช้งานตรรกะเงื่อนไข
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

ใช้ custom executors เช่น `to_reviewer_result` เพื่อแปลงผล JSON จากเอเจนต์เป็นอ็อบเจกต์ชนิดเข้มงวดที่ฟังก์ชันเลือกตรวจสอบ

#### วิเคราะห์การใช้งาน .NET (C\#)

เวอร์ชัน .NET ใช้วิธีคล้ายกันกับฟังก์ชันเงื่อนไข กำหนด `Func<object?, bool>` เพื่อตรวจสอบคุณสมบัติ `Result` ของอ็อบเจกต์ `ReviewResult`

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

พารามิเตอร์ `condition` ของเมธอด `AddEdge` ช่วยให้ `WorkflowBuilder` สร้างเส้นทางแยกทาง เลือกโฟลว์ไปยัง `publishExecutor` เมื่อตรงตามเงื่อนไข `GetCondition(expectedResult: "Yes")` เท่านั้น มิฉะนั้นจะเลือกเส้นทางไปยัง `sendReviewerExecutor`

## สรุป

Microsoft Agent Framework Workflow ให้รากฐานที่แข็งแกร่งและยืดหยุ่นสำหรับการออร์เคสตราระบบหลายเอเจนต์ที่ซับซ้อน ด้วยการใช้สถาปัตยกรรมกราฟและส่วนประกอบหลักของมัน นักพัฒนาสามารถออกแบบและใช้งานโฟลว์งานขั้นสูงในทั้ง Python และ .NET ไม่ว่าคุณจะต้องการเพียงการประมวลผลแบบทวนลำดับธรรมดา, การประมวลผลคู่ขนาน หรือระบบที่มีตรรกะมีเงื่อนไขไดนามิก เฟรมเวิร์กนี้ก็พร้อมให้เครื่องมือในการสร้างโซลูชัน AI ที่ทรงพลัง ขยายขนาดได้ และปลอดภัยในเชิงชนิดข้อมูล

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->