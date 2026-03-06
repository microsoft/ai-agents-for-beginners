# AGENTS.md

## 프로젝트 개요

이 저장소는 "AI Agents for Beginners"라는 포괄적인 교육 과정 자료를 포함하고 있으며, AI 에이전트를 구축하는 데 필요한 모든 것을 가르칩니다. 이 과정은 기본 개념, 설계 패턴, 프레임워크 및 AI 에이전트의 프로덕션 배포를 다루는 15개 이상의 레슨으로 구성되어 있습니다.

**주요 기술:**
- Python 3.12+
- 대화형 학습을 위한 Jupyter Notebooks
- AI 프레임워크: Microsoft Agent Framework (MAF)
- Azure AI 서비스: Microsoft Foundry, Azure AI Foundry Agent Service V2

**아키텍처:**
- 레슨 기반 구조(00-15+ 디렉터리)
- 각 레슨에는 README 문서, 코드 샘플(Jupyter 노트북) 및 이미지 포함
- 자동 번역 시스템을 통한 다국어 지원
- 각 레슨당 Microsoft Agent Framework를 사용하는 Python 노트북 1개

## 설정 명령

### 전제 조건
- Python 3.12 이상
- Azure 구독(Azure AI Foundry 용)
- Azure CLI 설치 및 인증(`az login`)

### 초기 설정

