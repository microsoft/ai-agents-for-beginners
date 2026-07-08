# Xây dựng Ứng dụng Đa Tác nhân với Microsoft Agent Framework Workflow

Hướng dẫn này sẽ giúp bạn hiểu và xây dựng các ứng dụng đa tác nhân sử dụng Microsoft Agent Framework. Chúng ta sẽ khám phá các khái niệm cốt lõi của hệ thống đa tác nhân, tìm hiểu kiến trúc của thành phần Workflow trong framework, và đi qua các ví dụ thực tiễn bằng Python và .NET cho các mẫu workflow khác nhau.

## 1\. Hiểu về Hệ Thống Đa Tác Nhân

Một Tác nhân AI là một hệ thống vượt ra ngoài khả năng của một Mô hình Ngôn ngữ Lớn (LLM) tiêu chuẩn. Nó có thể cảm nhận môi trường, đưa ra quyết định và thực hiện hành động để đạt được các mục tiêu cụ thể. Một hệ thống đa tác nhân bao gồm nhiều tác nhân phối hợp với nhau để giải quyết một vấn đề mà một tác nhân đơn lẻ khó hoặc không thể xử lý một mình.

### Kịch bản Ứng Dụng Thông Thường

  * **Giải quyết vấn đề phức tạp**: Chia một tác vụ lớn (ví dụ, lên kế hoạch sự kiện toàn công ty) thành các nhiệm vụ con nhỏ hơn được xử lý bởi các tác nhân chuyên môn (ví dụ, tác nhân ngân sách, tác nhân logistics, tác nhân marketing).
  * **Trợ lý ảo**: Một tác nhân trợ lý chính ủy thác các nhiệm vụ như lên lịch, nghiên cứu và đặt chỗ cho các tác nhân chuyên môn khác.
  * **Tạo nội dung tự động**: Một workflow trong đó một tác nhân soạn thảo nội dung, một tác nhân khác xem xét độ chính xác và tông điệu, và tác nhân thứ ba thì xuất bản.

### Các Mẫu Đa Tác Nhân

Hệ thống đa tác nhân có thể được tổ chức theo nhiều mẫu khác nhau, điều này quyết định cách thức tương tác của chúng:

  * **Tuần tự**: Các tác nhân làm việc theo thứ tự định trước, giống như một dây chuyền lắp ráp. Đầu ra của một tác nhân trở thành đầu vào cho tác nhân tiếp theo.
  * **Đồng thời**: Các tác nhân làm việc song song trên các phần khác nhau của tác vụ, và kết quả của chúng được tổng hợp khi kết thúc.
  * **Có điều kiện**: Workflow theo các đường đi khác nhau dựa trên đầu ra của một tác nhân, tương tự câu lệnh if-then-else.

## 2\. Kiến Trúc Workflow của Microsoft Agent Framework

Hệ thống workflow của Agent Framework là một công cụ điều phối tiên tiến được thiết kế để quản lý các tương tác phức tạp giữa nhiều tác nhân. Nó được xây dựng trên kiến trúc đồ thị sử dụng [mô hình thực thi kiểu Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), trong đó việc xử lý diễn ra theo các bước đồng bộ gọi là "supersteps."

### Các Thành Phần Cốt Lõi

Kiến trúc bao gồm ba phần chính:

1.  **Executors**: Đây là các đơn vị xử lý cơ bản. Trong ví dụ của chúng ta, một `Agent` là một loại executor. Mỗi executor có thể có nhiều bộ xử lý tin nhắn được tự động gọi dựa trên loại tin nhắn nhận được.
2.  **Edges**: Xác định đường đi mà các tin nhắn đi qua giữa các executor. Edges có thể có điều kiện, cho phép điều hướng linh hoạt thông tin qua đồ thị workflow.
3.  **Workflow**: Thành phần điều phối toàn bộ quá trình, quản lý các executor, edges và luồng thực thi tổng thể. Nó đảm bảo tin nhắn được xử lý đúng thứ tự và truyền sự kiện để theo dõi.

*Một sơ đồ minh họa các thành phần cốt lõi của hệ thống workflow.*

Cấu trúc này cho phép xây dựng các ứng dụng mạnh mẽ và có thể mở rộng bằng cách sử dụng các mẫu cơ bản như chuỗi tuần tự, fan-out/fan-in cho xử lý song song, và logic switch-case cho luồng có điều kiện.

## 3\. Ví dụ Thực Tiễn và Phân Tích Mã

Bây giờ, hãy cùng khám phá cách triển khai các mẫu workflow khác nhau sử dụng framework. Chúng ta sẽ xem mã ví dụ bằng cả Python và .NET cho từng trường hợp.

### Trường hợp 1: Workflow Tuần Tự Cơ Bản

