# Khám Phá Microsoft Agent Framework

![Agent Framework](../../../translated_images/vi/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Giới Thiệu

Bài học này sẽ bao gồm:

- Hiểu về Microsoft Agent Framework: Các Tính Năng Chính và Giá Trị  
- Khám phá các Khái Niệm Chính của Microsoft Agent Framework
- Các Mẫu MAF Nâng Cao: Quy Trình Làm Việc, Middleware và Bộ Nhớ

## Mục Tiêu Học Tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

- Xây dựng các AI Agent sẵn sàng cho sản xuất sử dụng Microsoft Agent Framework
- Áp dụng các tính năng cốt lõi của Microsoft Agent Framework cho các trường hợp sử dụng Agentic của bạn
- Sử dụng các mẫu nâng cao bao gồm quy trình làm việc, middleware và khả năng quan sát

## Mẫu Mã Lệnh 

Các mẫu mã lệnh cho [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) có thể được tìm thấy trong kho lưu trữ này dưới các file `xx-python-agent-framework` và `xx-dotnet-agent-framework`.

## Hiểu Về Microsoft Agent Framework

![Framework Intro](../../../translated_images/vi/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) là khung làm việc thống nhất của Microsoft để xây dựng các AI agent. Nó cung cấp sự linh hoạt để giải quyết nhiều loại trường hợp sử dụng agentic đa dạng được thấy trong cả môi trường sản xuất và nghiên cứu bao gồm:

- **Điều phối Agent theo trình tự** trong các kịch bản cần quy trình công việc từng bước.
- **Điều phối Đồng thời** trong các kịch bản nơi các agent cần hoàn thành nhiệm vụ cùng lúc.
- **Điều phối Chat nhóm** trong các kịch bản nơi các agent có thể hợp tác cùng nhau trên một nhiệm vụ.
- **Điều phối Chuyển giao** trong các kịch bản nơi các agent chuyển giao nhiệm vụ cho nhau khi các phần nhiệm vụ phụ được hoàn thành.
- **Điều phối Từ Tính** trong các kịch bản nơi một agent quản lý tạo và chỉnh sửa danh sách nhiệm vụ và xử lý phối hợp các subagent để hoàn thành nhiệm vụ.

Để triển khai AI Agent trong Sản xuất, MAF cũng bao gồm các tính năng cho:

- **Khả năng Quan sát** thông qua việc sử dụng OpenTelemetry, nơi mỗi hành động của AI Agent bao gồm việc gọi công cụ, các bước điều phối, luồng lý luận và giám sát hiệu suất qua bảng điều khiển Microsoft Foundry.
- **Bảo mật** bằng cách lưu trữ agents trực tiếp trên Microsoft Foundry bao gồm các kiểm soát bảo mật như truy cập dựa trên vai trò, xử lý dữ liệu riêng tư và an toàn nội dung tích hợp sẵn.
- **Độ bền** khi các luồng và quy trình agent có thể tạm dừng, tiếp tục và phục hồi từ lỗi, điều này cho phép quy trình chạy lâu hơn.
- **Kiểm soát** khi các quy trình làm việc có con người tham gia được hỗ trợ, nơi nhiệm vụ được đánh dấu là cần phê duyệt con người.

Microsoft Agent Framework cũng tập trung vào khả năng tương tác bằng cách:

- **Độc lập Đám mây** - Các agent có thể chạy trong container, tại chỗ và trên nhiều đám mây khác nhau.
- **Độc lập Nhà cung cấp** - Các agent có thể được tạo ra qua SDK bạn ưa thích bao gồm Azure OpenAI và OpenAI
- **Tích hợp Chuẩn Mở** - Các agent có thể sử dụng các giao thức như Agent-to-Agent(A2A) và Model Context Protocol (MCP) để phát hiện và sử dụng các agent và công cụ khác.
- **Plugin và Kết nối** - Có thể kết nối với các dịch vụ dữ liệu và bộ nhớ như Microsoft Fabric, SharePoint, Pinecone và Qdrant.

Hãy cùng xem cách các tính năng này được áp dụng cho một số khái niệm cốt lõi của Microsoft Agent Framework.

## Các Khái Niệm Chính của Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/vi/agent-components.410a06daf87b4fef.webp)

**Tạo Agents**

Việc tạo agent được thực hiện bằng cách định nghĩa dịch vụ suy diễn (Nhà cung cấp LLM), một
bộ hướng dẫn cho AI Agent để theo dõi, và một `name` được gán:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Đoạn mã trên sử dụng `Azure OpenAI` nhưng agent có thể được tạo bằng nhiều dịch vụ khác nhau bao gồm `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

APIs OpenAI `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

hoặc [MiniMax](https://platform.minimaxi.com/), cung cấp API tương thích OpenAI với cửa sổ ngữ cảnh lớn (lên tới 204K token):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

hoặc agents từ xa sử dụng giao thức A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Chạy Agents**

Các agent được chạy sử dụng phương thức `.run` hoặc `.run_stream` cho phản hồi không phát trực tiếp hoặc phát trực tiếp.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Mỗi lần chạy agent cũng có thể có các tùy chọn tùy chỉnh các tham số như `max_tokens` được sử dụng bởi agent, `tools` mà agent có thể gọi, và thậm chí `model` được sử dụng cho agent.

Điều này hữu ích trong các trường hợp yêu cầu các mô hình hoặc công cụ cụ thể để hoàn thành nhiệm vụ của người dùng.

**Công Cụ**

Công cụ có thể được định nghĩa cả khi định nghĩa agent:

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

Luồng Agent được sử dụng để xử lý các cuộc trò chuyện nhiều lượt. Luồng có thể được tạo bằng cách:

- Sử dụng `get_new_thread()` cho phép lưu luồng theo thời gian
- Tự động tạo luồng khi chạy agent và chỉ giữ luồng trong lần chạy hiện tại.

Để tạo luồng, đoạn mã trông như sau:

```python
# Tạo một luồng mới.
thread = agent.get_new_thread() # Chạy tác nhân với luồng.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Bạn sau đó có thể tuần tự hóa luồng để lưu trữ cho lần sử dụng sau:

```python
# Tạo một luồng mới.
thread = agent.get_new_thread() 

# Chạy agent với luồng đó.

response = await agent.run("Hello, how are you?", thread=thread) 

# Tuần tự hóa luồng để lưu trữ.

serialized_thread = await thread.serialize() 

# Giải tuần tự trạng thái luồng sau khi tải từ lưu trữ.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware Agent**

Agents tương tác với công cụ và LLMs để hoàn thành nhiệm vụ của người dùng. Trong một số kịch bản, chúng ta muốn thực thi hoặc theo dõi giữa các tương tác này. Middleware agent cho phép điều này qua:

*Middleware Hàm*

Middleware này cho phép thực thi một hành động giữa agent và một hàm/công cụ mà nó sẽ gọi. Ví dụ khi bạn muốn ghi lại log cho cuộc gọi hàm.

Trong đoạn mã bên dưới, `next` xác định xem middleware tiếp theo hay hàm thật sự sẽ được gọi.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Tiền xử lý: Ghi nhật ký trước khi thực thi hàm
    print(f"[Function] Calling {context.function.name}")

    # Tiếp tục đến middleware hoặc thực thi hàm tiếp theo
    await next(context)

    # Hậu xử lý: Ghi nhật ký sau khi thực thi hàm
    print(f"[Function] {context.function.name} completed")
```

*Middleware Chat*

Middleware này cho phép thực thi hoặc ghi lại một hành động giữa agent và các yêu cầu giữa LLM.

Nó bao gồm thông tin quan trọng như `messages` được gửi tới dịch vụ AI.

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

**Bộ Nhớ Agent**

Như đã đề cập trong bài học `Agentic Memory`, bộ nhớ là yếu tố quan trọng giúp agent hoạt động qua các ngữ cảnh khác nhau. MAF cung cấp nhiều loại bộ nhớ khác nhau:

*Bộ Lưu Trữ Trong Bộ Nhớ*

Đây là bộ nhớ được lưu trong các luồng trong thời gian chạy ứng dụng.

```python
# Tạo một luồng mới.
thread = agent.get_new_thread() # Chạy tác nhân với luồng.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Tin Nhắn Bền Vững*

Bộ nhớ này được dùng khi lưu trữ lịch sử hội thoại qua các phiên khác nhau. Nó được định nghĩa bằng `chat_message_store_factory`:

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

Bộ nhớ này được thêm vào ngữ cảnh trước khi các agent được chạy. Các bộ nhớ này có thể được lưu trữ trong các dịch vụ bên ngoài như mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Sử dụng Mem0 cho các tính năng bộ nhớ nâng cao
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

**Khả Năng Quan Sát Agent**

Khả năng quan sát rất quan trọng để xây dựng các hệ thống agentic đáng tin cậy và dễ bảo trì. MAF tích hợp với OpenTelemetry để cung cấp giám sát và số đo cho khả năng quan sát tốt hơn.

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

MAF cung cấp các quy trình làm việc gồm các bước được định nghĩa trước để hoàn thành một nhiệm vụ và bao gồm các AI agent như các thành phần trong các bước đó.

Quy trình làm việc được tạo thành từ các thành phần khác nhau cho phép kiểm soát luồng tốt hơn. Đồng thời chúng cũng hỗ trợ **điều phối đa agent** và **checkpointing** để lưu trạng thái quy trình.

Các thành phần cốt lõi của một quy trình làm việc là:

**Executor (Bộ thực thi)**

Các executor nhận các tin nhắn đầu vào, thực hiện các nhiệm vụ được giao và sau đó tạo ra tin nhắn đầu ra. Điều này giúp quy trình tiến tới hoàn thành nhiệm vụ lớn hơn. Executor có thể là AI agent hoặc logic tùy chỉnh.

**Cạnh (Edges)**

Cạnh dùng để định nghĩa luồng gửi tin nhắn trong quy trình làm việc. Có thể là:

*Cạnh Trực Tiếp* - Kết nối một-nhất giản đơn giữa các executor:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Cạnh Điều Kiện* - Kích hoạt sau khi điều kiện nhất định được thỏa mãn. Ví dụ, khi phòng khách sạn không có sẵn, executor có thể gợi ý các lựa chọn khác.

*Cạnh Switch-case* - Định tuyến tin nhắn đến các executor khác nhau dựa trên điều kiện định nghĩa. Ví dụ, nếu khách hàng du lịch có quyền ưu tiên thì nhiệm vụ của họ sẽ được xử lý qua quy trình khác.

*Cạnh Fan-out* - Gửi một tin nhắn tới nhiều đích.

*Cạnh Fan-in* - Thu thập nhiều tin nhắn từ các executor khác nhau rồi gửi đến một đích.

**Sự Kiện**

Để cung cấp khả năng quan sát tốt hơn vào quy trình làm việc, MAF cung cấp các sự kiện tích hợp cho việc thực thi bao gồm:

- `WorkflowStartedEvent`  - Bắt đầu thực thi quy trình làm việc
- `WorkflowOutputEvent` - Quy trình làm việc tạo ra đầu ra
- `WorkflowErrorEvent` - Quy trình làm việc gặp lỗi
- `ExecutorInvokeEvent`  - Executor bắt đầu xử lý
- `ExecutorCompleteEvent`  -  Executor hoàn thành xử lý
- `RequestInfoEvent` - Một yêu cầu được gửi đi

## Các Mẫu MAF Nâng Cao

Các phần trên đã trình bày các khái niệm chính của Microsoft Agent Framework. Khi bạn xây dựng các agent phức tạp hơn, đây là một số mẫu nâng cao để cân nhắc:

- **Middleware Tích Hợp**: Chuỗi các bộ xử lý middleware (ghi log, xác thực, giới hạn tỷ lệ) sử dụng middleware hàm và chat để kiểm soát hành vi agent một cách chi tiết.
- **Checkpoint Quy Trình Làm Việc**: Sử dụng các sự kiện quy trình và tuần tự hóa để lưu và tiếp tục các quy trình agent chạy dài.
- **Chọn Công Cụ Động**: Kết hợp RAG qua mô tả công cụ với đăng ký công cụ của MAF để chỉ hiển thị các công cụ phù hợp cho từng truy vấn.
- **Chuyển Giao Đa Agent**: Sử dụng các cạnh quy trình và điều hướng có điều kiện để điều phối chuyển giao giữa các agent chuyên biệt.

## Lưu Trữ LangChain / LangGraph Agents trên Microsoft Foundry

Microsoft Agent Framework là **khung làm việc tương tác** — bạn không bị giới hạn bởi các agent viết với MAF. Nếu bạn đã có agent được xây dựng bằng **LangChain** hoặc **LangGraph**, bạn có thể chạy nó như một **agent được lưu trữ trên Microsoft Foundry** để Foundry quản lý runtime, phiên, mở rộng, nhận diện và điểm cuối giao thức cho bạn, trong khi logic agent của bạn vẫn ở LangGraph.

Việc này được thực hiện qua gói `langchain_azure_ai.agents.hosting`, cung cấp một đồ thị LangGraph biên dịch qua cùng các giao thức mà các agent lưu trữ Foundry sử dụng.

**1. Cài đặt phần mở rộng hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Phần mở rộng `hosting` cài đặt thư viện giao thức Foundry: `azure-ai-agentserver-responses` (điểm cuối `/responses` tương thích OpenAI) và `azure-ai-agentserver-invocations` (điểm cuối chung `/invocations`).

**2. Chọn giao thức lưu trữ:**

| Giao thức | Lớp Host | Điểm cuối | Sử dụng khi |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Bạn muốn chat tương thích OpenAI, streaming, lịch sử phản hồi, và luồng hội thoại — mặc định khuyến nghị cho các agent đối thoại. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Bạn cần định dạng JSON tùy chỉnh, điểm cuối kiểu webhook, hoặc xử lý không đối thoại. |

Vì **API Responses là API chính cho phát triển agent trong Foundry**, hãy bắt đầu với `ResponsesHostServer` cho hầu hết agent.

**3. Cấu hình các biến môi trường** (`az login` trước để `DefaultAzureCredential` có thể xác thực):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Khi agent sau này chạy như một agent được lưu trữ trong Foundry, nền tảng sẽ tự động tiêm `FOUNDRY_PROJECT_ENDPOINT`.

**4. Công khai agent LangGraph qua giao thức Responses:**

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

    # ChatOpenAI ở đây hướng tới điểm cuối (Responses) tương thích OpenAI của dự án Foundry.
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

Chạy nó cục bộ với `python main.py`, sau đó gửi yêu cầu Responses tới `http://localhost:8088/responses`.

**Các hành vi chính:**

- **Cuộc trò chuyện**: Khách hàng tiếp tục cuộc trò chuyện bằng cách truyền `previous_response_id` hoặc ID `conversation`. Nếu đồ thị của bạn được biên dịch với bộ checkpoint LangGraph, Foundry sẽ khóa trạng thái cuộc trò chuyện với checkpoint (hãy dùng checkpoint bền vững trong sản xuất; `MemorySaver` phù hợp để thử nghiệm cục bộ).
- **Con người tham gia**: Nếu đồ thị của bạn sử dụng LangGraph `interrupt()`, `ResponsesHostServer` sẽ hiển thị việc chờ xử lý interrupt như một mục `function_call` / `mcp_approval_request` của Responses, và khách hàng sẽ tiếp tục với `function_call_output` / `mcp_approval_response` tương ứng.
- **Triển khai tới Foundry**: Sử dụng Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (cục bộ, yêu cầu Docker), sau đó `azd provision` và `azd deploy`. Triển khai agent lưu trữ yêu cầu vai trò **Foundry Project Manager**.

Phiên bản chạy được của ví dụ này nằm trong [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Để xem hướng dẫn đầy đủ (giao thức Invocations, định dạng yêu cầu tùy chỉnh, và khắc phục sự cố), xem [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Mẫu Mã Lệnh 

Các mẫu mã lệnh cho Microsoft Agent Framework có thể được tìm thấy trong kho lưu trữ này dưới các tệp `xx-python-agent-framework` và `xx-dotnet-agent-framework`.

## Có Thêm Câu Hỏi Về Microsoft Agent Framework?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ những người học khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về AI Agents của bạn.
## Bài Học Trước

[Bộ Nhớ cho AI Agents](../13-agent-memory/README.md)

## Bài Học Tiếp Theo

[Xây Dựng Agents Sử Dụng Máy Tính (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->