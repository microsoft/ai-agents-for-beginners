# Mẫu Chứng Từ Biên Lai

Bốn tệp biên lai được tạo sẵn để kiểm tra mà không cần chạy notebook.

| Tệp | Đây là gì |
|---|---|
| `01_valid_receipt.json` | Một biên lai hợp lệ đã ký cho một cuộc gọi công cụ `lookup_flights`. Việc xác minh trả về True. |
| `02_tampered_receipt.json` | Cùng một biên lai với một trường bị thay đổi sau khi ký. Việc xác minh trả về False. |
| `03_chain_three_receipts.json` | Một chuỗi ba biên lai hợp lệ (tìm kiếm, giữ chỗ, đặt chỗ) với `previous_receipt_hash` liên kết từng cái với cái trước đó. |
| `04_resigned_receipt.json` | Cùng một biên lai bị giả mạo và sau đó được ký lại bởi kẻ tấn công, với khóa công khai riêng của kẻ tấn công được nhúng. Xác minh dựa trên khóa bên trong nó. Thất bại khi xác minh bằng khóa của người phát hành. |

Các mẫu này ký trực tiếp các byte JCS chuẩn của phần tải bằng Ed25519.
SHA-256 vẫn được sử dụng cho các bản tóm tắt nội dung và các liên kết chuỗi biên lai, không phải như một
bước tiền-hash bổ sung trước khi ký.

## Xác minh các mẫu

Trong `18-signed-receipts.ipynb`, chạy Setup và các Mục 1 đến 3 trước.
Mục 3 định nghĩa `verify_chain`; chỉ Mục 1 và 2 thì không đủ.
Sau đó chạy đoạn mã dưới đây trong một ô mới, với thư mục làm việc của notebook
được đặt thành `18-securing-ai-agents/code_samples`. Các đường dẫn mẫu bên dưới là đường dẫn tương đối
đến thư mục đó.

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# The issuer's key, pinned here rather than read from any receipt. In a real
# deployment it comes from the issuer's JWK Set or a pinned config value.
# This is the public half of the fixed signing key in generate_fixtures.py.
ISSUER_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text(encoding="utf-8"))
print(f"Valid receipt: {verify_receipt(valid, ISSUER_KEY)}")        # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text(encoding="utf-8"))
print(f"Tampered receipt: {verify_receipt(tampered, ISSUER_KEY)}")  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text(encoding="utf-8"))
for r in verify_chain(chain, ISSUER_KEY):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")

# The forgery. Verified against the key it carries, it passes. Against the
# issuer's key, it fails. Only the second question is worth asking.
forged = json.loads((fixture_dir / "04_resigned_receipt.json").read_text(encoding="utf-8"))
print(f"Forged, checked against its own key: "
      f"{verify_receipt(forged, forged['signature']['public_key'])}")  # True
print(f"Forged, checked against issuer key:  "
      f"{verify_receipt(forged, ISSUER_KEY)}")                        # False
```

### Kiểm tra ví dụ mà không dùng Jupyter

Từ thư mục gốc của kho lưu trữ, cài đặt các phụ thuộc bài học và chạy:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Những kiểm tra này thực thi các ví dụ Python trong notebook và chính xác đoạn README
ở trên. Chúng cũng kiểm tra việc giả mạo và các khóa không được cố định có bị từ chối bởi
bộ xác minh hay không. Các kiểm tra bỏ qua ô thiết lập `%pip` của notebook vì các phụ thuộc
được cài đặt riêng. Chúng không thay đổi notebook hoặc các mẫu.

## Cách những mẫu này được tạo ra

Các mẫu sử dụng cùng một đường dẫn mã như notebook, với một khóa ký cố định
và dấu thời gian cố định để đảm bảo tái tạo byte. Để tái tạo:

```bash
python3 generate_fixtures.py
```

(Script nằm tại `generate_fixtures.py` trong thư mục này.)

`../test_signed_receipts.py` kiểm tra tất cả tự động: nó chạy
mã sổ tay, xác minh bốn thành phần cố định này với sổ tay
`verify_receipt` và `verify_chain`, và xác nhận rằng việc tái tạo lại
các thành phần cố định cho ra các byte giống hệt nhau. Từ `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Học sinh học được gì từ việc kiểm tra JSON thô

Đọc định dạng biên nhận thô xây dựng trực giác mà các ô trong sổ tay
không phải lúc nào cũng cung cấp. Các học sinh lướt qua JSON thường nhận thấy:

1. Chữ ký là một chuỗi base64url không thể nhìn thấu, nhưng mọi trường khác đều là JSON
   có thể đọc được. Chữ ký không mã hóa nội dung; nó xác nhận nội dung đó.
2. `public_key` được nhúng trong biên nhận, làm cho tệp
   tự chứa nhưng không phải là thứ mà kiểm toán viên xác minh. So sánh
   `02_tampered_receipt.json` với `04_resigned_receipt.json`: cả hai đều
   bị thay đổi sau khi ký, nhưng bản thứ hai được ký lại bằng
   khóa của kẻ tấn công, nên nó xác minh được bằng khóa mà nó mang theo. Khóa được nhúng
   cho bạn biết tệp này nhất quán bên trong. Chỉ có một khóa lấy
   từ nơi khác mới cho biết ai đã phát hành nó.
3. Sửa đổi một ký tự duy nhất của bất kỳ trường nào ngoài `signature`, sau đó
   so sánh lại tệp này với `02_tampered_receipt.json`, làm cho cơ chế
   cấp byte trở nên rõ ràng.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->