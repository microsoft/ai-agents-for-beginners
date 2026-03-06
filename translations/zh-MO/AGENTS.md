# AGENTS.md

## 專案概覽

此存儲庫包含「初學者 AI 代理」— 一套全面的教育課程，教授建立 AI 代理所需的一切知識。課程由 15+ 課程組成，涵蓋基礎知識、設計模式、框架以及 AI 代理的生產部署。

**關鍵技術：**
- Python 3.12 以上版本
- 使用 Jupyter 筆記本進行互動學習
- AI 框架：Microsoft Agent Framework (MAF)
- Azure AI 服務：Microsoft Foundry、Azure AI Foundry Agent Service V2

**架構：**
- 課程結構依目錄劃分（00-15+）
- 每課包含：README 文件、程式碼範例（Jupyter 筆記本）及圖片
- 透過自動翻譯系統支持多語言
- 每課均有一個使用 Microsoft Agent Framework 的 Python 筆記本

## 設定指令

### 先決條件
- Python 3.12 或以上版本
- Azure 訂閱（用於 Azure AI Foundry）
- 已安裝及登入的 Azure CLI (`az login`)

### 初始設定

1. **克隆或分支此存儲庫：**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # 或者
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **建立並啟用 Python 虛擬環境：**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # 在 Windows：venv\Scripts\activate
   ```

3. **安裝依賴套件：**
   ```bash
   pip install -r requirements.txt
   ```

4. **設定環境變數：**
   ```bash
   cp .env.example .env
   # 使用您的 API 金鑰和端點編輯 .env
   ```

### 必須的環境變數

針對 **Azure AI Foundry**（必填）：
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry 專案端點
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - 模型部署名稱（如 gpt-4o）

針對 **Azure AI Search**（第 05 課 - RAG）：
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search 端點
- `AZURE_SEARCH_API_KEY` - Azure AI Search API 金鑰

認證：在執行筆記本前請執行 `az login`（使用 `AzureCliCredential`）。

## 開發工作流程

### 執行 Jupyter 筆記本

每課包含多個不同框架的 Jupyter 筆記本：

1. **啟動 Jupyter：**
   ```bash
   jupyter notebook
   ```

2. **進入某課程目錄**（例如 `01-intro-to-ai-agents/code_samples/`）

3. **開啟並執行筆記本：**
   - `*-python-agent-framework.ipynb` — 使用 Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` — 使用 Microsoft Agent Framework (.NET)

### 使用 Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry：**
- 需要 Azure 訂閱
- 使用 `AzureAIProjectAgentProvider` 連接 Agent Service V2（代理於 Foundry 入口網站可見）
- 支援生產環境，內建可觀察性
- 檔案命名格式：`*-python-agent-framework.ipynb`

## 測試指引

此為教育用存儲庫，含範例程式碼，無生產等級自動化測試。驗證設定及修改請執行：

### 手動測試

1. **測試 Python 環境：**
   ```bash
   python --version  # 應該是 3.12 或以上
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **測試筆記本執行：**
   ```bash
   # 將筆記本轉換為腳本並執行（測試導入）
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **驗證環境變數設定：**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### 單獨執行筆記本

於 Jupyter 中打開筆記本，依序執行各儲存格。每本筆記本皆自成一格並包含：
- 匯入語句
- 設定載入
- 範例代理實作
- Markdown 儲存格中的預期輸出

## 程式碼風格

### Python 慣例

- **Python 版本**：3.12+
- **程式碼風格**：遵循標準 Python PEP 8 慣例
- **筆記本**：以清晰的 markdown 儲存格說明概念
- **匯入語句**：按標準庫、第三方、本地庫分組

### Jupyter 筆記本慣例

- 於程式碼儲存格前加入描述性 markdown
- 筆記本中包含輸出範例供參考
- 使用清楚且符課程概念的變數命名
- 保持筆記本執行順序線性（儲存格 1 → 2 → 3 ...）

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

## 建構與部署

### 文件建構

此存儲庫使用 Markdown 文件：
- 各課文件夾包含 README.md
- 存儲庫根目錄有主要 README.md
- 透過 GitHub Actions 自動翻譯系統維護多語言

### CI/CD 流程

位於 `.github/workflows/`：

1. **co-op-translator.yml** — 自動翻譯至 50+ 種語言
2. **welcome-issue.yml** — 歡迎新議題建立者
3. **welcome-pr.yml** — 歡迎新拉取請求貢獻者

### 部署

