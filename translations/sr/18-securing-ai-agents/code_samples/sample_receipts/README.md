# Пример фајлова рачуна

Четири унапред генерисана фајла рачуна за преглед без покретања свеске.

| Фајл | Шта је то |
|---|---|
| `01_valid_receipt.json` | Важећи потписани рачун за позив алата `lookup_flights`. Верификација враћа True. |
| `02_tampered_receipt.json` | Исти рачун са једним изменљивим пољем након потписивања. Верификација враћа False. |
| `03_chain_three_receipts.json` | Ланац од три важећа рачуна (претрага, чување, резервација) где `previous_receipt_hash` повезује сваки са претходним. |
| `04_resigned_receipt.json` | Исти рачун је нарушен, а затим поново потписан од стране нападача, са уграђеним јавним кључем нападача. Верификује се према кључу унутар рачуна. Не успева према кључу издаваоца. |

Фајлови директно потписују канонске JCS бајтове оптерећења са Ed25519.
SHA-256 се и даље користи за садржајне дигесте и линкове у ланцу рачуна, али не као
додатна претходна хеш функција пре потписивања.

## Верификовање примера

У `18-signed-receipts.ipynb` прво покрените Setup и одељке 1 до 3.
Одељак 3 дефинише `verify_chain`; сами одељци 1 и 2 нису довољни.
Затим покрените следећи блок у новој ћелији, са радним директоријумом свеске
постављеним на `18-securing-ai-agents/code_samples`. Путеви до фајлова испод су релативни
у односу на тај директоријум.

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

### Проверa примера без Јупитера

Из корена репозиторијума, инсталирајте зависности лекције и покрените:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Ови тестови извршавају Python примере из свеске и тачан блок README горе.
Такође проверавају да су нарушавања и непиновани кључеви одбијени од стране
верификатора. Тестови прескачу `%pip` ћелију за подешавање из свеске јер се зависности
инсталирају посебно. Не мењају свеску или фајлове.

## Како су ово генерисани

Фајлови користе исти пут кода као свеска, са једним фиксним кључем за потписивање
и фиксним временским жиговима ради репродуцирања бајтова. За поновну генерисање:

```bash
python3 generate_fixtures.py
```

(Скрипта се налази у `generate_fixtures.py` овог директоријума.)

`../test_signed_receipts.py` аутоматски проверава све ово: извршава
код свеске, верификује ова четири фајла са свескиним
`verify_receipt` и `verify_chain`, и потврђује да поновна генерација
фајлова даје идентичне бајтове. Из `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Шта студенти уче из прегледа сировог JSON-а

Читање сировог формата рачуна гради интуицију коју ћелије у свесци
не дају увек. Студенти који само прегледају JSON често примете:

1. Потпис је непрозирни base64url низ, али свако друго поље је обичан
   читљив JSON. Потпис не шифрује садржај; он га потврђује.
2. `public_key` је уграђен у рачун, што чини фајл
   самоодрживим али није оно што ревизор верификује. Упоредите
   `02_tampered_receipt.json` са `04_resigned_receipt.json`: оба су била
   измењена након потписивања, али други је поново потписан својим
   кључем нападача, па се верификује према кључу који носи. Уграђени кључ
   показује да је фајл унутрашње конзистентан. Само кључ добијен
   са другог места говори ко га је издао.
3. Измена само једног карактера у пољу ван `signature`, а затим
   поређење овог фајла са `02_tampered_receipt.json`, чини
   механизам на нивоу бајтова конкретним.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->