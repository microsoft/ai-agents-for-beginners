# Microsoft Agent Framework Workflow을 활용한 다중 에이전트 애플리케이션 구축

이 튜토리얼은 Microsoft Agent Framework을 사용하여 다중 에이전트 애플리케이션을 이해하고 구축하는 과정을 안내합니다. 다중 에이전트 시스템의 핵심 개념을 탐구하고, 프레임워크의 Workflow 구성 요소 아키텍처를 깊이 있게 살펴보며, Python과 .NET에서 다양한 워크플로 패턴을 활용한 실용적인 예제를 다룹니다.

## 1\. 다중 에이전트 시스템 이해하기

AI 에이전트는 일반적인 대형 언어 모델(LLM)의 능력을 넘어서는 시스템입니다. 환경을 인식하고, 결정을 내리며, 특정 목표를 달성하기 위해 행동할 수 있습니다. 다중 에이전트 시스템은 여러 에이전트가 협력하여 단일 에이전트로는 해결하기 어려운 문제를 해결하는 방식입니다.

### 일반적인 애플리케이션 시나리오

  * **복잡한 문제 해결**: 대규모 작업(예: 회사 전체 이벤트 계획)을 작은 하위 작업으로 나누고, 이를 전문화된 에이전트(예: 예산 에이전트, 물류 에이전트, 마케팅 에이전트)가 처리하도록 합니다.
  * **가상 비서**: 주요 비서 에이전트가 일정 관리, 조사, 예약과 같은 작업을 다른 전문화된 에이전트에게 위임합니다.
  * **자동화된 콘텐츠 생성**: 한 에이전트가 콘텐츠를 초안 작성하고, 다른 에이전트가 정확성과 톤을 검토하며, 세 번째 에이전트가 이를 게시하는 워크플로.

### 다중 에이전트 패턴

다중 에이전트 시스템은 상호작용 방식을 결정하는 여러 패턴으로 구성될 수 있습니다:

  * **순차적**: 에이전트가 정해진 순서대로 작업하며, 한 에이전트의 출력이 다음 에이전트의 입력이 됩니다.
  * **동시적**: 에이전트가 작업의 다른 부분을 병렬로 처리하며, 결과를 최종적으로 집계합니다.
  * **조건부**: 워크플로가 에이전트의 출력에 따라 다른 경로를 따릅니다. 이는 if-then-else 문과 유사합니다.

## 2\. Microsoft Agent Framework Workflow 아키텍처

Agent Framework의 워크플로 시스템은 다중 에이전트 간의 복잡한 상호작용을 관리하기 위해 설계된 고급 오케스트레이션 엔진입니다. 이는 [Pregel 스타일 실행 모델](https://kowshik.github.io/JPregel/pregel_paper.pdf)을 기반으로 한 그래프 기반 아키텍처로, "슈퍼스텝"이라고 불리는 동기화된 단계에서 처리가 이루어집니다.

### 핵심 구성 요소

아키텍처는 세 가지 주요 부분으로 구성됩니다:

1.  **Executors**: 기본 처리 단위입니다. 예제에서는 `Agent`가 executor의 한 유형입니다. 각 executor는 수신된 메시지 유형에 따라 자동으로 호출되는 여러 메시지 핸들러를 가질 수 있습니다.
2.  **Edges**: 메시지가 executor 간에 이동하는 경로를 정의합니다. Edge는 조건을 가질 수 있어 워크플로 그래프를 통해 정보를 동적으로 라우팅할 수 있습니다.
3.  **Workflow**: 전체 프로세스를 오케스트레이션하며, executor, edge, 전체 실행 흐름을 관리합니다. 메시지가 올바른 순서로 처리되도록 하고, 관찰 가능성을 위해 이벤트를 스트리밍합니다.

*워크플로 시스템의 핵심 구성 요소를 설명하는 다이어그램.*

이 구조는 순차적 체인, 병렬 처리용 팬아웃/팬인, 조건부 흐름을 위한 switch-case 논리와 같은 기본 패턴을 사용하여 견고하고 확장 가능한 애플리케이션을 구축할 수 있도록 합니다.

## 3\. 실용적인 예제와 코드 분석

이제 프레임워크를 사용하여 다양한 워크플로 패턴을 구현하는 방법을 살펴보겠습니다. 각 예제에 대해 Python과 .NET 코드를 살펴봅니다.

### 사례 1: 기본 순차 워크플로

가장 간단한 패턴으로, 한 에이전트의 출력이 직접 다른 에이전트로 전달됩니다. 우리의 시나리오는 호텔 `FrontDesk` 에이전트가 여행 추천을 하고, 이를 `Concierge` 에이전트가 검토하는 것입니다.

*기본 FrontDesk -\> Concierge 워크플로 다이어그램.*

#### 시나리오 배경

여행자가 파리에서 추천을 요청합니다.

1.  간결함을 중시하는 `FrontDesk` 에이전트는 루브르 박물관 방문을 추천합니다.
2.  진정한 경험을 우선시하는 `Concierge` 에이전트는 이 추천을 검토하고, 더 현지적이고 관광객이 적은 대안을 제안합니다.

#### Python 구현 분석

Python 예제에서는 먼저 두 에이전트를 정의하고 생성합니다. 각 에이전트는 특정 지침을 가지고 있습니다.

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

다음으로, `WorkflowBuilder`를 사용하여 그래프를 구성합니다. `front_desk_agent`를 시작점으로 설정하고, 출력이 `reviewer_agent`로 연결되도록 edge를 생성합니다.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

마지막으로, 초기 사용자 프롬프트로 워크플로를 실행합니다.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) 구현 분석

