# Sử Dụng Giao Thức Agentic (MCP, A2A và NLWeb)

[![Agentic Protocols](../../../translated_images/vi/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Nhấp vào hình ảnh trên để xem video bài học này)_

Khi việc sử dụng các tác nhân AI ngày càng tăng, nhu cầu về các giao thức đảm bảo chuẩn hóa, bảo mật và hỗ trợ đổi mới mở cũng tăng theo. Trong bài học này, chúng ta sẽ trình bày 3 giao thức nhằm đáp ứng nhu cầu này - Giao Thức Ngữ Cảnh Mô Hình (MCP), Tác Nhân đến Tác Nhân (A2A) và Web Ngôn Ngữ Tự Nhiên (NLWeb).

## Giới Thiệu

Trong bài học này, chúng ta sẽ tìm hiểu:

• Cách **MCP** cho phép các tác nhân AI truy cập công cụ và dữ liệu bên ngoài để hoàn thành các tác vụ người dùng.

• Cách **A2A** hỗ trợ giao tiếp và hợp tác giữa các tác nhân AI khác nhau.

• Cách **NLWeb** mang giao diện ngôn ngữ tự nhiên đến bất kỳ trang web nào, cho phép các tác nhân AI khám phá và tương tác với nội dung.

## Mục Tiêu Học Tập

• **Nhận diện** mục đích cốt lõi và lợi ích của MCP, A2A và NLWeb trong bối cảnh các tác nhân AI.

• **Giải thích** cách mỗi giao thức tạo điều kiện giao tiếp và tương tác giữa các LLM, công cụ và các tác nhân khác.

• **Nhận biết** vai trò riêng biệt mà mỗi giao thức đóng góp trong việc xây dựng hệ thống tác nhân phức tạp.

## Giao Thức Ngữ Cảnh Mô Hình

**Giao Thức Ngữ Cảnh Mô Hình (MCP)** là một tiêu chuẩn mở cung cấp cách chuẩn hóa để ứng dụng cung cấp ngữ cảnh và công cụ cho LLM. Điều này cho phép một "bộ chuyển đổi toàn cầu" đối với các nguồn dữ liệu và công cụ khác nhau mà các tác nhân AI có thể kết nối theo cách nhất quán.

Hãy xem xét các thành phần của MCP, những lợi ích so với việc sử dụng API trực tiếp, và một ví dụ về cách các tác nhân AI có thể sử dụng một máy chủ MCP.

### Các Thành Phần Cốt Lõi của MCP

MCP hoạt động trên kiến trúc **client-server (khách-chủ)** và các thành phần cốt lõi bao gồm:

• **Hosts** là các ứng dụng LLM (ví dụ như một trình soạn mã như VSCode) khởi tạo kết nối tới máy chủ MCP.

• **Clients** là các thành phần bên trong ứng dụng host duy trì kết nối một-một với máy chủ.

• **Servers** là các chương trình nhẹ cung cấp các khả năng cụ thể.

Giao thức bao gồm ba nguyên thủy cốt lõi là các khả năng của một máy chủ MCP:

• **Tools (Công cụ)**: Đây là các hành động hoặc chức năng riêng biệt mà một tác nhân AI có thể gọi để thực hiện một hành động. Ví dụ, một dịch vụ thời tiết có thể cung cấp công cụ "lấy thời tiết", hoặc máy chủ thương mại điện tử có thể cung cấp công cụ "mua sản phẩm". Máy chủ MCP quảng bá tên công cụ, mô tả và lược đồ đầu vào/đầu ra trong danh sách khả năng của chúng.

• **Resources (Tài nguyên)**: Đây là các mục dữ liệu chỉ đọc hoặc tài liệu mà một máy chủ MCP có thể cung cấp, và các client có thể truy xuất theo yêu cầu. Ví dụ như nội dung file, bản ghi cơ sở dữ liệu hoặc file log. Tài nguyên có thể là văn bản (như mã nguồn hoặc JSON) hoặc nhị phân (như hình ảnh hoặc PDF).

• **Prompts (Câu nhắc)**: Đây là các mẫu định nghĩa sẵn cung cấp các đề xuất, cho phép các luồng công việc phức tạp hơn.

### Lợi ích của MCP

MCP mang lại nhiều lợi thế quan trọng cho các tác nhân AI:

• **Khám Phá Công Cụ Động**: Các tác nhân có thể nhận danh sách các công cụ có sẵn từ máy chủ cùng với mô tả chức năng của chúng một cách động. Điều này khác với các API truyền thống, thường yêu cầu mã tĩnh cho tích hợp, có nghĩa là bất kỳ thay đổi API nào cũng đòi hỏi cập nhật mã. MCP cung cấp cách “tích hợp một lần” giúp dễ dàng thích ứng hơn.

• **Tính Tương Tác Giữa Các LLM**: MCP hoạt động với nhiều LLM khác nhau, cung cấp sự linh hoạt để chuyển đổi model lõi nhằm đánh giá hiệu suất tốt hơn.

• **Chuẩn Mực Bảo Mật**: MCP bao gồm phương thức xác thực chuẩn, nâng cao khả năng mở rộng khi thêm truy cập các máy chủ MCP khác. Điều này đơn giản hơn so với việc quản lý nhiều loại khóa và xác thực cho các API truyền thống khác nhau.

### Ví dụ về MCP

![MCP Diagram](../../../translated_images/vi/mcp-diagram.e4ca1cbd551444a1.webp)

Giả sử một người dùng muốn đặt vé máy bay sử dụng trợ lý AI được hỗ trợ bởi MCP.

1. **Kết nối**: Trợ lý AI (client MCP) kết nối đến máy chủ MCP do hãng hàng không cung cấp.

2. **Khám phá công cụ**: Client hỏi máy chủ MCP của hãng hàng không, "Bạn có những công cụ nào?" Máy chủ trả lời với các công cụ như "tìm chuyến bay" và "đặt chuyến bay".

3. **Gọi công cụ**: Người dùng yêu cầu trợ lý AI, "Hãy tìm chuyến bay từ Portland đến Honolulu." Trợ lý AI, sử dụng LLM của nó, nhận ra cần gọi công cụ "tìm chuyến bay" và truyền các tham số liên quan (nơi đi, nơi đến) đến máy chủ MCP.

4. **Thực thi và phản hồi**: Máy chủ MCP, như một bộ bao bọc, gọi API đặt chỗ bên trong của hãng hàng không. Sau đó nhận dữ liệu chuyến bay (ví dụ dữ liệu JSON) và gửi lại cho trợ lý AI.

5. **Tương tác tiếp theo**: Trợ lý AI trình bày các lựa chọn chuyến bay. Khi người dùng chọn chuyến bay, trợ lý có thể gọi công cụ "đặt chuyến bay" trên cùng máy chủ MCP để hoàn tất đặt chỗ.

## Giao Thức Tác Nhân đến Tác Nhân (A2A)

Trong khi MCP tập trung vào việc kết nối LLM với công cụ, **Giao Thức Tác Nhân đến Tác Nhân (A2A)** nâng cao hơn bằng cách cho phép giao tiếp và hợp tác giữa các tác nhân AI khác nhau. A2A kết nối các tác nhân AI giữa nhiều tổ chức, môi trường và hệ thống công nghệ để hoàn thành tác vụ chung.

Chúng ta sẽ xem xét các thành phần và lợi ích của A2A, cùng ví dụ về cách ứng dụng nó trong ứng dụng du lịch của chúng ta.

### Các Thành Phần Cốt Lõi của A2A

A2A tập trung vào việc cho phép giao tiếp giữa các tác nhân và làm việc cùng nhau để hoàn thành một tác vụ phụ của người dùng. Mỗi thành phần của giao thức đóng góp vào điều này:

#### Thẻ Tác Nhân (Agent Card)

Tương tự như máy chủ MCP chia sẻ danh sách công cụ, Thẻ Tác Nhân có:
- Tên của Tác Nhân.
- Một **mô tả các tác vụ chung** mà nó hoàn thành.
- Một **danh sách các kỹ năng cụ thể** cùng mô tả giúp các tác nhân khác (hoặc thậm chí người dùng con người) hiểu khi nào và tại sao họ muốn gọi tác nhân đó.
- **URL Điểm Kết (Endpoint) hiện tại** của tác nhân.
- **Phiên bản** và **khả năng** của tác nhân như trả về luồng dữ liệu streaming và thông báo đẩy.

#### Trình Thực Thi Tác Nhân (Agent Executor)

Trình Thực Thi Tác Nhân chịu trách nhiệm **truyền bối cảnh của cuộc trò chuyện người dùng đến tác nhân từ xa**, tác nhân từ xa cần điều này để hiểu tác vụ cần hoàn thành. Trong một máy chủ A2A, tác nhân sử dụng LLM riêng của mình để phân tích yêu cầu đến và thực hiện tác vụ bằng công cụ nội bộ của nó.

#### Sản Phẩm Tác Nhân (Artifact)

Khi tác nhân từ xa hoàn thành tác vụ yêu cầu, sản phẩm công việc của nó được tạo thành một artifact. Artifact **chứa kết quả công việc của tác nhân**, **mô tả những gì đã hoàn thành**, và **bối cảnh văn bản** được truyền qua giao thức. Sau khi artifact được gửi, kết nối với tác nhân từ xa được đóng lại cho đến khi cần lại.

#### Hàng Đợi Sự Kiện (Event Queue)

Thành phần này dùng để **xử lý các cập nhật và truyền tin nhắn**. Nó đặc biệt quan trọng trong môi trường sản xuất của các hệ thống tác nhân nhằm ngăn kết nối giữa các tác nhân bị đóng trước khi tác vụ hoàn thành, nhất là khi thời gian hoàn thành tác vụ có thể kéo dài.

### Lợi ích của A2A

• **Tăng Cường Hợp Tác**: Cho phép các tác nhân từ các nhà cung cấp và nền tảng khác nhau tương tác, chia sẻ bối cảnh và làm việc cùng nhau, tạo điều kiện tự động hóa liền mạch qua những hệ thống vốn tách biệt.

• **Linh Hoạt về Lựa Chọn Mô Hình**: Mỗi tác nhân A2A có thể quyết định sử dụng LLM nào để phục vụ các yêu cầu của mình, cho phép tối ưu hoặc tinh chỉnh từng model cho từng tác nhân, khác với việc kết nối một LLM duy nhất trong một số trường hợp MCP.

• **Xác Thực Tích Hợp**: Xác thực được tích hợp trực tiếp vào giao thức A2A, cung cấp khung bảo mật mạnh mẽ cho sự tương tác giữa các tác nhân.

### Ví dụ về A2A

![A2A Diagram](../../../translated_images/vi/A2A-Diagram.8666928d648acc26.webp)

Hãy mở rộng kịch bản đặt chuyến du lịch của chúng ta, lần này sử dụng A2A.

1. **Yêu cầu người dùng tới đa tác nhân**: Người dùng tương tác với một "Tác Nhân Du Lịch" A2A client/agent, ví dụ nói, "Hãy đặt toàn bộ chuyến đi tới Honolulu cho tuần tới, bao gồm vé máy bay, khách sạn và thuê xe".

2. **Điều phối bởi Tác Nhân Du Lịch**: Tác Nhân Du Lịch nhận yêu cầu phức tạp này. Nó sử dụng LLM của mình để suy luận về tác vụ và xác định cần tương tác với các tác nhân chuyên môn hóa khác.

3. **Giao tiếp liên tác nhân**: Tác Nhân Du Lịch sau đó dùng giao thức A2A để kết nối với các tác nhân phụ trợ, như "Tác Nhân Hãng Hàng Không," "Tác Nhân Khách Sạn," và "Tác Nhân Thuê Xe" được tạo bởi các công ty khác nhau.

4. **Phân công thực hiện tác vụ**: Tác Nhân Du Lịch gửi các tác vụ cụ thể cho các tác nhân chuyên môn này (ví dụ, "Tìm chuyến bay tới Honolulu," "Đặt khách sạn," "Thuê xe"). Mỗi tác nhân chuyên môn này, chạy LLM của riêng mình và sử dụng công cụ riêng (có thể là máy chủ MCP), thực hiện phần công việc cụ thể của mình.

5. **Phản hồi tổng hợp**: Sau khi các tác nhân phụ trợ hoàn thành tác vụ, Tác Nhân Du Lịch tổng hợp kết quả (chi tiết chuyến bay, xác nhận khách sạn, đặt xe thuê) và gửi phản hồi kiểu trò chuyện toàn diện trở lại người dùng.

## Web Ngôn Ngữ Tự Nhiên (NLWeb)

Các trang web từ lâu đã là cách chính để người dùng truy cập thông tin và dữ liệu trên internet.

Hãy xem xét các thành phần khác nhau của NLWeb, lợi ích của NLWeb và một ví dụ về cách hoạt động của NLWeb trong ứng dụng du lịch của chúng ta.

### Các Thành Phần của NLWeb

- **Ứng Dụng NLWeb (Mã Dịch Vụ Cốt Lõi)**: Hệ thống xử lý các câu hỏi ngôn ngữ tự nhiên. Nó kết nối các phần khác nhau của nền tảng để tạo câu trả lời. Bạn có thể coi đây là **động cơ hỗ trợ các tính năng ngôn ngữ tự nhiên** của trang web.

- **Giao Thức NLWeb**: Đây là **bộ quy tắc cơ bản để tương tác ngôn ngữ tự nhiên** với trang web. Nó gửi lại phản hồi dưới dạng JSON (thường sử dụng Schema.org). Mục đích là tạo nền tảng đơn giản cho “Web AI,” giống như HTML làm cho việc chia sẻ tài liệu trực tuyến trở nên khả thi.

- **Máy Chủ MCP (Điểm Kết Giao Thức Model Context Protocol)**: Mỗi cài đặt NLWeb cũng hoạt động như **một máy chủ MCP**. Điều này nghĩa là nó có thể **chia sẻ công cụ (như phương thức “ask”) và dữ liệu** với các hệ thống AI khác. Thực tế, điều này khiến nội dung và năng lực trang web trở nên có thể sử dụng bởi các tác nhân AI, giúp trang web trở thành một phần trong “hệ sinh thái tác nhân” rộng lớn hơn.

- **Mô hình Embedding**: Các mô hình này dùng để **chuyển đổi nội dung trang web thành các biểu diễn số gọi là vector (embedding)**. Các vector này nắm bắt ý nghĩa theo cách máy tính có thể so sánh và tìm kiếm. Chúng được lưu trữ trong cơ sở dữ liệu đặc biệt, và người dùng có thể chọn mô hình embedding mình muốn sử dụng.

- **Cơ Sở Dữ Liệu Vector (Cơ chế Truy Xuất)**: Cơ sở dữ liệu này **lưu trữ các embedding của nội dung trang web**. Khi ai đó đặt câu hỏi, NLWeb kiểm tra cơ sở dữ liệu vector để nhanh chóng tìm thông tin liên quan nhất. Nó cung cấp danh sách câu trả lời tiềm năng nhanh chóng, được xếp hạng theo độ tương đồng. NLWeb làm việc với các hệ thống lưu trữ vector khác nhau như Qdrant, Snowflake, Milvus, Azure AI Search và Elasticsearch.

### Ví dụ về NLWeb

![NLWeb](../../../translated_images/vi/nlweb-diagram.c1e2390b310e5fe4.webp)

Hãy xem lại trang web đặt chuyến du lịch của chúng ta, nhưng lần này, nó được hỗ trợ bởi NLWeb.

1. **Nhập Dữ Liệu**: Các danh mục sản phẩm hiện có của trang du lịch (ví dụ như danh sách chuyến bay, mô tả khách sạn, gói tour) được định dạng theo Schema.org hoặc tải qua RSS feed. Công cụ của NLWeb nhập dữ liệu có cấu trúc này, tạo embedding và lưu vào cơ sở dữ liệu vector cục bộ hoặc từ xa.

2. **Truy Vấn Ngôn Ngữ Tự Nhiên (Con Người)**: Người dùng truy cập trang web và thay vì duyệt menu, gõ vào giao diện chat: "Tìm khách sạn phù hợp cho gia đình ở Honolulu có hồ bơi cho tuần tới".

3. **Xử lý của NLWeb**: Ứng dụng NLWeb nhận truy vấn này. Nó gửi truy vấn đến LLM để hiểu ý nghĩa và đồng thời tìm kiếm cơ sở dữ liệu vector để lấy danh sách khách sạn liên quan.

4. **Kết quả chính xác**: LLM giúp diễn giải kết quả tìm kiếm từ cơ sở dữ liệu, xác định các kết quả phù hợp nhất dựa trên tiêu chí "phù hợp gia đình," "có hồ bơi," và "Honolulu," rồi định dạng đáp án bằng ngôn ngữ tự nhiên. Quan trọng là câu trả lời tham chiếu đến các khách sạn thực tế trong danh mục của trang, tránh thông tin bịa đặt.

5. **Tương tác với Tác Nhân AI**: Vì NLWeb hoạt động như máy chủ MCP, một tác nhân du lịch AI bên ngoài cũng có thể kết nối với phiên bản NLWeb của trang web này. Tác nhân AI có thể sử dụng phương thức `ask` MCP để truy vấn trực tiếp trang web: `ask("Có nhà hàng chay nào được khách sạn ở Honolulu khuyên dùng không?")`. Phiên bản NLWeb sẽ xử lý câu hỏi này, sử dụng cơ sở dữ liệu thông tin nhà hàng (nếu đã được nhập) và trả về phản hồi dạng JSON có cấu trúc.

### Cần thêm câu hỏi về MCP/A2A/NLWeb?

Tham gia cùng [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ những người học khác, tham dự giờ làm việc và được giải đáp các thắc mắc về Tác Nhân AI.

## Tài Nguyên

- [MCP cho Người Mới Bắt Đầu](https://aka.ms/mcp-for-beginners)  
- [Tài Liệu MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Kho Mã NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Khung Tác Nhân Microsoft](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->