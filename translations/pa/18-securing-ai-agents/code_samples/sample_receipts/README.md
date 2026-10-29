# ਨਮੂਨਾ ਰਸੀਦ ਫਿਕਸਚਰ

ਤਿੰਨ ਪੂਰਵ-ਤਿਆਰ ਕੀਤੀਆਂ ਰਸੀਦਾਂ ਦੀਆਂ ਫਾਇਲਾਂ ਬਿਨਾਂ ਨੋਟਬੁੱਕ ਚਲਾਏ ਜਾਂਚ ਲਈ।

| ਫਾਇਲ | ਕੀ ਹੈ |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` ਟੂਲ ਕਾਲ ਲਈ ਇੱਕ ਸਹੀ ਦਸਤਖਤ ਵਾਲੀ ਰਸੀਦ। ਵੈਰੀਫਿਕੇਸ਼ਨ ਸੱਚ (True) ਵਾਪਸ ਕਰਦਾ ਹੈ। |
| `02_tampered_receipt.json` | ਦਸਤਖਤ ਕਰਨ ਤੋਂ ਬਾਦ ਇੱਕ ਖੇਤਰ ਬਦਲਿਆ ਹੋਇਆ ਇਕੋ ਜਿਹੀ ਰਸੀਦ। ਵੈਰੀਫਿਕੇਸ਼ਨ ਝੂਠਾ (False) ਵਾਪਸ ਕਰਦਾ ਹੈ। |
| `03_chain_three_receipts.json` | ਤਿੰਨ ਸਹੀ ਰਸੀਦਾਂ ਦੀ ਇੱਕ ਲੜੀ (search, hold, book) ਜਿਸ ਵਿੱਚ ਹਰ ਇੱਕ `previous_receipt_hash` ਪਹਿਲੀ ਨਾਲ ਜੋੜਦੀ ਹੈ। |

ਫਿਕਸਚਰ payload ਦੇ ਕੈਨੋਨਿਕਲ JCS ਬਾਈਟਸ ਨੂੰ ਸਿੱਧਾ Ed25519 ਨਾਲ ਦਸਤਖਤ ਕਰਦੇ ਹਨ।
SHA-256 ਸਮੱਗਰੀ ਡਾਈਜੈਸਟ ਅਤੇ ਰਸੀਦ-ਲੜੀ ਲਿੰਕ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਸਾਈਨਿੰਗ ਤੋਂ ਪਹਿਲਾਂ ਕੋਈ ਵਾਧੂ ਪ੍ਰੀ-ਹੈਸ਼ ਨਹੀਂ।


## ਨਮੂਨਿਆਂ ਦੀ ਪੁਸ਼ਟੀ

ਨੋਟਬੁੱਕ ਚਾਰ ਭਾਗਾਂ ਵਿੱਚ ਵੈਰੀਫਿਕੇਸ਼ਨ ਦਿਖਾਉਂਦਾ ਹੈ। ਇਨ੍ਹਾਂ ਫਿਕਸਚਰਾਂ ਨੂੰ ਨੋਟਬੁੱਕ ਸੰਵਾਦ ਤੋਂ ਬਿਨਾਂ ਸਿੱਧਾ ਚੈੱਕ ਕਰਨ ਲਈ:


```python
import json
from pathlib import Path

# Assumes you have completed the imports and helper functions
# from sections 1 and 2 of 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # True

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # False

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## ਇਹ ਕਿਵੇਂ ਤਿਆਰ ਕੀਤੇ ਗਏ

ਫਿਕਸਚਰ ਨੋਟਬੁੱਕ ਦੇ ਸਮਾਨ ਕੋਡ ਰਾਹ ਦਾ ਉਪਯੋਗ ਕਰਦੇ ਹਨ, ਇੱਕ ਫਿਕਸ ਸਾਈਨਿੰਗ ਕੀ ਅਤੇ ਫਿਕਸ ਸਮੇਂ ਦੇ ਸਟੈਂਪ ਨਾਲ ਬਾਈਟ-ਪੁਨਰਤਿਆਰਥਤਾ ਲਈ। ਮੁੜ ਤਿਆਰ ਕਰਨ ਲਈ:


```bash
python3 generate_fixtures.py
```

(ਸਕ੍ਰਿਪਟ ਇਹ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ `generate_fixtures.py` 'ਤੇ ਹੈ।)

## ਵਿਦਿਆਰਥੀ ਕੱਚੇ JSON ਦੇ ਨਿਰੀਅਨ ਕਰਨ ਤੋਂ ਕੀ ਸਿੱਖਦੇ ਹਨ

ਕੱਚੇ ਰਸੀਦ ਫਾਰਮੈਟ ਨੂੰ ਪੜ੍ਹਨ ਨਾਲ ਉਹ ਸੂਝ ਬਣਦੀ ਹੈ ਜੋ ਨੋਟਬੁੱਕ ਵਿੱਚ ਹਮੇਸ਼ਾ ਨਹੀਂ ਮਿਲਦੀ। JSON ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਪੜ੍ਹਨ ਵਾਲੇ ਵਿਦਿਆਰਥੀ ਅਕਸਰ ਧਿਆਨ ਦੇਂਦੇ ਹਨ:


1. ਦਸਤਖਤ ਇਕ ਅਸਪਸ਼ਟ base64url ਸਤਰ ਹੈ, ਪਰ ਹਰ ਇਕ ਹੋਰ ਖੇਤਰ ਸਧਾਰਨ ਪੜ੍ਹਨ ਯੋਗ JSON ਹੈ।  
   ਦਸਤਖਤ ਸਮੱਗਰੀ ਨੂੰ ਇੰਕ੍ਰਿਪਟ ਨਹੀਂ ਕਰਦਾ; ਇਹ ਇਸ ਦੀ ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ।  
2. `public_key` ਰਸੀਦ ਵਿੱਚ ਸਾਮਿਲ ਹੈ। ਇੱਕ ਆਡੀਟਰ ਨੂੰ ਹੋਰ ਕੁਝ ਵੀ ਜਾਂਚਣ ਲਈ ਲੋੜ ਨਹੀਂ ਹੈ
   (ਜਦ ਤੱਕ ਇਹ ਮੰਨਿਆ ਜਾਵੇ ਕਿ ਕੁੰਜੀ ਵਾਸਤਵ ਵਿੱਚ ਦਾਅਵਾ ਕੀਤੇ ਜਾਰੀਕਰਤਾ ਦੀ ਹੈ;
   ਪਛਾਣ ਢਾਂਚੇ ਬਾਰੇ ਪਾਠ ਪਾਠੋ README ਵੇਖੋ)।
3. ਕਿਸੇ ਵੀ ਖੇਤਰ ਦੇ ਇੱਕ ਅੱਖਰ ਨੂੰ ਬਦਲਣ ਤੋਂ ਬਾਅਦ, ਇਸ ਫਾਇਲ ਨੂੰ ਦੁਬਾਰਾ `02_tampered_receipt.json` ਨਾਲ
   ਤੁਲਨਾ ਕਰਨਾ, ਬਾਈਟ-ਸਤਰ ਮਕੈਨਿਜ਼ਮ ਨੂੰ ਵਿਅਕਤ ਕਰਦਾ ਹੈ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->