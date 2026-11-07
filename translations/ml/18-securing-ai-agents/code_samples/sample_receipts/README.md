# സാമ്പിൾ റസീറ്റ് ഫിക്സ്ചേഴ്സ്

നോഡ്ബുക്ക് പ്രവർത്തിപ്പിക്കാതെ പരിശോധനക്ക് നാല് മുമ്പ്_GEN_ ഫയലുകൾ.

| ഫയൽ | എന്താണ് ഇത് |
|---|---|
| `01_valid_receipt.json` | ഒരു `lookup_flights` ഉപകരണ വിളിക്കുവാനുള്ള സാധുവായ ഒപ്പിട്ട രസീത്. സ്ഥിരീകരണം True തിരികെയായി നൽകുന്നു. |
| `02_tampered_receipt.json` | ഒപ്പിട്ടതിന് ശേഷം ഒരു ഫീൽഡ് മാറ്റിയിട്ടുള്ള അതേ രസീതും. സ്ഥിരീകരണം False ആയി ഫലം നൽകുന്നു. |
| `03_chain_three_receipts.json` | മൂന്ന് സാധുവായ രസീതുകളുടെ ചെയിൻ (search, hold, book), ഓരോന്നും മുൻപത്തേത് ബന്ധിപ്പിക്കുന്ന `previous_receipt_hash` ഉപയോഗിച്ച്. |
| `04_resigned_receipt.json` | ഒരേ രസീത് ആക്രമകൻ ഭ്രഷ്ടു ചെയ്ത് പിന്നീട് അവന്റെ സ്വന്തം പൊതു കീ ഉൾപ്പെടുത്തി വീണ്ടും ഒപ്പിട്ടിരിക്കുന്നു. അതിലെ കീ ഉപയോഗിച്ച് പരിശോധിക്കുമ്പോൾ ശരിയാണെന്ന് കാണിക്കുന്നു. നൽകുന്നവന്റെ കീ ഉപയോഗിച്ച് പരിശോധിച്ചാൽ പരാജയപ്പെടുന്നു. |

ഫിക്സ്‌ചറുകൾ പെയ്ലോഡിന്റെ കാനോണിക്കൽ JCS ബൈറ്റുകൾ നേരിട്ട് Ed25519 ഉപയോഗിച്ച് ഒപ്പുവെക്കുന്നു.
SHA-256 ഉള്ളടക്ക ഡൈജെസ്റ്റ്‌സിനും രസീത്-ചെയിൻ ലിങ്കുകൾക്കും ഉപയോഗത്തിൽ തുടരുന്നു, ഒപ്പുവെക്കുന്നതിന് മുമ്പുള്ള അധിക പ്രീ-ഹാഷ് ആയി അല്ല.


## സാമ്പിളുകൾ സ്ഥിരീകരിക്കൽ

`18-signed-receipts.ipynb` ൽ, ആദ്യം Setup ಮತ್ತು Section 1 മുതൽ 3 വരെ പ്രവർത്തിക്കുക.
Section 3 ൽ `verify_chain` നിർവചിക്കുന്നു; Section 1 ಮತ್ತು 2 മാത്രം کافی அல்ல.
തുടർന്ന്, പുതിയ സെല്ലിൽ താഴെ കാണുന്ന ബ്ലോക്ക് പ്രവർത്തിക്കുക, നോട്ട്‌ബുക്ക് പ്രവർത്തിക്കുന്ന ഡയറക്ടറി
`18-securing-ai-agents/code_samples` ആയി സജ്ജമാക്കിയിട്ടുണ്ട്. താഴെ കാണുന്ന ഫിക്സ്ചർ പാതകൾ ആ ഡയറക്ടറിയോട്
ബന്ധപ്പെട്ടു കാണിക്കുന്നു.

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

### ജ്യൂപ്പിറ്റർ ഇല്ലാതെ ഉദാഹരണം പരിശോധിക്കൽ

റിപ്പോസിറ്ററിയുടെ റൂട്ട്ിരുന്ന്, പാഠപുസ്തകത്തിലെ ആശ്രിതങ്ങൾ ഇൻസ്റ്റാൾ ചെയ്ത് التشغيل কৰক:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

ഈ പരിശോധനകൾ നോട്ട്‌ബുക്കിലെ Python ഉദാഹരണങ്ങളും മുകൾവശത്ത് കൊടുത്തിരിക്കുന്ന README ബ്ലോക്കും പ്രവർത്തിപ്പിക്കുന്നു.
അവ, തട്ടിപ്പ് നടത്തിയതും അണഞ്ഞ കീകളും വേരിഫയറുകൾ നിരസിക്കുന്നുണ്ടോ എന്ന് പരിശോധിക്കും.
പരിശോധനകൾ നോട്ട്‌ബുക്കിന്റെ `%pip` സജ്ജീകരണ സെല് മറികടക്കുന്നു, കാരണം ആശ്രിതങ്ങൾ
വേർതിരിച്ച് ഇൻസ്റ്റാൾ ചെയ്തു. അവ നോട്ട്‌ബുക്ക് അല്ലെങ്കിൽ ഫിക്ഷറുകൾ മാറ്റാറില്ല.

