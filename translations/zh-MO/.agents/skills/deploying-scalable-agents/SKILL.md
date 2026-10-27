---
name: deploying-scalable-agents
license: MIT
---
# 使用 Microsoft Foundry 部署可擴展代理

> 與[第16課 – 部署可擴展代理](../../../16-deploying-scalable-agents/README.md)相輔相成的技能。
> 用於幫助學習者將代理從原型階段推進到可擴展且可觀察的
> 生產部署。所有建議均基於課程內容和
> 可運行的筆記本；不要編造 Foundry API。

## 觸發條件

在學習者希望進行以下操作時啟用此技能：
- 將代理部署到 Microsoft Foundry 作為<strong>託管代理</strong>並使其具版本控制/可觀察性。
- 在<strong>客戶端託管、託管代理和代理工作流</strong>部署模式間進行選擇。
- 添加<strong>模型路由</strong>、<strong>響應緩存</strong>或<strong>有界併發</strong>以控制延遲和成本。
- 添加<strong>評估門檻</strong>，以防止錯誤代理版本上線。
- 添加<strong>人工審批</strong>步驟，用於高風險操作。
- 用<strong>OpenTelemetry</strong>追蹤儀器化代理，以實現生產可觀察性。
- <strong>煙霧測試</strong>已部署的代理作為快速的後部署檢查。

## 核心思維模型

生產代理主要是環繞模型（約80%）的運營骨架，
而非模型本身。將每個建議對應到以下關注點之一：

| 關注點 | 原型 → 生產 |
|---------|------------------------|
| 託管 | 筆記本 → 具版本控制的託管服務 |
| 身份 | 你的 `az login` → 託管身份 + 範圍 RBAC |
| 狀態 | 內存中 → 外部線程/記憶體存儲 |
| 故障 | 回溯 → 重試、備援、警報 |
| 成本 |「幾分錢」→ 追蹤、路由、緩存、預算控制 |
| 質量 | 目測 → 自動化評估門檻 |
| 信任 | 你批准 → 政策 + 人工介入審核 |

## 部署模式（選一或組合使用）

1. <strong>客戶端託管</strong> — 推理循環在你的過程中運行。最大控制權；你負責擴展/狀態管理。
2. **託管代理（Foundry Agent Service）** — Foundry 托管循環，存儲線程，執行 RBAC/內容安全限制，在入口網站展示代理。控制較少，運營面積顯著降低。
3. <strong>代理工作流</strong> — 多個代理/工具組成帶有分支、審批節點和持久檢查點的圖形。

## 生命周期（發布代理的循環）

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`。
**離線評估是一道門檻，而非事後考量** — 版本通過門檻才能發佈。
在線可觀察性將真實失敗反饋至離線測試集。


## 擴展與成本槓桿（優先級順序）

1. <strong>調整模型尺寸</strong> — 使用通過評估門檻的最小模型。
2. <strong>按複雜度路由</strong> — 簡單請求使用小/快速模型，複雜推理使用大型模型（DIY 分類器或 Foundry 模型路由器）。
3. <strong>緩存</strong> — 近重複請求不調用模型直接服務。
4. **無狀態設計 + 有界併發** — 狀態外部化；帶退避機制重試。

## 需要複製的關鍵模式

指引用戶到筆記本中的以下內容
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb)：

- <strong>請求處理器</strong>：緩存 → 按複雜度路由 → 追蹤跨度 → 運行 → 緩存。
- <strong>評估門檻</strong>：對離線測試集打分；回傳 `pass_rate >= threshold` 且僅在為真時部署。
- <strong>人工審批</strong>：`@tool(approval_mode="always_require")` 用於大額退款等操作。
- <strong>追蹤</strong>：將每個請求包裹在 `tracer.start_as_current_span(...)` 中，並設置 `routed.model`、`customer.id` 等屬性。

## 煙霧測試已部署代理

部署後，驗證端點確實有回應（部署成功不代表一定有回應）。
使用[AI 煙霧測試](https://github.com/marketplace/actions/ai-smoke-test)
操作，透過 [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
搭配 [`tests/`](../../../tests/README.md) 目錄。執行器將每個提示
POST 到 `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`，
並對回復文本做斷言。身份需在 Foundry 專案範圍擁有 **Azure AI User** 角色；令牌受眾必須是 `https://ai.azure.com/`。






## 企業控管

- **RBAC**：給每個託管代理一個擁有最小權限的託管身份。
- **生產中的 MCP**：將每個 MCP 服務視為不受信任的邊界 — 鎖定版本、限定身份範圍、驗證輸出、限速、不暴露秘密。

## 助手的防護措施

- 優先採用課程中通用的 `FoundryChatClient(...)` + `provider.as_agent(...)` 模式。
- 不承諾未驗證的即時 Azure 結果；建議使用煙霧測試工作流程確認部署。
- 評估與成本建議需掛鈎：評估設定質量底線，路由/緩存將成本控制在該底線附近。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->