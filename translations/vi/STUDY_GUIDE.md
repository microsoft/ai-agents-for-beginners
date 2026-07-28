# Đại lý AI cho người mới bắt đầu - Hướng dẫn học tập

Sử dụng hướng dẫn này như một người bạn đồng hành thực tiễn khi bạn tiến hành khóa học. Nó
không nhằm thay thế các bài học. Nó giúp bạn quyết định bắt đầu từ đâu, nên
tìm kiếm gì trong mỗi bài học và làm thế nào để kết nối các ý tưởng thành một bản trình diễn
đại lý nhỏ vận hành được.

Nếu đây là lần đầu tiên bạn đến đây, hãy bắt đầu đơn giản:

1. Đọc [Thiết lập khóa học](./00-course-setup/README.md).
2. Hoàn thành các Bài học 01-06 theo thứ tự.
3. Giữ một ý tưởng demo nhỏ trong đầu khi học.
4. Sau mỗi bài học, hãy hỏi: "Đại lý của tôi có thể làm gì bây giờ mà trước đó nó không thể làm?
   "

## Một bản demo đơn giản để nhớ

Một cách tốt để học về đại lý là theo dõi một ý tưởng demo xuyên suốt khóa học.

Ví dụ demo: **một đại lý trợ giúp khóa học**.

Người dùng hỏi:

> "Tôi muốn học cách các đại lý sử dụng công cụ. Tìm các bài học phù hợp, tóm tắt những gì
> tôi nên đọc trước, và cho tôi một bài tập thực hành ngắn."

Một chatbot thường có thể trả lời dựa trên những gì nó đã biết. Một đại lý có thể làm nhiều hơn:

1. **Đọc hoặc tìm kiếm tệp khóa học** để tìm các bài học phù hợp.
2. **Sử dụng công cụ** để lấy liên kết bài học, ví dụ hoặc tài liệu hỗ trợ.
3. **Lập kế hoạch** một lộ trình học tập ngắn thay vì đưa ra một câu trả lời dài.
4. **Sử dụng ngữ cảnh** từ cuộc trò chuyện hiện tại để tập trung vào
   mục tiêu của người học.
5. **Ghi nhớ các sở thích hữu ích** nếu ứng dụng hỗ trợ bộ nhớ.
6. **Hiển thị dấu vết, trích dẫn hoặc nhật ký** để người dùng có thể hiểu điều đã xảy ra.
7. **Áp dụng các biện pháp an toàn** trước khi thực hiện các hành động rủi ro hoặc sử dụng dữ liệu nhạy cảm.

Khi bạn học mỗi bài, hãy quay lại demo này và hỏi: bài học này sẽ thêm khả năng mới gì?


## Những gì bạn đang hướng tới xây dựng

Cuối khóa học, bạn nên có khả năng giải thích và xây dựng các hệ thống đại lý
kết hợp các phần sau:

| Phần | Ý nghĩa bằng ngôn ngữ đơn giản | Trong demo |
|------|------------------------|-------------|
| Mô hình | Bộ máy suy luận giải thích yêu cầu của người dùng | Hiểu rằng người học muốn các bài học về cách sử dụng công cụ |
| Công cụ | Các chức năng, API, tệp, trình duyệt hoặc dịch vụ mà đại lý có thể sử dụng | Tìm kiếm kho lưu trữ hoặc truy xuất nội dung bài học |
| Kiến thức | Tài liệu hoặc dữ liệu dùng để làm cơ sở trả lời | Các tệp README và tài liệu bài học khóa học |
| Ngữ cảnh | Thông tin bao gồm trong lần gọi mô hình tiếp theo | Mục tiêu của người dùng và kết quả công cụ |
| Bộ nhớ | Thông tin được lưu giữ để sử dụng sau | Người học ưu tiên ví dụ Python thực hành |
| Lập kế hoạch | Phân chia mục tiêu lớn thành các bước nhỏ hơn | Tìm bài học, tóm tắt chúng, gợi ý thực hành |
| Điều phối | Phân phối công việc qua công cụ, bước hoặc đại lý | Một bộ lập kế hoạch gọi công cụ tìm kiếm, sau đó là bộ tóm tắt |
| Niềm tin | An toàn, bảo mật, đánh giá và giám sát | Ghi lại các cuộc gọi công cụ và hỏi trước khi thực hiện tác vụ ảnh hưởng cao |

## Mô hình và nhà cung cấp

Ví dụ mã khóa học sử dụng **Microsoft Agent Framework (MAF)** và nhắm tới **Azure OpenAI Responses API** — API được khuyến nghị trong tương lai, kết hợp các hoàn thành trò chuyện, gọi công cụ, đầu vào đa phương tiện và hội thoại có trạng thái trong một bề mặt API duy nhất. Bạn kết nối qua một dự án **Microsoft Foundry** (với `FoundryChatClient`) hoặc trực tiếp tới Azure OpenAI (với `OpenAIChatClient`).

