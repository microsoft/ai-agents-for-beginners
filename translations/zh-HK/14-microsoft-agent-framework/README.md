# 探索 Microsoft Agent Framework

![代理框架](../../../translated_images/zh-HK/lesson-14-thumbnail.90df0065b9d234ee.webp)

### 介紹

本課程會涵蓋：

- 了解 Microsoft Agent Framework：主要功能與價值  
- 探索 Microsoft Agent Framework 的關鍵概念
- 進階 MAF 範式：工作流程、中介層與記憶

## 學習目標

完成本課程後，您將會知道如何：

- 使用 Microsoft Agent Framework 建置可投入生產的 AI 代理
- 將 Microsoft Agent Framework 的核心功能應用到您的代理式使用情境
- 使用包含工作流程、中介層與可觀測性在內的進階模式

## 範例程式碼 

範例程式碼可在本存放庫的 `xx-python-agent-framework` 與 `xx-dotnet-agent-framework` 檔案中找到，針對 [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok)。

## 了解 Microsoft Agent Framework

![框架簡介](../../../translated_images/zh-HK/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) 是 Microsoft 用於構建 AI 代理的統一框架。它提供靈活性，以應對在生產與研究環境中出現的各種代理式使用情境，包括：

- **Sequential Agent orchestration**：在需要逐步工作流程的情境中。
- **Concurrent orchestration**：在代理需同時完成任務的情境中。
- **Group chat orchestration**：在代理能夠協同處理同一任務的情境中。
- **Handoff Orchestration**：在子任務完成時代理彼此交接任務的情境中。
- **Magnetic Orchestration**：在管理代理建立並修改任務清單，並協調子代理完成任務的情境中。

為了在生產環境部署 AI 代理，MAF 也包含以下功能：

- **Observability**：透過使用 OpenTelemetry，追蹤 AI 代理的每個動作，包括工具調用、編排步驟、推理流程，以及透過 Microsoft Foundry 儀表板的效能監控。
- **Security**：透過在 Microsoft Foundry 原生託管代理來提供安全性，該平台包含角色存取控制、私人資料處理及內建內容安全等控制機制。
- **Durability**：代理執行緒與工作流程可以暫停、恢復與從錯誤中復原，從而支援更長時程的處理。
- **Control**：支援人員介入的工作流程，將任務標記為需要人工批准。

Microsoft Agent Framework 也注重互通性，具體包括：

- **Being Cloud-agnostic**：代理可以在容器中、本地部署或跨多個不同雲端執行。
- **Being Provider-agnostic**：代理可透過您偏好的 SDK 建立，包括 Azure OpenAI 與 OpenAI
- **Integrating Open Standards**：代理可使用像 Agent-to-Agent(A2A) 與 Model Context Protocol (MCP) 等協定來發現並使用其他代理與工具。
- **Plugins and Connectors**：可連接到如 Microsoft Fabric、SharePoint、Pinecone 與 Qdrant 等資料與記憶服務。

讓我們看看這些功能如何套用到 Microsoft Agent Framework 的一些核心概念。

## Microsoft Agent Framework 的關鍵概念

### 代理

![代理組件](../../../translated_images/zh-HK/agent-components.410a06daf87b4fef.webp)

**建立代理**

代理的建立是透過定義推論服務（LLM Provider）、一個
供 AI 代理遵循的指令集合，以及指定的 `name`：

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

上述範例使用了 `Azure OpenAI`，但代理可以使用各種服務建立，包括 `Microsoft Foundry Agent Service`：

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

或使用 A2A 協定的遠端代理：

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**執行代理**

代理透過 `.run` 或 `.run_stream` 方法執行，以獲得非串流或串流回應。

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

每次代理執行也可以包含選項來自訂參數，例如代理使用的 `max_tokens`、代理可以調用的 `tools`，甚至代理使用的 `model` 本身。

當完成使用者任務需要特定模型或工具時，這非常有用。

**工具**

工具可以在定義代理時一起定義：

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# 直接建立 ChatAgent 時

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

