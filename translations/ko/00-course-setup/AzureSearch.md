# Azure AI Search 설정 가이드

이 가이드는 Azure 포털을 사용하여 Azure AI Search를 설정하는 데 도움이 됩니다. 아래 단계를 따라 Azure AI Search 서비스를 생성하고 구성하세요.

## 사전 준비 사항

시작하기 전에 다음을 준비했는지 확인하세요:

- Azure 구독. Azure 구독이 없는 경우 [Azure 무료 계정](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)에서 무료 계정을 만들 수 있습니다.

## 1단계: Azure 저장소 계정 생성

1. [Azure 저장소 계정 만들기](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) 지침을 따라 새 Azure 저장소 계정을 생성하세요.
   <strong>참고</strong>: 저장소 계정 유형이 Standard General Purpose V2인지 확인하세요.

## 2단계: Azure AI Search 서비스 생성

1. [Azure 포털](https://portal.azure.com/?wt.mc_id=studentamb_258691)에 로그인합니다.
2. 왼쪽 탐색 창에서 <strong>리소스 만들기</strong>를 클릭합니다.
3. 검색 상자에 "Azure AI Search"를 입력하고 결과 목록에서 <strong>Azure AI Search</strong>를 선택합니다.
4. <strong>만들기</strong> 버튼을 클릭합니다.
5. **기본 사항** 탭에서 다음 정보를 제공합니다:
   - <strong>구독</strong>: Azure 구독을 선택합니다.
   - **리소스 그룹**: 새 리소스 그룹을 만들거나 기존 그룹을 선택합니다.
   - **리소스 이름**: 검색 서비스에 고유한 이름을 입력합니다.
   - <strong>지역</strong>: 사용자를 가장 가까운 지역을 선택합니다.
   - **가격 책정 계층**: 요구 사항에 맞는 가격 책정 계층을 선택합니다. 테스트용으로는 무료 계층을 시작할 수 있습니다.
6. <strong>검토 + 만들기</strong>를 클릭합니다.
7. 설정을 검토한 후 <strong>만들기</strong>를 클릭하여 검색 서비스를 만듭니다.

## 3단계: Azure AI Search 시작하기

1. 배포가 완료되면 Azure 포털에서 검색 서비스로 이동합니다.
2. 검색 서비스 개요 창에서 URL을 복사합니다. 형식은 `https://<service-name>.search.windows.net`와 같습니다.
3. **(권장)** 아래 4단계에 설명된 대로 Microsoft Entra ID(RBAC)를 사용하여 키 없는 액세스를 활성화하세요 — 키가 필요 없습니다. 이 가이드의 샘플은 인덱스 생성/업데이트 및 문서 업로드를 수행하는데, 이는 **검색 서비스 기여자** 및 **검색 인덱스 데이터 기여자** 역할이 필요합니다(또는 키 기반 인증의 경우 <strong>기본 관리자 키</strong>가 필요하며, 조회 키는 아닙니다). RBAC를 사용할 수 없는 경우에만 **설정 > 키** 창을 열고 <strong>기본 관리자 키</strong>를 복사하세요.
4. 인덱스를 생성하고 데이터를 업로드한 후 검색을 수행하는 방법은 [빠른 시작 가이드](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) 페이지를 따르세요.

## 4단계: Azure AI Search 도구 사용하기

Azure AI Search는 다양한 도구와 통합되어 검색 기능을 향상시킵니다. 고급 구성 및 작업을 위해 Azure CLI, Python SDK, .NET SDK 및 기타 도구를 사용할 수 있습니다.

### Azure CLI 사용하기

1. [Azure CLI 설치](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691)의 지침에 따라 Azure CLI를 설치합니다.
2. 다음 명령어를 사용하여 Azure CLI에 로그인합니다:

   ```bash
   az login
   ```
3. **(권장) Microsoft Entra ID(RBAC)로 키 없는 액세스 활성화:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC이 활성화된 경우, 아래 Python 및 .NET SDK 샘플은 `DefaultAzureCredential`을 사용하여 인증하며, 이는 로컬 개발 중에 `az login` 세션을 사용하므로 관리자 키가 필요 없습니다. 자세한 내용은 [역할을 사용하여 Azure AI Search에 연결하기](https://learn.microsoft.com/azure/search/search-security-rbac)를 참조하세요.

4. **(보조) 키 기반 인증** — RBAC를 사용할 수 없는 경우에만 관리자 키를 저장하세요:

#### Azure AI Search 인스턴스의 엔드포인트와 API 키를 환경 변수에 저장하세요.

   * **zsh / bash**
     ```bash
     # az search service show has no "endpoint" field; build the URL from the service name.
     export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
     export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

   * **PowerShell**
     ```powershell
     # az search service show has no "endpoint" field; build the URL from the service name.
     $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
     $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

### Python SDK 사용하기

1. Azure Cognitive Search 클라이언트 라이브러리와 Azure Identity for Python을 설치합니다:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. 다음 Python 코드를 사용하여 인덱스를 생성하고 문서를 업로드합니다:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    # Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    credential = DefaultAzureCredential()
    # Fallback (key-based auth):
    # from azure.core.credentials import AzureKeyCredential
    # credential = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
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

1. 다음 명령어를 실행하여 인덱스를 생성하고 문서를 업로드합니다:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    아래 .NET 샘플은 `DefaultAzureCredential`을 사용하며, 이는 로컬 개발 중에 `az login`에서 Azure CLI 로그인 정보를 사용할 수 있습니다.

2. 다음은 `AzureSearch.cs`의 .NET 코드입니다:

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:package Azure.Identity@1.21.0
    #:property PublishAot=false

    using Azure;
    using Azure.Identity;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var indexName = "sample-index";

    // Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    // Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    var credential = new DefaultAzureCredential();
    // Fallback (key-based auth): the `using Azure;` directive above already imports
    // AzureKeyCredential; replace the credential line above with:
    // var credential = new AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!);
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

자세한 내용은 다음 문서를 참조하세요:

- [Azure Cognitive Search 서비스 만들기](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Azure Cognitive Search 시작하기](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search 도구](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 결론

Azure 포털과 통합 도구를 사용하여 Azure AI Search를 성공적으로 설정했습니다. 이제 Azure AI Search의 고급 기능과 기능을 탐색하여 검색 솔루션을 향상시킬 수 있습니다.

추가 도움이 필요하면 [Azure Cognitive Search 문서](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)를 방문하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->