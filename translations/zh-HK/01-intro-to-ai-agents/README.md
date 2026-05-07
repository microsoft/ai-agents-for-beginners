[![Intro to AI Agents](../../../translated_images/zh-HK/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(點擊上方圖片觀看本課視頻)_

# AI Agents 及代理用例介紹

歡迎來到 **AI Agents for Beginners** 課程！本課程會為你提供基礎知識 — 以及實際可用的代碼 — 從零開始構建 AI Agents。

來 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord 社區</a> 打個招呼吧 — 這裡聚集著許多學習者和 AI 建造者，樂意解答問題。

在開始構建之前，先確保我們實際了解什麼是 AI Agent，以及在什麼情況下使用它才合理。

---

## 介紹

本課涵蓋內容：

- 什麼是 AI Agents，以及它們的不同類型
- AI Agents 最適合用來處理哪些類型的任務
- 設計 Agentic 解決方案時會使用的核心構建模塊

## 學習目標

完成本課後，你應該能夠：

- 解釋什麼是 AI Agent，以及它與普通 AI 解決方案的區別
- 知道何時該使用 AI Agent（以及何時不該）
- 為真實世界問題草擬一個基本的 Agentic 解決方案設計

---

## 定義 AI Agents 及 AI Agents 的類型

### 什麼是 AI Agents？

這裡有一個簡單的理解方式：

> **AI Agents 是讓大型語言模型（LLMs）真正能「做事」的系統 —— 給它們工具和知識來影響世界，而不只是回應提示。**

我們詳細說說這點：

- <strong>系統</strong> — AI Agent 不只是單一個體。它是多個部分協同運作的集合。每個 Agent 核心都有三個部分：
  - <strong>環境</strong> — Agent 工作的空間。對旅遊預訂代理來說，就是預訂平台本身。
  - <strong>感知元件</strong> — Agent 如何讀取環境當前狀態。我們的旅遊代理可能會檢查酒店房態或機票價格。
  - <strong>執行元件</strong> — Agent 如何採取行動。旅遊代理可能會預訂房間、發送確認或取消預訂。

![What Are AI Agents?](../../../translated_images/zh-HK/what-are-ai-agents.1ec8c4d548af601a.webp)

- <strong>大型語言模型</strong> — Agent 在 LLM 出現之前就存在，但現代的 Agent 因為 LLM 變得強大。它們能理解自然語言，推理上下文，以及把模糊的用戶請求轉化為具體行動計劃。

- <strong>執行動作</strong> — 沒有代理系統，LLM 只是生成文字。在代理系統內，LLM 可以真正 <em>執行</em> 步驟 —— 搜尋資料庫、調用 API、發送訊息。

- <strong>工具訪問</strong> — Agent 可使用的工具取決於 (1) 它運行的環境，和 (2) 開發者給它配置什麼。旅遊代理可能能搜尋航班，但不能修改顧客資料 —— 全看你怎麼接線。

- **記憶 + 知識** — Agent 可以有短期記憶（當前對話）和長期記憶（顧客資料庫、過往互動）。旅遊代理或許會「記得」你偏好靠窗座位。

---

### 不同類型的 AI Agents

並非所有 Agents 結構相同。以下用旅遊預訂代理作為範例，說明主要類型：

| **Agent 類型** | <strong>功能說明</strong> | <strong>旅遊代理範例</strong> |
|---|---|---|
| <strong>簡單反射代理</strong> | 遵循硬編碼規則 — 無記憶，無規劃。 | 收到投訴郵件 → 轉給客服。完事。 |
| <strong>基於模型的反射代理</strong> | 內部維護世界模型並隨狀態更新。 | 跟蹤歷史機票價格，標記突然變貴路線。 |
| <strong>目標導向代理</strong> | 心中有目標，逐步推演如何達成。 | 預訂完整行程（飛機、車、酒店），從現地出發到目的地。 |
| <strong>效用導向代理</strong> | 不只找到一個解決方案，而是經權衡找到最佳方案。 | 平衡價格與便利性，找出最符合偏好的行程。 |
| <strong>學習代理</strong> | 通過反饋持續學習提升。 | 根據行程後調查結果調整未來推薦。 |
| <strong>層次代理</strong> | 高層代理拆分任務並委派低層代理。 | 「取消行程」分為：取消機票、取消酒店、取消租車，各由子代理處理。 |
| **多代理系統 (MAS)** | 多個獨立代理協同工作（或競爭）。 | 協作型：不同代理分別處理酒店、航班和娛樂。競爭型：多代理競爭以最優惠價格搶訂酒店。 |

---

## 何時使用 AI Agents

能用 AI Agent 不代表一定要用。以下是代理真正大放異彩的情況：

![When to use AI Agents?](../../../translated_images/zh-HK/when-to-use-ai-agents.54becb3bed74a479.webp)

- <strong>開放式問題</strong> — 解決步驟無法事先編程，需讓 LLM 動態推理流程。
- <strong>多步驟流程</strong> — 用工具完成跨多輪的任務，不只是單步查詢或生成。
- <strong>持續優化</strong> — 希望系統能根據用戶反饋或環境信號變得更聰明。

課程後續會在 **建構可信的 AI Agents** 課程深入探討何時該用與不該用。

---

## Agentic 解決方案基礎

### Agent 開發

建立代理前，第一件事是定義 <em>它能做什麼</em> — 它的工具、行為和動作。

本課程主要使用 **Azure AI Agent Service** 平台。它支持：

- 開放模型，如 OpenAI、Mistral 和 Llama
- 來自 Tripadvisor 等供應商的授權資料
- 標準化 OpenAPI 3.0 工具定義

### Agentic 模式

與 LLM 通訊靠提示詞。對 Agent 而言，不能手工打造每個提示 —— 代理需跨多步執行操作。這就是 **Agentic Patterns** 的用武之地。它們是可重用的提示與協調策略，使 LLM 以更可擴展、可靠的形式運作。

本課圍繞最常見且有用的 Agentic 模式結構。

### Agentic 框架

Agentic 框架為開發者提供現成模板、工具和基礎設施，讓構建代理更輕鬆：

- 快速串接工具和能力
- 觀察代理行為（並在錯誤時除錯）
- 多代理間協作

本課聚焦使用 **Microsoft Agent Framework (MAF)** 來建立生產級代理。

---

## 程式碼範例

準備好實戰演練了嗎？本課的程式碼範例如下：

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## 有問題嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，與其他學習者互動、參加答疑時間，並由社群解答你的 AI Agent 問題。

---

## 上一課

[課程設定](../00-course-setup/README.md)

## 下一課

[探索 Agentic 框架](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原文的母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或錯誤詮釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->