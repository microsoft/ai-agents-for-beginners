# 🔍 探索 Microsoft Agent Framework - 基本代理 (.NET)

## 📋 學習目標

本範例透過 .NET 中的基本代理實作，探索 Microsoft Agent Framework 的基本概念。您將學習核心的代理模式，並了解智能代理如何使用 C# 及 .NET 生態系統在背後運作。

### 你將發現什麼

- 🏗️ <strong>代理架構</strong>：理解 .NET 中 AI 代理的基本結構
- 🛠️ <strong>工具整合</strong>：代理如何使用外部函數以擴展功能  
- 💬 <strong>會話流程</strong>：以執行緒管理多輪對話與上下文
- 🔧 <strong>配置模式</strong>：.NET 中代理設置與管理的最佳實務

## 🎯 涵蓋的關鍵概念

### 代理框架原則

- <strong>自主性</strong>：代理如何使用 .NET AI 抽象自主決策
- <strong>反應性</strong>：對環境變化和使用者輸入做出回應
- <strong>前瞻性</strong>：根據目標和上下文主動採取行動
- <strong>社交能力</strong>：通過自然語言與會話執行緒互動

### 技術組件

- **AIAgent**：核心代理編排與會話管理 (.NET)
- <strong>工具函數</strong>：使用 C# 方法及屬性擴展代理功能
- **Azure OpenAI 整合**：透過 Azure OpenAI Responses API 使用語言模型
- <strong>安全配置</strong>：基於環境的端點管理

## 🔧 技術堆疊

### 核心技術

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) 整合
- Azure.AI.OpenAI 用戶端模式
- 使用 DotNetEnv 的基於環境的配置

### 代理功能

- 自然語言理解與生成
- 使用 C# 屬性進行函數調用及工具使用
- 支援上下文感知的回應與會話階段
- 可擴展架構與依賴注入模式

## 📚 框架比較

本範例示範 Microsoft Agent Framework 與其他代理框架的比較：

| 功能 | Microsoft Agent Framework | 其他框架 |
|---------|-------------------------|------------------|
| <strong>整合性</strong> | 原生 Microsoft 生態系統 | 相容性多樣 |
| <strong>簡易性</strong> | 乾淨直覺的 API | 通常需複雜設定 |
| <strong>擴展性</strong> | 容易整合工具 | 依框架而異 |
| <strong>企業適用</strong> | 適合生產環境 | 因框架而異 |

## 🚀 快速開始

### 先決條件

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更高版本
- 擁有 Azure OpenAI 資源與模型部署的 [Azure 訂閱](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — 使用 `az login` 登入

### 必填環境變數

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# 然後登入，以便 AzureCliCredential 可以獲取令牌
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# 然後登入，讓 AzureCliCredential 可以取得權杖
az login
```

### 範例程式碼

若要執行範例程式碼，

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

或使用 dotnet CLI：

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

完整程式碼請參見 [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs)。

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

## 🎓 重要重點

1. <strong>代理架構</strong>：Microsoft Agent Framework 提供一種乾淨且型別安全的 .NET AI 代理建立方式
2. <strong>工具整合</strong>：以 `[Description]` 屬性標註的函式會成為代理可用的工具
3. <strong>會話上下文</strong>：會話管理使多輪對話具備完整上下文感知
4. <strong>配置管理</strong>：環境變數與安全憑證處理符合 .NET 最佳實務
5. **Azure OpenAI Responses API**：代理透過 Azure.AI.OpenAI SDK 使用 Azure OpenAI Responses API

## 🔗 額外資源

- [Microsoft Agent Framework 文件](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry 中的 Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET 單檔應用程式](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->