<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:17:32+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "vi"
}
-->
# 🤝 Hệ thống quy trình làm việc đa tác nhân doanh nghiệp (.NET)

## 📋 Mục tiêu học tập

Notebook này hướng dẫn cách xây dựng các hệ thống đa tác nhân cấp doanh nghiệp phức tạp bằng Microsoft Agent Framework trong .NET với GitHub Models. Bạn sẽ học cách điều phối nhiều tác nhân chuyên biệt làm việc cùng nhau thông qua các quy trình làm việc có cấu trúc, tận dụng các tính năng doanh nghiệp của .NET để tạo ra các giải pháp sẵn sàng cho sản xuất.

**Các khả năng đa tác nhân doanh nghiệp bạn sẽ xây dựng:**
- 👥 **Hợp tác giữa các tác nhân**: Phối hợp tác nhân an toàn kiểu với xác thực thời gian biên dịch
- 🔄 **Điều phối quy trình làm việc**: Định nghĩa quy trình làm việc khai báo với các mẫu async của .NET
- 🎭 **Chuyên môn hóa vai trò**: Cá tính và lĩnh vực chuyên môn của tác nhân được định kiểu mạnh mẽ
- 🏢 **Tích hợp doanh nghiệp**: Các mẫu sẵn sàng cho sản xuất với giám sát và xử lý lỗi

## ⚙️ Yêu cầu & Cài đặt

**Môi trường phát triển:**
- .NET 9.0 SDK hoặc cao hơn
- Visual Studio 2022 hoặc VS Code với phần mở rộng C#
- Đăng ký Azure (cho các tác nhân lưu trữ)

**Các gói NuGet cần thiết:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Mẫu mã

Mã hoàn chỉnh cho bài học này có trong tệp C# đi kèm: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Để chạy mẫu:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Hoặc sử dụng .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Những gì mẫu này thể hiện

Hệ thống quy trình làm việc đa tác nhân này tạo ra một dịch vụ gợi ý du lịch khách sạn với hai tác nhân chuyên biệt:

1. **Tác nhân FrontDesk**: Một tác nhân du lịch cung cấp gợi ý về hoạt động và địa điểm
2. **Tác nhân Concierge**: Xem xét các gợi ý để đảm bảo trải nghiệm chân thực, không mang tính du lịch đại trà

Các tác nhân làm việc cùng nhau trong một quy trình làm việc nơi:
- Tác nhân FrontDesk nhận yêu cầu du lịch ban đầu
- Tác nhân Concierge xem xét và tinh chỉnh gợi ý
- Quy trình làm việc truyền phát phản hồi theo thời gian thực

## Các khái niệm chính

### Phối hợp tác nhân
Mẫu này thể hiện sự phối hợp tác nhân an toàn kiểu bằng Microsoft Agent Framework với xác thực thời gian biên dịch.

### Điều phối quy trình làm việc
Sử dụng định nghĩa quy trình làm việc khai báo với các mẫu async của .NET để kết nối nhiều tác nhân trong một pipeline.

### Truyền phát phản hồi
Thực hiện truyền phát phản hồi của tác nhân theo thời gian thực bằng cách sử dụng async enumerables và kiến trúc sự kiện.

### Tích hợp doanh nghiệp
Hiển thị các mẫu sẵn sàng cho sản xuất bao gồm:
- Cấu hình biến môi trường
- Quản lý thông tin đăng nhập an toàn
- Xử lý lỗi
- Xử lý sự kiện không đồng bộ

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính xác nhất. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.