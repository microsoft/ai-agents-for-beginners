---
name: azure-openai-to-responses
license: MIT
---
# Azure OpenAI 채팅완성에서 Responses API로 파이썬 앱 마이그레이션하기

> **권위 있는 안내 — 정확히 따르세요**
>
> 이 스킬은 Azure OpenAI 채팅완성을 사용하는 파이썬 코드베이스를
> 통합 Responses API로 마이그레이션합니다. 아래 지침을 정확히 따르세요.
> 매개변수 매핑을 임의로 조작하거나 API 형태를 임의로 만들지 마십시오.

---

## 트리거

사용자가 다음 동작을 원할 때 이 스킬을 활성화하세요:
- Azure OpenAI 채팅완성에서 Responses API로 파이썬 앱 마이그레이션
- Azure OpenAI를 대상으로 파이썬 OpenAI SDK를 최신 API 형태로 업그레이드
- Responses가 필요한 GPT-5 이상 모델을 위해 파이썬 코드 준비
- `AzureOpenAI`/`AsyncAzureOpenAI`에서 v1 엔드포인트를 사용하는 표준 `OpenAI`/`AsyncOpenAI` 클라이언트로 전환
- `AzureOpenAI` 생성자 혹은 `api_version` 관련 사용 중단 경고 해결

---

## ⚠️ 모델 호환성 — 반드시 먼저 확인

> **마이그레이션 전, Azure OpenAI 배포가 Responses API를 지원하는지 확인하세요.**

### 1. 배포 스모크 테스트 (가장 빠름)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> <strong>참고</strong>: Azure OpenAI에서는 `max_output_tokens`가 <strong>최소 16</strong>입니다. 16 미만 값은 400 에러를 반환합니다. 스모크 테스트 시 50 이상을 사용하세요.

결과가 404이면 배포된 모델이 아직 Responses를 지원하지 않는 것입니다 — 아래 참고 문서를 확인하거나 지원되는 모델로 다시 배포하세요.

### 2. 리전 내 사용 가능한 모델 확인 (권장)

내 리전에서 Responses API를 지원하는 모델이 어떤 것이 있는지 내장된 모델 호환성 도구를 실행하세요:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

이 도구는 Azure ARM 라이브 쿼리를 수행해 호환성 매트릭스(Responses, 구조화된 출력, 도구 지원 등)를 보여줍니다. `--filter gpt-5.1,gpt-5.2`로 결과를 좁히거나 `--json`으로 스크립팅할 수 있습니다.

### 3. 전체 모델 지원 참조

