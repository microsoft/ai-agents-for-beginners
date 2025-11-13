<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T13:17:08+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "vi"
}
-->
# 🔍 Khám phá Microsoft Agent Framework - Agent cơ bản (.NET)

## 📋 Mục tiêu học tập

Ví dụ này khám phá các khái niệm cơ bản của Microsoft Agent Framework thông qua việc triển khai một agent cơ bản trong .NET. Bạn sẽ học các mẫu thiết kế cốt lõi của agent và hiểu cách các agent thông minh hoạt động bên trong bằng cách sử dụng C# và hệ sinh thái .NET.

### Những gì bạn sẽ khám phá

- 🏗️ **Kiến trúc Agent**: Hiểu cấu trúc cơ bản của các agent AI trong .NET  
- 🛠️ **Tích hợp công cụ**: Cách các agent sử dụng các hàm bên ngoài để mở rộng khả năng  
- 💬 **Luồng hội thoại**: Quản lý các cuộc hội thoại nhiều lượt và ngữ cảnh với quản lý luồng  
- 🔧 **Mẫu cấu hình**: Các phương pháp tốt nhất để thiết lập và quản lý agent trong .NET  

## 🎯 Các khái niệm chính được đề cập

### Nguyên tắc của Agentic Framework

- **Tự chủ**: Cách các agent đưa ra quyết định độc lập bằng cách sử dụng các trừu tượng AI của .NET  
- **Phản ứng**: Đáp ứng các thay đổi từ môi trường và đầu vào của người dùng  
- **Chủ động**: Chủ động hành động dựa trên mục tiêu và ngữ cảnh  
- **Khả năng xã hội**: Tương tác thông qua ngôn ngữ tự nhiên với các luồng hội thoại  

### Các thành phần kỹ thuật

- **AIAgent**: Điều phối agent cốt lõi và quản lý hội thoại (.NET)  
- **Hàm công cụ**: Mở rộng khả năng của agent với các phương thức và thuộc tính C#  
- **Tích hợp OpenAI**: Tận dụng các mô hình ngôn ngữ thông qua các API chuẩn hóa của .NET  
- **Cấu hình bảo mật**: Quản lý khóa API dựa trên môi trường  

## 🔧 Công nghệ kỹ thuật

### Công nghệ cốt lõi

- Microsoft Agent Framework (.NET)  
- Tích hợp API GitHub Models  
- Các mẫu client tương thích với OpenAI  
- Cấu hình dựa trên môi trường với DotNetEnv  

### Khả năng của Agent

- Hiểu và tạo ngôn ngữ tự nhiên  
- Gọi hàm và sử dụng công cụ với các thuộc tính C#  
- Phản hồi theo ngữ cảnh với các luồng hội thoại  
- Kiến trúc mở rộng với các mẫu tiêm phụ thuộc  

## 📚 So sánh Framework

Ví dụ này minh họa cách tiếp cận của Microsoft Agent Framework so với các framework agentic khác:

| Tính năng | Microsoft Agent Framework | Các Framework khác |
|-----------|---------------------------|--------------------|
| **Tích hợp** | Hệ sinh thái Microsoft gốc | Tương thích đa dạng |
| **Đơn giản** | API sạch, trực quan | Thường thiết lập phức tạp |
| **Mở rộng** | Tích hợp công cụ dễ dàng | Phụ thuộc vào framework |
| **Sẵn sàng cho doanh nghiệp** | Xây dựng cho sản xuất | Tùy thuộc vào framework |

## 🚀 Bắt đầu

### Yêu cầu trước

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) hoặc cao hơn  
- [Mã truy cập API GitHub Models](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Các biến môi trường cần thiết

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```

```powershell
# PowerShell
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```

### Mã mẫu

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

Xem [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) để có mã đầy đủ.  

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*

using System.ClientModel;
using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using OpenAI;

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

// Extract configuration from environment variables
// Retrieve the GitHub Models API endpoint, defaults to https://models.github.ai/inference if not specified
// Retrieve the model ID, defaults to openai/gpt-5-mini if not specified
// Retrieve the GitHub token for authentication, throws exception if not specified
var github_endpoint = Environment.GetEnvironmentVariable("GH_ENDPOINT") ?? "https://models.github.ai/inference";
var github_model_id = Environment.GetEnvironmentVariable("GH_MODEL_ID") ?? "openai/gpt-5-mini";
var github_token = Environment.GetEnvironmentVariable("GH_TOKEN") ?? throw new InvalidOperationException("GH_TOKEN is not set.");

// Configure OpenAI Client Options
// Create configuration options to point to GitHub Models endpoint
// This redirects OpenAI client calls to GitHub's model inference service
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
// Create OpenAI client using GitHub token for authentication
// Configure it to use GitHub Models endpoint instead of OpenAI directly
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

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
// Initialize complete agent pipeline: OpenAI client → Chat client → AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
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

## 🎓 Những điểm chính cần nhớ

1. **Kiến trúc Agent**: Microsoft Agent Framework cung cấp một cách tiếp cận sạch sẽ, an toàn kiểu dữ liệu để xây dựng các agent AI trong .NET  
2. **Tích hợp công cụ**: Các hàm được trang trí với thuộc tính `[Description]` trở thành các công cụ có sẵn cho agent  
3. **Ngữ cảnh hội thoại**: Quản lý luồng cho phép các cuộc hội thoại nhiều lượt với nhận thức đầy đủ về ngữ cảnh  
4. **Quản lý cấu hình**: Các biến môi trường và xử lý thông tin xác thực an toàn tuân theo các phương pháp tốt nhất của .NET  
5. **Tương thích OpenAI**: Tích hợp GitHub Models hoạt động liền mạch thông qua các API tương thích với OpenAI  

## 🔗 Tài nguyên bổ sung

- [Tài liệu Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->