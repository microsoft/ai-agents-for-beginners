# Phát triển Dịch vụ Microsoft Foundry Agent

Trong bài tập này, bạn sử dụng các công cụ Microsoft Foundry Agent Service trong [cổng Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) để tạo một đại lý cho Đặt Vé Máy Bay. Đại lý sẽ có khả năng tương tác với người dùng và cung cấp thông tin về các chuyến bay.

## Yêu cầu trước

Để hoàn thành bài tập này, bạn cần những điều sau:
1. Một tài khoản Azure với một đăng ký đang hoạt động. [Tạo tài khoản miễn phí](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Bạn cần có quyền tạo một trung tâm Microsoft Foundry hoặc có một trung tâm được tạo cho bạn.
    - Nếu vai trò của bạn là Người đóng góp hoặc Chủ sở hữu, bạn có thể theo các bước trong hướng dẫn này.

## Tạo một trung tâm Microsoft Foundry

> **Lưu ý:** Microsoft Foundry trước đây được biết đến với tên Azure AI Studio.

1. Theo các hướng dẫn từ bài đăng trên blog [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) để tạo một trung tâm Microsoft Foundry.
2. Khi dự án của bạn được tạo, đóng bất kỳ mẹo nào hiển thị và xem lại trang dự án trên cổng Microsoft Foundry, nó sẽ giống như hình ảnh sau:

    ![Microsoft Foundry Project](../../../translated_images/vi/azure-ai-foundry.88d0c35298348c2f.webp)

## Triển khai một mô hình

1. Trong ngăn bên trái cho dự án của bạn, trong phần **Tài sản của tôi**, chọn trang **Models + endpoints**.
2. Trong trang **Models + endpoints**, ở tab **Model deployments**, trong menu **+ Deploy model**, chọn **Deploy base model**.
3. Tìm kiếm mô hình `gpt-4.1-mini` trong danh sách, sau đó chọn và xác nhận.

    > **Lưu ý**: Giảm TPM giúp tránh sử dụng quá mức hạn mức có sẵn trong đăng ký bạn đang sử dụng.

    ![Model Deployed](../../../translated_images/vi/model-deployment.3749c53fb81e18fd.webp)

## Tạo một đại lý

Bây giờ bạn đã triển khai một mô hình, bạn có thể tạo một đại lý. Đại lý là một mô hình AI hội thoại có thể được sử dụng để tương tác với người dùng.

1. Trong ngăn bên trái cho dự án của bạn, trong phần **Xây dựng & Tùy chỉnh**, chọn trang **Agents**.
2. Nhấp vào **+ Tạo đại lý** để tạo một đại lý mới. Trong hộp thoại **Thiết lập Đại lý**:
    - Nhập tên cho đại lý, ví dụ như `FlightAgent`.
    - Đảm bảo rằng triển khai mô hình `gpt-4.1-mini` bạn đã tạo trước đó được chọn
    - Đặt **Hướng dẫn** theo lời nhắc bạn muốn đại lý tuân theo. Đây là một ví dụ:
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
> Để có lời nhắc chi tiết, bạn có thể tham khảo [kho lưu trữ này](https://github.com/ShivamGoyal03/RoamMind) để biết thêm thông tin.
    
> Hơn nữa, bạn có thể thêm **Cơ sở Kiến thức** và **Hành động** để nâng cao khả năng của đại lý trong việc cung cấp thêm thông tin và thực hiện các tác vụ tự động dựa trên yêu cầu của người dùng. Trong bài tập này, bạn có thể bỏ qua các bước này.
    
![Agent Setup](../../../translated_images/vi/agent-setup.9bbb8755bf5df672.webp)

3. Để tạo một đại lý đa AI mới, chỉ cần nhấp vào **Đại lý Mới**. Đại lý mới tạo sẽ được hiển thị trên trang Agents.


## Kiểm tra đại lý

Sau khi tạo đại lý, bạn có thể kiểm tra nó để xem cách nó phản hồi các truy vấn của người dùng trong sân chơi của cổng Microsoft Foundry.

1. Ở đầu ngăn **Thiết lập** cho đại lý của bạn, chọn **Thử trong sân chơi**.
2. Trong ngăn **Sân chơi**, bạn có thể tương tác với đại lý bằng cách nhập truy vấn trong cửa sổ trò chuyện. Ví dụ, bạn có thể yêu cầu đại lý tìm chuyến bay từ Seattle đến New York vào ngày 28.

    > **Lưu ý**: Đại lý có thể không cung cấp câu trả lời chính xác, vì không sử dụng dữ liệu thời gian thực trong bài tập này. Mục đích là để kiểm tra khả năng hiểu và phản hồi các truy vấn của người dùng dựa trên hướng dẫn đã cung cấp.

    ![Agent Playground](../../../translated_images/vi/agent-playground.dc146586de715010.webp)

3. Sau khi kiểm tra đại lý, bạn có thể tùy chỉnh thêm bằng cách thêm nhiều mục đích, dữ liệu huấn luyện và hành động để nâng cao khả năng của nó.

## Dọn dẹp tài nguyên

Khi bạn đã hoàn tất việc kiểm tra đại lý, bạn có thể xóa nó để tránh phát sinh thêm chi phí.
1. Mở [cổng Azure](https://portal.azure.com) và xem nội dung của nhóm tài nguyên nơi bạn đã triển khai các tài nguyên trung tâm sử dụng trong bài tập này.
2. Trên thanh công cụ, chọn **Xóa nhóm tài nguyên**.
3. Nhập tên nhóm tài nguyên và xác nhận rằng bạn muốn xóa nó.

## Tài nguyên

- [Tài liệu Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Cổng Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Bắt đầu với Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Những điều cơ bản về đại lý AI trên Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->