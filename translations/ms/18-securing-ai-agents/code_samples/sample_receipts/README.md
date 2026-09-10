# Contoh Resit Penyesuaian

Tiga fail resit yang telah dijana awal untuk pemeriksaan tanpa menjalankan buku nota.

| Fail | Apa ia |
|---|---|
| `01_valid_receipt.json` | Resit sah yang ditandatangani untuk panggilan alat `lookup_flights`. Pengesahan mengembalikan Nilai Benar. |
| `02_tampered_receipt.json` | Resit yang sama dengan satu medan diubah selepas penandatanganan. Pengesahan mengembalikan Nilai Salah. |
| `03_chain_three_receipts.json` | Rantaian tiga resit sah (cari, tahan, tempah) dengan `previous_receipt_hash` menghubungkan setiap satu kepada yang sebelumnya. |

Penyesuaian ini menandatangani bait JCS kanonik muatan secara langsung dengan Ed25519.
SHA-256 kekal digunakan untuk ringkasan kandungan dan pautan rantaian resit, bukan sebagai
pra-ringkasan tambahan sebelum penandatanganan.

## Mengesahkan contoh

Buku nota ini berjalan melalui proses pengesahan dalam empat bahagian. Untuk mengesahkan penyesuaian ini
secara langsung tanpa menjalankan naratif buku nota:

```python
import json
from pathlib import Path

# Andaian anda telah menyelesaikan import dan fungsi pembantu
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

Penyesuaian menggunakan laluan kod yang sama seperti buku nota, dengan satu kunci penandatanganan tetap
dan cap masa tetap untuk kebolehhasilbentukkan bait. Untuk menjana semula:

```bash
python3 generate_fixtures.py
```

(Skrip terletak di `generate_fixtures.py` dalam direktori ini.)

## Apa yang pelajar pelajari dari memeriksa JSON mentah

Membaca format resit mentah membina intuisi yang tidak selalu disediakan oleh sel dalam buku nota.
Pelajar yang melihat sepintas lalu JSON sering perasan:

1. Tandatangan adalah rentetan base64url yang tidak jelas, tetapi semua medan lain adalah JSON yang
   boleh dibaca secara jelas. Tandatangan tidak menyulitkan kandungan; ia mengesahkannya.
2. `public_key` disematkan dalam resit. Pemeriksa tidak memerlukan apa-apa lagi
   untuk mengesahkan (dengan syarat mempercayai bahawa kunci itu sebenarnya milik yang didakwa
   penerbit; lihat README pelajaran tentang infrastruktur identiti).
3. Mengubah satu aksara mana-mana medan, kemudian membandingkan semula fail ini dengan
   `02_tampered_receipt.json`, menjadikan mekanisme tahap bait itu nyata.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->