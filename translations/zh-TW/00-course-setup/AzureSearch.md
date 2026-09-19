# Azure AI 搜尋設定指南

本指南將協助您使用 Azure 入口網站設定 Azure AI 搜尋。請依照以下步驟建立並設定您的 Azure AI 搜尋服務。

## 前置需求

開始之前，請確定您擁有以下項目：

- 一個 Azure 訂閱。如果您沒有 Azure 訂閱，您可以在 [Azure 免費帳戶](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 創建一個免費帳戶。

## 第 1 步：建立 Azure 儲存帳戶

1. 依照此說明，[建立 Azure 儲存帳戶](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) 來建立新的 Azure 儲存帳戶。
   <strong>注意</strong>：請確保儲存帳戶類型為 Standard General Purpose V2。

## 第 2 步：建立 Azure AI 搜尋服務

1. 登入 [Azure 入口網站](https://portal.azure.com/?wt.mc_id=studentamb_258691)。
2. 在左側導覽窗格中，點擊 <strong>建立資源</strong>。
3. 在搜尋框中輸入「Azure AI Search」，並從結果列表中選擇 **Azure AI Search**。
4. 點擊 <strong>建立</strong> 按鈕。
5. 在 <strong>基本資訊</strong> 分頁中，提供以下資訊：
   - <strong>訂閱</strong>：選擇您的 Azure 訂閱。
   - <strong>資源群組</strong>：建立新的資源群組或選擇既有的資源群組。
   - <strong>資源名稱</strong>：輸入您的搜尋服務的唯一名稱。
   - <strong>區域</strong>：選擇離用戶最近的區域。
   - <strong>定價層級</strong>：選擇符合您需求的定價層級。您可以先從免費層級開始測試。
6. 點擊 **檢閱 + 建立**。
7. 檢閱設定後點擊 <strong>建立</strong> 來建立搜尋服務。

## 第 3 步：開始使用 Azure AI 搜尋

1. 部署完成後，在 Azure 入口網站中導覽至您的搜尋服務。
2. 在搜尋服務總覽窗格中，複製 URL。它應該類似 `https://<service-name>.search.windows.net`。
3. **（建議）** 啟用使用 Microsoft Entra ID（RBAC）之無鑰匙存取，如下方第 4 步所示 — 不需鑰匙。本指南的範例會建立／更新索引並上傳文件，這些操作需要擁有 <strong>搜尋服務貢獻者</strong> 及 <strong>搜尋索引資料貢獻者</strong> 角色的權限（或是，使用基於鑰匙的認證，則需要<strong>管理主鑰</strong> — 非查詢鑰匙）。如果無法使用 RBAC，請開啟 **設定 > 金鑰** 窗格並複製 <strong>管理主鑰</strong>。
4. 依照 [快速入門指南](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) 的步驟建立索引、上傳資料並執行搜尋。

## 第 4 步：使用 Azure AI 搜尋工具

Azure AI 搜尋整合了多種工具以增強您的搜尋功能。您可以使用 Azure CLI、Python SDK、.NET SDK 及其他工具進行進階設定及操作。

### 使用 Azure CLI

1. 依照 [安裝 Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 中的說明安裝 Azure CLI。
2. 使用指令登入 Azure CLI：

   ```bash
   az login
   ```
3. **（建議）啟用使用 Microsoft Entra ID（RBAC）的無鑰匙存取：**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show 沒有「endpoint」欄位；從服務名稱建立 URL。
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    啟用 RBAC 後，下方 Python 和 .NET SDK 範例會使用 `DefaultAzureCredential` 進行驗證，該驗證於本機開發過程中會使用您的 `az login` 會話，無需管理鑰匙。請參閱 [使用角色連接 Azure AI 搜尋](https://learn.microsoft.com/azure/search/search-security-rbac)。

4. **（備用方案）基於鑰匙的認證** — 僅當無法使用 RBAC 時，請同時儲存管理鑰匙：

#### 將 Azure AI 搜尋服務的端點與 API 金鑰存入環境變數。

    ```bash
    # zsh/bash
    # az search service show 無“endpoint”欄位；請從服務名稱組成 URL。
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show 無“endpoint”欄位；請從服務名稱組成 URL。
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### 使用 Python SDK

1. 安裝 Azure 認知搜尋客戶端函式庫及 Azure 身份驗證套件：

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. 使用以下 Python 程式碼建立索引並上傳文件：

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # 無鑰匙（建議）：透過 Entra ID RBAC 使用您的 `az login` 身份。
    # 需要「搜尋服務貢獻者」和「搜尋索引資料貢獻者」角色。
    credential = DefaultAzureCredential()
    # 備援（基於金鑰的身份驗證）：
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

1. 執行下列指令建立索引並上傳文件：

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    下列 .NET 範例使用 `DefaultAzureCredential`，其可在本機開發時使用您的 Azure CLI `az login` 登入資訊。

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

詳細資訊請參閱以下文件：

- [建立 Azure 認知搜尋服務](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [開始使用 Azure 認知搜尋](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI 搜尋工具](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 結論

您已成功透過 Azure 入口網站及整合工具設定完成 Azure AI 搜尋。現在您可以探索更進階的 Azure AI 搜尋功能與能力，以強化您的搜尋方案。

如需更多協助，請參閱 [Azure 認知搜尋文件](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->