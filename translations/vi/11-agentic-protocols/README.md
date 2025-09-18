<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T15:15:44+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "vi"
}
-->
# Sử dụng Các Giao Thức Agentic (MCP, A2A và NLWeb)

[![Agentic Protocols](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.vi.png)](https://youtu.be/X-Dh9R3Opn8)

> _(Nhấp vào hình ảnh trên để xem video của bài học này)_

Khi việc sử dụng các tác nhân AI ngày càng phát triển, nhu cầu về các giao thức đảm bảo tiêu chuẩn hóa, bảo mật và hỗ trợ đổi mới mở cũng tăng lên. Trong bài học này, chúng ta sẽ tìm hiểu 3 giao thức nhằm đáp ứng nhu cầu này - Model Context Protocol (MCP), Agent to Agent (A2A) và Natural Language Web (NLWeb).

## Giới thiệu

Trong bài học này, chúng ta sẽ tìm hiểu:

• Cách **MCP** cho phép các tác nhân AI truy cập công cụ và dữ liệu bên ngoài để hoàn thành nhiệm vụ của người dùng.

• Cách **A2A** hỗ trợ giao tiếp và hợp tác giữa các tác nhân AI khác nhau.

• Cách **NLWeb** mang giao diện ngôn ngữ tự nhiên đến bất kỳ trang web nào, cho phép các tác nhân AI khám phá và tương tác với nội dung.

## Mục tiêu học tập

• **Xác định** mục đích cốt lõi và lợi ích của MCP, A2A và NLWeb trong bối cảnh các tác nhân AI.

• **Giải thích** cách mỗi giao thức hỗ trợ giao tiếp và tương tác giữa LLMs, công cụ và các tác nhân khác.

• **Nhận biết** vai trò riêng biệt của từng giao thức trong việc xây dựng các hệ thống tác nhân phức tạp.

## Model Context Protocol

**Model Context Protocol (MCP)** là một tiêu chuẩn mở cung cấp cách thức tiêu chuẩn hóa để các ứng dụng cung cấp ngữ cảnh và công cụ cho LLMs. Điều này cho phép một "bộ chuyển đổi phổ quát" kết nối với các nguồn dữ liệu và công cụ khác nhau mà các tác nhân AI có thể sử dụng một cách nhất quán.

Hãy cùng tìm hiểu các thành phần của MCP, lợi ích so với việc sử dụng API trực tiếp, và một ví dụ về cách các tác nhân AI có thể sử dụng máy chủ MCP.

### Các thành phần cốt lõi của MCP

MCP hoạt động trên kiến trúc **client-server** và các thành phần cốt lõi bao gồm:

• **Hosts** là các ứng dụng LLM (ví dụ như trình chỉnh sửa mã như VSCode) bắt đầu kết nối với máy chủ MCP.

• **Clients** là các thành phần trong ứng dụng host duy trì kết nối một-một với các máy chủ.

• **Servers** là các chương trình nhẹ cung cấp các khả năng cụ thể.

Giao thức bao gồm ba nguyên thủy cốt lõi, đó là các khả năng của máy chủ MCP:

• **Tools**: Đây là các hành động hoặc chức năng riêng lẻ mà một tác nhân AI có thể gọi để thực hiện một hành động. Ví dụ, một dịch vụ thời tiết có thể cung cấp công cụ "get weather", hoặc một máy chủ thương mại điện tử có thể cung cấp công cụ "purchase product". Các máy chủ MCP quảng cáo tên, mô tả và schema đầu vào/đầu ra của từng công cụ trong danh sách khả năng của họ.

• **Resources**: Đây là các mục dữ liệu hoặc tài liệu chỉ đọc mà máy chủ MCP có thể cung cấp, và các client có thể truy xuất theo yêu cầu. Ví dụ bao gồm nội dung tệp, bản ghi cơ sở dữ liệu hoặc tệp nhật ký. Resources có thể là văn bản (như mã hoặc JSON) hoặc nhị phân (như hình ảnh hoặc PDF).

• **Prompts**: Đây là các mẫu được định sẵn cung cấp các gợi ý, cho phép thực hiện các quy trình làm việc phức tạp hơn.

### Lợi ích của MCP

MCP mang lại những lợi ích đáng kể cho các tác nhân AI:

• **Khám phá công cụ động**: Các tác nhân có thể nhận danh sách các công cụ có sẵn từ máy chủ cùng với mô tả về chức năng của chúng. Điều này khác với API truyền thống, thường yêu cầu mã hóa tĩnh để tích hợp, nghĩa là bất kỳ thay đổi nào trong API đều cần cập nhật mã. MCP cung cấp cách tiếp cận "tích hợp một lần", dẫn đến khả năng thích ứng cao hơn.

• **Khả năng tương tác giữa các LLMs**: MCP hoạt động trên các LLM khác nhau, cung cấp sự linh hoạt để chuyển đổi mô hình cốt lõi nhằm đánh giá hiệu suất tốt hơn.

• **Bảo mật tiêu chuẩn hóa**: MCP bao gồm phương pháp xác thực tiêu chuẩn, cải thiện khả năng mở rộng khi thêm quyền truy cập vào các máy chủ MCP bổ sung. Điều này đơn giản hơn so với việc quản lý các khóa và loại xác thực khác nhau cho các API truyền thống.

### Ví dụ về MCP

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.vi.png)

