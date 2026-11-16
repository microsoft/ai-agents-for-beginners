# Примеры квитанций

Четыре заранее сгенерированных файла квитанций для проверки без запуска блокнота.

| Файл | Что это такое |
|---|---|
| `01_valid_receipt.json` | Действительная подписанная квитанция для вызова инструмента `lookup_flights`. Проверка возвращает True. |
| `02_tampered_receipt.json` | Та же квитанция с одним изменённым полем после подписания. Проверка возвращает False. |
| `03_chain_three_receipts.json` | Цепочка из трёх действительных квитанций (поиск, удержание, бронирование) с `previous_receipt_hash`, связывающим каждую с предыдущей. |
| `04_resigned_receipt.json` | Та же квитанция, но подвергнутая подделке и затем повторно подписанная злоумышленником, с встроенным собственным открытым ключом атакующего. Проверяется по ключу внутри неё. Не проходит проверку по ключу издателя. |

Примеры подписывают канонические байты JCS полезной нагрузки напрямую с помощью Ed25519.
SHA-256 остаётся в использовании для дайджестов содержимого и ссылок в цепочке квитанций, а не как
дополнительный препроцессор хэша перед подписанием.

## Проверка примеров

В `18-signed-receipts.ipynb` сначала выполните Setup и разделы 1–3.
Раздел 3 определяет `verify_chain`; одних только разделов 1 и 2 недостаточно.
Затем выполните следующий блок в новой ячейке, установив рабочую директорию блокнота
в `18-securing-ai-agents/code_samples`. Пути к примерам ниже относительны
этой директории.

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

### Проверка примера без Jupyter

Из корня репозитория установите зависимости урока и запустите:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Эти тесты выполняют примеры Python из блокнота и точный блок README
выше. Они также проверяют, что изменения и неподписанные ключи отвергаются
проверяющими. Тесты пропускают ячейку настройки `%pip` в ноутбуке, потому что зависимости
устанавливаются отдельно. Они не изменяют ноутбук или фикстуры.

## Как они были сгенерированы

Фикстуры используют тот же кодовый путь, что и ноутбук, с одним фиксированным
ключом подписи и фиксированными временными метками для побайтовой воспроизводимости. Чтобы сгенерировать заново:

```bash
python3 generate_fixtures.py
```

(Скрипт находится в `generate_fixtures.py` в этом каталоге.)

`../test_signed_receipts.py` проверяет все это автоматически: он запускает
код ноутбука, проверяет эти четыре фикстуры с помощью
`verify_receipt` и `verify_chain` из ноутбука и подтверждает, что повторное создание
фикстур дает идентичные байты. Из `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Чему студенты учатся при изучении исходного JSON

Чтение исходного формата квитанции формирует интуицию, которую ячейки в ноутбуке
не всегда дают. Студенты, которые бегло просматривают JSON, часто замечают:

1. Подпись — это непрозрачная строка в base64url, а все остальные поля — обычный
   читаемый JSON. Подпись не шифрует содержимое; она подтверждает его.
2. `public_key` встроен в квитанцию, что делает файл
   автономным, но это не то, что проверяет аудитор. Сравните
   `02_tampered_receipt.json` и `04_resigned_receipt.json`: оба были
   изменены после подписи, но второй был повторно подписан ключом
   злоумышленника, поэтому он проверяется с помощью ключа, который содержит. Встроенный ключ
   показывает, что файл внутренне согласован. Только ключ,
   полученный из другого источника, показывает, кто его выдал.
3. Изменение одного символа в любом поле, кроме `signature`, а затем
   повторное сравнение этого файла с `02_tampered_receipt.json` делает
   механизм на уровне байтов понятным на практике.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->