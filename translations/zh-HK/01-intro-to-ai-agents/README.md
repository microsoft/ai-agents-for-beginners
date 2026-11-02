[![Intro to AI Agents](../../../translated_images/zh-HK/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(點擊上方圖片觀看本課程影片)_

# 什麼是 AI 代理人及其使用案例介紹

歡迎來到 **AI 代理人入門** 課程！本課程將提供你基礎知識及實作程式碼，讓你從零開始打造 AI 代理人。

歡迎到 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord 社群</a> 打招呼 — 這裡聚集了許多學習者和 AI 建構者，願意協助回答問題。

在開始建置之前，讓我們先確定什麼是 AI 代理人，以及什麼時候使用才合理。

---

## 介紹

本課程內容包括：

- 什麼是 AI 代理人，以及不同類型
- AI 代理人適合處理哪些任務
- 設計代理人解決方案時會用到的核心構建模組

## 學習目標

本課程結束後，你應該能夠：

- 解釋什麼是 AI 代理人，以及與一般 AI 解決方案的不同
- 知道什麼時候該使用 AI 代理人（和什麼時候不該用）
- 草擬一個針對真實世界問題的基本代理人解決方案設計

---

## AI 代理人定義與類型

### 什麼是 AI 代理人？

這是一個簡單的理解方式：

> **AI 代理人是系統，讓大型語言模型（LLMs）能夠<em>實際執行動作</em> — 通過提供工具和知識去影響世界，而不只是回應輸入提示。**

讓我們稍微拆解說明：

- <strong>系統</strong> — AI 代理人不是單一元件，而是一組協同工作的部分組成。每個代理人的核心包含三個部分：
  - <strong>環境</strong> — 代理人執行工作的空間。例如，旅行代理人就是在訂票平台上工作。
  - <strong>感測器</strong> — 代理人如何讀取當前環境狀態。旅行代理人可能會查看飯店房態或航班價格。
  - <strong>執行器</strong> — 代理人如何採取行動。旅行代理人可能會訂房、發送確認，或取消訂單。

![What Are AI Agents?](../../../translated_images/zh-HK/what-are-ai-agents.1ec8c4d548af601a.webp)

- <strong>大型語言模型</strong> — 代理人在 LLM 出現前就存在，但正是 LLM 讓現代代理人變得如此強大。它們能理解自然語言、推理上下文，並將模糊的用戶需求轉化為具體行動方案。

- <strong>執行動作</strong> — 沒有代理系統，LLM 只是產生文字。代理系統中，LLM 能夠<em>執行</em>步驟 — 搜尋資料庫、呼叫 API、發送訊息。

- <strong>存取工具</strong> — 代理人可用的工具取決於 (1) 執行環境，以及 (2) 開發者賦予它的權限。旅行代理人可能能查詢航班，卻無法修改客戶資料 — 取決於你的設計。

- <strong>記憶與知識</strong> — 代理人可具備短期記憶（當前對話）與長期記憶（客戶資料庫、過往互動）。旅行代理人可能會「記住」你偏好靠窗座位。

---

### 不同類型的 AI 代理人

代理人種類不盡相同。以下以旅行代理人為例，描述主要類型：

| <strong>代理人類型</strong> | <strong>功能說明</strong> | <strong>旅行代理人範例</strong> |
|---|---|---|
| <strong>簡單反射代理人</strong> | 遵循硬編碼規則 — 無記憶，無規劃。 | 接收到投訴信 → 轉交客服。僅此而已。 |
| <strong>基於模型的反射代理人</strong> | 維持內部世界模型並隨變化更新。 | 追蹤歷史航班價格，標示價格飆升路線。 |
| <strong>目標導向代理人</strong> | 有明確目標，逐步規劃達成方案。 | 預訂全程行程（航班、租車、飯店），從你所在位置到目的地。 |
| <strong>效用導向代理人</strong> | 不只是找到<em>一</em>個方案，而是尋找<em>最佳</em>方案，權衡取捨。 | 平衡花費與便利性，選出最符合偏好的旅程。 |
| <strong>學習型代理人</strong> | 從回饋中持續學習，逐步進步。 | 根據旅後問卷調整未來推薦。 |
| <strong>階層式代理人</strong> | 高階代理人拆分任務，由低階代理人執行子任務。 | 「取消行程」請求拆成：取消航班、取消飯店、取消租車，分別由子代理人處理。 |
| **多代理系統 (MAS)** | 多個獨立代理人合作或競合。 | 合作：分別負責飯店、航班與娛樂。競爭：多個代理人搶訂同間飯店之最佳價格。 |

---

## 何時使用 AI 代理人

你能使用 AI 代理人，不代表每次都應該用。以下是代理人表現出色的情境：

![When to use AI Agents?](../../../translated_images/zh-HK/when-to-use-ai-agents.54becb3bed74a479.webp)

- <strong>開放式問題</strong> — 解決步驟無法預先編程，需要 LLM 動態決策路徑。
- <strong>多步驟流程</strong> — 任務需跨多次互動使用工具，而非單次查詢或產出。
- <strong>持續優化</strong> — 希望系統能根據用戶回饋或環境訊號逐步聰明。

我們稍後在課程的 **打造可信賴 AI 代理人** 章節中，會更深入討論何時（及何時不該）使用 AI 代理人。

---

## 代理人解決方案基礎

### 代理人開發

建立代理人時，首要定義的是它「能做什麼」 — 它的工具、行動與行為。

本課程以 **Microsoft Foundry Agent Service** 為主要平台。它支持：

- 來自 OpenAI、Mistral、Meta (Llama) 等提供者的模型
- 授權資料來源如 Tripadvisor
- 標準化的 OpenAPI 3.0 工具定義

### 代理人模式

你透過提示詞與 LLM 溝通。有了代理人，不可能所有提示詞都有人手打造，代理人需要跨多步執行動作。這時候就用到 <strong>代理人模式</strong>，它們是用於提示與協調 LLM 的可重用策略，讓整體更具擴展性與穩定性。

本課程架構即圍繞最常見且實用的代理人模式設計。

### 代理人框架

代理人框架為開發者提供現成的範本、工具與架構，方便建置代理人。它們能協助你：

- 連接工具和功能
- 監控代理人行為（及時偵錯）
- 多代理人間的協作

本課程聚焦於用於生產環境的 **Microsoft Agent Framework (MAF)** 。

---

## 範例程式碼

想看實際運作嗎？本課程的程式碼範例如下：

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## 有問題嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者互動，參加線上答疑，並從社群獲得 AI 代理人的解答。


---

## 代理人煙霧測試（選用）

在你學會於 [Lesson 16](../16-deploying-scalable-agents/README.md) 部署代理人後，可以使用現成目錄 [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) 快速做這課程「TravelAgent」的部署後健康檢查。詳情請參考 [`tests/README.md`](../tests/README.md) 說明。

---

## 上一課

[課程設定](../00-course-setup/README.md)

## 下一課

[探索代理人框架](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->