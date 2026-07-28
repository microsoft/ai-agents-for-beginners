# 🔍 RAG Doanh nghiệp với Microsoft Foundry (.NET)

## 📋 Mục Tiêu Học Tập

Sổ tay này trình bày cách xây dựng các hệ thống Tăng cường Truy xuất Thông tin (RAG) cấp doanh nghiệp sử dụng Microsoft Agent Framework trong .NET với Microsoft Foundry. Bạn sẽ học cách tạo các agent sẵn sàng sản xuất có thể tìm kiếm qua tài liệu và cung cấp câu trả lời chính xác, có ngữ cảnh với bảo mật và khả năng mở rộng cấp doanh nghiệp.

**Các Khả Năng RAG Doanh Nghiệp Bạn Sẽ Xây Dựng:**
- 📚 **Trí Thông Minh Tài Liệu**: Xử lý tài liệu nâng cao với dịch vụ Azure AI
- 🔍 **Tìm Kiếm Ngữ Nghĩa**: Tìm kiếm vector hiệu năng cao với các tính năng doanh nghiệp
- 🛡️ **Tích Hợp Bảo Mật**: Truy cập dựa trên vai trò và các mô hình bảo vệ dữ liệu
- 🏢 **Kiến Trúc Có Thể Mở Rộng**: Hệ thống RAG sẵn sàng sản xuất với giám sát

## 🎯 Kiến Trúc RAG Doanh Nghiệp

### Các Thành Phần Cốt Lõi Doanh Nghiệp
- **Microsoft Foundry**: Nền tảng AI doanh nghiệp được quản lý với bảo mật và tuân thủ
- **Agents Bền Vững**: Agents có trạng thái với lịch sử hội thoại và quản lý ngữ cảnh
- **Quản Lý Kho Vector**: Đánh chỉ mục và truy xuất tài liệu cấp doanh nghiệp
- **Tích Hợp Định Danh**: Xác thực Azure AD và kiểm soát truy cập dựa trên vai trò

### Lợi Ích .NET Doanh Nghiệp
- **An Toàn Kiểu Dữ Liệu**: Xác thực lúc biên dịch cho các thao tác và cấu trúc dữ liệu RAG
- **Hiệu Năng Bất Đồng Bộ**: Xử lý tài liệu và tìm kiếm không chặn
- **Quản Lý Bộ Nhớ**: Sử dụng hiệu quả tài nguyên cho bộ sưu tập tài liệu lớn
- **Mô Hình Tích Hợp**: Tích hợp dịch vụ Azure gốc với dependency injection

## 🏗️ Kiến Trúc Kỹ Thuật

### Chu Trình RAG Doanh Nghiệp
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Các Thành Phần .NET Cốt Lõi
- **Azure.AI.Agents.Persistent**: Quản lý agents doanh nghiệp với lưu trạng thái
- **Azure.Identity**: Xác thực tích hợp để truy cập dịch vụ Azure an toàn
- **Microsoft.Agents.AI.AzureAI**: Triển khai framework agent tối ưu cho Azure
- **System.Linq.Async**: Các thao tác LINQ bất đồng bộ hiệu năng cao

## 🔧 Tính Năng & Lợi Ích Doanh Nghiệp

### Bảo Mật & Tuân Thủ
- **Tích Hợp Azure AD**: Quản lý định danh và xác thực doanh nghiệp
- **Truy Cập Dựa Trên Vai Trò**: Phân quyền truy cập và thao tác trên tài liệu chi tiết
- **Bảo Vệ Dữ Liệu**: Mã hóa khi lưu và truyền tài liệu nhạy cảm
- **Ghi Nhật Ký Kiểm Toán**: Theo dõi hoạt động toàn diện để đáp ứng yêu cầu tuân thủ

### Hiệu Năng & Khả Năng Mở Rộng
- **Quản Lý Kết Nối**: Quản lý kết nối dịch vụ Azure hiệu quả
- **Xử Lý Bất Đồng Bộ**: Các thao tác không chặn cho các kịch bản băng thông cao
- **Chiến Lược Bộ Đệm**: Bộ đệm thông minh cho tài liệu truy cập thường xuyên
- **Cân Bằng Tải**: Xử lý phân tán cho triển khai quy mô lớn

