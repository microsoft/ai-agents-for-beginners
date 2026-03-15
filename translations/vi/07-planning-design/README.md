[![Planning Design Pattern](../../../translated_images/vi/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Nhấp vào hình trên để xem video bài học này)_

# Thiết Kế Lập Kế Hoạch

## Giới thiệu

Bài học này sẽ bao gồm

* Xác định mục tiêu tổng thể rõ ràng và chia nhỏ một nhiệm vụ phức tạp thành các nhiệm vụ dễ quản lý.
* Tận dụng đầu ra có cấu trúc để có các phản hồi đáng tin cậy hơn và dễ đọc bởi máy.
* Áp dụng phương pháp tiếp cận dựa trên sự kiện để xử lý các nhiệm vụ động và các đầu vào bất ngờ.

## Mục Tiêu Học Tập

Sau khi hoàn thành bài học này, bạn sẽ hiểu về:

* Xác định và thiết lập mục tiêu tổng thể cho một tác nhân AI, đảm bảo nó rõ ràng biết cần đạt được điều gì.
* Phân tách một nhiệm vụ phức tạp thành các nhiệm vụ nhỏ hơn và tổ chức chúng theo trình tự hợp lý.
* Trang bị cho các tác nhân các công cụ phù hợp (ví dụ: công cụ tìm kiếm hoặc công cụ phân tích dữ liệu), quyết định khi nào và cách sử dụng chúng, đồng thời xử lý các tình huống bất ngờ phát sinh.
* Đánh giá kết quả của các nhiệm vụ phụ, đo lường hiệu suất và lặp lại các hành động để cải thiện đầu ra cuối cùng.

## Xác Định Mục Tiêu Tổng Thể và Phân Chia Nhiệm Vụ

![Defining Goals and Tasks](../../../translated_images/vi/defining-goals-tasks.d70439e19e37c47a.webp)

Hầu hết các nhiệm vụ trong thế giới thực đều quá phức tạp để xử lý trong một bước duy nhất. Một tác nhân AI cần một mục tiêu súc tích để hướng dẫn việc lập kế hoạch và hành động của nó. Ví dụ, hãy xem xét mục tiêu:

    "Tạo một lịch trình du lịch 3 ngày."

Mặc dù nó đơn giản để phát biểu, nhưng vẫn cần được tinh chỉnh. Mục tiêu càng rõ ràng, tác nhân (và bất kỳ cộng tác viên con người nào) càng có thể tập trung đạt được kết quả đúng đắn, chẳng hạn như tạo một lịch trình đầy đủ với các lựa chọn chuyến bay, đề xuất khách sạn và các hoạt động gợi ý.

### Phân Tách Nhiệm Vụ

Các nhiệm vụ lớn hoặc phức tạp trở nên dễ quản lý hơn khi được chia thành các nhiệm vụ nhỏ hơn, có mục tiêu rõ ràng.
Đối với ví dụ về lịch trình du lịch, bạn có thể phân chia mục tiêu thành:

* Đặt vé máy bay
* Đặt khách sạn
* Thuê xe
* Cá nhân hóa

Mỗi nhiệm vụ phụ sau đó có thể được xử lý bởi các tác nhân hoặc quy trình chuyên biệt. Một tác nhân có thể chuyên về tìm kiếm các ưu đãi chuyến bay tốt nhất, một tác nhân khác tập trung vào đặt khách sạn, v.v. Một tác nhân điều phối hoặc "tác nhân hạ nguồn" có thể tổng hợp các kết quả này thành một lịch trình liền mạch cho người dùng cuối.

Cách tiếp cận mô-đun này cũng cho phép nâng cấp dần dần. Ví dụ, bạn có thể thêm các tác nhân chuyên biệt cho Đề xuất Ẩm thực hoặc Gợi ý Hoạt động Địa phương và tinh chỉnh lịch trình theo thời gian.

### Đầu ra có cấu trúc

Các Mô Hình Ngôn Ngữ Lớn (LLM) có thể tạo ra đầu ra có cấu trúc (ví dụ: JSON) mà các tác nhân hoặc dịch vụ hạ nguồn có thể dễ dàng phân tích và xử lý. Điều này đặc biệt hữu ích trong bối cảnh đa tác nhân, nơi chúng ta có thể thực thi các nhiệm vụ này sau khi nhận được kết quả lập kế hoạch.

Đoạn mã Python dưới đây minh họa một tác nhân lập kế hoạch đơn giản phân tách mục tiêu thành các nhiệm vụ phụ và tạo ra một kế hoạch có cấu trúc:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Mô hình nhiệm vụ phụ du lịch
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # chúng tôi muốn phân công nhiệm vụ cho đại lý

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Định nghĩa tin nhắn người dùng
system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text
pprint(json.loads(response_content))
```

### Tác nhân Lập kế hoạch với Điều phối Đa tác nhân

Trong ví dụ này, một Tác nhân Bộ Điều Hướng Ngữ nghĩa nhận một yêu cầu từ người dùng (ví dụ, "Tôi cần một kế hoạch khách sạn cho chuyến đi của tôi.").

Người lập kế hoạch sau đó sẽ:

* Nhận Kế hoạch Khách sạn: Người lập kế hoạch lấy tin nhắn của người dùng và, dựa trên lời nhắc hệ thống (bao gồm thông tin các tác nhân có sẵn), tạo ra một kế hoạch du lịch có cấu trúc.
* Liệt kê Tác nhân và Công cụ của họ: Đăng ký tác nhân chứa danh sách các tác nhân (ví dụ: cho chuyến bay, khách sạn, thuê xe và hoạt động) cùng với các chức năng hoặc công cụ mà họ cung cấp.
* Điều phối Kế hoạch đến các Tác nhân Tương ứng: Tùy thuộc vào số lượng nhiệm vụ phụ, người lập kế hoạch hoặc gửi trực tiếp thông điệp đến tác nhân chuyên biệt (cho các trường hợp làm việc đơn nhiệm vụ) hoặc điều phối qua quản lý nhóm trò chuyện để hợp tác đa tác nhân.
* Tóm tắt Kết quả: Cuối cùng, người lập kế hoạch tóm tắt kế hoạch đã tạo để rõ ràng.
Đoạn mã Python dưới đây minh họa các bước này:

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Mô hình Công việc phụ Du lịch

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # chúng tôi muốn giao công việc cho đại lý

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Tạo khách hàng

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Định nghĩa tin nhắn người dùng

system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text

# In nội dung phản hồi sau khi tải nó dưới dạng JSON

pprint(json.loads(response_content))
```

Phần tiếp theo là đầu ra từ đoạn mã trước đó và bạn có thể sử dụng đầu ra có cấu trúc này để điều phối đến `assigned_agent` và tóm tắt kế hoạch du lịch cho người dùng cuối.

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

Một notebook ví dụ với đoạn mã trên có sẵn [tại đây](07-python-agent-framework.ipynb).

### Lập kế hoạch Lặp lại

Một số nhiệm vụ đòi hỏi trao đổi qua lại hoặc lập kế hoạch lại, nơi kết quả của một nhiệm vụ phụ ảnh hưởng đến nhiệm vụ tiếp theo. Ví dụ, nếu tác nhân phát hiện định dạng dữ liệu không mong đợi khi đặt chuyến bay, nó có thể cần điều chỉnh chiến lược trước khi tiếp tục đặt khách sạn.

Ngoài ra, phản hồi của người dùng (ví dụ: một người dùng quyết định muốn chuyến bay sớm hơn) có thể kích hoạt việc lập kế hoạch lại một phần. Cách tiếp cận động, lặp lại này đảm bảo rằng giải pháp cuối cùng phù hợp với các giới hạn thực tế và sở thích người dùng thay đổi theo thời gian.

ví dụ mã

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. giống như mã trước và chuyển tiếp lịch sử người dùng, kế hoạch hiện tại

system_prompt = """You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(
    input=user_message,
    instructions=system_prompt,
    context=f"Previous travel plan - {TravelPlan}",
)
# .. lập lại kế hoạch và gửi các nhiệm vụ đến các đại lý tương ứng
```

Để lập kế hoạch toàn diện hơn, hãy xem bài <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost Magnetic One</a> về giải quyết các nhiệm vụ phức tạp.

## Tóm tắt

Trong bài viết này, chúng ta đã xem xét ví dụ về cách tạo một bộ lập kế hoạch có thể chọn động các tác nhân có sẵn được định nghĩa. Đầu ra của Bộ lập kế hoạch phân tách các nhiệm vụ và phân công các tác nhân để có thể thực hiện. Giả định rằng các tác nhân có quyền truy cập vào các chức năng/công cụ cần thiết để thực hiện nhiệm vụ. Bên cạnh các tác nhân, bạn có thể bao gồm các mẫu thiết kế khác như phản chiếu, tóm tắt và quản lý trò chuyện theo vòng để tùy biến thêm.

## Tài nguyên bổ sung

Magentic One - Hệ thống đa tác nhân tổng quát để giải quyết các nhiệm vụ phức tạp và đã đạt được kết quả ấn tượng trên nhiều tiêu chuẩn đánh giá tác nhân thử thách. Tham khảo: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Trong triển khai này, bộ điều phối tạo kế hoạch chi tiết từng nhiệm vụ và giao những nhiệm vụ này cho các tác nhân có sẵn. Bên cạnh việc lập kế hoạch, bộ điều phối cũng sử dụng cơ chế theo dõi tiến độ nhiệm vụ và lập kế hoạch lại khi cần.

### Có thêm câu hỏi về Mẫu Thiết kế Lập kế hoạch?

Tham gia [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ những người học khác, tham dự giờ văn phòng và được giải đáp các câu hỏi về Tác nhân AI.

## Bài học trước

[Xây dựng Tác nhân AI Đáng Tin Cậy](../06-building-trustworthy-agents/README.md)

## Bài học tiếp theo

[Mẫu Thiết kế Đa tác nhân](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn thông tin chính xác nhất. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu lầm hay diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->