---
name: testing-course-samples
---
# 測試課程範例

驗證課堂筆記本和程式碼範例是否能夠在實際運行的
Microsoft Foundry / Azure OpenAI 環境中執行。此版本庫附帶一個執行器
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1)，
可無頭方式執行所有 Python 筆記本並列印出 PASS/FAIL 矩陣。

## 什麼時候使用
- 「驗證所有筆記本 / 範例是否與我的 Azure 訂閱相容。」
- 「在升級套件或更換模型後做煙霧測試課程。」
- 「哪些課程仍然通過 / 失敗？」

請<strong>勿</strong>將此用於 AI Smoke Test GitHub Action（該動作驗證<em>已部署</em>
的主機代理 — 請參考 [`tests/README.md`](../../../tests/README.md)）。這個功能
是在本機運行筆記本。

## 前置條件（先檢查）
1. **Python 3.12+** 且安裝課程依賴：`python -m pip install -r requirements.txt`
   以及執行器：`python -m pip install nbconvert ipykernel`。
2. **倉庫根目錄要有 `.env`**（從 [`.env.example`](../../../../../.env.example) 複製）且至少包含：
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry 專案端點
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — 一個未過時的部署（例如 `gpt-5-mini`）
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) 和 `AZURE_OPENAI_DEPLOYMENT`
     給直接呼叫 Azure OpenAI 的課程（例如課程 06、02-azure-openai、14 handoff/human-loop）。
3. 已完成 **`az login`** — 範例以 `AzureCliCredential` 認證（Entra ID，免金鑰）。
4. 確認模型部署存在：
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`。

## 執行驗證
```powershell
# 所有 Python 筆記本（跳過 .NET、.venv、site-packages、翻譯、技能資產）
pwsh scripts/validate-notebooks.ps1

# 單一課程，每個單元格有較長的超時時間
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# 僅列出會執行的內容（不執行）
pwsh scripts/validate-notebooks.ps1 -List

# 明確指定直譯器（如果 PATH 中沒有 `python`，例如 Windows Store 別名）
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
腳本會將執行過的複本、每支筆記本的日誌及 `results.json`
寫入 `$env:TEMP\aiab-nbval`，並以失敗數目作為退出碼。

短暫失敗（共享訂閱的 HTTP 429 限流，偶爾的
`AzureCliCredential` 令牌異常，或逾時）會自動重試
（`-Retries`，預設 2 次，搭配 `-RetryDelaySeconds` 延遲，預設 20 秒）。如果某個
模型部署經常遇到 429，請檢查訂閱的 GlobalStandard
TPM 配額（`az cognitiveservices usage list -l <region>`）——提升單一
部署容量不會有用，因為是<em>整個訂閱</em>配額用盡了。

## 解讀結果
- `PASS` — 筆記本從頭到尾執行完成，無任何儲存格錯誤。
- `FAIL` — 顯示第一個 `*Error` / `*Exception` 行；請開啟輸出目錄中的對應
  `log_*.txt` 查看完整追蹤紀錄。
- 單支筆記本失敗由 `-Timeout`（每儲存格）限制，因此人機交互儲存格當掛起
  時會呈現 `StdinNotImplementedError`，而非無限掛起。

## 需要額外資源的課程（若無資源則預期失敗）
| 課堂 | 額外需求 |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search（`AZURE_SEARCH_SERVICE_ENDPOINT`、金鑰）— 有記憶體內備用方案 |
| 11 MCP / GitHub | GitHub MCP 伺服器加 PAT |
| 13 memory (cognee) | 已設定具有模型供應商的 `cognee` |
| 15 browser-use | 安裝 Playwright 瀏覽器（`playwright install`）＋ `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local 運行環境＋已下載的 Qwen 模型（本機裝置，無雲端） |
| `*-dotnet-*` 筆記本 | .NET Interactive kernel（預設排除，使用 `-IncludeDotnet`） |

## 回報結果
彙整為按課堂分組的 PASS/FAIL 表格。將真正的回歸問題
（需修正的程式碼或配置錯誤）與環境缺項（缺少 Search/Foundry Local/PAT）分開，
並為每個實際失敗引用其失敗的 `log_*.txt`。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->