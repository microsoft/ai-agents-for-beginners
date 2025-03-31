<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c069d7ff0feca3027f88819355866ca1",
  "translation_date": "2025-03-28T13:47:45+00:00",
  "source_file": "06-building-trustworthy-agents\\README.md",
  "language_code": "ko"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.74ea485dbd9a9c3fb4c749f30f2b8130d025072b4d7d911c6f540eac5a78e6b8.ko.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(위 이미지를 클릭하면 해당 강의의 영상을 볼 수 있습니다)_

# 신뢰할 수 있는 AI 에이전트 구축

## 소개

이 강의에서는 다음 내용을 다룹니다:

- 안전하고 효과적인 AI 에이전트를 구축하고 배포하는 방법
- AI 에이전트를 개발할 때 중요한 보안 고려사항
- 데이터와 사용자 프라이버시를 유지하며 AI 에이전트를 개발하는 방법

## 학습 목표

이 강의를 마치면 다음을 할 수 있습니다:

- AI 에이전트를 만들 때 발생할 수 있는 위험을 식별하고 완화하는 방법
- 데이터를 적절히 관리하고 접근을 보호하기 위한 보안 조치를 구현하는 방법
- 데이터 프라이버시를 유지하며 사용자 경험의 품질을 제공하는 AI 에이전트를 만드는 방법

## 안전성

먼저 안전한 에이전트 애플리케이션을 구축하는 방법을 살펴보겠습니다. 안전성이란 AI 에이전트가 설계된 대로 작동하는 것을 의미합니다. 에이전트 애플리케이션 개발자로서 우리는 안전성을 극대화하기 위한 방법과 도구를 가지고 있습니다:

### 시스템 메시지 프레임워크 구축

대규모 언어 모델(LLM)을 사용하여 AI 애플리케이션을 구축해본 적이 있다면, 강력한 시스템 프롬프트 또는 시스템 메시지를 설계하는 것이 얼마나 중요한지 알 것입니다. 이러한 프롬프트는 LLM이 사용자 및 데이터와 상호작용하는 방식에 대한 메타 규칙, 지침, 가이드라인을 설정합니다.

AI 에이전트의 경우, 시스템 프롬프트는 더욱 중요합니다. 에이전트가 설계된 작업을 수행하기 위해 매우 구체적인 지침이 필요하기 때문입니다.

확장 가능한 시스템 프롬프트를 만들기 위해, 애플리케이션에서 하나 이상의 에이전트를 구축할 수 있는 시스템 메시지 프레임워크를 사용할 수 있습니다:

![Building a System Message Framework](../../../translated_images/system-message-framework.9df67f3d863520cd48878f71a1289740d8cb46e9d63ee065090ccf3b9b6b82a1.ko.png)

#### 단계 1: 메타 시스템 메시지 생성

메타 프롬프트는 LLM이 우리가 생성하는 에이전트의 시스템 프롬프트를 생성하도록 사용됩니다. 이를 템플릿으로 설계하여 필요에 따라 여러 에이전트를 효율적으로 생성할 수 있습니다.

다음은 LLM에 제공할 메타 시스템 메시지 예시입니다:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### 단계 2: 기본 프롬프트 생성

다음 단계는 AI 에이전트를 설명하는 기본 프롬프트를 만드는 것입니다. 여기에는 에이전트의 역할, 수행할 작업, 기타 책임이 포함되어야 합니다.

예시는 다음과 같습니다:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### 단계 3: 기본 시스템 메시지 제공

이제 메타 시스템 메시지를 시스템 메시지로 제공하고 기본 시스템 메시지를 추가하여 이 시스템 메시지를 최적화할 수 있습니다.

이를 통해 더 잘 설계된 시스템 메시지가 생성되어 AI 에이전트를 안내할 수 있습니다:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### 단계 4: 반복 및 개선

이 시스템 메시지 프레임워크의 가치는 여러 에이전트의 시스템 메시지를 쉽게 생성하고 시간이 지남에 따라 시스템 메시지를 개선할 수 있다는 점입니다. 처음부터 완벽한 시스템 메시지를 만드는 경우는 드뭅니다. 기본 시스템 메시지를 변경하고 이를 시스템에 실행하여 결과를 비교하고 평가함으로써 작은 조정과 개선을 할 수 있습니다.

## 위협 이해

신뢰할 수 있는 AI 에이전트를 구축하려면, AI 에이전트에 대한 위험과 위협을 이해하고 완화하는 것이 중요합니다. 다음은 AI 에이전트에 대한 몇 가지 주요 위협과 이를 계획하고 준비하는 방법입니다.

![Understanding Threats](../../../translated_images/understanding-threats.f8fbe6fe11e025b3085fc91e82d975937ad1d672260a2aeed40458aa41798d0e.ko.png)

### 작업 및 지침

**설명:** 공격자가 프롬프트를 조작하거나 입력을 변경하여 AI 에이전트의 지침이나 목표를 변경하려고 시도합니다.

