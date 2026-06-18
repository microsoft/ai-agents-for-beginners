# Bộ nhớ cho các tác nhân AI  
[![Agent Memory](../../../translated_images/vi/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Khi thảo luận về những lợi ích độc đáo của việc tạo các tác nhân AI, hai điều chính được đề cập là: khả năng gọi các công cụ để hoàn thành nhiệm vụ và khả năng cải thiện theo thời gian. Bộ nhớ là nền tảng của việc tạo ra tác nhân tự cải tiến có thể tạo ra trải nghiệm tốt hơn cho người dùng của chúng ta.

Trong bài học này, chúng ta sẽ xem xét bộ nhớ là gì đối với các tác nhân AI và cách quản lý cũng như sử dụng nó để mang lại lợi ích cho các ứng dụng của chúng ta.

## Giới thiệu

Bài học này sẽ bao gồm:

• **Hiểu về Bộ nhớ của Tác nhân AI**: Bộ nhớ là gì và tại sao nó quan trọng đối với các tác nhân.

• **Triển khai và Lưu trữ Bộ nhớ**: Các phương pháp thực tế để thêm khả năng bộ nhớ cho tác nhân AI của bạn, tập trung vào bộ nhớ ngắn hạn và dài hạn.

• **Làm thế nào để các Tác nhân AI tự cải tiến**: Bộ nhớ giúp các tác nhân học từ các tương tác trước đó và cải thiện theo thời gian như thế nào.

## Các Triển khai Có sẵn

Bài học này bao gồm hai hướng dẫn notebook toàn diện:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Triển khai bộ nhớ sử dụng Mem0 và Azure AI Search với Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Triển khai bộ nhớ có cấu trúc sử dụng Cognee, tự động xây dựng biểu đồ tri thức hỗ trợ bởi embeddings, trực quan hóa biểu đồ, và truy xuất thông minh

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

• **Phân biệt các loại bộ nhớ khác nhau của tác nhân AI**, bao gồm bộ nhớ làm việc, bộ nhớ ngắn hạn và bộ nhớ dài hạn, cũng như các dạng đặc biệt như bộ nhớ cá nhân và bộ nhớ theo tập.

• **Triển khai và quản lý bộ nhớ ngắn hạn và dài hạn cho các tác nhân AI** sử dụng Microsoft Agent Framework, tận dụng các công cụ như Mem0, Cognee, bộ nhớ Whiteboard, và tích hợp với Azure AI Search.

• **Hiểu các nguyên tắc đằng sau các tác nhân AI tự cải tiến** và cách các hệ thống quản lý bộ nhớ thích hợp đóng góp vào việc học liên tục và thích nghi.

## Hiểu về Bộ nhớ của Tác nhân AI

Về cốt lõi, **bộ nhớ cho các tác nhân AI đề cập đến các cơ chế cho phép chúng giữ và nhớ lại thông tin**. Thông tin này có thể là chi tiết cụ thể về một cuộc trò chuyện, sở thích của người dùng, các hành động trước đây, hoặc thậm chí các mẫu đã học.

Không có bộ nhớ, các ứng dụng AI thường không trạng thái (stateless), nghĩa là mỗi lần tương tác bắt đầu lại từ đầu. Điều này dẫn đến trải nghiệm người dùng lặp đi lặp lại và gây khó chịu khi tác nhân "quên" bối cảnh hoặc sở thích trước đó.

### Tại sao Bộ nhớ quan trọng?

Trí thông minh của một tác nhân gắn chặt với khả năng nhớ lại và sử dụng thông tin trong quá khứ. Bộ nhớ cho phép các tác nhân:

• **Phản ánh**: Học từ các hành động và kết quả trước đó.

• **Tương tác**: Duy trì ngữ cảnh trong suốt một cuộc trò chuyện đang diễn ra.

• **Chủ động và Phản ứng**: Dự đoán nhu cầu hoặc phản hồi phù hợp dựa trên dữ liệu lịch sử.

• **Tự chủ**: Hoạt động độc lập hơn bằng cách dựa vào kiến thức đã lưu trữ.

Mục tiêu của việc triển khai bộ nhớ là làm cho các tác nhân trở nên **đáng tin cậy và có khả năng hơn**.

### Các loại Bộ nhớ

#### Bộ nhớ làm việc

Hãy tưởng tượng đây như một mảnh giấy nháp mà tác nhân sử dụng trong một nhiệm vụ hoặc quá trình suy nghĩ đang diễn ra. Nó giữ thông tin ngay lập tức cần thiết để tính toán bước tiếp theo.

Đối với các tác nhân AI, bộ nhớ làm việc thường ghi lại những thông tin liên quan nhất từ một cuộc trò chuyện, ngay cả khi lịch sử trò chuyện đầy đủ dài hoặc bị cắt bớt. Nó tập trung vào việc trích xuất các yếu tố chính như yêu cầu, đề xuất, quyết định, và hành động.

**Ví dụ về Bộ nhớ làm việc**

Trong một tác nhân đặt chuyến đi, bộ nhớ làm việc có thể ghi lại yêu cầu hiện tại của người dùng, ví dụ "Tôi muốn đặt chuyến đi đến Paris". Yêu cầu cụ thể này được giữ trong ngữ cảnh hiện tại của tác nhân để hướng dẫn tương tác hiện tại.

#### Bộ nhớ ngắn hạn

Loại bộ nhớ này giữ thông tin trong suốt thời gian của một cuộc trò chuyện hoặc phiên làm việc duy nhất. Đây là ngữ cảnh của cuộc trò chuyện hiện tại, cho phép tác nhân tham khảo lại các lượt trao đổi trước đó.

Trong các mẫu SDK Python của [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), điều này tương ứng với `AgentSession`, được tạo bằng `agent.create_session()`. Phiên làm việc là bộ nhớ ngắn hạn tích hợp trong framework: nó giữ bối cảnh cuộc trò chuyện trong khi phiên đó được dùng lại, nhưng bối cảnh này không được lưu giữ sau khi phiên kết thúc hoặc ứng dụng khởi động lại. Hãy sử dụng bộ nhớ dài hạn cho các dữ liệu và sở thích cần tồn tại qua các phiên làm việc, thường thông qua cơ sở dữ liệu, chỉ mục vector, hoặc kho lưu trữ bền vững khác.

**Ví dụ về Bộ nhớ ngắn hạn**

Nếu người dùng hỏi, "Một chuyến bay đến Paris giá bao nhiêu?" rồi sau đó hỏi tiếp "Còn chỗ ở thì sao?", bộ nhớ ngắn hạn đảm bảo tác nhân biết rằng "ở đó" là chỉ "Paris" trong cùng cuộc trò chuyện.

#### Bộ nhớ dài hạn

Đây là thông tin tồn tại qua nhiều cuộc trò chuyện hoặc phiên làm việc khác nhau. Nó cho phép các tác nhân nhớ sở thích người dùng, tương tác lịch sử, hoặc kiến thức chung trong thời gian dài. Việc này rất quan trọng cho cá nhân hóa.

**Ví dụ về Bộ nhớ dài hạn**

Một bộ nhớ dài hạn có thể lưu trữ rằng "Ben thích trượt tuyết và các hoạt động ngoài trời, thích cà phê có view núi, và muốn tránh các đường trượt khó do chấn thương trong quá khứ". Thông tin này, được học từ các tương tác trước đây, ảnh hưởng đến các đề xuất trong các phiên lập kế hoạch du lịch tương lai, làm cho chúng rất cá nhân hoá.

#### Bộ nhớ cá nhân (Persona Memory)

Loại bộ nhớ đặc biệt này giúp tác nhân phát triển một "tính cách" hoặc "nhân vật" nhất quán. Nó cho phép tác nhân nhớ các chi tiết về chính mình hoặc vai trò dự kiến, làm cho các tương tác trở nên mượt mà và tập trung hơn.

**Ví dụ về Bộ nhớ cá nhân**

Nếu tác nhân du lịch được thiết kế như một "chuyên gia lập kế hoạch trượt tuyết," bộ nhớ cá nhân có thể củng cố vai trò này, ảnh hưởng đến câu trả lời sao cho phù hợp với giọng điệu và kiến thức của một chuyên gia.

#### Bộ nhớ Quy trình / Theo tập (Workflow/Episodic Memory)

Bộ nhớ này lưu trữ chuỗi các bước tác nhân thực hiện trong một nhiệm vụ phức tạp, bao gồm cả thành công và thất bại. Nó giống như việc ghi nhớ các "tập phim" hoặc kinh nghiệm trong quá khứ để rút ra bài học.

**Ví dụ về Bộ nhớ theo tập**

Nếu tác nhân cố gắng đặt một chuyến bay cụ thể nhưng thất bại do vé không có, bộ nhớ theo tập có thể ghi lại thất bại này, cho phép tác nhân thử các chuyến bay thay thế hoặc thông báo cho người dùng về vấn đề một cách hiểu biết hơn trong lần thử sau.

#### Bộ nhớ Thực thể (Entity Memory)

Bộ nhớ này liên quan đến việc trích xuất và ghi nhớ các thực thể cụ thể (như con người, địa điểm, hoặc vật thể) và sự kiện từ các cuộc trò chuyện. Nó cho phép tác nhân xây dựng một hiểu biết có cấu trúc về các yếu tố chính được thảo luận.

**Ví dụ về Bộ nhớ Thực thể**

Từ một cuộc trò chuyện về chuyến đi trước đây, tác nhân có thể trích xuất "Paris," "Tháp Eiffel," và "bữa tối tại nhà hàng Le Chat Noir" như các thực thể. Trong tương tác tương lai, tác nhân có thể nhớ "Le Chat Noir" và đề nghị đặt chỗ lại tại đó.

#### RAG có cấu trúc (Structured RAG - Retrieval Augmented Generation)

Trong khi RAG là một kỹ thuật rộng hơn, "Structured RAG" được nhấn mạnh như một công nghệ bộ nhớ mạnh mẽ. Nó trích xuất thông tin đặc, có cấu trúc từ nhiều nguồn khác nhau (cuộc trò chuyện, email, hình ảnh) và sử dụng nó để nâng cao độ chính xác, khả năng nhớ lại và tốc độ phản hồi. Khác với RAG cổ điển chỉ dựa trên sự tương đồng ngữ nghĩa, Structured RAG làm việc với cấu trúc vốn có của thông tin.

**Ví dụ về Structured RAG**

Thay vì chỉ đối chiếu từ khóa, Structured RAG có thể phân tích chi tiết chuyến bay (đích đến, ngày giờ, hãng bay) từ một email và lưu trữ chúng theo cách có cấu trúc. Điều này cho phép truy vấn chính xác như "Tôi đã đặt chuyến bay đến Paris vào thứ Ba nào?"

## Triển khai và Lưu trữ Bộ nhớ

Triển khai bộ nhớ cho các tác nhân AI liên quan đến một quy trình hệ thống về **quản lý bộ nhớ**, bao gồm tạo, lưu trữ, truy xuất, tích hợp, cập nhật, và thậm chí "quên" (hay xóa) thông tin. Việc truy xuất là một khía cạnh đặc biệt quan trọng.

### Công cụ Bộ nhớ chuyên biệt

#### Mem0

Một cách để lưu trữ và quản lý bộ nhớ tác nhân là sử dụng các công cụ chuyên biệt như Mem0. Mem0 hoạt động như một lớp bộ nhớ bền vững, cho phép tác nhân nhớ lại các tương tác liên quan, lưu trữ sở thích người dùng và bối cảnh thực tế, và học từ thành công cũng như thất bại theo thời gian. Ý tưởng ở đây là biến các tác nhân không trạng thái thành có trạng thái.

Nó hoạt động qua **quy trình bộ nhớ hai giai đoạn: trích xuất và cập nhật**. Đầu tiên, các tin nhắn được thêm vào luồng của tác nhân được gửi đến dịch vụ Mem0, sử dụng Mô hình Ngôn ngữ Lớn (LLM) để tóm tắt lịch sử cuộc trò chuyện và trích xuất các ký ức mới. Sau đó, giai đoạn cập nhật do LLM điều khiển xác định có nên thêm, sửa đổi, hay xóa những ký ức này, lưu chúng vào hệ thống dữ liệu lai có thể bao gồm cơ sở dữ liệu vector, biểu đồ, và key-value. Hệ thống này cũng hỗ trợ nhiều loại bộ nhớ và có thể kết hợp bộ nhớ biểu đồ để quản lý các mối quan hệ giữa các thực thể.

#### Cognee

Một cách tiếp cận mạnh mẽ khác là sử dụng **Cognee**, một bộ nhớ ngữ nghĩa mã nguồn mở cho các tác nhân AI biến dữ liệu cấu trúc và phi cấu trúc thành biểu đồ tri thức có thể truy vấn hỗ trợ bởi embeddings. Cognee cung cấp **kiến trúc lưu trữ kép** kết hợp tìm kiếm tương đồng vector với các mối quan hệ biểu đồ, cho phép các tác nhân hiểu không chỉ thông tin nào giống nhau mà còn cách các khái niệm liên quan với nhau.

Nó nổi trội trong **truy xuất lai** pha trộn tìm kiếm tương đồng vector, cấu trúc biểu đồ, và lý luận LLM - từ truy vấn khối dữ liệu thô đến trả lời câu hỏi có nhận thức biểu đồ. Hệ thống duy trì **bộ nhớ sống** phát triển và mở rộng đồng thời vẫn có thể truy vấn dưới dạng một biểu đồ kết nối, hỗ trợ cả ngữ cảnh phiên ngắn hạn và bộ nhớ bền vững dài hạn.

Hướng dẫn notebook Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) minh họa việc xây dựng lớp bộ nhớ thống nhất này, với các ví dụ thực tế về nhập liệu từ nhiều nguồn dữ liệu khác nhau, trực quan hóa biểu đồ tri thức, và truy vấn với các chiến lược tìm kiếm khác nhau phù hợp với nhu cầu cụ thể của tác nhân.

### Lưu trữ Bộ nhớ với RAG

Ngoài các công cụ bộ nhớ chuyên biệt như mem0, bạn có thể tận dụng các dịch vụ tìm kiếm mạnh mẽ như **Azure AI Search làm backend để lưu trữ và truy xuất ký ức**, đặc biệt cho Structured RAG.

Điều này cho phép bạn làm nền tảng câu trả lời của tác nhân dựa trên dữ liệu của riêng bạn, đảm bảo câu trả lời phù hợp và chính xác hơn. Azure AI Search có thể được dùng lưu trữ ký ức du lịch cá nhân, danh mục sản phẩm, hoặc bất kỳ kiến thức chuyên môn nào khác.

Azure AI Search hỗ trợ các tính năng như **Structured RAG**, vượt trội trong việc trích xuất và truy xuất thông tin đặc, có cấu trúc từ các bộ dữ liệu lớn như lịch sử cuộc trò chuyện, email, hoặc thậm chí hình ảnh. Điều này cung cấp "độ chính xác và khả năng nhớ lại siêu phàm" so với cách tiếp cận chia nhỏ văn bản và nhúng truyền thống.

## Làm cho các Tác nhân AI tự Cải tiến

Mẫu phổ biến cho các tác nhân tự cải tiến liên quan đến việc giới thiệu một **"tác nhân tri thức"** riêng biệt. Tác nhân này quan sát cuộc trò chuyện chính giữa người dùng và tác nhân chính. Vai trò của nó là:

1. **Xác định thông tin có giá trị**: Xem phần nào của cuộc trò chuyện đáng được lưu lại như tri thức chung hoặc sở thích người dùng cụ thể.

2. **Trích xuất và tóm tắt**: Đúc kết những bài học hoặc sở thích quan trọng từ cuộc trò chuyện.

3. **Lưu trữ trong cơ sở tri thức**: Ghi nhận thông tin đã trích xuất, thường trong cơ sở dữ liệu vector, để có thể truy xuất sau này.

4. **Tăng cường truy vấn tương lai**: Khi người dùng bắt đầu truy vấn mới, tác nhân tri thức truy xuất thông tin liên quan đã lưu và thêm vào lời nhắc của người dùng, cung cấp ngữ cảnh quan trọng cho tác nhân chính (tương tự như RAG).

### Tối ưu hóa cho Bộ nhớ

• **Quản lý Độ trễ**: Để tránh làm chậm tương tác với người dùng, một mô hình nhanh, rẻ hơn có thể được sử dụng ban đầu để nhanh chóng kiểm tra xem thông tin có đáng lưu hoặc truy xuất không, chỉ kích hoạt quy trình trích xuất/truy xuất phức tạp hơn khi cần thiết.

• **Bảo trì Cơ sở tri thức**: Với cơ sở tri thức đang phát triển, thông tin ít được sử dụng có thể được chuyển vào "lưu trữ lạnh" để quản lý chi phí.

## Còn câu hỏi nào về Bộ nhớ Tác nhân?

Tham gia cộng đồng [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ những người học khác, tham dự giờ học và nhận câu trả lời cho các câu hỏi về Tác nhân AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->