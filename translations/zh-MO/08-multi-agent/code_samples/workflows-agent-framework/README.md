# 使用 Microsoft Agent Framework Workflow 建立多代理應用程式

本教學將帶領你了解並建立使用 Microsoft Agent Framework 的多代理應用程式。我們將探討多代理系統的核心概念，深入了解該框架的 Workflow 組件架構，並透過 Python 和 .NET 的實際範例，展示不同工作流程模式的實作。

## 1\. 了解多代理系統

AI 代理（Agent）是一個超越標準大型語言模型（LLM）功能的系統。它能感知環境、做出決策並採取行動以達成特定目標。多代理系統則包含多個此類代理協同合作，解決單一代理無法單獨應付的問題。

### 常見應用場景

  * <strong>複雜問題解決</strong>：將大型任務（例如規劃公司整體活動）拆分為多個子任務，由專門代理負責處理（如預算代理、物流代理、市場行銷代理）。
  * <strong>虛擬助理</strong>：主要助理代理委派排程、研究與預訂任務給其他專門代理。
  * <strong>自動內容創作</strong>：一個代理起草內容，另一個代理檢視內容的準確性與語氣，第三個代理負責發布。

### 多代理模式

多代理系統可以組織為多種互動模式，決定它們的互動方式：

  * <strong>順序式</strong>：代理依預定順序工作，如組裝線。前一個代理的輸出成為下一代理的輸入。
  * <strong>並行式</strong>：代理同時處理任務不同部分，最後聚合結果。
  * <strong>條件式</strong>：根據代理輸出而走不同路徑，類似 if-then-else 陳述式。

## 2\. Microsoft Agent Framework Workflow 架構

Agent Framework 的工作流程系統是一個進階的協調引擎，用於管理多代理間複雜互動。其採用基於圖形的架構，使用 [Pregel風格執行模型](https://kowshik.github.io/JPregel/pregel_paper.pdf)，處理透過稱為「超步」（supersteps）的同步階段進行。

### 核心組件

架構包含三大部分：

1.  **執行者（Executors）**：基礎處理單元。在範例中，`Agent` 是執行者的一種。每個執行者可擁有多個訊息處理器，依收訊息類型自動呼叫。
2.  **邊（Edges）**：定義訊息在執行者間的路徑。邊可設定條件，實現資訊於工作流程圖中動態路由。
3.  **工作流程（Workflow）**：協調整個過程，管理執行者、邊和執行流程。確保訊息依正確順序處理，並串流事件以便觀察。

*此圖示說明工作流程系統的核心組件。*

此結構支援建立穩健且具擴充性的應用，包含順序鏈式、放射/聚合並行處理，以及條件選擇流程等基礎模式。

## 3\. 實作範例與程式碼分析

現在，我們來探討如何運用此框架實作不同工作流程模式。每個範例會展示 Python 和 .NET 版本的程式碼。

### 範例 1：基本順序工作流程

這是最簡單的模式，一個代理的輸出直接傳遞給下一個代理。我們的情境是飯店的 `FrontDesk` 代理提供旅遊建議，接著由 `Concierge` 代理審查。

*基本 FrontDesk → Concierge 工作流程示意圖。*

#### 情境背景

一位旅客詢問巴黎的推薦。

1.  `FrontDesk` 代理提供簡潔建議，推薦參觀羅浮宮博物館。
2.  `Concierge` 代理重視真實體驗，收到建議後審核並給出回饋，建議更在地且少觀光客的替代方案。

#### Python 實作分析

Python 範例中，首先定義與建立兩個代理，分別帶有特定指令。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# 定義代理角色與指令
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# 建立代理實例
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

接著使用 `WorkflowBuilder` 建構工作流程圖。設定 `front_desk_agent` 為起點，並建立一條邊將此代理輸出連接到 `reviewer_agent`。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

最後以初始使用者提示執行工作流程。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run 執行工作流程；get_outputs() 返回輸出執行器的結果。
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) 實作分析

.NET 的實作邏輯與此類似。先定義代理名稱及指令為常數。

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

利用 `AzureOpenAIClient`（Responses API）建立代理，再用 `WorkflowBuilder` 將 `frontDeskAgent` 與 `reviewerAgent` 透過邊連接起來，完成順序流程。

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

使用者訊息啟動工作流程，並串流回傳結果。

### 範例 2：多步驟順序工作流程

此模式將基本序列延伸至多個代理，適用於需多階段修正或轉換的流程。

#### 情境背景

使用者提供客廳圖像，要求家具報價。

1.  <strong>銷售代理</strong>：辨識圖中家具並建立清單。
2.  <strong>價格代理</strong>：根據清單提供詳細價格細目，包含經濟型、中階與高階選項。
3.  <strong>報價代理</strong>：接收定價清單，轉換成正式 Markdown 報價文件。

