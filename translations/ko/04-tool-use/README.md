[![How to Design Good AI Agents](../../../translated_images/ko/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(위 이미지를 클릭하여 이 수업의 동영상을 시청하세요)_

# 도구 사용 디자인 패턴

도구는 AI 에이전트가 더 넓은 범위의 기능을 가지도록 해주기 때문에 흥미롭습니다. 에이전트가 수행할 수 있는 동작이 제한된 세트에 머무르는 대신, 도구를 추가함으로써 에이전트는 이제 다양한 동작을 수행할 수 있습니다. 이 장에서는 AI 에이전트가 특정 도구를 사용하여 목표를 달성하는 방법을 설명하는 도구 사용 디자인 패턴을 살펴보겠습니다.

## 소개

이번 수업에서는 다음 질문들에 답하고자 합니다:

- 도구 사용 디자인 패턴이란 무엇인가?
- 어디에 적용할 수 있는가?
- 디자인 패턴을 구현하는 데 필요한 요소/빌딩 블록은 무엇인가?
- 신뢰할 수 있는 AI 에이전트를 구축하기 위해 도구 사용 디자인 패턴을 사용할 때의 특별한 고려사항은 무엇인가?

## 학습 목표

이 수업을 완료하면 다음을 수행할 수 있습니다:

- 도구 사용 디자인 패턴과 그 목적을 정의할 수 있다.
- 도구 사용 디자인 패턴이 적용 가능한 사용 사례를 식별할 수 있다.
- 디자인 패턴을 구현하는 데 필요한 핵심 요소를 이해할 수 있다.
- 이 디자인 패턴을 사용하는 AI 에이전트의 신뢰성을 보장하기 위한 고려사항을 인식할 수 있다.

## 도구 사용 디자인 패턴이란 무엇인가?

<strong>도구 사용 디자인 패턴</strong>은 LLM이 특정 목표를 달성하기 위해 외부 도구와 상호작용할 수 있게 하는 데 중점을 둡니다. 도구는 에이전트가 실행하여 동작을 수행할 수 있는 코드입니다. 도구는 계산기와 같은 단순한 함수거나 주식 가격 조회나 일기 예보와 같은 타사 서비스에 대한 API 호출일 수 있습니다. AI 에이전트의 맥락에서 도구는 <strong>모델이 생성한 함수 호출</strong>에 응답하여 에이전트에 의해 실행되도록 설계되었습니다.

## 어디에 적용할 수 있는가?

AI 에이전트는 도구를 활용하여 복잡한 작업을 완료하거나 정보를 검색하고 결정을 내릴 수 있습니다. 도구 사용 디자인 패턴은 데이터베이스, 웹 서비스 또는 코드 인터프리터와 같이 외부 시스템과 동적으로 상호작용해야 하는 시나리오에서 자주 사용됩니다. 다음과 같은 다양한 사용 사례에 유용합니다:

- **동적 정보 검색:** 에이전트가 최신 데이터를 가져오기 위해 외부 API나 데이터베이스에 질의할 수 있습니다(예: 데이터 분석을 위한 SQLite 데이터베이스 질의, 주식 가격 또는 날씨 정보 조회).
- **코드 실행 및 해석:** 수학 문제 해결, 보고서 생성 또는 시뮬레이션 수행을 위해 코드나 스크립트를 실행할 수 있습니다.
- **워크플로 자동화:** 작업 스케줄러, 이메일 서비스 또는 데이터 파이프라인과 같은 도구를 통합하여 반복적이거나 다단계 워크플로를 자동화합니다.
- **고객 지원:** CRM 시스템, 티켓팅 플랫폼 또는 지식 베이스와 상호작용하여 사용자 문의를 해결할 수 있습니다.
- **콘텐츠 생성 및 편집:** 문법 검사기, 텍스트 요약기 또는 콘텐츠 안전성 평가기와 같은 도구를 활용하여 콘텐츠 생성 작업을 지원할 수 있습니다.

## 도구 사용 디자인 패턴을 구현하는 데 필요한 요소/빌딩 블록은 무엇인가?

이 빌딩 블록들은 AI 에이전트가 다양한 작업을 수행할 수 있도록 합니다. 도구 사용 디자인 패턴 구현에 필요한 핵심 요소를 살펴보겠습니다:

- **함수/도구 스키마**: 함수 이름, 목적, 필수 매개변수 및 예상 출력물을 포함한 사용 가능한 도구들의 세부 정의. 이러한 스키마를 통해 LLM은 어떤 도구가 사용 가능한지, 어떻게 유효한 요청을 구성할지 이해할 수 있습니다.

- **함수 실행 로직**: 사용자의 의도와 대화 맥락에 따라 도구가 어떻게, 언제 호출되는지를 제어합니다. 플래너 모듈, 라우팅 메커니즘 또는 도구 사용을 동적으로 결정하는 조건부 흐름 등이 포함될 수 있습니다.

- **메시지 처리 시스템**: 사용자 입력, LLM 응답, 도구 호출 및 도구 출력 간의 대화 흐름을 관리하는 구성요소들.

- **도구 통합 프레임워크**: 간단한 함수부터 복잡한 외부 서비스까지 에이전트를 다양한 도구에 연결하는 인프라.

- **오류 처리 및 검증**: 도구 실행 실패 처리, 매개변수 검증, 예상치 못한 응답 관리 메커니즘.

- **상태 관리**: 대화 맥락, 이전 도구 상호작용 및 지속적인 데이터를 추적하여 다회차 상호작용 간 일관성 보장.

다음으로 함수/도구 호출에 대해 좀 더 자세히 살펴보겠습니다.

### 함수/도구 호출

함수 호출은 대형 언어 모델(LLM)이 도구와 상호작용할 수 있게 하는 주된 방법입니다. '함수(Function)'와 '도구(Tool)'는 종종 같은 의미로 사용되는데, '함수'는 작업을 수행하는 재사용 가능한 코드 블록이며, 이것이 에이전트가 사용하는 '도구'이기 때문입니다. 함수를 호출하려면 LLM이 사용자의 요청과 함수 설명을 비교해야 합니다. 이를 위해 사용 가능한 모든 함수에 대한 설명이 담긴 스키마가 LLM에 전달됩니다. LLM은 작업에 가장 적합한 함수를 선택하고 이름과 인수를 반환합니다. 선택된 함수가 호출되고, 그 응답이 LLM에 되돌아가 사용자의 요청에 응답하는 데 사용됩니다.

개발자가 에이전트용 함수 호출을 구현하려면 다음이 필요합니다:

1. 함수 호출을 지원하는 LLM 모델
2. 함수 설명이 포함된 스키마
3. 각 함수에 해당하는 코드

도시의 현재 시간을 조회하는 예제로 설명해보겠습니다:

1. **함수 호출을 지원하는 LLM 초기화:**

    모든 모델이 함수 호출을 지원하는 것은 아니므로 사용하는 LLM이 지원하는지 확인하는 것이 중요합니다. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a>는 함수 호출을 지원합니다. Azure OpenAI 클라이언트를 시작하면 됩니다.

    ```python
    # Azure OpenAI 클라이언트를 초기화합니다
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **함수 스키마 생성**:

    다음으로 함수 이름, 함수가 수행하는 작업에 대한 설명, 함수 매개변수 이름과 설명이 포함된 JSON 스키마를 정의합니다.
    그런 다음 이 스키마와 사용자의 샌프란시스코 시간 조회 요청을 이전에 생성한 클라이언트로 전달합니다. 중요한 점은 <strong>도구 호출(tool call)</strong>이 반환되며, 최종 답변이 아니라는 점입니다. 앞서 언급했듯이 LLM은 작업에 적합하다고 선택한 함수 이름과 전달될 인수를 반환합니다.

    ```python
    # 모델이 읽을 함수 설명
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # 초기 사용자 메시지
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # 첫 번째 API 호출: 모델에게 함수를 사용하도록 요청
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # 모델의 응답 처리
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **작업 수행을 위한 함수 코드:**

    이제 LLM이 실행할 함수를 선택했으므로, 작업을 수행하는 코드를 구현하고 실행해야 합니다.
    현재 시간을 가져오는 코드를 Python으로 구현할 수 있습니다. 또한 최종 결과를 얻기 위해 response_message에서 함수 이름과 인수를 추출하는 코드를 작성해야 합니다.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # 함수 호출 처리
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # 두 번째 API 호출: 모델에서 최종 응답 받기
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

함수 호출은 대부분, 아니면 모든 에이전트 도구 사용 디자인의 핵심이지만, 스크래치부터 구현하는 것은 때때로 어려울 수 있습니다.
[Lesson 2](../../../02-explore-agentic-frameworks)에서 배웠듯이, 에이전틱 프레임워크는 도구 사용을 구현하기 위한 미리 만들어진 빌딩 블록을 제공합니다.
 
## 에이전틱 프레임워크를 이용한 도구 사용 예제

다음은 다양한 에이전틱 프레임워크를 사용하여 도구 사용 디자인 패턴을 구현하는 예시입니다:

### Microsoft 에이전트 프레임워크

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft 에이전트 프레임워크</a>는 AI 에이전트를 구축하기 위한 오픈 소스 AI 프레임워크입니다. `@tool` 데코레이터를 사용하여 도구를 Python 함수로 정의하면 함수 호출 사용을 단순화합니다. 프레임워크는 모델과 코드 간의 상호작용을 자동으로 처리합니다. 또한 `AzureAIProjectAgentProvider`를 통해 파일 검색이나 코드 인터프리터와 같은 미리 만들어진 도구에 접근할 수 있습니다.

다음 다이어그램은 Microsoft 에이전트 프레임워크에서 함수 호출 프로세스를 보여줍니다:

![function calling](../../../translated_images/ko/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft 에이전트 프레임워크에서 도구는 데코레이터된 함수로 정의됩니다. 이전에 보았던 `get_current_time` 함수를 `@tool` 데코레이터를 사용해 도구로 변환할 수 있습니다. 프레임워크는 자동으로 함수와 매개변수를 직렬화하여 LLM에 보낼 스키마를 생성합니다.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# 클라이언트 생성
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# 에이전트를 생성하고 도구와 함께 실행하기
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI 에이전트 서비스

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI 에이전트 서비스</a>는 개발자가 기본 컴퓨팅 및 저장 리소스를 관리할 필요 없이 안전하게 고품질의 확장 가능한 AI 에이전트를 구축, 배포 및 확장할 수 있도록 설계된 최신 에이전틱 프레임워크입니다. 기업용 애플리케이션에 특히 유용하며, 엔터프라이즈급 보안을 갖춘 완전 관리형 서비스입니다.

LLM API를 직접 개발하는 것과 비교할 때, Azure AI 에이전트 서비스가 제공하는 장점은 다음과 같습니다:

- 자동 도구 호출 – 도구 호출 구문 분석, 도구 실행, 응답 처리 작업이 서버 측에서 모두 처리됩니다.
- 안전하게 관리되는 데이터 – 자체 대화 상태를 관리하는 대신, 필요한 모든 정보를 저장하는 `threads`를 활용할 수 있습니다.
- 바로 사용할 수 있는 도구들 – Bing, Azure AI Search, Azure Functions 등 데이터 소스와 상호작용할 수 있는 도구를 제공합니다.

Azure AI 에이전트 서비스의 도구는 두 가지 범주로 나뉩니다:

1. 지식 도구:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing 검색 기반 지식</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">파일 검색</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 검색</a>

2. 동작 도구:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">함수 호출</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">코드 인터프리터</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 정의 도구</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

에이전트 서비스는 이러한 도구들을 `toolset`으로 함께 사용할 수 있게 해줍니다. 또한 특정 대화 내역을 추적하는 `threads`를 활용합니다.

컨토소(Contoso)라는 회사의 영업 담당 에이전트라고 가정해봅시다. 영업 데이터에 관한 질문에 답할 수 있는 대화형 에이전트를 개발하려고 합니다.

다음 이미지는 Azure AI 에이전트 서비스를 사용하여 영업 데이터를 분석하는 방법을 보여줍니다:

![Agentic Service In Action](../../../translated_images/ko/agent-service-in-action.34fb465c9a84659e.webp)

이 서비스를 사용하여 이들 도구를 활용하려면 클라이언트를 생성하고 도구 또는 도구 세트를 정의할 수 있습니다. 실무 구현을 위해 다음 Python 코드를 사용할 수 있습니다. LLM은 도구 세트를 보고 사용자가 만든 함수 `fetch_sales_data_using_sqlite_query`를 사용할지, 아니면 미리 만들어진 코드 인터프리터를 사용할지 결정할 수 있습니다.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_functions.py 파일에서 찾을 수 있는 fetch_sales_data_using_sqlite_query 함수입니다.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# 도구 세트 초기화
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query 함수를 사용하여 함수 호출 에이전트를 초기화하고 도구 세트에 추가합니다.
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# 코드 인터프리터 도구를 초기화하고 도구 세트에 추가합니다.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 신뢰할 수 있는 AI 에이전트를 구축하기 위해 도구 사용 디자인 패턴을 사용할 때의 특별한 고려사항은 무엇인가?

LLM이 동적으로 생성한 SQL에 대한 일반적인 우려는 보안 문제이며, 특히 SQL 인젝션이나 데이터베이스를 삭제하거나 변조하는 악의적 행위의 위험이 있습니다. 이러한 우려는 데이터베이스 접근 권한을 적절히 구성하면 효과적으로 완화할 수 있습니다. 대부분 데이터베이스에서는 읽기 전용으로 설정하는 것이 여기에 해당합니다. PostgreSQL 또는 Azure SQL과 같은 데이터베이스 서비스에서는 앱에 읽기 전용(SELECT) 역할을 할당해야 합니다.

앱을 안전한 환경에서 실행하는 것은 보호를 더욱 강화합니다. 엔터프라이즈 환경에서는 데이터가 일반적으로 운영 시스템에서 추출 및 변환되어 읽기 전용 데이터베이스나 데이터 웨어하우스에 사용자 친화적 스키마로 저장됩니다. 이 접근법은 데이터의 보안성과 성능 및 접근성을 최적화하며, 앱이 제한된 읽기 전용 권한만 갖도록 보장합니다.

## 샘플 코드

- Python: [에이전트 프레임워크](./code_samples/04-python-agent-framework.ipynb)
- .NET: [에이전트 프레임워크](./code_samples/04-dotnet-agent-framework.md)

## 도구 사용 디자인 패턴에 대해 더 궁금한 점이 있나요?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)에 참여하여 다른 학습자와 만나고, 오피스 아워에 참석하며, AI 에이전트 관련 질문에 답변을 받아보세요.

## 추가 자료

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI 에이전트 서비스 워크숍</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso 창작 작가 다중 에이전트 워크숍</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft 에이전트 프레임워크 개요</a>

## 이전 수업

[에이전틱 디자인 패턴 이해하기](../03-agentic-design-patterns/README.md)

## 다음 수업
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->