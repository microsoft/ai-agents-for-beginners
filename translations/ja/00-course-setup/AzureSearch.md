# Azure AI Search セットアップガイド

このガイドでは、Azure ポータルを使用して Azure AI Search をセットアップする方法を説明します。以下の手順に従って、Azure AI Search サービスを作成および構成してください。

## 前提条件

開始する前に、以下のものがあることを確認してください：

- Azure サブスクリプション。サブスクリプションをお持ちでない場合は、[Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) で無料アカウントを作成できます。

## ステップ 1: Azure ストレージアカウントの作成

1. [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) の手順に従い、新しい Azure ストレージアカウントを作成します。
   <strong>注意</strong>: ストレージアカウントの種類は Standard General Purpose V2 であることを確認してください。

## ステップ 2: Azure AI Search サービスの作成

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) にサインインします。
2. 左側のナビゲーションペインで **Create a resource** をクリックします。
3. 検索ボックスに「Azure AI Search」と入力し、結果の一覧から **Azure AI Search** を選択します。
4. **Create** ボタンをクリックします。
5. **Basics** タブで、以下の情報を入力します：
   - **Subscription**: Azure サブスクリプションを選択します。
   - **Resource group**: 新しいリソースグループを作成するか、既存のものを選択します。
   - **Resource name**: 検索サービスの一意の名前を入力します。
   - **Region**: ユーザーに最も近いリージョンを選択します。
   - **Pricing tier**: 要件に合った価格帯を選択します。テストには Free tier から始めることができます。
6. **Review + create** をクリックします。
7. 設定内容を確認し、**Create** をクリックして検索サービスを作成します。

## ステップ 3: Azure AI Search の開始

1. デプロイ完了後、Azure ポータルで検索サービスのページへ移動します。
2. 検索サービス概要ペインで URL をコピーします。URL は `https://<service-name>.search.windows.net` のようになっています。
3. **（推奨）** Microsoft Entra ID (RBAC) によるキー不要アクセスを有効にします（以下のステップ 4 を参照）— キーは不要です。このガイドのサンプルはインデックスの作成／更新やドキュメントのアップロードを行いますが、これには **Search Service Contributor** と **Search Index Data Contributor** のロールが必要です（または、キー認証の場合は **primary admin key** — クエリーキーではありません）。RBAC を使えない場合のみ、**Settings > Keys** ペインを開き、**primary admin key** をコピーしてください。
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) の手順に従って、インデックスの作成、データのアップロード、検索の実行を行います。

## ステップ 4: Azure AI Search ツールの使用

Azure AI Search はさまざまなツールと統合して検索機能を強化します。高度な設定・操作には Azure CLI、Python SDK、.NET SDK などを利用できます。

### Azure CLI の使用

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) の指示に従って Azure CLI をインストールします。
2. 以下のコマンドで Azure CLI にサインインします：

   ```bash
   az login
   ```
3. **（推奨）Microsoft Entra ID (RBAC) によるキー不要アクセスの有効化：**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC 有効時、以下の Python/.NET SDK サンプルは `DefaultAzureCredential` で認証し、`az login` セッションをローカル開発時に利用するため、管理者キーは不要です。[Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) を参照してください。

4. **（代替）キー認証** — RBAC が使えない場合のみ、管理者キーも保存します：

#### Azure AI Search インスタンスのエンドポイントと API キーを環境変数に保存します。

   * **zsh / bash**
     ```bash
     # az search service show has no "endpoint" field; build the URL from the service name.
     export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
     export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

   * **PowerShell**
     ```powershell
     # az search service show has no "endpoint" field; build the URL from the service name.
     $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
     $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

### Python SDK の使用

1. Azure Cognitive Search クライアントライブラリと Azure Identity for Python をインストールします：

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. 以下の Python コードでインデックスを作成し、ドキュメントをアップロードします：

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    # Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    credential = DefaultAzureCredential()
    # Fallback (key-based auth):
    # from azure.core.credentials import AzureKeyCredential
    # credential = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
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

1. 以下のコマンドでインデックスを作成し、ドキュメントをアップロードします：

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    以下の .NET サンプルは `DefaultAzureCredential` を使用し、ローカル開発時には `az login` から Azure CLI のサインイン情報を利用できます。

2. `AzureSearch.cs` の .NET コードはこちらです：

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:package Azure.Identity@1.21.0
    #:property PublishAot=false

    using Azure;
    using Azure.Identity;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var indexName = "sample-index";

    // Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    // Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    var credential = new DefaultAzureCredential();
    // Fallback (key-based auth): the `using Azure;` directive above already imports
    // AzureKeyCredential; replace the credential line above with:
    // var credential = new AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!);
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

詳細な情報は、以下のドキュメントを参照してください：

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 結論

Azure ポータルと統合ツールを使用して Azure AI Search のセットアップが完了しました。これで、Azure AI Search のより高度な機能や機能強化を活用して検索ソリューションを向上させることができます。

さらなるサポートが必要な場合は、[Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) をご覧ください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->