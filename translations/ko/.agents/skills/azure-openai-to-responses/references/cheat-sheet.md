# Responses API 치트 시트 (Python + Azure OpenAI)

> 아래 모든 예제는 `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` 와 `client`가 이미 초기화되어 있다고 가정합니다 (클라이언트 설정 참조).

## 기본 요청
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## 클라이언트 설정 — EntraID (권장)
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = OpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## 클라이언트 설정 — API 키
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## 비동기 클라이언트 설정 — EntraID
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AsyncOpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## 비동기 클라이언트 설정 — 명시적 테넌트 포함 EntraID (다중 테넌트)

Azure OpenAI 리소스가 기본 테넌트와 <strong>다른 테넌트</strong>에 있는 경우, 자격 증명에 `tenant_id`를 명시적으로 전달하세요. 이는 개발자의 홈 테넌트와 리소스 테넌트가 다른 개발/테스트 시나리오에서 일반적입니다.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# 프로덕션용 ManagedIdentityCredential (Azure Container Apps, App Service 등)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # 사용자 할당 관리 ID
)
# 로컬 개발용 AzureDeveloperCliCredential — 명시적 tenant_id가 중요함
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# 체인: 먼저 관리 ID 시도, 실패 시 azd CLI로 대체
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## 비동기 클라이언트 마이그레이션 — 이전/이후

이전 (더 이상 권장하지 않음):
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

이후:
```python
from openai import AsyncOpenAI

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)

resp = await client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## 전체 동기 마이그레이션 — 이전/이후

이전 (레거시 — Azure OpenAI 채팅 완성):
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

이후 (Responses API — Azure OpenAI v1 엔드포인트):
```python
from openai import OpenAI
import os

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## 스트리밍 (동기)
```python
stream = client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()  # 끝에 새 줄
```

## 스트리밍 (비동기)
```python
stream = await client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
async for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()
```

## 웹 앱 스트리밍 — 백엔드에서 프런트엔드로 데이터 형태

SSE/JSONL을 프런트엔드로 스트리밍하는 웹 앱을 마이그레이션할 때, <strong>백엔드 직렬화 형식</strong>이 변경됩니다. 프런트엔드가 기존 접근 방식을 유지하도록 새 백엔드 출력을 설계하여 프런트엔드 변경이 필요 없게 만드세요.

<strong>이전</strong> — 채팅 완성 백엔드는 각 청크의 `choices[0]` 딕셔너리를 일반적으로 직렬화했습니다:
```python
# 이전: 청크별 직렬화된 전체 선택 사전
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
프런트엔드 읽기: `response.delta.content` (선택 객체의 깊은 경로).

<strong>이후</strong> — Responses API 백엔드는 동일한 프런트엔드 접근 경로를 보존하는 최소한의 형태를 출력합니다:
```python
# 새로움: 프런트엔드에서 필요한 것만 전송
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
프런트엔드는 여전히 `response.delta.content`를 읽습니다 — **프런트엔드 변경 불필요**.

> **핵심 인사이트**: Responses API 스트리밍 형태(`event.type` + `event.delta`)는 채팅 완성(`chunk.choices[0].delta.content`)와 근본적으로 다릅니다. 그러나 백엔드에서 프런트엔드로 전달하는 계약은 여러분이 정의하는 것입니다. 백엔드 출력 형식을 프런트엔드가 이미 기대하는 형태에 맞추세요.

## 스트리밍 이벤트 순서

`stream: true`일 때, API는 다음 순서로 이벤트를 내보냅니다:
1. `response.created` – 응답 객체 초기화됨
2. `response.in_progress` – 생성 시작됨
3. `response.output_item.added` – 출력 항목 생성됨
4. `response.content_part.added` – 콘텐츠 부분 시작됨
5. `response.output_text.delta` – 텍스트 청크 (여러 개, 각각 `delta: string` 포함)
6. `response.output_text.done` – 텍스트 생성 완료됨
7. `response.content_part.done` – 콘텐츠 부분 완료됨
8. `response.output_item.done` – 출력 항목 완료됨
9. `response.completed` – 전체 응답 완료됨

기본 텍스트 스트리밍의 경우, `response.output_text.delta`(텍스트 청크용)와 `response.completed`(완료용)만 처리하세요.

## 웹 앱에서 스트리밍 오류 처리

웹 앱에서 스트리밍할 때, 비동기 반복을 `try/except`로 감싸고 오류를 JSON으로 내보내 프런트엔드가 이를 우아하게 표시할 수 있게 하세요 (예: 요율 제한, 일시적 실패):

