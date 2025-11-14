<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:32:38+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "tw"
}
-->
# 🔍 探索代理框架 - 基本代理 (.NET)

## 📋 學習目標

本筆記本透過在 .NET 中實現基本代理，探討 Microsoft Agent Framework 的基本概念。您將學習核心代理模式，並了解智能代理如何在 C# 和 .NET 生態系統中運作。

**您將學到：**
- 🏗️ **代理架構**：了解 .NET 中 AI 代理的基本結構
- 🛠️ **工具整合**：代理如何使用外部函數擴展功能  
- 💬 **對話流程**：通過線程管理處理多輪對話和上下文
- 🔧 **配置模式**：在 .NET 中進行代理設置和管理的最佳實踐

## 🎯 涵蓋的關鍵概念

### 代理框架原則
- **自主性**：代理如何使用 .NET AI 抽象進行獨立決策
- **反應性**：對環境變化和用戶輸入的響應
- **主動性**：根據目標和上下文採取主動行動
- **社交能力**：通過自然語言與對話線程進行互動

### 技術組件
- **AIAgent**：核心代理編排和對話管理 (.NET)
- **工具函數**：使用 C# 方法和屬性擴展代理功能
- **OpenAI 整合**：通過標準化 .NET API 利用語言模型
- **環境管理**：使用 DotNetEnv 進行安全配置和憑證處理

## ⚙️ 前置條件與設置

**所需依賴項：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或安裝 C# 擴展的 VS Code

**NuGet 套件：**
- `Microsoft.Extensions.AI` - 核心 AI 抽象
- `Microsoft.Extensions.AI.OpenAI` - OpenAI 整合 (預覽版)
- `DotNetEnv` - 環境變數管理

**環境配置 (.env 文件)：**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 技術堆疊

**核心技術：**
- Microsoft Agent Framework (.NET)
- GitHub 模型 API 整合
- OpenAI 兼容的客戶端模式
- 基於環境的配置與 DotNetEnv

**代理功能：**
- 自然語言理解與生成
- 使用 C# 屬性進行函數調用和工具使用
- 基於對話線程的上下文感知響應
- 使用依賴注入模式的可擴展架構

## 📚 框架比較

此示例展示了 .NET 中 Microsoft Agent Framework 與其他平台的對比：

| 功能 | .NET 代理框架 | Python 等效框架 |
|------|---------------|----------------|
| **類型安全性** | 使用 C# 的強類型 | 動態類型 |
| **整合性** | 原生 .NET 生態系統 | 兼容性多樣 |
| **性能** | 編譯代碼性能 | 解釋執行 |
| **企業級準備** | 為生產級 .NET 應用構建 | 依框架而異 |
| **工具支持** | Visual Studio 整合 | 依賴 IDE |

## 🚀 開始使用

按照以下步驟構建您的第一個基本代理，並了解基礎代理概念！

## 📦 安裝與設置

此示例可作為可運行的 .NET 單文件應用程序使用。請參閱附帶的 `02-dotnet-agent-framework.cs` 文件以獲取完整實現。

運行此示例：

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

或使用 dotnet CLI：

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 代碼解析

完整實現包括：

### 1. 套件依賴項

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

### 2. 必要導入

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. 環境配置

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. 工具函數定義

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

### 5. 配置與客戶端設置

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

### 8. 對話管理

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 關鍵收穫

1. **代理架構**：Microsoft Agent Framework 提供了一種乾淨且類型安全的方法來在 .NET 中構建 AI 代理
2. **工具整合**：使用 `[Description]` 屬性修飾的函數成為代理可用的工具
3. **對話上下文**：線程管理支持多輪對話並具備完整上下文感知
4. **配置管理**：環境變數和安全憑證處理遵循 .NET 最佳實踐
5. **OpenAI 兼容性**：GitHub 模型整合通過 OpenAI 兼容 API 無縫運作

## 🔗 其他資源

- [Microsoft Agent Framework 文件](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub 模型市場](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET 單文件應用](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。