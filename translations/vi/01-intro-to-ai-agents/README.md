[![Giới thiệu về Tác nhân AI](../../../translated_images/vi/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Nhấp vào hình ảnh phía trên để xem video của bài học này)_


# Giới thiệu về Tác nhân AI và Các Trường hợp Sử dụng Tác nhân

Chào mừng đến với khóa học "AI Agents for Beginners"! Khóa học này cung cấp kiến thức cơ bản và các ví dụ ứng dụng để xây dựng Tác nhân AI.

Tham gia <a href="https://discord.gg/kzRShWzttr" target="_blank">Cộng đồng Azure AI trên Discord</a> để gặp gỡ những người học khác và những người xây dựng Tác nhân AI, và đặt bất kỳ câu hỏi nào bạn có về khóa học này.

Để bắt đầu khóa học này, chúng ta sẽ bắt đầu bằng cách hiểu rõ hơn Tác nhân AI là gì và cách chúng ta có thể sử dụng chúng trong các ứng dụng và quy trình làm việc mà chúng ta xây dựng.

## Giới thiệu

Bài học này bao gồm:

- Tác nhân AI là gì và có những loại tác nhân nào?
- Những trường hợp sử dụng nào phù hợp nhất cho Tác nhân AI và chúng có thể giúp gì cho chúng ta?
- Một số khối xây dựng cơ bản khi thiết kế các Giải pháp Tác nhân là gì?

## Mục tiêu học tập
Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Hiểu các khái niệm về Tác nhân AI và cách chúng khác với các giải pháp AI khác.
- Áp dụng Tác nhân AI một cách hiệu quả nhất.
- Thiết kế các giải pháp tác nhân một cách hữu ích cho cả người dùng và khách hàng.

## Định nghĩa Tác nhân AI và Các loại Tác nhân AI

### Tác nhân AI là gì?

Tác nhân AI là **hệ thống** cho phép **Large Language Models(LLMs)** **thực hiện hành động** bằng cách mở rộng khả năng của chúng thông qua việc cung cấp cho LLMs **quyền truy cập vào công cụ** và **kiến thức**.

Hãy chia định nghĩa này thành các phần nhỏ hơn:

- **System** - Điều quan trọng là nên nghĩ về tác nhân không chỉ là một thành phần đơn lẻ mà là một hệ thống gồm nhiều thành phần. Ở mức cơ bản, các thành phần của một Tác nhân AI là:
  - **Environment** - Không gian được xác định nơi tác nhân AI hoạt động. Ví dụ, nếu chúng ta có một tác nhân đặt vé du lịch, môi trường có thể là hệ thống đặt chỗ mà tác nhân AI sử dụng để hoàn thành nhiệm vụ.
  - **Sensors** - Môi trường có thông tin và cung cấp phản hồi. Tác nhân AI sử dụng cảm biến để thu thập và diễn giải thông tin này về trạng thái hiện tại của môi trường. Trong ví dụ Tác nhân Đặt Vé Du Lịch, hệ thống đặt chỗ có thể cung cấp thông tin như tình trạng phòng khách sạn hoặc giá vé máy bay.
  - **Actuators** - Khi Tác nhân AI nhận được trạng thái hiện tại của môi trường, đối với nhiệm vụ hiện tại tác nhân xác định hành động nào cần thực hiện để thay đổi môi trường. Đối với tác nhân đặt chỗ du lịch, hành động đó có thể là đặt một phòng có sẵn cho người dùng.

![Tác nhân AI là gì?](../../../translated_images/vi/what-are-ai-agents.1ec8c4d548af601a.webp)

**Large Language Models** - Khái niệm về tác nhân tồn tại trước khi có các LLMs. Lợi thế của việc xây dựng Tác nhân AI với LLMs là khả năng diễn giải ngôn ngữ con người và dữ liệu. Khả năng này cho phép LLMs diễn giải thông tin môi trường và xác định một kế hoạch để thay đổi môi trường.

**Perform Actions** - Bên ngoài hệ thống Tác nhân AI, LLMs bị giới hạn ở các tình huống mà hành động là tạo nội dung hoặc thông tin dựa trên lời nhắc của người dùng. Bên trong hệ thống Tác nhân AI, LLMs có thể hoàn thành nhiệm vụ bằng cách diễn giải yêu cầu của người dùng và sử dụng các công cụ có sẵn trong môi trường của chúng.

**Access To Tools** - Những công cụ mà LLM có thể truy cập được xác định bởi 1) môi trường mà nó đang hoạt động và 2) nhà phát triển của Tác nhân AI. Ví dụ tác nhân du lịch của chúng ta, các công cụ của tác nhân bị giới hạn bởi các thao tác có sẵn trong hệ thống đặt chỗ, và/hoặc nhà phát triển có thể giới hạn quyền truy cập công cụ của tác nhân đối với vé máy bay.

