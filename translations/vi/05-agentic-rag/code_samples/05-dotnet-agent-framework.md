<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:05:57+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "vi"
}
-->
# 🔍 RAG Doanh Nghiệp với Azure AI Foundry (.NET)

## 📋 Mục Tiêu Học Tập

Notebook này hướng dẫn cách xây dựng hệ thống Retrieval-Augmented Generation (RAG) cấp doanh nghiệp bằng Microsoft Agent Framework trong .NET với Azure AI Foundry. Bạn sẽ học cách tạo các agent sẵn sàng cho sản xuất, có khả năng tìm kiếm tài liệu và cung cấp câu trả lời chính xác, phù hợp với ngữ cảnh, đồng thời đảm bảo bảo mật và khả năng mở rộng cho doanh nghiệp.

**Các Tính Năng RAG Doanh Nghiệp Bạn Sẽ Xây Dựng:**
- 📚 **Trí Tuệ Tài Liệu**: Xử lý tài liệu nâng cao với dịch vụ Azure AI
- 🔍 **Tìm Kiếm Ngữ Nghĩa**: Tìm kiếm vector hiệu suất cao với các tính năng doanh nghiệp
- 🛡️ **Tích Hợp Bảo Mật**: Kiểm soát truy cập dựa trên vai trò và các mẫu bảo vệ dữ liệu
- 🏢 **Kiến Trúc Có Khả Năng Mở Rộng**: Hệ thống RAG sẵn sàng cho sản xuất với khả năng giám sát

## 🎯 Kiến Trúc RAG Doanh Nghiệp

### Các Thành Phần Cốt Lõi Doanh Nghiệp
- **Azure AI Foundry**: Nền tảng AI doanh nghiệp được quản lý với bảo mật và tuân thủ
- **Persistent Agents**: Các agent có trạng thái với lịch sử hội thoại và quản lý ngữ cảnh
- **Quản Lý Vector Store**: Lập chỉ mục và truy xuất tài liệu cấp doanh nghiệp
- **Tích Hợp Danh Tính**: Xác thực Azure AD và kiểm soát truy cập dựa trên vai trò

### Lợi Ích .NET Doanh Nghiệp
- **Kiểm Tra Kiểu**: Xác thực tại thời điểm biên dịch cho các hoạt động RAG và cấu trúc dữ liệu
- **Hiệu Suất Async**: Xử lý tài liệu và tìm kiếm không chặn
- **Quản Lý Bộ Nhớ**: Sử dụng tài nguyên hiệu quả cho các bộ sưu tập tài liệu lớn
- **Mẫu Tích Hợp**: Tích hợp dịch vụ Azure gốc với dependency injection

## 🏗️ Kiến Trúc Kỹ Thuật

### Pipeline RAG Doanh Nghiệp
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Các Thành Phần Cốt Lõi .NET
- **Azure.AI.Agents.Persistent**: Quản lý agent doanh nghiệp với trạng thái được lưu trữ
- **Azure.Identity**: Xác thực tích hợp để truy cập dịch vụ Azure an toàn
- **Microsoft.Agents.AI.AzureAI**: Triển khai framework agent tối ưu hóa cho Azure
- **System.Linq.Async**: Các hoạt động LINQ không đồng bộ hiệu suất cao

## 🔧 Tính Năng & Lợi Ích Doanh Nghiệp

### Bảo Mật & Tuân Thủ
- **Tích Hợp Azure AD**: Quản lý danh tính doanh nghiệp và xác thực
- **Truy Cập Dựa Trên Vai Trò**: Quyền chi tiết cho truy cập tài liệu và hoạt động
- **Bảo Vệ Dữ Liệu**: Mã hóa khi lưu trữ và truyền tải cho các tài liệu nhạy cảm
- **Ghi Nhật Ký Kiểm Toán**: Theo dõi hoạt động toàn diện để đáp ứng yêu cầu tuân thủ

### Hiệu Suất & Khả Năng Mở Rộng
- **Connection Pooling**: Quản lý kết nối dịch vụ Azure hiệu quả
- **Xử Lý Async**: Các hoạt động không chặn cho các kịch bản thông lượng cao
- **Chiến Lược Caching**: Bộ nhớ đệm thông minh cho các tài liệu được truy cập thường xuyên
- **Cân Bằng Tải**: Xử lý phân tán cho các triển khai quy mô lớn

