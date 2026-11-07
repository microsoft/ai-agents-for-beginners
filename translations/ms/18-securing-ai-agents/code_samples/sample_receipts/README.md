# Kecacatan Resit Sampel

Empat fail resit yang telah dijana terlebih dahulu untuk pemeriksaan tanpa menjalankan buku nota.

| Fail | Apa itu |
|---|---|
| `01_valid_receipt.json` | Resit sah yang ditandatangani untuk panggilan alat `lookup_flights`. Pengesahan mengembalikan Nilai Benar. |
| `02_tampered_receipt.json` | Resit yang sama dengan satu medan diubah selepas penandatanganan. Pengesahan mengembalikan Nilai Salah. |
| `03_chain_three_receipts.json` | Rantaian tiga resit sah (carian, tahan, tempah) dengan `previous_receipt_hash` yang menghubungkan setiap satu ke yang sebelumnya. |
| `04_resigned_receipt.json` | Resit yang sama telah diubah suai dan kemudian ditandatangani semula oleh penyerang, dengan kekunci awam penyerang disematkan. Disahkan terhadap kekunci di dalamnya. Gagal disahkan terhadap kekunci penerbit. |

Kecacatan menandatangani bait JCS kanonik terus dengan Ed25519.
SHA-256 masih digunakan untuk penggayaan kandungan dan pautan rantaian resit, bukan sebagai
pra-hash tambahan sebelum penandatanganan.

## Mengesahkan sampel

Dalam `18-signed-receipts.ipynb`, jalankan Setup dan Bahagian 1 hingga 3 terlebih dahulu.
Bahagian 3 mentakrifkan `verify_chain`; Bahagian 1 dan 2 sahaja tidak mencukupi.
Kemudian jalankan blok berikut dalam sel baru, dengan direktori kerja buku nota
ditetapkan kepada `18-securing-ai-agents/code_samples`. Laluan kecacatan di bawah adalah relatif
kepada direktori itu.

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

Dari akar repositori, pasang kebergantungan pelajaran dan jalankan:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Ujian ini menjalankan contoh Python buku nota dan blok README yang tepat
di atas. Ia juga memeriksa bahawa pengubahan dan kekunci tidak berpinned ditolak oleh
pemeriksa. Ujian melangkau sel setup `%pip` buku nota kerana kebergantungan
dipasang secara berasingan. Ia tidak mengubah buku nota atau kecacatan.

## Bagaimana ini dijana

Kecacatan menggunakan laluan kod yang sama dengan buku nota, dengan satu kekunci
tandatangan tetap dan cap masa tetap untuk penghasilan semula bait. Untuk menjana semula:

```bash
python3 generate_fixtures.py
```

(Skrip berada di `generate_fixtures.py` dalam direktori ini.)

`../test_signed_receipts.py` memeriksa semua ini secara automatik: ia menjalankan
kod buku nota, mengesahkan keempat-empat kecacatan ini dengan buku nota
`verify_receipt` dan `verify_chain`, dan mengesahkan bahawa menjana semula
kecacatan memberikan bait yang sama. Dari `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Apa yang pelajar pelajari dari memeriksa JSON mentah

Membaca format resit mentah membina intuisi yang sel-sel dalam buku nota
tidak selalu sediakan. Pelajar yang memeriksa JSON biasanya menyedari:

1. Tandatangan ialah rentetan base64url yang samar, tetapi setiap medan lain ialah JSON terbaca biasa.
   Tandatangan tidak menyulitkan kandungan; ia mengesahkan kandungan itu.
2. `public_key` disematkan dalam resit, yang menjadikan fail
   berdiri sendiri tetapi bukan apa yang diaudit pengesah. Bandingkan
   `02_tampered_receipt.json` dengan `04_resigned_receipt.json`: kedua-duanya
   diubah selepas penandatanganan, tetapi yang kedua ditandatangani semula dengan kekunci
   sendiri penyerang, jadi ia disahkan dengan kekunci yang dibawa. Kekunci yang disemat
   memberitahu anda fail adalah konsisten secara dalaman. Hanya kekunci yang diperoleh
   dari tempat lain memberitahu anda siapa yang mengeluarkannya.
3. Mengubah satu aksara mana-mana medan di luar `signature`, kemudian
   membandingkan semula fail ini dengan `02_tampered_receipt.json` menjadikan
   mekanisme tahap bait itu nyata.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->