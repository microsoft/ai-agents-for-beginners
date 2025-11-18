<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T11:20:49+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "mo"
}
-->
# 🔍 探索 Microsoft Agent Framework - 基本代理 (.NET)

## 📋 學習目標

此範例透過在 .NET 中實現基本代理，探索 Microsoft Agent Framework 的基本概念。您將學習核心代理模式，並了解智能代理如何在 C# 和 .NET 生態系統中運作。

### 您將學到的內容

- 🏗️ **代理架構**：了解 .NET 中 AI 代理的基本結構  
- 🛠️ **工具整合**：代理如何使用外部函數來擴展功能  
- 💬 **對話流程**：通過線程管理處理多輪對話和上下文  
- 🔧 **配置模式**：在 .NET 中設置和管理代理的最佳實踐  

## 🎯 涵蓋的關鍵概念

### 代理框架原則

- **自主性**：代理如何使用 .NET AI 抽象進行獨立決策  
- **反應性**：響應環境變化和使用者輸入  
- **主動性**：根據目標和上下文主動採取行動  
- **社交能力**：通過自然語言與對話線程進行互動  

### 技術組件

- **AIAgent**：核心代理編排和對話管理 (.NET)  
- **工具函數**：使用 C# 方法和屬性擴展代理功能  
- **OpenAI 整合**：通過標準化 .NET API 利用語言模型  
- **安全配置**：基於環境的 API 金鑰管理  

## 🔧 技術堆疊

### 核心技術

- Microsoft Agent Framework (.NET)  
- GitHub Models API 整合  
- OpenAI 兼容的客戶端模式  
- 使用 DotNetEnv 的基於環境的配置  

### 代理功能

- 自然語言理解和生成  
- 使用 C# 屬性進行函數調用和工具使用  
- 基於上下文的回應和對話線程管理  
- 使用依賴注入模式的可擴展架構  

## 📚 框架比較

此範例展示了 Microsoft Agent Framework 與其他代理框架的比較：

| 功能         | Microsoft Agent Framework | 其他框架          |
|--------------|---------------------------|-------------------|
| **整合性**   | 原生 Microsoft 生態系統   | 兼容性各異        |
| **簡易性**   | 乾淨直觀的 API            | 通常設置較複雜    |
| **擴展性**   | 易於工具整合              | 依賴框架          |
| **企業級**   | 為生產環境而設計          | 因框架而異        |

## 🚀 快速入門

### 先決條件

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更高版本  
- [GitHub Models API 訪問令牌](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### 必需的環境變數

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
  

### 範例代碼

要運行代碼範例，

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
或者使用 dotnet CLI：

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
請參閱 [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) 以獲取完整代碼。

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
  

## 🎓 關鍵要點

1. **代理架構**：Microsoft Agent Framework 提供了一種乾淨且類型安全的方法來在 .NET 中構建 AI 代理  
2. **工具整合**：使用 `[Description]` 屬性修飾的函數成為代理可用的工具  
3. **對話上下文**：線程管理支持多輪對話並具備完整的上下文感知能力  
4. **配置管理**：環境變數和安全憑證處理遵循 .NET 的最佳實踐  
5. **OpenAI 兼容性**：GitHub Models 整合通過 OpenAI 兼容的 API 無縫運作  

## 🔗 其他資源

- [Microsoft Agent Framework 文件](https://learn.microsoft.com/agent-framework)  
- [GitHub Models 市場](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET 單文件應用](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用本翻譯而引起的任何誤解或誤釋不承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->