```python
@stream_with_context
async def response_stream():
    chat_coroutine = client.responses.create(
        model=deployment,
        input=all_messages,
        max_output_tokens=1000,
        stream=True,
        store=False,
    )
    try:
        async for event in await chat_coroutine:
            if event.type == "response.output_text.delta":
                yield json.dumps({"delta": {"content": event.delta}}) + "\n"
            elif event.type == "response.completed":
                yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
    except Exception as e:
        current_app.logger.error(e)
        yield json.dumps({"error": str(e)}) + "\n"
```


> **중요한 이유**: Azure OpenAI는 속도 제한 시 `429 Too Many Requests`를 반환합니다. `try/except`가 없으면 스트리밍 응답이 조용히 중단됩니다. 있으면 프런트엔드가 `{"error": "Too Many Requests"}`를 수신하여 재시도 메시지를 표시할 수 있습니다.

## 스트리밍 이벤트 유형 (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## 대화 형식
```python
# Responses API는 입력 배열을 통한 대화 형식을 지원합니다
response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are an Azure cloud architect."},
        {"role": "user", "content": "Design a scalable web application architecture."},
    ],
    max_output_tokens=1000,
)
print(response.output_text)
```

## 콘텐츠 필터 오류 처리

오류 본문 구조가 Chat Completions에서 Responses API로 변경되었습니다.

