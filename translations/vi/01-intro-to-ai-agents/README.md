[![Intro to AI Agents](../../../translated_images/vi/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Nhấp vào hình ảnh trên để xem video cho bài học này)_

# Giới thiệu về AI Agents và Các trường hợp sử dụng Agent

Chào mừng bạn đến với khóa học **AI Agents dành cho người mới bắt đầu**! Khóa học này cung cấp cho bạn kiến thức nền tảng — và mã thực thi thực tế — để bắt đầu xây dựng AI Agents từ đầu.

Hãy chào hỏi trong <a href="https://discord.gg/kzRShWzttr" target="_blank">Cộng đồng Azure AI Discord</a> — nơi hội tụ các học viên và người xây dựng AI luôn sẵn sàng trả lời các câu hỏi.

Trước khi bắt tay vào xây dựng, hãy đảm bảo chúng ta thực sự hiểu AI Agent *là gì* và khi nào nên sử dụng nó.

---

## Giới thiệu

Bài học này bao gồm:

- AI Agents là gì, và các loại khác nhau tồn tại
- Những loại nhiệm vụ nào AI Agents thích hợp nhất để giải quyết
- Các thành phần cốt lõi bạn sẽ sử dụng khi thiết kế một giải pháp Agentic

## Mục tiêu học tập

Sau bài học này, bạn sẽ có thể:

- Giải thích AI Agent là gì và điểm khác biệt so với giải pháp AI thông thường
- Biết khi nào nên sử dụng AI Agent (và khi nào không nên)
- Phác thảo thiết kế cơ bản của một giải pháp Agentic cho một vấn đề thực tế

---

## Định nghĩa AI Agents và các loại AI Agents

### AI Agents là gì?

Đây là cách đơn giản để nghĩ về nó:

> **AI Agents là hệ thống cho phép Mô hình Ngôn ngữ Lớn (LLMs) thực sự *làm việc* — bằng cách cung cấp cho chúng công cụ và kiến thức để tác động lên thế giới, không chỉ phản hồi các yêu cầu.**

Hãy phân tích thêm một chút:

- **Hệ thống** — AI Agent không chỉ là một thành phần đơn lẻ. Nó là tập hợp các phần làm việc cùng nhau. Về cơ bản, mỗi agent đều có ba phần:
  - **Môi trường** — Không gian mà agent hoạt động. Với agent đặt vé du lịch, đây chính là nền tảng đặt chỗ.
  - **Cảm biến** — Cách agent đọc trạng thái hiện tại của môi trường. Agent du lịch có thể kiểm tra tình trạng phòng khách sạn hoặc giá vé máy bay.
  - **Bộ chấp hành** — Cách agent thực hiện hành động. Agent du lịch có thể đặt phòng, gửi xác nhận hoặc hủy đặt chỗ.

![What Are AI Agents?](../../../translated_images/vi/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Mô hình ngôn ngữ lớn** — Agents đã tồn tại trước khi có LLMs, nhưng chính LLMs là yếu tố giúp agent hiện đại trở nên mạnh mẽ. Chúng có thể hiểu ngôn ngữ tự nhiên, lý giải về ngữ cảnh và biến yêu cầu mơ hồ của người dùng thành kế hoạch hành động cụ thể.

- **Thực hiện hành động** — Nếu không có hệ thống agent, LLM chỉ tạo ra văn bản. Trong hệ thống agent, LLM có thể *thực thi* các bước — tìm kiếm cơ sở dữ liệu, gọi API, gửi tin nhắn.

- **Truy cập công cụ** — Công cụ mà agent có thể sử dụng phụ thuộc vào (1) môi trường nó hoạt động và (2) nhà phát triển cho phép. Agent du lịch có thể tìm kiếm chuyến bay nhưng không chỉnh sửa hồ sơ khách hàng — tất cả tuỳ thuộc vào những gì bạn cấu hình.

- **Bộ nhớ + Kiến thức** — Agents có thể có bộ nhớ ngắn hạn (cuộc hội thoại hiện tại) và bộ nhớ dài hạn (cơ sở dữ liệu khách hàng, các tương tác trước đó). Agent du lịch có thể "nhớ" rằng bạn thích chỗ ngồi gần cửa sổ.

---

### Các loại AI Agents khác nhau

Không phải tất cả các agent đều được xây dựng giống nhau. Dưới đây là phân loại chính, lấy agent đặt vé du lịch làm ví dụ:

| **Loại Agent** | **Chức năng** | **Ví dụ Agent Du lịch** |
|---|---|---|
| **Simple Reflex Agents** | Tuân thủ các quy tắc cứng nhắc — không có bộ nhớ, không lên kế hoạch. | Thấy email khiếu nại → chuyển tiếp cho bộ phận chăm sóc khách hàng. Chỉ vậy thôi. |
| **Model-Based Reflex Agents** | Giữ mô hình nội bộ về thế giới và cập nhật khi có thay đổi. | Theo dõi giá vé máy bay lịch sử và đánh dấu các chuyến bay tăng giá đột ngột. |
| **Goal-Based Agents** | Có mục tiêu rõ ràng và tìm cách đạt được mục tiêu từng bước một. | Đặt một chuyến đi đầy đủ (chuyến bay, xe, khách sạn) từ vị trí hiện tại đến điểm đến. |
| **Utility-Based Agents** | Không chỉ tìm *một* giải pháp — tìm giải pháp *tốt nhất* bằng cách cân nhắc các lựa chọn. | Cân bằng chi phí và tiện lợi để tìm chuyến đi phù hợp nhất với sở thích của bạn. |
| **Learning Agents** | Cải thiện theo thời gian dựa trên phản hồi. | Điều chỉnh gợi ý đặt phòng tương lai dựa trên khảo sát sau chuyến đi. |
| **Hierarchical Agents** | Agent cấp cao phân công công việc thành các nhiệm vụ nhỏ và giao cho agent cấp thấp hơn. | Yêu cầu "hủy chuyến đi" chia thành: hủy vé máy bay, hủy khách sạn, hủy thuê xe — mỗi phần do một sub-agent xử lý. |
| **Multi-Agent Systems (MAS)** | Nhiều agent độc lập hợp tác (hoặc cạnh tranh). | Hợp tác: các agent riêng biệt xử lý khách sạn, chuyến bay, và giải trí. Cạnh tranh: nhiều agent cạnh tranh để bán phòng khách sạn với giá tốt nhất. |

---

## Khi nào nên dùng AI Agents

Không phải vì bạn *có thể* dùng AI Agent là bạn lúc nào cũng *nên*. Dưới đây là những tình huống agent thực sự phát huy hiệu quả:

![When to use AI Agents?](../../../translated_images/vi/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Vấn đề mở** — Khi các bước giải quyết không thể lập trình sẵn. Bạn cần LLM tự động xác định con đường.
- **Quy trình nhiều bước** — Nhiệm vụ yêu cầu sử dụng công cụ nhiều lượt, không chỉ tra cứu hoặc tạo dữ liệu một lần.
- **Cải thiện theo thời gian** — Khi bạn muốn hệ thống trở nên thông minh hơn dựa trên phản hồi của người dùng hoặc tín hiệu môi trường.

Chúng ta sẽ đi sâu hơn về khi nào (và khi nào *không*) nên dùng AI Agents trong bài học **Xây dựng AI Agents đáng tin cậy** sau trong khóa học.

---

## Những điều cơ bản của giải pháp Agentic

### Phát triển Agent

Điều đầu tiên bạn làm khi xây dựng agent là xác định *nó có thể làm gì* — các công cụ, hành động và hành vi.

Trong khóa học này, chúng ta dùng **Azure AI Agent Service** làm nền tảng chính. Nó hỗ trợ:

- Các mô hình mở như OpenAI, Mistral, và Llama
- Dữ liệu có bản quyền từ các nhà cung cấp như Tripadvisor
- Định nghĩa công cụ chuẩn OpenAPI 3.0

### Mẫu Agentic

Bạn giao tiếp với LLM thông qua các prompt. Với agent, bạn không thể tự tay tạo từng prompt cho mọi bước — agent cần hành động qua nhiều bước. Đó là lý do có **Mẫu Agentic**. Đây là các chiến lược tái sử dụng để prompt và điều phối LLM theo cách mở rộng và đáng tin cậy hơn.

Khóa học này được xây dựng dựa trên các mẫu agentic phổ biến và hữu ích nhất.

### Framework Agentic

Framework Agentic cung cấp cho nhà phát triển các mẫu sẵn, công cụ và cơ sở hạ tầng để xây dựng agent. Chúng giúp:

- Kết nối công cụ và khả năng
- Giám sát hoạt động agent (và gỡ lỗi khi có sự cố)
- Hợp tác giữa nhiều agent

Trong khóa học này, chúng ta tập trung vào **Microsoft Agent Framework (MAF)** để xây dựng các agent sẵn sàng dùng trong sản xuất.

---

## Mẫu mã

Sẵn sàng xem nó hoạt động chưa? Dưới đây là các mẫu mã cho bài học này:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Có câu hỏi?

Tham gia [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) để kết nối với các học viên khác, tham dự giờ làm việc và nhận được câu trả lời cho các câu hỏi về AI Agent từ cộng đồng.

---

## Bài học trước

[Course Setup](../00-course-setup/README.md)

## Bài học tiếp theo

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn chính xác và có thẩm quyền. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm cho bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->