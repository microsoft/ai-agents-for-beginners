# 代理煙霧測試

此資料夾保存你在課程中構建的代理的<strong>煙霧測試目錄</strong>。
煙霧測試是一種廉價、快速的檢查，用於確認<strong>已部署的 Microsoft Foundry 托管代理</strong>
是否可達、回應正常，並遵守其最基本的提示
預期。它是一道初步門檻——並非替代你在[第10課](../10-ai-agents-production/README.md)和
[第16課](../16-deploying-scalable-agents/README.md)中學到的完整評估
流程。

這些目錄會被[AI 煙霧測試](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action 通過 [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
工作流程所使用。

## 如何執行

1. <strong>將課程中的代理部署</strong>到 Microsoft Foundry 作為托管代理（請參考
   第16課的部署流程）。記下<strong>代理名稱</strong>及你的
   **Foundry 項目終端點**。
2. 新增這些儲存庫秘密（設定 → 秘密和變數 → Actions）：
   `AZURE_CLIENT_ID`、`AZURE_TENANT_ID`、`AZURE_SUBSCRIPTION_ID`。聯邦
   身份需要在<strong>Foundry 項目範圍</strong>內擁有<strong>Azure AI 使用者</strong>角色。
3. 從 **Actions** 標籤頁，執行 **Smoke-test hosted agents** 並選擇
   課程相符的 `tests_file`，接著提供相應的 `agent_name` 和
   `project_endpoint`。

## 目錄 → 課程 → 代理名稱

| 目錄 | 課程 | 部署代理為 |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – AI 代理簡介](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – 工具使用](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – 代理式 RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – 部署可擴展代理](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## 哪些課程有煙霧測試？

煙霧測試適用於你<strong>部署代理</strong>並且其文字回覆可以
依已知內容進行斷言的課程。概念性課程、僅本地執行的課程，
或產生非決定性創意輸出的課程故意排除在外：

- **第17課（建立本地 AI 代理）** 完全在你的工作站上透過
  Foundry Local 執行，<strong>不</strong>對外公開 Foundry 回應終端點，因此此
  操作不適用。請透過本地執行筆記本來驗證。
- 設計模式與理論課程（02、03、06、07、09、12）不會提供任何
  可部署代理供煙霧測試。

## 目錄架構（快速參考）

每個目錄是一個 JSON 文件，包含頂層的 `tests` 陣列。每個項目會 POST
一個提示並對回覆進行斷言：

| 欄位 | 意義 |
|-------|---------|
| `id` | 唯一步驟識別碼，將印出在日誌中。 |
| `description` | 可供人閱讀的目的說明。 |
| `prompt` | 傳送給代理的訊息。 |
| `assertions.status` | 預期的 HTTP 狀態碼（預設為 200）。 |
| `assertions.contains_any` | 若回覆包含這些子字串中任一即通過。 |
| `assertions.contains_all` | 若回覆包含這些子字串全部即通過。 |
| `assertions.contains_none` | 若回覆不包含這些子字串即通過。 |
| `save_response_id_as` | 儲存回覆 id 以供後續多輪步驟使用。 |
| `use_previous_response_id` | 此輪將鏈結至先前儲存的回覆 id 發送。 |

斷言為不區分大小寫的子字串檢查。詳見
[Action 文件](https://github.com/marketplace/actions/ai-smoke-test)了解
完整架構，包含 Foundry 管理的對話資源。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->