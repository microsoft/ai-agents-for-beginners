[![Cách Thiết Kế Các Đại Lý AI Tốt](../../../translated_images/vi/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Nhấp vào hình trên để xem video bài học này)_

# Mẫu Thiết Kế Sử Dụng Công Cụ

Công cụ rất thú vị vì chúng cho phép các đại lý AI có phạm vi khả năng rộng hơn. Thay vì đại lý chỉ có một tập hợp các hành động hạn chế có thể thực hiện, bằng cách thêm một công cụ, đại lý giờ đây có thể thực hiện nhiều hành động khác nhau. Trong chương này, chúng ta sẽ xem xét Mẫu Thiết Kế Sử Dụng Công Cụ, mô tả cách các đại lý AI có thể sử dụng các công cụ cụ thể để đạt được mục tiêu của họ.

## Giới thiệu

Trong bài học này, chúng ta sẽ tìm kiếm câu trả lời cho các câu hỏi sau:

- Mẫu thiết kế sử dụng công cụ là gì?
- Những trường hợp sử dụng nào có thể áp dụng được?
- Những yếu tố/khối xây dựng nào cần thiết để triển khai mẫu thiết kế?
- Những lưu ý đặc biệt khi sử dụng Mẫu Thiết Kế Sử Dụng Công Cụ để xây dựng các đại lý AI đáng tin cậy là gì?

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Định nghĩa Mẫu Thiết Kế Sử Dụng Công Cụ và mục đích của nó.
- Xác định các trường hợp sử dụng mà Mẫu Thiết Kế Sử Dụng Công Cụ phù hợp.
- Hiểu các yếu tố chính cần thiết để triển khai mẫu thiết kế.
- Nhận biết những lưu ý để đảm bảo tính đáng tin cậy cho các đại lý AI sử dụng mẫu thiết kế này.

## Mẫu Thiết Kế Sử Dụng Công Cụ là gì?

**Mẫu Thiết Kế Sử Dụng Công Cụ** tập trung vào việc cung cấp cho LLM khả năng tương tác với các công cụ bên ngoài để đạt được các mục tiêu cụ thể. Công cụ là các đoạn mã có thể được đại lý thực thi để thực hiện các hành động. Một công cụ có thể là một hàm đơn giản như máy tính, hoặc một lệnh gọi API đến dịch vụ bên thứ ba như tra cứu giá cổ phiếu hoặc dự báo thời tiết. Trong bối cảnh các đại lý AI, các công cụ được thiết kế để được thực thi bởi đại lý theo phản hồi từ **các lệnh gọi hàm do mô hình tạo ra**.

## Những trường hợp sử dụng mà mẫu thiết kế này có thể áp dụng?

Các đại lý AI có thể tận dụng các công cụ để hoàn thành các nhiệm vụ phức tạp, truy xuất thông tin hoặc đưa ra quyết định. Mẫu thiết kế sử dụng công cụ thường được dùng trong các kịch bản yêu cầu tương tác động với các hệ thống bên ngoài, như cơ sở dữ liệu, dịch vụ web hoặc trình thông dịch mã. Khả năng này hữu ích cho nhiều trường hợp sử dụng khác nhau bao gồm:

- **Truy xuất thông tin động:** Đại lý có thể truy vấn các API hoặc cơ sở dữ liệu bên ngoài để lấy dữ liệu cập nhật mới nhất (ví dụ: truy vấn cơ sở dữ liệu SQLite để phân tích dữ liệu, lấy giá cổ phiếu hoặc thông tin thời tiết).
- **Thực thi và thông dịch mã:** Đại lý có thể chạy mã hoặc script để giải các bài toán toán học, tạo báo cáo hoặc thực hiện mô phỏng.
- **Tự động hóa quy trình làm việc:** Tự động hóa các quy trình lặp đi lặp lại hoặc nhiều bước bằng cách tích hợp các công cụ như bộ lập lịch tác vụ, dịch vụ email, hoặc pipeline dữ liệu.
- **Hỗ trợ khách hàng:** Đại lý có thể tương tác với các hệ thống CRM, nền tảng quản lý vé, hoặc cơ sở tri thức để giải quyết các câu hỏi của người dùng.
- **Tạo và chỉnh sửa nội dung:** Đại lý có thể dùng các công cụ như kiểm tra ngữ pháp, tóm tắt văn bản, hoặc đánh giá an toàn nội dung để hỗ trợ công việc sáng tạo nội dung.

## Những yếu tố/khối xây dựng cần thiết để triển khai mẫu thiết kế sử dụng công cụ?

Những khối xây dựng này cho phép đại lý AI thực hiện nhiều nhiệm vụ khác nhau. Hãy cùng xem các yếu tố chính cần thiết để triển khai Mẫu Thiết Kế Sử Dụng Công Cụ:

- **Mô hình hàm/công cụ:** Định nghĩa chi tiết các công cụ có sẵn, bao gồm tên hàm, mục đích, các tham số yêu cầu và kết quả dự kiến. Các mô hình này giúp LLM hiểu được công cụ nào có sẵn và cách xây dựng các yêu cầu hợp lệ.

- **Logic thực thi hàm:** Quy định cách thức và thời điểm các công cụ được gọi dựa trên ý định người dùng và ngữ cảnh cuộc trò chuyện. Điều này có thể bao gồm các mô-đun lập kế hoạch, cơ chế định tuyến, hoặc các luồng điều kiện xác định việc sử dụng công cụ động.

- **Hệ thống xử lý tin nhắn:** Các thành phần quản lý luồng hội thoại giữa đầu vào người dùng, phản hồi của LLM, các lệnh gọi công cụ và kết quả trả về của công cụ.

- **Khung tích hợp công cụ:** Cơ sở hạ tầng kết nối đại lý với các công cụ khác nhau, dù là các hàm đơn giản hay các dịch vụ bên ngoài phức tạp.

- **Xử lý lỗi & xác thực:** Cơ chế xử lý lỗi khi thực thi công cụ, xác thực tham số, và quản lý các phản hồi bất ngờ.

- **Quản lý trạng thái:** Theo dõi ngữ cảnh hội thoại, các tương tác công cụ trước đó và dữ liệu lưu trữ để đảm bảo nhất quán qua nhiều vòng trao đổi.

Tiếp theo, chúng ta sẽ tìm hiểu chi tiết về Gọi Hàm/Công Cụ.
 
### Gọi Hàm/Công Cụ

Gọi hàm là phương thức chính cho phép Mô hình Ngôn ngữ Lớn (LLM) tương tác với các công cụ. Bạn sẽ thường thấy 'Hàm' và 'Công cụ' được dùng thay thế cho nhau vì 'hàm' (các đoạn mã có thể tái sử dụng) chính là 'công cụ' mà các đại lý sử dụng để thực hiện nhiệm vụ. Để mã của một hàm được gọi, LLM phải so sánh yêu cầu của người dùng với mô tả của hàm. Để làm điều này, một mô hình chứa các mô tả về tất cả các hàm có sẵn sẽ được gửi đến LLM. LLM sau đó chọn hàm phù hợp nhất cho nhiệm vụ và trả về tên cùng các tham số của hàm đó. Hàm được chọn sẽ được gọi, phản hồi của nó được gửi trở lại cho LLM, và LLM sử dụng thông tin này để phản hồi yêu cầu của người dùng.

Để các nhà phát triển triển khai gọi hàm cho đại lý, bạn cần:

1. Một mô hình LLM hỗ trợ gọi hàm
2. Một mô hình chứa các mô tả hàm
3. Mã cho mỗi hàm đã được mô tả

Hãy lấy ví dụ về việc lấy thời gian hiện tại ở một thành phố để minh họa:

1. **Khởi tạo LLM hỗ trợ gọi hàm:**

    Không phải tất cả các mô hình đều hỗ trợ gọi hàm, nên điều quan trọng là phải kiểm tra xem LLM bạn đang dùng có hỗ trợ không. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> hỗ trợ gọi hàm. Chúng ta có thể bắt đầu bằng cách khởi tạo client OpenAI với Azure OpenAI **Responses API** (điểm cuối ổn định `/openai/v1/` — không cần `api_version`).

    ```python
    # Khởi tạo client OpenAI cho Azure OpenAI (API Responses, điểm cuối v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Tạo Mô hình Hàm:**

    Tiếp theo, chúng ta sẽ định nghĩa một mô hình JSON chứa tên hàm, mô tả công việc của hàm, và tên cùng mô tả các tham số của hàm.
    Sau đó chúng ta sẽ lấy mô hình này và truyền cho client đã tạo ở trên, cùng với yêu cầu của người dùng để tìm giờ ở San Francisco. Điều quan trọng cần lưu ý là một **cuộc gọi công cụ** là thứ được trả về, **không phải** câu trả lời cuối cùng cho câu hỏi. Như đã đề cập, LLM trả về tên hàm được chọn thực hiện nhiệm vụ cùng các tham số sẽ truyền vào hàm.

    ```python
    # Mô tả chức năng cho mô hình đọc (định dạng công cụ phẳng API Phản hồi)
    tools = [
        {
            "type": "function",
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
    ]
    ```
   
    ```python
  
    # Tin nhắn người dùng ban đầu
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Lần gọi API đầu tiên: Yêu cầu mô hình sử dụng chức năng
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # API Phản hồi trả về các cuộc gọi công cụ dưới dạng các mục function_call trong response.output.
    # Thêm chúng vào cuộc hội thoại để mô hình có đầy đủ ngữ cảnh trong lượt tiếp theo.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Mã hàm cần thiết để thực hiện nhiệm vụ:**

    Khi LLM đã chọn được hàm cần chạy, mã thực thi nhiệm vụ phải được triển khai và chạy.
    Chúng ta có thể viết mã lấy thời gian hiện tại bằng Python. Chúng ta cũng cần viết mã để trích xuất tên và tham số từ response_message để có kết quả cuối cùng.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Trả về kết quả công cụ dưới dạng một mục function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Cuộc gọi API thứ hai: Lấy phản hồi cuối cùng từ mô hình
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Gọi Hàm là trọng tâm trong hầu hết, nếu không muốn nói là tất cả các mẫu thiết kế sử dụng công cụ của đại lý, tuy nhiên việc triển khai từ đầu đôi khi cũng khá thách thức.
Như chúng ta đã học ở [Bài học 2](../../../02-explore-agentic-frameworks), các khuôn khổ agentic cung cấp sẵn các khối xây dựng giúp triển khai việc sử dụng công cụ.
 
## Ví dụ Sử Dụng Công Cụ với các Khuôn Khổ Agentic

Dưới đây là một số ví dụ cách bạn có thể triển khai Mẫu Thiết Kế Sử Dụng Công Cụ với các khuôn khổ agentic khác nhau:

### Khuôn Khổ Đại Lý Microsoft

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> là một khuôn khổ AI mã nguồn mở để xây dựng các đại lý AI. Nó đơn giản hóa quy trình sử dụng gọi hàm bằng cách cho phép bạn định nghĩa công cụ dưới dạng các hàm Python với decorator `@tool`. Khuôn khổ sẽ xử lý giao tiếp qua lại giữa mô hình và mã của bạn. Nó cũng cung cấp quyền truy cập tới các công cụ có sẵn như Tìm tệp và Trình thông dịch Mã qua `FoundryChatClient`.

Sơ đồ dưới đây minh họa quy trình gọi hàm với Khuôn Khổ Đại Lý Microsoft:

![gọi hàm](../../../translated_images/vi/functioncalling-diagram.a84006fc287f6014.webp)

Trong Khuôn Khổ Đại Lý Microsoft, các công cụ được định nghĩa dưới dạng hàm được trang trí. Chúng ta có thể chuyển hàm `get_current_time` đã xem trước đó thành một công cụ bằng cách dùng decorator `@tool`. Khuôn khổ sẽ tự động tuần tự hóa hàm và các tham số, tạo thành mô hình để gửi tới LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Tạo client
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Tạo một agent và chạy với công cụ
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Dịch Vụ Đại Lý Microsoft Foundry

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> là một khuôn khổ agentic mới hơn, được thiết kế để giúp các nhà phát triển xây dựng, triển khai và mở rộng các đại lý AI chất lượng cao, có khả năng mở rộng, một cách an toàn mà không cần phải quản lý tài nguyên tính toán và lưu trữ bên dưới. Nó đặc biệt hữu ích cho các ứng dụng doanh nghiệp vì là dịch vụ được quản lý hoàn toàn với bảo mật cấp doanh nghiệp.

So với việc phát triển trực tiếp với API LLM, Microsoft Foundry Agent Service cung cấp một số lợi ích như:

- Gọi công cụ tự động – không cần phải phân tích cuộc gọi công cụ, thực thi công cụ và xử lý phản hồi; tất cả được thực hiện phía máy chủ
- Quản lý dữ liệu an toàn – thay vì quản lý trạng thái hội thoại riêng, bạn có thể dựa vào các thread lưu trữ tất cả thông tin cần thiết
- Công cụ dùng ngay – Các công cụ bạn có thể dùng để tương tác với nguồn dữ liệu của mình, như Bing, Azure AI Search và Azure Functions.

Các công cụ có sẵn trong Microsoft Foundry Agent Service được chia thành hai loại:

1. Công Cụ Kiến Thức:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Nền tảng với Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Tìm kiếm tệp</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Tìm kiếm Azure AI</a>

2. Công Cụ Hành Động:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Gọi Hàm</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Trình Thông Dịch Mã</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Công cụ định nghĩa OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Dịch vụ Đại lý cho phép chúng ta sử dụng các công cụ này cùng nhau như một `toolset`. Nó cũng sử dụng `threads` để theo dõi lịch sử tin nhắn của một cuộc trò chuyện cụ thể.

Hãy tưởng tượng bạn là một đại lý bán hàng tại một công ty có tên Contoso. Bạn muốn phát triển một đại lý hội thoại có thể trả lời các câu hỏi về dữ liệu bán hàng của bạn.

Hình ảnh dưới đây minh họa cách bạn có thể sử dụng Microsoft Foundry Agent Service để phân tích dữ liệu bán hàng:

![Dịch vụ Agentic hoạt động](../../../translated_images/vi/agent-service-in-action.34fb465c9a84659e.webp)

Để sử dụng bất kỳ công cụ nào trong số này với dịch vụ, chúng ta có thể tạo một client và định nghĩa công cụ hoặc bộ công cụ. Để triển khai thực tế, chúng ta có thể dùng đoạn mã Python sau. LLM sẽ có thể xem bộ công cụ và quyết định sử dụng hàm do người dùng tạo, `fetch_sales_data_using_sqlite_query`, hoặc Trình Thông Dịch Mã có sẵn tùy thuộc vào yêu cầu của người dùng.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # hàm fetch_sales_data_using_sqlite_query có thể được tìm thấy trong tệp fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Khởi tạo bộ công cụ
toolset = ToolSet()

# Khởi tạo đại lý gọi hàm với hàm fetch_sales_data_using_sqlite_query và thêm nó vào bộ công cụ
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Khởi tạo công cụ Phiên dịch Mã và thêm nó vào bộ công cụ.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Những lưu ý đặc biệt khi sử dụng Mẫu Thiết Kế Sử Dụng Công Cụ để xây dựng các đại lý AI đáng tin cậy?

Một mối quan ngại phổ biến với SQL được sinh động bởi LLM là bảo mật, đặc biệt là rủi ro tiêm nhiễm SQL hoặc hành động ác ý, như xóa hoặc sửa đổi cơ sở dữ liệu. Mặc dù những lo ngại này có cơ sở, chúng có thể được giảm thiểu hiệu quả bằng cách cấu hình quyền truy cập cơ sở dữ liệu phù hợp. Với hầu hết các cơ sở dữ liệu, điều này liên quan đến việc cấu hình cơ sở dữ liệu ở chế độ chỉ đọc. Đối với các dịch vụ cơ sở dữ liệu như PostgreSQL hoặc Azure SQL, ứng dụng nên được gán vai trò chỉ đọc (SELECT).

Chạy ứng dụng trong môi trường an toàn càng làm tăng khả năng bảo vệ. Trong các kịch bản doanh nghiệp, dữ liệu thường được trích xuất và chuyển đổi từ các hệ thống vận hành sang cơ sở dữ liệu chỉ đọc hoặc kho dữ liệu với sơ đồ thân thiện người dùng. Cách tiếp cận này đảm bảo dữ liệu được bảo mật, tối ưu cho hiệu suất và khả năng truy cập, và ứng dụng có quyền truy cập giới hạn, chỉ đọc.

## Mã mẫu

- Python: [Khuôn Khổ Đại Lý](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Khuôn Khổ Đại Lý](./code_samples/04-dotnet-agent-framework.md)

## Có Thêm Câu Hỏi về Mẫu Thiết Kế Sử Dụng Công Cụ?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ các học viên khác, tham dự giờ làm việc và nhận giải đáp các câu hỏi về Đại Lý AI của bạn.

## Tài Nguyên Bổ Sung

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Hội Thảo Dịch Vụ Đại Lý AI Azure</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Hội Thảo Đa Đại Lý Viết Sáng Tạo Contoso</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Tổng Quan Khuôn Khổ Đại Lý Microsoft</a>


## Kiểm Tra Nhanh Tác Nhân Này (Tùy Chọn)

Sau khi bạn học cách triển khai các tác nhân trong [Bài học 16](../16-deploying-scalable-agents/README.md), bạn có thể kiểm tra nhanh `TravelToolAgent` của bài học này (nó có còn gọi công cụ và trả lời không?) với [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Xem [`tests/README.md`](../tests/README.md) để biết cách chạy nó.

## Bài Học Trước

[Hiểu Về Mẫu Thiết Kế Agentic](../03-agentic-design-patterns/README.md)

## Bài Học Tiếp Theo

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->