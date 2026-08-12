# Rozwiązywanie problemów, tabela ryzyka i pułapki

## Rozwiązywanie problemów z błędami 400

| Błąd | Naprawa |
|-------|-----|
| `missing_required_parameter: tools[0].name` | Definicja narzędzia używa starego zagnieżdżonego formatu Chat Completions | Spłaszcz z `{"type": "function", "function": {"name": ...}}` do `{"type": "function", "name": ..., "parameters": ...}` — name, description, parameters idą na najwyższy poziom |
| `unknown_parameter: input[N].tool_calls` | Wyniki narzędzia w multi-turn używają starego formatu Chat Completions | Zamień `{"role": "assistant", "tool_calls": [...]}` + `{"role": "tool", ...}` na elementy `response.output` + `{"type": "function_call_output", "call_id": ..., "output": ...}` |
| `invalid_function_parameters: 'required' is required` | `strict: true` w narzędziu nie ma tablicy `required` | Gdy `strict: true`, wszystkie właściwości muszą być wymienione w `required`, a `additionalProperties: false` musi być ustawione |
| `invalid_function_parameters: 'additionalProperties' is required` | `strict: true` w narzędziu nie ma `additionalProperties: false` | Dodaj `"additionalProperties": false` do obiektu parametrów |
| `invalid input[N].id: Expected an ID that begins with 'fc'` | ID funkcji Few-shot ma zły prefiks | ID wywołań funkcji muszą zaczynać się od `fc_` (np. `fc_example1`), a nie `call_` |
| `missing_required_parameter: text.format.name` | Dodaj klucz `"name"` do słownika formatu (np. `"name": "Output"`) |
| `invalid_type: text.format` | Upewnij się, że `text.format` jest słownikiem z kluczami `type`, `name`, `strict`, `schema` — nie ciągiem znaków |
| `invalid input content type` | Użyj typów zawartości `input_text`/`output_text` zamiast Chatowego `text` |
| `invalid input content type` (obraz) | Zawartość obrazu nadal używa `"type": "image_url"` | Zmień na `"type": "input_image"` |
| `Expected object, got string` w `image_url` | `image_url` nadal jest zagnieżdżonym obiektem `{"url": "..."}` | Spłaszcz do prostego ciągu: `"image_url": "https://..."` lub `"image_url": "data:image/...;base64,..."` |
| `integer below minimum value` dla `max_output_tokens` | Minimum to **16** na Azure OpenAI. Do testów używaj 50+, do produkcji 1000+. |
| `429 Too Many Requests` podczas streamingu | Ograniczenie częstości żądań. Otocz streaming `try/except`, zwracaj JSON z błędem do frontendu, zaimplementuj backoff/retry. |
| `KeyError: 'innererror'` podczas błędu filtru treści | Struktura błędu filtru treści zmieniła się w Responses API | Chat Completions używało `error.body["innererror"]["content_filter_result"]`; Responses API używa `error.body["content_filters"][0]["content_filter_results"]` (w liczbie mnogiej, w tablicy). Przepisać wszystkie dostępy `innererror`. |

---

## Tabela ryzyka migracji

