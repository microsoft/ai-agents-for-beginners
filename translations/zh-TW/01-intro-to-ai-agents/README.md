[![Intro to AI Agents](../../../translated_images/zh-TW/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(點擊上方圖片觀看本課程影片)_

# AI 代理人與代理人使用案例簡介

歡迎來到 **AI 代理人初學者** 課程！本課程將提供您基礎知識和實際可運作的程式碼，讓您能從零開始構建 AI 代理人。

歡迎加入 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord 社群</a>，裡面聚集了許多學習者與 AI 建置者，樂於解答各種問題。

在開始動手打造之前，讓我們先確定實際了解 AI 代理人是什麼，什麼時候使用代理人才合理。

---

## 簡介

本課程內容涵蓋：

- 什麼是 AI 代理人，以及不同種類的代理人
- AI 代理人適合執行哪種任務
- 設計代理人式解決方案時的核心構成要素

## 學習目標

完成本課程後，您應該能夠：

- 解釋 AI 代理人是什麼以及它與一般 AI 解決方案的不同之處
- 知道何時該尋求 AI 代理人（以及何時不該）
- 草擬針對真實問題的基本代理人式解決方案設計

---

## 定義 AI 代理人與 AI 代理人類型

### 什麼是 AI 代理人？

這裡有個簡單的理解方式：

> **AI 代理人是讓大型語言模型（LLM）真正「做事」的系統——透過給予它們工具與知識，對世界採取行動，而非單純回應提示。**

讓我們來詳細解釋：

- <strong>系統</strong> — AI 代理人不只是單一事物，它是多個部分協同運作的集合體。每個代理人核心包含三個元件：
  - <strong>環境</strong> — 代理人工作的空間。以旅遊訂票代理人為例，這裡的環境即為訂票平台本身。
  - <strong>感測器</strong> — 代理人讀取環境當前狀態的方式。旅遊代理人可能查看飯店的可訂房間數或機票價格。
  - <strong>驅動器</strong> — 代理人採取行動的方法。旅遊代理人可能會訂房、寄送確認信或取消預約。

![What Are AI Agents?](../../../translated_images/zh-TW/what-are-ai-agents.1ec8c4d548af601a.webp)

- <strong>大型語言模型</strong> — 代理人在 LLM 出現之前就有了，但 LLM 是現代代理人強大的關鍵。它們能理解自然語言、推理上下文，並把模糊的使用者請求轉化為具體行動計畫。

- <strong>執行動作</strong> — 沒有代理人系統時，LLM 只會產生文字；有了代理人系統，LLM 可以實際執行步驟——搜索資料庫、呼叫 API、發送訊息。

- <strong>工具存取</strong> — 代理人能用哪些工具取決於（1）它運行的環境，和（2）開發者給它的工具。旅遊代理人可以查機票，但不能修改客戶紀錄——看您接上什麼服務。

- <strong>記憶與知識</strong> — 代理人可以擁有短期記憶（當前對話內容）和長期記憶（客戶資料庫、過去互動紀錄）。旅遊代理人可能「記得」您偏好靠窗座位。

---

### 不同類型的 AI 代理人

並非所有代理人都是同一種架構。以旅遊訂票代理人為例，以下是主要種類說明：

| <strong>代理人類型</strong> | <strong>功能說明</strong> | <strong>旅遊代理人例子</strong> |
|---|---|---|
| <strong>簡單反射代理人</strong> | 遵循硬編碼規則，無記憶、無規劃。 | 看到投訴郵件 → 轉交客服，就這樣。 |
| <strong>基於模型的反射代理人</strong> | 保持對世界內部模型，隨情況更新。 | 追蹤歷史機票價格，發現路線價格忽然暴漲。 |
| <strong>目標導向代理人</strong> | 有目標，逐步找方法達成。 | 從您目前位置訂完整旅行（機票、租車、飯店），帶您到目的地。 |
| <strong>效用導向代理人</strong> | 不只找<em>一個</em>解決方案，而是找<em>最佳</em>方案，權衡取捨。 | 平衡價格與便利性，找到最符合偏好的行程。 |
| <strong>學習型代理人</strong> | 透過回饋持續學習提升。 | 根據旅程結束後調查結果調整未來推薦。 |
| <strong>階層式代理人</strong> | 高層代理人拆解任務，分配給低層代理人。 | 「取消行程」請求拆成：取消機票、取消飯店、取消租車，各自由子代理人處理。 |
| **多代理人系統 (MAS)** | 多個獨立代理人合作（或競爭）。 | 合作模式：分別處理飯店、機票、娛樂；競爭模式：多代理人競價飯店房間。 |

---

## 何時使用 AI 代理人

能用 AI 代理人不代表隨時都該用。以下是代理人最適合發揮的情境：

![When to use AI Agents?](../../../translated_images/zh-TW/when-to-use-ai-agents.54becb3bed74a479.webp)

- <strong>開放式問題</strong> — 問題的解決步驟無法事先寫死，需 LLM 動態規劃路徑。
- <strong>多步驟流程</strong> — 任務需跨多輪使用工具，不是單次查詢或生成。
- <strong>持續優化</strong> — 想讓系統根據用戶回饋或環境訊號逐漸變聰明。

課程中後段的【建構可信賴 AI 代理人】單元會更深入探討何時（與何時不該）使用 AI 代理人。

---

## 代理人式解決方案基礎

### 代理人開發

開始建置代理人時，先定義它能做什麼——包含工具、行動與行為模式。

本課程使用 **Azure AI Agent Service** 作為主要平台，支援：

- 來自 OpenAI、Mistral、Meta (Llama) 等提供者的模型
- 來自 Tripadvisor 等供應商的授權資料
- 標準化 OpenAPI 3.0 工具定義

### 代理人模式

您和 LLM 之間透過提示 (prompts) 溝通。代理人不可能完全手寫每個提示，他們必須跨多步驟行動，此時用到 <strong>代理人模式</strong>。它們是提示及指揮 LLM 更可擴展、穩定的策略。

本課程架構就是以最常見、最實用的代理人模式為核心設計。

### 代理人框架

代理人框架為開發者提供現成模板、工具、基礎設施，讓建置代理人更輕鬆。他們能協助：

- 接駁工具與功能
- 觀察代理人動作，及時除錯
- 多代理人協作

本課程重點是使用 **Microsoft Agent Framework (MAF)**，打造可投入產線的代理人。

---

## 程式碼範例

想馬上看範例嗎？以下是本課的程式碼示範：

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## 有問題嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，與其他學習者交流，參加線上答疑，獲社群幫助解決 AI 代理人問題。

---

## 上一課

[課程設定](../00-course-setup/README.md)

## 下一課

[探索代理人框架](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->