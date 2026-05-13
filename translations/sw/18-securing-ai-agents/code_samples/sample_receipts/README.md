# Sampuli za Risiti za Mfano

Faili tatu za risiti zilizotengenezwa awali kwa ajili ya ukaguzi bila kuendesha daftari.

| Faili | Ni nini |
|---|---|
| `01_valid_receipt.json` | Risiti halali iliyosainiwa kwa wito wa zana ya `lookup_flights`. Uhakiki unarudisha Kweli. |
| `02_tampered_receipt.json` | Risiti ile ile yenye uwanja mmoja uliobadilishwa baada ya kusainiwa. Uhakiki unarudisha Si kweli. |
| `03_chain_three_receipts.json` | Mnyororo wa risiti tatu halali (tafutiza, shika, fungua) zenye `previous_receipt_hash` kuziunganisha kwa kila moja hadi ile ya awali. |

## Kuhakiki Sampuli

Daftari linaelekeza kupitia uhakiki sehemu nne. Ili kuhakiki sampuli hizi moja kwa moja bila kupitia simulizi la daftari:

```python
import json
from pathlib import Path

# Inadhani umekamilisha imports na kazi za msaada
# kutoka sehemu 1 na 2 za 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Kweli

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Si kweli

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Jinsi hizi zilivyotengenezwa

Sampuli hizi hutumia njia ile ile ya msimbo kama daftari, kwa funguo moja la kusaini lililowekwa
na nyakati za kudumu kwa ajili ya kurudiwa kwa biti. Ili kutengeneza upya:

```bash
python3 generate_fixtures.py
```

(Skripti iko katika `generate_fixtures.py` katika saraka hii.)

## Kile wanafunzi wanachojifunza kwa kukagua JSON ghafi

Kusoma muundo wa risiti ghafi hujenga hisia ambazo seli katika daftari haitoi kila wakati. Wanafunzi wanaosoma haraka JSON mara nyingi hugundua:

1. Saini ni mfuatiliaji wa base64url usio wazi, lakini kila uwanja mwingine ni JSON rahisi kusomeka. Saini haihifadhi siri ya maudhui; inathibitisha tu.
2. `public_key` imejumuishwa ndani ya risiti. Mkaguzi hahitaji kitu kingine chochote
   kuthibitisha (kwa sharti la kuamini kuwa ufunguo huo kweli ni wa mtengenezaji aliyedaiwa; angalia README ya somo kuhusu miundombinu ya utambulisho).
3. Kubadilisha herufi moja tu ya uwanja wowote, kisha kulinganisha tena faili hii na
   `02_tampered_receipt.json`, hufanya utaratibu wa ngazi ya biti uonekane wazi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->