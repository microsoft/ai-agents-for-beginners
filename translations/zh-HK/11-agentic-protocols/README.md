# 使用自主代理協議 (MCP、A2A 及 NLWeb)

[![Agentic Protocols](../../../translated_images/zh-HK/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(點擊上面圖片觀看本課程影片)_

隨著 AI 代理使用量的增加，亦對確保標準化、安全性及支持開放創新的協議需求逐漸提升。在本課中，我們將涵蓋三個旨在滿足此需求的協議──模型上下文協議（Model Context Protocol, MCP）、代理與代理通訊協議（Agent to Agent, A2A）以及自然語言網絡（Natural Language Web, NLWeb）。

## 介紹

本課將涵蓋：

• MCP 如何允許 AI 代理存取外部工具及數據以完成使用者任務。

• A2A 如何使不同 AI 代理間能進行溝通與協作。

• NLWeb 如何為任何網站帶來自然語言介面，使 AI 代理能夠發現及互動網站內容。

## 學習目標

• <strong>識別</strong> MCP、A2A 與 NLWeb 在 AI 代理場景中的核心目的及優勢。

• <strong>解釋</strong> 每個協議如何促進大型語言模型（LLM）、工具與其他代理之間的溝通與互動。

• <strong>辨認</strong> 各協議在構建複雜代理系統中扮演的不同角色。

## 模型上下文協議（Model Context Protocol）

**模型上下文協議（MCP）** 是一個開放標準，提供一種標準化方式，讓應用程式能對大型語言模型提供上下文與工具。它充當一個「通用介面」，能以一致的方式連接不同的資料來源與工具，以供 AI 代理使用。

以下將介紹 MCP 的組成、相較直接 API 使用的優勢，以及 AI 代理如何使用 MCP 伺服器的範例。

### MCP 核心組件

MCP 採用<strong>用戶端-伺服器架構</strong>，核心組件為：

• **主機（Hosts）**：大型語言模型應用程式（例如如 VSCode 代碼編輯器）啟動與 MCP 伺服器的連線。

• **用戶端（Clients）**：主機內部的組件，維持與伺服器間的一對一連線。

• **伺服器（Servers）**：輕量級程式，公開特定功能。

協議中包含三個核心基元，即 MCP 伺服器的功能：

• **工具（Tools）**：這些是 AI 代理可呼叫以執行任務的離散動作或函式。例如，天氣服務可公開「取得天氣」工具，電子商務伺服器則可能公開「購買產品」工具。MCP 伺服器會在功能列表中公布每個工具的名稱、描述與輸入/輸出模式。

• **資源（Resources）**：這是 MCP 伺服器可提供的唯讀資料項目或文件，用戶端可按需取得。範例包括檔案內容、資料庫記錄或日誌檔。資源可為文字（如程式碼或 JSON）或二進位檔（如影像或 PDF）。

• **提示（Prompts）**：這是預先定義的範本，提供建議的提示，允許更複雜的工作流程。

### MCP 的優勢

MCP 對 AI 代理具有重大優勢：

• <strong>動態工具發現</strong>：代理可動態獲得伺服器提供的工具清單及相關描述。這與傳統 API 不同，後者通常需要靜態程式碼集成，API 有改動時必須更新程式碼。MCP 採用「集成一次」的方法，增強適應性。

• **跨 LLM 互通性**：MCP 可跨不同大型語言模型運作，提供更換核心模型以提升效能的靈活性。

• <strong>標準化安全性</strong>：MCP 包含標準驗證方式，增加擴充性，在接入更多 MCP 伺服器時簡化管理。相較管理不同 API 金鑰及驗證類型更為簡單。

### MCP 範例

![MCP Diagram](../../../translated_images/zh-HK/mcp-diagram.e4ca1cbd551444a1.webp)

設想用戶想使用 MCP 助力的 AI 助理訂機票。

1. <strong>連線</strong>：AI 助理（MCP 用戶端）連接航空公司提供的 MCP 伺服器。

2. <strong>工具發現</strong>：用戶端詢問航空公司的 MCP 伺服器：「你們有哪些工具？」伺服器回覆如「搜尋航班」與「訂票」工具。

3. <strong>工具調用</strong>：用戶向 AI 助理說：「請搜尋從波特蘭到檀香山的航班。」AI 助理利用其 LLM 辨識需調用「搜尋航班」工具，並將相關參數（起點、終點）傳給 MCP 伺服器。

4. <strong>執行與回應</strong>：MCP 伺服器作為包裝器，實際呼叫航空公司內部訂票 API，接收航班資訊（如 JSON 格式），再返回給 AI 助理。

5. <strong>後續互動</strong>：AI 助理呈現航班選擇。用戶選擇後，助理可能調用同個 MCP 伺服器上的「訂票」工具，完成訂票流程。

## 代理對代理協議（A2A）

MCP 著重於將 LLM 連接工具，**代理對代理協議（A2A）** 則更進一步，允許不同 AI 代理間的溝通與協作，連接來自不同組織、環境與技術堆疊的代理，共同完成任務。

我們將探討 A2A 的組件與優勢，並舉一個在旅遊應用中如何應用的範例。

### A2A 核心組件

A2A 專注於促進代理間溝通與協作，共同完成使用者子任務。協議中每個組件都對此有所貢獻：

#### 代理卡（Agent Card）

類似 MCP 伺服器公開工具列表，代理卡包含：
- 代理的名稱。
- <strong>可完成的一般任務描述</strong>。
- <strong>特定技能清單</strong>及描述，協助其他代理（甚至人類使用者）了解何時及為何呼叫該代理。
- 代理的<strong>當前端點 URL</strong>。
- 代理的<strong>版本</strong>與<strong>功能</strong>，如串流回應及推播通知。

#### 代理執行器（Agent Executor）

負責<strong>將使用者對話上下文傳遞給遠程代理</strong>。遠程代理依此了解需完成的任務。在 A2A 伺服器中，代理使用自己的大型語言模型（LLM）解析請求，並透過自有工具執行任務。

#### 工作產物（Artifact）

遠程代理完成任務後，會產生工作產物。工作產物<strong>包含代理工作結果</strong>、<strong>完成項描述</strong>及透過協議傳送的<strong>文字上下文</strong>。產出發送後，與遠程代理連線將關閉，直到再次需要。

#### 事件佇列（Event Queue）

用於<strong>處理更新與傳遞訊息</strong>。在生產環境中極其重要，以防止代理間連線在任務完成前關閉，尤其任務可能耗時較久。

### A2A 優勢

• <strong>加強協作</strong>：允許來自不同供應商與平台的代理互動、共享上下文與協作，促成傳統上彼此隔離系統的自動化整合。

• <strong>模型選擇彈性</strong>：每個 A2A 代理可自行決定使用哪個 LLM 來服務請求，針對不同代理可使用最佳化或微調模型，與部分 MCP 場景僅接入單一 LLM 不同。

• <strong>內建驗證機制</strong>：驗證直接整合在 A2A 協議中，為代理間互動提供強健安全架構。

### A2A 範例

![A2A Diagram](../../../translated_images/zh-HK/A2A-Diagram.8666928d648acc26.webp)

我們擴展旅遊預訂範例，改以 A2A 實作。

1. <strong>使用者向多代理下達請求</strong>：使用者與「旅遊代理」A2A 用戶端/代理互動，指示「請幫我訂下週前往檀香山的完整行程，包括航班、飯店及租車」。

2. <strong>旅遊代理協調</strong>：旅遊代理接收到此複雜請求，利用 LLM 判斷任務需求，並決定需與其他專業代理互動。

3. <strong>代理間通訊</strong>：旅遊代理透過 A2A 協議連接多個下游代理，如「航空代理」、「飯店代理」與「租車代理」，這些代理各由不同公司建立。

4. <strong>任務委派執行</strong>：旅遊代理將特定任務下派給專門代理（如「尋找檀香山航班」、「訂飯店」、「租賃汽車」）。每個專門代理使用其自身 LLM 並調用自有工具（也可能是 MCP 伺服器）完成該部分訂單。

5. <strong>整合回應</strong>：所有下游代理完成後，旅遊代理匯整結果（航班資訊、飯店確認、租車預約），以聊天式詳盡回應返還予使用者。

## 自然語言網絡（NLWeb）

網站長期以來是使用者瀏覽網際網路資訊與資料的主要方式。

讓我們看看 NLWeb 的不同組成、優勢，以及透過旅遊應用示範 NLWeb 的運作方式。

### NLWeb 的組件

- **NLWeb 應用程式（核心服務代碼）**：處理自然語言問題的系統，連結平台各部分以生成回應。可想像成網站自然語言功能的<strong>引擎</strong>。

- **NLWeb 協議**：自然語言與網站互動的<strong>基本規則集合</strong>。以 JSON 格式（通常用 Schema.org）回傳回應。旨在為「AI 網」打造簡單基底，猶如 HTML 讓線上文件共享成為可能。

- **MCP 伺服器（模型上下文協議端點）**：每個 NLWeb 部署同時作為 **MCP 伺服器** 運作，能與其他 AI 系統分享工具（例如「詢問」方法）及資料。實務上使網站內容與功能可供 AI 代理使用，成為更廣泛「代理生態系」的一環。

- <strong>嵌入模型</strong>：將網站內容轉換為稱為向量（embeddings）的數值表示的模型。這些向量能捕捉含義，讓電腦能比較和檢索。向量存於特殊資料庫，使用者可選擇所需的嵌入模型。

- **向量資料庫（檢索機制）**：存放網站內容的向量。當有人詢問時，NLWeb 會查詢向量資料庫快速尋找最相關資訊，並按相似度排序回傳列表。NLWeb 可搭配多種向量存儲系統，如 Qdrant、Snowflake、Milvus、Azure AI Search 與 Elasticsearch。

### NLWeb 範例

![NLWeb](../../../translated_images/zh-HK/nlweb-diagram.c1e2390b310e5fe4.webp)

再次以旅遊訂票網站為例，這次網站由 NLWeb 提供動力。

1. <strong>資料攝取</strong>：旅遊網站現有商品目錄（例如航班列表、酒店描述、旅遊套票）採用 Schema.org 格式，或透過 RSS 擷取。NLWeb 工具吸收結構化資料，建立向量，並存入本地或遠端向量資料庫。

2. **自然語言查詢（人類使用者）**：使用者造訪網站，非透過導覽，而於聊天介面輸入：「幫我找檀香山下週有泳池的親子飯店」。

3. **NLWeb 處理**：NLWeb 應用接收查詢，將其送給 LLM 理解，同時在向量資料庫中搜尋相關飯店列表。

4. <strong>精準結果</strong>：LLM 協助詮釋資料庫搜尋結果，根據「親子友善」、「泳池」、「檀香山」條件識別最佳匹配，然後格式化為自然語言回應。關鍵在於，回應指向網站真實飯店目錄，避免虛構資訊。

5. **AI 代理互動**：因 NLWeb 同時也是 MCP 伺服器，外部 AI 旅遊代理亦可連接該網站的 NLWeb 實例。該代理可用 `ask` MCP 方法直接查詢網站，如 `ask("有無檀香山地區飯店推薦的素食餐廳?")`。NLWeb 實例會處理該請求，利用餐廳資料庫（如已載入）回傳結構化 JSON 回應。

### 想知道更多關於 MCP/A2A/NLWeb 的問題？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者交流，參與辦公時間並解決你關於 AI 代理的疑惑。

## 資源

- [適合初學者的 MCP](https://aka.ms/mcp-for-beginners)  
- [MCP 文件](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb 原始碼庫](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## 上一課

[生產環境中的 AI 代理](../10-ai-agents-production/README.md)

## 下一課

[AI 代理的上下文工程](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->