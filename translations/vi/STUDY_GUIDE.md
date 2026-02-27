# Đại lý AI cho người mới bắt đầu - Hướng dẫn học & Tóm tắt khóa học

Hướng dẫn này cung cấp tóm tắt về khóa học "Đại lý AI cho người mới bắt đầu" và giải thích các khái niệm chính, khung công tác và mẫu thiết kế để xây dựng Đại lý AI.

## 1. Giới thiệu về Đại lý AI

**Đại lý AI là gì?**  
Đại lý AI là các hệ thống mở rộng khả năng của Mô hình Ngôn ngữ Lớn (LLMs) bằng cách cung cấp cho chúng quyền truy cập vào **công cụ**, **kiến thức**, và **bộ nhớ**. Khác với chatbot LLM tiêu chuẩn chỉ tạo văn bản dựa trên dữ liệu huấn luyện, Đại lý AI có thể:  
- **Nhận biết** môi trường của nó (qua cảm biến hoặc đầu vào).  
- **Lý luận** về cách giải quyết một vấn đề.  
- **Hành động** để thay đổi môi trường (qua thiết bị chấp hành hoặc thực thi công cụ).

**Các thành phần chính của một đại lý:**  
- **Môi trường**: Không gian nơi đại lý hoạt động (ví dụ: hệ thống đặt chỗ).  
- **Cảm biến**: Cơ chế thu thập thông tin (ví dụ: đọc một API).  
- **Thiết bị chấp hành**: Cơ chế thực hiện hành động (ví dụ: gửi email).  
- **Bộ não (LLM)**: Bộ máy lý luận lập kế hoạch và quyết định các hành động cần thực hiện.

## 2. Khung công tác Agentic

Khóa học sử dụng **Microsoft Agent Framework (MAF)** với **Azure AI Foundry Agent Service V2** để xây dựng đại lý:

| Thành phần | Tập trung | Phù hợp nhất cho |
|------------|-----------|------------------|
| **Microsoft Agent Framework** | SDK Python/C# thống nhất cho đại lý, công cụ và quy trình | Xây dựng đại lý với công cụ, quy trình đa đại lý, và mẫu sản xuất. |  
| **Azure AI Foundry Agent Service** | Môi trường chạy đám mây được quản lý | Triển khai an toàn, mở rộng với quản lý trạng thái tích hợp sẵn, quan sát và tin cậy. |

## 3. Mẫu thiết kế Agentic

Mẫu thiết kế giúp cấu trúc cách các đại lý hoạt động để giải quyết vấn đề một cách tin cậy.

### **Mẫu Sử dụng Công cụ** (Bài học 4)  
Mẫu này cho phép đại lý tương tác với thế giới bên ngoài.  
- **Khái niệm**: Đại lý được cung cấp một "lược đồ" (danh sách các chức năng có sẵn và tham số của chúng). LLM quyết định *công cụ nào* được gọi và với *tham số* gì dựa trên yêu cầu của người dùng.  
- **Luồng**: Yêu cầu người dùng -> LLM -> **Chọn công cụ** -> **Thực thi công cụ** -> LLM (với đầu ra công cụ) -> Phản hồi cuối cùng.  
- **Trường hợp sử dụng**: Truy xuất dữ liệu thời gian thực (thời tiết, giá cổ phiếu), thực hiện phép tính, chạy mã.

### **Mẫu Lập kế hoạch** (Bài học 7)  
Mẫu này giúp đại lý giải quyết công việc phức tạp nhiều bước.  
- **Khái niệm**: Đại lý chia nhỏ mục tiêu cao cấp thành một chuỗi các nhiệm vụ phụ nhỏ hơn.  
- **Phương pháp**:  
  - **Phân rã nhiệm vụ**: Tách "Lập kế hoạch chuyến đi" thành "Đặt vé máy bay", "Đặt khách sạn", "Thuê xe".  
  - **Lập kế hoạch lặp đi lặp lại**: Đánh giá lại kế hoạch dựa trên kết quả bước trước (ví dụ: nếu chuyến bay đầy, chọn ngày khác).  
- **Triển khai**: Thường bao gồm đại lý "Người lập kế hoạch" tạo một kế hoạch có cấu trúc (ví dụ: JSON) sau đó được các đại lý khác thực thi.

## 4. Nguyên tắc thiết kế

Khi thiết kế đại lý, hãy cân nhắc ba chiều:  
- **Không gian**: Đại lý nên kết nối con người và kiến thức, dễ tiếp cận nhưng không gây phiền phức.  
- **Thời gian**: Đại lý nên học từ *Quá khứ*, cung cấp gợi ý thích hợp trong *Hiện tại*, và thích nghi cho *Tương lai*.  
- **Cốt lõi**: Chấp nhận sự không chắc chắn nhưng xây dựng niềm tin qua sự minh bạch và quyền kiểm soát của người dùng.

## 5. Tóm tắt các bài học chính

- **Bài học 1**: Đại lý là hệ thống, không chỉ là mô hình. Chúng nhận biết, lý luận và hành động.  
- **Bài học 2**: Microsoft Agent Framework trừu tượng hóa độ phức tạp của việc gọi công cụ và quản lý trạng thái.  
- **Bài học 3**: Thiết kế với sự minh bạch và quyền kiểm soát của người dùng trong tâm trí.  
- **Bài học 4**: Công cụ là "đôi tay" của đại lý. Định nghĩa lược đồ rất quan trọng để LLM hiểu cách sử dụng chúng.  
- **Bài học 7**: Lập kế hoạch là "chức năng điều hành" của đại lý, cho phép nó xử lý các quy trình phức tạp.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi nỗ lực đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc thiếu sót. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và có thẩm quyền. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai lệch nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->