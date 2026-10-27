# AGENTS.md

## 프로젝트 개요

이 리포지토리는 "초보자를 위한 AI 에이전트"라는 포괄적인 교육 과정으로 AI 에이전트를 구축하는 데 필요한 모든 것을 가르칩니다. 이 과정은 00-18로 번호가 매겨진 18개 수업으로 구성되며, 기본 개념, 디자인 패턴, 프레임워크, 프로덕션 배포, 로컬/디바이스 에이전트, AI 에이전트의 보안을 다룹니다.

**주요 기술:**
- Python 3.12 이상
- 대화형 학습을 위한 Jupyter 노트북
- AI 프레임워크: Microsoft Agent Framework (MAF)
- Azure AI 서비스: Microsoft Foundry, Microsoft Foundry Agent Service V2

**아키텍처:**
- 수업 기반 구조 (00-18 디렉터리)
- 각 수업에는 README 문서, 코드 샘플(Jupyter 노트북), 이미지 포함
- 자동 번역 시스템을 통한 다국어 지원
- 각 수업마다 Microsoft Agent Framework를 사용하는 파이썬 노트북 1개

## 설정 명령어

### 필수 사항
- Python 3.12 이상
- Microsoft Foundry용 Azure 구독
- Azure CLI 설치 및 인증 (`az login`)

### 초기 설정

1. **리포지토리를 클론 또는 포크하세요:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **파이썬 가상 환경 생성 및 활성화:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **의존성 설치:**
   ```bash
   pip install -r requirements.txt
   ```

4. **환경 변수 설정:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### 필수 환경 변수

**Microsoft Foundry용** (필수):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry 프로젝트 엔드포인트
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - 모델 배포 이름 (예: gpt-5-mini)

