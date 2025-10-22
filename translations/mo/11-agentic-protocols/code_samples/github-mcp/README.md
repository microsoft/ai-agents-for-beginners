<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T13:30:28+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "mo"
}
-->
# Github MCP Server 範例

## 描述

這是一個為 Microsoft Reactor 主辦的 AI Agents Hackathon 所創建的示範。

這個工具用於根據使用者的 Github 儲存庫推薦黑客松專案。其運作方式如下：

1. **Github Agent** - 使用 Github MCP Server 來檢索儲存庫及相關資訊。
2. **Hackathon Agent** - 根據 Github Agent 提供的資料，結合使用者的專案、使用的程式語言以及 AI Agents Hackathon 的專案主題，構思創意黑客松專案。
3. **Events Agent** - 根據 Hackathon Agent 的建議，推薦 AI Agents Hackathon 系列中相關的活動。

## 執行程式碼

### 環境變數

此示範使用 Azure Open AI Service、Semantic Kernel、Github MCP Server 和 Azure AI Search。

請確保已正確設定使用這些工具所需的環境變數：

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## 啟動 Chainlit 伺服器

為了連接 MCP 伺服器，此示範使用 Chainlit 作為聊天介面。

要啟動伺服器，請在終端機中執行以下指令：

```bash
chainlit run app.py -w
```

這將啟動您的 Chainlit 伺服器，位於 `localhost:8000`，並將 `event-descriptions.md` 的內容填入 Azure AI Search Index。

## 連接 MCP 伺服器

要連接到 Github MCP Server，請點擊 "Type your message here.." 聊天框下方的「插頭」圖示：

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.mo.png)

接著，您可以點擊 "Connect an MCP" 來新增連接到 Github MCP Server 的指令：

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

將 "[YOUR PERSONAL ACCESS TOKEN]" 替換為您的實際個人存取權杖。

連接成功後，您應該會看到插頭圖示旁出現一個 (1)，表示已連接。如果未顯示，請嘗試使用 `chainlit run app.py -w` 重新啟動 Chainlit 伺服器。

## 使用示範

要啟動推薦黑客松專案的代理工作流程，您可以輸入類似以下的訊息：

"Recommend hackathon projects for the Github user koreyspace"

Router Agent 會分析您的請求，並決定哪種代理組合（GitHub、Hackathon 和 Events）最適合處理您的查詢。這些代理將協同合作，根據 Github 儲存庫分析、專案構思以及相關技術活動提供全面的建議。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。  