# 테스트 인프라 마이그레이션

코드베이스를 Chat Completions에서 Responses API로 마이그레이션할 때, **테스트가 예측 가능한 방식으로 깨집니다**. 이 참조 문서는 수정할 내용을 다룹니다.

---

## 스트리밍 응답 모킹 (Python pytest)

### 핵심 모크 클래스

```python
class MockResponseEvent:
    """Simulates a Responses API streaming event."""
    def __init__(self, event_type: str, delta: str | None = None):
        self.type = event_type
        self.delta = delta

class AsyncResponseIterator:
    """Async iterator that yields Responses API streaming events from a string answer."""
    def __init__(self, answer: str):
        self.event_index = 0
        self.events = []
        for i, word in enumerate(answer.split(" ")):
            # 공백 유지: 첫 번째 단어를 제외한 모든 단어 앞에 공백 추가
            if i > 0:
                word = " " + word
            self.events.append(MockResponseEvent("response.output_text.delta", delta=word))
        self.events.append(MockResponseEvent("response.completed"))

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.event_index < len(self.events):
            event = self.events[self.event_index]
            self.event_index += 1
            return event
        raise StopAsyncIteration
```

### 메시지 내용에 따른 모크 응답 라우팅

실제 애플리케이션은 프롬프트에 따라 다른 응답을 제공합니다. `messages`가 아닌 `input`으로 라우팅하세요:

```python
async def mock_acreate(*args, **kwargs):
    # Responses API는 'messages'가 아닌 'input'을 사용합니다
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### 몽키패치 경로

| 클라이언트 유형 | 몽키패치 경로 |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (동기) | `openai.resources.responses.Responses.create` |

> <strong>이전</strong> (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> <strong>이후</strong> (Responses): `openai.resources.responses.AsyncResponses.create`

### 전체 픽스쳐 예제

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... 여기 MockResponseEvent와 AsyncResponseIterator 클래스 ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. 모크 픽스쳐 업데이트

`ChatCompletionChunk` 기반 모크를 위의 `MockResponseEvent` / `AsyncResponseIterator` 패턴으로 교체하세요. 주요 변경사항:

| 이전 (Chat Completions 모크) | 이후 (Responses 모크) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| 청크 내 `finish_reason="stop"` | `event.type == "response.completed"` |
| Azure 전용 `prompt_filter_results` 청크 | 완전히 제거 |
| 선택 항목별 Azure 전용 `content_filter_results` | 완전히 제거 |
| 모크 내 `kwargs.get("messages")` | 모크 내 `kwargs.get("input")` |

---

## 2. 스냅샷 / 골든 파일 업데이트

테스트 스위트가 스냅샷 테스트를 사용하는 경우(예: `pytest-snapshot`, syrupy 또는 직접 만든 JSONL 스냅샷), 예상 출력 형식이 변경됩니다:

<strong>이전</strong> (Chat Completions 스트리밍 JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

<strong>이후</strong> (Responses API 스트리밍 JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

새로운 형식은 훨씬 단순합니다 — `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` 또는 `content_filter_results` 필드는 없습니다. 모든 스냅샷 파일을 업데이트하거나 재생성하세요.

> <strong>팁</strong>: 마이그레이션 후 `--snapshot-update` (pytest-snapshot) 또는 `--update-snapshots` (syrupy) 옵션으로 테스트를 실행하여 자동으로 재생성하세요.

---

## 3. 테스트 어설션 업데이트

일반적인 어설션 실패 사례:

| 이전 어설션 | 문제점 | 새로운 어설션 |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI`에 `_azure_ad_token_provider` 속성 없음 | `isinstance(client, AsyncOpenAI)` 및 `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI`에 `api_version` 없음 | 완전히 제거 |
| `isinstance(client, AsyncAzureOpenAI)` | 클라이언트 유형 변경됨 | `isinstance(client, AsyncOpenAI)` |

---

## 4. 테스트 픽스쳐 내 환경 변수 업데이트

테스트는 종종 `monkeypatch.setenv`로 환경 변수를 설정합니다. 다음과 같이 업데이트하세요:

| 이전 환경 변수 | 새로운 환경 변수 | 비고 |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | 표준 Azure Identity SDK 관례 |
| `AZURE_OPENAI_VERSION` | 제거 | 더 이상 `api_version` 불필요 |
| `AZURE_OPENAI_API_VERSION` | 제거 | 더 이상 `api_version` 불필요 |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | 유지 (`base_url`에 여전히 필요) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | 유지 (`model` 파라미터의 배포 이름) |

---

## 5. 마이그레이션이 필요한 테스트 코드 검색

```bash
# 테스트 전용 레거시 패턴
rg "ChatCompletionChunk" tests/
rg "AsyncCompletions\.create" tests/
rg "chat\.completions" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results" tests/
rg "content_filter_results" tests/
rg "AZURE_OPENAI_VERSION|AZURE_OPENAI_API_VERSION" tests/
rg "AZURE_OPENAI_CLIENT_ID" tests/
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->