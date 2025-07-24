<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-24T08:43:28+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "vi"
}
-->
# Các Tác Nhân AI Trong Sản Xuất: Khả Năng Quan Sát & Đánh Giá

Khi các tác nhân AI chuyển từ các nguyên mẫu thử nghiệm sang ứng dụng thực tế, khả năng hiểu hành vi của chúng, giám sát hiệu suất và đánh giá đầu ra một cách có hệ thống trở nên rất quan trọng.

## Mục Tiêu Học Tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách/hiểu được:
- Các khái niệm cốt lõi về khả năng quan sát và đánh giá tác nhân
- Các kỹ thuật để cải thiện hiệu suất, chi phí và hiệu quả của tác nhân
- Cách đánh giá tác nhân AI của bạn một cách có hệ thống
- Cách kiểm soát chi phí khi triển khai tác nhân AI vào sản xuất
- Cách triển khai các công cụ quan sát cho các tác nhân được xây dựng bằng AutoGen

Mục tiêu là trang bị cho bạn kiến thức để biến các tác nhân "hộp đen" của mình thành các hệ thống minh bạch, có thể quản lý và đáng tin cậy.

_**Lưu ý:** Việc triển khai các tác nhân AI an toàn và đáng tin cậy là rất quan trọng. Hãy xem bài học [Xây Dựng Các Tác Nhân AI Đáng Tin Cậy](./06-building-trustworthy-agents/README.md) để biết thêm chi tiết._

## Traces và Spans