Khi bạn tiến hành các bài học, bạn có vài lựa chọn nhà cung cấp:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — đường chính được dùng xuyên suốt các bài học. Đăng nhập bằng `az login` để xác thực Entra ID không cần khoá.
- **Foundry Local** — chạy mô hình hoàn toàn trên thiết bị qua OpenAI-compatible API (không dùng đám mây, không cần khoá API). Lý tưởng cho thử nghiệm offline hoặc miễn phí. Xem [Thiết lập khóa học](./00-course-setup/README.md).
- **MiniMax** — nhà cung cấp tương thích OpenAI với mô hình ngữ cảnh lớn, dùng thay thế tiện lợi.

> **Lưu ý:** GitHub Models đã ngừng sử dụng (sẽ ngưng tới tháng 7 năm 2026) và không hỗ trợ Responses API. Các ví dụ đã được cập nhật dùng Azure OpenAI / Microsoft Foundry thay thế.

## Chọn lộ trình học của bạn

Bạn có thể học toàn bộ khóa theo thứ tự, hoặc nhảy tới một lộ trình dựa trên điều bạn muốn
xây dựng.

| Nếu mục tiêu của bạn là... | Bắt đầu với | Rồi học |
|-----------------------|------------|------------|
| Hiểu đại lý là gì | 01, 02, 03 | 04, 05, 06 |
| Xây dựng đại lý sử dụng công cụ | 04 | 05, 07, 14 |
| Xây dựng đại lý dựa trên RAG | 05 | 04, 06, 12 |
| Thiết kế quy trình đa bước | 07 | 08, 09, 14 |
| Hiểu hệ thống đa đại lý | 08 | 07, 09, 11 |
| Chuẩn bị đại lý cho sản xuất | 06, 10 | 12, 13, 16, 18 |
| Triển khai và mở rộng đại lý trên Foundry | 10, 16 | 06, 13, 18 |
| Xây dựng đại lý chạy cục bộ / ưu tiên offline | 17 | 04, 05, 11 |
| Khám phá giao thức và tự động trình duyệt | 11, 15 | 10, 18 |

Mẹo: nếu bạn mới với đại lý, đừng bỏ qua các Bài học 01-06. Chúng cung cấp cho bạn
từ vựng cần thiết cho phần còn lại của khóa học.

## Hướng dẫn từng bài học

| Bài học | Bạn học được gì | Thử làm sau bài học |
|--------|----------------|---------------------------|
| [01 - Giới thiệu về Đại lý AI](./01-intro-to-ai-agents/README.md) | Điều gì làm đại lý khác biệt với chatbot cơ bản. | Giải thích ý tưởng demo của bạn như một đại lý, không chỉ là một ứng dụng chat. |
| [02 - Khung Agentic](./02-explore-agentic-frameworks/README.md) | Khung giúp với mô hình, công cụ, trạng thái, và quy trình làm việc. | Xác định phần nào trong demo của bạn thuộc quản lý của khung. |
| [03 - Mẫu thiết kế Agentic](./03-agentic-design-patterns/README.md) | Các mẫu phổ biến thiết kế hành vi đại lý. | Phác thảo hành trình người dùng trước khi viết mã. |
| [04 - Sử dụng công cụ](./04-tool-use/README.md) | Cách đại lý gọi công cụ để lấy dữ liệu hoặc thực hiện hành động. | Xác định một công cụ mà đại lý demo của bạn cần. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Cách truy xuất làm cơ sở trả lời đại lý bằng tài liệu hoặc dữ liệu. | Quyết định nguồn kiến thức mà demo của bạn nên tìm kiếm. |