Đây là mẫu đơn giản nhất, trong đó đầu ra của một tác nhân được truyền trực tiếp cho tác nhân khác. Kịch bản của chúng ta liên quan đến tác nhân `FrontDesk` khách sạn đưa ra lời khuyên du lịch, sau đó được tác nhân `Concierge` xem xét.

*Sơ đồ workflow cơ bản FrontDesk -\> Concierge.*

#### Bối cảnh Kịch bản

Một khách du lịch hỏi lời khuyên ở Paris.

1.  Tác nhân `FrontDesk`, được thiết kế ngắn gọn, đề xuất thăm Bảo tàng Louvre.
2.  Tác nhân `Concierge`, ưu tiên trải nghiệm chân thực, nhận đề xuất này. Nó xem xét lời khuyên và phản hồi, gợi ý lựa chọn địa phương hơn, ít mang tính du lịch.

#### Phân Tích Triển Khai Python

Trong ví dụ Python, trước tiên chúng ta định nghĩa và tạo hai tác nhân, mỗi tác nhân có hướng dẫn cụ thể.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Định nghĩa vai trò và hướng dẫn của tác nhân
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Tạo các thể hiện của tác nhân
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Tiếp theo, `WorkflowBuilder` được sử dụng để xây dựng đồ thị. `front_desk_agent` được đặt làm điểm bắt đầu, và một đường nối được tạo để kết nối đầu ra của nó tới `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Cuối cùng, workflow được thực thi với lời nhắc ban đầu từ người dùng.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run thực thi luồng công việc; get_outputs() trả về kết quả của bộ thực thi đầu ra.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Phân Tích Triển Khai .NET (C#)

Cách triển khai .NET theo logic rất giống. Đầu tiên, các hằng số được định nghĩa cho tên và hướng dẫn của các tác nhân.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Các tác nhân được tạo qua `AzureOpenAIClient` (API Responses), rồi `WorkflowBuilder` định nghĩa luồng tuần tự bằng cách thêm cạnh từ `frontDeskAgent` tới `reviewerAgent`.

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

Workflow sau đó được chạy với tin nhắn của người dùng, và kết quả được truyền về theo luồng.

### Trường hợp 2: Workflow Tuần Tự Nhiều Bước

Mẫu này mở rộng chuỗi cơ bản với nhiều tác nhân hơn. Phù hợp cho các quá trình yêu cầu nhiều giai đoạn tinh chỉnh hoặc chuyển đổi.

#### Bối cảnh Kịch bản

Người dùng cung cấp hình ảnh phòng khách và yêu cầu báo giá nội thất.

1.  **Tác nhân Bán hàng**: Nhận diện các món nội thất trong hình và tạo danh sách.
2.  **Tác nhân Giá cả**: Nhận danh sách và cung cấp bảng giá chi tiết, bao gồm tùy chọn ngân sách, trung cấp và cao cấp.
3.  **Tác nhân Báo giá**: Nhận danh sách đã định giá và định dạng thành tài liệu báo giá chính thức bằng Markdown.

*Sơ đồ workflow Sales -\> Price -\> Quote.*

#### Phân Tích Triển Khai Python

Ba tác nhân được định nghĩa, mỗi tác nhân đảm nhiệm một vai trò chuyên biệt. Workflow được xây dựng bằng cách sử dụng `add_edge` tạo chuỗi: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Tạo ba đại lý chuyên dụng
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Xây dựng quy trình làm việc tuần tự
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Đầu vào là một `ChatMessage` bao gồm cả văn bản và URL hình ảnh. Framework đảm bảo truyền đầu ra của từng tác nhân tới tác nhân kế tiếp trong chuỗi cho tới khi tạo ra báo giá cuối cùng.

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

# Chạy quy trình làm việc
events = await workflow.run(message)
```

#### Phân Tích Triển Khai .NET (C#)

Ví dụ .NET phản chiếu phiên bản Python. Ba tác nhân (`salesagent`, `priceagent`, `quoteagent`) được tạo. `WorkflowBuilder` liên kết chúng theo thứ tự.

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

Tin nhắn của người dùng được tạo ra với cả dữ liệu ảnh (dạng byte) và lời nhắc văn bản. Phương thức `InProcessExecution.StreamAsync` bắt đầu workflow, và đầu ra cuối cùng được lấy từ luồng.

### Trường hợp 3: Workflow Đồng Thời

Mẫu này dùng khi các nhiệm vụ có thể thực hiện đồng thời để tiết kiệm thời gian. Nó bao gồm một bước "fan-out" đến nhiều tác nhân và "fan-in" để tổng hợp kết quả.

#### Bối cảnh Kịch bản

Người dùng yêu cầu lên kế hoạch chuyến đi đến Seattle.

