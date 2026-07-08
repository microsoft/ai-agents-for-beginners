# 🔍 Enterprise RAG với Microsoft Foundry (.NET)

## 📋 Mục tiêu học tập

Notebook này trình bày cách xây dựng các hệ thống Retrieval-Augmented Generation (RAG) cấp doanh nghiệp sử dụng Microsoft Agent Framework trong .NET với Microsoft Foundry. Bạn sẽ học cách tạo các agent sẵn sàng cho sản xuất có thể tìm kiếm tài liệu và cung cấp câu trả lời chính xác, nhận biết ngữ cảnh với bảo mật và khả năng mở rộng cấp doanh nghiệp.

**Các khả năng RAG doanh nghiệp bạn sẽ xây dựng:**
- 📚 **Trí tuệ Tài liệu**: Xử lý tài liệu nâng cao với dịch vụ AI Azure
- 🔍 **Tìm kiếm Ngữ nghĩa**: Tìm kiếm vector hiệu năng cao với các tính năng doanh nghiệp
- 🛡️ **Tích hợp Bảo mật**: Kiểm soát truy cập theo vai trò và mẫu bảo vệ dữ liệu
- 🏢 **Kiến trúc Có thể mở rộng**: Hệ thống RAG sẵn sàng cho sản xuất với giám sát

## 🎯 Kiến trúc RAG Doanh nghiệp

### Các Thành phần Doanh nghiệp Cốt lõi
- **Microsoft Foundry**: Nền tảng AI doanh nghiệp được quản lý với bảo mật và tuân thủ
- **Persistent Agents**: Agent có trạng thái với lịch sử hội thoại và quản lý ngữ cảnh
- **Quản lý Vector Store**: Lập chỉ mục và truy xuất tài liệu cấp doanh nghiệp
- **Tích hợp Định danh**: Xác thực Azure AD và kiểm soát truy cập theo vai trò

### Lợi ích .NET Doanh nghiệp
- **An toàn kiểu dữ liệu**: Xác thực lúc biên dịch cho các thao tác RAG và cấu trúc dữ liệu
- **Hiệu năng Async**: Xử lý tài liệu và tìm kiếm không chặn
- **Quản lý Bộ nhớ**: Sử dụng tài nguyên hiệu quả cho bộ sưu tập tài liệu lớn
- **Mẫu Tích hợp**: Tích hợp dịch vụ Azure gốc với dependency injection

## 🏗️ Kiến trúc Kỹ thuật

### Pipeline RAG Doanh nghiệp
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Các Thành phần .NET Cốt lõi
- **Azure.AI.Agents.Persistent**: Quản lý agent doanh nghiệp với trạng thái bền vững
- **Azure.Identity**: Xác thực tích hợp cho truy cập dịch vụ Azure an toàn
- **Microsoft.Agents.AI.AzureAI**: Triển khai khung agent tối ưu cho Azure
- **System.Linq.Async**: Thao tác LINQ bất đồng bộ hiệu năng cao

## 🔧 Tính năng & Lợi ích Doanh nghiệp

### Bảo mật & Tuân thủ
- **Tích hợp Azure AD**: Quản lý định danh và xác thực doanh nghiệp
- **Truy cập theo Vai trò**: Quyền truy cập chi tiết cho tài liệu và thao tác
- **Bảo vệ Dữ liệu**: Mã hóa lúc lưu và truyền cho tài liệu nhạy cảm
- **Ghi nhật ký Kiểm toán**: Theo dõi hoạt động toàn diện cho yêu cầu tuân thủ

### Hiệu năng & Khả năng mở rộng
- **Pooling Kết nối**: Quản lý kết nối dịch vụ Azure hiệu quả
- **Xử lý Async**: Thao tác không chặn cho các kịch bản thông lượng cao
- **Chiến lược Caching**: Bộ nhớ đệm thông minh cho tài liệu truy cập thường xuyên
- **Cân bằng Tải**: Xử lý phân tán cho triển khai quy mô lớn