| Symptomy | Prawdopodobny błąd | Naprawa |
|---------|---------------|-----|
| Pusty `output_text` / ucięta odpowiedź | `max_output_tokens` za niskie dla modeli rozumujących | Ustaw `max_output_tokens=1000` lub więcej — tokeny rozumowania są wliczane do limitu |
| `400 invalid_type: text.format` | Przekazano ciąg `response_format` zamiast słownika `text.format` | Użyj `text={"format": {"type": "json_schema", "name": "...", "strict": True, "schema": {...}}}` |
| `404 Not Found` na `/openai/v1/responses` | Błędny `base_url` — brak końcówki `/openai/v1/` | Upewnij się, że `base_url=f"{endpoint}/openai/v1/"` (z ukośnikiem na końcu) |
| `401 Unauthorized` po przełączeniu na `OpenAI()` | `api_key` nie ustawiony lub dostawca tokenów przekazany nieprawidłowo | Dla EntraID: `api_key=token_provider` (wywoływalne). Dla klucza API: `api_key=os.environ["AZURE_OPENAI_API_KEY"]` |
| Model zwraca `deployment not found` | Parametr `model` nie pasuje do twojej nazwy wdrożenia Azure | Użyj `model=os.environ["AZURE_OPENAI_DEPLOYMENT"]` — to jest nazwa wdrożenia, nie nazwa modelu |
| `json.loads(resp.output_text)` rzuca `JSONDecodeError` | Schemat nie jest wymuszony lub model nie obsługuje ścisłego JSON | Upewnij się, że `"strict": True` w schemacie i zweryfikuj, czy model wspiera wyjście ustrukturyzowane |
| Streaming nie generuje zdarzeń `delta` | Sprawdzanie niewłaściwego typu zdarzenia | Filtruj na `event.type == "response.output_text.delta"`, nie na Chat `chat.completion.chunk` |
| Błąd 400 na wejściu obrazu po migracji | Nie zaktualizowano typu zawartości obrazu | Zmień `"type": "image_url"` → `"type": "input_image"` i spłaszcz `"image_url": {"url": "..."}` → `"image_url": "..."` (prosty ciąg) |
| Wywołania narzędzi w pętli nieskończonej | Brak wyniku narzędzia w następnym `input` | Po wykonaniu narzędzia dodaj element `{"type": "function_call_output", "call_id": ..., "output": ...}` do `input` w następnym zapytaniu |
| Błąd `temperature` z GPT-5 lub o-series | Jawna wartość `temperature` inna niż 1 | Usuń `temperature` lub ustaw na `1` dla GPT-5 i modeli z serii o (o1, o3-mini, o3, o4-mini) |
| Błąd `top_p` z serią o | `top_p` nie jest obsługiwane | Usuń `top_p`, gdy celujesz w modele z serii o |
| `max_completion_tokens` nieznany | Używany parametr specyficzny dla Azure | Zamień `max_completion_tokens` na `max_output_tokens`. Ustaw na 4096+ dla serii o (tokeny rozumowania wliczane do limitu). |
| Pusty/ucięty output z serii o | `max_output_tokens` za niskie | Seria o używa tokenów rozumowania wewnętrznie. Ustaw `max_output_tokens=4096` lub więcej — nie 500–1000. |
| `400 integer_below_min_value` dla `max_output_tokens` | Wartość poniżej 16 | Azure OpenAI wymusza `max_output_tokens >= 16`. Używaj 50+ do testów, 1000+ do produkcji. |
| `429 Too Many Requests` w trakcie streamu | Ograniczenie częstości przez Azure OpenAI | Stream przerywa się bez błędu. Zawszę otaczaj `async for event in await coroutine:` blokiem `try/except` i przekazuj `{"error": str(e)}` do frontend. |
| `AzureDeveloperCliCredential` → `CredentialUnavailableError` | Zły tenant lub brak zalogowania | Przekaż `tenant_id=os.getenv("AZURE_TENANT_ID")` jawnie. Uruchom lokalnie `azd auth login --tenant <tenant-id>`. |
| `404 Not Found` używając modeli GitHub (`models.github.ai`) | Modele GitHub nie obsługują Responses API | Usuń całkowicie ścieżkę kodu dla modeli GitHub. Używaj Azure OpenAI, OpenAI lub kompatybilnego lokalnego endpointu (np. Ollama z obsługą Responses). |
| MAF `OpenAIChatCompletionClient` nadal używa Chat Completions | Używasz klienta MAF legacy w wersji 1.0.0+ | W MAF 1.0.0+ `OpenAIChatClient` domyślnie korzysta z Responses API. Zamień `OpenAIChatCompletionClient` na `OpenAIChatClient`. Przy wersjach przed 1.0.0, zaktualizuj do `agent-framework-openai>=1.0.0`. |
| Agent LangChain zwraca pusty wynik lub wywala się przy wywołaniach narzędzi | `ChatOpenAI` nie używa Responses API | Dodaj `use_responses_api=True` do `ChatOpenAI(...)`. Zmień też `.content` → `.text` w wiadomościach odpowiedzi. |
| `KeyError: 'innererror'` w handlerze błędu filtru treści | Struktura błędu zmieniła się w Responses API | Przepisać `error.body["innererror"]["content_filter_result"]["jailbreak"]` → `error.body["content_filters"][0]["content_filter_results"]["jailbreak"]`. Wrapper `innererror` zniknął; szczegóły filtru są teraz w tablicy `content_filters` na najwyższym poziomie, z `content_filter_results` (w liczbie mnogiej) w każdym elemencie. |
| Surowe wywołanie HTTP do `/openai/deployments/.../chat/completions` zwraca 404 | Stary endpoint REST Chat Completions | Przepisać URL na `/openai/v1/responses`. Zmienić ciało zapytania: `messages` → `input`, dodać `max_output_tokens` + `store: false`, usunąć parametr zapytania `api-version`. Zmienić parsowanie odpowiedzi: `choices[0].message.content` → `output[0].content[0].text` (uwaga: `output_text` to właściwość ułatwiająca korzystanie w SDK, nie jest w surowym JSON REST). |