### Quản Lý & Giám Sát
- **Kiểm Tra Sức Khỏe**: Giám sát tích hợp cho các thành phần hệ thống RAG
- **Chỉ Số Hiệu Suất**: Phân tích chi tiết về chất lượng tìm kiếm và thời gian phản hồi
- **Xử Lý Lỗi**: Quản lý ngoại lệ toàn diện với các chính sách retry
- **Quản Lý Cấu Hình**: Cài đặt cụ thể theo môi trường với xác thực

## ⚙️ Yêu Cầu & Cài Đặt

**Môi Trường Phát Triển:**
- .NET 9.0 SDK hoặc cao hơn
- Visual Studio 2022 hoặc VS Code với extension C#
- Tài khoản Azure với quyền truy cập AI Foundry

**Các Gói NuGet Yêu Cầu:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Cài Đặt Xác Thực Azure:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Cấu Hình Môi Trường:**
* Cấu hình Azure AI Foundry (được xử lý tự động qua Azure CLI)
* Đảm bảo bạn đã xác thực vào tài khoản Azure chính xác

## 📊 Mẫu RAG Doanh Nghiệp

### Mẫu Quản Lý Tài Liệu
- **Tải Lên Hàng Loạt**: Xử lý hiệu quả các bộ sưu tập tài liệu lớn
- **Cập Nhật Từng Phần**: Thêm và sửa đổi tài liệu theo thời gian thực
- **Kiểm Soát Phiên Bản**: Quản lý phiên bản tài liệu và theo dõi thay đổi
- **Quản Lý Metadata**: Thuộc tính tài liệu phong phú và phân loại

### Mẫu Tìm Kiếm & Truy Xuất
- **Tìm Kiếm Kết Hợp**: Kết hợp tìm kiếm ngữ nghĩa và từ khóa để đạt kết quả tối ưu
- **Tìm Kiếm Theo Khía Cạnh**: Lọc và phân loại đa chiều
- **Điều Chỉnh Độ Liên Quan**: Thuật toán chấm điểm tùy chỉnh cho nhu cầu cụ thể của lĩnh vực
- **Xếp Hạng Kết Quả**: Xếp hạng nâng cao với tích hợp logic kinh doanh

### Mẫu Bảo Mật
- **Bảo Mật Cấp Tài Liệu**: Kiểm soát truy cập chi tiết theo từng tài liệu
- **Phân Loại Dữ Liệu**: Gắn nhãn nhạy cảm tự động và bảo vệ
- **Dấu Vết Kiểm Toán**: Ghi nhật ký toàn diện cho tất cả các hoạt động RAG
- **Bảo Vệ Quyền Riêng Tư**: Phát hiện và che giấu thông tin cá nhân (PII)

## 🔒 Tính Năng Bảo Mật Doanh Nghiệp

### Xác Thực & Ủy Quyền
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### Bảo Vệ Dữ Liệu
- **Mã Hóa**: Mã hóa đầu cuối cho tài liệu và chỉ mục tìm kiếm
- **Kiểm Soát Truy Cập**: Tích hợp với Azure AD cho quyền người dùng và nhóm
- **Vị Trí Dữ Liệu**: Kiểm soát vị trí địa lý của dữ liệu để tuân thủ
- **Sao Lưu & Phục Hồi**: Khả năng sao lưu và phục hồi tự động

## 📈 Tối Ưu Hiệu Suất

### Mẫu Xử Lý Async
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Quản Lý Bộ Nhớ
- **Xử Lý Streaming**: Xử lý tài liệu lớn mà không gặp vấn đề về bộ nhớ
- **Tái Sử Dụng Tài Nguyên**: Sử dụng hiệu quả các tài nguyên đắt đỏ
- **Thu Gom Rác**: Mẫu phân bổ bộ nhớ tối ưu
- **Quản Lý Kết Nối**: Vòng đời kết nối dịch vụ Azure hợp lý

