# 🌍 使用 Microsoft Agent Framework (.NET) 构建 AI旅行助手

## 📋 场景概述

本笔记本展示了如何使用 Microsoft Agent Framework for .NET 构建一个智能旅行规划助手。该助手可以自动为全球随机目的地生成个性化的一日游行程。

**主要功能：**
- 🎲 **随机目的地选择**：使用自定义工具选择度假地点
- 🗺️ **智能旅行规划**：创建详细的每日行程
- 🔄 **实时流式响应**：支持即时和流式响应
- 🛠️ **自定义工具集成**：展示如何扩展助手功能

## 🔧 技术架构

### 核心技术
- **Microsoft Agent Framework**：用于开发 AI助手的最新 .NET 实现
- **GitHub 模型集成**：使用 GitHub 的 AI模型推理服务
- **OpenAI API 兼容性**：利用 OpenAI 客户端库和自定义端点
- **安全配置**：基于环境的 API密钥管理

### 关键组件
1. **AIAgent**：主要的助手协调器，负责对话流程
2. **自定义工具**：提供给助手的 `GetRandomDestination()` 函数
3. **聊天客户端**：基于 GitHub 模型的对话界面
4. **流式支持**：实时响应生成功能

### 集成模式
```mermaid
graph LR
    A[User Request] --> B[AI Agent]
    B --> C[GitHub Models API]
    B --> D[GetRandomDestination Tool]
    C --> E[Travel Itinerary]
    D --> E
```

## 🚀 快速开始

**前置条件：**
- .NET 9.0 或更高版本
- GitHub Models API访问令牌
- 在 `.env` 文件中配置的环境变量

**所需环境变量：**
```env
GITHUB_TOKEN=your_github_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

按顺序运行以下单元格，体验旅行助手的功能！

---

## .NET Single File App: AI Travel Agent Example

See `01-dotnet-agent-framework.cs` for the complete runnable code sample.

运行以下代码示例：

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
