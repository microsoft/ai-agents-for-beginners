# 강의 설정

## 소개

이 강의에서는 이 과정의 코드 샘플을 실행하는 방법을 다룹니다.

## 다른 학습자들과 소통하고 도움 받기

저장소를 복제하기 전에, [AI Agents For Beginners Discord 채널](https://aka.ms/ai-agents/discord)에 가입하여 설치 관련 도움을 받거나, 과정에 대한 질문을 하거나, 다른 학습자들과 연결하세요.

## 저장소 복제 또는 포크하기

시작하려면 GitHub 저장소를 복제하거나 포크하세요. 이렇게 하면 코스 자료를 실행, 테스트, 수정할 자신의 버전을 만들 수 있습니다!

<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">저장소 포크하러 가기</a> 링크를 클릭하여 할 수 있습니다.

이제 아래 링크에서 자신만의 포크된 코스 버전을 확인할 수 있습니다:

![Forked Repo](../../../translated_images/ko/forked-repo.33f27ca1901baa6a.webp)

### 얕은 복제 (워크숍 / Codespaces에 권장)

  >전체 기록과 모든 파일을 내려받으면 전체 저장소 크기가 클 수 있습니다(~3GB). 워크숍 참석이나 일부 강의 폴더만 필요한 경우, 얕은 복제(또는 sparse clone)를 사용하면 기록을 잘라내거나 blob을 건너뛰어 대부분 다운로드를 피할 수 있습니다.

#### 빠른 얕은 복제 — 최소 기록, 모든 파일

아래 명령어에서 `<your-username>`을 자신의 포크 URL(또는 기본 원본 URL)로 바꾸세요.

최신 커밋 기록만 복제하려면 (다운로드 용량 작음):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

특정 브랜치를 복제하려면:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 부분(스파스) 복제 — 최소 blob + 선택한 폴더만

부분 복제와 sparse-checkout을 사용합니다 (Git 2.25+ 필요하며 부분 복제 지원 최신 Git 권장):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

저장소 폴더로 이동:

```bash|powershell
cd ai-agents-for-beginners
```

원하는 폴더를 지정하세요 (아래 예시는 두 개 폴더):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

복제 후 파일을 확인하고, 파일만 필요해서 공간을 확보하려면(깃 기록 제거), 저장소 메타데이터를 삭제하세요 (💀돌이킬 수 없음 — 커밋, 풀, 푸시, 기록 접근 불가).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# 파워쉘
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces 사용하기 (로컬 대용량 다운로드 회피 권장)

- [GitHub UI](https://github.com/codespaces)를 통해 이 저장소에 대한 새 Codespace 생성.

- 새 Codespace 터미널에서 위 얕은/스파스 복제 명령어 중 하나를 실행하여 필요한 강의 폴더만 Codespace 작업 영역에 가져오기.
- 선택 사항: Codespaces 내 복제 후 .git 제거하여 공간 확보 (제거 명령어 참고).
- 참고: 저장소를 Codespaces에서 바로 열 경우(추가 복제 없이), Codespaces가 devcontainer 환경을 구축하며 필요한 것 이상을 프로비저닝할 수 있음. 새 Codespace 안에서 얕은 복제를 하면 디스크 사용량 제어에 유리함.

#### 팁

- 수정/커밋할 때는 항상 자신의 포크 URL로 복제 URL 교체.
- 나중에 더 많은 기록이나 파일이 필요하면 가져오거나 sparse-checkout으로 추가 폴더 포함 가능.

## 코드 실행하기

이 과정은 인공지능 에이전트 구축을 직접 경험할 수 있는 일련의 Jupyter 노트북을 제공합니다.

코드 샘플은 **Microsoft Agent Framework (MAF)** 와 `FoundryChatClient`를 사용하며, 이는 <strong>Microsoft Foundry</strong>를 통해 **Microsoft Foundry Agent Service V2** (Responses API)에 연결됩니다.

모든 Python 노트북 파일 이름은 `*-python-agent-framework.ipynb`로 표시되어 있습니다.

## 요구 사항

- Python 3.12 이상
  - <strong>참고</strong>: Python 3.12가 설치되어 있지 않으면 설치하세요. 그리고 python3.12로 venv를 생성하여 requirements.txt에서 올바른 버전이 설치되도록 하세요.
  
    >예시

    Python venv 디렉터리 생성:

    ```bash|powershell
    python -m venv venv
    ```

    그런 다음 아래로 venv 활성화:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10 이상: .NET 코드 샘플을 실행하려면 [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 이상을 설치하세요. 설치한 .NET SDK 버전 확인:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — 인증에 필요합니다. [aka.ms/installazurecli](https://aka.ms/installazurecli)에서 설치하세요.
- **Azure 구독** — Microsoft Foundry 및 Microsoft Foundry Agent Service 접근용.
- **Microsoft Foundry 프로젝트** — 배포된 모델이 있는 프로젝트(e.g., `gpt-5-mini`). 아래 [1단계](#1단계-microsoft-foundry-프로젝트-생성) 참조.

이 저장소 루트에 코드 실행에 필요한 모든 Python 패키지를 포함한 `requirements.txt` 파일이 있습니다.

저장소 루트 터미널에서 다음 명령어로 설치할 수 있습니다:

```bash|powershell
pip install -r requirements.txt
```

충돌과 문제를 피하기 위해 Python 가상 환경을 만드는 것을 권장합니다.

## VSCode 설정하기

VSCode에서 올바른 Python 버전을 사용 중인지 확인하세요.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry 및 Microsoft Foundry Agent Service 설정하기

### 1단계: Microsoft Foundry 프로젝트 생성

노트북 실행을 위해 모델이 배포된 Microsoft Foundry <strong>허브</strong>와 <strong>프로젝트</strong>가 필요합니다.

1. [ai.azure.com](https://ai.azure.com)으로 이동하여 Azure 계정으로 로그인합니다.
2. <strong>허브</strong> 생성(또는 기존 사용). 참고: [Hub 리소스 개요](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. 허브 내에서 <strong>프로젝트</strong> 생성.
4. **Models + Endpoints** → <strong>모델 배포</strong>에서 모델(ex: `gpt-5-mini`) 배포.

### 2단계: 프로젝트 엔드포인트와 모델 배포 이름 가져오기

Microsoft Foundry 포털의 프로젝트에서:

- **프로젝트 엔드포인트** — <strong>개요</strong> 페이지에서 엔드포인트 URL 복사.

![Project Connection String](../../../translated_images/ko/project-endpoint.8cf04c9975bbfbf1.webp)

- **모델 배포 이름** — <strong>Models + Endpoints</strong>에서 배포한 모델 선택 후 **배포 이름** 확인(e.g., `gpt-5-mini`).

### 3단계: `az login`으로 Azure 로그인하기

모든 노트북은 인증에 **`AzureCliCredential`**를 사용하므로 API 키 관리가 필요 없습니다. Azure CLI로 로그인해야 합니다.

1. 아직 설치하지 않았다면 **Azure CLI 설치**: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. 다음 명령어로 <strong>로그인</strong>:

    ```bash|powershell
    az login
    ```

    만약 브라우저가 없는 원격/Codespace 환경이면:

    ```bash|powershell
    az login --use-device-code
    ```

3. 로그인 후 구독 선택 요청 시, 자신 프로젝트가 포함된 구독 선택.

4. 가입 여부 확인:

    ```bash|powershell
    az account show
    ```

> **왜 `az login`인가?** 노트북은 `azure-identity` 패키지의 `AzureCliCredential`로 인증합니다. Azure CLI 세션이 인증 정보를 제공하므로 `.env` 파일에 API 키나 비밀키가 필요 없습니다. 이것은 [보안 모범 사례](https://learn.microsoft.com/azure/developer/ai/keyless-connections)입니다.

### 4단계: `.env` 파일 생성하기

예시 파일 복사:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# 파워셸
Copy-Item .env.example .env
```

`.env` 파일 열고 아래 두 값을 채우세요:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| 변수 | 위치 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry 포털 → 프로젝트 → <strong>개요</strong> 페이지 |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry 포털 → **Models + Endpoints** → 배포한 모델 이름 |

대부분의 강의는 여기까지면 됩니다! 노트북은 자동으로 `az login` 세션을 통해 인증됩니다.

### 5단계: Python 의존성 설치

```bash|powershell
pip install -r requirements.txt
```

아까 생성한 가상환경 내부에서 실행하는 걸 권장합니다.

## 5강 추가 설정 (Agentic RAG)

5강은 검색 강화 생성용으로 <strong>Azure AI Search</strong>를 사용합니다. 해당 강의를 실행할 경우 `.env` 파일에 아래 변수를 추가하세요:

| 변수 | 위치 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure 포털 → **Azure AI Search** 리소스 → <strong>개요</strong> → URL |
| `AZURE_SEARCH_API_KEY` | Azure 포털 → **Azure AI Search** 리소스 → <strong>설정</strong> → <strong>키</strong> → 기본 관리자 키 |

## Azure OpenAI 직접 호출하는 강의 추가 설정 (6강, 8강)

6강, 8강의 일부 노트북은 Microsoft Foundry 프로젝트 대신 <strong>Azure OpenAI</strong>를 직접 호출합니다(Responses API 사용). 해당 샘플은 이전에 GitHub Models를 사용했었는데, 이것은 (2026년 7월 퇴출 예정) Responses API를 지원하지 않습니다. 해당 샘플을 실행할 경우 `.env` 파일에 다음 변수를 추가하세요:

| 변수 | 위치 |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure 포털 → **Azure OpenAI** 리소스 → **키 및 엔드포인트** → 엔드포인트 (예: `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Responses API 지원하는 배포된 모델 이름 (예: `gpt-5-mini`) |
| `AZURE_OPENAI_API_KEY` | 선택 사항 — `az login` / Entra ID 대신 키 기반 인증 시 |

> Responses API는 안정된 `/openai/v1/` 엔드포인트를 사용하므로 `api-version`은 필요 없습니다. 키 없는 Entra ID 인증을 위해 `az login`으로 로그인하세요.

## 대체 공급자: MiniMax (OpenAI 호환)

[MiniMax](https://platform.minimaxi.com/)는 OpenAI 호환 API를 통해 최대 204K 토큰의 대용량 컨텍스트 모델을 제공합니다. Microsoft Agent Framework의 `OpenAIChatClient`가 OpenAI 호환 엔드포인트에서 동작하므로, MiniMax를 Azure OpenAI 또는 OpenAI의 드롭인 대체재로 사용할 수 있습니다.

`.env` 파일에 다음 변수를 추가하세요:

| 변수 | 위치 |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API 키 |
| `MINIMAX_BASE_URL` | 기본값 `https://api.minimax.io/v1` 사용 |
| `MINIMAX_MODEL_ID` | 사용할 모델 이름 (예: `MiniMax-M3`) |

**예시 모델**: `MiniMax-M3` (권장), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (더 빠른 응답). 모델 이름과 가용성은 시간에 따라 변동될 수 있으며, 모델 접근은 계정 또는 지역에 따라 다릅니다 — 현재 목록은 [MiniMax Platform](https://platform.minimaxi.com/)에서 확인하세요. `MiniMax-M3`가 계정에 없다면 `MINIMAX_MODEL_ID`를 접근 가능한 모델로 설정하세요(예: `MiniMax-M2.7`).

`OpenAIChatClient`를 사용하는 코드 샘플(예: 14강 호텔 예약 워크플로우)은 `MINIMAX_API_KEY` 설정 시 자동으로 MiniMax 구성을 인식하여 사용합니다.

## 대체 공급자: Foundry Local (모델을 장치에서 직접 실행)

[Foundry Local](https://foundrylocal.ai)은 OpenAI 호환 API를 통해 언어 모델을 <strong>완전히 자신의 기기에서 다운로드, 관리, 제공</strong>하는 경량 런타임입니다 — 클라우드, Azure 구독, API 키 불필요. 오프라인 개발, 클라우드 비용 없이 실험, 데이터 온디바이스 유지에 좋습니다.

Microsoft Agent Framework의 `OpenAIChatClient`가 모든 OpenAI 호환 엔드포인트에서 작동하기 때문에 Foundry Local은 Azure OpenAI의 드롭인 로컬 대안입니다.

**1. Foundry Local 설치**

```bash
# 윈도우
winget install Microsoft.FoundryLocal

# 맥OS
brew install foundrylocal
```

**2. 모델 다운로드 및 실행** (로컬 서비스 시작 포함):

```bash
foundry model list          # 사용 가능한 모델 보기
foundry model run phi-4-mini
```

**3. 로컬 엔드포인트 발견용 Python SDK 설치:**

```bash
pip install foundry-local-sdk
```

**4. Microsoft Agent Framework를 로컬 모델로 지정:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# 모델을 로컬에서 다운로드(필요한 경우) 및 제공한 후, 엔드포인트/포트를 탐색합니다.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # 예: http://localhost:<포트>/v1
    api_key=manager.api_key,        # Foundry Local의 경우 항상 "필요하지 않음"
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **참고:** Foundry Local은 OpenAI 호환 **Chat Completions** 엔드포인트를 제공합니다. 로컬 개발 및 오프라인 시나리오용입니다. 완전한 **Responses API** 기능(상태 저장 대화, 고도화된 도구 오케스트레이션, 에이전트 스타일 개발)을 위해서는 **Azure OpenAI** 또는 본 강의에 나온 **Microsoft Foundry** 프로젝트를 이용하세요. 최신 모델 카탈로그 및 플랫폼 지원은 [Foundry Local 문서](https://foundrylocal.ai) 참조.

## 8강 추가 설정 (Bing 연동 워크플로우)


8과의 조건부 워크플로 노트북은 Microsoft Foundry를 통한 <strong>Bing 접지(grounding)</strong>를 사용합니다. 해당 샘플을 실행할 계획이라면 `.env` 파일에 이 변수를 추가하세요:

| 변수 | 위치 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry 포털 → 프로젝트 → <strong>관리</strong> → **연결된 리소스** → Bing 연결 → 연결 ID 복사 |

## 문제 해결

### macOS에서 SSL 인증서 검증 오류

macOS에서 다음과 같은 오류가 발생한다면:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

이는 macOS의 Python에서 시스템 SSL 인증서를 자동으로 신뢰하지 않는 알려진 문제입니다. 다음 해결 방법을 순서대로 시도해보세요:

**옵션 1: Python의 Install Certificates 스크립트 실행 (권장)**

```bash
# 설치한 파이썬 버전(예: 3.12 또는 3.13)으로 3.XX를 교체하세요:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**옵션 2: 노트북에서 `connection_verify=False` 사용 (GitHub Models 노트북 전용)**

6과 노트북(`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`)에 이미 주석 처리된 해결 방법이 포함되어 있습니다. 클라이언트를 생성할 때 `connection_verify=False`의 주석을 해제하세요:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 인증서 오류가 발생하는 경우 SSL 검증을 비활성화하세요
)
```

> **⚠️ 경고:** SSL 검증 비활성화(`connection_verify=False`)는 인증서 확인을 건너뛰어 보안을 저하시킵니다. 개발 환경에서 임시 해결책으로만 사용하고, 절대 운영 환경에서는 사용하지 마세요.

**옵션 3: `truststore` 설치 및 사용**

```bash
pip install truststore
```

그런 다음 네트워크 호출 전에 노트북 또는 스크립트 상단에 다음을 추가하세요:

```python
import truststore
truststore.inject_into_ssl()
```

## 막히셨나요?

설정 실행에 문제가 있으면 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI 커뮤니티 Discord</a>에 참여하거나 <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">이슈를 생성</a>하세요.

## 다음 강의

이제 이 과정의 코드를 실행할 준비가 되었습니다. AI 에이전트의 세계를 더 많이 배우며 즐거운 학습 되세요!

[AI 에이전트 소개 및 사용 사례](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->