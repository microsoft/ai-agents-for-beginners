[![如何設計良好的 AI 代理](../../../translated_images/zh-TW/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(點擊上方圖片觀看本課程影片)_

# 工具使用設計模式

工具很有趣，因為它們允許 AI 代理擁有更廣泛的能力範圍。代理不再只有有限的行動集，而是通過新增工具，代理現在能執行多種動作。在本章中，我們將探討工具使用設計模式，描述 AI 代理如何使用特定工具來達成目標。

## 介紹

在本課程中，我們希望解答以下問題：

- 什麼是工具使用設計模式？
- 這個設計模式適用於哪些使用案例？
- 實作這個設計模式需要哪些元素／建構模組？
- 使用工具使用設計模式建立值得信賴的 AI 代理，有哪些特別考量？

## 學習目標

完成本課程後，您將能夠：

- 定義工具使用設計模式及其目的。
- 識別適用工具使用設計模式的使用案例。
- 了解實作該設計模式所需的關鍵元素。
- 辨識使用此設計模式確保 AI 代理可信性的考量。

## 什麼是工具使用設計模式？

<strong>工具使用設計模式</strong> 著眼於賦予大型語言模型（LLM）與外部工具互動的能力，以達成特定目標。工具指的是代理可執行的程式碼以完成動作。工具可以是像計算機這樣的簡單函數，也可以是查詢第三方服務（例如股價查詢或天氣預報）的 API 呼叫。在 AI 代理上下文中，工具設計為由代理回應 **模型產生的函數呼叫（function calls）** 來執行。

## 它可應用於哪些使用案例？

AI 代理能利用工具完成複雜任務、檢索資訊或作出決策。工具使用設計模式常用於需要動態與外部系統互動的場景，例如資料庫、網路服務或程式碼解譯器。這種能力適用於多種不同使用案例，包括：

- **動態資訊擷取：** 代理能查詢外部 API 或資料庫以取得最新資料（例如查詢 SQLite 資料庫進行資料分析、取得股價或天氣資訊）。
- **程式執行及解譯：** 代理能執行程式碼或腳本以解決數學問題、生成報告或執行模擬。
- **工作流程自動化：** 透過整合工作排程器、郵件服務或資料管線，自動化重複或多步驟工作流程。
- **客戶支援：** 代理能與 CRM 系統、票務平台或知識庫互動，以解決用戶查詢。
- **內容生成與編輯：** 代理能利用文法檢查器、文本摘要器或內容安全評估工具來協助內容創建工作。

## 實作工具使用設計模式需要哪些元素／建構模組？

這些建構模組使 AI 代理能執行廣泛的任務。讓我們來看實作工具使用設計模式所需的關鍵元素：

- **函數／工具結構（Function/Tool Schemas）**：詳細定義可用工具，包括函數名稱、用途、所需參數及預期輸出。這些結構讓 LLM 瞭解有哪些工具可用及如何構造有效請求。

- **函數執行邏輯（Function Execution Logic）**：決定何時及如何根據用戶意圖及對話上下文調用工具。可能包含計劃模組、路由機制或條件流程，用以動態決定工具使用。

- **訊息處理系統（Message Handling System）**：管理用戶輸入、LLM 回應、工具呼叫與工具輸出之間對話流的元件。

- **工具整合框架（Tool Integration Framework）**：將代理連接到各種工具的基礎架構，無論是簡單函數還是複雜外部服務。

- **錯誤處理與驗證（Error Handling & Validation）**：處理工具執行失敗、驗證參數，並管理非預期回應的機制。

- **狀態管理（State Management）**：追蹤對話上下文、先前工具交互以及持久化資料，確保多回合互動的一致性。

接著，我們詳細探討函數／工具呼叫。

### 函數／工具呼叫

函數呼叫是啟用大型語言模型（LLM）與工具互動的主要方式。通常「函數（Function）」與「工具（Tool）」可互換使用，因為「函數」（可重用的程式碼區塊）是代理用以執行任務的「工具」。為使函數程式碼能被呼叫，LLM 必須將用戶請求與函數描述進行比對。為此，會傳送一份包含所有可用函數描述的架構（schema）給 LLM。LLM 從中選擇最合適的函數，並回傳函數名稱及參數。該函數被呼叫後，其回應回傳至 LLM，LLM 利用這些資訊回應用戶的請求。

開發者實作代理函數呼叫須具備：

1. 支援函數呼叫的 LLM 模型
2. 包含函數描述的架構（schema）
3. 每個函數對應的程式碼

用「取得某城市現在時間」的範例來說明：

1. **初始化支援函數呼叫的 LLM：**

    並非所有模型都支援函數呼叫，因此要確認使用的 LLM 是否具備該功能。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支援函數呼叫。我們可先啟動 Azure OpenAI 客戶端。

    ```python
    # 初始化 Azure OpenAI 用戶端
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **建立函數結構：**

    接著定義一份 JSON 架構，包含函數名稱、說明函數功能，以及函數參數名稱與描述。
    再將此架構與用戶查詢（例如找到舊金山時間的請求）傳給先前建立的客戶端。重要的是，**傳回的是工具呼叫，而非問題的最終答案**。如前所述，LLM 會回傳為完成任務所選函數的名稱與會傳入的參數。

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
  
    # 初始使用者訊息
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # 第一次 API 調用：請模型使用該函數
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

    當 LLM 已選定要執行的函數，接著需要實作並執行相關程式碼。
    我們可以用 Python 編寫取得當前時間的程式碼。同時寫程式碼從 response_message 中解析函數名稱與參數，以獲得最終結果。

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
     # 處理函式呼叫
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
  
      # 第二次 API 呼叫：從模型獲取最終回應
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

函數呼叫幾乎是所有代理工具使用設計的核心，但自行實作有時可能較具挑戰性。
如我們在[課程 2](../../../02-explore-agentic-frameworks)所學，代理框架提供現成建構模組以實作工具使用。

## 使用代理框架的工具使用範例

以下展示如何利用不同代理框架實作工具使用設計模式：

### Microsoft 代理框架

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft 代理框架</a> 是建構 AI 代理的開源框架。它簡化函數呼叫的流程，允許您用 `@tool` 裝飾器定義 Python 函數為工具。此框架處理模型與代碼間的雙向通訊，也可透過 `AzureAIProjectAgentProvider` 提供如檔案搜尋、程式碼解譯器等預建工具。

下圖說明 Microsoft 代理框架中函數呼叫的流程：

![function calling](../../../translated_images/zh-TW/functioncalling-diagram.a84006fc287f6014.webp)

在 Microsoft 代理框架中，工具定義為裝飾函數。我們可將先前的 `get_current_time` 函數用 `@tool` 裝飾器轉成工具。框架會自動序列化函數及其參數，建立送至 LLM 的架構。

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# 建立客戶端
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# 建立代理並與工具一起運行
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI 代理服務

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI 代理服務</a> 是一個較新的代理框架，致力於協助開發者安全構建、部署與擴展高品質且可擴充的 AI 代理，無需自行管理底層計算與儲存資源。此服務特別適用企業應用，因為是全託管服務並具企業級安全性。

與直接使用 LLM API 相比，Azure AI 代理服務提供部分優勢，包括：

- 自動工具呼叫 — 不必解析工具呼叫、執行工具並處理回應；所有這些均由伺服器端完成
- 安全管理數據 — 不必自行管理對話狀態，可依賴線程（threads）存儲所有必要資訊
- 開箱即用的工具 — 可用於與資料來源互動的工具，如 Bing、Azure AI 搜尋及 Azure Functions

Azure AI 代理服務中的工具可分為兩類：

1. 知識工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing 搜尋基礎</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">檔案搜尋</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 搜尋</a>

2. 動作工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函數呼叫</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">程式碼解譯器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 定義工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

代理服務讓我們能將這些工具組合成 `toolset`，並利用 `threads` 追蹤特定對話的訊息歷史。

假設您是 Contoso 公司的銷售代理，希望開發一個會話代理來回答關於銷售資料的問題。

下圖示範如何使用 Azure AI 代理服務來分析銷售資料：

![Agentic Service In Action](../../../translated_images/zh-TW/agent-service-in-action.34fb465c9a84659e.webp)

要在服務中使用這些工具，可建立客戶端並定義工具或工具組。以下 Python 範例展示實作細節。LLM 能查看工具組並根據用戶請求決定使用自訂函數 `fetch_sales_data_using_sqlite_query` 或預建的程式碼解譯器。

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query 函數位於 fetch_sales_data_functions.py 檔案中。
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# 初始化工具集
toolset = ToolSet()

# 使用 fetch_sales_data_using_sqlite_query 函數初始化函數調用代理並將其加入工具集中
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# 初始化程式碼解釋器工具並將其加入工具集中。
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用設計模式建立值得信賴的 AI 代理有哪些特別考量？

LLM 動態產生的 SQL 一般會引起安全疑慮，尤其是 SQL 注入攻擊或惡意操作資料庫（例如刪除或破壞資料庫）的風險。儘管此類疑慮合理，但只要妥善設定資料庫存取權限，即可有效降低風險。多數資料庫可透過設成唯讀來實現。對於 PostgreSQL 或 Azure SQL 等資料庫服務，應為應用程式分配唯讀（SELECT）角色。

將應用程式執行於安全環境更能提升保護。在企業場景中，資料通常從營運系統中抽取並轉換成唯讀資料庫或資料倉儲，且結構簡潔易用。此法確保資料安全、優化性能與可存取性，且應用程式擁有限制性的唯讀存取權限。

## 範例程式碼

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## 對工具使用設計模式還有疑問嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，與其他學習者交流，參加辦公時間並獲得 AI 代理問題解答。

## 其他資源

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI 代理服務工作坊</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso 創意寫作者多代理工作坊</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft 代理框架概覽</a>

## 前一課程

[理解 Agentic 設計模式](../03-agentic-design-patterns/README.md)

## 下一課程
[自主式 RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->