也可以在執行代理時定義：

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # 此工具僅於本次執行提供 )
```

**代理執行緒**

代理執行緒用於處理多回合對話。執行緒可以透過以下方式建立：

- 使用 `get_new_thread()`，可讓該執行緒隨時間儲存
- 在執行代理時自動建立執行緒，該執行緒只在當前執行期間存在。

要建立執行緒，程式碼如下：

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() # 用該執行緒執行代理程式。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

接著您可以序列化該執行緒以便日後儲存使用：

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() 

# 使用該執行緒運行代理程式。

response = await agent.run("Hello, how are you?", thread=thread) 

# 將執行緒序列化以便儲存。

serialized_thread = await thread.serialize() 

# 從儲存載入後反序列化執行緒狀態。

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**代理中介層**

代理與工具及 LLM 互動以完成使用者的任務。在某些情境中，我們希望在這些互動之間執行或追蹤一些操作。代理中介層讓我們能透過以下方式做到這點：

*Function Middleware*

此中介層允許我們在代理與其要呼叫的函式/工具之間執行一個動作。適用範例包括在函式呼叫時進行一些日誌記錄。

在下方程式碼中，`next` 決定是否應呼叫下一個中介層或實際的函式。

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # 前置處理：在函數執行前記錄日誌
    print(f"[Function] Calling {context.function.name}")

    # 繼續到下一個中間件或函數執行
    await next(context)

    # 後置處理：在函數執行後記錄日誌
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

此中介層允許我們在代理與 LLM 之間的請求過程中執行或記錄一個動作。

這包含重要資訊，例如傳送到 AI 服務的 `messages`。

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # 前置處理：在呼叫 AI 前記錄日誌
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # 繼續至下一個中介軟體或 AI 服務
    await next(context)

    # 後置處理：在 AI 回應後記錄日誌
    print("[Chat] AI response received")

```

**代理記憶**

如在 `Agentic Memory` 課程所述，記憶是讓代理能在不同上下文中運作的重要元素。MAF 提供了幾種不同類型的記憶：

*In-Memory Storage*

這是應用程式執行期間儲存在執行緒中的記憶。

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() # 使用該執行緒執行代理。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

此類記憶用於跨不同會話儲存對話記錄。它是透過 `chat_message_store_factory` 定義的：

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

*Dynamic Memory*

此類記憶會在代理執行前加入到上下文中。這些記憶可以儲存在外部服務，例如 mem0：

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

**代理可觀測性**

可觀測性對於構建可靠且可維護的代理系統非常重要。MAF 與 OpenTelemetry 整合以提供追蹤與度量，提升可觀測性。

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

### 工作流程

MAF 提供工作流程，這些流程是預先定義的步驟用來完成任務，並將 AI 代理作為步驟中的組成元件。

工作流程由不同的元件組成，以實現更好的控制流程。工作流程也支援 **multi-agent orchestration** 與 **checkpointing**，以保存工作流程狀態。

工作流程的核心元件包括：

**執行者 (Executors)**

執行者接收輸入訊息，執行指派的任務，然後產生輸出訊息。這將工作流程推進以完成更大的任務。執行者可以是 AI 代理或自訂邏輯。

**邊 (Edges)**

邊用來定義工作流程中訊息的流向。它們可以是：

*Direct Edges* - 執行者之間的簡單一對一連接：

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - 在特定條件滿足後啟用。例如，當飯店房間不可用時，執行者可以建議其他選項。

*Switch-case Edges* - 根據定義的條件將訊息導向不同的執行者。例如，若旅遊客戶具有優先存取，其任務可能會透過另一個工作流程處理。

*Fan-out Edges* - 將一則訊息發送到多個目標。

*Fan-in Edges* - 從不同執行者收集多則訊息並傳送到單一目標。

**事件**

為了提供更好的工作流程可觀測性，MAF 提供了內建的執行事件，包括：

- `WorkflowStartedEvent`  - 工作流程執行開始
- `WorkflowOutputEvent` - 工作流程產生輸出
- `WorkflowErrorEvent` - 工作流程遇到錯誤
- `ExecutorInvokeEvent`  - 執行者開始處理
- `ExecutorCompleteEvent`  -  執行者完成處理
- `RequestInfoEvent` - 發出請求

## 進階 MAF 範式

上面章節涵蓋了 Microsoft Agent Framework 的關鍵概念。當您構建更複雜的代理時，以下是一些值得考慮的進階範式：

- **Middleware Composition**：使用 function 與 chat 中介層串接多個中介處理器（如 logging、auth、rate-limiting），以對代理行為進行細緻控制。
- **Workflow Checkpointing**：使用工作流程事件與序列化來保存並恢復長時間執行的代理流程。
- **Dynamic Tool Selection**：結合對工具描述的 RAG 與 MAF 的工具註冊，針對每個查詢只呈現相關工具。
- **Multi-Agent Handoff**：使用工作流程邊與條件路由來協調專責代理之間的交接。

## 範例程式碼 

Microsoft Agent Framework 的範例程式碼可在本存放庫的 `xx-python-agent-framework` 與 `xx-dotnet-agent-framework` 檔案中找到。

## 對 Microsoft Agent Framework 有更多問題嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者交流、參加辦公時間並獲得您有關 AI 代理的問題解答。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但自動翻譯可能包含錯誤或不準確之處。原始文件應被視為具權威性的版本。對於重要資訊，建議採用專業人工翻譯。我們對因使用本翻譯而引致的任何誤解或錯誤詮釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->