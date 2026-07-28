# 使用 Microsoft Agent Framework Workflow 建構多智能體應用程式

本教程將引導您了解並建構使用 Microsoft Agent Framework 的多智能體應用程式。我們將探討多智能體系統的核心概念，深入探討框架中 Workflow 組件的架構，並透過 Python 和 .NET 的實際範例展示不同的工作流程模式。

## 1\. 了解多智能體系統

AI 智能體是一種超越標準大型語言模型（LLM）能力的系統。它能感知環境、做出決策並採取行動以達成特定目標。多智能體系統則涉及多個這樣的智能體合作解決單一智能體難以或無法獨立解決的問題。

### 常見應用場景

  * <strong>複雜問題解決</strong>：將大型任務（例如規劃公司全體活動）細分成多個子任務，由專門智能體負責（例如預算智能體、物流智能體、市場營銷智能體）。
  * <strong>虛擬助理</strong>：主助理智能體分派排程、研究和預訂等任務給其他專門智能體。
  * <strong>自動化內容創作</strong>：一個智能體撰寫草稿，另一個智能體審核內容的準確性與語氣，第三個智能體負責發佈。

### 多智能體模式

多智能體系統可以組織成數種模式，決定它們之間如何互動：

  * <strong>順序式</strong>：智能體依預定順序工作，如生產線般。前一智能體的輸出成為下一智能體的輸入。
  * <strong>並行式</strong>：智能體同時在不同任務部分工作，最終結果會被彙總。
  * <strong>條件式</strong>：根據智能體輸出，工作流程走不同路徑，類似 if-then-else 陳述。

## 2\. Microsoft Agent Framework Workflow 架構

Agent Framework 的工作流程系統是一個先進的協調引擎，設計用來管理多個智能體之間的複雜互動。它建立在基於圖形的架構上，採用[Pregel風格執行模型](https://kowshik.github.io/JPregel/pregel_paper.pdf)，處理過程以稱為「超步（supersteps）」的同步步驟進行。

### 核心組件

架構由三個主要部分組成：

1.  <strong>執行者</strong>：這是基本的處理單位。在範例中，`Agent` 是一種執行者。每個執行者可有多個訊息處理器，根據接收到的訊息類型自動調用。
2.  <strong>邊緣</strong>：定義訊息在執行者間的路徑。邊緣可具條件，允許訊息在工作流程圖中動態路由。
3.  <strong>工作流程</strong>：協調整個流程，管理執行者、邊緣及執行順序，確保訊息按正確順序處理並串流事件以便觀察。

*說明工作流程系統核心組件的示意圖。*

此結構允許透過基本模式如順序串聯、分流合併並行處理，及條件切換邏輯建構穩健且可擴充的應用程式。

## 3\. 實作範例與程式碼分析

現在，讓我們來探討如何使用該框架實作不同工作流程模式。我們將同時查看 Python 與 .NET 的範例程式碼。

### 案例 1：基本順序工作流程

這是最簡單的模式，其中一個智能體的輸出直接傳給另一個。情境是旅館的 `FrontDesk` 智能體提供旅行建議，接著由 `Concierge` 智能體審核。

*基本 FrontDesk -> Concierge 工作流程示意圖。*

#### 情境背景

一位旅客請求巴黎的推薦。

1.  為簡潔設計的 `FrontDesk` 智能體建議前往羅浮宮。
2.  強調真實體驗的 `Concierge` 智能體收到建議後，審查並回饋，推薦更本地化、較少觀光客的選擇。

#### Python 實作分析

Python 範例中，首先定義並建立兩個智能體，各具特定指令。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# 定義代理角色和指令
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# 創建代理實例
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

接著使用 `WorkflowBuilder` 建構圖。`front_desk_agent` 設為起點，並建立一條邊連接其輸出至 `reviewer_agent`。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

最後以初始使用者提示執行工作流程。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run 執行工作流程；get_outputs() 返回輸出執行者的結果。
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) 實作分析

.NET 的實作邏輯非常相似。首先定義智能體名稱及指令常數。

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

使用 `AzureOpenAIClient`(Responses API) 建立智能體後，再用 `WorkflowBuilder` 定義順序流程，加入一條從 `frontDeskAgent` 到 `reviewerAgent` 的邊緣。

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

使用者訊息觸發工作流程執行，結果串流回傳。

### 案例 2：多階段順序工作流程

此模式延伸基本序列，涵蓋更多智能體，適合需要多階段精煉或轉換的流程。

#### 情境背景

使用者提供一張客廳圖片並請求家具報價。

1.  <strong>銷售智能體</strong>：識別圖片中的家具物件並產生清單。
2.  <strong>價格智能體</strong>：根據清單，提供詳細價格分解，涵蓋預算、中階與高端選項。
3.  <strong>報價智能體</strong>：接收帶價格的清單，並格式化成 Markdown 正式報價文件。

