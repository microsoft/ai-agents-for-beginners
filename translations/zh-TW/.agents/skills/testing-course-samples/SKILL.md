---
name: testing-course-samples
---
# 測試課程範例

驗證課程筆記本和程式範例是否能在即時的
Microsoft Foundry / Azure OpenAI 環境中執行。此儲存庫提供一個運行器，位於
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1)，
它會無頭方式執行每個 Python 筆記本並印出通過／失敗矩陣。

## 何時使用
- 「驗證所有筆記本／範例是否與我的 Azure 訂閱相容。」
- 「升級套件或更改模型後，對課程進行煙霧測試。」
- 「哪些課程仍然通過／失敗？」

<strong>不要</strong> 將此用於 AI 煙霧測試 GitHub Action（此測試驗證<em>已部署</em>的
宿主代理 — 請參考[`tests/README.md`](../../../tests/README.md)）。此技能
是在本地執行筆記本。

## 先決條件（請先確認）
1. **Python 3.12+** 且安裝課程相依套件：`python -m pip install -r requirements.txt`
   以及執行器套件：`python -m pip install nbconvert ipykernel`。
2. **在儲存庫根目錄有 `.env`**（從 [`.env.example`](../../../../../.env.example) 複製），且至少包含：
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry 專案端點
     （`https://<account>.services.ai.azure.com/api/projects/<project>`）
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — 非棄用部署（例如 `gpt-5-mini`）
   - `AZURE_OPENAI_ENDPOINT`（`https://<account>.openai.azure.com`）與 `AZURE_OPENAI_DEPLOYMENT`
     用於直接呼叫 Azure OpenAI 的課程（課程 06、02-azure-openai、14 handoff/human-loop）。
3. **完成 `az login`** — 範例以 `AzureCliCredential` 驗證身份（Entra ID，無金鑰）。
4. 驗證模型部署存在：
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`。

## 執行驗證
```powershell
# All Python notebooks (skips .NET, .venv, site-packages, translations, skill assets)
pwsh scripts/validate-notebooks.ps1

# A single lesson, with a longer per-cell timeout
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Just list what would run (no execution)
pwsh scripts/validate-notebooks.ps1 -List

# Explicit interpreter (if `python` is not on PATH, e.g. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
此腳本會寫出執行後的複本、每筆記本的日誌，及 `results.json` 於
`$env:TEMP\aiab-nbval`，並以失敗數量作為退出碼。

短暫失敗（共用訂閱 HTTP 429 限流、偶發的
`AzureCliCredential` 令牌異常，或逾時）會自動重新嘗試
（`-Retries`，預設 2 次，搭配 `-RetryDelaySeconds` 回溯，預設 20 秒）。若
模型部署經常出現 429，請檢查訂閱的 GlobalStandard
TPM 配額（`az cognitiveservices usage list -l <region>`）— 單一部署容量增加並無助於訂閱<em>整體</em>配額耗盡的情況。


## 解讀結果
- `PASS` — 筆記本已全程執行且無單元錯誤。
- `FAIL` — 顯示第一條 `*Error` / `*Exception` 線；打開輸出目錄中的
  `log_*.txt` 以查看完整追蹤。
- 單一筆記本失敗受 `-Timeout`（每個單元）限制，因此卡住的人機互動單元
  會表現為 `StdinNotImplementedError` 而不是卡住。

## 需要額外資源的課程（預期在沒有資源時會失敗）
| 課程 | 額外需求 |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`，金鑰) — 具備記憶體中備援路徑 |
| 11 MCP / GitHub | GitHub MCP 伺服器 + PAT |
| 13 memory (cognee) | 已配置模型提供者的 `cognee` |
| 15 browser-use | 已安裝 Playwright 瀏覽器 (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local 執行環境 + 下載的 Qwen 模型（本地設備，無雲端） |
| `*-dotnet-*` 筆記本 | .NET Interactive 核心（預設排除；使用 `-IncludeDotnet` 啟用） |

## 回報
以課程群組匯總為 PASS/FAIL 表格。將真正的回歸（代碼/配置錯誤需修復）
與環境缺口（缺少 Search/Foundry Local/PAT）分開，並針對每個真實失敗
引用失敗的 `log_*.txt`。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->