## ഇവ എങ്ങനെ സൃഷ്ടിക്കപ്പെട്ടുവെന്ന്

ഫിക്ഷറുകൾ നോട്ട് ബുക്കിനൊപ്പം ഒരേ കോഡ് പാത ഉപയോഗിക്കുന്നു, ഒറ്റ നിശ്ചിത സൈൻ ചെയ്‌വാനുള്ള കീ
കൂടാതെ ബൈറ്റു-പുനഃസംസ്‌ക്കരണത്തിന് നിശ്ചിത ടൈംസ്റ്റാമ്പുകൾ ഉണ്ട്. പുനഃസൃഷ്ടിക്കാൻ:

```bash
python3 generate_fixtures.py
```

(സ്ക്രിപ്റ്റ് ഈ ഡയറക്ടറിയിലെ `generate_fixtures.py` ആയിടത്താണ്.)

`../test_signed_receipts.py` എല്ലാം സ്വയം പരിശോധിക്കുന്നു: ഇത്
നോട്ട്‌ബുക്ക് കോഡ് പ്രവർത്തിപ്പിക്കുന്നു, നോട്ട്‌ബുക്കിന്റെ ഈ നാല് ഫിക്ഷറുകൾ
`verify_receipt` ഉം `verify_chain` ഉം ഉപയോഗിച്ച് സ്ഥിരീകരിക്കുന്നു, കൂടാതെ
ഫിക്ഷറുകൾ പുനഃസൃഷ്ടിക്കുന്നത് സമാനമായ ബൈറ്റുകൾ നൽകുന്നു എന്ന് പൂർണ്ണമായും സ്ഥിരീകരിക്കുന്നു. `code_samples` മുതലാണ്:

```bash
python -m unittest test_signed_receipts
```

## രോ/raw JSON പരിശോധിച്ച് വിദ്യാര്‍ത്ഥികൾ എന്താണ് കല്‍പ്പിക്കുന്നത്

രോ/raw റസീറ്റ് ഫോർമാറ്റ് വായിക്കുന്നത് നോട്ട്ബുക്കിലെ സെല്ലുകൾ എല്ലായ്പ്പോഴും നൽകുന്നില്ലാത്ത
ബോധത്തെ പടുത്തുയർത്തുന്നു. JSON നെ സ്കിം ചെയ്തു നോക്കുന്ന വിദ്യാര്‍ത്ഥികൾ

1. ഒപ്പ് ഒരു ഗൂഢമായ base64url സ്ട്രിംഗ് ആണ്, പക്ഷേ മറ്റു എല്ലാ ഫീൽഡുകളും എല്ലാം
   വായിക്കാവുന്ന JSON ആണ്. ഒപ്പ് ഉള്ളടക്കം എൻക്രിപ്റ്റ് ചെയ്യാറില്ല; അത് അതിന് സാക്ഷ്യം നൽകുന്നു.
2. ഫയലിൽ ഫയലിൽ `public_key` ഉൾപ്പെടുത്തിയിരിക്കുന്നുണ്ടു, ഇത് ഫയൽ
   സ്വയം സമ്പൂർണ്ണമാണ്, എന്നാൽ ഓഡിറ്റർ പരിശോധിക്കുന്നത് ഇതല്ല. താരതമ്യം ചെയ്യുക
   `02_tampered_receipt.json` നും `04_resigned_receipt.json` നും: ഇരண்டும்
   ഒപ്പിട്ടതിനുശേഷം മാറ്റം വന്നതാണ്, പക്ഷേ രണ്ടാംത് ആക്രമകന്റെ
   സ്വസ്വ കീ ഉപയോഗിച്ച് വീണ്ടും ഒപ്പിട്ടതിനാൽ, ഇത് ഈ കീ ഉപയോഗിച്ച് സാധൂകരിക്കുന്നു. ഔട്ടേഷൻ ചെയ്ത കീ
   ഫയൽ ഉൾകാഴ്ചയിൽ ചിട്ടപ്രദമാണ് എന്ന് കാണിക്കുന്നു. വെറും മറ്റിടത്തുനിന്ന് ലഭിക്കുന്ന ഒരു കീ മാത്രം
   അത് ആർ പുറത്തിറക്കിയെന്ന് കാണിക്കുന്നു.
3. `signature` ന് പുറത്തുള്ള ഏതെങ്കിലും ഫീൽഡിലെ ഒരു അക്ഷരം മാറ്റി, 
   പിന്നീടാണ് ഈ ഫയൽ `02_tampered_receipt.json` ilə വീണ്ടും താരതമ്യം ചെയ്യുന്നത്, ഇത് 
   ബൈറ്റ് നിലയിലുള്ള മെക്കാനിസം സുസൂക്ഷ്മമാക്കുന്നു.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->