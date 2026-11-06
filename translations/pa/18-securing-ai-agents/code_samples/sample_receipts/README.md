# ਨਮੂਨਾ ਰਸੀਦ ਫਿਕਸਚਰ

ਨੋਟਬੁੱਕ ਚਲਾਏ ਬਿਨਾਂ ਜਾਂਚ ਲਈ ਤਿੰਨ ਪਹਿਲਾਂ ਤੋਂ ਤਿਆਰ ਕੀਤੀਆਂ ਰਸੀਦ ਫਾਈਲਾਂ।

| ਫਾਈਲ | ਇਹ ਕੀ ਹੈ |
|---|---|
| `01_valid_receipt.json` | ਇੱਕ ਵੈਧ ਸਾਈਨ ਕੀਤਾ ਹੋਇਆ ਰਸੀਦ ਇੱਕ `lookup_flights` ਟੂਲ ਕਾਲ ਲਈ। ਜਾਂਚ ਸੱਚਾ ਵਾਪਸ ਕਰਦੀ ਹੈ। |
| `02_tampered_receipt.json` | ਸਾਈਨਿੰਗ ਦੇ ਬਾਅਦ ਇੱਕ ਫੀਲਡ ਸੋਧਿਆ ਹੋਇਆ ਉਹੀ ਰਸੀਦ। ਸੱਤੀਕਰਨ False ਵਾਪਸ ਕਰਦਾ ਹੈ। |
| `03_chain_three_receipts.json` | ਤਿੰਨ ਵੈਧ ਰਸੀਦਾਂ (ਖੋਜ, ਰੋਕਣਾ, ਬੁੱਕ ਕਰਨਾ) ਦੀ ਲੜੀ ਜਿੱਥੇ ਹਰ ਇੱਕ ਨੂੰ ਪਿਛਲੇ ਨਾਲ ਜੋੜਨ ਲਈ `previous_receipt_hash` ਬੰਨ੍ਹੀ ਹੁੰਦੀ ਹੈ। |

ਫਿਕਸਚਰ ਸਿੱਧਾ ਹੀ ਪੇਲੋਡ ਦੇ ਕੈਨੋਨਿਕਲ JCS ਬਾਈਟਸ ਨੂੰ Ed25519 ਨਾਲ ਸਾਇਨ ਕਰਦੇ ਹਨ।
SHA-256 ਸਮੱਗਰੀ ਡਾਈਜੈਸਟਸ ਅਤੇ ਰਸੀਦ-ਚੇਨ ਲਿੰਕਸ ਲਈ ਇਸਤਮਾਲ ਹੁੰਦਾ ਰਹਿੰਦਾ ਹੈ, ਸਾਈਨ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਕਿਸੇ ਵਾਧੂ ਪ੍ਰੀ-ਹੈਸ਼ ਵਜੋਂ ਨਹੀਂ।


## ਨਮੂਨਿਆਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨਾ

`18-signed-receipts.ipynb` ਵਿੱਚ, ਸਭ ਤੋਂ ਪਹਿਲਾਂ Setup ਅਤੇ ਭਾਗ 1 ਤੋਂ 3 ਤੱਕ ਚਲਾਓ।
ਭਾਗ 3 `verify_chain` ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ; ਸਿਰਫ ਭਾਗ 1 ਅਤੇ 2 ਕਾਫ਼ੀ ਨਹੀਂ ਹਨ।
ਫਿਰ ਹੇਠਾਂ ਦਿੱਤਾ ਹੋਇਆ ਬਲਾਕ ਨਵੀਂ ਸੈੱਲ ਵਿੱਚ ਚਲਾਓ, ਨੋਟਬੁੱਕ ਦੇ ਕਾਮ ਕਰਨ ਵਾਲੇ ਡਾਇਰੈਕਟਰੀ ਨੂੰ
`18-securing-ai-agents/code_samples` 'ਤੇ ਸੈੱਟ ਕੀਤਾ ਹੋਇਆ। ਹੇਠਾਂ ਦਿੱਤੀ ਗਈ ਫਿਕਸਚਰ ਪਾਥ ਉਸ ਡਾਇਰੈਕਟਰੀ ਨਾਲ ਸੰਬੰਧਤ ਹਨ।


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

### ਜੁਪਾਈਟਰ ਦੇ ਬਿਨਾਂ ਉਦਾਹਰਨ ਦੀ ਜਾਂਚ ਕਰਨਾ

ਰਿਪੋਜ਼ਿਟਰੀ ਰੂਟ ਤੋਂ, ਲੈਸ਼ਨ ਦੀਆਂ ਲੋੜਾਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰੋ ਅਤੇ ਚਲਾਓ:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

