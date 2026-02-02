# Xây dựng ứng dụng đa tác nhân với Microsoft Agent Framework Workflow

Hướng dẫn này sẽ giúp bạn hiểu và xây dựng các ứng dụng đa tác nhân bằng Microsoft Agent Framework. Chúng ta sẽ khám phá các khái niệm cốt lõi của hệ thống đa tác nhân, đi sâu vào kiến trúc của thành phần Workflow trong framework, và thực hiện các ví dụ thực tế bằng Python và .NET cho các mẫu workflow khác nhau.

## 1\. Hiểu về hệ thống đa tác nhân

Một AI Agent là một hệ thống vượt xa khả năng của một Mô hình Ngôn ngữ Lớn (LLM) thông thường. Nó có thể nhận thức môi trường, đưa ra quyết định và thực hiện hành động để đạt được các mục tiêu cụ thể. Hệ thống đa tác nhân bao gồm nhiều tác nhân hợp tác để giải quyết một vấn đề mà một tác nhân đơn lẻ khó hoặc không thể xử lý được.

### Các kịch bản ứng dụng phổ biến

  * **Giải quyết vấn đề phức tạp**: Phân chia một nhiệm vụ lớn (ví dụ: lập kế hoạch cho một sự kiện toàn công ty) thành các nhiệm vụ nhỏ hơn được xử lý bởi các tác nhân chuyên biệt (ví dụ: tác nhân ngân sách, tác nhân hậu cần, tác nhân tiếp thị).
  * **Trợ lý ảo**: Một tác nhân trợ lý chính phân công các nhiệm vụ như lên lịch, nghiên cứu, và đặt chỗ cho các tác nhân chuyên biệt khác.
  * **Tạo nội dung tự động**: Một workflow nơi một tác nhân soạn thảo nội dung, một tác nhân khác kiểm tra độ chính xác và giọng điệu, và một tác nhân thứ ba xuất bản nội dung.

### Các mẫu đa tác nhân

Hệ thống đa tác nhân có thể được tổ chức theo nhiều mẫu khác nhau, xác định cách chúng tương tác:

  * **Tuần tự**: Các tác nhân làm việc theo thứ tự định trước, giống như dây chuyền sản xuất. Đầu ra của một tác nhân trở thành đầu vào cho tác nhân tiếp theo.
  * **Song song**: Các tác nhân làm việc đồng thời trên các phần khác nhau của một nhiệm vụ, và kết quả của chúng được tổng hợp lại ở cuối.
  * **Có điều kiện**: Workflow đi theo các đường khác nhau dựa trên đầu ra của một tác nhân, tương tự như câu lệnh if-then-else.

## 2\. Kiến trúc Workflow của Microsoft Agent Framework

Hệ thống workflow của Agent Framework là một công cụ điều phối tiên tiến được thiết kế để quản lý các tương tác phức tạp giữa nhiều tác nhân. Nó được xây dựng trên kiến trúc dựa trên đồ thị sử dụng [mô hình thực thi kiểu Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), nơi xử lý diễn ra trong các bước đồng bộ hóa gọi là "supersteps."

### Các thành phần cốt lõi

Kiến trúc bao gồm ba phần chính:

1.  **Executors**: Đây là các đơn vị xử lý cơ bản. Trong các ví dụ của chúng ta, một `Agent` là một loại executor. Mỗi executor có thể có nhiều trình xử lý thông điệp được tự động gọi dựa trên loại thông điệp nhận được.
2.  **Edges**: Các cạnh này xác định đường đi của thông điệp giữa các executors. Các cạnh có thể có điều kiện, cho phép định tuyến thông tin động qua đồ thị workflow.
3.  **Workflow**: Thành phần này điều phối toàn bộ quy trình, quản lý các executors, edges, và luồng thực thi tổng thể. Nó đảm bảo rằng các thông điệp được xử lý theo đúng thứ tự và phát luồng sự kiện để quan sát.

*Hình minh họa các thành phần cốt lõi của hệ thống workflow.*

Cấu trúc này cho phép xây dựng các ứng dụng mạnh mẽ và có khả năng mở rộng bằng cách sử dụng các mẫu cơ bản như chuỗi tuần tự, fan-out/fan-in để xử lý song song, và logic switch-case cho các luồng có điều kiện.

## 3\. Ví dụ thực tế và phân tích mã

Bây giờ, chúng ta sẽ khám phá cách triển khai các mẫu workflow khác nhau bằng framework. Chúng ta sẽ xem xét mã Python và .NET cho từng ví dụ.

