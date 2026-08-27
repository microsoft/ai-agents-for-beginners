# Khám phá Microsoft Agent Framework

![Agent Framework](../../../translated_images/vi/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Giới thiệu

Bài học này sẽ đề cập đến:

- Hiểu về Microsoft Agent Framework: Các tính năng chính và giá trị  
- Khám phá các khái niệm chính của Microsoft Agent Framework
- Các mẫu nâng cao của MAF: Quy trình công việc, middleware và bộ nhớ

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

- Xây dựng các AI Agent sẵn sàng cho môi trường sản xuất sử dụng Microsoft Agent Framework
- Áp dụng các tính năng cốt lõi của Microsoft Agent Framework vào các trường hợp sử dụng Agentic của bạn
- Sử dụng các mẫu nâng cao bao gồm quy trình công việc, middleware và khả năng quan sát

## Mẫu mã code 

Các mẫu mã code cho [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) có thể được tìm thấy trong kho lưu trữ này dưới các tệp `xx-python-agent-framework` và `xx-dotnet-agent-framework`.

## Hiểu về Microsoft Agent Framework

![Framework Intro](../../../translated_images/vi/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) là framework hợp nhất của Microsoft để xây dựng các AI Agent. Nó cung cấp sự linh hoạt để giải quyết nhiều trường hợp sử dụng agentic đa dạng thấy trong cả môi trường sản xuất và nghiên cứu bao gồm:

- **Điều phối Agent theo tuần tự** trong các kịch bản cần quy trình từng bước.
- **Đồng thời điều phối** trong các kịch bản nơi các agent cần hoàn thành các công việc cùng lúc.
- **Điều phối nhóm chat** trong những kịch bản agent có thể hợp tác cùng nhau trên một tác vụ.
- **Điều phối chuyển giao** trong các kịch bản các agent chuyển giao tác vụ cho nhau khi các công việc phụ được hoàn thành.
- **Điều phối từ xa (Magnetic Orchestration)** trong các kịch bản một agent quản lý tạo và chỉnh sửa danh sách tác vụ và điều phối các subagent để hoàn thành tác vụ.

Để triển khai AI Agents trong môi trường Sản xuất, MAF cũng bao gồm các tính năng cho:

- **Khả năng quan sát** thông qua việc sử dụng OpenTelemetry, nơi mọi hành động của AI Agent bao gồm gọi công cụ, các bước điều phối, luồng suy luận và giám sát hiệu suất qua bảng điều khiển Microsoft Foundry.
- **Bảo mật** bằng cách lưu trữ agent trực tiếp trên Microsoft Foundry với các kiểm soát bảo mật như phân quyền theo vai trò, xử lý dữ liệu riêng tư và an toàn nội dung tích hợp.
- **Độ bền** vì các luồng và quy trình agent có thể tạm dừng, tiếp tục và khôi phục lỗi cho phép tiến trình chạy dài hơn.
- **Kiểm soát** khi hỗ trợ quy trình có sự can thiệp của con người với các tác vụ được đánh dấu cần phê duyệt bởi con người.

Microsoft Agent Framework cũng tập trung vào khả năng tương tác bằng cách:

- **Không phụ thuộc đám mây** - Agent có thể chạy trong container, tại chỗ và trên nhiều đám mây khác nhau.
- **Không phụ thuộc nhà cung cấp** - Agent có thể được tạo qua SDK yêu thích của bạn bao gồm Azure OpenAI và OpenAI
- **Tích hợp tiêu chuẩn mở** - Agent có thể sử dụng các giao thức như Agent-to-Agent (A2A) và Model Context Protocol (MCP) để khám phá và sử dụng agent và công cụ khác.
- **Plugin và Kết nối** - Kết nối có thể được thiết lập với các dịch vụ dữ liệu và bộ nhớ như Microsoft Fabric, SharePoint, Pinecone và Qdrant.

Hãy cùng xem cách các tính năng này được áp dụng trong một số khái niệm cốt lõi của Microsoft Agent Framework.

## Các khái niệm chính của Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/vi/agent-components.410a06daf87b4fef.webp)

**Tạo Agents**

Việc tạo agent được thực hiện bằng cách định nghĩa dịch vụ suy luận (Nhà cung cấp LLM), 
tập hợp các hướng dẫn cho AI Agent theo, và một `name` được gán:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Phía trên đang sử dụng `Azure OpenAI` nhưng agent có thể được tạo bằng nhiều dịch vụ khác nhau bao gồm `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, API `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

hoặc [MiniMax](https://platform.minimaxi.com/), cung cấp API tương thích OpenAI với các cửa sổ ngữ cảnh lớn (tối đa 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

hoặc agents từ xa sử dụng giao thức A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Chạy Agents**

Agents được chạy bằng các phương thức `.run` hoặc `.run_stream` cho phản hồi không streaming hoặc streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Mỗi lần chạy agent cũng có thể có các tuỳ chọn để tùy chỉnh các tham số như `max_tokens` được agent sử dụng, `tools` mà agent có thể gọi, và thậm chí mô hình `model` được dùng cho agent.

Điều này hữu ích trong các trường hợp yêu cầu mô hình hoặc công cụ cụ thể để hoàn thành tác vụ của người dùng.

**Công cụ**

Công cụ có thể được định nghĩa cả khi tạo agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Khi tạo một ChatAgent trực tiếp

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

và cũng khi chạy agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Công cụ chỉ được cung cấp cho lần chạy này thôi )
```

**Luồng Agent (Agent Threads)**

Agent Threads được sử dụng để xử lý các cuộc trò chuyện đa lượt. Luồng có thể được tạo bằng cách:

- Sử dụng `get_new_thread()` cho phép luồng được lưu lại theo thời gian
- Tự động tạo một luồng khi chạy agent và luồng chỉ tồn tại trong lần chạy hiện tại.

Để tạo luồng, mã nguồn như sau:

```python
# Tạo một luồng mới.
thread = agent.get_new_thread() # Chạy tác nhân với luồng đó.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Sau đó bạn có thể tuần tự hóa luồng để lưu trữ dùng sau:

```python
# Tạo một luồng mới.
thread = agent.get_new_thread() 

# Chạy tác nhân với luồng.

response = await agent.run("Hello, how are you?", thread=thread) 

# Chuẩn hóa luồng để lưu trữ.

serialized_thread = await thread.serialize() 

# Giải chuẩn hóa trạng thái luồng sau khi tải từ lưu trữ.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware của Agent**

Agents tương tác với công cụ và LLM để hoàn thành các tác vụ của người dùng. Trong một số tình huống, chúng ta muốn thực thi hoặc theo dõi giữa các tương tác này. Middleware của agent cho phép chúng ta làm điều này thông qua:

*Middleware chức năng*

Middleware này cho phép thực hiện một hành động giữa agent và một hàm/công cụ mà nó sẽ gọi. Ví dụ khi bạn muốn ghi lại nhật ký cuộc gọi hàm.

Trong đoạn mã dưới đây `next` xác định liệu middleware kế tiếp hoặc chính hàm thực sự có được gọi.

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

*Middleware chat*

Middleware này cho phép thực thi hoặc ghi nhật ký hành động giữa agent và các yêu cầu gửi đến LLM.

Điều này chứa các thông tin quan trọng như các `messages` được gửi đến dịch vụ AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Tiền xử lý: Ghi nhật ký trước cuộc gọi AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Tiếp tục đến middleware hoặc dịch vụ AI tiếp theo
    await next(context)

    # Hậu xử lý: Ghi nhật ký sau phản hồi của AI
    print("[Chat] AI response received")

```

**Bộ nhớ của Agent**

Như đã trình bày trong bài học `Agentic Memory`, bộ nhớ là yếu tố quan trọng giúp agent hoạt động trên các ngữ cảnh khác nhau. MAF cung cấp nhiều loại bộ nhớ khác nhau:

*Bộ nhớ trong phiên làm việc*

Đây là bộ nhớ lưu trong các luồng trong quá trình chạy ứng dụng.

```python
# Tạo một luồng mới.
thread = agent.get_new_thread() # Chạy tác nhân với luồng.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Tin nhắn bền vững*

Bộ nhớ này được sử dụng để lưu lịch sử hội thoại qua các phiên khác nhau. Nó được định nghĩa bằng `chat_message_store_factory`:

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

Bộ nhớ này được thêm vào ngữ cảnh trước khi các agents được chạy. Các bộ nhớ này có thể được lưu trong dịch vụ bên ngoài như mem0:

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

**Khả năng quan sát của Agent**

Khả năng quan sát rất quan trọng để xây dựng hệ thống agent có độ tin cậy và dễ bảo trì. MAF tích hợp với OpenTelemetry để cung cấp việc theo dõi và đo đếm giúp quan sát tốt hơn.

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

### Quy trình công việc (Workflows)

MAF cung cấp các quy trình công việc là các bước được định nghĩa sẵn để hoàn thành một tác vụ và bao gồm các AI agents như các thành phần trong đó.

Quy trình công việc gồm các thành phần khác nhau cho phép kiểm soát luồng tốt hơn. Quy trình cũng hỗ trợ **điều phối đa-agent** và **điểm kiểm tra** để lưu trạng thái workflow.

Các thành phần cốt lõi của một workflow là:

**Executor**

Các executor nhận thông điệp đầu vào, thực hiện nhiệm vụ được giao và sinh ra tin nhắn đầu ra. Điều này làm workflow tiến tới hoàn thành tác vụ lớn hơn. Executor có thể là agent AI hoặc logic tùy chỉnh.

**Edges**

Edges dùng để định nghĩa luồng của thông điệp trong workflow. Nó có thể là:

*Edges trực tiếp* - Kết nối một-nhất giản đơn giữa các executor:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Edges có điều kiện* - Kích hoạt sau khi điều kiện nhất định được đáp ứng. Ví dụ, khi phòng khách sạn không còn, một executor có thể đề xuất các lựa chọn khác.

*Edges switch-case* - Chuyển hướng thông điệp đến executor khác nhau dựa trên điều kiện định nghĩa. Ví dụ, nếu khách du lịch có quyền ưu tiên, tác vụ của họ sẽ xử lý qua workflow khác.

*Edges fan-out* - Gửi một tin nhắn tới nhiều đích.

*Edges fan-in* - Thu thập nhiều tin nhắn từ các executor khác nhau và gửi đến một đích.

**Sự kiện**

Để cung cấp khả năng quan sát tốt hơn cho workflow, MAF có sẵn các sự kiện thực thi bao gồm:

- `WorkflowStartedEvent`  - Bắt đầu thực thi workflow
- `WorkflowOutputEvent` - Workflow sinh ra kết quả đầu ra
- `WorkflowErrorEvent` - Workflow gặp lỗi
- `ExecutorInvokeEvent`  - Executor bắt đầu xử lý
- `ExecutorCompleteEvent`  -  Executor hoàn thành xử lý
- `RequestInfoEvent` - Có yêu cầu được gửi

## Các mẫu nâng cao của MAF

Các phần trên trình bày các khái niệm chính của Microsoft Agent Framework. Khi bạn xây dựng các agent phức tạp hơn, dưới đây là một số mẫu nâng cao để xem xét:

- **Composition Middleware**: Liên kết nhiều middleware xử lý (ghi nhật ký, xác thực, giới hạn tần suất) sử dụng middleware chức năng và chat để kiểm soát chi tiết hành vi agent.
- **Chấm điểm checkpoint workflow**: Sử dụng sự kiện workflow và tuần tự hóa để lưu và tiếp tục quy trình agent chạy lâu.
- **Lựa chọn công cụ động**: Kết hợp RAG trên mô tả công cụ với đăng ký công cụ của MAF để trình bày chỉ các công cụ liên quan mỗi truy vấn.
- **Chuyển giao đa-agent**: Sử dụng edge workflow và điều hướng có điều kiện để điều phối chuyển giao giữa các agent chuyên biệt.

## Lưu trữ LangChain / LangGraph Agents trên Microsoft Foundry

Microsoft Agent Framework là **framework tương tác được** — bạn không bị giới hạn với các agent viết bằng MAF. Nếu bạn đã có một agent xây dựng với **LangChain** hoặc **LangGraph**, bạn có thể chạy nó như một **agent được host trên Microsoft Foundry** để Foundry quản lý runtime, phiên, scaling, định danh và các điểm cuối giao thức cho bạn, trong khi logic của agent vẫn nằm trong LangGraph.

Việc này được thực hiện với gói `langchain_azure_ai.agents.hosting`, cung cấp một đồ thị LangGraph đã biên dịch thông qua cùng giao thức mà agent được host trên Foundry sử dụng.

**1. Cài đặt phần mở rộng hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Phần mở rộng `hosting` cài đặt các thư viện giao thức Foundry: `azure-ai-agentserver-responses` (điểm cuối `/responses` tương thích OpenAI) và `azure-ai-agentserver-invocations` (điểm cuối tổng quát `/invocations`).

**2. Chọn giao thức hosting:**

| Giao thức | Lớp Host | Điểm cuối | Dùng khi |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Bạn muốn chat tương thích OpenAI, streaming, lịch sử phản hồi và luồng hội thoại — lựa chọn mặc định được khuyến nghị cho agent hội thoại. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Bạn cần định dạng JSON tùy chỉnh, điểm cuối kiểu webhook, hoặc xử lý không hội thoại. |

Vì **API Responses là API chính cho phát triển kiểu agent trên Foundry**, bắt đầu với `ResponsesHostServer` cho hầu hết các agent.

**3. Cấu hình biến môi trường** (`az login` trước để `DefaultAzureCredential` có thể xác thực):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Khi agent chạy sau này như một agent host trên Foundry, nền tảng sẽ tự động chèn `FOUNDRY_PROJECT_ENDPOINT`.

**4. Triển khai agent LangGraph qua giao thức Responses:**

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

    # ChatOpenAI ở đây hướng tới điểm cuối OpenAI-compatible (Responses) của dự án Foundry.
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

Chạy cục bộ bằng `python main.py`, sau đó gửi yêu cầu Responses đến `http://localhost:8088/responses`.

**Hành vi chính:**

- **Hội thoại**: Client tiếp tục một cuộc hội thoại bằng cách truyền `previous_response_id` hoặc ID `conversation`. Nếu đồ thị của bạn được biên dịch với bộ điểm kiểm tra LangGraph, Foundry sẽ khóa trạng thái hội thoại vào điểm kiểm tra (dùng bộ điểm kiểm tra bền vững trong sản xuất; `MemorySaver` dùng được cho thử nghiệm cục bộ).
- **Con người trong vòng lặp**: Nếu đồ thị của bạn sử dụng LangGraph `interrupt()`, `ResponsesHostServer` sẽ hiển thị ngắt đang chờ dưới dạng mục `function_call` / `mcp_approval_request` của Responses, và client tiếp tục với `function_call_output` / `mcp_approval_response` tương ứng.
- **Triển khai trên Foundry**: Sử dụng Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (chạy cục bộ, yêu cầu Docker), rồi `azd provision` và `azd deploy`. Việc triển khai agent được host đòi hỏi vai trò **Foundry Project Manager**.

Phiên bản có thể chạy của ví dụ này nằm trong [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Để xem hướng dẫn đầy đủ (giao thức Invocations, schema yêu cầu tùy chỉnh, và xử lý sự cố), xem [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Mẫu mã code 

Mẫu mã code cho Microsoft Agent Framework có thể được tìm thấy trong kho lưu trữ này dưới các tệp `xx-python-agent-framework` và `xx-dotnet-agent-framework`.

## Có thêm câu hỏi về Microsoft Agent Framework?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ các học viên khác, tham dự giờ làm việc và nhận được câu trả lời cho các thắc mắc về AI Agents.
## Bài học trước

[Bộ nhớ cho AI Agents](../13-agent-memory/README.md)

## Bài học tiếp theo

[Xây dựng Agents sử dụng máy tính (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->