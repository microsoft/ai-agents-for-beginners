[![如何設計優良的 AI 代理](../../../translated_images/zh-TW/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(點擊上方圖片觀看本課程影片)_

# 工具使用設計模式

工具很有趣，因為它們允許 AI 代理擁有更廣泛的能力範圍。代理不再僅限於執行有限的一組動作，而是通過添加工具，代理現在可以執行多種不同的動作。本章中，我們將探討工具使用設計模式，描述 AI 代理如何使用特定工具達成其目標。

## 簡介

在本課程中，我們將嘗試回答以下問題：

- 什麼是工具使用設計模式？
- 它可以應用於哪些使用情境？
- 實作該設計模式所需的元素／組件是什麼？
- 使用工具使用設計模式建立值得信賴的 AI 代理有哪些特殊考量？

## 學習目標

完成本課程後，您將能夠：

- 定義工具使用設計模式及其目的。
- 識別適合應用工具使用設計模式的使用情境。
- 了解實作該設計模式所需的關鍵元素。
- 認識如何使用此設計模式確保 AI 代理的可信度。

## 什麼是工具使用設計模式？

**工具使用設計模式** 著重於賦予大型語言模型（LLM）與外部工具互動的能力，以達成特定目標。工具是代理可以執行以完成動作的程式碼。工具可以是簡單的函數，例如計算器，或第三方服務的 API 呼叫，例如股票價格查詢或天氣預報。在 AI 代理的語境中，工具是為了響應**模型生成的函數調用**而設計執行的。

## 它可以應用於哪些使用情境？

AI 代理可以利用工具完成複雜任務、檢索資訊或做出決策。工具使用設計模式常用於需要與外部系統（如資料庫、網路服務或程式碼解譯器）進行動態互動的場景。這種能力對多種使用情境非常有用，包括：

- **動態資訊檢索：** 代理可以查詢外部 API 或資料庫以獲取最新數據（例如查詢 SQLite 資料庫做資料分析，撈取股票行情或天氣資訊）。
- **程式碼執行與解譯：** 代理可執行代碼或腳本來解數學問題、產生報告或執行模擬。
- **工作流程自動化：** 藉由整合任務排程、電子郵件服務或資料管線等工具，實現重複性或多步驟工作流程的自動化。
- **客戶支援：** 代理可與 CRM 系統、工單平臺或知識庫互動，解決用戶詢問。
- **內容生成與編輯：** 代理可利用文法檢查器、文字摘要工具或內容安全評估工具，輔助內容創建任務。

## 實作工具使用設計模式所需的元素／組件是什麼？

這些組件使 AI 代理能執行多元任務。以下是實作工具使用設計模式所需的關鍵元素：

- **函數／工具結構定義（Function/Tool Schemas）**：可用工具的詳細定義，包括函數名稱、用途、必要參數與預期回傳。這些結構定義幫助 LLM 了解可用工具以及如何建立有效的請求。

- **函數執行邏輯（Function Execution Logic）**：根據使用者意圖與對話上下文決定何時以及如何呼叫工具。可能包含規劃模組、路由機制或條件流程，動態決策使用工具。

- **訊息處理系統（Message Handling System）**：管理使用者輸入、LLM 回應、工具呼叫與工具輸出之間對話流程的組件。

- **工具整合框架（Tool Integration Framework）**：連接代理與各種工具的架構，無論是簡單函數還是複雜外部服務。

- **錯誤處理與驗證（Error Handling & Validation）**：處理工具執行失敗、驗證參數、管理異常回應的機制。

- **狀態管理（State Management）**：追蹤對話上下文、先前工具互動及持久資料，確保多輪交互的一致性。

接下來，我們將更詳細了解函數／工具呼叫。

### 函數／工具呼叫

函數呼叫是讓大型語言模型與工具互動的主要方式。你會經常看到「函數（Function）」和「工具（Tool）」交替使用，因為「函數」（可重用的程式區塊）正是代理用來執行任務的「工具」。要呼叫函數的程式碼，LLM 必須根據使用者請求與函數描述作比較。為此，一個包含所有可用函數描述的結構定義會被送到 LLM，LLM 從中挑選最合適的函數，回傳該函數名稱與參數。被選中的函數隨後被呼叫，其回應送回 LLM，LLM 使用此資訊來回應使用者請求。

開發者實作代理的函數呼叫需：

1. 支援函數呼叫的 LLM 模型
2. 含函數描述的結構定義
3. 每個函數對應的程式碼

用「取得某城市當前時間」這個示例說明：

1. **初始化支援函數呼叫的 LLM：**

    並非所有模型都支援函數呼叫，務必確認您使用的 LLM 是否支援。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支援函數呼叫。我們可以從啟動 Azure OpenAI 客戶端開始。

    ```python
    # 初始化 Azure OpenAI 用戶端
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **建立函數結構定義（Function Schema）：**

    接著定義一個 JSON 結構，包含函數名稱、函數描述，以及參數名稱與描述。然後將該結構與使用者想查詢舊金山時間的請求一併傳給先前建立的客戶端。重要的是，返回的是**工具呼叫**，**非問題最終答案**。如前所述，LLM 回傳它選擇的函數名稱和將要傳遞的引數。

    ```python
    # 模型閱讀用的函式描述
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
  
    # 第一次 API 呼叫：請模型使用該功能
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # 處理模型回應
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

    LLM 選擇函數後，必須實作並執行該函數程式碼來完成任務。
    我們用 Python 編寫取得當前時間的程式碼，也會實作程式來從 response_message 中提取函數名稱與參數，進而獲得最終結果。

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


函數呼叫是大多數（若非全部）代理工具使用設計的核心，然而自行實作有時候較為困難。
正如我們在[第 2 課](../../../02-explore-agentic-frameworks)所學，代理框架為我們提供了預建組件，方便實作工具使用。

## 使用代理框架的工具使用範例

以下是使用不同代理框架實作工具使用設計模式的一些範例：

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> 是一個用於構建 AI 代理的開源框架。它簡化函數呼叫的使用，允許你用 `@tool` 裝飾器將函數定義為工具。此框架處理模型與程式碼間的雙向通訊，也提供透過 `AzureAIProjectAgentProvider` 使用的預建工具，例如檔案搜尋和程式碼解譯器。

下圖示意 Microsoft Agent Framework 中函數呼叫的流程：

![function calling](../../../translated_images/zh-TW/functioncalling-diagram.a84006fc287f6014.webp)

在 Microsoft Agent Framework 中，工具是以裝飾函數的方式定義。我們可將前面示範的 `get_current_time` 函數使用 `@tool` 裝飾器轉換為工具。框架會自動序列化函數及其參數，建立傳給 LLM 的結構定義。

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

# 建立代理並使用工具執行
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> 是較新的代理框架，旨在幫助開發者安全地建立、部署及擴展高品質且具擴充性的 AI 代理，無需管理底層運算和存儲資源。此服務特別適合企業應用，因為它是全托管且具備企業級安全性。

相比直接使用 LLM API，Azure AI Agent Service 具有以下優勢：

- 自動工具呼叫 —— 無需解析工具呼叫、執行工具和處理回應，所有這些在伺服器端完成
- 安全管理資料 —— 不需自行管理對話狀態，可利用聊天室 (threads) 儲存所需資訊
- 開箱即用的工具 —— 可與資料來源互動的工具，如 Bing、Azure AI 搜尋及 Azure Functions

Azure AI Agent Service 的工具可分為兩大類別：

1. 知識工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">結合 Bing 搜尋</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">檔案搜尋</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 搜尋</a>

2. 動作工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函數呼叫</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">程式碼解譯器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 定義的工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

此代理服務允許我們將這些工具組合成一個 `toolset`。它也利用 `threads` 來追蹤特定對話的訊息歷史。

假設你是 Contoso 公司的銷售代理，想建立一個能回答銷售資料問題的對話代理。

下圖說明如何運用 Azure AI Agent Service 來分析銷售資料：

![Agentic Service In Action](../../../translated_images/zh-TW/agent-service-in-action.34fb465c9a84659e.webp)

要在此服務中使用任一工具，可先建立客戶端並定義工具或工具集。我們可用以下 Python 程式碼實作。LLM 將可參考工具集，根據使用者需求選擇使用自訂函數 `fetch_sales_data_using_sqlite_query` 或預建的程式碼解譯器。

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query 函式，可以在 fetch_sales_data_functions.py 檔案中找到。
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# 初始化工具集
toolset = ToolSet()

# 使用 fetch_sales_data_using_sqlite_query 函式初始化函式調用代理，並將其加入工具集
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# 初始化程式碼解譯器工具並將其加入工具集。
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用設計模式建立值得信賴 AI 代理的特殊考量？

LLM 動態生成的 SQL 通常引發安全疑慮，尤其是 SQL 注入或惡意操作（如刪除或篡改資料庫）的風險。儘管這些顧慮合理，但透過正確配置資料庫存取權限，能有效緩解這些風險。對大多數資料庫而言，通常將資料庫設定為唯讀即可。像 PostgreSQL 或 Azure SQL 這類資料庫服務，應將應用分配唯讀（SELECT）角色。

在安全環境中運行應用更能提升保護。企業場景多是先從營運系統中提取、轉換資料到唯讀資料庫或資料倉儲，並使用易用結構。此策略確保資料安全、優化效能與可存取性，同時應用僅有受限的唯讀權限。

## 範例程式碼

- Python：[Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET：[Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## 還有關於工具使用設計模式的問題？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，與其他學習者交流，參加辦公時間，解決你的 AI 代理問題。

## 其他資源

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service 工作坊</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso 創意寫作多代理工作坊</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework 概覽</a>

## 上一課

[了解代理設計模式](../03-agentic-design-patterns/README.md)

## 下一課
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原文文件及其母語版本應視為權威依據。對於關鍵資訊，建議採用專業人工翻譯。我們對因使用本翻譯所引起的任何誤解或誤釋不負任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->