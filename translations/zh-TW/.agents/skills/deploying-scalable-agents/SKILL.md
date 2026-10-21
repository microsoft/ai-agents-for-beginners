---
name: deploying-scalable-agents
license: MIT
---
# 使用 Microsoft Foundry 部署可擴充代理

> [第16課 - 部署可擴充代理](../../../16-deploying-scalable-agents/README.md) 的配套技能。
> 用它來協助學習者將代理從原型轉移到可擴展、可觀察的生產部署。
> 將每一項建議都根植於課程內容和可運行筆記本；不得自行創造 Foundry API。


## 觸發條件

當學習者想要：
- 將代理部署到 Microsoft Foundry 作為<strong>託管代理</strong>，並使其版本化/可觀察。
- 在<strong>用戶端託管、託管代理及代理工作流程</strong>部署模式中進行選擇。
- 添加<strong>模型路由</strong>、<strong>回應快取</strong>或<strong>有界並行性</strong>來控制延遲與成本。
- 添加一個<strong>評估門檻</strong>，以防止錯誤的代理版本被部署。
- 添加一個<strong>人機介入的核准</strong>步驟，針對高風險操作。
- 以<strong>OpenTelemetry</strong>追蹤為代理進行生產環境的觀察性儀表。
- 進行<strong>冒煙測試</strong>作為快速的部署後門檻。

## 核心心智模型

生產代理主要是在模型之外的運作框架（約佔80%），
而非模型本身。將每個建議對應到以下關注點之一：

| 關注點 | 原型 → 生產 |
|---------|------------------------|
| 託管 | 筆記本 → 版本化託管服務 |
| 身分識別 | 你的`az login` → 管理身分 + 範圍 RBAC |
| 狀態 | 記憶體內 → 外部線程/記憶體存儲 |
| 失敗 | 堆疊追蹤 → 重試、回退、警示 |
| 成本 | 「幾分錢」→ 被追蹤、路由、快取、預算化 |
| 品質 | 目視檢查 → 自動評估門檻 |
| 信任 | 你核准 → 政策 + 人機介入 |

## 部署模式（選擇一種或組合使用）

1. <strong>用戶端託管</strong> — 推理迴圈在你的程序中運行。最高控制權；你擁有擴展與狀態管理。
2. **託管代理（Foundry Agent Service）** — Foundry 託管迴圈，儲存線程，執行 RBAC/內容安全，並於入口網站展示代理。較少控制權，且大幅降低操作複雜度。
3. <strong>代理工作流程</strong> — 多代理/工具組成帶有分支、核准節點及持久檢查點的圖形化流程。

## 生命週期（部署代理的循環）

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`。
**離線評估是一道門檻，而非事後考量** — 版本不會上線，除非通過此門檻。
在線可觀察性會將真實失敗反饋至離線測試集。


## 規模與成本槓桿（優先排序）

1. <strong>調整模型大小</strong> — 使用通過評估門檻的最小模型。
2. <strong>依複雜度路由</strong> — 簡單請求用小且快速模型，真正推理用大型模型（DIY 分類器或 Foundry 模型路由器）。
3. <strong>快取</strong> — 對近重複的請求不透過模型呼叫直接回應。
4. **無狀態設計 + 有界並發** — 外部化狀態；采用指數退避重試。

## 需復現的關鍵模式

從筆記本指向學習者這些
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb)：

- <strong>請求處理器</strong>：快取 → 按複雜度路由 → 跟蹤 span → 執行 → 快取。
- <strong>評估門檻</strong>：對離線測試集打分；回傳 `pass_rate >= threshold`，且僅於為真時部署。
- <strong>人工審核</strong>：`@tool(approval_mode="always_require")` 用於大額退款等行動。
- <strong>追蹤</strong>：將每次請求包裹在 `tracer.start_as_current_span(...)` 中，並設置屬性如 `routed.model`、`customer.id`。

## 簡易測試已部署代理

部署後，驗證端點確實有回應（綠燈部署仍可能無聲無息）。
透過 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
動作使用 [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
搭配 [`tests/`](../../../tests/README.md) 中的目錄。執行器會將每個
提示以 POST 發送至 `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`，
並對回覆文字斷言。身份需具備 Foundry 專案範圍內的<strong>Azure AI User</strong>角色；Token 受眾必須是 `https://ai.azure.com/`。






## 企業控管

- **RBAC**：為每個託管代理配置最少權限的管理身份。
- **生產中的 MCP**：將所有 MCP 服務器視為不信任邊界 – 固定版本、限制身份範圍、驗證輸出、流控、不外露密鑰。

## 助手的護欄

- 首選課程中採用的標準 `FoundryChatClient(...)` + `provider.as_agent(...)` 模式。
- 不要承諾尚未驗證的 live-Azure 結果；建議使用簡易測試工作流程確認部署。
- 將評估與成本建議綁定：評估設定品質底線，路由／快取將成本維持於該底線附近。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->