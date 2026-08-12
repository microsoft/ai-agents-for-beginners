# 🤝 Hệ thống Quy trình làm việc Đa tác nhân Doanh nghiệp (.NET)

## 📋 Mục tiêu học tập

Sổ tay này trình bày cách xây dựng các hệ thống đa tác nhân chuẩn doanh nghiệp tinh vi sử dụng Microsoft Agent Framework trong .NET với Azure OpenAI (Responses API). Bạn sẽ học cách điều phối nhiều tác nhân chuyên biệt làm việc cùng nhau thông qua các quy trình làm việc có cấu trúc, tận dụng các tính năng doanh nghiệp của .NET để có các giải pháp sẵn sàng cho sản xuất.

**Khả năng đa tác nhân doanh nghiệp bạn sẽ xây dựng:**
- 👥 **Hợp tác tác nhân**: Điều phối tác nhân an toàn kiểu với xác thực tại thời điểm biên dịch
- 🔄 **Điều phối quy trình làm việc**: Định nghĩa quy trình làm việc khai báo với các mẫu async của .NET
- 🎭 **Chuyên môn vai trò**: Tính cách tác nhân kiểu mạnh và các lĩnh vực chuyên môn
- 🏢 **Tích hợp doanh nghiệp**: Các mẫu sẵn sàng cho sản xuất với giám sát và xử lý lỗi

## ⚙️ Yêu cầu & Cài đặt

**Môi trường phát triển:**
- .NET 9.0 SDK hoặc cao hơn
- Visual Studio 2022 hoặc VS Code với tiện ích mở rộng C#
- Đăng ký Azure (cho tác nhân liên tục)

**Gói NuGet yêu cầu:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## Ví dụ Mã

Mã hoàn chỉnh cho bài học này có trong tệp C# kèm theo: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Để chạy mẫu:

```bash
# Làm cho tệp có thể thực thi (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Chạy ví dụ
./08-dotnet-agent-framework.cs
```

Hoặc sử dụng .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Điều mẫu này minh họa

Hệ thống quy trình làm việc đa tác nhân này tạo dịch vụ đề xuất chuyến đi khách sạn với hai tác nhân chuyên biệt:

1. **Tác nhân FrontDesk**: Một tác nhân du lịch cung cấp đề xuất hoạt động và địa điểm
2. **Tác nhân Concierge**: Xem xét đề xuất để đảm bảo trải nghiệm chân thực, không mang tính du lịch phổ biến

Các tác nhân phối hợp trong quy trình làm việc nơi:
- Tác nhân FrontDesk nhận yêu cầu du lịch ban đầu
- Tác nhân Concierge xem xét và hoàn thiện đề xuất
- Quy trình làm việc phát trực tiếp phản hồi theo thời gian thực

## Khái niệm chính

### Điều phối Tác nhân
Mẫu minh họa điều phối tác nhân an toàn kiểu sử dụng Microsoft Agent Framework với xác thực lúc biên dịch.

### Điều phối Quy trình làm việc
Sử dụng định nghĩa quy trình làm việc khai báo với các mẫu async của .NET để kết nối nhiều tác nhân trong một quy trình.

### Phát trực tiếp Phản hồi
Triển khai phát trực tiếp phản hồi của tác nhân theo thời gian thực sử dụng async enumerable và kiến trúc hướng sự kiện.

### Tích hợp Doanh nghiệp
Minh họa các mẫu sẵn sàng cho sản xuất bao gồm:
- Cấu hình biến môi trường
- Quản lý chứng chỉ bảo mật
- Xử lý lỗi
- Xử lý sự kiện bất đồng bộ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->