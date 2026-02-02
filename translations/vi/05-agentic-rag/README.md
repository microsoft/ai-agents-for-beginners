[![Agentic RAG](../../../translated_images/vi/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Nhấp vào hình ảnh trên để xem video của bài học này)_

# Agentic RAG

Bài học này cung cấp một cái nhìn tổng quan toàn diện về Agentic Retrieval-Augmented Generation (Agentic RAG), một mô hình AI mới nổi, nơi các mô hình ngôn ngữ lớn (LLMs) tự động lên kế hoạch cho các bước tiếp theo trong khi lấy thông tin từ các nguồn bên ngoài. Không giống như các mô hình truy xuất-đọc tĩnh, Agentic RAG bao gồm các lần gọi lặp lại đến LLM, xen kẽ với các cuộc gọi công cụ hoặc hàm và các đầu ra có cấu trúc. Hệ thống đánh giá kết quả, tinh chỉnh truy vấn, gọi thêm công cụ nếu cần và tiếp tục chu trình này cho đến khi đạt được giải pháp thỏa đáng.

## Giới thiệu

Bài học này sẽ bao gồm:

- **Hiểu về Agentic RAG:** Tìm hiểu về mô hình mới nổi trong AI, nơi các mô hình ngôn ngữ lớn (LLMs) tự động lên kế hoạch cho các bước tiếp theo trong khi lấy thông tin từ các nguồn dữ liệu bên ngoài.
- **Nắm bắt phong cách Maker-Checker lặp lại:** Hiểu vòng lặp của các lần gọi lặp lại đến LLM, xen kẽ với các cuộc gọi công cụ hoặc hàm và các đầu ra có cấu trúc, được thiết kế để cải thiện độ chính xác và xử lý các truy vấn bị lỗi.
- **Khám phá các ứng dụng thực tiễn:** Xác định các tình huống mà Agentic RAG phát huy hiệu quả, chẳng hạn như môi trường ưu tiên độ chính xác, tương tác cơ sở dữ liệu phức tạp và quy trình làm việc mở rộng.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách/hiểu:

- **Hiểu về Agentic RAG:** Tìm hiểu về mô hình mới nổi trong AI, nơi các mô hình ngôn ngữ lớn (LLMs) tự động lên kế hoạch cho các bước tiếp theo trong khi lấy thông tin từ các nguồn dữ liệu bên ngoài.
- **Phong cách Maker-Checker lặp lại:** Nắm bắt khái niệm về vòng lặp của các lần gọi lặp lại đến LLM, xen kẽ với các cuộc gọi công cụ hoặc hàm và các đầu ra có cấu trúc, được thiết kế để cải thiện độ chính xác và xử lý các truy vấn bị lỗi.
- **Sở hữu quy trình suy luận:** Hiểu khả năng của hệ thống trong việc sở hữu quy trình suy luận của mình, đưa ra quyết định về cách tiếp cận vấn đề mà không dựa vào các lộ trình được xác định trước.
- **Quy trình làm việc:** Hiểu cách một mô hình agentic tự quyết định lấy báo cáo xu hướng thị trường, xác định dữ liệu đối thủ cạnh tranh, liên kết các số liệu bán hàng nội bộ, tổng hợp kết quả và đánh giá chiến lược.
- **Vòng lặp lặp lại, tích hợp công cụ và bộ nhớ:** Tìm hiểu về sự phụ thuộc của hệ thống vào mô hình tương tác lặp lại, duy trì trạng thái và bộ nhớ qua các bước để tránh vòng lặp lặp lại và đưa ra quyết định sáng suốt.
- **Xử lý các chế độ lỗi và tự sửa lỗi:** Khám phá các cơ chế tự sửa lỗi mạnh mẽ của hệ thống, bao gồm lặp lại và truy vấn lại, sử dụng công cụ chẩn đoán và dựa vào sự giám sát của con người.
- **Giới hạn của tính tự chủ:** Hiểu các hạn chế của Agentic RAG, tập trung vào tính tự chủ theo lĩnh vực, sự phụ thuộc vào cơ sở hạ tầng và tôn trọng các rào cản an toàn.
- **Các trường hợp sử dụng thực tiễn và giá trị:** Xác định các tình huống mà Agentic RAG phát huy hiệu quả, chẳng hạn như môi trường ưu tiên độ chính xác, tương tác cơ sở dữ liệu phức tạp và quy trình làm việc mở rộng.
- **Quản trị, minh bạch và sự tin tưởng:** Tìm hiểu về tầm quan trọng của quản trị và minh bạch, bao gồm lý luận có thể giải thích, kiểm soát thiên vị và sự giám sát của con người.

## Agentic RAG là gì?

Agentic Retrieval-Augmented Generation (Agentic RAG) là một mô hình AI mới nổi, nơi các mô hình ngôn ngữ lớn (LLMs) tự động lên kế hoạch cho các bước tiếp theo trong khi lấy thông tin từ các nguồn bên ngoài. Không giống như các mô hình truy xuất-đọc tĩnh, Agentic RAG bao gồm các lần gọi lặp lại đến LLM, xen kẽ với các cuộc gọi công cụ hoặc hàm và các đầu ra có cấu trúc. Hệ thống đánh giá kết quả, tinh chỉnh truy vấn, gọi thêm công cụ nếu cần và tiếp tục chu trình này cho đến khi đạt được giải pháp thỏa đáng. Phong cách lặp lại “maker-checker” này cải thiện độ chính xác, xử lý các truy vấn bị lỗi và đảm bảo kết quả chất lượng cao.

Hệ thống chủ động sở hữu quy trình suy luận của mình, viết lại các truy vấn bị lỗi, chọn các phương pháp truy xuất khác nhau và tích hợp nhiều công cụ—chẳng hạn như tìm kiếm vector trong Azure AI Search, cơ sở dữ liệu SQL hoặc API tùy chỉnh—trước khi hoàn thiện câu trả lời của mình. Điểm khác biệt của một hệ thống agentic là khả năng sở hữu quy trình suy luận của nó. Các triển khai RAG truyền thống dựa vào các lộ trình được xác định trước, nhưng một hệ thống agentic tự động xác định trình tự các bước dựa trên chất lượng thông tin mà nó tìm thấy.

## Định nghĩa Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) là một mô hình mới nổi trong phát triển AI, nơi LLMs không chỉ lấy thông tin từ các nguồn dữ liệu bên ngoài mà còn tự động lên kế hoạch cho các bước tiếp theo. Không giống như các mô hình truy xuất-đọc tĩnh hoặc các chuỗi nhắc được kịch bản hóa cẩn thận, Agentic RAG bao gồm một vòng lặp các lần gọi lặp lại đến LLM, xen kẽ với các cuộc gọi công cụ hoặc hàm và các đầu ra có cấu trúc. Ở mỗi bước, hệ thống đánh giá kết quả mà nó đã thu được, quyết định có nên tinh chỉnh truy vấn, gọi thêm công cụ nếu cần và tiếp tục chu trình này cho đến khi đạt được giải pháp thỏa đáng.

Phong cách lặp lại “maker-checker” này được thiết kế để cải thiện độ chính xác, xử lý các truy vấn bị lỗi đối với cơ sở dữ liệu có cấu trúc (ví dụ: NL2SQL) và đảm bảo kết quả cân bằng, chất lượng cao. Thay vì chỉ dựa vào các chuỗi nhắc được thiết kế cẩn thận, hệ thống chủ động sở hữu quy trình suy luận của mình. Nó có thể viết lại các truy vấn bị lỗi, chọn các phương pháp truy xuất khác nhau và tích hợp nhiều công cụ—chẳng hạn như tìm kiếm vector trong Azure AI Search, cơ sở dữ liệu SQL hoặc API tùy chỉnh—trước khi hoàn thiện câu trả lời của mình. Điều này loại bỏ nhu cầu về các khung điều phối quá phức tạp. Thay vào đó, một vòng lặp tương đối đơn giản của “gọi LLM → sử dụng công cụ → gọi LLM → …” có thể tạo ra các đầu ra tinh vi và có cơ sở.

![Agentic RAG Core Loop](../../../translated_images/vi/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Sở hữu quy trình suy luận

Điểm khác biệt làm cho một hệ thống trở nên “agentic” là khả năng sở hữu quy trình suy luận của nó. Các triển khai RAG truyền thống thường phụ thuộc vào con người để xác định trước một lộ trình cho mô hình: một chuỗi suy nghĩ phác thảo những gì cần truy xuất và khi nào.
Nhưng khi một hệ thống thực sự agentic, nó tự quyết định cách tiếp cận vấn đề. Nó không chỉ thực hiện một kịch bản; nó tự động xác định trình tự các bước dựa trên chất lượng thông tin mà nó tìm thấy.
Ví dụ, nếu được yêu cầu tạo chiến lược ra mắt sản phẩm, nó không chỉ dựa vào một nhắc nhở mô tả toàn bộ quy trình nghiên cứu và ra quyết định. Thay vào đó, mô hình agentic tự quyết định:

1. Lấy báo cáo xu hướng thị trường hiện tại bằng Bing Web Grounding.
2. Xác định dữ liệu đối thủ cạnh tranh liên quan bằng Azure AI Search.
3. Liên kết các số liệu bán hàng nội bộ lịch sử bằng Azure SQL Database.
4. Tổng hợp các kết quả thành một chiến lược mạch lạc được điều phối qua Azure OpenAI Service.
5. Đánh giá chiến lược để tìm các khoảng trống hoặc sự không nhất quán, thúc đẩy một vòng truy xuất khác nếu cần.
Tất cả các bước này—tinh chỉnh truy vấn, chọn nguồn, lặp lại cho đến khi “hài lòng” với câu trả lời—đều do mô hình quyết định, không được kịch bản hóa trước bởi con người.

## Vòng lặp lặp lại, tích hợp công cụ và bộ nhớ

![Tool Integration Architecture](../../../translated_images/vi/tool-integration.0f569710b5c17c10.webp)

Một hệ thống agentic dựa vào mô hình tương tác lặp lại:

- **Lần gọi ban đầu:** Mục tiêu của người dùng (tức là nhắc nhở của người dùng) được trình bày cho LLM.
- **Kích hoạt công cụ:** Nếu mô hình xác định thông tin bị thiếu hoặc hướng dẫn không rõ ràng, nó chọn một công cụ hoặc phương pháp truy xuất—chẳng hạn như truy vấn cơ sở dữ liệu vector (ví dụ: Azure AI Search Hybrid search trên dữ liệu riêng tư) hoặc một cuộc gọi SQL có cấu trúc—để thu thập thêm ngữ cảnh.
- **Đánh giá & Tinh chỉnh:** Sau khi xem xét dữ liệu trả về, mô hình quyết định liệu thông tin có đủ hay không. Nếu không, nó tinh chỉnh truy vấn, thử một công cụ khác hoặc điều chỉnh cách tiếp cận của mình.
- **Lặp lại cho đến khi hài lòng:** Chu trình này tiếp tục cho đến khi mô hình xác định rằng nó có đủ sự rõ ràng và bằng chứng để đưa ra một phản hồi cuối cùng, có lý lẽ tốt.
- **Bộ nhớ & Trạng thái:** Vì hệ thống duy trì trạng thái và bộ nhớ qua các bước, nó có thể nhớ các lần thử trước đó và kết quả của chúng, tránh các vòng lặp lặp lại và đưa ra quyết định sáng suốt hơn khi tiến hành.

Theo thời gian, điều này tạo ra cảm giác hiểu biết đang phát triển, cho phép mô hình điều hướng các nhiệm vụ phức tạp, nhiều bước mà không cần con người can thiệp liên tục hoặc định hình lại nhắc nhở.

## Xử lý các chế độ lỗi và tự sửa lỗi

Tính tự chủ của Agentic RAG cũng bao gồm các cơ chế tự sửa lỗi mạnh mẽ. Khi hệ thống gặp ngõ cụt—chẳng hạn như truy xuất tài liệu không liên quan hoặc gặp phải các truy vấn bị lỗi—nó có thể:

- **Lặp lại và truy vấn lại:** Thay vì trả về các phản hồi có giá trị thấp, mô hình thử các chiến lược tìm kiếm mới, viết lại các truy vấn cơ sở dữ liệu hoặc xem xét các tập dữ liệu thay thế.
- **Sử dụng công cụ chẩn đoán:** Hệ thống có thể kích hoạt các chức năng bổ sung được thiết kế để giúp nó gỡ lỗi các bước suy luận hoặc xác nhận tính chính xác của dữ liệu truy xuất. Các công cụ như Azure AI Tracing sẽ rất quan trọng để cho phép khả năng quan sát và giám sát mạnh mẽ.
- **Dựa vào sự giám sát của con người:** Đối với các tình huống có rủi ro cao hoặc thất bại lặp lại, mô hình có thể đánh dấu sự không chắc chắn và yêu cầu hướng dẫn từ con người. Khi con người cung cấp phản hồi sửa chữa, mô hình có thể kết hợp bài học đó trong tương lai.

Cách tiếp cận lặp lại và năng động này cho phép mô hình cải thiện liên tục, đảm bảo rằng nó không chỉ là một hệ thống một lần mà là một hệ thống học hỏi từ những sai lầm của mình trong một phiên làm việc nhất định.

![Self Correction Mechanism](../../../translated_images/vi/self-correction.da87f3783b7f174b.webp)

## Giới hạn của tính tự chủ

Mặc dù có tính tự chủ trong một nhiệm vụ, Agentic RAG không tương đương với Trí tuệ Nhân tạo Tổng quát. Các khả năng “agentic” của nó bị giới hạn trong các công cụ, nguồn dữ liệu và chính sách do các nhà phát triển con người cung cấp. Nó không thể tự tạo ra công cụ hoặc vượt ra ngoài các ranh giới lĩnh vực đã được thiết lập. Thay vào đó, nó xuất sắc trong việc điều phối động các nguồn lực hiện có.

Các điểm khác biệt chính so với các hình thức AI tiên tiến hơn bao gồm:

1. **Tự chủ theo lĩnh vực:** Các hệ thống Agentic RAG tập trung vào việc đạt được các mục tiêu do người dùng xác định trong một lĩnh vực đã biết, sử dụng các chiến lược như viết lại truy vấn hoặc chọn công cụ để cải thiện kết quả.
2. **Phụ thuộc vào cơ sở hạ tầng:** Các khả năng của hệ thống phụ thuộc vào các công cụ và dữ liệu được tích hợp bởi các nhà phát triển. Nó không thể vượt qua các ranh giới này mà không có sự can thiệp của con người.
3. **Tôn trọng các rào cản an toàn:** Các hướng dẫn đạo đức, quy tắc tuân thủ và chính sách kinh doanh vẫn rất quan trọng. Sự tự do của agent luôn bị giới hạn bởi các biện pháp an toàn và cơ chế giám sát (hy vọng vậy?).

## Các trường hợp sử dụng thực tiễn và giá trị

Agentic RAG phát huy hiệu quả trong các tình huống yêu cầu sự tinh chỉnh lặp lại và độ chính xác:

1. **Môi trường ưu tiên độ chính xác:** Trong kiểm tra tuân thủ, phân tích quy định hoặc nghiên cứu pháp lý, mô hình agentic có thể liên tục xác minh các sự kiện, tham khảo nhiều nguồn và viết lại các truy vấn cho đến khi nó tạo ra một câu trả lời được kiểm chứng kỹ lưỡng.
2. **Tương tác cơ sở dữ liệu phức tạp:** Khi xử lý dữ liệu có cấu trúc, nơi các truy vấn thường thất bại hoặc cần điều chỉnh, hệ thống có thể tự động tinh chỉnh các truy vấn của mình bằng Azure SQL hoặc Microsoft Fabric OneLake, đảm bảo việc truy xuất cuối cùng phù hợp với ý định của người dùng.
3. **Quy trình làm việc mở rộng:** Các phiên làm việc dài hơn có thể phát triển khi thông tin mới xuất hiện. Agentic RAG có thể liên tục kết hợp dữ liệu mới, thay đổi chiến lược khi nó học thêm về không gian vấn đề.

## Quản trị, minh bạch và sự tin tưởng

Khi các hệ thống này trở nên tự chủ hơn trong suy luận của mình, quản trị và minh bạch là rất quan trọng:

- **Lý luận có thể giải thích:** Mô hình có thể cung cấp một bản ghi kiểm toán về các truy vấn mà nó đã thực hiện, các nguồn mà nó đã tham khảo và các bước suy luận mà nó đã thực hiện để đạt được kết luận. Các công cụ như Azure AI Content Safety và Azure AI Tracing / GenAIOps có thể giúp duy trì tính minh bạch và giảm thiểu rủi ro.
- **Kiểm soát thiên vị và truy xuất cân bằng:** Các nhà phát triển có thể điều chỉnh các chiến lược truy xuất để đảm bảo các nguồn dữ liệu cân bằng, đại diện được xem xét, và thường xuyên kiểm tra các đầu ra để phát hiện thiên vị hoặc các mẫu lệch lạc bằng cách sử dụng các mô hình tùy chỉnh cho các tổ chức khoa học dữ liệu tiên tiến sử dụng Azure Machine Learning.
- **Sự giám sát của con người và tuân thủ:** Đối với các nhiệm vụ nhạy cảm, việc xem xét của con người vẫn rất cần thiết. Agentic RAG không thay thế phán đoán của con người trong các quyết định có rủi ro cao—nó bổ sung bằng cách cung cấp các tùy chọn được kiểm chứng kỹ lưỡng hơn.

Có các công cụ cung cấp một bản ghi rõ ràng về các hành động là rất cần thiết. Nếu không có chúng, việc gỡ lỗi một quy trình nhiều bước có thể rất khó khăn. Xem ví dụ sau từ Literal AI (công ty đứng sau Chainlit) về một Agent run:

![AgentRunExample](../../../translated_images/vi/AgentRunExample.471a94bc40cbdc0c.webp)

## Kết luận

Agentic RAG đại diện cho một sự phát triển tự nhiên trong cách các hệ thống AI xử lý các nhiệm vụ phức tạp, đòi hỏi nhiều dữ liệu. Bằng cách áp dụng mô hình tương tác lặp lại, tự động chọn công cụ và tinh chỉnh truy vấn cho đến khi đạt được kết quả chất lượng cao, hệ thống vượt ra ngoài việc chỉ theo dõi nhắc nhở tĩnh để trở thành một người ra quyết định thích ứng, nhận thức ngữ cảnh hơn. Mặc dù vẫn bị giới hạn bởi các cơ sở hạ tầng và hướng dẫn đạo đức do con người xác định, các khả năng agentic này cho phép các tương tác AI phong phú hơn, năng động hơn và cuối cùng hữu ích hơn cho cả doanh nghiệp và người dùng cuối.

### Có thêm câu hỏi về Agentic RAG?

Tham gia [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ các học viên khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về AI Agents của bạn.

## Tài liệu bổ sung

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Triển khai Retrieval Augmented Generation (RAG) với Azure OpenAI Service: Tìm hiểu cách sử dụng dữ liệu của riêng bạn với Azure OpenAI Service. Module Microsoft Learn này cung cấp hướng dẫn toàn diện về việc triển khai RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Đánh giá các ứng dụng AI tạo sinh với Azure AI Foundry: Bài viết này đề cập đến việc đánh giá và so sánh các mô hình
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Hướng dẫn toàn diện về hệ thống truy xuất và tạo nội dung dựa trên tác nhân – Tin tức từ thế hệ RAG</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: tăng tốc RAG của bạn với cải tiến truy vấn và tự truy vấn! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Thêm các lớp tác nhân vào RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Tương lai của các trợ lý tri thức: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Cách xây dựng hệ thống Agentic RAG</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Sử dụng Azure AI Foundry Agent Service để mở rộng quy mô các tác nhân AI của bạn</a>

### Các bài báo học thuật

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Tinh chỉnh lặp lại với phản hồi tự động</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Các tác nhân ngôn ngữ với học tăng cường bằng lời nói</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Các mô hình ngôn ngữ lớn có thể tự sửa lỗi với công cụ phê bình tương tác</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Khảo sát về Agentic RAG</a>

## Bài học trước

[Mẫu thiết kế sử dụng công cụ](../04-tool-use/README.md)

## Bài học tiếp theo

[Xây dựng các tác nhân AI đáng tin cậy](../06-building-trustworthy-agents/README.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.