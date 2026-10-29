# Agent 煙霧測試

此資料夾保存你在課程中建立的代理程式的<strong>煙霧測試目錄</strong>。
煙霧測試是一種廉價且快速的檢查，確認<strong>已部署的 Microsoft Foundry 托管代理程式</strong>
是否可存取、是否有回應，且是否符合其最基本的提示
預期。這是第一道門檻 — 並非你在 [Lesson 10](../10-ai-agents-production/README.md) 和
[Lesson 16](../16-deploying-scalable-agents/README.md) 中學到的完整評估
流程的替代方案。

這些目錄由 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action 透過 [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
工作流程消費。

## 如何執行

1. <strong>將課程的代理程式</strong> 部署到 Microsoft Foundry 作為托管代理（請參考
   Lesson 16 之部署流程）。記下 <strong>代理名稱</strong> 和你的
   **Foundry 專案端點**。
2. 新增這些儲存庫秘密（Settings → Secrets and variables → Actions）：
   `AZURE_CLIENT_ID`、`AZURE_TENANT_ID`、`AZURE_SUBSCRIPTION_ID`。聯邦
   身分識別需要在 **Foundry 專案範圍** 擁有 **Azure AI 使用者** 角色。
3. 在 **Actions** 分頁中，執行 **Smoke-test hosted agents** 並選擇此
   課程的 `tests_file`，然後提供相應的 `agent_name` 和
   `project_endpoint`。

## 目錄 → 課程 → 代理名稱

| 目錄 | 課程 | 部署為代理 |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – AI 代理入門](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – 工具使用](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – 代理式 RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – 部署可擴展代理](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## 哪些課程有煙霧測試？

煙霧測試適用於你<strong>部署代理</strong>並且其文字回覆可
依照已知內容進行斷言的課程。概念性的課程、僅在本機執行的課程，
或產製非確定性創意輸出的課程則故意排除：

- **Lesson 17（建立本地 AI 代理）** 完全在你的工作站搭配
  Foundry Local 執行，且<strong>不</strong>公開 Foundry Responses 端點，故此
  動作不適用。請透過本機執行 notebook 來驗證。
- 設計模式與理論課程（02、03、06、07、09、12）不提供任何
  可部署成代理供煙霧測試。

## 目錄架構（快速參考）

每個目錄都是一個 JSON 文件，擁有頂層的 `tests` 陣列。每個條目都會 POST
一個提示並針對回覆進行斷言：

| 欄位 | 意義 |
|-------|---------|
| `id` | 日誌中印出的獨特步驟識別碼。 |
| `description` | 人類可讀的目的描述。 |
| `prompt` | 傳送給代理的訊息。 |
| `assertions.status` | 預期的 HTTP 狀態碼（預設 200）。 |
| `assertions.contains_any` | 如果回覆包含其中任一子字串即通過。 |
| `assertions.contains_all` | 如果回覆包含所有子字串則通過。 |
| `assertions.contains_none` | 如果回覆不包含任何這些子字串則通過。 |
| `save_response_id_as` | 儲存回覆 ID 以供後續多回合步驟使用。 |
| `use_previous_response_id` | 將此回合訊息與已儲存的回覆 ID 串接傳送。 |

斷言採用不分大小寫的子字串檢查。完整架構及
Foundry 管理的會話資源說明，請參閱
[action documentation](https://github.com/marketplace/actions/ai-smoke-test)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->