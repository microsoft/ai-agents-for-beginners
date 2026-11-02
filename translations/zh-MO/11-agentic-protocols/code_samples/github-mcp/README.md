# Github MCP Server 範例

## 說明

這是為 Microsoft Reactor 主辦的 AI Agents Hackathon 所製作的示範。

此工具用於根據使用者的 Github 倉庫來推薦競賽專案。
這是透過以下方式完成的：

1. **Github Agent** - 使用 Github MCP Server 來擷取倉庫和那些倉庫的相關資訊。
2. **Hackathon Agent** - 使用來自 Github Agent 的資料，根據專案、使用者使用的程式語言以及 AI Agents hackathon 的專案軌道，提出有創意的競賽專案構想。
3. **Events Agent** - 根據 Hackathon Agent 的建議，Events Agent 會推薦 AI Agent Hackathon 系列中相關的活動。
## 執行程式碼 

### 環境變數

此示範使用 Microsoft Agent Framework、Azure OpenAI Service、Github MCP Server 以及 Azure AI Search。

請確保您已設定好使用這些工具所需的環境變數：

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## 執行 Chainlit 伺服器

為了連線至 MCP server，此示範使用 Chainlit 作為聊天介面。 

要啟動伺服器，請在終端機中使用下列指令：

```bash
chainlit run app.py -w
```

這應會在 `localhost:8000` 啟動您的 Chainlit 伺服器，並將 `event-descriptions.md` 的內容填入您的 Azure AI Search Index。 

## 連線至 MCP Server

要連線到 Github MCP Server，請在 "Type your message here.." 聊天框下方選擇 "plug" 圖示：

![MCP 連接](../../../../../translated_images/zh-MO/mcp-chainlit-1.7ed66d648e3cfb28.webp)

從那裡您可以點選 "Connect an MCP" 以加入連線到 Github MCP Server 的指令：

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

連線後，您應該會在 plug 圖示旁看到 (1) 以確認已連線。如果沒有，請嘗試使用 `chainlit run app.py -w` 重新啟動 chainlit 伺服器。

## 使用示範 

要開始推薦競賽專案的 agent 工作流程，您可以輸入類似的訊息： 

"Recommend hackathon projects for the Github user koreyspace"

Router Agent 會分析您的請求，並決定哪一組 agents (GitHub, Hackathon, and Events) 最適合處理您的查詢。這些 agents 會協同合作，根據 GitHub 倉庫分析、專案構思以及相關技術活動，提供完整的推薦。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件係使用 AI 翻譯服務 Co‑op Translator（https://github.com/Azure/co-op-translator）所翻譯。雖然我們致力於維持準確性，但請注意自動翻譯可能含有錯誤或不準確之處。原始文件的母語版本應被視為權威來源。若涉及重要資訊，建議採用專業人工翻譯。我們對因使用此翻譯而引致的任何誤解或錯誤詮釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->