<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:38:27+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "vi"
}
-->
# Hướng Dẫn Cài Đặt Azure AI Search

Hướng dẫn này sẽ giúp bạn thiết lập Azure AI Search thông qua cổng thông tin Azure. Hãy làm theo các bước dưới đây để tạo và cấu hình dịch vụ Azure AI Search của bạn.

## Yêu Cầu Trước Khi Bắt Đầu

Trước khi bắt đầu, hãy đảm bảo bạn có những điều sau:

- Một tài khoản Azure. Nếu bạn chưa có tài khoản Azure, bạn có thể tạo tài khoản miễn phí tại [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Bước 1: Tạo Dịch Vụ Azure AI Search

1. Đăng nhập vào [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Trong thanh điều hướng bên trái, nhấp vào **Create a resource**.
3. Trong ô tìm kiếm, nhập "Azure AI Search" và chọn **Azure AI Search** từ danh sách kết quả.
4. Nhấn nút **Create**.
5. Trong tab **Basics**, cung cấp các thông tin sau:
   - **Subscription**: Chọn tài khoản Azure của bạn.
   - **Resource group**: Tạo nhóm tài nguyên mới hoặc chọn nhóm đã có.
   - **Resource name**: Nhập tên duy nhất cho dịch vụ tìm kiếm của bạn.
   - **Region**: Chọn khu vực gần người dùng của bạn nhất.
   - **Pricing tier**: Chọn gói giá phù hợp với nhu cầu. Bạn có thể bắt đầu với gói Free để thử nghiệm.
6. Nhấn **Review + create**.
7. Kiểm tra lại các thiết lập và nhấn **Create** để tạo dịch vụ tìm kiếm.

## Bước 2: Bắt Đầu Với Azure AI Search

1. Khi việc triển khai hoàn tất, điều hướng đến dịch vụ tìm kiếm của bạn trong Azure portal.
2. Trên trang tổng quan dịch vụ tìm kiếm, nhấn nút **Quickstart**.
3. Làm theo các bước trong hướng dẫn Quickstart để tạo chỉ mục, tải dữ liệu lên và thực hiện truy vấn tìm kiếm.

### Tạo Chỉ Mục

1. Trong hướng dẫn Quickstart, nhấn vào **Create an index**.
2. Định nghĩa cấu trúc chỉ mục bằng cách xác định các trường và thuộc tính của chúng (ví dụ: kiểu dữ liệu, có thể tìm kiếm, có thể lọc).
3. Nhấn **Create** để tạo chỉ mục.

### Tải Dữ Liệu Lên

1. Trong hướng dẫn Quickstart, nhấn vào **Upload data**.
2. Chọn nguồn dữ liệu (ví dụ: Azure Blob Storage, Azure SQL Database) và cung cấp các thông tin kết nối cần thiết.
3. Ánh xạ các trường dữ liệu nguồn với các trường trong chỉ mục.
4. Nhấn **Submit** để tải dữ liệu lên chỉ mục.

### Thực Hiện Truy Vấn Tìm Kiếm

1. Trong hướng dẫn Quickstart, nhấn vào **Search explorer**.
2. Nhập truy vấn tìm kiếm vào ô tìm kiếm để kiểm tra chức năng tìm kiếm.
3. Xem lại kết quả tìm kiếm và điều chỉnh cấu trúc chỉ mục hoặc dữ liệu nếu cần.

## Bước 3: Sử Dụng Công Cụ Azure AI Search

Azure AI Search tích hợp với nhiều công cụ khác nhau để nâng cao khả năng tìm kiếm của bạn. Bạn có thể sử dụng Azure CLI, Python SDK và các công cụ khác để cấu hình và vận hành nâng cao.

### Sử Dụng Azure CLI

1. Cài đặt Azure CLI theo hướng dẫn tại [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Đăng nhập vào Azure CLI bằng lệnh:
   ```bash
   az login
   ```
3. Tạo dịch vụ tìm kiếm mới bằng Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Tạo chỉ mục bằng Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Sử Dụng Python SDK

1. Cài đặt thư viện Azure Cognitive Search client cho Python:
   ```bash
   pip install azure-search-documents
   ```
2. Sử dụng đoạn mã Python sau để tạo chỉ mục và tải tài liệu lên:
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

Để biết thêm chi tiết, tham khảo tài liệu sau:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Kết Luận

Bạn đã thiết lập thành công Azure AI Search thông qua Azure portal và các công cụ tích hợp. Bây giờ bạn có thể khám phá thêm các tính năng và khả năng nâng cao của Azure AI Search để cải thiện giải pháp tìm kiếm của mình.

Nếu cần hỗ trợ thêm, hãy truy cập [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.