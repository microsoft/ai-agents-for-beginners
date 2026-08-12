# Github MCP Server の例

## 説明

これは Microsoft Reactor で開催された AI Agents ハッカソンのために作成されたデモです。

このツールはユーザーの Github リポジトリに基づいてハッカソンプロジェクトを推奨するために使用されます。
これは次の方法で行われます:

1. **Github Agent** - Github MCP Server を使ってリポジトリとそれらの情報を取得します。
2. **Hackathon Agent** - Github Agent からのデータを受け取り、ユーザーが使用しているプロジェクトや言語、AI Agents ハッカソンのプロジェクトトラックに基づいて創造的なハッカソンプロジェクトのアイデアを考案します。
3. **Events Agent** - Hackathon Agent の提案に基づいて、Events Agent は AI Agent ハッカソンシリーズの関連イベントを推奨します。

## コードの実行 

### 環境変数

このデモは Microsoft Agent Framework、Azure OpenAI Service、Github MCP Server、Azure AI Search を使用します。

これらのツールを使用するために、適切な環境変数が設定されていることを確認してください:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit サーバーの実行

MCP サーバーに接続するために、このデモではチャットインターフェイスとして Chainlit を使用します。 

サーバーを実行するには、ターミナルで次のコマンドを使用してください:

```bash
chainlit run app.py -w
```

これにより `localhost:8000` 上で Chainlit サーバーが起動し、`event-descriptions.md` の内容で Azure AI Search インデックスが登録されるはずです。 

## MCP サーバーへの接続

Github MCP Server に接続するには、チャットボックスの "Type your message here.." の下にある「plug」アイコンを選択してください:

![MCP 接続](../../../../../translated_images/ja/mcp-chainlit-1.7ed66d648e3cfb28.webp)

そこから "Connect an MCP" をクリックして、Github MCP Server に接続するコマンドを追加できます:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" を実際の Personal Access Token に置き換えてください。 

接続後、接続が確認できるようにプラグアイコンの横に (1) が表示されるはずです。表示されない場合は、`chainlit run app.py -w` で chainlit サーバーを再起動してみてください。

## デモの使用方法 

ハッカソンプロジェクトを推奨するエージェントワークフローを開始するには、次のようなメッセージを入力できます: 

"Github ユーザー koreyspace のためにハッカソンプロジェクトを推奨してください"

Router Agent はリクエストを分析し、どの組み合わせのエージェント（GitHub、Hackathon、Events）がクエリに最適かを判断します。エージェントは協力して、GitHub リポジトリの分析、プロジェクトのアイデア化、および関連する技術イベントに基づいた包括的な推奨を提供します。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責事項：
本書は AI 翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を用いて翻訳されました。正確性には努めていますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご了承ください。原文（原言語での文書）を正式な出典と見なしてください。重要な情報については専門の人間による翻訳を推奨します。本翻訳の利用に起因するいかなる誤解や誤訳についても責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
