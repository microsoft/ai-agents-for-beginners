# Contoh Fikstur Resit

Tiga fail resit yang telah dijana terlebih dahulu untuk pemeriksaan tanpa menjalankan buku nota.

| Fail | Apa itu |
|---|---|
| `01_valid_receipt.json` | Resit yang sah dan ditandatangani untuk panggilan alat `lookup_flights`. Pengesahan mengembalikan True. |
| `02_tampered_receipt.json` | Resit yang sama dengan satu medan yang diubah selepas menandatangani. Pengesahan mengembalikan False. |
| `03_chain_three_receipts.json` | Rantaian tiga resit sah (cari, tahan, tempah) dengan `previous_receipt_hash` menghubungkan setiap satu kepada yang sebelumnya. |

Fikstur menandatangani bait JCS kanonik payload terus dengan Ed25519.
SHA-256 masih digunakan untuk pencacahan kandungan dan pautan rantaian resit, bukan sebagai
pra-hash tambahan sebelum menandatangani.

## Mengesahkan contoh

Dalam `18-signed-receipts.ipynb`, jalankan Setup dan Bahagian 1 hingga 3 terlebih dahulu.
Bahagian 3 mendefinisikan `verify_chain`; Bahagian 1 dan 2 sahaja tidak mencukupi.
Kemudian jalankan blok berikut dalam sel baru, dengan direktori kerja buku nota
ditetapkan ke `18-securing-ai-agents/code_samples`. Laluan fikstur di bawah adalah relatif
kepada direktori tersebut.

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

Dari akar repositori, pasang kebergantungan pelajaran dan jalankan:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Ujian ini melaksanakan contoh Python buku nota dan blok README yang tepat
di atas. Ia juga memeriksa bahawa pengubahan dan kekunci tanpa pin ditolak oleh
pengesah. Ujian melangkau sel setup `%pip` buku nota kerana kebergantungan
dipasang secara berasingan. Ia tidak mengubah buku nota atau fikstur.

## Bagaimana ini dijana

Fikstur menggunakan laluan kod yang sama seperti buku nota, dengan satu kunci tandatangan tetap
dan cap masa tetap untuk kebolehulangan bait. Untuk menjana semula:

```bash
python3 generate_fixtures.py
```

(Skrip terletak di `generate_fixtures.py` dalam direktori ini.)

## Apa yang pelajar pelajari daripada memeriksa JSON mentah

Membaca format resit mentah membina intuisinya yang tidak selalu disediakan oleh sel dalam buku nota.
Pelajar yang menyemak JSON sering perhatikan:

1. Tandatangan adalah rentetan base64url yang tidak jelas, tetapi setiap medan lain adalah JSON
   yang boleh dibaca dengan jelas. Tandatangan tidak menyulitkan kandungan; ia mengesahkannya.
2. `public_key` tertanam dalam resit, yang cukup untuk memeriksa
   konsistensi sendiri tetapi bukan kepercayaan penerbit. Pemeriksa mesti membandingkannya dengan kekunci
   yang dipin di luar resit atau diselesaikan melalui registri yang dipercayai.
3. Mengubah satu aksara mana-mana medan, kemudian membandingkan semula fail ini dengan
   `02_tampered_receipt.json`, menjadikan mekanisme paras bait itu jelas dan nyata.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->