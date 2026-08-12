# 探索 Microsoft Agent Framework

![Agent Framework](../../../translated_images/zh-TW/lesson-14-thumbnail.90df0065b9d234ee.webp)

### 介紹

本課程將涵蓋：

- 了解 Microsoft Agent Framework：主要功能與價值  
- 探索 Microsoft Agent Framework 的關鍵概念
- 進階的 MAF 模式：工作流程、中介軟體與記憶體

## 學習目標

完成本課程後，您將能夠：

- 使用 Microsoft Agent Framework 建立生產就緒的 AI 代理
- 將 Microsoft Agent Framework 的核心功能應用於您的代理使用案例
- 使用進階模式，包括工作流程、中介軟體和可觀察性

## 程式碼範例 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) 的程式碼範例可在本儲存庫中的 `xx-python-agent-framework` 與 `xx-dotnet-agent-framework` 檔案中找到。

## 了解 Microsoft Agent Framework

![Framework Intro](../../../translated_images/zh-TW/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) 是微軟建置 AI 代理的統一框架。它提供彈性，能因應生產與研究環境中各種不同的代理使用案例，包括：

- <strong>順序代理協調</strong>，適用於需要逐步工作流程的場景。
- <strong>並行協調</strong>，適用於代理需要同時完成任務的場景。
- <strong>群組聊天協調</strong>，適用於代理能共同協作完成同一任務的場景。
- <strong>移交協調</strong>，適用於代理在子任務完成後相互移交任務的場景。
- <strong>磁性協調</strong>，適用於管理代理創建與修改任務清單，並協調子代理完成任務的場景。

為了在生產中部署 AI 代理，MAF 還包含以下功能：

- <strong>可觀察性</strong>，透過 OpenTelemetry，記錄 AI 代理的每個動作，包括工具調用、協調步驟、推理流程，以及透過 Microsoft Foundry 儀表板進行效能監控。
- <strong>安全性</strong>，代理原生託管於 Microsoft Foundry，包含角色基礎存取、私密資料處理和內建內容安全等安全控管。
- <strong>耐用性</strong>，代理執行緒和工作流程可暫停、恢復並從錯誤中復原，支援長時間運行流程。
- <strong>控制</strong>，支援人工審核工作流程，任務可標記為需要人工核准。

Microsoft Agent Framework 也重視互通性，具備：

- <strong>雲端中立性</strong> — 代理可在容器、內部部署與多個不同雲端間運行。
- <strong>供應商中立性</strong> — 代理可使用您偏好的 SDK 創建，包括 Azure OpenAI 和 OpenAI
- <strong>整合開放標準</strong> — 代理能利用 Agent-to-Agent (A2A) 與 Model Context Protocol (MCP) 等協定去發現和使用其他代理與工具。
- <strong>外掛與連接器</strong> — 可連結至 Microsoft Fabric、SharePoint、Pinecone 與 Qdrant 等資料及記憶體服務。

接下來讓我們看看這些功能如何應用於 Microsoft Agent Framework 的一些核心概念。

## Microsoft Agent Framework 的關鍵概念

### 代理

![Agent Framework](../../../translated_images/zh-TW/agent-components.410a06daf87b4fef.webp)

<strong>建立代理</strong>

代理的創建是透過定義推理服務（LLM 提供者）、
AI 代理須遵循的一組指令，以及指定的 `name` 來完成：


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

上述範例使用的是 `Azure OpenAI`，但代理人也可以使用多種服務創建，包括 `Microsoft Foundry Agent Service`：

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

