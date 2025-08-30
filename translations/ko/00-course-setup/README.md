<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c55b973b1562abf5aadf6a4028265ac5",
  "translation_date": "2025-08-30T08:02:10+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ko"
}
-->
# 코스 설정

## 소개

이 강의에서는 코스의 코드 샘플을 실행하는 방법을 다룹니다.

## 다른 학습자들과 함께하고 도움받기

저장소를 복제하기 전에 [AI Agents For Beginners Discord 채널](https://aka.ms/ai-agents/discord)에 가입하세요. 여기에서 설정에 대한 도움을 받거나, 강의에 대한 질문을 하거나, 다른 학습자들과 교류할 수 있습니다.

## 이 저장소를 복제하거나 포크하기

먼저 GitHub 저장소를 복제하거나 포크하세요. 이렇게 하면 강의 자료의 개인 버전을 만들어 코드를 실행하고, 테스트하고, 수정할 수 있습니다!

이 작업은 아래 링크를 클릭하여 수행할 수 있습니다.

![포크된 저장소](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.ko.png)

## 코드 실행하기

이 강의는 AI 에이전트를 구축하는 실습 경험을 제공하는 일련의 Jupyter Notebook을 제공합니다.

코드 샘플은 다음 중 하나를 사용합니다:

**GitHub 계정 필요 - 무료**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. (semantic-kernel.ipynb)로 표시됨  
2) AutoGen Framework + GitHub Models Marketplace. (autogen.ipynb)로 표시됨  

**Azure 구독 필요**:  
3) Azure AI Foundry + Azure AI Agent Service. (azureaiagent.ipynb)로 표시됨  

세 가지 예제를 모두 시도해보고 자신에게 가장 적합한 것을 확인해보는 것을 권장합니다.

선택한 옵션에 따라 아래의 설정 단계를 따르세요:

## 요구 사항

- Python 3.12+  
  - **NOTE**: Python 3.12가 설치되어 있지 않다면 설치하세요. 그런 다음 `python3.12`를 사용하여 가상 환경(venv)을 생성하여 `requirements.txt` 파일에서 올바른 버전이 설치되도록 하세요.
- GitHub 계정 - GitHub Models Marketplace에 액세스하기 위해 필요
- Azure 구독 - Azure AI Foundry에 액세스하기 위해 필요
- Azure AI Foundry 계정 - Azure AI Agent Service에 액세스하기 위해 필요

이 저장소의 루트에 있는 `requirements.txt` 파일에는 코드 샘플을 실행하는 데 필요한 모든 Python 패키지가 포함되어 있습니다.

다음 명령어를 터미널에서 실행하여 패키지를 설치할 수 있습니다:

```bash
pip install -r requirements.txt
```  
Python 가상 환경을 생성하여 충돌 및 문제를 방지하는 것을 권장합니다.

## VSCode 설정하기

VSCode에서 올바른 Python 버전을 사용하고 있는지 확인하세요.

![이미지](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Models를 사용하는 샘플 설정

### 1단계: GitHub 개인 액세스 토큰(PAT) 가져오기

이 강의는 GitHub Models Marketplace를 활용하여 대형 언어 모델(LLM)에 무료로 액세스할 수 있도록 합니다. 이를 통해 AI 에이전트를 구축할 수 있습니다.

GitHub Models를 사용하려면 [GitHub 개인 액세스 토큰](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)을 생성해야 합니다.

GitHub 계정에서 다음 단계를 따르세요.

[최소 권한 원칙](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely)을 따르세요. 즉, 이 강의의 코드 샘플을 실행하는 데 필요한 권한만 토큰에 부여해야 합니다.

1. **개발자 설정**으로 이동하여 화면 왼쪽에서 `세분화된 토큰` 옵션을 선택합니다.  
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.ko.png)

   그런 다음 `새 토큰 생성`을 선택합니다.  
   ![토큰 생성](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.ko.png)

2. 토큰의 목적을 반영하는 설명적인 이름을 입력하여 나중에 쉽게 식별할 수 있도록 합니다.

    🔐 **토큰 기간 추천**  
    추천 기간: 30일  
    더 안전한 설정을 원한다면 7일과 같은 짧은 기간을 선택할 수 있습니다 🛡️  
    이는 학습 동력을 유지하며 강의를 완료하는 데 좋은 목표가 될 수 있습니다 🚀.  
    ![토큰 이름 및 만료일](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.ko.png)

3. 토큰의 범위를 이 저장소의 포크로 제한합니다.  
   ![저장소 범위 제한](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.ko.png)

4. 토큰의 권한을 제한합니다: **권한** 아래에서 **계정** 탭을 클릭하고 "+ 권한 추가" 버튼을 클릭합니다. 드롭다운이 나타납니다. **Models**를 검색하고 해당 상자를 선택하세요.  
   ![Models 권한 추가](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.ko.png)

5. 토큰을 생성하기 전에 필요한 권한을 확인하세요.  
   ![권한 확인](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.ko.png)

6. 토큰을 생성하기 전에 비밀번호 관리 프로그램과 같은 안전한 장소에 토큰을 저장할 준비가 되었는지 확인하세요. 생성 후에는 다시 표시되지 않습니다.  
   ![토큰 안전하게 저장](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.ko.png)

방금 생성한 새 토큰을 복사하세요. 이제 이 강의에 포함된 `.env` 파일에 추가합니다.

