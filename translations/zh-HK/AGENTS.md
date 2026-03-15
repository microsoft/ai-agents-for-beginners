# AGENTS.md

## 專案概覽

此儲存庫包含「AI Agents for Beginners」— 一個完整的教學課程，教導建立 AI Agents 所需的一切。課程由 15+ 節組成，涵蓋基礎、設計模式、框架以及 AI agent 的生產部署。

**主要技術：**
- Python 3.12+
- Jupyter Notebooks 用於互動式學習
- AI 框架：Microsoft Agent Framework (MAF)
- Azure AI 服務：Microsoft Foundry、Azure AI Foundry Agent Service V2

**架構：**
- 以課程為基礎的結構（00-15+ 目錄）
- 每個課程包含：README 文件、程式範例（Jupyter notebooks）與圖片
- 透過自動翻譯系統提供多語言支援
- 每課一個使用 Microsoft Agent Framework 的 Python notebook

## 設定指令

### 先決條件
- Python 3.12 或更新版本
- Azure 訂閱（用於 Azure AI Foundry）
- 已安裝並已驗證的 Azure CLI（`az login`）

### 初始設定

1. **Clone or fork the repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # 或
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Create and activate Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # 在 Windows 上：venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # 使用你嘅 API 金鑰同端點編輯 .env
   ```

### 所需環境變數

對於 **Azure AI Foundry**（必需）：
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry 專案端點
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - 模型部署名稱（例如：gpt-4o）

對於 **Azure AI Search**（Lesson 05 - RAG）：
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search 端點
- `AZURE_SEARCH_API_KEY` - Azure AI Search API 金鑰

認證：在執行 notebooks 之前請執行 `az login`（使用 `AzureCliCredential`）。

## 開發工作流程

### 執行 Jupyter Notebooks

每個課程包含多個針對不同框架的 Jupyter notebooks：

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigate to a lesson directory** (e.g., `01-intro-to-ai-agents/code_samples/`)

3. **Open and run notebooks:**
   - `*-python-agent-framework.ipynb` - 使用 Microsoft Agent Framework（Python）
   - `*-dotnet-agent-framework.ipynb` - 使用 Microsoft Agent Framework（.NET）

### 使用 Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry：**
- 需要 Azure 訂閱
- 使用 `AzureAIProjectAgentProvider` 來連接 Agent Service V2（agents 可在 Foundry 入口網站查看）
- 具備內建可觀察性的生產就緒方案
- 檔案模式：`*-python-agent-framework.ipynb`

## 測試說明

這是一個教學儲存庫，包含範例程式碼，而非具有自動化測試的生產程式碼。要驗證你的環境及變更：

### 手動測試

1. **Test Python environment:**
   ```bash
   python --version  # 應該為 3.12 或以上
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook execution:**
   ```bash
   # 將 notebook 轉換為腳本並執行（測試匯入）
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verify environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### 執行單一 Notebook

在 Jupyter 中打開 notebooks 並依序執行儲存格。每個 notebook 都是自包含的並包含：
- 匯入敘述
- 設定載入
- 範例 agent 實作
- 預期輸出於 markdown 儲存格中

## 程式碼風格

### Python 規範

- **Python 版本**：3.12+
- **程式碼風格**：遵循標準 Python PEP 8 規範
- **Notebooks**：使用清楚的 markdown 儲存格來解釋概念
- **匯入**：按標準函式庫、第三方、本地匯入分組

### Jupyter Notebook 慣例

- 在程式碼儲存格前加入描述性的 markdown 儲存格
- 在 notebooks 中加入輸出範例供參考
- 使用與課程概念相符的清晰變數名稱
- 保持 notebook 執行順序線性（儲存格 1 → 2 → 3...）

### 檔案組織

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## 建置與部署

### 文件建置

此儲存庫使用 Markdown 作為文件：
- 每個課程資料夾中的 README.md 檔案
- 儲存庫根目錄的主要 README.md
- 透過 GitHub Actions 的自動翻譯系統

### CI/CD 管線

位於 `.github/workflows/`：

1. **co-op-translator.yml** - 自動翻譯到 50+ 種語言
2. **welcome-issue.yml** - 歡迎新的議題建立者
3. **welcome-pr.yml** - 歡迎新的 pull request 貢獻者

### 部署

這是一個教學儲存庫 - 無部署流程。使用者可：
1. Fork 或 clone 此儲存庫
2. 在本地或 GitHub Codespaces 中執行 notebooks
3. 透過修改與實驗範例來學習

## 拉取請求 (Pull Request) 指南

### 提交之前

1. **Test your changes:**
   - 完整執行受影響的 notebooks
   - 驗證所有儲存格皆可執行且無錯誤
   - 檢查輸出是否合理

2. **Documentation updates:**
   - 若加入新概念請更新 README.md
   - 在 notebooks 中為複雜程式碼加入註解
   - 確保 markdown 儲存格解釋其用途

3. **File changes:**
   - 避免提交 `.env` 檔案（請使用 `.env.example`）
   - 不要提交 `venv/` 或 `__pycache__/` 目錄
   - 當 notebook 輸出用於示範概念時，可保留輸出
   - 移除臨時檔案與備份 notebook（`*-backup.ipynb`）

### PR 標題格式

使用描述性標題：
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### 必要檢查

- Notebooks 應能無錯誤執行
- README 檔案應清晰且正確
- 遵循儲存庫中既有的程式碼模式
- 與其他課程保持一致性

## 附加注意事項

### 常見問題

1. **Python 版本不符：**
   - 確保使用 Python 3.12+
   - 有些套件可能不支援較舊版本
   - 使用 `python3 -m venv` 明確指定 Python 版本

2. **環境變數：**
   - 始終從 `.env.example` 建立 `.env`
   - 不要提交 `.env` 檔案（已加入 `.gitignore`）
   - GitHub token 需具備適當權限

3. **套件衝突：**
   - 使用全新虛擬環境
   - 從 `requirements.txt` 安裝，而非單獨套件
   - 有些 notebooks 可能需要其 markdown 儲存格中提到的額外套件

4. **Azure 服務：**
   - Azure AI 服務需要有效訂閱
   - 部分功能為區域性
   - 免費方案對 GitHub Models 有使用限制

### 學習路徑

建議按順序學習課程：
1. **00-course-setup** - 從此開始進行環境設定
2. **01-intro-to-ai-agents** - 了解 AI agent 基礎
3. **02-explore-agentic-frameworks** - 認識不同框架
4. **03-agentic-design-patterns** - 核心設計模式
5. 依序繼續學習編號課程

### 框架選擇

根據目標選擇合適的框架：
- **所有課程**：使用 Microsoft Agent Framework (MAF) 與 `AzureAIProjectAgentProvider`
- **Agents 在伺服器端註冊** 至 Azure AI Foundry Agent Service V2，並可在 Foundry 入口網站檢視

### 取得協助

- 加入 [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- 檢閱各課程的 README 檔案以獲得具體指引
- 查看主要的 [README.md](./README.md) 以獲取課程概覽
- 參考 [Course Setup](./00-course-setup/README.md) 以獲得詳細設定指示

### 貢獻

這是一個開放的教育專案，歡迎貢獻：
- 改善程式範例
- 修正錯字或錯誤
- 新增說明註解
- 建議新的課程主題
- 翻譯成更多語言

請參閱 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) 了解目前需求。

## 專案相關內容

### 多語言支援

此儲存庫使用自動翻譯系統：
- 支援 50+ 種語言
- 翻譯存放於 `/translations/<lang-code>/` 目錄
- GitHub Actions workflow 處理翻譯更新
- 原始檔案以英文存放於儲存庫根目錄

### 課程結構

每課遵循一致格式：
1. 含有連結的影片縮圖
2. 書面課程內容（README.md）
3. 多框架的程式範例
4. 學習目標與先決需求
5. 連結的額外學習資源

### 程式範例命名

格式：`<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 第 1 課，MAF Python
- `14-sequential.ipynb` - 第 14 課，MAF 進階模式

### 特殊目錄

- `translated_images/` - 本地化的翻譯圖片
- `images/` - 英文原始圖片
- `.devcontainer/` - VS Code 開發容器設定
- `.github/` - GitHub Actions workflows 與範本

### 相依套件

`requirements.txt` 中的關鍵套件：
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protocol 支援
- `azure-ai-inference`, `azure-ai-projects` - Azure AI 服務
- `azure-identity` - Azure 驗證（AzureCliCredential）
- `azure-search-documents` - Azure AI Search 整合
- `mcp[cli]` - Model Context Protocol 支援

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件由 AI 翻譯服務 Co‑op Translator（https://github.com/Azure/co-op-translator）所翻譯。雖然我們力求準確，但自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要或關鍵資訊，建議採用專業人工翻譯。我們不會就因使用此翻譯而導致的任何誤解或錯誤詮釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->