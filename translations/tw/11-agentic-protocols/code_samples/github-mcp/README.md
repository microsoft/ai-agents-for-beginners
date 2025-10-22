<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-28T09:55:51+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "tw"
}
-->
# Github MCP Server 範例

## 描述

這是一個為 AI Agents Hackathon 所創建的示範，活動由 Microsoft Reactor 主辦。

此工具用於根據使用者的 Github 儲存庫推薦黑客松項目。其運作方式如下：

1. **Github Agent** - 使用 Github MCP Server 來檢索儲存庫及其相關資訊。
2. **Hackathon Agent** - 根據 Github Agent 提供的資料，結合使用者的項目、使用的程式語言以及 AI Agents Hackathon 的項目主題，提出創意的黑客松項目建議。
3. **Events Agent** - 根據 Hackathon Agent 的建議，Events Agent 會推薦 AI Agents Hackathon 系列中相關的活動。

## 執行程式碼

### 環境變數

此示範使用 Azure Open AI Service、Semantic Kernel、Github MCP Server 和 Azure AI Search。

請確保已正確設置環境變數以使用這些工具：

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## 執行 Chainlit Server

為了連接 MCP Server，此示範使用 Chainlit 作為聊天介面。

要啟動伺服器，請在終端機中使用以下指令：

```bash
chainlit run app.py -w
```

此指令將啟動您的 Chainlit 伺服器，位於 `localhost:8000`，並將 `event-descriptions.md` 的內容填入 Azure AI Search Index。

## 連接 MCP Server

要連接 Github MCP Server，請點選 "Type your message here.." 聊天框下方的 "plug" 圖示：

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.tw.png)

接著，您可以點選 "Connect an MCP" 來新增指令以連接 Github MCP Server：

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

將 "[YOUR PERSONAL ACCESS TOKEN]" 替換為您的實際個人存取權杖。

連接成功後，您應該會看到 plug 圖示旁出現 (1)，表示已連接。如果未顯示，請嘗試使用 `chainlit run app.py -w` 重新啟動 Chainlit 伺服器。

## 使用示範

要啟動推薦黑客松項目的代理工作流程，您可以輸入類似以下的訊息：

"Recommend hackathon projects for the Github user koreyspace"

Router Agent 會分析您的請求，並決定哪種代理組合（GitHub、Hackathon 和 Events）最適合處理您的查詢。這些代理會協同合作，根據 Github 儲存庫分析、項目創意以及相關技術活動提供全面的建議。

---

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不精確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。