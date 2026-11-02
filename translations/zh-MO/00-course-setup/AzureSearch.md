# Azure AI Search 設置指南

本指南將協助您透過 Azure 入口網站設置 Azure AI Search。請按照以下步驟創建並配置您的 Azure AI Search 服務。

## 先決條件

開始前，請確保您擁有以下條件：

- 一個 Azure 訂閱。如果您沒有 Azure 訂閱，可以在 [Azure 免費帳戶](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 創建一個免費帳戶。

## 第 1 步：建立 Azure 儲存帳戶

1. 請按照此指示，[建立 Azure 儲存帳戶](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) 建立新的 Azure 儲存帳戶。
   <strong>注意</strong>：請確保儲存帳戶類型為 Standard General Purpose V2。

## 第 2 步：建立 Azure AI Search 服務

1. 登入 [Azure 入口網站](https://portal.azure.com/?wt.mc_id=studentamb_258691)。
2. 在左側導覽窗格中，點擊 <strong>建立資源</strong>。
3. 在搜尋框中輸入 "Azure AI Search"，並從結果列表中選擇 **Azure AI Search**。
4. 點擊 <strong>建立</strong> 按鈕。
5. 在 <strong>基礎知識</strong> 分頁，提供以下資訊：
   - <strong>訂閱</strong>：選擇您的 Azure 訂閱。
   - <strong>資源群組</strong>：建立新的資源群組或選擇現有的。
   - <strong>資源名稱</strong>：輸入您搜尋服務的唯一名稱。
   - <strong>地區</strong>：選擇離您的使用者最近的地區。
   - <strong>定價層級</strong>：選擇符合您的需求的定價層級。您可以先從免費層開始測試。
6. 點擊 **檢閱 + 建立**。
7. 檢閱設定後，點擊 <strong>建立</strong> 以建立搜尋服務。

## 第 3 步：開始使用 Azure AI Search

1. 部署完成後，前往 Azure 入口網站中的搜尋服務頁面。
2. 在搜尋服務概覽窗格中，複製 URL。它應該看起來像 `https://<service-name>.search.windows.net`。
3. **（建議）** 啟用 Microsoft Entra ID (RBAC) 無密鑰存取，如下方第 4 步所示 — 無須金鑰。本指南中的範例會建立/更新索引及上傳文件，這需要 <strong>搜尋服務協作者</strong> 和 <strong>搜尋索引資料協作者</strong> 角色（或者，使用基於金鑰的認證，則需使用 <strong>主要管理金鑰</strong> — 非查詢金鑰）。只有在無法使用 RBAC 時，才開啟 **設定 > 金鑰** 窗格並複製 <strong>主要管理金鑰</strong>。
4. 請參考 [快速入門指南](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) 頁面，建立索引、上傳資料並進行搜尋。

## 第 4 步：使用 Azure AI Search 工具

Azure AI Search 整合多種工具以增強搜尋功能。您可以使用 Azure CLI、Python SDK、.NET SDK 及其他工具進行進階設定及操作。

### 使用 Azure CLI

1. 請按照 [安裝 Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 的說明安裝 Azure CLI。
2. 使用以下命令登入 Azure CLI：

   ```bash
   az login
   ```
3. **（建議）啟用 Microsoft Entra ID (RBAC) 的無密鑰存取：**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    啟用 RBAC 後，下方 Python 和 .NET SDK 範例會使用 `DefaultAzureCredential` 認證，該認證於本機開發階段會使用您的 `az login` 會話 — 無需管理金鑰。詳見 [使用角色連線至 Azure AI Search](https://learn.microsoft.com/azure/search/search-security-rbac)。

4. **（備用）基於金鑰的認證** — 僅在無法使用 RBAC 時，請同時儲存管理金鑰：

#### 將 Azure AI Search 實例的端點和 API 金鑰存入環境變數。

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

### 使用 Python SDK

1. 安裝 Azure Cognitive Search 用戶端程式庫及 Azure Identity for Python：

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. 使用以下 Python 程式碼來建立索引和上傳文件：

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

### 使用 .NET SDK

1. 執行以下命令以建立索引和上傳文件：

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    下方 .NET 範例使用 `DefaultAzureCredential`，本機開發階段可使用您從 `az login` 登入的 Azure CLI。

2. 以下是 `AzureSearch.cs` 的 .NET 程式碼：

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

更多詳細資訊，請參考以下文件：

- [建立 Azure Cognitive Search 服務](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [快速入門 Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search 工具](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 結論

您已成功透過 Azure 入口網站及整合工具設置 Azure AI Search。您現在可以進一步探索 Azure AI Search 的進階功能與能力，以強化您的搜尋解決方案。

如需進一步協助，請造訪 [Azure Cognitive Search 文件](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->