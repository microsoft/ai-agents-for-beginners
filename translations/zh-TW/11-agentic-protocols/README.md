# 使用代理協議 (MCP、A2A 與 NLWeb)

[![代理協議](../../../translated_images/zh-TW/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(點擊上方圖片觀看本課程影片)_

隨著 AI 代理的使用日益增加，也越來越需要確保標準化、安全性並支持開放創新的協議。在本課程中，我們將介紹三個旨在滿足此需求的協議——模型上下文協議 (MCP)、代理對代理 (A2A) 以及自然語言網頁 (NLWeb)。

## 介紹

本課程將涵蓋：

• **MCP** 如何讓 AI 代理存取外部工具與資料以完成使用者任務。

• **A2A** 如何啟用不同 AI 代理間的通訊與協作。

• **NLWeb** 如何為任何網站帶來自然語言介面，使 AI 代理能發現並互動內容。

## 學習目標

• <strong>識別</strong> MCP、A2A 與 NLWeb 在 AI 代理上下文中的核心目的與效益。

• <strong>說明</strong> 各協議如何促進大型語言模型、工具及其他代理間的通訊與互動。

• <strong>認識</strong> 各協議在構建複雜代理系統中所扮演的不同角色。

## 模型上下文協議

**模型上下文協議 (MCP)** 是一個開放標準，提供應用程式以標準化方式向大型語言模型提供上下文與工具。這讓 AI 代理以一致方式連接不同資料源與工具，成為通用的中介者。

我們將探討 MCP 的組件、與直接使用 API 相比的優勢，以及 AI 代理如何使用 MCP 伺服器的範例。

### MCP 核心組件

MCP 採用<strong>客戶端-伺服器架構</strong>，核心組件包括：

• **主機 (Hosts)**：大型語言模型應用（例如像 VSCode 的程式碼編輯器），負責啟動與 MCP 伺服器的連線。

• **客戶端 (Clients)**：主機應用內部維護與伺服器一對一連接的元件。

• **伺服器 (Servers)**：輕量程序，公開特定功能。

協議包含三個核心原語，代表 MCP 伺服器的能力：

• **工具 (Tools)**：AI 代理可呼叫以執行動作的獨立功能。例如，天氣服務可公開「取得天氣」工具，電子商務伺服器可能公開「購買商品」工具。MCP 伺服器會在能力清單中公布工具名稱、說明及輸入/輸出結構。

• **資源 (Resources)**：MCP 伺服器可提供的唯讀資料項目或文件，客戶端可按需提取。示例有檔案內容、資料庫紀錄或日誌文件。資源可為文字（如程式碼或 JSON）或二進位（如圖片或 PDF）。

• **提示 (Prompts)**：預先定義的範本，提供建議的提示詞，支援更複雜的工作流程。

### MCP 的效益

MCP 為 AI 代理帶來顯著優勢：

• <strong>動態工具發現</strong>：代理可動態接收伺服器可用工具列表及功能說明。這與傳統 API 需要靜態編碼整合不同，任何 API 變更都需更新程式碼。而 MCP 採「一次整合」方法，更具適應性。

• <strong>跨大型語言模型互通性</strong>：MCP 適用於不同 LLM，提供切換核心模型的彈性以評估更佳效能。

• <strong>標準化安全性</strong>：MCP 含有標準驗證方法，增加新增 MCP 伺服器存取的可擴展性，比管理多種傳統 API 的金鑰及驗證簡單。

### MCP 範例

![MCP 圖示](../../../translated_images/zh-TW/mcp-diagram.e4ca1cbd551444a1.webp)

想像使用者想用以 MCP 驅動的 AI 助理訂機票。

1. <strong>連線</strong>：AI 助理（MCP 客戶端）連接航空公司提供的 MCP 伺服器。

2. <strong>工具發現</strong>：客戶端詢問航空公司 MCP 伺服器：「你有哪些可用工具？」伺服器回覆有「搜尋航班」和「訂航班」等工具。

3. <strong>工具呼叫</strong>：使用者請 AI 助理「請幫我搜尋從波特蘭到火奴魯魯的航班」。助理透過其 LLM 確認需呼叫「搜尋航班」工具，並將相關參數（出發地、目的地）傳給 MCP 伺服器。

4. <strong>執行和回應</strong>：MCP 伺服器作為包裝層，實際呼叫航空公司內部訂票 API，接收航班資料（例如 JSON），回傳給 AI 助理。

5. <strong>後續互動</strong>：AI 助理呈現航班選項。使用者選擇航班後，助理可能呼叫同一 MCP 伺服器的「訂航班」工具，完成訂票。

## 代理對代理協議 (A2A)

MCP 著重於連接 LLM 與工具，<strong>代理對代理 (A2A) 協議</strong>則進一步讓不同 AI 代理間通訊與協作。A2A 連結來自不同組織、環境與技術棧的 AI 代理以共同完成任務。

我們將檢視 A2A 的組件與效益，並以旅遊應用為例說明應用方式。

### A2A 核心組件

A2A 著眼於促進代理間溝通並協力完成使用者子任務。各組件功能如下：

#### 代理卡 (Agent Card)

類似 MCP 伺服器分享工具清單，代理卡包含：
- 代理名稱。
- 它完成的一般任務<strong>描述</strong>。
- <strong>具體技能清單</strong>及說明，協助其他代理（甚至人類使用者）理解何時及為何呼叫該代理。
- 代理<strong>當前終端 URL</strong>。
- 代理的<strong>版本</strong>與<strong>功能</strong>，例如串流回應與推播通知。

#### 代理執行器 (Agent Executor)

代理執行器負責<strong>將使用者對話上下文傳遞給遠端代理</strong>，遠端代理需此以理解待完成任務。在 A2A 伺服器中，代理使用自身 LLM 解析請求並運用內部工具執行任務。

#### 工件 (Artifact)

遠端代理完成任務後，會產生成果工件。工件<strong>包含代理工作結果</strong>、<strong>完成內容描述</strong>及<strong>傳遞於協議的文字上下文</strong>。工件傳送後，與遠端代理連線關閉，待下次需要時再開啟。

#### 事件佇列 (Event Queue)

此元件用於<strong>處理更新與訊息傳遞</strong>。在生產環境中特別重要，防止代理間連線在任務完成前被關閉，尤其當任務完成時間較長時。

### A2A 的效益

• <strong>增強協作</strong>：讓來自不同供應商與平台的代理互動、共享上下文並協同工作，促成跨本來未連結系統的無縫自動化。

• <strong>模型選擇彈性</strong>：每個 A2A 代理可自行決定使用的 LLM，使得代理可使用經優化或微調的模型，而非 MCP 某些情境中的單一 LLM 連接。

• <strong>內建認證</strong>：認證直接整合於 A2A 協議，為代理互動提供強固的安全架構。

### A2A 範例

![A2A 圖示](../../../translated_images/zh-TW/A2A-Diagram.8666928d648acc26.webp)

讓我們以旅遊預訂場景擴展，但這次使用 A2A。

1. <strong>使用者請求至多代理</strong>：使用者與「旅遊代理」A2A 客戶端/代理互動，可能說：「請幫我預訂下週去火奴魯魯的全程行程，包括航班、飯店與租車」。

2. <strong>旅遊代理協調</strong>：旅遊代理接收這複雜請求，利用其 LLM 推理任務並判定需與其他專門代理互動。

3. <strong>代理間通訊</strong>：旅遊代理利用 A2A 協議連線給下游代理，如不同公司創建的「航空代理」、「飯店代理」與「租車代理」。

4. <strong>委派任務執行</strong>：旅遊代理分派特定任務給專業代理（例如「尋找飛往火奴魯魯的航班」、「訂飯店」、「租車」）。這些專業代理運行自有 LLM 且利用自身工具（可能也是 MCP 伺服器），分別完成各自的預訂部分。

5. <strong>整合回應</strong>：當所有下游代理完成任務後，旅遊代理彙整結果（航班細節、飯店確認、租車預訂）並以聊天式回應發送給使用者。

## 自然語言網頁 (NLWeb)

網站長久以來是使用者在網際網路上存取資訊與資料的主要方式。

讓我們看看 NLWeb 的不同組件、NLWeb 的優點，以及透過旅行應用範例了解 NLWeb 的運作。

### NLWeb 的組件

- **NLWeb 應用程式（核心服務程式碼）**：處理自然語言問題的系統。它連接平台的不同部分以產生回應。你可以把它視為推動網站自然語言功能的<strong>引擎</strong>。

- **NLWeb 協議**：與網站自然語言互動的<strong>基本規則集合</strong>。以 JSON 格式回應（常用 Schema.org）。其目的是為了建立「AI 網路」的簡易基礎，就像 HTML 使文件在網路上共用成為可能。

- **MCP 伺服器（模型上下文協議端點）**：每個 NLWeb 設定同時作為一個<strong>MCP 伺服器</strong>。這意味著它能<strong>與其他 AI 系統共享工具（如「詢問」方法）和資料</strong>。實務中，讓網站內容與功能可被 AI 代理使用，使網站成為更廣泛「代理生態系」的一部分。

- <strong>嵌入模型</strong>：用於<strong>將網站內容轉換成數值表示法（向量，embedding）</strong>的模型。這些向量以電腦可比較與搜尋的方式捕捉意義。向量會存於特殊資料庫，使用者可選擇希望使用的嵌入模型。

- **向量資料庫（檢索機制）**：該資料庫<strong>存放網站內容的嵌入向量</strong>。當有人提問，NLWeb 會查詢向量資料庫快速找出最相關資訊，並依相似度排名提供快速答案清單。NLWeb 支援多種向量儲存系統，如 Qdrant、Snowflake、Milvus、Azure AI Search 與 Elasticsearch。

### NLWeb 範例

![NLWeb](../../../translated_images/zh-TW/nlweb-diagram.c1e2390b310e5fe4.webp)

再次思考我們的旅遊預訂網站，但這次它由 NLWeb 提供動力。

1. <strong>資料導入</strong>：旅遊網站現有的產品目錄（例如航班列表、飯店介紹、旅遊套裝）使用 Schema.org 格式或透過 RSS 載入。NLWeb 的工具會擷取這些結構化資料、產生嵌入向量，並存入本地或遠端向量資料庫。

2. **自然語言查詢（人類）**：使用者訪問網站，不用瀏覽選單，而是在聊天介面輸入：「請幫我找下週在火奴魯魯有游泳池的親子飯店」。

3. **NLWeb 處理**：NLWeb 應用收到此查詢，將其傳送給 LLM 進行理解，同時查詢向量資料庫尋找相關飯店資訊。

4. <strong>精確結果</strong>：LLM 協助解讀資料庫搜尋結果，依據「親子友善」、「游泳池」及「火奴魯魯」標準找出最佳匹配，並格式化自然語言回應。關鍵是，回應引用網站目錄中的真實飯店資料，避免憑空捏造。

5. **AI 代理互動**：因 NLWeb 同時作為 MCP 伺服器，外部 AI 旅遊代理也可連接此網站的 NLWeb 實例。AI 代理能使用 `ask` MCP 方法直接詢問網站：`ask("酒店推薦的火奴魯魯地區有任何適合素食者的餐廳嗎？")`。NLWeb 實例將處理此問句，運用其餐廳資料庫（若已載入）並回傳結構化 JSON 回應。

### 想了解更多 MCP/A2A/NLWeb 嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者交流，參加問答時段並獲得 AI 代理相關疑問解答。

## 相關資源

- [MCP 初學者指南](https://aka.ms/mcp-for-beginners)  
- [MCP 文件](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb 倉庫](https://github.com/nlweb-ai/NLWeb)
- [Microsoft 代理框架](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## 前一課

[產品環境中的 AI 代理](../10-ai-agents-production/README.md)

## 下一課

[AI 代理的上下文工程](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->