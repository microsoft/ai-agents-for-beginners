# การสร้างแอปพลิเคชันหลายตัวแทนด้วย Microsoft Agent Framework Workflow

บทเรียนนี้จะช่วยให้คุณเข้าใจและสร้างแอปพลิเคชันหลายตัวแทนโดยใช้ Microsoft Agent Framework เราจะสำรวจแนวคิดหลักของระบบหลายตัวแทน เจาะลึกสถาปัตยกรรมของส่วน Workflow ในเฟรมเวิร์ก และดูตัวอย่างการใช้งานจริงใน Python และ .NET สำหรับรูปแบบ Workflow ต่างๆ

## 1\. การทำความเข้าใจระบบหลายตัวแทน

AI Agent คือระบบที่มีความสามารถเกินกว่าระบบ Large Language Model (LLM) ทั่วไป มันสามารถรับรู้สภาพแวดล้อม ตัดสินใจ และดำเนินการเพื่อบรรลุเป้าหมายเฉพาะ ระบบหลายตัวแทนเกี่ยวข้องกับตัวแทนหลายตัวที่ทำงานร่วมกันเพื่อแก้ปัญหาที่ตัวแทนตัวเดียวอาจไม่สามารถจัดการได้

### สถานการณ์การใช้งานทั่วไป

  * **การแก้ปัญหาที่ซับซ้อน**: การแบ่งงานขนาดใหญ่ (เช่น การวางแผนงานระดับบริษัท) ออกเป็นงานย่อยที่จัดการโดยตัวแทนเฉพาะทาง (เช่น ตัวแทนงบประมาณ ตัวแทนโลจิสติกส์ ตัวแทนการตลาด)
  * **ผู้ช่วยเสมือน**: ตัวแทนผู้ช่วยหลักที่มอบหมายงาน เช่น การจัดตาราง การค้นคว้า และการจอง ให้กับตัวแทนเฉพาะทางอื่นๆ
  * **การสร้างเนื้อหาอัตโนมัติ**: Workflow ที่ตัวแทนหนึ่งร่างเนื้อหา ตัวแทนอีกตัวตรวจสอบความถูกต้องและโทนเสียง และตัวแทนที่สามเผยแพร่เนื้อหา

### รูปแบบระบบหลายตัวแทน

ระบบหลายตัวแทนสามารถจัดระเบียบในรูปแบบต่างๆ ซึ่งกำหนดวิธีการที่พวกเขาโต้ตอบกัน:

  * **แบบลำดับ**: ตัวแทนทำงานตามลำดับที่กำหนดไว้ เช่น สายการผลิต ผลลัพธ์ของตัวแทนหนึ่งจะกลายเป็นข้อมูลนำเข้าของตัวแทนถัดไป
  * **แบบคู่ขนาน**: ตัวแทนทำงานพร้อมกันในส่วนต่างๆ ของงาน และผลลัพธ์จะถูกรวมกันในตอนท้าย
  * **แบบมีเงื่อนไข**: Workflow จะดำเนินไปตามเส้นทางต่างๆ ตามผลลัพธ์ของตัวแทน คล้ายกับคำสั่ง if-then-else

## 2\. สถาปัตยกรรม Workflow ของ Microsoft Agent Framework

ระบบ Workflow ของ Agent Framework เป็นเครื่องมือจัดการขั้นสูงที่ออกแบบมาเพื่อจัดการการโต้ตอบที่ซับซ้อนระหว่างตัวแทนหลายตัว มันถูกสร้างขึ้นบนสถาปัตยกรรมแบบกราฟที่ใช้ [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf) ซึ่งการประมวลผลเกิดขึ้นในขั้นตอนที่ซิงโครไนซ์เรียกว่า "supersteps"

### ส่วนประกอบหลัก

สถาปัตยกรรมประกอบด้วยสามส่วนหลัก:

