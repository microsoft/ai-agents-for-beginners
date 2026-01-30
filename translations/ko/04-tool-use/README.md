[![좋은 AI 에이전트 설계 방법](../../../translated_images/ko/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(위 이미지를 클릭하여 이번 강의의 영상을 시청하세요)_

# 도구 사용 디자인 패턴

도구는 AI 에이전트가 더 넓은 범위의 기능을 갖도록 해주기 때문에 흥미롭습니다. 에이전트가 수행할 수 있는 동작이 제한된 집합에 머무는 대신, 도구를 추가함으로써 에이전트는 다양한 동작을 수행할 수 있습니다. 이번 장에서는 AI 에이전트가 목표를 달성하기 위해 특정 도구를 어떻게 사용할 수 있는지 설명하는 도구 사용 디자인 패턴에 대해 살펴봅니다.

## 소개

이번 강의에서는 다음 질문에 답하고자 합니다:

- 도구 사용 디자인 패턴이란 무엇인가?
- 어떤 사용 사례에 적용할 수 있는가?
- 디자인 패턴을 구현하는 데 필요한 요소/구성 블록은 무엇인가?
- 신뢰할 수 있는 AI 에이전트를 구축하기 위해 도구 사용 디자인 패턴을 사용할 때의 특별한 고려사항은 무엇인가?

## 학습 목표

이 강의를 완료한 후 다음을 할 수 있습니다:

- 도구 사용 디자인 패턴과 그 목적을 정의할 수 있습니다.
- 도구 사용 디자인 패턴이 적용 가능한 사용 사례를 식별할 수 있습니다.
- 디자인 패턴을 구현하는 데 필요한 주요 요소를 이해할 수 있습니다.
- 이 디자인 패턴을 사용하는 AI 에이전트의 신뢰성을 보장하기 위한 고려사항을 인식할 수 있습니다.

## 도구 사용 디자인 패턴이란 무엇인가?

**도구 사용 디자인 패턴**은 LLM이 특정 목표를 달성하기 위해 외부 도구와 상호작용할 수 있는 능력을 부여하는 데 중점을 둡니다. 도구는 에이전트가 동작을 수행하기 위해 실행할 수 있는 코드입니다. 도구는 계산기와 같은 단순한 함수일 수도 있고, 주가 조회나 날씨 예보와 같은 타사 서비스에 대한 API 호출일 수도 있습니다. AI 에이전트 맥락에서 도구는 **모델이 생성한 함수 호출**에 응답하여 에이전트가 실행하도록 설계됩니다.

## 어떤 사용 사례에 적용할 수 있는가?

AI 에이전트는 도구를 활용하여 복잡한 작업을 완료하거나 정보를 검색하거나 의사 결정을 할 수 있습니다. 도구 사용 디자인 패턴은 데이터베이스, 웹 서비스, 코드 인터프리터와 같은 외부 시스템과의 동적 상호 작용이 필요한 시나리오에서 자주 사용됩니다. 이 능력은 다음을 포함한 여러 다양한 사용 사례에 유용합니다:

- **동적 정보 검색:** 에이전트가 외부 API 또는 데이터베이스에 쿼리하여 최신 데이터를 가져올 수 있습니다(예: SQLite 데이터베이스에서 데이터 분석용 쿼리, 주가 또는 날씨 정보 조회).
- **코드 실행 및 해석:** 에이전트가 코드 또는 스크립트를 실행하여 수학 문제를 해결하거나 보고서를 생성하거나 시뮬레이션을 수행할 수 있습니다.
- **워크플로 자동화:** 작업 스케줄러, 이메일 서비스 또는 데이터 파이프라인과 같은 도구를 통합해 반복적이거나 다단계 워크플로 자동화.
- **고객 지원:** 에이전트가 CRM 시스템, 티켓팅 플랫폼, 지식 베이스와 상호 작용하여 사용자 문의 해결.
- **콘텐츠 생성 및 편집:** 문법 검사기, 텍스트 요약기, 콘텐츠 안전 평가기와 같은 도구를 활용하여 콘텐츠 작성 지원.

## 도구 사용 디자인 패턴을 구현하는 데 필요한 요소/구성 블록은 무엇인가?

이 구성 블록들은 AI 에이전트가 다양한 작업을 수행할 수 있게 합니다. 도구 사용 디자인 패턴을 구현하는 데 필요한 주요 요소를 살펴봅시다:

- **함수/도구 스키마:** 사용 가능한 도구의 상세 정의로 함수 이름, 목적, 요구 매개변수 및 예상 출력 포함. 이 스키마는 LLM이 어떤 도구가 사용 가능하며 유효한 요청을 어떻게 구성하는지 이해할 수 있도록 합니다.

- **함수 실행 로직:** 사용자 의도와 대화 맥락에 따라 언제 어떻게 도구를 호출할지 결정하는 규칙. 플래너 모듈, 라우팅 메커니즘, 조건 흐름 등이 포함될 수 있습니다.

- **메시지 처리 시스템:** 사용자 입력, LLM 응답, 도구 호출 및 도구 출력 간의 대화 흐름을 관리하는 구성 요소.

- **도구 통합 프레임워크:** 단순 함수부터 복잡한 외부 서비스까지 에이전트를 다양한 도구에 연결하는 인프라.

- **오류 처리 및 검증:** 도구 실행 실패 처리, 매개변수 검증, 예기치 않은 응답 관리 메커니즘.

- **상태 관리:** 대화 맥락, 이전 도구 상호작용, 영속 데이터 추적으로 다중 턴 상호작용 간 일관성 보장.

다음으로, 함수/도구 호출에 대해 자세히 살펴봅시다.
 
### 함수/도구 호출

함수 호출은 LLM이 도구와 상호작용하도록 하는 주된 방법입니다. '함수'와 '도구'라는 용어가 종종 혼용되는데, 이는 '함수'(재사용 가능한 코드 블록)가 에이전트가 작업 수행에 사용하는 '도구'이기 때문입니다. 함수의 코드를 실행하려면, LLM이 사용자 요청을 함수 설명과 비교해야 합니다. 이를 위해 사용 가능한 모든 함수의 설명을 포함하는 스키마를 LLM에 전달합니다. LLM은 그 후 작업에 가장 적합한 함수를 선택하고 함수 이름과 인자를 반환합니다. 선택된 함수가 호출되고, 응답이 LLM에 전달되어 사용자의 요청에 응답하는 데 활용됩니다.

개발자가 함수 호출 기능을 구현하려면 다음이 필요합니다:

1. 함수 호출을 지원하는 LLM 모델
2. 함수 설명이 담긴 스키마
3. 각 함수에 해당하는 코드

도시의 현재 시간을 얻는 예시로 살펴봅시다:

1. **함수 호출을 지원하는 LLM 초기화:**

    모든 모델이 함수 호출을 지원하는 것은 아니므로 사용 중인 LLM이 지원하는지 확인하는 것이 중요합니다. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a>는 함수 호출을 지원합니다. 먼저 Azure OpenAI 클라이언트를 초기화할 수 있습니다.

    ```python
    # Azure OpenAI 클라이언트를 초기화합니다
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **함수 스키마 생성:**

    다음으로 함수 이름, 기능 설명 및 함수 매개변수 이름과 설명이 포함된 JSON 스키마를 정의합니다.
    이 스키마를 앞서 생성한 클라이언트와 함께 사용자 요청(샌프란시스코 시간 조회)과 함께 전달합니다. 중요하게도, **도구 호출**은 반환되지만, 질문에 대한 최종 답변이 아닙니다. 앞서 설명한 바와 같이 LLM은 작업에 적합한 함수 이름과 전달할 인자를 반환합니다.

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

    LLM이 실행할 함수 선택 후, 해당 작업을 수행하는 코드를 구현하고 실행해야 합니다.
    Python으로 현재 시간을 가져오는 코드를 구현할 수 있습니다. 또한 response_message에서 함수 이름과 인자를 추출하여 최종 결과를 얻기 위한 코드를 작성해야 합니다.

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
  
      # 두 번째 API 호출: 모델로부터 최종 응답 받기
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

함수 호출은 대부분, 혹은 모든 에이전트 도구 사용 디자인의 핵심이지만, 처음부터 직접 구현하는 것은 때로 어려울 수 있습니다.
[Lesson 2](../../../02-explore-agentic-frameworks)에서 알게 된 것처럼, 에이전트 프레임워크는 도구 사용을 구현하기 위한 미리 만들어진 구성 블록을 제공합니다.
 
## 에이전트 프레임워크를 활용한 도구 사용 예시

다양한 에이전트 프레임워크를 사용하여 도구 사용 디자인 패턴을 구현하는 일부 예시는 다음과 같습니다:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a>은 .NET, Python, Java 개발자를 위한 오픈 소스 AI 프레임워크로, 대규모 언어 모델(LLM) 사용을 간소화합니다. 함수 및 매개변수의 서술을 모델에 자동으로 전달하는 <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">직렬화</a> 과정을 통해 함수 호출 과정을 단순화합니다. 또한 모델과 코드 간의 쌍방향 통신도 처리합니다. Semantic Kernel과 같은 에이전트 프레임워크를 사용하면 <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">파일 검색</a> 및 <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">코드 인터프리터</a>와 같은 미리 만들어진 도구도 활용할 수 있습니다.

다음 다이어그램은 Semantic Kernel의 함수 호출 과정을 나타냅니다:

![function calling](../../../translated_images/ko/functioncalling-diagram.a84006fc287f6014.webp)

Semantic Kernel에서 함수/도구는 <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">플러그인</a>이라고 불립니다. 앞서 본 `get_current_time` 함수를 플러그인으로 변환하려면, 함수를 포함하는 클래스로 만들 수 있습니다. 또한 함수 설명을 받는 `kernel_function` 데코레이터를 가져올 수 있습니다. 이후 GetCurrentTimePlugin으로 커널을 생성하면, 커널이 자동으로 함수와 매개변수를 직렬화하여 LLM에 전달할 스키마를 생성합니다.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# 커널을 생성합니다
kernel = Kernel()

# 플러그인을 생성합니다
get_current_time_plugin = GetCurrentTimePlugin(location)

# 플러그인을 커널에 추가합니다
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>는 개발자가 기본 컴퓨트 및 저장소 리소스를 관리하지 않고도 안전하게 고품질의 확장 가능한 AI 에이전트를 구축, 배포, 확장할 수 있도록 설계된 최신 에이전트 프레임워크입니다. 엔터프라이즈급 보안을 갖춘 완전 관리형 서비스로 특히 기업 애플리케이션에 유용합니다.

LLM API를 직접 사용하는 것과 비교할 때 Azure AI Agent Service가 제공하는 장점은 다음과 같습니다:

- 자동 도구 호출 – 도구 호출 구문 분석, 도구 실행, 응답 처리 불필요; 모든 것이 서버 측에서 처리.
- 안전하게 관리되는 데이터 – 대화 상태를 직접 관리하는 대신 스레드를 이용해 필요한 모든 정보를 저장.
- 즉시 사용 가능한 도구 – Bing, Azure AI Search, Azure Functions 등 데이터 소스와 상호작용할 수 있는 도구 제공.

Azure AI Agent Service에서 제공되는 도구는 두 가지 카테고리로 나뉩니다:

1. 지식 도구:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing 검색과 연동</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">파일 검색</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. 작업 도구:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">함수 호출</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">코드 인터프리터</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 정의 도구</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service는 이러한 도구들을 `toolset`으로 함께 사용할 수 있게 해줍니다. 또한 `스레드`를 활용하여 특정 대화의 메시지 이력을 추적합니다.

가령 Contoso라는 회사의 영업 담당자라고 가정합시다. 여러분은 영업 데이터에 대한 질문에 답변할 수 있는 대화형 에이전트를 개발하고자 합니다.

다음 이미지는 Azure AI Agent Service를 사용해 영업 데이터를 분석하는 방법을 보여줍니다:

![Agentic Service In Action](../../../translated_images/ko/agent-service-in-action.34fb465c9a84659e.webp)

이들 도구를 서비스에서 사용하려면 클라이언트를 생성하고 도구 또는 도구 집합을 정의할 수 있습니다. 이를 실제로 구현하기 위해 다음 Python 코드를 사용할 수 있습니다. LLM은 도구 집합을 보고 사용자 생성 함수 `fetch_sales_data_using_sqlite_query`를 사용할지, 미리 만들어진 코드 인터프리터를 사용할지 사용자의 요청에 따라 결정할 수 있습니다.

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

# fetch_sales_data_using_sqlite_query 함수로 함수 호출 에이전트를 초기화하고 도구 세트에 추가합니다.
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# 코드 인터프리터 도구를 초기화하고 도구 세트에 추가합니다.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 신뢰할 수 있는 AI 에이전트를 구축하기 위해 도구 사용 디자인 패턴을 사용할 때 특별히 고려할 점은 무엇인가?

LLM이 동적으로 생성하는 SQL에 대한 흔한 우려사항은 보안입니다. 특히 SQL 인젝션이나 데이터베이스 삭제 또는 변조와 같은 악의적 행위에 대한 위험입니다. 이러한 우려는 타당하지만, 데이터베이스 접근 권한을 적절히 구성하면 효과적으로 완화할 수 있습니다. 대부분의 데이터베이스는 읽기 전용으로 구성하는 것을 포함합니다. PostgreSQL이나 Azure SQL과 같은 데이터베이스 서비스의 경우, 앱에 읽기 전용(SELECT) 역할을 할당해야 합니다.
앱을 보안 환경에서 실행하면 보호가 더욱 강화됩니다. 엔터프라이즈 시나리오에서는 운영 시스템에서 데이터를 추출하여 읽기 전용 데이터베이스나 데이터 웨어하우스로 변환하고, 사용자 친화적인 스키마를 적용하는 경우가 많습니다. 이 접근 방식은 데이터 보안이 유지되고 성능과 접근성이 최적화되며, 앱이 제한된 읽기 전용 액세스 권한만 갖도록 보장합니다.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Got More Questions about the Tool Use Design Patterns?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하였으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인적 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 모든 오해나 오해석에 대해 당사는 책임지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->