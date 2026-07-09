# Решавање проблема, табела ризика и замке

## Решавање проблема са 400-има

| Грешка | Поправка |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Дефиниција алата користи стари угнежђени формат Чет Комплитација | Исправити са `{"type": "function", "function": {"name": ...}}` на `{"type": "function", "name": ..., "parameters": ...}` — име, опис, параметри иду на највиши ниво |
| `unknown_parameter: input[N].tool_calls` | Резултати вишеструких окрета алата користе стари формат Чет Комплитација | Заменити `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` са предметима из `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` алат нема `required` низ | Када је `strict: true`, све особине морају бити наведене у `required` и мора бити постављено `additionalProperties: false` |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` алат нема `additionalProperties: false` | Додати `"additionalProperties": false` у објекат параметара |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | Једнај функцијски позив има погрешан префикс | Идентитети функцијских позива морају почети са `fc_` (нпр. `fc_example1`), а не са `call_` |
| `missing_required_parameter: text.format.name` | Додати кључ `"name"` у дицт формата (нпр. `"name": "Output"`) |
| `invalid_type: text.format` | Осигурати да је `text.format` речник са кључевима `type`, `name`, `strict`, `schema` — не текст |
| `invalid input content type` | Користити типове садржаја `input_text`/`output_text` уместо Чат `text` |
| `invalid input content type` (слика) | Тип садржаја слике још увек користи `"type": "image_url"` | Променити у `"type": "input_image"` |
| `Expected object, got string` на `image_url` | `image_url` је још увек угнежђени објекат `{"url": "..."}` | Исправити на обичан низ: `"image_url": "https://..."` или `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` за `max_output_tokens` | Минимална вредност је **16** на Azure OpenAI. За тестове користити 50+, за продукцију 1000+. |
| `429 Too Many Requests` током стримовања | Ограничавање брзине. Увити стримовање у `try/except`, послати JSON грешку фронтенду, имплементирати одлагање/покушај поново. |
| `KeyError: 'innererror'` на грешци филтера садржаја | Структура тела грешке филтера садржаја се променила у Responses API-ју | Чет Комплитације су користиле `error.body["innererror"]["content_filter_result"]`; Responses API користи `error.body["content_filters"][0]["content_filter_results"]` (множествено, у низу). Пребацити сав приступ `innererror`. |

---

## Табела ризика миграције

| Симптом | Вероваћна грешка | Поправка |
|---------|---------------|-----|
| Празан `output_text` / скраћен одговор | `max_output_tokens` прегрмкао за моделе за расуђивање | Поставити `max_output_tokens=1000` или више — расуђивачки токени рачунају у лимит |
| `400 invalid_type: text.format` | Прослеђен низ `response_format` уместо речника `text.format` | Користити `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` на `/openai/v1/responses` | Погрешан `base_url` — недостаје суфикс `/openai/v1/` | Обезбедити `base_url=f"{endpoint}/openai/v1/"` (са завршним косим цртом) |
| `401 Unauthorized` након преласка на `OpenAI()` | `api_key` није постављен или није исправно прослеђен токен провајдер | За EntraID: `api_key=token_provider` (позивни објекат). За API кључ: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Модел враћа `deployment not found` | `model` параметар не одговара имену ваше Azure имплементације | Користите `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — ово је име имплементације, не модела |
| `json.loads(resp.output_text)` баца `JSONDecodeError` | Шема није обезбеђена или модел не подржава стриктни JSON | Поставити `"strict": True` у шему и провјерити подршку модела за структуриран излаз |
| Стримовање не враћа `delta` догађаје | Проверава се погрешан тип догађаја | Филтрирати по `event.type == "response.output_text.delta"`, а не Чат-ов `chat.completion.chunk` |
| `400` грешка на улазу слике након миграције | Тип садржаја слике није ажуриран | Променити `"type": "image_url"` → `"type": "input_image"` и исправити `"image_url": {"url": "..."}` → `"image_url": "..."` (обичан низ) |
| Позиви алата се бесконачно понављају | Недостаје резултат алата у следећем `input`-у | Након извршења алата, додати ставка `{"type": "function_call_output", "call_id": ..., "output": ...}` у `input` следећег захтева |
| Грешка `temperature` са GPT-5 или o-серијом | Јасно назначена `temperature` вредност другачија од 1 | Уклонити `temperature` или поставити на `1` за GPT-5 и о-серију моделе (о1, о3-mini, о3, о4-mini) |
| Грешка `top_p` са о-серијом | `top_p` није подржан | Уклонити `top_p` када циљате о-серијске моделе |
| `max_completion_tokens` није признат | Користи се Azure-специфичан параметар | Заменити `max_completion_tokens` са `max_output_tokens`. Поставити на 4096+ за о-серију (рачунају се разуђивачки токени) |
| Празан или скраћен излаз из о-серије | `max_output_tokens` је пренизак | О-серија користи разуђивачке токене. Поставити `max_output_tokens=4096` или више — не 500–1000. |
| `400 integer_below_min_value` за `max_output_tokens` | Вредност испод 16 | Azure OpenAI захтева `max_output_tokens >= 16`. Користити 50+ за брзе тестове, 1000+ за продукцију. |
| `429 Too Many Requests` током стрима | Ограничење брзине од стране Azure OpenAI | Стрим се тихо прекида без обраде грешке. Увек увијати `async for event in await coroutine:` у `try/except` и испоручити `{"error": str(e)}` фронтенду. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Погрешан тенант или није пријављен | Проследити `tenant_id=os.getenv("AZURE_TENANT_ID")` експлицитно. Покренути `azd auth login --tenant <tenant-id>` локално. |
| `404 Not Found` користећи GitHub моделе (`models.github.ai`) | GitHub модели не подржавају Responses API | Уклонити цео код за GitHub моделе. Користити Azure OpenAI, OpenAI или компатибилни локални крај (нпр. Ollama са подршком Responses). |
| MAF `OpenAIChatCompletionClient` још користи Чат Комплитације | Користи стари MAF клијент у 1.0.0+ | У MAF 1.0.0+, `OpenAIChatClient` по дефоулту користи Responses API. Заменити `OpenAIChatCompletionClient` са `OpenAIChatClient`. За верзије пре 1.0.0 ажурирати на `agent-framework-openai>=1.0.0`. |
| LangChain агент враћа празно или неуспех са позивима алата | `ChatOpenAI` не користи Responses API | Додати `use_responses_api=True` у `ChatOpenAI(...)`. Такође променити `.content` → `.text` код одговора порука. |
| `KeyError: 'innererror'` у хендлеру грешке филтера садржаја | Структура тела грешке се променила у Responses API | Пребацити `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror` је уклоњен; детаљи филтера садржаја су сада у горњем нивоу низу `content_filters` са множином `content_filter_results` у сваком уносу. |
| Сирови HTTP позив `/openai/deployments/.../chat/completions` враћа 404 | Стари REST крај Чат Комплитација | Пребацити УРЛ на `/openai/v1/responses`. Променити тело захтева: `messages` → `input`, додати `max_output_tokens` + `store: false`, уклонити „api-version“ query параметар. Променити парсирање одговора: `choices[0].message.content` → `output[0].content[0].text` (напомена: `output_text` је SDK погодност, није у сировом REST JSON). |

