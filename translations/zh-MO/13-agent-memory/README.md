# AI 代理人的記憶 
[![代理人記憶](../../../translated_images/zh-MO/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

When discussing the unique benefits of creating AI Agents, two things are mainly discussed: the ability to call tools to complete tasks and the ability to improve over time. Memory is at the foundation of creating self-improving agent that can create better experiences for our users.

In this lesson, we will look at what memory is for AI Agents and how we can manage it and use it for the benefit of our applications.

## 介紹

本課涵蓋：

• **理解 AI 代理人的記憶**：記憶是什麼以及為何對代理人至關重要。

• **實作與儲存記憶**：為您的 AI 代理人新增記憶功能的實務方法，重點在短期與長期記憶。

• **讓 AI 代理人自我改進**：記憶如何使代理人從過去的互動中學習並隨時間改善。

## 可用實作

This lesson includes two comprehensive notebook tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: 使用 Mem0 與 Azure AI Search 以及 Microsoft Agent Framework 實作記憶功能

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: 使用 Cognee 實作結構化記憶，自動建立由 向量嵌入 (embeddings) 支援的知識圖譜、視覺化圖譜，並進行智慧型檢索

## 學習目標

完成本課後，您將會知道如何：

• **區分各種 AI 代理人記憶類型**，包括工作記憶、短期記憶與長期記憶，以及像個人設定（persona）和情節記憶（episodic）等專門形式。

• **為 AI 代理人實作並管理短期與長期記憶**，使用 Microsoft Agent Framework，並運用像 Mem0、Cognee、Whiteboard memory 等工具，以及整合 Azure AI Search。

• **了解使 AI 代理人自我改進的原則**，以及健全的記憶管理系統如何促進持續學習與適應。

## 理解 AI 代理人的記憶

本質上，**AI 代理人的記憶指的是使其能保留並回憶資訊的機制**。這些資訊可以是對話的具體細節、使用者偏好、過去的行為，甚至是學到的模式。

沒有記憶的 AI 應用通常是無狀態的，意即每次互動都從頭開始。這會導致重複且令人挫折的使用者體驗，因為代理人會「忘記」先前的上下文或偏好。

### 為何記憶很重要？

代理人的智慧與其回憶並運用過去資訊的能力息息相關。記憶讓代理人能夠：

• **反思性**：從過去的行動與結果中學習。

• **互動性**：在持續進行的對話中維持上下文。

• **主動與反應性**：根據歷史資料預測需求或做出適當回應。

• **自主性**：藉由調用已儲存的知識，更獨立地運作。

實作記憶的目標是讓代理人更 **可靠且更有能力**。

### 記憶類型

#### 工作記憶

可以把它想像成代理人在單一進行中任務或思考過程中使用的一張草稿紙。它儲存計算下一步所需的即時資訊。

對 AI 代理人來說，工作記憶通常擷取對話中最相關的資訊，即使完整對話歷史很長或被截斷。它專注於抽取關鍵元素，例如需求、提案、決策與行動。

**工作記憶示例**

在旅遊訂票代理人的情境中，工作記憶可能會擷取使用者當前的請求，例如「我想預訂一趟去巴黎的旅程」。這項特定需求被保存在代理人的即時上下文中，以引導目前的互動。

#### 短期記憶

這種類型的記憶會在單次對話或工作階段期間保留資訊。它是目前聊天的上下文，讓代理人可以回溯到對話中的先前回合。

**短期記憶示例**

如果使用者問「飛去巴黎的機票會多少錢？」然後接著問「那裏的住宿呢？」，短期記憶確保代理人知道「那裏」在同一次對話中是指「巴黎」。

#### 長期記憶

這是會在多次對話或工作階段之間持續存在的資訊。它讓代理人能在較長時間內記住使用者偏好、歷史互動或一般性知識。這對個人化服務很重要。

**長期記憶示例**

長期記憶可能會記住像「Ben 喜歡滑雪和戶外活動、喜歡能看到山景的咖啡，以及因為過往受傷希望避免高難度滑雪坡道」等資訊。這些從先前互動中得知的資訊會影響未來旅遊規劃時的建議，使其高度客製化。

#### 角色記憶

這種專門的記憶類型幫助代理人發展一致的「個性」或「角色設定」。它允許代理人記住關於自己或其預期角色的細節，使互動更流暢且更有焦點。

**角色記憶示例**
如果旅遊代理人被設計成為一位「滑雪專家規劃師」，角色記憶可能會強化這個角色，使其回應帶有專家的語氣與知識。

#### 工作流程／情節記憶

這類記憶儲存代理人在處理複雜任務時所採取的步驟序列，包括成功與失敗。它像是記住特定的「片段」或過去經驗，以便從中學習。

**情節記憶示例**

如果代理人嘗試預訂某班航班但因為無座而失敗，情節記憶可以記錄這個失敗，使代理人在後續嘗試時能嘗試替代航班或以更有根據的方式告知使用者該問題。

#### 實體記憶

這涉及從對話中擷取並記住特定實體（例如人、地點或事物）與事件。它讓代理人能建立對所討論關鍵要素的結構化理解。

**實體記憶示例**

從一段關於過去旅程的對話中，代理人可能會擷取「Paris」、「Eiffel Tower」以及「在 Le Chat Noir 餐廳用晚餐」等實體。在未來的互動中，代理人就可以回想起「Le Chat Noir」並主動提出幫忙重新訂位。

#### 結構化 RAG（檢索增強生成）

雖然 RAG 是一種較廣泛的技術，但「結構化 RAG」被突顯為一種強大的記憶技術。它從各種來源（對話、電子郵件、影像）擷取密集且結構化的資訊，並用以提升回應的精確性、召回率與速度。不同於僅仰賴語意相似度的經典 RAG，結構化 RAG 處理資訊的內在結構。

**結構化 RAG 範例**

結構化 RAG 並非只匹配關鍵字，它可以從郵件中解析航班細節（目的地、日期、時間、航空公司）並以結構化方式儲存。這使得可以進行像「我在星期二預訂了哪班去巴黎的航班？」這樣精確的查詢。

## 實作與儲存記憶

為 AI 代理人實作記憶涉及系統性的**記憶管理**流程，包括產生、儲存、檢索、整合、更新，甚至「遺忘」（或刪除）資訊。檢索是一個特別關鍵的環節。

### 專門的記憶工具

#### Mem0

One way to store and manage agent memory is using specialized tools like Mem0. Mem0 works as a persistent memory layer, allowing agents to recall relevant interactions, store user preferences and factual context, and learn from successes and failures over time. The idea here is that stateless agents turn into stateful ones.

It works through a **two-phase memory pipeline: extraction and update**. First, messages added to an agent's thread are sent to the Mem0 service, which uses a Large Language Model (LLM) to summarize conversation history and extract new memories. Subsequently, an LLM-driven update phase determines whether to add, modify, or delete these memories, storing them in a hybrid data store that can include vector, graph, and key-value databases. This system also supports various memory types and can incorporate graph memory for managing relationships between entities.

#### Cognee

Another powerful approach is using **Cognee**, an open-source semantic memory for AI agents that transforms structured and unstructured data into queryable knowledge graphs backed by embeddings. Cognee provides a **dual-store architecture** combining vector similarity search with graph relationships, enabling agents to understand not just what information is similar, but how concepts relate to each other.

It excels at **hybrid retrieval** that blends vector similarity, graph structure, and LLM reasoning - from raw chunk lookup to graph-aware question answering. The system maintains **living memory** that evolves and grows while remaining queryable as one connected graph, supporting both short-term session context and long-term persistent memory.

The Cognee notebook tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstrates building this unified memory layer, with practical examples of ingesting diverse data sources, visualizing the knowledge graph, and querying with different search strategies tailored to specific agent needs.

### Storing Memory with RAG

Beyond specialized memory tools like mem0 , you can leverage robust search services like **Azure AI Search as a backend for storing and retrieving memories**, especially for structured RAG.

This allows you to ground your agent's responses with your own data, ensuring more relevant and accurate answers. Azure AI Search can be used to store user-specific travel memories, product catalogs, or any other domain-specific knowledge.

Azure AI Search supports capabilities like **Structured RAG**, which excels at extracting and retrieving dense, structured information from large datasets like conversation histories, emails, or even images. This provides "superhuman precision and recall" compared to traditional text chunking and embedding approaches.

## 讓 AI 代理人自我改進

A common pattern for self-improving agents involves introducing a **"knowledge agent"**. This separate agent observes the main conversation between the user and the primary agent. Its role is to:

1. **識別有價值的資訊**：判斷對話中的哪一部分值得作為一般知識或特定使用者偏好來儲存。

2. **擷取與摘要**：從對話中萃取出核心的學習或偏好。

3. **儲存到知識庫**：將擷取出的資訊持久化，通常會儲存在向量資料庫，以便日後檢索。

4. **增強未來查詢**：當使用者發起新查詢時，知識代理人會檢索相關的儲存資訊並附加至使用者的提示，為主要代理人提供關鍵上下文（類似於 RAG）。

### 記憶的優化策略

• **延遲管理**：為避免拖慢使用者互動，可先使用較便宜且較快速的模型來快速檢查資訊是否值得儲存或檢索，僅在必要時才呼叫較複雜的擷取／檢索程序。

• **知識庫維護**：對於成長中的知識庫，較少被使用的資訊可遷移到「冷儲存」，以控制成本。

## 對代理人記憶還有更多疑問嗎？

加入[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者交流、參加線上答疑時間，並獲得您關於 AI 代理人的問題解答。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件已使用 AI 翻譯服務「Co-op Translator」(https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但自動翻譯可能包含錯誤或不準確之處。原始語言的文件應視為具權威性的版本。對於重要資訊，建議委託專業人工翻譯。對於因使用本翻譯而導致的任何誤解或錯誤詮釋，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->