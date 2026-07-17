# Решавање проблема, Табела ризика и Замке

## Решавање проблема са 400 грешкама

| Грешка | Поправка |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Дефиниција алата користи стари угнежђени формат за Chat Completions | Реформатирати са `{"type": "function", "function": {"name": ...}}` у `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters иду на највиши ниво |
| `unknown_parameter: input[N].tool_calls` | Резултати више корака алата користе стари формат за Chat Completions | Заменити `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` са ставкама `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` алат нема `required` низ | Када је `strict: true`, све особине морају бити наведене у `required`, а `additionalProperties: false` мора бити подешено |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` алат нема `additionalProperties: false` | Додати `"additionalProperties": false` у објекат параметара |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID за function_call у few-shot има погрешан префикс | ID за function call морају почети са `fc_` (нпр. `fc_example1`), а не са `call_` |
| `missing_required_parameter: text.format.name` | Додати кључ `"name"` у формат речник (нпр. `"name": "Output"`) |
| `invalid_type: text.format` | Осигурати да је `text.format` речник са кључевима `type`, `name`, `strict`, `schema` — не стринг |
| `invalid input content type` | Користити типове садржаја `input_text`/`output_text` уместо Chat `text` |
| `invalid input content type` (слика) | Садржај слике и даље користи `"type": "image_url"` | Променити у `"type": "input_image"` |
| `Expected object, got string` на `image_url` | `image_url` је и даље угнежђени објекат `{"url": "..."}` | Обавити флатенинг у обичан стринг: `"image_url": "https://..."` или `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` за `max_output_tokens` | Минимум је **16** на Azure OpenAI. Користити 50+ за тестове, 1000+ у продукцији. |
| `429 Too Many Requests` током стримовања | Ограничење учесталости позива. Укључити стримовање у `try/except`, враћати JSON са грешком фронтенду, применити backoff/retry. |
| `KeyError: 'innererror'` код грешке филтра садржаја | Структура тела грешке филтра садржаја је промењена у Responses API-ју | Chat Completions је користио `error.body["innererror"]["content_filter_result"]`; Responses API користи `error.body["content_filters"][0]["content_filter_results"]` (у множини, унутар низа). Преписати све приступе `innererror`. |

---

## Табела ризика за миграцију

