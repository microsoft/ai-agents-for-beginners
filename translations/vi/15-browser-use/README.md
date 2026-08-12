# Xây dựng đại lý sử dụng máy tính (CUA)

Đại lý sử dụng máy tính có thể tương tác với các trang web giống như một người: bằng cách mở trình duyệt, kiểm tra trang và thực hiện hành động tốt nhất tiếp theo dựa trên những gì họ thấy. Trong bài học này, bạn sẽ xây dựng một đại lý tự động hóa trình duyệt tìm kiếm Airbnb, trích xuất dữ liệu danh sách có cấu trúc và xác định chỗ ở rẻ nhất tại Stockholm.

Bài học kết hợp Browser-Use cho điều hướng dựa trên AI, Playwright và Chrome DevTools Protocol (CDP) để điều khiển trình duyệt, Azure OpenAI cho lý luận hỗ trợ thị giác, và Pydantic để trích xuất có cấu trúc.

## Giới thiệu

Bài học này sẽ bao gồm:

- Hiểu khi nào đại lý sử dụng máy tính phù hợp hơn tự động hóa chỉ dựa trên API
- Kết hợp Browser-Use với Playwright và CDP để quản lý vòng đời trình duyệt đáng tin cậy
- Sử dụng thị giác Azure OpenAI và đầu ra có cấu trúc Pydantic để trích xuất dữ liệu danh sách từ các trang web động
- Quyết định khi nào sử dụng quy trình tự động hóa trình duyệt theo kiểu đại lý trước, người thực hiện trước hoặc kết hợp

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ biết cách:

- Cấu hình Browser-Use với Azure OpenAI và Playwright
- Xây dựng quy trình tự động hóa trình duyệt để điều hướng trang web thực và xử lý các phần tử giao diện người dùng động
- Trích xuất kết quả kiểu dữ liệu từ nội dung trang hiển thị và chuyển chúng thành logic nghiệp vụ tiếp theo
- Chọn giữa mô hình đại lý và người thực hiện dựa trên tính dự đoán của tác vụ trình duyệt

## Mẫu mã nguồn

Bài học này bao gồm một bài hướng dẫn notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Khởi chạy phiên Chrome qua CDP, tìm kiếm các danh sách tại Stockholm trên Airbnb, trích xuất giá với thị giác Browser-Use, và trả về lựa chọn rẻ nhất dưới dạng dữ liệu có cấu trúc.

## Yêu cầu tiên quyết

- Python 3.12+
- Triển khai Azure OpenAI đã cấu hình trong môi trường của bạn
- Cài đặt Chrome hoặc Chromium trên máy cục bộ
- Cài đặt các phụ thuộc Playwright
- Hiểu biết cơ bản về Python bất đồng bộ

## Thiết lập

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

## Tổng quan Kiến trúc

Notebook trình bày một quy trình tự động hóa trình duyệt kết hợp:

1. Chrome khởi động với CDP được bật để cả Playwright và Browser-Use có thể chia sẻ cùng một phiên trình duyệt.
2. Đại lý Browser-Use xử lý các nhiệm vụ điều hướng mở như mở Airbnb, đóng các cửa sổ pop-up, và tìm kiếm Stockholm.
3. Trang đang hoạt động được kiểm tra bằng sơ đồ Pydantic có cấu trúc để trích xuất tiêu đề danh sách, giá theo đêm, đánh giá và URL.
4. Logic Python so sánh các danh sách đã trích xuất và làm nổi bật kết quả rẻ nhất.

Cách tiếp cận này giúp giữ được khả năng lý luận dựa trên thị giác linh hoạt mà Browser-Use mạnh mẽ đồng thời vẫn cho phép bạn kiểm soát trình duyệt một cách xác định khi cần.

## Những điểm quan trọng và thực hành tốt nhất

### Khi nào nên dùng Đại lý và khi nào nên dùng Người thực hiện

