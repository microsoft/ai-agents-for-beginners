# Mga Halimbawang Resibo na Fixtures

Apat na pre-generated na mga file ng resibo para sa inspeksyon nang hindi na kailangang patakbuhin ang notebook.

| File | Ano ito |
|---|---|
| `01_valid_receipt.json` | Isang balidong naka-sign na resibo para sa isang `lookup_flights` na tawag sa tool. Nagbabalik ang beripikasyon ng True. |
| `02_tampered_receipt.json` | Parehong resibo ngunit may isang field na binago pagkatapos ng pag-sign. Nagbabalik ang beripikasyon ng False. |
| `03_chain_three_receipts.json` | Isang chain ng tatlong balidong resibo (search, hold, book) na may `previous_receipt_hash` na nag-uugnay sa bawat isa sa naunang resibo. |
| `04_resigned_receipt.json` | Parehong resibo na inalamang binago at pagkatapos ay muling nilagdaan ng isang atake, na may pampublikong susi ng umaatake na naka-embed. Nabeberipika laban sa susi na nasa loob nito. Nabibigo laban sa susi ng issuer. |

Nilalagdaan ng mga fixtures ang canonical JCS bytes ng payload nang direkta gamit ang Ed25519.
Ginagamit pa rin ang SHA-256 para sa mga content digest at mga koneksyon sa chain ng resibo, hindi bilang
dagdag na pre-hash bago ang pag-sign.

## Pagbeberipika sa mga Halimbawa

Sa `18-signed-receipts.ipynb`, patakbuhin muna ang Setup at Sections 1 hanggang 3.
Tinukoy sa Section 3 ang `verify_chain`; Hindi sapat ang Sections 1 at 2 lamang.
Pagkatapos ay patakbuhin ang sumusunod na block sa isang bagong cell, na ang working directory ng notebook
ay nakatakda sa `18-securing-ai-agents/code_samples`. Ang mga path ng fixture sa ibaba ay relative
sa direktoryong iyon.

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

### Pagsusuri sa halimbawa nang walang Jupyter

Mula sa root ng repository, i-install ang mga dependency ng aralin at patakbuhin:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Pinapatakbo ng mga pagsusulit na ito ang mga halimbawa ng Python sa notebook at ang eksaktong README block
sa itaas. Sinusuri rin nila na tinatanggihan ng mga
verifier ang mga na-tamper at mga hindi naka-pin na mga susi. Nilalaktawan ng mga pagsusulit ang setup cell na `%pip` ng notebook dahil ang mga dependency
ay na-install nang hiwalay. Hindi nila binabago ang notebook o mga fixtures.

## Paano ito na-generate

Ginagamit ng mga fixtures ang parehong code path tulad ng notebook, na may isang fixed na signing key
at mga fixed na timestamp para sa byte-reproducibility. Para mag-regenerate:

```bash
python3 generate_fixtures.py
```

(Ang script ay nasa `generate_fixtures.py` sa direktoryong ito.)

Ang `../test_signed_receipts.py` ay awtomatikong sinusuri ang lahat ng ito: pinapatakbo nito ang
code ng notebook, binibeberipika ang apat na fixtures na ito gamit ang
`verify_receipt` at `verify_chain` ng notebook, at kinukumpirma na ang muling pag-generate ng
mga fixtures ay nagbibigay ng magkaparehong bytes. Mula sa `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Ano ang natututuhan ng mga estudyante mula sa pag-inspeksyon ng raw JSON

Ang pagbabasa ng raw na format ng resibo ay nagpapalawak ng intuwisyon na hindi palaging naibibigay ng mga cell sa notebook.
Madalas mapansin ng mga estudyante na nagmamadaling tingnan ang JSON:

1. Ang pirma ay isang opaque na base64url na string, ngunit ang bawat ibang field ay plain
   at nababasang JSON. Hindi ini-encrypt ng pirma ang nilalaman; pinatutunayan nito ito.
2. Ang `public_key` ay naka-embed sa resibo, na ginagawa ang file na
   self-contained ngunit hindi ito ang sinusuri ng auditor. Ihambing ang
   `02_tampered_receipt.json` sa `04_resigned_receipt.json`: pareho itong
   binago pagkatapos papanigan, ngunit ang pangalawa ay muling nilagdaan gamit ang sariling
   susi ng umaatake, kaya ito ay nabeberipika laban sa susi na daladala nito. Ang naka-embed na susi
   ay nagsasabi sa iyo na ang file ay internally consistent. Ang susi na nakuha
   mula sa ibang lugar lang ang nagsasabi kung sino ang nag-isyu nito.
3. Ang pagbabago ng isang karakter sa kahit anong field sa labas ng `signature`, pagkatapos
   muling paghahambing ng file na ito gamit ang `02_tampered_receipt.json`, ay ginagawa ang
   mekanismo sa antas ng byte na mas konkreto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->