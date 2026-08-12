# 使用代理協議（MCP、A2A 與 NLWeb）

[![代理協議](../../../translated_images/zh-TW/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(點擊上方圖片觀看本課程視頻)_

隨著 AI 代理的使用日益增長，也對確保標準化、安全性以及支持開放創新的協議需求日益增加。在本課程中，我們將介紹三種致力於滿足此需求的協議──模型上下文協議（Model Context Protocol，MCP）、代理對代理（Agent to Agent，A2A）與自然語言網絡（Natural Language Web，NLWeb）。

## 介紹

本課程將涵蓋：

• **MCP** 如何讓 AI 代理存取外部工具與資料以完成使用者任務。

• **A2A** 如何促進不同 AI 代理之間的通訊與協作。

• **NLWeb** 如何為任何網站帶來自然語言介面，使 AI 代理能夠發現並互動網站內容。

## 學習目標

• <strong>識別</strong> MCP、A2A 與 NLWeb 在 AI 代理背景下的核心目的與優勢。

• <strong>解釋</strong> 每個協議如何促進大型語言模型(LLM)、工具與其他代理之間的溝通與互動。

• <strong>認識</strong> 每個協議在構建複雜代理系統中的不同角色。

## 模型上下文協議

**模型上下文協議（Model Context Protocol, MCP）** 是一個開放標準，提供應用程式以標準化方式向大型語言模型(LLMs)提供上下文與工具。這使 AI 代理能通過「通用接頭」以一致方式連接不同資料來源與工具。

讓我們來看看 MCP 的組成元件、相較直接使用 API 的優勢，以及 AI 代理如何使用 MCP 伺服器的範例。

### MCP 核心組件

MCP 採用<strong>客戶端-伺服器架構</strong>，核心組件包括：

• **Hosts（主機）**：大型語言模型應用程式（例如像 VSCode 的代碼編輯器），負責啟動與 MCP 伺服器的連線。

• **Clients（客戶端）**：主機應用中維持與伺服器一對一連線的組件。

• **Servers（伺服器）**：暴露特定功能的輕量級程式。

協議中包含三種核心原語，代表 MCP 伺服器的能力：

• <strong>工具</strong>：AI 代理可以呼叫的獨立動作或功能。例如，氣象服務可能提供「取得天氣」工具，電商伺服器可能提供「購買商品」工具。MCP 伺服器會在其能力列表中公布每個工具名稱、說明與輸入/輸出結構。

• <strong>資源</strong>：MCP 伺服器可提供的唯讀資料項目或文件，客戶端可按需取得。如檔案內容、資料庫紀錄或日誌檔。資源可以是文本（如程式碼或 JSON）或二進位（如圖像或 PDF）。

• <strong>提示</strong>：預先定義的模板，提供建議提示，允許更複雜的工作流程。

### MCP 的優勢

MCP 為 AI 代理帶來以下重大優勢：

• <strong>動態工具發現</strong>：代理能動態從伺服器接收可用工具清單及其功能說明，與傳統需靜態編碼整合的 API 不同，MCP 只需「整合一次」，更具適應性。

• **跨 LLM 互操作性**：MCP 可跨不同大型語言模型運作，提供彈性切換核心模型以獲得更佳效能。

• <strong>標準化安全性</strong>：MCP 包含標準驗證方法，增強擴展性，加入更多 MCP 伺服器時更簡單，不需為不同傳統 API 管理多種金鑰與驗證類型。

### MCP 範例

![MCP 圖示](../../../translated_images/zh-TW/mcp-diagram.e4ca1cbd551444a1.webp)

假設用戶想用由 MCP 驅動的 AI 助理預訂機票。

1. <strong>連線</strong>：AI 助理（MCP 客戶端）連接到航空公司提供的 MCP 伺服器。

2. <strong>工具發現</strong>：客戶端詢問航空公司的 MCP 伺服器「你有什麼工具？」伺服器回覆有「搜尋航班」和「訂票」工具。

3. <strong>工具調用</strong>：您請 AI 助理「請搜尋從波特蘭到檀香山的航班」，AI 助理使用大型語言模型判斷需呼叫「搜尋航班」工具並將相關參數（出發地、目的地）傳給 MCP 伺服器。

4. <strong>執行與回應</strong>：MCP 伺服器作為包裝層，實際呼叫航空公司內部訂票 API，接收航班資訊（例如 JSON 資料），然後回傳至 AI 助理。

5. <strong>後續互動</strong>：AI 助理展示航班選項，使用者選定後，助理可能呼叫同一 MCP 伺服器上的「訂票」工具來完成預訂。

## 代理對代理協議（A2A）

MCP 專注於連接大型語言模型與工具，而<strong>代理對代理協議（Agent-to-Agent, A2A）</strong>更進一步，允許不同 AI 代理之間的通訊與協作。A2A 連接來自不同組織、環境與技術棧的 AI 代理，共同完成共享任務。

我們將探討 A2A 的組成元件與優勢，並以旅遊應用為例說明其運用。

### A2A 核心組件

A2A 著重於代理間的通訊與協作，以完成使用者子任務。協議中的各組件功能如下：

#### 代理卡（Agent Card）

類似 MCP 伺服器分享工具清單，代理卡包含：
- 代理的名稱。
- <strong>一般任務描述</strong>。
- 幫助其他代理（與人類用戶）理解何時以及為何呼叫該代理的<strong>具體技能清單</strong>及說明。
- 代理的<strong>目前端點 URL</strong>。
- 代理的<strong>版本</strong>與<strong>能力</strong>（例如支援串流回應與推播通知）。

#### 代理執行器（Agent Executor）

代理執行器負責將<strong>使用者聊天上下文傳遞給遠端代理</strong>，遠端代理需此來理解要完成的任務。在 A2A 伺服器中，代理使用自身的 LLM 解析輸入請求並利用內部工具執行任務。

#### 藝品（Artifact）

遠端代理完成任務後，產出成為藝品。藝品<strong>包含代理工作結果</strong>、對所完成工作的<strong>描述</strong>及透過協議傳送的<strong>文字上下文</strong>。藝品傳送後，與該遠端代理的連線將關閉，直到再次需要。

#### 事件佇列（Event Queue）

用於<strong>處理更新與傳送消息</strong>，對於預防代理間連線因任務尚未完成而提早關閉尤其重要，特別是任務完成時間較長時。

### A2A 的優勢

• <strong>增強協作</strong>：讓來自不同廠商與平台的代理能互動、共享上下文並協同工作，實現跨傳統斷裂系統的無縫自動化。

• <strong>模型選擇彈性</strong>：每個 A2A 代理可決定使用哪個 LLM 服務其請求，允許針對需求最佳化或微調模型，相較 MCP 某些情況只用單一 LLM 連線更靈活。

• <strong>內建驗證機制</strong>：A2A 協議直接整合驗證，為代理互動提供保護性強的安全框架。

### A2A 範例

![A2A 圖示](../../../translated_images/zh-TW/A2A-Diagram.8666928d648acc26.webp)

我們擴充旅遊預訂情境，這次使用 A2A。

1. <strong>多代理接收使用者請求</strong>：使用者與「旅遊代理」A2A 用戶端／代理互動，例如說：「請為我預訂下週前往檀香山的全套行程，包括機票、飯店與租車」。

2. <strong>旅遊代理進行協調</strong>：旅遊代理利用自身 LLM 推理該工作，判斷需與其他專業代理溝通。

3. <strong>代理間通訊</strong>：旅遊代理使用 A2A 協議連結下游代理，例如由不同公司建立的「航空代理」、「飯店代理」及「租車代理」。

4. <strong>委派任務執行</strong>：旅遊代理將特定任務（如「找檀香山航班」、「訂飯店」、「租車」）委派給這些專業代理，這些代理運行各自的 LLM 並使用其工具（可能也是 MCP 伺服器）完成任務。

5. <strong>綜合回應</strong>：所有下游代理任務完成後，旅遊代理彙整結果（航班詳情、飯店確認、租車預訂）並以聊天式介面回覆使用者。

## 自然語言網絡（NLWeb）

網站長期以來是使用者獲取網路資訊與數據的主要管道。

讓我們了解 NLWeb 的不同組件，其優勢，並藉由旅遊應用範例探索其運作方式。

### NLWeb 組件

- **NLWeb 應用程式（核心服務程式碼）**：處理自然語言問題的系統。將平台不同部分連結以產生回應。可視為<strong>驅動網站自然語言功能的引擎</strong>。

- **NLWeb 協議**：基於網站自然語言互動的<strong>基本規則集合</strong>。回傳 JSON 格式回應（常用 Schema.org）。目標是為「AI 網路」建立簡易基礎，就像 HTML 使線上文件分享成為可能。

- **MCP 伺服器（模型上下文協議端點）**：每個 NLWeb 設定同時也是一個 **MCP 伺服器**。這表示可與其他 AI 系統共享工具（如「ask」方法）與數據。實務上，讓網站內容與功能可被 AI 代理使用，使網站成為更廣泛「代理生態系」的一部分。

- <strong>嵌入模型</strong>：用於將網站內容轉換成稱為向量（embeddings）的數值表示。這些向量以可被電腦比較與搜尋的方式捕捉意義，並儲存在特殊資料庫中，使用者可選擇想用的嵌入模型。

- **向量資料庫（檢索機制）**：儲存網站內容嵌入的資料庫。使用者提問時，NLWeb 會查詢向量資料庫快速找到最相關資訊，並根據相似度排序提供可能回答。NLWeb 支援 Qdrant、Snowflake、Milvus、Azure AI Search 與 Elasticsearch 等向量存儲系統。

### NLWeb 範例

![NLWeb](../../../translated_images/zh-TW/nlweb-diagram.c1e2390b310e5fe4.webp)

再次考慮我們的旅遊預訂網站，這次由 NLWeb 驅動。

1. <strong>數據導入</strong>：旅遊網站現有產品目錄（如航班列表、飯店介紹、旅遊套裝）經由 Schema.org 格式化或透過 RSS 載入。NLWeb 工具吸收結構化數據，建立嵌入並存入本地或遠端向量資料庫。

2. **自然語言查詢（人類）**：使用者訪問網站，不必透過導覽選單，而是在聊天介面輸入：「幫我找下週有游泳池且適合家庭入住的檀香山飯店」。

3. **NLWeb 處理**：NLWeb 應用程式收到查詢，將問題送入大型語言模型理解，同時查詢向量資料庫尋找相關飯店列表。

4. <strong>精確結果</strong>：大型語言模型協助解析資料庫搜尋結果，根據「適合家庭」、「游泳池」與「檀香山」條件找出最佳匹配，並格式化自然語言回應。關鍵是回應直接引用網站目錄中的實際飯店，避免虛構資訊。

5. **AI 代理互動**：由於 NLWeb 同時是 MCP 伺服器，外部 AI 旅遊代理也能連接本網站的 NLWeb 實例。該 AI 代理可使用 `ask` MCP 方法直接查詢網站：`ask("住宿飯店推薦的檀香山區有沒有素食友善餐廳？")`。NLWeb 實例將處理此問題，利用其餐廳資料庫（若已載入），並回傳結構化 JSON 回應。

### 對 MCP / A2A / NLWeb 有更多疑問嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，與其他學習者互動，參加問答時間，解答您對 AI 代理的疑問。

## 資源

- [入門 MCP](https://aka.ms/mcp-for-beginners)  
- [MCP 文件](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb 倉庫](https://github.com/nlweb-ai/NLWeb)
- [Microsoft 代理架構](https://aka.ms/ai-agents-beginners/agent-framework)

## 前一課

[生產環境中的 AI 代理](../10-ai-agents-production/README.md)

## 下一課

[AI 代理的上下文工程](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->