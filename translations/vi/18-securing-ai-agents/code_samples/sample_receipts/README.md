# Các mẫu Biên nhận

Ba tệp biên nhận được tạo sẵn để kiểm tra mà không cần chạy sổ tay.

| Tệp | Đây là gì |
|---|---|
| `01_valid_receipt.json` | Một biên nhận hợp lệ đã được ký cho một lần gọi công cụ `lookup_flights`. Việc xác minh trả về True. |
| `02_tampered_receipt.json` | Cùng một biên nhận với một trường bị chỉnh sửa sau khi ký. Việc xác minh trả về False. |
| `03_chain_three_receipts.json` | Một chuỗi ba biên nhận hợp lệ (tìm kiếm, giữ chỗ, đặt chỗ) với `previous_receipt_hash` liên kết mỗi biên nhận với biên nhận trước đó. |

Các mẫu ký trực tiếp các byte JCS chuẩn của payload với Ed25519.
SHA-256 vẫn được sử dụng cho các bản tóm tắt nội dung và các liên kết chuỗi biên nhận, không như một
bước tiền băm bổ sung trước khi ký.

## Xác minh các mẫu

Sổ tay hướng dẫn xác minh qua bốn phần. Để kiểm tra các mẫu này
trực tiếp mà không cần qua phần giải thích của sổ tay:

```python
import json
from pathlib import Path

# Giả sử bạn đã hoàn thành việc nhập khẩu và các hàm trợ giúp
# từ các phần 1 và 2 của 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Đúng

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Sai

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Cách các mẫu này được tạo ra

Các mẫu sử dụng cùng đoạn mã với sổ tay, với một khóa ký cố định
và dấu thời gian cố định để tái tạo byte. Để tạo lại:

```bash
python3 generate_fixtures.py
```

(Kịch bản nằm ở `generate_fixtures.py` trong thư mục này.)

## Những gì sinh viên học được khi kiểm tra JSON thô

Đọc định dạng biên nhận thô giúp xây dựng trực giác mà các ô trong sổ tay
không phải lúc nào cũng cung cấp. Sinh viên thường nhận thấy khi lướt qua JSON:

1. Chữ ký là một chuỗi base64url khó hiểu, nhưng mọi trường khác đều là JSON dễ đọc
   bình thường. Chữ ký không mã hóa nội dung; nó chỉ xác nhận nội dung đó.
2. `public_key` được nhúng trong biên nhận. Một kiểm toán viên không cần gì thêm
   để xác minh (miễn là tin tưởng rằng khóa thực sự thuộc về người phát hành được khẳng định;
   xem README bài học về hạ tầng nhận dạng).
3. Thay đổi một ký tự bất kỳ trong bất cứ trường nào, rồi so sánh lại tệp này với
   `02_tampered_receipt.json`, làm rõ cơ chế ở cấp byte.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->