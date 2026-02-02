# AGENTS.md

## 프로젝트 개요

이 저장소는 "초보자를 위한 AI 에이전트"라는 교육 과정을 포함하고 있으며, AI 에이전트를 구축하는 데 필요한 모든 것을 가르칩니다. 이 과정은 AI 에이전트의 기본 개념, 디자인 패턴, 프레임워크, 그리고 실제 배포까지 다루는 15개 이상의 강의로 구성되어 있습니다.

**주요 기술:**
- Python 3.12 이상
- Jupyter Notebooks를 활용한 대화형 학습
- AI 프레임워크: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI 서비스: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (무료 등급 제공)

**아키텍처:**
- 강의 기반 구조 (00-15+ 디렉토리)
- 각 강의는 README 문서, 코드 샘플(Jupyter 노트북), 이미지로 구성
- 자동 번역 시스템을 통한 다국어 지원
- 강의별로 다양한 프레임워크 옵션 제공 (Semantic Kernel, AutoGen, Azure AI Agent Service)

## 설정 명령어

### 사전 요구사항
- Python 3.12 이상
- GitHub 계정 (GitHub Models - 무료 등급)
- Azure 구독 (선택 사항, Azure AI 서비스용)

### 초기 설정

1. **저장소를 클론하거나 포크하세요:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python 가상 환경을 생성하고 활성화하세요:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **필요한 종속성을 설치하세요:**
   ```bash
   pip install -r requirements.txt
   ```

4. **환경 변수를 설정하세요:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### 필수 환경 변수

**GitHub Models (무료)**:
- `GITHUB_TOKEN` - GitHub에서 발급받은 개인 액세스 토큰

**Azure AI 서비스** (선택 사항):
- `PROJECT_ENDPOINT` - Azure AI Foundry 프로젝트 엔드포인트
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API 키
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI 엔드포인트 URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - 채팅 모델 배포 이름
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - 임베딩 배포 이름
- `.env.example`에 표시된 추가 Azure 구성

## 개발 워크플로우

### Jupyter 노트북 실행

각 강의는 다양한 프레임워크를 위한 여러 Jupyter 노트북을 포함합니다:

1. **Jupyter 시작:**
   ```bash
   jupyter notebook
   ```

2. **강의 디렉토리로 이동** (예: `01-intro-to-ai-agents/code_samples/`)

3. **노트북 열고 실행:**
   - `*-semantic-kernel.ipynb` - Semantic Kernel 프레임워크 사용
   - `*-autogen.ipynb` - AutoGen 프레임워크 사용
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python) 사용
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET) 사용
   - `*-azureaiagent.ipynb` - Azure AI Agent Service 사용

### 다양한 프레임워크 활용

**Semantic Kernel + GitHub Models:**
- GitHub 계정으로 무료 등급 사용 가능
- 학습 및 실험에 적합
- 파일 패턴: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- GitHub 계정으로 무료 등급 사용 가능
- 다중 에이전트 오케스트레이션 기능 제공
- 파일 패턴: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Microsoft의 최신 프레임워크
- Python 및 .NET에서 사용 가능
- 파일 패턴: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Azure 구독 필요
- 실제 배포에 적합한 기능 제공
- 파일 패턴: `*-azureaiagent.ipynb`

## 테스트 지침

이 저장소는 교육용 예제 코드로 구성되어 있으며, 자동화된 테스트가 포함된 프로덕션 코드가 아닙니다. 설정 및 변경 사항을 확인하려면:

### 수동 테스트

1. **Python 환경 테스트:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **노트북 실행 테스트:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **환경 변수 확인:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### 개별 노트북 실행

Jupyter에서 노트북을 열고 셀을 순차적으로 실행하세요. 각 노트북은 독립적으로 구성되어 있으며 다음을 포함합니다:
- import 문
- 구성 로딩
- 에이전트 구현 예제
- Markdown 셀에 예상 출력

## 코드 스타일

### Python 규칙

- **Python 버전**: 3.12 이상
- **코드 스타일**: 표준 Python PEP 8 규칙 준수
- **노트북**: 개념을 설명하는 명확한 Markdown 셀 사용
- **import**: 표준 라이브러리, 서드파티, 로컬 import 순서로 그룹화

### Jupyter 노트북 규칙

- 코드 셀 앞에 설명이 포함된 Markdown 셀 추가
- 참조용 출력 예제를 노트북에 포함
- 강의 개념에 맞는 명확한 변수 이름 사용
- 노트북 실행 순서를 선형적으로 유지 (셀 1 → 2 → 3...)

### 파일 구성

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## 빌드 및 배포

### 문서 빌드

이 저장소는 Markdown을 문서화에 사용합니다:
- 각 강의 폴더에 README.md 파일 포함
- 저장소 루트에 메인 README.md 파일
- GitHub Actions를 통한 자동 번역 시스템

### CI/CD 파이프라인

`.github/workflows/`에 위치:

1. **co-op-translator.yml** - 50개 이상의 언어로 자동 번역
2. **welcome-issue.yml** - 새로운 이슈 작성자 환영
3. **welcome-pr.yml** - 새로운 PR 기여자 환영

### 배포

이 저장소는 교육용으로 설계되었으며 배포 프로세스가 없습니다. 사용자는:
1. 저장소를 포크하거나 클론
2. 노트북을 로컬 또는 GitHub Codespaces에서 실행
3. 예제를 수정하고 실험하며 학습

