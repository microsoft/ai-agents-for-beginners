# Microsoft Agent Framework Workflow를 사용한 다중 에이전트 애플리케이션 구축

이 튜토리얼에서는 Microsoft Agent Framework를 사용하여 다중 에이전트 애플리케이션을 이해하고 구축하는 방법을 안내합니다. 다중 에이전트 시스템의 핵심 개념을 탐구하고, 프레임워크의 Workflow 구성 요소 아키텍처를 살펴보며, 다양한 워크플로우 패턴에 대해 Python과 .NET에서의 실용적인 예제를 함께 살펴봅니다.

## 1\. 다중 에이전트 시스템 이해하기

AI 에이전트는 표준 대형 언어 모델(LLM)의 능력을 넘어서는 시스템입니다. 환경을 인지하고, 결정을 내리며, 특정 목표를 달성하기 위해 행동을 취할 수 있습니다. 다중 에이전트 시스템은 여러 에이전트가 협력하여 단일 에이전트가 혼자 처리하기 어렵거나 불가능한 문제를 해결하는 것을 말합니다.

### 일반적인 적용 사례

  * **복잡한 문제 해결**: 대규모 작업(예: 회사 전체 이벤트 계획)을 전문화된 에이전트(예: 예산 에이전트, 물류 에이전트, 마케팅 에이전트)가 처리하는 더 작은 하위 작업으로 나누기.
  * **가상 비서**: 주 에이전트가 일정 관리, 조사, 예약 등의 작업을 다른 전문 에이전트에게 위임하기.
  * **자동 콘텐츠 생성**: 한 에이전트가 초안을 작성하고, 또 다른 에이전트가 정확성과 톤을 검토하며, 세 번째 에이전트가 출판까지 하는 워크플로우.

### 다중 에이전트 패턴

다중 에이전트 시스템은 상호작용 방식을 결정하는 여러 패턴으로 구성될 수 있습니다:

  * **순차적(Sequential)**: 에이전트들이 정해진 순서대로 작업하며, 한 에이전트의 출력이 다음 에이전트의 입력이 됩니다.
  * **병행적(Concurrent)**: 에이전트들이 작업의 다른 부분을 병렬로 처리하고, 결과를 최종적으로 합산합니다.
  * **조건부(Conditional)**: 에이전트 출력에 따라 워크플로우가 다른 경로로 분기하며, if-then-else 문과 유사합니다.

## 2\. Microsoft Agent Framework Workflow 아키텍처

Agent Framework의 워크플로우 시스템은 복잡한 다중 에이전트 간 상호작용을 관리하는 고급 오케스트레이션 엔진입니다. [Pregel 스타일 실행 모델](https://kowshik.github.io/JPregel/pregel_paper.pdf)을 기반으로 한 그래프 기반 아키텍처로, “슈퍼스텝”이라고 불리는 동기화된 단계에서 처리가 이루어집니다.

### 핵심 구성 요소

아키텍처는 세 부분으로 구성됩니다:

1.  **실행자(Executors)**: 기본 처리 단위입니다. 예제에서는 `Agent`가 실행자의 한 종류입니다. 각 실행자는 수신된 메시지 유형에 따라 자동으로 호출되는 여러 메시지 핸들러를 가질 수 있습니다.
2.  **엣지(Edges)**: 실행자 간 메시지 경로를 정의합니다. 조건부가 있을 수 있어, 워크플로우 그래프에서 동적인 정보 라우팅이 가능합니다.
3.  **워크플로우(Workflow)**: 전체 프로세스를 조율하며, 실행자, 엣지, 전체 실행 흐름을 관리합니다. 메시지가 올바른 순서로 처리되도록 보장하며, 이벤트 스트림을 제공해 관찰 가능성을 지원합니다.

*워크플로우 시스템의 핵심 구성 요소를 보여주는 다이어그램.*

이 구조를 통해 순차 체인, 병렬 처리용 팬 아웃/팬 인, 조건부 흐름용 스위치 케이스 논리와 같은 기본 패턴을 사용해 견고하고 확장 가능한 애플리케이션을 구축할 수 있습니다.

## 3\. 실용적인 예제 및 코드 분석

이제 프레임워크를 사용해 다양한 워크플로우 패턴을 구현하는 방법을 살펴보겠습니다. 각 예제에 대해 Python과 .NET 코드를 모두 확인합니다.

### 사례 1: 기본 순차 워크플로우

가장 간단한 패턴으로, 한 에이전트의 출력이 직접 다른 에이전트로 전달됩니다. 시나리오는 호텔 `FrontDesk` 에이전트가 여행 추천을 하고, `Concierge` 에이전트가 이를 검토하는 것입니다.

*기본 FrontDesk -> Concierge 워크플로우 다이어그램.*

#### 시나리오 배경

여행자가 파리에서 추천을 요청합니다.

1.  간결하게 설계된 `FrontDesk` 에이전트가 루브르 박물관 방문을 제안합니다.
2.  진정한 경험을 중시하는 `Concierge` 에이전트가 제안을 받아 검토 후, 더 지역적이고 관광객이 적은 대안을 제시합니다.

#### Python 구현 분석

Python 예제에서는 먼저 각기 특정 지침을 가진 두 에이전트를 정의하고 생성합니다.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# 에이전트 역할과 지침 정의
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# 에이전트 인스턴스 생성
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

다음으로 `WorkflowBuilder`를 사용해 그래프를 구성합니다. `front_desk_agent`를 시작점으로 설정하고, 그 출력이 `reviewer_agent`로 연결되도록 엣지를 생성합니다.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

마지막으로 초기 사용자 프롬프트와 함께 워크플로우를 실행합니다.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run은 워크플로우를 실행합니다; get_outputs()는 출력 실행기의 결과를 반환합니다.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) 구현 분석

