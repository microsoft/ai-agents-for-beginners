# Github MCP 伺服器範例

## 描述

這是一個為 Microsoft Reactor 主辦的 AI Agents 黑客松所製作的示範。

此工具用於根據使用者的 Github 倉庫來推薦黑客松專案。  
實作方式如下：

1. **Github Agent** - 使用 Github MCP 伺服器來檢索倉庫及其相關資訊。
2. **Hackathon Agent** - 從 Github Agent 取得資料，並根據專案、使用者所用語言及 AI Agents 黑客松的專案主題，提出創意的黑客松專案點子。
3. **Events Agent** - 根據 Hackathon Agent 的建議，Events Agent 將推薦 AI Agent 黑客松系列活動的相關活動。

## 執行程式碼

### 環境變數

此示範使用 Microsoft Agent Framework、Azure OpenAI 服務、Github MCP 伺服器及 Azure AI Search。

請確保您已設定適當的環境變數以使用這些工具：

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 
  
## 執行 Chainlit 伺服器

為連接 MCP 伺服器，此示範使用 Chainlit 作為聊天介面。

在終端機輸入下列指令以啟動伺服器：

```bash
chainlit run app.py -w
```
  
這會在 `localhost:8000` 啟動您的 Chainlit 伺服器，並使用 `event-descriptions.md` 內容填充您的 Azure AI Search 索引。

## 連接 MCP 伺服器

要連接 Github MCP 伺服器，請選擇「Type your message here..」聊天框下方的「插頭」圖示：

![MCP Connect](../../../../../translated_images/zh-HK/mcp-chainlit-1.7ed66d648e3cfb28.webp)

接著點擊「Connect an MCP」，新增連接 Github MCP 伺服器的命令：

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```
  
將 "[YOUR PERSONAL ACCESS TOKEN]" 替換成您的個人存取令牌。

連接後，您應該會看到插頭圖示旁出現(1)，表示已連接成功。若未顯示，請嘗試使用 `chainlit run app.py -w` 重新啟動 chainlit 伺服器。

## 使用示範

要啟動推薦黑客松專案的 agent 流程，您可以輸入以下訊息：

"Recommend hackathon projects for the Github user koreyspace"

Router Agent 會分析您的請求並判斷由哪組 agent（GitHub、Hackathon 和 Events）來處理您的查詢最合適。這些 agent 將協同合作，根據 Github 倉庫分析、專案構想及相關技術活動，提供完整的推薦建議。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件透過 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的原文版本應視為權威來源。對於重要資訊，建議採用專業人員進行人工翻譯。本公司對因使用本翻譯而引起的任何誤解或誤釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->