## Pull Request 지침

### 제출 전

1. **변경 사항 테스트:**
   - 영향을 받은 노트북을 완전히 실행
   - 모든 셀이 오류 없이 실행되는지 확인
   - 출력이 적절한지 확인

2. **문서 업데이트:**
   - 새로운 개념을 추가할 경우 README.md 업데이트
   - 복잡한 코드에 주석 추가
   - Markdown 셀이 목적을 설명하도록 작성

3. **파일 변경 사항:**
   - `.env` 파일을 커밋하지 않음 (`.env.example` 사용)
   - `venv/` 또는 `__pycache__/` 디렉토리를 커밋하지 않음
   - 개념을 설명하는 경우 노트북 출력 유지
   - 임시 파일 및 백업 노트북(`*-backup.ipynb`) 제거

### PR 제목 형식

설명적인 제목 사용:
- `[Lesson-XX] <개념>에 대한 새로운 예제 추가`
- `[Fix] Lesson-XX README의 오타 수정`
- `[Update] Lesson-XX 코드 샘플 개선`
- `[Docs] 설정 지침 업데이트`

### 필수 확인 사항

- 노트북이 오류 없이 실행되어야 함
- README 파일이 명확하고 정확해야 함
- 저장소의 기존 코드 패턴을 따를 것
- 다른 강의와 일관성을 유지할 것

## 추가 참고 사항

### 일반적인 문제

1. **Python 버전 불일치:**
   - Python 3.12 이상 사용
   - 일부 패키지는 이전 버전에서 작동하지 않을 수 있음
   - `python3 -m venv`를 사용하여 Python 버전을 명시적으로 지정

2. **환경 변수:**
   - 항상 `.env.example`에서 `.env` 생성
   - `.env` 파일을 커밋하지 않음 (`.gitignore`에 포함)
   - GitHub 토큰은 적절한 권한 필요

3. **패키지 충돌:**
   - 새 가상 환경 사용
   - 개별 패키지 대신 `requirements.txt`에서 설치
   - 일부 노트북은 Markdown 셀에 언급된 추가 패키지가 필요할 수 있음

4. **Azure 서비스:**
   - Azure AI 서비스는 활성 구독 필요
   - 일부 기능은 지역별로 제한될 수 있음
   - GitHub Models의 무료 등급 제한 적용

### 학습 경로

강의 진행 순서 추천:
1. **00-course-setup** - 환경 설정을 위한 시작점
2. **01-intro-to-ai-agents** - AI 에이전트 기본 개념 이해
3. **02-explore-agentic-frameworks** - 다양한 프레임워크 학습
4. **03-agentic-design-patterns** - 핵심 디자인 패턴
5. 번호 순서대로 강의 진행

### 프레임워크 선택

목표에 따라 프레임워크 선택:
- **학습/프로토타입**: Semantic Kernel + GitHub Models (무료)
- **다중 에이전트 시스템**: AutoGen
- **최신 기능**: Microsoft Agent Framework (MAF)
- **실제 배포**: Azure AI Agent Service

### 도움 받기

- [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)에 참여
- 강의 README 파일에서 특정 지침 검토
- 메인 [README.md](./README.md)에서 과정 개요 확인
- [Course Setup](./00-course-setup/README.md)에서 자세한 설정 지침 참조

### 기여

이 프로젝트는 오픈 교육 프로젝트입니다. 기여를 환영합니다:
- 코드 예제 개선
- 오타 또는 오류 수정
- 명확한 주석 추가
- 새로운 강의 주제 제안
- 추가 언어로 번역

현재 필요 사항은 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues)에서 확인하세요.

## 프로젝트 특수 맥락

### 다국어 지원

이 저장소는 자동 번역 시스템을 사용합니다:
- 50개 이상의 언어 지원
- 번역은 `/translations/<lang-code>/` 디렉토리에 저장
- GitHub Actions 워크플로우가 번역 업데이트 처리
- 원본 파일은 저장소 루트에 영어로 제공

### 강의 구조

각 강의는 일관된 패턴을 따릅니다:
1. 비디오 썸네일 및 링크
2. 작성된 강의 내용 (README.md)
3. 다양한 프레임워크의 코드 샘플
4. 학습 목표 및 사전 요구사항
5. 추가 학습 자료 링크

### 코드 샘플 명명 규칙

형식: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - 강의 4, Semantic Kernel
- `07-autogen.ipynb` - 강의 7, AutoGen
- `14-python-agent-framework.ipynb` - 강의 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - 강의 14, MAF .NET

### 특별 디렉토리

- `translated_images/` - 번역된 이미지 저장
- `images/` - 영어 콘텐츠의 원본 이미지
- `.devcontainer/` - VS Code 개발 컨테이너 구성
- `.github/` - GitHub Actions 워크플로우 및 템플릿

### 종속성

`requirements.txt`의 주요 패키지:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen 프레임워크
- `semantic-kernel` - Semantic Kernel 프레임워크
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI 서비스
- `azure-search-documents` - Azure AI 검색 통합
- `chromadb` - RAG 예제를 위한 벡터 데이터베이스
- `chainlit` - 채팅 UI 프레임워크
- `browser_use` - 에이전트용 브라우저 자동화
- `mcp[cli]` - 모델 컨텍스트 프로토콜 지원
- `mem0ai` - 에이전트 메모리 관리

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.