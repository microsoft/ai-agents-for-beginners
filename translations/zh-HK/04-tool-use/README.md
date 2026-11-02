[![如何設計優秀的 AI 代理](../../../translated_images/zh-HK/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(點擊上方圖片觀看本課程影片)_

# 工具使用設計模式

工具很有趣，因為它們允許 AI 代理擁有更廣泛的能力。代理不再僅限於執行有限的一組動作，透過添加工具，代理現在可以執行各種動作。在本章中，我們將探討工具使用設計模式，說明 AI 代理如何利用特定工具達成目標。

## 介紹

在本課程中，我們將回答以下問題：

- 什麼是工具使用設計模式？
- 它適用於哪些使用案例？
- 實現該設計模式需要哪些元素/構建塊？
- 使用工具使用設計模式來構建值得信賴的 AI 代理有哪些特殊考慮？

## 學習目標

完成本課程後，你將能夠：

- 定義工具使用設計模式及其目的。
- 識別適合應用工具使用設計模式的使用案例。
- 理解實現該設計模式所需的關鍵元素。
- 認識使用該設計模式確保 AI 代理可信度的考量。

## 什麼是工具使用設計模式？

<strong>工具使用設計模式</strong> 聚焦於賦予大型語言模型（LLM）與外部工具互動的能力以達成特定目標。工具是代理可執行的程式碼，以執行動作。工具可以是簡單函式，如計算機，或是第三方服務的 API 呼叫，如股票價格查詢或天氣預報。在 AI 代理的情境中，工具設計用於回應<strong>模型產生的函式呼叫</strong>由代理執行。

## 它適用於哪些使用案例？

AI 代理可以利用工具完成複雜任務、檢索資訊或做出決策。工具使用設計模式常用於需與外部系統（如資料庫、網路服務、程式碼解譯器）動態互動的場景。其應用涵蓋多個使用案例，包括：

- **動態資訊檢索：** 代理能查詢外部 API 或資料庫，取得最新數據（例如，使用 SQLite 資料庫做資料分析，查詢股票價格或天氣資訊）。
- **程式碼執行與解譯：** 代理能執行程式碼或腳本，解決數學問題、產生報告、或進行模擬。
- **工作流程自動化：** 透過整合任務排程器、電子郵件服務或資料管線，自動化重複或多步驟工作流程。
- **客戶支援：** 代理能與 CRM 系統、客服平台或知識庫互動，解決用戶問題。
- **內容生成與編輯：** 代理能運用語法檢查器、文本摘要器或內容安全評估工具，協助內容創作任務。

## 實現工具使用設計模式所需元素/構建塊是什麼？

這些構建塊允許 AI 代理執行廣泛任務。讓我們來看實現工具使用設計模式的關鍵元素：

- **函式/工具架構（Function/Tool Schemas）**：可用工具的詳細定義，包括函式名稱、目的、所需參數以及預期輸出。這些架構讓 LLM 了解可用工具及如何構造有效請求。

- **函式執行邏輯（Function Execution Logic）**：根據使用者意圖與對話上下文，控制何時及如何調用工具。可能包含規劃模組、路由機制或決策流程以動態決定工具使用。

- **訊息處理系統（Message Handling System）**：管理使用者輸入、LLM 回應、工具呼叫及工具輸出之間的對話流程。

- **工具整合框架（Tool Integration Framework）**：將代理連結至各種工具的基礎設施，無論是簡單函式或複雜外部服務。

- **錯誤處理與驗證（Error Handling & Validation）**：處理工具執行失敗、參數驗證及非預期回應的機制。

- **狀態管理（State Management）**：追蹤對話上下文、先前工具互動及持久化資料，確保多輪互動中一致性。

接著，我們更詳細地看函式/工具呼叫。
 
### 函式/工具呼叫

函式呼叫是我們使大型語言模型（LLM）與工具互動的主要方式。你常會見到「函式」和「工具」互換使用，因為「函式」(可重用程式碼區塊) 即是代理執行任務所用的「工具」。為了能調用函式的程式碼，LLM 必須比較使用者的請求與函式描述。為此，會將包含所有可用函式描述的 schema 傳給 LLM。LLM 接著選擇最適合該任務的函式，並回傳其名稱與參數。呼叫該函式，將其回應傳回給 LLM，LLM 再利用此資訊回應使用者請求。

開發者若要為代理實作函式呼叫，需要：

1. 支援函式呼叫的 LLM 模型
2. 包含函式描述的 schema
3. 每個被描述函式的程式碼

我們以取得某城市當前時間為例說明：

1. **初始化支援函式呼叫的 LLM：**

    不是所有模型都支援函式呼叫，使用前請確認你的 LLM 有此能力。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支援函式呼叫。我們可以從呼叫 Azure OpenAI **Responses API**（穩定版 `/openai/v1/` 端點－無需 `api_version`）開始。 

    ```python
    # 初始化 Azure OpenAI 的 OpenAI 客戶端（回應 API，v1 端點）
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **建立函式 Schema：**

    接著定義一個 JSON schema，包含函式名稱、函式功能描述，以及函式參數的名稱與描述。
    然後將此 schema 與使用者詢問「取得舊金山時間」的請求一同傳給先前創建的客戶端。要注意的是，回傳的是<strong>工具呼叫</strong>，<strong>非</strong>問題的最終答案。正如前述，LLM 回傳選定的函式名稱及將傳遞參數。

    ```python
    # 模型閱讀用的功能描述（回應 API 扁平工具格式）
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

    # 第一次 API 調用：請模型使用該函數
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API 在 response.output 中以 function_call 項目回傳工具調用。
    # 將它們附加到對話中，讓模型在下一輪擁有完整上下文。
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **執行任務所需的函式程式碼：**

    現在 LLM 已選出要執行的函式，需實作並執行該程式碼完成任務。
    我們可用 Python 實作取得當前時間的程式碼。也需撰寫程式碼從 response_message 中取出函式名稱與參數以取得最終結果。

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
    # 處理函數調用
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # 將工具結果作為 function_call_output 項目返回
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # 第二次 API 調用：從模型獲取最終回應
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

函式呼叫是大多數（若非全部）代理工具使用設計的核心，但從零實作有時頗具挑戰性。
正如我們在[課程 2](../../../02-explore-agentic-frameworks)中了解到，代理框架為我們提供現成構建塊以實現工具使用。
 
## 使用代理框架的工具使用範例

以下是使用不同代理框架實現工具使用設計模式的範例：

### 微軟代理框架

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">微軟代理框架</a> 是一個開源 AI 框架，用於構建 AI 代理。它簡化了函式呼叫的使用，允許你使用 `@tool` 裝飾器將工具定義為 Python 函式。該框架負責處理模型與你的程式碼間的來回通信，並提供預建工具，如 File Search 和 Code Interpreter，透過 `FoundryChatClient` 存取。

下列示意圖說明了使用微軟代理框架的函式呼叫流程：

![function calling](../../../translated_images/zh-HK/functioncalling-diagram.a84006fc287f6014.webp)

在微軟代理框架中，工具被定義為帶裝飾器的函式。我們可以把之前看到的 `get_current_time` 函式用 `@tool` 裝飾轉成工具。框架會自動序列化該函式及其參數，建立要發送給 LLM 的 schema。

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

# 建立代理並使用工具運行
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### 微軟 Foundry 代理服務

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">微軟 Foundry 代理服務</a> 是較新的代理框架，能讓開發者安全地構建、部署及擴展高品質且可擴充的 AI 代理，而無需管理底層運算與儲存資源。它對企業應用特別有用，因為它是全管理服務，具備企業級安全性。

相較於直接使用 LLM API，微軟 Foundry 代理服務提供一些優勢，包括：

- 自動工具呼叫 — 無需解析工具呼叫、調用工具及處理回應，所有這些皆在伺服器端完成
- 安全管理的資料 — 無需自行管理對話狀態，可依賴執行緒以存儲所有必要資訊
- 開箱即用工具 — 可用來與資料來源互動的工具，如 Bing、Azure AI Search 與 Azure Functions。

微軟 Foundry 代理服務所提供的工具分為兩種類型：

1. 知識工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">使用 Bing 搜索作為資訊基礎</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">檔案搜尋</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 搜索</a>

2. 動作工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函式呼叫</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">程式碼解譯器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 定義工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

代理服務使我們能將這些工具組合成 `toolset` 一起使用。它也利用 `threads` 來追蹤特定對話的資訊歷史。

假設你是 Contoso 公司的銷售代理，想開發一個可回答銷售數據問題的對話代理。

下圖示範如何使用微軟 Foundry 代理服務分析你的銷售數據：

![Agentic Service In Action](../../../translated_images/zh-HK/agent-service-in-action.34fb465c9a84659e.webp)

想用這些服務中的任一工具，我們可以建立客戶端並定義工具或工具組。實際操作時，可以使用以下 Python 程式碼。LLM 將能依使用者請求決定使用用戶創建的 `fetch_sales_data_using_sqlite_query` 函式或預建的程式碼解譯器。

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

# 初始化工具組
toolset = ToolSet()

# 使用 fetch_sales_data_using_sqlite_query 函數初始化函數調用代理，並將其加入工具組
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# 初始化程式碼解釋器工具並將其加入工具組。
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用設計模式構建值得信賴 AI 代理的特殊考慮事項？

LLM 動態生成 SQL 常見的安全擔憂，特別是 SQL 注入或惡意操作（如刪除或篡改資料庫）。雖然擔憂合理，但可透過妥善設定資料庫存取權限有效防範。對大多數資料庫而言，設定為唯讀是關鍵。針對 PostgreSQL 或 Azure SQL 類型資料庫，應給予應用程式唯讀（SELECT）角色。

將應用程式執行於安全環境可進一步加強保護。在企業場景中，資料通常由營運系統抽取轉換至具有使用者友好 schema 的唯讀資料庫或資料倉儲。此方式確保資料安全、最佳化效能及存取性，且應用程式獲取受限的唯讀存取權。

## 範例程式碼

- Python: [代理框架](./code_samples/04-python-agent-framework.ipynb)
- .NET: [代理框架](./code_samples/04-dotnet-agent-framework.md)

## 對工具使用設計模式有更多疑問嗎？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)，與其他學習者交流，參加開放時間並獲得 AI 代理相關問題解答。

## 額外資源

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI 代理服務工作坊</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso 創意寫作多代理工作坊</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">微軟代理框架概覽</a>


## 測試此代理程式（可選）

在學習如何部署代理程式於[第16課](../16-deploying-scalable-agents/README.md)後，你可以使用[`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json)來測試本課的`TravelToolAgent`（它是否仍然能呼叫工具並作答？）。請參閱[`tests/README.md`](../tests/README.md)了解如何執行測試。

## 上一課

[了解 Agentic 設計模式](../03-agentic-design-patterns/README.md)

## 下一課

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->