[![AI 에이전트 프레임워크 탐색](../../../translated_images/ko/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(위 이미지를 클릭하면 이 수업의 비디오를 볼 수 있습니다)_

# AI 에이전트 프레임워크 탐색하기

AI 에이전트 프레임워크는 AI 에이전트의 생성, 배포 및 관리를 단순화하도록 설계된 소프트웨어 플랫폼입니다. 이러한 프레임워크는 개발자에게 복잡한 AI 시스템 개발을 간소화하는 미리 구축된 구성 요소, 추상화 및 도구를 제공합니다.

이 프레임워크들은 AI 에이전트 개발에서 흔히 발생하는 문제에 대해 표준화된 접근 방식을 제공하여 개발자가 애플리케이션의 고유한 측면에 집중할 수 있게 돕습니다. 또한 AI 시스템 구축 시 확장성, 접근성 및 효율성을 향상시킵니다.

## 소개

이 수업에서 다룰 내용:

- AI 에이전트 프레임워크란 무엇이며 개발자가 이를 통해 무엇을 달성할 수 있는가?
- 팀이 어떻게 이를 사용해 빠르게 프로토타입을 만들고, 반복하며 에이전트의 기능을 향상시킬 수 있는가?
- Microsoft에서 만든 프레임워크 및 도구들(<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a>와 <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) 간의 차이는 무엇인가?
- 기존 Azure 생태계 도구를 직접 통합할 수 있나, 아니면 독립 실행형 솔루션이 필요한가?
- Microsoft Foundry Agent Service란 무엇이며 이것이 어떻게 도움이 되는가?

## 학습 목표

이 수업의 목표는 다음을 이해하는 데 도움을 주는 것입니다:

- AI 에이전트 프레임워크가 AI 개발에서 하는 역할
- AI 에이전트 프레임워크를 활용해 지능형 에이전트를 구축하는 방법
- AI 에이전트 프레임워크가 제공하는 주요 기능
- Microsoft Agent Framework와 Microsoft Foundry Agent Service의 차이점

## AI 에이전트 프레임워크란 무엇이며 개발자가 이를 통해 무엇을 할 수 있는가?

기존 AI 프레임워크는 다음과 같은 방식으로 앱에 AI를 통합하고 앱을 향상시키는 데 도움을 줄 수 있습니다:

- <strong>개인화</strong>: AI는 사용자 행동 및 선호도를 분석하여 맞춤형 추천, 콘텐츠 및 경험을 제공합니다.
예: 넷플릭스와 같은 스트리밍 서비스가 시청 기록을 바탕으로 영화와 프로그램을 추천하여 사용자 참여와 만족도를 높입니다.
- **자동화 및 효율성**: AI는 반복 작업을 자동화하고 워크플로우를 최적화하며 운영 효율성을 향상시킵니다.
예: 고객 서비스 앱은 AI 기반 챗봇을 사용해 일반 문의를 처리함으로써 응답 시간을 줄이고 복잡한 문제는 인간 상담원이 처리할 수 있도록 합니다.
- **향상된 사용자 경험**: AI는 음성 인식, 자연어 처리, 예측 텍스트 등 지능형 기능을 제공하여 전반적인 사용자 경험을 개선합니다.
예: Siri와 Google Assistant와 같은 가상 비서가 음성 명령을 이해하고 응답하여 사용자의 장치 상호작용을 쉽게 합니다.

### 이 모든 게 좋게 들리지만, 왜 AI 에이전트 프레임워크가 필요한가요?

AI 에이전트 프레임워크는 단순한 AI 프레임워크 이상의 의미를 가집니다. 이들은 사용자, 다른 에이전트 및 환경과 상호작용하며 특정 목표를 달성할 수 있는 지능형 에이전트 생성에 중점을 둡니다. 이러한 에이전트는 자율적으로 행동하고, 의사결정을 하며, 변화하는 조건에 적응할 수 있습니다. AI 에이전트 프레임워크가 제공하는 몇 가지 주요 기능을 살펴보겠습니다:

- **에이전트 협업 및 조정**: 여러 AI 에이전트가 함께 작업하고, 소통하며, 복잡한 작업을 협력하여 해결할 수 있도록 지원합니다.
- **작업 자동화 및 관리**: 다단계 워크플로우 자동화, 작업 위임, 에이전트 간 동적 작업 관리를 위한 메커니즘을 제공합니다.
- **맥락 이해 및 적응**: 에이전트가 맥락을 이해하고 변화하는 환경에 적응하며 실시간 정보를 기반으로 의사결정할 수 있습니다.

요약하자면, 에이전트는 더 많은 작업을 수행하고 자동화를 한층 진화시키며, 환경에서 학습하고 적응할 수 있는 더 지능적인 시스템을 만들 수 있게 합니다.

## 에이전트의 기능을 빠르게 프로토타입하고 반복하며 개선하려면?

AI 에이전트 프레임워크 분야는 빠르게 변하는 환경이지만, 대부분의 AI 에이전트 프레임워크에서 공통적으로 볼 수 있는 몇 가지 요소가 있습니다. 모듈형 구성 요소, 협업 도구, 실시간 학습 등이 그것입니다. 이들을 자세히 살펴봅시다:

- **모듈형 구성 요소 사용**: AI SDK는 AI 및 메모리 커넥터, 자연어 또는 코드 플러그인을 이용한 함수 호출, 프롬프트 템플릿 등 미리 구축된 컴포넌트를 제공합니다.
- **협업 도구 활용**: 특정 역할과 작업을 가진 에이전트를 설계하여 협업 워크플로우를 테스트하고 개선할 수 있습니다.
- **실시간 학습**: 에이전트가 상호작용에서 학습하고 행동을 동적으로 조정하는 피드백 루프를 구현합니다.

### 모듈형 구성 요소 사용하기

Microsoft Agent Framework 같은 SDK는 AI 커넥터, 도구 정의, 에이전트 관리와 같은 미리 만들어진 구성 요소를 제공합니다.

**팀이 사용하는 방법**: 팀은 이러한 구성 요소를 신속히 조립해 기능적인 프로토타입을 만들 수 있어, 처음부터 새로 구축하지 않고 빠르게 실험 및 반복할 수 있습니다.

**실제 작동 방식**: 사전 구축된 파서를 사용해 사용자 입력에서 정보를 추출하고, 메모리 모듈을 이용해 데이터를 저장 및 검색하며, 프롬프트 생성기를 통해 사용자와 상호작용할 수 있습니다. 모두 직접 구성 요소를 처음부터 만들 필요 없이 가능합니다.

**예제 코드**. Microsoft Agent Framework를 `FoundryChatClient`와 함께 사용해 도구 호출로 모델이 사용자 입력에 응답하는 예를 살펴보겠습니다:

``` python
# 마이크로소프트 에이전트 프레임워크 파이썬 예제

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# 여행 예약을 위한 샘플 도구 함수 정의
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # 예시 출력: 2025년 1월 1일 뉴욕행 항공편이 성공적으로 예약되었습니다. 안전한 여행 되세요! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

이 예제에서 볼 수 있듯이, 사전 구축된 파서를 활용해 비행기 예약 요청에서 출발지, 도착지, 날짜 등 주요 정보를 추출할 수 있습니다. 이러한 모듈식 접근은 고레벨 로직에 집중할 수 있도록 돕습니다.

### 협업 도구 활용하기

Microsoft Agent Framework 같은 프레임워크는 여러 에이전트가 협력할 수 있게 합니다.

**팀이 사용하는 방법**: 팀은 각기 역할과 작업을 지정한 에이전트를 설계해 협업 워크플로우를 테스트 및 개선하고 시스템 효율성을 높일 수 있습니다.

**실제 작동 방식**: 데이터 검색, 분석, 의사결정 등 각기 기능을 전문화한 에이전트들로 팀을 구성합니다. 이들은 소통하며 정보를 공유해 사용자 문의 답변이나 작업 완수 같은 공통 목표를 달성합니다.

**예제 코드 (Microsoft Agent Framework)**:

```python
# Microsoft Agent Framework를 사용하여 함께 작동하는 여러 에이전트 생성

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# 데이터 검색 에이전트
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# 데이터 분석 에이전트
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# 작업에서 에이전트를 순차적으로 실행
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

이전 코드에서 여러 에이전트가 협력해 데이터를 분석하는 작업을 만드는 방법을 볼 수 있습니다. 각 에이전트는 특정 기능을 수행하며, 작업은 에이전트 간 조정을 통해 원하는 결과를 도출합니다. 역할이 특화된 전담 에이전트를 만들면 작업 효율과 성능을 향상시킬 수 있습니다.

### 실시간 학습하기

고급 프레임워크는 실시간 맥락 이해와 적응 기능을 제공합니다.

**팀이 사용하는 방법**: 팀은 에이전트가 상호작용에서 학습하고 동적으로 행동을 조정하는 피드백 루프를 구현해 능력을 지속적으로 개선하고 다듬을 수 있습니다.

**실제 작동 방식**: 에이전트는 사용자 피드백, 환경 데이터, 작업 결과를 분석해 지식 베이스를 갱신하고 의사결정 알고리즘을 조정하며 시간에 따라 성능을 향상시킵니다. 이러한 반복 학습 프로세스는 에이전트가 변화하는 상황과 사용자 선호에 적응하게 하여 시스템 전체 효율성을 높입니다.

## Microsoft Agent Framework와 Microsoft Foundry Agent Service의 차이는 무엇인가?

다양한 비교 방법이 있지만, 설계, 기능 및 대상 사용 사례 측면에서 몇 가지 주요 차이점을 보겠습니다:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework는 `FoundryChatClient`를 사용해 AI 에이전트를 구축하기 위한 간결한 SDK를 제공합니다. Azure OpenAI 모델을 활용해 도구 호출, 대화 관리, Azure 아이덴티티를 통한 엔터프라이즈급 보안을 지원합니다.

**사용 사례**: 도구 사용, 다단계 워크플로우, 엔터프라이즈 통합 시나리오를 갖춘 프로덕션 준비 AI 에이전트 구축.

Microsoft Agent Framework의 주요 핵심 개념은 다음과 같습니다:

- <strong>에이전트</strong>. `FoundryChatClient`를 통해 이름, 지침, 도구 등으로 구성된 에이전트 생성. 에이전트는:
  - **사용자 메시지 처리** 및 Azure OpenAI 모델을 활용한 응답 생성.
  - **대화 맥락에 따른 도구 자동 호출**.
  - **다수 상호작용에 걸친 대화 상태 유지**.

  에이전트를 생성하는 코드 스니펫은 다음과 같습니다:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- <strong>도구</strong>. 에이전트가 자동으로 호출할 수 있는 파이썬 함수 형태 도구 정의를 지원합니다. 도구는 에이전트 생성 시 등록됩니다:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **다중 에이전트 조정**. 여러 전문화된 에이전트를 생성하고 이들의 작업을 조정할 수 있습니다:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure 아이덴티티 통합**. API 키 관리를 없애는 `AzureCliCredential`(또는 `DefaultAzureCredential`)를 이용한 보안 인증 제공.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service는 Microsoft Ignite 2024에서 소개된 최신 서비스로서, Llama 3, Mistral, Cohere 같은 오픈 소스 LLM에 직접 호출할 수 있는 유연한 모델을 사용해 AI 에이전트를 개발 및 배포할 수 있습니다.

Microsoft Foundry Agent Service는 강력한 엔터프라이즈 보안 메커니즘과 데이터 저장 방식을 제공하여 기업용 애플리케이션에 적합합니다.

Microsoft Agent Framework와 즉시 연동되어 에이전트를 구축하고 배포할 수 있습니다.

현재 퍼블릭 프리뷰 단계이며 Python과 C#을 지원합니다.

Microsoft Foundry Agent Service Python SDK를 사용하면 사용자 정의 도구가 포함된 에이전트를 생성할 수 있습니다:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# 도구 함수를 정의합니다
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### 핵심 개념

Microsoft Foundry Agent Service의 주요 핵심 개념은 다음과 같습니다:

- <strong>에이전트</strong>. Microsoft Foundry 내에서 AI 에이전트는 질문 응답(RAG), 작업 수행, 워크플로우 완전 자동화를 할 수 있는 "스마트" 마이크로서비스 역할을 합니다. 생성 AI 모델과 실제 데이터 소스 접근 및 상호작용 도구를 결합해 이를 구현합니다. 에이전트 예시는 다음과 같습니다:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    이 예제에서는 `gpt-5-mini` 모델, 이름 `my-agent`, 지침 `You are helpful agent`로 에이전트를 생성하며, 코드 해석 작업에 도구와 리소스를 갖추고 있습니다.

- **스레드와 메시지**. 스레드는 에이전트와 사용자 간 대화나 상호작용을 나타내는 중요한 개념입니다. 스레드는 대화 진행 상황 추적, 맥락 저장, 상호작용 상태 관리를 위해 사용됩니다. 스레드 예시는 다음과 같습니다:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # 에이전트에게 스레드에서 작업을 수행하도록 요청합니다
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # 에이전트의 응답을 확인하기 위해 모든 메시지를 가져오고 기록합니다
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    이전 코드에서 스레드를 생성하고 메시지를 전송했습니다. `create_and_process_run` 호출로 에이전트에게 작업을 수행하도록 요청합니다. 마지막으로 메시지를 가져와 에이전트의 응답을 확인합니다. 메시지는 사용자와 에이전트 간 대화 진행 상황을 나타냅니다. 메시지는 텍스트, 이미지, 파일 등 다양한 유형일 수 있으며, 이는 에이전트 작업 결과로 생성된 예입니다. 개발자는 이를 활용해 응답을 추가 처리하거나 사용자에게 표시할 수 있습니다.

- **Microsoft Agent Framework와의 통합**. Microsoft Foundry Agent Service는 Microsoft Agent Framework와 매끄럽게 연동하여, `FoundryChatClient`로 에이전트를 만들고 생산 환경에서 에이전트 서비스를 통해 배포할 수 있습니다.

**사용 사례**: Microsoft Foundry Agent Service는 보안성, 확장성, 유연성이 요구되는 엔터프라이즈 AI 에이전트 배포용으로 설계되었습니다.

## 이 두 접근법의 차이는 무엇인가?
 
겹치는 부분도 있지만 설계, 기능, 대상 사용 사례 면에서 몇 가지 주요 차이점이 있습니다:
 
- **Microsoft Agent Framework (MAF)**: 도구 호출, 대화 관리, Azure 아이덴티티 통합 기능을 갖춘 프로덕션 준비 SDK입니다.
- **Microsoft Foundry Agent Service**: Microsoft Foundry 내 에이전트 플랫폼 겸 배포 서비스로 Azure OpenAI, Azure AI Search, Bing Search, 코드 실행 등 서비스와 내장 연동 기능을 제공합니다.
 
아직 어떤 것을 선택해야 할지 고민되나요?

### 사용 사례
 
흔한 사용 사례를 함께 살펴봅시다:
 
> Q: 프로덕션 AI 에이전트 애플리케이션을 빠르게 구축하고 싶어요.
>

>A: Microsoft Agent Framework가 좋은 선택입니다. `FoundryChatClient`를 통한 간단하고 파이썬 친화적인 API로 몇 줄 코드만으로 에이전트에 도구와 지침을 정의할 수 있습니다.

>Q: Azure 통합(Search, 코드 실행 등)을 포함한 엔터프라이즈급 배포가 필요해요.
>
> A: Microsoft Foundry Agent Service가 최적입니다. 여러 모델, Azure AI Search, Bing Search, Azure 함수와 내장 연동 기능을 제공하는 플랫폼 서비스로 Foundry 포털에서 쉽게 에이전트를 구축하고 대규모 배포할 수 있습니다.
 
> Q: 아직도 헷갈리는데, 그냥 하나만 추천해 주세요.
>
> A: 우선 Microsoft Agent Framework로 에이전트를 구축하고, 필요할 때 Microsoft Foundry Agent Service를 통해 프로덕션에서 배포 및 확장하는 방식을 권장합니다. 이렇게 하면 에이전트 로직을 빠르게 반복하면서도 엔터프라이즈 배포 경로를 확보할 수 있습니다.
 
주요 차이를 표로 정리해 보겠습니다:

| 프레임워크 | 초점 | 핵심 개념 | 사용 사례 |
| --- | --- | --- | --- |
| Microsoft Agent Framework | 도구 호출을 갖춘 간결한 에이전트 SDK | 에이전트, 도구, Azure 아이덴티티 | AI 에이전트 구축, 도구 활용, 다단계 워크플로우 |
| Microsoft Foundry Agent Service | 유연한 모델, 엔터프라이즈 보안, 코드 생성, 도구 호출 | 모듈성, 협업, 프로세스 오케스트레이션 | 안전하고 확장 가능하며 유연한 AI 에이전트 배포 |

## 기존 Azure 생태계 도구를 직접 통합할 수 있나요, 아니면 독립 실행형 솔루션이 필요한가요?


답변은 예입니다. 기존 Azure 생태계 도구를 Microsoft Foundry Agent Service와 직접 통합할 수 있습니다. 특히 이 서비스는 다른 Azure 서비스와 원활하게 작동하도록 구축되었습니다. 예를 들어 Bing, Azure AI Search 및 Azure Functions를 통합할 수 있습니다. Microsoft Foundry와의 깊은 통합도 지원됩니다.

Microsoft Agent Framework는 `FoundryChatClient`와 Azure ID를 통해 Azure 서비스와도 통합되어 에이전트 도구에서 직접 Azure 서비스를 호출할 수 있습니다.

## 샘플 코드

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI 에이전트 프레임워크에 대해 더 궁금하신가요?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)에 가입하여 다른 학습자와 만나고, 오피스 아워에 참석하며 AI 에이전트 관련 질문에 대한 답변을 받아보세요.

## 참고 자료

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## 이전 강의

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## 다음 강의

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->