1.  **Bộ Phân Phối (Fan-Out)**: Yêu cầu của người dùng được gửi đồng thời đến hai tác nhân.
2.  **Tác nhân Nghiên cứu**: Nghiên cứu các điểm tham quan, thời tiết, và các điểm quan trọng cho chuyến đi Seattle vào tháng Mười Hai.
3.  **Tác nhân Lập kế hoạch**: Độc lập tạo ra lịch trình chi tiết từng ngày.
4.  **Bộ Tổng hợp (Fan-In)**: Đầu ra từ cả tác nhân nghiên cứu và lập kế hoạch được tập hợp và trình bày cùng nhau như kết quả cuối cùng.

*Sơ đồ workflow đồng thời của Researcher và Planner.*

#### Phân Tích Triển Khai Python

`ConcurrentBuilder` đơn giản hóa việc tạo mẫu này. Bạn chỉ cần liệt kê các tác nhân tham gia, và builder tự động tạo logic fan-out và fan-in cần thiết.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder xử lý logic fan-out/fan-in
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Chạy quy trình công việc
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework đảm bảo `research_agent` và `plan_agent` thực thi song song, và kết quả cuối cùng của chúng được thu thập vào một danh sách.

#### Phân Tích Triển Khai .NET (C#)

Trong .NET, mẫu này yêu cầu định nghĩa rõ ràng hơn. Các executor tùy chỉnh (`ConcurrentStartExecutor` và `ConcurrentAggregationExecutor`) được tạo để xử lý logic fan-out và fan-in.

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

`WorkflowBuilder` sử dụng `AddFanOutEdge` và `AddFanInEdge` để xây dựng đồ thị với các executor và tác nhân tùy chỉnh này.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Trường hợp 4: Workflow Có Điều Kiện

Workflow có điều kiện giới thiệu logic phân nhánh, cho phép hệ thống đi theo các hướng khác nhau dựa trên kết quả trung gian.

#### Bối cảnh Kịch bản

Workflow này tự động tạo và xuất bản một hướng dẫn kỹ thuật.

1.  **Tác nhân Evangelist**: Viết bản thảo hướng dẫn dựa trên đề cương và URL đã cho.
2.  **Tác nhân ContentReviewer**: Xem xét bản thảo. Kiểm tra xem số từ có vượt quá 200 từ không.
3.  **Nhánh Điều kiện**:
      * **Nếu được duyệt (`Yes`)**: Workflow tiếp tục đến `Publisher-Agent`.
      * **Nếu bị từ chối (`No`)**: Workflow dừng và xuất lý do từ chối.
4.  **Tác nhân Publisher**: Nếu bản thảo được duyệt, tác nhân này lưu nội dung thành file Markdown.

#### Phân Tích Triển Khai Python

Ví dụ này sử dụng hàm tùy chỉnh `select_targets` để thực hiện logic có điều kiện. Hàm này được truyền vào `add_multi_selection_edge_group` và điều hướng workflow dựa trên trường `review_result` từ đầu ra của người xem xét.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Hàm này xác định bước tiếp theo dựa trên kết quả đánh giá
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Nếu được phê duyệt, tiếp tục đến executor 'save_draft'
        return [save_draft_id]
    else:
        # Nếu bị từ chối, tiếp tục đến executor 'handle_review' để báo cáo thất bại
        return [handle_review_id]

# Trình tạo quy trình làm việc sử dụng hàm lựa chọn để điều hướng
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Cạnh lựa chọn đa chiều thực hiện logic điều kiện
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Các executor tùy chỉnh như `to_reviewer_result` được sử dụng để phân tích cú pháp đầu ra JSON từ các tác nhân và chuyển đổi thành các đối tượng kiểu mạnh mà hàm chọn có thể kiểm tra.

#### Phân Tích Triển Khai .NET (C#)

Phiên bản .NET sử dụng cách tiếp cận tương tự với hàm điều kiện. Một `Func<object?, bool>` được định nghĩa để kiểm tra thuộc tính `Result` của đối tượng `ReviewResult`.

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

Tham số `condition` của phương thức `AddEdge` cho phép `WorkflowBuilder` tạo ra đường đi phân nhánh. Workflow chỉ theo cạnh tới `publishExecutor` nếu điều kiện `GetCondition(expectedResult: "Yes")` trả về true. Nếu không, nó theo đường đến `sendReviewerExecutor`.

## Kết Luận

Microsoft Agent Framework Workflow cung cấp nền tảng mạnh mẽ và linh hoạt để điều phối các hệ thống đa tác nhân phức tạp. Bằng cách tận dụng kiến trúc dựa trên đồ thị và các thành phần cốt lõi, nhà phát triển có thể thiết kế và triển khai các workflow tinh vi cả trong Python và .NET. Dù ứng dụng của bạn cần xử lý tuần tự đơn giản, thực thi song song, hay logic điều kiện động, framework cung cấp công cụ để xây dựng các giải pháp AI mạnh mẽ, có khả năng mở rộng và an toàn về kiểu dữ liệu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->