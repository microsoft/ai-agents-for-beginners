<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:27:09+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "mo"
}
-->
# Azure AI Search 設定指南

本指南將幫助您使用 Azure 入口網站設置 Azure AI Search。請按照以下步驟創建並配置您的 Azure AI Search 服務。

## 先決條件

在開始之前，請確保您具備以下條件：

- 一個 Azure 訂閱。如果您尚未擁有 Azure 訂閱，可以在 [Azure 免費帳戶](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 創建一個免費帳戶。

## 步驟 1：創建 Azure 儲存帳戶

1. 按照此說明 [創建 Azure 儲存帳戶](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) 創建一個新的 Azure 儲存帳戶。  
   **注意**：請確保儲存帳戶的類型為 Standard General Purpose V2。

## 步驟 2：創建 Azure AI Search 服務

1. 登錄 [Azure 入口網站](https://portal.azure.com/?wt.mc_id=studentamb_258691)。
2. 在左側導航窗格中，點擊 **創建資源**。
3. 在搜索框中輸入 "Azure AI Search"，並從結果列表中選擇 **Azure AI Search**。
4. 點擊 **創建** 按鈕。
5. 在 **基本資訊** 標籤中，提供以下信息：
   - **訂閱**：選擇您的 Azure 訂閱。
   - **資源群組**：創建一個新的資源群組或選擇現有的資源群組。
   - **資源名稱**：輸入您的搜索服務的唯一名稱。
   - **區域**：選擇最接近您用戶的區域。
   - **定價層**：選擇適合您需求的定價層。您可以從免費層開始進行測試。
6. 點擊 **檢閱 + 建立**。
7. 檢查設置，然後點擊 **建立** 以創建搜索服務。

## 步驟 3：開始使用 Azure AI Search

1. 部署完成後，導航到 Azure 入口網站中的搜索服務。
2. 在搜索服務概覽窗格中，複製 URL。它應該類似於 `https://<service-name>.search.windows.net`。
3. 在 **設置 > 金鑰** 窗格中，複製查詢金鑰。
4. 按照 [快速入門指南](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) 頁面上的步驟創建索引、上傳數據並執行搜索查詢。

## 步驟 4：使用 Azure AI Search 工具

Azure AI Search 與各種工具集成，以增強您的搜索功能。您可以使用 Azure CLI、Python SDK、.NET SDK 和其他工具進行高級配置和操作。

### 使用 Azure CLI

1. 按照 [安裝 Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 的說明安裝 Azure CLI。
2. 使用以下命令登錄 Azure CLI：

   ```bash
   az login
   ```

3. 將 Azure AI Search 實例的端點和 API 金鑰存儲到環境變數中。

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

### 使用 Python SDK

1. 安裝 Azure 語義搜索的 Python 客戶端庫：

   ```bash
   pip install azure-search-documents
   ```

2. 使用以下 Python 代碼創建索引並上傳文檔：

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

### 使用 .NET SDK

1. 運行以下命令創建索引並上傳文檔：

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. 以下是 `AzureSearch.cs` 的 .NET 代碼：

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

有關更詳細的信息，請參考以下文檔：

- [創建 Azure 語義搜索服務](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [開始使用 Azure 語義搜索](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search 工具](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 結論

您已成功使用 Azure 入口網站設置了 Azure AI Search 並集成了相關工具。現在，您可以探索 Azure AI Search 的更多高級功能和能力，以增強您的搜索解決方案。

如需進一步的幫助，請訪問 [Azure 語義搜索文檔](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。