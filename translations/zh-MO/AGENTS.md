# AGENTS.md

## 專案概覽

本儲存庫包含「初學者 AI 代理人」— 一個全面的教育課程，教授建構 AI 代理人所需的一切。課程由 18 課（編號 00-18）組成，涵蓋基礎、設計模式、框架、產品部署、本地/裝置代理人與 AI 代理人安全性。

**關鍵技術：**
- Python 3.12 以上
- 用於互動學習的 Jupyter 筆記本
- AI 框架：Microsoft 代理框架（MAF）
- Azure AI 服務：Microsoft Foundry、Microsoft Foundry 代理服務 V2

**架構：**
- 以課程為基礎的結構（00-15+ 資料夾）
- 每課包含：README 文件、程式碼範例（Jupyter 筆記本）與圖片
- 透過自動翻譯系統支援多語言
- 每課一個使用 Microsoft 代理框架的 Python 筆記本

## 設定指令

### 前置需求
- Python 3.12 或以上版本
- Azure 訂閱（用於 Microsoft Foundry）
- 已安裝並認證的 Azure CLI（`az login`）

### 初始設定

1. **克隆或衍生此儲存庫：**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # 或
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **建立並啟用 Python 虛擬環境：**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # 在 Windows 上：venv\Scripts\activate
   ```

3. **安裝依賴套件：**
   ```bash
   pip install -r requirements.txt
   ```

4. **設定環境變數：**
   ```bash
   cp .env.example .env
   # 編輯 .env，加入你的 API 金鑰及端點
   ```

### 必需的環境變數

對於 **Microsoft Foundry**（必需）：
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry 專案端點
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - 模型部署名稱（例如：gpt-5-mini）

對於 **Azure AI Search**（第五課 - RAG）：
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search 端點
- `AZURE_SEARCH_API_KEY` - Azure AI Search API 金鑰

驗證：執行筆記本前請先執行 `az login`（使用 `AzureCliCredential`）。

## 開發工作流程

### 運行 Jupyter 筆記本

每課包含不同框架的多個 Jupyter 筆記本：

1. **啟動 Jupyter：**
   ```bash
   jupyter notebook
   ```

2. <strong>進入課程資料夾</strong>（例如 `01-intro-to-ai-agents/code_samples/`）

3. **開啟並執行筆記本：**
   - `*-python-agent-framework.ipynb` - 使用 Microsoft 代理框架（Python）
   - `*-dotnet-agent-framework.ipynb` - 使用 Microsoft 代理框架（.NET）

### 使用 Microsoft 代理框架

**Microsoft 代理框架 + Microsoft Foundry：**
- 需 Azure 訂閱
- 使用 `FoundryChatClient` 連接代理服務 V2（代理於 Foundry 入口網站可見）
- 具備生產級別的監控能力
- 檔案範例：`*-python-agent-framework.ipynb`

## 測試說明

本為教育用儲存庫，包含示範程式碼，非具備自動化測試的生產代碼。欲驗證你的設定與變更：

### 手動測試

1. **測試 Python 環境：**
   ```bash
   python --version  # 應該係3.12或以上
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **測試筆記本執行：**
   ```bash
   # 將筆記本轉換為腳本並運行（測試匯入）
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **驗証環境變數：**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### 執行單個筆記本

在 Jupyter 中開啟筆記本並依序執行各個儲存格。每個筆記本獨立且包含：
- 匯入語句
- 配置載入
- 範例代理人實作
- Markdown 儲存格中的預期輸出

### 對已部署代理人進行初步測試

對於以 Microsoft Foundry 托管代理人方式部署的課程（01、04、05、16），儲存庫提供位於 `tests/` 下的初步測試目錄，透過 `.github/workflows/smoke-test.yml` 工作流程使用 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) 操作執行。這是一個簡易的部署後檢查（代理是否可達且基本提示是否符合預期？），用以補充第 10 與第 16 課的評估流程。請參閱 [tests/README.md](./tests/README.md) 了解測試目錄、課程與代理人對應情形。第 17 課在本地使用 Foundry Local 執行，無託管端點，因此直接執行筆記本驗證。

## 程式碼風格

### Python 慣例

- **Python 版本**：3.12 以上
- <strong>程式碼風格</strong>：遵循標準 Python PEP 8 規範
- <strong>筆記本</strong>：使用清楚的 Markdown 儲存格說明概念
- <strong>匯入</strong>：分組標準函式庫、第三方套件及本地匯入

### Jupyter 筆記本慣例

- 在程式碼儲存格前加說明性 Markdown 儲存格
- 筆記本中加入輸出範例作為參考
- 使用清晰且符合課程概念的變數名稱
- 筆記本執行順序保持直線（一 → 二 → 三……）

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

本儲存庫使用 Markdown 作為文件格式：
- 每課資料夾內的 README.md 檔案
- 儲存庫根目錄的主 README.md
- 透過 GitHub Actions 自動化翻譯系統

### CI/CD 管線

位於 `.github/workflows/`：

1. **co-op-translator.yml** - 自動翻譯成 50 多種語言
2. **welcome-issue.yml** - 歡迎新議題提案者
3. **welcome-pr.yml** - 歡迎新拉取請求貢獻者

### 部署

本儲存庫為教育用，無佈署流程。使用者可：
1. 分叉或克隆儲存庫
2. 本地或 GitHub Codespaces 運行筆記本
3. 透過修改與嘗試範例學習

## 拉取請求指引

### 提交前

1. **測試你的變更：**
   - 完整執行受影響的筆記本
   - 確保所有儲存格無錯誤執行
   - 檢查輸出是否合適

2. **文件更新：**
   - 新增概念時更新 README.md
   - 筆記本中複雜程式碼加入註解
   - 確保 Markdown 儲存格說明目的

3. **檔案變更：**
   - 避免提交 `.env` 檔案（改用 `.env.example`）
   - 不提交 `venv/` 或 `__pycache__/` 目錄
   - 若筆記本輸出說明概念，保留輸出
   - 移除臨時檔與備份筆記本（`*-backup.ipynb`）

### 拉取請求標題格式

使用具描述性的標題：
- `[Lesson-XX] 新增 <概念> 範例`
- `[Fix] 修正第 XX 課 README 的錯字`
- `[Update] 改進第 XX 課的程式碼範例`
- `[Docs] 更新設定說明`

### 必需通過的檢查項目

- 筆記本應無錯誤執行
- README 文件應清晰且準確
- 遵循儲存庫現有程式碼樣式
- 維持與其他課程一致性

## 附加注意事項

### 常見問題

1. **Python 版本不匹配：**
   - 確保使用 Python 3.12+
   - 部分套件在舊版本可能無法運作
   - 使用 `python3 -m venv` 明確指定 Python 版本

2. **環境變數：**
   - 永遠從 `.env.example` 建立 `.env`
   - 不提交 `.env` 檔案（列入 `.gitignore`）
   - 以 `az login` 登入使用無鑰匙 Entra ID 驗證

3. **套件衝突：**
   - 使用全新虛擬環境
   - 從 `requirements.txt` 安裝套件，避免單獨安裝
   - 部分筆記本可能需額外套件，詳見其 Markdown 儲存格說明

4. **Azure 服務：**
   - Azure AI 服務需有效訂閱
   - 部分功能具區域限制
   - 確保 Azure OpenAI 模型部署支持 Responses API

### 學習路線

推薦依序學習課程：
1. **00-course-setup** - 從此開始環境設定
2. **01-intro-to-ai-agents** - 了解 AI 代理人基礎
3. **02-explore-agentic-frameworks** - 學習不同框架
4. **03-agentic-design-patterns** - 核心設計模式
5. 依序接續數字編號課程

### 框架選擇

根據目標選擇框架：
- <strong>所有課程</strong>：使用 Microsoft 代理框架（MAF）與 `FoundryChatClient`
- <strong>代理人於伺服器端註冊</strong>於 Microsoft Foundry 代理服務 V2，並於 Foundry 入口網站可見

### 獲取協助

- 加入 [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- 查閱課程 README 文件以獲取具體指導
- 檢視主 [README.md](./README.md) 以了解課程概覽
- 參考 [Course Setup](./00-course-setup/README.md) 得詳細設定說明

### 貢獻

這是開放的教育專案，歡迎貢獻：
- 改進程式碼範例
- 修正錯字或錯誤
- 新增澄清註解
- 建議新增課程主題
- 翻譯為其他語言

請參閱 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) 查看目前需求。

## 專案特定背景

### 多語言支援

本儲存庫使用自動翻譯系統：
- 支援 50 多種語言
- 翻譯檔案位於 `/translations/<lang-code>/` 目錄
- GitHub Actions 工作流程負責翻譯更新
- 源檔為英文，位於儲存庫根目錄

### 課程結構

每課遵循一致模式：
1. 視頻縮圖附連結
2. 課文內容（README.md）
3. 多框架程式碼範例
4. 學習目標與前置需求
5. 附加學習資源連結

### 程式碼範例命名

格式：`<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 第 1 課，MAF Python
- `14-sequential.ipynb` - 第 14 課，MAF 進階模式
- `16-python-agent-framework.ipynb` - 第 16 課，生產用客戶支援代理人
- `17-local-agent-foundry-local.ipynb` - 第 17 課，使用 Foundry Local + Qwen 的本地代理人

### 特殊資料夾

- `translated_images/` - 本地化圖片
- `images/` - 英文內容原始圖片
- `.devcontainer/` - VS Code 開發容器設定
- `.github/` - GitHub Actions 工作流程與範本

### 依賴套件

來自 `requirements.txt` 的主要套件：
- `agent-framework` - Microsoft 代理框架
- `a2a-sdk` - 代理間通訊協定支援
- `azure-ai-inference`、`azure-ai-projects` - Azure AI 服務
- `azure-identity` - Azure 驗證（AzureCliCredential）
- `azure-search-documents` - Azure AI Search 整合
- `mcp[cli]` - 模型上下文通訊協定支援

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->