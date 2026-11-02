# 🔍 探索 Microsoft Agent Framework - 基本代理 (.NET)

## 📋 學習目標

此範例透過 .NET 中的基本代理實作，探討 Microsoft Agent Framework 的基本概念。您將學習核心的代理模式，並了解使用 C# 及 .NET 生態系統下智能代理的運作原理。

### 您將發現

- 🏗️ <strong>代理架構</strong>：理解 .NET 中 AI 代理的基本結構
- 🛠️ <strong>工具整合</strong>：代理如何使用外部功能來擴充能力  
- 💬 <strong>對話流程</strong>：透過線程管理維護多輪對話及上下文
- 🔧 <strong>配置模式</strong>：.NET 中代理設置與管理的最佳實踐

## 🎯 涵蓋的關鍵概念

### 代理框架原則

- <strong>自治性</strong>：代理如何使用 .NET AI 抽象進行獨立決策
- <strong>反應性</strong>：對環境變化與使用者輸入的回應
- <strong>主動性</strong>：基於目標與情境採取主動行動
- <strong>社交能力</strong>：透過自然語言及對話線程進行互動

### 技術組件

- **AIAgent**：核心代理調度與對話管理 (.NET)
- <strong>工具功能</strong>：透過 C# 方法與屬性擴展代理能力
- **Azure OpenAI 整合**：利用 Azure OpenAI Responses API 的語言模型
- <strong>安全配置</strong>：基於環境的端點管理

## 🔧 技術棧

### 核心技術

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) 整合
- Azure.AI.OpenAI 用戶端模式
- 使用 DotNetEnv 進行環境配置

### 代理能力

- 自然語言理解與生成
- 以 C# 屬性呼叫函數與工具使用
- 支援上下文感知回應與對話會話
- 可擴充架構，採用依賴注入模式

## 📚 框架比較

此範例展示 Microsoft Agent Framework 與其他代理框架的比較：

| 功能 | Microsoft Agent Framework | 其他框架 |
|---------|-------------------------|------------------|
| <strong>整合性</strong> | 原生 Microsoft 生態系統 | 相容性多樣 |
| <strong>簡單性</strong> | 乾淨且直觀的 API | 通常設定較複雜 |
| <strong>擴充性</strong> | 容易整合工具 | 依賴特定框架 |
| <strong>企業就緒度</strong> | 為生產環境打造 | 依框架而異 |

## 🚀 快速開始

### 先決條件

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或更高版本
- 擁有 Azure OpenAI 資源及模型部署的 [Azure 訂閱](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — 使用 `az login` 登入

### 必需環境變數

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# 然後登入，以便 AzureCliCredential 可以取得權杖
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# 然後登入，讓 AzureCliCredential 可以取得權杖
az login
```

### 範例代碼

執行範例代碼，

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

或使用 dotnet CLI：

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

完整程式碼見 [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs)。

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

## 🎓 主要重點

1. <strong>代理架構</strong>：Microsoft Agent Framework 提供在 .NET 建構 AI 代理的乾淨且類型安全方法
2. <strong>工具整合</strong>：以 `[Description]` 屬性裝飾的函數會成為代理可用工具
3. <strong>對話上下文</strong>：會話管理支援帶完整上下文感知的多輪對話
4. <strong>配置管理</strong>：環境變數與安全憑證處理遵循 .NET 最佳實踐
5. **Azure OpenAI Responses API**：代理透過 Azure.AI.OpenAI SDK 使用 Azure OpenAI Responses API

## 🔗 其他資源

- [Microsoft Agent Framework 文件](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry 中的 Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET 單一檔案應用程式](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->