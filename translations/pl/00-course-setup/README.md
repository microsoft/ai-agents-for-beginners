# Ustawienie kursu

## Wprowadzenie

Ta lekcja pokaże, jak uruchomić przykłady kodu z tego kursu.

## Dołącz do innych uczniów i uzyskaj pomoc

Zanim zaczniesz klonować swoje repozytorium, dołącz do [kanału Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord), aby uzyskać pomoc przy konfiguracji, zadawać pytania dotyczące kursu lub połączyć się z innymi uczniami.

## Klonowanie lub forking tego repozytorium

Aby zacząć, proszę sklonuj lub zrób fork repozytorium GitHub. To umożliwi Ci posiadanie własnej wersji materiałów kursu, dzięki czemu będziesz mógł uruchamiać, testować i modyfikować kod!

Możesz to zrobić, klikając link do <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">zrób forka repo</a>

Teraz powinieneś mieć własną wersję forka tego kursu pod następującym linkiem:

![Forked Repo](../../../translated_images/pl/forked-repo.33f27ca1901baa6a.webp)

### Płytkie klonowanie (zalecane na warsztat / Codespaces)

  >Pełne repozytorium może być duże (~3 GB), gdy pobierasz całą historię i wszystkie pliki. Jeśli bierzesz udział tylko w warsztacie lub potrzebujesz tylko kilku folderów z lekcjami, płytkie klonowanie (lub sparse clone) unika większości pobierania, ograniczając historię i/lub pomijając blobsy.

#### Szybkie płytkie klonowanie — minimalna historia, wszystkie pliki

Zamień `<your-username>` w poniższych poleceniach na URL twojego forka (lub upstream, jeśli wolisz).

Aby sklonować tylko najnowszą historię commitów (mała paczka do pobrania):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Aby sklonować konkretną gałąź:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Częściowe (sparse) klonowanie — minimalne bloby + tylko wybrane foldery

