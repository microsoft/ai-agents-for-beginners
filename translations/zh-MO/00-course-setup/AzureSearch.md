# Azure AI 搜尋設定指南

本指南將協助您使用 Azure 入口網站設定 Azure AI 搜尋。請依照以下步驟建立並配置您的 Azure AI 搜尋服務。

## 先決條件

在開始之前，請確保您擁有以下條件：

- 一個 Azure 訂閱。如果您尚未擁有 Azure 訂閱，可以在 [Azure 免費帳戶](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 建立免費帳戶。

## 第一步：建立 Azure 儲存體帳戶

1. 請依照此說明，[建立 Azure 儲存體帳戶](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) 來建立新的 Azure 儲存體帳戶。
   <strong>注意</strong>：請確認儲存體帳戶的類型為標準通用型 V2。

## 第二步：建立 Azure AI 搜尋服務

1. 登入 [Azure 入口網站](https://portal.azure.com/?wt.mc_id=studentamb_258691)。
2. 在左側導覽窗格中，點選 <strong>建立資源</strong>。
3. 在搜尋框輸入「Azure AI Search」，並從結果列表中選擇 **Azure AI Search**。
4. 點選 <strong>建立</strong> 按鈕。
5. 在 <strong>基本資料</strong> 分頁中，提供以下資訊：
   - <strong>訂閱</strong>：選擇您的 Azure 訂閱。
   - <strong>資源群組</strong>：建立新的資源群組或選擇現有的資源群組。
   - <strong>資源名稱</strong>：輸入您搜尋服務的唯一名稱。
   - <strong>區域</strong>：選擇距離您的使用者最近的區域。
   - <strong>定價方案</strong>：選擇符合您需求的定價方案。初次測試可從免費方案開始。
6. 點選 **檢閱 + 建立**。
7. 檢閱設定後，點選 <strong>建立</strong> 以建立搜尋服務。

## 第三步：開始使用 Azure AI 搜尋

1. 部署完成後，請在 Azure 入口網站中導覽至您的搜尋服務。
2. 在搜尋服務的概覽窗格中，複製 URL，格式類似 `https://<service-name>.search.windows.net`。
3. **（建議）** 啟用無金鑰訪問與 Microsoft Entra ID (RBAC)，如以下第四步所示 — 無需金鑰。本指南中的範例會建立/更新索引及上傳文件，這需要 <strong>搜尋服務貢獻者</strong> 及 <strong>搜尋索引資料貢獻者</strong> 角色（或金鑰基礎驗證需使用 <strong>主要管理金鑰</strong> — 查詢金鑰無此權限）。若無法使用 RBAC，請開啟 **設定 > 金鑰** 窗格並複製 <strong>主要管理金鑰</strong>。
4. 請依 [快速入門指南](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) 的步驟建立索引、上傳資料及執行搜尋。

## 第四步：使用 Azure AI 搜尋工具

Azure AI 搜尋與多種工具整合，增強您的搜尋功能。您可以使用 Azure CLI、Python SDK、.NET SDK 以及其他工具進行進階設定及操作。

### 使用 Azure CLI

1. 依照說明安裝 Azure CLI，請參考 [安裝 Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691)。
2. 使用以下指令登入 Azure CLI：

   ```bash
   az login
   ```
3. **（建議）啟用無金鑰訪問與 Microsoft Entra ID (RBAC)：**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show 沒有 "endpoint" 欄位；從服務名稱建構 URL。
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    啟用 RBAC 後，以下 Python 和 .NET SDK 範例透過 `DefaultAzureCredential` 進行身份驗證，於本地開發時會使用您的 `az login` 會話 — 無需管理金鑰。詳情請參閱 [使用角色連線到 Azure AI Search](https://learn.microsoft.com/azure/search/search-security-rbac)。

4. **（備用）基於金鑰的驗證** — 僅當無法使用 RBAC 時，請將管理金鑰也儲存：

#### 將 Azure AI Search 實例的端點和 API 金鑰存入環境變數。

    ```bash
    # zsh/bash
    # az search service show 沒有 "endpoint" 欄位；請從服務名稱建立 URL。
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show 沒有 "endpoint" 欄位；請從服務名稱建立 URL。
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### 使用 Python SDK

1. 安裝 Azure Cognitive Search 客戶端庫及 Azure Identity for Python：

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

    # 無需金鑰（建議）：使用您透過 Entra ID RBAC 的 `az login` 身份。
    # 需要「搜尋服務貢獻者」和「搜尋索引資料貢獻者」角色。
    credential = DefaultAzureCredential()
    # 備用（基於金鑰的身份驗證）：
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

1. 執行以下指令建立索引並上傳文件：

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    下面的 .NET 範例使用 `DefaultAzureCredential`，可在本地開發時利用您從 `az login` 登入的 Azure CLI 身份。

2. 這是 `AzureSearch.cs` 的 .NET 程式碼：

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

更多詳細資訊，請參閱以下文件：

- [建立 Azure Cognitive Search 服務](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [開始使用 Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI 搜尋工具](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 結論

您已成功透過 Azure 入口網站及整合工具完成 Azure AI 搜尋的設定。現在，您可以探索 Azure AI 搜尋的更多進階功能與能力，以提升您的搜尋解決方案。

若需進一步協助，請造訪 [Azure Cognitive Search 文件](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->