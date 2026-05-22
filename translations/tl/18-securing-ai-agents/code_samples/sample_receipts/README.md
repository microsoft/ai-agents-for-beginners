# Sample Receipt Fixtures

Tatlong pre-generated na mga file ng resibo para sa inspeksyon nang hindi pinapatakbo ang notebook.

| File | Ano ito |
|---|---|
| `01_valid_receipt.json` | Isang valid na nilagdang resibo para sa `lookup_flights` tool call. Ang beripikasyon ay nagbabalik ng True. |
| `02_tampered_receipt.json` | Ang parehong resibo na may isang field na binago matapos lagdaan. Ang beripikasyon ay nagbabalik ng False. |
| `03_chain_three_receipts.json` | Isang chain ng tatlong valid na mga resibo (search, hold, book) na may `previous_receipt_hash` na nag-uugnay ng bawat isa sa naunang isa. |

## Pag-beripika sa mga sample

Ang notebook ay naglalakad sa beripikasyon sa apat na seksyon. Upang beripikahin ang mga fixture na ito
direkta nang hindi nagpapatakbo sa kuwentong notebook:

```python
import json
from pathlib import Path

# Ipinagpapalagay na natapos mo na ang mga imports at helper functions
# mula sa mga seksyon 1 at 2 ng 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Tama

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Mali

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Paano ito ginawa

Ang mga fixture ay gumagamit ng parehong daan ng code tulad ng notebook, na may isang fixed na signing key
at fixed na mga timestamp para sa byte-reproducibility. Upang muling likhain:

```bash
python3 generate_fixtures.py
```

(Ang script ay nasa `generate_fixtures.py` sa direktoryong ito.)

## Ano ang natutunan ng mga estudyante mula sa pagsusuri ng raw JSON

Ang pagbabasa ng raw na format ng resibo ay nagtatatag ng intuwisyon na hindi palaging naibibigay ng mga cell sa notebook.
Ang mga estudyanteng mabilis na tumingin sa JSON ay madalas napapansin:

1. Ang lagda ay isang opaque na base64url string, ngunit bawat ibang field ay plain
   readable JSON. Hindi ini-encrypt ng lagda ang nilalaman; pinatutunayan nito ito.
2. Ang `public_key` ay naka-embed sa resibo. Hindi kailangan ng auditor ng anumang iba pa
   para magberipika (depende sa pagtitiwala na ang key ay talagang pag-aari ng sinasabing
   nag-isyu; tingnan ang lesson README tungkol sa identity infrastructure).
3. Ang pagbabago ng isang karakter sa anumang field, pagkatapos ay muling paghahambingin ang file na ito sa
   `02_tampered_receipt.json`, ay nagpapalinaw ng byte-level na mekanismo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->