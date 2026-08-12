# 探索 Microsoft Agent Framework

![Agent Framework](../../../translated_images/zh-MO/lesson-14-thumbnail.90df0065b9d234ee.webp)

### 介紹

本課程將涵蓋：

- 了解 Microsoft Agent Framework：主要特點與價值  
- 探索 Microsoft Agent Framework 的關鍵概念
- 進階 MAF 模式：工作流程、中介軟體和記憶體

## 學習目標

完成本課程後，你將會知道如何：

- 使用 Microsoft Agent Framework 建立可投入生產的 AI 代理
- 將 Microsoft Agent Framework 的核心功能套用到你的代理使用案例中
- 使用包括工作流程、中介軟體和可觀察性等進階模式

## 代碼範例

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) 的代碼範例可以在此存儲庫中的 `xx-python-agent-framework` 與 `xx-dotnet-agent-framework` 檔案中找到。

## 了解 Microsoft Agent Framework

![Framework Intro](../../../translated_images/zh-MO/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) 是微軟用來建構 AI 代理的統一框架。它具備靈活性，能解決生產與研究環境中各種代理使用案例，包括：

- <strong>序列代理協同</strong>，適用於需要逐步工作流程的場景。
- <strong>並行協同</strong>，適用於代理需要同時完成任務的場景。
- <strong>群組聊天協同</strong>，適用於代理可共同合作完成同一任務的場景。
- <strong>任務交接協同</strong>，適用於代理在完成子任務後將任務交接給下一位代理的場景。
- <strong>磁性協同</strong>，適用於管理代理建立和修改任務列表並協調子代理完成任務的場景。

要實現 AI 代理於生產環境的運作，MAF 還包含以下功能：

- <strong>可觀察性</strong>，通過使用 OpenTelemetry，監控 AI 代理的每一項行動，包括工具調用、協同步驟、推理流程，以及透過 Microsoft Foundry 儀錶板進行效能監控。
- <strong>安全性</strong>，代理原生託管於 Microsoft Foundry，包含角色基礎存取控制、私有資料處理及內建內容安全等安全控管。
- <strong>耐久性</strong>，代理線程與工作流程可暫停、繼續並錯誤復原，適合長時間運作的流程。
- <strong>控制</strong>，支持人類介入的工作流程，任務標記為需人類審核。

Microsoft Agent Framework 也強調互操作性，包括：

- <strong>雲端中立</strong> — 代理可運行於容器、內部部署及多種不同雲端環境。
- <strong>供應商中立</strong> — 可透過你偏好的 SDK 建立代理，包括 Azure OpenAI 與 OpenAI。
- <strong>整合開放標準</strong> — 代理可使用如 Agent-to-Agent (A2A) 與模型上下文協定 (MCP) 等協議，發現及使用其他代理與工具。
- <strong>外掛與連接器</strong> — 可連接至資料與記憶體服務，如 Microsoft Fabric、SharePoint、Pinecone 和 Qdrant。

讓我們看看這些功能如何應用於 Microsoft Agent Framework 的一些核心概念。

## Microsoft Agent Framework 的關鍵概念

### 代理

![Agent Framework](../../../translated_images/zh-MO/agent-components.410a06daf87b4fef.webp)

<strong>建立代理</strong>

建立代理是透過定義推論服務（LLM 提供者）、
一組 AI 代理所需遵循的指令，以及一個指定的 `name` 來完成：


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

以上範例使用的是 `Azure OpenAI`，但代理人也可以使用包括 `Microsoft Foundry Agent Service` 在內的各種服務來建立：

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

