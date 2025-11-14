<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:42:51+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "vi"
}
-->
# Hướng dẫn thiết lập Azure AI Search

Hướng dẫn này sẽ giúp bạn thiết lập Azure AI Search bằng cách sử dụng Azure portal. Làm theo các bước dưới đây để tạo và cấu hình dịch vụ Azure AI Search của bạn.

## Điều kiện tiên quyết

Trước khi bắt đầu, hãy đảm bảo bạn có những điều sau:

- Một đăng ký Azure. Nếu bạn chưa có đăng ký Azure, bạn có thể tạo tài khoản miễn phí tại [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Bước 1: Tạo tài khoản lưu trữ Azure

1. Làm theo hướng dẫn này, [Tạo tài khoản lưu trữ Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), để tạo một tài khoản lưu trữ Azure mới.  
   **NOTE**: Đảm bảo rằng loại tài khoản lưu trữ là Standard General Purpose V2.

## Bước 2: Tạo dịch vụ Azure AI Search

1. Đăng nhập vào [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Trong bảng điều hướng bên trái, nhấp vào **Create a resource**.
3. Trong hộp tìm kiếm, nhập "Azure AI Search" và chọn **Azure AI Search** từ danh sách kết quả.
4. Nhấp vào nút **Create**.
5. Trong tab **Basics**, cung cấp các thông tin sau:
   - **Subscription**: Chọn đăng ký Azure của bạn.
   - **Resource group**: Tạo một nhóm tài nguyên mới hoặc chọn một nhóm tài nguyên hiện có.
   - **Resource name**: Nhập một tên duy nhất cho dịch vụ tìm kiếm của bạn.
   - **Region**: Chọn khu vực gần nhất với người dùng của bạn.
   - **Pricing tier**: Chọn một cấp giá phù hợp với yêu cầu của bạn. Bạn có thể bắt đầu với cấp Free để thử nghiệm.
6. Nhấp vào **Review + create**.
7. Xem lại các cài đặt và nhấp vào **Create** để tạo dịch vụ tìm kiếm.

## Bước 3: Bắt đầu với Azure AI Search

1. Sau khi triển khai hoàn tất, điều hướng đến dịch vụ tìm kiếm của bạn trong Azure portal.
2. Trong bảng tổng quan dịch vụ tìm kiếm, sao chép URL. URL sẽ có dạng `https://<service-name>.search.windows.net`.
3. Trong Settings > Keys, sao chép query key.
4. Làm theo các bước trong trang [Hướng dẫn nhanh](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) để tạo một index, tải dữ liệu lên và thực hiện truy vấn tìm kiếm.

## Bước 4: Sử dụng các công cụ Azure AI Search

Azure AI Search tích hợp với nhiều công cụ khác nhau để nâng cao khả năng tìm kiếm của bạn. Bạn có thể sử dụng Azure CLI, Python SDK, .NET SDK và các công cụ khác để cấu hình và vận hành nâng cao.

### Sử dụng Azure CLI

1. Cài đặt Azure CLI bằng cách làm theo hướng dẫn tại [Cài đặt Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Đăng nhập vào Azure CLI bằng lệnh:

   ```bash
   az login
   ```

3. Lưu cả endpoint và API key của Azure AI Search instance vào các biến môi trường.

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

### Sử dụng Python SDK

1. Cài đặt thư viện khách Azure Cognitive Search cho Python:

   ```bash
   pip install azure-search-documents
   ```

2. Sử dụng đoạn mã Python sau để tạo một index và tải tài liệu lên:

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

### Sử dụng .NET SDK

1. Chạy lệnh sau để tạo một index và tải tài liệu lên:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Đây là mã .NET của `AzureSearch.cs`:

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

Để biết thêm thông tin chi tiết, tham khảo tài liệu sau:

- [Tạo dịch vụ Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Bắt đầu với Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Công cụ Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Kết luận

Bạn đã thiết lập thành công Azure AI Search bằng cách sử dụng Azure portal và các công cụ tích hợp. Bây giờ bạn có thể khám phá thêm các tính năng và khả năng nâng cao của Azure AI Search để cải thiện giải pháp tìm kiếm của mình.

Để được hỗ trợ thêm, hãy truy cập [Tài liệu Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.