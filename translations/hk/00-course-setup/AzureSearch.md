<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:34:23+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "hk"
}
-->
# Azure AI Search 設定指南

本指南將協助你透過 Azure 入口網站設定 Azure AI Search。請依照以下步驟建立並配置你的 Azure AI Search 服務。

## 前置條件

開始之前，請確保你具備以下條件：

- 一個 Azure 訂閱。如果你還沒有 Azure 訂閱，可以在 [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 創建免費帳戶。

## 步驟 1：建立 Azure AI Search 服務

1. 登入 [Azure 入口網站](https://portal.azure.com/?wt.mc_id=studentamb_258691)。
2. 在左側導覽窗格中，點擊 **建立資源**。
3. 在搜尋框中輸入「Azure AI Search」，並從結果列表中選擇 **Azure AI Search**。
4. 點擊 **建立** 按鈕。
5. 在 **基本資料** 標籤頁，填寫以下資訊：
   - **訂閱**：選擇你的 Azure 訂閱。
   - **資源群組**：建立新的資源群組或選擇現有的。
   - **資源名稱**：輸入你的搜尋服務的唯一名稱。
   - **區域**：選擇最接近使用者的區域。
   - **定價層級**：選擇符合需求的定價層級。你可以先從免費層級開始測試。
6. 點擊 **檢閱 + 建立**。
7. 檢查設定後，點擊 **建立** 以建立搜尋服務。

## 步驟 2：開始使用 Azure AI Search

1. 部署完成後，前往 Azure 入口網站中的搜尋服務。
2. 在搜尋服務概覽頁面，點擊 **快速入門** 按鈕。
3. 按照快速入門指南的步驟建立索引、上傳資料，並執行搜尋查詢。

### 建立索引

1. 在快速入門指南中，點擊 **建立索引**。
2. 定義索引結構，指定欄位及其屬性（例如資料類型、是否可搜尋、是否可篩選）。
3. 點擊 **建立** 以建立索引。

### 上傳資料

1. 在快速入門指南中，點擊 **上傳資料**。
2. 選擇資料來源（例如 Azure Blob Storage、Azure SQL Database），並提供必要的連線資訊。
3. 將資料來源欄位對應到索引欄位。
4. 點擊 **提交** 將資料上傳至索引。

### 執行搜尋查詢

1. 在快速入門指南中，點擊 **搜尋瀏覽器**。
2. 在搜尋框中輸入查詢字串，測試搜尋功能。
3. 檢視搜尋結果，並根據需要調整索引結構或資料。

## 步驟 3：使用 Azure AI Search 工具

Azure AI Search 可與多種工具整合，提升搜尋功能。你可以使用 Azure CLI、Python SDK 及其他工具進行進階設定與操作。

### 使用 Azure CLI

1. 按照 [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 的說明安裝 Azure CLI。
2. 使用以下指令登入 Azure CLI：
   ```bash
   az login
   ```
3. 使用 Azure CLI 建立新的搜尋服務：
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. 使用 Azure CLI 建立索引：
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### 使用 Python SDK

1. 安裝 Azure Cognitive Search 的 Python 用戶端函式庫：
   ```bash
   pip install azure-search-documents
   ```
2. 使用以下 Python 程式碼建立索引並上傳文件：
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

更多詳細資訊，請參考以下文件：

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 結論

你已成功透過 Azure 入口網站及整合工具設定 Azure AI Search。現在可以進一步探索 Azure AI Search 的進階功能與能力，提升你的搜尋解決方案。

如需更多協助，請造訪 [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691)。

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。