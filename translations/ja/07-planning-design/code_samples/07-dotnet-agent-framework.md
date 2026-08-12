# 🎯 Azure OpenAI (Responses API) を使ったプランニング & デザインパターン (.NET)

## 📋 学習目標

このノートブックは、.NETのMicrosoft Agent FrameworkとAzure OpenAI（Responses API）を用いてインテリジェントエージェントを構築するためのエンタープライズ向けプランニングとデザインパターンを示します。複雑な問題を分解し、マルチステップのソリューションを計画し、.NETのエンタープライズ機能を活用して高度なワークフローを実行できるエージェントの作成方法を学びます。

## ⚙️ 前提条件とセットアップ

**開発環境：**
- .NET 9.0 SDK 以上
- Visual Studio 2022 または C# 拡張機能付きの VS Code
- Azure OpenAI リソースとモデル展開がある Azure サブスクリプション
- Azure CLI — `az login` でログイン

**必要な依存関係：**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**環境構成 (.env ファイル)：**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## コードの実行

本レッスンには .NET シングルファイルアプリの実装が含まれています。実行するには：

```bash
# ファイルを実行可能にする（Linux/macOS）
chmod +x 07-dotnet-agent-framework.cs

# アプリケーションを実行する
./07-dotnet-agent-framework.cs
```

または dotnet run コマンドを使用：

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## コード実装

完全な実装は `07-dotnet-agent-framework.cs` にあり、以下を示しています：

- DotNetEnv を使った環境構成の読み込み
- Azure OpenAI クライアントの設定と `GetChatClient().AsAIAgent()` による AI エージェント作成
- JSON シリアライズ対応の構造化データモデル（Plan と TravelPlan）の定義
- JSON スキーマを用いた構造化出力のある AI エージェントの作成
- 型安全なレスポンスによるプランニングリクエストの実行

## 重要なコンセプト

### 型安全なモデルによる構造化プランニング

エージェントは C# クラスを使ってプランニング出力の構造を定義します：

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

### 構造化出力のための JSON スキーマ

エージェントは TravelPlan スキーマに準拠したレスポンスを返すよう設定されています：

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### プランニングエージェントの指示

エージェントはコーディネーターとして機能し、専門のサブエージェントにタスクを委任します：

- FlightBooking: フライト予約およびフライト情報提供用
- HotelBooking: ホテル予約およびホテル情報提供用
- CarRental: 車レンタル予約および車両情報提供用
- ActivitiesBooking: アクティビティ予約および情報提供用
- DestinationInfo: 目的地情報提供用
- DefaultAgent: 一般的なリクエスト処理用

## 期待される出力

旅行プランニングリクエストでエージェントを実行すると、リクエストを解析し、専門エージェントへの適切なタスク割り当てを伴う構造化プランを生成します。出力は TravelPlan スキーマに準拠した JSON 形式になります。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->