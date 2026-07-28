[![Multi-Agent Design](../../../translated_images/ko/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(위 이미지를 클릭하면 이 수업의 비디오를 볼 수 있습니다)_
# AI 에이전트에서의 메타인지

## 소개

AI 에이전트의 메타인지에 대한 수업에 오신 것을 환영합니다! 이 장은 AI 에이전트가 자신의 사고 과정을 어떻게 생각할 수 있는지 궁금해하는 초보자들을 위해 설계되었습니다. 이 수업이 끝나면, 핵심 개념을 이해하고 AI 에이전트 설계에 메타인지를 적용할 수 있는 실용적인 예제를 갖추게 될 것입니다.

## 학습 목표

이 수업을 완료하면, 다음을 할 수 있습니다:

1. 에이전트 정의에서 추론 루프가 가지는 함의를 이해합니다.
2. 계획 및 평가 기법을 사용하여 자기 수정 에이전트를 돕습니다.
3. 작업 수행을 위해 코드를 조작할 수 있는 자체 에이전트를 만듭니다.

## 메타인지 소개

메타인지는 자신의 사고에 대해 생각하는 고차원 인지 과정을 말합니다. AI 에이전트에게는 자기 인식과 과거 경험을 바탕으로 자신의 행동을 평가하고 조정할 수 있는 능력을 의미합니다. '사고에 대한 사고'라는 메타인지는 에이전틱 AI 시스템 개발에서 중요한 개념입니다. 이는 AI 시스템이 자신의 내부 과정을 인식하고 그에 따라 행동을 모니터링, 조절, 적응할 수 있음을 포함합니다. 우리가 상황을 파악하거나 문제를 바라볼 때 하는 것과 비슷합니다. 이러한 자기 인식은 AI 시스템이 더 나은 결정을 내리고 오류를 식별하며 시간이 지남에 따라 성능을 향상시키는 데 도움이 됩니다—이는 튜링 테스트와 AI가 세상을 지배할지에 대한 논쟁으로 다시 연결됩니다.

에이전틱 AI 시스템의 맥락에서 메타인지는 다음과 같은 여러 문제를 해결하는 데 도움을 줄 수 있습니다:
- 투명성: AI 시스템이 자신의 추론과 결정을 설명할 수 있도록 보장합니다.
- 추론: AI 시스템이 정보를 종합하고 건전한 결정을 내리는 능력을 향상시킵니다.
- 적응성: AI 시스템이 새로운 환경과 변화하는 조건에 적응할 수 있게 합니다.
- 인식: AI 시스템이 환경에서 데이터를 인식하고 해석하는 정확성을 향상시킵니다.

### 메타인지란 무엇인가?

메타인지는 '사고에 대한 사고'로서, 자신의 인지 과정을 자각하고 자기 조절하는 고차원 인지 과정입니다. AI 영역에서는 메타인지가 에이전트가 전략과 행동을 평가하고 조정할 수 있게 하여 문제 해결과 의사결정 능력을 향상시킵니다. 메타인지를 이해하면 더 똑똑할 뿐 아니라 더 적응력 있고 효율적인 AI 에이전트를 설계할 수 있습니다. 진정한 메타인지에서는 AI가 자신의 추론에 대해 명시적으로 사고하는 모습을 볼 수 있습니다.

예시: “저렴한 항공편을 우선시했는데… 직항편을 놓치고 있을지도 몰라, 다시 확인해볼게.”
특정 경로를 선택한 이유나 방식을 기록합니다.
- 이전 사용자 선호에 과도하게 의존해서 실수가 발생했음을 인지하고, 단순히 최종 추천뿐 아니라 의사결정 전략을 수정합니다.
- "사용자가 '너무 붐빈다'고 언급할 때마다, 인기 순으로 항상 상위 명소를 고르는 내 방식을 반성하고, 특정 명소를 제거하는 것뿐 아니라 내 명소 선정 방법이 잘못되었음을 진단합니다."

### AI 에이전트에서 메타인지의 중요성

메타인지는 여러 가지 이유로 AI 에이전트 설계에서 중요한 역할을 합니다:

![Importance of Metacognition](../../../translated_images/ko/importance-of-metacognition.b381afe9aae352f7.webp)

- 자기 성찰: 에이전트가 자신의 성능을 평가하고 개선할 분야를 식별할 수 있습니다.
- 적응성: 에이전트가 과거 경험과 변화하는 환경에 따라 전략을 수정할 수 있습니다.
- 오류 수정: 에이전트가 오류를 자율적으로 감지하고 교정하여 더 정확한 결과를 만듭니다.
- 자원 관리: 에이전트가 시간과 계산 능력 같은 자원 사용을 계획하고 평가하여 최적화합니다.

## AI 에이전트 구성 요소

메타인지 과정을 탐구하기 전에 AI 에이전트의 기본 구성 요소를 이해하는 것이 중요합니다. AI 에이전트는 일반적으로 다음으로 구성됩니다:

- 페르소나: 사용자와 상호작용하는 방식을 정의하는 에이전트의 성격과 특성.
- 도구: 에이전트가 수행할 수 있는 능력과 기능.
- 기술: 에이전트가 보유한 지식과 전문성.

이러한 구성 요소가 함께 작용하여 특정 작업을 수행할 수 있는 "전문성 단위"를 만듭니다.

<strong>예시</strong>:
실시간 데이터와 과거 고객 여정 경험을 바탕으로 경로를 조정하는 여행 계획 서비스를 제공하는 여행 에이전트를 생각해 보세요.

### 예시: 여행 에이전트 서비스에서의 메타인지

AI 기반의 여행 에이전트 서비스를 설계한다고 상상해보세요. 이 에이전트 "여행 에이전트"는 사용자가 휴가를 계획하는 데 도움을 줍니다. 메타인지를 포함하기 위해 여행 에이전트는 자기 인식과 과거 경험을 기반으로 행동을 평가하고 조정해야 합니다. 메타인지가 어떻게 작용할 수 있는지 살펴보겠습니다:

#### 현재 과제

현재 과제는 사용자가 파리 여행을 계획하도록 돕는 것입니다.

#### 과제 완료 단계

1. **사용자 선호 수집**: 여행 날짜, 예산, 관심사(예: 박물관, 요리, 쇼핑), 특정 요구사항을 사용자에게 묻습니다.
2. **정보 검색**: 사용자의 선호에 맞는 항공편, 숙소, 명소, 음식점을 찾습니다.
3. **추천 생성**: 항공 세부사항, 호텔 예약, 제안 활동을 포함한 맞춤형 일정을 제공합니다.
4. **피드백에 따른 조정**: 사용자의 추천에 대한 피드백을 받고 필요한 조정을 합니다.

#### 필요한 자원

- 항공 및 호텔 예약 데이터베이스 접근.
- 파리 명소와 음식점에 관한 정보.
- 이전 상호작용에서 수집한 사용자 피드백 데이터.

#### 경험과 자기 성찰

여행 에이전트는 메타인지를 이용해 자신의 성능을 평가하고 과거 경험에서 학습합니다. 예를 들어:

1. **사용자 피드백 분석**: 여행 에이전트가 사용자 피드백을 검토하여 어떤 추천이 긍정적이었고 어떤 것이 그렇지 않았는지 파악합니다. 그리고 미래 제안을 조정합니다.
2. <strong>적응성</strong>: 사용자가 붐비는 장소를 싫어한다고 이전에 말한 경우, 여행 에이전트는 향후 붐비는 관광지를 추천하지 않을 것입니다.
3. **오류 수정**: 예를 들어, 여행 에이전트가 이미 예약이 꽉 찬 호텔을 제안하는 오류가 있었다면, 추천 전에 더 철저히 가용성을 확인하는 방법을 학습합니다.

#### 실용적 개발자 예시

메타인지를 포함한 여행 에이전트 코드가 어떻게 작성될 수 있는지 간단한 예시입니다:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # 선호도에 따라 항공편, 호텔, 명소 검색
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # 피드백을 분석하고 향후 추천 조정
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# 사용 예시
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### 메타인지가 중요한 이유

- **자기 성찰**: 에이전트가 자신의 성능을 분석하고 개선 가능 영역을 식별할 수 있습니다.
- <strong>적응성</strong>: 에이전트가 피드백과 변화하는 조건에 맞춰 전략을 수정할 수 있습니다.
- **오류 수정**: 에이전트가 스스로 실수를 감지하고 수정할 수 있습니다.
- **자원 관리**: 에이전트가 시간과 계산 자원 같은 자원의 활용을 최적화할 수 있습니다.

메타인지를 도입함으로써, 여행 에이전트는 더 개인화되고 정확한 여행 추천을 제공하여 사용자 경험을 향상시킬 수 있습니다.

---

## 2. 에이전트의 계획 수립

계획은 AI 에이전트 행동의 핵심 요소입니다. 목표를 달성하기 위해 필요한 단계들을 현재 상태, 자원, 가능한 장애물을 고려하여 구성하는 과정입니다.

### 계획의 요소

- **현재 과제**: 과제를 명확히 정의합니다.
- **과제 완료 단계**: 과제를 관리 가능한 단계로 분해합니다.
- **필요 자원**: 필요한 자원을 식별합니다.
- <strong>경험</strong>: 과거 경험을 활용해 계획을 수립합니다.

<strong>예시</strong>:
사용자의 여행 계획을 효과적으로 돕기 위해 여행 에이전트가 수행해야 할 단계입니다:

### 여행 에이전트를 위한 단계

1. **사용자 선호 수집**
   - 여행 날짜, 예산, 관심사, 특정 요구사항에 대해 사용자에게 질문합니다.
   - 예시: "여행 예정일은 언제인가요?" "예산 범위가 어떻게 되나요?" "휴가 동안 어떤 활동을 즐기시나요?"

2. **정보 검색**
   - 사용자 선호를 바탕으로 적합한 여행 옵션을 찾습니다.
   - <strong>항공편</strong>: 사용자의 예산과 여행 예정일에 맞는 항공편을 찾습니다.
   - <strong>숙소</strong>: 위치, 가격, 편의시설 등 사용자 선호에 맞는 호텔이나 임대 숙소를 찾습니다.
   - **명소 및 음식점**: 사용자의 관심사와 맞는 인기 명소, 활동, 식당을 확인합니다.

3. **추천 생성**
   - 수집한 정보를 바탕으로 맞춤형 일정을 만듭니다.
   - 항공편, 호텔 예약, 제안 활동 등 사용자 선호에 맞춰 추천을 제공합니다.

4. **일정 사용자에게 제시**
   - 제안한 일정을 사용자에게 공유하여 검토하도록 합니다.
   - 예시: "파리 여행을 위한 추천 일정입니다. 항공편 세부사항, 호텔 예약, 추천 활동 및 음식점 목록이 포함되어 있습니다. 의견을 알려주세요!"

5. **피드백 수집**
   - 제안된 일정에 대한 사용자의 피드백을 받습니다.
   - 예시: "항공편 옵션이 마음에 드시나요?" "호텔이 요구사항에 맞나요?" "추가하거나 제거하고 싶은 활동이 있나요?"

6. **피드백에 따른 일정 조정**
   - 사용자의 피드백을 반영하여 일정을 수정합니다.
   - 항공편, 숙박, 활동 추천을 사용자의 선호에 맞게 변경합니다.

7. **최종 확인**
   - 수정된 일정을 사용자에게 최종 확인 받습니다.
   - 예시: "피드백을 반영해 일정을 조정했습니다. 업데이트된 일정입니다. 모두 괜찮으신가요?"

8. **예약 및 확인**
   - 사용자가 일정을 승인하면 항공편, 숙박, 사전 계획된 활동을 예약합니다.
   - 확인 세부사항을 사용자에게 보냅니다.

9. **지속적인 지원 제공**
   - 여행 전과 중에 사용자 변경 요청이나 추가 지원에 대비하여 대기합니다.
   - 예시: "여행 기간 중 추가 지원이 필요하시면 언제든 연락주세요!"

### 예시 상호작용

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# 부킹 요청 내에서의 예시 사용법
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. 교정적 RAG 시스템

먼저, RAG 도구와 사전 맥락 로드의 차이를 이해하는 것부터 시작합시다.

![RAG vs Context Loading](../../../translated_images/ko/rag-vs-context.9eae588520c00921.webp)

### 검색 기반 생성(RAG)

RAG는 검색 시스템과 생성 모델을 결합합니다. 질의가 이루어지면, 검색 시스템이 외부 출처에서 관련 문서나 데이터를 가져오고, 이 검색된 정보가 생성 모델에 제공되어 더 정확하고 상황에 적절한 응답을 생성하도록 돕습니다.

RAG 시스템에서 에이전트는 지식 베이스에서 관련 정보를 검색하여 적절한 응답이나 행동을 생성합니다.

### 교정적 RAG 접근법

교정적 RAG 접근법은 RAG 기법을 사용하여 오류를 수정하고 AI 에이전트의 정확성을 향상시키는 데 중점을 둡니다. 이는 다음을 포함합니다:

1. **프롬프트 기법**: 에이전트가 관련 정보를 검색하도록 특정 프롬프트를 사용합니다.
2. <strong>도구</strong>: 에이전트가 검색된 정보의 관련성을 평가하고 정확한 응답을 생성할 수 있게 하는 알고리즘과 메커니즘을 구현합니다.
3. <strong>평가</strong>: 에이전트의 성능을 지속적으로 평가하고 정확도와 효율성을 개선하기 위한 조정을 합니다.

#### 예시: 검색 에이전트에서의 교정적 RAG

사용자 질의에 답하기 위해 웹에서 정보를 검색하는 검색 에이전트를 생각해 보세요. 교정적 RAG 접근법은 다음을 포함할 수 있습니다:

1. **프롬프트 기법**: 사용자의 입력을 기반으로 검색 쿼리를 작성합니다.
2. <strong>도구</strong>: 자연어 처리 및 기계 학습 알고리즘을 사용하여 검색 결과를 순위 매기고 필터링합니다.
3. <strong>평가</strong>: 사용자 피드백을 분석하여 검색된 정보의 부정확성을 식별하고 수정합니다.

### 여행 에이전트에서의 교정적 RAG

교정적 RAG(검색 기반 생성)는 AI가 정보를 검색하고 생성하는 능력을 향상시키면서 오류를 교정하는 역할을 합니다. 여행 에이전트가 더 정확하고 적합한 여행 추천을 제공하기 위해 어떻게 교정적 RAG 접근법을 사용할 수 있는지 알아봅시다.

여기에 포함된 내용:

- **프롬프트 기법:** 관련 정보를 검색하도록 에이전트를 안내하는 특정 프롬프트 사용.
- **도구:** 에이전트가 검색된 정보의 관련성을 평가하고 정확한 답변을 생성할 수 있도록 하는 알고리즘 및 메커니즘 구현.
- **평가:** 에이전트의 성능을 꾸준히 평가하고 정확도 및 효율성을 높이기 위한 조치 시행.

#### 여행 에이전트에 교정적 RAG 구현 단계

1. **초기 사용자 상호작용**
   - 여행 에이전트가 목적지, 여행 날짜, 예산, 관심사 등 초기 선호도를 수집합니다.
   - 예시:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **정보 검색**
   - 여행 에이전트가 사용자 선호에 기반해 항공편, 숙소, 명소, 음식점 정보를 검색합니다.
   - 예시:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **초기 추천 생성**
   - 여행 에이전트가 검색된 정보를 사용해 맞춤형 일정을 만듭니다.
   - 예시:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **사용자 피드백 수집**
   - 여행 에이전트가 초기 추천에 대해 사용자 피드백을 요청합니다.
   - 예시:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **교정적 RAG 과정**
   - **프롬프트 기법**: 사용자 피드백을 바탕으로 새로운 검색 쿼리를 작성합니다.
     - 예시:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - <strong>도구</strong>: 사용자 피드백을 반영해 검색 결과를 순위 매기고 필터링하는 알고리즘을 사용합니다.
     - 예시:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - <strong>평가</strong>: 사용자 피드백을 분석하여 추천의 관련성과 정확성을 지속적으로 평가하고 조정합니다.
     - 예시:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### 실용적 예시

다음은 교정적 RAG 접근법을 포함하는 여행 에이전트의 간단한 Python 코드 예시입니다:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# 사용 예시
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### 사전 맥락 로드


선행 컨텍스트 로드는 쿼리를 처리하기 전에 모델에 관련 컨텍스트나 배경 정보를 로드하는 것을 포함합니다. 이는 모델이 시작부터 이 정보에 접근할 수 있음을 의미하며, 처리 중에 추가 데이터를 가져올 필요 없이 더 정보에 기반한 응답을 생성하는 데 도움이 될 수 있습니다.

다음은 여행사 애플리케이션에서 선행 컨텍스트 로드가 어떻게 작동할 수 있는지 간단한 예입니다(Python):

```python
class TravelAgent:
    def __init__(self):
        # 인기 목적지 및 해당 정보 미리 로드
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # 미리 로드된 컨텍스트에서 목적지 정보 가져오기
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# 사용 예제
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### 설명

1. **초기화(`__init__` 메서드)**: `TravelAgent` 클래스는 파리, 도쿄, 뉴욕, 시드니와 같은 인기 여행지 정보가 포함된 딕셔너리를 미리 로드합니다. 이 딕셔너리는 각 여행지의 국가, 통화, 언어 및 주요 명소 등의 세부 정보를 포함합니다.

2. **정보 조회(`get_destination_info` 메서드)**: 사용자가 특정 여행지에 대해 문의하면 `get_destination_info` 메서드가 미리 로드된 컨텍스트 딕셔너리에서 관련 정보를 가져옵니다.

사전 로딩된 컨텍스트를 통해 여행사 앱은 외부 소스에서 실시간으로 정보를 가져올 필요 없이 사용자 문의에 빠르게 응답할 수 있습니다. 이는 애플리케이션을 보다 효율적이고 반응성 있게 만듭니다.

### 반복 전에 목표로 계획 부트스트래핑하기

목표로 계획을 부트스트래핑하는 것은 명확한 목적이나 최종 목표를 염두에 두고 시작하는 것을 뜻합니다. 이 목표를 사전에 정의함으로써 모델은 반복 과정 내내 이를 지침으로 삼아 각 반복이 원하는 결과에 가까워지도록 하여 프로세스를 더욱 효율적이고 집중적으로 만듭니다.

여기 여행사 애플리케이션에서 반복 전에 목표를 설정해 여행 계획을 부트스트랩하는 예제가 있습니다(Python):

### 시나리오

여행사는 고객 맞춤형 휴가 계획을 세우고자 합니다. 목표는 고객의 선호도와 예산을 기반으로 만족도를 극대화하는 여행 일정을 만드는 것입니다.

### 단계

1. 고객의 선호도와 예산 정의하기.
2. 이 선호도를 바탕으로 초기 계획 부트스트래핑하기.
3. 고객 만족도를 최적화하며 계획을 반복적으로 개선하기.

#### Python 코드

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# 사용 예시
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### 코드 설명

1. **초기화(`__init__` 메서드)**: `TravelAgent` 클래스는 이름, 비용, 활동 유형과 같은 속성을 가진 잠재적 여행지 목록으로 초기화됩니다.

2. **계획 부트스트래핑(`bootstrap_plan` 메서드)**: 이 메서드는 고객의 선호도와 예산에 기반해 초기 여행 계획을 만듭니다. 여행지 목록을 반복하며 고객의 선호와 예산 범위에 맞는 여행지를 계획에 추가합니다.

3. **선호도 일치(`match_preferences` 메서드)**: 이 메서드는 여행지가 고객의 선호와 일치하는지 확인합니다.

4. **계획 반복(`iterate_plan` 메서드)**: 이 메서드는 계획 내 각 여행지를 고객 선호도와 예산 제한 사항을 고려해 더 나은 여행지로 교체 시도하면서 초기 계획을 개선합니다.

5. **비용 계산(`calculate_cost` 메서드)**: 이 메서드는 새 여행지를 포함한 현재 계획의 총 비용을 계산합니다.

#### 사용 예

- **초기 계획**: 여행사는 고객의 관광 선호도와 2,000달러 예산에 기반해 초기 계획을 만듭니다.
- **개선된 계획**: 여행사는 고객의 선호와 예산을 최적화하면서 계획을 반복적으로 개선합니다.

명확한 목표(예: 고객 만족도 극대화)로 계획을 부트스트랩하고 반복 개선함으로써 여행사는 고객 맞춤형이고 최적화된 여행 일정을 만들 수 있습니다. 이는 계획이 처음부터 고객 선호도와 예산에 맞게 조율되고 반복마다 개선됨을 보장합니다.

### 순위 재조정과 점수 매기기를 위한 LLM 활용

대규모 언어 모델(LLM)은 검색된 문서나 생성된 응답의 관련성과 품질을 평가하여 순위 재조정과 점수 매기기에 활용할 수 있습니다. 작동 방식은 다음과 같습니다:

**검색:** 초기 검색 단계에서 쿼리에 기반한 후보 문서나 응답 집합을 가져옵니다.

**재순위화:** LLM이 후보들을 평가하고 관련성과 품질에 따라 재순위화합니다. 이 단계는 가장 관련성 높고 품질 좋은 정보가 우선적으로 제시되도록 합니다.

**점수 매기기:** LLM이 각 후보에 점수를 부여하여 그 관련성과 품질을 반영합니다. 이는 최상의 응답이나 문서를 선택하는 데 도움을 줍니다.

LLM을 재순위화와 점수 매기기에 활용함으로써, 시스템은 보다 정확하고 문맥상 적절한 정보를 제공하여 전반적인 사용자 경험을 개선할 수 있습니다.

다음은 여행사가 사용자의 선호도에 따라 여행지를 재순위화하고 점수 매기기 위해 대규모 언어 모델(LLM)을 사용하는 예제입니다(Python):

#### 시나리오 - 선호도 기반 여행

여행사는 고객에게 최적의 여행지를 추천하고자 합니다. LLM은 이를 위해 여행지를 재순위화하고 점수 매김하여 가장 관련성 높은 옵션을 제공하도록 돕습니다.

#### 단계:

1. 사용자 선호도 수집하기.
2. 잠재 여행지 목록 검색하기.
3. LLM을 사용해 사용자 선호도에 따라 여행지를 재순위화하고 점수 매기기.

이전 예제를 Azure OpenAI 서비스 사용 예제로 업데이트하는 방법은 다음과 같습니다:

#### 요구 사항

1. Azure 구독이 필요합니다.
2. Azure OpenAI 리소스를 생성하고 API 키를 받으십시오.

#### 예제 Python 코드

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Azure OpenAI를 위한 프롬프트 생성
        prompt = self.generate_prompt(preferences)
        
        # 요청을 위한 헤더와 페이로드 정의
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # 재순위 지정되고 점수가 매겨진 목적지를 얻기 위해 Azure OpenAI API 호출
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # 추천 항목 추출 및 반환
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# 사용 예시
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### 코드 설명 - 선호도 북커

1. <strong>초기화</strong>: `TravelAgent` 클래스는 이름과 설명과 같은 속성을 가진 잠재 여행지 목록으로 초기화됩니다.

2. **추천 받기(`get_recommendations` 메서드)**: 이 메서드는 사용자 선호도를 기반으로 Azure OpenAI 서비스에 전달할 프롬프트를 생성하고, Azure OpenAI API에 HTTP POST 요청을 보내 재순위화되고 점수 매겨진 여행지를 가져옵니다.

3. **프롬프트 생성(`generate_prompt` 메서드)**: 이 메서드는 사용자 선호도와 여행지 목록을 포함한 Azure OpenAI용 프롬프트를 구성합니다. 이 프롬프트가 모델에게 여행지를 선호도에 따라 재순위화하고 점수 매기도록 안내합니다.

4. **API 호출**: `requests` 라이브러리를 사용해 Azure OpenAI API 엔드포인트에 HTTP POST 요청을 합니다. 응답에는 재순위화되고 점수 매겨진 여행지가 포함됩니다.

5. **사용 예**: 여행사는 사용자의 관광과 다양한 문화 관심과 같은 선호도를 수집하고, Azure OpenAI 서비스를 사용해 여행지 추천에 대한 재순위화와 점수 매김을 받습니다.

`your_azure_openai_api_key`는 실제 Azure OpenAI API 키로, `https://your-endpoint.com/...`은 실제 Azure OpenAI 배포 엔드포인트 URL로 반드시 교체하십시오.

LLM을 재순위화와 점수 매기기에 활용함으로써 여행사는 고객에게 보다 개인화되고 관련성 높은 여행 추천을 제공하여 전반적인 경험을 향상시킬 수 있습니다.

### RAG: 프롬프트 기법 대 도구

검색 증강 생성(RAG)은 AI 에이전트 개발에서 프롬프트 기법이자 도구가 될 수 있습니다. 두 가지 차이를 이해하면 프로젝트에서 RAG를 더욱 효과적으로 활용할 수 있습니다.

#### RAG를 프롬프트 기법으로 사용하기

**무엇인가?**

- 프롬프트 기법으로서 RAG는 크고 방대한 말뭉치나 데이터베이스에서 관련 정보를 검색하도록 구체적인 쿼리나 프롬프트를 작성하는 것을 포함합니다. 이 정보를 사용해 응답이나 동작을 생성합니다.

**작동 방식:**

1. **프롬프트 작성**: 작업이나 사용자 입력에 기반해 잘 구조화된 프롬프트나 쿼리를 생성합니다.
2. **정보 검색**: 기존 지식 베이스나 데이터셋에서 프롬프트를 사용해 관련 데이터를 검색합니다.
3. **응답 생성**: 검색된 정보를 생성형 AI 모델과 결합해 포괄적이고 일관된 응답을 만듭니다.

**여행사 예시**:

- 사용자 입력: "파리에서 박물관을 방문하고 싶어요."
- 프롬프트: "파리의 주요 박물관을 찾아주세요."
- 검색 정보: 루브르 박물관, 오르세 미술관 등의 상세 정보.
- 생성 응답: "파리의 주요 박물관은 루브르 박물관, 오르세 미술관, 퐁피두 센터입니다."

#### RAG를 도구로 사용하기

**무엇인가?**

- 도구로서 RAG는 통합된 시스템으로 검색 및 생성 과정을 자동화하여 개발자가 각 쿼리에 대해 수동으로 프롬프트를 만들지 않고도 복잡한 AI 기능을 구현할 수 있게 합니다.

**작동 방식:**

1. <strong>통합</strong>: RAG를 AI 에이전트 아키텍처에 삽입해 자동으로 검색 및 생성 작업을 처리하게 합니다.
2. <strong>자동화</strong>: 사용자 입력 수신부터 최종 응답 생성까지 모든 과정을 명시적 프롬프트 없이 자동으로 관리합니다.
3. <strong>효율성</strong>: 검색 및 생성 과정을 간소화해 에이전트 성능을 향상시키고 더 빠르고 정확한 응답을 가능하게 합니다.

**여행사 예시**:

- 사용자 입력: "파리의 박물관을 방문하고 싶어요."
- RAG 도구: 박물관 정보를 자동으로 검색해 응답을 생성합니다.
- 생성 응답: "파리의 주요 박물관은 루브르 박물관, 오르세 미술관, 퐁피두 센터입니다."

### 비교

| 측면                    | 프롬프트 기법                                           | 도구                                                    |
|------------------------|---------------------------------------------------------|---------------------------------------------------------|
| **수동 대 자동**         | 각 쿼리에 대해 수동으로 프롬프트 작성                    | 검색 및 생성을 자동화하는 프로세스                        |
| <strong>제어</strong>                | 검색 프로세스에 대한 더 많은 제어 제공                   | 검색 및 생성 자동화로 간소화                             |
| <strong>유연성</strong>              | 특정 요구에 맞춘 맞춤형 프롬프트 허용                   | 대규모 구현에 더 효율적                                  |
| <strong>복잡성</strong>              | 프롬프트 작성 및 조정 필요                               | AI 에이전트 아키텍처 내 통합이 더 쉬움                   |

### 실용 예제

**프롬프트 기법 예제:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**도구 예제:**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### 관련성 평가

관련성 평가란 AI 에이전트 성능의 핵심 요소로, 에이전트가 검색하고 생성하는 정보가 사용자에게 적절하고 정확하며 유용한지 보장합니다. 여기서는 관련성 평가 방법과 실용적 예제 및 기법을 살펴보겠습니다.

#### 관련성 평가의 주요 개념

1. **컨텍스트 인지**:
   - 에이전트가 사용자의 쿼리 맥락을 이해해 관련 정보 검색 및 생성을 해야 합니다.
   - 예: 사용자가 "파리의 최고의 레스토랑"을 묻는다면 취향, 예산 등을 고려해야 합니다.

2. <strong>정확성</strong>:
   - 에이전트가 제공하는 정보는 사실에 근거하고 최신이어야 합니다.
   - 예: 리뷰가 좋은 현재 영업 중인 식당을 추천하고, 폐업이나 구식 정보는 배제.

3. **사용자 의도**:
   - 에이전트는 쿼리 뒤에 숨은 사용자의 의도를 추론해 가장 관련성 높은 정보를 제공해야 합니다.
   - 예: "저예산 호텔"을 묻는다면 합리적인 가격대 호텔을 우선 추천.

4. **피드백 루프**:
   - 지속적으로 사용자 피드백을 수집 및 분석해 관련성 평가 과정을 개선합니다.
   - 예: 이전 추천에 대한 사용자 평점 및 피드백을 반영해 향후 응답 개선.

#### 관련성 평가를 위한 실용적 기법

1. **관련성 점수 부여**:
   - 검색된 항목마다 사용자 쿼리 및 선호도와 얼마나 잘 맞는지에 따라 관련 점수를 매깁니다.
   - 예:

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. **필터링 및 랭킹**:
   - 관련성 낮은 항목을 걸러내고 남은 항목을 관련성 점수순으로 정렬합니다.
   - 예:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # 상위 10개 관련 항목 반환
     ```

3. **자연어 처리(NLP)**:
   - NLP 기법을 활용해 사용자의 쿼리를 이해하고 관련 정보를 검색합니다.
   - 예:

     ```python
     def process_query(query):
         # 사용자의 쿼리에서 주요 정보를 추출하기 위해 NLP 사용
         processed_query = nlp(query)
         return processed_query
     ```

4. **사용자 피드백 통합**:
   - 제공된 추천에 대한 사용자 피드백을 수집하고 이를 바탕으로 미래 관련성 평가에 반영합니다.
   - 예:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### 예제: 여행사에서 관련성 평가하기

여행사가 여행 추천의 관련성을 평가하는 실제 예입니다:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # 상위 10개 관련 항목 반환

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

# 사용 예시
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### 의도에 따른 검색

의도에 따른 검색이란 사용자의 쿼리 뒤에 숨은 목적이나 목표를 이해·해석하여 가장 관련성 높고 유용한 정보를 검색·생성하는 것입니다. 단순 키워드 매칭을 넘어서 사용자의 실제 필요와 상황을 파악하는 접근법입니다.

#### 의도에 따른 검색의 주요 개념

1. **사용자 의도 이해**:
   - 사용자 의도는 정보 탐색, 네비게이션, 거래 세 가지 주요 유형으로 구분할 수 있습니다.
     - **정보 탐색 의도**: 사용자가 주제에 대한 정보를 찾음(예: "파리 최고의 박물관은?").
     - **네비게이션 의도**: 특정 웹사이트나 페이지로 이동하려 함(예: "루브르 박물관 공식 사이트").
     - **거래 의도**: 예약이나 구매 등 거래를 수행하려 함(예: "파리행 비행기 예약하기").

2. **컨텍스트 인지**:
   - 쿼리 맥락을 분석해 정확히 사용자 의도를 식별합니다. 이전 상호작용, 사용자 선호, 현재 쿼리 세부사항 등을 고려합니다.

3. **자연어 처리(NLP)**:
   - 엔터티 인식, 감성 분석, 쿼리 파싱 등 NLP 기법을 활용해 사용자의 자연어 쿼리를 이해하고 해석합니다.

4. <strong>개인화</strong>:
   - 사용자의 이력, 선호, 피드백 등에 맞춰 검색 결과를 개인화해 관련성을 높입니다.

#### 실용적 예: 여행사에서 의도에 따른 검색 구현하기

여행사 예를 통해 의도 기반 검색이 어떻게 구현될 수 있는지 살펴봅시다.

1. **사용자 선호 수집하기**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **사용자 의도 이해하기**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **컨텍스트 인지**


   ```python
   def analyze_context(query, user_history):
       # 현재 쿼리를 사용자 기록과 결합하여 문맥을 이해하기 위해
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **검색 및 결과 개인화**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # 정보성 의도를 위한 예시 검색 로직
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # 탐색성 의도를 위한 예시 검색 로직
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # 거래성 의도를 위한 예시 검색 로직
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # 예시 개인화 로직
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # 상위 10개 개인화 결과 반환
   ```

5. **사용 예시**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. 도구로서 코드 생성

코드 생성 에이전트는 AI 모델을 사용하여 코드를 작성하고 실행하며, 복잡한 문제를 해결하고 작업을 자동화합니다.

### 코드 생성 에이전트

코드 생성 에이전트는 생성 AI 모델을 사용하여 코드를 작성하고 실행합니다. 이 에이전트들은 다양한 프로그래밍 언어로 코드를 생성하고 실행함으로써 복잡한 문제를 해결하고 작업을 자동화하며 귀중한 통찰을 제공합니다.

#### 실제 적용 사례

1. **자동 코드 생성**: 데이터 분석, 웹 스크래핑 또는 머신러닝과 같은 특정 작업을 위한 코드 스니펫 생성.
2. **SQL을 RAG로 사용**: 데이터베이스에서 데이터를 조회하고 조작하기 위한 SQL 쿼리 사용.
3. **문제 해결**: 알고리즘 최적화나 데이터 분석과 같은 특정 문제를 해결하기 위한 코드 생성 및 실행.

#### 예시: 데이터 분석용 코드 생성 에이전트

코드 생성 에이전트를 설계한다고 가정해 봅시다. 작동 방식은 다음과 같습니다:

1. <strong>작업</strong>: 데이터셋을 분석하여 추세와 패턴을 식별합니다.
2. <strong>단계</strong>:
   - 데이터셋을 데이터 분석 도구에 로드합니다.
   - 데이터를 필터링하고 집계하기 위한 SQL 쿼리를 생성합니다.
   - 쿼리를 실행하고 결과를 가져옵니다.
   - 결과를 활용해 시각화와 인사이트를 생성합니다.
3. **필요 자원**: 데이터셋 접근 권한, 데이터 분석 도구, SQL 기능.
4. <strong>경험</strong>: 이전 분석 결과를 활용하여 미래 분석의 정확성과 관련성을 향상합니다.

### 예시: 여행 에이전트를 위한 코드 생성 에이전트

이번 예에서는 여행 옵션 가져오기, 결과 필터링, 일정 작성 등 여행 계획을 돕는 코드 생성 에이전트, Travel Agent를 설계합니다. 이 에이전트는 생성 AI를 활용해 코드를 생성하고 실행할 수 있습니다.

#### 코드 생성 에이전트 개요

1. **사용자 선호도 수집**: 목적지, 여행 날짜, 예산, 관심사 등 사용자 입력을 수집합니다.
2. **데이터 조회용 코드 생성**: 항공편, 호텔, 명소 정보 조회를 위한 코드 스니펫을 생성합니다.
3. **생성된 코드 실행**: 실시간 정보를 조회하기 위해 생성된 코드를 실행합니다.
4. **일정 생성**: 조회한 데이터를 개인화된 여행 일정으로 정리합니다.
5. **피드백에 따른 조정**: 사용자 피드백을 받고 필요시 결과를 개선하기 위해 코드를 재생성합니다.

#### 단계별 구현

1. **사용자 선호도 수집**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **데이터 조회용 코드 생성**

   ```python
   def generate_code_to_fetch_data(preferences):
       # 예시: 사용자 선호도를 기반으로 항공편을 검색하는 코드를 생성합니다
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # 예시: 호텔을 검색하는 코드를 생성합니다
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **생성된 코드 실행**

   ```python
   def execute_code(code):
       # exec를 사용하여 생성된 코드를 실행합니다
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **일정 생성**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **피드백에 따른 조정**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # 사용자 피드백을 기반으로 환경설정을 조정합니다
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # 업데이트된 환경설정으로 코드를 재생성하고 실행합니다
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### 환경 인식 및 추론 활용

테이블의 스키마를 기반으로 쿼리 생성 과정을 환경 인식 및 추론을 활용해 향상시킬 수 있습니다.

어떻게 가능한지 예시를 살펴보겠습니다:

1. **스키마 이해**: 시스템이 테이블의 스키마를 이해하고 이를 바탕으로 쿼리 생성을 근거 있게 수행합니다.
2. **피드백 기반 조정**: 시스템이 사용자 선호도를 피드백에 따라 조정하고 스키마의 어떤 필드를 업데이트해야 할지 추론합니다.
3. **쿼리 생성 및 실행**: 새로운 선호도에 기반해 업데이트된 항공편 및 호텔 데이터를 가져오는 쿼리를 생성하고 실행합니다.

다음은 이 개념들을 통합한 업데이트된 Python 코드 예제입니다:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # 사용자 피드백을 기반으로 환경 설정 조정
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # 스키마를 기반으로 다른 관련 환경 설정 조정 추론
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # 스키마와 피드백을 기반으로 환경 설정을 조정하는 맞춤 논리
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # 업데이트된 환경 설정을 기반으로 항공편 데이터를 가져오는 코드 생성
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # 업데이트된 환경 설정을 기반으로 호텔 데이터를 가져오는 코드 생성
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # 코드 실행 시뮬레이션 및 모의 데이터 반환
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # 항공편, 호텔, 명소를 기반으로 일정 생성
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# 예시 스키마
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# 사용 예시
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# 업데이트된 환경 설정으로 코드 재생성 및 실행
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### 설명 - 피드백 기반 예약

1. **스키마 인식**: `schema` 딕셔너리는 피드백에 따라 선호도를 조정하는 방법을 정의하며, `favorites` 및 `avoid`와 같은 필드와 대응 조정을 포함합니다.
2. **선호도 조정(`adjust_based_on_feedback` 메서드)**: 이 메서드는 사용자 피드백과 스키마에 따라 선호도를 조정합니다.
3. **환경 기반 조정(`adjust_based_on_environment` 메서드)**: 이 메서드는 스키마와 피드백을 바탕으로 조정을 맞춤화합니다.
4. **쿼리 생성 및 실행**: 시스템은 조정된 선호도에 따라 업데이트된 항공편과 호텔 데이터를 불러오는 코드를 생성하고 실행을 시뮬레이션합니다.
5. **일정 생성**: 시스템은 새로운 항공편, 호텔, 명소 데이터를 기반으로 업데이트된 여행 일정을 만듭니다.

시스템을 환경 인식적으로 만들고 스키마에 기반한 추론을 적용함으로써, 더 정확하고 관련성 높은 쿼리를 생성해 더 나은 여행 추천과 개인화된 사용자 경험을 제공할 수 있습니다.

### RAG 기법으로서 SQL 활용

SQL(구조적 쿼리 언어)은 데이터베이스와 상호작용하는 강력한 도구입니다. RAG(Retrieval-Augmented Generation) 접근법의 일부로 사용하면, SQL은 데이터베이스에서 관련 데이터를 조회하여 AI 에이전트의 응답이나 행동 생성을 지원합니다. 여행 에이전트 문맥에서 SQL이 RAG 기법으로 어떻게 사용되는지 살펴봅니다.

#### 핵심 개념

1. **데이터베이스 상호작용**:
   - SQL은 데이터베이스 쿼리, 관련 정보 조회 및 데이터 조작에 사용됩니다.
   - 예시: 여행 데이터베이스에서 항공편 상세, 호텔 정보, 명소 데이터 조회.

2. **RAG와 통합**:
   - 사용자 입력 및 선호도에 기반하여 SQL 쿼리가 생성됩니다.
   - 조회된 데이터는 개인화된 추천이나 행동 생성을 위해 사용됩니다.

3. **동적 쿼리 생성**:
   - AI 에이전트는 상황과 사용자 필요에 맞게 동적으로 SQL 쿼리를 생성합니다.
   - 예시: 예산, 날짜, 관심사에 따라 필터링 조건을 맞춤화하는 SQL 쿼리 생성.

#### 적용 사례

- **자동 코드 생성**: 특정 작업을 위한 코드 스니펫 생성.
- **SQL을 RAG로 사용**: 데이터를 조작하기 위한 SQL 쿼리 활용.
- **문제 해결**: 문제 해결용 코드 생성 및 실행.

<strong>예시</strong>:
데이터 분석 에이전트:

1. <strong>작업</strong>: 데이터셋을 분석해 추세를 찾음.
2. <strong>단계</strong>:
   - 데이터셋을 로드.
   - 데이터를 필터링하는 SQL 쿼리 생성.
   - 쿼리 실행 및 결과 수집.
   - 시각화 및 인사이트 생성.
3. <strong>자원</strong>: 데이터셋 접근, SQL 기능.
4. <strong>경험</strong>: 이전 결과를 활용해 미래 분석 향상.

#### 실용적 예시: Travel Agent에서 SQL 사용

1. **사용자 선호도 수집**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **SQL 쿼리 생성**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **SQL 쿼리 실행**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **추천 생성**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### SQL 쿼리 예시

1. **항공편 쿼리**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **호텔 쿼리**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **명소 쿼리**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

RAG 기법의 일부로 SQL을 활용함으로써, Travel Agent와 같은 AI 에이전트는 관련 데이터를 동적으로 조회하고 이를 활용해 정확하고 개인화된 추천을 제공할 수 있습니다.

### 메타인지 예시

메타인지 구현을 보여주기 위해, 문제를 해결하는 과정에서 *자신의 의사결정 과정을 반성하는* 간단한 에이전트를 만들어 보겠습니다. 이 예에서는 호텔 선택을 최적화하려고 시도하지만, 오류나 최적이 아닌 선택을 했을 때 스스로 추론을 평가하고 전략을 조정하는 시스템을 구축합니다.

가격과 품질을 조합하여 호텔을 선택하는 기본 예시를 시뮬레이션하며, 의사결정을 "반성"하고 그에 따라 조정합니다.

#### 이것이 메타인지의 예시인 이유:

1. **초기 결정**: 에이전트는 품질 영향을 이해하지 못한 채 가장 저렴한 호텔을 선택합니다.
2. **반성 및 평가**: 초기 선택 후, 사용자 피드백을 통해 호텔이 "나쁜" 선택인지 검사하고, 품질이 너무 낮다고 판단되면 자신의 추론을 반성합니다.
3. **전략 조정**: 에이전트는 반성에 따라 전략을 수정해, "가장 저렴한"에서 "최고 품질" 선택으로 전환하며, 이후 의사결정 과정을 개선합니다.

예시는 다음과 같습니다:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # 이전에 선택된 호텔을 저장합니다
        self.corrected_choices = []  # 수정된 선택을 저장합니다
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # 사용 가능한 전략들

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # 마지막 선택이 좋았는지 여부를 알려주는 사용자 피드백이 있다고 가정합니다
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # 이전 선택이 만족스럽지 않은 경우 전략을 조정합니다
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# 호텔 목록(가격 및 품질)을 시뮬레이션합니다
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# 에이전트를 생성합니다
agent = HotelRecommendationAgent()

# 1단계: 에이전트가 "가장 저렴한" 전략을 사용해 호텔을 추천합니다
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# 2단계: 에이전트가 선택을 되돌아보고 필요에 따라 전략을 조정합니다
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# 3단계: 에이전트가 조정된 전략을 사용하여 다시 추천합니다
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### 에이전트의 메타인지 능력

핵심은 에이전트가:
- 이전 선택과 의사결정 과정을 평가하고,
- 그 반성에 따라 전략을 조정하는, 즉 메타인지적 행동을 보인다는 점입니다.

이는 시스템이 내부 피드백에 기반하여 추론 과정을 조정할 수 있는 간단한 형태의 메타인지입니다.

### 결론

메타인지는 AI 에이전트의 역량을 크게 향상시킬 수 있는 강력한 도구입니다. 메타인지적 프로세스를 통합함으로써, 더 지능적이고 적응력있으며 효율적인 에이전트를 설계할 수 있습니다. 추가 자료를 활용해 AI 에이전트에서의 메타인지의 흥미로운 세계를 더 깊이 탐구해 보세요.

### 메타인지 디자인 패턴에 대한 추가 질문이 있으신가요?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)에 참여하여 다른 학습자들과 만나고, 오피스 아워에 참석하며, AI 에이전트 관련 질문을 해결해 보세요.

## 이전 강의

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## 다음 강의

[AI Agents in Production](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->