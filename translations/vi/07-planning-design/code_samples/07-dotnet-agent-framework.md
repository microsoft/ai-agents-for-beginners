# 🎯 Lập kế hoạch & Mẫu thiết kế với Azure OpenAI (Responses API) (.NET)

## 📋 Mục tiêu học tập

Nhật ký này trình bày các mẫu lập kế hoạch và thiết kế cấp doanh nghiệp để xây dựng các tác nhân thông minh sử dụng Microsoft Agent Framework trong .NET với Azure OpenAI (Responses API). Bạn sẽ học cách tạo các tác nhân có thể phân tích vấn đề phức tạp, lập kế hoạch giải pháp nhiều bước và thực thi các luồng công việc tinh vi với các tính năng doanh nghiệp của .NET.

## ⚙️ Yêu cầu & Cài đặt

**Môi trường phát triển:**
- .NET 9.0 SDK hoặc cao hơn
- Visual Studio 2022 hoặc VS Code với phần mở rộng C#
- Một đăng ký Azure với tài nguyên Azure OpenAI và triển khai mô hình
- Azure CLI — đăng nhập với `az login`

**Phụ thuộc cần thiết:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Cấu hình môi trường (file .env):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Chạy mã nguồn

Bài học này bao gồm triển khai ứng dụng đơn file .NET. Để chạy nó:

```bash
# Làm cho tập tin có thể thực thi được (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Chạy ứng dụng
./07-dotnet-agent-framework.cs
```

Hoặc sử dụng lệnh dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Triển khai mã nguồn

Triển khai hoàn chỉnh có trong `07-dotnet-agent-framework.cs`, trình bày:

- Tải cấu hình môi trường với DotNetEnv
- Cấu hình client Azure OpenAI cho Responses API
- Định nghĩa mô hình dữ liệu cấu trúc (Plan và TravelPlan) với trình tuần tự hóa JSON
- Tạo tác nhân AI với kết quả cấu trúc sử dụng JSON schema
- Thực thi các yêu cầu lập kế hoạch với phản hồi an toàn kiểu

## Khái niệm chính

### Lập kế hoạch cấu trúc với mô hình an toàn kiểu

Tác nhân sử dụng các lớp C# để định nghĩa cấu trúc đầu ra lập kế hoạch:

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

### JSON Schema cho kết quả cấu trúc

Tác nhân được cấu hình trả về phản hồi phù hợp với lược đồ TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Hướng dẫn lập kế hoạch cho tác nhân

Tác nhân hoạt động như người điều phối, giao nhiệm vụ cho các tác nhân phụ chuyên biệt:

- FlightBooking: Để đặt vé máy bay và cung cấp thông tin chuyến bay
- HotelBooking: Để đặt khách sạn và cung cấp thông tin khách sạn
- CarRental: Để đặt thuê xe và cung cấp thông tin thuê xe
- ActivitiesBooking: Để đặt hoạt động và cung cấp thông tin hoạt động
- DestinationInfo: Để cung cấp thông tin về điểm đến
- DefaultAgent: Để xử lý các yêu cầu chung

## Kết quả mong đợi

Khi bạn chạy tác nhân với yêu cầu lập kế hoạch du lịch, nó sẽ phân tích yêu cầu và tạo ra một kế hoạch cấu trúc với phân công nhiệm vụ thích hợp cho các tác nhân chuyên biệt, được định dạng dưới dạng JSON tuân theo lược đồ TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->