---

## Pułapki

1. Jeśli wcześniej używałeś Chat Completions do stanu konwersacji, zarządzaj własnym stanem jawnie z Responses.
2. Preferuj `max_output_tokens` zamiast starego `max_tokens`.
3. Przy migracji na `gpt-5` upewnij się, że `temperature` nie jest podane lub jest ustawione na `1`.
4. Zamień Chatowe `content[].type: "text"` na Responses `content[].type: "input_text"` dla wejść użytkownika/systemu.
5. Dla `text.format` podaj właściwy słownik (np. `{"type": "json_schema", "name": "Output", "schema": ..., "strict": True}`), a nie zwykły ciąg znaków.
6. Parametr `seed` nie jest wspierany w Responses; usuń go z zapytań.
7. **Reasoning**: Uwzględniaj `reasoning` tylko jeśli oryginalny kod już go używał. Nie dodawaj `reasoning` do wywołań API, które go nie miały — wiele modeli nierozumujących tego nie obsługuje.
8. **Rozmiar `max_output_tokens`**: Dla modeli rozumujących (GPT-5-mini, GPT-5, seria o) używaj `max_output_tokens=4096` lub więcej — nie 50–1000. Model na wejściu używa tokenów rozumowania zanim wygeneruje widoczny output; zbyt niskie limity powodują ucięte lub puste odpowiedzi.
9. **`max_completion_tokens` w serii o**: Jeśli oryginalny kod używał `max_completion_tokens` (specyficzne dla Azure dla serii o), zamień na `max_output_tokens`. Responses API nie akceptuje `max_completion_tokens`.
10. **`reasoning_effort` w serii o**: Jeśli oryginalny kod używa `reasoning_effort` (low/medium/high), migruj do `reasoning={"effort": "<value>"}` w wywołaniu Responses API.
11. **Opóźnienie streamingu w serii o**: Modele serii o wykonują rozumowanie wewnętrznie przed generowaniem outputu. Przy streamingu spodziewaj się dłuższego opóźnienia przed pierwszym zdarzeniem `response.output_text.delta`. To normalne — model rozumuje, a nie zawiesił się.
9. **`_azure_ad_token_provider` zniknął**: `AsyncOpenAI` / `OpenAI` nie mają atrybutu `_azure_ad_token_provider`. Testy lub kod odwołujący się do tego atrybutu zakończą się `AttributeError`. Dostawca tokenów jest przekazywany jako `api_key` i nie jest dostępny do inspekcji w obiekcie klienta.
10. **Pliki snapshot/golden**: Jeśli zestaw testów używa snapshotów, **wszystkie** pliki snapshot zawierające kształty streamingu Chat Completions (`choices[0]`, `content_filter_results`, `function_call` itd.) muszą zostać zaktualizowane do nowego kształtu Responses. To łatwo przeoczyć i powoduje błędy asercji w snapshotach.
11. **Ścieżka monkeypatch do mocków**: Cel monkeypatch zmienił się z `openai.resources.chat.AsyncCompletions.create` → `openai.resources.responses.AsyncResponses.create` (lub `Responses.create` dla wersji synchronicznej). Użycie starej ścieżki nie robi nic cicho — mock nie przechwyci wywołań, testy uderzą w prawdziwe API lub się zepsują.
12. **`input`, nie `messages`**: Funkcje mock muszą czytać `kwargs.get("input")` a nie `kwargs.get("messages")`. Responses API używa `input` jako historii konwersacji.
13. **Nazwa zmiennej środowiskowej**: Azure Identity SDK używa `AZURE_CLIENT_ID` (nie `AZURE_OPENAI_CLIENT_ID`) dla `ManagedIdentityCredential(client_id=...)`. Zmień nazwę w testach, plikach `.env`, ustawieniach aplikacji i Bicep/infrastrukturze.
14. **Minimalne `max_output_tokens` to 16**: Azure OpenAI odrzuca wartości poniżej 16 z błędem `400 integer_below_min_value`. Używaj 50 do testów dymnych, 1000+ do produkcji. Stary `max_tokens` nie miał takiego minimum.
15. **`tenant_id` dla `AzureDeveloperCliCredential`**: Gdy zasób Azure OpenAI jest w innym tenancie, **musisz** jawnie podać `tenant_id` — `AzureDeveloperCliCredential(tenant_id=os.getenv("AZURE_TENANT_ID"))`. Bez tego poświadczenie użyje cichego złego tenant i zwróci `401`.
16. **Limity częstości występują inaczej w streamingu**: Z Chat Completions 429 zwykle blokował start streamu. W streamingu Responses API 429 może nastąpić **w trakcie streamu** — iterator async rzuca wyjątek. Zawsze otaczaj pętlę streamingu w `try/except` i zwracaj linię JSON z błędem, aby frontend mógł ją łagodnie obsłużyć.

