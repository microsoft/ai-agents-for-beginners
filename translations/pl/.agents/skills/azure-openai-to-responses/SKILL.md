---
name: azure-openai-to-responses
license: MIT
---
# Migracja aplikacji Python z Azure OpenAI Chat Completions do Responses API

> **AUTORYTATYWNE WSKAZÓWKI — POSTĘPUJ ZGODNIE Z NIMI**
>
> Ten zestaw umiejętności migruje kod Python używający Azure OpenAI Chat Completions
> do zunifikowanego Responses API. Postępuj zgodnie z tymi instrukcjami dokładnie.
> Nie wymyślaj mapowania parametrów ani nowych kształtów API.

---

## Wyzwalacze

Aktywuj tę umiejętność, gdy użytkownik chce:
- Migrować aplikację Python z Azure OpenAI Chat Completions do Responses API
- Zaktualizować użycie Python OpenAI SDK do najnowszego kształtu API dla Azure OpenAI
- Przygotować kod Python dla modeli GPT-5 lub nowszych, które wymagają Responses na Azure
- Przełączyć się z `AzureOpenAI`/`AsyncAzureOpenAI` na standardowy klient `OpenAI`/`AsyncOpenAI` z endpointem v1
- Naprawić ostrzeżenia o wycofaniu związane z konstruktorami `AzureOpenAI` lub `api_version`

---

## ⚠️ Zgodność modeli — SPRAWDŹ NAJPIERW

> **Przed migracją zweryfikuj, czy Twoje wdrożenie Azure OpenAI obsługuje Responses API.**

### 1. Test dymny wdrożenia (najszybszy)

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

> **Uwaga**: `max_output_tokens` ma **minimum 16** na Azure OpenAI. Wartości poniżej 16 zwracają błąd 400. Używaj 50+ do testów dymnych.

Jeśli zwraca 404, model wdrożenia jeszcze nie obsługuje Responses — sprawdź poniższe odniesienia lub ponownie wdroż model obsługujący.

### 2. Sprawdź dostępne modele w twoim regionie (zalecane)

Uruchom wbudowane narzędzie zgodności modeli, aby zobaczyć, co jest dostępne z wsparciem Responses API w twoim regionie:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

To zapytanie bezpośrednio do Azure ARM i pokazuje macierz zgodności — które modele wspierają Responses, zorganizowany output, narzędzia itp. Użyj `--filter gpt-5.1,gpt-5.2` do zawężenia wyników lub `--json` dla skryptów.

### 3. Pełne odniesienie wsparcia modeli

