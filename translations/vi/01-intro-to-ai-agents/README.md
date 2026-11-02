[![Giới thiệu về Tác nhân AI](../../../translated_images/vi/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Bấm vào hình trên để xem video bài học này)_

# Giới thiệu về Tác nhân AI và Các trường hợp sử dụng Tác nhân

Chào mừng bạn đến với khóa học **Tác nhân AI cho Người mới bắt đầu**! Khóa học này cung cấp cho bạn kiến thức nền tảng — và mã hoạt động thực tế — để bắt đầu xây dựng Tác nhân AI từ đầu.

Hãy cùng chào hỏi tại <a href="https://discord.gg/kzRShWzttr" target="_blank">Cộng đồng Discord Azure AI</a> — nơi đầy ắp những người học và nhà xây dựng AI sẵn sàng trả lời câu hỏi của bạn.

Trước khi bắt đầu xây dựng, hãy chắc chắn rằng chúng ta thực sự hiểu Tác nhân AI *là gì* và khi nào nên sử dụng.

---

## Giới thiệu

Bài học này bao gồm:

- Tác nhân AI là gì, và các loại khác nhau tồn tại
- Các loại tác vụ phù hợp nhất với Tác nhân AI
- Các khối xây dựng cốt lõi bạn sẽ sử dụng khi thiết kế giải pháp Agentic

## Mục tiêu học tập

Đến cuối bài học này, bạn sẽ có thể:

- Giải thích tác nhân AI là gì và nó khác biệt so với giải pháp AI thông thường như thế nào
- Biết khi nào nên sử dụng Tác nhân AI (và khi nào không nên)
- Phác thảo thiết kế giải pháp Agentic cơ bản cho một vấn đề thực tế

---

## Định nghĩa Tác nhân AI và các loại Tác nhân AI

### Tác nhân AI là gì?

Dưới đây là cách đơn giản để suy nghĩ về nó:

> **Tác nhân AI là hệ thống cho phép Mô hình Ngôn ngữ Lớn (LLMs) thực sự *làm việc* — bằng cách cung cấp cho chúng công cụ và kiến thức để hành động trên thế giới, không chỉ trả lời theo lời gợi ý.**

Hãy phân tích kỹ hơn:

- **Hệ thống** — Một Tác nhân AI không chỉ là một thứ đơn lẻ. Đây là tập hợp của nhiều phần làm việc cùng nhau. Cốt lõi mỗi tác nhân có ba phần:
  - **Môi trường** — Không gian mà tác nhân hoạt động. Ví dụ, tác nhân đặt vé du lịch thì đó chính là nền tảng đặt vé.
  - **Cảm biến** — Cách tác nhân đọc trạng thái hiện tại của môi trường. Tác nhân du lịch có thể kiểm tra tình trạng phòng khách sạn hay giá vé máy bay.
  - **Bộ kích hoạt** — Cách tác nhân thực hiện hành động. Tác nhân du lịch có thể đặt phòng, gửi xác nhận, hoặc hủy đặt chỗ.

![Tác nhân AI là gì?](../../../translated_images/vi/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Mô hình Ngôn ngữ Lớn** — Tác nhân tồn tại trước cả LLM, nhưng chính LLM làm cho tác nhân hiện đại mạnh mẽ. Chúng có thể hiểu ngôn ngữ tự nhiên, suy luận ngữ cảnh, và biến yêu cầu mơ hồ của người dùng thành kế hoạch hành động cụ thể.

- **Thực hiện hành động** — Nếu không có hệ thống tác nhân, LLM chỉ sinh văn bản. Trong hệ thống tác nhân, LLM thực sự *thực thi* các bước — tìm kiếm cơ sở dữ liệu, gọi API, gửi tin nhắn.

- **Truy cập công cụ** — Công cụ mà tác nhân có thể sử dụng phụ thuộc vào (1) môi trường chạy nó và (2) những gì nhà phát triển cung cấp. Tác nhân du lịch có thể tìm chuyến bay nhưng không thể sửa hồ sơ khách hàng — tất cả tùy thuộc vào cách bạn kết nối.

- **Bộ nhớ + Kiến thức** — Tác nhân có thể có bộ nhớ ngắn hạn (cuộc trò chuyện hiện tại) và bộ nhớ dài hạn (cơ sở dữ liệu khách hàng, tương tác trước). Tác nhân du lịch "nhớ" rằng bạn thích chỗ ngồi cạnh cửa sổ.

---

### Các loại Tác nhân AI khác nhau

Không phải tất cả tác nhân được xây dựng giống nhau. Dưới đây là phân loại chính, lấy ví dụ tác nhân đặt vé du lịch làm minh họa:

| **Loại Tác nhân** | **Chức năng** | **Ví dụ tác nhân du lịch** |
|---|---|---|
| **Tác nhân Phản xạ đơn giản** | Tuân theo quy tắc cứng nhắc — không có bộ nhớ, không lập kế hoạch. | Nhận email phàn nàn → chuyển cho bộ phận hỗ trợ khách hàng. Chỉ vậy thôi. |
| **Tác nhân Phản xạ dựa trên mô hình** | Giữ mô hình nội tại của thế giới và cập nhật khi có thay đổi. | Theo dõi giá vé lịch sử và cảnh báo các tuyến đường đột nhiên tăng giá. |
| **Tác nhân dựa trên mục tiêu** | Có mục tiêu cụ thể và tìm cách đạt được từng bước. | Đặt toàn bộ chuyến đi (vé máy bay, xe, khách sạn) từ vị trí hiện tại của bạn đến điểm đến. |
| **Tác nhân dựa trên tiện ích** | Không chỉ tìm *một* giải pháp — mà tìm *giải pháp tốt nhất* bằng cách cân nhắc các yếu tố. | Cân bằng chi phí và tiện lợi để tìm chuyến đi phù hợp nhất với sở thích của bạn. |
| **Tác nhân học máy** | Cải thiện theo thời gian qua phản hồi. | Điều chỉnh đề xuất đặt vé trong tương lai dựa trên khảo sát sau chuyến đi. |
| **Tác nhân phân cấp** | Tác nhân cấp cao phân chia công việc thành các nhiệm vụ nhỏ và giao cho tác nhân cấp dưới. | Yêu cầu "hủy chuyến đi" được chia thành: hủy vé máy bay, hủy khách sạn, hủy thuê xe — mỗi phần do tác nhân phụ xử lý. |
| **Hệ thống nhiều tác nhân (MAS)** | Nhiều tác nhân độc lập làm việc cùng nhau (hoặc cạnh tranh). | Hợp tác: tác nhân riêng xử lý khách sạn, chuyến bay, và giải trí. Cạnh tranh: nhiều tác nhân tìm cách lấp đầy phòng khách sạn với giá tốt nhất. |

---

## Khi nào sử dụng Tác nhân AI

Chỉ vì bạn *có thể* dùng Tác nhân AI không có nghĩa là lúc nào bạn cũng *nên* dùng. Đây là những tình huống mà tác nhân thực sự phát huy hiệu quả:

![Khi nào sử dụng Tác nhân AI?](../../../translated_images/vi/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Vấn đề mở** — Khi các bước giải quyết vấn đề không thể lập trình trước. Bạn cần LLM tự động tìm đường đi.
- **Quy trình nhiều bước** — Nhiệm vụ yêu cầu sử dụng công cụ qua nhiều lần tương tác, không chỉ tra cứu hoặc tạo một lần.
- **Cải thiện theo thời gian** — Khi bạn muốn hệ thống thông minh hơn dựa trên phản hồi người dùng hoặc tín hiệu môi trường.

Chúng ta sẽ tìm hiểu sâu hơn về khi nào (và khi nào *không*) dùng Tác nhân AI trong bài học **Xây dựng Tác nhân AI Đáng tin cậy** sau trong khóa học.

---

## Những điều cơ bản về giải pháp Agentic

### Phát triển Tác nhân

Việc đầu tiên bạn làm khi xây dựng tác nhân là định nghĩa *nó có thể làm gì* — các công cụ, hành động, và hành vi của nó.

Trong khóa học này, chúng ta sử dụng **Dịch vụ Tác nhân Microsoft Foundry** làm nền tảng chính. Nó hỗ trợ:

- Mô hình từ các nhà cung cấp như OpenAI, Mistral, và Meta (Llama)
- Dữ liệu có bản quyền từ các nhà cung cấp như Tripadvisor
- Định nghĩa công cụ chuẩn theo OpenAPI 3.0

### Mẫu Agentic

Bạn giao tiếp với LLM qua lời gợi ý. Với tác nhân, bạn không thể tạo từng lời gợi ý thủ công — tác nhân phải hành động qua nhiều bước. Đó là lý do có **Mẫu Agentic**. Chúng là các chiến lược tái sử dụng để gợi ý và điều phối LLM theo cách mở rộng, đáng tin cậy hơn.

Khóa học này được cấu trúc theo các mẫu agentic phổ biến và hữu ích nhất.

### Khung Agentic

Khung Agentic cung cấp cho nhà phát triển các mẫu, công cụ, và hạ tầng sẵn sàng dùng để xây dựng tác nhân. Chúng làm cho bạn dễ dàng hơn:

- Kết nối công cụ và khả năng
- Quan sát tác nhân làm gì (và gỡ lỗi khi lỗi xảy ra)
- Hợp tác giữa nhiều tác nhân

Trong khóa học này, chúng ta tập trung vào **Khung Agent Microsoft (MAF)** để xây dựng tác nhân sẵn sàng sản xuất.

---

## Ví dụ Mã nguồn

Sẵn sàng xem nó hoạt động? Dưới đây là các ví dụ mã nguồn cho bài học này:

- 🐍 Python: [Khung Tác nhân](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Khung Tác nhân](./code_samples/01-dotnet-agent-framework.md)

---

## Có câu hỏi?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để kết nối với các học viên khác, tham dự giờ hỗ trợ, và được cộng đồng trả lời các câu hỏi về Tác nhân AI.


---

## Kiểm thử nhanh Tác nhân này (Tùy chọn)

Khi bạn học được cách triển khai tác nhân trong [Bài học 16](../16-deploying-scalable-agents/README.md), bạn có thể thêm một kiểm tra sức khỏe nhanh sau triển khai cho `TravelAgent` của bài học này với bộ catalog sẵn [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Xem [`tests/README.md`](../tests/README.md) để biết cách chạy.

---

## Bài học trước

[Thiết lập Khóa học](../00-course-setup/README.md)

## Bài học tiếp theo

[Khám phá Khung Agentic](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->