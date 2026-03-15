# Đại lý AI cho người mới bắt đầu - Hướng dẫn học & Tóm tắt khóa học

Hướng dẫn này cung cấp tóm tắt khóa học "Đại lý AI cho người mới bắt đầu" và giải thích các khái niệm chính, khung công tác, và mẫu thiết kế để xây dựng Đại lý AI.

## 1. Giới thiệu về Đại lý AI

**Đại lý AI là gì?**  
Đại lý AI là các hệ thống mở rộng khả năng của Mô hình Ngôn ngữ Lớn (LLM) bằng cách cung cấp cho chúng quyền truy cập vào **công cụ**, **kiến thức**, và **bộ nhớ**. Khác với chatbot LLM tiêu chuẩn chỉ tạo ra văn bản dựa trên dữ liệu huấn luyện, một Đại lý AI có thể:  
- **Nhận biết** môi trường của nó (thông qua cảm biến hoặc đầu vào).  
- **Lập luận** về cách giải quyết vấn đề.  
- **Hành động** để thay đổi môi trường (thông qua bộ truyền động hoặc thực thi công cụ).

**Các thành phần chính của một đại lý:**  
- **Môi trường**: Không gian nơi đại lý hoạt động (ví dụ: hệ thống đặt chỗ).  
- **Cảm biến**: Cơ chế để thu thập thông tin (ví dụ: đọc API).  
- **Bộ truyền động**: Cơ chế để thực hiện hành động (ví dụ: gửi email).  
- **Bộ não (LLM)**: Công cụ lập luận lên kế hoạch và quyết định hành động nào cần thực hiện.

## 2. Khung công tác Đại lý

Khóa học sử dụng **Microsoft Agent Framework (MAF)** với **Dịch vụ Đại lý Azure AI Foundry V2** để xây dựng các đại lý:

| Thành phần | Tập trung | Phù hợp nhất cho |
|------------|-----------|------------------|
| **Microsoft Agent Framework** | SDK Python/C# hợp nhất cho đại lý, công cụ và luồng công việc | Xây dựng đại lý với công cụ, luồng công việc đa đại lý và mẫu hình sản xuất. |
| **Dịch vụ Đại lý Azure AI Foundry** | Môi trường chạy đám mây được quản lý | Triển khai an toàn, có thể mở rộng với quản lý trạng thái tích hợp, khả năng quan sát và độ tin cậy. |

## 3. Mẫu thiết kế Đại lý

Mẫu thiết kế giúp cấu trúc cách đại lý vận hành để giải quyết vấn đề một cách tin cậy.

### **Mẫu Sử dụng Công cụ** (Bài 4)  
Mẫu này cho phép đại lý tương tác với thế giới bên ngoài.  
- **Khái niệm**: Đại lý được cung cấp một "kịch bản" (danh sách các chức năng có sẵn và tham số của chúng). LLM quyết định *công cụ* nào sẽ gọi và với *tham số* gì dựa trên yêu cầu của người dùng.  
- **Luồng**: Yêu cầu người dùng -> LLM -> **Chọn công cụ** -> **Thực thi công cụ** -> LLM (với kết quả công cụ) -> Phản hồi cuối cùng.  
- **Trường hợp sử dụng**: Truy xuất dữ liệu thời gian thực (thời tiết, giá cổ phiếu), thực hiện phép tính, chạy mã lệnh.

### **Mẫu Lập kế hoạch** (Bài 7)  
Mẫu này cho phép đại lý giải quyết các nhiệm vụ phức tạp nhiều bước.  
- **Khái niệm**: Đại lý phân nhỏ mục tiêu cao thành chuỗi các nhiệm vụ nhỏ hơn.  
- **Phương pháp**:  
  - **Phân rã nhiệm vụ**: Chia "Lên kế hoạch chuyến đi" thành "Đặt vé máy bay", "Đặt khách sạn", "Thuê xe".  
  - **Lập kế hoạch lặp đi lặp lại**: Đánh giá lại kế hoạch dựa trên kết quả của các bước trước (ví dụ: nếu chuyến bay hết chỗ, chọn ngày khác).  
- **Triển khai**: Thường bao gồm đại lý "Người lập kế hoạch" tạo ra kế hoạch cấu trúc (ví dụ: JSON) sau đó các đại lý khác thực thi.

## 4. Nguyên tắc thiết kế

Khi thiết kế đại lý, xem xét ba chiều:  
- **Không gian**: Đại lý nên kết nối con người và kiến thức, dễ tiếp cận nhưng không gây phiền hà.  
- **Thời gian**: Đại lý nên học từ *Quá khứ*, cung cấp gợi ý phù hợp trong *Hiện tại*, và thích ứng cho *Tương lai*.  
- **Cốt lõi**: Chấp nhận sự không chắc chắn nhưng xây dựng tin cậy qua minh bạch và kiểm soát của người dùng.

## 5. Tóm tắt các bài học chính

- **Bài 1**: Đại lý là hệ thống, không chỉ là mô hình. Chúng nhận biết, lập luận và hành động.  
- **Bài 2**: Microsoft Agent Framework đơn giản hóa việc gọi công cụ và quản lý trạng thái.  
- **Bài 3**: Thiết kế với sự minh bạch và kiểm soát của người dùng trong tâm trí.  
- **Bài 4**: Công cụ là "cánh tay" của đại lý. Định nghĩa kịch bản rất quan trọng để LLM hiểu cách sử dụng chúng.  
- **Bài 7**: Lập kế hoạch là "chức năng điều hành" của đại lý, cho phép nó xử lý các luồng công việc phức tạp.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi nỗ lực đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn có thẩm quyền. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->