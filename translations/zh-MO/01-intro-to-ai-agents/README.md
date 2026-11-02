[![Intro to AI Agents](../../../translated_images/zh-MO/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(點擊上方圖片觀看本課程視頻)_

# AI代理與代理使用案例介紹

歡迎來到 **AI代理初學者課程**！本課程為您提供基礎知識和實際可運行的代碼，讓您從零開始構建AI代理。

歡迎來 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord社區</a> 打個招呼——這裡匯集了許多學習者和AI開發者，樂意回答您的問題。

在我們正式開始構建之前，先確保您了解什麼是AI代理，以及什麼情況下使用AI代理才合適。

---

## 介紹

本課程涵蓋：

- 什麼是AI代理，以及存在的各種不同類型
- 哪些任務最適合由AI代理完成
- 設計代理解決方案時使用的核心組件

## 學習目標

本課結束後，您應該能夠：

- 解釋什麼是AI代理，以及它與普通AI解決方案的不同之處
- 知道何時該使用AI代理（何時不該）
- 為現實問題草擬一個基本的代理解決方案設計

---

## 定義AI代理及AI代理的類型

### 什麼是AI代理？

這裡有一個簡單的理解方式：

> **AI代理是一套系統，使大型語言模型（LLM）不只是在回應提示，而是能真正“做事”——通過工具和知識來影響世界。**

我們來詳細解釋一下：

- <strong>系統</strong> — AI代理不是單一事物，而是多個部件協同工作組成的系統。每個代理核心都有三個部分：
  - <strong>環境</strong> — 代理運作的空間。如旅遊訂票代理的環境就是訂票平台本身。
  - <strong>感應器</strong> — 代理讀取環境當前狀態的方式。我們的旅遊代理可能會檢查酒店是否有空房或航班價格。
  - <strong>執行器</strong> — 代理行動的方法。旅遊代理可能會訂房、發送確認或取消預訂。

![What Are AI Agents?](../../../translated_images/zh-MO/what-are-ai-agents.1ec8c4d548af601a.webp)

- <strong>大型語言模型</strong> — 代理在LLM出現之前就有，但LLM讓現代代理更強大。它們能理解自然語言、分析上下文，並將模糊的使用者需求轉換成具體行動計劃。

- <strong>執行操作</strong> — 沒有代理系統，LLM只是生成文字。在代理系統中，LLM能實際<em>執行</em>步驟——比如搜尋資料庫、調用API、發送訊息。

- <strong>使用工具</strong> — 代理能使用哪些工具取決於（1）運作的環境和（2）開發者賦予的權限。旅遊代理或許能查航班，但不能修改客戶資料——這取決於您如何配置。

- <strong>記憶與知識</strong> — 代理可以有短期記憶（當前對話）和長期記憶（客戶資料庫、過往互動）。旅遊代理可能“記得”您偏好靠窗座位。

---

### AI代理的不同類型

不是所有代理的構造都相同。這裡以旅遊訂票代理為例說明主要類型：

| <strong>代理類型</strong> | <strong>功能</strong> | <strong>旅遊代理範例</strong> |
|---|---|---|
| <strong>簡單反射代理</strong> | 遵循硬編碼規則——無記憶，無規劃。 | 收到投訴郵件 → 轉給客服。就是這麼簡單。 |
| <strong>基於模型的反射代理</strong> | 持有世界的內部模型，並隨變化更新。 | 跟蹤歷史航班價格，標記價格突然上漲的路線。 |
| <strong>目標導向代理</strong> | 有明確目標，逐步規劃達成方法。 | 從當前地點訂票，安排完整行程（航班、車輛、酒店）到達目的地。 |
| <strong>效用導向代理</strong> | 不只找到<em>一個</em>解決方案，而是權衡取捨找到<em>最佳</em>方案。 | 平衡費用與便利性，找出最高評價且符合您偏好的行程。 |
| <strong>學習型代理</strong> | 通過反饋逐漸優化。 | 根據旅遊後調查結果調整未來的訂票推薦。 |
| <strong>階層式代理</strong> | 高階代理將工作拆分成子任務，交給低階代理處理。 | 「取消行程」指令會拆分為取消航班、取消酒店、取消租車——由子代理分別處理。 |
| **多代理系統（MAS）** | 多個獨立代理協同工作（或競爭）。 | 協作型：獨立代理分別處理酒店、航班和娛樂。競爭型：多代理競爭以最優價格訂滿酒店客房。 |

---

## 何時使用AI代理

能用AI代理不代表總該用。以下是代理真正發揮優勢的場景：

![When to use AI Agents?](../../../translated_images/zh-MO/when-to-use-ai-agents.54becb3bed74a479.webp)

- <strong>開放式問題</strong> — 解決步驟無法預先程式化。需要LLM動態找出解決路徑。
- <strong>多步驟程序</strong> — 任務需跨多輪使用多種工具，不是單一查詢或生成。
- <strong>持續優化</strong> — 想讓系統根據用戶反饋或環境訊號變得更聰明。

稍後課程中《打造可信賴AI代理》一課，會更深入探討何時該用（和不該用）AI代理。

---

## 代理解決方案基礎

### 代理開發

構建代理的第一步是定義它<em>能做什麼</em>——它的工具、動作和行為。

本課程使用 **Microsoft Foundry Agent Service** 作為主要平台。它支持：

- OpenAI、Mistral和Meta（Llama）等廠商的模型
- Tripadvisor等廠商授權的數據
- 標準化的OpenAPI 3.0工具定義

### 代理模式

您是透過提示與LLM溝通。對於代理，不能每條提示都手工製作——代理需要跨多步驟執行操作。這時候就用到<strong>代理模式</strong>。它們是可重用的提示和指揮LLM的策略，讓整體流程更具擴展性和可靠性。

本課程的結構圍繞最常用且實用的代理模式設計。

### 代理框架

代理框架為開發者提供現成範本、工具及基礎架構，讓建造代理更簡單。它們能幫助您：

- 連結工具和功能
- 觀察代理的行為（並排除錯誤）
- 促進多代理間的協作

本課程聚焦於用於生產環境的 **Microsoft Agent Framework (MAF)**。

---

## 範例代碼

準備好實戰演示了嗎？以下是本課的代碼範例：

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## 有問題？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，與其他學習者交流，參加辦公時間，並由社區回答您的AI代理問題。


---

## 對本代理做煙霧測試（可選）

當您學會在 [Lesson 16](../16-deploying-scalable-agents/README.md) 部署代理後，可使用現成的目錄 [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) 快速為本課「TravelAgent」做部署後健康檢查。詳見 [`tests/README.md`](../tests/README.md) 的執行說明。

---

## 上一課

[課程設定](../00-course-setup/README.md)

## 下一課

[探索代理框架](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->