<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:32:03+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "zh"
}
-->
# 🔍 探索 Agentic 框架 - 基础代理 (.NET)

## 📋 学习目标

本笔记本通过在 .NET 中实现一个基础代理，探索 Microsoft Agent Framework 的基本概念。您将学习核心代理模式，并了解智能代理如何通过 C# 和 .NET 生态系统在底层工作。

**您将学到：**
- 🏗️ **代理架构**：理解 .NET 中 AI 代理的基本结构
- 🛠️ **工具集成**：代理如何使用外部函数扩展功能  
- 💬 **对话流程**：通过线程管理处理多轮对话和上下文
- 🔧 **配置模式**：.NET 中代理设置和管理的最佳实践

## 🎯 关键概念

### Agentic 框架原则
- **自主性**：代理如何使用 .NET AI 抽象做出独立决策
- **反应性**：响应环境变化和用户输入
- **主动性**：根据目标和上下文采取行动
- **社交能力**：通过自然语言与对话线程进行交互

### 技术组件
- **AIAgent**：核心代理编排和对话管理 (.NET)
- **工具函数**：通过 C# 方法和属性扩展代理功能
- **OpenAI 集成**：通过标准化 .NET API 利用语言模型
- **环境管理**：使用 DotNetEnv 进行安全配置和凭证处理

## ⚙️ 前置条件与设置

**所需依赖：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或安装了 C# 扩展的 VS Code

**NuGet 包：**
- `Microsoft.Extensions.AI` - 核心 AI 抽象
- `Microsoft.Extensions.AI.OpenAI` - OpenAI 集成（预览版）
- `DotNetEnv` - 环境变量管理

**环境配置 (.env 文件)：**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 技术栈

**核心技术：**
- Microsoft Agent Framework (.NET)
- GitHub 模型 API 集成
- OpenAI 兼容客户端模式
- 基于环境的配置与 DotNetEnv

**代理功能：**
- 自然语言理解与生成
- 使用 C# 属性进行函数调用和工具使用
- 通过对话线程进行上下文感知响应
- 使用依赖注入模式扩展架构

## 📚 框架对比

此示例展示了 .NET 中 Microsoft Agent Framework 的方法与其他平台的对比：

| 功能       | .NET Agent Framework | Python 等价框架 |
|------------|---------------------|----------------|
| **类型安全** | 使用 C# 强类型       | 动态类型        |
| **集成**   | 原生 .NET 生态系统    | 兼容性多样      |
| **性能**   | 编译代码性能          | 解释执行        |
| **企业级** | 专为生产级 .NET 应用构建 | 取决于框架       |
| **工具支持** | Visual Studio 集成    | 依赖 IDE        |

## 🚀 快速开始

按照以下步骤构建您的第一个基础代理，并理解基础代理概念！

## 📦 安装与设置

此示例可作为可运行的 .NET 单文件应用程序使用。完整实现请参见附带的 `02-dotnet-agent-framework.cs` 文件。

运行此示例：

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

或使用 dotnet CLI：

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 代码解析

完整实现包括：

### 1. 包依赖

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

### 2. 必要导入

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. 环境配置

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. 工具函数定义

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

### 5. 配置与客户端设置

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

### 6. 代理配置

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

### 7. 代理初始化

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

### 8. 对话管理

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 关键收获

1. **代理架构**：Microsoft Agent Framework 提供了一种干净、类型安全的方式来在 .NET 中构建 AI 代理
2. **工具集成**：使用 `[Description]` 属性装饰的函数成为代理可用的工具
3. **对话上下文**：线程管理支持多轮对话并具备完整的上下文感知
4. **配置管理**：环境变量和安全凭证处理遵循 .NET 最佳实践
5. **OpenAI 兼容性**：GitHub 模型集成通过 OpenAI 兼容 API 无缝工作

## 🔗 其他资源

- [Microsoft Agent Framework 文档](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub 模型市场](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET 单文件应用](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。