Hãy tưởng tượng một người dùng muốn đặt vé máy bay bằng trợ lý AI được hỗ trợ bởi MCP.

1. **Kết nối**: Trợ lý AI (client MCP) kết nối với máy chủ MCP do một hãng hàng không cung cấp.

2. **Khám phá công cụ**: Client hỏi máy chủ MCP của hãng hàng không, "Bạn có những công cụ nào?" Máy chủ trả lời với các công cụ như "search flights" và "book flights".

3. **Gọi công cụ**: Sau đó, bạn yêu cầu trợ lý AI, "Vui lòng tìm chuyến bay từ Portland đến Honolulu." Trợ lý AI, sử dụng LLM của mình, xác định rằng cần gọi công cụ "search flights" và truyền các tham số liên quan (điểm xuất phát, điểm đến) đến máy chủ MCP.

4. **Thực thi và phản hồi**: Máy chủ MCP, hoạt động như một lớp bao bọc, thực hiện cuộc gọi thực tế đến API đặt vé nội bộ của hãng hàng không. Sau đó, nhận thông tin chuyến bay (ví dụ: dữ liệu JSON) và gửi lại cho trợ lý AI.

5. **Tương tác tiếp theo**: Trợ lý AI trình bày các tùy chọn chuyến bay. Khi bạn chọn một chuyến bay, trợ lý có thể gọi công cụ "book flight" trên cùng máy chủ MCP, hoàn tất việc đặt vé.

## Giao Thức Agent-to-Agent (A2A)

Trong khi MCP tập trung vào việc kết nối LLMs với công cụ, **Agent-to-Agent (A2A)** tiến xa hơn bằng cách cho phép giao tiếp và hợp tác giữa các tác nhân AI khác nhau. A2A kết nối các tác nhân AI trên các tổ chức, môi trường và nền tảng công nghệ khác nhau để hoàn thành một nhiệm vụ chung.

Chúng ta sẽ xem xét các thành phần và lợi ích của A2A, cùng với một ví dụ về cách nó có thể được áp dụng trong ứng dụng du lịch của chúng ta.

### Các thành phần cốt lõi của A2A

A2A tập trung vào việc cho phép giao tiếp giữa các tác nhân và để họ làm việc cùng nhau để hoàn thành một nhiệm vụ phụ của người dùng. Mỗi thành phần của giao thức đóng góp vào điều này:

#### Agent Card

Tương tự như cách một máy chủ MCP chia sẻ danh sách công cụ, một Agent Card có:

- Tên của tác nhân.  
- **Mô tả về các nhiệm vụ chung** mà nó hoàn thành.  
- **Danh sách các kỹ năng cụ thể** với mô tả để giúp các tác nhân khác (hoặc thậm chí người dùng) hiểu khi nào và tại sao họ muốn gọi tác nhân đó.  
- **URL Endpoint hiện tại** của tác nhân.  
- **Phiên bản** và **khả năng** của tác nhân như phản hồi streaming và thông báo đẩy.  

#### Agent Executor

Agent Executor chịu trách nhiệm **truyền ngữ cảnh của cuộc trò chuyện người dùng đến tác nhân từ xa**, tác nhân từ xa cần điều này để hiểu nhiệm vụ cần hoàn thành. Trong một máy chủ A2A, một tác nhân sử dụng LLM của riêng mình để phân tích yêu cầu đến và thực hiện nhiệm vụ bằng các công cụ nội bộ của nó.

#### Artifact

