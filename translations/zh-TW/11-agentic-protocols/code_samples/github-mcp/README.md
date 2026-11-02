# Github MCP Server 範例

## Description

這是一個為 Microsoft Reactor 主辦的 AI Agents Hackathon 所建立的示範。

這些工具用來根據使用者的 Github 倉庫推薦黑客松專案。這是透過以下方式完成的：

1. **Github Agent** - 使用 Github MCP Server 來檢索倉庫及其相關資訊。
2. **Hackathon Agent** - 根據 Github Agent 提供的資料，根據專案、使用語言與 AI Agents 黑客松的賽道提出創意黑客松專案點子。
3. **Events Agent** - 根據 hackathon agent 的建議，events agent 將推薦 AI Agent Hackathon 系列的相關活動。

## Running the code 

### Environment Variables

此示範使用 Microsoft Agent Framework、Azure OpenAI Service、Github MCP Server 與 Azure AI Search。

請確保已設定正確的環境變數以使用這些工具：

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Running the Chainlit Server

要連線到 MCP server，這個示範使用 Chainlit 作為聊天介面。 

要啟動伺服器，請在終端機中使用下列指令：

```bash
chainlit run app.py -w
```

這應該會在 `localhost:8000` 上啟動你的 Chainlit 伺服器，並將 `event-descriptions.md` 的內容填入你的 Azure AI Search Index。 

## Connecting to the MCP Server

要連線到 Github MCP Server，請在 "Type your message here.." 聊天框下方選取 "plug" 圖示：

![MCP 連線](../../../../../translated_images/zh-TW/mcp-chainlit-1.7ed66d648e3cfb28.webp)

接著你可以點擊 "Connect an MCP" 以新增連線到 Github MCP Server 的指令：

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

請將 "[YOUR PERSONAL ACCESS TOKEN]" 替換為你實際的 Personal Access Token。 

連線後，你應該會在插頭圖示旁看到 (1) 以確認已連線。如果沒有，試著以 `chainlit run app.py -w` 重新啟動 chainlit 伺服器。

## Using the Demo 

要啟動推薦黑客松專案的 agent 工作流程，你可以輸入類似的訊息：

"為 Github 使用者 koreyspace 推薦黑客松專案"

Router Agent 會分析你的請求並判斷哪種 agent 組合（GitHub, Hackathon, and Events）最適合處理你的查詢。這些 agents 協同工作，根據 GitHub 倉庫分析、專案構想，以及相關技術活動，提供完整的推薦。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言版本的文件應視為具權威性的依據。對於重要資訊，建議委託專業人工翻譯。我們不對因使用本翻譯而導致的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->