[![Agentic RAG](../../../translated_images/vi/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Nhấn vào hình trên để xem video bài học này)_

# Agentic RAG

Bài học này cung cấp tổng quan toàn diện về Agentic Retrieval-Augmented Generation (Agentic RAG), một mô hình AI mới nổi nơi các mô hình ngôn ngữ lớn (LLM) tự động lập kế hoạch các bước tiếp theo trong khi tra cứu thông tin từ các nguồn bên ngoài. Khác với mẫu tra cứu-tự đọc tĩnh, Agentic RAG bao gồm các lệnh gọi lặp đi lặp lại tới LLM, xen kẽ với các lệnh gọi công cụ hoặc chức năng và các đầu ra có cấu trúc. Hệ thống đánh giá kết quả, tinh chỉnh truy vấn, gọi thêm công cụ nếu cần và tiếp tục chu trình này cho đến khi đạt được giải pháp thỏa mãn.

## Giới thiệu

Bài học này sẽ bao gồm

- **Hiểu về Agentic RAG:** Tìm hiểu về mô hình mới nổi trong AI nơi các mô hình ngôn ngữ lớn (LLM) tự động lập kế hoạch các bước tiếp theo trong khi tra cứu thông tin từ các nguồn dữ liệu bên ngoài.
- **Nắm bắt phong cách Maker-Checker lặp đi lặp lại:** Hiểu vòng lặp các lệnh gọi lặp lại đến LLM, xen kẽ với lệnh gọi công cụ hoặc chức năng và các đầu ra có cấu trúc, thiết kế để cải thiện độ chính xác và xử lý các truy vấn bị lỗi.
- **Khám phá ứng dụng thực tiễn:** Xác định các tình huống mà Agentic RAG tỏa sáng, như môi trường ưu tiên độ chính xác, tương tác cơ sở dữ liệu phức tạp và quy trình làm việc mở rộng.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách/hiểu:

- **Hiểu về Agentic RAG:** Tìm hiểu về mô hình mới nổi trong AI nơi các mô hình ngôn ngữ lớn (LLM) tự động lập kế hoạch các bước tiếp theo trong khi tra cứu thông tin từ các nguồn dữ liệu bên ngoài.
- **Phong cách Maker-Checker lặp đi lặp lại:** Nắm bắt khái niệm vòng lặp các lệnh gọi lặp lại tới LLM, xen kẽ với lệnh gọi công cụ hoặc chức năng và các đầu ra có cấu trúc, nhằm nâng cao độ chính xác và xử lý truy vấn bị lỗi.
- **Sở hữu quy trình suy luận:** Hiểu khả năng của hệ thống trong việc tự kiểm soát quy trình suy luận, quyết định cách tiếp cận vấn đề mà không dựa vào các con đường được định nghĩa trước.
- **Quy trình làm việc:** Hiểu cách một mô hình agentic tự quyết định thu thập báo cáo xu hướng thị trường, xác định dữ liệu đối thủ, liên kết chỉ số bán hàng nội bộ, tổng hợp kết quả và đánh giá chiến lược.
- **Vòng lặp lặp lại, tích hợp công cụ và bộ nhớ:** Tìm hiểu về sự dựa vào mô hình tương tác vòng lặp, duy trì trạng thái và bộ nhớ xuyên suốt các bước để tránh lặp lại vòng lặp và đưa ra quyết định thông minh hơn.
- **Xử lý lỗi và tự sửa:** Khám phá cơ chế tự sửa lỗi mạnh mẽ của hệ thống, bao gồm lặp lại và truy vấn lại, sử dụng công cụ chẩn đoán và dự phòng giám sát bởi con người.
- **Ranh giới của quyền tự chủ:** Hiểu giới hạn của Agentic RAG, tập trung vào tự chủ theo miền, phụ thuộc vào hạ tầng và tôn trọng các giới hạn bảo vệ.
- **Trường hợp sử dụng thực tế và giá trị:** Xác định bối cảnh mà Agentic RAG phát huy hiệu quả, như môi trường ưu tiên độ chính xác, tương tác cơ sở dữ liệu phức tạp và quy trình làm việc mở rộng.
- **Quản trị, minh bạch và tin cậy:** Tìm hiểu tầm quan trọng của quản trị và minh bạch, bao gồm giải thích suy luận, kiểm soát thiên lệch và sự giám sát của con người.

## Agentic RAG là gì?

Agentic Retrieval-Augmented Generation (Agentic RAG) là một mô hình AI mới nổi trong đó các mô hình ngôn ngữ lớn (LLM) tự động lập kế hoạch các bước tiếp theo trong khi tra cứu thông tin từ các nguồn bên ngoài. Khác với mẫu tra cứu-tự đọc tĩnh, Agentic RAG bao gồm các lệnh gọi lặp lại tới LLM, xen kẽ với các lệnh gọi công cụ hoặc chức năng và các đầu ra có cấu trúc. Hệ thống đánh giá kết quả, tinh chỉnh truy vấn, gọi thêm công cụ nếu cần và tiếp tục chu trình cho đến khi đạt được giải pháp thỏa mãn. Phong cách “maker-checker” lặp lại này cải thiện độ chính xác, xử lý truy vấn bị lỗi và đảm bảo kết quả chất lượng cao.

Hệ thống chủ động kiểm soát quy trình suy luận của mình, viết lại truy vấn thất bại, chọn phương pháp tra cứu khác nhau và tích hợp nhiều công cụ—chẳng hạn như tìm kiếm vector trong Azure AI Search, cơ sở dữ liệu SQL hoặc API tùy chỉnh—trước khi hoàn thiện câu trả lời. Đặc tính nổi bật của hệ thống agentic là khả năng tự chủ quy trình suy luận. Các triển khai RAG truyền thống dựa vào các con đường được định nghĩa trước, nhưng hệ thống agentic tự xác định chuỗi bước dựa trên chất lượng thông tin thu thập được.

## Định nghĩa Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) là một mô hình AI mới nổi, trong đó các LLM không chỉ tra cứu thông tin từ các nguồn dữ liệu bên ngoài mà còn tự động lập kế hoạch bước tiếp theo. Khác với mẫu tra cứu-tự đọc tĩnh hoặc chuỗi lệnh prompt được viết kỹ lưỡng, Agentic RAG bao gồm vòng lặp các lệnh gọi lặp lại tới LLM, xen kẽ với gọi công cụ hoặc chức năng và đầu ra có cấu trúc. Ở mỗi bước, hệ thống đánh giá kết quả đạt được, quyết định có cần tinh chỉnh truy vấn không, gọi thêm công cụ nếu cần và tiếp tục chu trình cho đến khi đạt giải pháp thỏa đáng.

Phong cách vận hành “maker-checker” lặp lại này nhằm nâng cao độ chính xác, xử lý các truy vấn bị lỗi với cơ sở dữ liệu có cấu trúc (ví dụ NL2SQL), và đảm bảo kết quả cân bằng, chất lượng cao. Thay vì chỉ dựa vào chuỗi prompt được xây dựng kỹ, hệ thống chủ động kiểm soát quy trình suy luận của mình. Nó có thể viết lại truy vấn thất bại, chọn phương pháp tra cứu khác và tích hợp nhiều công cụ—như tìm kiếm vector trong Azure AI Search, cơ sở dữ liệu SQL hoặc API tùy chỉnh—trước khi hoàn thiện câu trả lời. Điều này loại bỏ nhu cầu về các khung điều phối phức tạp. Thay vào đó, một vòng lặp tương đối đơn giản như “gọi LLM → dùng công cụ → gọi LLM → …” có thể tạo ra đầu ra tinh vi và vững chắc.

![Agentic RAG Core Loop](../../../translated_images/vi/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Sở hữu quy trình suy luận

Đặc điểm làm nên sự “agentic” của hệ thống là khả năng tự chủ quy trình suy luận. Các triển khai RAG truyền thống thường phụ thuộc vào con người định sẵn lộ trình cho mô hình: một chuỗi suy nghĩ xác định lúc nào lấy dữ liệu gì.
Nhưng khi hệ thống thật sự agentic, nó sẽ tự mình quyết định cách tiếp cận vấn đề. Nó không chỉ thực thi kịch bản; mà tự động xác định chuỗi bước dựa trên chất lượng thông tin tìm thấy.
Ví dụ, nếu được yêu cầu tạo chiến lược ra mắt sản phẩm, nó không chỉ dựa vào prompt ghi chi tiết chu trình nghiên cứu và quyết định. Thay vào đó, mô hình agentic sẽ tự quyết định:

1. Thu thập báo cáo xu hướng thị trường hiện tại bằng cách sử dụng Bing Web Grounding
2. Xác định dữ liệu đối thủ liên quan qua Azure AI Search.
3.	Liên kết các chỉ số bán hàng nội bộ theo lịch sử qua Azure SQL Database.
4. Tổng hợp các phát hiện thành chiến lược gắn kết được điều phối bởi Azure OpenAI Service.
5.	Đánh giá chiến lược tìm lỗ hổng hoặc mâu thuẫn, yêu cầu truy xuất dữ liệu thêm nếu cần.
Tất cả các bước này—tinh chỉnh truy vấn, chọn nguồn, lặp lại cho tới khi “hài lòng” với câu trả lời—đều do mô hình quyết định, không phải do con người lập kịch bản trước.

## Vòng lặp lặp lại, tích hợp công cụ và bộ nhớ

![Tool Integration Architecture](../../../translated_images/vi/tool-integration.0f569710b5c17c10.webp)

Một hệ thống agentic dựa vào mẫu tương tác vòng lặp:

- **Lệnh gọi ban đầu:** Mục tiêu của người dùng (hay còn gọi là prompt người dùng) được chuyển tới LLM.
- **Triệu hồi công cụ:** Nếu mô hình nhận thấy thông tin thiếu hoặc hướng dẫn mơ hồ, nó chọn công cụ hoặc phương pháp tra cứu—ví dụ truy vấn cơ sở dữ liệu vector (như Azure AI Search Hybrid tìm kiếm dữ liệu riêng tư) hoặc gọi SQL có cấu trúc—để thu thập thêm ngữ cảnh.
- **Đánh giá & Tinh chỉnh:** Sau khi xem lại dữ liệu trả về, mô hình quyết định liệu thông tin đó có đủ không. Nếu không, nó sửa truy vấn, thử công cụ khác hoặc điều chỉnh phương pháp tiếp cận.
- **Lặp lại cho đến khi hài lòng:** Chu kỳ được tiếp tục cho đến khi mô hình xác định đã có đủ sự rõ ràng và bằng chứng để đưa ra phản hồi cuối cùng vững chắc.
- **Bộ nhớ & trạng thái:** Vì hệ thống duy trì trạng thái và bộ nhớ qua các bước, nó có thể nhớ lại các lần thử trước và kết quả, tránh lặp lại vòng lặp và đưa ra quyết định sáng suốt hơn khi tiến hành.

Qua thời gian, điều này tạo cảm giác hiểu biết tiến triển, cho phép mô hình xử lý các tác vụ phức tạp, nhiều bước mà không cần con người thường xuyên can thiệp hay chỉnh sửa prompt.

## Xử lý các chế độ lỗi và tự sửa lỗi

Quyền tự chủ của Agentic RAG cũng gồm cơ chế tự sửa lỗi vững chắc. Khi hệ thống gặp bế tắc—như lấy tài liệu không liên quan hay truy vấn bị lỗi—nó có thể:

- **Lặp lại và truy vấn lại:** Thay vì trả về phản hồi ít giá trị, mô hình thử các chiến lược tìm kiếm mới, viết lại truy vấn cơ sở dữ liệu, hoặc xem bộ dữ liệu thay thế.
- **Dùng công cụ chẩn đoán:** Hệ thống có thể gọi thêm chức năng giúp gỡ lỗi các bước suy luận hoặc xác nhận độ đúng của dữ liệu thu thập. Các công cụ như Azure AI Tracing sẽ rất quan trọng để đảm bảo khả năng quan sát và giám sát vững chắc.
- **Dựa vào giám sát của con người:** Với những tình huống quan trọng hoặc lỗi lặp lại, mô hình có thể báo hiệu sự không chắc chắn và yêu cầu hướng dẫn từ con người. Khi người dùng cung cấp phản hồi chỉnh sửa, mô hình sẽ học hỏi để áp dụng vào các lần kế tiếp.

Phương pháp lặp lại và linh hoạt này cho phép mô hình cải thiện liên tục, đảm bảo không chỉ đơn thuần là hệ thống một lần mà là hệ thống học từ sai sót trong một phiên làm việc.

![Self Correction Mechanism](../../../translated_images/vi/self-correction.da87f3783b7f174b.webp)

## Ranh giới của quyền tự chủ

Dù có tính tự chủ trong phạm vi nhiệm vụ, Agentic RAG không tương đương với Trí tuệ Nhân tạo Tổng quát. Khả năng “agentic” của nó giới hạn trong công cụ, nguồn dữ liệu và chính sách do nhà phát triển con người cung cấp. Nó không thể tự tạo công cụ riêng hoặc vượt ra ngoài ranh giới miền được thiết lập. Thay vào đó, nó nổi trội trong việc phối hợp động các nguồn lực hiện có.
Sự khác biệt chính so với các dạng AI tiên tiến hơn gồm:

1. **Tự chủ theo miền cụ thể:** Hệ thống Agentic RAG tập trung đạt mục tiêu do người dùng xác định trong phạm vi miền biết trước, sử dụng chiến lược như viết lại truy vấn hoặc chọn công cụ để cải thiện kết quả.
2. **Phụ thuộc vào hạ tầng:** Khả năng của hệ thống phụ thuộc vào công cụ và dữ liệu được các nhà phát triển tích hợp. Nó không thể vượt ngoài những giới hạn này nếu không có sự can thiệp của con người.
3. **Tôn trọng các giới hạn bảo vệ:** Các hướng dẫn đạo đức, quy định tuân thủ và chính sách doanh nghiệp rất quan trọng. Sự tự do của agent luôn bị giới hạn bởi các biện pháp an toàn và cơ chế giám sát (hy vọng là vậy)

## Các trường hợp sử dụng thực tế và giá trị

Agentic RAG phát huy mạnh trong các tình huống yêu cầu tinh chỉnh và độ chính xác lặp đi lặp lại:

1. **Môi trường ưu tiên độ chính xác:** Trong kiểm tra tuân thủ, phân tích quy định hay nghiên cứu pháp lý, mô hình agentic liên tục xác minh sự kiện, tham khảo đa nguồn và viết lại truy vấn cho tới khi có câu trả lời được kiểm chứng kỹ lưỡng.
2. **Tương tác cơ sở dữ liệu phức tạp:** Khi làm việc với dữ liệu có cấu trúc mà truy vấn thường xuyên thất bại hoặc cần điều chỉnh, hệ thống có thể tự động tinh chỉnh truy vấn sử dụng Azure SQL hoặc Microsoft Fabric OneLake, đảm bảo kết quả truy xuất phù hợp ý định người dùng.
3. **Quy trình làm việc mở rộng:** Các phiên làm việc kéo dài có thể phát triển khi thông tin mới xuất hiện. Agentic RAG liên tục cập nhật dữ liệu mới, thay đổi chiến lược khi hiểu rõ hơn về vấn đề.

## Quản trị, minh bạch và tin cậy

Khi các hệ thống này tự chủ hơn trong suy luận, quản trị và minh bạch trở nên rất quan trọng:

- **Suy luận có thể giải thích:** Mô hình có thể cung cấp dấu vết kiểm toán các truy vấn đã thực hiện, nguồn đã tham khảo và các bước suy luận để đi tới kết luận. Công cụ như Azure AI Content Safety và Azure AI Tracing / GenAIOps giúp duy trì minh bạch và giảm thiểu rủi ro.
- **Kiểm soát thiên lệch và truy xuất cân bằng:** Nhà phát triển có thể điều chỉnh chiến lược truy xuất để đảm bảo các nguồn dữ liệu cân bằng, đại diện, đồng thời định kỳ kiểm tra đầu ra để phát hiện thiên lệch hoặc mẫu lệch dùng mô hình tùy chỉnh dành cho các tổ chức khoa học dữ liệu nâng cao qua Azure Machine Learning.
- **Giám sát của con người và tuân thủ:** Với các nhiệm vụ nhạy cảm, xem xét của con người vẫn thiết yếu. Agentic RAG không thay thế phán đoán con người trong các quyết định quan trọng—mà hỗ trợ bằng cách cung cấp các tùy chọn được rà soát kỹ hơn.

Việc có công cụ ghi lại rõ ràng các hành động là cần thiết. Nếu không, việc gỡ lỗi quy trình nhiều bước sẽ rất khó khăn. Xem ví dụ dưới đây từ Literal AI (công ty phát triển Chainlit) cho một lần chạy Agent:

![AgentRunExample](../../../translated_images/vi/AgentRunExample.471a94bc40cbdc0c.webp)

## Kết luận

Agentic RAG đại diện cho bước tiến tự nhiên trong cách các hệ thống AI xử lý các tác vụ phức tạp, dữ liệu cường độ cao. Bằng cách áp dụng mô hình tương tác vòng lặp, tự chọn công cụ và tinh chỉnh truy vấn cho đến khi đạt kết quả chất lượng cao, hệ thống vượt ra khỏi khuôn khổ theo prompt tĩnh thành người quyết định thích nghi và nhận thức ngữ cảnh tốt hơn. Dù vẫn bị giới hạn bởi hạ tầng do con người định nghĩa và hướng dẫn đạo đức, các khả năng agentic này cho phép tương tác AI phong phú hơn, linh hoạt hơn và hữu ích hơn cho cả doanh nghiệp và người dùng cuối.

### Bạn còn câu hỏi nào về Agentic RAG?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ các học viên khác, tham dự giờ làm việc và được giải đáp thắc mắc về AI Agent.

## Tài nguyên bổ sung

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Triển khai Retrieval Augmented Generation (RAG) với Azure OpenAI Service: Tìm hiểu cách dùng dữ liệu riêng của bạn với Azure OpenAI Service. Module Microsoft Learn này cung cấp hướng dẫn toàn diện về triển khai RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Đánh giá các ứng dụng AI tạo sinh với Microsoft Foundry: Bài viết này trình bày đánh giá và so sánh các mô hình trên tập dữ liệu công khai, bao gồm ứng dụng AI Agentic và kiến trúc RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Agentic RAG là gì | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Hướng dẫn toàn diện về Retrieval Augmented Generation dựa trên Agent – Tin tức từ generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: tăng tốc RAG của bạn với việc tái diễn đạt truy vấn và tự truy vấn! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Thêm các lớp Agentic vào RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Tương lai của Trợ lý Kiến thức: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Cách xây dựng hệ thống Agentic RAG</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Sử dụng Microsoft Foundry Agent Service để mở rộng quy mô các tác nhân AI của bạn</a>

### Bài báo học thuật

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Tinh chỉnh lặp đi lặp lại với Phản hồi Tự thân</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Các tác nhân ngôn ngữ với Học tăng cường bằng lời nói</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Mô hình Ngôn ngữ Lớn có thể tự chỉnh sửa với Phê bình tương tác công cụ</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Tạo nội dung tăng cường truy xuất theo kiểu Agentic: Tổng quan về Agentic RAG</a>

## Kiểm tra nhanh Tác nhân này (Tùy chọn)

Sau khi bạn học cách triển khai các tác nhân trong [Bài học 16](../16-deploying-scalable-agents/README.md), bạn có thể kiểm tra nhanh `TravelRAGAgent` của bài học này — kiểm tra xem các câu trả lời có dựa trên cơ sở kiến thức hay không — với [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Xem [`tests/README.md`](../tests/README.md) để biết cách chạy kiểm tra.

## Bài học trước

[Mẫu Thiết kế Sử dụng Công cụ](../04-tool-use/README.md)

## Bài học tiếp theo

[Xây dựng tác nhân AI đáng tin cậy](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->