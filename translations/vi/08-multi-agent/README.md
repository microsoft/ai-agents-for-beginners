[![Thiết kế đa tác nhân](../../../translated_images/vi/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Nhấp vào hình ảnh trên để xem video của bài học này)_

# Các mẫu thiết kế đa tác nhân

Ngay khi bạn bắt đầu làm việc trên một dự án liên quan đến nhiều tác nhân, bạn sẽ cần xem xét mẫu thiết kế đa tác nhân. Tuy nhiên, có thể không rõ ngay khi nào nên chuyển sang đa tác nhân và những lợi ích của nó là gì.

## Giới thiệu

Trong bài học này, chúng ta sẽ tìm câu trả lời cho các câu hỏi sau:

- Những kịch bản nào phù hợp với đa tác nhân?
- Ưu điểm của việc sử dụng đa tác nhân so với chỉ một tác nhân thực hiện nhiều nhiệm vụ là gì?
- Các thành phần cơ bản để triển khai mẫu thiết kế đa tác nhân là gì?
- Làm sao để ta có thể quan sát cách các tác nhân tương tác với nhau?

## Mục tiêu học tập

Sau bài học này, bạn nên có khả năng:

- Nhận diện các kịch bản phù hợp với đa tác nhân
- Nhận ra những lợi ích của việc sử dụng đa tác nhân so với chỉ một tác nhân.
- Hiểu rõ các thành phần cấu tạo để triển khai mẫu thiết kế đa tác nhân.

Bức tranh tổng thể là gì?

*Đa tác nhân là một mẫu thiết kế cho phép nhiều tác nhân làm việc cùng nhau để đạt được một mục tiêu chung*.

Mẫu này được sử dụng rộng rãi trong nhiều lĩnh vực, bao gồm robot, hệ thống tự hành, và điện toán phân tán.

## Các kịch bản phù hợp với đa tác nhân

Vậy những kịch bản nào là trường hợp sử dụng tốt cho đa tác nhân? Câu trả lời là có nhiều trường hợp mà việc sử dụng nhiều tác nhân là có lợi, đặc biệt trong các trường hợp sau:

- **Khối lượng công việc lớn**: Khối lượng lớn có thể được chia nhỏ thành các nhiệm vụ nhỏ hơn và giao cho các tác nhân khác nhau, cho phép xử lý đồng thời và hoàn thành nhanh hơn. Ví dụ điển hình là xử lý dữ liệu lớn.
- **Nhiệm vụ phức tạp**: Nhiệm vụ phức tạp, giống như khối lượng lớn, có thể được chia thành các phân công nhỏ hơn và giao cho các tác nhân, mỗi tác nhân chuyên về một khía cạnh cụ thể của nhiệm vụ. Ví dụ điển hình là trong xe tự hành, các tác nhân điều phối định vị, phát hiện vật cản, và liên lạc với các xe khác.
- **Chuyên môn đa dạng**: Các tác nhân khác nhau có thể có chuyên môn đa dạng, giúp xử lý các khía cạnh khác nhau của nhiệm vụ hiệu quả hơn so với một tác nhân duy nhất. Ví dụ trong lĩnh vực chăm sóc sức khỏe, các tác nhân có thể quản lý chẩn đoán, kế hoạch điều trị và theo dõi bệnh nhân.

## Lợi ích của việc sử dụng đa tác nhân so với một tác nhân duy nhất

Hệ thống một tác nhân có thể đáp ứng tốt các nhiệm vụ đơn giản, nhưng với các nhiệm vụ phức tạp, sử dụng nhiều tác nhân sẽ mang lại một số lợi thế:

- **Chuyên môn hóa**: Mỗi tác nhân có thể chuyên về một nhiệm vụ cụ thể. Thiếu sự chuyên môn hóa ở một tác nhân đơn nghĩa là bạn có một tác nhân làm tất cả mọi thứ nhưng có thể bị bối rối khi phải xử lý nhiệm vụ phức tạp. Ví dụ, nó có thể làm một nhiệm vụ mà nó không phù hợp nhất.
- **Tăng khả năng mở rộng**: Dễ dàng mở rộng hệ thống bằng cách thêm nhiều tác nhân hơn thay vì quá tải một tác nhân duy nhất.
- **Khả năng chịu lỗi**: Nếu một tác nhân thất bại, các tác nhân khác vẫn có thể tiếp tục hoạt động, đảm bảo độ tin cậy của hệ thống.

Hãy lấy ví dụ, đặt chuyến đi cho một người dùng. Hệ thống một tác nhân sẽ phải xử lý tất cả các khía cạnh của quá trình đặt chuyến đi, từ tìm chuyến bay đến đặt khách sạn và thuê xe. Để làm được điều này, tác nhân đó phải có công cụ xử lý tất cả các nhiệm vụ này. Điều này có thể dẫn đến một hệ thống phức tạp và đồng nhất khó bảo trì và mở rộng. Hệ thống đa tác nhân, ngược lại, có thể có các tác nhân chuyên về tìm chuyến bay, đặt khách sạn, và thuê xe. Điều này làm cho hệ thống trở nên mô đun hơn, dễ dàng bảo trì và mở rộng.

So sánh điều này với một đại lý du lịch do một cửa hàng gia đình điều hành so với một đại lý du lịch theo mô hình nhượng quyền. Cửa hàng gia đình sẽ có một tác nhân xử lý tất cả các khía cạnh của quá trình đặt chuyến, trong khi mô hình nhượng quyền sẽ có các tác nhân xử lý riêng từng khía cạnh của quá trình đặt chuyến.

## Các thành phần cơ bản để triển khai mẫu thiết kế đa tác nhân

Trước khi triển khai mẫu thiết kế đa tác nhân, bạn cần hiểu các thành phần cấu thành của mẫu này.

Hãy làm điều này cụ thể hơn bằng ví dụ đặt chuyến đi cho người dùng. Trong trường hợp này, các thành phần cơ bản bao gồm:

- **Giao tiếp giữa các tác nhân**: Các tác nhân tìm chuyến bay, đặt khách sạn, và thuê xe cần giao tiếp và chia sẻ thông tin về sở thích và hạn chế của người dùng. Bạn phải quyết định các giao thức và phương pháp giao tiếp này. Cụ thể, tác nhân tìm chuyến bay cần giao tiếp với tác nhân đặt khách sạn để đảm bảo khách sạn được đặt trong cùng ngày với chuyến bay. Điều đó nghĩa là các tác nhân cần chia sẻ thông tin về ngày đi lại của người dùng, bạn cần quyết định *tác nhân nào chia sẻ thông tin và chia sẻ như thế nào*.
- **Cơ chế phối hợp**: Các tác nhân cần phối hợp hành động để đảm bảo sở thích và hạn chế của người dùng được đáp ứng. Ví dụ sở thích của người dùng có thể là muốn khách sạn gần sân bay trong khi hạn chế là xe thuê chỉ có ở sân bay. Điều này có nghĩa tác nhân đặt khách sạn cần phối hợp với tác nhân đặt xe để đảm bảo sở thích và hạn chế đó. Bạn cần quyết định *cách các tác nhân phối hợp hành động*.
- **Kiến trúc tác nhân**: Các tác nhân cần có cấu trúc nội bộ để đưa ra quyết định và học hỏi từ tương tác với người dùng. Ví dụ tác nhân tìm chuyến bay cần có cấu trúc để quyết định các chuyến bay đề xuất cho người dùng. Bạn cần quyết định *cách các tác nhân ra quyết định và học hỏi từ tương tác với người dùng*. Ví dụ một tác nhân có thể dùng mô hình học máy để đề xuất chuyến bay dựa trên sở thích trước đây của người dùng.
- **Tính khả kiến trong tương tác đa tác nhân**: Bạn cần có khả năng quan sát cách các tác nhân tương tác với nhau. Điều này nghĩa là bạn cần các công cụ và kỹ thuật theo dõi hoạt động và tương tác của tác nhân. Có thể là các công cụ ghi nhật ký và giám sát, công cụ trực quan hóa và đo lường hiệu suất.
- **Mẫu đa tác nhân**: Có nhiều mẫu cho hệ thống đa tác nhân như kiến trúc tập trung, phi tập trung và lai. Bạn cần chọn mẫu phù hợp nhất với trường hợp sử dụng.
- **Con người tham gia**: Trong hầu hết các trường hợp, bạn sẽ có con người tham gia và cần hướng dẫn các tác nhân khi nào cần hỏi sự can thiệp của con người. Ví dụ người dùng yêu cầu một khách sạn hoặc chuyến bay cụ thể mà tác nhân chưa đề xuất hoặc yêu cầu xác nhận trước khi đặt.

## Tính khả kiến trong tương tác đa tác nhân

Việc có khả năng quan sát cách các tác nhân tương tác với nhau rất quan trọng. Khả năng này cần thiết để gỡ lỗi, tối ưu và đảm bảo hiệu quả toàn hệ thống. Để đạt được điều này, bạn cần có các công cụ và kỹ thuật để theo dõi hoạt động và tương tác của tác nhân. Có thể dưới dạng các công cụ ghi nhật ký, giám sát, trực quan hóa và đo lường hiệu suất.

Ví dụ, trong trường hợp đặt chuyến đi cho người dùng, bạn có thể có một bảng điều khiển hiển thị trạng thái của từng tác nhân, sở thích và hạn chế của người dùng, và các tương tác giữa các tác nhân. Bảng điều khiển này có thể hiển thị ngày đi lại của người dùng, các chuyến bay được đề xuất bởi tác nhân chuyến bay, các khách sạn được đề xuất bởi tác nhân khách sạn, và các xe thuê được đề xuất bởi tác nhân thuê xe. Điều này giúp bạn có cái nhìn rõ ràng về cách các tác nhân tương tác và liệu sở thích và hạn chế của người dùng có được đáp ứng không.

Hãy xem xét chi tiết từng khía cạnh này.

- **Công cụ ghi nhật ký và giám sát**: Bạn nên ghi lại từng hành động của tác nhân. Một mục nhập nhật ký có thể lưu thông tin về tác nhân thực hiện hành động, hành động đã làm, thời gian thực hiện và kết quả. Thông tin này sau đó có thể dùng để gỡ lỗi, tối ưu và nhiều việc khác.

- **Công cụ trực quan hóa**: Công cụ này giúp bạn nhìn thấy tương tác giữa các tác nhân một cách trực quan hơn. Ví dụ, bạn có thể có một biểu đồ thể hiện luồng thông tin giữa các tác nhân. Điều này giúp phát hiện điểm nghẽn, sự không hiệu quả và các vấn đề khác trong hệ thống.

- **Chỉ số hiệu suất**: Chỉ số hiệu suất giúp theo dõi hiệu quả của hệ thống đa tác nhân. Ví dụ, bạn có thể theo dõi thời gian hoàn thành nhiệm vụ, số lượng nhiệm vụ hoàn thành mỗi đơn vị thời gian, và độ chính xác của các đề xuất do các tác nhân đưa ra. Thông tin này giúp xác định các điểm cần cải thiện và tối ưu hệ thống.

## Các mẫu đa tác nhân

Hãy khám phá một số mẫu cụ thể bạn có thể sử dụng để tạo ứng dụng đa tác nhân. Dưới đây là một số mẫu thú vị đáng được xem xét:

### Trò chuyện nhóm

Mẫu này hữu ích khi bạn muốn tạo một ứng dụng trò chuyện nhóm nơi nhiều tác nhân có thể giao tiếp với nhau. Các trường hợp sử dụng điển hình cho mẫu này bao gồm hợp tác nhóm, hỗ trợ khách hàng, và mạng xã hội.

Trong mẫu này, mỗi tác nhân đại diện cho một người dùng trong nhóm trò chuyện, và tin nhắn được trao đổi giữa các tác nhân qua giao thức tin nhắn. Các tác nhân có thể gửi tin nhắn vào nhóm, nhận tin nhắn từ nhóm, và phản hồi tin nhắn từ các tác nhân khác.

Mẫu này có thể triển khai bằng kiến trúc tập trung, nơi tất cả tin nhắn được chuyển qua máy chủ trung tâm, hoặc kiến trúc phi tập trung, nơi tin nhắn được trao đổi trực tiếp.

![Trò chuyện nhóm](../../../translated_images/vi/multi-agent-group-chat.ec10f4cde556babd.webp)

### Chuyển giao nhiệm vụ

Mẫu này hữu ích khi bạn muốn tạo ứng dụng mà nhiều tác nhân có thể chuyển giao nhiệm vụ cho nhau.

Các trường hợp sử dụng điển hình cho mẫu này bao gồm hỗ trợ khách hàng, quản lý nhiệm vụ, và tự động hóa quy trình làm việc.

Trong mẫu này, mỗi tác nhân đại diện cho một nhiệm vụ hoặc bước trong quy trình, và các tác nhân có thể chuyển giao nhiệm vụ cho nhau dựa trên các quy tắc đã định trước.

![Chuyển giao nhiệm vụ](../../../translated_images/vi/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Lọc cộng tác

Mẫu này hữu ích khi bạn muốn tạo ứng dụng mà nhiều tác nhân có thể cộng tác để đưa ra đề xuất cho người dùng.

Lý do bạn muốn nhiều tác nhân cộng tác là vì mỗi tác nhân có thể có chuyên môn khác nhau và đóng góp vào quá trình đề xuất theo những cách khác nhau.

Hãy lấy ví dụ một người dùng muốn nhận đề xuất cổ phiếu tốt nhất để mua trên thị trường chứng khoán.

- **Chuyên gia ngành nghề**: Một tác nhân có thể là chuyên gia trong lĩnh vực cụ thể.
- **Phân tích kỹ thuật**: Một tác nhân khác có thể là chuyên gia phân tích kỹ thuật.
- **Phân tích cơ bản**: Và một tác nhân nữa có thể là chuyên gia phân tích cơ bản. Bằng cách cộng tác, các tác nhân này có thể cung cấp một đề xuất toàn diện hơn cho người dùng.

![Đề xuất](../../../translated_images/vi/multi-agent-filtering.d959cb129dc9f608.webp)

## Kịch bản: Quy trình hoàn tiền

Hãy xem xét một kịch bản khách hàng muốn hoàn tiền cho một sản phẩm, có thể có khá nhiều tác nhân tham gia trong quy trình này nhưng hãy chia ra thành các tác nhân riêng cho quy trình hoàn tiền và các tác nhân chung có thể dùng cho các quy trình khác.

**Các tác nhân riêng cho quy trình hoàn tiền**:

Sau đây là một số tác nhân có thể tham gia vào quy trình hoàn tiền:

- **Tác nhân khách hàng**: Đại diện cho khách hàng và chịu trách nhiệm khởi tạo quy trình hoàn tiền.
- **Tác nhân người bán**: Đại diện cho người bán và chịu trách nhiệm xử lý việc hoàn tiền.
- **Tác nhân thanh toán**: Đại diện cho quy trình thanh toán và chịu trách nhiệm hoàn tiền cho khách hàng.
- **Tác nhân giải quyết**: Đại diện cho quy trình giải quyết và chịu trách nhiệm xử lý các vấn đề phát sinh trong quá trình hoàn tiền.
- **Tác nhân tuân thủ**: Đại diện cho quy trình tuân thủ và chịu trách nhiệm đảm bảo quy trình hoàn tiền phù hợp với các quy định và chính sách.

**Các tác nhân chung**:

Các tác nhân này có thể được sử dụng bởi các bộ phận khác trong doanh nghiệp của bạn.

- **Tác nhân vận chuyển**: Đại diện cho quy trình vận chuyển và chịu trách nhiệm gửi hàng trả lại cho người bán. Tác nhân này có thể dùng cả cho quy trình hoàn tiền và cho việc vận chuyển sản phẩm theo đơn mua hàng thông thường.
- **Tác nhân phản hồi**: Đại diện cho quy trình thu thập phản hồi từ khách hàng. Phản hồi có thể được thu thập bất cứ lúc nào chứ không chỉ trong quy trình hoàn tiền.
- **Tác nhân tăng cấp**: Đại diện cho quy trình tăng cấp và chịu trách nhiệm chuyển các vấn đề đến mức hỗ trợ cao hơn. Loại tác nhân này có thể dùng cho bất kỳ quy trình nào cần tăng cấp vấn đề.
- **Tác nhân thông báo**: Đại diện cho quy trình gửi thông báo và chịu trách nhiệm gửi các thông báo đến khách hàng trong các giai đoạn khác nhau của quy trình hoàn tiền.
- **Tác nhân phân tích**: Đại diện cho quy trình phân tích và chịu trách nhiệm phân tích dữ liệu liên quan đến quy trình hoàn tiền.
- **Tác nhân kiểm toán**: Đại diện cho quy trình kiểm toán và chịu trách nhiệm kiểm tra quy trình hoàn tiền để đảm bảo được thực thi đúng.
- **Tác nhân báo cáo**: Đại diện cho quy trình báo cáo và chịu trách nhiệm tạo báo cáo về quy trình hoàn tiền.
- **Tác nhân kiến thức**: Đại diện cho quy trình quản lý kiến thức và chịu trách nhiệm duy trì cơ sở tri thức liên quan đến quy trình hoàn tiền. Tác nhân này có thể am hiểu cả về hoàn tiền và các phần khác trong doanh nghiệp.
- **Tác nhân bảo mật**: Đại diện cho quy trình bảo mật và chịu trách nhiệm đảm bảo an toàn cho quy trình hoàn tiền.
- **Tác nhân chất lượng**: Đại diện cho quy trình chất lượng và chịu trách nhiệm đảm bảo chất lượng của quy trình hoàn tiền.

Có khá nhiều tác nhân đã được liệt kê vừa cho quy trình hoàn tiền riêng biệt vừa cho các tác nhân chung có thể dùng ở các bộ phận khác trong doanh nghiệp. Hy vọng điều này giúp bạn hình dung cách quyết định các tác nhân cần dùng trong hệ thống đa tác nhân của bạn.

## Bài tập

Thiết kế một hệ thống đa tác nhân cho quy trình hỗ trợ khách hàng. Xác định các tác nhân tham gia quy trình, vai trò và trách nhiệm của họ, và cách họ tương tác với nhau. Cân nhắc cả các tác nhân riêng cho quy trình hỗ trợ khách hàng và các tác nhân chung có thể dùng ở các phần khác của doanh nghiệp.


> Hãy suy nghĩ kỹ trước khi bạn đọc giải pháp dưới đây, bạn có thể cần nhiều đại lý hơn bạn nghĩ.

> MẸO: Hãy nghĩ về các giai đoạn khác nhau của quy trình hỗ trợ khách hàng và cũng cân nhắc các đại lý cần thiết cho bất kỳ hệ thống nào.

## Giải pháp

[Giải pháp](./solution/solution.md)

## Kiểm tra kiến thức

### Câu hỏi 1

Kịch bản nào phù hợp nhất cho hệ thống đa đại lý?

- [ ] A1: Một bot hỗ trợ trả lời các câu hỏi phổ biến sử dụng một cơ sở tri thức và một bộ công cụ nhỏ.
- [ ] A2: Một quy trình hoàn tiền cần các vai trò riêng biệt về gian lận, thanh toán và tuân thủ, mỗi vai trò có công cụ riêng, và kết quả của họ phải được phối hợp.
- [ ] A3: Yêu cầu phân loại đơn giản giống nhau đến hàng ngàn lần mỗi giờ.

### Câu hỏi 2

Khi nào một đại lý đơn lẻ thường là lựa chọn tốt hơn?

- [ ] A1: Nhiệm vụ có thể được xử lý với một bộ hướng dẫn và công cụ duy nhất, không cần chuyển giao chuyên môn.
- [ ] A2: Đại lý có quyền truy cập vào hơn một công cụ.
- [ ] A3: Quy trình công việc yêu cầu các vai trò riêng biệt với các quyền khác nhau và các dấu vết kiểm toán độc lập.

[Giải pháp câu đố](./solution/solution-quiz.md)

## Tóm tắt

Trong bài học này, chúng ta đã xem xét mẫu thiết kế đa đại lý, bao gồm các kịch bản áp dụng đa đại lý, các lợi thế khi sử dụng đa đại lý so với đại lý đơn, các thành phần xây dựng để triển khai mẫu thiết kế đa đại lý, và cách có thể quan sát được cách các đại lý tương tác với nhau.

### Có Thêm Câu Hỏi về Mẫu Thiết Kế Đa Đại Lý?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ những người học khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về Đại Lý AI của bạn.

## Tài nguyên bổ sung

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Tài liệu Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Mẫu thiết kế Agentic</a>


## Bài học trước

[Lập kế hoạch thiết kế](../07-planning-design/README.md)

## Bài học tiếp theo

[Siêu nhận thức trong Đại Lý AI](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->