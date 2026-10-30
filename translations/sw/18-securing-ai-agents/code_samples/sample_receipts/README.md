# Sampuli za Risiti

Faili tatu za risiti zilizotayarishwa mapema kwa ukaguzi bila kukimbia daftari la kumbukumbu.

| Faili | Inavyokuwa |
|---|---|
| `01_valid_receipt.json` | Risiti halali iliyoainishwa kwa wito wa zana ya `lookup_flights`. Uhakiki unarudisha Kweli. |
| `02_tampered_receipt.json` | Risiti ile ile yenye sehemu moja iliyobadilishwa baada ya kusainiwa. Uhakiki unarudisha Siyo kweli. |
| `03_chain_three_receipts.json` | Mnyororo wa risiti tatu halali (tafuta, shikilia, kitabu) na `previous_receipt_hash` kuunganisha kila moja na ile ya awali. |

Sampuli hizi husaini bayt za JCS za teremu moja kwa moja kwa Ed25519.
SHA-256 bado inatumika kwa diiji za maudhui na viungo vya mnyororo wa risiti, si kama
awali ya ziada kabla ya kusaini.

## Kuhakiki sampuli

Katika `18-signed-receipts.ipynb`, endesha Setup na Sehemu 1 hadi 3 kwanza.
Sehemu ya 3 hufafanua `verify_chain`; Sehemu za 1 na 2 peke yake hazitoshi.
Kisha endesha kipande kinachofuata katika seli mpya, na saraka ya kazi ya daftari
ikitengenezwa kuwa `18-securing-ai-agents/code_samples`. Njia za sampuli zilizo hapa chini ni kwa
kuhusiana na saraka hiyo.

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

### Kukagua mfano bila Jupyter

Kutoka mizizi ya hifadhidata, weka utegemezi wa somo na endesha:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Majaribio haya hufanya mifano ya Python ya daftari la kumbukumbu na kipande halisi cha README
hapo juu. Pia huangalia kama uliyumba na funguo zisizolipishwa zinakataliwa na
wahakiki. Majaribio yanapuuza seli ya usanidi ya `%pip` kwa sababu utegemezi
umewekwa kando. Hayabadilishi daftari au sampuli.

## Jinsi zilivyozalishwa

Sampuli hutumia njia ile ile ya msimbo kama daftari la kumbukumbu, na ufunguo mmoja wa sahihi wa kusaini
pamoja na nyakati za kurekebisha kwa kurudia tena bayt. Ili kuzalisha tena:

```bash
python3 generate_fixtures.py
```

(Skripti iko katika `generate_fixtures.py` katika saraka hii.)

## Kile wanafunzi wanachojifunza kwa kukagua JSON ghafi

Kusoma muundo wa risiti ghafi hujenga hisia ambazo seli katika daftari la kumbukumbu
hazizitoi kila wakati. Wanafunzi wanaosoma kwa haraka JSON mara nyingi hugundua:

1. Saini ni mfuatiliaji wa base64url wa kuficha, lakini kila sehemu nyingine ni JSON wazi
   inayosomeka. Saini haisimbui maudhui; inathibitisha.
2. `public_key` imejumuishwa katika risiti, ambayo inatosha kuangalia
   uthabiti wa ndani lakini si kuaminiwa kwa mtayarishaji. Mkaguzi lazima aitazame kwa ufunguo
   uliowekwa nje ya risiti au uliotatuliwa kupitia rejista ya kuaminika.
3. Kubadilisha herufi moja katika sehemu yoyote, kisha kuilinganisha tena faili hili
   na `02_tampered_receipt.json`, hufanya utaratibu wa ngazi ya bayt kuwa wazi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->