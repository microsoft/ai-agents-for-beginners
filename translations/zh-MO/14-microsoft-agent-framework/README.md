# 探索 Microsoft Agent Framework

![Agent Framework](../../../translated_images/zh-MO/lesson-14-thumbnail.90df0065b9d234ee.webp)

### 介紹

本課程將涵蓋：

- 理解 Microsoft Agent Framework：主要特點與價值  
- 探索 Microsoft Agent Framework 的核心概念
- 高級 MAF 模式：工作流、中介軟件與記憶體

## 學習目標

完成本課程後，您將能夠：

- 使用 Microsoft Agent Framework 建構生產就緒的 AI 代理
- 將 Microsoft Agent Framework 的核心功能應用於您的代理用例
- 使用包括工作流、中介軟件和可觀察性在內的高級模式

## 程式碼範例

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) 的程式碼範例可在本儲存庫中 `xx-python-agent-framework` 和 `xx-dotnet-agent-framework` 檔案下找到。

## 理解 Microsoft Agent Framework

![Framework Intro](../../../translated_images/zh-MO/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) 是微軟統一的 AI 代理架構。它靈活地應對了生產及研究環境中看到的各種代理用例，包括：

- **序列代理編排**，適用於需要逐步工作流程的場景。
- **並行編排**，適用於代理需同時完成任務的場景。
- **群組聊天編排**，適用於代理在同一任務上協同工作的場景。
- **任務交接編排**，適用於代理在完成子任務後相互交接任務的場景。
- **磁性編排**，用於管理代理建立及修改任務清單，並協調子代理完成任務。

為了在生產中提供 AI 代理，MAF 也包含以下功能：

- **可觀察性**，透過 OpenTelemetry，監控 AI 代理的每一個動作，包括工具調用、編排步驟、推理流程及透過 Microsoft Foundry 儀表板進行效能監控。
- **安全性**，代理直接託管於 Microsoft Foundry，包含角色存取、私有資料處理及內建內容安全的安全控管。
- **耐久性**，代理線程和工作流程可暫停、恢復並從錯誤中復原，支持長時間運行的流程。
- **控制性**，支持人類介入的工作流程，其中任務標記為需人類審核。

Microsoft Agent Framework 亦著眼於可互操作性：

- **跨雲中立性** — 代理可運行於容器內、本地端及多個不同雲端環境。
- **供應商中立性** — 可透過您喜愛的 SDK 建立代理，包括 Azure OpenAI 和 OpenAI。
- **整合開放標準** — 代理可利用如 Agent-to-Agent (A2A) 以及模型上下文協定 (MCP) 來發現和使用其他代理與工具。
- **外掛及連接器** — 可連接至 Microsoft Fabric、SharePoint、Pinecone 及 Qdrant 等資料及記憶服務。

接著看看這些功能如何應用於 Microsoft Agent Framework 的一些核心概念。

## Microsoft Agent Framework 的核心概念

### 代理（Agents）

![Agent Framework](../../../translated_images/zh-MO/agent-components.410a06daf87b4fef.webp)

**建立代理**

代理建立是通過定義推理服務（LLM 提供者）、代理須遵循的一組指令，以及指派的 `name`：

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

上述範例使用了 `Azure OpenAI`，代理也可以使用各種服務建立，包括 `Microsoft Foundry Agent Service`：

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

**執行代理**

代理可透過 `.run` 或 `.run_stream` 方法執行，分別對應非串流或串流回應。

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

每次代理執行也可帶有自定義選項，如代理可用的 `max_tokens`、`tools`，甚至是代理使用的 `model`。

這在需要特定模型或工具來完成用戶任務時很有用。

**工具**

工具可在定義代理時設置：

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# 當直接創建一個 ChatAgent 時

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

也可在執行代理時指定：

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # 僅提供此運行使用的工具 )
```

**代理線程**

代理線程用來處理多輪對話。線程可由以下兩種方式建立：

- 使用 `get_new_thread()` 來啟動線程，可持續儲存使用
- 在執行代理時自動建立線程，且該線程只在當次執行期間存在。

建立線程的程式碼如下：

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() # 使用該執行緒執行代理程式。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

然後可以將線程序列化，以便後續儲存使用：

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() 

# 使用該執行緒運行代理。

response = await agent.run("Hello, how are you?", thread=thread) 

# 將執行緒序列化以供存儲。

serialized_thread = await thread.serialize() 

# 從存儲加載後反序列化執行緒狀態。

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**代理中介軟件**

代理會與工具和大型語言模型 (LLM) 互動以完成用戶任務。在某些情況下，我們希望在此互動過程中執行或追蹤行為。代理中介軟件允許我們這樣做，包含：

*函式中介軟件*

此中介軟件允許我們在代理和其調用的函式/工具間執行動作。舉例而言，您可能想在函式調用時做些記錄。

下方程式碼中，`next` 決定是否呼叫下一個中介軟件或真正的函式。

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # 預處理：函數執行前記錄日誌
    print(f"[Function] Calling {context.function.name}")

    # 繼續下一個中介軟件或函數執行
    await next(context)

    # 後處理：函數執行後記錄日誌
    print(f"[Function] {context.function.name} completed")
```

