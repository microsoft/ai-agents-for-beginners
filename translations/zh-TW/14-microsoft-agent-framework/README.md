# 探索 Microsoft Agent Framework

![Agent Framework](../../../translated_images/zh-TW/lesson-14-thumbnail.90df0065b9d234ee.webp)

### 介紹

本課程將涵蓋：

- 了解 Microsoft Agent Framework：關鍵功能與價值  
- 探索 Microsoft Agent Framework 的核心概念
- 進階 MAF 範式：工作流程、中介軟體和記憶體

## 學習目標

完成本課程後，您將會知道如何：

- 使用 Microsoft Agent Framework 建立生產等級的 AI 代理
- 將 Microsoft Agent Framework 的核心功能應用於您的代理使用案例
- 使用包括工作流程、中介軟體和可觀測性在內的進階範式

## 範例程式碼

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) 的範例程式碼可以在此存放庫的 `xx-python-agent-framework` 和 `xx-dotnet-agent-framework` 檔案中找到。

## 了解 Microsoft Agent Framework

![Framework Intro](../../../translated_images/zh-TW/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) 是 Microsoft 用於建立 AI 代理的統一框架。它提供靈活性以應對生產和研究環境中各種代理使用案例，包括：

- 需要逐步工作流程的 **順序代理協調**。
- 代理需同時完成任務的 **並行協調**。
- 多個代理可協作完成同一任務的 **群組聊天協調**。
- 代理依完成子任務相互交接任務的 **交接協調**。
- 由管理代理建立並修改任務列表，並協調子代理完成任務的 **磁性協調**。

為了在生產環境中提供 AI 代理，MAF 還包含以下功能：

- 透過 OpenTelemetry 實現 **可觀測性**，追蹤 AI 代理的每個行動，包括工具調用、協調步驟、推理流程，以及透過 Microsoft Foundry 儀表板進行效能監控。
- 透過 Microsoft Foundry 原生託管代理以實現 **安全性**，包含基於角色的存取控制、私人資料處理和內建內容安全性。
- 支援代理線程和工作流程暫停、恢復及錯誤復原的 **耐久性**，使得可進行較長的執行流程。
- 支援人類介入工作流程的 **控制**，可標記任務需要人類批准。

Microsoft Agent Framework 同時注重互通性，包含：

- **無特定雲端限制** — 代理可在容器、本地端及多種不同雲端中執行。
- **無提供者限制** — 代理可使用您偏好的 SDK 建立，包括 Azure OpenAI 及 OpenAI。
- **整合開放標準** — 代理可使用 Agent-to-Agent（A2A）與 Model Context Protocol（MCP）等協定來發現和使用其他代理和工具。
- **外掛及連接器** — 可連接至 Microsoft Fabric、SharePoint、Pinecone 和 Qdrant 等資料與記憶服務。

讓我們看看這些功能如何應用在 Microsoft Agent Framework 的一些核心概念上。

## Microsoft Agent Framework 的核心概念

### 代理 (Agents)

![Agent Framework](../../../translated_images/zh-TW/agent-components.410a06daf87b4fef.webp)

**建立代理**

建立代理是透過定義推論服務（LLM 提供者）、一組 AI 代理要遵循的指令，並指派 `name` 來完成：

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

以上是使用 `Azure OpenAI`，但是代理也可以使用多種服務建立，包括 `Microsoft Foundry Agent Service`：

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI 的 `Responses`、`ChatCompletion` API

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

或是使用 A2A 協定的遠端代理：

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**運行代理**

代理使用 `.run` 或 `.run_stream` 方法執行，分別用於非串流或串流回應。

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

每次代理執行也可以有選項來自訂參數，例如 `max_tokens`（代理使用的最大令牌數）、代理能調用的 `tools`，甚至是代理使用的 `model`。

當完成使用者任務需要特定模型或工具時，此功能非常有用。

**工具 (Tools)**

工具可以在定義代理時指定：

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# 當直接建立一個 ChatAgent 時

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

也可以在執行代理時指定：

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # 僅為此執行提供的工具 )
```

**代理線程 (Agent Threads)**

代理線程用於處理多回合對話。線程可以透過以下方式建立：

- 使用 `get_new_thread()`，能讓線程隨時間保存
- 在執行代理時自動建立線程，且該線程只在當前執行期間存在

建立線程的程式碼如下：

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() # 使用該執行緒執行代理。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

之後可以將線程序列化，以便後續存取：

```python
# 建立一個新的執行緒。
thread = agent.get_new_thread() 

# 使用該執行緒運行代理。

response = await agent.run("Hello, how are you?", thread=thread) 

# 將執行緒序列化以便儲存。

serialized_thread = await thread.serialize() 

# 從儲存中載入後反序列化執行緒狀態。

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**代理中介軟體 (Agent Middleware)**

