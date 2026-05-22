# Sample Receipt Fixtures

Thri pre-generated receipt files for inspection without run di notebook.

| File | Wetin e be |
|---|---|
| `01_valid_receipt.json` | Valid signed receipt for `lookup_flights` tool call. Verification go return True. |
| `02_tampered_receipt.json` | Same receipt but one field modify after signing. Verification go return False. |
| `03_chain_three_receipts.json` | Chain of three valid receipts (search, hold, book) wit `previous_receipt_hash` weh link each one to di one wey dey before am. |

## Verifying the samples

Di notebook go show how to verify am for four sections. If you want verify these fixtures
direct without run di notebook talk:

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

## How dem generate am

Di fixtures use di same code path as di notebook, wit one fixed signing key
and fixed timestamps for byte-reproducibility. To generate am again:

```bash
python3 generate_fixtures.py
```

(Script dey for `generate_fixtures.py` for this directory.)

## Wetin students fit learn from inspecting raw JSON

Read di raw receipt format dey build intuition wey di cells for di notebook
no dey always show. Students wey just waka through di JSON go notice:

1. Di signature na opaque base64url string, but every other field na plain
   readable JSON. Di signature no dey encrypt di content; e dey confirm am.
2. Di `public_key` dey inside di receipt. Auditor no need anything else
   to verify (if dem trust say di key na correct one wey belong to di
   issuer wey dem talk about; see di lesson README on identity infrastructure).
3. If you modify one character for any field, then compare dis file wit
   `02_tampered_receipt.json`, e go make di byte-level mechanism clear.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->