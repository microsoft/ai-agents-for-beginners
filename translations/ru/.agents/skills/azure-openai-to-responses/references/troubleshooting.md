# Устранение неполадок, таблица рисков и подводные камни

## Устранение неполадок 400-х ошибок

| Ошибка | Исправление |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Определение инструмента использует старый вложенный формат Chat Completions | Сверните из `{"type": "function", "function": {"name": ...}}` в `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters должны быть на верхнем уровне |
| `unknown_parameter: input[N].tool_calls` | Многошаговые результаты инструментов используют старый формат Chat Completions | Замените `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` на элементы `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | У инструмента с `strict: true` отсутствует массив `required` | При `strict: true` все свойства должны быть перечислены в `required`, а `additionalProperties: false` должен быть установлен |
| `invalid_function_parameters: 'additionalProperties' is required` | У инструмента с `strict: true` отсутствует `additionalProperties: false` | Добавьте `"additionalProperties": false` в объект параметров |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | У идентификатора function_call из few-shot неправильный префикс | Идентификаторы function_call должны начинаться с `fc_` (например, `fc_example1`), а не с `call_` |
| `missing_required_parameter: text.format.name` | Добавьте ключ `"name"` в словарь формата (например, `"name": "Output"`) |
| `invalid_type: text.format` | Убедитесь, что `text.format` — это словарь с ключами `type`, `name`, `strict`, `schema`, а не строка |
| `invalid input content type` | Используйте типы контента `input_text`/`output_text` вместо Chat `text` |
| `invalid input content type` (image) | Тип контента изображения все еще `"type": "image_url"` | Измените на `"type": "input_image"` |
| `Expected object, got string` на `image_url` | `image_url` все еще вложенный объект `{"url": "..."}` | Сверните в простую строку: `"image_url": "https://..."` или `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` для `max_output_tokens` | Минимум **16** в Azure OpenAI. Используйте 50+ для тестов, 1000+ для продакшена. |
| `429 Too Many Requests` при стриминге | Ограничение по скорости. Оберните стриминг в `try/except`, возвращайте JSON с ошибкой во фронтенд, реализуйте повторные попытки с откатом. |
| `KeyError: 'innererror'` при ошибке фильтра контента | Структура тела ошибки фильтра контента изменилась в Responses API | В Chat Completions использовалось `error.body["innererror"]["content_filter_result"]`; Responses API использует `error.body["content_filters"][0]["content_filter_results"]` (множественное число, внутри массива). Перепишите весь доступ к `innererror`. |

---

## Таблица рисков при миграции

