# Sample Receipt Fixtures

Tri pre-generate receipt files wey you fit check without to run the notebook.

| File | Wetin e be |
|---|---|
| `01_valid_receipt.json` | Na valid signed receipt for `lookup_flights` tool call. Verification dey give True. |
| `02_tampered_receipt.json` | Di same receipt wit one field wey dem modify after dem sign am. Verification dey give False. |
| `03_chain_three_receipts.json` | Chain of three correct receipts (search, hold, book) wey `previous_receipt_hash` dey link each other. |

Di fixtures dey sign di payload's correct JCS bytes direct wit Ed25519.
SHA-256 still dey use for content digests and receipt-chain links, no be as
extra pre-hash before the signing.

## How to verify di samples

For `18-signed-receipts.ipynb`, run Setup and Sections 1 to 3 first.
Section 3 define `verify_chain`; Sections 1 and 2 alone no reach.
Then run di next block for new cell, and make sure say di notebook working directory
set to `18-securing-ai-agents/code_samples`. Di fixture paths for below dey relative
to dat directory.

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

### How to check di example without Jupyter

From the repository root, install di lesson dependencies and run:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

These tests go run all di notebook Python examples and di exact README block
wey dey above. Dem still dey check say no tampering or unpinned keys fit pass by di
verifiers. Di tests no go run di notebook's `%pip` setup cell because dependencies
dem install separate. Dem no go change di notebook or di fixtures.

## How dem generate dem

Di fixtures use di same code path as di notebook, with one fixed signing key
and fixed timestamps to make di bytes reproducible. To regenerate dem:

```bash
python3 generate_fixtures.py
```

(Script dey for `generate_fixtures.py` inside dis directory.)

## Wetin students dey learn from to inspect raw JSON

To read di raw receipt format go build intuition wey di cells for di notebook no always fit give.
Students wey dey look quick quick di JSON dey often notice:

1. Di signature na opaque base64url string, but every other field na normal
   readable JSON. Di signature no dey encrypt di content; e just dey confirm am.
2. Di `public_key` dey inside di receipt, wey enough for check
   self-consistency but e no reach issuer trust. Auditor must compare am wit key
   wey dem pin outside di receipt or wey dem resolve through trusted registry.
3. If person modify one character for any field, then compare am again wit
   `02_tampered_receipt.json`, e go make di byte-level mechanism clear.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->