或是 [MiniMax](https://platform.minimaxi.com/)，它提供了具有大型上下文視窗（最多 204K 代幣）的 OpenAI 相容 API：

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

或使用 A2A 協議的遠端代理人：

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

<strong>運行代理人</strong>

代理人透過 `.run` 或 `.run_stream` 方法運行，分別對應非串流或串流的回應。

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

每次運行代理人時，也可以帶入選項以自訂代理人使用的參數，如 `max_tokens`、代理人能調用的 `tools`，甚至使用的 `model` 本身。

這在需要特定模型或工具完成用戶任務的情況下非常有用。

<strong>工具</strong>

定義代理人時可以設定工具：

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# 當直接建立 ChatAgent時

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

運行代理人時也可以設定工具：

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # 此工具僅供本次運行使用 )
```

<strong>代理執行緒</strong>

代理執行緒用以處理多輪對話。執行緒可以透過以下方式建立：

- 使用 `get_new_thread()`，讓該執行緒可被保存起來以供後續使用
- 在運行代理人時自動建立執行緒，且該執行緒只在當前運行期間存在

建立執行緒的程式碼示例如下：

```python
# 建立一個新線程。
thread = agent.get_new_thread() # 用該線程執行代理。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

您可以序列化該執行緒以便存儲日後使用：

```python
# 建立一個新的執行緒。
thread = agent.get_new_thread() 

# 使用該執行緒執行代理。

response = await agent.run("Hello, how are you?", thread=thread) 

# 將執行緒序列化以便儲存。

serialized_thread = await thread.serialize() 

# 從儲存中載入後反序列化執行緒狀態。

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

<strong>代理中介軟體</strong>

代理人與工具及大型語言模型互動以完成用戶任務。在某些場景中，我們希望在這些互動之間執行或追蹤某些操作。代理中介軟體讓我們能夠做到這點，方式包括：

<em>函式中介軟體</em>

此中介軟體允許我們在代理人與它調用的函式／工具之間執行動作。例如可能在函式呼叫時做一些日誌紀錄。

以下程式碼中，`next` 定義了是否呼叫下一個中介軟體或實際的函式。

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # 前置處理：函數執行前記錄日誌
    print(f"[Function] Calling {context.function.name}")

    # 繼續執行下一個中介軟件或函數
    await next(context)

    # 後置處理：函數執行後記錄日誌
    print(f"[Function] {context.function.name} completed")
```

<em>聊天中介軟體</em>

此中介軟體允許我們在代理人與大型語言模型的請求之間執行或記錄動作。

它包含例如發送給 AI 服務的 `messages` 等重要資訊。

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # 預處理：在呼叫 AI 之前進行記錄
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # 繼續執行下一個中介軟體或 AI 服務
    await next(context)

    # 後處理：在 AI 回應後進行記錄
    print("[Chat] AI response received")

```

<strong>代理記憶體</strong>

如 `Agentic Memory` 課程中所述，記憶體是使代理人能在不同上下文中運作的重要元素。MAF 提供了多種不同類型的記憶體：

<em>記憶體內存儲</em>

這是應用執行時，在執行緒中所保存的記憶體。

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() # 使用該執行緒運行代理。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

<em>持久化訊息</em>

用於跨不同會話存儲對話歷史，透過 `chat_message_store_factory` 定義：

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

<em>動態記憶體</em>

在運行代理人之前，此類記憶會被新增至上下文中。這些記憶可以儲存在像 mem0 這類外部服務：

```python
from agent_framework.mem0 import Mem0Provider

# 使用 Mem0 以獲取進階記憶體功能
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

<strong>代理可觀測性</strong>


觀察性對於構建可靠且可維護的自治系統非常重要。MAF 與 OpenTelemetry 集成，提供追蹤和計量以提升觀察性。

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

MAF 提供預定義步驟的工作流程來完成任務，並在這些步驟中包括 AI 代理作為組件。

工作流程由不同組件組成，以允許更好的控制流程。工作流程還支持<strong>多代理協作</strong>和<strong>檢查點</strong>以保存流程狀態。

工作流程的核心組件有：

<strong>執行者</strong>

執行者接收輸入消息，執行指派的任務，然後產生輸出消息。這推動工作流程向完成更大的任務前進。執行者可以是 AI 代理或自訂邏輯。

<strong>邊緣</strong>

邊緣用來定義工作流程中消息的流向。這些可以包括：

<em>直連邊緣</em> - 執行者之間簡單的一對一連接：

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

<em>條件邊緣</em> - 當特定條件達成後啟動。例如，當飯店房間無法預訂時，執行者可以建議其他選擇。

<em>分支條件邊緣</em> - 根據定義條件將消息路由到不同執行者。例如，如果旅遊客戶有優先權訪問，他們的任務將通過另一個工作流程處理。

<em>分散邊緣</em> - 將一則消息發送到多個目標。

<em>聚合邊緣</em> - 收集來自多個執行者的多則消息並發送到一個目標。

<strong>事件</strong>

為了提供更好的工作流程觀察性，MAF 提供內建的執行事件，包括：

- `WorkflowStartedEvent`  - 工作流程執行開始
- `WorkflowOutputEvent` - 工作流程產生輸出
- `WorkflowErrorEvent` - 工作流程遇到錯誤
- `ExecutorInvokeEvent`  - 執行者開始處理
- `ExecutorCompleteEvent`  -  執行者完成處理
- `RequestInfoEvent` - 發出請求

## 進階 MAF 模式

上述章節涵蓋了 Microsoft Agent Framework 的關鍵概念。當你構建更複雜的代理時，以下是一些值得考慮的進階模式：

- <strong>中介軟體組合</strong>：使用函數和聊天中介軟體連接多個中介軟體處理程序（記錄、驗證、頻率限制）以精細控制代理行為。
- <strong>工作流程檢查點</strong>：使用工作流程事件和序列化來保存和恢復長時間運行的代理過程。
- <strong>動態工具選擇</strong>：結合對工具描述的 RAG 與 MAF 的工具註冊，只為每次查詢呈現相關工具。
- <strong>多代理交接</strong>：使用工作流程邊緣和條件路由來協調專門代理之間的交接。

## 在 Microsoft Foundry 上主機 LangChain / LangGraph 代理

Microsoft Agent Framework 是<strong>框架可互操作的</strong>——你不限於使用 MAF 編寫的代理。如果你已經有使用 **LangChain** 或 **LangGraph** 建立的代理，可以將其作為 **Microsoft Foundry 託管代理** 運行，讓 Foundry 管理執行時、會話、擴展、身份及通訊協定端點，而你的代理邏輯仍然保留在 LangGraph。

這是通過 `langchain_azure_ai.agents.hosting` 套件完成的，該套件在 Foundry 託管代理使用的相同協議上暴露已編譯的 LangGraph 圖。

**1. 安裝 hosting 附加包：**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` 附加包安裝 Foundry 通訊協定庫：`azure-ai-agentserver-responses`（OpenAI 相容的 `/responses` 端點）和 `azure-ai-agentserver-invocations`（通用的 `/invocations` 端點）。

**2. 選擇 hosting 協議：**

| 協議 | 主機類別 | 端點 | 適用場合 |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | 你想要相容 OpenAI 的聊天、串流、回應歷史和對話線索——推薦的預設對話代理協議。 |
| **Invocations** | `InvocationsHostServer` | `/invocations` | 你需要自訂 JSON 格式、webhook 風格端點或非對話式處理。 |

因為<strong>Responses API 是 Foundry 中主要的代理式開發 API</strong>，大多數代理建議從 `ResponsesHostServer` 開始。

**3. 配置環境變數**（先執行 `az login` 以便 `DefaultAzureCredential` 認證）：

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

當代理日後作為 Foundry 託管代理執行時，平台會自動注入 `FOUNDRY_PROJECT_ENDPOINT`。

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

    # ChatOpenAI 這度針對 Foundry 項目嘅 OpenAI 兼容（響應）端點設計。
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

在本地執行 `python main.py`，然後向 `http://localhost:8088/responses` 發送 Responses 請求。

**關鍵行為：**

- <strong>對話</strong>：客戶端通過傳遞 `previous_response_id` 或 `conversation` ID 繼續對話。如果你的圖已用 LangGraph 檢查點編譯，Foundry 將對話狀態與檢查點關聯（生產環境使用耐久性檢查點；本地測試 `MemorySaver` 可）。
- <strong>人機迴路</strong>：如果你的圖使用 LangGraph `interrupt()`，`ResponsesHostServer` 會將待處理的中斷以 Responses `function_call` / `mcp_approval_request` 項目顯示，客戶端以對應的 `function_call_output` / `mcp_approval_response` 繼續。
- **部署到 Foundry**：使用 Azure 開發者 CLI — `azd ext install azure.ai.agents`、`azd ai agent init -m <manifest>`、`azd ai agent run`（本地，需 Docker），然後執行 `azd provision` 和 `azd deploy`。託管代理部署需要 **Foundry 專案管理員** 角色。

可運行的範例位於 [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)。完整教學（Invocations 協議、自訂請求結構和除錯）請參見 [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)。

## 程式碼範例

Microsoft Agent Framework 的程式碼範例可在此存放庫中 `xx-python-agent-framework` 和 `xx-dotnet-agent-framework` 檔案找到。

## 還有更多關於 Microsoft Agent Framework 的問題嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，與其他學習者交流，參加辦公時間並獲得 AI 代理問題的解答。
## 上一課

[AI 代理的記憶](../13-agent-memory/README.md)

## 下一課

[構建電腦使用代理 (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->