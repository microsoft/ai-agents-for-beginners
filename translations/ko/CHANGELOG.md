# 변경 로그

**AI Agents for Beginners** 코스에 대한 모든 주목할 만한 변경 사항은 이 파일에 문서화되어 있습니다.

## [출시됨] — 2026-07-14

이번 릴리스는 코스를 두 개의 새로 더 이상 지원되지 않는 모델에서 마이그레이션하고, 나머지 Lesson 노트북을 안정적인 Microsoft Agent Framework API로 이전했으며, Python 노트북을 라이브 Microsoft Foundry 배포본에 대해 검증합니다.

### 변경됨

- **지원 중단된 모델에서 이동 (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** `gpt-4.1`과 `gpt-4.1-mini` 모델은 이제 더 이상 지원되지 않습니다(공개 은퇴일 **2026년 10월 14일**). 모든 코스 참조(문서, `.env.example`, Python/.NET 노트북 및 샘플)에서 지원되지 않는 모델을 `gpt-5-mini`로 교체했습니다. Lesson 16의 모델 라우팅 예제는 `gpt-5-nano`(작은 모델)와 `gpt-5-mini`(큰 모델)를 사용해 크기 대비를 유지합니다. 서드파티 파일([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), 이전 GitHub Models 텍스트, `azure-openai-to-responses` 스킬의 역량 노트는 의도적으로 변경하지 않았습니다.
- **Lesson 14 핸드오프 노트북을 안정적인 API로 마이그레이션.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb)는 이제 제거된 pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` 기호를 대체하여 `agent_framework.orchestrations.HandoffBuilder`와 `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type` 기반 스트리밍, `FoundryChatClient`를 사용합니다.
- **Lesson 14 인간 개입 노트북을 안정적인 API로 마이그레이션.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb)는 제거된 `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`를 대체하여 `ctx.request_info(...)` + `@response_handler`로 일시 중지하며, `WorkflowBuilder(start_executor=..., output_executors=[...])`로 빌드하고, `default_options={"response_format": ...}`를 통해 구조화된 출력을 구동하며, 스크립트 답변을 사용해 노트북이 무인 실행됩니다(차단 입력 `input()` 없음).
- **환경 구성** ([.env.example](../../.env.example)) : 모델 배포 이름을 `gpt-5-mini`로 변경; `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL`(Lesson 16 라우팅) 및 이전에 누락된 `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`(Lesson 15 브라우저 사용) 추가.
- <strong>종속성</strong> ([requirements.txt](../../requirements.txt)) : `agent-framework`, `agent-framework-foundry`, `agent-framework-openai`를 `~=1.10.0` 버전으로 고정하여 자기 일관되고 검증된 세트 유지 (1.11.0은 이들 레슨에서 사용하는 인터페이스에 실험적 파괴적 변경을 포함).

### 참고 및 알려진 제한 사항

- **라이브 Microsoft Foundry에서 검증됨.** Python 노트북들은 `nbconvert`로 헤드리스 실행되어 Microsoft Foundry 프로젝트에서 `gpt-5-mini`(및 Lesson 16 라우팅용 `gpt-5-nano`)를 사용해 검증되었습니다. 자신의 프로젝트에서 이와 동등한 더 이상 지원되지 않는 모델들을 배포하세요; 노트북은 `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`에서 배포 이름을 읽어들입니다.
- **일부 레슨은 추가 리소스 필요.** Lesson 05는 Azure AI Search가 필요; Lesson 08 Bing-grounding 워크플로우 (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`)는 Bing 연결과 Microsoft Foundry Agent Service 호스팅 도구가 필요; Lesson 13 (Cognee) 및 Lesson 17 (Foundry Local)은 자체 런타임이 필요합니다.

## [출시됨] — 2026-07-13

이번 릴리스는 배포 아크를 완성하는 두 개의 새로운 레슨 — Microsoft Foundry로 에이전트 확장과 단일 워크스테이션 축소 — 으로 구성되며, 스모크 테스트 파이프라인, 새로 고친 코스 내비게이션, 새로운 학습자 능력 및 업데이트된 브랜딩을 포함합니다.

### 추가됨

