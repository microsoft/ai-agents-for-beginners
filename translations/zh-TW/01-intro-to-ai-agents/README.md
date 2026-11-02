[![AI 代理入門](../../../translated_images/zh-TW/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(點擊上方圖片觀看本課影片)_

# AI 代理與代理使用案例介紹

歡迎來到 **AI 代理初學者課程**！本課程將提供您基礎知識與實際運作的程式碼，讓您從零開始建置 AI 代理。

來 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord 社群</a> 打個招呼吧 — 這裡聚集了許多學習者和 AI 開發者，樂意回答您的問題。

在開始建置之前，請先確定您明白什麼是 AI 代理，以及何時適合使用代理。

---

## 簡介

本課程涵蓋內容：

- 什麼是 AI 代理，以及存在的不同類型
- AI 代理最適合處理的任務種類
- 設計代理解決方案時會用到的核心建構塊

## 學習目標

上完本課後，您應該能：

- 解釋什麼是 AI 代理，以及它與一般 AI 解決方案的不同
- 瞭解何時應該使用 AI 代理（以及何時不該使用）
- 草擬出針對真實世界問題的基本代理解決方案設計

---

## 定義 AI 代理與 AI 代理類型

### 什麼是 AI 代理？

這裡有個簡單的理解方式：

> **AI 代理是讓大型語言模型（LLM）真正「做事情」的系統 — 不只是回應提示，而是賦予工具與知識來作用於世界。**

讓我們稍微拆解一下：

- <strong>系統</strong> — AI 代理不是單一東西，而是一組部件協同運作。每個代理核心都有三個組成部分：
  - <strong>環境</strong> — 代理所工作的空間。以旅遊預訂代理為例，就是預訂平台本身。
  - <strong>感應器</strong> — 代理讀取環境狀態的方式。旅遊代理可能會查看飯店可用性或航班價格。
  - <strong>執行器</strong> — 代理採取行動的方式。旅遊代理可能會預訂房間、發送確認信或取消訂房。

![什麼是 AI 代理？](../../../translated_images/zh-TW/what-are-ai-agents.1ec8c4d548af601a.webp)

- <strong>大型語言模型</strong> — 代理早有存在，但大型語言模型讓現代代理變得強大。它們能理解自然語言、推理上下文，並將模糊的用戶請求轉成具體行動計劃。

- <strong>執行動作</strong> — 沒有代理系統時，LLM 只能產生文字；代理系統內，LLM 可以實際執行操作 — 搜尋資料庫、呼叫 API、發送訊息。

- <strong>存取工具</strong> — 代理能用的工具取決於（1）它運行的環境，和（2）開發者授予的工具。旅遊代理可能能查航班，但不能編輯客戶資料 — 全看您如何串接。

- **記憶 + 知識** — 代理可有短期記憶（當前對話）和長期記憶（客戶資料庫、過往互動）。旅遊代理可能「記得」您偏好靠窗座位。

---

### 不同類型的 AI 代理

代理並非都一樣。以下以旅遊預訂代理為例，列出主要類型：

| <strong>代理類型</strong> | <strong>功能說明</strong> | <strong>旅遊代理範例</strong> |
|---|---|---|
| <strong>簡單反射代理</strong> | 遵循硬編碼規則 — 無記憶、無規劃。 | 看見抱怨信 → 轉交客服。就這樣。 |
| <strong>基於模型的反射代理</strong> | 持有並隨變化更新內部世界模型。 | 追蹤過去航班價格並標示突然貴的路線。 |
| <strong>基於目標的代理</strong> | 有明確目標，逐步推敲如何達成。 | 從您目前位置預訂包含航班、車輛、飯店的完整旅程至目的地。 |
| <strong>基於效用的代理</strong> | 不只找到<em>一個</em>解決方案，而是透過權衡取捨找到<em>最佳</em>解。 | 平衡成本與便利性，找到最符合您偏好的旅程。 |
| <strong>學習型代理</strong> | 透過回饋持續變得更好。 | 根據旅後調查調整未來預訂建議。 |
| <strong>分層代理</strong> | 高階代理將工作拆為子任務並交由低階代理執行。 | 「取消行程」請求拆分為：取消航班、取消飯店、取消租車 — 各有子代理負責。 |
| **多代理系統 (MAS)** | 多個獨立代理協同（或競爭）作業。 | 協作：不同代理各管飯店、航班、娛樂。競爭：多代理競爭以最佳價格搶客。 |

---

## 何時使用 AI 代理

可以使用 AI 代理不代表每次都該用。以下是代理真正出色的場合：

![何時使用 AI 代理？](../../../translated_images/zh-TW/when-to-use-ai-agents.54becb3bed74a479.webp)

- <strong>開放式問題</strong> — 解決步驟無法預先程式化時。需要 LLM 動態找路。
- <strong>多步驟流程</strong> — 任務需跨多輪使用工具，而非單一查詢或生成。
- <strong>隨時間改進</strong> — 希望系統基於使用者回饋或環境訊號智慧進化。

關於何時（或不該）使用 AI 代理，我們在後面課程的 **打造可信賴 AI 代理** 章節會有更深討論。

---

## 代理解決方案基礎

### 代理開發

建構代理的第一步是定義其<em>能力</em> — 工具、動作與行為。

本課程使用 **Microsoft Foundry Agent Service** 作為主要平台。它支援：

- 來自 OpenAI、Mistral 與 Meta（Llama）等供應商的模型
- 來自 Tripadvisor 等供應商的授權資料
- 標準化的 OpenAPI 3.0 工具定義

### 代理模式

您透過提示與 LLM 溝通。使用代理時，無法完全手工撰寫每個提示 — 代理需跨多步行動。這時候就用到<strong>代理模式</strong>，它們是提示與協調 LLM 的可重用策略，更有擴展性與可靠性。

本課程圍繞最常用和最實用的代理模式設計。

### 代理框架

代理框架為開發者提供現成的樣板、工具與基礎架構，讓建置代理更簡單，能：

- 串接工具與能力
- 觀察代理行為（並於錯誤時除錯）
- 多代理協作

本課程集中使用 **Microsoft Agent Framework (MAF)** 建置可投產的代理。

---

## 程式碼範例

準備好看實作了嗎？以下為本課程的程式碼範例：

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## 有問題嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，與其他學習者交流、參加開放時間，並由社群幫助解答您的 AI 代理疑問。


---

## 代理的煙霧測試（選用）

在學習如何部署代理的 [Lesson 16](../16-deploying-scalable-agents/README.md) 之後，您可以用現成的檢測目錄 [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) 對本課的 `TravelAgent` 進行快速部署健康檢查。請參考 [`tests/README.md`](../tests/README.md) 了解如何執行。

---

## 上一課

[課程設定](../00-course-setup/README.md)

## 下一課

[探索代理框架](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->