[![Mẫu thiết kế Lập kế hoạch](../../../translated_images/vi/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Nhấp vào hình ảnh phía trên để xem video bài học này)_

# Lập kế hoạch thiết kế

## Giới thiệu

Bài học này sẽ bao gồm

* Xác định một mục tiêu tổng thể rõ ràng và chia một công việc phức tạp thành các nhiệm vụ nhỏ có thể quản lý được.
* Tận dụng đầu ra có cấu trúc để tạo phản hồi đáng tin cậy hơn và có thể đọc được bằng máy.
* Áp dụng cách tiếp cận dựa trên sự kiện để xử lý các công việc động và các đầu vào bất ngờ.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ hiểu về:

* Xác định và đặt mục tiêu tổng thể cho một tác nhân AI, đảm bảo tác nhân đó biết rõ điều gì cần đạt được.
* Phân tách một công việc phức tạp thành các nhiệm vụ nhỏ hơn có thể quản lý và sắp xếp chúng theo một trình tự logic.
* Trang bị cho các tác nhân các công cụ phù hợp (ví dụ: công cụ tìm kiếm hoặc công cụ phân tích dữ liệu), quyết định khi nào và cách sử dụng chúng, cũng như xử lý các tình huống bất ngờ phát sinh.
* Đánh giá kết quả các nhiệm vụ nhỏ, đo lường hiệu suất và lặp lại các hành động để cải thiện đầu ra cuối cùng.

## Xác định mục tiêu tổng thể và phân tách công việc

![Xác định mục tiêu và nhiệm vụ](../../../translated_images/vi/defining-goals-tasks.d70439e19e37c47a.webp)

Hầu hết các công việc trong thực tế quá phức tạp để giải quyết trong một bước duy nhất. Một tác nhân AI cần một mục tiêu ngắn gọn để hướng dẫn việc lập kế hoạch và hành động của nó. Ví dụ, hãy xem xét mục tiêu:

    "Tạo một lịch trình du lịch 3 ngày."

Mặc dù mục tiêu đơn giản để phát biểu, nhưng vẫn cần được làm rõ hơn. Mục tiêu càng rõ ràng, tác nhân (và bất kỳ cộng tác viên con người nào) càng có thể tập trung vào việc đạt được kết quả đúng, chẳng hạn như tạo lịch trình chi tiết với các lựa chọn bay, đề xuất khách sạn và gợi ý hoạt động.

### Phân tách nhiệm vụ

Các công việc lớn hoặc phức tạp trở nên dễ quản lý hơn khi được chia nhỏ thành các nhiệm vụ nhỏ hướng tới mục tiêu.
Với ví dụ lịch trình du lịch, bạn có thể phân tách mục tiêu thành:

* Đặt vé máy bay
* Đặt khách sạn
* Thuê xe
* Cá nhân hóa

Mỗi nhiệm vụ nhỏ sau đó có thể được xử lý bởi các tác nhân hoặc quy trình chuyên biệt. Một tác nhân có thể chuyên về tìm kiếm các ưu đãi vé máy bay tốt nhất, tác nhân khác tập trung vào đặt khách sạn, v.v. Một tác nhân điều phối hoặc “xuống dòng” có thể tổng hợp các kết quả này thành một lịch trình thống nhất cho người dùng cuối.

Cách tiếp cận mô-đun này cũng cho phép cải tiến từng bước. Ví dụ, bạn có thể thêm các tác nhân chuyên biệt cho Gợi ý ẩm thực hoặc Hoạt động địa phương và tinh chỉnh lịch trình theo thời gian.

### Đầu ra có cấu trúc

Các Mô hình Ngôn ngữ Lớn (LLMs) có thể tạo đầu ra có cấu trúc (ví dụ JSON) giúp các tác nhân hoặc dịch vụ xuống dòng dễ dàng phân tích và xử lý hơn. Điều này đặc biệt hữu ích trong bối cảnh đa tác nhân, nơi chúng ta có thể thực hiện các công việc này sau khi nhận được đầu ra từ kế hoạch.

Đoạn mã Python dưới đây minh họa một tác nhân lập kế hoạch đơn giản phân tách mục tiêu thành các nhiệm vụ nhỏ và tạo một kế hoạch có cấu trúc:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Mô hình Công việc Phụ Du lịch
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # chúng tôi muốn giao nhiệm vụ cho đại lý

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

### Tác nhân lập kế hoạch với phối hợp đa tác nhân

Trong ví dụ này, một Tác nhân Định tuyến Ngữ nghĩa nhận được yêu cầu của người dùng (ví dụ: "Tôi cần một kế hoạch khách sạn cho chuyến đi.").

Người lập kế hoạch sau đó:

* Nhận Kế hoạch Khách sạn: Người lập kế hoạch lấy tin nhắn của người dùng và dựa trên lời nhắc hệ thống (bao gồm thông tin các tác nhân có sẵn), tạo một kế hoạch du lịch có cấu trúc.
* Liệt kê các Tác nhân và Công cụ của họ: Danh sách tác nhân chứa danh sách các tác nhân (ví dụ: vé máy bay, khách sạn, thuê xe, và hoạt động) cùng với các chức năng hoặc công cụ họ cung cấp.
* Điều phối Kế hoạch đến các Tác nhân Tương ứng: Dựa trên số lượng nhiệm vụ nhỏ, người lập kế hoạch gửi tin nhắn trực tiếp tới một tác nhân chuyên biệt (cho trường hợp một nhiệm vụ) hoặc phối hợp qua quản lý nhóm trò chuyện để hợp tác đa tác nhân.
* Tóm tắt Kết quả: Cuối cùng, người lập kế hoạch tóm tắt kế hoạch được tạo ra để rõ ràng.
Mã Python dưới đây minh họa các bước này:

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

# Mô hình Nhiệm vụ Phụ Du lịch

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # chúng tôi muốn giao nhiệm vụ cho đại lý

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Tạo khách hàng

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Định nghĩa tin nhắn của người dùng

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

Phần tiếp theo là đầu ra từ đoạn mã trước và bạn có thể sử dụng đầu ra có cấu trúc này để định tuyến tới `assigned_agent` và tóm tắt kế hoạch du lịch cho người dùng cuối.

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

Một ví dụ notebook với đoạn mã trước có sẵn [tại đây](./code_samples/07-python-agent-framework.ipynb).

### Lập kế hoạch lặp đi lặp lại

Một số công việc đòi hỏi sự trao đổi qua lại hoặc tổ chức lại kế hoạch, nơi kết quả của một nhiệm vụ nhỏ ảnh hưởng đến nhiệm vụ tiếp theo. Ví dụ, nếu tác nhân phát hiện một định dạng dữ liệu bất ngờ khi đặt vé máy bay, nó có thể cần điều chỉnh chiến lược trước khi chuyển sang đặt khách sạn.

Ngoài ra, phản hồi của người dùng (ví dụ, một người quyết định họ muốn chuyến bay sớm hơn) có thể kích hoạt việc lập lại kế hoạch một phần. Cách tiếp cận động và lặp lại này bảo đảm rằng giải pháp cuối cùng phù hợp với các ràng buộc thực tế và sở thích người dùng thay đổi.

ví dụ mã mẫu

```python
import os
from agent_framework.foundry import FoundryChatClient
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

Để có kế hoạch toàn diện hơn, hãy xem bài <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost Magnetic One</a> về giải quyết các công việc phức tạp.

## Tóm tắt

Trong bài viết này, chúng ta đã xem ví dụ về cách tạo một tác nhân lập kế hoạch có thể lựa chọn năng động các tác nhân có sẵn được định nghĩa. Đầu ra của Bộ Lập kế hoạch phân tách các nhiệm vụ và giao tác nhân để thực thi. Giả định các tác nhân có quyền truy cập vào các chức năng/công cụ cần thiết để thực hiện nhiệm vụ. Bên cạnh các tác nhân, bạn có thể bao gồm các mẫu khác như phản chiếu, tóm tắt, và vòng quay trò chuyện để tùy chỉnh thêm.

## Tài nguyên bổ sung

Magnetic One - Hệ thống đa tác nhân tổng quát cho việc giải quyết các nhiệm vụ phức tạp và đã đạt được kết quả ấn tượng trên nhiều bài kiểm tra agentic khó khăn. Tham khảo: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. Trong triển khai này, bộ điều phối tạo các kế hoạch cụ thể nhiệm vụ và phân công các tác vụ này cho các tác nhân có sẵn. Ngoài việc lập kế hoạch, bộ điều phối còn sử dụng cơ chế theo dõi để giám sát tiến độ công việc và lập lại kế hoạch khi cần thiết.

### Có thêm câu hỏi về Mẫu thiết kế Lập kế hoạch?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ những người học khác, tham dự giờ làm việc và nhận giải đáp thắc mắc về Tác nhân AI của bạn.

## Bài học trước

[Xây dựng Tác nhân AI Đáng tin cậy](../06-building-trustworthy-agents/README.md)

## Bài học tiếp theo

[Mẫu thiết kế Đa tác nhân](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->