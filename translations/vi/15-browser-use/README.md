# Xây dựng các tác nhân sử dụng máy tính (CUA)

Các tác nhân sử dụng máy tính có thể tương tác với các trang web giống như con người: bằng cách mở trình duyệt, kiểm tra trang, và thực hiện hành động tốt nhất tiếp theo dựa trên những gì họ thấy. Trong bài học này, bạn sẽ xây dựng một tác nhân tự động hóa trình duyệt tìm kiếm Airbnb, trích xuất dữ liệu danh sách có cấu trúc, và xác định chỗ ở rẻ nhất tại Stockholm.

Bài học kết hợp Browser-Use để điều hướng theo trí tuệ nhân tạo, Playwright và Giao thức Chrome DevTools (CDP) để điều khiển trình duyệt, Azure OpenAI cho suy luận có hỗ trợ hình ảnh, và Pydantic để trích xuất có cấu trúc.

## Giới thiệu

Bài học này sẽ bao gồm:

- Hiểu khi nào tác nhân sử dụng máy tính phù hợp hơn so với tự động hóa chỉ API
- Kết hợp Browser-Use với Playwright và CDP để quản lý vòng đời trình duyệt đáng tin cậy
- Sử dụng Azure OpenAI với khả năng thị giác và đầu ra Pydantic có cấu trúc để trích xuất dữ liệu danh sách từ các trang web động
- Quyết định khi nào sử dụng quy trình tự động hóa trình duyệt ưu tiên tác nhân, ưu tiên diễn viên, hoặc kết hợp

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

- Cấu hình Browser-Use với Azure OpenAI và Playwright
- Xây dựng quy trình tự động hóa trình duyệt điều hướng một trang web thực và xử lý các yếu tố giao diện người dùng động
- Trích xuất kết quả có kiểu từ nội dung trang hiển thị và biến chúng thành logic kinh doanh phụ trợ
- Lựa chọn giữa mẫu tác nhân và mẫu diễn viên dựa trên mức độ dự đoán được của nhiệm vụ trình duyệt

## Mẫu mã nguồn

Bài học này bao gồm một tutorial notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Khởi chạy phiên Chrome qua CDP, tìm kiếm danh sách Airbnb cho Stockholm, trích xuất giá với thị giác Browser-Use, và trả về lựa chọn rẻ nhất dưới dạng dữ liệu có cấu trúc.

## Yêu cầu tiên quyết

- Python 3.12+
- Triển khai Azure OpenAI được cấu hình trong môi trường của bạn
- Đã cài đặt Chrome hoặc Chromium cục bộ
- Đã cài đặt các phụ thuộc Playwright
- Làm quen cơ bản với Python bất đồng bộ

## Cài đặt

