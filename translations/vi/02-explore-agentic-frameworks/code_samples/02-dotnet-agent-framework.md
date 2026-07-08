# 🔍 Khám Phá Microsoft Agent Framework - Đại Lý Cơ Bản (.NET)

## 📋 Mục Tiêu Học Tập

Ví dụ này khám phá các khái niệm cơ bản của Microsoft Agent Framework thông qua một triển khai đại lý cơ bản trong .NET. Bạn sẽ học các mẫu đại lý cốt lõi và hiểu cách các đại lý thông minh hoạt động bên trong sử dụng C# và hệ sinh thái .NET.

### Những Gì Bạn Sẽ Khám Phá

- 🏗️ **Kiến Trúc Đại Lý**: Hiểu cấu trúc cơ bản của các đại lý AI trong .NET
- 🛠️ **Tích Hợp Công Cụ**: Làm thế nào các đại lý sử dụng các chức năng bên ngoài để mở rộng khả năng  
- 💬 **Luồng Hội Thoại**: Quản lý các cuộc trò chuyện đa lượt và ngữ cảnh với quản lý luồng
- 🔧 **Mẫu Cấu Hình**: Thực tiễn tốt nhất cho việc thiết lập và quản lý đại lý trong .NET

## 🎯 Các Khái Niệm Chính Được Đề Cập

### Nguyên Tắc Framework Đại Lý

- **Tự Chủ**: Cách các đại lý đưa ra quyết định độc lập sử dụng trừu tượng AI của .NET
- **Phản Ứng**: Phản hồi sự thay đổi môi trường và đầu vào của người dùng
- **Chủ Động**: Chủ động dựa trên mục tiêu và ngữ cảnh
- **Khả Năng Xã Hội**: Tương tác qua ngôn ngữ tự nhiên với các luồng hội thoại

### Thành Phần Kỹ Thuật

- **AIAgent**: Thành phần điều phối đại lý cốt lõi và quản lý hội thoại (.NET)
- **Chức Năng Công Cụ**: Mở rộng khả năng đại lý với các phương thức và thuộc tính C#
- **Tích Hợp Azure OpenAI**: Tận dụng các mô hình ngôn ngữ qua Azure OpenAI Responses API
- **Cấu Hình Bảo Mật**: Quản lý điểm cuối dựa trên môi trường

## 🔧 Ngăn Xếp Kỹ Thuật

### Công Nghệ Cốt Lõi

- Microsoft Agent Framework (.NET)
- Tích hợp Azure OpenAI (Responses API)
- Mẫu khách Azure.AI.OpenAI
- Cấu hình dựa trên môi trường với DotNetEnv

### Khả Năng Đại Lý

- Hiểu và tạo ngôn ngữ tự nhiên
- Gọi hàm và sử dụng công cụ với thuộc tính C#
- Phản hồi dựa trên ngữ cảnh với các luồng hội thoại
- Kiến trúc mở rộng với các mẫu tiêm phụ thuộc

## 📚 So Sánh Framework

Ví dụ này thể hiện cách tiếp cận của Microsoft Agent Framework so với các framework đại lý khác:

| Tính Năng | Microsoft Agent Framework | Framework Khác |
|---------|-------------------------|------------------|
| **Tích Hợp** | Hệ sinh thái Microsoft gốc | Tương thích đa dạng |
| **Đơn Giản** | API gọn, trực quan | Thường phức tạp khi thiết lập |
| **Khả Năng Mở Rộng** | Dễ tích hợp công cụ | Phụ thuộc vào framework |
| **Sẵn Sàng Doanh Nghiệp** | Xây dựng cho môi trường sản xuất | Thay đổi theo framework |

## 🚀 Bắt Đầu

### Yêu Cầu

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) hoặc phiên bản cao hơn
- Một [đăng ký Azure](https://azure.microsoft.com/free/) với tài nguyên Azure OpenAI và triển khai mô hình
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — đăng nhập với `az login`

### Biến Môi Trường Cần Thiết

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Sau đó đăng nhập để AzureCliCredential có thể lấy token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Sau đó đăng nhập để AzureCliCredential có thể lấy token
az login
```

### Mã Mẫu

Để chạy ví dụ mã,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Hoặc sử dụng dotnet CLI:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Xem [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) để biết mã đầy đủ.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*
#:package Azure.AI.OpenAI@2.1.0
#:package Azure.Identity@1.13.1

using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using Azure.AI.OpenAI;
using Azure.Identity;

// Tool Function: Random Destination Generator
// This static method will be available to the agent as a callable tool
// The [Description] attribute helps the AI understand when to use this function
// This demonstrates how to create custom tools for AI agents
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
    // List of popular vacation destinations around the world
    // The agent will randomly select from these options
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

    // Generate random index and return selected destination
    // Uses System.Random for simple random selection
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// Azure OpenAI with the Responses API (stable v1 endpoint). Sign in with `az login`.
var azureEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4o-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

// Define Agent Identity and Comprehensive Instructions
// Agent name for identification and logging purposes
var AGENT_NAME = "TravelAgent";

// Detailed instructions that define the agent's personality, capabilities, and behavior
// This system prompt shapes how the agent responds and interacts with users
var AGENT_INSTRUCTIONS = """
You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
"Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?"

Always prioritize user preferences. If they mention a specific destination like "Bali" or "Paris," focus your planning on that location rather than suggesting alternatives.
""";

// Create AI Agent with Advanced Travel Planning Capabilities
// Get the Responses client for the deployment and create the AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = azureClient
    .GetOpenAIResponseClient(deployment)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Conversation Thread for Context Management
// Initialize a new conversation thread to maintain context across multiple interactions
// Threads enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentThread thread = agent.GetNewThread();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the thread parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation threads and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Những Điểm Quan Trọng

1. **Kiến Trúc Đại Lý**: Microsoft Agent Framework cung cấp cách tiếp cận rõ ràng, an toàn kiểu để xây dựng đại lý AI trong .NET
2. **Tích Hợp Công Cụ**: Các hàm được trang trí với thuộc tính `[Description]` trở thành công cụ có sẵn cho đại lý
3. **Ngữ Cảnh Hội Thoại**: Quản lý luồng cho phép hội thoại đa lượt với nhận thức đầy đủ về ngữ cảnh
4. **Quản Lý Cấu Hình**: Biến môi trường và xử lý thông tin xác thực an toàn theo thực tiễn tốt nhất của .NET
5. **Azure OpenAI Responses API**: Đại lý sử dụng Azure OpenAI Responses API thông qua SDK Azure.AI.OpenAI

## 🔗 Tài Nguyên Bổ Sung

- [Tài liệu Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI trong Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Ứng dụng đơn file .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->