# Tác nhân AI cho Người mới bắt đầu - Hướng dẫn học tập

Sử dụng hướng dẫn này như một người bạn đồng hành thực tiễn khi bạn tiến hành khoá học. Nó
không nhằm thay thế các bài học. Nó giúp bạn quyết định bắt đầu từ đâu, nên
tìm gì trong mỗi bài học, và cách kết nối các ý tưởng thành một bản demo tác nhân
nhỏ hoạt động được.

Nếu đây là lần đầu bạn đến đây, hãy bắt đầu đơn giản:

1. Đọc [Cài đặt Khoá học](./00-course-setup/README.md).
2. Hoàn thành các Bài học 01-06 theo thứ tự.
3. Giữ một ý tưởng demo nhỏ trong đầu trong khi học.
4. Sau mỗi bài học, hãy hỏi: "Tác nhân của tôi bây giờ có thể làm gì mà trước đây
   không thể làm được?"

## Một Demo Đơn giản để Ghi nhớ

Một cách tốt để học về các tác nhân là theo một ý tưởng demo trong suốt khoá học.

Ví dụ demo: **một tác nhân trợ giúp khoá học**.

Người dùng hỏi:

> "Tôi muốn học cách tác nhân sử dụng công cụ. Tìm các bài học phù hợp, tóm tắt những gì
> tôi nên đọc trước, và cho tôi một bài tập thực hành ngắn."

Một chatbot thông thường có thể trả lời dựa trên những gì nó đã biết. Một tác nhân có thể làm được nhiều hơn:

1. **Đọc hoặc tìm kiếm các tập tin khoá học** để tìm bài học phù hợp.
2. **Sử dụng công cụ** để truy xuất liên kết bài học, ví dụ hoặc tài liệu hỗ trợ.
3. **Lập kế hoạch** một lộ trình học ngắn thay vì đưa ra câu trả lời dài.
4. **Sử dụng ngữ cảnh** từ cuộc trò chuyện hiện tại để giữ tập trung vào mục tiêu của người học.

5. **Nhớ sở thích hữu ích** nếu ứng dụng hỗ trợ bộ nhớ.
6. **Hiển thị dấu vết, trích dẫn hoặc nhật ký** để người dùng hiểu những gì đã xảy ra.
7. **Áp dụng các hàng rào bảo vệ** trước khi thực hiện các hành động rủi ro hoặc sử dụng dữ liệu nhạy cảm.

Khi bạn học từng bài, hãy trở lại với demo này và hỏi: bài học này sẽ thêm khả năng mới gì?


## Những gì bạn đang hướng tới xây dựng

Đến cuối khoá học, bạn nên có khả năng giải thích và xây dựng hệ thống tác nhân
kết hợp các phần sau:

| Phần | Ý nghĩa theo ngôn ngữ thường ngày | Trong demo |
|------|------------------------|-------------|
| Mô hình | Bộ máy suy luận giải thích yêu cầu của người dùng | Hiểu rằng người học muốn các bài học về sử dụng công cụ |
| Công cụ | Các hàm, API, tệp, trình duyệt hoặc dịch vụ mà tác nhân có thể sử dụng | Tìm kiếm trong kho hoặc truy xuất nội dung bài học |
| Kiến thức | Các tài liệu hoặc dữ liệu dùng để căn cứ cho câu trả lời | Các tệp README khoá học và tài liệu bài học |
| Ngữ cảnh | Thông tin bao gồm trong lần gọi mô hình tiếp theo | Mục tiêu của người dùng và kết quả từ công cụ |
| Bộ nhớ | Thông tin được lưu lại để sử dụng sau | Người học thích ví dụ thực hành Python |
| Lập kế hoạch | Phân chia mục tiêu lớn thành các bước nhỏ hơn | Tìm bài học, tóm tắt, đề xuất thực hành |
| Điều phối | Phân phối công việc qua các công cụ, bước hoặc tác nhân | Người lập kế hoạch gọi công cụ tìm kiếm, sau đó là tóm tắt |
| Độ tin cậy | An toàn, bảo mật, đánh giá, và quan sát | Ghi nhật ký các lần gọi công cụ và hỏi trước khi thực hiện hành động ảnh hưởng lớn |

## Mô hình và Nhà cung cấp

