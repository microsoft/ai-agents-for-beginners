<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:29:04+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ja"
}
-->
# Azure AI Search セットアップガイド

このガイドでは、Azure ポータルを使用して Azure AI Search をセットアップする方法を説明します。以下の手順に従って、Azure AI Search サービスを作成および構成してください。

## 前提条件

始める前に、以下を確認してください：

- Azure サブスクリプション。Azure サブスクリプションをお持ちでない場合は、[Azure 無料アカウント](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)で無料アカウントを作成できます。

## ステップ 1: Azure ストレージアカウントを作成する

1. [Azure ストレージアカウントを作成する](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)の手順に従って、新しい Azure ストレージアカウントを作成してください。
   **NOTE**: ストレージアカウントの種類は Standard General Purpose V2 にしてください。

## ステップ 2: Azure AI Search サービスを作成する

1. [Azure ポータル](https://portal.azure.com/?wt.mc_id=studentamb_258691)にサインインします。
2. 左側のナビゲーションペインで **リソースの作成** をクリックします。
3. 検索ボックスに「Azure AI Search」と入力し、結果リストから **Azure AI Search** を選択します。
4. **作成** ボタンをクリックします。
5. **基本** タブで以下の情報を入力します：
   - **サブスクリプション**: Azure サブスクリプションを選択します。
   - **リソースグループ**: 新しいリソースグループを作成するか、既存のものを選択します。
   - **リソース名**: 検索サービスの一意の名前を入力します。
   - **リージョン**: ユーザーに最も近いリージョンを選択します。
   - **価格レベル**: 要件に合った価格レベルを選択します。テストには無料レベルを選択できます。
6. **レビュー + 作成** をクリックします。
7. 設定を確認し、**作成** をクリックして検索サービスを作成します。

## ステップ 3: Azure AI Search を開始する

1. デプロイが完了したら、Azure ポータルで検索サービスに移動します。
2. 検索サービスの概要ペインで URL をコピーします。形式は `https://<service-name>.search.windows.net` のようになります。
3. 設定 > キー ペインでクエリキーをコピーします。
4. [クイックスタートガイド](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new)の手順に従って、インデックスを作成し、データをアップロードし、検索クエリを実行してください。

## ステップ 4: Azure AI Search ツールを使用する

Azure AI Search は、検索機能を強化するためのさまざまなツールと統合されています。Azure CLI、Python SDK、.NET SDK などのツールを使用して、高度な構成や操作を行うことができます。

### Azure CLI の使用

1. [Azure CLI のインストール](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691)の手順に従って Azure CLI をインストールします。
2. 次のコマンドを使用して Azure CLI にサインインします：

   ```bash
   az login
   ```

3. Azure AI Search インスタンスのエンドポイントと API キーを環境変数に保存します。

    ```bash
    # zsh/bash
    export AZURE_SEARCH_SERVICE_ENDPOINT=$(az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv)
    export AZURE_SEARCH_API_KEY=$(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv
    $env:AZURE_SEARCH_API_KEY = $(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK の使用

1. Azure Cognitive Search クライアントライブラリを Python にインストールします：

   ```bash
   pip install azure-search-documents
   ```

2. 次の Python コードを使用してインデックスを作成し、ドキュメントをアップロードします：

    ```python
    import os
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    api_key = os.getenv("AZURE_SEARCH_API_KEY")
    index_name = "sample-index"

    credential = AzureKeyCredential(api_key)
    index_client = SearchIndexClient(service_endpoint, credential)

    fields = [
        SimpleField(name="id", type=edm.String, key=True),
        SimpleField(name="content", type=edm.String, searchable=True),
    ]

    index = SearchIndex(name=index_name, fields=fields)

    index_client.create_index(index)

    search_client = SearchClient(service_endpoint, index_name, credential)

    documents = [
        {"id": "1", "content": "Hello world"},
        {"id": "2", "content": "Azure Cognitive Search"}
    ]

    search_client.upload_documents(documents)
    ```

### .NET SDK の使用

1. 次のコマンドを実行してインデックスを作成し、ドキュメントをアップロードします：

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. `AzureSearch.cs` の .NET コードは以下の通りです：

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:property PublishAot=false

    using Azure;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var apiKey = Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!;
    var indexName = "sample-index";

    var credential = new AzureKeyCredential(apiKey);
    var indexClient = new SearchIndexClient(serviceEndpoint, credential);

    var fields = new List<SearchField>()
    {
        new SimpleField("id", SearchFieldDataType.String) { IsKey = true },
        new SearchableField("content")
    };

    var index = new SearchIndex(name: indexName, fields: fields);

    var response = await indexClient.CreateOrUpdateIndexAsync(index);
    Console.WriteLine($"Index '{response.Value.Name}' ready.");

    var searchClient = new SearchClient(serviceEndpoint, indexName, credential);

    var documents = new[]
    {
        new { id = "1", content = "Hello world" },
        new { id = "2", content = "Azure Cognitive Search" }
    };

    var result = await searchClient.UploadDocumentsAsync(documents);
    Console.WriteLine($"Uploaded {result.Value.Results.Count} documents to index '{response.Value.Name}'.");
    ```

詳細な情報については、以下のドキュメントを参照してください：

- [Azure Cognitive Search サービスを作成する](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Azure Cognitive Search を開始する](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search ツール](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 結論

Azure ポータルを使用して Azure AI Search を正常にセットアップし、ツールを統合しました。これで、Azure AI Search の高度な機能や能力を探索して、検索ソリューションを強化することができます。

さらに支援が必要な場合は、[Azure Cognitive Search ドキュメント](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)をご覧ください。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。