# Khám phá Microsoft Agent Framework

![Agent Framework](../../../translated_images/vi/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Giới thiệu

Bài học này sẽ bao gồm:

- Hiểu về Microsoft Agent Framework: Các Tính Năng Chính và Giá Trị  
- Khám phá Các Khái Niệm Chính của Microsoft Agent Framework
- Các Mẫu MAF Nâng Cao: Quy trình làm việc, Middleware và Bộ nhớ

## Mục Tiêu Học Tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

- Xây dựng các Đại lý AI sẵn sàng cho sản xuất sử dụng Microsoft Agent Framework
- Áp dụng các tính năng cốt lõi của Microsoft Agent Framework vào các trường hợp sử dụng đại lý
- Sử dụng các mẫu nâng cao bao gồm quy trình làm việc, middleware và khả năng quan sát

## Mẫu Mã Code 

Mẫu mã code cho [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) có thể được tìm thấy trong kho lưu trữ này dưới các tệp `xx-python-agent-framework` và `xx-dotnet-agent-framework`.

## Hiểu về Microsoft Agent Framework

![Framework Intro](../../../translated_images/vi/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) là khuôn khổ thống nhất của Microsoft để xây dựng các đại lý AI. Nó cung cấp sự linh hoạt để giải quyết nhiều trường hợp sử dụng đại lý khác nhau được thấy cả trong môi trường sản xuất và nghiên cứu bao gồm:

- **Điều phối đại lý theo trình tự** trong các tình huống cần các quy trình làm việc từng bước.
- **Điều phối đồng thời** trong các tình huống đại lý cần hoàn thành nhiệm vụ cùng lúc.
- **Điều phối trò chuyện nhóm** trong các tình huống đại lý có thể cộng tác cùng nhau trong một nhiệm vụ.
- **Điều phối chuyển giao** trong các tình huống đại lý chuyển giao nhiệm vụ cho nhau khi các nhiệm vụ con được hoàn thành.
- **Điều phối từ xa (Magnetic Orchestration)** trong các tình huống một đại lý quản lý tạo và chỉnh sửa danh sách nhiệm vụ và xử lý việc phối hợp các đại lý phụ để hoàn thành nhiệm vụ.

Để cung cấp các Đại lý AI trong Sản xuất, MAF còn bao gồm các tính năng cho:

- **Khả năng quan sát** bằng cách sử dụng OpenTelemetry nơi mọi hành động của Đại lý AI bao gồm gọi công cụ, các bước điều phối, luồng suy luận và giám sát hiệu suất qua bảng điều khiển Microsoft Foundry.
- **Bảo mật** bằng việc lưu trữ đại lý trực tiếp trên Microsoft Foundry với các kiểm soát bảo mật như quyền truy cập dựa trên vai trò, xử lý dữ liệu riêng tư và an toàn nội dung tích hợp sẵn.
- **Độ bền** khi các luồng đại lý và quy trình làm việc có thể tạm dừng, tiếp tục và khôi phục từ lỗi cho phép quá trình chạy dài hơn.
- **Kiểm soát** khi các quy trình làm việc có sự tham gia của con người được hỗ trợ, ở đó các nhiệm vụ được đánh dấu là cần phê duyệt bởi con người.

Microsoft Agent Framework cũng tập trung vào khả năng tương tác bằng cách:

- **Không phụ thuộc vào Cloud cụ thể** - Đại lý có thể chạy trong container, tại chỗ và trên nhiều đám mây khác nhau.
- **Không phụ thuộc vào nhà cung cấp** - Đại lý có thể được tạo qua SDK ưa thích của bạn bao gồm Azure OpenAI và OpenAI
- **Tích hợp các tiêu chuẩn mở** - Đại lý có thể sử dụng các giao thức như Agent-to-Agent (A2A) và Model Context Protocol (MCP) để khám phá và sử dụng các đại lý và công cụ khác.
- **Plugin và Kết nối** - Kết nối có thể được thiết lập với các dịch vụ dữ liệu và bộ nhớ như Microsoft Fabric, SharePoint, Pinecone và Qdrant.

Hãy xem cách các tính năng này được áp dụng vào một số khái niệm cốt lõi của Microsoft Agent Framework.

## Các Khái Niệm Chính của Microsoft Agent Framework

### Đại lý

![Agent Framework](../../../translated_images/vi/agent-components.410a06daf87b4fef.webp)

**Tạo đại lý**

Việc tạo đại lý được thực hiện bằng cách định nghĩa dịch vụ suy luận (Nhà cung cấp LLM),  
một bộ hướng dẫn cho Đại lý AI tuân theo, và một `name` được chỉ định:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ví dụ trên sử dụng `Azure OpenAI` nhưng đại lý có thể được tạo bằng nhiều dịch vụ bao gồm `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

API OpenAI `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

hoặc [MiniMax](https://platform.minimaxi.com/), cung cấp API tương thích với OpenAI với các cửa sổ ngữ cảnh lớn (tới 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

hoặc đại lý từ xa dùng giao thức A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Chạy đại lý**

Đại lý được chạy sử dụng phương thức `.run` hoặc `.run_stream` cho các phản hồi không stream hoặc có stream.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Mỗi lần chạy đại lý cũng có các tùy chọn để tùy chỉnh tham số như `max_tokens` mà đại lý sử dụng, `tools` mà đại lý có thể gọi, và thậm chí `model` dùng cho đại lý.

Điều này hữu ích trong các trường hợp yêu cầu các mô hình hoặc công cụ cụ thể để hoàn thành nhiệm vụ của người dùng.

**Công cụ**

Công cụ có thể được định nghĩa cả khi định nghĩa đại lý:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Khi tạo một ChatAgent trực tiếp

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

và cũng khi chạy đại lý:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Công cụ chỉ được cung cấp cho lần chạy này )
```

**Luồng đại lý**

Luồng đại lý được dùng để xử lý các cuộc hội thoại nhiều lượt. Luồng có thể được tạo bằng cách:

- Sử dụng `get_new_thread()` cho phép luồng được lưu lại theo thời gian
- Tạo luồng tự động khi chạy đại lý và luồng chỉ tồn tại trong lần chạy đó.

Để tạo luồng, mã sẽ như sau:

```python
# Tạo một luồng mới.
thread = agent.get_new_thread() # Chạy tác nhân với luồng.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Sau đó bạn có thể tuần tự hóa luồng để lưu trữ dùng về sau:

```python
# Tạo một luồng mới.
thread = agent.get_new_thread() 

# Chạy tác nhân với luồng.

response = await agent.run("Hello, how are you?", thread=thread) 

# Tuần tự hóa luồng để lưu trữ.

serialized_thread = await thread.serialize() 

# Giải tuần tự trạng thái luồng sau khi tải từ bộ nhớ.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware đại lý**

Đại lý tương tác với công cụ và LLM để hoàn thành nhiệm vụ của người dùng. Trong một số tình huống, chúng ta muốn thực thi hoặc theo dõi giữa các tương tác này. Middleware đại lý cho phép chúng ta làm điều này thông qua:

*Middleware chức năng*

Middleware này cho phép thực thi một hành động giữa đại lý và một chức năng/công cụ mà nó sẽ gọi. Ví dụ trường hợp dùng nó là khi bạn muốn ghi lại nhật ký cuộc gọi chức năng.

Trong mã dưới đây `next` định nghĩa xem middleware kế tiếp hay chính chức năng cần gọi.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Tiền xử lý: Ghi log trước khi thực thi hàm
    print(f"[Function] Calling {context.function.name}")

    # Tiếp tục đến middleware tiếp theo hoặc thực thi hàm
    await next(context)

    # Hậu xử lý: Ghi log sau khi thực thi hàm
    print(f"[Function] {context.function.name} completed")
```

*Middleware trò chuyện*

Middleware này cho phép thực thi hoặc ghi lại hành động giữa đại lý và các yêu cầu giữa LLM.

Nó bao gồm thông tin quan trọng như `messages` được gửi đến dịch vụ AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Tiền xử lý: Ghi log trước khi gọi AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Tiếp tục đến middleware hoặc dịch vụ AI tiếp theo
    await next(context)

    # Hậu xử lý: Ghi log sau khi nhận phản hồi từ AI
    print("[Chat] AI response received")

```

**Bộ nhớ đại lý**

Như đã đề cập trong bài học `Agentic Memory`, bộ nhớ là một yếu tố quan trọng để đại lý có thể hoạt động trên nhiều bối cảnh khác nhau. MAF cung cấp nhiều loại bộ nhớ khác nhau:

*Bộ nhớ trong ứng dụng*

Đây là bộ nhớ được lưu trong các luồng trong thời gian chạy ứng dụng.

```python
# Tạo một luồng mới.
thread = agent.get_new_thread() # Chạy tác nhân với luồng đó.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Tin nhắn bền vững*

Bộ nhớ này dùng để lưu lịch sử hội thoại qua các phiên khác nhau. Nó được định nghĩa bằng `chat_message_store_factory`:

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

*Bộ nhớ động*

Bộ nhớ này được thêm vào ngữ cảnh trước khi các đại lý được chạy. Những bộ nhớ này có thể được lưu trữ trong các dịch vụ bên ngoài như mem0:

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

**Khả năng quan sát đại lý**


Khả năng quan sát là quan trọng để xây dựng các hệ thống tác nhân đáng tin cậy và dễ bảo trì. MAF tích hợp với OpenTelemetry để cung cấp theo dõi và đo lường nhằm nâng cao khả năng quan sát.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # làm điều gì đó
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Luồng công việc

MAF cung cấp các luồng công việc là các bước được định nghĩa sẵn để hoàn thành một nhiệm vụ và bao gồm các tác nhân AI như các thành phần trong những bước đó.

Luồng công việc được tạo thành từ các thành phần khác nhau giúp kiểm soát luồng tốt hơn. Luồng công việc cũng cho phép **điều phối đa tác nhân** và **điểm kiểm tra** để lưu trạng thái luồng công việc.

Các thành phần cốt lõi của một luồng công việc là:

**Trình thực thi**

Trình thực thi nhận các tin nhắn đầu vào, thực hiện các nhiệm vụ được giao, sau đó tạo ra một tin nhắn đầu ra. Điều này giúp luồng công việc tiến về phía trước để hoàn thành nhiệm vụ lớn hơn. Trình thực thi có thể là tác nhân AI hoặc logic tùy chỉnh.

**Cạnh**

Cạnh được dùng để xác định luồng của các tin nhắn trong luồng công việc. Bao gồm các loại:

*Cạnh trực tiếp* - Kết nối đơn giản một-một giữa các trình thực thi:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Cạnh có điều kiện* - Kích hoạt sau khi một điều kiện nhất định được thỏa mãn. Ví dụ, khi phòng khách sạn không còn, một trình thực thi có thể đề xuất các lựa chọn khác.

*Cạnh chuyển đổi* - Định tuyến các tin nhắn đến các trình thực thi khác nhau dựa trên các điều kiện đã xác định. Ví dụ, nếu khách du lịch có quyền ưu tiên thì nhiệm vụ của họ sẽ được xử lý qua một luồng công việc khác.

*Cạnh phân nhánh* - Gửi một tin nhắn đến nhiều đích.

*Cạnh hội tụ* - Thu thập nhiều tin nhắn từ các trình thực thi khác nhau và gửi đến một đích duy nhất.

**Sự kiện**

Để cung cấp khả năng quan sát tốt hơn vào các luồng công việc, MAF cung cấp các sự kiện có sẵn cho quá trình thực thi bao gồm:

- `WorkflowStartedEvent`  - Bắt đầu thực thi luồng công việc
- `WorkflowOutputEvent` - Luồng công việc tạo ra một đầu ra
- `WorkflowErrorEvent` - Luồng công việc gặp lỗi
- `ExecutorInvokeEvent`  - Trình thực thi bắt đầu xử lý
- `ExecutorCompleteEvent`  -  Trình thực thi hoàn thành xử lý
- `RequestInfoEvent` - Một yêu cầu được phát ra

## Các mẫu nâng cao của MAF

Các phần trên đã đề cập các khái niệm chính của Microsoft Agent Framework. Khi bạn xây dựng các tác nhân phức tạp hơn, đây là một số mẫu nâng cao để cân nhắc:

- **Kết hợp Middleware**: Chuỗi nhiều bộ xử lý middleware (ghi log, xác thực, giới hạn tần suất) sử dụng middleware chức năng và chat để kiểm soát hành vi tác nhân tinh vi hơn.
- **Checkpoint luồng công việc**: Sử dụng sự kiện luồng công việc và tuần tự hóa để lưu và tiếp tục các quá trình tác nhân kéo dài.
- **Lựa chọn công cụ động**: Kết hợp RAG trên mô tả công cụ với đăng ký công cụ của MAF để chỉ trình bày các công cụ phù hợp cho từng truy vấn.
- **Chuyển giao đa tác nhân**: Sử dụng các cạnh luồng công việc và định tuyến có điều kiện để điều phối chuyển giao giữa các tác nhân chuyên biệt.

## Lưu trữ các tác nhân LangChain / LangGraph trên Microsoft Foundry

Microsoft Agent Framework là **đa khung phát triển** — bạn không bị giới hạn với các tác nhân viết bằng MAF. Nếu bạn đã có một tác nhân được xây dựng với **LangChain** hoặc **LangGraph**, bạn có thể chạy nó như một **tác nhân lưu trữ Microsoft Foundry** để Foundry quản lý thời gian chạy, phiên làm việc, quy mô, định danh và điểm đầu cuối giao thức cho bạn, trong khi logic tác nhân vẫn nằm trong LangGraph.

Điều này được thực hiện qua gói `langchain_azure_ai.agents.hosting`, cung cấp một đồ thị LangGraph đã biên dịch qua cùng các giao thức mà các tác nhân lưu trữ Foundry sử dụng.

**1. Cài đặt phần mở rộng hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Phần mở rộng `hosting` cài đặt các thư viện giao thức Foundry: `azure-ai-agentserver-responses` (điểm cuối `/responses` tương thích OpenAI) và `azure-ai-agentserver-invocations` (điểm cuối `/invocations` chung).

**2. Chọn một giao thức hosting:**

| Giao thức | Lớp máy chủ | Điểm cuối | Dùng khi |
|----------|-------------|-----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Bạn muốn chat, streaming, lịch sử phản hồi và chuỗi hội thoại tương thích OpenAI — là mặc định được khuyến nghị cho các tác nhân hội thoại. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Bạn cần một định dạng JSON tùy chỉnh, một điểm cuối kiểu webhook hoặc xử lý phi hội thoại. |

Vì **Responses API là API chính để phát triển tác nhân trong Foundry**, hãy bắt đầu với `ResponsesHostServer` cho hầu hết các tác nhân.

**3. Cấu hình biến môi trường** (`az login` trước để `DefaultAzureCredential` xác thực):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Khi tác nhân chạy sau đó như tác nhân lưu trữ trong Foundry, nền tảng sẽ tự động chèn `FOUNDRY_PROJECT_ENDPOINT`.

**4. Phơi bày tác nhân LangGraph qua giao thức Responses:**

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

    # ChatOpenAI ở đây nhắm vào điểm cuối (Responses) tương thích OpenAI của dự án Foundry.
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

Chạy trên máy cục bộ với `python main.py`, sau đó gửi yêu cầu Responses tới `http://localhost:8088/responses`.

**Các hành vi chủ chốt:**

- **Hội thoại**: Khách hàng tiếp tục hội thoại bằng cách truyền `previous_response_id` hoặc ID `conversation`. Nếu đồ thị của bạn được biên dịch với bộ lưu trữ kiểm tra LangGraph, Foundry sẽ khóa trạng thái hội thoại với điểm kiểm tra (dùng bộ lưu trữ bền vững trong môi trường sản xuất; `MemorySaver` phù hợp cho kiểm thử cục bộ).
- **Con người can thiệp**: Nếu đồ thị của bạn dùng `interrupt()` của LangGraph, `ResponsesHostServer` sẽ hiển thị sự can thiệp đang chờ như một mục `function_call` / `mcp_approval_request` trong Responses, và khách hàng sẽ tiếp tục với `function_call_output` / `mcp_approval_response` tương ứng.
- **Triển khai lên Foundry**: Sử dụng Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, yêu cầu Docker), rồi `azd provision` và `azd deploy`. Việc triển khai tác nhân lưu trữ yêu cầu vai trò **Foundry Project Manager**.

Phiên bản chạy được của ví dụ này có trong [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Để có hướng dẫn đầy đủ (giao thức Invocations, định dạng yêu cầu tùy chỉnh và xử lý sự cố), xem [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Mẫu mã

Mẫu mã cho Microsoft Agent Framework có thể tìm thấy trong kho lưu trữ này dưới các tệp `xx-python-agent-framework` và `xx-dotnet-agent-framework`.

## Còn câu hỏi gì về Microsoft Agent Framework?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ các học viên khác, tham gia giờ làm việc và nhận câu trả lời cho các câu hỏi về AI Agents.
## Bài học trước

[Bộ nhớ cho AI Agents](../13-agent-memory/README.md)

## Bài học kế tiếp

[Xây dựng tác nhân sử dụng máy tính (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->