### Quản Lý & Giám Sát
- **Kiểm Tra Sức Khỏe**: Giám sát tích hợp cho các thành phần hệ thống RAG
- **Chỉ Số Hiệu Năng**: Phân tích chi tiết về chất lượng tìm kiếm và thời gian phản hồi
- **Xử Lý Lỗi**: Quản lý ngoại lệ toàn diện với chính sách thử lại
- **Quản Lý Cấu Hình**: Cài đặt theo môi trường kèm xác thực

## ⚙️ Điều Kiện & Thiết Lập

**Môi Trường Phát Triển:**
- .NET 9.0 SDK trở lên
- Visual Studio 2022 hoặc VS Code với phần mở rộng C#
- Azure subscription có quyền truy cập Microsoft Foundry

**Gói NuGet Yêu Cầu:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Thiết Lập Xác Thực Azure:**
```bash
# Cài đặt Azure CLI và xác thực
az login
az account set --subscription "your-subscription-id"
```

**Cấu Hình Môi Trường:**
* Cấu hình Microsoft Foundry (tự động qua Azure CLI)
* Đảm bảo bạn đã xác thực vào subscription Azure chính xác

## 📊 Các Mô Hình RAG Doanh Nghiệp

### Mô Hình Quản Lý Tài Liệu
- **Tải Lên Hàng Loạt**: Xử lý hiệu quả bộ sưu tập tài liệu lớn
- **Cập Nhật Từng Phần**: Thêm và chỉnh sửa tài liệu theo thời gian thực
- **Kiểm Soát Phiên Bản**: Phiên bản hóa tài liệu và theo dõi thay đổi
- **Quản Lý Metadata**: Thuộc tính phong phú và phân loại tài liệu

### Mô Hình Tìm Kiếm & Truy Xuất
- **Tìm Kiếm Lai**: Kết hợp tìm kiếm ngữ nghĩa và từ khóa cho kết quả tối ưu
- **Tìm Kiếm Phân Lọc Đa Chiều**: Lọc và phân loại đa chiều
- **Tùy Chỉnh Độ Liên Quan**: Thuật toán điểm hóa tùy chỉnh cho nhu cầu đặc thù
- **Xếp Hạng Kết Quả**: Xếp hạng nâng cao tích hợp logic kinh doanh

### Mô Hình Bảo Mật
- **Bảo Mật Cấp Tài Liệu**: Kiểm soát truy cập chi tiết theo từng tài liệu
- **Phân Loại Dữ Liệu**: Gắn nhãn nhạy cảm và bảo vệ tự động
- **Dấu Vết Kiểm Toán**: Ghi nhật ký đầy đủ các thao tác RAG
- **Bảo Vệ Quyền Riêng Tư**: Phát hiện và làm mờ thông tin nhận dạng cá nhân (PII)

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
- **Kiểm Soát Truy Cập**: Tích hợp Azure AD cho quyền người dùng và nhóm
- **Dữ Liệu Lưu Trú**: Kiểm soát vị trí địa lý dữ liệu để tuân thủ
- **Sao Lưu & Khôi Phục**: Khả năng sao lưu tự động và phục hồi thảm họa

## 📈 Tối Ưu Hiệu Năng

### Mô Hình Xử Lý Bất Đồng Bộ
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Quản Lý Bộ Nhớ
- **Xử Lý Streaming**: Xử lý tài liệu lớn mà không gặp vấn đề bộ nhớ
- **Tái Sử Dụng Tài Nguyên**: Tái sử dụng hiệu quả tài nguyên đắt tiền
- **Thu Gom Rác**: Mô hình cấp phát bộ nhớ tối ưu
- **Quản Lý Kết Nối**: Vòng đời kết nối dịch vụ Azure đúng cách

### Chiến Lược Bộ Đệm
- **Bộ Đệm Truy Vấn**: Bộ đệm các truy vấn thực thi thường xuyên
- **Bộ Đệm Tài Liệu**: Bộ đệm trong bộ nhớ cho tài liệu nóng
- **Bộ Đệm Chỉ Mục**: Tối ưu bộ đệm vector index
- **Bộ Đệm Kết Quả**: Bộ đệm thông minh cho phản hồi được tạo

