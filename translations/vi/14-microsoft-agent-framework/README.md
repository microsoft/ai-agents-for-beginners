# Khám Phá Microsoft Agent Framework

![Agent Framework](../../../translated_images/vi/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Giới Thiệu

Bài học này sẽ bao gồm:

- Hiểu về Microsoft Agent Framework: Các Tính Năng Chính và Giá Trị  
- Khám Phá Các Khái Niệm Chính của Microsoft Agent Framework
- Các Mẫu MAF Nâng Cao: Quy Trình Làm Việc, Middleware, và Bộ Nhớ

## Mục Tiêu Học Tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

- Xây dựng các AI Agents sẵn sàng cho sản xuất sử dụng Microsoft Agent Framework
- Áp dụng các tính năng cốt lõi của Microsoft Agent Framework vào các trường hợp sử dụng Agentic của bạn
- Sử dụng các mẫu nâng cao bao gồm quy trình làm việc, middleware và khả năng quan sát

## Mẫu Mã

Mẫu mã cho [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) có thể được tìm thấy trong kho lưu trữ này dưới các tệp `xx-python-agent-framework` và `xx-dotnet-agent-framework`.

## Hiểu Về Microsoft Agent Framework

![Framework Intro](../../../translated_images/vi/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) là framework thống nhất của Microsoft để xây dựng các AI agent. Nó cung cấp sự linh hoạt để giải quyết đa dạng các trường hợp sử dụng agentic thấy trong cả môi trường sản xuất và nghiên cứu bao gồm:

- **Điều phối Agent tuần tự** trong các kịch bản cần các bước làm việc theo trình tự.
- **Điều phối đồng thời** trong các kịch bản nơi các agent cần hoàn thành nhiệm vụ cùng lúc.
- **Điều phối nhóm chat** trong các kịch bản nơi các agent có thể cộng tác cùng nhau trên một nhiệm vụ.
- **Điều phối bàn giao** trong các kịch bản nơi các agent chuyển giao nhiệm vụ cho nhau khi các nhiệm vụ con được hoàn thành.
- **Điều phối Hút** trong các kịch bản nơi một agent quản lý tạo và sửa đổi danh sách nhiệm vụ và xử lý phối hợp các subagent để hoàn thành nhiệm vụ.

Để triển khai AI Agents trong sản xuất, MAF cũng bao gồm các tính năng cho:

- **Khả năng quan sát** thông qua việc sử dụng OpenTelemetry nơi mọi hành động của AI Agent bao gồm gọi công cụ, các bước điều phối, luồng suy luận và giám sát hiệu suất qua bảng điều khiển Microsoft Foundry.
- **Bảo mật** bằng cách lưu trữ agents trực tiếp trên Microsoft Foundry bao gồm các kiểm soát bảo mật như truy cập dựa trên vai trò, xử lý dữ liệu riêng tư và an toàn nội dung tích hợp sẵn.
- **Độ bền** vì các luồng agent và quy trình làm việc có thể tạm dừng, tiếp tục và phục hồi lỗi, cho phép các quy trình chạy dài hơn.
- **Kiểm soát** vì quy trình làm việc có sự tham gia của con người được hỗ trợ, nơi các nhiệm vụ được đánh dấu là yêu cầu phê duyệt của con người.

Microsoft Agent Framework cũng tập trung vào khả năng tương tác bằng:

- **Không lệ thuộc đám mây** - Agents có thể chạy trong containers, on-prem và trên nhiều đám mây khác nhau.
- **Không lệ thuộc nhà cung cấp** - Agents có thể được tạo qua SDK yêu thích của bạn bao gồm Azure OpenAI và OpenAI
- **Tích hợp các chuẩn mở** - Agents có thể sử dụng các giao thức như Agent-to-Agent (A2A) và Model Context Protocol (MCP) để khám phá và sử dụng các agent và công cụ khác.
- **Plugin và Kết nối** - Có thể kết nối với các dịch vụ dữ liệu và bộ nhớ như Microsoft Fabric, SharePoint, Pinecone và Qdrant.

Hãy xem các tính năng này được áp dụng như thế nào cho một số khái niệm cốt lõi của Microsoft Agent Framework.

## Các Khái Niệm Chính của Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/vi/agent-components.410a06daf87b4fef.webp)

**Tạo Agents**

Việc tạo agent được thực hiện bằng cách định nghĩa dịch vụ suy luận (Nhà cung cấp LLM), một tập hợp các hướng dẫn để AI Agent thực hiện, và một `name` được gán:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ví dụ trên sử dụng `Azure OpenAI` nhưng agent có thể được tạo bằng nhiều dịch vụ khác nhau bao gồm `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, các API `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

hoặc agent từ xa sử dụng giao thức A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Chạy Agents**

Agents được chạy bằng các phương thức `.run` hoặc `.run_stream` cho các phản hồi không streaming hoặc streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Mỗi lần chạy agent cũng có thể có các tùy chọn để tùy chỉnh các tham số như `max_tokens` được agent sử dụng, các `tools` mà agent có thể gọi, và thậm chí là `model` được sử dụng cho agent.

Điều này hữu ích trong các trường hợp cần các mô hình hoặc công cụ cụ thể để hoàn thành nhiệm vụ người dùng.

**Công Cụ**

Công cụ có thể được định nghĩa cả khi tạo agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Khi tạo một ChatAgent trực tiếp

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

và cũng khi chạy agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Công cụ chỉ được cung cấp cho lần chạy này )
```

**Luồng Agent**

Luồng Agent được dùng để xử lý các cuộc hội thoại đa lượt. Luồng có thể được tạo theo một trong hai cách:

- Sử dụng `get_new_thread()` cho phép luồng được lưu lại theo thời gian
- Tạo luồng tự động khi chạy agent và chỉ tồn tại trong lần chạy hiện tại.

Để tạo một luồng, đoạn mã trông như sau:

```python
# Tạo một luồng mới.
thread = agent.get_new_thread() # Chạy tác nhân với luồng.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Bạn có thể tuần tự hóa luồng này để lưu trữ sử dụng sau:

