# Sampuli za Tiketi

Faili nne za tiketi zilizotengenezwa awali kwa ajili ya ukaguzi bila kuendesha daftari ya kumbukumbu.

| Faili | Ni Nini |
|---|---|
| `01_valid_receipt.json` | Tiketi halali iliyosainiwa kwa wito wa zana ya `lookup_flights`. Uhakiki unarudisha Kweli. |
| `02_tampered_receipt.json` | Tiketi ile ile yenye mabadiliko moja kwenye fani baada ya kusaini. Uhakiki unarudisha Sio Kweli. |
| `03_chain_three_receipts.json` | Mnyororo wa tiketi tatu halali (tafuta, shikilia, kitaabu) zenye `previous_receipt_hash` zinazoziunganisha kwa ile ya awali. |
| `04_resigned_receipt.json` | Tiketi ile ile iliyoharibika kisha kusainiwa tena na mwovu, akiwa na ufunguo wa umma wa mwovu huyo aliowekwa ndani. Inathibitishwa dhidi ya ufunguo uliomo ndani yake. Inashindwa dhidi ya ufunguo wa mtengeneza tiketi. |

Sampuli husaini moja kwa moja baiti za JCS za mzigo wa data kwa kutumia Ed25519.
SHA-256 bado inatumika kwa michakato ya maudhui na viungo vya mnyororo wa tiketi, si kama
pre-hash ya ziada kabla ya kusaini.

## Kuhakikisha sampuli

Katika `18-signed-receipts.ipynb`, endesha Setup na Sehemu 1 hadi 3 kwanza.
Sehemu ya 3 hufafanua `verify_chain`; Sehemu 1 na 2 pekee hazitoshi.
Kisha endesha kipande kinachofuata katika seli mpya, na saraka ya kazi ya daftari
iwe imesetwa kwa `18-securing-ai-agents/code_samples`. Njia za sampuli ziko
katika saraka hiyo.

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

### Kukagua mfano bila Jupyter

Kutoka kwenye mzizi wa hifadhidata, install utegemezi wa somo na endesha:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Vipimo hivi hufanya mfano wa Python kwenye daftari na kipande cha README
kilichotajwa hapo juu. Pia hubaini kuwa maneno yaliyoharibiwa na funguo zisizofungamanishwa hukubaliwa na
wachunguzi. Vipimo hukosa seli ya setup ya daftari ya `%pip` kwa sababu utegemezi
huwekwa kando. Havibadilishi daftari wala sampuli.

## Jinsi hizi zilivyosababishwa

Sampuli hutumia njia hiyo hiyo ya msimbo wa daftari, kwa kutumia ufunguo wa kudumu wa kusaini
na muda wa kudumu kwa urekebishaji kinasauri. Ili kuizalisha tena:

```bash
python3 generate_fixtures.py
```

(Skripti iko kwenye `generate_fixtures.py` katika saraka hii.)

`../test_signed_receipts.py` huchunguza yote haya moja kwa moja: inaendesha
msimbo wa daftari, huhakiki sampuli hizi nne kwa kutumia daftari
ya `verify_receipt` na `verify_chain`, na kuthibitisha kuwa kuzalisha tena
sampuli hutoa baiti sawa. Kutoka kwa `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Kile wanafunzi wanachojifunza kwa kuchunguza JSON ghafi

Kusoma muundo wa tiketi ghafi huunda ufahamu ambao seli za daftari
mara nyingi hazizitoi. Wanafunzi wanaokagua JSON mara nyingi hugundua:

1. Sahihi ni mfuatano usio wazi wa base64url, lakini kila fani nyingine ni wazi
   JSON inayosomika. Saini haitafsiri yaliyomo; inathibitisha tu.
2. `public_key` imejumuishwa katika risiti, ambayo huifanya faili
   kuwa huru lakini si hiyo ambayo mkaguzi anathibitisha dhidi yake. Linganisha
   `02_tampered_receipt.json` na `04_resigned_receipt.json`: zote mbili ziliharibishwa baada ya kusainiwa,
   lakini ya pili ilisainiwa tena kwa ufunguo wa mwadaji,
   hivyo inathibitishwa dhidi ya ufunguo unaobeba. Ufunguo uliomo ndani
   unakuambia faili hilo lina muafaka wa ndani. Funguo inayopatikana
   mahali pengine tu ndiyo inakuambia nani alilitolea.
3. Kubadilisha herufi moja ya shamba lolote nje ya `signature`, kisha
   kulinganisha tena faili hili na `02_tampered_receipt.json`, kunafanya
   mbinu ya kiwango cha byte kuwa halisi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->