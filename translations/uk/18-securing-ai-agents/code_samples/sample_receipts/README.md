# Зразки файлів квитанцій

Три наперед створені файли квитанцій для перегляду без запуску блокнота.

| Файл | Що це таке |
|---|---|
| `01_valid_receipt.json` | Дійсна підписана квитанція для виклику інструменту `lookup_flights`. Перевірка повертає True. |
| `02_tampered_receipt.json` | Та сама квитанція з одним зміненим полем після підписання. Перевірка повертає False. |
| `03_chain_three_receipts.json` | Ланцюг із трьох дійсних квитанцій (search, hold, book) з `previous_receipt_hash`, що пов’язує кожну з попередньою. |

Зразки безпосередньо підписують канонічні байти JCS навантаження за допомогою Ed25519.
SHA-256 залишається в використанні для дайджестів вмісту та посилань у ланцюгу квитанцій, а не як
додатковий попередній хеш перед підписанням.

## Перевірка зразків

У `18-signed-receipts.ipynb` спочатку виконайте Setup і Розділи 1–3.
Розділ 3 визначає `verify_chain`; лише Розділи 1 і 2 недостатні.
Потім виконайте наступний блок у новій клітинці, встановивши робочу директорію блокнота
у `18-securing-ai-agents/code_samples`. Шляхи до зразків нижче відносні
до цієї директорії.

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

### Перевірка прикладу без Jupyter

З кореневої директорії репозиторію встановіть залежності уроку й запустіть:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Ці тести виконують приклади Python із блокнота та точний блок README
вище. Вони також перевіряють, що фальсифікація та неприкріплені ключі відхиляються
перевіряльниками. Тести пропускають клітинку налаштування `%pip` блокнота, тому що залежності
встановлені окремо. Вони не змінюють блокнот чи зразки.

## Як це було згенеровано

Зразки використовують той самий шлях коду, що й блокнот, з одним фіксованим ключем підпису
і фіксованими часовими позначками для відтворюваності байтів. Щоб відтворити:

```bash
python3 generate_fixtures.py
```

(Сценарій знаходиться у `generate_fixtures.py` цієї директорії.)

## Чому студенти вчаться, переглядаючи сирий JSON

Читання сирого формату квитанції формує інтуїцію, якої клітинки в блокноті
не завжди дають. Студенти, які переглядають JSON, часто помічають:

1. Підпис — це непрозорий рядок у форматі base64url, але всі інші поля — простий
   читабельний JSON. Підпис не шифрує вміст; він підтверджує його.
2. `public_key` вбудовано у квитанцію, чого достатньо для перевірки
   самозгодженості, але не довіри до видавця. Аудитор має порівняти його з ключем,
   прикріпленим поза квитанцією або вирішеним через надійний реєстр.
3. Зміна одного символу будь-якого поля, а потім повторне порівняння цього файлу з
   `02_tampered_receipt.json` робить механізм на рівні байтів відчутним.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->