| Tình huống | Dùng Đại lý | Dùng Người thực hiện |
|----------|-----------|-----------|
| Bố cục động | Có, AI có thể thích nghi với thay đổi trang | Không, bộ chọn dễ gãy |
| Cấu trúc biết trước | Không, đại lý chậm hơn điều khiển trực tiếp | Có, nhanh và chính xác |
| Tìm kiếm phần tử | Có, ngôn ngữ tự nhiên hoạt động tốt | Không, cần bộ chọn chính xác |
| Kiểm soát thời gian | Không, kém dự đoán hơn | Có, toàn quyền kiểm soát chờ và thử lại |
| Quy trình phức tạp | Có, xử lý trạng thái UI bất ngờ | Không, cần phân nhánh rõ ràng |

### Thực hành tốt nhất với Browser-Use

1. Bắt đầu với đại lý để khám phá và điều hướng động.
2. Chuyển sang điều khiển trang trực tiếp khi tương tác trở nên dễ dự đoán.
3. Sử dụng mô hình đầu ra có cấu trúc để dữ liệu trích xuất được xác thực và an toàn kiểu dữ liệu.
4. Thêm các khoảng dừng chiến lược sau các hành động gây thay đổi UI rõ ràng.
5. Chụp ảnh màn hình trong quá trình lặp để dễ dàng gỡ lỗi khi thất bại.
6. Dự đoán trang web sẽ thay đổi và thiết kế chiến lược dự phòng cho pop-up và thay đổi bố cục.
7. Kết hợp mô hình đại lý và người thực hiện để có cả sự linh hoạt và chính xác.

### Hàng rào an toàn cho đại lý trình duyệt

Đại lý trình duyệt hoạt động trên các trang web trực tiếp, vì vậy chúng cần giới hạn chặt chẽ hơn một tập lệnh chỉ gọi API đã biết. Trước khi chuyển từ demo notebook sang quy trình thực tế, hãy định nghĩa các kiểm soát về những gì đại lý có thể xem, nhấp và gửi.

1. **Phạm vi môi trường duyệt.** Chạy đại lý trong hồ sơ trình duyệt riêng biệt hoặc hộp cát, và giới hạn nó vào các miền cần thiết cho nhiệm vụ.
2. **Tách quan sát khỏi hành động.** Cho đại lý tìm kiếm, đọc và trích xuất dữ liệu trước; yêu cầu sự phê duyệt rõ ràng trước khi nó gửi biểu mẫu, gửi tin nhắn, đặt chuyến đi, mua hàng, xóa hồ sơ hoặc thay đổi cài đặt tài khoản.
3. **Giữ bí mật tránh khỏi lời nhắc và bản ghi.** Không đặt mật khẩu, thông tin thanh toán, cookie phiên hoặc dữ liệu cá nhân thô trong ngữ cảnh mô hình. Hãy để người dùng kiểm soát xác thực và biên tập các trường nhạy cảm khỏi nhật ký.
4. **Xem nội dung trang như đầu vào không đáng tin cậy.** Một trang web có thể chứa chỉ dẫn dành cho đại lý, không phải cho người dùng. Đại lý nên bỏ qua văn bản trang yêu cầu thay đổi mục tiêu, tiết lộ dữ liệu, vô hiệu hóa bảo vệ hoặc truy cập các trang không liên quan.
5. **Dùng kiểm tra xác định quanh các bước rủi ro.** Xác minh URL hiện tại, tiêu đề trang, mục được chọn, giá, người nhận và tóm tắt hành động bằng mã trước khi yêu cầu người dùng phê duyệt bước cuối.
6. **Đặt ngân sách và điều kiện dừng.** Giới hạn số hành động, số lần thử lại, số tab và thời gian sử dụng của đại lý. Dừng khi trạng thái trang không rõ thay vì tiếp tục nhấp.
7. **Ghi lại bằng chứng hữu ích, không phải tất cả mọi thứ.** Giữ tóm tắt hành động, dấu thời gian, URL, mô tả phần tử được chọn và tham chiếu ảnh chụp màn hình để có thể xem lại lỗi mà không lưu nội dung trang nhạy cảm không cần thiết.

Trong ví dụ Airbnb, mặc định an toàn là tìm kiếm danh sách và trích xuất giá. Đăng nhập, liên hệ chủ nhà hoặc hoàn tất đặt phòng nên là hành động được người dùng phê duyệt riêng.

