# AGENTS.md

## 專案概述

此儲存庫包含「初學者 AI 代理」- 一個全面的教育課程，教授建立 AI 代理所需的一切。該課程包含 15+ 課程，涵蓋基礎、設計模式、框架及 AI 代理的生產部署。

**關鍵技術：**
- Python 3.12+
- 用於互動學習的 Jupyter 筆記本
- AI 框架：Microsoft Agent Framework (MAF)
- Azure AI 服務：Microsoft Foundry、Azure AI Foundry Agent Service V2

**架構：**
- 基於課程的結構（00-15+ 目錄）
- 每個課程包含：README 文件、程式碼範例（Jupyter 筆記本）、圖片
- 透過自動翻譯系統支援多語言
- 每課一份使用 Microsoft Agent Framework 的 Python 筆記本

## 安裝指令

### 先決條件
- Python 3.12 或更高版本
- Azure 訂閱（用於 Azure AI Foundry）
- 安裝並登入 Azure CLI（`az login`）

### 初始設定

1. **克隆或分支此儲存庫：**
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
   # 編輯 .env 並加入您的 API 金鑰和端點
   ```

### 必要環境變數

針對 **Azure AI Foundry**（必須）：
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry 專案端點
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - 模型部署名稱（例如 gpt-4o）

針對 **Azure AI Search**（第 05 課 - RAG）：
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search 端點
- `AZURE_SEARCH_API_KEY` - Azure AI Search API 金鑰

身分驗證：執行筆記本前先執行 `az login`（使用 `AzureCliCredential`）。

## 開發流程

### 執行 Jupyter 筆記本

每堂課含多個針對不同框架的 Jupyter 筆記本：

1. **啟動 Jupyter：**
   ```bash
   jupyter notebook
   ```

2. **瀏覽至某課程目錄**（例如 `01-intro-to-ai-agents/code_samples/`）

3. **開啟並執行筆記本：**
   - `*-python-agent-framework.ipynb` - 使用 Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - 使用 Microsoft Agent Framework (.NET)

### 使用 Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry：**
- 需要 Azure 訂閱
- 使用 `AzureAIProjectAgentProvider` 連接 Agent Service V2（代理可於 Foundry 入口網站查看）
- 生產級，內建可觀察性
- 檔案格式：`*-python-agent-framework.ipynb`

## 測試說明

此為教育用途儲存庫，內容為示例程式碼，非生產及自動化測試程式碼。驗證環境與更動：

### 手動測試

1. **測試 Python 環境：**
   ```bash
   python --version  # 應該是 3.12 以上
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **測試筆記本執行：**
   ```bash
   # 將筆記本轉換為腳本並運行（測試導入）
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **驗證環境變數：**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### 執行個別筆記本

於 Jupyter 開啟筆記本依序執行所有儲存格。每份筆記本皆自含且包括：
- 匯入語句
- 設定載入
- 範例代理實作
- 期望輸出於 markdown 儲存格內

## 程式碼風格

### Python 規範

- **Python 版本**：3.12+
- **程式碼風格**：遵循 Python PEP 8 標準
- **筆記本**：使用清晰 markdown 儲存格說明概念
- **匯入**：依標準程式庫、第三方、區域匯入群組

### Jupyter 筆記本規範

- 代碼區前加描述性 markdown 儲存格
- 筆記本中附上輸出範例供參考
- 使用與課程概念相符的變數名稱
- 筆記本執行順序保持線性（儲存格 1 → 2 → 3 ...）

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

此儲存庫使用 Markdown 撰寫文件：
- 每課資料夾內 README.md
- 儲存庫根目錄的主要 README.md
- 透過 GitHub Actions 自動翻譯系統

### CI/CD 管線

位於 `.github/workflows/`：

1. **co-op-translator.yml** - 自動翻譯成 50+ 種語言
2. **welcome-issue.yml** - 歡迎新 issue 建立者
3. **welcome-pr.yml** - 歡迎新 pull request 貢獻者

### 部署

此為教育用儲存庫，無部署流程。使用者：
1. 分支或克隆儲存庫
2. 於本機或 GitHub Codespaces 執行筆記本
3. 透過修改及實驗範例學習

## Pull Request 指南

### 提交前

1. **測試變更：**
   - 完整執行受影響的筆記本
   - 確認所有儲存格無錯誤
   - 並檢查輸出是否合理

2. **文件更新：**
   - 新增概念需更新 README.md
   - 筆記本中複雜程式碼加註解
   - markdown 儲存格須說明目的

3. **檔案變更：**
   - 避免提交 `.env` 檔（使用 `.env.example`）
   - 不提交 `venv/` 或 `__pycache__/` 目錄
   - 保留示範概念的筆記本輸出
   - 移除暫存檔與備份筆記本 (`*-backup.ipynb`)

### PR 標題格式

使用描述性標題：
- `[Lesson-XX] 新增 <概念> 範例`
- `[Fix] 修正 lesson-XX README 打字錯誤`
- `[Update] 改善 lesson-XX 範例程式碼`
- `[Docs] 更新安裝說明`

### 必需檢查項目

- 筆記本執行無誤
- README 清楚且正確
- 遵守現有程式碼風格
- 與其他課程保持一致

## 額外說明

### 常見問題

1. **Python 版本不符：**
   - 確保使用 Python 3.12+
   - 舊版本某些套件可能無法運作
   - 使用 `python3 -m venv` 指定 Python 版本

2. **環境變數：**
   - 始終由 `.env.example` 新建 `.env`
   - 不提交 `.env`（已列入 `.gitignore`）
   - GitHub token 需有適當權限

3. **套件衝突：**
   - 建議使用全新虛擬環境
   - 從 `requirements.txt` 安裝，非單獨安裝套件
   - 某些筆記本需求額外套件，詳見其 markdown 儲存格

4. **Azure 服務：**
   - 需有效 Azure 訂閱
   - 部分功能區域限定
   - GitHub 模型有免費層限制

### 學習路徑

建議依序學習課程：
1. **00-course-setup** - 環境建置起點
2. **01-intro-to-ai-agents** - 理解 AI 代理基礎
3. **02-explore-agentic-frameworks** - 認識不同框架
4. **03-agentic-design-patterns** - 核心設計模式
5. 依序至後續課程

### 框架選擇

根據目標選擇框架：
- **所有課程**：使用 Microsoft Agent Framework (MAF)，搭配 `AzureAIProjectAgentProvider`
- **代理伺服器端註冊**於 Azure AI Foundry Agent Service V2，並可在 Foundry 入口網站查看

### 尋求協助

- 加入 [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- 查閱各課 README 文件取得指導
- 參考主 README.md（./README.md）了解課程概況
- 詳見 [課程設定說明](./00-course-setup/README.md)

### 參與貢獻

此為開放教育專案，歡迎貢獻：
- 改善程式碼範例
- 修正文法或錯誤
- 增加註解說明
- 建議新課題目
- 翻譯至其他語言

請參考 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) 了解目前需求。

## 專案特定說明

### 多語言支援

本儲存庫使用自動翻譯系統：
- 支援 50+ 種語言
- 翻譯檔於 `/translations/<lang-code>/` 目錄中
- 由 GitHub Actions 工作流程自動更新翻譯
- 原始檔案以英文儲存在儲存庫根目錄

### 課程結構

每堂課遵循固定模式：
1. 影片縮圖與連結
2. 純文字課程內容（README.md）
3. 多框架程式碼範例
4. 學習目標與先備知識
5. 附加學習資源連結

### 範例命名規範

格式：`<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 第 1 課，MAF Python 版本
- `14-sequential.ipynb` - 第 14 課，MAF 進階模式

### 特殊目錄

- `translated_images/` - 已翻譯圖片
- `images/` - 英文原始圖片
- `.devcontainer/` - VS Code 開發容器設定
- `.github/` - GitHub Actions 工作流程與範本

### 相依套件

自 `requirements.txt` 重要套件：
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - 代理對代理通訊協定支援
- `azure-ai-inference`, `azure-ai-projects` - Azure AI 服務
- `azure-identity` - Azure 身分驗證（AzureCliCredential）
- `azure-search-documents` - Azure AI Search 整合
- `mcp[cli]` - 模型上下文協定支援

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提升準確性，請注意自動翻譯可能包含錯誤或不精確之處。原始文件的母語版本應視為具權威性的參考來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯所引起的任何誤解或錯誤詮釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->