*銷售 → 價格 → 報價工作流程示意圖。*

#### Python 實作分析

定義三個專業代理。使用 `add_edge` 建立鏈式流程：`sales_agent` → `price_agent` → `quote_agent`。

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# 建立三個專門代理
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# 建立順序工作流程
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

輸入為包含文字與影像 URI 的 `ChatMessage`。框架自動將每個代理的輸出傳給下一個，直到產生最終報價。

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# 用戶訊息同時包含文字同圖片
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# 執行工作流程
events = await workflow.run(message)
```

#### .NET (C\#) 實作分析

.NET 範例與 Python 類似。建立三個代理（`salesagent`, `priceagent`, `quoteagent`），再由 `WorkflowBuilder` 依序串接。

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

使用者訊息包含影像資料（位元組）與文字提示，並透過 `InProcessExecution.RunStreamingAsync` 開始流程，從串流中取得最終輸出。

### 範例 3：並行工作流程

此模式適合可同時執行的任務以節省時間。包含多個代理的「放射」（fan-out）與結果的「聚合」（fan-in）。

#### 情境背景

使用者要求規劃前往西雅圖的行程。

1.  **分派者（Fan-Out）**：同時將請求發送給兩個代理。
2.  <strong>研究代理</strong>：調查西雅圖十二月的景點、氣候及重要提醒。
3.  <strong>規劃代理</strong>：獨立制定詳細每日行程。
4.  **聚合者（Fan-In）**：收集研究者與規劃者輸出，合併成最終結果。

*並行的研究者與規劃者工作流程示意圖。*

#### Python 實作分析

`ConcurrentBuilder` 簡化了建立此模式。只要列出參與代理，建構器自動生成所需的放射與聚合邏輯。

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder 處理扇出/扇入邏輯
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# 執行工作流程
events = await workflow.run("Plan a trip to Seattle in December")
```

框架確保 `research_agent` 與 `plan_agent` 平行執行，最終輸出聚合成清單。

#### .NET (C\#) 實作分析

在 .NET 中，此模式需更明確定義。自訂執行者（`ConcurrentStartExecutor` 與 `ConcurrentAggregationExecutor`）用於處理放射與聚合邏輯。

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

之後由 `WorkflowBuilder` 使用 `AddFanOutEdge` 與 `AddFanInEdge`，利用這些自訂執行者和代理組成圖表。

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### 範例 4：條件式工作流程

條件式工作流程引入分支邏輯，允許系統根據中間結果走不同路徑。

#### 情境背景

此工作流程自動建立並發布技術教學。

1.  <strong>推廣代理</strong>：依給定大綱與 URL 撰寫教學草稿。
2.  <strong>內容審核代理</strong>：審核草稿，檢查是否超過 200 字。
3.  <strong>條件分支</strong>：
      * **若通過（`Yes`）**：流程繼續至 `Publisher-Agent`。
      * **若拒絕（`No`）**：流程終止並輸出拒絕理由。
4.  <strong>發布代理</strong>：若草稿通過審核，將內容存成 Markdown 文件。

#### Python 實作分析

範例中使用自訂函式 `select_targets` 實現條件邏輯。該函式被傳入 `add_multi_selection_edge_group`，依審核輸出中的 `review_result` 欄位決定流程分支。

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# 此函數根據審核結果決定下一步驟
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # 如獲批准，繼續執行「save_draft」執行器
        return [save_draft_id]
    else:
        # 如被拒絕，繼續執行「handle_review」執行器以回報失敗
        return [handle_review_id]

# 工作流程建構器使用選擇函數進行路由
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # 多選邊緣實現條件邏輯
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

自訂執行者如 `to_reviewer_result` 用於解析代理回傳的 JSON 輸出，轉換成強型別物件供選擇函式檢查。

#### .NET (C\#) 實作分析

.NET 範例使用近似方法與條件函數。定義 `Func<object?, bool>` 檢查 `ReviewResult` 物件的 `Result` 屬性。

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

`AddEdge` 方法的條件參數 (`condition`) 讓 `WorkflowBuilder` 建立分支路徑。當 `GetCondition(expectedResult: "Yes")` 回傳 true 時，流程會走向 `publishExecutor`，否則走向 `sendReviewerExecutor`。

## 結論

Microsoft Agent Framework Workflow 提供穩健且靈活的基礎，協調複雜的多代理系統。藉由其基於圖形的架構與核心組件，開發者可在 Python 與 .NET 中設計並實作高階工作流程。無論應用需求是簡單順序處理、並行執行或動態條件邏輯，此框架均提供強大、可擴充且類型安全的 AI 驅動解決方案工具。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->