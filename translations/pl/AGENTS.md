# AGENTS.md

## Przegląd projektu

To repozytorium zawiera "Agentów AI dla początkujących" - kompleksowy kurs edukacyjny uczący wszystkiego, co potrzebne do budowy Agentów AI. Kurs składa się z 18 lekcji (numerowanych od 00 do 18), obejmujących podstawy, wzorce projektowe, frameworki, wdrożenie produkcyjne, agentów lokalnych/na urządzeniach oraz bezpieczeństwo agentów AI.

**Kluczowe technologie:**
- Python 3.12+
- Jupyter Notebooks do nauki interaktywnej
- Frameworki AI: Microsoft Agent Framework (MAF)
- Usługi Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektura:**
- Struktura oparta na lekcjach (foldery 00-15+)
- Każda lekcja zawiera: dokumentację README, przykładowy kod (notatniki Jupyter) oraz obrazy
- Wsparcie wielojęzyczne poprzez zautomatyzowany system tłumaczeń
- Jeden notatnik Python na lekcję wykorzystujący Microsoft Agent Framework

## Polecenia konfiguracji

### Wymagania wstępne
- Python 3.12 lub nowszy
- Subskrypcja Azure (dla Microsoft Foundry)
- Zainstalowane i uwierzytelnione Azure CLI (`az login`)

### Początkowa konfiguracja

