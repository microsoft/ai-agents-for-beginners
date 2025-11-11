<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cdd28bc00816d2773bb2b5968d782abc",
  "translation_date": "2025-11-11T11:27:19+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "vi"
}
-->
[![Giới thiệu về AI Agents](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.vi.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Nhấn vào hình ảnh trên để xem video của bài học này)_

# Giới thiệu về AI Agents và Các Trường Hợp Sử Dụng

Chào mừng bạn đến với khóa học "AI Agents cho Người Mới Bắt Đầu"! Khóa học này cung cấp kiến thức cơ bản và các ví dụ ứng dụng để xây dựng AI Agents.

Tham gia <a href="https://discord.gg/kzRShWzttr" target="_blank">Cộng đồng Azure AI Discord</a> để gặp gỡ các học viên khác và những người xây dựng AI Agents, cũng như đặt câu hỏi về khóa học này.

Để bắt đầu khóa học, chúng ta sẽ tìm hiểu rõ hơn về AI Agents là gì và cách chúng ta có thể sử dụng chúng trong các ứng dụng và quy trình làm việc mà chúng ta xây dựng.

## Giới thiệu

Bài học này bao gồm:

- AI Agents là gì và các loại agents khác nhau?
- Những trường hợp sử dụng nào phù hợp nhất với AI Agents và chúng có thể giúp chúng ta như thế nào?
- Một số khối xây dựng cơ bản khi thiết kế các giải pháp dựa trên Agent là gì?

## Mục tiêu học tập
Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Hiểu các khái niệm về AI Agents và cách chúng khác biệt so với các giải pháp AI khác.
- Áp dụng AI Agents một cách hiệu quả nhất.
- Thiết kế các giải pháp dựa trên Agent một cách hiệu quả cho cả người dùng và khách hàng.

## Định nghĩa AI Agents và Các Loại AI Agents

### AI Agents là gì?

AI Agents là **hệ thống** cho phép **Large Language Models (LLMs)** **thực hiện hành động** bằng cách mở rộng khả năng của chúng thông qua việc cung cấp cho LLMs **truy cập vào công cụ** và **kiến thức**.

Hãy phân tích định nghĩa này thành các phần nhỏ hơn:

- **Hệ thống** - Điều quan trọng là phải nghĩ về agents không chỉ là một thành phần đơn lẻ mà là một hệ thống gồm nhiều thành phần. Ở mức cơ bản, các thành phần của một AI Agent bao gồm:
  - **Môi trường** - Không gian được xác định nơi AI Agent hoạt động. Ví dụ, nếu chúng ta có một AI Agent đặt vé du lịch, môi trường có thể là hệ thống đặt vé du lịch mà AI Agent sử dụng để hoàn thành nhiệm vụ.
  - **Cảm biến** - Môi trường có thông tin và cung cấp phản hồi. AI Agents sử dụng cảm biến để thu thập và diễn giải thông tin về trạng thái hiện tại của môi trường. Trong ví dụ về Agent đặt vé du lịch, hệ thống đặt vé du lịch có thể cung cấp thông tin như tình trạng phòng khách sạn hoặc giá vé máy bay.
  - **Bộ truyền động** - Sau khi AI Agent nhận được trạng thái hiện tại của môi trường, đối với nhiệm vụ hiện tại, agent xác định hành động nào cần thực hiện để thay đổi môi trường. Đối với agent đặt vé du lịch, hành động có thể là đặt một phòng trống cho người dùng.

![AI Agents là gì?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.vi.png)

**Large Language Models** - Khái niệm về agents đã tồn tại trước khi LLMs được tạo ra. Lợi thế của việc xây dựng AI Agents với LLMs là khả năng diễn giải ngôn ngữ và dữ liệu của con người. Khả năng này cho phép LLMs diễn giải thông tin môi trường và xác định kế hoạch để thay đổi môi trường.

**Thực hiện hành động** - Bên ngoài hệ thống AI Agent, LLMs bị giới hạn trong các tình huống mà hành động là tạo nội dung hoặc thông tin dựa trên yêu cầu của người dùng. Bên trong hệ thống AI Agent, LLMs có thể hoàn thành nhiệm vụ bằng cách diễn giải yêu cầu của người dùng và sử dụng các công cụ có sẵn trong môi trường của chúng.

**Truy cập vào công cụ** - Các công cụ mà LLM có thể truy cập được xác định bởi 1) môi trường mà nó hoạt động và 2) nhà phát triển của AI Agent. Trong ví dụ về agent du lịch, các công cụ của agent bị giới hạn bởi các hoạt động có sẵn trong hệ thống đặt vé, và/hoặc nhà phát triển có thể giới hạn quyền truy cập của agent vào các công cụ như đặt vé máy bay.

