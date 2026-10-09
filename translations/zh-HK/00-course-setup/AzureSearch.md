# Azure AI 搜尋設置指南

本指南將協助您使用 Azure 入口網站設定 Azure AI 搜尋。請按照以下步驟建立並配置您的 Azure AI 搜尋服務。

## 先決條件

開始之前，請確保您擁有以下項目：

- 一個 Azure 訂閱。如果您沒有 Azure 訂閱，可以於 [Azure 免費帳戶](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 創建免費帳戶。

## 第一步：建立 Azure 儲存帳戶

1. 請遵循此指示，[建立 Azure 儲存帳戶](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) 開啟頁面，建立新的 Azure 儲存帳戶。
   <strong>注意</strong>：請確保儲存帳戶類型為 Standard General Purpose V2。

## 第二步：建立 Azure AI 搜尋服務

1. 登入 [Azure 入口網站](https://portal.azure.com/?wt.mc_id=studentamb_258691)。
2. 在左側導覽窗格中，按一下 <strong>建立資源</strong>。
3. 在搜尋框中輸入「Azure AI Search」，並從結果清單中選擇 **Azure AI Search**。
4. 按下 <strong>建立</strong> 按鈕。
5. 在 <strong>基本資料</strong> 標籤下，提供以下資訊：
   - <strong>訂閱</strong>：選擇您的 Azure 訂閱。
   - <strong>資源群組</strong>：建立新的資源群組或選擇現有資源群組。
   - <strong>資源名稱</strong>：輸入唯一的搜尋服務名稱。
   - <strong>區域</strong>：選擇離您用戶最近的區域。
   - <strong>價格層級</strong>：選擇符合您需求的價格層級。您可以開始使用免費層測試。
6. 按 **檢閱 + 建立**。
7. 檢閱設定，然後按一下 <strong>建立</strong>，建立搜尋服務。

## 第三步：開始使用 Azure AI Search

1. 部署完成後，於 Azure 入口網站中導航至您的搜尋服務。
2. 在搜尋服務概觀窗格中，複製 URL。格式應為 `https://<service-name>.search.windows.net`。
3. <strong>（建議）</strong>啟用使用 Microsoft Entra ID（RBAC）無密鑰存取，如下方第 4 步所示 — 不需密鑰。本指南內的範例進行建立／更新索引及上傳文件，需求 <strong>搜尋服務貢獻者</strong> 與 <strong>搜尋索引資料貢獻者</strong> 角色（或使用基於密鑰驗證，則使用 <strong>主要管理密鑰</strong> — 非查詢密鑰）。若無法使用 RBAC，請開啟 **設定 > 金鑰** 窗格並複製 <strong>主要管理密鑰</strong>。
4. 按照 [快速入門指南](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) 中的步驟建立索引、上傳資料並執行搜尋。

## 第四步：使用 Azure AI 搜尋工具

Azure AI 搜尋整合多種工具以增強您的搜尋功能。您可以使用 Azure CLI、Python SDK、.NET SDK 及其他工具進行進階配置與操作。

### 使用 Azure CLI

1. 按照 [安裝 Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 的指示安裝 Azure CLI。
2. 使用以下命令登入 Azure CLI：

   ```bash
   az login
   ```
3. **（建議）啟用使用 Microsoft Entra ID（RBAC）無密鑰存取：**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show 沒有 "endpoint" 欄位；從服務名稱構建 URL。
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    啟用 RBAC 後，下方 Python 與 .NET SDK 範例會使用 `DefaultAzureCredential` 認證，該方式在本機開發時會使用您的 `az login` 會話 — 不需管理密鑰。詳細資訊請見 [使用角色連接到 Azure AI 搜尋](https://learn.microsoft.com/azure/search/search-security-rbac)。

4. **（替代方案）基於密鑰的驗證** — 若無法使用 RBAC，請同時儲存管理密鑰：

#### 將 Azure AI 搜尋服務的端點與 API 密鑰存到環境變數。

    ```bash
    # zsh/bash
    # az search service show 沒有 "endpoint" 欄位，需自行從服務名稱組成 URL。
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show 沒有 "endpoint" 欄位，需自行從服務名稱組成 URL。
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### 使用 Python SDK

1. 安裝 Azure Cognitive Search 用戶端程式庫及 Azure Identity for Python：

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. 使用下列 Python 程式碼建立索引並上傳文件：

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # 無需金鑰（建議）：透過 Entra ID RBAC 使用你的 `az login` 身份。
    # 需要 "Search Service Contributor" 和 "Search Index Data Contributor" 角色。
    credential = DefaultAzureCredential()
    # 備用方案（基於金鑰認證）：
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

    下方 .NET 範例使用 `DefaultAzureCredential`，可在本機開發時利用您透過 `az login` 登入的 Azure CLI。

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
- [開始使用 Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI 搜尋工具](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 結論

您已成功使用 Azure 入口網站及整合工具設定 Azure AI 搜尋。接下來您可以探索 Azure AI 搜尋的進階功能與能力，強化您的搜尋解決方案。

如需進一步協助，請造訪 [Azure Cognitive Search 文件](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->