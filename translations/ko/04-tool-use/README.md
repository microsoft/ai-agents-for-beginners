[![좋은 AI 에이전트 설계 방법](../../../translated_images/ko/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(위 이미지 클릭 시 이 수업의 동영상 시청)_

# 도구 사용 디자인 패턴

도구는 AI 에이전트가 더 넓은 범위의 능력을 갖추게 해주기 때문에 흥미롭습니다. 에이전트가 수행할 수 있는 작업들이 제한된 집합에만 국한되는 대신 도구를 추가함으로써, 에이전트는 훨씬 다양한 작업을 수행할 수 있게 됩니다. 본 장에서는 AI 에이전트가 특정 도구를 사용하여 목표를 달성하는 방법을 설명하는 도구 사용 디자인 패턴을 살펴보겠습니다.

## 소개

이번 수업에서는 다음 질문들에 답하려고 합니다:

- 도구 사용 디자인 패턴이란 무엇인가?
- 어떤 사용 사례에 적용할 수 있는가?
- 디자인 패턴 구현에 필요한 요소/구성 블록은 무엇인가?
- 신뢰할 수 있는 AI 에이전트를 구축하기 위해 도구 사용 디자인 패턴 사용 시 고려할 특별한 사항은 무엇인가?

## 학습 목표

이 수업을 마치면 다음을 할 수 있습니다:

- 도구 사용 디자인 패턴과 그 목적 정의하기.
- 도구 사용 디자인 패턴이 적용 가능한 사용 사례 식별하기.
- 디자인 패턴 구현에 필요한 주요 요소 이해하기.
- 이 디자인 패턴을 사용한 AI 에이전트 신뢰성 확보를 위한 고려사항 인식하기.

## 도구 사용 디자인 패턴이란 무엇인가?

<strong>도구 사용 디자인 패턴</strong>은 LLM이 특정 목표를 달성하기 위해 외부 도구와 상호작용할 수 있도록 권한을 부여하는 데 중점을 둡니다. 도구는 에이전트가 실행할 수 있는 코드로, 단순한 계산기 함수이거나 주식 시세 조회, 날씨 예보 같은 타사 서비스에 대한 API 호출일 수 있습니다. AI 에이전트 맥락에서는 도구가 <strong>모델 생성 함수 호출</strong>에 응답하여 실행되도록 설계됩니다.

## 어떤 사용 사례에 적용할 수 있는가?

AI 에이전트는 도구를 활용하여 복잡한 작업을 완료하거나 정보를 검색하거나 결정을 내릴 수 있습니다. 도구 사용 디자인 패턴은 데이터베이스, 웹 서비스, 코드 인터프리터 같은 외부 시스템과의 동적 상호작용이 필요한 시나리오에서 자주 사용됩니다. 이 기능은 다음과 같은 다양한 사용 사례에 유용합니다:

- **동적 정보 검색:** 에이전트가 외부 API 또는 데이터베이스에서 최신 데이터를 조회할 수 있습니다 (예: 데이터 분석을 위한 SQLite 데이터베이스 쿼리, 주식 가격 또는 날씨 정보 조회).
- **코드 실행 및 해석:** 에이전트가 수학 문제 해결, 보고서 생성, 시뮬레이션 수행을 위해 코드나 스크립트를 실행할 수 있습니다.
- **워크플로우 자동화:** 작업 스케줄러, 이메일 서비스, 데이터 파이프라인과 같은 도구를 통합하여 반복적이거나 다단계 워크플로우 자동화.
- **고객 지원:** 에이전트가 CRM 시스템, 티켓팅 플랫폼 또는 지식 기반과 상호작용하여 사용자 문의 해결.
- **콘텐츠 생성 및 편집:** 문법 검사기, 텍스트 요약기, 콘텐츠 안전 평가기 같은 도구를 활용하여 콘텐츠 제작 도움.

## 도구 사용 디자인 패턴 구현에 필요한 요소/구성 블록은 무엇인가?

이 구성 블록들은 AI 에이전트가 다양한 작업을 수행할 수 있게 합니다. 도구 사용 디자인 패턴 구현에 필요한 주요 요소를 살펴보겠습니다:

- **함수/도구 스키마**: 함수 이름, 목적, 필수 매개변수, 예상 출력 등 사용 가능한 도구의 상세 정의. 이러한 스키마는 LLM이 어떤 도구가 사용 가능한지 이해하고 유효한 요청을 구성하는 데 도움을 줍니다.

- **함수 실행 로직**: 사용자 의도와 대화 맥락에 따라 도구가 언제 어떻게 호출되는지 관리합니다. 플래너 모듈, 라우팅 메커니즘, 조건부 흐름 등이 포함되어 도구 사용을 동적으로 결정합니다.

- **메시지 처리 시스템**: 사용자 입력, LLM 응답, 도구 호출 및 결과 출력 간의 대화 흐름을 관리하는 구성요소.

- **도구 통합 프레임워크**: 단순 함수든 복잡한 외부 서비스든 에이전트가 다양한 도구와 연결되게 하는 인프라.

- **오류 처리 및 검증**: 도구 실행 실패 처리, 매개변수 검증, 예기치 않은 응답 관리 메커니즘.

- **상태 관리**: 대화 맥락, 이전 도구 상호작용, 지속 데이터 추적을 통해 다회 대화 간 일관성 유지.

다음으로 함수/도구 호출에 대해 좀 더 자세히 살펴보겠습니다.
 
### 함수/도구 호출

함수 호출은 대형 언어 모델(LLM)이 도구와 상호작용할 수 있도록 하는 주요 방법입니다. 함수와 도구는 자주 혼용되는데, '함수'(재사용 가능한 코드 블록)는 에이전트가 작업 수행에 사용하는 '도구'이기 때문입니다. 함수를 호출하려면 LLM이 사용자 요청을 함수 설명과 비교해야 하며, 이를 위해 모든 사용 가능한 함수 설명을 담은 스키마가 LLM에 전달됩니다. LLM은 작업에 가장 적절한 함수를 선택해 이름과 인수를 반환합니다. 선택된 함수가 호출되고, 그 응답이 LLM에 전달되며, LLM은 이를 바탕으로 사용자 요청에 응답합니다.

개발자가 에이전트 함수 호출을 구현하려면 다음이 필요합니다:

1. 함수 호출을 지원하는 LLM 모델
2. 함수 설명을 포함한 스키마
3. 설명된 각 함수에 대한 코드

현재 도시의 시간을 가져오는 예제를 사용해 설명해 보겠습니다:

1. **함수 호출을 지원하는 LLM 초기화:**

    모든 모델이 함수 호출을 지원하지 않으므로, 사용하는 LLM이 이를 지원하는지 확인하는 것이 중요합니다.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a>는 함수 호출을 지원합니다. 우리는 안정적인 `/openai/v1/` 엔드포인트(별도의 `api_version` 불필요)를 사용하는 Azure OpenAI <strong>Responses API</strong>를 통해 OpenAI 클라이언트를 시작할 수 있습니다.

    ```python
    # Azure OpenAI(OpenAI 응답 API, v1 엔드포인트)용 OpenAI 클라이언트를 초기화합니다
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **함수 스키마 생성**:

    다음으로 함수 이름, 함수 설명, 함수 매개변수 이름과 설명을 포함하는 JSON 스키마를 정의합니다.
    이 스키마를 앞서 생성한 클라이언트에 전달하고, 샌프란시스코 시간을 찾는 사용자 요청과 함께 사용합니다. 중요한 점은 <strong>도구 호출</strong>이 반환된다는 것, 즉 질문에 대한 최종 답변이 아니라는 것입니다. 앞서 설명했듯이, LLM은 작업에 선택한 함수 이름과 전달할 인수를 반환합니다.

    ```python
    # 모델이 읽을 함수 설명 (Responses API 플랫 도구 형식)
    tools = [
        {
            "type": "function",
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
    ]
    ```
   
    ```python
  
    # 초기 사용자 메시지
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # 첫 번째 API 호출: 모델에 함수 사용 요청
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API는 response.output에 function_call 항목으로 도구 호출을 반환합니다.
    # 다음 차례에 모델이 전체 문맥을 가질 수 있도록 대화에 추가하세요.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **작업 수행에 필요한 함수 코드:**

    이제 LLM이 실행할 함수를 선택했으므로, 그 작업을 수행하는 코드를 구현하고 실행해야 합니다.
    파이썬으로 현재 시간을 구하는 코드를 구현할 수 있습니다. 또한 최종 결과를 얻기 위해 response_message에서 함수 이름과 인수를 추출하는 코드도 작성해야 합니다.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # 도구 결과를 function_call_output 항목으로 반환
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # 두 번째 API 호출: 모델에서 최종 응답 가져오기
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

함수 호출은 대부분의, 아니 거의 모든 에이전트 도구 사용 설계의 핵심이지만, 처음부터 구현하는 것은 때때로 어려울 수 있습니다.
[수업 2](../../../02-explore-agentic-frameworks)에서 배운 바와 같이, 에이전틱 프레임워크는 도구 사용 구현을 위한 미리 만들어진 빌딩 블록을 제공합니다.
 
## 에이전틱 프레임워크를 이용한 도구 사용 예제

다양한 에이전틱 프레임워크를 사용해 도구 사용 디자인 패턴을 구현하는 몇 가지 예시는 다음과 같습니다:

### Microsoft 에이전트 프레임워크

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft 에이전트 프레임워크</a>는 AI 에이전트를 구축하기 위한 오픈 소스 AI 프레임워크입니다. `@tool` 데코레이터로 도구를 파이썬 함수로 정의할 수 있게 하여 함수 호출을 단순화합니다. 프레임워크는 모델과 코드 간 통신을 처리합니다. 또한 `FoundryChatClient`를 통해 파일 검색, 코드 인터프리터 같은 미리 만들어진 도구도 제공합니다.

아래 그림은 Microsoft 에이전트 프레임워크로 함수 호출 과정을 보여줍니다:

![function calling](../../../translated_images/ko/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft 에이전트 프레임워크에서는 도구가 데코레이터 함수로 정의됩니다. 앞서 본 `get_current_time` 함수를 `@tool` 데코레이터를 사용해 도구로 전환할 수 있습니다. 프레임워크는 함수와 매개변수를 자동으로 직렬화하여 LLM에 보낼 스키마를 생성합니다.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# 클라이언트 생성
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# 에이전트를 생성하고 도구와 함께 실행하기
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry 에이전트 서비스

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry 에이전트 서비스</a>는 개발자가 근간의 컴퓨팅 및 저장소 자원을 관리할 필요 없이 보안적으로 고품질 확장 가능한 AI 에이전트를 구축, 배포, 운영할 수 있도록 설계된 최신 에이전틱 프레임워크입니다. 기업용 애플리케이션에 특히 유용하며, 완전 관리형 서비스로 기업급 보안을 제공합니다.

LLM API를 직접 사용할 때와 비교할 때, Microsoft Foundry 에이전트 서비스는 다음과 같은 장점을 제공합니다:

- 자동 도구 호출 – 도구 호출 분석, 실행, 응답 처리 과정이 서버 측에서 자동으로 처리됩니다.
- 안전하게 관리되는 데이터 – 자체 대화 상태를 관리하는 대신, threads를 이용해 필요한 모든 정보를 저장할 수 있습니다.
- 즉시 사용 가능한 도구 – Bing, Azure AI Search, Azure Functions 같은 데이터 소스와 상호작용할 수 있는 도구 제공.

Microsoft Foundry 에이전트 서비스에서 제공되는 도구는 두 가지 범주로 나눌 수 있습니다:

1. 지식 도구:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing 검색 기반</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">파일 검색</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 검색</a>

2. 실행 도구:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">함수 호출</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">코드 인터프리터</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 정의 도구</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

에이전트 서비스는 이 도구들을 `toolset`으로 함께 사용할 수 있게 하며, 특정 대화의 메시지 이력을 추적하는 `threads`를 활용합니다.

여러분이 Contoso라는 회사의 영업 담당자라고 가정해보겠습니다. 여러분은 영업 데이터에 관한 질문에 답할 수 있는 대화형 에이전트를 개발하고자 합니다.

다음 이미지는 Microsoft Foundry 에이전트 서비스를 사용해 영업 데이터를 분석하는 방법을 보여줍니다:

![에이전트 서비스 작동 예](../../../translated_images/ko/agent-service-in-action.34fb465c9a84659e.webp)

이 서비스에서 도구 또는 도구 세트를 정의하기 위해 클라이언트를 생성할 수 있습니다. 실제 구현에서는 다음 파이썬 코드를 사용할 수 있습니다. LLM은 도구 세트를 보고 사용자 생성 함수 `fetch_sales_data_using_sqlite_query`를 쓸지, 미리 만들어진 코드 인터프리터를 쓸지 사용자 요청에 따라 결정할 수 있습니다.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_functions.py 파일에 있는 fetch_sales_data_using_sqlite_query 함수입니다.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# 도구 세트 초기화
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query 함수를 사용하여 함수 호출 에이전트를 초기화하고 도구 세트에 추가
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# 코드 인터프리터 도구를 초기화하고 도구 세트에 추가하기.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 신뢰할 수 있는 AI 에이전트 구축을 위한 도구 사용 디자인 패턴 이용 시 특별 고려사항은?

LLM이 동적으로 생성한 SQL에 흔히 제기되는 보안 우려는 SQL 인젝션이나 데이터베이스 삭제 또는 변조 같은 악의적 행위 위험입니다. 이러한 우려는 적절한 데이터베이스 접근 권한 설정으로 효과적으로 완화할 수 있습니다. 대부분의 데이터베이스는 읽기 전용 설정을 권장하며, PostgreSQL 또는 Azure SQL 같은 서비스에서는 앱에 읽기 전용(SELECT) 역할을 부여합니다.

앱을 안전한 환경에서 실행하는 것도 보호를 강화합니다. 기업 시나리오에서는 운영 시스템에서 데이터를 추출해 읽기 전용 데이터베이스 또는 데이터 웨어하우스로 변환하고 사용자 친화적 스키마를 적용합니다. 이런 접근은 데이터 보안, 성능 및 접근성 최적화, 그리고 앱 권한을 제한된 읽기 전용으로 하는 데 도움이 됩니다.

## 샘플 코드

- 파이썬: [에이전트 프레임워크](./code_samples/04-python-agent-framework.ipynb)
- .NET: [에이전트 프레임워크](./code_samples/04-dotnet-agent-framework.md)

## 도구 사용 디자인 패턴에 대해 더 궁금한 점이 있으신가요?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)에 참여해 다른 학습자들과 만나고, 오피스 아워에 참석하며, AI 에이전트 관련 질문에 답을 얻으세요.

## 추가 자료

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI 에이전트 서비스 워크샵</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer 다중 에이전트 워크샵</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft 에이전트 프레임워크 개요</a>


## 이 에이전트 스모크 테스트하기 (선택 사항)

[Lesson 16](../16-deploying-scalable-agents/README.md)에서 에이전트 배포 방법을 배운 후, 이 수업의 `TravelToolAgent`가 여전히 도구를 호출하고 응답하는지 [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json)으로 스모크 테스트할 수 있습니다. 실행 방법은 [`tests/README.md`](../tests/README.md)를 참조하세요.

## 이전 강의

[Agentic Design Patterns 이해하기](../03-agentic-design-patterns/README.md)

## 다음 강의

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->