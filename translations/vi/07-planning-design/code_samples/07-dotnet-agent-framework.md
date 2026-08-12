# 🎯 Lập Kế Hoạch & Mẫu Thiết Kế với Azure OpenAI (Responses API) (.NET)

## 📋 Mục Tiêu Học Tập

Sổ tay này trình bày các mẫu thiết kế và lập kế hoạch cấp doanh nghiệp để xây dựng các đại lý thông minh sử dụng Microsoft Agent Framework trong .NET với Azure OpenAI (Responses API). Bạn sẽ học cách tạo đại lý có thể phân rã các vấn đề phức tạp, lập kế hoạch các giải pháp nhiều bước, và thực thi các quy trình phức tạp với các tính năng doanh nghiệp của .NET.

## ⚙️ Yêu Cầu & Cài Đặt

**Môi Trường Phát Triển:**
- SDK .NET 9.0 trở lên
- Visual Studio 2022 hoặc VS Code với tiện ích mở rộng C#
- Một thuê bao Azure với tài nguyên Azure OpenAI và một triển khai mô hình
- Azure CLI — đăng nhập với `az login`

**Phụ Thuộc Cần Thiết:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Cấu Hình Môi Trường (tệp .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Chạy Mã Nguồn

Bài học này bao gồm một ứng dụng đơn tệp .NET. Để chạy nó:

```bash
# Đặt file thành có thể thực thi (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Chạy ứng dụng
./07-dotnet-agent-framework.cs
```

Hoặc dùng lệnh dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Triển Khai Mã Nguồn

Triển khai đầy đủ có trong `07-dotnet-agent-framework.cs`, trình bày:

- Tải cấu hình môi trường với DotNetEnv
- Cấu hình khách hàng Azure OpenAI và tạo đại lý AI sử dụng `GetChatClient().AsAIAgent()`
- Định nghĩa mô hình dữ liệu có cấu trúc (Plan và TravelPlan) với tuần tự JSON
- Tạo đại lý AI có đầu ra có cấu trúc sử dụng JSON schema
- Thực thi các yêu cầu lập kế hoạch với phản hồi kiểu an toàn

## Khái Niệm Chính

### Lập Kế Hoạch Có Cấu Trúc với Mô Hình Kiểu An Toàn

Đại lý sử dụng các lớp C# để định nghĩa cấu trúc đầu ra kế hoạch:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### JSON Schema cho Đầu Ra Có Cấu Trúc

Đại lý được cấu hình để trả về phản hồi khớp với schema TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Hướng Dẫn Đại Lý Lập Kế Hoạch

Đại lý đóng vai trò điều phối viên, phân công nhiệm vụ cho các đại lý phụ chuyên biệt:

- FlightBooking: Đặt vé máy bay và cung cấp thông tin chuyến bay
- HotelBooking: Đặt phòng khách sạn và cung cấp thông tin khách sạn
- CarRental: Đặt thuê xe và cung cấp thông tin thuê xe
- ActivitiesBooking: Đặt các hoạt động và cung cấp thông tin hoạt động
- DestinationInfo: Cung cấp thông tin về điểm đến
- DefaultAgent: Xử lý các yêu cầu chung

## Kết Quả Mong Đợi

Khi bạn chạy đại lý với một yêu cầu lập kế hoạch du lịch, nó sẽ phân tích yêu cầu và tạo ra kế hoạch có cấu trúc với việc phân công nhiệm vụ thích hợp cho các đại lý chuyên biệt, được định dạng dưới dạng JSON phù hợp với schema TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->