# Зразки квитанцій (Fixtures)

Чотири заздалегідь створені файли квитанцій для огляду без запуску ноутбука.

| Файл | Що це таке |
|---|---|
| `01_valid_receipt.json` | Дійсна підписана квитанція для виклику інструменту `lookup_flights`. Перевірка повертає True. |
| `02_tampered_receipt.json` | Та сама квитанція з одним полем, зміненим після підписання. Перевірка повертає False. |
| `03_chain_three_receipts.json` | Ланцюжок із трьох дійсних квитанцій (пошук, утримання, бронювання) з `previous_receipt_hash`, що посилює кожну попередню. |
| `04_resigned_receipt.json` | Та сама квитанція, змінена, а потім повторно підписана зловмисником із вбудованим власним відкритим ключем зловмисника. Перевіряється за ключем, що в ній міститься. Не проходить перевірку за ключем видавця. |

Fixtures підписують байти canonical JCS навантаження безпосередньо за допомогою Ed25519.
SHA-256 залишається для дайджестів вмісту та посилань у ланцюжку квитанцій, а не як
додаткова передхеш-функція перед підписанням.

## Перевірка зразків

У `18-signed-receipts.ipynb` спочатку запустіть Setup та розділи 1 до 3.
Розділ 3 визначає `verify_chain`; лише розділи 1 та 2 недостатньо.
Потім запустіть наступний блок у новій клітинці, з робочою директорією ноутбука,
встановленою у `18-securing-ai-agents/code_samples`. Шляхи до fixture файлів нижче відносні
до цієї директорії.

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

### Перевірка прикладу без Jupyter

З кореня репозиторію встановіть залежності уроку і запустіть:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Ці тести виконують приклади Python у ноутбуці та точний блок README
вище. Вони також перевіряють, що маніпуляції та непіннені ключі відхиляються
перевіряльниками. Тести пропускають клітинку налаштування `%pip` ноутбука, бо залежності
встановлюються окремо. Вони не змінюють ноутбук або fixtures.

## Як їх було згенеровано

Fixtures використовують той самий кодовий шлях, що і ноутбук, із фіксованим ключем підпису
і фіксованими відмітками часу для відтворюваності байтів. Щоб згенерувати знову:

```bash
python3 generate_fixtures.py
```

(Скрипт знаходиться у `generate_fixtures.py` в цій папці.)

`../test_signed_receipts.py` автоматично перевіряє все це: він запускає
код ноутбука, перевіряє ці чотири fixtures за допомогою
`verify_receipt` і `verify_chain` ноутбука та підтверджує, що повторна генерація
fixtures дає ідентичні байти. З `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Чому студенти вчаться, аналізуючи необроблений JSON

Читання необробленого формату квитанції формує інтуїцію, якої іноді бракує у клітинках ноутбука.
Студенти, які швидко переглядають JSON, часто помічають:

1. Підпис — це непрозорий рядок base64url, але кожне інше поле — це звичайний
   читабельний JSON. Підпис не шифрує вміст; він підтверджує його.
2. `public_key` вбудовано в квитанцію, що робить файл
   автономним, але це не те, що перевіряє аудитор. Порівняйте
   `02_tampered_receipt.json` з `04_resigned_receipt.json`: обидва
   були змінені після підписання, але другий був повторно підписаний власним
   ключем зловмисника, тому він перевіряється за ключем, який міститься у файлі.
   Вбудований ключ показує, що файл внутрішньо узгоджений. Лише ключ,
   отриманий зовні, вказує, хто його видавець.
3. Зміна одного символу будь-якого поля поза `signature`, а потім
   повторне порівняння цього файлу з `02_tampered_receipt.json`
   конкретизує механізм на байтовому рівні.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->