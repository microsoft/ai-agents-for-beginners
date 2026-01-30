# AGENTS.md

## Przegląd projektu

To repozytorium zawiera kurs edukacyjny "AI Agents for Beginners" - kompleksowy przewodnik uczący wszystkiego, co potrzebne do budowy agentów AI. Kurs składa się z ponad 15 lekcji obejmujących podstawy, wzorce projektowe, frameworki oraz wdrażanie agentów AI w środowisku produkcyjnym.

**Kluczowe technologie:**
- Python 3.12+
- Jupyter Notebooks do interaktywnej nauki
- Frameworki AI: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Usługi Azure AI: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (dostępna darmowa wersja)

**Architektura:**
- Struktura oparta na lekcjach (katalogi 00-15+)
- Każda lekcja zawiera: dokumentację README, przykłady kodu (notatniki Jupyter) oraz obrazy
- Obsługa wielu języków dzięki automatycznemu systemowi tłumaczeń
- Wiele opcji frameworków dla każdej lekcji (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Polecenia instalacji

### Wymagania wstępne
- Python 3.12 lub nowszy
- Konto GitHub (dla GitHub Models - darmowa wersja)
- Subskrypcja Azure (opcjonalnie, dla usług Azure AI)

### Wstępna konfiguracja

1. **Sklonuj lub zrób fork repozytorium:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Utwórz i aktywuj wirtualne środowisko Python:**
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

Dla **GitHub Models (darmowe):**
- `GITHUB_TOKEN` - Token dostępu osobistego z GitHub

Dla **Azure AI Services** (opcjonalnie):
- `PROJECT_ENDPOINT` - Endpoint projektu Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - Klucz API Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL endpointu Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Nazwa wdrożenia modelu czatu
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Nazwa wdrożenia dla osadzeń
- Dodatkowa konfiguracja Azure, jak pokazano w `.env.example`

## Przebieg pracy nad projektem

### Uruchamianie notatników Jupyter

Każda lekcja zawiera wiele notatników Jupyter dla różnych frameworków:

1. **Uruchom Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Przejdź do katalogu lekcji** (np. `01-intro-to-ai-agents/code_samples/`)

3. **Otwórz i uruchom notatniki:**
   - `*-semantic-kernel.ipynb` - Korzystanie z frameworka Semantic Kernel
   - `*-autogen.ipynb` - Korzystanie z frameworka AutoGen
   - `*-python-agent-framework.ipynb` - Korzystanie z Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Korzystanie z Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Korzystanie z Azure AI Agent Service

### Praca z różnymi frameworkami

**Semantic Kernel + GitHub Models:**
- Dostępna darmowa wersja z kontem GitHub
- Dobre do nauki i eksperymentowania
- Wzorzec pliku: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Dostępna darmowa wersja z kontem GitHub
- Możliwości orkiestracji wieloagentowej
- Wzorzec pliku: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Najnowszy framework od Microsoft
- Dostępny w wersji Python i .NET
- Wzorzec pliku: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Wymaga subskrypcji Azure
- Funkcje gotowe do wdrożenia produkcyjnego
- Wzorzec pliku: `*-azureaiagent.ipynb`

## Instrukcje testowania

To repozytorium ma charakter edukacyjny i zawiera przykładowy kod, a nie kod produkcyjny z automatycznymi testami. Aby zweryfikować konfigurację i zmiany:

### Testowanie ręczne

1. **Przetestuj środowisko Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Przetestuj wykonanie notatników:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Zweryfikuj zmienne środowiskowe:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Uruchamianie pojedynczych notatników

Otwórz notatniki w Jupyter i wykonuj komórki sekwencyjnie. Każdy notatnik jest samodzielny i zawiera:
- Instrukcje importu
- Ładowanie konfiguracji
- Przykłady implementacji agentów
- Oczekiwane wyniki w komórkach markdown

## Styl kodowania

### Konwencje dla Pythona

- **Wersja Pythona**: 3.12+
- **Styl kodowania**: Zgodny ze standardem PEP 8
- **Notatniki**: Używaj przejrzystych komórek markdown do wyjaśniania koncepcji
- **Importy**: Grupuj według biblioteki standardowej, zewnętrznych i lokalnych importów

### Konwencje dla notatników Jupyter

- Dodawaj opisowe komórki markdown przed komórkami kodu
- Dodawaj przykłady wyników w notatnikach jako odniesienie
- Używaj przejrzystych nazw zmiennych zgodnych z koncepcjami lekcji
- Zachowaj liniową kolejność wykonywania notatnika (komórka 1 → 2 → 3...)

### Organizacja plików

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```

## Budowa i wdrożenie

### Tworzenie dokumentacji

To repozytorium używa Markdown do dokumentacji:
- Pliki README.md w każdym folderze lekcji
- Główny README.md w katalogu głównym repozytorium
- Automatyczny system tłumaczeń za pomocą GitHub Actions

### Pipeline CI/CD

Znajduje się w `.github/workflows/`:

1. **co-op-translator.yml** - Automatyczne tłumaczenie na ponad 50 języków
2. **welcome-issue.yml** - Powitanie twórców nowych zgłoszeń
3. **welcome-pr.yml** - Powitanie nowych współtwórców pull requestów

### Wdrożenie

To repozytorium ma charakter edukacyjny - brak procesu wdrożeniowego. Użytkownicy:
1. Tworzą fork lub klonują repozytorium
2. Uruchamiają notatniki lokalnie lub w GitHub Codespaces
3. Uczą się, modyfikując i eksperymentując z przykładami

## Wytyczne dotyczące pull requestów

### Przed przesłaniem

1. **Przetestuj swoje zmiany:**
   - Uruchom w pełni zmienione notatniki
   - Zweryfikuj, że wszystkie komórki wykonują się bez błędów
   - Sprawdź, czy wyniki są odpowiednie

2. **Aktualizacje dokumentacji:**
   - Zaktualizuj README.md, jeśli dodajesz nowe koncepcje
   - Dodaj komentarze w notatnikach dla złożonego kodu
   - Upewnij się, że komórki markdown wyjaśniają cel

3. **Zmiany w plikach:**
   - Unikaj commitowania plików `.env` (używaj `.env.example`)
   - Nie commituj katalogów `venv/` ani `__pycache__/`
   - Zachowaj wyniki notatników, gdy demonstrują koncepcje
   - Usuń tymczasowe pliki i kopie zapasowe notatników (`*-backup.ipynb`)

### Format tytułu PR

Używaj opisowych tytułów:
- `[Lesson-XX] Dodaj nowy przykład dla <koncepcji>`
- `[Fix] Popraw literówkę w README lekcji-XX`
- `[Update] Ulepsz przykład kodu w lekcji-XX`
- `[Docs] Zaktualizuj instrukcje konfiguracji`

### Wymagane kontrole

- Notatniki powinny wykonywać się bez błędów
- Pliki README powinny być jasne i dokładne
- Przestrzegaj istniejących wzorców kodu w repozytorium
- Zachowaj spójność z innymi lekcjami

## Dodatkowe uwagi

### Częste problemy

1. **Niezgodność wersji Pythona:**
   - Upewnij się, że używasz Python 3.12+
   - Niektóre pakiety mogą nie działać z starszymi wersjami
   - Użyj `python3 -m venv`, aby wyraźnie określić wersję Pythona

2. **Zmienne środowiskowe:**
   - Zawsze twórz `.env` na podstawie `.env.example`
   - Nie commituj pliku `.env` (jest w `.gitignore`)
   - Token GitHub wymaga odpowiednich uprawnień

3. **Konflikty pakietów:**
   - Używaj świeżego wirtualnego środowiska
   - Instaluj z `requirements.txt`, a nie pojedyncze pakiety
   - Niektóre notatniki mogą wymagać dodatkowych pakietów wymienionych w ich komórkach markdown

4. **Usługi Azure:**
   - Usługi Azure AI wymagają aktywnej subskrypcji
   - Niektóre funkcje są specyficzne dla regionu
   - Ograniczenia darmowej wersji dotyczą GitHub Models

### Ścieżka nauki

Rekomendowana kolejność przechodzenia przez lekcje:
1. **00-course-setup** - Zacznij tutaj, aby skonfigurować środowisko
2. **01-intro-to-ai-agents** - Zrozum podstawy agentów AI
3. **02-explore-agentic-frameworks** - Poznaj różne frameworki
4. **03-agentic-design-patterns** - Podstawowe wzorce projektowe
5. Kontynuuj kolejne lekcje w kolejności numeracji

### Wybór frameworka

Wybierz framework w zależności od swoich celów:
- **Nauka/Prototypowanie**: Semantic Kernel + GitHub Models (darmowe)
- **Systemy wieloagentowe**: AutoGen
- **Najnowsze funkcje**: Microsoft Agent Framework (MAF)
- **Wdrożenie produkcyjne**: Azure AI Agent Service

### Uzyskiwanie pomocy

- Dołącz do [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Przejrzyj pliki README lekcji dla konkretnych wskazówek
- Sprawdź główny [README.md](./README.md) dla przeglądu kursu
- Odwiedź [Course Setup](./00-course-setup/README.md) dla szczegółowych instrukcji konfiguracji

### Współtworzenie

To otwarty projekt edukacyjny. Współtworzenie jest mile widziane:
- Ulepsz przykłady kodu
- Popraw literówki lub błędy
- Dodaj wyjaśniające komentarze
- Zaproponuj nowe tematy lekcji
- Przetłumacz na dodatkowe języki

Zobacz [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) dla bieżących potrzeb.

## Kontekst specyficzny dla projektu

### Obsługa wielu języków

To repozytorium korzysta z automatycznego systemu tłumaczeń:
- Obsługa ponad 50 języków
- Tłumaczenia w katalogach `/translations/<lang-code>/`
- Workflow GitHub Actions obsługuje aktualizacje tłumaczeń
- Pliki źródłowe są w języku angielskim w katalogu głównym repozytorium

### Struktura lekcji

Każda lekcja ma spójny schemat:
1. Miniatura wideo z linkiem
2. Treść lekcji pisemnej (README.md)
3. Przykłady kodu w różnych frameworkach
4. Cele nauki i wymagania wstępne
5. Dodatkowe zasoby edukacyjne w linkach

### Nazewnictwo przykładów kodu

Format: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Lekcja 4, Semantic Kernel
- `07-autogen.ipynb` - Lekcja 7, AutoGen
- `14-python-agent-framework.ipynb` - Lekcja 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Lekcja 14, MAF .NET

### Specjalne katalogi

- `translated_images/` - Lokalizowane obrazy dla tłumaczeń
- `images/` - Oryginalne obrazy dla treści w języku angielskim
- `.devcontainer/` - Konfiguracja kontenera deweloperskiego VS Code
- `.github/` - Workflow GitHub Actions i szablony

### Zależności

Kluczowe pakiety z `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - Framework AutoGen
- `semantic-kernel` - Framework Semantic Kernel
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Usługi Azure AI
- `azure-search-documents` - Integracja Azure AI Search
- `chromadb` - Baza danych wektorowa dla przykładów RAG
- `chainlit` - Framework UI dla czatu
- `browser_use` - Automatyzacja przeglądarki dla agentów
- `mcp[cli]` - Obsługa Model Context Protocol
- `mem0ai` - Zarządzanie pamięcią dla agentów

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.