# 🌍 Đại lý Du lịch AI với Microsoft Agent Framework (.NET)

## 📋 Tổng Quan Kịch Bản

Notebook này hướng dẫn cách xây dựng một đại lý lập kế hoạch du lịch thông minh bằng Microsoft Agent Framework cho .NET. Đại lý có thể tự động tạo lịch trình du lịch cá nhân hóa cho các điểm đến ngẫu nhiên trên toàn thế giới.

**Các Tính Năng Chính:**
- 🎲 **Chọn Điểm Đến Ngẫu Nhiên**: Sử dụng công cụ tùy chỉnh để chọn địa điểm nghỉ dưỡng
- 🗺️ **Lập Kế Hoạch Du Lịch Thông Minh**: Tạo lịch trình chi tiết từng ngày
- 🔄 **Phát Trực Tiếp Theo Thời Gian Thực**: Hỗ trợ phản hồi ngay lập tức và phát trực tiếp
- 🛠️ **Tích Hợp Công Cụ Tùy Chỉnh**: Minh họa cách mở rộng khả năng của đại lý

## 🔧 Kiến Trúc Kỹ Thuật

### Công Nghệ Cốt Lõi
- **Microsoft Agent Framework**: Phiên bản .NET mới nhất để phát triển đại lý AI
- **Tích Hợp Mô Hình GitHub**: Sử dụng dịch vụ suy luận mô hình AI của GitHub
- **Tương Thích API OpenAI**: Tận dụng thư viện khách hàng của OpenAI với các điểm cuối tùy chỉnh
- **Cấu Hình Bảo Mật**: Quản lý khóa API dựa trên môi trường

### Các Thành Phần Chính
1. **AIAgent**: Bộ điều phối chính của đại lý xử lý luồng hội thoại
2. **Công Cụ Tùy Chỉnh**: Hàm `GetRandomDestination()` có sẵn cho đại lý
3. **Chat Client**: Giao diện hội thoại hỗ trợ bởi mô hình GitHub
4. **Hỗ Trợ Phát Trực Tiếp**: Khả năng tạo phản hồi theo thời gian thực

### Mô Hình Tích Hợp
```mermaid
graph LR
    A[User Request] --> B[AI Agent]
    B --> C[GitHub Models API]
    B --> D[GetRandomDestination Tool]
    C --> E[Travel Itinerary]
    D --> E
```

## 🚀 Bắt Đầu

**Yêu Cầu:**
- .NET 9.0 hoặc cao hơn
- Mã truy cập API của GitHub Models
- Các biến môi trường được cấu hình trong tệp `.env`

**Các Biến Môi Trường Cần Thiết:**
```env
GITHUB_TOKEN=your_github_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Chạy các ô dưới đây theo thứ tự để xem đại lý du lịch hoạt động!

---

## .NET Single File App: AI Travel Agent Example

See `01-dotnet-agent-framework.cs` for the complete runnable code sample.

Chạy mẫu mã bên dưới:

```bash
dotnet run 01-dotnet-agent-framework.cs
```

### Sample Code

```csharp
static string GetRandomDestination()
{
    var destinations = new List<string>
    {
        "Paris, France",
        "Tokyo, Japan",
        "New York City, USA",
        "Sydney, Australia",
        "Rome, Italy",
        "Barcelona, Spain",
        "Cape Town, South Africa",
        "Rio de Janeiro, Brazil",
        "Bangkok, Thailand",
        "Vancouver, Canada"
    };
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// Extract configuration from environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI Client Options
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

// Create AI Agent with Travel Planning Capabilities
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip (Non-Streaming)
Console.WriteLine(await agent.RunAsync("Plan me a day trip"));

// Execute Agent: Plan a Day Trip (Streaming Response)
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    Console.Write(update);
}
```
