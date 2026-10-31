# Contoh Fixture Tanda Terima

Tiga berkas tanda terima yang telah dibuat sebelumnya untuk inspeksi tanpa menjalankan notebook.

| Berkas | Apa itu |
|---|---|
| `01_valid_receipt.json` | Tanda terima yang ditandatangani secara sah untuk pemanggilan alat `lookup_flights`. Verifikasi mengembalikan True. |
| `02_tampered_receipt.json` | Tanda terima yang sama dengan satu kolom diubah setelah penandatanganan. Verifikasi mengembalikan False. |
| `03_chain_three_receipts.json` | Rangkaian tiga tanda terima yang sah (cari, tahan, pesan) dengan `previous_receipt_hash` menghubungkan setiap tanda terima dengan yang sebelumnya. |

Fixture menandatangani byte JCS kanonik dari payload langsung dengan Ed25519.
SHA-256 tetap digunakan untuk ringkasan konten dan tautan rantai tanda terima, bukan sebagai
pre-hash ekstra sebelum penandatanganan.

## Memverifikasi Contoh

Dalam `18-signed-receipts.ipynb`, jalankan Setup dan Bagian 1 sampai 3 terlebih dahulu.
Bagian 3 mendefinisikan `verify_chain`; Bagian 1 dan 2 saja tidak cukup.
Kemudian jalankan blok berikut dalam sel baru, dengan direktori kerja notebook
diatur ke `18-securing-ai-agents/code_samples`. Jalur fixture di bawah ini relatif
terhadap direktori tersebut.

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

### Memeriksa contoh tanpa Jupyter

Dari akar repositori, pasang ketergantungan pelajaran dan jalankan:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Tes ini menjalankan contoh Python dalam notebook dan blok README yang sama
di atas. Tes juga memeriksa bahwa pemalsuan dan kunci yang tidak dipin ditolak oleh
verifier. Tes melewati sel setup `%pip` notebook karena ketergantungan
dipasang secara terpisah. Tes tidak mengubah notebook atau fixture.

## Bagaimana ini dibuat

Fixture menggunakan jalur kode yang sama dengan notebook, dengan satu kunci tanda tangan tetap
dan waktu tetap untuk reproduksibilitas byte. Untuk membuat ulang:

```bash
python3 generate_fixtures.py
```

(Skrip berada di `generate_fixtures.py` dalam direktori ini.)

## Apa yang dipelajari siswa dari inspeksi JSON mentah

Membaca format tanda terima mentah membangun intuisi yang tidak selalu diberikan oleh sel di notebook.
Siswa yang membaca sekilas JSON sering memperhatikan:

1. Tanda tangan adalah string base64url buram, tetapi setiap kolom lain adalah JSON yang dapat
   dibaca biasa. Tanda tangan tidak mengenkripsi isi; ia menyatakan isi tersebut.
2. `public_key` tertanam dalam tanda terima, yang cukup untuk memeriksa
   konsistensi diri tetapi bukan kepercayaan penerbit. Auditor harus membandingkannya dengan kunci
   yang dipin di luar tanda terima atau diselesaikan melalui registri terpercaya.
3. Mengubah satu karakter dari kolom mana pun, lalu membandingkan ulang berkas ini dengan
   `02_tampered_receipt.json`, membuat mekanisme pada tingkat byte menjadi lebih nyata.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->