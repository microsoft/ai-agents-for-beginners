# Отстраняване на проблеми, таблица с рискове и предупреждения

## Отстраняване на проблеми с кодове 400

| Грешка | Поправка |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Дефиницията на инструмента използва стария вложен формат за Chat Completions | Преобразувайте от `{"type": "function", "function": {"name": ...}}` към `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters са на върховото ниво |
| `unknown_parameter: input[N].tool_calls` | Резултатите от многооборотен инструмент използват стария формат на Chat Completions | Заменете `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` с елементи `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Инструмент с `strict: true` няма масив `required` | Когато е `strict: true`, всички свойства трябва да са в `required`, а `additionalProperties: false` трябва да е зададено |
| `invalid_function_parameters: 'additionalProperties' is required` | Липсва `additionalProperties: false` при инструмент с `strict: true` | Добавете `"additionalProperties": false` към обекта с параметри |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID на функция с few-shot повикване е с грешен префикс | ID-тата на повикванията на функции трябва да започват с `fc_` (напр. `fc_example1`), а не с `call_` |
| `missing_required_parameter: text.format.name` | Добавете ключ `"name"` към речника format (напр. `"name": "Output"`) |
| `invalid_type: text.format` | Уверете се, че `text.format` е речник с ключове `type`, `name`, `strict`, `schema` — не низ |
| `invalid input content type` | Използвайте типове съдържание `input_text`/`output_text` вместо Chat `text` |
| `invalid input content type` (image) | Съдържанието на изображение все още използва `"type": "image_url"` | Променете на `"type": "input_image"` |
| `Expected object, got string` на `image_url` | `image_url` все още е вложен обект `{"url": "..."}` | Опростете на обикновен низ: `"image_url": "https://..."` или `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` за `max_output_tokens` | Минималната стойност е **16** при Azure OpenAI. Използвайте 50+ за тестове, 1000+ за продукция. |
| `429 Too Many Requests` по време на стрийминг | Ограничение по честота. Обвийте стрийминга в `try/except`, връщайте грешка в JSON към фронтенда, имплементирайте backoff/retry. |
| `KeyError: 'innererror'` при грешка в content filter | Структурата на грешката в content filter е променена в Responses API | Chat Completions използваше `error.body["innererror"]["content_filter_result"]`; Responses API използва `error.body["content_filters"][0]["content_filter_results"]` (множествено число, в масив). Пренапишете всички достъпи до `innererror`. |

---

## Таблица на риска при миграция