Khi một tác nhân từ xa hoàn thành nhiệm vụ được yêu cầu, sản phẩm công việc của nó được tạo thành một artifact. Artifact **chứa kết quả công việc của tác nhân**, **mô tả những gì đã được hoàn thành**, và **ngữ cảnh văn bản** được gửi qua giao thức. Sau khi artifact được gửi, kết nối với tác nhân từ xa sẽ bị đóng cho đến khi cần lại.

#### Event Queue

Thành phần này được sử dụng để **xử lý cập nhật và truyền tin nhắn**. Nó đặc biệt quan trọng trong sản xuất cho các hệ thống tác nhân để ngăn kết nối giữa các tác nhân bị đóng trước khi nhiệm vụ hoàn thành, đặc biệt khi thời gian hoàn thành nhiệm vụ có thể kéo dài.

### Lợi ích của A2A

• **Hợp tác nâng cao**: Nó cho phép các tác nhân từ các nhà cung cấp và nền tảng khác nhau tương tác, chia sẻ ngữ cảnh và làm việc cùng nhau, tạo điều kiện tự động hóa liền mạch giữa các hệ thống truyền thống không kết nối.  

• **Linh hoạt trong lựa chọn mô hình**: Mỗi tác nhân A2A có thể quyết định sử dụng LLM nào để xử lý yêu cầu của nó, cho phép tối ưu hóa hoặc tinh chỉnh mô hình theo từng tác nhân, không giống như kết nối LLM đơn lẻ trong một số trường hợp MCP.  

• **Xác thực tích hợp**: Xác thực được tích hợp trực tiếp vào giao thức A2A, cung cấp một khung bảo mật mạnh mẽ cho các tương tác giữa các tác nhân.  

### Ví dụ về A2A

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.vi.png)

Hãy mở rộng kịch bản đặt vé du lịch của chúng ta, nhưng lần này sử dụng A2A.

1. **Yêu cầu của người dùng đến Multi-Agent**: Một người dùng tương tác với một "Travel Agent" A2A client/agent, có thể bằng cách nói, "Vui lòng đặt toàn bộ chuyến đi đến Honolulu vào tuần tới, bao gồm vé máy bay, khách sạn và xe thuê."

2. **Điều phối bởi Travel Agent**: Travel Agent nhận yêu cầu phức tạp này. Nó sử dụng LLM của mình để suy luận về nhiệm vụ và xác định rằng cần tương tác với các tác nhân chuyên biệt khác.

3. **Giao tiếp giữa các tác nhân**: Travel Agent sau đó sử dụng giao thức A2A để kết nối với các tác nhân hạ nguồn, chẳng hạn như "Airline Agent," "Hotel Agent," và "Car Rental Agent" được tạo bởi các công ty khác nhau.

4. **Thực hiện nhiệm vụ được ủy quyền**: Travel Agent gửi các nhiệm vụ cụ thể đến các tác nhân chuyên biệt này (ví dụ: "Tìm chuyến bay đến Honolulu," "Đặt khách sạn," "Thuê xe"). Mỗi tác nhân chuyên biệt này, chạy LLM của riêng mình và sử dụng các công cụ riêng (có thể là các máy chủ MCP), thực hiện phần cụ thể của việc đặt vé.

5. **Phản hồi hợp nhất**: Khi tất cả các tác nhân hạ nguồn hoàn thành nhiệm vụ của họ, Travel Agent tổng hợp kết quả (chi tiết chuyến bay, xác nhận khách sạn, đặt xe thuê) và gửi phản hồi toàn diện, kiểu trò chuyện, trở lại cho người dùng.

## Natural Language Web (NLWeb)

Các trang web từ lâu đã là cách chính để người dùng truy cập thông tin và dữ liệu trên internet.

Hãy cùng tìm hiểu các thành phần khác nhau của NLWeb, lợi ích của NLWeb và một ví dụ về cách NLWeb hoạt động bằng cách xem xét ứng dụng du lịch của chúng ta.

### Các thành phần của NLWeb

- **Ứng dụng NLWeb (Mã dịch vụ cốt lõi)**: Hệ thống xử lý các câu hỏi ngôn ngữ tự nhiên. Nó kết nối các phần khác nhau của nền tảng để tạo phản hồi. Bạn có thể nghĩ nó như **động cơ cung cấp các tính năng ngôn ngữ tự nhiên** của một trang web.

- **Giao thức NLWeb**: Đây là **bộ quy tắc cơ bản cho tương tác ngôn ngữ tự nhiên** với một trang web. Nó gửi phản hồi dưới dạng JSON (thường sử dụng Schema.org). Mục đích của nó là tạo nền tảng đơn giản cho “AI Web,” giống như cách HTML làm cho việc chia sẻ tài liệu trực tuyến trở nên khả thi.

