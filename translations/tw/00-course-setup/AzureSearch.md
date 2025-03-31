<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "932a1f463f0fcf97090b93b5d0255dff",
  "translation_date": "2025-03-28T14:06:13+00:00",
  "source_file": "00-course-setup\\AzureSearch.md",
  "language_code": "tw"
}
-->
# Azure AI 搜尋設定指南

本指南將協助您透過 Azure 入口網站設定 Azure AI 搜尋服務。請按照以下步驟來建立並配置您的 Azure AI 搜尋服務。

## 先決條件

開始之前，請確保您已具備以下條件：

- 一個 Azure 訂閱。如果您尚未擁有 Azure 訂閱，可以在 [Azure 免費帳戶](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 建立一個免費帳戶。

## 第一步：建立 Azure AI 搜尋服務

1. 登入 [Azure 入口網站](https://portal.azure.com/?wt.mc_id=studentamb_258691)。
2. 在左側導覽窗格中，點擊 **建立資源**。
3. 在搜尋框中輸入 "Azure Cognitive Search"，並從結果列表中選擇 **Azure Cognitive Search**。
4. 點擊 **建立** 按鈕。
5. 在 **基本資訊** 標籤中，提供以下資訊：
   - **訂閱**：選擇您的 Azure 訂閱。
   - **資源群組**：建立新的資源群組或選擇現有的資源群組。
   - **資源名稱**：輸入您的搜尋服務的唯一名稱。
   - **地區**：選擇最接近使用者的地區。
   - **定價層級**：選擇符合您需求的定價層級。您可以從免費層級開始測試。
6. 點擊 **檢閱 + 建立**。
7. 檢查設定後，點擊 **建立** 以建立搜尋服務。

## 第二步：開始使用 Azure AI 搜尋

1. 部署完成後，前往 Azure 入口網站中的搜尋服務。
2. 在搜尋服務概覽頁面，點擊 **快速入門** 按鈕。
3. 按照快速入門指南中的步驟建立索引、上傳資料並執行搜尋查詢。

### 建立索引

1. 在快速入門指南中，點擊 **建立索引**。
2. 定義索引結構，指定欄位及其屬性（例如：資料類型、可搜尋、可篩選）。
3. 點擊 **建立** 以建立索引。

### 上傳資料

1. 在快速入門指南中，點擊 **上傳資料**。
2. 選擇資料來源（例如：Azure Blob Storage、Azure SQL Database），並提供必要的連接詳細資訊。
3. 將資料來源欄位映射到索引欄位。
4. 點擊 **提交** 將資料上傳至索引。

### 執行搜尋查詢

1. 在快速入門指南中，點擊 **搜尋探索**。
2. 在搜尋框中輸入搜尋查詢以測試搜尋功能。
3. 檢視搜尋結果，並根據需要調整索引結構或資料。

## 第三步：使用 Azure AI 搜尋工具

Azure AI 搜尋整合了多種工具，能提升您的搜尋功能。您可以使用 Azure CLI、Python SDK 等工具進行進階配置和操作。

### 使用 Azure CLI

1. 按照 [安裝 Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 的指示安裝 Azure CLI。
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

1. 安裝 Azure Cognitive Search 的 Python 客戶端程式庫：
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

如需更詳細的資訊，請參考以下文件：

- [建立 Azure Cognitive Search 服務](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [開始使用 Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI 搜尋工具](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## 結論

您已成功使用 Azure 入口網站設定 Azure AI 搜尋並整合相關工具。現在，您可以探索 Azure AI 搜尋的更多進階功能和能力，來提升您的搜尋解決方案。

如需更多協助，請造訪 [Azure Cognitive Search 文件](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691)。

**免責聲明**:  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤概不負責。