**Azure AI Search용** (수업 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search 엔드포인트
- `AZURE_SEARCH_API_KEY` - Azure AI Search API 키

인증: 노트북 실행 전 `az login`를 실행하세요 (`AzureCliCredential` 사용).

## 개발 워크플로우

### Jupyter 노트북 실행

각 수업에는 다양한 프레임워크용 Jupyter 노트북이 포함되어 있습니다:

1. **Jupyter 시작:**
   ```bash
   jupyter notebook
   ```

2. **수업 디렉터리로 이동** (예: `01-intro-to-ai-agents/code_samples/`)

3. **노트북 열기 및 실행:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework 사용 (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework 사용 (.NET)

### Microsoft Agent Framework 작업

**Microsoft Agent Framework + Microsoft Foundry:**
- Azure 구독 필요
- Agent Service V2에는 `FoundryChatClient` 사용 (Foundry 포털에서 에이전트 확인 가능)
- 내장된 관찰 기능으로 프로덕션 준비 완료
- 파일 패턴: `*-python-agent-framework.ipynb`

## 테스트 지침

본 리포지토리는 교육용 예제 코드이며 자동화된 테스트가 포함된 프로덕션 코드는 아닙니다. 설정과 변경 사항을 확인하려면:

### 수동 테스트

1. **파이썬 환경 테스트:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **노트북 실행 테스트:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **환경 변수 확인:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### 개별 노트북 실행

Jupyter에서 노트북을 열고 순서대로 셀을 실행하세요. 각 노트북은 독립적이며 다음을 포함합니다:
- import 구문
- 구성 로딩
- 예제 에이전트 구현
- 마크다운 셀에 예상 출력

### 배포된 에이전트 스모크 테스트

Microsoft Foundry 호스팅 에이전트로 배포된 수업(01, 04, 05, 16)의 경우, 리포에는 `tests/`에 스모크 테스트 카탈로그가 포함되어 있으며 `.github/workflows/smoke-test.yml` 워크플로우를 통해 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) 액션으로 실행됩니다. 이는 기본 프롬프트 기대치를 따르고 있는지 확인하는 가벼운 사후 배포 게이트로, 수업 10과 16의 평가 파이프라인을 보완합니다. 카탈로그-수업-에이전트 매핑은 [tests/README.md](./tests/README.md)를 참조하세요. 수업 17은 Foundry Local로 로컬에서 실행되며 호스팅 엔드포인트가 없으므로 노트북을 직접 실행하여 검증합니다.

## 코드 스타일

### 파이썬 컨벤션

- **파이썬 버전**: 3.12 이상
- **코드 스타일**: 표준 Python PEP 8 규칙 준수
- <strong>노트북</strong>: 개념 설명을 위한 명확한 마크다운 셀 사용
- <strong>임포트</strong>: 표준 라이브러리, 써드파티, 로컬 임포트별로 그룹화

### Jupyter 노트북 컨벤션

- 코드 셀 앞에 설명적 마크다운 셀 포함
- 참고용 출력 예제 추가
- 수업 개념과 일치하는 명확한 변수명 사용
- 노트북 실행 순서는 직선적이어야 함 (셀 1 → 2 → 3…)

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

이 리포지토리는 마크다운을 문서화에 사용합니다:
- 각 수업 폴더 내 README.md 파일
- 리포지토리 루트의 메인 README.md
- GitHub 액션을 통한 자동 번역 시스템

### CI/CD 파이프라인

위치: `.github/workflows/`

1. **co-op-translator.yml** - 50개 이상의 언어로 자동 번역
2. **welcome-issue.yml** - 새 이슈 생성자 환영
3. **welcome-pr.yml** - 새 풀 리퀘스트 기여자 환영

### 배포

교육용 리포지토리로 배포 과정이 없습니다. 사용자는:
1. 리포지토리를 포크하거나 클론
2. 로컬 또는 GitHub Codespaces에서 노트북 실행
3. 예제를 수정하며 학습 및 실험

## 풀 리퀘스트 가이드라인

### 제출 전

1. **변경 사항 테스트:**
   - 영향받는 노트북 완전히 실행
   - 모든 셀 오류 없이 실행 확인
   - 출력이 적절한지 점검

2. **문서 업데이트:**
   - 새 개념 추가 시 README.md 수정
   - 복잡한 코드는 노트북에 주석 추가
   - 마크다운 셀에 목적 설명 포함

3. **파일 변경사항:**
   - `.env` 파일 커밋 금지(대신 `.env.example` 사용)
   - `venv/`나 `__pycache__/` 디렉터리 커밋 금지
   - 개념 설명에 도움이 되는 노트북 출력은 유지
   - 임시 파일 및 백업 노트북(`*-backup.ipynb`) 제거

### PR 제목 형식

설명적인 제목 사용:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### 필수 검사

- 노트북은 오류 없이 실행되어야 함
- README 파일이 명확하고 정확해야 함
- 리포지토리 내 기존 코드 패턴 준수
- 다른 수업과 일관성 유지

## 추가 참고 사항

### 흔한 문제점

1. **파이썬 버전 불일치:**
   - Python 3.12 이상 사용 권장
   - 일부 패키지는 구버전에서 작동하지 않을 수 있음
   - 명시적 버전 지정 위해 `python3 -m venv` 사용

2. **환경 변수:**
   - 항상 `.env`에서 `.env.example` 생성
   - `.env` 파일 커밋하지 말 것 (`.gitignore`에 있음)
   - 키 없는 Entra ID 인증 위해 `az login`로 로그인

3. **패키지 충돌:**
   - 새 가상 환경 사용
   - 개별 패키지보다 `requirements.txt`에서 설치 권장
   - 노트북 별로 마크다운 셀에 추가 패키지 필요성 언급

4. **Azure 서비스:**
   - 활성화된 구독 필요
   - 일부 기능은 지역별로 다름
   - Azure OpenAI 모델 배포가 Responses API를 지원하는지 확인

### 학습 경로

권장 수업 진행 순서:
1. **00-course-setup** - 환경 설정 시작
2. **01-intro-to-ai-agents** - AI 에이전트 기본 이해
3. **02-explore-agentic-frameworks** - 다양한 프레임워크 학습
4. **03-agentic-design-patterns** - 핵심 디자인 패턴
5. 번호 순서대로 수업 계속 진행

### 프레임워크 선택

목표에 따라 프레임워크 선택:
- **모든 수업**: Microsoft Agent Framework (MAF) 및 `FoundryChatClient`
- Microsoft Foundry Agent Service V2 서버 측에 에이전트 등록, Foundry 포털에서 확인 가능

### 도움 받기

- [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) 참여
- 수업별 README 파일 참고
- 주요 [README.md](./README.md)에서 과정 개요 확인
- 자세한 설정 지침은 [Course Setup](./00-course-setup/README.md) 참고

### 기여하기

열린 교육 프로젝트입니다. 기여 환영:
- 코드 예제 개선
- 오타 및 오류 수정
- 명확한 주석 추가
- 새 수업 주제 제안
- 추가 언어로 번역

현재 필요한 사항은 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) 참조.

## 프로젝트 특유 상황

### 다국어 지원

자동 번역 시스템 사용:
- 50개 이상의 언어 지원
- `/translations/<lang-code>/` 디렉터리에 번역본 포함
- GitHub Actions 워크플로우가 번역 업데이트 처리
- 소스 파일은 리포지토리 루트에서 영어로 제공

### 수업 구조

각 수업은 일관된 패턴 따름:
1. 링크가 포함된 비디오 썸네일
2. 작성된 수업 내용 (README.md)
3. 여러 프레임워크용 코드 샘플
4. 학습 목표 및 사전 요구조건
5. 추가 학습 자료 링크 포함

### 코드 샘플 명명법

형식: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 1수업, MAF 파이썬
- `14-sequential.ipynb` - 14수업, MAF 고급 패턴
- `16-python-agent-framework.ipynb` - 16수업, 프로덕션 고객지원 에이전트
- `17-local-agent-foundry-local.ipynb` - 17수업, Foundry Local + Qwen을 사용하는 로컬 에이전트

### 특수 디렉터리

- `translated_images/` - 번역용 로컬라이즈된 이미지
- `images/` - 영어 콘텐츠용 원본 이미지
- `.devcontainer/` - VS Code 개발 컨테이너 설정
- `.github/` - GitHub Actions 워크플로우 및 템플릿

### 의존성

`requirements.txt`에서 주요 패키지:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent 프로토콜 지원
- `azure-ai-inference`, `azure-ai-projects` - Azure AI 서비스
- `azure-identity` - Azure 인증 (AzureCliCredential)
- `azure-search-documents` - Azure AI Search 통합
- `mcp[cli]` - Model Context Protocol 지원

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->