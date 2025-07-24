<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T07:56:06+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "ja"
}
-->
# レッスン11: モデルコンテキストプロトコル (MCP) の統合

## モデルコンテキストプロトコル (MCP) の概要

モデルコンテキストプロトコル (MCP) は、AIモデルとクライアントアプリケーション間のやり取りを標準化するために設計された最先端のフレームワークです。MCPはAIモデルとそれを利用するアプリケーションの間の橋渡しを行い、基盤となるモデルの実装に関係なく一貫したインターフェースを提供します。

MCPの主な特徴:

- **標準化された通信**: MCPは、アプリケーションがAIモデルと通信するための共通言語を確立します
- **高度なコンテキスト管理**: AIモデルに効率的にコンテキスト情報を渡すことが可能です
- **クロスプラットフォーム互換性**: C#、Java、JavaScript、Python、TypeScriptなど、さまざまなプログラミング言語で動作します
- **シームレスな統合**: 開発者が異なるAIモデルを簡単にアプリケーションに統合できるようにします

MCPは特にAIエージェントの開発において価値があり、統一されたプロトコルを通じてエージェントがさまざまなシステムやデータソースとやり取りできるようにすることで、エージェントをより柔軟かつ強力にします。

## 学習目標
- MCPとは何か、そしてAIエージェント開発におけるその役割を理解する
- GitHub統合のためのMCPサーバーをセットアップおよび構成する
- MCPツールを使用してマルチエージェントシステムを構築する
- Azure Cognitive Searchを用いたRAG (Retrieval Augmented Generation) を実装する

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
   - Azure Cognitive Searchリソースを作成する  
   - Azure OpenAIサービスをセットアップする  
   - `.env`に環境変数を設定する  

3. **MCPサーバーのセットアップ**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## プロジェクト構成

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
- ハッカソンエージェント: プロジェクト推奨
- イベントエージェント: 技術イベントの提案

### 2. Azure統合
- イベントのインデックス作成にCognitive Searchを使用
- エージェントの知能にAzure OpenAIを活用
- RAGパターンの実装

### 3. MCPツール
- GitHubリポジトリ分析
- コード検査
- メタデータ抽出

## コードウォークスルー

このサンプルでは以下を示します:
1. MCPサーバーの統合
2. マルチエージェントのオーケストレーション
3. Azure Cognitive Searchの統合
4. RAGパターンの実装

主な機能:
- リアルタイムのGitHubリポジトリ分析
- インテリジェントなプロジェクト推奨
- Azure Searchを使用したイベントマッチング
- Chainlitを用いたストリーミングレスポンス

## サンプルの実行

詳細なセットアップ手順や追加情報については、[Github MCP Server Example README](./code_samples/github-mcp/README.md) を参照してください。

1. MCPサーバーを起動する:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. アプリケーションを起動する:  
   ```bash
   chainlit run app.py -w
   ```

3. 統合をテストする:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## トラブルシューティング

よくある問題と解決策:
1. MCP接続の問題  
   - サーバーが稼働していることを確認する  
   - ポートの使用状況を確認する  
   - GitHubトークンを確認する  

2. Azure Searchの問題  
   - 接続文字列を検証する  
   - インデックスが存在することを確認する  
   - ドキュメントのアップロードを確認する  

## 次のステップ
- 追加のMCPツールを探索する
- カスタムエージェントを実装する
- RAG機能を強化する
- より多くのイベントソースを追加する
- **上級者向け**: [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) をチェックして、エージェント間通信の例を確認する

## リソース
- [MCP初心者向けガイド](https://aka.ms/mcp-for-beginners)  
- [MCPドキュメント](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search ドキュメント](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel ガイド](https://learn.microsoft.com/semantic-kernel/)  

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語で記載された原文が公式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。