- **Lesson 16 — Microsoft Foundry로 확장 가능한 에이전트 배포.** 새로운 레슨 [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) 및 실행 가능한 노트북 [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb)는 생산용 고객 지원 에이전트를 구축합니다(도구, RAG, 메모리, 모델 라우팅, 응답 캐싱, 인간 승인, 평가 게이트, OpenTelemetry 추적 포함), 개발/배포/런타임 Mermaid 다이어그램, 지식 점검, 과제, 도전과제 포함.
- **Lesson 17 — Foundry Local과 Qwen으로 로컬 AI 에이전트 생성.** 새로운 레슨 [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) 및 노트북 [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb)는 완전 온-디바이스 엔지니어링 어시스턴트를 구축합니다(Qwen 함수 호출 via Foundry Local, 샌드박스 파일 도구, 로컬 RAG with Chroma, 선택적 로컬 MCP 포함), 로컬 전용 / 로컬 RAG / 도구 호출 다이어그램, 지식 점검, 과제, 도전 과제 포함.
- **스모크 테스트 파이프라인.** 새로운 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) 워크플로우 [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml)과 Lessons 01, 04, 05, 16에 배포 가능한 에이전트용 레슨별 카탈로그가 [tests/](./tests/README.md)에 추가되었으며, 각 카탈로그가 해당 레슨 및 호스팅 에이전트 이름과 매핑되는 인덱스 README를 포함합니다. Lesson 16는 "스모크 테스트를 통한 배포된 에이전트 검증" 섹션이 추가되었고, Lessons 01/04/05는 선택적 스모크 테스트 포인터가 추가되었습니다.
- **학습자 능력.** `.agents/skills/`에 새로운 Agent Skills 추가: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (Lesson 16, 17 가이드 팩), [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (라이브 Microsoft Foundry / Azure OpenAI 설정과 노트북 샘플 검증 방법).
- **노트북 검증 실행기.** 모든 Python 노트북을 `nbconvert`로 헤드리스 실행하고 PASS/FAIL 매트릭스(및 `results.json`)를 출력하는 새로운 [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1). 자동으로 리포지토리 루트 및 Python을 감지하고, 기본적으로 코스 외 노트북(`.venv`, `site-packages`, `translations`, 스킬 템플릿 자산) 및 `.NET` 노트북을 제외하며, `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, `-Python` 옵션을 지원합니다.
- **코스 내비게이션.** 이전/다음 레슨 링크를 Lessons 11–15에 추가하여 전체 코스가 양방향으로 00 → 18까지 체인으로 연결됨(기존에 누락됨).
- **새 섬네일.** Lessons 16 및 17의 레슨 썸네일과 료포지터리 소셜 이미지 [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) 갱신됨 (새 레슨 2개와 `aka.ms/ai-agents-beginners` URL 홍보).
- <strong>종속성</strong> ([requirements.txt](../../requirements.txt)) : Lesson 17을 위한 `foundry-local-sdk` 및 `chromadb` 추가.

### 변경됨

- **메인 [README.md](./README.md)** 레슨 테이블: Lessons 16 및 17이 이제 콘텐츠로 링크됨(이전에는 "곧 공개 예정"); 리포지터리 이미지가 `repo-thumbnailv3.png`로 업데이트됨.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)** : 레슨 바이 레슨 가이드와 학습 경로에 Lessons 16 및 17 추가; "스모크 테스트로 배포된 에이전트 검증" 섹션 추가.
- **[AGENTS.md](./AGENTS.md)** : 레슨 개수/설명 업데이트(00–18), 스모크 테스트 검증 섹션 추가, Lesson 16/17 샘플 네이밍 예제 추가.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)** : "이전 레슨"이 Lesson 17(이전에는 Lesson 15)를 가리켜 체인 완성.
- **지원 중단되지 않은 모델에 대한 표준화된 모델 참조.** 코스 전체(문서, `.env.example`, Python/.NET 노트북 및 샘플)에 걸쳐 모든 `gpt-4o` / `gpt-4o-mini` 참조를 `gpt-4.1-mini`로 교체 — `gpt-4o`(모든 버전)는 2026년에 은퇴 예정. Lesson 16 모델 라우팅 예제는 `gpt-4.1-mini`(작은 모델)와 `gpt-4.1`(큰 모델)로 크기 대비 유지. Python 노트북은 이제 하드코딩된 모델명을 사용하지 않고 환경 변수(`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`)에서 모델을 선택함.

### 참고 및 알려진 제한 사항

- **라이브 Azure에서 실행되지 않음.** 새 레슨 노트북들은 교육용 샘플임; 자체 Microsoft Foundry / Foundry Local 설정에서 실행하고 검증해야 함. 스모크 테스트 워크플로우는 레슨 에이전트를 배포하고 Azure OIDC 비밀(`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`)을 Foundry 프로젝트 범위에서 **Azure AI User** 역할로 설정해야 함.
- **Lesson 17은 로컬 전용.** Foundry Responses 엔드포인트가 없어 스모크 테스트 액션이 적용되지 않음; 워크스테이션에서 노트북을 실행하여 검증해야 함.

## [출시됨] — 2026-07-06

이번 릴리스는 코스를 <strong>Azure OpenAI Responses API</strong>로 이전하고, 제품 명칭을 **Microsoft Foundry** 및 <strong>Microsoft Agent Framework (MAF)</strong>로 표준화하며, GitHub Models를 폐지하고, SDK 버전을 업데이트하며, 로컬 모델 및 Foundry에서 다른 프레임워크 호스팅에 관한 새 내용을 추가합니다.

### 추가됨

- **마이그레이션 스킬** — `.agents/skills/`에 [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill 설치 (출처: [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) 및 해당 참조와 스캐너 스크립트 포함.
- **Foundry Local (모델 온-디바이스 실행)** — [00-course-setup/README.md](./00-course-setup/README.md)에 새로운 "대안 공급자: Foundry Local" 섹션 추가, 설치(`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, Microsoft Agent Framework와 `OpenAIChatClient`로 `FoundryLocalManager` 연결 설명.
- **Microsoft Foundry에서 LangChain / LangGraph 에이전트 호스팅** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md)에 새 섹션과 실행 가능한 샘플 [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) 추가, `langchain-azure-ai[hosting]` 및 `ResponsesHostServer`(`/responses` 프로토콜) 사용, [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) 기반.
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md)에 새로운 "실제 사례: Microsoft Project Opal" 섹션 추가, Opal을 기업용 컴퓨터 사용 에이전트로 프레이밍하고 코스 개념(인간 개입, 신뢰/보안, 계획, 스킬)과 매핑.
- **두 번째 Lesson 02 Python 샘플** — 이전 Semantic Kernel 노트북에서 마이그레이션된 [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) 추가; 레슨 README에 링크 포함.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)에 모델 및 공급자 섹션 추가.**

