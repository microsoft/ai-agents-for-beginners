# ตัวอย่างไฟล์ใบเสร็จ

ไฟล์ใบเสร็จสามไฟล์ที่สร้างไว้ล่วงหน้าสำหรับตรวจสอบโดยไม่ต้องรันโน้ตบุ๊ก

| ไฟล์ | คืออะไร |
|---|---|
| `01_valid_receipt.json` | ใบเสร็จที่ลงลายมือชื่อถูกต้องสำหรับการเรียกใช้เครื่องมือ `lookup_flights` การตรวจสอบจะคืนค่าเป็น True |
| `02_tampered_receipt.json` | ใบเสร็จเดียวกันที่มีการแก้ไขฟิลด์หนึ่งหลังจากลงลายมือชื่อ การตรวจสอบจะคืนค่าเป็น False |
| `03_chain_three_receipts.json` | โซ่ของใบเสร็จที่ถูกต้องสามใบ (ค้นหา, ถือ, จอง) โดยมี `previous_receipt_hash` เชื่อมต่อตัวก่อนหน้าแต่ละใบ |

ตัวอย่างไฟล์เหล่านี้ลงลายมือชื่อโดยตรงกับไบต์ JCS ที่เป็น canonical ของ payload ด้วย Ed25519
SHA-256 ยังคงใช้งานอยู่สำหรับการดึงย่อเนื้อหาและลิงก์ใบเสร็จ-โซ่ ไม่ใช่เป็นการ
แฮชล่วงหน้าที่เพิ่มก่อนการลงลายมือชื่อ

## การตรวจสอบตัวอย่าง

ใน `18-signed-receipts.ipynb` ให้รัน Setup และ ส่วนที่ 1 ถึง 3 ก่อน
ส่วนที่ 3 กำหนด `verify_chain`; ส่วนที่ 1 และ 2 อย่างเดียวไม่พอ
แล้วรันบล็อกต่อไปนี้ในเซลล์ใหม่ โดยตั้งไดเรกทอรีทำงานของโน้ตบุ๊ก
เป็น `18-securing-ai-agents/code_samples` เส้นทางตัวอย่างไฟล์ด้านล่างเป็นสัมพัทธ์
กับไดเรกทอรีนั้น

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

### การตรวจสอบตัวอย่างโดยไม่ใช้ Jupyter

จากไดเรกทอรีรากของ repository ให้ติดตั้ง dependencies ของบทเรียนและรัน:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

การทดสอบเหล่านี้จะรันตัวอย่าง Python ของโน้ตบุ๊กและบล็อก README ที่ถูกต้อง
ข้างต้น พวกเขายังตรวจสอบด้วยว่าการปลอมแปลงและกุญแจที่ไม่ได้ตรึงจะถูกปฏิเสธโดย
ตัวตรวจสอบ การทดสอบข้ามเซลล์ `%pip` ของโน้ตบุ๊กเพราะ dependencies
ถูกติดตั้งแยกต่างหาก พวกเขาไม่เปลี่ยนโน้ตบุ๊กหรือไฟล์ตัวอย่าง

## วิธีที่ไฟล์เหล่านี้ถูกสร้าง

ตัวอย่างไฟล์ใช้เส้นทางโค้ดเดียวกับโน้ตบุ๊ก โดยมีกุญแจลงลายมือชื่อคงที่
และเวลาคงที่เพื่อให้ได้ไบต์ที่เหมือนกันทุกครั้ง เมื่อต้องการสร้างใหม่:

```bash
python3 generate_fixtures.py
```

(สคริปต์อยู่ที่ `generate_fixtures.py` ในไดเรกทอรีนี้)

## สิ่งที่นักเรียนเรียนรู้จากการตรวจสอบ JSON ดิบ

การอ่านรูปแบบใบเสร็จดิบช่วยสร้างสัญชาตญาณที่เซลล์ในโน้ตบุ๊ก
ไม่ได้ให้เสมอไป นักเรียนที่สแกน JSON จะมักสังเกตเห็นว่า:

1. ลายเซ็นเป็นสตริงฐาน64url ทึบแสง แต่ว่าแต่ละฟิลด์อื่นๆ เป็น JSON ที่
   อ่านได้ตรงๆ ลายเซ็นไม่เข้ารหัสเนื้อหา แต่นำเสนอว่ามีอยู่จริง
2. `public_key` ถูกฝังอยู่ในใบเสร็จ ซึ่งเพียงพอที่จะตรวจสอบ
   ความสอดคล้องภายในแต่ไม่ใช่ความน่าเชื่อถือของผู้ออก ใครที่ตรวจสอบต้องเปรียบเทียบมันกับกุญแจ
   ที่ตรึงไว้นอกใบเสร็จหรือหาได้จากรีจิสทรีที่เชื่อถือได้
3. การแก้ไขตัวอักษรเดียวของฟิลด์ใดๆ แล้วเปรียบเทียบไฟล์นี้กับ
   `02_tampered_receipt.json` จะทำให้กลไกระดับไบต์เป็นรูปธรรม

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->