| Симптом | Веројатна грешка | Поправка |
|---------|---------------|-----|
| Празан `output_text` / скраћен одговор | `max_output_tokens` је превише низак за reasoning моделе | Поставити `max_output_tokens=1000` или више — reasoning токени урачунавају се у лимит |
| `400 invalid_type: text.format` | Прослеђен стринг `response_format` уместо речника `text.format` | Користити `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` на `/openai/v1/responses` | Погрешан `base_url` — недостаје `/openai/v1/` наставак | Осигурати да је `base_url=f"{endpoint}/openai/v1/"` (са завршним овом) |
| `401 Unauthorized` након преласка на `OpenAI()` | `api_key` није подешен или token provider није исправно прослеђен | За EntraID: `api_key=token_provider` (позивни блоб). За API кључ: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Модел враћа `deployment not found` | Праметар `model` не одговара вашем Azure deployment имену | Користити `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — ово је име deployment-а, не модела |
| `json.loads(resp.output_text)` подиже `JSONDecodeError` | Схема није применљена или модел не подржава строги JSON | Осигурати `"strict": True` у схеми, и потврдити да модел подржава структуирани излаз |
| Стримовање не даје `delta` догађаје | Проверава се погрешан тип догађаја | Филтрирати према `event.type == "response.output_text.delta"`, а не Chat-овом `chat.completion.chunk` |
| `400` грешка на сликовном улазу након миграције | Тип садржаја слике није ажуриран | Променити `"type": "image_url"` → `"type": "input_image"` и урадити флатенинг `"image_url": {"url": "..."}` → `"image_url": "..."` (обичан стринг) |
| Позиви алата бесконачно се понављају | Недостаје резултат алата у следећем `input` | Након извршавања алата, додати ставку `{"type": "function_call_output", "call_id": ..., "output": ...}` у `input` наредног захтева |
| Грешка `temperature` са GPT-5 или o-series | Изричита вредност `temperature` другачија од 1 | Уклонити `temperature` или поставити на `1` за GPT-5 и o-series моделе (o1, o3-mini, o3, o4-mini) |
| Грешка `top_p` са o-series | `top_p` није подржан | Уклонити `top_p` када се користе o-series модели |
| `max_completion_tokens` није препознат | Kористи се Azure-специфичан параметар | Заменити `max_completion_tokens` са `max_output_tokens`. Поставити 4096+ за o-series (reasoning токени урачунавати ограничење). |
| Празан или скраћен излаз од o-series | `max_output_tokens` је превише низак | O-series користи reasoning токене унутарње. Поставити `max_output_tokens=4096` или више — не 500–1000. |
| `400 integer_below_min_value` за `max_output_tokens` | Вредност испод 16 | Azure OpenAI захтева да је `max_output_tokens >= 16`. Користити 50+ за тестове, 1000+ у продукцији. |
| `429 Too Many Requests` током стримовања | Ограничење учесталости од стране Azure OpenAI | Стрим се прекида тихо без обраде грешке. Увек укључити `async for event in await coroutine:` у `try/except` и вратити `{"error": str(e)}` фронтенду. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Погрешан тенант или корисник није пријављен | Проследити `tenant_id=os.getenv("AZURE_TENANT_ID")` јасно. Покренути `azd auth login --tenant <tenant-id>` локално. |
| `404 Not Found` користећи GitHub моделе (`models.github.ai`) | GitHub модели не подржавају Responses API | Уклонити у потпуности код путању за GitHub моделе. Користити Azure OpenAI, OpenAI, или компатибилни локални ендпоинт (нпр. Ollama са подршком за Responses). |
| MAF `OpenAIChatCompletionClient` и даље користи Chat Completions | Користи се наследни MAF клијент у 1.0.0+ | У MAF 1.0.0+, `OpenAIChatClient` подразумевано користи Responses API. Заменити `OpenAIChatCompletionClient` са `OpenAIChatClient`. За верзије пре 1.0.0, надоградити на `agent-framework-openai>=1.0.0`. |
| LangChain агент враћа празно или пада са позивима алата | `ChatOpenAI` не користи Responses API | Додати `use_responses_api=True` у `ChatOpenAI(...)`. Такође променити `.content` → `.text` на порукама одговора. |
| `KeyError: 'innererror'` у руковаоцу грешака филтра садржаја | Структура тела грешке је промењена у Responses API-ју | Преписати `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. `innererror` омотач је уклоњен; детаљи филтра садржаја сада су у врхунском низу `content_filters` са `content_filter_results` (у множини) унутар сваког уноса. |
| Сирови HTTP позив на `/openai/deployments/.../chat/completions` враћа 404 | Стари Chat Completions REST endpoint | Преписати URL у `/openai/v1/responses`. Променити тело захтева: са `messages` на `input`, додати `max_output_tokens` + `store: false`, уклонити параметар упита `api-version`. Променити парсирање одговора: `choices[0].message.content` → `output[0].content[0].text` (напомена: `output_text` је погодност SDK-а, није у сировом REST JSON-у). |

---

## Замке

