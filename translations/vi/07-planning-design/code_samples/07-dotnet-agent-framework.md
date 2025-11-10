<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:58:23+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "vi"
}
-->
# 🎯 Lập kế hoạch & Mẫu thiết kế với GitHub Models (.NET)

## 📋 Mục tiêu học tập

Notebook này trình bày các mẫu lập kế hoạch và thiết kế cấp doanh nghiệp để xây dựng các tác nhân thông minh sử dụng Microsoft Agent Framework trong .NET với GitHub Models. Bạn sẽ học cách tạo các tác nhân có khả năng phân tích các vấn đề phức tạp, lập kế hoạch giải pháp nhiều bước và thực hiện các quy trình làm việc tinh vi với các tính năng doanh nghiệp của .NET.

## ⚙️ Yêu cầu & Cài đặt

**Môi trường phát triển:**
- .NET 9.0 SDK hoặc cao hơn
- Visual Studio 2022 hoặc VS Code với phần mở rộng C#
- Quyền truy cập API GitHub Models

**Các phụ thuộc cần thiết:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Cấu hình môi trường (tệp .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Chạy mã

Bài học này bao gồm một triển khai ứng dụng tệp đơn .NET. Để chạy:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Hoặc sử dụng lệnh dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Triển khai mã

Triển khai đầy đủ có sẵn trong `07-dotnet-agent-framework.cs`, minh họa:

- Tải cấu hình môi trường với DotNetEnv
- Cấu hình client OpenAI cho GitHub Models
- Định nghĩa các mô hình dữ liệu có cấu trúc (Plan và TravelPlan) với JSON serialization
- Tạo một tác nhân AI với đầu ra có cấu trúc sử dụng JSON schema
- Thực hiện các yêu cầu lập kế hoạch với phản hồi an toàn kiểu dữ liệu

## Các khái niệm chính

### Lập kế hoạch có cấu trúc với mô hình an toàn kiểu dữ liệu

Tác nhân sử dụng các lớp C# để định nghĩa cấu trúc của các đầu ra lập kế hoạch:

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

### JSON Schema cho đầu ra có cấu trúc

Tác nhân được cấu hình để trả về các phản hồi phù hợp với schema TravelPlan:

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

### Hướng dẫn cho tác nhân lập kế hoạch

Tác nhân hoạt động như một điều phối viên, phân công nhiệm vụ cho các tác nhân phụ chuyên biệt:

- FlightBooking: Đặt vé máy bay và cung cấp thông tin chuyến bay
- HotelBooking: Đặt phòng khách sạn và cung cấp thông tin khách sạn
- CarRental: Đặt thuê xe và cung cấp thông tin thuê xe
- ActivitiesBooking: Đặt các hoạt động và cung cấp thông tin hoạt động
- DestinationInfo: Cung cấp thông tin về điểm đến
- DefaultAgent: Xử lý các yêu cầu chung

## Kết quả mong đợi

Khi bạn chạy tác nhân với yêu cầu lập kế hoạch du lịch, nó sẽ phân tích yêu cầu và tạo một kế hoạch có cấu trúc với các nhiệm vụ được phân công phù hợp cho các tác nhân chuyên biệt, được định dạng dưới dạng JSON tuân theo schema TravelPlan.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.