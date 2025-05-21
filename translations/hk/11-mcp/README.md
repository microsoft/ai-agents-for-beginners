<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-05-21T09:30:10+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "hk"
}
-->
# Lesson 11: Model Context Protocol (MCP) Integration

## Introduction to Model Context Protocol (MCP)

Model Context Protocol (MCP) 係一個先進嘅框架，專門用嚟標準化 AI 模型同客戶端應用程式之間嘅互動。MCP 充當 AI 模型同應用程式之間嘅橋樑，無論底層模型點樣實現，都提供一個統一嘅介面。

MCP 嘅重點包括：

- **標準化溝通**：MCP 建立咗一套共通語言，方便應用程式同 AI 模型溝通
- **強化上下文管理**：可以有效地將上下文資訊傳遞畀 AI 模型
- **跨平台兼容**：支援多種編程語言，包括 C#、Java、JavaScript、Python 同 TypeScript
- **無縫整合**：令開發者容易將唔同 AI 模型整合入佢哋嘅應用程式

MCP 喺 AI 代理開發特別有用，因為佢令代理可以透過統一協議同唔同系統同數據源互動，令代理更加靈活同強大。

## Learning Objectives
- 明白 MCP 係乜嘢同佢喺 AI 代理開發中嘅角色
- 設置同配置 MCP 伺服器以作 GitHub 整合
- 用 MCP 工具建立多代理系統
- 實現結合 Azure Cognitive Search 嘅 RAG（Retrieval Augmented Generation）

## Prerequisites
- Python 3.8 或以上
- Node.js 14 或以上
- Azure 訂閱
- GitHub 帳戶
- 基本 Semantic Kernel 知識

## Setup Instructions

1. **環境設置**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **配置 Azure 服務**
   - 建立 Azure Cognitive Search 資源
   - 設置 Azure OpenAI 服務
   - 喺 `.env` 配置環境變量

3. **MCP 伺服器設置**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Project Structure

```
11-mcp/
├── code_samples/
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## Core Components

### 1. 多代理系統
- GitHub 代理：倉庫分析
- Hackathon 代理：項目推薦
- Events 代理：科技活動建議

### 2. Azure 整合
- 用 Cognitive Search 做活動索引
- Azure OpenAI 提供代理智能
- 實現 RAG 模式

### 3. MCP 工具
- GitHub 倉庫分析
- 代碼檢查
- 元數據提取

## Code Walkthrough

示範內容包括：
1. MCP 伺服器整合
2. 多代理協調
3. Azure Cognitive Search 整合
4. RAG 模式實現

主要功能：
- 即時 GitHub 倉庫分析
- 智能項目推薦
- 用 Azure Search 做活動匹配
- Chainlit 流式回應

## Running the Sample

詳細設置指引同更多資料，請參考 [Github MCP Server Example README](./code_samples/github-mcp/README.md)。

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

## Troubleshooting

常見問題同解決方案：
1. MCP 連接問題
   - 確認伺服器有冇運行
   - 檢查端口是否可用
   - 確認 GitHub token 是否正確

2. Azure Search 問題
   - 驗證連接字串
   - 檢查索引是否存在
   - 確認文檔已上傳

## Next Steps
- 探索更多 MCP 工具
- 實現自訂代理
- 強化 RAG 功能
- 加入更多活動來源

## Resources
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋努力追求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原文文件以其母語版本為準，係唯一具權威性嘅版本。對於重要資料，建議採用專業人手翻譯。本公司對因使用此翻譯而引致嘅任何誤解或誤釋概不負責。