[![Cách Thiết Kế Các Tác Nhân AI Tốt](../../../translated_images/vi/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Nhấn vào hình ảnh trên để xem video của bài học này)_

# Mẫu Thiết Kế Sử Dụng Công Cụ

Công cụ rất thú vị vì chúng cho phép các tác nhân AI có phạm vi khả năng rộng hơn. Thay vì tác nhân chỉ có một bộ hành động giới hạn, bằng cách thêm công cụ, tác nhân giờ đây có thể thực hiện một loạt các hành động đa dạng. Trong chương này, chúng ta sẽ xem xét Mẫu Thiết Kế Sử Dụng Công Cụ, mô tả cách các tác nhân AI có thể sử dụng các công cụ cụ thể để đạt được mục tiêu của họ.

## Giới thiệu

Trong bài học này, chúng ta sẽ tìm câu trả lời cho các câu hỏi sau:

- Mẫu thiết kế sử dụng công cụ là gì?
- Các trường hợp sử dụng mà nó có thể áp dụng là gì?
- Các yếu tố/khối xây dựng cần thiết để triển khai mẫu thiết kế là gì?
- Các lưu ý đặc biệt khi sử dụng Mẫu Thiết Kế Sử Dụng Công Cụ để xây dựng các tác nhân AI đáng tin cậy là gì?

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Định nghĩa Mẫu Thiết Kế Sử Dụng Công Cụ và mục đích của nó.
- Xác định các trường hợp sử dụng mà Mẫu Thiết Kế Sử Dụng Công Cụ thích hợp.
- Hiểu các yếu tố chính cần thiết để triển khai mẫu thiết kế.
- Nhận biết các lưu ý để đảm bảo độ tin cậy trong các tác nhân AI sử dụng mẫu thiết kế này.

## Mẫu Thiết Kế Sử Dụng Công Cụ là gì?

**Mẫu Thiết Kế Sử Dụng Công Cụ** tập trung vào việc cung cấp cho các Mô Hình Ngôn Ngữ Lớn (LLMs) khả năng tương tác với các công cụ bên ngoài để đạt được các mục tiêu cụ thể. Công cụ là đoạn mã có thể được một tác nhân thực thi để thực hiện các hành động. Một công cụ có thể là một hàm đơn giản như máy tính, hoặc một cuộc gọi API đến dịch vụ bên thứ ba như tra cứu giá cổ phiếu hoặc dự báo thời tiết. Trong ngữ cảnh các tác nhân AI, các công cụ được thiết kế để được thực thi bởi các tác nhân đáp lại các **lệnh gọi hàm do mô hình tạo ra**.

## Các trường hợp sử dụng mà nó có thể áp dụng là gì?

Các tác nhân AI có thể tận dụng các công cụ để hoàn thành các tác vụ phức tạp, truy xuất thông tin hoặc đưa ra quyết định. Mẫu thiết kế sử dụng công cụ thường được dùng trong những kịch bản yêu cầu tương tác động với các hệ thống bên ngoài, chẳng hạn như cơ sở dữ liệu, dịch vụ web hoặc trình thông dịch mã. Khả năng này hữu ích cho nhiều trường hợp sử dụng khác nhau bao gồm:

- **Truy xuất Thông tin Động:** Các tác nhân có thể truy vấn API bên ngoài hoặc cơ sở dữ liệu để lấy dữ liệu cập nhật (ví dụ: truy vấn cơ sở dữ liệu SQLite để phân tích dữ liệu, lấy giá cổ phiếu hoặc thông tin thời tiết).
- **Thực thi và Giải thích Mã:** Các tác nhân có thể thực thi mã hoặc script để giải các bài toán toán học, tạo báo cáo, hoặc thực hiện mô phỏng.
- **Tự động hóa Quy trình làm việc:** Tự động hóa các quy trình lặp đi lặp lại hoặc đa bước bằng cách tích hợp các công cụ như bộ lập lịch tác vụ, dịch vụ email, hoặc pipeline dữ liệu.
- **Hỗ trợ Khách hàng:** Các tác nhân có thể tương tác với hệ thống quản lý khách hàng (CRM), nền tảng quản lý phiếu hỗ trợ, hoặc cơ sở kiến thức để giải đáp thắc mắc của người dùng.
- **Tạo và Chỉnh sửa Nội dung:** Các tác nhân có thể sử dụng các công cụ như kiểm tra ngữ pháp, tóm tắt văn bản, hoặc đánh giá an toàn nội dung để hỗ trợ tạo nội dung.

## Các yếu tố/khối xây dựng cần thiết để triển khai mẫu thiết kế sử dụng công cụ là gì?

Các khối xây dựng này cho phép tác nhân AI thực hiện đa dạng nhiệm vụ. Hãy xem xét các yếu tố chính cần thiết để triển khai Mẫu Thiết Kế Sử Dụng Công Cụ:

- **Lược đồ Hàm/Công cụ:** Định nghĩa chi tiết các công cụ có sẵn, bao gồm tên hàm, mục đích, các tham số cần thiết và kết quả mong đợi. Các lược đồ này giúp LLM hiểu được những công cụ có thể dùng và cách tạo các yêu cầu hợp lệ.

- **Logic Thực thi Hàm:** Quy định cách và khi nào công cụ được gọi dựa trên ý định của người dùng và ngữ cảnh cuộc trò chuyện. Có thể bao gồm các mô-đun lập kế hoạch, cơ chế định tuyến hoặc luồng điều kiện để quyết định sử dụng công cụ một cách động.

- **Hệ thống Xử lý Tin nhắn:** Các thành phần quản lý luồng hội thoại giữa đầu vào người dùng, phản hồi của LLM, các cuộc gọi công cụ và kết quả công cụ.

- **Khung Tích hợp Công cụ:** Cơ sở hạ tầng kết nối tác nhân với các công cụ khác nhau, dù đó là hàm đơn giản hay dịch vụ bên ngoài phức tạp.

- **Xử lý Lỗi & Xác thực:** Cơ chế xử lý lỗi khi thực thi công cụ, xác thực tham số và quản lý các phản hồi bất ngờ.

- **Quản lý Trạng thái:** Theo dõi ngữ cảnh cuộc trò chuyện, các tương tác công cụ trước đó và dữ liệu lưu trữ để đảm bảo nhất quán qua nhiều lượt tương tác.

Tiếp theo, chúng ta hãy tìm hiểu chi tiết hơn về gọi Hàm/Công cụ.

### Gọi Hàm/Công cụ

Gọi hàm là cách chính để chúng ta cho phép các Mô Hình Ngôn Ngữ Lớn (LLMs) tương tác với công cụ. Bạn sẽ thường thấy 'Hàm' và 'Công cụ' được sử dụng thay thế cho nhau vì 'hàm' (khối mã tái sử dụng) chính là 'công cụ' mà tác nhân sử dụng để thực thi nhiệm vụ. Để đoạn mã hàm được gọi, LLM phải so sánh yêu cầu của người dùng với mô tả hàm. Để làm điều này, một lược đồ chứa mô tả tất cả các hàm có sẵn được gửi tới LLM. LLM sau đó chọn hàm phù hợp nhất cho nhiệm vụ và trả về tên hàm cùng các đối số. Hàm được chọn sẽ được gọi, phản hồi của nó sẽ được gửi lại cho LLM, và LLM sử dụng thông tin này để đáp lại yêu cầu của người dùng.

Để triển khai gọi hàm cho tác nhân, bạn cần:

1. Một mô hình LLM hỗ trợ gọi hàm
2. Một lược đồ chứa mô tả các hàm
3. Mã cho từng hàm mô tả

Hãy dùng ví dụ lấy thời gian hiện tại ở một thành phố để minh họa:

1. **Khởi tạo một LLM hỗ trợ gọi hàm:**

    Không phải tất cả mô hình đều hỗ trợ gọi hàm, nên việc kiểm tra kỹ LLM bạn đang dùng có hỗ trợ là rất quan trọng. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> hỗ trợ gọi hàm. Chúng ta có thể bắt đầu bằng cách khởi tạo client Azure OpenAI.

    ```python
    # Khởi tạo client Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Tạo Lược đồ Hàm:**

    Tiếp theo, chúng ta sẽ định nghĩa một lược đồ JSON chứa tên hàm, mô tả chức năng của hàm, và tên cùng mô tả các tham số hàm.
    Sau đó ta sẽ truyền lược đồ này cùng với yêu cầu của người dùng muốn tìm giờ ở San Francisco cho client vừa tạo. Điều quan trọng cần lưu ý là một **cuộc gọi công cụ** mới là thứ được trả về, **không phải** câu trả lời cuối cùng cho câu hỏi. Như đã đề cập, LLM trả về tên hàm nó chọn cho nhiệm vụ và các đối số sẽ được truyền vào.

    ```python
    # Mô tả chức năng để mô hình đọc
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
  
    # Tin nhắn người dùng ban đầu
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Lần gọi API đầu tiên: Yêu cầu mô hình sử dụng hàm
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Xử lý phản hồi của mô hình
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Mã hàm cần thiết để thực thi nhiệm vụ:**

    Khi LLM đã chọn hàm cần chạy, mã để thực thi nhiệm vụ đó phải được triển khai và thực thi.
    Chúng ta có thể triển khai mã để lấy thời gian hiện tại bằng Python. Đồng thời cũng cần viết mã để trích xuất tên và đối số từ response_message để lấy kết quả cuối cùng.

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
     # Xử lý các cuộc gọi hàm
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
  
      # Cuộc gọi API thứ hai: Lấy phản hồi cuối cùng từ mô hình
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

Gọi Hàm là trung tâm của hầu hết, nếu không phải tất cả, thiết kế sử dụng công cụ cho tác nhân, tuy nhiên việc triển khai từ đầu có thể đôi khi khó khăn.
Như chúng ta đã học trong [Bài 2](../../../02-explore-agentic-frameworks), các framework tác nhân cung cấp cho ta các khối xây dựng sẵn để triển khai sử dụng công cụ.
 
## Ví dụ Sử Dụng Công Cụ với Các Framework Agentic

Dưới đây là một số ví dụ về cách bạn có thể triển khai Mẫu Thiết Kế Sử Dụng Công Cụ bằng các framework agentic khác nhau:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> là một framework AI mã nguồn mở dành cho các nhà phát triển .NET, Python, và Java làm việc với Mô Hình Ngôn Ngữ Lớn (LLMs). Nó đơn giản hóa quá trình gọi hàm bằng cách tự động mô tả các hàm và tham số cho mô hình qua một quá trình gọi là <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">chuẩn hóa</a>. Nó cũng xử lý giao tiếp qua lại giữa mô hình và mã của bạn. Một lợi thế khác khi dùng framework agentic như Semantic Kernel là nó cho phép bạn truy cập các công cụ được xây dựng sẵn như <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Tìm kiếm Tệp</a> và <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Trình Giải Thích Mã</a>.

Sơ đồ dưới đây minh họa quá trình gọi hàm với Semantic Kernel:

![function calling](../../../translated_images/vi/functioncalling-diagram.a84006fc287f6014.webp)

Trong Semantic Kernel, các hàm/công cụ được gọi là <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugin</a>. Chúng ta có thể chuyển hàm `get_current_time` đã thấy trước đó thành một plugin bằng cách chuyển nó thành một lớp có chứa hàm. Ta cũng có thể nhập decorator `kernel_function`, nhận vào mô tả của hàm. Khi tạo kernel với GetCurrentTimePlugin, kernel sẽ tự động chuẩn hóa hàm và tham số, tạo lược đồ để gửi tới LLM trong quá trình đó.

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

# Tạo kernel
kernel = Kernel()

# Tạo plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Thêm plugin vào kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Dịch vụ Azure AI Agent

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dịch vụ Azure AI Agent</a> là một framework agentic mới được thiết kế nhằm giúp các nhà phát triển xây dựng, triển khai và mở rộng các tác nhân AI chất lượng cao, có thể mở rộng một cách an toàn mà không cần quản lý tài nguyên tính toán và lưu trữ cơ sở. Dịch vụ đặc biệt hữu ích cho các ứng dụng doanh nghiệp vì nó là dịch vụ quản lý toàn bộ với bảo mật cấp doanh nghiệp.

So với việc phát triển trực tiếp với API LLM, Azure AI Agent Service có một số lợi thế, bao gồm:

- Tự động gọi công cụ – không cần phân tích cuộc gọi công cụ, thực thi công cụ và xử lý phản hồi; tất cả được xử lý phía máy chủ
- Quản lý dữ liệu an toàn – thay vì quản lý trạng thái hội thoại, bạn có thể dựa vào các thread để lưu trữ toàn bộ thông tin cần thiết
- Công cụ có sẵn – Các công cụ giúp tương tác với nguồn dữ liệu của bạn, như Bing, Azure AI Search và Azure Functions.

Các công cụ có sẵn trong Azure AI Agent Service được chia thành hai nhóm:

1. Công cụ Kiến thức:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Ghép nối với Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Tìm kiếm Tệp</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Công cụ Hành động:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Gọi Hàm</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Trình Giải Thích Mã</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Công cụ định nghĩa OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Dịch vụ Agent cho phép chúng ta sử dụng các công cụ này cùng nhau như một `toolset`. Nó cũng sử dụng `threads` để theo dõi lịch sử tin nhắn trong một cuộc trò chuyện cụ thể.

Hãy tưởng tượng bạn là một đại diện bán hàng tại công ty Contoso. Bạn muốn phát triển một tác nhân hội thoại có thể trả lời các câu hỏi về dữ liệu bán hàng của bạn.

Hình ảnh dưới đây minh họa cách bạn có thể sử dụng Azure AI Agent Service để phân tích dữ liệu bán hàng của mình:

![Agentic Service In Action](../../../translated_images/vi/agent-service-in-action.34fb465c9a84659e.webp)

Để sử dụng bất kỳ công cụ nào với dịch vụ, chúng ta có thể tạo client và định nghĩa một công cụ hoặc bộ công cụ. Để thực hiện điều này trong thực tế, ta có thể dùng đoạn mã Python sau. LLM sẽ có thể xem bộ công cụ và quyết định sử dụng hàm do người dùng tạo `fetch_sales_data_using_sqlite_query` hoặc Trình Giải Thích Mã có sẵn tùy theo yêu cầu người dùng.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # hàm fetch_sales_data_using_sqlite_query có thể được tìm thấy trong file fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Khởi tạo bộ dụng cụ công cụ
toolset = ToolSet()

# Khởi tạo đại lý gọi hàm với hàm fetch_sales_data_using_sqlite_query và thêm nó vào bộ dụng cụ công cụ
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Khởi tạo công cụ Code Interpreter và thêm nó vào bộ dụng cụ công cụ.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Những điều cần lưu ý đặc biệt khi dùng Mẫu Thiết Kế Sử Dụng Công Cụ để xây dựng các tác nhân AI đáng tin cậy?

Một mối quan tâm phổ biến với SQL được tạo động bởi LLMs là bảo mật, đặc biệt là rủi ro tiêm SQL hoặc các hành động độc hại, ví dụ như xóa hoặc làm hỏng cơ sở dữ liệu. Mặc dù các mối lo ngại này là hợp lý, chúng có thể được giảm thiểu hiệu quả bằng cách cấu hình quyền truy cập cơ sở dữ liệu phù hợp. Với hầu hết các cơ sở dữ liệu, điều này bao gồm việc cấu hình cơ sở dữ liệu ở chế độ chỉ đọc. Với các dịch vụ cơ sở dữ liệu như PostgreSQL hoặc Azure SQL, ứng dụng nên được gán vai trò chỉ đọc (SELECT).
Chạy ứng dụng trong môi trường an toàn hơn nữa giúp nâng cao khả năng bảo vệ. Trong các kịch bản doanh nghiệp, dữ liệu thường được trích xuất và biến đổi từ các hệ thống vận hành sang cơ sở dữ liệu hoặc kho dữ liệu chỉ đọc với một sơ đồ thân thiện với người dùng. Cách tiếp cận này đảm bảo rằng dữ liệu được bảo mật, tối ưu cho hiệu suất và khả năng truy cập, đồng thời ứng dụng có quyền truy cập giới hạn, chỉ đọc.

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
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->