# Microsoft Agent Framework 살펴보기

![에이전트 프레임워크](../../../translated_images/ko/lesson-14-thumbnail.90df0065b9d234ee.webp)

### 소개

이 수업에서는 다음을 다룹니다:

- Microsoft Agent Framework 이해하기: 주요 기능 및 가치  
- Microsoft Agent Framework의 핵심 개념 살펴보기
- 고급 MAF 패턴: 워크플로우, 미들웨어, 메모리

## 학습 목표

이 수업을 완료하면 다음을 할 수 있게 됩니다:

- Microsoft Agent Framework를 사용하여 프로덕션 준비가 된 AI 에이전트를 구축하기
- 에이전틱 사용 사례에 Microsoft Agent Framework의 핵심 기능 적용하기
- 워크플로우, 미들웨어, 관찰성(Observability) 등을 포함한 고급 패턴 사용하기

## 코드 샘플

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok)의 코드 샘플은 이 저장소의 `xx-python-agent-framework` 및 `xx-dotnet-agent-framework` 파일에서 찾을 수 있습니다.

## Microsoft Agent Framework 이해하기

![프레임워크 소개](../../../translated_images/ko/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok)는 AI 에이전트를 구축하기 위한 Microsoft의 통합 프레임워크입니다. 생산 환경과 연구 환경 모두에서 볼 수 있는 다양한 에이전틱 사용 사례를 해결할 수 있는 유연성을 제공합니다. 예를 들면 다음과 같습니다:

- **순차적 에이전트 오케스트레이션**: 단계별 워크플로우가 필요한 시나리오에서 사용됩니다.
- **동시 오케스트레이션**: 에이전트들이 동시에 작업을 완료해야 하는 시나리오에서 사용됩니다.
- **그룹 채팅 오케스트레이션**: 여러 에이전트가 하나의 작업에서 함께 협력할 수 있는 시나리오에서 사용됩니다.
- **핸드오프 오케스트레이션**: 하위 작업이 완료됨에 따라 에이전트들이 작업을 서로 넘겨주는 시나리오에서 사용됩니다.
- **마그네틱 오케스트레이션**: 매니저 에이전트가 작업 목록을 생성 및 수정하고 하위 에이전트들의 조정을 처리하여 작업을 완료하는 시나리오에서 사용됩니다.

프로덕션에서 AI 에이전트를 제공하기 위해, MAF는 또한 다음과 같은 기능을 포함합니다:

- **관찰성(Observability)**: OpenTelemetry를 사용하여 도구 호출, 오케스트레이션 단계, 추론 흐름 및 Microsoft Foundry 대시보드를 통한 성능 모니터링을 포함한 에이전트의 모든 작업을 추적합니다.
- **보안(Security)**: 역할 기반 접근, 개인 데이터 처리 및 내장된 콘텐츠 안전성 같은 보안 제어를 포함하는 Microsoft Foundry에 에이전트를 네이티브로 호스팅합니다.
- **내구성(Durability)**: 에이전트 스레드와 워크플로우는 일시 중지, 재개 및 오류 복구가 가능하여 장기간 실행되는 프로세스를 지원합니다.
- **제어(Control)**: 작업이 인간의 승인을 필요로 하는 것으로 표시되는 휴먼 인 더 루프 워크플로우를 지원합니다.

Microsoft Agent Framework는 또한 상호 운용성에 중점을 두고 있습니다:

- **클라우드 비종속성(Being Cloud-agnostic)** - 에이전트는 컨테이너, 온프레미스 및 여러 다른 클라우드에서 실행될 수 있습니다.
- **제공자 비종속성(Being Provider-agnostic)** - 에이전트는 Azure OpenAI 및 OpenAI를 포함한 선호하는 SDK를 통해 생성할 수 있습니다.
- **오픈 표준 통합(Integrating Open Standards)** - 에이전트는 다른 에이전트와 도구를 발견하고 사용할 수 있도록 Agent-to-Agent(A2A) 및 Model Context Protocol (MCP) 같은 프로토콜을 활용할 수 있습니다.
- **플러그인 및 커넥터(Plugins and Connectors)** - Microsoft Fabric, SharePoint, Pinecone 및 Qdrant와 같은 데이터 및 메모리 서비스에 연결할 수 있습니다.

이제 이러한 기능이 Microsoft Agent Framework의 몇 가지 핵심 개념에 어떻게 적용되는지 살펴보겠습니다.

## Microsoft Agent Framework의 핵심 개념

### 에이전트

![에이전트 프레임워크](../../../translated_images/ko/agent-components.410a06daf87b4fef.webp)

**에이전트 생성하기**

에이전트 생성은 추론 서비스(LLM 제공자), 에이전트가 따라야 할 지침 세트, 그리고 할당된 `name`을 정의하여 수행됩니다:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

