# Примерни файлове с касови бележки

Три предварително генерирани файла с касови бележки за преглед без изпълнение на тетрадката.

| Файл | Какво е |
|---|---|
| `01_valid_receipt.json` | Валидна подписана касова бележка за повикване на инструмент `lookup_flights`. Проверката връща True. |
| `02_tampered_receipt.json` | Същата касова бележка с едно променено поле след подписването. Проверката връща False. |
| `03_chain_three_receipts.json` | Верига от три валидни касови бележки (търсене, задържане, запазване) с `previous_receipt_hash`, свързващ всяка с предишната. |

Файловете подписват директно каноничните JCS байтове на натоварването с Ed25519.
SHA-256 остава в употреба за хешове на съдържанието и връзки в касовата верига, не като
допълнителен предподписен хеш.

## Проверка на примерите

В `18-signed-receipts.ipynb`, първо стартирайте Setup и секции 1 до 3.
Секция 3 дефинира `verify_chain`; само секции 1 и 2 не са достатъчни.
След това изпълнете следния блок в нова клетка, като работната директория на тетрадката
е зададена на `18-securing-ai-agents/code_samples`. Пътищата във файловете са относителни
спрямо тази директория.

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

### Проверка на примера без Jupyter

От корена на репозитория инсталирайте зависимостите и стартирайте:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Тези тестове изпълняват Python примерите от тетрадката и точно блока README
по-горе. Те също проверяват дали манипулациите и неприкрепените ключове са отхвърлени от
проверяващите. Тестовете пропускат настройващата клетка `%pip` на тетрадката, тъй като зависимостите
се инсталират отделно. Те не променят тетрадката или файловете.

## Как са генерирани тези файлове

Файловете използват същия кодов път като тетрадката, с фиксиран подписващ ключ
и фиксирани времеви печати за байтово възпроизводимост. За да ги регенерирате:

```bash
python3 generate_fixtures.py
```

(Сценарият е в `generate_fixtures.py` в тази директория.)

## Какво научават студентите, когато разглеждат суров JSON

Четенето на суровия формат на касовата бележка изгражда интуиция, която клетките в тетрадката
не винаги предоставят. Студентите, които разглеждат JSON, често забелязват:

1. Подписът е непрозрачен низ в base64url, но всички останали полета са обикновен
   четим JSON. Подписът не криптира съдържанието; той го удостоверява.
2. `public_key` е вграден в касовата бележка, което е достатъчно за проверка на
   самосъгласуваност, но не и доверие към издателя. Одиторът трябва да го сравни с ключ,
   прикрепен извън касовата бележка или резолвиран чрез доверен регистър.
3. Модифицирането на един символ в произволно поле и повторното сравнение на този файл с
   `02_tampered_receipt.json` прави механизма на байтово ниво конкретен.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->