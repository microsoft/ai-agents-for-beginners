<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5f54aa3f419865e5d58bcfddb1d3198",
  "translation_date": "2025-10-03T15:27:16+00:00",
  "source_file": "AGENTS.md",
  "language_code": "tw"
}
-->
# AGENTS.md

## 專案概述

此存儲庫包含「AI代理入門」課程——一個全面的教育課程，教授建立AI代理所需的一切知識。課程由超過15個課程組成，涵蓋基礎知識、設計模式、框架以及AI代理的生產部署。

**主要技術：**
- Python 3.12+
- 使用Jupyter Notebook進行互動式學習
- AI框架：Semantic Kernel、AutoGen、Microsoft Agent Framework (MAF)
- Azure AI服務：Azure AI Foundry、Azure AI Agent Service
- GitHub模型市場（提供免費層）

**架構：**
- 基於課程的結構（00-15+目錄）
- 每個課程包含：README文檔、代碼示例（Jupyter Notebook）和圖片
- 通過自動翻譯系統支持多語言
- 每課程提供多種框架選項（Semantic Kernel、AutoGen、Azure AI Agent Service）

## 設置指令

### 先決條件
- Python 3.12或更高版本
- GitHub帳戶（用於GitHub模型——免費層）
- Azure訂閱（可選，用於Azure AI服務）

### 初始設置

1. **克隆或分叉存儲庫：**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **創建並激活Python虛擬環境：**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **安裝依賴項：**
   ```bash
   pip install -r requirements.txt
   ```

4. **設置環境變量：**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### 必需的環境變量

對於 **GitHub模型（免費）**：
- `GITHUB_TOKEN` - 從GitHub獲取的個人訪問令牌

對於 **Azure AI服務**（可選）：
- `PROJECT_ENDPOINT` - Azure AI Foundry項目端點
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API密鑰
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI端點URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - 聊天模型的部署名稱
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - 嵌入模型的部署名稱
- 其他Azure配置詳見 `.env.example`

## 開發工作流程

### 運行Jupyter Notebook

每個課程包含多個針對不同框架的Jupyter Notebook：

1. **啟動Jupyter：**
   ```bash
   jupyter notebook
   ```

2. **導航到課程目錄**（例如，`01-intro-to-ai-agents/code_samples/`）

3. **打開並運行Notebook：**
   - `*-semantic-kernel.ipynb` - 使用Semantic Kernel框架
   - `*-autogen.ipynb` - 使用AutoGen框架
   - `*-python-agent-framework.ipynb` - 使用Microsoft Agent Framework（Python）
   - `*-dotnet-agent-framework.ipynb` - 使用Microsoft Agent Framework（.NET）
   - `*-azureaiagent.ipynb` - 使用Azure AI Agent Service

### 使用不同框架

**Semantic Kernel + GitHub模型：**
- 使用GitHub帳戶可享免費層
- 適合學習和實驗
- 文件模式：`*-semantic-kernel*.ipynb`

**AutoGen + GitHub模型：**
- 使用GitHub帳戶可享免費層
- 支持多代理協作功能
- 文件模式：`*-autogen.ipynb`

**Microsoft Agent Framework (MAF)：**
- 微軟最新框架
- 提供Python和.NET版本
- 文件模式：`*-agent-framework.ipynb`

**Azure AI Agent Service：**
- 需要Azure訂閱
- 生產級功能
- 文件模式：`*-azureaiagent.ipynb`

## 測試說明

此存儲庫是教育性質的，包含示例代碼，而非帶有自動化測試的生產代碼。要驗證您的設置和更改：

### 手動測試

1. **測試Python環境：**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **測試Notebook執行：**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **驗證環境變量：**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### 運行單個Notebook

在Jupyter中打開Notebook並按順序執行每個單元格。每個Notebook都是自包含的，包含：
- 導入語句
- 配置加載
- 示例代理實現
- Markdown單元格中的預期輸出

## 代碼風格

### Python約定

- **Python版本**：3.12+
- **代碼風格**：遵循標準Python PEP 8約定
- **Notebook**：使用清晰的Markdown單元格解釋概念
- **導入**：按標準庫、第三方庫、本地導入分組

### Jupyter Notebook約定

- 在代碼單元格之前包含描述性Markdown單元格
- 在Notebook中添加輸出示例作為參考
- 使用清晰的變量名稱以匹配課程概念
- 保持Notebook執行順序線性（單元格1 → 2 → 3...）

### 文件組織

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## 構建與部署

### 構建文檔

此存儲庫使用Markdown進行文檔編寫：
- 每個課程文件夾中的README.md文件
- 存儲庫根目錄的主README.md
- 通過GitHub Actions進行自動翻譯

### CI/CD管道

位於 `.github/workflows/`：

1. **co-op-translator.yml** - 自動翻譯至50多種語言
2. **welcome-issue.yml** - 歡迎新問題創建者
3. **welcome-pr.yml** - 歡迎新拉取請求貢獻者