Các ví dụ mã khoá học sử dụng **Microsoft Agent Framework (MAF)** và hướng tới **Azure OpenAI Responses API** — API được khuyến nghị trong tương lai, kết hợp trả lời trò chuyện, gọi công cụ, đầu vào đa phương tiện, và các cuộc trò chuyện có trạng thái trong một bề mặt API duy nhất. Bạn kết nối thông qua dự án **Microsoft Foundry** (với `FoundryChatClient`) hoặc trực tiếp qua Azure OpenAI (với `OpenAIChatClient`).

Khi học qua các bài, bạn có một số lựa chọn nhà cung cấp:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — đường dẫn chính được sử dụng xuyên suốt các bài học. Đăng nhập bằng `az login` để xác thực Entra ID không cần khoá.
- **Foundry Local** — chạy mô hình hoàn toàn trên thiết bị qua API tương thích OpenAI (không dùng đám mây, không khoá API). Lý tưởng cho thử nghiệm ngoại tuyến hoặc miễn phí. Xem [Cài đặt Khoá học](./00-course-setup/README.md).
- **MiniMax** — nhà cung cấp tương thích OpenAI với mô hình ngữ cảnh lớn, có thể thay thế dễ dàng.

> **Lưu ý:** GitHub Models đã bị ngừng (ngừng hoạt động vào tháng 7 năm 2026) và không hỗ trợ Responses API. Các mẫu đã được cập nhật để dùng Azure OpenAI / Microsoft Foundry thay thế.

## Chọn Lộ trình Học tập

Bạn có thể học toàn bộ khoá theo thứ tự, hoặc chọn lộ trình dựa trên những gì bạn muốn
xây dựng.

| Nếu mục tiêu của bạn là... | Bắt đầu với | Sau đó học |
|-----------------------|------------|------------|
| Hiểu tác nhân là gì | 01, 02, 03 | 04, 05, 06 |
| Xây dựng tác nhân sử dụng công cụ | 04 | 05, 07, 14 |
| Xây dựng tác nhân dựa trên RAG | 05 | 04, 06, 12 |
| Thiết kế luồng công việc nhiều bước | 07 | 08, 09, 14 |
| Hiểu hệ thống đa tác nhân | 08 | 07, 09, 11 |
| Chuẩn bị tác nhân cho sản xuất | 06, 10 | 12, 13, 18 |
| Khám phá giao thức và tự động hóa trình duyệt | 11, 15 | 10, 18 |

Mẹo: nếu bạn là người mới về tác nhân, đừng bỏ qua các Bài học 01-06. Chúng cung cấp
từ vựng cần thiết cho phần còn lại của khoá học.

## Hướng dẫn từng Bài học

| Bài học | Bạn học được gì | Thử làm điều này sau bài học |
|--------|----------------|---------------------------|
| [01 - Giới thiệu về Tác nhân AI](./01-intro-to-ai-agents/README.md) | Tác nhân khác chatbot thông thường như thế nào. | Giải thích ý tưởng demo của bạn như một tác nhân, không chỉ là ứng dụng chat. |
| [02 - Các Framework Tác nhân](./02-explore-agentic-frameworks/README.md) | Các framework giúp với mô hình, công cụ, trạng thái, và luồng công việc. | Xác định phần nào của demo bạn framework sẽ quản lý. |
| [03 - Mẫu Thiết kế Tác nhân](./03-agentic-design-patterns/README.md) | Các mẫu phổ biến để thiết kế hành vi tác nhân. | Phác thảo hành trình người dùng trước khi viết mã. |
| [04 - Sử dụng Công cụ](./04-tool-use/README.md) | Cách tác nhân gọi công cụ để lấy dữ liệu hoặc thực hiện hành động. | Xác định một công cụ mà tác nhân demo của bạn cần có. |
| [05 - RAG tác nhân](./05-agentic-rag/README.md) | Cách truy xuất củng cố câu trả lời của tác nhân trên tài liệu hoặc dữ liệu. | Quyết định nguồn kiến thức mà demo của bạn nên tìm kiếm. |
| [06 - Tác nhân Đáng tin cậy](./06-building-trustworthy-agents/README.md) | Cách thêm hàng rào bảo vệ, giám sát, và hành vi an toàn hơn. | Thêm một quy tắc để khi nào tác nhân cần hỏi người dùng trước. |
| [07 - Thiết kế Lập kế hoạch](./07-planning-design/README.md) | Cách tác nhân phân chia mục tiêu lớn thành các bước nhỏ. | Viết kế hoạch ba bước cho yêu cầu demo của bạn. |