*聊天中介軟件*

此中介軟件使我們能在代理與 LLM 之間的請求過程中執行或記錄動作。

其中包含如發送至 AI 服務的 `messages` 等重要資訊。

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # 預處理：在 AI 呼叫之前記錄日志
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # 繼續至下一個中介軟件或 AI 服務
    await next(context)

    # 後處理：在 AI 響應後記錄日志
    print("[Chat] AI response received")

```

**代理記憶**

如同在 `Agentic Memory` 課程中所提，記憶對於允許代理在不同上下文中運作至關重要。MAF 提供多種記憶類型：

*記憶體中儲存*

此為應用程序執行期間存於線程中的記憶體。

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() # 使用該執行緒運行代理。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*永久性訊息*

此記憶用於跨會話保存對話歷史。可利用 `chat_message_store_factory` 定義：

```python
from agent_framework import ChatMessageStore

# 建立一個自訂訊息儲存庫
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*動態記憶*

此記憶會在代理執行前加入上下文，這些記憶可儲存在外部服務，如 mem0：

```python
from agent_framework.mem0 import Mem0Provider

# 使用 Mem0 作為進階記憶體功能
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

**代理可觀察性**

可觀察性對建構可靠且可維護的代理系統十分重要。MAF 整合 OpenTelemetry，提供追蹤與儀表，增強可觀察性。

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # 做某事
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### 工作流

MAF 提供工作流，這是為完成任務預定義的步驟，且工作流包含 AI 代理作為其中組件。

工作流由不同組件構成，以提升流程控制。工作流亦支持**多代理編排**與**檢查點存取**以保存工作流狀態。

工作流的核心組件是：

**執行者**

執行者接收輸入訊息，執行其分派任務，然後產生輸出訊息。此過程推進工作流朝向任務完成。執行者可以是 AI 代理或自訂邏輯。

**連結（Edges）**

連結用於定義工作流中訊息的流向，可包括：

*直接連結* — 執行者之間的簡單一對一連接：

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*條件連結* — 當條件達成時觸發。例如：當旅館房間無法提供時，執行者可建議其他選項。

*分支條件連結* — 根據定義的條件將訊息路由至不同執行者。例如：旅客若有優先權，其任務將透過另一工作流程處理。

*分散連結* — 將一則訊息發送至多個目標。

*彙集連結* — 從多個執行者收集多則訊息，並發送至一個目標。

**事件**

為了提供更好的工作流可觀察性，MAF 提供內建執行事件，包括：

- `WorkflowStartedEvent`  - 工作流執行開始
- `WorkflowOutputEvent` - 工作流產生輸出
- `WorkflowErrorEvent` - 工作流遭遇錯誤
- `ExecutorInvokeEvent`  - 執行者開始處理
- `ExecutorCompleteEvent`  - 執行者完成處理
- `RequestInfoEvent` - 發出請求

## 進階 MAF 模式

以上章節涵蓋了 Microsoft Agent Framework 的核心概念。當您建立更複雜的代理時，可考慮以下高級模式：

- **中介軟件組合**：鏈結多個中介軟件處理器（如記錄、驗證、流量限制），使用函式和聊天中介軟件實現對代理行為的細粒度控制。
- **工作流檢查點**：使用工作流事件與序列化功能保存與恢復長時間執行的代理流程。
- **動態工具選擇**：結合對工具描述的檢索增強生成 (RAG) 與 MAF 的工具登錄，根據查詢僅呈現相關工具。
- **多代理交接**：使用工作流邊界和條件路由實現專業代理之間的任務交接編排。

## 程式碼範例

Microsoft Agent Framework 的程式碼範例可於本儲存庫中 `xx-python-agent-framework` 與 `xx-dotnet-agent-framework` 檔案找到。

## 還有關於 Microsoft Agent Framework 的疑問嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，與其他學習者交流，參加辦公時間，並獲取關於 AI 代理的疑問解答。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原文文件之原語版本應視為權威來源。如涉及重要資訊，建議採用專業人類翻譯。我們不對因使用本翻譯所引致之任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->