# Sample Receipt Fixtures

Four pre-generated receipt files for inspection without running the notebook.

| File | What it is |
|---|---|
| `01_valid_receipt.json` | A valid signed receipt for a `lookup_flights` tool call. Verification returns True. |
| `02_tampered_receipt.json` | The same receipt with one field modified after signing. Verification returns False. |
| `03_chain_three_receipts.json` | A chain of three valid receipts (search, hold, book) with `previous_receipt_hash` linking each to the prior one. |
| `04_resigned_receipt.json` | The same receipt tampered with and then re-signed by an attacker, with the attacker's own public key embedded. Verifies against the key inside it. Fails against the issuer's key. |

The fixtures sign the payload's canonical JCS bytes directly with Ed25519.
SHA-256 remains in use for content digests and receipt-chain links, not as an
extra pre-hash before signing.

## Verifying the samples

In `18-signed-receipts.ipynb`, run Setup and Sections 1 through 3 first.
Section 3 defines `verify_chain`; Sections 1 and 2 alone are not enough.
Then run the following block in a new cell, with the notebook's working directory
set to `18-securing-ai-agents/code_samples`. The fixture paths below are relative
to that directory.

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# The issuer's key, pinned here rather than read from any receipt. In a real
# deployment it comes from the issuer's JWK Set or a pinned config value.
# This is the public half of the fixed signing key in generate_fixtures.py.
ISSUER_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid, ISSUER_KEY)}")        # True

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered, ISSUER_KEY)}")  # False

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain, ISSUER_KEY):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")

# The forgery. Verified against the key it carries, it passes. Against the
# issuer's key, it fails. Only the second question is worth asking.
forged = json.loads(Path("04_resigned_receipt.json").read_text())
print(f"Forged, checked against its own key: "
      f"{verify_receipt(forged, forged['signature']['public_key'])}")  # True
print(f"Forged, checked against issuer key:  "
      f"{verify_receipt(forged, ISSUER_KEY)}")                        # False
```

### Checking the example without Jupyter

From the repository root, install the lesson dependencies and run:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

These tests execute the notebook's Python examples and the exact README block
above. They also check that tampering and unpinned keys are rejected by the
verifiers. The tests skip the notebook's `%pip` setup cell because dependencies
are installed separately. They do not change the notebook or fixtures.

## How these were generated

The fixtures use the same code path as the notebook, with one fixed signing key
and fixed timestamps for byte-reproducibility. To regenerate:

```bash
python3 generate_fixtures.py
```

(Script is at `generate_fixtures.py` in this directory.)

`../test_signed_receipts.py` checks all of this automatically: it runs the
notebook's code, verifies these four fixtures with the notebook's
`verify_receipt` and `verify_chain`, and confirms that regenerating the
fixtures gives identical bytes. From `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## What students learn from inspecting raw JSON

Reading the raw receipt format builds intuition that the cells in the notebook
do not always provide. Students who skim the JSON often notice:

1. The signature is an opaque base64url string, but every other field is plain
   readable JSON. The signature does not encrypt the content; it attests to it.
2. The `public_key` is embedded in the receipt, which makes the file
   self-contained but is not what an auditor verifies against. Compare
   `02_tampered_receipt.json` with `04_resigned_receipt.json`: both were
   altered after signing, but the second was re-signed with the attacker's
   own key, so it verifies against the key it carries. The embedded key
   tells you the file is internally consistent. Only a key obtained
   elsewhere tells you who issued it.
3. Modifying a single character of any field outside `signature`, then
   re-comparing this file with `02_tampered_receipt.json`, makes the
   byte-level mechanism concrete.