- **Máy chủ MCP (Điểm cuối Model Context Protocol)**: Mỗi thiết lập NLWeb cũng hoạt động như một **máy chủ MCP**. Điều này có nghĩa là nó có thể **chia sẻ công cụ (như phương pháp “ask”) và dữ liệu** với các hệ thống AI khác. Trong thực tế, điều này làm cho nội dung và khả năng của trang web có thể sử dụng bởi các tác nhân AI, cho phép trang web trở thành một phần của “hệ sinh thái tác nhân” rộng lớn hơn.

- **Mô hình nhúng**: Các mô hình này được sử dụng để **chuyển đổi nội dung trang web thành các biểu diễn số gọi là vectors** (nhúng). Các vectors này nắm bắt ý nghĩa theo cách mà máy tính có thể so sánh và tìm kiếm. Chúng được lưu trữ trong một cơ sở dữ liệu đặc biệt, và người dùng có thể chọn mô hình nhúng mà họ muốn sử dụng.

- **Cơ sở dữ liệu vector (Cơ chế truy xuất)**: Cơ sở dữ liệu này **lưu trữ các vectors của nội dung trang web**. Khi ai đó đặt câu hỏi, NLWeb kiểm tra cơ sở dữ liệu vector để nhanh chóng tìm thông tin phù hợp nhất. Nó cung cấp danh sách các câu trả lời khả thi, được xếp hạng theo mức độ tương đồng. NLWeb hoạt động với các hệ thống lưu trữ vector khác nhau như Qdrant, Snowflake, Milvus, Azure AI Search, và Elasticsearch.

### NLWeb qua ví dụ

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.vi.png)

Hãy xem xét trang web đặt vé du lịch của chúng ta, nhưng lần này được hỗ trợ bởi NLWeb.

1. **Thu thập dữ liệu**: Các danh mục sản phẩm hiện có của trang web du lịch (ví dụ: danh sách chuyến bay, mô tả khách sạn, gói tour) được định dạng bằng Schema.org hoặc tải qua RSS feeds. Các công cụ của NLWeb thu thập dữ liệu có cấu trúc này, tạo nhúng, và lưu trữ chúng trong cơ sở dữ liệu vector cục bộ hoặc từ xa.

2. **Truy vấn ngôn ngữ tự nhiên (Người dùng)**: Một người dùng truy cập trang web và, thay vì điều hướng menu, nhập vào giao diện trò chuyện: "Tìm cho tôi một khách sạn thân thiện với gia đình ở Honolulu có hồ bơi vào tuần tới".

3. **Xử lý NLWeb**: Ứng dụng NLWeb nhận truy vấn này. Nó gửi truy vấn đến một LLM để hiểu và đồng thời tìm kiếm cơ sở dữ liệu vector của mình để tìm danh sách khách sạn phù hợp.

4. **Kết quả chính xác**: LLM giúp diễn giải kết quả tìm kiếm từ cơ sở dữ liệu, xác định các kết quả phù hợp nhất dựa trên tiêu chí "thân thiện với gia đình," "hồ bơi," và "Honolulu," sau đó định dạng phản hồi ngôn ngữ tự nhiên. Quan trọng là, phản hồi này đề cập đến các khách sạn thực tế từ danh mục của trang web, tránh thông tin bịa đặt.

5. **Tương tác với tác nhân AI**: Vì NLWeb hoạt động như một máy chủ MCP, một tác nhân AI du lịch bên ngoài cũng có thể kết nối với phiên bản NLWeb của trang web này. Tác nhân AI có thể sử dụng phương pháp `ask` của MCP để truy vấn trực tiếp trang web: `ask("Có nhà hàng nào thân thiện với người ăn chay ở khu vực Honolulu được khách sạn đề xuất không?")`. Phiên bản NLWeb sẽ xử lý điều này, tận dụng cơ sở dữ liệu thông tin nhà hàng của mình (nếu được tải), và trả về phản hồi JSON có cấu trúc.

### Có thêm câu hỏi về MCP/A2A/NLWeb?

Tham gia [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ các học viên khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về tác nhân AI của bạn.

## Tài nguyên

- [MCP cho người mới bắt đầu](https://aka.ms/mcp-for-beginners)  
- [Tài liệu MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Kho lưu trữ NLWeb](https://github.com/nlweb-ai/NLWeb)  
- [Hướng dẫn Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)  

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.