---
name: testing-course-samples
---
# 測試課程範例

驗證課程筆記本和程式碼範例是否可在即時的
Microsoft Foundry / Azure OpenAI 環境中執行。此倉庫包含一個執行器，位置為
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1)，
該執行器會以無頭模式執行所有 Python 筆記本並列印通過/失敗矩陣。

## 何時使用
- 「驗證所有筆記本 / 範例是否可在我的 Azure 訂閱中運行。」
- 「在升級套件或更改模型後，對課程進行煙霧測試。」
- 「哪些課程仍然可通過 / 失敗於實際環境？」

不要用於 AI 煙霧測試 GitHub Action（該 Action 驗證 <em>已部署</em> 的托管代理 — 請參閱 [`tests/README.md`](../../../tests/README.md)）。此工具
在本地端運行筆記本。


## 先決條件（先檢查）
1. **Python 3.12+** 及課程依賴：`python -m pip install -r requirements.txt`
   外加執行環境：`python -m pip install nbconvert ipykernel`。
2. **倉庫根目錄有 `.env`**（複製自 [`.env.example`](../../../../../.env.example)）並至少包含：
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry 專案端點
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — 非棄用的部署名稱（例如 `gpt-5-mini`）
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) 與 `AZURE_OPENAI_DEPLOYMENT`
     用於直接呼叫 Azure OpenAI 的課程（第 06 課、02-azure-openai、14 handoff/human-loop）。
3. 完成 **`az login`** — 範例使用 `AzureCliCredential` 認證（Entra ID、無需金鑰）。
4. 確認模型部署存在：
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`。

## 執行驗證
```powershell
# 所有 Python 筆記本（跳過 .NET、.venv、site-packages、翻譯、技能資產）
pwsh scripts/validate-notebooks.ps1

# 一個單一課程，每個儲存格較長的逾時時間
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# 只列出會執行的內容（不執行）
pwsh scripts/validate-notebooks.ps1 -List

# 明確指定解譯器（如果 `python` 不在 PATH，例如 Windows Store 別名）
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
此腳本將執行結果的複本、筆記本日誌及 `results.json` 寫入
`$env:TEMP\aiab-nbval`，並以失敗數量作為退出碼結束。

短暫失敗（共用訂閱 HTTP 429 限速、偶發的
`AzureCliCredential` 權杖問題或逾時）會自動重試
（`-Retries`，預設 2 次，並使用 `-RetryDelaySeconds` 延遲，預設 20 秒）。若
模型部署經常出現 429，請檢查訂閱之 GlobalStandard
TPM 配額（`az cognitiveservices usage list -l <region>`）— 單一部署增量無助於當 <em>訂閱</em> 配額用盡時。


## 解讀結果
- `PASS` — 筆記本自始至終無任何單元錯誤。
- `FAIL` — 顯示第一條 `*Error` / `*Exception` 訊息；完整錯誤追蹤請開啟輸出目錄中的
  `log_*.txt` 檔案。
- 單一筆記本的失敗受 `-Timeout`（每單元）限制，故掛起的人類互動單元將顯示為 `StdinNotImplementedError` 而非無限掛起。


## 需要額外資源（缺少時預期失敗）的課程
| 課程 | 額外需求 |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`、金鑰) — 有記憶體內備援路徑 |
| 11 MCP / GitHub | GitHub MCP 伺服器 + PAT |
| 13 memory (cognee) | 已配置的 `cognee` 模型提供者 |
| 15 browser-use | 安裝 Playwright 瀏覽器（`playwright install`）+ `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry 本地執行環境 + 下載的 Qwen 模型（本機端，無雲端） |
| `*-dotnet-*` 筆記本 | .NET Interactive 核心（預設排除，使用 `-IncludeDotnet` 引入） |

## 回報結果
以課程為群組匯總成通過/失敗表。將真正的回歸問題
（需修正的程式碼／設定錯誤）與環境缺口（缺少 Search/Foundry Local/PAT）
分開，並對每個真實失敗附上失敗的 `log_*.txt` 檔案。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->