# Azure AI 搜尋設定指南

本指南將協助您透過 Azure 入口網站設定 Azure AI 搜尋。請依照以下步驟建立並配置您的 Azure AI 搜尋服務。

## 先決條件

開始之前，請確保您具備以下條件：

- 一個 Azure 訂閱。如果您尚無 Azure 訂閱，可以在[Azure 免費帳戶](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)建立免費帳戶。

## 步驟 1：建立 Azure 儲存帳戶

1. 請參考此說明 [建立 Azure 儲存帳戶](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) 來建立新的 Azure 儲存帳戶。
   <strong>注意</strong>：請確保儲存帳戶的類型為 Standard General Purpose V2。

## 步驟 2：建立 Azure AI 搜尋服務

1. 登入 [Azure 入口網站](https://portal.azure.com/?wt.mc_id=studentamb_258691)。
2. 在左側導覽窗格中，點選 <strong>建立資源</strong>。
3. 在搜尋框中，輸入「Azure AI Search」，然後從結果列表中選擇 **Azure AI Search**。
4. 點擊 <strong>建立</strong> 按鈕。
5. 在 <strong>基本資料</strong> 頁籤中，提供以下資訊：
   - <strong>訂閱</strong>：選擇您的 Azure 訂閱。
   - <strong>資源群組</strong>：建立新的資源群組或選擇現有的。
   - <strong>資源名稱</strong>：輸入您搜尋服務的唯一名稱。
   - <strong>區域</strong>：選擇最接近您用戶的區域。
   - <strong>定價方案</strong>：選擇適合您需求的價格方案。測試階段可從免費方案開始。
6. 點擊 **檢閱 + 建立**。
7. 檢閱設定後，點擊 <strong>建立</strong> 以建立搜尋服務。

## 步驟 3：開始使用 Azure AI 搜尋

1. 部署完成後，前往 Azure 入口網站中的搜尋服務頁面。
2. 在搜尋服務概覽窗格中，複製 URL。其格式應為 `https://<service-name>.search.windows.net`。
3. **（建議）** 啟用 Microsoft Entra ID（RBAC）的無金鑰存取，如下 第 4 步所示 — 不需金鑰。本指南範例會建立/更新索引並上傳文件，這需要 <strong>搜尋服務貢獻者</strong> 和 <strong>搜尋索引資料貢獻者</strong> 角色（或使用金鑰授權時，需要<strong>主要管理金鑰</strong> — 不同於查詢金鑰）。只有當您無法使用 RBAC 時，才開啟 **設定 > 金鑰** 頁籤並複製 <strong>主要管理金鑰</strong>。
4. 依照[快速入門指南](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new)的步驟建立索引、上傳資料並執行搜尋。

## 步驟 4：使用 Azure AI 搜尋工具

Azure AI 搜尋整合多種工具以提升搜尋功能。您可以使用 Azure CLI、Python SDK、.NET SDK 以及其他工具進行進階設定與操作。

### 使用 Azure CLI

1. 按照[安裝 Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691)說明安裝 Azure CLI。
2. 使用命令登入 Azure CLI：

   ```bash
   az login
   ```
3. **（建議）啟用 Microsoft Entra ID（RBAC）的無金鑰存取：**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show 沒有 "endpoint" 欄位；從服務名稱構建 URL。
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    啟用 RBAC 後，以下 Python 和 .NET SDK 範例會使用 `DefaultAzureCredential` 進行驗證，該驗證會在本機開發時利用您的 `az login` 工作階段 — 不需要管理金鑰。詳見 [使用角色連接至 Azure AI 搜尋](https://learn.microsoft.com/azure/search/search-security-rbac)。

4. **（備用方案）基於金鑰的驗證** — 僅當無法使用 RBAC 時，也請儲存管理金鑰：

#### 將 Azure AI 搜尋服務的端點與 API 金鑰存到環境變數。

    ```bash
    # zsh/bash
    # az search service show 中沒有 "endpoint" 欄位；請自行由服務名稱組建 URL。
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show 中沒有 "endpoint" 欄位；請自行由服務名稱組建 URL。
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### 使用 Python SDK

1. 安裝 Azure 認知搜尋客戶端函式庫及 Azure Identity for Python：

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. 使用以下 Python 代碼建立索引並上傳文件：

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # 無金鑰（建議）：透過 Entra ID RBAC 使用您的 `az login` 身份。
    # 需要「搜尋服務貢獻者」和「搜尋索引資料貢獻者」角色。
    credential = DefaultAzureCredential()
    # 備援（金鑰驗證）：
    # 從 azure.core.credentials 匯入 AzureKeyCredential
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

1. 執行以下命令建立索引並上傳文件：

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    以下 .NET 範例使用 `DefaultAzureCredential`，可在本機開發時利用您透過 `az login` 所登入的 Azure CLI。

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

更多詳細資訊，請參閱下列文件：

- [建立 Azure 認知搜尋服務](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [開始使用 Azure 認知搜尋](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI 搜尋工具](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 結論

您已成功透過 Azure 入口網站與整合的工具設定 Azure AI 搜尋。現在，您可以進一步探索 Azure AI 搜尋的更多進階功能與能力，以強化您的搜尋解決方案。

如需進一步協助，請造訪[Azure 認知搜尋文件](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->