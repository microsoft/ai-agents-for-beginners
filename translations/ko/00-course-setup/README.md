# 과정 설정

## 소개

이 수업에서는 이 과정의 코드 샘플을 실행하는 방법을 다룹니다.

## 다른 학습자와 함께 참여하고 도움 받기

레포를 클론하기 전에, [AI Agents For Beginners Discord 채널](https://aka.ms/ai-agents/discord)에 참여하여 설정 관련 도움을 받거나 수업에 대한 질문을 하거나 다른 학습자와 소통하세요.

## 이 레포 복제 또는 포크하기

시작하려면 GitHub 저장소를 복제하거나 포크하세요. 이렇게 하면 코스 자료의 자신만의 버전을 만들어 코드를 실행, 테스트 및 조정할 수 있습니다!

<a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">레포 포크하기</a> 링크를 클릭하면 됩니다.

이제 다음 링크에서 이 과정의 포크된 자신의 버전을 갖게 됩니다:

![Forked Repo](../../../translated_images/ko/forked-repo.33f27ca1901baa6a.webp)

### 얕은 복제 (워크숍 / Codespaces 추천)

  >전체 저장소는 전체 히스토리와 모든 파일을 다운로드하면 용량이 클 수 있습니다(~3GB). 워크숍에만 참여하거나 몇 개의 수업 폴더만 필요할 경우, 얕은 복제(또는 희소 복제)는 히스토리를 줄이거나 blob을 건너뛰어 대부분의 다운로드를 피합니다.

#### 빠른 얕은 복제 — 최소 히스토리, 전체 파일

아래 명령어에서 `<your-username>`을 자신의 포크 URL(또는 업스트림 URL로 선호하는 경우)로 교체하세요.

최신 커밋 히스토리만 복제하려면(작은 다운로드):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

특정 브랜치를 복제하려면:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### 부분(희소) 복제 — 최소 blob + 선택한 폴더만

부분 복제와 희소 체크아웃을 사용합니다(Git 2.25+ 필요, 부분 복제 지원이 있는 최신 Git 권장):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

레포 폴더로 이동:

```bash|powershell
cd ai-agents-for-beginners
```

원하는 폴더를 지정하세요(아래 예시는 두 폴더):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

복제하고 파일을 확인한 후, 파일만 필요하고 공간을 확보하려면(히스토리 제외), 저장소 메타데이터를 삭제하세요 (💀복구 불가 — 모든 Git 기능 소실: 커밋, 풀, 푸시, 히스토리 접근 불가).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# 파워셸
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces 사용 (로컬 대용량 다운로드 회피 권장)

- [GitHub UI](https://github.com/codespaces)를 통해 이 레포로 새 Codespace를 만드세요.

- 새 Codespace의 터미널에서 위 얕은/희소 복제 명령 중 하나를 실행해 필요한 수업 폴더만 Codespace 작업공간으로 가져옵니다.
- 선택사항: Codespace 내 복제 후 .git을 제거해 추가 공간 확보 가능(위 제거 명령 참고).
- 참고: 레포를 Codespaces에서 직접 열 경우(추가 복제 없이) devcontainer 환경을 구성하고 필요 이상으로 프로비저닝할 수 있습니다. 새 Codespace 내에서 얕은 복제를 실행하면 디스크 사용을 더 잘 제어할 수 있습니다.

#### 팁

- 편집/커밋하려면 클론 URL을 항상 자신의 포크로 바꾸세요.
- 이후 더 많은 히스토리나 파일이 필요하면 가져오거나 희소 체크아웃을 조정해 추가 폴더를 포함할 수 있습니다.

## 코드 실행

이 과정은 AI 에이전트 구축을 실습할 수 있는 일련의 Jupyter 노트북을 제공합니다.

코드 샘플은 **Microsoft Agent Framework (MAF)** 와 `AzureAIProjectAgentProvider` 를 사용하며, 이는 **Microsoft Foundry** 를 통해 **Azure AI Agent Service V2** (Responses API)에 연결합니다.

모든 Python 노트북은 `*-python-agent-framework.ipynb` 로 표시됩니다.

## 요구사항

- Python 3.12+
  - **참고**: Python3.12가 설치되어 있지 않으면 설치하세요. 그리고 해당 버전 python3.12로 가상환경을 만들어 requirements.txt 파일에서 올바른 버전이 설치되게 하세요.
  
    >예시

    파이썬 가상환경 디렉터리 만들기:

    ```bash|powershell
    python -m venv venv
    ```

    이후 venv 환경 활성화:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: .NET을 사용하는 샘플 코드의 경우, [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 이상을 설치하세요. 그리고 설치된 .NET SDK 버전을 확인하세요:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — 인증에 필요. [aka.ms/installazurecli](https://aka.ms/installazurecli)에서 설치 가능.
- **Azure 구독** — Microsoft Foundry 및 Azure AI Agent Service 액세스용.
- **Microsoft Foundry 프로젝트** — 배포된 모델(e.g., `gpt-4o`)이 포함된 프로젝트. 아래 [1단계](../../../00-course-setup) 참고.

이 저장소 루트에는 코드 샘플 실행에 필요한 모든 Python 패키지가 나열된 `requirements.txt` 파일이 포함되어 있습니다.

루트 폴더에서 다음 명령어로 설치하세요:

```bash|powershell
pip install -r requirements.txt
```

충돌과 문제를 방지하기 위해 Python 가상환경을 만들고 실행하는 것을 권장합니다.

## VSCode 설정

VSCode에서 올바른 Python 버전을 사용하고 있는지 확인하세요.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry 및 Azure AI Agent Service 설정

### 1단계: Microsoft Foundry 프로젝트 만들기

노트북을 실행하려면 Azure AI Foundry **허브**와 **프로젝트**, 그리고 배포된 모델이 있어야 합니다.

1. [ai.azure.com](https://ai.azure.com)으로 가서 Azure 계정으로 로그인하세요.
2. **허브**를 만들거나 기존 허브를 사용하세요. 참고: [허브 리소스 개요](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. 허브 내에서 **프로젝트**를 만드세요.
4. **Models + Endpoints** → **Deploy model**에서 모델(e.g., `gpt-4o`)을 배포하세요.

### 2단계: 프로젝트 엔드포인트 및 모델 배포 이름 가져오기

Microsoft Foundry 포털의 프로젝트에서:

- **프로젝트 엔드포인트** — **Overview** 페이지로 가서 엔드포인트 URL을 복사하세요.

![Project Connection String](../../../translated_images/ko/project-endpoint.8cf04c9975bbfbf1.webp)

- **모델 배포 이름** — **Models + Endpoints**로 가서 배포된 모델을 선택하고 **Deployment name**(예: `gpt-4o`)을 확인하세요.

### 3단계: `az login`으로 Azure 로그인

모든 노트북은 인증을 위해 **`AzureCliCredential`** 을 사용합니다 — API 키 관리가 불필요합니다. 이를 위해 Azure CLI로 로그인해야 합니다.

1. Azure CLI를 설치하지 않았다면 설치: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. 다음을 실행해 로그인:

    ```bash|powershell
    az login
    ```

    마우스 없는 원격/Codespace 환경이면:

    ```bash|powershell
    az login --use-device-code
    ```

3. 구독 선택 요청 시 - Foundry 프로젝트가 포함된 구독을 선택하세요.

4. 로그인 상태 확인:

    ```bash|powershell
    az account show
    ```

> **왜 `az login`인가요?** 노트북은 `azure-identity` 패키지의 `AzureCliCredential`을 이용해 인증합니다. 즉, Azure CLI 세션이 자격 증명을 제공하므로 `.env` 파일에 API 키나 비밀을 포함하지 않아도 됩니다. 이는 [보안 모범 사례](https://learn.microsoft.com/azure/developer/ai/keyless-connections)입니다.

### 4단계: `.env` 파일 만들기

샘플 파일을 복사하세요:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# 파워셸
Copy-Item .env.example .env
```

`.env` 를 열어 이 두 값을 채워 넣으세요:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| 변수 | 위치 |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry 포털 → 프로젝트 → **Overview** 페이지 |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry 포털 → **Models + Endpoints** → 배포된 모델 이름 |

대부분 수업은 여기까지입니다! 노트북은 자동으로 `az login` 세션을 통해 인증됩니다.

### 5단계: Python 의존성 설치

```bash|powershell
pip install -r requirements.txt
```

앞서 만든 가상환경 안에서 실행하는 걸 권장합니다.

## 수업 5 추가 설정 (Agentic RAG)

수업 5는 검색 증강 생성에 **Azure AI Search**를 사용합니다. 실행할 계획이면 `.env`에 이 변수들을 추가하세요:

| 변수 | 위치 |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure 포털 → **Azure AI Search** 리소스 → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure 포털 → **Azure AI Search** 리소스 → **Settings** → **Keys** → 기본 관리자 키 |

## 수업 6 및 8 추가 설정 (GitHub Models)

수업 6, 8의 일부 노트북은 Azure AI Foundry 대신 **GitHub Models**를 사용합니다. 실행할 경우 `.env`에 다음을 추가하세요:

| 변수 | 위치 |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | 기본값: `https://models.inference.ai.azure.com` |
| `GITHUB_MODEL_ID` | 사용할 모델 이름 (예: `gpt-4o-mini`) |

## 수업 8 추가 설정 (Bing Grounding Workflow)

수업 8의 조건부 워크플로 노트북은 Azure AI Foundry를 통한 **Bing grounding**을 사용합니다. 실행하면 `.env`에 이 변수를 추가하세요:

| 변수 | 위치 |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry 포털 → 프로젝트 → **Management** → **Connected resources** → Bing 연결 → 연결 ID 복사 |

## 문제 해결

### macOS에서 SSL 인증서 검증 오류

macOS에서 다음과 같은 오류가 발생할 수 있습니다:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

이는 Python이 시스템 SSL 인증서를 자동으로 신뢰하지 않는 macOS의 알려진 문제입니다. 아래 해결책을 순서대로 시도하세요:

**옵션 1: Python 설치 인증서 스크립트 실행 (권장)**

```bash
# 설치한 Python 버전(예: 3.12 또는 3.13)으로 3.XX를 교체하세요:
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**옵션 2: 노트북에서 `connection_verify=False` 사용 (GitHub Models 노트북 전용)**

수업 6 노트북(`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`)에는 이미 주석 처리된 해결책이 포함되어 있습니다. 클라이언트 생성 시 `connection_verify=False` 주석을 해제하세요:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # 인증서 오류가 발생할 경우 SSL 검증을 비활성화하세요
)
```

> **⚠️ 경고:** SSL 검증 해제(`connection_verify=False`)는 인증서 검증을 건너뛰어 보안을 저하시킵니다. 개발 환경에서만 임시 우회 방법으로 사용하고, 운영 환경에서는 금지하세요.

**옵션 3: `truststore` 설치 및 사용**

```bash
pip install truststore
```

네트워크 호출 전에 노트북이나 스크립트 상단에 다음을 추가하세요:

```python
import truststore
truststore.inject_into_ssl()
```

## 어디에서 막혔나요?

설정 실행 중 문제 있으면 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>에 참여하거나 <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">이슈를 만드세요</a>.

## 다음 수업

이제 이 과정의 코드를 실행할 준비가 되었습니다. AI 에이전트 세계에 대한 학습을 즐기세요!

[AI 에이전트 소개 및 에이전트 사용 사례](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문 인력에 의한 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->