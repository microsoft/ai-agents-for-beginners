# Sử dụng Giao thức Agentic (MCP, A2A và NLWeb)

[![Giao thức Agentic](../../../translated_images/vi/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Nhấp vào hình ảnh ở trên để xem video của bài học này)_

Khi việc sử dụng các tác nhân AI (AI agents) tăng lên, nhu cầu về các giao thức đảm bảo tiêu chuẩn hóa, bảo mật và hỗ trợ đổi mới mở cũng tăng theo. Trong bài học này, chúng ta sẽ trình bày 3 giao thức nhằm đáp ứng nhu cầu đó - Model Context Protocol (MCP), Agent to Agent (A2A) và Natural Language Web (NLWeb).

## Giới thiệu

Trong bài học này, chúng ta sẽ bao quát:

• Cách **MCP** cho phép các AI Agents truy cập công cụ và dữ liệu bên ngoài để hoàn thành nhiệm vụ của người dùng.

• Cách **A2A** cho phép giao tiếp và hợp tác giữa các tác nhân AI khác nhau.

• Cách **NLWeb** đem giao diện ngôn ngữ tự nhiên tới bất kỳ trang web nào, cho phép AI Agents khám phá và tương tác với nội dung.

## Mục tiêu học tập

• **Xác định** mục đích cốt lõi và lợi ích của MCP, A2A và NLWeb trong bối cảnh các tác nhân AI.

• **Giải thích** cách mỗi giao thức tạo điều kiện cho giao tiếp và tương tác giữa LLMs, công cụ và các tác nhân khác.

• **Nhận diện** vai trò khác biệt mà mỗi giao thức đóng góp khi xây dựng các hệ thống agentic phức tạp.

## Model Context Protocol

Giao thức **Model Context Protocol (MCP)** là một tiêu chuẩn mở cung cấp cách tiêu chuẩn hóa để các ứng dụng cung cấp ngữ cảnh và công cụ cho LLMs. Điều này cho phép một “bộ chuyển đổi phổ quát” tới các nguồn dữ liệu và công cụ khác nhau mà các AI Agents có thể kết nối theo một cách nhất quán.

Hãy xem các thành phần của MCP, lợi ích so với việc sử dụng API trực tiếp, và một ví dụ về cách các tác nhân AI có thể sử dụng một máy chủ MCP.

### Thành phần cốt lõi của MCP

MCP hoạt động theo kiến trúc **client-server** và các thành phần cốt lõi là:

• **Hosts** là các ứng dụng LLM (ví dụ một trình soạn thảo mã như VSCode) khởi tạo kết nối tới một Máy chủ MCP.

• **Clients** là các thành phần bên trong ứng dụng host duy trì kết nối một-một với các server.

• **Servers** là các chương trình nhẹ cung cấp các khả năng cụ thể.

Bao gồm trong giao thức có ba nguyên thủy cốt lõi là các khả năng của một Máy chủ MCP:

• **Tools**: Đây là các hành động hoặc chức năng rời rạc mà một tác nhân AI có thể gọi để thực hiện một thao tác. Ví dụ, một dịch vụ thời tiết có thể công khai một công cụ "get weather", hoặc một máy chủ thương mại điện tử có thể công khai một công cụ "purchase product". Máy chủ MCP quảng bá tên, mô tả và schema input/output của từng tool trong danh sách khả năng của chúng.

• **Resources**: Đây là các mục dữ liệu chỉ đọc hoặc tài liệu mà một Máy chủ MCP có thể cung cấp, và clients có thể lấy chúng theo nhu cầu. Ví dụ gồm nội dung file, bản ghi cơ sở dữ liệu hoặc file log. Resources có thể là văn bản (như mã hoặc JSON) hoặc nhị phân (như hình ảnh hoặc PDF).

• **Prompts**: Đây là các mẫu được định nghĩa trước cung cấp các gợi ý, cho phép các workflow phức tạp hơn.

### Lợi ích của MCP

MCP mang lại những lợi thế đáng kể cho các AI Agents:

• **Khám phá Công cụ Động**: Các tác nhân có thể nhận danh sách các công cụ có sẵn từ một server cùng với mô tả về chức năng của chúng. Điều này trái ngược với API truyền thống, vốn thường yêu cầu mã tĩnh để tích hợp, nghĩa là bất kỳ thay đổi API nào đều cần cập nhật mã. MCP cung cấp cách "tích hợp một lần", dẫn đến tính thích ứng cao hơn.

• **Tương tác liên mô hình (Interoperability Across LLMs)**: MCP hoạt động qua các LLM khác nhau, cung cấp sự linh hoạt để thay đổi mô hình lõi nhằm đánh giá hiệu suất tốt hơn.

• **Bảo mật Chuẩn hóa**: MCP bao gồm một phương thức xác thực tiêu chuẩn, cải thiện khả năng mở rộng khi thêm quyền truy cập tới các máy chủ MCP bổ sung. Điều này đơn giản hơn so với việc quản lý các khóa và kiểu xác thực khác nhau cho nhiều API truyền thống.

### Ví dụ MCP

![Sơ đồ MCP](../../../translated_images/vi/mcp-diagram.e4ca1cbd551444a1.webp)

Hãy tưởng tượng một người dùng muốn đặt vé máy bay bằng một trợ lý AI sử dụng MCP.

1. **Kết nối**: Trợ lý AI (MCP client) kết nối tới một Máy chủ MCP do một hãng hàng không cung cấp.

2. **Khám phá Công cụ**: Client hỏi Máy chủ MCP của hãng hàng không, "Bạn có những công cụ nào?" Server phản hồi với các công cụ như "search flights" và "book flights".

3. **Gọi Công cụ**: Bạn sau đó yêu cầu trợ lý AI, "Hãy tìm chuyến bay từ Portland đến Honolulu." Trợ lý AI, sử dụng LLM của nó, xác định rằng cần gọi công cụ "search flights" và truyền các tham số liên quan (sân bay đi, điểm đến) tới Máy chủ MCP.

4. **Thực thi và Phản hồi**: Máy chủ MCP, đóng vai bọc (wrapper), thực hiện cuộc gọi thực tế tới API đặt vé nội bộ của hãng hàng không. Nó sau đó nhận thông tin chuyến bay (ví dụ dữ liệu JSON) và gửi lại cho trợ lý AI.

5. **Tương tác Tiếp theo**: Trợ lý AI trình bày các lựa chọn chuyến bay. Khi bạn chọn một chuyến bay, trợ lý có thể gọi công cụ "book flight" trên cùng Máy chủ MCP, hoàn tất việc đặt vé.

## Giao thức Agent-to-Agent (A2A)

Trong khi MCP tập trung vào việc kết nối LLMs với công cụ, giao thức **Agent-to-Agent (A2A)** tiến thêm một bước bằng cách cho phép giao tiếp và hợp tác giữa các tác nhân AI khác nhau. A2A kết nối các tác nhân AI giữa các tổ chức, môi trường và ngăn xếp công nghệ khác nhau để hoàn thành một nhiệm vụ chung.

Chúng ta sẽ xem xét các thành phần và lợi ích của A2A, cùng với một ví dụ về cách nó có thể được áp dụng trong ứng dụng du lịch của chúng ta.

### Thành phần cốt lõi của A2A

A2A tập trung vào việc cho phép giao tiếp giữa các tác nhân và để chúng cùng làm việc nhằm hoàn thành một nhiệm vụ phụ của người dùng. Mỗi thành phần của giao thức đóng góp vào điều này:

#### Agent Card

Tương tự như cách một máy chủ MCP chia sẻ danh sách công cụ, một Agent Card có:
- Tên của Agent.
- Một **mô tả các nhiệm vụ chung** mà nó hoàn thành.
- Một **danh sách các kỹ năng cụ thể** với mô tả để giúp các tác nhân khác (hoặc cả người dùng) hiểu khi nào và tại sao họ muốn gọi tác nhân đó.
- **URL Endpoint hiện tại** của tác nhân
- **Phiên bản** và **khả năng** của tác nhân như streaming responses và push notifications.

#### Agent Executor

Agent Executor chịu trách nhiệm **truyền ngữ cảnh của cuộc trò chuyện người dùng tới tác nhân từ xa**, tác nhân từ xa cần điều này để hiểu nhiệm vụ cần hoàn thành. Trong một server A2A, một tác nhân sử dụng chính Large Language Model (LLM) của mình để phân tích yêu cầu đến và thực thi các nhiệm vụ bằng các công cụ nội bộ của chính nó.

#### Artifact

Khi một tác nhân từ xa đã hoàn thành nhiệm vụ được yêu cầu, sản phẩm công việc của nó được tạo thành một artifact. Một artifact **chứa kết quả công việc của tác nhân**, một **mô tả về những gì đã được hoàn thành**, và **ngữ cảnh văn bản** được gửi qua giao thức. Sau khi artifact được gửi, kết nối với tác nhân từ xa được đóng cho đến khi cần lại.

#### Event Queue

Thành phần này được dùng để **xử lý các cập nhật và truyền tin nhắn**. Nó đặc biệt quan trọng trong môi trường production cho các hệ thống agentic để ngăn kết nối giữa các tác nhân bị đóng trước khi nhiệm vụ hoàn tất, đặc biệt khi thời gian hoàn thành nhiệm vụ có thể kéo dài.

### Lợi ích của A2A

• **Tăng cường Hợp tác**: Nó cho phép các tác nhân từ các nhà cung cấp và nền tảng khác nhau tương tác, chia sẻ ngữ cảnh và làm việc cùng nhau, tạo điều kiện tự động hóa liền mạch qua các hệ thống vốn trước đây không kết nối.

• **Linh hoạt Trong Việc Chọn Mô hình**: Mỗi tác nhân A2A có thể quyết định LLM mà nó sử dụng để phục vụ các yêu cầu, cho phép tối ưu hóa hoặc tinh chỉnh mô hình theo từng tác nhân, khác với việc chỉ có một kết nối LLM trong một số kịch bản MCP.

• **Xác thực Tích hợp sẵn**: Xác thực được tích hợp trực tiếp vào giao thức A2A, cung cấp một khung bảo mật vững chắc cho các tương tác giữa các tác nhân.

### Ví dụ A2A

![Sơ đồ A2A](../../../translated_images/vi/A2A-Diagram.8666928d648acc26.webp)

Hãy mở rộng tình huống đặt chuyến du lịch của chúng ta, nhưng lần này sử dụng A2A.

1. **Yêu cầu của Người dùng tới Multi-Agent**: Một người dùng tương tác với một client/agent "Travel Agent" A2A, có thể bằng cách nói, "Hãy đặt toàn bộ chuyến đi tới Honolulu cho tuần tới, bao gồm vé máy bay, khách sạn và thuê xe."

2. **Điều phối bởi Travel Agent**: Travel Agent nhận yêu cầu phức tạp này. Nó sử dụng LLM của mình để suy luận về nhiệm vụ và xác định rằng cần tương tác với các tác nhân chuyên môn khác.

3. **Giao tiếp Liên-tác vụ**: Travel Agent sau đó sử dụng giao thức A2A để kết nối với các tác nhân hạ nguồn, chẳng hạn như "Airline Agent", "Hotel Agent" và "Car Rental Agent" được tạo bởi các công ty khác nhau.

4. **Ủy nhiệm Thực thi Nhiệm vụ**: Travel Agent gửi các nhiệm vụ cụ thể tới các tác nhân chuyên môn này (ví dụ, "Find flights to Honolulu", "Book a hotel", "Rent a car"). Mỗi tác nhân chuyên môn này, chạy LLM riêng và sử dụng công cụ của chính họ (có thể là các máy chủ MCP), thực hiện phần công việc cụ thể của mình trong việc đặt dịch vụ.

5. **Phản hồi Tổng hợp**: Khi tất cả các tác nhân hạ nguồn hoàn thành nhiệm vụ, Travel Agent tổng hợp kết quả (chi tiết chuyến bay, xác nhận khách sạn, đặt thuê xe) và gửi một phản hồi phong cách chat toàn diện trở lại cho người dùng.

## Natural Language Web (NLWeb)

Các trang web từ lâu là cách chính để người dùng truy cập thông tin và dữ liệu trên internet.

Hãy xem các thành phần khác nhau của NLWeb, lợi ích của NLWeb và một ví dụ về cách NLWeb hoạt động bằng cách nhìn vào ứng dụng du lịch của chúng ta.

### Các thành phần của NLWeb

- **NLWeb Application (Core Service Code)**: Hệ thống xử lý các câu hỏi bằng ngôn ngữ tự nhiên. Nó kết nối các phần khác nhau của nền tảng để tạo phản hồi. Bạn có thể coi nó như **động cơ vận hành các tính năng ngôn ngữ tự nhiên** của một trang web.

- **NLWeb Protocol**: Đây là **tập quy tắc cơ bản cho tương tác ngôn ngữ tự nhiên** với một trang web. Nó trả về phản hồi ở định dạng JSON (thường sử dụng Schema.org). Mục đích của nó là tạo nền tảng đơn giản cho “AI Web”, tương tự cách HTML cho phép chia sẻ tài liệu trực tuyến.

- **MCP Server (Model Context Protocol Endpoint)**: Mỗi thiết lập NLWeb cũng hoạt động như một **MCP server**. Điều này có nghĩa là nó có thể **chia sẻ các công cụ (như phương thức “ask”) và dữ liệu** với các hệ thống AI khác. Trong thực tế, điều này làm cho nội dung và khả năng của trang web trở nên có thể sử dụng bởi các tác nhân AI, cho phép trang web trở thành một phần của “hệ sinh thái tác nhân” rộng lớn hơn.

- **Embedding Models**: Các mô hình này được dùng để **chuyển nội dung trang web thành các biểu diễn số gọi là vectors** (embeddings). Các vectors này nắm bắt ý nghĩa theo cách mà máy tính có thể so sánh và tìm kiếm. Chúng được lưu trữ trong một cơ sở dữ liệu đặc biệt, và người dùng có thể chọn mô hình embedding mà họ muốn sử dụng.

- **Vector Database (Retrieval Mechanism)**: Cơ sở dữ liệu này **lưu trữ embeddings của nội dung trang web**. Khi ai đó đặt câu hỏi, NLWeb kiểm tra cơ sở dữ liệu vector để nhanh chóng tìm thông tin phù hợp nhất. Nó đưa ra một danh sách câu trả lời khả dĩ, được xếp hạng theo độ tương tự. NLWeb làm việc với các hệ thống lưu trữ vector khác nhau như Qdrant, Snowflake, Milvus, Azure AI Search và Elasticsearch.

### NLWeb qua ví dụ

![NLWeb](../../../translated_images/vi/nlweb-diagram.c1e2390b310e5fe4.webp)

Hãy xét lại trang web đặt chuyến du lịch của chúng ta, nhưng lần này nó được hỗ trợ bởi NLWeb.

1. **Nhập dữ liệu**: Các catalog sản phẩm hiện có của trang web du lịch (ví dụ, danh sách chuyến bay, mô tả khách sạn, gói tour) được định dạng bằng Schema.org hoặc tải qua RSS feeds. Các công cụ của NLWeb nhập dữ liệu có cấu trúc này, tạo embeddings và lưu chúng vào cơ sở dữ liệu vector cục bộ hoặc từ xa.

2. **Truy vấn bằng Ngôn ngữ Tự nhiên (Người dùng)**: Một người dùng truy cập trang web và, thay vì điều hướng qua menu, gõ vào giao diện chat: "Tìm cho tôi một khách sạn phù hợp cho gia đình ở Honolulu có hồ bơi cho tuần tới".

3. **Xử lý bởi NLWeb**: Ứng dụng NLWeb nhận truy vấn này. Nó gửi truy vấn tới một LLM để hiểu và đồng thời tìm kiếm trong cơ sở dữ liệu vector của nó các danh sách khách sạn liên quan.

4. **Kết quả Chính xác**: LLM giúp diễn giải các kết quả tìm kiếm từ cơ sở dữ liệu, xác định các kết quả phù hợp nhất dựa trên tiêu chí "phù hợp cho gia đình", "hồ bơi" và "Honolulu", rồi định dạng một phản hồi bằng ngôn ngữ tự nhiên. Quan trọng là, phản hồi tham chiếu tới các khách sạn thực tế trong catalog của trang web, tránh việc bịa đặt thông tin.

5. **Tương tác với AI Agent**: Bởi vì NLWeb hoạt động như một MCP server, một tác nhân du lịch AI bên ngoài cũng có thể kết nối tới instance NLWeb của trang web này. AI agent có thể sử dụng phương thức `ask` của MCP để truy vấn trực tiếp trang web: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. Instance NLWeb sẽ xử lý điều này, khai thác cơ sở dữ liệu thông tin nhà hàng của nó (nếu đã được tải), và trả về một phản hồi có cấu trúc JSON.

### Còn câu hỏi về MCP/A2A/NLWeb?

Tham gia [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ những người học khác, tham dự giờ làm việc và nhận trả lời cho các câu hỏi về AI Agents của bạn.

## Tài nguyên

- [MCP cho Người mới bắt đầu](https://aka.ms/mcp-for-beginners)  
- [Tài liệu MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Tuyên bố miễn trừ trách nhiệm:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi nỗ lực để đảm bảo tính chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn chính thức. Đối với những thông tin quan trọng, nên sử dụng bản dịch chuyên nghiệp do người dịch thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->