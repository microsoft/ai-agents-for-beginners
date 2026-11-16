# Contoh Fixture Struk

Empat file struk yang telah dibuat sebelumnya untuk pemeriksaan tanpa menjalankan notebook.

| Berkas | Apa itu |
|---|---|
| `01_valid_receipt.json` | Struk yang ditandatangani dengan valid untuk panggilan alat `lookup_flights`. Verifikasi mengembalikan True. |
| `02_tampered_receipt.json` | Struk yang sama dengan satu bidang diubah setelah penandatanganan. Verifikasi mengembalikan False. |
| `03_chain_three_receipts.json` | Rangkaian tiga struk valid (search, hold, book) dengan `previous_receipt_hash` yang menghubungkan tiap satu ke yang sebelumnya. |
| `04_resigned_receipt.json` | Struk yang sama dirusak dan kemudian ditandatangani ulang oleh penyerang, dengan kunci publik penyerang sendiri tertanam. Memverifikasi terhadap kunci di dalamnya. Gagal terhadap kunci penerbit. |

Fixture ini menandatangani byte JCS kanonik payload langsung dengan Ed25519.
SHA-256 tetap digunakan untuk ringkasan isi dan rantai tautan struk, bukan sebagai
pre-hash tambahan sebelum penandatanganan.

## Memverifikasi contoh

Di `18-signed-receipts.ipynb`, jalankan Setup dan Bagian 1 sampai 3 terlebih dahulu.
Bagian 3 mendefinisikan `verify_chain`; Bagian 1 dan 2 saja tidak cukup.
Kemudian jalankan blok berikut di sel baru, dengan direktori kerja notebook
diatur ke `18-securing-ai-agents/code_samples`. Jalur fixture di bawah ini relatif
terhadap direktori tersebut.

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

### Memeriksa contoh tanpa Jupyter

Dari direktori root repositori, pasang dependensi pelajaran dan jalankan:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Tes ini menjalankan contoh-contoh Python notebook dan blok README persis
di atas. Mereka juga memeriksa bahwa manipulasi dan kunci yang tidak terpasang ditolak oleh
verifikator. Tes melewati sel setup `%pip` notebook karena dependensi
dipasang secara terpisah. Tes ini tidak mengubah notebook atau fixtures.

## Cara pembuatan ini dilakukan

Fixture menggunakan jalur kode yang sama dengan notebook, dengan satu kunci tanda tangan tetap
dan stempel waktu tetap untuk reprodusibilitas byte. Untuk menghasilkan ulang:

```bash
python3 generate_fixtures.py
```

(Script berada di `generate_fixtures.py` dalam direktori ini.)

`../test_signed_receipts.py` memeriksa semua ini secara otomatis: ia menjalankan
kode notebook, memverifikasi keempat fixture ini dengan
`verify_receipt` dan `verify_chain` notebook, dan mengonfirmasi bahwa menghasilkan ulang
fixture memberikan byte yang identik. Dari `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Apa yang dipelajari siswa dari memeriksa JSON mentah

Membaca format struk mentah membangun intuisi yang tidak selalu diberikan oleh sel-sel dalam notebook.
Siswa yang melihat sekilas JSON sering memperhatikan:

1. Tanda tangan adalah string base64url yang tidak dapat dilihat isinya, tetapi semua bidang lain adalah JSON
   yang bisa dibaca biasa. Tanda tangan tidak mengenkripsi konten; ia menyatakan kebenarannya.
2. `public_key` tertanam di dalam struk, yang membuat file ini
   berdiri sendiri tapi bukan apa yang diverifikasi auditor. Bandingkan
   `02_tampered_receipt.json` dengan `04_resigned_receipt.json`: keduanya
   diubah setelah ditandatangani, tetapi yang kedua ditandatangani ulang dengan
   kunci penyerang sendiri, sehingga diverifikasi dengan kunci yang dibawanya.
   Kunci yang tertanam memberi tahu anda bahwa file ini konsisten secara internal.
   Hanya kunci yang didapat dari tempat lain yang memberitahu siapa penerbitnya.
3. Mengubah satu karakter dari bidang mana saja di luar `signature`, lalu
   membandingkan ulang file ini dengan `02_tampered_receipt.json`, membuat mekanisme
   tingkat byte menjadi konkret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->