---

## Замке

1. Ако сте раније користили Чат Комплитације за стање разговора, сада управљајте сопственим стањем експлицитно са Responses.
2. Преферирајте `max_output_tokens` уместо застарелог `max_tokens`.
3. При миграцији на `gpt-5`, обезбедите да `temperature` није назначен или је постављен на `1`.
4. Замените Чат `content[].type: "text"` са Responses `content[].type: "input_text"` за уносе корисника/система.
5. За `text.format`, доставите правилан речник (нпр. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), не обичан низ.
6. Параметар `seed` није подржан у Responses; уклоните га из захтева.
7. **Расуђивање**: Укључите `reasoning` само ако га је оригинални код већ користио. Немојте додавати `reasoning` у API позиве који га нису имали — многи модели (нпр. gpt-4o-mini) не подржавају овај параметар.
8. **Величина `max_output_tokens`**: За расуђивачке моделе (GPT-5-mini, GPT-5, о-серија), користите `max_output_tokens=4096` или више — не 50–1000. Модел користи разуђивачке токене унутарно пре генерисања видљивог излаза; превише низак лимит доводи до скраћених или празних одговора.
9. **О-серија `max_completion_tokens`**: Ако је оригинални код користио `max_completion_tokens` (Azure-специфично за о-серију), замените са `max_output_tokens`. Responses API не прихвата `max_completion_tokens`.
10. **О-серија `reasoning_effort`**: Ако оригинални код користи `reasoning_effort` (low/medium/high), мигрирајте га у `reasoning={"effort": "<value>"}` у Responses API позиву.
11. **Касњење у стримовању о-серије**: О-серија модели извештавају интерно разуђивање пре него што генеришу излаз. Код стримовања очекујте дужи период пре првог `response.output_text.delta` догађаја. Ово је нормално — модел размишља, није заглављен.
9. **`_azure_ad_token_provider` више не постоји**: `AsyncOpenAI` / `OpenAI` немају атрибут `_azure_ad_token_provider`. Тестови или код који му приступају имаће `AttributeError`. Провајдер токена се прослеђује као `api_key` и није доступан преко клијента.
10. **Снимци / „златне“ датотеке**: Ако тестни скуп користи snapshot тестирање, **све** snapshot датотеке које садрже облике стримовања Чат Комплитација (`choices[0]`, `content_filter_results`, `function_call`, итд.) морају бити ажуриране у нови облик Responses. Ово је лако пропустити и узрокује неуспехе у snapshot проверама.
11. **Путања за mock monkeypatch**: Циљ монкипача се мења са `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (или `Responses.create` за синхрони начин). Коришћење старе путање тихо не ради — mock неће пресрести позиве, а тестови ће користити стварни API или неће успети.
12. **`input`, а не `messages`**: Mock функције морају читати `kwargs.get("input")`, а не `kwargs.get("messages")`. Responses API користи `input` за историју разговора.
13. **Именовање променљивих окружења**: Azure Identity SDK користи `AZURE_CLIENT_ID` (не `AZURE_OPENAI_CLIENT_ID`) за `ManagedIdentityCredential(client_id=...)`. Преименовати у тестовима, `.env` фајловима, подешавањима апликације и Bicep/инфраструктури.
14. **Минимална вредност `max_output_tokens` је 16**: Azure OpenAI одбија вредности испод 16 са `400 integer_below_min_value`. За брзе тестове користити 50, за продукцију 1000+. Стари `max_tokens` није имао такав минимум.
15. **`tenant_id` за `AzureDeveloperCliCredential`**: Када је Azure OpenAI ресурс у другом тенанту, морате проследити `tenant_id` експлицитно — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Без тога, креденцијал тихо користи погрешан тенант и враћа `401`.
16. **Ограничења брзине се појављују другачије у стримовању**: Код Чат Комплитација, 429 је обично спречавао почетак стрима. Код стримовања Responses API-ја, 429 може доћи **усред стрима** — асинхрони итератор баца изузетак. Увек увијати стримовање у `try/except` и слати JSON грешку да фронтенд може изаћи на крај.

17. **Обавезна је обрада грешака у стримингу за веб апликације**: Шаблон `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` је критичан. Без њега, SSE/JSONL стрим тихо прекида рад при било којој грешци на серверу и фронтенд се замрзава.
18. **Дефиниције алата морају бити у равном формату**: Responses API очекује `{"type": "function", "name": ..., "parameters": ...}` — а не угњежђени Chat Completions формат `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Ово је најчешћа грешка при миграцији кода за позив функција.
19. **`pydantic_function_tool()` је некомпатибилан**: Помоћна функција `openai.pydantic_function_tool()` и даље генерише стари угњежђени формат. Немојте је користити са `responses.create()`. Дефинишите шеме алата ручно или спљоштите излаз.
20. **Резултати алата користе `function_call_output`, а не `role: tool`**: Након извршења алата додајте `{"type": "function_call_output", "call_id": ..., "output": ...}` — а не `{"role": "tool", "tool_call_id": ..., "content": ...}`. За захтев асистенту за алат користите `messages.extend(response.output)` — а не ручни речник `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` захтева `required` + `additionalProperties: false`**: Када користите `strict: true` за алат, свака особина мора бити наведена у низу `required`, а `additionalProperties` мора бити `false`. Изостајање било ког понекида узрокује грешку 400.
22. **ИД позива функција има специфичне префиксе**: При пружању неколико `function_call` ставки у `input`, поље `id` мора почети са `fc_` а поље `call_id` са `call_` (нпр. `"id": "fc_example1", "call_id": "call_example1"`). Коришћење старог Chat Completions префикса `call_` за `id` се одбија.
23. **GitHub Models не подржава Responses API**: Ако апликација има GitHub Models код (са `base_url` који показује на `models.github.ai` или `models.inference.ai.azure.com`), уклоните га у потпуности. Не постоји пут миграције — прелазите на Azure OpenAI, OpenAI или компатибилан локални ентпоинт.
24. **Структура тела грешке филтера садржаја се променила**: Грешке Chat Completions су користиле `error.body["innererror"]["content_filter_result"]` (једнина). Грешке Responses API користе `error.body["content_filters"][0]["content_filter_results"]` (множина, у низу). Кључ `innererror` више не постоји. Код који директно приступа `innererror` изазваће `KeyError` током извођења — лако је то пропустити при миграцији јер се појављује само када филтер садржаја заиста активира. Увек претражујте за `innererror` током миграције.
25. **Сирови HTTP позиви захтевају преписивање URL-а и тела**: Апликације које директно позивају Azure OpenAI REST (путем `requests`, `httpx`, `aiohttp`) користећи `/openai/deployments/{name}/chat/completions?api-version=...` морају прелазити на `/openai/v1/responses`. Тело захтева користи `input` уместо `messages`, захтева `max_output_tokens` и `store`, а параметар упита `api-version` се уклања. Текст тела одговора је у `output[0].content[0].text` — **не** у `output_text`, који је згодан својство SDK-а али није присутан у сировом REST JSON-у.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->