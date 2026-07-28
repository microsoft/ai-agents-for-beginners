# AGENTS.md

## 專案概述

本存儲庫包含「AI 初學者代理人」——一個全面的教育課程，教授建立 AI 代理人所需的一切。課程包含 18 課題（編號 00-18），涵蓋基礎知識、設計模式、框架、生產部署、本地/裝置代理人，以及 AI 代理人的安全性。

**關鍵技術：**
- Python 3.12+
- 使用 Jupyter 筆記本進行互動學習
- AI 框架：Microsoft Agent Framework (MAF)
- Azure AI 服務：Microsoft Foundry、Microsoft Foundry Agent Service V2

**架構：**
- 基於課程的結構（00-15+ 目錄）
- 每課包含：README 文件、代碼範例（Jupyter 筆記本）和圖片
- 通過自動翻譯系統支持多語言
- 每課有一個使用 Microsoft Agent Framework 的 Python 筆記本

## 設定命令

### 前置條件
- Python 3.12 或更高版本
- Azure 訂閱（用於 Microsoft Foundry）
- 安裝並已認證 Azure CLI（`az login`）

### 初始設定

1. **克隆或分支存儲庫：**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # 或者
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **建立並啟用 Python 虛擬環境：**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # 在 Windows 上：venv\Scripts\activate
   ```

3. **安裝依賴項：**
   ```bash
   pip install -r requirements.txt
   ```

4. **設定環境變數：**
   ```bash
   cp .env.example .env
   # 使用你的 API 密鑰和端點編輯 .env
   ```

### 必填環境變數

用於 **Microsoft Foundry**（必填）：
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry 專案端點
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - 模型部署名稱（如 gpt-5-mini）

用於 **Azure AI Search**（第 05 課 - RAG）：
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search 端點
- `AZURE_SEARCH_API_KEY` - Azure AI Search API 金鑰

認證：在執行筆記本之前執行 `az login`（使用 `AzureCliCredential`）。

## 開發工作流程

### 運行 Jupyter 筆記本

每課包含多個針對不同框架的 Jupyter 筆記本：

1. **啟動 Jupyter：**
   ```bash
   jupyter notebook
   ```

2. <strong>導航到課程目錄</strong>（例如 `01-intro-to-ai-agents/code_samples/`）

3. **打開並運行筆記本：**
   - `*-python-agent-framework.ipynb` - 使用 Microsoft Agent Framework（Python）
   - `*-dotnet-agent-framework.ipynb` - 使用 Microsoft Agent Framework（.NET）

### Microsoft Agent Framework 操作

**Microsoft Agent Framework + Microsoft Foundry：**
- 需要 Azure 訂閱
- 使用 `FoundryChatClient` 連接 Agent Service V2（代理人可見於 Foundry 入口網站）
- 生產環境就緒，內建可觀察性功能
- 檔案模式：`*-python-agent-framework.ipynb`

## 測試指引

這是一個教育存儲庫，用於示範代碼，而非具備自動化測試的生產代碼。驗證設定及修改方法：

### 手動測試

1. **測試 Python 環境：**
   ```bash
   python --version  # 應該係3.12或以上
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **測試筆記本執行：**
   ```bash
   # 將筆記本轉換為腳本並運行（測試導入）
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **核對環境變數：**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### 單獨執行筆記本

在 Jupyter 中打開筆記本並順序執行儲存格。每個筆記本都是自包含，並包括：
- 匯入語句
- 載入設定
- 範例代理人實作
- 預期輸出在 markdown 儲存格中

### 部署代理人的冒煙測試

對於作為 Microsoft Foundry 主機代理人部署的課程（01、04、05、16）中，存儲庫提供在 `tests/` 下的冒煙測試目錄，該目錄由 `.github/workflows/smoke-test.yml` 工作流程通過 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) 操作運行。這是輕量級的部署後檢查（代理人是否可連接且符合基本提示預期？），輔助第 10 與第 16 課的評估流程。請參閱 [tests/README.md](./tests/README.md) 了解目錄到課程到代理人的對應。第 17 課使用 Foundry Local 本地運行，無託管端點，因此透過直接執行其筆記本進行驗證。

## 代碼風格

### Python 慣例

- **Python 版本**：3.12+
- <strong>代碼風格</strong>：遵循標準 Python PEP 8 規範
- <strong>筆記本</strong>：使用清晰的 markdown 儲存格解釋概念
- <strong>匯入</strong>：按標準庫、第三方、本地匯入分組

### Jupyter 筆記本慣例

- 在程式碼儲存格前包含描述性 markdown 儲存格
- 筆記本中加入輸出範例作參考
- 使用符合課程概念的清晰變數名稱
- 保持筆記本執行順序線性（儲存格 1 → 2 → 3...）

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

### 建置文件

本存儲庫使用 Markdown 作文件：
- 每課文件夾下的 README.md 檔案
- 儲存庫根目錄下的主 README.md
- 透過 GitHub Actions 自動翻譯系統

### CI/CD 流程

位於 `.github/workflows/`：

1. **co-op-translator.yml** - 自動翻譯成 50+ 種語言
2. **welcome-issue.yml** - 歡迎新議題建立者
3. **welcome-pr.yml** - 歡迎新拉取請求貢獻者

### 部署

這是一個教育存儲庫，沒有部署流程。使用者可：
1. 分支或克隆存儲庫
2. 在本地或 GitHub Codespaces 運行筆記本
3. 透過修改和試驗範例來學習

## 拉取請求指引

### 提交前

1. **測試修改：**
   - 完整運行影響的筆記本
   - 確認所有儲存格均無錯誤執行
   - 檢查輸出是否合適

2. **文件更新：**
   - 若新增概念，更新 README.md
   - 在筆記本中為複雜代碼加入註釋
   - 確保 markdown 儲存格說明目的

3. **檔案修改：**
   - 避免提交 `.env` 檔（使用 `.env.example`）
   - 不提交 `venv/` 或 `__pycache__/` 目錄
   - 展示概念時保留筆記本輸出
   - 移除臨時檔及備份筆記本（`*-backup.ipynb`）

### 拉取請求標題格式

使用描述性標題：
- `[Lesson-XX] 新增 <概念> 範例`
- `[Fix] 修正 lesson-XX README 的錯字`
- `[Update] 改善 lesson-XX 中的程式碼範例`
- `[Docs] 更新設定指引`

### 必要檢查

- 筆記本應無錯誤執行
- README 文件應清晰且準確
- 遵循存儲庫內現有代碼模式
- 與其他課程保持一致性

## 附加說明

### 常見陷阱

1. **Python 版本不匹配：**
   - 確保使用 Python 3.12+ 版本
   - 某些套件不支援較舊版本
   - 使用 `python3 -m venv` 明確指定 Python 版本

2. **環境變數：**
   - 始終從 `.env.example` 創建 `.env`
   - 不提交 `.env` 檔（已加入 `.gitignore`）
   - 使用 `az login` 登入以取得無鑰匙 Entra ID 認證

3. **套件衝突：**
   - 使用新的虛擬環境
   - 從 `requirements.txt` 安裝，而非單獨安裝套件
   - 某些筆記本可能需要其 markdown 格中提及的額外套件

4. **Azure 服務：**
   - Azure AI 服務需有效訂閱
   - 某些功能區域專用
   - 確認您的 Azure OpenAI 模型部署支持 Responses API

### 學習路徑

建議依序進行課程：
1. **00-course-setup** - 從這裡開始環境設定
2. **01-intro-to-ai-agents** - 了解 AI 代理人基礎
3. **02-explore-agentic-frameworks** - 認識不同框架
4. **03-agentic-design-patterns** - 核心設計模式
5. 按順序繼續完成編號課程

### 框架選擇

根據您的目標選擇框架：
- <strong>所有課程</strong>：使用帶有 `FoundryChatClient` 的 Microsoft Agent Framework (MAF)
- <strong>代理人註冊於伺服器端</strong>，位於 Microsoft Foundry Agent Service V2，並可於 Foundry 入口網站查看

### 獲得幫助

- 加入 [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- 查閱課程 README 文件得到具體指引
- 檢視主 README.md 了解課程概述
- 參考 [Course Setup](./00-course-setup/README.md) 以獲詳細設定說明

### 貢獻

這是一個開放教育專案，歡迎貢獻：
- 改進程式碼範例
- 修正錯字或錯誤
- 添加說明性註釋
- 建議新增課程主題
- 翻譯成更多語言

請參閱 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) 了解目前需求。

## 專案特定背景

### 多語言支持

本存儲庫使用自動翻譯系統：
- 支援 50 多種語言
- 翻譯檔位於 `/translations/<lang-code>/` 目錄
- 由 GitHub Actions 工作流程管理翻譯更新
- 原始檔為英文，位於存儲庫根目錄

### 課程結構

每課遵循一致模式：
1. 含連結的影片縮圖
2. 書面課程內容（README.md）
3. 多框架的代碼範例
4. 學習目標與先修條件
5. 連結額外學習資源

### 代碼範例命名

格式：`<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 第 1 課，MAF Python
- `14-sequential.ipynb` - 第 14 課，MAF 進階模式
- `16-python-agent-framework.ipynb` - 第 16 課，生產環境客戶支援代理人
- `17-local-agent-foundry-local.ipynb` - 第 17 課，本地代理人使用 Foundry Local + Qwen

### 特殊目錄

- `translated_images/` - 本地化圖片，用於翻譯
- `images/` - 英文內容的原始圖片
- `.devcontainer/` - VS Code 開發容器設定
- `.github/` - GitHub Actions 工作流程及範本

### 依賴項

來自 `requirements.txt` 的主要套件：
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent 協定支持
- `azure-ai-inference`、`azure-ai-projects` - Azure AI 服務
- `azure-identity` - Azure 認證（AzureCliCredential）
- `azure-search-documents` - Azure AI Search 整合
- `mcp[cli]` - 模型上下文協定支持

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->