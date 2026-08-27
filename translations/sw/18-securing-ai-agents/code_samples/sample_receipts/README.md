# Sampuli za Risiti

Faili tatu za risiti zilizotengenezwa awali kwa ukaguzi bila kuendesha daftari.

| Faili | Ni nini |
|---|---|
| `01_valid_receipt.json` | Risiti halali iliyo saini kwa wito wa zana ya `lookup_flights`. Uhakiki unarudisha Kweli. |
| `02_tampered_receipt.json` | Risiti ile ile iliyo na uwanja mmoja uliobadilishwa baada ya kusaini. Uhakiki unarudisha Kw falso. |
| `03_chain_three_receipts.json` | Mnyororo wa risiti tatu halali (tafuta, shikilia, toa kitabu) zenye `previous_receipt_hash` zinazowahangaisha kila moja kwa ile ya awali. |

Sampuli hizi zinaweka saini moja kwa moja kwa biti za JCS za mzigo wa data kwa kutumia Ed25519.
SHA-256 bado inatumika kwa vidokezo vya maudhui na viungo vya mnyororo wa risiti, si kama
maandalizi ya ziada ya kabla ya kusaini.

## Kuhakiki sampuli

Daftari linaeleza uhakiki katika sehemu nne. Ili kuhakiki sampuli hizi
moja kwa moja bila kupitia hadithi ya daftari:

```python
import json
from pathlib import Path

# Inadhani umekamilisha kuleta na kazi za msaada
# kutoka sehemu za 1 na 2 za 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Kweli

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Si kweli

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Jinsi hizi zilivyotengenezwa

Sampuli hutumia njia ile ile ya msimbo kama daftari, na ufunguo mmoja wa kusaini ulio thibitishwa
na nyakati zilizo thibitishwa kwa uundaji wa biti zinazoweza kurudiwa. Kutengeneza tena:

```bash
python3 generate_fixtures.py
```

(Skripti iko `generate_fixtures.py` katika saraka hii.)

## Wanajifunza nini kwa kukagua JSON ghafi

Kusoma muundo wa risiti ghafi hujenga ufahamu ambao seli katika daftari
hazitoi kila mara. Wanafunzi wanaosoma JSON kwa makini mara nyingi hugundua:

1. Saini ni mfuatano wa siri wa base64url, lakini kila uwanja mwingine ni JSON rahisi
   inayosomeka. Saini haiwafichui maudhui; inathibitisha tu.
2. `public_key` imejumuishwa ndani ya risiti. Mkaguzi hahitaji chochote kingine
   kuthibitisha (kulingana na kuamini kuwa ufunguo kweli unatoka kwa mtangazaji aliye tamka;
   angalia README ya somo juu ya miundombinu ya utambulisho).
3. Kubadilisha herufi moja ya uwanja wowote, kisha kulinganisha tena faili hii na
   `02_tampered_receipt.json`, hufanya utaratibu wa ngazi za biti kuwa dhahiri.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->