```python
# Tạo một chuỗi mới.
thread = agent.get_new_thread() 

# Chạy tác nhân với chuỗi.

response = await agent.run("Hello, how are you?", thread=thread) 

# Tuần tự hóa chuỗi để lưu trữ.

serialized_thread = await thread.serialize() 

# Giải tuần tự trạng thái chuỗi sau khi tải từ bộ nhớ.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware của Agent**

Agents tương tác với công cụ và LLM để hoàn thành nhiệm vụ người dùng. Trong một số kịch bản, chúng ta muốn thực thi hoặc theo dõi các hành động giữa các tương tác này. Middleware cho agent cho phép làm điều đó thông qua:

*Middleware cho Hàm*

Middleware này cho phép thực thi một hành động giữa agent và một hàm/công cụ mà nó sẽ gọi. Ví dụ khi bạn muốn ghi lại nhật ký việc gọi hàm.

Trong đoạn mã dưới đây `next` định nghĩa có gọi middleware tiếp theo hoặc gọi hàm thực tế hay không.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Tiền xử lý: Ghi lại trước khi chạy hàm
    print(f"[Function] Calling {context.function.name}")

    # Tiếp tục đến middleware tiếp theo hoặc thực thi hàm
    await next(context)

    # Hậu xử lý: Ghi lại sau khi chạy hàm
    print(f"[Function] {context.function.name} completed")
```

*Middleware Chat*

Middleware này cho phép thực thi hoặc ghi lại hành động giữa agent và các yêu cầu giữa LLM.

Điều này chứa thông tin quan trọng như `messages` được gửi đến dịch vụ AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Tiền xử lý: Ghi nhật ký trước khi gọi AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Tiếp tục tới middleware hoặc dịch vụ AI tiếp theo
    await next(context)

    # Hậu xử lý: Ghi nhật ký sau phản hồi của AI
    print("[Chat] AI response received")

```

**Bộ Nhớ của Agent**

Như đã đề cập trong bài học `Agentic Memory`, bộ nhớ là yếu tố quan trọng để agent hoạt động trên các ngữ cảnh khác nhau. MAF cung cấp nhiều loại bộ nhớ khác nhau:

*Lưu Trữ Trong Bộ Nhớ*

Đây là bộ nhớ được lưu trong các luồng khi ứng dụng chạy.

```python
# Tạo một luồng mới.
thread = agent.get_new_thread() # Chạy agent với luồng đó.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Tin Nhắn Lưu Trữ*

