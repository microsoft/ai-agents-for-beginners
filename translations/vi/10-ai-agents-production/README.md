# Tác nhân AI trong Sản xuất: Quan sát & Đánh giá

[![Tác nhân AI trong Sản xuất](../../../translated_images/vi/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Khi các tác nhân AI chuyển từ nguyên mẫu thí nghiệm sang ứng dụng thực tế, khả năng hiểu hành vi của chúng, theo dõi hiệu suất và đánh giá đầu ra một cách hệ thống trở nên quan trọng.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách/hiểu được:
- Những khái niệm cốt lõi về khả năng quan sát (observability) và đánh giá tác nhân
- Các kỹ thuật để cải thiện hiệu suất, chi phí và hiệu quả của tác nhân
- Cái gì và làm thế nào để đánh giá tác nhân AI của bạn một cách hệ thống
- Cách kiểm soát chi phí khi triển khai tác nhân AI vào sản xuất
- Cách thêm instrumentation cho các tác nhân được xây dựng bằng Microsoft Agent Framework

Mục tiêu là trang bị cho bạn kiến thức để biến các tác nhân "hộp đen" của bạn thành các hệ thống minh bạch, dễ quản lý và đáng tin cậy.

_**Lưu ý:** Việc triển khai các Tác nhân AI an toàn và đáng tin cậy là quan trọng. Hãy xem thêm bài học [Xây dựng tác nhân AI đáng tin cậy](./06-building-trustworthy-agents/README.md)._

## Traces and Spans

Các công cụ quan sát như [Langfuse](https://langfuse.com/) hoặc [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) thường biểu diễn các lần chạy tác nhân dưới dạng traces và spans.

- **Trace** đại diện cho một nhiệm vụ tác nhân hoàn chỉnh từ bắt đầu đến kết thúc (như xử lý một truy vấn của người dùng).
- **Spans** là các bước riêng lẻ trong trace (như gọi một mô hình ngôn ngữ hoặc truy xuất dữ liệu).

![Cây trace trong Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Nếu không có khả năng quan sát, một tác nhân AI có thể giống như một "hộp đen" — trạng thái nội bộ và quá trình suy luận của nó không rõ ràng, khiến việc chẩn đoán sự cố hoặc tối ưu hóa hiệu suất trở nên khó khăn. Với khả năng quan sát, các tác nhân trở thành "hộp trong suốt", cung cấp tính minh bạch cần thiết để xây dựng niềm tin và đảm bảo chúng hoạt động như mong đợi. 

## Tại sao khả năng quan sát lại quan trọng trong môi trường sản xuất

Việc chuyển các tác nhân AI sang môi trường sản xuất giới thiệu một tập hợp thách thức và yêu cầu mới. Khả năng quan sát không còn là điều "tốt để có" mà là một năng lực then chốt:

*   **Gỡ lỗi và phân tích nguyên nhân gốc rễ:** Khi một tác nhân thất bại hoặc tạo ra đầu ra không mong muốn, các công cụ quan sát cung cấp các traces cần thiết để xác định nguồn gốc lỗi. Điều này đặc biệt quan trọng trong các tác nhân phức tạp có thể bao gồm nhiều lần gọi LLM, tương tác công cụ và logic có điều kiện.
*   **Quản lý độ trễ và chi phí:** Các tác nhân AI thường phụ thuộc vào LLM và các API bên ngoài được tính phí theo token hoặc theo lần gọi. Khả năng quan sát cho phép theo dõi chính xác các lần gọi này, giúp xác định các thao tác quá chậm hoặc tốn kém. Điều này cho phép các nhóm tối ưu hóa prompt, chọn mô hình hiệu quả hơn hoặc thiết kế lại luồng công việc để quản lý chi phí vận hành và đảm bảo trải nghiệm người dùng tốt.
*   **Niềm tin, an toàn và tuân thủ:** Trong nhiều ứng dụng, điều quan trọng là đảm bảo các tác nhân hành xử an toàn và có đạo đức. Khả năng quan sát cung cấp một bản ghi kiểm toán các hành động và quyết định của tác nhân. Điều này có thể được sử dụng để phát hiện và giảm thiểu các vấn đề như prompt injection, tạo nội dung gây hại, hoặc xử lý sai thông tin nhận dạng cá nhân (PII). Ví dụ, bạn có thể xem lại traces để hiểu tại sao tác nhân đưa ra một phản hồi nhất định hoặc sử dụng một công cụ cụ thể.
*   **Vòng lặp cải tiến liên tục:** Dữ liệu quan sát là nền tảng cho quá trình phát triển lặp. Bằng cách giám sát cách thức tác nhân hoạt động trong thế giới thực, các nhóm có thể xác định khu vực cần cải tiến, thu thập dữ liệu để tinh chỉnh mô hình và xác nhận tác động của các thay đổi. Điều này tạo thành một vòng phản hồi nơi những hiểu biết từ đánh giá trực tuyến dẫn đến thí nghiệm và điều chỉnh ngoại tuyến, giúp hiệu suất tác nhân ngày càng tốt hơn.

## Các chỉ số chính cần theo dõi

Để giám sát và hiểu hành vi tác nhân, cần theo dõi một loạt chỉ số và tín hiệu. Mặc dù các chỉ số cụ thể có thể thay đổi tùy theo mục đích của tác nhân, một số chỉ số là quan trọng chung.

Dưới đây là một số chỉ số phổ biến mà các công cụ quan sát thường theo dõi:

**Độ trễ (Latency):** Tác nhân trả lời nhanh đến mức nào? Thời gian chờ lâu ảnh hưởng tiêu cực đến trải nghiệm người dùng. Bạn nên đo độ trễ cho các nhiệm vụ và các bước riêng lẻ bằng cách trace các lần chạy tác nhân. Ví dụ, một tác nhân mất 20 giây cho tất cả các lần gọi mô hình có thể được tăng tốc bằng cách sử dụng mô hình nhanh hơn hoặc chạy các lần gọi mô hình song song.

**Chi phí:** Chi phí cho mỗi lần chạy tác nhân là bao nhiêu? Các tác nhân AI phụ thuộc vào các lần gọi LLM được tính theo token hoặc API bên ngoài. Việc sử dụng công cụ thường xuyên hoặc nhiều prompt có thể nhanh chóng làm tăng chi phí. Ví dụ, nếu một tác nhân gọi LLM năm lần cho cải thiện chất lượng nhỏ, bạn cần đánh giá xem chi phí có xứng đáng hay có thể giảm số lần gọi hoặc sử dụng mô hình rẻ hơn. Giám sát theo thời gian thực cũng có thể giúp phát hiện các đột biến không mong muốn (ví dụ: lỗi gây vòng lặp API quá mức).

**Lỗi yêu cầu (Request Errors):** Có bao nhiêu yêu cầu mà tác nhân không hoàn thành? Điều này có thể bao gồm lỗi API hoặc gọi công cụ thất bại. Để làm cho tác nhân của bạn bền bỉ hơn trong sản xuất, bạn có thể thiết lập các cơ chế dự phòng hoặc thử lại. Ví dụ: nếu nhà cung cấp LLM A bị lỗi, bạn chuyển sang nhà cung cấp LLM B làm phương án dự phòng.

**Phản hồi của người dùng:** Thực hiện đánh giá trực tiếp từ người dùng cung cấp những hiểu biết giá trị. Điều này có thể bao gồm xếp hạng rõ ràng (👍giơ ngón cái lên/👎giơ ngón cái xuống, ⭐1-5 sao) hoặc nhận xét bằng văn bản. Phản hồi tiêu cực liên tục nên cảnh báo bạn vì đây là dấu hiệu tác nhân không hoạt động như mong đợi.

**Phản hồi gián tiếp của người dùng:** Hành vi người dùng cung cấp phản hồi gián tiếp ngay cả khi không có xếp hạng rõ ràng. Điều này có thể bao gồm việc người dùng ngay lập tức chỉnh sửa câu hỏi, gửi truy vấn lặp lại hoặc nhấn nút thử lại. Ví dụ: nếu bạn thấy người dùng lặp đi lặp lại câu hỏi giống nhau, đó là dấu hiệu tác nhân không hoạt động như mong đợi.

**Độ chính xác (Accuracy):** Tần suất tác nhân tạo ra đầu ra chính xác hoặc mong muốn là bao nhiêu? Định nghĩa độ chính xác thay đổi (ví dụ: độ đúng trong giải quyết vấn đề, độ chính xác truy xuất thông tin, hài lòng của người dùng). Bước đầu là xác định thành công trông như thế nào đối với tác nhân của bạn. Bạn có thể theo dõi độ chính xác thông qua kiểm tra tự động, điểm đánh giá, hoặc nhãn hoàn thành nhiệm vụ. Ví dụ, gắn nhãn traces là "succeeded" hoặc "failed". 

**Chỉ số đánh giá tự động:** Bạn cũng có thể thiết lập các bài đánh giá tự động. Ví dụ, bạn có thể dùng một LLM để chấm điểm đầu ra của tác nhân, ví dụ nó có hữu ích, chính xác hay không. Cũng có một số thư viện mã nguồn mở giúp bạn chấm điểm các khía cạnh khác nhau của tác nhân. Ví dụ: [RAGAS](https://docs.ragas.io/) cho các tác nhân RAG hoặc [LLM Guard](https://llm-guard.com/) để phát hiện ngôn ngữ có hại hoặc prompt injection. 

Trong thực tế, sự kết hợp của các chỉ số này cung cấp bao phủ tốt nhất về sức khỏe của một tác nhân AI. Trong [notebook ví dụ](./code_samples/10-expense_claim-demo.ipynb) của chương này, chúng tôi sẽ cho bạn thấy những chỉ số này trông như thế nào trong các ví dụ thực tế nhưng trước tiên, chúng ta sẽ tìm hiểu quy trình đánh giá điển hình trông ra sao.

## Thêm instrumentation cho Tác nhân của bạn

Để thu thập dữ liệu tracing, bạn sẽ cần thêm instrumentation vào mã của mình. Mục tiêu là instrument mã tác nhân để phát ra traces và metrics có thể được thu thập, xử lý và trực quan hóa bởi một nền tảng quan sát.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) đã trở thành tiêu chuẩn ngành cho khả năng quan sát LLM. Nó cung cấp một bộ API, SDK và công cụ để tạo, thu thập và xuất dữ liệu telemetry. 

Có nhiều thư viện instrumentation bao bọc các framework tác nhân hiện có và làm cho việc xuất OpenTelemetry spans tới công cụ quan sát trở nên dễ dàng. Microsoft Agent Framework tích hợp với OpenTelemetry một cách bản địa. Dưới đây là một ví dụ về cách instrument một tác nhân MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Việc thực thi tác nhân được theo dõi tự động
    pass
```

Trong [notebook ví dụ](./code_samples/10-expense_claim-demo.ipynb) của chương này sẽ minh họa cách thêm instrumentation cho tác nhân MAF của bạn.

**Tạo Span thủ công:** Mặc dù các thư viện instrumentation cung cấp một nền tảng tốt, thường có những trường hợp cần thông tin chi tiết hoặc tùy chỉnh hơn. Bạn có thể tạo spans thủ công để thêm logic ứng dụng tùy chỉnh. Quan trọng hơn, bạn có thể làm giàu các spans được tạo tự động hoặc thủ công bằng các thuộc tính tùy chỉnh (còn gọi là tags hoặc metadata). Các thuộc tính này có thể bao gồm dữ liệu đặc thù doanh nghiệp, các tính toán trung gian, hoặc bất kỳ ngữ cảnh nào có thể hữu ích cho việc gỡ lỗi hoặc phân tích, chẳng hạn như `user_id`, `session_id`, hoặc `model_version`.

Ví dụ về tạo traces và spans thủ công với [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Đánh giá Tác nhân

Khả năng quan sát cung cấp cho chúng ta các chỉ số, nhưng đánh giá là quá trình phân tích dữ liệu đó (và thực hiện các bài kiểm tra) để xác định mức độ hiệu quả của tác nhân AI và cách thức cải thiện nó. Nói cách khác, khi bạn có các traces và metrics đó, bạn sử dụng chúng như thế nào để đánh giá tác nhân và đưa ra quyết định?

Đánh giá định kỳ là quan trọng vì các tác nhân AI thường không xác định và có thể tiến hoá (thông qua cập nhật hoặc drift hành vi mô hình) – nếu không có đánh giá, bạn sẽ không biết liệu "tác nhân thông minh" của mình có thực sự làm tốt nhiệm vụ hay đang bị suy giảm.

Có hai loại đánh giá cho tác nhân AI: **đánh giá trực tuyến (online evaluation)** và **đánh giá ngoại tuyến (offline evaluation)**. Cả hai đều có giá trị và bổ sung cho nhau. Thông thường chúng ta bắt đầu với đánh giá ngoại tuyến, vì đây là bước tối thiểu cần thiết trước khi triển khai bất kỳ tác nhân nào.

### Đánh giá ngoại tuyến

![Mục trong tập dữ liệu trong Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Điều này bao gồm đánh giá tác nhân trong môi trường được kiểm soát, thường sử dụng các bộ dữ liệu kiểm thử, không phải truy vấn người dùng trực tiếp. Bạn sử dụng các bộ dữ liệu được tuyển chọn nơi bạn biết đầu ra mong đợi hoặc hành vi đúng, sau đó chạy tác nhân trên chúng.

Ví dụ, nếu bạn xây dựng một tác nhân giải bài toán lời văn toán học, bạn có thể có một [bộ dữ liệu kiểm thử](https://huggingface.co/datasets/gsm8k) gồm 100 bài toán với đáp án đã biết. Đánh giá ngoại tuyến thường được thực hiện trong quá trình phát triển (và có thể là một phần của pipeline CI/CD) để kiểm tra cải tiến hoặc ngăn ngừa suy giảm. Lợi ích là **có thể lặp lại và bạn có thể nhận được các chỉ số độ chính xác rõ ràng vì bạn có ground truth**. Bạn cũng có thể mô phỏng truy vấn người dùng và đo phản hồi của tác nhân so với câu trả lời lý tưởng hoặc sử dụng các chỉ số tự động như mô tả ở trên.

Thách thức chính với đánh giá ngoại tuyến là đảm bảo bộ dữ liệu kiểm thử của bạn toàn diện và luôn có liên quan – tác nhân có thể hoạt động tốt trên một bộ kiểm thử cố định nhưng gặp các truy vấn rất khác trong sản xuất. Do đó, bạn nên cập nhật bộ kiểm thử với các trường hợp biên và ví dụ mới phản ánh kịch bản thực tế​. Việc kết hợp các bộ "smoke test" nhỏ và các bộ đánh giá lớn hơn là hữu ích: bộ nhỏ để kiểm tra nhanh và bộ lớn để có các chỉ số hiệu suất rộng hơn​.

### Đánh giá trực tuyến

![Tổng quan các chỉ số quan sát](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Đây là việc đánh giá tác nhân trong môi trường sống, thực tế, tức là trong quá trình sử dụng thực tế trên sản xuất. Đánh giá trực tuyến bao gồm việc giám sát hiệu suất tác nhân trên các tương tác người dùng thực và phân tích kết quả liên tục.

Ví dụ, bạn có thể theo dõi tỷ lệ thành công, điểm hài lòng của người dùng, hoặc các chỉ số khác trên lưu lượng trực tiếp. Ưu điểm của đánh giá trực tuyến là nó **bắt được những thứ bạn có thể không lường trước trong phòng thí nghiệm** – bạn có thể quan sát drift mô hình theo thời gian (nếu hiệu quả của tác nhân giảm khi mẫu đầu vào thay đổi) và phát hiện các truy vấn hoặc tình huống bất ngờ không có trong dữ liệu kiểm thử​. Nó cung cấp một bức tranh thực sự về cách tác nhân hành xử ngoài đời.

Đánh giá trực tuyến thường liên quan đến việc thu thập phản hồi rõ ràng và ngầm định của người dùng, như đã thảo luận, và có thể chạy các bài kiểm tra shadow hoặc A/B (nơi một phiên bản mới của tác nhân chạy song song để so sánh với phiên bản cũ). Thách thức là việc có được nhãn hoặc điểm số đáng tin cậy cho các tương tác trực tiếp có thể khó – bạn có thể phụ thuộc vào phản hồi người dùng hoặc các chỉ số hạ nguồn (ví dụ: người dùng có nhấp vào kết quả hay không).

### Kết hợp cả hai

Đánh giá trực tuyến và ngoại tuyến không loại trừ lẫn nhau; chúng bổ sung cho nhau rất nhiều. Những hiểu biết từ giám sát trực tuyến (ví dụ: các loại truy vấn người dùng mới mà tác nhân hoạt động kém) có thể được sử dụng để bổ sung và cải thiện bộ dữ liệu kiểm thử ngoại tuyến. Ngược lại, các tác nhân hoạt động tốt trong các bài kiểm thử ngoại tuyến có thể được triển khai và giám sát trực tuyến với sự tự tin lớn hơn.

Thực tế, nhiều đội áp dụng một vòng lặp:

_đánh giá ngoại tuyến -> triển khai -> giám sát trực tuyến -> thu thập các trường hợp lỗi mới -> thêm vào bộ dữ liệu ngoại tuyến -> tinh chỉnh tác nhân -> lặp lại_.

## Các vấn đề phổ biến

Khi bạn triển khai các tác nhân AI vào sản xuất, bạn có thể gặp phải các thách thức khác nhau. Dưới đây là một số vấn đề phổ biến và các giải pháp tiềm năng:

| **Vấn đề**    | **Giải pháp Tiềm năng**   |
| ------------- | ------------------ |
| Tác nhân AI không thực hiện nhiệm vụ một cách nhất quán | - Tinh chỉnh prompt đưa cho Tác nhân AI; rõ ràng về mục tiêu.<br>- Xác định nơi chia nhiệm vụ thành các nhiệm vụ con và xử lý chúng bởi nhiều tác nhân có thể hữu ích. |
| Tác nhân AI rơi vào vòng lặp liên tục  | - Đảm bảo bạn có các điều khoản và điều kiện chấm dứt rõ ràng để Tác nhân biết khi nào dừng quy trình.<br>- Đối với các nhiệm vụ phức tạp đòi hỏi suy luận và lập kế hoạch, sử dụng mô hình lớn hơn chuyên về các nhiệm vụ suy luận. |
| Các cuộc gọi công cụ của Tác nhân không hoạt động tốt   | - Kiểm tra và xác thực đầu ra của công cụ bên ngoài hệ thống tác nhân.<br>- Tinh chỉnh các tham số đã định nghĩa, prompt, và tên gọi các công cụ.  |
| Hệ thống đa tác nhân không hoạt động ổn định | - Tinh chỉnh prompt đưa cho từng tác nhân để đảm bảo chúng cụ thể và phân biệt với nhau.<br>- Xây dựng hệ thống phân cấp sử dụng một tác nhân "điều phối" hoặc bộ điều khiển để xác định tác nhân phù hợp. |

Nhiều vấn đề này có thể được nhận diện hiệu quả hơn với khả năng quan sát được triển khai. Các traces và metrics đã thảo luận ở trên giúp xác định chính xác nơi trong luồng công việc tác nhân xảy ra sự cố, giúp gỡ lỗi và tối ưu hóa hiệu quả hơn nhiều.

## Quản lý Chi phí
Dưới đây là một số chiến lược để quản lý chi phí khi triển khai các tác tử AI vào môi trường sản xuất:

**Sử dụng Mô hình Nhỏ hơn:** Small Language Models (SLMs) có thể hoạt động tốt trong một số trường hợp sử dụng agentic nhất định và sẽ giảm chi phí đáng kể. Như đã đề cập trước đó, xây dựng một hệ thống đánh giá để xác định và so sánh hiệu suất so với các mô hình lớn hơn là cách tốt nhất để hiểu xem một SLM sẽ hoạt động như thế nào trong trường hợp sử dụng của bạn. Cân nhắc sử dụng SLM cho các tác vụ đơn giản hơn như phân loại ý định hoặc trích xuất tham số, trong khi dành các mô hình lớn hơn cho suy luận phức tạp.

**Sử dụng Mô hình Bộ định tuyến:** Một chiến lược tương tự là sử dụng đa dạng các mô hình và kích thước. Bạn có thể sử dụng một LLM/SLM hoặc hàm serverless để định tuyến các yêu cầu dựa trên mức độ phức tạp đến các mô hình phù hợp nhất. Điều này cũng sẽ giúp giảm chi phí đồng thời đảm bảo hiệu suất cho các tác vụ phù hợp. Ví dụ, định tuyến các truy vấn đơn giản tới các mô hình nhỏ hơn, nhanh hơn, và chỉ sử dụng các mô hình lớn tốn kém cho các tác vụ suy luận phức tạp.

**Bộ nhớ đệm Phản hồi:** Xác định các yêu cầu và tác vụ phổ biến và cung cấp các phản hồi trước khi chúng đi qua hệ thống tác tử của bạn là một cách tốt để giảm khối lượng các yêu cầu tương tự. Bạn thậm chí có thể triển khai một luồng để xác định mức độ tương đồng của một yêu cầu với các yêu cầu đã được lưu trong bộ nhớ đệm bằng cách sử dụng các mô hình AI cơ bản hơn. Chiến lược này có thể giảm đáng kể chi phí cho các câu hỏi thường gặp hoặc các quy trình làm việc phổ biến.

## Lets see how this works in practice

In the [notebook ví dụ của phần này](./code_samples/10-expense_claim-demo.ipynb), we’ll see examples of how we can use observability tools to monitor and evaluate our agent.

### Got More Questions about AI Agents in Production?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Previous Lesson

[Mô hình Thiết kế Siêu nhận thức](../09-metacognition/README.md)

## Next Lesson

[Giao thức Agentic](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Miễn trừ trách nhiệm:
Tài liệu này được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi nỗ lực đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc thông tin không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính thức. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->