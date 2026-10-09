# 探索 Microsoft Agent Framework

![Agent Framework](../../../translated_images/zh-MO/lesson-14-thumbnail.90df0065b9d234ee.webp)

### 簡介

本課程將涵蓋：

- 認識 Microsoft Agent Framework：關鍵特性與價值  
- 探索 Microsoft Agent Framework 的核心概念
- 進階 MAF 模式：工作流程、中介軟體與記憶體

## 學習目標

完成本課程後，您將能夠：

- 使用 Microsoft Agent Framework 建立生產級 AI 代理
- 將 Microsoft Agent Framework 的核心功能應用於您的代理使用案例
- 使用包含工作流程、中介軟體及觀察性的進階模式

## 程式碼範例

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) 的程式碼範例可在本儲存庫中的 `xx-python-agent-framework` 和 `xx-dotnet-agent-framework` 檔案找到。

## 認識 Microsoft Agent Framework

![Framework Intro](../../../translated_images/zh-MO/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) 是微軟用來建構 AI 代理的統一框架。它靈活地解決生產及研究環境中廣泛的代理使用案例，包括：

- <strong>序列代理編排</strong>：在需要一步步工作流程的場景中。
- <strong>並行編排</strong>：在代理需同時完成任務的場景中。
- <strong>群組聊天編排</strong>：在代理可共同合作完成同一任務的場景中。
- <strong>交接編排</strong>：在代理完成子任務後，將任務交接給其他代理的場景中。
- <strong>磁性編排</strong>：在管理代理建立與修改任務清單並協調子代理完成任務的場景中。

為了在生產中交付 AI 代理，MAF 還包括以下功能：

- <strong>可觀察性</strong>：透過 OpenTelemetry，使 AI 代理的每項行動（包括工具調用、編排步驟、推理流程及利用 Microsoft Foundry 儀表板的效能監控）都能被追蹤。
- <strong>安全性</strong>：代理原生托管於 Microsoft Foundry，包含角色基礎存取、私密資料處理與內建內容安全控制。
- <strong>耐久性</strong>：代理線程與工作流程可以暫停、恢復並從錯誤中復原，支持長時間運行的流程。
- <strong>控制</strong>：支援人工介入的工作流程，標記需要人工核准的任務。

Microsoft Agent Framework 也聚焦於互通性，具備：

- <strong>雲端中立性</strong> - 代理可以在容器、本地端及多個不同雲端運行。
- <strong>供應商中立性</strong> - 代理可透過您偏好的 SDK 建立，包括 Azure OpenAI 與 OpenAI。
- <strong>整合開放標準</strong> - 代理能使用 Agent-to-Agent (A2A) 與 Model Context Protocol (MCP) 協定，來發掘及使用其他代理與工具。
- <strong>外掛與連接器</strong> - 可連結到資料與記憶服務，如 Microsoft Fabric、SharePoint、Pinecone 及 Qdrant。

現在讓我們看看這些功能如何應用於 Microsoft Agent Framework 的核心概念。

## Microsoft Agent Framework 的核心概念

### 代理

![Agent Framework](../../../translated_images/zh-MO/agent-components.410a06daf87b4fef.webp)


<strong>建立代理</strong>

代理的建立是透過定義推理服務（LLM 提供者）、
供 AI 代理遵循的一組指令，及指定的 `name`：

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

上述範例使用 `Azure OpenAI`，但代理亦可透過多種服務建立，包括 `Microsoft Foundry Agent Service`：

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

