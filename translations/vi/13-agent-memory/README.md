# Bộ nhớ cho các Đại lý AI 
[![Agent Memory](../../../translated_images/vi/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Khi thảo luận về lợi ích độc đáo của việc tạo ra các Đại lý AI, hai điều thường được đề cập chính là: khả năng gọi công cụ để hoàn thành nhiệm vụ và khả năng cải thiện theo thời gian. Bộ nhớ là nền tảng của việc tạo ra đại lý tự cải tiến có thể tạo ra trải nghiệm tốt hơn cho người dùng của chúng ta.

Trong bài học này, chúng ta sẽ xem xét bộ nhớ là gì đối với các Đại lý AI và cách chúng ta có thể quản lý và sử dụng nó vì lợi ích của các ứng dụng của chúng ta.

## Giới thiệu

Bài học này sẽ bao gồm:

• **Hiểu về Bộ nhớ của Đại lý AI**: Bộ nhớ là gì và tại sao nó lại quan trọng đối với các đại lý.

• **Triển khai và Lưu trữ Bộ nhớ**: Các phương pháp thực tiễn để thêm khả năng bộ nhớ cho các đại lý AI của bạn, tập trung vào bộ nhớ ngắn hạn và dài hạn.

• **Làm cho các Đại lý AI Tự cải tiến**: Cách bộ nhớ cho phép các đại lý học hỏi từ các tương tác trước đây và cải thiện theo thời gian.

## Các Triển khai Có sẵn

Bài học này bao gồm hai hướng dẫn notebook toàn diện:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Triển khai bộ nhớ sử dụng Mem0 và Azure AI Search với Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Triển khai bộ nhớ có cấu trúc sử dụng Cognee, tự động xây dựng đồ thị kiến thức dựa trên embeddings, trực quan hóa đồ thị và truy xuất thông minh

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

• **Phân biệt các loại bộ nhớ khác nhau của đại lý AI**, bao gồm bộ nhớ làm việc, ngắn hạn và dài hạn, cũng như các dạng chuyên biệt như bộ nhớ nhân cách và bộ nhớ theo tập.

• **Triển khai và quản lý bộ nhớ ngắn hạn và dài hạn cho các đại lý AI** sử dụng Microsoft Agent Framework, tận dụng các công cụ như Mem0, Cognee, bộ nhớ Whiteboard, và tích hợp với Azure AI Search.

• **Hiểu các nguyên lý đứng sau các đại lý AI tự cải tiến** và cách các hệ thống quản lý bộ nhớ mạnh mẽ góp phần vào việc học tập và thích ứng liên tục.

## Hiểu về Bộ nhớ của Đại lý AI

Về cốt lõi, **bộ nhớ cho các đại lý AI đề cập đến các cơ chế cho phép họ giữ lại và nhớ lại thông tin**. Thông tin này có thể là các chi tiết cụ thể về một cuộc trò chuyện, sở thích của người dùng, các hành động trong quá khứ, hoặc thậm chí các mẫu đã học.

Nếu không có bộ nhớ, các ứng dụng AI thường không trạng thái, nghĩa là mỗi tương tác bắt đầu từ đầu. Điều này dẫn đến trải nghiệm người dùng lặp lại và khó chịu khi đại lý "quên" bối cảnh hoặc sở thích trước đó.

### Tại sao Bộ nhớ lại Quan trọng?

trí thông minh của đại lý gắn bó sâu sắc với khả năng nhớ và sử dụng thông tin trong quá khứ. Bộ nhớ cho phép các đại lý:

• **Phản chiếu**: Học từ các hành động và kết quả trong quá khứ.

• **Tương tác**: Duy trì bối cảnh trong cuộc trò chuyện đang diễn ra.

• **Chủ động và Phản ứng**: Dự đoán nhu cầu hoặc phản hồi phù hợp dựa trên dữ liệu lịch sử.

• **Tự chủ**: Hoạt động độc lập hơn bằng cách khai thác kiến thức đã lưu trữ.

Mục tiêu của việc triển khai bộ nhớ là làm cho các đại lý trở nên **đáng tin cậy và có khả năng** hơn.

### Các loại Bộ nhớ

#### Bộ nhớ Làm việc

Hãy nghĩ về nó như một tờ giấy nháp mà đại lý sử dụng trong một nhiệm vụ hoặc quá trình suy nghĩ đang diễn ra. Nó giữ thông tin cần thiết ngay lập tức để tính toán bước tiếp theo.

Đối với các đại lý AI, bộ nhớ làm việc thường ghi lại thông tin liên quan nhất từ một cuộc trò chuyện, ngay cả khi toàn bộ lịch sử trò chuyện dài hoặc bị cắt ngắn. Nó tập trung vào việc trích xuất các yếu tố chính như yêu cầu, đề xuất, quyết định và hành động.

**Ví dụ về Bộ nhớ Làm việc**

Trong một đại lý đặt chuyến đi, bộ nhớ làm việc có thể ghi lại yêu cầu hiện tại của người dùng, chẳng hạn như "Tôi muốn đặt một chuyến đi đến Paris". Yêu cầu cụ thể này được giữ trong bối cảnh ngay lập tức của đại lý để hướng dẫn tương tác hiện tại.

#### Bộ nhớ Ngắn hạn

Loại bộ nhớ này giữ thông tin trong suốt thời gian của một cuộc trò chuyện hoặc phiên làm việc duy nhất. Nó là bối cảnh của cuộc trò chuyện hiện tại, cho phép đại lý tham khảo lại các lượt nói trước đó trong đối thoại.

Trong các mẫu Python SDK [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), điều này tương ứng với `AgentSession`, được tạo ra bằng `agent.create_session()`. Phiên làm việc là bộ nhớ ngắn hạn tích hợp sẵn của framework: nó giữ bối cảnh cuộc trò chuyện trong khi cùng một phiên làm việc được tái sử dụng, nhưng bối cảnh đó không được lưu khi phiên kết thúc hoặc ứng dụng khởi động lại. Sử dụng bộ nhớ dài hạn cho các sự kiện và sở thích cần tồn tại qua các phiên làm việc, thường thông qua cơ sở dữ liệu, chỉ mục vector, hoặc một kho lưu trữ bền vững khác.

**Ví dụ về Bộ nhớ Ngắn hạn**

Nếu người dùng hỏi, "Một chuyến bay đến Paris sẽ tốn bao nhiêu tiền?" sau đó tiếp tục với "Còn chỗ ở bên đó thì sao?", bộ nhớ ngắn hạn đảm bảo đại lý biết "bên đó" đề cập đến "Paris" trong cùng một cuộc trò chuyện.

#### Bộ nhớ Dài hạn

Đây là thông tin tồn tại qua nhiều cuộc trò chuyện hoặc phiên làm việc. Nó cho phép các đại lý ghi nhớ sở thích người dùng, các tương tác lịch sử, hoặc kiến thức chung trong khoảng thời gian dài. Điều này rất quan trọng cho cá nhân hóa.

**Ví dụ về Bộ nhớ Dài hạn**

Bộ nhớ dài hạn có thể lưu rằng "Ben thích trượt tuyết và các hoạt động ngoài trời, thích cà phê với tầm nhìn núi non, và muốn tránh các đường trượt tuyết nâng cao do chấn thương trong quá khứ". Thông tin này, được rút ra từ các tương tác trước đây, ảnh hưởng đến các đề xuất trong các phiên lập kế hoạch du lịch tương lai, làm cho chúng rất cá nhân hóa.

#### Bộ nhớ Nhân cách

Loại bộ nhớ chuyên biệt này giúp đại lý phát triển một "tính cách" hoặc "nhân cách" nhất quán. Nó cho phép đại lý nhớ các chi tiết về bản thân hoặc vai trò dự kiến, làm cho các tương tác trở nên mượt mà và tập trung hơn.

**Ví dụ về Bộ nhớ Nhân cách**
Nếu đại lý du lịch được thiết kế như một "chuyên gia lập kế hoạch trượt tuyết," bộ nhớ nhân cách có thể củng cố vai trò này, ảnh hưởng đến câu trả lời để phù hợp với giọng điệu và kiến thức của một chuyên gia.

#### Bộ nhớ Quy trình làm việc/Tập sự kiện

Bộ nhớ này lưu trữ chuỗi các bước mà đại lý thực hiện trong một nhiệm vụ phức tạp, bao gồm cả thành công và thất bại. Nó giống như nhớ lại các "tập" hoặc trải nghiệm trong quá khứ để học hỏi từ chúng.

**Ví dụ về Bộ nhớ Tập sự kiện**

Nếu đại lý cố gắng đặt một chuyến bay cụ thể nhưng thất bại do không có chỗ, bộ nhớ tập sự kiện có thể ghi nhận thất bại này, cho phép đại lý thử các chuyến bay thay thế hoặc thông báo cho người dùng về vấn đề với thông tin đầy đủ hơn trong lần thử tiếp theo.

#### Bộ nhớ Thực thể

Điều này liên quan đến việc trích xuất và ghi nhớ các thực thể cụ thể (như người, địa điểm hoặc vật thể) và sự kiện từ các cuộc trò chuyện. Nó cho phép đại lý xây dựng hiểu biết có cấu trúc về các yếu tố chính được thảo luận.

**Ví dụ về Bộ nhớ Thực thể**

Từ một cuộc trò chuyện về chuyến đi trước đây, đại lý có thể trích xuất "Paris," "Tháp Eiffel," và "bữa tối tại nhà hàng Le Chat Noir" như các thực thể. Trong tương tác tương lai, đại lý có thể nhớ "Le Chat Noir" và đề nghị đặt chỗ mới ở đó.

#### Structured RAG (Tạo văn bản tăng cường truy xuất có cấu trúc)

Trong khi RAG là một kỹ thuật rộng hơn, "Structured RAG" được nhấn mạnh là một công nghệ bộ nhớ mạnh mẽ. Nó trích xuất thông tin cô đọng, có cấu trúc từ nhiều nguồn khác nhau (cuộc trò chuyện, email, hình ảnh) và sử dụng nó để nâng cao độ chính xác, khả năng truy xuất và tốc độ phản hồi. Khác với RAG cổ điển chỉ dựa vào sự tương đồng ngữ nghĩa, Structured RAG làm việc với cấu trúc vốn có của thông tin.

**Ví dụ về Structured RAG**

Thay vì chỉ khớp từ khóa, Structured RAG có thể phân tích các chi tiết chuyến bay (điểm đến, ngày, giờ, hãng bay) từ một email và lưu trữ chúng theo cách có cấu trúc. Điều này cho phép các truy vấn chính xác như "Tôi đã đặt chuyến bay nào đến Paris vào thứ Ba?"

## Triển khai và Lưu trữ Bộ nhớ

Triển khai bộ nhớ cho các đại lý AI bao gồm một quy trình có hệ thống quản lý bộ nhớ, bao gồm tạo, lưu trữ, truy xuất, tích hợp, cập nhật, và thậm chí là "quên" (hoặc xóa) thông tin. Truy xuất là một khía cạnh đặc biệt quan trọng.

### Công cụ Bộ nhớ Chuyên biệt

#### Mem0

Một cách để lưu trữ và quản lý bộ nhớ đại lý là sử dụng các công cụ chuyên biệt như Mem0. Mem0 hoạt động như một lớp bộ nhớ bền vững, cho phép các đại lý nhớ lại các tương tác liên quan, lưu trữ sở thích người dùng và bối cảnh thực tế, và học hỏi từ thành công cũng như thất bại theo thời gian. Ý tưởng ở đây là các đại lý không trạng thái trở thành có trạng thái.

Nó hoạt động thông qua **quy trình bộ nhớ hai giai đoạn: trích xuất và cập nhật**. Đầu tiên, các tin nhắn được thêm vào chuỗi của đại lý được gửi đến dịch vụ Mem0, nơi sử dụng Mô hình Ngôn ngữ Lớn (LLM) để tóm tắt lịch sử cuộc trò chuyện và trích xuất các kí ức mới. Sau đó, giai đoạn cập nhật do LLM điều khiển xác định xem có nên thêm, sửa đổi hay xóa các kí ức này, lưu trữ chúng trong một kho dữ liệu lai có thể bao gồm cơ sở dữ liệu vector, đồ thị và khóa-giá trị. Hệ thống này cũng hỗ trợ nhiều loại bộ nhớ và có thể tích hợp bộ nhớ dạng đồ thị để quản lý các mối quan hệ giữa các thực thể.

#### Cognee

Một phương pháp mạnh mẽ khác là sử dụng **Cognee**, một bộ nhớ ngữ nghĩa nguồn mở cho các đại lý AI chuyển đổi dữ liệu có cấu trúc và không có cấu trúc thành đồ thị kiến thức có thể truy vấn dựa trên embeddings. Cognee cung cấp **kiến trúc lưu trữ kép** kết hợp tìm kiếm tương tự vector với mối quan hệ đồ thị, cho phép các đại lý hiểu không chỉ thông tin nào tương tự, mà còn cách các khái niệm liên quan đến nhau.

Nó ưu việt ở **truy xuất lai** kết hợp sự tương đồng vector, cấu trúc đồ thị và lập luận LLM - từ việc tra cứu các đoạn dữ liệu thô đến trả lời câu hỏi có nhận thức đồ thị. Hệ thống duy trì **bộ nhớ sống động** phát triển và mở rộng trong khi vẫn có thể truy vấn như một đồ thị kết nối duy nhất, hỗ trợ cả bối cảnh phiên ngắn hạn và bộ nhớ bền vững dài hạn.

Hướng dẫn notebook Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) trình bày cách xây dựng lớp bộ nhớ thống nhất này, với các ví dụ thực tiễn về việc nhập dữ liệu đa dạng, trực quan hóa đồ thị kiến thức, và tra cứu với các chiến lược tìm kiếm khác nhau phù hợp với nhu cầu cụ thể của đại lý.

### Lưu trữ Bộ nhớ với RAG

Ngoài các công cụ bộ nhớ chuyên biệt như Mem0, bạn có thể tận dụng các dịch vụ tìm kiếm mạnh mẽ như **Azure AI Search làm nền tảng lưu trữ và truy xuất kí ức**, đặc biệt cho Structured RAG.

Điều này cho phép bạn củng cố câu trả lời của đại lý với dữ liệu riêng của bạn, đảm bảo các câu trả lời phù hợp và chính xác hơn. Azure AI Search có thể được sử dụng để lưu trữ kí ức chuyến đi cụ thể người dùng, danh mục sản phẩm, hoặc bất kỳ kiến thức chuyên môn nào khác.

Azure AI Search hỗ trợ các khả năng như **Structured RAG**, ưu việt trong việc trích xuất và truy xuất thông tin cô đọng, có cấu trúc từ các tập dữ liệu lớn như lịch sử cuộc trò chuyện, email, hoặc thậm chí hình ảnh. Điều này cung cấp độ chính xác và khả năng truy xuất "siêu nhân" so với các phương pháp truyền thống như phân đoạn văn bản và nhúng.

## Làm cho các Đại lý AI Tự Cải tiến

Một mô hình phổ biến cho đại lý tự cải tiến là giới thiệu một **"đại lý kiến thức"**. Đại lý riêng biệt này quan sát cuộc trò chuyện chính giữa người dùng và đại lý chính. Vai trò của nó là:

1. **Xác định thông tin quý giá**: Xác định xem phần nào của cuộc trò chuyện đáng lưu như kiến thức chung hoặc sở thích người dùng cụ thể.

2. **Trích xuất và tóm tắt**: Chắt lọc kiến thức hoặc sở thích cốt lõi từ cuộc trò chuyện.

3. **Lưu trữ trong cơ sở kiến thức**: Lưu giữ thông tin trích xuất, thường trong cơ sở dữ liệu vector, để có thể truy xuất sau này.

4. **Tăng cường truy vấn trong tương lai**: Khi người dùng khởi tạo một truy vấn mới, đại lý kiến thức truy xuất thông tin lưu trữ liên quan và đính kèm nó vào yêu cầu của người dùng, cung cấp bối cảnh quan trọng cho đại lý chính (tương tự như RAG).

### Tối ưu hóa cho Bộ nhớ

• **Quản lý Độ trễ**: Để tránh làm chậm các tương tác với người dùng, một mô hình rẻ hơn, nhanh hơn có thể được sử dụng ban đầu để nhanh chóng kiểm tra xem thông tin có đáng lưu hoặc truy xuất không, chỉ gọi quy trình trích xuất/truy xuất phức tạp hơn khi cần thiết.

• **Bảo trì Cơ sở Kiến thức**: Đối với cơ sở kiến thức ngày càng mở rộng, các thông tin ít được sử dụng hơn có thể được chuyển đến "kho lưu trữ lạnh" để quản lý chi phí.

## Bạn Có Thắc Mắc Thêm về Bộ nhớ Đại lý?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ các học viên khác, tham dự giờ làm việc và nhận được câu trả lời cho các câu hỏi về Đại lý AI của bạn.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->