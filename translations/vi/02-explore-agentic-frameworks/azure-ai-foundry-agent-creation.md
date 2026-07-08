# Phát triển Dịch vụ Đại lý Microsoft Foundry

Trong bài tập này, bạn sử dụng các công cụ Dịch vụ Đại lý Microsoft Foundry trong [cổng Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) để tạo một đại lý cho Đặt chuyến bay. Đại lý này sẽ có khả năng tương tác với người dùng và cung cấp thông tin về các chuyến bay.

## Yêu cầu tiên quyết

Để hoàn thành bài tập này, bạn cần:
1. Một tài khoản Azure với một đăng ký đang hoạt động. [Tạo tài khoản miễn phí](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Bạn cần quyền để tạo một Microsoft Foundry hub hoặc có người tạo cho bạn.
    - Nếu vai trò của bạn là Người đóng góp hoặc Chủ sở hữu, bạn có thể làm theo các bước trong hướng dẫn này.

## Tạo một Microsoft Foundry hub

> **Lưu ý:** Microsoft Foundry trước đây được biết đến với tên Azure AI Studio.

1. Làm theo các hướng dẫn từ bài viết trên blog [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) để tạo một Microsoft Foundry hub.
2. Khi dự án của bạn được tạo, đóng mọi mẹo hiển thị và xem lại trang dự án trên cổng Microsoft Foundry, trang này sẽ trông giống hình ảnh sau:

    ![Microsoft Foundry Project](../../../translated_images/vi/azure-ai-foundry.88d0c35298348c2f.webp)

## Triển khai một mô hình

1. Trong ngăn bên trái cho dự án của bạn, trong phần **My assets**, chọn trang **Models + endpoints**.
2. Trong trang **Models + endpoints**, tab **Model deployments**, trong menu **+ Deploy model**, chọn **Deploy base model**.
3. Tìm kiếm mô hình `gpt-4o-mini` trong danh sách, sau đó chọn và xác nhận nó.

    > **Lưu ý**: Giảm TPM giúp tránh sử dụng quá mức hạn ngạch có trong đăng ký bạn đang dùng.

    ![Model Deployed](../../../translated_images/vi/model-deployment.3749c53fb81e18fd.webp)

## Tạo một đại lý

Bây giờ bạn đã triển khai một mô hình, bạn có thể tạo một đại lý. Đại lý là mô hình AI đàm thoại có thể dùng để tương tác với người dùng.

1. Trong ngăn bên trái cho dự án, trong phần **Build & Customize**, chọn trang **Agents**.
2. Nhấp vào **+ Create agent** để tạo đại lý mới. Trong hộp thoại **Agent Setup**:
    - Nhập tên cho đại lý, ví dụ `FlightAgent`.
    - Đảm bảo rằng việc triển khai mô hình `gpt-4o-mini` bạn đã tạo trước đó được chọn
    - Đặt **Instructions** theo lời nhắc bạn muốn đại lý tuân theo. Đây là ví dụ:
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> Để có lời nhắc chi tiết, bạn có thể xem [kho lưu trữ này](https://github.com/ShivamGoyal03/RoamMind) để biết thêm thông tin.
    
> Hơn nữa, bạn có thể thêm **Cơ sở Kiến thức** và **Hành động** để tăng cường khả năng của đại lý cung cấp thêm thông tin và thực hiện các tác vụ tự động dựa trên yêu cầu người dùng. Trong bài tập này, bạn có thể bỏ qua các bước này.
    
![Agent Setup](../../../translated_images/vi/agent-setup.9bbb8755bf5df672.webp)

3. Để tạo một đại lý đa AI mới, chỉ cần nhấp **New Agent**. Đại lý mới tạo sẽ được hiển thị trên trang Agents.


## Kiểm tra đại lý

Sau khi tạo đại lý, bạn có thể kiểm tra nó để xem cách nó phản hồi các truy vấn người dùng trong khu thử nghiệm trên cổng Microsoft Foundry.

1. Ở đầu ngăn **Setup** cho đại lý của bạn, chọn **Try in playground**.
2. Trong ngăn **Playground**, bạn có thể tương tác với đại lý bằng cách nhập truy vấn trong cửa sổ chat. Ví dụ, bạn có thể yêu cầu đại lý tìm chuyến bay từ Seattle đến New York vào ngày 28.

    > **Lưu ý**: Đại lý có thể không cung cấp câu trả lời chính xác do không có dữ liệu thời gian thực được sử dụng trong bài tập này. Mục đích là để kiểm tra khả năng hiểu và phản hồi các truy vấn dựa trên hướng dẫn đã cho.

    ![Agent Playground](../../../translated_images/vi/agent-playground.dc146586de715010.webp)

3. Sau khi kiểm tra đại lý, bạn có thể tùy chỉnh thêm bằng cách thêm các ý định, dữ liệu huấn luyện và hành động để nâng cao khả năng.

## Dọn dẹp tài nguyên

Khi bạn đã hoàn thành kiểm tra đại lý, bạn có thể xóa nó để tránh phát sinh chi phí thêm.
1. Mở [cổng Azure](https://portal.azure.com) và xem nội dung của nhóm tài nguyên nơi bạn đã triển khai tài nguyên hub dùng trong bài tập này.
2. Trên thanh công cụ, chọn **Delete resource group**.
3. Nhập tên nhóm tài nguyên và xác nhận bạn muốn xóa nó.

## Tài nguyên

- [Tài liệu Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Cổng Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Bắt đầu với Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Kiến thức nền tảng về đại lý AI trên Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->