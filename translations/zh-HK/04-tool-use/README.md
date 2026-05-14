[![如何設計優秀的 AI 代理](../../../translated_images/zh-HK/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(點擊上方圖片觀看本課程影片)_

# 工具使用設計模式

工具很有趣，因為它們讓 AI 代理擁有更廣泛的能力範圍。代理不再只有有限的行動集，而是通過添加工具，代理現在可以執行各種不同的行動。在本章節中，我們將探討工具使用設計模式，描述 AI 代理如何使用特定工具來達成其目標。

## 簡介

在本課程中，我們希望回答以下問題：

- 什麼是工具使用設計模式？
- 它可以應用於哪些使用案例？
- 實作該設計模式需要哪些元素或建構模組？
- 使用工具使用設計模式打造可信賴 AI 代理時有哪些特別的注意事項？

## 學習目標

完成本課程後，你將能夠：

- 定義工具使用設計模式及其目的。
- 辨識適用工具使用設計模式的使用案例。
- 了解實作此設計模式所需的關鍵元素。
- 認識使用該設計模式確保 AI 代理可信賴性的考量。

## 什麼是工具使用設計模式？

<strong>工具使用設計模式</strong>專注於賦予大型語言模型（LLM）與外部工具進行互動的能力，以達成特定目標。工具是代理可以執行的程式碼，能完成各種動作。工具可以是簡單的函式，例如計算器，或呼叫第三方服務的 API，如股價查詢或天氣預報。在 AI 代理的情境中，工具設計為由代理根據<strong>模型產生的函式呼叫</strong>來執行。

## 它可以應用於哪些使用案例？

AI 代理可利用工具完成複雜任務、擷取資訊或做出決策。工具使用設計模式常用於需要動態與外部系統互動的場景，如資料庫、網路服務或程式碼解譯器。這項能力適用於多種不同使用案例，包括：

- **動態資訊擷取：** 代理可查詢外部 API 或資料庫，以取得最新資料（例如查詢 SQLite 資料庫進行資料分析、取得股價或天氣資訊）。
- **程式碼執行與解釋：** 代理可執行程式碼或腳本來解決數學問題、生成報告或進行模擬。
- **工作流程自動化：** 透過整合任務排程器、電子郵件服務或資料管線，實現重複性或多步驟工作流程的自動化。
- **客戶支援：** 代理能與 CRM 系統、工單平台或知識庫互動，以解決用戶問題。
- **內容生成與編輯：** 代理可利用語法檢查器、文本摘要器或內容安全評估器等工具，輔助內容創作任務。

## 實作工具使用設計模式所需的元素/建構模組是什麼？

這些建構模組讓 AI 代理能執行各種任務。以下是實作工具使用設計模式所需的關鍵元素：

- **函式/工具結構描述（Schema）：** 詳細定義可用工具，包括函式名稱、目的、必要參數和預期輸出。這些結構描述讓 LLM 理解哪些工具可用，以及如何構造有效的請求。

- **函式執行邏輯：** 控制根據使用者意圖和對話上下文何時、如何調用工具。這可能包含規畫模組、路由機制或條件流程，動態決定工具使用。

- **訊息處理系統：** 管理使用者輸入、LLM 回應、工具呼叫及工具輸出間的對話流程。

- **工具整合框架：** 連接代理與各種工具的基礎設施，無論是簡單函式還是複雜外部服務。

- **錯誤處理與驗證：** 處理工具執行失敗、驗證參數及管理意外回應的機制。

- **狀態管理：** 追蹤對話上下文、先前工具互動及持久資料，以確保多輪互動的一致性。

接下來，我們將更詳細探討函式/工具呼叫。

### 函式/工具呼叫

函式呼叫是讓大型語言模型（LLMs）與工具互動的主要方式。你會發現「函式」和「工具」常被交替使用，因為「函式」（可重複使用的程式碼區塊）就是代理用來完成任務的「工具」。要調用函式的程式碼，LLM 必須依照使用者請求，與函式描述進行匹配。為此，會傳送一個包含所有可用函式描述的結構描述（schema）給 LLM。LLM 隨後會選擇最合適的函式，並返回其名稱及參數。該函式被調用後，回應被送回 LLM，LLM 利用該資訊來回應使用者請求。

開發者實作代理的函式呼叫功能，需具備：

1. 支援函式呼叫的 LLM 模型
2. 包含函式描述的結構描述（schema）
3. 每個函式對應的程式碼

讓我們以取得某城市目前時間為例說明：

1. **初始化支援函式呼叫的 LLM：**

    並非所有模型都支援函式呼叫，因此確定所使用的 LLM 有此功能很重要。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支援函式呼叫。我們可以先啟動 Azure OpenAI 用戶端。

    ```python
    # 初始化 Azure OpenAI 用戶端
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **建立函式結構描述（Schema）：**

    接著我們會定義一個 JSON 結構描述，包含函式名稱、函式功能描述，以及函式參數的名稱和描述。
    然後將此結構描述與使用者想取得舊金山時間的請求一併傳給前面創建的用戶端。值得注意的是，返回的是<strong>工具呼叫</strong>，<strong>不是</strong>問題的最終答案。如前所述，LLM 回傳它為任務選擇的函式名稱及會傳給該函式的參數。

    ```python
    # 供模型閱讀的功能描述
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
  
1. **執行工作所需的函式程式碼：**

    LLM 選定需要執行的函式後，必須實作並執行該函式程式碼以完成任務。
    我們可以用 Python 實作取得當前時間的程式碼。還需撰寫從 response_message 中擷取函式名稱及參數的程式碼，以取得最終結果。

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

函式呼叫是大多數（若非全部）代理工具使用設計的核心，但自行從頭實作有時具有挑戰性。
正如我們在[課程 2](../../../02-explore-agentic-frameworks)所學，代理框架提供了預建的建構模組，方便實作工具使用。

## 使用代理框架的工具使用範例

以下示範如何使用不同代理框架來實作工具使用設計模式：

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> 是一個開源 AI 框架，用於創建 AI 代理。它簡化了函式呼叫的流程，允許你使用 `@tool` 裝飾器將工具定義為 Python 函式。框架負責模型與程式碼之間的雙向通信，並提供對預建工具（如檔案搜尋和程式碼解釋器）的存取，藉由 `AzureAIProjectAgentProvider`。

下圖說明了 Microsoft Agent Framework 中函式呼叫的流程：

![function calling](../../../translated_images/zh-HK/functioncalling-diagram.a84006fc287f6014.webp)

在 Microsoft Agent Framework 中，工具以被裝飾的函式定義。我們可以用 `@tool` 裝飾器將先前的 `get_current_time` 函式轉成工具。框架會自動序列化函式及其參數，產生送給 LLM 的結構描述。

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

# 建立一個代理並使用工具運行
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> 是較新的代理框架，旨在使開發者能安全地建立、部署並擴充高品質且可擴展的 AI 代理，而無需管理底層的計算和存儲資源。它特別適合企業應用，因為該服務是全方位管理且具企業級安全性的服務。

相較於直接使用 LLM API 進行開發，Azure AI Agent Service 提供以下優勢：

- 自動化工具呼叫 — 不用自行分析工具呼叫、調用工具並處理回應；這些皆在伺服器端完成。
- 安全管理資料 — 無需自行管理對話狀態，可依靠話題（threads）存儲所有必要資訊。
- 開箱即用的工具 — 提供可與資料來源互動的工具，如 Bing、Azure AI 搜尋和 Azure Functions。

Azure AI Agent Service 提供的工具可分為兩大類：

1. 知識工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing 搜尋基底支援</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">檔案搜尋</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 搜尋</a>

2. 行動工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函式呼叫</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">程式碼解譯器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 定義工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service 允許我們將這些工具作為一個 `toolset` 一起使用，同時利用 `threads` 追蹤特定對話的訊息歷史。

假設你是名為 Contoso 公司的銷售代理，你想開發一個會話代理，回答銷售資料相關問題。

以下圖片示範如何利用 Azure AI Agent Service 分析銷售資料：

![Agentic Service In Action](../../../translated_images/zh-HK/agent-service-in-action.34fb465c9a84659e.webp)

若要使用這些服務中的工具，可以建立用戶端並定義工具或工具集。以下 Python 程式碼示範了實作方式。LLM 將能夠根據使用者請求，選擇使用使用者自創函式 `fetch_sales_data_using_sqlite_query` 或內建的程式碼解譯器。

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

# 初始化工具集合
toolset = ToolSet()

# 使用 fetch_sales_data_using_sqlite_query 函數初始化函數調用代理，並將其添加到工具集合中
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# 初始化代碼解譯器工具並將其添加到工具集合中。
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用設計模式建立可信賴 AI 代理的特別考量是什麼？

一般來說，LLM 動態生成 SQL 最常見的疑慮是安全性，尤其是 SQL 注入風險或惡意操作（如刪除或竄改資料庫）。這些疑慮雖然合理，但可以透過適當設定資料庫存取權限有效減輕。對大多數資料庫來說，就是將資料庫設定為唯讀。對 PostgreSQL 或 Azure SQL 等資料庫服務，應給應用程式唯讀（SELECT）角色。

在安全環境中執行應用程式會進一步提升保護。在企業情境，資料通常會從作業系統擷取並轉換成具有易用結構的唯讀資料庫或資料倉儲。此做法確保資料安全，優化效能與可存取性，並且限制應用程式只能唯讀存取。

## 範例程式碼

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## 想了解更多關於工具使用設計模式的問題？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，與其他學習者交流，參加辦公時間並解決你的 AI 代理問題。

## 其他資源

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service 工作坊</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso 創意作者多代理工作坊</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework 簡介</a>

## 上一課

[理解代理設計模式](../03-agentic-design-patterns/README.md)

## 下一課
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->