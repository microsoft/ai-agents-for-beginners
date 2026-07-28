# Tác nhân AI trong Sản xuất: Quan sát & Đánh giá

[![Tác nhân AI trong Sản xuất](../../../translated_images/vi/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Khi các tác nhân AI chuyển từ nguyên mẫu thử nghiệm sang các ứng dụng thực tế, khả năng hiểu hành vi của chúng, giám sát hiệu suất và đánh giá đầu ra theo hệ thống trở nên rất quan trọng.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách/hiểu:
- Các khái niệm cốt lõi về quan sát và đánh giá tác nhân
- Các kỹ thuật để cải thiện hiệu suất, chi phí và hiệu quả của các tác nhân
- Cái gì và làm thế nào để đánh giá tác nhân AI của bạn một cách hệ thống
- Cách kiểm soát chi phí khi triển khai tác nhân AI vào sản xuất
- Cách tích hợp công cụ đo lường vào các tác nhân được xây dựng bằng Microsoft Agent Framework

Mục tiêu là trang bị cho bạn kiến thức để biến các tác nhân "hộp đen" thành các hệ thống minh bạch, dễ quản lý và đáng tin cậy.

_**Lưu ý:** Việc triển khai các tác nhân AI an toàn và đáng tin cậy là rất quan trọng. Hãy tham khảo bài học [Xây dựng tác nhân AI đáng tin cậy](../06-building-trustworthy-agents/README.md) nhé._

## Traces và Spans

Các công cụ quan sát như [Langfuse](https://langfuse.com/) hoặc [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) thường biểu diễn các lần chạy của tác nhân dưới dạng traces và spans.

- **Trace** đại diện cho một nhiệm vụ tác nhân hoàn chỉnh từ đầu đến cuối (ví dụ như xử lý một truy vấn người dùng).
- **Spans** là các bước đơn lẻ trong trace (ví dụ gọi một mô hình ngôn ngữ hoặc truy xuất dữ liệu).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Không có quan sát, một tác nhân AI có thể giống như một "hộp đen" – trạng thái nội bộ và lý luận của nó không rõ ràng, khiến việc chẩn đoán lỗi hoặc tối ưu hiệu suất trở nên khó khăn. Với quan sát, các tác nhân trở thành "hộp kính," cung cấp sự minh bạch rất quan trọng để xây dựng sự tin tưởng và đảm bảo chúng hoạt động đúng như dự định.

## Tại sao Quan sát lại Quan trọng trong Môi trường Sản xuất

Chuyển các tác nhân AI sang môi trường sản xuất mang lại một bộ thách thức và yêu cầu mới. Quan sát không còn là "một điều tốt để có" mà là một năng lực thiết yếu:

*   **Gỡ lỗi và Phân tích nguyên nhân gốc rễ**: Khi một tác nhân thất bại hoặc tạo ra đầu ra không mong đợi, các công cụ quan sát cung cấp các traces cần thiết để xác định nguồn gốc lỗi. Điều này đặc biệt quan trọng với các tác nhân phức tạp có thể thực hiện nhiều lần gọi LLM, tương tác với công cụ và logic điều kiện.
*   **Quản lý độ trễ và chi phí**: Các tác nhân AI thường dựa vào các LLM và API bên ngoài được tính phí theo token hoặc mỗi lần gọi. Quan sát cho phép theo dõi chính xác các lần gọi này, giúp xác định các thao tác quá chậm hoặc tốn kém. Điều này giúp các nhóm tối ưu lời nhắc, chọn mô hình nhanh hơn hoặc thiết kế lại quy trình để kiểm soát chi phí vận hành và đảm bảo trải nghiệm người dùng tốt.
*   **Tin cậy, An toàn và Tuân thủ**: Trong nhiều ứng dụng, điều quan trọng là đảm bảo tác nhân hoạt động an toàn và đạo đức. Quan sát cung cấp một hồ sơ kiểm toán về các hành động và quyết định của tác nhân. Điều này có thể được dùng để phát hiện và giảm thiểu các vấn đề như tiêm nhiễm lời nhắc, tạo nội dung có hại hoặc xử lý sai thông tin cá nhân (PII). Ví dụ, bạn có thể xem lại các trace để hiểu lý do tại sao tác nhân trả lời một cách cụ thể hoặc sử dụng một công cụ nhất định.
*   **Vòng lặp Cải tiến Liên tục**: Dữ liệu quan sát là nền tảng của quy trình phát triển lặp đi lặp lại. Bằng cách giám sát hiệu suất tác nhân trong thực tế, các nhóm có thể xác định điểm cần cải thiện, thu thập dữ liệu để tinh chỉnh mô hình và xác nhận ảnh hưởng của các thay đổi. Điều này tạo ra vòng phản hồi trong đó các hiểu biết từ đánh giá trực tuyến trong sản xuất giúp làm giàu cho các thí nghiệm và tinh chỉnh ngoại tuyến, dẫn đến hiệu suất tác nhân ngày càng tốt hơn.

## Các chỉ số chính cần theo dõi

Để giám sát và hiểu hành vi của tác nhân, cần theo dõi nhiều chỉ số và tín hiệu. Mặc dù các chỉ số cụ thể có thể khác nhau tùy thuộc vào mục đích của tác nhân, nhưng một số chỉ số là quan trọng và phổ quát.

Dưới đây là một số chỉ số phổ biến nhất mà các công cụ quan sát thường theo dõi:

**Độ trễ:** Tác nhân phản hồi nhanh như thế nào? Thời gian chờ dài ảnh hưởng tiêu cực đến trải nghiệm người dùng. Bạn nên đo độ trễ cho các nhiệm vụ và các bước riêng lẻ bằng cách theo dõi trace của các lần chạy tác nhân. Ví dụ, một tác nhân mất 20 giây cho tất cả các lần gọi mô hình có thể được tăng tốc bằng cách sử dụng mô hình nhanh hơn hoặc chạy các lần gọi song song.

**Chi phí:** Chi phí cho mỗi lần chạy tác nhân là bao nhiêu? Các tác nhân AI dựa vào các lần gọi LLM được tính phí theo token hoặc API bên ngoài. Việc dùng công cụ nhiều lần hoặc nhiều lời nhắc có thể nhanh chóng làm tăng chi phí. Ví dụ, nếu một tác nhân gọi một LLM năm lần để cải thiện chất lượng chút ít, bạn cần đánh giá xem chi phí có hợp lý hay nên giảm số lần gọi hoặc dùng mô hình rẻ hơn. Giám sát thời gian thực cũng giúp phát hiện các đột biến bất thường (ví dụ lỗi gây vòng lặp API quá mức).

**Lỗi yêu cầu:** Có bao nhiêu yêu cầu bị tác nhân thất bại? Đây có thể là lỗi API hoặc gọi công cụ không thành công. Để làm cho tác nhân mạnh mẽ hơn trước các lỗi này khi triển khai, bạn có thể thiết lập các phương án dự phòng hoặc thử lại. Ví dụ, nếu nhà cung cấp LLM A bị ngưng dịch vụ, bạn chuyển sang nhà cung cấp B làm dự phòng.

**Phản hồi người dùng:** Việc sử dụng đánh giá trực tiếp từ người dùng cung cấp các thông tin quý giá. Điều này có thể bao gồm đánh giá rõ ràng (👍cảm giác tốt/👎xấu, ⭐1-5 sao) hoặc bình luận văn bản. Phản hồi tiêu cực nhiều lần nên cảnh báo bạn vì đó là dấu hiệu tác nhân không hoạt động như mong đợi.

**Phản hồi người dùng ngầm định:** Hành vi người dùng cũng cung cấp phản hồi gián tiếp kể cả khi không có đánh giá rõ ràng. Chẳng hạn như việc người dùng ngay lập tức thay đổi câu hỏi, hỏi lại nhiều lần hoặc nhấn nút thử lại. Ví dụ, nếu bạn thấy người dùng liên tục hỏi cùng một câu, đó là dấu hiệu tác nhân không hoạt động đúng.

**Độ chính xác:** Tác nhân tạo ra kết quả đúng hoặc mong muốn với tần suất bao nhiêu? Định nghĩa độ chính xác có thể khác nhau (ví dụ, độ chính xác giải quyết vấn đề, độ chính xác tìm kiếm thông tin, sự hài lòng của người dùng). Bước đầu tiên là xác định thành công nghĩa là gì với tác nhân của bạn. Bạn có thể theo dõi độ chính xác qua kiểm tra tự động, điểm đánh giá hoặc nhãn hoàn thành nhiệm vụ. Ví dụ, đánh dấu trace là “thành công” hoặc “thất bại”.

**Chỉ số đánh giá tự động:** Bạn cũng có thể thiết lập đánh giá tự động. Ví dụ, dùng một LLM để chấm điểm đầu ra của tác nhân rằng nó có hữu ích, chính xác hay không. Có nhiều thư viện mã nguồn mở giúp bạn chấm điểm các khía cạnh khác nhau của tác nhân. Ví dụ [RAGAS](https://docs.ragas.io/) cho tác nhân RAG hoặc [LLM Guard](https://llm-guard.com/) để phát hiện ngôn ngữ có hại hoặc tiêm nhiễm lời nhắc.

Trong thực tế, sự kết hợp các chỉ số này cung cấp cái nhìn tổng thể tốt nhất về sức khỏe của một tác nhân AI. Trong [tập notebook ví dụ](./code_samples/10-expense_claim-demo.ipynb) của chương này, chúng tôi sẽ cho bạn thấy các chỉ số này trông ra sao trong các ví dụ thực tế nhưng trước hết, chúng ta sẽ học quy trình đánh giá điển hình như thế nào.

## Tích hợp công cụ đo lường vào tác nhân của bạn

Để thu thập dữ liệu trace, bạn cần tích hợp công cụ đo lường vào mã của mình. Mục tiêu là tích hợp mã tác nhân để phát ra các trace và chỉ số có thể được một nền tảng quan sát thu thập, xử lý và trực quan hóa.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) đã trở thành tiêu chuẩn ngành cho quan sát các LLM. Nó cung cấp bộ API, SDK và công cụ để tạo, thu thập và xuất dữ liệu telemety.

Có nhiều thư viện hỗ trợ tích hợp sẵn bọc quanh các framework tác nhân hiện có, giúp xuất spans OpenTelemetry dễ dàng đến công cụ quan sát. Microsoft Agent Framework tích hợp OpenTelemetry một cách gốc. Dưới đây là ví dụ về việc tích hợp một tác nhân MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Việc thực thi tác nhân được theo dõi tự động
    pass
```

Tập [notebook ví dụ](./code_samples/10-expense_claim-demo.ipynb) trong chương này sẽ hướng dẫn bạn cách tích hợp với tác nhân MAF.

**Tạo Span thủ công:** Mặc dù các thư viện tích hợp cung cấp nền tảng tốt, nhưng thường có các trường hợp bạn cần thông tin chi tiết hoặc tùy chỉnh hơn. Bạn có thể tạo các span thủ công để thêm logic ứng dụng riêng. Quan trọng hơn, bạn có thể làm giàu các span tạo tự động hoặc thủ công với các thuộc tính tùy chỉnh (còn gọi là tags hoặc metadata). Những thuộc tính này có thể là dữ liệu kinh doanh cụ thể, tính toán trung gian hoặc bất kỳ ngữ cảnh nào hữu ích cho việc gỡ lỗi và phân tích, như `user_id`, `session_id` hoặc `model_version`.

Ví dụ tạo trace và span thủ công với [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Đánh giá tác nhân

Quan sát cung cấp cho ta các chỉ số, nhưng đánh giá là quá trình phân tích dữ liệu đó (và thực hiện các kiểm tra) để xác định mức độ tác nhân AI hoạt động hiệu quả và cách nó có thể được cải thiện. Nói cách khác, khi bạn đã có những trace và chỉ số đó, làm thế nào bạn sử dụng chúng để đánh giá tác nhân và đưa ra quyết định?

Việc đánh giá thường xuyên rất quan trọng bởi vì các tác nhân AI thường không quyết định được chắc chắn mỗi lần và có thể phát triển (qua cập nhật hoặc thay đổi hành vi mô hình) – nếu không đánh giá, bạn sẽ không biết tác nhân “thông minh” của mình thực sự làm tốt công việc hay đã sa sút.

Có hai loại đánh giá cho tác nhân AI: **đánh giá trực tuyến** và **đánh giá ngoại tuyến**. Cả hai đều có giá trị và bổ trợ cho nhau. Chúng ta thường bắt đầu với đánh giá ngoại tuyến vì đó là bước tối thiểu cần thiết trước khi triển khai một tác nhân.

### Đánh giá ngoại tuyến

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Điều này bao gồm việc đánh giá tác nhân trong môi trường kiểm soát, thường sử dụng bộ dữ liệu kiểm thử, không phải là truy vấn người dùng trực tiếp. Bạn sử dụng các bộ dữ liệu đã được chọn lọc, trong đó bạn biết trước đầu ra hoặc hành vi đúng, rồi chạy tác nhân trên các bộ này.

Ví dụ, nếu bạn xây dựng một tác nhân giải bài toán văn bản toán học, bạn có thể có một [bộ dữ liệu kiểm thử](https://huggingface.co/datasets/gsm8k) gồm 100 bài toán với câu trả lời đã biết. Đánh giá ngoại tuyến thường được thực hiện trong quá trình phát triển (và có thể là một phần của các pipeline CI/CD) để kiểm tra sự tiến bộ hoặc ngăn ngừa sự thoái trào. Lợi ích là nó **có thể lặp lại và bạn có được các chỉ số độ chính xác rõ ràng vì bạn có mặt thật**. Bạn cũng có thể mô phỏng truy vấn người dùng và đo lường phản hồi của tác nhân với câu trả lời lý tưởng hoặc sử dụng chỉ số tự động như đã mô tả ở trên.

Thách thức chính với đánh giá ngoại tuyến là đảm bảo bộ dữ liệu kiểm thử đầy đủ và luôn cập nhật – tác nhân có thể hoạt động tốt trên bộ kiểm thử cố định nhưng gặp các truy vấn rất khác trong sản xuất. Do đó, bạn nên cập nhật bộ kiểm thử với các trường hợp cạnh và ví dụ mới phản ánh kịch bản thực tế. Một sự kết hợp giữa các bộ kiểm thử nhỏ “kiểm tra nhanh” và các bộ lớn hơn để đo lường hiệu suất rộng hơn là hữu ích: bộ nhỏ để kiểm tra nhanh và bộ lớn để đánh giá hiệu suất tổng thể.

### Đánh giá trực tuyến

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Điều này đề cập đến việc đánh giá tác nhân trong môi trường thực tế, tức là trong quá trình sử dụng trực tiếp ở sản xuất. Đánh giá trực tuyến liên quan đến việc giám sát hiệu suất tác nhân trong các tương tác thực tế với người dùng và phân tích liên tục các kết quả.

Ví dụ, bạn có thể theo dõi tỷ lệ thành công, điểm hài lòng của người dùng hoặc các chỉ số khác trên lưu lượng trực tiếp. Ưu điểm của đánh giá trực tuyến là nó **bắt được những điều bạn có thể không dự đoán được trong môi trường phòng lab** – bạn có thể quan sát sự dịch chuyển mô hình qua thời gian (nếu hiệu quả tác nhân giảm khi mẫu đầu vào thay đổi) và phát hiện các truy vấn hoặc tình huống bất ngờ không có trong dữ liệu kiểm thử. Nó cung cấp cái nhìn chân thực về cách tác nhân hành xử trong môi trường thực tế.

Đánh giá trực tuyến thường bao gồm thu thập phản hồi người dùng ngầm định và rõ ràng như đã thảo luận, và có thể chạy các bài kiểm tra shadow hoặc A/B (nơi phiên bản mới của tác nhân chạy song song để so sánh với phiên bản cũ). Thách thức là có thể khó được nhãn hoặc điểm số đáng tin cậy cho các tương tác trực tiếp – bạn có thể sẽ dựa vào phản hồi người dùng hoặc chỉ số hạ nguồn (ví dụ người dùng có nhấn vào kết quả không).

### Kết hợp cả hai

Đánh giá trực tuyến và ngoại tuyến không loại trừ nhau; chúng rất bổ trợ. Các hiểu biết từ giám sát trực tuyến (ví dụ loại truy vấn người dùng mới nơi tác nhân hoạt động kém) có thể dùng để làm phong phú và cải thiện bộ dữ liệu kiểm thử ngoại tuyến. Ngược lại, các tác nhân hoạt động tốt trong kiểm thử ngoại tuyến có thể được triển khai với sự tự tin cao hơn và giám sát trực tuyến.

Thực tế, nhiều nhóm áp dụng một vòng lặp:

_đánh giá ngoại tuyến -> triển khai -> giám sát trực tuyến -> thu thập các trường hợp lỗi mới -> thêm vào bộ kiểm thử ngoại tuyến -> tinh chỉnh tác nhân -> lặp lại_.

## Các vấn đề phổ biến

Khi triển khai tác nhân AI vào sản xuất, bạn có thể gặp nhiều thách thức. Dưới đây là một số vấn đề phổ biến và giải pháp tiềm năng:

| **Vấn đề**    | **Giải pháp tiềm năng**   |
| ------------- | ------------------ |
| Tác nhân AI không thực hiện nhiệm vụ đều đặn | - Tinh chỉnh lời nhắc cho tác nhân AI; rõ ràng về mục tiêu.<br>- Xác định điểm có thể chia nhiệm vụ thành các nhiệm vụ nhỏ hơn và xử lý bằng nhiều tác nhân. |
| Tác nhân AI bị lặp vòng liên tục  | - Đảm bảo bạn có các điều kiện dừng rõ ràng để tác nhân biết khi nào dừng quá trình.<br>- Với các nhiệm vụ phức tạp yêu cầu suy luận và lập kế hoạch, hãy dùng mô hình lớn hơn chuyên biệt cho nhiệm vụ suy luận. |
| Lời gọi công cụ của tác nhân AI không hoạt động tốt   | - Thử nghiệm và xác nhận đầu ra của công cụ ngoài hệ thống tác nhân.<br>- Tinh chỉnh tham số đã định nghĩa, lời nhắc và tên gọi công cụ.  |
| Hệ thống đa tác nhân không hoạt động nhất quán | - Tinh chỉnh lời nhắc cho mỗi tác nhân để đảm bảo chúng cụ thể và khác biệt nhau.<br>- Xây dựng hệ thống phân cấp sử dụng tác nhân "điều phối" hoặc điều khiển để xác định tác nhân phù hợp. |

Nhiều trong số những vấn đề này có thể được phát hiện hiệu quả hơn với quan sát. Các trace và chỉ số chúng ta đã thảo luận giúp xác định chính xác vị trí xảy ra sự cố trong quy trình của tác nhân, làm cho việc gỡ lỗi và tối ưu dễ dàng hơn rất nhiều.

## Quản lý Chi phí


Dưới đây là một số chiến lược để quản lý chi phí triển khai các tác nhân AI vào sản xuất:

**Sử dụng Mô hình Nhỏ hơn:** Các Mô hình Ngôn ngữ Nhỏ (SLMs) có thể hoạt động tốt trong một số trường hợp sử dụng tác nhân và sẽ giảm đáng kể chi phí. Như đã đề cập trước đó, xây dựng một hệ thống đánh giá để xác định và so sánh hiệu suất với các mô hình lớn hơn là cách tốt nhất để hiểu SLM sẽ hoạt động tốt như thế nào trong trường hợp sử dụng của bạn. Hãy cân nhắc sử dụng SLM cho các tác vụ đơn giản như phân loại ý định hoặc trích xuất tham số, trong khi để dành các mô hình lớn hơn cho việc suy luận phức tạp.

**Sử dụng Mô hình Bộ định tuyến:** Một chiến lược tương tự là sử dụng đa dạng các mô hình và kích cỡ. Bạn có thể sử dụng một LLM/SLM hoặc hàm serverless để định tuyến các yêu cầu dựa trên độ phức tạp tới các mô hình phù hợp nhất. Điều này cũng sẽ giúp giảm chi phí đồng thời đảm bảo hiệu suất cho các tác vụ phù hợp. Ví dụ, định tuyến các truy vấn đơn giản tới các mô hình nhỏ hơn, nhanh hơn, và chỉ sử dụng các mô hình lớn, đắt tiền cho các tác vụ suy luận phức tạp.

**Bộ nhớ đệm Phản hồi:** Xác định các yêu cầu và tác vụ phổ biến và cung cấp phản hồi trước khi chúng đi qua hệ thống tác nhân của bạn là một cách tốt để giảm khối lượng các yêu cầu tương tự. Bạn thậm chí có thể thiết lập một quy trình để xác định mức độ tương đồng của một yêu cầu với các yêu cầu được lưu trong bộ nhớ đệm bằng cách sử dụng các mô hình AI cơ bản hơn. Chiến lược này có thể giảm đáng kể chi phí cho các câu hỏi thường gặp hoặc các quy trình làm việc phổ biến.

## Hãy xem cách điều này hoạt động trong thực tế

Trong [sổ tay ví dụ của phần này](./code_samples/10-expense_claim-demo.ipynb), chúng ta sẽ thấy các ví dụ về cách sử dụng các công cụ quan sát để theo dõi và đánh giá tác nhân của mình.


### Có Thêm Câu hỏi về Tác nhân AI trong Sản xuất?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ những người học khác, tham dự giờ làm việc và nhận câu trả lời cho các câu hỏi về Tác nhân AI của bạn.

## Bài Học Trước

[Mẫu Thiết Kế Siêu Nhận Thức](../09-metacognition/README.md)

## Bài Học Tiếp Theo

[Giao Thức Tác nhân](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->