1. **Sklonuj lub forkuj repozytorium:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # LUB
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Utwórz i aktywuj wirtualne środowisko Pythona:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # W systemie Windows: venv\Scripts\activate
   ```

3. **Zainstaluj zależności:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Skonfiguruj zmienne środowiskowe:**
   ```bash
   cp .env.example .env
   # Edytuj plik .env, dodając swoje klucze API i punkty końcowe
   ```

### Wymagane zmienne środowiskowe

Dla **Microsoft Foundry** (wymagane):
- `AZURE_AI_PROJECT_ENDPOINT` - punkt końcowy projektu Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nazwa wdrożenia modelu (np. gpt-5-mini)

Dla **Azure AI Search** (Lekcja 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - punkt końcowy Azure AI Search
- `AZURE_SEARCH_API_KEY` - klucz API Azure AI Search

Uwierzytelnianie: Uruchom `az login` przed uruchomieniem notatników (używa `AzureCliCredential`).

## Przebieg rozwoju

### Uruchamianie notatników Jupyter

Każda lekcja zawiera wiele notatników Jupyter dla różnych frameworków:

1. **Uruchom Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Przejdź do folderu lekcji** (np. `01-intro-to-ai-agents/code_samples/`)

3. **Otwórz i uruchom notatniki:**
   - `*-python-agent-framework.ipynb` - korzystanie z Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - korzystanie z Microsoft Agent Framework (.NET)

### Praca z Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Wymaga subskrypcji Azure
- Używa `FoundryChatClient` dla Agent Service V2 (agenci widoczni w portalu Foundry)
- Gotowe do produkcji z wbudowaną obserwowalnością
- Wzorzec pliku: `*-python-agent-framework.ipynb`

## Instrukcje testowania

To jest repozytorium edukacyjne z przykładowym kodem, a nie produkcyjne z automatycznymi testami. Aby zweryfikować instalację i zmiany:

### Testowanie ręczne

1. **Przetestuj środowisko Python:**
   ```bash
   python --version  # Powinno być 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Przetestuj wykonanie notatnika:**
   ```bash
   # Konwertuj notatnik na skrypt i uruchom (importy testów)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Zweryfikuj zmienne środowiskowe:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Uruchamianie pojedynczych notatników

Otwórz notatniki w Jupyter i wykonuj komórki kolejno. Każdy notatnik jest samodzielny i zawiera:
- Instrukcje importu
- Ładowanie konfiguracji
- Przykładowe implementacje agentów
- Oczekiwane wyjścia w komórkach markdown

### Testy podstawowe wdrożonych agentów

W lekcjach, gdzie agent jest wdrożony jako hostowany agent Microsoft Foundry (01, 04, 05, 16), repo dostarcza katalogi testów dymnych w folderze `tests/`, które są uruchamiane przez workflow `.github/workflows/smoke-test.yml` za pomocą akcji [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Są one lekkim testem po wdrożeniu (czy agent jest dostępny i spełnia podstawowe oczekiwania dotyczące promptu?), uzupełniającym pipeline ewaluacyjny w Lekcjach 10 i 16. Zobacz [tests/README.md](./tests/README.md) dla mapowania katalog-lekcja-agent. Lekcja 17 działa lokalnie z Foundry Local i nie ma hostowanego endpointu, więc jest walidowana przez bezpośrednie uruchomienie notatnika.

## Styl kodu

### Konwencje Pythona

- **Wersja Pythona**: 3.12+
- **Styl kodu**: Przestrzegaj standardowych konwencji PEP 8
- **Notatniki**: Używaj przejrzystych komórek markdown do wyjaśnień
- **Importy**: Grupuj biblioteki standardowe, zewnętrzne, lokalne

### Konwencje notatników Jupyter

- Zawieraj opisowe komórki markdown przed komórkami kodu
- Dodawaj przykłady wyników w notatnikach dla odniesienia
- Używaj jasnych nazw zmiennych zgodnych z koncepcjami lekcji
- Zachowuj liniową kolejność wykonywania notatnika (komórka 1 → 2 → 3...)

### Organizacja plików

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Budowa i wdrożenie

### Budowanie dokumentacji

To repozytorium używa Markdown do dokumentacji:
- Pliki README.md w każdym folderze lekcji
- Główny plik README.md w katalogu głównym repozytorium
- Zautomatyzowany system tłumaczeń poprzez GitHub Actions

### Pipeline CI/CD

Znajduje się w `.github/workflows/`:

1. **co-op-translator.yml** - Automatyczne tłumaczenia na 50+ języków
2. **welcome-issue.yml** - Powitanie nowych twórców issue
3. **welcome-pr.yml** - Powitanie nowych współtwórców pull requestów

### Wdrożenie

To jest repozytorium edukacyjne - brak procesu wdrożenia. Użytkownicy:
1. Tworzą forka lub klonują repozytorium
2. Uruchamiają notatniki lokalnie lub w GitHub Codespaces
3. Uczą się poprzez modyfikację i eksperymentowanie na przykładach

## Zasady dotyczące pull requestów

### Przed przesłaniem

1. **Przetestuj swoje zmiany:**
   - Uruchom całkowicie zmienione notatniki
   - Sprawdź, czy wszystkie komórki wykonują się bez błędów
   - Zweryfikuj, czy wyjścia są odpowiednie

2. **Aktualizacje dokumentacji:**
   - Aktualizuj README.md przy dodawaniu nowych konceptów
   - Dodaj komentarze w notatnikach dla skomplikowanego kodu
   - Upewnij się, że komórki markdown wyjaśniają cel

3. **Zmiany w plikach:**
   - Unikaj commitowania plików `.env` (używaj `.env.example`)
   - Nie commituj katalogów `venv/` ani `__pycache__/`
   - Zachowuj wyjścia notatników, gdy ilustrują koncepcje
   - Usuwaj pliki tymczasowe i kopie zapasowe notatników (`*-backup.ipynb`)

### Format tytułu PR

Używaj opisowych tytułów:
- `[Lesson-XX] Dodaj nowy przykład dla <konceptu>`
- `[Fix] Popraw literówkę w README lekcji-XX`
- `[Update] Ulepsz przykład kodu w lekcji-XX`
- `[Docs] Zaktualizuj instrukcje konfiguracji`

### Wymagane sprawdzenia

- Notatniki powinny wykonywać się bez błędów
- Pliki README powinny być jasne i dokładne
- Przestrzegaj istniejących wzorców kodu w repozytorium
- Zachowaj spójność z pozostałymi lekcjami

## Dodatkowe uwagi

### Typowe pułapki

1. **Niezgodność wersji Pythona:**
   - Używaj Pythona 3.12+
   - Niektóre pakiety mogą nie działać na starszych wersjach
   - Użyj `python3 -m venv`, by jawnie określić wersję Pythona

2. **Zmienne środowiskowe:**
   - Zawsze twórz `.env` na podstawie `.env.example`
   - Nie commituj pliku `.env` (jest w `.gitignore`)
   - Loguj się za pomocą `az login` dla uwierzytelniania Entra ID bez klucza

3. **Konflikty pakietów:**
   - Użyj świeżego wirtualnego środowiska
   - Instaluj z `requirements.txt`, nie pojedynczo
   - Niektóre notatniki mogą wymagać dodatkowych pakietów podanych w komórkach markdown

4. **Usługi Azure:**
   - Usługi Azure AI wymagają aktywnej subskrypcji
   - Niektóre funkcje są specyficzne dla regionu
   - Upewnij się, że twoje wdrożenie modelu Azure OpenAI obsługuje API odpowiedzi

### Ścieżka nauki

Zalecana kolejność lekcji:
1. **00-course-setup** - Zacznij tu, aby skonfigurować środowisko
2. **01-intro-to-ai-agents** - Zrozum podstawy agentów AI
3. **02-explore-agentic-frameworks** - Poznaj różne frameworki
4. **03-agentic-design-patterns** - Kluczowe wzorce projektowe
5. Kontynuuj kolejno kolejne numerowane lekcje

### Wybór frameworka

Wybierz framework zgodnie z celami:
- **Wszystkie lekcje**: Microsoft Agent Framework (MAF) z `FoundryChatClient`
- **Agenci rejestrują się po stronie serwera** w Microsoft Foundry Agent Service V2 i są widoczni w portalu Foundry

### Uzyskanie pomocy

- Dołącz do [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Przejrzyj pliki README lekcji dla szczegółowych wskazówek
- Sprawdź główny [README.md](./README.md) dla przeglądu kursu
- Odwiedź [Course Setup](./00-course-setup/README.md) dla szczegółowych instrukcji konfiguracji

### Współtworzenie

To jest otwarty projekt edukacyjny. Zapraszamy do współpracy:
- Poprawianie przykładów kodu
- Poprawianie literówek lub błędów
- Dodawanie wyjaśniających komentarzy
- Proponowanie nowych tematów lekcji
- Tłumaczenie na dodatkowe języki

Zobacz [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) dla aktualnych potrzeb.

## Kontekst specyficzny dla projektu

### Wsparcie wielojęzyczne

To repozytorium korzysta z automatycznego systemu tłumaczeń:
- Wspiera 50+ języków
- Tłumaczenia w katalogach `/translations/<lang-code>/`
- Workflow GitHub Actions zarządza aktualizacjami tłumaczeń
- Pliki źródłowe są po angielsku w katalogu głównym repozytorium

### Struktura lekcji

Każda lekcja ma ujednolicony wzorzec:
1. Miniatura wideo z linkiem
2. Pisane treści lekcji (README.md)
3. Przykłady kodu w wielu frameworkach
4. Cele nauki i wymagania wstępne
5. Powiązane dodatkowe materiały edukacyjne

### Nazewnictwo przykładów kodu

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcja 1, MAF Python
- `14-sequential.ipynb` - Lekcja 14, zaawansowane wzorce MAF
- `16-python-agent-framework.ipynb` - Lekcja 16, produkcyjny agent wsparcia klienta
- `17-local-agent-foundry-local.ipynb` - Lekcja 17, agent lokalny z Foundry Local + Qwen

### Specjalne katalogi

- `translated_images/` - Zlokalizowane obrazy do tłumaczeń
- `images/` - Oryginalne obrazy dla treści w języku angielskim
- `.devcontainer/` - Konfiguracja kontenera deweloperskiego VS Code
- `.github/` - Workflow i szablony GitHub Actions

### Zależności

Kluczowe pakiety z `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - wsparcie protokołu Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - usługi Azure AI
- `azure-identity` - uwierzytelnianie Azure (AzureCliCredential)
- `azure-search-documents` - integracja Azure AI Search
- `mcp[cli]` - wsparcie Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->