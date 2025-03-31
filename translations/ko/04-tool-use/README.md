<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b8ea2abd1a674f736d5fc08982e6ec06",
  "translation_date": "2025-03-28T13:45:28+00:00",
  "source_file": "04-tool-use\\README.md",
  "language_code": "ko"
}
-->
[![How to Design Good AI Agents](../../../translated_images/lesson-4-thumbnail.2c292cd87b951b3e914e9548b46cb4d14a0852f9c8d75e9566d46da839c983d9.ko.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(위 이미지를 클릭하면 해당 강의의 영상을 볼 수 있습니다)_

# 도구 사용 디자인 패턴

도구는 AI 에이전트가 더 넓은 범위의 기능을 가질 수 있도록 해준다는 점에서 흥미롭습니다. 에이전트가 수행할 수 있는 행동이 제한된 상태에서 도구를 추가하면 이제 다양한 행동을 수행할 수 있게 됩니다. 이 장에서는 AI 에이전트가 특정 도구를 사용하여 목표를 달성하는 방법을 설명하는 도구 사용 디자인 패턴에 대해 살펴보겠습니다.

## 소개

이번 강의에서는 다음 질문들에 답하고자 합니다:

- 도구 사용 디자인 패턴이란 무엇인가?
- 이 패턴이 적용될 수 있는 사용 사례는 무엇인가?
- 이 디자인 패턴을 구현하는 데 필요한 요소/구성 요소는 무엇인가?
- 신뢰할 수 있는 AI 에이전트를 구축하기 위해 도구 사용 디자인 패턴을 사용할 때의 특별한 고려 사항은 무엇인가?

## 학습 목표

이 강의를 완료한 후, 여러분은 다음을 수행할 수 있습니다:

- 도구 사용 디자인 패턴과 그 목적을 정의할 수 있습니다.
- 도구 사용 디자인 패턴이 적용 가능한 사용 사례를 식별할 수 있습니다.
- 이 디자인 패턴을 구현하는 데 필요한 주요 요소를 이해할 수 있습니다.
- 이 디자인 패턴을 사용하는 AI 에이전트의 신뢰성을 보장하기 위한 고려 사항을 인식할 수 있습니다.

## 도구 사용 디자인 패턴이란 무엇인가?

**도구 사용 디자인 패턴**은 LLM이 특정 목표를 달성하기 위해 외부 도구와 상호작용할 수 있는 능력을 제공하는 데 중점을 둡니다. 도구는 에이전트가 행동을 수행하기 위해 실행할 수 있는 코드입니다. 도구는 계산기 같은 간단한 함수일 수도 있고, 주식 가격 조회나 날씨 예보 같은 제3자 서비스 API 호출일 수도 있습니다. AI 에이전트의 맥락에서 도구는 **모델 생성 함수 호출**에 따라 에이전트가 실행하도록 설계됩니다.

## 이 패턴이 적용될 수 있는 사용 사례는 무엇인가?

AI 에이전트는 도구를 활용하여 복잡한 작업을 완료하거나 정보를 검색하거나 결정을 내릴 수 있습니다. 도구 사용 디자인 패턴은 데이터베이스, 웹 서비스 또는 코드 인터프리터와 같은 외부 시스템과 동적으로 상호작용해야 하는 시나리오에서 자주 사용됩니다. 이 능력은 다양한 사용 사례에서 유용합니다:

- **동적 정보 검색:** 에이전트는 외부 API나 데이터베이스를 쿼리하여 최신 데이터를 가져올 수 있습니다(예: SQLite 데이터베이스를 쿼리하여 데이터 분석 수행, 주식 가격 또는 날씨 정보 가져오기).
- **코드 실행 및 해석:** 에이전트는 수학 문제를 해결하거나 보고서를 생성하거나 시뮬레이션을 수행하기 위해 코드나 스크립트를 실행할 수 있습니다.
- **워크플로 자동화:** 작업 스케줄러, 이메일 서비스, 데이터 파이프라인과 같은 도구를 통합하여 반복적이거나 다단계 워크플로를 자동화합니다.
- **고객 지원:** 에이전트는 CRM 시스템, 티켓 플랫폼 또는 지식 기반과 상호작용하여 사용자 문의를 해결할 수 있습니다.
- **콘텐츠 생성 및 편집:** 에이전트는 문법 검사기, 텍스트 요약 도구 또는 콘텐츠 안전성 평가기 같은 도구를 활용하여 콘텐츠 생성 작업을 지원할 수 있습니다.

## 도구 사용 디자인 패턴을 구현하는 데 필요한 요소/구성 요소는 무엇인가?

이 구성 요소들은 AI 에이전트가 다양한 작업을 수행할 수 있도록 합니다. 도구 사용 디자인 패턴을 구현하는 데 필요한 주요 요소를 살펴보겠습니다:

- **함수/도구 호출:** LLM이 도구와 상호작용할 수 있도록 하는 주요 방법입니다. 함수나 도구는 에이전트가 작업을 수행하기 위해 사용하는 재사용 가능한 코드 블록입니다. 이는 계산기 같은 간단한 함수에서 주식 가격 조회나 날씨 예보 같은 제3자 서비스 API 호출까지 다양합니다.
- **동적 정보 검색:** 에이전트는 외부 API나 데이터베이스를 쿼리하여 최신 데이터를 가져올 수 있습니다. 이는 데이터 분석, 주식 가격 검색, 날씨 정보 검색과 같은 작업에 유용합니다.
- **코드 실행 및 해석:** 에이전트는 수학 문제를 해결하거나 보고서를 생성하거나 시뮬레이션을 수행하기 위해 코드나 스크립트를 실행할 수 있습니다.
- **워크플로 자동화:** 작업 스케줄러, 이메일 서비스, 데이터 파이프라인 같은 도구를 통합하여 반복적이거나 다단계 워크플로를 자동화합니다.
- **고객 지원:** 에이전트는 CRM 시스템, 티켓 플랫폼 또는 지식 기반과 상호작용하여 사용자 문의를 해결할 수 있습니다.
- **콘텐츠 생성 및 편집:** 에이전트는 문법 검사기, 텍스트 요약 도구 또는 콘텐츠 안전성 평가기 같은 도구를 활용하여 콘텐츠 생성 작업을 지원할 수 있습니다.

다음으로 함수/도구 호출에 대해 자세히 알아보겠습니다.

### 함수/도구 호출

함수 호출은 대형 언어 모델(LLM)이 도구와 상호작용할 수 있도록 하는 주요 방법입니다. '함수'와 '도구'는 종종 교환하여 사용되는데, '함수'(재사용 가능한 코드 블록)가 에이전트가 작업을 수행하는 데 사용하는 '도구'이기 때문입니다. 함수의 코드가 호출되려면 LLM은 사용자의 요청을 함수 설명과 비교해야 합니다. 이를 위해 모든 사용 가능한 함수 설명을 포함하는 스키마가 LLM에 전송됩니다. LLM은 작업에 가장 적합한 함수를 선택하고 함수 이름과 인수를 반환합니다. 선택된 함수가 호출되고, 해당 응답이 LLM으로 다시 전송되며, 이를 통해 사용자의 요청에 응답합니다.

에이전트의 함수 호출을 구현하려면 다음이 필요합니다:

1. 함수 호출을 지원하는 LLM 모델
2. 함수 설명을 포함하는 스키마
3. 설명된 각 함수의 코드

도시의 현재 시간을 가져오는 예제를 사용해 봅시다:

1. **함수 호출을 지원하는 LLM 초기화:**

    모든 모델이 함수 호출을 지원하는 것은 아니므로 사용하는 LLM이 이를 지원하는지 확인하는 것이 중요합니다. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a>는 함수 호출을 지원합니다. Azure OpenAI 클라이언트를 초기화하는 것으로 시작할 수 있습니다.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **함수 스키마 생성:**

    다음으로 함수 이름, 함수가 수행하는 작업에 대한 설명, 함수 매개변수의 이름 및 설명을 포함하는 JSON 스키마를 정의합니다. 그런 다음 이 스키마를 앞서 생성한 클라이언트와 함께 사용자의 요청(예: 샌프란시스코의 시간을 찾기)을 전달합니다. 중요한 점은 **도구 호출**이 반환된다는 것이지, 질문에 대한 최종 답변이 반환되는 것이 아니라는 점입니다. 앞서 언급했듯이 LLM은 작업에 선택된 함수 이름과 전달될 인수를 반환합니다.

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **작업을 수행하는 데 필요한 함수 코드:**

    이제 LLM이 실행해야 할 함수를 선택했으므로 작업을 수행하는 코드를 구현하고 실행해야 합니다. 우리는 Python에서 현재 시간을 가져오는 코드를 구현할 수 있습니다. 또한 응답 메시지에서 이름과 인수를 추출하여 최종 결과를 얻는 코드를 작성해야 합니다.

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

함수 호출은 대부분의 에이전트 도구 사용 디자인의 핵심이지만, 이를 처음부터 구현하는 것은 때로는 어려울 수 있습니다. [2강](../../../02-explore-agentic-frameworks)에서 배운 것처럼 에이전트 프레임워크는 도구 사용을 구현하기 위한 사전 구축된 구성 요소를 제공합니다.

## 에이전트 프레임워크를 활용한 도구 사용 예제

다음은 다양한 에이전트 프레임워크를 사용하여 도구 사용 디자인 패턴을 구현하는 방법의 예입니다:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a>은 대형 언어 모델(LLM)을 사용하는 .NET, Python, Java 개발자를 위한 오픈소스 AI 프레임워크입니다. 함수 호출을 사용하는 과정을 자동화하여 함수와 매개변수를 모델에 설명하는 <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">직렬화</a> 과정을 간소화합니다. 또한 모델과 코드 간의 상호작용을 처리합니다. Semantic Kernel 같은 에이전트 프레임워크를 사용하면 <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">파일 검색</a> 및 <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">코드 인터프리터</a> 같은 사전 구축된 도구에 액세스할 수 있습니다.

다음 다이어그램은 Semantic Kernel을 사용한 함수 호출 과정을 보여줍니다:

![function calling](../../../translated_images/functioncalling-diagram.b5493ea5154ad8e3e4940d2e36a49101eec1398948e5d1039942203b4f5a4209.ko.png)

Semantic Kernel에서는 함수/도구가 <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">플러그인</a>이라고 불립니다. 우리는 `get_current_time` function we saw earlier into a plugin by turning it into a class with the function in it. We can also import the `kernel_function` 데코레이터를 사용하여 함수의 설명을 입력할 수 있습니다. 그런 다음 GetCurrentTimePlugin을 포함한 커널을 생성하면 커널이 함수와 매개변수를 자동으로 직렬화하여 LLM에 보낼 스키마를 생성합니다.

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

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>는 개발자가 고품질의 확장 가능한 AI 에이전트를 안전하게 구축, 배포 및 확장할 수 있도록 설계된 최신 에이전트 프레임워크입니다. 기본 컴퓨팅 및 저장 리소스를 관리할 필요가 없어 특히 엔터프라이즈 애플리케이션에 유용합니다. 이 서비스는 엔터프라이즈급 보안이 적용된 완전 관리형 서비스입니다.

LLM API를 직접 사용하는 것과 비교했을 때, Azure AI Agent Service는 다음과 같은 이점을 제공합니다:

- 자동 도구 호출 – 도구 호출을 분석하고 도구를 호출하며 응답을 처리할 필요가 없으며, 이 모든 것이 서버 측에서 처리됩니다.
- 안전하게 관리된 데이터 – 대화 상태를 직접 관리하는 대신 스레드를 사용하여 필요한 모든 정보를 저장할 수 있습니다.
- 기본 제공 도구 – Bing, Azure AI Search, Azure Functions와 같은 데이터 소스와 상호작용하기 위한 도구를 사용할 수 있습니다.

Azure AI Agent Service에서 제공되는 도구는 두 가지 범주로 나뉩니다:

1. 지식 도구:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing 검색 기반</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">파일 검색</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. 액션 도구:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">함수 호출</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">코드 인터프리터</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAI 정의 도구</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service를 사용하면 사용자의 요청에 따라 `toolset`. It also utilizes `threads` which keep track of the history of messages from a particular conversation.

Imagine you are a sales agent at a company called Contoso. You want to develop a conversational agent that can answer questions about your sales data.

The following image illustrates how you could use Azure AI Agent Service to analyze your sales data:

![Agentic Service In Action](../../../translated_images/agent-service-in-action.8c2d8aa8e9d91feeb29549b3fde529f8332b243875154d03907616a69198afbc.ko.jpg)

To use any of these tools with the service we can create a client and define a tool or toolset. To implement this practically we can use the following Python code. The LLM will be able to look at the toolset and decide whether to use the user created function, `fetch_sales_data_using_sqlite_query` 또는 사전 구축된 코드 인터프리터를 함께 사용할 수 있습니다.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fecth_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 신뢰할 수 있는 AI 에이전트를 구축하기 위해 도구 사용 디자인 패턴을 사용할 때의 특별한 고려 사항은 무엇인가?

LLM이 동적으로 생성한 SQL과 관련된 일반적인 우려 사항은 보안, 특히 SQL 삽입 또는 데이터베이스 삭제 및 조작과 같은 악의적인 행동의 위험입니다. 이러한 우려는 타당하지만 데이터베이스 액세스 권한을 적절히 구성함으로써 효과적으로 완화할 수 있습니다. 대부분의 데이터베이스에서는 데이터베이스를 읽기 전용으로 구성하는 것이 포함됩니다. PostgreSQL이나 Azure SQL 같은 데이터베이스 서비스의 경우 앱에 읽기 전용(SELECT) 역할을 할당해야 합니다.

앱을 안전한 환경에서 실행하면 보호 수준이 더욱 강화됩니다. 엔터프라이즈 시나리오에서는 데이터를 운영 시스템에서 추출하여 읽기 전용 데이터베이스 또는 사용하기 쉬운 스키마를 가진 데이터 웨어하우스로 변환하는 것이 일반적입니다. 이러한 접근 방식은 데이터를 안전하게 유지하고 성능 및 접근성을 최적화하며 앱이 제한된 읽기 전용 액세스를 갖도록 보장합니다.

## 추가 자료

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service 워크숍</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer 다중 에이전트 워크숍</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel 함수 호출 튜토리얼</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel 코드 인터프리터</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen 도구</a>

## 이전 강의

[에이전트 디자인 패턴 이해하기](../03-agentic-design-patterns/README.md)

## 다음 강의

[Agentic RAG](../05-agentic-rag/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원문은 해당 언어로 작성된 문서를 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역을 사용하는 과정에서 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.