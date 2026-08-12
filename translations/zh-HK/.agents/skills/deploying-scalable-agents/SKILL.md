---
name: deploying-scalable-agents
license: MIT
---
# 使用 Microsoft Foundry 部署可擴展代理

> [課程 16 – 部署可擴展代理](../../../16-deploying-scalable-agents/README.md) 的輔助技能。
> 用於協助學習者將代理從原型移動到可擴展、可觀察的
> 生產部署。所有建議均基於課程內容和
> 可執行的筆記本；不要憑空捏造 Foundry API。

## 觸發條件

當學習者希望：
- 將代理部署到 Microsoft Foundry 作為<strong>託管代理</strong>，並使其具備版本控制／可觀察性。
- 在<strong>用戶端主機、託管代理和代理工作流</strong>部署模式間做選擇。
- 添加<strong>模型路由</strong>、<strong>響應緩存</strong>或<strong>有界併發性</strong>來控制延遲和成本。
- 添加<strong>評估門檻</strong>，防止不良代理版本上線。
- 為高風險操作添加<strong>人工審核批准</strong>步驟。
- 使用<strong>OpenTelemetry</strong>追踪為生產環境儀表化代理。
- 部署後以<strong>煙霧測試</strong>快速檢驗代理。

## 核心心智模型

生產代理主要是模型（約 80%）<em>之外的</em>運行骨架，
而不是模型本身。將每個建議對應到以下某個關注點：

| 關注點 | 原型 → 生產 |
|---------|------------------------|
| 託管 | 筆記本 → 版本化託管服務 |
| 身份 | 你的 `az login` → 管理身份 + 範圍 RBAC |
| 狀態 | 內存中 → 外部線程/記憶體存儲 |
| 錯誤 | 堆疊追蹤 → 重試、回退、警報 |
| 成本 | "幾分錢" → 追蹤、路由、緩存、預算控制 |
| 質量 | 目測 → 自動化評估門檻 |
| 信任 | 你批准 → 政策 + 人工審核 |

## 部署模式（選一或組合使用）

1. <strong>用戶端主機</strong> — 推理迴圈運行於你的進程中。最大控制權；你掌握擴展與狀態。
2. **託管代理 (Foundry Agent Service)** — Foundry 托管推理迴圈，存儲線程，執行 RBAC/內容安全，並在入口網站顯示代理。控制較少，運維面積大幅縮減。
3. <strong>代理工作流</strong> — 多個代理／工具組成有分支、批准節點及持久檢查點的工作圖。

## 生命周期（代理部署迴圈）

`建立 → 版本化 → 評估（門檻）→ 託管部署 → 在線觀察 → 收集失敗 → 重複。`
**離線評估是一個門檻，不是事後補充** — 未達標版本不會上線，
在線可觀察性會將實際失敗反饋
回離線測試集。

## 擴展與成本調節桿（優先順序）

1. <strong>模型尺寸適配</strong> — 使用通過評估門檻的最小模型。
2. <strong>按複雜度路由</strong> — 簡單請求用小而快模型，複雜推理用大模型（DIY 分類器或 Foundry 模型路由器）。
3. <strong>緩存</strong> — 服務近似重複請求，無需模型調用。
4. **無狀態設計 + 有界併發** — 狀態外部化；帶回退的重試。

## 主要範例可複製

從筆記本指引學習者觀看
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- <strong>請求處理器</strong>：緩存 → 按複雜度路由 → 追踪 span → 執行 → 緩存。
- <strong>評估門檻</strong>：對離線測試集打分；返回 `pass_rate >= threshold`，僅在符合時部署。
- <strong>人工批准</strong>：`@tool(approval_mode="always_require")` 用於大額退款等操作。
- <strong>追踪</strong>：用 `tracer.start_as_current_span(...)` 包裹每個請求，並設置屬性如 `routed.model`、`customer.id`。

## 已部署代理的煙霧測試

部署後，確認端點確實有回應（綠色部署仍可能
沒有響應）。通過 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
行動，使用 [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
和 [`tests/`](../../../tests/README.md) 中的目錄。執行者將每條
提示 POST 到 `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
並檢查回覆文字。身份需要在
Foundry 專案範圍內擁有 **Azure AI User** 角色；令牌受眾必須是 `https://ai.azure.com/`。

分層關卡：<strong>煙霧測試</strong>（可到達、有回應，每次部署）→ <strong>離線評估</strong>（達標才可發布，升級前）→ <strong>在線評估</strong>（持續追蹤運行情況）。



## 企業安全控管

- **RBAC**：給每個託管代理分配一個具最低權限的管理身份。
- **生產中的 MCP**：將每台 MCP 伺服器視為不受信任邊界 — 鎖定版本、範圍身份、驗證輸出、限速，絕不曝光機密。

## 助手的保護措施

- 優先使用課程中通用的 `FoundryChatClient(...)` + `provider.as_agent(...)` 模式。
- 不要承諾未驗證的即時 Azure 結果；建議使用煙霧測試工作流確認部署。
- 評估與成本建議需綁定：評估設定品質底線，路由／緩存則將成本限制於該底線附近。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->