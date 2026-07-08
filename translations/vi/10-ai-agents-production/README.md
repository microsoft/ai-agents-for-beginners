# Đại lý AI trong Sản xuất: Khả năng quan sát & Đánh giá

[![AI Agents in Production](../../../translated_images/vi/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Khi các đại lý AI chuyển từ nguyên mẫu thử nghiệm sang các ứng dụng thực tế, khả năng hiểu hành vi, giám sát hiệu suất và đánh giá hệ thống kết quả của chúng trở nên quan trọng.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách/hiểu:
- Các khái niệm cốt lõi về khả năng quan sát và đánh giá đại lý
- Các kỹ thuật cải thiện hiệu suất, chi phí và hiệu quả của đại lý
- Cái gì và cách hệ thống đánh giá đại lý AI của bạn
- Cách kiểm soát chi phí khi triển khai đại lý AI vào sản xuất
- Cách đo lường đại lý xây dựng bằng Microsoft Agent Framework

Mục tiêu là trang bị cho bạn kiến thức để chuyển đổi các đại lý "hộp đen" thành hệ thống minh bạch, dễ quản lý và đáng tin cậy.

_**Lưu ý:** Điều quan trọng là triển khai các Đại lý AI an toàn và đáng tin cậy. Hãy xem thêm bài học [Xây dựng Đại lý AI Đáng Tin cậy](../06-building-trustworthy-agents/README.md)._

## Traces và Spans

Công cụ khả năng quan sát như [Langfuse](https://langfuse.com/) hoặc [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) thường biểu diễn các phiên chạy đại lý dưới dạng traces và spans.

- **Trace** biểu diễn một tác vụ hoàn chỉnh của đại lý từ đầu đến cuối (như xử lý truy vấn người dùng).
- **Spans** là các bước riêng lẻ trong trace (như gọi mô hình ngôn ngữ hoặc truy xuất dữ liệu).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Nếu không có khả năng quan sát, đại lý AI có thể giống như một "hộp đen" - trạng thái nội bộ và suy luận không rõ ràng, khiến việc chẩn đoán sự cố hoặc tối ưu hiệu suất trở nên khó khăn. Với khả năng quan sát, các đại lý trở thành "hộp kính," cung cấp sự minh bạch thiết yếu cho việc xây dựng niềm tin và đảm bảo chúng hoạt động như mong đợi.

## Tại sao Khả năng Quan sát Quan trọng trong Môi trường Sản xuất

Việc chuyển các đại lý AI sang môi trường sản xuất đặt ra một loạt thách thức và yêu cầu mới. Khả năng quan sát không còn là "điều tốt nên có" mà là một năng lực quan trọng:

*   **Gỡ lỗi và Phân tích nguyên nhân gốc rễ**: Khi đại lý gặp lỗi hoặc tạo ra kết quả không mong muốn, công cụ khả năng quan sát cung cấp các traces cần thiết để xác định nguồn gốc lỗi. Điều này đặc biệt quan trọng trong các đại lý phức tạp có thể liên quan đến nhiều lần gọi LLM, tương tác công cụ và logic điều kiện.
*   **Quản lý Độ trễ và Chi phí**: Các đại lý AI thường dựa vào LLM và các API bên ngoài được tính phí theo token hoặc theo lần gọi. Khả năng quan sát cho phép theo dõi chính xác các lần gọi này, giúp xác định các thao tác quá chậm hoặc đắt tiền. Điều này cho phép nhóm tối ưu prompt, chọn mô hình hiệu quả hơn hoặc thiết kế lại quy trình để quản lý chi phí vận hành và đảm bảo trải nghiệm người dùng tốt.
*   **Niềm tin, An toàn và Tuân thủ**: Trong nhiều ứng dụng, điều quan trọng là đảm bảo đại lý hành xử an toàn và đạo đức. Khả năng quan sát cung cấp dấu vết kiểm toán các hành động và quyết định của đại lý. Điều này có thể được sử dụng để phát hiện và giảm thiểu các vấn đề như chèn prompt, tạo nội dung độc hại hoặc xử lý sai thông tin nhận dạng cá nhân (PII). Ví dụ, bạn có thể xem lại traces để hiểu tại sao đại lý đưa ra phản hồi nhất định hoặc sử dụng công cụ cụ thể.
*   **Vòng lặp Cải tiến Liên tục**: Dữ liệu khả năng quan sát là nền tảng của quá trình phát triển lặp đi lặp lại. Bằng cách giám sát hiệu suất đại lý trong thực tế, nhóm có thể xác định các điểm cần cải tiến, thu thập dữ liệu để điều chỉnh mô hình và xác nhận tác động của các thay đổi. Điều này tạo nên vòng phản hồi, trong đó các hiểu biết sản xuất từ đánh giá trực tuyến giúp hướng dẫn thử nghiệm và tinh chỉnh ngoại tuyến, dẫn đến hiệu suất đại lý ngày càng tốt hơn.

## Các Chỉ số Chính cần Theo dõi

Để giám sát và hiểu hành vi đại lý, cần theo dõi một loạt các chỉ số và tín hiệu. Mặc dù các chỉ số cụ thể có thể khác nhau tùy theo mục đích đại lý, một số chỉ số là quan trọng chung.

Dưới đây là một số chỉ số phổ biến nhất mà các công cụ khả năng quan sát theo dõi:

**Độ trễ:** Đại lý phản hồi nhanh như thế nào? Thời gian chờ lâu ảnh hưởng tiêu cực đến trải nghiệm người dùng. Bạn nên đo độ trễ cho các tác vụ và các bước riêng lẻ bằng cách theo dõi các phiên chạy đại lý. Ví dụ, một đại lý mất 20 giây cho tất cả gọi mô hình có thể được tăng tốc bằng cách dùng mô hình nhanh hơn hoặc chạy các lần gọi mô hình song song.

**Chi phí:** Chi phí cho mỗi phiên chạy đại lý là bao nhiêu? Đại lý AI dựa vào các lệnh gọi LLM được tính phí theo token hoặc API bên ngoài. Sử dụng dụng cụ thường xuyên hoặc nhiều prompt có thể nhanh chóng tăng chi phí. Ví dụ, nếu đại lý gọi LLM năm lần để cải thiện chất lượng nhỏ, bạn phải đánh giá xem chi phí có hợp lý không hoặc có thể giảm số lần gọi hoặc chọn mô hình rẻ hơn. Giám sát theo thời gian thực cũng giúp phát hiện các đột biến không mong muốn (ví dụ: lỗi gây vòng lặp API quá mức).

**Lỗi yêu cầu:** Có bao nhiêu yêu cầu đại lý bị lỗi? Điều này có thể bao gồm lỗi API hoặc gọi công cụ thất bại. Để làm cho đại lý của bạn bền bỉ hơn trong sản xuất, bạn có thể thiết lập các dự phòng hoặc thử lại. Ví dụ, nếu nhà cung cấp LLM A bị lỗi, bạn chuyển sang nhà cung cấp LLM B làm dự phòng.

**Phản hồi người dùng:** Thực hiện đánh giá người dùng trực tiếp cung cấp những hiểu biết quý giá. Điều này có thể bao gồm đánh giá rõ ràng (👍 thích/👎 không thích, ⭐1-5 sao) hoặc nhận xét bằng văn bản. Phản hồi tiêu cực liên tục nên cảnh báo bạn vì đó là dấu hiệu đại lý không hoạt động như mong đợi.

**Phản hồi người dùng ngầm định:** Hành vi người dùng cung cấp phản hồi gián tiếp ngay cả khi không có đánh giá rõ ràng. Điều này có thể bao gồm việc diễn giải lại câu hỏi ngay lập tức, truy vấn lặp lại hoặc nhấn nút thử lại. Ví dụ, nếu bạn thấy người dùng liên tục hỏi cùng một câu hỏi, đây là dấu hiệu đại lý không hoạt động như mong đợi.

**Độ chính xác:** Đại lý bao lâu tạo ra kết quả đúng hoặc mong muốn? Định nghĩa độ chính xác khác nhau (ví dụ, đúng đắn trong giải quyết bài toán, chính xác trong truy xuất thông tin, sự hài lòng của người dùng). Bước đầu tiên là định nghĩa thành công như thế nào với đại lý của bạn. Bạn có thể theo dõi độ chính xác qua các kiểm tra tự động, điểm đánh giá hoặc nhãn hoàn thành tác vụ. Ví dụ, đánh dấu traces là "thành công" hoặc "thất bại".

**Chỉ số đánh giá tự động:** Bạn cũng có thể thiết lập các đánh giá tự động. Ví dụ có thể dùng LLM để chấm điểm đầu ra của đại lý xem nó có hữu ích, chính xác hay không. Cũng có nhiều thư viện mã nguồn mở giúp bạn chấm điểm các khía cạnh khác nhau của đại lý. Ví dụ [RAGAS](https://docs.ragas.io/) cho đại lý RAG hoặc [LLM Guard](https://llm-guard.com/) để phát hiện ngôn ngữ độc hại hoặc chèn prompt.

Trong thực tế, kết hợp các chỉ số này sẽ cung cấp cái nhìn toàn diện về tình trạng đại lý AI. Trong [notebook ví dụ](./code_samples/10-expense_claim-demo.ipynb) của chương này, chúng tôi sẽ cho bạn thấy các chỉ số này trong ví dụ thực, nhưng trước tiên hãy học cách quy trình đánh giá điển hình trông như thế nào.

## Đo lường đại lý của bạn

Để thu thập dữ liệu trace, bạn cần đo lường mã của mình. Mục tiêu là đo lường mã đại lý để phát sinh traces và chỉ số có thể được thu thập, xử lý và trực quan hóa bởi nền tảng khả năng quan sát.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) đã trở thành chuẩn công nghiệp cho khả năng quan sát LLM. Nó cung cấp bộ API, SDK và công cụ để tạo, thu thập và xuất dữ liệu telemetry.

Có nhiều thư viện đo lường bao gồm khung đại lý hiện có và giúp dễ dàng xuất spans OpenTelemetry đến công cụ khả năng quan sát. Microsoft Agent Framework tích hợp sẵn với OpenTelemetry. Dưới đây là ví dụ về đo lường một đại lý MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Việc thực thi đại lý được theo dõi tự động
    pass
```

[notebook ví dụ](./code_samples/10-expense_claim-demo.ipynb) trong chương này sẽ hướng dẫn bạn cách đo lường đại lý MAF của bạn.

**Tạo Span thủ công:** Mặc dù thư viện đo lường cung cấp điểm khởi đầu tốt, thường có các trường hợp cần thông tin chi tiết hoặc tùy chỉnh hơn. Bạn có thể tạo spans thủ công để thêm logic ứng dụng tùy chỉnh. Quan trọng hơn, bạn có thể làm giàu spans tạo tự động hoặc thủ công với các thuộc tính tùy chỉnh (còn gọi là nhãn hoặc siêu dữ liệu). Các thuộc tính này có thể bao gồm dữ liệu đặc thù ngành, tính toán trung gian hoặc ngữ cảnh hữu ích cho gỡ lỗi hoặc phân tích, ví dụ như `user_id`, `session_id` hoặc `model_version`.

Ví dụ tạo traces và spans thủ công với [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Đánh giá đại lý

Khả năng quan sát cung cấp số liệu, nhưng đánh giá là quá trình phân tích dữ liệu đó (và thực hiện các bài kiểm tra) để xác định đại lý AI hoạt động tốt thế nào và cách cải thiện. Nói cách khác, khi bạn có các traces và số liệu đó, làm sao bạn sử dụng để đánh giá đại lý và đưa ra quyết định?

Đánh giá thường xuyên quan trọng vì các đại lý AI thường không xác định được chính xác và có thể tiến hóa (qua cập nhật hoặc thay đổi hành vi mô hình) – nếu không đánh giá, bạn sẽ không biết “đại lý thông minh” của bạn có thực hiện tốt công việc không hay đã suy giảm.

Có hai loại đánh giá cho đại lý AI: **đánh giá trực tuyến** và **đánh giá ngoại tuyến**. Cả hai đều có giá trị và bổ sung cho nhau. Chúng ta thường bắt đầu với đánh giá ngoại tuyến, vì đây là bước cần thiết tối thiểu trước khi triển khai đại lý.

### Đánh giá Ngoại tuyến

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Điều này liên quan đến đánh giá đại lý trong môi trường kiểm soát, thường sử dụng bộ dữ liệu thử nghiệm, không phải truy vấn người dùng trực tiếp. Bạn dùng bộ dữ liệu được lựa chọn kỹ nơi bạn biết đầu ra mong đợi hoặc hành vi đúng, rồi chạy đại lý trên đó.

Ví dụ, nếu bạn xây dựng một đại lý giải toán, bạn có thể sử dụng [bộ dữ liệu thử nghiệm](https://huggingface.co/datasets/gsm8k) gồm 100 bài toán với đáp án đã biết. Đánh giá ngoại tuyến thường được thực hiện trong phát triển (và có thể là một phần của các pipeline CI/CD) để kiểm tra cải tiến hoặc tránh suy giảm. Ưu điểm là nó **có thể lặp lại và bạn có số liệu độ chính xác rõ ràng vì bạn có sự thật nền**. Bạn cũng có thể mô phỏng truy vấn người dùng và so sánh phản hồi đại lý với câu trả lời lý tưởng hoặc sử dụng các chỉ số tự động như đã mô tả ở trên.

Thách thức lớn với đánh giá ngoại tuyến là đảm bảo bộ dữ liệu thử nghiệm toàn diện và luôn phù hợp – đại lý có thể hoạt động tốt trên bộ thử cố định nhưng gặp các truy vấn rất khác trong sản xuất. Vì vậy, bạn nên cập nhật bộ thử với các trường hợp biên mới và ví dụ phản ánh bối cảnh thực tế. Một hỗn hợp bộ test nhỏ "kiểm tra nhanh" và bộ đánh giá lớn hơn sẽ hữu ích: bộ nhỏ để kiểm tra nhanh, bộ lớn để đo chỉ số hiệu suất rộng hơn.

### Đánh giá Trực tuyến

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Đây là đánh giá đại lý trong môi trường sống, tức là trong quá trình sử dụng thực tế tại sản xuất. Đánh giá trực tuyến liên quan đến giám sát hiệu suất đại lý trên các tương tác người dùng thật và phân tích kết quả liên tục.

Ví dụ, bạn có thể theo dõi tỉ lệ thành công, điểm hài lòng người dùng hoặc các chỉ số khác trên lưu lượng thực tế. Ưu điểm của đánh giá trực tuyến là nó **bắt được những điều bạn không thể lường trước trong phòng lab** – bạn có thể quan sát sự trôi mô hình theo thời gian (nếu hiệu quả đại lý giảm khi mẫu đầu vào thay đổi) và phát hiện các truy vấn hoặc tình huống bất ngờ không có trong dữ liệu thử nghiệm. Nó cung cấp bức tranh thực sự về cách đại lý hành xử trong thực tế.

Đánh giá trực tuyến thường thu thập cả phản hồi người dùng ngầm định và rõ ràng như đã thảo luận, và có thể chạy các thử nghiệm bóng tối hoặc A/B (phiên bản đại lý mới chạy song song để so sánh với phiên bản cũ). Thách thức là có thể khó có được nhãn hay điểm tin cậy cho các tương tác thực tế – bạn có thể phải dựa vào phản hồi người dùng hoặc các chỉ số phụ trợ (như việc người dùng có nhấn vào kết quả hay không).

### Kết hợp hai loại

Đánh giá trực tuyến và ngoại tuyến không loại trừ nhau; chúng bổ sung rất tốt cho nhau. Thông tin từ giám sát trực tuyến (ví dụ, loại truy vấn người dùng mới mà đại lý hoạt động kém) có thể được dùng để mở rộng và cải thiện bộ dữ liệu thử nghiệm ngoại tuyến. Ngược lại, những đại lý hoạt động tốt trong kiểm tra ngoại tuyến có thể được triển khai tự tin hơn và giám sát trực tuyến.

Thực tế, nhiều nhóm áp dụng vòng lặp:

_đánh giá ngoại tuyến -> triển khai -> giám sát trực tuyến -> thu thập ca lỗi mới -> thêm vào bộ dữ liệu ngoại tuyến -> tinh chỉnh đại lý -> lặp lại_.

## Các Vấn đề Thường gặp

Khi bạn triển khai đại lý AI vào sản xuất, bạn có thể gặp các thách thức khác nhau. Dưới đây là một số vấn đề phổ biến và giải pháp tiềm năng:

| **Vấn đề**    | **Giải pháp Tiềm năng**   |
| ------------- | ------------------ |
| Đại lý AI không thực hiện tác vụ nhất quán | - Tinh chỉnh prompt cho đại lý AI; rõ ràng về mục tiêu.<br>- Nhận biết nơi chia nhỏ tác vụ thành các tác vụ con và xử lý chúng bằng nhiều đại lý có thể giúp. |
| Đại lý AI chạy vào vòng lặp liên tục  | - Đảm bảo bạn có điều kiện dừng rõ ràng để đại lý biết khi nào dừng quá trình.<br>- Đối với các tác vụ phức tạp yêu cầu lý luận và lên kế hoạch, dùng mô hình lớn hơn chuyên biệt cho tác vụ lý luận. |
| Các lệnh gọi công cụ của đại lý AI không hoạt động tốt   | - Kiểm tra và xác thực đầu ra của công cụ ngoài hệ thống đại lý.<br>- Tinh chỉnh các tham số, prompt và tên công cụ được định nghĩa.  |
| Hệ thống đa đại lý không hoạt động nhất quán | - Tinh chỉnh prompt cho từng đại lý để đảm bảo chúng cụ thể và khác biệt.<br>- Xây dựng hệ thống phân cấp dùng đại lý “điều phối” hoặc điều khiển để xác định đại lý phù hợp. |

Nhiều vấn đề này có thể được xác định hiệu quả hơn với khả năng quan sát. Các traces và chỉ số đã thảo luận giúp xác định chính xác điểm xảy ra vấn đề trong quy trình đại lý, khiến việc gỡ lỗi và tối ưu hiệu quả hơn nhiều.

## Quản lý Chi phí


Dưới đây là một số chiến lược để quản lý chi phí triển khai các đại lý AI vào sản xuất:

**Sử dụng Mô hình Nhỏ hơn:** Các Mô hình Ngôn ngữ Nhỏ (SLMs) có thể hoạt động tốt trong một số trường hợp sử dụng đại lý nhất định và sẽ giảm đáng kể chi phí. Như đã đề cập trước đây, xây dựng một hệ thống đánh giá để xác định và so sánh hiệu năng so với các mô hình lớn hơn là cách tốt nhất để hiểu SLM sẽ hoạt động tốt như thế nào trên trường hợp sử dụng của bạn. Hãy xem xét sử dụng SLM cho các tác vụ đơn giản hơn như phân loại ý định hoặc trích xuất tham số, trong khi dành các mô hình lớn hơn cho các tác vụ suy luận phức tạp.

**Sử dụng Mô hình Router:** Một chiến lược tương tự là sử dụng đa dạng các mô hình và kích thước. Bạn có thể sử dụng LLM/SLM hoặc hàm serverless để phân luồng yêu cầu dựa trên độ phức tạp tới các mô hình phù hợp nhất. Điều này cũng sẽ giúp giảm chi phí đồng thời đảm bảo hiệu năng trên các tác vụ phù hợp. Ví dụ, chuyển các truy vấn đơn giản đến các mô hình nhỏ hơn, nhanh hơn, và chỉ sử dụng các mô hình lớn đắt tiền cho các tác vụ suy luận phức tạp.

**Lưu bộ nhớ đệm các Phản hồi:** Xác định các yêu cầu và tác vụ phổ biến và cung cấp câu trả lời trước khi chúng đi qua hệ thống đại lý của bạn là một cách tốt để giảm khối lượng các yêu cầu tương tự. Bạn thậm chí có thể triển khai một luồng để xác định mức độ tương đồng của một yêu cầu với các yêu cầu đã lưu trong bộ nhớ đệm bằng cách sử dụng các mô hình AI cơ bản hơn. Chiến lược này có thể giảm đáng kể chi phí cho các câu hỏi thường gặp hoặc quy trình làm việc phổ biến.

## Hãy xem cách điều này hoạt động trong thực tế

Trong [notebook ví dụ của phần này](./code_samples/10-expense_claim-demo.ipynb), chúng ta sẽ xem các ví dụ về cách sử dụng công cụ quan sát để giám sát và đánh giá đại lý của mình.


### Còn Thắc mắc gì về Đại lý AI trong Sản xuất?

Tham gia [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) để gặp gỡ những người học khác, tham gia giờ làm việc và được giải đáp các câu hỏi về Đại lý AI.

## Bài học trước

[Mẫu Thiết kế Metacognition](../09-metacognition/README.md)

## Bài học tiếp theo

[Giao thức Đại lý](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->