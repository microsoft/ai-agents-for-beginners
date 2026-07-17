# Вирішення проблем, таблиця ризиків та застереження

## Вирішення проблем із 400 помилками

| Помилка | Виправлення |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Визначення інструменту використовує старий вкладений формат Chat Completions | Перетворіть з `{"type": "function", "function": {"name": ...}}` в `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters повинні бути на верхньому рівні |
| `unknown_parameter: input[N].tool_calls` | Результати мультихвильових інструментів використовують старий формат Chat Completions | Замініть `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` на елементи `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Інструмент з `strict: true` не має масиву `required` | При `strict: true` усі властивості мають бути перелічені у `required`, а також має бути встановлено `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | Інструмент з `strict: true` не має `additionalProperties: false` | Додайте `"additionalProperties": false` в об'єкт параметрів |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID для функції Few-shot `function_call` має неправильний префікс | ID виклику функції має починатися з `fc_` (наприклад, `fc_example1`), а не з `call_` |
| `missing_required_parameter: text.format.name` | Додайте ключ `"name"` у словник формату (наприклад `"name": "Output"`) |
| `invalid_type: text.format` | Переконайтеся, що `text.format` є словником із ключами `type`, `name`, `strict`, `schema` — не рядком |
| `invalid input content type` | Використовуйте типи вмісту `input_text` / `output_text` замість Chat `text` |
| `invalid input content type` (image) | Вміст зображення досі використовує `"type": "image_url"` | Змініть на `"type": "input_image"` |
| `Expected object, got string` на `image_url` | `image_url` все ще є вкладеним об'єктом `{"url": "..."}` | Сплющіть у простий рядок: `"image_url": "https://..."` або `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` для `max_output_tokens` | Мінімум — **16** на Azure OpenAI. Для тестів використовуйте 50+, для продакшена 1000+ |
| `429 Too Many Requests` під час стрімінгу | Перевищено ліміти запитів. Обгорніть стрімінг у `try/except`, передавайте JSON з помилкою на фронтенд, реалізуйте backoff/retry |
| `KeyError: 'innererror'` при помилці фільтра вмісту | Змінилася структура тіла помилки фільтра в Responses API | Chat Completions використовував `error.body["innererror"]["content_filter_result"]`; Responses API використовує `error.body["content_filters"][0]["content_filter_results"]` (множина, масив). Переробіть доступи до `innererror`. |

---

## Таблиця ризиків міграції

| Симптом | Ймовірна помилка | Виправлення |
|---------|---------------|-----|
| Порожній `output_text` / обрізана відповідь | `max_output_tokens` занизький для моделей із reasoning | Встановіть `max_output_tokens=1000` або більше — токени reasoning зараховуються у ліміт |
| `400 invalid_type: text.format` | Передано рядок `response_format` замість словника `text.format` | Використовуйте `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` на `/openai/v1/responses` | Неправильний `base_url` — відсутній суфікс `/openai/v1/` | Переконайтесь, що `base_url=f"{endpoint}/openai/v1/"` (з кінцевим слешем) |
| `401 Unauthorized` після переходу на `OpenAI()` | `api_key` не встановлений або токен-провайдер переданий неправильно | Для EntraID: `api_key=token_provider` (викликальний об'єкт). Для ключа API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Модель повертає `deployment not found` | Параметр `model` не збігається з вашим ім'ям розгортання Azure | Використовуйте `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — це ім'я розгортання, а не моделі |
| `json.loads(resp.output_text)` викликає `JSONDecodeError` | Схема не застосовується або модель не підтримує суворий JSON | Забезпечте `"strict": True` у схемі та перевірте, що модель підтримує структурований вивід |
| Стрімінг не має подій `delta` | Перевірка неправильного типу події | Фільтруйте події за `event.type == "response.output_text.delta"`, а не за Chat `chat.completion.chunk` |
| Помилка 400 на вхідному зображенні після міграції | Тип вмісту зображення не оновлено | Замініть `"type": "image_url"` на `"type": "input_image"` і сплющіть `"image_url": {"url": "..."}` на `"image_url": "..."` (рядок) |
| Виклики інструментів зациклюються | У follow-up `input` відсутній результат інструменту | Після виконання інструменту додайте елемент `{"type": "function_call_output", "call_id": ..., "output": ...}` у `input` наступного запиту |
| Помилка `temperature` з GPT-5 або серією o | Вказане явне значення `temperature`, відмінне від 1 | Приберіть `temperature` або встановіть 1 для моделей GPT-5 та o-серії (o1, o3-mini, o3, o4-mini) |
| Помилка `top_p` з о-серією | `top_p` не підтримується | Приберіть `top_p` при використанні моделей о-серії |
| `max_completion_tokens` не розпізнається | Використання Azure-специфічного параметра | Замініть `max_completion_tokens` на `max_output_tokens`. Встановіть 4096+ для о-серії (токени reasoning зараховуються у ліміт). |
| Порожній/обрізаний вивід з о-серії | `max_output_tokens` надто низький | О-серія використовує токени reasoning внутрішньо. Встановіть `max_output_tokens=4096` або більше — не 500–1000. |
| `400 integer_below_min_value` для `max_output_tokens` | Значення менше 16 | Azure OpenAI вимагає `max_output_tokens >= 16`. Використовуйте 50+ для тестів, 1000+ для продакшена. Старий `max_tokens` такого мінімуму не мав. |
| `429 Too Many Requests` посередині стріму | Ліміт запитів Azure OpenAI | Стрімінг несподівано обривається без обробки помилки. Завжди обгортайте `async for event in await coroutine:` у `try/except` і повертайте `{"error": str(e)}` на фронтенд. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Неправильний орендар або відсутній вхід у систему | Передайте `tenant_id=os.getenv("AZURE_TENANT_ID")` явно. Запустіть `azd auth login --tenant <tenant-id>` локально. |
| `404 Not Found` при використанні GitHub Models (`models.github.ai`) | GitHub Models не підтримує Responses API | Повністю видаліть шлях коду GitHub Models. Використовуйте Azure OpenAI, OpenAI або сумісний локальний endpoint (наприклад, Ollama з підтримкою Responses). |
| MAF `OpenAIChatCompletionClient` досі використовує Chat Completions | Використання застарілого клієнта MAF у 1.0.0+ | У MAF 1.0.0+ `OpenAIChatClient` за замовчуванням використовує Responses API. Замініть `OpenAIChatCompletionClient` на `OpenAIChatClient`. Для версій до 1.0.0 оновіться до `agent-framework-openai>=1.0.0`. |
| Агент LangChain повертає порожні дані або не працює з викликами інструментів | `ChatOpenAI` не використовує Responses API | Додайте `use_responses_api=True` до `ChatOpenAI(...)`. Також змініть `.content` на `.text` у відповідях повідомлень. |
| `KeyError: 'innererror'` в обробнику помилок фільтра вмісту | Змінилася структура тіла помилки у Responses API | Перепишіть `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Обгортка `innererror` зникла; деталі фільтра тепер у масиві верхнього рівня `content_filters` з множиною `content_filter_results` у кожному записі. |
| Прямий HTTP виклик на `/openai/deployments/.../chat/completions` повертає 404 | Старий REST endpoint Chat Completions | Перепишіть URL на `/openai/v1/responses`. Змініть тіло запиту: `messages` → `input`, додайте `max_output_tokens` + `store: false`, видаліть параметр запиту `api-version`. Змініть парсинг відповіді: `choices[0].message.content` → `output[0].content[0].text` (зверніть увагу: `output_text` — це властивість SDK для зручності, немає в сирому REST JSON). |

---

## Застереження

1. Якщо раніше ви використовували Chat Completions для стану розмови, керуйте станом явно через Responses.
2. Надавайте перевагу `max_output_tokens` замість застарілого `max_tokens`.
3. Під час міграції на `gpt-5` переконайтеся, що `temperature` не вказано або встановлено на `1`.
4. Замініть Chat `content[].type: "text"` на Responses `content[].type: "input_text"` для введень користувача/системи.
5. Для `text.format` подайте правильний словник (наприклад, `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), а не простий рядок.
6. Параметр `seed` не підтримується в Responses; видаліть його з запитів.
7. **Reasoning**: Включайте `reasoning` лише якщо початковий код вже його використовував. Не додавайте `reasoning` до API викликів, що його не мали — багато моделей без reasoning цей параметр не підтримують.
8. **Розмір `max_output_tokens`**: Для моделей reasoning (GPT-5-mini, GPT-5, о-серія) використовуйте `max_output_tokens=4096` або більше — не 50–1000. Модель внутрішньо використовує reasoning токени перед генерацією видимого виводу; надто низькі ліміти призводять до обрізаних або порожніх відповідей.
9. **O-series `max_completion_tokens`**: Якщо у початковому коді використовувався `max_completion_tokens` (специфічно для Azure о-серії), замініть його на `max_output_tokens`. Responses API не приймає `max_completion_tokens`.
10. **O-series `reasoning_effort`**: Якщо початковий код використовує `reasoning_effort` (low/medium/high), мігруйте це до `reasoning={"effort": "<value>"}` у виклику Responses API.
11. **Затримка стрімінгу о-серії**: Моделі о-серії виконують внутрішнє reasoning перед генерацією виводу. Під час стрімінгу очікуйте довшу затримку перед першою подією `response.output_text.delta`. Це нормально — модель мислить, а не зависла.
9. **`_azure_ad_token_provider` зник**: `AsyncOpenAI` / `OpenAI` не мають атрибута `_azure_ad_token_provider`. Тести або код, що звертаються до цього атрибута, викличуть `AttributeError`. Провайдер токенів передається як `api_key` і не доступний для інспекції на клієнті.
10. **Снэпшоти / golden файли**: Якщо тестовий набір використовує снэпшот-тестування, **усі** снэпшоти, що містять форми Chat Completions стрімінгу (`choices[0]`, `content_filter_results`, `function_call` тощо), повинні бути оновлені під новий формат Responses. Це легко пропустити і викликає помилки асерції снэпшотів.
11. **Шлях мок-монкіпатчу**: Ціль мокування змінюється з `openai.resources.chat.AsyncCompletions.create` на `openai.resources.responses.AsyncResponses.create` (або `Responses.create` для синхронного). Використання старого шляху нічого не робить — мок не перехопить виклики, і тести звернуться до реального API або впадуть.
12. **`input`, а не `messages`**: Мок-функції мають читати `kwargs.get("input")`, а не `kwargs.get("messages")`. Responses API використовує `input` для історії розмови.
13. **Іменування змінних оточення**: Azure Identity SDK використовує `AZURE_CLIENT_ID` (не `AZURE_OPENAI_CLIENT_ID`) для `ManagedIdentityCredential(client_id=...)`. Перейменуйте у тестах, `.env` файлах, налаштуваннях додатку та Bicep/інфраструктурі.
14. **Мінімум `max_output_tokens` — 16**: Azure OpenAI відхиляє значення менше 16 з помилкою `400 integer_below_min_value`. Використовуйте 50 для smoke-тестів, 1000+ для продакшена. Старий `max_tokens` такого мінімуму не мав.
15. **`tenant_id` для `AzureDeveloperCliCredential`**: Якщо ресурс Azure OpenAI в іншому орендарі, ви **повинні** явно передати `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Без цього обліковий запис мовчки використовує неправильного орендаря і повертає `401`.
16. **Різна поведінка лімітів запитів під час стрімінгу**: З Chat Completions 429 зазвичай блокував початок стріму. З Responses API стрімінг 429 може трапитися **посередині стріму** — асинхронний ітератор викидає виключення. Завжди обгортайте цикл стріму у `try/except` і повертайте JSON з помилкою, щоб фронтенд міг коректно обробити ситуацію.

17. **Обробка помилок у стрімінгу обов’язкова для вебзастосунків**: Шаблон `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` є критично важливим. Без нього потік SSE/JSONL безшумно припиняється при будь-якій серверній помилці, і фронтенд зависає.
18. **Визначення інструментів повинні використовувати плоский формат**: API Responses очікує `{"type": "function", "name": ..., "parameters": ...}` — а не вкладений формат Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Це найпоширеніша помилка міграції для коду виклику функцій.
19. **`pydantic_function_tool()` несумісний**: Хелпер `openai.pydantic_function_tool()` досі генерує старий вкладений формат. Не використовуйте його з `responses.create()`. Визначайте схеми інструментів вручну або робіть плоский вихід.
20. **Результати інструменту використовують `function_call_output`, а не `role: tool`**: Після виконання інструменту додавайте `{"type": "function_call_output", "call_id": ..., "output": ...}` — а не `{"role": "tool", "tool_call_id": ..., "content": ...}`. Для запиту інструменту асистента використовуйте `messages.extend(response.output)` — а не ручний словник `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` вимагає `required` + `additionalProperties: false`**: При використанні `strict: true` для інструменту кожна властивість має бути перерахована в масиві `required`, а `additionalProperties` має бути `false`. Відсутність хоча б однієї з цих вимог призводить до помилки 400.
22. **Ідентифікатори викликів функцій мають специфічні префікси**: При передачі декількох елементів `function_call` у `input`, поле `id` має починатися з `fc_`, а поле `call_id` має починатися з `call_` (наприклад, `"id": "fc_example1", "call_id": "call_example1"`). Використання старого префіксу Chat Completions `call_` для `id` відхиляється.
23. **GitHub Models не підтримує Responses API**: Якщо у застосунку є шлях коду GitHub Models (`base_url`, що вказує на `models.github.ai` або `models.inference.ai.azure.com`), повністю видаліть його. Шляху міграції немає — перейдіть на Azure OpenAI, OpenAI або сумісний локальний кінцевий пункт.
24. **Структура тіла помилки фільтрації контенту змінилася**: Помилки Chat Completions використовували `error.body["innererror"]["content_filter_result"]` (однина). Помилки Responses API використовують `error.body["content_filters"][0]["content_filter_results"]` (множина, всередині масиву). Ключ `innererror` більше не існує. Код, що безпосередньо звертається до `innererror`, викличе `KeyError` під час виконання — це легко пропустити при міграції, оскільки помилка виводиться лише коли фільтр контенту спрацьовує. Завжди шукайте `innererror` під час міграції.
25. **Сирі HTTP виклики потребують переписування URL + тіла запиту**: Застосунки, що безпосередньо викликають Azure OpenAI REST (через `requests`, `httpx`, `aiohttp`) з `/openai/deployments/{name}/chat/completions?api-version=...`, мають перейти на `/openai/v1/responses`. Тіло запиту використовує `input` замість `messages`, вимагає `max_output_tokens` і `store`, а параметр `api-version` у рядку запиту вилучено. Текст у тілі відповіді знаходиться в `output[0].content[0].text` — **не** в `output_text`, що є властивістю зручності SDK і відсутня в сирому REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->