### Quản lý & Giám sát
- **Kiểm tra Sức khỏe**: Giám sát tích hợp cho các thành phần hệ thống RAG
- **Chỉ số Hiệu năng**: Phân tích chi tiết về chất lượng tìm kiếm và thời gian phản hồi
- **Xử lý Lỗi**: Quản lý ngoại lệ toàn diện với chính sách thử lại
- **Quản lý Cấu hình**: Cấu hình riêng môi trường với xác thực

## ⚙️ Yêu cầu & Thiết lập

**Môi trường Phát triển:**
- SDK .NET 9.0 hoặc cao hơn
- Visual Studio 2022 hoặc VS Code với phần mở rộng C#
- Đăng ký Azure với quyền truy cập Microsoft Foundry

**Gói NuGet Cần thiết:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Thiết lập Xác thực Azure:**
```bash
# Cài đặt Azure CLI và xác thực
az login
az account set --subscription "your-subscription-id"
```

**Cấu hình Môi trường:**
* Cấu hình Microsoft Foundry (được xử lý tự động qua Azure CLI)
* Đảm bảo bạn đã đăng nhập đúng đăng ký Azure

## 📊 Mẫu RAG Doanh nghiệp

### Mẫu Quản lý Tài liệu
- **Tải lên Hàng loạt**: Xử lý hiệu quả bộ sưu tập tài liệu lớn
- **Cập nhật Tăng dần**: Thêm và sửa đổi tài liệu theo thời gian thực
- **Kiểm soát Phiên bản**: Phiên bản hóa tài liệu và theo dõi thay đổi
- **Quản lý Metadata**: Thuộc tính tài liệu phong phú và phân loại

### Mẫu Tìm kiếm & Truy xuất
- **Tìm kiếm Lai**: Kết hợp tìm kiếm ngữ nghĩa và từ khóa để kết quả tối ưu
- **Tìm kiếm Có Phân đoạn**: Lọc đa chiều và phân loại
- **Điều chỉnh Độ liên quan**: Thuật toán điểm tùy chỉnh cho nhu cầu theo lĩnh vực
- **Xếp hạng Kết quả**: Xếp hạng nâng cao với tích hợp logic kinh doanh

### Mẫu Bảo mật
- **Bảo mật ở Mức Tài liệu**: Kiểm soát truy cập chi tiết theo từng tài liệu
- **Phân loại Dữ liệu**: Gán nhãn độ nhạy và bảo vệ tự động
- **Theo dõi Kiểm toán**: Ghi nhật ký toàn diện các thao tác RAG
- **Bảo vệ Quyền riêng tư**: Phát hiện và che dấu thông tin nhận dạng cá nhân (PII)

## 🔒 Tính năng Bảo mật Doanh nghiệp

### Xác thực & Ủy quyền
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

### Bảo vệ Dữ liệu
- **Mã hóa**: Mã hóa đầu cuối cho tài liệu và chỉ mục tìm kiếm
- **Kiểm soát Truy cập**: Tích hợp với Azure AD cho quyền người dùng và nhóm
- **Lưu trú Dữ liệu**: Kiểm soát vị trí địa lý dữ liệu để tuân thủ
- **Sao lưu & Phục hồi**: Khả năng sao lưu tự động và phục hồi thảm họa

## 📈 Tối ưu Hiệu năng

### Mẫu Xử lý Bất đồng bộ
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Quản lý Bộ nhớ
- **Xử lý Phát trực tiếp**: Xử lý tài liệu lớn không gây vấn đề bộ nhớ
- **Pooling Tài nguyên**: Tái sử dụng tài nguyên tốn kém hiệu quả
- **Thu gom Rác**: Mẫu cấp phát bộ nhớ tối ưu
- **Quản lý Kết nối**: Vòng đời kết nối dịch vụ Azure đúng cách

