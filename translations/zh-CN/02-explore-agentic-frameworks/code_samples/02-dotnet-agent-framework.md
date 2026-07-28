# 🔍 探索 Microsoft Agent Framework - 基础代理 (.NET)

## 📋 学习目标

本示例通过在 .NET 中实现基础代理，探索 Microsoft Agent Framework 的基本概念。您将学习核心代理模式，并通过 C# 和 .NET 生态系统了解智能代理的运行原理。

### 您将发现

- 🏗️ <strong>代理架构</strong>：理解 .NET 中人工智能代理的基本结构
- 🛠️ <strong>工具集成</strong>：代理如何使用外部函数扩展功能  
- 💬 <strong>对话流程</strong>：通过线程管理管理多轮对话与上下文
- 🔧 <strong>配置模式</strong>：.NET 中代理设置和管理的最佳实践

## 🎯 涉及的关键概念

### 代理框架原则

- <strong>自治性</strong>：代理如何使用 .NET AI 抽象独立决策
- <strong>响应性</strong>：响应环境变化和用户输入
- <strong>主动性</strong>：基于目标和上下文主动采取行动
- <strong>社交能力</strong>：通过自然语言和对话线程进行交互

### 技术组件

- **AIAgent**：核心代理协调和对话管理 (.NET)
- <strong>工具函数</strong>：通过 C# 方法和特性扩展代理功能
- **Azure OpenAI 集成**：利用 Azure OpenAI Responses API 调用语言模型
- <strong>安全配置</strong>：基于环境的端点管理

## 🔧 技术栈

### 核心技术

- Microsoft Agent Framework (.NET)
- Azure OpenAI（Responses API）集成
- Azure.AI.OpenAI 客户端模式
- 使用 DotNetEnv 进行基于环境的配置

### 代理能力

- 自然语言理解与生成
- 使用 C# 特性进行函数调用和工具使用
- 具备上下文感知的对话会话响应
- 通过依赖注入模式实现可扩展架构

## 📚 框架比较

本示例演示 Microsoft Agent Framework 方法与其他代理框架的对比：

| 特性 | Microsoft Agent Framework | 其他框架 |
|---------|-------------------------|------------------|
| <strong>集成</strong> | 原生微软生态系统 | 兼容性多样 |
| <strong>简洁性</strong> | 清晰直观的 API | 通常设置复杂 |
| <strong>可扩展性</strong> | 轻松集成工具 | 依赖于框架 |
| <strong>企业级</strong> | 面向生产环境构建 | 取决于框架 |

## 🚀 入门

### 前置条件

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更高版本
- 拥有 Azure OpenAI 资源和模型部署的 [Azure 订阅](https://azure.microsoft.com/free/)
- 安装 [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) 并使用 `az login` 登录

### 所需环境变量

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# 然后登录，以便 AzureCliCredential 能获取令牌
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# 然后登录，以便 AzureCliCredential 可以获取令牌
az login
```

### 示例代码

运行代码示例，

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

或使用 dotnet CLI：

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

完整代码请参见 [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs)。

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

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
    .GetChatClient(deployment)
    .AsAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Session for Context Management.
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentSession session = await agent.CreateSessionAsync();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the session parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", session))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation sessions and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", session))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 关键要点

1. <strong>代理架构</strong>：Microsoft Agent Framework 提供用于在 .NET 中构建 AI 代理的清晰、类型安全的方法
2. <strong>工具集成</strong>：带有 `[Description]` 特性的函数成为代理可用的工具
3. <strong>对话上下文</strong>：会话管理支持多轮对话的完整上下文感知
4. <strong>配置管理</strong>：环境变量和安全凭证处理遵循 .NET 最佳实践
5. **Azure OpenAI Responses API**：代理通过 Azure.AI.OpenAI SDK 使用 Azure OpenAI Responses API

## 🔗 其他资源

- [Microsoft Agent Framework 文档](https://learn.microsoft.com/agent-framework)
- [微软 Foundry 中的 Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET 单文件应用程序](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->