.NET 구현도 매우 유사한 논리를 따릅니다. 먼저 에이전트 이름과 지침에 대한 상수를 정의합니다.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

`AzureOpenAIClient`(Responses API)를 이용해 에이전트를 생성한 후, `WorkflowBuilder`가 `frontDeskAgent`에서 `reviewerAgent`로의 순차 흐름을 나타내는 엣지를 추가합니다.

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

그런 다음 사용자의 메시지로 워크플로우를 실행하고, 결과를 스트리밍 방식으로 받습니다.

### 사례 2: 다단계 순차 워크플로우

이 패턴은 기본 순차를 확장해 더 많은 에이전트를 포함합니다. 여러 단계의 정제나 변환이 필요한 프로세스에 적합합니다.

#### 시나리오 배경

사용자가 거실 이미지를 제공하고 가구 견적을 요청합니다.

1.  **Sales-Agent**: 이미지 내 가구 항목을 식별하고 목록을 작성합니다.
2.  **Price-Agent**: 항목 목록을 받아 예산, 중간, 프리미엄 옵션을 포함한 상세 가격 내역을 제공합니다.
3.  **Quote-Agent**: 가격이 매겨진 목록을 받아 Markdown 형식의 공식 견적 문서로 구성합니다.

*Sales -> Price -> Quote 워크플로우 다이어그램.*

#### Python 구현 분석

세 에이전트를 각각 전문화된 역할로 정의합니다. `add_edge`를 사용해 `sales_agent` -> `price_agent` -> `quote_agent` 체인을 만듭니다.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# 세 가지 전문 에이전트 생성
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# 순차 워크플로우 구축
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

입력은 텍스트와 이미지 URI가 포함된 `ChatMessage`입니다. 프레임워크가 각 에이전트 출력물을 순서대로 다음 에이전트에게 전달해 최종 견적이 만들어질 때까지 처리합니다.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# 사용자 메시지는 텍스트와 이미지를 모두 포함합니다
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# 워크플로우를 실행하십시오
events = await workflow.run(message)
```

#### .NET (C\#) 구현 분석

.NET 예제도 Python 버전을 반영합니다. 세 에이전트(`salesagent`, `priceagent`, `quoteagent`)를 생성하고, `WorkflowBuilder`가 이를 차례대로 연결합니다.

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

사용자의 메시지는 이미지 데이터(바이트)와 텍스트 프롬프트를 모두 포함합니다. `InProcessExecution.RunStreamingAsync` 메서드가 워크플로우를 시작하고, 최종 출력은 스트림에서 캡처됩니다.

### 사례 3: 병행 워크플로우

이 패턴은 작업을 동시에 수행해 시간을 절약할 때 사용됩니다. 여러 에이전트에 "팬 아웃"하고, 결과를 모으는 "팬 인"을 포함합니다.

#### 시나리오 배경

사용자가 시애틀 여행 계획을 요청합니다.

1.  **Dispatcher (팬 아웃)**: 사용자의 요청이 동시에 두 에이전트에 전송됩니다.
2.  **Researcher-Agent**: 12월 시애틀 여행의 명소, 날씨 및 주요 고려사항을 조사합니다.
3.  **Plan-Agent**: 상세한 일별 여행 일정을 독립적으로 작성합니다.
4.  **Aggregator (팬 인)**: 연구원과 플래너 두 에이전트의 결과물을 수집해 최종 결과로 제시합니다.

*병행 Researcher와 Planner 워크플로우 다이어그램.*

#### Python 구현 분석

`ConcurrentBuilder`는 이 패턴 생성을 간소화합니다. 참여 에이전트를 나열하기만 하면, 팬 아웃과 팬 인 논리를 자동으로 생성합니다.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder는 팬아웃/팬인 로직을 처리합니다
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# 워크플로우 실행하기
events = await workflow.run("Plan a trip to Seattle in December")
```

