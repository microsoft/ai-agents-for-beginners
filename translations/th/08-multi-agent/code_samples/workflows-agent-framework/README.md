# การสร้างแอปพลิเคชันหลายตัวแทนด้วย Microsoft Agent Framework Workflow

บทช่วยสอนนี้จะแนะนำคุณเกี่ยวกับความเข้าใจและการสร้างแอปพลิเคชันหลายตัวแทนโดยใช้ Microsoft Agent Framework เราจะสำรวจแนวคิดพื้นฐานของระบบหลายตัวแทน ดำดิ่งสู่สถาปัตยกรรมของส่วนประกอบ Workflow ของเฟรมเวิร์ก และเดินผ่านตัวอย่างใช้งานจริงในทั้ง Python และ .NET สำหรับรูปแบบ workflow ที่แตกต่างกัน

## 1\. การเข้าใจระบบหลายตัวแทน

ตัวแทน AI คือระบบที่มีความสามารถเกินกว่าระบบ Large Language Model (LLM) แบบมาตรฐาน มันสามารถรับรู้สภาพแวดล้อมของมัน ตัดสินใจ และดำเนินการเพื่อให้บรรลุเป้าหมายที่กำหนด ระบบหลายตัวแทนเกี่ยวข้องกับตัวแทนเหล่านี้หลายตัวที่ทำงานร่วมกันเพื่อแก้ปัญหาที่ยากหรือเป็นไปไม่ได้สำหรับตัวแทนเดียวที่จะจัดการได้เอง

### สถานการณ์การใช้งานทั่วไป

  * **การแก้ปัญหาที่ซับซ้อน**: แบ่งงานขนาดใหญ่ (เช่น การวางแผนกิจกรรมทั่วทั้งบริษัท) ออกเป็นงานย่อยเล็ก ๆ ที่ตัวแทนเฉพาะทางแต่ละตัวจัดการ (เช่น ตัวแทนงบประมาณ ตัวแทนโลจิสติกส์ ตัวแทนการตลาด)
  * **ผู้ช่วยเสมือน**: ตัวแทนผู้ช่วยหลักที่มอบหมายงานเช่น การนัดหมาย การค้นคว้า และการจองให้กับตัวแทนเฉพาะทางอื่น ๆ
  * **การสร้างเนื้อหาอัตโนมัติ**: workflow ที่ตัวแทนหนึ่งร่างเนื้อหา ตัวแทนอีกรับผิดชอบตรวจสอบความถูกต้องและโทนเสียง และตัวแทนที่สามเผยแพร่เนื้อหา

### รูปแบบหลายตัวแทน

ระบบหลายตัวแทนสามารถจัดระเบียบในหลายรูปแบบ ซึ่งกำหนดวิธีที่พวกมันโต้ตอบกัน:

  * **แบบลำดับ**: ตัวแทนทำงานตามลำดับที่กำหนดไว้ เช่น สายประกอบ ผลลัพธ์ของตัวแทนหนึ่งกลายเป็นอินพุตของตัวถัดไป
  * **แบบพร้อมกัน**: ตัวแทนทำงานขนานกันในส่วนต่าง ๆ ของงาน และรวบรวมผลลัพธ์เมื่อสิ้นสุด
  * **แบบมีเงื่อนไข**: workflow เดินตามเส้นทางต่าง ๆ ขึ้นอยู่กับผลลัพธ์ของตัวแทน คล้ายกับคำสั่ง if-then-else

## 2\. สถาปัตยกรรม Workflow ของ Microsoft Agent Framework

ระบบ workflow ของ Agent Framework เป็นเอนจินออร์เคสตราชั้นสูงที่ออกแบบมาเพื่อจัดการปฏิสัมพันธ์ซับซ้อนระหว่างตัวแทนหลายตัว มันถูกสร้างบนสถาปัตยกรรมแบบกราฟโดยใช้ [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf) ซึ่งการประมวลผลเกิดขึ้นในขั้นตอนที่ซิงโครไนซ์เรียกว่า "supersteps"

### ส่วนประกอบหลัก

สถาปัตยกรรมประกอบด้วยสามส่วนหลัก:

