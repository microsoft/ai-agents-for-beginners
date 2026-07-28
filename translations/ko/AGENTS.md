# AGENTS.md

## 프로젝트 개요

이 저장소에는 "초보자를 위한 AI 에이전트"가 포함되어 있으며, AI 에이전트를 구축하는 데 필요한 모든 내용을 가르치는 종합 교육 과정입니다. 이 과정은 기본 개념, 설계 패턴, 프레임워크, 프로덕션 배포, 로컬/디바이스 에이전트, AI 에이전트의 보안을 다루는 18개의 레슨(00~18번)으로 구성되어 있습니다.

**주요 기술:**
- Python 3.12+
- 상호작용 학습을 위한 Jupyter 노트북
- AI 프레임워크: Microsoft Agent Framework (MAF)
- Azure AI 서비스: Microsoft Foundry, Microsoft Foundry Agent Service V2

**아키텍처:**
- 레슨 기반 구조 (00~15+ 디렉터리)
- 각 레슨은 README 문서, 코드 샘플(Jupyter 노트북), 이미지 포함
- 자동 번역 시스템을 통한 다국어 지원
- Microsoft Agent Framework를 사용하는 각 레슨당 하나의 Python 노트북

## 설정 명령어

### 사전 요구 사항
- Python 3.12 이상
- Azure 구독 (Microsoft Foundry용)
- Azure CLI 설치 및 인증 (`az login`)

### 초기 설정

