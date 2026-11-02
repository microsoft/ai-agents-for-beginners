# 🔍 探索 Microsoft Agent Framework - 基本代理 (.NET)

## 📋 學習目標

此範例透過在 .NET 中的基本代理實作，探索 Microsoft Agent Framework 的基本概念。您將學習核心代理模式，並了解如何使用 C# 及 .NET 生態系統在底層運作智慧代理。

### 您將發現

- 🏗️ <strong>代理架構</strong>：理解 .NET 中 AI 代理的基本結構
- 🛠️ <strong>工具整合</strong>：代理如何使用外部函式擴展功能  
- 💬 <strong>對話流程</strong>：使用執行緒管理多輪對話與上下文
- 🔧 <strong>組態模式</strong>：在 .NET 中的代理設置與管理最佳實踐

## 🎯 涵蓋的關鍵概念

### 代理框架原則

- <strong>自主性</strong>：代理如何使用 .NET AI 抽象獨立做決策
- <strong>反應能力</strong>：回應環境變化和使用者輸入
- <strong>主動性</strong>：根據目標和情境採取主動
- <strong>社交能力</strong>：透過自然語言與對話執行緒互動

### 技術組件

- **AIAgent**：核心代理協調與對話管理 (.NET)
- <strong>工具函式</strong>：使用 C# 方法和屬性擴展代理功能
- **Azure OpenAI 整合**：透過 Azure OpenAI Responses API 利用語言模型
- <strong>安全組態</strong>：基於環境的端點管理

## 🔧 技術棧

### 核心技術

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) 整合
- Azure.AI.OpenAI 用戶端模式
- 使用 DotNetEnv 進行基於環境的組態

### 代理能力

- 自然語言理解與生成
- 使用 C# 屬性進行函式呼叫與工具使用
- 具上下文感知的回應與對話會話
- 透過依賴注入模式實現可擴展架構

## 📚 框架比較

本範例展示 Microsoft Agent Framework 的方法，並與其他代理框架比較：

| 功能 | Microsoft Agent Framework | 其他框架 |
|---------|-------------------------|------------------|
| <strong>整合性</strong> | 原生 Microsoft 生態系統 | 相容性多元 |
| <strong>簡易性</strong> | 乾淨且直覺的 API | 通常設置較複雜 |
| <strong>擴充性</strong> | 輕鬆整合工具 | 依賴框架 |
| <strong>企業級準備</strong> | 為生產環境打造 | 根據框架而異 |

## 🚀 快速入門

### 前置需求

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更高版本
- 具有 Azure OpenAI 資源和模型部署的 [Azure 訂閱](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — 使用 `az login` 登入

### 必要環境變數

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# 然後登入，以便 AzureCliCredential 可以取得令牌
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# 然後登入，以便 AzureCliCredential 能取得權杖
az login
```

### 範例程式碼

執行範例程式碼，

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

或使用 dotnet CLI：

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

完整程式碼請參閱 [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs)。

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

## 🎓 主要重點歸納

1. <strong>代理架構</strong>：Microsoft Agent Framework 提供在 .NET 中構建 AI 代理的乾淨且類型安全方法
2. <strong>工具整合</strong>：用 `[Description]` 屬性裝飾的函式會成為代理可用的工具
3. <strong>對話上下文</strong>：會話管理支援多輪對話，具備完整上下文感知
4. <strong>組態管理</strong>：環境變數與安全憑證處理遵循 .NET 最佳實踐
5. **Azure OpenAI Responses API**：代理透過 Azure.AI.OpenAI SDK 使用 Azure OpenAI Responses API

## 🔗 額外資源

- [Microsoft Agent Framework 文件](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry 中的 Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET 單一檔案應用](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->