# Sử dụng Giao thức Agentic (MCP, A2A và NLWeb)

[![Agentic Protocols](../../../translated_images/vi/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Nhấn vào hình trên để xem video bài học này)_

Khi việc sử dụng các đại lý AI ngày càng tăng, nhu cầu về các giao thức đảm bảo tiêu chuẩn hóa, an toàn và hỗ trợ đổi mới mở cũng càng lớn. Trong bài học này, chúng ta sẽ tìm hiểu 3 giao thức nhằm đáp ứng nhu cầu này - Giao thức Ngữ cảnh Mô hình (MCP), Đại lý với Đại lý (A2A) và Mạng Ngôn ngữ Tự nhiên (NLWeb).

## Giới thiệu

Trong bài học này, chúng ta sẽ đề cập đến:

• Cách **MCP** cho phép Đại lý AI truy cập các công cụ và dữ liệu bên ngoài để hoàn thành nhiệm vụ người dùng.

• Cách **A2A** cho phép giao tiếp và hợp tác giữa các đại lý AI khác nhau.

• Cách **NLWeb** mang các giao diện ngôn ngữ tự nhiên đến bất kỳ trang web nào, cho phép các đại lý AI khám phá và tương tác với nội dung.

## Mục tiêu học tập

• **Xác định** mục đích cốt lõi và lợi ích của MCP, A2A và NLWeb trong bối cảnh các đại lý AI.

• **Giải thích** cách mỗi giao thức tạo điều kiện cho giao tiếp và tương tác giữa các LLM, công cụ, và các đại lý khác.

• **Nhận biết** các vai trò riêng biệt mà mỗi giao thức đóng vai trò trong việc xây dựng các hệ thống đa đại lý phức tạp.

## Giao thức Ngữ cảnh Mô hình

**Giao thức Ngữ cảnh Mô hình (MCP)** là một tiêu chuẩn mở cung cấp cách chuẩn hóa để ứng dụng cung cấp ngữ cảnh và công cụ cho các LLM. Điều này tạo điều kiện cho một "bộ điều hợp chung" với các nguồn dữ liệu và công cụ khác nhau mà các Đại lý AI có thể kết nối một cách nhất quán.

Hãy cùng xem các thành phần của MCP, lợi ích so với việc sử dụng API trực tiếp, và một ví dụ về cách các đại lý AI có thể sử dụng một máy chủ MCP.

### Các thành phần cốt lõi của MCP

MCP hoạt động trên kiến trúc **máy khách - máy chủ** và các thành phần cốt lõi gồm:

• **Hosts (Máy chủ lưu trữ)** là các ứng dụng LLM (ví dụ một trình soạn thảo mã như VSCode) khởi tạo kết nối với một Máy chủ MCP.

• **Clients (Máy khách)** là các thành phần trong ứng dụng host duy trì kết nối một-một với các máy chủ.

• **Servers (Máy chủ)** là các chương trình nhẹ cung cấp các khả năng cụ thể.

Bao gồm trong giao thức là ba nguyên tắc cốt lõi, tức là khả năng của một Máy chủ MCP:

• **Tools (Công cụ)**: Đây là các hành động hoặc chức năng riêng biệt mà một đại lý AI có thể gọi để thực hiện hành động. Ví dụ, một dịch vụ thời tiết có thể cung cấp công cụ "lấy thời tiết", hoặc một máy chủ thương mại điện tử có thể cung cấp công cụ "mua sản phẩm". Máy chủ MCP quảng bá tên công cụ, mô tả và lược đồ đầu vào/đầu ra trong danh sách khả năng của chúng.

• **Resources (Tài nguyên)**: Đây là các mục dữ liệu hoặc tài liệu chỉ đọc mà một máy chủ MCP có thể cung cấp và các máy khách có thể truy xuất theo yêu cầu. Ví dụ bao gồm nội dung tệp, bản ghi cơ sở dữ liệu hoặc tệp nhật ký. Tài nguyên có thể là văn bản (như mã hoặc JSON) hoặc nhị phân (như hình ảnh hoặc PDF).

• **Prompts (Lời nhắc)**: Đây là các mẫu được định nghĩa trước cung cấp các lời nhắc đề xuất, cho phép các luồng công việc phức tạp hơn.

### Lợi ích của MCP

MCP mang lại các lợi thế đáng kể cho các Đại lý AI:

• **Khám phá Công cụ Động**: Các đại lý có thể nhận được động danh sách các công cụ sẵn có từ máy chủ cùng với mô tả về chức năng của chúng. Điều này khác với API truyền thống, thường yêu cầu mã hóa tĩnh cho các tích hợp, có nghĩa là bất kỳ thay đổi API nào cũng đòi hỏi cập nhật mã. MCP cung cấp cách "tích hợp một lần", dẫn đến sự thích ứng tốt hơn.

• **Tương tác Đa LLM**: MCP hoạt động trên nhiều LLM khác nhau, cung cấp sự linh hoạt để thay đổi mô hình cốt lõi để đánh giá hiệu suất tốt hơn.

• **Bảo mật Chuẩn hóa**: MCP bao gồm phương thức xác thực tiêu chuẩn, cải thiện khả năng mở rộng khi thêm quyền truy cập vào các máy chủ MCP bổ sung. Điều này đơn giản hơn nhiều so với quản lý các khóa và loại xác thực khác nhau cho các API truyền thống.

### Ví dụ về MCP

![MCP Diagram](../../../translated_images/vi/mcp-diagram.e4ca1cbd551444a1.webp)

Hãy tưởng tượng một người dùng muốn đặt một chuyến bay bằng một trợ lý AI được hỗ trợ bởi MCP.

1. **Kết nối**: Trợ lý AI (một máy khách MCP) kết nối với một máy chủ MCP do một hãng hàng không cung cấp.

2. **Khám phá Công cụ**: Máy khách hỏi máy chủ MCP của hãng hàng không, "Bạn có những công cụ nào sẵn có?" Máy chủ trả về các công cụ như "tìm kiếm chuyến bay" và "đặt chuyến bay".

3. **Gọi Công cụ**: Bạn sau đó bảo trợ lý AI, "Hãy tìm chuyến bay từ Portland đến Honolulu." Trợ lý AI, sử dụng LLM của mình, xác định cần gọi công cụ "tìm kiếm chuyến bay" và truyền các tham số liên quan (nơi đi, điểm đến) đến máy chủ MCP.

4. **Thực thi và Phản hồi**: Máy chủ MCP, hoạt động như một lớp bao quanh, thực hiện cuộc gọi thực tế đến API đặt chỗ nội bộ của hãng hàng không. Sau đó nhận thông tin chuyến bay (ví dụ dữ liệu JSON) và gửi về cho trợ lý AI.

5. **Tương tác tiếp theo**: Trợ lý AI trình bày các lựa chọn chuyến bay. Khi bạn chọn chuyến, trợ lý có thể gọi công cụ "đặt chuyến bay" trên cùng máy chủ MCP, hoàn tất đặt chỗ.

## Giao thức Đại lý với Đại lý (A2A)

Trong khi MCP tập trung kết nối LLM với công cụ, **Giao thức Đại lý với Đại lý (A2A)** tiến một bước nữa bằng cách cho phép giao tiếp và hợp tác giữa các đại lý AI khác nhau. A2A kết nối các đại lý AI thuộc các tổ chức, môi trường và nền tảng kỹ thuật khác nhau để hoàn thành một nhiệm vụ chung.

Chúng ta sẽ xem xét các thành phần và lợi ích của A2A, cùng một ví dụ về cách nó có thể được áp dụng trong ứng dụng du lịch của chúng ta.

### Các thành phần cốt lõi của A2A

A2A tập trung vào việc tạo điều kiện giao tiếp giữa các đại lý và khiến họ làm việc cùng nhau để hoàn thành một phần tác vụ của người dùng. Mỗi thành phần trong giao thức góp phần vào điều này:

#### Thẻ Đại lý (Agent Card)

Tương tự như cách máy chủ MCP chia sẻ danh sách công cụ, Thẻ Đại lý có:
- Tên của Đại lý.
- Một **mô tả về các nhiệm vụ chung** mà nó thực hiện.
- Một **danh sách các kỹ năng cụ thể** với mô tả giúp các đại lý khác (hoặc người dùng con người) hiểu khi nào và tại sao họ nên gọi đại lý đó.
- **URL điểm cuối hiện tại** của đại lý.
- **Phiên bản** và **khả năng** của đại lý như phản hồi liên tục và thông báo đẩy.

#### Bộ Thực thi Đại lý (Agent Executor)

Bộ Thực thi Đại lý chịu trách nhiệm **truyền bối cảnh cuộc trò chuyện người dùng đến đại lý từ xa**, đại lý cần điều này để hiểu nhiệm vụ cần hoàn thành. Trong máy chủ A2A, một đại lý sử dụng chính mô hình ngôn ngữ lớn (LLM) của mình để phân tích các yêu cầu đến và thực hiện các tác vụ bằng các công cụ nội bộ của nó.

#### Thành phẩm (Artifact)

Khi một đại lý từ xa hoàn thành nhiệm vụ được yêu cầu, sản phẩm công việc của nó được tạo thành một thành phẩm. Một thành phẩm **chứa kết quả công việc của đại lý**, một **mô tả những gì đã hoàn thành**, và **bối cảnh văn bản** được gửi qua giao thức. Sau khi thành phẩm được gửi đi, kết nối với đại lý từ xa bị đóng cho đến khi cần lại.

#### Hàng đợi Sự kiện (Event Queue)

Thành phần này được dùng để **xử lý cập nhật và truyền tin nhắn**. Nó đặc biệt quan trọng trong môi trường sản xuất cho hệ thống đa đại lý để ngăn ngừa việc kết nối giữa các đại lý bị đóng trước khi tác vụ hoàn thành, nhất là khi thời gian thực hiện tác vụ có thể kéo dài.

### Lợi ích của A2A

• **Hợp tác Nâng cao**: Nó cho phép các đại lý từ các nhà cung cấp và nền tảng khác nhau tương tác, chia sẻ ngữ cảnh, và làm việc cùng nhau, tạo điều kiện tự động hóa liền mạch trên các hệ thống từng bị tách rời.

• **Lựa chọn Mô hình Linh hoạt**: Mỗi đại lý A2A có thể quyết định LLM nào được sử dụng để phục vụ yêu cầu của mình, cho phép tối ưu hóa hoặc tinh chỉnh mô hình theo từng đại lý, khác với việc chỉ kết nối một LLM trong một số tình huống MCP.

• **Xác thực Tích hợp sẵn**: Xác thực được tích hợp trực tiếp vào giao thức A2A, cung cấp một khung bảo mật mạnh mẽ cho tương tác giữa các đại lý.

### Ví dụ về A2A

![A2A Diagram](../../../translated_images/vi/A2A-Diagram.8666928d648acc26.webp)

Hãy mở rộng kịch bản đặt chuyến du lịch của chúng ta, nhưng lần này sử dụng A2A.

1. **Yêu cầu Người dùng tới Multi-Đại lý**: Người dùng tương tác với một đại lý "Du lịch" là máy khách/đại lý A2A, có thể bằng cách nói, "Hãy đặt một chuyến đi toàn bộ đến Honolulu cho tuần tới, bao gồm chuyến bay, khách sạn, và xe thuê."

2. **Điều phối bởi Đại lý Du lịch**: Đại lý Du lịch nhận yêu cầu phức tạp này. Nó sử dụng LLM của mình để suy luận về nhiệm vụ và xác định rằng cần tương tác với các đại lý chuyên môn khác.

3. **Giao tiếp Giữa các Đại lý**: Đại lý Du lịch dùng giao thức A2A kết nối với các đại lý hạ nguồn, như "Đại lý Hàng không", "Đại lý Khách sạn", và "Đại lý Thuê xe" được tạo bởi các công ty khác nhau.

4. **Giao nhiệm vụ Ủy quyền**: Đại lý Du lịch gửi các nhiệm vụ cụ thể cho các đại lý chuyên môn này (ví dụ, "Tìm chuyến bay đến Honolulu," "Đặt khách sạn," "Thuê xe"). Mỗi đại lý chuyên môn, chạy LLM của riêng và sử dụng công cụ riêng của mình (có thể là máy chủ MCP), thực hiện phần việc đặt chỗ cụ thể.

5. **Phản hồi Hợp nhất**: Khi tất cả các đại lý hạ nguồn hoàn tất nhiệm vụ, Đại lý Du lịch tổng hợp kết quả (chi tiết chuyến bay, xác nhận khách sạn, đặt xe thuê) và gửi một phản hồi toàn diện, kiểu trò chuyện lại cho người dùng.

## Mạng Ngôn ngữ Tự nhiên (NLWeb)

Các trang web đã từ lâu là phương tiện chính để người dùng truy cập thông tin và dữ liệu trên internet.

Hãy xem xét các thành phần khác nhau của NLWeb, lợi ích của NLWeb và một ví dụ về cách NLWeb hoạt động qua ứng dụng du lịch của chúng ta.

### Các thành phần của NLWeb

- **Ứng dụng NLWeb (Mã dịch vụ cốt lõi)**: Hệ thống xử lý các câu hỏi ngôn ngữ tự nhiên. Nó kết nối các phần khác nhau của nền tảng để tạo câu trả lời. Có thể coi nó như **động cơ cung cấp các tính năng ngôn ngữ tự nhiên** của một trang web.

- **Giao thức NLWeb**: Đây là **bộ quy tắc cơ bản cho tương tác ngôn ngữ tự nhiên** với một trang web. Nó trả về các phản hồi ở định dạng JSON (thường dùng Schema.org). Mục tiêu là tạo nền tảng đơn giản cho “Web AI,” tương tự như HTML cho phép chia sẻ tài liệu trực tuyến.

- **Máy chủ MCP (Điểm cuối Giao thức Ngữ cảnh Mô hình)**: Mỗi thiết lập NLWeb cũng hoạt động như một **máy chủ MCP**. Điều này nghĩa là nó có thể **chia sẻ công cụ (như phương thức “ask”) và dữ liệu** với các hệ thống AI khác. Thực tế, điều này làm cho nội dung và khả năng của trang web có thể dùng được bởi các đại lý AI, cho phép trang web trở thành một phần của “hệ sinh thái đại lý” rộng lớn hơn.

- **Mô hình Nhúng**: Các mô hình này được dùng để **chuyển đổi nội dung trang web thành các biểu diễn số gọi là vector** (embedding). Các vector này nắm bắt ý nghĩa theo cách mà máy tính có thể so sánh và tìm kiếm. Chúng được lưu trong cơ sở dữ liệu đặc biệt, và người dùng có thể chọn mô hình nhúng mình muốn dùng.

- **Cơ sở dữ liệu vector (Cơ chế truy xuất)**: Cơ sở dữ liệu này **lưu trữ các embedding của nội dung trang web**. Khi ai đó đặt câu hỏi, NLWeb kiểm tra cơ sở dữ liệu vector để nhanh chóng tìm thông tin phù hợp nhất. Nó cung cấp danh sách nhanh các câu trả lời khả thi, xếp theo độ tương đồng. NLWeb hoạt động với nhiều hệ thống lưu trữ vector khác nhau như Qdrant, Snowflake, Milvus, Azure AI Search, và Elasticsearch.

### NLWeb thông qua ví dụ

![NLWeb](../../../translated_images/vi/nlweb-diagram.c1e2390b310e5fe4.webp)

Hãy xem lại trang web đặt chuyến du lịch của chúng ta, nhưng lần này được hỗ trợ bởi NLWeb.

1. **Nhập dữ liệu**: Danh mục sản phẩm hiện có của trang web du lịch (ví dụ, danh sách chuyến bay, mô tả khách sạn, gói tour) được định dạng theo Schema.org hoặc tải qua RSS feeds. Công cụ của NLWeb nhập dữ liệu có cấu trúc này, tạo embedding và lưu trong cơ sở dữ liệu vector cục bộ hoặc từ xa.

2. **Truy vấn ngôn ngữ tự nhiên (Con người)**: Người dùng truy cập trang web và thay vì điều hướng menu, nhập vào giao diện trò chuyện: "Tìm khách sạn thân thiện với gia đình ở Honolulu có hồ bơi cho tuần tới."

3. **Xử lý NLWeb**: Ứng dụng NLWeb nhận truy vấn này. Nó gửi truy vấn đến LLM để hiểu và đồng thời tìm kiếm cơ sở dữ liệu vector cho danh sách khách sạn liên quan.

4. **Kết quả chính xác**: LLM giúp diễn giải kết quả tìm kiếm từ cơ sở dữ liệu, xác định các kết quả phù hợp nhất dựa trên tiêu chí "thân thiện với gia đình," "hồ bơi," và "Honolulu," rồi định dạng phản hồi bằng ngôn ngữ tự nhiên. Quan trọng là, phản hồi tham chiếu đến các khách sạn thực từ danh mục trang web, tránh thông tin bịa đặt.

5. **Tương tác đại lý AI**: Vì NLWeb đóng vai trò máy chủ MCP, một đại lý du lịch AI bên ngoài cũng có thể kết nối với phiên bản NLWeb của trang web này. Đại lý AI có thể dùng phương thức `ask` của MCP để truy vấn trực tiếp trang web: `ask("Có nhà hàng ăn chay được khách sạn giới thiệu nào ở khu vực Honolulu không?")`. Phiên bản NLWeb sẽ xử lý, tận dụng cơ sở dữ liệu về nhà hàng (nếu có), và trả về phản hồi JSON có cấu trúc.

### Có thêm câu hỏi về MCP/A2A/NLWeb?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ những người học khác, tham gia giờ tư vấn và nhận câu trả lời cho các câu hỏi về Đại lý AI.

## Tài nguyên

- [MCP dành cho người mới bắt đầu](https://aka.ms/mcp-for-beginners)  
- [Tài liệu MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Kho mã nguồn NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Khung Đại lý Microsoft](https://aka.ms/ai-agents-beginners/agent-framework)

## Bài học trước

[Đại lý AI trong sản xuất](../10-ai-agents-production/README.md)

## Bài học tiếp theo

[Kỹ thuật Ngữ cảnh cho Đại lý AI](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->