# Примерни фикстури за касови бележки

Четири предварително генерирани файла с касови бележки за проверка без стартиране на тетрадката.

| Файл | Какво представлява |
|---|---|
| `01_valid_receipt.json` | Валидна подписана бележка за извикване на инструмент `lookup_flights`. Верификацията връща True. |
| `02_tampered_receipt.json` | Същата бележка с едно поле променено след подписване. Верификацията връща False. |
| `03_chain_three_receipts.json` | Верига от три валидни бележки (търсене, задържане, резервация) с `previous_receipt_hash`, свързващ всяка с предходната. |
| `04_resigned_receipt.json` | Същата бележка, манипулирана и след това преподписана от нападател, с вградения публичен ключ на нападателя. Верифицира се спрямо ключа вътре в нея. Не успява спрямо ключа на издателя. |

Фикстурите подписват директно каноничните JCS байтове на полезния товар с Ed25519.
SHA-256 остава в употреба за хеширане на съдържанието и връзките в веригата от касови бележки, не като
допълнителен предварителен хеш преди подписване.

## Верифициране на примерите

В `18-signed-receipts.ipynb` първо стартирайте Setup и секции 1 до 3.
Секция 3 дефинира `verify_chain`; само секции 1 и 2 не са достатъчни.
След това стартирайте следващия блок в нова клетка с работната директория на тетрадката
зададена на `18-securing-ai-agents/code_samples`. Пътищата до фикстурите по-долу са относителни
спрямо тази директория.

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

### Проверка на примера без Jupyter

От корена на хранилището инсталирайте зависимостите за урока и изпълнете:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Тези тестове изпълняват Python примерите от тетрадката и точно горния блок от README.
Те също проверяват дали манипулации и неприковани ключове се отхвърлят от
проверяващите. Тестовете пропускат клетката за настройка `%pip` на тетрадката, тъй като зависимостите
се инсталират поотделно. Те не променят тетрадката или фикстурите.

## Как са генерирани тези файлове

Фикстурите използват същия код като тетрадката, с фиксиран ключ за подписване
и фиксирани времена за бита-по-бит възпроизводимост. За регенериране:

```bash
python3 generate_fixtures.py
```

(Скриптът е в `generate_fixtures.py` в тази директория.)

`../test_signed_receipts.py` автоматично проверява всичко това: изпълнява
кода на тетрадката, верифицира тези четири фикстури със
`verify_receipt` и `verify_chain` от тетрадката и потвърждава, че регенерирането на
фикстурите дава идентични байтове. От `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Какво научават студентите от разглеждането на суровия JSON

Четенето на суровия формат на касовата бележка изгражда интуиция, която клетките в тетрадката
не винаги предлагат. Студентите, които преглеждат JSON-а, често забелязват:

1. Подписът е непрозрачен низ base64url, но всяко друго поле е обикновен
   четим JSON. Подписът не криптира съдържанието; той го потвърждава.
2. `public_key` е вграден в касовата бележка, което прави файла
   самостоятелен, но не е това, срещу което проверява одиторът. Сравнете
   `02_tampered_receipt.json` със `04_resigned_receipt.json`: и двата са
   променени след подписване, но вторият е преподписан с ключа на нападателя,
   така че верифицира според ключа, който носи. Вграденият ключ
   ви казва, че файлът е вътрешно последователен. Единствено ключ, получен
   от външен източник ви казва кой го е издал.
3. Модифицирането на един символ на каквото и да е поле извън `signature`, след това
   сравняването на този файл с `02_tampered_receipt.json`, прави
   байтово ниво на механизма осезаемо.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->