위 예시는 `Azure OpenAI`를 사용하고 있지만, 에이전트는 `Microsoft Foundry Agent Service`를 포함한 다양한 서비스로 생성할 수 있습니다:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

또는 A2A 프로토콜을 사용하는 원격 에이전트:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**에이전트 실행하기**

에이전트는 비스트리밍 또는 스트리밍 응답을 위해 `.run` 또는 `.run_stream` 메서드를 사용하여 실행됩니다.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

각 에이전트 실행에는 에이전트가 사용하는 `max_tokens`와 같은 매개변수, 에이전트가 호출할 수 있는 `tools`, 심지어 에이전트에 사용되는 `model` 자체와 같은 옵션을 사용자 정의할 수 있는 옵션이 있을 수 있습니다.

이는 특정 모델이나 도구가 사용자의 작업을 완료하는 데 필요할 때 유용합니다.

**도구(도구들)**

도구는 에이전트를 정의할 때 다음과 같이 정의할 수 있습니다:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgent를 직접 생성할 때

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

또한 에이전트를 실행할 때 다음과 같이 정의할 수 있습니다:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # 이번 실행에만 제공된 도구 )
```

**에이전트 스레드**

에이전트 스레드는 다회차 대화를 처리하는 데 사용됩니다. 스레드는 다음 중 하나로 생성할 수 있습니다:

- 시간이 지남에 따라 스레드를 저장할 수 있게 하는 `get_new_thread()` 사용
- 에이전트를 실행할 때 자동으로 스레드를 생성하고 해당 스레드가 현재 실행 동안에만 지속되게 하기

스레드를 생성하는 코드는 다음과 같습니다:

```python
# 새 스레드를 생성합니다.
thread = agent.get_new_thread() # 해당 스레드에서 에이전트를 실행합니다.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

그런 다음 스레드를 직렬화하여 나중에 저장할 수 있습니다:

```python
# 새 스레드를 생성합니다.
thread = agent.get_new_thread() 

# 스레드와 함께 에이전트를 실행합니다.

response = await agent.run("Hello, how are you?", thread=thread) 

# 저장을 위해 스레드를 직렬화합니다.

serialized_thread = await thread.serialize() 

# 저장소에서 로드한 후 스레드 상태를 역직렬화합니다.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**에이전트 미들웨어**

에이전트는 사용자의 작업을 완료하기 위해 도구와 LLM과 상호작용합니다. 특정 시나리오에서는 이러한 상호작용 사이에 실행하거나 추적하고자 할 때가 있습니다. 에이전트 미들웨어는 다음을 통해 이를 가능하게 합니다:

*함수(Function) 미들웨어*

이 미들웨어는 에이전트가 호출할 함수/도구와의 사이에서 동작을 실행할 수 있게 합니다. 예를 들어 함수 호출에 대해 로깅을 하고자 할 때 사용될 수 있습니다.

아래 코드에서 `next`는 다음 미들웨어나 실제 함수가 호출되어야 하는지를 정의합니다.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # 사전 처리: 함수 실행 전에 로그 기록
    print(f"[Function] Calling {context.function.name}")

    # 다음 미들웨어 또는 함수 실행으로 계속 진행
    await next(context)

    # 사후 처리: 함수 실행 후 로그 기록
    print(f"[Function] {context.function.name} completed")
```

*채팅(Chat) 미들웨어*

이 미들웨어는 에이전트와 LLM 사이의 요청 사이에서 동작을 실행하거나 로깅할 수 있게 합니다.

여기에는 AI 서비스로 전송되는 `messages`와 같은 중요한 정보가 포함됩니다.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # 전처리: AI 호출 전에 로그 기록
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # 다음 미들웨어 또는 AI 서비스로 계속 진행
    await next(context)

    # 후처리: AI 응답 후 로그 기록
    print("[Chat] AI response received")

```

**에이전트 메모리**

`Agentic Memory` 수업에서 다루었듯이, 메모리는 에이전트가 다양한 컨텍스트에서 작동할 수 있게 하는 중요한 요소입니다. MAF는 여러 종류의 메모리를 제공합니다:

*인메모리 저장(In-Memory Storage)*

이는 애플리케이션 런타임 동안 스레드에 저장되는 메모리입니다.

```python
# 새 스레드를 생성합니다.
thread = agent.get_new_thread() # 스레드와 함께 에이전트를 실행합니다.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*영구 메시지(Persistent Messages)*

이 메모리는 서로 다른 세션에 걸쳐 대화 기록을 저장할 때 사용됩니다. `chat_message_store_factory`를 사용하여 정의됩니다:

```python
from agent_framework import ChatMessageStore

# 사용자 정의 메시지 저장소를 만듭니다
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*동적 메모리(Dynamic Memory)*

이 메모리는 에이전트를 실행하기 전에 컨텍스트에 추가됩니다. 이러한 메모리는 mem0와 같은 외부 서비스에 저장될 수 있습니다:

```python
from agent_framework.mem0 import Mem0Provider

