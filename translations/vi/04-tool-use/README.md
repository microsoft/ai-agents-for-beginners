[![Cách thiết kế các tác nhân AI tốt](../../../translated_images/vi/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Nhấn vào hình ảnh trên để xem video bài học này)_

# Mô hình thiết kế Sử dụng Công cụ

Công cụ rất thú vị vì chúng cho phép các tác nhân AI có phạm vi khả năng rộng hơn. Thay vì tác nhân chỉ có một tập các hành động hạn chế có thể thực hiện, bằng cách thêm một công cụ, tác nhân giờ đây có thể thực hiện nhiều hành động đa dạng hơn. Trong chương này, chúng ta sẽ xem xét Mô hình thiết kế Sử dụng Công cụ, mô tả cách các tác nhân AI có thể sử dụng các công cụ cụ thể để đạt được mục tiêu của mình.

## Giới thiệu

Trong bài học này, chúng ta sẽ tìm câu trả lời cho các câu hỏi sau:

- Mô hình thiết kế sử dụng công cụ là gì?
- Những trường hợp sử dụng nào có thể áp dụng mô hình này?
- Những yếu tố/khối xây dựng nào cần thiết để triển khai mô hình thiết kế này?
- Những cân nhắc đặc biệt nào khi sử dụng Mô hình thiết kế Sử dụng Công cụ để xây dựng các tác nhân AI đáng tin cậy?

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Định nghĩa Mô hình thiết kế Sử dụng Công cụ và mục đích của nó.
- Xác định các trường hợp sử dụng phù hợp với Mô hình thiết kế Sử dụng Công cụ.
- Hiểu các yếu tố chính cần thiết để triển khai mô hình thiết kế này.
- Nhận biết các cân nhắc đảm bảo độ tin cậy cho các tác nhân AI sử dụng mô hình thiết kế này.

## Mô hình thiết kế Sử dụng Công cụ là gì?

**Mô hình thiết kế Sử dụng Công cụ** tập trung vào việc cung cấp cho LLM khả năng tương tác với các công cụ bên ngoài để đạt được các mục tiêu cụ thể. Công cụ là mã có thể được tác nhân thực thi để thực hiện hành động. Một công cụ có thể là một hàm đơn giản như máy tính, hoặc một cuộc gọi API đến dịch vụ bên thứ ba như tra cứu giá cổ phiếu hoặc dự báo thời tiết. Trong bối cảnh các tác nhân AI, các công cụ được thiết kế để được tác nhân thực thi dựa trên các **cuộc gọi hàm được mô hình tạo ra**.

## Những trường hợp sử dụng nào có thể áp dụng?

Các tác nhân AI có thể tận dụng công cụ để hoàn thành các nhiệm vụ phức tạp, truy xuất thông tin hoặc đưa ra quyết định. Mô hình thiết kế sử dụng công cụ thường được sử dụng trong các kịch bản yêu cầu tương tác động với các hệ thống bên ngoài, như cơ sở dữ liệu, dịch vụ web, hoặc trình thông dịch mã. Khả năng này hữu ích cho nhiều trường hợp sử dụng khác nhau bao gồm:

- **Truy xuất Thông tin Động:** Tác nhân có thể truy vấn các API bên ngoài hoặc cơ sở dữ liệu để lấy dữ liệu cập nhật (ví dụ: truy vấn cơ sở dữ liệu SQLite để phân tích dữ liệu, lấy giá cổ phiếu hoặc thông tin thời tiết).
- **Thực thi và Giải thích Mã:** Tác nhân có thể thực thi mã hoặc script để giải các bài toán toán học, tạo báo cáo, hoặc thực hiện mô phỏng.
- **Tự động hóa Quy trình Làm việc:** Tự động hóa các quy trình lặp đi lặp lại hoặc đa bước bằng cách tích hợp các công cụ như trình lập lịch tác vụ, dịch vụ email, hoặc pipeline dữ liệu.
- **Hỗ trợ Khách hàng:** Tác nhân có thể tương tác với hệ thống CRM, nền tảng vé hỗ trợ, hoặc cơ sở kiến thức để giải đáp thắc mắc của người dùng.
- **Tạo và Chỉnh sửa Nội dung:** Tác nhân có thể sử dụng các công cụ như trình kiểm tra ngữ pháp, tóm tắt văn bản, hoặc trình đánh giá an toàn nội dung để hỗ trợ công việc tạo nội dung.

## Những yếu tố/khối xây dựng cần thiết để triển khai mô hình thiết kế sử dụng công cụ?

Các khối xây dựng này cho phép tác nhân AI thực hiện nhiều nhiệm vụ đa dạng. Hãy cùng xem các yếu tố chính cần thiết để triển khai Mô hình thiết kế Sử dụng Công cụ:

- **Lược đồ Hàm/Công cụ**: Định nghĩa chi tiết về các công cụ sẵn có, bao gồm tên hàm, mục đích, thông số cần thiết, và kết quả dự kiến. Các lược đồ này giúp LLM hiểu những công cụ nào có sẵn và cách xây dựng các yêu cầu hợp lệ.

- **Logic Thực thi Hàm**: Quy định cách và thời điểm các công cụ được gọi dựa trên ý định của người dùng và ngữ cảnh cuộc hội thoại. Điều này có thể bao gồm các module lập kế hoạch, cơ chế định tuyến, hoặc luồng điều kiện xác định việc sử dụng công cụ một cách động.

- **Hệ thống Xử lý Tin nhắn**: Các thành phần quản lý luồng hội thoại giữa đầu vào người dùng, phản hồi của LLM, các cuộc gọi công cụ và kết quả trả về từ công cụ.

- **Khung Tích hợp Công cụ**: Cơ sở hạ tầng kết nối tác nhân với các công cụ khác nhau, dù đó là các hàm đơn giản hay dịch vụ phức tạp bên ngoài.

- **Xử lý Lỗi & Xác thực**: Các cơ chế xử lý lỗi khi thực thi công cụ, xác thực tham số, và quản lý các phản hồi không mong đợi.

- **Quản lý Trạng thái**: Theo dõi ngữ cảnh cuộc hội thoại, các tương tác trước đó với công cụ, và dữ liệu tồn tại để đảm bảo tính nhất quán trong các tương tác đa lượt.

Tiếp theo, hãy xem xét chi tiết về Cuộc gọi Hàm/Công cụ.

### Cuộc gọi Hàm/Công cụ

Cuộc gọi hàm là cách chính để chúng ta cho phép các Mô hình Ngôn ngữ Lớn (LLM) tương tác với các công cụ. Bạn thường thấy 'Hàm' và 'Công cụ' được dùng thay thế cho nhau vì 'hàm' (đoạn mã có thể tái sử dụng) chính là 'công cụ' mà các tác nhân sử dụng để thực hiện nhiệm vụ. Để mã hàm được gọi, LLM phải so sánh yêu cầu của người dùng với mô tả của các hàm. Để thực hiện điều này, một lược đồ chứa mô tả tất cả các hàm sẵn có được gửi đến LLM. LLM sau đó chọn hàm phù hợp nhất cho nhiệm vụ và trả về tên hàm cùng các đối số. Hàm được chọn sẽ được gọi, phản hồi của nó được gửi trả lại cho LLM, LLM sử dụng thông tin này để phản hồi yêu cầu của người dùng.

Để các nhà phát triển triển khai cuộc gọi hàm cho các tác nhân, bạn sẽ cần:

1. Một mô hình LLM hỗ trợ cuộc gọi hàm
2. Một lược đồ chứa mô tả các hàm
3. Mã cho từng hàm được mô tả

Hãy dùng ví dụ lấy thời gian hiện tại ở một thành phố để minh họa:

1. **Khởi tạo một LLM hỗ trợ cuộc gọi hàm:**

    Không phải tất cả các mô hình đều hỗ trợ cuộc gọi hàm, vì vậy cần kiểm tra LLM bạn đang dùng có hỗ trợ không. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> hỗ trợ cuộc gọi hàm. Chúng ta có thể bắt đầu bằng cách khởi tạo client Azure OpenAI.

    ```python
    # Khởi tạo client Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Tạo lược đồ Hàm**:

    Tiếp theo, chúng ta định nghĩa một lược đồ JSON chứa tên hàm, mô tả chức năng của hàm, và tên cũng như mô tả các tham số.
    Sau đó chúng ta đưa lược đồ này cùng yêu cầu của người dùng về việc tìm thời gian ở San Francisco cho client đã tạo trước đó. Điều quan trọng cần lưu ý là một **cuộc gọi công cụ** được trả về, **không phải** câu trả lời cuối cùng cho câu hỏi. Như đã đề cập trước đó, LLM trả về tên hàm mà nó chọn cho nhiệm vụ, cùng các đối số sẽ được truyền cho hàm.

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
  
    # Tin nhắn ban đầu của người dùng
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Cuộc gọi API đầu tiên: Yêu cầu mô hình sử dụng chức năng
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
  
1. **Mã hàm cần thiết để thực hiện nhiệm vụ:**

    Khi LLM đã chọn được hàm cần chạy, mã thực hiện nhiệm vụ cần được triển khai và chạy.
    Chúng ta có thể hiện thực đoạn mã lấy thời gian hiện tại bằng Python. Đồng thời cần viết mã để trích xuất tên và đối số từ response_message để lấy kết quả cuối cùng.

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

Cuộc gọi Hàm là trung tâm của hầu hết, nếu không nói là tất cả các thiết kế sử dụng công cụ cho tác nhân, tuy nhiên việc triển khai từ đầu đôi khi có thể khá thách thức.
Như đã học trong [Bài học 2](../../../02-explore-agentic-frameworks), các framework tác nhân (agentic) cung cấp cho chúng ta các khối xây dựng đã được dựng sẵn để triển khai sử dụng công cụ.

## Ví dụ Sử dụng Công cụ với Framework Tác nhân

Dưới đây là một số ví dụ về cách bạn có thể triển khai Mô hình thiết kế Sử dụng Công cụ dùng các framework tác nhân khác nhau:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> là một framework AI mã nguồn mở để xây dựng các tác nhân AI. Nó đơn giản hóa quá trình sử dụng cuộc gọi hàm bằng cách cho phép bạn định nghĩa công cụ dưới dạng các hàm Python với decorator `@tool`. Framework xử lý giao tiếp hai chiều giữa mô hình và mã của bạn. Nó cũng cung cấp quyền truy cập các công cụ dựng sẵn như Tìm kiếm Tệp và Trình thông dịch Mã thông qua `AzureAIProjectAgentProvider`.

Sơ đồ dưới đây mô tả quy trình cuộc gọi hàm với Microsoft Agent Framework:

![function calling](../../../translated_images/vi/functioncalling-diagram.a84006fc287f6014.webp)

Trong Microsoft Agent Framework, công cụ được định nghĩa là các hàm được trang trí. Chúng ta có thể chuyển hàm `get_current_time` đã thấy trước đó thành một công cụ bằng cách sử dụng decorator `@tool`. Framework tự động tuần tự hóa hàm cùng các tham số, tạo lược đồ gửi đến LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Tạo client
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Tạo một agent và chạy với công cụ
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> là một framework tác nhân mới hơn, được thiết kế để giúp các nhà phát triển xây dựng, triển khai và mở rộng các tác nhân AI chất lượng cao, mở rộng được và an toàn mà không cần quản lý tài nguyên tính toán và lưu trữ cơ bản. Nền tảng này đặc biệt hữu ích cho ứng dụng doanh nghiệp vì là dịch vụ quản lý đầy đủ với bảo mật cấp doanh nghiệp.

So với việc phát triển trực tiếp với API LLM, Azure AI Agent Service có một số lợi thế, bao gồm:

- Cuộc gọi công cụ tự động – không cần phải phân tích cuộc gọi công cụ, gọi công cụ, và xử lý phản hồi; tất cả việc này giờ được thực hiện phía máy chủ
- Dữ liệu được quản lý an toàn – thay vì tự quản lý trạng thái cuộc hội thoại, bạn có thể dựa vào threads để lưu trữ tất cả thông tin cần thiết
- Công cụ có sẵn ngay – Các công cụ bạn có thể dùng để tương tác với nguồn dữ liệu của bạn, như Bing, Azure AI Search, và Azure Functions.

Các công cụ có trong Azure AI Agent Service được chia thành hai loại:

1. Công cụ Kiến thức:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding với Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Tìm kiếm Tệp</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Công cụ Hành động:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Cuộc gọi Hàm</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Trình Thông dịch Mã</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Công cụ định nghĩa OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Dịch vụ Tác nhân cho phép chúng ta có thể sử dụng các công cụ này cùng nhau như một `bộ công cụ` (toolset). Nó cũng sử dụng `threads` để theo dõi lịch sử tin nhắn cho từng cuộc hội thoại cụ thể.

Hãy tưởng tượng bạn là một nhân viên bán hàng tại công ty Contoso. Bạn muốn phát triển một tác nhân hội thoại có thể trả lời các câu hỏi về dữ liệu bán hàng của bạn.

Hình ảnh dưới đây mô tả cách bạn có thể sử dụng Azure AI Agent Service để phân tích dữ liệu bán hàng của bạn:

![Agentic Service In Action](../../../translated_images/vi/agent-service-in-action.34fb465c9a84659e.webp)

Để sử dụng bất kỳ công cụ nào với dịch vụ, ta có thể tạo client và định nghĩa một công cụ hoặc bộ công cụ. Để triển khai thực tế, ta có thể dùng đoạn mã Python dưới đây. LLM sẽ có thể xem xét bộ công cụ và quyết định sử dụng hàm do người dùng tạo, `fetch_sales_data_using_sqlite_query`, hoặc Trình Thông dịch Mã dựng sẵn tùy theo yêu cầu người dùng.

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

# Khởi tạo bộ công cụ
toolset = ToolSet()

# Khởi tạo tác nhân gọi hàm với hàm fetch_sales_data_using_sqlite_query và thêm nó vào bộ công cụ
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Khởi tạo công cụ Code Interpreter và thêm nó vào bộ công cụ.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Những cân nhắc đặc biệt khi sử dụng Mô hình thiết kế Sử dụng Công cụ để xây dựng các tác nhân AI đáng tin cậy?

Một mối quan ngại phổ biến với SQL được tạo động bởi LLM là vấn đề an ninh, đặc biệt là nguy cơ tấn công chèn SQL hoặc các hành động độc hại, như xóa hoặc sửa đổi cơ sở dữ liệu. Mặc dù những lo ngại này là hợp lệ, chúng có thể được giảm thiểu hiệu quả bằng cách cấu hình quyền truy cập cơ sở dữ liệu đúng cách. Đối với hầu hết cơ sở dữ liệu, việc này bao gồm cấu hình cơ sở dữ liệu ở chế độ chỉ đọc. Đối với các dịch vụ cơ sở dữ liệu như PostgreSQL hoặc Azure SQL, ứng dụng nên được gán vai trò chỉ đọc (SELECT).

Chạy ứng dụng trong môi trường an toàn còn tăng cường bảo vệ. Trong các kịch bản doanh nghiệp, dữ liệu thường được trích xuất và chuyển đổi từ các hệ thống vận hành sang cơ sở dữ liệu hoặc kho dữ liệu chỉ đọc với lược đồ thân thiện người dùng. Cách tiếp cận này đảm bảo dữ liệu an toàn, tối ưu về hiệu năng và tính khả dụng, đồng thời ứng dụng chỉ có quyền truy cập giới hạn, chỉ đọc.

## Mã ví dụ

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Còn thắc mắc về Mô hình thiết kế Sử dụng Công cụ?

Tham gia [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ các người học khác, tham dự giờ làm việc và nhận giải đáp các câu hỏi về Tác nhân AI.

## Tài nguyên bổ sung

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Hội thảo Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Hội thảo Đa tác nhân Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Tổng quan Microsoft Agent Framework</a>

## Bài học trước

[Hiểu các Mô hình thiết kế Agentic](../03-agentic-design-patterns/README.md)

## Bài học tiếp theo
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi nỗ lực để đạt được độ chính xác cao, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ ban đầu nên được xem là nguồn tham khảo có thẩm quyền. Đối với những thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bằng con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->