- **라이브 쿼리**: `python migrate.py models` (위 설명 참조 — 리전별, 항상 최신)
- **가용성 탐색**: [모델 요약 테이블 및 리전 가용성](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **빠른 시작 및 안내**: **https://aka.ms/openai/start**

### ⚠️ 구형 모델 제한 사항

> <strong>경고</strong>: `gpt-4.1` 이전 구형 모델은 Responses API의 모든 기능을 완전히 지원하지 않을 수 있습니다.
>
> 구형 모델의 알려진 제한점:
> - **`reasoning` 매개변수**: 비추론 모델 다수는 미지원. 원본 코드에 `reasoning`이 이미 존재할 경우에만 마이그레이션.
> - **`seed` 매개변수**: Responses API에서 전혀 미지원 — 모든 요청에서 제거.
> - **`text.format` 통한 구조화 출력**: 구형 모델은 `strict: true` JSON 스키마를 신뢰성있게 강제하지 못할 수 있음.
> - **도구 오케스트레이션**: GPT-5 이상은 내부 추론 과정에서 도구 호출을 오케스트레이션함. 구형 모델도 Responses 사용 가능하지만 이 깊은 통합은 없음.
> - **온도 제약**: `gpt-5` 마이그레이션 시 온도를 생략하거나 `1`로 설정해야 함. 구형 모델은 제약 없음.

### O-시리즈 추론 모델 (o1, o3-mini, o3, o4-mini)

O-시리즈 모델은 고유한 매개변수 제약이 있습니다. o-시리즈 용 앱을 마이그레이션할 때:

- **`temperature`**: `1`이어야 하며(혹은 생략 가능). 다른 값 허용 안 됨.
- **`max_completion_tokens` → `max_output_tokens`**: Azure 전용 `max_completion_tokens` 사용 앱은 `max_output_tokens`로 전환. 추론 토큰을 고려해 4096 이상 높게 설정 권장.
- **`reasoning_effort`**: `reasoning_effort`(low/medium/high) 사용시 유지 — Responses API가 o-시리즈 모델에 대해 지원함.
- **스트리밍 동작**: o-시리즈 모델은 추론 종료까지 출력을 버퍼링한 후 텍스트 델타 이벤트 방출 가능. 스트리밍은 동작하지만 첫 `response.output_text.delta`가 GPT 모델보다 지연될 수 있음.
- **`top_p`**: o-시리즈는 미지원 — 사용 중이면 제거.
- **도구 사용**: o-시리즈는 GPT 모델과 유사하게 Responses API를 통해 도구 지원하지만 도구 호출 오케스트레이션 품질은 모델별 차이 있음.

**조치 — 사전 모델 조언**: 스캔 시 앱이 타깃팅하는 모델(배포 이름, 환경 변수, 설정)을 확인하세요. `gpt-4.1` 미만 모델이면 아래를 사용자에게 미리 알려주십시오:
- 기본 텍스트, 채팅, 스트리밍, 도구는 현재 모델에서 마이그레이션 가능.
- 최신 모델(`gpt-5.1`, `gpt-5.2`)은 향상된 도구 오케스트레이션, 구조화 출력 강제, 추론, 크로스 리전 가용성 제공.
- 준비되면 배포 업그레이드를 고려하라고 권장 — 마이그레이션 차단 요소는 아님.

모델 버전으로 마이그레이션을 차단하거나 거부하지 마십시오. 조언은 참고용입니다.

### GitHub 모델은 Responses API를 지원하지 않음

> **GitHub 모델(`models.github.ai`, `models.inference.ai.azure.com`)은 Responses API를 지원하지 않습니다.**

코드베이스에 GitHub 모델 코드 경로(`base_url`이 `models.github.ai` 또는 `models.inference.ai.azure.com`인 경우)가 있으면 마이그레이션 시 완전히 제거해야 합니다. Responses API는 Azure OpenAI, OpenAI 또는 호환 로컬 엔드포인트(예: Responses 지원 Ollama) 필요합니다.

스캔 중 조치:
- GitHub 모델 코드 경로 제거 플래그 지정.

---

## 프레임워크 마이그레이션

많은 앱이 OpenAI 위에 상위 프레임워크를 사용합니다. 이들 마이그레이션 시에는 기본 OpenAI 호출만 아니라 프레임워크 자체 API 변경도 필요합니다.

### Microsoft Agent Framework (MAF)

**먼저 MAF 버전을 확인하세요** — 마이그레이션은 MAF 1.0.0 이상인지 아닌지에 따라 다릅니다 (베타/RC 버전 구분).

#### MAF 1.0.0 이상 (agent-framework-openai >= 1.0.0)

`OpenAIChatClient`는 <strong>이미 Responses API를 사용</strong>하고 있어 마이그레이션이 필요 없습니다. 레거시 `OpenAIChatCompletionClient`(`chat.completions.create` 사용) 코드는 `OpenAIChatClient`로 교체하세요.

| 이전 | 이후 |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

버전 확인: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF 1.0.0 이전 (베타/RC 릴리스)

MAF 1.0.0 이전 버전은 `OpenAIChatClient`가 채팅완성을 사용합니다. `agent-framework-openai>=1.0.0`으로 업그레이드하면 `OpenAIChatClient`가 기본적으로 Responses API를 사용합니다.

다른 변경사항은 필요 없습니다 — `Agent`와 도구 API는 동일합니다.

### LangChain (`langchain-openai`)

`ChatOpenAI()` 호출에 `use_responses_api=True`를 추가하세요. 응답 접근은 `.content`에서 `.text`로 업데이트하세요.

| 이전 | 이후 |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

전체 전후 코드 예시는 [cheat-sheet.md](./references/cheat-sheet.md)를 참조하세요.

---

## 프런트엔드 마이그레이션 안내

> **Responses API는 서버 사이드 문제입니다.** 파이썬 백엔드만 마이그레이션하세요; 프런트엔드의 HTTP 계약은 백엔드가 단순 중계가 아닌 한 변경하지 않아야 합니다. 단순 패스스루인 경우, 변환 레이어 제거를 위해 Responses 요청 형태 채택을 고려하세요. 프런트엔드가 클라이언트 키로 직접 OpenAI를 호출한다면, 우선 백엔드로 이전하세요.

### `@microsoft/ai-chat-protocol` 사용 중단

`@microsoft/ai-chat-protocol` npm 패키지는 사용 중단되었으며 [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream)으로 대체해야 합니다. 프런트엔드에서 이 패키지를 발견하면:

1. CDN 스크립트 태그 교체:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` 인스턴스 생성(`new ChatProtocol.AIChatProtocolClient("/chat")`) 제거.
3. `client.getStreamedCompletion(messages)`를 백엔드 스트리밍 엔드포인트 직접 `fetch()` 호출로 대체.
4. `for await (const response of result)`를 `for await (const chunk of readNDJSONStream(response.body))`로 변경.
5. 속성 접근을 `response.delta.content` / `response.error`에서 `chunk.delta.content` / `chunk.error`로 업데이트.

---

## 목표

- Azure OpenAI 대상 채팅완성 또는 레거시 완성 호출 위치 모두 열거
- 파이썬 코드베이스에 대한 마이그레이션 계획과 순서 제안
- 안전하고 최소한의 수정으로 Responses API 전환 적용
- 호출 측을 Responses 출력 스키마 소비로 업데이트; 역호환 래퍼 미사용
- 테스트/린트 실행; 마이그레이션 도중 발생한 사소한 깨짐 수정
- 작고 검토 편한 변경 세트 준비 및 최종 요약(diff 포함) 제공 (커밋 금지)

---

## 안전장치

- git 작업 공간 내부 파일만 수정. 절대 외부 파일 작성 금지.
- 역호환성 셈 도구 삭제; 코드를 새 API 형태로 마이그레이션.
- 주석 전환표시 또는 백업 파일 남기지 말 것.
- 이전에 스트리밍 사용 시 유지; 미사용 시에는 비스트리밍 활용.
- 승인 모드일 때 명령 실행 및 네트워크 호출 전 승인 요청.
- `git add`/`git commit`/`git push` 실행하지 말고 작업 트리 편집만 생성.

---

## 0단계: Azure OpenAI 클라이언트 마이그레이션 (선행조건)

코드베이스가 `AzureOpenAI` 또는 `AsyncAzureOpenAI` 생성자를 사용하면 우선 표준 `OpenAI` / `AsyncOpenAI` 생성자로 마이그레이션합니다. Azure 전용 생성자는 `openai>=1.108.1`에서 사용 중단되었습니다.

### 왜 v1 API 경로인가?

신규 `/openai/v1` 엔드포인트는 `AzureOpenAI()` 대신 표준 `OpenAI()` 클라이언트를 사용하며, `api_version` 매개변수가 필요 없고 OpenAI와 Azure OpenAI에서 동일하게 작동합니다. 이 클라이언트 코드는 미래에도 호환되며 버전 관리가 필요 없습니다.

### 핵심 변경사항

| 이전 | 이후 |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | 완전히 제거 |

### 정리 체크리스트

- 클라이언트 생성자에서 `api_version` 인자 제거.
- `.env`, 앱 설정, Bicep/인프라 파일에서 `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` 환경 변수 제거.
- `.env`, 앱 설정, Bicep/인프라, 테스트 픽스처에서 `AZURE_OPENAI_CLIENT_ID`를 `AZURE_CLIENT_ID`로 이름 변경 (표준 Azure Identity SDK 관례).
- `requirements.txt` 또는 `pyproject.toml`에서 `openai>=1.108.1` 확인.

### 환경 변수 마이그레이션

| 기존 환경 변수 | 조치 | 비고 |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | <strong>제거</strong> | v1 엔드포인트에서 `api_version` 불필요 |
| `AZURE_OPENAI_API_VERSION` | <strong>제거</strong> | 위와 동일 |
| `AZURE_OPENAI_CLIENT_ID` | **이름 변경** → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)`용 표준 Azure Identity SDK 관례 |
| `AZURE_OPENAI_ENDPOINT` | <strong>유지</strong> | 여전히 `base_url` 생성에 사용 |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | <strong>유지</strong> | `responses.create`의 `model` 파라미터로 사용 |
| `AZURE_OPENAI_API_KEY` | <strong>유지</strong> | 키 기반 인증을 위한 `api_key`로 사용 |

클라이언트 설정 코드 예제(동기, 비동기, EntraID, API 키, 다중 테넌트)는 [cheat-sheet.md](./references/cheat-sheet.md) 참조.

---

## 1단계: 레거시 호출 위치 감지

마이그레이션 대상 호출 위치 전체를 찾으려면 [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) 스크립트를 실행하세요:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

또는 수동으로 다음 검색을 실행하세요 — 모든 일치 위치가 마이그레이션 대상입니다:

```bash
# 레거시 API 호출 (재작성 필요)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# 더 이상 사용되지 않는 Azure 클라이언트 생성자 (교체 필요)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# 응답 형식 접근 패턴 (업데이트 필요)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# 이전 중첩 형식의 도구 정의 (평탄화 필요)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# 이전 형식의 도구 결과 (function_call_output으로 변환 필요)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# 더 이상 사용되지 않는 매개변수 (제거 또는 이름 변경 필요)
rg "response_format"
rg "max_tokens\b"        # max_output_tokens로 이름 변경
rg "['\"]seed['\"]"      # remove entirely

# 더 이상 사용되지 않는 환경 변수 (정리 필요)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID여야 함

# GitHub 모델 엔드포인트 (제거 필요 — 응답 API 미지원)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# 프레임워크 수준 레거시 패턴 (업데이트 필요)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0 이상: OpenAIChatClient로 교체
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True 필요

# 테스트 인프라 (업데이트 필요)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# 콘텐츠 필터 오류 본문 접근 (업데이트 필요 — 구조 변경)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # 이전 단수형 — 현재 content_filters 배열 내의 content_filter_results (복수형)

# Chat Completions 엔드포인트에 대한 원시 HTTP 호출 (URL 업데이트 필요)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### 휴리스틱 (감지 및 재작성)

- **채팅완성 클라이언트**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure 클라이언트 생성자**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- <strong>도구</strong>: 중첩 형식(`{"type": "function", "function": {"name": ...}}`)에서 평면 Responses 형식(`{"type": "function", "name": ...}`)으로 함수 호출 도구 정의 변환; `tool_choice` 사용; 도구 결과는 `{"type": "function_call_output", "call_id": ..., "output": ...}` 항목으로 반환( `{"role": "tool", ...}` 아님).
- **도구 왕복**: 모델이 함수 호출을 반환할 때, 대화에 `response.output` 항목을 추가(수동 `{"role": "assistant", "tool_calls": [...]}` 딕셔너리 아님), 그런 다음 각 결과에 대해 `function_call_output` 항목 추가.
- **소수 샷 도구 예제**: 대화에 하드코딩된 도구 호출 예제가 포함된 경우, 이를 `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` 항목으로 변환. ID는 반드시 `fc_`로 시작해야 함.
- **`pydantic_function_tool()`**: 이 도우미는 여전히 이전 중첩 형식을 생성하며 `responses.create()`와 **호환되지 않음**. 수동 도구 정의 또는 평면화 래퍼로 교체.
- **다중 턴**: 앱 내에서 대화 기록 유지; 이전 턴은 `input` 항목을 통해 전달.
- <strong>포맷팅</strong>: Chat의 최상위 `response_format`을 Responses의 `text.format`으로 교체. 표준 형태: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **내용 항목**: Chat `content[].type: "text"`를 Responses `content[].type: "input_text"`로 교체 (사용자/시스템 턴 대상).
- **이미지 내용 항목**: Chat `content[].type: "image_url"`를 Responses `content[].type: "input_image"`로 교체. `image_url` 필드는 중첩 객체 `{"url": "..."}`에서 평면 문자열로 변경됨. 전/후 예제는 치트 시트 참조.
- **추론 노력**: **원본 코드에 이미 `reasoning`이 있을 경우에만 마이그레이션 수행**.
- **콘텐츠 필터 오류 처리**: 오류 본문 구조 변경. Chat Completion은 `error.body["innererror"]["content_filter_result"]` (단수) 사용; Responses API는 `error.body["content_filters"][0]["content_filter_results"]` (복수, 배열 내) 사용. `innererror`에 접근하는 코드는 `KeyError` 발생함. 새 경로로 재작성.
- **원시 HTTP 호출**: 앱이 Azure OpenAI REST API를 직접 호출할 경우 (`requests`, `httpx` 등 사용; 경로: `/openai/deployments/{name}/chat/completions?api-version=...`), `/openai/v1/responses`로 재작성. 요청 본문 변경: `messages` → `input`, `max_output_tokens` 및 `store: false` 추가, `api-version` 쿼리 파라미터 제거. 응답 본문 변경: `choices[0].message.content` → `output[0].content[0].text` (참고: `output_text`는 SDK 편의 속성으로 원시 REST JSON에는 없음).

---

## 2단계: 마이그레이션 적용

### 마이그레이션 노트 (Chat Completions → Responses)

- <strong>이유</strong>: Responses는 텍스트, 도구, 스트리밍을 위한 통합 API이며; Chat Completions는 레거시. GPT-5부터는 최고의 성능을 위해 Responses 필수.
- **HTTP**: Azure 엔드포인트가 `/openai/deployments/{name}/chat/completions`에서 `/openai/v1/responses`로 변경.
- <strong>필드</strong>: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature`는 변동 없음.
- <strong>포맷팅</strong>: `response_format` → `text.format` (객체형).
- **내용 항목**: 시스템/사용자 턴에 대해 Chat `content[].type: "text"`를 Responses `content[].type: "input_text"`로 교체.
- **이미지 내용 항목**: Chat `content[].type: "image_url"`를 Responses `content[].type: "input_image"`로 교체. `image_url` 필드는 `{"image_url": {"url": "..."}}`에서 `{"image_url": "..."}`로 평면화 (평범한 문자열 — HTTPS URL 또는 `data:image/...;base64,...` 데이터 URI).

### 매개변수 매핑 참조

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (항목 배열) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (객체) |
| `temperature` | `temperature` (변경 없음) |
| `stop` | `stop` (변경 없음) |
| `frequency_penalty` | `frequency_penalty` (변경 없음) |
| `presence_penalty` | `presence_penalty` (변경 없음) |
| `tools` / 함수 호출 | `tools` (변경 없음) |
| `seed` | <strong>제거</strong> (지원하지 않음) |
| `store` | `store` (항상 `false`로 설정) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (평면 문자열) |

전체 전/후 코드 예제는 [cheat-sheet.md](./references/cheat-sheet.md) 참조.

테스트 인프라 마이그레이션(모의, 스냅샷, 단언) 관련 내용은 [test-migration.md](./references/test-migration.md) 참조.

오류 및 주의사항 문제 해결사항은 [troubleshooting.md](./references/troubleshooting.md) 참조.

---

## 데이터 보존 및 상태

- 모든 Responses 요청에 `store: false` 설정.
- 이전 메시지 ID나 서버 저장 컨텍스트에 의존하지 말고; 상태는 클라이언트 측에서 관리 및 메타데이터 최소화.

---

## 수용 기준

### 코드 수준 게이트 (모두 통과해야 함)

- [ ] 마이그레이션된 파일 내에서 `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"`의 일치 항목 없음.
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` 일치 항목 없음 — 모든 생성자는 v1 엔드포인트를 사용하는 `OpenAI`/`AsyncOpenAI`.
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` 일치 항목 없음 — GitHub 모델 코드 경로 제거됨.
- [ ] `rg "OpenAIChatCompletionClient"` 일치 항목 없음 — MAF 1.0.0+ 코드는 `OpenAIChatClient` 사용 (Responses API 사용). 1.0.0 이전 버전은 `agent-framework-openai>=1.0.0`으로 업그레이드.
- [ ] 모든 `ChatOpenAI(...)` 호출에 `use_responses_api=True` 포함.
- [ ] `rg "choices\[0\]"` 일치 항목 없음 — 응답 접근은 모두 `resp.output_text` 또는 Responses 출력 스키마 사용.
- [ ] 최상위 수준에 `response_format` 없음; 모든 구조화된 출력은 `text={"format": {...}}` 사용.
- [ ] `requirements.txt` 또는 `pyproject.toml`에 `openai>=1.108.1` 및 `azure-identity`; 의존성 재설치됨.
- [ ] 모든 `responses.create` 호출에 `store=False` 설정됨.
- [ ] 클라이언트 생성에 `api_version` 없음; 환경 파일 및 인프라에서 `AZURE_OPENAI_API_VERSION` 제거됨.

### 테스트 인프라 게이트 (모두 통과해야 함)

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` 일치 항목 없음.
- [ ] `rg "_azure_ad_token_provider" tests/` 일치 항목 없음 — 단언문은 `isinstance(client, AsyncOpenAI)` 또는 `base_url` 확인으로 업데이트됨.
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` 일치 항목 없음 — Azure 특정 필터 모의 제거됨.
- [ ] 모의 픽스처는 `kwargs.get("input")` 사용, `kwargs.get("messages")` 아님.
- [ ] 스냅샷/골든 파일은 Responses 스트리밍 형태로 업데이트됨 (`choices[0]`, `function_call`, `logprobs` 등 없음).
- [ ] 모든 테스트 업데이트 후 `pytest`는 실패 없이 통과.

### 동작 게이트 (수동 또는 테스트 하니스 통해 검증)

- [ ] **기본 완료**: 비스트리밍 `responses.create`가 비어 있지 않은 `output_text` 반환.
- [ ] **스트림 동등성**: 원본 코드에 스트리밍이 사용되었다면, 마이그레이션된 코드도 스트리밍하며 비어 있지 않은 델타와 함께 `response.output_text.delta` 이벤트를 산출.
- [ ] **구조화된 출력**: `text.format`을 `json_schema`와 함께 사용하는 경우, `json.loads(resp.output_text)`가 성공하고 스키마와 일치함.
- [ ] **도구 호출 루프**: 도구 사용 시, 모델이 도구 호출을 발행하고 앱이 이를 실행하며, 후속 요청이 최종 `output_text`를 반환 (무한 루프 아님).
- [ ] **비동기 동등성**: `AsyncAzureOpenAI` 사용한 경우, `AsyncOpenAI` 동등 기능이 `await`와 함께 작동.
- [ ] <strong>오류률</strong>: 마이그레이션 전 기준과 비교하여 새로운 400/401/404 오류 없음.

### 산출물

- 수정된 파일, 레거시 호출 지점의 전/후 개수, 다음 단계가 포함된 요약.
- 변경사항은 작업 트리 편집만 포함 (커밋 아님).

---

## SDK 버전 요구 사항

| 패키지 | 최소 버전 |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | 최신 (EntraID 인증용) |

---

## 참고자료

- [치트 시트 — 모든 코드 스니펫](./references/cheat-sheet.md)
- [테스트 마이그레이션 — 모의, 스냅샷, 단언문](./references/test-migration.md)
- [문제 해결 — 오류, 위험 표, 주의사항](./references/troubleshooting.md)
- [detect_legacy.py — 자동 스캐너](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI 스타터 키트](https://aka.ms/openai/start)
- [Azure OpenAI Responses API 문서](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API 버전 수명 주기](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API 참조](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->