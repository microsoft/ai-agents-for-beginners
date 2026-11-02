# 使用 Microsoft Agent Framework Workflow 建立多代理應用程式

本教學將引導您了解並建立使用 Microsoft Agent Framework 的多代理應用程式。我們將探討多代理系統的核心概念，深入了解框架中 Workflow 部件的架構，並透過 Python 與 .NET 的實務範例，一步步示範不同的工作流程模式。

## 1\. 了解多代理系統

AI 代理是一個超越標準大型語言模型（LLM）能力的系統。它能感知環境、做出決策並採取行動，以達成特定目標。多代理系統則包含多個此類代理協作，共同解決單一代理難以或無法獨自處理的問題。

### 常見應用場景

  * <strong>複雜問題解決</strong>：將大任務（例如規劃全公司活動）分解成由專門代理處理的較小子任務（例如預算代理、物流代理、行銷代理）。
  * <strong>虛擬助理</strong>：主要助理代理將排程、研究與預訂等任務委派給其他專門代理。
  * <strong>自動內容創作</strong>：一個代理草擬內容，另一個代理審核其準確性與語調，第三個代理負責發佈。

### 多代理模式

多代理系統可組織成多種互動模式：

  * <strong>序列式</strong>：代理按預定順序運作，如組裝線。前一代理的輸出成為下一代理的輸入。
  * <strong>並行式</strong>：代理同時處理任務不同部分，最後將結果彙聚。
  * <strong>條件式</strong>：根據代理輸出選擇不同工作流路徑，類似 if-then-else 判斷。

## 2\. Microsoft Agent Framework Workflow 架構

Agent Framework 的工作流程系統是一個先進的編排引擎，用以管理多代理間的複雜互動。它建立在圖形化架構之上，採用[Pregel 風格執行模型](https://kowshik.github.io/JPregel/pregel_paper.pdf)，在稱為「超步驟 (supersteps)」的同步階段中執行處理。

### 核心元件

架構包含三大部分：

1.  **執行者（Executors）**：基礎執行單元。在範例中，`Agent` 便是一種執行者。每個執行者可含多個訊息處理器，會根據接收到的訊息類型自動觸發。
2.  **邊（Edges）**：定義訊息在執行者間傳遞的路徑。邊可設定條件，用以動態路由資訊於工作流程圖中。
3.  **工作流程（Workflow）**：負責整合管理執行者、邊與整體執行流程。確保訊息依正確順序處理並串流事件以利觀察。

*展示工作流程系統核心元件的示意圖。*

此結構讓您能以序列流程、扇出/扇入並行處理及條件分支（switch-case）等基本模式，建構強健且可擴充的應用程式。

## 3\. 實務範例與程式碼分析

現在，讓我們探索如何使用此框架實作各種工作流程模式。我們將針對每個範例同時檢視 Python 與 .NET 程式碼。

### 範例 1：基礎序列工作流程

此為最簡單模式，一個代理的輸出直接傳遞給另一代理。我們的場景為飯店的 `FrontDesk` 代理提供旅遊建議，再由 `Concierge` 代理審核。

*基礎 FrontDesk -> Concierge 工作流程示意圖。*

#### 場景背景

旅客請求巴黎旅遊建議。

1.  精簡型的 `FrontDesk` 代理建議前往羅浮宮博物館。
2.  重視真實體驗的 `Concierge` 代理收到建議，審核並反饋，建議更在地且遊客較少的替代方案。

#### Python 實作分析

Python 範例先定義並建立兩個具有特定指令的代理。

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

接著使用 `WorkflowBuilder` 建立圖形。設定 `front_desk_agent` 為起點，建立邊將其輸出連接至 `reviewer_agent`。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

最後使用初始使用者提示執行工作流程。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run 執行工作流程；get_outputs() 返回輸出執行器的結果。
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) 實作分析

.NET 實作邏輯類似。先定義代理名稱與指令常數。

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

透過 `AzureOpenAIClient` (Responses API) 建立代理，接著使用 `WorkflowBuilder` 以增加連結邊界 (`frontDeskAgent` 到 `reviewerAgent`) 設定序列流程。

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

以使用者訊息執行工作流程，結果以串流回傳。

### 範例 2：多階段序列工作流程

此模式擴展基本序列，加入更多代理。適用於需多階段精煉或轉換的流程。

#### 場景背景

使用者提供一張客廳圖片並請求家具報價。

1.  <strong>銷售代理</strong>：識別圖片中的家具物品並建立清單。
2.  <strong>價格代理</strong>：針對清單提供詳細價格分析，包括預算款、中階與高階選擇。
3.  <strong>報價代理</strong>：接收帶價格的清單，並將其格式化成 Markdown 格式的正式報價文件。

