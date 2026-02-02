# 使用 Microsoft Agent Framework Workflow 建構多代理應用程式

本教程將引導您了解並使用 Microsoft Agent Framework 建構多代理應用程式。我們將探討多代理系統的核心概念，深入了解框架 Workflow 元件的架構，並通過 Python 和 .NET 的實際範例展示不同的工作流程模式。

## 1\. 了解多代理系統

AI 代理是一種超越標準大型語言模型 (LLM) 功能的系統。它能感知環境、做出決策並採取行動以達成特定目標。多代理系統則涉及多個代理協作解決單一代理難以處理的問題。

### 常見應用場景

  * **複雜問題解決**：將大型任務（例如規劃公司活動）分解為由專業代理處理的小型子任務（例如預算代理、物流代理、行銷代理）。
  * **虛擬助理**：主要助理代理將排程、研究和預訂等任務委派給其他專業代理。
  * **自動化內容創作**：工作流程中，一個代理撰寫內容，另一個代理審核準確性和語調，第三個代理負責發布。

### 多代理模式

多代理系統可以按照不同的模式組織，這些模式決定了代理之間的互動方式：

  * **順序模式**：代理按照預定順序工作，類似於流水線。一個代理的輸出成為下一個代理的輸入。
  * **並行模式**：代理同時處理任務的不同部分，最後將結果匯總。
  * **條件模式**：工作流程根據代理的輸出採取不同的路徑，類似於 if-then-else 語句。

## 2\. Microsoft Agent Framework Workflow 架構