*Sales -> Price -> Quote 工作流程示意圖。*

#### Python 實作分析

定義三個具特定角色的智能體。使用 `add_edge` 建立串聯鏈：`sales_agent` -> `price_agent` -> `quote_agent`。

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# 建立三個專門的代理
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# 建立序列工作流程
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

輸入為包含文字和圖片 URI 的 `ChatMessage`。框架負責將每個智能體的輸出傳遞給下一個，直到產生最終報價。

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

.NET 範例與 Python 版本類似。三個智能體（`salesagent`、`priceagent`、`quoteagent`）被建立，並由 `WorkflowBuilder` 順序連接。

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

使用者訊息包含圖片資料（位元組）與文本提示。使用 `InProcessExecution.RunStreamingAsync` 方法執行流程，並從串流中捕獲最終輸出。

### 案例 3：並行工作流程

當任務可同時進行以節省時間時使用此模式。涉及分流（fan-out）給多個智能體，與合流（fan-in）彙整結果。

#### 情境背景

使用者請求規劃西雅圖之旅。

1.  **調度者（分流）**：同時將使用者請求送給兩個智能體。
2.  <strong>研究智能體</strong>：調查景點、氣候及西雅圖十二月旅遊注意事項。
3.  <strong>規劃智能體</strong>：獨立製作詳細的一日行程表。
4.  **彙整者（合流）**：收集兩方輸出，並一同呈現作為最終結果。

*同時進行的研究智能體與規劃智能體工作流程示意圖。*

#### Python 實作分析

`ConcurrentBuilder` 簡化此模式創建。只需列出參與的智能體，建構器自動生成必要的分流與合流邏輯。

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder 處理分支展開/合併邏輯
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# 執行工作流程
events = await workflow.run("Plan a trip to Seattle in December")
```

框架確保 `research_agent` 與 `plan_agent` 並行執行，最終輸出會被收集到列表中。

#### .NET (C\#) 實作分析

在 .NET 中，此模式需要更明確的定義。自訂執行者（`ConcurrentStartExecutor` 與 `ConcurrentAggregationExecutor`）負責實現分流與合流邏輯。

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

然後使用 `WorkflowBuilder` 的 `AddFanOutEdge` 與 `AddFanInEdge` 建構包含這些自訂執行者與智能體的圖。

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### 案例 4：條件工作流程

條件工作流程引入分支邏輯，允許系統根據中間結果選擇不同路徑。

#### 情境背景

此工作流程自動化技術教學的創作與發佈。

1.  <strong>布道者智能體</strong>：根據提供的綱要與 URL 撰寫教學草稿。
2.  <strong>內容審核智能體</strong>：審查草稿，檢查字數是否超過 200 字。
3.  <strong>條件分支</strong>：
      * **若通過（`Yes`）**：流程繼續至 `Publisher-Agent`。
      * **若不通過（`No`）**：流程停止並輸出拒絕原因。
4.  <strong>發佈智能體</strong>：草稿通過後，該智能體將內容儲存為 Markdown 文件。

#### Python 實作分析

本範例使用自訂函式 `select_targets` 實現條件邏輯。此函式傳入 `add_multi_selection_edge_group`，根據審核結果 `review_result` 欄位指導工作流程。

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# 此函數根據審查結果決定下一步
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # 如果通過，則進入 'save_draft' 執行器
        return [save_draft_id]
    else:
        # 如果被拒絕，則進入 'handle_review' 執行器以報告失敗
        return [handle_review_id]

# 工作流程構建器使用選擇函數進行路由
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

自訂執行者如 `to_reviewer_result` 用於解析智能體的 JSON 輸出，轉換成強型別物件供選擇函式檢查。

#### .NET (C\#) 實作分析

.NET 版本採用類似策略，使用判斷函式 `Func<object?, bool>` 以檢查 `ReviewResult` 物件的 `Result` 屬性。

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

`AddEdge` 方法的 `condition` 參數允許 `WorkflowBuilder` 建立分支路徑。若 `GetCondition(expectedResult: "Yes")` 回傳 true，流程才會走往 `publishExecutor`，否則轉往 `sendReviewerExecutor`。

## 結論

Microsoft Agent Framework Workflow 提供穩健且彈性的基礎，來協調複雜的多智能體系統。藉由運用基於圖形的架構與核心組件，開發者能以 Python 與 .NET 設計並實作複雜且先進的工作流程。無論您的應用程式需要簡單的順序處理、平行執行，或動態條件邏輯，此框架皆提供強大、可擴充且型別安全的 AI 解決方案建置工具。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->