# Đại lý AI cho Người mới bắt đầu - Hướng dẫn học & Tóm tắt khóa học

Hướng dẫn này cung cấp bản tóm tắt về khóa học "Đại lý AI cho Người mới bắt đầu" và giải thích các khái niệm chính, khung làm việc, và các mẫu thiết kế để xây dựng Đại lý AI.

## 1. Giới thiệu về Đại lý AI

**Đại lý AI là gì?**  
Đại lý AI là các hệ thống mở rộng khả năng của Mô hình Ngôn ngữ Lớn (LLMs) bằng cách cung cấp cho chúng quyền truy cập vào **công cụ**, **kiến thức**, và **bộ nhớ**. Không giống như chatbot LLM tiêu chuẩn chỉ tạo ra văn bản dựa trên dữ liệu đào tạo, Đại lý AI có thể:  
- **Nhận thức** môi trường của nó (thông qua cảm biến hoặc đầu vào).  
- **Lý luận** về cách giải quyết vấn đề.  
- **Hành động** để thay đổi môi trường (thông qua bộ truyền động hoặc thực thi công cụ).

**Các thành phần chính của một đại lý:**  
- **Môi trường**: Không gian nơi đại lý hoạt động (ví dụ: hệ thống đặt chỗ).  
- **Cảm biến**: Cơ chế thu thập thông tin (ví dụ: đọc API).  
- **Bộ truyền động**: Cơ chế để thực hiện hành động (ví dụ: gửi email).  
- **Bộ não (LLM)**: Bộ máy lý luận lên kế hoạch và quyết định hành động cần thực hiện.

## 2. Khung làm việc dành cho Đại lý

Khóa học trình bày ba khung làm việc chính để xây dựng đại lý:

| Khung làm việc | Tập trung | Thích hợp nhất cho |
|-----------|-------|----------|
| **Semantic Kernel** | SDK sẵn sàng sản xuất cho .NET/Python | Ứng dụng doanh nghiệp, tích hợp AI với mã hiện có. |
| **AutoGen** | Hợp tác đa đại lý | Các kịch bản phức tạp yêu cầu nhiều đại lý chuyên biệt giao tiếp với nhau. |
| **Azure AI Agent Service** | Dịch vụ đám mây được quản lý | Triển khai bảo mật, có thể mở rộng với quản lý trạng thái tích hợp sẵn. |

## 3. Mẫu thiết kế dành cho Đại lý

Các mẫu thiết kế giúp cấu trúc cách đại lý vận hành để giải quyết vấn đề một cách tin cậy.

### **Mẫu Sử dụng Công cụ** (Bài học 4)  
Mẫu này cho phép các đại lý tương tác với thế giới bên ngoài.  
- **Khái niệm**: Đại lý được cung cấp một "schema" (danh sách các chức năng có sẵn và tham số của chúng). LLM quyết định *công cụ nào* gọi và với *tham số gì* dựa trên yêu cầu của người dùng.  
- **Luồng xử lý**: Yêu cầu người dùng -> LLM -> **Chọn công cụ** -> **Thực thi công cụ** -> LLM (với đầu ra công cụ) -> Phản hồi cuối cùng.  
- **Các trường hợp sử dụng**: Truy xuất dữ liệu thời gian thực (thời tiết, giá cổ phiếu), thực hiện tính toán, chạy mã.

### **Mẫu Lập kế hoạch** (Bài học 7)  
Mẫu này cho phép đại lý giải quyết các nhiệm vụ phức tạp, nhiều bước.  
- **Khái niệm**: Đại lý phân chia một mục tiêu tổng thể thành chuỗi các nhiệm vụ nhỏ hơn.  
- **Phương pháp**:  
  - **Phân rã nhiệm vụ**: Chia "Lập kế hoạch chuyến đi" thành "Đặt vé máy bay", "Đặt khách sạn", "Thuê xe".  
  - **Lập kế hoạch lặp đi lặp lại**: Đánh giá lại kế hoạch dựa trên kết quả các bước trước (ví dụ: nếu chuyến bay đầy, chọn ngày khác).  
- **Triển khai**: Thường có một đại lý "Người lập kế hoạch" tạo ra kế hoạch có cấu trúc (ví dụ: JSON) sau đó được các đại lý khác thực hiện.

## 4. Nguyên tắc Thiết kế

Khi thiết kế đại lý, hãy cân nhắc ba chiều:  
- **Không gian**: Đại lý nên kết nối con người và kiến thức, dễ tiếp cận nhưng không gây phiền hà.  
- **Thời gian**: Đại lý nên học từ *Quá khứ*, cung cấp gợi ý phù hợp trong *Hiện tại*, và thích nghi cho *Tương lai*.  
- **Cốt lõi**: Chấp nhận sự không chắc chắn nhưng xây dựng niềm tin qua minh bạch và kiểm soát của người dùng.

## 5. Tóm tắt các Bài học Chính

- **Bài học 1**: Đại lý là hệ thống, không chỉ là mô hình. Họ nhận thức, lý luận, và hành động.  
- **Bài học 2**: Các khung như Semantic Kernel và AutoGen trừu tượng hóa việc gọi công cụ và quản lý trạng thái.  
- **Bài học 3**: Thiết kế với sự minh bạch và kiểm soát của người dùng trong tâm trí.  
- **Bài học 4**: Công cụ là "đôi tay" của đại lý. Định nghĩa schema rất quan trọng để LLM hiểu cách sử dụng chúng.  
- **Bài học 7**: Lập kế hoạch là "chức năng điều hành" của đại lý, giúp nó xử lý các quy trình phức tạp.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được xem là nguồn đáng tin cậy nhất. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->