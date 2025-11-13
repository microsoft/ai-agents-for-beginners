<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T11:32:33+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ja"
}
-->
# 🔍 Microsoft Agent Framework を探る - 基本的なエージェント (.NET)

## 📋 学習目標

この例では、.NET における基本的なエージェント実装を通じて、Microsoft Agent Framework の基本概念を探ります。C# と .NET エコシステムを使用して、エージェントの基本的なパターンを学び、知的エージェントがどのように動作するかを理解します。

### 学べること

- 🏗️ **エージェントアーキテクチャ**: .NET における AI エージェントの基本構造を理解する  
- 🛠️ **ツール統合**: エージェントが外部関数を使用して機能を拡張する方法  
- 💬 **会話フロー**: スレッド管理を用いたマルチターン会話とコンテキストの管理  
- 🔧 **設定パターン**: .NET におけるエージェントのセットアップと管理のベストプラクティス  

## 🎯 カバーする主要な概念

### エージェントフレームワークの原則

- **自律性**: .NET の AI 抽象化を使用してエージェントが独立して意思決定を行う方法  
- **反応性**: 環境の変化やユーザー入力に応答する能力  
- **積極性**: 目標やコンテキストに基づいて主体的に行動する能力  
- **社会的能力**: 会話スレッドを通じて自然言語でやり取りする能力  

### 技術的コンポーネント

- **AIAgent**: エージェントのオーケストレーションと会話管理 (.NET)  
- **ツール関数**: C# メソッドと属性を使用してエージェントの機能を拡張  
- **OpenAI 統合**: 標準化された .NET API を通じて言語モデルを活用  
- **セキュアな設定**: 環境ベースの API キー管理  

## 🔧 技術スタック

### コア技術

- Microsoft Agent Framework (.NET)  
- GitHub Models API 統合  
- OpenAI 互換クライアントパターン  
- DotNetEnv を使用した環境ベースの設定  

### エージェントの機能

- 自然言語の理解と生成  
- C# 属性を使用した関数呼び出しとツール利用  
- 会話スレッドを用いたコンテキスト対応の応答  
- 依存性注入パターンによる拡張可能なアーキテクチャ  

## 📚 フレームワーク比較

この例では、Microsoft Agent Framework のアプローチを他のエージェントフレームワークと比較しています:

| 機能 | Microsoft Agent Framework | 他のフレームワーク |
|------|---------------------------|--------------------|
| **統合性** | Microsoft エコシステムにネイティブ | 互換性はさまざま |
| **シンプルさ** | クリーンで直感的な API | 設定が複雑な場合が多い |
| **拡張性** | ツール統合が容易 | フレームワーク依存 |
| **エンタープライズ対応** | 本番環境向けに構築 | フレームワークによる |

## 🚀 始め方

### 前提条件

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 以上  
- [GitHub Models API アクセストークン](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### 必要な環境変数

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

### サンプルコード

コード例を実行するには、

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

または dotnet CLI を使用して:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

完全なコードは [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) を参照してください。

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

## 🎓 重要なポイント

1. **エージェントアーキテクチャ**: Microsoft Agent Framework は、.NET で AI エージェントを構築するためのクリーンで型安全なアプローチを提供します  
2. **ツール統合**: `[Description]` 属性で装飾された関数は、エージェントの利用可能なツールになります  
3. **会話コンテキスト**: スレッド管理により、完全なコンテキスト認識を持つマルチターン会話が可能になります  
4. **設定管理**: 環境変数とセキュアな資格情報管理は .NET のベストプラクティスに従います  
5. **OpenAI 互換性**: GitHub Models 統合は OpenAI 互換 API を通じてシームレスに動作します  

## 🔗 追加リソース

- [Microsoft Agent Framework ドキュメント](https://learn.microsoft.com/agent-framework)  
- [GitHub Models Marketplace](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET シングルファイルアプリ](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->