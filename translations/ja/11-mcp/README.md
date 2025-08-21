<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:09:05+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "ja"
}
-->
# レッスン11: モデルコンテキストプロトコル (MCP) の統合

## モデルコンテキストプロトコル (MCP) の概要

モデルコンテキストプロトコル (MCP) は、AIモデルとクライアントアプリケーション間のやり取りを標準化するために設計された最先端のフレームワークです。MCPは、AIモデルとそれを利用するアプリケーションの間の橋渡しを行い、基盤となるモデルの実装に関係なく一貫したインターフェースを提供します。

MCPの主な特徴:

- **標準化された通信**: MCPは、アプリケーションがAIモデルと通信するための共通言語を確立します
- **コンテキスト管理の強化**: AIモデルに効率的にコンテキスト情報を渡すことが可能
- **クロスプラットフォーム互換性**: C#、Java、JavaScript、Python、TypeScriptなど、さまざまなプログラミング言語で動作
- **シームレスな統合**: 開発者が異なるAIモデルを簡単にアプリケーションに統合できるようにします

MCPは特にAIエージェントの開発において価値があり、統一されたプロトコルを通じてエージェントがさまざまなシステムやデータソースとやり取りできるようにすることで、エージェントをより柔軟で強力にします。

## 学習目標
- MCPとは何か、そしてAIエージェント開発におけるその役割を理解する
- GitHub統合のためのMCPサーバーをセットアップおよび構成する
- MCPツールを使用してマルチエージェントシステムを構築する
- Azure Cognitive Searchを使用したRAG (Retrieval Augmented Generation) を実装する

## 前提条件
- Python 3.8以上
- Node.js 14以上
- Azureサブスクリプション
- GitHubアカウント
- Semantic Kernelの基本的な理解

## セットアップ手順

1. **環境のセットアップ**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azureサービスの構成**
   - Azure Cognitive Searchリソースを作成
   - Azure OpenAIサービスをセットアップ
   - `.env`ファイルに環境変数を設定

3. **MCPサーバーのセットアップ**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## プロジェクト構造

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## コアコンポーネント

### 1. マルチエージェントシステム
- GitHubエージェント: リポジトリ分析
- ハッカソンエージェント: プロジェクトの推奨
- イベントエージェント: 技術イベントの提案

### 2. Azure統合
- イベントインデックス作成のためのCognitive Search
- エージェントの知能化のためのAzure OpenAI
- RAGパターンの実装

### 3. MCPツール
- GitHubリポジトリ分析
- コード検査
- メタデータ抽出

## コードの解説

このサンプルでは以下を示します:
1. MCPサーバーの統合
2. マルチエージェントのオーケストレーション
3. Azure Cognitive Searchの統合
4. RAGパターンの実装

主な機能:
- リアルタイムのGitHubリポジトリ分析
- インテリジェントなプロジェクト推奨
- Azure Searchを使用したイベントマッチング
- Chainlitによるストリーミングレスポンス

## サンプルの実行

詳細なセットアップ手順や追加情報については、[Github MCP Server Example README](./code_samples/github-mcp/README.md) を参照してください。

1. MCPサーバーを起動:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. アプリケーションを起動:
   ```bash
   chainlit run app.py -w
   ```

3. 統合をテスト:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## トラブルシューティング

よくある問題と解決策:
1. MCP接続の問題
   - サーバーが稼働していることを確認
   - ポートの利用可能性を確認
   - GitHubトークンを確認

2. Azure Searchの問題
   - 接続文字列を検証
   - インデックスの存在を確認
   - ドキュメントのアップロードを確認

## 次のステップ
- 追加のMCPツールを探索する
- カスタムエージェントを実装する
- RAG機能を強化する
- より多くのイベントソースを追加する
- **上級**: [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) をチェックしてエージェント間通信の例を確認する

## リソース
- [MCP初心者向けガイド](https://aka.ms/mcp-for-beginners)  
- [MCPドキュメント](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。