## 📊 Các Trường Hợp Sử Dụng Doanh Nghiệp

### Quản Lý Kiến Thức
- **Wiki Doanh Nghiệp**: Tìm kiếm thông minh qua các cơ sở kiến thức công ty
- **Chính Sách & Thủ Tục**: Hướng dẫn tuân thủ và thủ tục tự động
- **Tài Liệu Đào Tạo**: Hỗ trợ học tập và phát triển thông minh
- **Cơ Sở Dữ Liệu Nghiên Cứu**: Hệ thống phân tích bài báo học thuật và nghiên cứu

### Hỗ Trợ Khách Hàng
- **Cơ Sở Kiến Thức Hỗ Trợ**: Phản hồi dịch vụ khách hàng tự động
- **Tài Liệu Sản Phẩm**: Truy xuất thông tin sản phẩm thông minh
- **Hướng Dẫn Khắc Phục Sự Cố**: Hỗ trợ giải quyết vấn đề theo ngữ cảnh
- **Hệ Thống FAQ**: Tạo FAQ động từ bộ sưu tập tài liệu

### Tuân Thủ Quy Định
- **Phân Tích Tài Liệu Pháp Lý**: Trí tuệ hợp đồng và tài liệu pháp lý
- **Giám Sát Tuân Thủ**: Kiểm tra tự động tuân thủ quy định
- **Đánh Giá Rủi Ro**: Phân tích và báo cáo rủi ro dựa trên tài liệu
- **Hỗ Trợ Kiểm Toán**: Tìm kiếm tài liệu thông minh cho kiểm toán

## 🚀 Triển Khai Sản Xuất

### Giám Sát & Quan Sát
- **Application Insights**: Thu thập dữ liệu và giám sát hiệu năng chi tiết
- **Chỉ Số Tùy Chỉnh**: Theo dõi KPI và cảnh báo theo nghiệp vụ
- **Phân Tích Phân Tán**: Theo dõi yêu cầu đầu-cuối qua các dịch vụ
- **Bảng Điều Khiển Sức Khỏe**: Hiển thị trạng thái và hiệu năng hệ thống theo thời gian thực

### Khả Năng Mở Rộng & Độ Tin Cậy
- **Tự Động Mở Rộng**: Mở rộng tự động dựa trên tải và chỉ số hiệu năng
- **Sẵn Sàng Cao**: Triển khai đa vùng với khả năng chuyển đổi khi lỗi
- **Kiểm Tra Tải**: Xác nhận hiệu năng dưới điều kiện tải doanh nghiệp
- **Khôi Phục Thảm Họa**: Quy trình sao lưu và phục hồi tự động

Sẵn sàng xây dựng hệ thống RAG cấp doanh nghiệp có khả năng xử lý tài liệu nhạy cảm ở quy mô lớn? Hãy cùng kiến trúc các hệ thống kiến thức thông minh cho doanh nghiệp! 🏢📖✨

## Triển Khai Mã Nguồn

Mẫu mã nguồn hoàn chỉnh cho bài học này có trong `05-dotnet-agent-framework.cs`.

Để chạy ví dụ:

```bash
# Làm cho script có thể thực thi (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Chạy ứng dụng .NET Single File
./05-dotnet-agent-framework.cs
```

Hoặc dùng lệnh `dotnet run` trực tiếp:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Mã nguồn minh họa:

1. **Cài Đặt Gói**: Cài đặt các gói NuGet cần thiết cho Azure AI Agents
2. **Cấu Hình Môi Trường**: Tải endpoint và thiết lập mô hình Microsoft Foundry
3. **Tải Lên Tài Liệu**: Tải tài liệu cho xử lý RAG
4. **Tạo Kho Vector**: Tạo kho vector cho tìm kiếm ngữ nghĩa
5. **Cấu Hình Agent**: Thiết lập agent AI có khả năng tìm kiếm file
6. **Thực Thi Truy Vấn**: Thực thi truy vấn trên tài liệu đã tải lên

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->