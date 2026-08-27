# Hướng Dẫn Thiết Lập Azure AI Search

Hướng dẫn này sẽ giúp bạn thiết lập Azure AI Search bằng cách sử dụng cổng thông tin Azure. Hãy làm theo các bước dưới đây để tạo và cấu hình dịch vụ Azure AI Search của bạn.

## Yêu Cầu Trước

Trước khi bắt đầu, hãy đảm bảo bạn có những thứ sau:

- Một đăng ký Azure. Nếu bạn chưa có đăng ký Azure, bạn có thể tạo một tài khoản miễn phí tại [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Bước 1: Tạo Tài Khoản Lưu Trữ Azure

1. Thực hiện theo hướng dẫn này, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), để tạo một Tài Khoản Lưu Trữ Azure mới.
   **CHÚ Ý**: Đảm bảo loại Tài Khoản Lưu Trữ là Standard General Purpose V2.

## Bước 2: Tạo Dịch Vụ Azure AI Search

1. Đăng nhập vào [cổng thông tin Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Trong thanh điều hướng bên trái, nhấp vào **Create a resource**.
3. Trong hộp tìm kiếm, gõ "Azure AI Search" và chọn **Azure AI Search** từ danh sách kết quả.
4. Nhấp vào nút **Create**.
5. Trong tab **Basics**, cung cấp các thông tin sau:
   - **Subscription**: Chọn đăng ký Azure của bạn.
   - **Resource group**: Tạo nhóm tài nguyên mới hoặc chọn nhóm tài nguyên hiện có.
   - **Resource name**: Nhập tên duy nhất cho dịch vụ tìm kiếm của bạn.
   - **Region**: Chọn vùng gần nhất với người dùng của bạn.
   - **Pricing tier**: Chọn bậc giá phù hợp với yêu cầu của bạn. Bạn có thể bắt đầu với bậc Miễn phí để thử nghiệm.
6. Nhấp **Review + create**.
7. Xem lại các cài đặt và nhấp **Create** để tạo dịch vụ tìm kiếm.

## Bước 3: Bắt Đầu Với Azure AI Search

1. Khi việc triển khai hoàn tất, chuyển đến dịch vụ tìm kiếm của bạn trong cổng thông tin Azure.
2. Trong khung tổng quan dịch vụ tìm kiếm, sao chép URL. Nó sẽ trông như `https://<service-name>.search.windows.net`.
3. **(Khuyến nghị)** Bật truy cập không cần khóa với Microsoft Entra ID (RBAC) như trong Bước 4 bên dưới — không cần khóa. Các ví dụ trong hướng dẫn này tạo/cập nhật chỉ mục và tải tài liệu lên, đòi hỏi vai trò **Search Service Contributor** và **Search Index Data Contributor** (hoặc, khi dùng xác thực khóa, dùng **primary admin key** — không phải query key). Chỉ khi bạn không thể sử dụng RBAC, mở khung **Settings > Keys** và sao chép **primary admin key**.
4. Làm theo các bước trong trang [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) để tạo chỉ mục, tải dữ liệu và thực hiện tìm kiếm.

## Bước 4: Sử Dụng Công Cụ Azure AI Search

Azure AI Search tích hợp với nhiều công cụ khác nhau để nâng cao khả năng tìm kiếm của bạn. Bạn có thể sử dụng Azure CLI, Python SDK, .NET SDK và các công cụ khác để cấu hình và vận hành nâng cao.

### Sử Dụng Azure CLI

1. Cài đặt Azure CLI theo hướng dẫn tại [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Đăng nhập Azure CLI sử dụng lệnh:

   ```bash
   az login
   ```
3. **(Khuyến nghị) Bật truy cập không dùng khóa với Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # dịch vụ tìm kiếm az show không có trường "endpoint"; xây dựng URL từ tên dịch vụ.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Khi RBAC được bật, các ví dụ Python và .NET SDK bên dưới xác thực với `DefaultAzureCredential`, sử dụng phiên đăng nhập `az login` của bạn trong quá trình phát triển cục bộ — không cần khóa quản trị. Xem [Kết nối với Azure AI Search sử dụng vai trò](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Dự phòng) Xác thực dựa trên khóa** — chỉ khi bạn không thể sử dụng RBAC, lưu khóa quản trị như sau:

#### Lưu cả điểm kết và khóa API của instance Azure AI Search vào biến môi trường.

    ```bash
    # zsh/bash
    # lệnh az search service show không có trường "endpoint"; xây dựng URL từ tên dịch vụ.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # lệnh az search service show không có trường "endpoint"; xây dựng URL từ tên dịch vụ.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Sử Dụng Python SDK

1. Cài đặt thư viện khách hàng Azure Cognitive Search và Azure Identity cho Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Sử dụng đoạn mã Python sau để tạo chỉ mục và tải tài liệu lên:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Không cần khóa (khuyến nghị): sử dụng danh tính `az login` của bạn qua Entra ID RBAC.
    # Yêu cầu các vai trò "Người đóng góp Dịch vụ Tìm kiếm" và "Người đóng góp Dữ liệu Chỉ mục Tìm kiếm".
    credential = DefaultAzureCredential()
    # Dự phòng (xác thực dựa trên khóa):
    # từ azure.core.credentials nhập AzureKeyCredential
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

### Sử Dụng .NET SDK

1. Chạy lệnh sau để tạo chỉ mục và tải tài liệu lên:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Ví dụ .NET bên dưới sử dụng `DefaultAzureCredential`, có thể dùng đăng nhập Azure CLI của bạn từ `az login` trong quá trình phát triển cục bộ.

2. Đây là mã .NET của `AzureSearch.cs`:

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

Để biết thông tin chi tiết hơn, hãy tham khảo tài liệu sau:

- [Tạo dịch vụ Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Bắt đầu với Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Công cụ Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Kết Luận

Bạn đã thiết lập thành công Azure AI Search bằng cổng thông tin Azure và các công cụ tích hợp. Bạn có thể khám phá thêm các tính năng và khả năng nâng cao của Azure AI Search để cải thiện giải pháp tìm kiếm của mình.

Để được hỗ trợ thêm, hãy truy cập [tài liệu Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->