### Trường hợp 1: Workflow tuần tự cơ bản

Đây là mẫu đơn giản nhất, nơi đầu ra của một tác nhân được chuyển trực tiếp cho tác nhân khác. Kịch bản của chúng ta liên quan đến một tác nhân `FrontDesk` của khách sạn đưa ra gợi ý du lịch, sau đó được một tác nhân `Concierge` xem xét.

*Hình minh họa workflow cơ bản FrontDesk -\> Concierge.*

#### Bối cảnh kịch bản

Một du khách yêu cầu gợi ý tại Paris.

1.  Tác nhân `FrontDesk`, được thiết kế để ngắn gọn, gợi ý thăm Bảo tàng Louvre.
2.  Tác nhân `Concierge`, ưu tiên trải nghiệm chân thực, nhận gợi ý này. Nó xem xét gợi ý và đưa ra phản hồi, đề xuất một lựa chọn địa phương, ít mang tính du lịch hơn.

#### Phân tích triển khai Python

Trong ví dụ Python, chúng ta đầu tiên định nghĩa và tạo hai tác nhân, mỗi tác nhân có hướng dẫn cụ thể.

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

Tiếp theo, `WorkflowBuilder` được sử dụng để xây dựng đồ thị. `front_desk_agent` được đặt làm điểm bắt đầu, và một cạnh được tạo để kết nối đầu ra của nó với `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Cuối cùng, workflow được thực thi với lời nhắc ban đầu của người dùng.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Phân tích triển khai .NET (C\#)

Triển khai .NET tuân theo logic rất tương tự. Đầu tiên, các hằng số được định nghĩa cho tên và hướng dẫn của các tác nhân.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Các tác nhân được tạo bằng `OpenAIClient`, sau đó `WorkflowBuilder` định nghĩa luồng tuần tự bằng cách thêm một cạnh từ `frontDeskAgent` đến `reviewerAgent`.

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

Workflow sau đó được chạy với thông điệp của người dùng, và kết quả được phát luồng trở lại.

### Trường hợp 2: Workflow tuần tự nhiều bước

Mẫu này mở rộng chuỗi cơ bản để bao gồm nhiều tác nhân hơn. Nó lý tưởng cho các quy trình yêu cầu nhiều giai đoạn tinh chỉnh hoặc chuyển đổi.

#### Bối cảnh kịch bản

Người dùng cung cấp một hình ảnh của phòng khách và yêu cầu báo giá nội thất.

1.  **Sales-Agent**: Xác định các món đồ nội thất trong hình ảnh và tạo danh sách.
2.  **Price-Agent**: Nhận danh sách các món đồ và cung cấp bảng giá chi tiết, bao gồm các tùy chọn ngân sách, trung bình, và cao cấp.
3.  **Quote-Agent**: Nhận danh sách đã định giá và định dạng nó thành tài liệu báo giá chính thức bằng Markdown.

*Hình minh họa workflow Sales -\> Price -\> Quote.*

#### Phân tích triển khai Python

Ba tác nhân được định nghĩa, mỗi tác nhân có vai trò chuyên biệt. Workflow được xây dựng bằng cách sử dụng `add_edge` để tạo chuỗi: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Đầu vào là một `ChatMessage` bao gồm cả văn bản và URI hình ảnh. Framework xử lý việc chuyển đầu ra của mỗi tác nhân cho tác nhân tiếp theo trong chuỗi cho đến khi báo giá cuối cùng được tạo.

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

#### Phân tích triển khai .NET (C\#)

Ví dụ .NET phản ánh phiên bản Python. Ba tác nhân (`salesagent`, `priceagent`, `quoteagent`) được tạo. `WorkflowBuilder` liên kết chúng theo tuần tự.

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

Thông điệp của người dùng được xây dựng với cả dữ liệu hình ảnh (dưới dạng byte) và lời nhắc văn bản. Phương thức `InProcessExecution.StreamAsync` khởi chạy workflow, và đầu ra cuối cùng được lấy từ luồng.

### Trường hợp 3: Workflow song song

Mẫu này được sử dụng khi các nhiệm vụ có thể được thực hiện đồng thời để tiết kiệm thời gian. Nó bao gồm một "fan-out" đến nhiều tác nhân và một "fan-in" để tổng hợp kết quả.

#### Bối cảnh kịch bản

Người dùng yêu cầu lập kế hoạch cho một chuyến đi đến Seattle.

1.  **Dispatcher (Fan-Out)**: Yêu cầu của người dùng được gửi đến hai tác nhân cùng lúc.
2.  **Researcher-Agent**: Nghiên cứu các điểm tham quan, thời tiết, và các lưu ý chính cho chuyến đi đến Seattle vào tháng 12.
3.  **Plan-Agent**: Độc lập tạo một lịch trình chi tiết từng ngày cho chuyến đi.
4.  **Aggregator (Fan-In)**: Các đầu ra từ cả nhà nghiên cứu và người lập kế hoạch được thu thập và trình bày cùng nhau dưới dạng kết quả cuối cùng.

*Hình minh họa workflow song song Researcher và Planner.*

#### Phân tích triển khai Python

`ConcurrentBuilder` đơn giản hóa việc tạo mẫu này. Bạn chỉ cần liệt kê các tác nhân tham gia, và builder tự động tạo logic fan-out và fan-in cần thiết.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework đảm bảo rằng `research_agent` và `plan_agent` thực thi song song, và các đầu ra cuối cùng của chúng được thu thập thành một danh sách.

#### Phân tích triển khai .NET (C\#)

Trong .NET, mẫu này yêu cầu định nghĩa rõ ràng hơn. Các executors tùy chỉnh (`ConcurrentStartExecutor` và `ConcurrentAggregationExecutor`) được tạo để xử lý logic fan-out và fan-in.

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

`WorkflowBuilder` sau đó sử dụng `AddFanOutEdge` và `AddFanInEdge` để xây dựng đồ thị với các executors tùy chỉnh và các tác nhân.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Trường hợp 4: Workflow có điều kiện

Workflow có điều kiện giới thiệu logic phân nhánh, cho phép hệ thống đi theo các đường khác nhau dựa trên kết quả trung gian.

#### Bối cảnh kịch bản

Workflow này tự động hóa việc tạo và xuất bản một hướng dẫn kỹ thuật.

1.  **Evangelist-Agent**: Viết bản nháp của hướng dẫn dựa trên một dàn ý và các URL được cung cấp.
2.  **ContentReviewer-Agent**: Xem xét bản nháp. Nó kiểm tra xem số lượng từ có vượt quá 200 từ hay không.
3.  **Nhánh có điều kiện**:
      * **Nếu được chấp thuận (`Yes`)**: Workflow tiếp tục đến `Publisher-Agent`.
      * **Nếu bị từ chối (`No`)**: Workflow dừng lại và xuất lý do từ chối.
4.  **Publisher-Agent**: Nếu bản nháp được chấp thuận, tác nhân này lưu nội dung vào một tệp Markdown.

#### Phân tích triển khai Python

Ví dụ này sử dụng một hàm tùy chỉnh, `select_targets`, để triển khai logic có điều kiện. Hàm này được truyền vào `add_multi_selection_edge_group` và định hướng workflow dựa trên trường `review_result` từ đầu ra của người xem xét.

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

Các executors tùy chỉnh như `to_reviewer_result` được sử dụng để phân tích đầu ra JSON từ các tác nhân và chuyển đổi nó thành các đối tượng có kiểu mạnh mà hàm lựa chọn có thể kiểm tra.

#### Phân tích triển khai .NET (C\#)

Phiên bản .NET sử dụng cách tiếp cận tương tự với một hàm điều kiện. Một `Func<object?, bool>` được định nghĩa để kiểm tra thuộc tính `Result` của đối tượng `ReviewResult`.

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

Tham số `condition` của phương thức `AddEdge` cho phép `WorkflowBuilder` tạo một đường phân nhánh. Workflow chỉ đi theo cạnh đến `publishExecutor` nếu điều kiện `GetCondition(expectedResult: "Yes")` trả về true. Nếu không, nó đi theo đường đến `sendReviewerExecutor`.

## Kết luận

Microsoft Agent Framework Workflow cung cấp một nền tảng mạnh mẽ và linh hoạt để điều phối các hệ thống đa tác nhân phức tạp. Bằng cách tận dụng kiến trúc dựa trên đồ thị và các thành phần cốt lõi của nó, các nhà phát triển có thể thiết kế và triển khai các workflow tinh vi bằng cả Python và .NET. Cho dù ứng dụng của bạn yêu cầu xử lý tuần tự đơn giản, thực thi song song, hay logic có điều kiện động, framework cung cấp các công cụ để xây dựng các giải pháp AI mạnh mẽ, có khả năng mở rộng và an toàn về kiểu dữ liệu.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.