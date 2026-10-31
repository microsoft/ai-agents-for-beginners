# Примеры квитанций

Три заранее сгенерированных файла квитанций для ознакомления без запуска блокнота.

| Файл | Что это такое |
|---|---|
| `01_valid_receipt.json` | Действительная подписанная квитанция для вызова инструмента `lookup_flights`. Проверка возвращает True. |
| `02_tampered_receipt.json` | Та же квитанция с изменённым после подписи полем. Проверка возвращает False. |
| `03_chain_three_receipts.json` | Цепочка из трёх действительных квитанций (search, hold, book) с `previous_receipt_hash`, связывающим каждую с предыдущей. |

Примеры подписывают канонические байты JCS полезной нагрузки напрямую с помощью Ed25519.
SHA-256 используется для дайджестов содержимого и связей цепочки квитанций, а не
как дополнительный препросчёт хеша перед подписью.

## Проверка примеров

В `18-signed-receipts.ipynb` сначала выполните Setup и разделы 1-3.
В разделе 3 определяется `verify_chain`; одних разделов 1 и 2 недостаточно.
Затем запустите следующий блок в новой ячейке, при этом рабочая директория блокнота
должна быть установлена в `18-securing-ai-agents/code_samples`. Пути к примерам ниже относительно
этой директории.

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

### Проверка примера без Jupyter

От корня репозитория установите зависимости урока и выполните:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Эти тесты выполняют примеры на Python из блокнота и точный блок README выше.
Они также проверяют, что изменения и неподтверждённые ключи отвергаются
проверяющими. Тесты пропускают ячейку настройки `%pip` блокнота, так как зависимости устанавливаются отдельно.
Они не изменяют блокнот или примеры.

## Как они были сгенерированы

Примеры используют тот же путь кода, что и блокнот, с одним постоянным ключом для подписи
и фиксированными отметками времени для воспроизводимости на уровне байтов. Для регенерации:

```bash
python3 generate_fixtures.py
```

(Скрипт находится по пути `generate_fixtures.py` в этой директории.)

## Что студенты узнают, изучая необработанный JSON

Чтение необработанного формата квитанции развивает интуицию, которой в ячейках блокнота
не всегда хватает. Студенты, быстро просматривающие JSON, часто замечают:

1. Подпись представляет собой непрозрачную строку base64url, но все остальные поля — 
   простой читаемый JSON. Подпись не шифрует содержимое; она подтверждает его.
2. `public_key` встроен в квитанцию, чего достаточно для проверки
   внутренней согласованности, но не для доверия эмитенту. Аудитор должен сравнить его с ключом,
   закреплённым вне квитанции или разрешённым через доверенный реестр.
3. Изменение одного символа в любом поле и повторное сравнение этого файла с
   `02_tampered_receipt.json` наглядно демонстрирует механизм на уровне байтов.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->