| [06 - Đại Lý Đáng Tin Cậy](./06-building-trustworthy-agents/README.md) | Cách thêm các hàng rào bảo vệ, kiểm soát và hành vi an toàn hơn. | Thêm một quy tắc cho khi đại lý nên hỏi người dùng trước. |
| [07 - Thiết Kế Lập Kế Hoạch](./07-planning-design/README.md) | Cách các đại lý chia mục tiêu lớn thành các bước nhỏ hơn. | Viết kế hoạch ba bước cho yêu cầu demo của bạn. |
| [08 - Thiết Kế Đa Đại Lý](./08-multi-agent/README.md) | Khi nào chia công việc cho các đại lý chuyên môn hóa. | Quyết định xem demo của bạn cần một đại lý hay nhiều đại lý. |
| [09 - Siêu Nhận Thức](./09-metacognition/README.md) | Cách các đại lý có thể xem lại và cải thiện đầu ra của chính mình. | Thêm bước tự kiểm tra cuối cùng trước khi đại lý phản hồi. |
| [10 - Đại Lý AI trong Sản Xuất](./10-ai-agents-production/README.md) | Điều gì thay đổi khi một đại lý chuyển từ demo sang sản xuất. | Liệt kê những gì bạn sẽ giám sát: chất lượng, chi phí, độ trễ, lỗi. |
| [11 - Giao Thức Agentic](./11-agentic-protocols/README.md) | Cách các giao thức kết nối đại lý với công cụ và đại lý khác. | Xác định nơi một giao thức chuẩn có thể đơn giản hóa tích hợp. |
| [12 - Kỹ Thuật Ngữ Cảnh](./12-context-engineering/README.md) | Cách chọn, cắt tỉa, cô lập và quản lý ngữ cảnh. | Quyết định điều gì thuộc về prompt và điều gì nên để ngoài. |
| [13 - Bộ Nhớ Đại Lý](./13-agent-memory/README.md) | Cách các đại lý có thể lưu giữ thông tin hữu ích qua các tương tác. | Chọn một sở thích an toàn mà demo của bạn có thể ghi nhớ. |
| [14 - Khung Đại Lý Microsoft](./14-microsoft-agent-framework/README.md) | Các khối xây dựng đặc thù cho đại lý và luồng công việc, cộng với việc lưu trữ đại lý LangChain/LangGraph trên Microsoft Foundry. | Ánh xạ các bước demo của bạn tới các khái niệm trong khung. |
| [15 - Đại Lý Sử Dụng Máy Tính](./15-browser-use/README.md) | Cách các đại lý tương tác với trình duyệt hoặc giao diện người dùng, bao gồm ví dụ thực tế như Microsoft Project Opal. | Chọn một tác vụ trình duyệt mà vẫn nên yêu cầu xác nhận người dùng. |
| [16 - Triển Khai Đại Lý Có Thể Mở Rộng](./16-deploying-scalable-agents/README.md) | Cách đưa đại lý từ nguyên mẫu đến triển khai sản xuất có thể mở rộng, quan sát được trên Microsoft Foundry (đại lý được lưu trữ, định tuyến mô hình, bộ nhớ đệm, cổng đánh giá, kiểm tra khói). | Liệt kê các mối quan tâm sản xuất mà demo của bạn vẫn cần: lưu trữ, định tuyến, chi phí, đánh giá. |
| [17 - Tạo Đại Lý AI Cục Bộ](./17-creating-local-ai-agents/README.md) | Cách xây dựng đại lý ưu tiên cục bộ chạy hoàn toàn trên máy của bạn với Foundry Local và Qwen (công cụ cục bộ, RAG cục bộ, MCP cục bộ). | Quyết định phần nào của demo nên giữ riêng tư và chạy cục bộ. |
| [18 - Bảo Mật Đại Lý AI](./18-securing-ai-agents/README.md) | Cách làm cho hành động của đại lý dễ kiểm toán và có dấu hiệu giả mạo. | Quyết định những hành động nào trong demo của bạn nên được ghi lại hoặc cấp biên nhận. |

## Kiểm Tra Đại Lý Được Triển Khai với Kiểm Tra Khói

Khi bạn triển khai một đại lý (Bài học 16), một **kiểm tra khói** là phép kiểm tra rẻ nhất đầu tiên
để đảm bảo việc triển khai thực sự trả lời. Kho lưu trữ này đi kèm các danh mục sẵn sàng chạy
dưới thư mục [tests/](./tests/README.md) cho các đại lý có thể triển khai ở Bài học
01, 04, 05, và 16, được kết nối với

[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) Hành động GitHub
Chạy chúng từ tab **Actions** sau khi triển khai đại lý của bài học.
Các bài kiểm tra khói là cửa ngõ đầu tiên — đánh giá ngoại tuyến và trực tuyến (Bài học 10 và 16)
cho bạn biết đại lý *tốt* đến mức nào.

## Những Ý Chính Bằng Ngôn Ngữ Dễ Hiểu Cho Người Mới Bắt Đầu

### Công cụ

Công cụ là thứ đại lý có thể gọi để thực hiện công việc bên ngoài mô hình. Một công cụ tốt
có tên rõ ràng, công việc hẹp, đầu vào kiểu rõ ràng, đầu ra có thể dự đoán được, và một cách an toàn
để thất bại.

Đối với bản demo trợ giúp khóa học, một công cụ có thể là:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG và Kiến Thức

RAG giúp đại lý trả lời dựa trên nguồn tài liệu thay vì đoán mò. Trong
khóa học này, nguồn tài liệu đó có thể là các README bài học, ví dụ mã, hoặc các
tài nguyên bên ngoài được liên kết từ các bài học.

Sử dụng RAG khi câu trả lời cần được dựa trên tài liệu, dữ liệu, hoặc các tệp dự án hiện tại.


### Lập kế hoạch

