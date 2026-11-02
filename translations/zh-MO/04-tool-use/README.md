[![如何設計優秀的 AI 代理](../../../translated_images/zh-MO/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(點擊上方圖片觀看本課程影片)_

# 工具使用設計模式

工具很有趣，因為它們使 AI 代理擁有更廣泛的能力。代理不再只有一組有限的動作可執行，透過加入工具，代理現在可以執行多種動作。在本章中，我們將探討工具使用設計模式，說明 AI 代理如何利用特定工具達成目標。

## 簡介

本課我們將嘗試回答以下問題：

- 什麼是工具使用設計模式？
- 它適用於哪些使用情境？
- 實現此設計模式所需的元素/組件是什麼？
- 使用工具使用設計模式建立可信賴的 AI 代理需要注意哪些特別考量？

## 學習目標

完成本課後，您將能夠：

- 定義工具使用設計模式及其目的。
- 辨識適用工具使用設計模式的使用案例。
- 理解實現此設計模式所需的關鍵元素。
- 認識使用此設計模式打造可信賴 AI 代理的考量。

## 什麼是工具使用設計模式？

<strong>工具使用設計模式</strong> 主要聚焦於賦予大型語言模型（LLM）與外部工具互動的能力，以達成特定目標。工具是代理可以執行的程式碼，用於完成各種動作。工具可以是簡單的函式，例如計算器，也可以是第三方服務的 API 調用，如查詢股價或天氣預報。在 AI 代理的語境下，工具設計是由代理依據 <strong>模型生成的函式呼叫</strong> 來執行的。

## 它可以應用於哪些使用情境？

AI 代理可以利用工具完成複雜任務、檢索資訊或做決策。工具使用設計模式常在需要與外部系統動態互動的情境中使用，例如資料庫、網絡服務或程式碼解譯器。此能力適用於多種不同用例，包括：

- **動態資訊檢索:** 代理可查詢外部 API 或資料庫來抓取最新資料（例如，查詢 SQLite 資料庫做資料分析，或獲取股價與天氣資訊）。
- **程式碼執行與解譯:** 代理可執行程式碼或腳本解決數學問題、生產報告或執行模擬。
- **工作流程自動化:** 透過整合任務排程器、郵件服務或資料管線，自動化重複或多階段工作流程。
- **客戶支援:** 代理可與 CRM 系統、票務平台或知識庫互動，以解決用戶查詢。
- **內容生成與編輯:** 代理可使用語法檢查器、文本摘要器或內容安全評估工具協助創作。

## 實現工具使用設計模式所需的元素/組件？

這些組件使 AI 代理能執行各種任務。讓我們來看看實現工具使用設計模式所需的關鍵元素：

- **函式／工具結構（Schema）**：對可用工具的詳細定義，包括函式名稱、用途、必要參數及預期輸出。這些結構使 LLM 瞭解有哪些工具可用，及如何構造有效請求。

- <strong>函式執行邏輯</strong>：依據用戶意圖與對話上下文決定何時與如何調用工具。可能包含計劃模組、路由機制或條件流程，動態決定工具使用。

- <strong>訊息處理系統</strong>：管理用戶輸入、LLM 回應、工具呼叫及工具輸出間對話流程的組件。

- <strong>工具整合框架</strong>：連接代理與多種工具的基礎設施，無論是簡單函式還是複雜外部服務。

- <strong>錯誤處理與驗證</strong>：處理工具執行失敗、驗證參數、應付異常回應的機制。

- <strong>狀態管理</strong>：追蹤對話上下文、過往工具互動與持久資料，以確保多回合交互的一致性。

接下來，我們將更詳細地探討函式／工具呼叫。
 
### 函式／工具呼叫

函式呼叫是啟用大型語言模型（LLM）與工具互動的主要方式。您會常見「函式」與「工具」可互換使用，因為「函式」（可重用程式碼塊）即是代理用以執行任務的「工具」。為了讓函式程式碼被調用，LLM 必須將用戶請求與函式描述做比較。為此，要將包含所有可用函式描述的結構（schema）傳送給 LLM。LLM 接著選擇最合適的函式並回傳其名稱與參數。系統調用所選函式，將其回應返回給 LLM，LLM 利用此資訊回應用戶請求。

開發者要為代理實現函式呼叫，需要：

1. 支援函式呼叫的 LLM 模型
2. 包含函式描述的結構
3. 各函式的程式碼

用取得某城市當前時間的例子來說明：

1. **初始化一個支援函式呼叫的 LLM：**

    並非所有模型都支援函式呼叫，因此重要的是確認您使用的 LLM 具備此功能。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支援函式呼叫。我們可以從對 Azure OpenAI **Response API** 發送請求開始（穩定的 `/openai/v1/` 端點——不需 `api_version`）。 

    ```python
    # 初始化用於 Azure OpenAI 的 OpenAI 客戶端（Responses API，v1 端點）
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **建立函式結構：**

    接著我們定義一個 JSON 結構，其中包含函式名稱、功能說明，以及函式參數的名稱與說明。
    然後將此結構與用戶請求（尋找舊金山時間）一同傳給前述的客戶端。重要的是，<strong>工具呼叫</strong>會被返回，<strong>而非問題的最終答案</strong>。如先前所述，LLM 回傳它為任務選擇的函式名稱及其參數。

    ```python
    # 函數描述供模型閱讀（回應 API 扁平工具格式）
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
  
    # 初始使用者訊息
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # 第一個 API 呼叫：要求模型使用該函數
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API 在 response.output 中以 function_call 項目返回工具呼叫。
    # 將它們附加到對話中，以便模型在下一輪擁有完整的上下文。
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **執行任務所需的函式程式碼：**

    LLM 選擇了要執行的函式後，必須實作並執行該函式程式碼。
    我們以 Python 實現取得當前時間的程式碼。還需撰寫提取 response_message 中函式名稱與參數的程式碼，獲得最終結果。

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

                # 將工具結果作為 function_call_output 項返回
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

函式呼叫是大多數（若非全部）代理工具使用設計的核心，但自行從頭實作有時會具挑戰性。
如我們在[第二課](../../../02-explore-agentic-frameworks)中學到的，代理框架為我們提供了預建組件來實現工具使用。
 
## 使用代理框架的工具使用範例

以下是如何使用不同代理框架實作工具使用設計模式的一些範例：

### Microsoft 代理框架

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft 代理框架</a> 是一個開源 AI 框架，用於構建 AI 代理。它簡化了函式呼叫的過程，允許您使用 `@tool` 裝飾器將 Python 函式定義為工具。此框架處理模型與您的程式碼之間的雙向通訊，並透過 `FoundryChatClient` 提供對預建工具如檔案搜索和程式碼解譯器的存取。

下圖說明了 Microsoft 代理框架中函式呼叫的過程：

![function calling](../../../translated_images/zh-MO/functioncalling-diagram.a84006fc287f6014.webp)

在 Microsoft 代理框架中，工具是以裝飾函式定義。我們可以用 `@tool` 裝飾器將先前看到的 `get_current_time` 函式轉換為工具。框架會自動序列化函式及其參數，建立要送給 LLM 的結構。

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# 創建客戶端
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# 創建一個代理並使用該工具運行
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry 代理服務

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry 代理服務</a> 是較新的代理框架，設計目標是幫助開發者安全地建立、部署並擴展高品質且可延展的 AI 代理，而無需管理底層運算與存儲資源。它對企業應用尤為有用，因為它是具有企業級安全性的全托管服務。

相較於直接使用 LLM API 開發，Microsoft Foundry 代理服務具備一些優勢，包括：

- 自動工具呼叫——不必解析工具呼叫、調用工具並處理回應；這一切現在在伺服器端完成
- 安全管理資料——無需管理自己的對話狀態，可依賴線程存儲所有資訊
- 開箱即用工具——可用於與資料源互動的工具，如 Bing、Azure AI 搜索與 Azure 函式

Microsoft Foundry 代理服務提供的工具可分為兩類：

1. 知識工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing 搜索基礎</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">檔案搜索</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 搜索</a>

2. 行動工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函式呼叫</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">程式碼解譯器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 定義工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure 函式</a>

代理服務讓我們能將這些工具一起組成 `toolset`，並使用 `threads` 追蹤特定對話的訊息歷史。

想像您是 Contoso 公司的業務代理，想開發一個會話代理來回答關於銷售資料的問題。

下圖展示如何使用 Microsoft Foundry 代理服務分析銷售資料：

![Agentic Service In Action](../../../translated_images/zh-MO/agent-service-in-action.34fb465c9a84659e.webp)

要搭配此服務使用任一工具，我們可以建立客戶端並定義工具或工具集。實作時，可使用以下 Python 程式碼。LLM 能夠檢視工具集並判斷要使用用戶自訂函式 `fetch_sales_data_using_sqlite_query` 還是預建的程式碼解譯器，視用戶請求而定。

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

# 使用 fetch_sales_data_using_sqlite_query 函數初始化功能調用代理，並將其添加到工具組
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# 初始化代碼解譯器工具並添加到工具組。
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用設計模式建立可信賴 AI 代理的特別考量？

由 LLM 動態產生的 SQL 常令安全成疑，尤其是 SQL 注入或惡意動作的風險，如刪除或竄改資料庫。雖然此類風險存在，但可透過正確設定資料庫訪問權限有效降低。對大多數資料庫來說，這涉及設定資料庫為唯讀。像 PostgreSQL 或 Azure SQL 這類資料庫服務，應賦予應用程式唯讀（SELECT）角色。

在安全環境中執行應用程式能進一步強化防護。在企業場景中，資料通常會從營運系統中擷取並轉換到結構化且方便使用的唯讀資料庫或資料倉儲。此方法確保資料安全、效能與可用性優化，且應用程式擁有受限的唯讀存取。

## 範例程式碼

- Python: [代理框架](./code_samples/04-python-agent-framework.ipynb)
- .NET: [代理框架](./code_samples/04-dotnet-agent-framework.md)

## 關於工具使用設計模式有更多問題？

加入 [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) 與其他學習者交流，參加辦公時間並獲取 AI 代理相關問題的解答。

## 額外資源

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI 代理服務工作坊</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso 創意寫作多代理工作坊</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft 代理框架概覽</a>


## 對此代理進行煙霧測試（可選）

在學習如何於[第16課](../16-deploying-scalable-agents/README.md)部署代理後，你可以透過[`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json)對本課的`TravelToolAgent`進行煙霧測試（它是否仍會調用工具並回應？）。關於如何運行，請參閱[`tests/README.md`](../tests/README.md)。

## 上一課

[理解代理設計模式](../03-agentic-design-patterns/README.md)

## 下一課

[代理式RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->