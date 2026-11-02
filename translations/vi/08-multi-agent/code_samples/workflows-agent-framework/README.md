# Xây dựng Ứng dụng Đa Tác nhân với Quy trình Microsoft Agent Framework

Hướng dẫn này sẽ giúp bạn hiểu và xây dựng các ứng dụng đa tác nhân sử dụng Microsoft Agent Framework. Chúng ta sẽ khám phá các khái niệm cốt lõi của hệ thống đa tác nhân, đi sâu vào kiến trúc của thành phần Workflow của framework, và đi qua các ví dụ thực tế bằng cả Python và .NET cho các mẫu quy trình khác nhau.

## 1\. Hiểu Về Hệ Thống Đa Tác Nhân

Một Tác nhân AI là một hệ thống vượt ra ngoài khả năng của một Mô hình Ngôn ngữ Lớn (LLM) tiêu chuẩn. Nó có thể nhận thức môi trường, đưa ra quyết định và thực hiện hành động để đạt được các mục tiêu cụ thể. Hệ thống đa tác nhân bao gồm nhiều tác nhân hợp tác để giải quyết một vấn đề mà một tác nhân đơn lẻ khó hoặc không thể xử lý một mình.

### Các Tình Huống Ứng Dụng Phổ Biến

  * **Giải quyết vấn đề phức tạp**: Phân nhỏ một nhiệm vụ lớn (ví dụ, lên kế hoạch sự kiện toàn công ty) thành các nhiệm vụ phụ nhỏ do các tác nhân chuyên môn xử lý (ví dụ, tác nhân ngân sách, tác nhân logistics, tác nhân marketing).
  * **Trợ lý ảo**: Một tác nhân trợ lý chính phân công các nhiệm vụ như lên lịch, nghiên cứu và đặt chỗ cho các tác nhân chuyên biệt khác.
  * **Tạo nội dung tự động**: Một quy trình làm việc trong đó một tác nhân soạn thảo nội dung, tác nhân khác xem xét độ chính xác và giọng điệu, tác nhân thứ ba công bố nó.

### Các Mẫu Đa Tác Nhân

Hệ thống đa tác nhân có thể được tổ chức theo nhiều mẫu khác nhau, quyết định cách chúng tương tác:

  * **Tuần tự**: Các tác nhân làm việc theo thứ tự đã định trước, giống như dây chuyền lắp ráp. Đầu ra của tác nhân này trở thành đầu vào cho tác nhân tiếp theo.
  * **Đồng thời**: Các tác nhân làm việc song song trên các phần khác nhau của nhiệm vụ, và kết quả của chúng được tập hợp lại vào cuối.
  * **Có điều kiện**: Quy trình theo các nhánh khác nhau dựa trên đầu ra của một tác nhân, tương tự như câu lệnh if-then-else.

## 2\. Kiến Trúc Quy Trình Microsoft Agent Framework

Hệ thống quy trình của Agent Framework là một động cơ điều phối tiên tiến được thiết kế để quản lý các tương tác phức tạp giữa nhiều tác nhân. Nó được xây dựng trên kiến trúc dựa trên đồ thị sử dụng [mô hình thực thi kiểu Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), nơi xử lý diễn ra theo các bước đồng bộ gọi là "supersteps."

### Các Thành Phần Cốt Lõi

Kiến trúc bao gồm ba phần chính:

1.  **Executor**: Đây là đơn vị xử lý cơ bản. Trong các ví dụ của chúng ta, một `Agent` là một kiểu executor. Mỗi executor có thể có nhiều bộ xử lý tin nhắn được tự động gọi dựa trên loại tin nhắn nhận được.
2.  **Edges**: Định nghĩa đường đi mà tin nhắn đi qua giữa các executor. Edges có thể có điều kiện, cho phép phân luồng thông tin động qua đồ thị quy trình.
3.  **Workflow**: Thành phần này điều phối toàn bộ quá trình, quản lý các executor, edges và dòng thực thi tổng thể. Nó đảm bảo các tin nhắn được xử lý đúng thứ tự và phát luồng sự kiện để có thể quan sát.

*Một sơ đồ minh họa các thành phần cốt lõi của hệ thống quy trình.*

Cấu trúc này cho phép xây dựng các ứng dụng mạnh mẽ và mở rộng sử dụng các mẫu cơ bản như chuỗi tuần tự, fan-out/fan-in cho xử lý song song, và logic switch-case cho luồng điều kiện.

## 3\. Ví Dụ Thực Tế và Phân Tích Mã Nguồn

Bây giờ, hãy khám phá cách triển khai các mẫu quy trình khác nhau sử dụng framework. Chúng ta sẽ xem cả mã Python và .NET cho từng ví dụ.

### Trường hợp 1: Quy trình Tuần tự Cơ Bản

