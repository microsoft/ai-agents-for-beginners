# AGENTS.md

## Przegląd projektu

To repozytorium zawiera "AI Agents for Beginners" - kompleksowy kurs edukacyjny uczący wszystkiego, co potrzebne do budowy agentów AI. Kurs składa się z ponad 15 lekcji obejmujących podstawy, wzorce projektowe, frameworki i wdrożenie agentów AI do produkcji.

**Kluczowe technologie:**
- Python 3.12+
- Notatniki Jupyter do nauki interaktywnej
- Frameworki AI: Microsoft Agent Framework (MAF)
- Usługi Azure AI: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architektura:**
- Struktura oparta na lekcjach (katalogi 00-15+)
- Każda lekcja zawiera: dokumentację README, przykłady kodu (notatniki Jupyter) oraz obrazy
- Obsługa wielu języków za pomocą zautomatyzowanego systemu tłumaczeń
- Jeden notatnik Pythona na lekcję korzystający z Microsoft Agent Framework

## Polecenia konfiguracji

### Wymagania wstępne
- Python 3.12 lub nowszy
- Subskrypcja Azure (dla Azure AI Foundry)
- Zainstalowany i uwierzytelniony Azure CLI (`az login`)

### Początkowa konfiguracja

1. **Clone or fork the repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # LUB
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Create and activate Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # W systemie Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edytuj plik .env, podając klucze API i adresy punktów końcowych
   ```

### Wymagane zmienne środowiskowe

For **Azure AI Foundry** (Wymagane):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (e.g., gpt-4o)

For **Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Uwierzytelnianie: Uruchom `az login` przed uruchomieniem notatników (używa `AzureCliCredential`).

## Proces rozwoju

### Uruchamianie notatników Jupyter

Każda lekcja zawiera kilka notatników Jupyter dla różnych frameworków:

1. **Uruchom Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Przejdź do katalogu lekcji** (np. `01-intro-to-ai-agents/code_samples/`)

3. **Otwórz i uruchom notatniki:**
   - `*-python-agent-framework.ipynb` - Korzystanie z Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Korzystanie z Microsoft Agent Framework (.NET)

### Praca z Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Wymaga subskrypcji Azure
- Używa `AzureAIProjectAgentProvider` dla Agent Service V2 (agenty widoczne w portalu Foundry)
- Gotowe do produkcji z wbudowaną obserwowalnością
- Wzorzec pliku: `*-python-agent-framework.ipynb`

## Instrukcje testowania

To repozytorium edukacyjne z przykładowym kodem, a nie kodem produkcyjnym z automatycznymi testami. Aby zweryfikować konfigurację i zmiany:

### Testy ręczne

1. **Przetestuj środowisko Pythona:**
   ```bash
   python --version  # Powinno być 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Przetestuj wykonanie notatnika:**
   ```bash
   # Konwertuj notebook na skrypt i uruchom (importy testów)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Zweryfikuj zmienne środowiskowe:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Uruchamianie pojedynczych notatników

Otwórz notatniki w Jupyter i wykonuj komórki kolejno. Każdy notatnik jest samodzielny i zawiera:
- Instrukcje importu
- Ładowanie konfiguracji
- Przykładowe implementacje agentów
- Oczekiwane wyjścia w komórkach markdown

## Styl kodu

### Konwencje Pythona

- **Wersja Pythona**: 3.12+
- **Styl kodu**: Stosuj standardowe konwencje PEP 8
- **Notatniki**: Używaj czytelnych komórek markdown do wyjaśniania koncepcji
- **Importy**: Grupuj wg biblioteki standardowej, bibliotek zewnętrznych i importów lokalnych

### Konwencje notatników Jupyter

- Dołącz opisowe komórki markdown przed komórkami z kodem
- Dodaj przykłady wyjść w notatnikach jako odniesienie
- Używaj czytelnych nazw zmiennych zgodnych z koncepcjami lekcji
- Zachowaj liniowy porządek wykonywania notatnika (komórka 1 → 2 → 3...)

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

### Tworzenie dokumentacji

To repozytorium używa Markdown do dokumentacji:
- Pliki README.md w każdym folderze lekcji
- Główny README.md w katalogu głównym repozytorium
- Zautomatyzowany system tłumaczeń za pomocą GitHub Actions

### Potok CI/CD

Znajduje się w `.github/workflows/`:

1. **co-op-translator.yml** - Automatyczne tłumaczenie na 50+ języków
2. **welcome-issue.yml** - Wita autorów nowych issue
3. **welcome-pr.yml** - Wita nowych kontrybutorów pull requestów

### Wdrażanie

To repozytorium edukacyjne - brak procesu wdrażania. Użytkownicy:
1. Forkuj lub sklonuj repozytorium
2. Uruchom notatniki lokalnie lub w GitHub Codespaces
3. Ucz się, modyfikując i eksperymentując z przykładami

## Wytyczne dotyczące pull requestów

### Przed wysłaniem

1. **Przetestuj swoje zmiany:**
   - Uruchom w pełni zmienione notatniki
   - Zweryfikuj, że wszystkie komórki wykonują się bez błędów
   - Sprawdź, czy wyjścia są odpowiednie

2. **Aktualizacje dokumentacji:**
   - Zaktualizuj README.md, jeśli dodajesz nowe koncepcje
   - Dodaj komentarze w notatnikach dla złożonego kodu
   - Upewnij się, że komórki markdown wyjaśniają cel

3. **Zmiany w plikach:**
   - Unikaj commitowania plików `.env` (używaj `.env.example`)
   - Nie commituj katalogów `venv/` ani `__pycache__/`
   - Zachowaj outputy notatników, gdy demonstrują koncepcje
   - Usuń pliki tymczasowe i kopie zapasowe notatników (`*-backup.ipynb`)

### Format tytułu PR

Używaj opisowych tytułów:
- `[Lesson-XX] Dodaj nowy przykład dla <concept>`
- `[Fix] Popraw literówkę w lesson-XX README`
- `[Update] Ulepsz przykład kodu w lesson-XX`
- `[Docs] Zaktualizuj instrukcje konfiguracji`

### Wymagane kontrole

- Notatniki powinny wykonywać się bez błędów
- Pliki README powinny być jasne i dokładne
- Podążaj za istniejącymi wzorcami kodu w repozytorium
- Zachowaj spójność z innymi lekcjami

## Dodatkowe uwagi

### Typowe problemy

1. **Niedopasowanie wersji Pythona:**
   - Upewnij się, że używasz Pythona 3.12+
   - Niektóre pakiety mogą nie działać ze starszymi wersjami
   - Użyj `python3 -m venv`, aby wyraźnie wskazać wersję Pythona

2. **Zmienne środowiskowe:**
   - Zawsze utwórz `.env` z `.env.example`
   - Nie commituj pliku `.env` (jest w `.gitignore`)
   - Token GitHub wymaga odpowiednich uprawnień

3. **Konflikty pakietów:**
   - Używaj świeżego wirtualnego środowiska
   - Instaluj z `requirements.txt` zamiast pojedynczych pakietów
   - Niektóre notatniki mogą wymagać dodatkowych pakietów wymienionych w ich komórkach markdown

4. **Usługi Azure:**
   - Usługi Azure AI wymagają aktywnej subskrypcji
   - Niektóre funkcje są specyficzne dla regionu
   - Ograniczenia darmowego poziomu obowiązują dla GitHub Models

### Ścieżka nauki

Zalecana kolejność lekcji:
1. **00-course-setup** - Zacznij tutaj, aby skonfigurować środowisko
2. **01-intro-to-ai-agents** - Zrozum podstawy agentów AI
3. **02-explore-agentic-frameworks** - Poznaj różne frameworki
4. **03-agentic-design-patterns** - Podstawowe wzorce projektowe
5. Kontynuuj przez kolejne lekcje numerowane sekwencyjnie

### Wybór frameworku

Wybierz framework w zależności od celów:
- **All lessons**: Microsoft Agent Framework (MAF) z `AzureAIProjectAgentProvider`
- **Agenty rejestrują się po stronie serwera** w Azure AI Foundry Agent Service V2 i są widoczne w portalu Foundry

### Uzyskanie pomocy

- Dołącz do [Społeczności Microsoft Foundry na Discordzie](https://aka.ms/ai-agents/discord)
- Przejrzyj pliki README lekcji po konkretne wskazówki
- Sprawdź główny [README.md](./README.md) z przeglądem kursu
- Odnieś się do [Konfiguracja kursu](./00-course-setup/README.md) po szczegółowe instrukcje konfiguracji

### Współtworzenie

To otwarty projekt edukacyjny. Zachęcamy do wkładu:
- Udoskonal przykłady kodu
- Popraw literówki lub błędy
- Dodaj wyjaśniające komentarze
- Zaproponuj nowe tematy lekcji
- Przetłumacz na dodatkowe języki

Zobacz [Zgłoszenia GitHub](https://github.com/microsoft/ai-agents-for-beginners/issues) dla bieżących potrzeb.

## Kontekst specyficzny dla projektu

### Wsparcie wielojęzyczne

To repozytorium korzysta z automatycznego systemu tłumaczeń:
- Obsługa 50+ języków
- Tłumaczenia w katalogach `/translations/<lang-code>/`
- Workflow GitHub Actions obsługuje aktualizacje tłumaczeń
- Pliki źródłowe są w języku angielskim w katalogu głównym repozytorium

### Struktura lekcji

Każda lekcja ma spójny wzorzec:
1. Miniaturka wideo z linkiem
2. Pisane treści lekcji (README.md)
3. Przykłady kodu w wielu frameworkach
4. Cele nauki i wymagania wstępne
5. Dodatkowe zasoby edukacyjne w linkach

### Nadawanie nazw przykładom kodu

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcja 1, MAF Python
- `14-sequential.ipynb` - Lekcja 14, zaawansowane wzorce MAF

### Specjalne katalogi

- `translated_images/` - Zlokalizowane obrazy dla tłumaczeń
- `images/` - Oryginalne obrazy dla treści angielskich
- `.devcontainer/` - Konfiguracja kontenera developerskiego VS Code
- `.github/` - Workflowy i szablony GitHub Actions

### Zależności

Kluczowe pakiety z `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Wsparcie protokołu Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Usługi Azure AI
- `azure-identity` - Uwierzytelnianie Azure (AzureCliCredential)
- `azure-search-documents` - Integracja z Azure AI Search
- `mcp[cli]` - Wsparcie Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Zastrzeżenie:
Niniejszy dokument został przetłumaczony z użyciem usługi tłumaczeń opartych na sztucznej inteligencji [Co-op Translator](https://github.com/Azure/co-op-translator). Pomimo że dokładamy starań, aby tłumaczenie było jak najdokładniejsze, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uważany za wersję wiążącą. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->