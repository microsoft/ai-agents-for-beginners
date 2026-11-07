# ตัวอย่างไฟล์ใบเสร็จ

ไฟล์ใบเสร็จสำเร็จรูปสี่ไฟล์สำหรับตรวจสอบโดยไม่ต้องรันโน้ตบุ๊ก

| ไฟล์ | คืออะไร |
|---|---|
| `01_valid_receipt.json` | ใบเสร็จลงนามถูกต้องสำหรับการเรียกใช้เครื่องมือ `lookup_flights` การตรวจสอบจะคืนค่า True |
| `02_tampered_receipt.json` | ใบเสร็จเดียวกันซึ่งแก้ไขหนึ่งฟิลด์หลังจากลงนามแล้ว การตรวจสอบคืนค่า False |
| `03_chain_three_receipts.json` | โซ่ของใบเสร็จสามฉบับที่ถูกต้อง (ค้นหา, ถือครอง, จอง) โดยใช้ `previous_receipt_hash` เชื่อมโยงแต่ละใบกับใบก่อนหน้า |
| `04_resigned_receipt.json` | ใบเสร็จเดียวกันซึ่งถูกปลอมแปลงแล้วลงนามใหม่โดยผู้โจมตี โดยฝังคีย์สาธารณะของผู้โจมตีไว้ ตรวจสอบได้โดยใช้คีย์นั้น แต่ตรวจสอบกับคีย์ของผู้ออกล้มเหลว |

ไฟล์เหล่านี้ลงนามบรรทัดข้อมูล JCS แบบ canonical ของ payload โดยตรงด้วย Ed25519
SHA-256 ยังคงใช้สำหรับสรุปเนื้อหาและเชื่อมใบเสร็จโซ่ ไม่ได้ใช้
เป็นการแฮชล่วงหน้าก่อนการลงนาม

## การตรวจสอบตัวอย่าง

ใน `18-signed-receipts.ipynb` ให้รัน Setup และตอนที่ 1 ถึง 3 ก่อน
ตอนที่ 3 กำหนด `verify_chain`; ตอนที่ 1 และ 2 อย่างเดียวไม่เพียงพอ
จากนั้นรันบล็อกต่อไปนี้ในเซลล์ใหม่ โดยตั้งไดเรกทอรีทำงานของโน้ตบุ๊ก
เป็น `18-securing-ai-agents/code_samples` เส้นทางไฟล์ตัวอย่างด้านล่างสัมพันธ์กับ
ไดเรกทอรีนั้น

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

### การตรวจสอบตัวอย่างโดยไม่ใช้ Jupyter

จากรากของที่เก็บ ติดตั้งไลบรารีที่จำเป็นสำหรับบทเรียนและรัน:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

การทดสอบเหล่านี้จะรันตัวอย่าง Python ในสมุดบันทึกและบล็อก README ที่ตรงกัน
ข้างต้น พวกเขายังตรวจสอบด้วยว่าการปลอมแปลงและกุญแจที่ไม่ได้ปักหมุดจะถูกปฏิเสธโดย
ตัวตรวจสอบ การทดสอบข้ามเซลล์การตั้งค่า `%pip` ของสมุดบันทึกเพราะขึ้นอยู่กับการติดตั้งแยกต่างหาก
พวกเขาไม่เปลี่ยนแปลงสมุดบันทึกหรืออุปกรณ์ช่วยเหลือใดๆ

## กระบวนการสร้างไฟล์เหล่านี้

อุปกรณ์ช่วยเหลือใช้เส้นทางโค้ดเดียวกันกับสมุดบันทึก โดยมีกุญแจลงนามชี้เฉพาะ
และเวลาคงที่เพื่อให้ได้ความเท่าเทียมกันของไบต์ สำหรับการสร้างใหม่:

```bash
python3 generate_fixtures.py
```

(สคริปต์อยู่ที่ `generate_fixtures.py` ในไดเรกทอรีนี้)

`../test_signed_receipts.py` จะตรวจสอบทั้งหมดนี้โดยอัตโนมัติ: มันรัน
โค้ดของสมุดบันทึก, ตรวจสอบอุปกรณ์ช่วยเหลือทั้งสี่นี้ด้วยสมุดบันทึก
`verify_receipt` และ `verify_chain`, และยืนยันว่าการสร้างใหม่ของ
อุปกรณ์ช่วยเหลือมีไบต์เหมือนกัน จาก `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## สิ่งที่นักเรียนได้เรียนรู้จากการตรวจสอบ JSON ดิบ

การอ่านรูปแบบใบเสร็จดิบสร้างความเข้าใจที่เซลล์ในสมุดบันทึก
อาจไม่ได้ให้ นักเรียนที่อ่าน JSON อย่างรวดเร็วมักจะสังเกตเห็น:

1. ลายเซ็นเป็นสตริง base64url แบบทึบคลุม แต่ฟิลด์อื่นทั้งหมดเป็น JSON
   ที่อ่านง่าย ลายเซ็นไม่เข้ารหัสเนื้อหา; มันเป็นการยืนยันเนื้อหา
2. `public_key` ฝังอยู่ในใบเสร็จ ซึ่งทำให้ไฟล์
   เป็นไฟล์ที่สมบูรณ์ แต่ไม่ใช่สิ่งที่ผู้ตรวจสอบตรวจสอบเทียบเคียง เปรียบเทียบ
   `02_tampered_receipt.json` กับ `04_resigned_receipt.json`: ทั้งสองถูก
   เปลี่ยนแปลงหลังจากลงนาม แต่ไฟล์ที่สองถูกลงลายมือชื่อใหม่ด้วยกุญแจของผู้โจมตีเอง
   ดังนั้นมันจึงยืนยันด้วยกุญแจที่มันถือ กุญแจฝังในไฟล์
   บอกว่าฟิล์นี้สอดคล้องภายใน เพียงแต่กุญแจที่ได้รับ
   ที่อื่นบอกคุณว่าใครเป็นผู้รับผิดชอบออกเอกสารนี้
3. การแก้ไขตัวอักษรเดียวในฟิลด์ใดๆ นอก `signature` แล้ว
   นำไฟล์นี้ไปเปรียบเทียบกับ `02_tampered_receipt.json` อีกครั้ง จะทำให้
   กลไกระดับไบต์เป็นรูปธรรม

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->