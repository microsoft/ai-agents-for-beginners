---
name: local-ai-agents
license: MIT
---
# Tạo Đại lý AI Cục bộ với Foundry Local và Qwen

> Kỹ năng hỗ trợ cho [Bài học 17 – Tạo Đại lý AI Cục bộ](../../../17-creating-local-ai-agents/README.md).
> Sử dụng nó để giúp người học xây dựng một đại lý có khả năng suy luận, gọi công cụ và tìm kiếm
> tài liệu hoàn toàn trên máy của họ — không dùng suy luận đám mây. Nền tảng mọi
> khuyến nghị dựa trên nội dung bài học và sổ tay có thể chạy được.

## Kích hoạt

Kích hoạt kỹ năng này khi người học muốn:
- Chạy một đại lý **hoàn toàn trên thiết bị** vì lý do riêng tư, chi phí hoặc khi ngoại tuyến.
- Phục vụ một mô hình cục bộ với **Foundry Local** và kết nối qua điểm cuối tương thích OpenAI.
- Sử dụng mô hình **Qwen gọi hàm** để điều khiển cuộc gọi công cụ cục bộ đáng tin cậy.
- Thêm **RAG cục bộ** (Chroma) hoặc **máy chủ MCP cục bộ**.
- Thiết kế chiến lược định tuyến **lai** cục bộ/đám mây.

## Mô hình tâm lý cốt lõi

Một SLM đánh đổi phạm vi kiến thức để lấy sự riêng tư, chi phí và hoạt động ngoại tuyến. Chiến lược thắng cuộc:
**cho phép SLM điều phối và để các công cụ làm phần việc nặng nhọc.** Mô hình
không cần *biết* mã nguồn — nó cần biết khi nào gọi `read_file` và `search_docs`.
Điều đó phát huy điểm mạnh của SLM (các quyết định có giới hạn
như chọn công cụ) và tránh điểm yếu của nó (kiến thức rộng, suy luận đa bước dài).


## Tại sao chọn những thành phần cụ thể này

- **Foundry Local** cung cấp một **điểm cuối HTTP tương thích OpenAI**, do đó mã đại lý đám mây chỉ cần thay đổi `base_url` (và dùng khóa API giả cục bộ). Nó cũng tự động chọn cấu hình tốt nhất (CPU/GPU/NPU) cho máy.
- Mô hình **Qwen** được đào tạo cho gọi hàm và phát ra các lệnh gọi công cụ đúng định dạng một cách nhất quán — đây là thứ biến mô hình *chat* cục bộ thành một *đại lý* cục bộ.
- **Chroma** chạy trong tiến trình và lưu vectơ trên đĩa, nên toàn bộ quy trình RAG (nhúng → lưu trữ → truy xuất → suy luận) đều giữ nguyên cục bộ.
- **MCP** là một phương tiện truyền tải, không phải dịch vụ đám mây: máy chủ MCP có thể chạy cục bộ qua `stdio`.

## Những điều cần thiết để thiết lập

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # vùng giữ chỗ cục bộ
```

Khoảng 8 GB RAM là mức tối thiểu thực tế; GPU/NPU hỗ trợ nhưng không bắt buộc.

## Các mẫu chủ chốt cần tái tạo

Hướng người học tới sổ tay
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Công cụ trong vùng cát**: mỗi công cụ tập tin phân giải đường dẫn và từ chối mọi thứ ngoài một thư mục gốc dự án duy nhất — ngay cả khi cục bộ, công cụ chạy với quyền của người dùng.
- **Vòng gọi công cụ**: đăng ký công cụ với sơ đồ công cụ OpenAI, thực thi công cụ được yêu cầu cục bộ, trả kết quả lại, lặp lại cho đến câu trả lời cuối cùng.
- **RAG cục bộ**: bổ sung tài liệu vào bộ sưu tập Chroma; `search_docs` trả về các đoạn top-k.
- **MCP cục bộ**: kết nối tới máy chủ cục bộ qua `stdio`; giới hạn phạm vi ở thư mục dự án và xác thực đầu ra.

## Định tuyến lai (cục bộ là một trong các mô hình)

| Tình huống | Nơi chạy |
|-----------|---------------|
| Dữ liệu nhạy cảm / ngoại tuyến | SLM cục bộ |
| Nhiệm vụ đơn giản, có giới hạn | SLM cục bộ (rẻ, nhanh) |
| Suy luận đa bước khó trên dữ liệu không nhạy cảm | Mô hình đám mây |
| Mất kết nối đám mây | SLM cục bộ (giảm chất lượng dần dần) |

Điều này phản ánh ý tưởng định tuyến mô hình từ Bài học 16, với máy trạm là một trong các tuyến. Ưu tiên thiết kế có thể chuyển sang cục bộ để đại lý giảm chất lượng thay vì thất bại hoàn toàn.



## Rào chắn cho trợ lý

- Giữ mọi thao tác tập tin/công cụ giới hạn trong thư mục dự án vùng cát.
- Không gửi mã hoặc dữ liệu lên đám mây khi mục tiêu của người học là riêng tư/ngắt kết nối — giữ toàn bộ quy trình cục bộ.
- Đặt kỳ vọng thực tế về chất lượng SLM; dựa vào công cụ và RAG thay vì kiến thức ghi nhớ của mô hình.
- Lưu ý rằng Bài 17 **không có** điểm cuối Phản hồi Foundry, nên kiểm tra bằng đám mây không áp dụng — xác thực bằng cách chạy sổ tay cục bộ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->