代理會與工具及 LLM 互動以完成使用者任務。在某些情況下，我們希望在兩者交互之間執行或追蹤動作。代理中介軟體可讓我們做到這點，包含：

*函式中介軟體 (Function Middleware)*

此中介軟體允許我們在代理與其將調用的函式/工具之間執行動作。例如，記錄函式呼叫時的日誌。

以下程式碼中，`next` 指定是否呼叫下一個中介軟體或實際函式。

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # 預處理：函式執行前記錄日誌
    print(f"[Function] Calling {context.function.name}")

    # 繼續執行下一個中介軟體或函式
    await next(context)

    # 後處理：函式執行後記錄日誌
    print(f"[Function] {context.function.name} completed")
```

*聊天中介軟體 (Chat Middleware)*

此中介軟體讓我們能在代理與 LLM 的請求間執行或記錄動作。

其中包含重要資訊，如傳送給 AI 服務的 `messages`。

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # 預處理：AI 呼叫前的日誌記錄
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # 繼續到下一個中介軟體或 AI 服務
    await next(context)

    # 後處理：AI 回應後的日誌記錄
    print("[Chat] AI response received")

```

**代理記憶體 (Agent Memory)**

如在 `Agentic Memory` 課程中所述，記憶是使代理能運作於多種上下文的重要元素。MAF 提供多種類型的記憶：

*記憶內儲存 (In-Memory Storage)*

此記憶儲存在執行時線程中。

```python
# 建立一個新的執行緒。
thread = agent.get_new_thread() # 使用該執行緒執行代理程式。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*持久化訊息 (Persistent Messages)*

當跨不同會話儲存對話歷史時使用。透過 `chat_message_store_factory` 定義：

```python
from agent_framework import ChatMessageStore

# 建立自訂的訊息存儲
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*動態記憶 (Dynamic Memory)*

此記憶在代理執行前加入上下文。這些記憶可以儲存在外部服務，如 mem0：

```python
from agent_framework.mem0 import Mem0Provider

# 使用 Mem0 以獲得進階記憶體功能
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**代理可觀測性 (Agent Observability)**

可觀測性對於建構可靠且可維護的代理系統非常重要。MAF 整合 OpenTelemetry 提供追蹤及度量，以增進可觀測性。

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # 做一些事情
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### 工作流程 (Workflows)

MAF 提供工作流程，為完成任務的預定義步驟，並包含 AI 代理作為這些步驟中的組件。

工作流程由不同組件組成，允許更好的流程控制。工作流程還支援 **多代理協調** 及 **檢查點**，以保存工作流程狀態。

工作流程的核心組件有：

**執行器 (Executors)**

執行器接收輸入訊息，執行指派任務，然後產出輸出訊息。這推動工作流程向完成較大任務邁進。執行器可以是 AI 代理或自訂邏輯。

**邊緣 (Edges)**

邊緣用於定義工作流程中訊息的流動。包含以下類型：

*直接邊緣* — 執行器間的簡單一對一連接：

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*條件邊緣* — 當特定條件滿足後啟動。例如，在旅館房間不可用時，執行器可建議其他選項。

*選擇-案例邊緣* — 根據定義條件將訊息導向不同執行器。例如，當旅遊客戶有優先權存取權，其任務可由另一個工作流程處理。

*分散邊緣* — 將一則訊息送到多個目標。

*匯聚邊緣* — 收集多個不同執行器的訊息並送達一個目標。

**事件 (Events)**

為了提供更好的工作流程可觀測性，MAF 提供內建執行事件，包括：

- `WorkflowStartedEvent` — 工作流程開始執行
- `WorkflowOutputEvent` — 工作流程產生輸出
- `WorkflowErrorEvent` — 工作流程出現錯誤
- `ExecutorInvokeEvent` — 執行器開始處理
- `ExecutorCompleteEvent` — 執行器完成處理
- `RequestInfoEvent` — 發出請求

## 進階 MAF 範式

上述章節涵蓋 Microsoft Agent Framework 的核心概念。隨著您建立更複雜的代理，以下是一些值得考慮的進階範式：

- **中介軟體組合**：使用函式及聊天中介軟體串聯多個中介軟體處理器（記錄、身份驗證、限速），以精細控制代理行為。
- **工作流程檢查點**：使用工作流程事件及序列化來儲存與恢復長時間執行的代理流程。
- **動態工具選擇**：結合針對工具描述的 RAG 以及 MAF 的工具註冊機制，為每個查詢只呈現相關工具。
- **多代理交接**：透過工作流程邊緣及條件路由協調專業代理間的交接。

## 範例程式碼

Microsoft Agent Framework 的範例程式碼可以在此存放庫的 `xx-python-agent-framework` 和 `xx-dotnet-agent-framework` 檔案中找到。

## 對 Microsoft Agent Framework 有更多疑問嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者交流、參加辦公時間，並獲得您的 AI 代理問題解答。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不精確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->