1.  **Executors**: เป็นหน่วยประมวลผลพื้นฐาน ในตัวอย่างของเรา `Agent` เป็นประเภทของ executor แต่ละ executor สามารถมีตัวจัดการข้อความหลายตัวที่ถูกเรียกโดยอัตโนมัติตามประเภทของข้อความที่ได้รับ
2.  **Edges**: กำหนดเส้นทางที่ข้อความเดินทางระหว่าง executors ขอบเขตสามารถมีเงื่อนไข เพื่อให้การเดินทางข้อมูลผ่านกราฟ workflow เป็นแบบไดนามิก
3.  **Workflow**: ส่วนประกอบนี้ออร์เคสตราทั้งหมด จัดการ executors, edges และลำดับการทำงานโดยรวม มันรับประกันว่าข้อความถูกประมวลผลตามลำดับที่ถูกต้องและส่งเหตุการณ์สำหรับการสังเกตการณ์

*แผนภาพแสดงส่วนประกอบหลักของระบบ workflow*

โครงสร้างนี้ช่วยให้สร้างแอปพลิเคชันที่ทนทานและขยายตัวได้โดยใช้รูปแบบพื้นฐาน เช่น โซ่ลำดับ ฟัน-ออก/ฟัน-อิน สำหรับประมวลผลคู่ขนาน และตรรกะสวิตช์-เคสสำหรับการไหลแบบมีเงื่อนไข

## 3\. ตัวอย่างใช้งานจริงและการวิเคราะห์โค้ด

ตอนนี้ เรามาสำรวจวิธีการใช้งานรูปแบบ workflow ที่แตกต่างกันโดยใช้เฟรมเวิร์กนี้ เราจะดูโค้ดทั้งใน Python และ .NET สำหรับแต่ละตัวอย่าง

### กรณีที่ 1: Workflow ลำดับขั้นพื้นฐาน

นี่คือรูปแบบง่ายที่สุด โดยที่ผลลัพธ์ของตัวแทนหนึ่งจะถูกส่งต่อโดยตรงไปยังอีกตัว เรามีสถานการณ์กับตัวแทนโรงแรม `FrontDesk` ที่แนะนำการเดินทาง ซึ่งจะถูกตรวจสอบโดยตัวแทน `Concierge`

*แผนภาพ Workflow แบบพื้นฐานระหว่าง FrontDesk -> Concierge*

#### ภูมิหลังสถานการณ์

นักเดินทางขอคำแนะนำในปารีส

1.  ตัวแทน `FrontDesk` ซึ่งถูกออกแบบให้สั้นกระชับ แนะนำให้ไปเยือนพิพิธภัณฑ์ลูฟวร์
2.  ตัวแทน `Concierge` ที่เน้นประสบการณ์แท้จริงได้รับคำแนะนำนี้ ตรวจสอบคำแนะนำและให้ข้อเสนอแนะโดยแนะนำทางเลือกที่เป็นท้องถิ่นมากกว่าและไม่ใช่แหล่งท่องเที่ยวหลัก

#### การวิเคราะห์การใช้งานใน Python

ในตัวอย่าง Python เราจะกำหนดและสร้างตัวแทนสองตัวแรก โดยแต่ละตัวมีคำสั่งเฉพาะตัว

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# กำหนดบทบาทและคำแนะนำของตัวแทน
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# สร้างอินสแตนซ์ของตัวแทน
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

จากนั้น `WorkflowBuilder` ถูกใช้สร้างกราฟ กำหนด `front_desk_agent` เป็นจุดเริ่มต้น และสร้าง edge เชื่อมผลลัพธ์ของมันไปยัง `reviewer_agent`

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

สุดท้าย รัน workflow โดยใช้อินพุตข้อความเริ่มต้นจากผู้ใช้

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run ดำเนินการตาม workflow; get_outputs() ส่งคืนผลลัพธ์ของตัวประมวลผลผลลัพธ์.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### การวิเคราะห์การใช้งานใน .NET (C#)

การใช้งานใน .NET ใช้ตรรกะที่คล้ายกันมาก กำหนดค่าคงที่สำหรับชื่อและคำสั่งของตัวแทนก่อน

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

สร้างตัวแทนด้วย `AzureOpenAIClient` (Responses API) แล้ว `WorkflowBuilder` กำหนดลำดับโดยเพิ่ม edge จาก `frontDeskAgent` ไปยัง `reviewerAgent`

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

จากนั้นรัน workflow ด้วยข้อความของผู้ใช้ และสตรีมผลลัพธ์กลับ

### กรณีที่ 2: Workflow ลำดับหลายขั้นตอน

รูปแบบนี้ขยายโซ่ลำดับขั้นพื้นฐานให้มีตัวแทนมากขึ้น เหมาะสำหรับกระบวนการที่ต้องการหลายขั้นตอนของการปรับแต่งหรือแปลงข้อมูล

#### ภูมิหลังสถานการณ์

