<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "932a1f463f0fcf97090b93b5d0255dff",
  "translation_date": "2025-03-28T11:34:10+00:00",
  "source_file": "00-course-setup\\AzureSearch.md",
  "language_code": "ja"
}
-->
# Azure AI Search セットアップガイド

このガイドでは、Azure ポータルを使用して Azure AI Search をセットアップする方法を説明します。以下の手順に従って、Azure AI Search サービスを作成および構成してください。

## 必要条件

始める前に、以下の条件を満たしていることを確認してください：

- Azure サブスクリプション。Azure サブスクリプションを持っていない場合は、[Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) で無料アカウントを作成できます。

## 手順 1: Azure AI Search サービスを作成する

1. [Azure ポータル](https://portal.azure.com/?wt.mc_id=studentamb_258691) にサインインします。
2. 左側のナビゲーションペインで **リソースの作成** をクリックします。
3. 検索ボックスに「Azure Cognitive Search」と入力し、結果リストから **Azure Cognitive Search** を選択します。
4. **作成** ボタンをクリックします。
5. **基本** タブで以下の情報を入力してください：
   - **サブスクリプション**: 使用する Azure サブスクリプションを選択します。
   - **リソースグループ**: 新しいリソースグループを作成するか、既存のグループを選択します。
   - **リソース名**: 検索サービスの一意の名前を入力します。
   - **リージョン**: ユーザーに最も近いリージョンを選択します。
   - **価格帯**: 必要に応じた価格帯を選択します。テストには無料プランを選択できます。
6. **レビュー + 作成** をクリックします。
7. 設定を確認し、**作成** をクリックして検索サービスを作成します。

## 手順 2: Azure AI Search の開始

1. デプロイメントが完了したら、Azure ポータル内の検索サービスに移動します。
2. 検索サービスの概要ページで **クイックスタート** ボタンをクリックします。
3. クイックスタートガイドに従って、インデックスの作成、データのアップロード、検索クエリの実行を行います。

### インデックスを作成する

1. クイックスタートガイドで **インデックスを作成する** をクリックします。
2. フィールドとその属性（例：データ型、検索可能、フィルタ可能）を指定してインデックススキーマを定義します。
3. **作成** をクリックしてインデックスを作成します。

### データをアップロードする

1. クイックスタートガイドで **データをアップロードする** をクリックします。
2. データソース（例：Azure Blob Storage、Azure SQL Database）を選択し、必要な接続情報を入力します。
3. データソースフィールドをインデックスフィールドにマッピングします。
4. **送信** をクリックしてインデックスにデータをアップロードします。

### 検索クエリを実行する

1. クイックスタートガイドで **検索エクスプローラー** をクリックします。
2. 検索ボックスに検索クエリを入力し、検索機能をテストします。
3. 検索結果を確認し、必要に応じてインデックススキーマやデータを調整します。

## 手順 3: Azure AI Search ツールを利用する

Azure AI Search は、検索機能を強化するためにさまざまなツールと統合されています。Azure CLI、Python SDK などを使用して高度な設定や操作を行うことができます。

### Azure CLI を使用する

1. [Azure CLI のインストール](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) の手順に従って Azure CLI をインストールします。
2. 以下のコマンドを使用して Azure CLI にサインインします：
   ```bash
   az login
   ```
3. Azure CLI を使用して新しい検索サービスを作成します：
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Azure CLI を使用してインデックスを作成します：
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK を使用する

1. Azure Cognitive Search の Python クライアントライブラリをインストールします：
   ```bash
   pip install azure-search-documents
   ```
2. 以下の Python コードを使用してインデックスを作成し、ドキュメントをアップロードします：
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

詳細情報については、以下のドキュメントを参照してください：

- [Azure Cognitive Search サービスを作成する](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Azure Cognitive Search の概要](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search ツール](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 結論

Azure ポータルと統合ツールを使用して Azure AI Search を正常にセットアップしました。これで、Azure AI Search の高度な機能や能力を探索し、検索ソリューションを強化することができます。

さらに支援が必要な場合は、[Azure Cognitive Search ドキュメント](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691) を訪問してください。

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で作成された原文が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用によって生じた誤解や解釈の誤りに関して、当方は責任を負いません。