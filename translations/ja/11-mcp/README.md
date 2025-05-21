<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-05-21T09:32:15+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "ja"
}
-->
# Lesson 11: Model Context Protocol (MCP) Integration

## Model Context Protocol (MCP) の紹介

Model Context Protocol (MCP) は、AIモデルとクライアントアプリケーション間のやり取りを標準化するために設計された最先端のフレームワークです。MCPはAIモデルとそれを利用するアプリケーションの橋渡し役を果たし、基盤となるモデルの実装に関わらず一貫したインターフェースを提供します。

MCPの主な特徴:

- **標準化された通信**: アプリケーションがAIモデルとやり取りするための共通言語を確立
- **強化されたコンテキスト管理**: コンテキスト情報を効率的にAIモデルに渡すことが可能
- **クロスプラットフォーム対応**: C#、Java、JavaScript、Python、TypeScriptなど多様な言語で動作
- **シームレスな統合**: 開発者が異なるAIモデルを簡単にアプリケーションに組み込める

MCPは、AIエージェント開発において特に有用で、エージェントが統一されたプロトコルを通じて様々なシステムやデータソースと連携できるため、より柔軟で強力なエージェントを実現します。

## 学習目標
- MCPとは何か、そしてAIエージェント開発における役割を理解する
- GitHub統合のためにMCPサーバーをセットアップ・構成する
- MCPツールを使ったマルチエージェントシステムを構築する
- Azure Cognitive Searchを用いたRAG（Retrieval Augmented Generation）を実装する

## 前提条件
- Python 3.8以上
- Node.js 14以上
- Azureサブスクリプション
- GitHubアカウント
- Semantic Kernelの基本知識

## セットアップ手順

1. **環境構築**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azureサービスの設定**
   - Azure Cognitive Searchリソースを作成
   - Azure OpenAIサービスをセットアップ
   - `.env`に環境変数を設定

3. **MCPサーバーのセットアップ**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## プロジェクト構成

```
11-mcp/
├── code_samples/
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## コアコンポーネント

### 1. マルチエージェントシステム
- GitHubエージェント: リポジトリ解析
- Hackathonエージェント: プロジェクト推薦
- Eventsエージェント: 技術イベントの提案

### 2. Azure連携
- イベントのインデックス作成にCognitive Searchを使用
- エージェントの知能にAzure OpenAIを活用
- RAGパターンの実装

### 3. MCPツール
- GitHubリポジトリ解析
- コード検査
- メタデータ抽出

## コード解説

サンプルで示す内容:
1. MCPサーバーの統合
2. マルチエージェントのオーケストレーション
3. Azure Cognitive Searchの連携
4. RAGパターンの実装

主な特徴:
- リアルタイムでのGitHubリポジトリ解析
- インテリジェントなプロジェクト推薦
- Azure Searchを用いたイベントマッチング
- Chainlitによるストリーミングレスポンス

## サンプルの実行方法

詳細なセットアップ手順や情報は、[Github MCP Server Example README](./code_samples/github-mcp/README.md)を参照してください。

1. MCPサーバーを起動:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. アプリケーションを起動:
   ```bash
   chainlit run app.py -w
   ```

3. 統合テストを実施:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## トラブルシューティング

よくある問題と対処法:
1. MCP接続の問題
   - サーバーが起動しているか確認
   - ポートの使用状況を確認
   - GitHubトークンの有効性を確認

2. Azure Searchの問題
   - 接続文字列の検証
   - インデックスの存在確認
   - ドキュメントのアップロード確認

## 次のステップ
- 追加のMCPツールを探る
- カスタムエージェントを実装する
- RAG機能を強化する
- さらに多くのイベントソースを追加する

## リソース
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**免責事項**:  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。正式な情報源としては、原文（原言語）の文書を参照してください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、一切の責任を負いかねます。