- **Zapytanie na żywo**: `python migrate.py models` (patrz wyżej — specyficzne dla regionu, zawsze aktualne)
- **Przegląd dostępności**: [Tabela podsumowania modeli i dostępność w regionach](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Szybki start i wskazówki**: **https://aka.ms/openai/start**

### ⚠️ Ograniczenia starszych modeli

> **OSTRZEŻENIE**: Starsze modele (te wcześniejsze niż `gpt-4.1`) mogą nie wspierać w pełni wszystkich funkcji Responses API.
>
> Znane ograniczenia starszych modeli:
> - **parametr `reasoning`**: Nieobsługiwany w wielu modelach bez reasoning. Migruj `reasoning` tylko jeśli był już w oryginalnym kodzie.
> - **parametr `seed`**: W Responses API w ogóle nie jest wspierany — usuń ze wszystkich zapytań.
> - **Zorganizowany output za pomocą `text.format`**: Starsze modele mogą nie wymuszać schematów JSON z `strict: true` wiarygodnie.
> - **Orkiestracja narzędzi**: GPT-5+ orkiestruje wywołania narzędzi w ramach wewnętrznego reasoning. Starsze modele na Responses działają, ale bez tej głębokiej integracji.
> - **Ograniczenia temperatury**: Przy migracji do `gpt-5` temperatura musi być pominięta lub ustawiona na `1`. Starsze modele tego ograniczenia nie mają.

### Modele reasoning serii O (o1, o3-mini, o3, o4-mini)

Modele serii O mają unikalne ograniczenia parametrów. Przy migracji aplikacji celujących w modele serii O:

- **`temperature`**: Musi być `1` (lub pominięte). Modele serii O nie akceptują innych wartości.
- **`max_completion_tokens` → `max_output_tokens`**: Aplikacje używające Azure-specyficznego `max_completion_tokens` muszą przełączyć się na `max_output_tokens`. Ustaw wysokie wartości (4096+), ponieważ tokeny reasoning liczą się do limitu.
- **`reasoning_effort`**: Jeśli aplikacja używa `reasoning_effort` (low/medium/high), zachowaj go — Responses API wspiera ten parametr dla modeli serii O.
- **Zachowanie streamingu**: Modele serii O mogą buforować output do zakończenia reasoning przed emitowaniem zdarzeń tekstowych delta. Streaming działa, ale pierwszy `response.output_text.delta` może przyjść z większym opóźnieniem niż w modelach GPT.
- **`top_p`**: Nieobsługiwany na serii O — usuń jeśli obecny.
- **Użycie narzędzi**: Modele serii O wspierają narzędzia przez Responses API jak modele GPT, ale jakość orkiestracji wywołań narzędzi różni się w zależności od modelu.

**Działanie — proaktywna porada modelowa**: Podczas fazy skanu sprawdź, który model aplikacja celuje (nazwy wdrożeń, zmienne środowiskowe, konfig). Jeśli model jest wcześniejszy niż `gpt-4.1` (nie gpt-4.1+), poinformuj użytkownika proaktywnie:
- Migracja będzie działać dla podstawowego tekstu, czatu, streamingu i narzędzi na ich obecnym modelu.
- Nowe modele (`gpt-5.1`, `gpt-5.2`) oferują lepszą orkiestrację narzędzi, wymuszanie zorganizowanego outputu, reasoning i dostępność międzyregionową.
- Powinni rozważyć aktualizację wdrożenia, gdy będą gotowi — nie blokuje to migracji.

Nie blokuj ani nie odmawiaj migracji ze względu na wersję modelu. Porada ma charakter informacyjny.

### GitHub Models NIE obsługuje Responses API

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) nie obsługuje Responses API.**

Jeśli kod zawiera ścieżkę kodu GitHub Models (szukaj `base_url` wskazującego na `models.github.ai` lub `models.inference.ai.azure.com`), **usuń ją całkowicie** podczas migracji. Responses API wymaga Azure OpenAI, OpenAI lub kompatybilnego lokalnego endpointu (np. Ollama z obsługą Responses).

Działanie podczas skanu:
- Oznacz każdą ścieżkę kodu GitHub Models do usunięcia.

---

## Migracja frameworków

Wiele aplikacji używa wyższych warstw frameworków na OpenAI. Podczas migracji tych frameworków zmienia się ich własne API — nie tylko wywołania OpenAI w tle.

### Microsoft Agent Framework (MAF)

