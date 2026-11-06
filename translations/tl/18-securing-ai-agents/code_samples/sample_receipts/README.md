# Mga Halimbawang Resibo

Tatlong paunang-gawang mga file ng resibo para sa pagsusuri nang hindi pinapatakbo ang notebook.

| File | Ano ito |
|---|---|
| `01_valid_receipt.json` | Isang valid na pinirmahang resibo para sa isang `lookup_flights` tool call. Ang beripikasyon ay nagbabalik ng True. |
| `02_tampered_receipt.json` | Parehong resibo na may isang field na binago pagkatapos ng pagpirma. Ang beripikasyon ay nagbabalik ng False. |
| `03_chain_three_receipts.json` | Isang chain ng tatlong valid na mga resibo (search, hold, book) na may `previous_receipt_hash` na nag-uugnay sa bawat isa sa nauna. |

Direktang pinipirmahan ng mga fixtures ang canonical JCS bytes ng payload gamit ang Ed25519.
Patuloy ang paggamit ng SHA-256 para sa content digests at links ng receipt-chain, hindi bilang
dagdag na pre-hash bago magpirma.

## Pagberipika sa mga halimbawa

Sa `18-signed-receipts.ipynb`, patakbuhin muna ang Setup at mga Seksyon 1 hanggang 3.
Tinukoy sa Seksyon 3 ang `verify_chain`; hindi sapat ang Seksyon 1 at 2 lamang.
Pagkatapos ay patakbuhin ang sumusunod na block sa bagong cell, na ang working directory ng notebook
ay nakatakda sa `18-securing-ai-agents/code_samples`. Ang mga daan ng fixture sa ibaba ay relative
sa direktoryong iyon.

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

### Pagsusuri ng halimbawa nang walang Jupyter

Mula sa ugat ng repository, i-install ang mga dependency ng aralin at patakbuhin:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Pinapatakbo ng mga test na ito ang mga halimbawa sa Python ng notebook at ang eksaktong README block
sa itaas. Sinusuri rin nila na tinatanggihan ang mga peke at hindi naka-pin na mga key ng mga
verifier. Nilalaktawan ng mga test ang `%pip` setup cell ng notebook dahil naka-install ang mga dependency nang hiwalay. Hindi nila binabago ang notebook o mga fixture.


## Paano ito ginawa

Ginagamit ng mga fixtures ang parehong path ng code gaya ng notebook, na may isang fixed na signing key
at fixed na mga timestamp para sa reproducibility ng bytes. Para gumawa muli:

```bash
python3 generate_fixtures.py
```

(Nasa `generate_fixtures.py` ang Script sa direktoryong ito.)

## Ano ang natutunan ng mga estudyante mula sa pagsusuri ng raw JSON

Ang pagbabasa ng raw na format ng resibo ay nagbibigay ng intuition na hindi palaging naibibigay ng mga cell sa notebook.
Madalas na napapansin ng mga estudyante na dumadaan sa JSON ang mga sumusunod:

1. Ang lagda ay isang opaque na base64url na string, ngunit ang bawat ibang field ay malinaw na
   nababasa na JSON. Hindi in-eencrypt ng lagda ang nilalaman; pinatutunayan nito ito.
2. Ang `public_key` ay naka-embed sa resibo, na sapat upang suriin ang
   self-consistency ngunit hindi ang pagkakatiwalaan sa issuer. Kailangang icompare ito ng auditor sa key
   na naka-pin sa labas ng resibo o naayos sa pamamagitan ng isang pinagkakatiwalaang registry.
3. Ang pagbabago ng isang karakter sa kahit anumang field, pagkatapos ay muling pag-compare ng file na ito sa
   `02_tampered_receipt.json`, ay nagpapakita ng mekanismo sa byte-level nang konkreto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->