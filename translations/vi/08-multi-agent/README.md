<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T17:50:02+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "vi"
}
-->
[![Thiết kế Đa Tác Nhân](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.vi.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Nhấp vào hình ảnh trên để xem video của bài học này)_

# Mẫu thiết kế đa tác nhân

Ngay khi bạn bắt đầu làm việc trên một dự án liên quan đến nhiều tác nhân, bạn sẽ cần xem xét mẫu thiết kế đa tác nhân. Tuy nhiên, có thể không rõ ràng ngay lập tức khi nào nên chuyển sang sử dụng đa tác nhân và những lợi ích của nó là gì.

## Giới thiệu

Trong bài học này, chúng ta sẽ tìm cách trả lời các câu hỏi sau:

- Những tình huống nào phù hợp để áp dụng đa tác nhân?
- Lợi ích của việc sử dụng đa tác nhân so với chỉ một tác nhân duy nhất thực hiện nhiều nhiệm vụ là gì?
- Các thành phần cơ bản để triển khai mẫu thiết kế đa tác nhân là gì?
- Làm thế nào để chúng ta có thể theo dõi cách các tác nhân tương tác với nhau?

## Mục tiêu học tập

Sau bài học này, bạn sẽ có thể:

- Xác định các tình huống phù hợp để áp dụng đa tác nhân.
- Nhận ra lợi ích của việc sử dụng đa tác nhân so với một tác nhân duy nhất.
- Hiểu các thành phần cơ bản để triển khai mẫu thiết kế đa tác nhân.

Bức tranh lớn hơn là gì?

*Đa tác nhân là một mẫu thiết kế cho phép nhiều tác nhân làm việc cùng nhau để đạt được một mục tiêu chung.*

Mẫu này được sử dụng rộng rãi trong nhiều lĩnh vực, bao gồm robot, hệ thống tự động, và điện toán phân tán.

## Tình huống phù hợp để áp dụng đa tác nhân

Vậy những tình huống nào là trường hợp sử dụng tốt cho đa tác nhân? Câu trả lời là có rất nhiều tình huống mà việc sử dụng nhiều tác nhân mang lại lợi ích, đặc biệt trong các trường hợp sau:

- **Khối lượng công việc lớn**: Khối lượng công việc lớn có thể được chia thành các nhiệm vụ nhỏ hơn và giao cho các tác nhân khác nhau, cho phép xử lý song song và hoàn thành nhanh hơn. Một ví dụ là trong trường hợp xử lý dữ liệu lớn.
- **Nhiệm vụ phức tạp**: Nhiệm vụ phức tạp, giống như khối lượng công việc lớn, có thể được chia thành các nhiệm vụ nhỏ hơn và giao cho các tác nhân khác nhau, mỗi tác nhân chuyên về một khía cạnh cụ thể của nhiệm vụ. Một ví dụ điển hình là trong trường hợp xe tự hành, nơi các tác nhân khác nhau quản lý điều hướng, phát hiện chướng ngại vật, và giao tiếp với các xe khác.
- **Chuyên môn đa dạng**: Các tác nhân khác nhau có thể có chuyên môn đa dạng, cho phép họ xử lý các khía cạnh khác nhau của một nhiệm vụ hiệu quả hơn so với một tác nhân duy nhất. Ví dụ trong lĩnh vực chăm sóc sức khỏe, các tác nhân có thể quản lý chẩn đoán, kế hoạch điều trị, và theo dõi bệnh nhân.

## Lợi ích của việc sử dụng đa tác nhân so với một tác nhân duy nhất

Hệ thống một tác nhân duy nhất có thể hoạt động tốt cho các nhiệm vụ đơn giản, nhưng đối với các nhiệm vụ phức tạp hơn, việc sử dụng nhiều tác nhân có thể mang lại nhiều lợi ích:

- **Chuyên môn hóa**: Mỗi tác nhân có thể chuyên về một nhiệm vụ cụ thể. Việc thiếu chuyên môn hóa trong một tác nhân duy nhất có nghĩa là bạn có một tác nhân có thể làm mọi thứ nhưng có thể bị nhầm lẫn khi đối mặt với một nhiệm vụ phức tạp. Ví dụ, nó có thể thực hiện một nhiệm vụ mà nó không phù hợp nhất.
- **Khả năng mở rộng**: Dễ dàng mở rộng hệ thống bằng cách thêm nhiều tác nhân hơn thay vì làm quá tải một tác nhân duy nhất.
- **Khả năng chịu lỗi**: Nếu một tác nhân gặp sự cố, các tác nhân khác có thể tiếp tục hoạt động, đảm bảo độ tin cậy của hệ thống.

Hãy lấy một ví dụ, đặt một chuyến đi cho người dùng. Một hệ thống một tác nhân duy nhất sẽ phải xử lý tất cả các khía cạnh của quá trình đặt chuyến đi, từ tìm chuyến bay đến đặt khách sạn và xe thuê. Để đạt được điều này với một tác nhân duy nhất, tác nhân sẽ cần có công cụ để xử lý tất cả các nhiệm vụ này. Điều này có thể dẫn đến một hệ thống phức tạp và nguyên khối, khó duy trì và mở rộng. Một hệ thống đa tác nhân, mặt khác, có thể có các tác nhân khác nhau chuyên về tìm chuyến bay, đặt khách sạn, và xe thuê. Điều này sẽ làm cho hệ thống trở nên mô-đun hơn, dễ duy trì và mở rộng.

So sánh điều này với một văn phòng du lịch hoạt động như một cửa hàng nhỏ lẻ so với một văn phòng du lịch hoạt động như một chuỗi nhượng quyền. Cửa hàng nhỏ lẻ sẽ có một tác nhân duy nhất xử lý tất cả các khía cạnh của quá trình đặt chuyến đi, trong khi chuỗi nhượng quyền sẽ có các tác nhân khác nhau xử lý các khía cạnh khác nhau của quá trình đặt chuyến đi.

## Các thành phần cơ bản để triển khai mẫu thiết kế đa tác nhân

Trước khi bạn có thể triển khai mẫu thiết kế đa tác nhân, bạn cần hiểu các thành phần cơ bản tạo nên mẫu này.

Hãy làm cho điều này cụ thể hơn bằng cách lại xem xét ví dụ về việc đặt một chuyến đi cho người dùng. Trong trường hợp này, các thành phần cơ bản sẽ bao gồm:

- **Giao tiếp giữa các tác nhân**: Các tác nhân tìm chuyến bay, đặt khách sạn, và xe thuê cần giao tiếp và chia sẻ thông tin về sở thích và ràng buộc của người dùng. Bạn cần quyết định các giao thức và phương pháp cho giao tiếp này. Điều này có nghĩa cụ thể là tác nhân tìm chuyến bay cần giao tiếp với tác nhân đặt khách sạn để đảm bảo rằng khách sạn được đặt cho cùng ngày với chuyến bay. Điều đó có nghĩa là các tác nhân cần chia sẻ thông tin về ngày đi của người dùng, nghĩa là bạn cần quyết định *các tác nhân nào đang chia sẻ thông tin và cách họ chia sẻ thông tin*.
- **Cơ chế phối hợp**: Các tác nhân cần phối hợp hành động của họ để đảm bảo rằng sở thích và ràng buộc của người dùng được đáp ứng. Một sở thích của người dùng có thể là họ muốn một khách sạn gần sân bay trong khi một ràng buộc có thể là xe thuê chỉ có sẵn tại sân bay. Điều này có nghĩa là tác nhân đặt khách sạn cần phối hợp với tác nhân đặt xe thuê để đảm bảo rằng sở thích và ràng buộc của người dùng được đáp ứng. Điều này có nghĩa là bạn cần quyết định *cách các tác nhân phối hợp hành động của họ*.
- **Kiến trúc tác nhân**: Các tác nhân cần có cấu trúc nội bộ để đưa ra quyết định và học hỏi từ các tương tác với người dùng. Điều này có nghĩa là tác nhân tìm chuyến bay cần có cấu trúc nội bộ để đưa ra quyết định về chuyến bay nào nên được đề xuất cho người dùng. Điều này có nghĩa là bạn cần quyết định *cách các tác nhân đưa ra quyết định và học hỏi từ các tương tác với người dùng*. Ví dụ về cách một tác nhân học hỏi và cải thiện có thể là tác nhân tìm chuyến bay có thể sử dụng một mô hình học máy để đề xuất chuyến bay cho người dùng dựa trên sở thích trước đây của họ.
- **Hiển thị tương tác giữa các tác nhân**: Bạn cần có khả năng theo dõi cách các tác nhân tương tác với nhau. Điều này có nghĩa là bạn cần có các công cụ và kỹ thuật để theo dõi hoạt động và tương tác của các tác nhân. Điều này có thể ở dạng công cụ ghi nhật ký và giám sát, công cụ trực quan hóa, và các chỉ số hiệu suất.
- **Mẫu đa tác nhân**: Có các mẫu khác nhau để triển khai hệ thống đa tác nhân, chẳng hạn như kiến trúc tập trung, phi tập trung, và lai. Bạn cần quyết định mẫu nào phù hợp nhất với trường hợp sử dụng của bạn.
- **Con người trong vòng lặp**: Trong hầu hết các trường hợp, bạn sẽ có con người trong vòng lặp và bạn cần hướng dẫn các tác nhân khi nào cần yêu cầu sự can thiệp của con người. Điều này có thể ở dạng người dùng yêu cầu một khách sạn hoặc chuyến bay cụ thể mà các tác nhân không đề xuất hoặc yêu cầu xác nhận trước khi đặt một chuyến bay hoặc khách sạn.

## Hiển thị tương tác giữa các tác nhân

Điều quan trọng là bạn có khả năng theo dõi cách các tác nhân tương tác với nhau. Khả năng hiển thị này rất cần thiết để gỡ lỗi, tối ưu hóa, và đảm bảo hiệu quả tổng thể của hệ thống. Để đạt được điều này, bạn cần có các công cụ và kỹ thuật để theo dõi hoạt động và tương tác của các tác nhân. Điều này có thể ở dạng công cụ ghi nhật ký và giám sát, công cụ trực quan hóa, và các chỉ số hiệu suất.

Ví dụ, trong trường hợp đặt một chuyến đi cho người dùng, bạn có thể có một bảng điều khiển hiển thị trạng thái của từng tác nhân, sở thích và ràng buộc của người dùng, và các tương tác giữa các tác nhân. Bảng điều khiển này có thể hiển thị ngày đi của người dùng, các chuyến bay được đề xuất bởi tác nhân chuyến bay, các khách sạn được đề xuất bởi tác nhân khách sạn, và các xe thuê được đề xuất bởi tác nhân xe thuê. Điều này sẽ cung cấp cho bạn một cái nhìn rõ ràng về cách các tác nhân tương tác với nhau và liệu sở thích và ràng buộc của người dùng có được đáp ứng hay không.

Hãy xem xét từng khía cạnh này chi tiết hơn.

- **Công cụ ghi nhật ký và giám sát**: Bạn muốn ghi nhật ký cho mỗi hành động được thực hiện bởi một tác nhân. Một mục nhật ký có thể lưu trữ thông tin về tác nhân đã thực hiện hành động, hành động được thực hiện, thời gian hành động được thực hiện, và kết quả của hành động. Thông tin này sau đó có thể được sử dụng để gỡ lỗi, tối ưu hóa và hơn thế nữa.

- **Công cụ trực quan hóa**: Công cụ trực quan hóa có thể giúp bạn thấy các tương tác giữa các tác nhân một cách trực quan hơn. Ví dụ, bạn có thể có một biểu đồ hiển thị luồng thông tin giữa các tác nhân. Điều này có thể giúp bạn xác định các nút thắt, sự không hiệu quả, và các vấn đề khác trong hệ thống.

- **Chỉ số hiệu suất**: Các chỉ số hiệu suất có thể giúp bạn theo dõi hiệu quả của hệ thống đa tác nhân. Ví dụ, bạn có thể theo dõi thời gian hoàn thành một nhiệm vụ, số lượng nhiệm vụ hoàn thành trong một đơn vị thời gian, và độ chính xác của các đề xuất được thực hiện bởi các tác nhân. Thông tin này có thể giúp bạn xác định các khu vực cần cải thiện và tối ưu hóa hệ thống.

## Mẫu đa tác nhân

Hãy đi sâu vào một số mẫu cụ thể mà chúng ta có thể sử dụng để tạo ứng dụng đa tác nhân. Dưới đây là một số mẫu thú vị đáng xem xét:

### Trò chuyện nhóm

Mẫu này hữu ích khi bạn muốn tạo một ứng dụng trò chuyện nhóm nơi nhiều tác nhân có thể giao tiếp với nhau. Các trường hợp sử dụng điển hình cho mẫu này bao gồm cộng tác nhóm, hỗ trợ khách hàng, và mạng xã hội.

Trong mẫu này, mỗi tác nhân đại diện cho một người dùng trong trò chuyện nhóm, và các tin nhắn được trao đổi giữa các tác nhân bằng một giao thức nhắn tin. Các tác nhân có thể gửi tin nhắn đến trò chuyện nhóm, nhận tin nhắn từ trò chuyện nhóm, và trả lời tin nhắn từ các tác nhân khác.

Mẫu này có thể được triển khai bằng cách sử dụng kiến trúc tập trung nơi tất cả các tin nhắn được định tuyến qua một máy chủ trung tâm, hoặc kiến trúc phi tập trung nơi các tin nhắn được trao đổi trực tiếp.

![Trò chuyện nhóm](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.vi.png)

### Chuyển giao

Mẫu này hữu ích khi bạn muốn tạo một ứng dụng nơi nhiều tác nhân có thể chuyển giao nhiệm vụ cho nhau.

Các trường hợp sử dụng điển hình cho mẫu này bao gồm hỗ trợ khách hàng, quản lý nhiệm vụ, và tự động hóa quy trình làm việc.

Trong mẫu này, mỗi tác nhân đại diện cho một nhiệm vụ hoặc một bước trong quy trình làm việc, và các tác nhân có thể chuyển giao nhiệm vụ cho các tác nhân khác dựa trên các quy tắc được định trước.

![Chuyển giao](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.vi.png)

### Lọc cộng tác

Mẫu này hữu ích khi bạn muốn tạo một ứng dụng nơi nhiều tác nhân có thể cộng tác để đưa ra các đề xuất cho người dùng.

Lý do bạn muốn nhiều tác nhân cộng tác là vì mỗi tác nhân có thể có chuyên môn khác nhau và có thể đóng góp vào quá trình đưa ra đề xuất theo những cách khác nhau.

Hãy lấy một ví dụ nơi một người dùng muốn có đề xuất về cổ phiếu tốt nhất để mua trên thị trường chứng khoán.

- **Chuyên gia ngành**: Một tác nhân có thể là chuyên gia trong một ngành cụ thể.
- **Phân tích kỹ thuật**: Một tác nhân khác có thể là chuyên gia trong phân tích kỹ thuật.
- **Phân tích cơ bản**: Và một tác nhân khác có thể là chuyên gia trong phân tích cơ bản. Bằng cách cộng tác, các tác nhân này có thể cung cấp một đề xuất toàn diện hơn cho người dùng.

![Đề xuất](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.vi.png)

## Tình huống: Quy trình hoàn tiền

Hãy xem xét một tình huống nơi một khách hàng đang cố gắng nhận hoàn tiền cho một sản phẩm, có thể có khá nhiều tác nhân tham gia vào quy trình này nhưng hãy chia nó thành các tác nhân cụ thể cho quy trình này và các tác nhân chung có thể được sử dụng trong các quy trình khác.

**Các tác nhân cụ thể cho quy trình hoàn tiền**:

Dưới đây là một số tác nhân có thể tham gia vào quy trình hoàn tiền:

- **Tác nhân khách hàng**: Tác nhân này đại diện cho khách hàng và chịu trách nhiệm khởi tạo quy trình hoàn tiền.
- **Tác nhân người bán**: Tác nhân này đại diện cho người bán và chịu trách nhiệm xử lý hoàn tiền.
- **Tác nhân thanh toán**: Tác nhân này đại diện cho quy trình thanh toán và chịu trách nhiệm hoàn tiền cho khách hàng.
- **Tác nhân giải quyết**: Tác nhân này đại diện cho quy trình giải quyết và chịu trách nhiệm giải quyết bất kỳ vấn đề nào phát sinh trong quy trình hoàn tiền.
- **Tác nhân tuân thủ**: Tác nhân này đại diện cho quy trình tuân thủ và chịu trách nhiệm đảm bảo rằng quy trình hoàn tiền tuân thủ các quy định và chính sách.

**Các tác nhân chung**:

Các tác nhân này có thể được sử dụng bởi các phần khác của doanh nghiệp của bạn.

- **Tác nhân vận chuyển**: Tác nhân này đại diện cho quy trình vận chuyển và chịu trách nhiệm vận chuyển sản phẩm trở lại cho người bán. Tác nhân này có thể được sử dụng cả trong quy trình hoàn tiền và trong vận chuyển sản phẩm nói chung, ví dụ như khi mua hàng.
- **Tác nhân phản hồi**: Tác nhân này đại diện cho quy trình phản hồi và chịu trách nhiệm thu thập phản hồi từ khách hàng. Phản hồi có thể được thu thập bất kỳ lúc nào, không chỉ trong quy trình hoàn tiền.
- **Tác nhân leo thang**: Tác nhân này đại diện cho quy trình leo thang và chịu trách nhiệm đưa vấn đề lên cấp hỗ trợ cao hơn. Bạn có thể sử dụng loại tác nhân này cho bất kỳ quy trình nào cần leo thang vấn đề.
- **Tác nhân thông báo**: Tác nhân này đại diện cho quy trình thông báo và chịu trách nhiệm gửi thông báo cho khách hàng ở các giai đoạn khác nhau của quy trình hoàn tiền.
- **Tác nhân phân tích**: Tác nhân này đại diện cho quy trình phân tích và chịu trách nhiệm phân tích dữ liệu liên quan đến quy trình hoàn tiền.
- **Tác nhân kiểm toán**: Tác nhân này đại diện cho quy trình kiểm toán và chịu trách nhiệm kiểm tra quy trình hoàn tiền để đảm bảo rằng nó được thực hiện đúng cách.
- **Tác nhân báo cáo**: Tác nhân này đại diện cho quy trình báo cáo và chịu trách nhiệm tạo báo cáo về quy trình hoàn tiền.
- **Tác nhân kiến thức**: Tác nhân này đại diện cho quy trình kiến thức và chịu trách nhiệm duy trì cơ sở kiến thức về thông tin liên quan đến quy trình hoàn tiền. Tác nhân này có thể có kiến thức cả về hoàn tiền và các phần khác của doanh nghiệp của bạn.
- **Tác nhân bảo mật**: Tác nhân này đại diện cho quy trình bảo mật và chịu trách nhiệm đảm bảo an ninh cho quy trình hoàn tiền.
- **Tác nhân chất lượng**: Tác nhân này đại diện cho quy trình chất lượng và chịu trách nhiệm đảm bảo chất lượng của quy trình hoàn tiền.

Có khá nhiều tác nhân được liệt kê ở trên, cả cho quy trình hoàn tiền cụ thể và cho các tác nhân chung có thể được sử dụng trong các phần khác của doanh nghiệp của bạn. Hy vọng điều này giúp bạn có ý tưởng về cách bạn có thể quyết định các tác nhân nào sẽ sử dụng trong hệ thống đa tác nhân của mình.

## Bài tập
Thiết kế một hệ thống đa tác nhân cho quy trình hỗ trợ khách hàng. Xác định các tác nhân tham gia vào quy trình, vai trò và trách nhiệm của họ, cũng như cách họ tương tác với nhau. Cân nhắc cả các tác nhân cụ thể cho quy trình hỗ trợ khách hàng và các tác nhân chung có thể được sử dụng trong các phần khác của doanh nghiệp.

> Hãy suy nghĩ trước khi đọc giải pháp dưới đây, bạn có thể cần nhiều tác nhân hơn bạn nghĩ.

> TIP: Hãy nghĩ về các giai đoạn khác nhau của quy trình hỗ trợ khách hàng và cũng cân nhắc các tác nhân cần thiết cho bất kỳ hệ thống nào.

## Giải pháp

[Giải pháp](./solution/solution.md)

## Kiểm tra kiến thức

Câu hỏi: Khi nào bạn nên cân nhắc sử dụng hệ thống đa tác nhân?

- [ ] A1: Khi bạn có khối lượng công việc nhỏ và nhiệm vụ đơn giản.
- [ ] A2: Khi bạn có khối lượng công việc lớn.
- [ ] A3: Khi bạn có một nhiệm vụ đơn giản.

[Giải pháp câu hỏi](./solution/solution-quiz.md)

## Tóm tắt

Trong bài học này, chúng ta đã tìm hiểu về mẫu thiết kế đa tác nhân, bao gồm các tình huống mà hệ thống đa tác nhân có thể áp dụng, những lợi ích của việc sử dụng hệ thống đa tác nhân so với một tác nhân đơn lẻ, các thành phần cơ bản để triển khai mẫu thiết kế đa tác nhân, và cách để có cái nhìn rõ ràng về cách các tác nhân tương tác với nhau.

### Có thêm câu hỏi về Mẫu Thiết Kế Đa Tác Nhân?

Tham gia [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ các học viên khác, tham dự giờ giải đáp thắc mắc và nhận câu trả lời cho các câu hỏi về AI Agents của bạn.

## Tài nguyên bổ sung

- 

## Bài học trước

[Thiết kế Kế hoạch](../07-planning-design/README.md)

## Bài học tiếp theo

[Siêu nhận thức trong AI Agents](../09-metacognition/README.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.