| Симптом | Вероятна грешка | Поправка |
|---------|---------------|-----|
| Празен `output_text` / срязан отговор | `max_output_tokens` е твърде ниско за модели за разсъждение | Задайте `max_output_tokens=1000` или повече — токените за разсъждение се броят към лимита |
| `400 invalid_type: text.format` | Подаден е низ `response_format` вместо речник `text.format` | Използвайте `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` на `/openai/v1/responses` | Неправилен `base_url` — липсва суфикс `/openai/v1/` | Уверете се, че `base_url=f"{endpoint}/openai/v1/"` (снаклонена черта накрая) |
| `401 Unauthorized` след смяна на `OpenAI()` | `api_key` не е зададен или token provider не е подаден правилно | За EntraID: `api_key=token_provider` (извикваемото). За API ключ: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Модел връща `deployment not found` | Параметърът `model` не съвпада с името на вашето Azure деплоймънт | Използвайте `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — това е името на деплоймънт, не на модела |
| `json.loads(resp.output_text)` хвърля `JSONDecodeError` | Схемата не се налага или моделът не поддържа стриктен JSON | Уверете се, че `"strict": True` в схемата, и проверете дали моделът поддържа структурирано изходно съдържание |
| Потокът не връща `delta` събития | Филтриране по неправилен тип събитие | Филтрирайте на `event.type == "response.output_text.delta"`, а не Chat `chat.completion.chunk` |
| `400` грешка при подаване на изображение след миграция | Типът съдържание на изображението не е обновен | Променете `"type": "image_url"` на `"type": "input_image"` и опростете `"image_url": {"url": "..."}` на `"image_url": "..."` (обикновен низ) |
| Обаждания към инструменти се въртят безкрайно | Липсва резултат от инструмент в следващия `input` | След изпълнение на инструмент, добавете елемент `{"type": "function_call_output", "call_id": ..., "output": ...}` към `input` в следващата заявка |
| Грешка при параметър `temperature` с GPT-5 или o-series | Ясно указана стойност различна от 1 | Премахнете `temperature` или задайте на `1` за GPT-5 и o-series модели (o1, o3-mini, o3, o4-mini) |
| Грешка при `top_p` с o-series | `top_p` не се поддържа | Премахнете `top_p` при използване на o-series модели |
| `max_completion_tokens` не се разпознава | Използване на параметър специфичен за Azure | Заменете `max_completion_tokens` с `max_output_tokens`. Задайте 4096+ за o-series (токените за разсъждение се броят към лимита). |
| Празен или срязан изход от o-series | `max_output_tokens` е твърде ниско | O-series използва токени за разсъждение вътрешно. Задайте `max_output_tokens=4096` или повече — не 500–1000. |
| `400 integer_below_min_value` за `max_output_tokens` | Стойност под 16 | Azure OpenAI налага `max_output_tokens >= 16`. Използвайте 50+ за тестове, 1000+ за продукция. |
| `429 Too Many Requests` по средата на стрийма | Ограничение от Azure OpenAI | Потокът спира тихо без обработка на грешки. Винаги обвивайте `async for event in await coroutine:` в `try/except` и връщайте `{"error": str(e)}` към фронтенда. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Грешен tenant или не сте влезли | Подайте `tenant_id=os.getenv("AZURE_TENANT_ID")` експлицитно. Стартирайте локално `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` при използване на GitHub Models (`models.github.ai`) | GitHub Models не поддържа Responses API | Премахнете кода за GitHub Models изцяло. Използвайте Azure OpenAI, OpenAI или съвместим локален endpoint (напр. Ollama с поддръжка на Responses). |
| MAF `OpenAIChatCompletionClient` все още използва Chat Completions | Използване на наследник MAF клиент във версия 1.0.0+ | В MAF 1.0.0+, `OpenAIChatClient` използва Responses API по подразбиране. Заменете `OpenAIChatCompletionClient` с `OpenAIChatClient`. За версии преди 1.0.0, обновете към `agent-framework-openai>=1.0.0`. |
| Агент LangChain връща празен или греши при повиквания към инструменти | `ChatOpenAI` не използва Responses API | Добавете `use_responses_api=True` при `ChatOpenAI(...)`. Също променете `.content` на `.text` в отговорните съобщения. |
| `KeyError: 'innererror'` в обработчик на грешки Content Filter | Структурата на тялото на грешката е променена в Responses API | Пренапишете `error.body["innererror"]["content_filter_result"]["jailbreak"]` на `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Обвивката `innererror` е премахната; детайлите за content filter сега са в главен масив `content_filters`, където всеки елемент съдържа множественото `content_filter_results`. |
| Сурово HTTP повикване към `/openai/deployments/.../chat/completions` връща 404 | Стар REST endpoint на Chat Completions | Пренапишете URL на `/openai/v1/responses`. Променете съдържанието на заявката: `messages` → `input`, добавете `max_output_tokens` + `store: false`, премахнете query параметъра `api-version`. Променете разбор на отговора: `choices[0].message.content` → `output[0].content[0].text` (забележка: `output_text` е удобство на SDK, не е в суровия REST JSON). |

---

## Предупреждения

1. Ако преди сте използвали Chat Completions за управление на състоянието на разговора, с Responses трябва да управлявате собственото си състояние явно.
2. Предпочитайте `max_output_tokens` пред наследения `max_tokens`.
3. При миграция към `gpt-5`, уверете се, че `temperature` не е посочен или е зададен на `1`.
4. Заменете Chat `content[].type: "text"` с Responses `content[].type: "input_text"` за входове от потребител/системата.
5. За `text.format` подайте валиден речник (напр. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), а не прост низ.
6. Параметърът `seed` не се поддържа в Responses; премахнете го от заявките.
7. **Разсъждение**: Включвайте `reasoning` само ако оригиналният код вече го използва. Не добавяйте `reasoning` в повиквания към API, които не го съдържаха — много модели (напр. gpt-4o-mini) не поддържат този параметър.
8. **Размер на `max_output_tokens`**: За модели за разсъждение (GPT-5-mini, GPT-5, o-series), използвайте `max_output_tokens=4096` или повече — не 50-1000. Моделът използва вътрешно токени за разсъждение преди генериране на видим изход; твърде ниските лимити водят до срязани или празни отговори.
9. **O-series `max_completion_tokens`**: Ако оригиналният код използва `max_completion_tokens` (специфично за Azure o-series), заменете с `max_output_tokens`. Responses API не приема `max_completion_tokens`.
10. **O-series `reasoning_effort`**: Ако оригиналният код използва `reasoning_effort` (ниско/средно/високо), мигрирайте го към `reasoning={"effort": "<стойност>"}` в повикването към Responses API.
11. **O-series забавяне при стрийминг**: O-series модели изпълняват вътрешно разсъждение преди генериране на изход. При стрийминг очаквайте по-дълго забавяне преди първото `response.output_text.delta` събитие. Това е нормално — моделът разсъждава, не е заседнал.
9. **`_azure_ad_token_provider` вече го няма**: `AsyncOpenAI` / `OpenAI` нямат атрибут `_azure_ad_token_provider`. Тестове или код, които достъпват този атрибут, ще изпаднат в `AttributeError`. Token provider-а се подава като `api_key` и не е достъпен за инспекция в клиентския обект.
10. **Снимки / golden files**: Ако тестовия пакет използва snapshot testing, **всички** snapshot файлове, съдържащи форми за стрийминг на Chat Completions (`choices[0]`, `content_filter_results`, `function_call` и др.) трябва да се обновят към новия формат Responses. Това лесно може да се пропусне и води до неуспех при сравнение на snapshot.
11. **Път към mock monkeypatch**: Целта за monkeypatch се променя от `openai.resources.chat.AsyncCompletions.create` към `openai.resources.responses.AsyncResponses.create` (или `Responses.create` за синхронни). Използването на стария път мълчаливо няма ефект — mock-ът няма да се прихване, а тестовете ще боравят с реалното API или ще се провалят.
12. **`input`, не `messages`**: Mock функциите трябва да четат `kwargs.get("input")`, а не `kwargs.get("messages")`. Responses API използва `input` за история на разговора.
13. **Име на променлива на средата**: Azure Identity SDK използва `AZURE_CLIENT_ID` (не `AZURE_OPENAI_CLIENT_ID`) за `ManagedIdentityCredential(client_id=...)`. Преноменувайте в тестове, `.env` файлове, настройки на приложението и Bicep/инфраструктура.
14. **Минимално `max_output_tokens` е 16**: Azure OpenAI отказва стойности под 16 с `400 integer_below_min_value`. Използвайте `50` за тестове, `1000`+ за продукция. Старият `max_tokens` не налагаше такова ограничение.
15. **`tenant_id` за `AzureDeveloperCliCredential`**: Когато ресурсът Azure OpenAI е в различен tenant, **трябва** да подадете `tenant_id` експлицитно — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Без него, креденциалът използва грешен tenant и връща `401`.
16. **Ограничения по честота се проявяват по-различно при стрийминг**: При Chat Completions, 429 обикновено предотвратява старта на потока. При Responses API стрийминг, 429 може да се случи **по средата на стрийма** — асинхронният итератор хвърля изключение. Винаги обвивайте цикъла за стрийминг в `try/except` и върнете JSON ред за грешка, за да може фронтендът да го обработи гладко.

