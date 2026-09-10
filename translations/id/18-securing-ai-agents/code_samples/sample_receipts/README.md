# Contoh Fixtures Struk

Tiga file struk yang sudah dibuat sebelumnya untuk pemeriksaan tanpa menjalankan notebook.

| File | Apa itu |
|---|---|
| `01_valid_receipt.json` | Struk yang valid dan ditandatangani untuk panggilan alat `lookup_flights`. Verifikasi mengembalikan True. |
| `02_tampered_receipt.json` | Struk yang sama dengan satu kolom diubah setelah penandatanganan. Verifikasi mengembalikan False. |
| `03_chain_three_receipts.json` | Rangkaian tiga struk valid (search, hold, book) dengan `previous_receipt_hash` yang menghubungkan setiap struk ke yang sebelumnya. |

Fixtures ini menandatangani byte JCS kanonik payload secara langsung dengan Ed25519.
SHA-256 tetap digunakan untuk digest konten dan link rantai struk, bukan sebagai
pre-hash tambahan sebelum penandatanganan.

## Memverifikasi contoh

Notebook membahas verifikasi dalam empat bagian. Untuk memverifikasi fixture ini
langsung tanpa menjalankan narasi notebook:

```python
import json
from pathlib import Path

# Mengasumsikan Anda telah menyelesaikan impor dan fungsi pembantu
# dari bagian 1 dan 2 dari 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Benar

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Salah

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Cara pembuatan ini

Fixtures menggunakan jalur kode yang sama dengan notebook, dengan satu kunci tanda tangan tetap
dan cap waktu tetap untuk reproduksi byte. Untuk membuat ulang:

```bash
python3 generate_fixtures.py
```

(Script ada di `generate_fixtures.py` di direktori ini.)

## Apa yang dipelajari siswa dari memeriksa JSON mentah

Membaca format struk mentah membangun intuisi yang tidak selalu tersedia di sel notebook.
Siswa yang membaca sekilas JSON sering memperhatikan:

1. Tanda tangan adalah string base64url yang tidak transparan, tetapi setiap kolom lain adalah JSON yang
   dapat dibaca biasa. Tanda tangan tidak mengenkripsi konten; itu membuktikannya.
2. `public_key` disisipkan di dalam struk. Auditor tidak memerlukan apa pun selain itu
   untuk memverifikasi (tergantung pada kepercayaan bahwa kunci benar-benar milik
   penerbit yang diklaim; lihat README pelajaran tentang infrastruktur identitas).
3. Mengubah satu karakter dari kolom apa pun, lalu membandingkan ulang file ini dengan
   `02_tampered_receipt.json`, membuat mekanisme tingkat byte menjadi konkrit.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->