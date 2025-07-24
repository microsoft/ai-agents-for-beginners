<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T07:52:02+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "hk"
}
-->
# 第十一課：模型上下文協議 (MCP) 整合

## 模型上下文協議 (MCP) 簡介

模型上下文協議 (MCP) 是一個先進的框架，旨在標準化 AI 模型與客戶端應用程式之間的互動。MCP 作為 AI 模型與使用這些模型的應用程式之間的橋樑，無論底層模型的實現方式如何，都能提供一致的介面。

MCP 的主要特點包括：

- **標準化的通信**：MCP 建立了一種應用程式與 AI 模型溝通的通用語言  
- **增強的上下文管理**：允許高效地將上下文資訊傳遞給 AI 模型  
- **跨平台兼容性**：支援多種程式語言，包括 C#、Java、JavaScript、Python 和 TypeScript  
- **無縫整合**：讓開發者能輕鬆將不同的 AI 模型整合到應用程式中  

MCP 對於 AI 代理的開發特別有價值，因為它允許代理通過統一的協議與各種系統和數據源互動，使代理更加靈活且功能強大。

## 學習目標
- 理解 MCP 是什麼以及它在 AI 代理開發中的角色  
- 設置並配置 MCP 伺服器以整合 GitHub  
- 使用 MCP 工具構建多代理系統  
- 使用 Azure 認知搜尋實現 RAG（檢索增強生成）  

## 先決條件
- Python 3.8+  
- Node.js 14+  
- Azure 訂閱  
- GitHub 帳戶  
- 基本的 Semantic Kernel 知識  

## 設置說明

1. **環境設置**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **配置 Azure 服務**  
   - 建立 Azure 認知搜尋資源  
   - 設置 Azure OpenAI 服務  
   - 在 `.env` 中配置環境變數  

3. **MCP 伺服器設置**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## 專案結構

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## 核心組件

### 1. 多代理系統
- GitHub 代理：倉庫分析  
- 黑客松代理：專案推薦  
- 活動代理：技術活動建議  

### 2. Azure 整合
- 使用認知搜尋進行活動索引  
- 使用 Azure OpenAI 提供代理智能  
- 實現 RAG 模式  

### 3. MCP 工具
- GitHub 倉庫分析  
- 代碼檢查  
- 元數據提取  

## 代碼講解

範例展示了以下內容：  
1. MCP 伺服器整合  
2. 多代理協調  
3. Azure 認知搜尋整合  
4. RAG 模式實現  

主要功能：  
- 即時 GitHub 倉庫分析  
- 智能專案推薦  
- 使用 Azure 搜尋進行活動匹配  
- 使用 Chainlit 實現流式響應  

## 運行範例

有關詳細的設置說明和更多資訊，請參閱 [Github MCP Server Example README](./code_samples/github-mcp/README.md)。

1. 啟動 MCP 伺服器：  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. 啟動應用程式：  
   ```bash
   chainlit run app.py -w
   ```

3. 測試整合：  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## 疑難排解

常見問題及解決方案：  
1. MCP 連接問題  
   - 確認伺服器正在運行  
   - 檢查埠是否可用  
   - 確認 GitHub 權杖  

2. Azure 搜尋問題  
   - 驗證連接字串  
   - 檢查索引是否存在  
   - 確認文檔是否已上傳  

## 下一步
- 探索更多 MCP 工具  
- 實現自定義代理  
- 增強 RAG 功能  
- 添加更多活動來源  
- **進階**：查看 [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) 以了解代理與代理之間的通信範例  

## 資源
- [MCP 初學者指南](https://aka.ms/mcp-for-beginners)  
- [MCP 文件](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure 認知搜尋文檔](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel 指南](https://learn.microsoft.com/semantic-kernel/)  

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。