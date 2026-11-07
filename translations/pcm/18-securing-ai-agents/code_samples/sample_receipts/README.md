# Sample Receipt Fixtures

Fo pre-generated receipt files wey u fit check without run di notebook.

| File | Wetin e be |
|---|---|
| `01_valid_receipt.json` | Valid signed receipt for one `lookup_flights` tool call. Verification go return True. |
| `02_tampered_receipt.json` | The same receipt but one field change after dem don sign am. Verification go return False. |
| `03_chain_three_receipts.json` | Chain of three valid receipts (search, hold, book) wey get `previous_receipt_hash` wey dey link each one to di previous one. |
| `04_resigned_receipt.json` | Same receipt wey attacker change then sign again with im own public key inside am. E go verify with di key inside am but no go work for issuer key. |

Di fixtures dey sign di payload's canonical JCS bytes straight with Ed25519.
SHA-256 still dey use for content digests and receipt-chain links, no be as
extra pre-hash before e sign.

## How to verify di samples

For `18-signed-receipts.ipynb`, run Setup and Sections 1 to 3 first.
Section 3 dey define `verify_chain`; Sections 1 and 2 alone no go complete.
Then run the next block for new cell, and make di notebook working directory
be set to `18-securing-ai-agents/code_samples`. Di fixture paths below na relative
to dat directory.

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

### How to check di example without Jupyter

From di repository root, install lesson dependencies then run:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

These tests dey run di notebook Python examples and di exact README block
wey dey above. Dem dey also check say tampering and unpinned keys no go pass
di verifiers. Tests no run di notebook’s `%pip` setup cell because dependencies
dem don install separate. Tests no go change di notebook or fixtures.

## How dem generate these tins

Di fixtures dey use di same code path as di notebook, with one constant signing key
and fixed timestamps make dem fit repeat same bytes. To regenerate:

```bash
python3 generate_fixtures.py
```

(Script dey for `generate_fixtures.py` inside dis directory.)

`../test_signed_receipts.py` go check all dis automatically: e go run di
notebook code, verify these four fixtures with di notebook's
`verify_receipt` and `verify_chain`, then confirm say regenerating di
fixtures go give identical bytes. From `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Wetin students fit learn from inspecting raw JSON

Reading di raw receipt format go build intuition wey di notebook cells
no always show. Students wey dey look through di JSON often notice say:

1. Di signature na opaque base64url string, but all others fields na plain
   readable JSON. Di signature no dey encrypt di content; e just talk say di content dey legit.
2. Di `public_key` dey inside di receipt, wey make di file
   self-contained but no be di one wey auditor dey verify against. Make u compare
   `02_tampered_receipt.json` and `04_resigned_receipt.json`: both of dem
   modify after dem don sign, but di second one dem sign again with di attacker's
   own key, so e verify with di key wey e carry. Di embedded key
   show say di file dey internally consistent. Only key wey person get
   from outside fit tell who issue am.
3. If person change one single character for any field outside `signature`, then
   check am again with `02_tampered_receipt.json`, e go make di
   byte-level mechanism clear.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->