### 변경됨

- **Chat Completions → Responses API (Python).** 모델을 직접 호출하던 샘플들이 Chat Completions에서 Responses API(`client.responses.create(input=..., store=False)`, `resp.output_text`)로 마이그레이션되었으며, 안정적인 Azure OpenAI `/openai/v1/` 엔드포인트(`api_version` 없음)에 `OpenAI` 클라이언트를 사용합니다. 영향을 받은 샘플은 다음과 같습니다:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — 전체 함수 호출 워크스루(도구 스키마를 Responses 형식으로 평탄화, 도구 결과를 `function_call_output`, `max_output_tokens` 등으로 반환).

- **GitHub Models → Azure OpenAI.** GitHub Models는 더 이상 사용되지 않으며(2026년 7월 종료 예정) Responses API를 지원하지 않습니다. 모든 GitHub Models 코드 경로는 Python 및 .NET 샘플에서 Azure OpenAI / Microsoft Foundry로 전환되었습니다:
  - Python: Lesson 08 워크플로우 노트북(`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + 동반 `.md` 문서, 그리고 Lesson 08 dotNET 워크플로우 노트북/`.md` (`01`–`03`)는 이제 `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)`와 `AzureCliCredential`을 사용합니다.
- **Semantic Kernel → Microsoft Agent Framework.** 이전의 `02-semantic-kernel.ipynb`는 Azure OpenAI(Responses API)와 Microsoft Agent Framework를 사용하도록 다시 작성되었으며, `02-python-agent-framework-azure-openai.ipynb`로 이름이 변경되었습니다.
- **`FoundryChatClient` + `as_agent` 표준화.** `AzureAIProjectAgentProvider`를 참조했던 README 및 노트북 코드는 Lesson 01 및 프레임워크 자체 샘플에서 사용하는 표준 패턴 `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())`와 `provider.as_agent(...)`를 사용하도록 통일되었습니다. Lesson 02–14 README 및 노트북(예: Lesson 13 메모리, 모든 Lesson 14 노트북, `11-agentic-protocols/code_samples/github-mcp/app.py`)에 걸쳐 업데이트되었습니다.
- **제품 명칭 변경.** 영어 콘텐츠 전반에 걸쳐 다음과 같이 이름이 변경되었습니다:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (변경 없음: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", 그리고 환경 변수 이름)
- <strong>종속성</strong> ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`로 고정
  - Responses API를 위한 최소 버전인 `openai>=1.108.1`로 고정
  - `azure-ai-inference` 제거 (기존에 GitHub Models 샘플에만 사용됨)
