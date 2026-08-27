# Mẫu Chứng Từ Biên Lai

Ba tệp biên lai đã được tạo sẵn để kiểm tra mà không cần chạy notebook.

| Tệp | Đây là gì |
|---|---|
| `01_valid_receipt.json` | Một biên lai hợp lệ đã ký cho một cuộc gọi công cụ `lookup_flights`. Xác minh trả về True. |
| `02_tampered_receipt.json` | Cùng một biên lai nhưng một trường đã bị sửa đổi sau khi ký. Xác minh trả về False. |
| `03_chain_three_receipts.json` | Chuỗi ba biên lai hợp lệ (tìm kiếm, giữ chỗ, đặt chỗ) với `previous_receipt_hash` liên kết mỗi biên lai với biên lai trước đó. |

Các mẫu này ký trực tiếp các byte JCS chuẩn hóa của payload bằng Ed25519.
SHA-256 vẫn được sử dụng cho các bản tóm tắt nội dung và liên kết chuỗi biên lai, không phải như một
bước băm trước thêm trước khi ký.

## Xác minh các mẫu

Notebook đi qua quá trình xác minh trong bốn phần. Để xác minh các mẫu này
trực tiếp mà không chạy theo hướng dẫn notebook:

```python
import json
from pathlib import Path

# Giả sử bạn đã hoàn thành việc nhập và các hàm trợ giúp
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

Các mẫu sử dụng cùng một đường dẫn mã như trong notebook, với một khóa ký cố định
và dấu thời gian cố định để tái tạo byte chuẩn xác. Để tạo lại:

```bash
python3 generate_fixtures.py
```

(Kịch bản tại `generate_fixtures.py` trong thư mục này.)

## Những gì học sinh học được khi kiểm tra JSON thô

Việc đọc định dạng biên lai thô giúp xây dựng trực giác mà các ô trong notebook
không phải lúc nào cũng cung cấp. Học sinh khi lướt qua JSON thường nhận thấy:

1. Chữ ký là một chuỗi base64url không giải mã được, nhưng mọi trường khác đều là JSON
   có thể đọc được rõ ràng. Chữ ký không mã hóa nội dung; nó xác nhận nội dung đó.
2. `public_key` được nhúng trong biên lai. Một kiểm toán viên không cần gì khác
   để xác minh (miễn là tin tưởng rằng khóa thực sự thuộc về người phát hành được tuyên bố;
   xem README bài học về hạ tầng nhận dạng).
3. Sửa đổi một ký tự duy nhất trong bất kỳ trường nào, sau đó so sánh lại tệp này với
   `02_tampered_receipt.json`, làm cho cơ chế mức byte trở nên rõ ràng.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->