이전 (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

이후 (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

주요 차이점:
- `innererror` 래퍼가 <strong>없어졌으며</strong> — 콘텐츠 필터 세부 사항이 이제 `error.body`의 최상위에 있습니다.
- `content_filter_result` (단수) → `content_filters` (복수 배열)로, 각 항목 안에 `content_filter_results` (복수)가 포함됩니다.
- `content_filters`의 각 항목에는 `blocked`, `source_type`, 그리고 카테고리별 세부사항이 포함된 `content_filter_results`(`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`)가 있습니다.

전체 Responses API 콘텐츠 필터 오류 본문 형태:
```json
{
  "message": "The response was filtered...",
  "type": "invalid_request_error",
  "param": "prompt",
  "code": "content_filter",
  "content_filters": [
    {
      "blocked": true,
      "source_type": "prompt",
      "content_filter_results": {
        "jailbreak": { "detected": true, "filtered": true },
        "hate": { "filtered": false, "severity": "safe" },
        "sexual": { "filtered": false, "severity": "safe" },
        "violence": { "filtered": false, "severity": "safe" },
        "self_harm": { "filtered": false, "severity": "safe" }
      }
    }
  ]
}
```

## 원시 HTTP 마이그레이션 (requests/httpx)

앱이 SDK 대신 Azure OpenAI REST를 직접 호출하는 경우:

이전 (Chat Completions):
```python
endpoint = f"{azure_endpoint}/openai/deployments/{deployment}/chat/completions?api-version=2024-03-01-preview"
data = {
    "messages": [{"role": "user", "content": query}],
    "model": model_name,
    "temperature": 0,
}
response = requests.post(endpoint, headers=headers, json=data)
message = response.json()["choices"][0]["message"]["content"]
```

이후 (Responses API):
```python
endpoint = f"{azure_endpoint}/openai/v1/responses"
data = {
    "model": deployment,
    "input": [{"role": "user", "content": query}],
    "temperature": 0,
    "max_output_tokens": 1000,
    "store": False,
}
response = requests.post(endpoint, headers=headers, json=data)
output_text = response.json()["output"][0]["content"][0]["text"]
```

> <strong>참고</strong>: `output_text`는 Python SDK의 `Response` 객체에 편의 속성입니다. 원시 REST JSON 응답에는 최상위 `output_text` 필드가 없으며 — 텍스트는 `output[0].content[0].text`에 있습니다.

## 다중 대화 턴
```python
# Responses API로 대화 구축하기
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# 대화에 어시스턴트의 응답 추가하기
messages.append({"role": "assistant", "content": response.output_text})

# 대화 계속하기
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

콘텐츠 타입 다중 턴 (명시적 `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id`를 통한 다중 턴 (대안)

대화 배열을 직접 관리하는 대신, `previous_response_id`를 사용해 서버 측에서 응답을 연쇄할 수 있습니다.
API는 각 응답을 저장하며 이전 턴을 자동으로 앞에 추가합니다.


```python
# 첫 번째 턴
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# 이후 턴 — 새 사용자 메시지와 이전 응답 ID 전달하기만 하면 됩니다
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**사용 시기:**

| 접근 방식 | 장점 | 단점 |
|---|---|---|
| `input` 배열 (수동) | 기록 전체 제어; 자르기/요약 가능; 서버 측 저장 필요 없음 (`store=False`) | 코드가 더 많음; 배열 직접 관리 필요 |
| `previous_response_id` | 간단한 코드; 자동 연쇄 | `store=True` 필요 (기본값); 대화 서버 측 저장; 턴 사이 기록 수정 불가 |

> **마이그레이션 참고:** 대부분 Chat Completions 앱은 이미 메시지 배열을 직접 관리하므로, `input` 배열로 변환하는 것이 더 직접적이고 1:1 마이그레이션입니다. 새 코드나 대화 기록을 조작하지 않을 경우 `previous_response_id`를 사용하세요.

## O-시리즈 추론 모델 (o1, o3-mini, o3, o4-mini)

O-시리즈 모델은 Responses API로 마이그레이션 시 고유한 매개변수 제약이 있습니다.

### O-시리즈 매개변수 매핑

| Chat Completions (o-시리즈) | Responses API | 참고 사항 |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | 높게 설정 (4096 이상) — 추론 토큰이 제한에 포함됨 |
| `reasoning_effort` | `reasoning.effort` | 존재하면 그대로 유지 (low/medium/high) |
| `temperature` | 제거하거나 `1`로 설정 | O-series는 `1`만 허용 |
| `top_p` | 제거 | o-series에서 지원하지 않음 |
| `seed` | 제거 | Responses API에서 지원하지 않음 |

### O-series 이전/이후

이전 (o-series Chat Completions):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

이후 (Responses API):
```python
resp = client.responses.create(
    model=deployment,
    input="Solve this step by step: 2x + 5 = 13",
    max_output_tokens=4096,
    reasoning={"effort": "medium"},
    store=False,
)
print(resp.output_text)
```

> <strong>참고</strong>: O-series 모델은 텍스트 델타를 내보내기 전에 추론 중 출력 버퍼링을 할 수 있습니다. 스트리밍은 계속 작동하지만 첫 번째 `response.output_text.delta` 이벤트가 GPT 모델 대비 더 긴 지연 후 도착할 수 있습니다.

## 추론 토큰 접근 방법
```python
# 추론 모델은 내부 추론을 사용합니다 — 얼마나 많은 추론 토큰이 사용되었는지 확인할 수 있습니다
response = client.responses.create(
    model=deployment,
    input="Explain quantum computing in simple terms",
    max_output_tokens=1000,
)
print(response.output_text)
print(f"Status: {response.status}")
print(f"Reasoning tokens: {response.usage.output_tokens_details.reasoning_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
```

> <strong>중요</strong>: 추론 모델 내부 추론 과정을 위해 `max_output_tokens=1000` (50–200이 아님)을 사용하세요. 모델은 최종 출력을 생성하기 전에 내부적으로 추론 토큰을 사용합니다.

## 구조화된 출력 — JSON 스키마
```python
resp = client.responses.create(
    model=deployment,
    input="What is the capital of France?",
    max_output_tokens=500,
    text={
        "format": {
            "type": "json_schema",
            "name": "Output",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {"answer": {"type": "string"}},
                "required": ["answer"],
                "additionalProperties": False,
            },
        }
    },
    store=False,
)
import json
data = json.loads(resp.output_text)
print(data["answer"])
```

## 도구 사용

- `tools`에 <strong>평면 Responses API 형식</strong>으로 함수 정의 — 최상위에 `name`, `description`, `parameters` (중첩된 `function` 아래 아님).
- 모델이 도구 호출을 요청하면 앱에서 실행하고 도구 결과를 다음 요청의 `input` 내 `function_call_output` 항목에 포함하세요.
- 스키마는 최소한으로 유지; 실행 전에 입력을 검증하세요.
- `strict: true`를 사용할 때는 모든 속성이 `required`에 나열되어야 하며 `additionalProperties: false`가 필수입니다.

> **⚠️ `pydantic_function_tool()`과 호환 불가**: `openai.pydantic_function_tool()` 헬퍼는 아직 이전 Chat Completions 중첩 형식(`{"type": "function", "function": {"name": ...}}`)을 생성합니다. `responses.create()`와 함께 사용하지 마세요. 도구 스키마를 수동으로 정의하거나 출력을 평면화하는 래퍼를 작성하세요.

### 도구 정의 형식

Responses API는 <strong>평면</strong> 도구 형식을 사용 — `name`, `description`, `parameters`는 최상위 키입니다 (`function` 아래가 아님).

**이전 (Chat Completions — 중첩):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**이후 (Responses API — 평면):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

전체 예시:
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are a weather chatbot."},
        {"role": "user", "content": "What's the weather in Berkeley?"},
    ],
    tools=tools,
    tool_choice="auto",
    store=False,
)
```

`strict: true` 설정 시 (스키마 강제):
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],       # 모든 속성이 나열되어야 합니다
            "additionalProperties": False,   # 엄격 모드에 필요합니다
        },
    }
]
```

