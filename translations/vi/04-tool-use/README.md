<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T17:54:29+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "vi"
}
-->
[![Cách thiết kế các tác nhân AI tốt](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.vi.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Nhấp vào hình ảnh trên để xem video của bài học này)_

# Mẫu thiết kế sử dụng công cụ

Công cụ rất thú vị vì chúng cho phép các tác nhân AI có khả năng rộng hơn. Thay vì tác nhân chỉ có một tập hợp hành động hạn chế, việc thêm một công cụ sẽ giúp tác nhân có thể thực hiện nhiều hành động khác nhau. Trong chương này, chúng ta sẽ tìm hiểu về Mẫu thiết kế sử dụng công cụ, mô tả cách các tác nhân AI có thể sử dụng các công cụ cụ thể để đạt được mục tiêu của mình.

## Giới thiệu

Trong bài học này, chúng ta sẽ tìm cách trả lời các câu hỏi sau:

- Mẫu thiết kế sử dụng công cụ là gì?
- Những trường hợp sử dụng nào có thể áp dụng mẫu thiết kế này?
- Những yếu tố/cấu trúc cần thiết để triển khai mẫu thiết kế này là gì?
- Những lưu ý đặc biệt nào khi sử dụng Mẫu thiết kế sử dụng công cụ để xây dựng các tác nhân AI đáng tin cậy?

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Định nghĩa Mẫu thiết kế sử dụng công cụ và mục đích của nó.
- Xác định các trường hợp sử dụng mà Mẫu thiết kế sử dụng công cụ có thể áp dụng.
- Hiểu các yếu tố chính cần thiết để triển khai mẫu thiết kế này.
- Nhận biết các lưu ý để đảm bảo tính đáng tin cậy trong các tác nhân AI sử dụng mẫu thiết kế này.

## Mẫu thiết kế sử dụng công cụ là gì?

**Mẫu thiết kế sử dụng công cụ** tập trung vào việc cung cấp cho LLMs khả năng tương tác với các công cụ bên ngoài để đạt được các mục tiêu cụ thể. Công cụ là đoạn mã có thể được thực thi bởi một tác nhân để thực hiện các hành động. Một công cụ có thể là một hàm đơn giản như máy tính, hoặc một API gọi đến dịch vụ bên thứ ba như tra cứu giá cổ phiếu hoặc dự báo thời tiết. Trong bối cảnh các tác nhân AI, công cụ được thiết kế để được thực thi bởi các tác nhân nhằm đáp ứng các **lời gọi hàm do mô hình tạo ra**.

## Những trường hợp sử dụng nào có thể áp dụng?

Các tác nhân AI có thể tận dụng công cụ để hoàn thành các nhiệm vụ phức tạp, truy xuất thông tin hoặc đưa ra quyết định. Mẫu thiết kế sử dụng công cụ thường được sử dụng trong các tình huống yêu cầu tương tác động với các hệ thống bên ngoài, chẳng hạn như cơ sở dữ liệu, dịch vụ web hoặc trình thông dịch mã. Khả năng này hữu ích cho nhiều trường hợp sử dụng khác nhau bao gồm:

- **Truy xuất thông tin động:** Các tác nhân có thể truy vấn API hoặc cơ sở dữ liệu bên ngoài để lấy dữ liệu cập nhật (ví dụ: truy vấn cơ sở dữ liệu SQLite để phân tích dữ liệu, lấy giá cổ phiếu hoặc thông tin thời tiết).
- **Thực thi và thông dịch mã:** Các tác nhân có thể thực thi mã hoặc script để giải quyết các vấn đề toán học, tạo báo cáo hoặc thực hiện các mô phỏng.
- **Tự động hóa quy trình làm việc:** Tự động hóa các quy trình lặp lại hoặc nhiều bước bằng cách tích hợp các công cụ như bộ lập lịch tác vụ, dịch vụ email hoặc đường dẫn dữ liệu.
- **Hỗ trợ khách hàng:** Các tác nhân có thể tương tác với hệ thống CRM, nền tảng quản lý vé hoặc cơ sở tri thức để giải quyết các câu hỏi của người dùng.
- **Tạo và chỉnh sửa nội dung:** Các tác nhân có thể tận dụng các công cụ như kiểm tra ngữ pháp, tóm tắt văn bản hoặc đánh giá an toàn nội dung để hỗ trợ các nhiệm vụ tạo nội dung.

## Những yếu tố/cấu trúc cần thiết để triển khai mẫu thiết kế sử dụng công cụ là gì?

Những cấu trúc này cho phép tác nhân AI thực hiện nhiều nhiệm vụ khác nhau. Hãy cùng xem các yếu tố chính cần thiết để triển khai Mẫu thiết kế sử dụng công cụ:

- **Schemas hàm/công cụ:** Định nghĩa chi tiết về các công cụ có sẵn, bao gồm tên hàm, mục đích, các tham số cần thiết và kết quả mong đợi. Các schemas này giúp LLM hiểu được các công cụ có sẵn và cách tạo các yêu cầu hợp lệ.

- **Logic thực thi hàm:** Quản lý cách và thời điểm các công cụ được gọi dựa trên ý định của người dùng và ngữ cảnh cuộc trò chuyện. Điều này có thể bao gồm các mô-đun lập kế hoạch, cơ chế định tuyến hoặc các luồng điều kiện xác định việc sử dụng công cụ một cách động.

- **Hệ thống xử lý tin nhắn:** Các thành phần quản lý luồng cuộc trò chuyện giữa đầu vào của người dùng, phản hồi của LLM, các lời gọi công cụ và kết quả công cụ.

- **Khung tích hợp công cụ:** Hạ tầng kết nối tác nhân với các công cụ khác nhau, dù đó là các hàm đơn giản hay các dịch vụ bên ngoài phức tạp.

- **Xử lý lỗi & xác thực:** Cơ chế xử lý các lỗi trong thực thi công cụ, xác thực tham số và quản lý các phản hồi không mong muốn.

- **Quản lý trạng thái:** Theo dõi ngữ cảnh cuộc trò chuyện, các tương tác công cụ trước đó và dữ liệu liên tục để đảm bảo tính nhất quán trong các tương tác nhiều lượt.

Tiếp theo, hãy cùng tìm hiểu chi tiết về việc gọi hàm/công cụ.

### Gọi hàm/công cụ

Gọi hàm là cách chính để chúng ta cho phép các Mô hình Ngôn ngữ Lớn (LLMs) tương tác với các công cụ. Bạn thường thấy 'Hàm' và 'Công cụ' được sử dụng thay thế cho nhau vì 'hàm' (các khối mã có thể tái sử dụng) chính là 'công cụ' mà các tác nhân sử dụng để thực hiện nhiệm vụ. Để mã của một hàm được gọi, LLM phải so sánh yêu cầu của người dùng với mô tả của hàm. Để làm điều này, một schema chứa mô tả của tất cả các hàm có sẵn được gửi đến LLM. LLM sau đó chọn hàm phù hợp nhất cho nhiệm vụ và trả về tên và các tham số của nó. Hàm được chọn sẽ được gọi, phản hồi của nó được gửi lại cho LLM, và LLM sử dụng thông tin này để phản hồi yêu cầu của người dùng.

Để các nhà phát triển triển khai việc gọi hàm cho các tác nhân, bạn sẽ cần:

1. Một mô hình LLM hỗ trợ gọi hàm
2. Một schema chứa mô tả hàm
3. Mã cho mỗi hàm được mô tả

Hãy sử dụng ví dụ về việc lấy thời gian hiện tại ở một thành phố để minh họa:

1. **Khởi tạo một LLM hỗ trợ gọi hàm:**

    Không phải tất cả các mô hình đều hỗ trợ gọi hàm, vì vậy điều quan trọng là phải kiểm tra xem LLM bạn đang sử dụng có hỗ trợ không. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> hỗ trợ gọi hàm. Chúng ta có thể bắt đầu bằng cách khởi tạo client Azure OpenAI.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Tạo một Schema hàm:**

    Tiếp theo, chúng ta sẽ định nghĩa một schema JSON chứa tên hàm, mô tả về những gì hàm thực hiện, và tên cùng mô tả của các tham số hàm. Sau đó, chúng ta sẽ lấy schema này và gửi nó đến client đã tạo trước đó, cùng với yêu cầu của người dùng để tìm thời gian ở San Francisco. Điều quan trọng cần lưu ý là một **lời gọi công cụ** được trả về, **không phải** câu trả lời cuối cùng cho câu hỏi. Như đã đề cập trước đó, LLM trả về tên của hàm mà nó chọn cho nhiệm vụ, và các tham số sẽ được gửi đến hàm đó.

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Mã hàm cần thiết để thực hiện nhiệm vụ:**

    Bây giờ LLM đã chọn hàm cần được chạy, mã thực hiện nhiệm vụ cần được triển khai và thực thi. Chúng ta có thể triển khai mã để lấy thời gian hiện tại bằng Python. Chúng ta cũng cần viết mã để trích xuất tên và tham số từ response_message để có kết quả cuối cùng.

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

Gọi hàm là cốt lõi của hầu hết, nếu không muốn nói là tất cả, thiết kế sử dụng công cụ của tác nhân, tuy nhiên việc triển khai từ đầu đôi khi có thể gặp khó khăn. Như chúng ta đã học trong [Bài học 2](../../../02-explore-agentic-frameworks), các khung tác nhân cung cấp cho chúng ta các cấu trúc dựng sẵn để triển khai sử dụng công cụ.

## Ví dụ sử dụng công cụ với các khung tác nhân

Dưới đây là một số ví dụ về cách bạn có thể triển khai Mẫu thiết kế sử dụng công cụ bằng các khung tác nhân khác nhau:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> là một khung AI mã nguồn mở dành cho các nhà phát triển .NET, Python và Java làm việc với các Mô hình Ngôn ngữ Lớn (LLMs). Nó đơn giản hóa quá trình sử dụng gọi hàm bằng cách tự động mô tả các hàm và tham số của chúng cho mô hình thông qua một quy trình gọi là <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializing</a>. Nó cũng xử lý việc giao tiếp qua lại giữa mô hình và mã của bạn. Một lợi thế khác của việc sử dụng khung tác nhân như Semantic Kernel là nó cho phép bạn truy cập các công cụ dựng sẵn như <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> và <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Sơ đồ sau minh họa quy trình gọi hàm với Semantic Kernel:

![gọi hàm](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.vi.png)

Trong Semantic Kernel, các hàm/công cụ được gọi là <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Chúng ta có thể chuyển đổi hàm `get_current_time` mà chúng ta đã thấy trước đó thành một plugin bằng cách biến nó thành một lớp chứa hàm đó. Chúng ta cũng có thể nhập decorator `kernel_function`, nhận mô tả của hàm. Khi bạn tạo một kernel với GetCurrentTimePlugin, kernel sẽ tự động serialize hàm và các tham số của nó, tạo schema để gửi đến LLM trong quá trình này.

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

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> là một khung tác nhân mới được thiết kế để giúp các nhà phát triển xây dựng, triển khai và mở rộng các tác nhân AI chất lượng cao, có thể mở rộng mà không cần quản lý tài nguyên tính toán và lưu trữ cơ bản. Nó đặc biệt hữu ích cho các ứng dụng doanh nghiệp vì đây là một dịch vụ được quản lý hoàn toàn với bảo mật cấp doanh nghiệp.

So với việc phát triển trực tiếp với API LLM, Azure AI Agent Service mang lại một số lợi thế, bao gồm:

- Gọi công cụ tự động – không cần phân tích lời gọi công cụ, thực thi công cụ và xử lý phản hồi; tất cả điều này hiện được thực hiện trên máy chủ
- Quản lý dữ liệu an toàn – thay vì quản lý trạng thái cuộc trò chuyện của riêng bạn, bạn có thể dựa vào các threads để lưu trữ tất cả thông tin bạn cần
- Các công cụ dựng sẵn – Các công cụ mà bạn có thể sử dụng để tương tác với các nguồn dữ liệu của mình, chẳng hạn như Bing, Azure AI Search và Azure Functions.

Các công cụ có sẵn trong Azure AI Agent Service có thể được chia thành hai loại:

1. Công cụ Kiến thức:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding với Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Công cụ Hành động:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Gọi hàm</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Các công cụ được định nghĩa bởi OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Dịch vụ Agent cho phép chúng ta sử dụng các công cụ này cùng nhau như một `toolset`. Nó cũng sử dụng `threads` để theo dõi lịch sử các tin nhắn từ một cuộc trò chuyện cụ thể.

Hãy tưởng tượng bạn là một nhân viên bán hàng tại một công ty tên là Contoso. Bạn muốn phát triển một tác nhân trò chuyện có thể trả lời các câu hỏi về dữ liệu bán hàng của bạn.

Hình ảnh sau minh họa cách bạn có thể sử dụng Azure AI Agent Service để phân tích dữ liệu bán hàng của mình:

![Dịch vụ Agent đang hoạt động](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.vi.jpg)

Để sử dụng bất kỳ công cụ nào với dịch vụ này, chúng ta có thể tạo một client và định nghĩa một công cụ hoặc bộ công cụ. Để triển khai điều này một cách thực tế, chúng ta có thể sử dụng mã Python sau. LLM sẽ có thể xem xét bộ công cụ và quyết định sử dụng hàm do người dùng tạo, `fetch_sales_data_using_sqlite_query`, hoặc Code Interpreter dựng sẵn tùy thuộc vào yêu cầu của người dùng.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Những lưu ý đặc biệt khi sử dụng Mẫu thiết kế sử dụng công cụ để xây dựng các tác nhân AI đáng tin cậy?

Một mối quan tâm phổ biến với SQL được tạo động bởi LLMs là vấn đề bảo mật, đặc biệt là nguy cơ SQL injection hoặc các hành động độc hại, chẳng hạn như xóa hoặc làm hỏng cơ sở dữ liệu. Mặc dù những lo ngại này là hợp lý, chúng có thể được giảm thiểu hiệu quả bằng cách cấu hình quyền truy cập cơ sở dữ liệu một cách đúng đắn. Đối với hầu hết các cơ sở dữ liệu, điều này bao gồm cấu hình cơ sở dữ liệu ở chế độ chỉ đọc. Đối với các dịch vụ cơ sở dữ liệu như PostgreSQL hoặc Azure SQL, ứng dụng nên được gán một vai trò chỉ đọc (SELECT).
Chạy ứng dụng trong một môi trường an toàn sẽ tăng cường bảo vệ hơn nữa. Trong các tình huống doanh nghiệp, dữ liệu thường được trích xuất và chuyển đổi từ các hệ thống vận hành sang một cơ sở dữ liệu chỉ đọc hoặc kho dữ liệu với một cấu trúc thân thiện với người dùng. Cách tiếp cận này đảm bảo rằng dữ liệu được bảo mật, tối ưu hóa cho hiệu suất và khả năng truy cập, đồng thời ứng dụng chỉ có quyền truy cập hạn chế, chỉ đọc.

## Mã Mẫu

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Có Thắc Mắc Thêm Về Cách Sử Dụng Các Mẫu Thiết Kế Công Cụ?

Tham gia [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ những người học khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về AI Agents của bạn.

## Tài Nguyên Bổ Sung

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Hội Thảo Dịch Vụ Azure AI Agents</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Hội Thảo Multi-Agent Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Hướng Dẫn Gọi Hàm Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Trình Thông Dịch Mã Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Công Cụ Autogen</a>

## Bài Học Trước

[Hiểu Các Mẫu Thiết Kế Agentic](../03-agentic-design-patterns/README.md)

## Bài Học Tiếp Theo

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->