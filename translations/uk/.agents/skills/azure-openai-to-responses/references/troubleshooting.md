# Усунення несправностей, таблиця ризиків і підводні камені

## Усунення несправностей 400-х помилок

| Помилка | Виправлення |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Визначення інструменту використовує старий вкладений формат Chat Completions | Згорніть з `{"type": "function", "function": {"name": ...}}` до `{"type": "function", "name": ..., "parameters": ...}` — name, опис, параметри мають знаходитися на верхньому рівні |
| `unknown_parameter: input[N].tool_calls` | Результати інструменту для багатокрокових запитів використовують старий формат Chat Completions | Замініть `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` на елементи `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Інструмент із `strict: true` відсутній масив `required` | Якщо `strict: true`, всі властивості мають бути вказані в `required`, а також має бути встановлено `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | Інструмент із `strict: true` не має `additionalProperties: false` | Додайте `"additionalProperties": false` до об’єкта параметрів |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | У Few-shot функціональному виклику ID має неправильний префікс | ID викликів функції мають починатися з `fc_` (наприклад, `fc_example1`), а не з `call_` |
| `missing_required_parameter: text.format.name` | Додайте ключ `"name"` в словник формату (наприклад, `"name": "Output"`) |
| `invalid_type: text.format` | Переконайтеся, що `text.format` є словником із ключами `type`, `name`, `strict`, `schema` — не рядком |
| `invalid input content type` | Використовуйте типи вмісту `input_text`/`output_text` замість Chat `text` |
| `invalid input content type` (image) | Вміст зображення ще використовує `"type": "image_url"` | Змініть на `"type": "input_image"` |
| `Expected object, got string` на `image_url` | `image_url` досі є вкладеним об’єктом `{"url": "..."}` | Згорніть до простого рядка: `"image_url": "https://..."` або `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` для `max_output_tokens` | Мінімум **16** на Azure OpenAI. Використовуйте 50+ для тестів, 1000+ для продакшн. |
| `429 Too Many Requests` під час потокової передачі | Обмеження швидкості. Огорніть потокову передачу в `try/except`, надсилайте JSON з помилкою на фронтенд, реалізуйте повторні спроби з відстрочкою. |
| `KeyError: 'innererror'` під час помилки фільтрації вмісту | Структура тіла помилки фільтру змінилася у Responses API | Chat Completions використовував `error.body["innererror"]["content_filter_result"]`; Responses API використовує `error.body["content_filters"][0]["content_filter_results"]` (множина, всередині масиву). Перепишіть усі доступи `innererror`. |

---

## Таблиця ризиків при міграції

