<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "932a1f463f0fcf97090b93b5d0255dff",
  "translation_date": "2025-03-28T11:32:57+00:00",
  "source_file": "00-course-setup\\AzureSearch.md",
  "language_code": "hk"
}
-->
# Azure AI Search 設置指南

這份指南將幫助你通過 Azure 入口網站設置 Azure AI Search。按照以下步驟創建並配置你的 Azure AI Search 服務。

## 先決條件

在開始之前，請確保你擁有以下內容：

- 一個 Azure 訂閱。如果你沒有 Azure 訂閱，可以在 [Azure 免費帳戶](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 創建一個免費帳戶。

## 步驟 1：創建 Azure AI Search 服務

1. 登錄 [Azure 入口網站](https://portal.azure.com/?wt.mc_id=studentamb_258691)。
2. 在左側導航欄中，點擊 **創建資源**。
3. 在搜索框中輸入 "Azure Cognitive Search"，並從結果列表中選擇 **Azure Cognitive Search**。
4. 點擊 **創建** 按鈕。
5. 在 **基本信息** 標籤中，提供以下信息：
   - **訂閱**：選擇你的 Azure 訂閱。
   - **資源組**：創建一個新的資源組或選擇現有的資源組。
   - **資源名稱**：輸入一個唯一的搜索服務名稱。
   - **區域**：選擇最接近你用戶的區域。
   - **定價層級**：選擇符合你需求的定價層級。你可以從免費層級開始進行測試。
6. 點擊 **查看 + 創建**。
7. 查看設置，然後點擊 **創建** 以創建搜索服務。

## 步驟 2：開始使用 Azure AI Search

1. 部署完成後，進入 Azure 入口網站中的搜索服務。
2. 在搜索服務概覽頁面，點擊 **快速入門** 按鈕。
3. 按照快速入門指南中的步驟創建索引、上傳數據並執行搜索查詢。

### 創建索引

1. 在快速入門指南中，點擊 **創建索引**。
2. 通過指定字段及其屬性（例如數據類型、可搜索、可篩選）來定義索引架構。
3. 點擊 **創建** 以創建索引。

### 上傳數據

1. 在快速入門指南中，點擊 **上傳數據**。
2. 選擇一個數據源（例如 Azure Blob Storage，Azure SQL Database），並提供必要的連接詳情。
3. 將數據源字段映射到索引字段。
4. 點擊 **提交** 將數據上傳到索引。

### 執行搜索查詢

1. 在快速入門指南中，點擊 **搜索瀏覽器**。
2. 在搜索框中輸入搜索查詢以測試搜索功能。
3. 查看搜索結果，並根據需要調整索引架構或數據。

## 步驟 3：使用 Azure AI Search 工具

Azure AI Search 與多種工具集成，能夠提升搜索能力。你可以使用 Azure CLI、Python SDK 和其他工具進行高級配置和操作。

### 使用 Azure CLI

1. 按照 [安裝 Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 的說明安裝 Azure CLI。
2. 使用以下命令登錄 Azure CLI：
   ```bash
   az login
   ```
3. 使用 Azure CLI 創建新的搜索服務：
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. 使用 Azure CLI 創建索引：
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### 使用 Python SDK

1. 安裝 Azure Cognitive Search 的 Python 客戶端庫：
   ```bash
   pip install azure-search-documents
   ```
2. 使用以下 Python 代碼創建索引並上傳文檔：
   ```python
   from azure.core.credentials import AzureKeyCredential
   from azure.search.documents import SearchClient
   from azure.search.documents.indexes import SearchIndexClient
   from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

   service_endpoint = "https://<service-name>.search.windows.net"
   api_key = "<api-key>"

   index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(api_key))

   fields = [
       SimpleField(name="id", type=edm.String, key=True),
       SimpleField(name="content", type=edm.String, searchable=True),
   ]

   index = SearchIndex(name="sample-index", fields=fields)

   index_client.create_index(index)

   search_client = SearchClient(service_endpoint, "sample-index", AzureKeyCredential(api_key))

   documents = [
       {"id": "1", "content": "Hello world"},
       {"id": "2", "content": "Azure Cognitive Search"}
   ]

   search_client.upload_documents(documents)
   ```

更多詳細信息，請參考以下文檔：

- [創建 Azure Cognitive Search 服務](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [開始使用 Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search 工具](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 結論

你已成功通過 Azure 入口網站設置 Azure AI Search 並集成工具。現在可以探索 Azure AI Search 的更多高級功能和能力，以提升你的搜索解決方案。

如需進一步幫助，請訪問 [Azure Cognitive Search 文檔](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691)。

**免責聲明**:  
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為具權威性的來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋概不負責。