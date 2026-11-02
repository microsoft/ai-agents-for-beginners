---
name: deploying-scalable-agents
license: MIT
---
# Triển khai các Đại lý Có thể Mở rộng với Microsoft Foundry

> Kỹ năng hỗ trợ cho [Bài học 16 – Triển khai các Đại lý Có thể Mở rộng](../../../16-deploying-scalable-agents/README.md).
> Sử dụng nó để giúp người học chuyển một đại lý từ nguyên mẫu sang triển khai sản xuất có thể mở rộng, có thể quan sát được.
> Căn cứ mọi khuyến nghị vào nội dung bài học và sổ tay có thể chạy được; không phát minh API Foundry.


## Kích hoạt

Kích hoạt kỹ năng này khi người học muốn:
- Triển khai một đại lý lên Microsoft Foundry như một **đại lý được lưu trữ** và làm cho nó có phiên bản/có thể quan sát được.
- Chọn giữa các mẫu triển khai **khách hàng-lưu trữ, đại lý được lưu trữ và quy trình công việc đại lý**.
- Thêm **định tuyến mô hình**, **bộ nhớ đệm phản hồi**, hoặc **ưu tiên giới hạn đồng thời** để kiểm soát độ trễ và chi phí.
- Thêm một **cổng đánh giá** để một phiên bản đại lý xấu không được phát hành.
- Thêm bước **phê duyệt có người kiểm soát** cho các hành động rủi ro cao.
- Gắn công cụ cho đại lý với **OpenTelemetry** để truy vết phục vụ quan sát trong sản xuất.
- **Kiểm thử khói** đại lý đã triển khai như một cổng nhanh sau khi triển khai.

## Mô hình tư duy cốt lõi

Một đại lý sản xuất chủ yếu là bộ khung vận hành *xung quanh* mô hình (~80%),
không phải bản thân mô hình. Ánh xạ mỗi khuyến nghị tới một trong các mối quan tâm sau:

| Mối quan tâm | Nguyên mẫu → Sản xuất |
|---------|------------------------|
| Lưu trữ | sổ tay → dịch vụ lưu trữ có phiên bản |
| Định danh | `az login` của bạn → định danh được quản lý + RBAC phạm vi |
| Trạng thái | trong bộ nhớ → lưu trữ luồng/bộ nhớ bên ngoài |
| Thất bại | theo dõi lỗi → thử lại, dự phòng, cảnh báo |
| Chi phí | "vài xu" → theo dõi, định tuyến, bộ nhớ đệm, lập ngân sách |
| Chất lượng | đánh giá bằng mắt → cổng đánh giá tự động |
| Tin cậy | bạn phê duyệt → chính sách + có người kiểm soát |

## Mẫu triển khai (chọn một, hoặc kết hợp)

1. **Khách hàng-lưu trữ** — vòng suy luận chạy trong quy trình của bạn. Kiểm soát tối đa; bạn sở hữu việc mở rộng/trạng thái.
2. **Đại lý được lưu trữ (Dịch vụ Đại lý Foundry)** — Foundry lưu trữ vòng lặp, lưu trữ luồng, thực thi RBAC/an toàn nội dung, hiển thị đại lý trong cổng thông tin. Kiểm soát ít hơn, bề mặt vận hành nhỏ hơn nhiều.
3. **Quy trình công việc đại lý** — nhiều đại lý/công cụ được kết hợp thành một đồ thị với các nhánh, nút phê duyệt và các điểm kiểm tra bền.

## Vòng đời (vòng lặp để đưa đại lý vào vận hành)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**Đánh giá ngoại tuyến là một cổng, không phải bước suy nghĩ sau cùng** — một phiên bản không được phát hành
trừ khi nó vượt qua ngưỡng. Quan sát trực tuyến cho phản hồi lỗi thực tế
vào bộ kiểm tra ngoại tuyến.

## Các đòn bẩy mở rộng và chi phí (theo thứ tự ưu tiên)

1. **Chọn kích cỡ mô hình phù hợp** — sử dụng mô hình nhỏ nhất vượt qua cổng đánh giá.
2. **Định tuyến theo độ phức tạp** — mô hình nhỏ/nhanh cho yêu cầu đơn giản, mô hình lớn cho suy luận thực tế (phân loại thủ công hoặc Bộ định tuyến Mô hình Foundry).
3. **Bộ nhớ đệm** — phục vụ các yêu cầu gần như trùng lặp mà không cần gọi mô hình.
4. **Thiết kế không trạng thái + ưu tiên giới hạn đồng thời** — lưu trạng thái bên ngoài; thử lại với chờ thời gian lùi.

## Các mẫu then chốt để tái tạo

Hướng người học tới các ví dụ này từ sổ tay
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Bộ xử lý yêu cầu**: bộ nhớ đệm → định tuyến theo độ phức tạp → vết truy vết → chạy → bộ nhớ đệm.
- **Cổng đánh giá**: điểm số bộ kiểm tra ngoại tuyến; trả `pass_rate >= threshold` và chỉ triển khai nếu đúng.
- **Phê duyệt con người**: `@tool(approval_mode="always_require")` cho các hành động như hoàn tiền lớn.
- **Truy vết**: bọc mỗi yêu cầu trong `tracer.start_as_current_span(...)` và đặt các thuộc tính như `routed.model`, `customer.id`.

## Kiểm thử khói đại lý đã triển khai

Sau khi triển khai, xác minh điểm cuối thật sự trả lời (một triển khai màu xanh vẫn có thể
im lặng). Sử dụng hành động [Kiểm thử Khói AI](https://github.com/marketplace/actions/ai-smoke-test)
qua [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
với danh mục trong [`tests/`](../../../tests/README.md). Trình chạy gửi POST từng
lời nhắc tới `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
và khẳng định kết quả trả lời văn bản. Định danh cần vai trò **Người dùng Azure AI** tại
phạm vi dự án Foundry; đối tượng token phải là `https://ai.azure.com/`.

Xếp lớp các cổng: **kiểm thử khói** (có thể truy cập/đáp ứng, mỗi lần triển khai) → **đánh giá ngoại tuyến** (đủ tốt để phát hành, trước khi thúc đẩy) → **đánh giá trực tuyến** (hoạt động ra sao trong thực tế, liên tục).



## Kiểm soát doanh nghiệp

- **RBAC**: cấp cho mỗi đại lý được lưu trữ một định danh được quản lý với quyền tối thiểu.
- **MCP trong sản xuất**: đối xử mọi máy chủ MCP như biên giới không đáng tin cậy — ghim phiên bản, giới hạn phạm vi định danh, kiểm tra kết quả, giới hạn tỷ lệ, không khi nào tiết lộ bí mật.

## Hàng rào bảo vệ cho trợ lý

- Ưu tiên mẫu `FoundryChatClient(...)` + `provider.as_agent(...)` chuẩn được sử dụng trên toàn khóa học.
- Không hứa hẹn kết quả Azure trực tiếp mà bạn chưa xác minh; khuyến nghị quy trình kiểm thử khói để xác nhận triển khai.
- Giữ lời khuyên về đánh giá và chi phí liên kết với nhau: đánh giá đặt sàn chất lượng, định tuyến/bộ nhớ đệm giữ chi phí gần mức đó.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->