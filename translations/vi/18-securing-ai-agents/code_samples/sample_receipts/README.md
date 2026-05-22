# Mẫu Phiếu Thu Tiền

Ba tệp phiếu thu đã được tạo sẵn để kiểm tra mà không cần chạy notebook.

| Tệp | Là gì |
|---|---|
| `01_valid_receipt.json` | Một phiếu thu có chữ ký hợp lệ cho lần gọi công cụ `lookup_flights`. Việc xác minh trả về True. |
| `02_tampered_receipt.json` | Cùng một phiếu thu với một trường bị sửa đổi sau khi ký. Việc xác minh trả về False. |
| `03_chain_three_receipts.json` | Một chuỗi ba phiếu thu hợp lệ (tìm kiếm, giữ chỗ, đặt chỗ) với `previous_receipt_hash` liên kết mỗi phiếu với phiếu trước đó. |

## Xác minh các mẫu này

Notebook hướng dẫn qua việc xác minh trong bốn phần. Để xác minh các mẫu này trực tiếp mà không cần chạy qua nội dung của notebook:

```python
import json
from pathlib import Path

# Giả sử bạn đã hoàn thành việc nhập khẩu và các hàm trợ giúp
# từ phần 1 và 2 của 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Đúng

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Sai

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Cách các mẫu này được tạo ra

Các mẫu sử dụng cùng một đường dẫn mã như notebook, với một khóa ký cố định
và các dấu thời gian cố định để tái tạo byte chính xác. Để tạo lại:

```bash
python3 generate_fixtures.py
```

(Script nằm ở `generate_fixtures.py` trong thư mục này.)

## Những gì học sinh học được từ việc xem xét JSON thô

Đọc định dạng phiếu thu thô xây dựng trực giác mà các ô trong notebook
không phải lúc nào cũng cung cấp. Học sinh khi lướt qua JSON thường nhận thấy:

1. Chữ ký là một chuỗi base64url mờ đục, nhưng mọi trường khác đều là JSON dễ đọc thông thường. Chữ ký không mã hóa nội dung; nó chứng nhận nội dung đó.
2. `public_key` được nhúng trong phiếu thu. Một kiểm toán viên không cần gì thêm
   để xác minh (tùy thuộc vào việc tin cậy rằng khóa thực sự thuộc về người phát hành được tuyên bố; xem README bài học về hạ tầng danh tính).
3. Thay đổi một ký tự duy nhất của bất kỳ trường nào, sau đó so sánh lại tệp này với
   `02_tampered_receipt.json`, làm cơ chế mức byte trở nên rõ ràng.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->