**Bộ nhớ + Kiến thức** - Bộ nhớ có thể là ngắn hạn trong ngữ cảnh của cuộc trò chuyện giữa người dùng và agent. Về lâu dài, ngoài thông tin được cung cấp bởi môi trường, AI Agents cũng có thể truy xuất kiến thức từ các hệ thống, dịch vụ, công cụ khác, và thậm chí từ các agents khác. Trong ví dụ về agent du lịch, kiến thức này có thể là thông tin về sở thích du lịch của người dùng được lưu trong cơ sở dữ liệu khách hàng.

### Các loại agents khác nhau

Bây giờ chúng ta đã có một định nghĩa chung về AI Agents, hãy xem xét một số loại agents cụ thể và cách chúng được áp dụng cho một agent đặt vé du lịch.

| **Loại Agent**                | **Mô tả**                                                                                                                       | **Ví dụ**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Simple Reflex Agents**      | Thực hiện hành động ngay lập tức dựa trên các quy tắc được định trước.                                                                                  | Agent du lịch diễn giải ngữ cảnh của email và chuyển các khiếu nại du lịch đến bộ phận chăm sóc khách hàng.                                                                                                                          |
| **Model-Based Reflex Agents** | Thực hiện hành động dựa trên một mô hình của thế giới và các thay đổi đối với mô hình đó.                                                              | Agent du lịch ưu tiên các tuyến đường có sự thay đổi giá đáng kể dựa trên quyền truy cập vào dữ liệu giá lịch sử.                                                                                                             |
| **Goal-Based Agents**         | Tạo kế hoạch để đạt được các mục tiêu cụ thể bằng cách diễn giải mục tiêu và xác định các hành động để đạt được nó.                                  | Agent du lịch đặt một hành trình bằng cách xác định các sắp xếp du lịch cần thiết (xe hơi, phương tiện công cộng, vé máy bay) từ vị trí hiện tại đến điểm đến.                                                                                |
| **Utility-Based Agents**      | Xem xét sở thích và cân nhắc các đánh đổi bằng cách định lượng để xác định cách đạt được mục tiêu.                                               | Agent du lịch tối đa hóa tiện ích bằng cách cân nhắc sự tiện lợi so với chi phí khi đặt vé du lịch.                                                                                                                                          |
| **Learning Agents**           | Cải thiện theo thời gian bằng cách phản hồi lại phản hồi và điều chỉnh hành động tương ứng.                                                        | Agent du lịch cải thiện bằng cách sử dụng phản hồi của khách hàng từ các khảo sát sau chuyến đi để thực hiện các điều chỉnh cho các lần đặt vé trong tương lai.                                                                                                               |
| **Hierarchical Agents**       | Có nhiều agents trong một hệ thống phân cấp, với các agents cấp cao hơn chia nhỏ nhiệm vụ thành các nhiệm vụ con để các agents cấp thấp hơn hoàn thành. | Agent du lịch hủy một chuyến đi bằng cách chia nhiệm vụ thành các nhiệm vụ con (ví dụ: hủy các đặt vé cụ thể) và để các agents cấp thấp hơn hoàn thành chúng, báo cáo lại cho agent cấp cao hơn.                                     |
| **Multi-Agent Systems (MAS)** | Các agents hoàn thành nhiệm vụ một cách độc lập, có thể hợp tác hoặc cạnh tranh.                                                           | Hợp tác: Nhiều agents đặt các dịch vụ du lịch cụ thể như khách sạn, vé máy bay, và giải trí. Cạnh tranh: Nhiều agents quản lý và cạnh tranh trên một lịch đặt phòng khách sạn chung để đặt khách hàng vào khách sạn. |

