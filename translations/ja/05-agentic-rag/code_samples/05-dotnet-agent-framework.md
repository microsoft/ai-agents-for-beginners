# 🔍 Microsoft Foundry（.NET）を用いたエンタープライズ向けRAG

## 📋 学習目標

本ノートブックでは、Microsoft Foundryと.NETのMicrosoft Agent Frameworkを使用して、エンタープライズグレードのRetrieval-Augmented Generation（RAG）システムを構築する方法を示します。ドキュメントを検索し、文脈に即した正確な回答をエンタープライズのセキュリティとスケーラビリティで提供できる、本番対応のエージェントの作成方法を学びます。

**作成するエンタープライズRAG機能:**  
- 📚 <strong>ドキュメントインテリジェンス</strong>: Azure AIサービスを用いた高度なドキュメント処理  
- 🔍 <strong>セマンティック検索</strong>: エンタープライズ機能を備えた高性能ベクトル検索  
- 🛡️ <strong>セキュリティ統合</strong>: ロールベースアクセス制御およびデータ保護パターン  
- 🏢 <strong>スケーラブルなアーキテクチャ</strong>: 監視機能搭載の本番対応RAGシステム  

## 🎯 エンタープライズRAGアーキテクチャ

### コアエンタープライズコンポーネント
- **Microsoft Foundry**: セキュリティとコンプライアンスを備えたマネージドエンタープライズAIプラットフォーム  
- **Persistent Agents**: 会話履歴とコンテキスト管理を持つステートフルエージェント  
- **Vector Store Management**: エンタープライズグレードのドキュメント索引付けと検索  
- **Identity Integration**: Azure AD認証およびロールベースアクセス制御  

### .NETのエンタープライズ向け利点
- <strong>型安全性</strong>: RAG操作とデータ構造のコンパイル時検証  
- <strong>非同期性能</strong>: ブロックしないドキュメント処理と検索操作  
- <strong>メモリ管理</strong>: 大量ドキュメントコレクションのための効率的リソース利用  
- <strong>統合パターン</strong>: 依存性注入を用いたネイティブAzureサービス統合  

## 🏗️ 技術アーキテクチャ

### エンタープライズRAGパイプライン
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### コア.NETコンポーネント
- **Azure.AI.Agents.Persistent**: 状態永続化を備えたエンタープライズエージェント管理  
- **Azure.Identity**: セキュアなAzureサービスアクセスの統合認証  
- **Microsoft.Agents.AI.AzureAI**: Azure最適化エージェントフレームワークの実装  
- **System.Linq.Async**: 高性能非同期LINQ操作  

## 🔧 エンタープライズ機能と利点

### セキュリティとコンプライアンス
- **Azure AD統合**: エンタープライズアイデンティティ管理と認証  
- <strong>ロールベースアクセス</strong>: ドキュメントアクセスおよび操作の細かい権限管理  
- <strong>データ保護</strong>: 保存時および転送時の暗号化による機密ドキュメント保護  
- <strong>監査ログ</strong>: コンプライアンス要件のための包括的な活動追跡  

### 性能とスケーラビリティ
- <strong>接続プーリング</strong>: Azureサービス接続の効率的管理  
- <strong>非同期処理</strong>: 高スループット向けの非同期化操作  
- <strong>キャッシュ戦略</strong>: 頻繁にアクセスされるドキュメントのインテリジェントキャッシュ  
- <strong>負荷分散</strong>: 大規模展開に対応した分散処理  

### 管理と監視
- <strong>ヘルスチェック</strong>: RAGシステムコンポーネントの内蔵監視  
- <strong>パフォーマンスメトリクス</strong>: 検索品質と応答時間に関する詳細分析  
- <strong>エラー処理</strong>: リトライポリシーを含む包括的な例外管理  
- <strong>構成管理</strong>: 環境ごとの設定と検証  

## ⚙️ 前提条件とセットアップ

**開発環境:**  
- .NET 9.0 SDK 以上  
- Visual Studio 2022 または C#拡張機能付き VS Code  
- Microsoft Foundryアクセス付きAzureサブスクリプション  

**必要なNuGetパッケージ:**  
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure認証セットアップ:**  
```bash
# Azure CLI をインストールして認証します
az login
az account set --subscription "your-subscription-id"
```

**環境構成:**  
* Microsoft Foundry構成（Azure CLIで自動処理）  
* 正しいAzureサブスクリプションへ認証済みであることを確認  

## 📊 エンタープライズRAGパターン

### ドキュメント管理パターン
- <strong>一括アップロード</strong>: 大規模ドキュメントコレクションの効率的処理  
- <strong>増分更新</strong>: リアルタイムのドキュメント追加および変更  
- <strong>バージョン管理</strong>: ドキュメントのバージョンと変更履歴の追跡  
- <strong>メタデータ管理</strong>: 豊富なドキュメント属性と分類体系  

### 検索と検索回収パターン
- <strong>ハイブリッド検索</strong>: セマンティック検索とキーワード検索の組み合わせで最適化  
- <strong>ファセット検索</strong>: 多次元フィルタリングと分類  
- <strong>関連度調整</strong>: ドメイン固有ニーズのカスタムスコアリングアルゴリズム  
- <strong>結果ランク付け</strong>: ビジネスロジック統合による高度なランキング  

