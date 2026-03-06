[![Exploring AI Agent Frameworks](../../../translated_images/ko/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(위 이미지 클릭 시 본 강의의 영상 보기)_

# AI 에이전트 프레임워크 탐색하기

AI 에이전트 프레임워크는 AI 에이전트의 생성, 배포 및 관리를 간소화하기 위해 고안된 소프트웨어 플랫폼입니다. 이 프레임워크들은 개발자에게 복잡한 AI 시스템 개발을 간편하게 할 수 있도록 사전 제작된 구성요소, 추상화 및 도구를 제공합니다.

이 프레임워크들은 AI 에이전트 개발의 공통 과제에 대한 표준화된 접근 방식을 제공하여 개발자가 애플리케이션의 고유한 측면에 집중할 수 있도록 돕습니다. 또한 AI 시스템 구축 시 확장성, 접근성 및 효율성을 향상합니다.

## 소개

이번 강의에서는 다음을 다룹니다:

- AI 에이전트 프레임워크란 무엇이며 개발자가 어떤 성과를 낼 수 있나요?
- 팀이 어떻게 이를 활용하여 에이전트의 기능을 빠르게 프로토타입하고 반복 개선할 수 있나요?
- Microsoft에서 만든 프레임워크와 도구(<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>, <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)의 차이점은 무엇인가요?
- 기존 Azure 생태계 도구를 직접 통합할 수 있나요, 아니면 독립형 솔루션이 필요한가요?
- Azure AI Agents 서비스란 무엇이며 어떻게 도움이 되나요?

## 학습 목표

이번 강의의 목표는 다음을 이해하는 데 있습니다:

- AI 개발에서 AI 에이전트 프레임워크의 역할
- AI 에이전트 프레임워크를 활용해 지능형 에이전트를 구축하는 방법
- AI 에이전트 프레임워크가 지원하는 핵심 기능
- Microsoft Agent Framework와 Azure AI Agent Service의 차이점

## AI 에이전트 프레임워크란 무엇이며 개발자로서 무엇을 할 수 있게 해주나요?

전통적인 AI 프레임워크는 다음과 같은 방식으로 애플리케이션에 AI를 통합하고 개선하는 데 도움을 줍니다:

- **개인화**: AI가 사용자 행동과 선호도를 분석하여 개인 맞춤형 추천, 콘텐츠 및 경험을 제공합니다.
예시: Netflix 같은 스트리밍 서비스는 AI를 활용해 시청 기록을 기반으로 영화와 프로그램을 추천하여 사용자 참여도와 만족도를 높입니다.
- **자동화 및 효율성**: AI가 반복적인 작업을 자동화하고, 업무 흐름을 간소화하며 운영 효율성을 개선합니다.
예시: 고객 서비스 앱은 AI 챗봇을 통해 일반 문의를 처리하여 대응 시간을 단축하고, 복잡한 문제에 대한 인적 상담사 리소스를 절약합니다.
- **향상된 사용자 경험**: AI가 음성 인식, 자연어 처리 및 예측 텍스트 같은 지능형 기능을 제공하여 전반적인 사용자 경험을 향상합니다.
예시: Siri, 구글 어시스턴트 같은 가상 비서는 AI를 활용하여 음성 명령을 이해하고 응답해 사용자가 기기와 쉽게 상호작용할 수 있게 합니다.

### 이 모든 게 훌륭해 보이지만, 왜 AI 에이전트 프레임워크가 필요한가요?

AI 에이전트 프레임워크는 단순한 AI 프레임워크 이상의 것을 의미합니다. 이들은 사용자, 다른 에이전트, 환경과 상호작용하며 특정 목표를 달성할 수 있는 지능형 에이전트를 생성하게 설계되었습니다. 이들 에이전트는 자율적 행동을 보이고, 의사결정을 하며, 상황 변화에 적응할 수 있습니다. AI 에이전트 프레임워크가 지원하는 주요 기능을 살펴보겠습니다:

- **에이전트 협업 및 조정**: 함께 작업하고 소통하며 복잡한 작업을 해결할 수 있는 다수의 AI 에이전트 생성 지원
- **업무 자동화 및 관리**: 다단계 워크플로우 자동화, 업무 위임, 에이전트 간 동적 작업 관리 메커니즘 제공
- **맥락 이해 및 적응**: 에이전트가 맥락을 이해하고 변화하는 환경에 적응하며 실시간 정보를 바탕으로 의사결정 하는 능력 부여

요약하면, 에이전트는 더 많은 일을 가능하게 하여 자동화를 다음 단계로 끌어올리고, 환경에서 학습하고 적응하는 더 지능적인 시스템을 생성할 수 있게 합니다.

## 에이전트의 기능을 빠르게 프로토타입하고 반복 개선하려면 어떻게 해야 할까요?

이 분야는 빠르게 변화하고 있지만, 대부분 AI 에이전트 프레임워크에서 공통적으로 제공하는 몇 가지가 있습니다. 모듈 구성요소, 협업 도구, 실시간 학습이 그것입니다. 각각을 살펴보겠습니다:

- **모듈 구성요소 사용**: AI SDK들은 AI 및 메모리 커넥터, 자연어 또는 코드 플러그인을 통한 함수 호출, 프롬프트 템플릿 등 사전 구축된 컴포넌트를 제공합니다.
- **협업 도구 활용**: 특정 역할과 작업을 가진 에이전트를 디자인해 함께 테스트하고 협업 워크플로우를 개선할 수 있습니다.
- **실시간 학습**: 피드백 루프를 구현해 에이전트가 상호작용에서 학습하고 동적으로 행동을 조절하도록 합니다.

### 모듈 구성요소 사용

Microsoft Agent Framework 같은 SDK는 AI 커넥터, 도구 정의, 에이전트 관리를 포함하는 사전 구축된 컴포넌트를 제공합니다.

**팀에서는 이렇게 활용할 수 있습니다**: 팀은 이러한 구성요소를 조합해 처음부터 개발하지 않고도 기능적 프로토타입을 신속하게 제작하여 빠른 실험과 반복이 가능합니다.

**실무 예시**: 미리 만들어진 파서를 사용해 사용자 입력에서 정보를 추출하고, 메모리 모듈로 데이터를 저장 및 검색하며, 프롬프트 생성기로 사용자와 상호작용하는 작업을 모두 직접 만들 필요 없이 수행할 수 있습니다.

**예제 코드**. Microsoft Agent Framework를 `AzureAIProjectAgentProvider`와 함께 사용해 모델이 사용자 입력에 도구 호출로 응답하는 방법을 예로 보겠습니다:

``` python
# Microsoft Agent Framework Python 예제

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# 여행 예약을 위한 샘플 도구 함수를 정의합니다
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
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

이 예시를 통해 사용자 입력에서 출발지, 목적지, 비행 날짜 같은 핵심 정보를 추출하는 사전 제작된 파서를 활용하는 방법을 알 수 있습니다. 이 모듈식 접근 방식은 상위 레벨의 로직에 집중할 수 있게 해줍니다.

### 협업 도구 활용

Microsoft Agent Framework 같은 프레임워크는 여러 에이전트가 함께 작업할 수 있도록 지원합니다.

**팀에서는 이렇게 활용할 수 있습니다**: 팀은 특정 역할과 작업을 가진 에이전트를 설계해 협업 워크플로우를 테스트하고 개선하여 전체 시스템 효율성을 향상시킬 수 있습니다.

**실무 예시**: 데이터 검색, 분석, 의사결정 각기 다른 전문 기능을 가진 에이전트 팀을 구성할 수 있습니다. 이 에이전트들은 공동의 목표(예: 사용자 질문 답변 또는 업무 완수)를 위해 소통하고 정보를 공유합니다.

**예제 코드 (Microsoft Agent Framework)**:

```python
# Microsoft Agent Framework를 사용하여 함께 작동하는 여러 에이전트를 생성

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# 데이터 검색 에이전트
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# 데이터 분석 에이전트
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# 작업에 대해 에이전트를 순차적으로 실행
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

이 코드는 여러 에이전트가 데이터를 분석하기 위해 협업하는 작업을 생성하는 방법을 보여줍니다. 각 에이전트는 특정 기능을 수행하며, 작업은 목표 달성을 위해 에이전트들 간 조정을 통해 실행됩니다. 전문화된 역할을 가진 전담 에이전트를 생성함으로써 작업 효율성과 성능을 높일 수 있습니다.

### 실시간 학습

고급 프레임워크는 실시간 맥락 이해 및 적응 기능을 제공합니다.

**팀에서는 이렇게 활용할 수 있습니다**: 팀은 에이전트가 상호작용에서 학습하고 동적으로 행동을 조절하는 피드백 루프를 구현해 능력을 지속적으로 개선하고 정제할 수 있습니다.

**실무 예시**: 에이전트는 사용자 피드백, 환경 데이터, 작업 결과를 분석하여 지식 기반을 업데이트하고 의사결정 알고리즘을 수정하며 성능을 개선합니다. 이 반복 학습 프로세스는 에이전트가 변화하는 조건과 사용자 선호에 적응해 전반적 시스템 효율을 향상시킵니다.

## Microsoft Agent Framework와 Azure AI Agent Service의 차이점은 무엇인가요?

이 두 접근법을 비교하는 방법은 다양하지만, 설계, 기능 및 대상 사용 사례 측면에서 주요 차이를 살펴보겠습니다:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework는 `AzureAIProjectAgentProvider`를 이용해 AI 에이전트를 쉽게 구축할 수 있는 간소화된 SDK를 제공합니다. 이 프레임워크는 도구 호출, 대화 관리, Azure 인증을 통한 엔터프라이즈급 보안을 갖춘 Azure OpenAI 모델을 활용하는 에이전트 생성을 지원합니다.

**사용 사례**: 도구 활용, 다단계 워크플로우, 엔터프라이즈 통합 시나리오에서 프로덕션용 AI 에이전트 구축.

Microsoft Agent Framework의 주요 핵심 개념:

- **에이전트**: 에이전트는 `AzureAIProjectAgentProvider`를 통해 생성하며, 이름, 지침, 도구로 구성합니다. 에이전트는:
  - **사용자 메시지 처리** 및 Azure OpenAI 모델로 응답 생성
  - **대화 맥락에 따른 도구 자동 호출**
  - **여러 상호작용에 걸친 대화 상태 유지**

  에이전트를 생성하는 코드 예시는 다음과 같습니다:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **도구**: 프레임워크는 에이전트가 자동으로 호출할 수 있는 파이썬 함수 형태 도구 정의를 지원합니다. 도구는 에이전트 생성 시 등록됩니다:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **다중 에이전트 조정**: 전문화된 다수의 에이전트를 생성하고 이들의 작업을 조정할 수 있습니다:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure 인증 통합**: `AzureCliCredential`(또는 `DefaultAzureCredential`)을 사용해 키를 직접 관리하지 않고도 안전하게 인증합니다.

## Azure AI Agent Service

Azure AI Agent Service는 Microsoft Ignite 2024에서 소개된 최신 서비스입니다. Llama 3, Mistral, Cohere 같은 오픈소스 LLM을 직접 호출하는 등 더 유연한 모델을 사용해 AI 에이전트를 개발 및 배포할 수 있게 합니다.

Azure AI Agent Service는 강화된 엔터프라이즈 보안 메커니즘과 데이터 저장 방식을 제공해 기업용 애플리케이션에 적합합니다.

Microsoft Agent Framework와 연동해 에이전트 빌드 및 배포가 가능합니다.

이 서비스는 현재 퍼블릭 프리뷰 단계이며 Python과 C#을 지원합니다.

Azure AI Agent Service Python SDK를 사용해 사용자 정의 도구를 갖춘 에이전트를 생성하는 예:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# 도구 함수 정의
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
        model="gpt-4o-mini",
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

Azure AI Agent Service는 다음 핵심 개념을 포함합니다:

- **에이전트**: Azure AI Agent Service는 Microsoft Foundry와 통합됩니다. AI Foundry 내에서 AI 에이전트는 질문에 답변(RAG), 작업 수행, 전면적인 워크플로우 자동화에 사용할 수 있는 "스마트" 마이크로서비스 역할을 합니다. 생성 AI 모델의 힘과 현실 데이터 소스에 접근하고 상호작용할 수 있게 하는 도구를 결합해 이를 실현합니다. 다음은 에이전트 예시입니다:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    예시에서 에이전트는 `gpt-4o-mini` 모델에 이름은 `my-agent`, 지침은 `You are helpful agent` 로 생성됩니다. 코드를 해석하는 작업을 수행할 도구와 리소스를 갖추고 있습니다.

- **대화 스레드와 메시지**: 스레드는 에이전트와 사용자 간의 대화 또는 상호작용을 나타내는 중요한 개념입니다. 스레드는 대화 진행 상황 추적, 맥락 정보 저장, 상호작용 상태 관리를 위해 사용됩니다. 스레드의 예시는 다음과 같습니다:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    위 코드에서 스레드가 생성된 후, 메시지가 스레드로 전송됩니다. `create_and_process_run` 호출로 에이전트에게 스레드 작업을 수행하도록 요청합니다. 마지막으로 메시지를 가져와 에이전트의 응답을 확인합니다. 메시지는 텍스트, 이미지, 파일 등 다양한 유형일 수 있으며, 예를 들어 이미지 또는 텍스트 응답이 될 수 있습니다. 개발자는 이 정보를 활용해 답변을 추가 처리하거나 사용자에게 표시할 수 있습니다.

- **Microsoft Agent Framework와 통합**: Azure AI Agent Service는 Microsoft Agent Framework와 원활히 작동해 `AzureAIProjectAgentProvider`를 이용해 에이전트를 만들고 Agent Service를 통해 프로덕션에 배포할 수 있습니다.

**사용 사례**: 보안성, 확장성, 유연성이 요구되는 엔터프라이즈 AI 에이전트 배포에 적합합니다.

## 이 두 접근법의 차이는 무엇인가요?

겹치는 부분도 있지만, 설계, 기능, 대상 사용 사례 면에서 주요 차이가 있습니다:

- **Microsoft Agent Framework (MAF)**: 도구 호출, 대화 관리, Azure 인증 통합을 포함하는 에이전트 구축용 프로덕션 준비 SDK입니다. 간단하고 일관성 있는 API를 제공합니다.
- **Azure AI Agent Service**: Azure Foundry 내 에이전트 플랫폼 및 배포 서비스입니다. Azure OpenAI, Azure AI Search, Bing Search, 코드 실행 등 다양한 서비스와 내장 연결성을 제공합니다.

아직도 어떤 것을 선택해야 할지 모르겠다면?

### 사용 사례별 안내

몇 가지 일반적인 사용 사례를 통해 도움을 드리겠습니다:

> Q: 프로덕션용 AI 에이전트 애플리케이션을 빠르게 시작하고 싶어요.
>

> A: Microsoft Agent Framework가 좋은 선택입니다. `AzureAIProjectAgentProvider`를 통해 도구와 지침을 몇 줄 코드로 정의하는 간단하고 파이썬 다운 API를 제공합니다.

> Q: Azure 통합(검색, 코드 실행 등)과 같은 엔터프라이즈급 배포가 필요합니다.
>
> A: Azure AI Agent Service가 가장 적합합니다. 여러 모델, Azure AI Search, Bing Search, Azure Functions를 위한 내장 기능이 있는 플랫폼 서비스이며, Foundry 포털에서 에이전트를 쉽게 빌드하고 대규모로 배포할 수 있습니다.

> Q: 아직 헷갈려요, 한 가지만 추천해주세요.
>
> A: 우선 Microsoft Agent Framework로 에이전트를 구축 시작하고, 프로덕션 배포 및 확장 시 Azure AI Agent Service를 사용하세요. 이렇게 하면 에이전트 로직을 빠르게 반복하면서도 엔터프라이즈 배포 경로를 확보할 수 있습니다.

핵심 차이를 표로 정리하면 다음과 같습니다:

| 프레임워크 | 초점 | 핵심 개념 | 사용 사례 |
| --- | --- | --- | --- |
| Microsoft Agent Framework | 도구 호출이 포함된 간소화된 에이전트 SDK | 에이전트, 도구, Azure 인증 | AI 에이전트 구축, 도구 사용, 다단계 워크플로우 |
| Azure AI Agent Service | 유연한 모델, 엔터프라이즈 보안, 코드 생성, 도구 호출 | 모듈화, 협업, 프로세스 오케스트레이션 | 안전하고 확장 가능하며 유연한 AI 에이전트 배포 |

## 기존 Azure 생태계 도구를 직접 통합할 수 있나요, 아니면 독립형 솔루션이 필요한가요?
답은 예입니다. 기존 Azure 생태계 도구를 Azure AI Agent Service와 직접 통합할 수 있습니다. 특히 이 서비스는 다른 Azure 서비스와 원활하게 작동하도록 구축되었기 때문입니다. 예를 들어 Bing, Azure AI Search, Azure Functions와 통합할 수 있습니다. 또한 Microsoft Foundry와도 깊이 통합되어 있습니다.

Microsoft Agent Framework는 `AzureAIProjectAgentProvider`와 Azure ID를 통해 Azure 서비스와 통합되어 에이전트 도구에서 직접 Azure 서비스를 호출할 수 있습니다.

## Sample Codes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI Agent Framework에 대해 더 궁금하신가요?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)에 참여하여 다른 학습자들과 만나고, 오피스 아워에 참석하며 AI Agents 관련 질문에 답을 얻으세요.

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Previous Lesson

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Next Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 양지해 주시기 바랍니다. 원본 문서는 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 모든 오해나 잘못된 해석에 대해 당사는 책임지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->