Lập kế hoạch hữu ích khi yêu cầu bao gồm hơn một bước. Giữ các kế hoạch ngắn gọn và
đủ rõ để nhà phát triển hoặc người dùng có thể kiểm tra.

Đối với bản demo, một kế hoạch có thể là:

1. Tìm các bài học liên quan đến việc sử dụng công cụ.
2. Tóm tắt các bài học liên quan nhất.
3. Đề xuất một nhiệm vụ thực hành.

### Ngữ cảnh

Ngữ cảnh là những gì mô hình nhìn thấy ngay lúc này. Quá ít ngữ cảnh có thể làm đại lý
bỏ lỡ những chi tiết quan trọng. Quá nhiều ngữ cảnh có thể làm đại lý chậm hơn, tốn kém hơn,
hoặc dễ bị nhầm lẫn.

Kỹ thuật ngữ cảnh tốt có nghĩa là lựa chọn thông tin đúng cho lần gọi mô hình tiếp theo.


### Bộ nhớ

Bộ nhớ là thông tin được lưu lại để dùng sau. Đừng lưu mọi thứ. Chỉ lưu thông tin
khi nó hữu ích, an toàn, và dễ cập nhật hoặc xóa.

Ví dụ, nhớ rằng "người học thích các ví dụ bằng Python" có thể hữu ích.
Thường thì nhớ dữ liệu cá nhân nhạy cảm thì không.

### Đánh giá và Quan sát

Đánh giá hỏi: đại lý có làm đúng không?

Quan sát hỏi: chúng ta có thể thấy điều đó diễn ra thế nào không?

Đối với các đại lý sản xuất, theo dõi các lần gọi mô hình, gọi công cụ, ngữ cảnh được truy xuất,
độ trễ, chi phí, lỗi, và phản hồi người dùng.

### Tin cậy và Bảo mật

Đại lý đáng tin cậy cần nhiều hơn một lời nhắc hữu ích. Sử dụng công cụ với quyền hạn tối thiểu,
phê duyệt con người cho các hành động tác động lớn, che giấu dữ liệu khi cần, và nhật ký hoặc
biên lai cho các hành động cần được kiểm tra.

## Thói Quen Đánh Giá 15 Phút

Sử dụng thói quen này sau mỗi bài học:

1. **Tóm tắt bài học trong một câu.**
2. **Đặt tên cho khả năng mới của đại lý.** Ví dụ: sử dụng công cụ, truy xuất,
   lập kế hoạch, bộ nhớ, quan sát, hoặc bảo mật.
3. **Thêm nó vào bản demo trợ giúp khóa học.** Bây giờ bản demo thay đổi gì?
4. **Tìm rủi ro.** Điều gì có thể sai nếu khả năng này bị lạm dụng?
5. **Viết một câu hỏi kiểm tra.** Làm thế nào để bạn kiểm tra đại lý hoạt động tốt?

## Tự Kiểm Tra Nhanh

Trước khi tiếp tục, hãy thử trả lời các câu hỏi sau:

1. Đại lý có thể làm gì mà chatbot thông thường không thể tự làm?
2. Công cụ nào đại lý của bạn cần trước tiên, và tại sao?
3. Nguồn kiến thức nào nên làm cơ sở cho câu trả lời của đại lý?
4. Ngữ cảnh nào nên được bao gồm trong lần gọi mô hình tiếp theo?

5. Đại lý nên nhớ những gì, và nên tránh lưu trữ những gì?
6. Khi nào đại lý nên hỏi sự chấp thuận của con người?
7. Những nhật ký, dấu vết, hoặc biên nhận nào sẽ giúp bạn gỡ lỗi hoặc kiểm tra đại lý sau này?


## Bài tập Capstone Đề xuất

Vào cuối khóa học, xây dựng một đại lý nhỏ giúp người học điều hướng
kho lưu trữ này.

Phiên bản tối thiểu:

- Nhận một chủ đề từ người dùng.
- Tìm các bài học có liên quan nhất.
- Tóm tắt những gì cần đọc trước tiên.
- Gợi ý một nhiệm vụ thực hành.
- Hiển thị các tệp bài học hoặc liên kết đã được sử dụng.

Phiên bản nâng cao:

- Ghi nhớ ngôn ngữ lập trình ưu tiên của người học.
- Sử dụng một kế hoạch đơn giản trước khi trả lời.
- Thêm bước tự kiểm tra trước khi phản hồi cuối cùng.
- Ghi lại các lần gọi công cụ và nguồn được truy xuất.
- Hỏi xác nhận trước khi mở trình duyệt hoặc thực hiện tự động hóa giao diện người dùng.

Điều này mang lại cho bạn một cách nhỏ nhưng thực tế để luyện tập công cụ, RAG, lập kế hoạch,
bối cảnh, bộ nhớ, khả năng quan sát và sự tin tưởng trong một dự án.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->