.NET 구현은 매우 유사한 논리를 따릅니다. 먼저 에이전트의 이름과 지침에 대한 상수를 정의합니다.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

`OpenAIClient`를 사용하여 에이전트를 생성한 후, `WorkflowBuilder`는 `frontDeskAgent`에서 `reviewerAgent`로 edge를 추가하여 순차적 흐름을 정의합니다.

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

그런 다음 사용자의 메시지로 워크플로를 실행하고 결과를 스트리밍합니다.

### 사례 2: 다단계 순차 워크플로

이 패턴은 기본 순서를 확장하여 더 많은 에이전트를 포함합니다. 이는 여러 단계의 정제 또는 변환이 필요한 프로세스에 적합합니다.

#### 시나리오 배경

사용자가 거실 이미지를 제공하고 가구 견적을 요청합니다.

1.  **Sales-Agent**: 이미지에서 가구 항목을 식별하고 목록을 생성합니다.
2.  **Price-Agent**: 항목 목록을 받아 예산, 중간 가격대, 고급 옵션을 포함한 상세 가격 내역을 제공합니다.
3.  **Quote-Agent**: 가격이 매겨진 목록을 받아 Markdown 형식의 공식 견적 문서를 작성합니다.

*Sales -\> Price -\> Quote 워크플로 다이어그램.*

#### Python 구현 분석

세 에이전트를 정의하며, 각 에이전트는 전문화된 역할을 가지고 있습니다. 워크플로는 `add_edge`를 사용하여 체인을 생성합니다: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

입력은 텍스트와 이미지 URI를 포함하는 `ChatMessage`입니다. 프레임워크는 각 에이전트의 출력을 다음 에이전트로 전달하여 최종 견적을 생성합니다.

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

#### .NET (C#) 구현 분석

.NET 예제는 Python 버전을 반영합니다. 세 에이전트(`salesagent`, `priceagent`, `quoteagent`)가 생성됩니다. `WorkflowBuilder`는 이들을 순차적으로 연결합니다.

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

사용자의 메시지는 이미지 데이터(바이트)와 텍스트 프롬프트를 포함하여 구성됩니다. `InProcessExecution.StreamAsync` 메서드는 워크플로를 시작하며, 최종 출력은 스트림에서 캡처됩니다.

### 사례 3: 동시 워크플로

이 패턴은 작업을 동시에 수행하여 시간을 절약할 때 사용됩니다. 여러 에이전트로 "팬아웃"하고 결과를 집계하는 "팬인"을 포함합니다.

#### 시나리오 배경

사용자가 시애틀 여행 계획을 요청합니다.

