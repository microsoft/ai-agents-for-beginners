# AGENTS.md

## 專案概述

此儲存庫包含「初學者 AI 代理人」— 一門全面的教育課程，教授建立 AI 代理人所需的所有知識。課程涵蓋 15 節以上的課程，包含基礎知識、設計模式、框架以及 AI 代理人的生產部署。

**主要技術：**
- Python 3.12+
- Jupyter 筆記本用於互動學習
- AI 框架：Microsoft Agent Framework (MAF)
- Azure AI 服務：Microsoft Foundry、Azure AI Foundry Agent Service V2

**架構：**
- 以課程為基礎結構（00-15+目錄）
- 每節課包含：README 文件、程式碼範例（Jupyter 筆記本）、與圖片
- 透過自動翻譯系統支援多語言
- 每課一個使用 Microsoft Agent Framework 的 Python 筆記本

## 設定指令

### 先決條件
- Python 3.12 或更高版本
- Azure 訂閱（用於 Azure AI Foundry）
- 已安裝並驗證身份的 Azure CLI（執行 `az login`）

### 初始設定

1. **克隆或分叉此儲存庫：**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # 或
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
   # 使用您的 API 金鑰和端點編輯 .env
   ```

### 必填環境變數

針對 **Azure AI Foundry**（必需）:
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry 專案端點
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - 模型部署名稱（例如：gpt-4o）

針對 **Azure AI Search**（第 05 章 - RAG）:
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search 端點
- `AZURE_SEARCH_API_KEY` - Azure AI Search API 金鑰

驗證身份：執行 `az login` 後再執行筆記本（使用 `AzureCliCredential`）。

## 開發流程

### 執行 Jupyter 筆記本

每節課包含多個針對不同框架的 Jupyter 筆記本：

1. **啟動 Jupyter：**
   ```bash
   jupyter notebook
   ```

2. **切換至課程目錄**（例如 `01-intro-to-ai-agents/code_samples/`）

3. **開啟並執行筆記本：**
   - `*-python-agent-framework.ipynb` - 使用 Microsoft Agent Framework（Python）
   - `*-dotnet-agent-framework.ipynb` - 使用 Microsoft Agent Framework（.NET）

### 使用 Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry：**
- 需要 Azure 訂閱
- 採用 `AzureAIProjectAgentProvider` 提供 Agent Service V2（代理人在 Foundry 入口網站中可見）
- 生產就緒，內建可監控性
- 檔案格式：`*-python-agent-framework.ipynb`

## 測試說明

此為教育用儲存庫，提供範例程式碼，非具有自動化測試的生產代碼。驗證設定與變更：

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

3. **確認環境變數設定：**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### 執行單一筆記本

於 Jupyter 打開筆記本並依序執行各單元格。每本筆記本獨立且包含：
- 匯入語句
- 配置載入
- 範例代理人實作
- Markdown 單元格中的預期輸出

## 程式碼風格

### Python 規範

- **Python 版本**：3.12+
- **程式風格**：遵守 Python PEP 8 標準
- **筆記本**：使用清晰的 markdown 單元格說明概念
- **匯入排序**：依標準庫、第三方套件、本地匯入分組

### Jupyter 筆記本慣例

- 在程式碼區塊前加入描述性的 markdown 單元格
- 筆記本中加入輸出範例供參考
- 使用清晰且符合課程概念的變數名稱
- 保持筆記本執行順序線性（單元格 1 → 2 → 3…）

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
- 各課程資料夾內的 README.md 文件
- 儲存庫根目錄的主 README.md
- 透過 GitHub Actions 執行自動翻譯系統

### CI/CD 管線

位於 `.github/workflows/`：

1. **co-op-translator.yml** - 自動翻譯為 50 多種語言
2. **welcome-issue.yml** - 歡迎新的 issue 建立者
3. **welcome-pr.yml** - 歡迎新的 pull request 貢獻者

### 部署

此為教育儲存庫，無部署流程。使用者：
1. 分叉或克隆儲存庫
2. 在本機或 GitHub Codespaces 執行筆記本
3. 透過修改與實驗範例來學習

## Pull Request 指南

### 提交前

1. **測試變更內容：**
   - 完整執行相關筆記本
   - 確認所有單元格皆能執行且無誤
   - 檢查輸出是否合理

2. **更新文件：**
   - 新增概念時更新 README.md
   - 在筆記本中加入複雜程式碼註解
   - 確保 markdown 單元格解釋目的

3. **檔案變更：**
   - 避免提交 `.env` 檔案（請使用 `.env.example`）
   - 不要提交 `venv/` 或 `__pycache__/` 目錄
   - 保留示範概念的筆記本輸出
   - 移除暫存檔與備份筆記本（`*-backup.ipynb`）

### PR 標題格式

使用描述性標題：
- `[Lesson-XX] 新增 <概念> 範例`
- `[Fix] 修正 lesson-XX README 拼字錯誤`
- `[Update] 改進 lesson-XX 的程式碼範例`
- `[Docs] 更新設定說明`

### 必需檢查

- 確保筆記本無錯誤執行
- README 文件清楚且準確
- 遵循儲存庫內既有程式碼規範
- 與其他課程保持一致性

## 其他注意事項

### 常見問題

1. **Python 版本不符：**
   - 請確保使用 Python 3.12+
   - 某些套件不適用舊版本
   - 使用 `python3 -m venv` 明確指定 Python 版本

2. **環境變數：**
   - 請務必從 `.env.example` 建立 `.env`
   - 避免提交 `.env` 文件（已加入 `.gitignore`）
   - GitHub Token 需具備適當權限

3. **套件衝突：**
   - 使用全新虛擬環境
   - 從 `requirements.txt` 安裝，不要單獨安裝個別套件
   - 部分筆記本需額外套件，請參閱 markdown 說明

4. **Azure 服務：**
   - 需有效的 Azure 訂閱
   - 有些功能區域受限
   - GitHub Models 有限制免費層額度

### 學習路徑

建議依序進行課程：
1. **00-course-setup** - 從環境設定開始
2. **01-intro-to-ai-agents** - 了解 AI 代理人基礎
3. **02-explore-agentic-frameworks** - 學習不同框架
4. **03-agentic-design-patterns** - 核心設計模式
5. 持續依序完成後續編號課程

### 框架選擇

依目標選擇框架：
- **所有課程**：採用 Microsoft Agent Framework (MAF) 與 `AzureAIProjectAgentProvider`
- **代理人註冊於 Azure AI Foundry Agent Service V2 伺服器端，並於 Foundry 入口網站可見**

### 尋求協助

- 參加 [Microsoft Foundry 社群 Discord](https://aka.ms/ai-agents/discord)
- 查閱各課程 README 文件以獲得具體指引
- 主 README.md 提供課程總覽
- 詳細設定說明見 [Course Setup](./00-course-setup/README.md)

### 參與貢獻

此為開放教育專案，歡迎貢獻：
- 改善程式碼範例
- 修正拼字或錯誤
- 增加說明註解
- 建議新課題
- 翻譯成更多語言

目前需求見 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues)。

## 專案特定內容

### 多語言支援

此儲存庫使用自動翻譯系統：
- 支援超過 50 種語言
- 翻譯結果放於 `/translations/<lang-code>/` 目錄
- GitHub Actions 工作流程自動更新翻譯
- 原文檔案位於儲存庫根目錄，語言為英語

### 課程結構

每節課遵循一致格式：
1. 附帶連結的影片縮圖
2. 書面課程內容（README.md）
3. 多框架的程式碼範例
4. 學習目標與先備條件
5. 輔助學習資源連結

### 程式碼範例命名

格式：`<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 第 1 課，MAF Python
- `14-sequential.ipynb` - 第 14 課，MAF 進階模式

### 特殊目錄

- `translated_images/` - 已本地化翻譯的圖片
- `images/` - 英文原始圖片
- `.devcontainer/` - VS Code 開發容器設定
- `.github/` - GitHub Actions 工作流程和範本

### 依賴套件

`requirements.txt` 的主要套件：
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent 協定支援
- `azure-ai-inference`, `azure-ai-projects` - Azure AI 服務
- `azure-identity` - Azure 驗證（AzureCliCredential）
- `azure-search-documents` - Azure AI Search 整合
- `mcp[cli]` - 模型上下文協定支援

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。我們雖致力於翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威依據。對於重要資訊，建議採用專業人工翻譯。本公司不對因使用本翻譯而產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->