Đây là mẫu đơn giản nhất, nơi đầu ra của một tác nhân được chuyển trực tiếp cho tác nhân khác. Kịch bản của chúng ta liên quan đến tác nhân `FrontDesk` của khách sạn đưa ra khuyến nghị du lịch, sau đó được tác nhân `Concierge` xem xét.

*Sơ đồ quy trình FrontDesk -> Concierge cơ bản.*

#### Bối Cảnh Kịch Bản

Một khách du lịch hỏi về một đề xuất tại Paris.

1.  Tác nhân `FrontDesk`, được thiết kế ngắn gọn, gợi ý thăm Bảo tàng Louvre.
2.  Tác nhân `Concierge`, ưu tiên trải nghiệm chân thực, nhận đề xuất này. Nó xem xét và phản hồi, gợi ý một lựa chọn địa phương hơn, ít khách du lịch hơn.

#### Phân Tích Triển Khai Python

Trong ví dụ Python, chúng ta định nghĩa và tạo hai tác nhân, mỗi tác nhân có chỉ dẫn cụ thể.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Định nghĩa vai trò và hướng dẫn của đại lý
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Tạo các thể hiện đại lý
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Tiếp theo, `WorkflowBuilder` được dùng để xây dựng đồ thị. `front_desk_agent` được đặt làm điểm khởi đầu, và một cạnh được tạo để kết nối đầu ra của nó với `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Cuối cùng, quy trình được thực thi với lời nhắc ban đầu của người dùng.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run thực thi luồng công việc; get_outputs() trả về kết quả của executor đầu ra.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Phân Tích Triển Khai .NET (C#)

Triển khai .NET theo logic tương tự. Đầu tiên, định nghĩa hằng số cho tên và chỉ dẫn của các tác nhân.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Các tác nhân được tạo bằng `AzureOpenAIClient` (Responses API), sau đó `WorkflowBuilder` định nghĩa luồng tuần tự bằng cách thêm cạnh từ `frontDeskAgent` đến `reviewerAgent`.

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

Quy trình được chạy với tin nhắn của người dùng, và kết quả được phát luồng trả về.

### Trường hợp 2: Quy trình Tuần tự Nhiều Bước

Mẫu này mở rộng dãy tuần tự cơ bản bằng cách thêm nhiều tác nhân hơn. Nó phù hợp cho các quy trình cần nhiều giai đoạn tinh chỉnh hoặc chuyển đổi.

#### Bối Cảnh Kịch Bản

Người dùng cung cấp một hình ảnh phòng khách và hỏi báo giá nội thất.

1.  **Sales-Agent**: Xác định các món nội thất trong hình và tạo danh sách.
2.  **Price-Agent**: Nhận danh sách và cung cấp bảng giá chi tiết, bao gồm các tùy chọn ngân sách thấp, trung cấp và cao cấp.
3.  **Quote-Agent**: Nhận danh sách đã định giá và định dạng nó thành tài liệu báo giá chính thức bằng Markdown.

*Sơ đồ quy trình Sales -> Price -> Quote.*

#### Phân Tích Triển Khai Python

Ba tác nhân được định nghĩa, mỗi tác nhân chuyên môn một vai trò. Quy trình được xây dựng bằng `add_edge` tạo thành chuỗi: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Tạo ba tác nhân chuyên biệt
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Xây dựng quy trình làm việc tuần tự
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Đầu vào là một `ChatMessage` bao gồm cả văn bản và URI hình ảnh. Framework xử lý việc chuyển đầu ra của từng tác nhân cho tác nhân tiếp theo trong chuỗi cho đến khi báo giá cuối cùng được tạo.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Tin nhắn người dùng chứa cả văn bản và hình ảnh
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Chạy luồng công việc
events = await workflow.run(message)
```

#### Phân Tích Triển Khai .NET (C#)

Ví dụ .NET tương tự phiên bản Python. Ba tác nhân (`salesagent`, `priceagent`, `quoteagent`) được tạo. `WorkflowBuilder` liên kết chúng theo chuỗi.

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

Tin nhắn người dùng được tạo với cả dữ liệu hình ảnh (dưới dạng bytes) và lời nhắc văn bản. Phương thức `InProcessExecution.RunStreamingAsync` khởi chạy quy trình, và đầu ra cuối cùng được lấy từ luồng.

### Trường hợp 3: Quy trình Đồng Thời

Mẫu này sử dụng khi các nhiệm vụ có thể được thực hiện đồng thời để tiết kiệm thời gian. Nó bao gồm một bước "fan-out" tới nhiều tác nhân và "fan-in" để tổng hợp kết quả.

#### Bối Cảnh Kịch Bản

Người dùng yêu cầu lên kế hoạch chuyến đi đến Seattle.