### Chiến lược Caching
- **Caching Truy vấn**: Lưu bộ nhớ đệm cho các tìm kiếm thực thi thường xuyên
- **Caching Tài liệu**: Bộ nhớ đệm trong bộ nhớ cho tài liệu nóng
- **Caching Chỉ mục**: Bộ nhớ đệm tối ưu cho chỉ mục vector
- **Caching Kết quả**: Bộ nhớ đệm thông minh cho các phản hồi được tạo

## 📊 Trường hợp Sử dụng Doanh nghiệp

### Quản lý Kiến thức
- **Wiki Doanh nghiệp**: Tìm kiếm thông minh qua cơ sở kiến thức công ty
- **Chính sách & Thủ tục**: Hướng dẫn tự động tuân thủ và quy trình
- **Tài liệu Đào tạo**: Hỗ trợ học tập và phát triển thông minh
- **Cơ sở Dữ liệu Nghiên cứu**: Hệ thống phân tích bài nghiên cứu và học thuật

### Hỗ trợ Khách hàng
- **Cơ sở Kiến thức Hỗ trợ**: Phản hồi dịch vụ khách hàng tự động
- **Tài liệu Sản phẩm**: Truy xuất thông tin sản phẩm thông minh
- **Hướng dẫn Khắc phục Sự cố**: Hỗ trợ giải quyết vấn đề theo ngữ cảnh
- **Hệ thống FAQ**: Tạo FAQ động từ bộ sưu tập tài liệu

### Tuân thủ Quy định
- **Phân tích Tài liệu Pháp lý**: Trí tuệ hợp đồng và tài liệu pháp lý
- **Giám sát Tuân thủ**: Kiểm tra tuân thủ quy định tự động
- **Đánh giá Rủi ro**: Phân tích và báo cáo rủi ro dựa trên tài liệu
- **Hỗ trợ Kiểm toán**: Khám phá tài liệu thông minh cho kiểm toán

## 🚀 Triển khai Sản xuất

### Giám sát & Quan sát
- **Application Insights**: Giám sát chi tiết điện tử và hiệu năng
- **Chỉ số Tùy chỉnh**: Theo dõi KPI và cảnh báo theo doanh nghiệp
- **Truy vết Phân tán**: Theo dõi yêu cầu đầu cuối qua các dịch vụ
- **Bảng điều khiển Sức khỏe**: Trực quan sức khỏe hệ thống và hiệu năng theo thời gian thực

### Khả năng mở rộng & Độ tin cậy
- **Tự động Mở rộng**: Tự động điều chỉnh quy mô dựa trên tải và chỉ số hiệu năng
- **Độ sẵn sàng cao**: Triển khai đa vùng với khả năng chuyển đổi dự phòng
- **Kiểm tra Tải**: Xác thực hiệu năng dưới điều kiện tải doanh nghiệp
- **Phục hồi Thảm họa**: Quy trình sao lưu và phục hồi tự động

Sẵn sàng xây dựng hệ thống RAG cấp doanh nghiệp có khả năng xử lý tài liệu nhạy cảm ở quy mô lớn? Hãy cùng kiến trúc các hệ thống kiến thức thông minh cho doanh nghiệp! 🏢📖✨

## Triển khai Code

Mẫu code hoạt động hoàn chỉnh cho bài học này có trong `05-dotnet-agent-framework.cs`.

Để chạy ví dụ:

```bash
# Làm cho script có thể thực thi được (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Chạy ứng dụng .NET Single File
./05-dotnet-agent-framework.cs
```

Hoặc chạy trực tiếp bằng `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Code trình bày:

1. **Cài đặt Gói**: Cài đặt các gói NuGet cần thiết cho Azure AI Agents
2. **Cấu hình Môi trường**: Tải cấu hình endpoint Microsoft Foundry và mô hình
3. **Tải Tài liệu Lên**: Tải tài liệu để xử lý RAG
4. **Tạo Vector Store**: Tạo kho vector cho tìm kiếm ngữ nghĩa
5. **Cấu hình Agent**: Thiết lập agent AI với khả năng tìm file
6. **Thực thi Truy vấn**: Thực hiện truy vấn trên tài liệu đã tải lên

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->