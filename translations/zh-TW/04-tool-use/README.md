[![如何設計良好的 AI 代理人](../../../translated_images/zh-TW/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(點擊上方圖片觀看本課程影片)_

# 工具使用設計模式

工具很有趣，因為它讓 AI 代理人能夠擴展其能力範圍。代理人不再僅僅能執行有限動作，透過加入工具，代理人現在可以執行廣泛的動作。在本章中，我們將探討工具使用設計模式，描述 AI 代理人如何使用特定工具達成目標。

## 介紹

本課程將回答以下問題：

- 什麼是工具使用設計模式？
- 它可以應用於哪些使用案例？
- 實作設計模式需要哪些元素/構建模組？
- 使用工具使用設計模式建立可信賴 AI 代理人時，有哪些特別考量？

## 學習目標

完成本課程後，您將能夠：

- 定義工具使用設計模式及其目的。
- 識別適用於工具使用設計模式的使用案例。
- 了解實作該設計模式所需的關鍵元素。
- 辨識使用此設計模式的 AI 代理人確保可信賴性的考量。

## 什麼是工具使用設計模式？

**工具使用設計模式**著重於賦予大型語言模型 (LLM) 與外部工具互動的能力，以達成特定目標。工具是可由代理人執行的程式碼，以執行動作。工具可以是簡單的函式，例如計算機，或呼叫第三方服務的 API，例如股票價格查詢或天氣預報。在 AI 代理人的語境中，工具設計成由代理人根據**模型產生的函式呼叫**來執行。

## 它可應用於哪些使用案例？

AI 代理人可利用工具完成複雜任務、檢索資訊或做出決策。工具使用設計模式常用於需要與外部系統如資料庫、網絡服務或程式碼解譯器進行動態互動的情境。這樣的能力對多種使用案例非常有用，包括：

- **動態資訊檢索：**代理人可查詢外部 API 或資料庫以取得最新資料（例如查詢 SQLite 資料庫進行資料分析，取得股票價格或天氣資訊）。
- **程式碼執行與解譯：**代理人可執行程式碼或腳本來解決數學問題、產生報告或進行模擬。
- **工作流程自動化：**透過整合任務排程器、電子郵件服務或資料管道等工具，自動化重複或多步驟的工作流程。
- **客戶支援：**代理人能與 CRM 系統、工單平台或知識庫互動，以解決使用者問題。
- **內容生成與編輯：**代理人可利用文法檢查器、文本摘要器或內容安全評估工具來協助內容創建任務。

## 實作工具使用設計模式需要哪些元素/構建模組？

這些構建模組允許 AI 代理人執行廣泛的任務。以下是實作工具使用設計模式所需的關鍵元素：

- **函式/工具結構（Schemas）：**詳細定義可用工具，包括函式名稱、用途、必要參數與預期輸出。這些結構讓 LLM 理解哪些工具可用及如何構造有效的請求。

- **函式執行邏輯：**管理何時及如何根據使用者意圖與對話上下文呼叫工具。可能包含規劃模組、路由機制或條件流程以動態決定工具使用。

- **訊息處理系統：**管理使用者輸入、LLM 回應、工具呼叫及工具輸出之間的對話流程組件。

- **工具整合框架：**連結代理人與各種工具，不論是簡單函式還是複雜的外部服務的基礎建設。

- **錯誤處理與驗證：**處理工具執行失敗、驗證參數及管理意外回應的機制。

- **狀態管理：**追蹤對話上下文、先前工具交互與持續資料，以確保多回合互動的連貫性。

接下來，我們將詳細介紹函式/工具呼叫。

### 函式/工具呼叫

函式呼叫是讓大型語言模型 (LLM) 與工具互動的主要方式。您會常見 “函式” 與 “工具” 一詞可互換使用，因為函式（可重複使用的程式碼區塊）就是代理人用來完成任務的 “工具”。要執行函式程式碼，LLM 必須根據使用者請求與函式描述進行對照。為此，我們會將包含所有可用函式描述的結構傳送給 LLM。LLM 將選擇最合適的函式並回傳其名稱與參數。接著呼叫所選函式，將其回應傳回給 LLM，LLM 會基於該資訊回應使用者。

開發者實作函式呼叫功能時，需要：

1. 支援函式呼叫的 LLM 模型
2. 包含函式描述的結構（Schema）
3. 每個函式的程式碼

我們以獲取某城市當前時間為例說明：

1. **初始化支援函式呼叫的 LLM：**

    不是所有模型都支援函式呼叫，必須確定您使用的 LLM 有此功能。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支援函式呼叫。我們可以先啟動 Azure OpenAI 用戶端。

    ```python
    # 初始化 Azure OpenAI 用戶端
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **建立函式結構（Schema）：**

    接著會定義一個 JSON 結構，包含函式名稱、函式功能描述，以及函式參數名稱與描述。
    之後將此結構連同使用者要求傳給之前建立的用戶端，要求查詢舊金山時間。重要的是要注意，回傳的是一個**工具呼叫**，**不是問題的最終答案**。如前所述，LLM 回傳它選擇的函式名稱與相應的參數。

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
  
    # 第一次 API 呼叫：請模型使用該函式
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
  
1. **執行任務所需的函式程式碼：**

    LLM 選定需要運行的函式後，就要實作並執行執行該功能的程式碼。
    我們以 Python 實作取得當前時間的程式碼。還須編寫程式碼從 response_message 中擷取函式名稱與參數來取得最終結果。

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
  
      # 第二次 API 調用：從模型取得最終回應
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

函式呼叫是大多數（如果不是全部）代理人工具使用設計的核心，但從頭實作有時非常挑戰。
如在 [第 2 課](../../../02-explore-agentic-frameworks) 所學，代理框架提供我們預建模組以實作工具使用。
 
## 使用代理框架的工具使用範例

以下是使用不同代理框架實作工具使用設計模式的範例：

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> 是一個為 .NET、Python 與 Java 開發者設計的開源 AI 框架，專注大型語言模型 (LLM)。它透過一種稱為 <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">序列化</a> 的過程，自動向模型描述您的函式及其參數，簡化函式呼叫使用。它也管理模型與程式碼之間的雙向通訊。使用 Semantic Kernel 此類代理框架的另一個優點是，它讓您可使用預建工具，如<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">檔案搜尋</a>與<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">程式碼解譯器</a>。

下圖說明 Semantic Kernel 的函式呼叫流程：

![function calling](../../../translated_images/zh-TW/functioncalling-diagram.a84006fc287f6014.webp)

在 Semantic Kernel 中，函式/工具稱為<a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">擴充套件（Plugins）</a>。我們可將之前的 `get_current_time` 函式轉成擴充套件，方法是將其包裝在类中，並引入 `kernel_function` 裝飾器，該裝飾器帶有函式描述。當您使用 GetCurrentTimePlugin 建立 kernel 時，kernel 會自動序列化函式與參數，在過程中建立可傳送給 LLM 的結構。

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

# 建立外掛
get_current_time_plugin = GetCurrentTimePlugin(location)

# 將外掛加入核心
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> 是較新的代理框架，旨在幫助開發者安全地建立、部署並擴展高品質且可延伸的 AI 代理人，無需自行管理底層計算與存儲資源。它特別適用於企業應用，因為它是具有企業級安全性的全方位管理服務。

相較於直接使用 LLM API 開發，Azure AI Agent Service 提供下列優勢：

- 自動工具呼叫—不需手動解析工具呼叫、執行工具及處理回應，這些皆由伺服器端完成
- 安全管理的資料—無需自行管理會話狀態，可依賴線程存儲所有必要資訊
- 現成工具—提供可用來互動資料來源的工具，如 Bing、Azure AI Search 及 Azure Functions

Azure AI Agent Service 中可用的工具可分為兩類：

1. 知識工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing 搜尋基底</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">檔案搜尋</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 搜尋</a>

2. 動作工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函式呼叫</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">程式碼解譯器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI 定義工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

此代理服務允許我們將這些工具作為 `toolset` 一起使用，並利用 `threads` 追蹤特定對話的訊息歷史。

假設您是名為 Contoso 公司的銷售代理人，想開發一個能回答銷售資料問題的會話型代理人。

下圖說明如何使用 Azure AI Agent Service 分析銷售資料：

![Agentic Service In Action](../../../translated_images/zh-TW/agent-service-in-action.34fb465c9a84659e.webp)

要使用這些工具，我們可以建立用戶端並定義工具或工具組。以下 Python 程式碼示範如何實作。LLM 將查看工具組並判斷要使用使用者建立的函式 `fetch_sales_data_using_sqlite_query`，或是內建的程式碼解譯器，取決於使用者需求。

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query 函數，可以在 fetch_sales_data_functions.py 檔案中找到。
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# 初始化工具集
toolset = ToolSet()

# 使用 fetch_sales_data_using_sqlite_query 函數初始化函數調用代理，並將其添加到工具集中
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# 初始化代碼解釋器工具並將其添加到工具集中。
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用設計模式建立可信賴 AI 代理人的特別考量？

LLM 動態生成的 SQL 常見安全疑慮是 SQL 注入或惡意操作，例如刪除或竄改資料庫。雖然這些擔憂合理，但可透過妥善配置資料庫存取權限來有效減輕。多數資料庫可設定為唯讀模式。對 PostgreSQL 或 Azure SQL 等資料庫服務，應將應用程式指定唯讀（SELECT）角色。
在安全環境中執行應用程式可進一步增強保護。在企業場景中，資料通常會從營運系統中抽取並轉換到具有使用者友善結構的唯讀資料庫或資料倉儲。此方法確保資料安全、為效能及可存取性進行最佳化，且應用程式擁有限制的唯讀存取權限。

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Got More Questions about the Tool Use Design Patterns?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們力求準確，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->