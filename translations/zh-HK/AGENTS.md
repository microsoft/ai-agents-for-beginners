# AGENTS.md

## 專案概覽

This repository contains "AI Agents for Beginners" - a comprehensive educational course teaching everything needed to build AI Agents. The course consists of 15+ lessons covering fundamentals, design patterns, frameworks, and production deployment of AI agents.

**主要技術：**
- Python 3.12+
- 用於互動學習的 Jupyter Notebooks
- AI 框架：Microsoft Agent Framework (MAF)
- Azure AI 服務：Microsoft Foundry、Azure AI Foundry Agent Service V2

**架構：**
- 以課程為單位的結構（00-15+ 目錄）
- 每課包含：README 文件、程式碼範例（Jupyter 筆記本），以及圖片
- 透過自動翻譯系統提供多語言支援
- 每課一份使用 Microsoft Agent Framework 的 Python 筆記本

## 設定指令

### 前置需求
- Python 3.12 或更高
- Azure 訂閱（用於 Azure AI Foundry）
- 已安裝並驗證 Azure CLI（`az login`）

### 初始設定

1. **複製或 fork 此儲存庫：**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # 或
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **建立並啟用 Python 虛擬環境：**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # 在 Windows 上： venv\Scripts\activate
   ```

3. **安裝相依套件：**
   ```bash
   pip install -r requirements.txt
   ```

4. **設定環境變數：**
   ```bash
   cp .env.example .env
   # 用你的 API 金鑰和端點編輯 .env 檔案
   ```

### 必需的環境變數

針對 **Azure AI Foundry**（必要）:
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (e.g., gpt-4o)

針對 **Azure AI Search**（Lesson 05 - RAG）:
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Run `az login` before running notebooks (uses `AzureCliCredential`).

## 開發流程

### 執行 Jupyter 筆記本

每課包含多個針對不同框架的 Jupyter 筆記本：

1. **啟動 Jupyter：**
   ```bash
   jupyter notebook
   ```

2. **前往課程資料夾**（例如 `01-intro-to-ai-agents/code_samples/`）

3. **開啟並執行筆記本：**
   - `*-python-agent-framework.ipynb` - 使用 Microsoft Agent Framework（Python）
   - `*-dotnet-agent-framework.ipynb` - 使用 Microsoft Agent Framework（.NET）

### 使用 Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry：**
- 需要 Azure 訂閱
- 使用 `AzureAIProjectAgentProvider` 於 Agent Service V2（agents 可在 Foundry 入口網站檢視）
- 生產就緒，內建可觀測性
- 檔案命名模式：`*-python-agent-framework.ipynb`

## 測試說明

這是示範程式碼為主的教育性儲存庫，而非具自動化測試的生產程式。要驗證你的設定與變更：

### 手動測試

1. **測試 Python 環境：**
   ```bash
   python --version  # 應該為 3.12 或以上
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **測試筆記本執行：**
   ```bash
   # 將 notebook 轉換為腳本並執行 (測試匯入)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **驗證環境變數：**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### 執行單一筆記本

在 Jupyter 中開啟筆記本並依序執行各儲存格。每本筆記本為自包含，並包含：
- 匯入敘述
- 設定載入
- 範例代理實作
- Markdown 儲存格中的預期輸出

## 程式風格

### Python 慣例

- **Python 版本**：3.12+
- **程式風格**：遵循標準 Python PEP 8 規範
- **筆記本**：使用清晰的 Markdown 儲存格來說明概念
- **匯入（Imports）**：依標準函式庫、第三方、本地匯入分組

### Jupyter 筆記本慣例

- 在程式區塊前加入描述性 Markdown 儲存格
- 在筆記本中加入輸出範例以供參考
- 使用與課程概念相符的清晰變數名稱
- 保持筆記本執行順序線性（cell 1 → 2 → 3...）

### 檔案結構

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

此儲存庫使用 Markdown 作為文件格式：
- README.md 檔案位於每個課程資料夾
- 主要的 README.md 位於儲存庫根目錄
- 透過 GitHub Actions 的自動翻譯系統

### CI/CD 流程

位於 `.github/workflows/`：

1. **co-op-translator.yml** - 自動翻譯至 50+ 種語言
2. **welcome-issue.yml** - 歡迎新的 issue 建立者
3. **welcome-pr.yml** - 歡迎新的 pull request 貢獻者

### 部署

這是一個教育性儲存庫 — 沒有部署流程。使用者：
1. Fork 或複製此儲存庫
2. 本地或在 GitHub Codespaces 執行筆記本
3. 透過修改與實驗範例來學習

## Pull Request 指南

### 提交前

1. **測試你的變更：**
   - 完整執行受影響的筆記本
   - 確認所有儲存格執行無錯誤
   - 檢查輸出是否適當

2. **文件更新：**
   - 若加入新概念，更新 README.md
   - 在筆記本中為複雜程式加入註解
   - 確保 Markdown 儲存格說明目的

3. **檔案變更：**
   - 避免提交 `.env` 檔案（使用 `.env.example`）
   - 不要提交 `venv/` 或 `__pycache__/` 目錄
   - 若輸出能說明概念，保留筆記本輸出
   - 移除暫存檔與備份筆記本（`*-backup.ipynb`）

### PR 標題格式

Use descriptive titles:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### 必要檢查

- 筆記本應無錯誤執行
- README 檔案應清晰且正確
- 遵循儲存庫中既有的程式範例
- 與其他課程保持一致性

## 其他注意事項

### 常見陷阱

1. **Python 版本不符：**
   - 確保使用 Python 3.12+
   - 某些套件在較舊版本可能無法運作
   - 使用 `python3 -m venv` 明確指定 Python 版本

2. **環境變數：**
   - 永遠從 `.env.example` 建立 `.env`
   - 不要提交 `.env` 檔案（已列入 `.gitignore`）
   - GitHub token 需有適當權限

3. **套件衝突：**
   - 使用新的虛擬環境
   - 由 `requirements.txt` 安裝而非逐一安裝套件
   - 某些筆記本可能需要其 Markdown 儲存格中提到的額外套件

4. **Azure 服務：**
   - Azure AI 服務需要有效訂閱
   - 某些功能依區域而異
   - GitHub Models 的免費方案有使用限制

### 學習路徑

建議的課程進度：
1. **00-course-setup** - 從此處開始環境設定
2. **01-intro-to-ai-agents** - 了解 AI agent 基礎
3. **02-explore-agentic-frameworks** - 學習不同框架
4. **03-agentic-design-patterns** - 主要設計模式
5. 依序繼續完成編號課程

### 框架選擇

依你的目標選擇框架：
- **所有課程**：Microsoft Agent Framework (MAF) 與 `AzureAIProjectAgentProvider`
- **代理在 server-side 註冊** 於 Azure AI Foundry Agent Service V2，並可在 Foundry 入口網站檢視

### 尋求協助

- 加入 [Microsoft Foundry 社群 Discord](https://aka.ms/ai-agents/discord)
- 檢視各課 README 檔以取得特定指引
- 查看主要的 [README.md](./README.md) 以取得課程概覽
- 參考 [Course Setup](./00-course-setup/README.md) 以取得詳細設定指示

### 貢獻

這是一個開放的教育專案。歡迎貢獻：
- 改善程式範例
- 修正錯字或錯誤
- 新增釐清性註解
- 建議新的課程主題
- 翻譯成更多語言

請參閱 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) 以了解當前需求。

## 專案特定背景

### 多語言支援

此儲存庫使用自動翻譯系統：
- 支援 50+ 種語言
- 翻譯存放於 `/translations/<lang-code>/` 目錄
- 由 GitHub Actions 工作流程處理翻譯更新
- 原始檔案為英文，位於儲存庫根目錄

### 課程結構

每課遵循一致的模式：
1. 影片縮圖與連結
2. 書面課程內容（README.md）
3. 多框架的程式範例
4. 學習目標與先備需求
5. 其他學習資源連結

### 程式範例命名

格式：`<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 第 1 課，MAF Python
- `14-sequential.ipynb` - 第 14 課，MAF 進階模式

### 特別目錄

- `translated_images/` - 用於翻譯的在地化圖片
- `images/` - 英文內容的原始圖片
- `.devcontainer/` - VS Code 開發容器設定
- `.github/` - GitHub Actions 工作流程與範本

### 相依套件

來自 `requirements.txt` 的主要套件：
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - 支援 Agent-to-Agent 通訊協定
- `azure-ai-inference`, `azure-ai-projects` - Azure AI 服務
- `azure-identity` - Azure 認證（AzureCliCredential）
- `azure-search-documents` - Azure AI Search 整合
- `mcp[cli]` - 支援 Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件已使用人工智能翻譯服務「Co‑op Translator」(https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但自動翻譯可能含有錯誤或不準確之處。原文檔案應被視為具權威性的來源。對於重要資訊，建議採用專業人工翻譯。我們不會就因使用本翻譯而引致的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->