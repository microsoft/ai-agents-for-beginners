# AGENTS.md

## 專案概覽

此儲存庫包含「初學者的 AI 代理人」— 一門全面的教育課程，教授構建 AI 代理人所需的一切。該課程包含18個課程（編號00-18），涵蓋基礎知識、設計模式、框架、正式部署、本地/裝置代理人以及 AI 代理人的安全性。

**主要技術：**
- Python 3.12+
- 用於互動學習的 Jupyter 筆記本
- AI 框架：Microsoft Agent Framework (MAF)
- Azure AI 服務：Microsoft Foundry、Microsoft Foundry Agent Service V2

**架構：**
- 以課程為基礎的結構（00-15+ 資料夾）
- 每個課程包含：README 文件、程式碼範例（Jupyter 筆記本）和圖片
- 透過自動翻譯系統支援多語言
- 每課一個使用 Microsoft Agent Framework 的 Python 筆記本

## 設置指令

### 前置條件
- Python 3.12 或更高版本
- Azure 訂閱（用於 Microsoft Foundry）
- 安裝且已登入 Azure CLI (`az login`)

### 初始設定

1. **複製或分叉此儲存庫：**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # 或者
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **建立並啟動 Python 虛擬環境：**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # 在 Windows 上：venv\Scripts\activate
   ```

3. **安裝相依套件：**
   ```bash
   pip install -r requirements.txt
   ```

4. **設定環境變數：**
   ```bash
   cp .env.example .env
   # 編輯 .env 並加入你的 API 金鑰和端點
   ```

### 必要環境變數

對於 **Microsoft Foundry**（必填）：
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry 專案端點
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - 模型部署名稱（例如 gpt-5-mini）

對於 **Azure AI Search**（第05課 - RAG）：
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search 端點
- `AZURE_SEARCH_API_KEY` - Azure AI Search API 金鑰

認證：執行筆記本前請先執行 `az login`（使用 `AzureCliCredential`）。

## 開發工作流程

### 執行 Jupyter 筆記本

每個課程包含多個不同框架的 Jupyter 筆記本：

1. **啟動 Jupyter：**
   ```bash
   jupyter notebook
   ```

2. <strong>前往某個課程目錄</strong>（例如 `01-intro-to-ai-agents/code_samples/`）

3. **開啟並執行筆記本：**
   - `*-python-agent-framework.ipynb` - 使用 Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - 使用 Microsoft Agent Framework (.NET)

### 使用 Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry：**
- 需要 Azure 訂閱
- 使用 `FoundryChatClient` 連接 Agent Service V2（在 Foundry 入口網站可見代理人）
- 具備生產就緒的內建可觀測功能
- 檔案模式：`*-python-agent-framework.ipynb`

## 測試說明

這是一個教育性質的儲存庫，包含示範程式碼而非具有自動化測試的正式生產代碼。驗證設定及修改方法如下：

### 手動測試

1. **測試 Python 環境：**
   ```bash
   python --version  # 應該是 3.12 以上
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **測試筆記本執行：**
   ```bash
   # 將筆記本轉換為腳本並執行（測試匯入）
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **驗證環境變數：**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### 執行單一筆記本

在 Jupyter 中打開筆記本並依序執行程式碼區塊。每份筆記本均為獨立完整，包含：
- 導入語句
- 配置載入
- 範例代理人實作
- 預期輸出（Markdown 單元格）

### 部署代理人的冒煙測試

對於以 Microsoft Foundry 託管代理人形式部署的課程（01、04、05、16），此儲存庫提供了位於 `tests/` 下的冒煙測試目錄，並由 `.github/workflows/smoke-test.yml` 工作流程透過 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) 操作執行。這是一種輕量的部署後檢查（代理人是否可訪問且符合基本提示預期？），補充第10與16課的評估管線。詳見 [tests/README.md](./tests/README.md) 以了解目錄、課程與代理人對應。第17課採本地 Foundry Local 運行，無託管端點，故透過直接執行其筆記本進行驗證。

## 程式碼風格

### Python 慣例

- **Python 版本**：3.12+
- <strong>代碼風格</strong>：遵循標準 Python PEP 8 慣例
- <strong>筆記本</strong>：使用清晰的 Markdown 單元格說明概念
- <strong>導入</strong>：依標準庫、第三方、本地分組

### Jupyter 筆記本慣例

- 程式碼區塊前加入描述性 Markdown 單元格
- 筆記本中附加輸出範例以供參考
- 使用符合課程內容的清晰變數名稱
- 使筆記本執行順序線性（第1格→2格→3格...）

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

此儲存庫使用 Markdown 格式文件：
- 每個課程資料夾中的 README.md 檔案
- 儲存庫根目錄主要 README.md
- 透過 GitHub Actions 自動翻譯系統

### CI/CD 管線

位於 `.github/workflows/`：

1. **co-op-translator.yml** - 自動翻譯成超過50種語言
2. **welcome-issue.yml** - 歡迎新議題創建者
3. **welcome-pr.yml** - 歡迎新拉取請求貢獻者

### 部署

這是一個教學性質的儲存庫，無部署流程。用戶：
1. 分叉或複製儲存庫
2. 在本地或 GitHub Codespaces 執行筆記本
3. 透過修改與實驗範例學習

## 拉取請求指南

### 提交前

1. **測試您的修改：**
   - 完整執行受影響的筆記本
   - 確認所有程式碼區塊無錯誤執行
   - 檢查輸出是否適當

2. **文件更新：**
   - 若新增概念請更新 README.md
   - 在筆記本為較複雜程式碼加入註解
   - 確保 Markdown 單元格能解釋目的

3. **檔案變更：**
   - 避免提交 `.env` 檔案（使用 `.env.example`）
   - 不提交 `venv/` 或 `__pycache__/` 目錄
   - 範例展示時保持筆記本輸出
   - 移除臨時檔案和備份筆記本（`*-backup.ipynb`）

### PR 標題格式

使用具描述性的標題：
- `[Lesson-XX] 新增 <概念> 範例`
- `[Fix] 修正 lesson-XX README 打字錯誤`
- `[Update] 改善 lesson-XX 程式碼範例`
- `[Docs] 更新安裝說明`

### 必要檢查

- 筆記本應無錯誤執行
- README 文件應清晰且正確
- 遵循儲存庫現有程式碼模式
- 維持與其他課程一致性

## 附加說明

### 常見問題

1. **Python 版本不符：**
   - 確保使用 Python 3.12+
   - 部分套件可能不支援舊版
   - 使用 `python3 -m venv` 指定 Python 版本

2. **環境變數：**
   - 永遠由 `.env.example` 建立 `.env`
   - `.env` 檔案不應提交（已加入 `.gitignore`）
   - 使用 `az login` 登入，執行免密多重身份驗證

3. **套件衝突：**
   - 使用全新虛擬環境
   - 透過 `requirements.txt` 安裝套件，而非單獨安裝
   - 某些筆記本需安裝附加套件，詳見 Markdown 單元格說明

4. **Azure 服務：**
   - 需有效 Azure 訂閱
   - 部分功能受區域限制
   - 確認所部署的 Azure OpenAI 模型支援 Responses API

### 學習路徑

推薦依序進行的課程：
1. **00-course-setup** - 從此開始環境設定
2. **01-intro-to-ai-agents** - 了解 AI 代理人基礎
3. **02-explore-agentic-frameworks** - 學習不同框架
4. **03-agentic-design-patterns** - 核心設計模式
5. 按編號順序繼續後續課程

### 框架選擇

根據目標選擇框架：
- <strong>所有課程</strong>：使用 Microsoft Agent Framework (MAF) 搭配 `FoundryChatClient`
- <strong>代理人伺服器端註冊</strong> 至 Microsoft Foundry Agent Service V2，代理人可在 Foundry 入口網站看到

### 尋求協助

- 加入 [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- 閱讀課程 README 文件取得具體指引
- 查閱主 [README.md](./README.md) 了解課程概況
- 參考 [Course Setup](./00-course-setup/README.md) 以獲得詳細設定說明

### 貢獻方式

這是一個開放教育專案，歡迎貢獻：
- 改進程式碼範例
- 修正拼寫或錯誤
- 增加解說註解
- 建議新增課程主題
- 翻譯成更多語言

詳見 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) 了解當前需求。

## 專案特定內容

### 多語言支援

此儲存庫使用自動翻譯系統：
- 支援超過50種語言
- 翻譯存放於 `/translations/<lang-code>/` 目錄
- 由 GitHub Actions 工作流程自動更新翻譯
- 原始英語檔案位於儲存庫根目錄

### 課程結構

每課遵循一致格式：
1. 影片縮圖連結
2. 書面課程內容（README.md）
3. 多框架程式碼範例
4. 學習目標與先修條件
5. 額外學習資源連結

### 程式碼範例命名

格式：`<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 第1課，MAF Python
- `14-sequential.ipynb` - 第14課，MAF 進階模式
- `16-python-agent-framework.ipynb` - 第16課，生產用客戶支援代理人
- `17-local-agent-foundry-local.ipynb` - 第17課，使用 Foundry Local + Qwen 的本地代理人

### 特殊目錄

- `translated_images/` - 翻譯用本地化圖片
- `images/` - 英語原圖
- `.devcontainer/` - VS Code 開發容器配置
- `.github/` - GitHub Actions 工作流程與範本

### 相依套件

`requirements.txt` 主要套件：
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - 代理人間通訊協議支援
- `azure-ai-inference`、`azure-ai-projects` - Azure AI 服務
- `azure-identity` - Azure 認證（AzureCliCredential）
- `azure-search-documents` - Azure AI Search 整合
- `mcp[cli]` - 模型上下文協議支援

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->