Agent Framework 的工作流程系統是一個先進的編排引擎，旨在管理多代理之間的複雜互動。它基於圖形架構，使用 [Pregel-style 執行模型](https://kowshik.github.io/JPregel/pregel_paper.pdf)，處理在同步步驟中進行，稱為「超步驟」。

### 核心元件

架構由三個主要部分組成：

1.  **執行器**：這些是基本的處理單元。在我們的範例中，`Agent` 是一種執行器。每個執行器可以有多個消息處理器，根據接收到的消息類型自動調用。
2.  **邊**：定義消息在執行器之間的傳遞路徑。邊可以設置條件，允許信息通過工作流程圖進行動態路由。
3.  **工作流程**：負責編排整個過程，管理執行器、邊以及整體執行流。它確保消息按正確順序處理並流式傳輸事件以供觀察。

*一個展示工作流程系統核心元件的圖表。*

此結構允許使用基本模式（如順序鏈、並行處理的分散/匯聚，以及條件流的 switch-case 邏輯）構建穩健且可擴展的應用程式。

## 3\. 實際範例與程式碼分析

接下來，我們將探討如何使用框架實現不同的工作流程模式。我們將針對每個範例展示 Python 和 .NET 的程式碼。

### 範例 1：基本順序工作流程

這是最簡單的模式，其中一個代理的輸出直接傳遞給另一個代理。我們的場景涉及一個酒店 `FrontDesk` 代理提供旅行建議，然後由 `Concierge` 代理進行審核。

*基本 FrontDesk -\> Concierge 工作流程的圖表。*

#### 場景背景

一位旅客詢問巴黎的推薦。

1.  `FrontDesk` 代理（設計簡潔）建議參觀羅浮宮。
2.  `Concierge` 代理（注重真實體驗）接收建議，審核後提供回饋，推薦更具地方特色、非旅遊化的選擇。

#### Python 實現分析

在 Python 範例中，我們首先定義並創建兩個代理，每個代理都有特定指令。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

接著使用 `WorkflowBuilder` 構建圖形。將 `front_desk_agent` 設為起點，並創建一條邊將其輸出連接到 `reviewer_agent`。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

最後，使用初始用戶提示執行工作流程。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C\#) 實現分析

.NET 實現遵循非常相似的邏輯。首先，定義代理的名稱和指令常數。

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

使用 `OpenAIClient` 創建代理，然後使用 `WorkflowBuilder` 定義順序流程，添加一條邊從 `frontDeskAgent` 連接到 `reviewerAgent`。

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

接著使用用戶消息執行工作流程，並流式傳輸結果。

### 範例 2：多步驟順序工作流程

此模式擴展基本順序模式，包含更多代理。適合需要多階段精煉或轉換的流程。

#### 場景背景

用戶提供一張客廳的圖片並要求家具報價。

1.  **Sales-Agent**：識別圖片中的家具項目並創建清單。
2.  **Price-Agent**：根據家具清單提供詳細的價格分解，包括預算、中檔和高端選項。
3.  **Quote-Agent**：接收定價清單並將其格式化為 Markdown 格式的正式報價文件。

*Sales -\> Price -\> Quote 工作流程的圖表。*

#### Python 實現分析

定義三個代理，每個代理都有專業角色。使用 `add_edge` 構建工作流程鏈：`sales_agent` -\> `price_agent` -\> `quote_agent`。

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

輸入是一個包含文字和圖片 URI 的 `ChatMessage`。框架負責將每個代理的輸出傳遞給下一個代理，直到生成最終報價。

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# The user message contains both text and an image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Run the workflow
async for event in workflow.run_stream(message):
    ...
```

#### .NET (C\#) 實現分析

.NET 範例與 Python 版本相似。創建三個代理（`salesagent`、`priceagent`、`quoteagent`）。使用 `WorkflowBuilder` 將它們順序連接。

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

用戶消息包含圖片數據（以字節形式）和文字提示。使用 `InProcessExecution.StreamAsync` 方法啟動工作流程，並從流中捕獲最終輸出。

### 範例 3：並行工作流程

此模式適用於任務可同時執行以節省時間的情況。它涉及「分散」到多個代理和「匯聚」以匯總結果。

#### 場景背景

用戶要求規劃西雅圖旅行。

1.  **Dispatcher (分散)**：用戶請求同時發送給兩個代理。
2.  **Researcher-Agent**：研究西雅圖十二月的景點、天氣和關鍵考量。
3.  **Plan-Agent**：獨立創建詳細的每日旅行行程。
4.  **Aggregator (匯聚)**：收集研究者和規劃者的輸出，並將結果一起呈現。

*並行 Researcher 和 Planner 工作流程的圖表。*

#### Python 實現分析

`ConcurrentBuilder` 簡化了此模式的創建。只需列出參與的代理，建構器會自動創建必要的分散和匯聚邏輯。

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

框架確保 `research_agent` 和 `plan_agent` 並行執行，並將最終輸出匯集到列表中。

#### .NET (C\#) 實現分析

在 .NET 中，此模式需要更明確的定義。創建自定義執行器（`ConcurrentStartExecutor` 和 `ConcurrentAggregationExecutor`）以處理分散和匯聚邏輯。

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

使用 `WorkflowBuilder` 的 `AddFanOutEdge` 和 `AddFanInEdge` 方法構建圖形，包含這些自定義執行器和代理。

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### 範例 4：條件工作流程

條件工作流程引入分支邏輯，允許系統根據中間結果採取不同路徑。

#### 場景背景

此工作流程自動化技術教程的創建和發布。

1.  **Evangelist-Agent**：根據提供的大綱和 URL 撰寫教程草稿。
2.  **ContentReviewer-Agent**：審核草稿，檢查字數是否超過 200 字。
3.  **條件分支**：
      * **若通過 (`Yes`)**：工作流程進入 `Publisher-Agent`。
      * **若拒絕 (`No`)**：工作流程停止並輸出拒絕原因。
4.  **Publisher-Agent**：若草稿通過審核，此代理將內容保存為 Markdown 文件。

#### Python 實現分析

此範例使用自定義函數 `select_targets` 實現條件邏輯。該函數傳遞給 `add_multi_selection_edge_group`，根據 `review_result` 字段指導工作流程。

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# This function determines the next step based on the review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If approved, proceed to the 'save_draft' executor
        return [save_draft_id]
    else:
        # If rejected, proceed to the 'handle_review' executor to report failure
        return [handle_review_id]

# The workflow builder uses the selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # The multi-selection edge implements the conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

使用自定義執行器（如 `to_reviewer_result`）解析代理的 JSON 輸出並轉換為強類型對象，供選擇函數檢查。

#### .NET (C\#) 實現分析

.NET 版本使用類似的方法，定義條件函數。`Func<object?, bool>` 用於檢查 `ReviewResult` 對象的 `Result` 屬性。

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

`AddEdge` 方法的 `condition` 參數允許 `WorkflowBuilder` 創建分支路徑。工作流程僅在條件 `GetCondition(expectedResult: "Yes")` 返回 true 時遵循到 `publishExecutor` 的邊，否則遵循到 `sendReviewerExecutor` 的路徑。

## 結論

Microsoft Agent Framework Workflow 提供了一個穩健且靈活的基礎，用於編排複雜的多代理系統。通過利用其基於圖形的架構和核心元件，開發者可以在 Python 和 .NET 中設計並實現精密的工作流程。無論您的應用程式需要簡單的順序處理、並行執行還是動態條件邏輯，該框架都提供了構建強大、可擴展且類型安全的 AI 驅動解決方案的工具。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。