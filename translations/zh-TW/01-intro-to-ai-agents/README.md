[![Intro to AI Agents](../../../translated_images/zh-TW/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(點擊上方圖片觀看本課程影片)_

# AI Agents 介紹與代理人使用案例

歡迎來到 **AI Agents 新手入門** 課程！這門課程提供你基礎知識與實際可用的程式碼，讓你從頭開始打造 AI Agents。

歡迎加入 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord 社群</a> 跟其他學習者和 AI 建構者打招呼，他們非常樂意回答你的問題。

在開始動手打造之前，讓我們先確認你真的了解什麼是 AI Agent，以及什麼時候適合使用它。

---

## 介紹

本課程涵蓋：

- AI Agents 是什麼，以及現有的不同類型
- AI Agents 最適合處理哪些任務
- 設計 Agentic 解決方案時會用到的核心建構模組

## 學習目標

本課程結束後，你應該能夠：

- 解釋什麼是 AI Agent，以及它和一般 AI 解決方案的差異
- 知道什麼時候該使用 AI Agent（以及什麼時候不該）
- 草擬一個針對現實問題的基本 Agentic 解決方案設計

---

## 定義 AI Agents 及不同類型的 AI Agents

### 什麼是 AI Agents？

這裡有個簡單的定義方式：

> **AI Agents 是一套讓大型語言模型（LLMs）實際「執行事情」的系統 — 給予它們工具和知識去作用於現實世界，而不僅僅是回應提示。**

我們來稍微拆解一下：

- <strong>系統</strong> — AI Agent 不只是單一東西。它是多個部分協同運作的集合體。每個 Agent 的核心都有三個部分：
  - <strong>環境</strong> — Agent 運作的空間。以旅遊訂票 Agent 為例，就是訂票平台本身。
  - <strong>感測器</strong> — Agent 用來讀取環境當前狀態的方式。我們的旅遊 Agent 可能會檢查飯店空房或機票價格。
  - <strong>執行器</strong> — Agent 採取行動的方式。旅遊 Agent 可能會預訂房間、發送確認信或取消訂單。

![What Are AI Agents?](../../../translated_images/zh-TW/what-are-ai-agents.1ec8c4d548af601a.webp)

- <strong>大型語言模型</strong> — 在 LLM 出現之前就有 Agents，但 LLM 使現代 Agents 功能更強大。它們能理解自然語言、推理上下文，並將模糊的使用者請求轉換成具體行動計劃。

- <strong>執行行動</strong> — 沒有 Agent 系統時，LLM 只能產生文字。加入 Agent 系統後，LLM 可以實際執行步驟——搜尋資料庫、呼叫 API、發送訊息。

- <strong>使用工具</strong> — Agent 可以使用什麼工具取決於（1）它所在環境，以及（2）開發者賦予它的能力。旅遊 Agent 可能能查機票，但不能修改客戶記錄——由你所連結的決定。

- <strong>記憶與知識</strong> — Agents 可以擁有短期記憶（當前對話）和長期記憶（客戶資料庫、過去互動）。旅遊 Agent 可能「記得」你偏好靠窗座位。

---

### 不同類型的 AI Agents

不是所有 Agent 都是相同的。以下以旅遊訂票 Agent 為例，說明主要類型：

| **Agent 類型** | <strong>功能說明</strong> | <strong>旅遊代理人範例</strong> |
|---|---|---|
| <strong>簡單反射型</strong> | 遵循硬編碼規則，沒有記憶、沒有規劃。 | 收到抱怨信 → 直接轉發給客服。就這樣。 |
| <strong>基於模型反射型</strong> | 持有內部世界模型，並隨狀況更新。 | 追蹤歷史機票價格，標記突然昂貴路線。 |
| <strong>目標導向型</strong> | 以目標為導向，逐步決定如何達成。 | 從你的所在地起，預訂完整行程（機票、租車、飯店）。 |
| <strong>效用導向型</strong> | 不只找到「一個」解法，還會衡量得失找到「最佳」解法。 | 在成本與便利間取得平衡，找到最符合偏好的行程。 |
| <strong>學習型</strong> | 從回饋持續改善。 | 根據旅後調查調整未來推薦。 |
| <strong>階層型</strong> | 高階 Agent 將工作拆成子任務，並委派給低階 Agent。 | 「取消行程」請求分拆為：取消機票、取消飯店、取消租車，分別由子 Agent 處理。 |
| **多 Agent 系統 (MAS)** | 多個獨立 Agents 協同（或競爭）作業。 | 協同：不同 Agent 負責飯店、航班、娛樂。競爭：多個 Agent 競爭提供最佳飯店價格。 |

---

## 何時使用 AI Agents

能用 AI Agent 不代表一定要用。以下是 Agents 真的很適合的情況：

![When to use AI Agents?](../../../translated_images/zh-TW/when-to-use-ai-agents.54becb3bed74a479.webp)

- <strong>開放式問題</strong> — 解決步驟無法事先編程，需要 LLM 動態推演路徑。
- <strong>多步驟流程</strong> — 任務需要多次使用工具，非一次查詢或生成即可完成。
- <strong>持續優化</strong> — 希望系統能根據使用者反饋或環境訊號不斷變聰明。

我們將在課程後段的 **打造可信賴的 AI Agents** 單元深度探討何時該用與不該用 AI Agents。

---

## Agentic 解決方案基礎

### Agent 開發

打造 Agent 的第一步是定義 <em>它能做什麼</em> — 也就是它的工具、行動和行為。

本課程使用 **Azure AI Agent Service** 作為主要平台。它支持：

- 開放模型，如 OpenAI、Mistral、Llama
- 來自 Tripadvisor 等供應商的授權資料
- 標準化的 OpenAPI 3.0 工具定義

### Agentic 模式

你用提示（prompts）與 LLM 互動。對 Agents 來說，不可能每次都手動撰寫提示——Agent 需跨多步驟採取行動。這時候就用到 **Agentic Patterns**，就是可重複使用的策略，以更可擴展、可靠的方式提示和協調 LLM。

本課程架構以最常見且實用的 Agentic 模式為基礎。

### Agentic 框架

Agentic Frameworks 給開發者現成範本、工具與基礎建設，方便搭建 Agents。它們讓你更容易：

- 連接工具和能力
- 監控 Agent 在做什麼（出錯時便於除錯）
- 多個 Agent 間協作

本課程聚焦在用於生產環境的 **Microsoft Agent Framework (MAF)**。

---

## 程式碼範例

準備好實作看看了嗎？以下是本課程的範例程式碼：

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## 有問題嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，連接其他學習者，參加線上答疑，並由社群回答你的 AI Agent 問題。

---

## 前一課

[課程設置](../00-course-setup/README.md)

## 下一課

[探索 Agentic 框架](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始母語文件應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。對於因使用本翻譯而產生的任何誤解或誤釋，本公司不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->