## Khi nào nên sử dụng AI Agents

Trong phần trước, chúng ta đã sử dụng trường hợp đặt vé du lịch để giải thích cách các loại agents khác nhau có thể được sử dụng trong các tình huống khác nhau của việc đặt vé du lịch. Chúng ta sẽ tiếp tục sử dụng ứng dụng này trong suốt khóa học.

Hãy xem xét các loại trường hợp sử dụng mà AI Agents phù hợp nhất:

![Khi nào nên sử dụng AI Agents?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.vi.png)

- **Vấn đề mở** - cho phép LLM xác định các bước cần thiết để hoàn thành một nhiệm vụ vì không phải lúc nào cũng có thể mã hóa cứng vào quy trình làm việc.
- **Quy trình nhiều bước** - các nhiệm vụ yêu cầu một mức độ phức tạp mà AI Agent cần sử dụng công cụ hoặc thông tin qua nhiều lượt thay vì chỉ truy xuất một lần.  
- **Cải thiện theo thời gian** - các nhiệm vụ mà agent có thể cải thiện theo thời gian bằng cách nhận phản hồi từ môi trường hoặc người dùng để cung cấp tiện ích tốt hơn.

Chúng ta sẽ tìm hiểu thêm về các cân nhắc khi sử dụng AI Agents trong bài học Xây dựng AI Agents Đáng Tin Cậy.

## Cơ bản về Giải pháp Dựa trên Agent

### Phát triển Agent

Bước đầu tiên trong việc thiết kế một hệ thống AI Agent là xác định các công cụ, hành động, và hành vi. Trong khóa học này, chúng ta tập trung vào việc sử dụng **Azure AI Agent Service** để định nghĩa các Agents của mình. Dịch vụ này cung cấp các tính năng như:

- Lựa chọn các Mô hình Mở như OpenAI, Mistral, và Llama
- Sử dụng Dữ liệu Được Cấp Phép thông qua các nhà cung cấp như Tripadvisor
- Sử dụng các công cụ OpenAPI 3.0 tiêu chuẩn

### Mẫu Dựa trên Agent

Giao tiếp với LLMs thông qua các lời nhắc. Với tính chất bán tự động của AI Agents, không phải lúc nào cũng có thể hoặc cần thiết để nhắc lại LLM sau một thay đổi trong môi trường. Chúng ta sử dụng **Mẫu Dựa trên Agent** cho phép chúng ta nhắc LLM qua nhiều bước một cách mở rộng hơn.

Khóa học này được chia thành một số mẫu dựa trên Agent phổ biến hiện nay.

### Khung Dựa trên Agent

Khung Dựa trên Agent cho phép các nhà phát triển triển khai các mẫu dựa trên Agent thông qua mã. Các khung này cung cấp các mẫu, plugin, và công cụ để cải thiện sự hợp tác của AI Agents. Những lợi ích này cung cấp khả năng quan sát và khắc phục sự cố tốt hơn cho các hệ thống AI Agent.

Trong khóa học này, chúng ta sẽ khám phá khung AutoGen dựa trên nghiên cứu và khung Agent sẵn sàng sản xuất từ Semantic Kernel.

## Mã Mẫu

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Có thêm câu hỏi về AI Agents?

Tham gia [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ các học viên khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về AI Agents của bạn.

## Bài học trước

[Thiết lập khóa học](../00-course-setup/README.md)

## Bài học tiếp theo

[Khám phá các Khung Dựa trên Agent](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->