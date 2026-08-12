# 문제 해결, 위험 표 및 주의 사항

## 400번대 오류 문제 해결

| 오류 | 해결 방법 |
|-------|-----|
| `missing_required_parameter: tools[0].name` | 도구 정의가 이전 Chat Completions 중첩 형식을 사용함 | `{"type": "function", "function": {"name": ...}}`에서 `{"type": "function", "name": ..., "parameters": ...}`로 평탄화 — name, description, parameters는 최상위에 위치해야 함 |
| `unknown_parameter: input[N].tool_calls` | 다중 턴 도구 결과가 이전 Chat Completions 형식을 사용함 | `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}`를 `response.output` 항목 + `{"type": "function_call_output", "call_id": ..., "output": ...}`로 교체 |
| `invalid_function_parameters: 'required' is required` | `strict: true` 도구에 `required` 배열 누락 | `strict: true`일 때는 모든 속성이 `required`에 나열되어야 하며 `additionalProperties: false`가 설정되어야 함 |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` 도구에 `additionalProperties: false` 누락 | 파라미터 객체에 `"additionalProperties": false` 추가 |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | 몇 샷 function_call ID 접두사 오류 | 함수 호출 ID는 `call_`가 아닌 `fc_`로 시작해야 함 (예: `fc_example1`) |
| `missing_required_parameter: text.format.name` | 형식 딕셔너리에 `"name"` 키 추가 (예: `"name": "Output"`) |
| `invalid_type: text.format` | `text.format`이 문자열이 아닌 `type`, `name`, `strict`, `schema` 키가 있는 딕셔너리인지 확인 |
| `invalid input content type` | Chat `text` 대신 `input_text`/`output_text` 콘텐츠 유형 사용 |
| `invalid input content type` (이미지) | 이미지 콘텐츠 유형이 여전히 `"type": "image_url"` | `"type": "input_image"`로 변경 |
| `Expected object, got string` on `image_url` | `image_url`이 여전히 `{"url": "..."}` 중첩 객체 | 평탄화하여 단순 문자열로: `"image_url": "https://..."` 또는 `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` for `max_output_tokens` | Azure OpenAI에서 최소 값은 <strong>16</strong>임. 테스트에는 50+, 프로덕션에는 1000+ 사용 |
| `429 Too Many Requests` during streaming | 속도 제한됨. 스트리밍을 `try/except`로 감싸고, 오류 JSON을 프런트엔드에 전달, 백오프/재시도 구현 |
| `KeyError: 'innererror'` on content filter error | Responses API에서 콘텐츠 필터 오류 본문 구조 변경됨 | Chat Completions는 `error.body["innererror"]["content_filter_result"]` 사용; Responses API는 `error.body["content_filters"][0]["content_filter_results"]` (복수 및 배열 내부) 사용. 모든 `innererror` 접근 방식 수정 필요 |

---

## 마이그레이션 위험 표

| 증상 | 가능성 있는 실수 | 해결 방법 |
|---------|---------------|-----|
| 빈 `output_text` / 잘린 응답 | 추론 모델에 `max_output_tokens`가 너무 낮음 | `max_output_tokens=1000` 이상으로 설정 — 추론 토큰도 한도에 포함 |
| `400 invalid_type: text.format` | `response_format` 문자열을 `text.format` 딕셔너리 대신 전달 | `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` 사용 |
| `/openai/v1/responses`에서 `404 Not Found` | `/openai/v1/` 접미사 누락된 잘못된 `base_url` | `base_url=f"{endpoint}/openai/v1/"` (슬래시 포함)인지 확인 |
| `OpenAI()`로 전환 후 `401 Unauthorized` | `api_key` 미설정 또는 토큰 공급자 전달 오류 | EntraID: `api_key=token_provider` (호출 가능한 객체). API 키: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| 모델이 `deployment not found` 반환 | `model` 매개변수가 Azure 배포 이름과 일치하지 않음 | `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` 사용 — 배포 이름이고 모델 이름이 아님 |
| `json.loads(resp.output_text)`에서 `JSONDecodeError` 발생 | 스키마 미적용 또는 모델이 엄격한 JSON 미지원 | 스키마에 `"strict": True` 설정 확인 및 모델이 구조화 출력 지원 확인 |
| 스트리밍에 `delta` 이벤트 없음 | 잘못된 이벤트 유형 검사 | `event.type == "response.output_text.delta"` 필터링, Chat의 `chat.completion.chunk`가 아님 |
| 마이그레이션 후 이미지 입력에서 `400` 오류 | 이미지 콘텐츠 유형 업데이트 누락 | `"type": "image_url"` → `"type": "input_image"` 변경 및 `"image_url": {"url": "..."}` → `"image_url": "..."` (단순 문자열) 평탄화 |
| 도구 호출 무한 루프 | 후속 `input`에 도구 결과 누락 | 도구 실행 후 다음 요청의 `input`에 `{"type": "function_call_output", "call_id": ..., "output": ...}` 항목 추가 |
| GPT-5 또는 o-series에서 `temperature` 오류 | 1 이외의 명시적 `temperature` 값 | GPT-5 및 o-series 모델(o1, o3-mini, o3, o4-mini)에서는 `temperature` 제거하거나 `1`로 설정 |
| o-series에서 `top_p` 오류 | `top_p` 지원 안 됨 | o-series 모델 대상일 때 `top_p` 제거 |
| `max_completion_tokens` 인식 안 됨 | Azure 전용 매개변수 사용 | `max_completion_tokens`를 `max_output_tokens`로 교체. o-series 대상 시 4096+ 설정 (추론 토큰 포함) |
| o-series 출력이 비거나 잘림 | `max_output_tokens` 지나치게 낮음 | o-series는 내부 추론 토큰 사용. `max_output_tokens=4096` 이상 설정 — 500~1000 아님 |
| `400 integer_below_min_value` for `max_output_tokens` | 값이 16 미만 | Azure OpenAI는 `max_output_tokens >= 16` 필수. smoke 테스트 50+, 프로덕션 1000+ 사용 |
| 스트림 중간에 `429 Too Many Requests` | Azure OpenAI 속도 제한 | 스트림이 오류 없이 중단됨. 항상 `async for event in await coroutine:`를 `try/except`로 감싸고 `{"error": str(e)}`를 프런트엔드에 전달 |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | 잘못된 테넌트 또는 로그인 안 됨 | `tenant_id=os.getenv("AZURE_TENANT_ID")` 명시적으로 전달. 로컬에서 `azd auth login --tenant <tenant-id>` 실행 |
| GitHub Models (`models.github.ai`) 사용 시 `404 Not Found` | GitHub 모델은 Responses API 지원 안 함 | GitHub Models 코드 경로 완전히 제거. Azure OpenAI, OpenAI 또는 Responses 지원 로컬 엔드포인트(e.g., Ollama) 사용 |
| MAF `OpenAIChatCompletionClient`가 여전히 Chat Completions 사용 | 1.0.0 이상에서 레거시 MAF 클라이언트 사용 | MAF 1.0.0 이상에서 `OpenAIChatClient`가 기본으로 Responses API 사용. `OpenAIChatCompletionClient` → `OpenAIChatClient` 교체. 1.0.0 이전 버전은 `agent-framework-openai>=1.0.0`로 업그레이드. |
| LangChain 에이전트가 도구 호출 시 비거나 실패 | `ChatOpenAI`가 Responses API 미사용 | `ChatOpenAI(...)`에 `use_responses_api=True` 추가. 응답 메시지의 `.content`를 `.text`로 변경 |
| 콘텐츠 필터 오류 처리기에서 `KeyError: 'innererror'` | Responses API에서 오류 본문 구조 변경 | `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`로 수정. `innererror` 래퍼 제거, 콘텐츠 필터 세부 정보는 최상위 `content_filters` 배열 내부 각 항목의 복수형 `content_filter_results`에 존재 |
| `/openai/deployments/.../chat/completions`에 대한 원시 HTTP 호출이 404 반환 | 이전 Chat Completions REST 엔드포인트 사용 | URL을 `/openai/v1/responses`로 바꾸고, 요청 본문에서 `messages` → `input` 변경, `max_output_tokens` + `store: false` 추가, `api-version` 쿼리 파라미터 제거. 응답 파싱 시 `choices[0].message.content` → `output[0].content[0].text` 변경 (참고: `output_text`는 SDK 편의 속성이며 원시 REST JSON에 없음). |

---

## 주의 사항

1. 이전에 Chat Completions로 대화 상태를 관리했다면 Responses로 명시적으로 상태를 관리해야 합니다.
2. 구버전 `max_tokens`보다는 `max_output_tokens`를 사용하는 것이 좋습니다.
3. `gpt-5`로 마이그레이션 시 `temperature`가 지정되어있거나 1이 아닌 경우가 없도록 확인하세요.
4. Chat의 `content[].type: "text"` 대신 Responses의 `content[].type: "input_text"`를 사용자/시스템 입력에 사용하세요.
5. `text.format`에는 일반 문자열이 아닌 적절한 딕셔너리(예: `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`)를 제공해야 합니다.
6. Responses는 `seed` 매개변수를 지원하지 않으므로 요청에서 제거하세요.
7. **추론(reasoning)**: 원래 코드에서 이미 `reasoning`을 사용했다면 포함하세요. 그렇지 않은 API 호출에 `reasoning`을 추가하지 마세요 — 많은 비추론 모델이 이 매개변수를 지원하지 않습니다.
8. **`max_output_tokens` 크기**: 추론 모델(GPT-5-mini, GPT-5, o-series)은 `max_output_tokens=4096` 이상을 사용하세요 — 50~1000은 안 됩니다. 모델은 출력 전에 내부적으로 추론 토큰을 사용하므로 너무 낮으면 출력이 잘리거나 비게 됩니다.
9. **O-series `max_completion_tokens`**: 원래 코드에서 Azure 전용 `max_completion_tokens`를 사용했다면 `max_output_tokens`로 교체하세요. Responses API는 `max_completion_tokens`를 허용하지 않습니다.
10. **O-series `reasoning_effort`**: 원래 코드에서 `reasoning_effort`(low/medium/high)를 사용했다면 Responses API 호출에서 `reasoning={"effort": "<값>"}`로 마이그레이션하세요.
11. **O-series 스트리밍 지연**: O-series 모델은 출력 생성 전에 내부적으로 추론을 수행합니다. 스트리밍 시 첫 번째 `response.output_text.delta` 이벤트까지 더 긴 지연이 발생할 수 있습니다. 이것은 정상이며 모델이 멈춘 것이 아닙니다.
9. **`_azure_ad_token_provider`가 사라짐**: `AsyncOpenAI` / `OpenAI`에는 `_azure_ad_token_provider` 속성이 없습니다. 이 속성에 접근하는 테스트나 코드는 `AttributeError`를 발생시킵니다. 토큰 공급자는 `api_key`로 전달되며 클라이언트 객체에서 확인할 수 없습니다.
10. **스냅샷/골든 파일**: 테스트 스위트가 스냅샷 테스트를 사용할 경우, Chat Completions 스트리밍 형태(`choices[0]`, `content_filter_results`, `function_call` 등)를 포함하는 모든 스냅샷 파일을 새로운 Responses 형태로 업데이트해야 합니다. 이 부분을 놓치기 쉽고 스냅샷 실패 원인이 됩니다.
11. **모킹 몽키패치 경로**: 몽키패치 대상이 `openai.resources.chat.AsyncCompletions.create`에서 `openai.resources.responses.AsyncResponses.create`(또는 동기일 경우 `Responses.create`)로 변경됨. 이전 경로를 사용하면 아무 작동을 하지 않아 모킹이 인터셉트하지 못하고 실제 API 호출 또는 테스트 실패가 발생합니다.
12. **`input`이므로 `messages` 아님**: 모킹 함수는 `kwargs.get("input")`을 읽어야 하며 `kwargs.get("messages")`가 아님. Responses API는 대화 이력을 `input`으로 사용합니다.
13. **환경 변수 명명**: Azure Identity SDK는 `ManagedIdentityCredential(client_id=...)`에 `AZURE_CLIENT_ID`를 사용합니다 (`AZURE_OPENAI_CLIENT_ID`가 아님). 테스트, `.env` 파일, 앱 설정 및 Bicep/인프라에서 이름 변경 필요.
14. **`max_output_tokens` 최소값은 16**: Azure OpenAI는 16 미만 값을 `400 integer_below_min_value` 오류로 거부합니다. smoke 테스트에는 50, 프로덕션에는 1000 이상 사용. 이전 `max_tokens`에는 최소값 제한 없음.
15. **`AzureDeveloperCliCredential`용 `tenant_id`**: Azure OpenAI 리소스가 다른 테넌트에 있을 경우 `tenant_id=os.getenv("AZURE_TENANT_ID")`를 반드시 명시적으로 전달해야 합니다. 없으면 자격 증명이 잘못된 테넌트를 조용히 사용하여 `401` 오류가 납니다.
16. **스트리밍에서 속도 제한이 다르게 나타남**: Chat Completions에서는 429가 스트림 시작 자체를 차단하는 경우가 많았으나 Responses API 스트리밍에서는 429가 **스트림 중간에** 발생할 수 있으며 비동기 반복기에서 예외를 일으킵니다. 항상 스트리밍 루프를 `try/except`로 감싸고 오류 JSON 라인을 반환하여 프런트엔드가 우아하게 처리할 수 있도록 하세요.

17. **웹 앱에서는 스트리밍 오류 처리가 필수입니다**: 패턴 `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})`가 매우 중요합니다. 이 패턴 없이는 SSE/JSONL 스트림이 서버 측 오류 시 조용히 중단되고 프런트엔드는 멈춥니다.
18. **도구 정의는 평탄화된 형식을 사용해야 합니다**: Responses API는 `{"type": "function", "name": ..., "parameters": ...}`를 기대하며, Chat Completions의 중첩된 `{"type": "function", "function": {"name": ..., "parameters": ...}}` 형식은 허용하지 않습니다. 이는 함수 호출 코드에서 가장 흔한 마이그레이션 오류입니다.
19. **`pydantic_function_tool()`는 호환되지 않습니다**: `openai.pydantic_function_tool()` 헬퍼는 아직 구형 중첩 형식을 생성합니다. `responses.create()`와 함께 사용하지 마십시오. 도구 스키마를 수동으로 정의하거나 출력을 평탄화하십시오.
20. **도구 결과는 `function_call_output`을 사용하고 `role: tool`을 사용하지 마십시오**: 도구 실행 후에는 `{"type": "function_call_output", "call_id": ..., "output": ...}`를 추가해야 하며, `{"role": "tool", "tool_call_id": ..., "content": ...}`는 사용하지 않습니다. 어시스턴트의 도구 요청에는 `messages.extend(response.output)`를 사용하고, 수동으로 `{"role": "assistant", "tool_calls": [...]}` 딕셔너리를 사용하지 마십시오.
21. **`strict: true`는 `required` + `additionalProperties: false` 요구**: 도구에서 `strict: true`를 사용할 때는 모든 속성이 `required` 배열에 있어야 하며 `additionalProperties`는 `false`여야 합니다. 둘 중 하나라도 빠지면 400 오류가 발생합니다.
22. **함수 호출 ID는 특정 접두사를 가져야 합니다**: `input`에 제공하는 few-shot `function_call` 항목에서 `id` 필드는 `fc_`로 시작해야 하고 `call_id` 필드는 `call_`로 시작해야 합니다(예: `"id": "fc_example1", "call_id": "call_example1"`). 이전 Chat Completions의 `call_` 접두사를 `id`에 사용하는 것은 거부됩니다.
23. **GitHub Models는 Responses API를 지원하지 않습니다**: 앱에 GitHub Models 경로(`base_url`이 `models.github.ai` 또는 `models.inference.ai.azure.com`을 가리키는 경우)가 있다면 전부 제거하십시오. 마이그레이션 경로가 없습니다 — Azure OpenAI, OpenAI 또는 호환 가능한 로컬 엔드포인트로 전환해야 합니다.
24. **콘텐츠 필터 오류 본문 구조가 변경되었습니다**: Chat Completions 오류는 `error.body["innererror"]["content_filter_result"]` (단수)를 사용했지만, Responses API 오류는 `error.body["content_filters"][0]["content_filter_results"]` (복수, 배열 내부)를 사용합니다. `innererror` 키는 더 이상 존재하지 않습니다. `innererror`를 직접 접근하는 코드는 런타임에 `KeyError`를 발생시키므로 마이그레이션 과정에서 쉽게 놓치기 쉽습니다. 콘텐츠 필터가 실제로 작동할 때만 드러나므로 마이그레이션 시 항상 `innererror`를 grep 하십시오.
25. **원시 HTTP 호출은 URL과 본문 재작성 필요**: `/openai/deployments/{name}/chat/completions?api-version=...` 경로로 직접 Azure OpenAI REST를 호출하는 앱(`requests`, `httpx`, `aiohttp` 사용)은 `/openai/v1/responses`로 전환해야 합니다. 요청 본문은 `messages` 대신 `input`을 사용하고 `max_output_tokens`와 `store`가 필요하며, 쿼리 매개변수 `api-version`은 제거됩니다. 응답 본문 텍스트는 `output[0].content[0].text`에 있으며 — **`output_text`가 아닙니다**. `output_text`는 SDK 편의 속성으로 원시 REST JSON에는 없습니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->