17. **Obsługa błędów streamingu jest obowiązkowa dla aplikacji internetowych**: Wzorzec `try: async for event in await coroutine: ... except Exception as e: yield json.dumps({"error": str(e)})` jest kluczowy. Bez niego strumień SSE/JSONL cicho umiera przy jakimkolwiek błędzie po stronie serwera, a frontend zawiesza się.
18. **Definicje narzędzi muszą używać płaskiego formatu**: API Responses oczekuje `{"type": "function", "name": ..., "parameters": ...}` — a nie zagnieżdżonego formatu Chat Completions `{"type": "function", "function": {"name": ..., "parameters": ...}}`. To najczęstszy błąd migracji w kodzie wywołującym funkcje.
19. **`pydantic_function_tool()` jest niekompatybilny**: Pomocnik `openai.pydantic_function_tool()` wciąż generuje stary zagnieżdżony format. Nie używaj go z `responses.create()`. Definiuj schematy narzędzi ręcznie lub spłaszczaj wynik.
20. **Wyniki narzędzi używają `function_call_output`, a nie `role: tool`**: Po wykonaniu narzędzia dołącz `{"type": "function_call_output", "call_id": ..., "output": ...}` — a nie `{"role": "tool", "tool_call_id": ..., "content": ...}`. Dla zapytania o narzędzie asystenta użyj `messages.extend(response.output)` — a nie ręcznego słownika `{"role": "assistant", "tool_calls": [...]}`.
21. **`strict: true` wymaga `required` + `additionalProperties: false`**: Korzystając z `strict: true` na narzędziu, każda właściwość musi być wymieniona w tablicy `required`, a `additionalProperties` musi być `false`. Brak któregoś z tych powoduje błąd 400.
22. **Identyfikatory wywołań funkcji mają określone prefiksy**: Podając elementy `function_call` w stylu few-shot w `input`, pole `id` musi zaczynać się od `fc_`, a pole `call_id` od `call_` (np. `"id": "fc_example1", "call_id": "call_example1"`). Użycie starego prefiksu Chat Completions `call_` dla `id` jest odrzucane.
23. **GitHub Models nie obsługuje Responses API**: Jeśli aplikacja ma ścieżkę kodu GitHub Models (`base_url` wskazuje na `models.github.ai` lub `models.inference.ai.azure.com`), usuń ją całkowicie. Nie ma ścieżki migracji — przełącz się na Azure OpenAI, OpenAI lub zgodny lokalny endpoint.
24. **Struktura ciała błędu filtra treści się zmieniła**: Błędy Chat Completions używały `error.body["innererror"]["content_filter_result"]` (pojedyńcze). Błędy Responses API używają `error.body["content_filters"][0]["content_filter_results"]` (liczba mnoga, w tablicy). Klucz `innererror` już nie istnieje. Kod bezpośrednio odwołujący się do `innererror` rzuci `KeyError` w czasie wykonywania — łatwo to przeoczyć podczas migracji, ponieważ pojawia się tylko gdy filtr treści faktycznie się uruchomi. Zawsze przeszukuj `innererror` podczas migracji.
25. **Surowe wywołania HTTP wymagają przepisywania URL i ciała**: Aplikacje wywołujące Azure OpenAI REST bezpośrednio (poprzez `requests`, `httpx`, `aiohttp`) używające `/openai/deployments/{name}/chat/completions?api-version=...` muszą przełączyć się na `/openai/v1/responses`. Ciało żądania używa `input` zamiast `messages`, wymaga `max_output_tokens` i `store`, a parametr zapytania `api-version` jest usunięty. Tekst odpowiedzi znajduje się pod `output[0].content[0].text` — **nie** `output_text`, które jest właściwością wygodną SDK, nieobecną w surowym JSON REST.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->