1.  **Dispatcher (Fan-Out)**: 사용자의 요청이 두 에이전트에 동시에 전달됩니다.
2.  **Researcher-Agent**: 시애틀의 명소, 날씨, 주요 고려 사항을 조사합니다.
3.  **Plan-Agent**: 독립적으로 상세한 일일 여행 일정표를 작성합니다.
4.  **Aggregator (Fan-In)**: 연구자와 플래너의 출력이 수집되어 최종 결과로 함께 제공됩니다.

*동시 Researcher와 Planner 워크플로 다이어그램.*

#### Python 구현 분석

`ConcurrentBuilder`는 이 패턴의 생성을 간소화합니다. 참여하는 에이전트를 나열하면 빌더가 팬아웃 및 팬인 논리를 자동으로 생성합니다.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

프레임워크는 `research_agent`와 `plan_agent`가 병렬로 실행되도록 하며, 최종 출력은 리스트로 수집됩니다.

#### .NET (C#) 구현 분석

.NET에서는 이 패턴이 더 명시적으로 정의되어야 합니다. 팬아웃 및 팬인 논리를 처리하기 위해 사용자 정의 executor(`ConcurrentStartExecutor` 및 `ConcurrentAggregationExecutor`)가 생성됩니다.

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

`WorkflowBuilder`는 이러한 사용자 정의 executor와 에이전트를 사용하여 그래프를 구성하기 위해 `AddFanOutEdge` 및 `AddFanInEdge`를 사용합니다.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### 사례 4: 조건부 워크플로

조건부 워크플로는 분기 논리를 도입하여 중간 결과에 따라 시스템이 다른 경로를 따를 수 있도록 합니다.

#### 시나리오 배경

이 워크플로는 기술 튜토리얼의 작성 및 게시를 자동화합니다.

1.  **Evangelist-Agent**: 주어진 개요와 URL을 기반으로 튜토리얼 초안을 작성합니다.
2.  **ContentReviewer-Agent**: 초안을 검토합니다. 단어 수가 200개를 초과하는지 확인합니다.
3.  **조건부 분기**:
      * **승인됨(`Yes`)**: 워크플로가 `Publisher-Agent`로 진행됩니다.
      * **거부됨(`No`)**: 워크플로가 중지되고 거부 이유를 출력합니다.
4.  **Publisher-Agent**: 초안이 승인되면 이 에이전트가 콘텐츠를 Markdown 파일로 저장합니다.

#### Python 구현 분석

이 예제에서는 조건부 논리를 구현하기 위해 사용자 정의 함수 `select_targets`를 사용합니다. 이 함수는 `add_multi_selection_edge_group`에 전달되어 `review_result` 필드를 기반으로 워크플로를 지시합니다.

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

`to_reviewer_result`와 같은 사용자 정의 executor는 에이전트의 JSON 출력을 구문 분석하여 선택 함수가 검사할 수 있는 강력한 형식의 객체로 변환합니다.

#### .NET (C#) 구현 분석

.NET 버전은 조건 함수와 유사한 접근 방식을 사용합니다. `Func<object?, bool>`이 정의되어 `ReviewResult` 객체의 `Result` 속성을 확인합니다.

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

`AddEdge` 메서드의 `condition` 매개변수는 `WorkflowBuilder`가 분기 경로를 생성할 수 있도록 합니다. 워크플로는 `GetCondition(expectedResult: "Yes")`가 true를 반환할 경우에만 `publishExecutor`로 이어지는 edge를 따릅니다. 그렇지 않으면 `sendReviewerExecutor`로 이어지는 경로를 따릅니다.

## 결론

Microsoft Agent Framework Workflow는 복잡한 다중 에이전트 시스템을 오케스트레이션하기 위한 견고하고 유연한 기반을 제공합니다. 그래프 기반 아키텍처와 핵심 구성 요소를 활용하여 개발자는 Python과 .NET에서 정교한 워크플로를 설계하고 구현할 수 있습니다. 애플리케이션이 간단한 순차 처리, 병렬 실행, 동적 조건부 논리를 필요로 하든, 프레임워크는 강력하고 확장 가능하며 타입 안전한 AI 기반 솔루션을 구축할 수 있는 도구를 제공합니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.