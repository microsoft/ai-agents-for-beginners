# 使用代理協議 (MCP、A2A 與 NLWeb)

[![代理協議](../../../translated_images/zh-TW/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(點擊上方圖片觀看本課程影片)_

隨著 AI 代理的使用增長，對於能確保標準化、安全性並促進開放創新的協議需求也隨之增加。在本課程中，我們將介紹三個旨在滿足此需求的協議：Model Context Protocol (MCP)、Agent to Agent (A2A) 與 Natural Language Web (NLWeb)。

## 簡介

在本課程中，我們將涵蓋：

• MCP 如何允許 AI 代理存取外部工具與資料以完成使用者任務。

• A2A 如何使不同 AI 代理之間進行通訊與協作。

• NLWeb 如何為任何網站帶來自然語言介面，使 AI 代理能夠發現並與內容互動。

## 學習目標

• **識別** MCP、A2A 與 NLWeb 在 AI 代理情境中的核心目的與優點。

• **說明** 每個協議如何促進 LLM、工具與其他代理之間的通訊與互動。

• **辨識** 每個協議在建構複雜代理系統時所扮演的不同角色。

## Model Context Protocol

**Model Context Protocol (MCP)** 是一個開放標準，提供應用程式向 LLM 提供上下文與工具的標準化方式。這使得一個「通用介面」可以以一致的方式連接不同的資料來源與工具，供 AI 代理使用。

讓我們來看看 MCP 的組成部分、相較於直接使用 API 的好處，以及 AI 代理如何使用 MCP 伺服器的範例。

### MCP 核心組成

MCP 採用 **客戶端-伺服器架構**，核心組成包括：

• **Hosts** 是 LLM 應用程式（例如像 VSCode 的程式碼編輯器），負責啟動與 MCP Server 的連線。

• **Clients** 是宿主應用程式內的元件，維持與伺服器的一對一連線。

• **Servers** 是對外揭露特定能力的輕量程式。

協議中包含三個核心原語，這些即為 MCP Server 的能力：

• **Tools**：這些是 AI 代理可以呼叫以執行動作的離散操作或函式。例如，氣象服務可能會公開一個「get weather」工具，或電商伺服器可能會公開一個「purchase product」工具。MCP 伺服器會在其能力清單中公告每個工具的名稱、描述及輸入/輸出架構。

• **Resources**：這些是 MCP 伺服器能提供的唯讀資料項或文件，客戶端可以按需取得。範例包括檔案內容、資料庫記錄或日誌檔。Resources 可以是文字（例如程式碼或 JSON）或二進位（例如影像或 PDF）。

• **Prompts**：這些是預定義的範本，提供建議提示，允許更複雜的工作流程。

### MCP 的好處

MCP 為 AI 代理提供顯著的優勢：

• **動態工具探索**：代理可以動態地從伺服器接收可用工具清單及其功能描述。這與傳統 API 不同，後者通常需要靜態的整合程式碼，任何 API 變更都需要程式碼更新。MCP 提供一次整合的方式，使適應性更高。

• **跨 LLM 的互通性**：MCP 可跨不同的 LLM 運作，提供在核心模型間切換以評估更好效能的彈性。

• **標準化安全性**：MCP 包含標準的認證方法，在新增對其他 MCP 伺服器的存取時可提升可擴充性。這比管理多種傳統 API 的金鑰與認證類型簡單許多。

### MCP 範例

![MCP 圖示](../../../translated_images/zh-TW/mcp-diagram.e4ca1cbd551444a1.webp)

想像使用由 MCP 驅動的 AI 助手要幫使用者訂機票。

1. **連線**：AI 助手（MCP 客戶端）連接到航空公司提供的 MCP 伺服器。

2. **工具探索**：客戶端問航空公司的 MCP 伺服器：「你們有哪些可用工具？」伺服器回應像是「search flights」和「book flights」等工具。

3. **工具呼叫**：接著你請 AI 助手：「請幫我搜尋從 Portland 到 Honolulu 的航班。」AI 助手利用其 LLM 判斷需要呼叫「search flights」工具，並將相關參數（出發地、目的地）傳給 MCP 伺服器。

4. **執行與回應**：MCP 伺服器作為包裝器，實際呼叫航空公司的內部訂票 API，然後接收航班資訊（例如 JSON 資料）並回傳給 AI 助手。

5. **後續互動**：AI 助手呈現航班選項。當你選擇航班後，助理可能會對相同的 MCP 伺服器呼叫「book flight」工具，完成訂票流程。

## Agent-to-Agent Protocol (A2A)

當 MCP 著重於將 LLM 連接到工具時，**Agent-to-Agent (A2A) 協議** 更進一步，允許不同 AI 代理之間的通訊與協作。A2A 將不同組織、環境與技術棧的 AI 代理連接起來，以完成共同任務。

我們將檢視 A2A 的組件與好處，並以旅行應用為例說明其應用。

### A2A 核心組件

A2A 著重於促成代理之間的通訊並讓它們協同工作以完成使用者的子任務。協議的每個組件都為此做出貢獻：

#### Agent Card

類似於 MCP 伺服器分享工具清單的方式，Agent Card 包含：
- The Name of the Agent .
- 一個 **描述其一般任務** 的說明。
- 一個 **具體技能清單**，附帶描述以幫助其他代理（甚至人類使用者）了解何時以及為何應呼叫該代理。
- 代理的 **目前 Endpoint URL**
- 代理的 **版本** 與 **能力**，例如串流回應與推播通知。

#### Agent Executor

Agent Executor 負責 **將使用者聊天的上下文傳遞給遠端代理**，遠端代理需要這些內容以理解需完成的任務。在 A2A 伺服器中，代理會使用其自己的大型語言模型 (LLM) 來解析傳入的請求，並使用其內部工具執行任務。

#### Artifact

一旦遠端代理完成請求的任務，其工作成果會被建立為 artifact。artifact **包含代理工作結果**、**已完成工作的描述**，以及透過協議傳送的 **文字上下文**。在 artifact 發送後，與遠端代理的連線會被關閉，直到再次需要。

#### Event Queue

此組件用於 **處理更新與傳遞訊息**。在生產環境中，對於代理系統來說，它特別重要，以防在任務完成前代理之間的連線被關閉，尤其當任務完成時間可能較長時。

### A2A 的好處

• **強化協作**：它使來自不同供應商與平台的代理能夠互動、分享上下文並共同工作，促進跨傳統斷裂系統的無縫自動化。

• **模型選擇的彈性**：每個 A2A 代理可以決定使用哪個 LLM 來處理它的請求，允許每個代理使用最佳化或微調過的模型，不像某些 MCP 情境僅有單一 LLM 連線。

• **內建認證**：認證直接整合在 A2A 協議中，為代理互動提供強固的安全框架。

### A2A 範例

![A2A 圖示](../../../translated_images/zh-TW/A2A-Diagram.8666928d648acc26.webp)

讓我們擴展旅行訂票情境，但這次使用 A2A。

1. **使用者向多代理發出請求**：使用者與一個「Travel Agent」A2A 客戶端/代理互動，或許說：「請幫我下週訂一趟完整的 Honolulu 旅程，包含機票、飯店與租車」。

2. **Travel Agent 的協調**：Travel Agent 收到此複雜請求。它使用其 LLM 推理任務並決定需要與其他專門代理互動。

3. **代理間通訊**：Travel Agent 使用 A2A 協議連接到下游代理，例如由不同公司建立的「Airline Agent」、「Hotel Agent」與「Car Rental Agent」。

4. **委派任務執行**：Travel Agent 將特定任務發送給這些專門代理（例如「找去 Honolulu 的航班」、「訂一間飯店」、「租一台車」）。每個專門代理皆運行自己的 LLM 並使用自己的工具（這些工具本身也可能是 MCP 伺服器），執行其負責的訂票部分。

5. **整合回應**：一旦所有下游代理完成任務，Travel Agent 將結果（航班資訊、飯店確認、租車訂單）彙整，並以聊天形式將完整回應送回使用者。

## Natural Language Web (NLWeb)

網站長期以來一直是使用者存取互聯網上資訊與資料的主要方式。

讓我們來看看 NLWeb 的不同組成、NLWeb 的好處，並以我們的旅行應用說明 NLWeb 的運作範例。

### NLWeb 的組成

- **NLWeb 應用程式（核心服務程式碼）**：處理自然語言問題的系統。它連接平台的不同部分以產生回應。你可以將它視為 **驅動網站自然語言功能的引擎**。

- **NLWeb 協議**：這是一套 **針對網站的自然語言互動的基本規則**。它以 JSON 格式（通常使用 Schema.org）回傳回應。其目的在於為「AI 網路」建立一個簡單的基礎，就像 HTML 讓線上文件分享成為可能一樣。

- **MCP Server (Model Context Protocol Endpoint)**：每個 NLWeb 設定同時也可以作為 **MCP 伺服器**。這表示它能 **與其他 AI 系統分享工具（例如「ask」方法）與資料**。實務上，這使得網站的內容與能力可被 AI 代理使用，讓網站成為更廣泛「代理生態系」的一部分。

- **Embedding Models**：這些模型用於 **將網站內容轉換為稱為向量（embeddings）的數值表示**。這些向量以一種電腦能夠比較與搜尋的方式捕捉意義。它們儲存在特殊資料庫中，使用者可以選擇想使用的 embedding 模型。

- **向量資料庫（檢索機制）**：此資料庫 **儲存網站內容的 embeddings**。當有人提出問題時，NLWeb 會檢查向量資料庫以快速找出最相關的資訊。它會提供一個依相似度排序的可能答案清單。NLWeb 可搭配不同的向量儲存系統，例如 Qdrant、Snowflake、Milvus、Azure AI Search 與 Elasticsearch。

### NLWeb 範例

![NLWeb 圖示](../../../translated_images/zh-TW/nlweb-diagram.c1e2390b310e5fe4.webp)

再回到我們的旅行訂票網站，但這次由 NLWeb 提供動力。

1. **資料擷取**：旅行網站現有的產品目錄（例如航班清單、飯店描述、旅遊套裝行程）使用 Schema.org 格式化或透過 RSS 載入。NLWeb 的工具會擷取這些結構化資料、建立 embeddings，並將它們儲存在本地或遠端的向量資料庫中。

2. **自然語言查詢（人類）**：使用者造訪網站，並不透過導覽選單，而是在聊天介面輸入：「幫我找下週在 Honolulu 有游泳池且適合家庭入住的飯店」。

3. **NLWeb 處理**：NLWeb 應用程式接收此查詢。它將查詢發送給 LLM 以進行理解，並同時在其向量資料庫中搜尋相關的飯店清單。

4. **準確結果**：LLM 協助詮釋資料庫的搜尋結果，根據「適合家庭」、「有游泳池」與「Honolulu」等條件識別最佳匹配，然後格式化自然語言回應。關鍵是，回應會參照網站目錄中的實際飯店，而非憑空捏造資訊。

5. **AI 代理互動**：因為 NLWeb 同時作為 MCP 伺服器，外部的 AI 旅行代理也可以連接到該網站的 NLWeb 實例。AI 代理可以使用 `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")` MCP 方法直接查詢該網站。NLWeb 實例會處理此查詢，利用其餐廳資訊資料庫（若已載入），並回傳結構化的 JSON 回應。

### 對 MCP/A2A/NLWeb 有更多疑問嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者交流、參加辦公時間並獲得你的 AI 代理相關問題的解答。

## 資源

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件為使用 AI 翻譯服務 Co-op Translator (https://github.com/Azure/co-op-translator) 所翻譯。雖然我們力求準確，但自動翻譯可能包含錯誤或不精確之處。原始語言版本的文件應被視為具權威性的依據。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或錯誤詮釋負任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->