Korzysta to z częściowego klonowania i sparse-checkout (wymaga Git 2.25+ oraz zalecany nowoczesny Git z obsługą partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Przejdź do folderu repozytorium:

```bash|powershell
cd ai-agents-for-beginners
```

Następnie określ, które foldery chcesz (w przykładzie poniżej dwa foldery):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Po sklonowaniu i zweryfikowaniu plików, jeśli potrzebujesz tylko plików i chcesz zwolnić miejsce (bez historii git), usuń metadane repozytorium (💀nieodwracalne — stracisz całą funkcjonalność Git: brak commitów, pobierania, wysyłania czy dostępu do historii).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Korzystanie z GitHub Codespaces (zalecane, by uniknąć dużych lokalnych pobrań)

- Utwórz nowy Codespace dla tego repozytorium za pomocą [GitHub UI](https://github.com/codespaces).  

- W terminalu nowo utworzonego codespace uruchom jedno z powyższych poleceń shallow/sparse clone, aby pobrać tylko potrzebne foldery lekcji do przestrzeni roboczej Codespace.
- Opcjonalnie: po sklonowaniu w Codespaces usuń .git, aby odzyskać dodatkowe miejsce (zobacz polecenia usunięcia powyżej).
- Uwaga: Jeśli wolisz otworzyć repo bezpośrednio w Codespaces (bez dodatkowego klonowania), pamiętaj, że Codespaces zbuduje środowisko devcontainer i może nadal dostarczyć więcej niż potrzebujesz. Klonowanie płytkie wewnątrz świeżego Codespace daje większą kontrolę nad zużyciem dysku.

#### Wskazówki

- Zawsze zamień URL do klonowania na swój fork, jeśli chcesz edytować/commitować.
- Jeśli później potrzebujesz więcej historii lub plików, możesz je pobrać lub dostosować sparse-checkout, by uwzględnić dodatkowe foldery.

## Uruchamianie kodu

Ten kurs oferuje serię notatników Jupyter, które możesz uruchamiać, aby zdobyć praktyczne doświadczenie w budowaniu AI Agents.

Przykłady kodu używają **Microsoft Agent Framework (MAF)** z `FoundryChatClient`, który łączy się z **Microsoft Foundry Agent Service V2** (Responses API) przez **Microsoft Foundry**.

Wszystkie notatniki w Python mają etykietę `*-python-agent-framework.ipynb`.

## Wymagania

- Python 3.12+
  - **UWAGA**: Jeśli nie masz zainstalowanego Python 3.12, upewnij się, że go zainstalujesz. Następnie utwórz środowisko wirtualne za pomocą python3.12, aby mieć pewność, że odpowiednie wersje zostaną zainstalowane z pliku requirements.txt.
  
    >Przykład

    Utwórz katalog środowiska wirtualnego Python:

    ```bash|powershell
    python -m venv venv
    ```

    Następnie aktywuj środowisko venv dla:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Dla przykładowych kodów używających .NET, zainstaluj [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) lub nowszą wersję. Następnie sprawdź zainstalowaną wersję SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Wymagany do uwierzytelniania. Zainstaluj z [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Subskrypcja Azure** — Do dostępu do Microsoft Foundry i Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Projekt z wdrożonym modelem (np. `gpt-5-mini`). Zobacz [Krok 1](#krok-1-utwórz-projekt-microsoft-foundry) poniżej.

W repozytorium w katalogu głównym znajduje się plik `requirements.txt`, zawierający wszystkie potrzebne pakiety Pythona do uruchomienia przykładów kodu.

Możesz je zainstalować, uruchamiając w terminalu w katalogu głównym repozytorium:

```bash|powershell
pip install -r requirements.txt
```

Zalecamy tworzenie wirtualnego środowiska Pythona, aby uniknąć konfliktów i problemów.

## Konfiguracja VSCode

Upewnij się, że używasz właściwej wersji Pythona w VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Konfiguracja Microsoft Foundry i Microsoft Foundry Agent Service

### Krok 1: Utwórz projekt Microsoft Foundry

Potrzebujesz **hubu** i **projektu** Microsoft Foundry z wdrożonym modelem, aby uruchomić notatniki.

1. Przejdź do [ai.azure.com](https://ai.azure.com) i zaloguj się na swoje konto Azure.
2. Utwórz **hub** (lub użyj istniejącego). Zobacz: [Przegląd zasobów hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. W hubie utwórz **projekt**.
4. Wdróż model (np. `gpt-5-mini`) z **Models + Endpoints** → **Deploy model**.

### Krok 2: Uzyskaj endpoint projektu i nazwę wdrożenia modelu

W portalu projektu Microsoft Foundry:

- **Endpoint projektu** — Przejdź do strony **Overview** i skopiuj URL endpointu.

![Project Connection String](../../../translated_images/pl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Nazwa wdrożenia modelu** — Przejdź do **Models + Endpoints**, wybierz wdrożony model i zanotuj **Deployment name** (np. `gpt-5-mini`).

### Krok 3: Zaloguj się do Azure przez `az login`

Wszystkie notatniki używają **`AzureCliCredential`** do uwierzytelniania — brak potrzeby zarządzania kluczami API. Wymaga to zalogowania się przez Azure CLI.

1. **Zainstaluj Azure CLI**, jeśli jeszcze nie masz: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Zaloguj się**, uruchamiając:

    ```bash|powershell
    az login
    ```

    Lub jeśli jesteś w zdalnym/Codespace bez przeglądarki:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Wybierz subskrypcję**, jeśli zostaniesz o to poproszony — wybierz tę, która zawiera twój projekt Foundry.

4. **Sprawdź**, czy jesteś zalogowany:

    ```bash|powershell
    az account show
    ```

> **Dlaczego `az login`?** Notatniki uwierzytelniają się za pomocą `AzureCliCredential` z pakietu `azure-identity`. Oznacza to, że sesja Azure CLI dostarcza poświadczenia — brak kluczy API lub sekretów w pliku `.env`. To [najlepsza praktyka bezpieczeństwa](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Krok 4: Utwórz plik `.env`

Skopiuj plik przykładowy:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Otwórz `.env` i uzupełnij te dwie wartości:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal Foundry → twój projekt → strona **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal Foundry → **Models + Endpoints** → nazwa wdrożonego modelu |

To wszystko na większość lekcji! Notatniki będą się automatycznie uwierzytelniać poprzez twoją sesję `az login`.

### Krok 5: Zainstaluj zależności Pythona

```bash|powershell
pip install -r requirements.txt
```

Zalecamy uruchomić to wewnątrz wcześniej utworzonego środowiska wirtualnego.

## Dodatkowa konfiguracja dla lekcji 5 (Agentic RAG)

Lekcja 5 wykorzystuje **Azure AI Search** do retrieval-augmented generation. Jeśli planujesz uruchomić tę lekcję, dodaj zmienne do pliku `.env`:

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal Azure → twój zasób **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Portal Azure → twój zasób **Azure AI Search** → **Settings** → **Keys** → klucz administratora główny |

## Dodatkowa konfiguracja dla lekcji korzystających bezpośrednio z Azure OpenAI (Lekcje 6 i 8)

Niektóre notatniki z lekcji 6 i 8 korzystają bezpośrednio z **Azure OpenAI** (używając **Responses API**) zamiast przez projekt Microsoft Foundry. Te próbki wcześniej korzystały z modeli GitHub, które są wycofywane (koniec wsparcia w lipcu 2026) i nie obsługują Responses API. Jeśli zamierzasz uruchomić te próbki, dodaj zmienne do pliku `.env`:

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal Azure → twój zasób **Azure OpenAI** → **Keys and Endpoint** → Endpoint (np. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Nazwa wdrożonego modelu (np. `gpt-5-mini`) wspierającego Responses API |
| `AZURE_OPENAI_API_KEY` | Opcjonalne — tylko jeśli używasz uwierzytelniania na bazie klucza zamiast `az login` / Entra ID |

> Responses API korzysta ze stabilnego endpointu `/openai/v1/`, więc `api-version` nie jest wymagany. Zaloguj się przez `az login`, aby używać bezkluczowego uwierzytelniania Entra ID.

## Alternatywny dostawca: MiniMax (kompatybilny z OpenAI)

[MiniMax](https://platform.minimaxi.com/) oferuje modele z dużym kontekstem (do 204K tokenów) przez API kompatybilne z OpenAI. Ponieważ `OpenAIChatClient` z Microsoft Agent Framework działa z każdym endpointem kompatybilnym z OpenAI, możesz użyć MiniMax jako zamiennika dla Azure OpenAI lub OpenAI.

Dodaj te zmienne do swojego pliku `.env`:

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → Klucze API |
| `MINIMAX_BASE_URL` | Użyj `https://api.minimax.io/v1` (wartość domyślna) |
| `MINIMAX_MODEL_ID` | Nazwa modelu do użycia (np. `MiniMax-M3`) |

**Przykładowe modele**: `MiniMax-M3` (zalecany), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (szybsze odpowiedzi). Nazwy modeli i ich dostępność mogą się zmieniać, a dostęp do konkretnego modelu może zależeć od twojego konta lub regionu — sprawdź [MiniMax Platform](https://platform.minimaxi.com/) po aktualną listę. Jeśli `MiniMax-M3` nie jest dostępny dla twojego konta, ustaw `MINIMAX_MODEL_ID` na model, do którego masz dostęp (np. `MiniMax-M2.7`).

Próbki używające `OpenAIChatClient` (np. workflow rezerwacji hotelu z lekcji 14) automatycznie wykryją i wykorzystają konfigurację MiniMax, gdy zmienna `MINIMAX_API_KEY` jest ustawiona.

## Alternatywny dostawca: Foundry Local (uruchamiaj modele lokalnie)

[Foundry Local](https://foundrylocal.ai) to lekkie środowisko uruchomieniowe, które pobiera, zarządza i udostępnia modele językowe **całkowicie na twoim komputerze**, przez API kompatybilne z OpenAI — bez chmury, subskrypcji Azure i kluczy API. To świetna opcja do pracy offline, eksperymentowania bez kosztów chmury lub przechowywania danych lokalnie.

Ponieważ `OpenAIChatClient` z Microsoft Agent Framework działa z każdym endpointem kompatybilnym z OpenAI, Foundry Local jest lokalnym zamiennikiem dla Azure OpenAI.

**1. Zainstaluj Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Pobierz i uruchom model** (to także uruchamia lokalną usługę):

```bash
foundry model list          # zobacz dostępne modele
foundry model run phi-4-mini
```

**3. Zainstaluj Python SDK** do wykrywania lokalnego endpointu:

```bash
pip install foundry-local-sdk
```

**4. Skieruj Microsoft Agent Framework na swój lokalny model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Pobiera (jeśli potrzebne) i udostępnia model lokalnie, a następnie wykrywa punkt końcowy/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # np. http://localhost:<port>/v1
    api_key=manager.api_key,        # zawsze "nie wymagane" dla Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Uwaga:** Foundry Local udostępnia endpoint kompatybilny z OpenAI **Chat Completions**. Używaj go do lokalnego rozwoju i scenariuszy offline. Dla pełnego zestawu funkcji **Responses API** (stanowe konwersacje, głęboka orkiestracja narzędzi, rozwój agentów) kieruj się na **Azure OpenAI** lub projekt **Microsoft Foundry** jak pokazano w lekcjach. Zobacz [dokumentację Foundry Local](https://foundrylocal.ai) po aktualny katalog modeli i wsparcie platformy.

## Dodatkowa konfiguracja do lekcji 8 (workflow Bing Grounding)


Notes o warunkowym przepływie pracy w lekcji 8 używają **Bing grounding** za pośrednictwem Microsoft Foundry. Jeśli planujesz uruchomić ten przykład, dodaj tę zmienną do swojego pliku `.env`:

| Zmienna | Gdzie ją znaleźć |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal Microsoft Foundry → twój projekt → **Zarządzanie** → **Połączone zasoby** → twoje połączenie Bing → skopiuj ID połączenia |

## Rozwiązywanie problemów

### Błędy weryfikacji certyfikatów SSL na macOS

Jeśli używasz macOS i napotkasz błędy takie jak:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

To jest znany problem z Pythonem na macOS, gdzie systemowe certyfikaty SSL nie są automatycznie zaufane. Wypróbuj poniższe rozwiązania w kolejności:

**Opcja 1: Uruchom skrypt instalacji certyfikatów Pythona (zalecane)**

```bash
# Zamień 3.XX na zainstalowaną wersję Pythona (np. 3.12 lub 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opcja 2: Użyj `connection_verify=False` w swoim notesie (dotyczy tylko notesów GitHub Models)**

W notesie z Lekcji 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) jest już zawarte zakomentowane obejście. Odkomentuj `connection_verify=False` podczas tworzenia klienta:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Wyłącz weryfikację SSL, jeśli napotkasz błędy certyfikatu
)
```

> **⚠️ Ostrzeżenie:** Wyłączenie weryfikacji SSL (`connection_verify=False`) zmniejsza bezpieczeństwo pomijając walidację certyfikatu. Używaj tego tylko tymczasowo podczas rozwoju, nigdy w środowisku produkcyjnym.

**Opcja 3: Zainstaluj i użyj `truststore`**

```bash
pip install truststore
```

Następnie dodaj poniższe na początku swojego notesu lub skryptu przed wykonywaniem jakichkolwiek wywołań sieciowych:

```python
import truststore
truststore.inject_into_ssl()
```

## Utknąłeś gdzieś?

Jeśli masz jakieś problemy z uruchomieniem tego środowiska, dołącz do naszej <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> lub <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">zgłoś problem</a>.

## Następna lekcja

Jesteś teraz gotowy, aby uruchomić kod tego kursu. Powodzenia w dalszej nauce świata AI Agentów! 

[Wprowadzenie do AI Agentów i przypadków użycia agentów](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->