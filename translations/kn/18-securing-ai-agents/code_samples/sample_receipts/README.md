# ಮಾದರಿ ರಸೀದಿ ಫಿಕ್ಸ್ಚರ್ಸ್

ನೋಟ್ಬುಕ್ ಓಡಿಸದೆ ಪರಿಶೀಲನೆಗಾಗಿ ಮುಂಚಿತವಾಗಿ ರಚಿಸಲಾದ ನಾಲ್ಕು ರಸೀದಿ ಫೈಲ್‌ಗಳು.

| ಫೈಲ್ | ಅದು ಏನು |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` ಉಪಕರಣ ಕರೆಗಾಗಿ ಮಾನ್ಯವಾದ ಸಹಿ ಮಾಡಿದ ರಸೀದಿ. ಪರಿಶೀಲನೆ ಸತ್ಯವನ್ನು ನೀಡುತ್ತದೆ. |
| `02_tampered_receipt.json` | ಸಹಿ ಮಾಡಿದ ನಂತರ ಒಂದೊಂದರ ಕ್ಷೇತ್ರವನ್ನು ಬದಲಾಯಿಸಿದ ಅದೇ ರಸೀದಿ. ಪರಿಶೀಲನೆ ಅಸತ್ಯವನ್ನು ನೀಡುತ್ತದೆ. |
| `03_chain_three_receipts.json` | ಮೂರು ಮಾನ್ಯ ರಸೀದಿಗಳ ಸರಪಳಿ (ಹುಡುಕು, ಹಿಡಿದಿಡು, ಪುಸ್ತಕ) ಪ್ರತಿಯೊಂದನ್ನು ಹಿಂದಿನದೊಂದಕ್ಕೆ ಜೋಡಿಸುವ `previous_receipt_hash` ಸಹಿತ. |
| `04_resigned_receipt.json` | ಅದೇ ರಸೀದಿಯನ್ನು ದಾಳಿಕೋರನು ತಿರುಮಾಡಿ ಪುನಃ ಸಹಿ ಮಾಡಿದದ್ದು, ದಾಳಿಕೋರನ ಸ್ವಂತ ಸಾರ್ವಜನಿಕ ಕೀಲನ್ನು ಒಳಗೊಂಡಿದೆ. ಅದರಲ್ಲಿ ಇರುವ ಕೀಲಿಗೆ ವಿರುದ್ಧ ಪರಿಶೀಲಿಸುತ್ತದೆ. ಮುದ్రಣಕರ ಕೀಲಿಗೆ ವಿರುದ್ಧ ವಿಫಲವಾಗುತ್ತದೆ. |

ಫಿಕ್ಸ್ಚರ್ಸ್ ಪೇಲೋಡ್‌ನ ಮಾನ್ಯ JCS ಬೈಟ್‌ಗಳನ್ನು ನೇರವಾಗಿ Ed25519 ಮೂಲಕ ಸಹಿ ಮಾಡುತ್ತವೆ.
ವಸ್ತು ಸಂಕ್ಷೇಪಣೆ ಮತ್ತು ರಸೀದಿ-ಸ೦ಪರ್ಕಿಕ ಸಂಪರ್ಕಗಳಿಗೆ SHA-256 ಬಳಸಲಾಗುತ್ತದೆ, ಸಹಿ ಮಾಡುವ ಮೊದಲು ಹೆಚ್ಚುವರಿ ಪೂರ್ವ-ಹ್ಯಾಷ್ ಆಗಿ ಅಲ್ಲ.


## ಮಾದರಿಗಳನ್ನು ಪರಿಶೀಲಿಸುವುದು

`18-signed-receipts.ipynb` ನಲ್ಲಿ, ಮೊದಲು Setup ಮತ್ತು ವಿಭಾಗಗಳು 1 ರಿಂದ 3 ರವರೆಗೆ ಓಡಿಸಿ.
ವಿಭಾಗ 3 `verify_chain` ವ್ಯಾಖ್ಯಾನಿಸುತ್ತದೆ; ವಿಭಾಗ 1 ಮತ್ತು 2 ಮಾತ್ರ ಸಾಕಾಗುವುದಿಲ್ಲ.
ನಂತರ ಕೆಳಗಿನ ಬ್ಲಾಕ್ ಅನ್ನು ಹೊಸ ಸೆಲ್ ನಲ್ಲಿ ಜಾನುವ, ನೋಟ್ಬುಕ್‌ನ ಕಾರ್ಯ ನಿರ್ವಹಣಾ ಡೈರೆಕ್ಟರಿ
`18-securing-ai-agents/code_samples` ಗೆ ಹೊಂದಿಸಲಾಗಿದೆ. ಕೆಳಗಿನ ಫಿಕ್ಸ್ಚರ್ ಪಥಗಳು ಆ ಡೈರೆಕ್ಟರಿಗೆ
ಸಂಬಂಧಿಸಿದೆ.

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

### ಜೂಪೈಟರ್ ಇಲ್ಲದೆ ಉದಾಹರಣೆಯನ್ನು ಪರಿಶೀಲಿಸುವುದು

ರೆಪೊಸಿಟರಿ ಮೂಲದಿಂದ, ಪಾಠದ ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ ಮತ್ತು ರನ್ ಮಾಡಿ:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

ಈ ಪರೀಕ್ಷೆಗಳು Ноಟ್ಬುಕ್‌ನ Python ಉದಾಹರಣೆಗಳನ್ನು ಮತ್ತು ನಿಖರ README ಬ್ಲಾಕ್ ಅನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸುತ್ತವೆ
ಮೇಲ್ಭಾಗ. ಅವು ತಪಾಸಕರು ತೊಂದರೆಯಾದ ಮತ್ತು ಅంకಿತವಿಲ್ಲದ ಕೀಲುಗಳನ್ನು ತಿರಸ್ಕರಿಸುತ್ತವೆ ಎಂದು ಕೂಡ ಪರಿಶೀಲಿಸುತ್ತವೆ.
ಪರೀಕ್ಷೆಗಳು ನೋಟ್ಬುಕ್‌ನ `%pip` ಸೆಟ್‌ಅಪ್ ಸೆಲ್ ಅನ್ನು ತಪ್ಪಿಸುವುವು ಏಕೆಂದರೆ ಅವಲಂಬನೆಗಳು
ಪ್ರತ್ಯೇಕವಾಗಿ ಸ್ಥಾಪಿತವಾಗಿವೆ. ಅವರು ನೋಟ್ಭುಕ್ ಅಥವಾ ಫಿಕ್ಸ್ಚರ್‌ಗಳನ್ನು ಬದಲಿಸುವುದಿಲ್ಲ.

## ಇವು ಹೇಗೆ ರಚಿಸಲ್ಪಟ್ಟವು

ಫಿಕ್ಸ್ಚರ್‌ಗಳು ನೋಟ್ಬುಕ್‌ನಂತೆ ಒಂದೇ ಕೋಡ್ ಮಾರ್ಗವನ್ನು ಬಳಸುತ್ತವೆ, ಒಂದು ಸ್ಥಿರ ಸಹಿಯ ಕೀ ಮತ್ತು
ಸ್ಥಿರ ಟೈಮ್ಸ್ಟ್ಯಾಂಪ್ಗಳೊಂದಿಗೆ ಬೈಟ್ ಪುನರಾವೃತಿಗಾಗಿ. ಮರುರಚಿಸಲು:

```bash
python3 generate_fixtures.py
```

(ಸ್ಕ್ರಿಪ್ಟ್ ಈ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ `generate_fixtures.py` ನಲ್ಲಿ ಇದೆ.)

`../test_signed_receipts.py` ಈ ಎಲ್ಲವನ್ನೂ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪರಿಶೀಲಿಸುತ್ತದೆ: ಇದು
ನೋಟ್ಬುಕ್‌ನ ಕೋಡ್ ಅನ್ನು ಚಲಾಯಿಸುತ್ತದೆ, ಈ ನಾಲ್ಕು ಫಿಕ್ಸ್ಚರ್‌ಗಳನ್ನೂ ನೋಟ್ಬುಕ್‌ನ
`verify_receipt` ಮತ್ತು `verify_chain` ಸಹಿತ ಪರಿಶೀಲಿಸುತ್ತದೆ, ಮತ್ತು ಫಿಕ್ಸ್ಚರ್‌ಗಳನ್ನು ಮರುರಚನೆ
ಯಾಗು ಬಿಟ್ಟೆಟ್‌ಗಳು ಸಮಾನವಾಗಿವೆ ಎಂದು ದೃಢಪಡಿಸುತ್ತದೆ. `code_samples` ನಿಂದ:

```bash
python -m unittest test_signed_receipts
```

## ವಿದ್ಯಾರ್ಥಿಗಳು ಕಚ್ಚಾ JSON ಪರಿಶೀಲಿಸುವ ಮೂಲಕ ಏನು ಕಲಿಯುತ್ತಾರೆ

ಕಚ್ಚಾ ರಸೀದಿ ಫಾರ್ಮ್ಯಾಟ್ ಓದುವುದರಿಂದ ನೋಟ್ಬುಕ್‌ನ ಸೆಲ್‌ಗಳು ಎಂದಿಗೂ ನೀಡದ ಅಂಶಗಳೂ ಸಹ ಗ್ರಹಿಸಬಹುದು.
JSON ಅನ್ನು ಸ್ಕಿಮ್ ಮಾಡಿದ ವಿದ್ಯಾರ್ಥಿಗಳು ಹೀಗೇ ಗಮನಿಸುತ್ತಾರೆ:

1. ಸಹಿ ಒಂದು ಅಪಾರದ ಅತ್ಯುತ್ತಮ ಬೇರ್ಲ 64-url ಸ್ಟ್ರಿಂಗಾಗಿದ್ದು, ಇತರ ಎಲ್ಲ ಕ್ಷೇತ್ರಗಳು ಸರಳವಾಗಿವೆ
   ಓದಲು ಸಿಗುವ JSON. ಸಹಿ ವಸ್ತುವನ್ನು ಎನ್ಕ್ರಿಪ್ಟ್ ಮಾಡೋದಿಲ್ಲ; ಅದು ಅದಕ್ಕೆ ಸಾಕ್ಷ್ಯ ಕೊಡುವದು.
2. `public_key` ರ್ಸಿ ಪ್ರಾಪ್ತಿಯಲ್ಲಿ ನುಡಿದುಹೋಗಿದ್ದು, ಇದರಿಂದ ಫೈಲ್
   ಸ್ವಯಂ-ಸಂಯೋಜಿತವಾಗಿದೆ ಆದರೆ ಆ ಅದಾಲತಿಗಾರರು ಪರಿಶೀಲಿಸುವುದಕ್ಕಾಗಿರುವುದು ಅಲ್ಲ. ಹೋಲಿಸಿ
   `02_tampered_receipt.json` ಮತ್ತು `04_resigned_receipt.json`: ಎರಡೂ ಸಹ ಸಹಿ ಹಾಕಿದ ನಂತರ ಬದಲಾವಣೆಗೊಂಡವು,
   ಆದರೆ ಎರಡನೆಯದು ದಾಳಿಕಾರರ ಸ್ವಂತ ಕೀಯಿಂದ ಮರು-ಸಹಿ ಮಾಡಲಾಯಿತು,
   ಆದ್ದರಿಂದ ಅದು ಅದರಲ್ಲಿರುವ ಕೀ ವಿರುದ್ಧವಾಗಿ ಪರಿಶೀಲಿಸುತ್ತದೆ. ಆ ಧಾರಿತ ಕೀ
   ಫೈಲ್ ಅಂತರ್ಗತವಾಗಿ ಸಾತ್\u200cಯವಾಗಿದೆಯೆಂದು ನಿಮಗೆ ಹೇಳುತ್ತದೆ. ಕೇವಲ ಪಡೆದ ಕೇ ಮಾತ್ರ
   ಮರುಬಳಸಿದವರು ಯಾರಂದರೆಂದು ಬೇರೆಡೆ ತಿಳಿಸುತ್ತದೆ.
3. `signature` ಹೊರಗಿನ ಯಾವುದೇ ಕ್ಷೇತ್ರದ ಒಂದು ಅಕ್ಷರವನ್ನು ಸಂಪಾದಿಸಿದ ನಂತರ,
   ಈ ಫೈಲನ್ನು `02_tampered_receipt.json` ಜೊತೆಗೆ ಮರು-ಹೋಲಿಸಿದರೆ,
   ಬೈಟ್-ಮಟ್ಟದ ಯಂತ್ರಗಳನ್ನು ಸ್ಪಷ್ಟಪಡಿಸುತ್ತದೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->