| Симптом | Вероятная ошибка | Исправление |
|---------|---------------|-----|
| Пустой `output_text` / усеченный ответ | `max_output_tokens` слишком низкий для моделей рассуждения | Установите `max_output_tokens=1000` или выше — токены рассуждения учитываются в лимите |
| `400 invalid_type: text.format` | Передана строка `response_format` вместо словаря `text.format` | Используйте `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` на `/openai/v1/responses` | Неверный `base_url` — отсутствует суффикс `/openai/v1/` | Убедитесь, что `base_url=f"{endpoint}/openai/v1/"` (с завершающим слэшем) |
| `401 Unauthorized` после переключения на `OpenAI()` | `api_key` не установлен или неправильно передан поставщик токена | Для EntraID: `api_key=token_provider` (вызываемый объект). Для API-ключа: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Модель возвращает `deployment not found` | Параметр `model` не совпадает с именем вашего Azure-развертывания | Используйте `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — это имя развертывания, а не имя модели |
| `json.loads(resp.output_text)` вызывает `JSONDecodeError` | Схема не соблюдена или модель не поддерживает строгий JSON | Убедитесь, что `"strict": True` в схеме, и проверьте поддержку структурированного вывода моделью |
| В стриме нет событий `delta` | Проверяется неправильный тип события | Фильтруйте по `event.type == "response.output_text.delta"`, а не по Chat'овскому `chat.completion.chunk` |
| Ошибка `400` на ввод изображения после миграции | Тип контента изображения не обновлен | Измените `"type": "image_url"` → `"type": "input_image"` и сверните `"image_url": {"url": "..."}` → `"image_url": "..."` (простая строка) |
| Цикл вызовов инструментов бесконечный | Отсутствует результат инструмента в следующем `input` | После исполнения инструмента добавьте элемент `{"type": "function_call_output", "call_id": ..., "output": ...}` в `input` следующего запроса |
| Ошибка `temperature` с GPT-5 или o-series | Явное значение `temperature`, отличное от 1 | Удалите `temperature` или установите в `1` для моделей GPT-5 и o-series (o1, o3-mini, o3, o4-mini) |
| Ошибка `top_p` с o-series | `top_p` не поддерживается | Удалите `top_p` при работе с моделями o-series |
| `max_completion_tokens` не распознается | Используется параметр, специфичный для Azure | Замените `max_completion_tokens` на `max_output_tokens`. Установите 4096+ для o-series (токены рассуждения учитываются в лимите). |
| Пустой или усеченный вывод от o-series | `max_output_tokens` слишком низкий | O-series использует внутренние токены рассуждения. Установите `max_output_tokens=4096` или выше — не 500–1000. |
| `400 integer_below_min_value` для `max_output_tokens` | Значение ниже 16 | Azure OpenAI требует `max_output_tokens >= 16`. Используйте 50+ для коротких тестов, 1000+ для продакшена. |
| `429 Too Many Requests` в середине потока | Ограничение скорости Azure OpenAI | Поток прерывается без ошибки. Всегда оборачивайте `async for event in await coroutine:` в `try/except` и возвращайте `{"error": str(e)}` во фронтенд. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Неверный тенант или не выполнен вход | Явно передайте `tenant_id=os.getenv("AZURE_TENANT_ID")`. Запустите `azd auth login --tenant <tenant-id>` локально. |
| `404 Not Found` при использовании GitHub Models (`models.github.ai`) | GitHub Models не поддерживает Responses API | Полностью уберите путь к GitHub Models. Используйте Azure OpenAI, OpenAI или совместимый локальный эндпоинт (например, Ollama с поддержкой Responses). |
| MAF `OpenAIChatCompletionClient` все еще использует Chat Completions | Используется устаревший клиент MAF в 1.0.0+ | В MAF 1.0.0+ `OpenAIChatClient` по умолчанию использует Responses API. Замените `OpenAIChatCompletionClient` на `OpenAIChatClient`. Для версий ниже 1.0.0 обновитесь до `agent-framework-openai>=1.0.0`. |
| Агент LangChain возвращает пустое или падает при вызовах инструментов | `ChatOpenAI` не использует Responses API | Добавьте `use_responses_api=True` в `ChatOpenAI(...)`. Также замените `.content` → `.text` в сообщениях ответа. |
| `KeyError: 'innererror'` в обработчике ошибки фильтра контента | Структура ошибки изменилась в Responses API | Перепишите `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Обертка `innererror` исчезла; детали фильтра контента теперь в верхнем массиве `content_filters` с `content_filter_results` (множественное число) внутри каждого элемента. |
| Сырой HTTP-вызов к `/openai/deployments/.../chat/completions` возвращает 404 | Старый REST эндпоинт Chat Completions | Перепишите URL в `/openai/v1/responses`. Измените тело запроса: `messages` → `input`, добавьте `max_output_tokens` + `store: false`, удалите параметр запроса `api-version`. Измените разбор ответа: `choices[0].message.content` → `output[0].content[0].text` (примечание: `output_text` — это свойство удобства SDK, отсутствует в сыром REST JSON). |

---

## Подводные камни

