# 探索 Microsoft Agent Framework

![代理框架](../../../translated_images/zh-HK/lesson-14-thumbnail.90df0065b9d234ee.webp)

### 介紹

本課程將涵蓋：

- 了解 Microsoft Agent Framework：主要特性與價值  
- 探索 Microsoft Agent Framework 的核心概念
- 進階 MAF 模式：工作流、中介層與記憶

## 學習目標

完成本課程後，你將會知道如何：

- 使用 Microsoft Agent Framework 建立可投入生產的 AI 代理
- 將 Microsoft Agent Framework 的核心功能應用於你的代理式用例
- 使用進階模式，包括工作流、中介層和可觀測性

## 程式範例 

此存放庫中的 `xx-python-agent-framework` 與 `xx-dotnet-agent-framework` 檔案包含了 [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) 的程式範例。

## 了解 Microsoft Agent Framework

![框架簡介](../../../translated_images/zh-HK/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) 是 Microsoft 用來建立 AI 代理的統一框架。它提供靈活性以處理生產與研究環境中各種代理式用例，包括：

- **順序代理編排**：在需要逐步工作流程的情境中使用。
- **並行編排**：在代理需要同時完成任務的情境中使用。
- **群組聊天編排**：在多個代理一起協作處理同一任務的情境中使用。
- **交接編排**：在代理隨著子任務完成而將任務交接給彼此的情境中使用。
- **磁性編排**：在一個管理者代理建立並修改任務清單，並協調子代理完成任務的情境中使用。

為了在生產環境中交付 AI 代理，MAF 也包含了以下功能：

- **可觀測性**：透過 OpenTelemetry，追蹤代理的每項動作，包括工具調用、編排步驟、推理流程，並透過 Microsoft Foundry 儀表板進行效能監控。
- **安全性**：在 Microsoft Foundry 上原生託管代理，包含角色存取控制、私人資料處理與內建內容安全等安全控管。
- **持久性**：代理執行緒與工作流可以暫停、恢復並從錯誤中復原，支援較長時間的處理流程。
- **控制**：支援人員在迴路（human-in-the-loop）的工作流程，可將任務標記為需人工核准。

Microsoft Agent Framework 也強調互通性：

- **雲端無關** - 代理可在容器、內部部署或多個不同雲端上執行。
- **供應者無關** - 可透過你偏好的 SDK（包括 Azure OpenAI 與 OpenAI）建立代理
- **整合開放標準** - 代理可利用 Agent-to-Agent (A2A) 與 Model Context Protocol (MCP) 等協議來發現並使用其他代理與工具。
- **外掛與連接器** - 可連接到資料與記憶服務，例如 Microsoft Fabric、SharePoint、Pinecone 與 Qdrant。

接下來我們來看看這些功能如何應用於 Microsoft Agent Framework 的一些核心概念。

## Microsoft Agent Framework 的核心概念

### 代理

![代理框架](../../../translated_images/zh-HK/agent-components.410a06daf87b4fef.webp)

**建立代理**

代理的建立透過定義推論服務（LLM 提供者）、一組供 AI 代理遵循的指示，及指定的 `name` 來完成：

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

上例使用的是 `Azure OpenAI`，但代理也可以使用多種服務建立，包括 `Microsoft Foundry Agent Service`：

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

或透過 A2A 協議使用遠端代理：

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**執行代理**

代理透過 `.run` 或 `.run_stream` 方法執行，以支援非串流或串流回應。

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

每次代理執行也可以帶有選項來自訂參數，例如代理使用的 `max_tokens`、代理可以調用的 `tools`，甚至代理所使用的 `model`。

在需要特定模型或工具來完成使用者任務的情況下，這一點非常有用。

**工具**

工具可以在定義代理時一併定義：

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# 當直接建立 ChatAgent 時

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

也可以在執行代理時傳入：

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # 此工具只於本次執行期間提供 )
```

**代理執行緒**

代理執行緒用於處理多回合對話。執行緒可以透過以下方式建立：

- 使用 `get_new_thread()`，使該執行緒可以隨時間儲存
- 在執行代理時自動建立執行緒，且該執行緒僅在當前執行期間存在

要建立執行緒，程式碼如下：

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() # 使用該執行緒執行代理程式。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

接著你可以序列化該執行緒以便日後儲存與使用：

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() 

# 使用該執行緒執行代理程式。

response = await agent.run("Hello, how are you?", thread=thread) 

# 將執行緒序列化以便儲存。

serialized_thread = await thread.serialize() 

# 從儲存載入後，反序列化執行緒狀態。

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**代理中間件**

代理與工具和 LLM 互動以完成使用者任務。在某些情境下，我們希望在這些互動之間執行或追蹤操作。代理中間件讓我們可以透過以下方式達成：

*函數中間件*

此中間件允許我們在代理與它將呼叫的函數/工具之間執行一個動作。這類情境的範例是你可能想對該函數呼叫進行日誌紀錄。

在下面的程式碼中，`next` 用以決定是否呼叫下一個中間件或實際的函數。

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # 前置處理：於函數執行前記錄日誌
    print(f"[Function] Calling {context.function.name}")

    # 繼續至下一個中介軟體或執行下一個函數
    await next(context)

    # 後置處理：於函數執行後記錄日誌
    print(f"[Function] {context.function.name} completed")
```