### セキュリティパターン
- <strong>ドキュメントレベルセキュリティ</strong>: 各ドキュメントの細かいアクセス制御  
- <strong>データ分類</strong>: 自動感度ラベル付けと保護  
- <strong>監査トレイル</strong>: 全RAG操作の包括的ログ記録  
- <strong>プライバシー保護</strong>: PII検出および修正機能  

## 🔒 エンタープライズセキュリティ機能

### 認証と承認
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### データ保護
- <strong>暗号化</strong>: ドキュメントと検索インデックスのエンドツーエンド暗号化  
- <strong>アクセス制御</strong>: ユーザーとグループ権限のAzure AD統合  
- <strong>データ居住地</strong>: コンプライアンスのための地理的データ配置制御  
- <strong>バックアップとリカバリー</strong>: 自動バックアップと災害復旧機能  

## 📈 パフォーマンス最適化

### 非同期処理パターン
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### メモリ管理
- <strong>ストリーミング処理</strong>: メモリ問題なく大容量ドキュメントを処理  
- <strong>リソースプーリング</strong>: 高コストリソースの効率的再利用  
- <strong>ガベージコレクション</strong>: 最適化されたメモリ割り当てパターン  
- <strong>接続管理</strong>: 適切なAzureサービス接続のライフサイクル  

### キャッシュ戦略
- <strong>クエリキャッシュ</strong>: 頻繁に実行される検索のキャッシュ  
- <strong>ドキュメントキャッシュ</strong>: ホットドキュメントのインメモリキャッシュ  
- <strong>インデックスキャッシュ</strong>: 最適化されたベクトルインデックスのキャッシュ  
- <strong>結果キャッシュ</strong>: 生成応答のインテリジェントキャッシュ  

## 📊 エンタープライズユースケース

### ナレッジマネジメント
- **企業Wiki**: 会社のナレッジベース全体へのインテリジェント検索  
- <strong>ポリシーと手順</strong>: 自動化されたコンプライアンスおよび手順ガイダンス  
- <strong>研修資料</strong>: インテリジェントな学習および開発支援  
- <strong>研究データベース</strong>: 学術および研究論文の解析システム  

### カスタマーサポート
- <strong>サポートナレッジベース</strong>: 自動化された顧客サービス応答  
- <strong>製品ドキュメント</strong>: インテリジェントな製品情報検索  
- <strong>トラブルシューティングガイド</strong>: 文脈に応じた問題解決支援  
- **FAQシステム**: ドキュメントコレクションからの動的FAQ生成  

### 規制コンプライアンス
- <strong>法的文書解析</strong>: 契約および法的文書インテリジェンス  
- <strong>コンプライアンス監視</strong>: 自動化された規制コンプライアンスチェック  
- <strong>リスク評価</strong>: ドキュメント基盤のリスク分析および報告  
- <strong>監査支援</strong>: 監査用のインテリジェント文書検索  

## 🚀 本番展開

### 監視と可観測性
- **Application Insights**: 詳細なテレメトリとパフォーマンス監視  
- <strong>カスタムメトリクス</strong>: ビジネス固有のKPI追跡とアラート  
- <strong>分散トレーシング</strong>: サービス間のエンドツーエンドリクエスト追跡  
- <strong>ヘルスダッシュボード</strong>: リアルタイムのシステム健康状態とパフォーマンス可視化  

### スケーラビリティと信頼性
- <strong>オートスケーリング</strong>: 負荷とパフォーマンス指標に基づく自動スケール  
- <strong>高可用性</strong>: フェイルオーバー機能付きのマルチリージョン展開  
- <strong>負荷テスト</strong>: エンタープライズ負荷条件下でのパフォーマンス検証  
- <strong>災害復旧</strong>: 自動バックアップおよび復旧プロセス  

機密ドキュメントをスケール対応で扱えるエンタープライズグレードのRAGシステムを構築する準備はできましたか？インテリジェントな知識システムをエンタープライズ向けに設計しましょう！🏢📖✨

## コード実装

本レッスンの完全な動作コードサンプルは `05-dotnet-agent-framework.cs` にて利用可能です。  

実例を実行するには:

```bash
# スクリプトを実行可能にする（Linux/macOS）
chmod +x 05-dotnet-agent-framework.cs

# .NET シングルファイルアプリを実行する
./05-dotnet-agent-framework.cs
```

または `dotnet run` を直接使用します:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

コード内容のポイント:  

1. <strong>パッケージインストール</strong>: Azure AI Agents用必須NuGetパッケージのインストール  
2. <strong>環境設定</strong>: Microsoft Foundryエンドポイントおよびモデル設定のロード  
3. <strong>ドキュメントアップロード</strong>: RAG処理のためのドキュメントアップロード  
4. <strong>ベクトルストア作成</strong>: セマンティック検索用ベクトルストアの作成  
5. <strong>エージェント設定</strong>: ファイル検索機能を持つAIエージェントのセットアップ  
6. <strong>クエリ実行</strong>: アップロード済みドキュメントに対するクエリの実行  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->