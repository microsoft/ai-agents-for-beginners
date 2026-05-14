[![Cách Thiết Kế Các Đại Lý AI Tốt](../../../translated_images/vi/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Nhấp vào hình ảnh bên trên để xem video bài học này)_

# Mô Hình Thiết Kế Sử Dụng Công Cụ

Công cụ rất thú vị vì chúng cho phép các đại lý AI có phạm vi khả năng rộng hơn. Thay vì đại lý chỉ có một bộ hành động giới hạn, bằng cách thêm một công cụ, đại lý bây giờ có thể thực hiện nhiều loại hành động khác nhau. Trong chương này, chúng ta sẽ xem xét Mô Hình Thiết Kế Sử Dụng Công Cụ, mô tả cách các đại lý AI có thể sử dụng các công cụ cụ thể để đạt được mục tiêu của họ.

## Giới thiệu

Trong bài học này, chúng ta sẽ đi tìm câu trả lời cho các câu hỏi sau:

- Mô hình thiết kế sử dụng công cụ là gì?
- Nó có thể áp dụng cho những trường hợp sử dụng nào?
- Các thành phần/khối xây dựng cần thiết để triển khai mô hình thiết kế là gì?
- Những cân nhắc đặc biệt nào khi sử dụng Mô Hình Thiết Kế Sử Dụng Công Cụ để xây dựng các đại lý AI đáng tin cậy?

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Định nghĩa Mô Hình Thiết Kế Sử Dụng Công Cụ và mục đích của nó.
- Xác định các trường hợp sử dụng phù hợp với Mô Hình Thiết Kế Sử Dụng Công Cụ.
- Hiểu các thành phần chính cần thiết để triển khai mô hình thiết kế.
- Nhận biết các cân nhắc để đảm bảo sự đáng tin cậy trong các đại lý AI sử dụng mô hình thiết kế này.

## Mô hình thiết kế sử dụng công cụ là gì?

**Mô Hình Thiết Kế Sử Dụng Công Cụ** tập trung vào việc cung cấp cho LLM khả năng tương tác với các công cụ bên ngoài để đạt được các mục tiêu cụ thể. Công cụ là mã có thể được thực thi bởi đại lý để thực hiện các hành động. Một công cụ có thể là một hàm đơn giản như máy tính, hoặc một gọi API tới dịch vụ bên thứ ba như tra cứu giá cổ phiếu hoặc dự báo thời tiết. Trong bối cảnh đại lý AI, các công cụ được thiết kế để được thực thi bởi đại lý nhằm phản hồi các **gọi hàm do mô hình tạo ra**.

## Các trường hợp sử dụng có thể áp dụng là gì?

Các đại lý AI có thể tận dụng công cụ để hoàn thành các tác vụ phức tạp, lấy thông tin hoặc đưa ra quyết định. Mô hình thiết kế sử dụng công cụ thường được sử dụng trong các tình huống đòi hỏi tương tác động với các hệ thống bên ngoài, chẳng hạn như cơ sở dữ liệu, dịch vụ web hoặc trình thông dịch mã. Khả năng này hữu ích cho một số trường hợp sử dụng khác nhau bao gồm:

- **Truy xuất thông tin động:** Đại lý có thể truy vấn API bên ngoài hoặc cơ sở dữ liệu để lấy dữ liệu cập nhật (ví dụ: truy vấn cơ sở dữ liệu SQLite để phân tích dữ liệu, lấy giá cổ phiếu hoặc thông tin thời tiết).
- **Thực thi và thông dịch mã:** Đại lý có thể thực thi mã hoặc tập lệnh để giải các bài toán toán học, tạo báo cáo hoặc thực hiện mô phỏng.
- **Tự động hóa quy trình làm việc:** Tự động hóa các quy trình nhiều bước hoặc lặp lại bằng cách tích hợp các công cụ như bộ lập lịch tác vụ, dịch vụ email hoặc pipeline dữ liệu.
- **Hỗ trợ khách hàng:** Đại lý có thể tương tác với hệ thống CRM, nền tảng quản lý vé hoặc cơ sở kiến thức để giải quyết các câu hỏi của người dùng.
- **Tạo và chỉnh sửa nội dung:** Đại lý có thể sử dụng các công cụ như kiểm tra ngữ pháp, tóm tắt văn bản hoặc đánh giá an toàn nội dung để hỗ trợ các nhiệm vụ tạo nội dung.

## Các thành phần/khối xây dựng cần thiết để triển khai mô hình thiết kế sử dụng công cụ là gì?

Các khối xây dựng này cho phép đại lý AI thực hiện nhiều loại nhiệm vụ khác nhau. Hãy xem xét các thành phần chính cần thiết để triển khai Mô Hình Thiết Kế Sử Dụng Công Cụ:

- **Lược đồ Hàm/Công cụ**: Định nghĩa chi tiết các công cụ sẵn có, bao gồm tên hàm, mục đích, tham số bắt buộc và đầu ra dự kiến. Các lược đồ này cho phép LLM hiểu các công cụ nào có thể sử dụng và cách tạo yêu cầu hợp lệ.

- **Logic Thực thi Hàm**: Quy định cách và thời điểm các công cụ được gọi dựa trên ý định người dùng và ngữ cảnh cuộc hội thoại. Điều này có thể bao gồm các module lập kế hoạch, cơ chế định tuyến hoặc luồng điều kiện quyết định việc sử dụng công cụ một cách linh hoạt.

- **Hệ thống Xử lý Tin nhắn**: Các thành phần quản lý luồng hội thoại giữa đầu vào của người dùng, phản hồi từ LLM, gọi công cụ và kết quả công cụ.

- **Khung Tích hợp Công cụ**: Hạ tầng kết nối đại lý với các công cụ khác nhau, dù là các hàm đơn giản hay dịch vụ bên ngoài phức tạp.

- **Xử lý Lỗi & Xác thực**: Cơ chế quản lý lỗi trong quá trình thực thi công cụ, xác thực tham số và xử lý các phản hồi ngoài dự kiến.

- **Quản lý Trạng thái**: Theo dõi ngữ cảnh cuộc hội thoại, tương tác công cụ trước đó và dữ liệu bền vững để đảm bảo tính nhất quán trong các tương tác đa lượt.

Tiếp theo, chúng ta sẽ tìm hiểu chi tiết về Gọi Hàm/Công cụ.
 
### Gọi Hàm/Công Cụ

Gọi hàm là cách chính giúp các Mô Hình Ngôn Ngữ Lớn (LLMs) tương tác với công cụ. Bạn thường thấy thuật ngữ 'Hàm' và 'Công cụ' được sử dụng thay thế cho nhau vì 'hàm' (khối mã có thể tái sử dụng) chính là những 'công cụ' mà đại lý dùng để thực hiện tác vụ. Để mã của một hàm được gọi thực thi, LLM phải so sánh yêu cầu của người dùng với mô tả của hàm đó. Để làm điều này, một lược đồ chứa mô tả của tất cả các hàm có sẵn được gửi đến LLM. LLM sau đó chọn hàm phù hợp nhất cho nhiệm vụ và trả về tên hàm cùng các tham số. Hàm được chọn sẽ được gọi thực thi, phản hồi được gửi lại cho LLM, từ đó LLM sử dụng thông tin này để trả lời yêu cầu của người dùng.

Để các nhà phát triển triển khai gọi hàm cho đại lý, bạn sẽ cần:

1. Một mô hình LLM hỗ trợ gọi hàm
2. Một lược đồ chứa mô tả hàm
3. Mã nguồn cho từng hàm được mô tả

Hãy sử dụng ví dụ lấy giờ hiện tại trong một thành phố để minh họa:

1. **Khởi tạo một LLM hỗ trợ gọi hàm:**

    Không phải tất cả các mô hình đều hỗ trợ gọi hàm, vì vậy bạn cần kiểm tra xem LLM bạn dùng có không. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> hỗ trợ gọi hàm. Chúng ta có thể bắt đầu bằng cách khởi tạo client Azure OpenAI. 

    ```python
    # Khởi tạo client Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Tạo Lược đồ Hàm**:

    Tiếp theo chúng ta sẽ định nghĩa một lược đồ JSON chứa tên hàm, mô tả chức năng của hàm, cùng tên và mô tả các tham số của hàm.
    Sau đó, chúng ta sẽ gửi lược đồ này đến client đã tạo ở bước trước, cùng với yêu cầu của người dùng để tìm giờ tại San Francisco. Điều quan trọng cần lưu ý là một **cuộc gọi công cụ** là kết quả trả về, **không phải** câu trả lời cuối cùng cho câu hỏi. Như đã nói, LLM trả về tên hàm đã chọn cho nhiệm vụ và các tham số sẽ được truyền vào.

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
  
1. **Mã hàm để thực hiện nhiệm vụ:**

    Khi LLM đã chọn hàm cần chạy, mã thực hiện nhiệm vụ cần được triển khai và chạy.
    Chúng ta có thể viết mã trong Python để lấy giờ hiện tại. Cũng cần viết mã để trích xuất tên hàm và tham số từ response_message để nhận kết quả cuối cùng.

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

Gọi Hàm là trung tâm của hầu hết, nếu không muốn nói là tất cả, các thiết kế sử dụng công cụ đại lý, tuy nhiên việc triển khai từ đầu đôi khi có thể là thách thức.
Như chúng ta đã học trong [Bài học 2](../../../02-explore-agentic-frameworks) các khung agentic cung cấp các khối xây dựng sẵn để triển khai việc sử dụng công cụ.
 
## Ví dụ Sử Dụng Công Cụ với Các Khung Agentic

Dưới đây là một số ví dụ về cách triển khai Mô Hình Thiết Kế Sử Dụng Công Cụ bằng các khung agentic khác nhau:

### Khung Đại Lý Microsoft

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Khung Đại Lý Microsoft</a> là một khung AI mã nguồn mở để xây dựng các đại lý AI. Nó đơn giản hóa quá trình gọi hàm bằng cách cho phép bạn định nghĩa công cụ dưới dạng các hàm Python với decorator `@tool`. Khung này xử lý giao tiếp qua lại giữa mô hình và mã của bạn. Nó cũng cung cấp truy cập tới các công cụ dựng sẵn như Tìm tập tin và Trình thông dịch Mã qua `AzureAIProjectAgentProvider`.

Sơ đồ sau minh họa quá trình gọi hàm với Khung Đại Lý Microsoft:

![function calling](../../../translated_images/vi/functioncalling-diagram.a84006fc287f6014.webp)

Trong Khung Đại Lý Microsoft, công cụ được định nghĩa là các hàm được trang trí. Chúng ta có thể chuyển hàm `get_current_time` đã thấy trước đó thành một công cụ bằng cách sử dụng decorator `@tool`. Khung tự động tuần tự hóa hàm và các tham số của nó, tạo lược đồ gửi tới LLM.

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
  
### Dịch Vụ Đại Lý Azure AI

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dịch Vụ Đại Lý Azure AI</a> là một khung agentic mới hơn được thiết kế nhằm giúp các nhà phát triển xây dựng, triển khai và mở rộng quy mô đại lý AI chất lượng cao một cách bảo mật mà không cần quản lý tài nguyên tính toán và lưu trữ bên dưới. Nó đặc biệt hữu ích cho các ứng dụng doanh nghiệp vì là dịch vụ được quản lý hoàn toàn với bảo mật cấp doanh nghiệp.

So với phát triển trực tiếp với API LLM, Dịch Vụ Đại Lý Azure AI cung cấp một số lợi ích, bao gồm:

- Gọi công cụ tự động – không cần phải phân tích cuộc gọi công cụ, gọi công cụ và xử lý phản hồi; tất cả việc này giờ được thực hiện phía máy chủ
- Quản lý dữ liệu một cách bảo mật – thay vì quản lý trạng thái cuộc trò chuyện, bạn có thể dựa vào các `threads` để lưu trữ tất cả thông tin cần thiết
- Công cụ có sẵn ngay – Các công cụ dùng để tương tác với nguồn dữ liệu của bạn như Bing, Azure AI Search và Azure Functions.

Các công cụ có trong Dịch Vụ Đại Lý Azure AI được chia thành hai loại:

1. Công cụ Kiến thức:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Tạo nền tảng với Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Tìm tập tin</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Công cụ Hành động:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Gọi Hàm</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Trình thông dịch Mã</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Công cụ định nghĩa OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Dịch vụ Đại Lý cho phép chúng ta sử dụng các công cụ này cùng nhau như một `toolset`. Nó cũng sử dụng `threads` để theo dõi lịch sử tin nhắn trong một cuộc hội thoại cụ thể.

Hãy tưởng tượng bạn là đại lý bán hàng tại một công ty có tên Contoso. Bạn muốn phát triển một đại lý đàm thoại có thể trả lời các câu hỏi về dữ liệu bán hàng của mình.

Hình ảnh dưới đây minh họa cách bạn có thể dùng Dịch Vụ Đại Lý Azure AI để phân tích dữ liệu bán hàng:

![Agentic Service In Action](../../../translated_images/vi/agent-service-in-action.34fb465c9a84659e.webp)

Để sử dụng bất kỳ công cụ nào với dịch vụ, chúng ta có thể tạo một client và định nghĩa một công cụ hoặc bộ công cụ. Để triển khai thực tế, ta dùng đoạn mã Python sau. LLM sẽ xem xét toolset và quyết định sử dụng hàm do người dùng tạo `fetch_sales_data_using_sqlite_query` hay Trình thông dịch Mã dựng sẵn, tùy yêu cầu người dùng.

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

# Khởi tạo công cụ Trình thông dịch Mã và thêm nó vào bộ công cụ.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Những cân nhắc đặc biệt khi sử dụng Mô Hình Thiết Kế Sử Dụng Công Cụ để xây dựng đại lý AI đáng tin cậy?

Một mối quan tâm phổ biến với SQL được sinh động bởi LLM là bảo mật, đặc biệt là rủi ro tiêm lệnh SQL hoặc các hành động độc hại, như xóa hoặc can thiệp vào cơ sở dữ liệu. Mặc dù những lo ngại này có cơ sở, nhưng chúng có thể được giảm thiểu hiệu quả bằng cách cấu hình đúng quyền truy cập cơ sở dữ liệu. Với hầu hết các cơ sở dữ liệu, điều này bao gồm việc cấu hình cơ sở dữ liệu ở chế độ chỉ đọc. Với các dịch vụ cơ sở dữ liệu như PostgreSQL hoặc Azure SQL, ứng dụng cần được gán vai trò chỉ đọc (SELECT).

Việc chạy ứng dụng trong môi trường bảo mật càng tăng cường bảo vệ. Trong các kịch bản doanh nghiệp, dữ liệu thường được trích xuất và chuyển đổi từ các hệ thống vận hành thành cơ sở dữ liệu hoặc kho dữ liệu chỉ đọc với lược đồ thân thiện với người dùng. Cách tiếp cận này đảm bảo dữ liệu an toàn, tối ưu hiệu suất và khả năng truy cập, đồng thời ứng dụng có quyền truy cập giới hạn, chỉ đọc.

## Mẫu Mã

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Còn thắc mắc về Mô Hình Thiết Kế Sử Dụng Công Cụ?

Tham gia [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ những người học khác, tham gia giờ giải đáp và nhận câu trả lời cho các câu hỏi về Đại Lý AI.

## Tài nguyên bổ sung

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Hội thảo Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Hội thảo Đa Đại Lý Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Tổng quan Khung Đại Lý Microsoft</a>

## Bài học trước

[Hiểu về Các Mô Hình Thiết Kế Agentic](../03-agentic-design-patterns/README.md)

## Bài học tiếp theo
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->