### Ứng dụng Thực tế

- Đặt chuyến đi và theo dõi giá
- So sánh giá thương mại điện tử và kiểm tra tồn kho
- Trích xuất có cấu trúc từ các trang web động
- Kiểm thử và xác minh giao diện người dùng có nhận diện thị giác
- Giám sát và cảnh báo trang web
- Tự động điền biểu mẫu thông minh qua các luồng nhiều bước

## Ví dụ Thực tế: Microsoft Project Opal

Đại lý bạn xây dựng trong bài học này là một phiên bản nhỏ, cục bộ của **đại lý sử dụng máy tính (CUA)** — một chương trình điều khiển trình duyệt như người dùng thật. Microsoft đang đưa ý tưởng này vào doanh nghiệp với **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, một tính năng trong Microsoft 365 Copilot.

Với Project Opal, bạn mô tả một nhiệm vụ và đại lý làm việc thay bạn bằng cách sử dụng **sử dụng máy tính trên Windows 365 Cloud PC an toàn**, thao tác trên các ứng dụng, trang và dữ liệu dựa trên trình duyệt trong tổ chức của bạn. Nó hoạt động **bất đồng bộ ở nền**, và bạn có thể hướng dẫn công việc hoặc kiểm soát bất cứ lúc nào. Các công việc ví dụ gồm:

- Quản lý yêu cầu thành viên nhóm bảo mật
- Thu thập và xác thực bằng chứng kiểm toán cho đánh giá tuân thủ
- Xử lý sự cố IT (cập nhật trạng thái vé, phân công người xử lý, đóng vé trùng)
- Tổng hợp dữ liệu Excel thành báo cáo tài chính

Opal là tham khảo hữu ích cho một đại lý sử dụng máy tính **đạt chuẩn sản xuất, đáng tin cậy** — và củng cố các khái niệm từ các bài học trước:

| Khái niệm trong khóa học này | Cách Project Opal áp dụng |
|------------------------|-----------------------------|
| **Con người tham gia vào vòng lặp** (Bài 06) | Opal tạm dừng để lấy thông tin đăng nhập, dữ liệu nhạy cảm, hay chỉ dẫn không rõ ràng, và không bao giờ nhập mật khẩu hay gửi biểu mẫu nếu không được xác nhận rõ ràng. Bạn có thể *Kiểm soát* và *Trả lại kiểm soát* trong lúc thực hiện tác vụ. |
| **Đại lý đáng tin cậy & an toàn** (Bài 06 & 18) | Chạy trong Windows 365 Cloud PC cách ly, mặc định chỉ dùng trình duyệt (khóa quyền truy cập máy tính khác, do Intune thực thi), dùng danh tính *của bạn* nên chỉ truy cập những gì bạn được phép, và ghi lại mọi hành động để kiểm toán. |
| **Lập kế hoạch & siêu nhận thức** (Bài 07 & 09) | Opal tạo kế hoạch công việc trước, sau đó tự giám sát lý luận từng bước và tạm dừng nếu phát hiện hoạt động đáng ngờ. |
| **Khả năng / công cụ tái sử dụng** (Bài 04) | **Kỹ năng** cho phép bạn viết hướng dẫn cho các công việc lặp lại (nhập từ file `.md` hoặc tạo bằng Opal) và tái dùng chúng qua các cuộc hội thoại. |

> **Khả dụng:** Project Opal hiện có sẵn cho người dùng trong [chương trình truy cập sớm Frontier](https://adoption.microsoft.com/copilot/frontier-program/) với đăng ký Microsoft 365 Copilot, và quản trị viên của bạn phải hoàn tất thiết lập. Vì đây là tính năng thử nghiệm Frontier, các khả năng có thể thay đổi theo thời gian.

## Tài nguyên Tham khảo bổ sung

- [Bắt đầu với Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Mẫu tích hợp Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Tham số người thực hiện Browser-Use và trích xuất nội dung](https://docs.browser-use.com/customize/actor/all-parameters)
- [Cài đặt Khóa học](../00-course-setup/README.md)

## Bài học trước

[Khám phá Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Bài học tiếp theo

[Triển khai Đại lý mở rộng quy mô](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->