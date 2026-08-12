# Kiểm thử khói cho Agent

Thư mục này chứa **danh mục kiểm thử khói** cho các agent bạn xây dựng trong khóa học.
Một bài kiểm thử khói là một phép kiểm tra nhanh và rẻ tiền để xác nhận một **agent được Microsoft Foundry
triển khai** có thể truy cập, phản hồi và tuân thủ những kỳ vọng cơ bản nhất của lời nhắc.
Đây là cánh cổng đầu tiên — không thay thế cho quy trình đánh giá đầy đủ mà bạn học trong
[Bài học 10](../10-ai-agents-production/README.md) và [Bài học 16](../16-deploying-scalable-agents/README.md).


Các danh mục được sử dụng bởi GitHub Action [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
thông qua workflow [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml).


## Cách chạy

1. **Triển khai agent của bài học** lên Microsoft Foundry dưới dạng agent được lưu trữ (xem
   Bài học 16 cho quy trình triển khai). Ghi nhớ **tên agent** và
   **điểm cuối dự án Foundry** của bạn.
2. Thêm các bí mật trong kho lưu trữ này (Cài đặt → Bí mật và biến → Actions):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Danh tính liên kết
   cần có vai trò **Azure AI User** ở **phạm vi dự án Foundry**.
3. Từ tab **Actions**, chạy **Smoke-test hosted agents** và chọn
   `tests_file` của bài học, sau đó cung cấp `agent_name`
   và `project_endpoint` tương ứng.

## Danh mục → bài học → tên agent

| Danh mục | Bài học | Triển khai agent dưới tên |
|---------|--------|-------------------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Giới thiệu về AI Agents](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Sử dụng công cụ](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Triển khai Agent có khả năng mở rộng](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Những bài học nào có kiểm thử khói?

Kiểm thử khói áp dụng cho các bài học mà bạn **triển khai một agent** có thể
trả lời bằng văn bản và có thể được khẳng định dựa trên nội dung đã biết. Những
bài học mang tính khái niệm, chạy chỉ ở máy cục bộ,


- **Bài 17 (Tạo AI Agents cục bộ)** chạy hoàn toàn trên máy làm việc của bạn với
  Foundry Local và **không** cung cấp điểm cuối Phản hồi Foundry, vì vậy
  hành động này không áp dụng. Hãy xác thực bằng cách chạy notebook tại địa phương.
- Bài học về mẫu thiết kế và lý thuyết (02, 03, 06, 07, 09, 12) không đưa ra một




Mỗi danh mục là tài liệu JSON với mảng `tests` ở cấp cao nhất. Mỗi mục gửi một lời nhắc và khẳng định phản hồi:

| Trường | Ý nghĩa |
|-------|---------|
| `id` | Mã định danh bước duy nhất được ghi trong nhật ký. |
| `description` | Mục đích có thể đọc được bởi con người. |
| `prompt` | Tin nhắn được gửi đến agent. |
| `assertions.status` | Trạng thái HTTP mong đợi (mặc định 200). |
| `assertions.contains_any` | Đạt nếu phản hồi chứa bất kỳ chuỗi con nào trong số này. |
| `assertions.contains_all` | Đạt nếu phản hồi chứa tất cả các chuỗi con. |
| `assertions.contains_none` | Đạt nếu phản hồi không chứa chuỗi con nào trong số này. |
| `save_response_id_as` | Lưu ID phản hồi để sử dụng cho bước đa lượt sau. |
| `use_previous_response_id` | Gửi lượt này nối tiếp với một ID phản hồi đã lưu. |

Các khẳng định là kiểm tra chuỗi con không phân biệt chữ hoa chữ thường. Xem
[tài liệu hành động](https://github.com/marketplace/actions/ai-smoke-test) để biết
cấu trúc đầy đủ, bao gồm nguồn tài nguyên hội thoại do Foundry quản lý.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->