<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1923cf93aba522a5f4a493597112a893",
  "translation_date": "2025-09-18T16:16:54+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "vi"
}
-->
# Bộ nhớ cho các tác nhân AI

Khi thảo luận về những lợi ích độc đáo của việc tạo ra các tác nhân AI, hai điều chính thường được nhắc đến: khả năng gọi công cụ để hoàn thành nhiệm vụ và khả năng cải thiện theo thời gian. Bộ nhớ là nền tảng để tạo ra các tác nhân tự cải thiện, mang lại trải nghiệm tốt hơn cho người dùng.

Trong bài học này, chúng ta sẽ tìm hiểu bộ nhớ là gì đối với các tác nhân AI, cách quản lý và sử dụng nó để mang lại lợi ích cho ứng dụng của chúng ta.

## Giới thiệu

Bài học này sẽ bao gồm:

• **Hiểu về bộ nhớ của tác nhân AI**: Bộ nhớ là gì và tại sao nó quan trọng đối với các tác nhân.

• **Triển khai và lưu trữ bộ nhớ**: Các phương pháp thực tiễn để thêm khả năng bộ nhớ vào các tác nhân AI, tập trung vào bộ nhớ ngắn hạn và dài hạn.

• **Làm cho các tác nhân AI tự cải thiện**: Cách bộ nhớ cho phép các tác nhân học hỏi từ các tương tác trước và cải thiện theo thời gian.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

• **Phân biệt giữa các loại bộ nhớ của tác nhân AI**, bao gồm bộ nhớ làm việc, bộ nhớ ngắn hạn, bộ nhớ dài hạn, cũng như các dạng chuyên biệt như bộ nhớ nhân vật và bộ nhớ theo tập.

• **Triển khai và quản lý bộ nhớ ngắn hạn và dài hạn cho các tác nhân AI** bằng cách sử dụng khung Semantic Kernel, tận dụng các công cụ như Mem0 và bộ nhớ Whiteboard, và tích hợp với Azure AI Search.

• **Hiểu các nguyên tắc đằng sau các tác nhân AI tự cải thiện** và cách các hệ thống quản lý bộ nhớ mạnh mẽ góp phần vào việc học hỏi và thích nghi liên tục.

## Hiểu về bộ nhớ của tác nhân AI

Về cốt lõi, **bộ nhớ của tác nhân AI đề cập đến các cơ chế cho phép chúng lưu giữ và nhớ lại thông tin**. Thông tin này có thể là các chi tiết cụ thể về một cuộc trò chuyện, sở thích của người dùng, hành động trước đây, hoặc thậm chí là các mẫu đã học.

Không có bộ nhớ, các ứng dụng AI thường không có trạng thái, nghĩa là mỗi tương tác bắt đầu từ đầu. Điều này dẫn đến trải nghiệm người dùng lặp lại và gây khó chịu khi tác nhân "quên" ngữ cảnh hoặc sở thích trước đó.

### Tại sao bộ nhớ quan trọng?

Trí thông minh của một tác nhân gắn liền với khả năng nhớ lại và sử dụng thông tin trước đó. Bộ nhớ cho phép các tác nhân trở nên:

• **Phản chiếu**: Học hỏi từ các hành động và kết quả trước đây.

• **Tương tác**: Duy trì ngữ cảnh trong một cuộc trò chuyện liên tục.

• **Chủ động và phản ứng**: Dự đoán nhu cầu hoặc phản hồi phù hợp dựa trên dữ liệu lịch sử.

• **Tự động**: Hoạt động độc lập hơn bằng cách dựa vào kiến thức đã lưu trữ.

Mục tiêu của việc triển khai bộ nhớ là làm cho các tác nhân trở nên **đáng tin cậy và có khả năng hơn**.

### Các loại bộ nhớ

#### Bộ nhớ làm việc

Hãy nghĩ về nó như một tờ giấy nháp mà tác nhân sử dụng trong một nhiệm vụ hoặc quá trình suy nghĩ đang diễn ra. Nó giữ thông tin ngay lập tức cần thiết để tính toán bước tiếp theo.

Đối với các tác nhân AI, bộ nhớ làm việc thường nắm bắt thông tin quan trọng nhất từ một cuộc trò chuyện, ngay cả khi lịch sử trò chuyện đầy đủ dài hoặc bị cắt ngắn. Nó tập trung vào việc trích xuất các yếu tố chính như yêu cầu, đề xuất, quyết định và hành động.

**Ví dụ về bộ nhớ làm việc**

Trong một tác nhân đặt vé du lịch, bộ nhớ làm việc có thể nắm bắt yêu cầu hiện tại của người dùng, chẳng hạn như "Tôi muốn đặt một chuyến đi đến Paris". Yêu cầu cụ thể này được giữ trong ngữ cảnh ngay lập tức của tác nhân để hướng dẫn tương tác hiện tại.

#### Bộ nhớ ngắn hạn