Các công cụ quan sát như [Langfuse](https://langfuse.com/) hoặc [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) thường biểu diễn các lần chạy của tác nhân dưới dạng traces và spans.

- **Trace** đại diện cho một nhiệm vụ hoàn chỉnh của tác nhân từ đầu đến cuối (như xử lý một truy vấn của người dùng).
- **Spans** là các bước riêng lẻ trong trace (như gọi một mô hình ngôn ngữ hoặc truy xuất dữ liệu).

![Cây Trace trong Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Nếu không có khả năng quan sát, một tác nhân AI có thể giống như một "hộp đen" - trạng thái nội bộ và lý luận của nó không rõ ràng, khiến việc chẩn đoán vấn đề hoặc tối ưu hóa hiệu suất trở nên khó khăn. Với khả năng quan sát, các tác nhân trở thành "hộp kính," mang lại sự minh bạch cần thiết để xây dựng niềm tin và đảm bảo chúng hoạt động như mong đợi.

## Tại Sao Khả Năng Quan Sát Quan Trọng Trong Môi Trường Sản Xuất

Việc chuyển các tác nhân AI sang môi trường sản xuất mang lại một loạt thách thức và yêu cầu mới. Khả năng quan sát không còn là một "tính năng tốt có" mà trở thành một khả năng quan trọng:

*   **Gỡ Lỗi và Phân Tích Nguyên Nhân Gốc Rễ**: Khi một tác nhân thất bại hoặc tạo ra đầu ra không mong đợi, các công cụ quan sát cung cấp các trace cần thiết để xác định nguồn gốc của lỗi. Điều này đặc biệt quan trọng trong các tác nhân phức tạp có thể liên quan đến nhiều lần gọi LLM, tương tác công cụ và logic điều kiện.
*   **Quản Lý Độ Trễ và Chi Phí**: Các tác nhân AI thường dựa vào LLM và các API bên ngoài được tính phí theo token hoặc mỗi lần gọi. Khả năng quan sát cho phép theo dõi chính xác các lần gọi này, giúp xác định các hoạt động quá chậm hoặc tốn kém. Điều này cho phép các nhóm tối ưu hóa prompt, chọn các mô hình hiệu quả hơn hoặc thiết kế lại quy trình làm việc để quản lý chi phí vận hành và đảm bảo trải nghiệm người dùng tốt.
*   **Niềm Tin, An Toàn và Tuân Thủ**: Trong nhiều ứng dụng, điều quan trọng là đảm bảo các tác nhân hoạt động an toàn và có đạo đức. Khả năng quan sát cung cấp một dấu vết kiểm toán về các hành động và quyết định của tác nhân. Điều này có thể được sử dụng để phát hiện và giảm thiểu các vấn đề như tiêm lệnh prompt, tạo nội dung có hại hoặc xử lý sai thông tin nhận dạng cá nhân (PII). Ví dụ, bạn có thể xem lại các trace để hiểu tại sao một tác nhân đưa ra một phản hồi cụ thể hoặc sử dụng một công cụ cụ thể.
*   **Vòng Lặp Cải Tiến Liên Tục**: Dữ liệu quan sát là nền tảng của một quy trình phát triển lặp đi lặp lại. Bằng cách giám sát cách các tác nhân hoạt động trong thế giới thực, các nhóm có thể xác định các lĩnh vực cần cải thiện, thu thập dữ liệu để tinh chỉnh mô hình và xác nhận tác động của các thay đổi. Điều này tạo ra một vòng lặp phản hồi, nơi các thông tin chi tiết từ đánh giá trực tuyến thông báo cho các thử nghiệm ngoại tuyến và tinh chỉnh, dẫn đến hiệu suất tác nhân ngày càng tốt hơn.

## Các Chỉ Số Chính Cần Theo Dõi

Để giám sát và hiểu hành vi của tác nhân, cần theo dõi một loạt các chỉ số và tín hiệu. Mặc dù các chỉ số cụ thể có thể thay đổi tùy thuộc vào mục đích của tác nhân, một số chỉ số là quan trọng đối với hầu hết các trường hợp.

Dưới đây là một số chỉ số phổ biến mà các công cụ quan sát thường theo dõi:

**Độ Trễ:** Tác nhân phản hồi nhanh như thế nào? Thời gian chờ lâu ảnh hưởng tiêu cực đến trải nghiệm người dùng. Bạn nên đo độ trễ cho các nhiệm vụ và các bước riêng lẻ bằng cách theo dõi các lần chạy của tác nhân. Ví dụ, một tác nhân mất 20 giây cho tất cả các lần gọi mô hình có thể được tăng tốc bằng cách sử dụng một mô hình nhanh hơn hoặc chạy các lần gọi mô hình song song.

**Chi Phí:** Chi phí cho mỗi lần chạy tác nhân là bao nhiêu? Các tác nhân AI dựa vào các lần gọi LLM được tính phí theo token hoặc các API bên ngoài. Việc sử dụng công cụ thường xuyên hoặc nhiều prompt có thể nhanh chóng tăng chi phí. Ví dụ, nếu một tác nhân gọi LLM năm lần để cải thiện chất lượng không đáng kể, bạn cần đánh giá xem chi phí có hợp lý không hoặc có thể giảm số lần gọi hoặc sử dụng một mô hình rẻ hơn. Giám sát thời gian thực cũng có thể giúp xác định các đột biến bất ngờ (ví dụ: lỗi gây ra các vòng lặp API quá mức).

**Lỗi Yêu Cầu:** Có bao nhiêu yêu cầu mà tác nhân thất bại? Điều này có thể bao gồm lỗi API hoặc lỗi gọi công cụ. Để làm cho tác nhân của bạn mạnh mẽ hơn trong sản xuất, bạn có thể thiết lập các phương án dự phòng hoặc thử lại. Ví dụ: nếu nhà cung cấp LLM A không hoạt động, bạn chuyển sang nhà cung cấp LLM B làm dự phòng.

**Phản Hồi Người Dùng:** Việc triển khai các đánh giá trực tiếp từ người dùng cung cấp thông tin chi tiết có giá trị. Điều này có thể bao gồm các đánh giá rõ ràng (👍thích/👎không thích, ⭐1-5 sao) hoặc nhận xét bằng văn bản. Phản hồi tiêu cực liên tục nên cảnh báo bạn vì đây là dấu hiệu cho thấy tác nhân không hoạt động như mong đợi.

**Phản Hồi Ngầm Định Từ Người Dùng:** Hành vi của người dùng cung cấp phản hồi gián tiếp ngay cả khi không có đánh giá rõ ràng. Điều này có thể bao gồm việc diễn đạt lại câu hỏi ngay lập tức, truy vấn lặp lại hoặc nhấp vào nút thử lại. Ví dụ: nếu bạn thấy người dùng liên tục hỏi cùng một câu hỏi, đây là dấu hiệu cho thấy tác nhân không hoạt động như mong đợi.

**Độ Chính Xác:** Tác nhân tạo ra các đầu ra chính xác hoặc mong muốn thường xuyên như thế nào? Định nghĩa về độ chính xác có thể khác nhau (ví dụ: độ chính xác trong giải quyết vấn đề, độ chính xác trong truy xuất thông tin, sự hài lòng của người dùng). Bước đầu tiên là xác định thành công trông như thế nào đối với tác nhân của bạn. Bạn có thể theo dõi độ chính xác thông qua các kiểm tra tự động, điểm đánh giá hoặc nhãn hoàn thành nhiệm vụ. Ví dụ: đánh dấu các trace là "thành công" hoặc "thất bại."

**Các Chỉ Số Đánh Giá Tự Động:** Bạn cũng có thể thiết lập các đánh giá tự động. Ví dụ: bạn có thể sử dụng một LLM để chấm điểm đầu ra của tác nhân, ví dụ: liệu nó có hữu ích, chính xác hay không. Ngoài ra, có một số thư viện mã nguồn mở giúp bạn chấm điểm các khía cạnh khác nhau của tác nhân. Ví dụ: [RAGAS](https://docs.ragas.io/) cho các tác nhân RAG hoặc [LLM Guard](https://llm-guard.com/) để phát hiện ngôn ngữ có hại hoặc tiêm lệnh prompt.

Trong thực tế, sự kết hợp của các chỉ số này mang lại phạm vi bao quát tốt nhất về sức khỏe của tác nhân AI. Trong [notebook ví dụ](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) của chương này, chúng ta sẽ xem các chỉ số này trông như thế nào trong các ví dụ thực tế, nhưng trước tiên, chúng ta sẽ tìm hiểu cách một quy trình đánh giá điển hình hoạt động.

## Triển Khai Công Cụ Quan Sát Cho Tác Nhân

Để thu thập dữ liệu trace, bạn cần triển khai công cụ quan sát vào mã của mình. Mục tiêu là triển khai mã tác nhân để phát ra các trace và chỉ số có thể được thu thập, xử lý và hiển thị bởi một nền tảng quan sát.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) đã nổi lên như một tiêu chuẩn ngành cho khả năng quan sát LLM. Nó cung cấp một tập hợp các API, SDK và công cụ để tạo, thu thập và xuất dữ liệu telemetry.

Có nhiều thư viện triển khai công cụ quan sát bao bọc các framework tác nhân hiện có và giúp dễ dàng xuất các span OpenTelemetry sang một công cụ quan sát. Dưới đây là một ví dụ về cách triển khai một tác nhân AutoGen với thư viện [OpenLit](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

[Notebook ví dụ](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) trong chương này sẽ minh họa cách triển khai công cụ quan sát cho tác nhân AutoGen của bạn.

**Tạo Span Thủ Công:** Trong khi các thư viện triển khai công cụ quan sát cung cấp một cơ sở tốt, thường có những trường hợp cần thông tin chi tiết hoặc tùy chỉnh hơn. Bạn có thể tạo span thủ công để thêm logic ứng dụng tùy chỉnh. Quan trọng hơn, bạn có thể làm phong phú các span được tạo tự động hoặc thủ công với các thuộc tính tùy chỉnh (còn được gọi là thẻ hoặc metadata). Các thuộc tính này có thể bao gồm dữ liệu cụ thể của doanh nghiệp, các tính toán trung gian hoặc bất kỳ ngữ cảnh nào có thể hữu ích cho việc gỡ lỗi hoặc phân tích, chẳng hạn như `user_id`, `session_id` hoặc `model_version`.

Ví dụ về cách tạo trace và span thủ công với [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Đánh Giá Tác Nhân

Khả năng quan sát cung cấp cho chúng ta các chỉ số, nhưng đánh giá là quá trình phân tích dữ liệu đó (và thực hiện các bài kiểm tra) để xác định tác nhân AI hoạt động tốt như thế nào và cách cải thiện nó. Nói cách khác, một khi bạn có các trace và chỉ số đó, làm thế nào để bạn sử dụng chúng để đánh giá tác nhân và đưa ra quyết định?

Việc đánh giá thường xuyên rất quan trọng vì các tác nhân AI thường không xác định và có thể tiến hóa (thông qua các bản cập nhật hoặc hành vi mô hình thay đổi) – nếu không có đánh giá, bạn sẽ không biết liệu "tác nhân thông minh" của mình có thực sự làm tốt công việc hay không hoặc liệu nó có bị suy giảm hiệu suất.

Có hai loại đánh giá cho các tác nhân AI: **đánh giá ngoại tuyến** và **đánh giá trực tuyến**. Cả hai đều có giá trị và bổ sung cho nhau. Chúng ta thường bắt đầu với đánh giá ngoại tuyến, vì đây là bước tối thiểu cần thiết trước khi triển khai bất kỳ tác nhân nào.

### Đánh Giá Ngoại Tuyến

![Các mục dữ liệu trong Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Điều này liên quan đến việc đánh giá tác nhân trong một môi trường được kiểm soát, thường sử dụng các tập dữ liệu thử nghiệm, không phải các truy vấn trực tiếp từ người dùng. Bạn sử dụng các tập dữ liệu được chọn lọc, nơi bạn biết đầu ra mong đợi hoặc hành vi đúng, và sau đó chạy tác nhân của bạn trên các tập dữ liệu đó.

Ví dụ, nếu bạn xây dựng một tác nhân giải bài toán từ ngữ toán học, bạn có thể có một [tập dữ liệu thử nghiệm](https://huggingface.co/datasets/gsm8k) gồm 100 bài toán với các câu trả lời đã biết. Đánh giá ngoại tuyến thường được thực hiện trong quá trình phát triển (và có thể là một phần của các pipeline CI/CD) để kiểm tra các cải tiến hoặc ngăn chặn sự suy giảm hiệu suất. Lợi ích là nó **có thể lặp lại và bạn có thể nhận được các chỉ số độ chính xác rõ ràng vì bạn có dữ liệu chuẩn**. Bạn cũng có thể mô phỏng các truy vấn của người dùng và đo lường các phản hồi của tác nhân so với các câu trả lời lý tưởng hoặc sử dụng các chỉ số tự động như đã mô tả ở trên.

Thách thức chính với đánh giá ngoại tuyến là đảm bảo tập dữ liệu thử nghiệm của bạn toàn diện và luôn phù hợp – tác nhân có thể hoạt động tốt trên một tập dữ liệu thử nghiệm cố định nhưng gặp phải các truy vấn rất khác nhau trong sản xuất. Do đó, bạn nên cập nhật các tập dữ liệu thử nghiệm với các trường hợp biên mới và các ví dụ phản ánh các kịch bản thực tế. Một sự kết hợp giữa các trường hợp "kiểm tra nhanh" nhỏ và các tập dữ liệu đánh giá lớn hơn là hữu ích: các tập nhỏ để kiểm tra nhanh và các tập lớn hơn để đo lường hiệu suất tổng thể.

### Đánh Giá Trực Tuyến

![Tổng quan về các chỉ số quan sát](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Điều này đề cập đến việc đánh giá tác nhân trong một môi trường thực tế, tức là trong quá trình sử dụng thực tế trong sản xuất. Đánh giá trực tuyến liên quan đến việc giám sát hiệu suất của tác nhân trên các tương tác thực tế của người dùng và phân tích kết quả liên tục.

Ví dụ, bạn có thể theo dõi tỷ lệ thành công, điểm hài lòng của người dùng hoặc các chỉ số khác trên lưu lượng truy cập trực tiếp. Lợi thế của đánh giá trực tuyến là nó **nắm bắt được những điều bạn có thể không dự đoán được trong môi trường phòng thí nghiệm** – bạn có thể quan sát sự thay đổi mô hình theo thời gian (nếu hiệu quả của tác nhân giảm khi các mẫu đầu vào thay đổi) và phát hiện các truy vấn hoặc tình huống bất ngờ không có trong dữ liệu thử nghiệm của bạn. Nó cung cấp một bức tranh thực sự về cách tác nhân hoạt động trong thực tế.

Đánh giá trực tuyến thường liên quan đến việc thu thập phản hồi ngầm định và rõ ràng từ người dùng, như đã thảo luận, và có thể chạy các thử nghiệm shadow hoặc A/B (nơi một phiên bản mới của tác nhân chạy song song để so sánh với phiên bản cũ). Thách thức là có thể khó để có được các nhãn hoặc điểm đáng tin cậy cho các tương tác trực tiếp – bạn có thể dựa vào phản hồi của người dùng hoặc các chỉ số hạ nguồn (như việc người dùng có nhấp vào kết quả hay không).

### Kết Hợp Cả Hai

Đánh giá trực tuyến và ngoại tuyến không loại trừ lẫn nhau; chúng bổ sung cho nhau rất tốt. Các thông tin chi tiết từ giám sát trực tuyến (ví dụ: các loại truy vấn mới của người dùng mà tác nhân hoạt động kém) có thể được sử dụng để bổ sung và cải thiện các tập dữ liệu thử nghiệm ngoại tuyến. Ngược lại, các tác nhân hoạt động tốt trong các bài kiểm tra ngoại tuyến có thể được triển khai và giám sát trực tuyến một cách tự tin hơn.

Trên thực tế, nhiều nhóm áp dụng một vòng lặp:

_đánh giá ngoại tuyến -> triển khai -> giám sát trực tuyến -> thu thập các trường hợp thất bại mới -> thêm vào tập dữ liệu ngoại tuyến -> tinh chỉnh tác nhân -> lặp lại_.

## Các Vấn Đề Thường Gặp

Khi bạn triển khai các tác nhân AI vào sản xuất, bạn có thể gặp phải nhiều thách thức khác nhau. Dưới đây là một số vấn đề phổ biến và các giải pháp tiềm năng:

| **Vấn Đề**    | **Giải Pháp Tiềm Năng**   |
| ------------- | ------------------ |
| Tác nhân AI không thực hiện nhiệm vụ một cách nhất quán | - Tinh chỉnh prompt được cung cấp cho tác nhân AI; làm rõ các mục tiêu.<br>- Xác định nơi việc chia nhiệm vụ thành các nhiệm vụ con và xử lý chúng bởi nhiều tác nhân có thể giúp ích. |
| Tác nhân AI rơi vào các vòng lặp liên tục  | - Đảm bảo bạn có các điều khoản và điều kiện kết thúc rõ ràng để tác nhân biết khi nào dừng quá trình.<br>- Đối với các nhiệm vụ phức tạp đòi hỏi lý luận và lập kế hoạch, sử dụng một mô hình lớn hơn chuyên về các nhiệm vụ lý luận. |
| Các lần gọi công cụ của tác nhân AI không hoạt động tốt   | - Kiểm tra và xác nhận đầu ra của công cụ bên ngoài hệ thống tác nhân. |

- Tinh chỉnh các tham số, lời nhắc và cách đặt tên công cụ đã được định nghĩa.  |
| Hệ thống đa tác nhân không hoạt động nhất quán | - Tinh chỉnh lời nhắc được cung cấp cho từng tác nhân để đảm bảo chúng cụ thể và khác biệt với nhau.<br>- Xây dựng một hệ thống phân cấp sử dụng một tác nhân "định tuyến" hoặc điều khiển để xác định tác nhân nào là phù hợp. |

Nhiều vấn đề trong số này có thể được xác định hiệu quả hơn khi có khả năng quan sát. Các dấu vết và số liệu mà chúng ta đã thảo luận trước đó giúp xác định chính xác vị trí trong quy trình làm việc của tác nhân xảy ra vấn đề, làm cho việc gỡ lỗi và tối ưu hóa trở nên hiệu quả hơn.

## Quản lý chi phí

Dưới đây là một số chiến lược để quản lý chi phí khi triển khai các tác nhân AI vào sản xuất:

**Sử dụng các mô hình nhỏ hơn:** Các Mô hình Ngôn ngữ Nhỏ (SLM) có thể hoạt động tốt trong một số trường hợp sử dụng tác nhân và sẽ giảm chi phí đáng kể. Như đã đề cập trước đó, xây dựng một hệ thống đánh giá để xác định và so sánh hiệu suất so với các mô hình lớn hơn là cách tốt nhất để hiểu SLM sẽ hoạt động tốt như thế nào trong trường hợp sử dụng của bạn. Hãy cân nhắc sử dụng SLM cho các nhiệm vụ đơn giản như phân loại ý định hoặc trích xuất tham số, trong khi dành các mô hình lớn hơn cho các nhiệm vụ suy luận phức tạp.

**Sử dụng Mô hình Định tuyến:** Một chiến lược tương tự là sử dụng đa dạng các mô hình với kích thước khác nhau. Bạn có thể sử dụng một LLM/SLM hoặc hàm serverless để định tuyến các yêu cầu dựa trên độ phức tạp đến các mô hình phù hợp nhất. Điều này cũng sẽ giúp giảm chi phí đồng thời đảm bảo hiệu suất cho các nhiệm vụ phù hợp. Ví dụ, định tuyến các truy vấn đơn giản đến các mô hình nhỏ hơn, nhanh hơn, và chỉ sử dụng các mô hình lớn, đắt đỏ cho các nhiệm vụ suy luận phức tạp.

**Lưu trữ phản hồi:** Xác định các yêu cầu và nhiệm vụ phổ biến và cung cấp phản hồi trước khi chúng đi qua hệ thống tác nhân của bạn là một cách tốt để giảm khối lượng các yêu cầu tương tự. Bạn thậm chí có thể triển khai một quy trình để xác định mức độ tương tự của một yêu cầu so với các yêu cầu đã được lưu trữ bằng cách sử dụng các mô hình AI cơ bản hơn. Chiến lược này có thể giảm đáng kể chi phí cho các câu hỏi thường gặp hoặc các quy trình làm việc phổ biến.

## Hãy xem cách điều này hoạt động trong thực tế

Trong [notebook ví dụ của phần này](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb), chúng ta sẽ xem các ví dụ về cách sử dụng các công cụ quan sát để giám sát và đánh giá tác nhân của mình.

## Bài học trước

[Mẫu thiết kế Siêu nhận thức](../09-metacognition/README.md)

## Bài học tiếp theo

[MCP](../11-mcp/README.md)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.