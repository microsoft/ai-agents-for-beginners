# 에이전트 스모크 테스트

이 폴더는 코스에서 구축하는 에이전트에 대한 <strong>스모크 테스트 카탈로그</strong>를 보관합니다.
스모크 테스트는 <strong>배포된 Microsoft Foundry 호스팅 에이전트</strong>가 접근 가능하고,
응답하며, 가장 기본적인 프롬프트 기대치를 충족하는지 빠르고 저렴하게 확인하는 절차입니다.
이것은 첫 번째 관문으로, [Lesson 10](../10-ai-agents-production/README.md)과
[Lesson 16](../16-deploying-scalable-agents/README.md)에서 배우는 전체 평가 파이프라인을 대체하지 않습니다.


이 카탈로그는 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub 액션에서 [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
워크플로우를 통해 사용됩니다.

## 실행 방법

1. Microsoft Foundry에 레슨의 에이전트를 호스팅 에이전트로 배포합니다 (배포 워크플로우는
   Lesson 16 참조). <strong>에이전트 이름</strong>과 <strong>Foundry 프로젝트 엔드포인트</strong>를 기록해 둡니다.
2. 저장소 비밀 (Settings → Secrets and variables → Actions)에 다음을 추가합니다:
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. 연합된
   ID에는 <strong>Foundry 프로젝트 범위</strong>에서 **Azure AI 사용자** 역할이 필요합니다.
3. **Actions** 탭에서 <strong>Smoke-test hosted agents</strong>를 실행하고 레슨에 맞는
   `tests_file`를 선택한 다음, 일치하는 `agent_name`와
   `project_endpoint`를 입력합니다.




| 카탈로그 | 레슨 | 배포할 에이전트 이름 |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – AI 에이전트 소개](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – 도구 사용](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – 대리적 RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – 확장 가능한 에이전트 배포](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |




<strong>에이전트를 배포하는 레슨</strong>에 적용됩니다. 개념 위주이거나 로컬에서만 실행되거나,
비결정적이고 창의적인 출력을 생성하는 레슨은 의도적으로 제외됩니다:


- **레슨 17 (로컬 AI 에이전트 만들기)**은 워크스테이션에서 Foundry Local을 사용해
  전적으로 실행되며 Foundry Responses 엔드포인트를 노출하지 않으므로
  이 액션이 적용되지 않습니다. 노트북을 로컬에서 실행하여 검증하세요.
- 디자인 패턴과 이론 레슨 (02, 03, 06, 07, 09, 12)은 배포 가능한
  에이전트를 포함하지 않아 스모크 테스트가 적용되지 않습니다.




각 카탈로그는 최상위 `tests` 배열을 가진 JSON 문서입니다. 각 항목은
하나의 프롬프트를 POST하고 응답에 대해 어설션을 수행합니다:

| 필드 | 의미 |
|-------|---------|
| `id` | 로그에 출력되는 고유한 단계 식별자입니다. |
| `description` | 사람이 읽을 수 있는 목적입니다. |
| `prompt` | 에이전트에게 전송되는 메시지입니다. |
| `assertions.status` | 예상되는 HTTP 상태(기본값 200)입니다. |
| `assertions.contains_any` | 응답에 이 하위 문자열 중 하나라도 포함되면 통과합니다. |
| `assertions.contains_all` | 응답이 모든 하위 문자열을 포함하면 통과합니다. |
| `assertions.contains_none` | 응답에 이 하위 문자열이 하나도 포함되지 않으면 통과합니다. |
| `save_response_id_as` | 나중에 다중 턴 단계에서 사용할 응답 id를 저장합니다. |
| `use_previous_response_id` | 저장된 응답 id에 연결되어 이 턴을 전송합니다. |

어설션은 대소문자를 구분하지 않는 하위 문자열 검사입니다. 자세한 내용은
[action documentation](https://github.com/marketplace/actions/ai-smoke-test)에서
Foundry가 관리하는 대화 리소스를 포함한 전체 스키마를 참조하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->