Loại bộ nhớ này giữ thông tin trong suốt một cuộc trò chuyện hoặc phiên làm việc. Đây là ngữ cảnh của cuộc trò chuyện hiện tại, cho phép tác nhân tham chiếu lại các lượt trước trong đối thoại.

**Ví dụ về bộ nhớ ngắn hạn**

Nếu người dùng hỏi, "Một chuyến bay đến Paris sẽ có giá bao nhiêu?" và sau đó tiếp tục với "Còn chỗ ở tại đó thì sao?", bộ nhớ ngắn hạn đảm bảo tác nhân biết "tại đó" đề cập đến "Paris" trong cùng cuộc trò chuyện.

#### Bộ nhớ dài hạn

Đây là thông tin tồn tại qua nhiều cuộc trò chuyện hoặc phiên làm việc. Nó cho phép các tác nhân nhớ sở thích của người dùng, các tương tác lịch sử, hoặc kiến thức chung trong thời gian dài. Điều này rất quan trọng đối với việc cá nhân hóa.

**Ví dụ về bộ nhớ dài hạn**

Bộ nhớ dài hạn có thể lưu trữ rằng "Ben thích trượt tuyết và các hoạt động ngoài trời, thích cà phê với khung cảnh núi non, và muốn tránh các dốc trượt tuyết khó do một chấn thương trước đây". Thông tin này, được học từ các tương tác trước, ảnh hưởng đến các đề xuất trong các phiên lập kế hoạch du lịch tương lai, làm cho chúng trở nên cá nhân hóa cao.

#### Bộ nhớ nhân vật

Loại bộ nhớ chuyên biệt này giúp một tác nhân phát triển một "tính cách" hoặc "vai trò" nhất quán. Nó cho phép tác nhân nhớ các chi tiết về bản thân hoặc vai trò dự định của nó, làm cho các tương tác trở nên mượt mà và tập trung hơn.

**Ví dụ về bộ nhớ nhân vật**

Nếu tác nhân du lịch được thiết kế để trở thành một "chuyên gia lập kế hoạch trượt tuyết", bộ nhớ nhân vật có thể củng cố vai trò này, ảnh hưởng đến các phản hồi của nó để phù hợp với giọng điệu và kiến thức của một chuyên gia.

#### Bộ nhớ theo tập/luồng công việc

Bộ nhớ này lưu trữ trình tự các bước mà một tác nhân thực hiện trong một nhiệm vụ phức tạp, bao gồm cả thành công và thất bại. Nó giống như việc nhớ lại các "tập" hoặc trải nghiệm trước đây để học hỏi từ chúng.

**Ví dụ về bộ nhớ theo tập**

Nếu tác nhân cố gắng đặt một chuyến bay cụ thể nhưng thất bại do không có chỗ, bộ nhớ theo tập có thể ghi lại thất bại này, cho phép tác nhân thử các chuyến bay thay thế hoặc thông báo cho người dùng về vấn đề một cách thông minh hơn trong lần thử sau.

#### Bộ nhớ thực thể

Điều này liên quan đến việc trích xuất và ghi nhớ các thực thể cụ thể (như người, địa điểm, hoặc vật) và các sự kiện từ các cuộc trò chuyện. Nó cho phép tác nhân xây dựng một hiểu biết có cấu trúc về các yếu tố chính được thảo luận.

**Ví dụ về bộ nhớ thực thể**

Từ một cuộc trò chuyện về một chuyến đi trước đây, tác nhân có thể trích xuất "Paris," "Tháp Eiffel," và "bữa tối tại nhà hàng Le Chat Noir" như các thực thể. Trong một tương tác tương lai, tác nhân có thể nhớ "Le Chat Noir" và đề nghị đặt chỗ mới tại đó.

#### RAG có cấu trúc (Retrieval Augmented Generation)

Mặc dù RAG là một kỹ thuật rộng hơn, "RAG có cấu trúc" được nhấn mạnh như một công nghệ bộ nhớ mạnh mẽ. Nó trích xuất thông tin dày đặc, có cấu trúc từ nhiều nguồn (cuộc trò chuyện, email, hình ảnh) và sử dụng nó để tăng độ chính xác, khả năng nhớ lại, và tốc độ trong các phản hồi. Không giống như RAG cổ điển chỉ dựa vào sự tương đồng ngữ nghĩa, RAG có cấu trúc hoạt động với cấu trúc vốn có của thông tin.

**Ví dụ về RAG có cấu trúc**

Thay vì chỉ khớp từ khóa, RAG có cấu trúc có thể phân tích chi tiết chuyến bay (điểm đến, ngày, giờ, hãng hàng không) từ một email và lưu trữ chúng theo cách có cấu trúc. Điều này cho phép các truy vấn chính xác như "Chuyến bay nào tôi đã đặt đến Paris vào thứ Ba?"

## Triển khai và lưu trữ bộ nhớ