**Memory+Knowledge** - Bộ nhớ có thể là ngắn hạn trong ngữ cảnh cuộc hội thoại giữa người dùng và tác nhân. Về lâu dài, ngoài thông tin do môi trường cung cấp, Tác nhân AI cũng có thể truy xuất kiến thức từ các hệ thống, dịch vụ, công cụ khác, thậm chí từ các tác nhân khác. Trong ví dụ tác nhân du lịch, kiến thức này có thể là thông tin về sở thích du lịch của người dùng được lưu trong cơ sở dữ liệu khách hàng.

### Các loại tác nhân khác nhau

Bây giờ chúng ta đã có định nghĩa chung về Tác nhân AI, hãy xem một số loại tác nhân cụ thể và cách chúng sẽ được áp dụng cho một tác nhân đặt chuyến du lịch.

| **Loại Tác nhân**            | **Mô tả**                                                                                                                            | **Ví dụ**                                                                                                                                                                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tác nhân phản xạ đơn giản** | Thực hiện các hành động ngay lập tức dựa trên các quy tắc đã định trước.                                                            | Tác nhân du lịch diễn giải ngữ cảnh của email và chuyển tiếp các khiếu nại về du lịch tới bộ phận chăm sóc khách hàng.                                                                                                       |
| **Tác nhân phản xạ dựa trên mô hình** | Thực hiện hành động dựa trên một mô hình về thế giới và các thay đổi đối với mô hình đó.                                              | Tác nhân du lịch ưu tiên các tuyến có thay đổi giá đáng kể dựa trên quyền truy cập dữ liệu giá lịch sử.                                                                                                                     |
| **Tác nhân dựa trên mục tiêu** | Tạo kế hoạch để đạt được các mục tiêu cụ thể bằng cách diễn giải mục tiêu và xác định các hành động để đạt được nó.                  | Tác nhân du lịch đặt một chuyến đi bằng cách xác định các sắp xếp cần thiết (xe, phương tiện công cộng, chuyến bay) từ vị trí hiện tại đến điểm đến.                                                                                    |
| **Tác nhân dựa trên tiện ích** | Xem xét sở thích và cân nhắc các đánh đổi một cách số học để xác định cách đạt được mục tiêu.                                         | Tác nhân du lịch tối đa hóa tiện ích bằng cách cân nhắc sự tiện lợi so với chi phí khi đặt chuyến đi.                                                                                                                       |
| **Tác nhân học hỏi**          | Cải thiện theo thời gian bằng cách phản hồi và điều chỉnh hành động cho phù hợp.                                                     | Tác nhân du lịch cải thiện bằng cách sử dụng phản hồi khách hàng từ khảo sát sau chuyến đi để điều chỉnh các đặt chỗ trong tương lai.                                                                                       |
| **Tác nhân phân cấp**         | Có nhiều tác nhân trong một hệ thống phân tầng, với các tác nhân cấp cao hơn chia nhiệm vụ thành các nhiệm vụ con để các tác nhân cấp thấp hoàn thành. | Tác nhân du lịch hủy một chuyến đi bằng cách chia nhiệm vụ thành các nhiệm vụ con (ví dụ, hủy các đặt chỗ cụ thể) và để các tác nhân cấp thấp hoàn thành chúng, báo cáo lại cho tác nhân cấp cao hơn.                        |
| **Hệ thống nhiều tác nhân (MAS)** | Các tác nhân hoàn thành nhiệm vụ độc lập, có thể hợp tác hoặc cạnh tranh.                                                              | Hợp tác: Nhiều tác nhân đặt các dịch vụ du lịch cụ thể như khách sạn, chuyến bay và giải trí. Cạnh tranh: Nhiều tác nhân quản lý và cạnh tranh trên một lịch đặt phòng khách sạn dùng chung để đặt khách vào khách sạn. |

