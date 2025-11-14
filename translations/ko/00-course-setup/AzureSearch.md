<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:29:41+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ko"
}
-->
# Azure AI Search 설정 가이드

이 가이드는 Azure 포털을 사용하여 Azure AI Search를 설정하는 방법을 안내합니다. 아래 단계를 따라 Azure AI Search 서비스를 생성하고 구성하세요.

## 사전 준비 사항

시작하기 전에 다음을 준비하세요:

- Azure 구독. Azure 구독이 없는 경우 [Azure 무료 계정](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)에서 무료 계정을 생성할 수 있습니다.

## 1단계: Azure Storage 계정 생성

1. [Azure Storage 계정 생성](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) 지침을 따라 새 Azure Storage 계정을 생성하세요.
   **NOTE**: Storage 계정 유형은 Standard General Purpose V2여야 합니다.

## 2단계: Azure AI Search 서비스 생성

1. [Azure 포털](https://portal.azure.com/?wt.mc_id=studentamb_258691)에 로그인합니다.
2. 왼쪽 탐색 창에서 **리소스 생성**을 클릭합니다.
3. 검색 상자에 "Azure AI Search"를 입력하고 결과 목록에서 **Azure AI Search**를 선택합니다.
4. **생성** 버튼을 클릭합니다.
5. **기본 정보** 탭에서 다음 정보를 입력합니다:
   - **구독**: Azure 구독을 선택합니다.
   - **리소스 그룹**: 새 리소스 그룹을 생성하거나 기존 그룹을 선택합니다.
   - **리소스 이름**: 검색 서비스에 대한 고유 이름을 입력합니다.
   - **지역**: 사용자와 가까운 지역을 선택합니다.
   - **가격 책정 계층**: 요구 사항에 맞는 가격 책정 계층을 선택합니다. 테스트를 위해 무료 계층으로 시작할 수 있습니다.
6. **검토 + 생성**을 클릭합니다.
7. 설정을 검토한 후 **생성**을 클릭하여 검색 서비스를 생성합니다.

## 3단계: Azure AI Search 시작하기

1. 배포가 완료되면 Azure 포털에서 검색 서비스로 이동합니다.
2. 검색 서비스 개요 창에서 URL을 복사합니다. URL은 `https://<service-name>.search.windows.net` 형식이어야 합니다.
3. 설정 > 키 창에서 쿼리 키를 복사합니다.
4. [빠른 시작 가이드](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) 페이지의 단계를 따라 인덱스를 생성하고 데이터를 업로드하며 검색 쿼리를 수행합니다.

## 4단계: Azure AI Search 도구 사용

Azure AI Search는 다양한 도구와 통합되어 검색 기능을 향상시킵니다. Azure CLI, Python SDK, .NET SDK 및 기타 도구를 사용하여 고급 구성 및 작업을 수행할 수 있습니다.

### Azure CLI 사용하기

1. [Azure CLI 설치](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 지침을 따라 Azure CLI를 설치합니다.
2. 다음 명령을 사용하여 Azure CLI에 로그인합니다:

   ```bash
   az login
   ```

3. Azure AI Search 인스턴스의 엔드포인트와 API 키를 환경 변수에 저장합니다.

    ```bash
    # zsh/bash
    export AZURE_SEARCH_SERVICE_ENDPOINT=$(az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv)
    export AZURE_SEARCH_API_KEY=$(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv
    $env:AZURE_SEARCH_API_KEY = $(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK 사용하기

1. Python용 Azure Cognitive Search 클라이언트 라이브러리를 설치합니다:

   ```bash
   pip install azure-search-documents
   ```

2. 다음 Python 코드를 사용하여 인덱스를 생성하고 문서를 업로드합니다:

    ```python
    import os
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    api_key = os.getenv("AZURE_SEARCH_API_KEY")
    index_name = "sample-index"

    credential = AzureKeyCredential(api_key)
    index_client = SearchIndexClient(service_endpoint, credential)

    fields = [
        SimpleField(name="id", type=edm.String, key=True),
        SimpleField(name="content", type=edm.String, searchable=True),
    ]

    index = SearchIndex(name=index_name, fields=fields)

    index_client.create_index(index)

    search_client = SearchClient(service_endpoint, index_name, credential)

    documents = [
        {"id": "1", "content": "Hello world"},
        {"id": "2", "content": "Azure Cognitive Search"}
    ]

    search_client.upload_documents(documents)
    ```

### .NET SDK 사용하기

1. 다음 명령을 실행하여 인덱스를 생성하고 문서를 업로드합니다:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. `AzureSearch.cs`의 .NET 코드 예시는 다음과 같습니다:

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:property PublishAot=false

    using Azure;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var apiKey = Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!;
    var indexName = "sample-index";

    var credential = new AzureKeyCredential(apiKey);
    var indexClient = new SearchIndexClient(serviceEndpoint, credential);

    var fields = new List<SearchField>()
    {
        new SimpleField("id", SearchFieldDataType.String) { IsKey = true },
        new SearchableField("content")
    };

    var index = new SearchIndex(name: indexName, fields: fields);

    var response = await indexClient.CreateOrUpdateIndexAsync(index);
    Console.WriteLine($"Index '{response.Value.Name}' ready.");

    var searchClient = new SearchClient(serviceEndpoint, indexName, credential);

    var documents = new[]
    {
        new { id = "1", content = "Hello world" },
        new { id = "2", content = "Azure Cognitive Search" }
    };

    var result = await searchClient.UploadDocumentsAsync(documents);
    Console.WriteLine($"Uploaded {result.Value.Results.Count} documents to index '{response.Value.Name}'.");
    ```

자세한 정보는 아래 문서를 참조하세요:

- [Azure Cognitive Search 서비스 생성](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Azure Cognitive Search 시작하기](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search 도구](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 결론

Azure 포털을 사용하여 Azure AI Search를 성공적으로 설정하고 도구를 통합했습니다. 이제 Azure AI Search의 고급 기능과 기능을 탐색하여 검색 솔루션을 향상시킬 수 있습니다.

추가 지원이 필요하면 [Azure Cognitive Search 문서](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)를 방문하세요.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.