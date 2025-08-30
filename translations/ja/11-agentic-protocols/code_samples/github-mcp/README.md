<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T10:28:43+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "ja"
}
-->
# Github MCP Server Example

## 説明

これは、Microsoft Reactorが主催したAI Agents Hackathonのために作成されたデモです。

このツールは、ユーザーのGithubリポジトリに基づいてハッカソンプロジェクトを提案するために使用されます。
以下の手順で実現されています：

1. **Github Agent** - Github MCP Serverを使用してリポジトリとその情報を取得します。
2. **Hackathon Agent** - Github Agentから得たデータを基に、ユーザーのプロジェクトや使用言語、AI Agents Hackathonのプロジェクトトラックに基づいて創造的なハッカソンプロジェクトのアイデアを考案します。
3. **Events Agent** - Hackathon Agentの提案に基づいて、AI Agents Hackathonシリーズの関連イベントを推奨します。

## コードの実行方法

### 環境変数

このデモでは、Azure Open AI Service、Semantic Kernel、Github MCP Server、Azure AI Searchを使用します。

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

## Chainlit Serverの実行

MCP Serverに接続するために、このデモではChainlitをチャットインターフェースとして使用します。

サーバーを実行するには、ターミナルで以下のコマンドを使用してください：

```bash
chainlit run app.py -w
```

これにより、`localhost:8000`でChainlitサーバーが起動し、`event-descriptions.md`の内容がAzure AI Search Indexに登録されます。

## MCP Serverへの接続

Github MCP Serverに接続するには、「Type your message here..」チャットボックスの下にある「プラグ」アイコンを選択してください：

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.ja.png)

そこから「Connect an MCP」をクリックして、Github MCP Serverに接続するコマンドを追加します：

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]"を実際のPersonal Access Tokenに置き換えてください。

接続後、プラグアイコンの横に(1)が表示され、接続が確認されます。表示されない場合は、`chainlit run app.py -w`でChainlitサーバーを再起動してみてください。

## デモの使用方法

ハッカソンプロジェクトを提案するエージェントワークフローを開始するには、以下のようなメッセージを入力してください：

"Githubユーザーkoreyspaceのためにハッカソンプロジェクトを提案してください"

Router Agentはリクエストを分析し、どのエージェント（GitHub、Hackathon、Events）の組み合わせが最適かを判断します。エージェントは協力して、Githubリポジトリの分析、プロジェクトのアイデア創出、関連する技術イベントに基づいた包括的な提案を提供します。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。