# Sample Receipt Fixtures

Three pre-generated receipt files for inspection without running the notebook.

| File | What it is |
|---|---|
| `01_valid_receipt.json` | A valid signed receipt for a `lookup_flights` tool call. Verification returns True. |
| `02_tampered_receipt.json` | The same receipt with one field modified after signing. Verification returns False. |
| `03_chain_three_receipts.json` | A chain of three valid receipts (search, hold, book) with `previous_receipt_hash` linking each to the prior one. |

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

## What students learn from inspecting raw JSON

Reading the raw receipt format builds intuition that the cells in the notebook
do not always provide. Students who skim the JSON often notice:

1. The signature is an opaque base64url string, but every other field is plain
   readable JSON. The signature does not encrypt the content; it attests to it.
2. The `public_key` is embedded in the receipt, which is enough to check
   self-consistency but not issuer trust. An auditor must compare it with a key
   pinned outside the receipt or resolved through a trusted registry.
3. Modifying a single character of any field, then re-comparing this file with
   `02_tampered_receipt.json`, makes the byte-level mechanism concrete.