ผู้ใช้ส่งภาพห้องนั่งเล่นและขอใบเสนอราคาสำหรับเฟอร์นิเจอร์

1.  **Sales-Agent**: ระบุรายการเฟอร์นิเจอร์ในภาพและสร้างรายการ
2.  **Price-Agent**: รับรายการเฟอร์นิเจอร์และให้รายละเอียดราคาที่แตกต่าง เช่น งบประมาณ ห้องกลาง และพรีเมียม
3.  **Quote-Agent**: รับรายการที่มีราคาและจัดรูปแบบเป็นเอกสารใบเสนอราคาอย่างเป็นทางการในรูปแบบ Markdown

*แผนภาพ Workflow Sales -> Price -> Quote*

#### การวิเคราะห์การใช้งานใน Python

กำหนดตัวแทนสามตัวโดยแต่ละตัวมีบทบาทเฉพาะเจาะจง สร้าง workflow โดยใช้ `add_edge` ต่อโซ่: `sales_agent` -> `price_agent` -> `quote_agent`

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# สร้างตัวแทนเฉพาะสามตัว
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# สร้างเวิร์กโฟลว์แบบเรียงลำดับ
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

อินพุตคืข้อความ `ChatMessage` ที่รวมทั้งข้อความและแหล่งที่อยู่รูปภาพ เฟรมเวิร์กจะจัดการส่งผลลัพธ์ของแต่ละตัวแทนไปยังตัวถัดไปตามลำดับจนกระทั่งใบเสนอราคาสุดท้ายถูกสร้าง

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# ข้อความของผู้ใช้ประกอบด้วยทั้งข้อความและภาพ
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# เรียกใช้โฟลว์เวิร์ก
events = await workflow.run(message)
```

#### การวิเคราะห์การใช้งานใน .NET (C#)

ตัวอย่างใน .NET สะท้อนเวอร์ชั่น Python โดยสร้างตัวแทนสามตัว (`salesagent`, `priceagent`, `quoteagent`) และ `WorkflowBuilder` เชื่อมต่อพวกเขาแบบลำดับ

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

ข้อความของผู้ใช้ถูกสร้างด้วยข้อมูลภาพ (ในรูปแบบไบต์) และข้อความคำสั่ง Method `InProcessExecution.RunStreamingAsync` เริ่ม workflow และจับผลลัพธ์สุดท้ายจากสตรีม

### กรณีที่ 3: Workflow พร้อมกัน

รูปแบบนี้ใช้เมื่อภารกิจสามารถทำงานพร้อมกันเพื่อประหยัดเวลา มีการ "fan-out" ไปยังตัวแทนหลายตัวและ "fan-in" เพื่อรวบรวมผลลัพธ์

#### ภูมิหลังสถานการณ์

ผู้ใช้ขอวางแผนการเดินทางไปซีแอตเทิล

1.  **Dispatcher (Fan-Out)**: ส่งคำขอผู้ใช้ไปยังตัวแทนสองตัวพร้อมกัน
2.  **Researcher-Agent**: ศึกษาสถานที่ท่องเที่ยว สภาพอากาศ และพิจารณาสำคัญสำหรับการเดินทางซีแอตเทิลในเดือนธันวาคม
3.  **Plan-Agent**: สร้างแผนการเดินทางอย่างละเอียดวันต่อวันอย่างอิสระ
4.  **Aggregator (Fan-In)**: รวบรวมผลลัพธ์จากทั้งนักวิจัยและผู้วางแผนและนำเสนอเป็นผลลัพธ์สุดท้าย

*แผนภาพ Workflow พร้อมกันระหว่างนักวิจัยและผู้วางแผน*

#### การวิเคราะห์การใช้งานใน Python

`ConcurrentBuilder` ช่วยให้สร้างรูปแบบนี้ง่ายขึ้น เพียงแค่ระบุตัวแทนที่เข้าร่วม แล้วบิวเดอร์จะสร้างฟัน-เอาต์และฟัน-อินให้โดยอัตโนมัติ

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder จัดการตรรกะ fan-out/fan-in
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# เรียกใช้ workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

เฟรมเวิร์กรับประกันว่า `research_agent` และ `plan_agent` จะทำงานคู่ขนาน และรวบรวมผลลัพธ์สุดท้ายเป็นรายการ

#### การวิเคราะห์การใช้งานใน .NET (C#)

ใน .NET รูปแบบนี้ต้องการการกำหนดที่ชัดเจนมากขึ้น สร้าง custom executors (`ConcurrentStartExecutor` และ `ConcurrentAggregationExecutor`) เพื่อจัดการฟัน-เอาต์และฟัน-อิน

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

`WorkflowBuilder` ใช้ `AddFanOutEdge` และ `AddFanInEdge` เพื่อสร้างกราฟพร้อม executors แบบกำหนดเองและตัวแทน

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### กรณีที่ 4: Workflow แบบมีเงื่อนไข

Workflow แบบมีเงื่อนไขเพิ่มตรรกะการแยกสาขา ทำให้ระบบเดินตามทางเลือกที่ต่างกันตามผลลัพธ์ระหว่างทาง

#### ภูมิหลังสถานการณ์

Workflow นี้อัตโนมัติการสร้างและเผยแพร่บทช่วยสอนทางเทคนิค

1.  **Evangelist-Agent**: เขียนร่างบทช่วยสอนจากโครงร่างและ URL ที่กำหนด
2.  **ContentReviewer-Agent**: ตรวจสอบร่าง โดยเช็คว่าคำเกิน 200 คำหรือไม่
3.  **สาขาแบบมีเงื่อนไข**:
      * **ถ้าอนุมัติ (`Yes`)**: workflow ดำเนินการต่อไปที่ `Publisher-Agent`
      * **ถ้าไม่อนุมัติ (`No`)**: workflow หยุดและแสดงเหตุผลการปฏิเสธ
4.  **Publisher-Agent**: หากร่างได้รับการอนุมัติ ตัวแทนนี้บันทึกเนื้อหาเป็นไฟล์ Markdown

#### การวิเคราะห์การใช้งานใน Python

ตัวอย่างนี้ใช้ฟังก์ชันกำหนดเอง `select_targets` เพื่อใช้งานตรรกะเงื่อนไข ฟังก์ชันนี้ถูกส่งให้กับ `add_multi_selection_edge_group` เพื่อกำหนด workflow ตามฟิลด์ `review_result` จากผลของผู้ตรวจสอบ

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# ฟังก์ชันนี้กำหนดขั้นตอนถัดไปตามผลการตรวจสอบ
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # หากอนุมัติ ให้ดำเนินการต่อที่ตัวจัดการ 'save_draft'
        return [save_draft_id]
    else:
        # หากถูกปฏิเสธ ให้ดำเนินการต่อที่ตัวจัดการ 'handle_review' เพื่อรายงานความล้มเหลว
        return [handle_review_id]

# ตัวสร้าง workflow ใช้ฟังก์ชันการเลือกสำหรับเส้นทาง
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # ขอบหลายตัวเลือกใช้ตรรกะเงื่อนไขในการดำเนินการ
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

ใช้ custom executors อย่าง `to_reviewer_result` เพื่อแปลงผล JSON จากตัวแทนเป็นอ็อบเจ็กต์ที่มีชนิดแน่นอนซึ่งฟังก์ชันเลือกสามารถตรวจสอบได้

#### การวิเคราะห์การใช้งานใน .NET (C#)

เวอร์ชัน .NET ใช้วิธีคล้ายกันกับฟังก์ชันเงื่อนไข กำหนด `Func<object?, bool>` เพื่อตรวจสอบสมบัติ `Result` ของอ็อบเจ็กต์ `ReviewResult`

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

พารามิเตอร์ `condition` ของเมธอด `AddEdge` อนุญาตให้ `WorkflowBuilder` สร้างเส้นทางแยก สายงานจะเดินตาม edge ไปยัง `publishExecutor` ก็ต่อเมื่อเงื่อนไข `GetCondition(expectedResult: "Yes")` คืนค่า true มิฉะนั้นจะไปเส้นทาง `sendReviewerExecutor`

## สรุป

Microsoft Agent Framework Workflow มอบพื้นฐานที่แข็งแกร่งและยืดหยุ่นสำหรับการออร์เคสตราระบบหลายตัวแทนที่ซับซ้อน ด้วยการใช้สถาปัตยกรรมแบบกราฟและส่วนประกอบหลัก นักพัฒนาสามารถออกแบบและสร้าง workflow ที่ซับซ้อนในทั้ง Python และ .NET ไม่ว่าจะเป็นการประมวลผลแบบลำดับง่าย ๆ การทำงานพร้อมกัน หรือตรรกะเงื่อนไขแบบไดนามิก เฟรมเวิร์กก็มีเครื่องมือที่จะสร้างโซลูชัน AI ที่ทรงพลัง ขยายตัวได้ และปลอดภัยด้วยชนิดข้อมูล

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->