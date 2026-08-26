# Sample Receipt Fixtures

Tri pre-gen-generated receipt files for inspection without running the notebook.

| File | Wetin e be |
|---|---|
| `01_valid_receipt.json` | A correct signed receipt for one `lookup_flights` tool call. Verification go return True. |
| `02_tampered_receipt.json` | Same receipt but one field change after dem sign am. Verification go return False. |
| `03_chain_three_receipts.json` | Chain of three correct receipts (search, hold, book) wey `previous_receipt_hash` link each one to the one before am. |

The fixtures dey sign the payload's canonical JCS bytes directly with Ed25519.
SHA-256 still dey use for content digests and receipt-chain links, no be as
extra pre-hash before dem sign.

## How to verify the samples

The notebook go show how to verify am for four sections. If you want verify these fixtures
direct without to run the notebook story:

```python
import json
from pathlib import Path

# E assume say you don finish di imports and helper functions
# from sections 1 and 2 of 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # True

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # False

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## How dem generate dem

The fixtures use the same code path as the notebook, with one fixed signing key
and fixed timestamps for byte-reproducibility. If you wan regenerate:

```bash
python3 generate_fixtures.py
```

(Script dey for `generate_fixtures.py` for this directory.)

## Wetin pikin dem go learn if dem inspect raw JSON

If you read the raw receipt format, e go help you know better pass wetin the cells for the notebook
dey show. Students wey just quickly look the JSON go notice:

1. The signature na opaque base64url string, but all other fields na plain
   readable JSON. The signature no encrypt the content; e just attest to am.
2. The `public_key` dey inside the receipt. Auditor no need anything else
   to verify (if im trust say the key really belong to the person wey dem claim be
   the issuer; check the lesson README about identity infrastructure).
3. If you change just one character for any field, then compare this file with
   `02_tampered_receipt.json`, e go make the byte-level mechanism clear.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->