[![Intro to AI Agents](../../../translated_images/zh-HK/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(點擊上方圖片觀看本課程影片)_

# AI 代理人簡介與代理人應用案例

歡迎來到 **AI 代理人初學者** 課程！本課程將提供你基礎知識與實作程式碼，讓你從零開始構建 AI 代理人。

歡迎在 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord 社群</a> 跟我們打聲招呼 — 這裡聚集了許多學習者和 AI 建設者，樂於回答你的問題。

在開始動手之前，我們先搞清楚 AI 代理人到底是什麼，以及什麼時候使用它才合適。

---

## 簡介

本課涵蓋：

- 什麼是 AI 代理人，及其不同類型
- 哪些任務最適合使用 AI 代理人
- 設計 Agentic 解決方案時會使用的核心構成要素

## 學習目標

完成本課後，你應該能夠：

- 解釋什麼是 AI 代理人，以及它和一般 AI 解決方案的差異
- 判斷何時該使用 AI 代理人（以及何時不該）
- 為真實問題初步規劃一個 Agentic 解決方案設計

---

## AI 代理人定義與類型

### 什麼是 AI 代理人？

這裡有個簡單理解方式：

> **AI 代理人是讓大型語言模型 (LLMs) 真正能「做事」的系統 — 透過提供工具和知識，讓它們能影響世界，而不只是回應提示。**

讓我們來拆解一下：

- <strong>系統</strong> — AI 代理人不是單一物件。它是多個部件合作的系統。核心部分都包含三個元素：
  - <strong>環境</strong> — 代理人工作的空間。以旅遊訂票代理人為例，這就是訂票平台本身。
  - <strong>感應器</strong> — 代理人讀取環境當前狀態的方式。我們的旅遊代理人可能會檢查飯店房況或機票價格。
  - <strong>執行器</strong> — 代理人採取行動的方式。旅遊代理人可能會訂房、發送確認信，或取消預約。

![What Are AI Agents?](../../../translated_images/zh-HK/what-are-ai-agents.1ec8c4d548af601a.webp)

- <strong>大型語言模型</strong> — 代理人在 LLM 出現之前就存在，但正是 LLM 讓現代代理人變得強大。它們能理解自然語言，推理情境，並將模糊的用戶需求轉化為具體行動計畫。

- <strong>執行行動</strong> — 沒有代理人系統時，LLM 只能產生文字。置身代理人系統內，LLM 可以真正 <em>執行</em> 步驟 — 搜尋資料庫、呼叫 API、發送訊息。

- <strong>使用工具</strong> — 代理人能用什麼工具取決於 (1) 它運行的環境，以及 (2) 開發者給予的工具。旅遊代理人可能能查航班，但不能編輯顧客資料 — 全看你怎麼連接。

- <strong>記憶與知識</strong> — 代理人可以具備短期記憶（當前對話）和長期記憶（顧客資料庫、過往互動）。旅遊代理人或許會「記得」你偏好靠窗座位。

---

### AI 代理人的不同類型

並非所有代理人都是一樣構建。以下以旅遊訂票代理人為例，解析主要類型：

| <strong>代理人類型</strong> | <strong>功能</strong> | <strong>旅遊代理人範例</strong> |
|---|---|---|
| <strong>簡單反射代理人</strong> | 遵循硬編碼規則 — 無記憶、無規劃。 | 看到客訴郵件 → 轉給客服。就這樣。 |
| <strong>模型導向反射代理人</strong> | 持有內部世界模型並隨變化更新。 | 追蹤歷史機票價格，標示突增路線。 |
| <strong>目標導向代理人</strong> | 有明確目標，逐步計劃達成。 | 從目前地點出發，一步步訂全程機票、租車、飯店。 |
| <strong>效用導向代理人</strong> | 不只找「解」，而是找「最佳解」，評估取捨。 | 平衡花費與便利，找出最符合你偏好的行程。 |
| <strong>學習代理人</strong> | 透過反饋持續優化。 | 根據旅後調查調整未來推薦。 |
| <strong>階層式代理人</strong> | 高階代理人將任務拆分成子任務，交由低階代理人處理。 | 「取消行程」拆解為取消機票、飯店、租車等子任務。 |
| **多代理系統 (MAS)** | 多個獨立代理人合作或競爭。 | 合作型：不同代理人各管飯店、航班、娛樂。競爭型：多代理人搶訂飯店房，以搶低價。 |

---

## 何時使用 AI 代理人

只是因為你 <em>能</em> 用 AI 代理人，並不代表你永遠 <em>該</em> 用。以下是代理人最適合發揮的場景：

![When to use AI Agents?](../../../translated_images/zh-HK/when-to-use-ai-agents.54becb3bed74a479.webp)

- <strong>開放式問題</strong> — 問題的解決步驟不能事先硬編程。需要 LLM 動態判斷路徑。
- <strong>多步驟流程</strong> — 任務需要跨多輪使用工具，而不只是單次查詢或生成。
- <strong>持續改進</strong> — 希望系統能基於用戶反饋或環境訊號變得更聰明。

我們會在課程後續的【建構可信賴的 AI 代理人】單元深入探討何時該用（及何時不該用）AI 代理人。

---

## Agentic 解決方案基礎

### 代理人開發

建置代理人的第一步是定義它能做什麼 — 包含工具、動作與行為。

本課程使用 **Azure AI Agent Service** 作為主要平台。它支援：

- OpenAI、Mistral 與 Meta (Llama) 等模型
- Tripadvisor 等授權資料來源
- 標準化的 OpenAPI 3.0 工具定義

### Agentic 模式

你使用提示與 LLM 溝通。對於代理人而言，不可能每個提示都手工設計 — 代理人需要跨多步驟執行行動。這時，**Agentic 模式** 就派上用場了。它們是促使提示與協調 LLM 更具擴展性且可靠的重用策略。

本課程架構即圍繞最常用且實用的 agentic 模式。

### Agentic 框架

Agentic 框架為開發者提供現成範本、工具與基礎建設，便於建構代理人。它讓你更輕鬆：

- 串接工具及能力
- 觀察代理人行為（出錯時除錯）
- 多代理人間的協作

本課將聚焦於建構可生產環境代理人的 **Microsoft Agent Framework (MAF)**。

---

## 程式碼範例

準備好實際動手了嗎？以下是本課的程式碼範例：

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## 有問題嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，與其他學習者交流、參加開放問答時間，並由社群協助解答你的 AI 代理人問題。

---

## 上一課

[課程設置](../00-course-setup/README.md)

## 下一課

[探索 Agentic 框架](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->