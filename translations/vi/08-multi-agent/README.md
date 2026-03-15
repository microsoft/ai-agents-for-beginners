[![Multi-Agent Design](../../../translated_images/vi/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Bấm vào hình trên để xem video bài học này)_

# Mẫu thiết kế đa tác nhân

Ngay khi bắt đầu làm việc trên một dự án liên quan đến nhiều tác nhân, bạn sẽ cần cân nhắc mẫu thiết kế đa tác nhân. Tuy nhiên, có thể chưa rõ ràng ngay khi nào nên chuyển sang đa tác nhân và lợi ích của nó là gì.

## Giới thiệu

Trong bài học này, chúng ta sẽ trả lời các câu hỏi sau:

- Những tình huống nào thì đa tác nhân có thể áp dụng?
- Lợi ích của việc sử dụng đa tác nhân so với chỉ một tác nhân đơn thực hiện nhiều nhiệm vụ là gì?
- Các thành phần cấu thành để triển khai mẫu thiết kế đa tác nhân là gì?
- Làm thế nào để có thể quan sát được cách các tác nhân tương tác với nhau?

## Mục tiêu học tập

Sau bài học này, bạn sẽ có thể:

- Xác định các tình huống sử dụng đa tác nhân phù hợp
- Nhận biết lợi ích của việc dùng đa tác nhân so với chỉ một tác nhân đơn.
- Hiểu được các thành phần cấu tạo để triển khai mẫu thiết kế đa tác nhân.

Bức tranh tổng thể là gì?

*Đa tác nhân là một mẫu thiết kế cho phép nhiều tác nhân phối hợp cùng nhau để đạt được một mục tiêu chung*.

Mẫu này được sử dụng rộng rãi trong nhiều lĩnh vực, bao gồm robot, hệ thống tự động và tính toán phân tán.

## Các tình huống phù hợp sử dụng đa tác nhân

Vậy những tình huống nào là trường hợp sử dụng tốt cho đa tác nhân? Câu trả lời là có nhiều tình huống mà việc dùng nhiều tác nhân mang lại lợi ích, đặc biệt trong các trường hợp sau:

- **Khối lượng công việc lớn**: Khối lượng công việc lớn có thể được phân chia thành các nhiệm vụ nhỏ hơn và giao cho các tác nhân khác nhau, cho phép xử lý song song và hoàn thành nhanh hơn. Ví dụ trong trường hợp xử lý dữ liệu lớn.
- **Nhiệm vụ phức tạp**: Nhiệm vụ phức tạp, giống như khối lượng công việc lớn, có thể được chia nhỏ thành các tiểu nhiệm vụ và giao cho các tác nhân, mỗi tác nhân chuyên về một khía cạnh cụ thể của nhiệm vụ. Ví dụ điển hình là xe tự lái, trong đó các tác nhân quản lý điều hướng, phát hiện chướng ngại vật và giao tiếp với các xe khác.
- **Chuyên môn đa dạng**: Các tác nhân khác nhau có thể có chuyên môn đa dạng, giúp xử lý các khía cạnh khác nhau của nhiệm vụ hiệu quả hơn một tác nhân đơn. Ví dụ trong lĩnh vực chăm sóc sức khỏe, nơi các tác nhân quản lý chẩn đoán, kế hoạch điều trị và theo dõi bệnh nhân.

## Lợi thế của việc sử dụng đa tác nhân so với tác nhân đơn

Hệ thống tác nhân đơn có thể hoạt động tốt cho các nhiệm vụ đơn giản, nhưng với các nhiệm vụ phức tạp hơn, việc sử dụng nhiều tác nhân có thể mang lại nhiều lợi ích:

- **Chuyên môn hóa**: Mỗi tác nhân có thể được chuyên môn hóa cho một nhiệm vụ cụ thể. Thiếu chuyên môn cho một tác nhân đơn nghĩa là ta có tác nhân có thể làm mọi việc nhưng có thể bị lúng túng khi phải xử lý nhiệm vụ phức tạp. Ví dụ, nó có thể bị giao làm nhiệm vụ không phù hợp nhất.
- **Khả năng mở rộng**: Dễ dàng mở rộng hệ thống bằng cách thêm nhiều tác nhân hơn thay vì khiến một tác nhân bị quá tải.
- **Độ bền lỗi**: Nếu một tác nhân gặp sự cố, các tác nhân khác vẫn có thể tiếp tục hoạt động, đảm bảo độ tin cậy hệ thống.

Hãy lấy ví dụ đặt chuyến đi cho một người dùng. Hệ thống tác nhân đơn sẽ phải xử lý tất cả các khía cạnh của quá trình đặt chuyến đi, từ tìm chuyến bay đến đặt khách sạn và thuê xe. Để làm được điều này với một tác nhân, tác nhân đó phải có công cụ để xử lý tất cả các nhiệm vụ trên. Điều này có thể dẫn đến hệ thống phức tạp, cồng kềnh, khó duy trì và mở rộng. Trong khi đó, hệ thống đa tác nhân có thể có các tác nhân riêng biệt chuyên về tìm chuyến bay, đặt khách sạn và thuê xe, làm cho hệ thống trở nên phân mảnh, dễ bảo trì và mở rộng.

So sánh điều này với một văn phòng du lịch nhỏ quản lý bởi một người hoặc một văn phòng du lịch theo hệ thống nhượng quyền. Văn phòng nhỏ có một tác nhân đảm nhiệm tất cả các công đoạn của quá trình đặt chuyến, trong khi hệ thống nhượng quyền sẽ có các tác nhân khác nhau đảm nhiệm từng phần riêng biệt.

## Các thành phần cấu thành để triển khai mẫu thiết kế đa tác nhân

Trước khi bạn triển khai mẫu thiết kế đa tác nhân, bạn cần hiểu các thành phần cấu thành làm nên mẫu này.

Hãy cụ thể hóa điều này bằng ví dụ đặt chuyến đi cho người dùng. Trong trường hợp này, các thành phần cấu thành có thể bao gồm:

- **Giao tiếp giữa các tác nhân**: Các tác nhân tìm chuyến bay, đặt khách sạn và thuê xe cần giao tiếp và chia sẻ thông tin về sở thích và giới hạn của người dùng. Bạn cần quyết định các giao thức và phương pháp cho giao tiếp này. Cụ thể là tác nhân tìm chuyến bay cần giao tiếp với tác nhân đặt khách sạn để đảm bảo khách sạn được đặt đúng ngày với chuyến bay. Điều này nghĩa là các tác nhân cần chia sẻ thông tin về ngày đi du lịch của người dùng, tức bạn phải quyết định *tác nhân nào chia sẻ thông tin và cách thức chia sẻ*.
- **Cơ chế phối hợp**: Các tác nhân cần phối hợp hành động để đảm bảo các sở thích và giới hạn của người dùng được thỏa mãn. Ví dụ sở thích người dùng có thể là muốn khách sạn gần sân bay, trong khi giới hạn là xe thuê chỉ có sẵn tại sân bay. Điều này nghĩa là tác nhân đặt khách sạn cần phối hợp với tác nhân thuê xe để đáp ứng các nhu cầu và giới hạn đó. Bạn cần xác định *cách các tác nhân phối hợp hành động*.
- **Kiến trúc tác nhân**: Các tác nhân cần có cấu trúc nội bộ để quyết định và học hỏi từ tương tác với người dùng. Ví dụ tác nhân tìm chuyến bay cần có cấu trúc nội bộ để quyết định chuyến bay nào nên đề xuất cho người dùng. Bạn cần xác định *cách các tác nhân ra quyết định và học hỏi từ tương tác người dùng*. Ví dụ, tác nhân tìm chuyến bay có thể dùng mô hình học máy để đề xuất chuyến bay dựa trên sở thích trước đó của người dùng.
- **Quan sát tương tác đa tác nhân**: Bạn cần có khả năng quan sát cách các tác nhân tương tác với nhau. Điều này đòi hỏi có công cụ và kỹ thuật để theo dõi hoạt động và tương tác của các tác nhân. Ví dụ như công cụ ghi log và giám sát, công cụ trực quan hóa, và số liệu hiệu suất.
- **Mẫu đa tác nhân**: Có nhiều mẫu để triển khai hệ thống đa tác nhân, như kiến trúc tập trung, phân tán và hybrid. Bạn cần chọn mẫu phù hợp nhất với trường hợp sử dụng.
- **Có người điều phối**: Trong đa số trường hợp, sẽ có người điều phối và bạn cần chỉ định khi nào các tác nhân nên yêu cầu can thiệp của con người. Ví dụ như khi người dùng yêu cầu một khách sạn hoặc chuyến bay cụ thể mà các tác nhân không đề xuất, hoặc yêu cầu xác nhận trước khi đặt chỗ.

## Quan sát tương tác đa tác nhân

Việc quan sát cách các tác nhân tương tác với nhau là rất quan trọng để gỡ lỗi, tối ưu và đảm bảo hiệu quả tổng thể của hệ thống. Để làm được điều này, bạn cần công cụ và kỹ thuật để theo dõi hoạt động và tương tác của các tác nhân. Điều này có thể được thực hiện qua các công cụ ghi log và giám sát, công cụ trực quan hóa và số liệu hiệu suất.

Ví dụ, trong trường hợp đặt chuyến đi cho người dùng, bạn có thể có một bảng điều khiển hiển thị trạng thái của từng tác nhân, sở thích và giới hạn của người dùng, cũng như các tương tác giữa các tác nhân. Bảng điều khiển này có thể hiển thị ngày đi lại của người dùng, các chuyến bay được tác nhân chuyến bay đề xuất, khách sạn do tác nhân khách sạn đề xuất, và xe thuê do tác nhân thuê xe đề xuất. Từ đó bạn có cái nhìn rõ ràng về cách các tác nhân tương tác với nhau và liệu các sở thích, giới hạn của người dùng có được đáp ứng.

Hãy xem xét kỹ từng khía cạnh dưới đây.

- **Công cụ ghi log và giám sát**: Bạn muốn ghi lại nhật ký cho mỗi hành động của tác nhân. Mỗi bản ghi có thể lưu thông tin về tác nhân thực hiện hành động, hành động đó, thời gian thực hiện và kết quả. Thông tin này dùng để gỡ lỗi, tối ưu và nhiều mục đích khác.
- **Công cụ trực quan hóa**: Các công cụ trực quan có thể giúp bạn thấy được các tương tác giữa các tác nhân một cách trực quan hơn. Ví dụ như một đồ thị thể hiện luồng thông tin giữa các tác nhân. Điều này giúp nhận diện nút nghẽn, bất cập, và các vấn đề khác trong hệ thống.
- **Chỉ số hiệu suất**: Các chỉ số giúp bạn theo dõi hiệu quả của hệ thống đa tác nhân. Ví dụ thời gian hoàn thành một nhiệm vụ, số lượng nhiệm vụ hoàn thành trong một khoảng thời gian, và độ chính xác của đề xuất từ các tác nhân. Thông tin này giúp bạn nhận diện điểm cần cải tiến và tối ưu hệ thống.

## Các mẫu đa tác nhân

Hãy khám phá một số mẫu cụ thể để tạo ứng dụng đa tác nhân. Dưới đây là vài mẫu thú vị đáng xem xét:

### Nhóm chat

Mẫu này hữu ích khi bạn muốn tạo ứng dụng chat nhóm nơi nhiều tác nhân có thể giao tiếp với nhau. Các trường hợp điển hình bao gồm hợp tác nhóm, hỗ trợ khách hàng, và mạng xã hội.

Trong mẫu này, mỗi tác nhân đại diện cho một người dùng trong nhóm chat, và tin nhắn được trao đổi giữa các tác nhân qua giao thức nhắn tin. Các tác nhân có thể gửi tin nhắn tới nhóm, nhận tin nhắn từ nhóm, và phản hồi tin nhắn từ các tác nhân khác.

Mẫu này có thể triển khai bằng kiến trúc tập trung, nơi mọi tin nhắn đi qua một máy chủ trung tâm, hoặc kiến trúc phân tán, nơi tin nhắn trao đổi trực tiếp.

![Group chat](../../../translated_images/vi/multi-agent-group-chat.ec10f4cde556babd.webp)

### Bàn giao nhiệm vụ

Mẫu này hữu ích khi bạn muốn tạo ứng dụng mà các tác nhân có thể bàn giao nhiệm vụ cho nhau.

Trường hợp điển hình bao gồm hỗ trợ khách hàng, quản lý nhiệm vụ, và tự động hóa quy trình làm việc.

Trong mẫu này, mỗi tác nhân đại diện cho một nhiệm vụ hoặc một bước trong quy trình làm việc, và các tác nhân có thể bàn giao nhiệm vụ cho nhau dựa trên các quy tắc định sẵn.

![Hand off](../../../translated_images/vi/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Lọc cộng tác

Mẫu này hữu ích khi bạn muốn tạo ứng dụng mà nhiều tác nhân có thể hợp tác để đưa ra đề xuất cho người dùng.

Lý do muốn nhiều tác nhân hợp tác là vì mỗi tác nhân có thể có chuyên môn khác nhau và góp phần vào quy trình đề xuất theo những cách khác nhau.

Hãy lấy ví dụ người dùng muốn đề xuất cổ phiếu tốt nhất để mua trên thị trường chứng khoán.

- **Chuyên gia ngành**: Một tác nhân có thể là chuyên gia về một ngành nghề nào đó.
- **Phân tích kỹ thuật**: Một tác nhân khác có thể là chuyên gia phân tích kỹ thuật.
- **Phân tích cơ bản**: Một tác nhân khác là chuyên gia phân tích cơ bản. Bằng sự hợp tác, các tác nhân này có thể cung cấp đề xuất toàn diện hơn cho người dùng.

![Recommendation](../../../translated_images/vi/multi-agent-filtering.d959cb129dc9f608.webp)

## Tình huống: Quy trình hoàn tiền

Xem xét tình huống khách hàng yêu cầu hoàn tiền cho một sản phẩm, có thể có nhiều tác nhân tham gia vào quy trình này nhưng chúng ta hãy chia thành các tác nhân chuyên biệt cho quy trình hoàn tiền và các tác nhân chung dùng cho các quy trình khác.

**Các tác nhân chuyên cho quy trình hoàn tiền**:

Dưới đây là một số tác nhân có thể tham gia quy trình hoàn tiền:

- **Tác nhân khách hàng**: Đại diện cho khách hàng, chịu trách nhiệm khởi tạo quy trình hoàn tiền.
- **Tác nhân người bán**: Đại diện cho người bán, chịu trách nhiệm xử lý việc hoàn tiền.
- **Tác nhân thanh toán**: Đại diện cho quy trình thanh toán, chịu trách nhiệm hoàn tiền cho khách hàng.
- **Tác nhân giải quyết**: Đại diện cho quy trình giải quyết, chịu trách nhiệm xử lý các vấn đề phát sinh trong quy trình hoàn tiền.
- **Tác nhân tuân thủ**: Đại diện cho quy trình tuân thủ, chịu trách nhiệm đảm bảo quy trình hoàn tiền phù hợp với các quy định và chính sách.

**Các tác nhân chung**:

Những tác nhân này có thể dùng cho các phần khác của doanh nghiệp bạn.

- **Tác nhân vận chuyển**: Đại diện cho quy trình vận chuyển, chịu trách nhiệm gửi sản phẩm về cho người bán. Tác nhân này có thể dùng cho cả quy trình hoàn tiền và vận chuyển sản phẩm nói chung như khi mua hàng.
- **Tác nhân phản hồi**: Đại diện cho quy trình thu thập phản hồi, chịu trách nhiệm lấy ý kiến từ khách hàng. Phản hồi có thể được thu thập bất cứ lúc nào, không chỉ trong quy trình hoàn tiền.
- **Tác nhân leo thang**: Đại diện cho quy trình leo thang, chịu trách nhiệm chuyển vấn đề lên cấp hỗ trợ cao hơn. Bạn có thể dùng loại tác nhân này cho mọi quy trình cần leo thang vấn đề.
- **Tác nhân thông báo**: Đại diện cho quy trình thông báo, chịu trách nhiệm gửi thông báo đến khách hàng ở các giai đoạn khác nhau của quy trình hoàn tiền.
- **Tác nhân phân tích**: Đại diện cho quy trình phân tích, chịu trách nhiệm phân tích dữ liệu liên quan đến quy trình hoàn tiền.
- **Tác nhân kiểm toán**: Đại diện cho quy trình kiểm toán, chịu trách nhiệm kiểm tra quy trình hoàn tiền để đảm bảo triển khai đúng.
- **Tác nhân báo cáo**: Đại diện cho quy trình báo cáo, chịu trách nhiệm tạo báo cáo về quy trình hoàn tiền.
- **Tác nhân kiến thức**: Đại diện cho quy trình quản lý kiến thức, chịu trách nhiệm duy trì cơ sở kiến thức liên quan đến quy trình hoàn tiền. Tác nhân này có thể có kiến thức về cả hoàn tiền và các phần khác của doanh nghiệp bạn.
- **Tác nhân bảo mật**: Đại diện cho quy trình bảo mật, chịu trách nhiệm đảm bảo an toàn cho quy trình hoàn tiền.
- **Tác nhân chất lượng**: Đại diện cho quy trình chất lượng, chịu trách nhiệm đảm bảo chất lượng quy trình hoàn tiền.

Có khá nhiều tác nhân đã liệt kê vừa rồi, cả cho quy trình hoàn tiền chuyên biệt lẫn các tác nhân chung dùng cho các phần khác của doanh nghiệp bạn. Hy vọng điều này giúp bạn hình dung cách quyết định nên sử dụng các tác nhân nào trong hệ thống đa tác nhân của mình.

## Bài tập

Thiết kế một hệ thống đa tác nhân cho quy trình hỗ trợ khách hàng. Xác định các tác nhân tham gia vào quy trình, vai trò và trách nhiệm của họ, cũng như cách họ tương tác với nhau. Cân nhắc cả các tác nhân chuyên biệt cho quy trình hỗ trợ khách hàng và các tác nhân chung có thể dùng ở các phần khác của doanh nghiệp bạn.
> Hãy suy nghĩ trước khi bạn đọc giải pháp sau, bạn có thể cần nhiều đại lý hơn bạn nghĩ.

> TIP: Hãy nghĩ về các giai đoạn khác nhau của quy trình hỗ trợ khách hàng và cũng xem xét các đại lý cần thiết cho bất kỳ hệ thống nào.

## Giải pháp

[Solution](./solution/solution.md)

## Kiểm tra kiến thức

Câu hỏi: Khi nào bạn nên cân nhắc sử dụng đa đại lý?

- [ ] A1: Khi bạn có khối lượng công việc nhỏ và nhiệm vụ đơn giản.
- [ ] A2: Khi bạn có khối lượng công việc lớn
- [ ] A3: Khi bạn có một nhiệm vụ đơn giản.

[Solution quiz](./solution/solution-quiz.md)

## Tóm tắt

Trong bài học này, chúng ta đã xem xét mẫu thiết kế đa đại lý, bao gồm các tình huống mà đa đại lý được áp dụng, những lợi thế của việc sử dụng đa đại lý so với một đại lý duy nhất, các yếu tố xây dựng để triển khai mẫu thiết kế đa đại lý, và cách để có cái nhìn rõ ràng về cách các đại lý nhiều tương tác với nhau.

### Có thêm câu hỏi về Mẫu Thiết Kế Đa Đại Lý?

Tham gia [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ những người học khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về Đại Lý AI của bạn.

## Tài nguyên bổ sung

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Tài liệu Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Các mẫu thiết kế theo hướng đại lý</a>


## Bài học trước

[Planning Design](../07-planning-design/README.md)

## Bài học tiếp theo

[Metacognition in AI Agents](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được coi là nguồn chính xác nhất. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->