**Sprawdź najpierw swoją wersję MAF** — migracja zależy od tego, czy masz MAF 1.0.0+ czy wersje beta/rc przed 1.0.0.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` **już używa Responses API** — migracja nie jest potrzebna. Jeśli kod używa legacy `OpenAIChatCompletionClient` (używającego `chat.completions.create`), zastąp go `OpenAIChatClient`.

| Przed | Po |
|--------|-----|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Aby sprawdzić wersję: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (wersje beta/rc)

W pre-1.0.0 MAF `OpenAIChatClient` używał Chat Completions. Zaktualizuj do `agent-framework-openai>=1.0.0` gdzie `OpenAIChatClient` domyślnie używa Responses API.

Inne zmiany nie są potrzebne — API `Agent` i narzędzi pozostają takie same.

### LangChain (`langchain-openai`)

Dodaj `use_responses_api=True` do `ChatOpenAI()`. Aktualizuj dostęp do odpowiedzi z `.content` na `.text`.

| Przed | Po |
|--------|-----|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Pełne przykłady kodu przed/po znajdziesz w [cheat-sheet.md](./references/cheat-sheet.md).

---

## Wskazówki dotyczące migracji frontendów

> **Responses API to kwestia serwerowa.** Migruj backend w Pythonie; kontrakt HTTP frontendu powinien pozostać niezmieniony o ile backend nie jest cienką warstwą przejściową — wtedy rozważ adaptację kształtu zapytań Responses, aby wyeliminować warstwę tłumaczenia. Jeśli frontend wywołuje OpenAI bezpośrednio z kluczem klienta, przenieś te wywołania najpierw do backendu.

### Deprecacja `@microsoft/ai-chat-protocol`

Pakiet npm `@microsoft/ai-chat-protocol` jest przestarzały i powinien zostać zastąpiony przez [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream). Jeśli masz go na froncie:

1. Zamień tag skryptu CDN:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Usuń instancjonowanie `AIChatProtocolClient` (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Zamień `client.getStreamedCompletion(messages)` na bezpośrednie wywołanie `fetch()` do endpointu backendowego ze streamingiem.
4. Zamień `for await (const response of result)` na `for await (const chunk of readNDJSONStream(response.body))`.
5. Aktualizuj dostęp do właściwości z `response.delta.content` / `response.error` na `chunk.delta.content` / `chunk.error`.

---

## Cele

- Wypisz wszystkie miejsca wywołań w Pythonie używające Chat Completions lub legacy Completions z Azure OpenAI.
- Zaproponuj plan migracji i kolejność dla bazy kodu Python.
- Wykonaj bezpieczne, minimalne poprawki do przełączenia na Responses API.
- Zaktualizuj wywołania do konsumowania schematu outputu Responses; brak warstw kompatybilności.
- Uruchom testy/analizę statyczną; napraw drobne błędy spowodowane migracją.
- Przygotuj małe, możliwe do review zestawy zmian i podaj końcowe podsumowanie z różnicami (nie zatwierdzaj).

---

## Zasady ochronne

- Modyfikuj tylko pliki w workspace git. Nigdy nie zapisuj na zewnątrz.
- Nie zachowuj kompatybilności wstecznej; migruj kod do nowego kształtu API.
- Nie zostawiaj komentarzy przejściowych ani kopii zapasowych.
- Zachowaj semantykę streamingu, jeśli była używana; inaczej użyj wariantu bez streamingu.
- W trybie zatwierdzania żądaj aprobaty przed uruchomieniem poleceń lub połączeń sieciowych.
- Nie wykonuj `git add`/`git commit`/`git push`; prodkuj tylko zmiany w working-tree.

---

## Krok 0: Migracja klienta Azure OpenAI (wymaganie wstępne)

Jeśli kod używa konstruktorów `AzureOpenAI` lub `AsyncAzureOpenAI`, najpierw migruj do standardowych konstruktorów `OpenAI` / `AsyncOpenAI`. Konstruktorzy specyficzni dla Azure są wycofani w `openai>=1.108.1`.

### Dlaczego ścieżka API v1?

Nowy endpoint `/openai/v1` używa standardowego klienta `OpenAI()` zamiast `AzureOpenAI()`, nie wymaga parametru `api_version` i działa identycznie na OpenAI i Azure OpenAI. Ten sam klient jest przyszłościowy — nie wymaga zarządzania wersjami.

### Kluczowe zmiany

| Przed | Po |
|--------|-----|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Usuń całkowicie |

### Lista kontrolna sprzątania

- Usuń argument `api_version` z konstrukcji klienta.
- Usuń zmienne środowiskowe `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` z `.env`, ustawień aplikacji i plików Bicep/infrastruktury.
- Zmień nazwę `AZURE_OPENAI_CLIENT_ID` → `AZURE_CLIENT_ID` w `.env`, ustawieniach, Bicep/infra i fixture testowych (standardowa konwencja SDK Azure Identity).
- Upewnij się, że `openai>=1.108.1` jest w `requirements.txt` lub `pyproject.toml`.

### Migracja zmiennych środowiskowych

| Stara zmienna env | Działanie | Uwagi |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Usuń** | Nie potrzebny `api_version` z endpointem v1 |
| `AZURE_OPENAI_API_VERSION` | **Usuń** | To samo co powyżej |
| `AZURE_OPENAI_CLIENT_ID` | **Zmień nazwę** → `AZURE_CLIENT_ID` | Standardowa konwencja SDK Azure Identity dla `ManagedIdentityCredential(client_id=...)` |
| `AZURE_OPENAI_ENDPOINT` | **Zachowaj** | Nadal potrzebny do budowy `base_url` |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Zachowaj** | Używany jako parametr `model` w `responses.create` |
| `AZURE_OPENAI_API_KEY` | **Zachowaj** | Używany jako `api_key` do uwierzytelniania kluczem |

Przykłady konfiguracji klienta (sync, async, EntraID, klucz API, multi-tenant) znajdziesz w [cheat-sheet.md](./references/cheat-sheet.md).

---

## Krok 1: Wykrywanie miejsc wywołań legacy

Uruchom skrypt [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py), aby znaleźć wszystkie miejsca wywołań wymagające migracji:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Lub wyszukaj ręcznie — każdy traf jest celem migracji:

```bash
# Dziedziczne wywołania API (należy przepisać)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Przestarzałe konstruktory klienta Azure (należy zastąpić)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Wzorce dostępu do struktury odpowiedzi (należy zaktualizować)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Definicje narzędzi w starej zagnieżdżonej formie (należy spłaszczyć)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Wyniki narzędzi w starym formacie (należy przekonwertować na function_call_output)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Przestarzałe parametry (należy usunąć lub zmienić nazwę)
rg "response_format"
rg "max_tokens\b"        # zmień nazwę na max_output_tokens
rg "['\"]seed['\"]"      # remove entirely

