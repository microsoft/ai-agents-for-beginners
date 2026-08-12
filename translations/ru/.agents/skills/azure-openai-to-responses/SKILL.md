---
name: azure-openai-to-responses
license: MIT
---
# Миграция Python-приложений с Azure OpenAI Chat Completions на Responses API

> **АВТОРИТЕТНЫЕ РЕКОМЕНДАЦИИ — СЛЕДУЙТЕ ТОЧНО**
>
> Этот навык выполняет миграцию Python-кода с использованием Azure OpenAI Chat Completions
> на единый Responses API. Следуйте этим инструкциям точно.
> Не придумывайте сопоставления параметров и не изобретайте структуру API.

---

## Триггеры

Активируйте этот навык, когда пользователь хочет:
- Мигрировать Python-приложение с Azure OpenAI Chat Completions на Responses API
- Обновить использование Python OpenAI SDK до последней версии API для Azure OpenAI
- Подготовить Python-код для моделей GPT-5 или новее, требующих Responses на Azure
- Переключиться с `AzureOpenAI`/`AsyncAzureOpenAI` на стандартные клиенты `OpenAI`/`AsyncOpenAI` с конечной точкой v1
- Исправить предупреждения об устаревании, связанные с конструкторами `AzureOpenAI` или параметром `api_version`

---

## ⚠️ Совместимость моделей — ПРОВЕРЬТЕ СНАЧАЛА

> **Перед миграцией убедитесь, что ваше развертывание Azure OpenAI поддерживает Responses API.**

### 1. Быстрая проверка развертывания (самый быстрый способ)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **Примечание**: `max_output_tokens` имеет **минимум 16** в Azure OpenAI. Значения меньше 16 вызывают ошибку 400. Для проверки используйте значение 50 и выше.

Если возвращается 404, модель в развертывании пока не поддерживает Responses — проверьте ссылку ниже или разверните с поддерживаемой моделью.

### 2. Проверьте доступные модели в вашем регионе (рекомендуется)

Запустите встроенный инструмент проверки совместимости моделей, чтобы увидеть доступные модели с поддержкой Responses API в вашем регионе:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Этот запрос обращается к Azure ARM в реальном времени и показывает матрицу совместимости — какие модели поддерживают Responses, структурированный вывод, инструменты и т. д. Используйте `--filter gpt-5.1,gpt-5.2` для сужения результатов или `--json` для скриптов.

### 3. Полная справочная информация по поддержке моделей

