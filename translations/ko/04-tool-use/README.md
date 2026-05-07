[![좋은 AI 에이전트 설계 방법](../../../translated_images/ko/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(위의 이미지를 클릭하면 이 수업의 비디오를 볼 수 있습니다)_

# 도구 사용 디자인 패턴

도구는 AI 에이전트가 더 넓은 범위의 기능을 갖도록 해 주기 때문에 흥미롭습니다. 에이전트가 수행할 수 있는 동작이 제한되는 대신, 도구를 추가하면 에이전트가 다양한 작업을 수행할 수 있게 됩니다. 이 장에서는 AI 에이전트가 목표를 달성하기 위해 특정 도구를 사용할 수 있는 방법을 설명하는 도구 사용 디자인 패턴을 살펴봅니다.

## 소개

이 수업에서는 다음 질문들에 답하려고 합니다:

- 도구 사용 디자인 패턴이란 무엇인가?
- 어떤 사용 사례에 적용될 수 있는가?
- 디자인 패턴을 구현하는 데 필요한 요소/구성 블록은 무엇인가?
- 신뢰할 수 있는 AI 에이전트를 구축하기 위해 도구 사용 디자인 패턴을 사용할 때의 특별한 고려사항은 무엇인가?

## 학습 목표

이 수업을 완료한 후, 당신은 다음을 할 수 있게 됩니다:

- 도구 사용 디자인 패턴과 그 목적을 정의할 수 있다.
- 도구 사용 디자인 패턴이 적용 가능한 사용 사례를 식별할 수 있다.
- 디자인 패턴을 구현하는 데 필요한 핵심 요소를 이해할 수 있다.
- 이 디자인 패턴을 사용하는 AI 에이전트의 신뢰성을 확보하기 위한 고려사항을 인식할 수 있다.

## 도구 사용 디자인 패턴이란 무엇인가?

**도구 사용 디자인 패턴**은 LLM이 특정 목표를 달성하기 위해 외부 도구와 상호작용할 수 있는 능력을 부여하는 것에 중점을 둡니다. 도구는 에이전트가 작업을 수행하기 위해 실행할 수 있는 코드입니다. 도구는 계산기와 같은 간단한 함수일 수도 있고, 주식 가격 조회나 일기 예보와 같은 타사 서비스에 대한 API 호출일 수도 있습니다. AI 에이전트의 맥락에서 도구는 **모델 생성 함수 호출(model-generated function calls)**에 응답하여 에이전트가 실행하도록 설계됩니다.

## 어떤 사용 사례에 적용될 수 있는가?

AI 에이전트는 도구를 활용하여 복잡한 작업을 완료하거나 정보를 검색하거나 결정을 내릴 수 있습니다. 도구 사용 디자인 패턴은 데이터베이스, 웹 서비스 또는 코드 인터프리터와 같은 외부 시스템과의 동적 상호작용이 필요한 시나리오에서 자주 사용됩니다. 이 능력은 다음과 같은 다양한 사용 사례에 유용합니다:

- **동적 정보 검색:** 에이전트는 외부 API 또는 데이터베이스에 질의하여 최신 데이터를 가져올 수 있습니다(예: 데이터 분석을 위해 SQLite 데이터베이스에 질의, 주식 가격이나 날씨 정보 가져오기).
- **코드 실행 및 해석:** 에이전트는 수학 문제 해결, 보고서 생성 또는 시뮬레이션 수행을 위해 코드나 스크립트를 실행할 수 있습니다.
- **워크플로 자동화:** 작업 스케줄러, 이메일 서비스 또는 데이터 파이프라인과 같은 도구를 통합하여 반복적이거나 다단계의 워크플로를 자동화합니다.
- **고객 지원:** 에이전트는 CRM 시스템, 티켓팅 플랫폼 또는 지식 베이스와 상호작용하여 사용자 문의를 해결할 수 있습니다.
- **콘텐츠 생성 및 편집:** 에이전트는 문법 검사기, 텍스트 요약기 또는 콘텐츠 안전성 평가자와 같은 도구를 활용하여 콘텐츠 작성 작업을 보조할 수 있습니다.

## 도구 사용 디자인 패턴을 구현하는 데 필요한 요소/구성 블록은 무엇인가?

이러한 구성 블록은 AI 에이전트가 다양한 작업을 수행할 수 있도록 합니다. 도구 사용 디자인 패턴을 구현하는 데 필요한 핵심 요소를 살펴보겠습니다:

- **함수/도구 스키마:** 사용 가능한 도구에 대한 함수 이름, 목적, 필수 매개변수 및 예상 출력 등을 포함한 상세한 정의입니다. 이러한 스키마는 LLM이 어떤 도구가 사용 가능한지, 그리고 유효한 요청을 어떻게 구성해야 하는지를 이해할 수 있게 합니다.

- **함수 실행 로직:** 사용자 의도 및 대화 맥락에 따라 도구가 언제 어떻게 호출될지를 결정하는 규정입니다. 여기에는 플래너 모듈, 라우팅 메커니즘 또는 도구 사용을 동적으로 결정하는 조건 흐름이 포함될 수 있습니다.

- **메시지 처리 시스템:** 사용자 입력, LLM 응답, 도구 호출 및 도구 출력 간의 대화 흐름을 관리하는 구성 요소들입니다.

- **도구 통합 프레임워크:** 에이전트를 단순 함수든 복잡한 외부 서비스든 다양한 도구에 연결하는 인프라입니다.

- **오류 처리 및 검증:** 도구 실행 실패를 처리하고, 매개변수를 검증하며, 예기치 않은 응답을 관리하는 메커니즘입니다.

- **상태 관리:** 대화 맥락, 이전 도구 상호작용 및 지속 데이터 추적을 통해 다중 턴 상호작용 전반에 걸쳐 일관성을 보장합니다.

다음으로 함수/도구 호출(Function/Tool Calling)을 자세히 살펴보겠습니다.
 
### 함수/도구 호출

함수 호출은 LLM이 도구와 상호작용할 수 있게 하는 주요 방법입니다. 'Function'과 'Tool'이 서로 교환되어 사용되는 것을 자주 볼 수 있는데, 그 이유는 '함수'(재사용 가능한 코드 블록)가 에이전트가 작업을 수행하기 위해 사용하는 '도구'이기 때문입니다. 함수의 코드를 호출하려면 LLM이 사용자의 요청을 함수 설명과 비교해야 합니다. 이를 위해 사용 가능한 모든 함수의 설명을 포함하는 스키마가 LLM에 전송됩니다. 그런 다음 LLM은 작업에 가장 적합한 함수를 선택하고 그 이름과 인수를 반환합니다. 선택된 함수가 호출되고, 그 응답이 LLM에 다시 전달되며, LLM은 그 정보를 사용하여 사용자의 요청에 응답합니다.

개발자가 에이전트용 함수 호출을 구현하려면 다음이 필요합니다:

1. 함수 호출을 지원하는 LLM 모델
2. 함수 설명을 포함하는 스키마
3. 설명된 각 함수의 코드

도시의 현재 시간을 얻는 예를 들어 보겠습니다:

1. **함수 호출을 지원하는 LLM 초기화:**

    모든 모델이 함수 호출을 지원하는 것은 아니므로 사용 중인 LLM이 이를 지원하는지 확인하는 것이 중요합니다.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a>는 함수 호출을 지원합니다. 우리는 Azure OpenAI 클라이언트를 초기화하는 것으로 시작할 수 있습니다. 

    ```python
    # Azure OpenAI 클라이언트를 초기화합니다
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **함수 스키마 생성**:

    다음으로 함수 이름, 함수가 수행하는 작업에 대한 설명, 그리고 함수 매개변수의 이름 및 설명을 포함하는 JSON 스키마를 정의합니다.
    그런 다음 이 스키마를 이전에 생성한 클라이언트에 전달하고, 사용자가 샌프란시스코의 시간을 찾기 위한 요청을 함께 전달합니다. 중요한 점은 **도구 호출**은 반환되는 것이지, 질문에 대한 최종 답변이 반환되는 것이 아니라는 것입니다. 앞서 언급했듯이 LLM은 작업을 위해 선택한 함수의 이름과 그 함수에 전달될 인수를 반환합니다.

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
  
1. **작업을 수행하기 위해 필요한 함수 코드:**

    이제 LLM이 실행해야 할 함수를 선택했으므로, 작업을 수행하는 코드를 구현하고 실행해야 합니다.
    우리는 Python으로 현재 시간을 얻는 코드를 구현할 수 있습니다. 또한 최종 결과를 얻기 위해 response_message에서 이름과 인수를 추출하는 코드를 작성해야 합니다.

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
  
      # 두 번째 API 호출: 모델로부터 최종 응답 가져오기
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

함수 호출은 대부분, 아니면 모든 에이전트 도구 사용 디자인의 핵심에 위치하지만, 이를 처음부터 구현하는 것은 때때로 도전적일 수 있습니다.
[레슨 2](../../../02-explore-agentic-frameworks)에서 배운 것처럼 에이전트 프레임워크는 도구 사용을 구현하기 위한 미리 구축된 구성 블록을 제공합니다.
 
## 에이전트 프레임워크를 사용한 도구 사용 예시

다음은 다양한 에이전트 프레임워크를 사용하여 도구 사용 디자인 패턴을 구현하는 방법에 대한 몇 가지 예시입니다:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a>는 AI 에이전트를 구축하기 위한 오픈 소스 AI 프레임워크입니다. 이 프레임워크는 `@tool` 데코레이터로 Python 함수로 도구를 정의할 수 있게 하여 함수 호출 사용을 간소화합니다. 프레임워크는 모델과 코드 간의 왕복 통신을 처리합니다. 또한 `AzureAIProjectAgentProvider`를 통해 파일 검색(File Search) 및 코드 인터프리터(Code Interpreter)와 같은 미리 구축된 도구에 대한 접근을 제공합니다.

다음 다이어그램은 Microsoft Agent Framework에서의 함수 호출 프로세스를 설명합니다:

![함수 호출](../../../translated_images/ko/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework에서는 도구가 데코레이터된 함수로 정의됩니다. 이전에 본 `get_current_time` 함수를 `@tool` 데코레이터를 사용하여 도구로 변환할 수 있습니다. 프레임워크는 자동으로 함수와 그 매개변수를 직렬화하여 LLM에 보낼 스키마를 생성합니다.

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

# 에이전트를 생성하고 도구를 사용하여 실행
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>는 개발자가 기본 컴퓨트 및 스토리지 리소스를 관리할 필요 없이 안전하게 고품질 확장 가능하고 확장 가능한 AI 에이전트를 구축, 배포 및 확장할 수 있도록 설계된 최신 에이전트 프레임워크입니다. 이는 엔터프라이즈급 보안을 갖춘 완전 관리형 서비스이기 때문에 특히 기업용 애플리케이션에 유용합니다.

LLM API를 직접 사용하여 개발할 때와 비교했을 때 Azure AI Agent Service는 다음과 같은 장점을 제공합니다:

- 자동 도구 호출 – 도구 호출을 파싱하고, 도구를 호출하고, 응답을 처리할 필요가 없습니다; 이 모든 것이 이제 서버 측에서 처리됩니다
- 안전하게 관리되는 데이터 – 자체 대화 상태를 관리하는 대신, 필요한 모든 정보를 저장하는 threads에 의존할 수 있습니다
- 즉시 사용 가능한 도구 – Bing, Azure AI Search 및 Azure Functions와 같은 데이터 소스와 상호작용할 수 있는 도구들

Azure AI Agent Service에서 사용 가능한 도구는 두 가지 범주로 나눌 수 있습니다:

1. 지식 도구:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. 액션 도구:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service는 이러한 도구들을 `toolset`으로 함께 사용할 수 있게 해 줍니다. 또한 특정 대화의 메시지 이력을 추적하는 `threads`를 활용합니다.

당신이 Contoso라는 회사의 영업 담당자라고 상상해 보세요. 영업 데이터에 대한 질문에 답할 수 있는 대화형 에이전트를 개발하고 싶습니다.

다음 이미지는 Azure AI Agent Service를 사용하여 영업 데이터를 분석하는 방법을 보여줍니다:

![에이전트 서비스 실행 예시](../../../translated_images/ko/agent-service-in-action.34fb465c9a84659e.webp)

서비스에서 이러한 도구를 사용하려면 클라이언트를 생성하고 도구 또는 도구집합(toolset)을 정의할 수 있습니다. 이를 실질적으로 구현하기 위해 다음 Python 코드를 사용할 수 있습니다. LLM은 toolset을 보고 사용자 생성 함수인 `fetch_sales_data_using_sqlite_query`를 사용할지, 또는 미리 구축된 코드 인터프리터(Code Interpreter)를 사용할지 사용자 요청에 따라 결정할 수 있습니다.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query 함수는 fetch_sales_data_functions.py 파일에서 찾을 수 있습니다.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# 도구 세트 초기화
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query 함수를 사용하여 함수 호출 에이전트를 초기화하고 이를 도구 세트에 추가합니다.
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreter 도구를 초기화하고 도구 세트에 추가합니다.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 도구 사용 디자인 패턴을 사용하여 신뢰할 수 있는 AI 에이전트를 구축할 때의 특별한 고려사항은 무엇인가?

LLM이 동적으로 생성한 SQL에 대한 일반적인 우려는 보안이며, 특히 SQL 인젝션이나 데이터베이스를 삭제하거나 변조하는 등의 악의적 행동의 위험입니다. 이러한 우려는 타당하지만, 데이터베이스 접근 권한을 적절히 구성하면 효과적으로 완화될 수 있습니다. 대부분의 데이터베이스에서는 데이터베이스를 읽기 전용으로 구성하는 것이 포함됩니다. PostgreSQL이나 Azure SQL과 같은 데이터베이스 서비스의 경우, 앱에는 읽기 전용(SELECT) 역할을 할당해야 합니다.

앱을 보안 환경에서 실행하면 보호를 더욱 강화할 수 있습니다. 엔터프라이즈 시나리오에서는 일반적으로 운영 시스템에서 데이터를 추출 및 변환하여 사용자 친화적인 스키마를 가진 읽기 전용 데이터베이스나 데이터 웨어하우스에 저장합니다. 이 접근 방식은 데이터의 보안성을 보장하고, 성능과 접근성을 최적화하며, 앱이 제한된 읽기 전용 접근 권한을 가지도록 합니다.

## 샘플 코드

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## 도구 사용 디자인 패턴에 대해 더 궁금한 점이 있으신가요?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)에 참여하여 다른 학습자들을 만나고, 오피스 아워에 참석하고, AI 에이전트 관련 질문에 대한 답변을 받아보세요.

## 추가 자료

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## 이전 수업

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## 다음 수업
[에이전트형 RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
면책 조항:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의해 주십시오. 원문(원어로 된 문서)을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 모든 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