# Przestarzałe zmienne środowiskowe (posprzątać)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # powinno być AZURE_CLIENT_ID

# Punkty końcowe modeli GitHub (należy usunąć — API odpowiedzi nie jest wspierane)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Dziedziczne wzorce na poziomie frameworka (należy zaktualizować)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: zastąp OpenAIChatClient
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: wymaga use_responses_api=True

# Infrastruktura testowa (należy zaktualizować)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Dostęp do ciała błędu filtra treści (należy zaktualizować — zmieniona struktura)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # stara forma pojedyncza — teraz content_filter_results (liczba mnoga) wewnątrz tablicy content_filters

# Surowe wywołania HTTP do punktu końcowego Chat Completions (należy zaktualizować URL)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heurystyki (wykrywanie i przepisywanie)

- **Klient Chat Completions**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Konstruktory klienta Azure**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Narzędzia**: konwertuj definicje narzędzi do wywołania funkcji z formatu zagnieżdżonego (`{"type": "function", "function": {"name": ...}}`) na płaski format Responses (`{"type": "function", "name": ...}`); używaj `tool_choice`; zwracaj wyniki narzędzi jako elementy `{"type": "function_call_output", "call_id": ..., "output": ...}` (nie jako `{"role": "tool", ...}`).
- **Obrót narzędzi**: gdy model zwraca wywołania funkcji, dopisuj elementy `response.output` do konwersacji (nie ręcznie słownik `{"role": "assistant", "tool_calls": [...]}`), następnie dopisuj elementy `function_call_output` dla każdego wyniku.
- **Przykłady wielu wywołań narzędzi**: jeśli konwersacja zawiera na stałe zakodowane przykłady wywołań narzędzi, konwertuj je na elementy `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}`. Identyfikatory muszą zaczynać się od `fc_`.
- **`pydantic_function_tool()`**: ten helper nadal generuje stary format zagnieżdżony i jest **niekompatybilny** z `responses.create()`. Zastąp go ręcznymi definicjami narzędzi lub opakowaniem spłaszczającym.
- **Wielokrotne tury**: utrzymuj historię konwersacji w aplikacji; przekazuj poprzednie tury przez elementy `input`.
- **Formatowanie**: zamień górnopoziomowy `response_format` w Chat na `text.format` w Responses. Kanoniczny kształt: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Elementy treści**: zamień Chat `content[].type: "text"` na Responses `content[].type: "input_text"` dla tur użytkownika/systemu.
- **Elementy treści obrazów**: zamień Chat `content[].type: "image_url"` na Responses `content[].type: "input_image"`. Pole `image_url` zmienia się z obiektu zagnieżdżonego `{"url": "..."}` na pusty string. Zobacz ściągę dla przykładów przed/po.
- **Wysiłek rozumowania**: **migracja `reasoning` tylko jeśli już jest w oryginalnym kodzie**.
- **Obsługa błędów filtru treści**: struktura błędu uległa zmianie. Chat Completions używało `error.body["innererror"]["content_filter_result"]` (pojedyncze); Responses API używa `error.body["content_filters"][0]["content_filter_results"]` (liczne, w tablicy). Kod odwołujący się do `innererror` zgłosi `KeyError`. Przeredaguj, by używać nowej ścieżki.
- **Surowe wywołania HTTP**: jeśli aplikacja wywołuje Azure OpenAI REST API bezpośrednio (przez `requests`, `httpx` itd.) używając `/openai/deployments/{name}/chat/completions?api-version=...`, zmień na `/openai/v1/responses`. Treść żądania zmienia się: `messages` → `input`, dodaj `max_output_tokens` i `store: false`, usuń parametr `api-version`. Treść odpowiedzi zmienia się: `choices[0].message.content` → `output[0].content[0].text` (uwaga: `output_text` to właściwość ułatwiająca w SDK, nieobecna w surowym JSON REST).

