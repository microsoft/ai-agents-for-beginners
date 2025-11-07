<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:49:25+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "vi"
}
-->
# 🎨 Mẫu Thiết Kế Tác Nhân với GitHub Models (.NET)

## 📋 Mục Tiêu Học Tập

Notebook này trình bày các mẫu thiết kế cấp doanh nghiệp để xây dựng các tác nhân thông minh sử dụng Microsoft Agent Framework trong .NET với tích hợp GitHub Models. Bạn sẽ học các mẫu chuyên nghiệp và cách tiếp cận kiến trúc giúp các tác nhân sẵn sàng cho sản xuất, dễ bảo trì và có khả năng mở rộng.

**Mẫu Thiết Kế Doanh Nghiệp:**
- 🏭 **Factory Pattern**: Tạo tác nhân chuẩn hóa với dependency injection
- 🔧 **Builder Pattern**: Cấu hình và thiết lập tác nhân một cách linh hoạt
- 🧵 **Thread-Safe Patterns**: Quản lý hội thoại đồng thời
- 📋 **Repository Pattern**: Quản lý công cụ và khả năng một cách có tổ chức

## 🎯 Lợi Ích Kiến Trúc Đặc Thù .NET

### Tính Năng Doanh Nghiệp
- **Strong Typing**: Xác thực tại thời điểm biên dịch và hỗ trợ IntelliSense
- **Dependency Injection**: Tích hợp container DI sẵn có
- **Quản Lý Cấu Hình**: Các mẫu IConfiguration và Options
- **Async/Await**: Hỗ trợ lập trình bất đồng bộ hàng đầu

### Mẫu Sẵn Sàng Cho Sản Xuất
- **Tích Hợp Logging**: Hỗ trợ ILogger và logging có cấu trúc
- **Kiểm Tra Sức Khỏe**: Giám sát và chẩn đoán tích hợp
- **Xác Thực Cấu Hình**: Strong typing với chú thích dữ liệu
- **Xử Lý Lỗi**: Quản lý ngoại lệ có cấu trúc

## 🔧 Kiến Trúc Kỹ Thuật

### Thành Phần Cốt Lõi .NET
- **Microsoft.Extensions.AI**: Các trừu tượng dịch vụ AI thống nhất
- **Microsoft.Agents.AI**: Framework điều phối tác nhân cấp doanh nghiệp
- **Tích Hợp GitHub Models**: Các mẫu client API hiệu suất cao
- **Hệ Thống Cấu Hình**: Tích hợp appsettings.json và môi trường

### Triển Khai Mẫu Thiết Kế
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Các Mẫu Doanh Nghiệp Được Minh Họa

### 1. **Mẫu Tạo**
- **Agent Factory**: Tạo tác nhân tập trung với cấu hình nhất quán
- **Builder Pattern**: API linh hoạt cho cấu hình tác nhân phức tạp
- **Singleton Pattern**: Quản lý tài nguyên và cấu hình chia sẻ
- **Dependency Injection**: Giảm sự phụ thuộc và dễ kiểm thử

### 2. **Mẫu Hành Vi**
- **Strategy Pattern**: Các chiến lược thực thi công cụ có thể thay đổi
- **Command Pattern**: Các thao tác tác nhân được đóng gói với undo/redo
- **Observer Pattern**: Quản lý vòng đời tác nhân dựa trên sự kiện
- **Template Method**: Quy trình thực thi tác nhân được chuẩn hóa

### 3. **Mẫu Cấu Trúc**
- **Adapter Pattern**: Lớp tích hợp API GitHub Models
- **Decorator Pattern**: Nâng cao khả năng của tác nhân
- **Facade Pattern**: Giao diện tương tác tác nhân đơn giản hóa
- **Proxy Pattern**: Tải chậm và caching để cải thiện hiệu suất

## ⚙️ Yêu Cầu & Thiết Lập

**Môi Trường Phát Triển:**
- .NET 9.0 SDK hoặc cao hơn
- Visual Studio 2022 hoặc VS Code với extension C#
- Truy cập API GitHub Models

**Phụ Thuộc NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Cấu Hình (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 Nguyên Tắc Thiết Kế .NET

### Nguyên Tắc SOLID
- **Single Responsibility**: Mỗi thành phần có một mục đích rõ ràng
- **Open/Closed**: Có thể mở rộng mà không cần sửa đổi
- **Liskov Substitution**: Triển khai công cụ dựa trên giao diện
- **Interface Segregation**: Các giao diện tập trung, mạch lạc
- **Dependency Inversion**: Phụ thuộc vào trừu tượng, không phải cụ thể

### Kiến Trúc Sạch
- **Domain Layer**: Các trừu tượng cốt lõi của tác nhân và công cụ
- **Application Layer**: Điều phối tác nhân và quy trình làm việc
- **Infrastructure Layer**: Tích hợp GitHub Models và các dịch vụ bên ngoài
- **Presentation Layer**: Tương tác người dùng và định dạng phản hồi

## 🔒 Cân Nhắc Doanh Nghiệp

### Bảo Mật
- **Quản Lý Thông Tin Đăng Nhập**: Xử lý khóa API an toàn với IConfiguration
- **Xác Thực Đầu Vào**: Strong typing và xác thực chú thích dữ liệu
- **Lọc Kết Quả**: Xử lý và lọc phản hồi an toàn
- **Logging Kiểm Toán**: Theo dõi hoạt động toàn diện

### Hiệu Suất
- **Mẫu Async**: Các thao tác I/O không chặn
- **Connection Pooling**: Quản lý client HTTP hiệu quả
- **Caching**: Caching phản hồi để cải thiện hiệu suất
- **Quản Lý Tài Nguyên**: Các mẫu xử lý và dọn dẹp đúng cách

### Khả Năng Mở Rộng
- **Thread Safety**: Hỗ trợ thực thi tác nhân đồng thời
- **Resource Pooling**: Sử dụng tài nguyên hiệu quả
- **Quản Lý Tải**: Giới hạn tốc độ và xử lý áp lực ngược
- **Giám Sát**: Các chỉ số hiệu suất và kiểm tra sức khỏe

## 🚀 Triển Khai Sản Xuất

- **Quản Lý Cấu Hình**: Cài đặt cụ thể theo môi trường
- **Chiến Lược Logging**: Logging có cấu trúc với ID tương quan
- **Xử Lý Lỗi**: Xử lý ngoại lệ toàn cầu với khôi phục phù hợp
- **Giám Sát**: Application insights và bộ đếm hiệu suất
- **Kiểm Thử**: Các mẫu kiểm thử đơn vị, kiểm thử tích hợp và kiểm thử tải

Sẵn sàng xây dựng các tác nhân thông minh cấp doanh nghiệp với .NET? Hãy cùng kiến trúc một thứ gì đó mạnh mẽ! 🏢✨

## Mẫu Code

Để xem ví dụ hoàn chỉnh, hãy xem [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.