1.  **Executors**: หน่วยประมวลผลพื้นฐาน ในตัวอย่างของเรา `Agent` เป็นประเภทของ executor แต่ละ executor สามารถมีตัวจัดการข้อความหลายตัวที่ถูกเรียกใช้อัตโนมัติตามประเภทของข้อความที่ได้รับ
2.  **Edges**: กำหนดเส้นทางที่ข้อความเดินทางระหว่าง executors Edges สามารถมีเงื่อนไข ทำให้สามารถกำหนดเส้นทางข้อมูลแบบไดนามิกผ่านกราฟ Workflow
3.  **Workflow**: ส่วนนี้จัดการกระบวนการทั้งหมด ดูแล executors, edges และการไหลของการดำเนินการโดยรวม มันรับรองว่าข้อความถูกประมวลผลตามลำดับที่ถูกต้องและสตรีมเหตุการณ์เพื่อการสังเกตการณ์

*แผนภาพแสดงส่วนประกอบหลักของระบบ Workflow*

โครงสร้างนี้ช่วยให้สามารถสร้างแอปพลิเคชันที่แข็งแกร่งและขยายได้โดยใช้รูปแบบพื้นฐาน เช่น การเชื่อมโยงแบบลำดับ การประมวลผลแบบคู่ขนาน และตรรกะแบบ switch-case สำหรับการไหลแบบมีเงื่อนไข

## 3\. ตัวอย่างการใช้งานจริงและการวิเคราะห์โค้ด

ตอนนี้เรามาดูวิธีการใช้งานรูปแบบ Workflow ต่างๆ โดยใช้เฟรมเวิร์ก เราจะดูโค้ดทั้งใน Python และ .NET สำหรับแต่ละตัวอย่าง

### กรณีที่ 1: Workflow แบบลำดับพื้นฐาน

นี่เป็นรูปแบบที่ง่ายที่สุด ซึ่งผลลัพธ์ของตัวแทนหนึ่งจะถูกส่งต่อไปยังตัวแทนถัดไปโดยตรง สถานการณ์ของเราคือ `FrontDesk` ตัวแทนโรงแรมที่แนะนำการเดินทาง ซึ่งจะถูกตรวจสอบโดย `Concierge` ตัวแทน

*แผนภาพของ Workflow FrontDesk -> Concierge แบบพื้นฐาน*

#### ภูมิหลังของสถานการณ์

นักเดินทางขอคำแนะนำในปารีส

1.  ตัวแทน `FrontDesk` ซึ่งออกแบบมาให้ตอบสั้นๆ แนะนำให้ไปเยี่ยมชมพิพิธภัณฑ์ลูฟวร์
2.  ตัวแทน `Concierge` ซึ่งให้ความสำคัญกับประสบการณ์ที่แท้จริง รับคำแนะนำนี้และตรวจสอบ โดยแนะนำทางเลือกที่เป็นท้องถิ่นและไม่ใช่แหล่งท่องเที่ยวมากนัก

#### การวิเคราะห์การใช้งานใน Python

ในตัวอย่าง Python เราเริ่มต้นด้วยการกำหนดและสร้างตัวแทนสองตัว แต่ละตัวมีคำแนะนำเฉพาะ

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

จากนั้นใช้ `WorkflowBuilder` เพื่อสร้างกราฟ โดยตั้งค่า `front_desk_agent` เป็นจุดเริ่มต้น และสร้าง edge เพื่อเชื่อมต่อผลลัพธ์ของมันกับ `reviewer_agent`

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

สุดท้าย Workflow จะถูกดำเนินการด้วยคำถามเริ่มต้นของผู้ใช้

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### การวิเคราะห์การใช้งานใน .NET (C#)

การใช้งานใน .NET มีตรรกะที่คล้ายกันมาก เริ่มต้นด้วยการกำหนดค่าคงที่สำหรับชื่อและคำแนะนำของตัวแทน

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

ตัวแทนถูกสร้างขึ้นโดยใช้ `OpenAIClient` จากนั้น `WorkflowBuilder` กำหนดการไหลแบบลำดับโดยเพิ่ม edge จาก `frontDeskAgent` ไปยัง `reviewerAgent`

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Workflow จะถูกดำเนินการด้วยข้อความของผู้ใช้ และผลลัพธ์จะถูกสตรีมกลับมา

### กรณีที่ 2: Workflow แบบลำดับหลายขั้นตอน

รูปแบบนี้ขยายลำดับพื้นฐานเพื่อรวมตัวแทนเพิ่มเติม เหมาะสำหรับกระบวนการที่ต้องการการปรับปรุงหรือการแปลงหลายขั้นตอน