### 도구 호출 왕복 (실행 및 결과 반환)

모델이 도구 호출을 요청할 때는 `response.output` 항목 + `function_call_output`을 사용하세요 — Chat Completions의 `role: assistant` + `role: tool` 패턴이 아닙니다.

```python
import json

messages = [
    {"role": "system", "content": "You are a weather chatbot."},
    {"role": "user", "content": "Is it sunny in Berkeley?"},
]

response = client.responses.create(
    model=deployment, input=messages, tools=tools, store=False,
)

tool_calls = [item for item in response.output if item.type == "function_call"]
if tool_calls:
    # 모델의 function_call 항목을 대화에 추가합니다
    messages.extend(response.output)

    # 각 도구를 실행하고 결과를 추가합니다
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # 도구 결과로 최종 응답을 받습니다
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### 몇 샷 도구 호출 예시

`input`에서 도구 호출 몇 샷 예시를 제공할 때는 `function_call`과 `function_call_output` 항목을 사용하세요. ID는 `fc_`로 시작해야 합니다.

```python
messages = [
    {"role": "system", "content": "You are a product search assistant."},
    {"role": "user", "content": "Find climbing gear for outdoors"},
    {
        "type": "function_call",
        "id": "fc_example1",
        "call_id": "call_example1",
        "name": "search_database",
        "arguments": '{"search_query": "climbing gear outdoor"}',
    },
    {
        "type": "function_call_output",
        "call_id": "call_example1",
        "output": "Results: ...",
    },
    {"role": "user", "content": "Now find shoes under $50"},
]
```

```python
# 내장 웹 검색 예제
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## 이미지 입력

이미지 콘텐츠 항목 유형이 `image_url`에서 `input_image`로 변경되었고, URL은 중첩 객체에서 평면 문자열로 변경되었습니다.

### 이미지 입력 — 이전 (Chat Completions)
```python
resp = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

### 이미지 입력 — 이후 (Responses API, URL)
```python
resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": "https://example.com/image.jpg",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

### 이미지 입력 — 이후 (Responses API, base64)
```python
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image("path_to_your_image.jpg")

resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

> **주요 변경점**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (중첩 객체) → `"image_url": "..."` (평면 문자열 — HTTPS URL 또는 `data:image/...;base64,...` 데이터 URI), (3) `"type": "text"` → `"type": "input_text"`.

## 마이크로소프트 에이전트 프레임워크 (MAF) 마이그레이션

**먼저 MAF 버전을 확인하세요** — 마이그레이션은 MAF 1.0.0+인지 또는 1.0.0 이전 베타/RC인지에 따라 다릅니다.

확인 방법: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+에서는 `OpenAIChatClient`가 <strong>이미 Responses API를 사용</strong>합니다 — 마이그레이션 불필요.

코드베이스가 기존 `OpenAIChatCompletionClient` (`chat.completions.create` 사용)를 사용하면 `OpenAIChatClient`로 교체하세요:

이전:
```python
from agent_framework.openai import OpenAIChatCompletionClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatCompletionClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

이후:
```python
from agent_framework.openai import OpenAIChatClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

### MAF 1.0.0 이전 (베타/RC 릴리스)

1.0.0 이전 MAF에서는 `OpenAIChatClient`가 Chat Completions를 사용했습니다. 기본적으로 Responses API를 사용하는 `agent-framework-openai>=1.0.0`로 업그레이드하세요.

> <strong>참고</strong>: `Agent`, `MCPStreamableHTTPTool` 및 기타 MAF API는 변경되지 않으며 클라이언트 클래스 임포트 및 인스턴스화만 변경됩니다.

## LangChain (`langchain-openai`) 마이그레이션

`ChatOpenAI()`에 `use_responses_api=True`를 추가하고 메시지 콘텐츠 접근을 `.content`에서 `.text`로 변경하세요.

이전:
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
)

# ... 에이전트 호출 ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

이후:
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
    use_responses_api=True,
)

# ... 에이전트 호출 ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **주요 변경사항**: (1) 생성자에 `use_responses_api=True` 추가, (2) 응답 메시지에서 `.content` → `.text`.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->