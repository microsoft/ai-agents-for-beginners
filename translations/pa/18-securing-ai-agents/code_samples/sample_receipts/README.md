# ਨਮੂਨਾ ਰਸੀਦ ਫਿਕਸਚਰਜ਼

ਨੋਟਬੁੱਕ ਚਲਾਏ ਬਿਨਾਂ ਜਾਂਚ ਲਈ ਚਾਰ ਪਹਿਲਾਂ ਤੋਂ ਬਣਾਈ ਹੋਈਆਂ ਰਸੀਦਾਂ ਦੀਆਂ ਫਾਈਲਾਂ।

| ਫਾਈਲ | ਇਹ ਕੀ ਹੈ |
|---|---|
| `01_valid_receipt.json` | ਇੱਕ ਵੈਧ ਸਾਈਨ ਕੀਤਾ ਹੋਇਆ ਰਸੀਦ ਇੱਕ `lookup_flights` ਟੂਲ ਕਾਲ ਲਈ। ਪੁਸ਼ਟੀ ਕਰਨ 'ਤੇ ਸੱਚ ਵਾਪਸ ਮਿਲਦਾ ਹੈ। |
| `02_tampered_receipt.json` | ਉਸੇ ਰਸੀਦ ਵਿੱਚ ਇੱਕ ਖੇਤਰ ਸਾਈਨਿੰਗ ਤੋਂ ਬਾਅਦ ਬਦਲਿਆ ਗਿਆ। ਪੁਸ਼ਟੀ ਕਰਨ 'ਤੇ ਝੂਠ ਵਾਪਸ ਮਿਲਦਾ ਹੈ। |
| `03_chain_three_receipts.json` | ਤਿੰਨ ਵੈਧ ਰਸੀਦਾਂ ਦੀ ਇੱਕ ਲੜੀ (search, hold, book) ਜਿਸ ਵਿੱਚ `previous_receipt_hash` ਹਰ ਇੱਕ ਨੂੰ ਪਿਛਲੇ ਨਾਲ ਜੋੜਦਾ ਹੈ। |
| `04_resigned_receipt.json` | ਉਹੀ ਰਸੀਦ ਜਿਸ ਨੂੰ ਛੇੜਖਾਣ ਕੀਤੀ ਗਈ ਅਤੇ ਫਿਰ ਇੱਕ ਹਮਲਾਵਰ ਨੇ ਦੁਬਾਰਾ ਸਾਈਨ ਕੀਤਾ, ਜਿਸ ਵਿੱਚ ਹਮਲਾਵਰ ਦੀ ਆਪਣੀ ਪਬਲਿਕ ਕੀ ਸ਼ਾਮਿਲ ਹੈ। ਇਸਦੇ ਅੰਦਰ ਦੀ ਕੀ ਵਿਰੁੱਧ ਸਾਬਤ ਹੁੰਦੀ ਹੈ। ਜਾਰੀ ਕਰਨ ਵਾਲੇ ਦੀ ਕੀ ਵਿਰੁੱਧ ਫੇਲ੍ਹ ਹੁੰਦੀ ਹੈ। |

ਫਿਕਸਚਰ payload ਦੇ ਕੈਨੋਨਿਕਲ JCS ਬਾਇਟਸ ਨੂੰ ਸਿੱਧਾ Ed25519 ਨਾਲ ਸਾਈਨ ਕਰਦੇ ਹਨ। 
SHA-256 ਸਮੱਗਰੀ ਦੀ ਡਾਈਜੇਸਟ ਅਤੇ ਰਸੀਦ-ਚੇਨ ਲਿੰਕਾਂ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਸਾਈਨ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਵਾਧੂ ਪ੍ਰੀ-ਹੈਸ਼ ਵਜੋਂ ਨਹੀਂ। 


## ਉਦਾਹਰਣਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨਾ

