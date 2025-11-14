<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:32:49+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ja"
}
-->
# 🔍 エージェントフレームワークの探求 - 基本エージェント (.NET)

## 📋 学習目標

このノートブックでは、Microsoft Agent Frameworkの基本概念を.NETでの基本的なエージェント実装を通じて探ります。C#と.NETエコシステムを使用して、エージェントの基本的なパターンを学び、インテリジェントエージェントがどのように動作するかを理解します。

**学べる内容:**
- 🏗️ **エージェントアーキテクチャ**: .NETにおけるAIエージェントの基本構造の理解
- 🛠️ **ツール統合**: エージェントが外部関数を使用して機能を拡張する方法  
- 💬 **会話フロー**: スレッド管理を使用したマルチターン会話とコンテキストの管理
- 🔧 **設定パターン**: .NETでのエージェント設定と管理のベストプラクティス

## 🎯 カバーする主要概念

### エージェントフレームワークの原則
- **自律性**: .NET AI抽象化を使用してエージェントが独立して意思決定を行う方法
- **反応性**: 環境の変化やユーザー入力への対応
- **積極性**: 目標やコンテキストに基づいて主体的に行動する能力
- **社会的能力**: 会話スレッドを通じて自然言語でやり取りする能力

### 技術的コンポーネント
- **AIAgent**: エージェントのオーケストレーションと会話管理 (.NET)
- **ツール関数**: C#メソッドと属性を使用してエージェントの機能を拡張
- **OpenAI統合**: 標準化された.NET APIを通じて言語モデルを活用
- **環境管理**: DotNetEnvを使用した安全な設定と資格情報の管理

## ⚙️ 必要条件とセットアップ

**必要な依存関係:**
- .NET 9.0 SDK以上
- Visual Studio 2022またはC#拡張機能付きVS Code

**NuGetパッケージ:**
- `Microsoft.Extensions.AI` - コアAI抽象化
- `Microsoft.Extensions.AI.OpenAI` - OpenAI統合 (プレビュー)
- `DotNetEnv` - 環境変数管理

**環境設定 (.envファイル):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 技術スタック

**コア技術:**
- Microsoft Agent Framework (.NET)
- GitHub Models API統合
- OpenAI互換クライアントパターン
- DotNetEnvを使用した環境ベースの設定

**エージェントの機能:**
- 自然言語の理解と生成
- C#属性を使用した関数呼び出しとツール利用
- 会話スレッドによるコンテキスト対応の応答
- 依存性注入パターンによる拡張可能なアーキテクチャ

## 📚 フレームワーク比較

この例では、.NETにおけるMicrosoft Agent Frameworkのアプローチを他のプラットフォームと比較しています:

| 機能 | .NETエージェントフレームワーク | Pythonの同等品 |
|---------|---------------------|-------------------|
| **型安全性** | C#による強い型付け | 動的型付け |
| **統合** | ネイティブな.NETエコシステム | 多様な互換性 |
| **パフォーマンス** | コンパイルコードのパフォーマンス | インタプリタ実行 |
| **エンタープライズ対応** | 本格的な.NETアプリ向け | フレームワークによる |
| **ツール** | Visual Studio統合 | IDE依存 |

## 🚀 始める方法

以下のセルに従って、.NETで最初の基本エージェントを構築し、エージェントの基本概念を理解しましょう！

## 📦 インストールとセットアップ

この例は実行可能な.NETシングルファイルアプリとして利用可能です。完全な実装については、付属の`02-dotnet-agent-framework.cs`ファイルを参照してください。

この例を実行するには:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

またはdotnet CLIを使用して:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 コード解説

完全な実装には以下が含まれます:

### 1. パッケージ依存関係

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

### 2. 必須インポート

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. 環境設定

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. ツール関数の定義

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

### 5. 設定とクライアントセットアップ

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

### 6. エージェント設定

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

### 7. エージェント初期化

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

### 8. 会話管理

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 重要なポイント

1. **エージェントアーキテクチャ**: Microsoft Agent Frameworkは、.NETでAIエージェントを構築するためのクリーンで型安全なアプローチを提供します
2. **ツール統合**: `[Description]`属性で装飾された関数は、エージェントが利用可能なツールになります
3. **会話コンテキスト**: スレッド管理により、完全なコンテキスト認識を持つマルチターン会話が可能になります
4. **設定管理**: 環境変数と安全な資格情報管理は.NETのベストプラクティスに従います
5. **OpenAI互換性**: GitHub Models統合はOpenAI互換APIを通じてシームレスに動作します

## 🔗 追加リソース

- [Microsoft Agent Framework ドキュメント](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。