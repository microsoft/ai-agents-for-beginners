# AGENTS.md

## Przegląd projektu

To repozytorium zawiera "AI Agents for Beginners" - kompleksowy kurs edukacyjny uczący wszystkiego, co potrzebne do budowy agentów AI. Kurs składa się z 18 lekcji (numerowanych od 00 do 18), obejmujących podstawy, wzorce projektowe, frameworki, wdrażanie produkcyjne, agentów lokalnych/na urządzeniu oraz bezpieczeństwo agentów AI.

**Kluczowe technologie:**
- Python 3.12+
- Jupyter Notebooks do nauki interaktywnej
- Frameworki AI: Microsoft Agent Framework (MAF)
- Usługi Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektura:**
- Struktura lekcji (foldery 00-18)
- Każda lekcja zawiera: dokumentację README, przykłady kodu (notatniki Jupyter) oraz obrazy
- Wsparcie wielojęzyczne poprzez zautomatyzowany system tłumaczeń
- Jeden notatnik Python na lekcję z wykorzystaniem Microsoft Agent Framework

## Polecenia instalacji

### Wymagania wstępne
- Python 3.12 lub nowszy
- Subskrypcja Azure (dla Microsoft Foundry)
- Zainstalowane oraz zalogowane Azure CLI (`az login`)

### Początkowa konfiguracja

1. **Sklonuj lub zrób fork repozytorium:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Utwórz i aktywuj wirtualne środowisko Pythona:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Zainstaluj zależności:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Skonfiguruj zmienne środowiskowe:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Wymagane zmienne środowiskowe

Dla **Microsoft Foundry** (wymagane):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint projektu Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nazwa wdrożenia modelu (np. gpt-5-mini)

