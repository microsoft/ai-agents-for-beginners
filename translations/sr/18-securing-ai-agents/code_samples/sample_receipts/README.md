# Примери пријема

Три претходно генерисана фајла пријема за преглед без покретања свеске.

| Фајл | Шта је то |
|---|---|
| `01_valid_receipt.json` | Важећи потписани пријем за `lookup_flights` позив алата. Верификација враћа True. |
| `02_tampered_receipt.json` | Исти пријем са једним измењеним пољем након потписивања. Верификација враћа False. |
| `03_chain_three_receipts.json` | Ланац од три важећа пријема (претрага, задржавање, резервација) са `previous_receipt_hash` који сваки повезује са претходним. |

Примери потписују канонске JCS бајтове корисног оптерећења директно са Ed25519.
SHA-256 остаје у употреби за дигесте садржаја и везе ланца пријема, не као
додатни пре-хаш пре потписивања.

## Верификација примера

У `18-signed-receipts.ipynb` прво покрените Подешавање и Одељке 1 до 3.
Одељак 3 дефинише `verify_chain`; сами Одељци 1 и 2 нису довољни.
Затим покрените следећи блок у новој ћелији, са радним директоријумом свеске
подешеним на `18-securing-ai-agents/code_samples`. Путање примера испод су релативне
према том директоријуму.

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

### Провера примера без Јупитера

Из корена репозиторијума инсталирајте зависности лекције и покрените:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Ови тестови извршавају Питхон примере из свеске и тачан блок из README
изнад. Такође проверавају да ли верификатори одбијају манипулације и неповезане кључеве.
Тестови прескачу ћелију за подешавање `%pip` јер се зависности
инсталирају посебно. Не мењају свеску нити примерке.

## Како су ови генерисани

Примери користе исти код као и свеска, са једним фиксним кључем за потписивање
и фиксним временским ознакама за репродукцију бајтова. Да бисте регенерисали:

```bash
python3 generate_fixtures.py
```

(Скрипта се налази у `generate_fixtures.py` у овом директоријуму.)

## Шта студенти уче из прегледа сировог JSON-а

Читање сировог формата пријема развија интуицију коју ћелије у свесци
не пружају увек. Студенти који брзо прелиставају JSON често примете:

1. Потпис је нејасан base64url стринг, али свако друго поље је уобичајени
   читљиви JSON. Потпис не шифрује садржај; он га потврђује.
2. `public_key` је уграђен у пријем, што је довољно за проверу
   само-конзистентности али не и поверења у издавача. Ревизор мора упоредити са кључем
   који је закључан изван пријема или решен кроз поуздан регистар.
3. Измена једног карактера у било ком пољу, па поновна упоредба овог фајла са
   `02_tampered_receipt.json` конкретизује механизам на нивоу бајта.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->