# 探索 Microsoft Agent Framework

![Agent Framework](../../../translated_images/zh-HK/lesson-14-thumbnail.90df0065b9d234ee.webp)

### 簡介

本課程將涵蓋：

- 了解 Microsoft Agent Framework：主要功能與價值  
- 探索 Microsoft Agent Framework 的核心概念
- 進階的 MAF 模式：工作流程、中介軟體與記憶功能

## 學習目標

完成本課程後，您將能夠：

- 使用 Microsoft Agent Framework 建置生產等級的 AI 代理
- 將 Microsoft Agent Framework 的核心功能應用於您的代理使用案例
- 使用進階模式，包括工作流程、中介軟體及可觀察性

## 程式碼範例 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) 的程式碼範例可於此存放庫中的 `xx-python-agent-framework` 與 `xx-dotnet-agent-framework` 檔案找到。

## 了解 Microsoft Agent Framework

![Framework Intro](../../../translated_images/zh-HK/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) 是微軟建構 AI 代理的統一框架。它提供彈性以應對在生產與研究環境中所見的各種代理使用案例，包括：

- <strong>序列代理編排</strong>，適用於需要逐步工作流程的場景。
- <strong>並行編排</strong>，適用於代理需同時完成任務的場景。
- <strong>群組聊天編排</strong>，適用於代理能協同合作完成同一任務的場景。
- <strong>交接編排</strong>，適用於代理在子任務完成後交接任務的場景。
- <strong>磁性編排</strong>，適用於管理代理創建和修改任務清單並負責子代理協作完成任務的場景。

為了在生產環境中部署 AI 代理，MAF 也包括：

- <strong>可觀察性</strong>，透過 OpenTelemetry 追蹤 AI 代理的每個動作，包括工具呼叫、編排步驟、推理流程，以及透過 Microsoft Foundry 儀表板的效能監控。
- <strong>安全性</strong>，代理原生托管於 Microsoft Foundry，其中包含角色基礎存取控制、私密資料處理及內建內容安全機制。
- <strong>耐久性</strong>，代理線程與工作流程可暫停、恢復並從錯誤中復原，支援長時間運行的程序。
- <strong>控制</strong>，支援人為介入工作流程，標記某些任務需人類批准。

Microsoft Agent Framework 同時著重於互通性，透過：

- <strong>雲端無關性</strong> — 代理可在容器、內部部署及多個不同雲端執行。
- <strong>提供者無關性</strong> — 可依您偏好的 SDK（包括 Azure OpenAI 與 OpenAI）建立代理。
- <strong>整合開放標準</strong> — 代理可利用 Agent-to-Agent (A2A) 和模型上下文協議（MCP）等協定，發現並使用其他代理和工具。
- <strong>插件與連接器</strong> — 可連接至資料與記憶服務，如 Microsoft Fabric、SharePoint、Pinecone 及 Qdrant。

現在讓我們看看這些功能如何應用於 Microsoft Agent Framework 的一些核心概念。

## Microsoft Agent Framework 的核心概念

### 代理

![Agent Framework](../../../translated_images/zh-HK/agent-components.410a06daf87b4fef.webp)

<strong>建立代理</strong>

建立代理的方法是定義推理服務 (LLM 提供者)、
AI 代理需遵循的一組指令，及指定的 `name`：


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

上述使用的是 `Azure OpenAI`，但代理可以使用多種服務建立，包括 `Microsoft Foundry Agent Service`：

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