1. **저장소를 클론하거나 포크하세요:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # 또는
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python 가상 환경 생성 및 활성화:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows에서: venv\Scripts\activate
   ```

3. **종속성 설치:**
   ```bash
   pip install -r requirements.txt
   ```

4. **환경 변수 설정:**
   ```bash
   cp .env.example .env
   # .env 파일을 API 키와 엔드포인트로 편집하세요
   ```

### 필수 환경 변수

**Azure AI Foundry**(필수):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry 프로젝트 엔드포인트
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - 모델 배포 이름(예: gpt-4o)

**Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search 엔드포인트
- `AZURE_SEARCH_API_KEY` - Azure AI Search API 키

인증: 노트북을 실행하기 전에 `az login`을 실행하세요(`AzureCliCredential` 사용).

## 개발 워크플로우

### Jupyter 노트북 실행

각 레슨에는 다양한 프레임워크용으로 여러 Jupyter 노트북이 포함되어 있습니다:

1. **Jupyter 시작:**
   ```bash
   jupyter notebook
   ```

2. **레슨 디렉터리로 이동** (예: `01-intro-to-ai-agents/code_samples/`)

3. **노트북 열고 실행하기:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework 사용(Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework 사용(.NET)

### Microsoft Agent Framework 사용하기

**Microsoft Agent Framework + Azure AI Foundry:**
- Azure 구독 필요
- Agent Service V2용 `AzureAIProjectAgentProvider` 사용(Foundry 포털에서 에이전트 확인 가능)
- 내장 관찰성으로 프로덕션 준비됨
- 파일 패턴: `*-python-agent-framework.ipynb`

## 테스트 지침

이 저장소는 자동화된 테스트가 포함된 프로덕션 코드가 아닌 예제 코드 중심의 교육용 저장소입니다. 설정 및 변경 사항을 검증하려면:

### 수동 테스트

1. **Python 환경 테스트:**
   ```bash
   python --version  # 3.12 이상이어야 합니다
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **노트북 실행 테스트:**
   ```bash
   # 노트북을 스크립트로 변환하고 실행(테스트 임포트)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **환경 변수 확인:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### 개별 노트북 실행

Jupyter에서 노트북을 열고 셀을 순차적으로 실행하세요. 각 노트북은 독립적으로 구성되어 있으며 다음을 포함합니다:
- 임포트 문
- 구성 로딩
- 예제 에이전트 구현
- 마크다운 셀에 포함된 예상 출력

## 코드 스타일

### Python 컨벤션

- **Python 버전**: 3.12+
- **코드 스타일**: 표준 Python PEP 8 규약 준수
- **노트북**: 개념을 설명하는 명확한 마크다운 셀 사용
- **임포트**: 표준 라이브러리, 서드파티, 로컬 임포트 순으로 그룹화

### Jupyter 노트북 규약

- 코드 셀 앞에 설명하는 마크다운 셀 포함
- 참조용으로 노트북에 출력 예시 추가
- 레슨 개념에 맞는 명확한 변수명 사용
- 노트북 실행 순서는 선형으로 유지(셀 1 → 2 → 3...)

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

이 저장소는 문서에 Markdown을 사용합니다:
- 각 레슨 폴더의 README.md 파일
- 저장소 루트의 메인 README.md
- GitHub Actions를 통한 자동 번역 시스템

### CI/CD 파이프라인

위치는 `.github/workflows/`:

1. **co-op-translator.yml** - 50개 이상의 언어로 자동 번역
2. **welcome-issue.yml** - 새 이슈 작성자 환영
3. **welcome-pr.yml** - 새 풀 리퀘스트 기여자 환영

### 배포

이 저장소는 교육용으로 배포 프로세스는 없습니다. 사용자는:
1. 저장소를 포크하거나 클론
2. 로컬 또는 GitHub Codespaces에서 노트북 실행
3. 예제를 수정하고 실험하면서 학습

## 풀 리퀘스트 가이드라인

### 제출 전

1. **변경사항 테스트:**
   - 영향을 받는 노트북을 완전히 실행
   - 모든 셀이 오류 없이 실행되는지 확인
   - 출력이 적절한지 확인

2. **문서 업데이트:**
   - 새 개념을 추가하는 경우 README.md 업데이트
   - 복잡한 코드에는 노트북에 주석 추가
   - 마크다운 셀이 목적을 설명하도록 보장

3. **파일 변경:**
   - `.env` 파일 커밋 금지(`.env.example` 사용)
   - `venv/` 또는 `__pycache__/` 디렉터리 커밋 금지
   - 개념을 보여주는 경우 노트북 출력을 유지
   - 임시 파일 및 백업 노트북(`*-backup.ipynb`) 제거

### PR 제목 형식

설명적인 제목 사용:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### 필수 검사

- 노트북이 오류 없이 실행되어야 함
- README 파일이 명확하고 정확해야 함
- 저장소의 기존 코드 패턴을 따를 것
- 다른 레슨과의 일관성 유지

## 추가 참고 사항

### 자주 발생하는 문제

1. **Python 버전 불일치:**
   - Python 3.12+ 사용 확인
   - 일부 패키지는 구버전에서 작동하지 않을 수 있음
   - 명시적으로 Python 버전을 지정하려면 `python3 -m venv` 사용

2. **환경 변수:**
   - 항상 `.env.example`에서 `.env`를 생성
   - `.env` 파일은 커밋하지 마세요(`.gitignore`에 있음)
   - GitHub 토큰은 적절한 권한 필요

3. **패키지 충돌:**
   - 새 가상 환경 사용
   - 개별 패키지보다 `requirements.txt`에서 설치
   - 일부 노트북은 마크다운 셀에 언급된 추가 패키지가 필요할 수 있음

4. **Azure 서비스:**
   - Azure AI 서비스는 활성 구독 필요
   - 일부 기능은 지역별로 제한됨
   - GitHub Models에는 무료 티어 제한 적용

### 학습 경로

권장 수강 순서:
1. **00-course-setup** - 환경 설정은 여기서 시작
2. **01-intro-to-ai-agents** - AI 에이전트 기본 개념 이해
3. **02-explore-agentic-frameworks** - 다양한 프레임워크 학습
4. **03-agentic-design-patterns** - 핵심 설계 패턴
5. 번호가 매겨진 레슨을 순차적으로 계속 진행

### 프레임워크 선택

목표에 따라 프레임워크 선택:
- **모든 레슨**: Microsoft Agent Framework (MAF) 및 `AzureAIProjectAgentProvider`
- **에이전트는 서버 측에 등록**되어 Azure AI Foundry Agent Service V2에서 확인 가능하며 Foundry 포털에 표시

### 도움 받기

- 가입: [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- 특정 안내는 레슨 README 파일 검토
- 과정 개요는 메인 [README.md](./README.md) 확인
- 자세한 설정 지침은 [Course Setup](./00-course-setup/README.md) 참조

### 기여하기

이 프로젝트는 오픈 교육용 프로젝트입니다. 기여 환영:
- 코드 예제 개선
- 오타 또는 오류 수정
- 설명 주석 추가
- 새 레슨 주제 제안
- 추가 언어로 번역

현재 필요 사항은 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) 참조.

## 프로젝트별 컨텍스트

### 다국어 지원

이 저장소는 자동 번역 시스템을 사용합니다:
- 50개 이상의 언어 지원
- 번역은 `/translations/<lang-code>/` 디렉터리에 있음
- 번역 업데이트는 GitHub Actions 워크플로우가 처리
- 소스 파일은 저장소 루트의 영어로 제공

### 레슨 구조

각 레슨은 일관된 패턴을 따릅니다:
1. 링크가 포함된 비디오 썸네일
2. 서면 레슨 콘텐츠(README.md)
3. 여러 프레임워크의 코드 샘플
4. 학습 목표 및 전제 조건
5. 링크된 추가 학습 리소스

### 코드 샘플 명명 규칙

형식: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 레슨 1, MAF Python
- `14-sequential.ipynb` - 레슨 14, MAF 고급 패턴

### 특수 디렉터리

- `translated_images/` - 번역용 로컬 이미지
- `images/` - 영어 원본 이미지
- `.devcontainer/` - VS Code 개발 컨테이너 구성
- `.github/` - GitHub Actions 워크플로우 및 템플릿

### 종속성

`requirements.txt`의 주요 패키지:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent 프로토콜 지원
- `azure-ai-inference`, `azure-ai-projects` - Azure AI 서비스
- `azure-identity` - Azure 인증(`AzureCliCredential`)
- `azure-search-documents` - Azure AI Search 통합
- `mcp[cli]` - Model Context Protocol 지원

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
면책 조항:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원문(원어) 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우 전문 번역가에 의한 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->