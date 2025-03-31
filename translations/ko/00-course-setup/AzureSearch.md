<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "932a1f463f0fcf97090b93b5d0255dff",
  "translation_date": "2025-03-28T13:39:42+00:00",
  "source_file": "00-course-setup\\AzureSearch.md",
  "language_code": "ko"
}
-->
# Azure AI Search 설정 가이드

이 가이드는 Azure 포털을 사용하여 Azure AI Search를 설정하는 방법을 안내합니다. 아래 단계를 따라 Azure AI Search 서비스를 생성하고 구성하세요.

## 사전 준비

시작하기 전에 다음을 준비하세요:

- Azure 구독. Azure 구독이 없는 경우 [Azure 무료 계정](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)에서 무료 계정을 생성할 수 있습니다.

## 1단계: Azure AI Search 서비스 생성

1. [Azure 포털](https://portal.azure.com/?wt.mc_id=studentamb_258691)에 로그인합니다.
2. 왼쪽 탐색 창에서 **리소스 생성**을 클릭합니다.
3. 검색 창에 "Azure Cognitive Search"를 입력하고 결과 목록에서 **Azure Cognitive Search**를 선택합니다.
4. **만들기** 버튼을 클릭합니다.
5. **기본** 탭에서 다음 정보를 입력합니다:
   - **구독**: 사용 중인 Azure 구독을 선택합니다.
   - **리소스 그룹**: 새 리소스 그룹을 생성하거나 기존 그룹을 선택합니다.
   - **리소스 이름**: 검색 서비스의 고유 이름을 입력합니다.
   - **지역**: 사용자와 가까운 지역을 선택합니다.
   - **가격 책정 계층**: 요구 사항에 맞는 가격 책정 계층을 선택합니다. 테스트를 위해 Free 계층을 선택할 수 있습니다.
6. **검토 + 만들기**를 클릭합니다.
7. 설정을 검토한 후 **만들기**를 클릭하여 검색 서비스를 생성합니다.

## 2단계: Azure AI Search 시작하기

1. 배포가 완료되면 Azure 포털에서 검색 서비스로 이동합니다.
2. 검색 서비스 개요 페이지에서 **빠른 시작** 버튼을 클릭합니다.
3. 빠른 시작 가이드를 따라 인덱스를 생성하고 데이터를 업로드하며 검색 쿼리를 수행합니다.

### 인덱스 생성

1. 빠른 시작 가이드에서 **인덱스 생성**을 클릭합니다.
2. 필드와 속성(예: 데이터 유형, 검색 가능 여부, 필터 가능 여부)을 지정하여 인덱스 스키마를 정의합니다.
3. **생성**을 클릭하여 인덱스를 생성합니다.

### 데이터 업로드

1. 빠른 시작 가이드에서 **데이터 업로드**를 클릭합니다.
2. 데이터 소스(예: Azure Blob Storage, Azure SQL Database)를 선택하고 필요한 연결 정보를 제공합니다.
3. 데이터 소스 필드를 인덱스 필드에 매핑합니다.
4. **제출**을 클릭하여 데이터를 인덱스에 업로드합니다.

### 검색 쿼리 수행

1. 빠른 시작 가이드에서 **검색 탐색기**를 클릭합니다.
2. 검색 상자에 검색 쿼리를 입력하여 검색 기능을 테스트합니다.
3. 검색 결과를 검토하고 필요한 경우 인덱스 스키마나 데이터를 조정합니다.

## 3단계: Azure AI Search 도구 사용

Azure AI Search는 다양한 도구와 통합되어 검색 기능을 향상시킬 수 있습니다. Azure CLI, Python SDK 등 고급 구성 및 작업을 위한 도구를 사용할 수 있습니다.

### Azure CLI 사용

1. [Azure CLI 설치](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 지침을 따라 Azure CLI를 설치합니다.
2. 다음 명령어를 사용하여 Azure CLI에 로그인합니다:
   ```bash
   az login
   ```
3. Azure CLI를 사용하여 새 검색 서비스를 생성합니다:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Azure CLI를 사용하여 인덱스를 생성합니다:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK 사용

1. Python용 Azure Cognitive Search 클라이언트 라이브러리를 설치합니다:
   ```bash
   pip install azure-search-documents
   ```
2. 다음 Python 코드를 사용하여 인덱스를 생성하고 문서를 업로드합니다:
   ```python
   from azure.core.credentials import AzureKeyCredential
   from azure.search.documents import SearchClient
   from azure.search.documents.indexes import SearchIndexClient
   from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

   service_endpoint = "https://<service-name>.search.windows.net"
   api_key = "<api-key>"

   index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(api_key))

   fields = [
       SimpleField(name="id", type=edm.String, key=True),
       SimpleField(name="content", type=edm.String, searchable=True),
   ]

   index = SearchIndex(name="sample-index", fields=fields)

   index_client.create_index(index)

   search_client = SearchClient(service_endpoint, "sample-index", AzureKeyCredential(api_key))

   documents = [
       {"id": "1", "content": "Hello world"},
       {"id": "2", "content": "Azure Cognitive Search"}
   ]

   search_client.upload_documents(documents)
   ```

자세한 내용은 다음 문서를 참조하세요:

- [Azure Cognitive Search 서비스 생성](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Azure Cognitive Search 시작하기](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search 도구](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 결론

Azure 포털과 통합 도구를 사용하여 Azure AI Search를 성공적으로 설정했습니다. 이제 Azure AI Search의 고급 기능과 역량을 탐색하여 검색 솔루션을 향상시킬 수 있습니다.

추가 지원이 필요하면 [Azure Cognitive Search 문서](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691)를 방문하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 모국어 버전이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역을 사용하여 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.