# 고급 메모리 기능을 위해 Mem0을 사용
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

**에이전트 관찰성(Observability)**

관찰성은 신뢰할 수 있고 유지 관리 가능한 에이전틱 시스템을 구축하는 데 중요합니다. MAF는 추적 및 계측을 제공하기 위해 OpenTelemetry와 통합됩니다.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # 무언가를 수행
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### 워크플로우

MAF는 미리 정의된 단계로 작업을 완료하고 그 단계들에 AI 에이전트를 구성 요소로 포함하는 워크플로우를 제공합니다.

워크플로우는 더 나은 제어 흐름을 가능하게 하는 다양한 구성 요소로 구성됩니다. 워크플로우는 또한 **다중 에이전트 오케스트레이션** 및 워크플로우 상태를 저장하는 **체크포인팅**을 가능하게 합니다.

워크플로우의 핵심 구성 요소는 다음과 같습니다:

**실행기(Executors)**

실행기는 입력 메시지를 받아 할당된 작업을 수행한 다음 출력 메시지를 생성합니다. 이는 더 큰 작업을 완료하는 쪽으로 워크플로우를 전진시킵니다. 실행기는 AI 에이전트이거나 사용자 정의 로직일 수 있습니다.

**엣지(Edges)**

엣지는 워크플로우에서 메시지의 흐름을 정의하는 데 사용됩니다. 이는 다음과 같을 수 있습니다:

*직접 엣지(Direct Edges)* - 실행기 간의 단순한 일대일 연결:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*조건 엣지(Conditional Edges)* - 특정 조건이 충족된 후 활성화됩니다. 예를 들어 호텔 객실이 이용 불가일 때 실행기가 다른 옵션을 제안할 수 있습니다.

*스위치-케이스 엣지(Switch-case Edges)* - 정의된 조건에 따라 메시지를 다른 실행기로 라우팅합니다. 예를 들어, 여행 고객이 우선 접근 권한이 있고 그들의 작업이 다른 워크플로우를 통해 처리되는 경우 등입니다.

*팬아웃 엣지(Fan-out Edges)* - 하나의 메시지를 여러 대상에게 보냅니다.

*팬인 엣지(Fan-in Edges)* - 다양한 실행기들로부터 여러 메시지를 수집하여 하나의 대상으로 보냅니다.

**이벤트(Events)**

워크플로우에 대한 더 나은 관찰성을 제공하기 위해, MAF는 실행을 위한 내장 이벤트를 제공합니다. 예를 들면 다음과 같습니다:

- `WorkflowStartedEvent`  - 워크플로우 실행 시작
- `WorkflowOutputEvent` - 워크플로우가 출력 생성
- `WorkflowErrorEvent` - 워크플로우가 오류를 만남
- `ExecutorInvokeEvent`  - 실행기가 처리를 시작함
- `ExecutorCompleteEvent`  - 실행기가 처리를 완료함
- `RequestInfoEvent` - 요청이 발행됨

## 고급 MAF 패턴

위 섹션들은 Microsoft Agent Framework의 핵심 개념을 다루었습니다. 더 복잡한 에이전트를 구축할 때 고려할 수 있는 고급 패턴은 다음과 같습니다:

- **미들웨어 구성(Middleware Composition)**: 함수 및 채팅 미들웨어를 사용하여 여러 미들웨어 핸들러(로깅, 인증, 속도 제한)를 체인하여 에이전트 동작에 대한 세밀한 제어를 제공합니다.
- **워크플로우 체크포인팅(Workflow Checkpointing)**: 워크플로우 이벤트 및 직렬화를 사용하여 장기 실행 에이전트 프로세스를 저장하고 재개합니다.
- **동적 도구 선택(Dynamic Tool Selection)**: 도구 설명에 대한 RAG와 MAF의 도구 등록을 결합하여 쿼리별로 관련 도구만 제시합니다.
- **다중 에이전트 핸드오프(Multi-Agent Handoff)**: 워크플로우 엣지 및 조건부 라우팅을 사용하여 전문화된 에이전트 간의 핸드오프를 오케스트레이션합니다.

## 코드 샘플

Microsoft Agent Framework의 코드 샘플은 이 저장소의 `xx-python-agent-framework` 및 `xx-dotnet-agent-framework` 파일에서 찾을 수 있습니다.

## Microsoft Agent Framework에 대해 더 궁금한 점이 있나요?

다른 학습자들과 만나고 오피스 아워에 참석하며 AI 에이전트 관련 질문에 대한 답변을 얻으려면 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)에 참여하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 사항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나 자동 번역은 오류나 부정확성을 포함할 수 있음을 유의해 주시기 바랍니다. 원문(원어)의 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생한 오해나 잘못된 해석에 대해서는 당사가 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->