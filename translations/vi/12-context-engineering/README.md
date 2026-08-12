# Kỹ Thuật Ngữ Cảnh cho Đại Lý AI

[![Kỹ Thuật Ngữ Cảnh](../../../translated_images/vi/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Nhấp vào hình ảnh trên để xem video bài học này)_

Hiểu được độ phức tạp của ứng dụng mà bạn đang xây dựng đại lý AI là điều quan trọng để tạo ra một đại lý đáng tin cậy. Chúng ta cần xây dựng các Đại Lý AI quản lý thông tin một cách hiệu quả để đáp ứng các nhu cầu phức tạp vượt ra ngoài kỹ thuật tạo lời nhắc (prompt engineering).

Trong bài học này, chúng ta sẽ xem xét kỹ thuật ngữ cảnh là gì và vai trò của nó trong việc xây dựng đại lý AI.

## Giới thiệu

Bài học này sẽ trình bày:

• **Kỹ thuật ngữ cảnh là gì** và tại sao nó khác với kỹ thuật tạo lời nhắc.

• **Các chiến lược cho kỹ thuật ngữ cảnh hiệu quả**, bao gồm cách viết, chọn lọc, nén, và cô lập thông tin.

• **Các thất bại phổ biến về ngữ cảnh** có thể làm lệch hướng đại lý AI của bạn và cách để sửa chúng.

## Mục tiêu học tập

Sau khi hoàn thành bài học, bạn sẽ hiểu được cách:

• **Định nghĩa kỹ thuật ngữ cảnh** và phân biệt nó với kỹ thuật tạo lời nhắc.

• **Xác định các thành phần chính của ngữ cảnh** trong các ứng dụng mô hình ngôn ngữ lớn (LLM).

• **Áp dụng các chiến lược viết, chọn lọc, nén và cô lập ngữ cảnh** để cải thiện hiệu suất đại lý.

• **Nhận diện các thất bại phổ biến về ngữ cảnh** như nhiễm độc, xao nhãng, nhầm lẫn và xung đột, và thực hiện các kỹ thuật giảm thiểu.

## Kỹ thuật ngữ cảnh là gì?

Đối với các Đại Lý AI, ngữ cảnh là yếu tố thúc đẩy việc lập kế hoạch để đại lý AI thực hiện một hành động nào đó. Kỹ thuật ngữ cảnh là thực hành đảm bảo đại lý AI có thông tin đúng để hoàn thành bước tiếp theo của nhiệm vụ. Cửa sổ ngữ cảnh có kích thước giới hạn, vì vậy là người xây dựng đại lý, chúng ta cần tạo ra các hệ thống và quy trình để quản lý việc thêm, loại bỏ và cô đọng thông tin trong cửa sổ ngữ cảnh.

### Kỹ thuật tạo lời nhắc vs Kỹ thuật ngữ cảnh

Kỹ thuật tạo lời nhắc tập trung vào một bộ hướng dẫn tĩnh đơn lẻ để hướng dẫn đại lý AI một cách hiệu quả bằng một tập hợp các quy tắc. Kỹ thuật ngữ cảnh là cách quản lý một tập hợp thông tin động, bao gồm lời nhắc ban đầu, để đảm bảo đại lý AI có những gì cần thiết theo thời gian. Ý tưởng chính của kỹ thuật ngữ cảnh là làm cho quá trình này trở nên lặp lại và đáng tin cậy.

### Các loại ngữ cảnh

[![Các loại ngữ cảnh](../../../translated_images/vi/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Cần nhớ rằng ngữ cảnh không chỉ là một thứ duy nhất. Thông tin mà đại lý AI cần có thể đến từ nhiều nguồn khác nhau và chúng ta phải đảm bảo đại lý có quyền truy cập vào các nguồn này:

Các loại ngữ cảnh mà một đại lý AI có thể cần quản lý bao gồm:

• **Hướng dẫn:** Giống như "quy tắc" của đại lý – lời nhắc, tin nhắn hệ thống, ví dụ ít mẫu (giúp AI biết cách làm điều gì đó), và mô tả các công cụ mà nó có thể sử dụng. Đây là nơi kỹ thuật tạo lời nhắc kết hợp với kỹ thuật ngữ cảnh.

• **Kiến thức:** Bao gồm các sự kiện, thông tin lấy từ cơ sở dữ liệu, hoặc ký ức dài hạn mà đại lý đã tích lũy. Điều này bao gồm việc tích hợp hệ thống Tăng cường Truy xuất (Retrieval Augmented Generation - RAG) nếu đại lý cần truy cập vào các kho kiến thức và cơ sở dữ liệu khác nhau.

• **Công cụ:** Đây là định nghĩa các chức năng bên ngoài, API và Máy chủ MCP mà đại lý có thể gọi, cùng với phản hồi (kết quả) mà nó nhận được khi sử dụng chúng.

• **Lịch sử hội thoại:** Cuộc đối thoại đang diễn ra với người dùng. Khi thời gian trôi đi, các cuộc hội thoại này trở nên dài hơn và phức tạp hơn, điều này làm chiếm không gian trong cửa sổ ngữ cảnh.

• **Sở thích người dùng:** Thông tin được học về sở thích hoặc không thích của người dùng theo thời gian. Những thông tin này có thể được lưu trữ và sử dụng khi đưa ra các quyết định quan trọng để hỗ trợ người dùng.

## Các chiến lược cho kỹ thuật ngữ cảnh hiệu quả

### Chiến lược lập kế hoạch

[![Thực tiễn tốt nhất cho kỹ thuật ngữ cảnh](../../../translated_images/vi/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Kỹ thuật ngữ cảnh tốt bắt đầu với lập kế hoạch tốt. Dưới đây là một cách tiếp cận giúp bạn bắt đầu suy nghĩ về cách áp dụng khái niệm kỹ thuật ngữ cảnh:

1. **Xác định kết quả rõ ràng** - Kết quả của các nhiệm vụ mà Đại Lý AI sẽ được giao nên được xác định rõ ràng. Trả lời câu hỏi - "Thế giới sẽ trông như thế nào khi Đại Lý AI hoàn thành nhiệm vụ?" Nói cách khác, sự thay đổi, thông tin hoặc phản hồi người dùng sẽ nhận được sau khi tương tác với Đại Lý AI.
2. **Lập bản đồ ngữ cảnh** - Khi bạn đã xác định kết quả của Đại Lý AI, bạn cần trả lời câu hỏi "Đại Lý AI cần những thông tin gì để hoàn thành nhiệm vụ này?". Bằng cách này, bạn có thể bắt đầu lập bản đồ ngữ cảnh nơi mà thông tin đó có thể nằm.
3. **Tạo các đường dẫn ngữ cảnh** - Bây giờ bạn biết được nơi thông tin nằm, bạn cần trả lời câu hỏi "Làm thế nào Đại Lý sẽ lấy được thông tin này?". Việc này có thể được thực hiện theo nhiều cách khác nhau bao gồm RAG, sử dụng máy chủ MCP và các công cụ khác.

### Chiến lược thực tế

Lập kế hoạch là quan trọng nhưng khi thông tin bắt đầu chảy vào cửa sổ ngữ cảnh của đại lý, chúng ta cần có các chiến lược thực tế để quản lý nó:

#### Quản lý ngữ cảnh

Trong khi một số thông tin sẽ được thêm vào cửa sổ ngữ cảnh tự động, kỹ thuật ngữ cảnh là việc chủ động hơn với thông tin này, điều này có thể được thực hiện bằng một số chiến lược sau:

 1. **Bảng ghi chú của đại lý**
 Điều này cho phép Đại Lý AI ghi chú lại các thông tin liên quan đến nhiệm vụ hiện tại và tương tác người dùng trong một phiên làm việc. Điều này nên tồn tại bên ngoài cửa sổ ngữ cảnh trong một tập tin hoặc đối tượng runtime mà đại lý có thể truy xuất lại trong phiên nếu cần.

 2. **Ký ức**
 Bảng ghi chú tốt cho việc quản lý thông tin bên ngoài cửa sổ ngữ cảnh của một phiên làm việc đơn lẻ. Ký ức cho phép đại lý lưu trữ và truy xuất thông tin liên quan qua nhiều phiên làm việc. Điều này có thể bao gồm tóm tắt, sở thích người dùng và phản hồi để cải thiện trong tương lai.

 3. **Nén ngữ cảnh**
  Khi cửa sổ ngữ cảnh lớn lên và gần đến giới hạn, các kỹ thuật như tóm tắt và cắt bỏ có thể được áp dụng. Điều này bao gồm giữ lại chỉ những thông tin quan trọng nhất hoặc loại bỏ các tin nhắn cũ hơn.
  
 4. **Hệ thống đa đại lý**
  Phát triển hệ thống đa đại lý là một hình thức của kỹ thuật ngữ cảnh vì mỗi đại lý có cửa sổ ngữ cảnh riêng. Cách ngữ cảnh được chia sẻ và truyền đến các đại lý khác nhau cũng là một điều cần lên kế hoạch khi xây dựng các hệ thống này.
  
 5. **Môi trường Sandbox**
  Nếu đại lý cần chạy một vài đoạn mã hoặc xử lý lượng lớn thông tin trong một tài liệu, điều này có thể tiêu tốn nhiều token để xử lý kết quả. Thay vì lưu trữ tất cả trong cửa sổ ngữ cảnh, đại lý có thể sử dụng môi trường sandbox để chạy mã này và chỉ đọc các kết quả và thông tin liên quan khác.
  
 6. **Đối tượng trạng thái runtime**
   Việc này được thực hiện bằng cách tạo các vùng chứa thông tin để quản lý khi Đại Lý cần truy cập những thông tin nhất định. Đối với nhiệm vụ phức tạp, điều này cho phép đại lý lưu trữ kết quả của từng bước nhiệm vụ con, giữ cho ngữ cảnh chỉ liên kết với nhiệm vụ con đó.

#### Kiểm tra ngữ cảnh

Sau khi áp dụng một trong những chiến lược này, xứng đáng kiểm tra xem cuộc gọi mô hình tiếp theo thực sự nhận được gì. Một câu hỏi gỡ lỗi hữu ích là:

> Đại lý đã tải quá nhiều ngữ cảnh, ngữ cảnh sai, hay thiếu ngữ cảnh cần thiết?

Bạn không cần ghi lại lời nhắc thô, đầu ra công cụ, hay nội dung ký ức để trả lời câu hỏi đó. Trong môi trường sản xuất, nên ưu tiên các bản ghi kiểm tra ngữ cảnh nhỏ, nắm bắt số lượng, id, hàm băm và nhãn chính sách:

- **Lựa chọn:** Theo dõi số lượng các đoạn dữ liệu, công cụ hoặc ký ức được xem xét, số lượng được chọn và quy tắc hoặc điểm số làm loại bỏ các mục khác.
- **Nén:** Ghi lại phạm vi nguồn hoặc id truy xuất, id tóm tắt, ước lượng số lượng token trước và sau nén, và liệu nội dung thô có bị loại khỏi cuộc gọi tiếp theo hay không.
- **Cô lập:** Ghi chú các nhiệm vụ con chạy trong đại lý, phiên hoặc sandbox riêng biệt, tóm tắt có giới hạn được trả về, và liệu đầu ra công cụ lớn có giữ bên ngoài ngữ cảnh đại lý chính.
- **Ký ức và RAG:** Lưu id tài liệu truy xuất, id ký ức, điểm số, id được chọn và trạng thái chỉnh sửa thay vì toàn bộ văn bản truy xuất.
- **An toàn và riêng tư:** Ưu tiên hàm băm, id, token bucket và nhãn chính sách hơn là văn bản lời nhắc nhạy cảm, đối số công cụ, kết quả công cụ hoặc nội dung ký ức người dùng.

Mục tiêu không phải là giữ nhiều ngữ cảnh hơn. Mà là để lại đủ bằng chứng để nhà phát triển có thể biết chiến lược ngữ cảnh nào đã chạy và liệu nó có thay đổi cuộc gọi mô hình tiếp theo theo cách mong muốn hay không.

### Ví dụ về kỹ thuật ngữ cảnh

Giả sử chúng ta muốn một đại lý AI **"Đặt cho tôi một chuyến đi đến Paris."**

• Một đại lý đơn giản chỉ sử dụng kỹ thuật tạo lời nhắc có thể chỉ phản hồi: **"Được rồi, bạn muốn đi Paris khi nào?"** Nó chỉ xử lý câu hỏi trực tiếp của bạn tại thời điểm người dùng hỏi.

• Một đại lý sử dụng các chiến lược kỹ thuật ngữ cảnh đã trình bày sẽ làm nhiều hơn thế. Trước khi phản hồi, hệ thống của nó có thể:

  ◦ **Kiểm tra lịch của bạn** để xem ngày nào có sẵn (lấy dữ liệu thời gian thực).

 ◦ **Nhớ các sở thích du lịch trước đây** (từ ký ức dài hạn) như hãng hàng không bạn ưu tiên, ngân sách, hoặc liệu bạn thích các chuyến bay thẳng.

 ◦ **Xác định các công cụ có sẵn** để đặt vé máy bay và khách sạn.

- Sau đó, một phản hồi ví dụ có thể là: "Chào [Tên của bạn]! Tôi thấy bạn rảnh vào tuần đầu tiên của tháng Mười. Tôi có nên tìm các chuyến bay thẳng đến Paris trên [Hãng hàng không ưu tiên] trong ngân sách thường lệ của bạn [Ngân sách] không?" Phản hồi giàu ngữ cảnh này thể hiện sức mạnh của kỹ thuật ngữ cảnh.

## Các thất bại phổ biến về ngữ cảnh

### Nhiễm độc ngữ cảnh

**Đó là gì:** Khi một ảo tưởng (thông tin sai lệch do LLM sinh ra) hoặc lỗi xâm nhập vào ngữ cảnh và được tham chiếu nhiều lần, khiến đại lý theo đuổi các mục tiêu không thể hoặc phát triển các chiến lược vô nghĩa.

**Cách xử lý:** Triển khai **xác nhận ngữ cảnh** và **cách ly**. Xác nhận thông tin trước khi thêm vào ký ức dài hạn. Nếu phát hiện khả năng nhiễm độc, hãy bắt đầu các luồng ngữ cảnh mới để ngăn chặn thông tin xấu lan rộng.

**Ví dụ Đặt Chuyến Bay:** Đại lý của bạn tưởng tượng ra một **chuyến bay thẳng từ sân bay địa phương nhỏ đến một thành phố quốc tế xa xôi** thực tế không có các chuyến bay quốc tế. Chi tiết chuyến bay không tồn tại này được lưu vào ngữ cảnh. Sau đó khi bạn yêu cầu đại lý đặt vé, nó liên tục cố tìm vé cho tuyến đường không thể này, dẫn đến lỗi lặp đi lặp lại.

**Giải pháp:** Thực hiện bước **xác minh sự tồn tại và lộ trình chuyến bay với API thời gian thực** _trước khi_ thêm thông tin chuyến bay vào ngữ cảnh làm việc của đại lý. Nếu xác minh không thành công, thông tin sai sẽ bị "cách ly" và không được sử dụng tiếp.

### Xao nhãng ngữ cảnh

**Đó là gì:** Khi ngữ cảnh trở nên quá lớn khiến mô hình tập trung quá mức vào lịch sử tích lũy thay vì dùng những gì đã học trong quá trình đào tạo, dẫn đến các hành động lặp đi lặp lại hoặc không hữu ích. Mô hình có thể bắt đầu sai sót ngay cả trước khi cửa sổ ngữ cảnh đầy.

**Cách xử lý:** Sử dụng **tóm tắt ngữ cảnh**. Định kỳ nén thông tin tích lũy thành các bản tóm tắt ngắn hơn, giữ lại chi tiết quan trọng trong khi loại bỏ lịch sử dư thừa. Điều này giúp "đặt lại" sự tập trung.

**Ví dụ Đặt Chuyến Bay:** Bạn đã thảo luận về nhiều điểm đến du lịch mơ ước trong một thời gian dài, bao gồm cả việc kể chi tiết chuyến đi ba lô cách đây hai năm. Khi bạn cuối cùng yêu cầu **"tìm cho tôi chuyến bay giá rẻ cho tháng tới,"** đại lý bị mắc kẹt trong các chi tiết cũ không liên quan và liên tục hỏi về đồ dùng ba lô hoặc lịch trình trước đây của bạn, bỏ qua yêu cầu hiện tại.

**Giải pháp:** Sau một số lượt đối thoại hoặc khi ngữ cảnh trở nên quá lớn, đại lý nên **tóm tắt phần gần đây và phù hợp nhất của cuộc trò chuyện** – tập trung vào ngày tháng và điểm đến hiện tại của bạn – và sử dụng bản tóm tắt cô đọng này cho lần gọi LLM tiếp theo, loại bỏ đoạn hội thoại lịch sử ít liên quan.

### Nhầm lẫn ngữ cảnh

**Đó là gì:** Khi ngữ cảnh không cần thiết, thường ở dạng quá nhiều công cụ có sẵn, khiến mô hình tạo ra câu trả lời sai hoặc gọi công cụ không liên quan. Các mô hình nhỏ hơn đặc biệt dễ bị vấn đề này.

**Cách xử lý:** Thực hiện **quản lý tải công cụ** sử dụng kỹ thuật RAG. Lưu mô tả công cụ trong cơ sở dữ liệu vector và chỉ chọn _chỉ_ những công cụ phù hợp nhất cho từng nhiệm vụ cụ thể. Nghiên cứu cho thấy giới hạn số công cụ dưới 30 là hiệu quả.

**Ví dụ Đặt Chuyến Bay:** Đại lý của bạn có quyền truy cập vào hàng chục công cụ: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations`, v.v. Bạn hỏi, **"Cách tốt nhất để đi lại ở Paris là gì?"** Do quá nhiều công cụ, đại lý bị nhầm lẫn và cố gọi `book_flight` _trong_ Paris, hoặc `rent_car` mặc dù bạn ưu tiên giao thông công cộng, vì mô tả công cụ có thể chồng chéo hoặc nó không thể phân biệt được cái tốt nhất.

**Giải pháp:** Sử dụng **RAG trên mô tả công cụ**. Khi bạn hỏi về việc đi lại ở Paris, hệ thống tự động lấy _chỉ_ các công cụ phù hợp nhất như `rent_car` hoặc `public_transport_info` theo truy vấn của bạn, đưa ra một danh sách "tải" công cụ tập trung cho LLM.

### Xung đột ngữ cảnh

**Đó là gì:** Khi thông tin trái ngược tồn tại trong ngữ cảnh, dẫn đến suy luận không nhất quán hoặc phản hồi cuối cùng sai. Điều này thường xảy ra khi thông tin được đưa đến theo từng giai đoạn, và giả định sai sớm vẫn còn trong ngữ cảnh.

**Cách xử lý:** Sử dụng **cắt tỉa ngữ cảnh** và **tách riêng**. Cắt tỉa có nghĩa là loại bỏ thông tin lỗi thời hoặc xung đột khi có chi tiết mới. Tách riêng cung cấp cho mô hình một "bảng ghi chú" riêng biệt để xử lý thông tin mà không làm rối ngữ cảnh chính.


**Ví dụ Đặt Chuyến Đi:** Ban đầu bạn nói với đại lý của mình, **"Tôi muốn bay hạng phổ thông."** Sau đó trong cuộc trò chuyện, bạn đổi ý và nói, **"Thực ra, cho chuyến đi này, hãy chọn hạng thương gia."** Nếu cả hai hướng dẫn vẫn còn trong ngữ cảnh, đại lý có thể nhận được kết quả tìm kiếm mâu thuẫn hoặc bị nhầm lẫn về ưu tiên nào nên đặt trước.

**Giải pháp:** Thực hiện **cắt tỉa ngữ cảnh**. Khi một hướng dẫn mới mâu thuẫn với hướng dẫn cũ, hướng dẫn cũ sẽ bị loại bỏ hoặc bị ghi đè rõ ràng trong ngữ cảnh. Ngoài ra, đại lý có thể sử dụng một **bảng ghi chú tạm** để giải quyết các ưu tiên mâu thuẫn trước khi quyết định, đảm bảo chỉ có hướng dẫn cuối cùng, nhất quán là hướng dẫn cho các hành động của mình.

## Có Thắc Mắc Thêm Về Kỹ Thuật Xử Lý Ngữ Cảnh?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ những người học khác, tham dự giờ làm việc và được trả lời các câu hỏi về Đại lý AI của bạn.
## Bài Học Trước

[Agentic Protocols](../11-agentic-protocols/README.md)

## Bài Học Tiếp Theo

[Memory for AI Agents](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->