或是 [MiniMax](https://platform.minimaxi.com/)，它提供兼容 OpenAI 的 API 且具有大型上下文視窗（最多可達 204K 代幣）：

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

或使用 A2A 協議的遠端代理人：

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

<strong>執行代理人</strong>

代理人使用 `.run` 或 `.run_stream` 方法執行，分別針對非串流或串流回應。

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

每次執行代理人都可以選擇自訂參數，例如代理人使用的 `max_tokens`、代理人可呼叫的 `tools`，甚至是代理人使用的 `model`。

這在需要使用特定模型或工具來完成用戶任務時特別有用。

<strong>工具</strong>

工具可以在定義代理人時設定：

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# 當直接創建一個 ChatAgent 時

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

也可以在執行代理人時設定：

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # 僅為此次運行提供的工具 )
```

<strong>代理人線程</strong>

代理人線程用於處理多輪對話。線程可以透過以下方式建立：

- 使用 `get_new_thread()`，允許該線程隨時間保存
- 在執行代理人時自動建立線程，且該線程只在當前執行期間存在。

創建線程的程式碼如下：

```python
# 建立一個新的執行緒。
thread = agent.get_new_thread() # 使用該執行緒執行代理程式。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

之後可以序列化該線程以便稍後使用：

```python
# 創建一個新執行緒。
thread = agent.get_new_thread() 

# 使用該執行緒運行代理。

response = await agent.run("Hello, how are you?", thread=thread) 

# 將執行緒序列化以便儲存。

serialized_thread = await thread.serialize() 

# 從儲存中加載後反序列化執行緒狀態。

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

<strong>代理人中介軟體</strong>

代理人與工具及大型語言模型（LLM）互動以完成用戶任務。在某些情境下，我們希望在它們之間的互動過程中執行或追蹤一些操作。代理人中介軟體讓我們能通過以下方式實現：

<em>功能中介軟體</em>

此中介軟體允許我們在代理人與其呼叫的功能／工具之間執行某個動作。舉例來說，若想在功能調用時做一些紀錄，就會用到這個中介軟體。

下方程式碼裡，`next` 用於定義是否呼叫下一個中介軟體或實際的功能。

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # 預處理：函式執行前記錄日誌
    print(f"[Function] Calling {context.function.name}")

    # 繼續至下一個中介軟體或函式執行
    await next(context)

    # 後處理：函式執行後記錄日誌
    print(f"[Function] {context.function.name} completed")
```

<em>聊天中介軟體</em>

這個中介軟體允許我們在代理人與 LLM 間的請求過程中執行或記錄動作。

其中包含重要資訊，例如發送給 AI 服務的 `messages`。

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # 預處理：在呼叫 AI 之前記錄日誌
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # 繼續下一個中介軟體或 AI 服務
    await next(context)

    # 後處理：在 AI 回應後記錄日誌
    print("[Chat] AI response received")

```

<strong>代理人記憶</strong>

如 `Agentic Memory` 章節所述，記憶是讓代理人能在不同語境下運作的重要元素。MAF 提供了多種不同類型的記憶：

<em>記憶體內存儲</em>

這是應用程序執行期間線程內部存儲的記憶。

```python
# 建立一個新的執行緒。
thread = agent.get_new_thread() # 使用該執行緒執行代理程序。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

<em>持久消息</em>

這種記憶用於不同會話間保存對話歷史。其定義使用 `chat_message_store_factory`：

```python
from agent_framework import ChatMessageStore

# 建立自訂訊息存放區
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

<em>動態記憶</em>

這種記憶會在代理人執行前加入上下文中。這些記憶可以存放於外部服務，如 mem0：

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

<strong>代理人可觀察性</strong>


可觀察性對於構建可靠且易於維護的具代理系統非常重要。MAF 與 OpenTelemetry 集成，以提供追蹤和計量器，以提升觀察能力。

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

MAF 提供預定義的一系列步驟來完成任務，並將 AI 代理作為這些步驟中的組件。

工作流程由不同組件組成，以便更好地控制流程。工作流程還支持<strong>多代理協同作業</strong>和<strong>檢查點存儲</strong>以保存流程狀態。

工作流程的核心組件包括：

**執行者（Executors）**

執行者接收輸入訊息，執行指定任務，然後產生輸出訊息。這推進工作流程，朝向完成更大的任務。執行者可以是 AI 代理或自訂邏輯。

**邊緣（Edges）**

邊緣用於定義工作流程中訊息的流向。邊緣類型包括：

<em>直接邊緣</em> - 執行者間簡單的一對一連接：

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

<em>條件邊緣</em> - 當特定條件符合時才觸發。例如，當飯店房間不可用時，執行者可以建議其他選項。

<em>分支條件邊緣</em> - 根據定義的條件將訊息導向不同執行者。例如，如果旅客擁有優先權，則其任務將透過另一工作流程處理。

<em>扇出邊緣</em> - 將一則訊息傳送給多個目標。

<em>扇入邊緣</em> - 收集來自多個執行者的訊息並傳送到單一目標。

**事件（Events）**

為了提升對工作流程的觀察能力，MAF 提供內建的執行相關事件，包括：

- `WorkflowStartedEvent`  - 工作流程執行開始
- `WorkflowOutputEvent` - 工作流程產生輸出
- `WorkflowErrorEvent` - 工作流程發生錯誤
- `ExecutorInvokeEvent`  - 執行者開始處理
- `ExecutorCompleteEvent`  -  執行者完成處理
- `RequestInfoEvent` - 發出請求

## 進階 MAF 模式

上述章節涵蓋了 Microsoft Agent Framework 的關鍵概念。隨著您建立更複雜的代理，以下是一些值得考慮的進階模式：

- <strong>中介軟體組合</strong>：使用函數和聊天中介軟體串連多個中介軟體處理程序（如日誌、授權、限流），以細緻控制代理行為。
- <strong>工作流程檢查點</strong>：使用工作流程事件與序列化以保存和恢復長時間執行的代理過程。
- <strong>動態工具選擇</strong>：結合基於工具描述的 RAG 與 MAF 工具註冊，以針對每個查詢只展示相關工具。
- <strong>多代理交接</strong>：利用工作流程邊緣和條件路由管理專門化代理間的交接協調。

## 在 Microsoft Foundry 上託管 LangChain / LangGraph 代理

Microsoft Agent Framework 是<strong>框架互通性</strong>的——您不必侷限於使用 MAF 所寫的代理。如果您已有使用 **LangChain** 或 **LangGraph** 所建的代理，您可以作為 **Microsoft Foundry 託管代理** 運行，由 Foundry 管理執行時、會話、擴展、身分和協議端點，而您的代理邏輯則保持於 LangGraph。

這是通過 `langchain_azure_ai.agents.hosting` 套件完成，該套件透過 Foundry 託管代理使用的相同協議暴露編譯過的 LangGraph 圖。

**1. 安裝 hosting 相關套件：**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` 額外套件會安裝 Foundry 協議庫：`azure-ai-agentserver-responses`（相容 OpenAI 的 `/responses` 端點）與 `azure-ai-agentserver-invocations`（通用的 `/invocations` 端點）。

**2. 選擇 hosting 協議：**

| 協議 | Host 類別 | 端點 | 使用場景 |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | 需要 OpenAI 相容的聊天、串流、回應歷史與會話串接——推薦用於對話代理。 |
| **Invocations** | `InvocationsHostServer` | `/invocations` | 需要自訂 JSON 格式、webhook 風格端點或非對話式處理。 |

由於<strong>Responses API 是 Foundry 中代理式開發的主要 API</strong>，大部分代理建議先使用 `ResponsesHostServer`。

**3. 設定環境變數**（先執行 `az login` 以讓 `DefaultAzureCredential` 可認證）：

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

當代理在 Foundry 中作為託管代理運行時，平台會自動注入 `FOUNDRY_PROJECT_ENDPOINT`。

**4. 以 Responses 協議暴露 LangGraph 代理：**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI 這裡針對 Foundry 項目的 OpenAI 相容（回應）端點。
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

於本機使用 `python main.py` 執行，然後向 `http://localhost:8088/responses` 發送 Responses 請求。

**主要行為特性：**

- <strong>會話</strong>：用戶端通過傳遞 `previous_response_id` 或 `conversation` ID 繼續會話。如果您的圖使用了 LangGraph 檢查點功能，Foundry 會將會話狀態與檢查點做關聯（生產環境使用持久化檢查器；本機測試用 `MemorySaver` 即可）。
- <strong>人工介入</strong>：若您的圖中有使用 LangGraph `interrupt()`，`ResponsesHostServer` 將待處理的中斷表現為 Responses 的 `function_call` / `mcp_approval_request` 項目，客戶端則以相符的 `function_call_output` / `mcp_approval_response` 繼續。
- **部署到 Foundry**：使用 Azure Developer CLI — `azd ext install azure.ai.agents`、`azd ai agent init -m <manifest>`、`azd ai agent run`（本機，需 Docker），接著執行 `azd provision` 及 `azd deploy`。託管代理部署需具備 **Foundry Project Manager** 角色。

此範例的可執行版本置於 [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) 。完整教學（Invocations 協議、自訂請求結構和疑難排解）請參見 [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)。

## 程式碼範例

Microsoft Agent Framework 的程式碼範例可在本倉庫的 `xx-python-agent-framework` 和 `xx-dotnet-agent-framework` 檔案中找到。

## 對 Microsoft Agent Framework 有更多疑問嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者交流，參加辦公時間，並獲得 AI 代理相關問題的解答。
## 前一課程

[AI 代理記憶](../13-agent-memory/README.md)

## 下一課程

[構建電腦使用代理 (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->