*銷售 -> 價格 -> 報價工作流程示意圖。*

#### Python 實作分析

定義三個擁有專門職責的代理。工作流程用 `add_edge` 依次串連 `sales_agent` -> `price_agent` -> `quote_agent`。

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# 創建三個專門代理
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# 建立序列工作流程
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

輸入為包含文字與圖片 URI 的 `ChatMessage`。框架處理將每個代理輸出傳遞至下一代理，直至產生最終報價。

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# 使用者訊息包含文字和圖像
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

.NET 版本與 Python 類似，建立三個代理 (`salesagent`、`priceagent`、`quoteagent`)，並以 `WorkflowBuilder` 依序連接。

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

使用者訊息含圖片資料（位元組）與文字提示，呼叫 `InProcessExecution.RunStreamingAsync` 執行工作流程，從串流捕獲最終輸出。

### 範例 3：並行工作流程

當任務可同步執行以節省時間時，採用此模式。涉及向多代理「扇出」並「扇入」結果彙集。

#### 場景背景

使用者要求規劃西雅圖旅行。

1.  **分派者（扇出）**：使用者請求同時傳送至兩個代理。
2.  <strong>研究代理</strong>：調查西雅圖十二月旅遊景點、天氣及重點注意事項。
3.  <strong>規劃代理</strong>：獨立制定詳細逐日行程。
4.  **彙集者（扇入）**：收集研究與規劃輸出，整合呈現最終結果。

*並行研究與規劃代理工作流程示意圖。*

#### Python 實作分析

`ConcurrentBuilder` 可簡化此模式建立。只要列出參與代理，建構器會自動產生扇出與扇入邏輯。

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder 處理扇出/扇入邏輯
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# 執行工作流程
events = await workflow.run("Plan a trip to Seattle in December")
```

框架確保 `research_agent` 與 `plan_agent` 並行執行，最終輸出被彙集成列表。

#### .NET (C\#) 實作分析

在 .NET 中需較明確定義此模式。建立自訂執行者（`ConcurrentStartExecutor` 與 `ConcurrentAggregationExecutor`）處理扇出與扇入邏輯。

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

再利用 `WorkflowBuilder` 的 `AddFanOutEdge` 和 `AddFanInEdge` 方法，使用這些自訂執行者與代理組成圖形。

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### 範例 4：條件式工作流程

條件式工作流程引入分支邏輯，使系統可依中間結果走不同路徑。

#### 場景背景

此工作流程用於自動撰寫及發布技術教學。

1.  <strong>傳播代理</strong>：根據提綱與 URL 撰寫教學草稿。
2.  <strong>內容審核代理</strong>：審核草稿，檢查字數是否超過 200 字。
3.  <strong>條件分支</strong>：
      * **通過（「是」）**：工作流程繼續至 `Publisher-Agent`。
      * **失敗（「否」）**：工作流程終止，輸出拒絕原因。
4.  <strong>發布代理</strong>：若草稿通過，該代理將內容保存為 Markdown 檔案。

#### Python 實作分析

使用自訂函數 `select_targets` 實作條件邏輯。此函數傳入 `add_multi_selection_edge_group`，根據審核代理輸出中的 `review_result` 欄位導引流程。

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# 此函數根據審核結果決定下一步
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # 若通過審核，則執行 'save_draft' 執行器
        return [save_draft_id]
    else:
        # 若審核未通過，則執行 'handle_review' 執行器並回報失敗
        return [handle_review_id]

# 工作流程建構器使用選擇函數進行路由
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # 多重選擇邊實現條件邏輯
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

利用 `to_reviewer_result` 等自訂執行者將代理的 JSON 輸出解析為強型別物件，使選擇函數得以檢查。

#### .NET (C\#) 實作分析

.NET 版本亦採用類似方法，定義一個 `Func<object?, bool>` 判斷 `ReviewResult` 物件的 `Result` 屬性。

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

`AddEdge` 方法的 `condition` 參數讓 `WorkflowBuilder` 建立分支路徑。當 `GetCondition(expectedResult: "Yes")` 回傳真時，工作流程會沿向 `publishExecutor` 的邊前進；否則走向 `sendReviewerExecutor`。

## 結語

Microsoft Agent Framework Workflow 為複雜多代理系統提供穩健且彈性的編排基礎。藉由其圖形化架構與核心元件，開發者得以在 Python 與 .NET 平台上設計並實作多樣化工作流程。無論應用需簡單序列處理、平行執行，或動態條件邏輯，此框架皆提供建構強大、可擴展且型別安全的 AI 驅動解決方案的工具。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->