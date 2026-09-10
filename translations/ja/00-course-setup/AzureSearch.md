# Azure AI 検索セットアップガイド

このガイドでは、Azure ポータルを使って Azure AI 検索をセットアップする方法を説明します。以下の手順に従って Azure AI 検索サービスを作成および設定してください。

## 前提条件

はじめる前に、以下を準備してください:

- Azure サブスクリプション。持っていない場合は、[Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) で無料アカウントを作成できます。

## ステップ 1: Azure ストレージアカウントの作成

1. 次の手順、[Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) に従って新しい Azure ストレージアカウントを作成します。
   <strong>注意</strong>: ストレージアカウントの種類は Standard General Purpose V2 にしてください。

## ステップ 2: Azure AI 検索サービスの作成

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) にサインインします。
2. 左側のナビゲーションペインで **Create a resource** をクリックします。
3. 検索ボックスに「Azure AI Search」と入力し、結果一覧から **Azure AI Search** を選択します。
4. **Create** ボタンをクリックします。
5. **Basics** タブで以下の情報を入力します:
   - **Subscription**: Azure サブスクリプションを選択します。
   - **Resource group**: 新しいリソースグループを作成するか、既存のものを選択します。
   - **Resource name**: 検索サービスのユニークな名前を入力します。
   - **Region**: ユーザーに最も近いリージョンを選択します。
   - **Pricing tier**: 必要に応じたプライシングティアを選択します。テストの場合は無料プランから始められます。
6. **Review + create** をクリックします。
7. 設定内容を確認し、**Create** をクリックして検索サービスを作成します。

## ステップ 3: Azure AI 検索の開始

1. デプロイが完了したら、Azure ポータルで検索サービスに移動します。
2. 検索サービスの概要ペインで URL をコピーします。例: `https://<service-name>.search.windows.net`
3. **（推奨）** Microsoft Entra ID (RBAC) を使ったキー不要アクセスを有効にします（ステップ 4 を参照）—キーは不要です。本ガイドのサンプルはインデックス作成や更新、ドキュメントのアップロードを行うため、**Search Service Contributor** と **Search Index Data Contributor** ロールが必要です（キー認証の場合は、クエリーキーではなく <strong>プライマリアドミンキー</strong> が必要）。RBAC が使えない場合のみ、**Settings > Keys** ペインを開き <strong>プライマリアドミンキー</strong> をコピーしてください。
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) の手順に従い、インデックス作成、データアップロード、検索を行います。

## ステップ 4: Azure AI 検索ツールの使用

Azure AI 検索は様々なツールと統合して検索機能を強化します。高度な設定や操作には Azure CLI、Python SDK、.NET SDK などを使用できます。

### Azure CLI の使用

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) の手順に従い Azure CLI をインストールします。
2. 以下のコマンドで Azure CLI にサインインします:

   ```bash
   az login
   ```
3. **（推奨）Microsoft Entra ID (RBAC) によるキー不要アクセスを有効化:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show には「endpoint」フィールドがないため、サービス名からURLを構築します。
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC を有効にすると、以下の Python および .NET SDK のサンプルは `DefaultAzureCredential` を使って認証します。これはローカル開発時に `az login` セッションを利用し、管理者キーは不要です。[Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) を参照してください。

4. **（フォールバック）キー認証** — RBAC が使えない場合のみ管理者キーを保存します:

#### Azure AI 検索インスタンスのエンドポイントと API キーを環境変数に設定します。

    ```bash
    # zsh/bash
    # az search service show に "endpoint" フィールドはないため、サービス名から URL を構築します。
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show に "endpoint" フィールドはないのでサービス名から URL を構築します。
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK の使用

1. Azure Cognitive Search クライアントライブラリと Azure Identity を Python にインストールします:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. 以下の Python コードを使ってインデックスを作成し、ドキュメントをアップロードします:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless（推奨）：Entra ID RBAC を通じて `az login` の認証情報を使用します。
    # 「Search Service Contributor」と「Search Index Data Contributor」ロールが必要です。
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

1. 次のコマンドでインデックス作成とドキュメントアップロードを行います:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    以下の .NET サンプルは `DefaultAzureCredential` を使用し、ローカル開発時には `az login` での Azure CLI サインインを利用できます。

2. こちらは `AzureSearch.cs` の .NET コードです:

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

詳細は以下のドキュメントを参照してください:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 結論

Azure ポータルおよび統合ツールを使って Azure AI 検索のセットアップに成功しました。これから Azure AI 検索のより高度な機能および能力を活用して検索ソリューションを強化できます。

さらにサポートが必要な場合は、[Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) をご覧ください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->