Bộ nhớ này dùng để lưu lịch sử hội thoại qua các phiên khác nhau. Nó được định nghĩa sử dụng `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Tạo một kho lưu trữ tin nhắn tùy chỉnh
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Bộ Nhớ Động*

Bộ nhớ này được thêm vào ngữ cảnh trước khi agents chạy. Những bộ nhớ này có thể lưu trữ trong các dịch vụ bên ngoài như mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Sử dụng Mem0 cho các khả năng bộ nhớ nâng cao
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

**Khả năng Quan sát của Agent**

Khả năng quan sát là quan trọng để xây dựng hệ thống agentic tin cậy và dễ bảo trì. MAF tích hợp với OpenTelemetry để cung cấp việc truy vết và đo lường cho khả năng quan sát tốt hơn.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # làm gì đó
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Quy Trình Làm Việc

MAF cung cấp các quy trình làm việc là các bước được định nghĩa sẵn để hoàn thành một nhiệm vụ và bao gồm các AI agents như các thành phần trong các bước đó.

Quy trình làm việc bao gồm các thành phần khác nhau cho phép kiểm soát luồng tốt hơn. Quy trình làm việc cũng hỗ trợ **điều phối đa agent** và **điểm kiểm tra** để lưu trạng thái quy trình làm việc.

Các thành phần cốt lõi của quy trình làm việc là:

**Executor**

Executor nhận các tin nhắn đầu vào, thực hiện nhiệm vụ được giao, sau đó tạo ra tin nhắn đầu ra. Điều này đẩy quy trình làm việc tiến tới hoàn thành nhiệm vụ lớn hơn. Executor có thể là AI agent hoặc logic tùy chỉnh.

**Edges**

Edges được dùng để định nghĩa luồng tin nhắn trong quy trình làm việc. Có thể là:

*Direct Edges* - Kết nối đơn giản một-một giữa các executor:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - Kích hoạt sau khi điều kiện nhất định được đáp ứng. Ví dụ, khi phòng khách sạn không còn, executor có thể đề xuất lựa chọn khác.

*Switch-case Edges* - Định tuyến tin nhắn tới các executor khác nhau dựa trên các điều kiện định nghĩa. Ví dụ, nếu khách du lịch có quyền truy cập ưu tiên thì nhiệm vụ của họ sẽ được xử lý qua một quy trình làm việc khác.

*Fan-out Edges* - Gửi một tin nhắn đến nhiều mục tiêu.

*Fan-in Edges* - Thu thập nhiều tin nhắn từ các executor khác nhau và gửi đến một mục tiêu.

**Sự kiện**

Để cung cấp khả năng quan sát tốt hơn vào quy trình làm việc, MAF cung cấp các sự kiện tích hợp cho việc thực thi bao gồm:

- `WorkflowStartedEvent`  - Bắt đầu thực thi quy trình làm việc
- `WorkflowOutputEvent` - Quy trình làm việc tạo ra kết quả
- `WorkflowErrorEvent` - Quy trình làm việc gặp lỗi
- `ExecutorInvokeEvent`  - Executor bắt đầu xử lý
- `ExecutorCompleteEvent`  -  Executor hoàn thành xử lý
- `RequestInfoEvent` - Một yêu cầu được gửi đi

## Các Mẫu MAF Nâng Cao

Các phần trên bao gồm các khái niệm chính của Microsoft Agent Framework. Khi bạn xây dựng các agents phức tạp hơn, dưới đây là một số mẫu nâng cao cần xem xét:

- **Ghé nối Middleware**: Chuỗi nhiều trình xử lý middleware (ghi nhật ký, xác thực, giới hạn tốc độ) sử dụng middleware hàm và chat để kiểm soát hành vi agent tinh vi hơn.
- **Điểm kiểm tra quy trình làm việc**: Sử dụng sự kiện quy trình làm việc và tuần tự hóa để lưu và tiếp tục các quy trình agent chạy dài.
- **Lựa chọn công cụ động**: Kết hợp RAG trên mô tả công cụ với đăng ký công cụ của MAF để chỉ trình bày các công cụ liên quan cho mỗi truy vấn.
- **Bàn giao đa agent**: Sử dụng các cạnh quy trình làm việc và định tuyến có điều kiện để điều phối bàn giao giữa các agent chuyên biệt.

## Mẫu Mã

Mẫu mã cho Microsoft Agent Framework có thể được tìm thấy trong kho lưu trữ này dưới các tệp `xx-python-agent-framework` và `xx-dotnet-agent-framework`.

## Có Thắc Mắc Gì Thêm Về Microsoft Agent Framework?

Tham gia [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ các người học khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về AI Agents của bạn.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với những thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu lầm hoặc hiểu sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->