### Chiến Lược Caching
- **Caching Truy Vấn**: Bộ nhớ đệm cho các tìm kiếm được thực hiện thường xuyên
- **Caching Tài Liệu**: Bộ nhớ đệm trong bộ nhớ cho các tài liệu nóng
- **Caching Chỉ Mục**: Bộ nhớ đệm chỉ mục vector tối ưu
- **Caching Kết Quả**: Bộ nhớ đệm thông minh cho các câu trả lời được tạo

## 📊 Các Trường Hợp Sử Dụng Doanh Nghiệp

### Quản Lý Kiến Thức
- **Wiki Công Ty**: Tìm kiếm thông minh trong cơ sở kiến thức của công ty
- **Chính Sách & Quy Trình**: Hướng dẫn tuân thủ và quy trình tự động
- **Tài Liệu Đào Tạo**: Hỗ trợ học tập và phát triển thông minh
- **Cơ Sở Dữ Liệu Nghiên Cứu**: Hệ thống phân tích bài báo học thuật và nghiên cứu

### Hỗ Trợ Khách Hàng
- **Cơ Sở Kiến Thức Hỗ Trợ**: Phản hồi dịch vụ khách hàng tự động
- **Tài Liệu Sản Phẩm**: Truy xuất thông tin sản phẩm thông minh
- **Hướng Dẫn Khắc Phục Sự Cố**: Hỗ trợ giải quyết vấn đề theo ngữ cảnh
- **Hệ Thống FAQ**: Tạo FAQ động từ các bộ sưu tập tài liệu

### Tuân Thủ Quy Định
- **Phân Tích Tài Liệu Pháp Lý**: Trí tuệ hợp đồng và tài liệu pháp lý
- **Giám Sát Tuân Thủ**: Kiểm tra tuân thủ quy định tự động
- **Đánh Giá Rủi Ro**: Phân tích và báo cáo rủi ro dựa trên tài liệu
- **Hỗ Trợ Kiểm Toán**: Khám phá tài liệu thông minh cho kiểm toán

## 🚀 Triển Khai Sản Xuất

### Giám Sát & Khả Năng Quan Sát
- **Application Insights**: Giám sát chi tiết về hiệu suất và telemetry
- **Chỉ Số Tùy Chỉnh**: Theo dõi KPI cụ thể của doanh nghiệp và cảnh báo
- **Tracing Phân Tán**: Theo dõi yêu cầu từ đầu đến cuối qua các dịch vụ
- **Bảng Điều Khiển Sức Khỏe**: Hình ảnh hóa sức khỏe và hiệu suất hệ thống theo thời gian thực

### Khả Năng Mở Rộng & Độ Tin Cậy
- **Tự Động Mở Rộng**: Mở rộng tự động dựa trên tải và chỉ số hiệu suất
- **Khả Năng Sẵn Sàng Cao**: Triển khai đa vùng với khả năng chuyển đổi dự phòng
- **Kiểm Tra Tải**: Xác thực hiệu suất dưới điều kiện tải doanh nghiệp
- **Phục Hồi Thảm Họa**: Quy trình sao lưu và phục hồi tự động

Sẵn sàng xây dựng hệ thống RAG cấp doanh nghiệp có thể xử lý tài liệu nhạy cảm ở quy mô lớn? Hãy cùng kiến trúc hệ thống kiến thức thông minh cho doanh nghiệp! 🏢📖✨

## Triển Khai Mã

Mẫu mã hoàn chỉnh cho bài học này có sẵn trong `05-dotnet-agent-framework.cs`. 

Để chạy ví dụ:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Hoặc sử dụng `dotnet run` trực tiếp:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Mã này minh họa:

1. **Cài Đặt Gói**: Cài đặt các gói NuGet cần thiết cho Azure AI Agents
2. **Cấu Hình Môi Trường**: Tải điểm cuối Azure AI Foundry và cài đặt mô hình
3. **Tải Lên Tài Liệu**: Tải lên tài liệu để xử lý RAG
4. **Tạo Vector Store**: Tạo vector store cho tìm kiếm ngữ nghĩa
5. **Cấu Hình Agent**: Thiết lập agent AI với khả năng tìm kiếm tài liệu
6. **Thực Thi Truy Vấn**: Chạy truy vấn trên tài liệu đã tải lên

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.