或 [MiniMax](https://platform.minimaxi.com/)，它提供具有大型上下文窗口（最多 204K 令牌）的 OpenAI 相容 API：

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

或使用 A2A 協定的遠端代理：

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

<strong>執行代理</strong>

代理透過 `.run` 或 `.run_stream` 方法執行，分別用於非串流或串流回應。

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

每次代理執行也可以帶有選項，自訂例如代理所用的 `max_tokens`、代理可呼叫的 `tools`，甚至用於代理的 `model`。

此功能在需要特定模型或工具來完成使用者任務時特別有用。

<strong>工具</strong>

工具可以在定義代理時設定：

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# 直接創建一個ChatAgent時

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

也可以在執行代理時設定：

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # 僅供此運行使用的工具 )
```

<strong>代理執行緒</strong>

代理執行緒用於處理多輪對話。執行緒可通過以下方式建立：

- 使用 `get_new_thread()`，使執行緒可隨時間儲存
- 在執行代理時自動建立執行緒，且該執行緒只持續當前執行期間

建立執行緒的程式碼如下：

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() # 使用該執行緒運行代理人。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

隨後您可以序列化該執行緒以便日後使用：

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() 

# 用該執行緒執行代理。

response = await agent.run("Hello, how are you?", thread=thread) 

# 將執行緒序列化以作儲存。

serialized_thread = await thread.serialize() 

# 從儲存中載入後反序列化執行緒狀態。

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

<strong>代理中介軟體</strong>

代理與工具和 LLM 互動來完成使用者任務。在某些情況下，我們想在這些互動間執行或追蹤動作。代理中介軟體使我們能夠透過以下方式做到這點：

<em>功能中介軟體</em>

此中介軟體允許我們在代理與其將呼叫的功能/工具之間執行動作。舉例來說，這可用於在呼叫功能時記錄日誌。

下方程式碼中的 `next` 定義是否呼叫下一個中介軟體或實際功能。

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # 預處理：函數執行前記錄日誌
    print(f"[Function] Calling {context.function.name}")

    # 繼續至下一個中介軟體或函數執行
    await next(context)

    # 後處理：函數執行後記錄日誌
    print(f"[Function] {context.function.name} completed")
```

<em>聊天中介軟體</em>

此中介軟體允許我們在代理與 LLM 之間的請求中執行或記錄動作。

其包含重要資訊，如傳送給 AI 服務的 `messages`。

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # 預處理：在 AI 調用之前記錄日誌
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # 繼續至下一中介軟體或 AI 服務
    await next(context)

    # 後處理：在 AI 回應後記錄日誌
    print("[Chat] AI response received")

```

<strong>代理記憶</strong>

如在 `Agentic Memory` 課程中所述，記憶是使代理能跨不同上下文運作的關鍵元素。MAF 提供多種記憶型態：

<em>記憶體內儲存</em>

這是應用程式執行期間執行緒中儲存的記憶。

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() # 用該執行緒執行代理。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

<em>持久訊息</em>

這用於跨不同會話儲存對話歷史。它透過 `chat_message_store_factory` 定義：

```python
from agent_framework import ChatMessageStore

# 建立一個自訂訊息儲存區
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

<em>動態記憶</em>


這段記憶會在代理運行前被加入到上下文中。這些記憶可以存儲在外部服務中，例如 mem0:

```python
from agent_framework.mem0 import Mem0Provider

# 使用 Mem0 進行高級記憶體功能
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

<strong>代理可觀察性</strong>

可觀察性對於構建可靠且可維護的代理系統非常重要。MAF 與 OpenTelemetry 集成，提供追蹤和度量，以提升可觀察性。

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # 做一啲嘢
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### 工作流

MAF 提供了預定義步驟的工作流來完成任務，並在這些步驟中包含 AI 代理作為組件。

工作流由不同的組件構成，以實現更好的控制流程。工作流還支持<strong>多代理協同</strong>和<strong>檢查點</strong>以保存工作流狀態。

工作流的核心組件包括：

<strong>執行者</strong>

執行者接收輸入訊息，執行指定任務，然後產生輸出訊息。這推動工作流向完成更大任務的方向進展。執行者可以是 AI 代理或自定義邏輯。

<strong>連接邊</strong>

連接邊用於定義工作流中訊息的流向。這些可以是：

<em>直接連接邊</em> - 執行者之間的一對一簡單連接：

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

<em>條件連接邊</em> - 在特定條件達成後啟動。例如，當酒店房間不可用時，執行者可以建議其他選項。

<em>分支選擇連接邊</em> - 根據定義條件將訊息路由至不同執行者。例如，若旅客享有優先通道，其任務將通過另一個工作流處理。

<em>擴散連接邊</em> - 一條訊息發送至多個目標。

<em>匯聚連接邊</em> - 收集來自不同執行者的多條訊息並發送至單一目標。

<strong>事件</strong>

為了更好地觀察工作流，MAF 提供了內建的執行事件，包括：

- `WorkflowStartedEvent`  - 工作流執行開始
- `WorkflowOutputEvent` - 工作流產生輸出
- `WorkflowErrorEvent` - 工作流遇到錯誤
- `ExecutorInvokeEvent`  - 執行者開始處理
- `ExecutorCompleteEvent`  - 執行者完成處理
- `RequestInfoEvent` - 發出請求

## 進階 MAF 模式

上述章節介紹了 Microsoft 代理框架的關鍵概念。在構建更複雜的代理時，可考慮以下進階模式：

- <strong>中介軟體組合</strong>：鏈接多個中介軟體處理器（記錄、認證、速率限制），利用函數和聊天中介軟體，對代理行為進行細粒度控制。
- <strong>工作流檢查點</strong>：使用工作流事件和序列化來保存和恢復長時間運行的代理流程。
- <strong>動態工具選擇</strong>：結合工具描述的 RAG 與 MAF 的工具註冊，根據查詢只展示相關工具。
- <strong>多代理交接</strong>：利用工作流連接邊和條件路由來協調專門代理之間的交接。

## 在 Microsoft Foundry 上托管 LangChain / LangGraph 代理

Microsoft 代理框架是<strong>框架互通的</strong>——您不必限於使用 MAF 寫的代理。如果您已有使用 **LangChain** 或 **LangGraph** 構建的代理，可以將其作為 **Microsoft Foundry 托管代理** 運行，讓 Foundry 管理運行時、會話、擴展、身份及協議端點，您的代理邏輯依然保持在 LangGraph。

這是通過 `langchain_azure_ai.agents.hosting` 套件實現，該套件以與 Foundry 托管代理相同的協議暴露已編譯的 LangGraph 圖。

**1. 安裝 hosting 額外套件：**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` 額外套件安裝 Foundry 協議庫：`azure-ai-agentserver-responses`（與 OpenAI 兼容的 `/responses` 端點）和 `azure-ai-agentserver-invocations`（通用的 `/invocations` 端點）。

**2. 選擇託管協議：**

| 協議 | 主機類別 | 端點 | 適用情況 |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | 您需要 OpenAI 兼容的聊天、串流、響應歷史和對話線程——這是對話代理的推薦預設。 |
| **Invocations** | `InvocationsHostServer` | `/invocations` | 您需自訂 JSON 格式、Webhook 風格端點或非對話式處理。 |

因為<strong>Responses API 是 Foundry 中代理式開發的主要 API</strong>，大部分代理建議先用 `ResponsesHostServer`。

**3. 配置環境變數**（先執行 `az login` 以讓 `DefaultAzureCredential` 認證）：

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

代理稍後作為 Foundry 托管代理運行時，平台會自動注入 `FOUNDRY_PROJECT_ENDPOINT`。

**4. 透過 Responses 協議暴露 LangGraph 代理：**

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

    # ChatOpenAI 係針對 Foundry 計劃嘅 OpenAI 相容（回應）端點。
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

在本地用 `python main.py` 運行，之後可向 `http://localhost:8088/responses` 發送 Responses 請求。

**主要行為：**

- <strong>對話</strong>：客戶端通過傳遞 `previous_response_id` 或 `conversation` ID 來繼續對話。如果您的圖編譯時使用 LangGraph 檢查點功能，Foundry 將會將對話狀態鍵控至該檢查點（在生產環境使用持久檢查點；本地測試 `MemorySaver` 即可）。
- <strong>人機互動過程</strong>：如果您的圖使用 LangGraph `interrupt()`，`ResponsesHostServer` 會將待處理中斷作為 Responses `function_call` / `mcp_approval_request` 項目暴露，客戶端以相應的 `function_call_output` / `mcp_approval_response` 繼續。
- **部署至 Foundry**：使用 Azure Developer CLI —— `azd ext install azure.ai.agents`、`azd ai agent init -m <manifest>`、`azd ai agent run`（本地需 Docker），然後執行 `azd provision` 和 `azd deploy`。托管代理部署需具備<strong>Foundry 專案管理員</strong>權限。

本範例的可執行版本位於 [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)。完整教學（Invocations 協議、自訂請求結構及故障排除）請參考 [將 LangGraph 代理作為 Foundry 托管代理](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)。

## 範例程式碼 

Microsoft 代理框架的範例程式碼可在此存儲庫中，位於 `xx-python-agent-framework` 和 `xx-dotnet-agent-framework` 文件夾。

## 對 Microsoft 代理框架有更多疑問？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者交流，參加辦公時間並獲得 AI 代理問題解答。
## 上一課

[AI 代理的記憶](../13-agent-memory/README.md)

## 下一課


[建立電腦使用代理 (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->