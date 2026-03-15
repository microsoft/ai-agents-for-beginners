# AGENTS.md

## Przegląd projektu

To repozytorium zawiera "AI Agents for Beginners" - kompleksowy kurs edukacyjny uczący wszystkiego, co potrzebne do budowania Agentów AI. Kurs składa się z 15+ lekcji obejmujących podstawy, wzorce projektowe, frameworki oraz wdrożenie agentów AI do produkcji.

**Kluczowe technologie:**
- Python 3.12+
- Jupyter Notebooks do nauki interaktywnej
- Frameworki AI: Microsoft Agent Framework (MAF)
- Usługi Azure AI: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architektura:**
- Struktura oparta na lekcjach (katalogi 00-15+)
- Każda lekcja zawiera: dokumentację README, przykłady kodu (notatniki Jupyter) oraz obrazy
- Wsparcie wielojęzyczne za pomocą zautomatyzowanego systemu tłumaczeń
- Jeden notatnik Pythona na lekcję korzystający z Microsoft Agent Framework

## Polecenia konfiguracji

### Wymagania wstępne
- Python 3.12 lub nowszy
- Subskrypcja Azure (dla Azure AI Foundry)
- Azure CLI zainstalowany i uwierzytelniony (`az login`)

### Wstępna konfiguracja

1. **Sklonuj lub sforkuj repozytorium:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # LUB
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Utwórz i aktywuj wirtualne środowisko Pythona:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Na Windowsie: venv\Scripts\activate
   ```

3. **Zainstaluj zależności:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Skonfiguruj zmienne środowiskowe:**
   ```bash
   cp .env.example .env
   # Edytuj plik .env, wpisując swoje klucze API i adresy endpointów
   ```

### Wymagane zmienne środowiskowe

Dla **Azure AI Foundry** (wymagane):
- `AZURE_AI_PROJECT_ENDPOINT` - punkt końcowy projektu Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - nazwa wdrożenia modelu (np. gpt-4o)

Dla **Azure AI Search** (Lekcja 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - punkt końcowy Azure AI Search
- `AZURE_SEARCH_API_KEY` - klucz API Azure AI Search

Uwierzytelnianie: Uruchom `az login` przed uruchomieniem notatników (używa `AzureCliCredential`).

## Przepływ pracy deweloperskiej

### Uruchamianie notatników Jupyter

Każda lekcja zawiera wiele notatników Jupyter dla różnych frameworków:

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
- Używa `AzureAIProjectAgentProvider` dla Agent Service V2 (agenci widoczni w portalu Foundry)
- Gotowy do produkcji z wbudowaną obserwowalnością
- Wzorzec pliku: `*-python-agent-framework.ipynb`

## Instrukcje testowania

To repozytorium edukacyjne zawierające przykładowy kod, a nie kod produkcyjny z automatycznymi testami. Aby zweryfikować konfigurację i zmiany:

### Testowanie ręczne

1. **Przetestuj środowisko Pythona:**
   ```bash
   python --version  # Powinno być 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Przetestuj wykonanie notatników:**
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
- **Styl kodu**: Stosuj standardowe konwencje PEP 8 dla Pythona
- **Notatniki**: Używaj czytelnych komórek markdown do wyjaśniania koncepcji
- **Importy**: Grupuj importy według: biblioteki standardowej, zewnętrznych, lokalnych

### Konwencje dotyczące notatników Jupyter

- Umieszczaj opisowe komórki markdown przed komórkami z kodem
- Dodawaj przykłady wyjść w notatnikach jako odniesienie
- Używaj jasnych nazw zmiennych zgodnych z koncepcjami lekcji
- Zachowaj liniową kolejność wykonywania notatnika (komórka 1 → 2 → 3...)

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

### Pipeline CI/CD

Zlokalizowany w `.github/workflows/`:

1. **co-op-translator.yml** - Automatyczne tłumaczenie na 50+ języków
2. **welcome-issue.yml** - Wita twórców nowych zgłoszeń
3. **welcome-pr.yml** - Wita nowych autorów pull requestów

### Wdrażanie

To repozytorium edukacyjne - brak procesu wdrożenia. Użytkownicy:
1. Sforkuj lub sklonuj repozytorium
2. Uruchamiaj notatniki lokalnie lub w GitHub Codespaces
3. Ucz się, modyfikując i eksperymentując na przykładach

## Wytyczne dotyczące pull requestów

### Przed wysłaniem

1. **Przetestuj swoje zmiany:**
   - Uruchom w całości zmienione notatniki
   - Sprawdź, czy wszystkie komórki wykonują się bez błędów
   - Sprawdź, czy wyjścia są prawidłowe

2. **Aktualizacje dokumentacji:**
   - Zaktualizuj README.md, jeśli dodajesz nowe koncepcje
   - Dodaj komentarze w notatnikach dla złożonego kodu
   - Upewnij się, że komórki markdown wyjaśniają cel

3. **Zmiany w plikach:**
   - Unikaj commitowania plików `.env` (użyj `.env.example`)
   - Nie commituj katalogów `venv/` lub `__pycache__/`
   - Zachowaj wyjścia notatników, gdy demonstrują koncepcje
   - Usuń pliki tymczasowe i kopie zapasowe notatników (`*-backup.ipynb`)

