# Sample Receipt Fixtures

Tri pre-generated receipt files wey you fit check without to run di notebook.

| File | Wetin e be |
|---|---|
| `01_valid_receipt.json` | Valid signed receipt for one `lookup_flights` tool call. Verification go return True. |
| `02_tampered_receipt.json` | Di same receipt but one field don change after e sign. Verification go return False. |
| `03_chain_three_receipts.json` | Chain of three valid receipts (search, hold, book) wey get `previous_receipt_hash` link each one to di one wey come before am. |

Di fixtures sign di payload's canonical JCS bytes direct with Ed25519.
SHA-256 still dey use for content digests and receipt-chain links, no be as
extra pre-hash before e sign.

## How to verify di samples

Di notebook waka through verification for four sections. If you wan verify these fixtures
direct without to run inside di notebook story:

```python
import json
from pathlib import Path

# E mean say you don finish the imports and helper functions
# from sections 1 and 2 of 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # True

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # False

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## How dem generate am

Di fixtures use di same code path like di notebook, with one fixed signing key
and fixed timestamps so dat di bytes go fit reproduce. To regenerate am:

```bash
python3 generate_fixtures.py
```

(Script dey for `generate_fixtures.py` inside dis directory.)

## Wetin students fit learn from inspecting raw JSON

Reading di raw receipt format dey help build intuition wey di cells for di notebook no
always dey show. Students wey dey look JSON well well dey notice:

1. Di signature na opaque base64url string, but every other field na plain
   readable JSON. Di signature no dey encrypt di content; e dey confirm am.
2. Di `public_key` dey inside di receipt. Auditor no need anything else
   to verify (if e trust say di key really belong to di person wey claim am;
   check di lesson README for identity infrastructure).
3. If person change even one character for any field, then compare di file with
   `02_tampered_receipt.json`, e go make di byte-level mechanism clear.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->