*聊天中間件*

此中間件允許我們在代理與 LLM 之間的請求流程上執行或記錄動作。

此處包含重要資訊，例如傳送到 AI 服務的 `messages`。

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # 前置處理：在呼叫 AI 之前記錄日誌
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # 繼續到下一個中間件或 AI 服務
    await next(context)

    # 後置處理：在 AI 回應後記錄日誌
    print("[Chat] AI response received")

```

**代理記憶**

如在 `Agentic Memory` 課程中所述，記憶是讓代理能在不同上下文中運作的重要元素。MAF 提供了數種不同類型的記憶：

*記憶體內儲存*

這是應用執行期間在執行緒內儲存的記憶。

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() # 用該執行緒執行代理程式。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*持久訊息*

當在不同會話間儲存對話歷史時會使用此類記憶。它是使用 `chat_message_store_factory` 定義的：

```python
from agent_framework import ChatMessageStore

# 建立自訂訊息儲存庫
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*動態記憶*

此類記憶會在代理執行前被加入到上下文中。這些記憶可以儲存在外部服務，例如 mem0：

```python
from agent_framework.mem0 import Mem0Provider

# 使用 Mem0 以獲得進階的記憶體功能
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

**代理可觀測性**

可觀測性對於建立可靠且可維護的代理系統非常重要。MAF 與 OpenTelemetry 整合，以提供追蹤與計量，進而提升可觀測性。

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # 做啲嘢
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### 工作流

MAF 提供工作流（預定義的步驟）來完成任務，並在這些步驟中包含 AI 代理作為元件。

工作流由不同的元件組成，以便更好的控制流程。工作流也支援 **多代理編排** 與 **檢查點** 用以儲存工作流狀態。

工作流的核心元件包括：

**執行器**

執行器接收輸入訊息、執行指派的任務，然後產生輸出訊息，推動工作流朝完成更大任務邁進。執行器可以是 AI 代理或自訂邏輯。

**邊**

邊用來定義工作流中訊息的流向。這些可以是：

*直接邊* - 執行器之間的一對一簡單連接：

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*條件邊* - 在滿足特定條件後啟動。例如，當飯店房間不可用時，某個執行器可以建議其他選項。

*Switch-case 邊* - 根據定義的條件將訊息路由到不同的執行器。例如，如果旅客具有優先存取，其任務將透過另一個工作流處理。

*分發（Fan-out）邊* - 將一則訊息傳送到多個目標。

*合併（Fan-in）邊* - 收集來自不同執行器的多則訊息並傳送到單一目標。

**事件**

為了提供對工作流更好的可觀測性，MAF 提供了執行過程中的內建事件，包括：

- `WorkflowStartedEvent`  - 工作流執行開始
- `WorkflowOutputEvent` - 工作流產生輸出
- `WorkflowErrorEvent` - 工作流遇到錯誤
- `ExecutorInvokeEvent`  - 執行器開始處理
- `ExecutorCompleteEvent`  -  執行器完成處理
- `RequestInfoEvent` - 發出請求

## 進階 MAF 模式

上面的章節涵蓋了 Microsoft Agent Framework 的關鍵概念。當你構建更複雜的代理時，以下是一些可以考慮的進階模式：

- **中間件組合（Middleware Composition）**：串接多個中間件處理器（日誌、認證、速率限制），使用函數與聊天中間件來細粒度控制代理行為。
- **工作流檢查點（Workflow Checkpointing）**：使用工作流事件與序列化來儲存與恢復長時間執行的代理流程。
- **動態工具選擇（Dynamic Tool Selection）**：將針對工具描述的 RAG 與 MAF 的工具註冊結合，以便每次查詢僅呈現相關工具。
- **多代理交接（Multi-Agent Handoff）**：使用工作流邊與條件路由來協調專門化代理之間的交接。

## 程式範例 

此存放庫中的 `xx-python-agent-framework` 與 `xx-dotnet-agent-framework` 檔案包含了 Microsoft Agent Framework 的程式範例。

## 對 Microsoft Agent Framework 有更多問題嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者交流、參加問答時間，並獲得你的 AI 代理相關問題的解答。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。儘管我們力求準確，請注意自動翻譯可能包含錯誤或不準確之處。原始語言的文件應視為具權威性的版本。如內容屬關鍵性資訊，建議採用專業人工翻譯。我們不對因使用此翻譯而引致的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->