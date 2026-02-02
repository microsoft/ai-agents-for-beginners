[![如何設計優秀的 AI 代理](../../../translated_images/zh-MO/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(點擊上方圖片觀看本課程影片)_

# 工具使用設計模式

工具很有趣，因為它們允許 AI 代理擁有更廣泛的能力範圍。代理不再只限於執行有限的動作，透過加入工具，代理現在能執行各種動作。在本章中，我們將探討工具使用設計模式，它描述了 AI 代理如何使用特定工具來達成目標。

## 介紹

在本課程中，我們將回答以下問題：

- 什麼是工具使用設計模式？
- 它能應用於哪些使用案例？
- 實現此設計模式需要哪些元素/構建區塊？
- 使用工具使用設計模式建造可信賴 AI 代理有哪些特別考量？

## 學習目標

完成本課程後，您將能夠：

- 定義工具使用設計模式及其目的。
- 識別適用於工具使用設計模式的使用案例。
- 了解實現該設計模式所需的關鍵元素。
- 辨識使用此設計模式建構可信賴 AI 代理的考量。

## 什麼是工具使用設計模式？

**工具使用設計模式**專注於賦予大型語言模型（LLM）與外部工具互動的能力，以達到特定目標。工具是代理執行動作可以使用的代碼。工具可以是簡單的函數，例如計算機，或呼叫第三方服務的 API，例如股價查詢或天氣預報。在 AI 代理的語境中，工具是設計來由代理根據**模型產生的函數呼叫**執行的。

## 它能應用於哪些使用案例？

AI 代理可以利用工具完成複雜任務、檢索資訊或做決策。工具使用設計模式常用於需要動態與外部系統互動的情境，例如資料庫、網路服務或程式碼解譯器。這種能力適用於多種使用案例，包括：

- **動態資訊檢索：**代理可以查詢外部 API 或資料庫以獲取最新數據（例如查詢 SQLite 資料庫做資料分析、抓取股價或天氣資訊）。
- **程式碼執行與解譯：**代理能執行程式碼或腳本來解數學問題、產生報告或進行模擬。
- **工作流程自動化：**透過整合排程任務、電子郵件服務或資料管線來自動化重複或多步驟工作。
- **客服支援：**代理能與 CRM 系統、票務平台或知識庫互動，解決使用者問題。
- **內容生成與編輯：**代理可以利用語法檢查器、文字摘要器或內容安全評估工具來輔助內容創作。

## 實現工具使用設計模式需要哪些元素/構建區塊？

這些構建區塊允許 AI 代理執行各種任務。以下是實現工具使用設計模式所需的關鍵元素：

- **函數/工具架構（Schemas）**：對可用工具的詳細定義，包括函數名稱、用途、必要參數及預期輸出。這些架構讓 LLM 理解有哪些工具可用，以及如何構造有效請求。

- **函數執行邏輯**：控制何時以及如何根據使用者意圖與對話上下文調用工具。這可能包含規劃模組、路由機制或動態決定工具使用的條件流程。

- **訊息處理系統**：管理使用者輸入、LLM 回應、工具呼叫及工具輸出之間的對話流程。

- **工具整合架構**：連接代理與各類工具的基礎設施，無論是簡單函數或複雜外部服務。

- **錯誤處理與驗證**：處理工具執行失敗、參數驗證及意外回應的機制。

- **狀態管理**：追蹤對話上下文、先前工具互動及持久化資料，確保多回合互動的一致性。

接下來，我們將更詳細探討函數／工具呼叫。

### 函數／工具呼叫

函數呼叫是我們讓大型語言模型（LLM）與工具互動的主要方式。您常會看到“函數”和“工具”可以互換使用，因為“函數”（可重用的代碼區塊）就是代理用來執行任務的“工具”。為了讓函數的代碼被呼叫，LLM 必須將使用者請求與函數描述進行比較。為此，我們會將包含所有可用函數描述的架構傳送給 LLM。LLM 接著選擇最適合任務的函數，返回它的名稱和參數。接著呼叫選擇的函數，該函數的回應傳回給 LLM，LLM 再用這些資訊回應使用者請求。

開發者想為代理實作函數呼叫，您需要：

1. 支援函數呼叫的 LLM 模型
2. 包含函數描述的架構
3. 描述中每個函數的程式碼

以取得城市當前時間的例子說明：

1. **初始化支援函數呼叫的 LLM：**

    不是所有模型都支援函數呼叫，確認您使用的 LLM 支援此功能非常重要。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支援函數呼叫。我們可以從初始化 Azure OpenAI 客戶端開始。

    ```python
    # 初始化 Azure OpenAI 客戶端
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

2. **建立函數架構（Function Schema）：**

    接著我們會定義一個 JSON 架構，其中包含函數名稱、該函數功能描述，以及函數參數名稱和描述。
    然後將此架構和使用者尋找舊金山時間的請求傳給先前建立的客戶端。值得注意的是，返回的是一個**工具呼叫**，而不是問題的最終答案。正如先前所述，LLM 回傳它為任務選擇的函數名稱和傳給該函數的參數。

    ```python
    # 模型可讀的功能說明
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
   
    ```python
  
    # 初始用戶訊息
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # 第一次 API 調用：請模型使用該功能
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # 處理模型的回應
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
3. **執行該任務所需的函數程式碼：**

    既然 LLM 已選擇要運行的函數，我們需要編寫並執行該任務的程式碼。
    我們可以用Python實現取得當前時間的程式碼。同時還要撰寫程式碼從 response_message 抽取名稱和參數，來得到最終結果。

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
     # 處理函式調用
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # 第二次 API 調用：從模型獲取最終回應
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

函數呼叫是大多數（若非全部）代理工具使用設計的核心方法，但從零開始實作有時會具挑戰性。
如我們在[第二課](../../../02-explore-agentic-frameworks)學到的，代理框架提供我們預建的構建區塊來實作工具使用。

## 使用代理框架的工具使用範例

以下是您如何使用不同代理框架實作工具使用設計模式的範例：

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> 是一個開源的 AI 框架，供 .NET、Python 和 Java 開發者使用大型語言模型 (LLM)。它透過<a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">序列化</a>過程，自動將您的函數及其參數描述傳給模型，簡化函數呼叫的流程。它同時處理模型與您的程式碼之間的雙向通訊。使用像 Semantic Kernel 這樣的代理框架的另一個優點是，您可以存取預建工具，如<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">檔案搜尋</a>及<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">程式碼解譯器</a>。

下圖說明了 Semantic Kernel 中函數呼叫的流程：

![function calling](../../../translated_images/zh-MO/functioncalling-diagram.a84006fc287f6014.webp)

在 Semantic Kernel 中，函數/工具稱為<a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">插件 (Plugins)</a>。我們可以把剛才看到的 `get_current_time` 函數轉成插件方法，將其封裝至類別中。也可以匯入 `kernel_function` 裝飾器，並傳入該函數的描述。之後當用 GetCurrentTimePlugin 創建 kernel 時，kernel 會自動序列化該函數及其參數，創建傳給 LLM 的架構。

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# 建立核心
kernel = Kernel()

# 建立插件
get_current_time_plugin = GetCurrentTimePlugin(location)

# 將插件加入核心
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> 是一個較新的代理框架，旨在幫助開發者安全地構建、部署及擴展高品質且可擴充的 AI 代理，同時無需管理底層的運算與儲存資源。它特別適用於企業應用，因為它是全託管服務並具備企業級安全性。

與直接使用 LLM API 開發相比，Azure AI Agent Service 有以下優勢：

- 自動工具呼叫 — 不需自行解析工具呼叫、執行工具及處理回應，這些都由伺服器端完成
- 安全管理資料 — 不需自行管理對話狀態，可依賴 threads 儲存所有必要資訊
- 即用型工具 — 可用於與資料源互動的工具，如 Bing、Azure AI Search 和 Azure Functions。

Azure AI Agent Service 中可用的工具分為兩類：

1. 知識工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">藉由 Bing 搜尋輔助依據 (Grounding)</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">檔案搜尋</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. 行動工具 (Action Tools)：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函數呼叫</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">程式碼解譯器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 定義工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service 允許我們將這些工具作為 `toolset` 一起使用。它同時利用 `threads` 追蹤特定對話的訊息歷史。

想像您是一家名為 Contoso 的公司的銷售代理，您想開發能回答銷售數據問題的對話代理。

下圖說明如何利用 Azure AI Agent Service 分析您的銷售數據：

![Agentic Service In Action](../../../translated_images/zh-MO/agent-service-in-action.34fb465c9a84659e.webp)

要與此服務一起使用任何工具，我們可以創建客戶端並定義單一工具或工具集合。實作上，我們可以使用以下 Python 程式碼。LLM 會查看工具集合，依據使用者請求選擇使用使用者自行定義的函數 `fetch_sales_data_using_sqlite_query`，或是內建的程式碼解譯器。

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query 函數，可喺 fetch_sales_data_functions.py 檔案搵到。
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# 初始化工具組
toolset = ToolSet()

# 用 fetch_sales_data_using_sqlite_query 函數初始化功能呼叫代理，並加入工具組
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# 初始化程式碼解譯器工具並加入工具組。
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用設計模式建造可信賴 AI 代理的特別考量為何？

一個常見的 SQL 安全疑慮是由 LLM 動態產生的 SQL 語句，主要包括 SQL 注入攻擊或惡意行為（如刪除或篡改資料庫）的風險。這些疑慮雖然合理，但可透過正確設定資料庫存取權限有效降低。針對大多數資料庫而言，這通常涉及將資料庫設成唯讀。像 PostgreSQL 或 Azure SQL 這類資料庫服務，應為應用程式分配唯讀（SELECT）角色。
喺一個安全環境運行應用程式進一步加強保護。喺企業場景中，數據通常會從操作系統提取並轉換到具備用戶友好架構的唯讀數據庫或數據倉庫。呢個方法確保數據安全，優化性能同易於存取，而且應用程式擁有限制性嘅唯讀訪問權限。

## 範例代碼

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## 想了解更多關於工具使用設計模式嘅問題？

加入 [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)，同其他學習者交流，參加辦公時間，並獲得你嘅 AI Agents 問題解答。

## 額外資源

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents 服務工作坊</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer 多代理工作坊</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel 函數調用教程</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel 代碼解釋器</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen 工具</a>

## 上一課

[理解 Agentic 設計模式](../03-agentic-design-patterns/README.md)

## 下一課

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件乃使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯而成。雖然我們力求準確，但請注意，自動翻譯可能含有錯誤或不準確之處。原始文件之母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們對因使用此翻譯而引致之任何誤解或誤譯不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->