17. **Обработката на грешки при стрийминг е задължителна за уеб приложения**: Шаблонът `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` е критичен. Без него SSE/JSONL потокът тихо спира при всяка грешка от страна на сървъра и фронтендът се блокира.
18. **Дефинициите на инструментите трябва да използват плосък формат**: Responses API очаква `{"type": "function", "name": ..., "parameters": ...}` — а не вложения формат на Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Това е най-честата грешка при миграция на код за извикване на функции.
19. **`pydantic_function_tool()` е несъвместим**: Помощната функция `openai.pydantic_function_tool()` все още генерира стария вложен формат. Не я използвайте с `responses.create()`. Дефинирайте схемите на инструментите ръчно или изравнете изхода.
20. **Резултатите от инструментите използват `function_call_output`, не `role: tool`**: След изпълнение на инструмент, добавете `{"type": "function_call_output", "call_id": ..., "output": ...}` — не `{"role": "tool", "tool_call_id": ..., "content": ...}`. За заявката на помощника към инструмент използвайте `messages.extend(response.output)` — не ръчното речниково `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` изисква `required` + `additionalProperties: false`**: При използване на `strict: true` за инструмент, всяко свойство трябва да бъде изброено в масива `required` и `additionalProperties` трябва да е `false`. Липсата на някое от двете предизвиква грешка 400.
22. **ID-та за извикване на функции имат специфични префикси**: При предоставяне на малък брой `function_call` елементи в `input`, полето `id` трябва да започва с `fc_`, а полето `call_id` трябва да започва с `call_` (например `"id": "fc_example1", "call_id": "call_example1"`). Използването на стария префикс `call_` на Chat Completions за `id` се отхвърля.
23. **GitHub Models не поддържа Responses API**: Ако приложението има код за GitHub Models (`base_url`, сочещ към `models.github.ai` или `models.inference.ai.azure.com`), премахнете го изцяло. Няма път за миграция — преминете към Azure OpenAI, OpenAI или съвместим локален крайна точка.
24. **Структурата на тялото при грешки на филтъра за съдържание се промени**: Грешките на Chat Completions използваха `error.body["innererror"]["content_filter_result"]` (единствено число). Грешките на Responses API използват `error.body["content_filters"][0]["content_filter_results"]` (множествено, в масив). Ключът `innererror` вече не съществува. Код, който директно достъпва `innererror`, ще хвърли `KeyError` по време на изпълнение — лесно е да се пропусне при миграция, тъй като се появява само когато филтърът за съдържание се активира. Винаги търсете `innererror` при миграция.
25. **Грубите HTTP извиквания изискват пренаписване на URL + тяло**: Приложения, които извикват директно Azure OpenAI REST (чрез `requests`, `httpx`, `aiohttp`) с `/openai/deployments/{name}/chat/completions?api-version=...` трябва да преминат към `/openai/v1/responses`. Тялото на заявката използва `input` вместо `messages`, изисква `max_output_tokens` и `store`, а параметърът `api-version` се отпада. Текстът на отговора е в `output[0].content[0].text` — **не** в `output_text`, който е удобство на SDK, липсващо в суровия REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->