或者 [MiniMax](https://platform.minimaxi.com/)，提供與 OpenAI 相容且擁有大型上下文視窗（最大可達 204K 代幣）的 API：

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

或使用 A2A 協議的遠端代理：

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

<strong>運行代理</strong>

代理是透過 `.run` 或 `.run_stream` 方法運行，以取得非串流或串流的回應。

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

每次代理運行也可以有選項自訂不同參數，例如代理使用的 `max_tokens`、代理能調用的 `tools`，甚至是代理使用的 `model` 本身。

這在需要特定模型或工具來完成使用者任務時非常有用。

<strong>工具</strong>

工具可以在定義代理時設定：

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# 直接建立 ChatAgent 時

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

也可以在運行代理時設定：

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # 僅提供此運行使用的工具 )
```

<strong>代理執行緒</strong>

代理執行緒用於處理多輪對話。執行緒可以透過以下方式建立：

- 使用 `get_new_thread()`，使執行緒能夠被持續保存
- 在運行代理時自動建立執行緒，且執行緒僅在該次運行期間存在。

建立執行緒的程式碼如下：

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() # 使用該執行緒運行代理。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

之後你可以序列化執行緒以便後續存取：

```python
# 創建一個新線程。
thread = agent.get_new_thread() 

# 用該線程運行代理。

response = await agent.run("Hello, how are you?", thread=thread) 

# 將線程序列化以便存儲。

serialized_thread = await thread.serialize() 

# 從存儲載入後反序列化線程狀態。

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

<strong>代理中介軟體</strong>

代理會與工具及大型語言模型互動以完成使用者的任務。在某些情境下，我們希望在這些互動中執行或追蹤某些動作。代理中介軟體使我們能透過以下方式達到此目的：

<em>函式中介軟體</em>

該中介軟體允許我們在代理與它將呼叫的函式/工具之間執行動作。使用情境範例是在函式呼叫時進行日誌記錄。

下方程式碼中，`next` 決定是否呼叫下一個中介軟體或實際函式。

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # 預處理：函數執行前記錄日誌
    print(f"[Function] Calling {context.function.name}")

    # 繼續至下一個中介軟件或函數執行
    await next(context)

    # 後處理：函數執行後記錄日誌
    print(f"[Function] {context.function.name} completed")
```

<em>聊天中介軟體</em>

該中介軟體允許我們在代理與大型語言模型間的請求階段執行或記錄動作。

它包含重要訊息，例如傳送給 AI 服務的 `messages`。

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # 預處理：在調用 AI 前記錄日誌
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # 繼續至下一個中介軟件或 AI 服務
    await next(context)

    # 後處理：在 AI 回應後記錄日誌
    print("[Chat] AI response received")

```

<strong>代理記憶體</strong>

如 `Agentic Memory` 課程所述，記憶體是使代理能在不同上下文中運作的關鍵元素。MAF 提供了幾種不同類型的記憶體：

<em>記憶體中儲存</em>

這是在應用執行緒中運行時儲存的記憶。

```python
# 建立一個新執行緒。
thread = agent.get_new_thread() # 使用該執行緒運行代理。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

<em>持久訊息</em>

此記憶用於跨不同會話儲存對話歷史。它是透過 `chat_message_store_factory` 定義的：

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

<em>動態記憶</em>

這類記憶會在代理運行前加入上下文中。這些記憶可以存放於外部服務，例如 mem0：

```python
from agent_framework.mem0 import Mem0Provider

# 使用 Mem0 進行高階記憶體功能
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


可觀察性對於構建可靠且易於維護的智能代理系統非常重要。MAF 整合了 OpenTelemetry，以提供追蹤和計量，增強可觀察性。

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

MAF 提供了預定義的工作流程，這些工作流程是用於完成任務的步驟，並在這些步驟中包含 AI 代理作為組件。

工作流程由不同組件組成，允許更好的流程控制。工作流程還支持<strong>多代理協調</strong>和<strong>檢查點</strong>以保存工作流程狀態。

工作流程的核心組件包括：

**執行者（Executors）**

執行者接收輸入消息，執行指定任務，然後產生輸出消息。這推動工作流程向完成更大任務邁進。執行者可以是 AI 代理或自定義邏輯。

**邊（Edges）**

邊用來定義工作流程中消息的流向。這些可包括：

<em>直接邊</em> - 執行者之間一對一的簡單連接：

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

<em>條件邊</em> - 滿足特定條件時啟動。例如，當旅館房間不可用時，執行者可建議其他選項。

*切換-案例邊* - 根據定義條件將消息路由到不同的執行者。例如，如果旅遊客戶享有優先權，他們的任務將透過另一個工作流程處理。

<em>放射邊</em> - 將一則消息發送到多個目標。

<em>匯聚邊</em> - 從不同執行者收集多條消息，然後發送到一個目標。

<strong>事件</strong>

為了增強對工作流程的可觀察性，MAF 提供了內建的執行事件，包括：

- `WorkflowStartedEvent`  - 工作流程執行開始
- `WorkflowOutputEvent` - 工作流程產生輸出
- `WorkflowErrorEvent` - 工作流程遇到錯誤
- `ExecutorInvokeEvent`  - 執行者開始處理
- `ExecutorCompleteEvent`  -  執行者完成處理
- `RequestInfoEvent` - 發出請求

## 進階 MAF 模式

以上章節涵蓋 Microsoft Agent Framework 的核心概念。當您構建更複雜的代理時，這裡有一些進階模式可供考慮：

- <strong>中介軟體組合</strong>：鏈接多個中介軟體處理程序（記錄、身份驗證、速率限制），使用函式與聊天中介軟體對代理行為進行細致控制。
- <strong>工作流程檢查點</strong>：利用工作流程事件和序列化來保存和恢復長時間執行的代理流程。
- <strong>動態工具選擇</strong>：結合工具描述的 RAG 與 MAF 的工具註冊，只針對每個查詢提供相關工具。
- <strong>多代理交接</strong>：利用工作流程邊和條件路由來編排專門代理間的交接。

## 在 Microsoft Foundry 上託管 LangChain / LangGraph 代理

Microsoft Agent Framework 是<strong>框架互操作</strong>的 — 您不必只限於用 MAF 編寫的代理。如果您已有用 **LangChain** 或 **LangGraph** 編寫的代理，可以將其作為 **Microsoft Foundry 託管代理** 運行，由 Foundry 管理執行時、會話、擴展、身份和協定端點，而您的代理邏輯仍保留在 LangGraph。

這是通過 `langchain_azure_ai.agents.hosting` 套件完成的，此套件透過 Foundry 託管代理使用的相同協定暴露編譯後的 LangGraph 圖。

**1. 安裝 hosting 額外套件：**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` 額外套件安裝 Foundry 協定庫：`azure-ai-agentserver-responses`（OpenAI 兼容的 `/responses` 端點）和 `azure-ai-agentserver-invocations`（通用 `/invocations` 端點）。

**2. 選擇 hosting 協定：**

| 協定 | 主機類別 | 端點 | 使用情境 |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | 需要 OpenAI 兼容的聊天、串流、回應歷史和對話串連 — 推薦用於對話代理。 |
| **Invocations** | `InvocationsHostServer` | `/invocations` | 需要自定義 JSON 結構、Webhook 風格端點或非對話式處理。 |

因為 **Responses API 是 Foundry 中代理風格開發的主要 API**，大多數代理建議使用 `ResponsesHostServer`。

**3. 配置環境變數**（先執行 `az login` 以便 `DefaultAzureCredential` 認證）：

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

當代理稍後作為 Foundry 託管代理運行時，平台會自動注入 `FOUNDRY_PROJECT_ENDPOINT`。

**4. 通過 Responses 協定暴露 LangGraph 代理：**

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

    # ChatOpenAI 這度係針對 Foundry 項目嘅 OpenAI 相容（Responses）端點。
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

於本機運行 `python main.py`，然後向 `http://localhost:8088/responses` 發送 Responses 請求。

**主要行為：**

- <strong>對話</strong>：用戶端透過傳遞 `previous_response_id` 或 `conversation` ID 繼續對話。若您的圖編譯時用了 LangGraph 檢查點器，Foundry 會將對話狀態綁定至檢查點（生產環境使用持久檢查點器；本地測試用 `MemorySaver` 即可）。
- <strong>人機協作</strong>：若您的圖使用 LangGraph 的 `interrupt()`，`ResponsesHostServer` 會將待處理中斷顯示為 Responses 的 `function_call` / `mcp_approval_request` 項目，客戶端則通過匹配的 `function_call_output` / `mcp_approval_response` 繼續。
- **部署至 Foundry**：使用 Azure Developer CLI — `azd ext install azure.ai.agents`，`azd ai agent init -m <manifest>`，`azd ai agent run`（本地，需 Docker），再執行 `azd provision` 和 `azd deploy`。託管代理部署需要 **Foundry 項目經理** 角色。

這個範例的可運行版本位於 [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)。完整教學（含 Invocations 協定、自定義請求架構及故障排除）請參閱 [在 Foundry 上將 LangGraph 代理作為託管代理](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)。

## 程式碼範例 

Microsoft Agent Framework 的程式碼範例可於本儲存庫中 `xx-python-agent-framework` 和 `xx-dotnet-agent-framework` 檔案找到。

## 對 Microsoft Agent Framework 還有更多疑問嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者交流，參加線上諮詢並獲得 AI 代理問題解答。
## 上一課

[AI 代理的記憶](../13-agent-memory/README.md)

## 下一課

[建立電腦使用代理（CUA）](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->