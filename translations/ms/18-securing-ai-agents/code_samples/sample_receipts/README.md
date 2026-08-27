# Penetapan Resit Contoh

Tiga fail resit pra-jana untuk pemeriksaan tanpa menjalankan buku nota.

| Fail | Apa ia |
|---|---|
| `01_valid_receipt.json` | Resit yang sah yang ditandatangani untuk panggilan alat `lookup_flights`. Pengesahan mengembalikan True. |
| `02_tampered_receipt.json` | Resit yang sama dengan satu medan diubah selepas penandatanganan. Pengesahan mengembalikan False. |
| `03_chain_three_receipts.json` | Rantaian tiga resit sah (cari, tahan, tempah) dengan `previous_receipt_hash` menghubungkan setiap satunya kepada yang sebelumnya. |

Penetapan ini menandatangani bait JCS kanonik payload secara langsung dengan Ed25519.
SHA-256 kekal digunakan untuk ringkasan kandungan dan pautan rantaian resit, bukan sebagai
pra-hash tambahan sebelum menandatangani.

## Mengesahkan contoh-contoh

Buku nota menerangkan pengesahan dalam empat bahagian. Untuk mengesahkan penetapan ini
secara langsung tanpa menjalankan naratif buku nota:

```python
import json
from pathlib import Path

# Menganggap anda telah menyelesaikan import dan fungsi pembantu
# dari bahagian 1 dan 2 fail 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Betul

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Salah

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Cara ia dijana

Penetapan menggunakan laluan kod yang sama seperti buku nota, dengan satu kunci tandatangan tetap
dan cap masa tetap untuk kebolehulangan bait. Untuk menjana semula:

```bash
python3 generate_fixtures.py
```

(Skrip berada di `generate_fixtures.py` dalam direktori ini.)

## Apa yang pelajar pelajari daripada memeriksa JSON mentah

Membaca format resit mentah membina intuisinya yang mana sel dalam buku nota
tidak sentiasa berikan. Pelajar yang meneliti JSON sering menyedari:

1. Tandatangan adalah rentetan base64url yang kabur, tetapi setiap medan lain adalah JSON yang
   boleh dibaca dengan jelas. Tandatangan tidak menyulitkan kandungan; ia mengesahkannya.
2. `public_key` disisipkan dalam resit. Pemeriksa tidak memerlukan apa-apa lagi
   untuk pengesahan (bergantung pada kepercayaan bahawa kunci itu benar-benar milik penerbit yang didakwa;
   lihat README pelajaran mengenai infrastruktur identiti).
3. Mengubah satu aksara pada mana-mana medan, kemudian membandingkan semula fail ini dengan
   `02_tampered_receipt.json`, menjadikan mekanisme peringkat bait itu nyata.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->