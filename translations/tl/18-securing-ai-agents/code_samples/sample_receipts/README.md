# Mga Halimbawang Resibo

Tatlong paunang-generate na mga file ng resibo para sa inspeksyon nang hindi pinapatakbo ang notebook.

| File | Ano ito |
|---|---|
| `01_valid_receipt.json` | Isang wastong pirmadong resibo para sa tawag ng tool na `lookup_flights`. Ang beripikasyon ay nagbabalik ng True. |
| `02_tampered_receipt.json` | Ang parehong resibo na may isang field na binago pagkatapos pirmahan. Ang beripikasyon ay nagbabalik ng False. |
| `03_chain_three_receipts.json` | Isang chain ng tatlong wastong resibo (search, hold, book) na may `previous_receipt_hash` na nag-uugnay ng bawat isa sa naunang resibo. |

Pinipirmahan ng mga fixtures ang canonical JCS na mga bytes ng payload nang direkta gamit ang Ed25519.
Ginagamit pa rin ang SHA-256 para sa mga content digest at mga link ng receipt-chain, hindi bilang
karagdagang pre-hash bago pirmahan.

## Pagberipika ng mga halimbawa

Tinatalakay ng notebook ang pagberipika sa apat na bahagi. Para direktang beripikahin ang mga fixtures
na ito nang hindi dumadaan sa kwento ng notebook:

```python
import json
from pathlib import Path

# Inaakala na nakumpleto mo na ang mga import at helper functions
# mula sa mga seksyon 1 at 2 ng 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Totoo

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Mali

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Paano ito ginawa

Ginagamit ng mga fixtures ang parehong code path ng notebook, na may isang fixed na signing key
at fixed na mga timestamp para sa byte-reproducibility. Para gumawa muli:

```bash
python3 generate_fixtures.py
```

(Ang script ay nasa `generate_fixtures.py` sa direktoryong ito.)

## Ano ang natutunan ng mga estudyante mula sa pag-inspeksyon ng raw JSON

Ang pagbabasa ng raw na format ng resibo ay nagtuturo ng intuwisyon na hindi palaging ibinibigay ng mga cell sa notebook.
Madalas napapansin ng mga estudyante na sumusuri sa JSON:

1. Ang pirma ay isang opaque na base64url na string, ngunit bawat ibang field ay plain
   na nababasang JSON. Hindi ini-encrypt ng pirma ang nilalaman; pinatutunayan nito ito.
2. Ang `public_key` ay naka-embed sa resibo. Walang kailangan ang isang auditor
   para magberipika (maliban sa pagtitiwala na ang key ay talaga namang pag-aari ng sinasabing
   nag-isyu; tingnan ang lesson README tungkol sa identity infrastructure).
3. Ang pagbabago ng isang karakter ng anumang field, pagkatapos ay ihambing muli ang file na ito sa
   `02_tampered_receipt.json`, ay nagpap konkretong mekanismo sa byte-level.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->