Triển khai bộ nhớ cho các tác nhân AI bao gồm một quy trình hệ thống về **quản lý bộ nhớ**, bao gồm tạo, lưu trữ, truy xuất, tích hợp, cập nhật, và thậm chí "quên" (hoặc xóa) thông tin. Truy xuất là một khía cạnh đặc biệt quan trọng.

### Công cụ bộ nhớ chuyên biệt

Một cách để lưu trữ và quản lý bộ nhớ của tác nhân là sử dụng các công cụ chuyên biệt như Mem0. Mem0 hoạt động như một lớp bộ nhớ liên tục, cho phép các tác nhân nhớ lại các tương tác liên quan, lưu trữ sở thích của người dùng và ngữ cảnh thực tế, và học hỏi từ thành công và thất bại theo thời gian. Ý tưởng ở đây là biến các tác nhân không trạng thái thành có trạng thái.

Nó hoạt động thông qua **quy trình bộ nhớ hai giai đoạn: trích xuất và cập nhật**. Đầu tiên, các tin nhắn được thêm vào luồng của tác nhân được gửi đến dịch vụ Mem0, sử dụng Mô hình Ngôn ngữ Lớn (LLM) để tóm tắt lịch sử cuộc trò chuyện và trích xuất các bộ nhớ mới. Sau đó, giai đoạn cập nhật do LLM điều khiển xác định liệu có nên thêm, sửa đổi, hay xóa các bộ nhớ này, lưu trữ chúng trong một kho dữ liệu lai có thể bao gồm cơ sở dữ liệu vector, đồ thị, và key-value. Hệ thống này cũng hỗ trợ các loại bộ nhớ khác nhau và có thể kết hợp bộ nhớ đồ thị để quản lý mối quan hệ giữa các thực thể.

### Lưu trữ bộ nhớ với RAG

Ngoài các công cụ bộ nhớ chuyên biệt như Mem0, bạn có thể tận dụng các dịch vụ tìm kiếm mạnh mẽ như **Azure AI Search làm backend để lưu trữ và truy xuất bộ nhớ**, đặc biệt đối với RAG có cấu trúc.

Điều này cho phép bạn căn cứ các phản hồi của tác nhân vào dữ liệu của riêng bạn, đảm bảo các câu trả lời phù hợp và chính xác hơn. Azure AI Search có thể được sử dụng để lưu trữ bộ nhớ du lịch cụ thể của người dùng, danh mục sản phẩm, hoặc bất kỳ kiến thức chuyên ngành nào khác.

Azure AI Search hỗ trợ các khả năng như **RAG có cấu trúc**, nổi trội trong việc trích xuất và truy xuất thông tin dày đặc, có cấu trúc từ các tập dữ liệu lớn như lịch sử cuộc trò chuyện, email, hoặc thậm chí hình ảnh. Điều này mang lại "độ chính xác và khả năng nhớ lại siêu nhân" so với các phương pháp phân đoạn văn bản và nhúng truyền thống.

## Làm cho các tác nhân AI tự cải thiện

Một mô hình phổ biến cho các tác nhân tự cải thiện là giới thiệu một **"tác nhân kiến thức"**. Tác nhân riêng biệt này quan sát cuộc trò chuyện chính giữa người dùng và tác nhân chính. Vai trò của nó là:

1. **Xác định thông tin có giá trị**: Xác định xem phần nào của cuộc trò chuyện đáng lưu giữ như kiến thức chung hoặc sở thích cụ thể của người dùng.

2. **Trích xuất và tóm tắt**: Chắt lọc thông tin học hỏi hoặc sở thích thiết yếu từ cuộc trò chuyện.

3. **Lưu trữ trong cơ sở kiến thức**: Lưu giữ thông tin đã trích xuất, thường trong cơ sở dữ liệu vector, để có thể truy xuất sau.

4. **Bổ sung các truy vấn tương lai**: Khi người dùng bắt đầu một truy vấn mới, tác nhân kiến thức truy xuất thông tin đã lưu trữ liên quan và thêm vào lời nhắc của người dùng, cung cấp ngữ cảnh quan trọng cho tác nhân chính (tương tự như RAG).

### Tối ưu hóa cho bộ nhớ

• **Quản lý độ trễ**: Để tránh làm chậm các tương tác của người dùng, một mô hình rẻ hơn, nhanh hơn có thể được sử dụng ban đầu để nhanh chóng kiểm tra xem thông tin có giá trị để lưu trữ hoặc truy xuất hay không, chỉ kích hoạt quy trình trích xuất/truy xuất phức tạp hơn khi cần thiết.

• **Bảo trì cơ sở kiến thức**: Đối với một cơ sở kiến thức đang phát triển, thông tin ít được sử dụng hơn có thể được chuyển sang "lưu trữ lạnh" để quản lý chi phí.

## Có thêm câu hỏi về kỹ thuật ngữ cảnh?

Tham gia [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ các học viên khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về tác nhân AI của bạn.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.