# Mga Sample na Resibo na Fixtures

Tatlong pre-generated na mga file ng resibo para sa inspeksyon nang hindi pinapatakbo ang notebook.

| File | Ano ito |
|---|---|
| `01_valid_receipt.json` | Isang valid na pirmahang resibo para sa tawag na `lookup_flights` tool. Nagbabalik ng True ang beripikasyon. |
| `02_tampered_receipt.json` | Ang parehong resibo na may isang field na binago pagkatapos pumirma. Nagbabalik ng False ang beripikasyon. |
| `03_chain_three_receipts.json` | Isang chain ng tatlong valid na resibo (search, hold, book) na may `previous_receipt_hash` na nag-uugnay bawat isa sa naunang resibo. |

Pinipirmahan ng fixtures ang canonical JCS bytes ng payload nang direkta gamit ang Ed25519.
Ang SHA-256 ay nananatiling ginagamit para sa content digests at mga link ng receipt-chain, hindi bilang isang
dagdag na pre-hash bago pumirma.

## Pagberipika ng mga sample

Nilalakbay ng notebook ang proseso ng pagberipika sa apat na seksyon. Upang i-verify ang mga fixtures
nang direkta nang hindi dumadaan sa kwento ng notebook:

```python
import json
from pathlib import Path

# Ipinapalagay na natapos mo na ang mga import at mga helper function
# mula sa mga sections 1 at 2 ng 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Totoo

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Mali

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Paano ito ginawa

Ginagamit ng fixtures ang parehong path ng code tulad ng sa notebook, na may isang fixed na signing key
at fixed na mga timestamp para sa reproducibility ng bytes. Upang muling gawin:

```bash
python3 generate_fixtures.py
```

(Ang script ay nasa `generate_fixtures.py` sa direktoryong ito.)

## Ano ang natututunan ng mga estudyante mula sa pagsusuri ng raw JSON

Ang pagbabasa ng raw receipt format ay nagtuturo ng intuwisyon na hindi palaging ibinibigay ng mga cell sa notebook.
Ang mga estudyanteng mabilis na tumingin sa JSON ay madalas napapansin:

1. Ang pirma ay isang opaque na base64url na string, ngunit ang bawat ibang field ay plain
   na nababasang JSON. Hindi ini-encrypt ng pirma ang nilalaman; pinatutunayan nito ito.
2. Ang `public_key` ay naka-embed sa resibo. Wala nang iba pang kailangan ang isang auditor
   upang ma-verify (basta't pinagkakatiwalaan na ang key ay talaga namang pag-aari ng inihayag na
   na issuer; tingnan ang README ng leksyon tungkol sa identity infrastructure).
3. Ang pagbabago ng isang karakter sa kahit anong field, pagkatapos ay pag-kompara muli sa file na ito gamit ang
   `02_tampered_receipt.json`, ay nagpapalinaw sa mekanismo sa lebel ng bytes.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->