<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:22:25+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "ja"
}
-->
# 🛠️ GitHubモデルを活用した高度なツール使用 (.NET)

## 📋 学習目標

このノートブックでは、Microsoft Agent Frameworkを使用してGitHubモデルと統合するエンタープライズ向けのツール統合パターンを紹介します。C#の強力な型付けと.NETのエンタープライズ機能を活用して、複数の専門的なツールを持つ高度なエージェントを構築する方法を学びます。

**習得する高度なツール機能:**
- 🔧 **マルチツールアーキテクチャ**: 複数の専門的な機能を持つエージェントの構築
- 🎯 **型安全なツール実行**: C#のコンパイル時検証を活用
- 📊 **エンタープライズツールパターン**: 実運用向けのツール設計とエラー処理
- 🔗 **ツールの組み合わせ**: 複雑なビジネスワークフローのためのツール統合

## 🎯 .NETツールアーキテクチャの利点

### エンタープライズツールの特徴
- **コンパイル時検証**: 強力な型付けによりツールパラメータの正確性を保証
- **依存性注入**: IoCコンテナ統合によるツール管理
- **非同期パターン**: 適切なリソース管理を伴う非ブロッキングツール実行
- **構造化ログ**: ツール実行の監視のための組み込みログ機能

### 実運用向けパターン
- **例外処理**: 型付けされた例外による包括的なエラー管理
- **リソース管理**: 適切な破棄パターンとメモリ管理
- **パフォーマンス監視**: 組み込みメトリクスとパフォーマンスカウンター
- **構成管理**: 検証付きの型安全な構成管理

## 🔧 技術アーキテクチャ

### .NETの主要ツールコンポーネント
- **Microsoft.Extensions.AI**: 統一されたツール抽象化レイヤー
- **Microsoft.Agents.AI**: エンタープライズ向けツールオーケストレーション
- **GitHubモデル統合**: 接続プールを備えた高性能APIクライアント

### ツール実行パイプライン
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ ツールカテゴリとパターン

### 1. **データ処理ツール**
- **入力検証**: データ注釈を使用した強力な型付け
- **変換操作**: 型安全なデータ変換とフォーマット
- **ビジネスロジック**: ドメイン固有の計算と分析ツール
- **出力フォーマット**: 構造化されたレスポンス生成

### 2. **統合ツール**
- **APIコネクタ**: HttpClientを使用したRESTfulサービス統合
- **データベースツール**: Entity Frameworkを使用したデータアクセス
- **ファイル操作**: 検証付きの安全なファイルシステム操作
- **外部サービス**: サードパーティサービス統合パターン

### 3. **ユーティリティツール**
- **テキスト処理**: 文字列操作とフォーマットユーティリティ
- **日付/時間操作**: 文化に配慮した日付/時間計算
- **数学ツール**: 精密な計算と統計操作
- **検証ツール**: ビジネスルール検証とデータ確認

## ⚙️ 前提条件とセットアップ

**開発環境:**
- .NET 9.0 SDK以上
- Visual Studio 2022またはC#拡張機能付きVS Code
- GitHubモデルAPIアクセス

**必要なNuGetパッケージ:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**環境構成 (.envファイル):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

.NETで強力で型安全なツール機能を備えたエンタープライズ向けエージェントを構築する準備はできましたか？プロフェッショナルなソリューションを設計しましょう！ 🏢⚡

## 💻 コード実装

完全なC#実装は、付属ファイル `04-dotnet-agent-framework.cs` にあります。この.NETシングルファイルアプリでは以下を示します:

- GitHubモデル構成のための環境変数の読み込み
- 属性を使用したC#メソッドによるカスタムツールの定義
- ツール統合を備えたAIエージェントの作成
- 会話スレッドの管理
- ツール呼び出しを伴うエージェントリクエストの実行

例を実行するには:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

または.NET CLIを使用して:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当社は責任を負いません。