## Khi nào sử dụng Tác nhân AI

Trong phần trước, chúng ta đã sử dụng trường hợp sử dụng Tác nhân Du lịch để giải thích cách các loại tác nhân khác nhau có thể được sử dụng trong các kịch bản đặt chuyến khác nhau. Chúng ta sẽ tiếp tục sử dụng ứng dụng này trong suốt khóa học.

Hãy xem các loại trường hợp sử dụng mà Tác nhân AI phù hợp nhất:

![Khi nào sử dụng Tác nhân AI?](../../../translated_images/vi/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Vấn đề mở** - cho phép LLM xác định các bước cần thiết để hoàn thành một nhiệm vụ vì nó không thể luôn được mã hóa cứng vào một quy trình làm việc.
- **Quy trình nhiều bước** - các nhiệm vụ yêu cầu mức độ phức tạp trong đó Tác nhân AI cần sử dụng công cụ hoặc thông tin qua nhiều lượt thay vì lấy thông tin một lần.  
- **Cải thiện theo thời gian** - các nhiệm vụ mà tác nhân có thể cải thiện theo thời gian bằng cách nhận phản hồi từ môi trường hoặc người dùng để cung cấp tiện ích tốt hơn.

Chúng tôi trình bày thêm các cân nhắc khi sử dụng Tác nhân AI trong bài học Xây dựng Tác nhân AI Đáng tin cậy.

## Những điều cơ bản về Giải pháp Tác nhân

### Phát triển Tác nhân

Bước đầu tiên trong việc thiết kế một hệ thống Tác nhân AI là xác định công cụ, hành động và hành vi. Trong khóa học này, chúng tôi tập trung vào việc sử dụng **Azure AI Agent Service** để định nghĩa các Tác nhân của chúng tôi. Nó cung cấp các tính năng như:

- Lựa chọn các Mô hình Mở như OpenAI, Mistral và Llama
- Sử dụng Dữ liệu được cấp phép thông qua các nhà cung cấp như Tripadvisor
- Sử dụng các công cụ OpenAPI 3.0 tiêu chuẩn

### Mẫu tác nhân

Giao tiếp với LLM thông qua các prompt. Do tính chất bán tự chủ của Tác nhân AI, không phải lúc nào cũng có thể hoặc cần thiết để yêu cầu LLM bằng tay sau khi có thay đổi trong môi trường. Chúng tôi sử dụng các **Mẫu tác nhân** cho phép chúng ta prompt LLM qua nhiều bước theo cách có thể mở rộng hơn.

Khóa học này được chia thành một số mẫu tác nhân phổ biến hiện nay.

### Khung tác nhân

Khung tác nhân cho phép các nhà phát triển triển khai các mẫu tác nhân thông qua mã. Các khung này cung cấp các mẫu, plugin và công cụ để hợp tác Tác nhân AI tốt hơn. Những lợi ích này cung cấp khả năng quan sát và khắc phục sự cố tốt hơn cho hệ thống Tác nhân AI.

Trong khóa học này, chúng ta sẽ khám phá Microsoft Agent Framework (MAF) để xây dựng các tác nhân AI sẵn sàng cho môi trường sản xuất.

## Mã mẫu

- Python: [Khung tác nhân](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Khung tác nhân](./code_samples/01-dotnet-agent-framework.md)

## Bạn còn câu hỏi nào về Tác nhân AI không?

Tham gia [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ những người học khác, tham dự giờ hỗ trợ và có các câu hỏi về Tác nhân AI của bạn được giải đáp.

## Previous Lesson

[Thiết lập Khóa học](../00-course-setup/README.md)

## Next Lesson

[Khám phá Khung tác nhân](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Miễn trừ trách nhiệm:
Tài liệu này đã được dịch bằng dịch vụ dịch máy AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi nỗ lực để đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu nhầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->