**대응 방안:** AI 에이전트가 처리하기 전에 잠재적으로 위험한 프롬프트를 감지하기 위해 유효성 검사와 입력 필터를 실행하십시오. 이러한 공격은 일반적으로 에이전트와 빈번한 상호작용을 필요로 하므로 대화 턴 수를 제한하는 것도 이러한 공격을 방지하는 방법입니다.

### 주요 시스템 접근

**설명:** AI 에이전트가 민감한 데이터를 저장하는 시스템 및 서비스에 접근할 경우, 공격자가 에이전트와 서비스 간의 통신을 손상시킬 수 있습니다. 이는 직접적인 공격일 수도 있고, 에이전트를 통해 이러한 시스템에 대한 정보를 얻으려는 간접적인 시도일 수도 있습니다.

**대응 방안:** AI 에이전트는 필요할 때만 시스템에 접근할 수 있도록 제한해야 합니다. 에이전트와 시스템 간의 통신은 보안이 유지되어야 하며, 인증 및 접근 제어를 구현하는 것도 이러한 정보를 보호하는 방법입니다.

### 자원 및 서비스 과부하

**설명:** AI 에이전트는 작업을 완료하기 위해 다양한 도구와 서비스를 사용할 수 있습니다. 공격자는 AI 에이전트를 통해 많은 요청을 전송하여 이러한 서비스에 공격을 가해 시스템 장애 또는 높은 비용을 초래할 수 있습니다.

**대응 방안:** AI 에이전트가 서비스에 요청할 수 있는 횟수를 제한하는 정책을 구현하십시오. 에이전트와의 대화 턴 수 및 요청 횟수를 제한하는 것도 이러한 공격을 방지하는 방법입니다.

### 지식 기반 오염

**설명:** 이 유형의 공격은 AI 에이전트를 직접적으로 목표로 하지 않고, AI 에이전트가 사용하는 지식 기반 및 기타 서비스를 목표로 합니다. 이는 데이터 또는 정보를 손상시켜 사용자가 의도하지 않은 응답을 받게 할 수 있습니다.

**대응 방안:** AI 에이전트가 워크플로에서 사용하는 데이터를 정기적으로 검증하십시오. 이 데이터에 대한 접근이 안전하고 신뢰할 수 있는 개인만 변경할 수 있도록 하여 이러한 공격을 방지하십시오.

### 연쇄 오류

**설명:** AI 에이전트는 작업을 완료하기 위해 여러 도구와 서비스를 사용합니다. 공격자가 초래한 오류는 에이전트가 연결된 다른 시스템의 실패로 이어질 수 있어 공격이 더욱 확산되고 문제를 해결하기 어려워질 수 있습니다.

**대응 방안:** AI 에이전트가 도커 컨테이너와 같은 제한된 환경에서 작업하도록 하여 직접적인 시스템 공격을 방지하십시오. 특정 시스템이 오류를 반환했을 때 대체 메커니즘과 재시도 로직을 만드는 것도 더 큰 시스템 장애를 예방하는 방법입니다.

## Human-in-the-Loop

신뢰할 수 있는 AI 에이전트 시스템을 구축하는 또 다른 효과적인 방법은 Human-in-the-loop를 사용하는 것입니다. 이를 통해 사용자가 실행 중인 에이전트에 피드백을 제공할 수 있는 흐름을 만듭니다. 사용자는 다중 에이전트 시스템에서 에이전트 역할을 하며 실행 프로세스를 승인하거나 종료할 수 있습니다.

![Human in The Loop](../../../translated_images/human-in-the-loop.e9edbe8f6d42041b4213421410823250aa750fe8bdba5601d69ed46f3ff6489d.ko.png)

다음은 AutoGen을 사용하여 이 개념을 구현하는 코드 스니펫입니다:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## 결론

신뢰할 수 있는 AI 에이전트를 구축하려면 신중한 설계, 강력한 보안 조치, 지속적인 반복이 필요합니다. 구조화된 메타 프롬프트 시스템을 구현하고, 잠재적인 위협을 이해하며, 대응 전략을 적용함으로써 안전하고 효과적인 AI 에이전트를 개발할 수 있습니다. 또한, Human-in-the-loop 접근 방식을 포함하면 AI 에이전트가 사용자 요구에 부합하면서 위험을 최소화할 수 있습니다. AI가 계속 발전함에 따라 보안, 프라이버시, 윤리적 고려 사항에 대해 적극적인 자세를 유지하는 것이 AI 기반 시스템에서 신뢰와 안정성을 키우는 핵심이 될 것입니다.

## 추가 자료

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">책임 있는 AI 개요</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">생성형 AI 모델 및 AI 애플리케이션 평가</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">안전한 시스템 메시지</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">위험 평가 템플릿</a>

## 이전 강의

[Agentic RAG](../05-agentic-rag/README.md)

## 다음 강의

[Planning Design Pattern](../07-planning-design/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역은 오류나 부정확한 내용이 포함될 수 있습니다. 원본 문서의 모국어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역을 사용함으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.