# Sample Receipt Fixtures

Tiga fail resit yang telah dijana terlebih dahulu untuk pemeriksaan tanpa menjalankan notebook.

| Fail | Apa itu |
|---|---|
| `01_valid_receipt.json` | Resit sah yang ditandatangani untuk panggilan alat `lookup_flights`. Pengesahan mengembalikan True. |
| `02_tampered_receipt.json` | Resit yang sama dengan satu medan diubah selepas penandatanganan. Pengesahan mengembalikan False. |
| `03_chain_three_receipts.json` | Rangkaian tiga resit sah (carian, tahan, tempah) dengan `previous_receipt_hash` yang menghubungkan setiap satu dengan yang sebelumnya. |

## Memeriksa contoh-contoh

Notebook menerangkan pengesahan dalam empat bahagian. Untuk mengesahkan fixture ini
secara langsung tanpa mengikuti naratif notebook:

```python
import json
from pathlib import Path

# Berpura-pura anda telah menyelesaikan import dan fungsi pembantu
# dari bahagian 1 dan 2 dari 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Benar

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Salah

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Cara ia dijana

Fixture menggunakan laluan kod yang sama seperti notebook, dengan satu kunci tandatangan tetap
dan cap masa tetap untuk kebolehulangan bait. Untuk menjana semula:

```bash
python3 generate_fixtures.py
```

(Skrip berada di `generate_fixtures.py` dalam direktori ini.)

## Apa yang pelajar pelajari dari memeriksa JSON mentah

Membaca format resit mentah membina intuisi yang tidak selalu diberikan oleh sel-sel dalam notebook.
Pelajar yang cepat melihat JSON selalunya perasan:

1. Tandatangan adalah rentetan base64url yang kabur, tetapi setiap medan lain adalah JSON yang boleh dibaca dengan jelas. Tandatangan tidak menyulitkan kandungan; ia mengesahkan kandungan tersebut.
2. `public_key` disematkan dalam resit. Seorang juruaudit tidak memerlukan apa-apa lagi
   untuk mengesahkan (tertakluk kepada mempercayai bahawa kunci itu benar-benar milik yang dinyatakan
   penerbit; lihat README pelajaran mengenai infrastruktur identiti).
3. Mengubah satu aksara dalam mana-mana medan, kemudian membandingkan semula fail ini dengan
   `02_tampered_receipt.json`, menjadikan mekanisme peringkat bait itu konkrit.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->