1. **저장소 복제 또는 포크:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # 또는
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python 가상환경 생성 및 활성화:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows에서: venv\Scripts\activate
   ```

3. **의존성 설치:**
   ```bash
   pip install -r requirements.txt
   ```

4. **환경 변수 설정:**
   ```bash
   cp .env.example .env
   # API 키와 엔드포인트를 포함하여 .env 파일을 수정하세요
   ```

### 필수 환경 변수

<strong>Microsoft Foundry</strong>용 (필수):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry 프로젝트 엔드포인트
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - 모델 배포 이름 (예: gpt-5-mini)

<strong>Azure AI Search</strong>용 (레슨 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search 엔드포인트
- `AZURE_SEARCH_API_KEY` - Azure AI Search API 키

인증: 노트북 실행 전 `az login` 명령어 실행 (AzureCliCredential 사용).

## 개발 워크플로우

### Jupyter 노트북 실행

각 레슨에는 여러 프레임워크용 Jupyter 노트북이 포함되어 있습니다:

1. **Jupyter 시작:**
   ```bash
   jupyter notebook
   ```

2. **레슨 디렉터리로 이동** (예: `01-intro-to-ai-agents/code_samples/`)

3. **노트북 열고 실행:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework 사용 (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework 사용 (.NET)

### Microsoft Agent Framework 사용

**Microsoft Agent Framework + Microsoft Foundry:**
- Azure 구독 필요
- Agent Service V2용 `FoundryChatClient` 사용 (에이전트가 Foundry 포털에 표시됨)
- 내장된 관찰 가능성 포함 프로덕션 준비 완료
- 파일 패턴: `*-python-agent-framework.ipynb`

## 테스트 지침

이 저장소는 자동 테스트가 포함된 프로덕션 코드는 아니며 교육용 예제 코드 저장소입니다. 설정과 변경 사항을 확인하려면:

### 수동 테스트

1. **Python 환경 테스트:**
   ```bash
   python --version  # 3.12 이상이어야 합니다
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **노트북 실행 테스트:**
   ```bash
   # 노트북을 스크립트로 변환하고 실행 (테스트용 임포트)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **환경 변수 확인:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### 개별 노트북 실행

Jupyter에서 노트북을 열고 셀을 순서대로 실행하세요. 각 노트북은 독립적이며 포함합니다:
- 임포트 구문
- 설정 로딩
- 예제 에이전트 구현
- 마크다운 셀에 예상 출력

### 배포된 에이전트 스모크 테스트

Microsoft Foundry 호스팅 에이전트로 배포된 레슨들(01, 04, 05, 16)의 경우, 리포지터리 내 `tests/`에 스모크 테스트 카탈로그가 포함되어 있으며, `.github/workflows/smoke-test.yml` 워크플로우가 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) 액션을 사용해 실행됩니다. 이는 배포 후 간단한 게이트(에이전트 접속 가능 여부와 기본 프롬프트 준수 여부)를 확인하며, 레슨 10과 16의 평가 파이프라인을 보완합니다. 카탈로그와 레슨, 에이전트 매핑은 [tests/README.md](./tests/README.md) 참조. 레슨 17은 Foundry Local에서 로컬로 실행되며 호스팅 엔드포인트가 없어 노트북 직접 실행으로 검증됩니다.

## 코드 스타일

### Python 규칙

- **Python 버전**: 3.12+
- **코드 스타일**: 표준 Python PEP 8 규칙 준수
- <strong>노트북</strong>: 개념 설명을 위한 명확한 마크다운 셀 사용
- <strong>임포트</strong>: 표준 라이브러리, 서드파티, 로컬 임포트 순으로 그룹화

### Jupyter 노트북 규칙

- 코드 셀 전 설명을 담은 마크다운 셀 포함
- 참조용 출력 예제 추가
- 레슨 개념에 맞는 명확한 변수명 사용
- 노트북 실행 순서 선형 유지 (셀 1 → 2 → 3...)

### 파일 구성

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## 빌드 및 배포

### 문서 빌드

이 저장소는 문서화를 위해 Markdown 사용:
- 각 레슨 폴더의 README.md 파일
- 저장소 루트에 메인 README.md
- GitHub Actions를 통한 자동 번역 시스템

### CI/CD 파이프라인

위치: `.github/workflows/`

1. **co-op-translator.yml** - 50개 이상 언어로 자동 번역
2. **welcome-issue.yml** - 새 이슈 작성자 환영
3. **welcome-pr.yml** - 새 풀 리퀘스트 기여자 환영

### 배포

이 저장소는 교육용이므로 별도 배포 과정 없음. 사용자는:
1. 저장소를 포크하거나 복제
2. 노트북을 로컬 또는 GitHub Codespaces에서 실행
3. 예제 수정 및 실험을 통해 학습

## 풀 리퀘스트 가이드라인

### 제출 전 확인 사항

1. **변경 사항 테스트:**
   - 영향을 받은 노트북을 완전히 실행
   - 모든 셀이 오류 없이 실행되는지 확인
   - 출력 결과가 적절한지 검증

2. **문서 업데이트:**
   - 새로운 개념 추가 시 README.md 업데이트
   - 복잡한 코드에는 노트북 내 주석 추가
   - 마크다운 셀이 목적을 명확히 설명하는지 확인

3. **파일 변경:**
   - `.env` 파일은 커밋하지 말 것 (`.env.example` 사용)
   - `venv/`나 `__pycache__/` 디렉터리 커밋 금지
   - 개념 시연 시 노트북 출력 유지
   - 임시 파일 및 백업 노트북(`*-backup.ipynb`) 삭제

### PR 제목 형식

설명적인 제목 사용:
- `[Lesson-XX] <개념>에 대한 새 예제 추가`
- `[Fix] lesson-XX README의 오타 수정`
- `[Update] lesson-XX 코드 샘플 개선`
- `[Docs] 설정 지침 업데이트`

### 필수 확인 사항

- 노트북은 오류 없이 실행되어야 함
- README 파일은 명확하고 정확해야 함
- 저장소 내 기존 코드 패턴 준수
- 다른 레슨과 일관성 유지

## 추가 참고사항

### 흔한 문제

1. **Python 버전 불일치:**
   - Python 3.12 이상 사용 보장
   - 일부 패키지는 구버전에서 작동하지 않을 수 있음
   - Python 버전을 명시적으로 지정하려면 `python3 -m venv` 사용

2. **환경 변수:**
   - 항상 `.env.example`에서 `.env` 생성
   - `.env` 파일은 커밋 금지 (`.gitignore`에 포함)
   - 무키 Entra ID 인증을 위해 `az login` 실행

3. **패키지 충돌:**
   - 새로운 가상환경 사용 권장
   - 개별 패키지보다 `requirements.txt`에서 설치
   - 일부 노트북은 마크다운 셀에 명시된 추가 패키지 필요할 수 있음

4. **Azure 서비스:**
   - Azure AI 서비스는 활성 구독 필요
   - 일부 기능은 지역별로 다름
   - Azure OpenAI 모델 배포가 Responses API 지원하는지 확인

### 학습 경로

권장 학습 순서:
1. **00-course-setup** - 환경 설정 시작 지점
2. **01-intro-to-ai-agents** - AI 에이전트 기초 이해
3. **02-explore-agentic-frameworks** - 다양한 프레임워크 학습
4. **03-agentic-design-patterns** - 주요 설계 패턴 학습
5. 번호 순으로 레슨 순차 진행

### 프레임워크 선택

목표에 따라 프레임워크 선택:
- **모든 레슨**: Microsoft Agent Framework (MAF) 및 `FoundryChatClient` 사용
- **에이전트는 서버 측에서 Microsoft Foundry Agent Service V2에 등록되며 Foundry 포털에 표시됨**

### 도움 받기

- [Microsoft Foundry 커뮤니티 Discord](https://aka.ms/ai-agents/discord) 참여
- 각 레슨 README 파일에서 구체적 안내 확인
- 메인 [README.md](./README.md)에서 과정 개요 확인
- 상세 설정 지침은 [Course Setup](./00-course-setup/README.md) 참조

### 기여

이 프로젝트는 개방형 교육 프로젝트입니다. 기여 환영:
- 코드 예제 개선
- 오타 및 오류 수정
- 명확한 주석 추가
- 새로운 레슨 주제 제안
- 추가 언어 번역

현재 필요 사항은 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) 참조.

## 프로젝트 특화 문맥

### 다국어 지원

이 저장소는 자동 번역 시스템 사용:
- 50개 이상 언어 지원
- `/translations/<lang-code>/` 디렉터리에서 번역본 제공
- GitHub Actions 워크플로우가 번역 업데이트 관리
- 원본 파일은 저장소 루트에 영어로 존재

### 레슨 구성

각 레슨은 일관된 구성:
1. 비디오 썸네일 및 링크
2. 서면 레슨 내용 (README.md)
3. 다양한 프레임워크별 코드 샘플
4. 학습 목표 및 사전 조건
5. 추가 학습 자료 링크

### 코드 샘플 명명법

형식: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 레슨 1, MAF Python
- `14-sequential.ipynb` - 레슨 14, MAF 고급 패턴
- `16-python-agent-framework.ipynb` - 레슨 16, 프로덕션 고객 지원 에이전트
- `17-local-agent-foundry-local.ipynb` - 레슨 17, Foundry Local + Qwen 로컬 에이전트

### 특수 디렉터리

- `translated_images/` - 번역용 현지화 이미지
- `images/` - 영어 콘텐츠 원본 이미지
- `.devcontainer/` - VS Code 개발 컨테이너 구성
- `.github/` - GitHub Actions 워크플로우 및 템플릿

### 의존성

`requirements.txt` 주요 패키지:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent 프로토콜 지원
- `azure-ai-inference`, `azure-ai-projects` - Azure AI 서비스
- `azure-identity` - Azure 인증 (AzureCliCredential)
- `azure-search-documents` - Azure AI Search 통합
- `mcp[cli]` - 모델 컨텍스트 프로토콜 지원

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->