<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:26:29+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "vi"
}
-->
# 🛠️ Sử dụng Công cụ Nâng cao với Mô hình GitHub (.NET)

## 📋 Mục tiêu học tập

Notebook này trình bày các mẫu tích hợp công cụ cấp doanh nghiệp sử dụng Microsoft Agent Framework trong .NET với Mô hình GitHub. Bạn sẽ học cách xây dựng các agent phức tạp với nhiều công cụ chuyên biệt, tận dụng kiểu dữ liệu mạnh mẽ của C# và các tính năng doanh nghiệp của .NET.

**Các khả năng công cụ nâng cao bạn sẽ thành thạo:**
- 🔧 **Kiến trúc Đa Công cụ**: Xây dựng các agent với nhiều khả năng chuyên biệt
- 🎯 **Thực thi Công cụ An toàn Kiểu Dữ liệu**: Tận dụng kiểm tra tại thời điểm biên dịch của C#
- 📊 **Mẫu Công cụ Doanh nghiệp**: Thiết kế công cụ sẵn sàng cho sản xuất và xử lý lỗi
- 🔗 **Kết hợp Công cụ**: Kết hợp các công cụ cho quy trình công việc kinh doanh phức tạp

## 🎯 Lợi ích của Kiến trúc Công cụ .NET

### Tính năng Công cụ Doanh nghiệp
- **Kiểm tra tại thời điểm biên dịch**: Kiểu dữ liệu mạnh mẽ đảm bảo tính chính xác của tham số công cụ
- **Dependency Injection**: Tích hợp IoC container để quản lý công cụ
- **Mẫu Async/Await**: Thực thi công cụ không chặn với quản lý tài nguyên hợp lý
- **Ghi nhật ký có cấu trúc**: Tích hợp ghi nhật ký để giám sát thực thi công cụ

### Mẫu sẵn sàng cho sản xuất
- **Xử lý ngoại lệ**: Quản lý lỗi toàn diện với các ngoại lệ kiểu hóa
- **Quản lý tài nguyên**: Mẫu xử lý và quản lý bộ nhớ đúng cách
- **Giám sát hiệu suất**: Các chỉ số tích hợp và bộ đếm hiệu suất
- **Quản lý cấu hình**: Cấu hình an toàn kiểu dữ liệu với kiểm tra hợp lệ

## 🔧 Kiến trúc Kỹ thuật

### Thành phần Công cụ .NET Cốt lõi
- **Microsoft.Extensions.AI**: Lớp trừu tượng công cụ thống nhất
- **Microsoft.Agents.AI**: Điều phối công cụ cấp doanh nghiệp
- **Tích hợp Mô hình GitHub**: API client hiệu suất cao với kết nối pooling

### Quy trình Thực thi Công cụ
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Danh mục & Mẫu Công cụ

### 1. **Công cụ Xử lý Dữ liệu**
- **Kiểm tra đầu vào**: Kiểu dữ liệu mạnh mẽ với chú thích dữ liệu
- **Hoạt động chuyển đổi**: Chuyển đổi và định dạng dữ liệu an toàn kiểu dữ liệu
- **Logic Kinh doanh**: Công cụ tính toán và phân tích theo miền cụ thể
- **Định dạng đầu ra**: Tạo phản hồi có cấu trúc

### 2. **Công cụ Tích hợp**
- **Kết nối API**: Tích hợp dịch vụ RESTful với HttpClient
- **Công cụ Cơ sở dữ liệu**: Tích hợp Entity Framework để truy cập dữ liệu
- **Hoạt động Tệp**: Hoạt động hệ thống tệp an toàn với kiểm tra hợp lệ
- **Dịch vụ bên ngoài**: Mẫu tích hợp dịch vụ bên thứ ba

### 3. **Công cụ Tiện ích**
- **Xử lý văn bản**: Tiện ích thao tác và định dạng chuỗi
- **Hoạt động Ngày/Giờ**: Tính toán ngày/giờ theo văn hóa
- **Công cụ Toán học**: Tính toán chính xác và hoạt động thống kê
- **Công cụ Kiểm tra**: Kiểm tra quy tắc kinh doanh và xác minh dữ liệu

## ⚙️ Yêu cầu & Cài đặt

**Môi trường phát triển:**
- .NET 9.0 SDK hoặc cao hơn
- Visual Studio 2022 hoặc VS Code với extension C#
- Truy cập API Mô hình GitHub

**Các gói NuGet cần thiết:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Cấu hình môi trường (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Sẵn sàng xây dựng các agent cấp doanh nghiệp với khả năng công cụ mạnh mẽ, an toàn kiểu dữ liệu trong .NET? Hãy cùng kiến trúc những giải pháp chuyên nghiệp! 🏢⚡

## 💻 Triển khai Mã

Toàn bộ triển khai C# có sẵn trong tệp đi kèm `04-dotnet-agent-framework.cs`. Ứng dụng Đơn Tệp .NET này minh họa:

- Tải biến môi trường cho cấu hình Mô hình GitHub
- Định nghĩa công cụ tùy chỉnh sử dụng các phương thức C# với thuộc tính
- Tạo agent AI với tích hợp công cụ
- Quản lý luồng hội thoại
- Thực thi yêu cầu agent với gọi công cụ

Để chạy ví dụ:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Hoặc sử dụng .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.