`18-signed-receipts.ipynb` ਵਿੱਚ, ਪਹਿਲਾਂ Setup ਅਤੇ ਸੈਕਸ਼ਨ 1 ਤੋਂ 3 ਚਲਾਓ। 
ਸੈਕਸ਼ਨ 3 `verify_chain` ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ; ਸਿਰਫ ਸੈਕਸ਼ਨ 1 ਅਤੇ 2 ਕਾਫ਼ੀ ਨਹੀਂ ਹਨ। 
ਫਿਰ ਹੇਠਾਂ ਦਿੱਤਾ ਬਲਾਕ ਨਵੇਂ ਸੈੱਲ ਵਿੱਚ ਚਲਾਓ, ਜਿੱਥੇ ਨੋਟਬੁੱਕ ਦਾ ਵਰਕਿੰਗ ਡਾਇਰੈਕਟਰੀ
`18-securing-ai-agents/code_samples` ਤੇ ਸੈੱਟ ਕੀਤਾ ਗਿਆ ਹੋਵੇ। ਹੇਠਾਂ ਦਿੱਤੇ ਫਿਕਸਚਰ ਪਾਥ ਉਸ ਡਾਇਰੈਕਟਰੀ ਨਾਲ ਸਬੰਧਤ ਹਨ।


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

### ਜੂਪਿਟਰ ਬਿਨਾਂ ਉਦਾਹਰਨ ਦੀ ਜਾਂਚ ਕਰਨਾ

ਰਿਪੋਜ਼ਟਰੀ ਰੂਟ ਤੋਂ, ਲੈੱਸਨ ਦੇ ਨਿਰਭਰਤਾਵਾਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰੋ ਅਤੇ ਚਲਾਓ:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

ਇਹ ਟੈਸਟ ਨੋਟਬੁੱਕ ਦੇ ਪਾਇਥਨ ਉਦਾਹਰਨਾਂ ਅਤੇ ਸਹੀ README ਬਲਾਕ ਨੂੰ ਚਲਾਉਂਦੇ ਹਨ
ਉਪਰ। ਇਹ tamén ਜਾਂਚਦੇ ਹਨ ਕਿ ਟੈਮਪਰਿੰਗ ਅਤੇ ਅਣਪਿਨ ਕੀਜ਼ ਡਿਟੈਕਟਰਾਂ ਵੱਲੋਂ ਖਾਰਜ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ।
ਟੈਸਟ ਨੋਟਬੁੱਕ ਦੇ `%pip` ਸੈਟਅਪ ਸੈੱਲ ਨੂੰ ਛੱਡ ਦਿੰਦੇ ਹਨ ਕਿਉਂਕਿ ਨਿਰਭਰਤਾਵਾਂ ਵੱਖ-ਵੱਖ ਇੰਸਟਾਲ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ।
ਉਹ ਨੋਟਬੁੱਕ ਜਾਂ ਫਿਕਸਚਰ ਵਿੱਚ ਕੋਈ ਬਦਲਾਵ ਨਹੀਂ ਕਰਦੇ।

## ਇਹ ਕਿਵੇਂ ਬਣਾਏ ਗਏ

ਫਿਕਸਚਰਸ ਨੋਟਬੁੱਕ ਦੇ ਵਰਗੇ ਕੋਡ ਪਾਥ ਨੂੰ ਵਰਤਦੇ ਹਨ, ਇੱਕ ਸਥਿਰ ਸਾਈਨਿੰਗ ਕੀ ਨਾਲ
ਅਤੇ ਬਾਈਟ-ਪੁਨਰੁਤਪਾਦਕਤਾ ਲਈ ਸਥਿਰ ਸਮੇਂ ਦੇ ਟੈਮਪਸਟੈਂਪ ਨਾਲ। ਦੁਬਾਰਾ ਬਣਾਉਣ ਲਈ:

```bash
python3 generate_fixtures.py
```