ਇਹ ਟੈਸਟ ਨੋਟਬੁੱਕ ਦੇ ਪਾਇਥਨ ਉਦਾਹਰਨਾਂ ਅਤੇ ਬਿਲਕੁਲ README ਬਲਾਕ ਨੂੰ ਚਲਾਉਂਦੇ ਹਨ
ਉੱਪਰ। ਉਹ ਇਹ ਵੀ ਜਾਂਚਦੇ ਹਨ ਕਿ ਟੈਂਪਰਿੰਗ ਅਤੇ ਅਣਪਿਨ ਕੀਜ਼ ਨੂੰ ਪਰਖ ਨਕਾਰ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ
ਦੁਆਰਾ। ਟੈਸਟ ਨੋਟਬੁੱਕ ਦੇ `%pip` ਸੈੱਟਅੱਪ ਸੈੱਲ ਨੂੰ ਛੱਡ ਦਿੰਦੇ ਹਨ ਕਿਉਂਕਿ ਡਿਪੈਂਡੈਂਸੀਜ਼
ਵੱਖ-ਵੱਖ ਤਰੀਕੇ ਨਾਲ ਇੰਸਟਾਲ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ। ਉਹ ਨੋਟਬੁੱਕ ਜਾਂ ਫਿਕਸਚਰਜ਼ ਵਿੱਚ ਕੋਈ ਤਬਦੀਲੀ ਨਹੀਂ ਕਰਦੇ।

## ਇਹ ਕਿਵੇਂ ਤਿਆਰ ਕੀਤੇ ਗਏ

ਫਿਕਸਚਰਜ਼ ਨੋਟਬੁੱਕ ਦੇ ਸਮਾਨ ਕੋਡ ਪਾਥ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ, ਇੱਕ ਫਿਕਸ ਕੀਤੀ ਹੋਈ ਸਾਈਨਿੰਗ ਕੀ
ਅਤੇ ਬਾਈਟ-ਪੁਨਰੁਤਪਾਦਨ ਲਈ ਫਿਕਸ ਕੀਤੀ ਗਈ ਟਾਈਮਸਟੈਂਪ ਨਾਲ। ਦੁਬਾਰਾ ਬਣਾਉਣ ਲਈ:

```bash
python3 generate_fixtures.py
```

(ਸਕ੍ਰਿਪਟ ਇਸ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ `generate_fixtures.py` 'ਤੇ ਹੈ।)

## ਵਿਦਿਆਰਥੀ ਕੱਚੇ JSON ਨੂੰ ਦੇਖ ਕੇ ਕੀ ਸਿੱਖਦੇ ਹਨ

ਕੱਚੇ ਰਸੀਦ ਫਾਰਮੈਟ ਨੂੰ ਪੜ੍ਹਨ ਨਾਲ ਉਹ ਅਹਿਸਾਸ ਬਣਦਾ ਹੈ ਜੋ ਨੋਟਬੁੱਕ ਦੀਆਂ ਸੈੱਲਜ਼ ਹਮੇਸ਼ਾ ਨਹੀਂ ਦਿੰਦੀਆਂ।
ਜੋ ਵਿਦਿਆਰਥੀ JSON ਨੂੰ ਜਲਦੀ ਵਿੱਚ ਵੇਖਦੇ ਹਨ ਉਹ ਅਕਸਰ ਨੋਟਿਸ ਕਰਦੇ ਹਨ:

1. ਦਸਤਖ਼ਤ ਇੱਕ ਅੰਧੇਰਾ base64url ਸਟਰਿੰਗ ਹੈ, ਪਰ ਹਰ ਹੋਰ ਖੇਤਰ ਸਿੱਧਾ ਹੈ
   ਪੜ੍ਹਨ ਯੋਗ JSON। ਸਿਗਨੇਚਰ ਸਮੱਗਰੀ ਨੂੰ ਇਨਕ੍ਰਿਪਟ ਨਹੀਂ ਕਰਦਾ; ਇਹ ਉਸ ਦੀ ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ।
2. `public_key` ਰਸੀਦ ਵਿੱਚ ਐਂਬੈੱਡ ਕੀਤਾ ਗਿਆ ਹੈ, ਜੋ ਸਵੈ-ਸੰਘਤਾ ਜਾਂਚ ਲਈ ਕਾਫੀ ਹੈ
   ਪਰ ਜਾਰੀ ਕਰਨ ਵਾਲੇ ਦੇ ਭਰੋਸੇ ਲਈ ਨਹੀਂ। ਇੱਕ ਆਡੀਟਰ ਨੂੰ ਇਹ ਇੱਕ ਕੁੰਜੀ ਨਾਲ ਤੁਲਨਾ ਕਰਨੀ ਪੈਂਦੀ ਹੈ
   ਜੋ ਰਸੀਦ ਦੇ ਬਾਹਰ ਪਿਨ ਕੀਤੀ ਹੋਈ ਹੈ ਜਾਂ ਇੱਕ ਭਰੋਸੇਮੰਦ ਰਜਿਸਟਰੀ ਰਾਹੀਂ ਹੱਲ ਕੀਤੀ ਗਈ ਹੈ।
3. ਕਿਸੇ ਵੀ ਖੇਤਰ ਦੇ ਇੱਕ ਅੱਖਰ ਨੂੰ ਸੋਧ ਕੇ, ਫਿਰ ਇਸ ਫਾਇਲ ਨੂੰ ਮੁੜ-ਤੁਲਨਾ ਕਰ ਕੇ
   `02_tampered_receipt.json` ਨਾਲ, ਬਾਈਟ-ਸਤਰ ਮਕੈਨਿਜ਼ਮ ਨੂੰ ਠوس ਬਣਾਉਂਦਾ ਹੈ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->