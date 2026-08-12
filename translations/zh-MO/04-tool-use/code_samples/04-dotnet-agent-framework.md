# 🛠️ 使用 Azure OpenAI (Responses API) 的進階工具應用 (.NET)

## 📋 學習目標

本筆記本展示如何使用 Microsoft Agent Framework 在 .NET 中，結合 Azure OpenAI (Responses API) 建立企業級的工具整合範例。你將學會如何利用 C# 的強型別與 .NET 的企業功能，打造多重專業工具的進階代理。

### 你將掌握的進階工具能力

- 🔧 <strong>多工具架構</strong>：構建具多種專業功能的代理
- 🎯 <strong>型別安全的工具執行</strong>：利用 C# 編譯時驗證
- 📊 <strong>企業級工具模式</strong>：生產環境可用的工具設計與錯誤處理
- 🔗 <strong>工具組合</strong>：結合工具以實現複雜的業務流程

## 🎯 .NET 工具架構優勢

### 企業級工具特性

- <strong>編譯時驗證</strong>：強型別確保工具參數正確性
- <strong>依賴注入</strong>：IoC 容器整合以管理工具
- **非同步/Await 模式**：非阻塞的工具執行與資源管理
- <strong>結構化日誌</strong>：內建的日誌整合以監控工具執行

### 生產可用模式

- <strong>例外處理</strong>：全面的錯誤管理與型別例外
- <strong>資源管理</strong>：完善的釋放模式與記憶體管理
- <strong>效能監控</strong>：內建指標與效能計數器
- <strong>配置管理</strong>：型別安全的配置並帶有驗證

## 🔧 技術架構

### 核心 .NET 工具組件

- **Microsoft.Extensions.AI**：統一工具抽象層
- **Microsoft.Agents.AI**：企業級工具調度
- **Azure OpenAI (Responses API)**：高效能 API 客戶端，具連線池功能

### 工具執行管線

```mermaid
graph LR
    A[使用者請求] --> B[代理分析]
    B --> C[工具選擇]
    C --> D[類型驗證]
    B --> E[參數綁定]
    E --> F[工具執行]
    C --> F
    F --> G[結果處理]
    D --> G
    G --> H[回應]
```

## 🛠️ 工具類別與模式

### 1. <strong>資料處理工具</strong>

- <strong>輸入驗證</strong>：強型別搭配資料註解
- <strong>轉換操作</strong>：型別安全的資料轉換與格式化
- <strong>業務邏輯</strong>：特定領域計算與分析工具
- <strong>輸出格式化</strong>：結構化的回應產生

### 2. <strong>整合工具</strong>

- **API 連接器**：使用 HttpClient 的 RESTful 服務整合
- <strong>資料庫工具</strong>：Entity Framework 整合資料存取
- <strong>檔案操作</strong>：帶驗證的安全檔案系統操作
- <strong>外部服務</strong>：第三方服務整合模式

### 3. <strong>實用工具</strong>

- <strong>文字處理</strong>：字串操作與格式化工具
- **日期/時間操作**：文化感知的日期時間計算
- <strong>數學工具</strong>：精準計算與統計操作
- <strong>驗證工具</strong>：業務規則驗證與資料核查

準備好在 .NET 中構建具強大型別安全工具能力的企業級代理了嗎？讓我們一起設計專業級解決方案吧！🏢⚡

## 🚀 開始使用

### 前置條件

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 或以上版本
- 一個具備 Azure OpenAI 資源與模型部署的 [Azure 訂閱](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — 使用 `az login` 登入

### 所需環境變數

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

執行範例程式碼，

```bash
# zsh/bash
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

或使用 dotnet CLI：

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

完整程式碼請參考 [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs)。

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

// Create New Conversation Session for Context Management
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
await using var session = await agent.CreateSessionAsync();

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->