[![如何設計優秀的 AI 代理](../../../translated_images/zh-TW/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(點擊上方圖片觀看本課程影片)_

# 工具使用設計模式

工具很有趣，因為它們讓 AI 代理具備更廣泛的能力範圍。代理不再只有一組有限的動作集合，而是透過添加工具，代理現在可以執行各種不同的動作。在本章中，我們將探討工具使用設計模式，該模式描述 AI 代理如何使用特定工具來達成其目標。

## 介紹

在這堂課中，我們的目標是回答以下問題：

- 什麼是工具使用設計模式？
- 它適用於哪些使用案例？
- 實現此設計模式需要哪些元素／構建模組？
- 使用工具使用設計模式建立值得信賴的 AI 代理有哪些特別的考量？

## 學習目標

完成本課程後，你將能：

- 定義工具使用設計模式及其目的。
- 辨識適合應用工具使用設計模式的使用案例。
- 理解實作此設計模式所需的關鍵元素。
- 認識使用此設計模式確保 AI 代理可信賴性的考量因素。

## 什麼是工具使用設計模式？

<strong>工具使用設計模式</strong> 著重於給予大型語言模型（LLM）與外部工具互動的能力，以達成特定目標。工具是代理執行代碼以完成動作的程式。工具可以是簡單的函式，如計算機，或是調用第三方服務的 API 呼叫，如股價查詢或天氣預報。在 AI 代理的上下文中，工具設計為由代理在 <strong>模型生成的函式呼叫</strong> 後執行。

## 它適用於哪些使用案例？

AI 代理可以利用工具完成複雜任務、檢索資訊或做出決策。工具使用設計模式常用於需要與外部系統動態互動的場景，如資料庫、網路服務或程式碼解譯器。此能力對多種使用案例都有幫助，包括：

- **動態資訊檢索：** 代理可以查詢外部 API 或資料庫以獲取最新資料（例如，查詢 SQLite 資料庫做資料分析、取得股價或天氣資訊）。
- **程式碼執行與解譯：** 代理可執行程式碼或腳本以解數學問題、生成報告或執行模擬。
- **工作流程自動化：** 透過整合排程工具、電子郵件服務或資料管線，自動化重複或多步驟工作流程。
- **客戶支持：** 代理可與 CRM 系統、問題單平台或知識庫互動，以解決用戶問題。
- **內容生成與編輯：** 代理可利用文法檢查器、文本摘要器或內容安全評估工具協助內容創作工作。

## 實現工具使用設計模式需要哪些元素／構建模組？

這些構建模組使 AI 代理能執行廣泛的任務。以下是實現工具使用設計模式所需的關鍵元素：

- **函式／工具 Schema**：可用工具的詳細定義，包括函式名稱、用途、必要參數和預期輸出。這些 Schema 使 LLM 能了解可用工具並構造有效請求。

- <strong>函式執行邏輯</strong>：根據使用者意圖與對話情境決定何時呼叫工具。這可能包含規劃模組、路由機制或決策條件來動態決定工具使用。

- <strong>訊息處理系統</strong>：管理使用者輸入、LLM 回應、工具呼叫及工具輸出之間對話流程的組件。

- <strong>工具整合框架</strong>：連接代理與各式工具的基礎設施，無論是簡單函式或複雜外部服務。

- <strong>錯誤處理與驗證</strong>：處理工具執行失敗、參數驗證及管理非預期回應的機制。

- <strong>狀態管理</strong>：追蹤對話上下文、先前工具互動及持久資料，以確保多回合互動中資料一致性。

接著，我們將更詳細地探討函式／工具呼叫。
 
### 函式／工具呼叫

函式呼叫是我們讓大型語言模型（LLM）與工具互動的主要方式。你常會看到「函式」與「工具」交替使用，因為「函式」（可重用的程式碼區塊）就是代理用來執行任務的「工具」。為了呼叫函式程式碼，LLM 必須根據使用者請求與函式描述進行比對。為此，我們會將包含所有可用函式描述的 schema 傳送給 LLM。LLM 再選擇最適合的函式，並回傳其名稱與參數。接著呼叫該函式，函式回應會送回 LLM，LLM 利用這些資訊回覆使用者請求。

開發者若要為代理實作函式呼叫，需要：

1. 支援函式呼叫的 LLM 模型
2. 包含函式描述的 schema
3. 每個函式的實作程式碼

讓我們用取得城市當前時間的範例說明：

1. **初始化支援函式呼叫的 LLM：**

    並非所有模型都支援函式呼叫，因此要確定你使用的 LLM 支援此功能。     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支援函式呼叫。我們可以從對 Azure OpenAI **回應 API** (穩定版 `/openai/v1/` 端點—不需要 `api_version`) 建立 OpenAI 客戶端開始。

    ```python
    # 初始化 Azure OpenAI 的 OpenAI 用戶端（回應 API，v1 端點）
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **建立函式 Schema**：

    接著定義一份 JSON schema，包含函式名稱、函式功能描述，以及函式參數的名稱與描述。
    再將該 schema 與使用者想查詢舊金山市時間的請求一併傳給先前建立的客戶端。需要注意的是，返回的是 <strong>一個工具呼叫</strong>，而不是問題的最終答案。前面提到，LLM 會回傳它為此任務選擇的函式名稱和將傳入的參數。

    ```python
    # 函式說明供模型閱讀（回應 API 扁平工具格式）
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # 初始用戶訊息
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # 第一次 API 呼叫：請模型使用該函式
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API 在 response.output 中以 function_call 項目返回工具呼叫。
    # 將它們附加到對話中，讓模型在下一輪擁有完整的上下文。
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **執行任務的函式程式碼：**

    現在 LLM 已選擇需要執行的函式，需實作並執行該函式程式碼來完成任務。
    我們可以使用 Python 實作取得當前時間，並且需撰寫程式碼從 response_message 中抽取名稱與參數來取得最終結果。

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # 處理函數呼叫
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # 以 function_call_output 項目回傳工具結果
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # 第二次 API 呼叫：從模型取得最終回應
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

函式呼叫是大部分（如果不是全部）代理工具使用設計的核心，但從零實作有時較具挑戰性。
如同我們在[第 2 課](../../../02-explore-agentic-frameworks)所學，代理框架為我們提供了預建的構建模組來實作工具使用。
 
## 使用代理框架的工具使用範例

以下是使用不同代理框架實作工具使用設計模式的一些範例：

### 微軟代理框架

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">微軟代理框架</a> 是一個用於建構 AI 代理的開源框架。它簡化了函式呼叫的過程，讓你可以使用 `@tool` 裝飾器將 Python 函式定義為工具。框架會處理模型與程式碼間的雙向通訊，並透過 `FoundryChatClient` 提供像是檔案搜尋、程式碼解譯等預建工具的存取。

下圖說明了使用微軟代理框架的函式呼叫流程：

![函式呼叫流程](../../../translated_images/zh-TW/functioncalling-diagram.a84006fc287f6014.webp)

在微軟代理框架中，工具定義為帶有裝飾器的函式。我們能用 `@tool` 裝飾器將先前的 `get_current_time` 函式轉為工具。框架會自動序列化函式及其參數，並建立送往 LLM 的 schema。

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# 建立客戶端
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# 建立代理並使用該工具執行
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### 微軟 Foundry 代理服務

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">微軟 Foundry 代理服務</a> 是較新的代理框架，旨在協助開發者安全地建置、部署及擴充高品質且可延展的 AI 代理，無需管理底層計算與儲存資源。它在企業應用中特別有用，因為是完全受管理服務且具企業級安全性。

與直接使用 LLM API 發展相較，微軟 Foundry 代理服務有以下優勢：

- 自動函式呼叫 — 不必手動解析工具呼叫、執行工具及處理回應，這些作業現由伺服器端完成
- 安全管理的資料 — 不必管理自己的對話狀態，可依賴 threads 儲存所有必要資訊
- 現成工具 — 可使用來訪問資料來源的工具，如 Bing、Azure AI Search 和 Azure Functions。

微軟 Foundry 代理服務的工具可分為兩類：

1. 知識工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">利用 Bing Search 進行根據檢索</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">檔案搜尋</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 搜尋</a>

2. 行動工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函式呼叫</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">程式碼解譯器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 定義工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

此代理服務允許我們將這些工具一起作為一個 `toolset` 使用，並使用 `threads` 追蹤特定對話的訊息歷史。

假設你是 Contoso 公司的銷售代理，想開發一個可以回答銷售數據問題的對話代理。

下圖說明如何使用微軟 Foundry 代理服務分析銷售數據：

![代理服務運作示意圖](../../../translated_images/zh-TW/agent-service-in-action.34fb465c9a84659e.webp)

為了使用這些工具，我們可以建立客戶端並定義工具或工具組。實務上，我們可使用以下 Python 程式碼，LLM 將能根據使用者請求決定使用用戶自定函式 `fetch_sales_data_using_sqlite_query` 或預建的程式碼解譯器。

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query 函數，可在 fetch_sales_data_functions.py 檔案中找到。
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# 初始化工具集
toolset = ToolSet()

# 使用 fetch_sales_data_using_sqlite_query 函數初始化函數呼叫代理，並將其加入工具集
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# 初始化程式碼直譯工具並將其加入工具集。
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用設計模式建立值得信賴的 AI 代理有哪些特別的考量？

LLM 動態生成的 SQL 一般常見的擔憂是安全性，特別是 SQL 注入或惡意操作風險，例如刪除或破壞資料庫。這些擔憂雖合理，但可透過妥善設定資料庫存取權限有效緩解。大多數資料庫做法為設定為唯讀。像 PostgreSQL 或 Azure SQL 服務，應為應用程式分配唯讀（SELECT）角色。

在安全環境中執行應用程式可進一步強化保護。在企業場景中，資料通常從營運系統萃取並轉換到僅可讀取的資料庫或資料倉儲，並具備易於使用的 schema。此策略確保資料安全、效能與可存取性最佳化，且應用程式持有限制的唯讀權限。

## 範例程式碼

- Python 範例：[Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET 範例：[Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## 對工具使用設計模式有更多問題嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他同學互動，參加辦公時間並獲得 AI 代理問題的解答。

## 額外資源

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service 工作坊</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso 創意寫作多代理工作坊</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">微軟代理框架概覽</a>


## 簡單測試這個代理（可選）

在你學會在 [第16課](../16-deploying-scalable-agents/README.md) 部署代理後，你可以用 [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) 對本課的 `TravelToolAgent` 進行簡單測試（它是否仍然呼叫工具並回答？）。有關如何執行，請參考 [`tests/README.md`](../tests/README.md)。

## 前一課

[理解代理設計模式](../03-agentic-design-patterns/README.md)

## 下一課

[代理 RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->