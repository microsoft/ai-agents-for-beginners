[![Intro to AI Agents](../../../translated_images/zh-MO/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(按一下上方圖片觀看本課程視頻)_

# AI Agents 及代理應用介紹

歡迎來到 **AI Agents for Beginners** 課程！本課程為你提供基礎知識與實際運作的程式碼，讓你能從零開始打造 AI Agents。

快來 <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord 社群</a> 打個招呼 — 這裡聚集了許多學習者和 AI 開發者，樂於解答你的疑問。

開始建構之前，讓我們先確定真正理解 AI Agent 是什麼，以及何時適合使用它。

---

## 介紹

本課程涵蓋：

- 什麼是 AI Agents，以及存在的不同類型
- AI Agents 最適合處理的任務類型
- 設計代理解決方案時所使用的核心組件

## 學習目標

完成本課程後，你應該能：

- 解釋 AI Agent 是什麼，以及它與一般 AI 解決方案的不同之處
- 知道何時應使用 AI Agent（以及何時不該使用）
- 草擬針對實際問題的基本代理解決方案設計

---

## 定義 AI Agents 及其種類

### 什麼是 AI Agents？

以下是簡單的理解方式：

> **AI Agents 是系統，讓大型語言模型（LLMs）真正能「做事情」— 提供工具和知識，讓模型能作用於世界，而不只是簡單回答提示。**

讓我們稍作拆解：

- <strong>系統</strong> — AI Agent 不僅是一個單一部分，而是多個組件協同作業。每個代理的核心包含三大部分：
  - <strong>環境</strong> — 代理工作的空間。以旅遊訂票代理為例，工作環境就是訂票平台。
  - <strong>感測器</strong> — 代理讀取環境當前狀態的方式。旅遊代理可能會查詢飯店空房或機票價格。
  - <strong>致動器</strong> — 代理執行行動的方式。旅遊代理可能會預訂房間、寄送確認函或取消訂單。

![What Are AI Agents?](../../../translated_images/zh-MO/what-are-ai-agents.1ec8c4d548af601a.webp)

- **大型語言模型（LLMs）** — 代理早於 LLMs 就存在，但現代代理的威力來自 LLM。它們能理解自然語言、推理背景，將模糊的使用者需求轉換為具體行動方案。

- <strong>執行動作</strong> — 沒有代理系統，LLM 只能產生文字。在代理系統內，LLM 可實際<em>執行</em>步驟—搜索資料庫、呼叫 API、傳送訊息。

- <strong>使用工具</strong> — 代理可使用什麼工具取決於（1）執行環境和（2）開發者賦予的功能。旅遊代理可能能查航班，但不能修改客戶資料 — 全看你如何設計。

- <strong>記憶與知識</strong> — 代理能擁有短期記憶（當前對話）和長期記憶（客戶資料庫、過去互動）。旅遊代理可能「記得」你喜歡靠窗座位。

---

### AI Agents 的不同類型

代理不盡相同。以下以旅遊訂票代理作為範例，說明主要類型：

| <strong>代理類型</strong> | <strong>功能</strong> | <strong>旅遊代理範例</strong> |
|---|---|---|
| <strong>簡單反射代理</strong> | 遵循硬編碼規則 — 無記憶，無規劃。 | 收到投訴電郵 → 轉交客服。就這樣。 |
| <strong>基於模型的反射代理</strong> | 保持世界內部模型，並隨變化更新。 | 追蹤歷史機票價，標記突然變貴的路線。 |
| <strong>目標導向代理</strong> | 有明確目標，逐步規劃達成路徑。 | 預訂完整行程（機票、租車、飯店），從現地出發到目的地。 |
| <strong>效用導向代理</strong> | 不只找 <em>一種</em> 解決方案，而是權衡利弊找到 <em>最佳</em> 方案。 | 平衡成本與便利，找出符合偏好的最高評分行程。 |
| <strong>學習代理</strong> | 持續從回饋學習，逐漸優化。 | 根據旅後調查調整未來預訂建議。 |
| <strong>階層式代理</strong> | 高階代理拆分任務，委派子代理執行。 | 「取消行程」請求拆成取消機票、取消飯店、取消租車 — 各由子代理負責。 |
| **多代理系統 (MAS)** | 多個獨立代理協同（或競爭）運作。 | 合作：分別負責飯店、航班、娛樂。競爭：多個代理競爭以最佳價格搶訂房。 |

---

## 何時使用 AI Agents

能用 AI Agent 不代表隨時適用。以下情境特別適合代理：

![When to use AI Agents?](../../../translated_images/zh-MO/when-to-use-ai-agents.54becb3bed74a479.webp)

- <strong>開放式問題</strong> — 解決步驟無法預先編程，需要 LLM 動態找路徑。
- <strong>多步驟流程</strong> — 需跨多回合使用多種工具，非單次查詢或生成。
- <strong>持續改進</strong> — 想要系統依用戶回饋或環境訊號變聰明。

本課後段的 **建立值得信賴的 AI Agents** 課程將更深入探討何時該用與不該用 AI Agents。

---

## 代理解決方案基礎

### 代理開發

建構代理第一步是定義<em>它能做什麼</em>— 包含工具、操作和行為。

本課程以 **Azure AI Agent Service** 為主平台，支持：

- OpenAI、Mistral、Meta（Llama）等供應商的模型
- Tripadvisor 等資料供應商的授權資料
- 標準化的 OpenAPI 3.0 工具定義

### 代理模式

與 LLM 通訊靠提示 (prompt)。代理常涉及多步驟執行，無法手動逐條撰寫提示。這時候就用到 **Agentic Patterns**：一種可重用的策略，方便更大規模、可靠地提示與編排 LLM。

本課程架構圍繞最常見和實用的代理模式。

### 代理框架

代理框架為開發者提供現成範本、工具和基礎建設，幫助：

- 連接工具和能力
- 觀察代理狀態（出錯時調試）
- 多代理協作

本課程重點教材為生產級的 **Microsoft Agent Framework (MAF)**。

---

## 程式碼範例

準備好實際操作了？本課程的程式碼範例如下：

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## 有問題嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者互動、參加開放答疑時段，由社群解答你的 AI Agent 問題。

---

## 上一課

[Course Setup](../00-course-setup/README.md)

## 下一課

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->