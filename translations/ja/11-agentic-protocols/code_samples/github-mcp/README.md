<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T00:19:13+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "ja"
}
-->
# Github MCP Server Example

## 説明

これは、Microsoft Reactorが主催したAIエージェントハッカソンのために作成されたデモです。

このツールは、ユーザーのGithubリポジトリに基づいてハッカソンプロジェクトを推薦するためのものです。以下の手順で実現します：

1. **Githubエージェント** - Github MCPサーバーを使用してリポジトリやその情報を取得します。
2. **ハッカソンエージェント** - Githubエージェントから得たデータを基に、ユーザーのプロジェクトや使用言語、AIエージェントハッカソンのプロジェクトトラックに基づいて創造的なハッカソンプロジェクトのアイデアを考案します。
3. **イベントエージェント** - ハッカソンエージェントの提案に基づき、AIエージェントハッカソンシリーズの関連イベントを推薦します。

## コードの実行方法

### 環境変数

このデモでは、Azure Open AI Service、Semantic Kernel、Github MCPサーバー、Azure AI Searchを使用します。

これらのツールを使用するために、適切な環境変数を設定してください：

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlitサーバーの実行

MCPサーバーに接続するために、このデモではChainlitをチャットインターフェースとして使用します。

サーバーを実行するには、ターミナルで以下のコマンドを使用してください：

```bash
chainlit run app.py -w
```

これにより、`localhost:8000`でChainlitサーバーが起動し、`event-descriptions.md`の内容がAzure AI Search Indexに登録されます。

## MCPサーバーへの接続

Github MCPサーバーに接続するには、「Type your message here..」チャットボックスの下にある「プラグ」アイコンを選択してください：

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.ja.png)

そこから「Connect an MCP」をクリックして、Github MCPサーバーに接続するコマンドを追加します：

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]"を実際のPersonal Access Tokenに置き換えてください。

接続が成功すると、プラグアイコンの横に(1)が表示され、接続が確認されます。表示されない場合は、`chainlit run app.py -w`でChainlitサーバーを再起動してみてください。

## デモの使用方法

ハッカソンプロジェクトを推薦するエージェントワークフローを開始するには、以下のようなメッセージを入力してください：

"Githubユーザーkoreyspaceのためにハッカソンプロジェクトを推薦してください"

ルーターエージェントがリクエストを分析し、どのエージェント（GitHub、ハッカソン、イベント）の組み合わせが最適かを判断します。エージェントは協力して、Githubリポジトリの分析、プロジェクトのアイデア出し、関連する技術イベントに基づいた包括的な推薦を提供します。

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。