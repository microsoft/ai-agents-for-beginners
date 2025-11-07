<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:55:29+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "ja"
}
-->
# 🎯 GitHubモデルを使用した計画とデザインパターン (.NET)

## 📋 学習目標

このノートブックでは、Microsoft Agent Frameworkを使用してGitHubモデルと.NETでインテリジェントエージェントを構築するためのエンタープライズ向けの計画とデザインパターンを紹介します。複雑な問題を分解し、複数ステップの解決策を計画し、.NETのエンタープライズ機能を活用して高度なワークフローを実行するエージェントの作成方法を学びます。

## ⚙️ 前提条件とセットアップ

**開発環境:**
- .NET 9.0 SDK以上
- Visual Studio 2022 または C#拡張機能付きのVS Code
- GitHub Models APIアクセス

**必要な依存関係:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**環境設定 (.envファイル):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## コードの実行

このレッスンでは、.NETシングルファイルアプリの実装が含まれています。実行するには:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

または、dotnet runコマンドを使用してください:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## コードの実装

完全な実装は `07-dotnet-agent-framework.cs` にあります。このファイルでは以下を示しています:

- DotNetEnvを使用した環境設定の読み込み
- GitHubモデル用OpenAIクライアントの設定
- JSONシリアル化を使用した構造化データモデル (PlanとTravelPlan) の定義
- JSONスキーマを使用した構造化出力を持つAIエージェントの作成
- 型安全なレスポンスを伴う計画リクエストの実行

## 重要な概念

### 型安全モデルを使用した構造化計画

エージェントはC#クラスを使用して計画出力の構造を定義します:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### 構造化出力のためのJSONスキーマ

エージェントはTravelPlanスキーマに一致するレスポンスを返すように設定されています:

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### 計画エージェントの指示

エージェントはコーディネーターとして機能し、専門のサブエージェントにタスクを委任します:

- FlightBooking: フライトの予約とフライト情報の提供
- HotelBooking: ホテルの予約とホテル情報の提供
- CarRental: 車のレンタルとレンタル情報の提供
- ActivitiesBooking: アクティビティの予約とアクティビティ情報の提供
- DestinationInfo: 目的地に関する情報の提供
- DefaultAgent: 一般的なリクエストの処理

## 期待される出力

旅行計画リクエストでエージェントを実行すると、リクエストを分析し、TravelPlanスキーマに準拠したJSON形式で専門エージェントへの適切なタスク割り当てを含む構造化計画を生成します。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。