Cài đặt các gói được sử dụng trong notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Thiết lập các biến môi trường Azure OpenAI được notebook sử dụng:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Tùy chọn: mặc định là phiên bản API mới nhất khi bỏ qua
AZURE_OPENAI_API_VERSION=...
```

## Tổng quan kiến trúc

Notebook minh họa một quy trình tự động hóa trình duyệt kết hợp:

1. Chrome khởi động với CDP được kích hoạt để cả Playwright và Browser-Use có thể chia sẻ cùng một phiên trình duyệt.
2. Tác nhân Browser-Use xử lý các nhiệm vụ điều hướng mở rộng như mở Airbnb, đóng các cửa sổ bật lên, và tìm kiếm Stockholm.
3. Trang hiện hoạt được kiểm tra với một sơ đồ Pydantic có cấu trúc để trích xuất tiêu đề danh sách, giá mỗi đêm, đánh giá, và URL.
4. Logic Python so sánh các danh sách đã trích xuất và làm nổi bật kết quả rẻ nhất.

Cách tiếp cận này duy trì khả năng suy luận linh hoạt dựa trên thị giác mà Browser-Use làm tốt trong khi vẫn cung cấp cho bạn kiểm soát trình duyệt có tính xác định khi bạn cần.

## Những điểm quan trọng và thực tiễn tốt nhất

### Khi nào dùng Agent và khi nào dùng Actor

| Tình huống | Dùng Agent | Dùng Actor |
|----------|------------|-----------|
| Bố cục động | Có, AI có thể thích ứng với thay đổi trang | Không, bộ chọn dễ bị phá vỡ |
| Cấu trúc đã biết | Không, agent chậm hơn kiểm soát trực tiếp | Có, nhanh và chính xác |
| Tìm phần tử | Có, ngôn ngữ tự nhiên hoạt động tốt | Không, yêu cầu bộ chọn chính xác |
| Kiểm soát thời gian | Không, ít dự đoán được | Có, kiểm soát hoàn toàn chờ đợi và thử lại |
| Quy trình phức tạp | Có, xử lý trạng thái UI không mong đợi | Không, cần phân nhánh rõ ràng |

### Thực tiễn tốt nhất cho Browser-Use

1. Bắt đầu với tác nhân cho khám phá và điều hướng động.
2. Chuyển sang kiểm soát trang trực tiếp khi tương tác trở nên có thể dự đoán.
3. Sử dụng các mô hình đầu ra có cấu trúc để dữ liệu trích xuất được xác thực và an toàn kiểu.
4. Thêm độ trễ một cách chiến lược sau các hành động kích hoạt thay đổi giao diện người dùng hiển thị.
5. Chụp ảnh màn hình trong quá trình lặp để lỗi dễ dàng gỡ lỗi hơn.
6. Mong đợi các trang web thay đổi và thiết kế các chiến lược dự phòng cho cửa sổ bật lên và thay đổi bố cục.
7. Kết hợp mẫu tác nhân và diễn viên để có cả tính linh hoạt và chính xác.

### Các biện pháp an toàn cho các tác nhân trình duyệt

Các tác nhân trình duyệt hoạt động trên các trang web trực tiếp, vì vậy chúng cần giới hạn nghiêm ngặt hơn so với script chỉ gọi API đã biết. Trước khi chuyển từ demo notebook sang quy trình làm việc thực tế, hãy xác định các kiểm soát về những gì tác nhân có thể xem, nhấp, và gửi.

1. **Xác định phạm vi môi trường duyệt web.** Chạy tác nhân trong cấu hình trình duyệt riêng biệt hoặc trong hộp cát, và giới hạn nó trong các miền cần thiết cho nhiệm vụ.
2. **Tách biệt quan sát và hành động.** Để tác nhân tìm kiếm, đọc, và trích xuất dữ liệu trước; yêu cầu bước phê duyệt rõ ràng trước khi gửi biểu mẫu, gửi tin nhắn, đặt chuyến đi, thực hiện mua hàng, xóa hồ sơ, hoặc thay đổi cài đặt tài khoản.
3. **Giữ bí mật không có trong lời nhắc và bản ghi.** Không đặt mật khẩu, thông tin thanh toán, cookie phiên, hoặc dữ liệu cá nhân thô trong bối cảnh mô hình. Để người dùng tiếp quản xác thực và loại bỏ các trường nhạy cảm khỏi nhật ký.
4. **Xem nội dung trang như đầu vào không tin cậy.** Một trang web có thể chứa hướng dẫn dành cho tác nhân, không phải người dùng. Tác nhân nên bỏ qua đoạn văn bản trang yêu cầu thay đổi mục tiêu, tiết lộ dữ liệu, tắt biện pháp kiểm soát, hoặc truy cập các trang không liên quan.
5. **Sử dụng kiểm tra xác định quanh các bước rủi ro.** Xác minh URL hiện tại, tiêu đề trang, mục được chọn, giá, người nhận, và tóm tắt hành động bằng mã trước khi yêu cầu người dùng phê duyệt bước cuối cùng.
6. **Đặt ngân sách và điều kiện dừng.** Giới hạn số hành động, số lần thử lại, số tab, và số phút tác nhân được phép sử dụng. Dừng lại khi trạng thái trang không rõ ràng thay vì tiếp tục nhấp.
7. **Ghi lại bằng chứng hữu ích, không phải tất cả mọi thứ.** Giữ tóm tắt hành động, dấu thời gian, URL, mô tả phần tử được chọn, và tham chiếu ảnh chụp màn hình để có thể xem xét lỗi mà không lưu trữ nội dung trang nhạy cảm không cần thiết.

Trong ví dụ Airbnb, mặc định an toàn là tìm kiếm danh sách và trích xuất giá. Đăng nhập, liên hệ chủ nhà, hoặc hoàn tất đặt phòng nên là hành động được người dùng phê duyệt riêng.

### Ứng dụng trong thực tế

- Đặt chuyến đi và theo dõi giá
- So sánh giá thương mại điện tử và kiểm tra tồn kho
- Trích xuất có cấu trúc từ các trang web động
- Kiểm thử và xác minh giao diện người dùng có hỗ trợ thị giác
- Giám sát và cảnh báo trang web
- Tự động điền biểu mẫu thông minh qua nhiều bước

## Ví dụ thực tế: Microsoft Project Opal

Tác nhân bạn xây dựng trong bài học này là phiên bản nhỏ, cục bộ của **tác nhân sử dụng máy tính (CUA)** — một chương trình điều khiển trình duyệt như con người. Microsoft đang mang ý tưởng này vào doanh nghiệp với **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, một tính năng trong Microsoft 365 Copilot.

Với Project Opal, bạn mô tả một nhiệm vụ và tác nhân làm việc thay bạn bằng **sử dụng máy tính trên một Windows 365 Cloud PC an toàn**, hoạt động trên các ứng dụng, trang web, và dữ liệu dựa trên trình duyệt trong tổ chức của bạn. Nó hoạt động **bất đồng bộ ở nền**, và bạn có thể hướng dẫn công việc hoặc kiểm soát bất cứ lúc nào. Các công việc mẫu bao gồm:

- Quản lý yêu cầu thành viên nhóm bảo mật
- Thu thập và xác thực bằng chứng kiểm toán cho đánh giá tuân thủ
- Phân loại sự cố IT (cập nhật trạng thái vé, phân công người phụ trách, đóng các vé trùng)
- Biên soạn dữ liệu Excel thành bộ trình bày báo cáo tài chính

Opal là tham chiếu hữu ích cho một tác nhân sử dụng máy tính **mức độ sản xuất, đáng tin cậy** — và củng cố các khái niệm từ các bài học trước:

| Khái niệm trong khóa học này | Cách Project Opal áp dụng |
|-----------------------------|-----------------------|
| **Con người tham gia quá trình** (Bài 06) | Opal tạm dừng để nhập thông tin đăng nhập, dữ liệu nhạy cảm hoặc hướng dẫn không rõ ràng, và không bao giờ nhập mật khẩu hay gửi biểu mẫu mà không có xác nhận rõ ràng. Bạn có thể *Kiểm soát* và *Trả lại quyền kiểm soát* giữa chừng. |
| **Tác nhân đáng tin cậy & an toàn** (Bài 06 & 18) | Chạy trong Windows 365 Cloud PC cách ly, mặc định chỉ dùng trình duyệt (chặn truy cập máy tính khác, thực thi qua Intune), sử dụng định danh *của bạn* để chỉ truy cập những gì bạn được phép, và ghi lại mọi hành động để kiểm toán. |
| **Lập kế hoạch & siêu nhận thức** (Bài 07 & 09) | Opal tạo kế hoạch cho công việc trước, rồi giám sát suy luận ở mỗi bước và tạm dừng nếu phát hiện hoạt động đáng ngờ. |
| **Khả năng/tài nguyên tái sử dụng** (Bài 04) | **Kỹ năng** cho phép bạn viết hướng dẫn cho các công việc lặp lại (nhập từ file `.md` hoặc tự tạo với Opal) và tái sử dụng chúng trong các cuộc hội thoại. |

> **Khả dụng:** Project Opal hiện được cung cấp cho người dùng trong [chương trình truy cập sớm Frontier](https://adoption.microsoft.com/copilot/frontier-program/) với gói Microsoft 365 Copilot, và quản trị viên của bạn phải hoàn thành cấu hình. Vì đây là tính năng thử nghiệm của Frontier, các tính năng có thể thay đổi theo thời gian.

## Kiểm tra kiến thức

Kiểm tra sự hiểu biết của bạn trước khi chuyển sang bài tiếp theo.

**1. Khi nào tác nhân sử dụng trình duyệt tốt hơn quy trình chỉ dùng API?**

<details>
<summary>Câu trả lời</summary>

Sử dụng tác nhân trình duyệt khi nhiệm vụ phụ thuộc vào những gì hiển thị trong giao diện web, trang không cung cấp API cần thiết, hoặc trang thay đổi đủ thường khiến logic API hoặc bộ chọn cứng trở nên dễ hỏng. Nếu có API ổn định cho cùng nhiệm vụ, nên ưu tiên API vì nó thường nhanh hơn, dễ kiểm thử, và dễ bảo mật hơn.
</details>

**2. Trong quy trình lai, phần nào nên do tác nhân xử lý và phần nào nên do mã Playwright trực tiếp xử lý?**

<details>
<summary>Câu trả lời</summary>

Để tác nhân xử lý điều hướng mở rộng và các trạng thái UI động, như tìm trang phù hợp hoặc đóng các cửa sổ bật lên không mong đợi. Chuyển sang điều khiển Playwright trực tiếp khi cấu trúc trang đã biết và hành động cần chính xác, thử lại, chờ đợi, hoặc xác nhận có tính xác định.
</details>

**3. Ví dụ Airbnb tìm một danh sách mà người dùng có thể muốn đặt. Điều gì nên xảy ra trước khi quy trình đăng nhập, liên hệ chủ nhà hoặc hoàn tất đặt phòng?**

<details>
<summary>Câu trả lời</summary>

Quy trình nên tạm dừng và yêu cầu sự phê duyệt rõ ràng từ người dùng. Trước khi hỏi, nó nên hiển thị tóm tắt rõ ràng của danh sách được chọn, URL hiện tại, giá, ngày tháng, và hành động dự định. Tìm kiếm và trích xuất giá có thể tự động; truy cập tài khoản, gửi tin nhắn, mua hàng, và đặt phòng nên được người dùng duyệt.
</details>

**4. Một trang web bảo tác nhân bỏ qua hướng dẫn ban đầu, truy cập trang khác, và tiết lộ dữ liệu xác thực đã lưu. Tác nhân nên xử lý văn bản đó thế nào?**

<details>
<summary>Câu trả lời</summary>

Xem đó như nội dung trang không đáng tin cậy, không phải là hướng dẫn từ nhà phát triển hay người dùng. Tác nhân nên ở trong phạm vi miền và nhiệm vụ cho phép, từ chối tiết lộ bí mật, và tránh theo văn bản trang thay đổi mục tiêu, vô hiệu hóa biện pháp kiểm soát, hoặc dẫn đến các trang không liên quan.
</details>

**5. Bằng chứng nào hữu ích cần giữ khi tác nhân trình duyệt chạy, và nên tránh gì?**

<details>
<summary>Câu trả lời</summary>

Giữ tóm tắt hành động, dấu thời gian, URL, mô tả phần tử được chọn, kết quả xác thực, và tham chiếu ảnh chụp màn hình để có thể xem xét hiệu suất chạy. Tránh lưu mật khẩu, thông tin thanh toán, cookie phiên, dữ liệu cá nhân thô, hoặc nội dung trang đầy đủ trừ khi có lý do về lưu trữ và bảo mật.
</details>

## Tài nguyên bổ sung

- [Bắt đầu với Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Mẫu tích hợp Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Tham số actor Browser-Use và trích xuất nội dung](https://docs.browser-use.com/customize/actor/all-parameters)
- [Thiết lập khóa học](../00-course-setup/README.md)

## Bài học trước

[Khám phá Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Bài học tiếp theo

[Triển khai tác nhân mở rộng](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->