(ਸਕ੍ਰਿਪਟ ਇਸ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ `generate_fixtures.py` 'ਤੇ ਹੈ।)

`../test_signed_receipts.py` ਇਹ ਸਾਰੀ ਚੀਜ਼ ਆਪਣੇ ਆਪ ਚੈੱਕ ਕਰਦਾ ਹੈ: ਇਹ
ਨੋਟਬੁੱਕ ਦਾ ਕੋਡ ਚਲਾਉਂਦਾ ਹੈ, ਨੋਟਬੁੱਕ ਦੇ ਨਾਲ ਇਹ ਚਾਰ ਫਿਕਸਚਰਸ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ
`verify_receipt` ਅਤੇ `verify_chain` ਨਾਲ, ਅਤੇ ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ ਕਿ ਫਿਕਸਚਰਸ ਨੂੰ ਦੁਬਾਰਾ ਬਣਾਉਣਾ
ਇਕਸਾਰ ਬਾਈਟ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। `code_samples` ਤੋਂ:

```bash
python -m unittest test_signed_receipts
```

## ਵਿਦਿਆਰਥੀ ਕੱਚੇ JSON ਦਾ ਜਾਇਜ਼ਾ ਲੈ ਕੇ ਕੀ ਸਿੱਖਦੇ ਹਨ

ਕੱਚੇ ਰਸੀਦ ਫਾਰਮੈਟ ਨੂੰ ਪੜ੍ਹਕੇ ਅੰਦਰੂਨੀ ਸਮਝ ਬਣਦੀ ਹੈ ਜੋ ਨੋਟਬੁੱਕ ਵਿੱਚ ਸੈੱਲ ਸੈੱਲ ਮਿਲਦੀ ਨਹੀਂ।
ਵਿਦਿਆਰਥੀ ਜੋ JSON ਨੂੰ ਝੱਲਦੇ ਹਨ ਉਹ ਅਕਸਰ ਧਿਆਨ ਦਿੰਦੇ ਹਨ:

1. ਸਾਈਨ ਇੱਕ ਅੰਧਕਾਰਮਈ base64url ਸਤਰ ਹੈ, ਪਰ ਹੋਰ ਹਰ ਖੇਤਰ ਸਪਸ਼ਟ ਪੜ੍ਹਯੋਗ JSON ਹੈ।
   ਸਾਈਨ ਸਮੱਗਰੀ ਨੂੰ ਇਨਕ੍ਰਿਪਟ ਨਹੀਂ ਕਰਦਾ; ਇਹ ਇਸਦਾ ਪ੍ਰਮਾਣ ਹੈ।
2. ਰਸੀਦ ਵਿੱਚ `public_key` ਸ਼ਾਮਿਲ ਹੈ, ਜੋ ਫਾਈਲ ਨੂੰ
   ਖੁਦ-ਮੁਹੱਈਆ ਬਣਾਉਂਦਾ ਹੈ ਪਰ ਇਹ ਉਹ ਨਹੀਂ ਜੋ ਆਡੀਟਰ ਵਿਰੁੱਧ ਜਾਂਚ ਕਰਦਾ ਹੈ। ਤੁਲਨਾ ਕਰੋ
   `02_tampered_receipt.json` ਨੂੰ `04_resigned_receipt.json` ਨਾਲ: ਦੋਹਾਂ ਹਨ
   ਦਸਤਖਤ ਕਰਨ ਤੋਂ ਬਾਅਦ ਬਦਲਿਆ ਗਿਆ, ਪਰ ਦੂਜਾ ਹਮਲਾਵਰ ਦੀ ਆਪਣੀ ਕੁੰਜੀ ਨਾਲ ਮੁੜ ਦਸਤਖਤ ਕੀਤਾ ਗਿਆ, 
   ਤਾਂ ਜੋ ਇਹ ਉਸ ਕੁੰਜੀ ਦੇ ਖਿਲਾਫ ਸਹੀ ਸਾਬਤ ਹੋ ਜਾਏ ਜੋ ਇਹ ਸਮੇਤਦਾ ਹੈ। ਸਮੇਤਿਆ ਕੁੰਜੀ 
   ਤੁਹਾਨੂੰ ਦੱਸਦੀ ਹੈ ਕਿ ਫਾਇਲ ਅੰਦਰੂਨੀ ਤੌਰ 'ਤੇ ਸੰਗਤਿਤ ਹੈ। ਸਿਰਫ਼ ਕਈਥੇ ਹੋਰ 
   ਪ੍ਰਾਪਤ ਕੀਤੀ ਕੁੰਜੀ ਹੀ ਤੁਸੀਂ ਦੱਸ ਸਕਦੇ ਹੋ ਕਿ ਇਸ ਨੂੰ ਕਿਸ ਨੇ ਜਾਰੀ ਕੀਤਾ ਸੀ।
3. ਕਿਸੇ ਵੀ ਫੀਲਡ ਦੇ ਬਾਹਰ ਇੱਕ ਇਕੱਲੇ ਅੱਖਰ ਨੂੰ ਬਦਲਣਾ `signature`, ਫਿਰ
   ਇਸ ਫਾਈਲ ਨੂੰ `02_tampered_receipt.json` ਨਾਲ ਮੁੜ-ਤੁਲਨਾ ਕਰਨਾ,
   ਬਾਈਟ-ਸਤਰ ਮਕੈਨੀਜ਼ਮ ਨੂੰ ਕਾਂਕਰੀਟ ਕਰਦਾ ਹੈ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->