#### ภูมิหลังของสถานการณ์

ผู้ใช้ให้ภาพห้องนั่งเล่นและขอใบเสนอราคาสำหรับเฟอร์นิเจอร์

1.  **Sales-Agent**: ระบุรายการเฟอร์นิเจอร์ในภาพและสร้างรายการ
2.  **Price-Agent**: ใช้รายการเฟอร์นิเจอร์และให้รายละเอียดราคาสำหรับตัวเลือกงบประมาณ ระดับกลาง และระดับพรีเมียม
3.  **Quote-Agent**: รับรายการราคาที่จัดทำและจัดรูปแบบเป็นเอกสารใบเสนอราคาใน Markdown

*แผนภาพของ Workflow Sales -> Price -> Quote*

#### การวิเคราะห์การใช้งานใน Python

ตัวแทนสามตัวถูกกำหนด แต่ละตัวมีบทบาทเฉพาะ Workflow ถูกสร้างขึ้นโดยใช้ `add_edge` เพื่อสร้างลำดับ: `sales_agent` -> `price_agent` -> `quote_agent`

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ข้อมูลนำเข้าเป็น `ChatMessage` ที่รวมข้อความและ URI ของภาพ Framework จะจัดการการส่งผลลัพธ์ของแต่ละตัวแทนไปยังตัวแทนถัดไปในลำดับจนกระทั่งใบเสนอราคาสุดท้ายถูกสร้างขึ้น

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# The user message contains both text and an image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Run the workflow
async for event in workflow.run_stream(message):
    ...
