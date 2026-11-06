# Bộ Dữ Liệu Mẫu Biên Lai

Ba tệp biên lai được tạo sẵn để kiểm tra mà không cần chạy notebook.

| Tệp | Nó là gì |
|---|---|
| `01_valid_receipt.json` | Một biên lai hợp lệ đã được ký cho một cuộc gọi công cụ `lookup_flights`. Xác minh trả về True. |
| `02_tampered_receipt.json` | Cùng một biên lai với một trường bị sửa đổi sau khi ký. Xác minh trả về False. |
| `03_chain_three_receipts.json` | Một chuỗi gồm ba biên lai hợp lệ (tìm kiếm, giữ, đặt chỗ) với `previous_receipt_hash` liên kết từng biên lai với biên lai trước đó. |

Bộ dữ liệu này ký trực tiếp các byte JCS chuẩn hóa của payload bằng Ed25519.
SHA-256 vẫn được dùng cho tiêu đề nội dung và các liên kết chuỗi biên lai, không phải như một
bước băm trước khi ký thêm.

## Xác minh các mẫu

Trong `18-signed-receipts.ipynb`, chạy phần Setup và các Phần 1 đến 3 trước.
Phần 3 định nghĩa `verify_chain`; Chỉ Phần 1 và 2 thì không đủ.
Sau đó chạy khối lệnh sau trong một ô mới, với thư mục làm việc của notebook
được đặt thành `18-securing-ai-agents/code_samples`. Đường dẫn bộ dữ liệu bên dưới là tương đối
so với thư mục đó.

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# This fixture key is pinned by the verifier, outside the receipt under test.
FIXTURE_ISSUER_PUBLIC_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"
fixture_trusted_public_keys = {FIXTURE_ISSUER_PUBLIC_KEY}

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text())
print(
    f"Valid receipt: {verify_receipt(valid, fixture_trusted_public_keys)}"
)  # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text())
print(
    f"Tampered receipt: {verify_receipt(tampered, fixture_trusted_public_keys)}"
)  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text())
for r in verify_chain(chain, fixture_trusted_public_keys):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

### Kiểm tra ví dụ mà không cần Jupyter

Từ thư mục gốc của kho lưu trữ, cài đặt phụ thuộc bài học và chạy:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Những bài kiểm tra này thực thi các ví dụ Python trong notebook và khối README chính xác
phía trên. Chúng cũng kiểm tra rằng sự giả mạo và các khóa không được ghim sẽ bị từ chối bởi
các trình xác minh. Các bài kiểm tra bỏ qua ô thiết lập `%pip` của notebook vì các phụ thuộc
được cài đặt riêng. Chúng không thay đổi notebook hay bộ dữ liệu.

## Cách những mẫu này được tạo ra

Bộ dữ liệu sử dụng cùng đường đi mã như notebook, với một khóa ký cố định
và dấu thời gian cố định để tái lập byte giống nhau. Để tạo lại:

```bash
python3 generate_fixtures.py
```

(Kịch bản nằm ở `generate_fixtures.py` trong thư mục này.)

## Sinh viên học gì khi xem xét JSON thô

Việc đọc định dạng biên lai thô xây dựng trực giác mà các ô trong notebook
không phải lúc nào cũng cung cấp. Sinh viên khi đọc lướt JSON thường nhận thấy:

1. Chữ ký là một chuỗi base64url không rõ cấu trúc, nhưng mọi trường khác đều là JSON
   đọc được rõ. Chữ ký không mã hóa nội dung; nó xác nhận nội dung đó.
2. `public_key` được nhúng trong biên lai, đủ để kiểm tra
   tính nhất quán nội bộ nhưng không phải sự tin cậy của người phát hành. Một kiểm toán viên phải so sánh nó với một khóa
   được ghim bên ngoài biên lai hoặc được giải quyết qua một đăng ký tin cậy.
3. Sửa một ký tự đơn trong bất kỳ trường nào, rồi so sánh lại tệp này với
   `02_tampered_receipt.json`, làm cho cơ chế cấp byte trở nên rõ ràng.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->