### 部署

此存儲庫為教育性質——無部署流程。用戶：
1. 分叉或克隆存儲庫
2. 在本地或GitHub Codespaces中運行Notebook
3. 通過修改和實驗示例進行學習

## 拉取請求指南

### 提交前

1. **測試您的更改：**
   - 完整運行受影響的Notebook
   - 確保所有單元格執行無錯誤
   - 檢查輸出是否合適

2. **文檔更新：**
   - 如果添加新概念，更新README.md
   - 在Notebook中為複雜代碼添加註釋
   - 確保Markdown單元格解釋目的

3. **文件更改：**
   - 避免提交 `.env` 文件（使用 `.env.example`）
   - 不提交 `venv/` 或 `__pycache__/` 目錄
   - 保留Notebook輸出以展示概念
   - 刪除臨時文件和備份Notebook（`*-backup.ipynb`）

### PR標題格式

使用描述性標題：
- `[Lesson-XX] 添加新示例以展示<概念>`
- `[Fix] 修正Lesson-XX README中的拼寫錯誤`
- `[Update] 改進Lesson-XX中的代碼示例`
- `[Docs] 更新設置說明`

### 必需檢查

- Notebook應無錯誤執行
- README文件應清晰準確
- 遵循存儲庫中的現有代碼模式
- 與其他課程保持一致性

## 附加說明

### 常見問題

1. **Python版本不匹配：**
   - 確保使用Python 3.12+
   - 某些包可能不支持舊版本
   - 使用 `python3 -m venv` 明確指定Python版本

2. **環境變量：**
   - 始終從 `.env.example` 創建 `.env`
   - 不提交 `.env` 文件（已在 `.gitignore` 中）
   - GitHub令牌需要適當的權限

3. **包衝突：**
   - 使用全新的虛擬環境
   - 從 `requirements.txt` 安裝，而非單獨安裝包
   - 某些Notebook可能需要Markdown單元格中提到的額外包

4. **Azure服務：**
   - Azure AI服務需要有效訂閱
   - 某些功能僅限特定地區
   - GitHub模型的免費層有使用限制

### 學習路徑

推薦的課程進度：
1. **00-course-setup** - 從此處開始設置環境
2. **01-intro-to-ai-agents** - 理解AI代理基礎知識
3. **02-explore-agentic-frameworks** - 學習不同框架
4. **03-agentic-design-patterns** - 核心設計模式
5. 按課程編號順序繼續學習

### 框架選擇

根據您的目標選擇框架：
- **學習/原型設計**：Semantic Kernel + GitHub模型（免費）
- **多代理系統**：AutoGen
- **最新功能**：Microsoft Agent Framework (MAF)
- **生產部署**：Azure AI Agent Service

### 獲取幫助

- 加入 [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- 查看課程README文件以獲取具體指導
- 查看主 [README.md](./README.md) 了解課程概述
- 參考 [Course Setup](./00-course-setup/README.md) 獲取詳細設置說明

### 貢獻

這是一個開放的教育項目，歡迎貢獻：
- 改進代碼示例
- 修正拼寫或錯誤
- 添加澄清性註釋
- 建議新課程主題
- 翻譯至其他語言

請參閱 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) 了解當前需求。

## 項目特定上下文

### 多語言支持

此存儲庫使用自動翻譯系統：
- 支持50多種語言
- 翻譯存儲於 `/translations/<lang-code>/` 目錄
- GitHub Actions工作流處理翻譯更新
- 源文件位於存儲庫根目錄，使用英文

### 課程結構

每個課程遵循一致的模式：
1. 帶鏈接的視頻縮略圖
2. 書面課程內容（README.md）
3. 多框架代碼示例
4. 學習目標和先決條件
5. 附加學習資源鏈接

### 代碼示例命名

格式：`<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - 第4課，Semantic Kernel
- `07-autogen.ipynb` - 第7課，AutoGen
- `14-python-agent-framework.ipynb` - 第14課，MAF Python
- `14-dotnet-agent-framework.ipynb` - 第14課，MAF .NET

### 特殊目錄

- `translated_images/` - 翻譯圖片的本地化版本
- `images/` - 英文內容的原始圖片
- `.devcontainer/` - VS Code開發容器配置
- `.github/` - GitHub Actions工作流和模板

### 依賴項

`requirements.txt` 中的主要包：
- `autogen-agentchat`、`autogen-core`、`autogen-ext` - AutoGen框架
- `semantic-kernel` - Semantic Kernel框架
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`、`azure-ai-projects` - Azure AI服務
- `azure-search-documents` - Azure AI搜索集成
- `chromadb` - 用於RAG示例的向量數據庫
- `chainlit` - 聊天UI框架
- `browser_use` - 用於代理的瀏覽器自動化
- `mcp[cli]` - 模型上下文協議支持
- `mem0ai` - 用於代理的內存管理

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。