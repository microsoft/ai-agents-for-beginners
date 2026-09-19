# Sử dụng Giao thức Agentic (MCP, A2A và NLWeb)

[![Agentic Protocols](../../../translated_images/vi/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Nhấp vào hình ảnh trên để xem video bài học này)_

Khi việc sử dụng các tác nhân AI ngày càng tăng, nhu cầu về các giao thức đảm bảo chuẩn hóa, bảo mật và hỗ trợ đổi mới mở cũng tăng theo. Trong bài học này, chúng ta sẽ tìm hiểu 3 giao thức nhằm đáp ứng nhu cầu đó - Giao thức Ngữ cảnh Mô hình (MCP), Agent to Agent (A2A) và Natural Language Web (NLWeb).

## Giới thiệu

Trong bài học này, chúng ta sẽ tìm hiểu:

• Làm thế nào **MCP** cho phép các tác nhân AI truy cập công cụ và dữ liệu bên ngoài để hoàn thành các nhiệm vụ người dùng.

• Làm thế nào **A2A** hỗ trợ giao tiếp và hợp tác giữa các tác nhân AI khác nhau.

• Làm thế nào **NLWeb** mang giao diện ngôn ngữ tự nhiên đến bất kỳ trang web nào, cho phép các tác nhân AI khám phá và tương tác với nội dung.

## Mục tiêu học tập

• **Nhận diện** mục đích cốt lõi và lợi ích của MCP, A2A, và NLWeb trong bối cảnh các tác nhân AI.

• **Giải thích** cách mỗi giao thức hỗ trợ giao tiếp và tương tác giữa LLM, công cụ và các tác nhân khác.

• **Nhận biết** vai trò riêng biệt của từng giao thức trong việc xây dựng các hệ thống tác nhân phức tạp.

## Giao thức Ngữ cảnh Mô hình

**Giao thức Ngữ cảnh Mô hình (MCP)** là một chuẩn mở cung cấp cách tiêu chuẩn cho các ứng dụng cung cấp ngữ cảnh và công cụ tới LLM. Điều này cho phép một "bộ chuyển đổi phổ quát" đến các nguồn dữ liệu và công cụ khác nhau mà các tác nhân AI có thể kết nối một cách nhất quán.

Hãy xem xét các thành phần của MCP, lợi ích so với việc sử dụng API trực tiếp, và một ví dụ về cách các tác nhân AI có thể sử dụng một máy chủ MCP.

### Các thành phần cốt lõi của MCP

MCP hoạt động trên kiến trúc **client-server** và các thành phần cốt lõi là:

• **Hosts** là các ứng dụng LLM (ví dụ một trình soạn mã như VSCode) khởi tạo kết nối tới Máy chủ MCP.

• **Clients** là các thành phần bên trong ứng dụng host duy trì kết nối một-một với các máy chủ.

• **Servers** là các chương trình nhẹ cung cấp các khả năng cụ thể.

Bao gồm trong giao thức là ba nguyên thủy cốt lõi, vốn là các khả năng của Máy chủ MCP:

• **Tools**: Đây là các hành động hoặc chức năng riêng biệt mà tác nhân AI có thể gọi để thực hiện một hành động. Ví dụ, dịch vụ thời tiết có thể cung cấp công cụ "lấy thông tin thời tiết", hoặc một máy chủ thương mại điện tử có thể cung cấp công cụ "mua sản phẩm". Các máy chủ MCP quảng cáo tên công cụ, mô tả và sơ đồ đầu vào/đầu ra trong danh sách khả năng của mình.

• **Resources**: Đây là các mục dữ liệu hay tài liệu chỉ đọc mà máy chủ MCP có thể cung cấp, và các client có thể truy xuất theo nhu cầu. Ví dụ bao gồm nội dung file, bản ghi cơ sở dữ liệu, hoặc file nhật ký. Resources có thể là văn bản (như mã hoặc JSON) hoặc nhị phân (như ảnh hoặc PDF).

• **Prompts**: Đây là các mẫu định sẵn cung cấp các gợi ý nhắc, cho phép các luồng công việc phức tạp hơn.

### Lợi ích của MCP

MCP mang lại lợi ích lớn cho các tác nhân AI:

• **Khám phá Công cụ Động**: Các tác nhân có thể nhận danh sách các công cụ có sẵn từ máy chủ cùng với mô tả về chức năng của chúng. Điều này khác với các API truyền thống, thường yêu cầu mã hóa tĩnh cho việc tích hợp, nghĩa là bất kỳ thay đổi API nào cũng đòi hỏi cập nhật mã. MCP cung cấp phương pháp "kết nối một lần", dẫn đến khả năng thích ứng cao hơn.

• **Tính Tương tác Giữa Các LLM**: MCP hoạt động trên các LLM khác nhau, cho phép linh hoạt thay đổi mô hình cốt lõi để đánh giá hiệu suất tốt hơn.

• **Bảo mật Chuẩn hóa**: MCP bao gồm phương pháp xác thực tiêu chuẩn, cải thiện khả năng mở rộng khi thêm truy cập vào các máy chủ MCP khác. Điều này đơn giản hơn so với việc quản lý các khóa và kiểu xác thực khác nhau cho các API truyền thống.

### Ví dụ về MCP

![MCP Diagram](../../../translated_images/vi/mcp-diagram.e4ca1cbd551444a1.webp)

Hãy tưởng tượng một người dùng muốn đặt chuyến bay qua trợ lý AI được cung cấp bởi MCP.

1. **Kết nối**: Trợ lý AI (client MCP) kết nối đến máy chủ MCP do một hãng hàng không cung cấp.

2. **Khám phá Công cụ**: Client hỏi máy chủ MCP của hãng hàng không, "Bạn có công cụ gì?" Máy chủ phản hồi với danh sách công cụ như "tìm kiếm chuyến bay" và "đặt chuyến bay".

3. **Gọi Công cụ**: Người dùng nói với trợ lý AI, "Vui lòng tìm chuyến bay từ Portland đến Honolulu." Trợ lý AI, sử dụng LLM của mình, xác định cần gọi công cụ "tìm kiếm chuyến bay" và truyền các tham số liên quan (nơi khởi hành, điểm đến) cho máy chủ MCP.

4. **Thực thi và Phản hồi**: Máy chủ MCP đóng vai trò như một lớp bao bọc, gọi thực tế API đặt chỗ nội bộ của hãng hàng không. Sau đó nhận thông tin chuyến bay (ví dụ dữ liệu JSON) và gửi lại cho trợ lý AI.

5. **Tương tác Thêm**: Trợ lý AI trình bày các lựa chọn chuyến bay. Khi người dùng chọn một chuyến bay, trợ lý có thể gọi công cụ "đặt chuyến bay" trên cùng máy chủ MCP, hoàn tất đặt chỗ.

## Giao thức Agent-to-Agent (A2A)

Trong khi MCP tập trung kết nối LLM với công cụ, **giao thức Agent-to-Agent (A2A)** tiến thêm một bước khi cho phép giao tiếp và hợp tác giữa các tác nhân AI khác nhau. A2A kết nối các tác nhân AI giữa các tổ chức, môi trường và hạ tầng công nghệ khác nhau để hoàn thành một nhiệm vụ chung.

Chúng ta sẽ xem xét thành phần và lợi ích của A2A, cùng với một ví dụ về cách có thể áp dụng trong ứng dụng du lịch của chúng ta.

### Các thành phần cốt lõi của A2A

A2A tập trung vào việc cho phép giao tiếp giữa các tác nhân và để họ làm việc cùng nhau hoàn thành các nhiệm vụ phụ của người dùng. Mỗi thành phần giao thức đóng góp vào điều này:

#### Agent Card

Tương tự như cách máy chủ MCP chia sẻ danh sách công cụ, Agent Card có:
- Tên của tác nhân.
- Một **mô tả về các nhiệm vụ chung** mà tác nhân hoàn thành.
- Một **danh sách các kỹ năng cụ thể** kèm mô tả giúp các tác nhân khác (hoặc người dùng) hiểu khi nào và tại sao họ muốn gọi tác nhân đó.
- **URL Điểm cuối hiện tại** của tác nhân.
- **Phiên bản** và **khả năng** của tác nhân như phản hồi streaming và thông báo đẩy.

#### Agent Executor

Agent Executor chịu trách nhiệm **truyền ngữ cảnh cuộc trò chuyện của người dùng tới tác nhân từ xa**, tác nhân từ xa cần điều này để hiểu nhiệm vụ phải hoàn thành. Trong server A2A, một tác nhân sử dụng LLM riêng của mình để phân tích yêu cầu đến và thực hiện nhiệm vụ bằng các công cụ nội bộ của nó.

#### Artifact

Khi tác nhân từ xa đã hoàn thành nhiệm vụ yêu cầu, sản phẩm công việc của nó được tạo thành một artifact. Một artifact **chứa kết quả công việc của tác nhân**, **mô tả những gì đã hoàn thành**, và **ngữ cảnh văn bản** được truyền qua giao thức. Sau khi gửi artifact, kết nối với tác nhân từ xa được đóng cho đến khi cần lại.

#### Event Queue

Thành phần này dùng cho **xử lý cập nhật và truyền tải tin nhắn**. Nó đặc biệt quan trọng trong môi trường sản xuất cho các hệ thống tác nhân để ngăn chặn việc đóng kết nối giữa các tác nhân trước khi hoàn thành nhiệm vụ, đặc biệt khi thời gian hoàn thành có thể kéo dài.

### Lợi ích của A2A

• **Hợp tác nâng cao**: Cho phép các tác nhân từ nhà cung cấp và nền tảng khác nhau tương tác, chia sẻ ngữ cảnh, và làm việc cùng nhau, tạo điều kiện tự động hóa mượt mà giữa các hệ thống vốn tách rời.

• **Linh hoạt chọn mô hình**: Mỗi tác nhân A2A có thể quyết định LLM sử dụng để phục vụ yêu cầu của mình, cho phép tối ưu hoặc tinh chỉnh mô hình riêng cho từng tác nhân, khác với việc kết nối LLM đơn lẻ trong một số trường hợp MCP.

• **Xác thực tích hợp sẵn**: Xác thực được tích hợp trực tiếp trong giao thức A2A, cung cấp khung bảo mật vững chắc cho tương tác giữa các tác nhân.

### Ví dụ về A2A

![A2A Diagram](../../../translated_images/vi/A2A-Diagram.8666928d648acc26.webp)

Hãy mở rộng kịch bản đặt chuyến đi của chúng ta, nhưng lần này sử dụng A2A.

1. **Yêu cầu Người dùng tới Tác nhân Đa tác nhân**: Một người dùng tương tác với tác nhân khách hàng "Travel Agent" A2A, có thể bằng cách nói, "Vui lòng đặt một chuyến đi toàn bộ đến Honolulu cho tuần tới, bao gồm vé máy bay, khách sạn và thuê xe."

2. **Điều phối bởi Travel Agent**: Travel Agent nhận yêu cầu phức tạp này. Nó dùng LLM của mình để suy luận về nhiệm vụ và xác định cần tương tác với các tác nhân chuyên biệt khác.

3. **Giao tiếp giữa các tác nhân**: Travel Agent sau đó sử dụng giao thức A2A để kết nối với các tác nhân hạ nguồn, như "Airline Agent", "Hotel Agent", và "Car Rental Agent" do các công ty khác nhau tạo ra.

4. **Ủy quyền thực hiện nhiệm vụ**: Travel Agent gửi các nhiệm vụ cụ thể cho các tác nhân chuyên biệt này (ví dụ, "Tìm chuyến bay đến Honolulu," "Đặt khách sạn," "Thuê xe"). Mỗi tác nhân chuyên biệt này, chạy các LLM riêng và sử dụng công cụ riêng của mình (có thể là các máy chủ MCP), thực hiện phần công việc đặt chỗ của riêng mình.

5. **Phản hồi Tổng hợp**: Khi tất cả các tác nhân hạ nguồn hoàn thành nhiệm vụ, Travel Agent tổng hợp kết quả (chi tiết chuyến bay, xác nhận khách sạn, đặt xe) và gửi phản hồi toàn diện theo phong cách chat lại cho người dùng.

## Natural Language Web (NLWeb)

Các trang web từ lâu đã là cách chính giúp người dùng truy cập thông tin và dữ liệu trên internet.

Hãy xem các thành phần khác nhau của NLWeb, lợi ích của NLWeb và ví dụ về cách NLWeb hoạt động qua ứng dụng du lịch của chúng ta.

### Các thành phần của NLWeb

- **Ứng dụng NLWeb (Mã dịch vụ lõi)**: Hệ thống xử lý các câu hỏi ngôn ngữ tự nhiên. Nó kết nối các phần khác nhau của nền tảng để tạo phản hồi. Bạn có thể nghĩ đây như là **động cơ hỗ trợ các tính năng ngôn ngữ tự nhiên của trang web**.

- **Giao thức NLWeb**: Đây là **bộ quy tắc cơ bản cho tương tác ngôn ngữ tự nhiên với website**. Nó gửi trả phản hồi ở định dạng JSON (thường dùng Schema.org). Mục tiêu là tạo nền tảng đơn giản cho "AI Web," tương tự như HTML đã mở ra khả năng chia sẻ tài liệu trực tuyến.

- **Máy chủ MCP (Điểm cuối Giao thức Ngữ cảnh Mô hình)**: Mỗi thiết lập NLWeb cũng hoạt động như một **máy chủ MCP**. Điều này có nghĩa là nó có thể **chia sẻ công cụ (như phương pháp "ask") và dữ liệu** với các hệ thống AI khác. Thực tế, điều này khiến nội dung và năng lực của website có thể sử dụng bởi các tác nhân AI, giúp website trở thành một phần của “hệ sinh thái tác nhân” rộng lớn hơn.

- **Mô hình Embedding**: Các mô hình này dùng để **chuyển nội dung website thành các biểu diễn số gọi là vector** (embedding). Các vector này nắm giữ ý nghĩa theo cách máy tính có thể so sánh và tìm kiếm. Chúng được lưu trữ trong cơ sở dữ liệu đặc biệt, và người dùng có thể chọn mô hình embedding muốn dùng.

- **Cơ sở dữ liệu Vector (Cơ chế truy xuất)**: Cơ sở dữ liệu này **lưu trữ các embedding của nội dung trang web**. Khi ai đó đặt câu hỏi, NLWeb kiểm tra cơ sở dữ liệu vector để nhanh chóng tìm thông tin phù hợp nhất. Nó cung cấp danh sách các câu trả lời khả thi, xếp theo độ tương đồng. NLWeb làm việc với các hệ thống lưu trữ vector khác nhau như Qdrant, Snowflake, Milvus, Azure AI Search và Elasticsearch.

### Ví dụ về NLWeb

![NLWeb](../../../translated_images/vi/nlweb-diagram.c1e2390b310e5fe4.webp)

Hãy xem lại trang web đặt chuyến đi của chúng ta, nhưng lần này, nó được cung cấp bởi NLWeb.

1. **Nhập dữ liệu**: Các danh mục sản phẩm hiện tại của trang du lịch (ví dụ, danh sách chuyến bay, mô tả khách sạn, các gói tour) được định dạng theo Schema.org hoặc tải qua các nguồn RSS. Công cụ NLWeb nhập dữ liệu có cấu trúc này, tạo embedding và lưu chúng vào cơ sở dữ liệu vector cục bộ hoặc từ xa.

2. **Truy vấn Ngôn ngữ Tự nhiên (Người dùng)**: Người dùng truy cập trang web và thay vì điều hướng menu, gõ vào giao diện chat: "Tìm khách sạn thân thiện với gia đình ở Honolulu có bể bơi cho tuần tới."

3. **Xử lý NLWeb**: Ứng dụng NLWeb nhận truy vấn này. Nó gửi truy vấn đến LLM để hiểu và đồng thời tìm kiếm trong cơ sở dữ liệu vector các khách sạn có liên quan.

4. **Kết quả chính xác**: LLM hỗ trợ diễn giải kết quả tìm kiếm từ cơ sở dữ liệu, xác định các kết quả tốt nhất dựa trên tiêu chí "thân thiện với gia đình," "bể bơi," và "Honolulu," rồi tạo phản hồi bằng ngôn ngữ tự nhiên. Quan trọng là phản hồi tham chiếu đến khách sạn thật từ danh mục trang web, tránh thông tin bịa đặt.

5. **Tương tác với Tác nhân AI**: Vì NLWeb hoạt động như một máy chủ MCP, một tác nhân du lịch AI bên ngoài cũng có thể kết nối với phiên bản NLWeb của trang này. Tác nhân AI có thể sử dụng phương pháp `ask` của MCP để truy vấn trực tiếp website: `ask("Có nhà hàng chay nào được khách sạn ở khu vực Honolulu khuyên không?")`. Phiên bản NLWeb sẽ xử lý, tận dụng cơ sở dữ liệu nhà hàng (nếu đã tải) và trả về phản hồi JSON có cấu trúc.

### Còn câu hỏi nào về MCP/A2A/NLWeb?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ các học viên khác, tham dự giờ văn phòng và nhận giải đáp cho các câu hỏi về Tác nhân AI.

## Tài nguyên

- [MCP cho người mới bắt đầu](https://aka.ms/mcp-for-beginners)  
- [Tài liệu MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Kho mã NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Bài học trước

[AI Agents in Production](../10-ai-agents-production/README.md)

## Bài học tiếp theo

[Kỹ thuật Ngữ cảnh cho Tác nhân AI](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->