<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:34:43+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ja"
}
-->
# Azure AI Search セットアップガイド

このガイドでは、Azure ポータルを使って Azure AI Search をセットアップする方法を説明します。以下の手順に従って、Azure AI Search サービスを作成および構成してください。

## 前提条件

始める前に、以下のものが揃っていることを確認してください。

- Azure サブスクリプション。まだお持ちでない場合は、[Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) から無料アカウントを作成できます。

## ステップ 1: Azure AI Search サービスの作成

1. [Azure ポータル](https://portal.azure.com/?wt.mc_id=studentamb_258691) にサインインします。
2. 左側のナビゲーションペインで **Create a resource** をクリックします。
3. 検索ボックスに「Azure AI Search」と入力し、結果一覧から **Azure AI Search** を選択します。
4. **Create** ボタンをクリックします。
5. **Basics** タブで以下の情報を入力します：
   - **Subscription**: ご自身の Azure サブスクリプションを選択します。
   - **Resource group**: 新しいリソースグループを作成するか、既存のものを選択します。
   - **Resource name**: 検索サービスの一意の名前を入力します。
   - **Region**: ユーザーに最も近いリージョンを選択します。
   - **Pricing tier**: ご要望に合った料金プランを選択します。テスト用には Free プランから始めることができます。
6. **Review + create** をクリックします。
7. 設定内容を確認し、**Create** をクリックして検索サービスを作成します。

## ステップ 2: Azure AI Search の使い始め

1. デプロイが完了したら、Azure ポータルで検索サービスに移動します。
2. 検索サービスの概要ページで **Quickstart** ボタンをクリックします。
3. Quickstart ガイドの手順に従い、インデックスの作成、データのアップロード、検索クエリの実行を行います。

### インデックスの作成

1. Quickstart ガイドで **Create an index** をクリックします。
2. フィールドとその属性（例：データ型、検索可能、フィルター可能）を指定してインデックススキーマを定義します。
3. **Create** をクリックしてインデックスを作成します。

### データのアップロード

1. Quickstart ガイドで **Upload data** をクリックします。
2. データソース（例：Azure Blob Storage、Azure SQL Database）を選択し、必要な接続情報を入力します。
3. データソースのフィールドをインデックスのフィールドにマッピングします。
4. **Submit** をクリックしてデータをインデックスにアップロードします。

### 検索クエリの実行

1. Quickstart ガイドで **Search explorer** をクリックします。
2. 検索ボックスにクエリを入力して検索機能をテストします。
3. 検索結果を確認し、必要に応じてインデックススキーマやデータを調整します。

## ステップ 3: Azure AI Search ツールの利用

Azure AI Search はさまざまなツールと連携して検索機能を強化できます。高度な設定や操作には Azure CLI、Python SDK などを利用できます。

### Azure CLI の使用

1. [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) の手順に従って Azure CLI をインストールします。
2. 以下のコマンドで Azure CLI にサインインします：
   ```bash
   az login
   ```
3. Azure CLI を使って新しい検索サービスを作成します：
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Azure CLI でインデックスを作成します：
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK の使用

1. Python 用の Azure Cognitive Search クライアントライブラリをインストールします：
   ```bash
   pip install azure-search-documents
   ```
2. 以下の Python コードを使ってインデックスを作成し、ドキュメントをアップロードします：
   ```python
   from azure.core.credentials import AzureKeyCredential
   from azure.search.documents import SearchClient
   from azure.search.documents.indexes import SearchIndexClient
   from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

   service_endpoint = "https://<service-name>.search.windows.net"
   api_key = "<api-key>"

   index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(api_key))

   fields = [
       SimpleField(name="id", type=edm.String, key=True),
       SimpleField(name="content", type=edm.String, searchable=True),
   ]

   index = SearchIndex(name="sample-index", fields=fields)

   index_client.create_index(index)

   search_client = SearchClient(service_endpoint, "sample-index", AzureKeyCredential(api_key))

   documents = [
       {"id": "1", "content": "Hello world"},
       {"id": "2", "content": "Azure Cognitive Search"}
   ]

   search_client.upload_documents(documents)
   ```

詳細については、以下のドキュメントを参照してください：

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## まとめ

Azure ポータルと連携ツールを使って Azure AI Search のセットアップが完了しました。これで、Azure AI Search のより高度な機能や可能性を活用して、検索ソリューションを強化できます。

さらにサポートが必要な場合は、[Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691) をご覧ください。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。