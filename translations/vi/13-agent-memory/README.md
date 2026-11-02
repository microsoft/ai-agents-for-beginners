# Bộ Nhớ cho Các Đại Lý AI 
[![Agent Memory](../../../translated_images/vi/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Khi thảo luận về lợi ích độc đáo của việc tạo các Đại Lý AI, chủ yếu có hai điều được đề cập: khả năng gọi công cụ để hoàn thành nhiệm vụ và khả năng cải thiện theo thời gian. Bộ nhớ là nền tảng của việc tạo ra đại lý có khả năng tự cải thiện để tạo ra trải nghiệm tốt hơn cho người dùng của chúng ta.

Trong bài học này, chúng ta sẽ xem xét bộ nhớ là gì đối với các Đại Lý AI và cách chúng ta có thể quản lý và sử dụng nó vì lợi ích của các ứng dụng của mình.

## Giới thiệu

Bài học này sẽ bao gồm:

• **Hiểu về Bộ Nhớ của Đại Lý AI**: Bộ nhớ là gì và tại sao nó quan trọng đối với các đại lý.

• **Triển khai và Lưu trữ Bộ Nhớ**: Các phương pháp thực tiễn để thêm khả năng bộ nhớ vào các đại lý AI của bạn, tập trung vào bộ nhớ ngắn hạn và dài hạn.

• **Làm cho Đại Lý AI Tự Cải Thiện**: Cách bộ nhớ giúp các đại lý học hỏi từ các tương tác trước và cải thiện theo thời gian.

## Các Triển khai Có sẵn

Bài học này bao gồm hai hướng dẫn notebook toàn diện:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Triển khai bộ nhớ sử dụng Mem0 và Azure AI Search với Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Triển khai bộ nhớ có cấu trúc sử dụng Cognee, tự động xây dựng đồ thị tri thức dựa trên embedding, trực quan hóa đồ thị và truy xuất thông minh

## Mục Tiêu Học Tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

• **Phân biệt giữa các loại bộ nhớ khác nhau của đại lý AI**, bao gồm bộ nhớ làm việc, ngắn hạn và dài hạn, cũng như các dạng chuyên biệt như bộ nhớ cá tính và bộ nhớ tập sự.

• **Triển khai và quản lý bộ nhớ ngắn hạn và dài hạn cho các đại lý AI** sử dụng Microsoft Agent Framework, tận dụng các công cụ như Mem0, Cognee, bộ nhớ Whiteboard, và tích hợp với Azure AI Search.

• **Hiểu các nguyên tắc đằng sau các đại lý AI tự cải thiện** và cách các hệ thống quản lý bộ nhớ mạnh mẽ góp phần vào việc học liên tục và thích nghi.

## Hiểu về Bộ Nhớ Đại Lý AI

Về cơ bản, **bộ nhớ cho các đại lý AI đề cập đến các cơ chế cho phép họ lưu giữ và nhớ lại thông tin**. Thông tin này có thể là các chi tiết cụ thể về một cuộc trò chuyện, sở thích người dùng, hành động trước đây hoặc thậm chí mẫu đã học.

Nếu không có bộ nhớ, các ứng dụng AI thường không trạng thái, nghĩa là mỗi tương tác bắt đầu lại từ đầu. Điều này dẫn đến trải nghiệm người dùng lặp đi lặp lại và gây khó chịu, nơi đại lý "quên" bối cảnh hoặc sở thích trước đó.

### Vì sao Bộ Nhớ lại Quan Trọng?

trí thông minh của một đại lý gắn liền mật thiết với khả năng nhớ lại và sử dụng thông tin trong quá khứ. Bộ nhớ cho phép các đại lý:

• **Phản chiếu**: Học hỏi từ các hành động và kết quả trước đó.

• **Tương tác**: Duy trì bối cảnh trong một cuộc trò chuyện đang diễn ra.

• **Chủ động và Phản hồi**: Dự đoán nhu cầu hoặc phản ứng phù hợp dựa trên dữ liệu lịch sử.

• **Tự chủ**: Hoạt động độc lập hơn bằng cách dựa trên kiến thức đã lưu trữ.

Mục tiêu của việc triển khai bộ nhớ là làm cho các đại lý trở nên **đáng tin cậy và có khả năng hơn**.

### Các Loại Bộ Nhớ

#### Bộ Nhớ Làm Việc

Hãy coi đây là một mảnh giấy nháp mà đại lý sử dụng trong một nhiệm vụ hoặc quá trình suy nghĩ đang diễn ra. Nó giữ thông tin ngay lập tức cần thiết để tính toán bước tiếp theo.

Đối với các đại lý AI, bộ nhớ làm việc thường lưu giữ thông tin quan trọng nhất từ một cuộc trò chuyện, ngay cả khi lịch sử trò chuyện đầy đủ dài hoặc bị cắt bớt. Nó tập trung vào việc trích xuất các yếu tố chính như yêu cầu, đề xuất, quyết định và hành động.

**Ví dụ về Bộ Nhớ Làm Việc**

Trong một đại lý đặt vé du lịch, bộ nhớ làm việc có thể ghi nhớ yêu cầu hiện tại của người dùng, chẳng hạn "Tôi muốn đặt một chuyến đi đến Paris". Yêu cầu cụ thể này được giữ trong bối cảnh ngay lập tức của đại lý để hướng dẫn tương tác hiện tại.

#### Bộ Nhớ Ngắn Hạn

Loại bộ nhớ này giữ thông tin trong suốt một cuộc trò chuyện hoặc phiên làm việc duy nhất. Đây là bối cảnh của cuộc trò chuyện hiện tại, cho phép đại lý tham chiếu lại các lượt trước trong hội thoại.

Trong các mẫu SDK Python của [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), điều này tương ứng với `AgentSession`, được tạo bằng `agent.create_session()`. Phiên làm việc là bộ nhớ ngắn hạn tích hợp sẵn của framework: nó giữ bối cảnh trò chuyện có sẵn khi cùng một phiên được sử dụng lại, nhưng bối cảnh đó không được lưu khi phiên kết thúc hoặc ứng dụng khởi động lại. Sử dụng bộ nhớ dài hạn cho các sự thật và sở thích cần tồn tại qua các phiên, thường thông qua cơ sở dữ liệu, chỉ mục vector, hoặc một kho lưu trữ bền vững khác.

**Ví dụ về Bộ Nhớ Ngắn Hạn**

Nếu người dùng hỏi, "Giá vé máy bay đến Paris là bao nhiêu?" và sau đó tiếp tục với "Còn chỗ ở thì sao?", bộ nhớ ngắn hạn đảm bảo đại lý biết "ở đó" đề cập đến "Paris" trong cùng một cuộc trò chuyện.

#### Bộ Nhớ Dài Hạn

Đây là thông tin tồn tại qua nhiều cuộc trò chuyện hoặc phiên làm việc. Nó cho phép các đại lý nhớ sở thích người dùng, các tương tác lịch sử hoặc kiến thức chung trong thời gian dài. Điều này quan trọng cho việc cá nhân hóa.

**Ví dụ về Bộ Nhớ Dài Hạn**

Bộ nhớ dài hạn có thể lưu rằng "Ben thích trượt tuyết và các hoạt động ngoài trời, thích cà phê với tầm nhìn núi, và muốn tránh các dốc trượt hiểm hóc do một chấn thương trước đây". Thông tin này, được học từ các tương tác trước, ảnh hưởng đến các đề xuất trong các phiên lên kế hoạch du lịch trong tương lai, làm cho chúng rất cá nhân hóa.

#### Bộ Nhớ Cá Tính

Loại bộ nhớ chuyên biệt này giúp một đại lý phát triển "tính cách" hoặc "cá tính" nhất quán. Nó cho phép đại lý nhớ các chi tiết về bản thân hoặc vai trò dự định, làm cho các tương tác trở nên mạch lạc và tập trung hơn.

**Ví dụ về Bộ Nhớ Cá Tính**
Nếu đại lý du lịch được thiết kế để là một "chuyên gia lên kế hoạch trượt tuyết," bộ nhớ cá tính có thể củng cố vai trò này, ảnh hưởng đến câu trả lời của nó để phù hợp với giọng điệu và kiến thức của một chuyên gia.

#### Bộ Nhớ Quy Trình Tác Vụ / Tập Sự

Bộ nhớ này lưu lại chuỗi các bước đại lý thực hiện trong một nhiệm vụ phức tạp, bao gồm những thành công và thất bại. Nó giống như việc nhớ các "tập sự" hoặc trải nghiệm trong quá khứ để học hỏi từ chúng.

**Ví dụ về Bộ Nhớ Tập Sự**

Nếu đại lý cố gắng đặt một chuyến bay cụ thể nhưng thất bại do hết chỗ, bộ nhớ tập sự có thể ghi lại thất bại này, cho phép đại lý thử các chuyến bay thay thế hoặc thông báo cho người dùng về vấn đề một cách có hiểu biết hơn trong lần thử tiếp theo.

#### Bộ Nhớ Thực Thể

Điều này liên quan đến việc trích xuất và nhớ các thực thể cụ thể (như người, địa điểm hoặc vật thể) và các sự kiện từ các cuộc trò chuyện. Nó cho phép đại lý xây dựng sự hiểu biết có cấu trúc về các yếu tố chính đã được thảo luận.

**Ví dụ về Bộ Nhớ Thực Thể**

Từ một cuộc trò chuyện về chuyến đi trước, đại lý có thể trích xuất "Paris," "Tháp Eiffel," và "bữa tối tại nhà hàng Le Chat Noir" như các thực thể. Trong tương tác tương lai, đại lý có thể nhớ lại "Le Chat Noir" và đề nghị đặt chỗ mới ở đó.

#### Structured RAG (Retrieval Augmented Generation - Tăng cường Truy xuất có Cấu trúc)

Trong khi RAG là một kỹ thuật rộng hơn, "Structured RAG" được nhấn mạnh như một công nghệ bộ nhớ mạnh mẽ. Nó trích xuất thông tin đặc, có cấu trúc từ nhiều nguồn khác nhau (cuộc trò chuyện, email, hình ảnh) và sử dụng chúng để tăng độ chính xác, khả năng truy xuất và tốc độ trả lời. Khác với RAG cổ điển chỉ dựa vào sự tương đồng ngữ nghĩa, Structured RAG làm việc với cấu trúc vốn có của thông tin.

**Ví dụ về Structured RAG**

Thay vì chỉ khớp từ khóa, Structured RAG có thể phân tích chi tiết chuyến bay (đích đến, ngày, giờ, hãng hàng không) từ một email và lưu trữ theo cách có cấu trúc. Điều này cho phép truy vấn chính xác như "Tôi đã đặt chuyến bay nào đến Paris vào thứ Ba?"

## Triển khai và Lưu trữ Bộ Nhớ

Triển khai bộ nhớ cho các đại lý AI bao gồm một quá trình hệ thống của **quản lý bộ nhớ**, bao gồm tạo, lưu trữ, truy xuất, tích hợp, cập nhật và thậm chí "quên" (hoặc xóa) thông tin. Truy xuất là một khía cạnh đặc biệt quan trọng.

### Công Cụ Bộ Nhớ Chuyên Biệt

#### Mem0

Một cách để lưu trữ và quản lý bộ nhớ đại lý là sử dụng các công cụ chuyên biệt như Mem0. Mem0 hoạt động như một lớp bộ nhớ bền vững, cho phép các đại lý nhớ lại các tương tác liên quan, lưu sở thích người dùng và bối cảnh thực tế, và học hỏi từ thành công và thất bại theo thời gian. Ý tưởng ở đây là các đại lý không trạng thái trở thành có trạng thái.

Nó hoạt động qua **quy trình bộ nhớ hai giai đoạn: trích xuất và cập nhật**. Đầu tiên, các tin nhắn thêm vào luồng của đại lý được gửi đến dịch vụ Mem0, sử dụng Mô Hình Ngôn Ngữ Lớn (LLM) để tóm tắt lịch sử trò chuyện và trích xuất các ký ức mới. Sau đó, một giai đoạn cập nhật do LLM điều khiển xác định xem có nên thêm, sửa đổi, hay xóa các ký ức này, lưu chúng trong một kho dữ liệu lai có thể bao gồm cơ sở dữ liệu vector, đồ thị, và khóa-giá trị. Hệ thống này cũng hỗ trợ nhiều loại bộ nhớ và có thể tích hợp bộ nhớ đồ thị để quản lý mối quan hệ giữa các thực thể.

#### Cognee

Một phương pháp mạnh mẽ khác là sử dụng **Cognee**, bộ nhớ ngữ nghĩa mã nguồn mở cho các đại lý AI, chuyển đổi dữ liệu có cấu trúc và không có cấu trúc thành đồ thị tri thức có thể truy vấn dựa trên embedding. Cognee cung cấp kiến trúc **kép kho lưu trữ** kết hợp tìm kiếm tương đồng vector với các mối quan hệ đồ thị, cho phép đại lý hiểu không chỉ thông tin nào là tương tự mà còn cách các khái niệm liên quan với nhau.

Nó xuất sắc trong việc **truy xuất lai** kết hợp tương đồng vector, cấu trúc đồ thị, và lý luận LLM - từ tra cứu mảnh dữ liệu thô đến trả lời câu hỏi nhận biết đồ thị. Hệ thống duy trì **bộ nhớ sống** phát triển và mở rộng trong khi vẫn có thể truy vấn như một đồ thị kết nối, hỗ trợ cả bối cảnh phiên làm việc ngắn hạn và bộ nhớ bền vững dài hạn.

Notebook hướng dẫn Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) minh họa việc xây dựng lớp bộ nhớ hợp nhất này, với các ví dụ thực tế về nhập nguồn dữ liệu đa dạng, trực quan hóa đồ thị tri thức, và truy vấn với các chiến lược tìm kiếm khác nhau phù hợp với nhu cầu cụ thể của đại lý.

### Lưu trữ Bộ Nhớ với RAG

Ngoài các công cụ bộ nhớ chuyên biệt như Mem0, bạn có thể tận dụng các dịch vụ tìm kiếm mạnh mẽ như **Azure AI Search làm backend để lưu trữ và truy xuất ký ức**, đặc biệt cho Structured RAG.

Điều này cho phép bạn căn cứ câu trả lời của đại lý vào dữ liệu của riêng bạn, đảm bảo câu trả lời chính xác và phù hợp hơn. Azure AI Search có thể được sử dụng để lưu trữ ký ức du lịch cụ thể của người dùng, danh mục sản phẩm hoặc bất kỳ kiến thức chuyên ngành nào khác.

Azure AI Search hỗ trợ các khả năng như **Structured RAG**, nổi bật trong việc trích xuất và truy xuất thông tin đặc, có cấu trúc từ các tập dữ liệu lớn như lịch sử trò chuyện, email, hoặc thậm chí hình ảnh. Điều này mang lại "độ chính xác và độ thu hồi siêu việt" so với các phương pháp chia nhỏ văn bản và embedding truyền thống.

## Làm Cho Các Đại Lý AI Tự Cải Thiện

Một mô hình phổ biến cho đại lý tự cải thiện bao gồm việc giới thiệu một **"đại lý kiến thức"**. Đại lý riêng biệt này quan sát cuộc trò chuyện chính giữa người dùng và đại lý chính. Vai trò của nó là:

1. **Xác định thông tin có giá trị**: Xác định xem phần nào của cuộc trò chuyện đáng lưu giữ như kiến thức chung hoặc sở thích người dùng cụ thể.

2. **Trích xuất và tóm tắt**: Chiết xuất kiến thức hoặc sở thích thiết yếu từ cuộc trò chuyện.

3. **Lưu trữ vào cơ sở kiến thức**: Lưu giữ thông tin trích xuất, thường trong cơ sở dữ liệu vector, để có thể truy xuất sau này.

4. **Tăng cường các truy vấn tương lai**: Khi người dùng bắt đầu truy vấn mới, đại lý kiến thức truy xuất thông tin liên quan đã lưu và đính kèm nó vào lời nhắc của người dùng, cung cấp bối cảnh quan trọng cho đại lý chính (tương tự như RAG).

### Tối Ưu Hóa cho Bộ Nhớ

• **Quản lý Độ Trễ**: Để tránh làm chậm tương tác người dùng, một mô hình rẻ hơn và nhanh hơn có thể được sử dụng ban đầu để nhanh chóng kiểm tra xem thông tin có giá trị để lưu hoặc truy xuất không, chỉ gọi quy trình trích xuất/truy xuất phức tạp hơn khi cần thiết.

• **Bảo Trì Cơ Sở Kiến Thức**: Đối với cơ sở kiến thức đang phát triển, thông tin ít được sử dụng có thể được chuyển sang "lưu trữ lạnh" để quản lý chi phí.

## Có Thắc Mắc Hơn Về Bộ Nhớ Đại Lý?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ những người học khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về Đại Lý AI của bạn.
## Bài Học Trước

[Kỹ Thuật Bối Cảnh cho Đại Lý AI](../12-context-engineering/README.md)

## Bài Học Tiếp Theo

[Khám Phá Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->