---

## Krok 2: Zastosuj migrację

### Notatki migracyjne (Chat Completions → Responses)

- **Dlaczego migrować**: Responses to zunifikowane API dla tekstu, narzędzi i streamingu; Chat Completions jest przestarzałe. Od GPT-5 wymagane jest korzystanie z Responses dla najlepszej wydajności.
- **HTTP**: punkt końcowy Azure zmienia się z `/openai/deployments/{name}/chat/completions` na `/openai/v1/responses`.
- **Pola**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` bez zmian.
- **Formatowanie**: `response_format` → `text.format` z odpowiednim obiektem.
- **Elementy treści**: zamień Chat `content[].type: "text"` na Responses `content[].type: "input_text"` dla tur systemu/użytkownika.
- **Elementy treści obrazów**: zamień Chat `content[].type: "image_url"` na Responses `content[].type: "input_image"`. Spłaszcz pole `image_url` z `{"image_url": {"url": "..."}}` na `{"image_url": "..."}` (zwykły string — URL HTTPS lub URI `data:image/...;base64,...`).

### Odniesienie mapowania parametrów

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (tablica elementów) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (obiekt) |
| `temperature` | `temperature` (bez zmian) |
| `stop` | `stop` (bez zmian) |
| `frequency_penalty` | `frequency_penalty` (bez zmian) |
| `presence_penalty` | `presence_penalty` (bez zmian) |
| `tools` / wywołanie funkcji | `tools` (bez zmian) |
| `seed` | **Usuń** (nieobsługiwane) |
| `store` | `store` (ustaw na `false`) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (płaski string) |

Pełne przykłady kodu przed/po znajdziesz w [cheat-sheet.md](./references/cheat-sheet.md).

Dla migracji infrastruktury testowej (mocks, snapshots, asercje), zobacz [test-migration.md](./references/test-migration.md).

Dla rozwiązywania problemów i pułapek, zobacz [troubleshooting.md](./references/troubleshooting.md).

---

## Przechowywanie danych i stan

- Ustaw `store: false` we wszystkich żądaniach Responses.
- Nie polegaj na poprzednich ID wiadomości ani na kontekście przechowywanym na serwerze; zarządzaj stanem po stronie klienta i minimalizuj metadane.

---

## Kryteria akceptacji

### Bramy na poziomie kodu (wszystkie muszą przejść)

- [ ] Brak trafień dla `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` w zmigrowanych plikach.
- [ ] Brak trafień dla `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` — wszystkie konstruktory używają `OpenAI`/`AsyncOpenAI` z punktem końcowym v1.
- [ ] Brak trafień dla `rg "models\.github\.ai|models\.inference\.ai\.azure"` — ścieżki kodu GitHub Models usunięte.
- [ ] Brak trafień dla `rg "OpenAIChatCompletionClient"` — kod MAF 1.0.0+ używa `OpenAIChatClient` (który korzysta z Responses API). W wersji pre-1.0.0 zaktualizuj do `agent-framework-openai>=1.0.0`.
- [ ] Wszystkie wywołania `ChatOpenAI(...)` zawierają `use_responses_api=True`.
- [ ] Brak trafień dla `rg "choices\[0\]"` — cały dostęp do odpowiedzi używa `resp.output_text` lub schematu wyjściowego Responses.
- [ ] Brak `response_format` na poziomie głównym; całe wyjście strukturalne używa `text={"format": {...}}`.
- [ ] `openai>=1.108.1` i `azure-identity` w `requirements.txt` lub `pyproject.toml`; zależności zainstalowane ponownie.
- [ ] `store=False` ustawione przy każdym wywołaniu `responses.create`.
- [ ] Brak `api_version` w konstrukcji klienta; `AZURE_OPENAI_API_VERSION` usunięte z plików środowiskowych i infrastruktury.

### Bramy infrastruktury testowej (wszystkie muszą przejść)

- [ ] Brak trafień dla `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/`.
- [ ] Brak trafień dla `rg "_azure_ad_token_provider" tests/` — asercje zaktualizowane, aby sprawdzać `isinstance(client, AsyncOpenAI)` lub `base_url`.
- [ ] Brak trafień dla `rg "prompt_filter_results|content_filter_results" tests/` — usunięto filtry specyficzne dla Azure.
- [ ] Mocki używają `kwargs.get("input")` zamiast `kwargs.get("messages")`.
- [ ] Snapshopy / pliki golden zaktualizowane do formatu streamingowego Responses (brak `choices[0]`, `function_call`, `logprobs` itp.).
- [ ] `pytest` przechodzi bez błędów po wszystkich aktualizacjach testów.

### Bramy zachowań (weryfikacja ręczna lub przez zestaw testów)

- [ ] **Podstawowe uzupełnienie**: niestreamingowe `responses.create` zwraca niepusty `output_text`.
- [ ] **Parzystość streamingu**: jeśli oryginalny kod używał streamingu, kod po migracji strumieniuje i generuje zdarzenia `response.output_text.delta` z niepustymi delta.
- [ ] **Strukturalne wyjście**: jeśli używasz `text.format` z `json_schema`, `json.loads(resp.output_text)` kończy się sukcesem i pasuje do schematu.
- [ ] **Pętla wywołań narzędzi**: jeśli używane są narzędzia, model wykonuje wywołania narzędzi, aplikacja je wykonuje, a zapytanie następcze zwraca finalny `output_text` (bez nieskończonych pętli).
- [ ] **Parzystość asynchroniczna**: jeśli używano `AsyncAzureOpenAI`, równoważnik `AsyncOpenAI` działa z `await`.
- [ ] **Wskaźnik błędów**: brak nowych błędów 400/401/404 w porównaniu do stanu przed migracją.

### Dostawy

- Podsumowanie zawiera edytowane pliki, liczbę wywołań legacy przed/po i kolejne kroki.
- Zmiany to tylko edycje w drzewie roboczym (bez commitów).

---

## Wymagania wersji SDK

| Pakiet | Minimalna wersja |
|--------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Najnowsza (dla uwierzytelniania EntraID) |

---

## Odnośniki

- [Cheat Sheet — wszystkie fragmenty kodu](./references/cheat-sheet.md)
- [Test Migration — mocki, snapshoty, asercje](./references/test-migration.md)
- [Troubleshooting — błędy, tabela ryzyka, pułapki](./references/troubleshooting.md)
- [detect_legacy.py — automatyczny skaner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Dokumentacja Azure OpenAI Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Cykl życia wersji API Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API reference](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->