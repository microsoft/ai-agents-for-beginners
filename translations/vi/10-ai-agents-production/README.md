# Tác nhân AI trong Sản xuất: Khả năng Quan sát & Đánh giá

[![Tác nhân AI trong Sản xuất](../../../translated_images/vi/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Khi các tác nhân AI chuyển từ nguyên mẫu thí nghiệm sang ứng dụng thực tế, khả năng hiểu hành vi của chúng, giám sát hiệu suất và đánh giá kết quả một cách có hệ thống trở nên quan trọng.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết/hiểu:
- Các khái niệm cốt lõi về khả năng quan sát và đánh giá tác nhân
- Kỹ thuật cải thiện hiệu suất, chi phí và hiệu quả của tác nhân
- Cái gì và cách thức đánh giá tác nhân AI của bạn một cách có hệ thống
- Cách kiểm soát chi phí khi triển khai tác nhân AI vào sản xuất
- Cách chèn công cụ đo lường cho tác nhân được xây dựng bằng Microsoft Agent Framework

Mục tiêu là trang bị cho bạn kiến thức để biến các tác nhân "hộp đen" thành các hệ thống minh bạch, dễ quản lý và đáng tin cậy.

_**Lưu ý:** Điều quan trọng là triển khai các Tác nhân AI an toàn và đáng tin cậy. Xem thêm bài học [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md)._

## Traces và Spans

Các công cụ khả năng quan sát như [Langfuse](https://langfuse.com/) hoặc [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) thường biểu diễn các lần chạy tác nhân dưới dạng traces và spans.

- **Trace** đại diện cho một nhiệm vụ tác nhân hoàn chỉnh từ đầu đến cuối (ví dụ như xử lý một truy vấn người dùng).
- **Spans** là các bước riêng lẻ trong trace (ví dụ gọi một mô hình ngôn ngữ hoặc truy xuất dữ liệu).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Không có khả năng quan sát, một tác nhân AI có thể cảm thấy như một "hộp đen" - trạng thái nội bộ và lý luận của nó không rõ ràng, khiến việc chẩn đoán sự cố hoặc tối ưu hóa hiệu suất khó khăn. Với khả năng quan sát, các tác nhân trở thành "hộp kính", mang lại tính minh bạch cần thiết để xây dựng lòng tin và đảm bảo chúng hoạt động như mong đợi.

## Tại sao Khả năng Quan sát quan trọng trong Môi trường Sản xuất

Chuyển đổi các tác nhân AI sang môi trường sản xuất giới thiệu một loạt thách thức và yêu cầu mới. Khả năng quan sát không còn là điều "hay có" mà là một năng lực then chốt:

*   **Gỡ lỗi và Phân tích Nguyên nhân Gốc rễ**: Khi một tác nhân lỗi hoặc tạo ra kết quả không mong đợi, các công cụ quan sát cung cấp các trace cần thiết để xác định nguồn gốc của lỗi. Điều này đặc biệt quan trọng trong các tác nhân phức tạp có thể liên quan đến nhiều lần gọi LLM, tương tác công cụ và logic điều kiện.
*   **Quản lý Độ trễ và Chi phí**: Các tác nhân AI thường phụ thuộc vào LLM và các API bên ngoài được tính phí theo token hoặc theo lần gọi. Khả năng quan sát cho phép theo dõi chính xác các lần gọi này, giúp xác định các thao tác chậm hoặc tốn kém quá mức. Điều này giúp nhóm tối ưu hóa prompt, chọn mô hình hiệu quả hơn hoặc thiết kế lại quy trình để quản lý chi phí vận hành và đảm bảo trải nghiệm người dùng tốt.
*   **Tin cậy, An toàn và Tuân thủ**: Trong nhiều ứng dụng, quan trọng là đảm bảo tác nhân hoạt động an toàn và có đạo đức. Khả năng quan sát cung cấp một dấu vết kiểm toán về hành động và quyết định của tác nhân. Điều này có thể dùng để phát hiện và giảm thiểu các vấn đề như prompt injection, sinh nội dung gây hại, hoặc xử lý sai thông tin cá nhân (PII). Ví dụ, bạn có thể xem lại traces để hiểu tại sao tác nhân cung cấp phản hồi nhất định hoặc sử dụng một công cụ cụ thể.
*   **Vòng lặp Cải tiến Liên tục**: Dữ liệu quan sát là nền tảng của quy trình phát triển lặp đi lặp lại. Bằng cách giám sát cách tác nhân hoạt động trong thực tế, các nhóm có thể xác định khu vực cần cải thiện, thu thập dữ liệu để tinh chỉnh mô hình và xác thực tác động của các thay đổi. Điều này tạo ra một vòng phản hồi nơi các thông tin từ đánh giá trực tuyến trong sản xuất sẽ thông báo cho các thử nghiệm và tinh chỉnh ngoại tuyến, dẫn đến hiệu suất tác nhân ngày càng tốt hơn.

## Các chỉ số chính cần theo dõi

Để giám sát và hiểu hành vi tác nhân, cần theo dõi một loạt chỉ số và tín hiệu. Mặc dù các chỉ số cụ thể có thể khác nhau tùy mục đích của tác nhân, một số chỉ số là quan trọng phổ quát.

Dưới đây là một số chỉ số phổ biến mà các công cụ quan sát theo dõi:

**Độ trễ (Latency):** Tác nhân phản hồi nhanh thế nào? Thời gian chờ dài ảnh hưởng tiêu cực đến trải nghiệm người dùng. Bạn nên đo độ trễ cho các tác vụ và các bước riêng lẻ bằng cách trace các lần chạy tác nhân. Ví dụ, một tác nhân mất 20 giây cho tất cả các lần gọi mô hình có thể được tăng tốc bằng cách sử dụng mô hình nhanh hơn hoặc gọi các mô hình song song.

**Chi phí:** Chi phí trên mỗi lần chạy tác nhân là bao nhiêu? Các tác nhân AI dựa vào các lần gọi LLM tính phí theo token hoặc các API bên ngoài. Việc sử dụng công cụ thường xuyên hoặc nhiều prompt có thể nhanh chóng tăng chi phí. Ví dụ, nếu một tác nhân gọi LLM năm lần để cải thiện chất lượng chỉ chút ít, bạn cần đánh giá liệu chi phí có xứng đáng hay có thể giảm số lần gọi hoặc dùng mô hình rẻ hơn. Giám sát thời gian thực cũng có thể giúp phát hiện các đột biến bất ngờ (ví dụ: lỗi gây vòng lặp API quá mức).

**Lỗi Yêu cầu (Request Errors):** Có bao nhiêu yêu cầu mà tác nhân thất bại? Điều này có thể bao gồm lỗi API hoặc cuộc gọi công cụ thất bại. Để làm cho tác nhân bền hơn khi vào sản xuất, bạn có thể thiết lập các phương án dự phòng hoặc thử lại. Ví dụ nếu nhà cung cấp LLM A bị lỗi, bạn chuyển sang nhà cung cấp LLM B làm dự phòng.

**Phản hồi Người dùng:** Thực hiện đánh giá trực tiếp từ người dùng cung cấp những hiểu biết quý giá. Điều này có thể bao gồm xếp hạng rõ ràng (👍thumbs-up/👎down, ⭐1-5 sao) hoặc nhận xét bằng văn bản. Phản hồi tiêu cực liên tục nên cảnh báo bạn vì đó là dấu hiệu rằng tác nhân không hoạt động như mong đợi.

**Phản hồi Người dùng Ngầm (Implicit User Feedback):** Hành vi người dùng cung cấp phản hồi gián tiếp ngay cả khi không có xếp hạng rõ ràng. Điều này có thể bao gồm việc người dùng ngay lập tức sửa lại câu hỏi, lặp lại truy vấn hoặc bấm nút thử lại. Ví dụ, nếu bạn thấy người dùng liên tục hỏi cùng một câu, đó là dấu hiệu tác nhân không hoạt động như mong đợi.

**Độ chính xác (Accuracy):** Tác nhân tạo ra đầu ra chính xác hoặc mong muốn bao nhiêu phần trăm? Định nghĩa độ chính xác thay đổi (ví dụ, đúng trong giải quyết bài toán, độ chính xác truy xuất thông tin, sự hài lòng của người dùng). Bước đầu tiên là xác định thành công trông như thế nào đối với tác nhân của bạn. Bạn có thể theo dõi độ chính xác qua kiểm tra tự động, điểm số đánh giá hoặc nhãn hoàn thành nhiệm vụ. Ví dụ, gắn nhãn traces là "succeeded" hoặc "failed".

**Các Chỉ số Đánh giá Tự động:** Bạn cũng có thể thiết lập đánh giá tự động. Ví dụ, bạn có thể dùng một LLM để chấm đầu ra của tác nhân, ví dụ nó có hữu ích, chính xác hay không. Cũng có một số thư viện mã nguồn mở giúp bạn chấm các khía cạnh khác nhau của tác nhân. Ví dụ [RAGAS](https://docs.ragas.io/) cho các tác nhân RAG hoặc [LLM Guard](https://llm-guard.com/) để phát hiện ngôn ngữ có hại hoặc prompt injection.

Trong thực tế, sự kết hợp của các chỉ số này cung cấp phạm vi bao phủ tốt nhất về sức khỏe của tác nhân AI. Trong ví dụ sổ notebook của chương này [example notebook](./code_samples/10-expense_claim-demo.ipynb), chúng tôi sẽ chỉ cho bạn cách các chỉ số này trông như thế nào trong các ví dụ thực tế nhưng trước tiên, chúng ta sẽ tìm hiểu quy trình đánh giá điển hình trông như thế nào.

## Chèn công cụ đo lường cho Tác nhân của bạn

Để thu thập dữ liệu trace, bạn cần chèn công cụ đo lường vào mã của mình. Mục tiêu là chèn mã vào tác nhân để phát ra traces và metrics có thể được một nền tảng quan sát thu lại, xử lý và trực quan hóa.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) đã trở thành tiêu chuẩn ngành cho khả năng quan sát LLM. Nó cung cấp một tập API, SDK và công cụ để tạo, thu thập và xuất dữ liệu telemetri.

Có nhiều thư viện chèn công cụ (instrumentation) bao bọc các framework tác nhân hiện có và giúp dễ dàng xuất OpenTelemetry spans tới một công cụ quan sát. Microsoft Agent Framework tích hợp với OpenTelemetry một cách bản địa. Dưới đây là một ví dụ về việc chèn đo lường cho một tác nhân MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Việc thực thi tác nhân được theo dõi tự động
    pass
```

Sổ notebook ví dụ [example notebook](./code_samples/10-expense_claim-demo.ipynb) trong chương này sẽ minh họa cách chèn công cụ đo lường cho tác nhân MAF của bạn.

**Tạo Span Thủ công:** Mặc dù các thư viện chèn công cụ cung cấp một nền tảng tốt, thường có các trường hợp cần thông tin chi tiết hơn hoặc tuỳ chỉnh. Bạn có thể tạo spans thủ công để thêm logic ứng dụng tuỳ chỉnh. Quan trọng hơn, bạn có thể làm giàu các spans được tạo tự động hoặc thủ công bằng các thuộc tính tuỳ chỉnh (còn gọi là tag hoặc metadata). Các thuộc tính này có thể bao gồm dữ liệu theo nghiệp vụ, phép tính trung gian, hoặc bất kỳ ngữ cảnh nào hữu ích cho gỡ lỗi hoặc phân tích, chẳng hạn như `user_id`, `session_id`, hoặc `model_version`.

Ví dụ về việc tạo traces và spans thủ công với [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Đánh giá Tác nhân

Khả năng quan sát cung cấp cho chúng ta các chỉ số, nhưng đánh giá là quá trình phân tích dữ liệu đó (và thực hiện các bài kiểm tra) để xác định tác nhân AI hoạt động tốt như thế nào và có thể được cải thiện ra sao. Nói cách khác, khi bạn có các traces và metrics đó, bạn dùng chúng như thế nào để đánh giá tác nhân và đưa ra quyết định?

Đánh giá thường xuyên là quan trọng vì các tác nhân AI thường không tuyến tính và có thể tiến hóa (thông qua cập nhật hoặc sự dịch chuyển hành vi mô hình) – nếu không đánh giá, bạn sẽ không biết liệu "tác nhân thông minh" của mình có thực sự làm tốt công việc hay đã bị suy giảm.

Có hai loại đánh giá cho tác nhân AI: **đánh giá trực tuyến (online evaluation)** và **đánh giá ngoại tuyến (offline evaluation)**. Cả hai đều có giá trị và bổ sung cho nhau. Thông thường chúng ta bắt đầu với đánh giá ngoại tuyến, vì đây là bước tối thiểu cần thiết trước khi triển khai bất kỳ tác nhân nào.

### Đánh giá Ngoại tuyến

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Điều này bao gồm đánh giá tác nhân trong môi trường kiểm soát, thường sử dụng bộ dữ liệu thử nghiệm, không phải truy vấn người dùng thực tế. Bạn sử dụng các bộ dữ liệu được tuyển chọn nơi bạn biết đầu ra mong đợi hoặc hành vi đúng, sau đó chạy tác nhân trên những dữ liệu đó.

Ví dụ, nếu bạn xây dựng một tác nhân giải bài toán lời văn toán học, bạn có thể có một [test dataset](https://huggingface.co/datasets/gsm8k) gồm 100 bài toán với đáp án đã biết. Đánh giá ngoại tuyến thường được thực hiện trong quá trình phát triển (và có thể là một phần của pipeline CI/CD) để kiểm tra cải tiến hoặc phòng ngừa suy giảm. Lợi ích là nó **có thể lặp lại và bạn có thể có các chỉ số độ chính xác rõ ràng vì bạn có ground truth**. Bạn cũng có thể mô phỏng các truy vấn người dùng và đo phản hồi của tác nhân so với câu trả lời lý tưởng hoặc sử dụng các chỉ số tự động như đã mô tả ở trên.

Thách thức chính với đánh giá ngoại tuyến là đảm bảo bộ dữ liệu thử nghiệm của bạn toàn diện và luôn phù hợp – tác nhân có thể hoạt động tốt trên một tập kiểm tra cố định nhưng gặp các truy vấn rất khác trong sản xuất. Do đó, bạn nên cập nhật bộ test với các trường hợp biên và ví dụ mới phản ánh kịch bản thực tế. Một sự kết hợp giữa các bộ “smoke test” nhỏ và các bộ đánh giá lớn hơn là hữu ích: các bộ nhỏ để kiểm tra nhanh và các bộ lớn hơn cho các chỉ số hiệu suất rộng hơn.

### Đánh giá Trực tuyến

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Điều này đề cập đến việc đánh giá tác nhân trong môi trường thực tế, tức là trong quá trình sử dụng thực tế trong sản xuất. Đánh giá trực tuyến bao gồm giám sát hiệu suất tác nhân trên các tương tác người dùng thực và phân tích kết quả liên tục.

Ví dụ, bạn có thể theo dõi tỷ lệ thành công, điểm hài lòng của người dùng hoặc các chỉ số khác trên lưu lượng thực. Lợi thế của đánh giá trực tuyến là nó **bắt được những điều bạn có thể không dự đoán được trong môi trường phòng thí nghiệm** – bạn có thể quan sát sự dịch chuyển mô hình theo thời gian (nếu hiệu quả của tác nhân giảm khi mẫu đầu vào thay đổi) và bắt các truy vấn hoặc tình huống bất ngờ không có trong dữ liệu thử nghiệm. Nó cung cấp bức tranh thực sự về cách tác nhân hành xử ngoài thực tế.

Đánh giá trực tuyến thường bao gồm thu thập phản hồi ngầm và rõ ràng của người dùng, như đã thảo luận, và có thể chạy các bài thử shadow hoặc thử nghiệm A/B (nơi phiên bản mới của tác nhân chạy song song để so sánh với phiên bản cũ). Thách thức là có thể khó có được nhãn hoặc điểm số đáng tin cậy cho các tương tác trực tiếp – bạn có thể dựa vào phản hồi người dùng hoặc các chỉ số hạ nguồn (ví dụ người dùng có bấm vào kết quả hay không).

### Kết hợp cả hai

Đánh giá trực tuyến và ngoại tuyến không loại trừ lẫn nhau; chúng bổ sung cho nhau rất nhiều. Những thông tin từ giám sát trực tuyến (ví dụ các loại truy vấn người dùng mới mà tác nhân thực hiện kém) có thể được dùng để mở rộng và cải thiện bộ dữ liệu thử nghiệm ngoại tuyến. Ngược lại, các tác nhân hoạt động tốt trong kiểm tra ngoại tuyến sau đó có thể được triển khai và giám sát trực tuyến với độ tin cậy cao hơn.

Thực tế, nhiều nhóm áp dụng một vòng:

_đánh giá ngoại tuyến -> triển khai -> giám sát trực tuyến -> thu thập các trường hợp thất bại mới -> thêm vào bộ dữ liệu ngoại tuyến -> tinh chỉnh tác nhân -> lặp lại_.

## Các Vấn đề Thường Gặp

Khi bạn triển khai tác nhân AI vào sản xuất, bạn có thể gặp nhiều thách thức khác nhau. Dưới đây là một số vấn đề phổ biến và các giải pháp tiềm năng:

| **Issue**    | **Potential Solution**   |
| ------------- | ------------------ |
| AI Agent not performing tasks consistently | - Refine the prompt given to the AI Agent; be clear on objectives.<br>- Identify where dividing the tasks into subtasks and handling them by multiple agents can help. |
| AI Agent running into continuous loops  | - Ensure you have clear termination terms and conditions so the Agent knows when to stop the process.<br>- For complex tasks that require reasoning and planning, use a larger model that is specialized for reasoning tasks. |
| AI Agent tool calls are not performing well   | - Test and validate the tool's output outside of the agent system.<br>- Refine the defined parameters, prompts, and naming of tools.  |
| Multi-Agent system not performing consistently | - Refine prompts given to each agent to ensure they are specific and distinct from one another.<br>- Build a hierarchical system using a "routing" or controller agent to determine which agent is the correct one. |

Nhiều vấn đề trong số này có thể được xác định hiệu quả hơn khi có khả năng quan sát. Các traces và metrics đã thảo luận ở trên giúp xác định chính xác nơi trong quy trình tác nhân xảy ra vấn đề, làm cho việc gỡ lỗi và tối ưu hóa hiệu quả hơn nhiều.

## Quản lý Chi phí
Dưới đây là một số chiến lược để quản lý chi phí khi triển khai các tác nhân AI vào môi trường sản xuất:

**Sử dụng Mô hình Nhỏ hơn:** Mô hình ngôn ngữ nhỏ (SLMs) có thể hoạt động tốt trong một số trường hợp sử dụng mang tính tác nhân và sẽ giảm chi phí đáng kể. Như đã đề cập trước đó, xây dựng một hệ thống đánh giá để xác định và so sánh hiệu suất so với các mô hình lớn hơn là cách tốt nhất để hiểu SLM sẽ hoạt động như thế nào với trường hợp sử dụng của bạn. Hãy cân nhắc sử dụng SLMs cho các nhiệm vụ đơn giản hơn như phân loại ý định hoặc trích xuất tham số, trong khi dành các mô hình lớn hơn cho những nhiệm vụ suy luận phức tạp.

**Sử dụng Mô hình Định tuyến:** Một chiến lược tương tự là sử dụng đa dạng các mô hình và kích cỡ. Bạn có thể dùng LLM/SLM hoặc hàm serverless để định tuyến các yêu cầu dựa trên độ phức tạp tới các mô hình phù hợp nhất. Điều này cũng sẽ giúp giảm chi phí đồng thời đảm bảo hiệu suất cho các nhiệm vụ phù hợp. Ví dụ, định tuyến các truy vấn đơn giản tới các mô hình nhỏ hơn, nhanh hơn, và chỉ sử dụng các mô hình lớn, đắt tiền cho các nhiệm vụ suy luận phức tạp.

**Bộ nhớ đệm phản hồi:** Xác định các yêu cầu và nhiệm vụ phổ biến và cung cấp các phản hồi trước khi chúng đi qua hệ thống tác nhân của bạn là một cách tốt để giảm khối lượng các yêu cầu tương tự. Bạn thậm chí có thể triển khai một luồng để xác định mức độ tương đồng của một yêu cầu với các yêu cầu đã được lưu trong bộ nhớ đệm bằng cách sử dụng các mô hình AI cơ bản hơn. Chiến lược này có thể giảm đáng kể chi phí cho các câu hỏi thường gặp hoặc các quy trình làm việc phổ biến.

## Hãy xem cách điều này hoạt động trong thực tế

Trong [notebook ví dụ của phần này](./code_samples/10-expense_claim-demo.ipynb), chúng ta sẽ thấy các ví dụ về cách chúng ta có thể sử dụng các công cụ quan sát để giám sát và đánh giá tác nhân của mình.

### Còn câu hỏi nào về các tác nhân AI trong môi trường sản xuất không?

Tham gia [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) để gặp gỡ những người học khác, tham dự giờ trao đổi và nhận câu trả lời cho các câu hỏi về Tác nhân AI của bạn.

## Bài học trước

[Mẫu Thiết kế Siêu nhận thức](../09-metacognition/README.md)

## Bài học tiếp theo

[Giao thức tác nhân](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Miễn trừ trách nhiệm:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa sai sót hoặc thông tin không chính xác. Văn bản gốc bằng ngôn ngữ gốc nên được coi là nguồn chính thức. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->