此為教育存儲庫，無部署流程。使用者流程：
1. Fork 或克隆存儲庫
2. 在本地或 GitHub Codespaces 運行筆記本
3. 通過修改與實驗範例學習

## 拉取請求指南

### 提交前

1. **測試變更：**
   - 完整運行受影響筆記本
   - 確認所有儲存格無錯誤且執行通過
   - 確認輸出符合預期

2. **文檔更新：**
   - 若新增概念，更新 README.md
   - 筆記本中添加複雜程式碼之註解
   - 用 markdown 儲存格說明用途

3. **檔案變更：**
   - 避免提交 `.env` 檔案（請使用 `.env.example`）
   - 不提交 `venv/` 或 `__pycache__/` 目錄
   - 保留可展示概念的筆記本輸出
   - 刪除暫存文件與備份筆記本（`*-backup.ipynb`）

### PR 標題格式

使用描述性標題：
- `[Lesson-XX] 新增 <概念> 範例`
- `[Fix] 修正 lesson-XX README 打字錯誤`
- `[Update] 改善 lesson-XX 程式碼範例`
- `[Docs] 更新設定說明`

### 必需檢查項

- 筆記本應無錯誤執行
- README 文件應清晰且準確
- 遵循已有程式碼風格
- 與其他課程保持一致性

## 附加說明

### 常見問題

1. **Python 版本不符：**
   - 請使用 Python 3.12 以上
   - 某些套件不支援舊版本
   - 使用 `python3 -m venv` 指定版本創建虛擬環境

2. **環境變數問題：**
   - 一定從 `.env.example` 建立 `.env`
   - 不要提交 `.env` 檔案（已列入 `.gitignore`）
   - GitHub token 需具適當權限

3. **套件衝突：**
   - 使用全新虛擬環境
   - 從 `requirements.txt` 安裝依賴，不要單獨裝包
   - 部分筆記本 markdown 中提及需要額外套件

4. **Azure 服務：**
   - 需有效 Azure 訂閱
   - 某些功能受限於區域
   - GitHub Models 受免費等級限制

### 學習路線

建議依序學習：
1. **00-course-setup** — 環境設定起點
2. **01-intro-to-ai-agents** — AI 代理基礎
3. **02-explore-agentic-frameworks** — 各類框架介紹
4. **03-agentic-design-patterns** — 核心設計模式
5. 按照編號課程逐步進行

### 框架選擇

依目標選擇框架：
- **所有課程**：Microsoft Agent Framework (MAF) 搭配 `AzureAIProjectAgentProvider`
- 代理於 Azure AI Foundry Agent Service V2 伺服器端註冊，並於 Foundry 入口網站可見

### 尋求協助

- 加入 [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- 查看課程 README 文件內的具體指引
- 參閱主 README.md 檔案了解課程總覽
- 詳看 [Course Setup](./00-course-setup/README.md) 取得詳細設定指示

### 貢獻指南

這是一個開放的教育專案，歡迎貢獻：
- 改善程式碼範例
- 修正錯字或錯誤
- 增添說明性註解
- 建議新增課程主題
- 協助翻譯成其他語言

請參閱 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) 了解當前需求。

## 專案特定背景

### 多語言支援

此存儲庫使用自動翻譯系統：
- 支援 50+ 種語言
- 翻譯內容位於 `/translations/<lang-code>/` 目錄
- GitHub Actions 工作流程處理翻譯更新
- 原始文件使用英文，存於存儲庫根目錄

### 課程結構

每課遵循一致模式：
1. 影片縮圖連結
2. 課程文字內容（README.md）
3. 多框架程式碼範例
4. 學習目標及前提條件
5. 連結額外學習資源

### 程式碼範例命名

格式：`<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` — 第 1 課，MAF Python
- `14-sequential.ipynb` — 第 14 課，MAF 進階範例

### 特殊目錄

- `translated_images/` — 本地化圖片
- `images/` — 英文原始圖片
- `.devcontainer/` — VS Code 開發容器設定
- `.github/` — GitHub Actions 工作流程及模板

### 依賴

主要套件於 `requirements.txt`：
- `agent-framework` — Microsoft Agent Framework
- `a2a-sdk` — Agent-to-Agent 通訊協定支援
- `azure-ai-inference`、`azure-ai-projects` — Azure AI 服務
- `azure-identity` — Azure 身份驗證（AzureCliCredential）
- `azure-search-documents` — Azure AI Search 整合
- `mcp[cli]` — 模型上下文協定支援

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件乃使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。儘管我們致力於追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的原文語言版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引致的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->