- **환경 설정** ([.env.example](../../.env.example)): GitHub Models 변수(`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`)를 제거하고, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` 및 선택 사항인 `AZURE_OPENAI_API_KEY`를 추가; 이름을 Microsoft Foundry에 맞게 업데이트
- <strong>문서</strong> — 위 변경사항에 맞춰 [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), [STUDY_GUIDE.md](./STUDY_GUIDE.md) 업데이트 (환경 변수 설정, 확인 스니펫, 프로바이더 안내, 명칭 변경 등)

### 제거됨

- GitHub Models 온보딩 단계 및 환경 변수 (Azure OpenAI / Microsoft Foundry로 대체됨)

### 보안 / 개인정보 보호(공개 공유 정리)

- 실제 **Azure 구독 ID**, 리소스 그룹/리소스 이름, Bing 연결 ID, 개발자 <strong>로컬 파일 경로 및 사용자 이름</strong>이 노출된 주피터 노트북 실행 결과 삭제:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- API 키, 토큰, 구독 ID 또는 개인 경로가 영어 콘텐츠 트래킹 내에 남아있지 않음을 확인했습니다(`GITHUB_TOKEN` 참조는 워크플로우 내 GitHub Actions 토큰과 Lesson 11 설정의 GitHub MCP 서버 PAT로, 모두 합법적이며 GitHub Models와 관련 없음).

### 참고 및 알려진 제한 사항

- **실행/컴파일되지 않음.** 이 샘플들은 API 및 명칭 정확성을 위해 교육 목적으로 업데이트되었으며, 라이브 Azure 리소스에서 실행되지 않았고 .NET 샘플은 이 환경에서 컴파일되지 않았습니다. 자체 Microsoft Foundry / Azure OpenAI 배포에서 검증하세요.
- **모델 배포는 Responses API를 지원해야 합니다.** `gpt-4.1-mini`, `gpt-4.1` 또는 `gpt-5.x` 모델과 같은 배포를 사용하세요. 이전 모델은 기본 Responses 기능을 지원하지만 모든 기능을 지원하지는 않습니다.
- **Agent-framework 버전.** 샘플은 최신 MAF(`>=1.10.0`)를 대상으로 합니다. 표준 에이전트 생성 호출은 `client.as_agent(...)`이며, API는 프레임워크 문서 및 설치 빌드와 비교해 검증되었습니다. 다른 버전을 고정한다면 메서드 사용 가능 여부(`as_agent` vs `create_agent`)를 확인하세요.
- <strong>Lesson 08 워크플로우 노트북 04</strong>는 Microsoft Foundry Agent Service 호스팅 도구(빙 접지, 코드 인터프리터)를 사용하므로 일부러 `AzureAIAgentClient`(`agent-framework-azure-ai`에서)를 유지하며, 이미 Responses 기반입니다.
- **.NET 기본 배포.** 두 개의 Lesson 08 dotNET 워크플로우 샘플은 이전에 특정 모델을 하드코딩했지만, 이제 기본값은 `AZURE_OPENAI_DEPLOYMENT`(`gpt-4.1-mini`)입니다. 샘플이 멀티모달/비전 입력을 사용하는 경우 적합한 모델로 `AZURE_OPENAI_DEPLOYMENT`를 설정하세요.
- <strong>Foundry Local</strong>은 OpenAI 호환 **Chat Completions** 엔드포인트를 노출하며 로컬 개발용입니다; 전체 Responses API 기능 세트는 Azure OpenAI / Microsoft Foundry를 사용하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->