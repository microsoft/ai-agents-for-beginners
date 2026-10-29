# 代理煙霧測試

此資料夾包含你在課程中建立的代理的<strong>煙霧測試目錄</strong>。
煙霧測試是一種廉價、快速的檢查，用於驗證<strong>部署於 Microsoft Foundry 的託管代理</strong>
是否可連接、是否有回應，並且是否符合其最基本的提示
預期。它是第一道關卡——而非你在[課程 10](../10-ai-agents-production/README.md)和
[課程 16](../16-deploying-scalable-agents/README.md)中學到的完整評估
流程的替代方案。

這些目錄由 [AI 煙霧測試](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action 透過 [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
工作流程使用。

## 如何執行

1. <strong>將課程的代理部署</strong> 至 Microsoft Foundry 作為託管代理（參見
   課程 16 的部署工作流程）。記下<strong>代理名稱</strong>和你的
   **Foundry 專案端點**。
2. 在此倉庫新增以下祕密（設定 → 祕密與變數 → 工作流程）：
   `AZURE_CLIENT_ID`、`AZURE_TENANT_ID`、`AZURE_SUBSCRIPTION_ID`。聯邦
   身份需擁有<strong>Foundry 專案範圍</strong>的<strong>Azure AI 使用者角色</strong>。
3. 在<strong>工作流程</strong>分頁中，執行<strong>煙霧測試託管代理</strong>，並選擇
   對應課程的 `tests_file`，然後提供相符的 `agent_name` 與
   `project_endpoint`。

## 目錄 → 課程 → 代理名稱

| 目錄 | 課程 | 部署代理為 |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – AI 代理入門](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – 工具使用](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – 代理式 RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – 部署可擴展代理](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## 哪些課程包含煙霧測試？

煙霧測試適用於你<strong>部署代理</strong>且其文字回覆可對已知內容進行斷言的課程。純概念性、
僅本地執行，或產出非決定性創意結果的課程會被刻意排除：


  Foundry Local 執行，且<strong>不</strong>暴露 Foundry 回應端點，因此此
  動作不適用。可透過本地執行筆記本來驗證。
- 設計模式與理論課程（02、03、06、07、09、12）不提供任何
  可部署的代理用於煙霧測試。




每個目錄都是一個頂層具有 `tests` 陣列的 JSON 文件。每個條目會 POST
一個提示並對回覆進行斷言：

| 欄位 | 含義 |
|-------|---------|
| `id` | 在日誌中列印的唯一步驟標識符。 |
| `description` | 人類可讀的目的。 |
| `prompt` | 發送給代理的訊息。 |
| `assertions.status` | 預期的 HTTP 狀態（預設為 200）。 |
| `assertions.contains_any` | 如果回覆包含這些子字串中的任意一個即通過。 |
| `assertions.contains_all` | 如果回覆包含每個子字串即通過。 |
| `assertions.contains_none` | 如果回覆不包含這些子字串則通過。 |
| `save_response_id_as` | 儲存回覆 ID 以用於稍後的多輪步驟。 |
| `use_previous_response_id` | 將此回合訊息鏈接到已儲存的回覆 ID 發送。 |

斷言是大小寫不敏感的子字串檢查。請參閱
[動作文件](https://github.com/marketplace/actions/ai-smoke-test)了解
完整結構，包括 Foundry 管理的對話資源。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->