```

#### การวิเคราะห์การใช้งานใน .NET (C#)

ตัวอย่างใน .NET สะท้อนเวอร์ชัน Python ตัวแทนสามตัว (`salesagent`, `priceagent`, `quoteagent`) ถูกสร้างขึ้น `WorkflowBuilder` เชื่อมโยงพวกเขาในลำดับ

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

ข้อความของผู้ใช้ถูกสร้างขึ้นพร้อมข้อมูลภาพ (ในรูปแบบ bytes) และข้อความ Framework ใช้ `InProcessExecution.StreamAsync` เพื่อเริ่ม Workflow และผลลัพธ์สุดท้ายจะถูกจับจาก stream

### กรณีที่ 3: Workflow แบบคู่ขนาน

รูปแบบนี้ใช้เมื่อสามารถดำเนินงานพร้อมกันเพื่อประหยัดเวลา มันเกี่ยวข้องกับ "fan-out" ไปยังตัวแทนหลายตัวและ "fan-in" เพื่อรวบรวมผลลัพธ์

#### ภูมิหลังของสถานการณ์

ผู้ใช้ขอให้วางแผนการเดินทางไปซีแอตเทิล

1.  **Dispatcher (Fan-Out)**: คำขอของผู้ใช้ถูกส่งไปยังตัวแทนสองตัวพร้อมกัน
2.  **Researcher-Agent**: ค้นคว้าสถานที่ท่องเที่ยว สภาพอากาศ และข้อควรพิจารณาสำคัญสำหรับการเดินทางไปซีแอตเทิลในเดือนธันวาคม
3.  **Plan-Agent**: สร้างแผนการเดินทางแบบวันต่อวันอย่างละเอียดโดยอิสระ
4.  **Aggregator (Fan-In)**: ผลลัพธ์จากทั้ง researcher และ planner จะถูกรวบรวมและนำเสนอเป็นผลลัพธ์สุดท้าย

*แผนภาพของ Workflow Researcher และ Planner แบบคู่ขนาน*

#### การวิเคราะห์การใช้งานใน Python

`ConcurrentBuilder` ช่วยให้การสร้างรูปแบบนี้ง่ายขึ้น เพียงแค่ระบุรายชื่อตัวแทนที่เข้าร่วม และ builder จะสร้างตรรกะ fan-out และ fan-in โดยอัตโนมัติ

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework รับรองว่า `research_agent` และ `plan_agent` ดำเนินการพร้อมกัน และผลลัพธ์สุดท้ายจะถูกรวบรวมเป็นรายการ

#### การวิเคราะห์การใช้งานใน .NET (C#)

ใน .NET รูปแบบนี้ต้องการการกำหนดที่ชัดเจนมากขึ้น Executors แบบกำหนดเอง (`ConcurrentStartExecutor` และ `ConcurrentAggregationExecutor`) ถูกสร้างขึ้นเพื่อจัดการตรรกะ fan-out และ fan-in

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

`WorkflowBuilder` ใช้ `AddFanOutEdge` และ `AddFanInEdge` เพื่อสร้างกราฟด้วย executors แบบกำหนดเองและตัวแทน

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### กรณีที่ 4: Workflow แบบมีเงื่อนไข

Workflow แบบมีเงื่อนไขแนะนำตรรกะแบบ branching logic ทำให้ระบบสามารถดำเนินไปตามเส้นทางต่างๆ ตามผลลัพธ์ระหว่างทาง

#### ภูมิหลังของสถานการณ์

Workflow นี้ทำให้การสร้างและเผยแพร่บทเรียนทางเทคนิคเป็นอัตโนมัติ

1.  **Evangelist-Agent**: เขียนร่างบทเรียนตามโครงร่างและ URL ที่ให้มา
2.  **ContentReviewer-Agent**: ตรวจสอบร่าง ตรวจสอบว่าจำนวนคำเกิน 200 คำหรือไม่
3.  **เงื่อนไข**:
      * **ถ้าอนุมัติ (`Yes`)**: Workflow ดำเนินต่อไปยัง `Publisher-Agent`
      * **ถ้าปฏิเสธ (`No`)**: Workflow หยุดและแสดงเหตุผลของการปฏิเสธ
4.  **Publisher-Agent**: หากร่างได้รับการอนุมัติ ตัวแทนนี้จะบันทึกเนื้อหาเป็นไฟล์ Markdown

#### การวิเคราะห์การใช้งานใน Python

ตัวอย่างนี้ใช้ฟังก์ชันกำหนดเอง `select_targets` เพื่อใช้งานตรรกะแบบมีเงื่อนไข ฟังก์ชันนี้ถูกส่งไปยัง `add_multi_selection_edge_group` และกำหนด Workflow ตามฟิลด์ `review_result` จากผลลัพธ์ของ reviewer

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# This function determines the next step based on the review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If approved, proceed to the 'save_draft' executor
        return [save_draft_id]
    else:
        # If rejected, proceed to the 'handle_review' executor to report failure
        return [handle_review_id]

# The workflow builder uses the selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # The multi-selection edge implements the conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Executors แบบกำหนดเอง เช่น `to_reviewer_result` ถูกใช้เพื่อแปลง JSON output จากตัวแทนให้เป็นออบเจ็กต์ที่มีประเภทชัดเจนซึ่งฟังก์ชัน selection สามารถตรวจสอบได้

#### การวิเคราะห์การใช้งานใน .NET (C#)

เวอร์ชัน .NET ใช้แนวทางที่คล้ายกันโดยมีฟังก์ชันเงื่อนไข `Func<object?, bool>` ที่กำหนดเพื่อตรวจสอบคุณสมบัติ `Result` ของออบเจ็กต์ `ReviewResult`

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

พารามิเตอร์ `condition` ของเมธอด `AddEdge` ช่วยให้ `WorkflowBuilder` สร้างเส้นทาง branching Workflow จะตาม edge ไปยัง `publishExecutor` ก็ต่อเมื่อเงื่อนไข `GetCondition(expectedResult: "Yes")` คืนค่า true มิฉะนั้นจะตามเส้นทางไปยัง `sendReviewerExecutor`

## สรุป

Microsoft Agent Framework Workflow ให้พื้นฐานที่แข็งแกร่งและยืดหยุ่นสำหรับการจัดการระบบหลายตัวแทนที่ซับซ้อน ด้วยการใช้สถาปัตยกรรมแบบกราฟและส่วนประกอบหลัก นักพัฒนาสามารถออกแบบและใช้งาน Workflow ที่ซับซ้อนใน Python และ .NET ไม่ว่าคุณจะต้องการการประมวลผลแบบลำดับง่ายๆ การดำเนินการแบบคู่ขนาน หรือตรรกะแบบมีเงื่อนไข Framework นี้มีเครื่องมือที่ช่วยสร้างโซลูชัน AI ที่ทรงพลัง ขยายได้ และปลอดภัย

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้