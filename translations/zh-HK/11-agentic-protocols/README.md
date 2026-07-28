# 使用 Agentic 協議 (MCP、A2A 與 NLWeb)

[![Agentic 協議](../../../translated_images/zh-HK/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(點擊上方圖片觀看本課程影片)_

隨著 AI 代理使用的增加，對於確保標準化、安全性和支持開放創新的協議需求也隨之增加。在本課裡，我們將介紹 3 種為滿足此需求而設計的協議——模型上下文協議（Model Context Protocol，MCP）、代理對代理協議（Agent to Agent，A2A）及自然語言網（Natural Language Web，NLWeb）。

## 介紹

本課將介紹：

• **MCP** 如何允許 AI 代理存取外部工具和數據以完成用戶任務。

• **A2A** 如何促進不同 AI 代理之間的溝通與合作。

• **NLWeb** 如何為任何網站帶來自然語言介面，使 AI 代理能發現並互動該內容。

## 學習目標

• <strong>識別</strong> MCP、A2A 與 NLWeb 在 AI 代理情境下的核心目的與好處。

• <strong>解釋</strong> 各協議如何促進大型語言模型（LLM）、工具與其他代理間的溝通與互動。

• <strong>辨識</strong> 每個協議在構建複雜代理系統中的不同角色。

## 模型上下文協議

**模型上下文協議（Model Context Protocol，MCP）** 是一項開放標準，提供應用程式向大型語言模型提供上下文與工具的標準化方式。它使 AI 代理能以一致的方式透過「通用適配器」連接到不同的數據來源和工具。

我們來看看 MCP 的組件、與直接使用 API 相比的優勢，以及 AI 代理可能如何利用 MCP 伺服器的範例。

### MCP 核心組件

MCP 採用<strong>客戶端-伺服器架構</strong>，核心組件包括：

• **主機（Hosts）** 是大型語言模型應用（例如像 VSCode 的程式碼編輯器），負責發起與 MCP 伺服器的連接。

• **用戶端（Clients）** 是主機應用內部負責維持與伺服器一對一連接的組件。

• **伺服器（Servers）** 是暴露特定功能的輕量程式。

協議包含三個核心原語，代表 MCP 伺服器的功能：

• **工具（Tools）**：是 AI 代理可調用的離散行動或函數。例如，氣象服務可能提供「取得天氣」工具，電子商務伺服器可能提供「購買商品」工具。MCP 伺服器會在功能列表中公布各工具的名稱、描述及輸入/輸出結構。

• **資源（Resources）**：是 MCP 伺服器可提供的唯讀資料項目或文件，客戶端可按需擷取，範例包括檔案內容、資料庫記錄或日誌文件。資源可以是文本（例如程式碼或 JSON）或二進制檔（例如圖片或 PDF）。

• **提示（Prompts）**：是預定義模板，提供建議的提示，有助於實現更複雜的工作流程。

### MCP 的好處

MCP 為 AI 代理帶來顯著優勢：

• <strong>動態工具發現</strong>：代理可以動態接收伺服器提供的可用工具清單及其描述，與傳統靜態編碼整合的 API 不同，只要 API 有改變就必須更新程式碼，MCP 採用「一次整合」方式，提高適應力。

• **跨 LLM 互通性**：MCP 支援不同大型語言模型，使得切換核心模型以評估更佳效果更靈活。

• <strong>標準化安全性</strong>：MCP 內建標準認證方法，當新增對其他 MCP 伺服器的存取時，更易於擴展，比管理多種傳統 API 的金鑰與認證方式更簡單。

### MCP 範例

![MCP 圖解](../../../translated_images/zh-HK/mcp-diagram.e4ca1cbd551444a1.webp)

想像用戶想借助 MCP 運作的 AI 助理訂購機票。

1. <strong>連接</strong>：AI 助理（MCP 用戶端）連接航空公司提供的 MCP 伺服器。

2. <strong>工具發現</strong>：用戶端詢問航空公司 MCP 伺服器：「你有哪些工具？」伺服器回應提供工具如「搜尋航班」及「訂票」。

3. <strong>調用工具</strong>：用戶對 AI 助理說：「請搜尋從波特蘭到檀香山的航班。」AI 助理利用其 LLM 辨識需要調用「搜尋航班」工具，並向 MCP 伺服器傳遞相關參數（起點、目的地）。

4. <strong>執行與回應</strong>：MCP 伺服器充當包裝器，呼叫航空公司內部預訂 API，接收航班資料（例如 JSON），並回傳給 AI 助理。

5. <strong>進一步互動</strong>：AI 助理呈現航班選項，用戶選擇後，助理可能使用同一 MCP 伺服器調用「訂票」工具完成訂票。

## 代理對代理協議 (A2A)

MCP 專注於連接 LLM 與工具，**代理對代理（Agent-to-Agent，A2A）協議** 則更進一步，讓不同 AI 代理之間能夠溝通與協作。A2A 連接跨組織、環境及技術堆疊的 AI 代理，共同完成共享任務。

我們將檢視 A2A 的組件與優勢，並以旅遊應用做示範。

### A2A 核心組件

A2A 著重促進代理之間的溝通，協同完成使用者子任務。協議中各成分的貢獻包括：

#### 代理卡片

類似 MCP 伺服器分享工具清單，代理卡片包含：
- 代理名稱。
- 一般完成任務的<strong>描述</strong>。
- 涵蓋<strong>特定技能清單</strong>及描述，幫助其他代理或人類用戶了解何時及為何調用該代理。
- 代理的<strong>當前端點 URL</strong>。
- 代理的<strong>版本</strong>及<strong>功能</strong>，如串流回應與推送通知。

#### 代理執行器

代理執行器負責<strong>將用戶對話上下文傳遞給遠端代理</strong>，遠端代理需此資料以理解任務。A2A 伺服器中，代理使用其大型語言模型解析請求，並利用自身工具執行任務。

#### 工件

遠端代理完成任務後產出工件。工件<strong>包含代理工作結果</strong>、<strong>完成描述</strong>及透過協議傳遞的<strong>文本上下文</strong>。工件傳送後，與遠端代理的連線關閉，直到再次需要。

#### 事件佇列

用於<strong>處理更新與訊息傳遞</strong>。在生產環境中對代理系統尤為重要，確保任務完成之前代理間連線不會中斷，尤其任務可能耗時較長。

### A2A 的好處

• <strong>增強協作</strong>：讓不同供應商及平台的代理交流、共享上下文、協同作業，促成本來分離系統間的無縫自動化。

• <strong>模型選擇彈性</strong>：每個 A2A 代理可自行決定其使用的 LLM，允許單個代理優化或微調模型，而非如某些 MCP 場景下只有單一 LLM 連線。

• <strong>內建認證</strong>：認證直接整合於 A2A 協議，為代理交互提供強健安全框架。

### A2A 範例

![A2A 圖解](../../../translated_images/zh-HK/A2A-Diagram.8666928d648acc26.webp)

讓我們擴展前述旅遊訂票情境，這次採用 A2A。

1. <strong>使用者向多代理請求</strong>：使用者與「旅遊代理」A2A 用戶端/代理互動，可能說：「請預訂下週前往檀香山的全套旅程，包括機票、飯店和租車」。

2. <strong>旅遊代理的調度</strong>：旅遊代理收到複雜請求，利用其 LLM 推理任務並判斷需與其他專門代理互動。

3. <strong>代理間通訊</strong>：旅遊代理利用 A2A 協議連接下游代理，如由不同公司建立的「航空公司代理」、「飯店代理」及「租車代理」。

4. <strong>委派任務執行</strong>：旅遊代理將具體任務分送給這些專門代理（如「尋找前往檀香山的航班」、「訂飯店」、「租車」）。每個專門代理運行自己的 LLM，利用其工具（可能也是 MCP 伺服器）完成各自的訂購部分。

5. <strong>整合回應</strong>：所有下游代理完成任務後，旅遊代理彙整結果（航班細節、飯店確認、租車訂單），並以聊天格式將綜合答覆發回使用者。

## 自然語言網 (NLWeb)

網站長期以來是使用者存取網際網路資料與資訊的主要途徑。

讓我們探討 NLWeb 的不同組件、其好處，並藉由旅遊應用示範 NLWeb 的運作。

### NLWeb 組件

- **NLWeb 應用程式（核心服務程式碼）**：負責處理自然語言問題的系統。它連接平台不同部分以產生回應。可以將其視為<strong>驅動網站自然語言功能的引擎</strong>。

- **NLWeb 協議**：網站自然語言互動的<strong>基本規則集</strong>。回應以 JSON 格式傳送（常用 Schema.org），其目標是為「AI 網路」打造簡單基礎，就像 HTML 使網上文件共享成為可能一樣。

- **MCP 伺服器（模型上下文協議端點）**：每個 NLWeb 系統同時作為<strong>MCP 伺服器</strong>。這代表它能與其他 AI 系統分享工具（如「ask」方法）與數據。實際上，讓網站內容與功能可以被 AI 代理使用，使網站成為更廣泛「代理生態系」的一部分。

- <strong>嵌入模型</strong>：用於<strong>將網站內容轉換成數值向量表示（embeddings）</strong>的模型。這些向量以電腦可比較及搜尋的方式捕捉意義，並存於特殊資料庫。使用者可選擇想使用的嵌入模型。

- **向量資料庫（檢索機制）**：存放網站內容的向量。當有人提問時，NLWeb 查詢向量資料庫，快速找出最相關資訊，提供依相似度排序的答案列表。NLWeb 支援多種向量儲存系統，如 Qdrant、Snowflake、Milvus、Azure AI 搜尋及 Elasticsearch。

### NLWeb 範例

![NLWeb](../../../translated_images/zh-HK/nlweb-diagram.c1e2390b310e5fe4.webp)

再以我們旅遊訂票網站為例，但這次由 NLWeb 提供動力。

1. <strong>資料擷取</strong>：旅遊網站的既有產品目錄（如航班清單、飯店介紹、旅遊行程包）透過 Schema.org 格式化或利用 RSS 餵送。NLWeb 的工具擷取此結構化數據，建立嵌入並存入本地或遠端向量資料庫。

2. **自然語言查詢（人類）**：使用者造訪網站，不透過目錄操作，而是在聊天介面輸入：「幫我找檀香山適合家庭入住，有游泳池的飯店，下週的訂房」。

3. **NLWeb 處理**：NLWeb 應用接收查詢，將問題送入 LLM 理解，同時在向量資料庫搜尋相關飯店清單。

4. <strong>準確結果</strong>：LLM 協助解讀資料庫搜索結果，根據「適合家庭」、「游泳池」與「檀香山」條件選出最佳匹配，並以自然語言格式化回應。關鍵是回應參照網站目錄中實際飯店，避免虛構資訊。

5. **AI 代理互動**：由於 NLWeb 同時作為 MCP 伺服器，外部 AI 旅遊代理也能連上該網站的 NLWeb 實例，使用 `ask` MCP 方法直接提問網站，比如 `ask("檀香山區有飯店推薦的純素友善餐廳嗎？")`。NLWeb 會利用其餐廳資訊（若已載入），並返回結構化 JSON 回應。

### 對 MCP/A2A/NLWeb 有更多問題？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者交流，參加辦公時間，並獲得 AI 代理相關問題解答。

## 資源

- [MCP 初學者指南](https://aka.ms/mcp-for-beginners)  
- [MCP 文件](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb 原始碼庫](https://github.com/nlweb-ai/NLWeb)
- [Microsoft 代理框架](https://aka.ms/ai-agents-beginners/agent-framework)

## 前一課

[生產環境中的 AI 代理](../10-ai-agents-production/README.md)

## 下一課

[AI 代理的上下文工程](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->