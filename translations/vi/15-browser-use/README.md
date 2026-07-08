# Xây Dựng Đại Lý Sử Dụng Máy Tính (CUA)

Đại lý sử dụng máy tính có thể tương tác với các trang web giống như con người: bằng cách mở trình duyệt, kiểm tra trang, và thực hiện hành động tốt nhất tiếp theo dựa trên những gì họ thấy. Trong bài học này, bạn sẽ xây dựng một đại lý tự động trình duyệt tìm kiếm Airbnb, trích xuất dữ liệu danh sách có cấu trúc, và xác định chỗ ở rẻ nhất ở Stockholm.

Bài học kết hợp Browser-Use cho điều hướng dựa trên AI, Playwright và Giao thức DevTools Chrome (CDP) để điều khiển trình duyệt, Azure OpenAI để suy luận có hỗ trợ thị giác, và Pydantic để trích xuất có cấu trúc.

## Giới Thiệu

Bài học này sẽ đề cập:

- Hiểu khi nào đại lý sử dụng máy tính là phù hợp hơn so với tự động hóa chỉ dùng API
- Kết hợp Browser-Use với Playwright và CDP để quản lý vòng đời trình duyệt đáng tin cậy
- Sử dụng thị giác Azure OpenAI và đầu ra có cấu trúc từ Pydantic để trích xuất dữ liệu danh sách từ các trang web động
- Quyết định khi nào nên sử dụng quy trình tự động hóa trình duyệt ưu tiên đại lý, ưu tiên tác nhân, hoặc kết hợp hai cách

## Mục Tiêu Học Tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

- Cấu hình Browser-Use với Azure OpenAI và Playwright
- Xây dựng quy trình tự động hóa trình duyệt điều hướng một trang web thực và xử lý các phần tử UI động
- Trích xuất kết quả có kiểu từ nội dung trang hiển thị và biến chúng thành logic nghiệp vụ downstream
- Lựa chọn giữa mô hình đại lý và mô hình tác nhân dựa trên mức độ dự đoán của nhiệm vụ trình duyệt

## Mẫu Mã Code

Bài học này bao gồm một hướng dẫn notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Khởi chạy một phiên Chrome qua CDP, tìm kiếm danh sách Airbnb ở Stockholm, trích xuất giá với thị giác Browser-Use, và trả về lựa chọn rẻ nhất dưới dạng dữ liệu có cấu trúc.

## Yêu Cầu Trước

- Python 3.12+
- Triển khai Azure OpenAI được cấu hình trong môi trường của bạn
- Chrome hoặc Chromium được cài đặt cục bộ
- Các phụ thuộc Playwright được cài đặt
- Hiểu biết cơ bản về Python async

## Thiết Lập

