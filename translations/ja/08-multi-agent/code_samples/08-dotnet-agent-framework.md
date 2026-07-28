# 🤝 エンタープライズマルチエージェントワークフローシステム (.NET)

## 📋 学習目標

このノートブックでは、Azure OpenAI (Responses API) と .NET の Microsoft Agent Framework を使用して、洗練されたエンタープライズグレードのマルチエージェントシステムを構築する方法を示します。複数の専門化されたエージェントが連携して構造化されたワークフローを通じて動作し、.NET のエンタープライズ機能を活用して本番環境対応のソリューションを実現する方法を学びます。

**構築するエンタープライズマルチエージェントの機能:**
- 👥 <strong>エージェントコラボレーション</strong>: コンパイル時検証による型安全なエージェント調整
- 🔄 <strong>ワークフローオーケストレーション</strong>: .NET の非同期パターンを用いた宣言的ワークフロー定義
- 🎭 <strong>役割の専門化</strong>: 強い型付けされたエージェントのパーソナリティと専門領域
- 🏢 <strong>エンタープライズ統合</strong>: 監視とエラーハンドリングを備えた本番対応パターン

## ⚙️ 前提条件 & セットアップ

**開発環境:**
- .NET 9.0 SDK 以上
- Visual Studio 2022 または C# 拡張機能付き VS Code
- Azure サブスクリプション（永続エージェント用）

**必要な NuGet パッケージ:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## コードサンプル

本レッスンの完全な動作コードは、添付の C# ファイル [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs) にあります。

サンプルを実行するには:

```bash
# ファイルを実行可能にする（Linux/macOS）
chmod +x 08-dotnet-agent-framework.cs

# サンプルを実行する
./08-dotnet-agent-framework.cs
```

または .NET CLI を使用して:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## このサンプルの説明内容

このマルチエージェントワークフローシステムは、2つの専門エージェントを備えたホテル旅行推奨サービスを作成します:

1. **FrontDesk エージェント**: アクティビティとロケーションの推奨を提供する旅行エージェント
2. **Concierge エージェント**: 推奨内容をレビューし、本物で観光地化されていない体験を確保

エージェントは以下の流れで連携します:
- FrontDesk エージェントが最初の旅行リクエストを受け取る
- Concierge エージェントが推奨内容をレビューして精緻化する
- ワークフローがリアルタイムに応答をストリーミング配信する

## 重要なコンセプト

### エージェント調整
本サンプルは、Microsoft Agent Framework を用いた型安全なエージェント調整をコンパイル時検証と共に示しています。

### ワークフローオーケストレーション
.NET の非同期パターンを用いた宣言的ワークフロー定義により複数のエージェントをパイプラインで接続します。

### 応答のストリーミング
非同期列挙子とイベント駆動アーキテクチャを用いたエージェント応答のリアルタイムストリーミングを実装しています。

### エンタープライズ統合
以下を含む本番対応パターンを示しています:
- 環境変数設定
- セキュアな資格情報管理
- エラーハンドリング
- 非同期イベント処理

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->