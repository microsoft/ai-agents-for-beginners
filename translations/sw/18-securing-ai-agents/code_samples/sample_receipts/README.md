# Sampuli za Risiti

Faili tatu za risiti zilizotengenezwa awali kwa ukaguzi bila kuendesha daftari.

| Faili | Kitu kilicho ndani |
|---|---|
| `01_valid_receipt.json` | Risiti halali yenye saini kwa wito wa zana ya `lookup_flights`. Uhakiki unarudisha True. |
| `02_tampered_receipt.json` | Risiti ile ile iliyo na urekebishaji moja baada ya kusainiwa. Uhakiki unarudisha False. |
| `03_chain_three_receipts.json` | Mnyororo wa risiti tatu halali (tafuta, hifadhi, kitabu) yenye `previous_receipt_hash` inayounganisha kila moja kwenye ile ya awali. |

Sampuli hizi husaini moja kwa moja bait ya JCS ya mzigo kwa kutumia Ed25519.
SHA-256 bado inatumika kwa mfumuko wa maudhui na viungo vya mnyororo wa risiti, si kama
pre-hash ya ziada kabla ya kusaini.

## Kukagua sampuli

Daftari huenda hatua kwa hatua kupitia ukaguzi katika sehemu nne. Ili kuthibitisha sampuli hizi
moja kwa moja bila kuandika hadithi ya daftari:

```python
import json
from pathlib import Path

# Inadhani umeamaliza kuingiza na kazi za msaada
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

Sampuli hizi hutumia njia ile ile ya msimbo kama daftari, na funguo moja ya kusaini iliyowekwa
na muda ulio thibitishwa kwa ajili ya urekebishaji wa bait. Ili kuzalisha tena:

```bash
python3 generate_fixtures.py
```

(Skripti iko `generate_fixtures.py` katika saraka hii.)

## Kile wanafunzi hujifunza kwa kukagua JSON ghafi

Kusoma muundo wa risiti ghafi hujenga hisia isiyopatikana kila wakati katika seli za daftari.
Wanafunzi wanaochambua JSON mara nyingi hugundua:

1. Saini ni kamba ya base64url isiyoonekana, lakini kila shamba lingine ni JSON ya kusomeka wazi.
   Saini haisimbui maudhui; inathibitisha tu.
2. `public_key` imejumuishwa kwenye risiti. Mkaguzi hahitaji chochote zaidi
   kuthibitisha (kwa kuzingatia kuamini kwamba funguo kweli ni mali ya
   mtumaji aliyejitaja; angalia README ya somo juu ya miundombinu ya utambulisho).
3. Kubadilisha herufi moja kati ya shamba lolote, kisha kulinganisha tena faili hii na
   `02_tampered_receipt.json`, huweka wazi utaratibu wa ngazi ya bait.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->