- **Живой запрос**: `python migrate.py models` (см. выше — регионально-специфичный, всегда актуальный)
- **Просмотр доступности**: [Таблица сводки моделей и доступность по регионам](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Быстрый старт и руководство**: **https://aka.ms/openai/start**

### ⚠️ Ограничения старых моделей

> **ПРЕДУПРЕЖДЕНИЕ**: Старые модели (предшествующие `gpt-4.1`) могут не полностью поддерживать все возможности Responses API.
>
> Известные ограничения старых моделей:
> - **Параметр `reasoning`**: Не поддерживается во многих моделях без рассуждений. Мигрируйте `reasoning` только если он уже был в исходном коде.
> - **Параметр `seed`**: Не поддерживается в Responses API вообще — удалите из всех запросов.
> - **Структурированный вывод через `text.format`**: Старые модели могут не надёжно применять JSON-схемы с `strict: true`.
> - **Оркестрация инструментов**: GPT-5 и новее оркестрируют вызовы инструментов как часть внутренних рассуждений. Старые модели с Responses работают, но без глубокой интеграции.
> - **Ограничения по температуре**: При миграции на `gpt-5` температуру нужно убирать или выставлять равной `1`. У старых моделей таких ограничений нет.

### Модели серии O (o1, o3-mini, o3, o4-mini)

Модели серии O имеют уникальные ограничения параметров. При миграции приложений, нацеленных на модели этой серии:

- **`temperature`**: Должна быть `1` (или отсутствовать). Модели серии O не принимают другие значения.
- **`max_completion_tokens` → `max_output_tokens`**: Приложения, использующие Azure-специфичный `max_completion_tokens`, должны перейти на `max_output_tokens`. Указывайте высокие значения (4096+), поскольку токены рассуждений учитываются в лимите.
- **`reasoning_effort`**: Если приложение использует `reasoning_effort` (low/medium/high), сохраняйте его — Responses API поддерживает этот параметр для моделей серии O.
- **Поведение потоковой передачи**: Модели серии O могут буферизировать вывод до завершения рассуждений, прежде чем отправлять дельты текста. Потоковая передача всё ещё работает, но первый `response.output_text.delta` может появиться с большей задержкой, чем у моделей GPT.
- **`top_p`**: Не поддерживается в серии O — удалите, если присутствует.
- **Использование инструментов**: Модели серии O поддерживают инструменты через Responses API как и GPT-модели, но качество оркестрации вызовов зависит от конкретной модели.

**Действие — проактивное уведомление по модели**: Во время фазы сканирования проверьте, на какую модель направлено приложение (имена развертываний, переменные окружения, конфигурация). Если модель предшествует `gpt-4.1` (не gpt-4.1+), сообщите пользователю:
- Миграция будет работать для базового текста, чата, потоковой передачи и инструментов на их текущей модели.
- Новые модели (`gpt-5.1`, `gpt-5.2`) предлагают улучшенную оркестрацию инструментов, строгость структурированного вывода, рассуждения и кросс-региональную доступность.
- Рекомендуется рассмотреть обновление развертывания при готовности — это не блокирует миграцию.

Не блокируйте и не отказывайте в миграции на основе версии модели. Уведомление носит информационный характер.

### GitHub Models НЕ поддерживает Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) не поддерживает Responses API.**

Если в коде есть код для GitHub Models (ищите `base_url`, указывающий на `models.github.ai` или `models.inference.ai.azure.com`), **полностью удалите его** при миграции. Responses API требует Azure OpenAI, OpenAI или совместимую локальную конечную точку (например, Ollama с поддержкой Responses).

Действие во время сканирования:
- Отметьте все пути с кодом GitHub Models для удаления.

---

## Миграция фреймворков

Многие приложения используют высокоуровневые фреймворки поверх OpenAI. При миграции таких приложений меняется API самого фреймворка — не только вызовы базового OpenAI.

### Microsoft Agent Framework (MAF)

**Сначала проверьте вашу версию MAF** — миграция зависит от того, используете ли вы MAF 1.0.0+ или бета/rc версию до 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **уже использует Responses API** — миграция не требуется. Если в коде встречается устаревший `OpenAIChatCompletionClient` (использующий `chat.completions.create`), замените его на `OpenAIChatClient`.

| До | После |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Для проверки версии: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF до версии 1.0.0 (бета/rc релизы)

В версиях MAF до 1.0.0 `OpenAIChatClient` использовал Chat Completions. Обновитесь до `agent-framework-openai>=1.0.0`, где `OpenAIChatClient` по умолчанию использует Responses API.

Других изменений не требуется — API `Agent` и инструментов остаются прежними.

### LangChain (`langchain-openai`)

Добавьте `use_responses_api=True` в `ChatOpenAI()`. Также обновите доступ к ответу с `.content` на `.text`.

| До | После |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Полные примеры кода до и после смотрите в [cheat-sheet.md](./references/cheat-sheet.md).

---

## Руководство по миграции фронтенда

> **Responses API — это серверная часть.** Мигрируйте ваш Python-бэкенд; HTTP-контракт фронтенда должен оставаться без изменений, если только ваш бэкенд не является легким прокси — в таком случае рассмотрите возможность использования формы запроса Responses для устранения слоя трансляции. Если фронтенд вызывает OpenAI напрямую с клиентским ключом, сначала перенесите эти вызовы на бэкенд.

### Устаревание `@microsoft/ai-chat-protocol`

Пакет `@microsoft/ai-chat-protocol` для npm устарел и должен быть заменён на [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Если вы встретите его во фронтенде:

1. Замените CDN-тег скрипта:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Удалите создание экземпляра `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Замените `client.getStreamedCompletion(messages)` прямым вызовом `fetch()` к эндпоинту потоковой передачи на бэкенде.
4. Замените `for await (const response of result)` на `for await (const chunk of readNDJSONStream(response.body))`.
5. Обновите доступ к свойствам с `response.delta.content` / `response.error` на `chunk.delta.content` / `chunk.error`.

---

## Цели

- Перечислить все вызовы Python, использующие Chat Completions или устаревшие Completions для Azure OpenAI.
- Предложить план миграции и последовательность для Python-кодовой базы.
- Внести безопасные минимальные изменения для перехода на Responses API.
- Обновить вызывающий код для использования схемы вывода Responses; без обёрток для обратной совместимости.
- Запустить тесты/линтеры; исправить тривиальные ошибки, внесённые миграцией.
- Подготовить небольшие удобные для обзора наборы изменений и предоставить финальное резюме с диффами (не коммитить).

---

## Ограничения

- Изменять только файлы внутри git-репозитория. Никогда не писать за его пределами.
- Не сохранять шимы обратной совместимости; мигрировать код на новую структуру API.
- Не оставлять комментарии переходного периода или резервные копии файлов.
- Сохранять семантику потоковой передачи, если она использовалась ранее; иначе использовать непротоковый режим.
- Запрашивать подтверждение перед выполнением команд или сетевых вызовов в режиме подтверждения.
- Не выполнять `git add`, `git commit` или `git push`; генерировать только изменения в рабочем дереве.

---

## Шаг 0: Миграция клиента Azure OpenAI (предварительное условие)

Если в кодовой базе используются конструкторы `AzureOpenAI` или `AsyncAzureOpenAI`, сначала мигрируйте их на стандартные конструкторы `OpenAI` / `AsyncOpenAI`. Azure-специфические конструкторы устарели в `openai>=1.108.1`.

### Почему путь API v1?

Новый эндпоинт `/openai/v1` использует стандартный клиент `OpenAI()`, а не `AzureOpenAI()`, не требует параметра `api_version` и одинаково работает как с OpenAI, так и с Azure OpenAI. Тот же клиентный код защищён от изменений — управление версиями не нужно.

### Ключевые изменения

| До | После |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Полностью удалить |

### Чеклист очистки

- Удалите аргумент `api_version` из конструктора клиента.
- Удалите переменные окружения `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` из `.env`, настроек приложения, файлов Bicep/инфраструктуры.
- Переименуйте `AZURE_OPENAI_CLIENT_ID` в `AZURE_CLIENT_ID` в `.env`, настройках приложения, Bicep/инфраструктуре и тестах (общепринятое соглашение Azure Identity SDK).
- Убедитесь, что `openai>=1.108.1` указана в `requirements.txt` или `pyproject.toml`.

### Миграция переменных окружения

| Старая переменная | Действие | Примечания |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Удалить** | `api_version` не нужен с эндпоинтом v1 |
| `AZURE_OPENAI_API_VERSION` | **Удалить** | То же, что выше |
| `AZURE_OPENAI_CLIENT_ID` | **Переименовать** → `AZURE_CLIENT_ID` | Общепринятое соглашение Azure Identity SDK для `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Оставить** | Нужно для построения `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Оставить** | Используется как параметр `model` в `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Оставить** | Используется как `api_key` для аутентификации по ключу |

Для примеров настройки клиента (синхронный, асинхронный, EntraID, API-ключ, мультиарендность) смотрите [cheat-sheet.md](./references/cheat-sheet.md).

---

## Шаг 1: Обнаружение устаревших точек вызова

Запустите скрипт [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) для поиска всех точек вызова, требующих миграции:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Или выполните эти поиски вручную — каждое совпадение является целью миграции:

```bash
# Вызовы устаревшего API (нужно переписать)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Устаревшие конструкторы клиента Azure (нужно заменить)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Паттерны доступа к форме ответа (нужно обновить)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Определения инструментов в старом вложенном формате (нужно упростить)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Результаты инструментов в старом формате (нужно преобразовать в function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Устаревшие параметры (нужно удалить или переименовать)
rg "response_format"
rg "max_tokens\b"        # переименовать в max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Устаревшие переменные окружения (нужно очистить)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # должно быть AZURE_CLIENT_ID

# Конечные точки моделей GitHub (нужно удалить — API ответов не поддерживается)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Легаси паттерны на уровне фреймворка (нужно обновить)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: заменить на OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: нужен use_responses_api=True

# Тестовая инфраструктура (нужно обновить)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Доступ к телу ошибки фильтра содержимого (нужно обновить — структура изменилась)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # старая единственная форма — теперь content_filter_results (множественное число) внутри массива content_filters

# Прямые HTTP вызовы к конечной точке Chat Completions (нужно обновить URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Эвристики (обнаружение и переписывание)

- **Chat Completions клиент**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Конструкторы клиента Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Инструменты**: преобразуйте определения инструментов для вызова функций из вложенного формата (`{"type": "function", "function": {"name": ...}}`) в плоский формат Responses (`{"type": "function", "name": ...}`); используйте `tool_choice`; возвращайте результаты инструментов как элементы `{"type": "function_call_output", "call_id": ..., "output": ...}` (а не `{"role": "tool", ...}`).
- **Обратные вызовы инструментов**: когда модель возвращает вызовы функций, добавляйте элементы `response.output` в разговор (а не ручной словарь `{"role": "assistant", "tool_calls": [...]}`), затем добавляйте элементы `function_call_output` для каждого результата.
- **Примеры использования инструментов с несколькими примерами**: если разговор включает жёстко заданные примеры вызова инструментов, преобразуйте их в элементы `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. Идентификаторы должны начинаться с `fc_`.
- **`pydantic_function_tool()`**: этот помощник по-прежнему генерирует старый вложенный формат и **не совместим** с `responses.create()`. Замените ручными определениями инструментов или обёрткой для уплощения.
- **Многошаговый диалог**: храните историю разговора в приложении; передавайте предыдущие шаги через элементы `input`.
- **Форматирование**: замените топ-левел `response_format` в Chat на `text.format` в Responses. Каноническая форма: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Элементы содержимого**: замените Chat `content[].type: "text"` на Responses `content[].type: "input_text"` для ходов пользователя/системы.
- **Элементы содержимого с изображениями**: замените Chat `content[].type: "image_url"` на Responses `content[].type: "input_image"`. Поле `image_url` изменяется с вложенного объекта `{"url": "..."}` на плоскую строку. Смотрите шпаргалку для примеров до и после.
- **Усилия рассуждения**: **переносите `reasoning` только если оно уже существует в исходном коде**.
- **Обработка ошибок фильтрации контента**: структура тела ошибки изменилась. Chat Completions использовал `error.body["innererror"]["content_filter_result"]` (единственное число); Responses API использует `error.body["content_filters"][0]["content_filter_results"]` (множественное число, внутри массива). Код, обращающийся к `innererror`, вызовет `KeyError`. Перепишите с использованием нового пути.
- **Прямые HTTP вызовы**: если приложение вызывает Azure OpenAI REST API напрямую (через `requests`, `httpx` и т.д.) используя `/openai/deployments/{name}/chat/completions?api-version=...`, перепишите на `/openai/v1/responses`. Тело запроса меняется: `messages` → `input`, добавляются `max_output_tokens` и `store: false`, удаляется параметр запроса `api-version`. Тело ответа меняется: `choices[0].message.content` → `output[0].content[0].text` (примечание: `output_text` — удобное свойство SDK, отсутствует в сыром JSON REST).

---

## Шаг 2: Применение миграции

### Примечания по миграции (Chat Completions → Responses)

- **Зачем мигрировать**: Responses — унифицированный API для текста, инструментов и потоковой передачи; Chat Completions — устаревший. Для GPT-5 Responses необходим для лучшей производительности.
- **HTTP**: конечная точка Azure меняется с `/openai/deployments/{name}/chat/completions` на `/openai/v1/responses`.
- **Поля**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` остаётся без изменений.
- **Форматирование**: `response_format` → `text.format` с правильным объектом.
- **Элементы содержимого**: замените Chat `content[].type: "text"` на Responses `content[].type: "input_text"` для ходов системы/пользователя.
- **Элементы содержимого с изображениями**: замените Chat `content[].type: "image_url"` на Responses `content[].type: "input_image"`. Упрощение поля `image_url` с `{"image_url": {"url": "..."}}` до `{"image_url": "..."}` (обычная строка — либо HTTPS URL, либо URI данных `data:image/...;base64,...`).

### Справочная таблица сопоставления параметров

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (массив элементов) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (объект) |
| `temperature` | `temperature` (без изменений) |
| `stop` | `stop` (без изменений) |
| `frequency_penalty` | `frequency_penalty` (без изменений) |
| `presence_penalty` | `presence_penalty` (без изменений) |
| `tools` / вызов функций | `tools` (без изменений) |
| `seed` | **Удалить** (не поддерживается) |
| `store` | `store` (установить в `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (плоская строка) |

Для полных примеров кода до и после смотрите [cheat-sheet.md](./references/cheat-sheet.md).

Для миграции тестовой инфраструктуры (моки, снимки, утверждения) смотрите [test-migration.md](./references/test-migration.md).

Для устранения ошибок и проблем смотрите [troubleshooting.md](./references/troubleshooting.md).

---

## Хранение данных и состояние

- Устанавливайте `store: false` во всех запросах Responses.
- Не полагайтесь на предыдущие ID сообщений или контекст, хранящийся на сервере; храните состояние на клиенте и минимизируйте метаданные.

---

## Критерии приемки

### Ворота на уровне кода (все должны пройти)

- [ ] Нет совпадений для `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` в мигрированных файлах.
- [ ] Нет совпадений для `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — все конструкторы используют `OpenAI`/`AsyncOpenAI` с конечной точкой v1.
- [ ] Нет совпадений для `rg "models\.github\.ai|models\.inference\.ai\.azure"` — удалены кодовые пути моделей GitHub.
- [ ] Нет совпадений для `rg "OpenAIChatCompletionClient"` — код MAF 1.0.0+ использует `OpenAIChatClient` (который использует Responses API). В версиях ниже 1.0.0 — обновитесь до `agent-framework-openai>=1.0.0`.
- [ ] Все вызовы `ChatOpenAI(...)` включают `use_responses_api=True`.
- [ ] Нет совпадений для `rg "choices\[0\]"` — весь доступ к ответам использует `resp.output_text` или схемы вывода Responses.
- [ ] Нет `response_format` на верхнем уровне; весь структурированный вывод использует `text={"format": {...}}`.
- [ ] В `requirements.txt` или `pyproject.toml` есть `openai>=1.108.1` и `azure-identity`; зависимости переустановлены.
- [ ] В каждом вызове `responses.create` установлен `store=False`.
- [ ] Нет `api_version` в конструкторе клиента; `AZURE_OPENAI_API_VERSION` удалён из файлов окружения и инфраструктуры.

### Ворота тестовой инфраструктуры (все должны пройти)

- [ ] Нет совпадений для `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Нет совпадений для `rg "_azure_ad_token_provider" tests/` — утверждения обновлены для проверки `isinstance(client, AsyncOpenAI)` или `base_url`.
- [ ] Нет совпадений для `rg "prompt_filter_results|content_filter_results" tests/` — удалены Azure-специфичные мок-объекты фильтров.
- [ ] Моковые фикстуры используют `kwargs.get("input")` вместо `kwargs.get("messages")`.
- [ ] Снимки / золотые файлы обновлены под формат потоковой передачи Responses (без `choices[0]`, `function_call`, `logprobs` и т.п.).
- [ ] `pytest` проходит без сбоев после всех обновлений тестов.

### Поведенческие ворота (проверка вручную или через тестовую оболочку)

- [ ] **Основное завершение**: нестриминговый `responses.create` возвращает непустой `output_text`.
- [ ] **Параллельность потока**: если исходный код использовал потоковую передачу, мигрированный код также использует поток и выдает события `response.output_text.delta` с непустыми дельтами.
- [ ] **Структурированный вывод**: если используется `text.format` с `json_schema`, то `json.loads(resp.output_text)` завершается успешно и соответствует схеме.
- [ ] **Цикл вызовов инструментов**: если используются инструменты, модель вызывает их, приложение выполняет, последующий запрос возвращает финальный `output_text` (без бесконечной петли).
- [ ] **Параллельность async**: если использовался `AsyncAzureOpenAI`, эквивалент `AsyncOpenAI` работает с `await`.
- [ ] **Уровень ошибок**: нет новых ошибок 400/401/404 по сравнению с базовым уровнем до миграции.

### Результаты

- В резюме указаны отредактированные файлы, количество устаревших вызовов до и после, а также следующие шаги.
- Изменения находятся только в рабочем дереве (без коммитов).

---

## Требования к версиям SDK

| Пакет | Минимальная версия |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Последняя (для аутентификации EntraID) |

---

## Ссылки

- [Шпаргалка — все примеры кода](./references/cheat-sheet.md)
- [Миграция тестов — моки, снимки, утверждения](./references/test-migration.md)
- [Устранение неполадок — ошибки, таблица рисков, подводные камни](./references/troubleshooting.md)
- [detect_legacy.py — автоматический сканер](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Стартовый набор Azure OpenAI](https://aka.ms/openai/start)
- [Документация Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Жизненный цикл версии Azure OpenAI API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [Справочник OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->