1.  **Dispatcher (Fan-Out)**: Yêu cầu của người dùng được gửi đến hai tác nhân cùng lúc.
2.  **Researcher-Agent**: Nghiên cứu các điểm tham quan, thời tiết và các cân nhắc chính cho chuyến đi tới Seattle vào tháng Mười Hai.
3.  **Plan-Agent**: Tự lập kế hoạch chi tiết từng ngày cho chuyến đi.
4.  **Aggregator (Fan-In)**: Thu thập và trình bày kết quả từ cả nhà nghiên cứu và nhà lập kế hoạch làm kết quả cuối cùng.

*Sơ đồ quy trình đồng thời của Nhà nghiên cứu và Nhà lập kế hoạch.*

#### Phân Tích Triển Khai Python

`ConcurrentBuilder` đơn giản hóa việc tạo mẫu này. Bạn chỉ cần liệt kê các tác nhân tham gia, và builder tự động tạo logic fan-out và fan-in cần thiết.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder xử lý logic phân nhánh và hợp nhất
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Chạy quy trình làm việc
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework đảm bảo rằng `research_agent` và `plan_agent` thực thi song song, và đầu ra cuối cùng của chúng được thu thập vào một danh sách.

#### Phân Tích Triển Khai .NET (C#)

Trong .NET, mẫu này cần phải định nghĩa rõ ràng hơn. Các executor tùy chỉnh (`ConcurrentStartExecutor` và `ConcurrentAggregationExecutor`) được tạo để xử lý logic fan-out và fan-in.

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

`WorkflowBuilder` sau đó sử dụng `AddFanOutEdge` và `AddFanInEdge` để xây dựng đồ thị với các executor tùy chỉnh và các tác nhân.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Trường hợp 4: Quy trình Có Điều Kiện

Quy trình có điều kiện đưa vào logic nhánh, cho phép hệ thống đi theo các đường khác nhau dựa trên kết quả trung gian.

#### Bối Cảnh Kịch Bản

Quy trình này tự động tạo và xuất bản một bài hướng dẫn kỹ thuật.

1.  **Evangelist-Agent**: Viết bản nháp hướng dẫn dựa trên dàn ý và URL được cung cấp.
2.  **ContentReviewer-Agent**: Xem xét bản nháp. Kiểm tra xem độ dài có trên 200 từ hay không.
3.  **Nhánh Có Điều Kiện**:
      * **Nếu được chấp thuận (`Yes`)**: Quy trình tiếp tục tới `Publisher-Agent`.
      * **Nếu bị từ chối (`No`)**: Quy trình dừng và xuất lý do từ chối.
4.  **Publisher-Agent**: Nếu bản nháp được duyệt, tác nhân này lưu nội dung vào tệp Markdown.

#### Phân Tích Triển Khai Python

Ví dụ này sử dụng một hàm tùy chỉnh, `select_targets`, để triển khai logic điều kiện. Hàm này được truyền vào `add_multi_selection_edge_group` và điều hướng quy trình dựa trên trường `review_result` từ đầu ra của tác nhân đánh giá.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Hàm này xác định bước tiếp theo dựa trên kết quả đánh giá
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Nếu được chấp nhận, tiếp tục đến bộ thực thi 'save_draft'
        return [save_draft_id]
    else:
        # Nếu bị từ chối, tiếp tục đến bộ thực thi 'handle_review' để báo lỗi
        return [handle_review_id]

# Trình tạo quy trình sử dụng hàm lựa chọn để định tuyến
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Cạnh chọn đa thực hiện logic điều kiện
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Các executor tùy chỉnh như `to_reviewer_result` được dùng để phân tích đầu ra JSON từ các tác nhân và chuyển đổi thành các đối tượng kiểu mạnh mà hàm chọn có thể kiểm tra.

#### Phân Tích Triển Khai .NET (C#)

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

Tham số `condition` của phương thức `AddEdge` cho phép `WorkflowBuilder` tạo đường nhánh. Quy trình chỉ đi theo cạnh tới `publishExecutor` nếu điều kiện `GetCondition(expectedResult: "Yes")` trả về true. Ngược lại, nó theo đường tới `sendReviewerExecutor`.

## Kết luận

Microsoft Agent Framework Workflow cung cấp nền tảng mạnh mẽ và linh hoạt để điều phối các hệ thống đa tác nhân phức tạp. Bằng cách tận dụng kiến trúc dựa trên đồ thị và các thành phần cốt lõi, nhà phát triển có thể thiết kế và triển khai các quy trình tinh vi trong cả Python và .NET. Dù ứng dụng của bạn yêu cầu xử lý tuần tự đơn giản, thực thi song song, hay logic điều kiện động, framework đều cung cấp công cụ để xây dựng giải pháp AI mạnh mẽ, mở rộng và an toàn kiểu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->