Dla **Azure AI Search** (Lekcja 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint Azure AI Search
- `AZURE_SEARCH_API_KEY` - klucz API Azure AI Search

Uwierzytelnianie: Uruchom `az login` przed uruchomieniem notatników (używa `AzureCliCredential`).

## Przebieg pracy developerskiej

### Uruchamianie Jupyter Notebooks

Każda lekcja zawiera kilka notatników Jupyter dla różnych frameworków:

1. **Uruchom Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Przejdź do folderu lekcji** (np. `01-intro-to-ai-agents/code_samples/`)

3. **Otwórz i uruchom notatniki:**
   - `*-python-agent-framework.ipynb` - użycie Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - użycie Microsoft Agent Framework (.NET)

### Praca z Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Wymaga subskrypcji Azure
- Używa `FoundryChatClient` dla Agent Service V2 (agenci widoczni na portalu Foundry)
- Gotowe do produkcji z wbudowaną obserwowalnością
- Wzorzec nazw plików: `*-python-agent-framework.ipynb`

## Instrukcje testowania

To repozytorium edukacyjne z przykładowym kodem, a nie kod produkcyjny z automatycznymi testami. Aby zweryfikować swój setup i zmiany:

### Testowanie ręczne

1. **Test środowiska Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test wykonania notatnika:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Weryfikacja zmiennych środowiskowych:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Uruchamianie pojedynczych notatników

Otwórz notatniki w Jupyter i wykonuj komórki po kolei. Każdy notatnik jest samodzielny i zawiera:
- instrukcje importu
- ładowanie konfiguracji
- przykładowe implementacje agentów
- oczekiwane wyniki w komórkach markdown

### Testy dymne wdrożonych agentów

Dla lekcji, w których agent jest wdrożony jako hostowany agent Microsoft Foundry (01, 04, 05, 16), repozytorium zawiera katalogi testów dymnych pod `tests/`, wywoływane w workflow `.github/workflows/smoke-test.yml` przez akcję [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Są to lekkie testy po wdrożeniu (czy agent jest osiągalny i reaguje na podstawowe prompt-y?), uzupełniające pipeline ewaluacyjny w lekcjach 10 i 16. Zobacz [tests/README.md](./tests/README.md) dla mapowania katalogów na lekcje i agentów. Lekcja 17 działa lokalnie z Foundry Local i nie ma hostowanego endpointu, więc jest weryfikowana przez bezpośrednie uruchomienie notatnika.

## Styl kodu

### Konwencje Pythona

- **Wersja Pythona**: 3.12+
- **Styl kodu**: stosuj standardy PEP 8 dla Pythona
- **Notatniki**: używaj czytelnych komórek markdown do wyjaśniania koncepcji
- **Importy**: grupuj importy ze standardowej biblioteki, zewnętrzne i lokalne

### Konwencje Jupyter Notebook

- Dołączaj opisowe komórki markdown przed komórkami kodu
- Dodawaj przykłady wyników w notatnikach jako odniesienie
- Używaj czytelnych nazw zmiennych odpowiadających koncepcjom lekcji
- Zachowuj liniową kolejność wykonania notatnika (komórka 1 → 2 → 3...)

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

## Budowanie i wdrażanie

### Budowanie dokumentacji

To repozytorium używa Markdown do dokumentacji:
- pliki README.md w każdym folderze lekcji
- Główny README.md w katalogu głównym repozytorium
- Zautomatyzowany system tłumaczeń przez GitHub Actions

### Pipeline CI/CD

Znajduje się w `.github/workflows/`:

1. **co-op-translator.yml** - Automatyczne tłumaczenie na ponad 50 języków
2. **welcome-issue.yml** - Powitanie nowych autorów zgłoszeń
3. **welcome-pr.yml** - Powitanie nowych współtwórców pull requestów

### Wdrażanie

To repozytorium edukacyjne - brak procesu wdrożenia. Użytkownicy:
1. Forkują lub klonują repozytorium
2. Uruchamiają notatniki lokalnie lub w GitHub Codespaces
3. Uczą się przez modyfikacje i eksperymenty z przykładami

## Wytyczne dotyczące pull requestów

### Przed wysłaniem

1. **Przetestuj swoje zmiany:**
   - Uruchom całkowicie zmienione notatniki
   - Sprawdź, czy wszystkie komórki wykonują się bez błędów
   - Zweryfikuj, czy wyniki są odpowiednie

2. **Aktualizacje dokumentacji:**
   - Zaktualizuj README.md, jeśli dodajesz nowe koncepcje
   - Dodaj komentarze w notatnikach dla złożonego kodu
   - Upewnij się, że komórki markdown wyjaśniają cel

3. **Zmiany w plikach:**
   - Unikaj dodawania plików `.env` (używaj `.env.example`)
   - Nie dodawaj katalogów `venv/` lub `__pycache__/`
   - Zachowuj wyniki notatników, jeśli demonstrują koncepcje
   - Usuń pliki tymczasowe i kopie zapasowe notatników (`*-backup.ipynb`)

### Format tytułu PR

Używaj opisowych tytułów:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Wymagane sprawdzenia

- Notatniki powinny się wykonywać bez błędów
- Pliki README powinny być jasne i dokładne
- Stosuj istniejące wzorce kodu w repozytorium
- Zachowaj spójność z innymi lekcjami

## Dodatkowe uwagi

### Typowe pułapki

1. **Niezgodność wersji Pythona:**
   - Używaj Pythona 3.12 lub nowszego
   - Niektóre pakiety mogą nie działać z wcześniejszymi wersjami
   - Używaj `python3 -m venv`, aby jawnie określić wersję Pythona

2. **Zmienne środowiskowe:**
   - Zawsze twórz `.env` z `.env.example`
   - Nie dodawaj pliku `.env` (jest w `.gitignore`)
   - Loguj się przez `az login` do uwierzytelniania bez klucza Entra ID

3. **Konflikty pakietów:**
   - Używaj świeżego wirtualnego środowiska
   - Instaluj z `requirements.txt` zamiast pojedynczych pakietów
   - Niektóre notatniki mogą wymagać dodatkowych pakietów wymienionych w ich komórkach markdown

4. **Usługi Azure:**
   - Usługi Azure AI wymagają aktywnej subskrypcji
   - Niektóre funkcje są specyficzne dla regionu
   - Upewnij się, że Twoje wdrożenie modelu Azure OpenAI obsługuje Responses API

### Ścieżka nauki

Zalecana kolejność lekcji:
1. **00-course-setup** - Zacznij od konfiguracji środowiska
2. **01-intro-to-ai-agents** - Poznaj podstawy agentów AI
3. **02-explore-agentic-frameworks** - Poznaj różne frameworki
4. **03-agentic-design-patterns** - Podstawowe wzorce projektowe
5. Kontynuuj kolejne lekcje po kolei

### Wybór frameworku

Wybierz framework zgodnie z celami:
- **Wszystkie lekcje**: Microsoft Agent Framework (MAF) z `FoundryChatClient`
- **Agenci rejestrowani po stronie serwera** w Microsoft Foundry Agent Service V2 i widoczni w portalu Foundry

### Uzyskiwanie pomocy

- Dołącz do [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Sprawdź pliki README poszczególnych lekcji po konkretne wskazówki
- Zobacz główny [README.md](./README.md) dla przeglądu kursu
- Odnieś się do [Course Setup](./00-course-setup/README.md) dla szczegółowych instrukcji instalacji

### Współtworzenie

To otwarty projekt edukacyjny. Zapraszamy do współpracy:
- Ulepszanie przykładów kodu
- Poprawianie literówek lub błędów
- Dodawanie komentarzy wyjaśniających
- Sugestie nowych tematów lekcji
- Tłumaczenia na dodatkowe języki

Zobacz [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) dla bieżących potrzeb.

## Kontekst specyficzny dla projektu

### Wsparcie wielojęzyczne

To repozytorium używa zautomatyzowanego systemu tłumaczeń:
- obsługa ponad 50 języków
- tłumaczenia w katalogach `/translations/<lang-code>/`
- workflow GitHub Actions zarządza aktualizacjami tłumaczeń
- pliki źródłowe są w języku angielskim w głównym katalogu repozytorium

### Struktura lekcji

Każda lekcja ma spójny schemat:
1. Miniatura wideo z linkiem
2. Pisany materiał lekcji (README.md)
3. Przykłady kodu w różnych frameworkach
4. Cele nauki i wymagania wstępne
5. Dodatkowe zasoby edukacyjne podlinkowane

### Nazewnictwo przykładowych kodów

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcja 1, MAF Python
- `14-sequential.ipynb` - Lekcja 14, zaawansowane wzorce MAF
- `16-python-agent-framework.ipynb` - Lekcja 16, produkcyjny agent wsparcia klienta
- `17-local-agent-foundry-local.ipynb` - Lekcja 17, lokalny agent z Foundry Local + Qwen

### Specjalne katalogi

- `translated_images/` - zlokalizowane obrazy do tłumaczeń
- `images/` - oryginalne obrazy dla treści angielskich
- `.devcontainer/` - konfiguracja kontenera deweloperskiego VS Code
- `.github/` - workflow i szablony GitHub Actions

### Zależności

Kluczowe pakiety z `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - wsparcie protokołu agent-to-agent
- `azure-ai-inference`, `azure-ai-projects` - usługi Azure AI
- `azure-identity` - uwierzytelnianie Azure (AzureCliCredential)
- `azure-search-documents` - integracja Azure AI Search
- `mcp[cli]` - wsparcie Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->