### Format tytułu PR

Używaj opisowych tytułów:
- `[Lesson-XX] Dodaj nowy przykład dla <concept>`
- `[Fix] Popraw literówkę w lesson-XX README`
- `[Update] Ulepsz przykład kodu w lesson-XX`
- `[Docs] Zaktualizuj instrukcje konfiguracji`

### Wymagane sprawdzenia

- Notatniki powinny wykonywać się bez błędów
- Pliki README powinny być jasne i dokładne
- Postępuj zgodnie z istniejącymi wzorcami kodu w repozytorium
- Zachowaj spójność z innymi lekcjami

## Dodatkowe uwagi

### Częste pułapki

1. **Niezgodność wersji Pythona:**
   - Upewnij się, że używasz Pythona 3.12+
   - Niektóre pakiety mogą nie działać z starszymi wersjami
   - Użyj `python3 -m venv`, aby jawnie określić wersję Pythona

2. **Zmienne środowiskowe:**
   - Zawsze twórz `.env` na podstawie `.env.example`
   - Nie commituj pliku `.env` (jest na liście `.gitignore`)
   - Token GitHub wymaga odpowiednich uprawnień

3. **Konflikty pakietów:**
   - Używaj świeżego wirtualnego środowiska
   - Instaluj z `requirements.txt` zamiast pojedynczych pakietów
   - Niektóre notatniki mogą wymagać dodatkowych pakietów wymienionych w ich komórkach markdown

4. **Usługi Azure:**
   - Usługi Azure AI wymagają aktywnej subskrypcji
   - Niektóre funkcje są specyficzne dla regionu
   - Ograniczenia darmowego poziomu dotyczą modeli GitHub

### Ścieżka nauki

Zalecana kolejność lekcji:
1. **00-course-setup** - Zacznij tutaj, aby skonfigurować środowisko
2. **01-intro-to-ai-agents** - Zrozum podstawy agentów AI
3. **02-explore-agentic-frameworks** - Poznaj różne frameworki
4. **03-agentic-design-patterns** - Podstawowe wzorce projektowe
5. Kontynuuj przez kolejne lekcje w porządku numeracji

### Wybór frameworku

Wybierz framework w zależności od celów:
- **Wszystkie lekcje**: Microsoft Agent Framework (MAF) z `AzureAIProjectAgentProvider`
- **Agenci rejestrują się po stronie serwera** w Azure AI Foundry Agent Service V2 i są widoczni w portalu Foundry

### Uzyskiwanie pomocy

- Dołącz do [Społeczności Microsoft Foundry na Discordzie](https://aka.ms/ai-agents/discord)
- Przejrzyj pliki README lekcji, aby uzyskać szczegółowe wskazówki
- Sprawdź główny [README.md](./README.md) dla przeglądu kursu
- Zapoznaj się z [Konfiguracją kursu](./00-course-setup/README.md) w celu szczegółowych instrukcji

### Współtworzenie

To otwarty projekt edukacyjny. Wkłady mile widziane:
- Popraw przykłady kodu
- Popraw literówki lub błędy
- Dodaj objaśniające komentarze
- Zaproponuj nowe tematy lekcji
- Przetłumacz na dodatkowe języki

Zobacz [Zgłoszenia na GitHub](https://github.com/microsoft/ai-agents-for-beginners/issues) aby poznać bieżące potrzeby.

## Kontekst specyficzny dla projektu

### Wsparcie wielojęzyczne

To repozytorium korzysta z zautomatyzowanego systemu tłumaczeń:
- Obsługiwane 50+ języków
- Tłumaczenia w katalogach `/translations/<lang-code>/`
- Workflow GitHub Actions obsługuje aktualizacje tłumaczeń
- Pliki źródłowe są po angielsku w katalogu głównym repozytorium

### Struktura lekcji

Każda lekcja ma spójny wzorzec:
1. Miniaturka wideo z linkiem
2. Treść lekcji w formie pisemnej (README.md)
3. Przykłady kodu w wielu frameworkach
4. Cele nauczania i wymagania wstępne
5. Dodatkowe powiązane zasoby do nauki

### Nazewnictwo przykładów kodu

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lekcja 1, MAF Python
- `14-sequential.ipynb` - Lekcja 14, zaawansowane wzorce MAF

### Specjalne katalogi

- `translated_images/` - Zlokalizowane obrazy dla tłumaczeń
- `images/` - Oryginalne obrazy dla treści w języku angielskim
- `.devcontainer/` - Konfiguracja kontenera deweloperskiego VS Code
- `.github/` - Workflowy i szablony GitHub Actions

### Zależności

Kluczowe pakiety z `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Obsługa protokołu Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Usługi Azure AI
- `azure-identity` - Uwierzytelnianie Azure (AzureCliCredential)
- `azure-search-documents` - Integracja z Azure AI Search
- `mcp[cli]` - Obsługa Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Zastrzeżenie:
Dokument ten został przetłumaczony przy użyciu usługi tłumaczenia AI Co-op Translator (https://github.com/Azure/co-op-translator). Chociaż dokładamy starań o dokładność, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za dokument wiążący. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za żadne nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->