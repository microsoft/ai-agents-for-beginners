# AGENTS.md

## Project Overview

此儲存庫包含「初學者 AI 代理」— 一個全面的教育課程，教授構建 AI 代理所需的一切知識。課程由15堂以上的課程組成，涵蓋基礎知識、設計模式、框架及 AI 代理的生產部署。

**主要技術：**
- Python 3.12+
- 用於互動學習的 Jupyter 筆記本
- AI 框架：Microsoft Agent Framework (MAF)
- Azure AI 服務：Microsoft Foundry、Azure AI Foundry Agent Service V2

**架構：**
- 基於課程結構（00-15+ 目錄）
- 每堂課包含：README 文件、程式碼範例（Jupyter 筆記本）及圖像
- 多語言支援透過自動翻譯系統
- 每堂課一個使用 Microsoft Agent Framework 的 Python 筆記本

## Setup Commands

### Prerequisites
- Python 3.12 或更高版本
- Azure 訂閱 (用於 Azure AI Foundry)
- 已安裝並驗證身份的 Azure CLI (`az login`)

### Initial Setup

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
   # 用你的 API 金鑰和端點編輯 .env
   ```

### Required Environment Variables

對於 **Azure AI Foundry** (必須):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry 項目端點
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - 模型部署名稱（例如 gpt-4o）

對於 **Azure AI Search** (課程 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search 端點
- `AZURE_SEARCH_API_KEY` - Azure AI Search API 金鑰

身份驗證：在執行筆記本前執行 `az login`（使用 `AzureCliCredential`）。

## Development Workflow

### Running Jupyter Notebooks

每堂課包含多個框架的 Jupyter 筆記本：

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigate to a lesson directory** (例如 `01-intro-to-ai-agents/code_samples/`)

3. **Open and run notebooks:**
   - `*-python-agent-framework.ipynb` - 使用 Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - 使用 Microsoft Agent Framework (.NET)

### Working with Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- 需要 Azure 訂閱
- 使用 `AzureAIProjectAgentProvider` 連接 Agent Service V2（代理可在 Foundry 入口網站查看）
- 具備生產就緒的內建監控能力
- 檔案名稱格式：`*-python-agent-framework.ipynb`

## Testing Instructions

這是一個教育儲存庫，內含示例程式碼，而非帶有自動化測試的生產程式碼。驗證您的設定與修改方式如下：

### Manual Testing

1. **Test Python environment:**
   ```bash
   python --version  # 應該係3.12或以上
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook execution:**
   ```bash
   # 將筆記本轉換為腳本並運行（測試匯入）
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verify environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Running Individual Notebooks

在 Jupyter 中打開筆記本並依序執行單元格。每本筆記本皆獨立且包含：
- 匯入敘述
- 設定載入
- 代理範例實作
- Markdown 單元中的預期輸出

## Code Style

### Python Conventions

- **Python 版本**：3.12+
- **程式碼風格**：遵循標準 Python PEP 8 慣例
- **筆記本**：使用清晰的 Markdown 單元解釋概念
- **匯入**：分組標準庫、第三方、在地匯入

### Jupyter Notebook Conventions

- 在程式碼單元前包含描述性 Markdown 單元
- 筆記本內加入輸出範本以供參考
- 使用與課程概念相符的清楚變數名稱
- 保持執行順序線性（第一單元 → 第二單元 → 第三單元...）

### File Organization

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Build and Deployment

### Building Documentation

本儲存庫使用 Markdown 撰寫文件：
- 各課程資料夾中的 README.md 檔案
- 儲存庫根目錄的主要 README.md
- 自動翻譯系統透過 GitHub Actions 執行

### CI/CD Pipeline

位於 `.github/workflows/`：

1. **co-op-translator.yml** - 自動翻譯至 50+ 種語言
2. **welcome-issue.yml** - 歡迎新議題創建者
3. **welcome-pr.yml** - 歡迎新的拉取請求貢獻者

### Deployment

這是教育儲存庫，無部署流程。使用者可：
1. Fork 或 clone 儲存庫
2. 本地或 GitHub Codespaces 執行筆記本
3. 透過修改與實驗範例學習

## Pull Request Guidelines

### Before Submitting

1. **Test your changes:**
   - 完整執行受影響筆記本
   - 確認單元格皆無錯誤
   - 確保輸出結果合適

2. **Documentation updates:**
   - 新增概念時更新 README.md
   - 複雜程式碼於筆記本中加入註解
   - 確保 Markdown 單元說明意圖

3. **File changes:**
   - 避免提交 `.env` 檔（改用 `.env.example`）
   - 不提交 `venv/` 或 `__pycache__/` 目錄
   - 當筆記本輸出用於示範時保留輸出
   - 清除暫存檔與備份筆記本 (`*-backup.ipynb`)

### PR Title Format

使用描述性標題：
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Required Checks

- 筆記本須無執行錯誤
- README 檔案須清晰且正確
- 遵循儲存庫內現有程式碼風格
- 與其他課程保持一致性

## Additional Notes

### Common Gotchas

1. **Python 版本不符：**
   - 確保使用 Python 3.12+
   - 有些套件於舊版不支援
   - 使用 `python3 -m venv` 明確指定 Python 版本

2. **環境變數：**
   - 請務必從 `.env.example` 建立 `.env`
   - 不要提交 `.env` 檔（已列入 `.gitignore`）
   - GitHub token 需具適當權限

3. **套件衝突：**
   - 建議使用全新虛擬環境
   - 從 `requirements.txt` 安裝套件，不建議分別安裝
   - 部分筆記本可能需額外套件，會在 Markdown 中說明

4. **Azure 服務：**
   - Azure AI 服務需有效訂閱
   - 部分功能僅限特定區域
   - GitHub Models 有免費層次限制

### Learning Path

建議依課程順序學習：
1. **00-course-setup** - 環境設定入門
2. **01-intro-to-ai-agents** - 理解 AI 代理基礎
3. **02-explore-agentic-frameworks** - 探索不同框架
4. **03-agentic-design-patterns** - 核心設計模式
5. 依序完成後續編號課程

### Framework Selection

根據目標選擇框架：
- **全部課程**：Microsoft Agent Framework (MAF) 搭配 `AzureAIProjectAgentProvider`
- **代理在伺服器端註冊**於 Azure AI Foundry Agent Service V2，並可於 Foundry 入口網站查看

### Getting Help

- 加入 [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- 閱讀各課程 README 文件以取得具體指引
- 參考主 README.md [./README.md] 了解課程概況
- 參看 [Course Setup](./00-course-setup/README.md) 了解詳細設置說明

### Contributing

這是一個開放教育專案，歡迎貢獻：
- 改進程式碼範例
- 修正錯字或錯誤
- 新增說明註解
- 建議新課程主題
- 翻譯更多語言

請見 [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) 查詢當前需求。

## Project-Specific Context

### Multi-Language Support

本儲存庫使用自動翻譯系統：
- 支援 50+ 種語言
- 翻譯檔置於 `/translations/<lang-code>/` 目錄
- GitHub Actions 工作流程管理翻譯更新
- 來源文件為儲存庫根目錄的英文檔案

### Lesson Structure

每堂課遵循固定模式：
1. 含連結的影片縮圖
2. 書面課程內容（README.md）
3. 多框架的程式碼範例
4. 學習目標與先決條件
5. 附加學習資源連結

### Code Sample Naming

格式：`<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 第1課，MAF Python
- `14-sequential.ipynb` - 第14課，MAF 進階模式

### Special Directories

- `translated_images/` - 翻譯後的本地化圖片
- `images/` - 原始英語圖片
- `.devcontainer/` - VS Code 開發容器設定
- `.github/` - GitHub Actions 工作流程與範本

### Dependencies

`requirements.txt` 主要套件：
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - 代理間通訊協定支援
- `azure-ai-inference`, `azure-ai-projects` - Azure AI 服務
- `azure-identity` - Azure 身份驗證（AzureCliCredential）
- `azure-search-documents` - Azure AI Search 整合
- `mcp[cli]` - 模型上下文協定支援

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。文件之原文版本應視為權威來源。對於重要資訊，建議尋求專業人類翻譯。我們對因使用此翻譯而引起之任何誤解或誤譯概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->