1. Ако сте раније користили Chat Completions за стање разговора, управљајте својим стањем јасно са Responses.
2. Преферирајте `max_output_tokens` уместо наследног `max_tokens`.
3. При миграцији на `gpt-5`, осигурајте да `temperature` није назначен или да је постављен на `1`.
4. Замените Chat `content[].type: "text"` са Responses `content[].type: "input_text"` за уносе корисника/система.
5. За `text.format`, обезбедите ваљан речник (нпр. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), не обичан стринг.
6. Параметар `seed` није подржан у Responses; уклоните га из захтева.
7. **Reasoning**: Укључујте `reasoning` само ако је оригинални код већ користио. Не додајте `reasoning` у API позиве који га нису имали — многи модели без reasoning не подржавају овај параметар.
8. **Величина `max_output_tokens`**: За reasoning моделе (GPT-5-mini, GPT-5, o-series), користите `max_output_tokens=4096` или више — не 50–1000. Модел унутарњо користи reasoning токене пре генерисања видљивог излаза; премали лимити доводе до скраћених или празних одговора.
9. **O-series `max_completion_tokens`**: Ако је оригинални код користио `max_completion_tokens` (Azure-специфично за o-series), замените га са `max_output_tokens`. Responses API не прихвата `max_completion_tokens`.
10. **O-series `reasoning_effort`**: Ако оригинални код користи `reasoning_effort` (low/medium/high), мигрирајте га на `reasoning={"effort": "<value>"}` у Responses API позиву.
11. **O-series кашњење у стримовању**: O-series модели обављају интерно reasoning пре генерисања излаза. При стримовању, очекује се дужи период пре првог `response.output_text.delta` догађаја. Ово је нормално — модел размишља, није заглављен.
9. **`_azure_ad_token_provider` је уклоњен**: `AsyncOpenAI` / `OpenAI` немају атрибут `_azure_ad_token_provider`. Тестови или код који приступају овом атрибуту ће приказати `AttributeError`. Token provider се прослеђује као `api_key` и није видно доступан на клијентском објекту.
10. **Snapshot / "златне" датотеке**: Ако тест скуп користи snapshot тестирање, **све** snapshot датотеке које садрже форме Chat Completions стримовања (`choices[0]`, `content_filter_results`, `function_call` итд.) морају бити ажуриране на нови облик Responses. Ово се лако пропусти и узрокује неуспехе на snapshot асерцијама.
11. **Mock monkeypatch путања**: Таргет за monkeypatch се мења са `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (или `Responses.create` за синхрони позиве). Коришћење старе путање нешто не ради, тј. mock неће пресрећивати, и тестови позивају прави API или падају.
12. **`input` не `messages`**: Mock функције морају читати `kwargs.get("input")`, а не `kwargs.get("messages")`. Responses API користи `input` за историју разговора.
13. **Називе env променљивих**: Azure Identity SDK користи `AZURE_CLIENT_ID` (не `AZURE_OPENAI_CLIENT_ID`) за `ManagedIdentityCredential(client_id=...)`. Промените у тестовима, `.env` датотекама, подешавањима апликације и Bicep/инфраструктури.
14. **Минимум `max_output_tokens` је 16**: Azure OpenAI одбија вредности испод 16 са `400 integer_below_min_value`. Користите 50 за smoke тестове, 1000+ за продукцију. Стари `max_tokens` није имао тај минимум.
15. **`tenant_id` за `AzureDeveloperCliCredential`**: Када је Azure OpenAI ресурс у другом тенанту, морате проследити `tenant_id` јасно — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Без тога, credentials тише користе погрешан тенант и враћају `401`.
16. **Rate limit-и се појављују другачије током стримовања**: Са Chat Completions, 429 је обично спречавао почетак стрима. Са Responses API стримовањем, 429 може се десити **у току стрима** — асинхрони итератор подиже изузетак. Увек обухватите стрим петљу `try/except` и дајте линe са JSON грешком како би фронтенд могао да руководи коректно.

17. **Обавезно руковање грешкама током стримовања за веб апликације**: Образац `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` је кључан. Без њега, SSE/JSONL стрим ћути и умире на било каквој серверској грешци, а фронтенд се замрзава.
18. **Дефиниције алата морају користити раван формат**: Responses API очекује `{"type": "function", "name": ..., "parameters": ...}` — а не угњеждени формат из Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. Ово је најчешћа грешка при миграцији за код који позива функције.
19. **`pydantic_function_tool()` није компатибилан**: Помоћна функција `openai.pydantic_function_tool()` и даље генерише стари угњеждени формат. Немојте је користити са `responses.create()`. Дефинишите шеме алата ручно или спљоштите излаз.
20. **Резултати алата користе `function_call_output`, а не `role: tool`**: Након извршења алата, додајте `{"type": "function_call_output", "call_id": ..., "output": ...}` — а не `{"role": "tool", "tool_call_id": ..., "content": ...}`. За захтев алата од помоћника, користите `messages.extend(response.output)` — а не ручни речник `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` захтева `required` + `additionalProperties: false`**: Када користите `strict: true` на алату, свака особина мора бити наведена у низу `required` и `additionalProperties` мора бити `false`. Недостајање било ког изазива грешку 400.
22. **ID позива функција имају специфичне префиксе**: Када уносите few-shot `function_call` ставке у `input`, поље `id` мора почети са `fc_` а поље `call_id` са `call_` (нпр. `"id": "fc_example1", "call_id": "call_example1"`). Користење старог префикса `call_` за `id` из Chat Completions се одбија.
23. **GitHub Models не подржава Responses API**: Ако апликација има GitHub Models код (са `base_url` који указује на `models.github.ai` или `models.inference.ai.azure.com`), уклоните га у потпуности. Нема пута миграције — пређите на Azure OpenAI, OpenAI или компатибилан локални ендпоинт.
24. **Структура тела грешке content фильтра се променила**: Грешке у Chat Completions су користиле `error.body["innererror"]["content_filter_result"]` (једнина). Грешке Responses API користе `error.body["content_filters"][0]["content_filter_results"]` (множења, унутар низа). Кључ `innererror` више не постоји. Код који директно приступа `innererror` ће избацити `KeyError` током извршавања — ово је лако пропустити при миграцији јер се јавља само када content filter заиста сработи. Увек претражите `innererror` током миграције.
25. **Сироки HTTP позиви захтевају прераду URL-а и тела**: Апликације које директно позивају Azure OpenAI REST (путем `requests`, `httpx`, `aiohttp`) користећи `/openai/deployments/{name}/chat/completions?api-version=...` морају прећи на `/openai/v1/responses`. Тело захтева користи `input` уместо `messages`, захтева `max_output_tokens` и `store`, а `api-version` параметар у упиту се уклања. Текст одговора је у `output[0].content[0].text` — **не** у `output_text`, који је погодност SDK-а а није присутан у сиромашном REST JSON-у.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->