Cài đặt các gói được sử dụng trong notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Thiết lập biến môi trường Azure OpenAI được notebook sử dụng:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Tùy chọn: mặc định là phiên bản API mới nhất khi bỏ qua
AZURE_OPENAI_API_VERSION=...
```

## Tổng Quan Kiến Trúc

Notebook trình bày quy trình tự động hóa trình duyệt kết hợp:

1. Chrome khởi động với CDP được bật để cả Playwright và Browser-Use có thể chia sẻ cùng một phiên trình duyệt.
2. Đại lý Browser-Use xử lý các nhiệm vụ điều hướng mở như mở Airbnb, đóng các cửa sổ bật lên, và tìm kiếm Stockholm.
3. Trang đang hoạt động được kiểm tra với một sơ đồ Pydantic có cấu trúc để trích xuất tiêu đề danh sách, giá mỗi đêm, đánh giá và URL.
4. Logic Python so sánh các danh sách trích xuất và làm nổi bật kết quả rẻ nhất.

Cách tiếp cận này giữ được khả năng suy luận linh hoạt dựa trên thị giác mà Browser-Use mạnh mẽ đồng thời cung cấp cho bạn kiểm soát trình duyệt có tính định hướng khi bạn cần.

## Những Điểm Chính và Thực Tiễn Tốt Nhất

### Khi Nào Nên Dùng Đại Lý so với Tác Nhân

| Kịch Bản | Dùng Đại Lý | Dùng Tác Nhân |
|----------|-----------|-----------|
| Bố cục động | Có, AI có thể thích nghi với thay đổi trang | Không, bộ chọn dễ bị hỏng |
| Cấu trúc đã biết | Không, đại lý chậm hơn điều khiển trực tiếp | Có, nhanh và chính xác |
| Tìm phần tử | Có, ngôn ngữ tự nhiên hoạt động tốt | Không, cần bộ chọn chính xác |
| Kiểm soát thời gian | Không, kém dự đoán hơn | Có, kiểm soát hoàn toàn chờ và thử lại |
| Quy trình phức tạp | Có, xử lý trạng thái UI không mong đợi | Không, cần phân nhánh rõ ràng |

### Thực Tiễn Tốt Nhất cho Browser-Use

1. Bắt đầu với đại lý để khám phá và điều hướng động.
2. Chuyển sang điều khiển trang trực tiếp khi tương tác trở nên có thể dự đoán.
3. Sử dụng các mô hình đầu ra có cấu trúc để dữ liệu trích xuất được xác thực và an toàn kiểu.
4. Thêm độ trễ có chiến lược sau các hành động kích hoạt thay đổi UI hiển thị.
5. Chụp ảnh màn hình trong quá trình lặp để dễ dàng gỡ lỗi khi lỗi xảy ra.
6. Mong đợi các trang web thay đổi và thiết kế các chiến lược dự phòng cho cửa sổ bật lên và chuyển đổi bố cục.
7. Kết hợp mô hình đại lý và tác nhân để có cả tính linh hoạt lẫn sự chính xác.

### Ứng Dụng Thực Tế

- Đặt phòng du lịch và giám sát giá cả
- So sánh giá và kiểm tra tình trạng hàng hóa thương mại điện tử
- Trích xuất có cấu trúc từ các trang web động
- Kiểm thử và xác minh UI có hỗ trợ thị giác
- Giám sát và cảnh báo trang web
- Tự động điền mẫu thông minh xuyên các quy trình nhiều bước

## Ví Dụ Thực Tế: Dự Án Microsoft Opal

Đại lý bạn xây dựng trong bài học này là một phiên bản nhỏ, cục bộ của một **đại lý sử dụng máy tính (CUA)** — một chương trình điều khiển trình duyệt giống như con người. Microsoft đang mang ý tưởng này vào doanh nghiệp với **[Dự Án Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, một tính năng trong Microsoft 365 Copilot.

Với Dự Án Opal, bạn mô tả một nhiệm vụ và đại lý sẽ làm việc thay bạn sử dụng **sử dụng máy tính trên Windows 365 Cloud PC an toàn**, vận hành trên các ứng dụng, trang web và dữ liệu dựa trên trình duyệt của tổ chức bạn. Nó hoạt động **bất đồng bộ ở chế độ nền**, và bạn có thể hướng dẫn công việc hoặc kiểm soát bất cứ lúc nào. Các công việc ví dụ bao gồm:

- Quản lý các yêu cầu thành viên nhóm bảo mật
- Thu thập và xác thực bằng chứng kiểm toán cho đánh giá tuân thủ
- Phân loại sự cố CNTT (cập nhật trạng thái vé, phân công người chịu trách nhiệm, đóng vé trùng)
- Tổng hợp dữ liệu Excel thành bộ tài liệu đóng tài chính

Opal là một tham chiếu hữu ích cho cách một đại lý sử dụng máy tính **cấp độ sản xuất, đáng tin cậy** trông như thế nào — và củng cố các khái niệm từ các bài học trước:

| Khái niệm trong khóa học này | Cách Dự Án Opal áp dụng |
|------------------------|-----------------------------|
| **Con người tham gia xử lý** (Bài học 06) | Opal tạm dừng để nhập thông tin đăng nhập, dữ liệu nhạy cảm, hoặc hướng dẫn không rõ ràng, và không bao giờ nhập mật khẩu hay gửi mẫu mà không có xác nhận rõ ràng. Bạn có thể *Kiểm Soát* và *Trả Lại Kiểm Soát* giữa chừng nhiệm vụ. |
| **Đại lý đáng tin cậy & an toàn** (Bài 06 & 18) | Chạy trong một Windows 365 Cloud PC cô lập, mặc định chỉ dùng trình duyệt (chặn truy cập máy tính khác, quản lý qua Intune), dùng danh tính *của bạn* nên chỉ truy cập những gì bạn được phép, và ghi nhật ký mọi hành động để kiểm toán. |
| **Lập kế hoạch & siêu nhận thức** (Bài 07 & 09) | Opal tạo kế hoạch cho công việc trước, sau đó tự giám sát suy luận ở từng bước và dừng nếu phát hiện hoạt động đáng ngờ. |
| **Khả năng / công cụ tái sử dụng** (Bài 04) | **Kỹ năng** cho phép bạn viết hướng dẫn cho các công việc lặp lại (nhập từ file `.md` hoặc tạo với Opal) và tái sử dụng chúng qua các cuộc trò chuyện. |

> **Khả dụng:** Dự Án Opal hiện có sẵn cho người dùng trong [chương trình truy cập sớm Frontier](https://adoption.microsoft.com/copilot/frontier-program/) với đăng ký Microsoft 365 Copilot, và quản trị viên của bạn phải hoàn thành thiết lập. Vì đây là tính năng thử nghiệm của Frontier, khả năng có thể thay đổi theo thời gian.

## Tài Nguyên Bổ Sung

- [Bắt đầu với Dự Án Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Mẫu tích hợp Browser-Use với Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Tham số tác nhân Browser-Use và trích xuất nội dung](https://docs.browser-use.com/customize/actor/all-parameters)
- [Thiết Lập Khóa Học](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->