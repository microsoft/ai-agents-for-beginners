[![如何設計良好的 AI 代理](../../../translated_images/zh-HK/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(點擊上方圖片觀看本課程影片)_

# 工具使用設計模式

工具很有趣，因為它們允許 AI 代理擁有更廣泛的能力。代理不再僅有有限的行動集合，而是透過添加工具，代理現在可以執行各種操作。在本章中，我們將探討工具使用設計模式，描述 AI 代理如何使用特定工具達成目標。

## 簡介

在本課程中，我們致力於解答以下問題：

- 什麼是工具使用設計模式？
- 它可以應用於哪些使用案例？
- 實現此設計模式需要哪些元素／建構方塊？
- 使用工具使用設計模式建立可信任 AI 代理時有哪些特殊考量？

## 學習目標

完成本課程後，您將能夠：

- 定義工具使用設計模式及其目的。
- 辨識適用工具使用設計模式的使用案例。
- 理解實現該設計模式所需的關鍵元素。
- 認識使用此設計模式確保 AI 代理可信性的考量。

## 什麼是工具使用設計模式？

**工具使用設計模式**專注於賦予大型語言模型（LLM）與外部工具互動以達成特定目標的能力。工具是代理可執行的程式碼以完成動作。工具可以是簡單的函數，例如計算機，或是第三方服務的 API 呼叫，例如股價查詢或天氣預報。在 AI 代理的語境中，工具設計為代理在回應**模型生成的函數呼叫**時執行。

## 它可以應用於哪些使用案例？

AI 代理可以利用工具完成複雜任務、檢索資訊或做出決策。工具使用設計模式常用於需要動態與外部系統互動的場景，如資料庫、網路服務或程式碼解譯器。此能力適用於多種使用案例，包括：

- **動態資訊檢索：**代理可查詢外部 API 或資料庫以擷取即時資料（例如查詢 SQLite 資料庫做資料分析，取得股價或天氣資訊）。
- **程式碼執行與解析：**代理可以執行程式碼或腳本，解決數學問題、產生報告或進行模擬。
- **工作流程自動化：**透過整合任務排程器、電子郵件服務或資料管線，自動化重複或多步驟流程。
- **客戶支援：**代理可與 CRM 系統、客服平台或知識庫互動，以回應用戶問題。
- **內容生成與編輯：**代理可使用語法檢查、文字摘要或內容安全評估等工具協助內容創作。

## 實現工具使用設計模式需要哪些元素／建構方塊？

這些建構方塊允許 AI 代理執行多元任務。以下是實現工具使用設計模式所需的關鍵元素：

- **函數／工具結構（Schema）**：詳細定義可用工具，包括函數名稱、用途、所需參數及預期輸出。這些結構協助 LLM 理解可用的工具及如何構造有效請求。

- **函數執行邏輯**：管理如何及何時根據使用者意圖及會話上下文調用工具。可能包括規劃模組、路由機制或條件流程，動態決定工具使用。

- **訊息處理系統**：管理使用者輸入、LLM 回應、工具呼叫及工具輸出之間的對話流程。

- **工具整合框架**：連接代理與多種工具的基礎設施，無論是簡單函數還是複雜外部服務。

- **錯誤處理與驗證**：處理工具執行失敗、驗證參數與管理非預期回應的機制。

- **狀態管理**：追蹤會話上下文、先前工具互動及持久資料，確保多輪互動中一致性。

接下來，我們將更詳細探討函數／工具呼叫。

### 函數／工具呼叫

函數呼叫是使大型語言模型（LLM）與工具互動的主要方式。您會常看到「函數」與「工具」互換使用，因為「函數」（可重用的程式碼區塊）即為代理執行任務用的「工具」。為了呼叫函數的程式碼，LLM 必須將用戶請求與函數描述比對。為此，所有可用函數的描述會以結構架構（schema）形式傳遞給 LLM。LLM 再從中選出最適合任務的函數，並回傳函數名稱及參數。選定函數被呼叫後，其回應會送回 LLM，LLM 利用該資訊回應用戶請求。

開發者若要實作代理的函數呼叫，需要：

1. 支援函數呼叫的 LLM 模型
2. 含函數描述的結構架構
3. 每個函數所需實作的程式碼

以下以取得城市當前時間為例說明：

1. **初始化支援函數呼叫的 LLM：**

    不是所有模型都支援函數呼叫，因此需確認所使用的 LLM 是否支援。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支援函數呼叫。我們可先啟用 Azure OpenAI 用戶端。 

    ```python
    # 初始化 Azure OpenAI 客戶端
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **建立函數結構架構：**

    接著定義一個 JSON 結構，包含函數名稱、函數功能描述，以及參數名稱與描述。然後將此結構與用戶要求（查詢舊金山時間）傳給先前建立的用戶端。重要的是要注意，回傳的是**工具呼叫**，而非問題的最終答案。正如前述，LLM 回傳選中執行任務的函數名與傳入參數。

    ```python
    # 模型閱讀的功能描述
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
  
    # 第一次 API 調用：請模型使用函數
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
  
1. **執行任務所需的函數程式碼：**

    LLM 選定要執行的函數後，需要實作並執行該函數程式碼。我們可以用 Python 實作取得當前時間的代碼，並撰寫程式碼從 response_message 取出函數名稱及參數，得到最終結果。

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

函數呼叫是大多數（若非全部）代理工具使用設計的核心，但從零實作有時會具挑戰性。
如 [第二課](../../../02-explore-agentic-frameworks) 所示，代理框架為我們提供了建構工具使用的預建建構方塊。

## 使用代理框架的工具使用範例

以下示範如何使用不同代理框架實作工具使用設計模式：

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> 是為 .NET、Python 和 Java 開發者打造的開源 AI 框架，專門使用大型語言模型（LLM）。它透過稱為<a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">序列化</a>的過程，自動將您的函數及其參數描述傳給模型，簡化了函數呼叫流程。它也處理模型與程式碼之間的來回通訊。使用如 Semantic Kernel 等代理框架的另一優點是，可存取預建工具，如<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">檔案搜尋</a>與<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">程式碼解譯器</a>。

下圖說明 Semantic Kernel 函數呼叫的流程：

![function calling](../../../translated_images/zh-HK/functioncalling-diagram.a84006fc287f6014.webp)

在 Semantic Kernel 中，函數／工具稱為<a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">外掛程式（Plugins）</a>。我們可以將先前的 `get_current_time` 函數改為外掛，將其包裝成含該函數的類別，並匯入 `kernel_function` 裝飾器，裝飾器接收函數描述。建立帶有 GetCurrentTimePlugin 的 kernel 時，kernel 會自動序列化函數及其參數，過程中產生發送給 LLM 的結構架構。

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

# 將插件加入到核心
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> 是較新的代理框架，旨在幫助開發者安全地構建、部署和擴充高品質且可擴展的 AI 代理，無需管理底層計算與儲存資源。它對企業應用尤其有用，因為它是具企業級安全性的全託管服務。

與直接使用 LLM API 開發相比，Azure AI Agent Service 具備以下優勢：

- 自動工具呼叫 — 無需手動解析工具呼叫、執行工具與處理回應，所有流程皆在服務端完成
- 安全管理資料 — 不必自行管理會話狀態，可依賴「線程（threads）」存儲所有所需資訊
- 現成工具 — 可用於與資料來源互動的工具，如 Bing、Azure AI Search 和 Azure Functions

Azure AI Agent Service 中可用的工具分為兩類：

1. 知識工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">利用 Bing 搜索做 Grounding</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">檔案搜尋</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. 行動工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函數呼叫</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">程式碼解譯器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 定義工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

代理服務允許我們將這些工具合為 `toolset` 使用，也利用 `threads` 追蹤特定對話的訊息歷史。

想像您是 Contoso 公司的銷售員工，想開發可以回答銷售數據問題的對話代理。

下圖展示如何使用 Azure AI Agent Service 來分析銷售數據：

![Agentic Service In Action](../../../translated_images/zh-HK/agent-service-in-action.34fb465c9a84659e.webp)

要在服務中使用這些工具，我們可以創建用戶端並定義工具或工具組。下列 Python 程式碼演示實作。LLM 會檢視工具組並根據使用者請求決定使用使用者自行建立的函數 `fetch_sales_data_using_sqlite_query` 還是預建的程式碼解譯器。

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query 函數，可以在 fetch_sales_data_functions.py 文件中找到。
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# 初始化工具組
toolset = ToolSet()

# 使用 fetch_sales_data_using_sqlite_query 函數初始化函數調用代理，並將其添加到工具組中
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# 初始化程式碼解釋器工具並將其添加到工具組中。
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用設計模式打造可信任 AI 代理的特殊考量？

LLM 動態生成 SQL 時常見的疑慮是安全性，特別是 SQL 注入或惡意操作（如刪除或竄改資料庫）的風險。這些擔憂雖然合理，但能透過妥善配置資料庫存取權限有效緩解。大部分資料庫可設定為唯讀模式。對於 PostgreSQL 或 Azure SQL 等資料庫服務，應給應用程式指派唯讀（SELECT）角色。
在安全環境中運行應用程式進一步增強保護。在企業場景中，資料通常會從營運系統中提取並轉換到具有用戶友好結構的唯讀資料庫或資料倉儲。此方法確保資料安全、優化效能與可存取性，且應用程式擁有限制的唯讀存取權限。

## 範例代碼

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## 有更多關於工具使用設計模式的問題嗎？

加入 [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者交流，參加辦公時間，並獲取 AI Agents 的問題解答。

## 其他資源

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents 服務工作坊</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer 多代理工作坊</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel 函數呼叫教學</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel 程式碼解譯器</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen 工具</a>

## 上一課

[理解 Agentic 設計模式](../03-agentic-design-patterns/README.md)

## 下一課

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力追求準確性，請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。本公司不對因使用本翻譯版本而引致的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->