| [08 - Thiết kế đa tác nhân](./08-multi-agent/README.md) | Khi nào nên phân chia công việc cho các tác nhân chuyên biệt. | Quyết định xem bản demo của bạn cần một tác nhân hay nhiều tác nhân. |
| [09 - Siêu nhận thức](./09-metacognition/README.md) | Làm thế nào để các tác nhân có thể xem xét và cải thiện kết quả của chính họ. | Thêm một bước tự kiểm tra cuối cùng trước khi tác nhân phản hồi. |
| [10 - Các tác nhân AI trong sản xuất](./10-ai-agents-production/README.md) | Điều gì thay đổi khi một tác nhân chuyển từ bản demo sang sản xuất. | Liệt kê những gì bạn sẽ theo dõi: chất lượng, chi phí, độ trễ, lỗi. |
| [11 - Giao thức tác nhân](./11-agentic-protocols/README.md) | Cách các giao thức kết nối tác nhân với công cụ và các tác nhân khác. | Xác định nơi một giao thức chuẩn có thể đơn giản hóa việc tích hợp. |
| [12 - Kỹ thuật ngữ cảnh](./12-context-engineering/README.md) | Cách chọn, cắt, cô lập và quản lý ngữ cảnh. | Quyết định cái gì nên nằm trong prompt và cái gì nên để ngoài. |
| [13 - Bộ nhớ tác nhân](./13-agent-memory/README.md) | Cách các tác nhân có thể lưu giữ thông tin hữu ích qua các tương tác. | Chọn một sở thích an toàn mà bản demo của bạn có thể ghi nhớ. |
| [14 - Khung tác nhân Microsoft](./14-microsoft-agent-framework/README.md) | Các khối xây dựng đặc thù của khung cho tác nhân và quy trình làm việc, cùng với việc lưu trữ tác nhân LangChain/LangGraph trên Microsoft Foundry. | Ánh xạ các bước demo của bạn tới các khái niệm trong khung. |
| [15 - Tác nhân sử dụng máy tính](./15-browser-use/README.md) | Cách các tác nhân có thể tương tác với trình duyệt hoặc giao diện người dùng, bao gồm các ví dụ thực tế như Microsoft Project Opal. | Chọn một tác vụ trình duyệt vẫn nên yêu cầu xác nhận từ người dùng. |
| [18 - Bảo mật tác nhân AI](./18-securing-ai-agents/README.md) | Cách làm cho các hành động của tác nhân dễ kiểm tra và tránh bị giả mạo. | Quyết định hành động nào trong bản demo của bạn nên được ghi lại hoặc có biên nhận. |

Các bài học 16 và 17 được liệt kê trong README chính là sẽ sớm xuất hiện. Thêm chúng vào
kế hoạch học tập của bạn khi nội dung bài học có sẵn.

## Ý tưởng chính bằng ngôn ngữ thân thiện với người mới bắt đầu

### Công cụ

Công cụ là thứ mà tác nhân có thể gọi để thực hiện công việc bên ngoài mô hình. Một công cụ tốt
có tên rõ ràng, công việc hẹp, đầu vào kiểu dữ liệu, đầu ra dự đoán được, và cách thất bại an toàn.


Đối với bản demo trợ lý khóa học, một công cụ có thể là:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG và kiến thức

RAG giúp tác nhân trả lời dựa trên tài liệu nguồn thay vì đoán mò. Trong
khóa học này, tài liệu nguồn có thể là README bài học, mẫu code, hoặc tài nguyên bên ngoài
được liên kết từ các bài học.

Dùng RAG khi câu trả lời nên được căn cứ trên tài liệu, dữ liệu hoặc các tập tin dự án hiện tại.


### Lập kế hoạch

Lập kế hoạch hữu ích khi yêu cầu có nhiều hơn một bước. Giữ kế hoạch ngắn gọn và
đủ rõ ràng để nhà phát triển hoặc người dùng có thể kiểm tra.

Đối với bản demo, một kế hoạch có thể là:

1. Tìm các bài học liên quan đến việc sử dụng công cụ.
2. Tóm tắt các bài học có liên quan nhất.
3. Đề xuất một bài tập thực hành.

### Ngữ cảnh

Ngữ cảnh là những gì mô hình đang nhìn thấy lúc này. Ngữ cảnh quá ít có thể khiến tác nhân
bỏ lỡ các chi tiết quan trọng. Ngữ cảnh quá nhiều có thể khiến tác nhân chậm hơn, tốn kém hơn,
hoặc dễ bị nhầm lẫn hơn.

Kỹ thuật ngữ cảnh tốt là chọn đúng thông tin cho lần gọi mô hình tiếp theo.




khi nó hữu ích, an toàn và dễ cập nhật hoặc xóa.


Ghi nhớ dữ liệu cá nhân nhạy cảm thường không nên.


### Đánh giá và khả năng quan sát

Đánh giá đặt câu hỏi: tác nhân có làm đúng không?

Khả năng quan sát hỏi: chúng ta có thể thấy quá trình diễn ra như thế nào không?

Đối với tác nhân sản xuất, theo dõi các lần gọi mô hình, gọi công cụ, ngữ cảnh được truy xuất,
độ trễ, chi phí, lỗi và phản hồi người dùng.

### Tin cậy và bảo mật

Các tác nhân đáng tin cậy cần hơn một prompt hữu ích. Dùng công cụ quyền hạn tối thiểu,
phê duyệt của con người cho các hành động ảnh hưởng cao, che giấu dữ liệu khi cần, và nhật ký hoặc
biên nhận cho các hành động cần được kiểm toán.

## Quy trình ôn tập 15 phút

Dùng quy trình này sau mỗi bài học:

1. **Tóm tắt bài học bằng một câu.**
2. **Nêu tên khả năng tác nhân mới.** Ví dụ: sử dụng công cụ, truy xuất,
   lập kế hoạch, bộ nhớ, khả năng quan sát, hoặc bảo mật.
3. **Thêm vào bản demo trợ lý khóa học.** Bây giờ bản demo thay đổi ra sao?
4. **Tìm rủi ro.** Điều gì có thể sai nếu khả năng này bị sử dụng sai?
5. **Viết một câu hỏi kiểm tra.** Bạn sẽ kiểm tra tác nhân hoạt động tốt bằng cách nào?

## Tự kiểm tra nhanh

Trước khi tiếp tục, hãy thử trả lời các câu hỏi sau:

1. Một tác nhân có thể làm gì mà chatbot thông thường không làm được một mình?
2. Công cụ nào tác nhân của bạn cần đầu tiên, và vì sao?
3. Nguồn kiến thức nào nên làm nền tảng cho câu trả lời của tác nhân?
4. Ngữ cảnh nào nên được bao gồm trong lần gọi mô hình tiếp theo?
5. Tác nhân nên nhớ gì, và nên tránh lưu gì?
6. Khi nào tác nhân nên yêu cầu phê duyệt từ con người?
7. Nhật ký, dấu vết, hoặc biên nhận nào sẽ giúp bạn gỡ lỗi hoặc kiểm toán tác nhân sau này?

## Bài tập cuối khóa được đề xuất

Cuối khóa, hãy xây dựng một tác nhân nhỏ giúp người học điều hướng
kho lưu trữ này.

Phiên bản tối thiểu:

- Nhận một chủ đề từ người dùng.
- Tìm các bài học liên quan nhất.
- Tóm tắt những gì nên đọc trước.
- Đề xuất một bài tập thực hành.
- Hiển thị những tập tin bài học hoặc liên kết đã dùng.

Phiên bản nâng cao:

- Ghi nhớ ngôn ngữ lập trình ưu tiên của người học.
- Dùng kế hoạch đơn giản trước khi trả lời.
- Thêm bước tự kiểm tra trước phản hồi cuối cùng.
- Ghi lại các lần gọi công cụ và nguồn truy xuất.
- Yêu cầu xác nhận trước khi mở trình duyệt hoặc tác vụ tự động hóa giao diện người dùng.

Cách này cung cấp cho bạn một phương án nhỏ nhưng thực tế để thực hành công cụ, RAG, lập kế hoạch,
ngữ cảnh, bộ nhớ, khả năng quan sát và tin cậy trong cùng một dự án.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->