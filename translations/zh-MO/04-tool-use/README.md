[![如何設計優秀的 AI 代理](../../../translated_images/zh-MO/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(點擊上方圖片觀看本課程影片)_

# 工具使用設計模式

工具非常有趣，因為它們讓 AI 代理擁有更廣泛的能力範圍。代理不再侷限於有限的動作集合，增加工具後，代理可執行更廣泛的動作。本章節將探討工具使用設計模式，說明 AI 代理如何使用特定工具達成其目標。

## 簡介

本課程將嘗試回答以下問題：

- 什麼是工具使用設計模式？
- 可應用於哪些使用案例？
- 實作這個設計模式需要哪些元素／構件？
- 使用工具使用設計模式構建值得信賴的 AI 代理有何特殊考量？

## 學習目標

完成本課程後，您將能：

- 定義工具使用設計模式及其目的。
- 辨識適用工具使用設計模式的使用案例。
- 了解實作該設計模式所需的關鍵元素。
- 注意使用此設計模式確保 AI 代理信賴度的重點。

## 什麼是工具使用設計模式？

<strong>工具使用設計模式</strong>著重於賦予大型語言模型（LLM）與外部工具互動的能力以達成特定目標。工具是代理可執行的程式碼以執行動作。工具可為簡單函式，如計算機，或第三方服務的 API 呼叫，如股票價格查詢或天氣預報。在 AI 代理的框架中，工具設計為回應<strong>模型產生的函式呼叫</strong>由代理執行。

## 它可應用於哪些使用案例？

AI 代理能透過工具完成複雜任務、檢索資訊或做出決策。工具使用設計模式常用於需與外部系統動態互動的場景，如資料庫、網路服務或程式碼解譯器。此能力適用於多種使用場景，包括：

- **動態資訊檢索：** 代理可查詢外部 API 或資料庫以獲取最新數據（例如查詢 SQLite 資料庫做數據分析、抓取股票價格或天氣資訊）。
- **程式碼執行與解譯：** 代理可執行程式碼或腳本，解決數學問題、產生報告或進行模擬。
- **流程自動化：** 利用工具如工作排程器、電子郵件服務或資料管線，實現重複及多步驟工作流程自動化。
- **客戶支持：** 代理可與 CRM 系統、工單平台或知識庫互動，處理使用者查詢。
- **內容生成與編輯：** 代理可利用文法檢查、文本摘要或內容安全評估工具，協助內容創作任務。

## 實作工具使用設計模式所需元素／構建模組？

這些構件讓 AI 代理可執行廣泛任務。以下為實作工具使用設計模式所需關鍵元素：

- **函式／工具結構定義（Schemas）**：界定可用工具的詳細資訊，包含函式名稱、用途、必要參數及預期輸出。這些結構讓 LLM 理解可用工具及如何組成有效請求。

- <strong>函式執行邏輯</strong>：根據使用者意圖和對話上下文，決定何時、如何喚用工具。可能包含規劃模組、路由機制或條件流程，動態決定工具使用。

- <strong>訊息管理系統</strong>：管理使用者輸入、LLM 回應、工具呼叫及工具回覆的對話流程。

- <strong>工具整合框架</strong>：連結代理與各種工具的基礎設施，無論是簡單函式或複雜外部服務。

- <strong>錯誤處理與驗證</strong>：處理工具執行錯誤，參數驗證，及異常回應管理。

- <strong>狀態管理</strong>：追蹤對話上下文、先前工具互動及持續資料，確保多輪交互一致性。

接下來，我們將更詳細介紹函式／工具呼叫。

### 函式／工具呼叫

函式呼叫為大型語言模型（LLM）與工具互動的主要方式。函式和工具常被互用，因為「函式」（可重用的程式碼區塊）即是代理用以執行任務的「工具」。為調用函式程式碼，LLM 需將使用者請求與函式描述比對。為此，會將包含所有可用函式描述的結構（schema）傳送給 LLM。LLM 會選擇最合適的函式，並回傳函式名及參數。然後執行該函式，回應結果發回 LLM，LLM 利用該資料回覆使用者請求。

開發者若要為代理實作函式呼叫，需具備：

1. 支援函式呼叫的 LLM 模型
2. 含有函式描述的結構（schema）
3. 每個函式對應的程式碼

以下以取得城市當前時間為例說明：

1. **初始化支援函式呼叫的 LLM：**

    非所有模型皆支援函式呼叫，確認所用 LLM 是否支援很重要。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支援函式呼叫。我們可以先啟動 Azure OpenAI 用戶端。

    ```python
    # 初始化 Azure OpenAI 用戶端
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **建立函式結構（Function Schema）：**

    接著定義 JSON 結構，包含函式名稱、功能描述及參數名稱與描述。
    再將此結構連同使用者要求（例如尋找舊金山時間）一起傳給先前建立的用戶端。重要的一點是，回傳的是一個<strong>工具呼叫</strong>，<strong>不是</strong>問題的最終答案。如前述，LLM 回傳其判斷適合的函式及將傳入的引數。

    ```python
    # 模型讀取的功能描述
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
  
    # 第一次 API 呼叫：要求模型使用該功能
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
  
1. **執行任務所需的函式程式碼：**

    LLM 已選定要執行的函式，接著執行對應程式碼完成任務。
    可以用 Python 實作獲得當前時間的程式碼。也需撰寫程式碼，從 response_message 擷取函式名稱與參數，以取得最終結果。

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

函式呼叫是多數（如果不是全部）代理工具使用設計的核心，然而從零實作有時較具挑戰性。
如我們在[課程 2](../../../02-explore-agentic-frameworks)所學，代理框架為我們提供預先建構的構件，方便實現工具使用。
 
## 使用代理框架的工具使用範例

以下為使用不同代理框架實作工具使用設計模式的範例：

### 微軟代理框架

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">微軟代理框架</a>是建構 AI 代理的開源框架。它透過 `@tool` 裝飾器讓你將工具定義為 Python 函式，簡化函式呼叫。框架管理模型與程式碼間的雙向溝通，也提供像是檔案搜尋與程式碼解譯器等預建工具，透過 `AzureAIProjectAgentProvider` 存取。

下圖展示使用微軟代理框架進行函式呼叫的流程：

![function calling](../../../translated_images/zh-MO/functioncalling-diagram.a84006fc287f6014.webp)

在此框架中，工具定義為被裝飾的函式。我們可用 `@tool` 裝飾先前看到的 `get_current_time` 函式，使其成為工具。框架會自動序列化函式及其參數，產生傳給 LLM 的結構。

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

# 建立代理並使用工具運行
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI 代理服務

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI 代理服務</a>為較新代理框架，設計讓開發者能安全構建、部署及擴展高品質且可擴充的 AI 代理，無需管理底層計算與儲存資源。此服務特別適合企業應用，因為它是全托管服務且具企業級安全性。

與直接使用 LLM API 開發相比，Azure AI 代理服務提供優勢包括：

- 自動工具呼叫 — 不必解析工具呼叫、呼叫工具及處理回應，這些皆由伺服器端處理
- 安全管理資料 — 透過 threads 儲存需要的資訊取代自行管理對話狀態
- 內建工具 — 可操作資料來源的工具，如 Bing、Azure AI 搜尋及 Azure Functions

Azure AI 代理服務的工具分為兩類：

1. 知識工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">以 Bing 搜尋為基底</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">檔案搜尋</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 搜尋</a>

2. 動作工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函式呼叫</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">程式碼解譯器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 定義工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

代理服務允許我們把這些工具組合成 `toolset`（工具集）。它亦利用 `threads` 記錄特定對話訊息歷史。

假設你是 Contoso 公司的銷售員代理，想設計一個對話代理回答銷售數據查詢。

下圖說明如何用 Azure AI 代理服務分析銷售數據：

![Agentic Service In Action](../../../translated_images/zh-MO/agent-service-in-action.34fb465c9a84659e.webp)

要使用服務中的任一工具，我們可建立用戶端並定義工具或工具集。實作可參考以下 Python 代碼。LLM 會根據使用者請求從工具集中判斷應使用自訂函式 `fetch_sales_data_using_sqlite_query` 或內建程式碼解譯器。

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

# 初始化工具集
toolset = ToolSet()

# 使用 fetch_sales_data_using_sqlite_query 函數初始化函數調用代理，並將其加入工具集
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# 初始化程式碼解譯器工具並將其加入工具集。
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用設計模式構建值得信賴 AI 代理時有哪些特殊考量？

使用 LLM 動態生成 SQL 等語句時，常見關注點為安全性，特別是 SQL 注入或惡意行為風險，如刪除或篡改資料庫。這些風險雖真實，但可透過適當設定資料庫存取權限有效減輕。一般資料庫配置為唯讀即可。對 PostgreSQL 或 Azure SQL 這類資料庫服務，應指派應用程式唯讀（SELECT）角色。

在安全環境運行應用更增強保障。企業情境中，數據通常自營運系統提取並轉換至唯讀資料庫或資料倉儲，並設計使用者友好結構。此方式確保數據安全、優化性能與可存取，應用也僅享受限制唯讀權限。

## 範例程式碼

- Python: [代理框架](./code_samples/04-python-agent-framework.ipynb)
- .NET: [代理框架](./code_samples/04-dotnet-agent-framework.md)

## 對工具使用設計模式有更多問題？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)，與其他學習者交流，參加辦公時間，並獲得 AI 代理相關問題解答。

## 額外資源

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI 代理服務工作坊</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso 創意寫作多代理工作坊</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">微軟代理框架總覽</a>

## 上一課

[理解代理設計模式](../03-agentic-design-patterns/README.md)

## 下一課
[自主代理 RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->