1. Если вы ранее использовали Chat Completions для состояния разговора, теперь явно управляйте своим состоянием с Responses.
2. Предпочитайте `max_output_tokens` вместо устаревшего `max_tokens`.
3. При миграции на `gpt-5` убедитесь, что `temperature` не указан или установлен в `1`.
4. Замените Chat `content[].type: "text"` на Responses `content[].type: "input_text"` для ввода пользователя/системы.
5. Для `text.format` поставьте правильный словарь (например, `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), а не простую строку.
6. Параметр `seed` не поддерживается в Responses; удалите его из запросов.
7. **Рассуждения**: Включайте `reasoning` только если исходный код уже его использовал. Не добавляйте `reasoning` в вызовы API, в которых его не было — многие модели без рассуждений не поддерживают этот параметр.
8. **Размер `max_output_tokens`**: Для моделей рассуждения (GPT-5-mini, GPT-5, o-series) используйте `max_output_tokens=4096` или выше — не 50–1000. Модель использует внутренние токены рассуждения перед генерацией видимого вывода; слишком низкие лимиты приводят к усеченным или пустым ответам.
9. **`max_completion_tokens` у o-series**: Если в исходном коде использовался `max_completion_tokens` (специфичный для Azure параметр для o-series), замените его на `max_output_tokens`. Responses API не принимает `max_completion_tokens`.
10. **`reasoning_effort` у o-series**: Если в исходном коде использовался `reasoning_effort` (low/medium/high), мигрируйте его в `reasoning={"effort": "<value>"}` в вызове Responses API.
11. **Задержка при стриминге у o-series**: Модели o-series выполняют внутренние рассуждения перед генерацией вывода. При стриминге ожидайте большую задержку перед первым событием `response.output_text.delta`. Это нормально — модель размышляет, а не зависла.
9. **`_azure_ad_token_provider` исчез**: `AsyncOpenAI` / `OpenAI` больше не имеют атрибута `_azure_ad_token_provider`. Тесты или код, обращающиеся к этому атрибуту, выдадут `AttributeError`. Поставщик токена передается как `api_key` и не доступен для просмотра в клиентском объекте.
10. **Снэпшоты / золотые файлы**: Если в тестах используется снэпшот-тестирование, **все** снэпшот-файлы, содержащие формы стрима Chat Completions (`choices[0]`, `content_filter_results`, `function_call` и т.д.), должны быть обновлены до новой формы Responses. Это легко пропустить и приводит к ошибкам проверки снэпшотов.
11. **Путь мок-монкипатча**: Цель монкипатча меняется с `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (или `Responses.create` для синхронных вызовов). Использование старого пути не вызывает ошибок, но мок не перехватывает запросы, тесты обращаются к реальному API или падают.
12. **`input`, а не `messages`**: Мок-функции должны читать `kwargs.get("input")`, а не `kwargs.get("messages")`. Responses API использует `input` для истории разговора.
13. **Именование переменных окружения**: Azure Identity SDK использует `AZURE_CLIENT_ID` (не `AZURE_OPENAI_CLIENT_ID`) для `ManagedIdentityCredential(client_id=...)`. Переименуйте в тестах, `.env` файлах, настройках приложений и Bicep/инфраструктуре.
14. **Минимум для `max_output_tokens` — 16**: Azure OpenAI отклоняет значения ниже 16 с ошибкой `400 integer_below_min_value`. Используйте 50 для простых тестов, 1000+ для продакшена. Старый `max_tokens` такого ограничения не имел.
15. **`tenant_id` для `AzureDeveloperCliCredential`**: Если ресурс Azure OpenAI находится в другом тенанте, вы **должны** явно передать `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Без этого учётные данные молча используют неправильный тенант и возвращают `401`.
16. **Ограничения скорости проявляются по-разному при стриминге**: В Chat Completions ошибка 429 обычно не позволяла начать поток. В Responses API при стриминге 429 может возникнуть **середине потока** — асинхронный итератор вызовет исключение. Всегда оборачивайте цикл стрима в `try/except` и возвращайте строку с JSON-ошибкой, чтобы фронтенд мог обработать ситуацию корректно.

17. **Обработка ошибок потоковой передачи обязательна для веб-приложений**: Шаблон `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` критически важен. Без него поток SSE/JSONL молча завершится при любой ошибке на стороне сервера, и фронтенд зависнет.
18. **Определения инструментов должны использовать плоский формат**: API Responses ожидает `{"type": "function", "name": ..., "parameters": ...}`, а не вложенный формат Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Это самая частая ошибка при миграции кода с вызовом функций.
19. **`pydantic_function_tool()` несовместим**: Помощник `openai.pydantic_function_tool()` по-прежнему генерирует старый вложенный формат. Не используйте его с `responses.create()`. Определяйте схемы для инструментов вручную или выравнивайте вывод.
20. **Результаты инструментов используют `function_call_output`, а не `role: tool`**: После выполнения инструмента добавляйте `{"type": "function_call_output", "call_id": ..., "output": ...}`, а не `{"role": "tool", "tool_call_id": ..., "content": ...}`. Для запроса ассистента к инструменту используйте `messages.extend(response.output)`, а не вручную создавайте словарь `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` требует `required` + `additionalProperties: false`**: При использовании `strict: true` для инструмента каждое свойство должно быть перечислено в массиве `required`, а `additionalProperties` обязателен и должен быть `false`. Отсутствие любого из этих требований вызывает ошибку 400.
22. **Идентификаторы вызова функций имеют специфические префиксы**: При передаче нескольких элементов `function_call` в `input` поле `id` должно начинаться с `fc_`, а поле `call_id` — с `call_` (например, `"id": "fc_example1", "call_id": "call_example1"`). Использование старого префикса Chat Completions `call_` для `id` отклоняется.
23. **GitHub Models не поддерживает Responses API**: Если в приложении есть код для GitHub Models (`base_url`, указывающий на `models.github.ai` или `models.inference.ai.azure.com`), полностью удалите его. Нет пути миграции — перейдите на Azure OpenAI, OpenAI или совместимый локальный эндпоинт.
24. **Структура тела ошибки контент-фильтра изменилась**: Ошибки Chat Completions использовали `error.body["innererror"]["content_filter_result"]` (в единственном числе). Ошибки Responses API используют `error.body["content_filters"][0]["content_filter_results"]` (во множественном числе, внутри массива). Ключ `innererror` больше не существует. Код, напрямую обращающийся к `innererror`, вызовет `KeyError` во время выполнения — это легко пропустить при миграции, так как ошибка появляется только при срабатывании контент-фильтра. Всегда ищите `innererror` при миграции.
25. **Вызовы raw HTTP требуют переписывания URL и тела запроса**: Приложения, обращающиеся к Azure OpenAI REST напрямую (через `requests`, `httpx`, `aiohttp`) с `/openai/deployments/{name}/chat/completions?api-version=...`, должны переключиться на `/openai/v1/responses`. Тело запроса использует `input` вместо `messages`, требует `max_output_tokens` и `store`, а параметр запроса `api-version` убран. Текст ответа находится в `output[0].content[0].text` — **не** в `output_text`, который является удобством SDK и отсутствует в raw REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->