| Симптом | Імовірна помилка | Виправлення |
|---------|---------------|-----|
| Порожній `output_text` / обрізана відповідь | Занизьке значення `max_output_tokens` для моделей, які мислять | Встановіть `max_output_tokens=1000` або більше — токени для мислення враховуються в ліміті |
| `400 invalid_type: text.format` | Передано рядок `response_format` замість словника `text.format` | Використовуйте `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` на `/openai/v1/responses` | Неправильний `base_url` — відсутній суфікс `/openai/v1/` | Переконайтеся, що `base_url=f"{endpoint}/openai/v1/"` (із кінцевим слешем) |
| `401 Unauthorized` після переходу на `OpenAI()` | Не встановлений `api_key` або токен-провайдер неправильно переданий | Для EntraID: `api_key=token_provider` (функція). Для API ключа: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Модель повертає `deployment not found` | Параметр `model` не збігається з ім’ям розгортання Azure | Використовуйте `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — це ім’я розгортання, а не моделі |
| `json.loads(resp.output_text)` викликає `JSONDecodeError` | Не застосовується схема або модель не підтримує строго JSON | Переконайтеся, що `"strict": True` в схемі, і що модель підтримує структурований вивід |
| Потокова передача не видає `delta` події | Перевірка неправильного типу події | Фільтруйте за `event.type == "response.output_text.delta"`, а не за Chat `chat.completion.chunk` |
| Помилка 400 при введенні зображення після міграції | Тип вмісту зображення не оновлено | Змініть `"type": "image_url"` → `"type": "input_image"` та згортання `"image_url": {"url": "..."}` → `"image_url": "..."` (рядок) |
| Виклики інструментів зациклюються | Пропущено результат інструменту у наступному `input` | Після виконання інструмента додайте елемент `{"type": "function_call_output", "call_id": ..., "output": ...}` у `input` наступного запиту |
| Помилка `temperature` з GPT-5 або моделями серії o | Явне значення `temperature`, відмінне від 1 | Видаліть `temperature` або встановіть `1` для GPT-5 та моделей o-серії (o1, o3-mini, o3, o4-mini) |
| Помилка `top_p` з моделями серії o | `top_p` не підтримується | Видаліть `top_p` під час використання моделей o-серії |
| `max_completion_tokens` не розпізнається | Використання параметра Azure-специфічного | Замініть `max_completion_tokens` на `max_output_tokens`. Встановіть 4096+ для моделей o-серії (токени мислення враховуються у ліміті). |
| Порожній або обрізаний вивід з моделей o-серії | `max_output_tokens` занизький | Моделі o-серії використовують внутрішні токени для мислення. Встановіть `max_output_tokens=4096` або більше — не 500–1000. |
| `400 integer_below_min_value` для `max_output_tokens` | Значення менше за 16 | Azure OpenAI вимагає `max_output_tokens >= 16`. Використовуйте 50+ для тестів, 1000+ для продакшн. |
| `429 Too Many Requests` посеред потоку | Обмеження швидкості Azure OpenAI | Потокове передавання переривається без повідомлення про помилки. Завжди огортайте `async for event in await coroutine:` в `try/except` і надсилайте `{"error": str(e)}` на фронтенд. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Неправильний орендар або відсутній вхід | Передайте явно `tenant_id=os.getenv("AZURE_TENANT_ID")`. Запустіть `azd auth login --tenant <tenant-id>` локально. |
| `404 Not Found` при використанні моделей GitHub (`models.github.ai`) | Моделі GitHub не підтримують Responses API | Повністю видаліть код для моделей GitHub. Використовуйте Azure OpenAI, OpenAI або сумісний локальний endpoint (наприклад, Ollama з підтримкою Responses). |
| MAF `OpenAIChatCompletionClient` досі використовує Chat Completions | Використання застарілого клієнта MAF в 1.0.0+ | У MAF 1.0.0+ `OpenAIChatClient` за замовчуванням використовує Responses API. Замініть `OpenAIChatCompletionClient` на `OpenAIChatClient`. Для версій до 1.0.0 оновіться до `agent-framework-openai>=1.0.0`. |
| Аґент LangChain повертає порожньо або не працює з викликами інструментів | `ChatOpenAI` не використовує Responses API | Додайте `use_responses_api=True` до `ChatOpenAI(...)`. Також змініть `.content` → `.text` у відповідях повідомлень. |
| `KeyError: 'innererror'` у обробнику помилок фільтрації вмісту | Структура тіла помилки змінилась у Responses API | Перепишіть `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Обгортка `innererror` зникла; деталі фільтрації вмісту тепер у верхньорівневому масиві `content_filters` з множиною `content_filter_results` всередині кожного елемента. |
| Прямий HTTP виклик до `/openai/deployments/.../chat/completions` повертає 404 | Старий REST endpoint Chat Completions | Перепишіть URL на `/openai/v1/responses`. Змініть тіло запиту: `messages` → `input`, додайте `max_output_tokens` і `store: false`, видаліть параметр запиту `api-version`. Змініть парсинг відповіді: `choices[0].message.content` → `output[0].content[0].text` (зверніть увагу: `output_text` — це зручна властивість SDK, в сирому REST JSON її немає). |

---

## Підводні камені

