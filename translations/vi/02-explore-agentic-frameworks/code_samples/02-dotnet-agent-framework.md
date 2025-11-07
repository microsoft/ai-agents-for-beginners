<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:37:50+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "vi"
}
-->
# 🔍 Khám phá các Khung Đại lý - Đại lý Cơ bản (.NET)

## 📋 Mục tiêu Học tập

Notebook này khám phá các khái niệm cơ bản của Microsoft Agent Framework thông qua việc triển khai một đại lý cơ bản trong .NET. Bạn sẽ học các mẫu đại lý cốt lõi và hiểu cách các đại lý thông minh hoạt động bên trong bằng C# và hệ sinh thái .NET.

**Những gì bạn sẽ khám phá:**
- 🏗️ **Kiến trúc Đại lý**: Hiểu cấu trúc cơ bản của các đại lý AI trong .NET
- 🛠️ **Tích hợp Công cụ**: Cách các đại lý sử dụng các chức năng bên ngoài để mở rộng khả năng  
- 💬 **Luồng Hội thoại**: Quản lý các cuộc hội thoại nhiều lượt và ngữ cảnh với quản lý luồng
- 🔧 **Mẫu Cấu hình**: Các thực hành tốt nhất để thiết lập và quản lý đại lý trong .NET

## 🎯 Các Khái niệm Chính Được Đề cập

### Nguyên tắc Khung Đại lý
- **Tự chủ**: Cách các đại lý đưa ra quyết định độc lập bằng cách sử dụng các trừu tượng AI của .NET
- **Phản ứng**: Đáp ứng các thay đổi môi trường và đầu vào của người dùng
- **Chủ động**: Chủ động dựa trên mục tiêu và ngữ cảnh
- **Khả năng Xã hội**: Tương tác thông qua ngôn ngữ tự nhiên với các luồng hội thoại

### Các Thành phần Kỹ thuật
- **AIAgent**: Điều phối đại lý cốt lõi và quản lý hội thoại (.NET)
- **Chức năng Công cụ**: Mở rộng khả năng của đại lý với các phương thức và thuộc tính C#
- **Tích hợp OpenAI**: Tận dụng các mô hình ngôn ngữ thông qua các API chuẩn hóa của .NET
- **Quản lý Môi trường**: Cấu hình an toàn và xử lý thông tin xác thực với DotNetEnv

## ⚙️ Yêu cầu & Thiết lập

**Các phụ thuộc cần thiết:**
- .NET 9.0 SDK hoặc cao hơn
- Visual Studio 2022 hoặc VS Code với tiện ích mở rộng C#

**Gói NuGet:**
- `Microsoft.Extensions.AI` - Các trừu tượng AI cốt lõi
- `Microsoft.Extensions.AI.OpenAI` - Tích hợp OpenAI (bản xem trước)
- `DotNetEnv` - Quản lý biến môi trường

**Cấu hình Môi trường (tệp .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Ngăn xếp Kỹ thuật

**Công nghệ Cốt lõi:**
- Microsoft Agent Framework (.NET)
- Tích hợp API Models của GitHub
- Các mẫu khách hàng tương thích OpenAI
- Cấu hình dựa trên môi trường với DotNetEnv

**Khả năng của Đại lý:**
- Hiểu và tạo ngôn ngữ tự nhiên
- Gọi chức năng và sử dụng công cụ với các thuộc tính C#
- Phản hồi theo ngữ cảnh với các luồng hội thoại
- Kiến trúc mở rộng với các mẫu tiêm phụ thuộc

## 📚 So sánh Khung

Ví dụ này minh họa cách tiếp cận của Microsoft Agent Framework trong .NET so với các nền tảng khác:

| Tính năng | Khung Đại lý .NET | Tương đương Python |
|-----------|-------------------|--------------------|
| **Độ an toàn kiểu** | Kiểu mạnh với C# | Kiểu động |
| **Tích hợp** | Hệ sinh thái .NET gốc | Tương thích đa dạng |
| **Hiệu suất** | Hiệu suất mã biên dịch | Thực thi thông dịch |
| **Sẵn sàng cho doanh nghiệp** | Xây dựng cho các ứng dụng .NET sản xuất | Tùy thuộc vào khung |
| **Công cụ** | Tích hợp Visual Studio | Phụ thuộc vào IDE |

## 🚀 Bắt đầu

Làm theo các ô dưới đây để xây dựng đại lý cơ bản đầu tiên của bạn trong .NET và hiểu các khái niệm đại lý cơ bản!

## 📦 Cài đặt và Thiết lập

Ví dụ này có sẵn dưới dạng một ứng dụng tệp đơn .NET có thể chạy. Xem tệp `02-dotnet-agent-framework.cs` đi kèm để biết triển khai đầy đủ.

Để chạy ví dụ này:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Hoặc sử dụng CLI dotnet:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Hướng dẫn Mã

Triển khai đầy đủ bao gồm:

### 1. Các Phụ thuộc Gói

```csharp
// Core AI abstraction layer for .NET applications
#r "nuget: Microsoft.Extensions.AI, 9.9.1"

// Microsoft Agent Framework OpenAI integration
#r "nuget: Microsoft.Agents.AI.OpenAI, 1.0.0-preview.251001.3"

// Core Microsoft Agent Framework library
#r "nuget: Microsoft.Agents.AI, 1.0.0-preview.251001.3"

// Environment variable management
#r "nuget: DotNetEnv, 3.1.1"
```

### 2. Nhập Cần thiết

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Cấu hình Môi trường

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Định nghĩa Chức năng Công cụ

```csharp
// Random destination generator tool
[Description("Provides a random vacation destination.")]
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
```

### 5. Cấu hình và Thiết lập Khách hàng

```csharp
// Extract environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? 
    throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? 
    throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI client for GitHub Models
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI client
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);
```

### 6. Cấu hình Đại lý

```csharp
const string AGENT_NAME = "TravelAgent";

const string AGENT_INSTRUCTIONS = @"You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
""Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?""

Always prioritize user preferences. If they mention a specific destination like ""Bali"" or ""Paris,"" focus your planning on that location rather than suggesting alternatives.
";
```

### 7. Khởi tạo Đại lý

```csharp
// Create AI agent with travel planning capabilities
AIAgent agent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions)
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create((Func<string>)GetRandomDestination)]
    );
```

### 8. Quản lý Hội thoại

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Những Điều Rút ra Quan trọng

1. **Kiến trúc Đại lý**: Microsoft Agent Framework cung cấp một cách tiếp cận sạch sẽ, an toàn kiểu để xây dựng các đại lý AI trong .NET
2. **Tích hợp Công cụ**: Các chức năng được trang trí với thuộc tính `[Description]` trở thành các công cụ có sẵn cho đại lý
3. **Ngữ cảnh Hội thoại**: Quản lý luồng cho phép các cuộc hội thoại nhiều lượt với nhận thức đầy đủ về ngữ cảnh
4. **Quản lý Cấu hình**: Các biến môi trường và xử lý thông tin xác thực an toàn tuân theo các thực hành tốt nhất của .NET
5. **Tương thích OpenAI**: Tích hợp Models của GitHub hoạt động liền mạch thông qua các API tương thích OpenAI

## 🔗 Tài nguyên Bổ sung

- [Tài liệu Microsoft Agent Framework](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.