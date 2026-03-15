[![如何設計良好的 AI 代理人](../../../translated_images/zh-HK/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(按上方圖片可觀看本課的影片)_

# 工具使用設計模式

工具很有趣，因為它們讓 AI 代理人擁有更廣泛的能力。代理人不再只有有限的一組可執行動作；透過加入工具，代理人現在可以執行各式各樣的操作。在本章中，我們會探討工具使用設計模式，說明 AI 代理人如何使用特定工具來達成目標。

## 介紹

在本課中，我們會嘗試回答以下問題：

- 什麼是工具使用設計模式？
- 它可以應用於哪些使用情境？
- 實作此設計模式需要哪些要素/建構模組？
- 在使用工具使用設計模式來建立可被信任的 AI 代理人時，有哪些特別需注意的事項？

## 學習目標

完成本課後，您將能夠：

- 定義工具使用設計模式及其目的。
- 辨識適用於工具使用設計模式的使用情境。
- 了解實作此設計模式所需的關鍵要素。
- 辨識使用此設計模式構建 AI 代理人時，確保可信度的考量事項。

## 什麼是工具使用設計模式？

**工具使用設計模式** 著重於賦予大型語言模型（LLM）與外部工具互動以達成特定目標的能力。工具是可由代理人執行的程式碼，用來執行動作。工具可以是簡單的函式，例如計算器，或是對第三方服務的 API 呼叫，例如查詢股票價格或天氣預報。在 AI 代理人的脈絡中，工具被設計為在回應 **模型產生的函數呼叫** 時由代理人執行。

## 它可以應用於哪些使用情境？

AI 代理人可以利用工具來完成複雜任務、檢索資訊或協助決策。工具使用設計模式常用於需要與外部系統動態互動的情境，例如資料庫、網路服務或程式碼直譯器。這項能力對於多種使用案例都很有用，包括：

- **動態資訊檢索：** 代理人可以查詢外部 API 或資料庫以取得最新資料（例如，查詢 SQLite 資料庫進行資料分析、取得股價或天氣資訊）。
- **程式碼執行與解譯：** 代理人可以執行程式碼或腳本來解決數學問題、產生報告或執行模擬。
- **工作流程自動化：** 透過整合像是排程器、電子郵件服務或資料管線等工具，自動化重複或多步驟的工作流程。
- **客戶支援：** 代理人可以與 CRM 系統、工單平台或知識庫互動以解決使用者疑問。
- **內容產生與編輯：** 代理人可以利用文法檢查器、摘要器或內容安全評估工具來協助內容創作任務。

## 實作工具使用設計模式需要哪些要素/建構模組？

這些建構模組讓 AI 代理人能執行各式任務。我們來看一下實作工具使用設計模式所需的關鍵要素：

- **函數/工具模式（Function/Tool Schemas）**：可用工具的詳細定義，包括函數名稱、用途、必要參數與預期輸出。這些模式讓 LLM 能理解有哪些工具可用以及如何構造有效的請求。

- **函數執行邏輯（Function Execution Logic）**：決定何時以及如何根據使用者意圖與對話情境來呼叫工具的機制。這可能包含規劃模組、路由機制或條件流程，以動態決定工具的使用。

- **訊息處理系統（Message Handling System）**：管理使用者輸入、LLM 回應、工具呼叫與工具輸出之間對話流程的組件。

- **工具整合框架（Tool Integration Framework）**：將代理人連接到各種工具的基礎設施，無論它們是簡單的函式或複雜的外部服務。

- **錯誤處理與驗證（Error Handling & Validation）**：處理工具執行失敗、驗證參數以及管理非預期回應的機制。

- **狀態管理（State Management）**：追蹤對話上下文、先前的工具互動與持久資料，以確保跨多回合互動的一致性。

接下來，我們將更詳細地探討函數/工具呼叫（Function/Tool Calling）。
 
### 函數/工具呼叫

函數呼叫是讓大型語言模型（LLM）與工具互動的主要方式。您會常看到「Function」和「Tool」互換使用，因為「函數」（可重用的程式區塊）就是代理人用來執行任務的「工具」。為了能夠呼叫函數的程式碼，LLM 必須將使用者的請求與函數的描述進行比對。為此，我們會將包含所有可用函數描述的模式（schema）傳送給 LLM。LLM 然後會選擇最適合該任務的函數並回傳其名稱與參數。所選函數會被呼叫，其回應會傳回給 LLM，LLM 利用這些資訊來回應使用者的請求。

對開發者而言，要為代理人實作函數呼叫，您需要：

1. 支援函數呼叫的 LLM 模型
2. 包含函數描述的模式（schema）
3. 每個描述中函數的程式碼

我們用取得某城市當前時間的範例來說明：

1. **初始化一個支援函數呼叫的 LLM：**

    並非所有模型都支援函數呼叫，因此確認您使用的 LLM 是否支援很重要。     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支援函數呼叫。我們可以先啟動 Azure OpenAI 用戶端。

    ```python
    # 初始化 Azure OpenAI 客戶端
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **建立函數模式（Function Schema）**：

    接下來我們會定義一個 JSON 模式，包含函數名稱、函數用途的描述，以及函數參數的名稱與描述。
    然後我們會將此模式與先前建立的用戶端一起傳給 LLM，並搭配使用者要求查詢 San Francisco 的時間。重要的是要注意，回傳的是一個 **工具呼叫**，**而不是**問題的最終答案。如前所述，LLM 回傳的是它為任務選擇的函數名稱，以及會傳給該函數的參數。

    ```python
    # 供模型閱讀的函數說明
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
  
    # 第一次 API 呼叫：要求模型使用該函數
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

    現在 LLM 已選擇需要執行的函數，我們需要實作並執行執行該任務的程式碼。
    我們可以用 Python 來實作取得當前時間的程式碼。還需要撰寫程式來從 response_message 中擷取名稱與參數，以取得最終結果。

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
  
      # 第二次 API 呼叫：從模型取得最終回應
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

函數呼叫是大多數（如果不是全部）代理人工具使用設計的核心，但從頭實作有時會具有挑戰性。
如我們在 [第2課](../../../02-explore-agentic-frameworks) 中所學，代理式框架（agentic frameworks）為我們提供了預建的建構模組來實作工具使用。
 
## 使用代理式框架的工具使用範例

以下是一些範例，說明您如何使用不同的代理式框架來實作工具使用設計模式：

### Microsoft 代理框架

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> 是一個用於建構 AI 代理人的開源 AI 框架。它透過允許您將工具定義為帶有 `@tool` 裝飾器的 Python 函數來簡化函數呼叫的流程。該框架處理模型與您的程式碼之間來回的通訊。它也透過 `AzureAIProjectAgentProvider` 提供像是檔案搜尋與程式碼解釋器等預建工具的存取。

下圖說明了使用 Microsoft 代理框架時的函數呼叫流程：

![函數呼叫](../../../translated_images/zh-HK/functioncalling-diagram.a84006fc287f6014.webp)

在 Microsoft 代理框架中，工具被定義為帶裝飾器的函數。我們可以將前面看到的 `get_current_time` 函數改寫成一個使用 `@tool` 裝飾器的工具。框架會自動序列化函數及其參數，建立要傳送給 LLM 的 schema。

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

# 建立一個代理程式，並用該工具執行
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI 代理服務

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> 是一個較新的代理式框架，旨在讓開發者能夠安全地建立、部署與擴展高品質且可擴充的 AI 代理人，而無需管理底層的運算與儲存資源。它對企業應用特別有用，因為它是一個具企業級安全性的完全管理服務。

與直接使用 LLM API 開發相比，Azure AI Agent Service 提供了一些優勢，包括：

- 自動工具呼叫 – 不需要自行解析工具呼叫、呼叫工具並處理回應；所有這些現在都在伺服器端完成
- 安全管理的資料 – 您可以依賴 threads 來儲存所需的所有對話資訊，而不需自己管理對話狀態
- 開箱即用的工具 – 可用來與資料來源互動的工具，例如 Bing、Azure AI Search 與 Azure Functions

Azure AI Agent Service 中可用的工具可分為兩類：

1. 知識型工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">以 Bing 搜尋 作為基礎</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">檔案搜尋</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 搜尋</a>

2. 動作型工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函數呼叫</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">程式碼解釋器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">以 OpenAPI 定義的工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service 讓我們能夠將這些工具作為一個 `toolset` 一起使用。它也會利用 `threads` 來追蹤特定對話的訊息歷史記錄。

想像您是 Contoso 公司的業務代理。您想要開發一個可以回答有關銷售資料問題的對話式代理人。

下圖說明了如何使用 Azure AI Agent Service 分析您的銷售資料：

![代理服務運作中](../../../translated_images/zh-HK/agent-service-in-action.34fb465c9a84659e.webp)

要在服務中使用這些工具中的任何一個，我們可以建立一個用戶端並定義一個工具或工具集。實作上我們可以使用以下 Python 程式碼。LLM 將能檢視該工具集並根據使用者的請求決定是使用使用者建立的函數 `fetch_sales_data_using_sqlite_query`，或是使用預建的 Code Interpreter。

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

# 初始化 Code Interpreter 工具並將其加入工具集。
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用設計模式構建可被信任的 AI 代理人時，有哪些特別需注意的事項？

LLM 動態產生的 SQL 常見關切是安全性，特別是 SQL 注入或惡意行為的風險，例如刪除或竄改資料庫。雖然這些擔憂是合理的，但可以透過適當配置資料庫存取權限有效緩解。對大多數資料庫而言，這涉及將資料庫設為唯讀。對像 PostgreSQL 或 Azure SQL 這類資料庫服務，應該為應用程式指派唯讀（SELECT）角色。

在安全的環境中執行應用程式會進一步增強保護。在企業情境中，資料通常會從營運系統抽取並轉換到一個具有使用者友善 schema 的唯讀資料庫或資料倉儲。這種做法可確保資料安全、最佳化效能與可取用性，並讓應用程式擁有限制性的唯讀存取權限。

## 範例程式碼

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## 對工具使用設計模式有更多問題嗎？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者交流、參加辦公時間，並讓您的 AI 代理人問題獲得解答。

## 進階資源

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## 前一課

[了解 Agentic 設計模式](../03-agentic-design-patterns/README.md)

## 下一課
[具能動性的 RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於確保準確性，但自動翻譯可能仍包含錯誤或不準確之處。請以原文（原始語言版本）為準。對於關鍵資訊，建議採用專業人工翻譯。我們不就因使用本翻譯而引致的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->