# Отстраняване на проблеми, таблица с рискове и уловки

## Отстраняване на проблеми с 400 грешки

| Грешка | Поправка |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Дефиницията на инструмента използва стария вложен формат на Chat Completions | Преобразувайте от `{"type": "function", "function": {"name": ...}}` към `{"type": "function", "name": ..., "parameters": ...}` — name, description и parameters са на най-горно ниво |
| `unknown_parameter: input[N].tool_calls` | Мултистъпкови резултати от инструменти използват стария формат на Chat Completions | Заменете `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` с `response.output` елементи + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | Инструмент със `strict: true` липсва масив `required` | При `strict: true` всички свойства трябва да са изброени в `required` и да е зададено `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | Инструмент със `strict: true` липсва `additionalProperties: false` | Добавете `"additionalProperties": false` в обекта на параметрите |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Малкофункционален ID на function_call с неправилен префикс | ID-тата на function call трябва да започват с `fc_` (например `fc_example1`), а не с `call_` |
| `missing_required_parameter: text.format.name` | Добавете ключ `"name"` в речника на формата (примерно `"name": "Output"`) |
| `invalid_type: text.format` | Уверете се, че `text.format` е речник с ключове `type`, `name`, `strict`, `schema` — не низ |
| `invalid input content type` | Използвайте типове съдържание `input_text`/`output_text` вместо Chat `text` |
| `invalid input content type` (изображение) | Типът на съдържание на изображението все още използва `"type": "image_url"` | Променете на `"type": "input_image"` |
| `Expected object, got string` при `image_url` | `image_url` все още е вложен обект `{"url": "..."}` | Превърнете го в обикновен низ: `"image_url": "https://..."` или `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` за `max_output_tokens` | Минималната стойност е **16** при Azure OpenAI. Използвайте 50+ за тестове, 1000+ за продукция. |
| `429 Too Many Requests` по време на стрийминг | Лимитиране на честотата. Обградете стрийминга с `try/except`, върнете JSON с грешка към фронтенда, имплементирайте отлагане/повторен опит. |
| `KeyError: 'innererror'` при филтър за съдържание | Структурата на тялото на грешката при филтър за съдържание се е променила в Responses API | Chat Completions използваше `error.body["innererror"]["content_filter_result"]`; Responses API използва `error.body["content_filters"][0]["content_filter_results"]` (множествено число, в масив). Пренапишете всички достъпи до `innererror`. |

---

## Таблица с рискове при миграция

| Симптом | Вероятна грешка | Поправка |
|---------|---------------|-----|
| Празен `output_text` / съкратен отговор | `max_output_tokens` прекалено нисък за модели за разсъждение | Задайте `max_output_tokens=1000` или повече — токените за разсъждение се броят към лимита |
| `400 invalid_type: text.format` | Подаден е низ `response_format` вместо речник `text.format` | Използвайте `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` на `/openai/v1/responses` | Неправилен `base_url` — липсва `/openai/v1/` суфикс | Уверете се, че `base_url=f"{endpoint}/openai/v1/"` (с наклонена черта накрая) |
| `401 Unauthorized` при смяна към `OpenAI()` | `api_key` не е зададен или токен доставчикът не е предаден правилно | За EntraID: `api_key=token_provider` (callable). За API ключ: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Модел връща `deployment not found` | Параметърът `model` не съвпада с името на Azure деплоймента | Използвайте `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — това е името на деплоймента, а не на модела |
| `json.loads(resp.output_text)` хвърля `JSONDecodeError` | Схемата не се налага или моделът не поддържа строги JSON | Уверете се, че `"strict": True` в схемата и проверете дали моделът поддържа структуриран изход |
| В стрийма няма `delta` събития | Филтриране по грешен тип събитие | Филтрирайте по `event.type == "response.output_text.delta"`, не по Chat `chat.completion.chunk` |
| `400` грешка при изображение след миграция | Типът на съдържание на изображението не е обновен | Променете `"type": "image_url"` → `"type": "input_image"` и разгърнете `"image_url": {"url": "..."}` → `"image_url": "..."` (низ) |
| Циклично извикване на инструмент | Липсва резултат от инструмент в следващия `input` | След изпълнение на инструмент, добавяйте елемент `{"type": "function_call_output", "call_id": ..., "output": ...}` към `input` в следващата заявка |
| Грешка при `temperature` с GPT-5 или o-series | Явно зададена стойност за `temperature`, различна от 1 | Премахнете `temperature` или задайте `1` за GPT-5 и о-серия (o1, o3-mini, o3, o4-mini) модели |
| Грешка при `top_p` с o-series | `top_p` не се поддържа | Премахнете `top_p` при използване на o-series модели |
| `max_completion_tokens` не е разпознат | Използване на параметър специфичен за Azure | Заменете `max_completion_tokens` с `max_output_tokens`. Задайте 4096+ за o-series (токените за разсъждение се броят към лимита). |
| Празен/съкратен изход от o-series | `max_output_tokens` прекалено нисък | O-series използва вътрешни токени за разсъждение. Задайте `max_output_tokens=4096` или повече — не 500–1000. |
| `400 integer_below_min_value` за `max_output_tokens` | Стойност под 16 | Azure OpenAI налага `max_output_tokens >= 16`. Използвайте 50+ за тестове, 1000+ за продукция. |
| `429 Too Many Requests` по средата на стрийма | Ограничение от Azure OpenAI | Стриймът прекъсва без грешка. Винаги обграждайте `async for event in await coroutine:` с `try/except` и връщайте `{"error": str(e)}` към фронтенда. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Грешен наемател или не сте влезли в системата | Предайте `tenant_id=os.getenv("AZURE_TENANT_ID")` явно. Изпълнете `azd auth login --tenant <tenant-id>` локално. |
| `404 Not Found` при използване на GitHub Models (`models.github.ai`) | GitHub Models не поддържа Responses API | Премахнете напълно кода за GitHub Models. Използвайте Azure OpenAI, OpenAI или съвместим локален хостинг (например Ollama с поддръжка на Responses). |
| MAF `OpenAIChatCompletionClient` все още използва Chat Completions | Използване на наследен MAF клиент в 1.0.0+ | В MAF 1.0.0+, `OpenAIChatClient` използва Responses API по подразбиране. Заменете `OpenAIChatCompletionClient` с `OpenAIChatClient`. За версии преди 1.0.0 обновете до `agent-framework-openai>=1.0.0`. |
| LangChain агент връща празен резултат или неуспех с повиквания на инструменти | `ChatOpenAI` не използва Responses API | Добавете `use_responses_api=True` на `ChatOpenAI(...)`. Също така променете `.content` → `.text` при съобщенията в отговорите. |
| `KeyError: 'innererror'` в обработчик на филтър за съдържание | Промяна във структурата на тялото на грешката в Responses API | Пренапишете `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Обвивката `innererror` е премахната; детайлите за филтъра за съдържание са сега в масив с върхово ниво `content_filters` с `content_filter_results` (множествено) във всеки елемент. |
| Сурово HTTP повикване към `/openai/deployments/.../chat/completions` връща 404 | Стар REST endpoint на Chat Completions | Пренапишете URL към `/openai/v1/responses`. Променете тялото на заявката: `messages` → `input`, добавете `max_output_tokens` + `store: false`, премахнете query параметъра `api-version`. Променете парсинга на отговора: `choices[0].message.content` → `output[0].content[0].text` (забележка: `output_text` е удобство на SDK, не е в суровия REST JSON). |

---

## Уловки

1. Ако преди сте използвали Chat Completions за управление на състоянието на разговора, управлявайте собственото си състояние явно с Responses.
2. Предпочитайте `max_output_tokens` пред наследствения `max_tokens`.
3. При миграция към `gpt-5`, уверете се, че `temperature` не е посочен или е зададено на `1`.
4. Заменете Chat `content[].type: "text"` с Responses `content[].type: "input_text"` за потребителски/системни входове.
5. За `text.format` предоставете правилен речник (примерно `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), а не обикновен низ.
6. Параметърът `seed` не се поддържа в Responses; премахнете го от заявките.
7. **Разсъждение**: Включвайте `reasoning` само ако оригиналният код вече го е използвал. Не добавяйте `reasoning` при API повиквания, които не го съдържат — много модели без разсъждение не поддържат този параметър.
8. **Размер на `max_output_tokens`**: За модели за разсъждение (GPT-5-mini, GPT-5, о-серия) използвайте `max_output_tokens=4096` или повече — не 50–1000. Моделът използва токени за разсъждение вътрешно преди да генерира видим изход; прекалено ниските лимити водят до съкратени или празни отговори.
9. **O-series `max_completion_tokens`**: Ако оригиналният код използваше `max_completion_tokens` (специфично за Azure o-series), заменете с `max_output_tokens`. Responses API не приема `max_completion_tokens`.
10. **O-series `reasoning_effort`**: Ако оригиналният код използва `reasoning_effort` (ниско/средно/високо), мигрирайте го към `reasoning={"effort": "<стойност>"}` в повикването към Responses API.
11. **Забавяне при стрийминг на o-series**: O-series моделите извършват вътрешно разсъждение преди да генерират изход. При стрийминг очаквайте по-дълго забавяне преди първото събитие `response.output_text.delta`. Това е нормално — моделът разсъждава, не е блокиран.
9. **`_azure_ad_token_provider` е премахнат**: `AsyncOpenAI` / `OpenAI` нямат атрибут `_azure_ad_token_provider`. Тестове или код, които достъпват този атрибут, ще се провалят с `AttributeError`. Доставчикът на токени се подава като `api_key` и не може да бъде инспектиран от клиента.
10. **Снимки / golden файлове**: Ако тестовият пакет използва snapshot тестване, **всички** snapshot файлове със структури от Chat Completions streaming (`choices[0]`, `content_filter_results`, `function_call` и др.) трябва да бъдат обновени към новия формат на Responses. Това е лесно да се пропусне и причинява провали в асерциите.
11. **Път на mock monkeypatch**: Целта на monkeypatch се променя от `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (или `Responses.create` за синхронни). Използването на стария път няма да прихване заявки — mock-ът няма да ги прехване и тестовете ще ползват реалния API или ще се провалят.
12. **`input`, не `messages`**: Mock функциите трябва да четат `kwargs.get("input")`, а не `kwargs.get("messages")`. Responses API използва `input` за история на разговора.
13. **Именуване на променливи на околната среда**: Azure Identity SDK използва `AZURE_CLIENT_ID` (а не `AZURE_OPENAI_CLIENT_ID`) за `ManagedIdentityCredential(client_id=...)`. Прекръстете променливата в тестове, `.env` файлове, настройки на приложения и Bicep/инфраструктура.
14. **Минимално стойност на `max_output_tokens` е 16**: Azure OpenAI отказва стойности под 16 с грешка `400 integer_below_min_value`. Използвайте `50` за бързи тестове, `1000`+ за продукция. Старият `max_tokens` нямаше такова ограничение.
15. **`tenant_id` за `AzureDeveloperCliCredential`**: Когато Azure OpenAI ресурсът е в друг наемател, **трябва** да подадете `tenant_id` явно — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Без него удостоверението използва грешен наемател тихомълком и връща `401`.
16. **Ограничения на честотата при стрийминг**: С Chat Completions, 429 грешка обикновено предотвратява стартирането на стрийма. С Responses API streaming, 429 може да се случи **в средата на стрийма** — асинхронният итератор хвърля изключение. Винаги обграждайте цикъла на стрийма с `try/except` и връщайте ред с JSON грешка, за да може фронтендът да го обработи грациозно.

17. **Обработката на грешки при стрийминг е задължителна за уеб приложения**: Шаблонът `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` е критичен. Без него SSE/JSONL потокът тихо спира при всяка грешка от страна на сървъра и фронтендът блокира.
18. **Дефинициите на инструментите трябва да използват плосък формат**: Responses API очаква `{"type": "function", "name": ..., "parameters": ...}` — а не вложения формат `{"type": "function", "function": {"name": ..., "parameters": ...}}` на Chat Completions. Това е най-честата грешка при миграция на код с извикване на функции.
19. **`pydantic_function_tool()` е несъвместим**: Помощната функция `openai.pydantic_function_tool()` все още генерира стария вложен формат. Не го използвайте с `responses.create()`. Дефинирайте схемите на инструментите ръчно или опростете изхода.
20. **Резултатите от инструментите използват `function_call_output`, а не `role: tool`**: След изпълнение на инструмент добавете `{"type": "function_call_output", "call_id": ..., "output": ...}` — а не `{"role": "tool", "tool_call_id": ..., "content": ...}`. За заявката на помощника към инструмент използвайте `messages.extend(response.output)` — а не ръчното добавяне на речник `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` изисква `required` + `additionalProperties: false`**: При използване на `strict: true` върху инструмент, всяко свойство трябва да бъде изброено в масива `required` и `additionalProperties` трябва да е `false`. Липсата на някое от двете причинява грешка 400.
22. **ID-та на извиквания на функции имат специфични префикси**: При предоставяне на няколко примера със `function_call` в `input`, полето `id` трябва да започва с `fc_`, а полето `call_id` трябва да започва с `call_` (например `"id": "fc_example1", "call_id": "call_example1"`). Използването на стария префикс `call_` за `id` от Chat Completions се отхвърля.
23. **GitHub Models не поддържа Responses API**: Ако приложението има кодова пътека за GitHub Models (`base_url`, сочещ към `models.github.ai` или `models.inference.ai.azure.com`), премахнете я изцяло. Няма път за миграция — преминете към Azure OpenAI, OpenAI или съвместим локален крайна точка.
24. **Структурата на тялото на грешката при филтриране на съдържание се промени**: Грешките в Chat Completions използваха `error.body["innererror"]["content_filter_result"]` (единствено число). Грешките в Responses API използват `error.body["content_filters"][0]["content_filter_results"]` (множествено число, в масив). Ключът `innererror` вече не съществува. Код, който директно достъпва `innererror`, ще хвърли `KeyError` по време на изпълнение — това е лесно да бъде пропуснато при миграция, защото се появява само когато филтърът за съдържание реално се задейства. Винаги търсете `innererror` при миграция.
25. **Трябва пренаписване на URL и тяло при директни HTTP извиквания**: Приложения, които използват Azure OpenAI REST директно (чрез `requests`, `httpx`, `aiohttp`) с `/openai/deployments/{name}/chat/completions?api-version=...`, трябва да преминат към `/openai/v1/responses`. Тялото на заявката използва `input` вместо `messages`, изисква `max_output_tokens` и `store`, а параметърът `api-version` се премахва. Текстът на отговора е под `output[0].content[0].text` — **не** `output_text`, който е удобна собственост на SDK и липсва в суровия REST JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->