프레임워크는 `research_agent`와 `plan_agent`가 병렬로 실행되도록 보장하며, 이들의 최종 결과를 리스트로 수집합니다.

#### .NET (C\#) 구현 분석

.NET에서는 이 패턴에 대해 더 명시적인 정의가 필요합니다. 팬 아웃과 팬 인 논리를 처리할 사용자 정의 실행자(`ConcurrentStartExecutor` 및 `ConcurrentAggregationExecutor`)를 생성합니다.

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

이후 `WorkflowBuilder`가 `AddFanOutEdge`와 `AddFanInEdge`를 사용해 이들 사용자 정의 실행자와 에이전트로 그래프를 구성합니다.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### 사례 4: 조건부 워크플로우

조건부 워크플로우는 분기 논리를 도입해 중간 결과에 따라 다른 경로를 취할 수 있도록 합니다.

#### 시나리오 배경

이 워크플로우는 기술 튜토리얼 작성과 출판을 자동화합니다.

1.  **Evangelist-Agent**: 주어진 개요와 URL을 바탕으로 튜토리얼 초안을 작성합니다.
2.  **ContentReviewer-Agent**: 초안을 검토하며, 단어 수가 200단어를 초과하는지 확인합니다.
3.  **조건부 분기**:
      * **승인된 경우 (`Yes`)**: 워크플로우는 `Publisher-Agent`로 진행합니다.
      * **거부된 경우 (`No`)**: 워크플로우가 중단되고, 거부 사유를 출력합니다.
4.  **Publisher-Agent**: 초안이 승인되면, 이 에이전트가 내용을 Markdown 파일로 저장합니다.

#### Python 구현 분석

이 예제는 조건부 논리를 구현하기 위해 사용자 정의 함수 `select_targets`를 사용합니다. 이 함수는 `add_multi_selection_edge_group`에 전달되어 리뷰어 출력의 `review_result` 필드에 따라 워크플로우 경로를 제어합니다.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# 이 함수는 검토 결과에 따라 다음 단계를 결정합니다
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # 승인이 되면 'save_draft' 실행기로 진행합니다
        return [save_draft_id]
    else:
        # 거부되면 실패를 보고하기 위해 'handle_review' 실행기로 진행합니다
        return [handle_review_id]

# 워크플로우 빌더는 라우팅을 위해 선택 함수를 사용합니다
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # 다중 선택 경로는 조건부 논리를 구현합니다
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

JSON 출력을 파싱해 선택 함수가 검사할 수 있는 강타입 객체로 변환하는 `to_reviewer_result` 같은 사용자 정의 실행자가 사용됩니다.

#### .NET (C\#) 구현 분석

.NET 버전도 조건 함수와 유사한 접근을 취합니다. `Func<object?, bool>`를 정의해 `ReviewResult` 객체의 `Result` 속성을 검사합니다.

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

`AddEdge` 메서드의 `condition` 인자를 통해 `WorkflowBuilder`가 분기 경로를 생성할 수 있습니다. 조건 `GetCondition(expectedResult: "Yes")`가 참인 경우에만 워크플로우가 `publishExecutor`를 따른다. 그렇지 않으면 `sendReviewerExecutor` 경로를 따릅니다.

## 결론

Microsoft Agent Framework Workflow는 복잡한 다중 에이전트 시스템을 오케스트레이션하기 위한 견고하고 유연한 기반을 제공합니다. 그래프 기반 아키텍처와 핵심 구성 요소를 활용해, 개발자는 Python과 .NET에서 모두 정교한 워크플로우를 설계하고 구현할 수 있습니다. 애플리케이션에 단순 순차 처리, 병렬 실행 또는 동적 조건부 논리가 필요하든, 이 프레임워크는 강력하고 확장 가능하며 타입 안전한 AI 기반 솔루션을 구축하는 도구를 제공합니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->