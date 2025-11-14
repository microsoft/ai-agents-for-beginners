<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:14:29+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "ja"
}
-->
# 🤝 エンタープライズ向けマルチエージェントワークフローシステム (.NET)

## 📋 学習目標

このノートブックでは、Microsoft Agent Frameworkを使用して.NETでGitHubモデルを活用し、洗練されたエンタープライズ向けマルチエージェントシステムを構築する方法を紹介します。複数の専門エージェントが協力して構造化されたワークフローを通じて作業する方法を学び、.NETのエンタープライズ機能を活用して本番環境に対応したソリューションを構築します。

**構築するエンタープライズマルチエージェント機能:**
- 👥 **エージェントの協力**: 型安全なエージェントの連携とコンパイル時検証
- 🔄 **ワークフローのオーケストレーション**: .NETの非同期パターンを活用した宣言的なワークフロー定義
- 🎭 **役割の専門化**: 強く型付けされたエージェントの個性と専門分野
- 🏢 **エンタープライズ統合**: 監視とエラー処理を備えた本番環境対応のパターン

## ⚙️ 前提条件とセットアップ

**開発環境:**
- .NET 9.0 SDK以上
- Visual Studio 2022 または C#拡張機能付きの VS Code
- Azureサブスクリプション (永続的なエージェント用)

**必要なNuGetパッケージ:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## コードサンプル

このレッスンの完全な動作コードは、付属のC#ファイルにあります: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

サンプルを実行するには:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

または .NET CLI を使用して:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## このサンプルで示す内容

このマルチエージェントワークフローシステムは、ホテル旅行のおすすめサービスを提供する2つの専門エージェントを作成します:

1. **フロントデスクエージェント**: アクティビティや場所のおすすめを提供する旅行エージェント
2. **コンシェルジュエージェント**: おすすめをレビューし、観光地化されていない本格的な体験を保証

エージェントは以下のワークフローで協力します:
- フロントデスクエージェントが最初の旅行リクエストを受け取る
- コンシェルジュエージェントがおすすめをレビューし、改善する
- ワークフローがリアルタイムでレスポンスをストリーミングする

## 重要な概念

### エージェントの連携
Microsoft Agent Frameworkを使用して型安全なエージェントの連携をコンパイル時検証とともに実現します。

### ワークフローのオーケストレーション
.NETの非同期パターンを使用して、複数のエージェントをパイプラインで接続する宣言的なワークフロー定義を実装します。

### レスポンスのストリーミング
非同期列挙とイベント駆動型アーキテクチャを使用して、エージェントのレスポンスをリアルタイムでストリーミングします。

### エンタープライズ統合
以下を含む本番環境対応のパターンを示します:
- 環境変数の設定
- 安全な資格情報管理
- エラー処理
- 非同期イベント処理

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。