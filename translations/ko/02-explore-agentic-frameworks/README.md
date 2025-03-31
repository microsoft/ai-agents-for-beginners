<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d3ceafa2939ede602b96d6bd412c5cbf",
  "translation_date": "2025-03-28T13:43:32+00:00",
  "source_file": "02-explore-agentic-frameworks\\README.md",
  "language_code": "ko"
}
-->
[![AI 에이전트 프레임워크 탐구](../../../translated_images/lesson-2-thumbnail.807a3a4fc57057096d10678bf84638d17d50c50239014e75a7708731a33bb802.ko.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(위 이미지를 클릭하면 해당 레슨의 영상을 볼 수 있습니다)_

# AI 에이전트 프레임워크 탐구

AI 에이전트 프레임워크는 AI 에이전트의 생성, 배포, 관리 과정을 간소화하도록 설계된 소프트웨어 플랫폼입니다. 이 프레임워크는 개발자들에게 사전 제작된 구성 요소, 추상화, 도구를 제공하여 복잡한 AI 시스템 개발을 보다 효율적으로 진행할 수 있도록 돕습니다.

이 프레임워크는 AI 에이전트 개발의 공통적인 도전 과제에 대해 표준화된 접근 방식을 제공함으로써 개발자들이 애플리케이션의 독창적인 측면에 집중할 수 있도록 돕습니다. 또한, AI 시스템 구축의 확장성, 접근성, 효율성을 향상시킵니다.

## 소개 

이 레슨에서는 다음 내용을 다룹니다:

- AI 에이전트 프레임워크란 무엇이며, 개발자들이 이를 통해 무엇을 달성할 수 있는가?
- 팀이 이를 활용하여 에이전트의 기능을 빠르게 프로토타입화, 반복, 개선할 수 있는 방법은?
- Microsoft가 만든 프레임워크 및 도구들 간의 차이점은 무엇인가?
- 기존 Azure 생태계 도구를 직접 통합할 수 있는가, 아니면 독립형 솔루션이 필요한가?
- Azure AI Agents 서비스란 무엇이며, 어떻게 도움이 되는가?

## 학습 목표

이 레슨의 목표는 다음을 이해하는 데 있습니다:

- AI 에이전트 프레임워크가 AI 개발에서 수행하는 역할.
- AI 에이전트 프레임워크를 활용하여 지능형 에이전트를 구축하는 방법.
- AI 에이전트 프레임워크가 가능하게 하는 주요 기능.
- AutoGen, Semantic Kernel, Azure AI Agent Service 간의 차이점.

## AI 에이전트 프레임워크란 무엇이며, 개발자들이 이를 통해 무엇을 할 수 있는가?

전통적인 AI 프레임워크는 애플리케이션에 AI를 통합하여 다음과 같은 방식으로 앱을 개선할 수 있습니다:

- **개인화**: AI는 사용자 행동과 선호도를 분석하여 맞춤형 추천, 콘텐츠, 경험을 제공합니다.  
  예: Netflix와 같은 스트리밍 서비스는 시청 기록을 기반으로 영화와 쇼를 추천하여 사용자 참여와 만족도를 높입니다.
- **자동화와 효율성**: AI는 반복적인 작업을 자동화하고, 워크플로를 간소화하며, 운영 효율성을 향상시킬 수 있습니다.  
  예: 고객 서비스 앱은 AI 기반 챗봇을 사용하여 일반적인 문의를 처리하고, 응답 시간을 줄이며, 복잡한 문제를 위해 인간 상담사를 확보합니다.
- **향상된 사용자 경험**: AI는 음성 인식, 자연어 처리, 예측 텍스트와 같은 지능형 기능을 제공하여 전반적인 사용자 경험을 향상시킬 수 있습니다.  
  예: Siri와 Google Assistant 같은 가상 비서는 음성 명령을 이해하고 응답하여 사용자가 기기와 상호작용하기 쉽게 만듭니다.

### 그렇다면, 왜 AI 에이전트 프레임워크가 필요한가?

AI 에이전트 프레임워크는 단순한 AI 프레임워크 이상의 것을 제공합니다. 이는 사용자, 다른 에이전트, 환경과 상호작용하여 특정 목표를 달성할 수 있는 지능형 에이전트를 생성하도록 설계되었습니다. 이러한 에이전트는 자율적으로 행동하고, 결정을 내리며, 변화하는 상황에 적응할 수 있습니다. AI 에이전트 프레임워크가 가능하게 하는 주요 기능을 살펴보겠습니다:

- **에이전트 간 협업 및 조정**: 여러 AI 에이전트를 생성하여 협력, 커뮤니케이션, 조정을 통해 복잡한 작업을 해결할 수 있습니다.
- **작업 자동화 및 관리**: 다단계 워크플로 자동화, 작업 위임, 에이전트 간 동적 작업 관리 메커니즘을 제공합니다.
- **상황 이해 및 적응**: 에이전트가 상황을 이해하고, 변화하는 환경에 적응하며, 실시간 정보를 기반으로 결정을 내릴 수 있는 능력을 갖추게 합니다.

요약하면, 에이전트는 더 많은 일을 가능하게 하고, 자동화를 한 단계 더 발전시키며, 환경에서 학습하고 적응할 수 있는 더 지능적인 시스템을 생성할 수 있도록 합니다.

## 에이전트의 기능을 빠르게 프로토타입화, 반복, 개선하는 방법?

이 분야는 빠르게 변화하고 있지만, 대부분의 AI 에이전트 프레임워크에서 공통적으로 제공하는 모듈 구성 요소, 협업 도구, 실시간 학습 등의 요소를 활용하면 빠르게 프로토타입화하고 반복할 수 있습니다. 자세히 살펴보겠습니다:

- **모듈 구성 요소 활용**: AI SDK는 AI 및 메모리 커넥터, 자연어 또는 코드 플러그인을 사용하는 함수 호출, 프롬프트 템플릿 등 사전 제작된 구성 요소를 제공합니다.
- **협업 도구 활용**: 특정 역할과 작업을 가진 에이전트를 설계하여 협업 워크플로를 테스트하고 개선할 수 있습니다.
- **실시간 학습**: 피드백 루프를 구현하여 에이전트가 상호작용에서 학습하고 동적으로 행동을 조정하도록 합니다.

### 모듈 구성 요소 활용

Microsoft Semantic Kernel 및 LangChain과 같은 SDK는 AI 커넥터, 프롬프트 템플릿, 메모리 관리와 같은 사전 제작된 구성 요소를 제공합니다.

**팀이 이를 활용하는 방법**: 팀은 이러한 구성 요소를 빠르게 조립하여 기능적 프로토타입을 만들 수 있으며, 이를 통해 처음부터 시작하지 않고도 빠르게 실험하고 반복할 수 있습니다.

**실제 작동 방식**: 사전 제작된 파서를 사용하여 사용자 입력에서 정보를 추출하고, 메모리 모듈을 통해 데이터를 저장하고 검색하며, 프롬프트 생성기를 사용하여 사용자와 상호작용할 수 있습니다. 이는 이러한 구성 요소를 처음부터 구축할 필요 없이 가능합니다.

**예제 코드**: Semantic Kernel Python 및 .Net에서 사전 제작된 AI 커넥터를 사용하는 코드 예제를 살펴보겠습니다. 이 코드는 모델이 사용자 입력에 응답하도록 자동 함수 호출을 활용합니다:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```  
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```  

이 예제에서 볼 수 있듯이, 사용자 입력에서 출발지, 목적지, 항공편 예약 날짜 등의 주요 정보를 추출하는 데 사전 제작된 파서를 활용할 수 있습니다. 이러한 모듈식 접근 방식은 고수준의 로직에 집중할 수 있게 합니다.

### 협업 도구 활용

CrewAI, Microsoft AutoGen, Semantic Kernel과 같은 프레임워크는 여러 에이전트를 생성하고 협력하도록 지원합니다.

**팀이 이를 활용하는 방법**: 팀은 특정 역할과 작업을 가진 에이전트를 설계하여 협업 워크플로를 테스트하고 개선하며 시스템 효율성을 향상시킬 수 있습니다.

**실제 작동 방식**: 데이터 검색, 분석, 의사 결정과 같은 특정 기능을 수행하는 에이전트 팀을 생성할 수 있습니다. 이러한 에이전트는 정보를 공유하고 커뮤니케이션하며 사용자 질의에 응답하거나 작업을 완료하는 등 공동 목표를 달성할 수 있습니다.

**예제 코드 (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```  

이 코드에서는 데이터를 분석하는 데 여러 에이전트가 협력하는 작업을 생성하는 방법을 보여줍니다. 각 에이전트는 특정 기능을 수행하며, 작업은 에이전트를 조정하여 원하는 결과를 달성합니다. 특정 역할을 가진 전용 에이전트를 생성함으로써 작업 효율성과 성능을 향상시킬 수 있습니다.

### 실시간 학습

고급 프레임워크는 실시간 상황 이해 및 적응 기능을 제공합니다.

**팀이 이를 활용하는 방법**: 팀은 피드백 루프를 구현하여 에이전트가 상호작용에서 학습하고 행동을 동적으로 조정하도록 합니다. 이를 통해 지속적으로 기능을 개선하고 정제할 수 있습니다.

**실제 작동 방식**: 에이전트는 사용자 피드백, 환경 데이터, 작업 결과를 분석하여 지식 기반을 업데이트하고, 의사 결정 알고리즘을 조정하며, 성능을 향상시킵니다. 이러한 반복 학습 과정은 에이전트가 변화하는 조건과 사용자 선호도에 적응할 수 있도록 하여 전체 시스템 효과성을 높입니다.

## AutoGen, Semantic Kernel, Azure AI Agent Service 프레임워크 간의 차이점은 무엇인가?

이 프레임워크들을 비교하는 방법은 여러 가지가 있지만, 설계, 기능, 대상 사용 사례 측면에서 주요 차이점을 살펴보겠습니다:  

모듈화, 협업, 프로세스 오케스트레이션 | 안전하고 확장 가능하며 유연한 AI 에이전트 배포 | 이러한 프레임워크 각각의 이상적인 사용 사례는 무엇인가요? 

## 기존 Azure 생태계 도구를 직접 통합할 수 있나요, 아니면 독립형 솔루션이 필요한가요?

답은 "예"입니다. 기존 Azure 생태계 도구를 Azure AI Agent Service와 직접 통합할 수 있습니다. 특히, 이 서비스는 다른 Azure 서비스와 원활하게 작동하도록 설계되었습니다. 예를 들어 Bing, Azure AI Search, Azure Functions를 통합할 수 있습니다. 또한 Azure AI Foundry와 깊게 통합되어 있습니다. 

AutoGen 및 Semantic Kernel의 경우에도 Azure 서비스와 통합할 수 있지만, 코드에서 Azure 서비스를 호출해야 할 수도 있습니다. 또 다른 통합 방법은 Azure SDK를 사용하여 에이전트에서 Azure 서비스와 상호작용하는 것입니다. 

추가적으로, 언급했듯이 AutoGen이나 Semantic Kernel에서 구축된 에이전트를 위해 Azure AI Agent Service를 오케스트레이터로 사용할 수 있으며, 이를 통해 Azure 생태계에 쉽게 접근할 수 있습니다.

## 참고 자료

---

## 이전 학습

[AI 에이전트와 에이전트 사용 사례 소개](../01-intro-to-ai-agents/README.md)

## 다음 학습

[에이전트 디자인 패턴 이해하기](../03-agentic-design-patterns/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원문은 해당 언어로 작성된 문서를 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생할 수 있는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.