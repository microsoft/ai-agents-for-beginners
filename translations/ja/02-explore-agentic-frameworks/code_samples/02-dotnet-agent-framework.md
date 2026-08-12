# 🔍 Microsoft Agent Framework の探求 - 基本エージェント (.NET)

## 📋 学習目標

この例では、.NET による基本的なエージェント実装を通じて Microsoft Agent Framework の基本概念を探ります。コアとなるエージェントパターンを学び、C# と .NET エコシステムを使ったインテリジェントエージェントの内部動作を理解します。

### 発見すること

- 🏗️ <strong>エージェントのアーキテクチャ</strong>: .NET での AI エージェントの基本構造の理解
- 🛠️ <strong>ツール統合</strong>: エージェントが外部機能を利用して能力を拡張する仕組み  
- 💬 <strong>会話の流れ</strong>: スレッド管理を用いた多ターン会話とコンテキストの管理
- 🔧 <strong>設定パターン</strong>: .NET におけるエージェントのセットアップと管理のベストプラクティス

## 🎯 主な概念の解説

### エージェントフレームワークの原則

- <strong>自律性</strong>: .NET AI 抽象化を使いエージェントが独立して意思決定する方法
- <strong>反応性</strong>: 環境変化やユーザー入力に反応する能力
- <strong>能動性</strong>: 目標とコンテキストに基づきイニシアチブを取ること
- <strong>社会的能力</strong>: 会話スレッドを通じて自然言語で交流すること

### 技術的要素

- **AIAgent**: コアのエージェントオーケストレーションと会話管理 (.NET)
- <strong>ツール関数</strong>: C# のメソッドや属性でエージェント機能を拡張
- **Azure OpenAI 統合**: Azure OpenAI Responses API を活用した言語モデル利用
- <strong>セキュアな設定</strong>: 環境に基づくエンドポイント管理

## 🔧 技術スタック

### コア技術

- Microsoft Agent Framework (.NET)
- Azure OpenAI (Responses API) 統合
- Azure.AI.OpenAI クライアントパターン
- DotNetEnv を使った環境ベース設定

### エージェント機能

- 自然言語理解と生成
- C# 属性による関数呼び出しとツール利用
- 会話セッションを活用したコンテキスト対応応答
- 依存性注入パターンによる拡張可能なアーキテクチャ

## 📚 フレームワーク比較

この例は、Microsoft Agent Framework アプローチを他のエージェントフレームワークと比較して示しています：

| 特徴 | Microsoft Agent Framework | 他のフレームワーク |
|---------|-------------------------|------------------|
| <strong>統合</strong> | Microsoft ネイティブエコシステム | 互換性はさまざま |
| <strong>簡便さ</strong> | クリーンで直感的な API | 設定が複雑になりがち |
| <strong>拡張性</strong> | 簡単なツール統合 | フレームワーク依存 |
| <strong>エンタープライズ対応</strong> | 本番環境向けに構築 | フレームワークにより異なる |

## 🚀 始め方

### 前提条件

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) 以上
- Azure OpenAI リソースとモデル展開を含む [Azure サブスクリプション](https://azure.microsoft.com/free/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — `az login` でサインイン

### 必須の環境変数

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# AzureCliCredential がトークンを取得できるようにサインインしてください
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# AzureCliCredential がトークンを取得できるようにサインインしてください
az login
```

### サンプルコード

コード例を実行するには、

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

または dotnet CLI を使って：

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

完全なコードは [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) を参照してください。

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

## 🎓 主なポイント

1. <strong>エージェントアーキテクチャ</strong>: Microsoft Agent Framework は .NET で AI エージェントを構築するためのクリーンで型安全なアプローチを提供する
2. <strong>ツール統合</strong>: `[Description]` 属性で装飾された関数がエージェントの利用可能なツールになる
3. <strong>会話コンテキスト</strong>: セッション管理によりコンテキストを完全に意識した多ターン会話が可能
4. <strong>設定管理</strong>: 環境変数と安全な認証情報管理は .NET のベストプラクティスに従う
5. **Azure OpenAI Responses API**: エージェントは Azure.AI.OpenAI SDK を通じて Azure OpenAI Responses API を利用する

## 🔗 追加リソース

- [Microsoft Agent Framework ドキュメント](https://learn.microsoft.com/agent-framework)
- [Microsoft Foundry の Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET シングルファイルアプリ](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->