### 2단계: `.env` 파일 생성하기

터미널에서 다음 명령어를 실행하여 `.env` 파일을 생성하세요.

```bash
cp .env.example .env
```

이 명령어는 예제 파일을 복사하여 `.env` 파일을 생성하며, 환경 변수 값을 입력할 수 있습니다.

복사한 토큰을 사용하여 선호하는 텍스트 편집기에서 `.env` 파일을 열고 `GITHUB_TOKEN` 필드에 토큰을 붙여넣으세요.  
![GitHub 토큰 필드](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.ko.png)

이제 이 강의의 코드 샘플을 실행할 준비가 되었습니다.

## Azure AI Foundry 및 Azure AI Agent Service를 사용하는 샘플 설정

### 1단계: Azure 프로젝트 엔드포인트 가져오기

Azure AI Foundry에서 허브와 프로젝트를 생성하는 단계는 [허브 리소스 개요](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)를 참조하세요.

프로젝트를 생성한 후에는 프로젝트의 연결 문자열을 가져와야 합니다.

이는 Azure AI Foundry 포털의 **개요** 페이지에서 확인할 수 있습니다.  
![프로젝트 연결 문자열](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.ko.png)

### 2단계: `.env` 파일 생성하기

터미널에서 다음 명령어를 실행하여 `.env` 파일을 생성하세요.

```bash
cp .env.example .env
```

이 명령어는 예제 파일을 복사하여 `.env` 파일을 생성하며, 환경 변수 값을 입력할 수 있습니다.

복사한 토큰을 사용하여 선호하는 텍스트 편집기에서 `.env` 파일을 열고 `PROJECT_ENDPOINT` 필드에 토큰을 붙여넣으세요.

### 3단계: Azure에 로그인하기

보안 모범 사례로, Microsoft Entra ID를 사용하여 Azure OpenAI에 [키리스 인증](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst)을 사용할 것입니다.

다음으로 터미널을 열고 `az login --use-device-code`를 실행하여 Azure 계정에 로그인하세요.

로그인한 후 터미널에서 구독을 선택하세요.

## 추가 환경 변수 - Azure Search 및 Azure OpenAI

Agentic RAG 강의 - 5강에서는 Azure Search 및 Azure OpenAI를 사용하는 샘플이 포함되어 있습니다.

이 샘플을 실행하려면 `.env` 파일에 다음 환경 변수를 추가해야 합니다:

### 개요 페이지 (프로젝트)

- `AZURE_SUBSCRIPTION_ID` - 프로젝트의 **개요** 페이지에서 **프로젝트 세부 정보**를 확인하세요.
- `AZURE_AI_PROJECT_NAME` - 프로젝트 **개요** 페이지 상단에서 확인하세요.
- `AZURE_OPENAI_SERVICE` - **Azure OpenAI Service**의 **포함된 기능** 탭에서 확인하세요.

### 관리 센터

- `AZURE_OPENAI_RESOURCE_GROUP` - **관리 센터**의 **개요** 페이지에서 **프로젝트 속성**으로 이동하세요.
- `GLOBAL_LLM_SERVICE` - **연결된 리소스**에서 **Azure AI Services** 연결 이름을 찾으세요. 나열되지 않은 경우, Azure 포털에서 리소스 그룹 아래 AI Services 리소스 이름을 확인하세요.

### 모델 + 엔드포인트 페이지

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - 임베딩 모델(예: `text-embedding-ada-002`)을 선택하고 모델 세부 정보에서 **배포 이름**을 확인하세요.
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - 채팅 모델(예: `gpt-4o-mini`)을 선택하고 모델 세부 정보에서 **배포 이름**을 확인하세요.

### Azure 포털

- `AZURE_OPENAI_ENDPOINT` - **Azure AI Services**를 찾고 클릭한 다음 **리소스 관리**, **키 및 엔드포인트**로 이동하여 "Azure OpenAI 엔드포인트"를 스크롤하여 "언어 API"를 복사하세요.
- `AZURE_OPENAI_API_KEY` - 동일한 화면에서 KEY 1 또는 KEY 2를 복사하세요.
- `AZURE_SEARCH_SERVICE_ENDPOINT` - **Azure AI Search** 리소스를 찾고 클릭한 다음 **개요**를 확인하세요.
- `AZURE_SEARCH_API_KEY` - 그런 다음 **설정**으로 이동하여 **키**에서 기본 또는 보조 관리자 키를 복사하세요.

### 외부 웹페이지

- `AZURE_OPENAI_API_VERSION` - [API 버전 수명 주기](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) 페이지에서 **최신 GA API 릴리스**를 확인하세요.

### 키리스 인증 설정

자격 증명을 하드코딩하는 대신 Azure OpenAI와 키리스 연결을 사용합니다. 이를 위해 `DefaultAzureCredential`을 가져오고 나중에 `DefaultAzureCredential` 함수를 호출하여 자격 증명을 가져옵니다.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## 어디에서 막혔나요?

설정 중 문제가 발생하면, [AI Agents For Beginners Discord 채널](https://aka.ms/ai-agents/discord)에 참여하여 도움을 요청하세요.

## 다음 강의

이제 이 강의의 코드를 실행할 준비가 되었습니다. AI 에이전트의 세계를 더 깊이 탐구하며 즐거운 학습 되세요!

[AI 에이전트 소개 및 에이전트 사용 사례](../01-intro-to-ai-agents/README.md)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.