1. Якщо раніше ви використовували Chat Completions для стану розмови, керуйте своїм станом явно з Responses.
2. Віддавайте перевагу `max_output_tokens` замість застарілого `max_tokens`.
3. При міграції на `gpt-5` переконайтеся, що `temperature` не вказано або встановлено `1`.
4. Замініть Chat `content[].type: "text"` на Responses `content[].type: "input_text"` для вводу користувача/системи.
5. Для `text.format` надайте правильний словник (наприклад, `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), а не простий рядок.
6. Параметр `seed` не підтримується в Responses; видаліть його із запитів.
7. **Мислення**: включайте `reasoning` лише якщо початковий код уже його використовував. Не додавайте `reasoning` у API виклики, де його не було — багато моделей (наприклад, gpt-4o-mini) не підтримують цей параметр.
8. **Розмір `max_output_tokens`**: Для моделей мислення (GPT-5-mini, GPT-5, o-серія) використовуйте `max_output_tokens=4096` або більше — не 50–1000. Модель спочатку використовує токени для мислення перед формуванням видимого виводу; занизькі ліміти призводять до обрізаних або порожніх відповідей.
9. **`max_completion_tokens` для o-серії**: Якщо початковий код використовував `max_completion_tokens` (Azure-специфічний для o-серії), замініть його на `max_output_tokens`. Responses API не приймає `max_completion_tokens`.
10. **`reasoning_effort` для o-серії**: Якщо початковий код використовує `reasoning_effort` (low/medium/high), перенесіть це в виклик Responses API як `reasoning={"effort": "<value>"}`.
11. **Затримка потокової передачі в o-серії**: Моделі o-серії виконують внутрішнє мислення перед виводом. Під час потокової передачі очікуйте більшу затримку перед першою подією `response.output_text.delta`. Це нормальна поведінка — модель мислить, а не зависла.
9. **`_azure_ad_token_provider` зник**: `AsyncOpenAI` / `OpenAI` не мають атрибуту `_azure_ad_token_provider`. Тести або код, що звертаються до цього атрибута, завершаться `AttributeError`. Провайдер токенів передається як `api_key` і не доступний для інспекції через об’єкт клієнта.
10. **Snapshot / golden файли**: Якщо тестовий набір використовує snapshot-тестування, **всі** файли snapshot, що містять форми потокових даних Chat Completions (`choices[0]`, `content_filter_results`, `function_call` тощо), мають бути оновлені до нової форми Responses. Це легко пропустити і викликає помилки перевірки snapshot.
11. **Шлях для monkeypatch моків**: Ціль для monkeypatch змінюється з `openai.resources.chat.AsyncCompletions.create` на `openai.resources.responses.AsyncResponses.create` (або `Responses.create` для синхронних). Використання старого шляху тихо не виконує перехоплення — мок не спрацьовує, тести звертаються до реального API або падають.
12. **`input` замість `messages`**: Мок-функції повинні читати `kwargs.get("input")`, а не `kwargs.get("messages")`. Responses API використовує `input` для історії розмови.
13. **Назви змінних оточення**: Azure Identity SDK використовує `AZURE_CLIENT_ID` (не `AZURE_OPENAI_CLIENT_ID`) для `ManagedIdentityCredential(client_id=...)`. Перейменуйте у тестах, `.env` файлах, налаштуваннях додатка і Bicep/інфраструктурі.
14. **Мінімум для `max_output_tokens` — 16**: Azure OpenAI відхиляє значення менше 16 з помилкою `400 integer_below_min_value`. Використовуйте 50 для тестування, 1000+ для продакшн. Старий `max_tokens` не мав такого мінімуму.
15. **`tenant_id` для `AzureDeveloperCliCredential`**: Коли ресурс Azure OpenAI знаходиться в іншому орендарі, **потрібно** явно передати `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Без цього облікові дані мовчки використовують неправильного орендаря і повертають `401`.
16. **Обмеження частоти проявляються по-іншому у потоках**: З Chat Completions, 429 зазвичай запобігав запуску потоку. З Responses API потокова передача може отримати 429 **посередині потоку** — асинхронний ітератор генерує виняток. Завжди огортайте цикл потокової передачі в `try/except` і надсилайте рядок JSON з помилкою, щоб фронтенд міг обробити це коректно.

17. **Обробка помилок у стрімінгу обов’язкова для веб-додатків**: Шаблон `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` є критично важливим. Без нього SSE/JSONL потік мовчки припиняється при будь-якій серверній помилці, а фронтенд зависає.
18. **Визначення інструментів повинно використовувати плоский формат**: Responses API очікує `{"type": "function", "name": ..., "parameters": ...}`, а не вкладений формат Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Це найпоширеніша помилка при міграції для коду з викликами функцій.
19. **`pydantic_function_tool()` є несумісним**: Хелпер `openai.pydantic_function_tool()` все ще генерує старий вкладений формат. Не використовуйте його з `responses.create()`. Визначайте схеми інструментів вручну або розгортайте вивід.
20. **Результати інструментів використовують `function_call_output`, а не `role: tool`**: Після виконання інструменту додайте `{"type": "function_call_output", "call_id": ..., "output": ...}`, а не `{"role": "tool", "tool_call_id": ..., "content": ...}`. Для запиту інструменту асистента використовуйте `messages.extend(response.output)`, а не вручну `{"role": "assistant", "tool_calls": [...]}` словник.
21. **`strict: true` вимагає `required` + `additionalProperties: false`**: При використанні `strict: true` у інструменті кожна властивість має бути вказана у масиві `required`, а `additionalProperties` має бути `false`. Відсутність будь-якого з них спричиняє помилку 400.
22. **Ідентифікатори викликів функцій мають специфічні префікси**: Коли у `input` подаються few-shot елементи `function_call`, поле `id` має починатися з `fc_`, а поле `call_id` — з `call_` (наприклад, `"id": "fc_example1", "call_id": "call_example1"`). Використання старого префікса Chat Completions `call_` для `id` відхиляється.
23. **GitHub Models не підтримує Responses API**: Якщо додаток містить код для GitHub Models (`base_url`, що вказує на `models.github.ai` або `models.inference.ai.azure.com`), його потрібно повністю видалити. Шляху міграції немає — переходьте на Azure OpenAI, OpenAI або сумісний локальний кінцевий пункт.
24. **Структура помилки фільтрації контенту змінилась**: Помилки Chat Completions використовували `error.body["innererror"]["content_filter_result"]` (однина). Помилки Responses API використовують `error.body["content_filters"][0]["content_filter_results"]` (множина, всередині масиву). Ключ `innererror` тепер відсутній. Код, що напряму звертається до `innererror`, викличе `KeyError` під час виконання — це легко пропустити при міграції, бо проявляється лише коли фільтр контенту спрацьовує. Завжди перевіряйте grep-ом наявність `innererror` під час міграції.
25. **Сирі HTTP виклики потребують перезапису URL + тіла**: Додатки, що викликають Azure OpenAI REST напряму (через `requests`, `httpx`, `aiohttp`), використовуючи `/openai/deployments/{name}/chat/completions?api-version=...`, мають перейти на `/openai/v1/responses`. Тіло запиту використовує `input` замість `messages`, потребує `max_output_tokens` і `store`, а параметр `api-version` видаляється. Текст відповіді знаходиться в `output[0].content[0].text` — **не** в `output_text`, що є властивістю зручності SDK, відсутньою в сирому JSON REST.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->