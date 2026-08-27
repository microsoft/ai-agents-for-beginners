# Azure AI Search セットアップガイド

このガイドでは、Azure ポータルを使用して Azure AI Search をセットアップする方法を説明します。以下の手順に従って、Azure AI Search サービスを作成し、構成してください。

## 前提条件

開始する前に、以下を準備してください：

- Azure サブスクリプション。お持ちでない場合は、[Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) で無料アカウントを作成できます。

## ステップ 1: Azure ストレージアカウントの作成

1. この指示に従って、[Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) で新しい Azure ストレージアカウントを作成します。
   <strong>注意</strong>: ストレージアカウントの種類が Standard General Purpose V2 であることを確認してください。

## ステップ 2: Azure AI Search サービスの作成

1. [Azure ポータル](https://portal.azure.com/?wt.mc_id=studentamb_258691) にサインインします。
2. 左側のナビゲーションペインで、<strong>リソースの作成</strong> をクリックします。
3. 検索ボックスに「Azure AI Search」と入力し、検索結果から **Azure AI Search** を選択します。
4. <strong>作成</strong> ボタンをクリックします。
5. <strong>基本</strong> タブで以下の情報を入力します：
   - <strong>サブスクリプション</strong>: Azure サブスクリションを選択します。
   - <strong>リソースグループ</strong>: 新しいリソースグループを作成するか、既存のものを選択します。
   - <strong>リソース名</strong>: 検索サービスの一意の名前を入力します。
   - <strong>リージョン</strong>: ユーザーに最も近いリージョンを選択します。
   - <strong>価格レベル</strong>: 要件に合った価格レベルを選択します。テスト用には Free レベルから始めることができます。
6. <strong>確認および作成</strong> をクリックします。
7. 設定を確認し、<strong>作成</strong> をクリックして検索サービスを作成します。

## ステップ 3: Azure AI Search の開始

1. 展開が完了したら、Azure ポータルの検索サービスに移動します。
2. 検索サービスの概要ペインで URL をコピーします。`https://<service-name>.search.windows.net` の形式です。
3. **（推奨）** キーレスアクセスを Microsoft Entra ID (RBAC) で有効にしてください（以下のステップ 4 参照）。キーは不要です。このガイドのサンプルでは、インデックスの作成/更新やドキュメントのアップロードを行いますが、これには **Search Service Contributor** および **Search Index Data Contributor** ロール（またはキー認証の場合は **primary admin key** - クエリキーではありません）が必要です。RBAC が使えない場合のみ、**設定 > キー** ペインを開き、**primary admin key** をコピーしてください。
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) の手順に従って、インデックスを作成し、データをアップロードし、検索を実行します。

## ステップ 4: Azure AI Search ツールの利用

Azure AI Search は様々なツールと統合して、検索機能を強化します。Azure CLI、Python SDK、.NET SDK などを使用して高度な構成や操作が可能です。

### Azure CLI の使用

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) の手順に従って Azure CLI をインストールします。
2. 以下のコマンドで Azure CLI にサインインします：

   ```bash
   az login
   ```
3. **（推奨）Microsoft Entra ID (RBAC) でキーレスアクセスを有効にする：**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show に "endpoint" フィールドはありません；URLはサービス名から構築します。
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC を有効にすると、以下の Python および .NET SDK のサンプルでは `DefaultAzureCredential` が認証に使われ、ローカル開発時の `az login` セッションを利用するため、管理者キーは不要です。詳細は [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) をご覧ください。

4. **（フォールバック）キー認証** — RBAC が使えない場合のみ、管理者キーも保存します：

#### Azure AI Search インスタンスのエンドポイントと API キーの両方を環境変数に保存します。

    ```bash
    # zsh/bash
    # az search service show は "endpoint" フィールドを持ちません。サービス名から URL を構築します。
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show は "endpoint" フィールドを持ちません。サービス名から URL を構築します。
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK の使用

1. Azure Cognitive Search クライアントライブラリと Azure Identity for Python をインストールします：

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. 以下の Python コードを使用して、インデックスの作成およびドキュメントのアップロードを行います：

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # キーレス（推奨）：Entra ID RBACを通じて `az login` のIDを使用します。
    # "Search Service Contributor" と "Search Index Data Contributor" ロールが必要です。
    credential = DefaultAzureCredential()
    # フォールバック（キー認証）：
    # azure.core.credentials から AzureKeyCredential をインポートします
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

1. 以下のコマンドを実行して、インデックスの作成およびドキュメントのアップロードを行います：

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    以下の .NET サンプルは `DefaultAzureCredential` を使用し、ローカル開発時には `az login` での Azure CLI サインインを利用できます。

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

詳しくは以下のドキュメントを参照してください：

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## まとめ

Azure ポータルと統合ツールを使用して、Azure AI Search のセットアップが正常に完了しました。これで、Azure AI Search の高度な機能や性能を活用して検索ソリューションを強化できます。

さらにサポートが必要な場合は、[Azure Cognitive Search のドキュメント](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)をご覧ください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->